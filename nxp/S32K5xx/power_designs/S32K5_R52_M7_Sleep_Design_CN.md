# R52 和 M7 双核独立 OS 的休眠设计方案

## 1. 整体架构认知

S32K5 的电源域（Power Domain）划分决定了休眠策略的根本约束：

| 电源域 | 包含内容 | 可独立开关 |
|---|---|---|
| **PD0**（Always-On） | PMC、RGM、WKPU、MC_PCU、FRO、SIRC、384KB SRAM 等 | 否（始终供电） |
| **PD1**（低功耗引擎） | **CM4**、DMA、ADC、LPUART、LPSPI、FTM、STM 等 | 是（可独立于 PD2） |
| **PD2**（全性能域） | **CM7、R52**、MRAM、HSE2 + 所有其他外设 | 是（可独立于 PD1） |

**关键约束**：CM7 和 R52 都位于 **PD2** 中，这意味着——**无法单独让 CM7 休眠而 R52 继续运行，反之亦然**。PD2 要么全上，要么全下。

## 2. 支持的电源模式及各核心状态

| 电源模式 | 供电域 | R52 | M7 | CM4（LPE） | HSE2 |
|---|---|---|---|---|---|
| **RUN** | PD2+PD1+PD0 | Run/Wait | Run/Wait | Run/Wait/Stop1/Stop2 | Run |
| **LPRUN** | PD1+PD0 | Off | Off | Run/Wait/Stop1/Stop2 | Off |
| **STANDBY** | PD0 | Off | Off | Off | Off |

也就是说，R52 和 M7 的休眠是**绑定的**，它们必须一起进入 LPRUN/STANDBY 或一起唤醒。

> **注 1**：CM4 在 RUN 和 LPRUN 下均为 `Run / Wait / Stop1 / Stop2`，其中 Stop1 与 Stop2 是**两种不同的低功耗状态**，配置时不可合并处理。
>
> **注 2（LPRUN 时钟）**：LPRUN/Standby 下 **PLL 不可用**，可用时钟仅为 FXOSC、SXOSC、SIRC、FIRC 及其派生。FIRC 在这些模式下**处于活动状态但不可配置**（资源仅 HSE2 可访问）。因此若要走 Run → LPRUN → Standby 路径，**FIRC 必须在 Run 模式下配置好**，因为 LPRUN 中 HSE2 已不可用。

## 3. 推荐的休眠设计方案

### 方案一：LPRUN 模式（推荐，最常用）

当 M7 和 R52 都无事可做时，两者都执行 WFI，PD2 断电，仅保留 **LPE（CM4）在 PD1 中运行**。

```
正常 RUN（M7+R52 全速运行）
    |
    v
M7 OS 和 R52 OS 各自完成关断前准备
    |
    v
Requestor Core 通过 MU 中断通知 CM4，CM4 停止使用 PD2 外设后确认
    |
    v
M7 和 R52 各自执行 WFI
    |
    v
Requestor Core 轮询 MC_ME 中对方 WFI 状态
    |
    v
PCFS ramp-down（降频到初始频率）
    |
    v
写 CTL_KEY 密钥序列，再通过 MC_ME[COREx_PCONF] 关闭 M7 和 R52 的时钟
    |
    v
关停 PD2 外设的时钟（写 CTL_KEY + MC_ME[COFB_CLKEN]）
    |
    v
切换时钟源到 FRO，关闭 PLL
    |
    v
Pad Keeping 配置（可选）
    |
    v
停止 HSE2 服务（可选）
    |
    v
PMIC handshake 配置（使用外部 PMIC 时必需）
    |
    v
执行 DSB + ISB 屏障，确保无挂起指令
    |
    v
写 CTL_KEY + MC_RGM 的 MODE_CONF[LPRUN] 请求进入 LPRUN
    --------------------------------
    LPRUN 模式（仅 CM4 运行在 PD1）
```

### 方案二：STANDBY 模式（最低功耗）

