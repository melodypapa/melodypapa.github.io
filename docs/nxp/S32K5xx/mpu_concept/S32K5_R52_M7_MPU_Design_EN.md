## MPU Design for S32K5xx (Cortex-M7 + Cortex-R52)

> **Target platform**: NXP S32K5xx family (S32K566 / S32K58, etc.), Cortex-M7 platform cores + Cortex-R52 compute cores
>
> **Sources**: Arm Cortex-M7 TRM (ARMv7-M PMSAv7), Arm Cortex-R52 TRM r1p2 (Armv8-R PMSAv8-32), Cortex-R52/R52+ Programmer's Guide, NXP S32K Knowledge Base / Zephyr S32K5XXCVB board documentation
>
> **Address authority**: NXP S32K5xx Reference Manual **Rev.3 (rm1131130)** and its embedded attachment **`S32K5xx_memory_map.xlsx`** ("Overview Memory Map" / "Peripherals Memory Map" tabs). All addresses in chapters 4–5 are taken from that attachment and replace the earlier S32K3-derived estimates.
>
> **Revision note (2026-10-14)**: Rev.B — every address in §4/§5 has been replaced with values verified against the Rev.3 memory map. Twelve of the thirteen open items in §11 are now closed. New findings added: `WXN` reset value, ATCM-vs-WXN conflict, TCM backdoor matrix, REG_PROT strongly-ordered coupling, secure/non-secure alias rule, OMU read-only remap, XRDC lacking XN.
>
> **Caveat**: Register encodings follow the Arm architecture specification. All values must be cross-checked against the Reference Manual of the specific derivative before production.

---

### 1. Why MPU design is mandatory on S32K5

S32K5 is an ASIL D platform with three heterogeneous core clusters sharing one MRAM and SRAM pool:

| Cluster | Role | S32K566 configuration | Typical tasks |
| --- | --- | --- | --- |
| Cortex-R52 | Compute / real-time | 2 cores (single cluster; 1×Lockstep or 2×Single Core) | Safety monitoring, real-time control, hypervisor |
| Cortex-M7 | Platform | **4 cores** (lockstep-only: 3 user cores; decoupled: 2 lockstep + 2 single) | Communication stacks, non-real-time tasks, gateway |
| Cortex-M4 | Low-power engine | 1 core | Keep-alive during LPRUN / Standby |

> **Correction**: earlier revisions of this document stated "6 Cortex-M7 cores" for S32K566. RM Rev.3 Table 9 ("Arm platforms: description") specifies **four** Cortex-M7 processors for the main platform domain. The "6×" figure in the family feature table counts lockstep pairs as two logical cores; the memory map and MSCM both expose only `M7_0`–`M7_3`. MPU region budgeting must use **4**.
> `[来源: rm1131130 Rev.3, Chapter_02 Table 9; memory_map.xlsx ITCM_0..3 / DTCM_0..3]`

In this system the MPU provides **responsibility isolation**, not merely memory protection:

1. **Inter-core isolation** — R52 and M7 each own separate SRAM partitions (1 MB for R52, 1.5 MB for M7). The MPU guarantees a task on one core cannot cross a boundary and corrupt another core's stack or data.
2. **Multi-task isolation** — mixed Linux/RTOS load on M7, AUTOSAR OS on R52; both need task-level protection.
3. **Fail-safe behaviour** — an illegal access must be **caught immediately and converted into a controlled exception**, rather than silently propagating the error onto bus transactions. This is essential for ASIL D memory safety (avoiding uncontrolled jumps into RAM).
4. **Cache attribute consistency** — S32K5 MRAM/SRAM is partitioned in hardware into cacheable / non-cacheable / shareable regions (visible in the linker as `int_sram_no_cacheable`, `int_sram_shareable`). The MPU is the only software-side mechanism to unify these attributes.

