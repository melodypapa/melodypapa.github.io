---
title: "AUTOSAR Diagnostic Event Manager（诊断事件管理器）"
spec: AUTOSAR_CP_SWS_DiagnosticEventManager
release: R23-11
---

## 1. 简介和功能概述

诊断事件管理器 (**Dem**) 服务组件，主要负责处理和存储诊断事件（错误）以及与其相关数据。此外 **Dem** 还需向 **Dcm** 提供故障信息，（例如：从事件内存中读取所有存储的 **DTC**）。**Dem** 也需提供与应用层和其他 **BSW** 模块的接口。

**Dem** 规范文档的基本目标是为汽车制造商和组件供应商定义《诊断故障内存》（**diagnostic fault memory**）通用方法的能力。

本规范定义了 AUTOSAR 基本软件模块诊断事件管理器 (Dem) 的功能、**API** 和配置。部分内部行为是制造商特定的，并在**限制**一章中进行了详细描述。

## 2. 缩略语

以下术语表包含与 **Dem** 模块相关、且未包含在 [4] AUTOSAR 词汇表中的首字母缩略词和缩写。

### 2.1. 首字母缩略词（Acronyms）

**激活模式 1（Activation Mode 1）**
> 无故障（**Absence of malfunction**）——**MIL** 应闪烁一次。

**激活模式 2（Activation Mode 2）**
> "on-demand-MI"——如果 **OBD** 系统根据判别式显示策略（**discriminatory display strategy**）要求 on-demand-MI，则 **MIL** 应闪烁两次。

**激活模式 3（Activation Mode 3）**
> "short-MI"——如果 **OBD** 系统根据判别式显示策略要求 short-MI，则 **MIL** 应闪烁三次。

**激活模式 4（Activation Mode 4）**
> "continuous-MI"——如果 **OBD** 系统根据判别式显示策略要求 continuous-MI，则 **MIL** 应持续点亮（"continuous-MI"）。

**老化（Aging）**
> 在定义数目的运行周期之后，从事件内存中淘汰/删除不再失败的事件/**DTC**。

**老化计数器（Aging Counter）**
> "Aging Counter"、"Aging Cycle Counter" 或 "DTC Aging Counter" 指定用于执行老化的计数器。它统计直到事件/**DTC** 从事件内存中移除为止的运行周期数。

**Class B1 计数器（Class B1 counter）**
> **Class B1** 故障被确认（**Confirmed**）且处于 **TestFailed** 期间所运行的发动机小时数。

**组合 DTC（Combined DTC）**
> 普通 **DTC**，但被多个监视器报告的多个事件所引用（例如 **ECU** 缺陷，由不同的硬件缺陷组成）。

**Continuous-MI 计数器（Continuous-MI counter）**
> continuous-MI 被要求点亮期间发动机运行的小时数。

**累计 Continuous-MI 计数器（Cumulative Continuous-MI counter）**
> 在其寿命期内 **MI** 被持续要求点亮所累计运行的发动机小时数。

**去抖动计数器（Debounce counter）**
> 用于基于计数器的去抖动算法的内部计数器。

**DemComponent / 受监控组件（Monitored Component）**
> 受监控组件是系统的一部分，由一个或多个监控检查其是否正常运行。（参见第 6.5 节）

**Dem 内部数据值（Dem-internal data value）**
> 某些数据值（例如发生计数器）由 **Dem** 模块在内部自行计算。

**分母（Denominator）**
> 特定监视器 m 的分母（Denominator<sub>m</sub>）是一个计数器，表示车辆行驶事件的次数，并考虑特定于该监视器的条件。

**从属/辅助 ECU（Dependent / Secondary ECUs）**
> 从属/辅助 **ECU**（dep. / sec.）始终与主 **ECU**（**Master** 或 **Primary**）相关联。

**有向无环图（Directed acyclic graph）**
> 无循环依赖的依赖关系图。

**置换（Displacement）**
> 用需要存储的更重要的事件内存条目替换最不重要的事件内存条目。

**DTC 组（DTC group）**
> 唯一标识一组 **DTC**。DTC 组被映射到有效 **DTC** 的取值范围内。通过提供一个 DTC 组，即表示对该组中的所有 **DTC** 请求某一操作。DTC 组的定义由 ISO 14229-1 给出，并且是 **OEM**/供应商特定的。

**DtcGroupAllDtcs**
> 所有已配置 **DTC** 的分组（表示为 0xFFFFFF）。

**事件组合（Event combination）**
> 事件组合是一种将多个事件合并为一个特定组合 **DTC** 的方法。它用于将不同的监视结果适配为一个明确的、可在维修站评估的故障。

**事件去抖动（Event debouncing）**
> 去抖动是一种特定的机制（例如基于计数器的），用于评估诊断事件是否合格。它在潜在的信号去抖动之上工作，可以在 **SW-C** 内部或 **Dem** 内部完成。

**事件确认（Event confirmation）**
> 在通过故障确认计数器评估出多个周期或时间内重复检测到合格事件的情况下，诊断事件被确认。因此，也会置位 **UDS** 状态位 3（**ConfirmedDTC**）。

**事件内存（Event memory）**
> 事件内存（例如主内存，**Primary memory**）由多个事件内存条目组成。

**事件内存条目（Event memory entry）**
> 事件内存条目是用于一个事件及其事件相关数据的单个存储容器。事件内存条目被动态地分配给特定事件。

**事件内存溢出指示（Event memory overflow indication）**
> 事件内存溢出指示用于指示该特定事件内存已满且下一个待存储的事件发生。

**事件鉴定（Event qualification）**
> 在置位通过（**passed**）或失败（**failed**）结果时（由 **Dem** 内部或另一个 **BSW** 模块或 **SW-C** 报告），诊断事件即合格。

**事件相关数据（Event related data）**
> 事件相关数据是与事件一起存储在事件内存中的附加数据，例如传感器值或时间戳/里程。ISO 定义了两种类型的事件相关数据：冻结帧（快照记录，**snapshot records**）和扩展数据（**extended data**）。

**事件状态字节（Event status byte）**
> 基于**事件**层级的、按 ISO 14229-1 定义的状态字节。

**扩展数据记录（Extended data record）**
> 扩展数据记录是存储与故障相关的特定信息的记录。

**失败计数器（Failure counter）**
> 失败计数器表示 ISO 14229-1 中的 **Trip Counter**。Trip Counter 统计发生故障的运行周期（驾驶循环）数。如果计数器达到阈值（例如 2 个驾驶循环），confirmed 位从 0 变为 1。

**故障检测计数器（Fault Detection Counter）**
> ISO 和 **FDC** API 中使用的 **sint8** 值。

