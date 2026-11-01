---
title: "S32K5 MPU 速查表"
---

配套主文档：[S32K5_R52_M7_MPU_Design_CN.md](S32K5_R52_M7_MPU_Design_CN.md) / [S32K5_R52_M7_MPU_Design_EN.md](S32K5_R52_M7_MPU_Design_EN.md)

> 2026-11-01 同步主文档重组：寄存器位域按 ARM TRM 修正、地址全部换为 S32K566 实测值（S32K3 时代的 `0x2040_xxxx` 地址在 S32K5 上不存在）。

---

## 寄存器速查

### Cortex-M7（PMSAv7，SCS `0xE000ED9x`）

| 寄存器 | 地址 | 说明 |
| --- | --- | --- |
| `MPU_TYPE` | `0xE000ED90` | RO；`DREGION[15:8]` 探测区域数（S32K566 = 16） |
| `MPU_CTRL` | `0xE000ED94` | `[0]` ENABLE、`[1]` HFNMIENA、`[2]` PRIVDEFENA |
| `MPU_RNR` | `0xE000ED98` | 选区域号 |
| `MPU_RBAR` | `0xE000ED9C` | `[31:5]` ADDR、`[4]` VALID、`[3:0]` REGION |
| `MPU_RASR` | `0xE000EDA0` | 属性 + SIZE + ENABLE（见下） |

### Cortex-R52（Armv8-R PMSAv8-32，EL1 MPU）

| 寄存器 | cp15 编码 | 说明 |
| --- | --- | --- |
| `MPUIR` | `MRC p15, 0, Rt, c0, c0, 4` | RO；`DREGION[15:8]`（S32K566 = 20） |
| `PRSELR` | `MCR/MRC p15, 0, Rt, c6, c2, 1` | 选区域号，20 区域实现为 `[4:0]` |
| `PRBAR` | `c6, c3, 0` | `[31:6]` BASE、`[4:3]` SH、`[2:1]` AP、`[0]` **XN** |
| `PRLAR` | `c6, c3, 1` | `[31:6]` LIMIT（含端点）、`[3:1]` AttrIndx、`[0]` EN |
| `MAIR0/1` | `c10, c2, 0/1` | 8 槽 × 8 bit 内存属性 |
| `SCTLR` | `c1, c0, 0` | `[0]` M、`[17]` BR、`[19]` WXN、`[20]` UWXN |
| `HCR` | `c1, c1, 0` | `DC` / `VM` —— S32K5 保持 0 |

EL2 侧（`p15, 4, ...`）：`HMPUIR` / `HPRSELR` / `HPRBAR` / `HPRLAR` / `HPRENR`（`c6, c1, 1`）/ `HMAIR0/1`。

> **注意**：EL1 没有 `PRENR`——区域使能只由 `PRLAR.EN` 决定；位掩码使能寄存器只有 EL2 的 `HPRENR`。region 16–19 只能经 `PRSELR` 间接访问。

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

### R52（2 bit，`PRBAR[2:1]`）

| AP | EL1 | EL0 |
| --- | --- | --- |
| `00` | RW | 无 |
| `01` | RW | RW |
| `10` | RO | 无 |
| `11` | RO | RO |

> M7 的 `010`（特权 RW + 用户 RO）混合编码在 R52 上**无对应**——需 OS 任务切换时改写区域 AP。

---

## XN / SH 位置对照

| | M7 | R52 |
| --- | --- | --- |
| XN | `MPU_RASR[28]` | **`PRBAR[0]`**（与基址同寄存器，评审易漏） |
| Shareable | `RASR[18]` S 位 | `PRBAR[4:3]` SH：`00` Non、`10` Outer、`11` Inner、`01` ❌ UNPREDICTABLE |
| WXN | 无此概念 | `SCTLR[19]` WXN / `[20]` UWXN，复位 0；置 1 会破坏 ATCM（必须可执行） |

---

## 内存属性对照

### M7：TEX/C/B/S

| 用途 | TEX | C | B | S |
| --- | --- | --- | --- | --- |
| Strongly-ordered | `000` | 0 | 0 | 固定 Shareable |
| Device Shared | `000` | 0 | 1 | 固定 Shareable |
| Device Non-shared | `010` | 0 | 0 | 固定 Non-shareable |
| Normal WT | `000` | 1 | 0 | S |
| Normal WB no-WA | `000` | 1 | 1 | S |
| Normal WB RA | `001` | 1 | 1 | S |
| Normal NC | `001` | 0 | 0 | S |

### R52：MAIR 值（S32K5 方案）

| AttrIndx | 值 | 含义 | 用途 |
| --- | --- | --- | --- |
| 0 | `0xFF` | Normal, RW, WB, RA | MRAM / SRAM |
| 1 | `0x00` | Device-nGnRnE（最严格） | PPB |
| 2 | `0xBB` | Normal, RW, WT（no WA） | 保留 |
| 3 | `0x04` | Device-nGnRE | 外设桥 |
| 4 | `0x44` | Normal, Non-cacheable | LPE_SRAM Code 只读视图 |

Device 严格度：`0x00` nGnRnE > `0x04` nGnRE > `0x0C` nGRE > `0x0F` GRE。

---

## 尺寸编码

| 平台 | 公式 | 最小 | 对齐 | 重叠 |
| --- | --- | --- | --- | --- |
| M7 | size = 2^(SIZE+1) | 32 B | BASE 按 size 对齐（不足则**悄悄扩大**） | 允许，编号大者优先 |
| R52 | LIMIT 含端点 | 64 B | BASE/LIMIT 按 64 B（不足即**异常**） | **禁止**，多重命中 = translation fault |

> PMSAv7 幂约束的 S32K566 实例：3 MB SRAM0-2 拆 2+1 MB；外设窗（约 50 MB）拆 32+8 MB。R52 同空间可单区覆盖。

