---
title: "ADC Functional Safety Mechanisms on S32K5xx (SARADC / SINC / LPCMP / TEMPSENSE)"
---

> **Target platform**: NXP S32K5xx family (S32K566, etc.) — SARADC_0 / SARADC_1 / LPE_SARADC, SINC, LPE_LPCMP 0–2, TEMPSENSE
>
> **Sources**: NXP S32K5 Foundation Training — *Analog (ADC - SINC - LPCMP - TEMPSENSE)* and *Safety* (AAES AMCU Systems and Applications); S32K5xx Reference Manual **Rev.2**, Chapter 63 *Safety Overview* (2026-06-01); S32K5 RTD ADC Driver User Manual (UM85ADCASRR23-11); S32K5 Safety Manual (SEooC documentation)
>
> **Version note (2026-10-15)**: the Foundation training material is based on **S32K5RM Rev2 DraftE** and **S32K5xx DS Rev1 DraftE**; RM citations are taken from the released Rev.2 Chapter 63. Every register name, bitfield and default value must be cross-checked against the released Reference Manual and Safety Manual of the specific derivative before production.
>
> **Addendum (2026-10-15)**: new Chapter 7 "VCU accelerator pedal application: failure scenarios and extra ADC-side mechanisms" — using dual-channel pedal acquisition as an example, it provides an F1–F10 failure-scenario list and the mapping between ADC hardware-layer and VCU software-layer mechanisms; application-layer thresholds are engineering convention examples and must be calibrated per project HARA.
>
> **Related reading** (same directory): [R52/M7 dual-OS sleep design](../power_designs/S32K5_R52_M7_Sleep_Design_EN.md) (power domains PD0/PD1/PD2) and [MPU memory protection design](../mpu_concept/S32K5_R52_M7_MPU_Design_EN.md) (ASIL partition isolation).

---

## 1. Why the ADC needs functional safety design

A typical safety chain in the ISO 26262 conceptual safety architecture looks like this:

```
Sensor → signal conditioning → ADC → processing unit → actuator
```

The ADC is the **only gateway from the analog world into the digital world**. A wrong conversion result contaminates both the upstream sensor interpretation and the downstream control decision, and the application usually cannot distinguish "the real signal is out of range" from "the ADC is broken". This is why NXP lists the **ADC self-test alongside LBIST/MBIST as a specific BIST** in RM Chapter 63 *Safety Overview*:

> "The implementation of the ADC self-test serves a special purpose that is important for a safety-related usage of the ADC. This self-test provides test steps that permit an **independent assessment of the elements of the ADC** integrated within this chip."
> `[Source: S32K5xx RM Rev.2, Ch.63 §63.7.2]`

S32K5 is developed as an ISO 26262 **SEooC (Safety Element out of Context)** targeting integrity levels up to **ASIL D**. For the ADC, the safety mechanisms fall into three layers, and this article follows that structure:

| Layer | Mechanism | Question answered |
| --- | --- | --- |
| Accuracy | Calibration | "Is the conversion accurate?" — compensates manufacturing spread and drift |
| Self-test | Self-Test algorithms S/O/C + watchdogs | "Is the ADC element broken?" — permanent fault detection |
| Monitoring | Analog watchdog (AWD), SINC detectors, TEMPSENSE thresholds | "Is this conversion result trustworthy?" — runtime data plausibility |

---

## 2. Analog subsystem overview (safety view)

| Module | Instances | Role | Safety-relevant features |
| --- | --- | --- | --- |
| SARADC | SARADC_0, SARADC_1, LPE_SARADC | 14-bit SAR conversion, up to 2 MSa/s | **Self-Test (algorithms S/O/C) + self-test watchdog timer**, 4 analog watchdogs per instance, internal bandgap reference channel |
| SINC | SINC (1 instance) | Decimation filter for external Σ-Δ modulator bitstreams | **SCD short/open-circuit detector, CAD clock-absence detector, ZCD zero-cross detector**, break signal outputs |
| LPCMP | LPE_LPCMP_0/1/2 | Low-power comparators (CMP + 8-bit DAC + ANMUX) | Round-Robin trigger in STANDBY, programmable hysteresis, window mode, wake-up comparison |
| TEMPSENSE | TEMPSENSE (1 instance) | On-chip high-accuracy temperature sensing (BJT + Σ-Δ + decimation + calibration engine) | **Threshold comparators in both normal and secure address spaces**, multi-level under/over-temperature and panic thresholds |

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 380" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>S32K5 analog acquisition chain — functional safety view</title>
<desc>Left to right: sensor, signal conditioning, SARADC/SINC acquisition, processing unit, actuator. Three safety layers (calibration, self-test, runtime monitoring) attach to the chain, and fault notifications converge into the VFCCU, which converts them into fault reactions and safe-state requests.</desc>
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="500" fill="#2C2C2A">S32K5 Analog Acquisition Chain — Functional Safety View</text>
<rect x="20" y="45" width="110" height="56" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="75" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Sensor</text>
<text x="75" y="86" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">analog input</text>
<rect x="160" y="45" width="110" height="56" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="215" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Conditioning</text>
<text x="215" y="86" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">filter / gain / ref</text>
<rect x="300" y="45" width="130" height="56" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="365" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">SARADC / SINC</text>
<text x="365" y="86" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">14-bit SAR · Σ-Δ decimation</text>
<rect x="460" y="45" width="100" height="56" rx="8" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="510" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">Processing</text>
<text x="510" y="86" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">M7 / R52</text>
<rect x="590" y="45" width="80" height="56" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="630" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Actuator</text>
<text x="630" y="86" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">output stage</text>
<path d="M130 73 L158 73" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M270 73 L298 73" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M430 73 L458 73" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M560 73 L588 73" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="255" y="118" width="220" height="88" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="365" y="138" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">Accuracy layer: Calibration</text>
<text x="365" y="156" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">offset / gain / capacitor mismatch</text>
<text x="365" y="172" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">preserved across functional reset;</text>
<text x="365" y="188" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">mandatory after destructive reset</text>
<path d="M365 118 L365 105" fill="none" stroke="#378ADD" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="255" y="222" width="220" height="88" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="365" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">Self-test layer: Self-Test</text>
<text x="365" y="260" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">Algorithm S supply / O offset / C capacitor</text>
<text x="365" y="276" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">per-algorithm watchdog + self-test AWD</text>
<text x="365" y="292" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">error bit + failing step number</text>
<path d="M365 222 L365 209" fill="none" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="20" y="222" width="210" height="88" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="125" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">Monitoring layer: runtime</text>
<text x="125" y="260" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">analog watchdog AWD (4 per instance)</text>
<text x="125" y="276" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">SINC: SCD / CAD / ZCD</text>
<text x="125" y="292" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">TEMPSENSE: thresholds + panic</text>
<rect x="505" y="222" width="155" height="88" rx="10" fill="#FAEEDC" stroke="#BA8A29" stroke-width="0.5"/>
<text x="582" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#433422" dominant-baseline="central">VFCCU fault mgmt</text>
<text x="582" y="260" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">5×LVFCCU + 1×CVFCCU</text>
<text x="582" y="276" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">interrupt / reset / EOUT</text>
<text x="582" y="292" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">→ safe state</text>
<path d="M230 266 L253 266" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M475 266 L503 266" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<text x="20" y="340" font-size="11" fill="#5F5E5A">Main chain: sensor → SARADC/SINC → processing → actuator. Three safety layers attach to it; fault notifications converge into the VFCCU.</text>
</svg>
</figure>