> **Safety-critical reminder**: The MPU does **not** provide runtime address relocation. Once a memory range is left unconfigured, the MPU permits access — it is a *whitelist filter*, not a sandbox. Missing one region means giving up protection for that region entirely.
>
> **An even more important point**: the MPU constrains only **the local core** and **cannot stop DMA**. eDMA, the Ethernet MAC, CAN and other masters bypass the CPU's MPU and drive the bus directly. Intercepting them requires **XRDC** (NXP's Extended Resource Domain Controller) — see 5.8. A safety design on S32K5 that only covers the MPU leaves a wide-open door for uncontrolled writes.

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 452" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" role="img">
<title>MPU architecture differences between Cortex-M7 and Cortex-R52</title>
<desc>Left: Cortex-M7 with ARMv7-M PMSAv7 uses MPU_RNR/RBAR/RASR with SIZE-encoded region size, subregion disable and overlap priority by region number. Right: Cortex-R52 with Armv8-R PMSAv8-32 uses PRBAR/PRLAR base-limit register pairs, 64-byte granularity, no overlapping regions, and dual EL1/EL2 MPUs taking the least permissive combination.</desc>
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<rect x="40" y="20" width="285" height="410" rx="14" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="182" y="46" text-anchor="middle" font-size="14" font-weight="500" fill="#0C447C">Cortex-M7</text>
<text x="182" y="66" text-anchor="middle" font-size="12" fill="#185FA5">ARMv7-M PMSAv7</text>
<rect x="60" y="84" width="245" height="66" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
<text x="182" y="105" text-anchor="middle" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">Register model</text>
<text x="182" y="124" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">RNR + RBAR + RASR</text>
<text x="182" y="140" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">Base + SIZE encoding</text>
<rect x="60" y="162" width="245" height="66" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
<text x="182" y="183" text-anchor="middle" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">Region count</text>
<text x="182" y="202" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">Up to 16 (8-15 optional)</text>
<text x="182" y="218" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">MPU_TYPE.DREGION detectable</text>
<rect x="60" y="240" width="245" height="66" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
<text x="182" y="261" text-anchor="middle" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">Region behaviour</text>
<text x="182" y="280" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">Overlap allowed, higher number wins</text>
<text x="182" y="296" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">SRD masks 8 subregions</text>
<rect x="60" y="318" width="245" height="66" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
<text x="182" y="339" text-anchor="middle" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">Privilege tiers</text>
<text x="182" y="358" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">Privileged / unprivileged</text>
<text x="182" y="374" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">Single MPU_CTRL set</text>
<rect x="60" y="396" width="245" height="20" rx="6" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="182" y="406" text-anchor="middle" font-size="12" fill="#2C2C2A" dominant-baseline="central">Fault: MemManage</text>
<rect x="355" y="20" width="285" height="410" rx="14" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="497" y="46" text-anchor="middle" font-size="14" font-weight="500" fill="#3C3489">Cortex-R52</text>
<text x="497" y="66" text-anchor="middle" font-size="12" fill="#534AB7">Armv8-R PMSAv8-32</text>
<rect x="375" y="84" width="245" height="66" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="497" y="105" text-anchor="middle" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">Register model</text>
<text x="497" y="124" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">PRBAR + PRLAR register pair</text>
<text x="497" y="140" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">Base + limit (inclusive)</text>
<rect x="375" y="162" width="245" height="66" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="497" y="183" text-anchor="middle" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">Region count</text>
<text x="497" y="202" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">EL1: 16 / 20 / 24</text>
<text x="497" y="218" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">EL2: 0 / 16 / 20 / 24</text>
<rect x="375" y="240" width="245" height="66" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="497" y="261" text-anchor="middle" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">Region behaviour</text>
<text x="497" y="280" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">Overlap forbidden, multiple hits fault</text>
<text x="497" y="296" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">64 B granularity, no SRD</text>
<rect x="375" y="318" width="245" height="66" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="497" y="339" text-anchor="middle" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">Privilege tiers</text>
<text x="497" y="358" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">EL0 / EL1 / EL2</text>
<text x="497" y="374" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">Dual MPU, least permissive</text>
<rect x="375" y="396" width="245" height="20" rx="6" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="497" y="406" text-anchor="middle" font-size="12" fill="#2C2C2A" dominant-baseline="central">Fault: permission + translation</text>
<path d="M325 225 L355 225" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)" marker-start="url(#ar)"/>
<text x="340" y="212" text-anchor="middle" font-size="11" fill="#5F5E5A">different</text>
</svg>
</figure>

---

### 2. Cortex-M7 MPU in detail (ARMv7-M PMSAv7)

#### 2.1 Register set

The M7 has **one** MPU only, located in the System Control Space (SCS) at base `0xE000ED90`:

| Register | Address | Function |
| --- | --- | --- |
| `MPU_TYPE` | `0xE000ED90` | Read-only; detects MPU presence and region count (DREGION) |
| `MPU_CTRL` | `0xE000ED94` | Enables the MPU, background region, fault-period behaviour |
| `MPU_RNR` | `0xE000ED98` | Selects the region number to operate on |
| `MPU_RBAR` | `0xE000ED9C` | Region base address + VALID |
| `MPU_RASR` | `0xE000EDA0` | Region attributes + size + enable |

The programming model is **"select the number first, then write attributes"**: write `MPU_RNR = n`, then write `MPU_RBAR` and `MPU_RASR`. CMSIS wraps this in `ARM_MPU_SetRegion()`.

#### 2.2 MPU_RASR bit fields

```
 31        28  26  24  21  19  18  17  16   15    8  6  5    1   0
┌────────────┬───────┬───────┬───┬─┬───┬───┬────────┬──┬──────┬───┐
│   ATTRS    │  RES  │ AP[2:0]│TEX│S│ C│ B │  SRD   │R │ SIZE │EN │
└────────────┴───────┴───────┴───┴─┴───┴───┴────────┴──┴──────┴───┘
              XN
```

| Field | Bits | Description |
| --- | --- | --- |
| `XN` | `[28]` | Execute Never; 1 = instruction fetch from this region forbidden |
| `AP[2:0]` | `[26:24]` | Access permission, see table below |
| `TEX[2:0]` | `[21:19]` | Memory type extension, combined with C/B/S |
| `S` | `[18]` | Shareable |
| `C` | `[17]` | Cacheable |
| `B` | `[16]` | Bufferable |
| `SRD[7:0]` | `[15:8]` | Subregion disable; 8 subregions when size ≥ 256 B |
| `SIZE[4:0]` | `[5:1]` | Region size = 2^(SIZE+1) bytes; values < 4 reserved (minimum 32 B) |
| `ENABLE` | `[0]` | Region enable (requires `MPU_CTRL.ENABLE` too) |

**Base alignment constraint**: a region's ADDR must be aligned to its SIZE. For example, a 64 KB region must fall on a `0x00010000` boundary, not `0x00010001`. This is the single most common PMSAv7 pitfall — if a linker-script section is not aligned to a power of two, the low bits of the written ADDR are ignored and the MPU actually protects a region **twice as large** as intended.

#### 2.3 AP access permission encoding

| AP[2:0] | Privileged | Unprivileged | Notes |
| --- | --- | --- | --- |
| `000` | No access | No access | Any access generates a permission fault |
| `001` | Read/Write | No access | Privileged access only |
| `010` | Read/Write | Read-only | Unprivileged writes fault |
| `011` | Read/Write | Read/Write | Full access |
| `100` | unpredictable | unpredictable | **Reserved, do not use** |
| `101` | Read-only | No access | Privileged read-only |
| `110` | Read-only | Read-only | Privileged and unprivileged read-only |
| `111` | Read-only | Read-only | Same as 110 |

#### 2.4 TEX/C/B/S memory attribute encoding

| TEX | C | B | Memory type / cacheability | Shareable |
| --- | --- | --- | --- | --- |
| `000` | 0 | 0 | Strongly-ordered | Always Shareable |
| `000` | 0 | 1 | Device, Shared device | Always Shareable |
| `000` | 1 | 0 | Normal, WT, no write-allocate | S bit |
| `000` | 1 | 1 | Normal, WB, no write-allocate | S bit |
| `001` | 0 | 0 | Normal, Non-cacheable | S bit |
| `001` | 0 | 1 | Reserved | — |
| `001` | 1 | 0 | Implementation defined | — |
| `001` | 1 | 1 | Normal, WB, write+read allocate | S bit |
| `010` | 0 | 0 | Device, Non-shared device | Always Non-shareable |
| `010` | 0 | 1 | Reserved | — |
| `010` | 1 | X | Reserved | — |
| `011` | X | X | Reserved | — |
| `1BB` | `BAA` | `A` | Normal, Cached (AA/BB encode cache policy) | S bit |

Cache policy for `{TEX,C,B} = 1BB`, where AA/BB are:

| AA or BB | Cacheability policy |
| --- | --- |
| `00` | Non-cacheable |
| `01` | Write-back, write and read allocate |
| `10` | Write-through, no write allocate |
| `11` | Write-back, no write allocate |

**Peripherals must use the Device type.** This is the most frequent error on M7: configuring the UART, FLEXCAN or GPIO register window as Normal cacheable makes registers read back stale values and swallows peripheral writes into the cache. The correct encoding is `TEX=000, C=0, B=1` (Shared Device) or `TEX=010, C=0, B=0` (Non-shared Device).

#### 2.5 MPU_CTRL three-bit semantics

| Bit | Name | Semantics |
| --- | --- | --- |
| `0` | `ENABLE` | MPU master enable. When 0, all other register settings are inactive |
| `1` | `HFNMIENA` | Whether the MPU stays enabled during HardFault / NMI / FAULTMASK handlers |
| `2` | `PRIVDEFENA` | Whether privileged code may use the default memory map as a background region |

Trade-off on `HFNMIENA`: when `=0` the fault handler itself is unconstrained by the MPU, which makes a full memory dump for offline analysis easy; when `=1` even the fault handler is constrained, giving stronger anti-tampering but potentially incomplete scene data. Safety-diagnostic firmware usually sets 0 and stores the scene in a dedicated no-cacheable region.

#### 2.6 Region overlap and subregions

- **On overlap, the higher region number wins**: if regions 0 and 1 both cover the same memory, region 1's attributes apply. This is PMSAv7's most useful feature — you can set a broad baseline with one large region and then tighten it with a smaller overlapping region.
- **SRD subregions**: when the region is ≥ 256 B it is divided into 8 equal subregions; `SRD[n]=1` disables subregion n, with `SRD[0]` mapping to the lowest-address subregion. **Note: for regions of 32/64/128 B, writing SRD has unpredictable effects.**

#### 2.7 Recommended M7 memory attributes (S32K5 perspective)

| Region | Address / size | TEX/C/B | AP | XN | Notes |
| --- | --- | --- | --- | --- | --- |
| Code MRAM | `0x0800_0000`, 32 MB | `001/1/1` WB | `011` | 0 | Executable and writable (RW needed for FOTA A/B swap) |
| M7 SRAM0-2 | `0x2100_0000`–`0x212F_FFFF`, 3 MB | `001/1/1` WB | `011` | 1 | Stack, heap, .data/.bss — **data, so XN=1** |
| SRAM NC sub-partition | per linker script | `001/0/0` NC | `011` | 1 | Data that must stay consistent with hardware / other cores |
| LPE_SRAM (M7 view) | `0x1000_0000`, 256 KB | `001/0/0` NC | `011` | 1 | Rev.A's "Standby RAM `0x2040_0000`" was S32K3 — see §4.1 correction 3 |
| ITCM | `0x0000_0000`, 32 KB | `001/1/1` WB | `011` | 0 | Interrupt vectors and hot code. **Shares the 1 MB window with LPE_SRAM alias** |
| DTCM | `0x2000_0000`, 64 KB | `001/1/1` WB | `011` | 1 | Stack data, non-executable |
| Peripheral window | `0x4000_0000`–`0x421F_FFFF` | `010/0/0` Device | `011` or `101` | 1 | Must be Device type — also required for REG_PROT error capture (§5.7) |
| XSPI data | `0x8100_0000`–`0xC0FF_FFFF` | `001/0/0` NC | `011` | 0 | External flash execution |
| PPB | `0xE000_0000`–`0xE00F_FFFF` | `010/0/0` Device | `101` | 1 | Core-private |

#### 2.8 M7 configuration code skeleton

```c
#include "core_cm7.h"

#define MPU_RNR(n)    (*((volatile uint32_t *)0xE000ED98U + (n) * 8U))
#define MPU_RBAR(n)   (*((volatile uint32_t *)0xE000ED9CU + (n) * 8U))
#define MPU_RASR(n)   (*((volatile uint32_t *)0xE000EDA0U + (n) * 8U))
#define MPU_CTRL      (*((volatile uint32_t *)0xE000ED94U))
#define MPU_RBAR_VALID_Msk  (1UL << 4)

static inline uint32_t rasr_make(uint32_t size_log2_minus1,
                                  uint8_t  ap, uint8_t tex,
                                  uint8_t c, uint8_t b, uint8_t s,
                                  uint8_t xn, uint8_t srd)
{
    return (size_log2_minus1 << 1) | ((tex & 0x7U) << 19) |
           ((s & 0x1U) << 18)   | ((c & 0x1U) << 17) |
           ((b & 0x1U) << 16)   | ((srd & 0xFFU) << 8) |
           ((ap & 0x7U) << 24)  | ((xn & 0x1U) << 28) | 1UL;
}

void M7_MPU_Init(void)
{
    uint32_t ctl;

    /* 1. Disable the MPU before configuring, avoiding faults mid-transition */
    MPU_CTRL = 0U;
    __DSB();
    __ISB();

    /* 2. Write each region. The programming code must not live in a region
     *    that is being reconfigured. */
    /* Region 0: peripheral Device Non-shareable, RO, XN */
    MPU_RNR(0)  = 0U;
    MPU_RBAR(0) = 0x40000000U | MPU_RBAR_VALID_Msk;
    MPU_RASR(0) = rasr_make(29U,        /* SIZE=29 -> 2^30 = 1 GB      */
                            5U,         /* AP=101 privileged RO       */
                            2U, 0U, 0U, /* TEX=010,C=0,B=0 -> Device  */
                            0U,         /* S=0 non-shareable          */
                            1U,         /* XN=1                       */
                            0x00U);

    /* Region 1: SRAM cacheable, RW, XN (data) */
    MPU_RNR(1)  = 1U;
    MPU_RBAR(1) = 0x20400000U | MPU_RBAR_VALID_Msk;
    MPU_RASR(1) = rasr_make(19U,        /* SIZE=19 -> 2^20 = 1 MB      */
                            3U,         /* AP=011 full access         */
                            1U, 1U, 1U, /* TEX=001,C=1,B=1 -> WB      */
                            0U,
                            1U,         /* XN=1                       */
                            0x00U);

    /* Region 2: Code MRAM, RW, executable */
    MPU_RNR(2)  = 2U;
    MPU_RBAR(2) = 0x08000000U | MPU_RBAR_VALID_Msk;
    MPU_RASR(2) = rasr_make(28U,        /* SIZE=28 -> 2^29 = 512 MB   */
                            3U,
                            1U, 1U, 1U,
                            1U,         /* S=0                        */
                            0U,         /* XN=0 execution permitted   */
                            0x00U);

    /* 3. DSB before enabling, ensuring all writes have landed */
    __DSB();

    /* 4. Enable the MPU, keeping the privileged default map as background */
    ctl = MPU_CTRL;
    ctl |= (1UL << 0)   /* ENABLE      */
        |  (1UL << 2);  /* PRIVDEFENA */
    MPU_CTRL = ctl;
    __DSB();
    __ISB();
}

uint32_t M7_MPU_GetRegionCount(void)
{
    return (MPU_TYPE >> 8) & 0xFFU;   /* DREGION field */
}
```

> The SIZE values above must be adapted to the actual linker script. **Always confirm via `MPU_TYPE.DREGION` how many regions are implemented before accessing them** — accessing an out-of-range region number is undefined behaviour.

#### 2.9 MemManage exception handling

```c
void MemManage_Handler(void)
{
    /* 1. Capture the scene first, clean up later */
    uint32_t ipsr   = __get_IPSR();
    uint32_t mfsr   = SCB->CFSR & 0xFFU;        /* MemManage status */
    uint32_t hfsr   = SCB->CFSR >> 16;
    uint32_t mmfar  = SCB->MMFAR;               /* Faulting address */
    uint32_t bfar   = SCB->BFAR;
    uint32_t stacked_pc, stacked_lr;
    __asm volatile("mov %0, lr\n" : "=r"(stacked_lr));
    __asm volatile("mov %0, pc\n" : "=r"(stacked_pc));

    /* 2. Store in a no-cacheable region for the diagnostic firmware to read */
    FaultRecord_SafeStore(ipsr, mfsr, hfsr, mmfar, bfar,
                          stacked_pc, stacked_lr);

    /* 3. ASIL D requires a controlled stop or safe state, not a retry loop */
    Safety_EnterSafeState(FAULT_SRC_MEMM, mmfar);
    for (;;) { }
}
```

MFSR byte in `SCB->CFSR` (critical for determining direction):

| Bit | Meaning |
| --- | --- |
| `0` | IACCVIOL — permission violation on instruction fetch |
| `1` | DACCVIOL — permission violation on data access |
| `3` | MUNSTKERR — invalid stack pointer on exception return |
| `4` | MSTKERR — invalid stack pointer on stacking |
| `5` | MLSPERR — floating-point stacking error |
| `7` | MMARVALID — address in MMFAR is valid |

---

### 3. Cortex-R52 MPU in detail (Armv8-R PMSAv8-32)

#### 3.1 The dual-MPU model

The R52 has **two independent MPUs** — the largest architectural difference from the M7:

| MPU | Controlled by | Region count | Scope |
| --- | --- | --- | --- |
| EL1 MPU | EL1 (EL2 may write it) | 16 / 20 / 24 | EL0 and EL1 accesses |
| EL2 MPU | EL2 (hypervisor) | 0 / 16 / 20 / 24 (optional) | Overlaid on EL0/EL1 |

Combination rules:

- **EL0/EL1 access** → looked up in **both** MPUs; the **least permissive** combination wins
- **EL2 access** → EL2 MPU only
- The EL2 MPU can be disabled wholesale (S32K5 typically does not use virtualization; keep the EL2 MPU off)

#### 3.2 Registers and AArch32 access

| Register | Function |
| --- | --- |
| `PRBAR` / `PRLAR` | EL1 region base / limit |
| `HPRBAR` / `HPRLAR` | EL2 region base / limit |
| `MAIR0` / `MAIR1` | Memory attribute indirection; 8 attributes × 8 bit |
| `PRENR` / `HPRENR` | Region enable (bitmask) |
| `PRSELR` / `HPRSELR` | Select the target region number |
| `MPUIR` / `HMPUIR` | Region information (read-only, detection) |

Two programming methods:

```asm
@ Method 1: indirect via PRSELR
MOV   R0, #0                  @ Select region 0
MCR   p15, 0, R0, c6, c2, 1   @ Write PRSELR
MCR   p15, 0, R1, c6, c3, 0   @ Write PRBAR
MCR   p15, 0, R2, c6, c3, 1   @ Write PRLAR

@ Method 2: direct access to PRBARn / PRLARn (op1 encoded into c8+)
MCR   p15, 0, R1, c6, c8+n[3:1], 4*n[0]      @ Read PRBARn
MCR   p15, 0, R1, c6, c8+n[3:1], 4*n[0]+1    @ Read PRLARn
```

> **Easy mistake**: the `op1` computation for direct access is error-prone (involving `c8 + n[3:1]` and `4*n[0]`). Prefer the PRSELR indirect method, or use the CMSIS `__set_PRBAR()` inline functions.

#### 3.3 Region definition: base + limit

The fundamental difference from PMSAv7:

| Feature | PMSAv7 (M7) | PMSAv8-32 (R52) |
| --- | --- | --- |
| Definition | BASE + SIZE | BASE + LIMIT |
| Limit semantics | Implicit | **Inclusive of endpoint** |
| Alignment | BASE aligned to SIZE | BASE and LIMIT both aligned to 64 B |
| Minimum size | 32 B | **64 B** |
| Overlap | Permitted, higher number wins | **Forbidden; multiple hits raise a translation fault** |

Region address range:

```
PRBAR.BASE:0b000000 <= address <= PRLAR.LIMIT:0b111111
```

The colon is the bit-concatenation operator. This means the low 6 bits of BASE are read as 0 and the low 6 bits of LIMIT are read as 1 — **the effective granularity is 64 bytes, and both ends are inclusive.** This is more intuitive than the M7's "align to SIZE", and it means a misconfiguration does not silently double the region size as on M7; instead it raises an exception immediately — fail-fast.

#### 3.4 PRBAR / PRLAR fields

| Field | Register | Semantics |
| --- | --- | --- |
| `BASE` | PRBAR | Region base address (low 6 bits read as 0) |
| `AP` | PRBAR | Access permission, 2 bit |
| `SH` | PRBAR | Shareability |
| `LIMIT` | PRLAR | Region limit (inclusive of endpoint; low 6 bits read as 1) |
| `AttrIndx` | PRLAR | Memory attribute index, indexes MAIRx |
| `EN` | PRLAR | Region enable |

**AP encoding**:

| AP | Meaning |
| --- | --- |
| `00` | Read/Write, this EL and lower |
| `01` | Read/Write, this EL only |
| `10` | Read-only, this EL and lower |
| `11` | Read-only, this EL only |

**SH encoding**:

| SH | Meaning |
| --- | --- |
| `00` | Non-shareable |
| `10` | Outer-shareable |
| `11` | Inner-shareable |

#### 3.5 MAIR memory attribute indirection

The R52 moves memory attributes out of the region registers into `MAIRx`; each MPU has 8 slots of 8 bits:

| AttrIndx | Typical value | Memory type |
| --- | --- | --- |
| 0 | `0xFF` | Normal, Inner/Outer RW, Write-back, Write-allocate (MRAM/SRAM) |
| 1 | `0x04` | Device-nGnRnE (peripherals) |
| 2 | `0xBB` | Normal, Inner/Outer RW, Write-through (no write-allocate) |
| 3 | `0x04` | Device-nGnRE |

Programming:

```asm
@ Update Attr0 and Attr1 of MAIR_EL1
MRC   p15, 0, R0, c10, c2, 0       @ Read MAIR0
LDR   R1, =0xFF
BFI   R0, R1, #0, #8              @ Attr0 = 0xFF (Normal WB RA)
LDR   R1, =0x04
BFI   R0, R1, #8, #8              @ Attr1 = 0x04 (Device-nGnRnE)
MCR   p15, 0, R0, c10, c2, 0       @ Write back
DSB
ISB
```

#### 3.6 Background region and default memory map

**Instruction-access background region**:

| Address range | SCTLR.I=1 | SCTLR.I=0 | XN |
| --- | --- | --- | --- |
| `0x0000_0000`–`0x7FFF_FFFF` | Normal, Non-shareable, WT cacheable | Normal, Shareable, Non-cacheable | Execution permitted |
| `0x8000_0000`–`0xFFFF_FFFF` | — | — | **Execute-never** |

**Data-access background region**:

| Address range | SCTLR.C=1 | SCTLR.C=0 |
| --- | --- | --- |
| `0x0000_0000`–`0x3FFF_FFFF` | Normal, Non-shareable, WB WA cacheable | Normal, Shareable, NC |
| `0x4000_0000`–`0x5FFF_FFFF` | Normal, Non-shareable, WT cacheable | Normal, Shareable, NC |
| `0x6000_0000`–`0x7FFF_FFFF` | Normal, Shareable, NC | Normal, Shareable, NC |
| `0x8000_0000`–`0xBFFF_FFFF` | Device-nGnRE | Device-nGnRE |
| `0xC000_0000`–`0xFFFF_FFFF` | Device-nGnRnE | Device-nGnRnE |

Note that everything above `0x8000_0000` defaults to Device type — exactly where the S32K5 peripheral windows live, so the default attribute is coincidentally the safe one (non-cacheable).

**Key control bits**:

| Bit | Function |
| --- | --- |
| `SCTLR.M` | EL1 MPU enable. When 0, the default memory map is used |
| `SCTLR.BR` | Background region check. When 1, EL1 privileged accesses missing all regions may use the background region |
| `HCR.DC` | Default cacheability. When 1, the background region uses Normal IB-OB WB + RA attributes |
| `HCR.VM` | Virtualization flag; when set, EL0/EL1 perform a two-stage MPU lookup |

> **Trap**: with `HCR.DC = 1` the default attributes are the **most permissive** (Normal, IB-OB WB, RA). After combination with the EL2 MPU attributes the result still equals the EL2 attributes, making the EL2 MPU completely transparent over the background region. In other words, `DC=1` strips the EL1 background region of its protective value; for S32K5 without virtualization, keep `DC=0`.

#### 3.7 Fault types

| Fault | Trigger condition |
| --- | --- |
| Permission fault | Access hits a region but the permission disallows it |
| Translation fault | Access hits multiple regions (overlap); or hits no region and the background region is unusable |

The M7 raises only permission faults (on MPU overlap the highest-number region is simply selected), whereas the R52 turns "overlap" from a feature into an error.

#### 3.8 R52 configuration code skeleton

```c
#include <stdint.h>

#define PRBAR(n)  (*((volatile uint32_t *)(uintptr_t)(0x42000000U + 8U * (n))))
#define PRLAR(n)  (*((volatile uint32_t *)(uintptr_t)(0x42000004U + 8U * (n))))
#define PRSELR    (*((volatile uint32_t *)0xE000ED90U))   /* Confirm against integration */

/* MAIR attribute slots */
#define ATTR_NORMAL_WB   0U
#define ATTR_DEVICE      1U

#define AP_RW_EL0_1      0U   /* Read/Write, this EL and lower */
#define AP_RO_EL0_1      2U
#define SH_NON_SHAREABLE 0U

static inline uint32_t mair_attr(uint8_t idx, uint8_t val)
{
    return (uint32_t)val << (8U * idx);
}

/* Build PRBAR/PRLAR from BASE/LIMIT: both aligned to 64B */
static inline uint32_t prbar_make(uint32_t base, uint8_t ap, uint8_t sh)
{
    return (base & 0xFFFFFFC0U) | ((uint32_t)sh << 6) | ((uint32_t)ap << 2);
}

static inline uint32_t prlar_make(uint32_t limit, uint8_t attr_idx, uint8_t xn)
{
    return (limit & 0xFFFFFFC0U) | 0x3FU
           | ((uint32_t)xn << 8)
           | ((uint32_t)(attr_idx & 0x7U) << 1)
           | 1UL;                       /* EN */
}

void R52_MPU_Init(void)
{
    uint32_t mair;

    /* 1. Disable the EL1 MPU */
    *((volatile uint32_t *)0xE000ED10U) &= ~(1UL << 0);  /* SCTLR.M = 0 */
    __DSB();
    __ISB();

    /* 2. Configure MAIR: Attr0 = Normal WB RA, Attr1 = Device-nGnRnE */
    mair = mair_attr(ATTR_NORMAL_WB, 0xFF) | mair_attr(ATTR_DEVICE, 0x04);
    __set_MAIR(mair);

    /* 3. Region 0: Code MRAM, executable and writable */
    PRBAR(0) = prbar_make(0x08000000U, AP_RW_EL0_1, SH_NON_SHAREABLE);
    PRLAR(0) = prlar_make(0x0FFFFFFFU, ATTR_NORMAL_WB, 0U);  /* XN=0 */

    /* Region 1: R52 SRAM, RW, non-executable */
    PRBAR(1) = prbar_make(0x20400000U, AP_RW_EL0_1, SH_NON_SHAREABLE);
    PRLAR(1) = prlar_make(0x204FFFFFU, ATTR_NORMAL_WB, 1U);  /* XN=1 */

    /* Region 2: peripheral Device, RO, non-executable */
    PRBAR(2) = prbar_make(0x40000000U, AP_RO_EL0_1, SH_NON_SHAREABLE);
    PRLAR(2) = prlar_make(0xFFFFFFFFU, ATTR_DEVICE, 1U);

    __DSB();
    __ISB();

    /* 4. Enable SCTLR.M, and set BR so privileged accesses may use the
     *    background region */
    *((volatile uint32_t *)0xE000ED10U) |= (1UL << 0);   /* M  = 1 */
    __DSB();
    __ISB();

    /* 5. Enable regions via PRENR (if not already set in PRLAR.EN) */
    /* PRENR |= 0x7U; */
}
```

> R52 system-register access must go through `MCR p15, ...` or CMSIS inline functions; you cannot simply dereference a memory address as on the M7. The `PRBAR(n)` base address and the `SCTLR` address in the code above must be confirmed against the NXP integration manual.

#### 3.9 Programming rules (Arm requirement)

1. When reconfiguring a region, **the programming code itself must not reside in that region** — otherwise the instant the permission changes, instruction fetch fails and the CPU wedges.
2. Execute **DSB** before changing `PRBAR`/`PRLAR` to ensure all prior memory accesses complete.
3. Execute **ISB** after the change to flush the pipeline and make the new attributes take effect.

These three rules apply equally to the M7.

---

### 4. S32K5 memory map and MPU layout

#### 4.1 Key memory resources

All values below are the **S32K566** figures from `S32K5xx_memory_map.xlsx`; the "Max size" column is the architectural window, "Actual" is what this derivative implements.

| Resource | Window (start–end) | Max size | S32K566 actual | Actual end | Attribute | Accessor |
| --- | --- | --- | --- | --- | --- | --- |
| Code MRAM | `0x0800_0000`–`0x0BFF_FFFF` | 64 MB | **32 MB** | `0x09FF_FFFF` | ECC, cacheable | All cores |
| Data MRAM | `0x0C80_0000`–`0x0C83_FFFF` | 256 KB | **256 KB** | `0x0C83_FFFF` | ECC | All cores |
| Non-secure OTP | `0x0C40_4000`–`0x0C42_0FFF` | 116 KB | 48 KB | `0x0C40_FFFF` | — | — |
| UTEST | `0x0C8F_E000`–`0x0C90_FFFF` | 72 KB | 40 KB | `0x0C90_7FFF` | — | — |
| M7 SRAM (SRAM0/1/2) | `0x2100_0000`–`0x212F_FFFF` | 3 MB | **3 MB** (3×1 MB) | `0x212F_FFFF` | ECC, incl. NC / shareable partitions | M7 cluster |
| R52 SRAM (CPE_SRAM0-3) | `0x2200_0000`–`0x220F_FFFF` | 1 MB | **1 MB** (4×256 KB) | `0x220F_FFFF` | ECC | R52 cluster |
| CPE_LLC0 Scratchpad | `0x0700_0000`–`0x073F_FFFF` | 4 MB | 960 KB | `0x070E_FFFF` | ECC | CPE |
| CPE_LLC1 Scratchpad | `0x0F00_0000`–`0x0F3F_FFFF` | 4 MB | 448 KB | `0x0F06_FFFF` | ECC | CPE |
| LPE_SRAM Code | `0x1000_0000`–`0x100F_FFFF` | 1 MB | 256 KB | `0x1003_FFFF` | ECC | LPE |
| LPE_SRAM Data | `0x2400_0000`–`0x240F_FFFF` | 1 MB | 128 KB | `0x2401_FFFF` | ECC | LPE |
| ITCM (per M7) | `0x0000_0000`–`0x000F_FFFF` | 1 MB | **32 KB** | `0x0000_7FFF` | ECC, cacheable | M7 |
| DTCM (per M7) | `0x2000_0000`–`0x200F_FFFF` | 1 MB | **64 KB** | `0x2000_FFFF` | ECC, cacheable | M7 |
| R52 ATCM/BTCM/CTCM (per core) | `0x0100_0000`–`0x016F_FFFF` | 1 MB each | **32 KB each** | `0x0160_7FFF` | ECC, zero wait state | R52 |
| XSPI/QSPI flash | `0x8100_0000`–`0xDFFF_FFFF` | 1556480 KB | 1024 MB | `0xC0FF_FFFF` | — | External flash |
| Peripheral bridges | `0x4000_0000`–`0x421F_FFFF` | — | 34 MB used | `0x4219_7FFF` | Device | All cores |
| PPB | `0xE000_0000`–`0xE00F_FFFF` | 1 MB | **1 MB** | `0xE00F_FFFF` | Device | Core-private |

**Three corrections against earlier revisions of this document:**

1. **M7 SRAM is at `0x2100_0000`, not `0x2040_0000`.** The `0x204x_xxxx` addresses in Rev.A came from an NXP S32K Knowledge Base linker example for **S32K3** and do not exist in the S32K5 memory map at all. S32K566 has SRAM0/1/2, each 1 MB, contiguous at `0x2100_0000`–`0x212F_FFFF`.
2. **R52 SRAM (`cpe_sram`) is at `0x2200_0000`–`0x220F_FFFF`**, four 256 KB banks (CPE_SRAM0-3) — not `0x2040_0000`–`0x204F_FFFF`.
3. **Standby RAM is not a separately-mapped 256 B region on S32K5.** The 256 B figure in Rev.A was S32K3's. On S32K5 the LPE retains 384 KB of `LPE_SRAM` in Standby mode; there is no dedicated 256 B standby window in the memory map. The "Standby RAM must be non-cacheable" hard constraint therefore **does not apply as written** — verify against the LPE Overview chapter before relying on it.

> **ITCM / LPE_SRAM address collision (S32K5-specific, easy to miss)**: `ITCM_0..3` and `Code LPE_SRAM Alias` **both start at `0x0000_0000`** and share the same 1 MB window, differing only in implemented size (32 KB vs 256 KB). An MPU cannot separate them by address — the distinction is *which core is executing*. Any region covering `0x0000_0000` is simultaneously "M7 ITCM" and "LPE SRAM alias".
> `[来源: memory_map.xlsx, Overview Memory Map rows ITCM_0..3 / Code LPE_SRAM Alias]`

S32K5 partitions SRAM in hardware into cacheable / non-cacheable / shareable blocks (reflected in the linker as `int_sram_no_cacheable` and `int_sram_shareable`); the MPU configuration must **strictly match this partitioning**, otherwise conflicting software and hardware attributes produce unpredictable behaviour.

#### 4.2 Recommended M7 region layout (16-region budget)

M7 implements **16 regions** (`MPU_TYPE` reset `0x00001000`). `[来源: rm1131130 Rev.3, Chapter_02 Table 10]`

| # | Region | BASE | LIMIT | Size | Attributes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | ITCM (self) | `0x0000_0000` | `0x0000_7FFF` | 32 KB | RWX, NC | Vector table + hot ISRs. **Shares the 1 MB window with LPE_SRAM alias — see 4.1** |
| 1 | Code MRAM | `0x0800_0000` | `0x09FF_FFFF` | 32 MB | RWX, WB | FOTA requires RW; immutability needs XRDC |
| 2 | Data MRAM | `0x0C80_0000` | `0x0C83_FFFF` | 256 KB | RW, WB, XN | |
| 3 | DTCM (self) | `0x2000_0000` | `0x2000_FFFF` | 64 KB | RW, NC, XN | Main stack; 64-bit write initialization for ECC before reads |
| 4 | SRAM0 | `0x2100_0000` | `0x210F_FFFF` | 1 MB | RW, WB, XN | .data/.bss/heap |
| 5 | SRAM1 | `0x2110_0000` | `0x211F_FFFF` | 1 MB | RW, WB, XN | |
| 6 | SRAM2 | `0x2120_0000` | `0x212F_FFFF` | 1 MB | RW, WB, XN | NC / shareable sub-partitions live here |
| 7 | LPE_SRAM Code | `0x1000_0000` | `0x1003_FFFF` | 256 KB | R, NC, XN | Read-only view for M7 |
| 8 | PERI_LO | `0x4000_0000` | `0x403F_FFFF` | 4 MB | RO/RW, **Device**, XN | PBRIDGE3_0/1 |
| 9 | PERI_MID | `0x4040_0000` | `0x40BF_FFFF` | 8 MB | RO/RW, **Device**, XN | PBRIDGE3_2–5; contains XRDC/MSCM/ERM/EIM |
| 10 | PERI_CPE_LPE | `0x4100_0000` | `0x421F_FFFF` | 18 MB | RO/RW, **Device**, XN | CPE + LPE + DSP bridges |
| 11 | XSPI data window | `0x8100_0000` | `0xC0FF_FFFF` | 1024 MB | RO, NC, XN | External QSPI / HyperRAM |
| 12 | XSPI register window | `0x40BA_4000` | `0x40BA_BFFF` | 2 KB | RO, **Device**, XN | Controller registers; **separate region from the data window** |
| 13 | PPB | `0xE000_0000` | `0xE00F_FFFF` | 1 MB | RO, Device, XN | Core-private, separate region |
| 14–15 | Task stack guards | per linker | — | 32 KB | RO / XN | Separate stack and data |

> **Device attribute is mandatory, not advisory.** RM Ch.11 §11.3.5 NOTE: a REG_PROT transfer error is only observable on the CPU that "has defined the **strongly ordered memory region (through its MPU or MMU)** covering the target register address." Configure the peripheral window as Normal memory and REG_PROT rejections degrade into asynchronous bus errors that surface far from their cause. See §5.7.

#### 4.3 Recommended R52 region layout (20-region budget)

S32K566 implements **EL1: 20 regions, EL2: 20 regions** (not 16 or 24). `[来源: rm1131130 Rev.3, Chapter_02 Table 6 / Table 10]`

| # | Region | BASE | LIMIT | Attr | XN | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | ATCM_CPU0 | `0x0100_0000` | `0x0100_7FFF` | Normal WB-WA | **0** | Must be configured **before** enabling the MPU (see 3.9) |
| 1 | BTCM_CPU0 | `0x0110_0000` | `0x0110_7FFF` | Normal WB-WA | 1 | |
| 2 | CTCM_CPU0 | `0x0120_0000` | `0x0120_7FFF` | Normal WB-WA | 1 | |
| 3 | CPE_LLC0 | `0x0700_0000` | `0x070E_FFFF` | Normal WB-WA | 1 | |
| 4 | Code MRAM | `0x0800_0000` | `0x09FF_FFFF` | Normal WT, RO | **0** | Attributes must match the M7 side field-for-field |
| 5 | Data MRAM | `0x0C80_0000` | `0x0C83_FFFF` | Normal WB-WA | 1 | |
| 6 | CPE_LLC1 | `0x0F00_0000` | `0x0F06_FFFF` | Normal WB-WA | 1 | |
| 7 | LPE_SRAM Code | `0x1000_0000` | `0x1003_FFFF` | Normal WT, RO | **0** | |
| 8 | SysSRAM 0-2 | `0x2100_0000` | `0x212F_FFFF` | Normal WB-WA | 1 | |
| 9 | CPE_SRAM 0-3 | `0x2200_0000` | `0x220F_FFFF` | Normal WB-WA | 1 | `cpe_sram` |
| 10 | LPE_SRAM Data | `0x2400_0000` | `0x2401_FFFF` | Normal WB-WA | 1 | |
| 11 | PERI_LO | `0x4000_0000` | `0x403F_FFFF` | Device-nGnRE | 1 | |
| 12 | PERI_MID | `0x4040_0000` | `0x40BF_FFFF` | Device-nGnRE | 1 | |
| 13 | PERI_CPE_LPE | `0x4100_0000` | `0x421F_FFFF` | Device-nGnRE | 1 | |
| 14 | PPB | `0xE000_0000` | `0xE00F_FFFF` | Device-nGnRnE | 1 | **EL1-only AP** |
| 15 | XSPI virtual | `0x8100_0000` | `0xC0FF_FFFF` | Normal WT, RO | **0** | |
| 16–19 | Task-level pairs (code RO+XN=0 / data RW+XN=1) | — | — | — | — | 4 regions reserved for dynamic switching |

> The R52's **no-overlap rule** is the hardest constraint in the design (see 3.3). The table above uses **16 of 20** regions and was verified pairwise non-overlapping and 64-byte aligned; four are left for OS task switching, because RM describes the MPU's purpose as "dynamic task protection".
>
> **CPU1 differs only in TCM base**: CPU1's ATCM/BTCM/CTCM are `0x0140_0000` / `0x0150_0000` / `0x0160_0000`. CPU1 does not need regions for CPU0's TCM.
>
> **Peripheral upper bound is `0x421F_FFFF`, not `0xE00F_FFFF`.** The `0xE00FFFFF` figure in Rev.A came from the Zephyr S32K566 R52 port and is a conservative placeholder; the actual memory map shows the last peripheral bridge (LPE_PBRIDGE3) ending at `0x4219_7FFF`, with DSP_PBRIDGE3 at `0x4260_0000`–`0x427F_FFFF` and CPE_GIC0 at `0x4300_0000`–`0x431F_FFFF`. Decide deliberately whether DSP and GIC belong in the Device region or get their own.

#### 4.4 Special handling of inter-core shared areas

The regions where R52 and M7 exchange data (CAN frames, timestamps, etc.) are cross-core shared and must be configured **identically on both cores as shareable + cacheable**, combined with:

| Mechanism | Description |
| --- | --- |
| Non-shareable cacheable | For small, latency-sensitive data, configure one core as Non-shareable to avoid cache-coherency overhead |
| Kernel lockstep / atomic | Use `ldrex`/`strex` to guarantee read-modify-write atomicity |
| Mailbox / MU | S32K5's Messaging Unit registers handle inter-core synchronization and interrupt notification |
| Cache maintenance | Cross-core visibility depends on hardware coherency; S32K5 cores do not share an L1 cache, so rely on memory attributes plus barriers |

---

### 5. MPU configuration by memory type (MRAM / SRAM / TCM / XSPI / peripherals)

This section expands the layout tables of chapter 4 down to **each individual memory type**. MPU attributes are not a matter of picking "Normal WB" at random — they are dictated by the physical characteristics of the storage medium. Pick the wrong attribute and nothing faults; the feature just quietly breaks.

#### 5.1 S32K5 memory-type landscape

| Memory type | Address range | Capacity (S32K566) | ECC | Volatility | Recommended MPU attribute | Reachable cores |
| --- | --- | --- | --- | --- | --- | --- |
| Code MRAM (eMRAM) | `0x0800_0000`–`0x09FF_FFFF` | **32 MB** | Yes | Non-volatile | Normal WB RA, RWX | All cores |
| Data MRAM | `0x0C80_0000`–`0x0C83_FFFF` | 256 KB | Yes | Non-volatile | Normal WB RA, RW, XN | All cores |
| M7 SRAM0 | `0x2100_0000`–`0x210F_FFFF` | 1 MB | Yes | Volatile | Normal WB RA, RW | M7 cluster |
| M7 SRAM1 | `0x2110_0000`–`0x211F_FFFF` | 1 MB | Yes | Volatile | Normal WB RA, RW | M7 cluster |
| M7 SRAM2 | `0x2120_0000`–`0x212F_FFFF` | 1 MB | Yes | Volatile | Normal WB RA, RW | M7 cluster |
| R52 SRAM (CPE_SRAM0-3) | `0x2200_0000`–`0x220F_FFFF` | 1 MB (4×256 KB) | Yes | Volatile | Normal WB RA, RW | R52 cluster |
| CPE_LLC0 / LLC1 scratchpad | `0x0700_0000` / `0x0F00_0000` | 960 KB / 448 KB | Yes | Volatile | Normal WB-WA | CPE |
| LPE_SRAM Code | `0x1000_0000`–`0x1003_FFFF` | 256 KB | Yes | Volatile | Normal NC / WT, RO | LPE (+ others) |
| LPE_SRAM Data | `0x2400_0000`–`0x2401_FFFF` | 128 KB | Yes | Volatile | Normal WB-WA | LPE (+ others) |
| ITCM (per M7) | `0x0000_0000`–`0x0000_7FFF` | 32 KB | Yes | Volatile | Normal NC / Device, RWX | M7 |
| DTCM (per M7) | `0x2000_0000`–`0x2000_FFFF` | 64 KB | Yes | Volatile | Normal NC / Device, RW | M7 |
| R52 ATCM/BTCM/CTCM | `0x0100_0000`–`0x0160_7FFF` | 32 KB each | Yes | Volatile | Normal WB-WA | R52 |
| XSPI/QSPI external flash | `0x8100_0000`–`0xC0FF_FFFF` | 1024 MB | Device-dependent | Non-volatile | Device or Normal NC, RO | All cores |
| Peripheral window | `0x4000_0000`–`0x421F_FFFF` | 34 MB used | — | — | **Device-nGnRnE**, XN | All cores |
| PPB (private peripheral bus) | `0xE000_0000`–`0xE00F_FFFF` | 1 MB | — | — | Device-nGnRnE | Core-private |

> **Peripheral window bound, corrected.** Rev.A used `0xE00FFFFF` (from the Zephyr R52 port) and warned against `0xFFFFFFFF`. The Rev.3 memory map shows the actual last peripheral at `0x4219_7FFF`. The honest statement is: **peripherals occupy `0x4000_0000`–`0x431F_FFFF`** (including DSP_PBRIDGE3 `0x4260_0000` and CPE_GIC0 `0x4300_0000`), and everything above `0xE000_0000` is PPB plus vendor space. Whether to bound the Device region at `0x431F_FFFF` or extend it to `0xDFFF_FFFF` is a design choice — extending it is simpler but loses the ability to fault on stray accesses into unmapped space.

#### 5.2 Code MRAM (eMRAM) — the biggest architectural change in S32K5

###### Hardware characteristics

S32K5 is the industry's first automotive MCU on 16 nm FinFET with embedded MRAM. Compared with eFlash (S32K3 and earlier), MRAM overturns several low-level assumptions:

| Characteristic | MRAM (S32K5) | eFlash (S32K3 and earlier) |
| --- | --- | --- |
| Addressing | **Byte-addressable**, direct read-modify-write | Page/block-oriented |
| Erase before write | **Not required** | Mandatory |
| Write speed | 8.8–15 MB/s (sources disagree) | 1/10–1/15 of that |
| Endurance | ~1 million write cycles | ~10k–100k erase cycles |
| Retention | Conflicting figures, see below | Typically 20 years |

> **Retention data conflict (confirm against the RM)**: an NXP–TSMC 16 nm MRAM technology announcement claims 20 years at 150 °C, while another source states 10 years at 85 °C for S32K5 MRAM, below eFlash. The gap is enormous — **check the MRAM chapter of the S32K5xx RM**, since it directly drives the logging-data policy.

###### MPU configuration implications

1. **The code region is readable, writable and executable** — MRAM needs no XIP read-only protection and supports in-place FOTA A/B image swapping. But this also means **the code region can be overwritten by its own data**. If ASIL D requires "code immutable at runtime", the MPU cannot deliver it (AP bottoms out at RO, which does not constrain privileged code); you need **XRDC read-only locking**.
2. **Both cores share the same MRAM** — M7 and R52 both fetch code from Code MRAM by default (in Zephyr both use `cmram` as `zephyr,flash`). The same physical region is configured by two independent MPUs, so **the attributes must match field for field**. Otherwise one core sees it as cacheable and the other as non-cacheable, and cross-core function-pointer jumps become unpredictable.
3. **Disable the cache during FOTA writes** — although MRAM writes are fast, if the target code section is still held in the cache or pipeline during the write, clean + invalidate is required. Have the FOTA driver perform cache maintenance before and after flashing.
4. **Do not configure MRAM as Device type** — performance collapses (MRAM is meant to be used as RAM) and MRAM does support caching.

#### 5.3 M7 SRAM (3 MB, three banks)

S32K566 exposes three 1 MB SRAM banks to the M7 cluster, contiguous at `0x2100_0000`–`0x212F_FFFF`. The Rev.A table below (retained for reference) listed S32K3 partition boundaries; **those addresses do not exist on S32K5** and must not be used.

| Bank | Address range | Size | Suggested use | MPU attribute |
| --- | --- | --- | --- | --- |
| SRAM0 | `0x2100_0000`–`0x210F_FFFF` | 1 MB | .data/.bss/heap, main working set | Normal WB RA |
| SRAM1 | `0x2110_0000`–`0x211F_FFFF` | 1 MB | Secondary data, cross-core buffers | Normal WB RA or NC |
| SRAM2 | `0x2120_0000`–`0x212F_FFFF` | 1 MB | Non-cacheable / shareable partitions | **Normal NC** / WB + Shareable |

> **Rev.A content, now superseded** — the "Standby RAM `0x2040_0000` / `int_sram_fls_rsv` `0x2040_7F00` / `int_sram_no_cacheable` `0x2040_8000` / `int_sram_shareable` `0x2041_0000`" partition table came from an NXP S32K Knowledge Base linker example for **S32K3**. The *structure* (four attribute classes) is still a useful mental model, but the boundaries must be taken from the S32K5 linker script, not from those addresses.
>
> **The Standby RAM hard constraint does not carry over.** Rev.A quoted NXP: *"CM7 CPU D-Cache MUST be disabled to use the Standby RAM area. Or set the standby RAM as non-cacheable in MPU configuration."* That constraint is S32K3-specific — there is no 256 B standby window in the S32K5 memory map. On S32K5 the equivalent concern is the **384 KB `LPE_SRAM` retained through Standby**, which lives at `0x1000_0000` (code) and `0x2400_0000` (data) and is configured by the M4, not the M7.

**Zephyr correspondence**: the M7 board target uses `sram0` as `zephyr,sram`, the R52 target uses `cpe_sram`. The two DTS files point at different SRAM — they are **not two names for the same memory**. On S32K5 specifically: M7 → `0x2100_0000`, R52 → `0x2200_0000`.

#### 5.4 R52 SRAM (cpe_sram, 1 MB)

| Item | Content |
| --- | --- |
| Ownership | R52 cluster private |
| Address | **`0x2200_0000`–`0x220F_FFFF`** (four banks: CPE_SRAM0-3, 256 KB each) |
| Size | 1 MB, with ECC (SECDED) |
| Zephyr node name | `cpe_sram` |

**Key risk**: although R52 SRAM "belongs to" the R52 cluster, it is physically visible to other on-chip masters (M7, eDMA, Ethernet MAC, ...). An MPU constrains only **the local core** and **cannot stop the M7 or DMA from barging in from the bus side**. Real isolation requires **XRDC** — specifically `CPE_MRC0`–`CPE_MRC3`, one MRC per CPE_SRAMCTL bank, 16 region descriptors each.

**MPU attributes**: Normal WB RA, RW, XN=1 (data regions non-executable). R52 SRAM hosts the R52-side stacks and task data; subdivide further per task as in 4.3.

#### 5.5 TCM (ITCM / DTCM / ATCM / BTCM / CTCM) — ECC and backdoor are the two traps

###### Hardware characteristics

| Item | Description |
| --- | --- |
| Fixed base addresses | M7 ITCM `0x0000_0000`, DTCM `0x2000_0000`; R52 ATCM/BTCM/CTCM `0x0100/0110/0120_0000` (CPU0), `0x0140/0150/0160_0000` (CPU1) |
| M7 sizes (S32K566) | ITCM 32 KB, DTCM 64 KB (Rev.A's "60 KB + 4 KB stack" was S32K3) |
| R52 sizes | ATCM/BTCM/CTCM 32 KB each, zero wait state |
| M7 DTCM interfaces | Dual interface D0TCM / D1TCM |
| Enable | `ITCMCR.EN` / `DTCMCR.EN` software-controllable |

###### ECC initialization constraint (very easy to trip over)

**Before reading TCM or system RAM, a 64-bit write initialization is mandatory**, otherwise ECC errors occur. NXP S32K documentation: *"To prevent ECC errors, TCM and system RAM both require 64-bit write initialization before read operations."*

This means the MPU configuration **must not** read TCM contents before the TCM is initialized — startup code must fill ECC first and build regions afterwards. Also, RAM ECC initialization must be done **only on Power-On Reset**; repeating it on other reset types destroys retained data.

###### TCM backdoor: the structural hole in core-MPU protection

This is the most important S32K5-specific finding in this revision, and it is **not** covered by Rev.A.

> Arm Cortex-M7 TRM: *"**AHBS interface transactions are not capable of performing MPU lookups.** No distinction is made internally between unprivileged and privileged AHBS interface accesses as indicated on HPROTS. **The system is entirely responsible for providing TCM protection functionality for AHBS interface accesses** as required."*

Consequence: **any master reaching a TCM through `AXBS_TCM` bypasses that core's MPU entirely.** RM Rev.3 Chapter_02 Table 11/12 tabulates exactly which initiators have backdoor access to which TCM — the list includes *other M7 cores, both R52 cores, the M4, DSP-V, Neutron, LPE_eDMA3 and eDMA5*. On S32K5, "TCM" is not private memory; it is memory whose **only** protection against other masters is XRDC.

| Path | Protected by |
| --- | --- |
| Owning core → its own TCM | Core MPU (M7: 16 regions; R52: EL1/EL2) |
| Any other master → TCM via `AXBS_TCM` | **XRDC only** — `MRC_B3` for M7_0-3 TCM backdoor, `CPE_MRC4` for R52 Cluster 0 TCM, `LPE_MRC0` for M4 TCM backdoor |

> **Design rule**: every TCM must be configured in **both** the owning core's MPU *and* the corresponding XRDC MRC. Configuring only the MPU leaves the backdoor wide open — and the backdoor addresses (`0x1100_0000`–`0x116F_FFFF` for ITCM, `0x2300_0000`–`0x236F_FFFF` for DTCM) are separate windows from the TCM's own base, so they need their own XRDC regions.

###### Multi-core TCM sharing (S32K5 specific)

Arm/NXP specify that on multi-core devices, all enabled cores and non-core masters **may use the TCMs of disabled cores as system memory**. For an enabled core to use a disabled core's TCM as ordinary RAM:

1. Enable the TCM control clock of that M7 core
2. Put that M7 core into wait mode
3. Enable that M7 core's clock

**MPU implication**: TCM ownership is dynamic — whichever core is enabled owns its TCM; once a core is disabled, its TCM becomes common RAM. Therefore TCM region MPU configuration cannot be statically hard-coded; it must follow core enable state, or simply be managed by XRDC per domain.

###### MPU attributes

The TCM interface is inherently **non-cacheable** (Tightly-Coupled Memory already runs at single-cycle latency, so caching buys nothing). Hence:

| Region | Recommended attribute | Notes |
| --- | --- | --- |
| ITCM | Normal NC, RWX | Vector table + hot ISRs, executable |
| DTCM data | Normal NC, RW, XN | Stack and core data |
| R52 ATCM | Normal WB-WA, **XN=0** | Must stay executable — see the WXN conflict below |

Configuring Normal cacheable raises no error, but the cache is ineffective over that range and the attribute is vacuous — harmless but pointless; it should still be written correctly at review.

###### ⚠️ The ATCM-vs-WXN conflict (new in Rev.B)

`SCTLR.WXN` resets to **0**, and the TRM states this explicitly: *"0 = EL1-controlled MPU regions with write permission are not forced to be XN, **this is the reset value**."*

The obvious mitigation — set `WXN = 1` globally to enforce write-xor-execute — **breaks ATCM**, because ATCM is a read/write region that must remain executable (vector table, startup code). With `WXN=1`, ATCM is force-XN and the core cannot boot from it.

Two ways out, neither free:

| Option | Cost |
| --- | --- |
| Do **not** set global `WXN`; set `XN` per region (code regions `XN=0`, all data regions `XN=1`) | Loses the global backstop. A forgotten `XN=1` on a code region, or a stray `XN=0` on a data region, is silent. Must be covered by a boot-time self-test that reads back every `PRBAR.XN`. |
| Set `WXN=1` and move the vector table / startup code out of ATCM into MRAM | ATCM becomes data-only. Costs the zero-wait-state benefit for the hottest code. |

Also note `SCTLR.UWXN` (bit 20, "unprivileged write permission implies EL1 XN") **also resets to 0** — setting only `WXN` leaves unprivileged-writable regions executable.

#### 5.6 XSPI / QSPI external storage

| Item | Content |
| --- | --- |
| XSPI base | `0x8100_0000` |
| Board device | IS66WVH8M8DAL HyperRAM 512 Mbit (S32K5XXCVB) |
| Use | Extended RAM / external flash / A/B image copies |

**MPU attributes**:

| Use | Attribute | Notes |
| --- | --- | --- |
| External flash execution | Normal NC or Device, RO, XN=0 | Cacheable is not recommended: XSPI goes over an external bus and cache coherency depends on the external device |
| HyperRAM data | Normal NC, RW, XN=1 | High bandwidth, latency-sensitive |
| XSPI register window | Device-nGnRnE, RO, XN=1 | Controller registers |

**Trap**: the XSPI **register window** and **data window** must be two separate MPU regions. Configuring the register window as Normal cacheable is the classic XSPI mistake — the same reasoning as on-chip peripherals. Also, MRAM programming over XSPI has special handling requirements (SEGGER explicitly notes *"QSPI flash programming requires special handling compared to internal flash"*).

#### 5.7 Peripheral window

| Item | Content |
| --- | --- |
| Start | `0x4000_0000` |
| Bridges | PBRIDGE3_0–5 (`0x4000_0000`–`0x40BF_FFFF`), CPE_PBRIDGE3_0/1 (`0x4100_0000`–`0x411F_FFFF`), LPE_PBRIDGE3 (`0x4200_0000`–`0x421F_FFFF`), DSP_PBRIDGE3 (`0x4260_0000`–`0x427F_FFFF`), CPE_GIC0 (`0x4300_0000`–`0x431F_FFFF`) |
| Last mapped peripheral | `0x4219_7FFF` |
| Alias window | PBRIDGE3_0 alias at `0x5000_0000`–`0x501F_FFFF` (= base **+ `0x1000_0000`**) |
| Attribute | **Device-nGnRE** (R52) / **Device-nGnRnE** (M7) |
| XN | 1 (non-executable) |

**Bridge slot geometry** (matters for region granularity): each PBRIDGE3 occupies 2 MB divided into 128 slots of 4 / 16 / 64 KB. The Rev.3 memory map shows 479 mapped peripherals across 486 rows, with slot sizes of 16 KB (384), 32 KB (91) and 64 KB (11). **Merging gaps ≤ 64 KB collapses the 34 MB peripheral space into 11 contiguous segments** — which is what makes the 3-region PERI layout in §4.2/§4.3 possible.

**Two ranges that need their own region**:

1. **PPB / system control space** `0xE000_0000`–`0xE00F_FFFF` (1 MB) — where the M7's `MPU_TYPE`/`MPU_CTRL` live at `0xE000_ED9x`. The PPB is **core-private**; M7 and R52 see entirely different contents. Do not merge the PPB with the peripheral window into one big Device region, or debugger access and system-register visibility become hard to reason about.
2. **Vendor-defined space** above `0xE010_0000`, partitioned per the RM.

**Secure / non-secure aliasing (new in Rev.B)**: the memory map gives an explicit alias window only for PBRIDGE3_0, at exactly **base + `0x1000_0000`** (`0x4000_0000` → `0x5000_0000`). The other 435 mapped peripherals have **no** alias. Combined with RM §36.2/§36.3 — "the memory slots in the table represent the **non-secure address region**" — the practical reading is: the tabulated addresses are the non-secure view, and the secure view's base rule is **not fully determined by this attachment**. Treat the `+0x1000_0000` rule as confirmed for PBRIDGE3_0 only, and verify before assuming it generalises.

#### 5.8 XRDC: the complementary layer that must be designed alongside the MPU

This is where S32K5 differs most from S32K3, and it is **an entire layer that an MPU-only design misses**.

###### NXP's two-level isolation model

NXP states it explicitly: *"Through XRDC and MPU, a two-level isolation hierarchy can be achieved"*:

| Level | Mechanism | Isolates |
| --- | --- | --- |
| Core level | **XRDC** | Core vs. core, core vs. peripheral |
| Task level | **MPU** | Task vs. task within one core |

In other words: **the MPU governs "who is who inside one core", XRDC governs "which master may touch which slave"**. The two do not overlap; neither is optional.

###### XRDC submodules

| Submodule | Responsibility |
| --- | --- |
| `XRDC_MGR` | Manager; coordinates all programming-model reads and writes |
| `XRDC_MDAC` | Master Domain Assignment Controller; assigns domain IDs to masters |
| `XRDC_MRC` | Memory Region Controller; memory access control via region descriptors |
| `XRDC_PAC` | Peripheral Access Controller; peripheral access control per domain |

###### S32K566 XRDC instances and MRC targets (new in Rev.B)

Five XRDC instances: `XRDC_A`, `XRDC_B`, `XRDC_C`, `CPE_XRDC`, `LPE_XRDC`. **16 Domain IDs**; each instance exposes **768 PDAC slots (0–767)**. `[来源: rm1131130 Rev.3, Chapter_31 §31.1.1–31.1.5]`

| MRC | # descriptors | Protected target |
| --- | --- | --- |
| `MRC_B0` | 16 | AXI MRAM Controller P1 (Code MRAM) |
| `MRC_B1` / `B2` / `B6` | 16 each | AXI RAM Controller 0/1/2 (SysSRAM) |
| **`MRC_B3`** | 16 | **Cortex-M7_0-3 TCM backdoor** |
| `MRC_B5` | 16 | AXI MRAM Controller P2 (Data MRAM) |
| **`CPE_MRC4`** | 16 | **R52 Cluster 0 TCM** |
| `CPE_MRC0`–`MRC3` | 16 each | `CPE_SRAMCTL_0/1/2/3` |
| `CPE_MRC5` / `M6` | 16 each | `CPE_LLC_0` / `CPE_LLC_1` |
| **`LPE_MRC0`** | 16 | **LPE Cortex-M4 TCM Backdoor** |
| `MRC_A0` | 16 | NETC Base AXI32 |
| `MRC_A2` | 8 | NETC IEPRC ECAM |
| `MRC_B4` | 8 | XSPI Controller |
| `MRC_B7` | 4 | Neutron64S AXI64 |
| `MRC_B8` | 16 | AMRAMC IPS0 |
| `MRC_C0` | 4 | DSP-V AHB32 |
| `MRC_A1` / `A3` | 4 each | CANXL_0 / CANXL_1 |

**PAC ↔ bridge mapping**: `PAC_A0-1`→PBRIDGE3_0 (slots 0–127), `PAC_C0-2`→PBRIDGE3_1 (128–255), `PAC_B0-2`→PBRIDGE3_2 (256–383), `PAC_C3-4`→PBRIDGE3_3 (384–511), `PAC_C5-6`→PBRIDGE3_4 (512–639), `PAC_B3-5`→PBRIDGE3_5 (640–767), `CPE_PAC0-1`→CPE_PBRIDGE3_0, `CPE_PAC2-3`→CPE_PBRIDGE3_1, `LPE_PAC0-2`→LPE_PBRIDGE3. The full slot↔peripheral table is in the "Peripherals Memory Map" tab of the memory map attachment.

###### ⚠️ XRDC has no execute-never attribute (new in Rev.B)

The `DdACP` permission field encodes only **read / write** across four levels (secure-privileged, secure-user, nonsecure-privileged, nonsecure-user). There is **no XN bit**.

> **Consequence: all code-executability control lives in the core MPU.** XRDC can make a region read-only for a domain, but it cannot make it non-executable. Any "this memory must never run as code" requirement must be enforced by `PRBAR.XN` / `MPU_RASR.XN` on every core that can fetch from it — and, per §5.5, that includes cores reaching it via backdoor.

###### Enable ordering: XRDC locks itself out if enabled half-configured

> "When XRDC is enabled (`CR[GVLD]` = 1), you **cannot access any XRDC-protected memory unless** you configure at least one set of memory region descriptors that includes the targeted memory." `[来源: Chapter_31 §31.5.6.5]`

**Configure all MRGD/PAC descriptors and self-check them before setting `GVLD=1`.** Enabling first and configuring second can lock you out of the XRDC's own registers.

###### Key differences from the MPU

| Dimension | MPU | XRDC |
| --- | --- | --- |
| Constrains | **The local core's** fetches and data accesses | **All masters** (cores + eDMA + MAC + ...) |
| Stops DMA | **No** | **Yes** |
| Configuration granularity | One set per core | One set for the whole chip |
| Violation exception | M7: MemManage; R52: permission/translation fault | **Bus Fault** |
| Context-switched | Yes (OS switches per task) | No (statically bound to domain ID) |

**The single most important conclusion: the MPU cannot stop DMA.** eDMA, the Ethernet MAC, CAN and other masters bypass the CPU's MPU and access the bus directly. If the safety design only covers the MPU, a misconfigured DMA descriptor can write through arbitrary memory — including the R52's stack and the M7's fault-record area. Such violations must be intercepted by XRDC's MRC/PAC.

###### Inter-domain sharing and SEMA42

XRDC supports marking a memory block or peripheral as shared across domains, with **SEMA42 hardware semaphores** for mutual exclusion. The typical flow from NXP AN14715:

1. Domain0 locks the SEMA42 channel, initializes the shared peripheral, and **does not release** the semaphore
2. Domain1 attempts to write that peripheral → **triggers a Bus Fault**
3. The fault handler records the faulting address and calls `Xrdc_Ip_GetDomainIDErrorStatus()` to read the XRDC error status

**Exception-handling implication**: an XRDC violation raises a **Bus Fault**, a different exception entry from the MPU's MemManage/Abort. The fault-handling code must implement two separate handlers, and XRDC error status must be read with the dedicated API — it is not found in `SCB->CFSR`.

###### MCUXpresso SDK support

The MCUXpresso SDK provides `XRDC_Init`, domain assignment (`xrdc_processor_domain_assignment_t`), memory access policy (`xrdc_mem_access_config_t`) and peripheral access policy (`xrdc_periph_access_config_t`). On the AUTOSAR path this corresponds to the `Xrdc_Ip` driver.

#### 5.9 MPU configuration quick reference by memory type

| Memory type | M7 attribute | R52 attribute | XN | Special notes |
| --- | --- | --- | --- | --- |
| Code MRAM `0x0800_0000`–`0x09FF_FFFF` | Normal WB RA | Normal WB RA (MAIR0=0xFF) | 0 | Attributes must match across cores; code immutability needs XRDC (XRDC has no XN) |
| Data MRAM `0x0C80_0000`–`0x0C83_FFFF` | Normal WB RA | Normal WB RA | 1 | |
| M7 SRAM0-2 `0x2100_0000`–`0x212F_FFFF` | Normal WB RA | — | 1 | Stack / heap / .data; NC and shareable sub-partitions live in these banks |
| R52 SRAM `0x2200_0000`–`0x220F_FFFF` | — | Normal WB RA | 1 | Guarding other masters needs XRDC (`CPE_MRC0`–`MRC3`) |
| CPE_LLC0/1 scratchpad | — | Normal WB-WA | 1 | `0x0700_0000` (960 KB) / `0x0F00_0000` (448 KB) |
| LPE_SRAM `0x1000_0000` / `0x2400_0000` | Normal NC / WB | Normal NC / WB | 1 | 256 KB code + 128 KB data; retained in Standby |
| ITCM `0x0000_0000` (32 KB) | Normal NC | — | 0 | **Shares 1 MB window with LPE_SRAM alias**; 64-bit write init for ECC before reads |
| DTCM `0x2000_0000` (64 KB) | Normal NC | — | 1 | Backdoor at `0x2300_0000`–`0x236F_FFFF` needs XRDC `MRC_B3` |
| R52 ATCM/BTCM/CTCM | — | Normal WB-WA | ATCM=0, others=1 | Backdoor needs XRDC `CPE_MRC4`; ATCM must stay executable (WXN conflict, §5.5) |
| XSPI data `0x8100_0000`–`0xC0FF_FFFF` | Device or Normal NC | Device or Normal NC | 0 | |
| XSPI registers `0x40BA_4000` | **Device-nGnRnE** | Device-nGnRE | 1 | **Separate region from the data window** |
| Peripherals `0x4000_0000`–`0x421F_FFFF` | Device-nGnRnE | Device-nGnRE | 1 | Actual last peripheral `0x4219_7FFF`; DSP bridge and GIC extend to `0x431F_FFFF` |
| PPB `0xE000_0000`–`0xE00F_FFFF` | Device-nGnRnE | Device-nGnRnE | 1 | Core-private, separate region |

---

---

### 6. Cache coherency: coupling between MPU attributes and Cache

This is the most underrated part of MPU design.

#### 5.1 Cache architecture of R52 vs M7

| Item | Cortex-M7 | Cortex-R52 |
| --- | --- | --- |
| L1 I-Cache | 4–64 KB, independently configurable | 0–32 KB |
| L1 D-Cache | 4–64 KB, independently configurable | 0–32 KB |
| TCM | 0–1 MB each for instruction and data | Up to 3 TCMs, each up to 1 MB |
| Bus | AXI4 128-bit | AXI4 128-bit (separate AXIM / Flash / LLPP ports) |
| ECC | Cache, TCM and bus fully covered | Same |

The S32K5's M7 and R52 are **mutually independent**, with no shared L2 cache. This means cross-core shared data cannot rely on a cache-coherency protocol to synchronize automatically.

#### 5.2 Attribute configuration rules

| Storage | Correct attribute | Consequence of wrong attribute |
| --- | --- | --- |
| Peripheral registers | Device-nGnRnE | Configured Normal cacheable → stale reads, swallowed writes |
| MRAM / SRAM | Normal, WT or WB + RA | Configured Device → performance collapses but still correct |
| LPE_SRAM `0x1000_0000` / `0x2400_0000` | Normal NC / WB | Cacheable on data retained through Standby → data lost on wake | Retained 384 KB; configured by the M4 |
| ITCM / DTCM | Normal WT WB | The TC interface is inherently non-cacheable; wrong config is harmless but pointless |
| Cross-core shared SRAM | Normal WB + Shareable | Attribute mismatch → permanently inconsistent data |

#### 5.3 Cache maintenance sequence

After changing MPU attributes you must invalidate the corresponding cache lines, otherwise data cached under the old attributes will be wrongly reused:

```c
/* After changing MPU attributes: DSB -> invalidate cache -> ISB */
MPU_UpdateRegionAttr(n);
__DSB();
SCB_CleanInvalidateDCache_by_Addr(addr, size);
__DSB();
__ISB();
```

**Disabling D-Cache as an alternative to MPU attributes**: NXP's retained-RAM examples offer two paths — "disable D-Cache" or "configure the MPU region as non-cacheable". Pick one, but **never neither**. On S32K5 this applies to the 384 KB `LPE_SRAM` retained through Standby (`0x1000_0000` code / `0x2400_0000` data), not to a 256 B standby window.

---

### 7. Startup sequence and configuration order

#### 6.1 M7 startup sequence

```
Reset
 └─> Disable MPU (MPU_CTRL = 0)
     └─> Configure all regions (RNR/RBAR/RASR)
         └─> DSB
             └─> Enable MPU (ENABLE=1, PRIVDEFENA=1)
                 └─> ISB
                     └─> Enable Cache as needed
                         └─> Start the scheduler
```

**Do not enable the MPU's cacheable attribute before enabling the cache** — configuring cacheable while no cache exists is safe, but the reverse (cache first, then changing attributes) requires invalidation first.

#### 6.2 R52 startup sequence

```
R52 reset (launched by M7 via BOOT configuration registers)
 └─> EL1: SCTLR.M = 0
     └─> Configure MAIR0/MAIR1
         └─> Write PRBAR/PRLAR per region  ← ATCM region MUST be among them (§5.5)
             └─> DSB + ISB
                 └─> Set the PRENR bits
                     └─> SCTLR.M = 1, SCTLR.BR = 1
                         └─> DSB + ISB
                             └─> Confirm HCR.DC = 0 (else background region is always executable)
                                 └─> Enable Cache / TCM
                                     └─> Start EL1 software
```

**Two constraints specific to this sequence**:

1. **ATCM first.** R52 TRM §6.1.1: *"Do not enable the MPU unless at least one MPU region is programmed and active. If the MPU is enabled, before using the TCM you must program MPU regions to cover the TCM regions."* Enable `SCTLR.M` without a TCM-covering region and TCM access faults immediately.
2. **`WXN` is a decision, not a default.** `WXN`/`UWXN` reset to 0. Because ATCM must stay executable, the global-`WXN=1` route is closed — set `XN` per region instead, and add a boot self-test that reads back every `PRBAR.XN`.

The R52 has no independent reset (SEGGER's documentation states that a debugger cannot reset an R52 core on its own), so **R52 MPU configuration must be triggered entirely from the M7-side startup code**, with an MU interrupt or shared-memory flag handshake between the two.

#### 6.3 Timing risks of dual-core configuration

| Risk | Description | Mitigation |
| --- | --- | --- |
| R52 runs first, M7 not yet started | R52 reads uninitialized shared data | Release R52 via MU only after M7 finishes MRAM/SRAM initialization |
| Inconsistent MPU attributes | One core sees stale values in a shared region | Centralize shared-region addresses and attributes in a shared header |
| Cache not cleaned before PD2 off | Dirty data not written back | Clean + invalidate before entering LPRUN/Standby |
| Self-reconfiguration | Reconfiguration code resides in the target region | Execute critical reconfiguration from RAM |

---

### 8. Fault handling and ASIL D implications

#### 7.1 Fault response matrix

| Scenario | Detection | Response |
| --- | --- | --- |
| Illegal pointer dereference | MPU permission fault | MemManage / Abort → record scene → safe stop |
| Stack overflow | TCM/MPU stack boundary configuration | Data abort → safe stop |
| R52 region overlap misconfiguration | Translation fault | Abort → configuration error, fail fast |
| Peripheral misconfigured cacheable | Functional anomaly, no fault | Only code review + static analysis |
| Cross-core data inconsistency | No fault | Requires a software consistency protocol; the MPU cannot help |

> Key insight: **the MPU can only stop "unauthorized access", not "misconfiguration"**. A peripheral window wrongly configured as cacheable generates no fault at all — it merely behaves oddly. Therefore MPU configuration tables belong in static checks and unit tests.

#### 7.2 Dual-core safety strategy

S32K5 is an ASIL D platform, and the MPU configuration itself is a **safety-related configuration item**, requiring:

1. **Configuration integrity check**: on boot, self-test iterates all regions and verifies BASE/LIMIT/attributes against a compile-time constant table; refuse to boot on mismatch.
2. **Dual-core cross-verification**: the M7 side holds the expected R52 configuration table and uses the MU to have the R52 read back its actual registers for comparison.
3. **Single-fault protection**: the MPU registers themselves are unprotected, and configuration errors raise no fault. Keep expected values in ECC-covered read-only constants and compare periodically at runtime.
4. **ASIL D decomposition**: as a hardware mechanism the MPU provides **QM-level** capability; reaching ASIL D requires diagnostic coverage (structural coverage + runtime comparison).

#### 7.3 Diagnostic coverage recommendations

| Diagnostic | Method | Coverage target |
| --- | --- | --- |
| MPU availability | Read `MPU_TYPE`, confirm DREGION != 0 | Boot self-test |
| Region configuration correctness | Iterate and compare against the expected table | Boot + runtime periodic |
| R52 register readability | Have R52 read back PRBAR/PRLAR via MU | Boot |
| Cache attributes consistent with MPU | Static configuration consistency check | Compile time + review |

---

### 9. Implementation checklist

#### 8.1 Porting-layer interface abstraction

Because the M7 and R52 register models are completely different, the driver layer should expose a unified interface:

```c
typedef struct {
    uint32_t base;        /* Region base address */
    uint32_t limit;       /* Region limit (inclusive); derived from size on M7 */
    uint8_t  attr;        /* Platform-independent attribute enum */
    uint8_t  ap;          /* Platform-independent permission enum */
    uint8_t  xn;
} MpuRegionCfg;

/* Platform-specific implementation */
typedef struct {
    int (*GetRegionCount)(void);
    int (*SetRegion)(uint32_t idx, const MpuRegionCfg *cfg);
    int (*Enable)(void);
    int (*Disable)(void);
    int (*Verify)(const MpuRegionCfg *cfg, uint32_t idx);
} MpuHalOps;

extern const MpuHalOps MpuHal_M7;   /* PMSAv7 implementation */
extern const MpuHalOps MpuHal_R52;  /* PMSAv8-32 implementation */
```

**Unified attribute enum mapping**:

| Platform-independent enum | M7 (TEX/C/B/S) | R52 (MAIR idx, val) |
| --- | --- | --- |
| `MPU_ATTR_DEVICE` | `010/0/0` | idx 1, `0x04` |
| `MPU_ATTR_NORMAL_WB` | `001/1/1` | idx 0, `0xFF` |
| `MPU_ATTR_NORMAL_WT` | `000/1/0` | idx 2, `0xBB` |
| `MPU_ATTR_NORMAL_NC` | `001/0/0` | idx 3, `0x04` |
| `MPU_ATTR_STRONGLY_ORDERED` | `000/0/0` | idx 4, `0x00` |

**Unified permission enum mapping**:

| Platform-independent enum | M7 AP | R52 AP |
| --- | --- | --- |
| `MPU_AP_NO_ACCESS` | `000` | — |
| `MPU_AP_PRIV_RW` | `001` | `01` (this EL) |
| `MPU_AP_PRIV_RO_UNPRIV_RO` | `110` | `10` |
| `MPU_AP_FULL_RW` | `011` | `00` |
| `MPU_AP_PRIV_RO` | `101` | `10` |

#### 8.2 Integration steps

1. Set the `MEMFAULTENA` bit in `SCB->SHCSR` (enable MemManage) and give it priority above other maskable exceptions.
2. Implement the MemManage handler (Abort exception at EL0/EL1), reading and saving CFSR/MMFAR/BFAR plus the stacked PC/LR.
3. Allocate a no-cacheable fault-log region so diagnostic data is unaffected by the cache.
4. Confirm the region count via `MPU_TYPE.DREGION` before accessing region registers.
5. Write configuration code per the layouts in 4.2 / 4.3, keeping **addresses and SIZE strictly consistent with the linker script**.
6. After enabling, run a self-check comparison and refuse to boot on failure.
7. Enable MemManage / Abort breakpoints in the debug configuration.

#### 8.3 Common errors checklist

| # | Error | Consequence | Fix |
| --- | --- | --- | --- |
| 1 | Peripheral configured Normal cacheable | Stale reads, lost writes | Use Device type |
| 2 | M7 region base not aligned to SIZE | Protected range silently enlarges | Align with the linker |
| 3 | R52 region overlap | Translation fault | Redivide into non-overlapping ranges |
| 4 | Takes effect without DSB/ISB | New attributes applied late | Add barriers around attribute changes |
| 5 | Reconfiguration code resides in the target region | Instruction fetch fails, CPU wedges | Move critical reconfiguration into RAM |
| 6 | Cache not invalidated after attribute change | Stale data reused | DSB → clean/invalidate → ISB |
| 7 | LPE_SRAM (retained through Standby) configured cacheable | Data lost after low power | Configure NC or disable D-Cache |
| 8 | Using AP=`100` (M7 reserved value) | Unpredictable behaviour | Use only legal encodings |
| 9 | Accessing an out-of-range region number | Undefined behaviour | Check DREGION first |
| 10 | Forgetting to enable `MEMFAULTENA` | Fault escalates to HardFault | Enable during init |
| 11 | Configuring TCM in the core MPU but not in XRDC `MRC_B3`/`CPE_MRC4`/`LPE_MRC0` | Backdoor writes from other masters succeed unimpeded | Configure both layers (§5.5) |
| 12 | Assuming XRDC makes a region non-executable | Code still runs | XRDC has no XN; set `XN` in the core MPU (§5.8) |
| 13 | Enabling XRDC `GVLD` before all descriptors are programmed | Protected memory becomes inaccessible | Program, self-check, then enable (§5.8) |
| 14 | Leaving OMU enabled in production | Reads silently served from a remapped address | `OER[OE]=0`; rely on the FCCU monitor (§12) |
| 15 | Iterating R52 regions 0–15 to self-check all 20 | Regions 16–19 silently skipped | Use `PRSELR` indirect access (§3.4) |

---

### 10. References

| # | Document | Link |
| --- | --- | --- |
| 0 | **NXP S32K5xx Reference Manual Rev.3 (rm1131130)** + embedded `S32K5xx_memory_map.xlsx` — **address authority for this revision** | local copy |
| 1 | Cortex-M7 TRM (ARMv7-M PMSAv7 registers) | `developer.arm.com/documentation/ddi0403` |
| 2 | Armv7-M ARM — MPU_RASR (TEX/C/B/S and AP encoding tables) | `developer.arm.com/documentation/ddi0403/d/.../MPU-Region-Attribute-and-Size-Register--MPU-RASR` |
| 3 | Cortex-R52 TRM r1p2 — About the MPU | `developer.arm.com/documentation/100026/0102/Memory-Protection-Unit` |
| 4 | Cortex-R52/R52+ Programmer's Guide — The Memory Protection Unit | `developer.arm.com/documentation/109997/0101` |
| 5 | Cortex-R52 product page (MPU region count and specs) | `developer.arm.com/ip-products/processors/cortex-r/cortex-r52` |
| 6 | Arm Cortex-R processor comparison table | `arm.com/-/media/Arm Developer Community/PDF/...` |
| 7 | Armv7-M and Armv8-R software migration guide (MPU init examples) | `documentation-service.arm.com/static/65e0a4c2837c4d065f654f42` |
| 8 | NXP S32K Knowledge Base (linker partitioning and Standby RAM constraints) | `community.nxp.com/t5/S32K-Knowledge-Base` |
| 9 | SEGGER NXP S32K5xx knowledge base (MRAM base and multi-core debug) | `kb.segger.com/NXP_S32K5xx` |
| 10 | Zephyr S32K5XXCVB board documentation (memory resources) | `docs.nordicsemi.com/bundle/ncs-latest/.../s32k5xxcvb` |
| 11 | Zephyr S32K566 SoC port commit (R52 `mpu_regions.c`; real peripheral window bound) | `jausoft.net/cgit/zephyr.git/commit?id=72fb81eb` |
| 12 | NXP AN14715 — XRDC memory/peripheral resource configuration and SEMA42 inter-domain sharing | `docs.nxp.com/bundle/AN14715` |
| 13 | MCUXpresso SDK XRDC API (MGR/MDAC/MRC/PAC) | `mcuxpresso.nxp.com/api_doc/dev/721/group__xrdc.html` |
| 14 | Cortex-M7 TRM — TCM configuration (fixed base addresses and sizing rules) | `developer.arm.com/docs/ddi0489/latest/memory-system/tcm-interfaces/tcm-configuration` |
| 15 | All About Circuits — S32K5 MRAM architecture analysis (XRDC two-level isolation, MRAM traits) | `allaboutcircuits.com/news/nxp-rolls-out-automotive-mcu-for-zonal-sdvs-leveraging-mram` |
| 16 | NXP S32K5 product page (41 MB MRAM, XRDC, ASIL D) | `nxp.com/products/S32K5` |

> **Note on reference 11**: the Zephyr `mpu_regions.c` bound of `0xE00FFFFF` was used as the peripheral upper bound in Rev.A. It is a conservative placeholder; Rev.B uses the actual memory map value `0x4219_7FFF` (bridges to `0x431F_FFFF`). Keep reference 11 as corroboration, not as the authority.

---

### 11. Open items

**Closed in Rev.B (2026-10-14)** — resolved against `rm1131130` Rev.3 and its embedded `S32K5xx_memory_map.xlsx`:

- [x] ~~R52 system-register integration addresses (`0x42000000` placeholder)~~ → PPB is `0xE000_0000`–`0xE00F_FFFF`; CPE_GIC0 is `0x4300_0000`–`0x431F_FFFF`
- [x] ~~Which of 16 / 20 / 24 regions the R52 EL1 MPU implements~~ → **EL1: 20, EL2: 20** (RM Ch.02 Table 6/10)
- [x] ~~Actual DREGION value for the M7 MPU~~ → **16 regions** (same table)
- [x] ~~Whether EL2 and virtualization are supported~~ → **Yes**; EL2 MPU present with hypervisor support
- [x] ~~Exact boundaries of each SRAM partition~~ → SRAM0/1/2 at `0x2100_0000`/`0x2110_0000`/`0x2120_0000`, 1 MB each; CPE_SRAM0-3 at `0x2200_0000`–`0x220F_FFFF`
- [x] ~~Base address and size of R52 SRAM (`cpe_sram`)~~ → `0x2200_0000`, 1 MB (4×256 KB)
- [x] ~~Actual ITCM / DTCM sizes and addresses~~ → ITCM 32 KB @ `0x0000_0000`; DTCM 64 KB @ `0x2000_0000`; R52 A/B/C TCM 32 KB each @ `0x0100/0110/0120_0000` (CPU0), `0x0140/0150/0160_0000` (CPU1)
- [x] ~~True upper bound of the peripheral window~~ → last mapped peripheral `0x4219_7FFF`; bridges extend to `0x431F_FFFF`
- [x] ~~Division of PPB vs vendor-defined space~~ → PPB is `0xE000_0000`–`0xE00F_FFFF` (1 MB)
- [x] ~~XSPI register-window and data-window base~~ → data `0x8100_0000`; registers `0x40BA_4000`–`0x40BA_BFFF`
- [x] ~~XRDC domain count and MRC/PAC region-count limits~~ → 16 Domain IDs; 768 PDAC slots per instance; 16 MRGD per MRC
- [x] ~~M7 core count~~ → **4** physical M7 cores (RM Table 9), not 6

**Still open:**

- [ ] M7 `MPU_RASR` `SIZE` field encoding formula and `AP[2:0]` semantics — deferred to *Arm v7-M Architecture Reference Manual*, which is not in the reference set. §2.3/§2.4 use the standard Armv7-M encodings and should be re-verified against DDI 0314 before production.
- [ ] MRAM data retention (NXP–TSMC claims 20 years at 150 °C; another source says 10 years at 85 °C — a huge gap)
- [ ] Exact MRAM write-speed figure (8.8 MB/s vs 15 MB/s)
- [ ] MRAM fetch/pipeline behaviour during writes (whether the cache must be disabled during FOTA)
- [ ] Secure-view base address rule (only PBRIDGE3_0's `+0x1000_0000` alias is confirmed)
- [ ] XRDC region minimum alignment granularity
- [ ] XRDC violation Bus Fault priority and handler attachment
- [ ] Availability of `MemoryProtection_Ip` and `Xrdc_Ip` in MCAL (AUTOSAR path)
- [ ] Whether the 384 KB LPE_SRAM retained through Standby imposes a non-cacheable constraint on the M7 side (the S32K3 Standby RAM rule does not carry over)

---

### 12. OMU: an address-remapping trap for ASIL partitions (new in Rev.B)

The Overlay Management Unit remaps **read** addresses only, and the FCCU is required to keep it disabled during normal operation.

| Item | Value |
| --- | --- |
| Instances | `OMU_0 0x40BC_0000`, `OMU_1 0x40BC_8000`, `OMU_2 0x40BD_0000`, `CPE_OMU_0 0x4109_0000` |
| Regions | 16 (ORD0–ORD15), 8 zones |
| Granularity | 1 KB – 8192 MB, power of two |
| Direction | **Read only** — writes are not remapped |
| Scope | **First 16 MB of Code MRAM** (`0x0800_0000`–`0x08FF_FFFF`) |
| Latency | +3 cycles on the AXI read address channel when hit |
| Priority | Lowest-order region hit wins; a global region must be the lowest-priority active region |

> RM Ch.35 §35.3: *"During normal operation, the **FCCU monitors the OMU enable signal to ensure that the OMU is always disabled**."*

**Why this matters for MPU design**: the OMU's scope overlaps exactly the Code MRAM region configured in §4.2/§4.3. If OMU is left enabled in development mode, the CPU reads remapped content while writing to the original address — code appears to run, but it is not the code at that address. **Set `OER[OE] = 0` (bypass) in production** and rely on the FCCU monitor as the safety mechanism.

---

### 13. Consolidated risk register (new in Rev.B)

| # | Risk | Severity | Source |
| --- | --- | --- | --- |
| 1 | R52 overlapping regions cause a **translation fault**, not priority resolution | 🔴 High | R52 TRM §8.1 |
| 2 | `SCTLR.WXN` / `UWXN` reset to **0** — writable regions are executable by default | 🔴 High | R52 TRM Table 3-133 |
| 3 | Global `WXN=1` breaks ATCM executability (vector table) | 🔴 High | Derived, §5.5 |
| 4 | Enabling R52 MPU without a TCM-covering region locks out TCM entirely | 🔴 High | R52 TRM §6.1.1 |
| 5 | M7/R52 TCM **backdoor bypasses the core MPU**; only XRDC MRCs cover it | 🔴 High | M7 TRM (AHBS) + RM Ch.02 Table 11/12 |
| 6 | XRDC `GVLD=1` before descriptors are configured locks out protected memory | 🔴 High | RM Ch.31 §31.5.6.5 |
| 7 | ITCM and LPE_SRAM alias share `0x0000_0000` — indistinguishable by address | 🟠 Med-high | memory_map.xlsx |
| 8 | EL2 MPU regions must cover every EL1-visible address, or two-stage lookup faults | 🟠 Med-high | R52 TRM §8.2.2 |
| 9 | `HMAIR0`/`HMAIR1` reset to 0 — EL2-side attributes invalid until programmed | 🟠 Med-high | R52 TRM §3.3.45 |
| 10 | `HCR.DC=1` makes background-region instruction fetches always executable | 🟠 Med-high | R52 TRM §8.2.3 |
| 11 | REG_PROT transfer errors need strongly-ordered MPU regions to be catchable | 🟠 Medium | RM Ch.11 §11.3.5 |
| 12 | R52 regions 16–19 reachable only via `PRSELR` — iteration self-tests silently skip them | 🟠 Medium | R52 TRM §3.3.85-87 |
| 13 | XRDC has **no XN** — executability is entirely the core MPU's job | 🟡 Medium | RM Ch.31 Table 147 |
| 14 | OMU remaps reads only, over Code MRAM's first 16 MB | 🟡 Medium | RM Ch.35 §35.3 |
| 15 | `GCR[HLB]` clears only on system reset — forecloses post-OTA reconfiguration | 🟡 Low | RM Ch.11 §11.6.3 |
| 16 | MSCM `CPXCFG3[CMP]` resets to unknown — must be read back, not assumed | 🟡 Low | RM Ch.09 §9.5.3.8 |

> Once the addresses and region counts above are confirmed, the layouts in 4.2 / 4.3, the per-memory-type tables in chapter 5, and the configuration code in 2.8 / 3.8 must all be updated.
