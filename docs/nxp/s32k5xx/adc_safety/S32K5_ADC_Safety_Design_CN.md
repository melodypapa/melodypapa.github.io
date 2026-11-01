---
title: "S32K5xx ADC 功能安全机制设计（SARADC / SINC / LPCMP / TEMPSENSE）"
---

> 适用平台：NXP S32K5xx 系列（S32K566 等），含 SARADC_0 / SARADC_1 / LPE_SARADC、SINC、LPE_LPCMP 0–2、TEMPSENSE 五个模拟/模数相关模块
>
> 资料来源：NXP S32K5 Foundation Training —— *Analog（ADC - SINC - LPCMP - TEMPSENSE）* 与 *Safety*（AAES AMCU Systems and Applications）、S32K5xx Reference Manual **Rev.2** Chapter 63 *Safety Overview*（2026-06-01）、S32K5 RTD ADC Driver User Manual（UM85ADCASRR23-11）、S32K5 Safety Manual（SEooC 文档）
>
> **版本说明（2026-10-15）**：Foundation 培训材料基于 **S32K5RM Rev2 DraftE** 与 **S32K5xx DS Rev1 DraftE**，RM 引用取自 Rev.2 正式版 Ch.63。所有寄存器名、位域与默认值在量产前必须以对应型号的正式 Reference Manual 和 Safety Manual 逐条核对。
>
> **增补（2026-10-15）**：新增第 7 章「VCU 加速踏板应用：失效场景与 ADC 侧的额外机制」—— 以加速踏板双路采集为例，给出 F1–F10 失效场景清单与 ADC 硬件层 / VCU 软件层的机制映射；应用层门限为工程惯例示例值，须按项目 HARA 标定。
>
> 关联阅读：本目录 [R52 和 M7 双核独立 OS 的休眠设计方案](../power_designs/S32K5_R52_M7_Sleep_Design_CN.md)（电源域 PD0/PD1/PD2 划分）、[MPU 内存保护单元设计方案](../mpu_concept/S32K5_R52_M7_MPU_Design_CN.md)（ASIL 分区隔离）。

---

## 1. 为什么 ADC 必须做功能安全设计

ISO 26262 的概念安全架构里，一条典型的安全链路是：

```
传感器 → 信号调理 → ADC → 处理单元 → 执行器
```

ADC 是**模拟世界进入数字世界的唯一入口**。一旦 ADC 给出错误转换值，上游的传感器监测和下游的控制决策会同时被污染，且应用层往往无法区分"真实信号越界"与"ADC 疯了"。因此 NXP 在 RM Ch.63 *Safety Overview* 中把 **ADC self-test 列为与 LBIST/MBIST 并列的 specific BIST** 之一：

> "The implementation of the ADC self-test serves a special purpose that is important for a safety-related usage of the ADC. This self-test provides test steps that permit an **independent assessment of the elements of the ADC** integrated within this chip."
> `[来源: S32K5xx RM Rev.2, Ch.63 §63.7.2]`

S32K5 按 ISO 26262 以 **SEooC（Safety Element out of Context）** 开发，目标完整性等级覆盖 **ASIL D**。对 ADC 而言，功能安全机制分为三层，本文按此展开：

| 层次 | 机制 | 回答的问题 |
| --- | --- | --- |
| 精度层 | 校准（Calibration） | "转换结果准不准？" —— 补偿制造偏差与温漂 |
| 自检层 | Self-Test 算法 S/O/C + 看门狗 | "ADC 元件坏没坏？" —— 永久故障检测 |
| 监控层 | 模拟看门狗（AWD）、SINC 检测器、TEMPSENSE 阈值 | "这次转换可不可信？" —— 运行时数据合理性 |

---

## 2. 模拟子系统总览（安全视角）

| 模块 | 实例 | 定位 | 与安全相关的关键特性 |
| --- | --- | --- | --- |
| SARADC | SARADC_0、SARADC_1、LPE_SARADC | 14-bit SAR 模数转换，最高 2 MSa/s | **Self-Test（算法 S/O/C）+ 自检看门狗定时器**、4 路模拟看门狗、内部带隙基准通道 |
| SINC | SINC（1 实例） | 外部 Σ-Δ 调制器位流抽取滤波 | **SCD 短路/开路检测、CAD 时钟缺失检测、ZCD 零交叉检测**、break signal 关断输出 |
| LPCMP | LPE_LPCMP_0/1/2 | 低功耗比较器（CMP + 8-bit DAC + ANMUX） | STANDBY 下 Round-Robin 触发、滞环、窗口模式、唤醒比较 |
| TEMPSENSE | TEMPSENSE（1 实例） | 片内高精度温度传感（BJT + Σ-Δ + 抽取滤波 + 校准引擎） | **normal 与 secure 双地址空间阈值比较器**、过温/欠温/panic 多级阈值 |

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 380" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>S32K5 模拟采集链路的功能安全视图</title>
<desc>从左到右展示传感器、信号调理、SARADC/SINC 采集、处理单元、执行器的主链路，主链路上下两侧标注安全机制（校准、Self-Test 算法 S/O/C、模拟看门狗、SCD/CAD/ZCD、TEMPSENSE 阈值），下方展示故障通知经 VFCCU 汇聚并触发安全状态的全路径。</desc>
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="500" fill="#2C2C2A">S32K5 模拟采集链路 —— 功能安全视图</text>
<rect x="20" y="45" width="110" height="56" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="75" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">传感器</text>
<text x="75" y="86" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">Sensor</text>
<rect x="160" y="45" width="110" height="56" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="215" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">信号调理</text>
<text x="215" y="86" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">滤波 / 放大 / 基准</text>
<rect x="300" y="45" width="130" height="56" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="365" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">SARADC / SINC</text>
<text x="365" y="86" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">14-bit SAR · Σ-Δ 抽取</text>
<rect x="460" y="45" width="100" height="56" rx="8" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="510" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">处理单元</text>
<text x="510" y="86" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">M7 / R52</text>
<rect x="590" y="45" width="80" height="56" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="630" y="68" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">执行器</text>
<text x="630" y="86" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">Actuator</text>
<path d="M130 73 L158 73" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M270 73 L298 73" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M430 73 L458 73" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M560 73 L588 73" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="255" y="118" width="220" height="88" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="365" y="138" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">精度层：校准 Calibration</text>
<text x="365" y="156" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">offset / gain / 电容失配补偿</text>
<text x="365" y="172" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">functional reset 后保留，</text>
<text x="365" y="188" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">destructive reset 后必须重校</text>
<path d="M365 118 L365 105" fill="none" stroke="#378ADD" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="255" y="222" width="220" height="88" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="365" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">自检层：Self-Test</text>
<text x="365" y="260" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">算法 S 电源 / 算法 O 失调 / 算法 C 电容</text>
<text x="365" y="276" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">每算法独立看门狗 + 自检模拟看门狗</text>
<text x="365" y="292" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">错误位 + 出错步号记录</text>
<path d="M365 222 L365 209" fill="none" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="20" y="222" width="210" height="88" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="125" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">监控层：运行时监控</text>
<text x="125" y="260" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">模拟看门狗 AWD（4 路/实例）</text>
<text x="125" y="276" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">SINC：SCD / CAD / ZCD</text>
<text x="125" y="292" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">TEMPSENSE：阈值 + panic</text>
<rect x="505" y="222" width="155" height="88" rx="10" fill="#FAEEDC" stroke="#BA8A29" stroke-width="0.5"/>
<text x="582" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#433422" dominant-baseline="central">VFCCU 故障管理</text>
<text x="582" y="260" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">5×LVFCCU + 1×CVFCCU</text>
<text x="582" y="276" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">中断 / 复位 / EOUT</text>
<text x="582" y="292" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">→ 安全状态</text>
<path d="M230 266 L253 266" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M475 266 L503 266" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#ar)"/>
<text x="20" y="340" font-size="11" fill="#5F5E5A">主链路：传感器 → SARADC/SINC → 处理 → 执行器；三层安全机制挂接其上，故障通知最终汇聚到 VFCCU 并转换为故障反应。</text>
</svg>
</figure>