> **Power-domain note**: per the PD0/PD1/PD2 split (see the sleep design article), LPE-side analog peripherals (LPE_SARADC, LPE_LPCMP 0–2) belong to **PD1**, while the platform SARADC_0 / SARADC_1 are powered down together with **PD2**. For ADC safety monitoring in LPRUN scenarios, only the LPE-side instances are usable. `[Derived from the power-domain table; re-verify against the RM power chapter]`

---

## 3. SARADC hardware basics

### 3.1 Instances and channel model

| Item | SARADC_0 | SARADC_1 | LPE_SARADC |
| --- | --- | --- | --- |
| BCTU trigger support | Yes | Yes | Yes |
| DMA support | Yes | Yes | Yes |
| Hardware channel interleaving | Yes | Yes | Yes |
| Number of analog watchdogs | **4** | **4** | **4** |
| Number of triggers | 51 | 51 | 51 |
| External channels | 32 | 32 | 32 |
| Extended channels (external MUX) | 32 | 32 | 32 |

- The chip provides **96 standard analog inputs**, plus support for **96 extended inputs** through external multiplexers.
- Resolution up to **14-bit**; conversion results are stored in **16-bit-wide** data registers.
- Sampling rate up to **2 MSa/s**; an internal **bandgap voltage reference channel** is available (one of the Algorithm S measurement targets).
- Each instance contains P-SARADC (Plus) and M-SARADC (Minus) SAR engines; differential mode uses both cooperatively.

> **Interleaving pitfall**: some ADC channels are driven by multiple pads, selected via `GPR_1.GPR_RWF_0[ADC_CHxx]` (e.g. `ADC1_X0_P16` defaults to GPIO 322, switchable to GPIO 240). Changing interleaving changes the hardware topology — freeze it together with the schematic during safety review.

### 3.2 Conversion formula and three trigger modes

$$
\text{Digitalcode}=\frac{V_{in}}{(VREFH-VREFL)}\times\left(2^{RESOLUTION}-1\right)
$$

| Mode | Trigger | Channel select | Behavior |
| --- | --- | --- | --- |
| Normal | SW / HW | `NCM0/1/2` | One-Shot or Scan (continuous loop); converts sequentially from the lowest to the highest channel number |
| Injected | SW / HW | `JCM0/1/2` | **One-Shot only**; suspends the running Normal chain, then resumes from the suspended channel after the injected chain completes |
| BCTU | BCTU hardware | channel number delivered by BCTU | single-channel conversion; result returned on the data bus with `Next command` / `End of conversion` signals; enable via `MC[CTUEN]=1` |

> In Normal mode, if all `NCMn` fields are 0 but a start trigger arrives, hardware sets `IS[ECH]` and raises the End of Chain interrupt — a natural sentinel for "conversion chain configuration lost". Hook it in safety applications.

### 3.3 Averaging

- Calibration path: up to **1024** conversions averaged.
- Input data path: up to **32** conversions averaged.

Averaging improves effective resolution and noise immunity — an **accuracy-layer** technique. It cannot detect element failures; do not confuse it with self-test.

---

## 4. Calibration: accuracy compensation, not a safety mechanism

**Positioning first**: calibration compensates **offset / gain / capacitor mismatch** caused by manufacturing spread and operating conditions (temperature, supply). Its goal is "accurate". An ISO 26262 safety mechanism answers "is it broken" — that is the job of Self-Test. The two are complementary and not interchangeable.

### 4.1 Hardware rules (Foundation Training)

- A **known reference voltage** is sampled and converted under controlled conditions to derive correction values for offset, gain and capacitor mismatch.
- It **must be executed as part of SARADC setup** to achieve best accuracy.
- **Two resets affect calibration very differently**:
  - **Functional reset**: all registers return to defaults **except the calibration registers** — no recalibration needed.
  - **Destructive reset**: calibration **must be re-run after every occurrence**.
- It is recommended to re-run calibration at runtime **whenever operating conditions change** (large temperature swing, supply variation, etc.).

### 4.2 RTD driver API

```c
/* Configuration time (AutosarExt container):
 *   AdcEnableCalibration = true
 *   AdcEnableAsyncCalibration = true   (optional, async mode)
 *   AdcCalibrationPrescale             (calibration clock input select)
 */
Adc_Init(&AdcConfigSet);        /* Init does NOT start calibration automatically */
Adc_Calibrate();                /* call explicitly when no conversion is ongoing */

/* Asynchronous calibration: two calls */
Adc_Calibrate();                /* 1st: starts calibration; other tasks may run */
/* ... no other ADC API except Adc_Deinit() allowed meanwhile ... */
Adc_Calibrate();                /* 2nd: blocking wait for completion, restores registers */
```

> **DET error**: `Adc_Calibrate()` returns `ADC_E_TIMEOUT` on calibration timeout.
>
> **Coupling with self-test**: **once Self-Test is enabled, calibration must be executed first** (Foundation Training: "It is mandatory to run calibration procedure if Self-Test is enabled."). The expected values of the self-test algorithms are defined on a calibrated device; skipping calibration causes false self-test failures.

---

## 5. Self-Test: deep dive into the three algorithms

The SARADC automatically checks its own elements and flags errors. Self-test inputs are **internal known quantities** (references, internal nodes) rather than external analog signals — that is what makes it a truly independent assessment.