```
正常 RUN（M7+R52）
    |
    v
（可选先进入 LPRUN）
    |
    v
CM4 接管关断流程（作为 Requestor Core）
    |
    v
关停 PD1 外设（写 CTL_KEY + MC_ME[COFB_CLKEN]）
    |
    v
配置 WKUP 唤醒源
    |
    v
Pad Keeping 配置
    |
    v
PMIC handshake 配置（使用外部 PMIC 时必需）
    |
    v
执行 DSB + ISB 屏障
    |
    v
写 CTL_KEY + MC_RGM 的 MODE_CONF[STANDBY] 请求进入 STANDBY
    --------------------------------
    STANDBY（仅 PD0 供电，384KB RAM 保持）
```

## 4. 多核休眠协调流程（关键）

S32K5 的 **MC_ME** 模块提供了 WFI 状态监测机制，用于多核协调。

> **与 MCU 驱动的对应关系**：NXP S32K5 MCU 驱动（UM85MCUASRR23-11）将整个 Standby 进入过程划分为 **SW1–SW4 四个软件阶段**，由 `Mcu_SetMode` / `Mcu_InitClock` 驱动，下表已按此阶段组织。实际项目中这些寄存器级操作由 MCU 驱动内部完成，应用层只需调用 API。
>
> | 阶段 | 名称 | 驱动 API | 本文对应步骤 |
> |---|---|---|---|
> | SW1 | Peripheral Shutdown | `Mcu_SetMode`（外设集） | Step 4.1–4.3 |
> | SW2 | Application Core Shutdown | 应用核 `Mcu_SetMode(CORE_STANDBY)`；主核 `Mcu_SetMode`（`McuCoreUnderMcuControl` 勾选 + `McuCoreClockEnable` 取消） | Step 4.2–4.3 |
> | SW3 | Flash 低功耗握手 + PMC_LASTMILE 关闭 | `Mcu_InitClock`、`Mcu_SetMode(SOC_PREPARE_STANDBY)` | Step 4.6 |
> | SW4 | Main Core Shutdown | `Mcu_SetMode(SOC_STANDBY)`，`McuMainCoreSelect` 选主核 | Step 4.12 |
>
> 相关 Tresos/MCAL 配置参数：`McuPowerMode`（`CORE_STANDBY` / `SOC_PREPARE_STANDBY` / `SOC_STANDBY`）、`McuCoreUnderMcuControl`、`McuCoreClockEnable`、`McuMainCoreSelect`。

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 741" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>S32K5 Standby entry: SW1-SW4 phases with dual-core coordination</title>
<desc>Four software phases driving the S32K5 MCU driver into Standby: peripheral shutdown, application core shutdown, flash low-power handshake with PMC_LASTMILE disable, and main core shutdown, with PD2/PD1/PD0 power state shown per phase.</desc>
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="40" y="26" font-size="15" font-weight="500" fill="#2C2C2A">Standby 入口：SW1–SW4 四阶段与双核协作</text>
<text x="40" y="45" font-size="12" fill="#5F5E5A">每阶段由 MCU 驱动 API 承接，应用层只调 API，不直接操作寄存器</text>
<rect x="40" y="62" width="424" height="119" rx="10" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
<path d="M40 72 a10 10 0 0 1 10 -10 h404 a10 10 0 0 1 10 10 v34 h-424 z" fill="#B5D4F4"/>
<text x="53" y="84.0" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">SW1</text>
<text x="88" y="84.0" font-size="13" font-weight="500" fill="#042C53" dominant-baseline="central">外设关断Peripheral Shutdown</text>
<text x="88" y="99.0" font-size="11" fill="#185FA5" dominant-baseline="central">Mcu_SetMode（外设集）</text>
<circle cx="57" cy="133.5" r="2" fill="#185FA5"/>
<text x="68" y="133.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">关停 PD2 外设时钟：CTL_KEY + COFB_CLKEN[REQnz]</text>
<circle cx="57" cy="152.5" r="2" fill="#185FA5"/>
<text x="68" y="152.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">一次只关一个 CPE 分区，否则 HardFault</text>
<rect x="480" y="86.5" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="96.5" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD2 运行</text>
<rect x="480" y="111.5" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="121.5" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD1 运行</text>
<rect x="480" y="136.5" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="146.5" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD0 运行</text>
<rect x="40" y="181" width="424" height="138" rx="10" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
<path d="M40 191 a10 10 0 0 1 10 -10 h404 a10 10 0 0 1 10 10 v34 h-424 z" fill="#CECBF6"/>
<text x="53" y="203.0" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">SW2</text>
<text x="88" y="203.0" font-size="13" font-weight="500" fill="#26215C" dominant-baseline="central">应用核关断Application Core Shutdown</text>
<text x="88" y="218.0" font-size="11" fill="#534AB7" dominant-baseline="central">Mcu_SetMode（CORE_STANDBY）</text>
<circle cx="57" cy="252.5" r="2" fill="#534AB7"/>
<text x="68" y="252.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">MU 中断通知 CM4 停止使用 PD2 外设</text>
<circle cx="57" cy="271.5" r="2" fill="#534AB7"/>
<text x="68" y="271.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">各核读 WFI 状态，PD2 两核彼此确认</text>
<circle cx="57" cy="290.5" r="2" fill="#534AB7"/>
<text x="68" y="290.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">PCFS ramp-down → 关钟 → MC_RGM_PRST</text>
<rect x="480" y="215.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="225.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD2 运行</text>
<rect x="480" y="240.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="250.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD1 运行</text>
<rect x="480" y="265.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="275.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD0 运行</text>
<rect x="40" y="319" width="424" height="138" rx="10" fill="#FAEEDA" stroke="#854F0B" stroke-width="0.5"/>
<path d="M40 329 a10 10 0 0 1 10 -10 h404 a10 10 0 0 1 10 10 v34 h-424 z" fill="#FAC775"/>
<text x="53" y="341.0" font-size="13" font-weight="500" fill="#412402" dominant-baseline="central">SW3</text>
<text x="88" y="341.0" font-size="13" font-weight="500" fill="#412402" dominant-baseline="central">Flash 握手 + 末级稳压器</text>
<text x="88" y="356.0" font-size="11" fill="#854F0B" dominant-baseline="central">Mcu_InitClock + SOC_PREPARE_STANDBY</text>
<circle cx="57" cy="390.5" r="2" fill="#854F0B"/>
<text x="68" y="390.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">等待进行中的 Flash 高压操作结束</text>
<circle cx="57" cy="409.5" r="2" fill="#854F0B"/>
<text x="68" y="409.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">系统时钟切 FIRC、关 PLL（PLLDIG 不可用）</text>
<circle cx="57" cy="428.5" r="2" fill="#854F0B"/>
<text x="68" y="428.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">关闭 PMC_LASTMILE，否则 Flash 仍耗电</text>
<rect x="480" y="353.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="363.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD2 运行</text>
<rect x="480" y="378.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="388.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD1 运行</text>
<rect x="480" y="403.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="413.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD0 运行</text>
<rect x="40" y="457" width="424" height="138" rx="10" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
<path d="M40 467 a10 10 0 0 1 10 -10 h404 a10 10 0 0 1 10 10 v34 h-424 z" fill="#9FE1CB"/>
<text x="53" y="479.0" font-size="13" font-weight="500" fill="#04342C" dominant-baseline="central">SW4</text>
<text x="88" y="479.0" font-size="13" font-weight="500" fill="#04342C" dominant-baseline="central">主核关断Main Core Shutdown</text>
<text x="88" y="494.0" font-size="11" fill="#0F6E56" dominant-baseline="central">Mcu_SetMode（SOC_STANDBY）</text>
<circle cx="57" cy="528.5" r="2" fill="#0F6E56"/>
<text x="68" y="528.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">配置 WKPU 唤醒源（内部源仅正极性）</text>
<circle cx="57" cy="547.5" r="2" fill="#0F6E56"/>
<text x="68" y="547.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">执行 DSB + ISB 屏障</text>
<circle cx="57" cy="566.5" r="2" fill="#0F6E56"/>
<text x="68" y="566.5" font-size="12" fill="#2C2C2A" dominant-baseline="central">写 MODE_CONF[STANDBY] + CTL_KEY 密钥</text>
<rect x="480" y="491.0" width="160" height="20" rx="5" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="560.0" y="501.0" font-size="11" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">PD2 断电</text>
<rect x="480" y="516.0" width="160" height="20" rx="5" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="560.0" y="526.0" font-size="11" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">PD1 断电</text>
<rect x="480" y="541.0" width="160" height="20" rx="5" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.5"/>
<text x="560.0" y="551.0" font-size="11" fill="#173404" text-anchor="middle" dominant-baseline="central">PD0 运行</text>
<path d="M252.0 182 L252.0 196" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M252.0 336 L252.0 350" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M252.0 490 L252.0 504" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="40" y="659" width="424" height="62" rx="10" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.5"/>
<text x="53" y="676" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">退出路径（唤醒）</text>
<text x="53" y="694" font-size="11" fill="#5F5E5A" dominant-baseline="central">WKPU 事件 → LPE CM4 断言 EXTWAKE → PD2 上电</text>
<text x="53" y="709" font-size="11" fill="#5F5E5A" dominant-baseline="central">（destructive reset）→ HSE2 BootROM → sBAF → HSE2_FW</text>
<rect x="480" y="667" width="160" height="20" rx="5" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="560.0" y="677" font-size="11" fill="#042C53" text-anchor="middle" dominant-baseline="central">Mcu_GetResetReason</text>
<text x="560.0" y="702" font-size="11" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">判定唤醒源</text>
</svg>
<figcaption style="font-size:0.85em;color:#666">图 1：Standby 入口的 SW1–SW4 四阶段与双核协作（PD 状态示意）</figcaption>
</figure>


