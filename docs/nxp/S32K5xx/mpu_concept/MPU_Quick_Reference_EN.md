## S32K5 MPU Quick Reference

Companion to the main design document: [S32K5_R52_M7_MPU_Design_EN.md](S32K5_R52_M7_MPU_Design_EN.md) / [S32K5_R52_M7_MPU_Design_CN.md](S32K5_R52_M7_MPU_Design_CN.md)

---

### Registers

#### Cortex-M7 (PMSAv7, SCS `0xE000ED9x`)

| Register | Address |
| --- | --- |
| `MPU_TYPE` | `0xE000ED90` |
| `MPU_CTRL` | `0xE000ED94` |
| `MPU_RNR` | `0xE000ED98` |
| `MPU_RBAR` | `0xE000ED9C` |
| `MPU_RASR` | `0xE000EDA0` |

#### Cortex-R52 (Armv8-R)

| Register | Access |
| --- | --- |
| `PRBAR` / `PRLAR` | `MCR p15, 0, Rt, c6, c3, 0/1` (via `PRSELR`) |
| `HPRBAR` / `HPRLAR` | `MCR p15, 0, Rt, c6, c3, 2/3` |
| `MAIR0/1` | `MCR p15, 0, Rt, c10, c2, 0/1` |
| `PRENR` | `MCR p15, 0, Rt, c12, c0, 2` (confirm against integration) |
| `SCTLR` | `MCR p15, 0, Rt, c1, c0, 0` |

---

### AP permissions

#### M7 (3 bit, `RASR[26:24]`)

| AP | Privileged | Unprivileged |
| --- | --- | --- |
| `000` | None | None |
| `001` | RW | None |
| `010` | RW | RO |
| `011` | RW | RW |
| `100` | reserved | reserved |
| `101` | RO | None |
| `110` | RO | RO |
| `111` | RO | RO |

#### R52 (2 bit, `PRBAR[3:2]`)

| AP | Meaning |
| --- | --- |
| `00` | RW, this EL and lower |
| `01` | RW, this EL only |
| `10` | RO, this EL and lower |
| `11` | RO, this EL only |

---

### Memory attributes

#### M7: TEX/C/B/S

| Use | TEX | C | B | S |
| --- | --- | --- | --- | --- |
| Strongly-ordered | `000` | 0 | 0 | ignored |
| Device Shared | `000` | 0 | 1 | ignored |
| Device Non-shared | `010` | 0 | 0 | ignored |
| Normal WT | `000` | 1 | 0 | S |
| Normal WB no-WA | `000` | 1 | 1 | S |
| Normal WB RA | `001` | 1 | 1 | S |
| Normal NC | `001` | 0 | 0 | S |

#### R52: MAIR values

| Index | Value | Meaning |
| --- | --- | --- |
| 0 | `0xFF` | Normal, RW, WB, RA |
| 1 | `0x04` | Device-nGnRnE |
| 2 | `0xBB` | Normal, RW, WT |
| 3 | `0x00` | Strongly-ordered |

---

### Size encoding

| Platform | Formula | Minimum | Alignment |
| --- | --- | --- | --- |
| M7 | size = 2^(SIZE+1) | 32 B | BASE aligned to size |
| R52 | LIMIT inclusive | 64 B | BASE and LIMIT both 64 B |

---

### SRD subregions (M7 only)

Regions ≥ 256 B split into 8 subregions; `SRD[n]=1` disables subregion n, `SRD[0]` maps to the lowest address.
For regions of 32/64/128 B, writing SRD has **unpredictable effects**.

---

### Memory types on S32K5

| Memory type | Address | M7 | R52 | XN | Notes |
| --- | --- | --- | --- | --- | --- |
| Code MRAM | `0x0800_0000` | Normal WB RA | Normal WB RA | 0 | 32-41 MB; attributes must match across cores |
| M7 SRAM main | `0x2040_0100` | Normal WB RA | — | 1 | 1.5 MB total |
| M7 SRAM NC | `0x2040_8000` | Normal NC | — | 1 | 32 KB |
| M7 SRAM shareable | `0x2041_0000` | Normal WB + Shareable | Normal WB + Shareable | 1 | 32 KB, both sides identical |
| Standby RAM | `0x2040_0000` | **Normal NC** | — | 1 | 256 B, hard constraint |
| R52 SRAM | see RM | — | Normal WB RA | 1 | `cpe_sram`, 1 MB; guard with XRDC |
| ITCM | `0x0000_0000` | Normal NC | — | 0 | 32 KB |
| DTCM | `0x2000_0000` | Normal NC | — | 1 | 60 KB + 4 KB stack |
| XSPI data | `0x8100_0000` | Normal NC | Normal NC | 0 | external flash / HyperRAM |
| Peripherals | `0x4000_0000`–`0xE00F_FFFF` | Device-nGnRnE | Device-nGnRnE | 1 | upper bound is `0xE00F_FFFF`, not 4 GB |
| PPB | `0xE000_0000`+ | Device-nGnRnE | Device-nGnRnE | 1 | core-private, separate region |

---

### MPU vs XRDC

| | MPU | XRDC |
| --- | --- | --- |
| Constrains | local core only | all masters (cores + eDMA + MAC) |
| Stops DMA | no | yes |
| Granularity | per core | whole chip |
| Fault | MemManage / Abort | Bus Fault |
| Isolation level | task level | core level |

---

### MRAM vs eFlash

| | MRAM (S32K5) | eFlash (S32K3) |
| --- | --- | --- |
| Addressing | byte | page/block |
| Erase before write | no | yes |
| Write speed | 8.8-15 MB/s | 1/10-1/15 of that |
| Endurance | ~1M writes | ~10k-100k erases |

---

### Three iron rules

1. **Programming code must not reside in a region being reconfigured** — otherwise instruction fetch fails the instant the permission changes and the CPU wedges.
2. **DSB before, ISB after** — guarantees the change takes effect.
3. **Clean/invalidate the cache after changing cache attributes** — otherwise stale data is reused.

---

### Traps

| Trap | Symptom |
| --- | --- |
| Peripheral configured Normal cacheable | Stale reads, lost writes, no fault |
| M7 BASE not aligned to SIZE | Protected range silently doubles |
| R52 region overlap | Translation fault (fail-fast, which is good) |
| Standby RAM configured cacheable | Data lost after low power |
| Forgetting `MEMFAULTENA` | Fault escalates to HardFault |
| Using M7 AP=`100` | Unpredictable behaviour |
| TCM/SRAM read before 64-bit ECC init write | ECC error |
| Relying on MPU to stop DMA | **It cannot** — use XRDC |