### 5.1 Algorithm overview

| Algorithm | Name | Measured target | Sequence |
| --- | --- | --- | --- |
| **S** | Supply Self-Test | Bandgap voltage `VBG`, supply `AVDD`, `VREFH`, `VREFL`, `VREFH/2`, `VREFH/3`, `2×VREFH/3` | **7-step atomic sequence** |
| **O** | Offset Self-Test | Comparator offset | single sequence |
| **C** | Capacitor Self-Test | Capacitor array: **33 MSB + 17 ISB + 17 LSB**, executed for **each of P-SARADC and M-SARADC** | multi-step **atomic** execution |

### 5.2 Self-test analog watchdog

- The digital interface provides **independent watchdog register sets per algorithm**, checking whether each self-test conversion result falls inside that algorithm's guard area.
- After **each step** of an algorithm, the result is compared against the upper/lower thresholds. On violation:
  - the corresponding **error bit is set**;
  - the **step number** where the error occurred is recorded — troubleshooting lands on the failing step, not just "self-test failed".

### 5.3 Self-test watchdog timer

- Monitors the **execution sequence** of the self-test algorithm and verifies completion within a **safe time**.
- Each algorithm has an **independent** watchdog timer.
- The safe time value is programmed in `STBR[WDT]`.
- Timing window: for Algorithm S, from **Step 0 start (including interleaved normal-chain conversions) until the next Step 0 start**; a timeout flags a sequence fault.

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 330" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>SARADC Self-Test: three algorithms and dual watchdogs</title>
<desc>Center: the SARADC self-test engine. Three branches: Algorithm S (7-step supply measurement), Algorithm O (comparator offset), Algorithm C (MSB/ISB/LSB capacitor array). Each algorithm has an independent watchdog timer (safe time in STBR[WDT]) and an independent self-test analog watchdog (error bit plus failing step number on violation). Self-test errors are reported through the self-test interrupt.</desc>
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="340" y="22" text-anchor="middle" font-size="14" font-weight="500" fill="#2C2C2A">SARADC Self-Test: Three Algorithms + Dual Watchdogs</text>
<rect x="240" y="130" width="200" height="70" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="340" y="155" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">SARADC self-test engine</text>
<text x="340" y="173" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">internal known inputs</text>
<text x="340" y="190" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">(bandgap / capacitor array)</text>
<rect x="30" y="40" width="185" height="66" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="122" y="60" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">Algorithm S · Supply</text>
<text x="122" y="78" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">7 atomic steps: VBG / AVDD /</text>
<text x="122" y="94" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">VREFH / VREFL / 1/2 / 1/3 / 2/3</text>
<rect x="247" y="40" width="185" height="66" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="340" y="60" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">Algorithm O · Offset</text>
<text x="340" y="78" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">single sequence</text>
<text x="340" y="94" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">comparator offset</text>
<rect x="465" y="40" width="185" height="66" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="557" y="60" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">Algorithm C · Capacitor</text>
<text x="557" y="78" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">33 MSB + 17 ISB + 17 LSB</text>
<text x="557" y="94" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">atomic per P / M engine</text>
<path d="M200 73 L240 140" fill="none" stroke="#378ADD" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M340 106 L340 128" fill="none" stroke="#378ADD" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M480 73 L440 140" fill="none" stroke="#378ADD" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="30" y="222" width="185" height="76" rx="8" fill="#FAEEDC" stroke="#BA8A29" stroke-width="0.5"/>
<text x="122" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#433422" dominant-baseline="central">Watchdog timers ×3</text>
<text x="122" y="260" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">independent per algorithm;</text>
<text x="122" y="276" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">verifies completion within</text>
<text x="122" y="292" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">safe time (STBR[WDT])</text>
<rect x="247" y="222" width="185" height="76" rx="8" fill="#FAEEDC" stroke="#BA8A29" stroke-width="0.5"/>
<text x="340" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#433422" dominant-baseline="central">Self-test AWDs ×3</text>
<text x="340" y="260" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">per-algorithm guard area</text>
<text x="340" y="276" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">step-by-step compare; error bit</text>
<text x="340" y="292" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">+ failing step number</text>
<rect x="465" y="222" width="185" height="76" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="557" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Self-test interrupt</text>
<text x="557" y="260" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">reports to application</text>
<text x="557" y="276" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">→ handled per fault-reaction</text>
<text x="557" y="292" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">policy (see chapter 9)</text>
<path d="M122 222 L122 203" fill="none" stroke="#BA8A29" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M340 222 L340 203" fill="none" stroke="#BA8A29" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M440 165 L500 220" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#ar)"/>
</svg>
</figure>

### 5.4 RTD driver API

```c
/* Configuration time: AdcEnableSelfTest = true (AutosarExt)
 *         AdcSelfTestInputSamplingAlgCVal  default 24 (range 1–255)
 *         AdcSelfTestInputSamplingAlgSVal  sampling phase duration for Algorithm S
 */
Adc_SelfTest();   /* call explicitly when no conversion is ongoing; ADC_E_TIMEOUT on timeout */
```

> The `AdcSelfTestInputSamplingConfiguration` container defines the **sampling phase duration of test conversions for Algorithms C and S** — it directly affects self-test accuracy. Read the corresponding RM chapter before changing defaults; do not guess values.

---

## 6. Analog watchdog: runtime data plausibility monitoring

Self-test answers "is the element broken"; the analog watchdog answers "**is this particular conversion result trustworthy**". Different time scales, different fault models — both are mandatory.

### 6.1 Hardware mechanism

- **4 analog watchdogs per instance**, each holding an upper threshold `THRH` and a lower threshold `THRL`.
- After conversion of the selected channel, the result is compared against both thresholds; a violation raises a threshold-violation interrupt:

| `WTIS[WDGnH]` | `WTIS[WDGnL]` | Converted data |
| --- | --- | --- |
| 1 | 0 | data > `THRH` |
| 0 | 1 | data < `THRL` |
| 0 | 0 | `THRL` ≤ data ≤ `THRH` (normal) |
| 1 | 1 | `THRH` < data and `THRL` > data (invalid combination) |

- Each channel can be enabled independently via the `CWEN` field; `CWSEL_n` selects the owning watchdog.

### 6.2 RTD driver API

