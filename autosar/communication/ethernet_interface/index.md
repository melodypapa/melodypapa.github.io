<section id="title">AUTOSAR Ethernet Interface（以太网接口）</section>

# 1. 简介和功能概述

此规范指定了 **AUTOSAR** 以太网接口基本软件模块的功能、API 和配置。

在AUTOSAR分层软件架构[1]中，以太网接口模块（EthIf）属于ECU抽象层。或者更准确地说，它属于通信硬件抽象。

这表示以太网接口模块的主要任务：

向上层提供以太网通信系统的硬件独立接口，包括多个不同的有线或者无线的以太网控制器和收发器。此接口对于所有以太网控制器和收发器以及蜂窝 **V2X** 控制器需被统一。因此上层模块（**TCP/IP** [2]、**EthSM** [3]、**CDD**、**V2x** 等模块）可以通过统一的方式访问底层总线系统。

以太网接口模块不直接访问以太网硬件（包括：以太网通信控制器和以太网收发器），而是通过一个或多个特定于硬件的驱动程序模块进行间接的。

为了访问以太网控制器（**Ethernet controller**），以太网接口模块需要使用一个或多个以太网驱动程序（**Ethernet Driver**）模块，并且这些模块需抽象出相应的以太网控制器的特定功能和接口。

为了访问以太网收发器（**Ethernet transceiver**），以太网接口模块需要使用一个或多个以太网收发器驱动程序（**Ethernet Transceiver Driver**）模块，并且这些模块需抽象出相应的以太网收发器的特定功能和接口。

为了访问以太网交换机（**Ethernet switch**），以太网接口模块需要使用一个或多个以太网交换机驱动程序（**Ethernet Switch Driver**）模块，并且这些模块抽象出相应以太网交换机的特定功能和接口。

所以，以太网接口模块的可执行代码需完全独立于以太网通信控制器（**Ethernet Communication Controller**），但不包括运行时的动态配置。

![Figure1-1](Figure1-1.png)

注意：因为以太网接口模块允许代码模块按指定的遵循“一刀切”原则方式交付目标代码，即以太网接口模块的整个配置可以在不修改任何源代码的情况下进行。所以以太网接口的配置在很大程度上，可以在不详细了解底层硬件的情况下进行。

# 2. 缩略语

**CBR**
> Channel Busy Ratio，通道繁忙比率。

**CIT** 
> Channel Idle Time，通道空闲时间。

**CV2x** 
> Cellular Vehicle to X driver，蜂窝车辆到X驱动程序。

**Eth** 
> Ethernet Controller Driver，以太网控制器驱动程序（AUTOSAR BSW 模块），

**EthIf** 
> Ethernet Interface， 以太网接口（AUTOSAR BSW 模块）。

**EthSM** 
> Ethernet State Manager，以太网状态管理器（AUTOSAR BSW 模块）。

**EthTrcv** 
> Ethernet Transceiver Driver，以太网收发器驱动程序（AUTOSAR BSW 模块）。

**IP** 
> Internet Protocol，网际协议。

**MCG** 
> Module Configuration Generator，模块配置生成器。

**MII** 
> Media Independent Interface，媒体独立接口（以太网控制器提供的用于访问以太网收发器的标准化接口）。

**RSSI** 
> Received Signal Strength Indicator，接收信号强度指示器。

**TCP** 
> Transmission Control Protocol，传输控制协议。

**TCP/IP Stack** 
> Ethernet communication stack，以太网通信栈。

**VLAN** 
> Virtual Local Area Network，虚拟局域网。

**WEth** 
> Wireless Ethernet Driver，无线以太网驱动程序。

**WEthTrcv** 
> Wireless Ethernet Transceiver Driver，无线以太网收发器驱动程序。

**OA TC10** 
> Open Alliance TC10，开放联盟 TC10 规格 [5]。

# 3. 相关文档

## 3.1. 输入文件

[1] Layered Software Architecture
> AUTOSAR_EXP_LayeredSoftwareArchitecture

[2] Specification of TCP/IP Stack
> AUTOSAR_SWS_TcpIp

[3] Specification of Ethernet State Manager
> AUTOSAR_SWS_EthernetStateManager

[4] Glossary
> AUTOSAR_TR_Glossary

[5] OPEN Sleep/Wake-up Specification for Automotive Ethernet
> http://www.opensig.org/Automotive-Ethernet-Specifications/

[6] General Specification of Basic Software Modules
> AUTOSAR_SWS_BSWGeneral

