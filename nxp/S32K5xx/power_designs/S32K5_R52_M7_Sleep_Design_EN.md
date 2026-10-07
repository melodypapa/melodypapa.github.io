# Design of Sleep Mode for R52 and M7 (Two Independent OSes)

## 1. Overall Architecture Understanding

The power domain (PD) division of S32K5 determines the fundamental constraints of the sleep strategy:

| Power Domain               | Contents                                           | Independently Switchable        |
| -------------------------- | -------------------------------------------------- | ------------------------------- |
| **PD0** (Always-On)        | PMC, RGM, WKPU, MC_PCU, FRO, SIRC, 384KB SRAM, etc. | No (always powered)           |
| **PD1** (Low-Power Engine) | **CM4**, eDMA3, FTM, LPSPI, LPUART, LPI2C, etc.   | Yes (can be independent of PD2) |
| **PD2** (Full-Performance) | **CM7, R52**, HSE2, MRAM, FlexCAN, SENT, etc.      | Yes (can be independent of PD1) |

**Key constraint**: Both CM7 and R52 are located in **PD2**, which means you cannot put CM7 to sleep while keeping R52 running, or vice versa. PD2 is either fully powered or fully off.

## 2. Supported Power Modes and Core States

| Power Mode  | Powered Domains | R52      | M7       | CM4 (LPE)     | HSE2 |
| ----------- | --------------- | -------- | -------- | ------------- | ---- |
| **RUN**     | PD2+PD1+PD0     | Run/Wait | Run/Wait | Run/Wait/Stop1/Stop2 | Run  |
| **LPRUN**   | PD1+PD0         | Off      | Off      | Run/Wait/Stop1/Stop2 | Off  |
| **STANDBY** | PD0             | Off      | Off      | Off           | Off  |

That is, R52 and M7 sleep **in tandem** — they must enter LPRUN/STANDBY together and wake up together.

> **Note 1**: CM4 supports `Run / Wait / Stop1 / Stop2` in both RUN and LPRUN, where **Stop1 and Stop2 are two distinct low-power states** and must not be merged when configuring.
>
> **Note 2 (clocks in LPRUN)**: PLLs are **not available** in LPRUN/Standby. The only usable clocks are FXOSC, SXOSC, SIRC, FIRC and their derivatives. FIRC is active in these modes but **not configurable** (its resources are accessible only by HSE2). Therefore, for a Run → LPRUN → Standby path, **FIRC must be configured in Run mode**, because HSE2 is unavailable once in LPRUN.

## 3. Recommended Sleep Design

### Scheme 1: LPRUN Mode (Recommended, most common)

When both M7 and R52 have nothing to do, both execute WFI, PD2 is powered off, leaving only **LPE (CM4) running in PD1**.

```
Normal RUN (M7 + R52 running at full speed)
    |
    v
M7 OS and R52 OS each complete pre-shutdown preparation
    |
    v
Requestor Core notifies CM4 via MU interrupt; CM4 stops using PD2 peripherals and confirms
    |
    v
M7 and R52 each execute WFI
    |
    v
Requestor Core polls the other's WFI status in MC_ME
    |
    v
PCFS ramp-down (ramp down to initial frequency)
    |
    v
Write CTL_KEY key sequence, then disable M7/R52 clocks via MC_ME[COREx_PCONF]
    |
    v
Shut down PD2 peripheral clocks (write CTL_KEY + MC_ME[COFB_CLKEN])
    |
    v
Switch clock source to FRO, disable PLL
    |
    v
Configure Pad keeping (optional)
    |
    v
Stop pending HSE2 services (optional)
    |
    v
PMIC handshake configuration (required when an external PMIC is used)
    |
    v
Execute DSB + ISB barriers to ensure no pending instructions
    |
    v
Write CTL_KEY + MC_RGM MODE_CONF[LPRUN] to request LPRUN entry
    ----------------------------
    LPRUN mode (only CM4 running in PD1)
```

### Scheme 2: STANDBY Mode (Lowest power)