```c
/* Configuration time: AdcEnableWatchdogFunctionality = true
 *         per AdcChannel: AdcEnableThresholds = true,
 *         AdcThresholdRegister (THRH/THRL) and AdcWdogNotification
 */
Adc_ConfigureThreshold(/* change thresholds at runtime */);
Adc_EnableWdgNotification(Channel);   /* enable watchdog event notification */
Adc_DisableWdgNotification(Channel);  /* disable */
```

> ⚠️ **Driver limitation (RTD ADC UM §3.5, verbatim)**: "**Watchdog threshold functionality not validated**." — the threshold watchdog is **not fully validated** at driver level. If the safety case relies on the AWD, run supplementary validation and error analysis on your own platform.
>
> Two further limitations in the same section: DMA functionality **not validated** on Adc0/Adc1; **LPE_BCTU not available** in Design Studio; interrupt/DMA data transfer **not validated** on Cortex-M4.

---

## 7. VCU accelerator pedal application: failure scenarios and extra ADC-side mechanisms

Chapters 1–6 covered the mechanisms of "the ADC itself"; this chapter stress-tests them in the most typical ASIL application — the **accelerator pedal (APPS, Accelerator Pedal Position Sensor)**. Three reasons for choosing it:

1. **Fully analog signal chain**: potentiometer → harness → ADC. Application software has little leverage, so detection responsibility shifts forward onto the ADC and signal conditioning.
2. **Failure equals unintended torque**: a wrong pedal signal maps directly to "unintended acceleration / loss of drive" — one of the highest-ranked safety goals on the VCU side (actual ASIL per project HARA, typically C/D).
3. **Dual redundancy is industry practice**: the APPS1/APPS2 potentiometers make "cross-checking the two conversion results" a hard requirement — and **whether the two channels are sampled in-step is decided by ADC configuration**.

> This chapter focuses on **analog potentiometer pedals**. With digital sensors such as SENT, part of the safety mechanism (CRC, rolling counter) is provided sensor-side; that chain is out of scope here.

### 7.1 Application signal chain and safety goal

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 448" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>VCU accelerator pedal dual-channel chain and failure-scenario detection mapping</title>
<desc>The main chain shows the pedal mechanism driving the APPS1/APPS2 potentiometers, through harness and conditioning into in-step CH0/CH1 conversion on SARADC_0, then into the VCU software check layer and torque arbitration. Two panels below list, respectively, the ADC hardware-layer mechanisms and the VCU software-layer mechanisms covering failure scenarios F1 through F10, converging on limp-home degradation and the safe state.</desc>
<defs><marker id="arpe" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="340" y="22" text-anchor="middle" font-size="13" font-weight="500" fill="#2C2C2A">VCU accelerator pedal dual-channel chain — failure scenarios vs. detection mechanisms</text>
<rect x="12" y="62" width="88" height="52" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="56" y="80" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Accelerator</text>
<text x="56" y="97" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">pedal mechanism</text>
<rect x="118" y="45" width="104" height="44" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="170" y="61" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">APPS1 pot.</text>
<text x="170" y="77" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">0.5 V → 4.5 V</text>
<rect x="118" y="97" width="104" height="44" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="170" y="113" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">APPS2 pot.</text>
<text x="170" y="129" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">complementary</text>
<rect x="240" y="62" width="88" height="52" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="284" y="80" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Harness + cond.</text>
<text x="284" y="97" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">pull-up/dn · filter</text>
<rect x="346" y="55" width="112" height="66" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="402" y="80" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">SARADC_0</text>
<text x="402" y="97" text-anchor="middle" font-size="10.5" fill="#185FA5" dominant-baseline="central">CH0/CH1 in-step</text>
<text x="402" y="112" text-anchor="middle" font-size="10.5" fill="#185FA5" dominant-baseline="central">14-bit · AWD ×4</text>
<rect x="476" y="55" width="92" height="66" rx="8" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="522" y="78" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">VCU software checks</text>
<text x="522" y="95" text-anchor="middle" font-size="10.5" fill="#534AB7" dominant-baseline="central">plausibility · stuck</text>
<text x="522" y="111" text-anchor="middle" font-size="10.5" fill="#534AB7" dominant-baseline="central">gradient · freshness</text>
<rect x="586" y="62" width="82" height="52" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="627" y="80" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Torque arbitration</text>
<text x="627" y="96" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">motor / MCU</text>
<path d="M100 78 L116 66" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<path d="M100 98 L116 118" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<path d="M222 70 L238 80" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<path d="M222 116 L238 96" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<path d="M328 88 L344 88" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<path d="M458 88 L474 88" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<path d="M568 88 L584 88" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<rect x="30" y="175" width="280" height="160" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="170" y="197" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">ADC hardware layer</text>
<text x="44" y="214" font-size="10.5" fill="#185FA5">Self-Test at power-up → element faults</text>
<text x="44" y="232" font-size="10.5" fill="#185FA5">AWD out-of-range → F3 GND / F4 VBAT short</text>
<text x="44" y="250" font-size="10.5" fill="#185FA5">　　　　　　　 F5 open / F6 over-range</text>
<text x="44" y="268" font-size="10.5" fill="#185FA5">Averaging → F7 spikes</text>
<text x="44" y="286" font-size="10.5" fill="#185FA5">scan back-to-back / BCTU → F8 in-step</text>
<text x="44" y="304" font-size="10.5" fill="#185FA5">conv-done IRQ / watermark → F9 freshness</text>
<text x="44" y="322" font-size="10.5" fill="#185FA5">ratiometric wiring (VREFH tracks supply) → F10</text>
<rect x="370" y="175" width="280" height="160" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="510" y="195" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">VCU software layer</text>
<text x="510" y="211" text-anchor="middle" font-size="10" fill="#534AB7" dominant-baseline="central">(app level; needs ADC freshness + in-step)</text>
<text x="384" y="229" font-size="10.5" fill="#534AB7">plausibility cross-check → F2</text>
<text x="384" y="247" font-size="10.5" fill="#534AB7">stuck monitor (deadband + time) → F1</text>
<text x="384" y="265" font-size="10.5" fill="#534AB7">gradient limit + rolling counter → F7/F9</text>
<text x="384" y="283" font-size="10.5" fill="#534AB7">ratiometric check + periodic recal → F10</text>
<text x="384" y="301" font-size="10.5" fill="#534AB7">zero-pos boot check · pedal/brake interlock</text>
<text x="384" y="319" font-size="10.5" fill="#534AB7">degradation: limp home → safe state</text>
<path d="M380 121 L305 173" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<path d="M424 121 L497 173" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<rect x="30" y="362" width="620" height="52" rx="10" fill="#FAEEDC" stroke="#BA8A29" stroke-width="0.5"/>
<text x="340" y="383" text-anchor="middle" font-size="12" font-weight="500" fill="#433422" dominant-baseline="central">Fault reaction: limp home degradation (torque limit / idle) → safe state</text>
<text x="340" y="401" text-anchor="middle" font-size="10.5" fill="#633806" dominant-baseline="central">Severity classes and EOUT / reset actions: see Chapter 10 (VFCCU); recovery needs plausibility pass</text>
<path d="M170 335 L170 360" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<path d="M510 335 L510 360" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arpe)"/>
<text x="340" y="436" text-anchor="middle" font-size="10.5" fill="#5F5E5A">Fully analog chain: F1–F10 are covered jointly by the ADC hardware layer and the VCU software layer.</text>
</svg>
</figure>

