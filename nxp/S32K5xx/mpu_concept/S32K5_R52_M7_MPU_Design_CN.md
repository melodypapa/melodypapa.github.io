# S32K5xx MPU 内存保护单元设计方案（Cortex-M7 + Cortex-R52）

> 适用平台：NXP S32K5xx 系列（S32K566 / S32K58 等），Cortex-M7 平台核 + Cortex-R52 计算核
>
> 资料来源：Arm Cortex-M7 TRM（ARMv7-M PMSAv7）、Arm Cortex-R52 TRM r1p2（Armv8-R PMSAv8-32）、Cortex-R52/R52+ Programmer's Guide、NXP S32K Knowledge Base / Zephyr S32K5XXCVB 板级文档
>
> **地址权威来源**：NXP S32K5xx Reference Manual **Rev.3（rm1131130）**及其内嵌附件 **`S32K5xx_memory_map.xlsx`**（"Overview Memory Map" / "Peripherals Memory Map" 两个 tab）。第 4、5 章的所有地址均取自该附件，取代了早期版本中源自 S32K3 的估算值。
>
> **修订说明（2026-10-14）**：Rev.B —— §4/§5 的全部地址已按 Rev.3 memory map 核实替换；§11 十三项待确认中十二项已关闭。新增发现：`WXN` 复位值、ATCM 与 WXN 冲突、TCM backdoor 矩阵、REG_PROT strongly-ordered 耦合、secure/non-secure alias 规则、OMU 只重映射读、XRDC 无 XN。
>
> 注意：寄存器取值以 Arm 架构规范为准。量产前必须与该型号的 Reference Manual 逐条核对。

---

## 1. 为什么在 S32K5 上必须做 MPU 设计

S32K5 是 ASIL D 平台，三簇异构核共用同一套 MRAM 与 SRAM：

| 核簇 | 定位 | S32K566 配置 | 典型任务 |
| --- | --- | --- | --- |
| Cortex-R52 | 计算 / 实时 | 2 核（单 cluster 内，可配 1×Lockstep 或 2×Single Core） | 安全监控、实时控制、Hypervisor |
| Cortex-M7 | 平台 | **4 核**（纯 lockstep：3 个用户核；解耦：2 lockstep + 2 单核） | 通信栈、非实时任务、网关 |
| Cortex-M4 | 低功耗引擎 | 1 核 | LPRUN / Standby 期间值守 |

> **核数纠正**：本文档早期版本写 S32K566 为"6 个 Cortex-M7 核"，这是错的。RM Rev.3 Table 9（"Arm platforms: description"）明确主平台域支持**四个** Cortex-M7。家族特性表里的"6×"是把 lockstep 对折算成两个逻辑核；memory map 与 MSCM 都只暴露 `M7_0`–`M7_3`。MPU region 预算必须按 **4** 计算。
> `[来源: rm1131130 Rev.3, Chapter_02 Table 9; memory_map.xlsx ITCM_0..3 / DTCM_0..3]`

MPU 在这套系统里承担的是**职责隔离**而非仅仅是内存保护：

1. **核间隔离** —— R52 与 M7 各自有独立 SRAM 分区（R52 侧 `cpe_sram` 1 MB，M7 侧 SRAM0-2 共 3 MB）。MPU 保证一个核的任务无法越界破坏另一个核的栈或数据。
2. **多任务隔离** —— M7 上跑 Linux/RTOS 混合负载、R52 上跑 AUTOSAR OS，需要 task 级保护。
3. **故障安全** —— 一次非法访问必须被**立即捕获并转为受控异常**，而不是静默地让错误扩散到总线事务。这对 ASIL D 的内存安全性（避免非受控跳转到 RAM）至关重要。
4. **Cache 属性一致性** —— S32K5 的 MRAM/SRAM 有 cacheable / non-cacheable / shareable 的硬件分区（如 `int_sram_no_cacheable`、`int_sram_shareable`），MPU 是软件侧统一这个属性的唯一手段。

> **安全关键提醒**：MPU 本身**不提供**运行时地址重定位。一旦某段内存没有按最小权限配置，MPU 会放行 —— 它是"白名单过滤器"，不是"沙箱"。漏配一个区域等于完全放弃该区域的保护。
>
> **更重要的一条**：MPU 只约束**本核**的访问，**挡不住 DMA**。eDMA、以太网 MAC、CAN 等 master 绕过 CPU 的 MPU 直接打总线。要拦住它们必须配 **XRDC**（NXP 的扩展资源域控制器）—— 详见第 5.8 节。S32K5 的安全设计如果只做 MPU，等于给非受控写入留了一扇敞开的大门。

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 452" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>M7 与 R52 的 MPU 架构差异对比</title>
<desc>左侧 Cortex-M7 使用 ARMv7-M PMSAv7，通过 MPU_RNR/RBAR/RASR 三寄存器组以 SIZE 编码区域大小，支持子区域禁用和区域重叠优先级；右侧 Cortex-R52 使用 Armv8-R PMSAv8-32，通过 PRBAR/PRLAR 基址-上限寄存器对定义区域，最小 64 字节粒度、区域不可重叠，并具备 EL1/EL2 双 MPU 两级保护。</desc>
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<rect x="40" y="20" width="285" height="410" rx="14" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="182" y="46" text-anchor="middle" font-size="14" font-weight="500" fill="#0C447C">Cortex-M7</text>
<text x="182" y="66" text-anchor="middle" font-size="12" fill="#185FA5">ARMv7-M PMSAv7</text>
<rect x="60" y="84" width="245" height="66" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
<text x="182" y="105" text-anchor="middle" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">寄存器模型</text>
<text x="182" y="124" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">RNR + RBAR + RASR</text>
<text x="182" y="140" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">基址 + SIZE 编码</text>
<rect x="60" y="162" width="245" height="66" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
<text x="182" y="183" text-anchor="middle" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">区域数量</text>
<text x="182" y="202" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">最多 16 个（8~15 可选）</text>
<text x="182" y="218" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">MPU_TYPE.DREGION 可探测</text>
<rect x="60" y="240" width="245" height="66" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
<text x="182" y="261" text-anchor="middle" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">区域特性</text>
<text x="182" y="280" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">可重叠，编号大者优先</text>
<text x="182" y="296" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">SRD 子区域 8 段屏蔽</text>
<rect x="60" y="318" width="245" height="66" rx="8" fill="#B5D4F4" stroke="#185FA5" stroke-width="0.5"/>
<text x="182" y="339" text-anchor="middle" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">权限维度</text>
<text x="182" y="358" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">特权 / 非特权 两级</text>
<text x="182" y="374" text-anchor="middle" font-size="12" fill="#0C447C" dominant-baseline="central">MPU_CTRL 一套</text>
<rect x="60" y="396" width="245" height="20" rx="6" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="182" y="406" text-anchor="middle" font-size="12" fill="#2C2C2A" dominant-baseline="central">故障：MemManage</text>
<rect x="355" y="20" width="285" height="410" rx="14" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="497" y="46" text-anchor="middle" font-size="14" font-weight="500" fill="#3C3489">Cortex-R52</text>
<text x="497" y="66" text-anchor="middle" font-size="12" fill="#534AB7">Armv8-R PMSAv8-32</text>
<rect x="375" y="84" width="245" height="66" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="497" y="105" text-anchor="middle" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">寄存器模型</text>
<text x="497" y="124" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">PRBAR + PRLAR 寄存器对</text>
<text x="497" y="140" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">基址 + 上限（含端点）</text>
<rect x="375" y="162" width="245" height="66" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="497" y="183" text-anchor="middle" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">区域数量</text>
<text x="497" y="202" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">EL1：16 / 20 / 24</text>
<text x="497" y="218" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">EL2：0 / 16 / 20 / 24</text>
<rect x="375" y="240" width="245" height="66" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="497" y="261" text-anchor="middle" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">区域特性</text>
<text x="497" y="280" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">禁止重叠，多重命中报错</text>
<text x="497" y="296" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">64 B 粒度，无 SRD</text>
<rect x="375" y="318" width="245" height="66" rx="8" fill="#CECBF6" stroke="#534AB7" stroke-width="0.5"/>
<text x="497" y="339" text-anchor="middle" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">权限维度</text>
<text x="497" y="358" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">EL0 / EL1 / EL2 三级</text>
<text x="497" y="374" text-anchor="middle" font-size="12" fill="#3C3489" dominant-baseline="central">双 MPU 取最小权限</text>
<rect x="375" y="396" width="245" height="20" rx="6" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="497" y="406" text-anchor="middle" font-size="12" fill="#2C2C2A" dominant-baseline="central">故障：权限错 + 转换错</text>
<path d="M325 225 L355 225" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)" marker-start="url(#ar)"/>
<text x="340" y="212" text-anchor="middle" font-size="11" fill="#5F5E5A">不同</text>
</svg>
</figure>

---

## 2. Cortex-M7 MPU 详解（ARMv7-M PMSAv7）

### 2.1 寄存器组

M7 只有**一套** MPU，寄存器位于系统控制空间（SCS），基址 `0xE000ED90`：

| 寄存器 | 地址 | 作用 |
| --- | --- | --- |
| `MPU_TYPE` | `0xE000ED90` | 只读，探测是否实现 MPU 及区域数（DREGION） |
| `MPU_CTRL` | `0xE000ED94` | 使能 MPU、背景区域、故障期行为 |
| `MPU_RNR` | `0xE000ED98` | 选择当前操作的 region 号 |
| `MPU_RBAR` | `0xE000ED9C` | 区域基址 + VALID |
| `MPU_RASR` | `0xE000EDA0` | 区域属性 + 大小 + 使能 |

编程模型是**"先选号，再写属性"**：写 `MPU_RNR = n`，然后写 `MPU_RBAR` 和 `MPU_RASR`。CMSIS 把它封装成 `ARM_MPU_SetRegion()`。

### 2.2 MPU_RASR 位域

```
 31        28  26  24  21  19  18  17  16   15    8  6  5    1   0
┌────────────┬───────┬───────┬───┬─┬───┬───┬────────┬──┬──────┬───┐
│   ATTRS    │  RES  │ AP[2:0]│TEX│S│ C│ B │  SRD   │R │ SIZE │EN │
└────────────┴───────┴───────┴───┴─┴───┴───┴────────┴──┴──────┴───┘
              XN
```

| 字段 | 位 | 说明 |
| --- | --- | --- |
| `XN` | `[28]` | Execute Never，1 = 禁止从该区取指执行 |
| `AP[2:0]` | `[26:24]` | 访问权限，见下表 |
| `TEX[2:0]` | `[21:19]` | 内存类型扩展，与 C/B/S 组合 |
| `S` | `[18]` | Shareable |
| `C` | `[17]` | Cacheable |
| `B` | `[16]` | Bufferable |
| `SRD[7:0]` | `[15:8]` | 子区域禁用，≥256 B 时分 8 段 |
| `SIZE[4:0]` | `[5:1]` | 区域大小 = 2^(SIZE+1) 字节，< 4 保留（最小 32 B） |
| `ENABLE` | `[0]` | 区域使能（还需 `MPU_CTRL.ENABLE`） |

**基址对齐约束**：region 的 ADDR 必须按 SIZE 对齐。例如 64 KB 区域必须落在 `0x00010000` 边界上，不能是 `0x00010001`。这是 PMSAv7 最容易踩的坑 —— 链接脚本里的段地址若未按 2 的幂对齐，写进去的 ADDR 低位会被忽略，MPU 实际保护的是一个大一倍的区域。

### 2.3 AP 访问权限编码

| AP[2:0] | 特权访问 | 非特权访问 | 说明 |
| --- | --- | --- | --- |
| `000` | 无访问 | 无访问 | 任何访问都产生 permission fault |
| `001` | 读/写 | 无访问 | 仅特权可访问 |
| `010` | 读/写 | 只读 | 非特权写产生 fault |
| `011` | 读/写 | 读/写 | 完全访问 |
| `100` | unpredictable | unpredictable | **保留，禁止使用** |
| `101` | 只读 | 无访问 | 特权只读 |
| `110` | 只读 | 只读 | 特权与非特权均只读 |
| `111` | 只读 | 只读 | 同 110 |

### 2.4 TEX/C/B/S 内存属性编码

| TEX | C | B | 内存类型 / 缓存属性 | Shareable |
| --- | --- | --- | --- | --- |
| `000` | 0 | 0 | Strongly-ordered | 固定 Shareable |
| `000` | 0 | 1 | Device, Shared device | 固定 Shareable |
| `000` | 1 | 0 | Normal, WT, no write-allocate | S 位 |
| `000` | 1 | 1 | Normal, WB, no write-allocate | S 位 |
| `001` | 0 | 0 | Normal, Non-cacheable | S 位 |
| `001` | 0 | 1 | Reserved | — |
| `001` | 1 | 0 | 实现定义 | — |
| `001` | 1 | 1 | Normal, WB, write+read allocate | S 位 |
| `010` | 0 | 0 | Device, Non-shared device | 固定 Non-shareable |
| `010` | 0 | 1 | Reserved | — |
| `010` | 1 | X | Reserved | — |
| `011` | X | X | Reserved | — |
| `1BB` | `BAA` | `A` | Normal, Cached（AA/BB 编码缓存策略） | S 位 |

其中 `{TEX,C,B} = 1BB` 时的 AA/BB 缓存策略：

| AA 或 BB | 缓存策略 |
| --- | --- |
| `00` | Non-cacheable |
| `01` | Write-back, write and read allocate |
| `10` | Write-through, no write allocate |
| `11` | Write-back, no write allocate |

**外设必须用 Device 类型**。这是 M7 上最高频的错误：把 UART、FLEXCAN、GPIO 寄存器窗口配成 Normal cacheable，会导致寄存器读回旧值、外设写入被 cache 吞掉。正确做法是 `TEX=000, C=0, B=1`（Shared Device）或 `TEX=010, C=0, B=0`（Non-shared Device）。

### 2.5 MPU_CTRL 三位语义

| 位 | 名称 | 语义 |
| --- | --- | --- |
| `0` | `ENABLE` | MPU 总使能。为 0 时其他寄存器配置全部无效 |
| `1` | `HFNMIENA` | HardFault / NMI / FAULTMASK 期间是否仍启用 MPU |
| `2` | `PRIVDEFENA` | 特权代码是否可使用默认内存映射作为背景区域 |

`HFNMIENA` 的取舍：`=0` 时故障处理器不受 MPU 约束，方便完整 dump 现场内存做离线分析；`=1` 时连故障处理器也受限，防篡改更强但现场信息可能残缺。做安全诊断固件时通常置 0 并把现场存入专用 no-cacheable 区域。

### 2.6 区域重叠与子区域

- **重叠时编号大的优先**：区域 0 和区域 1 覆盖同一段内存，区域 1 的属性生效。这是 PMSAv7 最有用的特性 —— 可以先用一个大区域定基调，再叠加小区域收紧。
- **SRD 子区域**：区域 ≥ 256 B 时被等分为 8 段，`SRD[n]=1` 表示禁用第 n 段，`SRD[0]` 对应最低地址段。**注意：区域为 32/64/128 B 时写 SRD 结果不可预测**。

### 2.7 M7 内存属性推荐表（S32K5 视角）

| 区域 | 地址 / 大小 | TEX/C/B | AP | XN | 说明 |
| --- | --- | --- | --- | --- | --- |
| Code MRAM | `0x0800_0000`，32 MB | `001/1/1` WB | `011` | 0 | 可执行可写（支持 FOTA A/B 切换需 RW） |
| M7 SRAM0-2 | `0x2100_0000`–`0x212F_FFFF`，3 MB | `001/1/1` WB | `011` | 1 | 栈、堆、.data/.bss —— **数据区，故 XN=1** |
| SRAM NC 子分区 | 按链接脚本 | `001/0/0` NC | `011` | 1 | 需与硬件/其他核一致的数据 |
| LPE_SRAM（M7 视图） | `0x1000_0000`，256 KB | `001/0/0` NC | `011` | 1 | Rev.A 的"Standby RAM `0x2040_0000`"是 S32K3 的，见 §4.1 纠正第 3 条 |
| ITCM | `0x0000_0000`，32 KB | `001/1/1` WB | `011` | 0 | 中断向量与热点代码。**与 LPE_SRAM alias 共用 1 MB 窗口** |
| DTCM | `0x2000_0000`，64 KB | `001/1/1` WB | `011` | 1 | 栈数据，不可执行 |
| 外设窗口 | `0x4000_0000`–`0x421F_FFFF` | `010/0/0` Device | `011` 或 `101` | 1 | 必须 Device 类型 —— 同时是 REG_PROT 错误捕获的前提（§5.7） |
| XSPI 数据 | `0x8100_0000`–`0xC0FF_FFFF` | `001/0/0` NC | `011` | 0 | 外部 flash 执行 |
| PPB | `0xE000_0000`–`0xE00F_FFFF` | `010/0/0` Device | `101` | 1 | 本核私有 |

### 2.8 M7 配置代码骨架

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

    /* 1. 关闭 MPU 后再配置，避免中间态产生意外 fault */
    MPU_CTRL = 0U;
    __DSB();
    __ISB();

    /* 2. 逐区域写入。编程代码本身不能位于被重配的区域内 */
    /* 区域 0：外设 Device Non-shareable, RO, XN */
    MPU_RNR(0)  = 0U;
    MPU_RBAR(0) = 0x40000000U | MPU_RBAR_VALID_Msk;
    MPU_RASR(0) = rasr_make(29U,        /* SIZE=29 -> 2^30 = 1 GB      */
                            5U,         /* AP=101 特权 RO             */
                            2U, 0U, 0U, /* TEX=010,C=0,B=0 -> Device  */
                            0U,         /* S=0 非共享                */
                            1U,         /* XN=1                      */
                            0x00U);

    /* 区域 1：SRAM cacheable, RW, XN（数据区） */
    MPU_RNR(1)  = 1U;
    MPU_RBAR(1) = 0x20400000U | MPU_RBAR_VALID_Msk;
    MPU_RASR(1) = rasr_make(19U,        /* SIZE=19 -> 2^20 = 1 MB      */
                            3U,         /* AP=011 全访问             */
                            1U, 1U, 1U, /* TEX=001,C=1,B=1 -> WB     */
                            0U,
                            1U,         /* XN=1                      */
                            0x00U);

    /* 区域 2：Code MRAM, RW, 可执行 */
    MPU_RNR(2)  = 2U;
    MPU_RBAR(2) = 0x08000000U | MPU_RBAR_VALID_Msk;
    MPU_RASR(2) = rasr_make(28U,        /* SIZE=28 -> 2^29 = 512 MB   */
                            3U,
                            1U, 1U, 1U,
                            1U,         /* S=0                       */
                            0U,         /* XN=0 允许执行             */
                            0x00U);

    /* 3. 使能前完成所有 DSB，确保写入落地 */
    __DSB();

    /* 4. 使能 MPU，保留特权默认内存映射作为背景 */
    ctl = MPU_CTRL;
    ctl |= (1UL << 0)   /* ENABLE      */
        |  (1UL << 2);  /* PRIVDEFENA */
    MPU_CTRL = ctl;
    __DSB();
    __ISB();
}