### Step 1：各 OS 各自完成睡眠前准备

| M7 OS 要做的事 | R52 OS 要做的事 |
|---|---|
| 关闭非必要中断源 | 关闭非必要中断源 |
| 保存上下文（保存到 PD0 SRAM） | 保存上下文（保存到 PD0 SRAM） |
| 停止 M7 上的 HSE2 服务请求 | 停止 R52 上的 HSE2 服务请求 |
| 设置唤醒中断 | 设置唤醒中断 |
| 通知 R52 OS 准备休眠（MU 中断） | 确认并回复 M7 |
| 执行 **WFI** | 执行 **WFI** |

**此外，Requestor Core 必须通过 MU 中断通知 CM4（LPE）**：即使 PD1 在 LPRUN 下保持供电，CM4 仍可能正在访问 PD2 域的资源（如 FLEXCAN、SENT 等位于 PD2 的外设）。Requestor Core 需通知 CM4 停止使用这些 PD2 外设，CM4 确认后方可继续关断流程。

### Step 2：Requestor Core 检查 WFI 状态

由任一核心（M7 或 R52）担任 **Requestor Core**，轮询检查各核心的 WFI 状态。

⚠️ **关键**：WFI 状态寄存器分属**三个不同的 MC_ME 分区**，各核心的寄存器不可混用。