- The mechanical pedal drives **two potentiometers**: range typically 0.5 V–4.5 V with **opposite slopes** (complementary design — one channel 0.5→4.5 V, the other 4.5→0.5 V) for easy cross-checking.
- The VCU samples both channels every **5–10 ms**, resolves pedal travel and feeds torque arbitration.
- The pull-up/pull-down resistors on the harness are not decoration — they decide **which distinguishable level** an open circuit or short presents to the ADC (see F5 in 7.2).
- Safety goal (example): "prevent torque exceeding driver intent"; no single-point fault may cause this violation.

### 7.2 Failure scenario list (FMEA view)

| # | Scenario | Typical physical cause | Hazardous behavior | Primary detection layer |
| --- | --- | --- | --- | --- |
| F1 | stuck signal | pot track wear, contact oxidation, loose connector | pedal position does not follow the physical pedal | software (freshness + time window) |
| F2 | channel mismatch | one channel aged, partial open, EMC on one channel | the two channels resolve different torque | software plausibility (needs in-step ADC sampling) |
| F3 | short to GND | harness damage, water in connector | reading ≈ 0 → false full-release / full-press | ADC: AWD |
| F4 | short to supply | harness shorted to VBAT / 5 V | reading ≈ full scale | ADC: AWD |
| F5 | open circuit | cracked solder, backed-out terminal | floating drift, or clamped by pull-up/down | ADC: AWD + conditioning criteria |
| F6 | over-range | sensor over-travel, mounting error | reading beyond physical travel | ADC: AWD |
| F7 | spikes | EMC coupling, ground bounce, reference ripple | single-cycle spikes, torque jitter | ADC averaging/filtering + software gradient limit |
| F8 | non-in-step sampling | two independent triggers, interrupt jitter | channels "disagree" during fast pedal motion | ADC trigger/scan configuration |
| F9 | stale data | DMA stall, lost interrupt, group not restarted | torque computed from an old position | software freshness (needs ADC completion flags) |
| F10 | ground offset / reference drift | single-ended wiring, ground bounce, supply droop | systematic bias, zero-position criteria fail | ratiometric wiring + calibration |

### 7.3 Mapping to ADC-side mechanisms

| Failure | ADC / hardware mechanism | RTD driver hook | Note |
| --- | --- | --- | --- |
| F1 | periodic scan + completion flag / timestamp | `Adc_StartGroupConversion` + group status query | stuck is "should change but doesn't" — first ensure the sampling cadence itself is fresh |
| F2 | in-step dual-channel conversion: scan back-to-back or single BCTU trigger | `Adc_CtuSetList` + `Adc_CtuStartConversion` | both channels in one conversion chain; µs-level skew vs. pedal ms-level dynamics |
| F3 / F4 / F6 | AWD upper/lower threshold violation = short / over-range | `Adc_ConfigureThreshold` + `Adc_EnableWdgNotification` | thresholds per valid window + margin (see 7.4) |
| F5 | AWD + conditioning: open reads the pull-up level, distinguishable from short levels | same AWD | half of the detection capability lives in signal conditioning, not the ADC |
| F7 | Averaging (multi-sample) | averaging configuration | averaging serves accuracy and suppresses spike false alarms |
| F8 | BCTU trigger source and scan order frozen | `Adc_CtuSetList` / GPR interleave config | interleaving pitfalls: Chapter 3; call sequence: Chapter 11 |
| F9 | conversion-complete IRQ / FIFO watermark as freshness anchor | `Adc_SetupResultBuffer` / `Adc_CtuSetFifoWatermark` | no completion event = no fresh data |
| F10 | ratiometric measurement: VREFH tracks pedal supply | hardware wiring | readings scale with the supply — inherently immune to droop |
| all | power-up Self-Test (algorithms S/O/C) | `Adc_SelfTest` | element-level faults (comparator / capacitor array / reference) exposed at power-up |

> In one sentence: **AWD guards the single-channel bounds, plausibility guards the two-channel relationship, Self-Test guards the element itself, and freshness guards data timeliness** — four different fault models, none substitutable.

### 7.4 A concrete configuration example (SARADC_0)

Example values only; finalize per sensor datasheet and project calibration:

- Resolution and reference: 14-bit, `VREFH = 5.0 V` (same source as the pedal sensor supply; actual value per schematic and RM electrical specs) → 1 LSB = 5.0 / 2^14 ≈ **0.305 mV**.
- Valid window 0.5 V–4.5 V → raw ≈ **1638 … 14746**.
- AWD bounds with 0.1 V margin: `THRL ≈ 0.4 V` (raw ≈ 1311), `THRH ≈ 4.6 V` (raw ≈ 15073) — violation means short / open / over-range: set DTC and degrade.
- Sampling chain: CH0 = APPS1, CH1 = APPS2 in the same group, scan mode **back-to-back**; or BCTU hardware trigger at 5–10 ms for a deterministic cadence.
- Result buffer: `Adc_SetupResultBuffer` + streaming (double buffer); do plausibility and freshness checks in the conversion-complete IRQ.
- Boot check: the first group after power-up must show the pedal at zero position (raw < deadband), otherwise limp mode may not be exited.
- ⚠️ Two known limitations: AWD is **not validated** in the RTD driver (Chapter 6); Adc0/1 DMA is not validated — prefer interrupt mode for the pedal data path; DMA needs platform-level validation.

### 7.5 Software check layer: the consumer of ADC data quality

