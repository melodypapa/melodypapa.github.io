# S32K5 MPU 速查表

配套主文档：[S32K5_R52_M7_MPU_Design_CN.md](S32K5_R52_M7_MPU_Design_CN.md) / [S32K5_R52_M7_MPU_Design_EN.md](S32K5_R52_M7_MPU_Design_EN.md)

---

## 寄存器速查

### Cortex-M7（PMSAv7，SCS `0xE000ED9x`）

| 寄存器 | 地址 |
| --- | --- |
| `MPU_TYPE` | `0xE000ED90` |
| `MPU_CTRL` | `0xE000ED94` |
| `MPU_RNR` | `0xE000ED98` |
| `MPU_RBAR` | `0xE000ED9C` |
| `MPU_RASR` | `0xE000EDA0` |

### Cortex-R52（Armv8-R）

| 寄存器 | 访问方式 |
| --- | --- |
| `PRBAR` / `PRLAR` | `MCR p15, 0, Rt, c6, c3, 0/1`（经 `PRSELR`） |
| `HPRBAR` / `HPRLAR` | `MCR p15, 0, Rt, c6, c3, 2/3` |
| `MAIR0/1` | `MCR p15, 0, Rt, c10, c2, 0/1` |
| `PRENR` | `MCR p15, 0, Rt, c12, c0, 2`（需按集成确认） |
| `SCTLR` | `MCR p15, 0, Rt, c1, c0, 0` |

---

## AP 权限对照

### M7（3 bit，`RASR[26:24]`）

| AP | 特权 | 非特权 |
| --- | --- | --- |
| `000` | 无 | 无 |
| `001` | RW | 无 |
| `010` | RW | RO |
| `011` | RW | RW |
| `100` | ❌ 保留 | ❌ 保留 |
| `101` | RO | 无 |
| `110` | RO | RO |
| `111` | RO | RO |

### R52（2 bit，`PRBAR[3:2]`）

| AP | 含义 |
| --- | --- |
| `00` | RW，本 EL 及更低 |
| `01` | RW，仅本 EL |
| `10` | RO，本 EL 及更低 |
| `11` | RO，仅本 EL |

---

## 内存属性对照

### M7：TEX/C/B/S

| 用途 | TEX | C | B | S |
| --- | --- | --- | --- | --- |
| Strongly-ordered | `000` | 0 | 0 | 忽略 |
| Device Shared | `000` | 0 | 1 | 忽略 |
| Device Non-shared | `010` | 0 | 0 | 忽略 |
| Normal WT | `000` | 1 | 0 | S |
| Normal WB no-WA | `000` | 1 | 1 | S |
| Normal WB RA | `001` | 1 | 1 | S |
| Normal NC | `001` | 0 | 0 | S |

### R52：MAIR 值

| 索引 | 值 | 含义 |
| --- | --- | --- |
| 0 | `0xFF` | Normal, RW, WB, RA |
| 1 | `0x04` | Device-nGnRnE |
| 2 | `0xBB` | Normal, RW, WT |
| 3 | `0x00` | Strongly-ordered |

---

## 尺寸编码

| 平台 | 公式 | 最小 | 对齐 |
| --- | --- | --- | --- |
| M7 | size = 2^(SIZE+1) | 32 B | BASE 按 size 对齐 |
| R52 | LIMIT 含端点 | 64 B | BASE/LIMIT 均 64 B |

---

## SRD 子区域（仅 M7）

区域 ≥ 256 B 时分 8 段，`SRD[n]=1` 禁用第 n 段，`SRD[0]` 对应最低地址。
区域为 32/64/128 B 时写 SRD **结果不可预测**。

---

## S32K5 存储类型速查

| 存储类型 | 地址 | M7 | R52 | XN | 备注 |
| --- | --- | --- | --- | --- | --- |
| Code MRAM | `0x0800_0000` | Normal WB RA | Normal WB RA | 0 | 32–41 MB；两核属性必须一致 |
| M7 SRAM 主区 | `0x2040_0100` | Normal WB RA | — | 1 | 共 1.5 MB |
| M7 SRAM NC | `0x2040_8000` | Normal NC | — | 1 | 32 KB |
| M7 SRAM shareable | `0x2041_0000` | Normal WB + Shareable | Normal WB + Shareable | 1 | 32 KB，双方配置一致 |
| Standby RAM | `0x2040_0000` | **Normal NC** | — | 1 | 256 B，硬约束 |
| R52 SRAM | 见 RM | — | Normal WB RA | 1 | `cpe_sram`，1 MB；需 XRDC 防护 |
| ITCM | `0x0000_0000` | Normal NC | — | 0 | 32 KB |
| DTCM | `0x2000_0000` | Normal NC | — | 1 | 60 KB + 4 KB 栈 |
| XSPI 数据 | `0x8100_0000` | Normal NC | Normal NC | 0 | 外部 flash / HyperRAM |
| 外设 | `0x4000_0000`–`0xE00F_FFFF` | Device-nGnRnE | Device-nGnRnE | 1 | 上限是 `0xE00F_FFFF`，不是 4 GB |
| PPB | `0xE000_0000`+ | Device-nGnRnE | Device-nGnRnE | 1 | 本核私有，单独建区 |

---

## MPU 与 XRDC 对照

| | MPU | XRDC |
| --- | --- | --- |
| 约束对象 | 仅本核 | 所有 master（核 + eDMA + MAC） |
| 能否挡 DMA | 不能 | **能** |
| 配置粒度 | 每核一套 | 全片一套 |
| 违规异常 | MemManage / Abort | Bus Fault |
| 隔离层级 | 任务级 | 核心级 |

---

## MRAM 与 eFlash 对照

| | MRAM (S32K5) | eFlash (S32K3) |
| --- | --- | --- |
| 寻址 | 字节 | 页/块 |
| 写前擦除 | 不需要 | 需要 |
| 写入速度 | 8.8–15 MB/s | 其 1/10–1/15 |
| 耐久 | 约 100 万次写 | 约 1 万–10 万次擦写 |

---

## 三条铁律

1. **编程代码不能位于被重配区域内** —— 否则改权限时取指失败，CPU 卡死。
2. **DSB 在前，ISB 在后** —— 确保改动生效。
3. **改 cache 属性后必须 clean/invalidate cache** —— 否则旧数据被复用。

---

## 必踩的坑

| 坑 | 表现 |
| --- | --- |
| 外设配 Normal cacheable | 读旧值、写丢失，无 fault |
| M7 BASE 未按 SIZE 对齐 | 保护范围悄悄扩大 |
| R52 区域重叠 | Translation fault（这算好的，fail fast） |
| Standby RAM 配 cacheable | 进低功耗后数据丢失 |
| 忘开 `MEMFAULTENA` | fault 升级为 HardFault |
| 用 M7 AP=`100` | 行为不可预测 |
| TCM/SRAM 读前未做 64-bit ECC 初始化写 | ECC 报错 |
| 指望 MPU 挡住 DMA | **挡不住** —— 用 XRDC |