| 核心 | WFI 状态寄存器 | 所属分区 |
|---|---|---|
| Cortex-M7_0 | `MC_ME.PRTN0_CORE0_STAT[WFI]` | SoC MC_ME |
| Cortex-M7_1 | `MC_ME.PRTN0_CORE2_STAT[WFI]` | SoC MC_ME |
| Cortex-M7_2 | `MC_ME.PRTN0_CORE3_STAT[WFI]` | SoC MC_ME |
| Cortex-M7_3 | `MC_ME.PRTN0_CORE4_STAT[WFI]` | SoC MC_ME |
| Cortex-R52_0 | `CPE_MC_ME.PRTN0_CORE0_STAT[WFI]` | CPE MC_ME |
| Cortex-R52_1 | `CPE_MC_ME.PRTN0_CORE1_STAT[WFI]` | CPE MC_ME |
| Cortex-M4 (LPE) | `LPE_MC_ME.PRTN0_CORE0_STAT[WFI]` | LPE MC_ME |

> **注意 M7 的编号不连续**：M7_0 对应 `CORE0`，M7_1 对应 `CORE2`，M7_2 对应 `CORE3`，M7_3 对应 `CORE4`。`CORE1` 不属于 M7，索引时不可按连续数组处理。

因此，**当 R52 作为 Requestor Core 时，读取 M7 的 WFI 状态需访问 SoC MC_ME 分区**（`MC_ME.PRTN0_CORE0_STAT` 等），而非 `CPE_MC_ME`。