**冻结帧（Freeze frame）**
> 冻结帧定义为一条数据记录（**DID**/**PID**）。冻结帧与 ISO 14229-1 中的 **SnapShotRecords** 相同。

**通用分母（General Denominator）**
> 通用分母是一个计数器，表示车辆运行的次数，并考虑一般性条件。

**恢复（Healing）**
> 在一段时间/多个运行周期内对报告的通过结果进行处理，包括关闭警告指示器。

**实际使用性能比（In-Use performance ratio）**
> **OBD** 系统中特定监视器 m 的实际使用性能比（**IUPR**）为：IUPRm = Numerator<sub>m</sub> / Denominator<sub>m</sub>

**主 ECU（Master ECU）**
> 作为主 **ECU**，**Master ECU** 在其事件内存中存储"自己的"以及相关的从属/辅助 **ECU** "报告的错误"。此外，**Master** 必须履行特殊的 **Master** 任务，如 **MIL Master** 或提供"通用分子"信息。

**监视器（Monitor）**
> 诊断监视器是确定组件是否正常运行的例程实体。也可以使用术语"诊断功能"（**diagnostic function**）。

**分子（Numerator）**
> 特定监视器 m 的分子（Numerator<sub>m</sub>）是一个计数器，表示车辆运行的次数，使得该特定监视器检测故障所需的所有监控条件都已得到满足。

**NvM is marked for NvM_WriteAll**
> **Dem** 已调用 NvM_SetRamBlockStatus() 将相应的 **NvM** 块设置为待由 NvM_WriteAll() 写入。

**运行周期（Operating cycle）**
> "运行周期"（**operation cycle**）是事件鉴定以及 **Dem** 调度（例如点火钥匙 off-on 循环、驾驶循环等）的基础。

**OBD**
> 车载诊断（**On-Board Diagnostics**），**OBD** 是指车辆自诊断和报告能力的通用术语。OBD 系统使车辆所有者或维修技术人员能够访问各种车辆子系统的健康状态信息。

**OBD ECU（OBD ECUs）**
> "一辆车中可以有 3 种不同类型的 OBD ECU：• **Master ECU**（每车一个）• **Primary ECU**（每车多个）• **Dependent / Secondary ECU**（每车多个）"

**OBD UDS DTC 分离（OBD UDS DTC separation）**
> 该功能针对基于 SAE J1979-2 的 **UDS** 通信所报告的 3 字节 **DTC** 编号，与针对非 J1979-2 UDS 通信所报告的不同。

**P-Code**
> 动力总成代码（**Power train code**）。

**PFC 循环（PFC cycle）**
> 永久故障代码（**Permanent fault code**）——驾驶循环（**OBD** 术语）。

**来自 NvM 的肯定回调（Positive Callback from NvM）**
> 如果需要在 Dem_Init 和 Dem_Shutdown 之间存储数据，**Dem** 模块应使用 **NVRAM** 管理器的 API NvM_WriteBlock 和 NvM_GetErrorStatus。此外，API NvM_GetErrorStatus 应等待写入块成功完成的肯定响应。

**PossibleErrors**
> PossibleErrors 表示元模型中定义的 **ApplicationErrors**。

**主 ECU（Primary ECU）**
> **Primary ECU** 在其事件内存中存储"自己的"以及相关的从属/辅助 **ECU** 的"报告的错误"。

**RBM 循环（RBM cycle）**
> **OBD** 术语：通用分子/基于比率的监控（**Rate-based monitoring**）——驾驶循环。

**就绪（Readiness）**
> 就绪 refers 指 **UDS** 状态字节的 **TestNotCompletedSinceLastClear**（位 4）和 **TestNotCompleteThisOperationCycle**（位 6）两个已测试位。

**已触发至 NvM（Triggered to NvM）**
> 如果需要在 Dem_Init 和 Dem_Shutdown 之间触发数据存储，**Dem** 模块应使用 **NVRAM** 管理器的 API NvM_WriteBlock。此外，如果请求已被接受，**Dem** 模块应等待 NvM_WriteBlock 的肯定响应。

**UDS 状态位 0（UDS status bit 0）**
> **UDS** 状态字节的 **testFailed** 位。表示最近执行的测试的结果。

**UDS 状态位 1（UDS status bit 1）**
> **UDS** 状态字节的 **testFailedThisOperationCycle** 位。表示诊断测试在当前运行周期内是否曾报告 **testFailed** 结果。

**UDS 状态位 2（UDS status bit 2）**
> **UDS** 状态字节的 **pendingDTC** 位。表示诊断测试在当前或上一个已完成的运行周期内是否曾报告 **testFailed** 结果。

**UDS 状态位 3（UDS status bit 3）**
> **UDS** 状态字节的 **confirmedDTC** 位。表示故障被检测到的次数是否足以使该 **DTC** 需要存储在长期内存中。

**UDS 状态位 4（UDS status bit 4）**
> **UDS** 状态字节的 **testNotCompletedSinceLastClear** 位。表示自上次调用 ClearDiagnosticInformation 以来 **DTC** 测试是否曾运行并完成。

**UDS 状态位 5（UDS status bit 5）**
> **UDS** 状态字节的 **testFailedSinceLastClear** 位。表示自上次调用 ClearDiagnosticInformation 以来 **DTC** 测试是否曾以失败结果完成。

**UDS 状态位 6（UDS status bit 6）**
> **UDS** 状态字节的 **testNotCompletedThisOperationCycle** 位。表示 **DTC** 测试在当前运行周期内是否曾运行并完成。

**UDS 状态位 7（UDS status bit 7）**
> **UDS** 状态字节的 **warningIndicatorRequested** 位。报告与特定 **DTC** 关联的任何警告指示器的状态。

**UDS 状态字节（UDS status byte）**
> 基于 **DTC** 层级的、按 ISO 14229-1 定义的状态字节。

### 2.2. 缩写（Abbreviations）

**API**
> 应用编程接口（**Application Programming Interface**）。

**BSW**
> 基础软件（**Basic Software**）。

**CDD**
> 复杂设备驱动（**Complex Device Driver**）。

**CRC**
> 循环冗余校验（**Cyclic Redundancy Check**）。

**Dcm**
> 诊断通信管理器（**Diagnostic Communication Manager**）。

**Dem**
> 诊断事件管理器（**Diagnostic Event Manager**）。

**Det**
> 默认错误跟踪器（**Default Error Tracer**）。

**DID**
> 数据标识符（**Data Identifier**）。

**DTC**
> 诊断故障代码（**Diagnostic Trouble Code**）。

**DTR**
> 诊断测试结果（**Diagnostic Test Result**）。

**DYC**
> **OBD** 术语：驾驶循环（**Driving Cycle**）。

**ECU**
> 电子控制单元（**Electronic Control Unit**）。

**EcuM**
> 电子控制单元管理器（**Electronic Control Unit Manager**）。

**FDC**
> 故障检测计数器（**Fault Detection Counter**）。

**Fim**
> 功能抑制管理器（**Function Inhibition Manager**）。

**FMI**
> 故障模式指示器（**Failure Mode Indicator**，SAE J1939）。

**FTB**
> 故障类型字节（**Failure Type Byte**）。

**HW**
> 硬件（**Hardware**）。

**ID**
> 标识/标识符（**Identification/Identifier**）。

**ISO**
> 国际标准化组织（**International Standardization Organization**）。

**IUMPR**
> 实际使用监控性能比（**In Use Monitoring Performance Ratio**，**OBD** 术语）。

**J1939Dcm**
> SAE J1939 诊断通信管理器（**SAEJ1939 Diagnostic Communication Manager**）。

**MIL**
> 故障指示灯（**Malfunction Indicator Light**，SAE J1979）或故障指示灯（**Malfunction Indicator Lamp**，SAE J1939）。

**NVRAM**
> 非易失性 RAM（**Non volatile RAM**）。

**OBD**
> 车载诊断（**On-Board-Diagnostics**）。

**OC**
> 发生计数（**Occurrence Count**，SAE J1939）。

**OEM**
> 原始设备制造商（汽车制造商）（**Original Equipment Manufacturer**）。

**OS**
> 操作系统（**Operating System**）。

**PID**
> 参数标识（**Parameter Identification**，SAE J1587 或 SAE J1979）。

**PTO**
> 动力输出（**Power Take Off**）。

**RAM**
> 随机存取存储器（**Random Access Memory**）。

**ROM**
> 只读存储器（**Read-only Memory**）。

**RTE**
> 运行时环境（**Runtime Environment**）。

**SPN**
> 疑似参数编号（**Suspect Parameter Number**，SAE J1939）。

**SSCP**
> 同步服务器调用点（**synchronous server call point**）。

**SW**
> 软件（**Software**）。

**SW-C**
> 软件组件（**Software Component**）。

**UDS**
> 统一诊断服务（**Unified Diagnostic Services**）。

**VOBD**
> 车载诊断（**Vehicle On-Board-Diagnostic**）。

**WUC**
> **OBD** 术语：暖机循环（**Warm up cycle**）。

**WIR**
> 警告指示器请求（**Warning Indicator Request**）。

**WWH-OBD**
> 全球统一车载诊断（**World Wide Harmonized On-Board-Diagnostic**）。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

- [1] Unified diagnostic services (UDS) - Part 1: Specification and requirements (Release 2006-12) https://www.iso.org
- [2] Unified diagnostic services (UDS) - Part 1: Application layer (Release 2013-03) https://www.iso.org
- [3] Road vehicles - Implementation of World-Wide Harmonized On-Board Diagnostics (WWH-OBD) communication requirements - Part 1: General information and use case definition https://www.iso.org
- [4] Glossary AUTOSAR_FO_TR_Glossary
- [5] Specification of NVRAM Manager AUTOSAR_CP_SWS_NVRAMManager
- [6] General Specification of Basic Software Modules AUTOSAR_CP_SWS_BSWGeneral
- [7] Specification of a Diagnostic Communication Manager for SAE J1939 AUTOSAR_CP_SWS_SAEJ1939DiagnosticCommunicationManager
- [8] Requirements on Function Inhibition Manager AUTOSAR_CP_SRS_FunctionInhibitionManager
- [9] Specification of Diagnostic Communication Manager AUTOSAR_CP_SWS_DiagnosticCommunicationManager
- [10] Requirements on Diagnostics AUTOSAR_FO_RS_Diagnostics
- [11] General Requirements on Basic Software Modules AUTOSAR_CP_SRS_BSWGeneral
- [12] Road vehicles - Communication between vehicle and external equipment for emission-related diagnostic - Part 5: Emission-related diagnostic services. https://www.iso.org
- [13] SAE J2012-DA Digital
- [14] SAE J1939-73 Application Layer - Diagnostics
- [15] Road vehicles - Interchange of digital information on electrical connections between towing and towed vehicles - Part 4: Diagnostic communication https://www.iso.org
- [16] Unified diagnostic services (UDS) - Part 1: Application layer (Release 2020-02) https://www.iso.org
- [17] ISO 17356-3: Road vehicles - Open interface for embedded automotive applications - Part 3: OSEK/VDX Operating System (OS)
- [18] SAE J1979
- [19] SAE J1979-DA Digital Annex of E/E Diagnostic Test Modes
- [20] Title 13, California Code Regulations, Section 1971.1, On-Board Diagnostic System Requirements for 2013 and Subsequent Model-Year Heavy-Duty Engines (HD OBD)
- [21] Title 13, California Code Regulations, Section 1968.2, Malfunction and Diagnostic System Requirements for 2004 and Subsequent Model-Year Passenger Cars, Light-Duty Trucks, and Medium-Duty Vehicles and Engines (OBD II) (Biennial Review MY08-11) [http://www.arb.ca.gov/regact/obdii06/19682clean.pdf](http://www.arb.ca.gov/regact/obdii06/19682clean.pdf)
- [22] Road vehicles - Implementation of World-Wide Harmonized On-Board Diagnostics (WWH-OBD) communication requirements - Part 3: Common message dictionary https://www.iso.org
- [23] Software Component Template AUTOSAR_CP_TPS_SoftwareComponentTemplate
- [24] Diagnostic Extract Template AUTOSAR_CP_TPS_DiagnosticExtractTemplate

### 3.2. 相关规范

AUTOSAR 提供的基础软件模块通用规范 [6, SWS BSW General] 同样适用于诊断事件管理器。

因此，SWS BSW General 规范应被视为诊断事件管理器的附加且必需的规范。

## 4. 约束和假设

Dem 中定义的一些同步 **API** 调用可能需要可变的时间才能完成。因此，在系统配置中必须考虑这一可变时间。

每个 **ECU** 只能有一个 **Dem** 模块可用。

**Dem** 可以拥有多个不同的事件内存分区。**DTC** 到相应分区的映射通过参数 **DTC Origin** 完成。特定 **ECU** 的 **Dem** 只能由位于同一 **ECU** 内的软件组件访问。

### 4.1. 限制

必须针对整个 **ECU** 考虑时序约束。如果对 **Dem** 的响应速度有明确要求、且高于 **Dem** 基本循环时间，则必须实施本 AUTOSAR 文档未规定的特殊措施。在具有大量事件的 **ECU** 中尤其如此。

与**事件**和 **DTC** 状态变化相关的回调在极少数情况下不是确定性的，因此不应用于安全相关的用例。考虑 ISO 14229-1 中的一般性声明：不建议将 **DTC** 状态与失效安全策略（**failsafe strategies**）相关联。

**SWS** 中缺少对 **Dem** 与 **SW-C** 交互期间由 **RTE** 报告的基础设施错误（**infrastructure errors**）的处理，如果实现者需要，可能必须将其考虑在内。

**Dem** 能够支持额外的事件内存（永久内存和用户自定义内存），但具体的事件内存处理未作详细定义。

本规范未定义 **Dem** 与特定排放相关 **SW-C** 之间交互的一些细节，因为它们依赖于 **SW-C** 的实现。以下功能未定义：

- **故障指示灯（MIL）**的激活（MIL 处理器与 **Dem** 的交互、**MIL** 灯泡检查、就绪闪烁、催化器损坏失火时的闪烁等）
- 失火故障处理（跨所有气缸的去抖动、单个/多个失火故障的过滤）
- 对失火和燃油系统故障的特定恢复（**healing**）类似条件的支持

**注意：**对于 **OBD2**，要求失火和燃油系统故障只能在与检测时类似的条件下进行恢复（从而离开 Service $07）。这种"类似性"源自故障检测时存在的发动机转速、发动机负荷和温度条件范围所构成的"窗口"。

对于类似条件的处理，假定失火检测/燃油系统诊断的 **SW-C** 模块自行执行必要的计算。也就是说，这不在 **Dem** 内部全局解决。

但是，基于相应的失火检测/燃油系统诊断的特定接口要求，这可能导致 **Dem** 的扩展。任何进一步的实现都需要根据具体的诊断和 **Dem** 实现，针对特定的发动机控制单元项目进行定义。

DTCStoredDataRecordNumber（绝对冻结帧记录寻址功能）仅限于 0x00（**OBD** 冻结帧，参见第 6.11.2.4 节）。

由记录号标识的特定扩展数据记录的结构在每个 **ECU** 内是唯一的。

由于架构设计，**Dcm** 可以在处理"读取诊断数据"服务期间锁定事件内存更新（参见第 6.7.2.2 节）。

本规范涵盖 SAE J1939 相关诊断需求的一个子集（参见 [7, SWS J1939 Dcm] 中的表 1：支持的 DMx 报文）。**SPN** 转换方法仅限于版本 4（**CM** = 0）。

AUTOSAR 仅支持 ID 为 0x10 到 0xFF 的用户自定义内存（如 AUTOSAR 向 ISO 14229-1 提议的那样）。

指示器（**Indicator**）仅在 **DemEventMemorySet** 局部有效。**Dem** 不支持在多个 **DemEventMemorySet** 上使用指示器的配置。

### 4.2. 汽车域的适用性

**Dem** 的设计旨在同时满足有 **OBD** 需求和无 **OBD** 需求的 **ECU** 的设计要求。当前的直接适用域为车身（**body**）、底盘（**chassis**）和动力总成（**powertrain**）**ECU**。但是，没有理由不能使用 **Dem** 来实现其他汽车域（例如信息娱乐，**infotainment**）的 **ECU**。

## 5. 对其他模块的依赖

AUTOSAR 诊断事件管理器（**Dem**）与以下基础软件模块和软件组件存在接口和依赖关系：

![Figure5_1.png](Figure5_1.png)

- 功能抑制管理器（**FiM**）（参见 [8, SWS FiM]）代表对事件进行评估并将其分配给软件组件所需动作（例如抑制特定的"监视器"）。当监视器状态发生变化时，**Dem** 会通知并更新功能抑制管理器（**FiM**），以便根据已分配的依赖关系停止或释放功能实体。
- 诊断通信管理器（**Dcm**）（参见 [9, SWS Dcm]) 负责 **UDS** 和 SAE J1979 通信路径以及诊断服务的执行，进而处理来自外部诊断仪或车载测试系统的诊断请求。它转发来自外部诊断扫描工具的请求，并负责组装响应报文（**DTC**、状态信息等），随后这些报文将被传输到外部诊断扫描工具。
- J1939 的诊断通信管理器（**J1939Dcm**）（参见 [7, SWS J1939 Dcm]）负责 SAE J1939-73 诊断通信协议。
- 软件组件（**SW-C**）和基础软件（**BSW**）模块可以访问 **Dem** 以更新和/或获取当前的监视器状态和 **UDS** 状态信息。SW-C 和 **BSW** 模块可以从 **Dem** 获取数据，例如用于打开或关闭指示灯。监视器是 **SW-C** / **BSW** 模块的子组件。
- 数据提供者 **SW-C** 和/或 **BSW** 模块将提供 **Dem** 所需的数据（即事件相关数据），例如用于创建事件内存条目。
- **NVRAM** 管理器（**NvM**）（参见 [5]）提供将数据块存储到 **NVRAM** 的机制。**NVRAM** 块（最大大小由配置决定）被分配给 **Dem**，并由 **Dem** 使用以实现 **UDS** 状态信息和相关数据（例如跨上电复位）的永久存储。
- **ECU** 状态管理器（**EcuM**）负责包括 **Dem** 在内的基础软件组件的基本初始化和去初始化。
- **RTE** 为 **BSW** 实现调度机制，例如为 **ECU** 中使用的每个 **BSW** 模块分配优先级和内存保护。

### 5.1. 文件结构

#### 5.1.1. 代码文件结构

详情请参阅 SWS_BSWGeneral [6] 中第 5.1.6 章"代码文件结构"（**Code File Structure**）（子章节"链接时配置源文件"（**Link time configuration source**）和"后构建时配置源文件"（**Post-build time configuration source**））。

#### 5.1.2. 头文件结构

符号名称（参见 TPS_ECUC_02108）会为包含标识符参数的配置容器生成，例如**事件** Id 符号、运行周期、指示器、使能/存储条件等。

注意，SW-C **事件** Id 也会被发布，尤其是供可能访问特定 **SW-C** 事件状态的复杂设备驱动使用。**SW-C** 使用不同的端口来区分不同的事件。

### 5.2. 集成提示

由于存在跨模块通信，建议将 **Dem** 和 **J1939Dcm** 映射到同一个 Task，以便 **RTE** 配置正确的调用上下文。也可能存在其他 **BSW** 供应商特定的解决方案，允许更灵活的映射（例如通过在 **BSW** 内部行为中描述这种跨模块通信，或通过类似于 **Dcm** 与 **Dem** 交互的机制）。

## 6. 功能规格

诊断事件管理器（**Dem**）处理并存储由软件组件（**SW-C**）和基础软件（**BSW**）模块中的诊断监视器检测到的事件。存储的事件信息可通过接口提供给其他 **BSW** 模块或 **SW-C**。

DemGeneral 包含配置的全局部分，DemConfigSet 包含配置的多配置部分。

### 6.1. 启动行为

函数 Dem_PreInit 由 **ECU** 状态管理器在 **ECU** 启动阶段、**NVRAM** 管理器初始化之前调用。**BSW** 模块可以通过 Dem_SetEventStatus 开始报告相关事件（参见第 6.8 节）。

函数 Dem_Init（另参见第 6.11.5 节）在 **ECU** 启动阶段、**NVRAM** 管理器完成 **NVRAM** 数据恢复之后调用。包含监视器的软件组件在其之后初始化。函数 Dem_Init 还用于在调用 Dem_Shutdown 之后重新初始化 **Dem** 模块。

Dem_Init 的注意事项：在 **Dem** 模块的环境调用函数 Dem_Init 之前，**Dem** 模块不可用。

### 6.2. 监视器的重新初始化

应用中监视器的主初始化通过 Rte_Start 完成。事件特定部分的监视器初始化可以由 **Dem** 触发。

详情另请参见第 6.7.3 节。

函数参数 **InitMonitorReason** 指示初始化的原因/触发。

**注意：** **Dem** 模块不评估该回调函数的返回值（例如非 E_OK 的情况）。

**注意：**配置容器 DemCallbackInitMForE 用于为每个事件指定相关的端口或 C 回调。

下图给出两个示例：

![Figure7_1.png](Figure7_1.png)

![Figure7_2.png](Figure7_2.png)

**Dem** 也可以触发任何函数（可能与监视器相关）的初始化。

**注意：** **Dem** 模块不评估该回调函数的返回值（例如非 E_OK 的情况）。

示例：在清除 **Dem** 模块时（按 Service $04/ISO 15031-5 请求），可以初始化某些适配值。

### 6.3. 诊断事件定义

"诊断事件"（**Diagnostic Event**）定义了 **Dem** 模块可以处理的原子单元。"诊断事件"的状态表示一个监视器的结果（参见第 6.3.5 节）。**Dem** 通过 **RTE** 从 **SW-C** 或其他 **BSW** 模块接收监视器的结果。

**Dem** 模块使用 **EventId** 来管理系统的"诊断事件"状态，并针对各个测试结果执行所需的操作，例如存储冻结帧。

**Dem** 模块应为每个诊断事件表示一个 **EventId** 及其相关的 **EventName**。

所有监视器和 **BSW** 模块都将 **EventId** 用作符号化的 **EventName**。**Dem** 配置工具将符号名称替换为编号。

**Dem** 的设计不打算处理多个监视器共享单个 **EventId** 的情况。

**Dem** 模块使用内部监视器状态来存储已报告事件的状态。向 **Dcm** 报告的是 **UDS** 状态。

**Dem** 模块支持多个事件特定的配置参数，如下图所示。详细描述请参见第 9 章配置规范。

![Figure7_3.png](Figure7_3.png)

![Figure7_4.png](Figure7_4.png)

#### 6.3.1. 事件优先级

**事件优先级**（**Event priority**）定义为基于重要程度的事件排序。它用于在已存储事件数超过内存条目最大数（事件内存已满）时，确定哪些故障条目可以从事件内存中移除。

每个受支持的**事件**都应被分配一个优先级（参见 DemDTCAttributes 中的参数 DemDTCPriority）。

优先级值 1 应为最高优先级。更大的优先级值表示更低的重要性。

#### 6.3.2. 事件发生

**Dem** 模块应为每个事件内存条目提供一个发生计数器（**occurrence counter**）。

如果相关**事件**已被登记到相应的事件内存中，**Dem** 模块应将该发生计数器初始化为值 1。

如果配置参数 DemOccurrenceCounterProcessing（参见 DemPrimaryMemory 或 DemUserDefinedMemory）设置为 `DEM_PROCESS_OCCCTR_TF`，则每当 **UDS** 状态位 0（**TestFailed**）发生从 0 到 1 的跳变时，如果相关**事件**已存储在事件内存中，**Dem** 模块应将该发生计数器加一。

如果配置参数 DemOccurrenceCounterProcessing（参见 DemPrimaryMemory 或 DemUserDefinedMemory）设置为 `DEM_PROCESS_OCCCTR_CDTC`，则每当 **UDS** 状态位 0 发生从 0 到 1 的跳变时，如果相关**事件**已存储在事件内存中且 **UDS** 状态位 3 等于 1，**Dem** 模块应将该发生计数器加一。

如果事件特定的发生计数器已达到其最大值（255，参见第 6.7.1.2 节），**Dem** 模块不应再递增该事件的发生计数器。

#### 6.3.3. 事件种类

有两种不同类型的事件：

- **BSW** 相关事件（通过 **C API** Dem_SetEventStatus 报告）
- **SW-C** 相关事件（通过 **RTE** 操作 SetEventStatus 报告）

该种类可按**事件**进行配置（参见 DemEventParameter 中的 DemEventKind）。

这是必要的，因为 **BSW** 事件可能在 **Dem** 完全初始化之前报告，因而需要缓冲（参见第 6.8 节）。

#### 6.3.4. 事件目的地

配置参数 DemMemoryDestinationRef（参见 DemDTCAttributes）定义**事件**及其相关数据的专用存储位置（参见第 6.7.7 节）。

"永久事件内存"（**permanent event memory**）分配是从相关的 **DTC** 种类（参见第 6.4.1 节）隐式派生的。排放相关事件被自动分配到永久事件内存，因为将**事件**存储为"永久 **DTC**"是从其当前状态动态派生的（处理方式在第 6.9.5.8 节中描述）。在此上下文中，术语"永久"（**permanent**）表示排放相关事件的一个属性，并不仅指通过 **NvM** 进行的持久存储——无论哪种事件内存类型，都会进行持久存储。

不同内存类型的定义和使用是 **OEM** 特定的。

对于 **Dcm**-**Dem** 接口，参数 **DTCOrigin** 用于区分不同的内存区域。其意图是允许对不同的内存区域（主内存、用户自定义内存和永久内存）执行特定操作。

**DemMemoryDestinationRef 的限制**：**DTC** 只能通过 DemMemoryDestinationRef 引用同一 **DemEventMemorySet** 的事件内存。不支持 **DTC** 通过 DemMemoryDestinationRef 引用不同 **DemEventMemorySet** 的事件内存的场景。

#### 6.3.5. 诊断监视器的定义

诊断监视器是确定组件是否正常运行的例程实体。该监控功能为监控路径（**monitoring path**）标识特定的故障类型（例如对地短路、开路负载等）。监控路径表示被监控的物理系统或电路（例如传感器输入）。每个监控路径恰好关联一个诊断事件。

如果监视器自行去抖，则只有在合格结果（通过或失败）可用之后才会调用报告 API。至少在结果发生变化时必须进行报告。但是，通常监视器始终调用 **Dem** 在计算上更高效，因此应优先采用。因此，如何处理未变化结果的报告是 **Dem** 的实现特定行为。

如果监视器使用 **Dem** 内部的去抖动机制（参见第 6.7.3 节），则每当执行带功能检查的代码时都会调用报告 API。

![Figure7_5.png](Figure7_5.png)

#### 6.3.6. 事件依赖关系

分配的 **DemComponent** 内的事件优先级以及 **DemComponent** 之间的依赖关系，用于对错误报告到故障内存的存储进行过滤。

每当一个**事件**报告 **FAILED** 时，如果同一 **DemComponent** 处已有任何其他具有更高优先级的**事件**处于 **FAILED**，则该事件应被视为**连续故障**（**CONSECUTIVE FAULT**）。

每当一个**事件**报告 **FAILED** 时，如果任何父 **DemComponent** 处于 **FAILED**，则该事件应被视为**连续故障**。

**Dem** 应允许忽略 **DemComponent** 的事件优先级（DemComponentIgnoresPriority）。在这种情况下，仅当任何父组件处于 **FAILED** 时，该事件才应被视为**连续故障**（应忽略同一组件处其他事件的 **FAILED** 状态）。

如果报告的故障不被视为连续故障，则应将其视为**因果故障**（**CAUSAL FAULT**）。因果故障应正常处理。

如果报告的故障不被视为连续故障且已配置 DemCausalityDelayTime，则应将其视为**初步因果故障**（**PRELIMINARY-CAUSAL FAULT**）。从事件报告发生的时间点起，直到 DemCausalityDelayTime 经过为止，该事件可以被重新考虑为连续故障。如果在此期间报告了另一个在同一 **DemComponent** 或任何父 **DemComponent** 处具有更高优先级的故障，则该事件应被重新考虑为连续故障。时间经过后，该故障不再被重新考虑。

被视为连续故障的故障不应存储到故障内存中。（处理方式应类似于存储条件未满足的情况。）

被视为连续故障报告的 DEM_EVENT_STATUS_FDC_THRESHOLD_REACHED 报告（例如通过接口调用或在去抖动算法中达到配置阈值时）不应存储到故障内存中。处理方式应类似于存储条件未满足的情况。

**注意：**DEM_EVENT_STATUS_FDC_THRESHOLD_REACHED 的其他报告不会被视为连续的。

**Dem** 应提供接口 Dem_GetComponentFailed，用于查询 **DemComponent** 的 **FAILED** 状态。

如果启用了 DemTriggerFiMReports（参见 DemGeneral），**Dem** 应在每次 **DemComponent** 失败状态变化时调用函数 DemTriggerOnComponentStatus 通知 **FiM** 模块 [8]。

如果组件状态发生变化且配置了 DemComponentFailedCallbackFnc 或 DemComponentFailedCallbackUsePort 设置为 TRUE，则 **Dem** 应触发回调 DemTriggerOnComponentStatus。

**注意**：只有当未配置 DemComponentFailedCallbackFnc 时，才允许将 DemComponentFailedCallbackUsePort 设置为 TRUE。

#### 6.3.7. 组件可用性

**Dem** 应支持 **DemComponent** 的可用性。不可用的组件应被视为系统中不包含该组件（例如 Dem_GetComponentFailed 将返回 E_NOT_OK）。

应提供接口 Dem_SetComponentAvailable 来设置组件的可用状态。

将某个 **DemComponent** 设置为不可用时，所有分配给它的**事件**也应被设置为不可用。

启动后，所有 **DemComponent** 都应为可用状态。

如果通过 Dem_SetComponentAvailable 将某个 **DemComponent** 设置为"不可用"，则 **Dem** 应将所有依赖组件（子组件）视为已被设置为"不可用"。

如果通过 Dem_SetComponentAvailable 将某个 **DemComponent** 设置为"不可用"，则 **Dem** 应将所有分配的事件设置为"不可用"，包括所有子节点的事件。事件的行为类似于将每个事件单独设置为"不可用"（例如设置事件状态）。

如果通过 Dem_SetComponentAvailable 将某个 **DemComponent** 设置为"不可用"，且分配给它的任何单独**事件**（参见第 6.3.7 节）已经失败，则该单独事件将保持为"可用"。Dem_SetComponentAvailable 仍应返回 E_OK。

如果通过 Dem_SetComponentAvailable 将某个 **DemComponent** 设置为"可用"，则所有分配的事件也被设置为"可用"，包括所有子节点的事件（如果这些节点尚未被设置为"不可用"）。单个事件的行为类似于将它们单独设置为"可用"（例如触发 InitMonitorForEvent）。

如果为将事件设置为"可用"而调用函数 Dem_SetEventAvailable，且其相关节点当前为"不可用"，则该函数应返回 E_NOT_OK。

如果使用 Dem_SetEventAvailable 将事件设置为可用，而其组件处于"不可用"状态，则 Dem_SetEventAvailable 应返回 E_NOT_OK。

### 6.4. 诊断故障代码定义

"诊断故障代码"（**Diagnostic trouble code**）定义了映射到 **Dem** 模块"诊断事件"的唯一标识符（显示给诊断测试仪）。**Dem** 向 **Dcm** 模块提供"诊断故障代码"的状态（参见第 6.11.2 节）。

![Figure7_6.png](Figure7_6.png)

![Figure7_7.png](Figure7_7.png)

#### 6.4.1. DTC 种类

#### 6.4.2. DTC 格式

**Dem** 模块应支持 **DemDTC** 的 **DTC** 格式，包括：

- ISO 14229-1
- SAE J2012 OBD DTC（即 2 字节 DTC）
- SAE J1939-73
- ISO 11992-4
- SAE J2012 WWH-OBD DTC（即 3 字节 DTC）

配置参数 DemTypeOfDTCSupported 用于指定 `SWS_Dem_00013` 所定义的 **ECU** 受支持的 **DTC** 格式之一（参见 Dem_GetTranslationType）。这是确定要为 ISO 14229-1 服务"读取 DTC 信息"（**Read DTC Information**, 0x19）报告的 **DTC** 格式值所必需的。

**Dem** 模块应基于单独的配置参数支持 **UDS**、**OBD** 和 **J1939** 不同的 **DTC** 编号（参见 DemConfigSet 中的参数 DemDTC 和 DemObdDTC）。

对于 **DTC**，受支持的 **DTC** 格式（**UDS**、**OBD**、**OBD3Byte** 和 **J1939**）可以有多种组合。**Dem** 内部处理两种 **OBD** 格式之一，并与 **UDS** 和 **J1939 DTC** 组合使用。

一些制造商不希望完全转向支持 **UDS** 的 SAE J1979-2，而只会按 J1979-2 定义的有限 **UDS** 子集支持 J1979-2 功能，因此增加了 **OBD UDS DTC 分离**（**OBD UDS DTC separation**）功能。

**Dem** 应将所有 3 字节 **DTC** 值报告为 **uint32**，其中 byte 0 = 低字节，byte 1 = 中字节，byte 2 = 高字节，byte 3 未使用。对于 2 字节 **OBD DTC** 格式，仅使用两个字节（高字节、低字节）。**Dem** 服务应将这些 **DTC** 报告为 **uint32**，其中 byte 1 = 低字节，byte 2 = 高字节，byte 3 未使用，byte 0 = 0x00。

![Figure7_8.png](Figure7_8.png)

**注意：** **Dem** 期望按照 J1939 标准配置 **J1939DTC** 的 **SPN** 和 **FMI** 值。**Dem** 不会进行任何编码/转码。详情请参见 [14] 中第 5.7.1.11 节"SPN 转换方法"（**SPN Conversion Method**）。

**Dem** 应将 **DTC** 值报告为 **uint32**，其中 byte 0 = 低字节，byte 1 = 中字节，byte 2 = 高字节，byte 3 未使用。对于 **WWH-OBD DTC** 格式，仅使用三个字节（高字节、中字节和低字节）。**Dem** 服务应将这些 **DTC** 报告为 **uint32**，其中 byte 1 = 低字节，byte 2 = 高字节，byte 0 用作 **FTB**（依据 SAE J2012-DA）。

**DemDtcValue 的依赖关系**：仅当 DemOBDSupport 设置为 `DEM_OBD_MASTER_ECU` 或 `DEM_OBD_PRIMARY_ECU` 时，才应存在 **OBD DTC** 的 DemDtcValue。

**将 OBD DTC 限制在主故障内存**：仅当 **DTC** 具有指向 DemPrimaryMemory 的 DemMemoryDestinationRef 时，**DemDTC** 才应具有已配置的 DemObdDTCRef。

函数 Dem_GetDTCOfEvent 应获取由 **Dem** 配置映射到 **EventId** 的 **DTC**。

**3 字节 OBD DTC 仅用于 OBD UDS DTC 分离的配置**：仅当 DemSupportedObdUdsDtcSeparation 设置为 TRUE 且 DemOBDSupport 设置为 `DEM_OBD_MASTER_ECU` 或 `DEM_OBD_PRIMARY_ECU` 时，才应配置 3 字节 **OBD DTC** 的 DemDtcValue3Byte。

**不带 DTC 分离的 2 字节 OBD DTC 配置**：仅当未配置 DemSupportedObdUdsDtcSeparation 或其设置为 FALSE 时，才应配置 2 字节 **OBD DTC** 的 DemDtcValue。

#### 6.4.3. DTC 组

除了单个 **DTC** 值之外，还可以配置 **DTC 组**（参见 DemGroupOfDTC），如 ISO 14229-1 附录 D.1 所定义。每个 DTC 组都分配有自己的 DTC 组值（该值必须与任何其他 DTC 值和 DTC 组值不同）。当请求对 DTC 组执行操作时（例如 ClearDTC 和禁用/启用 DTC），通过 **DTC** 值选择 **DTCGroup**。

**DemGroupOfDTC** 应表示 **DTC** 组边界的值。**注意：**具有全局边界 0x000100 和 0xfffe00 的组不需要配置，因为组 **ALL** 是自动定义的。

介于所请求组的 dtc-code 与下一个更高 dtcgroup-code 之间的所有 **DTC** 应被视为属于该组。

**注意：**DTC 组与诊断服务 ClearDiagnosticInformation（0x14，参见 **Dem_ClearDTC**）相关。

**Dem** 应支持在 Dem_SelectDTC 的参数 **DTC** 中预定义的 **DTC** 组 **GroupOfAllDTCs**（0xFFFFFF）。

如果支持 **WWH-OBD** 或 J1979-2，**Dem** 应支持在 Dem_SelectDTC 的参数 **DTC** 中为 **WWH-OBD** 和 J1979-2 预定义的、与排放相关的 **DTC** 组（0xFFFF33）。

注意，DTC 组"所有 DTC"不会在 DemGroupOfDTC 中配置，因为它必须始终由 **Dem** 模块提供。考虑到 0xFFFFFF 是表示"所有 DTC 组"的不可配置值，为组"X"配置的每个 **DTC** 的 id 应位于开区间 (ID_of_group_X, ID_of_next_configured_group) 内，例如：

| powertrain DTC 组 -> 0x3FFF00 | DTC1 -> 0x3FFF04 DTC2 -> 0x3FFF06 … DTCn -> 0x3FFF0E |
| --- | --- |
| body DTC 组 -> 0x7FFF0F | … body DTC 组中的 DTC … |

作为对上述 DTC 组方法的配置约束：如果配置了一个或多个 DTC 组，则无法配置不属于任何组的独立 **DTC**。

#### 6.4.4. DTC 严重度

**DTC 严重度**用于按照 ISO 14229-1 附录 D.3"DTC 严重度与等级定义"提供特定**事件**重要程度的信息。DemDTCSeverity 仅适用于 **UDS DTC**。

如果调用了 API Dem_GetSeverityOfDTC 或 Dem_GetNextFilteredDTCAndSeverity，且所选 **DTC** 在 DemDTCSeverity 中配置了严重度值，则 **Dem** 应将 DemDTCSeverity 中配置的值设置为 **DTCSeverity**。

如果调用了 API Dem_GetSeverityOfDTC 或 Dem_GetNextFilteredDTCAndSeverity，且所选 **DTC** 未在 DemDTCSeverity 中配置严重度值，则 **Dem** 应将 `DEM_SEVERITY_NO_SEVERITY` 设置为 **DTCSeverity**。

#### 6.4.5. 功能单元

如果调用了 API Dem_GetFunctionalUnitOfDTC，且所选 **DTC** 在 DemDTCFunctionalUnit 中配置了功能单元值，则 **Dem** 应将 DemDTCFunctionalUnit 中配置的值设置到出参 **DTCFunctionalUnit** 中。

如果调用了 API Dem_GetFunctionalUnitOfDTC，且所选 **DTC** 未在 DemDTCFunctionalUnit 中配置功能单元，则 **Dem** 应在出参 **DTCFunctionalUnit** 中设置值 0x00。

#### 6.4.6. DTC 重要性

**DTC** 有两种不同的重要性级别：

- **fault**：归类与组件/**ECU** 自身相关的故障（例如需要维修措施）
- **occurrence**：归类指示有关系统行为不足的附加信息的问题（例如与 **ECU** 无法控制的状态相关）

该重要性级别可按**事件**配置（参见 DemDTCAttributes 中的 DemDTCSignificance），并且可以映射为一个数据元素（参见 `DEM_SIGNIFICANCE`）。

#### 6.4.7. 抑制 DTC 输出

本章描述在运行期间通过 **API** 调用对**事件**/**DTC** 的动态抑制。被抑制的 **DTC** 的行为是：对测试仪不可见，但诊断监视器可以继续对其进行处理。