> **电源域提示**：按 PD0/PD1/PD2 划分（见休眠设计文档），LPE 侧模拟外设（LPE_SARADC、LPE_LPCMP 0–2）隶属 **PD1**，主平台 SARADC_0 / SARADC_1 随 **PD2** 一起关断。在 LPRUN 场景做 ADC 安全监控时，必须选用 LPE 侧实例。`[推导自电源域表，量产前以 RM 电源章节复核]`

---

## 3. SARADC 硬件基础

### 3.1 实例与通道模型

| 项目 | SARADC_0 | SARADC_1 | LPE_SARADC |
| --- | --- | --- | --- |
| BCTU 触发 | 支持 | 支持 | 支持 |
| DMA | 支持 | 支持 | 支持 |
| 硬件通道交错（interleaving） | 支持 | 支持 | 支持 |
| 模拟看门狗数量 | **4** | **4** | **4** |
| 触发源数量 | 51 | 51 | 51 |
| 外部通道 | 32 | 32 | 32 |
| 外部 MUX 扩展通道 | 32 | 32 | 32 |

- 全芯片共 **96 路标准模拟输入**，另支持经外部 MUX 扩展 **96 路**扩展输入。
- 分辨率最高 **14-bit**，转换结果存入 **16 位宽**数据寄存器。
- 采样率最高 **2 MSa/s**；内置 **bandgap 电压基准通道**（自检算法 S 的被测对象之一）。
- 每实例含 P-SARADC（Plus）与 M-SARADC（Minus）两个 SAR 引擎，差分模式由两者协同完成。

> **通道交错陷阱**：部分 ADC 通道由多个 pad 驱动，具体接哪个 pad 由 `GPR_1.GPR_RWF_0[ADC_CHxx]` 决定（如 `ADC1_X0_P16` 默认走 GPIO 322，可切到 GPIO 240）。改交错等于改硬件拓扑，安全评审时必须与原理图一起冻结。

### 3.2 转换公式与三种启动模式

$$
\text{Digitalcode}=\frac{V_{in}}{(VREFH-VREFL)}\times\left(2^{RESOLUTION}-1\right)
$$

| 模式 | 触发 | 通道选择寄存器 | 行为 |
| --- | --- | --- | --- |
| Normal | 软件 / 硬件 | `NCM0/1/2` | One-Shot 或 Scan（连续循环）；从最低通道号顺序转换到最高 |
| Injected | 软件 / 硬件 | `JCM0/1/2` | **仅 One-Shot**；到达时挂起正在进行的 Normal 链，转完注入链后从挂起点续跑 |
| BCTU | BCTU 硬件 | 由 BCTU 送入通道号 | 单通道转换；结果经数据总线 + `Next command` / `End of conversion` 信号返回；`MC[CTUEN]=1` 使能 |

> Normal 模式下若 `NCMn` 全为 0 却收到启动触发，硬件置位 `IS[ECH]` 并发出 End of Chain 中断 —— 这是"转换链配置丢失"的天然哨兵，建议在安全应用中挂接处理。

### 3.3 平均（Averaging）

- 校准路径：最多 **1024** 次转换平均。
- 输入数据路径：最多 **32** 次转换平均。

平均提高的是有效精度与抗噪能力，属于**精度层**手段；它不能检测 ADC 元件失效，不要与自检混淆。

---

## 4. 校准（Calibration）：精度补偿，不是安全机制

**定位先讲清楚**：校准补偿的是制造偏差与运行环境（温度、供电）变化引起的 **offset / gain / 电容失配**，目标是"准"。ISO 26262 意义上的安全机制要回答的是"坏没坏"，由 Self-Test 承担。两者互补，不可互相替代。

### 4.1 硬件规则（Foundation Training）

- 采样并转换**已知参考电压**，在受控条件下推导 offset、gain、电容失配的校正值。
- **必须作为 SARADC 初始化流程的一部分执行**，否则达不到最佳精度。
- **两种复位对校准的影响截然不同**：
  - **functional reset**：所有寄存器回默认值，**但校准寄存器被保留** —— 无需重校。
  - **destructive reset**：**每次之后必须重新执行校准**。
- 运行期间**工作条件发生变化时**（温度大幅波动、供电变化等），建议重新校准。

### 4.2 RTD 驱动 API

```c
/* 配置期（AutosarExt 容器）：
 *   AdcEnableCalibration = true
 *   AdcEnableAsyncCalibration = true   （可选，异步模式）
 *   AdcCalibrationPrescale             （校准时钟输入选择）
 */
Adc_Init(&AdcConfigSet);        /* 校准不会由 Init 自动启动 */
Adc_Calibrate();                /* 无进行中转换时显式调用 */

/* 异步校准：分两次调用 */
Adc_Calibrate();                /* 第一次：启动校准，随后可执行其他任务 */
/* ... 期间禁止调用除 Adc_DeInit() 外的任何 ADC API ... */
Adc_Calibrate();                /* 第二次：阻塞等待完成并恢复校准占用的寄存器 */
```

> **DET 错误**：`Adc_Calibrate()` 超时返回 `ADC_E_TIMEOUT`（校准操作超时）。
>
> **与自检的耦合**：**一旦启用 Self-Test，必须先执行校准**（Foundation Training 原文："It is mandatory to run calibration procedure if Self-Test is enabled."）。自检算法的期望值是在校准后的器件上定义的，跳过校准会导致自检误报。

---

## 5. Self-Test：三大算法深度解析

SARADC 可自动检查自身元件并置位错误标志。自检的输入不是外部模拟信号，而是**内部已知量**（基准、内部节点），因此是真正独立的评估。

### 5.1 算法总览