uint32_t M7_MPU_GetRegionCount(void)
{
    return (MPU_TYPE >> 8) & 0xFFU;   /* DREGION 字段 */
}
```

> 上例的 SIZE 值需按实际链接脚本调整。**务必先用 `MPU_TYPE.DREGION` 确认实现了多少区域再访问**，写越界区域号的行为未定义。

### 2.9 MemManage 异常处理

```c
void MemManage_Handler(void)
{
    /* 1. 先抓现场，再考虑清理 */
    uint32_t ipsr   = __get_IPSR();
    uint32_t mfsr   = SCB->CFSR & 0xFFU;        /* MemManage 状态 */
    uint32_t hfsr   = SCB->CFSR >> 16;
    uint32_t mmfar  = SCB->MMFAR;               /* 出错地址 */
    uint32_t bfar   = SCB->BFAR;
    uint32_t stacked_pc, stacked_lr;
    __asm volatile("mov %0, lr\n" : "=r"(stacked_lr));
    __asm volatile("mov %0, pc\n" : "=r"(stacked_pc));

    /* 2. 存入 no-cacheable 区域供诊断固件读取 */
    FaultRecord_SafeStore(ipsr, mfsr, hfsr, mmfar, bfar,
                          stacked_pc, stacked_lr);

    /* 3. ASIL D 要求：受控停机或安全状态，而非循环重试 */
    Safety_EnterSafeState(FAULT_SRC_MEMM, mmfar);
    for (;;) { }
}
```

`SCB->CFSR` 中 MFSR 字节的含义（判断方向的关键）：

| 位 | 含义 |
| --- | --- |
| `0` | IACCVIOL — 指令取指时权限违规 |
| `1` | DACCVIOL — 数据访问时权限违规 |
| `3` | MUNSTKERR — 异常返回时栈指针非法 |
| `4` | MSTKERR — 压栈时栈指针非法 |
| `5` | MLSPERR — 浮点压栈出错 |
| `7` | MMARVALID — MMFAR 中的地址有效 |

---

## 3. Cortex-R52 MPU 详解（Armv8-R PMSAv8-32）

### 3.1 双 MPU 模型

R52 有**两个独立 MPU**，这是与 M7 最大的架构差异：

| MPU | 控制者 | 区域数 | 生效范围 |
| --- | --- | --- | --- |
| EL1 MPU | EL1（EL2 可代写） | 16 / 20 / 24 | EL0 与 EL1 访问 |
| EL2 MPU | EL2（Hypervisor） | 0 / 16 / 20 / 24（可选） | 叠加在 EL0/EL1 之上 |

组合规则：

- **EL0/EL1 访问** → 两个 MPU 都查，结果取 **least permissive（最小权限组合）**
- **EL2 访问** → 只查 EL2 MPU
- EL2 MPU 可整体禁用（S32K5 一般不用虚拟化，EL2 MPU 保持关闭）

### 3.2 寄存器与 AArch32 访问

| 寄存器 | 作用 |
| --- | --- |
| `PRBAR` / `PRLAR` | EL1 区域基址 / 上限 |
| `HPRBAR` / `HPRLAR` | EL2 区域基址 / 上限 |
| `MAIR0` / `MAIR1` | 内存属性间接寄存器，8 个属性 × 8 bit |
| `PRENR` / `HPRENR` | 区域使能（位掩码） |
| `PRSELR` / `HPRSELR` | 选择目标区域号 |
| `MPUIR` / `HMPUIR` | 区域信息（只读，探测） |

两种编程方式：

```asm
@ 方式一：经 PRSELR 间接访问
MOV   R0, #0                  @ 选区域 0
MCR   p15, 0, R0, c6, c2, 1   @ 写 PRSELR
MCR   p15, 0, R1, c6, c3, 0   @ 写 PRBAR
MCR   p15, 0, R2, c6, c3, 1   @ 写 PRLAR