一个示例用例：由 **SW-C** 在运行期间决定在某个市场隐藏某个 **DTC**。

配置参数 DemSuppressionSupport（参见 DemGeneral）控制 **DTC** 抑制功能的可用性。

如果某个 **DTC** 的所有相关**事件**都不可用，则 **Dem** 应抑制该 **DTC**。

详情参见第 6.4.8 节。

如果 **DTC** 与**事件**之间存在一对一的关系，则当相关**事件**不可用时该 **DTC** 被抑制。如果该 **DTC** 是**组合 DTC**，则当所有组合事件都不可用时该 **DTC** 被抑制。

关于输出和查询函数，被抑制的 **DTC** 应被视为未在系统中配置。

**被抑制 DTC 的 DTC 查询函数的行为**：如果针对某个被抑制的、单独选择的 **DTC** 调用以下任一 API：

- Dem_GetStatusOfDTC
- Dem_GetSeverityOfDTC
- Dem_GetFunctionalUnitOfDTC
- Dem_ClearDTC

则 **Dem** 应返回 `DEM_WRONG_DTC`。

被抑制的 **DTC** 对以下 **Dcm** 查询函数不可见；因此以下函数应将该 **DTC** 视为过滤器不匹配：

- Dem_DcmGetDTCOfOBDFreezeFrame
- Dem_DcmReadDataOfOBDFreezeFrame
- Dem_DcmGetInfoTypeValue08
- Dem_DcmGetInfoTypeValue0B
- Dem_DcmReadDataOfPID01
- Dem_GetDTCByOccurrenceTime
- Dem_GetNextFilteredDTC
- Dem_GetNextFilteredDTCAndFDC
- Dem_GetNextFilteredDTCAndSeverity
- Dem_GetNextFilteredRecord
- Dem_J1939DcmFirstDTCwithLampStatus
- Dem_J1939DcmGetNextDTCwithLampStatus
- Dem_J1939DcmGetNextFreezeFrame
- Dem_J1939DcmSetDTCFilter
- Dem_J1939DcmGetNumberOfFilteredDTC
- Dem_J1939DcmGetNextFilteredDTC
- Dem_J1939DcmSetRatioFilter
- Dem_J1939DcmGetNextFilteredRatio
- Dem_J1939DcmReadDiagnosticReadiness1
- Dem_J1939DcmReadDiagnosticReadiness2
- Dem_J1939DcmReadDiagnosticReadiness3
- Dem_SelectFreezeFrameData
- Dem_SetDTCFilter
- Dem_SelectExtendedDataRecord
- Dem_SetDTCFilterByExtendedDataRecordNumber
- Dem_SetDTCFilterByReadinessGroup