```
Normal RUN (M7 + R52)
    |
    v
(Optional: enter LPRUN first)
    |
    v
CM4 takes over the shutdown sequence (acts as Requestor Core)
    |
    v
Shut down PD1 peripherals (write CTL_KEY + MC_ME[COFB_CLKEN])
    |
    v
Configure WKUP wake-up sources
    |
    v
Configure Pad keeping
    |
    v
PMIC handshake configuration (required when an external PMIC is used)
    |
    v
Execute DSB + ISB barriers
    |
    v
Write CTL_KEY + MC_RGM MODE_CONF[STANDBY] to request STANDBY entry
    ----------------------------
    STANDBY (only PD0 powered, 384KB RAM retained)
```

## 4. Multi-Core Sleep Coordination Sequence (Key)

The **MC_ME** module of S32K5 provides a WFI status monitoring mechanism for multi-core coordination.

> **Relationship to the MCU driver**: the NXP S32K5 MCU Driver (UM85MCUASRR23-11) divides the entire Standby entry process into **four software phases SW1–SW4**, driven by `Mcu_SetMode` / `Mcu_InitClock`. The steps below are organized by these phases. In a real project these register-level operations are performed internally by the MCU driver; the application layer only calls the APIs.
>
> | Phase | Name | Driver API | Corresponding step below |
> |---|---|---|---|
> | SW1 | Peripheral Shutdown | `Mcu_SetMode` (peripheral set) | Steps 4.1–4.3 |
> | SW2 | Application Core Shutdown | app core: `Mcu_SetMode(CORE_STANDBY)`; main core: `Mcu_SetMode` (`McuCoreUnderMcuControl` checked + `McuCoreClockEnable` unchecked) | Steps 4.2–4.3 |
> | SW3 | Flash Low-Power Handshake + PMC_LASTMILE Disable | `Mcu_InitClock`, `Mcu_SetMode(SOC_PREPARE_STANDBY)` | Step 4.6 |
> | SW4 | Main Core Shutdown | `Mcu_SetMode(SOC_STANDBY)` with `McuMainCoreSelect` set to the main core | Step 4.12 |
>
> Relevant Tresos/MCAL configuration parameters: `McuPowerMode` (`CORE_STANDBY` / `SOC_PREPARE_STANDBY` / `SOC_STANDBY`), `McuCoreUnderMcuControl`, `McuCoreClockEnable`, `McuMainCoreSelect`.

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 779" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>S32K5 Standby entry: SW1-SW4 phases with dual-core coordination</title>
<desc>Four software phases driving the S32K5 MCU driver into Standby: peripheral shutdown, application core shutdown, flash low-power handshake with PMC_LASTMILE disable, and main core shutdown, with PD2/PD1/PD0 power state shown per phase.</desc>
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="40" y="26" font-size="15" font-weight="500" fill="#2C2C2A">Standby Entry: SW1–SW4 Phases and Dual-Core Coordination</text>
<text x="40" y="45" font-size="12" fill="#5F5E5A">Each phase is handled by an MCU driver API; the application never touches registers directly</text>
<rect x="40" y="62" width="424" height="138" rx="10" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
<path d="M40 72 a10 10 0 0 1 10 -10 h404 a10 10 0 0 1 10 10 v34 h-424 z" fill="#B5D4F4"/>
<text x="53" y="84.0" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">SW1</text>
<text x="88" y="84.0" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">Peripheral Shutdown</text>
<text x="88" y="99.0" font-size="11" fill="#185FA5" dominant-baseline="central">Mcu_SetMode (peripheral set)</text>
<circle cx="57" cy="133.5" r="2" fill="#185FA5"/>
<text x="68" y="133.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Disable PD2 peripheral clocks: CTL_KEY +</text>
<circle cx="57" cy="152.5" r="2" fill="#185FA5"/>
<text x="68" y="152.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">COFB_CLKEN[REQnz]</text>
<circle cx="57" cy="171.5" r="2" fill="#185FA5"/>
<text x="68" y="171.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Disable one CPE partition at a time, else HardFault</text>
<rect x="480" y="96.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="106.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD2 On</text>
<rect x="480" y="121.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="131.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD1 On</text>
<rect x="480" y="146.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="156.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD0 On</text>
<rect x="40" y="200" width="424" height="138" rx="10" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
<path d="M40 210 a10 10 0 0 1 10 -10 h404 a10 10 0 0 1 10 10 v34 h-424 z" fill="#CECBF6"/>
<text x="53" y="222.0" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">SW2</text>
<text x="88" y="222.0" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">Application Core Shutdown</text>
<text x="88" y="237.0" font-size="11" fill="#534AB7" dominant-baseline="central">Mcu_SetMode (CORE_STANDBY)</text>
<circle cx="57" cy="271.5" r="2" fill="#534AB7"/>
<text x="68" y="271.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">MU interrupt tells CM4 to stop using PD2 peripherals</text>
<circle cx="57" cy="290.5" r="2" fill="#534AB7"/>
<text x="68" y="290.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Each core reads WFI status; PD2 cores confirm each other</text>
<circle cx="57" cy="309.5" r="2" fill="#534AB7"/>
<text x="68" y="309.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">PCFS ramp-down, clock off, then MC_RGM_PRST</text>
<rect x="480" y="234.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="244.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD2 On</text>
<rect x="480" y="259.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="269.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD1 On</text>
<rect x="480" y="284.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="294.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD0 On</text>
<rect x="40" y="338" width="424" height="157" rx="10" fill="#FAEEDA" stroke="#854F0B" stroke-width="0.5"/>
<path d="M40 348 a10 10 0 0 1 10 -10 h404 a10 10 0 0 1 10 10 v34 h-424 z" fill="#FAC775"/>
<text x="53" y="360.0" font-size="13" font-weight="500" fill="#412402" dominant-baseline="central">SW3</text>
<text x="88" y="360.0" font-size="13" font-weight="500" fill="#412402" dominant-baseline="central">Flash Handshake + Last-Mile Regulator</text>
<text x="88" y="375.0" font-size="11" fill="#854F0B" dominant-baseline="central">Mcu_InitClock + SOC_PREPARE_STANDBY</text>
<circle cx="57" cy="409.5" r="2" fill="#854F0B"/>
<text x="68" y="409.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Wait for ongoing flash high-voltage operations to finish</text>
<circle cx="57" cy="428.5" r="2" fill="#854F0B"/>
<text x="68" y="428.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Switch system clock to FIRC, disable PLL (PLLDIG</text>
<circle cx="57" cy="447.5" r="2" fill="#854F0B"/>
<text x="68" y="447.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">unavailable)</text>
<circle cx="57" cy="466.5" r="2" fill="#854F0B"/>
<text x="68" y="466.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Disable PMC_LASTMILE, else flash array still draws power</text>
<rect x="480" y="381.5" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="391.5" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD2 On</text>
<rect x="480" y="406.5" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="416.5" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD1 On</text>
<rect x="480" y="431.5" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="441.5" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD0 On</text>
<rect x="40" y="495" width="424" height="138" rx="10" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
<path d="M40 505 a10 10 0 0 1 10 -10 h404 a10 10 0 0 1 10 10 v34 h-424 z" fill="#9FE1CB"/>
<text x="53" y="517.0" font-size="13" font-weight="500" fill="#04342C" dominant-baseline="central">SW4</text>
<text x="88" y="517.0" font-size="13" font-weight="500" fill="#04342C" dominant-baseline="central">Main Core Shutdown</text>
<text x="88" y="532.0" font-size="11" fill="#0F6E56" dominant-baseline="central">Mcu_SetMode (SOC_STANDBY)</text>
<circle cx="57" cy="566.5" r="2" fill="#0F6E56"/>
<text x="68" y="566.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Configure WKPU wake-up sources (internal: positive only)</text>
<circle cx="57" cy="585.5" r="2" fill="#0F6E56"/>
<text x="68" y="585.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Execute DSB + ISB barriers</text>
<circle cx="57" cy="604.5" r="2" fill="#0F6E56"/>
<text x="68" y="604.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">Write MODE_CONF[STANDBY] plus the CTL_KEY sequence</text>
<rect x="480" y="529.0" width="160" height="20" rx="5" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="560.0" y="539.0" font-size="11" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">PD2 Off</text>
<rect x="480" y="554.0" width="160" height="20" rx="5" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="560.0" y="564.0" font-size="11" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">PD1 Off</text>
<rect x="480" y="579.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="589.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD0 On</text>
<path d="M252.0 201 L252.0 215" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M252.0 355 L252.0 369" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M252.0 528 L252.0 542" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="40" y="697" width="424" height="62" rx="10" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.5"/>
<text x="53" y="714" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Exit path (wake-up)</text>
<text x="53" y="732.0" font-size="11" fill="#5F5E5A" dominant-baseline="central">WKPU event, LPE CM4 asserts EXTWAKE, PD2 powers up</text>
<text x="53" y="747.0" font-size="11" fill="#5F5E5A" dominant-baseline="central">(destructive reset), HSE2 BootROM, sBAF, HSE2_FW</text>
<rect x="480" y="705" width="160" height="20" rx="5" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="560.0" y="715" font-size="11" fill="#042C53" text-anchor="middle" dominant-baseline="central">Mcu_GetResetReason</text>
<text x="560.0" y="740" font-size="11" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">identify wake source</text>
</svg>
<figcaption style="font-size:0.85em;color:#666">Figure 1: SW1–SW4 Standby entry phases with dual-core coordination (power domain states)</figcaption>
</figure>

