---
title: "AUTOSAR 术语表（缩略语与缩写）"
---

本页汇总各 AUTOSAR 模块文章以及 AUTOSAR TR 术语表（Foundation）的术语，按字母排序。所有词条均出自 AUTOSAR **R23-11** 版规范文档；「来源」行注明该词条所引用的规范文档及其 spec 编号。

## A

**A2L**
> ASAM 2MC 语言文件的文件扩展名（**File Extension for an ASAM 2MC Language File**）。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**AB**
> 安全气囊（**Airbag**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ABS**
> 防抱死制动系统（**Antilock Braking System**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**absolute timer（绝对定时器）**
> 绝对定时器被设置为 FlexRay 集群的一个绝对全局时间并由其触发。FlexRay 全局时间由一个循环和一个宏节拍偏移量组成。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**ACC**
> 自适应巡航控制（**Adaptive Cruise Control**）。
>
> 来源：[Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC）
{: .glossary-source}

**Accuracy**
> 精度（**Accuracy**）取决于用于采样或者生成的硬件外围设备。如：**ADC**转换器可以是 8/10/12/16 位转换器
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Acquisition Time**
> 采集时间 = 采样时间（**Sample Time**）+ 转换时间（**Conversion Time**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**Activation Mode 1**
> 无故障——**MIL** 应闪烁一次。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Activation Mode 2**
> "按需 MI"（on-demand-MI）——如果 **OBD** 系统按照区分显示策略会命令按需 MI，**MIL** 应闪烁两次。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Activation Mode 3**
> "短时 MI"（short-MI）——如果 **OBD** 系统按照区分显示策略会命令短时 MI，**MIL** 应闪烁三次。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Activation Mode 4**
> "持续 MI"（continuous-MI）——如果 **OBD** 系统按照区分显示策略会命令持续 MI，**MIL** 应保持持续点亮。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Active Time Base Customer**
> 一种时基客户，它自主调用同步时基管理器，或用于从同步时基管理器读取某时基的时间信息，或用于根据应用信息更新同步时基管理器维护的时基。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Activity state**
> 活动状态：软件组件正在执行时的状态。活动状态以许可状态为前提条件，并叠加物理使能条件。它不由 **FiM** 计算，也不作为状态变量提供，只能通过观察或测量确定。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**ADC**
> 模数转换器（**Analogue Digital Converter**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC Channel**
> **ADC**通道是指绑定到一个端口引脚的逻辑**ADC**实体。同时多个**ADC**实体也可以映射到同一个端口引脚。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC Channel Group**
> **ADC**通道组是指由一组**ADC**通道链接到同一个**ADC**硬件单元（**ADC HW Unit**）。例如：一个采样保持器（**Sample & Hold**）和一个**A/D**转换器。整个组的转换由一个触发源触发。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC HW Unit**
> 微控制器的输入电子设备，包括执行模拟到数字转换所需的所有部件。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC Module**
> ADC的基础软件模块ADC驱动模块（**ADC Driver**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC Result Buffer**（**ADC Streaming Buffer**，**ADC Stream Buffer**）
> **ADC**驱动程序的用户必须为每个组提供一个缓冲区。如果选择流式访问模式（**streaming access mode**），此缓冲区可以保存同一组通道的多个样本。如果选择单一访问模式（**Single Access Mode**），每个组通道的一个样本将保存在缓冲区中。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**Address Area**
> 地址区（**Address Area**）是指逻辑地址空间中连续的存储区域。通常，多个物理存储扇区组合成一个逻辑地址区。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**AEB**
> 自主紧急制动（**Autonomous Emergency Braking**）。
>
> 来源：[Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC）
{: .glossary-source}

**Aging**
> 在经过确定的运行周期数之后，从事件内存中遗忘/删除不再失败的事件/**DTC**。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Aging Counter**
> 用于执行老化的计数器（也称 **Aging Cycle Counter** 或 **DTC Aging Counter**）。它对事件/**DTC** 从事件内存中移除之前所经历的运行周期数进行计数。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**AI**
> 存活指示（**Alive Indication**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**AI Table**
> 应用接口表（**Application Interface Table**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**AIFS**
> 仲裁帧间间隔（**Arbitration Inter Frame Space**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）
{: .glossary-source}

**Alive Counter**
> **WdgM** 中在**检查点**上下文内的独立数据资源，用于跟踪和处理该**检查点**的**存活指示**数量。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Alive Indication**
> 由**被监督实体**的**检查点**提供的指示，用于向**WdgM** 标识其存活状态。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Alive Supervision**
> 一种监督，用于检查**被监督实体**的执行是否足够频繁且不过于频繁（包括容差）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Antisubmarine**
> 下潜——约束系统中与汽车应用相关的术语（**Antisubmarine**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**AP**
> 执行器池（**Actuator Pool**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**API**
> 应用编程接口（**Application Programming Interface**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Standard Types（标准类型）](general/standard_types/index.md)（SWS_StandardTypes）
{: .glossary-source}

**APID**
> Application ID —— 应用 ID。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Application ID**
> 一个应用/**SW-C** 的缩写，标识一条日志和跟踪消息所来自的应用/**SW-C**；由四个 8 位 ASCII 字符组成。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Applied Rate**
> 用于设置/计算全局时间的本地实例所施加的速率。对于时基主节点，它与速率校正 r_rc 相同；对于时基从节点，对于同步时基为 r_rc 与 r_oc 之和，对于偏移时基分别为 (r_orc − 1) 与 r_oc。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**ARP**
> Address Resolution Protocol —— 地址解析协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**ARTI**
> AUTOSAR 运行时接口——用于调试与跟踪嵌入式系统运行时行为的一组标准（**AUTOSAR Run-Time Interface**）
>
> 来源：[ARTI（AUTOSAR 运行时接口）](sw_arch/arti/index.md)（AUTOSAR_CP_EXP_ARTI）
{: .glossary-source}

**arxml**
> .arxml——AUTOSAR 可扩展标记语言文件（**AUTOSAR Extensible Markup Language File**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**ASAM**
> 自动化与测量系统标准化协会（**Association for Standardization of Automation and Measuring Systems**）。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**ASIL**
> 汽车安全完整性等级（**Automotive Safety Integrity Level**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**ASN.1**
> 抽象语法标记一号（**Abstract Syntax Notation One**）：一种描述数据结构的标准记法，常与 DER 编码规则一起用于证书等密码学数据的编码。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**Assembly Connector**
> 组装连接器。在 VFB 层级把一个组件的 RPort/PRPort 与另一个组件的 PPort/PRPort 连接起来的连接器；恰好连接一个提供端口与一个要求端口。
>
> 来源：[VFB（虚拟功能总线）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**Atomic sequence/ atomic piece**
> 原子序列是一段不得被中断的测试。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Attributes**
> 属性（**Attributes**）是**ECU**中存在的每个**ECU**信号所包含的软件或者硬件特性。一些属性是固定的，由端口定义决定。还有一些属性是可以在**I/O**硬件抽象中进行配置的。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**ATWS**
> 防盗警告系统（**Anti-Theft Warning System**）。可借助光学与声学信号警示未授权进入尝试、并可防止发动机被起动的防盗系统。
>
> 来源：[Explanation of Application Interfaces of the Body and Comfort Domain（车身与舒适域应用接口说明）](application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort）
{: .glossary-source}

**AUTOSAR**
> 汽车开放系统架构（**AUTomotive Open System ARchitecture**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**AUTOSAR Connector**
> **SoAd** 在不同的 PDU 源/提供者与 TCP/IP 协议栈之间、以及 TCP/IP 协议栈与不同的 PDU 汇/消费者之间充当（解）复用器（**(De)Multiplexer**）。术语 AUTOSAR 连接器（**AUTOSAR connector**）指一个 PDU 的源/提供者或汇/消费者。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**Autosar EthTSyn**
>  EthTSyn，**Ethernet** 的时间同步提供者模块。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**AVB**
> 音视频桥接（**Audio Video Bridging**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

## B

**Background test**
> 后台测试由 **SW** 调度器/**RTOS** 周期性调用。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Bank**
> 存储 **Bank** 是一组扇区批次（**Sector Batch**）的集合。如果存储技术支持按扇区分段，则存储 **Bank** 是不允许边读边写操作的扇区批次组实例。对于闪存设备，**Bank** 通常映射到单独的闪存控制器。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**BAS**
> 制动辅助（**Brake Assist**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Binary Manifest**
> 软件集群的二进制对象的定义良好的接口，提供资源的元信息与访问此类资源的句柄（**Binary Manifest**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**Binary Object**
> 一组文件的集合，包含在编程到目标 ECU 之前不会再被修改的二进制可执行代码与数据（**Binary Object**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**BIST**
> 内建自测试（**Built in Self Test**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）、[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**BMCA**
> 最佳主时钟算法（**Best Master Clock Algorithm**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**BndM**
> 大容量非易失性数据管理器（**Bulk Non-Volatile Data Manager**）
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**BRWS**
> 基本后轮转向（**Basic Rear Wheel Steering**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**BSAS**
> 基本转向角叠加（**Basic Steering Angle Superposition**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**BSTS**
> 基本转向力矩叠加（**Basic Steering Torque Superposition**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**BSW**
> 基础软件（**Basic Software**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping）、[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**BSW driver**
> 有关 BSW 驱动（**BSW driver**）的列表，请参阅基础软件模块列表中 "AUTOSAR SW layer" 列。
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**BswM**
> 基础软件模式管理器（**Basic Software Mode Manager**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**BSWMD**
> 基础软件模块描述（**Basic Software Module Description**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**buffer（缓冲区）**
> 在 Fr SWS 的上下文中，缓冲区描述一个硬件发送/接收资源，它是 FlexRay 控制器的一部分，被映射到一个 FlexRay 槽、信道、循环用于发送或接收。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**Bugzilla**
> 变更请求管理工具（**Bugzilla**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**Bus Off**
> CAN 总线的错误状态：CAN 控制器因错误计数达到上限而与总线脱离。CAN 状态管理器（CanSM）通过 Bus Off 恢复状态机进行恢复。
>
> 来源：[Error Description（错误描述）](general/error_description/index.md)（AUTOSAR_CP_EXP_ErrorDescription）
{: .glossary-source}

## C

**C/S**
> 客户端/服务器（**Client/Server**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Callback**
> 术语回调函数（**Callback**）主要用于**API**服务，实现通知其他**BSW**模块。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Caller/calling entity**
> 调用者/调用实体位于较高的 **AUTOSAR** 或 **ISO** 层。它是 **API** 调用的用户。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Callout**
> **Callout**是一种函数**Stub**。主要在配置时进行填写，目的是向提供**Callout**函数的模块添加功能。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Camel case**
> 驼峰命名法：书写短语时不带空格或标点符号、以单个大写字母指示单词之间分隔的书写方式，第一个单词以大写或小写开头。示例：GetVersionInfo。
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**CAN**
> Controller Area Network —— 控制器局域网。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**CanIf**
> CAN Interface —— CAN 接口。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**CanTSyn**
> **CAN** 时间同步模块（**Time Synchronization over CAN** module）。通过 **CAN** 总线分发时间信息、实现 **CAN** 特定时间同步协议的模块。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**CBC**
> 弯道制动控制（**Cornering Brake Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**CBR**
> 信道忙闲比（**Channel Busy Ratio**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）
{: .glossary-source}

**CC**
> 通信控制器（**Communication Controller**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**CDD**
> 复杂驱动（**Complex Driver**）。未被 AUTOSAR 标准化的软件实体，可以访问 AUTOSAR 接口和/或基础软件模块 API，或经由它们被访问；位于分层软件架构的复杂驱动层。
>
> 来源：[CDD Design and Integration Guideline（CDD 设计与集成指南）](general/cdd_design_and_integration/index.md)（AUTOSAR_CP_EXP_CDDDesignAndIntegrationGuideline）、[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**Channel**
> 通道：从加密服务管理器队列经由加密接口到特定加密驱动程序对象的路径。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**Checkpoint**
> **被监督实体**控制流中的一个点，在该处向**WdgM** 报告活动。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**CHI**
> 控制器主机接口（**Controller Host Interface**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**CIT**
> 信道空闲时间（**Channel Idle Time**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）
{: .glossary-source}

**Class**
> 一个类（**Class**）代表一组具有相似电气特性的信号。如：模拟类（**Analogue class**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Class B1 counter**
> Class B1 故障被确认（**Confirmed**）且处于 **TestFailed** 状态期间的发动机运行小时数。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Client-Server communication**
> 客户端-服务器通信（**Client-Server communication**）涉及两个实体。客户端是要求服务的一方，服务器是提供服务的一方。客户端发起通信，请求服务器执行服务，必要时传输参数集合。服务器以**RTE**的形式，等待来自客户端的传入通信请求，执行请求的服务并发送对客户端请求的响应。因此服务启动的方向是用来对**AUTOSAR**软件组件是客户端还是服务器分类的主要标识。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**cluster（集群）**
> 多个相互连接的节点构成的通信系统。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**CoG**
> 重心（**Center of Gravity**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Com**
> 通信（**Communication**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**Combined DTC**
> 普通 **DTC**，但被多个监视器报告的多个事件引用（例如 **ECU** 缺陷，由不同的硬件缺陷组成）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Context ID**
> 一个用户定义的标识符，用于对一个应用/**SW-C** 生成的日志和跟踪消息进行分组；Context ID 按 Application ID 分组，且在一个 Application ID 内唯一。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Continuous-MI counter**
> 持续 MI 被命令点亮期间发动机运行的小时数。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Conversion Mode**
> One-Shot：**ADC**通道组的转换在触发后执行一次，结果写入所分配的结果缓冲区。触发可以是软件**API**调用或硬件事件。Continuous：**ADC**通道组的转换在软件**API**调用（启动）后连续执行，结果写入所分配的结果缓冲区。转换本身自动运行（由硬件/中断控制）。连续转换可通过软件**API**调用（停止）停止。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**Conversion Time**
> 转换时间是指将采样的模拟值转换为数值所需的时间。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**COOP**
> 严重离位（**Critical Out of Position**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**Core**
> **CPU** 及其紧邻的功能资源。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**CPU**
> 中央处理器（**Central Processing Unit**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**CRC**
> 循环冗余校验（**Cyclic Redundancy Check**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Cross-Cluster External Graph**
> 一种特殊的**外部图**，在集群式软件架构下跨越多个**软件集群**（**Software Cluster**）。其配置依赖于模式（由**宿主软件集群**（**Host Software Cluster**）控制），并且另外具有专门的配置结构。注意：单个**软件集群**内的**外部图**可以在不使用集群式软件架构专门配置结构的情况下建模。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**CRYIF**
> 加密接口（**Crypto Interface**）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**CRYPTO**
> 加密驱动程序（**Crypto Driver**）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**Crypto Driver Object**
> 加密驱动程序对象：加密驱动程序实现一个或多个加密驱动程序对象，每个对象可以在硬件或软件中提供不同的加密原语；同一加密驱动程序的各加密驱动程序对象彼此独立，每个对象只有一个工作区（即同一时刻只能执行一个加密原语），独立性的唯一例外是默认随机数生成器的使用。
>
> 来源：[Utilization of Crypto Services（加密服务使用指南）](crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices）、[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**Crypto Primitive**
> 加密原语：在加密驱动程序对象中实现的已配置加密算法的实例；它指向 **CSM** 向应用程序提供的功能、具体的底层算法家族（如 **AES**、**MD5**、**RSA**）以及算法模式（如 **ECB**、**CBC**）。
>
> 来源：[Utilization of Crypto Services（加密服务使用指南）](crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices）、[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**CS**
> 片选（**Chip Select**）。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**CSM**
> 加密服务管理器（**Crypto Service Manager**）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**CSUM/Checksum/signature**
> 测试执行结果的数值表示。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**CTID**
> Context ID —— 上下文 ID。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**CTO**
> Command Transfer Object —— 命令传输对象。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**Cumulative Continuous-MI counter**
> 在其寿命期内 **MI** 被持续命令点亮的发动机运行小时数。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Current Time Tuple**
> 保存当前全局时间的本地实例及对应当前虚拟本地时间的时间元组。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**CVC**
> 卡片可验证证书（**Card Verifiable Certificate**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**CVT**
> 无级变速器（**Continuously Variable Transmission**）
>
> 来源：[Explanation of Application Interfaces of the Powertrain Engine Domain（动力总成（发动机）域应用接口说明）](application_interfaces/powertrain/index.md)（AUTOSAR_CP_EXP_AIPowertrain）
{: .glossary-source}

**CW**
> 竞争窗口（**Contention Window**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）
{: .glossary-source}

## D

**DAQ**
> Data AcQuisition, Data AcQuisition Packet —— 数据采集，数据采集包。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**DAS**
> 驾驶辅助系统（**Driver Assistance System**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Data frame**
> 数据帧：**SPI** 总线上与 SpiDataWidth 相关的位的物理帧。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**DCM**
> 诊断通信管理器（**Diagnostic Communication Manager**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**Deadline End Checkpoint**（**Deadline Stop Checkpoint**）
> 为其配置了**截止时间监督**、并且是某个特定**截止时间监督**终点的**检查点**。一个**检查点**可以同时是**截止时间起始检查点**和**截止时间结束检查点**——即当**截止时间监督**被串联时。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Deadline Start Checkpoint**
> 为其配置了**截止时间监督**、并且是某个特定**截止时间监督**起点的**检查点**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Deadline Supervision**
> 一种监督，用于检查两个**检查点**之间的执行时间是否小于给定的执行时间上限。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Debounce counter**
> 用于基于计数器去抖动算法的内部计数器。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Debounce Time**
> 具有相同 **PDU** 的两条 **TX** 报文之间的最小间隔。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**DEM**
> 诊断事件管理器（**Diagnostic Event Manager**）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver）、[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）、[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver）、[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）、[AUTOSAR Large Data COM（大数据 COM）](communication/large_data_com/index.md)（SWS_LargeDataCOM）
{: .glossary-source}

**Dem-internal data value**
> 某些数据值（例如发生计数器）由 **Dem** 模块自身在内部计算。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DemComponent / Monitored Component**
> 被监控组件是系统的一部分，由一个或多个监控检查其是否正常运行（参见第 6.5 节）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Denominator**
> 特定监视器 m 的分母（Denominatorm）是一个计数器，指示车辆驾驶事件的数量，并考虑该特定监视器特定的条件。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Dependent / Secondary ECUs**
> 从属/辅助 **ECU**（dep. / sec. ECU）始终与一个 **Master** 或 **Primary ECU** 相关联。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DET**
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver）、[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver）、[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Default Error Tracer（默认错误跟踪器）](system_services/default_error_tracer/index.md)（SWS_DefaultErrorTracer）、[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）、[AUTOSAR Large Data COM（大数据 COM）](communication/large_data_com/index.md)（SWS_LargeDataCOM）
{: .glossary-source}

**DHCP**
> Diagnostic Host Configuration Protocol —— 诊断主机配置协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**DID**
> 数据标识符（**Data Identifier**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DIP**
> 数字输入/输出（**Digital Input/Output**）
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**Directed acyclic graph**
> 没有循环依赖的依赖关系图。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Disciplined HW Clock**
> 可以在速率和偏移上被调整以跟随参考时钟的硬件时钟。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Displacement**
> 用需要存储的更重要的事件内存条目替换最不重要的条目。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Dlt**
> Diagnostic Log and Trace —— 诊断日志与跟踪。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Dlt User**
> 一个 **Dlt** 用户代表一个生成的 **Dlt** 消息的来源。可能的用户是 **SW-C**、RTE（用于 **VFB** 跟踪）、**DEM** 或 **DET**。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**DoS**
> 拒绝服务（**Denial of Service**）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**DP**
> DCC 配置（**DCC Profile**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）
{: .glossary-source}

**DRL**
> 日间行车灯（**Daytime Running Light**）
>
> 来源：[Safety Use Case（安全用例）](safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**&lt;DstLo&gt;**
> 作为 L-SDU 目标的下层通信接口模块。DstLo 可以是一对多。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**DTC**
> 拖滞力矩调节（**Regulation of the Drag Torque**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**DTC group**
> 唯一标识一组 **DTC**。一个 **DTC** 组被映射到有效 **DTC** 的范围内。通过提供一个 **DTC** 组，表示对该组中的所有 **DTC** 请求某一特定操作。**DTC** 组的定义由 ISO 14229-1 规定，并为 **OEM**/供应商特定。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DtcGroupAllDtcs**
> 所有已配置 **DTC** 的分组（表示为 0xFFFFFF）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DTO**
> Data Transfer Object —— 数据传输对象。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**DTR**
> 诊断测试结果（**Diagnostic Test Result**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DYC**
> **OBD** 术语：驾驶循环（**Driving Cycle**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

## E

**e.g.**
> （拉丁语）exempli gratia =（英语）for example，即「例如」。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**EAI**
> 期望存活指示（**Expected Alive Indications**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**EB**
> 外部缓冲通道（**Externally buffered channels**）：包含待传输数据的缓冲区位于 SPI 处理器/驱动程序之外。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**EBD**
> 制动力分配（**Electronic Brake Force Distribution**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**EC**
> 以太网控制器（**Ethernet controller**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**eCall**
> 紧急呼叫（**Emergency Call**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ECC**
> 纠错码（**Error Correction Code**）
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**ECU**
> 电子控制单元（**Electronic Control Unit**）
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**ECU ID**
> 一个 ECU 的名称，由四个 8 位 ASCII 字符组成（例如 ABS0 或 COMB）。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**ECU pin**
> ECU引脚（**ECU pin**）是**ECU**与电子系统其余部分的电气硬件连接。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**ECU Signal**
> ECU信号（**ECU Signal**）是电信号的软件表示。一个**ECU**信号具有一些属性（**Attribute**）和一个符号名称（**Symbolic name**）。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**ECU Signal Group**
> ECU信号组（**ECU Signal Group**）是一组电信号的软件表示。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**EcuC**
> **ECU** 配置（**ECU Configuration**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**EcuM**
> **ECU** 状态管理器（**ECU State Manager**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**EID**
> Entity identifier —— 实体标识符。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**Electrical Signal**
> 电信号（**Electrical Signal**）代表**ECU**引脚上的物理信号。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**EPB**
> 电子驻车制动（**Electronic Parking Brake**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Error**
> 错误。系统中的错误（软）状态，即该状态不同于若故障不存在时系统应有的状态；传播越过系统屏障即转变为失效（failure）。
>
> 来源：[Application Level Error Handling（应用层错误处理）](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

**ESC**
> 电子稳定控制（**Electronic Stability Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**ET**
> 以太网收发器（**Ethernet transceiver**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**Eth**
> Ethernet Controller Driver（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**EthIf**
> Ethernet Interface（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**EthTrcv**
> Ethernet Transceiver Driver（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**EthTSyn**
> **Ethernet** 的时间同步提供者模块（**Time Synchronization Provider module for Ethernet**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**Event combination**
> 事件组合是将多个事件合并为一个特定组合 **DTC** 的方法。它用于将不同的监视器结果适配为一个显著的、在维修站可清晰评估的故障。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event confirmation**
> 在通过故障确认计数器评估的、跨越多个周期或时间的合格事件的重复检测的情况下，诊断事件被确认。因此 **UDS** 状态位 3（ConfirmedDTC）被置位。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event debouncing**
> 去抖动是评估诊断事件是否被鉴定的特定机制（例如基于计数器）。它在潜在的信号去抖动之上工作，可以在 **SW-C** 内或 **Dem** 内进行。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event memory**
> 一个事件内存（例如主内存）由多个事件内存条目组成。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event memory entry**
> 事件内存条目是一个事件及其事件相关数据的单一存储容器。事件内存条目被动态分配给特定的事件。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event qualification**
> 在通过或失败结果被置位时（**Dem** 内部或由另一个 **BSW** 模块或 **SW-C** 报告），诊断事件被鉴定。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event related data**
> 事件相关数据是与事件一起存储在事件内存中的附加数据，例如传感器值或时间戳/里程。ISO 定义了两种类型的事件相关数据：冻结帧（快照记录）和扩展数据。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event status byte**
> 按 ISO 14229-1 定义、基于事件级别的状态字节。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Excel**
> Microsoft 电子表格应用（**Excel**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**Expired Supervision Cycle**
> 一个**监督周期**，其中**存活监督**已失败其两个升级步骤（**存活计数器**失败的**期望存活指示**数量（包括容差）超过允许的失败参考周期次数）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Extended data record**
> 扩展数据记录是用于存储与故障相关联的特定信息的记录。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**External client**
> 一种控制、监视和存储使用 **Dlt** 模块的 ECU 所提供的日志/跟踪消息的工具。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**External device**
> 物理外部实体；例如另一个微控制器。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**External Graph**
> 可能涉及多于一个**被监督实体**的**图**。其配置依赖于模式。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**External Transition**
> **外部转换**是两个**检查点**之间的**转换**，其中这两个**检查点**属于不同的**被监督实体**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Application Level Error Handling（应用层错误处理）](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

## F

**FA**
> 前轴（**Front Axle**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Failed Supervision Reference Cycle**
> 一个**监督参考周期**，其结束时刻检测到**存活计数器**与**期望存活指示**数量之间存在偏差（包括容差）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Failure**
> 失效。错误传播越过系统屏障、对系统环境可见后的结果：系统不再提供其规定的功能。
>
> 来源：[Application Level Error Handling（应用层错误处理）](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

**Failure counter**
> 失效计数器表示 ISO 14229-1 定义的 Trip Counter。Trip Counter 对发生故障的运行周期（驾驶循环）数进行计数。当计数器达到阈值（例如 2 个驾驶循环）时，confirmed 位从 0 变为 1。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Fallback Virtual Local Time**
> 从与导出主虚拟本地时间不同的硬件时钟导出的次级虚拟本地时间。可用于监视主虚拟本地时间，并在后者不可用时作为其本地替代。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Fast-Mode**
> 对看门狗硬件的触发必须以较短的超时期限完成。例如，该模式可用于 **ECU** 的正常运行。例如，看门狗硬件被配置为窗口模式（触发看门狗必须发生在超时期限内的特定最小/最大边界中）且超时期限为 5 毫秒。
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**Fault**
> 故障。系统的瞬态或永久性变化，使其完整性偏离预期的正确完整性；被激活并传播后成为错误（error）。
>
> 来源：[Application Level Error Handling（应用层错误处理）](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

**Fault Detection Counter**
> ISO 和 **FDC API** 中使用的 sint8 值。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**FCS**
> 帧校验序列（**Frame Check Sequence**）。
>
> 来源：[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）
{: .glossary-source}

**FDC**
> 故障检测计数器（**Fault Detection Counter**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**FDIR**
> 故障检测、隔离与恢复（**Fault Detection, Isolation and Recovery**）。系统运行期间处理故障的过程：检测→隔离→恢复。
>
> 来源：[Application Level Error Handling（应用层错误处理）](general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

**FID**
> 功能标识符（**Function Identifier**）：在 **FiM** 中标识一个应用程序功能及其相关禁止条件的标识符。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**FIFO**
> 先进先出缓冲区（**First In First Out buffer**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**FiM**
> 功能抑制管理器（**Function Inhibition Manager**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**FLM**
> 前灯管理（**Front Light Management**）
>
> 来源：[Safety Use Case（安全用例）](safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**FMI**
> 失效模式指示符（**Failure Mode Indicator**，SAE J1939）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Foreground test**
> 前台测试是同步测试，不得被中断。它通过用户应用程序调用。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**FOTA**
> 固件远程升级（**Firmware Over The Air**），通过无线通信进行固件远程更新。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）、[Explanation of Firmware Over-The-Air（固件远程升级说明）](memory/firmware_over_the_air/index.md)（AUTOSAR_CP_EXP_FirmwareOverTheAir）
{: .glossary-source}

**Fr**
> AUTOSAR 模块：FlexRay 驱动程序（**FlexRay Driver**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**Freeze frame**
> 冻结帧被定义为数据的记录（**DID**/**PID**）。冻结帧与 ISO 14229-1 中的 SnapShotRecords 相同。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Freshness Value**
> 用于确保经认证的时间同步报文新鲜度的单调计数器，可以是独立报文计数器（新鲜度计数器）或时间戳值（新鲜度时间戳）。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Freshness Value Manager**
> 新鲜度值管理器（**Freshness Value Manager**）。新鲜度值的提供者，**StbM** 充当 &lt;Bus&gt;TSyn 模块与 **FVM** 之间的接口。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**FrIf**
> FlexRay Interface —— FlexRay 接口。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）、[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**FrTp**
> AUTOSAR 模块：FlexRay 传输协议（**FlexRay Transport Protocol**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**FrTrcv**
> AUTOSAR 模块：FlexRay 收发器驱动程序（**FlexRay Transceiver Driver**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**FSC**
> 功能安全概念（**Functional Safety Concept**）
>
> 来源：[Safety Use Case（安全用例）](safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**FTB**
> 失效类型字节（**Failure Type Byte**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**FTT**
> 故障容忍时间（德语「Fehlertoleranzzeit」）（**Fault Tolerance Time**）
>
> 来源：[Safety Use Case（安全用例）](safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**FTTI**
> 故障容忍时间间隔（**Fault Tolerant Time Interval**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**Functionality**
> 功能：涵盖系统用户可见和用户不可见的功能方面（见 [2]）。在 **FiM** 上下文中，一个功能可以由一个或多个可运行实体的全部或部分内容、以同一组许可/禁止条件构成。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

## G

**General Denominator**
> 通用分母是一个计数器，指示车辆被操作的次数，并考虑通用条件。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**GID**
> Group identifier —— 组标识符。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**Global Supervision Status**
> 汇总所有**被监督实体****局部监督状态**的状态。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Global Time**
> 由全局时间主节点提供的时间值，即跨网络时间同步的参考时间。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Global Time Master**
> 全局时间主节点（**Global Time Master**）。某时基的系统级源头，其时基值通过网络分发给各时基从节点。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**GM(C)**
> 顶级主节点（时钟）（**Grand Master (Clock)**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**Golden (Ref.) Value**
> 用于与先前计算出的测试结果值进行比较的参考值（例如校验和/签名）。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Good Case**
> 执行完成且未报告错误。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**GPT**
> 通用定时器（**General Purpose Timer**）
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**GPT Predef Timer**
> **GPT Predef Timer** 是 **GPT** 驱动程序提供的自由运行递增计数器。哪些 **GPT Predef Timer** 可用取决于硬件（时钟、硬件定时器、预分频器、定时器寄存器宽度等）和配置。**GPT Predef Timer** 具有预定义的物理时间单位和范围。
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**Graph**
> 控制流图（**Control Flow Graph**）。一组通过**转换**相连的**检查点**，其中至少有一个**检查点**是**初始检查点**。在该**图**的任意两个**检查点**之间都存在一条（通过**转换**的）路径。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

## H

**HARA**
> 危害分析（**Hazard Analysis**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**Hardware Trigger**
> 硬件触发是**ADC**内部触发信号，用于启动ADC通道组的一次转换。**ADC**硬件触发在ADC硬件内部生成（例如：基于**ADC**定时器或触发沿信号）。触发硬件是强耦合或者直接集成在**ADC**的硬件中。当检测到硬件触发后，无需软件即可启动**ADC**通道组转换。**注意：**即使**ADC**硬件不支持硬件触发，也可以通过软件触发结合**GPT/ICU**驱动程序来实现类似的行为。（例如：在GPT定时器通知函数中，启动软件触发的**ADC**通道组的转换）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**HAZOP**
> 危害与可操作性分析（**Hazard & Operability Analysis**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**HDC**
> 坡道缓降控制（**Hill Decent Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Healing**
> 关闭警告指示器，包括对在一段时间/若干运行周期内报告的通过结果的处理。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**HHC**
> 坡道起步控制（**Hill Hold Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**HMI**
> 人机接口（**Human Machine Interface**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**hold-over**
> 主时间源（通常）暂时不可用，而另一个时间源提供（可能降级的）时间信息的场景。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**HSM**
> 硬件安全模块（**Hardware Security Module**），专用安全 **MCU** 的内核。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）、[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**HTM**
> 硬件测试管理器（**Hardware Test Manager**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**HW**
> 硬件（**Hardware**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

## I

**I-PDU**
> 交互层 **PDU**（**Interaction Layer PDU**）。在 **AUTOSAR** 中，交互层等价于通信服务层。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**I-PDU ID**
> I-PDU 标识符（**I-PDU Identifier**）。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**i.e.**
> （拉丁语）id est =（英语）that is，即「也就是说」。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**IB**
> 内部缓冲通道（**Internally buffered channels**）：包含待传输数据的缓冲区位于 SPI 处理器/驱动程序之内。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**ICC**
> 实现一致性等级（**Implementation Conformance Class**）。AUTOSAR 对基础软件实现合规程度的分级（ICC1–ICC3）：ICC3 要求逐模块符合 AUTOSAR 规范，ICC2 允许项目定义的集群，ICC1 为专有基础软件（对外行为仍须符合 ICC3 模块规范）。
>
> 来源：[Layered Software Architecture（分层软件架构）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）
{: .glossary-source}

**ICMP**
> Internet Control Message Protocol —— 互联网控制消息协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**ICU**
> 输入捕获单元（**Input Capture Unit**）
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**ICV**
> 完整性校验值（**Integrity Check Value**）。为时间同步报文提供完整性和真实性保护的校验值。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**ID**
> 标识符（**Identifier**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**IdsM**
> 入侵检测系统管理器（**Intrusion Detection System Manager**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**&lt;Ie&gt;**
> 实现特定文件名扩展名（**implementation specific file name extension**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**IF-PDU**
> 通过 SoAd 的 IF-API 发送/接收的 PDU。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**IFL**
> 浮点插值库（**Floating Point Interpolation Routines**）的模块 ID 前缀；浮点插值例程名称以 Ifl 开头。
>
> 来源：[Macro Encapsulation of Interpolation Calls（插值调用宏封装）](libraries/macro_encapsulation_of_interpolation_calls/index.md)（AUTOSAR_CP_EXP_MacroEncapsulationofInterpolationCalls）
{: .glossary-source}

**IFX**
> 定点插值库（**Fixed Point Interpolation Routines**）的模块 ID 前缀；整数插值例程名称以 Ifx 开头。
>
> 来源：[Macro Encapsulation of Interpolation Calls（插值调用宏封装）](libraries/macro_encapsulation_of_interpolation_calls/index.md)（AUTOSAR_CP_EXP_MacroEncapsulationofInterpolationCalls）
{: .glossary-source}

**In-Use performance ratio**
> **OBD** 系统特定监视器 m 的实际使用性能比为：IUPRm = Numeratorm / Denominatorm。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Inhibition Condition**
> 禁止条件：一个 **FID**、一个禁止掩码与 **Dem** 事件/组件状态之间的关系（见 FiMInhibitionConfiguration）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**int**
> 整数（**Integer**）
>
> 来源：[AUTOSAR Platform Types（平台类型）](general/platform_types/index.md)（SWS_PlatformTypes）
{: .glossary-source}

**Internal Graph**
> 不跨越若干**被监督实体**的**图**。其配置与模式无关，并且可以通过禁用对应的**被监督实体**而被禁用。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Internal Transition**
> **内部转换**是同一个**被监督实体**内两个**检查点**之间的**转换**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Inversion**
> 物理值与逻辑值的反转（**Inversion**）。此属性不可见，但可以由**I/O**硬件抽象来实现，并向用户传递预期值。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**IoHwAb**
> 输入/输出硬件抽象（**Input/Output Hardware Abstraction**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**IP**
> Internet Protocol —— 互联网协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**IPv4**
> Internet Protocol version 4 —— 互联网协议第 4 版。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**IPv6**
> Internet Protocol version 6 —— 互联网协议第 6 版。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**IRQ**
> 中断请求（**Interrupt Request**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**ISR**
> 中断服务程序（**Interrupt Service Routine**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping）、[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）
{: .glossary-source}

**IUMPR**
> 在使用中的监控性能比（**In-Use-Monitor Performance Ratio**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

## J

**J1939Dcm**
> SAE J1939 诊断通信管理器（**SAE J1939 Diagnostic Communication Manager**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Job**
> 作业：一个已配置的 **CsmJob**，它引用一个密钥、一个加密原语和一个参考通道。
>
> 来源：[Utilization of Crypto Services（加密服务使用指南）](crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices）、[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**Job Request**
> 作业请求（**Job Request**）是指上层模块对地址区的存储访问请求。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

## K

**Key**
> 密钥：密钥可以被 **Csm** 中的作业引用；在加密驱动程序中，每个密钥引用一种特定的密钥类型。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**Key Element**
> 密钥元素：用于存储数据（例如 **AES** 加密所需的密钥材料或 **IV**），也可用于配置密钥管理功能的行为；不同密钥的密钥元素拥有不同的存储区域（**NV** 区域和 **RAM** 区域）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**Key Type**
> 密钥类型：由对密钥元素的引用组成，通常由加密驱动程序的供应商预先配置。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

## L

**L-PDU**
> 数据链路层 **PDU**（**Data Link Layer PDU**）。在 **AUTOSAR** 中，数据链路层等价于通信硬件抽象和微控制器抽象层。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L-PDU ID**
> L-PDU 标识符（**L-PDU Identifier**）。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L-SDU**
> 链路层服务数据单元（**Data link layer service data unit**）。一个 L-SDU 由数据（缓冲区）、长度、L-SDU ID 以及可能经由元数据传输的 L-PDU 特定信息组成。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L-SDU ID**
> L-SDU 标识符（**L-SDU identifier**）。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L-SDU Router**
> 在模块之间传输 L-SDU 的模块。L-SDU Router 模块可用于内部路由目的。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L1**
> 第一级存储器（**1st level memory**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**L2**
> 第二级存储器（**2nd level memory**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**LB**
> 近光功能（德语「Abblendlicht」）（**Low Beam**）
>
> 来源：[Safety Use Case（安全用例）](safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**LED**
> 发光二极管（**Light Emitting Diode**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**LET**
> 逻辑执行时间——通过抽象物理执行来确保稳定软件行为的概念（**Logical Execution Time**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**LKA**
> 车道保持辅助（**Lane Keep Assist**）。
>
> 来源：[Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC）
{: .glossary-source}

**&lt;Lo&gt;**
> 下层通信接口模块。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**Local Instance of the Global Time**
> 在从全局时间主节点接收到两个时间值采样之间，借助虚拟本地时间或受控硬件时钟对时间当前值的本地外推。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Local Supervision Status**
> 表示单个**被监督实体**当前存活监督结果的状态。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Log and trace level**
> 日志级别为日志消息的严重程度定义了一种分类。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Log and trace message**
> 包含描述软件中一个日志和跟踪事件的所有数据和选项的消息；由头部和载荷组成。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Log Channel**
> 用于传输 **Dlt** 消息的物理通信总线。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Log Message**
> 包含诸如状态变化或值变化之类调试信息的消息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Logical Supervision**
> 一种对软件的在线监督，用于检查软件（**被监督实体**或一组**被监督实体**）是否按程序员（即已开发的代码）定义的顺序执行。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Lower Layer Modules（Lo）**
> 位于 L-SDU Router 之下的模块。该层包括以太网通信接口模块。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**LPDU**
> Data Link Layer PDU —— 数据链路层 PDU。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**LPdu**
> 数据链路层协议数据单元（**Datalink layer Protocol Datagram Unit**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**LS**
> 灯光开关（**Light Switch**）
>
> 来源：[Safety Use Case（安全用例）](safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

## M

**&lt;MA&gt;**
> 大写模块缩写（**Capitalized module abbreviation**），即完全以大写形式书写的模块缩写 &lt;Ma&gt;
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**&lt;Ma&gt;**
> 模块缩写（**Module abbreviation**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**MAC**
> 报文认证码（**Message Authentication Code**）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**Macrotick**
> 宏节拍——FlexRay 集群全局同步时间的最小单位。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**Main Time Triple**
> 参考时间三元组 [TL_Main, TV_Main, TV_Fallback]，在主时间元组基础上增加了第三个成员——在主时间元组被更新的时刻采样的备用虚拟本地时间。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Main Time Tuple**
> 参考时间元组 [TL_Main, TV_Main]，用于在不支持受控硬件时钟的情况下基于主虚拟本地时间计算全局时间的本地实例。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**MAKW**
> 内存分配关键字（**Memory Allocation Key Word**）
>
> 来源：[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping）
{: .glossary-source}

**Master**
> 主。分布式 BSW 模块中协调卫星请求、并可过滤或监控进入的卫星请求的部分。
>
> 来源：[BSW Distribution Guide（BSW 分布指南）](general/bsw_distribution_guide/index.md)（AUTOSAR_CP_EXP_BSWDistributionGuide）
{: .glossary-source}

**Master ECU**
> 与 **Primary ECU** 一样，**Master ECU** 在其事件内存中存储"自己的"以及相关的从属/辅助 **ECU** 的"报告的错误"。除此之外，**Master** 必须履行特殊的 **Master** 任务，如 **MIL Master** 或提供"通用分子"信息。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**MCAL**
> 微机抽象层（**Microcomputer Abstraction Layer**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）、[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**MCD**
> Measurement Calibration and Diagnostics —— 测量、标定与诊断。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**MCG**
> 模块配置生成器（**Module Configuration Generator**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）、[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）
{: .glossary-source}

**MCNT**
> Message Counter —— 消息计数器。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MCU**
> 微控制器单元（**Microcontroller Unit**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver）、[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Memory Device**
> 存储设备（**Memory Device**）是指一组存储 **Bank** 的组合。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Message ID**
> 用于表征消息自身所传输信息的 ID；唯一地标识一种日志或跟踪消息，并在开发或配置时静态固定。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MII**
> 媒体独立接口（**Media Independent Interface**，由以太网控制器提供的用于访问以太网收发器的标准化接口，参见 IEEE 802.3-2006）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**MIL**
> 故障指示灯（**Malfunction Indication Light**）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**&lt;MIP&gt;**
> 大写模块实现前缀（**Capitalized module implementation prefix**），即完全以大写形式书写的模块实现前缀 &lt;Mip&gt;
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**&lt;Mip&gt;**
> 模块实现前缀（**Module implementation prefix**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**MISO**
> Master Input Slave Output（主入从出）。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**MISRA**
> 汽车工业软件可靠性协会（**Motor Industry Software Reliability Association**）。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**Modality**
> 模态——到用户的输出通道的类型，例如音频或视频输出（**Modality**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**Mode**
> 模式是车辆中运行的各个状态机的特定状态集合，这些状态与某个特定实体相关，例如 **SW-C**、**BSW** 模块、应用或整个车辆。在其生命周期内，一个实体在一组互斥的模式之间切换。这些切换由环境数据触发，例如信号接收、操作调用。在**看门狗管理器**的上下文中，一个模式由一组配置选项定义。被监督的**被监督实体**集合可以随模式而变化。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Module abbreviation**
> 模块缩写（**Module abbreviation**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**Module implementation prefix**
> 模块实现前缀（**Module implementation prefix**），用于构成 BSW 模块实现的工作成果中使用的各种标识符（例如 API 名称、参数名称、符号和文件名），主要由模块缩写构成，必要时加上额外的厂商特定信息
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**Monitor**
> 诊断监视器是确定组件是否正常运行的例程实体。也可以使用术语"诊断功能"。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Monitoring function**
> 监控功能：软件组件的一部分；用于监控并最终检测某个传感器、执行器故障或进行合理性检查的机制；报告来自 **SW-C** 内部处理或来自其他块返回值进一步处理的事件状态。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**MOSI**
> Master Output Slave Input（主出从入）。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**MPU**
> 内存保护单元（**Memory Protection Unit**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**MS**
> 里程碑（**Milestone**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**MSBF**
> Most Significant Byte First —— 最高有效字节在前。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSBI**
> Message Bus Info —— 消息总线信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSCI**
> Message Control Info —— 消息控制信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSLI**
> Message Log Info —— 消息日志信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSTI**
> Message Trace Info —— 消息跟踪信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSTP（Message Type）**
> Message Type —— 消息类型。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSTP（Microcontroller Specific Test Package）**
> 微控制器特定测试包（**Microcontroller Specific Test Package**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

## N

**N-PDU**
> 网络层 **PDU**（**Network Layer PDU**）。在 **AUTOSAR** 中，网络层等价于传输协议。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**neighborRateRatio**
> **IEEE 802.1AS** 定义的邻速率比。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**NIT**
> FlexRay 网络空闲时间（**FlexRay Network Idle Time**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**NOAR**
> Number of Arguments —— 参数数量。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**nop**
> 无操作（**No Operation**）。
>
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**NOP, nop**
> 空操作（**Null Operation**）
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**Notification Time Base Customer**
> 一种时基客户，当时基状态改变或时基值到达客户先前设置的给定值时，由同步时基管理器通知。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Numerator**
> 特定监视器 m 的分子（Numeratorm）是一个计数器，指示车辆被操作的次数，使得检测该特定监视器故障所需的所有监控条件都已被满足。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**NVH**
> 噪声、振动、平顺性（**Noise, Vibration, Harshness**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**NVRAM**
> 非易失性 RAM（**Non-Volatile RAM**）
>
> 来源：[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping）
{: .glossary-source}

## O

**OA TC10**
> Open Alliance TC10（参见 OPEN Sleep/Wake-up Specification for Automotive Ethernet）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**OBD**
> 车载诊断（**On-board Diagnostics**）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**OBD ECUs**
> 车辆中可以有 3 种不同类型的 **OBD ECU**：**Master ECU**（每车一个）、**Primary ECU**（每车多个）、从属/辅助 **ECU**（每车多个）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**OBD UDS DTC separation**
> 该特性为基于 SAE J1979-2 的 **UDS** 通信报告与其它 J1979-2 **UDS** 通信不同的 3 字节 **DTC** 编号。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**OBDII**
> 排放相关车载诊断（**Emission-related On-board Diagnostics**）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**OC**
> 发生计数（**Occurrence Count**，SAE J1939）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**OD**
> 乘员检测（**Occupant Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ODT**
> Object Descriptor Table —— 对象描述表。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**Off-Mode**
> 看门狗硬件被禁用/关闭。这样做可能是为了关闭整个 **ECU**，而不遭受仍在运行的外部看门狗的周期性复位。对于安全关键系统，该模式可能不被允许。在这种情况下，必须将 **Wdg** 模块配置为禁止切换到此模式。
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**Offset Correction**
> 补偿时间偏移所需的偏移值。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Offset Time Base**
> 只与其底层同步时基结合存在的时基；其绝对时间值由偏移时基的偏移时间值加上底层同步时基的时间值得到。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**OFNS message**
> 偏移调整报文（Offset adjustment message）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**OFS message**
> 偏移同步报文（**Offset Synchronization message**）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**OID**
> 对象标识符（**Object Identifier**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**OOP**
> 离位（**Out Of Position**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**OPC**
> 乘员预处理（**Occupant Pre Conditioning**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**Operating cycle**
> "运行周期"是事件鉴定和 **Dem** 调度的基础（例如点火钥匙关-开循环、驾驶循环等）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Operation**
> 操作：加密原语的操作声明应执行加密原语的哪一部分，共有 **START**、**UPDATE**、**FINISH** 三种操作模式；通过拼接操作模式参数的相应位可以一次执行多个操作。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**OPS**
> 乘员与行人安全（**Occupant and Pedestrian Safety**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**OPSS**
> OPS 系统（**OPS Systems**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ORA**
> 乘员约束激活（**Occupant Restraint Activation**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ORTI**
> OSEK 运行时接口——针对 OSEK 平台将跟踪工具对 OS 内部的访问标准化的标准（**OSEK Run-Time Interface**）
>
> 来源：[ARTI（AUTOSAR 运行时接口）](sw_arch/arti/index.md)（AUTOSAR_CP_EXP_ARTI）
{: .glossary-source}

**OS**
> 操作系统（**Operating System**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**OSEK/VDX**
> 1993 年 5 月，**OSEK** 作为德国汽车工业的一个联合项目创立，旨在为车辆内分布式控制单元的开放式架构建立一个行业标准。**OSEK** 是德语术语「Offene Systeme und deren Schnittstellen für die Elektronik im Kraftfahrzeug」（英语：Open Systems and the Corresponding Interfaces for Automotive Electronics）的缩写。初始项目合作伙伴为 **BMW**、**Bosch**、**Daimler Chrysler**、**Opel**、**Siemens**、**VW** 以及作为协调方的卡尔斯鲁厄大学 **IIIT**。法国汽车制造商 **PSA** 和 **Renault** 于 1994 年加入 **OSEK**，引入了他们的 **VDX**（**Vehicle Distributed eXecutive**）方案——法国汽车工业内的一个类似项目。在 1995 年 10 月的第一次研讨会上，**OSEK/VDX** 小组展示了 **OSEK** 与 **VDX** 之间协调一致的规范成果。1997 年 10 月第 2 届国际 **OSEK/VDX** 研讨会之后，发布了规范的第二版。
>
> 来源：[AUTOSAR Standard Types（标准类型）](general/standard_types/index.md)（SWS_StandardTypes）、[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**OTA**
> 远程升级（**Over The Air**），OEM 后台（**backend**）与车辆之间无线通信的总称。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**OVS**
> 溢出秒值（**Overflow Seconds** value，**FUP** 报文中的字段）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

## P

**P-Code**
> 动力总成代码（**Power train code**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**P2P**
> 点对点（**Point-to-Point**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**Page Burst**
> 通过聚合访问存储页面来提高性能。在存储设备技术支持物理分段的情况下，一些存储设备可以提供一次读取或写入多个页面的优化访问方式。页面突发（**Page Burst**）表示用于访问优化的存储页面聚合。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Partial test**
> 部分测试定义为一个或多个「硬件资源」的测试。（部分测试是可中断的，因为它在后台模式下执行。）
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**PASE**
> 无源进入（**Passive Entry**）。帮助用户无需物理使用钥匙即可进入汽车的锁定系统。
>
> 来源：[Explanation of Application Interfaces of the Body and Comfort Domain（车身与舒适域应用接口说明）](application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort）
{: .glossary-source}

**PCD**
> 行人碰撞检测（**Pedestrian Crash Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**PCI**
> 协议控制信息（**Protocol Control Information**）。把一个 SDU 从协议层的一个实例传递到另一个实例所需的信息，例如源与目标信息。PCI 由发送侧的协议层添加，在接收侧移除。PDU 包含 SDU 和 PCI。
>
> 来源：[Layered Software Architecture（分层软件架构）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）
{: .glossary-source}

**PCP**
> 行人碰撞预测（**Pedestrian Crash Prediction**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**PDC**
> 泊车距离控制（**Park Distance Control**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**Pdelay**
> **IEEE 802.1AS** 给出的传播/路径延迟（Propagation / path delay）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**PDU**
> 协议数据单元（**Protocol Data Unit**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[Layered Software Architecture（分层软件架构）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）、[VFB（虚拟功能总线）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）、[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**Permission state**
> 许可状态：包含由其 **FID** 表示的功能是否可以执行的信息。该状态由 **FiM** 基于已报告的事件控制。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**PFC cycle**
> 永久故障代码——驾驶循环（**OBD** 术语）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**PID**
> 参数标识（**Parameter Identification**，SAE J1587 或 SAE J1979）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**PKI**
> 公钥基础设施（**Public Key Infrastructure**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**PLCA**
> 物理层冲突避免（**Physical Layer Collision Avoidance**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**PNC**
> 部分网络集群（**Partial Network Cluster**）。一组系统信号，用于支持分布在车辆网络多个 ECU 上的一个或多个车辆功能；表示把一组总线映射到一个或多个虚拟功能集群（VFC）的系统视图。
>
> 来源：[Layered Software Architecture（分层软件架构）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）
{: .glossary-source}

**POC**
> 协议运行控制（**Protocol Operation Control**，详情参见 ISO 17458-1）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**POCState**
> **CC** 内部的 **POC** 实际状态。该状态在某些情况下可能与 vPOC!State 不同，例如在 FREEZE 命令调用之后（详情参见 ISO 17458-1）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**POD**
> 俯仰翻覆碰撞检测（**Pitchover Crash Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**Port-Interface**
> 端口接口。定义提供或要求该接口的端口必须履行的契约；AUTOSAR 支持客户端-服务器、发送者-接收者、参数、非易失性数据、触发与模式切换六种端口接口。
>
> 来源：[VFB（虚拟功能总线）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**Positive Callback from NvM**
> 如果需要在 Dem_Init 和 Dem_Shutdown 之间存储数据，**Dem** 模块应使用 **NVRAM** 管理器的 **API** NvM_WriteBlock 和 NvM_GetErrorStatus。此外，**API** NvM_GetErrorStatus 应等待块写入成功完成的肯定响应。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**PPA**
> 行人保护执行器激活（**Pedestrian Protection Actuator Activation**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**PPP**
> 行人保护系统预处理（**Pedestrian Protection system Pre conditioning**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**Primary ECU**
> **Primary ECU** 在其事件内存中存储"自己的"以及相关的从属/辅助 **ECU** 的"报告的错误"。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Primitive**
> 原语：在加密驱动程序对象中实现的已配置加密算法的实例；它指向 **CSM** 向应用程序提供的功能、具体的底层算法家族（如 **AES**、**MD5**、**RSA**）以及算法模式（如 **ECB**、**CBC**）。
>
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**Priority**
> 优先级：作业的优先级定义其重要性，优先级（数值）越高，作业越需立即执行；加密作业的优先级是配置的一部分。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**Processing**
> 处理：指示作业处理的类型。异步（**Asynchronous**）：调用相应函数时作业不会被立即处理，通常由后续的调度函数处理并通过回调通知结果；同步（**Synchronous**）：调用相应函数时作业被立即处理，函数返回时结果已可用。
>
> 来源：[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**Prototype**
> 原型。组件类型在一个组合（Composition）中的使用；组合经由相互连接的原型定义。
>
> 来源：[VFB（虚拟功能总线）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**Proxy Module**
> 替代应用软件集群中一个 BSW 模块的模块，拆分为高代理与低代理（**Proxy Module**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**PTC**
> 动力总成协调器（**Powertrain Coordinator**）
>
> 来源：[Explanation of Application Interfaces of the Powertrain Engine Domain（动力总成（发动机）域应用接口说明）](application_interfaces/powertrain/index.md)（AUTOSAR_CP_EXP_AIPowertrain）
{: .glossary-source}

**PTO**
> 动力输出（**Power Take Off**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**PTP**
> 精确时间协议（**Precision Time Protocol**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**Pure Local Time Base**
> 只在本地被设置和读取、不通过 Timesync 模块同步但随时间推进的时基；只支持 **API** 的一个子集。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

## R

**RA**
> 后轴（**Rear Axle**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**RAM**
> Random Access Memory —— 随机访问存储器。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**Range**
> 范围（**Range**）在这里是一个功能范围（**functional range**），而不是电气范围（**electrical range**）。所有范围都用于功能的需要或者诊断的检测。对于模拟**ECU**信号，可以定义上下限值 [lowerLimit...upperLimit]（电压、电流）。对于电阻信号和时序信号（周期）的特殊情况，下限值（**lowerLimit**）不能为负。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Rate Correction**
> 补偿速率偏差所需的因子。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Rate Deviation**
> 速率偏差值表示时钟的频率偏离参考时钟速率的程度。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**RBM cycle**
> **OBD** 术语：通用分子/基于比率的监控——驾驶循环。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Readiness**
> 就绪状态指 **UDS** 状态字节的已测试位 TestNotCompletedSinceLastClear（位 4）和 TestNotCompletedThisOperationCycle（位 6）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Reference time**
> 参考时间：为每个计时器实例存储的时间值，是 **API** 数据类型 Tm_PredefTimer...bitType 所对应的实现特定元素。
>
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**Resolution**
> 分辨率（**Resolution**）属性适用于依赖于范围和数据类型的许多类别。如：(upperLimit - lowerLimit) / (2<sup>datatypelength</sup> -1)。 对于其他类别，它可能是已知和被定义的。如：[-12 Volts…+12Volts]，数据类型: 16 bits，**Resolution** 为 24 / 65535。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Resource**
> 「硬件资源」是 **CoreTest** 驱动程序用户可以选择的最小单元（实例）。它可以在一个或多个原子序列中被测试。它是执行特定功能（例如 **IRQ** 控制器）的内核内部单元。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**retransmit counter**
> 部分 **CAN XL** 控制器提供的一项特性：当 **ACK** 槽未在总线上置位时，允许将一个 **CAN** 帧连续多次发送。该计数器给出了最大发送次数。
>
> 来源：[AUTOSAR CAN XL Driver（CAN XL 驱动程序）](communication/canxl_driver/index.md)（SWS_CANXLDriver）
{: .glossary-source}

**RKE**
> 遥控无钥匙进入（**Remote Keyless Entry**）。设计用于远程锁定或解锁汽车进入的系统；单向广播无线电波，实现加密与滚动码算法。
>
> 来源：[Explanation of Application Interfaces of the Body and Comfort Domain（车身与舒适域应用接口说明）](application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort）
{: .glossary-source}

**ROD**
> 翻滚碰撞检测（**Rollover Crash Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**Rollover mechanism**
> 下面的示例序列被称为"回绕"（**rollover**）：一个无符号字符（**unsigned char**）的值为 255；将其加 1；结果为 0。
>
> 来源：[AUTOSAR Platform Types（平台类型）](general/platform_types/index.md)（SWS_PlatformTypes）
{: .glossary-source}

**ROM**
> Read Only Memory —— 只读存储器。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**RSC**
> 侧翻稳定控制（**Roll Stability Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**RSM**
> 约束系统监测（**Restraint System Monitoring**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**RSP**
> 约束系统预处理（**Restraint System Pre conditioning**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**RTE**
> 运行时环境（**Runtime Environment**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Runnable**
> 可运行体。原子软件组件实现中的一段可由 RTE 启动的指令序列；在任务的上下文中运行。
>
> 来源：[VFB（虚拟功能总线）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**Runnable entity**
> 可运行实体：原子软件组件的一部分，可以独立于该原子软件组件的其他可运行实体被执行和调度。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**RWW**
> 并行读写（**Read While Write**）。指存储设备在一个存储 **Bank** 中执行读取操作，同时在另一个存储 **Bank** 中执行写入或擦除操作的能力。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Rx Time Tuple**
> 时间元组 [TG_Rx, TV_Rx]，在跟随报文进入时导出，并由 &lt;Bus&gt;TSyn 模块通过 StbM_BusSetGlobalTime 交给 **StbM**。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

## S

**S/R**
> 发送方/接收方（**Sender/Receiver**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Sampling rate**
> 采样率（**Sampling rate**）是获得信号值所需的时间段。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Sampling Time, Sample Time**
> 采样时间是指对模拟值进行采样的时间（例如：加载电容器，……）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**Satellite**
> 卫星。分布式 BSW 模块的一部分；主与卫星之间的工作分配是实现特定的，卫星一般不能在没有主的情况下工作。
>
> 来源：[BSW Distribution Guide（BSW 分布指南）](general/bsw_distribution_guide/index.md)（AUTOSAR_CP_EXP_BSWDistributionGuide）
{: .glossary-source}

**SBR**
> 安全带提醒（**Seat Belt Reminder**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**SC**
> 监督周期（**Supervision Cycle**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**SchM**
> Schedule Manager —— 调度管理器。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**SDU**
> 服务数据单元（**Service Data Unit**）——**PDU** 的载荷。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR Platform Types（平台类型）](general/platform_types/index.md)（SWS_PlatformTypes）、[Layered Software Architecture（分层软件架构）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）、[VFB（虚拟功能总线）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）、[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**SDU type**
> 服务数据单元类型（**service data unit type**）。
>
> 来源：[AUTOSAR CAN XL Driver（CAN XL 驱动程序）](communication/canxl_driver/index.md)（SWS_CANXLDriver）
{: .glossary-source}

**SE**
> 被监督实体（**Supervised Entity**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Sector**
> 扇区（**Sector**）是指最小的可擦除存储单元（以字节为单位）。某些存储设备技术在写入存储前需要显式执行物理擦除操作。扇区定义了此类擦除单元的最小大小。根据存储设备的不同，扇区可以为统一大小或可变大小。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Sector Batch**
> 扇区批次（**Sector Batch**）是大小统一的扇区集合，即大小相同且连续的扇区的逻辑集合。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Sector Burst**
> 扇区突发（**Sector Burst**）是聚合扇区以提高擦除性能。如果存储技术需要物理擦除操作，一些设备会通过一步擦除一组扇区来优化擦除性能。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Sender-receiver communication**
> 发送方-接收方通信涉及原子数据元素组成的信号的发送和接收，这些原子数据元素由一个组件发送给另一个或多个组件。发送方-接收方接口可以包含多个数据元素。发送方-接收方通信是单向的 接收方发送的任何回复都可以视为一个单独的发送方-接收方通信。接收方组件的端口可以读取接口描述定义的数据元素，而提供方组件的端口可以按照接口描述定义写入数据元素。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**SEooC**
> 脱离语境的安全要素（**Safety Element out of Context**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**Sequence**
> 序列：若干个待传输的连续作业，但可以使用优先级机制在作业之间重新调度；序列传输是否可被中断取决于静态配置。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**Service**
> 服务：按 **TR_Glossary** 文档的定义理解——服务是一种具有已发布的接口和行为规范的操作，涉及功能提供者与潜在客户之间的合同。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**Session**
> 日志或跟踪消息来源的一个逻辑实体；如果一个应用/**SW-C** 打开了多个到 **Dlt** 的端口，则它可以拥有多个并发的日志或跟踪会话。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Session ID**
> 一个日志或跟踪会话的标识编号。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**SFR**
> 特殊功能寄存器（**Special Function Register**），**MCU** 寄存器
>
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver）
{: .glossary-source}

**SGW**
> 时间同步的「已同步到网关」（**Synchronized to Gateway**）状态。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**SHE**
> 安全硬件扩展（**Security Hardware Extension**）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**Slow-Mode**
> 对看门狗硬件的触发可以以较长的超时期限完成。例如，该模式可用于系统启动/初始化阶段。例如，看门狗硬件被配置为翻转模式（对触发的时间点没有约束）且超时期限为 20 毫秒。
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**Software Trigger**
> 软件触发是一个软件**API**调用，用于启动转换一个**ADC**通道组或一系列连续**ADC**通道组转换的。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**SOTA**
> 软件远程升级（**Software Over The Air**），使用无线通信进行软件远程更新。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**SP**
> 传感器池（**Sensor Pool**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**SPEM**
> 软件过程工程元模型（**Software Process Engineering meta-model**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**SPI**
> 串行外设接口（**Serial Peripheral Interface**）
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**SPN**
> 可疑参数编号（**Suspect Parameter Number**，SAE J1939）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**SR**
> 态势识别（**Situation Recognition**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**SRC**
> 监督参考周期（**Supervision Reference Cycle**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**&lt;SrcLo&gt;**
> 作为 L-SDU 源的下层通信接口模块。SrcLo 始终只有一个。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**SRS（Safety Restraint System）**
> 安全约束系统（**Safety Restraint System**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**SRS（Software Requirements Specification）**
> Software Requirements Specification —— 软件需求规范。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**SSCP**
> 同步服务器调用点（**synchronous server call point**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**SSM**
> 静止管理（**Stand Still Manager/Management**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**StbM**
> 同步时基管理器（**Synchronized Time-Base Manager**）。向其客户提供与分布式系统其他节点上的时基同步的时基的基础软件模块。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**STD**
> 标准（**Standard**）
>
> 来源：[AUTOSAR Standard Types（标准类型）](general/standard_types/index.md)（SWS_StandardTypes）
{: .glossary-source}

**STIM**
> Data Stimulation packet —— 数据激励包。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**STMS**
> Timestamp —— 时间戳。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Sub Address Area**
> 子地址区（**Sub Address Area**）是指逻辑地址空间中的连续存储区域，并映射到一个存储设备的一个扇区批次（**Sector Batch**）。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Supervised Entity**
> 被纳入**WdgM** 监督的软件实体。每个**被监督实体**恰好具有一个标识符。**被监督实体**表示软件组件类型或基础软件模块某个实例内的一组**检查点**。在一个软件组件类型或基础软件模块的实例中，可以有零个、一个或多个**被监督实体**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Supervised Entity Identifier**
> 在一个应用内唯一标识某个**被监督实体**的**标识符**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Supervision Counter**
> 在**被监督实体**上下文内的独立数据资源，由**WdgM** 在每个**监督周期**期间更新，并被**存活监督**算法用于执行对已计数**存活指示**的检查。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Supervision Cycle**
> **WdgM****监督参考周期**的时基，在其中执行周期性的**存活监督**。它同时也是更新**全局监督状态**以及执行由此产生的恢复动作的间隔。这在所属 **WdgM** 的主函数每次被调用时完成，并且依赖于模式（在切换模式时可能变化）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Supervision Reference Cycle**
> **存活监督**用于执行已计数**存活指示**检查所使用的**监督周期**数量（对每个**被监督实体**分别确定），并且依赖于模式。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**SVN**
> Subversion（版本控制系统）（**Subversion**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**SW**
> 软件（**Software**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Crypto Driver（加密驱动程序）](crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](crypto/crypto_interface/index.md)（SWS_CryptoInterface）
{: .glossary-source}

**SW-C**
> 软件组件（**Software Component**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**SWC**
> 软件组件（**SoftWare Component**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**SWCD**
> 软件组件描述（**Software Component Description**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**SwClu**
> 软件集群——将在一台机器上部署软件相关的所有 AUTOSAR 产物分组在一起的独立构建单元（**Software Cluster**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**SwCluC**
> 软件集群连接（**Software Cluster Connection**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**SWCo**
> 软件组合（**Software Composition**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**SWS**
> Software Specification —— 软件规范。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**Symbolic name**
> ECU信号的符号名称（**Symbolic name**）在**I/O**硬件抽象模块中是用来建立链接的。（包括：功能、引脚等）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**SYNC Ingress Processing Delay**
> 在 Timesync 模块一侧，从 **SYNC** 报文进入到通过 StbM_BusSetGlobalTime 将接收时间元组转发给 **StbM** 之间的时间区间。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**SYNC message**
> 时间同步报文（**Time Synchronization message**）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**Synchronized Time Base**
> 通过 Timesync 报文与其他节点上的时基同步的时基，由时基标识符 0..127 标识。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Synchronized（同步）**
> 只要 ((!vPOC!Freeze) && (vPOC!State == NORMAL_ACTIVE) || (vPOC!State == NORMAL_PASSIVE)) 成立，就认为 FlexRay CC 与其所连接的 FlexRay 集群同步。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**SyncLocal Time Tuple**
> 时间元组 [TL_Sync, TV_Sync]，在 TV_Sync 时刻导出，或按公式 7.1 计算，或在支持时从受控硬件时钟导出。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

## T

**Target time**
> 目标时间：到达该值时应有某事发生。其行为取决于配置和已启用的功能。
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**TCP**
> Transmission Control Protocol —— 传输控制协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**TCP socket connection**
> 使用 TCP 作为传输协议的套接字连接（选择容器 **SoAdSocketProtocol** 包含 **SoAdSocketTcp** 子容器）。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**TCP/IP**
> 计算机网络中使用的一族通信协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**TCS**
> 牵引力控制系统（**Traction Control System**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**test interval**
> **CoreTest** 测试间隔：在配置为构成一个完整内核测试的硬件资源上（后台模式下执行的）所有部分测试的总和。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Test Interval Id**
> 测试间隔的标识符，每开始一个新的测试间隔时应递增。
>
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Tick**
> 定义定时器分辨率，即定时器一次递增的持续时间。
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**Time Base Customer**
> 同步时基管理器支持的 3 种时基客户：主动型客户、触发型客户、通知型客户。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Time Gateway**
> 被一个时基从节点和一个或多个时基主节点引用的时基；Timesync 报文不直接穿过时间网关路由，因为路由延迟需要被补偿。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Time Offset**
> 施加速率校正之后仍然残留的时间偏移。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Time Service Predef Timer**
> 时间服务预定义定时器：一种自由运行的计数器，具有预定义的物理时间单位和范围；硬件定时器的功能基于相应的 **GPT** 预定义定时器。时间服务模块为每个预定义定时器提供一组 **API** 服务，用户可以实例化任何计时器（仅受可用内存限制）并完全独立地使用这些实例。
>
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**Time Slave**
> 基于由相应 Timesync 模块提供的全局时基值来更新其内部维护的本地时基的角色。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Time Triple**
> 在时间元组的基础上加入对应的备用虚拟本地时间作为第三个成员而得到。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Time Tuple**
> Timesync 栈始终通过时间元组结构管理时基的时间，即在同一时间点采样的全局时间采样与虚拟本地时间采样。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Timer channel**
> 表示分配给一个定时器硬件的逻辑定时器实体。
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**Timer instance**
> 定时器实例：由 **API** 数据类型 Tm_PredefTimer...bitType 所对应的一个数据对象，即用户软件级别上的时间服务预定义定时器的实例化。
>
> 来源：[AUTOSAR Time Service（时间服务）](system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**TO**
> 发送机会（**Transmit Opportunity**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**TP**
> 传输协议（**Transport Protocol**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**TP-PDU**
> 通过 SoAd 的 TP-API 发送/接收的 PDU。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**Trace Message**
> 包含已经过 **VFB** 的信息的消息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Trace status**
> 提供是否应发送跟踪消息的信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Triggered Time Base Customer**
> 由同步时基管理器触发的时基客户；该功能目前仅限于 **OS** ScheduleTable 的同步。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Triggered to NvM**
> 如果需要在 Dem_Init 和 Dem_Shutdown 之间触发数据的存储，**Dem** 模块应使用 **NVRAM** 管理器的 **API** NvM_WriteBlock。此外，如果请求已被接受，**Dem** 模块应等待 NvM_WriteBlock 的肯定响应。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**TS**
> Time Stamp —— 时间戳。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

## U

**uC**
> 微控制器（**Microcontroller**）
>
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver）
{: .glossary-source}

**UDP**
> User Datagram Protocol —— 用户数据报协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**UDP socket connection**
> 使用 UDP 作为传输协议的套接字连接（选择容器 **SoAdSocketProtocol** 包含 **SoAdSocketUdp** 子容器）。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**UDP/IP**
> User Datagram Protocol / Internet Protocol —— 用户数据报协议/互联网协议。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**UDS**
> 统一诊断服务（**Unified Diagnostic Services**）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**UDS status byte**
> 按 ISO 14229-1 定义、基于 **DTC** 级别的状态字节。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**UEH**
> Use Extended Header —— 使用扩展头。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**UI**
> 用户界面（**User Interface**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**&lt;Up&gt;**
> 上层通信接口模块。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**Updated Rx Time Tuple**
> 时间元组 [TG_URx, TV_URx]，通过在接收时间元组上加入经速率校正的 **SYNC** 进入处理延迟而导出。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Upper Layer Modules（Up）**
> 位于 L-SDU Router 之上的模块。该层通常包括 **IEEE1722Tp**。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**URL**
> Uniform Resource Locator —— 统一资源定位符。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

## V

**Variation Point**
> 变体点。设计中在 2 个或更多变体之间给出选择的位置；必须做出选择的时间称为最晚绑定时间。
>
> 来源：[VFB（虚拟功能总线）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**VB**
> Visual Basic
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**VCD**
> 车辆碰撞检测（**Vehicle Crash Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**VCP**
> 车辆碰撞预测（**Vehicle Crash Prediction**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**VERB**
> Verbose —— 详细模式。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**VERS**
> Version Number —— 版本号。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**VFB**
> 虚拟功能总线（**Virtual Functional Bus**）。AUTOSAR 中允许组件相互交互的通信机制；应用被建模为相互连接的组件的组合，组件经由端口与端口接口交互。
>
> 来源：[VFB（虚拟功能总线）](general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**VFC**
> 虚拟功能集群（**Virtual Function Cluster**）。把实现一个或多个车辆功能所需的 SW 组件之间端口层面的通信分组；逻辑视图，允许可复用的、独立于总线/ECU 的设计。在部分组网（Partial Networking）中，VFC 映射到一个或多个部分网络集群（PNC）。
>
> 来源：[Layered Software Architecture（分层软件架构）](general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）
{: .glossary-source}

**VGR**
> 可变传动比（**Variable Gear Ratio**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**VH**
> 变型处理概念（**Variant Handling concept**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**VIN**
> Vehicle Identification Number —— 车辆识别码。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**Virtual Local Time**
> **StbM** 从硬件时钟导出的本地时间参考，用于全局时间本地实例的推移。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**VLC**
> 车辆纵向控制（**Vehicle Longitudinal Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**VM**
> 车辆模型（**Vehicle Model**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**VMC**
> 车辆运动控制（**Vehicle Motion Control**）。
>
> 来源：[Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC）
{: .glossary-source}

**VOBD**
> 车辆车载诊断（**Vehicle On-Board-Diagnostic**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**vPOC**
> **CC** 在 **CHI** 处提供给主机的数据结构，包含 **CC** 的实际 **POC** 状态（详情参见 ISO 17458-1）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

## W

**WCET**
> 最坏情况执行时间（**Worst case execution time**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**WDG**
> 看门狗（**Watchdog**，模块特定前缀）
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**WdgM**
> 看门狗管理器（**Watchdog Manager**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**WEID**
> With ECU ID —— 带 ECU ID。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**WEth**
> Wireless Ethernet Driver（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）
{: .glossary-source}

**WEthTrcv**
> Wireless Ethernet Transceiver（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）
{: .glossary-source}

**WIR**
> 警告指示器请求（**Warning Indicator Request**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**WP**
> 工作包（**Work package**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**Write Page**
> 写入页面（**Write Page**）是指存储设备的最小可写单元（以字节为单位）。某些存储设备技术的访问必须考虑物理分段，因此并非所有存储设备技术都支持按字节访问。该术语定义了单次访问所需写入的最小大小。
>
> 来源：[AUTOSAR Memory Access（存储访问）](memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**WSID**
> With Session ID —— 带会话 ID。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**WTMS**
> With Timestamp —— 带时间戳。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**WUC**
> **OBD** 术语：暖机循环（**Warm up cycle**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**WWH-OBD**
> 全球统一车载诊断（**World Wide Harmonized On-Board-Diagnostic**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

## X

**X.509**
> 定义公钥证书格式的 **ITU-T** 标准。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**XCP**
> Universal Calibration Protocol —— 通用校准协议。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**XLFF**
> XL 帧格式（**XL Frame Format**）。
>
> 来源：[AUTOSAR CAN XL Driver（CAN XL 驱动程序）](communication/canxl_driver/index.md)（SWS_CANXLDriver）
{: .glossary-source}

**XML**
> 可扩展标记语言（**eXtensible Markup Language**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**XSD**
> XML 模式定义（**XML Schema Definition**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

## Y

**YRC**
> 横摆角速度控制（**Yaw Rate Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}
