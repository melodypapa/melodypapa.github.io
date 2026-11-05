---
title: "AUTOSAR 术语表（缩略语与缩写）"
---

本页汇总各 AUTOSAR 模块文章以及 AUTOSAR TR 术语表（Foundation）的术语，按字母排序。所有词条均出自 AUTOSAR **R23-11** 版规范文档；「来源」行注明该词条所引用的规范文档及其 spec 编号。

## A

**A2L**
> ASAM 2MC 语言文件的文件扩展名（**File Extension for an ASAM 2MC Language File**）。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**AAF**
> **AVTP** 音频格式（**AVTP Audio Format**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**AB**
> 安全气囊（**Airbag**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ABS**
> 防抱死制动系统（**Antilock Braking System**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**absolute timer（绝对定时器）**
> 绝对定时器被设置为 FlexRay 集群的一个绝对全局时间并由其触发。FlexRay 全局时间由一个循环和一个宏节拍偏移量组成。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**Abstract Platform**
> 抽象平台（**Abstract Platform**，**XP**）。平台无关的功能设计层，独立于 AUTOSAR 自适应平台（AP）与经典平台（CP）；描述组件、端口、接口与连接器，不涉及部署与实现细节。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**Abstract Platform System Description**
> 抽象平台系统描述（**Abstract Platform System Description**，**ASD**）。承载抽象平台设计工件的系统描述，其 `System.category` 为 `ABSTRACT_PLATFORM_SYSTEM_DESCRIPTION`。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**Abstract Software Component**
> 抽象软件组件（**Abstract Software Component**，**XSC**）。抽象平台中不绑定具体用例的软件组件，通常以 `CompositionSwComponentType` 建模。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**AC**
> J1939 **AddressClaimed PG**（**PGN** = 0x0EE00）；当 **SA** = 0xFE 时为 **CannotClaimAddress**。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）
{: .glossary-source}