>
> **Note**: the clock of the main core must always stay enabled — either leave `McuCoreUnderMcuControl` unchecked if the application configures the main core, or check both `McuCoreUnderMcuControl` and `McuCoreClockEnable` together.

### Step 1: Each OS completes its own pre-sleep preparation

| What the M7 OS does                              | What the R52 OS does                    |
| ------------------------------------------------ | --------------------------------------- |
| Disable non-essential interrupt sources          | Disable non-essential interrupt sources |
| Save context (to PD0 SRAM)                       | Save context (to PD0 SRAM)              |
| Stop HSE2 service requests on M7                 | Stop HSE2 service requests on R52       |
| Set up wake-up interrupts                        | Set up wake-up interrupts               |
| Notify R52 OS of pending sleep (MU interrupt)    | Confirm and reply to M7                 |
| Execute **WFI**                                  | Execute **WFI**                         |

**In addition, the Requestor Core must notify CM4 (LPE) via an MU interrupt.** Even though PD1 stays powered in LPRUN, CM4 may still be accessing PD2 domain resources (e.g. FlexCAN, SENT, which reside in PD2). The Requestor Core must notify CM4 to stop using those PD2 peripherals, and proceed only after CM4 confirms.

### Step 2: Requestor Core checks WFI status

Either core (M7 or R52) acts as the **Requestor Core**, polling each core's WFI status.