These mechanisms go beyond the ADC, but **each item depends on ADC-provided freshness and in-step sampling**; they are listed here to keep the chain complete:

- **plausibility**: `|APPS1 − APPS2|` window + debounce (example 100 ms)
- **stuck**: "no change beyond deadband for an extended time" (example 300–500 ms)
- **gradient**: per-cycle slew limit (example: full travel not faster than 150–200 ms)
- **freshness**: a new sample every control cycle (completion IRQ / watermark + rolling counter); stale data degrades immediately
- **interlock**: pedal valid + brake valid at the same time = conflict
- **degradation & recovery**: limp home (torque limit / idle) → safe state; recovery requires passing plausibility again

### 7.6 Risks and validation focus

| # | Risk | Severity | Mitigation |
| --- | --- | --- | --- |
| 1 | AWD not validated — pedal out-of-range detection directly in the safety case leaves a gap | 🔴 High | platform-level AWD validation + redundant software threshold checks |
| 2 | non-in-step sampling → plausibility false alarm / miss under dynamic conditions | 🔴 High | scan back-to-back or single BCTU trigger for both channels |
| 3 | AWD only, no plausibility → "each channel individually plausible but mutually contradictory" is missed | 🟠 Med-High | both layers: AWD per channel, plausibility for the relation |
| 4 | poor open/short level design → F3/F4/F5 indistinguishable | 🟠 Med-High | pull-up/down resistors + criteria review + bench fault injection |
| 5 | longest harness, EMC spikes mistaken for real pedal motion | 🟠 Med-High | averaging + gradient limit + EMC injection tests |
| 6 | no zero-position boot check → torque output with pedal off zero at power-up | 🟡 Med | add zero-position criteria to boot-to-safety |
| 7 | no ratiometric handling of supply droop → all readings shift | 🟡 Med | VREFH tracks supply + periodic recalibration |

> Note: thresholds and time windows in 7.2–7.6 are **engineering convention examples**; finalize per project HARA, sensor datasheet and bench calibration. NXP documentation does not cover application-layer algorithms; the mechanism mapping and risk conclusions here must be independently confirmed in the project safety analysis.

---

## 8. SINC: digital protection for the Σ-Δ chain

When currents, voltages and similar analog quantities enter S32K5 through an external Σ-Δ modulator, SINC is more than a decimation filter — it embeds a set of **dedicated detectors for open/short circuit and clock failure**, a second runtime defense line besides the analog watchdog.

### 8.1 The digital protection trio

| Detector | Monitors | Typical use |
| --- | --- | --- |
| **SCD** (Short-Circuit Detector) | short-circuit (overcurrent) and open-circuit (overvoltage) errors | detects actuator-driver / sensor wiring faults |
| **CAD** (Clock-Absence Detector) | modulator clock input absence | exposes clock-tree failure immediately instead of silent filter degradation |
| **ZCD** (Zero-Cross Detector) | filter channel sign change | zero-cross event monitoring (e.g. PWM applications) |

- **Break signal outputs**: turn off external peripherals on protection events — hardware-level fault containment with the lowest latency, no software in the loop.
- Per channel: 16-entry FIFO with watermark, 2 DMA requests, programmable high/low detection limits, offset bias compensation, HPF for DC removal, Manchester-encoded bitstream support, pulse-triggered output.

### 8.2 Filters and conversion modes

- Structure: one Primary Filter (PF, shifted CIC, **24-bit precision**) per channel + optional CIC sub-module + optional HPF/bias/wake-up.
- Order: `CnDR[PFORD]=0` selects **FastSinc**; `>0` selects the given order (up to 3).
- OSR: `CnDR[PFOSR]+1`, up to **2048**.
- Conversion modes (`CnDR[PFCM]`):

| Mode | Behavior |
| --- | --- |
| Single (00b) | one trigger per conversion |
| Continuous (01b) | converts after a trigger until the next trigger, which cancels and restarts |
| Always (10b) | converts after a trigger until disabled; later triggers ignored |
| Fixed-Number (11b) | stops after `CnCFR[FIFOWMK]` conversions (`NIS[CHFn]=1`) |

- Conversion time: first 24-bit sample takes **ORD × OSR × MOD_CLK cycles**; subsequent samples every OSR × MOD_CLK cycles.

> **Recommended safety usage**: enable CAD + SCD + programmable high/low limits per SINC channel — this adds "data plausibility + wiring integrity + clock liveness" monitoring to the Σ-Δ chain. Route the break signal directly into the actuator shutdown path for the lowest reaction latency.

---

## 9. LPCMP and TEMPSENSE: the low-power monitoring pair

### 9.1 LPCMP (low-power comparator)

- 3 instances: `LPE_LPCMP_0/1/2`, each with 8 input channels, one 8-bit DAC and an ANMUX.
- Safety-relevant capabilities: programmable hysteresis, window mode (`WINDOW_EN`, samples the comparator output only during known stable periods — suppresses false triggers in PWM applications), output inversion, filter counter.
- **Round-Robin Trigger mode in STANDBY**: with the RTC-API, multiple inputs are scanned periodically and compared against the previous result; **any mismatch wakes the chip** — the key mechanism for "monitoring never sleeps" (continuous mode only; RTC_CLK supports SIRC/SXOSC only).
- Interrupt flags: `CSR[CFR]` falling edge, `CSR[CFF]` rising edge, `CSR[RRF]` round-robin cycle complete.

### 9.2 TEMPSENSE (on-chip temperature sensor)