@ 方式二：直接访问 PRBARn / PRLARn（op1 编码进 c8+）
MCR   p15, 0, R1, c6, c8+n[3:1], 4*n[0]      @ 读 PRBARn
MCR   p15, 0, R1, c6, c8+n[3:1], 4*n[0]+1    @ 读 PRLARn
```

> **易错点**：直接访问方式的 `op1` 计算容易写错（涉及 `c8 + n[3:1]` 与 `4*n[0]`）。建议统一用 PRSELR 间接方式，或直接用 CMSIS 封装的 `__set_PRBAR()` 系列内联函数。

### 3.3 区域定义：基址 + 上限

与 PMSAv7 的根本区别：

| 特性 | PMSAv7（M7） | PMSAv8-32（R52） |
| --- | --- | --- |
| 定义方式 | BASE + SIZE | BASE + LIMIT |
| 上限语义 | 隐含 | **含端点** |
| 对齐要求 | BASE 按 SIZE 对齐 | BASE 与 LIMIT 均按 64 B 对齐 |
| 最小区域 | 32 B | **64 B** |
| 区域重叠 | 允许，编号大者优先 | **禁止，多重命中即报转换错** |

区域地址范围：

```
PRBAR.BASE:0b000000 <= address <= PRLAR.LIMIT:0b111111
```

冒号是位连接运算符。这意味着 BASE 的低 6 位被硬件读为 0，LIMIT 的低 6 位被读为 1 —— **实际粒度 64 字节，且两端都是包含的**。这比 M7 的"按 SIZE 对齐"更直观，但也意味着配错时不会像 M7 那样"悄悄扩成大一倍"，而是立刻产生异常，属于 fail-fast。

### 3.4 PRBAR / PRLAR 字段

| 字段 | 所属 | 语义 |
| --- | --- | --- |
| `BASE` | PRBAR | 区域基址（低 6 位读为 0） |
| `AP` | PRBAR | 访问权限，2 bit |
| `SH` | PRBAR | 可共享性 |
| `LIMIT` | PRLAR | 区域上限（含端点，低 6 位读为 1） |
| `AttrIndx` | PRLAR | 内存属性索引，索引 MAIRx |
| `EN` | PRLAR | 区域使能 |

**AP 编码**：

| AP | 含义 |
| --- | --- |
| `00` | Read/Write，本 EL 及更低 EL |
| `01` | Read/Write，仅本 EL |
| `10` | Read-only，本 EL 及更低 EL |
| `11` | Read-only，仅本 EL |

**SH 编码**：

| SH | 含义 |
| --- | --- |
| `00` | Non-shareable |
| `10` | Outer-shareable |
| `11` | Inner-shareable |

### 3.5 MAIR 内存属性间接

R52 把内存属性从区域寄存器里搬到了 `MAIRx`，每个 MPU 有 8 个 8-bit 属性槽：

| AttrIndx | 典型值 | 内存类型 |
| --- | --- | --- |
| 0 | `0xFF` | Normal, Inner/Outer RW, Write-back, Write-allocate（MRAM/SRAM） |
| 1 | `0x04` | Device-nGnRnE（外设） |
| 2 | `0xBB` | Normal, Inner/Outer RW, Write-through（no write-allocate） |
| 3 | `0x04` | Device-nGnRE |

编程：

```asm
@ 更新 MAIR_EL1 的 Attr0 和 Attr1
MRC   p15, 0, R0, c10, c2, 0       @ 读 MAIR0
LDR   R1, =0xFF
BFI   R0, R1, #0, #8              @ Attr0 = 0xFF (Normal WB RA)
LDR   R1, =0x04
BFI   R0, R1, #8, #8              @ Attr1 = 0x04 (Device-nGnRnE)
MCR   p15, 0, R0, c10, c2, 0       @ 写回
DSB
ISB
```

### 3.6 背景区域与默认内存映射

**指令访问背景区域**：

| 地址范围 | SCTLR.I=1 | SCTLR.I=0 | XN |
| --- | --- | --- | --- |
| `0x0000_0000`–`0x7FFF_FFFF` | Normal, Non-shareable, WT cacheable | Normal, Shareable, Non-cacheable | 允许执行 |
| `0x8000_0000`–`0xFFFF_FFFF` | — | — | **Execute-never** |

**数据访问背景区域**：

| 地址范围 | SCTLR.C=1 | SCTLR.C=0 |
| --- | --- | --- |
| `0x0000_0000`–`0x3FFF_FFFF` | Normal, Non-shareable, WB WA cacheable | Normal, Shareable, NC |
| `0x4000_0000`–`0x5FFF_FFFF` | Normal, Non-shareable, WT cacheable | Normal, Shareable, NC |
| `0x6000_0000`–`0x7FFF_FFFF` | Normal, Shareable, NC | Normal, Shareable, NC |
| `0x8000_0000`–`0xBFFF_FFFF` | Device-nGnRE | Device-nGnRE |
| `0xC000_0000`–`0xFFFF_FFFF` | Device-nGnRnE | Device-nGnRnE |

注意上表中 `0x8000_0000` 以上默认是 Device 类型 —— S32K5 的外设窗口正落在这个范围，默认属性恰好是安全的（不可 cache）。

**关键控制位**：

| 位 | 作用 |
| --- | --- |
| `SCTLR.M` | EL1 MPU 使能。为 0 时使用默认内存映射 |
| `SCTLR.BR` | 背景区域检查。为 1 时 EL1 特权访问未命中区域可用背景区域 |
| `HCR.DC` | 默认 cacheability。为 1 时背景区域用 Normal IB-OB WB + RA 属性 |
| `HCR.VM` | 虚拟化标志，置位后 EL0/EL1 走两阶段 MPU 查找 |

> **陷阱**：`HCR.DC = 1` 时默认属性是**最宽松**的（Normal, IB-OB WB, RA）。与 EL2 MPU 属性组合后结果仍等于 EL2 的属性，EL2 MPU 因此对背景区域完全透明。也就是说 `DC=1` 会让 EL1 背景区域失去它本来的保护意义，S32K5 无虚拟化场景建议保持 `DC=0`。

### 3.7 故障类型

| 故障 | 触发条件 |
| --- | --- |
| Permission fault | 访问命中区域但权限不允许 |
| Translation fault | 访问命中多个区域（重叠）；或未命中任何区域且背景区域不可用 |

M7 只有 Permission fault（MPU 重叠时按优先级选中，不报错），R52 把"重叠"从特性变成了错误。

### 3.8 R52 配置代码骨架

```c
#include <stdint.h>

#define PRBAR(n)  (*((volatile uint32_t *)(uintptr_t)(0x42000000U + 8U * (n))))
#define PRLAR(n)  (*((volatile uint32_t *)(uintptr_t)(0x42000004U + 8U * (n))))
#define PRSELR    (*((volatile uint32_t *)0xE000ED90U))   /* 按集成确认 */

/* MAIR 属性槽 */
#define ATTR_NORMAL_WB   0U
#define ATTR_DEVICE      1U

#define AP_RW_EL0_1      0U   /* Read/Write，本 EL 及更低 */
#define AP_RO_EL0_1      2U
#define SH_NON_SHAREABLE 0U

static inline uint32_t mair_attr(uint8_t idx, uint8_t val)
{
    return (uint32_t)val << (8U * idx);
}