---

## SRD 子区域（仅 M7）

区域 ≥ 256 B 时分 8 段，`SRD[n]=1` 禁用第 n 段，`SRD[0]` 对应最低地址。
区域为 32/64/128 B 时写 SRD **结果不可预测**。

---

## S32K566 资源速查（全部为实测地址）

| 资源 | 地址 | 大小 | M7 属性 | R52 属性 | XN | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| Code MRAM Bank A | `0x0800_0000`–`0x08FF_FFFF` | 16 MB | Normal WB RA | Attr0 | 0 | FOTA 期可收紧 RO+X |
| Code MRAM Bank B | `0x0900_0000`–`0x09FF_FFFF` | 16 MB | Normal WB RA | Attr0 | 0 | A/B 分区隔离 |
| Data MRAM | `0x0C80_0000`–`0x0C83_FFFF` | 256 KB | Normal WB RA | Attr0 | 1 | |
| M7 SRAM0-2 | `0x2100_0000`–`0x212F_FFFF` | 3 MB | WB，NC/shareable 子区重叠收紧 | —（R52 作跨核共享 Attr0） | 1 | **不是 2 的幂**，M7 拆 2+1 MB |
| R52 SRAM | `0x2200_0000`–`0x220F_FFFF` | 1 MB | — | Attr0 | 1 | 防其他 master 需 XRDC `CPE_MRC0-3` |
| LPE_SRAM Code | `0x1000_0000`–`0x1003_FFFF` | 256 KB | Normal NC，特权 RO | Attr4 `0x44`，RO | 1 | Standby 保持 |
| LPE_SRAM Data | `0x2400_0000`–`0x2401_FFFF` | 128 KB | 不建区 | Attr0 | 1 | M7 不访问 |
| ITCM | `0x0000_0000`（32 KB） | 32 KB | Normal NC | — | 0 | **与 LPE_SRAM alias 共用 1 MB 窗口**；读前 64-bit 写初始化 ECC |
| DTCM | `0x2000_0000`（64 KB） | 64 KB | Normal NC | — | 1 | backdoor `0x2300_0000`+ 需 XRDC `MRC_B3` |
| R52 ATCM/BTCM/CTCM | `0x0100/0110/0120_0000`（CPU1：`0x0140/0150/0160`） | 各 32 KB | — | Attr0 | **ATCM=0**，其余 1 | ATCM 必须可执行（WXN 冲突）；backdoor 需 `CPE_MRC4` |
| XSPI | `0x8100_0000`+ | 1024 MB | **不建区**（背景 no-access） | **不建区**（BR=0 fault） | — | 本项目不使用 |
| 外设 | `0x4000_0000`–`0x431F_FFFF` | — | Device，2 区（32+8 MB） | Device-nGnRE 单区 | 1 | 最后外设 `0x4219_7FFF`；含 DSP 桥与 GIC |
| PPB | `0xE000_0000`–`0xE00F_FFFF` | 1 MB | Device | Attr1 `0x00` | 1 | 本核私有；**必须特权/EL1 可写** |

**区域预算**：M7 16 区 = 13 静态 + 3 OS 动态；R52 EL1 20 区 = 12 静态 + 8 OS 动态。
**背景策略**：M7 `PRIVDEFENA=0` + 4 GB 背景 no-access（SDEN 1013783-B workaround）；R52 `SCTLR.BR=0`，未命中即 fault。

---

## MPU 与 XRDC 对照

| | MPU | XRDC |
| --- | --- | --- |
| 约束对象 | 仅本核 | 所有 master（核 + eDMA + MAC） |
| 能否挡 DMA | 不能 | **能** |
| 能否禁执行 | **能**（XN） | **不能**（无 XN 属性） |
| 配置粒度 | 每核一套 | 全片一套（16 Domain ID，768 PDAC slot） |
| 违规异常 | MemManage / Abort | Bus Fault（独立入口） |
| 隔离层级 | 任务级 | 核心级 |
| 启用顺序 | 先配后使能 | **先配完 descriptor 再置 `GVLD=1`**，否则自锁 |

---

## MRAM 与 eFlash 对照

| | MRAM (S32K5) | eFlash (S32K3) |
| --- | --- | --- |
| 寻址 | 字节 | 页/块 |
| 写前擦除 | 不需要 | 需要 |
| 写入速度 | 8.8–15 MB/s | 其 1/10–1/15 |
| 耐久 | 约 100 万次写 | 约 1 万–10 万次擦写 |
| A/B 切换 | 硬件 Flexible A/B swap + RWW（2 MB 分区粒度） | — |

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
| R52 区域重叠 | Translation fault（fail fast，属期望行为） |
| R52 `SCTLR.WXN=1` | ATCM 被强制 XN，核无法启动 —— 逐 region 管 XN |
| R52 自检只遍历 region 0–15 | region 16–19 被静默跳过 —— 用 `PRSELR` 间接访问 |
| 忘开 `MEMFAULTENA` | fault 升级为 HardFault |
| 用 M7 AP=`100` / R52 SH=`01` | 行为不可预测（分别是保留值 / UNPREDICTABLE） |
| TCM/SRAM 读前未做 64-bit ECC 初始化写 | ECC 报错（仅 POR 时做） |
| 指望 MPU 挡住 DMA | **挡不住** —— 用 XRDC |
| 指望 XRDC 禁执行 | **XRDC 无 XN** —— 禁执行只能在核 MPU 里做 |
| XRDC `GVLD` 提前置位 | 被保护内存不可访问 —— 先配完再使能 |
| OMU 量产未禁用 | 读被静默重映射 —— 量产置 `OER[OE]=0`，FCCU 监控 |