| 算法 | 名称 | 被测对象 | 序列特征 |
| --- | --- | --- | --- |
| **S** | Supply Self-Test | Bandgap 电压 `VBG`、供电 `AVDD`、`VREFH`、`VREFL`、`VREFH/2`、`VREFH/3`、`2×VREFH/3` | **7 步原子序列**（atomic，执行期间不可被中断插入正常转换之外的动作） |
| **O** | Offset Self-Test | 比较器失调（Comparator Offset） | 单一序列 |
| **C** | Capacitor Self-Test | 电容阵列：**33 MSB + 17 ISB + 17 LSB**，对 **P-SARADC 与 M-SARADC 各自**执行 | 多步**原子**执行 |

### 5.2 自检模拟看门狗（Self-Test Analog Watchdog）

- 数字接口为**每个算法提供独立的看门狗寄存器组**，判定自检转换结果是否落在该算法的 guard area 内。
- 算法内**每一步转换后**都比较结果与上下门限；越界时：
  - 对应**错误位被置位**；
  - **记录出错的步号**（step number）—— 排障时可直接定位坏在哪一步，而不是只知道"自检挂了"。

### 5.3 自检看门狗定时器（Watchdog Timer）

- 监控自检算法的**执行序列**，验证算法在**安全时间（safe time）**内完成。
- 每个算法有**独立**的看门狗定时器，互不影响。
- 安全时间值编程在 `STBR[WDT]`。
- 计时窗口定义：以算法 S 为例，从 **Step 0 启动（含其间插入的正常链转换）到下一轮 Step 0 再次启动**为一个周期；超时即判序列故障。

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 330" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>SARADC Self-Test 三算法与看门狗结构</title>
<desc>中间为 SARADC 自检引擎，向上分出算法 S（7 步电源测量）、算法 O（比较器失调）、算法 C（MSB/ISB/LSB 电容阵列）三个分支，每个算法配独立看门狗定时器（STBR[WDT] 设定安全时间）与独立自检模拟看门狗（越界置错误位并记录步号），自检错误最终以中断形式上报。</desc>
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="340" y="22" text-anchor="middle" font-size="14" font-weight="500" fill="#2C2C2A">SARADC Self-Test：三算法 + 双看门狗</text>
<rect x="240" y="130" width="200" height="70" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="340" y="155" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">SARADC 自检引擎</text>
<text x="340" y="173" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">内部已知量输入</text>
<text x="340" y="190" text-anchor="middle" font-size="11" fill="#534AB7" dominant-baseline="central">（bandgap / 电容阵列）</text>
<rect x="30" y="40" width="185" height="66" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="122" y="60" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">算法 S · Supply</text>
<text x="122" y="78" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">7 步原子：VBG / AVDD /</text>
<text x="122" y="94" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">VREFH / VREFL / 1/2 / 1/3 / 2/3</text>
<rect x="247" y="40" width="185" height="66" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="340" y="60" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">算法 O · Offset</text>
<text x="340" y="78" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">单一序列</text>
<text x="340" y="94" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">比较器失调</text>
<rect x="465" y="40" width="185" height="66" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="557" y="60" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">算法 C · Capacitor</text>
<text x="557" y="78" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">33 MSB + 17 ISB + 17 LSB</text>
<text x="557" y="94" text-anchor="middle" font-size="11" fill="#185FA5" dominant-baseline="central">P / M 引擎各自原子执行</text>
<path d="M200 73 L240 140" fill="none" stroke="#378ADD" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M340 106 L340 128" fill="none" stroke="#378ADD" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M480 73 L440 140" fill="none" stroke="#378ADD" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="30" y="222" width="185" height="76" rx="8" fill="#FAEEDC" stroke="#BA8A29" stroke-width="0.5"/>
<text x="122" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#433422" dominant-baseline="central">看门狗定时器 ×3</text>
<text x="122" y="260" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">每算法独立，验证序列</text>
<text x="122" y="276" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">在安全时间内完成</text>
<text x="122" y="292" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">STBR[WDT] 设定 safe time</text>
<rect x="247" y="222" width="185" height="76" rx="8" fill="#FAEEDC" stroke="#BA8A29" stroke-width="0.5"/>
<text x="340" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#433422" dominant-baseline="central">自检模拟看门狗 ×3</text>
<text x="340" y="260" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">每算法独立阈值 guard area</text>
<text x="340" y="276" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">逐步比较，越界置错误位</text>
<text x="340" y="292" text-anchor="middle" font-size="11" fill="#633806" dominant-baseline="central">并记录出错步号</text>
<rect x="465" y="222" width="185" height="76" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="557" y="242" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">Self-Test 中断</text>
<text x="557" y="260" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">上报应用层</text>
<text x="557" y="276" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">→ 按故障反应策略</text>
<text x="557" y="292" text-anchor="middle" font-size="11" fill="#5F5E5A" dominant-baseline="central">处置（见第 9 章）</text>
<path d="M122 222 L122 203" fill="none" stroke="#BA8A29" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M340 222 L340 203" fill="none" stroke="#BA8A29" stroke-width="1.5" marker-end="url(#ar)"/>
<path d="M440 165 L500 220" fill="none" stroke="#888780" stroke-width="1.5" marker-end="url(#ar)"/>
</svg>
</figure>

### 5.4 RTD 驱动 API

```c
/* 配置期：AutosarExt 容器 AdcEnableSelfTest = true
 *         AdcSelfTestInputSamplingAlgCVal  默认 24（范围 1–255）
 *         AdcSelfTestInputSamplingAlgSVal  算法 S 测试转换采样相位时长
 */
Adc_SelfTest();   /* 无进行中转换时显式调用；超时返回 ADC_E_TIMEOUT */
```

> `AdcSelfTestInputSamplingConfiguration` 容器定义算法 C / S **测试转换的采样相位时长**，直接影响自检建立的精度 —— 改动前先读 RM 对应章节，不要凭经验拍值。

---

## 6. 模拟看门狗（Analog Watchdog）：运行时数据合理性监控

自检回答"器件坏没坏"，模拟看门狗回答"**这一次转换结果可不可信**"—— 两者时间尺度和覆盖的故障模型完全不同，必须同时使用。

### 6.1 硬件机制

- 每实例 **4 个模拟看门狗**，各自持有上阈 `THRH` 与下阈 `THRL`。
- 所选通道转换完成后，结果与双阈比较，越界产生阈值违例中断：

| `WTIS[WDGnH]` | `WTIS[WDGnL]` | 转换数据 |
| --- | --- | --- |
| 1 | 0 | 数据 > `THRH` |
| 0 | 1 | 数据 < `THRL` |
| 0 | 0 | `THRL` ≤ 数据 ≤ `THRH`（正常） |
| 1 | 1 | `THRH` < 数据 且 `THRL` > 数据（异常组合） |

- 每通道可经 `CWEN` 字段独立使能；经 `CWSEL_n` 选择归属哪个看门狗。

### 6.2 RTD 驱动 API