**注意：**这意味着该 **DTC** 的（对外）报告（例如 **DTC** 编号、**UDS** 状态、**DTC** 扩展数据记录、**DTC** 统计数据、**IUMPR** 等）被抑制。

**DTC** 抑制不应停止相应 **DTC** 的事件处理。

**注意：**这意味着例如**事件鉴定**、环境数据的更新和功能降级仍在 **Dem** 内部处理。

**注意：**如果 **DTC**/冻结帧不应存储到故障内存中，则应另外使用存储条件。

**Dem_GetDTCSuppression 的功能**：如果调用了 Dem_GetDTCSuppression，**Dem** 应在出参 **SuppressionStatus** 中返回 **DTC** 抑制状态。值 TRUE 表示该 **DTC** 曾通过以 SuppressionStatus = TRUE 调用 Dem_SetDTCSuppression 而被抑制；值 FALSE 表示该 **DTC** 当前未被抑制。

如果调用了 Dem_SetDTCSuppression，**Dem** 应将所选 **DTC** 的抑制状态设置为参数 **SuppressionStatus** 的值。

**DTC** 不被处理因而对诊断不可见的原因有多种，而抑制状态本身只能通过 Dem_SetDTCSuppression 改变。Dem_GetDTCSuppression 仅评估该抑制状态。