[7] Specification of Vehicle-2-X Geo Networking
> AUTOSAR_SWS_V2XGeoNetworking

[8] Specification of Chinese Vehicle-2-X Network
> AUTOSAR_SWS_ChineseV2XNetwork

[9] Specification of Chinese Vehicle-2-X Management
> AUTOSAR_SWS_ChineseV2XManagement

[10] Specification of Ethernet Driver
> AUTOSAR_SWS_EthernetDriver

[11] Specification of Ethernet Transceiver Driver
> AUTOSAR_SWS_EthernetTransceiverDriver

[12] General Requirements on Basic Software Modules
> AUTOSAR_SRS_BSWGeneral

[13] Requirements on Ethernet Support in AUTOSAR
> AUTOSAR_SRS_Ethernet

[14] Specification of Default Error Tracer
> AUTOSAR_SWS_DefaultErrorTracer

[15] Specification of Time Synchronization over Ethernet
> AUTOSAR_SWS_TimeSyncOverEthernet

[16] Specification of Wireless Ethernet Driver
> AUTOSAR_SWS_WirelessEthernetDriver

[17] Specification of Ethernet Switch Driver
> AUTOSAR_SWS_EthernetSwitchDriver

[18] Specification of Wireless Ethernet Transceiver Driver
> AUTOSAR_SWS_WirelessEthernetTransceiverDriver

[19] Specification of Cellular Vehicle-2-X Driver
> AUTOSAR_SWS_CellularV2XDriver

[20] IEEE Standard for Local and metropolitan area networks-Media Access Control (MAC) Security
> https://ieeexplore.ieee.org/document/8585421


## 3.2. 相关规格

**AUTOSAR** 提供了基本软件模块的一般规范[6，SWS BSW通用]，该规范也适用于以太网接口模块。

所以，SWS BSW 通用规范应被视为以太网接口模块的附加和必需规范。

# 4. 约束和假设

## 4.1. 局限性

以太网接口模块在概念上能够访问一个或多个以太网驱动程序和一个或多个以太网收发器驱动程序。

同时无法传输超过当前所用的以太网控制器的可用缓冲区大小的数据。更长的数据必须使用互联网协议（**IP**）或传输控制协议（**TCP**）进行传输。

## 4.2. 汽车领域的适用性

以太网BSW堆栈旨在用于需要高数据速率但不需要硬实时的场合。当然，它也可用于要求较低的用例，即：低数据速率。

# 5. 对其他模块的依赖关系

本章列出了与以太网接口模块交互的模块。

## 5.1. 使用以太网接口模块的模块：

* 以太网通信堆栈（TCP/IP Stack [2]）
* 以太网状态管理器（EthSM [3]）
* V2xGn [7]
* CnV2xNet [8]
* CnV2xM [9]

## 5.2. 对其他模块的依赖：

* 以太网接口模块不负责配置以太网驱动程序 [10]，但需要其前面的初始化和配置。
* 以太网接口模块不负责配置以太网收发器驱动程序 [11]，但需要其前面的初始化和配置。

# 6. 功能规范

## 6.1. 以太网 BSW 堆栈

作为 AUTOSAR 分层软件架构 [1] 的一部分，以太网 BSW 模块也形成了分层软件堆栈。图 7.1 描述了此以太网 BSW 堆栈的基本结构。以太网接口模块使用以太网驱动程序层访问多个以太网控制器，该层可由多个以太网驱动程序模块组成。

![Figure7-1](Figure7-1.png)

### 6.1.1. 以太网控制器的索引方案

如果使用**CAN XL**作为物理介质，则配置中需包含**EthIfEthCanXLCtrlRef**来替代**EthIfEthCtrlRef**，以及**EthIfCanXLTrcvRef**来替代**EthIfEthTrcvRef**。在这种情况下，表示为以太网驱动的**\<EthDrv\>_Xxx** 的 **API** 将会被**CanXL_Xxx**替换，而不是直接使用以太网驱动的**Eth_Xxx**的接口。同样，表示为以太网收发器的**\<EthTrcv\>_Yyy** 的 **API** 将会被**CanXLTrcv_Yyy**替换，而不是直接使用以太网收费器的 **EthTrcv_Yyy** 的调用。

以太网接口模块的用户使用索引的方案来识别以太网控制器资源，如图 **7.2** 所示。

![Figure7-2](Figure7-2.png)