```c
/* 配置期：AdcEnableWatchdogFunctionality = true
 *         AdcChannel 下 AdcEnableThresholds = true，
 *         指定 AdcThresholdRegister（THRH/THRL）与 AdcWdogNotification
 */
Adc_ConfigureThreshold(/* 运行时改写阈值 */);
Adc_EnableWdgNotification(Channel);   /* 使能通道的看门狗事件通知 */
Adc_DisableWdgNotification(Channel);  /* 关闭 */
```

> ⚠️ **驱动限制（RTD ADC UM §3.5 原文）**："**Watchdog threshold functionality not validated**." —— 阈值看门狗功能在驱动层面**未经充分验证**。若安全案例依赖 AWD，必须在自己的平台上做补充验证与误差分析。
>
> 另两条同节限制：Adc0/Adc1 的 **DMA 功能未经验证**；**LPE_BCTU 在 Design Studio 中不可用**；Cortex-M4 侧中断/DMA 数据传输未经验证。

---

## 7. VCU 加速踏板应用：失效场景与 ADC 侧的额外机制

前六章讲的是"ADC 本身"的机制；本章把它们放进最典型的 ASIL 应用场景里检验 —— **加速踏板（APPS，Accelerator Pedal Position Sensor）**。选它作为试金石有三个原因：

1. **信号链全模拟**：电位器 → 线束 → ADC，应用层软件使不上力，检测责任大量前移到 ADC 与信号调理；
2. **失效即非预期扭矩**：踏板信号错误直接映射到"非预期加速 / 失速"，是 VCU 侧等级最高的安全目标之一（具体等级以项目 HARA 为准，通常 ASIL C/D）；
3. **双路冗余是行业惯例**：APPS1/APPS2 两路电位器把"两路转换结果互相对照"做成了硬性要求，而**两路是否同期采样，是 ADC 配置决定的**。

> 本章聚焦**模拟电位器踏板**。若采用 SENT 等数字传感器，安全机制的一部分（CRC、rolling counter）由传感器侧提供，链路不同，不在本文展开。

### 7.1 应用信号链与安全目标

<figure style="margin:1.2em 0;text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 448" width="100%" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif" role="img">
<title>VCU 加速踏板双路采集链路与失效场景检测映射</title>
<desc>主链路展示加速踏板机构驱动 APPS1/APPS2 双电位器，经线束与信号调理进入 SARADC_0 的 CH0/CH1 同期转换，再到 VCU 软件检查层与扭矩仲裁；下方左右两个面板分别列出 ADC 硬件层机制与 VCU 软件层机制对 F1 至 F10 失效场景的覆盖，最终汇入 limp home 降级与安全状态。</desc>
<defs><marker id="arp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="340" y="22" text-anchor="middle" font-size="13" font-weight="500" fill="#2C2C2A">VCU 加速踏板双路采集链路 —— 失效场景与检测机制映射</text>
<rect x="12" y="62" width="88" height="52" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="56" y="80" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">加速踏板</text>
<text x="56" y="97" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">APPS 机构</text>
<rect x="118" y="45" width="104" height="44" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="170" y="61" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">APPS1 电位器</text>
<text x="170" y="77" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">0.5 V → 4.5 V</text>
<rect x="118" y="97" width="104" height="44" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="170" y="113" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">APPS2 电位器</text>
<text x="170" y="129" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">互补斜率</text>
<rect x="240" y="62" width="88" height="52" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="284" y="80" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">线束 + 调理</text>
<text x="284" y="97" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">上/下拉 · 滤波</text>
<rect x="346" y="55" width="112" height="66" rx="8" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="402" y="80" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">SARADC_0</text>
<text x="402" y="97" text-anchor="middle" font-size="10.5" fill="#185FA5" dominant-baseline="central">CH0/CH1 同期转换</text>
<text x="402" y="112" text-anchor="middle" font-size="10.5" fill="#185FA5" dominant-baseline="central">14-bit · AWD ×4</text>
<rect x="476" y="55" width="92" height="66" rx="8" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="522" y="78" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">VCU 软件检查层</text>
<text x="522" y="95" text-anchor="middle" font-size="10.5" fill="#534AB7" dominant-baseline="central">plausibility · stuck</text>
<text x="522" y="111" text-anchor="middle" font-size="10.5" fill="#534AB7" dominant-baseline="central">gradient · 新鲜度</text>
<rect x="586" y="62" width="82" height="52" rx="8" fill="#F1EFE8" stroke="#888780" stroke-width="0.5"/>
<text x="627" y="80" text-anchor="middle" font-size="12" font-weight="500" fill="#2C2C2A" dominant-baseline="central">扭矩仲裁</text>
<text x="627" y="96" text-anchor="middle" font-size="10.5" fill="#5F5E5A" dominant-baseline="central">电机 / MCU</text>
<path d="M100 78 L116 66" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<path d="M100 98 L116 118" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<path d="M222 70 L238 80" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<path d="M222 116 L238 96" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<path d="M328 88 L344 88" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<path d="M458 88 L474 88" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<path d="M568 88 L584 88" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<rect x="30" y="175" width="280" height="160" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="0.5"/>
<text x="170" y="197" text-anchor="middle" font-size="12" font-weight="500" fill="#0C447C" dominant-baseline="central">ADC 硬件层机制</text>
<text x="44" y="214" font-size="10.5" fill="#185FA5">Self-Test 上电自检 → 元件级故障</text>
<text x="44" y="232" font-size="10.5" fill="#185FA5">AWD 越界 → F3 对地 / F4 对电源短路</text>
<text x="44" y="250" font-size="10.5" fill="#185FA5">　　　　　 F5 开路 / F6 超出量程</text>
<text x="44" y="268" font-size="10.5" fill="#185FA5">Averaging 平均 → F7 信号跳变</text>
<text x="44" y="286" font-size="10.5" fill="#185FA5">scan 背靠背 / BCTU → F8 双路同期</text>
<text x="44" y="304" font-size="10.5" fill="#185FA5">完成中断 / watermark → F9 新鲜度</text>
<text x="44" y="322" font-size="10.5" fill="#185FA5">比率式接线（VREFH 跟踪供电）→ F10</text>
<rect x="370" y="175" width="280" height="160" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.5"/>
<text x="510" y="195" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489" dominant-baseline="central">VCU 软件层机制</text>
<text x="510" y="211" text-anchor="middle" font-size="10" fill="#534AB7" dominant-baseline="central">（应用层，依赖 ADC 新鲜度与同期性）</text>
<text x="384" y="229" font-size="10.5" fill="#534AB7">plausibility 双路一致性 → F2</text>
<text x="384" y="247" font-size="10.5" fill="#534AB7">stuck 卡死监控（死区+时间窗）→ F1</text>
<text x="384" y="265" font-size="10.5" fill="#534AB7">gradient 限幅 + rolling counter → F7/F9</text>
<text x="384" y="283" font-size="10.5" fill="#534AB7">比率式判据 + 周期重校 → F10</text>
<text x="384" y="301" font-size="10.5" fill="#534AB7">零位 boot 检查 · 踏板/制动互斥</text>
<text x="384" y="319" font-size="10.5" fill="#534AB7">降级：limp home 限制扭矩 → 安全状态</text>
<path d="M380 121 L305 173" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<path d="M424 121 L497 173" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<rect x="30" y="362" width="620" height="52" rx="10" fill="#FAEEDC" stroke="#BA8A29" stroke-width="0.5"/>
<text x="340" y="383" text-anchor="middle" font-size="12" font-weight="500" fill="#433422" dominant-baseline="central">故障反应：limp home 降级（限制扭矩 / 怠速）→ 安全状态</text>
<text x="340" y="401" text-anchor="middle" font-size="10.5" fill="#633806" dominant-baseline="central">反应严重度分级与 EOUT / 复位动作见第 10 章 VFCCU；恢复行驶需重新通过 plausibility</text>
<path d="M170 335 L170 360" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<path d="M510 335 L510 360" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arp)"/>
<text x="340" y="436" text-anchor="middle" font-size="10.5" fill="#5F5E5A">主链路为全模拟采集：F1–F10 十个失效场景由 ADC 硬件层与 VCU 软件层机制共同覆盖，两侧缺一不可。</text>
</svg>
</figure>