⚠️ **Critical**: the WFI status registers live in **three different MC_ME partitions** and must not be mixed up.

| Core                | WFI status register                    | Partition    |
| ------------------- | -------------------------------------- | ------------ |
| Cortex-M7_0         | `MC_ME.PRTN0_CORE0_STAT[WFI]`          | SoC MC_ME    |
| Cortex-M7_1         | `MC_ME.PRTN0_CORE2_STAT[WFI]`          | SoC MC_ME    |
| Cortex-M7_2         | `MC_ME.PRTN0_CORE3_STAT[WFI]`          | SoC MC_ME    |
| Cortex-M7_3         | `MC_ME.PRTN0_CORE4_STAT[WFI]`          | SoC MC_ME    |
| Cortex-R52_0        | `CPE_MC_ME.PRTN0_CORE0_STAT[WFI]`      | CPE MC_ME    |
| Cortex-R52_1        | `CPE_MC_ME.PRTN0_CORE1_STAT[WFI]`      | CPE MC_ME    |
| Cortex-M4 (LPE)     | `LPE_MC_ME.PRTN0_CORE0_STAT[WFI]`      | LPE MC_ME    |

> **M7 core indices are non-contiguous**: M7_0 maps to `CORE0`, M7_1 to `CORE2`, M7_2 to `CORE3`, M7_3 to `CORE4`. `CORE1` does not belong to M7, so do not treat these as a contiguous array.