因为以太网接口模块使用索引（**EthIfCtrlIdx**），从以太网控制器模块和以太网收发器模块的底层通信系统中抽象出对 **VLAN** 的访问，所以以太网接口模块需实现从以太网接口控制器（**EthIfCtrlIdx**）到相应硬件资源控制器（**EthCtrlId** + **EthTrcvId**）的映射。

### 6.1.2. 以太网交换机的索引方案

由于以太网接口模块（**EthIf**）不涉及属于单个以太网交换机的单个**EthSwtPorts**，所以**EthIf**中不需要任何**EthSwtPorts**的索引方案。任何与**EthSwtPorts**交互的BSW模块都可以直接引用**EthSwtPort**的ECU配置进行索引。

**EthIf** 应将 **EthIfSwitchIdx** 索引的所有访问分派到具有 **EthSwtIdx** 值的相应 **EthSwt** 驱动程序模块。

### 6.1.3. 以太网接口主函数

以太网接口模块需实现在轮询模式下用于帧传输确认和帧接收的主函数，并且主函数的调用周期需在系统配置时进行设置。

### 6.1.4. 需求说明

本章节列出了以太网接口模块需实现的需求。

* 以太网接口模块环境，包括了调用以太网接口模块接口的所有模块。
* 以太网接口模块应支持预编译时（**pre-compile time**）、链接时（**link time**）和构建后时（**post-build time**）的配置。
* 头文件 **EthIf.h** 应包含软件和规范版本号。
* 以太网接口模块应根据相关代码文件和头文件的版本号的预处理检查，在代码文件和头文件之间执行一致性检查。
* 如果为以太网接口模块启用了开发错误检测，则以太网接口模块需检查 **API** 参数有效性，并向 **DET** 模块报告检测到的错误。**DET API** 函数在 [参考文献 14 - 默认错误跟踪器规范] 中定义。
* 以太网接口模块需将以太网接口 **SWS** 指定的 **API** 函数实现为实际的 **C** 代码函数，而不是以宏的方式实现后进行目标代码交付。
* 任何以太网接口模块头文件都不应定义全局变量。

### 6.1.5. 配置说明

以太网接口模块应提供包含软件标识（应包含供应商标识、模块 ID 和软件版本信息）、配置和集成过程所需的数据的 **XML** 文件。此文件应描述供应商特定的配置参数，并应包含建议的配置参数值。

**MCG** 应读取以太网驱动程序和以太网接口模块的 **ECU** 配置说明。虽然与群集相关的配置参数包含在以太网接口模块配置说明中，但与以太网驱动程序相关的配置数据需包含在以太网驱动程序模块配置说明中。以太网接口模块特定配置工具需读取这两个 **ECU** 模块说明，以派生映射到以太网接口模块的所有以太网驱动程序的配置数据。

**MCG** 应确保生成的配置数据的一致性。

以太网接口模块的配置应在ECU配置时进行配置。运行时不得配置任何通信参数。

构建后（**post-build time**）配置数据的起始地址需在模块初始化期间传递。这些配置类分配给配置参数可以在第10章中找到。所有以太网接口相关配置参数的详细说明可在本文档的第 10 章中找到。此外，应针对以太网接口模块配置评估以太网驱动程序的配置说明。

### 6.1.6. 虚拟局域网（VLAN）支持

以太网接口模块应支持虚拟局域网（**VLAN**）。

以太网接口模块应将虚拟局域网（**VLAN**）封装到代表专用 **VLAN** 的虚拟控制器（以太网接口控制器）中。以太网接口模块上层的所有 **BSW** 模块都应基于这些虚拟控制器进行交互。以太网驱动程序和收发器仅处理实际控制器，并不知道虚拟控制器的存在。

警告：如果未设置 **VLAN ID**，则虚拟控制器把它表示为未标记的 **VLAN**。

以太网接口模块应使用以太网驱动程序提供的缓冲区来支持 **VLAN**。如果使用 **Can XL**，以太网接口模块应使用 **Can XL** 驱动程序提供的缓冲区。

### 6.1.7. 唤醒支持

以太网接口模块支持唤醒，具体支持选项依赖于参数 **EthIfWakeUpSupport**。

注意：只有在底层 **EthTrcv** 也支持唤醒时，在 **EthIf** 中启用唤醒支持才有意义。

### 6.1.8. 以太网交换机管理支持