- 机械踏板驱动**双电位器**：量程通常 0.5 V–4.5 V，两路斜率相反（互补设计，一路 0.5→4.5 V、另一路 4.5→0.5 V），便于交叉校验；
- VCU 以 **5–10 ms 周期**采样两路，解算踏板行程并进入扭矩仲裁；
- 线束上的上拉/下拉电阻不是可选装饰 —— 它决定开路、短路在 ADC 眼里呈现**哪种可区分电平**（见 7.2 的 F5）；
- 安全目标（示例）："防止输出超过驾驶员意图的扭矩"，任何单点失效不得导致该违背。

### 7.2 失效场景清单（FMEA 视角）

| # | 失效场景 | 典型物理成因 | 危险表现 | 主检测层 |
| --- | --- | --- | --- | --- |
| F1 | 信号卡死（stuck） | 电位器导轨磨损、触点氧化、接插件松动 | 踏板位置不跟随物理踏板 | 软件（新鲜度 + 时间窗） |
| F2 | 双路信号不一致 | 一路老化、半断路、EMC 单路受扰 | 两路解算出的扭矩不同 | 软件 plausibility（依赖 ADC 同期采样） |
| F3 | 对地短路 | 线束破损、接插件进水 | 读数 ≈ 0，误判全松 / 全踩 | ADC：AWD |
| F4 | 对电源短路 | 线束与 VBAT/5 V 短接 | 读数 ≈ 满量程 | ADC：AWD |
| F5 | 开路 / 断路 | 焊点开裂、端子退出 | 悬空漂移或被上/下拉钳位 | ADC：AWD + 调理判据 |
| F6 | 超出量程 | 传感器超程、安装错位 | 读数越过物理行程 | ADC：AWD |
| F7 | 信号跳变（spike） | EMC 耦合、地弹、参考纹波 | 单周期尖峰，扭矩抖动 | ADC 平均/滤波 + 软件梯度限幅 |
| F8 | 双路非同期采样 | 两次独立触发、中断抖动 | 快速踩踏板时两路"对不上" | ADC 触发/扫描配置 |
| F9 | 数据陈旧（stale） | DMA 停摆、中断丢失、组未重启 | 用旧位置算扭矩 | 软件新鲜度（依赖 ADC 完成标志） |
| F10 | 地偏移 / 参考漂移 | 单端接线、地弹、供电跌落 | 系统性偏置，零位判据失效 | 比率式接线 + 校准 |

### 7.3 ADC 侧机制映射：每个场景靠什么抓

| 失效 | ADC / 硬件机制 | RTD 驱动落点 | 说明 |
| --- | --- | --- | --- |
| F1 | 周期扫描 + 转换完成标志 / 时间戳 | `Adc_StartGroupConversion` + 组状态查询 | 卡死本质是"该变不变"，先保证采样节拍本身新鲜 |
| F2 | 双通道同期转换：scan 背靠背或 BCTU 单次触发 | `Adc_CtuSetList` + `Adc_CtuStartConversion` | 两路落在同一转换链，时间差微秒级，远小于踏板毫秒级动态 |
| F3 / F4 / F6 | AWD 上下阈越界即判短路 / 超程 | `Adc_ConfigureThreshold` + `Adc_EnableWdgNotification` | 阈值按有效窗 + 余量设定（见 7.4） |
| F5 | AWD + 调理设计：断路读到上拉电平，与短路电平可区分 | 同 AWD | 检测能力一半在信号调理，不在 ADC |
| F7 | Averaging 多采样平均 | 配置项 averaging | 平均服务精度，同时压低尖峰误报 |
| F8 | BCTU 触发源与扫描顺序冻结 | `Adc_CtuSetList` / GPR 交错配置 | 通道交错陷阱见第 3 章；调用序列见第 11 章 |
| F9 | 转换完成中断 / FIFO watermark 作新鲜度锚点 | `Adc_SetupResultBuffer` / `Adc_CtuSetFifoWatermark` | 没有完成事件 = 没有新鲜数据 |
| F10 | 比率式测量：VREFH 跟踪踏板供电 | 硬件接线 | 读数随供电同比缩放，天然抗电源跌落 |
| 全场景 | 上电 Self-Test（算法 S/O/C） | `Adc_SelfTest` | 元件级故障（比较器 / 电容阵列 / 参考）在上电时暴露 |

> 一句话总结：**AWD 保"单路边界"，plausibility 保"两路关系"，Self-Test 保"元件本身"，新鲜度保"数据时效"** —— 四类机制覆盖的是不同故障模型，互相不可替代。

### 7.4 一个可落地的配置示例（SARADC_0）

以下为**示例值**，量产前按传感器数据手册与项目标定确定：

- 分辨率与基准：14-bit，设 `VREFH = 5.0 V`（与踏板传感器供电同源；实际以原理图与 RM 电气特性为准）→ 1 LSB = 5.0 / 2^14 ≈ **0.305 mV**；
- 有效窗 0.5 V–4.5 V → raw ≈ **1638 … 14746**；
- AWD 边界各留 0.1 V 余量：`THRL ≈ 0.4 V`（raw ≈ 1311）、`THRH ≈ 4.6 V`（raw ≈ 15073）—— 越界即短路 / 开路 / 超程，置 DTC 并进入降级；
- 采样链：CH0 = APPS1、CH1 = APPS2 放同一 group，scan 模式**背靠背转换**；或经 BCTU 以 5–10 ms 周期硬件触发，保证确定性节拍；
- 结果缓冲：`Adc_SetupResultBuffer` + streaming（双缓冲），转换完成中断里做 plausibility 与新鲜度检查；
- boot 检查：上电后首组转换，踏板必须处于零位（raw < 死区），否则不允许退出 limp 模式；
- ⚠️ 两个已知限制：AWD 在 RTD 驱动中 **not validated**（第 6 章），Adc0/1 的 DMA 未验证 —— 踏板数据通路建议先用中断模式，DMA 需平台级验证。