Therefore, **when R52 acts as the Requestor Core, reading M7's WFI status requires the SoC MC_ME partition** (`MC_ME.PRTN0_CORE0_STAT`, etc.), not `CPE_MC_ME`.

### Step 3: Clock ramp-down, shutdown and reset

```
1. Set clocks to initial frequency and complete PCFS ramp-down
2. Confirm the peer core's WFI is set (read the register from the table above)
3. Write the CTL_KEY key sequence (0x5AF0, then 0xA50F)
4. Disable the target core clock via MC_ME[COREn_PCONF][CCE]
5. Confirm clock stopped via MC_ME[COREn_STAT][CCS] (CCS=0 means clock inactive)
6. Assert core reset via MC_RGM_PRST
7. Read MC_RGM_PSTAT to confirm reset took effect -> core officially off
```

### Step 4: Shut down PD2 peripherals and request mode switch

```
1. Write the CTL_KEY key sequence (0x5AF0, then 0xA50F)
2. Shut down PD2 peripheral clocks: MC_ME[PRTNn_COFB_CLKEN][REQnz] = 0
3. Write PRTNn_PUPD and poll it; read PRTNn_COFB_STAT[BLOCKnz] to confirm clocks off
4. Switch system clock to FIRC, disable PLL
   - **Standby entry must switch to FIRC** (PLLDIG is not available in Standby)
   - FXOSC may be used instead if the 2.5 V supply is available and PMC.CONFIG[LPM25EN] is configured
   - All clock sources may be optionally disabled (including FIRC), yielding a no-clock lowest-power mode
5. Configure Pad keeping (PD2 pins controlled globally by WKPU.GPIO_QUAL[PD2_PD0])
6. **SW3: Flash Low-Power Handshake and PMC_LASTMILE Regulator Disable**
   a. Suspend or wait for any ongoing flash high-voltage operations (otherwise a flash programming interruption causes non-deterministic behavior)
   b. Configure FIRC as the system clock and disable the PLL
   c. Prepare the SoC for standby mode
7. Stop HSE2 services (optional; wait for in-flight services to finish)
8. Configure WKPU wake-up sources (mandatory for Standby entry; no core is active in Standby)
9. PMIC handshake configuration (required when powering rails via an external PMIC)
10. **Disable only one CPE partition at a time** (disabling both CPE_0 and CPE_1 causes a HardFault)
11. Execute DSB + ISB barriers to ensure no pending instructions
12. Write CTL_KEY key sequence + MC_RGM MODE_CONF[LPRUN] or MODE_CONF[STANDBY]
    -> start the hardware mode transition
```

> ⚠️ **CPE partition constraint**: disabling `PARTITION_CPE_0_INDEX` and `PARTITION_CPE_1_INDEX` together powers down the whole CPE system, causing a HardFault when the driver subsequently accesses CPE_0. **Disable only one CPE partition at a time.**
>
> ⚠️ **CPE_LLC caution**: selecting `PowerOffState` for CPE_LLC0/CPE_LLC1 causes a HardFault (the driver still accesses the unpowered partition). Select `PowerOnState` instead.

## 5. Wake-Up Flow

### Waking M7+R52 from LPRUN

Wake-up is executed by **LPE (CM4)**:

```
External/internal wake-up event triggers
    |
    v
WKPU detects wake-up source -> interrupts LPE CM4
    |
    v
CM4 performs PMIC handshake (asserts EXTWAKE, see table below)
    |
    v
PD2 powers up (PD1-PD2 distributed switch closes)
    |
    v
A destructive reset occurs on PD2
    |
    v
HSE2 BootROM -> sBAF integrity check -> HSE2_FW enables PD2 application cores
    |
    v
M7 and R52 OSes each restore their context
    |
    v
Return to RUN mode
```