### Step 3：时钟降频、关断与复位

```
1. 设置时钟到初始频率，完成 PCFS ramp-down（降频）
2. 确认对方核心 WFI 已置位（读上表对应寄存器）
3. 写 CTL_KEY 密钥序列（0x5AF0，然后 0xA50F）
4. 通过 MC_ME[COREn_PCONF][CCE] 关断目标核心的时钟
5. 确认 MC_ME[COREn_STAT][CCS] 时钟已停止（CCS=0 表示时钟 inactive）
6. 通过 MC_RGM_PRST 断言核心复位
7. 读 MC_RGM_PSTAT 确认复位已生效 -> 核心正式关断
```

### Step 4：关停 PD2 外设与请求模式切换

```
1. 写 CTL_KEY 密钥序列（0x5AF0，然后 0xA50F）
2. 关停 PD2 外设时钟：MC_ME[PRTNn_COFB_CLKEN][REQnz] = 0
3. 写 PRTNn_PUPD 并轮询，读 PRTNn_COFB_STAT[BLOCKnz] 确认时钟已关
4. 切换系统时钟到 FIRC，关闭 PLL
   - Standby 入口**必须切到 FIRC**（PLLDIG 在 Standby 下不可用）
   - 若 2.5V 供电可用且已配置 PMC.CONFIG[LPM25EN]，可改用 FXOSC
   - 所有时钟源均可选关闭（含 FIRC），全关即 no-clock 最低功耗模式
5. 配置 Pad Keeping（PD2 引脚由 WKPU.GPIO_QUAL[PD2_PD0] 统一控制）
6. **SW3：Flash 低功耗握手与 PMC_LASTMILE 稳压器关闭**
   a. 挂起或等待进行中的 Flash 高压操作结束（否则 Flash 编程中途掉电导致非确定性行为）
   b. 切换系统时钟到 FIRC 并关闭 PLL
   c. 配置 SoC 进入 Standby 预备态
7. 停止 HSE2 服务（可选，等待进行中的服务完成）
8. 配置 WKPU 唤醒源（Standby 入口必做；Standby 下无活动核心）
9. PMIC handshake 配置（使用外部 PMIC 供电时必需）
10. **一次只关闭一个 CPE 分区**（CPE_0 与 CPE_1 同时禁用会导致 HardFault）
11. 执行 DSB + ISB 屏障，确保无挂起指令
12. 写 CTL_KEY 密钥序列 + MC_RGM 的 MODE_CONF[LPRUN] 或 MODE_CONF[STANDBY]
    -> 启动硬件模式转换
```

> ⚠️ **CPE 分区关断硬约束**：同时禁用 `PARTITION_CPE_0_INDEX` 和 `PARTITION_CPE_1_INDEX` 会关闭整个 CPE 系统，导致后续禁用 CPE_0 时触发 HardFault。**必须一次只关一个 CPE 分区。**
>
> ⚠️ **CPE_LLC 注意**：对 CPE_LLC0/CPE_LLC1 选择 PowerOffState 会导致 HardFault（驱动仍会访问已断电的分区），应选 PowerOnState。

## 5. 唤醒流程

### 从 LPRUN 唤醒 M7+R52

唤醒主体由 **LPE（CM4）** 执行：

```
外部/内部唤醒事件触发
    |
    v
WKPU 检测到唤醒源 -> 中断 LPE CM4
    |
    v
CM4 执行 PMIC handshake（断言 EXTWAKE，见下表）
    |
    v
PD2 上电（连接 PD1-PD2 的 distributed switch）
    |
    v
PD2 发生 destructive reset
    |
    v
HSE2 BootROM -> sBAF 完整性检查 -> HSE2_FW 使能 PD2 应用核
    |
    v
M7 和 R52 各自的 OS 恢复上下文
    |
    v
恢复到 RUN 模式
```