#### 6.4.8. 事件的可用性（可见性与计算）

本章描述一种将**事件**标记为不可用的方法，而不将它们从实际配置中移除。不可用的事件被视为未包含在 **Dem** 配置中。

一个示例用例：某个控制单元及其软件支持控制多种硬件。硬件型式的某些部分可能可用或不可用，但仍然应用相同的控制单元和软件。

1. 每个硬件型式生成一个标定集。应用工程师建立后构建（**post-build**）配置，以确保软件针对硬件正确运行。对于某个硬件型式中不包含的部分，这意味着相关**事件**需要被关闭、被抑制。这些事件应表现为完全中性：永不置位其 **LastFailed**、不引发跛行回家（**limp-home**）模式、对维修站服务不可见。
   =&gt; ECUC 参数 DemEventAvailableInVariant 设置为 TRUE（启用）或 FALSE（禁用）
2. 一个标定覆盖多个硬件型式。在生产期间，甚至在运行期间（维修站）更换硬件时，会向控制单元写入一些编码位，或接收到某些网络报文，以根据硬件的变化更改软件的行为。与情形 1 相同，某些**事件**需要被抑制。
   =&gt; ECUC 参数 DemEventAvailableInVariant 设置为 TRUE（启用）
   =&gt; ECUC 参数 DemEventAvailable 定义**事件**的初始可用性
   =&gt; 接口 Dem_SetEventAvailable 用于在运行期间更改由 DemEventAvailable 定义的可用性