以太网交换机管理能够控制有关以太网交换机端口特定入口（**ingress**）和出口（**egress**）来处理的以太网帧，并提供处理以太网交换机端口的特定时间戳。此功能对于其他 **BSW** 模块至关重要，特别是对于 **EthTSyn**，它需要与时间同步 [15] 或路径延迟测量帧关联的端口特定信息。

基本硬件架构及交互介绍请 [参考文献**10**，以太网驱动规范]。

有关功能序列的更多详细信息，请参阅 [参考文献**16**，无线以太网驱动程序规范]。

注意：以太网交换机管理 **API** 需支持上层应用（**\<Upper Layer\>**）收集/修改以太网交换机端口特定的通信属性。

### 6.1.9. 处理维护的以太网硬件

以太网接口（**EthIf**）依赖配置来处理所需维护的以太网硬件：

* **EthIfPhysController**（表示：物理以太网控制器）
* **EthIfController**（表示：支持**VLAN**的虚拟以太网控制器）
* **EthIfTransceiver**（表示：PHY）
* **EthIfSwitch**（表示：以太网交换机）
* **EthIfSwitchPortGroups**（表示：**EthSwtPort** 组）

配置中应至少存在一个 **EthIfPhysController** 以便与以太网驱动程序交互。**EthIfController** 表示物理的以太网控制器与用于在以太网上进行通信的以太网硬件之间的连接。它可以是 **EthIfTransceiver**、**EthIfSwitch** 或 **EthIfSwitchPortGroup**。

如果上层想要控制特定以太网上的通信，则通过 **EthIf_SetControllerMode** 调用相应的 **EthIfController**。以太网接口模块处理通信请求，以便将请求转发到相应的以太网硬件，包括：

* 以太网收发器（**EthIfTransceiver**）
* 以太网交换机（**EthIfSwitch**）
* 以太网交换机端口组的引用类型。

对于引用 **EthIfSwitchPortGroup** 类型的链路信息（**link-information**）的 **EthIfController**，以太网接口模块监控 **EthIfSwitchPortGroup** 内所有 **EthSwtPort** 的链路状态，并将累加的链路状态（**link state**）发送给相应的上层的 **EthSM**（参考文献 [3]）。

**EthIfSwitchPortGroups** 是通过调用 **EthIf_SwitchPortGroupRequestMode** 被控制。如果根据部分网络请求控制 **EthIfSwitchPortGroups**，则可以使用此选项。部分网络请求被转发到 **BswM**，**BswM** 中的某条特定的规则会触发控制相应 **EthIfSwitchPortGroup** 的操作。所以如果使用 **EthIfSwitchPortGroup** 选项，则控制通信的以太网接口的上层是 **EthSM** 和 **BswM**。如果针对通信请求寻址 **EthIfController** 或 **EthIfSwitchPortGroup**，则上层请求以太网连接处于活动状态（**ETH_MODE_ACTIVE** 或 **ETH_MODE_WITH_WAKEUP_REQUEST**）或者关闭状态（**ETH_MODE_DOWN**），这是独立的。以太网接口请求相应的下层针对 **ACITVE** 请求打开相应的以太网硬件，或者针对 **DOWN** 请求关闭相应的以太网硬件。

#### 6.1.9.1. 以太网交换机端口组（EthIfSwitchPortGroup）

以太网接口模块支持以太网交换机端口组 (EthIfSwitchPortGroup)。**ACITVE** 或者 **DOWN**的请求将由以太网接口模块处理并进行评级。以太网接口模块必须决定 **EthIfSwitchPotGroup** 的 **DOWN** 或者 **ACTIVE** 状态。**EthIfSwitchPortGroup** 的 **ACTIVE** 请求将始终否决 **EthIfSwitchPortGroup** 的 **DOWN** 请求。如果针对 **EthIfSwitchPortGroup** 的 **DOWN** 请求已准备好执行，则以太网接口模块（**EthIf**）将检查该 **EthIfSwitchPortGroup** 引用的 **EthSwtPort**，并决定是否可以将该 **EthSwtPort** 设置为 **DOWN** 状态。如果有效，则在配置的关闭延迟计时器到期后，引用的**EthSwtPort** 将被设置为 **DOWN** 状态。

注意：第 6.1.9.2 和 7.3.21 章节中有更大 **EthIfSwitchPortGroup** 切换的需求。

##### 6.1.9.1.1. EthIfSwitchPortGroup 链路状态累加