**注意**：从 LPRUN 唤醒 M7+R52 时，PD2 上电后 **M7 和 R52 会经历 destructive reset**（见 Ch58 Table 308：LPRUN → RUN 时 PD2 发生 destructive reset，PD1/PD0 保持），必须通过启动链重新启动。因此两个 OS 的**上下文保存**至关重要。

> **启动链说明（S32K5 无 IVT 概念）**：硬件复位完成后，**唯一先运行的是 HSE2 上的 ZenV 核**，经 BootROM → sBAF（Secure Boot Assist Firmware）→ HSE2_FW 由 **HSE2_FW 使能 PD2 中的应用核**。S32K5 不使用 IVT（Image Vector Table）机制。

### 唤醒导致的复位域范围

| 模式转换 | PD2 | PD1 | PD0 |
|---|---|---|---|
| Standby → LPRUN | 保持 OFF | destructive reset | 保持活动 |
| Standby → RUN | destructive reset | destructive reset | 保持活动 |
| LPRUN → RUN | destructive reset | 保持活动 | 保持活动 |

> **省电关键路径**：Standby → LPRUN 转换时 **PD2 保持 OFF**，仅 PD1 上电。这是唤醒后 CM4 先跑起来、PD2 应用核稍后才启动的分级上电路径。

### 唤醒源支持

**外部唤醒源**

| 唤醒源类型 | 来源 | 说明 |
|---|---|---|
| **外部 GPIO** | 最少 60 个 WKPU 引脚（WKPU[0]-WKPU[59]） | 实际引脚需查 IOMUX 表；每个源均带独立毛刺滤波器 |

**内部唤醒源（共 8 个，依据 Ch57 Table 299）**

| # | 内部唤醒源 | 说明 |
|---|---|---|
| 1 | LPE_SWT0 | 看门狗定时器 |
| 2 | (NOR (CMPn Round Robin Mode)) AND (LPE_RTC_API Timeout) | 比较器轮询模式与 RTC 超时的组合逻辑源 |
| 3 | LPE_RTC_API Timeout | RTC 唤醒计数器溢出或超时 |
| 4 | LPE_CMP0 Async | 比较器 0 异步边沿 |
| 5 | LPE_CMP1 Async | 比较器 1 异步边沿 |
| 6 | LPE_CMP2 Async | 比较器 2 异步边沿（S32K511 不支持） |
| 7 | LPE_PIT_RTI | PIT 实时中断 |
| 8 | LPE_LCU | 逻辑控制单元 |

> ⚠️ **关键约束**：内部唤醒源**仅支持正极性，不可配置为下降沿触发**。这是休眠后无法唤醒的最常见原因。
>
> **模式关联**：每个唤醒事件都可通过软件配置关联到不同的模式转换（Standby→Run 或 Standby→LPRUN），并非固定支持所有模式。
>
> **NMI 不支持从 Standby 唤醒。**

**多源同时到达时的仲裁**
- 第一个到达 MCU 的唤醒源决定整个模式转换序列，该序列会**执行到底**，除非发生 POR / functional / destructive reset
- 两个及以上唤醒源同时采样且指示不同的模式转换时，**Standby → Run 优先级最高**
- 所有唤醒事件无论设备当前处于何种模式、也无论是否正在进行模式转换，**都会在 WKPU 中置位对应标志**

## 6. STANDBY RAM 使用建议

PD0 域有 **384KB 的 SRAM** 可供数据保持（SRAM UPPER PD0 = 256KB，SRAM LOWER PD0 = 128KB），建议在两个 OS 的休眠方案中这样分配：

| 区域 | 用途 | 建议容量 |
|---|---|---|
| **M7 保留区** | M7 OS 上下文、关键变量 | ~192KB |
| **R52 保留区** | R52 OS 上下文、关键变量 | ~128KB |
| **共享保留区** | 核间通信标志、唤醒原因 | ~64KB |

> **注**：上述 192/128/64KB 的切分是**建议值，非硬件约束**。实际分配需按两个 OS 的实测上下文大小调整，且总容量不得超过 384KB。PD0 SRAM 在低功耗模式下由保持电压供电以维持数据。

## 7. 推荐实施总结