### 7.5 软件检查层：ADC 数据质量的"消费者"

以下机制超出 ADC 范畴，但**每一项都依赖 ADC 提供新鲜度与同期性**，列在这里保证链路完整：

- **plausibility**：`|APPS1 − APPS2|` 窗口 + 去抖（示例 100 ms）；
- **stuck**：死区内"长时间不变"判卡死（示例 300–500 ms）；
- **gradient**：单周期变化率限幅（示例：全行程不低于 150–200 ms）；
- **新鲜度**：每控制周期必须有新样本（完成中断 / watermark + 滚动计数），陈旧数据立即降级；
- **互斥**：踏板有效 + 制动有效同时出现即冲突；
- **降级与恢复**：limp home（限制扭矩 / 怠速）→ 安全状态；恢复需重新通过 plausibility。

### 7.6 风险与验证要点

| # | 风险 | 严重度 | 缓解 |
| --- | --- | --- | --- |
| 1 | AWD not validated，踏板越界检测直接进安全案例有缺口 | 🔴 高 | 平台级 AWD 验证 + 软件冗余阈值检查 |
| 2 | 双路采样非同期 → 动态工况 plausibility 误报 / 漏报 | 🔴 高 | scan 背靠背或 BCTU 单次触发双路 |
| 3 | 只配 AWD 不配 plausibility → 两路"各自合理但互相矛盾"漏检 | 🟠 中高 | 双层并行：AWD 保单路，plausibility 保关系 |
| 4 | 断路 / 短路电平设计不当 → F3/F4/F5 不可区分 | 🟠 中高 | 上拉 / 下拉电阻 + 判据表评审 + 台架注入验证 |
| 5 | 踏板线束最长，EMC 尖峰被误判为真实踏板动作 | 🟠 中高 | Averaging + gradient 限幅 + EMC 注入试验 |
| 6 | 未做零位 boot 检查 → 上电时踏板非零位直接输出扭矩 | 🟡 中 | boot-to-safety 序列加零位判据 |
| 7 | 电源跌落未做比率式处理 → 全体读数偏移 | 🟡 中 | VREFH 跟踪供电 + 周期性重校 |

> 注：7.2–7.6 中的门限、时间窗均为**工程惯例示例值**，须按项目 HARA、传感器数据手册与台架标定确定；NXP 文档不覆盖应用层算法，本节的机制映射与风险结论需在项目安全分析中独立确认。

---

## 8. SINC：Σ-Δ 链路的数字保护逻辑

当电流、电压等模拟量经外部 Σ-Δ 调制器进入 S32K5 时，SINC 不只是抽取滤波器 —— 它内置了一组**面向开路/短路/时钟失效的专用检测器**，这是模拟看门狗之外的第二道运行时防线。

### 8.1 数字保护三件套

| 检测器 | 监测对象 | 典型用途 |
| --- | --- | --- |
| **SCD**（Short-Circuit Detector） | 短路（过流）与开路（过压）错误 | 检测执行器驱动/传感器线路故障 |
| **CAD**（Clock-Absence Detector） | 调制器时钟输入缺失 | 时钟树失效时立即暴露，避免滤波器输出静默劣化 |
| **ZCD**（Zero-Cross Detector） | 滤波通道符号翻转 | 过零事件监控（如 PWM 应用） |

- **Break signal 输出**：保护事件发生时直接关断外部器件 —— 硬件级故障遏制，不等软件反应。
- 每通道 16 项 FIFO（带 watermark）、每通道 2 个 DMA 请求、可编程高/低检测限、偏移 bias 补偿、HPF 去直流、支持 Manchester 编码位流、脉冲触发输出。

### 8.2 滤波器与转换模式

- 结构：每通道 1 个 Primary Filter（PF，带 shift 的 CIC，**24-bit 精度**）+ 可选 CIC 子模块 + 可选 HPF/bias/唤醒。
- 阶数：`CnDR[PFORD]=0` 选 **FastSinc**；`>0` 选对应阶数（最高 3 阶）。
- OSR：`CnDR[PFOSR]+1`，最大 **2048**。
- 转换模式（`CnDR[PFCM]`）：

| 模式 | 行为 |
| --- | --- |
| Single（00b） | 每转换需一次触发 |
| Continuous（01b） | 触发后持续转换，下一触发取消并重启 |
| Always（10b） | 触发后持续转换直到被禁用，忽略后续触发 |
| Fixed-Number（11b） | 转换满 `CnCFR[FIFOWMK]` 设定数量后停（`NIS[CHFn]=1`） |

- 转换时间：首个 24-bit 样本 = **ORD × OSR × MOD_CLK 周期**；后续样本每 OSR × MOD_CLK 周期出一个。

> **安全用法建议**：给 SINC 配置 CAD + SCD + 可编程高/低限，等价于给 Σ-Δ 链路补上了"数据合理性 + 线路完整性 + 时钟活性"三项监控；break signal 直接映射到执行器关断路径，延迟最低。

---

## 9. LPCMP 与 TEMPSENSE：低功耗监控搭档

### 9.1 LPCMP（低功耗比较器）

- 3 个实例：`LPE_LPCMP_0/1/2`，每实例 8 路输入通道 + 1 个 8-bit DAC + ANMUX。
- 安全相关能力：可编程滞环、窗口模式（`WINDOW_EN`，仅允许在已知稳定期采样比较器输出，抑制 PWM 类应用的误触发）、输出反相、滤波计数。
- **STANDBY 下的 Round-Robin Trigger 模式**：配合 RTC-API 周期性扫描多路输入并与上次结果比较，**不等则唤醒芯片** —— 这是"睡觉时也不丢监控"的关键机制（仅 continuous 模式；RTC_CLK 仅支持 SIRC/SXOSC）。
- 中断标志：`CSR[CFR]` 下降沿、`CSR[CFF]` 上升沿、`CSR[RRF]` round-robin 周期完成。

### 9.2 TEMPSENSE（片内温度传感）

- 结构：BJT 传感器 + Σ-Δ ADC + 抽取滤波器 + **校准引擎**；数字输出直接以 °C 表示。
- 模式：Single One-Shot / Periodic One-Shot（测量间自动休眠，可编程间隔）/ Low-Power。
- **阈值比较器同时位于 normal 与 secure 地址空间**，支持方向与阈值编程，多级阈值覆盖**欠温 / 过温 / panic**；结束测量与阈值违例均有中断和状态位。
- 数字格式：`DATAn[DATA_VAL]` 为 16-bit 有符号数，低 6 位为小数位 —— 例：`0000_0110_0101_0000` = **+25.25 °C**，`1111_1001_1011_0000` = **−25.25 °C**（二进制补码）。