以太网接口模块需要知道 **EthIfSwitchPortGroups** 的实际链路状态。**EthIfSwitchPortGroup** 的链路状态是根据 **EthIfSwitchPortGroup** 中引用的所有 **EthSwtPort** 的链路状态计算的。计算的执行动作被称为链路状态累加（**link state accumulation**），结果称为累加的链路状态（**accumulated link state**）。**EthIfSwitchPortGroup**的累加的链路状态是 **EthIfSwitchPortGroup** 的实际状态。**EthIfController** 所引用的 **EthIfSwitchPortGroup** 的实际状态通过调用 **EthSM_TrcvLinkStateChg** 报告给 **EthSM**。未被任何 **EthIfController** 引用的 **EthIfSwitchPortGroup** 的实际状态通过调用 **BswM_EthIf_PortGroupLinkStateChg** 报告给 **BswM**。

**EthIfSwitchPortGroup** 的链路状态是根据 **EthIfSwitchPortGroup** 引用的 **EthSwtPort** 的所有链路状态计算得出的。

如果满足以下条件之一，**EthIfSwitchPortGroup** 的链路状态为 **ETHTRCV_LINK_STATE_DOWN**（链路断开）：

* 被引用的**EthSwtPort** 扮演主机端口（**host port**）角色或者上行链路端口（**up link port**）角色，他们都为链路关闭状态（**link down state**）。
* 所有被引用的无角色的 **EthSwtPort** 都处于链路关闭状态。

否则 **EthIfSwitchPortGroup** 的累加的链接状态为 **ETHTRCV_LINK_STATE_ACTIVE**（连接）。

如果 **EthIfCtrl** 引用了**EthIfSwitch**，但是没有配置端口组，则当链路状态发生变化时，以太网接口模块（**EthIf**）应通过调用 **EthIfController** 的**EthSM_TrcvLinkStateChg** 向 **EthSM** 指示主机端口的链路状态。

如果 **EthIfSwitchPortGroup** 未连接到任何 **EthIfController**，则当链路状态发生变化时，以太网接口模块（**EthIf**）将通过调用 **EthIfSwitchPortGroup** 的 **BswM_EthIf_PortGroupLinkStateChg** 向 **BswM** 指示 **EthIfSwitchPortGroup** 的累加的链路状态。

如果 **EthIfSwitchPortGroup** 连接到 **EthIfController**，则当链路状态发生变化时，以太网接口模块（**EthIf**）应通过调用 **EthIfController** 的 **EthSM_TrcvLinkStateChg** 向 **EthSM** 指示 **EthIfSwitchPortGroup** 的累加的链路状态。

#### EthIfController和相应以太网硬件的切换

**EthIfController** 的切换是通过调用 **EthIf_SetControllerMode** 来触发的。**EthIfController** 的切换隐含地包括相应的以太网硬件，如：**PHY**、以太网交换机、以太网交换机端口的切换。以太网接口通过异步回调通知（例如：**EthIf_TrcvModeInduction**）与下层交互。本章节描述了用于切换 **EthIfController** 和相应的以太网硬件之间 **API** 的交互。

注意：
1. 如果引用的 **EthIfPhysController** 的模式已更改，则对 **EthIf_SetControllerMode** 的调用会通过调用 **EthIf_CtrlModeInduction** 引起异步指示（**asynchronous indication**）。
2. 这些需求假设以太网控制器 (**EthIfPhysControllerIdx**) 和引用的以太网硬件（例如：**PHY**、以太网交换机）彼此独立控制。例如，如果已请求 **ETH_MODE_ACITVE** 或 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**，并且受影响的以太网控制器 (**EthIfPhysControllerIdx**) 的以太网控制器驱动程序尚未指示 **ETH_MODE_ACITVE**，则这些请求可以直接转发到所引用以太网硬件的相应较低层。实施必须考虑以下几点：
    * **ETH_MODE_ACTIVE** 和 **ETH_MODE_DOWN** 用于激活和停用以太网控制器的通信能力（**communication capability**），但不激活所连接的以太网硬件的控制能力（**control capability**）。例如：**MDIO**。
    * 如果以太网控制器的控制能力被驱动程序模块需要，例如：以太网交换机驱动程序，那么实施必须确保此控制能力始终可用。
3. 如果请求由于 **EthIfPhysController** 尚未接收到底层模块 **ETH_MODE_ACTIVE** 的指示而被推迟，则 **EthIf** 必须确保具有**ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST** 的请求不会被另一个具有 **ETH_MODE_ACTIVE** 的 **EthIf_SetControllerMode** 调用覆盖。