/* 由 BASE/LIMIT 生成 PRBAR/PRLAR：BASE 与 LIMIT 均按 64B 对齐 */
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

    /* 1. 关闭 EL1 MPU */
    *((volatile uint32_t *)0xE000ED10U) &= ~(1UL << 0);  /* SCTLR.M = 0 */
    __DSB();
    __ISB();

    /* 2. 配置 MAIR：Attr0 = Normal WB RA，Attr1 = Device-nGnRnE */
    mair = mair_attr(ATTR_NORMAL_WB, 0xFF) | mair_attr(ATTR_DEVICE, 0x04);
    __set_MAIR(mair);

    /* 3. 区域 0：Code MRAM 可执行可写 */
    PRBAR(0) = prbar_make(0x08000000U, AP_RW_EL0_1, SH_NON_SHAREABLE);
    PRLAR(0) = prlar_make(0x0FFFFFFFU, ATTR_NORMAL_WB, 0U);  /* XN=0 */

    /* 区域 1：R52 SRAM 可读写不可执行 */
    PRBAR(1) = prbar_make(0x20400000U, AP_RW_EL0_1, SH_NON_SHAREABLE);
    PRLAR(1) = prlar_make(0x204FFFFFU, ATTR_NORMAL_WB, 1U);  /* XN=1 */

    /* 区域 2：外设 Device 只读不可执行 */
    PRBAR(2) = prbar_make(0x40000000U, AP_RO_EL0_1, SH_NON_SHAREABLE);
    PRLAR(2) = prlar_make(0xFFFFFFFFU, ATTR_DEVICE, 1U);

    __DSB();
    __ISB();

    /* 4. 使能 SCTLR.M，并置 BR 使特权访问可用背景区域 */
    *((volatile uint32_t *)0xE000ED10U) |= (1UL << 0);   /* M  = 1 */
    __DSB();
    __ISB();

    /* 5. 通过 PRENR 统一使能区域（若未在 PRLAR.EN 中设置） */
    /* PRENR |= 0x7U; */
}
```

> R52 的系统寄存器访问必须走 `MCR p15, ...` 或 CMSIS 内联函数，不能像 M7 那样直接对内存地址解引用。上面代码中的 `PRBAR(n)` 基址与 `SCTLR` 地址需按 NXP 集成手册确认。

### 3.9 编程规则（ARM 官方要求）

1. 重配某区域时，**编程代码本身不得位于该区域内** —— 否则改权限的瞬间取指就失败，CPU 卡死。
2. 改 `PRBAR`/`PRLAR` 前执行 **DSB**，确保此前所有访存完成。
3. 改完执行 **ISB**，冲刷流水线使新属性生效。

这三条对 M7 同样适用。

---

## 4. S32K5 存储映射与 MPU 布局

### 4.1 关键存储资源

以下均为 **S32K566** 取值，来自 `S32K5xx_memory_map.xlsx`；"窗口"列是架构地址范围，"实际"列是本型号真正实现的部分。

| 资源 | 窗口（起–止） | 最大 | S32K566 实际 | 实际结束 | 属性 | 访问方 |
| --- | --- | --- | --- | --- | --- | --- |
| Code MRAM | `0x0800_0000`–`0x0BFF_FFFF` | 64 MB | **32 MB** | `0x09FF_FFFF` | ECC，cacheable | 全部核 |
| Data MRAM | `0x0C80_0000`–`0x0C83_FFFF` | 256 KB | **256 KB** | `0x0C83_FFFF` | ECC | 全部核 |
| Non-secure OTP | `0x0C40_4000`–`0x0C42_0FFF` | 116 KB | 48 KB | `0x0C40_FFFF` | — | — |
| UTEST | `0x0C8F_E000`–`0x0C90_FFFF` | 72 KB | 40 KB | `0x0C90_7FFF` | — | — |
| M7 SRAM（SRAM0/1/2） | `0x2100_0000`–`0x212F_FFFF` | 3 MB | **3 MB**（3×1 MB） | `0x212F_FFFF` | ECC，含 NC / shareable 分区 | M7 核簇 |
| R52 SRAM（CPE_SRAM0-3） | `0x2200_0000`–`0x220F_FFFF` | 1 MB | **1 MB**（4×256 KB） | `0x220F_FFFF` | ECC | R52 核簇 |
| CPE_LLC0 Scratchpad | `0x0700_0000`–`0x073F_FFFF` | 4 MB | 960 KB | `0x070E_FFFF` | ECC | CPE |
| CPE_LLC1 Scratchpad | `0x0F00_0000`–`0x0F3F_FFFF` | 4 MB | 448 KB | `0x0F06_FFFF` | ECC | CPE |
| LPE_SRAM Code | `0x1000_0000`–`0x100F_FFFF` | 1 MB | 256 KB | `0x1003_FFFF` | ECC | LPE |
| LPE_SRAM Data | `0x2400_0000`–`0x240F_FFFF` | 1 MB | 128 KB | `0x2401_FFFF` | ECC | LPE |
| ITCM（每 M7） | `0x0000_0000`–`0x000F_FFFF` | 1 MB | **32 KB** | `0x0000_7FFF` | ECC，cacheable | M7 |
| DTCM（每 M7） | `0x2000_0000`–`0x200F_FFFF` | 1 MB | **64 KB** | `0x2000_FFFF` | ECC，cacheable | M7 |
| R52 ATCM/BTCM/CTCM（每核） | `0x0100_0000`–`0x016F_FFFF` | 各 1 MB | **各 32 KB** | `0x0160_7FFF` | ECC，零等待 | R52 |
| XSPI/QSPI flash | `0x8100_0000`–`0xDFFF_FFFF` | 1556480 KB | 1024 MB | `0xC0FF_FFFF` | — | 外部 flash |
| 外设桥 | `0x4000_0000`–`0x421F_FFFF` | — | 已用 34 MB | `0x4219_7FFF` | Device | 全部核 |
| PPB | `0xE000_0000`–`0xE00F_FFFF` | 1 MB | **1 MB** | `0xE00F_FFFF` | Device | 核私有 |

**相对早期版本的三处纠正：**

1. **M7 SRAM 在 `0x2100_0000`，不是 `0x2040_0000`。** Rev.A 的 `0x204x_xxxx` 地址来自 NXP S32K Knowledge Base 的 **S32K3** linker 示例，在 S32K5 memory map 中根本不存在。S32K566 有 SRAM0/1/2，各 1 MB，连续位于 `0x2100_0000`–`0x212F_FFFF`。
2. **R52 SRAM（`cpe_sram`）在 `0x2200_0000`–`0x220F_FFFF`**，四个 256 KB bank（CPE_SRAM0-3）——不是 `0x2040_0000`–`0x204F_FFFF`。
3. **S32K5 上没有独立映射的 256 B Standby RAM。** Rev.A 的 256 B 是 S32K3 的。S32K5 上 LPE 在 Standby 模式保持 384 KB `LPE_SRAM`，memory map 中没有专用 256 B standby 窗口。因此"Standby RAM 必须 non-cacheable"这条硬约束**不能按原样套用**——依赖前需对照 LPE Overview 章节核实。

> **ITCM / LPE_SRAM 地址冲突（S32K5 特有，极易漏看）**：`ITCM_0..3` 与 `Code LPE_SRAM Alias` **都起始于 `0x0000_0000`** 并共用同一 1 MB 窗口，仅实现容量不同（32 KB vs 256 KB）。MPU 无法按地址区分二者——区别在于*哪个核在取指*。任何覆盖 `0x0000_0000` 的 region 同时是"M7 ITCM"和"LPE SRAM alias"。
> `[来源: memory_map.xlsx, Overview Memory Map ITCM_0..3 / Code LPE_SRAM Alias 行]`

S32K5 已在硬件层面把 SRAM 切分为 cacheable / non-cacheable / shareable 段（linker 里体现为 `int_sram_no_cacheable`、`int_sram_shareable`），MPU 配置必须与这套划分**严格对齐**，否则软件属性与硬件属性冲突会导致不可预测行为。

### 4.2 推荐的 M7 区域布局（16 区域预算）

M7 实现 **16 个区域**（`MPU_TYPE` 复位值 `0x00001000`）。`[来源: rm1131130 Rev.3, Chapter_02 Table 10]`

| # | 区域 | BASE | LIMIT | 大小 | 属性 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | ITCM（本核） | `0x0000_0000` | `0x0000_7FFF` | 32 KB | RWX, NC | 向量表 + 热点 ISR。**与 LPE_SRAM alias 共用 1 MB 窗口，见 4.1** |
| 1 | Code MRAM | `0x0800_0000` | `0x09FF_FFFF` | 32 MB | RWX, WB | FOTA 需 RW；不可变性靠 XRDC |
| 2 | Data MRAM | `0x0C80_0000` | `0x0C83_FFFF` | 256 KB | RW, WB, XN | |
| 3 | DTCM（本核） | `0x2000_0000` | `0x2000_FFFF` | 64 KB | RW, NC, XN | 主栈；读前需 64-bit 写初始化做 ECC |
| 4 | SRAM0 | `0x2100_0000` | `0x210F_FFFF` | 1 MB | RW, WB, XN | .data/.bss/堆 |
| 5 | SRAM1 | `0x2110_0000` | `0x211F_FFFF` | 1 MB | RW, WB, XN | |
| 6 | SRAM2 | `0x2120_0000` | `0x212F_FFFF` | 1 MB | RW, WB, XN | NC / shareable 子分区在此 |
| 7 | LPE_SRAM Code | `0x1000_0000` | `0x1003_FFFF` | 256 KB | R, NC, XN | M7 侧只读视图 |
| 8 | PERI_LO | `0x4000_0000` | `0x403F_FFFF` | 4 MB | RO/RW, **Device**, XN | PBRIDGE3_0/1 |
| 9 | PERI_MID | `0x4040_0000` | `0x40BF_FFFF` | 8 MB | RO/RW, **Device**, XN | PBRIDGE3_2–5；含 XRDC/MSCM/ERM/EIM |
| 10 | PERI_CPE_LPE | `0x4100_0000` | `0x421F_FFFF` | 18 MB | RO/RW, **Device**, XN | CPE + LPE + DSP 桥 |
| 11 | XSPI 数据窗口 | `0x8100_0000` | `0xC0FF_FFFF` | 1024 MB | RO, NC, XN | 外部 QSPI / HyperRAM |
| 12 | XSPI 寄存器窗口 | `0x40BA_4000` | `0x40BA_BFFF` | 2 KB | RO, **Device**, XN | 控制器寄存器；**与数据窗口分开建区** |
| 13 | PPB | `0xE000_0000` | `0xE00F_FFFF` | 1 MB | RO, Device, XN | 本核私有，单独建区 |
| 14–15 | 任务栈守护 | 按链接脚本 | — | 32 KB | RO / XN | 小栈 + 数据分离 |

> **Device 属性是强制的，不是建议。** RM Ch.11 §11.3.5 NOTE：REG_PROT 的 transfer error 只有在"通过其 MPU 或 MMU 定义了覆盖目标寄存器地址的 **strongly ordered 内存区域**"的 CPU 上才可观测。把外设窗口配成 Normal memory，REG_PROT 的拒绝会退化成异步总线错误，出错点离原因很远。详见 §5.7。

### 4.3 推荐的 R52 区域布局（20 区域预算）

S32K566 实现 **EL1: 20 区域，EL2: 20 区域**（不是 16 或 24）。`[来源: rm1131130 Rev.3, Chapter_02 Table 6 / Table 10]`

| # | 区域 | BASE | LIMIT | Attr | XN | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | ATCM_CPU0 | `0x0100_0000` | `0x0100_7FFF` | Normal WB-WA | **0** | 必须在使能 MPU **之前**配置（见 3.9） |
| 1 | BTCM_CPU0 | `0x0110_0000` | `0x0110_7FFF` | Normal WB-WA | 1 | |
| 2 | CTCM_CPU0 | `0x0120_0000` | `0x0120_7FFF` | Normal WB-WA | 1 | |
| 3 | CPE_LLC0 | `0x0700_0000` | `0x070E_FFFF` | Normal WB-WA | 1 | |
| 4 | Code MRAM | `0x0800_0000` | `0x09FF_FFFF` | Normal WT, RO | **0** | 属性必须与 M7 侧逐字段一致 |
| 5 | Data MRAM | `0x0C80_0000` | `0x0C83_FFFF` | Normal WB-WA | 1 | |
| 6 | CPE_LLC1 | `0x0F00_0000` | `0x0F06_FFFF` | Normal WB-WA | 1 | |
| 7 | LPE_SRAM Code | `0x1000_0000` | `0x1003_FFFF` | Normal WT, RO | **0** | |
| 8 | SysSRAM 0-2 | `0x2100_0000` | `0x212F_FFFF` | Normal WB-WA | 1 | |
| 9 | CPE_SRAM 0-3 | `0x2200_0000` | `0x220F_FFFF` | Normal WB-WA | 1 | `cpe_sram` |
| 10 | LPE_SRAM Data | `0x2400_0000` | `0x2401_FFFF` | Normal WB-WA | 1 | |
| 11 | PERI_LO | `0x4000_0000` | `0x403F_FFFF` | Device-nGnRE | 1 | |
| 12 | PERI_MID | `0x4040_0000` | `0x40BF_FFFF` | Device-nGnRE | 1 | |
| 13 | PERI_CPE_LPE | `0x4100_0000` | `0x421F_FFFF` | Device-nGnRE | 1 | |
| 14 | PPB | `0xE000_0000` | `0xE00F_FFFF` | Device-nGnRnE | 1 | **仅 EL1 的 AP** |
| 15 | XSPI virtual | `0x8100_0000` | `0xC0FF_FFFF` | Normal WT, RO | **0** | |
| 16–19 | 任务级成对区域（代码 RO+XN=0 / 数据 RW+XN=1） | — | — | — | — | 预留 4 个给动态切换 |

> R52 **禁止区域重叠**是设计中最硬的约束（见 3.3）。上表用掉 **16/20** 个区域，已做两两不重叠与 64 字节对齐校验，留 4 个给 OS 任务切换——RM 对 MPU 用途的描述正是"dynamic task protection"。
>
> **CPU1 仅 TCM 基址不同**：CPU1 的 ATCM/BTCM/CTCM 是 `0x0140_0000` / `0x0150_0000` / `0x0160_0000`。CPU1 不需要为 CPU0 的 TCM 建区。
>
> **外设上界是 `0x421F_FFFF`，不是 `0xE00F_FFFF`。** Rev.A 的 `0xE00FFFFF` 取自 Zephyr S32K566 R52 移植，是个保守占位值；真实 memory map 显示最后一个外设桥（LPE_PBRIDGE3）结束于 `0x4219_7FFF`，另有 DSP_PBRIDGE3 在 `0x4260_0000`–`0x427F_FFFF`、CPE_GIC0 在 `0x4300_0000`–`0x431F_FFFF`。需明确决定 DSP 与 GIC 是归入 Device 区域还是单独建区。

### 4.4 核间共享区的特殊处理

R52 与 M7 交换数据（如 CAN 报文、时间戳）的区域是跨核共享的，必须**双方一致地配置为 shareable + cacheable**，并配合以下手段：

| 手段 | 说明 |
| --- | --- |
| Non-shareable cacheable | 若数据量小且延迟敏感，让其中一个核配成 Non-shareable 避免 cache 一致性开销 |
| 内核 lockstep / atomic | 用 `ldrex`/`strex` 保证读改写原子性 |
| Mailbox / MU | S32K5 的 MU（Messaging Unit）寄存器用于核间同步与中断通知 |
| Cache 维护 | 跨核可见性依赖硬件一致性；S32K5 的核间不共享 L1 cache，需靠内存属性 + 屏障 |

---

## 5. 按存储类型的 MPU 配置详解（MRAM / SRAM / TCM / XSPI / 外设）

本节把第 4 章的布局表展开到**每一种存储类型**。MPU 属性不是"拍脑袋选 Normal WB"，而是由存储介质的物理特性决定的 —— 选错属性不会报错，只会让功能悄悄坏掉。

### 5.1 S32K5 存储类型全景

| 存储类型 | 地址范围 | 容量（S32K566） | ECC | 易失性 | 建议 MPU 属性 | 可达核 |
| --- | --- | --- | --- | --- | --- | --- |
| Code MRAM (eMRAM) | `0x0800_0000`–`0x09FF_FFFF` | **32 MB** | 有 | 非易失 | Normal WB RA，RWX | 全部核 |
| Data MRAM | `0x0C80_0000`–`0x0C83_FFFF` | 256 KB | 有 | 非易失 | Normal WB RA，RW，XN | 全部核 |
| M7 SRAM0 | `0x2100_0000`–`0x210F_FFFF` | 1 MB | 有 | 易失 | Normal WB RA，RW | M7 核簇 |
| M7 SRAM1 | `0x2110_0000`–`0x211F_FFFF` | 1 MB | 有 | 易失 | Normal WB RA，RW | M7 核簇 |
| M7 SRAM2 | `0x2120_0000`–`0x212F_FFFF` | 1 MB | 有 | 易失 | Normal WB RA，RW | M7 核簇 |
| R52 SRAM（CPE_SRAM0-3） | `0x2200_0000`–`0x220F_FFFF` | 1 MB（4×256 KB） | 有 | 易失 | Normal WB RA，RW | R52 核簇 |
| CPE_LLC0 / LLC1 scratchpad | `0x0700_0000` / `0x0F00_0000` | 960 KB / 448 KB | 有 | 易失 | Normal WB-WA | CPE |
| LPE_SRAM Code | `0x1000_0000`–`0x1003_FFFF` | 256 KB | 有 | 易失 | Normal NC / WT，RO | LPE（及其他） |
| LPE_SRAM Data | `0x2400_0000`–`0x2401_FFFF` | 128 KB | 有 | 易失 | Normal WB-WA | LPE（及其他） |
| ITCM（每 M7） | `0x0000_0000`–`0x0000_7FFF` | 32 KB | 有 | 易失 | Normal NC / Device，RWX | M7 |
| DTCM（每 M7） | `0x2000_0000`–`0x2000_FFFF` | 64 KB | 有 | 易失 | Normal NC / Device，RW | M7 |
| R52 ATCM/BTCM/CTCM | `0x0100_0000`–`0x0160_7FFF` | 各 32 KB | 有 | 易失 | Normal WB-WA | R52 |
| XSPI/QSPI 外部 flash | `0x8100_0000`–`0xC0FF_FFFF` | 1024 MB | 依器件 | 非易失 | Device 或 Normal NC，RO | 全部核 |
| 外设窗口 | `0x4000_0000`–`0x421F_FFFF` | 已用 34 MB | — | — | **Device-nGnRnE**，XN | 全部核 |
| PPB（私有外设总线） | `0xE000_0000`–`0xE00F_FFFF` | 1 MB | — | — | Device-nGnRnE | 本核私有 |

> **外设窗口上界，已纠正。** Rev.A 用 `0xE00FFFFF`（取自 Zephyr R52 移植）并提醒不要用 `0xFFFFFFFF`。Rev.3 memory map 显示真实最后一个外设在 `0x4219_7FFF`。准确的表述是：**外设占据 `0x4000_0000`–`0x431F_FFFF`**（含 DSP_PBRIDGE3 `0x4260_0000`、CPE_GIC0 `0x4300_0000`），`0xE000_0000` 以上是 PPB 加厂商空间。Device region 的边界取 `0x431F_FFFF` 还是延伸到 `0xDFFF_FFFF` 是个设计选择——延伸更简单，但会失去"对误入未映射空间的访问报错"的能力。

### 5.2 Code MRAM（eMRAM）—— S32K5 最大的架构变化

#### 硬件特性

S32K5 是业界首款 16 nm FinFET + 嵌入式 MRAM 的车规 MCU。与 S32K3 及更早的 eFlash 相比，MRAM 改变了几条底层假设：

| 特性 | MRAM (S32K5) | eFlash (S32K3 及更早) |
| --- | --- | --- |
| 寻址方式 | **字节寻址**，可直接读改写 | 需整页/整块操作 |
| 写前擦除 | **不需要** | 必须先擦除 |
| 写入速度 | 8.8–15 MB/s（各方口径不一） | eFlash 的 1/10–1/15 |
| 耐久 | 约 100 万次写 | 约 1 万–10 万次擦写 |
| 保持期 | 口径冲突，见下 | 通常 20 年 |

> **保持期数据冲突（待 RM 确认）**：NXP–TSMC 的 16 nm MRAM 技术公告称 20 年 @150 °C；另有中文资料称 S32K5 MRAM 数据保持期为 10 年 @85 °C，低于 eFlash。两者差异巨大，**必须查 S32K5xx RM 的 MRAM 章节**，这直接影响日志类数据的落盘策略。

#### MPU 配置含义

1. **代码区可读可写可执行** —— MRAM 不需要 XIP 只读保护，支持 FOTA 的 A/B 双镜像原地切换。但这也意味着**代码区能被自身数据覆盖**。ASIL D 场景下若要求"运行期代码不可变"，MPU 做不到（AP 最低只能 RO，而 RO 对特权代码无效），必须靠 **XRDC 的只读锁定**实现。
2. **两核共用同一块 MRAM** —— M7 与 R52 默认都从 Code MRAM 取指执行（Zephyr 中两者都以 `cmram` 作为 `zephyr,flash`）。同一物理区被两个核的 MPU 分别配置，**属性必须逐字段一致**，否则一个核看到的是 cacheable，另一个看到的是 non-cacheable，跨核函数指针跳转会出现不可预测行为。
3. **FOTA 写入期间应关闭 cache** —— MRAM 写入虽快，但写入过程中若目标代码段正在被 cache 或流水线持有，需要 clean + invalidate。建议 FOTA 驱动在刷写前后统一做 cache 维护。
4. **不要把 MRAM 配成 Device 类型** —— 性能会崩塌（MRAM 就是当 RAM 用的），且 MRAM 支持 cache。

### 5.3 M7 SRAM（3 MB，三个 bank）

S32K566 向 M7 核簇暴露三个 1 MB SRAM bank，连续位于 `0x2100_0000`–`0x212F_FFFF`。下表是 Rev.A 的分区表（保留备查），**这些地址在 S32K5 上不存在，不得使用**。

| Bank | 地址范围 | 大小 | 建议用途 | MPU 属性 |
| --- | --- | --- | --- | --- |
| SRAM0 | `0x2100_0000`–`0x210F_FFFF` | 1 MB | .data/.bss/堆、主工作集 | Normal WB RA |
| SRAM1 | `0x2110_0000`–`0x211F_FFFF` | 1 MB | 次级数据、跨核缓冲 | Normal WB RA 或 NC |
| SRAM2 | `0x2120_0000`–`0x212F_FFFF` | 1 MB | non-cacheable / shareable 分区 | **Normal NC** / WB + Shareable |

> **Rev.A 内容，现已废弃** —— "Standby RAM `0x2040_0000` / `int_sram_fls_rsv` `0x2040_7F00` / `int_sram_no_cacheable` `0x2040_8000` / `int_sram_shareable` `0x2041_0000`"这套分区表取自 NXP S32K Knowledge Base 的 **S32K3** linker 示例。"四类属性分区"的*结构*仍是有用的心智模型，但边界必须取自 S32K5 的 linker 脚本，而不是那些地址。
>
> **Standby RAM 硬约束不延续。** Rev.A 引用 NXP：*"CM7 CPU D-Cache MUST be disabled to use the Standby RAM area. Or set the standby RAM as non-cacheable in MPU configuration."* 该约束是 S32K3 特有的 —— S32K5 memory map 中没有 256 B standby 窗口。S32K5 上对应的关注点是 **Standby 模式下保持的 384 KB `LPE_SRAM`**，位于 `0x1000_0000`（code）与 `0x2400_0000`（data），由 M4 配置而非 M7。

**Zephyr 对应关系**：M7 板级目标用 `sram0` 作为 `zephyr,sram`，R52 目标用 `cpe_sram`。两套 DTS 走的是不同的 SRAM，**不是同一块内存的两种名字**。具体到 S32K5：M7 → `0x2100_0000`，R52 → `0x2200_0000`。

### 5.4 R52 SRAM（cpe_sram，1 MB）

| 项 | 内容 |
| --- | --- |
| 归属 | R52 cluster 私有 |
| 地址 | **`0x2200_0000`–`0x220F_FFFF`**（四个 bank：CPE_SRAM0-3，各 256 KB） |
| 大小 | 1 MB，带 ECC（SECDED） |
| Zephyr 节点名 | `cpe_sram` |

**关键风险**：R52 SRAM 虽然"归属 R52 核簇"，但物理上对片上其他 master（M7、eDMA、以太网 MAC 等）是可见的。MPU 只约束**本核**的访问，**挡不住 M7 或 DMA 从总线侧闯入**。要真正隔离必须配 **XRDC** —— 具体是 `CPE_MRC0`–`CPE_MRC3`，每个 CPE_SRAMCTL bank 对应一个 MRC，各 16 个 region descriptor。

**MPU 属性**：Normal WB RA，RW，XN=1（数据区不可执行）。R52 SRAM 是 R52 侧栈与任务数据的所在地，建议按任务再细分（见 4.3）。

### 5.5 TCM（ITCM / DTCM / ATCM / BTCM / CTCM）—— ECC 与 backdoor 是两个坑

#### 硬件特性

| 项 | 说明 |
| --- | --- |
| 固定基址 | M7 ITCM `0x0000_0000`、DTCM `0x2000_0000`；R52 ATCM/BTCM/CTCM `0x0100/0110/0120_0000`（CPU0）、`0x0140/0150/0160_0000`（CPU1） |
| M7 大小（S32K566） | ITCM 32 KB、DTCM 64 KB（Rev.A 的"60 KB + 4 KB 栈"是 S32K3 的值） |
| R52 大小 | ATCM/BTCM/CTCM 各 32 KB，零等待 |
| M7 DTCM 接口 | 双接口 D0TCM / D1TCM |
| 使能 | `ITCMCR.EN` / `DTCMCR.EN` 软件可关 |

#### ECC 初始化约束（极易踩坑）

**读 TCM 或系统 RAM 之前，必须先做 64-bit 写初始化**，否则 ECC 会报错。NXP S32K 文档原文：*"为了防止 ECC 报错，在读操作前，TCM 和系统 RAM 都需要 64bit 写入初始化。"*

这意味着 MPU 配置**不能**放在 TCM 初始化之前去读 TCM 内容 —— 启动代码必须先填 ECC 再建区域。且 RAM ECC 初始化**只在 Power-On Reset 时做**，其他复位类型不能重复做（会破坏 retained 数据）。

#### TCM backdoor：核 MPU 保护的结构性漏洞

这是 Rev.B 新增的最重要 S32K5 特有发现，Rev.A 完全没有覆盖。

> Arm Cortex-M7 TRM：*"**AHBS interface transactions are not capable of performing MPU lookups.** No distinction is made internally between unprivileged and privileged AHBS interface accesses as indicated on HPROTS. **The system is entirely responsible for providing TCM protection functionality for AHBS interface accesses** as required."*

后果：**任何主控经 `AXBS_TCM` 访问 TCM 时，完全绕过该核的 MPU。** RM Rev.3 Chapter_02 Table 11/12 明确列出了哪些 initiator 对哪些 TCM 有 backdoor 访问权 —— 名单包括*其他 M7 核、两个 R52 核、M4、DSP-V、Neutron、LPE_eDMA3 和 eDMA5*。在 S32K5 上，TCM 不是私有内存；它对抗其他主控的**唯一**保护是 XRDC。

| 路径 | 由谁保护 |
| --- | --- |
| 拥有核 → 自己的 TCM | 核 MPU（M7：16 region；R52：EL1/EL2） |
| 其他主控 → TCM（经 `AXBS_TCM`） | **仅 XRDC** —— `MRC_B3` 管 M7_0-3 TCM backdoor，`CPE_MRC4` 管 R52 Cluster 0 TCM，`LPE_MRC0` 管 M4 TCM backdoor |

> **设计规则：每个 TCM 必须同时在拥有核的 MPU 和对应的 XRDC MRC 中配置。** 只配 MPU 等于把 backdoor 敞开 —— 而且 backdoor 地址（ITCM `0x1100_0000`–`0x116F_FFFF`，DTCM `0x2300_0000`–`0x236F_FFFF`）是与 TCM 自身基址不同的窗口，需要独立的 XRDC region。

#### 多核共享 TCM（S32K5 特有）

Arm/NXP 规定：多核器件上，所有已使能的核与非核 master **都可以使用未启用核的 TCM 作为系统内存**。启用核要把禁用核的 TCM 当普通 RAM 用，需按步骤执行：

1. 使能该 M7 核的 TCM 控制时钟
2. 该 M7 核进入等待模式
3. 使能该 M7 核的时钟

**MPU 含义**：TCM 的归属是动态的 —— 哪个核启用了，TCM 就归谁；核被禁用后，它的 TCM 变成公共 RAM。因此 TCM 区域的 MPU 配置不能静态写死，需要随核的使能状态调整，或者干脆用 XRDC 按 domain 管。

#### MPU 属性

TCM 接口本身**不可 cache**（Tightly-Coupled Memory 的延迟已经是单周期级别，cache 无意义）。所以：

| 区域 | 建议属性 | 说明 |
| --- | --- | --- |
| ITCM | Normal NC，RWX | 向量表 + 热点 ISR，可执行 |
| DTCM 数据 | Normal NC，RW，XN | 栈与核心数据 |
| R52 ATCM | Normal WB-WA，**XN=0** | 必须保持可执行 —— 见下文的 WXN 冲突 |

配成 Normal cacheable 不会报错，但 cache 对该区间无效，属性形同虚设 —— 属"无害但无意义"，评审时仍应写对。

#### ⚠️ ATCM 与 WXN 的冲突（Rev.B 新增）

`SCTLR.WXN` 复位为 **0**，TRM 原文写得很明确：*"0 = EL1-controlled MPU regions with write permission are not forced to be XN, **this is the reset value**."*

显而易见的缓解办法 —— 全局置 `WXN=1` 强制 write-xor-execute —— **会破坏 ATCM**，因为 ATCM 是可读写且必须可执行的 region（向量表、启动代码）。`WXN=1` 时 ATCM 被强制 XN，核无法从它启动。

两条出路，各有代价：

| 方案 | 代价 |
| --- | --- |
| **不置全局 `WXN`**，逐 region 置 `XN`（代码区 `XN=0`，所有数据区 `XN=1`） | 失去全局兜底。某个代码区漏置 `XN=1`、或某个数据区误置 `XN=0`，都是静默的。必须靠上电自检读回每个 `PRBAR.XN` 来覆盖。 |
| 置 `WXN=1`，把向量表/启动代码搬出 ATCM 到 MRAM | ATCM 变成纯数据区，失去零等待状态对最热代码的收益。 |

另需注意 `SCTLR.UWXN`（bit 20，"unprivileged write permission implies EL1 XN"）**同样复位为 0** —— 只置 `WXN` 的话，非特权可写区域仍然是可执行的。

### 5.6 XSPI / QSPI 外部存储

| 项 | 内容 |
| --- | --- |
| XSPI 基址 | `0x8100_0000` |
| 板级器件 | IS66WVH8M8DAL HyperRAM 512 Mbit（S32K5XXCVB） |
| 用途 | 扩展 RAM / 外部 flash / A/B 镜像副本 |

**MPU 属性**：

| 用途 | 属性 | 说明 |
| --- | --- | --- |
| 外部 flash 执行 | Normal NC 或 Device，RO，XN=0 | 不建议配 cacheable：XSPI 走外部总线，cache 一致性由外部器件保证，风险高 |
| HyperRAM 数据 | Normal NC，RW，XN=1 | 高带宽，延迟敏感 |
| XSPI 寄存器窗口 | Device-nGnRnE，RO，XN=1 | 控制器寄存器 |

**陷阱**：XSPI 的**寄存器窗口**与**数据窗口**必须分成两个 MPU 区域。把寄存器窗口配成 Normal cacheable 是最典型的 XSPI 配置错误 —— 与片上外设同理。另外 MRAM 编程走 XSPI 时有特殊处理要求（SEGGER 文档特别标注 *"QSPI flash programming requires special handling compared to internal flash"*）。

### 5.7 外设窗口

| 项 | 内容 |
| --- | --- |
| 起始 | `0x4000_0000` |
| 桥 | PBRIDGE3_0–5（`0x4000_0000`–`0x40BF_FFFF`）、CPE_PBRIDGE3_0/1（`0x4100_0000`–`0x411F_FFFF`）、LPE_PBRIDGE3（`0x4200_0000`–`0x421F_FFFF`）、DSP_PBRIDGE3（`0x4260_0000`–`0x427F_FFFF`）、CPE_GIC0（`0x4300_0000`–`0x431F_FFFF`） |
| 最后一个已映射外设 | `0x4219_7FFF` |
| Alias 窗口 | PBRIDGE3_0 alias 在 `0x5000_0000`–`0x501F_FFFF`（= 基址 **+ `0x1000_0000`**） |
| 属性 | **Device-nGnRE**（R52）/ **Device-nGnRnE**（M7） |
| XN | 1（不可执行） |

**桥的槽位几何**（决定 region 粒度）：每个 PBRIDGE3 占 2 MB，划分为 128 个 4 / 16 / 64 KB 槽。Rev.3 memory map 显示 486 行中有 479 个已映射外设，槽大小为 16 KB（384 个）、32 KB（91 个）、64 KB（11 个）。**合并 ≤ 64 KB 的间隙可把 34 MB 外设空间折叠成 11 个连续段** —— 这正是 §4.2/§4.3 能用 3 个 PERI region 覆盖全部外设的原因。

**必须单独建区的两块**：

1. **PPB / 系统控制空间** `0xE000_0000`–`0xE00F_FFFF`（1 MB）—— M7 的 `MPU_TYPE`/`MPU_CTRL` 等就在 `0xE000_ED9x`。PPB 是**本核私有**的，M7 与 R52 看到的内容完全不同。不要把 PPB 与外设窗口合在一个大区里配成 Device，否则调试器访问与系统寄存器的可见性会变得难以推理。
2. **厂商自定义空间** `0xE010_0000` 以上，按 RM 划分。

**Secure / non-secure alias（Rev.B 新增）**：memory map 只为 PBRIDGE3_0 给出了明确的 alias 窗口，地址正好是 **基址 + `0x1000_0000`**（`0x4000_0000` → `0x5000_0000`）。其余 435 个已映射外设**没有** alias。结合 RM §36.2/§36.3 的表述 —— "表中内存槽代表的是 **non-secure 地址区**" —— 符合实际的解读是：表中地址即 non-secure 视图，而 secure 视图的基址规则**无法由该附件完全确定**。`+0x1000_0000` 规则仅对 PBRIDGE3_0 确认，推广前需核实。

### 5.8 XRDC：MPU 的互补层，必须一起设计

这是 S32K5 与 S32K3 设计上最大的差别，也是**只做 MPU 设计会漏掉的一整层**。

#### NXP 的两级隔离模型

NXP 官方明确表述：*"通过 XRDC 和 MPU，可以实现 2 级隔离层级"*：

| 层级 | 机制 | 隔离对象 |
| --- | --- | --- |
| 核心级 | **XRDC** | 核与核之间、核与外设之间 |
| 任务级 | **MPU** | 同一核内的任务之间 |

也就是说：**MPU 管"一个核内部谁是谁"，XRDC 管"哪个 master 能碰哪个 slave"**。两者职责不重叠，缺一不可。

#### XRDC 子模块

| 子模块 | 职责 |
| --- | --- |
| `XRDC_MGR` | Manager，协调所有编程模型的读写 |
| `XRDC_MDAC` | Master Domain Assignment Controller，给每个 master 分配 domain ID |
| `XRDC_MRC` | Memory Region Controller，按 region descriptor 管内存访问 |
| `XRDC_PAC` | Peripheral Access Controller，按 domain access control 管外设访问 |

#### S32K566 XRDC 实例与 MRC 目标（Rev.B 新增）

五个 XRDC 实例：`XRDC_A`、`XRDC_B`、`XRDC_C`、`CPE_XRDC`、`LPE_XRDC`。**16 个 Domain ID**；每实例 **768 个 PDAC slot（0–767）**。`[来源: rm1131130 Rev.3, Chapter_31 §31.1.1–31.1.5]`

| MRC | # descriptor | 保护目标 |
| --- | --- | --- |
| `MRC_B0` | 16 | AXI MRAM Controller P1（Code MRAM） |
| `MRC_B1` / `B2` / `B6` | 各 16 | AXI RAM Controller 0/1/2（SysSRAM） |
| **`MRC_B3`** | 16 | **Cortex-M7_0-3 TCM backdoor** |
| `MRC_B5` | 16 | AXI MRAM Controller P2（Data MRAM） |
| **`CPE_MRC4`** | 16 | **R52 Cluster 0 TCM** |
| `CPE_MRC0`–`MRC3` | 各 16 | `CPE_SRAMCTL_0/1/2/3` |
| `CPE_MRC5` / `M6` | 各 16 | `CPE_LLC_0` / `CPE_LLC_1` |
| **`LPE_MRC0`** | 16 | **LPE Cortex-M4 TCM Backdoor** |
| `MRC_A0` | 16 | NETC Base AXI32 |
| `MRC_A2` | 8 | NETC IEPRC ECAM |
| `MRC_B4` | 8 | XSPI Controller |
| `MRC_B7` | 4 | Neutron64S AXI64 |
| `MRC_B8` | 16 | AMRAMC IPS0 |
| `MRC_C0` | 4 | DSP-V AHB32 |
| `MRC_A1` / `A3` | 各 4 | CANXL_0 / CANXL_1 |

**PAC ↔ 桥映射**：`PAC_A0-1`→PBRIDGE3_0（slot 0–127）、`PAC_C0-2`→PBRIDGE3_1（128–255）、`PAC_B0-2`→PBRIDGE3_2（256–383）、`PAC_C3-4`→PBRIDGE3_3（384–511）、`PAC_C5-6`→PBRIDGE3_4（512–639）、`PAC_B3-5`→PBRIDGE3_5（640–767）、`CPE_PAC0-1`→CPE_PBRIDGE3_0、`CPE_PAC2-3`→CPE_PBRIDGE3_1、`LPE_PAC0-2`→LPE_PBRIDGE3。完整的 slot↔外设对照表见 memory map 附件的 "Peripherals Memory Map" tab。

#### ⚠️ XRDC 没有 execute-never 属性（Rev.B 新增）

`DdACP` 权限字段只编码**读/写**，分四级（secure-privileged、secure-user、nonsecure-privileged、nonsecure-user）。**没有 XN 位。**

> **后果：所有代码可执行性控制都在核 MPU 里。** XRDC 能让某 region 对某域只读，但不能让它不可执行。任何"这段内存绝不能当代码跑"的要求，必须靠每个能从这里取指的核上的 `PRBAR.XN` / `MPU_RASR.XN` 来落实 —— 而且按 §5.5，这包括经 backdoor 触达它的那些核。

#### 启用顺序：XRDC 会把自己锁死

> "When XRDC is enabled (`CR[GVLD]` = 1), you **cannot access any XRDC-protected memory unless** you configure at least one set of memory region descriptors that includes the targeted memory." `[来源: Chapter_31 §31.5.6.5]`

**必须在置 `GVLD=1` 之前配完所有 MRGD/PAC descriptor 并自检。** 先启用后配置，可能把自己锁在 XRDC 寄存器之外。

#### 与 MPU 的关键差异

| 维度 | MPU | XRDC |
| --- | --- | --- |
| 约束对象 | **本核**的取指与数据访问 | **所有 master**（核 + eDMA + MAC + ...） |
| 能否挡住 DMA | **不能** | **能** |
| 能否禁执行 | **能**（XN） | **不能**（无 XN 属性） |
| 配置粒度 | 每核一套 | 全片一套 |
| 违规异常 | M7: MemManage；R52: Permission/Translation fault | **Bus Fault** |
| 是否随上下文切换 | 是（OS 按任务切换） | 否（按 domain ID 静态绑定） |

**最关键的结论：MPU 挡不住 DMA。** eDMA、以太网 MAC、CAN 等 master 绕过 CPU 的 MPU 直接访问总线。若安全设计只做 MPU，一个配置错误的 DMA 描述符就能写穿任意内存 —— 包括 R52 的栈和 M7 的故障记录区。这类越权必须用 XRDC 的 MRC/PAC 拦。

#### 域间共享与 SEMA42

XRDC 支持把某块内存/外设设为多域共享，并用 **SEMA42 硬件信号量**做互斥。NXP AN14715 给出的典型流程：

1. Domain0 锁定 SEMA42 通道，初始化共享外设，**不释放**信号量
2. Domain1 尝试写该外设 → **触发 Bus Fault**
3. Fault handler 记录出错地址，调 `Xrdc_Ip_GetDomainIDErrorStatus()` 读 XRDC 错误状态

**异常处理含义**：XRDC 违规产生的是 **Bus Fault**，与 MPU 的 MemManage/Abort 是**不同的异常入口**。故障处理代码必须分别实现两个 handler，且 XRDC 的错误状态要用专用 API 读，不能从 `SCB->CFSR` 里找。

#### MCUXpresso SDK 支持

MCUXpresso SDK 提供 `XRDC_Init`、domain assignment（`xrdc_processor_domain_assignment_t`）、memory access policy（`xrdc_mem_access_config_t`）、peripheral access policy（`xrdc_periph_access_config_t`）等 API。AUTOSAR 路径下对应 `Xrdc_Ip` 驱动。

### 5.9 按存储类型的 MPU 配置速查

| 存储类型 | M7 属性 | R52 属性 | XN | 特别注意事项 |
| --- | --- | --- | --- | --- |
| Code MRAM `0x0800_0000`–`0x09FF_FFFF` | Normal WB RA | Normal WB RA（MAIR0=0xFF） | 0 | 两核属性必须逐字段一致；代码区不可变需 XRDC（XRDC 无 XN） |
| Data MRAM `0x0C80_0000`–`0x0C83_FFFF` | Normal WB RA | Normal WB RA | 1 | |
| M7 SRAM0-2 `0x2100_0000`–`0x212F_FFFF` | Normal WB RA | — | 1 | 栈/堆/.data；NC 与 shareable 子分区在这些 bank 内 |
| R52 SRAM `0x2200_0000`–`0x220F_FFFF` | — | Normal WB RA | 1 | 防其他 master 需 XRDC（`CPE_MRC0`–`MRC3`） |
| CPE_LLC0/1 scratchpad | — | Normal WB-WA | 1 | `0x0700_0000`（960 KB）/ `0x0F00_0000`（448 KB） |
| LPE_SRAM `0x1000_0000` / `0x2400_0000` | Normal NC / WB | Normal NC / WB | 1 | 256 KB code + 128 KB data；Standby 模式保持 |
| ITCM `0x0000_0000`（32 KB） | Normal NC | — | 0 | **与 LPE_SRAM alias 共用 1 MB 窗口**；读前必须 64-bit 写初始化 ECC |
| DTCM `0x2000_0000`（64 KB） | Normal NC | — | 1 | backdoor 在 `0x2300_0000`–`0x236F_FFFF`，需 XRDC `MRC_B3` |
| R52 ATCM/BTCM/CTCM | — | Normal WB-WA | ATCM=0，其余=1 | backdoor 需 XRDC `CPE_MRC4`；ATCM 必须可执行（WXN 冲突，见 §5.5） |
| XSPI 数据 `0x8100_0000`–`0xC0FF_FFFF` | Device 或 Normal NC | Device 或 Normal NC | 0 | |
| XSPI 寄存器 `0x40BA_4000` | **Device-nGnRnE** | Device-nGnRE | 1 | **与数据窗口分开建区** |
| 外设 `0x4000_0000`–`0x421F_FFFF` | Device-nGnRnE | Device-nGnRE | 1 | 真实最后外设 `0x4219_7FFF`；DSP 桥与 GIC 延伸到 `0x431F_FFFF` |
| PPB `0xE000_0000`–`0xE00F_FFFF` | Device-nGnRnE | Device-nGnRnE | 1 | 本核私有，单独建区 |

---

---

## 6. Cache 一致性：MPU 属性与 Cache 的耦合

这是 MPU 设计中最容易被低估的部分。

### 5.1 R52 与 M7 的 Cache 架构

| 项 | Cortex-M7 | Cortex-R52 |
| --- | --- | --- |
| L1 I-Cache | 4–64 KB，独立配置 | 0–32 KB |
| L1 D-Cache | 4–64 KB，独立配置 | 0–32 KB |
| TCM | 指令/数据各 0–1 MB | 最多 3 个 TCM，各至 1 MB |
| Bus | AXI4 128-bit | AXI4 128-bit（AXIM / Flash / LLPP 独立端口） |
| ECC | Cache、TCM、总线全支持 | 同左 |

S32K5 的 M7 与 R52 **各自独立**，没有共享 L2 cache。这意味着跨核共享数据不能依赖 cache 一致性协议自动同步。

### 5.2 属性配置规则

| 存储 | 正确属性 | 错误属性的后果 |
| --- | --- | --- |
| 外设寄存器 | Device-nGnRnE | 配成 Normal cacheable → 读到旧值、写被吞 |
| MRAM / SRAM | Normal, WT 或 WB + RA | 配成 Device → 性能崩塌但正确 |
| Standby RAM | **Normal Non-cacheable** | cacheable → 进入低功耗后数据丢失 |
| ITCM / DTCM | Normal WT WB | TC 接口本身不可 cache，配错无害但无意义 |
| 跨核共享 SRAM | Normal WB + Shareable | 属性不一致 → 数据永久不一致 |

### 5.3 Cache 维护序列

MPU 改属性后，必须失效对应 cache line，否则旧属性下缓存的数据会被错误复用：

```c
/* 改 MPU 属性后：DSB → 失效 cache → ISB */
MPU_UpdateRegionAttr(n);
__DSB();
SCB_CleanInvalidateDCache_by_Addr(addr, size);
__DSB();
__ISB();
```

**禁用 D-Cache 与 MPU 的替代方案**：NXP 在 Standby RAM 案例中给出的两条路是「禁用 D-Cache」或「MPU 配成 non-cacheable」。二选一，但**不能都不做**。

---

## 7. 启动时序与配置顺序

### 6.1 M7 启动序列

```
复位
 └─> 关闭 MPU (MPU_CTRL = 0)
     └─> 配置全部区域 (RNR/RBAR/RASR)
         └─> DSB
             └─> 使能 MPU (ENABLE=1, PRIVDEFENA=1)
                 └─> ISB
                     └─> 按需使能 Cache
                         └─> 启动调度器
