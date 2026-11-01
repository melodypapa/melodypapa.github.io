---
title: "S32K5 MPU Quick Reference"
---

Companion to the main design document: [S32K5_R52_M7_MPU_Design_EN.md](S32K5_R52_M7_MPU_Design_EN.md) / [S32K5_R52_M7_MPU_Design_CN.md](S32K5_R52_M7_MPU_Design_CN.md)

> 2026-11-01 synced with the main document restructure: register bit fields corrected against the ARM TRMs, all addresses replaced with verified S32K566 values (the S32K3-era `0x2040_xxxx` addresses do not exist on S32K5).

---

## Registers

### Cortex-M7 (PMSAv7, SCS `0xE000ED9x`)

| Register | Address | Notes |
| --- | --- | --- |
| `MPU_TYPE` | `0xE000ED90` | RO; `DREGION[15:8]` detects region count (S32K566 = 16) |
| `MPU_CTRL` | `0xE000ED94` | `[0]` ENABLE, `[1]` HFNMIENA, `[2]` PRIVDEFENA |
| `MPU_RNR` | `0xE000ED98` | Selects region number |
| `MPU_RBAR` | `0xE000ED9C` | `[31:5]` ADDR, `[4]` VALID, `[3:0]` REGION |
| `MPU_RASR` | `0xE000EDA0` | Attributes + SIZE + ENABLE (below) |

### Cortex-R52 (Armv8-R PMSAv8-32, EL1 MPU)

| Register | cp15 encoding | Notes |
| --- | --- | --- |
| `MPUIR` | `MRC p15, 0, Rt, c0, c0, 4` | RO; `DREGION[15:8]` (S32K566 = 20) |
| `PRSELR` | `MCR/MRC p15, 0, Rt, c6, c2, 1` | Region select; `[4:0]` on 20-region implementations |
| `PRBAR` | `c6, c3, 0` | `[31:6]` BASE, `[4:3]` SH, `[2:1]` AP, `[0]` **XN** |
| `PRLAR` | `c6, c3, 1` | `[31:6]` LIMIT (inclusive), `[3:1]` AttrIndx, `[0]` EN |
| `MAIR0/1` | `c10, c2, 0/1` | 8 slots × 8-bit memory attributes |
| `SCTLR` | `c1, c0, 0` | `[0]` M, `[17]` BR, `[19]` WXN, `[20]` UWXN |
| `HCR` | `c1, c1, 0` | `DC` / `VM` — keep 0 on S32K5 |

EL2 side (`p15, 4, ...`): `HMPUIR` / `HPRSELR` / `HPRBAR` / `HPRLAR` / `HPRENR` (`c6, c1, 1`) / `HMAIR0/1`.

> **Note**: there is **no `PRENR` at EL1** — region enabling is solely via `PRLAR.EN`; the bitmask enable register only exists at EL2 (`HPRENR`). Regions 16–19 are reachable only via indirect `PRSELR` access.

---

## AP permissions

### M7 (3 bit, `RASR[26:24]`)

| AP | Privileged | Unprivileged |
| --- | --- | --- |
| `000` | None | None |
| `001` | RW | None |
| `010` | RW | RO |
| `011` | RW | RW |
| `100` | ❌ reserved | ❌ reserved |
| `101` | RO | None |
| `110` | RO | RO |
| `111` | RO | RO |

### R52 (2 bit, `PRBAR[2:1]`)

| AP | EL1 | EL0 |
| --- | --- | --- |
| `00` | RW | none |
| `01` | RW | RW |
| `10` | RO | none |
| `11` | RO | RO |

> M7's `010` (privileged RW + unprivileged RO) mixed encoding has **no R52 equivalent** — rewrite the region AP on task switch, or accept equal permissions.

---

## XN / SH locations