**Note**: when waking M7+R52 from LPRUN, PD2 undergoes a **destructive reset** after power-up (Ch58 Table 308: LPRUN → RUN asserts a destructive reset on PD2 while PD1/PD0 remain active), so both cores restart through the boot chain. Therefore, **context saving** of both OSes is crucial.

> **Boot chain (S32K5 has no IVT concept)**: after the hardware reset sequence completes, **the only core running initially is the ZenV core on HSE2**, which proceeds BootROM → sBAF (Secure Boot Assist Firmware) → HSE2_FW, and it is **HSE2_FW that enables the application cores in PD2**. S32K5 does not use an IVT (Image Vector Table) mechanism.

### Reset domain scope triggered by wake-up

| Mode transition | PD2                  | PD1                  | PD0         |
| ---------------- | -------------------- | -------------------- | ----------- |
| Standby → LPRUN | stays OFF           | destructive reset    | stays active |
| Standby → RUN    | destructive reset    | destructive reset    | stays active |
| LPRUN → RUN      | destructive reset    | stays active         | stays active |

> **Low-power fast path**: on Standby → LPRUN, **PD2 stays OFF** and only PD1 powers up. This is the staged power-up path where CM4 starts running first and the PD2 application cores are enabled later.

### Supported Wake-Up Sources

**External wake-up sources**

| Wake-Up Source Type | Origin                                                     | Notes |
| ------------------- | ---------------------------------------------------------- | ----- |
| **External GPIO**   | Minimum 60 WKPU pins (WKPU[0]-WKPU[59])                     | Actual pins per the IOMUX table; each source has its own glitch filter |

**Internal wake-up sources (8 total, per Ch57 Table 299)**

| # | Internal wake-up source                                          | Notes |
|---|-------------------------------------------------------------------|-------|
| 1 | LPE_SWT0                                                          | Watchdog timer |
| 2 | (NOR (CMPn Round Robin Mode)) AND (LPE_RTC_API Timeout)           | Combined logic source of comparator round-robin and RTC timeout |
| 3 | LPE_RTC_API Timeout (Wakeup counter or rollover)                  | RTC wakeup counter overflow or timeout |
| 4 | LPE_CMP0 Async                                                    | Comparator 0 asynchronous edge |
| 5 | LPE_CMP1 Async                                                    | Comparator 1 asynchronous edge |
| 6 | LPE_CMP2 Async                                                    | Comparator 2 asynchronous edge (not supported on S32K511) |
| 7 | LPE_PIT_RTI                                                       | PIT real-time interrupt |
| 8 | LPE_LCU                                                           | Logic control unit |

> ⚠️ **Critical constraint**: internal wake-up sources are **positive polarity only and must not be configured for negedge-triggered operation**. This is the most common reason a device fails to wake from low power.
>
> **Mode association**: each wake-up event can be software-configured for a different mode transition (Standby→Run or Standby→LPRUN); the supported modes are not fixed per source.
>
> **NMI does not support wake-up from Standby.**

**Arbitration when multiple sources arrive together**
- The **first** wake-up source to arrive at the MCU determines the power mode sequence, and that sequence **runs to completion** unless a POR, functional or destructive reset occurs
- When two or more wake-up sources are sampled together and indicate different mode transitions, **Standby → Run has the highest priority**
- All wake-up events set their corresponding flag in WKPU whenever they occur, regardless of the device's current power mode or any ongoing power mode transition

## 6. PD0 SRAM Usage Recommendations

PD0 provides **384KB of SRAM** for data retention (SRAM UPPER PD0 = 256KB, SRAM LOWER PD0 = 128KB). Suggested allocation for the two OSes:

| Region | Purpose | Suggested capacity |
|---|---|---|
| **M7 reserved** | M7 OS context, critical variables | ~192KB |
| **R52 reserved** | R52 OS context, critical variables | ~128KB |
| **Shared reserved** | Inter-core comm flags, wake-up reason | ~64KB |

> **Note**: the 192/128/64KB split is a **suggestion, not a hardware constraint**. Adjust it to the measured context size of each OS, and do not exceed the 384KB total. PD0 SRAM is powered by the retention voltage in low-power modes to preserve data.