```

**不要在使能 Cache 前使能 MPU 的 cacheable 属性** —— 没有 cache 时配 cacheable 是安全的，但反过来（先有 cache 再改属性）必须先 invalidate。

### 6.2 R52 启动序列

```
R52 复位（由 M7 通过 BOOT 配置寄存器启动）
 └─> EL1: SCTLR.M = 0
     └─> 配置 MAIR0/MAIR1
         └─> 逐区域写 PRBAR/PRLAR  ← ATCM 区域必须在其中（§5.5）
             └─> DSB + ISB
                 └─> 置 PRENR 对应位
                     └─> SCTLR.M = 1, SCTLR.BR = 1
                         └─> DSB + ISB
                             └─> 确认 HCR.DC = 0（否则背景区域始终可执行）
                                 └─> 使能 Cache / TCM
                                     └─> 启动 EL1 软件
```

**该序列特有的两条约束**：

1. **ATCM 优先。** R52 TRM §6.1.1：*"Do not enable the MPU unless at least one MPU region is programmed and active. If the MPU is enabled, before using the TCM you must program MPU regions to cover the TCM regions."* 若在没有覆盖 TCM 的 region 时就置 `SCTLR.M`，TCM 访问会立即 fault。
2. **`WXN` 是决策，不是默认。** `WXN`/`UWXN` 复位为 0。由于 ATCM 必须保持可执行，全局 `WXN=1` 这条路走不通 —— 改为逐 region 置 `XN`，并加上电自检读回每个 `PRBAR.XN`。

R52 无独立复位（SEGGER 文档明确指出调试器无法单独复位 R52 核），因此**R52 的 MPU 配置完全由 M7 侧的启动代码负责触发**，两者之间需要 MU 中断或共享内存标志握手。

### 6.3 双核配置的时序风险

| 风险 | 说明 | 缓解 |
| --- | --- | --- |
| R52 先跑，M7 未起 | R52 访问未初始化的共享数据 | M7 完成 MRAM/SRAM 初始化后才通过 MU 释放 R52 |
| 各自 MPU 属性不一致 | 跨核共享区一个核看到旧值 | 共享区地址与属性集中定义在共享头文件 |
| 关 PD2 前未清 cache | 脏数据未写回 | 进 LPRUN/Standby 前 clean + invalidate |
| 重配区域时自举 | 改权限的代码在目标区内 | 关键重配放 RAM 中执行 |

---

## 8. 故障处理与 ASIL D 关联

### 7.1 故障响应矩阵

| 场景 | 检测手段 | 响应 |
| --- | --- | --- |
| 非法指针解引用 | MPU Permission fault | MemManage / Abort → 记录现场 → 安全停机 |
| 栈溢出 | TCM/MPU 栈边界配置 | Data abort → 安全停机 |
| R52 区域重叠配置错 | Translation fault | Abort → 配置错误，fail fast |
| 外设被误配 cacheable | 功能异常，无 fault | 只能靠代码评审 + 静态检查 |
| 跨核数据不一致 | 无 fault | 需要软件一致性协议，MPU 无能为力 |

> 关键认知：**MPU 只能挡住"越权"，挡不住"配置错误"**。外设窗口误配为 cacheable 这类问题不会产生任何 fault，只表现为功能异常。所以 MPU 配置表应纳入静态检查与单元测试。

### 7.2 双核协同的安全策略

S32K5 是 ASIL D 平台，MPU 配置本身属于**安全相关配置项**，需要：

1. **配置完整性检查**：上电后自检遍历所有 region，验证 BASE/LIMIT/属性与编译期常量表一致，不一致则拒绝启动。
2. **双核交叉校验**：M7 侧持有 R52 的期望配置表，通过 MU 让 R52 回读实际寄存器并比对。
3. **单点故障防护**：MPU 寄存器本身不受保护，配置错误不会产生 fault。需在 ECC 覆盖的只读常量中保存期望值，运行期周期性比对。
4. **ASIL D 分解**：MPU 作为硬件机制提供的是 **QM 级能力**，要达到 ASIL D 需要配合诊断覆盖率（结构性覆盖 + 运行时比对）。

### 7.3 诊断覆盖建议

| 诊断项 | 方法 | 覆盖率目标 |
| --- | --- | --- |
| MPU 可用性 | 读 `MPU_TYPE`，确认 DREGION != 0 | 开机自检 |
| 区域配置正确性 | 遍历比对期望表 | 开机 + 运行时周期 |
| R52 寄存器可读 | 通过 MU 让 R52 回读 PRBAR/PRLAR | 开机 |
| Cache 属性与 MPU 一致 | 静态配置一致性检查 | 编译期 + 评审 |

---

## 9. 实现清单

### 8.1 移植层接口抽象

由于 M7 与 R52 的寄存器模型完全不同，驱动层应抽象出统一接口：

```c
typedef struct {
    uint32_t base;        /* 区域基址 */
    uint32_t limit;       /* 区域上限（含）；M7 侧由 size 换算 */
    uint8_t  attr;        /* 平台无关的属性枚举 */
    uint8_t  ap;          /* 平台无关的权限枚举 */
    uint8_t  xn;
} MpuRegionCfg;