| | M7 | R52 |
| --- | --- | --- |
| XN | `MPU_RASR[28]` | **`PRBAR[0]`** (same register as the base — easy to miss in review) |
| Shareable | `RASR[18]` S bit | `PRBAR[4:3]` SH: `00` Non, `10` Outer, `11` Inner, `01` ❌ UNPREDICTABLE |
| WXN | no equivalent | `SCTLR[19]` WXN / `[20]` UWXN, reset 0; setting WXN=1 breaks ATCM (must stay executable) |

---

## Memory attributes

### M7: TEX/C/B/S

| Use | TEX | C | B | S |
| --- | --- | --- | --- | --- |
| Strongly-ordered | `000` | 0 | 0 | always Shareable |
| Device Shared | `000` | 0 | 1 | always Shareable |
| Device Non-shared | `010` | 0 | 0 | always Non-shareable |
| Normal WT | `000` | 1 | 0 | S |
| Normal WB no-WA | `000` | 1 | 1 | S |
| Normal WB RA | `001` | 1 | 1 | S |
| Normal NC | `001` | 0 | 0 | S |

### R52: MAIR values (S32K5 scheme)

| AttrIndx | Value | Meaning | Used for |
| --- | --- | --- | --- |
| 0 | `0xFF` | Normal, RW, WB, RA | MRAM / SRAM |
| 1 | `0x00` | Device-nGnRnE (strictest) | PPB |
| 2 | `0xBB` | Normal, RW, WT (no WA) | reserved |
| 3 | `0x04` | Device-nGnRE | peripheral bridges |
| 4 | `0x44` | Normal, Non-cacheable | LPE_SRAM Code read-only view |

Device strictness: `0x00` nGnRnE > `0x04` nGnRE > `0x0C` nGRE > `0x0F` GRE.

---

## Size encoding

| Platform | Formula | Minimum | Alignment | Overlap |
| --- | --- | --- | --- | --- |
| M7 | size = 2^(SIZE+1) | 32 B | BASE aligned to size (misaligned → **silently doubles**) | allowed, higher number wins |
| R52 | LIMIT inclusive | 64 B | BASE/LIMIT 64 B (misaligned → **immediate fault**) | **forbidden**, multiple hits = translation fault |

> PMSAv7 power-of-two examples on S32K566: 3 MB SRAM0-2 splits into 2+1 MB; the ~50 MB peripheral window splits into 32+8 MB. R52 covers the same space with a single region.

---

## SRD subregions (M7 only)

Regions ≥ 256 B split into 8 subregions; `SRD[n]=1` disables subregion n, `SRD[0]` maps to the lowest address.
For regions of 32/64/128 B, writing SRD has **unpredictable effects**.

---

## S32K566 resource quick reference (all verified addresses)

| Resource | Address | Size | M7 attr | R52 attr | XN | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Code MRAM Bank A | `0x0800_0000`–`0x08FF_FFFF` | 16 MB | Normal WB RA | Attr0 | 0 | may tighten to RO+X during FOTA |
| Code MRAM Bank B | `0x0900_0000`–`0x09FF_FFFF` | 16 MB | Normal WB RA | Attr0 | 0 | A/B bank isolation |
| Data MRAM | `0x0C80_0000`–`0x0C83_FFFF` | 256 KB | Normal WB RA | Attr0 | 1 | |
| M7 SRAM0-2 | `0x2100_0000`–`0x212F_FFFF` | 3 MB | WB, NC/shareable sub-partitions via overlap | — (R52 uses it as cross-core shared, Attr0) | 1 | **not a power of two** — M7 splits 2+1 MB |
| R52 SRAM | `0x2200_0000`–`0x220F_FFFF` | 1 MB | — | Attr0 | 1 | guarding other masters needs XRDC `CPE_MRC0-3` |
| LPE_SRAM Code | `0x1000_0000`–`0x1003_FFFF` | 256 KB | Normal NC, privileged RO | Attr4 `0x44`, RO | 1 | retained through Standby |
| LPE_SRAM Data | `0x2400_0000`–`0x2401_FFFF` | 128 KB | no region | Attr0 | 1 | M7 does not access |
| ITCM | `0x0000_0000` | 32 KB | Normal NC | — | 0 | **shares the 1 MB window with the LPE_SRAM alias**; 64-bit write ECC init before reads |
| DTCM | `0x2000_0000` | 64 KB | Normal NC | — | 1 | backdoor at `0x2300_0000`+ needs XRDC `MRC_B3` |
| R52 ATCM/BTCM/CTCM | `0x0100/0110/0120_0000` (CPU1: `0x0140/0150/0160`) | 32 KB each | — | Attr0 | **ATCM=0**, others 1 | ATCM must stay executable (WXN conflict); backdoor needs `CPE_MRC4` |
| XSPI | `0x8100_0000`+ | 1024 MB | **no region** (background no-access) | **no region** (faults with BR=0) | — | not used in this project |
| Peripherals | `0x4000_0000`–`0x431F_FFFF` | — | Device, 2 regions (32+8 MB) | Device-nGnRE, single region | 1 | last peripheral `0x4219_7FFF`; includes DSP bridge and GIC |
| PPB | `0xE000_0000`–`0xE00F_FFFF` | 1 MB | Device | Attr1 `0x00` | 1 | core-private; **must stay privileged/EL1 writable** |