> **过温即系统性风险**：S32K5 的 fault reaction 分级中，"SoC out-of-context local"一类的例子正是过温 —— TEMPSENSE 的 panic 阈值建议直接接入主安全核的故障处理路径，而不是仅做日志。

---

## 10. 从故障到安全状态：VFCCU 反应分级与 SAF 软件栈

ADC 自检错误、看门狗违例、SINC 检测器事件，最终都要汇入芯片的故障管理单元（FMU）才能变成**受控动作**。

### 10.1 故障反应分级（Foundation Training: Safety）

| 反应类型 | 名称 | 故障影响 | EOUT | 反应所有者 | 升级路径 |
| --- | --- | --- | --- | --- | --- |
| Transparent | 透明 | 被观测元件 | 不置位 | 安全机制自身 | 无（如 ECC 单位纠错） |
| R1 | 应用内本地 | 限于应用及其资源 | 不置位 | 受影响应用 | 告警中断 → 全局软件 |
| R1 | 应用外本地 | 可能影响全芯片/共享资源 | 不置位 | 主安全核 | 告警中断 → 全局硬件 |
| R1 | SoC 上下文本地 | 共享外设/共享内存类 | 不置位 | 受影响应用（分布式） | 告警中断 → 全局软件 |
| R1 | SoC 外上下文本地 | 过温等系统性故障 | 不置位 | 主安全核 | 由片外安全硬件观测 |
| R2 | 全局软件 | 全芯片 | **置位** | 主安全核 | 故障中断（如 ECC 多位错误） |
| R3 | 全局硬件 | 全芯片 | **置位** | RGM | 复位（如 EDC gasket / XBIC 错误） |

- R1 四类若在告警/升级超时窗口内未完成恢复，**自动升级**。
- **VFCCU 规模**：5 个 LVFCCU（本地汇聚）+ 1 个 CVFCCU（中央管理），最多 **8 类反应**经 **27 个反应输出**，EOUT 支持 **7 种引脚模式**（Input-Only / Push-Pull / Open-Drain / Open-Collector / Bistable / Fault-Toggle / Time Switch）。
- 每条故障输入的推荐立即/延迟反应以 RM 附件 **fault map** 为准（`S32K5xx_fault_map.xlsx`）。

### 10.2 Boot-to-Safety：安全上下文在此建立

上电后主安全启动核依次：检查安全机制是否按预期工作 → 启动芯片 BIST 检测潜在永久故障 → 检查安全配置（所需机制已使能且配置正确）。全部通过才进入 Normal Operation；任一失败，由应用决定降级模式或进入安全状态。**ADC 的首次自检与校准应纳入 boot-to-safety 序列。**

### 10.3 安全软件栈（SAF / SPD / SCST）

| 组件 | 作用 |
| --- | --- |
| **SPD**（Safety Peripheral Drivers） | `Bist` + `eMcem`（Extended Microcontroller Error Manager）两个安全外设驱动，AUTOSAR 与非 AUTOSAR 环境均适用 |
| **SAF**（Safety Framework） | 6 组件：Bist、eMcem、mSel（Mode Selector）、sBoot、**sCheck**（周期性平方校验）、sReco（软件恢复） |
| **SCST**（Structural Core Self-Test） | 运行时检测处理器核永久故障，诊断覆盖度 **90%**，覆盖 M4/M7/R52 |

> **软件侧的周期性策略**：sCheck 提供周期性校验框架，ADC 的 `Adc_Calibrate()` + `Adc_SelfTest()` 应按安全分析确定的周期挂入其中；自检结果（错误位 + 步号）纳入 eMcem 的诊断信息一并记录。

---

## 11. RTD ADC 驱动：安全相关配置与调用时序

### 11.1 配置项清单（AutosarExt）

| 参数 | 作用 | 备注 |
| --- | --- | --- |
| `AdcEnableSelfTest` | 使能 `Adc_SelfTest()` API | 安全应用必开 |
| `AdcEnableCalibration` | 使能 `Adc_Calibrate()` API | **启用自检则必须执行校准** |
| `AdcEnableAsyncCalibration` | 异步校准（两次调用） | 校准期间不得调用其他 ADC API |
| `AdcCalibrationPrescale` | 校准时钟输入选择 | — |
| `AdcSelfTestInputSamplingAlgCVal` | 算法 C 采样相位时长 | 默认 24，范围 1–255 |
| `AdcSelfTestInputSamplingAlgSVal` | 算法 S 采样相位时长 | 同上 |
| `AdcEnableWatchdogFunctionality` | 模拟看门狗总开关 | 预编译期移除相关代码 |
| `AdcEnableThresholds` / `AdcThresholdRegister` / `AdcWdogNotification` | 通道级阈值与通知 | 每通道独立 |

### 11.2 推荐调用序列

```text
上电 / boot-to-safety
   │
   ▼
Adc_Init(&AdcConfigSet)              ── 失败：ADC_E_TIMEOUT（硬件无法进入 power-down/idle）
   │
   ▼
Adc_Calibrate()                      ── 补偿 offset/gain/电容失配
   │                                    functional reset 后不必重跑；
   │                                    destructive reset 后必须重跑
   ▼
Adc_SelfTest()                       ── 算法 S / O / C + 双看门狗
   │                                    超时：ADC_E_TIMEOUT
   ▼
┌─ 正常运行 ─────────────────────────────────────┐
│ Adc_StartGroupConversion(Group)                │
│   ├─ Normal / Injected / BCTU 模式              │
│   ├─ 模拟看门狗实时监控（AWD 中断 → notification）│
│   └─ SINC 链路：SCD / CAD / ZCD + break signal   │
│ Adc_StopGroupConversion(Group)                 │
└────────────────────────────────────────────────┘
   │
   ▼
条件变化（温度剧变 / destructive reset）→ 回到 Adc_Calibrate()
```

### 11.3 DET 运行时错误速查

| 函数 | 错误码 | 触发条件 |
| --- | --- | --- |
| `Adc_Init()` / `Adc_DeInit()` | `ADC_E_TIMEOUT` | ADC 硬件无法进入 power-down / idle |
| `Adc_StartGroupConversion()` / `Adc_StopGroupConversion()` | `ADC_E_TIMEOUT` | 进行中的转换无法中止 |
| `Adc_SetHwUnitPowerMode()` | `ADC_E_TIMEOUT` | 设置电源模式超时 |
| `Adc_Calibrate()` | `ADC_E_TIMEOUT` | 校准操作超时 |
| `Adc_SelfTest()` | `ADC_E_TIMEOUT` | 自检操作超时 |
| `Adc_SetClockMode()` | `ADC_E_UNINIT` / `ADC_E_INVALID_CLOCK_MODE` / `ADC_E_TIMEOUT` | 全局指针为空 / 时钟模式非法 / 超时 |

---

## 12. 设计检查清单与风险登记

### 12.1 检查清单