| 事项 | 建议 |
|---|---|
| **目标模式** | **LPRUN**（CM4 保持运行，M7+R52 休眠） |
| **协调机制** | Requestor Core 通过各分区 MC_ME 的 WFI 状态位确认双方就绪（M7 查 `MC_ME`，R52 查 `CPE_MC_ME`，CM4 查 `LPE_MC_ME`） |
| **核间通信** | 用 **MU（Message Unit）** 通知其他核心启动关断流程；共享 PD0 SRAM 用于握手数据 |
| **CM4 通知** | Requestor Core **必须**通知 CM4 停止使用 PD2 外设并确认 |
| **上下文保存** | 每个 OS 将上下文保存到 **PD0 SRAM**（384KB） |
| **时钟降频** | 关钟前先完成 **PCFS ramp-down**；LPRUN/Standby 下 **FIRC 须在 Run 模式预配置** |
| **Flash 低功耗** | Standby 前须**等待 Flash 高压操作结束**并关闭 **PMC_LASTMILE**，否则 Flash 阵列仍耗电 |
| **分区关断顺序** | **一次只关一个 CPE 分区**；CPE_LLC0/1 须选 PowerOnState，否则 HardFault |
| **寄存器写保护** | 所有受控寄存器写入前须执行 **CTL_KEY 密钥序列（0x5AF0 / 0xA50F）** |
| **模式切换屏障** | 写 `MODE_CONF` 前须执行 **DSB + ISB** |
| **唤醒源** | 依 RM Table 299 配置 8 个内部源之一或 WKPU 外部引脚；**内部源仅支持正极性** |
| **中断责任** | 请求模式切换前**必须屏蔽所有中断**；**EcuM 负责确保无唤醒中断丢失**（MCU 驱动无法感知） |
| **PLL 恢复** | 唤醒后需**显式调用 `Mcu_DistributePllClock`** 恢复 PLL 时钟（切 PLL 动作不由 `Mcu_InitClock` 完成） |
| **唤醒源判定** | 用 `Mcu_GetResetReason` 判断唤醒原因 |
| **PMIC 协同** | 推荐 **FS25 SBC**（专为 S32K5/S32J 设计，ASIL D），通过 **PGOOD + EXTWAKE(1)/(2)** 完成 handshake |

> **注**：以上第 4 节中大量寄存器级步骤（PCFS ramp-down、CTL_KEY 密钥序列、`COREn_PCONF[CCE]`、`COFB_CLKEN[REQnz]`、`MODE_CONF`、DSB+ISB）在实际项目中**由 MCU 驱动内部完成**，应用层不应直接操作这些寄存器。详见 `MCAL_API_MAPPING.md`。

### PMIC Handshake 信号语义

S32K5 通过 **PGOOD**（输入）与 **EXTWAKE(1)/EXTWAKE(2)**（输出）与 PMIC/SBC 握手，最多使用 4 个 GPIO。EXTWAKE 的极性可通过 `GPR_0` 寄存器配置，映射通过 SIUL2 的 MSCR 配置。

| 设备模式转换 | EXTWAKE(1) | EXTWAKE(2) |
|---|---|---|
| Run → LPRUN | 信号解除断言 | 信号解除断言 |
| Run → Standby | 信号解除断言 | 信号解除断言 |
| LPRUN → Standby | 信号解除断言 | 信号解除断言 |
| LPRUN → Run | 信号断言 | 无变化 |
| Standby → Run | 信号断言 | 无变化 |
| Standby → LPRUN | 无变化 | 信号断言 |

> **PMIC 侧仅响应 EXTWAKE 的断言（assertion）**，解除断言应被忽略。
>
> **EXTWAKE 断言后 POR WDOG 被触发**：若 PGOOD 在配置时间内未拉高，POR WDOG 将对芯片发出复位。
>
> **Run → Standby 需注意 PGOOD 毛刺**：切换时可能检测到非预期复位状态。规避步骤为：① 置 `PMC.CONFIG[PGOODMASK]` 暂时屏蔽 PGOOD；② 将 PMIC 配置进入 LPE 模式（带延时）。此两步必须**受中断保护**，确保序列不会在时间上被拆开。