**Region budget**: M7 16 regions = 13 static + 3 OS dynamic; R52 EL1 20 regions = 12 static + 8 OS dynamic.
**Background strategy**: M7 `PRIVDEFENA=0` + explicit 4 GB no-access background (SDEN 1013783-B workaround); R52 `SCTLR.BR=0`, miss = fault.

---

## MPU vs XRDC

| | MPU | XRDC |
| --- | --- | --- |
| Constrains | local core only | all masters (cores + eDMA + MAC) |
| Stops DMA | no | **yes** |
| Disables execution | **yes** (XN) | **no** (no XN attribute) |
| Granularity | per core | whole chip (16 Domain IDs, 768 PDAC slots) |
| Fault | MemManage / Abort | Bus Fault (separate entry) |
| Isolation level | task level | core level |
| Enable order | configure then enable | **finish all descriptors before `GVLD=1`**, else lockout |

---

## MRAM vs eFlash

| | MRAM (S32K5) | eFlash (S32K3) |
| --- | --- | --- |
| Addressing | byte | page/block |
| Erase before write | no | yes |
| Write speed | 8.8-15 MB/s | 1/10-1/15 of that |
| Endurance | ~1M writes | ~10k-100k erases |
| A/B swap | hardware Flexible A/B swap + RWW (2 MB partition granularity) | — |

---

## Three iron rules

1. **Programming code must not reside in a region being reconfigured** — otherwise instruction fetch fails the instant the permission changes and the CPU wedges.
2. **DSB before, ISB after** — guarantees the change takes effect.
3. **Clean/invalidate the cache after changing cache attributes** — otherwise stale data is reused.

---

## Traps

| Trap | Symptom |
| --- | --- |
| Peripheral configured Normal cacheable | Stale reads, lost writes, no fault |
| M7 BASE not aligned to SIZE | Protected range silently doubles |
| R52 region overlap | Translation fault (fail-fast, which is good) |
| R52 `SCTLR.WXN=1` | ATCM force-XN, core cannot boot — manage XN per region |
| R52 self-test iterates only regions 0-15 | Regions 16-19 silently skipped — use indirect `PRSELR` access |
| Forgetting `MEMFAULTENA` | Fault escalates to HardFault |
| Using M7 AP=`100` / R52 SH=`01` | Unpredictable (reserved / UNPREDICTABLE respectively) |
| TCM/SRAM read before 64-bit ECC init write | ECC error (POR only) |
| Relying on MPU to stop DMA | **It cannot** — use XRDC |
| Relying on XRDC to disable execution | **XRDC has no XN** — executability lives only in the core MPU |
| XRDC `GVLD` set too early | Protected memory becomes inaccessible — configure first, enable last |
| OMU left enabled in production | Reads silently remapped — set `OER[OE]=0`, rely on FCCU monitor |