- [ ] ADC 实例选型确认电源域：LPRUN 场景仅 LPE_SARADC 可用（PD1），主域 SARADC_0/1 随 PD2 关断
- [ ] boot-to-safety 序列包含：`Adc_Init` → `Adc_Calibrate` → `Adc_SelfTest`，且首结果入库
- [ ] destructive reset 处理流程中安排了重新校准（functional reset 不需要）
- [ ] 自检启用即校准的前提条件已在配置中固化（`AdcEnableCalibration` + `AdcEnableSelfTest` 同开）
- [ ] `STBR[WDT]` 安全时间与自检周期匹配（Step0 到下一轮 Step0 的完整窗口）
- [ ] 自检模拟看门狗错误位 + 步号已接入诊断记录（排障可定位到步）
- [ ] 模拟看门狗 THRH/THRL 按信号量程设置，`AdcWdogNotification` 已挂处理函数
- [ ] AWD 驱动未验证的限制已在项目安全分析中显式记录并安排平台验证
- [ ] SINC 通道 CAD / SCD / ZCD 已使能，break signal 接入执行器关断路径
- [ ] TEMPSENSE panic 阈值接入主安全核故障处理（而非仅日志）
- [ ] 通道交错（GPR_RWF_0）配置与原理图一致并冻结
- [ ] Normal 模式空链（`NCMn=0`）的 `IS[ECH]` 中断已挂接（配置丢失哨兵）
- [ ] 温度/供电大幅变化的运行场景安排了周期性重校（重校期间无正常转换）
- [ ] 加速踏板双路通道置于同一 group：scan 背靠背或 BCTU 单次触发，两路采样时间差远小于踏板动态（微秒级 vs 毫秒级）
- [ ] 踏板通道 AWD 阈值按有效窗 + 余量设定（示例：0.5–4.5 V 窗，0.4 V / 4.6 V 越界），越界即置 DTC 并降级
- [ ] 上拉/下拉电阻设计使 F3 对地短路 / F4 对电源短路 / F5 开路呈现可区分电平，台架逐条注入验证
- [ ] VREFH 跟踪踏板传感器供电（比率式接线），电源跌落场景读数同比缩放
- [ ] boot-to-safety 增加零位检查：上电首组转换踏板必须处于零位，否则不允许退出 limp 模式
- [ ] 每控制周期必须有新鲜样本（转换完成中断 / FIFO watermark + 滚动计数），陈旧数据立即降级
- [ ] plausibility 双路一致性窗口与去抖时间、stuck 死区时间窗、gradient 变化率限幅均按 HARA 标定并冻结
- [ ] limp home 降级策略（限制扭矩）与恢复条件（重新通过 plausibility）已在安全状态机中定义

### 12.2 风险登记

| # | 风险 | 严重度 | 依据 |
| --- | --- | --- | --- |
| 1 | 启用 Self-Test 却跳过校准 → 自检误报，安全机制被"狼来了"废掉 | 🔴 高 | Foundation Training：自检启用的前提是已校准 |
| 2 | destructive reset 后未重校 → 全部后续转换带着错误 offset | 🔴 高 | functional reset 保留校准寄存器，destructive reset 不保留 |
| 3 | 自检/校准期间仍有进行中转换 → API 报错或功能不执行，静默失去保护 | 🔴 高 | RTD UM：调用前提是 no ongoing conversions |
| 4 | 模拟看门狗功能在 RTD 驱动中 **not validated**，直接用于安全案例有缺口 | 🔴 高 | RTD ADC UM §3.5 Driver Limitations |
| 5 | LPRUN 下错用主域 SARADC → 休眠策略与监控需求互相打架 | 🟠 中高 | 电源域表（推导，需 RM 复核） |
| 6 | Adc0/Adc1 DMA 未验证，安全数据通路若依赖 DMA 需补充验证 | 🟠 中高 | RTD ADC UM §3.5 |
| 7 | 通道交错 GPR 配置与原理图不一致 → 采到的不是想采的 pad | 🟠 中高 | Foundation Training：interleaving 表 |
| 8 | 自检安全时间 `STBR[WDT]` 配得过紧 → 正常链转换插入导致误超时 | 🟡 中 | 安全时间窗口含间插的正常链转换 |
| 9 | 异步校准期间调用其他 ADC API → 返回错误或静默不执行 | 🟡 中 | RTD UM：仅允许 `Adc_Deinit()` |
| 10 | SINC Manchester 编码/HPF/bias 配置错误 → 抽取结果系统性偏移 | 🟡 中 | Foundation Training：均为可选功能，需按调制器数据手册配置 |
| 11 | TEMPSENSE 仅接日志未接反应 → 过温事件无故障遏制 | 🟡 中 | Fault reaction 分级：过温属 SoC out-of-context local |
| 12 | LPE_BCTU 在 Design Studio 不可用，工具链方案需提前确认 | 🟡 低 | RTD ADC UM §3.5 |
| 13 | 踏板双路采样非同期 → 动态工况 plausibility 误报 / 漏报 | 🔴 高 | scan 背靠背或 BCTU 单次触发双路（第 7 章 F2/F8） |
| 14 | 只配 AWD 未配 plausibility → 两路各自合理但互相矛盾时漏检 | 🟠 中高 | 双层并行：AWD 保单路边界，plausibility 保两路关系 |
| 15 | 踏板线束最长，EMC 尖峰被误判为真实踏板动作 | 🟠 中高 | Averaging + gradient 限幅 + EMC 注入试验 |

---

## 13. 参考资料

1. NXP S32K5 Foundation Training —— *Analog: SARADC, SINC, LPCMP, TEMPSENSE*（AAES AMCU Systems and Applications；基于 S32K5RM Rev2 DraftE / S32K5xx DS Rev1 DraftE）
2. NXP S32K5 Foundation Training —— *Safety*（同上）
3. NXP *S32K5xx Reference Manual*, Rev.2（2026-06-01），Chapter 63 *Safety Overview*（§63.4.2 specific BIST / §63.5 boot-to-safety / §63.7 BIST）
4. NXP *S32K5xx Safety Manual*（SEooC 安全概念、assumptions of use、fault map 附件）
5. NXP *User Manual for S32K5 ADC Driver*（RTD，UM85ADCASRR23-11）—— §3.6.2 Calibration / §3.6.3 Self-Test / §3.6.13 Analog Watchdog / §3.7 Runtime errors / §3.5 Driver Limitations
6. 本目录关联文章：[S32K5_R52_M7_Sleep_Design_CN.md](../power_designs/S32K5_R52_M7_Sleep_Design_CN.md)、[S32K5_R52_M7_MPU_Design_CN.md](../mpu_concept/S32K5_R52_M7_MPU_Design_CN.md)

> 本文所有寄存器名、位域与默认值均来自上述公开培训与文档；量产前必须与对应型号的正式 Reference Manual 及 Safety Manual 逐条核对，并以项目自身的 HARA/FSC 结论为准。