- Structure: BJT sensor + Σ-Δ ADC + decimation filter + **calibration engine**; digital output directly in °C.
- Modes: Single One-Shot / Periodic One-Shot (sleeps between measurements, programmable interval) / Low-Power.
- **Threshold comparators exist in both normal and secure address spaces**, with programmable direction and thresholds; multi-level thresholds cover **under-temperature / over-temperature / panic**; end-of-measurement and threshold violations each have interrupt and status bits.
- Digital format: `DATAn[DATA_VAL]` is a 16-bit signed value with the lower 6 bits as fraction — e.g. `0000_0110_0101_0000` = **+25.25 °C**, `1111_1001_1011_0000` = **−25.25 °C** (two's complement).

> **Over-temperature is a systemic risk**: in the S32K5 fault-reaction classification, the "SoC out-of-context local" example is exactly over-temperature. Route the TEMPSENSE panic threshold into the main safety core's fault handling, not just into a log.

---

## 10. From fault to safe state: VFCCU reaction classes and the SAF software stack

ADC self-test errors, watchdog violations and SINC detector events must all converge into the chip's fault management unit (FMU) before they become **controlled actions**.

### 10.1 Fault-reaction classification (Foundation Training: Safety)

| Reaction type | Name | Fault impact | EOUT | Reaction owner | Escalation |
| --- | --- | --- | --- | --- | --- |
| Transparent | transparent | observed element | not asserted | safety mechanism itself | none (e.g. ECC single-bit correction) |
| R1 | application in-context local | limited to the application and its resources | not asserted | impacted application | alarm interrupt → global software |
| R1 | application out-of-context local | potential chip-wide / shared-resource impact | not asserted | main safety core | alarm interrupt → global hardware |
| R1 | SoC in-context local | shared peripherals / shared memory | not asserted | impacted application(s), distributed | alarm interrupt → global software |
| R1 | SoC out-of-context local | systemic faults (e.g. over-temperature) | not asserted | main safety core | observed by off-chip safety hardware |
| R2 | global SW | whole chip | **asserted** | main safety core | fault interrupt (e.g. ECC multi-bit) |
| R3 | global HW | whole chip | **asserted** | RGM | reset (e.g. EDC gasket / XBIC errors) |

- All four R1 classes **escalate automatically** if recovery does not complete within the alarm/escalation timeout window.
- **VFCCU scale**: 5 LVFCCUs (local aggregation) + 1 CVFCCU (central management), up to **8 reaction types** via **27 reaction outputs**; EOUT supports **7 pin modes** (Input-Only / Push-Pull / Open-Drain / Open-Collector / Bistable / Fault-Toggle / Time Switch).
- Recommended immediate/delayed reactions per fault input are given in the RM attachment **fault map** (`S32K5xx_fault_map.xlsx`).

### 10.2 Boot-to-safety: where the safety context is established

After power-up, the main safety boot core checks that the safety mechanisms work as intended, starts the chip BISTs to detect permanent latent faults, and verifies the safety configuration (required mechanisms enabled and correctly configured). Only after all checks pass does the chip enter Normal Operation; on any failure, the application decides between a degraded mode and a safe state. **The first ADC calibration and self-test belong in the boot-to-safety sequence.**

### 10.3 Safety software stack (SAF / SPD / SCST)

| Component | Role |
| --- | --- |
| **SPD** (Safety Peripheral Drivers) | `Bist` + `eMcem` (Extended Microcontroller Error Manager) safety peripheral drivers; usable in both AUTOSAR and non-AUTOSAR environments |
| **SAF** (Safety Framework) | 6 components: Bist, eMcem, mSel (Mode Selector), sBoot, **sCheck** (periodic square check), sReco (software recovery) |
| **SCST** (Structural Core Self-Test) | runtime detection of permanent core faults, **90% diagnostic coverage**, covering M4/M7/R52 |

> **Periodic software strategy**: sCheck provides the periodic verification framework; hook `Adc_Calibrate()` and `Adc_SelfTest()` into it at the period derived from your safety analysis, and record self-test results (error bit + step number) as part of eMcem diagnostics.

---

## 11. RTD ADC driver: safety-relevant configuration and call sequence

### 11.1 Configuration checklist (AutosarExt)

| Parameter | Purpose | Notes |
| --- | --- | --- |
| `AdcEnableSelfTest` | enables `Adc_SelfTest()` | mandatory for safety applications |
| `AdcEnableCalibration` | enables `Adc_Calibrate()` | **calibration mandatory once self-test is enabled** |
| `AdcEnableAsyncCalibration` | asynchronous calibration (two calls) | no other ADC API allowed while calibrating |
| `AdcCalibrationPrescale` | calibration clock input select | — |
| `AdcSelfTestInputSamplingAlgCVal` | Algorithm C sampling phase duration | default 24, range 1–255 |
| `AdcSelfTestInputSamplingAlgSVal` | Algorithm S sampling phase duration | same |
| `AdcEnableWatchdogFunctionality` | analog watchdog master switch | removes watchdog code at pre-compile time when off |
| `AdcEnableThresholds` / `AdcThresholdRegister` / `AdcWdogNotification` | per-channel thresholds and notification | independent per channel |

### 11.2 Recommended call sequence

```text
Power-up / boot-to-safety
   │
   ▼
Adc_Init(&AdcConfigSet)              ── failure: ADC_E_TIMEOUT (HW cannot enter power-down/idle)
   │
   ▼
Adc_Calibrate()                      ── compensate offset/gain/capacitor mismatch
   │                                    not needed after functional reset;
   │                                    mandatory after destructive reset
   ▼
Adc_SelfTest()                       ── algorithms S / O / C + dual watchdogs
   │                                    timeout: ADC_E_TIMEOUT
   ▼
┌─ Normal operation ───────────────────────────────────────┐
│ Adc_StartGroupConversion(Group)                          │
│   ├─ Normal / Injected / BCTU modes                       │
│   ├─ analog watchdog live monitoring (AWD IRQ → notif.)  │
│   └─ SINC chain: SCD / CAD / ZCD + break signal           │
│ Adc_StopGroupConversion(Group)                           │
└──────────────────────────────────────────────────────────┘
   │
   ▼
Condition change (temperature swing / destructive reset) → back to Adc_Calibrate()
```

### 11.3 DET runtime error quick reference

| Function | Error code | Trigger condition |
| --- | --- | --- |
| `Adc_Init()` / `Adc_DeInit()` | `ADC_E_TIMEOUT` | ADC hardware cannot enter power-down / idle |
| `Adc_StartGroupConversion()` / `Adc_StopGroupConversion()` | `ADC_E_TIMEOUT` | ongoing conversion cannot be aborted |
| `Adc_SetHwUnitPowerMode()` | `ADC_E_TIMEOUT` | power mode setting timed out |
| `Adc_Calibrate()` | `ADC_E_TIMEOUT` | calibration operation timed out |
| `Adc_SelfTest()` | `ADC_E_TIMEOUT` | self-test operation timed out |
| `Adc_SetClockMode()` | `ADC_E_UNINIT` / `ADC_E_INVALID_CLOCK_MODE` / `ADC_E_TIMEOUT` | NULL global pointer / illegal clock mode / timeout |

---

## 12. Design checklist and risk register

### 12.1 Checklist

- [ ] ADC instance selection verified against power domains: LPRUN scenarios only LPE_SARADC is available (PD1); platform SARADC_0/1 go down with PD2
- [ ] boot-to-safety sequence includes `Adc_Init` → `Adc_Calibrate` → `Adc_SelfTest`, with first results archived
- [ ] destructive-reset handling flow includes recalibration (functional reset does not)
- [ ] prerequisite "self-test enabled ⇒ calibrated" enforced in configuration (`AdcEnableCalibration` + `AdcEnableSelfTest` together)
- [ ] `STBR[WDT]` safe time matched to the self-test period (full Step0-to-next-Step0 window)
- [ ] self-test AWD error bit + step number wired into diagnostics (fault isolation down to the step)
- [ ] AWD THRH/THRL set per signal range; `AdcWdogNotification` handler hooked
- [ ] "AWD not validated" driver limitation explicitly recorded in the project safety analysis, with platform validation planned
- [ ] SINC channels: CAD / SCD / ZCD enabled, break signal routed to actuator shutdown
- [ ] TEMPSENSE panic threshold routed to main safety core fault handling (not log-only)
- [ ] channel interleaving (`GPR_RWF_0`) matches the schematic and is frozen
- [ ] Normal-mode empty-chain `IS[ECH]` interrupt hooked (configuration-loss sentinel)
- [ ] periodic recalibration scheduled for runtime condition changes (no ongoing conversions during recalibration)
- [ ] accelerator pedal dual channels in the same group: scan back-to-back or single BCTU trigger, sampling skew far below pedal dynamics (µs-level vs. ms-level)
- [ ] pedal-channel AWD thresholds set per valid window + margin (example: 0.5–4.5 V window, 0.4 V / 4.6 V violation), violation sets DTC and degrades
- [ ] pull-up/down resistor design makes F3 GND short / F4 supply short / F5 open present distinguishable levels; verified one-by-one with bench fault injection
- [ ] VREFH tracks the pedal sensor supply (ratiometric wiring); readings scale proportionally under supply droop
- [ ] boot-to-safety adds a zero-position check: the first group after power-up must show the pedal at zero, otherwise limp mode may not be exited
- [ ] a fresh sample every control cycle (conversion-complete IRQ / FIFO watermark + rolling counter); stale data degrades immediately
- [ ] plausibility window and debounce time, stuck deadband time window, gradient slew limit all calibrated per HARA and frozen
- [ ] limp-home degradation strategy (torque limit) and recovery condition (pass plausibility again) defined in the safety state machine

### 12.2 Risk register

| # | Risk | Severity | Source |
| --- | --- | --- | --- |
| 1 | Self-Test enabled but calibration skipped → false self-test failures, safety mechanism cries wolf | 🔴 High | Foundation Training: calibration is a prerequisite of self-test |
| 2 | No recalibration after destructive reset → all subsequent conversions carry a wrong offset | 🔴 High | functional reset preserves calibration registers; destructive reset does not |
| 3 | Conversions still ongoing during self-test/calibration → API errors or silent no-op, protection silently lost | 🔴 High | RTD UM: prerequisite is no ongoing conversions |
| 4 | AWD **not validated** in the RTD driver — using it directly in the safety case leaves a gap | 🔴 High | RTD ADC UM §3.5 Driver Limitations |
| 5 | Platform SARADC used in LPRUN → sleep strategy fights monitoring requirements | 🟠 Med-High | power-domain table (derived; verify against RM) |
| 6 | Adc0/Adc1 DMA not validated — safety data path on DMA needs supplementary validation | 🟠 Med-High | RTD ADC UM §3.5 |
| 7 | Interleaving GPR configuration mismatched with schematic → sampling the wrong pad | 🟠 Med-High | Foundation Training: interleaving table |
| 8 | `STBR[WDT]` safe time too tight → false timeout from interleaved normal-chain conversions | 🟡 Med | safe-time window includes interleaved normal conversions |
| 9 | Other ADC APIs called during async calibration → error or silent no-op | 🟡 Med | RTD UM: only `Adc_Deinit()` allowed |
| 10 | SINC Manchester / HPF / bias misconfiguration → systematic decimation offset | 🟡 Med | Foundation Training: all optional, must follow modulator datasheet |
| 11 | TEMPSENSE log-only → no fault containment on over-temperature | 🟡 Med | fault-reaction classes: over-temperature is SoC out-of-context local |
| 12 | LPE_BCTU unavailable in Design Studio — confirm toolchain plan early | 🟡 Low | RTD ADC UM §3.5 |
| 13 | pedal dual channels sampled non-in-step → plausibility false alarm / miss under dynamic conditions | 🔴 High | scan back-to-back or single BCTU trigger for both channels (Chapter 7, F2/F8) |
| 14 | AWD only, no plausibility → each channel individually plausible but mutually contradictory is missed | 🟠 Med-High | both layers: AWD per channel, plausibility for the relation |
| 15 | longest pedal harness, EMC spikes mistaken for real pedal motion | 🟠 Med-High | averaging + gradient limit + EMC injection tests |

---

## 13. References

1. NXP S32K5 Foundation Training — *Analog: SARADC, SINC, LPCMP, TEMPSENSE* (AAES AMCU Systems and Applications; based on S32K5RM Rev2 DraftE / S32K5xx DS Rev1 DraftE)
2. NXP S32K5 Foundation Training — *Safety* (same source)
3. NXP *S32K5xx Reference Manual*, Rev.2 (2026-06-01), Chapter 63 *Safety Overview* (§63.4.2 specific BIST / §63.5 boot-to-safety / §63.7 BIST)
4. NXP *S32K5xx Safety Manual* (SEooC safety concept, assumptions of use, fault-map attachment)
5. NXP *User Manual for S32K5 ADC Driver* (RTD, UM85ADCASRR23-11) — §3.6.2 Calibration / §3.6.3 Self-Test / §3.6.13 Analog Watchdog / §3.7 Runtime errors / §3.5 Driver Limitations
6. Related articles in this directory: [S32K5_R52_M7_Sleep_Design_EN.md](../power_designs/S32K5_R52_M7_Sleep_Design_EN.md), [S32K5_R52_M7_MPU_Design_EN.md](../mpu_concept/S32K5_R52_M7_MPU_Design_EN.md)

> All register names, bitfields and default values in this article come from the public training material and documents listed above. Before production, cross-check every item against the released Reference Manual and Safety Manual of the specific derivative, and rely on your project's own HARA/FSC conclusions.