/* 平台相关实现 */
typedef struct {
    int (*GetRegionCount)(void);
    int (*SetRegion)(uint32_t idx, const MpuRegionCfg *cfg);
    int (*Enable)(void);
    int (*Disable)(void);
    int (*Verify)(const MpuRegionCfg *cfg, uint32_t idx);
} MpuHalOps;

extern const MpuHalOps MpuHal_M7;   /* PMSAv7 实现 */
extern const MpuHalOps MpuHal_R52;  /* PMSAv8-32 实现 */
```

**属性枚举统一映射**：

| 平台无关枚举 | M7 (TEX/C/B/S) | R52 (MAIR idx, val) |
| --- | --- | --- |
| `MPU_ATTR_DEVICE` | `010/0/0` | idx 1, `0x04` |
| `MPU_ATTR_NORMAL_WB` | `001/1/1` | idx 0, `0xFF` |
| `MPU_ATTR_NORMAL_WT` | `000/1/0` | idx 2, `0xBB` |
| `MPU_ATTR_NORMAL_NC` | `001/0/0` | idx 3, `0x04` |
| `MPU_ATTR_STRONGLY_ORDERED` | `000/0/0` | idx 4, `0x00` |

**权限枚举统一映射**：

| 平台无关枚举 | M7 AP | R52 AP |
| --- | --- | --- |
| `MPU_AP_NO_ACCESS` | `000` | — |
| `MPU_AP_PRIV_RW` | `001` | `01`（本 EL） |
| `MPU_AP_PRIV_RO_UNPRIV_RO` | `110` | `10` |
| `MPU_AP_FULL_RW` | `011` | `00` |
| `MPU_AP_PRIV_RO` | `101` | `10` |

### 8.2 集成步骤

1. 打开 `SCB->SHCSR` 的 `MEMFAULTENA` 位（MemManage 使能），并设置优先级高于其他可屏蔽异常。
2. 实现 MemManage（EL0/EL1 为 Abort 异常）处理程序，读取并保存 CFSR/MMFAR/BFAR 与堆栈 PC/LR。
3. 分配 no-cacheable 的 fault log 区域，确保诊断数据不被 cache 影响。
4. 在 `MPU_TYPE.DREGION` 确认区域数后再访问 region 寄存器。
5. 按 4.2 / 4.3 的布局表编写配置代码，**地址与 SIZE 必须与 linker script 严格一致**。
6. 使能后执行自检比对，失败则拒绝启动。
7. 在 Debug 配置中打开 MemManage / Abort 断点。

### 8.3 常见错误清单

| # | 错误 | 后果 | 修正 |
| --- | --- | --- | --- |
| 1 | 外设配成 Normal cacheable | 读旧值、写丢失 | 用 Device 类型 |
| 2 | M7 region 基址未按 SIZE 对齐 | 保护范围悄悄扩大 | 与 linker 对齐 |
| 3 | R52 区域重叠 | Translation fault | 重新划分不重叠区间 |
| 4 | 未先 DSB/ISB 就生效 | 新属性延迟生效 | 改属性前后加屏障 |
| 5 | 重配区域的代码位于该区域内 | 取指失败、CPU 卡死 | 关键重配移入 RAM |
| 6 | 改属性后未 invalidate cache | 旧数据被复用 | DSB → clean/invalidate → ISB |
| 7 | LPE_SRAM（Standby 保持区）配成 cacheable | 低功耗后数据丢失 | 配 NC 或关 D-Cache |
| 8 | 用 AP=`100`（M7 保留值） | 行为不可预测 | 只用合法编码 |
| 9 | 访问越界 region 序号 | 未定义行为 | 先查 DREGION |
| 10 | 忘开 `MEMFAULTENA` | fault 直接进 HardFault | 初始化时开 |
| 11 | TCM 只配了核 MPU，没配 XRDC | 其他 master 经 backdoor 写入畅通无阻 | 两层都配（§5.5） |
| 12 | 以为 XRDC 能让区域不可执行 | 代码照样跑 | XRDC 无 XN，`XN` 要在核 MPU 里设（§5.8） |
| 13 | XRDC `GVLD` 提前置位 | 被保护内存变得不可访问 | 先配完、自检、再使能（§5.8） |
| 14 | OMU 量产未禁用 | 读被静默转到重映射地址 | `OER[OE]=0`，靠 FCCU 监控（§12） |
| 15 | R52 自检只遍历 region 0–15 | region 16–19 被静默跳过 | 用 `PRSELR` 间接访问（§3.4） |

---

## 10. 参考资料

| # | 文档 | 链接 |
| --- | --- | --- |
| 0 | **NXP S32K5xx Reference Manual Rev.3（rm1131130）** + 内嵌 `S32K5xx_memory_map.xlsx` —— **本修订的地址权威** | 本地副本 |
| 1 | Cortex-M7 TRM（ARMv7-M PMSAv7 寄存器） | `developer.arm.com/documentation/ddi0403` |
| 2 | Armv7-M ARM — MPU_RASR（含 TEX/C/B/S 与 AP 编码表） | `developer.arm.com/documentation/ddi0403/d/.../MPU-Region-Attribute-and-Size-Register--MPU-RASR` |
| 3 | Cortex-R52 TRM r1p2 — About the MPU | `developer.arm.com/documentation/100026/0102/Memory-Protection-Unit` |
| 4 | Cortex-R52/R52+ Programmer's Guide — The Memory Protection Unit | `developer.arm.com/documentation/109997/0101` |
| 5 | Cortex-R52 产品页（MPU 区域数与规格） | `developer.arm.com/ip-products/processors/cortex-r/cortex-r52` |
| 6 | Arm Cortex-R 处理器对比表 | `arm.com/-/media/Arm Developer Community/PDF/...` |
| 7 | Armv7-M and Armv8-R 软件迁移指南（MPU 初始化示例） | `documentation-service.arm.com/static/65e0a4c2837c4d065f654f42` |
| 8 | NXP S32K Knowledge Base（linker 分区与 Standby RAM 约束） | `community.nxp.com/t5/S32K-Knowledge-Base` |
| 9 | SEGGER NXP S32K5xx 知识库（MRAM 基址与多核调试） | `kb.segger.com/NXP_S32K5xx` |
| 10 | Zephyr S32K5XXCVB 板级文档（存储资源） | `docs.nordicsemi.com/bundle/ncs-latest/.../s32k5xxcvb` |
| 11 | Zephyr S32K566 SoC 移植提交（R52 `mpu_regions.c`，外设窗口真实上限） | `jausoft.net/cgit/zephyr.git/commit?id=72fb81eb` |
| 12 | NXP AN14715 — XRDC 内存/外设资源配置与 SEMA42 域间共享 | `docs.nxp.com/bundle/AN14715` |
| 13 | MCUXpresso SDK XRDC API（MGR/MDAC/MRC/PAC） | `mcuxpresso.nxp.com/api_doc/dev/721/group__xrdc.html` |
| 14 | Cortex-M7 TRM — TCM configuration（固定基址与大小规则） | `developer.arm.com/docs/ddi0489/latest/memory-system/tcm-interfaces/tcm-configuration` |
| 15 | All About Circuits — S32K5 MRAM 架构解读（XRDC 两层隔离、MRAM 特性） | `allaboutcircuits.com/news/nxp-rolls-out-automotive-mcu-for-zonal-sdvs-leveraging-mram` |
| 16 | NXP S32K5 产品页（MRAM 41 MB、XRDC、ASIL D） | `nxp.com/products/S32K5` |

> **关于参考资料 11 的说明**：Zephyr `mpu_regions.c` 给出的 `0xE00FFFFF` 外设上界在 Rev.A 中被当作权威使用。Rev.B 改用 memory map 真实值 `0x4219_7FFF`（桥延伸到 `0x431F_FFFF`）。参考资料 11 仅作佐证，不作权威。

---

## 11. 待确认事项

**Rev.B（2026-10-14）已关闭** —— 依据 `rm1131130` Rev.3 及其内嵌 `S32K5xx_memory_map.xlsx` 解决：

- [x] ~~S32K5 中 R52 的系统寄存器实际集成地址（`0x42000000` 占位）~~ → PPB 为 `0xE000_0000`–`0xE00F_FFFF`；CPE_GIC0 为 `0x4300_0000`–`0x431F_FFFF`
- [x] ~~R52 EL1 MPU 实现了 16 / 20 / 24 中的哪个~~ → **EL1: 20，EL2: 20**（RM Ch.02 Table 6/10）
- [x] ~~M7 的 MPU 区域数（DREGION 实际值）~~ → **16 个区域**（同表）
- [x] ~~是否支持 EL2 与虚拟化~~ → **支持**；EL2 MPU 存在且支持 hypervisor
- [x] ~~SRAM 各分区的确切边界~~ → SRAM0/1/2 在 `0x2100_0000`/`0x2110_0000`/`0x2120_0000`，各 1 MB；CPE_SRAM0-3 在 `0x2200_0000`–`0x220F_FFFF`
- [x] ~~R52 SRAM（`cpe_sram`）的基址与大小~~ → `0x2200_0000`，1 MB（4×256 KB）
- [x] ~~ITCM / DTCM 的实际大小与地址~~ → ITCM 32 KB @ `0x0000_0000`；DTCM 64 KB @ `0x2000_0000`；R52 A/B/C TCM 各 32 KB @ `0x0100/0110/0120_0000`（CPU0）、`0x0140/0150/0160_0000`（CPU1）
- [x] ~~外设窗口的真实上限~~ → 最后一个已映射外设 `0x4219_7FFF`；桥延伸到 `0x431F_FFFF`
- [x] ~~PPB 与厂商自定义空间的划分~~ → PPB 为 `0xE000_0000`–`0xE00F_FFFF`（1 MB）
- [x] ~~XSPI 寄存器窗口与数据窗口基址~~ → 数据 `0x8100_0000`；寄存器 `0x40BA_4000`–`0x40BA_BFFF`
- [x] ~~XRDC domain 数量与 MRC/PAC region 数量上限~~ → 16 个 Domain ID；每实例 768 个 PDAC slot；每 MRC 16 个 MRGD
- [x] ~~M7 核数~~ → **4** 个物理 M7 核（RM Table 9），不是 6

**仍未解决：**

- [ ] M7 `MPU_RASR` 的 `SIZE` 字段编码公式与 `AP[2:0]` 语义 —— 需 *Arm v7-M Architecture Reference Manual*，该文档不在参考集内。§2.3/§2.4 用的是 Armv7-M 标准编码，量产前应以 DDI 0314 复核。
- [ ] MRAM 数据保持期（NXP–TSMC 称 20 年 @150 °C，另有资料称 10 年 @85 °C，差异巨大）
- [ ] MRAM 写入速度的确切口径（8.8 MB/s vs 15 MB/s）
- [ ] MRAM 写期间的取指/流水线行为（是否需要 FOTA 期间关 cache）
- [ ] Secure 视图的基址规则（仅 PBRIDGE3_0 的 `+0x1000_0000` alias 已确认）
- [ ] XRDC region 的最小对齐粒度
- [ ] XRDC 违规的 Bus Fault 优先级与 handler 挂接方式
- [ ] MCAL 中 `MemoryProtection_Ip` 与 `Xrdc_Ip` 的可用性（AUTOSAR 路径）
- [ ] Standby 模式保持的 384 KB LPE_SRAM 是否对 M7 侧构成 non-cacheable 约束（S32K3 的 Standby RAM 规则不延续）

---

## 12. OMU：ASIL 分区的地址重映射陷阱（Rev.B 新增）

Overlay Management Unit 只重映射**读**地址，且 FCCU 被要求在其正常工作时保持其禁用。

| 项 | 值 |
| --- | --- |
| 实例 | `OMU_0 0x40BC_0000`、`OMU_1 0x40BC_8000`、`OMU_2 0x40BD_0000`、`CPE_OMU_0 0x4109_0000` |
| Region | 16 个（ORD0–ORD15），8 个 zone |
| 粒度 | 1 KB – 8192 MB，2 的幂 |
| 方向 | **仅读** —— 写不重映射 |
| 作用范围 | **Code MRAM 前 16 MB**（`0x0800_0000`–`0x08FF_FFFF`） |
| 延迟 | 命中时 AXI 读地址通道 +3 周期 |
| 优先级 | lowest order region hit wins；全局 region 必须是最低优先级活动 region |

> RM Ch.35 §35.3：*"During normal operation, the **FCCU monitors the OMU enable signal to ensure that the OMU is always disabled**."*

**为什么这与 MPU 设计相关**：OMU 的作用范围正好覆盖 §4.2/§4.3 配置的 Code MRAM region。若 OMU 在开发模式下遗留启用，CPU 读到的是重映射后的内容，而写的是原地址 —— 代码看起来在跑，但跑的不是那个地址的代码。**量产必须置 `OER[OE]=0`（bypass）**，并依赖 FCCU 监控作为安全机制。

---

## 13. 风险清单汇总（Rev.B 新增）

| # | 风险 | 严重度 | 依据 |
| --- | --- | --- | --- |
| 1 | R52 区域重叠产生 **translation fault**，而非按优先级裁决 | 🔴 高 | R52 TRM §8.1 |
| 2 | `SCTLR.WXN` / `UWXN` 复位为 **0** —— 可写区域默认可执行 | 🔴 高 | R52 TRM Table 3-133 |
| 3 | 全局 `WXN=1` 会破坏 ATCM 可执行性（向量表） | 🔴 高 | 推导，见 §5.5 |
| 4 | R52 使能 MPU 前未配覆盖 TCM 的 region → TCM 访问全锁 | 🔴 高 | R52 TRM §6.1.1 |
| 5 | M7/R52 TCM **backdoor 绕过核 MPU**，只有 XRDC MRC 能覆盖 | 🔴 高 | M7 TRM（AHBS）+ RM Ch.02 Table 11/12 |
| 6 | XRDC `GVLD=1` 早于 descriptor 配置完成 → 被保护内存不可访问 | 🔴 高 | RM Ch.31 §31.5.6.5 |
| 7 | ITCM 与 LPE_SRAM alias 共用 `0x0000_0000` —— 无法按地址区分 | 🟠 中高 | memory_map.xlsx |
| 8 | EL2 MPU region 必须覆盖所有 EL1 可见地址，否则两级查找 fault | 🟠 中高 | R52 TRM §8.2.2 |
| 9 | `HMAIR0`/`HMAIR1` 复位为 0 —— EL2 侧属性编程前全部无效 | 🟠 中高 | R52 TRM §3.3.45 |
| 10 | `HCR.DC=1` 使背景区域的指令取指始终可执行 | 🟠 中高 | R52 TRM §8.2.3 |
| 11 | REG_PROT transfer error 需 MPU 配 strongly-ordered 才可捕获 | 🟡 中 | RM Ch.11 §11.3.5 |
| 12 | R52 region 16–19 只能经 `PRSELR` 访问 —— 遍历自检会静默漏掉 | 🟡 中 | R52 TRM §3.3.85-87 |
| 13 | XRDC **无 XN** —— 可执行性完全由核 MPU 负责 | 🟡 中 | RM Ch.31 Table 147 |
| 14 | OMU 只重映射读，且作用于 Code MRAM 前 16 MB | 🟡 中 | RM Ch.35 §35.3 |
| 15 | `GCR[HLB]` 仅系统复位可清 —— 断送 OTA 后重配置的可能 | 🟡 低 | RM Ch.11 §11.6.3 |
| 16 | MSCM `CPXCFG3[CMP]` 复位值未知 —— 必须回读，不能假设 | 🟡 低 | RM Ch.09 §9.5.3.8 |

> 上表中的地址与区域数一旦确认，需要同步更新 4.2 / 4.3 的布局表、第 5 章的按存储类型配置表，以及 2.8 / 3.8 的配置代码。