**通过配置启用/禁用事件**：配置参数 DemEventAvailableInVariant 应作为将**事件**视为启用或禁用的主控。如果配置参数 DemEventAvailableInVariant 设置为 FALSE，**Dem** 应将该**事件**视为未配置为 DemEventParameter。如果 DemEventAvailableInVariant 未设置或设置为 TRUE，**Dem** 应视其他来源的情况考虑启用该**事件**。

**注意：**DemEventAvailableInVariant 允许禁用软件发布中包含但不需要的**事件**；甚至会阻止相关 **SW-C** 通过 Dem_SetEventAvailable 使其变为可用。

**处理事件的可用性**：在以下情况时，**Dem** 应将**事件**视为不可用：

- DemEventAvailableInVariant == FALSE，或
- DemEventAvailable == FALSE，或
- DemEventAvailable 已被 Dem_SetEventAvailable（FALSE）改写，或
- DemComponentClassRef 引用的组件不可用

**Dem** 应提供运行期间的功能，将事件视为未配置为 DemEventParameter。配置参数 DemAvailabilitySupport 用于启用 Dem_SetEventAvailable() 提供的功能。

不可用的事件不应参与 Service $01 PID $41 的计算。

引用不可用事件的 **IUMPR** 比率既不应计算也不应报告。