## 7. Recommended Implementation Summary

| Item | Recommendation |
|---|---|
| **Target mode** | **LPRUN** (CM4 stays running, M7+R52 sleep) |
| **Coordination mechanism** | Requestor Core confirms readiness via each partition's WFI status bit (M7 → `MC_ME`, R52 → `CPE_MC_ME`, CM4 → `LPE_MC_ME`) |
| **Inter-core communication** | Use **MU (Message Unit)** interrupts to notify peers of the shutdown sequence; use shared PD0 SRAM for handshake data |
| **CM4 notification** | The Requestor Core **must** notify CM4 to stop using PD2 peripherals and wait for confirmation |
| **Context saving** | Each OS saves context to **PD0 SRAM** (384KB) |
| **Clock ramp-down** | Complete **PCFS ramp-down** before clock gating; **FIRC must be pre-configured in Run mode** for LPRUN/Standby |
| **Flash low power** | Before Standby, **wait for ongoing flash high-voltage operations to finish** and disable **PMC_LASTMILE**, otherwise the flash array still consumes power |
| **Partition shutdown order** | **Disable only one CPE partition at a time**; CPE_LLC0/1 must use `PowerOnState`, otherwise HardFault |
| **Register write protection** | Execute the **CTL_KEY key sequence (0x5AF0 / 0xA50F)** before writing any protected register |
| **Mode switch barrier** | Execute **DSB + ISB** before writing `MODE_CONF` |
| **Wake-up sources** | Configure one of the 8 internal sources per RM Table 299, or WKPU external pins; **internal sources are positive polarity only** |
| **Interrupt responsibility** | **All interrupts must be disabled** before requesting the mode switch; **EcuM is responsible for ensuring no wake-up interrupt is lost** (the MCU driver cannot detect this) |
| **PLL recovery** | After wake-up, **explicitly call `Mcu_DistributePllClock`** to restore the PLL clock (the switch to PLL is not completed by `Mcu_InitClock`) |
| **Wake-up reason** | Use `Mcu_GetResetReason` to determine why the MCU woke up |
| **PMIC collaboration** | **FS25 SBC** recommended (purpose-built for S32K5/S32J, ASIL D), handshake via **PGOOD + EXTWAKE(1)/(2)** |

> **Note**: many of the register-level steps in Section 4 (PCFS ramp-down, CTL_KEY key sequence, `COREn_PCONF[CCE]`, `COFB_CLKEN[REQnz]`, `MODE_CONF`, DSB+ISB) are **performed internally by the MCU driver** in a real project. The application layer should not manipulate these registers directly. See `MCAL_API_MAPPING.md` for details.

### PMIC Handshake Signal Semantics

The S32K5 handshakes with a PMIC/SBC via **PGOOD** (input) and **EXTWAKE(1)/EXTWAKE(2)** (outputs), using up to four GPIOs. EXTWAKE polarity is configurable via `GPR_0` registers, and pin mapping via the SIUL2 MSCR registers.

| Device mode transition | EXTWAKE(1) | EXTWAKE(2) |
|---|---|---|
| Run → LPRUN | Signal de-assertion | Signal de-assertion |
| Run → Standby | Signal de-assertion | Signal de-assertion |
| LPRUN → Standby | Signal de-assertion | Signal de-assertion |
| LPRUN → Run | Signal assertion | No change |
| Standby → Run | Signal assertion | No change |
| Standby → LPRUN | No change | Signal assertion |

> The PMIC responds **only to the assertion** of EXTWAKEn; de-assertion must be ignored by the PMIC.
>
> **POR WDOG is triggered after EXTWAKE assertion**: if PGOOD does not assert within the configured time, POR WDOG issues a reset to the chip.
>
> **Run → Standby PGOOD glitch**: an unintended reset state can be detected during this transition. To avoid it: ① set `PMC.CONFIG[PGOODMASK]` to temporarily mask PGOOD; ② program the PMIC into LPE mode (with a delay). These two steps **must be interrupt-protected** so the sequence cannot be split in time.