**ACC**
> 自适应巡航控制（**Adaptive Cruise Control**）。
>
> 来源：[Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](cp/application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC）
{: .glossary-source}

**Acceptance Test Suite**
> 在验收测试（**Acceptance Testing**）语境中使用的一种测试用例描述。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Access Control Decision**
> 访问控制判定是一个布尔值，指示所请求的操作是否被允许。它基于调用者的身份以及"访问控制策略"（**Access Control Policy**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Access Control Policy**
> 访问控制策略绑定到调用的目标（即服务接口），用于表达访问这些接口需要何种"身份信息"（**Identity Information**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Accuracy**
> 精度（**Accuracy**）取决于用于采样或者生成的硬件外围设备。如：**ADC**转换器可以是 8/10/12/16 位转换器
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**ACF**
> **AVTP** 控制格式（**AVTP Control Format**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**ACF_CAN**
> 控制器局域网（**CAN**）/**CAN** 弹性数据率（**CAN FD**）消息（**Controller Area Network (CAN)/CAN with Flexible Data-Rate (CAN FD) message**），由 IEEE 1722 定义。
>
> 来源：[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**ACF_CAN_BRIEF**
> 缩略 **CAN**/**CAN FD** 消息（**Abbreviated CAN/CAN FD message**），由 IEEE 1722 定义。
>
> 来源：[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**ACF_LIN**
> **LIN** 消息（**LIN message**），由 IEEE 1722 定义。
>
> 来源：[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**ACK**
> 控制字节置 0 的 **J1939** **Acknowledgement PG**（**ACKM**）。
>
> 来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**ACKM**
> J1939 确认 PG（**J1939 Acknowledgement PG**，PGN = 0x0E800）
>
> 来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**Acquisition Time**
> 采集时间 = 采样时间（**Sample Time**）+ 转换时间（**Conversion Time**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**Activation Mode 1**
> 无故障——**MIL** 应闪烁一次。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Activation Mode 2**
> "按需 MI"（on-demand-MI）——如果 **OBD** 系统按照区分显示策略会命令按需 MI，**MIL** 应闪烁两次。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Activation Mode 3**
> "短时 MI"（short-MI）——如果 **OBD** 系统按照区分显示策略会命令短时 MI，**MIL** 应闪烁三次。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Activation Mode 4**
> "持续 MI"（continuous-MI）——如果 **OBD** 系统按照区分显示策略会命令持续 MI，**MIL** 应保持持续点亮。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Active Time Base Customer**
> 一种时基客户，它自主调用同步时基管理器，或用于从同步时基管理器读取某时基的时间信息，或用于根据应用信息更新同步时基管理器维护的时基。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Active wake-up**
> 由本 ECU 引起的唤醒，例如由传感器引起（**Wake-up caused by the hosting ECU e.g. by a sensor**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Activity state**
> 活动状态：软件组件正在执行时的状态。活动状态以许可状态为前提条件，并叠加物理使能条件。它不由 **FiM** 计算，也不作为状态变量提供，只能通过观察或测量确定。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**Adaptability**
> 适应性是系统调整自身以应对其环境变化、从而继续提供预期功能的能力。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Adaptive Application**
> 遵循自适应 AUTOSAR 规范、因而可部署到自适应平台实例上的软件。它由其实现、运行数据（如地图数据）以及由应用设计模型给出的元数据组成。自适应应用至少包含一个可执行文件。为了能部署到不同的自适应平台上，它只使用 ARA 编程接口。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Adaptive Platform Foundation**
> 自适应平台实现的一部分，通过软件接口（API）向应用提供标准化的平台功能。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Adaptive Platform Services**
> 由属于 AUTOSAR 平台实现一部分的应用所提供的标准平台服务。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ADC**
> 模数转换器（**Analogue Digital Converter**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC Channel**
> **ADC**通道是指绑定到一个端口引脚的逻辑**ADC**实体。同时多个**ADC**实体也可以映射到同一个端口引脚。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC Channel Group**
> **ADC**通道组是指由一组**ADC**通道链接到同一个**ADC**硬件单元（**ADC HW Unit**）。例如：一个采样保持器（**Sample & Hold**）和一个**A/D**转换器。整个组的转换由一个触发源触发。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC HW Unit**
> 微控制器的输入电子设备，包括执行模拟到数字转换所需的所有部件。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC Module**
> ADC的基础软件模块ADC驱动模块（**ADC Driver**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**ADC Result Buffer**（**ADC Streaming Buffer**，**ADC Stream Buffer**）
> **ADC**驱动程序的用户必须为每个组提供一个缓冲区。如果选择流式访问模式（**streaming access mode**），此缓冲区可以保存同一组通道的多个样本。如果选择单一访问模式（**Single Access Mode**），每个组通道的一个样本将保存在缓冲区中。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**Address Area**
> 地址区（**Address Area**）是指逻辑地址空间中连续的存储区域。通常，多个物理存储扇区组合成一个逻辑地址区。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**AddressAndLengthFormat Identifier**
> 地址和长度格式标识符：定义请求消息中 memoryAddress 和 memorySize 参数使用的字节数。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**AddressAndLengthFormatIdentifier**
> 定义请求消息中 memoryAddress 与 memorySize 参数所占用的字节数（**Defines the number of bytes used for the memoryAddress and memorySize parameter in the request messages**）
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Administrative Block**
> 「管理块」是「基本存储对象」。它驻留在 **RAM** 中。「管理块」是「NVRAM 块」的强制部分。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**AEAD**
> 具有关联数据的经过身份验证的加密（**Authenticated Encryption with Associated Data**）。
>
> 来源：[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**AEB**
> 自主紧急制动（**Autonomous Emergency Braking**）。
>
> 来源：[Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](cp/application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC）
{: .glossary-source}

**AF**
> 确认帧（Acknowledge Frame，请参阅 ISO 10681-2）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**Aging**
> 在经过确定的运行周期数之后，从事件内存中遗忘/删除不再失败的事件/**DTC**。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Aging Counter**
> 用于执行老化的计数器（也称 **Aging Cycle Counter** 或 **DTC Aging Counter**）。它对事件/**DTC** 从事件内存中移除之前所经历的运行周期数进行计数。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**AH**
> 认证报头（**Authentication Header**），**IPsec** 的认证协议。
>
> 来源：[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**AI**
> 存活指示（**Alive Indication**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**AI Table**
> 应用接口表（**Application Interface Table**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**AID**
> 应用标识符（**Application identifier**）。
>
> 来源：[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**AIFS**
> 仲裁帧间间隔（**Arbitration Inter Frame Space**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](cp/communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）
{: .glossary-source}

**Alive Counter**
> **WdgM** 中在**检查点**上下文内的独立数据资源，用于跟踪和处理该**检查点**的**存活指示**数量。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**Alive Indication**
> 由**被监督实体**的**检查点**提供的指示，用于向**WdgM** 标识其存活状态。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**Alive Supervision**
> 一种监督，用于检查**被监督实体**的执行是否足够频繁且不过于频繁（包括容差）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**ALU**
> 算术逻辑单元（**Arithmetic Logic Unit**）
>
> 来源：[Specification of CRC Routines（CRC 例程规范）](cp/libraries/crc/index.md)（SWS_CRCLibrary）
{: .glossary-source}

**AN**
> 关联编号（**Association Number**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）
{: .glossary-source}

**Antisubmarine**
> 下潜——约束系统中与汽车应用相关的术语（**Antisubmarine**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**AP**
> 执行器池（**Actuator Pool**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**API**
> 应用编程接口（**Application Programming Interface**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Standard Types（标准类型）](cp/general/standard_types/index.md)（SWS_StandardTypes）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**APID**
> Application ID —— 应用 ID。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Application**
> 为解决需要信息处理的最终用户问题而规定的软件（或程序）。一个软件实体的"软件配置"（**Software Configuration**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Application Data Type**
> 应用数据类型（**Application Data Type**）。从应用视角定义的数据类型，描述物理含义（如测量单位）而不涉及位宽、字节序等实现细节；抽象平台只允许应用数据层的数据类型。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**Application ID**
> 一个应用/**SW-C** 的缩写，标识一条日志和跟踪消息所来自的应用/**SW-C**；由四个 8 位 ASCII 字符组成。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Application Interface**
> 应用接口（**Application Interface**）。抽象平台中的端口接口类型，元素包括命令（`command`）、指示（`indication`）与属性（`attribute`），与中间件部署无关。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**Application Layer**
> 应用层位于 **RTE** 之上；**AUTOSAR** 软件组件位于应用层中。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**application mode manager**
> 提供模式切换服务的 **AUTOSAR** 软件组件（**application mode manager**）。应用模式管理者的模式不必是标准化的。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Application Programming Interface**
> 应用编程接口（API）是特定软件部分的既定方法，编写程序的程序员通过它可以向该软件部分发出请求。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Application Software Cluster**
> 主要包含软件组件、仅包含选定的 BSW 模块（例如服务模块、转换器等）的软件集群（**Application Software Cluster**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）、[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}

**Application Software Component**
> 应用软件组件是一种特定的"软件组件"，它在应用层实现已定义的功能并运行于 AUTOSAR 基础设施之上。它只通过 AUTOSAR 运行时环境进行通信。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Applied Rate**
> 用于设置/计算全局时间的本地实例所施加的速率。对于时基主节点，它与速率校正 r_rc 相同；对于时基从节点，对于同步时基为 r_rc 与 r_oc 之和，对于偏移时基分别为 (r_orc − 1) 与 r_oc。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Architecture**
> 体系结构是系统的基本组织方式，体现在其组件、组件之间及其与环境的静态与动态关系、以及指导其设计与演化的原则之中。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ARP**
> Address Resolution Protocol —— 地址解析协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**ARTI**
> AUTOSAR 运行时接口——用于调试与跟踪嵌入式系统运行时行为的一组标准（**AUTOSAR Run-Time Interface**）
>
> 来源：[ARTI（AUTOSAR 运行时接口）](cp/sw_arch/arti/index.md)（AUTOSAR_CP_EXP_ARTI）、[Requirements on Debug Trace Profile（调试跟踪配置文件需求）](foundation/communication_management/rs_debug_trace_profile/index.md)（AUTOSAR_FO_RS_DebugTraceProfile）
{: .glossary-source}

**Artifact**
> 制品是一种工作产品定义（**Work Product Definition**），为有形的工作产品类型提供描述与定义。制品可以由其他制品组成。在高层次上，制品表示为单个概念性文件。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**arxml**
> .arxml——AUTOSAR 可扩展标记语言文件（**AUTOSAR Extensible Markup Language File**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**ASAM**
> 自动化与测量系统标准化协会（**Association for Standardization of Automation and Measuring Systems**）。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**ASCR runnable**
> 由至少一个 `AsynchronousServerCallReturnsEvent` 触发的可运行实体（**ASCR runnable**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**ASIL**
> 汽车安全完整性等级（**Automotive Safety Integrity Level**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](cp/safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**ASIL Decomposition**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.7
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ASN.1**
> 抽象语法标记一号（**Abstract Syntax Notation One**）：一种描述数据结构的标准记法，常与 DER 编码规则一起用于证书等密码学数据的编码。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**Assembly Connector**
> 组装连接器。在 VFB 层级把一个组件的 RPort/PRPort 与另一个组件的 PPort/PRPort 连接起来的连接器；恰好连接一个提供端口与一个要求端口。
>
> 来源：[VFB（虚拟功能总线）](cp/general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**Asserted Property**
> 如果设计实体（例如软件组件或系统）保证该属性或质量得到满足，则称设计实体的该属性或质量是"已断言的"（**asserted**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Assessment**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.4
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Asset**
> 为在多种上下文中使用而设计的条目。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**associated Local Software Cluster Communication Plug-In**
> 被分配给某个通信图、独占区、模式机实例或分布式共享模式队列，因而处理所有经由 **RTE API**、**SchM API** 或 **RTE** 内部代码的访问的本地软件集群通信插件（**Local Software Cluster Communication Plug-In**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**associated Cross Software Cluster Communication Plug-In**
> 被分配给某个通信图或模式机实例，因而处理所有经由 **RTE API** 或 **RTE** 内部代码的访问的跨软件集群通信插件（**Cross Software Cluster Communication Plug-In**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**associated RTE Implementation Plug-In**
> 被分配给某个通信图、独占区、模式机实例或分布式共享模式队列，因而处理所有经由 **RTE API**、**SchM API** 或 **RTE** 内部代码的访问的本地软件集群通信插件或跨软件集群通信插件（**associated RTE Implementation Plug-In**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Asynchronous Communication**
> 异步通信不会阻塞发送方软件实体。发送方软件实体无需等待通信伙伴的响应即可继续其自身的操作。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Asynchronous Function**
> 如果某个"函数"（**Function**）所描述的功能在其返回调用者时不能保证已完成，则该函数称为异步函数。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Atomic Sender/Receiver interface**
> 原子发送者/接收者接口可将 **DID** 数据元素分组为一个记录数据元素原型，所有数据元素都可以通过单个读取或写入操作访问。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Atomic sequence/ atomic piece**
> 原子序列是一段不得被中断的测试。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Atomic Software Component**
> 非组合的软件组件。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Attributes**
> 属性（**Attributes**）是**ECU**中存在的每个**ECU**信号所包含的软件或者硬件特性。一些属性是固定的，由端口定义决定。还有一些属性是可以在**I/O**硬件抽象中进行配置的。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**ATWS**
> 防盗警告系统（**Anti-Theft Warning System**）。可借助光学与声学信号警示未授权进入尝试、并可防止发动机被起动的防盗系统。
>
> 来源：[Explanation of Application Interfaces of the Body and Comfort Domain（车身与舒适域应用接口说明）](cp/application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort）
{: .glossary-source}

**Audit**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.5
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Authentic I-PDU**（可信 I-PDU）
> 可信 I-PDU 是一个任意的 AUTOSAR I-PDU，其内容在通过网络传输期间借助受保护的 I-PDU（**Secured I-PDU**）得到保护。受保护的内容包括完整的 I-PDU 或 I-PDU 的一部分。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Authentication Information**（认证信息）
> 认证信息由新鲜度值（**Freshness Value**，或其一部分）和验证器（**Authenticator**，或其一部分）组成。认证信息是 **SecOC** 为实现受保护的 I-PDU 而添加的附加信息。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Authentication**（认证）
> 认证是与识别相关的一项服务。该功能既适用于实体本身，也适用于信息。进入通信的两个参与方应相互识别。通过信道传递的信息应就其来源、来源日期、数据内容、发送时间等进行认证。因此，密码学的这一方面通常细分为两大类：实体认证（**entity authentication**）和数据来源认证（**data origin authentication**）。数据来源认证隐含地提供了数据完整性（因为如果消息被修改，则来源已改变）。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Authenticator**
> 认证器（**Authenticator**）——用于提供消息认证的数据；对称方法使用消息认证码（**MAC**），非对称方法使用签名。
>
> 来源：[Secure Onboard Communication Protocol Specification（安全车载通信协议规范）](foundation/protocols/prs_secoc_protocol/index.md)（AUTOSAR_FO_PRS_SecOcProtocol）
{: .glossary-source}

**Authenticator**（验证器）
> 验证器是用于提供消息认证的数据。通常，术语消息验证码（**Message Authentication Code**，**MAC**）用于对称方法，而术语签名或数字签名（**Signature** 或 **Digital Signature**）指的是具有不同属性和约束的非对称方法。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Authenticity**
> 数据确实来源于其所声称来源的特性。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Automotive Safety Integrity Levels**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.7
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR**
> 汽车开放系统架构（**AUTomotive Open System ARchitecture**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**AUTOSAR Adaptive Platform**
> 由 AUTOSAR 标准化的自适应计算平台。狭义上指其规范；广义上可指自适应平台实现的一个实例。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Application Interface**
> 由 AUTOSAR 标准化、可用于创建"应用"（**Application**）的"AUTOSAR 接口"（**AUTOSAR Interface**）的一组"蓝图"（**Blueprint**）。从标准化蓝图（**Standardized AUTOSAR Blueprint**）派生的 AUTOSAR 接口即标准化的 AUTOSAR 接口（**Standardized AUTOSAR Interface**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Authoring Tool**
> 用于创建和修改"AUTOSAR XML 描述"（**AUTOSAR XML description**）的 AUTOSAR 工具（**AUTOSAR Tool**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Blueprint**
> AUTOSAR 蓝图是 AUTOSAR 元素的"蓝图"（**Blueprint**）。它还包括：在 AUTOSAR 项目中规定，对于某一特定类别的 AUTOSAR 元素类型的蓝图，哪些属性是必须规定的，以及如何从该蓝图派生出 AUTOSAR 对象。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR COM**
> AUTOSAR COM模块源自[3]。详情见第6.2.1节。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**AUTOSAR Connector**
> **SoAd** 在不同的 PDU 源/提供者与 TCP/IP 协议栈之间、以及 TCP/IP 协议栈与不同的 PDU 汇/消费者之间充当（解）复用器（**(De)Multiplexer**）。术语 AUTOSAR 连接器（**AUTOSAR connector**）指一个 PDU 的源/提供者或汇/消费者。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](cp/communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**AUTOSAR Converter Tool**
> 通过转换其他 AUTOSAR XML 文件中的信息来创建 AUTOSAR XML 文件的 AUTOSAR 工具。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Definition**
> 这是对可以有取值的参数的定义。可以说，参数值是这些定义的实例。但在 AUTOSAR 的元模型层次结构中，定义本身也是元模型的实例，因此被视为一种描述。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Autosar EthTSyn**
>  EthTSyn，**Ethernet** 的时间同步提供者模块。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](cp/globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**AUTOSAR Interface**
> 软件组件的 AUTOSAR 接口（**AUTOSAR Interface**）指该组件中用于与其他组件交互的所有"端口"（**Port**）的集合。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Meta-model**
> AUTOSAR 元模型是一个 UML2.0 模型，它定义了描述 AUTOSAR 系统及相关制品的语言。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Model**
> 这是 AUTOSAR 元模型的一个实例。AUTOSAR 模型表示按照 AUTOSAR 方法论适合预期用途的各个方面。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Partial Model**
> 在 AUTOSAR 中，模型可能的划分方式在元模型中用 &lt;&lt;atp Splitable&gt;&gt; 标记。一个部分模型在一个"AUTOSAR XML 描述"（**AUTOSAR XML description**）中由一个文件表示。部分模型不需要满足适用于 AUTOSAR 模型的全部语义约束。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Processor Tool**
> 通过处理 AUTOSAR XML 文件中的信息来创建非 AUTOSAR 文件的 AUTOSAR 工具。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Run-Time Interface**
> AUTOSAR 运行时接口（AUTOSAR Run-Time Interface）应定义构建工具与调试/跟踪工具之间的接口。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Runtime for Adaptive Applications**
> 由功能簇（**Functional Cluster**）提供的一组标准应用接口，这些功能簇属于自适应平台基础（**Adaptive Platform Foundation**）或自适应平台服务（**Adaptive Platform Services**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Service**
> "服务"（**service**）一词在分层软件架构中用于表示与应用交互的 AUTOSAR 软件架构的最高层。服务一词按面向服务架构（**service-oriented architecture**）中定义的含义使用。该含义与 AUTOSAR 自适应平台上服务一词的用法关联最强。服务一词也用于描述诊断服务的处理，例如 UDS 服务 ReadDataByIdentifier，用于诊断测试仪与（AUTOSAR）ECU 上的诊断协议栈之间的通信。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Software**
> 按照 AUTOSAR 标准开发的应用软件或基础/平台软件。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR Tool**
> 这是一种软件工具，它支持方法论中定义的 AUTOSAR 任务中的一个或多个任务。根据所支持的任务，AUTOSAR 工具可以用作"AUTOSAR 编写工具"（**AUTOSAR Authoring Tool**）、"AUTOSAR 转换工具"（**AUTOSAR Converter Tool**）、"AUTOSAR 处理工具"（**AUTOSAR Processor Tool**），或它们的组合。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR XML description**
> 在 AUTOSAR 中，这是序列化的 AUTOSAR 模型。实际上，AUTOSAR XML 描述是"AUTOSAR 模型"（**AUTOSAR Model**）的 XML 表示。AUTOSAR XML 描述可以由多个文件组成。每个单独的文件表示一个"AUTOSAR 部分模型"（**AUTOSAR Partial Model**），并且必须能够针对"AUTOSAR XML 模式"（**AUTOSAR XML Schema**）成功通过校验。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AUTOSAR XML Schema**
> AUTOSAR XML 模式是用于交换 AUTOSAR 模型（**AUTOSAR Model**）及描述的 XML 语言定义。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AutosarDataPrototype implementation**
> **RTE** 分配的、实现 `AutosarDataPrototype`（或其所属状态处理）的非自动内存对象的定义与声明（**AutosarDataPrototype implementation**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Availability**
> 1. 可用性是系统按照其规范完整地执行某个功能 A 的能力。2. 在给定时间间隔内系统执行功能 A（按第 1 条定义）的总时间与该时间间隔长度之比。另一种表述：系统在指定时刻 t 正在执行功能 A 的概率。3. 在降级模式下，如果完整的 A 不可用，系统具有执行 A 的子集 B 的能力。此时，功能 B 是可用的。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**AVB**
> 音视频桥接（**Audio Video Bridging**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](cp/globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**AVTP**
> 音视频传输协议（**Audio/Video Transport Protocol**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**AVTPDU**
> 音视频传输协议数据单元（**Audio/Video Transport Protocol Data Unit**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

## B

**&lt;Bus&gt;TSyn**
> 特定总线的时间同步模块（**Bus specific Time Synchronization** module）。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Background test**
> 后台测试由 **SW** 调度器/**RTOS** 周期性调用。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**BAM**
> 广播公告消息（**Broadcast Announce Message**），SAE J1939 传输层的广播变体
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**Bank**
> 存储 **Bank** 是一组扇区批次（**Sector Batch**）的集合。如果存储技术支持按扇区分段，则存储 **Bank** 是不允许边读边写操作的扇区批次组实例。对于闪存设备，**Bank** 通常映射到单独的闪存控制器。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**BAS**
> 制动辅助（**Brake Assist**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Base Socket**
> 在低层代理和高层代理之间链接通用基础设施（例如 BSW API 集合）的通用链接（**base socket**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**Basic Software**
> 基础软件（**Basic Software**, BSW）提供"电子控制单元"（**Electronic Control Unit**）的基础设施功能（依赖于原理图的和独立于原理图的）。它由"集成代码"（**Integration Code**）和"标准软件"（**Standard Software**）组成。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Basic Software Module**
> 在"电子控制单元"（**Electronic Control Unit**）上定义某个特定基础软件功能的软件文件（代码与描述）的集合。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Basic Storage Object**
> 「基本存储对象」是 **NVRAM** 块的最小实体。多个基本存储对象可用于构建 **NVRAM** 块。「基本存储对象」可以驻留在不同的内存位置，包括：**RAM**、**ROM**、NV 内存（**NV memory**）中。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**BER**
> 误码率（**Bit Error Rate**）——字节流中被损坏比特的比率，例如 1e-5。
>
> 来源：[Requirements on E2E（端到端通信保护需求）](foundation/communication_management/rs_e2e/index.md)（AUTOSAR_FO_RS_E2E）
{: .glossary-source}

**Binary Manifest**
> 软件集群的二进制对象的定义良好的接口，提供资源的元信息与访问此类资源的句柄（**Binary Manifest**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](cp/system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）、[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**Binary Object**
> 一组文件的集合，包含在编程到目标 ECU 之前不会再被修改的二进制可执行代码与数据（**Binary Object**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](cp/system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）、[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**BIST**
> 内建自测试（**Built in Self Test**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）、[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](cp/safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）、[Hardware Test Management startup shutdown（硬件测试管理启动和关闭）](cp/system_services/hw_test_manager/index.md)（AUTOSAR_CP_SWS_HWTestManager）
{: .glossary-source}

**Bit Position**
> 在 AUTOSAR 中，I-PDU 内的位位置 N 表示字节 J 中的位 I，其中 I = N mod 8，J = N / 8。字节 J 和位位置 I 按照 ISO 17356-4（OSEK/VDX 通信）中的定义进行解释。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Block Management Type**
> NVRAM 块的类型。它取决于 NVRAM 块在不同强制/可选基本存储对象块中的（可配置）单独组合以及此 NVRAM 块的后续处理。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**Blueprint**
> 这是一种模型，其他模型可以通过复制和细化从中派生。注意，与元模型及类型相对照，这一过程不是实例化。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Bmc**
> 基础软件多核库（**Basic Software Multicore Library**）
>
> 来源：[Specification of Basic Software Multicore Library（基础软件多核库规范）](cp/libraries/bmc/index.md)（AUTOSAR_CP_SWS_BSWMulticoreLibrary）
{: .glossary-source}

**BMCA**
> 最佳主时钟算法（**Best Master Clock Algorithm**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](cp/globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**BndM**
> 大容量非易失性数据管理器（**Bulk Non-Volatile Data Manager**）
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**BRWS**
> 基本后轮转向（**Basic Rear Wheel Steering**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**BS**
> 块大小（**Block Size**）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**BSAS**
> 基本转向角叠加（**Basic Steering Angle Superposition**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**BSM**
> 基本安全消息（**Basic Safety Message**）。
>
> 来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**BSTS**
> 基本转向力矩叠加（**Basic Steering Torque Superposition**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**BSW**
> 基础软件（**Basic Software**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](cp/memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping）、[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）、[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**BSW driver**
> 有关 BSW 驱动（**BSW driver**）的列表，请参阅基础软件模块列表中 "AUTOSAR SW layer" 列。
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**BswM**
> 基础软件模式管理器（**Basic Software Mode Manager**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**BSWMD**
> 基础软件模块描述（**Basic Software Module Description**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**BswSchedulableEntity activation**
> `BswSchedulableEntity` 的激活被定义为包含该 `BswSchedulableEntity` 的任务/ISR2 的激活，并最终包括置位一个标志，告知任务/ISR2 中的胶水代码应执行哪个 `BswSchedulableEntity`（**BswSchedulableEntity activation**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**BswSchedulableEntity start**
> `BswSchedulableEntity` 的启动指在已启动的任务/ISR2 内调用实现该 `BswSchedulableEntity` 的 **C** 函数（**BswSchedulableEntity start**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**BTP**
> 基本传输协议（**Basic Transport Protocol**）。
>
> 来源：[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**BTP-A**
> 表示交互式包传输的 **BTP** 报头类型。
>
> 来源：[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）
{: .glossary-source}

**BTP-B**
> 表示非交互式包传输的 **BTP** 报头类型。
>
> 来源：[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）
{: .glossary-source}

**buffer（缓冲区）**
> 在 Fr SWS 的上下文中，缓冲区描述一个硬件发送/接收资源，它是 FlexRay 控制器的一部分，被映射到一个 FlexRay 槽、信道、循环用于发送或接收。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**Bugzilla**
> 变更请求管理工具（**Bugzilla**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**Bulk Data**
> "批量数据"（**Bulk Data**）是指规模大到处理较小数据集的标准机制不再适用的一类数据。这意味着软件系统中的批量数据需要用不同于较小数据集的机制来建模、存储、访问和传输。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Bus**
> NM节点/ECU所连接到的物理通信介质。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**Bus idle timeout**
> 总线没有活动所持续流逝的时长。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**Bus Mirroring**
> 将信息从车内内部总线转发到外部总线，例如诊断连接器。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Bus Off**
> CAN 总线的错误状态：CAN 控制器因错误计数达到上限而与总线脱离。CAN 状态管理器（CanSM）通过 Bus Off 恢复状态机进行恢复。
>
> 来源：[Error Description（错误描述）](cp/general/error_description/index.md)（AUTOSAR_CP_EXP_ErrorDescription）
{: .glossary-source}

**Bus sleep**
> 通信总线上无需任何活动，例如 CAN 总线睡眠（**No activity required on the communication bus**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Bus Wake-Up**
> 总线唤醒由专用通信标准（如 CAN、LIN、FR）规范中定义的总线上的特定唤醒脉冲引发。总线唤醒会促使收发器和控制器离开节能模式并进入正常模式，重新开始总线通信。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Bus-Off state**
> 指没有电缆连接到以太网硬件的情况。
>
> 来源：[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

**Bus-Sleep Mode**
> 所有互连的通信控制器均处于睡眠模式的网络模式。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**Bypassing**
> 在 ECU 镜像内以实验方式并入新功能。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

## C

**'C' typed PerInstanceMemory**
> 以 `PerInstanceMemory` 类定义的 **C** 类型按实例内存（**'C' typed PerInstanceMemory**）；内存的类型由 `typeDefinition` 属性中的 **C** typedef 定义。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}

**C-V2X**
> 基于蜂窝的车联网（**Cellular based Vehicle to Everything**）。
>
> 来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**C/S**
> 客户端/服务器（**Client/Server**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**CA**
> 控制器应用（**Controller Application**），与一个地址绑定的 **ECU** 角色。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）
{: .glossary-source}

**CAK**
> 安全连接关联密钥（**Secure Connectivity Association Key**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**Calibration**
> 标定是对实现控制功能的 SW-C 的参数（即 AUTOSAR SW-C、ECU 抽象或"复杂驱动"（**Complex Driver**）的参数）进行的调整。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Call Point**
> "软件组件"（**Software Component**）中的一个位置，SW-C 在此强制另一 SW-C 中的执行实体（"入口点"（**Entry Point**））执行。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Callback**
> 术语回调函数（**Callback**）主要用于**API**服务，实现通知其他**BSW**模块。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Caller/calling entity**
> 调用者/调用实体位于较高的 **AUTOSAR** 或 **ISO** 层。它是 **API** 调用的用户。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Callout**
> **Callout**是一种函数**Stub**。主要在配置时进行填写，目的是向提供**Callout**函数的模块添加功能。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**CAM**
> 协作感知消息（**Cooperative Awareness Message**）。
>
> 来源：[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**Camel case**
> 驼峰命名法：书写短语时不带空格或标点符号、以单个大写字母指示单词之间分隔的书写方式，第一个单词以大写或小写开头。示例：GetVersionInfo。
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**CAN**
> Controller Area Network —— 控制器局域网。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）
{: .glossary-source}

**Can**
> CAN驱动程序模块
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN CF**
> CAN连续帧N-PDU
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN Channel**
> 从**CAN**控制器通过**CAN**收发器连接到**CAN**网络的物理通道。
>
> 来源：[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）
{: .glossary-source}

**CAN controller**
> CAN控制器仅服务于一个物理通道。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**CAN FC**
> CAN流控N-PDU
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN FD**
> CAN灵活数据速率
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN FF**
> CAN首帧N-PDU
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN Hardware Unit**
> CAN硬件单元可以由一个或多个相同类型的CAN控制器和一个或多个CAN RAM区域组成。CAN硬件单元可以是片上设备，也可以是外部设备。CAN硬件单元由一个CAN驱动程序表示。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**CAN L-PDU**
> 数据链路层协议数据单元。由标识符（**Identifier**）、数据长度（**Data Length**）和数据（**Data (SDU)**）组成。（见[2]）
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**CAN L-SDU**
> 数据链路层服务数据单元。在L-PDU内部传输的数据。（见[2]）
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN LSduId**
> 这是SDU在CAN接口内的唯一标识符。它用于引用L-SDU的路由属性。因此，为了通过CAN接口的API与之交互，上层使用CAN LSduId来引用CAN L-SDU信息结构。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN N-PDU**
> 这是CAN传输层的PDU。它包含一个唯一标识符、数据长度和数据（协议控制信息加上整个N-SDU或其一部分）。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN N-SDU**
> 这是CAN传输层的SDU。在AUTOSAR架构中，它是来自PDU路由器的一组数据。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN N-SDU Info Structure**
> 这是CAN传输层内部的常量结构，包含处理相关CAN N-SDU的发送、接收、分段和重组所需的特定CAN传输层信息。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN NSduId**
> SDU在CAN传输层内的唯一标识符。它用于引用N-SDU的路由属性。因此，为了通过CAN传输层的API与之交互，上层使用CAN NSduId来引用CAN N-SDU信息结构。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CAN SF**
> CAN单帧N-PDU
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Can XL**
> CAN XL 规定了一种具有更高数据速率和更清晰关注点分离的协议与物理层，它构建在 CAN 2.0/FD 之上，并支持以太网帧的隧道传输。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**CAN_DL**
> CAN帧数据长度
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CanIf**
> CAN Interface —— CAN 接口。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）、[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）、[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）、[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**CanNm**
> CAN网络管理（**CAN Network Management**）的缩写
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**CanSM**
> CAN状态管理器（**CAN State Manager**）。
>
> 来源：[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）
{: .glossary-source}

**CanTp**
> CAN传输层
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**CanTrcv**
> CAN收发器模块
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**CanTSyn**
> **CAN** 时间同步模块（**Time Synchronization over CAN** module）。通过 **CAN** 总线分发时间信息、实现 **CAN** 特定时间同步协议的模块。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**Cascaded Switch**
> 级联交换机（**Cascaded Switch**）是由至少两个以太网交换机组成的以太网交换机：一个主交换机和一个从交换机。主交换机与从交换机通过上行端口连接。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Cascading Failure**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.13
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Category 1 Interrupt**
> 类别 1（Cat1）中断由 OS 支持，但其代码只允许调用 OS 函数的一个非常小的子集。此外，它们可以绕过 OS。类别 1 中断的代码（通常）取决于所使用的编译器和微控制器。类别 1 中断不允许使用 ISR() 宏。类别 1 中断需要自行实现/建立自己的中断帧（**Interrupt Frame**）。尽管如此，仍必须对它们进行配置，以便将其纳入中断向量表。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Category 2 Interrupt**
> 类别 2（Cat2）中断由 OS 支持，其代码可以调用 OS 函数的一个子集。类别 2 中断的定义必须使用 ISR() 宏，以便被 OS 识别。类别 2 中断的中断帧由 OS 管理。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Causality of Transmission**
> 来自源网络的、具有相同标识符的 PDU（PDU 实例）的发送顺序在目的网络中得以保持。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**CBC**
> 弯道制动控制（**Cornering Brake Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**CBF**
> 基于竞争的转发（**Contention-Based Forwarding**）。
>
> 来源：[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**CBR**
> 信道忙闲比（**Channel Busy Ratio**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](cp/communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**CBV**
> 控制位向量（**Control Bit Vector**）
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）、[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**CC**
> 通信控制器（**Communication Controller**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**CCS**
> 组合充电系统（**Combined Charging System**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**CCSA**
> 中国通信标准化协会（**China Communications Standards Association**）。
>
> 来源：[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**CDD**
> 复杂驱动（**Complex Driver**）。未被 AUTOSAR 标准化的软件实体，可以访问 AUTOSAR 接口和/或基础软件模块 API，或经由它们被访问；位于分层软件架构的复杂驱动层。
>
> 来源：[CDD Design and Integration Guideline（CDD 设计与集成指南）](cp/general/cdd_design_and_integration/index.md)（AUTOSAR_CP_EXP_CDDDesignAndIntegrationGuideline）、[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）
{: .glossary-source}

**CEMR**
> 控制使能掩码记录（**ControlEnableMaskRecord**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**CF**
> 连续帧，传输协议术语。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）、[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Channel**
> 通道：按相同准则定义的数据的软件交换媒介。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**channel**
> NM节点/ECU所连接到的逻辑总线。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**Channel（Crypto Driver Object Path）**
> 通道：从加密服务管理器队列经由加密接口到特定加密驱动程序对象的路径。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Channel（Data Transfer Link）**
> 可以进行数据传输的链路；存在多个 Channel 时，通常会为 Channel 分配某种 ID（**A link at which a data transfer can take place**）
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Checkpoint**
> 受监督实体控制流中报告活动的一个点（**A point in the control flow of a Supervised Entity where the activity is reported**）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**CHI**
> 控制器主机接口（**Controller Host Interface**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**ChrgM**
> **Charging Manager**，充电管理器。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**CIT**
> 信道空闲时间（**Channel Idle Time**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](cp/communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）
{: .glossary-source}

**Class**
> 一个类（**Class**）代表一组具有相似电气特性的信号。如：模拟类（**Analogue class**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Class B1 counter**
> Class B1 故障被确认（**Confirmed**）且处于 **TestFailed** 状态期间的发动机运行小时数。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Classic Platform**
> AUTOSAR 为深度嵌入式系统以及对可预测性、安全性和响应性有高要求的应用软件定义的软件平台。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Client**
> 承载客户端服务（**ClientServices**）的ECU。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）、[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}

**Client Server Communication Graph**
> 相互连接的各 `PortPrototype` 中实例化的操作上的所有 `ServerCallPoint` 之和，包括所属的服务器可运行实体（**Client Server Communication Graph**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Client Service**
> 消费一个服务。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Client-Server Communication**
> 一种可能分布在系统中的特定通信形式，其中软件实体充当客户端、服务器或二者兼有，通常由 1...n 个客户端通过特定协议向一个服务器请求服务。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Client-Server communication**
> 客户端-服务器通信（**Client-Server communication**）涉及两个实体。客户端是要求服务的一方，服务器是提供服务的一方。客户端发起通信，请求服务器执行服务，必要时传输参数集合。服务器以**RTE**的形式，等待来自客户端的传入通信请求，执行请求的服务并发送对客户端请求的响应。因此服务启动的方向是用来对**AUTOSAR**软件组件是客户端还是服务器分类的主要标识。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Client-Server Interface**
> 客户端-服务器接口是一种特殊的"端口接口"（**Port Interface**），用于客户端-服务器通信的情形。客户端-服务器接口定义了"服务器"（**Server**）提供的、可被"客户端"（**Client**）使用的操作。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Client-Service-Instance-Entry**
> 另一个ECU所提供的服务实例的配置和所需数据，在使用该服务（客户端）的ECU上被称为Client-Service-Instance-Entry。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）
{: .glossary-source}

**Cluster Signal**
> 簇信号表示某个特定通信簇上的聚合系统信号。簇信号可以独立于帧来定义。这允许一种开发方法论：先定义信号，然后在后续阶段将信号分配到帧。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**cluster（集群）**
> 多个相互连接的节点构成的通信系统。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**CM**
> **AUTOSAR** 自适应通信管理（**AUTOSAR Adaptive Communication Management**）。
>
> 来源：[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**CMDT**
> **Connection Mode Data Transfer**，又称 **RTS**/**CTS**，**SAE J1939** 传输协议的点对点变体。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**CnV2xM**
> 中国车辆到一切管理（**Chinese Vehicle-2-X Management**）。
>
> 来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**CnV2xMgt**
> 中国 **Vehicle-2-X** 管理（**Chinese Vehicle-2-X Management**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**CnV2xMsg**
> 中国车辆到一切消息（**Chinese Vehicle-2-X Message**）。
>
> 来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**CnV2xNet**
> 中国车辆到一切网络（**Chinese Vehicle-2-X Network**）。
>
> 来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**CnV2xSec**
> 中国车辆到一切安全（**Chinese Vehicle-2-X Security**）。
>
> 来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**Code Generator**
> 代码生成器（**Code Generator**）接收针对 BSW 模块的完整且格式正确的 XML，并生成配置该模块的代码和数据。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Code Variant Coding**
> 根据外部需求，通过选择功能备选项来调整软件。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**CodeGenerationTime variability**
> 由最迟绑定时间为 `CodeGenerationTime` 的 `VariationPoint` 或 `AttributeValueVariationPoint` 定义的可变性（**CodeGenerationTime variability**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**CoG**
> 重心（**Center of Gravity**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**coherency group**
> 由 **RTE** 负责数据相干性的一组隐式读访问和隐式写访问（**coherency group**）。请注意在本规范的上下文中，相干性的定义包括：不同 `VariableDataPrototype` 的读数据值必须来自同一代，除非这些值由属于该相干组的隐式写访问改变；不同 `VariableDataPrototype` 的已写数据值，应在属于该相干组的最后一个隐式写访问之后才传送给不属于该相干组的读者。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**coherent implicit data access**
> 属于某个相干组的隐式读访问或隐式写访问（**coherent implicit data access**）；因此它被某个 `RteImplicitCommunication` 容器中 `RteCoherentAccess` 参数设置为 true 的 `RteVariableReadAccessRef` 或 `RteVariableWriteAccessRef` 引用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**coherent implicit read access**
> 属于某个相干组的隐式读访问（**coherent implicit read access**）；因此它被某个 `RteImplicitCommunication` 容器中 `RteCoherentAccess` 参数设置为 true 的 `RteVariableReadAccessRef` 引用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**coherent implicit write access**
> 属于某个相干组的隐式写访问（**coherent implicit write access**）；因此它被某个 `RteImplicitCommunication` 容器中 `RteCoherentAccess` 参数设置为 true 的 `RteVariableReadAccessRef` 或 `RteVariableWriteAccessRef` 引用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Com**
> 通信（**Communication**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**COM I-PDU**
> 由COM信号（**COM Signals**）在COM模块中组装而成的I-PDU。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Combined DTC**
> 普通 **DTC**，但被多个监视器报告的多个事件引用（例如 **ECU** 缺陷，由不同的硬件缺陷组成）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**ComM**
> Communication Manager
>
> 来源：[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）
{: .glossary-source}

**Common Cause Failure**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.14
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**common mode machine instance**
> 由 **BSW** 模块和 **SW-C** 共享的特殊模式机实例（**common mode machine instance**）：当软件组件端口中实例化的某个 `ModeDeclarationGroupPrototype` 与某个基础软件模块实例的 `providedModeGroup` `ModeDeclarationGroupPrototype` 同步（`SwcBswMapping` 的 `synchronizedModeGroup`）时，**RTE** 生成器只创建一个模式机实例，即公共模式机实例。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Communication Attribute**
> 通信属性按照开发阶段定义 AUTOSAR 通信模式的行为与实现两个方面。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Communication Channel**
> 用于将信息从发送方（或发送器）传递到接收方的介质（**The medium used to convey information from a sender (or transmitter) to a receiver**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Communication Graph**
> 相互连接的各 `PortPrototype` 中实例化的 `PortInterface` 元素上的所有 `AbstractAccessPoint` 之和，或相互连接的各 `BswModuleDescription` 中 `BswModuleEntity` 对接口元素的所有访问之和（**Communication Graph**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Communication Job**
> TTCAN 通信作业定义特定的通信操作与所分配的执行时间。
>
> 来源：[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**Communication Mode**
> 决定允许何种通信的模式：完全通信 = COMM_FULL_COMMUNICATION；无通信 = COMM_NO_COMMUNICATION；静默通信 = COMM_SILENT_COMMUNICATION（**Mode determining which kind of communication are allowed**）。用户不能请求 COMM_SILENT_COMMUNICATION——它是关机时用于同步网络的内部模式。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Complex Driver**
> AUTOSAR 未标准化的软件实体，它可以通过"AUTOSAR 接口"（**AUTOSAR Interface**）和/或"基础软件模块"（**Basic Software Module**）API 访问其他实体或被其他实体访问。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Composition**
> 组合（**Composition**）。以类型-原型模式嵌套组织软件组件的结构；在抽象平台中用于按任意深度递归地定义组件层次。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**Compositionality**
> 当系统中某个软件组件或子系统的行为与整个系统的负载和配置无关时，即具有可组合性（**Compositionality**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Concurrent TesterPresent**
> 设置 suppressPosRspMsgIndicationBit（3E 80）并通过功能寻址接收的 **UDS** 服务 **TesterPresent**；也称为保活（keep-alive）逻辑。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Conditioned Signal**
> 处理后的信号（**Conditioned Signal**）是电信号在 ECU 内部的电气表示。它被传送给处理器，并以电压和时间表示（对于逻辑信号则以高电平或低电平表示）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Confidentiality**
> 数据或信息不向未授权的人员或进程提供或泄露的特性。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Configuration**
> 系统中硬件和/或软件元素的布置。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Confirmation**
> 确认（**Confirmation**）是PDU路由器对AUTOSAR COM模块请求已成功完成的报告。它是对COM请求的响应，例如PDU已成功发送。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Connection**
> 一个传输协议会话，或者是N-SDU上的发送会话，或者是接收会话。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Connection channel**
> CAN传输层管理多个连接所使用的资源以节省RAM。当一个连接变为活动状态时，该连接使用的通道将对其他连接不可用。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Connector**
> 连接器（**Connector**）连接软件组件（**Software Component**）的"端口"（**Port**），并表示这些端口之间的信息流。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Consumed Eventgroup multicast connection**
> 描述当**SdClientService**经由Consumed Eventgroup多播端点接收事件时，已建立的套接字连接的使用情况的术语。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Consumed Eventgroup multicast endpoint**
> 描述按**Consumed Eventgroup**为**SdClientService**预配置的多播地址和端口元组的术语。以该多播地址和端口订阅的SdClientService向SdServer指示应将相应的事件发送到哪个端点。Consumed Eventgroup多播端点经由**SubscribeEventgroup**或**StopSubscribeEventgroup**条目所引用的Multicast option通告。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Consumed Eventgroup unicast connection**
> 描述当**SdClientService**经由Consumed Eventgroup单播端点接收事件时，已建立的套接字连接的使用情况的术语。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Consumed Eventgroup unicast endpoint**
> 描述按**Consumed Eventgroup**为**SdClientService**预配置的单播地址和端口元组的术语。以该单播地址和端口订阅的SdClientService向SdServer指示应将相应的事件发送到哪个端点。Consumed Eventgroup单播端点经由**SubscribeEventgroup**或**StopSubscribeEventgroup**条目所引用的Endpoint option通告。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**contained I-PDU**
> 被组装进容器PDU（**Container PDU**）或从中提取出来的I-PDU。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Container PDU**
> 包含I-PDU和报头的PDU。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Context Data**
> 与安全事件（**SEv**）相关的可选信息，提供对安全事件的更广泛理解（例如被损坏的数据）；其内容和编码由传感器外部定义，**IdsM** 模块不知晓。
>
> 来源：[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**Context Data Buffer**
> 大小可变的缓冲区，以适配 **SEv** 上下文数据的需要。
>
> 来源：[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**Context ID**
> 一个用户定义的标识符，用于对一个应用/**SW-C** 生成的日志和跟踪消息进行分组；Context ID 按 Application ID 分组，且在一个 Application ID 内唯一。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Continuous Transmission**
> 与单次发送相反，即使没有新的发送请求，消息也将被周期性地传输。
>
> 来源：[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**Continuous-MI counter**
> 持续 MI 被命令点亮期间发动机运行的小时数。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Control Flow**
> 多个实体之间信息的定向传输，直接导致接收实体的状态改变。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Controller**
> （TTCAN）控制器是 **CPU** 片上或外部的独立硬件器件。一个控制器连接到一个物理通道。
>
> 来源：[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**Conversion Mode**
> One-Shot：**ADC**通道组的转换在触发后执行一次，结果写入所分配的结果缓冲区。触发可以是软件**API**调用或硬件事件。Continuous：**ADC**通道组的转换在软件**API**调用（启动）后连续执行，结果写入所分配的结果缓冲区。转换本身自动运行（由硬件/中断控制）。连续转换可通过软件**API**调用（停止）停止。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**Conversion Time**
> 转换时间是指将采样的模拟值转换为数值所需的时间。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**COOP**
> 严重离位（**Critical Out of Position**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**Coordinate**
> 控制并协调两个或多个事件或操作，使其以有组织、可预测的方式运行。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Coordinated shutdown**
> 以两个或多个总线的关闭恰好同时完成的方式关闭它们。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**Coordination algorithm**
> 在所有条件都满足的情况下发起协调关闭。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**copy semantic**
> 副本语义指访问实体能够以非并发、非抢占的方式从自己的执行上下文读取或写入"被复制的"数据（**copy semantic**）。如果所有访问实体位于同一抢占区内，这可能不需要真正的物理数据复制。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Core**
> **CPU** 及其紧邻的功能资源。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**core local mode user group**
> 在模式使用者属于不同分区、而这些分区又被调度到不同微控制器核上的情况下，整体模式机实例需要跨核分布；此时某些限制只适用于在同一微控制器核上执行的模式使用者之间。属于同一模式管理者、且其 `EcucPartition` 属于引用同一 `EcucCoreDefinition` 的 `OsApplication` 的所有模式使用者，属于同一个核本地模式使用者组（**core local mode user group**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**CPU**
> 中央处理器（**Central Processing Unit**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**CRC**
> 循环冗余校验（**Cyclic Redundancy Check**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[AUTOSAR RamTst（RAM测试）](cp/memory/ramtst/index.md)（AUTOSAR_CP_SWS_RAMTest）、[Specification of CRC Routines（CRC 例程规范）](cp/libraries/crc/index.md)（SWS_CRCLibrary）
{: .glossary-source}

**CRF**
> 时钟参考格式（**Control Reference Format**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**Cross Cluster Communication**
> 实现软件集群之间 VFB 通信的 Software Cluster Connection 功能块（**Cross Cluster Communication**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**Cross Software Cluster Communication Plug-In**
> 跨软件集群通信插件（**Cross Software Cluster Communication Plug-In**）是处理通往其他软件集群的通信的 **RTE** 实现插件；如果配置了 **ECU** 内转换，则也包括转换器的处理。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Cross-Cluster External Graph**
> 一种特殊的**外部图**，在集群式软件架构下跨越多个**软件集群**（**Software Cluster**）。其配置依赖于模式（由**宿主软件集群**（**Host Software Cluster**）控制），并且另外具有专门的配置结构。注意：单个**软件集群**内的**外部图**可以在不使用集群式软件架构专门配置结构的情况下建模。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**CRYIF**
> 加密接口（**Crypto Interface**）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**CRYPTO**
> 加密驱动程序（**Crypto Driver**）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Crypto Driver Object**
> 加密驱动程序对象：加密驱动程序实现一个或多个加密驱动程序对象，每个对象可以在硬件或软件中提供不同的加密原语；同一加密驱动程序的各加密驱动程序对象彼此独立，每个对象只有一个工作区（即同一时刻只能执行一个加密原语），独立性的唯一例外是默认随机数生成器的使用。
>
> 来源：[Utilization of Crypto Services（加密服务使用指南）](cp/crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices）、[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Crypto Primitive**
> 加密原语：在加密驱动程序对象中实现的已配置加密算法的实例；它指向 **CSM** 向应用程序提供的功能、具体的底层算法家族（如 **AES**、**MD5**、**RSA**）以及算法模式（如 **ECB**、**CBC**）。
>
> 来源：[Utilization of Crypto Services（加密服务使用指南）](cp/crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices）、[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**CS**
> 片选（**Chip Select**）。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**CSM**
> 加密服务管理器（**Crypto Service Manager**）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**CSUM/Checksum/signature**
> 测试执行结果的数值表示。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**CTID**
> Context ID —— 上下文 ID。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**CTO**
> Command Transfer Object —— 命令传输对象。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**Cumulative Continuous-MI counter**
> 在其寿命期内 **MI** 被持续命令点亮的发动机运行小时数。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Current Time Tuple**
> 保存当前全局时间的本地实例及对应当前虚拟本地时间的时间元组。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**CV2x**
> Cellular Vehicle to X driver，蜂窝车辆到X驱动程序。
>
> 来源：[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）
{: .glossary-source}

**CVC**
> 卡片可验证证书（**Card Verifiable Certificate**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**CVT**
> 无级变速器（**Continuously Variable Transmission**）
>
> 来源：[Explanation of Application Interfaces of the Powertrain Engine Domain（动力总成（发动机）域应用接口说明）](cp/application_interfaces/powertrain/index.md)（AUTOSAR_CP_EXP_AIPowertrain）
{: .glossary-source}

**CW**
> 竞争窗口（**Contention Window**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](cp/communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）
{: .glossary-source}

**CWU**
> 整车唤醒（**Car Wakeup**）
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

## D

**DA**
> 目标地址（**Destination Address**），SAE J1939 消息 29 位标识符的组成部分
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）
{: .glossary-source}

**DAD**
> 重复地址检测（**Duplicate Address Detection**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**DAQ**
> Data AcQuisition, Data AcQuisition Packet —— 数据采集，数据采集包。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**DAS**
> 驾驶辅助系统（**Driver Assistance System**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Data**
> 以适合通信、解释或处理的形式化方式对信息的可重新解释的表示。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Data Communication Graph**
> 相互连接的各 `PortPrototype` 中实例化的 `VariableDataPrototype` 上的所有 `VariableAccess` 之和，或 `InternalBehavior` 中对 `VariableDataPrototype` 的所有 `VariableAccess` 之和，或相互连接的各 `BswModuleDescription` 中对 `VariableDataPrototype` 的所有 `BswVariableAccess` 之和（**Data Communication Graph**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Data Element**
> 数据元素（**Data Element**）在"发送方-接收方接口"（**Sender-Receiver Interface**）的上下文中声明。它们用作发送方与接收方之间交换的数据单元。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Data element**
> 发送者和接收者之间交换的数据。**E2E** 转换器将数据元素一对一地映射到 **I-signal** 或 **I-signal** 组。
>
> 来源：[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）
{: .glossary-source}

**Data Flow**
> 多个实体之间数据的定向传输。所传输的数据与接收方的状态改变没有直接关系。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Data frame**
> 数据帧：**SPI** 总线上与 SpiDataWidth 相关的位的物理帧。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**Data integrity**
> 数据完整性（**Data integrity**）——数据自被授权源创建、传输或存储之时起未曾以未经授权方式更改的特性。
>
> 来源：[Secure Onboard Communication Protocol Specification（安全车载通信协议规范）](foundation/protocols/prs_secoc_protocol/index.md)（AUTOSAR_FO_PRS_SecOcProtocol）
{: .glossary-source}

**Data integrity**（数据完整性）
> 数据完整性是指数据自被合法来源创建、传输或存储以来未被以未经授权的方式更改的属性。为确保数据完整性，应具备检测未经授权方数据操纵的能力。数据操纵包括插入、删除和替换等。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Data Invalid Value**
> 数据无效值（**Data Invalid Value**）是AUTOSAR COM模块发送的值，用于指示发送侧的AUTOSAR软件组件无法提供有效值。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Data origin authentication**（数据来源认证）
> 数据来源认证是一种认证类型，其中一方被证实为在过去某个（通常未指定的）时间创建的特定数据的（原始）来源。根据定义，数据来源认证包含数据完整性。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**data semantic**
> 当数据被分布时，最后接收到的值是所关注的（last-is-best 语义）；因此 `SwDataDefProps` 的 `swImplPolicy` 属性所声明的软件实现策略不应为 `queued`（**data semantic**，数据语义）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Data Variant Coding**
> 根据外部需求，通过设置某些特征数据来调整软件。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**DCC**
> 分布式拥塞控制（**Decentralized Congestion Control**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**DCM**
> 诊断通信管理器（**Diagnostic Communication Manager**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**Dcm**
> 诊断通信管理器模块
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**DDS PDU** / **非 DDS PDU**
> 包含/不包含 **DDS** 数据的 **PDU**（例如：列出或未列在 **DdsAppDataTxPduCollection**、**DdsAppDataRxPduCollection**、**DdsDomainParticipantUnicastRtpsPduCollection** 或 **DdsDomainParticipantMulticastRtpsPduCollection** 容器中的 **PDU**）。
>
> 来源：[Data Distribution Service for Classic Platform（经典平台数据分发服务）](cp/communication/data_distribution/index.md)（AUTOSAR_CP_SWS_DataDistributionService）
{: .glossary-source}

**DE**
> 数据元素（**Data Element**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**Deadline**
> 实体的某次执行必须结束的时间点。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Deadline End Checkpoint**（**Deadline Stop Checkpoint**）
> 为其配置了**截止时间监督**、并且是某个特定**截止时间监督**终点的**检查点**。一个**检查点**可以同时是**截止时间起始检查点**和**截止时间结束检查点**——即当**截止时间监督**被串联时。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Deadline Start Checkpoint**
> 为其配置了**截止时间监督**、并且是某个特定**截止时间监督**起点的**检查点**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Deadline Supervision**
> 一种监督，用于检查两个**检查点**之间的执行时间是否小于给定的执行时间上限。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**Debounce counter**
> 用于基于计数器去抖动算法的内部计数器。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Debounce Time**
> 具有相同 **PDU** 的两条 **TX** 报文之间的最小间隔。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Debugging**
> 调试是在出现软件问题时收集信息的过程。所收集的信息用于分析该软件问题。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Default Error Tracer**
> 默认错误跟踪器仅用于支持软件开发和集成，不包含在生产代码中。其API是定义了的，但功能可以由开发人员根据其特定需求进行选择和实现。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Deferred Data Type**
> 推迟数据类型（**Deferred Data Type**）。抽象平台独有的占位数据类型 `ApplicationDeferredDataType`，不承载具体类型类别，用于把精确类型化推迟到下游设计阶段。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**DEM**
> 诊断事件管理器（**Diagnostic Event Manager**）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR MCU Driver（微控制器单元驱动）](cp/mcal/mcu_driver/index.md)（SWS_MCUDriver）、[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）、[AUTOSAR Watchdog Driver（看门狗驱动）](cp/safety/watchdog_driver/index.md)（SWS_WatchdogDriver）、[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）、[AUTOSAR Large Data COM（大数据 COM）](cp/communication/large_data_com/index.md)（SWS_LargeDataCOM）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）、[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](cp/communication/ethernet_switch_driver/index.md)（AUTOSAR_CP_SWS_EthernetSwitchDriver）、[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**Dem-internal data value**
> 某些数据值（例如发生计数器）由 **Dem** 模块自身在内部计算。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DemComponent / Monitored Component**
> 被监控组件是系统的一部分，由一个或多个监控检查其是否正常运行（参见第 6.5 节）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DEN**
> 分布式环境通知（**Decentralized Environmental Notification**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**DENM**
> 分布式环境通知消息（**Decentralized Environmental Notification Message**）。
>
> 来源：[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**Denominator**
> 特定监视器 m 的分母（Denominatorm）是一个计数器，指示车辆驾驶事件的数量，并考虑该特定监视器特定的条件。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Dependability**
> 可信性（**Dependability**）定义为计算机系统的可信程度，使得对其所交付服务的依赖是正当合理的。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Dependent / Secondary ECUs**
> 从属/辅助 **ECU**（dep. / sec. ECU）始终与一个 **Master** 或 **Primary ECU** 相关联。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Dependent Failure**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.22
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**DET**
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR MCU Driver（微控制器单元驱动）](cp/mcal/mcu_driver/index.md)（SWS_MCUDriver）、[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Watchdog Driver（看门狗驱动）](cp/safety/watchdog_driver/index.md)（SWS_WatchdogDriver）、[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Default Error Tracer（默认错误跟踪器）](cp/system_services/default_error_tracer/index.md)（SWS_DefaultErrorTracer）、[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）、[AUTOSAR Large Data COM（大数据 COM）](cp/communication/large_data_com/index.md)（SWS_LargeDataCOM）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**Det**
> 默认错误追踪器（**Default Error Tracer**）。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**DF**
> 数据帧（**Data Frame**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**DHCP**
> Diagnostic Host Configuration Protocol —— 诊断主机配置协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**DHCPv4**
> 互联网协议版本4的动态主机配置协议（**Dynamic Host Configuration Protocol for Internet Protocol Version 4**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**DHCPv6**
> 互联网协议版本6的动态主机配置协议（**Dynamic Host Configuration Protocol for Internet Protocol Version 6**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**Diagnostic Channel**
> 诊断通道：诊断工具与 **ECU** 之间可以进行数据传输的链路。例如，**ECU** 通过 **CAN** 连接时，诊断通道会分配一个 **CAN-ID**；连接至 **MOST**、**FlexRay**、**LIN** 等总线系统的诊断通道同样适用。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Diagnostic Coverage**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.25
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Diagnostic Event**
> 诊断事件（**Diagnostic Event**）定义了可由 DEM 模块处理的最小单元。诊断事件的状态表示某个监控器的结果。DEM 通过 RTE 或其他 BSW 模块从 SW-C 接收监控器的结果。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Diagnostic Event Manager**
> 诊断事件管理器是生产代码中提供的标准AUTOSAR模块，其功能在AUTOSAR项目中规定。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**DID**
> 数据标识符（**Data Identifier**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**DIO**
> Digital Input Output (SPAL module)
>
> 来源：[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）
{: .glossary-source}

**Dio**
> 数字输入输出，**SPAL** 软件模块之一（**Digital input output**）。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**DIP**
> 数字输入/输出（**Digital Input/Output**）
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](cp/safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**direct function call**
> 直接函数调用（**direct function call**）是纯 **RTE** 代码之外的任何手段都不参与的函数调用。通常它是 **RTE API** 中的一个 **C** 函数调用（见 7.1.6、6.2.2.3.1 和 8.5.1.2 节）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Directed acyclic graph**
> 没有循环依赖的依赖关系图。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Disciplined HW Clock**
> 可以在速率和偏移上被调整以跟随参考时钟的硬件时钟。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Displacement**
> 用需要存储的更重要的事件内存条目替换最不重要的条目。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Distinction unilateral/ bilateral authentication**（单向/双向认证的区分）
> 在单向认证（**unilateral authentication**）中，一方证明其身份。请求方甚至未被认证到可证明其有权请求认证的程度。在双向认证（**bilateral authentication**）中，请求方也至少被认证（见下文）以证明其请求的权限。基于上述双向认证，存在一种高效且更安全的双向端点认证方式。除了最初由接收方（在第一条消息中）请求的认证（在第二条消息中）之外，发送方也请求一次认证。接收方发送第三条消息，提供发送方所请求的认证。这仅需要三条消息（相比之下，两条单向消息需要四条）。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Diversity**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.28
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**DLC**
> 数据长度码（**Data Length Code**，CAN报文中描述SDU长度的部分）。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**DLL**
> 数据链路层（**Data Link Layer**）。
>
> 来源：[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**Dlt**
> Diagnostic Log and Trace —— 诊断日志与跟踪。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Dlt User**
> 一个 **Dlt** 用户代表一个生成的 **Dlt** 消息的来源。可能的用户是 **SW-C**、RTE（用于 **VFB** 跟踪）、**DEM** 或 **DET**。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**DM**
> **AUTOSAR** 自适应诊断管理（**AUTOSAR Adaptive Diagnostic Management**）。
>
> 来源：[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**DME**
> 专用管理实体（**Dedicated Management Entity**）。
>
> 来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）
{: .glossary-source}

**DM（Deadline Monitoring）**
> 截止期监控（**Deadline Monitoring**），详情见第6.3.6节。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**DM（Diagnostic Message）**
> SAE J1939 诊断消息（**SAE J1939 Diagnostic Message**），定义于 SAE J1939-73，多数由灯状态（Lamp Status）与可变数量的 DTC 组成
>
> 来源：[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**DoS**
> 拒绝服务（**Denial of Service**）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**DP**
> 数据页（**Data Page**），18 位 **PGN** 的最高有效位（**MSB**）。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**DPI**
> 深度包检查（**Deep Packet Inspection**）——额外分析 **OSI** 模型第 5-7 层的有状态应用层防火墙技术。
>
> 来源：[Requirements on Firewall（防火墙需求）](foundation/security/rs_firewall/index.md)（AUTOSAR_FO_RS_Firewall）
{: .glossary-source}

**DP（Data Page）**
> 数据页（**Data Page**），18 位 PGN 的最高有效位（MSB）
>
> 来源：[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**DP（DCC Profile）**
> DCC 配置（**DCC Profile**）。
>
> 来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](cp/communication/wlan_transceiver_driver/index.md)（SWS_WirelessEthernetTransceiverDriver）
{: .glossary-source}

**DRL**
> 日间行车灯（**Daytime Running Light**）
>
> 来源：[Safety Use Case（安全用例）](cp/safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**DSD**
> 诊断服务分发器（**Diagnostic Service Dispatcher**），**Dcm** 模块的子模块。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**DSL**
> 诊断会话层（**Diagnostic Session Layer**），**Dcm** 模块的子模块。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**DSMP**
> 专用短消息协议（**Dedicated Short Message Protocol**）。
>
> 来源：[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）
{: .glossary-source}

**DSP**
> 诊断服务处理（**Diagnostic Service Processing**），**Dcm** 模块的子模块。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**&lt;DstLo&gt;**
> 作为 L-SDU 目标的下层通信接口模块。DstLo 可以是一对多。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**&lt;DstLoTp&gt;**
> 下层传输协议模块，作为**I-PDU**的目的地。**DstLoTp**可以是一对多的。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**DTC group**
> 唯一标识一组 **DTC**。一个 **DTC** 组被映射到有效 **DTC** 的范围内。通过提供一个 **DTC** 组，表示对该组中的所有 **DTC** 请求某一特定操作。**DTC** 组的定义由 ISO 14229-1 规定，并为 **OEM**/供应商特定。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DtcGroupAllDtcs**
> 所有已配置 **DTC** 的分组（表示为 0xFFFFFF）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DTC（Diagnostic Trouble Code）**
> 诊断故障码（**Diagnostic Trouble Code**），在诊断消息中传输，包含问题来源（SPN）、问题种类（FMI）与出现计数器（OC）
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**DTC（Regulation of the Drag Torque）**
> 拖滞力矩调节（**Regulation of the Drag Torque**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**DTO**
> Data Transfer Object —— 数据传输对象。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**DTR**
> 诊断测试结果（**Diagnostic Test Result**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**DYC**
> **OBD** 术语：驾驶循环（**Driving Cycle**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Dynamic Length I-PDU**
> 动态长度I-PDU（**Dynamic Length I-PDU**）是包含动态长度信号的I-PDU。其长度随所包含动态长度信号的长度而变化。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Dynamic Length Signal**
> 动态长度信号（**Dynamic Length Signal**）是其长度可以在运行时变化的信号。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**dynamic part**
> 见[2]。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Dynamic PDU**
> 具有动态标识符的"协议数据单元"（**Protocol Data Unit**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Dynamic Routing**
> 网关中信号或"协议数据单元"（**Protocol Data Unit**）的路由可以在整个运行期间改变，而无需改变网关的运行模式。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

## E

**e.g.**
> （拉丁语）exempli gratia =（英语）for example，即「例如」。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**E2E**
> 端到端保护（**End-To-End Protection**）。
>
> 来源：[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）
{: .glossary-source}

**E2E Profile**
> 对特定通信栈在数据结构、服务、行为状态机、错误处理方面的功能完整描述。E2E Profile 定义在 AUTOSAR E2E 库中。E2E Profile 可通过运行时参数配置。一组特定的运行时参数称为 E2E profile 变体（**E2E profile variant**）。为了实现互操作性，应用开发者应使用 E2E 库中定义的 E2E profile 变体。
>
> 来源：[Requirements on E2E（端到端通信保护需求）](foundation/communication_management/rs_e2e/index.md)（AUTOSAR_FO_RS_E2E）、[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**E2E Protection Alive Counter**
> 存活计数器（**Alive Counter**）是每次发送请求时递增的计数器。接收方检查计数值是否发生变化，但不检查计数器是否被正确递增。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**E2E Protection Sequence Counter**
> 序列计数器（**Sequence Counter**）是每次发送请求时递增的计数器。接收方对每条报文检查计数值是否被正确递增。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**EA**
> EEPROM 抽象（**EEPROM Abstraction**）。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**EAI**
> 期望存活指示（**Expected Alive Indications**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**EB**
> 外部缓冲通道（**Externally buffered channels**）：包含待传输数据的缓冲区位于 SPI 处理器/驱动程序之外。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）
{: .glossary-source}

**EBD**
> 制动力分配（**Electronic Brake Force Distribution**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**EC**
> 以太网控制器（**Ethernet controller**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**eCall**
> 紧急呼叫（**Emergency Call**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ECC**
> 纠错码（**Error Correction Code**）
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**ECDSA**
> 椭圆曲线数字签名算法（**Elliptic Curve Digital Signature Algorithm**）。
>
> 来源：[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**ECU**
> 电子控制单元（**Electronic Control Unit**）
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**ECU Abstraction Layer**
> ECU 抽象层（**ECU Abstraction Layer**）位于"微控制器抽象层"（**Microcontroller Abstraction Layer**）之上，对 ECU 原理图进行抽象。它为特定 ECU 实现，并提供访问外设和设备的 API，而无论其位置（片上/片下）及其与微控制器的连接方式（端口引脚、接口类型）如何。任务：使较高的软件层次独立于 ECU 硬件布局。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ECU Configuration**
> 集成并配置一个 ECU 软件的活动。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ECU Configuration Description**
> ECU 配置活动的输出，包含配置参数的取值和引用。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ECU HW**
> AP 机器与 CP ECU 的任意组合的容器术语。一般来说，ECU-HW 通常是对物理或虚拟实现的抽象/独立于物理或虚拟实现，并且不传递任何硬件壳体（**HW-Housing**）信息，即多个物理 ECU-HW 或一个物理 ECU-HW 提供多个虚拟 ECU-HW（除非另有说明）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ECU ID**
> 一个 ECU 的名称，由四个 8 位 ASCII 字符组成（例如 ABS0 或 COMB）。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**ECU Instance**
> ECU 实例（**ECU Instance**）表示经典平台协议栈的一次单独实例化，它可以运行在物理 ECU-HW 上（无 hypervisor）或虚拟 ECU-HW 上（有 hypervisor）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ECU pin**
> ECU引脚（**ECU pin**）是**ECU**与电子系统其余部分的电气硬件连接。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**ECU Signal**
> ECU信号（**ECU Signal**）是电信号的软件表示。一个**ECU**信号具有一些属性（**Attribute**）和一个符号名称（**Symbolic name**）。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**ECU Signal Group**
> ECU信号组（**ECU Signal Group**）是一组电信号的软件表示。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**EcuC**
> **ECU** 配置（**ECU Configuration**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**EcuM**
> **ECU** 状态管理器（**ECU State Manager**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](cp/communication/ethernet_switch_driver/index.md)（AUTOSAR_CP_SWS_EthernetSwitchDriver）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**EDP**
> 扩展数据页（**Extended Data Page**），18 位 **PGN** 的第二位（**MSB** 之后）。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**Efx**
> 扩展定点数学库（**Extended Mathematical library - Fixed point**）。
>
> 来源：[Specification of Extended Fixed Point Routines（扩展定点例程规范）](cp/libraries/efx/index.md)（AUTOSAR_CP_SWS_EFXLibrary）
{: .glossary-source}

**EID**
> Entity identifier —— 实体标识符。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**EIM**
> 外部识别方式（**External Identification Means**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**EIRA**
> 外部和内部请求数组（**External and Internal Request Array**）
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Electrical Signal**
> 电信号（**Electrical Signal**）代表**ECU**引脚上的物理信号。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Electronic Control Unit**
> 由至少一个 CPU 和相应外设组成、置于同一壳体内的嵌入式计算机系统。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Elementary Supervision Status**
> 表示**存活监督**、**时限监督**或**逻辑监督**当前状态的状态，基于对该监督的评估（正确/错误）。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**eMAID**
> e-移动账户标识符（**e-Mobility Account Identifier**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**Empty Function**
> 由 AUTOSAR 规范定义、但不实现或不改变完成其被指派的功能职责所需行为的任何 C 函数。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Endpoint Option**
> 端点选项（**Endpoint Options**）用于通告一个单播地址和端口的元组。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**EndToEndTransformationDescription**
> 所定义的特定类，包含约 30 个用于 **E2E** 配置的参数（参见 [4]）。它被 **TransformationTechnology** 引用。
>
> 来源：[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）
{: .glossary-source}

**Entity authentication**（实体认证）
> 实体认证是这样一种过程：一方（通过获取佐证证据）确信协议中涉及的第二方的身份，并且该第二方确实参与了协议（即，在获取证据时或紧邻其之前处于活动状态）。
> **注意：** 实体认证意味着证明存在性和操作就绪性。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Entry Point**
> "软件组件"（**Software Component**）中 SW-C 的某个执行实体开始的位置。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**EPB**
> 电子驻车制动（**Electronic Parking Brake**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**ERA**
> 外部请求数组（**External Request Array**）
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**ERAn**
> ComM 中可用的全部外部请求阵列，即 n 个设置了 ComMPncGatewayType 的 ComMChannel 会在 ComM 中产生 n 个外部请求阵列（**All External Request Arrays which are available in ComM**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Error**
> 错误。系统中的错误（软）状态，即该状态不同于若故障不存在时系统应有的状态；传播越过系统屏障即转变为失效（failure）。
>
> 来源：[Application Level Error Handling（应用层错误处理）](cp/general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

**Error Detection Rate**
> 检测到的丢失/故障字/符号/块的数量除以已发送的符号/字/块总数的比值。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ESC**
> 电子稳定控制（**Electronic Stability Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**ESP**
> 封装安全载荷（**Encapsulating Security Payload**），**IPsec** 的加密/认证协议。
>
> 来源：[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**ET**
> 以太网收发器（**Ethernet transceiver**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**Eth**
> Ethernet Controller Driver（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](cp/communication/ethernet_switch_driver/index.md)（AUTOSAR_CP_SWS_EthernetSwitchDriver）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）
{: .glossary-source}

**Ethernet Switch Port Groups**
> 以太网交换机端口组（**Ethernet Switch Port Groups**）是以太网交换机中被分组为所谓端口组的以太网交换机端口。以太网交换机端口组只与宿主 ECU（**host ECU**）相关。以太网交换机端口组按 VLAN 和 PNC 从模型中派生。宿主端口参与所有端口组。一个以太网交换机端口组可以是内部端口和外部端口的混合。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**EthIf**
> Ethernet Interface（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](cp/communication/ethernet_switch_driver/index.md)（AUTOSAR_CP_SWS_EthernetSwitchDriver）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）
{: .glossary-source}

**EthSM**
> Ethernet State Manager，以太网状态管理器（AUTOSAR BSW 模块）。
>
> 来源：[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）
{: .glossary-source}

**EthTrcv**
> Ethernet Transceiver Driver（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](cp/communication/ethernet_switch_driver/index.md)（AUTOSAR_CP_SWS_EthernetSwitchDriver）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）
{: .glossary-source}

**EthTSyn**
> **Ethernet** 的时间同步提供者模块（**Time Synchronization Provider module for Ethernet**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](cp/globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**ETSI**
> 欧洲电信标准协会（**European Telecommunications Standards Institute**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**EV**
> 电动汽车（**Electric Vehicle**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**EVCC**
> 电动汽车通信控制器（**Electric Vehicle Communication Controller**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**Event**
> 由实现一个服务实例的ECU发送给使用该服务实例的ECU的消息。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**Event Buffer**
> 临时存储已上报 **SEv** 的缓冲区。
>
> 来源：[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**Event Chain**
> 事件链——具有功能依赖关系的两个可观测事件（激励 **Stimulus** 与响应 **Response**）之间的时间关联，用作附加时序约束的主体。
>
> 来源：[Requirements on Timing Extensions（时序扩展需求）](foundation/methodology_templates/rs_timing_extensions/index.md)（AUTOSAR_FO_RS_TimingExtensions）
{: .glossary-source}

**Event combination**
> 事件组合是将多个事件合并为一个特定组合 **DTC** 的方法。它用于将不同的监视器结果适配为一个显著的、在维修站可清晰评估的故障。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event confirmation**
> 在通过故障确认计数器评估的、跨越多个周期或时间的合格事件的重复检测的情况下，诊断事件被确认。因此 **UDS** 状态位 3（ConfirmedDTC）被置位。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event debouncing**
> 去抖动是评估诊断事件是否被鉴定的特定机制（例如基于计数器）。它在潜在的信号去抖动之上工作，可以在 **SW-C** 内或 **Dem** 内进行。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event Frame**
> **IDS** 协议的主帧，包含安全事件 ID 等基本信息。
>
> 来源：[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**Event memory**
> 一个事件内存（例如主内存）由多个事件内存条目组成。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event memory entry**
> 事件内存条目是一个事件及其事件相关数据的单一存储容器。事件内存条目被动态分配给特定的事件。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event Message (SOME/IP)**
> 事件（**Event**）——由实现某服务实例的 ECU 发送给使用该服务实例的 ECU 的报文（发布/订阅）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Event qualification**
> 在通过或失败结果被置位时（**Dem** 内部或由另一个 **BSW** 模块或 **SW-C** 报告），诊断事件被鉴定。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Event related data**
> 事件相关数据是与事件一起存储在事件内存中的附加数据，例如传感器值或时间戳/里程。ISO 定义了两种类型的事件相关数据：冻结帧（快照记录）和扩展数据。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**event semantic**
> 当事件被分布时，接收到的全部事件历史都是所关注的，因此它们必须在接收方排队；因此 `SwDataDefProps` 的 `swImplPolicy` 属性将取值 `queued`（对应于带队列的事件分布）（**event semantic**，事件语义）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Event status byte**
> 按 ISO 14229-1 定义、基于事件级别的状态字节。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Eventgroup**
> 一个或多个事件的逻辑分组。一个事件组（**Eventgroup**）是服务的一部分。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**Eventhandler multicast connection**
> 描述当**SdServerService**经由已配置的Eventhandler多播端点提供多播事件时，已建立的套接字连接的使用情况的术语。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Eventhandler multicast endpoint**
> 描述按**EventHandler**为**SdServerService**预配置的多播地址和端口元组的术语。如果订阅的、具有不同端点信息的客户端数量已达到阈值，则服务器将相应的事件发送到该预配置的多播地址和端口。Eventhandler多播端点经由**SubscribeEventgroupAck**条目所引用的Multicast option通告。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**EVSE**
> 电动汽车供电设备（**Electrical Vehicle Supply Equipment**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**Excel**
> Microsoft 电子表格应用（**Excel**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**Executable**
> 应用的一部分，它要么是包含带已定义入口点的可执行代码、适合作为部署目标平台实例的文件（部署期），要么是已准备好为特定平台集成的软件代码。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Executable Entity Cluster**
> 一组可执行实体（**Executable Entity**, EE）以及这些 EE 之间的一组执行顺序约束（**Execution Order Constraint**, EOC）的引用。构建可执行实体簇（**Executable Entity Cluster**, EEC）的目的是将 EE 映射到 LET 区间和任务。多个 EEC 可以映射到同一个 LET 区间。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Execution Order Constraint**
> 定义同一 LET 区间内可执行实体（**Executable Entity**, EE）实例之间的执行顺序。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Execution Time**
> 程序实际执行所经历的时间，或更精确地说，某个执行线程处于活动状态的时间。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**execution-instance**
> 可执行实体的一个执行实例是该可执行实体在并发执行意义上的一个实例或调用上下文（**execution-instance**），见 6.2.2.3 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**EXI**
> 高效 XML 交换（**Efficient XML Interchange**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**Exit Point**
> "软件组件"（**Software Component**）中 SW-C 的某个执行实体结束的位置。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Expired Supervision Cycle**
> 一个**监督周期**，其中**存活监督**已失败其两个升级步骤（**存活计数器**失败的**期望存活指示**数量（包括容差）超过允许的失败参考周期次数）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Extended addressing format**
> 为每个N_SA和Mtype的组合分配一个唯一的CAN标识符。在CAN帧数据域的第一个数据字节中，为每个N_TA和N_TAtype的组合填入一个唯一的地址。N_PCI和N_Data填入CAN帧数据域的其余字节。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Extended data record**
> 扩展数据记录是用于存储与故障相关联的特定信息的记录。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**External client**
> 一种控制、监视和存储使用 **Dlt** 模块的 ECU 所提供的日志/跟踪消息的工具。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**External device**
> 物理外部实体；例如另一个微控制器。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**External Diagnostic Tool**
> 外部诊断工具：并非永久连接到车辆通信网络的设备，可为开发、制造或维修用途连接车辆，例如诊断测试仪或 OBD 扫描工具。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**External Graph**
> 可能涉及多于一个**被监督实体**的**图**。其配置依赖于模式。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**External Port**
> 外部端口（**External Port**）是汽车以太网交换机上用于通过以太网物理连接与其他 ECU 通信（例如 100BASE-TX、100BASE-T1）的端口。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**External Transition**
> **外部转换**是两个**检查点**之间的**转换**，其中这两个**检查点**属于不同的**被监督实体**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Application Level Error Handling（应用层错误处理）](cp/general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

## F

**FA**
> 前轴（**Front Axle**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Fail-operational**
> 系统或功能单元的一种属性。描述系统或功能单元在存在硬件或软件故障的情况下，仍能在其输出接口上继续正常运行的能力。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Fail-safe**
> 系统或功能单元的一种属性。在发生故障时，系统或功能单元转入安全状态。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Fail-silent**
> 失效静默（**Fail-silent**）是系统的一种属性，即在存在故障时不产生任何输出。在汽车领域，失效静默系统通常只在下一个层级系统提供安全状态时才被使用。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Failed Supervision Reference Cycle**
> 一个**监督参考周期**，其结束时刻检测到**存活计数器**与**期望存活指示**数量之间存在偏差（包括容差）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Failure**
> 失效。错误传播越过系统屏障、对系统环境可见后的结果：系统不再提供其规定的功能。
>
> 来源：[Application Level Error Handling（应用层错误处理）](cp/general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

**Failure counter**
> 失效计数器表示 ISO 14229-1 定义的 Trip Counter。Trip Counter 对发生故障的运行周期（驾驶循环）数进行计数。当计数器达到阈值（例如 2 个驾驶循环）时，confirmed 位从 0 变为 1。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Failure Mode**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.40
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Failure Rate**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.41
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Fallback Virtual Local Time**
> 从与导出主虚拟本地时间不同的硬件时钟导出的次级虚拟本地时间。可用于监视主虚拟本地时间，并在后者不可用时作为其本地替代。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Fan-out**
> 同一消息/指示被发送到多个目的地/接收方（**Same message/indication are sent to multiple destinations/receivers**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Fast-Mode**
> 对看门狗硬件的触发必须以较短的超时期限完成。例如，该模式可用于 **ECU** 的正常运行。例如，看门狗硬件被配置为窗口模式（触发看门狗必须发生在超时期限内的特定最小/最大边界中）且超时期限为 5 毫秒。
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](cp/safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**Fault**
> 故障。系统的瞬态或永久性变化，使其完整性偏离预期的正确完整性；被激活并传播后成为错误（error）。
>
> 来源：[Application Level Error Handling（应用层错误处理）](cp/general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

**Fault Detection**
> 监控错误并将故障状态设置为特定值的动作称为故障检测。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Fault Detection Counter**
> ISO 和 **FDC API** 中使用的 sint8 值。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Fault Reaction**
> 在 SW-C 发生失效（**Failure**）时，有一个需要执行的特定动作。该动作称为"故障反应"（**Fault Reaction**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Fault Reaction Time**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.44
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Fault Tolerance**
> 在存在一个或多个规定故障的情况下交付规定功能的能力。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Fault Tolerant Time Interval**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.45
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**FC**
> 见「CAN FC」
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**FCFS**
> 先到先服务（**First come first served**）。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**FCNT**
> **FlexRay** 周期计数器（**FlexRay Cycle Counter**）。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**FCS**
> 帧校验序列（**Frame Check Sequence**）。
>
> 来源：[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](cp/communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）
{: .glossary-source}

**FDC**
> 故障检测计数器（**Fault Detection Counter**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**FDIR**
> 故障检测、隔离与恢复（**Fault Detection, Isolation and Recovery**）。系统运行期间处理故障的过程：检测→隔离→恢复。
>
> 来源：[Application Level Error Handling（应用层错误处理）](cp/general/application_level_error_handling/index.md)（AUTOSAR_CP_EXP_ApplicationLevelErrorHandling）
{: .glossary-source}

**Feature**
> 特性（**Feature**）是系统的一个显著特征。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**FEE**
> 闪存 EEPROM 仿真（**Flash EEPROM Emulation**）。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**FF**
> 第一帧，传输协议术语。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）、[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**FID**
> 功能标识符（**Function Identifier**）：在 **FiM** 中标识一个应用程序功能及其相关禁止条件的标识符。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**Field**
> 字段表示一个状态，因此在任何时刻都有一个有效值，getter、setter和notifier作用于该值。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**FIFO**
> 先进先出缓冲区（**First In First Out buffer**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**Filter Chain**
> 施加于安全事件的一组连续过滤器（**A set of consecutive filters which is applied to Security Events**）。
>
> 来源：[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）
{: .glossary-source}

**FIM**
> 功能禁用管理器
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**FiM**
> 功能抑制管理器（**Function Inhibition Manager**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**Final Checkpoint**
> **图**的结束**检查点**。每个**图**可以有零个或多个**最终检查点**。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Find**
> 用于查找一个服务实例的消息条目。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Finding a service instance**
> 发送一条SOME/IP-SD消息以查找所需的服务实例。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**Firewall**
> 汽车以太网防火墙——监控流入/流出网络流量并授予或拒绝 **ECU** 之间或网络区域之间网络访问的网络安全设备。
>
> 来源：[Requirements on Firewall（防火墙需求）](foundation/security/rs_firewall/index.md)（AUTOSAR_FO_RS_Firewall）、[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Flag**
> 一种数据，可以取两个值之一，用于指示某个逻辑条件为真还是为假。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Flash access code**
> 由主函数（作业处理函数）调用的内部闪存驱动程序例程，用于擦除或写入闪存硬件。
>
> 来源：[AUTOSAR FLS（闪存驱动程序）](cp/memory/flash_driver/index.md)（AUTOSAR_CP_SWS_FlashDriver）
{: .glossary-source}

**Flash page**
> 一次可以编程的最小闪存量。闪存页的大小取决于闪存技术，因此取决于硬件。
>
> 来源：[AUTOSAR FLS（闪存驱动程序）](cp/memory/flash_driver/index.md)（AUTOSAR_CP_SWS_FlashDriver）
{: .glossary-source}

**Flash sector**
> 一次可以擦除的最小闪存量。闪存扇区的大小取决于闪存技术，因此取决于硬件。
>
> 来源：[AUTOSAR FLS（闪存驱动程序）](cp/memory/flash_driver/index.md)（AUTOSAR_CP_SWS_FlashDriver）
{: .glossary-source}

**FlexRay**
> 在 ISO 17458（[29]）中标准化的汽车时间触发、容错网络通信协议，它既提供在可预测时间范围内到达的确定性数据，也支持动态的事件驱动数据。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**FLM**
> 前灯管理（**Front Light Management**）
>
> 来源：[Safety Use Case（安全用例）](cp/safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**FM**
> 新鲜度管理器（**Freshness Manager**）——为每个安全通信链路向 **SecOC** 提供新鲜度的外部组件。
>
> 来源：[Secure Onboard Communication Protocol Specification（安全车载通信协议规范）](foundation/protocols/prs_secoc_protocol/index.md)（AUTOSAR_FO_PRS_SecOcProtocol）
{: .glossary-source}

**FMI**
> 失效模式指示符（**Failure Mode Indicator**，SAE J1939）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**FM**（**Freshness Manager**）
> 新鲜度管理器
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Foreground test**
> 前台测试是同步测试，不得被中断。它通过用户应用程序调用。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**FOTA**
> 固件远程升级（**Firmware Over The Air**），通过无线通信进行固件远程更新。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）、[Explanation of Firmware Over-The-Air（固件远程升级说明）](cp/memory/firmware_over_the_air/index.md)（AUTOSAR_CP_EXP_FirmwareOverTheAir）
{: .glossary-source}

**Foundation**
> Foundation 包含自适应平台与经典平台通用的制品，以确保以下二者之间的兼容性：• 经典平台与自适应平台 • 非 AUTOSAR 平台与 AUTOSAR 平台。在 AUTOSAR 中，这些通用制品的具体实现分别在自适应平台和经典平台中描述，并且可能不同。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**FR**
> **FlexRay**。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Fr**
> AUTOSAR 模块：FlexRay 驱动程序（**FlexRay Driver**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**Fr L-SDU**
> FlexRay 接口模块的 SDU。从 FlexRay 接口模块的角度看，它与 Fr N-PDU 类似（**The SDU of the FlexRay Interface module**）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**Fr N-PDU**
> FlexRay 传输层的 PDU。它包含地址信息、协议控制信息与数据（完整的 Fr N-SDU 或其一部分）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**Fr N-SDU**
> FlexRay 传输层的 SDU。在 AUTOSAR 架构中，它是来自 PDU 路由器的一组数据。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**Frame**
> 按照数据链路协议规定在传输介质上传输序列中位或位域的排列与含义的数据单元。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Frame PDU**
> 能放入 1 个帧实例的 PDU，例如在网络上传输时不需要跨多个帧分段。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Freedom from Interference**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.49
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Freeze frame**
> 冻结帧被定义为数据的记录（**DID**/**PID**）。冻结帧与 ISO 14229-1 中的 SnapShotRecords 相同。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Freshness**
> 数据新鲜度（**Freshness**）意味着数据是最近的，它确保重放攻击中被重放的报文能够被检测出来。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Freshness Value**
> 用于确保经认证的时间同步报文新鲜度的单调计数器，可以是独立报文计数器（新鲜度计数器）或时间戳值（新鲜度时间戳）。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[Secure Onboard Communication Protocol Specification（安全车载通信协议规范）](foundation/protocols/prs_secoc_protocol/index.md)（AUTOSAR_FO_PRS_SecOcProtocol）
{: .glossary-source}

**Freshness Value Manager**
> 新鲜度值管理器（**Freshness Value Manager**）。新鲜度值的提供者，**StbM** 充当 &lt;Bus&gt;TSyn 模块与 **FVM** 之间的接口。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**FrIf**
> FlexRay Interface —— FlexRay 接口。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）、[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**Frt**
> 自由运行定时器（**Free Running Timer**）。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**FrTp**
> AUTOSAR 模块：FlexRay 传输协议（**FlexRay Transport Protocol**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）、[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**FrTp_Ar**
> 接收方的定时器参数：接收方一侧 FlexRay 帧（任意 N_PDU）的传输时间（请参阅 ISO 10681-2）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**FrTp_As**
> 发送方的定时器参数：发送方一侧 FlexRay 帧（任意 N_PDU）的传输时间（请参阅 ISO 10681-2）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**FrTp_Br**
> 接收方的定时器参数：直到发送下一个流控制 N_PDU 的时间（请参阅 ISO 10681-2）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**FrTp_BS**
> 发送方的定时器参数：直到收到下一个流控制 N_PDU 的时间（请参阅 ISO 10681-2）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**FrTp_Cr**
> 接收方的定时器参数：直到收到下一个连续帧 N_PDU 的时间（请参阅 ISO 10681-2）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**FrTp_Cs**
> 发送方的定时器参数：直到发送下一个连续帧 N_PDU/末帧 N_PDU 的时间（请参阅 ISO 10681-2）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**FrTrcv**
> AUTOSAR 模块：FlexRay 收发器驱动程序（**FlexRay Transceiver Driver**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**FrTSyn**
> **FlexRay** 时间同步模块（**Time Synchronization over FlexRay** module）。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**FS**
> 流状态（**Flow Status**）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**FSC**
> 功能安全概念（**Functional Safety Concept**）
>
> 来源：[Safety Use Case（安全用例）](cp/safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**FTB**
> 失效类型字节（**Failure Type Byte**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**FTT**
> 故障容忍时间（德语「Fehlertoleranzzeit」）（**Fault Tolerance Time**）
>
> 来源：[Safety Use Case（安全用例）](cp/safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**FTTI**
> 故障容忍时间间隔（**Fault Tolerant Time Interval**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](cp/safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**Function**
> 1. 为达到期望结果而必须完成的任务、动作或活动。2. 由程序的其他部分为达到期望目的而调用的程序代码的一部分。3. 在数学中，函数是两组值之间的关联，其中一组的每个元素在另一组中有一个被指派的对应元素，于是从该组中选出的任何元素成为自变量，其关联元素成为因变量。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Function Inhibition Manager**
> 功能禁用管理器（**FIM**）代表事件的评估和分配，以及软件组件所需操作（例如禁用特定的「监控功能」）的分配。当事件状态发生变化时，DEM会通知并更新功能禁用管理器（**FIM**），以便根据分配的依赖关系停止或释放功能实体。功能实体的接口由模式管理器定义和支持。FIM不是DEM的一部分。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Functional Addressing**
> 功能寻址：特定通信网络中的一组或全部节点从一个发送节点接收消息（1:n）的诊断通信模型，也称为广播或多播。**OBD** 通信始终使用功能寻址模式。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Functional addressing**
> 在传输层中，功能寻址指的是N_TAtype参数（它是用于编码通信模型的N_TA参数[1]的扩展）取值为functional的N-SDU。这意味着该N-SDU用于1到n的通信。因此，对于CAN协议，功能寻址仅支持单帧通信。在应用方面，如果外部（或内部）测试仪不知道应响应服务请求的ECU的物理地址，或者ECU的功能是作为分布在多个ECU上的分布式服务器实现的，则外部（或内部）测试仪会使用功能寻址。使用功能寻址时，通信是从外部测试仪到一个或多个ECU的通信广播（1到n通信）。用例有（例如）广播消息，如「ECUReset」或「Communication Control」。OBD通信将始终作为功能寻址的一部分执行。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Functional Cluster**
> 按照其所指的方面分组的一组需求。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Functional Network**
> 特性（**Feature**）的已定义功能部分之间互连的一种逻辑结构。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Functional Safety Concept**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.52
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Functional Safety Requirement**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.53
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Functional Unit**
> 能够完成特定目的的软件或硬件实体，或二者的结合。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Functionality**
> 功能：涵盖系统用户可见和用户不可见的功能方面（见 [2]）。在 **FiM** 上下文中，一个功能可以由一个或多个可运行实体的全部或部分内容、以同一组许可/禁止条件构成。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**FV**
> 新鲜度值（**Freshness Value**）——用于确保安全 I-PDU 新鲜度的单调计数器或时间戳值。
>
> 来源：[Secure Onboard Communication Protocol Specification（安全车载通信协议规范）](foundation/protocols/prs_secoc_protocol/index.md)（AUTOSAR_FO_PRS_SecOcProtocol）
{: .glossary-source}

**FVL**
> 新鲜度值长度（**Freshness Value Length**）。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**FV**（**Freshness Value**）
> 新鲜度值
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

## G

**3GPP**
> 第三代合作伙伴项目（**The 3rd Generation Partnership Project**），提供制定定义 3GPP 技术的报告和规范的环境。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**5GAA**
> 5G 汽车协会（**The 5G Automotive Association**），一个开发未来出行和运输服务的全球性跨行业组织。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**GAC**
> 地理任意播（**GeoAnycast**）。
>
> 来源：[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**Gap**
> 参见 ISO 11898-4。
>
> 来源：[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**Gateway**
> 网关（**Gateway**）是经典平台 ECU 内的一种功能，它在两个通信系统之间执行帧或信号映射功能。这里的通信系统例如指 CAN 系统或 FlexRay 系统的一个通道。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Gateway ECU**
> 网关 ECU（**Gateway ECU**）是连接到两个或多个通信信道并执行网关功能的"电子控制单元"（**Electronic Control Unit**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**GBC**
> 地理广播（**GeoBroadcast**）。
>
> 来源：[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**General Denominator**
> 通用分母是一个计数器，指示车辆被操作的次数，并考虑通用条件。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Getter**
> 允许对字段进行读访问的请求/响应（**Request/Response**）调用。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**GID**
> Group identifier —— 组标识符。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**Global Supervision Status**
> 汇总所有**被监督实体****局部监督状态**的状态。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**Global Time**
> 由全局时间主节点提供的时间值，即跨网络时间同步的参考时间。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Global Time Master**
> 全局时间主节点（**Global Time Master**）。某时基的系统级源头，其时基值通过网络分发给各时基从节点。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**GM(C)**
> 顶级主节点（时钟）（**Grand Master (Clock)**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](cp/globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**GN**
> 地理网络（**GeoNetworking**）。
>
> 来源：[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）、[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**GN-SDU**
> **GeoNetworking** 服务数据单元（**GeoNetworking Service Data Unit**）。
>
> 来源：[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**Golden (Ref.) Value**
> 用于与先前计算出的测试结果值进行比较的参考值（例如校验和/签名）。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Good Case**
> 执行完成且未报告错误。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**GPT**
> 通用定时器（**General Purpose Timer**）
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**Gpt**
> 通用定时器（**General purpose Timer**）。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**GPT Predef Timer**
> **GPT Predef Timer** 是 **GPT** 驱动程序提供的自由运行递增计数器。哪些 **GPT Predef Timer** 可用取决于硬件（时钟、硬件定时器、预分频器、定时器寄存器宽度等）和配置。**GPT Predef Timer** 具有预定义的物理时间单位和范围。
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR Time Service（时间服务）](cp/system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**gPTP**
> 广义精确时间协议（**generalized Precision Time Protocol**，IEEE Std 802.1AS）。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**Graceful Degradation**
> 优雅降级（**Graceful Degradation**）：系统在存在错误的情况下继续运行，在恢复或修理期间接受功能或性能的部分降级。文献中也称为"fail soft"。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Graph**
> 控制流图（**Control Flow Graph**）。一组通过**转换**相连的**检查点**，其中至少有一个**检查点**是**初始检查点**。在该**图**的任意两个**检查点**之间都存在一条（通过**转换**的）路径。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Green-fields**
> 绿地设计（**Green-fields**）。在所关注系统中从零开始的全新设计方法，与受既有架构约束的增量设计相对。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**Group signal**
> 组信号（**Group signal**）是包含在信号组中的信号。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**GTM**
> 全局时间主节点（**Global Time Master**）。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Guard Value**
> 由对某些接口属性的哈希构成的守护信息，确保只有兼容的接口才会被连接（**Guard Value**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

## H

**HARA**
> 危害分析（**Hazard Analysis**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](cp/safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**hard error runnable**
> 由至少一个 `TransformerHardErrorEvent` 触发的可运行实体（**hard error runnable**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Hardware Abstraction Layer**
> 硬件抽象层（**Hardware Abstraction Layer**）是介于物理硬件与其软件之间的抽象层软件。它允许通过编程接口访问硬件资源。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Hardware Connection**
> 硬件连接（**HW Connection**）用于描述硬件元素（**Hardware Element**）彼此之间的连接。它定义/刻画硬件元素之间的相互关系（用于抽象建模）。硬件元素的"硬件端口"（**Hardware Port**）充当连接点。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Hardware Element**
> 硬件元素（**HW Element**）是"电子控制单元"（**Electronic Control Unit**）的主要描述元素。它提供硬件端口（**Hardware Port**）以便彼此互连。通用硬件元素规定对所有特定硬件元素有效的定义。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Hardware Interrupt**
> 由硬件事件触发的中断。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Hardware Object**
> CAN硬件对象定义为CAN硬件单元/CAN控制器的CAN RAM中的一个PDU缓冲区。硬件对象定义为CAN硬件单元CAN RAM中的L-PDU缓冲器。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）、[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**Hardware Port**
> 硬件端口（**HW port**）向"硬件元素"（**Hardware Element**）的外部暴露功能。硬件元素可以通过"硬件连接"（**Hardware Connection**）互连。它为硬件元素定义一个连接端点。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Hardware Receive Handle (HRH)**
> 硬件接收句柄（**Hardware Receive Handle**，**HRH**）由 TTCAN/CAN 驱动程序定义并提供。通常每个 **HRH** 恰好表示一个硬件对象。**HRH** 可用于优化软件过滤。
>
> 来源：[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）、[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**Hardware Transmit Handle (HTH)**
> 硬件传输句柄（**HTH**）由CAN驱动程序定义和提供。每个HTH通常只表示一个或多个硬件对象，这些硬件对象被配置为硬件传输缓冲池。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**Hardware Trigger**
> 硬件触发是**ADC**内部触发信号，用于启动ADC通道组的一次转换。**ADC**硬件触发在ADC硬件内部生成（例如：基于**ADC**定时器或触发沿信号）。触发硬件是强耦合或者直接集成在**ADC**的硬件中。当检测到硬件触发后，无需软件即可启动**ADC**通道组转换。**注意：**即使**ADC**硬件不支持硬件触发，也可以通过软件触发结合**GPT/ICU**驱动程序来实现类似的行为。（例如：在GPT定时器通知函数中，启动软件触发的**ADC**通道组的转换）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**hashedID8**
> 通过首先计算授权票证的 **SHA 256** 哈希、然后取哈希输出的最低有效 8 字节而得到的值。
>
> 来源：[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**HAZOP**
> 危害与可操作性分析（**Hazard & Operability Analysis**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](cp/safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**HDC**
> 坡道缓降控制（**Hill Decent Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Healing**
> 关闭警告指示器，包括对在一段时间/若干运行周期内报告的通过结果的处理。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Health Channel**
> 提供有关（子）系统健康状态信息的通道。它可能是应用的**全局监督状态**、任一测试例程的结果，或（子）系统报告的状态（例如电压监控、**OS** 内核、**ECU** 状态）。
>
> 来源：[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**Health Channel Supervision**
> 检查被监督软件所登记的健康指标是否在容差/限值内的一类监督。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Health Indicator**
> 健康指示器（**Health Indicators**, HI）是针对安全需求的当前系统性能的评估度量。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Health Indicator (HI)**
> **健康指标**提供针对安全要求的当前系统性能的评估度量。
>
> 来源：[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Health Indicator Interface**
> 使用标准化服务字段来通信**健康指标**的接口。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Health Monitoring**
> 对软件行为的正确时序与顺序进行的监督。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Health of Service (HoS)**
> 把服务提供方的**健康指标**作为质量参数绑定到所提供的数据上，使接收方在无需了解其背后架构的情况下决定如何使用该服务。
>
> 来源：[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）
{: .glossary-source}

**Health Status**
> 与被监督软件相关的一组状态（例如电压状态、应用状态、**RAM** 监控算法的结果）。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**Health Status Supervision**
> 检查被监督软件所登记的健康指标是否在容差/限值内。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**HHC**
> 坡道起步控制（**Hill Hold Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**HLC**
> 高层通信（**High Level Communication**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**HMI**
> 人机接口（**Human Machine Interface**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](cp/application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**hold-over**
> 主时间源（通常）暂时不可用，而另一个时间源提供（可能降级的）时间信息的场景。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Hook**
> ECU 软件中用于交换数据的干预点。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Host ECU**
> 宿主 ECU（**Host ECU**）是控制一个或多个汽车以太网交换机的 ECU（例如打开/关闭以太网交换机及其端口，读/写以太网交换机配置）。为此，宿主 ECU 通过公共控制接口（如 SPI、MDIO）连接到以太网交换机。宿主 ECU 也参与网络通信。为此，宿主 ECU 通过数据接口（如 MII）连接到特定的以太网交换机端口（宿主端口）。它发送和接收以太网帧。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Host Port**
> 宿主端口（**host port**）是汽车以太网交换机上连接"宿主 ECU"（**Host ECU**）数据接口（如 MII）的端口。宿主端口可以是内部端口或外部端口。从软件的角度看，宿主端口具有特殊角色（参见链路汇聚和端口组）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Host Software Cluster**
> 包含 BSW 主要部分（尤其是微控制器相关的下层 BSW 模块，例如 OS 和 MCAL）的唯一软件集群（**Host Software Cluster**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）、[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}

**HSM**
> 硬件安全模块（**Hardware Security Module**），专用安全 **MCU** 的内核。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）、[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**HTM**
> 硬件测试管理器（**Hardware Test Manager**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](cp/safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**HTTP**
> 超文本传输协议（**HyperText Transfer Protocol**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**HW**
> 硬件（**Hardware**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Hypervisor**
> 在一台物理机中提供并管理多台虚拟机的底层软件。它可以是独立的软件，也可以作为 OS 的功能包含在内。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

## I

**61883_IIDC**
> **IEC** 61883/**IIDC** 格式（**IEC 61883/IIDC format**），由 IEEE 1722 定义。
>
> 来源：[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**I-**
> 相对于AUTOSAR COM交互层（**Interaction Layer**）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**I-PDU**
> 交互层 **PDU**（**Interaction Layer PDU**）。在 **AUTOSAR** 中，交互层等价于通信服务层。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）、[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**I-PDU group**
> I-PDU组（**I-PDU group**）是COM模块中同方向（即发送或接收）I-PDU的任意集合。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**I-PDU ID**
> I-PDU 标识符（**I-PDU Identifier**）。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**I-PDU Multiplexer**
> **I-PDU** 复用器——一个 **AUTOSAR** 基础软件模块，规定用一个协议控制信息复用多个 **PDU** 的协议。
>
> 来源：[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**I-Signal**
> 待序列化为字节数组以进行 **E2E** 保护的条目。为了进行 **E2E** 保护，**I-Signal** 必须分配给一个 **I-Signal 组**。
>
> 来源：[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）
{: .glossary-source}

**I-Signal group**
> 要进行 **E2E** 保护的一组 **I-Signal**。**E2E** 保护在 **I-Signal** 组这一层级上定义。
>
> 来源：[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）
{: .glossary-source}

**i.e.**
> （拉丁语）id est =（英语）that is，即「也就是说」。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**IANA**
> 互联网号码分配局（**Internet Assigned Numbers Authority**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**IB**
> 内部缓冲通道（**Internally buffered channels**）：包含待传输数据的缓冲区位于 SPI 处理器/驱动程序之内。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）
{: .glossary-source}

**ICC**
> 实现一致性等级（**Implementation Conformance Class**）。AUTOSAR 对基础软件实现合规程度的分级（ICC1–ICC3）：ICC3 要求逐模块符合 AUTOSAR 规范，ICC2 允许项目定义的集群，ICC1 为专有基础软件（对外行为仍须符合 ICC3 模块规范）。
>
> 来源：[Layered Software Architecture（分层软件架构）](cp/general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）
{: .glossary-source}

**ICK**
> 完整性校验值密钥（**Integrity Check Value Key**）——从相应 **CAK** 派生、用于传输/验证完整性受保护 **MKPDU** 的密钥。
>
> 来源：[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**ICMP**
> Internet Control Message Protocol —— 互联网控制消息协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**ICMPv4**
> 互联网协议版本4的互联网控制消息协议（**Internet Control Message Protocol for Internet Protocol Version 4**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**ICMPv6**
> 互联网协议版本6的互联网控制消息协议（**Internet Control Message Protocol for Internet Protocol Version 6**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**ICU**
> 输入捕获单元（**Input Capture Unit**）
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**ICV**
> 完整性校验值（**Integrity Check Value**）。为时间同步报文提供完整性和真实性保护的校验值。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**ICVL**
> 完整性校验值长度（**Integrity Check Value Length**）。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**ID**
> 标识符（**Identifier**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**Identity and Access Management (IAM)**
> IAM（身份与访问管理）是关于管理自适应应用对自适应平台基础与服务的接口的访问权限。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Identity Information**
> 访问控制基于代表自适应应用属性的身份信息（**Identity Information**）来决策/执行。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**IDPS**
> 入侵检测与防御系统（**Intrusion Detection and Prevention System**）——针对 **IDS** 传感器检测并上报的合格安全事件采取预定义预防措施的安全控制。
>
> 来源：[Requirements on Firewall（防火墙需求）](foundation/security/rs_firewall/index.md)（AUTOSAR_FO_RS_Firewall）
{: .glossary-source}

**IDS**
> 入侵检测系统（**Intrusion Detection System**）——对车辆电子系统中安全事件的检测体系。
>
> 来源：[Requirements on Security Extract Template（安全提取模板需求）](foundation/methodology_templates/rs_security_extract_template/index.md)（AUTOSAR_FO_RS_SecurityExtractTemplate）、[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）、[Requirements on Firewall（防火墙需求）](foundation/security/rs_firewall/index.md)（AUTOSAR_FO_RS_Firewall）
{: .glossary-source}

**IDS Message**
> 由 **IdsM** 使用 **IDS** 协议发送的消息。
>
> 来源：[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**IdsM**
> 入侵检测系统管理器（**Intrusion Detection System Manager**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on Security Extract Template（安全提取模板需求）](foundation/methodology_templates/rs_security_extract_template/index.md)（AUTOSAR_FO_RS_SecurityExtractTemplate）、[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）、[Requirements on Firewall（防火墙需求）](foundation/security/rs_firewall/index.md)（AUTOSAR_FO_RS_Firewall）
{: .glossary-source}

**IdsR**
> 入侵检测系统报告器（**Intrusion Detection System Reporter**）——处理从 **IdsM** 实例接收到的合格安全事件。
>
> 来源：[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）
{: .glossary-source}

**&lt;Ie&gt;**
> 实现特定文件名扩展名（**implementation specific file name extension**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**IETF**
> 互联网工程任务组（**Internet Engineering Task Force**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**IF**
> 接口（**Interface**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**IF-PDU**
> 通过 SoAd 的 IF-API 发送/接收的 PDU。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](cp/communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**IFL**
> 浮点插值库（**Floating Point Interpolation Routines**）的模块 ID 前缀；浮点插值例程名称以 Ifl 开头。
>
> 来源：[Macro Encapsulation of Interpolation Calls（插值调用宏封装）](cp/libraries/macro_encapsulation_of_interpolation_calls/index.md)（AUTOSAR_CP_EXP_MacroEncapsulationofInterpolationCalls）、[Specification of Floating Point Interpolation Routines（浮点插值例程规范）](cp/libraries/ifl/index.md)（AUTOSAR_CP_SWS_IFLLibrary）
{: .glossary-source}

**IFX**
> 定点插值库（**Fixed Point Interpolation Routines**）的模块 ID 前缀；整数插值例程名称以 Ifx 开头。
>
> 来源：[Macro Encapsulation of Interpolation Calls（插值调用宏封装）](cp/libraries/macro_encapsulation_of_interpolation_calls/index.md)（AUTOSAR_CP_EXP_MacroEncapsulationofInterpolationCalls）、[Specification of Fixed Point Interpolation Routines（定点插值例程规范）](cp/libraries/ifx/index.md)（AUTOSAR_CP_SWS_IFXLibrary）
{: .glossary-source}

**IIDC**
> 仪器与工业数码相机（**Instrumentation and Industrial Digital Camera**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**IKE**
> 互联网密钥交换（**Internet Key Exchange**）。
>
> 来源：[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**IKEv2**
> 互联网密钥交换版本 2（**Internet Key Exchange version 2**）。
>
> 来源：[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**Implementation Conformance Class 1 (ICC1)**
> ICC1 集群提供"软件组件接口"（**Software Component Interface**）和/或"网络接口"（**Network Interface**）。ICC1 集群的软件组件接口和网络接口提供 AUTOSAR 规范在 ICC3 级别所规定的功能行为。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Implementation Conformance Class 2 (ICC2)**
> ICC2 集群将逻辑相关的 ICC3 基础软件（**BSW**）模块（2...N 个模块）组合在一起。ICC2 集群中集群特性（**Cluster Feature**）的数量是被集群的 ICC3 模块特性数量并集的子集。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Implementation Conformance Class 3 (ICC3)**
> 对于 ICC3，AUTOSAR BSW 由基础软件模块列表中定义的 BSW 模块组成，包括 RTE。ICC3 是最高级别的粒度。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**implicit read access**
> 以 `dataReadAccess` 角色聚合到某个 `VariableDataPrototype` 的 `VariableAccess`（**implicit read access**，隐式读访问）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**implicit write access**
> 以 `dataWriteAccess` 角色聚合到某个 `VariableDataPrototype` 的 `VariableAccess`（**implicit write access**，隐式写访问）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**In-Use performance ratio**
> **OBD** 系统特定监视器 m 的实际使用性能比为：IUPRm = Numeratorm / Denominatorm。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**incoherent implicit data access**
> 不属于任何相干组的隐式读访问或隐式写访问（**incoherent implicit data access**）；因此它不被任何 `RteImplicitCommunication` 容器中 `RteCoherentAccess` 参数设置为 true 的 `RteVariableReadAccessRef` 或 `RteVariableWriteAccessRef` 引用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**incoherent implicit read access**
> 不属于任何相干组的隐式读访问（**incoherent implicit read access**）；因此它不被任何 `RteImplicitCommunication` 容器中 `RteCoherentAccess` 参数设置为 true 的 `RteVariableReadAccessRef` 引用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**incoherent implicit write access**
> 不属于任何相干组的隐式写访问（**incoherent implicit write access**）；因此它不被任何 `RteImplicitCommunication` 容器中 `RteCoherentAccess` 参数设置为 true 的 `RteVariableWriteAccessRef` 引用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**IND**
> 反向邻居发现（**Inverse Neighbor Discovery**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**Independence**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.61
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Independent Failures**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.62
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Indication**
> 指示（**Indication**）是从PDU路由器到COM的异步信息，例如确认已接收到某些内容。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Inhibition Condition**
> 禁止条件：一个 **FID**、一个禁止掩码与 **Dem** 事件/组件状态之间的关系（见 FiMInhibitionConfiguration）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**Init Value**
> 初始值（**Init Value**）。AUTOSAR COM模块在启动后将I-PDU和信号设置为初始值。在被覆盖之前一直使用该值。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Initial Checkpoint**
> **图**的起始**检查点**。每个**图**可以有一个或多个**初始检查点**。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Inner Priority Inversion**
> 高优先级的**L-PDU**的传输由于在同一个发送硬件对象中存在一个未决的低优先级的L-PDU而被阻止。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）、[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**instance of an I-PDU**
> 具有一种特定布局和内容的IpduM I-PDU。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Instances of a Container**
> 同一容器PDU的多个实例。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**int**
> 整数（**Integer**）
>
> 来源：[AUTOSAR Platform Types（平台类型）](cp/general/platform_types/index.md)（SWS_PlatformTypes）
{: .glossary-source}

**Integration**
> 将系统组件逐步组装成整个系统。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Integration Code**
> 集成者需要添加到 AUTOSAR 系统中以适配未标准化功能的代码。例如 ECU 状态管理器（**EcuM**）的 Callout（**Callout**）以及各种其他基础软件模块的回调（**Callback**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Integrity**
> 数据或信息未以未授权方式被更改或销毁的特性。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Integrity Check Value**
> 用于确保未授权的消息修改能够被检测到的密码学函数的结果。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**inter-ECU communication**
> **ECU** 之间的通信（通常使用 **COM**），本文称为 **ECU** 间通信（**inter-ECU communication**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Inter-ECU-communication**
> ECU间通信（**Inter-ECU-communication**）是两个或多个ECU之间的通信，例如经由CAN网络。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**inter-partition communication**
> 同一 **ECU** 内不同分区（由不同的 **OS** application 表示）之间的通信，本文称为分区间通信（**inter-partition communication**）。它可能涉及 **IOC** 或可信函数调用等 **OS** 机制的使用。各分区可以位于不同的核上，或使用 **ECU** 的不同内存节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Interface**
> 两个功能单元（**Functional Unit**）之间的共享边界，由涉及功能、物理互连、信号交换及其他特性的各种特征（视情况而定）定义。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Intermediate PNC Coordinator**
> 中间 PNC 协调器（**Intermediate PNC Coordinator**）在 PNC 网络中位于"顶层 PNC 协调器"（**Top-level PNC Coordinator**）或另一个中间 PNC 协调器之下、PNC 叶节点（**PNC Leaf Node**）或另一个中间 PNC 协调器之上。中间 PNC 协调器将收到的 PNC 请求和自己的 PNC 请求转发给其"顶层 PNC 协调器"。中间 PNC 协调器立即处理收到的 PN 关机报文，将其转发给其下级 ECU（另一个中间 PNC 协调器或 PNC 叶节点），释放所指示的 PNC 并为这些 PNC 重置 PN 复位定时器。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Intermediate PNC coordinator**
> 一个ECU，对在至少一个通道上被被动协调的那些PNC充当中间PNC协调器。该ECU启用了PNC网关功能。如果启用了同步PNC关闭，中间PNC协调器将被被动协调的PNC的同步PNC关闭转发到主动协调的通道。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**Internal Diagnostic Tool**
> 内部诊断工具：连接到车辆通信网络的设备或 **ECU**，可用于高级事件跟踪、高级分析和维修。其行为可以与外部诊断工具相同；该术语并不意味着它作为 **AUTOSAR** 软件组件包含在每个 **ECU** 中。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Internal Graph**
> 不跨越若干**被监督实体**的**图**。其配置与模式无关，并且可以通过禁用对应的**被监督实体**而被禁用。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Internal Port**
> 内部端口（**Internal Port**）是汽车以太网交换机上用于本地通信（宿主 ECU 或级联交换机）的端口。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Internal Transition**
> **内部转换**是同一个**被监督实体**内两个**检查点**之间的**转换**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Interrupt**
> 强制处理器改变其状态的事件。这种中断导致正常的指令序列被停止。一旦发生中断，正在运行的软件实体被挂起，并调用一个"中断服务程序"（**Interrupt Service Routine**）（专用于该中断的那一个）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Interrupt Frames**
> 中断帧（**Interrupt Frame**）是处理进入/离开（用 C 编写的）中断服务程序的代码。这段代码与微控制器相关，通常用汇编语言编写。中断帧通常由 OS 生成工具生成。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Interrupt Handler**
> 对于类别 2 中断，ISR 与中断处理程序（**Interrupt Handler**）同义。对于类别 1 中断，中断处理程序是由硬件中断向量调用的函数。在这两种情况下，中断处理程序都是用户代码，通常是 BSW 模块的一部分。因此中断处理程序是用户级的一段代码。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Interrupt Service Routine**
> 在发生"中断"（**Interrupt**）时被调用的软件例程。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Interrupt Vector Table**
> 中断向量表（**Interrupt Vector Table**）是一张中断向量表，它将中断服务程序与相应的中断请求关联起来（通常通过跳转数组或类似机制）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**intra-ECU communication**
> 一个 **ECU** 之内的通信，本文称为 **ECU** 内通信（**intra-ECU communication**）。它是分区间通信和分区内通信的超集。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Intra-ECU-communication**
> ECU内通信（**Intra-ECU-communication**）是驻留在同一ECU上的软件组件之间的通信。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**intra-partition communication**
> 一个 **ECU** 的一个分区之内的通信，称为分区内通信（**intra-partition communication**）。在这种情况下，**RTE** 可以使用内部缓冲区和队列进行通信。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Intrusion Detection System**
> 负责检测、记录和报告安全事件的系统。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Invalid Flag**
> 对于 PDU 中的信号，可以在 PDU 有效载荷布局中添加一个可选的无效标志（**Invalid Flag**）。该标志指示有效载荷中其他信号的有效性。当某个信号的无效标志在 PDU 实例中被置为 true 时，该 PDU 实例有效载荷中的相应信号不包含有效的信号值。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Invalid Value of Signal**
> 对于 PDU 中的信号，可以定义一个可选的无效值（**Invalid Value**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**invalidateable**
> 可失效的 `VariableDataPrototype` 是拥有 `invalidValue` 的 `VariableDataPrototype`（**invalidateable**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Inverse transformer**
> 接收端的转换器，它反转在发送端应用的转换步骤。
>
> 来源：[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）
{: .glossary-source}

**Inversion**
> 物理值与逻辑值的反转（**Inversion**）。此属性不可见，但可以由**I/O**硬件抽象来实现，并向用户传递预期值。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**IoHwAb**
> 输入/输出硬件抽象（**Input/Output Hardware Abstraction**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**IP**
> Internet Protocol —— 互联网协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）、[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）
{: .glossary-source}

**IPC**
> 进程间通信（**Inter Process Communication**）。
>
> 来源：[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**IpduM**
> I-PDU多路复用器。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**IpduM I-PDU**
> 由两个COM I-PDU在IpduM模块中组装而成的I-PDU。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**IPsec**
> 互联网协议安全（**Internet Protocol Security**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**IPv4**
> Internet Protocol version 4 —— 互联网协议第 4 版。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**IPv6**
> Internet Protocol version 6 —— 互联网协议第 6 版。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**IRA**
> 内部请求阵列（**Internal Request Array**）。这是一个位向量，包含每个通道聚合后的内部 PNC 请求。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**IRQ**
> 中断请求（**Interrupt Request**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Irrelevant frame**
> 从 LIN 从节点的角度来看，LIN 总线上存在 3 种不同方向的帧：从节点发送的响应、从节点接收的响应和从节点忽略的响应（即主节点与另一个从节点之间或另外两个从节点之间的通信）。这些被忽略的帧在本规范中被称为无关帧（**irrelevant frame**）。这在 ISO 17987 规范中没有明确描述。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**ISR**
> 中断服务程序（**Interrupt Service Routine**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](cp/memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping）、[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](cp/communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）、[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**ISR body**
> 使用宏 `ISR` 定义的任务函数（**ISR body**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**ISR2**
> 类别 2 的中断服务例程（**ISR2**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**ITS**
> 智能交通系统（**Intelligent Transport System**）。
>
> 来源：[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**ITS-G5**
> 基于 **IEEE** 802.11p 的无线通信技术。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**ITS-S**
> ITS 站（**ITS-Station**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**IUMPR**
> 在使用中的监控性能比（**In-Use-Monitor Performance Ratio**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**IVI**
> 基础设施到车辆信息（**Infrastructure to Vehicle Information**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**IVIM**
> 基础设施到车辆信息消息（**Infrastructure to Vehicle Information Message**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

## J

**J1939Dcm**
> SAE J1939 诊断通信管理器（**SAE J1939 Diagnostic Communication Manager**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Jitter**
> 最长延迟和最短延迟之间的差异（例如，最坏情况执行时间 - 最佳情况执行时间）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**JLEF**
> （**TTCAN**）作业列表执行函数（**Job List Execution Function**）。
>
> 来源：[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**Job**
> 作业：一个已配置的 **CsmJob**，它引用一个密钥、一个加密原语和一个参考通道。
>
> 来源：[Utilization of Crypto Services（加密服务使用指南）](cp/crypto/utilization_of_crypto_services/index.md)（AUTOSAR_CP_EXP_UtilizationOfCryptoServices）、[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Job List**
> **TTCAN** 作业列表是按各自执行开始时间排序的（可能不同的）通信作业的列表。
>
> 来源：[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**Job Request**
> 作业请求（**Job Request**）是指上层模块对地址区的存储访问请求。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

## K

**KAF**
> **DENM** 保活转发（**DENM Keep Alive Forwarding**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**KaY**
> **MAC** 安全密钥协商实体（**MAC Security Key Agreement Entity**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**KDF**
> 密钥派生函数（**Key Derivation Function**）——**MKA** 使用、基于 **CMAC** 模式 **AES** 密码的密钥派生函数。
>
> 来源：[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**KEK**
> 密钥加密密钥（**Key Encrypting Key**）——从相应 **CAK** 派生、用于加密/解密安全关联密钥（**SAK**）的密钥。
>
> 来源：[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**Key**
> 密钥：密钥可以被 **Csm** 中的作业引用；在加密驱动程序中，每个密钥引用一种特定的密钥类型。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Key Element**
> 密钥元素：用于存储数据（例如 **AES** 加密所需的密钥材料或 **IV**），也可用于配置密钥管理功能的行为；不同密钥的密钥元素拥有不同的存储区域（**NV** 区域和 **RAM** 区域）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Key Type**
> 密钥类型：由对密钥元素的引用组成，通常由加密驱动程序的供应商预先配置。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

## L

**L-**
> 相对于CAN接口模块，它等同于逻辑链路控制（**Logical Link Control**，数据链路层的上半部分——下半部分称为媒体访问控制）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**L-PDU**
> 数据链路层 **PDU**（**Data Link Layer PDU**）。在 **AUTOSAR** 中，数据链路层等价于通信硬件抽象和微控制器抽象层。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）、[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）、[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**L-PDU Handle**
> L-PDU句柄被定义并放置在**CanIf**模块层内。通常每个句柄代表一个L-PDU，它是一个包含Tx/Rx处理信息的常量结构。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**L-PDU ID**
> L-PDU 标识符（**L-PDU Identifier**）。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L-SDU**
> 链路层服务数据单元（**Data link layer service data unit**）。一个 L-SDU 由数据（缓冲区）、长度、L-SDU ID 以及可能经由元数据传输的 L-PDU 特定信息组成。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L-SDU ID**
> L-SDU 标识符（**L-SDU identifier**）。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L-SDU Router**
> 在模块之间传输 L-SDU 的模块。L-SDU Router 模块可用于内部路由目的。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**L1**
> 第一级存储器（**1st level memory**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**L2**
> 第二级存储器（**2nd level memory**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**L2ID**
> 层 2 ID（**Layer 2 ID**），相当于以太网的「消息认证码」。
>
> 来源：[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**LampStatus**
> 灯状态（**Lamp Status**）包含激活错误的严重程度信息，作为诊断消息的一部分传输
>
> 来源：[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**Large I-PDU**
> 大I-PDU（**Large I-PDU**）是太大而无法放入底层通信协议单个L-PDU的I-Signal-I-PDU。大I-PDU由COM像其他I-PDU一样处理，但经由TP API发送/接收。请注意，如果大I-PDU只包含一个信号，或者信号可以由RTE（反）序列化，**LargeDataCOM**可以更高效地处理它们。但如果信号必须被单独处理或必须被路由，则大I-PDU必须由COM处理。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Large Signal**
> 大信号（**Large Signal**）是太大而无法放入底层通信协议单个L-PDU的信号。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**LB**
> 近光功能（德语「Abblendlicht」）（**Low Beam**）
>
> 来源：[Safety Use Case（安全用例）](cp/safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**LDF**
> LIN 描述文件（**LIN Description File**）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**LDM**
> 局部动态地图（**Local Dynamic Map**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**LED**
> 发光二极管（**Light Emitting Diode**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](cp/application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**LET**
> 逻辑执行时间——通过抽象物理执行来确保稳定软件行为的概念（**Logical Execution Time**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](cp/system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**Life Cycle**
> 模型元素在其生存期内的发展/演化阶段历程。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**LIN**
> 局部互联网络（**Local Interconnect Network**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**LIN Bus Idle**
> 总线空闲（**Bus Idle**）定义为 LIN 总线上隐性位与显性位值之间没有跳变的状态。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**LIN TP**（**LinTp**）
> LIN 传输协议（**LIN Transport Protocol**）（LIN 接口的一部分）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**LinIf**
> LIN 接口（**LIN Interface**）
>
> 来源：[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**Link State Accumulation**
> 通过汇总端口组中每个端口的链路状态来累积某个交换机端口组的链路状态。汇总链路状态的规则在以太网接口（**Ethernet Interface**）中规定。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Link Time Configuration**
> SW 模块的配置在链接期之前完成。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**LinkTime variability**
> 由最迟绑定时间为 `LinkTime` 的 `VariationPoint` 或 `AttributeValueVariationPoint` 定义的可变性（**LinkTime variability**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**LinSM**
> LIN 状态管理器（**LIN State Manager**）
>
> 来源：[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**LinTrcv**
> LIN 收发器驱动程序（**LIN Transceiver Driver**）。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**LKA**
> 车道保持辅助（**Lane Keep Assist**）。
>
> 来源：[Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](cp/application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC）
{: .glossary-source}

**&lt;Lo&gt;**
> 下层通信接口模块。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**Local Health Monitor**
> 收集其所在平台的健康信息的组件。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Local Instance of the Global Time**
> 在从全局时间主节点接收到两个时间值采样之间，借助虚拟本地时间或受控硬件时钟对时间当前值的本地外推。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Local Software Cluster Communication Plug-In**
> 本地软件集群通信插件（**Local Software Cluster Communication Plug-In**）是处理软件集群内部本地通信的 **RTE** 实现插件；如果相应的通信图存在 `DataMapping`，则也包括转换器的处理。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Local Supervision Status**
> 表示单个**被监督实体**当前存活监督结果的状态。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**Log and Trace**
> 日志与跟踪（**Log and Trace**）为应用提供接口，用于将日志和跟踪信息转发到通信总线、控制台或文件系统。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Log and trace level**
> 日志级别为日志消息的严重程度定义了一种分类。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Log and trace message**
> 包含描述软件中一个日志和跟踪事件的所有数据和选项的消息；由头部和载荷组成。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Log Channel**
> 用于传输 **Dlt** 消息的物理通信总线。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Log Message**
> 包含诸如状态变化或值变化之类调试信息的消息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Logging**
> 日志记录（**Logging**）是在运行期间收集系统中任意的、不必然相关的事件信息的活动。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Logical Execution Time**
> 是一个固定的时间区间。输入数据在该区间的开始处读取，输出数据在该区间的结束处写出。数据的处理被限制在该时间区间内。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Logical Supervision**
> 一种对软件的在线监督，用于检查软件（**被监督实体**或一组**被监督实体**）是否按程序员（即已开发的代码）定义的顺序执行。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）、[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**&lt;LoTp&gt;**
> 下层传输协议模块。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**Lower Layer Modules（Lo）**
> 位于 L-SDU Router 之下的模块。该层包括以太网通信接口模块。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**LPDU**
> Data Link Layer PDU —— 数据链路层 PDU。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**LPdu**
> 数据链路层协议数据单元（**Datalink layer Protocol Datagram Unit**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**LS**
> 灯光开关（**Light Switch**）
>
> 来源：[Safety Use Case（安全用例）](cp/safety/safety_use_case/index.md)（AUTOSAR_CP_EXP_SafetyUseCase）
{: .glossary-source}

**LTC**
> 长期证书（**Long Term Certificate**）。
>
> 来源：[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**LTE**
> 长期演进（**Long Term Evolution**）。
>
> 来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）
{: .glossary-source}

**LTE-PC5**
> 通过蜂窝调制解调器的侧行链路（**Sidelink**）通信（蜂窝调制解调器之间的直接通信，无需基站介入）。
>
> 来源：[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**LTE-Uu**
> 由基站控制的蜂窝通信。
>
> 来源：[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**LTE-V2X**
> 基于长期演进的车联网技术（**Long Term Evolution based Vehicle to Everything**）。
>
> 来源：[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）
{: .glossary-source}

## M

**&lt;MA&gt;**
> 大写模块缩写（**Capitalized module abbreviation**），即完全以大写形式书写的模块缩写 &lt;Ma&gt;
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**&lt;Ma&gt;**
> 模块缩写（**Module abbreviation**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**MAC**
> 报文认证码（**Message Authentication Code**）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）、[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）、[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）、[Secure Onboard Communication Protocol Specification（安全车载通信协议规范）](foundation/protocols/prs_secoc_protocol/index.md)（AUTOSAR_FO_PRS_SecOcProtocol）
{: .glossary-source}

**Machine**
> MCU、虚拟机或分区；本身未被标准化，参见 AUTOSAR 术语表。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Macrotick**
> 宏节拍——FlexRay 集群全局同步时间的最小单位。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**MACsec**
> 介质访问控制安全（**Media Access Control Security**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**Main Time Triple**
> 参考时间三元组 [TL_Main, TV_Main, TV_Fallback]，在主时间元组基础上增加了第三个成员——在主时间元组被更新的时刻采样的备用虚拟本地时间。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Main Time Tuple**
> 参考时间元组 [TL_Main, TV_Main]，用于在不支持受控硬件时钟的情况下基于主虚拟本地时间计算全局时间的本地实例。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**MAKW**
> 内存分配关键字（**Memory Allocation Key Word**）
>
> 来源：[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](cp/memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping）
{: .glossary-source}

**Managed channel**
> 由 ECUC 参数 ComMManageReference 从另一个通道独占引用的 ComM 通道（**A ComM channel that is referenced exclusively from one other channel by ECUC parameter ComMManageReference**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Managing channel**
> 通过 ECUC 参数 ComMManageReference 引用 1..n 个其他通道的 ComM 通道（**A ComM channel that references 1..n other channels by ECUC parameter ComMManageReference**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Manifest**
> 清单（**Manifest**）表示为支持 AUTOSAR 自适应平台产品的配置而创建的一段 AUTOSAR 模型描述，它被上传到 AUTOSAR 自适应平台产品，可能与其他包含清单所适用可执行代码的制品（如二进制文件）一起上传。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**MAPEM**
> **MAP** 扩展消息（**MAP Extended Message**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**Mappable Element**
> 可映射元素（**Mappable Element**）是 MCAL 模块的一部分，可以通过该模块基础软件模块描述中的引用参数将其分配到某个分区。可映射元素允许以形式化方式描述 MCAL 模块在分区（以及核）上的可用性/分布方式。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Mapping**
> 映射（**Mapping**）指定逻辑视图中的元素到物理视图中的元素的分布。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Master**
> 主。分布式 BSW 模块中协调卫星请求、并可过滤或监控进入的卫星请求的部分。
>
> 来源：[BSW Distribution Guide（BSW 分布指南）](cp/general/bsw_distribution_guide/index.md)（AUTOSAR_CP_EXP_BSWDistributionGuide）
{: .glossary-source}

**Master ECU**
> 与 **Primary ECU** 一样，**Master ECU** 在其事件内存中存储"自己的"以及相关的从属/辅助 **ECU** 的"报告的错误"。除此之外，**Master** 必须履行特殊的 **Master** 任务，如 **MIL Master** 或提供"通用分子"信息。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Master Switch**
> 主交换机（**Master Switch**）是宿主端口所在的以太网交换机。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Maximum frame length**
> 最大帧长度是 ISO 17987-3 [6] 中定义的 **T_FRAME_MAX**（即标称帧长度加上 40%）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**MCAL**
> 微机抽象层（**Microcomputer Abstraction Layer**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）、[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**MCAL Signal**
> MCAL 信号（**MCAL Signal**）是"处理后的信号"（**Conditioned Signal**）的软件表示。它由微控制器抽象层（**MCAL**）提供，并由 ECU 抽象进一步处理。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**MCD**
> Measurement Calibration and Diagnostics —— 测量、标定与诊断。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**MCG**
> 模块配置生成器（**Module Configuration Generator**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）、[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](cp/communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）
{: .glossary-source}

**MCNT**
> Message Counter —— 消息计数器。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MCU**
> 微控制器单元（**Microcontroller Unit**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR MCU Driver（微控制器单元驱动）](cp/mcal/mcu_driver/index.md)（SWS_MCUDriver）、[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**MDIO**
> 管理数据输入/输出（**Management Data Input/Output**）。
>
> 来源：[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](cp/communication/ethernet_switch_driver/index.md)（AUTOSAR_CP_SWS_EthernetSwitchDriver）
{: .glossary-source}

**MDR**
> 最大数据速率（**Maximum Data Rate**）。
>
> 来源：[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**MDT**
> 最小延迟定时器（**Minimum Delay Timer**）的详细描述见[3]。另见第6.3.5.5节。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Memory Device**
> 存储设备（**Memory Device**）是指一组存储 **Bank** 的组合。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Message**
> [3]始终使用同义词消息（**message**）。在AUTOSAR中，message被signal替换，但含义相同。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Message authentication**（消息认证）
> 消息认证是与数据来源认证类似使用的术语。它提供关于原始消息来源的数据来源认证（以及数据完整性，但不提供唯一性）。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Message ID**
> 用于表征消息自身所传输信息的 ID；唯一地标识一种日志或跟踪消息，并在开发或配置时静态固定。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Meta-class**
> 元类（**Meta-class**）。AUTOSAR 元模型（M2 层）中定义模型元素结构与语义的类，例如 `System`、`CompositionSwComponentType`。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**Meta-data**
> 元数据（**Meta-data**）是关于数据的数据。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Meta-model**
> 元模型（**Meta-model**）。定义建模语言本身的模型层（M2）；抽象平台复用 AUTOSAR 元模型，通过平台特定限制约束其工件。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**MetaData**
> 与PDU一起传输的元数据，由一组元数据项组成
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）
{: .glossary-source}

**Metadata**
> 元数据（**Metadata**）。对于某些I-PDU（如J1939 I-PDU），有效载荷会扩展以包含附加的元数据，例如CAN-ID。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**MetaDataItem**
> 具有定义的类型和大小的单个MetaData项
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**Method**
> 被调用/调用的方法、过程、函数或子例程。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**MFL**
> 浮点数学库（**Mathematical Floating point Library**），**AUTOSAR** 库中提供浮点算术例程的模块简称 Mfl。
>
> 来源：[Specification of Floating Point Math Routines（浮点数学例程规范）](cp/libraries/mfl/index.md)（AUTOSAR_CP_SWS_MFLLibrary）
{: .glossary-source}

**Mfx**
> 定点数学库（**Math - Fixed Point library**）。
>
> 来源：[Specification of Fixed Point Math Routines（定点数学例程规范）](cp/libraries/mfx/index.md)（AUTOSAR_CP_SWS_MFXLibrary）
{: .glossary-source}

**Microcontroller**
> 在单个芯片（包括存储器）中集成计算与通信资源以及外围电路的硬件元素。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Microcontroller Abstraction Layer**
> 包含各类驱动程序的软件层，通过已定义的"应用编程接口"（**Application Programming Interface**）实现对微控制器片上外设和片下存储器映射外设的访问。任务：使较高的软件层次独立于微控制器。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**MII**
> 媒体独立接口（**Media Independent Interface**，由以太网控制器提供的用于访问以太网收发器的标准化接口，参见 IEEE 802.3-2006）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](cp/communication/ethernet_switch_driver/index.md)（AUTOSAR_CP_SWS_EthernetSwitchDriver）
{: .glossary-source}

**MIL**
> 故障指示灯（**Malfunction Indication Light**）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**&lt;MIP&gt;**
> 大写模块实现前缀（**Capitalized module implementation prefix**），即完全以大写形式书写的模块实现前缀 &lt;Mip&gt;
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**&lt;Mip&gt;**
> 模块实现前缀（**Module implementation prefix**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**MISO**
> Master Input Slave Output（主入从出）。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**MISRA**
> 汽车工业软件可靠性协会（**Motor Industry Software Reliability Association**）。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**Mistake**
> 人为错误。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Mixed addressing format**
> 为每个N_SA、N_TA、N_TAtype的组合分配一个唯一的CAN标识符。N_AE放置在CAN帧数据域的第一个数据字节中。N_PCI和N_Data放置在CAN帧数据域的其余字节中。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**MKA**
> **MACsec** 密钥协商协议（**MACsec Key Agreement protocol**，IEEE Std 802.1X）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**MKPDU**
> **MACsec** 密钥协商协议数据单元（**MACsec Key Agreement Protocol Data Unit**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）
{: .glossary-source}

**Modality**
> 模态——到用户的输出通道的类型，例如音频或视频输出（**Modality**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](cp/application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**Mode**
> 模式是车辆中运行的各个状态机的特定状态集合，这些状态与某个特定实体相关，例如 **SW-C**、**BSW** 模块、应用或整个车辆。在其生命周期内，一个实体在一组互斥的模式之间切换。这些切换由环境数据触发，例如信号接收、操作调用。在**看门狗管理器**的上下文中，一个模式由一组配置选项定义。被监督的**被监督实体**集合可以随模式而变化。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**&lt;module&gt;**
> 任何类型的软件模块 <...>.
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**Mode Communication Graph**
> 相互连接的各 `PortPrototype` 中实例化的 `ModeDeclarationGroupPrototype` 上的所有 `ModeAccessPoint` 和 `ModeSwitchPoint` 之和，或相互连接的各 `BswModuleDescription` 中对 `ModeDeclarationGroupPrototype` 的所有 `managedModeGroup` 和 `accessedModeGroup` 之和（**Mode Communication Graph**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**mode disabling**
> 当某个模式禁用（**mode disabling**）活动时，**RTE** 和基础软件调度器禁用模式禁用依赖的可执行实体的激活。模式禁用在模式禁用依赖所引用的模式期间、以及进入和离开该模式的转换期间是活动的。另见 6.2.4.1 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**mode disabling dependency**
> 启动 `RunnableEntity`（或 `BswSchedulableEntity`）的 `RTEEvent`（或 `BswEvent`）可以包含一个引用某个 `ModeDeclaration` 的 `disabledMode`（或 `disabledInMode`）关联。本规范称该关联为模式禁用依赖（**mode disabling dependency**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**mode disabling dependent ExecutableEntity**
> 由带有模式禁用依赖的 `RTEEvent`（或 `BswEvent`）触发的 `RunnableEntity` 或 `BswSchedulableEntity`（**mode disabling dependent ExecutableEntity**）。当相应的模式禁用活动时，**RTE** 和基础软件调度器阻止这些 `RunnableEntity` 或 `BswSchedulableEntity` 被该 `RTEEvent`/`BswEvent` 激活。另见 6.2.4.1 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**mode machine instance**
> 模式机或 `ModeDeclarationGroup` 的实例由模式管理者的 `ModeDeclarationGroupPrototype` 定义（**mode machine instance**）。由于模式切换不是瞬时完成的，**RTE** 或基础软件调度器必须维护自己的状态。对每个模式管理者的 `ModeDeclarationGroupPrototype`，**RTE** 或基础软件调度器有一个状态机，该状态机称为模式机实例。对同一模式管理者 `ModeDeclarationGroupPrototype` 的所有模式使用者，**RTE** 和基础软件调度器使用同一个模式机实例。另见 6.2.4.2 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**mode manager**
> 进入和离开模式由模式管理者（**mode manager**）发起。模式管理者要么是提供一个由 `ModeSwitchInterface` 定义类型的 p-port 的软件组件，要么是在其 `BswModuleDescription` 中以 `providedModeGroup` 角色定义了 `ModeDeclarationGroupPrototype` 的 **BSW** 模块。另见 6.2.4.2 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**ModeSwitchAck ExecutableEntity**
> 由连接到模式管理者 `ModeDeclarationGroupPrototype` 的 `ModeSwitchedAckEvent`（或 `BswModeSwitchedAckEvent`）触发的 `RunnableEntity` 或 `BswSchedulableEntity`（**ModeSwitchAck ExecutableEntity**）。另见 6.2.4.1 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**mode switch notification**
> 使用 `ModeSwitchInterface` 或 `providedModeGroup` 与 `requiredModeGroup` `ModeDeclarationGroupPrototype`、从模式管理者到模式使用者的模式切换通信（**mode switch notification**，模式切换通知）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**mode switch port**
> 用于接收（或发送）模式切换通知的端口（**mode switch port**，模式切换端口）；为此，模式切换端口由 `ModeSwitchInterface` 定义类型。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**mode user**
> 依赖模式的 **AUTOSAR SW-C** 或 **AUTOSAR** 基础软件模块称为模式使用者（**mode user**）。该依赖可以经由 `SwcModeSwitchEvent`/`BswModeSwitchEvent`、针对提供/需求模式切换端口的 `ModeAccessPoint`、或针对 `providedModeGroup`/`requiredModeGroup` `ModeDeclarationGroupPrototype` 的 `accessedModeGroup` 产生。另见 6.2.4.1 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Module abbreviation**
> 模块缩写（**Module abbreviation**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**Module implementation prefix**
> 模块实现前缀（**Module implementation prefix**），用于构成 BSW 模块实现的工作成果中使用的各种标识符（例如 API 名称、参数名称、符号和文件名），主要由模块缩写构成，必要时加上额外的厂商特定信息
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**Monitor**
> 诊断监视器是确定组件是否正常运行的例程实体。也可以使用术语"诊断功能"。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Monitoring function**
> 监控功能：软件组件的一部分；用于监控并最终检测某个传感器、执行器故障或进行合理性检查的机制；报告来自 **SW-C** 内部处理或来自其他块返回值进一步处理的事件状态。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**MOSI**
> Master Output Slave Input（主出从入）。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**MOST**
> 面向媒体的系统传输（**Media Orientated System Transport**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**MPDU**
> **MACsec** 协议数据单元（**MACsec Protocol Data Unit**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）
{: .glossary-source}

**MPU**
> 内存保护单元（**Memory Protection Unit**）
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**MRF**
> 主节点请求帧（**Master Request Frame**）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**MS**
> 里程碑（**Milestone**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**MSBF**
> Most Significant Byte First —— 最高有效字节在前。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSBI**
> Message Bus Info —— 消息总线信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSCI**
> Message Control Info —— 消息控制信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSLI**
> Message Log Info —— 消息日志信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSTI**
> Message Trace Info —— 消息跟踪信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSTP（Message Type）**
> Message Type —— 消息类型。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**MSTP（Microcontroller Specific Test Package）**
> 微控制器特定测试包（**Microcontroller Specific Test Package**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](cp/safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）、[Hardware Test Management startup shutdown（硬件测试管理启动和关闭）](cp/system_services/hw_test_manager/index.md)（AUTOSAR_CP_SWS_HWTestManager）
{: .glossary-source}

**MTU**
> 最大传输单元（**Maximum Transmission Unit**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）
{: .glossary-source}

**Mtype**
> 消息类型（可能取值：诊断、远程诊断）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Multicast event**
> 由承载**SdServerService**的ECU发送到多播端点的事件。该多播端点可以由SdServerService（见「Eventhandler multicast endpoint」）和SdClientService（见「Consumed Eventgroup multicast endpoint」）提供。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Multicast Option**
> 多播选项（**Multicast Options**）用于通告一个多播地址和端口的元组。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Multimedia Stream**
> 随时间变化的一致的数字数据序列，适合作为那些将这些数据转换为对人类连续可见或可听印象的设备的输入。通过物理链路传输时，多媒体流数据通常以与数据汇消耗它们相同的速率（由数据源）产生。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Multiple connection**
> CAN传输层应同时管理多个传输协议通信会话。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**multiplexed I-PDU**
> 见IpduM I-PDU。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Multiplexed PDU**
> 多路复用 PDU（**Multiplexed PDU**）是具有可配置数量的不同有效载荷布局的 PDU。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

## N

**N-**
> 相对于CAN传输层，它等同于OSI网络层（**Network Layer**）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N-PDU**
> 网络层 **PDU**（**Network Layer PDU**）。在 **AUTOSAR** 中，网络层等价于传输协议。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）、[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**n/a**
> 不适用（**Not applicable**）。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**N_AE**
> 网络地址扩展（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_AI**
> 网络地址信息（见ISO 15765-2）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_Ar**
> 接收方CAN帧（任意N-PDU）的传输时间（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_As**
> 发送端发送 LIN 帧（任何 N-PDU）的时间（见 ISO 17987-2 [5]）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_Br**
> 直到发送下一个流控N-PDU的时间（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_Bs**
> 直到接收到下一个流控N-PDU的时间（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_Cr**
> 直到接收到下一个连续帧 N-PDU 的时间（见 ISO 17987-2 [5]）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_Cs**
> 直到传输下一个连续帧 N-PDU 的时间（见 ISO 17987-2 [5]）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_Data**
> 传输层的数据信息
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_PCI**
> 传输层的协议控制信息
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_SA**
> 网络源地址（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_TA**
> 网络目标地址（见ISO 15765-2 [1]）。在扩展寻址的情况下，它可能已包含N_TAtype（物理/功能）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**N_TAtype**
> 网络目标地址类型（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**NACK**
> 控制字节置 1 的 **J1939** **Acknowledgement PG**（**ACKM**）。
>
> 来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**NAD**
> 节点地址（**Node Address**）。LIN 中的每个从节点都必须具有唯一的 NAD。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**NAME**
> 节点的 64 位 **NAME**。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）
{: .glossary-source}

**NC**
> 节点配置（**Node Configuration**）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**NDP**
> 邻居发现协议（**Neighbor Discovery Protocol**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**neighborRateRatio**
> **IEEE 802.1AS** 定义的邻速率比。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](cp/globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**Network**
> AUTOSAR ECU/机器之间的通信基础设施。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**network**
> 连接到同一总线的所有NM节点/ECU的实体。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**Network Interface**
> 网络接口（**Network Interface**）是"基础软件"（**Basic Software**）向其所连接的网络提供的全部接口的总和。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Network Mode**
> 网络模式——网络被请求或处于活动状态的 **NM** 状态。
>
> 来源：[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**NIT**
> FlexRay 网络空闲时间（**FlexRay Network Idle Time**）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**NM**
> 网络管理（**Network Management**）
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）、[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**Nm**
> 通用网络管理接口模块，本规范全文中用它作为该模块的缩写。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**NM Coordination Cluster**
> 协调关机的一组离散 NM 信道（**NM Channel**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**NM Coordinator**
> 通用 NM 接口（**Generic NM Interface**）的一种功能，允许多个 NM 信道之间协调网络休眠。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**NM Message**
> 最抽象的术语，指在NM算法的方法论中传输的任何单个信息项。
>
> 来源：[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

**NM Packet**
> 指一个以太网帧，除了由NM在有效载荷部分传输的数据（**PDU**）之外，还包含一个**IP**和一个**UDP**报头。
>
> 来源：[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

**NM PDU**
> 指在数据包中传输的有效载荷。它包含**NM**用户数据以及控制位向量和源节点标识符。
>
> 来源：[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

**NM User Data**
> 附在总线上发送的每条NM消息上的补充性应用特定数据。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**NM-Channel**
> 与NM集群相关联的逻辑通道。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**NM-Cluster**
> 使用NM算法协调的NM节点的集合。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**NM-Coordinator**
> Nm的一项功能，它允许对多个NM通道的网络睡眠进行协调。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**NM-Message**
> 为NM算法的目的而交换的信息包。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**NM-Timeout**
> NM算法中引发向总线睡眠模式（**Bus-Sleep Mode**）转换的超时。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**NOAR**
> Number of Arguments —— 参数数量。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Node**
> **J1939** 节点 — 可以连接到多于一个通道。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）
{: .glossary-source}

**Node Identifier**
> 为NM算法的目的而交换的节点地址信息。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**Node Identifier List**
> NM算法所识别的节点标识符列表。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**NodeChannel**
> 节点与一个通道的连接。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）
{: .glossary-source}

**Non-repudiation**
> 信息安全中使用的一种概念，确保信息发送方获得送达证明，接收方获得发送方身份证明，从而使双方事后都不能否认处理过该信息。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**nop**
> 无操作（**No Operation**）。
>
> 来源：[AUTOSAR Time Service（时间服务）](cp/system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**NOP, nop**
> 空操作（**Null Operation**）
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**Normal addressing format**
> 为每个N_SA、N_TA、N_TAtype和Mtype的组合分配一个唯一的CAN标识符。N_PCI和N_Data填入CAN帧数据域。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Notification**
> 通知（**Notification**）是AUTOSAR COM模块向其用户（如**RTE**、**SwCluC**）提供的信息，例如新数据可用或发生错误。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Notification Event**
> 字段的通知器（**Notifier**）发出的事件消息（**An event message of the notifier of a field**）。
>
> 来源：[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**Notification Time Base Customer**
> 一种时基客户，当时基状态改变或时基值到达客户先前设置的给定值时，由同步时基管理器通知。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Notifier**
> 在字段的值发生变化时发送带有新值的事件消息。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）
{: .glossary-source}

**NRC**
> 负响应码（**Negative Response Code**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**NTCAS**
> 全国汽车标准化技术委员会（**National Technical Committee of Auto Standardization**）。
>
> 来源：[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**NTSCF**
> 非时间敏感控制格式（**None Time Sensitive Control Format**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**Numerator**
> 特定监视器 m 的分子（Numeratorm）是一个计数器，指示车辆被操作的次数，使得检测该特定监视器故障所需的所有监控条件都已被满足。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**NV**
> 非易失性（**Non volatile**）。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**NV Block**
> 「NV 块」是「基本存储对象」。它代表驻留在 **NV 内存** 中的「NVRAM 块」的一部分。「NV 块」是「NVRAM 块」的强制性部分。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**NV Block Header**
> 如果启用「静态块 ID」机制，则 **NV 块**中包含的附加信息。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**NV data**
> 「NV 数据」是指要存储在非易失性存储器中的数据。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**NvBlockSwComponent**
> `NvBlockSwComponent` 是由 `NvBlockSwComponentType` 定义类型的 `SwComponentPrototype`。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**NVH**
> 噪声、振动、平顺性（**Noise, Vibration, Harshness**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**NVM**
> 非易失性存储器（**Non-Volatile Memory**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）
{: .glossary-source}

**NVRAM**
> 非易失性 RAM（**Non-Volatile RAM**）
>
> 来源：[AUTOSAR Memory Mapping（AUTOSAR 内存映射）](cp/memory/memory_mapping/index.md)（AUTOSAR_CP_SWS_MemoryMapping）
{: .glossary-source}

**NVRAM Block**
> 「NVRAM 块」是管理和存储 NV 数据块所需的整个结构。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

## O

**OA TC10**
> Open Alliance TC10（参见 OPEN Sleep/Wake-up Specification for Automotive Ethernet）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](cp/communication/ethernet_switch_driver/index.md)（AUTOSAR_CP_SWS_EthernetSwitchDriver）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**OBD**
> 车载诊断（**On-board Diagnostics**）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**OBD ECUs**
> 车辆中可以有 3 种不同类型的 **OBD ECU**：**Master ECU**（每车一个）、**Primary ECU**（每车多个）、从属/辅助 **ECU**（每车多个）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**OBD Scan tool**
> 参见外部诊断工具（**External Diagnostic Tool**）的定义。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**OBD Service**
> 这是指 **ISO 15031-5** 中定义的 **OBD** 服务。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**OBD UDS DTC separation**
> 该特性为基于 SAE J1979-2 的 **UDS** 通信报告与其它 J1979-2 **UDS** 通信不同的 3 字节 **DTC** 编号。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**OBDII**
> 排放相关车载诊断（**Emission-related On-board Diagnostics**）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**OC**
> 发生计数（**Occurrence Count**，SAE J1939）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**OD**
> 乘员检测（**Occupant Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ODT**
> Object Descriptor Table —— 对象描述表。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**OEM**
> 原始设备制造商（**Original Equipment Manufacturer**）。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**Off-Mode**
> 看门狗硬件被禁用/关闭。这样做可能是为了关闭整个 **ECU**，而不遭受仍在运行的外部看门狗的周期性复位。对于安全关键系统，该模式可能不被允许。在这种情况下，必须将 **Wdg** 模块配置为禁止切换到此模式。
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](cp/safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**Offer**
> 提供一个服务实例（**Service Instance**）的消息条目。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Offering a service instance**
> **ECU** 实现服务的一个实例，并通过 **SOME/IP-SD** 告知其他 **ECU** 可以使用它（**An ECU implements an instance of a service and tells other ECUs using SOME/IP-SD that they may use it**）。
>
> 来源：[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**Offset Correction**
> 补偿时间偏移所需的偏移值。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Offset Time Base**
> 只与其底层同步时基结合存在的时基；其绝对时间值由偏移时基的偏移时间值加上底层同步时基的时间值得到。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**OFNS message**
> 偏移调整报文（Offset adjustment message）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

**OFS message**
> 偏移同步报文（**Offset Synchronization message**）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**OID**
> 对象标识符（**Object Identifier**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**on-entry ExecutableEntity**
> 由具有 `ModeActivationKind` 为 `entry` 的 `SwcModeSwitchEvent`（或 `BswModeSwitchEvent`）触发的 `RunnableEntity` 或 `BswSchedulableEntity`，在进入模式时被触发，称为进入时可执行实体（**on-entry ExecutableEntity**）。另见 6.2.4.1 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**on-exit ExecutableEntity**
> 由具有 `ModeActivationKind` 为 `exit` 的 `SwcModeSwitchEvent`（或 `BswModeSwitchEvent`）触发的 `RunnableEntity` 或 `BswSchedulableEntity`，在退出模式时被触发，称为退出时可执行实体（**on-exit ExecutableEntity**）。另见 6.2.4.1 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**on-transition ExecutableEntity**
> 由具有 `ModeActivationKind` 为 `transition` 的 `SwcModeSwitchEvent`（或 `BswModeSwitchEvent`）触发的 `RunnableEntity` 或 `BswSchedulableEntity`，在两个指定模式之间的转换中被触发，称为转换时可执行实体（**on-transition ExecutableEntity**）。另见 6.2.4.1 节。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Onboard Security Event**
> 类比 ISO/IEC 27000:2018（[44]），车载安全事件（**SEv**）是已识别的车载系统、服务或网络状态的出现，它指示可能违反信息安全策略或控制措施失效，或者是先前未知的、可能具有安全相关性的情形。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**OOP**
> 离位（**Out Of Position**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**OPC**
> 乘员预处理（**Occupant Pre Conditioning**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**Operating cycle**
> "运行周期"是事件鉴定和 **Dem** 调度的基础（例如点火钥匙关-开循环、驾驶循环等）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Operation**
> 操作：加密原语的操作声明应执行加密原语的哪一部分，共有 **START**、**UPDATE**、**FINISH** 三种操作模式；通过拼接操作模式参数的相应位可以一次执行多个操作。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**OPS**
> 乘员与行人安全（**Occupant and Pedestrian Safety**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**OPSS**
> OPS 系统（**OPS Systems**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ORA**
> 乘员约束激活（**Occupant Restraint Activation**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ORTI**
> OSEK 运行时接口——针对 OSEK 平台将跟踪工具对 OS 内部的访问标准化的标准（**OSEK Run-Time Interface**）
>
> 来源：[ARTI（AUTOSAR 运行时接口）](cp/sw_arch/arti/index.md)（AUTOSAR_CP_EXP_ARTI）
{: .glossary-source}

**OS**
> 操作系统（**Operating System**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）、[Requirements on Debug Trace Profile（调试跟踪配置文件需求）](foundation/communication_management/rs_debug_trace_profile/index.md)（AUTOSAR_FO_RS_DebugTraceProfile）
{: .glossary-source}

**OS Application**
> 包括任务、中断、钩子和用户服务在内、构成一个内聚功能单元的软件块。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**OS Event**
> 事件机制：• 是一种同步手段 • 仅为扩展任务提供 • 引发任务在等待状态之间进行状态转换。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**OSEK/VDX**
> 1993 年 5 月，**OSEK** 作为德国汽车工业的一个联合项目创立，旨在为车辆内分布式控制单元的开放式架构建立一个行业标准。**OSEK** 是德语术语「Offene Systeme und deren Schnittstellen für die Elektronik im Kraftfahrzeug」（英语：Open Systems and the Corresponding Interfaces for Automotive Electronics）的缩写。初始项目合作伙伴为 **BMW**、**Bosch**、**Daimler Chrysler**、**Opel**、**Siemens**、**VW** 以及作为协调方的卡尔斯鲁厄大学 **IIIT**。法国汽车制造商 **PSA** 和 **Renault** 于 1994 年加入 **OSEK**，引入了他们的 **VDX**（**Vehicle Distributed eXecutive**）方案——法国汽车工业内的一个类似项目。在 1995 年 10 月的第一次研讨会上，**OSEK/VDX** 小组展示了 **OSEK** 与 **VDX** 之间协调一致的规范成果。1997 年 10 月第 2 届国际 **OSEK/VDX** 研讨会之后，发布了规范的第二版。
>
> 来源：[AUTOSAR Standard Types（标准类型）](cp/general/standard_types/index.md)（SWS_StandardTypes）、[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）
{: .glossary-source}

**OSI**
> 开放系统互连（**Open Systems Interconnection**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**OTA**
> 远程升级（**Over The Air**），OEM 后台（**backend**）与车辆之间无线通信的总称。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Outer Priority Inversion**
> 由于两个连续发送的**L-PDU**之间存在时间间隔。在这种情况下，来自另一个节点的低优先级的**L-PDU**可以阻止发送自己的高优先级的**L-PDU**。此时，高优先级的**L-PDU**不能参与网络访问仲裁，因为低优先级的**L-PDU**已经赢得了仲裁。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**OVS**
> 溢出秒值（**Overflow Seconds** value，**FUP** 报文中的字段）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）
{: .glossary-source}

## P

**P-Code**
> 动力总成代码（**Power train code**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**P2**
> 在 LIN 总线上接收到诊断请求的最后一帧与从节点能够提供响应数据之间的时间。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**P2\***
> 从发送响应挂起帧（0x78）到 LIN 从设备能够为响应提供数据之间的时间。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**P2P**
> 点对点（**Point-to-Point**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**PAD**
> 对端授权数据库（**Peer Authorization Database**），**IPsec** 的数据库。
>
> 来源：[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**PAE**
> 端口访问实体（**Port Access Entity**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**Page Burst**
> 通过聚合访问存储页面来提高性能。在存储设备技术支持物理分段的情况下，一些存储设备可以提供一次读取或写入多个页面的优化访问方式。页面突发（**Page Burst**）表示用于访问优化的存储页面聚合。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Parameter**
> 参数（**Parameter**），SAE J1939 对信号的称谓，包含已定义的量程、限值、偏移量与物理单位
>
> 来源：[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**Parameter Communication Graph**
> 相互连接的各 `PortPrototype` 中实例化的 `ParameterDataPrototype` 上的所有 `ParameterAccess` 之和，或 `InternalBehavior` 中对 `ParameterDataPrototype` 的所有 `ParameterAccess` 之和（**Parameter Communication Graph**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Partial test**
> 部分测试定义为一个或多个「硬件资源」的测试。（部分测试是可中断的，因为它在后台模式下执行。）
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Partitioning**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.85
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**PASE**
> 无源进入（**Passive Entry**）。帮助用户无需物理使用钥匙即可进入汽车的锁定系统。
>
> 来源：[Explanation of Application Interfaces of the Body and Comfort Domain（车身与舒适域应用接口说明）](cp/application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort）
{: .glossary-source}

**Passive wake-up**
> 由另一个 ECU 引起、并（例如通过总线或唤醒线）传播到当前关注的 ECU 的唤醒（**Wake-up by another ECU and propagated to the ECU currently in focus**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**PC5**
> 用于 V2X 业务的 ProSe（基于邻近的服务）直接通信中 **UE**（用户设备）之间控制面和用户面的参考点。
>
> 来源：[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）
{: .glossary-source}

**PCD**
> 行人碰撞检测（**Pedestrian Crash Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**PCI**
> 协议控制信息（**Protocol Control Information**）。把一个 SDU 从协议层的一个实例传递到另一个实例所需的信息，例如源与目标信息。PCI 由发送侧的协议层添加，在接收侧移除。PDU 包含 SDU 和 PCI。
>
> 来源：[Layered Software Architecture（分层软件架构）](cp/general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）
{: .glossary-source}

**PCP**
> 行人碰撞预测（**Pedestrian Crash Prediction**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**PDC**
> 泊车距离控制（**Park Distance Control**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](cp/application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**Pdelay**
> **IEEE 802.1AS** 给出的传播/路径延迟（Propagation / path delay）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](cp/globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**PDID**
> 周期数据标识符（**Periodic Data Identifier**），在 **ReadDataByPeriodicIdentifier** 请求后由 **Dcm** 周期性发送。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**PDU**
> 协议数据单元（**Protocol Data Unit**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[Layered Software Architecture（分层软件架构）](cp/general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）、[VFB（虚拟功能总线）](cp/general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）、[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）
{: .glossary-source}

**PDU Meta-Data**
> "协议数据单元"（**Protocol Data Unit**）的附加数据，不属于有效载荷。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**PDU Router**
> PDU路由器是在模块之间传输I-PDU的模块。PDU路由器可用于网关操作和内部路由目的。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）、[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**PDU Timeout**
> 超过一个 PDU 的两个实例被接收之间的最大时间。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**PDU1**
> J1939 PDU 类型 1（**J1939 PDU Type 1**），这种 PG 可以发送到特定的目标地址
>
> 来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**PDU2**
> J1939 PDU 类型 2（**J1939 PDU Type 2**），这种 PG 只能以广播方式发送
>
> 来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**PDUF**
> **PDU** 格式（**PDU Format**），18 位 **PGN** 的中间字节。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**PduInfoType**
> 该类型指用于存储处理PDU（或SDU）发送/接收所需基本信息（即指向RAM中其有效载荷的指针和相应的长度（以字节为单位））的结构。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**PduR**
> PDU路由器
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**PDUS**
> **PDU** 特定（**PDU Specific**），18 位 **PGN** 的低位字节。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**PDU传输能力被禁用**（**PDU transmission ability is disabled**）
> 这意味着网络管理**PDU**传输已被服务**CanNm_DisableCommunication**禁用。
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

**PDU路由器（PDU Router）**
> 将**I-PDU**从一个模块传输到另一个模块的模块。PDU路由器模块可用于网关操作和内部路由目的。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**Performance**
> 针对故障行为对性能进行评级。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**periodic transmission rate**
> 周期数据标识符传输的两次调用之间的时间间隔；快速、中速和慢速周期传输分别配置速率，且配置值始终是 **Dcm** 主任务时间的整数倍。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Peripheral Hardware**
> 集成在微控制器架构中、用于与环境交互的硬件设备。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Permission state**
> 许可状态：包含由其 **FID** 表示的功能是否可以执行的信息。该状态由 **FiM** 基于已报告的事件控制。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**Personalization**
> 用户特定的、被记忆保存的 SW 数据调整或功能备选项选择。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**PFC cycle**
> 永久故障代码——驾驶循环（**OBD** 术语）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**PG**
> 参数组（**Parameter Group**）。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**PGN**
> 参数组编号（**Parameter Group Number**）（18 位，包含 **EDP**、**DP**、**PDUF**、**PDUS**）。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**PH**
> 路径历史（**Path History**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**PHM**
> 平台健康管理（**Platform Health Management**）——自适应平台的健康监控。
>
> 来源：[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**PHY**
> 物理层（**Physical Layer**）。
>
> 来源：[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**Physical Addressing**
> 物理寻址：特定通信网络中的一个节点从一个发送节点接收消息（1:1）的诊断通信模型，也称为单播。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Physical addressing**
> 在传输层中，物理寻址指的是N_TAtype参数（它是用于编码通信模型的N_TA参数[1]的扩展）取值为physical的N-SDU。这意味着该N-SDU用于1到1的通信，因此所有类型的网络层消息都支持物理寻址。在应用方面，如果外部（或内部）测试仪知道应响应服务请求的ECU的物理地址，则外部（或内部）测试仪会使用物理寻址。使用物理寻址时，通信为点对点通信（1对1通信）。用例有（例如）「ReadDataByIdentifier」或「InputOutputControlByIdentifier」等消息。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Physical Channel**
> 一个物理通道代表一个从CAN控制器到CAN网络的接口。CAN硬件单元的不同物理通道可能访问不同的网络。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**PID**
> 参数标识（**Parameter Identification**，SAE J1587 或 SAE J1979）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**PKI**
> 公钥基础设施（**Public Key Infrastructure**）。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**Platform Health Management**
> 健康监控（**Health Monitoring**）在自适应平台的实现。
>
> 来源：[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**Platform Health Management (PHM)**
> 平台健康管理（**Platform Health Management**）。
>
> 来源：[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Plausibility**
> 运行时合理性检查（**Plausibility**）是一种在运行期间验证计算/算法的输入或结果相对于简化参考模型的对应值是否合理的方法。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**PLC**
> 导引线通信（**Pilot Line Communication**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**PLCA**
> 物理层冲突避免（**Physical Layer Collision Avoidance**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**PN**
> 包编号（**Packet Number**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**PN filter mask**
> 由每通道的配置容器NmPnFilterMaskByte定义的过滤掩码字节向量，用于为PNC定时器处理过滤相关的PNC请求。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**PN shutdown message**
> 顶层PNC协调器发送PN关闭消息以在PN拓扑上指示一次同步PNC关闭。PN关闭消息是一条控制位向量中PNSR位置位、且所有被指示为同步关闭的PNC均置为「1」的NM消息。接收到PN关闭消息的中间PNC协调器必须在受影响的通道上将该PNC位向量作为PN关闭消息转发。注意：中间PNC协调器必须尽快转发所接收PN关闭消息的PNC位向量，以确保受影响的PNC在PN拓扑上近乎同步地关闭。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**PNC**
> 部分网络集群（**Partial Network Cluster**）。一组系统信号，用于支持分布在车辆网络多个 ECU 上的一个或多个车辆功能；表示把一组总线映射到一个或多个虚拟功能集群（VFC）的系统视图。
>
> 来源：[Layered Software Architecture（分层软件架构）](cp/general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）、[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）、[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**PNC bit**
> 在部分网络信息范围（**Partial Network Info Range**）中表示某个特定部分网络的一个位。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**PNC bit vector**
> 在NM帧中表示部分网络信息。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**PNC bit vector length**
> 以字节表示部分网络信息的长度。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**PNC Gateway**
> **PNC** 网关——跨总线/通信信道边界跨越（逻辑）部分网络集群、转发 **PNC** 请求的网关功能。
>
> 来源：[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**PNC Leaf Node**
> PNC 叶节点（**PNC Leaf Node**）位于"顶层 PNC 协调器"（**Top-level PNC Coordinator**）或"中间 PNC 协调器"（**Intermediate PNC Coordinator**）之下。PNC 叶节点代表 PN 拓扑层级中的最低层级。PNC 叶节点不跨其本地通信信道协调 PNC 请求。它接收和发送带 PN 信息的 Nm 帧，但不将收到的 PNC 请求转发到其他本地通信信道。PNC 叶节点将 PN 关机报文当作普通的带 PN 信息的 Nm 帧处理。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**PNC leaf node**
> PNC叶节点是既不充当顶层PNC协调器也不充当中间PNC协调器的ECU。它在网络中充当没有PNC网关的ECU，并将PN关闭消息作为普通NM消息处理。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**PNC叶节点**（**PNC leaf node**）
> PNC叶节点是一个**ECU**，在网络中根本不充当PNC协调器。它像通常的NM消息一样处理PN关闭消息。
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

**PNI**
> 部分网络信息（**Partial Network Information**）
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**PNL**
> 部分网络学习（**Partial Network Learning**）
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**PN关闭消息**（**PN shutdown message**）
> 顶级PNC协调器传输PN关闭消息以指示跨PN拓扑的同步PNC关闭。PN关闭消息是作为**NM**消息，它在控制位向量中具有**PNSR**位，并且所有被指示用于同步关闭的PNC都设置为**1**
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**POC**
> 协议运行控制（**Protocol Operation Control**，详情参见 ISO 17458-1）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**POCState**
> **CC** 内部的 **POC** 实际状态。该状态在某些情况下可能与 vPOC!State 不同，例如在 FREEZE 命令调用之后（详情参见 ISO 17458-1）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**POD**
> 俯仰翻覆碰撞检测（**Pitchover Crash Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**Policy Decision Point (PDP)**
> PDP（策略决策点）表示做出访问控制决策的逻辑。它确定是否允许应用执行所请求的任务。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Policy Enforcement Point (PEP)**
> PEP（策略执行点）表示执行"访问控制判定"（**Access Control Decision**）的逻辑。它直接与相应的"策略决策点（**Policy Decision Point (PDP)**）"通信以接收访问控制判定。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Port**
> Port module (SPAL module)
>
> 来源：[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）
{: .glossary-source}

**Port Group**
> 端口组（**Port Group**）。把离散端口分组的建模元素；抽象平台允许把离散端口分配给零个或多个端口组。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**Port Interface**
> 端口接口（**Port Interface**）刻画"软件组件"（**Software Component**）的某个"端口"（**Port**）所提供或所需的信息。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Port-Interface**
> 端口接口。定义提供或要求该接口的端口必须履行的契约；AUTOSAR 支持客户端-服务器、发送者-接收者、参数、非易失性数据、触发与模式切换六种端口接口。
>
> 来源：[VFB（虚拟功能总线）](cp/general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**Positive Callback from NvM**
> 如果需要在 Dem_Init 和 Dem_Shutdown 之间存储数据，**Dem** 模块应使用 **NVRAM** 管理器的 **API** NvM_WriteBlock 和 NvM_GetErrorStatus。此外，**API** NvM_GetErrorStatus 应等待块写入成功完成的肯定响应。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Post-build Hooking**
> 将便于快速原型支持的钩子（**Hook**）插入（完整的）ECU hex 镜像。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Post-build Time Configuration**
> SW 模块的配置可以在构建 SW 模块之后进行。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**post-build variability**
> 由带有 `PostBuildVariantCriterion` 的 `VariationPoint` 定义的可变性（**post-build variability**，构建后可变性）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**POTI**
> 位置与时间（**Position and Time**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**PPA**
> 行人保护执行器激活（**Pedestrian Protection Actuator Activation**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**PPP**
> 行人保护系统预处理（**Pedestrian Protection system Pre conditioning**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**PPPP**
> ProSe 按包优先级（**ProSe Per-Packet Priority**）。
>
> 来源：[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）、[AUTOSAR Chinese V2X Network（中国V2X网络）](cp/communication/chinesev2x_net/index.md)（AUTOSAR_CP_SWS_ChineseV2XNetwork）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**Pre-build Hooking**
> 在创建 ECU hex 镜像之前，将便于快速原型支持的钩子（**Hook**）插入软件源代码。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**pre-build variability**
> 由最迟绑定时间为 `SystemDesignTime`、`CodeGenerationTime`、`PreCompileTime` 或 `LinkTime` 的 `VariationPoint` 或 `AttributeValueVariationPoint` 定义的可变性（**pre-build variability**，构建前可变性）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Pre-Compile Time Configuration**
> SW 模块的配置在源代码级别完成，并在编译期之后生效。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**PreCompileTime variability**
> 由最迟绑定时间为 `PreCompileTime` 的 `VariationPoint` 或 `AttributeValueVariationPoint` 定义的可变性（**PreCompileTime variability**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Predictabiliy**
> 可预测性（**Predictability**）是指能够对系统的状态/行为做出正确的定性或定量预测或预估的程度。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**preemption area**
> 抢占区（**preemption area**）定义了一组协作式调度的任务。因此一个抢占区的各任务只在专用的调度点相互抢占。调度点不允许出现在可运行实体的执行期间。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Pretended Networking**
> 在不改变网络基础设施的情况下，降低现有活动网络中能耗的方法。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**PRF**
> 伪随机函数（**Pseudo Random Function**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**Primary ECU**
> **Primary ECU** 在其事件内存中存储"自己的"以及相关的从属/辅助 **ECU** 的"报告的错误"。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Primitive**
> 原语：在加密驱动程序对象中实现的已配置加密算法的实例；它指向 **CSM** 向应用程序提供的功能、具体的底层算法家族（如 **AES**、**MD5**、**RSA**）以及算法模式（如 **ECB**、**CBC**）。
>
> 来源：[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**primitive data type**
> 基本数据类型（**primitive data type**）是由布尔量、整数（最多 32 位）、浮点数或不透明类型（最多 32 位）实现的类型。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Priority**
> 优先级：作业的优先级定义其重要性，优先级（数值）越高，作业越需立即执行；加密作业的优先级是配置的一部分。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Private Interface**
> 私有接口（**Private Interface**）是 AUTOSAR"基础软件"（**Basic Software**）内部的接口，既未被标准化也未在 AUTOSAR 中定义。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Probability of Failure**
> 系统或功能单元中发生失效（**Failure**）的概率。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Procedure Call**
> 一种简单的语句，它为过程（软件函数）的执行提供实际参数并调用该执行。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Process**
> 由操作系统调度器管理的可执行单元，它拥有自己的命名空间和资源（包括内存），并受保护不被其他进程使用。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Processed Manifest**
> 已处理清单（**Processed Manifest**）是以实现特定格式存储在 AUTOSAR 自适应平台产品上的清单。通常这与其他包含清单所适用可执行代码的制品（如二进制文件）一起完成。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Processing**
> 处理：指示作业处理的类型。异步（**Asynchronous**）：调用相应函数时作业不会被立即处理，通常由后续的调度函数处理并通过回调通知结果；同步（**Synchronous**）：调用相应函数时作业被立即处理，函数返回时结果已可用。
>
> 来源：[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**Profiling**
> 性能剖析（**Profiling**）指评估"性能"（**Performance**）的过程。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Protocol Control Information**
> 将"服务数据单元"（**Service Data Unit**）从一个特定协议层的实例传递到另一个实例所需的信息。例如它包含源和目标信息。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Protocol Data Unit**
> 协议数据单元（**Protocol Data Unit**, PDU）包含"服务数据单元"（**Service Data Unit**）和"协议控制信息"（**Protocol Control Information**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Prototype**
> 原型。组件类型在一个组合（Composition）中的使用；组合经由相互连接的原型定义。
>
> 来源：[VFB（虚拟功能总线）](cp/general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**Proven In Use Argument**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.90
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Provide Port**
> 提供数据或提供服务器服务的特定"端口"（**Port**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Proxy Module**
> 替代应用软件集群中一个 BSW 模块的模块，拆分为高代理与低代理（**Proxy Module**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](cp/system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）、[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**PRS IDS**
> 协议需求规范入侵检测系统——描述 **IDS** 协议全部元素的规范文档。
>
> 来源：[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**PSK**
> 预共享密钥（**Pre-Shared Keys**）。
>
> 来源：[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**PTC**
> 动力总成协调器（**Powertrain Coordinator**）
>
> 来源：[Explanation of Application Interfaces of the Powertrain Engine Domain（动力总成（发动机）域应用接口说明）](cp/application_interfaces/powertrain/index.md)（AUTOSAR_CP_EXP_AIPowertrain）
{: .glossary-source}

**PTO**
> 动力输出（**Power Take Off**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**PTP**
> 精确时间协议（**Precision Time Protocol**）。
>
> 来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](cp/globaltime/eth_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverEthernet）
{: .glossary-source}

**Pure Local Time Base**
> 只在本地被设置和读取、不通过 Timesync 模块同步但随时间推进的时基；只支持 **API** 的一个子集。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

## Q

**QSEv**
> 合格安全事件（**Qualified Security Event**）——通过其过滤器链的安全事件。
>
> 来源：[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）、[Requirements on Firewall（防火墙需求）](foundation/security/rs_firewall/index.md)（AUTOSAR_FO_RS_Firewall）
{: .glossary-source}

## R

**RA**
> 后轴（**Rear Axle**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**RAM**
> Random Access Memory —— 随机访问存储器。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**RAM Block**
> 「RAM 块」是「基本存储对象」。它代表驻留在 **RAM** 中的「NVRAM 块」的一部分。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**Range**
> 范围（**Range**）在这里是一个功能范围（**functional range**），而不是电气范围（**electrical range**）。所有范围都用于功能的需要或者诊断的检测。对于模拟**ECU**信号，可以定义上下限值 [lowerLimit...upperLimit]（电压、电流）。对于电阻信号和时序信号（周期）的特殊情况，下限值（**lowerLimit**）不能为负。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Rapid Prototyping**
> 以实验方式并入新功能。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Rapid Prototyping Memory Interface**
> "快速原型工具"（**Rapid Prototyping Tool**）所必需的内存访问模式。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Rapid Prototyping Tool**
> 支持"快速原型"（**Rapid Prototyping**）的软件和/或硬件工具。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Rate Conversion**
> 改变同一 PduId 在一个物理网络上两次传输之间时序的操作。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Rate Correction**
> 补偿速率偏差所需的因子。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Rate Deviation**
> 速率偏差值表示时钟的频率偏离参考时钟速率的程度。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Raw Data Stream**
> 原始数据流（**Raw Data Stream**）是未处理的数据集合，基本上是一系列字节，不带有任何关于如何解释它们的信息。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**RBM cycle**
> **OBD** 术语：通用分子/基于比率的监控——驾驶循环。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**RCRRP**
> 正确接收响应——响应挂起（**Response correctly received - response pending**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Readiness**
> 就绪状态指 **UDS** 状态字节的已测试位 TestNotCompletedSinceLastClear（位 4）和 TestNotCompletedThisOperationCycle（位 6）。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Recovery**
> 在故障检测后恢复到预期功能，而不违反安全目标。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Redundancy**
> 在足以使元素执行所需功能或表示信息的手段之外，还存在额外的手段。硬件元素冗余包括为支持容错而添加到系统中的复制或附加的硬件手段。软件元素冗余包括用于支持容错的附加软件单元和/或数据。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Reentrancy**
> 在 AUTOSAR 中，如果一个函数可以在其执行过程中被中断，并且在其先前的调用完成执行之前被安全地再次调用（"重入"），则该函数称为可重入函数。AUTOSAR 区分：•（完全）可重入 • 不可重入 • 条件可重入。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Reference time**
> 参考时间：为每个计时器实例存储的时间值，是 **API** 数据类型 Tm_PredefTimer...bitType 所对应的实现特定元素。
>
> 来源：[AUTOSAR Time Service（时间服务）](cp/system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**Relevant frame**
> 从 LIN 从节点的角度来看，从节点发送或接收的帧。与无关帧相对。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**Reliability**
> 评估由于不确定性而对系统的可信程度。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Relocatability**
> 软件部件能够在不同硬件环境中执行而不改变该软件部件代码的能力。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Remote Procedure Call**
> 远程过程调用（**RPC**）——从一个 **ECU** 到另一个 **ECU**、使用消息传输的方法调用。
>
> 来源：[Requirements on SOME/IP Protocol（SOME/IP 协议需求）](foundation/protocols/rs_someip_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPProtocol）
{: .glossary-source}

**Repeat Message State**
> 重复消息状态——通过重复传输 **NM** 消息确保向正常运行转换对总线上其他节点可见的 **NM** 状态。
>
> 来源：[Network Management Protocol Specification（网络管理协议规范）](foundation/protocols/prs_network_management_protocol/index.md)（AUTOSAR_FO_PRS_NetworkManagementProtocol）
{: .glossary-source}

**Request**
> 客户端发给服务器、调用某个方法的消息。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）
{: .glossary-source}

**Require Port**
> 需要数据或需要服务器服务的特定"端口"（**Port**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Required Property**
> 设计实体（例如软件组件或系统）的"被要求的属性或质量"（**Required Property**）是指必须由该设计实体的环境来满足的属性或质量。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Residual Error Rate**
> 接收错误且未被检测到的位、单元元素或块的数量，除以已发送的位、单元元素、字符或块的总数所得的比值。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Resolution**
> 分辨率（**Resolution**）属性适用于依赖于范围和数据类型的许多类别。如：(upperLimit - lowerLimit) / (2<sup>datatypelength</sup> -1)。 对于其他类别，它可能是已知和被定义的。如：[-12 Volts…+12Volts]，数据类型: 16 bits，**Resolution** 为 24 / 65535。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Resource**
> 「硬件资源」是 **CoreTest** 驱动程序用户可以选择的最小单元（实例）。它可以在一个或多个原子序列中被测试。它是执行特定功能（例如 **IRQ** 控制器）的内核内部单元。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Resource-Management**
> 控制"资源"（**Resource**）使用的实体。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Response**
> 服务器发给客户端、传输方法调用结果的消息。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）
{: .glossary-source}

**Response Time**
> 从接收激励到交付适当响应或反应之间的时间。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**REST Services Interface**
> REST 服务接口（**REST Services Interface**，**RSI**）。以 REST 风格提供的服务接口。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**retransmit counter**
> 部分 **CAN XL** 控制器提供的一项特性：当 **ACK** 槽未在总线上置位时，允许将一个 **CAN** 帧连续多次发送。该计数器给出了最大发送次数。
>
> 来源：[AUTOSAR CAN XL Driver（CAN XL 驱动程序）](cp/communication/canxl_driver/index.md)（SWS_CANXLDriver）
{: .glossary-source}

**RID**
> 例程标识符（**Routine Identifier**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**RIPS**
> 缩写 **RIPS** 代表 **RTE Implementation Plug-In Service**，相关的 **API** 中缀 `Rips` 由此派生。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RIPS FlatInstanceDescriptor**
> 把通信图分配给某个 **RTE** 实现插件的 `FlatInstanceDescriptor`（**RIPS FlatInstanceDescriptor**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Risk**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.99
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**RKE**
> 遥控无钥匙进入（**Remote Keyless Entry**）。设计用于远程锁定或解锁汽车进入的系统；单向广播无线电波，实现加密与滚动码算法。
>
> 来源：[Explanation of Application Interfaces of the Body and Comfort Domain（车身与舒适域应用接口说明）](cp/application_interfaces/body_and_comfort/index.md)（AUTOSAR_CP_EXP_AIBodyAndComfort）
{: .glossary-source}

**RLT**
> 道路与车道拓扑（**Road and Lane Topology**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**RNG**
> 随机数发生器（**Random Number Generator**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**Robustness**
> 系统或功能单元即使在意外条件下也能按预期执行的能力。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**ROD**
> 翻滚碰撞检测（**Rollover Crash Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**ROE**
> 事件响应（**ResponseOnEvent**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Rollover mechanism**
> 下面的示例序列被称为"回绕"（**rollover**）：一个无符号字符（**unsigned char**）的值为 255；将其加 1；结果为 0。
>
> 来源：[AUTOSAR Platform Types（平台类型）](cp/general/platform_types/index.md)（SWS_PlatformTypes）
{: .glossary-source}

**ROM**
> Read Only Memory —— 只读存储器。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**ROM Block**
> 「ROM 块」是「基本存储对象」。它代表驻留在 **ROM** 中的「NVRAM 块」的一部分。「ROM 块」是「NVRAM 块」的可选部分。
>
> 来源：[AUTOSAR NVM（非易失性存储管理器）](cp/memory/nvram_manager/index.md)（AUTOSAR_CP_SWS_NVRAMManager）
{: .glossary-source}

**RP enabler flag**
> 允许在运行时启用/禁用旁路的布尔标志（**RP enabler flag**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP event id**
> 被旁路事件的标识符；作为参数传递给 **RP** 服务函数（**RP event id**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP global buffer**
> 由 **RP** 读写的缓冲区（**RP global buffer**）。**RP** 全局缓冲区在概念上与保存变量数据原型值的 **RTE** 管理缓冲区分离。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP global measurement buffer**
> **RP** 用于在用 **RP** 生成的值替换之前、为后续测量目的保存原始变量数据原型值的缓冲区（**RP global measurement buffer**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP runnable disabler flag**
> 允许条件性 `RunnableEntity` 执行的布尔标志（**RP runnable disabler flag**）。配置了条件执行时，该标志为 `FALSE` 时可运行实体才被执行。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP service component**
> 提供 **RP** 服务（例如 "XCP on CAN" 或 "XCP on Ethernet"）的 **AUTOSAR** 或供应商专有 **BSW** 模块（**RP service component**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP service profile**
> 组合提供服务的函数符号与允许的 **RP** 服务点 ID 范围的服务定义（**RP service profile**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP service function**
> 对由 **RP** 服务组件提供的函数的一次调用，其中数据被采样和/或激励（**RP service function**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP service point**
> 调用由 **RP** 服务组件提供的一个或多个 **RP** 服务函数的位置（**RP service point**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP service point id**
> **RP** 服务点的整数标识符（**RP service point id**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP service invocation wrapper**
> 由 **RTE** 创建的、负责调用各 **RP** 服务函数的"包装"函数（**RP service invocation wrapper**）。由此引入的间接层使构建后工具能够用任意功能替换对 **RTE** 生成函数的调用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RP stimulation enabler flag**
> 允许条件性 **RP** 激励的布尔标志（**RP stimulation enabler flag**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RPC**
> 远程过程调用（**Remote Procedure Call**）——从一个 **ECU** 到另一个 **ECU**、使用消息传输的方法调用。
>
> 来源：[Requirements on SOME/IP Protocol（SOME/IP 协议需求）](foundation/protocols/rs_someip_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPProtocol）
{: .glossary-source}

**RQST**
> **J1939** 请求 **PG**（**Request PG**）（**PGN** = 0x0EA00）。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）
{: .glossary-source}

**RQST2**
> **J1939** 请求 2 **PG**（**Request2 PG**）（**PGN** = 0x0C900）。
>
> 来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）
{: .glossary-source}

**RSA**
> Rivest-Shamir-Adleman。一种使用公钥和私钥进行数据加密和解密的方法。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**RSC**
> 侧翻稳定控制（**Roll Stability Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**RSI**
> 路侧信息（**Road Side Information**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**RSM**
> 约束系统监测（**Restraint System Monitoring**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）、[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**RSP**
> 约束系统预处理（**Restraint System Pre conditioning**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**RSSI**
> Received Signal Strength Indicator，接收信号强度指示器。
>
> 来源：[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）
{: .glossary-source}

**RSU**
> 路侧单元（**Roadside Unit**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**RTE**
> 运行时环境（**Runtime Environment**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}

**RTE Event**
> RTE 事件（**RTE Event**）涵盖能够触发 RTE 执行"可运行实体"（**Runnable Entity**）的所有可能情形。因此它们可以涉及时序、数据发送与接收、操作调用、服务器调用返回、模式切换或外部事件。RTE 事件可以激活一个可运行实体，或在其等待点唤醒一个可运行实体。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**RTE event identifier**
> **RP** 用于标识与某个 **RP** 服务点关联的 **RTE** 事件的整数标识符（**RTE event identifier**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RTE Implementation Plug-In**
> **RTE** 实现插件（**RTE Implementation Plug-In**）是整体 **RTE** 实现的一部分，它不是由 **RTE** 生成器提供，而是来自附加来源（例如插件生成器或手工实现的源代码）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RTE Implementation Plug-In Service**
> **RTE** 实现插件服务（**RTE Implementation Plug-In Service**）是进入 **RTE** 实现插件、为 **RTE** 实现某个低层服务的单一入口点，例如对某个特定缓冲区的访问。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Runnable**
> 可运行体。原子软件组件实现中的一段可由 RTE 启动的指令序列；在任务的上下文中运行。
>
> 来源：[VFB（虚拟功能总线）](cp/general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**runnable activation**
> 可运行实体的激活与导致该可运行实体执行的 `RTEEvent` 相关联（**runnable activation**）。它被定义为该 `RTEEvent` 所指称的事件。例如，对于定时事件，当定时器到期时相应的可运行实体被激活；对于数据接收事件，当 **RTE** 接收到数据时可运行实体被激活。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Runnable Entity**
> 可运行实体（**Runnable Entity**）是"原子软件组件"（**Atomic Software Component**）的一部分，可以独立于该原子软件组件的其他可运行实体被执行和调度。它由一串可由 RTE 启动的指令描述。每个可运行实体恰好关联一个"入口点"（**Entry Point**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Runnable entity**
> 可运行实体：原子软件组件的一部分，可以独立于该原子软件组件的其他可运行实体被执行和调度。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）
{: .glossary-source}

**runnable start**
> 可运行实体的启动指在已启动的任务/ISR2 内调用实现该可运行实体的 **C** 函数（**runnable start**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**RVF**
> 原始视频格式（**Raw Video Format**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**RWW**
> 并行读写（**Read While Write**）。指存储设备在一个存储 **Bank** 中执行读取操作，同时在另一个存储 **Bank** 中执行写入或擦除操作的能力。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**RX**
> 接收（**Reception**）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**Rx Time Tuple**
> 时间元组 [TG_Rx, TV_Rx]，在跟随报文进入时导出，并由 &lt;Bus&gt;TSyn 模块通过 StbM_BusSetGlobalTime 交给 **StbM**。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**RX_DL**
> 接收数据链路层数据长度
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

## S

**S/R**
> 发送方/接收方（**Sender/Receiver**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**SA**
> 安全关联（**Security Association**）。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**SACK**
> 选择性确认（**Selective Acknowledgment**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**SAD**
> 安全关联数据库（**Security Association Database**），**IPsec** 的数据库。
>
> 来源：[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**SAE J1939**
> SAE J1939 是由 SAE（美国汽车工程师学会，美国的标准机构）为轿车和重型卡车行业创建的车载总线标准。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Safe State**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.102
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Safety**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.103
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Safety Analysis**
> 安全分析的目的是在考虑其功能、行为和设计的前提下，检查故障和失效对项目与元素造成的后果。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Safety Case**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.106
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Safety Goal**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.108
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Safety Measure**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.110
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Safety Mechanism**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.111
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Safety Protocol**
> 一种通信协议，定义了确保所传输数据完整性并检测任何与通信相关错误所需的机制。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**SAI**
> 安全关联标识符（**Secure Association Identifier**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）
{: .glossary-source}

**SAK**
> 安全关联密钥（**Secure Association Key**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**Sample Application**
> 用于评估目的的已定义系统。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Sampling rate**
> 采样率（**Sampling rate**）是获得信号值所需的时间段。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Sampling Time, Sample Time**
> 采样时间是指对模拟值进行采样的时间（例如：加载电容器，……）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**SAP**
> 服务访问点（**Service Access Point**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**Satellite**
> 卫星。分布式 BSW 模块的一部分；主与卫星之间的工作分配是实现特定的，卫星一般不能在没有主的情况下工作。
>
> 来源：[BSW Distribution Guide（BSW 分布指南）](cp/general/bsw_distribution_guide/index.md)（AUTOSAR_CP_EXP_BSWDistributionGuide）
{: .glossary-source}

**SBC**
> System Basis Chip 系统基础芯片。集成了例如 CAN 和/或 LIN 收发器、看门狗和电源控制。
>
> 来源：[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**SBR**
> 安全带提醒（**Seat Belt Reminder**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**SC**
> 监督周期（**Supervision Cycle**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）
{: .glossary-source}

**Scalability**
> 资产能够按各种已定义的度量被适配到特定目标环境的程度。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Schedule entry is due**
> 这意味着 LIN 接口已到达调度表中的新条目，并且将启动一个帧（接收或发送）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**Scheduler**
> 调度器（**Scheduler**）根据优先级和调度策略（预定义的或可配置的）处理任务/可运行实体（"任务"（**Task**）/"可运行实体"（**Runnable Entity**））的调度。它负责在运行期间决定哪个任务何时可以在 ECU 的 CPU 上运行。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**SchM**
> 基础软件调度管理器，**RTE** 的一部分（**Basic Software Schedule Manager**）。
>
> 来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](cp/communication/j1939nm/index.md)（AUTOSAR_CP_SWS_SAEJ1939NetworkManagement）、[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**SCI**
> 安全通道标识符（**Secure Channel Identifier**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**SD**
> 服务发现（**Service Discovery**）。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）
{: .glossary-source}

**Sd**
> AUTOSAR中的服务发现模块（**Service Discovery Module in AUTOSAR**）。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**SDP**
> SECC 发现协议（**SECC Discovery Protocol**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**SDU**
> 服务数据单元（**Service Data Unit**）——**PDU** 的载荷。
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR Platform Types（平台类型）](cp/general/platform_types/index.md)（SWS_PlatformTypes）、[Layered Software Architecture（分层软件架构）](cp/general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）、[VFB（虚拟功能总线）](cp/general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）、[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）、[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**SDU type**
> 服务数据单元类型（**service data unit type**）。
>
> 来源：[AUTOSAR CAN XL Driver（CAN XL 驱动程序）](cp/communication/canxl_driver/index.md)（SWS_CANXLDriver）
{: .glossary-source}

**SE**
> 被监督实体（**Supervised Entity**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**SECC**
> 供电设备通信控制器（**Supply Equipment Communication Controller**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**SecOC**
> 安全车载通信（**Secure Onboard Communication**）——验证 **PDU** 级通信真实性与新鲜度的 **AUTOSAR** 协议。
>
> 来源：[Secure Onboard Communication Protocol Specification（安全车载通信协议规范）](foundation/protocols/prs_secoc_protocol/index.md)（AUTOSAR_FO_PRS_SecOcProtocol）
{: .glossary-source}

**SecOC**（**Secure Onboard Communication**）
> 安全板载通信
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**SecTAG**
> **MAC** 安全标签（**MAC Security TAG**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**Sector**
> 扇区（**Sector**）是指最小的可擦除存储单元（以字节为单位）。某些存储设备技术在写入存储前需要显式执行物理擦除操作。扇区定义了此类擦除单元的最小大小。根据存储设备的不同，扇区可以为统一大小或可变大小。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Sector Batch**
> 扇区批次（**Sector Batch**）是大小统一的扇区集合，即大小相同且连续的扇区的逻辑集合。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Sector Burst**
> 扇区突发（**Sector Burst**）是聚合扇区以提高擦除性能。如果存储技术需要物理擦除操作，一些设备会通过一步擦除一组扇区来优化擦除性能。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Secure Channel**
> 安全通道（**Secure Channel**）是两方之间的通信信道。安全通道至少应提供通信的完整性和真实性。它应提供至少对通信一方进行身份验证的手段。它可以提供对通信双方进行相互身份验证的手段。安全通道还可以额外提供通信的机密性。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Secured I-PDU**（受保护的 I-PDU）
> 受保护的 I-PDU 是一个 AUTOSAR I-PDU，它包含可信 I-PDU 的负载并附加了额外的认证信息。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**Security**
> 保护数据、软件实体或资源免受意外或恶意行为的影响。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Security Event**
> 安全事件（**Security Event**）——由 **IdsM** 检测并上报的安全相关的观测事件，由安全提取定义和配置。
>
> 来源：[Requirements on Security Extract Template（安全提取模板需求）](foundation/methodology_templates/rs_security_extract_template/index.md)（AUTOSAR_FO_RS_SecurityExtractTemplate）、[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）、[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Security Event Type**
> 安全事件类型（**Security Event Type**）——可通过其安全事件类型 ID 标识；其实例称为安全事件并共享同一类型 ID。
>
> 来源：[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）
{: .glossary-source}

**Security Sensors**
> 安全传感器（**Security Sensors**）——向 **IdsM** 上报安全事件的 **BSW** 或 **SWC**。
>
> 来源：[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）
{: .glossary-source}

**SecXT**
> 安全提取（**Security Extract**）——规定哪些安全事件由 **IdsM** 实例处理及其配置参数。
>
> 来源：[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）
{: .glossary-source}

**SecY**
> **MAC** 安全实体（**MAC Security Entity**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**segment**
> 静态部分或动态部分可以由多于一个片段组成。这些片段称为段（**segment**）。另见第6.2.1节和图7.1。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**selector field**
> 见[2]。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Sem**
> 安全事件存储器（**Security Event Memory**）——独立于主诊断事件存储器的用户定义诊断事件存储器。
>
> 来源：[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）
{: .glossary-source}

**Sender-Receiver Communication**
> 一种通信模式，它提供信息的异步分发：发送方将信息传送给一个或多个接收方，或接收方从一个或多个发送方接收信息。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Sender-receiver communication**
> 发送方-接收方通信涉及原子数据元素组成的信号的发送和接收，这些原子数据元素由一个组件发送给另一个或多个组件。发送方-接收方接口可以包含多个数据元素。发送方-接收方通信是单向的 接收方发送的任何回复都可以视为一个单独的发送方-接收方通信。接收方组件的端口可以读取接口描述定义的数据元素，而提供方组件的端口可以按照接口描述定义写入数据元素。
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**Sender-Receiver Interface**
> 发送方-接收方接口（**Sender-Receiver Interface**）是一种特殊的"端口接口"（**Port Interface**），用于"发送方-接收方通信"（**Sender-Receiver Communication**）的情形。发送方-接收方接口定义了由发送组件（拥有提供该发送方-接收方接口的 p 端口）发送、或由接收组件（拥有需要该发送方-接收方接口的 r 端口）接收的数据元素。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Sensor/Actuator SW-Component**
> 专用于控制传感器或执行器的"软件组件"（**Software Component**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**SEooC**
> 脱离语境的安全要素（**Safety Element out of Context**）
>
> 来源：[Overview of Functional Safety Measures in AUTOSAR（AUTOSAR 功能安全措施概览）](cp/safety/functional_safety_measures/index.md)（AUTOSAR_CP_EXP_FunctionalSafetyMeasures）
{: .glossary-source}

**Sequence**
> 序列：若干个待传输的连续作业，但可以使用优先级机制在作业之间重新调度；序列传输是否可被中断取决于静态配置。
>
> 来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](cp/communication/spi_handler_driver/index.md)（SWS_SPIHandlerDriver）
{: .glossary-source}

**Sequence Counter**
> 时间同步报文中的序列计数器（**SC**）。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Server**
> 承载服务器服务（**ServerServices**）的ECU。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）、[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}

**server ExecutableEntity**
> 由 `OperationInvokedEvent` 或 `BswOperationInvokedEvent` 触发的服务器（**server ExecutableEntity**）。在某些情况下，**RTE** 可以把客户端-服务器通信实现为简单的函数调用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**server runnable**
> 由 `OperationInvokedEvent` 触发的服务器（**server runnable**）。它兼有可运行实体与函数调用的行为。在某些情况下，**RTE** 可以把客户端-服务器通信实现为简单的函数调用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Server Service**
> 提供一个服务。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Service**
> 服务：按 **TR_Glossary** 文档的定义理解——服务是一种具有已发布的接口和行为规范的操作，涉及功能提供者与潜在客户之间的合同。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）、[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**Service Data Unit**
> 服务数据单元（**Service Data Unit**）是上层为请求传输而传递的数据。它也是下层在接收后提取并传递给上层的数据。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Service Discovery**
> 由通信管理（**Communication Management**）向应用提供的通用功能，允许应用在运行时找到提供所请求服务的、本地或远程可用的服务实例。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Service Instance**
> 服务（**Service**）的单个实例。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**Service Interface**
> 服务的形式化规范，包括其方法、事件和字段。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）
{: .glossary-source}

**Service Oriented Communication**
> 通信伙伴一般不在设计期定义、而是在运行期间动态发现和绑定的通信。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Service Port**
> "原子软件组件"（**Atomic Software Component**）的一种特殊"端口"（**Port**），用于描述服务通信。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Service Proxy**
> 从服务消费者的角度在代码级别代表特定服务的一个外观（**facade**），它为所代表服务提供的所有功能提供了相应的方法。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Service Skeleton**
> 从服务实现的角度在代码级别对特定服务的表示，它按照服务定义提供功能，并允许将服务实现连接到通信管理的传输层，使服务实现能够被服务消费者联系。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Services Layer**
> 服务层（**Services Layer**）是基础软件的最高层，这也决定了它与应用软件的相关性：对 I/O 信号的访问由硬件抽象层负责，而服务层提供：操作系统服务、车辆网络通信与管理服务、存储服务（NVRAM 管理）、诊断服务（包括 KWP2000 接口和错误存储器）、ECU 状态管理。任务：为应用和基础软件模块提供基础服务。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Session**
> 日志或跟踪消息来源的一个逻辑实体；如果一个应用/**SW-C** 打开了多个到 **Dlt** 的端口，则它可以拥有多个并发的日志或跟踪会话。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Session ID**
> 一个日志或跟踪会话的标识编号。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Setter**
> 允许对字段进行写访问的请求/响应调用。
>
> 来源：[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）、[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**SEv**
> 安全事件（**Security Event**）——由 **BSW** 或 **SWC** 向 **IdsM** 上报的安全事件类型的实例。
>
> 来源：[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）、[Requirements on Firewall（防火墙需求）](foundation/security/rs_firewall/index.md)（AUTOSAR_FO_RS_Firewall）
{: .glossary-source}

**SF**
> 单帧，传输协议术语。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）、[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**SF_DL**
> 单帧数据长度（字节）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**SFR**
> 特殊功能寄存器（**Special Function Register**），**MCU** 寄存器
>
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](cp/mcal/mcu_driver/index.md)（SWS_MCUDriver）、[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）
{: .glossary-source}

**SGW**
> 时间同步的「已同步到网关」（**Synchronized to Gateway**）状态。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**SHB**
> 单跳广播（**Single Hop Broadcast**）。
>
> 来源：[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**SHE**
> 安全硬件扩展（**Security Hardware Extension**）。
>
> 来源：[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）
{: .glossary-source}

**SHM**
> 系统健康监控器（**System Health Monitor**）——跨多个平台聚合与转发健康信息的平台无关组件。
>
> 来源：[Requirements on Health Monitoring（健康监控需求）](foundation/health_monitoring/rs_health_monitoring/index.md)（AUTOSAR_FO_RS_HealthMonitoring）
{: .glossary-source}

**SID**
> 服务标识符（**Service Identifier**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**SIEM**
> 安全事件与事件管理（**Security Incident and Event Management**）系统，作为安全运营中心的一部分，解读从 **IdsM** 实例接收到的二进制数据。
>
> 来源：[Requirements on Security Extract Template（安全提取模板需求）](foundation/methodology_templates/rs_security_extract_template/index.md)（AUTOSAR_FO_RS_SecurityExtractTemplate）、[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）
{: .glossary-source}

**Signal**
> 在AUTOSAR COM模块的上下文中，信号（**Signal**）等同于[3]中的消息；另见[1]。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**signal**
> 见[3]。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Signal group**
> 在AUTOSAR中使用所谓的复杂数据类型（**complex data types**）。在复杂数据类型内部，有一个或多个数据元素（基本数据类型），就像C结构体一样。这种复杂数据类型的数据一致性必须得到保证。用户（如**RTE**或**SwCluC**）将复杂数据类型分解为单个信号并将其发送给AUTOSAR COM模块。由于这些信号需要被一致地处理，它们被称为信号组（**signal group**）。另见[1]。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**signal group**
> 见[3]。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**Signal Service Translation**
> 信号服务转换（**Signal Service Translation**）是将基于信号的通信的定义映射到面向服务的通信、以及反向映射的标准化方式。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**SIL**
> 安全完整性等级（**Safety Integrity Level**），**IEC 61508** 定义。
>
> 来源：[Requirements on Methodology（方法论需求）](foundation/methodology_templates/rs_methodology/index.md)（AUTOSAR_FO_RS_Methodology）
{: .glossary-source}

**Single connection**
> CAN传输层一次只管理一个传输协议通信会话。
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Single Shot**
> 与连续传输相反，消息将仅被传输一次。
>
> 来源：[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**SL-LET**
> 系统级逻辑执行时间（**System Level Logical Execution Time**）——跨平台描述时间确定性数据流的 **LET** 扩展，指向被交换的数据类型。
>
> 来源：[Requirements on Timing Extensions（时序扩展需求）](foundation/methodology_templates/rs_timing_extensions/index.md)（AUTOSAR_FO_RS_TimingExtensions）
{: .glossary-source}

**Slave Switch**
> 从交换机（**Slave Switch**）是通过上行端口连接到主交换机的以太网交换机。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Slave-to-slave**
> 从 LIN 主节点的角度来看，LIN 总线上存在 3 种不同方向的帧：主节点发送的响应、主节点接收的响应和一个从节点发送并由另一个从节点接收的响应。**slave-to-slave** 描述的是最后一个。这在 ISO 17987 规范中没有明确描述，但在 ISO 17987-3 中的图 14 中提到：三个无条件帧传输。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**Slot Delay**
> 调度表中帧开始之间的时间。单位是特定集群的时基数。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**Slow-Mode**
> 对看门狗硬件的触发可以以较长的超时期限完成。例如，该模式可用于系统启动/初始化阶段。例如，看门狗硬件被配置为翻转模式（对触发的时间点没有约束）且超时期限为 20 毫秒。
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](cp/safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**SN**
> 序列号（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）、[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**SNA**
> 信号不可用（**Signal Not Available**），在 **SAE J1939 PG**/**参数** 中所有位置 1。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**SNI**
> 源节点标识符（**Source Node Identifier**）
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**SoAd**
> 套接字适配器（**Socket Adaptor**）。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR EthSM（以太网状态管理器）](cp/communication/ethsm/index.md)（AUTOSAR_CP_SWS_EthernetStateManager）、[Intrusion Detection System Protocol Specification（入侵检测系统协议规范）](foundation/protocols/prs_intrusion_detection_system/index.md)（AUTOSAR_FO_PRS_IntrusionDetectionSystem）
{: .glossary-source}

**SOC**
> 安全运营中心（**Security Operation Center**）。
>
> 来源：[Requirements on Security Extract Template（安全提取模板需求）](foundation/methodology_templates/rs_security_extract_template/index.md)（AUTOSAR_FO_RS_SecurityExtractTemplate）、[Requirements on Intrusion Detection System（入侵检测系统需求）](foundation/security/rs_intrusion_detection_system/index.md)（AUTOSAR_FO_RS_IntrusionDetectionSystem）、[Requirements on Firewall（防火墙需求）](foundation/security/rs_firewall/index.md)（AUTOSAR_FO_RS_Firewall）
{: .glossary-source}

**Software Cluster**
> 将所有与在机器上部署软件相关的 AUTOSAR 工件归为一组（**Software Cluster**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**Software Cluster (Adaptive Platform)**
> 自适应平台软件集群（**Software Cluster**）将所有与在自适应平台机器（**Machine**）上部署相关的 AUTOSAR 制品分组在一起。软件集群的内容取决于其类别，"可以"（但不限于）包含诸如以下制品：• 自适应平台应用（可执行文件） • 自适应平台功能簇（模块） • 清单 • 持久化存储数据库 • 平台库，例如转换器（**Transformers**）、加密（**Cryptographics**） • 引导加载程序
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Software Cluster Connection**
> 提供以下特性的 BSW 模块：连接部署在同一机器上的二进制对象、通过代理模块替代应用软件集群中缺失的 BSW 模块、与 RTE 一起通过 RTE 实现插件实现软件集群之间的 VFB 通信（**Software Cluster Connection**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**Software Cluster Connector**
> 读取未连接的二进制清单的信息并计算可修改的二进制清单部分（**Software Cluster Connector**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**Software Component**
> 软件组件（**Software Component**）是提供和/或需要接口的架构元素，它们通过虚拟功能总线彼此连接，以履行架构职责。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Software Component Interface**
> 软件组件接口（**SW-CI**）是"基础软件"（**Basic Software**）向"软件组件"（**Software Component**）提供的全部接口的总和。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Software Configuration**
> SW 系统中软件元素的布置。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Software Interrupt**
> 由软件事件触发的中断。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Software Package**
> 用于将软件部署到自适应 AUTOSAR 平台实例上的单元，包含零个或多个可执行文件以及在该机器（**Machine**）上安装和执行它们的元数据。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Software Platform**
> 执行应用软件的软件环境。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Software Signal**
> 软件信号（**Software Signal**）是在进程与进程之间传输的异步事件。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Software Trigger**
> 软件触发是一个软件**API**调用，用于启动转换一个**ADC**通道组或一系列连续**ADC**通道组转换的。
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）
{: .glossary-source}

**Software Unit**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.125
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**SOME/IP**
> 可扩展的面向服务的基于IP的中间件（**Scalable service-Oriented MiddlwarE over IP**）。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）、[AUTOSAR SomeIpXf（SOME/IP转换器）](cp/communication/someipxf/index.md)（AUTOSAR_CP_SWS_SOMEIPTransformer）、[AUTOSAR SomeIpTp（SOME/IP传输协议）](cp/communication/someiptp/index.md)（AUTOSAR_CP_SWS_SOMEIPTransportProtocol）、[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Requirements on SOME/IP Protocol（SOME/IP 协议需求）](foundation/protocols/rs_someip_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPProtocol）
{: .glossary-source}

**SOME/IP-SD**
> SOME/IP服务发现（**SOME/IP Service Discovery**）。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**SOTA**
> 软件远程升级（**Software Over The Air**），使用无线通信进行软件远程更新。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**SOTIF**
> 预期功能安全（**Safety Of The Intended Functionality**）。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**SP**
> 传感器池（**Sensor Pool**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**SPAL**
> 标准外围抽象层（**Standard Peripheral Abstraction Layer**）。
>
> 来源：[AUTOSAR CAN Driver（CAN驱动程序）](cp/communication/can_driver/index.md)（AUTOSAR_CP_SWS_CANDriver）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**SPAT**
> 信号相位与时间（**Signal Phase And Time**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**SPATEM**
> 信号相位与配时扩展消息（**Signal Phase And Timing Extended Message**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**SPD**
> 安全策略数据库（**Security Policy Database**），**IPsec** 的数据库。
>
> 来源：[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**SPDU**
> 安全协议数据单元（**Secured protocol data Unit**）。
>
> 来源：[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）
{: .glossary-source}

**Special Periphery Access**
> 访问标准外设设备或特殊外设的特殊函数。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**SPEM**
> 软件过程工程元模型（**Software Process Engineering meta-model**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**SPI**
> 串行外设接口（**Serial Peripheral Interface**）
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](cp/safety/watchdog_driver/index.md)（SWS_WatchdogDriver）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**SPI Channel**
> 通道是按相同准则定义的数据的软件交换媒介：配置参数、具有相同大小的数据元素的数量以及数据指针（源与目标）或位置。更多细节参见 SPI 驱动程序规范。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）
{: .glossary-source}

**SPI Job**
> 一个作业由一个或多个具有相同片选的通道组成。作业被认为是原子的，因此不能被中断。 作业也具有指定的优先级。 有关详细信息，请参阅SPI驱动程序规范。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）
{: .glossary-source}

**SPI Sequence**
> 一个序列是要传输的多个连续作业。 序列取决于静态配置。 有关详细信息，请参阅 SPI 驱动程序规范。
>
> 来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）、[AUTOSAR CAN Transceiver Driver](cp/communication/can_transceiver_driver/index.md)（AUTOSAR_CP_SWS_CANTransceiverDriver）
{: .glossary-source}

**SPN**
> 可疑参数编号（**Suspect Parameter Number**），**SAE J1939** 参数的唯一标识符。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）、[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）、[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](cp/diagnostics/j1939dcm/index.md)（SWS_SAEJ1939DiagnosticCommunicationManager）
{: .glossary-source}

**Sporadic frame**
> 这是附加到偶发时隙（**Sporadic slot**）的一种无条件帧。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**Sporadic slot**
> 这是偶发帧（**Sporadic frame**）的占位符。将其命名为时隙（**slot**）的原因是它没有 LIN 帧的 ID。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**SPRMIB**
> 正响应消息指示位抑制（**suppressPosRspMsgIndicationBit**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**SR**
> 态势识别（**Situation Recognition**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**SRC**
> 监督参考周期（**Supervision Reference Cycle**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**&lt;SrcLo&gt;**
> 作为 L-SDU 源的下层通信接口模块。SrcLo 始终只有一个。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**&lt;SrcLoTp&gt;**
> 下层传输协议模块，作为**I-PDU**的来源。**SrcLoTp**始终只有一个。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**SRF**
> 从节点的响应帧（**Slave Response Frame**）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**SRS**
> 软件需求规范（**Software Requirement Specification**）
>
> 来源：[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**SRS（Safety Restraint System）**
> 安全约束系统（**Safety Restraint System**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**SRS（Software Requirements Specification）**
> Software Requirements Specification —— 软件需求规范。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）、[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**SSCI**
> 短安全通道标识符（**Short Secure Channel Identifier**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）
{: .glossary-source}

**SSCP**
> 同步服务器调用点（**synchronous server call point**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**SSM**
> 静止管理（**Stand Still Manager/Management**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Standard Periphery Access**
> 针对汽车嵌入式应用中使用的 ECU（大多数为微控制器集成）上可用的典型标准外设设备的标准函数。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Standard Software**
> 标准软件（**Standard Software**）是在 ECU 上提供独立于原理图的基础设施功能的软件。它只包含标准化的 AUTOSAR 接口（**Standardized AUTOSAR Interface**）、标准化接口（**Standardized Interface**）和/或私有接口（**Private Interface**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Standardized AUTOSAR Blueprint**
> 标准化 AUTOSAR 蓝图（**Standardized AUTOSAR Blueprint**）是在 AUTOSAR 项目内标准化的"蓝图"（**Blueprint**）。其派生对象也被视为在 AUTOSAR 项目内标准化。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Standardized AUTOSAR Interface**
> 这是在 AUTOSAR 项目内标准化的 AUTOSAR 接口（**AUTOSAR Interface**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Standardized Blueprint**
> 如果"蓝图"（**Blueprint**）的派生对象也被视为标准化，则该蓝图称为标准化蓝图（**Standardized Blueprint**）。它还包括：额外存在具体的标准化规则，规定如何规定蓝图以及如何从该蓝图派生对象。这通常不是针对某个特定蓝图，而是针对同一类的所有蓝图进行的。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Standardized Interface**
> 如果存在具体的标准化 API，则软件接口称为标准化接口（**Standardized Interface**）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**State Management (SM)**
> 状态管理（**State Management**）。
>
> 来源：[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）
{: .glossary-source}

**Static Configuration**
> 路由配置在网关正常运行期间无法改变的设置。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**static part**
> 见[2]。
>
> 来源：[AUTOSAR IpduM（I-PDU多路复用器）](cp/communication/ipdum/index.md)（AUTOSAR_CP_SWS_IPDUMultiplexer）
{: .glossary-source}

**StbM**
> 同步时基管理器（**Synchronized Time-Base Manager**）。向其客户提供与分布式系统其他节点上的时基同步的时基的基础软件模块。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**STD**
> 标准（**Standard**）
>
> 来源：[AUTOSAR Standard Types（标准类型）](cp/general/standard_types/index.md)（SWS_StandardTypes）
{: .glossary-source}

**STF**
> 起始帧（Start Frame，请参阅 ISO 10681-2）。
>
> 来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](cp/communication/flexray_iso_transport_layer/index.md)（SWS_FlexRayISOTransportLayer）
{: .glossary-source}

**STIM**
> Data Stimulation packet —— 数据激励包。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**STmin**
> 发送方在两次CF传输之间需等待的最短时间（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**STMS**
> Timestamp —— 时间戳。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Stop Offer**
> 停止提供一个服务实例的消息。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Sub Address Area**
> 子地址区（**Sub Address Area**）是指逻辑地址空间中的连续存储区域，并映射到一个存储设备的一个扇区批次（**Sector Batch**）。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**Substitution Software Cluster**
> 出于缺陷修复目的可以覆盖其他软件集群所提供资源的唯一软件集群（**Substitution Software Cluster**）。
>
> 来源：[Software Cluster Connection（软件集群连接）](cp/system_services/software_cluster_connection/index.md)（AUTOSAR_CP_SWS_SoftwareClusterConnection）
{: .glossary-source}

**Supervised Entity**
> 被纳入**WdgM** 监督的软件实体。每个**被监督实体**恰好具有一个标识符。**被监督实体**表示软件组件类型或基础软件模块某个实例内的一组**检查点**。在一个软件组件类型或基础软件模块的实例中，可以有零个、一个或多个**被监督实体**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Supervised Entity Identifier**
> 在一个应用内唯一标识某个**被监督实体**的**标识符**。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Supervision Counter**
> 在**被监督实体**上下文内的独立数据资源，由**WdgM** 在每个**监督周期**期间更新，并被**存活监督**算法用于执行对已计数**存活指示**的检查。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Supervision Cycle**
> **WdgM****监督参考周期**的时基，在其中执行周期性的**存活监督**。它同时也是更新**全局监督状态**以及执行由此产生的恢复动作的间隔。这在所属 **WdgM** 的主函数每次被调用时完成，并且依赖于模式（在切换模式时可能变化）。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**Supervision Mode**
> 微控制器或虚拟机的整体状态，或（在 **Adaptive Platform** 情况下）功能组的状态。各模式互斥；模式例如可以是 Startup、Shutdown、Low power。
>
> 来源：[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**Supervision Reference Cycle**
> **存活监督**用于执行已计数**存活指示**检查所使用的**监督周期**数量（对每个**被监督实体**分别确定），并且依赖于模式。
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**SVN**
> Subversion（版本控制系统）（**Subversion**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**SW**
> 软件（**Software**）
>
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](cp/io/adc_driver/index.md)（SWS_ADCDriver）、[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR Crypto Driver（加密驱动程序）](cp/crypto/crypto_driver/index.md)（SWS_CryptoDriver）、[AUTOSAR Crypto Interface（加密接口）](cp/crypto/crypto_interface/index.md)（SWS_CryptoInterface）、[AUTOSAR Crypto Service Manager（加密服务管理器）](cp/crypto/crypto_service_manager/index.md)（SWS_CryptoServiceManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR LinTrcv（LIN 收发器驱动程序）](cp/communication/lintrcv/index.md)（AUTOSAR_CP_SWS_LINTransceiverDriver）
{: .glossary-source}

**SW-C**
> （应用的）AUTOSAR 软件组件（**AUTOSAR Software Component (of the Application)**）。
>
> 来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）、[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**SWC**
> 软件组件（**SoftWare Component**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）
{: .glossary-source}

**SWCD**
> 软件组件描述（**Software Component Description**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**SwClu**
> 软件集群——将在一台机器上部署软件相关的所有 AUTOSAR 产物分组在一起的独立构建单元（**Software Cluster**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](cp/system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**SwCluC**
> 软件集群连接（**Software Cluster Connection**）
>
> 来源：[Software Cluster Design and Integration Guideline for Classic Platform（经典平台软件集群设计与集成指南）](cp/system_services/sw_cluster_design_and_integration/index.md)（AUTOSAR_CP_EXP_SwClusterDesignAndIntegrationGuideline）
{: .glossary-source}

**SWCo**
> 软件组合（**Software Composition**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**SWS**
> Software Specification —— 软件规范。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**Symbolic name**
> ECU信号的符号名称（**Symbolic name**）在**I/O**硬件抽象模块中是用来建立链接的。（包括：功能、引脚等）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）
{: .glossary-source}

**SYNC Ingress Processing Delay**
> 在 Timesync 模块一侧，从 **SYNC** 报文进入到通过 StbM_BusSetGlobalTime 将接收时间元组转发给 **StbM** 之间的时间区间。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**SYNC message**
> 时间同步报文（**Time Synchronization message**）。
>
> 来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](cp/globaltime/can_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverCAN）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Synchronization Points**
> 用于同步在同一 LET 区间内执行的不同任务的 EE 的执行。同步点（**Synchronization Point**）实现属于不同 EEC 的 EE 的执行顺序。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Synchronize**
> 使两个或多个事件或操作在同一预定义时刻发生。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Synchronized Time Base**
> 通过 Timesync 报文与其他节点上的时基同步的时基，由时基标识符 0..127 标识。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Synchronized（同步）**
> 只要 ((!vPOC!Freeze) && (vPOC!State == NORMAL_ACTIVE) || (vPOC!State == NORMAL_PASSIVE)) 成立，就认为 FlexRay CC 与其所连接的 FlexRay 集群同步。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

**Synchronous Communication**
> 当调用方软件实体被阻塞、直到被调用的操作完成求值时，该通信是同步的。调用方软件实体通过获得结果继续其操作。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Synchronous Function**
> 如果某函数所描述的功能在该函数返回调用者时保证已完成，则该函数称为同步函数。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**SyncLocal Time Tuple**
> 时间元组 [TL_Sync, TV_Sync]，在 TV_Sync 时刻导出，或按公式 7.1 计算，或在支持时从受控硬件时钟导出。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**System**
> 车辆中软件相关部分的表示，以及它们彼此通信的方式。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**System Constraint**
> 限制（汽车 E/E）系统设计自由度的边界条件。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**System Description**
> 系统描述（**System Description**）。以 `System` 为顶层元素描述系统内容的设计工件；抽象平台、经典平台与自适应平台各自使用 `category` 区分的系统描述。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**System Health Monitor**
> 系统健康监控器（**System Health Monitor**, SHM）分析子系统的健康状况。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**System Health Monitor (SHM)**
> **系统健康监控器**组件允许在若干 **Classic**、**Adaptive** 或任意第三方平台之间对错误处理进行系统级协调。
>
> 来源：[Explanation of System Health Monitoring（系统健康监控说明）](foundation/health_monitoring/exp_system_health_monitoring/index.md)（AUTOSAR_FO_EXP_SystemHealthMonitoring）、[Specification of Health Monitoring（健康监控规范）](foundation/health_monitoring/asws_health_monitoring/index.md)（AUTOSAR_FO_ASWS_HealthMonitoring）
{: .glossary-source}

**System Signal**
> 系统信号（**System Signal**）表示通信系统对驻留在不同 ECU 上的 SW 组件之间交换的数据的视图。系统信号允许以扁平化的结构表示这种通信，为每个 SW 组件实例发送或接收的数据元素定义（至少）一个系统信号。如果数据必须经由网关发送，仍然只有一个系统信号表示该数据。数据在各个通信系统上的表示由簇信号（**Cluster Signal**）完成。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**System User**
> 一种管理功能（一个在 ComM 内部上下文中生成的特定「用户」），用于发起默认请求以及覆盖用户请求（**An administration functionality for making a default request and for overriding the user requests**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**Systematic Fault**
> 参见 ISO-DIS-26262-Part-1（[7]），ID 1.131
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**SystemDesignTime variability**
> 由最迟绑定时间为 `SystemDesignTime` 的 `VariationPoint` 或 `AttributeValueVariationPoint` 定义的可变性（**SystemDesignTime variability**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Systems Modelling Language**
> 系统建模语言（**Systems Modelling Language**，**SYSML**）。面向系统工程的通用建模语言。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

## T

**Target time**
> 目标时间：到达该值时应有某事发生。其行为取决于配置和已启用的功能。
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**Task**
> 任务（**Task**）是由 OS 管理的最小可调度单元。OS 决定哪个任务何时可以在 ECU 的 CPU 上运行。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Task body**
> 使用宏 `TASK` 定义的任务函数（**Task body**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**TC**
> 流量类别（**Traffic Class**）。
>
> 来源：[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**TCP**
> Transmission Control Protocol —— 传输控制协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**TCP socket connection**
> 使用 TCP 作为传输协议的套接字连接（选择容器 **SoAdSocketProtocol** 包含 **SoAdSocketTcp** 子容器）。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](cp/communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**TCP/IP**
> 计算机网络中使用的一族通信协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**TCP/IP Stack**
> Ethernet communication stack，以太网通信栈。
>
> 来源：[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）
{: .glossary-source}

**TCS**
> 牵引力控制系统（**Traction Control System**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**Technical Signal**
> 技术信号（**Technical Signal**）是与 AUTOSAR 系统耦合的外部事件的物理值。技术信号以 SI 单位表示（例如压力以 Pa 表示）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**test interval**
> **CoreTest** 测试间隔：在配置为构成一个完整内核测试的硬件资源上（后台模式下执行的）所有部分测试的总和。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Test Interval Id**
> 测试间隔的标识符，每开始一个新的测试间隔时应递增。
>
> 来源：[AUTOSAR CoreTest（内核测试）](cp/mcal/core_test/index.md)（SWS_CoreTest）
{: .glossary-source}

**Tick**
> 定义定时器分辨率，即定时器一次递增的持续时间。
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）、[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）
{: .glossary-source}

**Time Base Customer**
> 同步时基管理器支持的 3 种时基客户：主动型客户、触发型客户、通知型客户。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Time Gateway**
> 被一个时基从节点和一个或多个时基主节点引用的时基；Timesync 报文不直接穿过时间网关路由，因为路由延迟需要被补偿。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Time Master**
> 某时基的主节点实体，作为该时基的源，将其传播给通信网络某个区段内的一组时基从节点。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Time Offset**
> 施加速率校正之后仍然残留的时间偏移。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Time Service Predef Timer**
> 时间服务预定义定时器：一种自由运行的计数器，具有预定义的物理时间单位和范围；硬件定时器的功能基于相应的 **GPT** 预定义定时器。时间服务模块为每个预定义定时器提供一组 **API** 服务，用户可以实例化任何计时器（仅受可用内存限制）并完全独立地使用这些实例。
>
> 来源：[AUTOSAR Time Service（时间服务）](cp/system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**Time Slave**
> 基于由相应 Timesync 模块提供的全局时基值来更新其内部维护的本地时基的角色。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）、[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**Time Triple**
> 在时间元组的基础上加入对应的备用虚拟本地时间作为第三个成员而得到。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Time Tuple**
> Timesync 栈始终通过时间元组结构管理时基的时间，即在同一时间点采样的全局时间采样与虚拟本地时间采样。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Timed Communication**
> 在 LET 区间末尾逻辑发布、在 LET 区间开头逻辑读取的隐式通信。对于通过 EEC 引用该 LET 区间的所有 EE，都可以访问定时通信（**Timed Communication**）缓冲区。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Timeout**
> 针对事件或任务的截止期限违反而给出的通知（例如在处理信息期间：接收、发送、处理等）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Timer channel**
> 表示分配给一个定时器硬件的逻辑定时器实体。
>
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](cp/mcal/gpt_driver/index.md)（SWS_GPTDriver）
{: .glossary-source}

**Timer instance**
> 定时器实例：由 **API** 数据类型 Tm_PredefTimer...bitType 所对应的一个数据对象，即用户软件级别上的时间服务预定义定时器的实例化。
>
> 来源：[AUTOSAR Time Service（时间服务）](cp/system_services/time_service/index.md)（SWS_TimeService）
{: .glossary-source}

**Timesync**
> 时间同步（**Time Synchronization**）。
>
> 来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](cp/globaltime/fr_tsyn/index.md)（AUTOSAR_CP_SWS_TimeSyncOverFlexRay）
{: .glossary-source}

**TLM**
> 交通灯操控（**Traffic Light Maneuver**）。
>
> 来源：[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**TLS**
> 传输层安全（**Transport Layer Security**）。
>
> 来源：[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）
{: .glossary-source}

**TLV**
> 标签-长度-值（**Tag-Length-Value**）。
>
> 来源：[AUTOSAR Mka（MACsec 密钥协商）](cp/communication/macsec/index.md)（AUTOSAR_CP_SWS_MACsecKeyAgreement）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**TM**
> 传输模式（**Transmission Mode**）。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**TMC**
> 传输模式条件（**Transmission Mode Condition**），见第6.3.3.2节。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**TMS**
> 传输模式选择器（**Transmission Mode Selector**），见第6.3.3.2节。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**TO**
> 发送机会（**Transmit Opportunity**）。
>
> 来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](cp/communication/eth_trcv/index.md)（SWS_EthernetTransceiverDriver）
{: .glossary-source}

**Top-level PNC Coordinator**
> 顶层 PNC 协调器（**Top-level PNC Coordinator**）是 PN 拓扑中的最顶层协调器，是构成特定 PNC 的逻辑部分网络集群的有向无环图的唯一根。顶层 PNC 协调器负责所有 PNC 成员的协调关机，因为它是唯一拥有所有 PNC 状态完整概览的节点。只有 PNC 顶层协调器才允许发送 PN 关机报文。注意，对于不同的 PNC，可以有不同的顶层 PNC 协调器。对于同一个 PNC，只支持一个顶层协调器。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Top-level PNC coordinator**
> 一个ECU，对在其所有已分配通道上被主动协调的那些PNC充当顶层PNC协调器。该ECU启用了PNC网关功能。如果没有网络中的其他ECU请求这些PNC且同步PNC关闭已启用，顶层PNC协调器会为这些PNC触发一次同步PNC关闭。注意：对于不同的PNC，可以有不同的顶层PNC协调器。但对于同一个PNC只支持一个顶层协调器。
>
> 来源：[AUTOSAR Nm（网络管理接口）](cp/communication/nm/index.md)（AUTOSAR_CP_SWS_NetworkManagementInterface）
{: .glossary-source}

**TP**
> 传输协议（**Transport Protocol**）
>
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](cp/general/communication_stack_types/index.md)（SWS_CommunicationStackTypes）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）、[AUTOSAR Chinese V2X Management（中国V2X管理）](cp/communication/chinesev2x_mgmt/index.md)（AUTOSAR_CP_SWS_ChineseV2XManagement）
{: .glossary-source}

**TP-PDU**
> 通过 SoAd 的 TP-API 发送/接收的 PDU。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](cp/communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**TP.CM**
> 连接管理消息（**Connection Management message**）（**PGN** = 0x0EC00），由 **SAE J1939** 传输协议使用，对应于传输层的一个 **N-PDU**。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**TP.CM_BAM**
> **Broadcast Announce Message**，**TP.CM** 的变体，发起一次 **BAM** 传输。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**TP.CM_CTS**
> **Connection Mode Clear To Send**，**TP.CM** 的变体，在 **CMDT** 传输期间用于握手。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**TP.CM_EndOfMsgAck**
> **End Of Message Acknowledge**，**TP.CM** 的变体，确认一次 **CMDT** 传输的正确接收。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**TP.CM_RTS**
> **Connection Mode Request To Send**，**TP.CM** 的变体，发起一次 **CMDT** 传输。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**TP.Conn_Abort**
> 连接中止（**Connection Abort**），**TP.CM** 的变体，终止一次 **CMDT** 传输。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**TP.DT**
> 数据传输消息（**Data Transfer message**）（**PGN** = 0x0EB00），由 **SAE J1939** 传输协议使用，对应于传输层的一个 **N-PDU**。
>
> 来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](cp/communication/j1939tp/index.md)（AUTOSAR_CP_SWS_SAEJ1939TransportLayer）
{: .glossary-source}

**Trace Message**
> 包含已经过 **VFB** 的信息的消息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Trace status**
> 提供是否应发送跟踪消息的信息。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Tracing**
> 跟踪（**Tracing**）是在一定时间段内记录程序在系统中的可观测状态和执行路径的活动。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Transaction authentication**（事务认证）
> 事务认证表示消息认证，额外提供数据的唯一性和时效性（从而防止不可检测的消息重放）。
>
> 来源：[AUTOSAR SecOC (Secure Onboard Communication)](cp/communication/sec_oc/index.md)（AUTOSAR_CP_SWS_SecOc）
{: .glossary-source}

**TransformationTechnology**
> **TransformationTechnology** 是 [4] 中定义的一个特定类。该类保存转换器（不仅是 **E2E** 转换器）的通用配置参数。
>
> 来源：[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）
{: .glossary-source}

**Trigger Communication Graph**
> 相互连接的各 `PortPrototype` 中实例化的触发器上的所有 `ExternalTriggeringPoint` 之和，包括所属的被触发可运行实体（**Trigger Communication Graph**）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**trigger emitter**
> 触发器发出者（**trigger emitter**）具有释放触发器的能力，这些触发器进而激活被触发的可执行实体。触发器发出者在元模型中由提供触发器端口、`releasedTrigger` 角色中的 `Trigger`、`InternalTriggeringPoint` 和 `BswInternalTriggeringPoint` 描述。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**trigger port**
> 由 `TriggerInterface` 定义类型的 `PortPrototype`（**trigger port**，触发器端口）。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**trigger sink**
> 触发器汇（**trigger sink**）依赖在某个特定 `Trigger` 被引发时对可运行实体或基础软件可调度实体的激活。触发器汇拥有与触发器源通信的专用需求触发器端口和/或 `requiredTrigger` `Trigger`。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**trigger source**
> 触发器源（**trigger source**）管理特定的 `Trigger`，并在该 `Trigger` 被引发时通知 **RTE** 或基础软件调度器。触发器源拥有与触发器汇通信的专用提供触发器端口和/或 `releasedTrigger` `Trigger`。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**triggered BswSchedulableEntity**
> 由至少一个 `BswExternalTriggerOccurredEvent` 或 `BswInternalTriggerOccurredEvent` 触发的 `BswSchedulableEntity`（**triggered BswSchedulableEntity**）。在特定情况下，触发器事件通信或基础软件可调度实体间触发由基础软件调度器实现为触发方可执行实体对被触发可执行实体的直接或可信函数调用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**triggered ExecutableEntity**
> 由至少一个 `ExternalTriggerOccurredEvent`/`BswExternalTriggerOccurredEvent` 或 `InternalTriggerOccurredEvent`/`BswInternalTriggerOccurredEvent` 触发的可运行实体或基础软件可调度实体（**triggered ExecutableEntity**）。在特定情况下，触发器事件通信或可运行实体间触发由 **RTE** 或基础软件调度器实现为触发方可执行实体对被触发可执行实体的直接或可信函数调用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**triggered runnable**
> 由至少一个 `ExternalTriggerOccurredEvent` 或 `InternalTriggerOccurredEvent` 触发的可运行实体（**triggered runnable**）。在特定情况下，触发器事件通信或可运行实体间触发由 **RTE** 实现为触发方可运行实体对被触发可运行实体的直接或可信函数调用。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Triggered Time Base Customer**
> 由同步时基管理器触发的时基客户；该功能目前仅限于 **OS** ScheduleTable 的同步。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Triggered to NvM**
> 如果需要在 Dem_Init 和 Dem_Shutdown 之间触发数据的存储，**Dem** 模块应使用 **NVRAM** 管理器的 **API** NvM_WriteBlock。此外，如果请求已被接受，**Dem** 模块应等待 NvM_WriteBlock 的肯定响应。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**trusted function call**
> 可信函数调用（**trusted function call**）是经由 **OS** 的 `CallTrustedFunction()` **API** 执行的函数调用。在跨越分区边界时，通常需要它来实现类似直接函数调用的行为。
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**TS**
> Time Stamp —— 时间戳。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**TSB**
> 拓扑范围广播（**Topologically Scoped Broadcast**）。
>
> 来源：[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**TSCF**
> 时间敏感控制格式（**Time Sensitive Control Format**），由 IEEE 1722 定义。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**TSN**
> 时间敏感网络（**Time-Sensitive Networking**）。
>
> 来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](cp/communication/ieee1722tp/index.md)（AUTOSAR_CP_SWS_IEEE1722TransportLayer）、[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**TSpec**
> 流量规范（**Traffic specification**），定义于 IEEE Std 802.1Q-2022。
>
> 来源：[Requirements on IEEE1722（IEEE 1722 需求）](foundation/communication_management/rs_ieee1722/index.md)（AUTOSAR_FO_RS_IEEE1722）
{: .glossary-source}

**TTCAN Controller**
> TTCAN 控制器恰好服务于一个物理通道。
>
> 来源：[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**TtcanDrv**
> 启用了 **TTCAN** 功能的 **CAN** 驱动程序模块。
>
> 来源：[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**TtcanIf**
> 启用了 **TTCAN** 功能的 **CAN** 接口模块。
>
> 来源：[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](cp/communication/ttcan_driver/index.md)（AUTOSAR_CP_SWS_TTCANDriver）
{: .glossary-source}

**TTL**
> 生存时间（**Time-to-Live**）
>
> 来源：[Requirements on SOME/IP Service Discovery Protocol（SOME/IP 服务发现协议需求）](foundation/protocols/rs_someip_service_discovery_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol）
{: .glossary-source}

**TX**
> 发送（**Transmission**）。
>
> 来源：[AUTOSAR LinIf (LIN Interface)](cp/communication/lin_interface/index.md)（AUTOSAR_CP_SWS_LINInterface）、[AUTOSAR CanSM（CAN状态管理器）](cp/communication/cansm/index.md)（AUTOSAR_CP_SWS_CANStateManager）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**TX_DL**
> 发送数据链路层数据长度
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**Type-prototype**
> 类型-原型模式（**Type-prototype**）。以类型定义、再以原型实例化并聚合到组合中的软件组件建模模式，抽象平台与经典平台一致采用。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

## U

**UART**
> 通用异步收发器（**Universal Asynchronous Receiver Transmitter**）
>
> 来源：[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**uC**
> 微控制器（**Microcontroller**）
>
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](cp/mcal/mcu_driver/index.md)（SWS_MCUDriver）
{: .glossary-source}

**UDP**
> User Datagram Protocol —— 用户数据报协议。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）、[AUTOSAR TcpIp（TCP/IP协议栈）](cp/communication/tcpip/index.md)（AUTOSAR_CP_SWS_TcpIp）、[AUTOSAR V2X Basic Transport（V2X基本传输协议）](cp/communication/v2x_basictp/index.md)（AUTOSAR_CP_SWS_V2XBasicTransport）、[AUTOSAR V2X GeoNetworking（V2X地理网络）](cp/communication/v2x_geonet/index.md)（AUTOSAR_CP_SWS_V2XGeoNetworking）
{: .glossary-source}

**UDP socket connection**
> 使用 UDP 作为传输协议的套接字连接（选择容器 **SoAdSocketProtocol** 包含 **SoAdSocketUdp** 子容器）。
>
> 来源：[AUTOSAR SoAd (Socket Adaptor)](cp/communication/soad/index.md)（SWS_SocketAdaptor）
{: .glossary-source}

**UDP/IP**
> User Datagram Protocol / Internet Protocol —— 用户数据报协议/互联网协议。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**UdpNm**
> UDP网络管理（**UDP Network Management**）
>
> 来源：[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

**UDS**
> 统一诊断服务（**Unified Diagnostic Services**）。
>
> 来源：[AUTOSAR FiM（功能禁止管理器）](cp/system_services/function_inhibition_manager/index.md)（SWS_FunctionInhibitionManager）、[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**UDS Service**
> 指 **ISO 14229-1** 中定义的 **UDS** 服务。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

**UDS status byte**
> 按 ISO 14229-1 定义、基于 **DTC** 级别的状态字节。
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**UEH**
> Use Extended Header —— 使用扩展头。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**UI**
> 用户界面（**User Interface**）
>
> 来源：[Explanation of Application Interfaces of the HMI, Multimedia and Telematics Domain（HMI/多媒体/远程信息处理域应用接口说明）](cp/application_interfaces/hmi/index.md)（AUTOSAR_CP_EXP_AIHMIMultimediaAndTelematics）
{: .glossary-source}

**UL**
> 上层（**Upper layer**）。
>
> 来源：[AUTOSAR TTCAN Interface（TTCAN 接口）](cp/communication/ttcan_interface/index.md)（AUTOSAR_CP_SWS_TTCANInterface）
{: .glossary-source}

**UML**
> 统一建模语言（**Universal Modelling Language**）
>
> 来源：[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**unconnected port**
> 未被任何 `AssemblySwConnector` 和/或 `DelegationSwConnector` 引用的 `RPortPrototype` 或 `PPortPrototype`，或其端口接口的元素中至少没有任何 `DataMapping` 的端口（**unconnected port**，未连接端口）。提示：`PRPortPrototype` 始终被视为已连接端口。（见 **SWS_Rte_06030**）
>
> 来源：[AUTOSAR RTE（运行时环境）](cp/rte/rte/index.md)（AUTOSAR_CP_SWS_RTE）
{: .glossary-source}
**Unicast event**
> 由承载**SdServerService**的ECU发送到单播端点的事件。该单播端点由已在Endpoint Option（见「Consumed Eventgroup unicast endpoint」）中引用的、订阅了该SdServerService的特定SdClientService提供。
>
> 来源：[AUTOSAR SD（服务发现）](cp/communication/service_discovery/index.md)（AUTOSAR_CP_SWS_ServiceDiscovery）
{: .glossary-source}

**Union**
> 联合（**Union**）——动态采用不同数据类型的数据结构。
>
> 来源：[Requirements on SOME/IP Protocol（SOME/IP 协议需求）](foundation/protocols/rs_someip_protocol/index.md)（AUTOSAR_FO_RS_SOMEIPProtocol）
{: .glossary-source}

**&lt;Up&gt;**
> 上层通信接口模块。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）、[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

**Update-bit**
> 更新位（**Update-bit**）是AUTOSAR COM模块支持的一种机制，信号/信号组的接收者可以借此识别发送者是否在发送之前更新了该信号/信号组中的数据。见第6.9节。
>
> 来源：[AUTOSAR COM（COM模块）](cp/communication/com/index.md)（AUTOSAR_CP_SWS_COM）
{: .glossary-source}

**Updated Rx Time Tuple**
> 时间元组 [TG_URx, TV_URx]，通过在接收时间元组上加入经速率校正的 **SYNC** 进入处理延迟而导出。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**UPER**
> 非对齐打包编码规则（**Unaligned Packed Encoding Rule**）。**ASN.1** 最高效的编码规则。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**Uplink Port**
> 上行端口（**Uplink Port**）是汽车以太网交换机上连接到另一台汽车以太网交换机（级联交换机）的端口。上行端口可以是内部端口或外部端口。一个上行端口连接到另一个上行端口。从软件的角度看，上行端口具有特殊角色。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Upper Layer Modules（Up）**
> 位于 L-SDU Router 之上的模块。该层通常包括 **IEEE1722Tp**。
>
> 来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](cp/communication/lsdu_router/index.md)（SWS_LSduRouter）
{: .glossary-source}

**URL**
> Uniform Resource Locator —— 统一资源定位符。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**Use Case**
> 用例（**Use Case**）定义了一组动作，用于刻画参与者与系统之间为达成某个目标而进行的交互。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**User**
> ECU 状态管理器模块与通信管理器模块的请求方概念。用户可以是 BswM、一个可运行实体、一个 SW-C 或一组 SW-C，它们作为一个整体与 ECU 状态管理器模块及通信管理器模块交互（**Concept for requestors of the ECU State Manager module and of the Communication Manager Module**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**User Request**
> 用户可以向 ComM 请求不同的通信模式（**A User can request different Communication Modes from ComM**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

## V

**V2GTP**
> 车辆到电网传输协议（**Vehicle to Grid Transport Protocol**）。
>
> 来源：[AUTOSAR Charging Manager（充电管理器）](cp/communication/chargingmanager/index.md)（AUTOSAR_CP_SWS_ChargingManager）
{: .glossary-source}

**V2X**
> 车联网（**Vehicle to Everything**）。
>
> 来源：[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cp/communication/cellularv2x_driver/index.md)（AUTOSAR_CP_SWS_CellularV2XDriver）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）、[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）、[Requirements on IPsec Protocol（IPsec 协议需求）](foundation/protocols/rs_ipsec_protocol/index.md)（AUTOSAR_FO_RS_IPsecProtocol）
{: .glossary-source}

**V2xBtp**
> **Vehicle-2-X** 基本传输协议（**Vehicle-2-X Basic Transport Protocol**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**V2xDM**
> **Vehicle-2-X** 数据管理器（**Vehicle-2-X Data Manager**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**V2xFac**
> **Vehicle-2-X** 设施（**Vehicle-2-X Facilities**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**V2xGn**
> **Vehicle-2-X** 地理网络（**Vehicle-2-X Geo Networking**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**V2xM**
> **Vehicle-2-X** 管理（**Vehicle-2-X Management**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**V2xML**
> **Vehicle-2-X** 消息层（**Vehicle-2-X Message Layer**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**V2xNL**
> **Vehicle-2-X** 网络层（**Vehicle-2-X Network Layer**）。
>
> 来源：[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）
{: .glossary-source}

**V2xRAL**
> **V2x** 远程访问层（**V2x Remote Access Layer**）——一个能够通过 **LTE-PC5** 或 **ITS-G5** 与车外单元通信的逻辑单元。
>
> 来源：[V2X Remote Access Layer Protocol Specification（V2X 远程访问层协议规范）](foundation/protocols/prs_v2x_remote_access_layer/index.md)（AUTOSAR_FO_PRS_V2XRemoteAccessLayer）
{: .glossary-source}

**Validation**
> 通过检查和提供客观证据，确认针对特定预期用途的特定要求已得到满足。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Variability**
> 系统的可变性（**Variability**）是系统描述一组变体的性质。这些变体的特征是变体特定的属性设置和/或选择。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Variant**
> 由 **TransformationTechnology** 和 **EndToEndTransformationDescription** 的配置定义的转换器变体。基于同一变体的 **E2E** 转换器使用相同的 **E2E** 配置文件（profile）（参见 [4] 中的 **constr_03313**）。
>
> 来源：[E2E Transformer (E2E转换器)](cp/communication/e2e_transformer/index.md)（AUTOSAR_CP_SWS_E2ETransformer）
{: .glossary-source}

**Variant Coding**
> 根据外部需求（例如国家相关或法律限制），通过选择功能备选项来调整软件。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Variation Binding**
> 变体是变体绑定（**Variation Binding**）过程的结果，该过程通过为系统的所有属性赋以特定的取值/选择来消解系统的可变性。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Variation Binding Time**
> 变体绑定时间（**Variation Binding Time**）确定方法论中由一组可变属性给出的可变性被消解的步骤。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Variation Point**
> 变体点。设计中在 2 个或更多变体之间给出选择的位置；必须做出选择的时间称为最晚绑定时间。
>
> 来源：[VFB（虚拟功能总线）](cp/general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**VB**
> Visual Basic
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**VCD**
> 车辆碰撞检测（**Vehicle Crash Detection**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**VCP**
> 车辆碰撞预测（**Vehicle Crash Prediction**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**VDP**
> 车辆数据提供者（**Vehicle Data provider**）。
>
> 来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](cp/communication/chinesev2x_msg/index.md)（AUTOSAR_CP_SWS_ChineseV2XMessage）、[AUTOSAR Chinese V2X Security（中国V2X安全）](cp/communication/chinesev2x_sec/index.md)（AUTOSAR_CP_SWS_ChineseV2XSecurity）、[AUTOSAR V2X Data Manager（V2X数据管理器）](cp/communication/v2x_datamgr/index.md)（AUTOSAR_CP_SWS_V2XDataManager）、[AUTOSAR V2X Facilities（V2X设施层）](cp/communication/v2x_facilities/index.md)（AUTOSAR_CP_SWS_V2XFacilities）
{: .glossary-source}

**Vehicle State Manager**
> 控制整车级别状态、并与车辆系统中各实体交互的 OEM 特定应用。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Vehicle Variant**
> 车辆变体（**Vehicle Variant**）是一个被完整刻画的产品，是产品线制品的子集。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Vendor ID**
> 供应商 ID（**Vendor ID**）是软件组件供应商的唯一标识。所有符合 AUTOSAR 标准的基础软件模块（**Basic Software Module**）都应提供一个可读的供应商 ID。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**VERB**
> Verbose —— 详细模式。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**Verification**
> 通过检查和提供客观证据，确认规定的要求已得到满足。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**VERS**
> Version Number —— 版本号。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**VFB**
> 虚拟功能总线（**Virtual Functional Bus**）。AUTOSAR 中允许组件相互交互的通信机制；应用被建模为相互连接的组件的组合，组件经由端口与端口接口交互。
>
> 来源：[VFB（虚拟功能总线）](cp/general/vfb/index.md)（AUTOSAR_CP_EXP_VFB）
{: .glossary-source}

**VFB View**
> VFB 视图（**VFB View**）独立于这些资源来描述汽车中的系统或子系统；换句话说，独立于：• 车中存在何种类型、多少个 ECU • VFB 视图中的实体运行在哪些 ECU 上 • ECU 如何互连：使用何种网络技术（CAN、LIN 等）以及何种拓扑（是否存在网关）。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**VFB++**
> 抽象平台 VFB（**Abstract Platform VFB**，**VFB++**）。抽象平台的功能视图，描述组件、端口、接口、连接器的交互，与信号式或服务式架构无关。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**VFC**
> 虚拟功能集群（**Virtual Function Cluster**）。把实现一个或多个车辆功能所需的 SW 组件之间端口层面的通信分组；逻辑视图，允许可复用的、独立于总线/ECU 的设计。在部分组网（Partial Networking）中，VFC 映射到一个或多个部分网络集群（PNC）。
>
> 来源：[Layered Software Architecture（分层软件架构）](cp/general/layered_software_architecture/index.md)（AUTOSAR_CP_EXP_LayeredSoftwareArchitecture）
{: .glossary-source}

**VGR**
> 可变传动比（**Variable Gear Ratio**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**VH**
> 变型处理概念（**Variant Handling concept**）
>
> 来源：[Explanation of Application Interfaces of Occupant and Pedestrian Safety Systems Domain（乘员与行人安全系统域应用接口说明）](cp/application_interfaces/occupant_safety/index.md)（AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety）
{: .glossary-source}

**VIN**
> Vehicle Identification Number —— 车辆识别码。
>
> 来源：[AUTOSAR DoIP（基于 IP 的诊断）](cp/communication/diagnostic_over_ip/index.md)（SWS_DiagnosticOverIP）
{: .glossary-source}

**Virtual Functional Bus**
> 虚拟功能总线（**Virtual Functional Bus**）是"原子软件组件"（**Atomic Software Component**）和"AUTOSAR 服务"（**AUTOSAR Service**）之间通信的抽象。这一抽象使得通信机制的规范独立于为实现通信所选定的具体技术。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Virtual Integration**
> 形成一个"系统"（**System**）的软件实体的仿真、建模和/或计算出来的（非真实的）组合。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Virtual Local Time**
> **StbM** 从硬件时钟导出的本地时间参考，用于全局时间本地实例的推移。
>
> 来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](cp/globaltime/stbm/index.md)（AUTOSAR_CP_SWS_SynchronizedTimeBaseManager）
{: .glossary-source}

**Virtualization**
> 虚拟化（**Virtualization**）是一种向用户隐藏计算平台物理特性、而呈现另一个抽象计算平台的机制。它可以用于实现可用性、分区（**Partitioning**）、资源冲突管理、恢复（**Recovery**）等功能安全需求。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**VLAN**
> Virtual Local Area Network，虚拟局域网。
>
> 来源：[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）
{: .glossary-source}

**VLC**
> 车辆纵向控制（**Vehicle Longitudinal Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**VM**
> 车辆模型（**Vehicle Model**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

**VMC**
> 车辆运动控制（**Vehicle Motion Control**）。
>
> 来源：[Explanation of Application Interface of AD/ADAS Vehicle Motion Control（AD/ADAS 车辆运动控制应用接口说明）](cp/application_interfaces/adas_vmc/index.md)（AUTOSAR_CP_EXP_AIADASAndVMC）
{: .glossary-source}

**VMM**
> 车辆消息矩阵（**Vehicle Message Matrix**）。
>
> 来源：[AUTOSAR Communication Manager（通信管理器）](cp/system_services/comm/index.md)（SWS_COMManager）
{: .glossary-source}

**VOBD**
> 车辆车载诊断（**Vehicle On-Board-Diagnostic**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**VOD**
> 按需验证（**Verification on Demand**）。
>
> 来源：[AUTOSAR V2X Management（V2X管理）](cp/communication/v2x_mgmt/index.md)（AUTOSAR_CP_SWS_V2XManagement）
{: .glossary-source}

**Volkswagen Infotainment Web Interface**
> 大众信息娱乐 Web 接口（**Volkswagen Infotainment Web Interface**，**VIWI**）。大众汽车的信息娱乐 Web 接口。
>
> 来源：[Specification of Abstract Platform（抽象平台规范）](foundation/methodology_templates/tps_abstract_platform_specification/index.md)（AUTOSAR_FO_TPS_AbstractPlatformSpecification）
{: .glossary-source}

**vPOC**
> **CC** 在 **CHI** 处提供给主机的数据结构，包含 **CC** 的实际 **POC** 状态（详情参见 ISO 17458-1）。
>
> 来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](cp/communication/flexray_driver/index.md)（SWS_FlexRayDriver）
{: .glossary-source}

## W

**Wake-up and Sleep on Dataline**
> 通过汽车以太网交换网络的数据线传输的唤醒请求或休眠请求。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**WCET**
> 最坏情况执行时间（**Worst case execution time**）
>
> 来源：[AUTOSAR BSW General（基础软件模块通用规范）](cp/general/bsw_general/index.md)（SWS_BSWGeneral）
{: .glossary-source}

**WDG**
> 看门狗（**Watchdog**，模块特定前缀）
>
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](cp/safety/watchdog_driver/index.md)（SWS_WatchdogDriver）
{: .glossary-source}

**WdgM**
> 看门狗管理器（**Watchdog Manager**）
>
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](cp/safety/watchdog_manager/index.md)（SWS_WatchdogManager）
{: .glossary-source}

**WEID**
> With ECU ID —— 带 ECU ID。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**WEth**
> Wireless Ethernet Driver（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](cp/communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）
{: .glossary-source}

**WEthTrcv**
> Wireless Ethernet Transceiver（**AUTOSAR BSW** 模块）。
>
> 来源：[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](cp/communication/wlan_driver/index.md)（SWS_WirelessEthernetDriver）、[AUTOSAR Ethernet Interface（以太网接口）](cp/communication/ethernet_interface/index.md)（AUTOSAR_CP_SWS_EthernetInterface）
{: .glossary-source}

**WFTmax**
> 接收方允许连续发送的FC.WAIT数量的上限（见ISO 15765-2 [1]）
>
> 来源：[AUTOSAR CanTp（CAN传输层）](cp/communication/cantp/index.md)（AUTOSAR_CP_SWS_CANTransportLayer）
{: .glossary-source}

**WIR**
> 警告指示器请求（**Warning Indicator Request**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**Worst Case Execution Time**
> 程序实际执行的最大可能时间。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**Worst Case Response Time**
> 从接收激励到交付适当响应或反应之间的最大可能时间。
>
> 来源：[TR Glossary（AUTOSAR 术语表）](foundation/general/tr_glossary/index.md)（AUTOSAR_FO_TR_Glossary）
{: .glossary-source}

**WP**
> 工作包（**Work package**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**WPII**
> AUTOSAR 第二阶段的工作包（**Work Package in AUTOSAR phase 2**）
>
> 来源：[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**Write Page**
> 写入页面（**Write Page**）是指存储设备的最小可写单元（以字节为单位）。某些存储设备技术的访问必须考虑物理分段，因此并非所有存储设备技术都支持按字节访问。该术语定义了单次访问所需写入的最小大小。
>
> 来源：[AUTOSAR Memory Access（存储访问）](cp/memory/memory_access/index.md)（AUTOSAR_CP_SWS_MemoryAccess）
{: .glossary-source}

**WSID**
> With Session ID —— 带会话 ID。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**WTMS**
> With Timestamp —— 带时间戳。
>
> 来源：[AUTOSAR Dlt（诊断日志与跟踪）](cp/communication/diagnostic_log_and_trace/index.md)（SWS_DiagnosticLogAndTrace）
{: .glossary-source}

**WUC**
> **OBD** 术语：暖机循环（**Warm up cycle**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

**WWH-OBD**
> 全球统一车载诊断（**World Wide Harmonized On-Board-Diagnostic**）
>
> 来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](cp/diagnostics/diagnostic_event_manager/index.md)（SWS_DiagnosticEventManager）
{: .glossary-source}

## X

**X.509**
> 定义公钥证书格式的 **ITU-T** 标准。
>
> 来源：[AUTOSAR Key Manager（密钥管理器）](cp/crypto/key_manager/index.md)（SWS_KeyManager）
{: .glossary-source}

**XCP**
> Universal Calibration Protocol —— 通用校准协议。
>
> 来源：[AUTOSAR XCP（通用测量与校准协议）](cp/communication/xcp/index.md)（SWS_XCP）
{: .glossary-source}

**XFER**
> **J1939** 传输 **PG**（**Transfer PG**）（**PGN** = 0x0CA00）。
>
> 来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](cp/communication/j1939rm/index.md)（AUTOSAR_CP_SWS_SAEJ1939RequestManager）
{: .glossary-source}

**XLFF**
> XL 帧格式（**XL Frame Format**）。
>
> 来源：[AUTOSAR CAN XL Driver（CAN XL 驱动程序）](cp/communication/canxl_driver/index.md)（SWS_CANXLDriver）
{: .glossary-source}

**XML**
> 可扩展标记语言（**eXtensible Markup Language**）
>
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](cp/io/iohwab/index.md)（SWS_IOHardwareAbstraction）、[AUTOSAR LinSM（LIN 状态管理器）](cp/communication/linsm/index.md)（AUTOSAR_CP_SWS_LINStateManager）
{: .glossary-source}

**XPN**
> 扩展数据包编号（**Extended Packet Number**）——将数据包编号 **PN** 扩展到 64 位的 **MACsec** 特性。
>
> 来源：[Requirements on MACsec（MACsec 需求）](foundation/communication_management/rs_macsec/index.md)（AUTOSAR_FO_RS_MACsec）
{: .glossary-source}

**XSD**
> XML 模式定义（**XML Schema Definition**）
>
> 来源：[Application Interfaces User Guide（应用接口用户指南）](cp/application_interfaces/user_guide/index.md)（AUTOSAR_CP_EXP_AIUserGuide）
{: .glossary-source}

**Xxx_**
> **API** 提供者的占位符（**Placeholder for an API provider**）。
>
> 来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](cp/diagnostics/diagnostic_communication_manager/index.md)（AUTOSAR_CP_SWS_DiagnosticCommunicationManager）
{: .glossary-source}

## Y

**YRC**
> 横摆角速度控制（**Yaw Rate Control**）
>
> 来源：[Explanation of Application Interfaces of the Chassis Domain（底盘域应用接口说明）](cp/application_interfaces/chassis/index.md)（AUTOSAR_CP_EXP_AIChassis）
{: .glossary-source}

## 上

**上层模块(Up)（Upper Layer Modules）**
> PDU路由器模块的上方模块。该层通常包括**Com**和诊断通信管理器 (**Dcm**)。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

## 下

**下层模块(Lo)（Lower Layer Modules）**
> PDU路由器模块的下方模块。该层可能包括**CAN**、**LIN**、**FlexRay**、以太网通信接口模块和相应的**TP**模块。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

## 中

**中间PNC协调员**（**Intermediate PNC coordinator**）
> 中间PNC协调器是一个**ECU**，它充当网络中的PNC网关，并在至少一个分配的通道上将至少一个PNC处理为被动协调。如果启用了同步PNC关闭，它会将收到的这些PNC的关闭请求转发到相应的主动协调通道，并相应地启动它们的关闭。
>
> 来源：[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

**中间PNC协调器**（**Intermediate PNC coordinator**）
> 中间PNC协调器是一个**ECU**，它充当网络中的PNC网关，并在至少一个分配的通道上将至少一个PNC处理为被动协调。如果启用了同步PNC关闭，它会将收到的这些PNC的关闭请求转发到相应的主动协调通道，并相应地启动它们的关闭。
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）
{: .glossary-source}

## 先

**先进先出（FIFO）缓冲**
> 缓冲区概念，采用先进先出策略。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

## 即

**即时传输确认**（**Immediate Transmission Confirmation**）
> 每个NM PDU传输请求都直接被视为已被总线确认，不需要超时处理。该机制可用于那些总线流量经过设计、确保每次传输总能被发送到总线上的总线系统。
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）
{: .glossary-source}

**即时网关（on-the-fly gatewaying）**
> 网关的能力。两个TP 模块之间的路由，其中在接收到所有数据之前（达到指定阈值时）开始转发数据。如果在两个接口之间传输大量数据，则希望能够在从源网络接收所有数据之前在目标网络上开始传输。这样可以节省内存和时间。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

## 多

**多播操作（multicast operation）**
> 将PDU同时传输到一组接收者，即：1:n路由。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

## 数

**数据提供（data provision）**
> 向接口模块提供数据。(a)直接数据提供：需传输的数据直接在传输请求时提供。目标通信接口可能以两种方式运行：直接复制数据或将复制推迟到触发传输。(b)触发传输数据提供：需传输的数据不是在传输请求时提供，而是由通信接口模块通过回调函数获取。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

## 最

**最后最好（last-is-best——缓冲**
> 最新值覆盖最后一个值的缓冲策略。
>
> 来源：[AUTOSAR PduR (PDU Router)](cp/communication/pdu_router/index.md)（AUTOSAR_CP_SWS_PduR）
{: .glossary-source}

## 重

**重复报文请求位指示**（**Repeat Message Request Bit Indication**）
> **CanNm_RxIndication**在收到的网络管理**PDU**的控制位向量中找到**RptMsgRequest**集。
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）
{: .glossary-source}

**重复消息请求位指示**（**Repeat Message Request Bit Indication**）
> **UdpNm_SoAdIfRxIndication**在接收到的**NM**消息的控制位向量中找到重复消息位。
>
> 来源：[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}

## 顶

**顶级PNC协调员**（**Top-level PNC coordinator**）
> 顶级PNC协调器是一个**ECU**，它充当网络中的PNC网关，并在所有分配的通道上主动协调处理至少一个PNC。如果启用了同步PNC关闭，如果网络中没有其他ECU请求它们，顶级PNC协调器将为这些PNC触发关闭。
>
> 来源：[AUTOSAR CAN NM（CAN网络管理）](cp/communication/can_network_management/index.md)（AUTOSAR_CP_SWS_CANNetworkManagement）、[AUTOSAR UdpNm (UDP Network Management)](cp/communication/udp_network_management/index.md)（AUTOSAR_CP_SWS_UDPNetworkManagement）
{: .glossary-source}