**Dem** 不应在 VARIANT-POST-BUILD 中提供函数 Dem_SetEventAvailable。理由：在 VARIANT-POST-BUILD 中，初始值在 Dem_Init（post-build 初始化时间）之前无效。

如果事件被设置为不可用，则相应**事件**应被视为未在系统中配置（例如 Dem_SetEventStatus 和 Dem_GetEventUdsStatus 应返回 E_NOT_OK）。受影响的 API 如下：

- Dem_SetEventStatus
- Dem_GetEventUdsStatus
- Dem_ResetEventDebounceStatus
- Dem_ResetEventStatus
- Dem_PrestoreFreezeFrame
- Dem_ClearPrestoredFreezeFrame
- Dem_GetDebouncingOfEvent
- Dem_GetDTCOfEvent
- Dem_GetFaultDetectionCounter
- Dem_GetEventFreezeFrameDataEx
- Dem_GetEventExtendedDataRecordEx
- Dem_ClearDTC
- Dem_DcmGetDTRData
- Dem_RepIUMPRFaultDetect
- Dem_RepIUMPRDenRelease
- Dem_SetWIRStatus
- Dem_SetEventStatusWithMonitorData
- Dem_GetMonitorStatus
- Dem_SetEventConfirmationThresholdCounter
- Dem_SetEventDisabled
- Dem_ResetMonitorStatus

**注意：**事件的可用性还可能影响 **DTC** 的抑制（参见第 6.4.7 节）。

当以 AvailableStatus = FALSE 调用 API Dem_SetEventAvailable 时，如果出现以下情况，**Dem** 应返回 E_NOT_OK：

- 该**事件**已存在事件内存条目，或
- 该**事件**的任何事件状态位"testFailed"、"pending"、"confirmed"或"warningIndicatorRequested"已置位

**Dem_SetEventAvailable 的异步行为**：**Dem** 应异步处理 Dem_SetEventAvailable 调用。这意味着最终结果在稍后的时间点才可用。

"稍后的时间点"是实现特定的，可能是下一个主函数，且在 Dem_SetEventAvailable 返回之后。

如果以 AvailableStatus == 'false' 调用 Dem_SetEventAvailable，**Dem** 应将该**事件**的 **UDS** 状态设置为 0x00。

**注意：**如果 **UDS** 状态发生变化，将调用相应的回调，以向用户正确提供状态变化的信息。

如果以 AvailableStatus == 'true' 调用 Dem_SetEventAvailable，**Dem** 应将该**事件**的 **UDS** 状态设置为 0x50。

**对已禁用事件相关调用的反应**：如果**事件**配置为 DemEventAvailableInVariant 设置为 FALSE，且以 AvailableStatus = TRUE 对该 **EventId** 调用 API Dem_SetEventAvailable，则 API Dem_SetEventAvailable 应返回 E_NOT_OK。

如果调用函数 Dem_SetEventAvailable 将事件设置为"可用"，**Dem** 应使用 **DEM_INIT_MONITOR_REENABLED** 作为 **InitMonitorReason** 触发事件初始化。

如果以有效的 **EventId** 调用 Dem_GetEventAvailable，则应将出参 **AvailableStatus** 设置为该**事件**的可用性并返回 E_OK。

可用性由配置参数 DemEventAvailable（可通过 Dem_SetEventAvailable 修改）和 DemEventAvailableCnf（"Dem 应将事件视为不可用……"）共同决定。


### 6.5. 受监控组件的定义

受监控组件是系统中与正常运行检查相关的部分。组件的故障需要被报告并记录。为此，通常定义一个或多个监控并将其分配给该组件。

此外，这类组件的状态也很重要，用于影响系统行为（组件状态可用于 **Fim**）和错误记录（对连续故障条目的过滤）。

**Dem** 允许将受监控组件显式定义为 **DemComponent**，定义事件与组件之间的关系，并最终定义组件之间的关系。

![Figure7_10.png](Figure7_10.png)

#### 6.5.1. 组件与依赖关系的定义

**Dem** 应将受监控组件表示为 **DemComponent**，并带有唯一标识符，用于在接口中标识该组件。

每个 **DemComponent** 应具有布尔状态 **FAILED**，表示该组件是否存在错误。

**Dem** 应允许定义 **DemComponent** 之间的关系。这些关系是有向的，即一个组件依赖于另一个组件（DemImmediateChildComponentRef）。任何具有有向关系（包括跨多个组件）的组件都被视为父组件（**parent component**）。

示例：a -&gt; b -&gt; c -&gt; d，a 和 b 是 c 的父组件；c 和 d 依赖于 b。

**DemComponent** 的依赖关系仅支持有向无环图结构。

**Dem** 应允许将事件分配给 **DemComponent**。

事件可以分配给恰好一个 **DemComponent**，对该组件的监控正在测试错误条件。多个事件可以分配给同一个组件。

**Dem** 应允许按优先级对分配给 **DemComponent** 的事件排序。优先级按**事件**通过 DemComponentPriority 定义。

在为某个**事件**报告错误（**DEM_MONITOR_STATUS_TF**）时，所分配的 **DemComponent** 应在该事件报告的上下文中被设置为 **FAILED**。

将某个 **DemComponent** 设置为 **FAILED** 时，所有依赖组件也应被设置为 **FAILED**。

当所有已分配事件均为 **NOT FAILED**（**DEM_MONITOR_STATUS_TF**）且所有父组件均为 **NOT FAILED** 时，**DemComponent** 应被设置为 **NOT FAILED**。

### 6.6. 运行周期管理

**Dem** 模块提供定义不同运行周期的可能性（参见 ISO 14229-1）。

运行周期的示例包括：

- 点火 on/off 循环
- 上电/下电循环
- **OBD** 驾驶循环
- 发动机暖机循环
- 运行有效/无效循环
- 累计运行时间

各种**运行周期**是计算周期相关状态信息（例如 **testCompleteThisOperationCycle**）的基础。此外，运行周期也是某些功能（例如故障的确认和故障的老化）的基础。通过 Dem_RestartOperationCycle 重启或切换到下一个运行周期，作为这些功能计算的触发。

**运行周期重启**：只有在 Dem_PreInit 之后才允许调用函数 Dem_RestartOperationCycle。如果在 Dem_Init 之前重启了某个运行周期，重启的处理应在 Dem_Init 之后进行。

**运行周期重启**：**Dem** 只应在上一次重启被完全处理之后才重启**运行周期**。换言之，即不存在运行周期重启队列。

**Dem** 允许使用 DemLeadingCycleRef 参数定义**从属运行周期**（**dependent operation cycle**）。只要设置了该参数，该运行周期就被视为从属运行周期。只要未设置该参数，该运行周期就被视为"普通"运行周期。

如果传递给 Dem_SetCycleQualified 的**运行周期**完全未配置，则应报告 **Det** 错误 `DEM_E_WRONG_CONFIGURATION`。

**Dem** 应跨电源周期存储**从属运行周期**的鉴定状态。

**运行周期重启**：每当请求通过 Dem_RestartOperationCycle 重启某个**运行周期**时，所有依赖于所选运行周期的**运行周期**也应被重启，但前提是它们已被鉴定。

**注意：**设置一个从属运行周期为已鉴定不会启动该运行周期，即使前导运行周期此前已经启动。

**运行周期重启**：重启一个**从属运行周期**时，其运行周期鉴定状态应被复位。

API Dem_GetCycleQualified 应在出参 **isQualified** 中提供所请求**运行周期**的鉴定状态。

如果传递给 Dem_GetCycleQualified 的**运行周期**完全未配置，则应报告 **Det** 错误 `DEM_E_WRONG_CONFIGURATION`。

如果 DemOBDDelayedDCYConfirmedAndMIL 设置为 TRUE，则链接到 **OBD** 驾驶循环（DemOBDDrivingCycleRef）的事件的行为应发生改变：

如果该**运行周期**未鉴定，则处理状态报告，但更新确认状态除外。当 **OBD** 驾驶周期被设置为已鉴定的那一刻，**Dem** 应执行必要的计算，以使在"未鉴定"阶段收集的事件达到已确认状态。

**OBD** 立法要求对运行周期进行特定的实现。对于排放相关的 **ECU**，必须相应地实现。

#### 6.6.1. 运行周期计数器

**运行周期计数器的初始化**：如果为某个**事件**创建了新的事件内存条目，则运行周期计数器"距上次失败的周期数"、"距首次失败的周期数"和"失败周期数"应初始化为零。

**运行周期计数器的大小**：每个运行周期计数器的大小应为一个字节。

**运行周期计数器的溢出处理**：如果对某个运行周期计数器的任何计数操作会导致其从 0xFF 回绕，则应将其保持在 0xFF。

##### 6.6.1.1. 距上次失败的周期数

计数器"距上次失败的周期数"（**Cycles since last failed**）表示自 **DTC** 故障检测计数器上次达到最大值 +127 以来（自 **DTC** 信息上次被清除以来）的运行周期数。应包括所有运行周期，包括测试未完成的周期。

如果计数器"距上次失败的周期数"被映射到扩展数据记录（DemInternalDataElement 设置为 `DEM_CYCLES_SINCE_LAST_FAILED`），则它应可用于每条"事件相关数据"记录。

如果计数器"距上次失败的周期数"已存储在事件内存中，则当内部去抖计数器达到 DemDebounceCounterFailedThreshold 时，应将其复位为零。

如果计数器"距上次失败的周期数"已存储在事件内存中，则应在所引用的**运行周期**（参见 DemOperationCycleRef）结束时将其递增。

##### 6.6.1.2. 距首次失败的周期数

计数器"距首次失败的周期数"（**Cycles since first failed**）表示自 **DTC** 故障检测计数器首次达到最大值 +127 以来（自 **DTC** 信息上次被清除以来）的运行周期数。应包括所有运行周期，包括测试未完成的周期。

如果计数器"距首次失败的周期数"被映射到扩展数据记录（DemInternalDataElement 设置为 `DEM_CYCLES_SINCE_FIRST_FAILED`），则它应可用于每条"事件相关数据"记录。

如果计数器"距首次失败的周期数"已存储在事件内存中，则应在所引用的**运行周期**（参见 DemOperationCycleRef）结束时将其递增。

##### 6.6.1.3. 失败周期数

计数器"失败周期数"（**Failed cycles**）表示 **DTC** 故障检测计数器达到最大值 +127 期间的运行周期数（自 **DTC** 信息上次被清除以来）。

如果计数器"失败周期数"被映射到扩展数据记录（DemInternalDataElement 设置为 `DEM_FAILED_CYCLES`），则它应可用于每条"事件相关数据"记录。

如果计数器"失败周期数"已存储在事件内存中，则应在所引用的**运行周期**（参见 DemOperationCycleRef）结束时、且 **UDS** 状态位 1 置位为 1 的情况下将其递增。

<!-- R-B holding area: existing translation of source 7.11.5 (from the legacy stub), to be re-homed under §6.11.5 in run R-B
**Dem**模块使用非易失性内存块（**Nonvolatile Memory Blocks**）来实现**UDS**状态信息、事件相关数据和所需内部状态的永久存储。例如：在启动时获取事件的状态。

**Dem**模块可以通过**NVRAM**管理器[5]进行大小的配置。

**Dem**使用的每个非易失性内存块也需要进行配置，具体内容可参阅：**DemNvRamBlockId**。使用的非易失性存储块的数量、类型和内容没有规定。这些可根据具体实现进行处理。**NvM**的使用也可以通过配置**DemNvRamBlockId**进行禁用，这时**Dem**将仅基于**RAM**工作。

**Dem**模块应验证非易失性块的有效性（与块状态相关）、完整性（与**CRC**结果相关）和一般**NvM**读取错误（在使用相应数据之前）。通常这种验证是在 **Dem_Init**中，通过对这些NvM内存块使用**NvM_GetErrorStatus**来完成的，这些内存块由ECU状态管理器通过**NvM_ReadAll**读取。

注意：

对于**Dem**模块的非易失性数据，建议在**NvM**中配置一个**CRC**。

如果**NVM**模块无法读取**Dem**模块的某些非易失性数据，则**Dem**模块需使用其初始值初始化所有非易失性数据。

注意：

为了避免可读数据块和错误的数据块之间的不一致，所有非易失性数据都会被初始化。完成初始化后，应允许**NvM**模块的故障检测机制向**Dem**模块报告相应的读取错误（具体可参阅**Dem_SetEventStatus**）。 用于表示有缺陷的**NVRAM**。

**Dem_Init**完成后，**Dem**模块应完全可操作。

如果**DTC**配置为**DemNvStorageStrategy** = **IMMEDIATE_AT_FIRST_OCCURRENCE**，则在事件第一次发生时需立即存储相关数据，则当配置的用于存储数据的触发器 DemEventMemoryEntryStorageTrigger 第一次发生时，Dem 应触发将其事件相关数据存储到 NvM。
-->
