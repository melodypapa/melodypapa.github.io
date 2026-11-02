---
title: "AUTOSAR Ethernet Interface（以太网接口）"
spec: AUTOSAR_CP_SWS_EthernetInterface
release: R23-11
---




## 已知限制

目前，「对其他模块的依赖」章节并未描述所依赖模块的版本。因此，后续将扩展该章节以加入版本检查。

## 1. 简介和功能概述

此规范指定了 **AUTOSAR** 以太网接口基本软件模块的功能、API 和配置。

在AUTOSAR分层软件架构[\[1\]](#ref-1)中，以太网接口模块（EthIf）属于ECU抽象层。或者更准确地说，它属于通信硬件抽象。

这表示以太网接口模块的主要任务：

向上层提供以太网通信系统的硬件独立接口，包括多个不同的有线或者无线的以太网控制器和收发器。此接口对于所有以太网控制器和收发器以及蜂窝 **V2X** 控制器需被统一。因此上层模块（**TCP/IP** [\[2\]](#ref-2)、**EthSM** [\[3\]](#ref-3)、**CDD**、**V2x** 等模块）可以通过统一的方式访问底层总线系统。

以太网接口模块不直接访问以太网硬件（包括：以太网通信控制器和以太网收发器），而是通过一个或多个特定于硬件的驱动程序模块进行间接的。

为了访问以太网控制器（**Ethernet controller**），以太网接口模块需要使用一个或多个以太网驱动程序（**Ethernet Driver**）模块，并且这些模块需抽象出相应的以太网控制器的特定功能和接口。

为了访问以太网收发器（**Ethernet transceiver**），以太网接口模块需要使用一个或多个以太网收发器驱动程序（**Ethernet Transceiver Driver**）模块，并且这些模块需抽象出相应的以太网收发器的特定功能和接口。

为了访问以太网交换机（**Ethernet switch**），以太网接口模块需要使用一个或多个以太网交换机驱动程序（**Ethernet Switch Driver**）模块，并且这些模块抽象出相应以太网交换机的特定功能和接口。

所以，以太网接口模块的可执行代码需完全独立于以太网通信控制器（**Ethernet Communication Controller**），但不包括运行时的动态配置。

![Figure1-1](Figure1-1.png)

注意：因为以太网接口模块允许代码模块按指定的遵循“一刀切”原则方式交付目标代码，即以太网接口模块的整个配置可以在不修改任何源代码的情况下进行。所以以太网接口的配置在很大程度上，可以在不详细了解底层硬件的情况下进行。

## 2. 缩略语

以下词汇表包含与以太网接口模块相关、但未包含在 [4, AUTOSAR 术语表] 中的缩略语和缩写。

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
> Open Alliance TC10 Specification，开放联盟 TC10 规格。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

<a id="ref-1"></a>[1] Layered Software Architecture
> AUTOSAR_CP_EXP_LayeredSoftwareArchitecture

<a id="ref-2"></a>[2] Specification of TCP/IP Stack
> AUTOSAR_CP_SWS_TcpIp

<a id="ref-3"></a>[3] Specification of Ethernet State Manager
> AUTOSAR_CP_SWS_EthernetStateManager

<a id="ref-4"></a>[4] Glossary
> AUTOSAR_FO_TR_Glossary

<a id="ref-5"></a>[5] OPEN Sleep/Wake-up Specification for Automotive Ethernet
> http://www.opensig.org/Automotive-Ethernet-Specifications/

<a id="ref-6"></a>[6] General Specification of Basic Software Modules
> AUTOSAR_CP_SWS_BSWGeneral

<a id="ref-7"></a>[7] Specification of Vehicle-2-X Geo Networking
> AUTOSAR_CP_SWS_V2XGeoNetworking

<a id="ref-8"></a>[8] Specification of Chinese Vehicle-2-X Network
> AUTOSAR_CP_SWS_ChineseV2XNetwork

<a id="ref-9"></a>[9] Specification of Chinese Vehicle-2-X Management
> AUTOSAR_CP_SWS_ChineseV2XManagement

<a id="ref-10"></a>[10] Specification of Ethernet Driver
> AUTOSAR_CP_SWS_EthernetDriver

<a id="ref-11"></a>[11] Specification of Ethernet Transceiver Driver
> AUTOSAR_CP_SWS_EthernetTransceiverDriver

<a id="ref-12"></a>[12] General Requirements on Basic Software Modules
> AUTOSAR_CP_SRS_BSWGeneral

<a id="ref-13"></a>[13] Requirements on Ethernet Support in AUTOSAR
> AUTOSAR_CP_SRS_Ethernet

<a id="ref-14"></a>[14] Specification of Default Error Tracer
> AUTOSAR_CP_SWS_DefaultErrorTracer

<a id="ref-15"></a>[15] Specification of Time Synchronization over Ethernet
> AUTOSAR_CP_SWS_TimeSyncOverEthernet

<a id="ref-16"></a>[16] Specification of Wireless Ethernet Driver
> AUTOSAR_CP_SWS_WirelessEthernetDriver

<a id="ref-17"></a>[17] Specification of IEEE1722 Transport Protocol Module
> AUTOSAR_CP_SWS_IEEE1722TransportLayer

<a id="ref-18"></a>[18] Specification of Linklayer Sdu Routing Module
> AUTOSAR_CP_SWS_LSduRouter

<a id="ref-19"></a>[19] IEEE 802.3-2022
> https://www.ieee802.org/3/

<a id="ref-20"></a>[20] Specification of Ethernet Switch Driver
> AUTOSAR_CP_SWS_EthernetSwitchDriver

<a id="ref-21"></a>[21] Specification of Wireless Ethernet Transceiver Driver
> AUTOSAR_CP_SWS_WirelessEthernetTransceiverDriver

<a id="ref-22"></a>[22] Specification of Cellular Vehicle-2-X Driver
> AUTOSAR_CP_SWS_CellularV2XDriver

<a id="ref-23"></a>[23] IEEE Standard for Local and metropolitan area networks-Media Access Control (MAC) Security
> https://ieeexplore.ieee.org/document/8585421

### 3.2. 相关规范

**AUTOSAR** 提供了基本软件模块的一般规范[**AUTOSAR_SWS_BSWGeneral**] [**6**]，该规范也适用于以太网接口模块。

所以**AUTOSAR_SWS_BSWGeneral**需被视为以太网接口模块的附加和必需规范。

## 4. 约束和假设

### 4.1. 限制

以太网接口模块在概念上能够访问一个或多个以太网驱动程序（**Ethernet Driver**），以及一个或多个以太网收发器驱动程序（**Ethernet Transceiver Driver**）。

同时无法传输超过当前所用的以太网控制器的可用缓冲区大小的数据。更长的数据必须使用互联网协议（**IP**）或传输控制协议（**TCP**）进行传输。

### 4.2. 汽车域的适用性

以太网BSW堆栈（**Ethernet BSW stack**）旨在用于需要高数据速率但不需要硬实时的场合。当然，它也可用于要求较低（**less-demanding**）的用例，即：低数据速率。

## 5. 对其他模块的依赖

本章列出了与以太网接口模块交互的模块。

### 5.1. 使用以太网接口模块的模块：

* 以太网通信堆栈（TCP/IP Stack [\[2\]](#ref-2)）
* 以太网状态管理器（EthSM [\[3\]](#ref-3)）
* V2xGn [\[7\]](#ref-7)
* CnV2xNet [\[8\]](#ref-8)
* CnV2xM [\[9\]](#ref-9)

### 5.2. 对其他模块的依赖：

* 以太网接口模块不负责配置以太网驱动程序 [\[10\]](#ref-10)，但需负责其前置的初始化和配置。
* 以太网接口模块不负责配置以太网收发器驱动程序 [\[11\]](#ref-11)，但需负责其前置的初始化和配置。

## 6. 功能规格

### 6.1. 以太网 BSW 堆栈（Ethernet BSW stack）

作为 AUTOSAR 分层软件架构 [\[1\]](#ref-1) 的一部分，以太网 BSW 模块也形成了分层软件堆栈。图 **7.1** 描述了此以太网 BSW 堆栈的基本结构。以太网接口模块使用以太网驱动程序层（**Ethernet Driver layer**）访问多个以太网控制器（**Ethernet controllers**），该层可由多个以太网驱动程序模块（**Ethernet Drivers modules**）组成。

![Figure7-1](Figure7-1.png)

#### 6.1.1. 以太网控制器的索引方案

如果使用**CAN XL**作为物理介质，则配置中需包含**EthIfEthCanXLCtrlRef**来替代**EthIfEthCtrlRef**，以及**EthIfCanXLTrcvRef**来替代**EthIfEthTrcvRef**。在这种情况下，表示为以太网驱动的 **&lt;EthDrv&gt;_Xxx** 的 **API** 将会被**CanXL_Xxx**替换，而不是直接使用以太网驱动的 **Eth_Xxx** 的接口。同样，表示为以太网收发器的 **&lt;EthTrcv&gt;_Yyy** 的 **API** 将会被**CanXLTrcv_Yyy** 替换，而不是直接使用以太网收费器的 **EthTrcv_Yyy** 的调用。

以太网接口模块的用户使用索引的方案来识别以太网控制器资源，如图 **7.2** 所示。

![Figure7-2](Figure7-2.png)

因为以太网接口模块使用索引（**EthIfCtrlIdx**），从以太网控制器模块和以太网收发器模块的底层通信系统中抽象出对 **VLAN** 的访问，所以以太网接口模块需实现从以太网接口控制器（**EthIfCtrlIdx**）到相应硬件资源控制器（**EthCtrlId** + **EthTrcvId**）的映射。

#### 6.1.2. 以太网交换机的索引方案

由于以太网接口模块（**EthIf**）不涉及属于单个以太网交换机的单个**EthSwtPorts**，所以**EthIf**中不需要任何**EthSwtPorts**的索引方案。任何与**EthSwtPorts**交互的BSW模块都可以直接引用**EthSwtPort**的ECU配置进行索引。

**EthIf** 应将 **EthIfSwitchIdx** 索引的所有访问分派到具有 **EthSwtIdx** 值的相应 **EthSwt** 驱动程序模块。

#### 6.1.3. 以太网接口主函数

以太网接口模块需实现在轮询模式下用于帧传输确认和帧接收的主函数，并且主函数的调用周期需在系统配置时进行设置。

#### 6.1.4. 需求说明

本章节列出了以太网接口模块需实现的需求。

* 以太网接口模块环境，包括了调用以太网接口模块接口的所有模块。
* 以太网接口模块应支持预编译时（**pre-compile time**）、链接时（**link time**）和构建后时（**post-build time**）的配置。
* 头文件 **EthIf.h** 应包含软件和规范版本号。
* 以太网接口模块应根据相关代码文件和头文件的版本号的预处理检查，在代码文件和头文件之间执行一致性检查。
* 如果为以太网接口模块启用了开发错误检测，则以太网接口模块需检查 **API** 参数有效性，并向 **DET** 模块报告检测到的错误。**DET API** 函数在 [参考文献 14 - 默认错误跟踪器规范] 中定义。
* 以太网接口模块需将以太网接口 **SWS** 指定的 **API** 函数实现为实际的 **C** 代码函数，而不是以宏的方式实现后进行目标代码交付。
* 任何以太网接口模块头文件都不应定义全局变量。

#### 6.1.5. 配置说明

以太网接口模块应提供包含软件标识（应包含供应商标识、模块 ID 和软件版本信息）、配置和集成过程所需的数据的 **XML** 文件。此文件应描述供应商特定的配置参数，并应包含建议的配置参数值。

**MCG** 应读取以太网驱动程序和以太网接口模块的 **ECU** 配置说明。虽然与群集相关的配置参数包含在以太网接口模块配置说明中，但与以太网驱动程序相关的配置数据需包含在以太网驱动程序模块配置说明中。以太网接口模块特定配置工具需读取这两个 **ECU** 模块说明，以派生映射到以太网接口模块的所有以太网驱动程序的配置数据。

**MCG** 应确保生成的配置数据的一致性。

以太网接口模块的配置应在ECU配置时进行配置。运行时不得配置任何通信参数。

构建后（**post-build time**）配置数据的起始地址需在模块初始化期间传递。这些配置类分配给配置参数可以在第10章中找到。所有以太网接口相关配置参数的详细说明可在本文档的第 10 章中找到。此外，应针对以太网接口模块配置评估以太网驱动程序的配置说明。

#### 6.1.6. 虚拟局域网（VLAN）支持

以太网接口模块应支持虚拟局域网（**VLAN**）。

以太网接口模块应将虚拟局域网（**VLAN**）封装到代表专用 **VLAN** 的虚拟控制器（以太网接口控制器）中。以太网接口模块上层的所有 **BSW** 模块都应基于这些虚拟控制器进行交互。以太网驱动程序和收发器仅处理实际控制器，并不知道虚拟控制器的存在。

警告：如果未设置 **VLAN ID**，则虚拟控制器把它表示为未标记的 **VLAN**。

以太网接口模块应使用以太网驱动程序提供的缓冲区来支持 **VLAN**。如果使用 **Can XL**，以太网接口模块应使用 **Can XL** 驱动程序提供的缓冲区。

#### 6.1.7. 唤醒支持

以太网接口模块支持唤醒，具体支持选项依赖于参数 **EthIfWakeUpSupport**。

注意：只有在底层 **EthTrcv** 也支持唤醒时，在 **EthIf** 中启用唤醒支持才有意义。

#### 6.1.8. 以太网交换机管理支持

以太网交换机管理能够控制有关以太网交换机端口特定入口（**ingress**）和出口（**egress**）来处理的以太网帧，并提供处理以太网交换机端口的特定时间戳。此功能对于其他 **BSW** 模块至关重要，特别是对于 **EthTSyn**，它需要与时间同步 [\[15\]](#ref-15) 或路径延迟测量帧关联的端口特定信息。

基本硬件架构及交互介绍请 [参考文献**10**，以太网驱动规范]。

有关功能序列的更多详细信息，请参阅 [参考文献**16**，无线以太网驱动程序规范]。

注意：以太网交换机管理 **API** 需支持上层应用（**&lt;Upper Layer&gt;**）收集/修改以太网交换机端口特定的通信属性。

#### 6.1.9. 处理维护的以太网硬件

以太网接口（**EthIf**）依赖配置来处理所需维护的以太网硬件：

* [**EthIfPhysController**](#926-ethifphyscontroller)（表示：物理以太网控制器）
* [**EthIfController**](#924-ethifcontroller)（表示：支持**VLAN**的虚拟以太网控制器）
* [**EthIfTransceiver**](#9212-ethiftransceiver)（表示：PHY）
* [**EthIfSwitch**](#9210-ethifswitch)（表示：以太网交换机）
* **EthIfSwitchPortGroups**（表示：**EthSwtPort** 组）

配置中应至少存在一个 [**EthIfPhysController**](#926-ethifphyscontroller) 以便与以太网驱动程序交互。[**EthIfController**](#924-ethifcontroller) 表示物理的以太网控制器与用于在以太网上进行通信的以太网硬件之间的连接。它可以是 [**EthIfTransceiver**](#9212-ethiftransceiver)、[**EthIfSwitch**](#9210-ethifswitch) 或 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)。

如果上层想要控制特定以太网上的通信，则通过 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 调用相应的 [**EthIfController**](#924-ethifcontroller)。以太网接口模块处理通信请求，以便将请求转发到相应的以太网硬件，包括：

* 以太网收发器（[**EthIfTransceiver**](#9212-ethiftransceiver)）
* 以太网交换机（[**EthIfSwitch**](#9210-ethifswitch)）
* 以太网交换机端口组的引用类型。

对于引用 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 类型的链路信息（**link-information**）的 [**EthIfController**](#924-ethifcontroller)，以太网接口模块监控 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 内所有 **EthSwtPort** 的链路状态，并将累加的链路状态（**link state**）发送给相应的上层的 **EthSM**（参考文献 [\[3\]](#ref-3)）。

**EthIfSwitchPortGroups** 是通过调用 [**EthIf_SwitchPortGroupRequestMode**](#7326-ethif_switchportgrouprequestmode) 被控制。如果根据部分网络请求控制 **EthIfSwitchPortGroups**，则可以使用此选项。部分网络请求被转发到 **BswM**，**BswM** 中的某条特定的规则会触发控制相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的操作。所以如果使用 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 选项，则控制通信的以太网接口的上层是 **EthSM** 和 **BswM**。如果针对通信请求寻址 [**EthIfController**](#924-ethifcontroller) 或 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)，则上层请求以太网连接处于活动状态（**ETH_MODE_ACTIVE** 或 **ETH_MODE_WITH_WAKEUP_REQUEST**）或者关闭状态（**ETH_MODE_DOWN**），这是独立的。以太网接口请求相应的下层针对 **ACITVE** 请求打开相应的以太网硬件，或者针对 **DOWN** 请求关闭相应的以太网硬件。

#### 6.1.9.1. 以太网交换机端口组（EthIfSwitchPortGroup）

以太网接口模块支持以太网交换机端口组 ([EthIfSwitchPortGroup](#9211-ethifswitchportgroup))。**ACITVE** 或者 **DOWN**的请求将由以太网接口模块处理并进行评级。以太网接口模块必须决定 **EthIfSwitchPotGroup** 的 **DOWN** 或者 **ACTIVE** 状态。[**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的 **ACTIVE** 请求将始终否决 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的 **DOWN** 请求。如果针对 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的 **DOWN** 请求已准备好执行，则以太网接口模块（**EthIf**）将检查该 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 引用的 **EthSwtPort**，并决定是否可以将该 **EthSwtPort** 设置为 **DOWN** 状态。如果有效，则在配置的关闭延迟计时器到期后，引用的**EthSwtPort** 将被设置为 **DOWN** 状态。

注意：关于 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 切换的更多需求请参见 [6.1.9.2](#6192-ethifcontroller-和相应以太网硬件的切换) 节和 [7.3.26](#7326-ethif_switchportgrouprequestmode) 节。

##### 6.1.9.1.1. EthIfSwitchPortGroup 链路状态累加

以太网接口模块需要知道 **EthIfSwitchPortGroups** 的实际链路状态。[**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的链路状态是根据 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 中引用的所有 **EthSwtPort** 的链路状态计算的。计算的执行动作被称为链路状态累加（**link state accumulation**），结果称为累加的链路状态（**accumulated link state**）。[**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)的累加的链路状态是 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的实际状态。[**EthIfController**](#924-ethifcontroller) 所引用的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的实际状态通过调用 **EthSM_TrcvLinkStateChg** 报告给 **EthSM**。未被任何 [**EthIfController**](#924-ethifcontroller) 引用的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的实际状态通过调用 **BswM_EthIf_PortGroupLinkStateChg** 报告给 **BswM**。

[**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的链路状态是根据 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 引用的 **EthSwtPort** 的所有链路状态计算得出的。

如果满足以下条件之一，[**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的链路状态为 **ETHTRCV_LINK_STATE_DOWN**（链路断开）：

* 被引用的**EthSwtPort** 扮演主机端口（**host port**）角色或者上行链路端口（**up link port**）角色，他们都为链路关闭状态（**link down state**）。
* 所有被引用的无角色的 **EthSwtPort** 都处于链路关闭状态。

否则 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的累加的链接状态为 **ETHTRCV_LINK_STATE_ACTIVE**（连接）。

如果 **EthIfCtrl** 引用了[**EthIfSwitch**](#9210-ethifswitch)，但是没有配置端口组，则当链路状态发生变化时，以太网接口模块（**EthIf**）应通过调用 [**EthIfController**](#924-ethifcontroller) 的**EthSM_TrcvLinkStateChg** 向 **EthSM** 指示主机端口的链路状态。

如果 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 未连接到任何 [**EthIfController**](#924-ethifcontroller)，则当链路状态发生变化时，以太网接口模块（**EthIf**）将通过调用 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的 **BswM_EthIf_PortGroupLinkStateChg** 向 **BswM** 指示 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的累加的链路状态。

如果 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 连接到 [**EthIfController**](#924-ethifcontroller)，则当链路状态发生变化时，以太网接口模块（**EthIf**）应通过调用 [**EthIfController**](#924-ethifcontroller) 的 **EthSM_TrcvLinkStateChg** 向 **EthSM** 指示 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的累加的链路状态。

#### 6.1.9.2. EthIfController 和相应以太网硬件的切换

[**EthIfController**](#924-ethifcontroller) 的切换是通过调用 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 来触发的。[**EthIfController**](#924-ethifcontroller) 的切换隐含地包括相应的以太网硬件，如：**PHY**、以太网交换机、以太网交换机端口的切换。以太网接口通过异步回调通知（例如：**EthIf_TrcvModeInduction**）与下层交互。本章节描述了用于切换 [**EthIfController**](#924-ethifcontroller) 和相应的以太网硬件之间 **API** 的交互。

注意：
1. 如果引用的 [**EthIfPhysController**](#926-ethifphyscontroller) 的模式已更改，则对 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 的调用会通过调用 **EthIf_CtrlModeInduction** 引起异步指示（**asynchronous indication**）。
2. 这些需求假设以太网控制器 (**EthIfPhysControllerIdx**) 和引用的以太网硬件（例如：**PHY**、以太网交换机）彼此独立控制。例如，如果已请求 **ETH_MODE_ACITVE** 或 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**，并且受影响的以太网控制器 (**EthIfPhysControllerIdx**) 的以太网控制器驱动程序尚未指示 **ETH_MODE_ACITVE**，则这些请求可以直接转发到所引用以太网硬件的相应较低层。实施必须考虑以下几点：
    * **ETH_MODE_ACTIVE** 和 **ETH_MODE_DOWN** 用于激活和停用以太网控制器的通信能力（**communication capability**），但不激活所连接的以太网硬件的控制能力（**control capability**）。例如：**MDIO**。
    * 如果以太网控制器的控制能力被驱动程序模块需要，例如：以太网交换机驱动程序，那么实施必须确保此控制能力始终可用。
3. 如果请求由于 [**EthIfPhysController**](#926-ethifphyscontroller) 尚未接收到底层模块 **ETH_MODE_ACTIVE** 的指示而被推迟，则 **EthIf** 必须确保具有**ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST** 的请求不会被另一个具有 **ETH_MODE_ACTIVE** 的 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 调用覆盖。

如果请求了模式 **ETH_MODE_ACTIVE** 或 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**，并且相应的以太网控制器驱动程序（**EthIfPhysControllerIdx**）尚未指示 **ETH_MODE_ACTIVE**，则函数 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 应以 **ETH_MODE_ACTIVE** 将调用转发给相应以太网控制器驱动程序（**EthIfPhysControllerIdx**）的 **&lt;EthDrv&gt;_SetControllerMode** 函数。

如果以 **ETH_MODE_ACTIVE** 对某个 [**EthIfController**](#924-ethifcontroller) 调用了 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode)，且该 [**EthIfController**](#924-ethifcontroller) 引用了 [**EthIfTransceiver**](#9212-ethiftransceiver)，那么在该 [**EthIfTransceiver**](#9212-ethiftransceiver) 的当前模式为 **ETH_MODE_DOWN** 时，**EthIf** 应按给定顺序将调用转发给以下函数：

1. **&lt;EthTrcv&gt;_SetTransceiverMode**，参数为 **ETH_MODE_ACTIVE**
2. **&lt;EthTrcv&gt;_TransceiverLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_ACTIVE**

如果以 **ETH_MODE_ACTIVE** 对某个 [**EthIfController**](#924-ethifcontroller) 调用了 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode)，且该 [**EthIfController**](#924-ethifcontroller) 引用了 [**EthIfSwitch**](#9210-ethifswitch)，那么在请求了模式 **ETH_MODE_ACTIVE** 且 **EthSwtPort** 的当前模式为 **ETH_MODE_DOWN** 时，**EthIf** 应按给定顺序对引用交换机的所有 **EthSwtPort** 转发调用到以下函数：

1. **EthSwt_SetSwitchPortMode**，参数为 **ETH_MODE_ACTIVE**
2. **EthSwt_PortLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_ACTIVE**

如果以 **ETH_MODE_ACTIVE** 对某个 [**EthIfController**](#924-ethifcontroller) 调用了 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode)，且该 [**EthIfController**](#924-ethifcontroller) 引用了类型为 "control" 的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)，那么在为第一个引用该 **EthSwtPort** 的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 请求了模式 **ETH_MODE_ACTIVE** 且 **EthSwtPort** 的当前模式为 **ETH_MODE_DOWN** 时，**EthIf** 应按给定顺序对相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的所有 **EthSwtPort** 转发调用到以下函数：

1. **EthSwt_SetSwitchPortMode**，参数为 **ETH_MODE_ACTIVE**
2. **EthSwt_PortLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_ACTIVE**

注意：如果 [**EthIfController**](#924-ethifcontroller) 引用了 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 且引用类型为 "link-information"（参见 [9.2.4](#924-ethifcontroller) 节 [**EthIfController**](#924-ethifcontroller) 容器中的端口组引用参数），那么这些 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 可以通过 **BswM** 中的专用规则按照 PNC 状态进行切换。**BswM** 规则可以通过 **BswMEthIfSwitchPortGroupRequestMode** 动作进行配置。**BswM** 调用 **API** 函数 [**EthIf_SwitchPortGroupRequestMode**](#7326-ethif_switchportgrouprequestmode) 来切换相应的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)。

如果以 **ETH_MODE_ACTIVE** 调用了 [**EthIf_SwitchPortGroupRequestMode**](#7326-ethif_switchportgrouprequestmode)，则 **EthIf** 应按给定顺序对相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的所有 **EthSwtPort** 转发调用：

1. 如果当前模式为 **ETH_MODE_DOWN**，则以 **ETH_MODE_ACTIVE** 调用 **EthSwt_SetSwitchPortMode**。
2. 如果当前链路状态为 **ETHTRCV_LINK_STATE_DOWN**，则以 **ETHTRCV_LINK_STATE_ACTIVE** 调用 **EthSwt_PortLinkStateRequest**。

每次以 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST** 对某个 [**EthIfController**](#924-ethifcontroller) 调用 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 且该 [**EthIfController**](#924-ethifcontroller) 引用了 [**EthIfTransceiver**](#9212-ethiftransceiver) 时，**EthIf** 都应按给定顺序、与当前模式无关地将调用转发给以下函数：

1. **&lt;EthTrcv&gt;_SetTransceiverMode**，参数为 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**
2. **&lt;EthTrcv&gt;_TransceiverLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_ACTIVE**，仅当当前状态为 **ETHTRCV_LINK_STATE_DOWN** 时

每次以 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST** 对某个 [**EthIfController**](#924-ethifcontroller) 调用 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 且该 [**EthIfController**](#924-ethifcontroller) 引用了 [**EthIfSwitch**](#9210-ethifswitch) 时，**EthIf** 都应按给定顺序、与当前模式无关地对相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的所有 **EthSwtPort** 转发调用到以下函数：

1. **EthSwt_SetSwitchPortMode**，参数为 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**
2. **EthSwt_PortLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_ACTIVE**，如果当前模式为 **ETHTRCV_LINK_STATE_DOWN** 时

每次以 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST** 对某个 [**EthIfController**](#924-ethifcontroller) 调用 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 且该 [**EthIfController**](#924-ethifcontroller) 引用了类型为 "control" 的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 时，**EthIf** 都应按给定顺序、与当前模式无关地对相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的所有 **EthSwtPort** 转发调用到以下函数：

1. **EthSwt_SetSwitchPortMode**，参数为 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**
2. **EthSwt_PortLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_ACTIVE**，如果当前链路状态为 **ETHTRCV_LINK_STATE_DOWN** 时

每次以 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST** 调用 [**EthIf_SwitchPortGroupRequestMode**](#7326-ethif_switchportgrouprequestmode) 时，**EthIf** 都应针对相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的所有 **EthSwtPort**，与当前 **EthSwtPort** 模式无关地按给定顺序将调用转发给以下函数：

1. **EthSwt_SetSwitchPortMode**，参数为 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**
2. **EthSwt_PortLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_ACTIVE**，仅当当前链路状态为 **ETHTRCV_LINK_STATE_DOWN** 时

上述四个需求的理由：唤醒请求必须始终、与当前模式无关地转发到下层，以确保在网络中触发唤醒。例如：这可被用于以太网硬件符合 OA TC10 的通信通道（参见 [5, OPEN Sleep/Wake-up Specification for Automotive Ethernet]）。

如果以 **ETH_MODE_ACTIVE** 或 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST** 调用 [**EthIf_SwitchPortGroupRequestMode**](#7326-ethif_switchportgrouprequestmode)，则应取消正在运行的、用于延迟关闭相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)（**PortGroupIdx**）所有端口的定时器。

如果对于所有引用该以太网控制器的以太网接口控制器都以 **ETH_MODE_DOWN** 调用了 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode)，则 **EthIf** 应以 **ETH_MODE_DOWN** 调用相应以太网控制器驱动程序（**EthIfPhysControllerIdx**）的 **&lt;EthDrv&gt;_SetControllerMode** 函数。

注意：

* 在支持 **VLAN** 的情况下，**EthIf** 必须在内部存储每个 [**EthIfController**](#924-ethifcontroller) 的状态，以便过滤来自上层的请求，并在 [**EthIfController**](#924-ethifcontroller) 被禁用时禁用到上层的调用。

如果以 **ETH_MODE_DOWN** 对某个 [**EthIfController**](#924-ethifcontroller) 调用 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 且该 [**EthIfController**](#924-ethifcontroller) 引用了 [**EthIfTransceiver**](#9212-ethiftransceiver)，那么在该 [**EthIfTransceiver**](#9212-ethiftransceiver) 的当前模式为 **ETH_MODE_ACTIVE** 时，**EthIf** 应按给定顺序将调用转发给以下函数：

1. **&lt;EthTrcv&gt;_SetTransceiverMode**，参数为 **ETH_MODE_DOWN**
2. **&lt;EthTrcv&gt;_TransceiverLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_DOWN**

如果以 **ETH_MODE_DOWN** 对某个 [**EthIfController**](#924-ethifcontroller) 调用 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 且该 [**EthIfController**](#924-ethifcontroller) 引用了 [**EthIfSwitch**](#9210-ethifswitch)，则 **EthIf** 应对所有 **EthSwtPort** 的当前模式为 **ETH_MODE_ACTIVE** 的端口，按给定顺序将调用转发给以下函数：

1. **EthSwt_PortLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_DOWN**
2. **EthSwt_SetSwitchPortMode**，参数为 **ETH_MODE_DOWN**

如果以 **ETH_MODE_DOWN** 对某个 [**EthIfController**](#924-ethifcontroller) 调用 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 且该 [**EthIfController**](#924-ethifcontroller) 引用了类型为 "control" 的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)，则 **EthIf** 应对相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 的所有 **EthSwtPort** 中、所有引用它的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 都已请求 **ETH_MODE_DOWN** 且当前模式为 **ETH_MODE_ACTIVE** 的端口，按给定顺序将调用转发给以下函数：

1. **EthSwt_PortLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_DOWN**
2. **EthSwt_SetSwitchPortMode**，参数为 **ETH_MODE_DOWN**

理由：如果相应 [**EthIfController**](#924-ethifcontroller) 没有引用 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)，或者引用类型为 "link information"，则请求的模式不会被转发。这些 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 会由上层（例如 **BswM**）通过 **API** 函数 [**EthIf_SwitchPortGroupRequestMode**](#7326-ethif_switchportgrouprequestmode) 请求。

#### 6.1.9.3. 附加的以太网交换机端口处理

引入以下附加的以太网交换机端口处理，是为了支持 ECU 被动唤醒的使用场景：此时相应以太网交换机的所有以太网交换机端口都应立即被打开，例如在发生唤醒之后。随后检查在 **EthIfPortStartupActiveTime** 时间窗口内是否通过 NM 帧接收到 PN 请求。如果收到 PN 请求，则相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 会以 **ETH_MODE_ACTIVE** 被请求，相应的以太网交换机端口保持活动状态。所有相应 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 未被请求的以太网交换机端口（由于在 **EthIfPortStartupActiveTime** 内未收到相应的 PN 请求）都会被关闭。

如果调用了 [**EthIf_StartAllPorts**](#7327-ethif_startallports)，则 **EthIf** 应对所有已配置 [**EthIfSwitch**](#9210-ethifswitch) 的所有 **EthSwtPort**，按给定顺序将调用转发给以下函数：

1. 如果当前模式为 **ETH_MODE_DOWN**，则以 **ETH_MODE_ACTIVE** 调用 **EthSwt_SetSwitchPortMode**。
2. 如果当前链路状态为 **ETHTRCV_LINK_STATE_DOWN**，则以 **ETHTRCV_LINK_STATE_ACTIVE** 调用 **EthSwt_PortLinkStateRequest**。

并为所有这些端口启动一个时长为 **EthIfPortStartupActiveTime** 的定时器。

在调用 [**EthIf_StartAllPorts**](#7327-ethif_startallports) 之后，**EthIf** 应按给定顺序调用以下函数，停用那些因 [**EthIf_StartAllPorts**](#7327-ethif_startallports) 而被激活、但在 **EthIfPortStartupActiveTime** 内未被以 **ETH_MODE_ACTIVE** 请求的端口：

1. **EthSwt_PortLinkStateRequest**，参数为 **ETHTRCV_LINK_STATE_DOWN**
2. **EthSwt_SetSwitchPortMode**，参数为 **ETH_MODE_DOWN**

理由：使用 **EthIfPortStartTime** 进行延迟是必要的，以确保带有 PNC 信息的 NM 消息能被接收，并使所请求的 PNC 被激活。

注意：

1. [**EthIf_StartAllPorts**](#7327-ethif_startallports) 可以在 **BswM_EcuM_CurrentWakeup** 的上下文中被调用。在唤醒线上发生唤醒之后，应激活所有 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)，以使通信栈能够接收 NM 消息（PNC 信息）。这样就可以在不启动 PNC 的情况下启动 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup)。
2. 关于在存在引用 [**EthIfSwitch**](#9210-ethifswitch) 的 [**EthIfController**](#924-ethifcontroller) 时切换 **EthSwtPort** 的更多需求，请参见 [6.1.9.2](#6192-ethifcontroller-和相应以太网硬件的切换) 节。

#### 6.1.10. 通信控制

以太网接口模块必须提供一种通信控制，以支持所谓的"静默通信"（**silent communication**）。静默通信用于模式管理，以支持这样一种通信模式：特定 [**EthIfController**](#924-ethifcontroller) 的发送路径被禁用，而接收路径仍然启用（参见 **COMM_SILENT_COMMUNICATION**）。发送路径的禁用在以太网接口模块中独占实现，对所使用以太网硬件没有影响。

如果以 **ETH_MODE_ACTIVE_TX_OFFLINE** 对某个 [**EthIfController**](#924-ethifcontroller) 调用 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode)，并且该 [**EthIfController**](#924-ethifcontroller) 最近一次被接受的控制器模式为 **ETH_MODE_ACTIVE** 或 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**，则应将 **ETH_MODE_TX_OFFLINE** 存储为当前控制器模式。否则，所请求的控制器模式应被拒绝，函数应以 **E_NOT_OK** 返回。

注意：与发送相关的 **API**（参见 [7.3.50](#7350-ethif_providetxbuffer) 节和 [7.3.51](#7351-ethif_transmit) 节）只有在所存储的通信模式为 **ETH_MODE_ACTIVE** 或 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST** 时，才会转发发送请求。

#### 6.1.11. 通信

以太网接口模块支持两种方式在底层和上层之间（或反向）传输数据。第一种是基于帧的（**frame-based**）通信方式，第二种是基于 **PDU** 的（**PDU-based**）通信方式。

##### 6.1.11.1. 基于帧的通信

基于帧的通信方式通过特定的 **API** 参数交换帧相关的信息。对于发送，采用一种双向 **API** 调用：

1. 上层调用 [**EthIf_ProvideTxBuffer**](#7350-ethif_providetxbuffer)，按照给定的优先级向以太网驱动程序请求一个发送方向的缓冲区。返回后，上层将数据复制到所提供的缓冲区中
2. 上层调用 [**EthIf_Transmit**](#7351-ethif_transmit)，请求以太网驱动程序发送发送方向缓冲区中的内容

发送的规格说明可在 [7.3.51](#7351-ethif_transmit) 小节和 [7.3.50](#7350-ethif_providetxbuffer) 小节中找到。

对于接收，使用 [**EthIf_RxIndication**](#741-ethif_rxindication)，并通过上层提供的 **RxIndication API**（例如 **TcpIp_RxIndication**）转发给所配置的上层。接收的规格说明可在 [7.4.1](#741-ethif_rxindication) 小节中找到。

在这两种情况下，**EthIf** 模块都充当直通（**path-through**）模块。这种方式用于服务于 [2, SWS TcpIp 模块] 和 [15, SWS TimeSyncOverEthernet 模块]。

##### 6.1.11.2. 基于PDU的通信

基于 **PDU** 的方式通过特定的 **PDU** 交换帧相关的信息。**API** 携带 **PduId** 和 **PduInfoPtr**。**PduId** 标识相应的 **PDU**。**PduInfoPtr** 包含 **SduDataPtr**（指向提供数据的缓冲区位置）和 **SduDataLength**（表示所提供数据的长度）。可选地，可以使用元数据（**meta data**）来传递额外的帧相关信息（参见 [6.1.11.4](#61114-元数据处理) 小节）。

注意：**EthIf** 模块通过 [18, SWS L-SDU 路由模块] 与上层（例如 [17, SWS IEEE1722Tp 模块]）交换 **PDU**。

对于基于帧的通信，配置 [**EthIfFrameOwnerConfig**](#925-ethifframeownerconfig) 即可满足需求，其中每个所有者（**owner**）被分配给一个 **EthIfFrameType**。**EthIfFrameType** 表示一种特定的帧类型（例如 0x22F01（**AVTP EtherType**））。相邻参数 **EthIfOwner** 定义 **RxIndication** 函数。**EthIf** 模块提供了额外配置 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 以表示基于 **PDU** 通信的可能性。一个 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 可以聚合多个 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry)。多个 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 构成一个所谓的「**PDU** 池（**PDU-pool**）」。一个 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 的 **EthIfFrameOwnerPduDirection** 可以设置为 **RX** 或 **TX**。**RX** 定义从 **EthIf** 模块到上层的通信方向。**TX** 定义从上层到 **EthIf** 模块的通信方向。

###### 6.1.11.2.1. 接收

如果通过调用 [**EthIf_RxIndication**](#741-ethif_rxindication) 指示 **EthIf** 接收一个以太网帧，则 **EthIf** 需要检查所接收以太网帧的帧类型是否与配置中的一个或多个 **EthIfFrameType** 匹配。如果匹配项配置了 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu)，则 **EthIf** 必须搜索一个可用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry)，如果某个 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 可用，则使用该 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 执行接收处理。接收被指示并转发给目标上层。目标上层接收一个指示。目标上层执行接收处理。可选地，如果接收处理已完成，上层可以通过调用 [**EthIf_ReleaseRxBuffer**](#7353-ethif_releaserxbuffer) 显式指示释放 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry)。此行为是可配置的，用于支持从底层缓冲区到上层目标接收缓冲区的硬件支持的数据传输（例如通过 **DMA**）。只要异步数据传输尚未完成，**EthCtrlConfigInressQueue** 元素就会被锁定，因此所使用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 也被锁定。对于后续的接收，必须使用相应 **PDU** 池中的另一个 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry)。只有当全局 **PDU** 被配置为 **KeepLocalPduBuffer** 设置为 **TRUE** 时，**EthIf** 才会期望收到 [**EthIf_ReleaseRxBuffer**](#7353-ethif_releaserxbuffer) 调用。**KeepLocalPduBuffer** 设置为 **TRUE** 表示目标上层可能触发硬件支持的数据传输。因此 **EthCtrlConfigInressQueue** 元素需要保持锁定，直到上层指示释放该 **EthCtrlConfigInressQueue** 元素。如果全局 **PDU** 被配置为 **KeepLocalPduBuffer** 设置为 **FALSE**，则 **EthIf** 模块在 **RxIndication** 函数调用返回后直接调用 **Eth_ReleaseRxBuffer**。

请注意：由于 **Eth** 驱动程序不感知 **PDU**（**PDU-aware**），**Eth** 驱动程序通过 [**EthIf_RxIndication**](#741-ethif_rxindication) 提供帧相关的 **API** 参数。

如果调用了 [**EthIf_RxIndication**](#741-ethif_rxindication) 且以下条件为真：

* 给定的 **FrameType** 与所配置 [**EthIfFrameOwnerConfig**](#925-ethifframeownerconfig) 的 **EthIfFrameType** 匹配
* 匹配的 [**EthIfFrameOwnerConfig**](#925-ethifframeownerconfig) 配置了一个 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu)
* 该 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 至少有一个 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 被配置为 **EthIfFrameOwnerPduDirection** 设置为 **RX**
* 该 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 处于 **PDU_AVAILABLE** 状态
* 给定以太网帧的 **VLAN-ID** 与所引用的 [**EthIfController**](#924-ethifcontroller) 匹配

则 **EthIf** 应执行以下操作。否则 **EthIf** 应中止对接收指示的处理：

* 将 **RxPduId** 设置为 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 所引用 **PDU** 的 **PDU-ID**
* 将给定的 **DataPtr** 和 **DataLen** 传递给所使用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 **PduInfoPtr**
* 如果 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 所引用的 **PDU** 配置了元数据项 **TIMETUPLE_TYPE_PTR**：
* -生成元数据项 **TIMETUPLE_TYPE_PTR** 并将给定的 **IngressTimeTuplePtr** 传递给所生成的元数据项 **TIMETUPLE_TYPE_PTR**
* -将所生成元数据项的指针添加到所使用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 **PduInfoPtr** 中
* 将 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 置为 **PDU_IN_USE** 状态
* 存储给定的 **RxHandleId** 与所使用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 **PDU-ID** 之间的映射
* 使用所创建的 **PduInfoPtr** 和所使用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 **RxPduId** 调用 **LSduR_EthIfRxIndication**

如果接收指示处理被中止，则 **EthIf** 应使用给定的 **RxHandleId** 调用 **Eth_ReleaseRxBuffer**。

如果 **LSduR_EthIfRxIndication** 返回，且所使用的 **PDU-ID** 指向一个 **KeepLocalPduBuffer** 设置为 **FALSE** 的全局 **PDU**，则 **EthIf** 应执行以下操作：

* 将受影响的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 置为 **PDU_AVAILABLE** 状态
* 释放为该 **PDU** 生成的本地缓冲区
* 移除 **RxHandleId** 与所使用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 **PDU-ID** 之间的映射
* 使用映射到给定 **RxPduId** 的 **RxHandleId** 调用 **Eth_ReleaseRxBuffer**

如果 **LSduR_EthIfRxIndication** 返回，且所使用的 **PDU-ID** 指向一个 **KeepLocalPduBuffer** 设置为 **TRUE** 的全局 **PDU**，则 **EthIf** 应保留本地缓冲区和所使用 **PDU** 的状态，直到针对所使用的 **PDU-ID** 调用了 [**EthIf_ReleaseRxBuffer**](#7353-ethif_releaserxbuffer)。

如果调用了 [**EthIf_ReleaseRxBuffer**](#7353-ethif_releaserxbuffer) 且以下条件为真：

* 给定的 **PduId** 指向一个存储了到相应 **RxHandleId** 映射的 **PDU-ID**
* 该 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 处于 **PDU_IN_USE** 状态

则 **EthIf** 应执行以下操作。否则该函数应以 **E_NOT_OK** 返回：

* 将受影响的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 置为 **PDU_AVAILABLE** 状态
* 释放为该 **PDU** 生成的本地缓冲区
* 移除 **RxHandleId** 与所使用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 **PDU-ID** 之间的映射
* 使用映射到给定 **RxPduId** 的 **RxHandleId** 调用 **Eth_ReleaseRxBuffer**

###### 6.1.11.2.2. 发送

如果通过调用 [**EthIf_ImmediateTransmit**](#7352-ethif_immediatetransmit) 请求 **EthIf** 发送数据，则 **EthIf** 需要检查给定的 **TxPduId** 是否可用；如果可用，则将给定的 **PduInfoPtr** 连同给定的元数据一起转换为 **Eth_ImmediateTransmit** 的基于帧的 **API** 调用。调用 [**EthIf_TxConfirmation**](#742-ethif_txconfirmation) 将释放带有 **TxPduId** 的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry)，并将确认转发给上层。

如果调用了 [**EthIf_ImmediateTransmit**](#7352-ethif_immediatetransmit) 且以下条件为真：

* 给定的 **TxPduId** 与所配置 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 的某个 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 所聚合的 **EthIfFrameOwnerPduId** 匹配
* 该 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 属于一个 **EthIfFrameOwnerPduDirection** 设置为 **TX** 的 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu)
* 匹配的 **EthIfFrameOwnerPduId** 所引用的 **PDU** 处于 **PDU_AVAILABLE** 状态

则 **EthIf** 应执行以下操作，作为调用 **Eth_ImmediateTransmit** 的准备。否则该函数应以 **E_NOT_OK** 返回：

* 将 **CtrlIdx** 参数设置为属于所引用 [**EthIfController**](#924-ethifcontroller) 的相应物理 **EthCtrl**
* 将 **TxHandleId** 参数设置为所使用的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 匹配的 **EthIfFrameOwnerPduId**
* 将优先级设置为聚合所使用 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 的 **EthIfFrameOwnerTxPriority** 配置值
* 按照 [7.3.51](#7351-ethif_transmit) 节的说明创建一个 **ListElemStructType** 类型的列表元素结构（**list-element-struct**），并将 **HeaderListPtr** 参数设置为所创建列表元素结构的地址
* 将 **PayloadPtr** 设置为随接收的 **PduInfoPtr** 给出的 **SduDataPtr**，并将 **PayloadLength** 设置为随接收的 **PduInfoPtr** 给出的 **SduDataLength**
* 调用 **Eth_ImmediateTransmit**，其中 **CtrlIdx**、**TxHandleId**、**priority**、**HeaderListPtr**、**PayloadPtr** 和 **PayloadLength** 按前述步骤所述设置

如果由于一个立即发送请求，**EthIf** 必须创建一个 **ListElemStructType** 类型的列表元素结构，且给定的 **TxPduId** 与引用了配置 **MetaDataItemType** 为 **ETHERNET_MAC_64** 的 **PDU** 的 **EthIfFrameOwnerPduId** 匹配，则 **EthIf** 在创建 **ListElemStructType** 类型的列表元素结构时应考虑以下几点：

* 从元数据项 **ETHERNET_MAC_64** 中取用目标 **MAC** 地址
* 从与相应 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 所引用的 [**EthIfPhysController**](#926-ethifphyscontroller) 对应的 **EthCtrl** 导出源 **MAC** 地址
* 使用聚合了引用所使用 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 的 [**EthIfFrameOwnerConfig**](#925-ethifframeownerconfig) 的 **EthIfFrameType**
* 导出所使用 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 所引用 [**EthIfController**](#924-ethifcontroller) 的 **VLAN-ID**
* 使用聚合所使用 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 的 **EthIfFrameOwnerTxPriority** 配置的优先级值
* 按照 [19, IEEE 802.3 Std 2022] 创建以太网报头（**DstMacAdr;SrcMacAdr;QTag;EtherType**），并将指向所构造报头的指针用作列表元素结构的 **DataPtr**，将以太网报头的长度用作其 **DataLength**
* 如果所引用的 **PDU** 配置了 **MetaDataItemType** 为 **LISTELEM_PTR**，则从元数据项 **LISTELEM_PTR** 中取用 **HeaderListPtr**，并将所创建列表元素结构的 **NextListElemPtr** 设置为所取用的 **HeaderListPtr** 的地址。否则将所创建列表元素结构的 **NextListElemPtr** 设置为 **NULL_PTR**

如果 **Eth_ImmediateTransmit** 返回 **E_OK**，且所使用的 **PDU-ID** 指向一个 **KeepLocalPduBuffer** 设置为 **TRUE** 的全局 **PDU**，则 **EthIf** 应保留本地缓冲区和所使用 **PDU** 的状态，直到针对所使用的 **PDU-ID** 调用了 [**EthIf_TxConfirmation**](#742-ethif_txconfirmation)。在 **EthIf** 调用 **Eth_ImmediateTransmit** 的所有其他情况下，应释放受影响 **PDU** 的本地生成数据的缓冲区。

如果调用了 [**EthIf_TxConfirmation**](#742-ethif_txconfirmation) 且以下条件为真：

* 给定的 **BufIdx** 和 **CtrlIdx** 指向一个 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry)（在之前调用 **Eth_ImmediateTransmit** 时作为 **TxHandleId** 给出）
* 受影响的 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 处于 **PDU_IN_USE** 状态

则 **EthIf** 应执行以下操作，否则中止发送处理并返回：

* 将 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的受影响 **PDU** 置为 **PDU_AVAILABLE** 状态
* 调用 **LSduR_EthIfTxConfirmation**，其中 **TxPduId** 设置为 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 所引用的 **PDU-ID**

##### 6.1.11.3. PDU的状态处理

**EthIf** 模块必须维护相应 **PDU** 池中 **PDU** 的使用状态（**usage-state**）。因此 **PDU** 有两种状态：**PDU_IN_USE** 或 **PDU_AVAILABLE**。

注意：**PDU_IN_USE** 或 **PDU_AVAILABLE** 的定义仅表示功能行为，而不表示实现方式，因为 **PDU** 的状态在本地维护，不会传播到其他模块。因此，没有为 **PDU** 状态定义任何类型。

**EthIf** 模块应为所有已配置 [**EthIfFrameOwnerPduPoolEntry**](#92511-ethifframeownerpdupoolentry) 的每个 **PDU** 维护两种状态：**PDU_AVAILABLE** 状态和 **PDU_IN_USE** 状态。

如果 **EthIf** 模块被请求发送数据或被指示接收数据，或者指示了发送确认或释放接收缓冲区，则 **EthIf** 模块应根据给定的 **PDU-ID** 检查该 **PDU** 的状态：

* 如果给定 **PDU-ID** 的 **PDU** 处于 **PDU_AVAILABLE** 状态且被请求发送或被指示接收，则 **EthIf** 模块应将该 **PDU** 的状态置为 **PDU_IN_USE**。否则 **EthIf** 模块应中止后续处理，报告运行时错误 [**ETHIF_E_PDU_STATE_TRANSITION_FAILED**](#632-运行时错误)，并在可能的情况下以 **E_NOT_OK** 返回。
* 如果给定 **PDU-ID** 的 **PDU** 处于 **PDU_IN_USE** 状态且指示了发送确认或释放接收缓冲区，则 **EthIf** 模块应将该 **PDU** 的状态置为 **PDU_AVAILABLE**。否则 **EthIf** 模块应中止后续处理，报告运行时错误 [**ETHIF_E_PDU_STATE_TRANSITION_FAILED**](#632-运行时错误) 并返回。

如果请求 **EthIf** 模块发送数据且函数调用 **Eth_ImmediateTransmit** 返回 **E_NOT_OK**，则 **IEEE1722Tp** 模块应将受影响 **PDU** 的状态置为 **PDU_AVAILABLE**。

##### 6.1.11.4. 元数据处理

**EthIf** 模块按照 [6, CP-SWS-BSWGeneral] 的规定使用元数据。元数据通过 **MetaDataPtr** 寻址，它是 **PduInfoPtr** 的一部分。基本上，**EthIf** 模块充当中间层，将来自以太网驱动程序的所提供（基于帧的）数据作为 **PDU** 传输给上层，并将来自上层通信协议栈的 **PDU** 作为帧相关的 **API** 调用传输给以太网驱动程序。在两个方向上，**EthIf** 模块都需要在基于帧的方式和基于 **PDU** 的方式之间进行相互转换。必须考虑以下通信场景：

* UpperLayer-To-LowerLayer-TxData：上层（例如 **IEEE1722Tp**）通过 **LSduR** 模块向 **EthIf** 进行数据发送
* LowerLayer-To-UpperLayer-RxData：**EthIf** 接收以太网帧的指示，将数据转换为基于 **PDU** 的方式，并通过 **LSduR** 将数据转发给上层（例如 **IEEE1722Tp**）

###### 6.1.11.4.1. 元数据类型

本小节描述 **EthIf** 所生成或使用的预期元数据类型。

**EthIfFrameOwnerPduDirection** 设置为 **RX** 的 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 所引用的 **PDU**，除以下元数据项类型外不得配置任何其他 **MetaDataItem**：

* **TIMETUPLE_TYPE_PTR**

**EthIfFrameOwnerPduDirection** 设置为 **TX** 的 [**EthIfFrameOwnerPdu**](#9251-ethifframeownerpdu) 所引用的 **PDU**，除以下元数据项类型外不得配置任何其他 **MetaDataItem**：

* **ETHERNET_MAC_64**
* **TIMETUPLE_TYPE_PTR**
* **LISTELEM_PTR**

##### 6.1.11.5. 入方向队列处理

以太网接口模块支持不同的入方向队列（**ingress queue**）处理方式。入方向队列的处理在很大程度上取决于以太网驱动程序上下文中配置的入方向队列处理方式。以太网驱动程序支持以下方式：

* 特定以太网控制器的所有入方向队列都在中断模式下处理
* 特定以太网控制器的所有入方向队列都在轮询模式下处理
* 特定以太网控制器的特定入方向队列在中断模式下处理，其余入方向队列在轮询模式下处理

轮询模式需要区分哪个函数负责轮询特定的入方向队列：

1. 如果一个 [**EthIfPhysController**](#926-ethifphyscontroller) 通过 **EthIfPhysCtrlRxMainFunctionIngressProcessing** 引用多个入方向队列，则被引用的队列在一个特定的 **EthIf_MainFunctionRx_&lt;IngressQueueProcessing ShortName&gt;** 中处理
2. 如果一个 [**EthIfPhysController**](#926-ethifphyscontroller) 的相应 **EthController** 配置了带有 **EthCtrlConfigIngressQueueHandlerFunction** 的入方向队列，则该入方向队列在一个特定的入方向队列处理函数中处理。该函数的调度是集成相关的（例如由 **CDD** 调度或映射到某个 **Os** 任务）
3. 所有未配置特定入方向队列处理函数的入方向队列，都在 [**EthIf_MainFunctionRx**](#751-ethif_mainfunctionrx) 的上下文中处理

以太网驱动程序支持在中断模式下处理特定的入方向队列。[**EthIfPhysController**](#926-ethifphyscontroller) 可以配置多个 **Rx** 主函数，通过使用 **EthIfPhysCtrlRxMainFunctionIngressProcessing** 来处理特定的入方向队列。一个 **EthIfPhysCtrlRxMainFunctionIngressProcessing** 可以通过 **EthIfCanXLCtrlRxIngressFifoRef** 或 **EthIfPhysCtrlRxIngressQueueRef** 引用一个入方向队列。伴随该引用会生成一个特定的主函数（参见 **EthIf_MainFunctionRx_&lt;IngressQueueProcessing ShortName&gt;**），入方向队列处理程序在该主函数中实现。

如果 [**EthIfPhysController**](#926-ethifphyscontroller) 配置了 **EthIfPhysCtrlRxMainFunctionIngressProcessing** 并通过 **EthIfPhysCtrlRxIngressQueueRef** 或 **EthIfCanXLCtrlRxIngressFifoRef** 引用入方向队列，则当被引用的入方向队列既未将 **EthCtrlConfigIngressQueueHandlerFunction** 配置为某函数、也未将 **EthCtrlEnableIngressQueueInterrupt** 设置为 **TRUE** 时，该配置应被判定为有效。

如果 [**EthIfPhysController**](#926-ethifphyscontroller) 配置了 **EthIfPhysCtrlRxMainFunctionIngressProcessing**，则通过 **EthIfPhysCtrlRxIngressQueueRef** 或 **EthIfCanXLCtrlRxIngressFifoRef** 引用的入方向队列应由相应的 **EthIf_MainFunctionRx_&lt;IngressQueueProcessing ShortName&gt;** 处理。

通用的 [**EthIf_MainFunctionRx**](#751-ethif_mainfunctionrx) 可以对所有未由其他入方向队列处理函数处理的入方向队列执行轮询。其他入方向队列处理函数可以由 **EthIf** 或 **Eth** 驱动程序提供。其他处理函数的存在会影响 [**EthIf_MainFunctionRx**](#751-ethif_mainfunctionrx) 的入方向队列处理。

如果 **EthIf** 的 **EthIfEnableRxInterrupt** 设置为 **FALSE**，则 [**EthIf_MainFunctionRx**](#751-ethif_mainfunctionrx) 应对所有满足以下全部条件的入方向队列执行轮询：

* 某个入方向队列既未被 **EthIfPhysCtrlRxIngressQueueRef** 也未被 **EthIfCanXLCtrlRxIngressFifoRef** 引用
* 以太网驱动程序处的某个入方向队列的 **EthCtrlEnableIngressQueueInterrupt** 设置为 **FALSE**
* 以太网驱动程序处的某个入方向队列未配置 **EthCtrlConfigIngressQueueHandlerFunction**

#### 6.1.12. 全局时间支持

关于交换机时间测量的更多细节，请参阅 [20, 以太网交换机驱动程序规范]。

#### 6.1.13. 无线以太网支持

以太网接口应支持无线以太网（**Wireless Ethernet**）的特定功能，取决于参数 **EthIfEnableWEthApi**。

无线功能分为控制器特定功能和收发器特定功能。主要是与 **EthIf** 上层模块及控制器/收发器交换发送和接收参数。

仅针对缓冲区特定的发送和接收参数调用控制器，所用的 **API** 为：

* [**EthIf_GetBufWRxParams**](#7343-ethif_getbufwrxparams)
* [**EthIf_GetBufWTxParams**](#7344-ethif_getbufwtxparams)
* [**EthIf_SetBufWTxParams**](#7345-ethif_setbufwtxparams)

针对无线射频（**radio**）和无线射频信道的常规配置调用收发器，所用的 **API** 为：

* [**EthIf_SetRadioParams**](#7346-ethif_setradioparams)
* [**EthIf_SetChanRxParams**](#7347-ethif_setchanrxparams)
* [**EthIf_SetChanTxParams**](#7348-ethif_setchantxparams)
* [**EthIf_GetChanRxParams**](#7349-ethif_getchanrxparams)

参数值通过唯一的参数标识符进行请求或传输。这些参数标识符定义在控制器和收发器规范 [\[16\]](#ref-16) [\[21\]](#ref-21) 中。

#### 6.1.14. 蜂窝V2X支持

以太网接口应支持蜂窝 **V2X**（**Cellular V2X**）的特定功能，取决于参数 **EthIfEnableCV2xApi**。

与 **EthIf** 上层模块及控制器交换发送和接收参数。仅针对缓冲区特定的发送和接收参数调用控制器，所用的 **API** 为：

* [**EthIf_GetBufCV2xPC5RxParams**](#7386-ethif_getbufcv2xpc5rxparams)
* [**EthIf_GetBufCV2xPC5TxParams**](#7387-ethif_getbufcv2xpc5txparams)
* [**EthIf_SetBufCV2xPC5TxParams**](#7388-ethif_setbufcv2xpc5txparams)

针对蜂窝 **V2X** 射频和蜂窝 **V2X** 射频信道的常规配置调用控制器，所用的 **API** 为：

* [**EthIf_GetChanCV2xPC5TxParams**](#7389-ethif_getchancv2xpc5txparams)

参数值通过唯一的参数标识符进行请求或传输。这些参数标识符定义在控制器规范 [\[22\]](#ref-22) 中。

#### 6.1.15. MACsec支持

以太网接口应支持将 **MACsec** 作为软件实现，如 [\[23\]](#ref-23) 中所规定。

以太网接口应支持配置哪些以太网接口控制器受 **MACsec** 保护。

以太网接口应支持为每个以太网接口控制器配置要使用的 **MACsec** 实体（**MACsec Entity**）（软件或硬件，即卸载（**offloaded**）实现）。

注意：这通过参数 **EthIfMacSecSupport** 随配置包含。

以太网接口的软件 **MACsec** 实体应提供一种机制，以配置基于 **EtherType** 和/或 **VLAN-ID** 对传入和传出流量绕过（**bypass**）**MACsec** 的规则。所有未配置为绕过流量的流量都应由 **MACsec** 实体处理或丢弃。此配置应在端口的初始配置时得到支持。

以太网接口的软件 **MACsec** 实体应支持以下信息的状态计数器，这些信息可附加到 **IDSM** 功能：

* 每端口因 **ICV** 不正确而丢弃的帧。
* 每对等端（**peer**）不成功的 **MKA** 序列。
* 此外，还包括 [\[23\]](#ref-23) 所要求的全部端口统计信息。

以太网接口的软件 **MACsec** 实体应为所有支持的密码套件（**cipher**）支持「仅完整性」（**Integrity only**）以及「完整性与机密性」（**Integrity with Confidentiality**）。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的 **MAC** 安全标签（**MAC Security TAG**，**SecTAG**）。**SecTAG** 应传递：

* 标签控制信息（**TAG Control Information**，**TCI**）
* 关联编号（**Association Number**，**AN**）
* 短长度（**Short Length**，**SL**）
* 包编号（**Packet Number**，**PN**）
* 安全通道标识符（**Secure Channel Identifier**，**SCI**）— 可选

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的 **MACsec EtherType**。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的标签控制信息（**TCI**）。**TCI** 应编码在 **SecTAG** 中。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的关联编号（**AN**）。**AN** 应编码在 **SecTAG** 中。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的短长度（**SL**）。**SL** 应编码在 **SecTAG** 中。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的、具有 32 个最低有效位的包编号（**PN**）。**PN** 应编码在 **SecTAG** 中。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的扩展包编号（**Extended Packet Number**，**XPN**）。**XPN** 将 **PN** 扩展到 64 位。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的安全通道标识符（**SCI**）。如果需要发送 **SCI**，则 **SCI** 可编码在 **SecTAG** 中。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的安全数据（**Secure Data**）。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中定义的完整性校验值（**Integrity check value**，**ICV**）。**ICV** 的长度取决于所使用的密码套件，但不小于 8 个八位组（**octet**），不大于 16 个八位组。发送的 **ICV** 始终为 16 个八位组。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中规定的保护（**protect**）功能。

以太网接口的软件 **MACsec** 实体应支持 [\[23\]](#ref-23) 中规定的验证（**validation**）功能。

以太网接口的软件 **MACsec** 实体应支持以下密码套件：

* GCM-AES-128
* GCM-AES-256
* GCM-AES-XPN-128
* GCM-AES-XPN-256

以太网接口的软件 **MACsec** 实体应支持 **MACsec ICV** 的验证功能。

以太网接口的软件 **MACsec** 实体应支持 **MACsec ICV** 的生成功能。

以太网接口模块应在共享同一物理或虚拟受控端口（**controlled port**）的以太网接口控制器之间共享 **MACsec** 操作（**Operational**）状态。以太网接口控制器在从交换机或收发器接收到「模式指示」（**Mode Indication**）（通过相应函数 [**EthIf_SwitchPortModeIndication**](#745-ethif_switchportmodeindication) 或 [**EthIf_TrcvModeIndication**](#744-ethif_trcvmodeindication)）后，应触发 **MKA** 模块在带有 **MKA_LinkStateChange** 的端口上启动 **MKA** 序列。

一旦物理或虚拟端口能够生成和验证 **MACsec** 流量（由 [**EthIf_MacSecOperational**](#73121-ethif_macsecoperational) 发出信号），所有使用该虚拟或物理端口的控制器应立即通过 **EthSM_TrcvLinkStateChg** 将 **MacSecOperational** 状态通告给上层。

以太网接口模块应支持 [\[23\]](#ref-23) 中定义的与 **MKA** 相关的 **EtherType**。

以太网接口模块应允许在已配置的情况下，将接收到的特定 **EtherType** 的以太网帧转发给多个帧所有者。

#### 6.1.16. 防火墙支持

以太网协议栈通过防火墙（**firewall**）模块支持对网络数据包的防火墙过滤。防火墙支持由参数 **EthIfFwSupport** 管理。

如果 **EthIfFwSupport** 设置为 **FIREWALL_WITHOUT_PERSTREAMFILTERING**，则 **EthIf** 应对它接收到的每个网络数据包调用 **Fw_InspectPacket**。**StreamHandleIdxPtr** 应设置为 **NULL**。

如果 **EthIfFwSupport** 设置为 **FIREWALL_WITH_PERSTREAMFILTERING**，则 **EthIf** 应在调用 **Fw_InspectPacket** 之前调用 **EthSwt_ExtractStreamHandleIdx** 来设置 **StreamHandleIdxPtr**。

**EthIf** 应在执行 [[6.2.1](#621-ethif-的安全事件) 章] 中规定的引发 **SEv** 的检查之前调用 **EthSwt_ExtractStreamHandleIdx**。

如果 **Fw_InspectPacket** 返回 **E_OK** 且 **InspectionResultPtr** 被设置为 **FW_BLOCK_NETWORK_PACKET**，则 **EthIf** 模块应丢弃该网络数据包，不作任何进一步通知。

如果 **Fw_InspectPacket** 返回 **E_OK** 且 **InspectionResultPtr** 被设置为 **FW_ALLOW_NETWORK_PACKET**，则 **EthIf** 模块应将该网络数据包转发到下一层。

##### 6.1.16.1. 向交换机的调用转发

在某些用例中，防火墙与以太网交换机驱动程序有一些交互。因此 **EthIf** 模块必须转发这些调用。

如果调用了 [**EthIf_GetStreamHandleIdxStatistics**](#73124-ethif_getstreamhandleidxstatistics)，则 **EthIf** 模块应使用相同的参数调用 **EthSwt_GetStreamHandleIdxStatistics**。当相应的回调函数 [**EthIf_StreamHandleIdxStatistics**](#748-ethif_streamhandleidxstatistics) 被调用时，**EthIf** 模块应使用相同的参数调用 **Fw_StreamHandleIdxStatistics**。

如果调用了 [**EthIf_SetStreamHandleIdxConfiguration**](#73125-ethif_setstreamhandleidxconfiguration)，则 **EthIf** 模块应使用相同的参数调用 **EthSwt_SetStreamHandleIdxConfiguration**。当相应的回调函数 [**EthIf_StreamHandleIdxConfiguration**](#747-ethif_streamhandleidxconfiguration) 被调用时，**EthIf** 模块应使用相同的参数调用 **Fw_StreamHandleIdxConfiguration**。

### 6.2. 安全事件

如果已为 **EthIf** 模块启用安全事件报告（**EthIfEnableSecurityEventReporting** = **true**），则应通过 **AUTOSAR_SWS_BSWGeneral** [\[6\]](#ref-6) 中定义的接口将相应的安全事件报告给 **IdsM**。

下表列出了为 **EthIf** 标准化的安全事件及其触发条件：

#### 6.2.1. EthIf 的安全事件

| 名称 | 描述 | ID |
| --- | --- | --- |
| SEV_ETH_DROP_UNKNOWN_ETHERTYPE | 由于 **EtherType** 未知而丢弃了以太网数据报。 | 15 |
| SEV_ETH_DROP_VLAN_DOUBLE_TAG | 由于双重 **VLAN** 标签而丢弃了以太网数据报。 | 16 |
| SEV_ETH_DROP_INV_VLAN | 由于无效的控制器索引/**VLAN** 而丢弃了以太网数据报。 | 17 |
| SEV_ETH_DROP_MAC_COLLISION | 由于本地 **MAC** 与传入帧中的源 **MAC** 相同而丢弃了以太网数据报。 | 18 |

**EthIf** 不为这些安全事件提供上下文数据（**context data**）。

### 6.3. 错误分类

文档 [\[6\]](#ref-6)「基础软件模块通用规范」（**General Specification of Basic Software Modules**）的「错误处理」（**Error Handling**）章节详细描述了基础软件的错误处理。其中最重要的是，它构成了一个由五种错误类型组成的分类方案，这些错误类型可能发生在 **BSW** 模块中。

基于此基础，以下章节在相应的小节中规定特定的错误。

#### 6.3.1. 开发错误

| 错误类型 | 相关错误码 | 错误值 |
| --- | --- | --- |
| 使用无效的控制器索引调用API服务 | ETHIF_E_INV_CTRL_IDX | 0x01 |
| 使用无效的收发器索引调用API服务 | ETHIF_E_INV_TRCV_IDX | 0x02 |
| 使用无效的交换机索引调用API服务 | ETHIF_E_INV_SWT_IDX | 0x03 |
| 使用无效的端口组索引调用API服务 | ETHIF_E_INV_PORT_GROUP_IDX | 0x04 |
| 在 **EthIf** 模块未初始化的情况下调用API服务 | ETHIF_E_UNINIT | 0x05 |
| 使用参数列表中的无效指针调用API服务 | ETHIF_E_PARAM_POINTER | 0x06 |
| 使用无效参数调用API服务 | ETHIF_E_INV_PARAM | 0x07 |
| 使用无效的配置指针调用 [**EthIf_Init**](#731-ethif_init) | ETHIF_E_INIT_FAILED | 0x08 |
| 无效的端口索引 | ETHIF_E_INV_PORT_IDX | 0x09 |

#### 6.3.2. 运行时错误

| 错误类型 | 相关错误码 | 错误值 |
| --- | --- | --- |
| 请求使用一个已处于使用中的 **PDU**，或请求将一个已处于可用状态的 **PDU** 置为可用 | ETHIF_E_PDU_STATE_TRANSITION_FAILED | 0x01 |

#### 6.3.3. 瞬态故障

没有瞬态故障。

#### 6.3.4. 生产错误

没有生产错误。

#### 6.3.5. 扩展生产错误

没有扩展生产错误。


## 7. API规范

### 7.1. 导入的类型

在本章中列出了从以下模块包含的所有类型：

| 模块 | 头文件 | 导入的类型 |
| --- | --- | --- |
| ComStack_Types | ComStack_Types.h | BufReq_ReturnType |
| ComStack_Types | ComStack_Types.h | ListElemStructType（draft） |
| ComStack_Types | ComStack_Types.h | PduIdType |
| ComStack_Types | ComStack_Types.h | PduInfoType |
| ComStack_Types | ComStack_Types.h | PduLengthType |
| ComStack_Types | ComStackTypes.h | TimeStampQualType（draft） |
| ComStack_Types | ComStackTypes.h | TimeStampType（draft） |
| ComStack_Types | ComStackTypes.h | TimeTupleType（draft） |
| CV2x | CV2x_GeneralTypes.h | CV2x_BufCV2xPC5RxParamIdType（draft） |
| CV2x | CV2x_GeneralTypes.h | CV2x_BufCV2xPC5TxParamIdType（draft） |
| CV2x | CV2x_GeneralTypes.h | CV2x_GetChanTxParamIdType（draft） |
| EcuM | EcuM.h | EcuM_WakeupSourceType |
| Eth | Eth.h | Eth_SpiStatusType（draft） |
| Eth | Eth_GeneralTypes.h | Eth_BufIdxType |
| Eth | Eth_GeneralTypes.h | Eth_CounterType |
| Eth | Eth_GeneralTypes.h | Eth_DataType |
| Eth | Eth_GeneralTypes.h | Eth_FilterActionType |
| Eth | Eth_GeneralTypes.h | Eth_FrameType |
| Eth | Eth_GeneralTypes.h | Eth_MacVlanType |
| Eth | Eth_GeneralTypes.h | Eth_ModeType |
| Eth | Eth_GeneralTypes.h | Eth_RxStatsType |
| Eth | Eth_GeneralTypes.h | Eth_RxStatusType |
| Eth | Eth_GeneralTypes.h | Eth_TimeStampQualType（obsolete） |
| Eth | Eth_GeneralTypes.h | Eth_TimeStampType（obsolete） |
| Eth | Eth_GeneralTypes.h | Eth_TxErrorCounterValuesType |
| Eth | Eth_GeneralTypes.h | Eth_TxStatsType |
| EthSwt | Eth_GeneralTypes.h | EthSwt_MacLearningType |
| EthSwt | Eth_GeneralTypes.h | EthSwt_MgmtInfoType |
| EthSwt | Eth_GeneralTypes.h | EthSwt_MgmtObjectType |
| EthSwt | Eth_GeneralTypes.h | EthSwt_MgmtObjectValidType |
| EthSwt | Eth_GeneralTypes.h | EthSwt_MgmtOwner |
| EthSwt | Eth_GeneralTypes.h | EthSwt_PortMirrorCfgType |
| EthSwt | Eth_GeneralTypes.h | EthSwt_PortMirrorStateType |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_BaudRateType |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_CableDiagResultType |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_DuplexModeType |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_LinkStateType |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_MacMethodType（draft） |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_PhyLoopbackModeType |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_PhyTestModeType |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_PhyTxModeType |
| EthTrcv | Eth_GeneralTypes.h | EthTrcv_WakeupReasonType |
| Fw | Fw_Types.h | Fw_InspectionResultType（draft） |
| IdsM | IdsM_Types.h | IdsM_SecurityEventIdType |
| Mka | Mka.h | Mka_ConfidentialityOffsetType（DRAFT） |
| Mka | Mka.h | Mka_MacSecConfigType（DRAFT） |
| Mka | Mka.h | Mka_SakKeyPtrType（DRAFT） |
| Mka | Mka.h | Mka_Stats_Rx_ScType（DRAFT） |
| Mka | Mka.h | Mka_Stats_Rx_SecYType（DRAFT） |
| Mka | Mka.h | Mka_Stats_SecYType（DRAFT） |
| Mka | Mka.h | Mka_Stats_Tx_ScType（DRAFT） |
| Mka | Mka.h | Mka_Stats_Tx_SecYType（DRAFT） |
| Mka | Mka.h | Mka_ValidateFramesType（DRAFT） |
| Std | Std_Types.h | Std_ReturnType |
| Std | Std_Types.h | Std_VersionInfoType |
| WEth | WEth_GeneralTypes.h | WEth_BufWRxParamIdType |
| WEth | WEth_GeneralTypes.h | WEth_BufWTxParamIdType |
| WEthTrcv | WEth_GeneralTypes.h | WEthTrcv_GetChanRxParamIdType |
| WEthTrcv | WEth_GeneralTypes.h | WEthTrcv_SetChanRxParamIdType |
| WEthTrcv | WEth_GeneralTypes.h | WEthTrcv_SetChanTxParamIdType |
| WEthTrcv | WEth_GeneralTypes.h | WEthTrcv_SetRadioParamIdType |

### 7.2. 类型定义

#### 7.2.1. EthIf_ConfigType

结构类型（**Structure**），构建后配置（**post build configuration**）的实现特定（**Implementation specific**）结构。可通过**EthIf.h**获得。

#### 7.2.2. EthIf_SwitchPortGroupIdxType

类型（**Type**），派生自**uint8**。取值范围：0..255。表示以太网接口交换机端口组索引的数据类型。该索引从零开始，对每个已配置的交换机端口组是唯一的。可通过**EthIf.h**获得。

#### 7.2.3. EthIf_MeasurementIdxType

类型（**Type**），派生自**uint8**。取值范围：**ETHIF_MEAS_DROP_CRTLIDX**（0x01）：由无效的控制器索引/**VLAN** 导致的数据报丢弃的测量索引；**ETHIF_MEAS_RESERVED_1**（0x02-0x7F）：由 **AUTOSAR** 保留；**ETHIF_MEAS_RESERVED_2**（0x80-0xEF）：供应商特定范围；**ETHIF_MEAS_RESERVED_3**（0xF0-0xFE）：由 **AUTOSAR** 保留（供将来使用）；**ETHIF_MEAS_ALL**（0xFF）：表示所有测量索引。用于选择特定测量数据的索引。可通过**EthIf.h**获得。

#### 7.2.4. EthIf_SignalQualityResultType

结构类型（**Structure**），包含以下元素：**HighestSignalQuality**（类型 **uint32**）：自上次清除以来链路的最高信号质量；**LowestSignalQuality**（类型 **uint32**）：自上次清除以来链路的最低信号质量；**ActualSignalQuality**（类型 **uint32**）：实际信号质量。可通过**EthIf.h**获得。

### 7.3. 函数定义

这是提供给上层模块的函数列表。

注意：本章中的所有函数都要求事先进行初始化（[**EthIf_Init**](#731-ethif_init)），但以下函数除外：[**EthIf_Init**](#731-ethif_init)、[**EthIf_GetVersionInfo**](#7354-ethif_getversioninfo)。

#### 7.3.1. EthIf_Init

**说明**: 初始化以太网接口。本服务为同步调用，不可重入。参数 CfgPtr（in）：指向实现特定结构的指针。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_Init ( const EthIf_ConfigType* CfgPtr )
```

该函数应存储对配置结构的访问，供后续的 **API** 调用使用。

该函数应将组件的状态从未初始化更改为已初始化。

如果启用了开发错误检测：该函数应检查参数 **CfgPtr** 是否包含有效的配置。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INIT_FAILED**](#631-开发错误)。

#### 7.3.2. EthIf_SetControllerMode

**说明**: 启用/禁用被索引的控制器。本服务为异步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 CtrlMode（in）：**ETH_MODE_DOWN**：禁用控制器；**ETH_MODE_ACTIVE**：启用控制器；**ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**：启用控制器并请求网络上的唤醒；**ETH_MODE_TX_OFFLINE**：禁用 **EthIf** 中的发送处理。请注意，相应的以太网控制器不受影响。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法更改控制器模式。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetControllerMode ( uint8 CtrlIdx, Eth_ModeType CtrlMode )
```

注意：关于调用 **EthIf_SetControllerMode** 的更多需求在 [6.1.9.2](#6192-ethifcontroller-和相应以太网硬件的切换) 章节和 [6.1.10](#6110-通信控制) 章节中描述。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

#### 7.3.3. EthIf_GetControllerMode

**说明**: 获取被索引控制器的状态。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 CtrlModePtr（out）：**ETH_MODE_DOWN**：控制器被禁用；**ETH_MODE_ACTIVE**：控制器被启用。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：控制器无法初始化。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetControllerMode ( uint8 CtrlIdx, Eth_ModeType* CtrlModePtr )
```

函数 **EthIf_GetControllerMode** 应将调用转发给相应以太网控制器驱动程序（**EthIfPhysControllerIdx**）的 **&lt;EthDrv&gt;_GetControllerMode** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlModePtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.4. EthIf_CheckWakeup

**说明**: 此 **API** 请求受影响的以太网硬件检查是否有被通知的唤醒。所使用的以太网硬件可以是以太网交换机或以太网收发器（**PHY**）。例如，这可用于符合 Open Alliance **TC10** 规范的以太网硬件。此 **API** 由集成代码调用。该函数可以在中断上下文或任务层中被调用。本服务为异步调用，可重入。参数 WakeupSource（in）：发起唤醒事件的源设备。源设备可以是以太网交换机或以太网收发器。返回值 **Std_ReturnType**：**E_OK**：检查受影响以太网硬件（例如 **PHY**）唤醒的请求已被接受；**E_NOT_OK**：检查受影响以太网硬件唤醒的请求被拒绝。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_CheckWakeup ( EcuM_WakeupSourceType WakeupSource )
```

对于所有受影响的以太网收发器（由 [**EthIfTransceiver**](#9212-ethiftransceiver) 或 **EthIfSwitchPortGroups** 引用），函数 **EthIf_CheckWakeup** 应将调用转发给相应以太网收发器驱动程序的 **&lt;EthTrcv&gt;_CheckWakeup** 函数。该调用对每个以太网收发器只应转发一次。

注意：如果多个 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 和/或多个 [**EthIfController**](#924-ethifcontroller) 引用同一个 [**EthIfTransceiver**](#9212-ethiftransceiver)，则该需求可避免多次调用。

对于所有受影响的以太网交换机（由 [**EthIfSwitch**](#9210-ethifswitch) 引用），函数 **EthIf_CheckWakeup** 应将调用转发给相应以太网交换机驱动程序的 **EthSwt_SwitchCheckWakeup** 函数。该调用对每个以太网交换机只应转发一次。

注意：如果多个 [**EthIfController**](#924-ethifcontroller) 引用同一个 [**EthIfSwitch**](#9210-ethifswitch)，则该需求可避免多次调用。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **WakeupSource** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

#### 7.3.5. EthIf_GetPhyWakeupReason

**说明**: 此函数通过调用 **EthTrcv_GetBusWuReason(...)** 获取被索引以太网收发器（**PHY**）的唤醒原因。本服务为同步调用，可重入。参数 TrcvIdx（in）：以太网接口上下文中收发器的索引。参数 WakeupReasonPtr（out）：指向由以太网 **PHY** 检测到的最近一次唤醒事件结构的指针。返回值 **Std_ReturnType**：**E_OK**：**PHY** 唤醒原因请求已被接受；**E_NOT_OK**：**PHY** 唤醒原因请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetPhyWakeupReason ( uint8 TrcvIdx, EthTrcv_WakeupReasonType* WakeupReasonPtr )
```

函数 **EthIf_GetPhyWakeupReason** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_GetBusWuReason** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **WakeupReasonPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.6. EthIf_GetSwitchPortWakeupReason

**说明**: 此函数通过调用 **EthSwt_GetSwitchPortWakeupReason()** 获取被索引以太网交换机端口的唤醒原因。本服务为同步调用，可重入。参数 SwitchIdx（in）：以太网接口上下文中以太网交换机的索引。参数 SwitchPortIdx（in）：以太网交换机驱动程序上下文中的以太网交换机端口索引。参数 WakeupReasonPtr（out）：指向由以太网交换机端口检测到的最近一次唤醒事件结构的指针。返回值 **Std_ReturnType**：**E_OK**：以太网交换机端口唤醒原因请求已被接受；**E_NOT_OK**：以太网交换机端口唤醒原因请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetSwitchPortWakeupReason ( uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_WakeupReasonType* WakeupReasonPtr )
```

函数 **EthIf_GetSwitchPortWakeupReason** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetSwitchPortWakeupReason** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)，否则（如果 **DET** 被禁用）返回 **E_NOT_OK**。

如果启用了开发错误检测：该函数应检查参数 **SwitchIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_SWT_IDX**](#631-开发错误)，否则（如果 **DET** 被禁用）返回 **E_NOT_OK**。

如果启用了开发错误检测：该函数应检查参数 **SwitchPortIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PORT_IDX**](#631-开发错误)，否则（如果 **DET** 被禁用）返回 **E_NOT_OK**。

如果启用了开发错误检测：该函数应检查参数 **WakeupReasonPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.7. EthIf_GetPhysAddr

**说明**: 获取被索引控制器所使用的物理源地址。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 PhysAddrPtr（out）：网络字节序的物理源地址（**MAC** 地址）。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_GetPhysAddr ( uint8 CtrlIdx, uint8* PhysAddrPtr )
```

函数 **EthIf_GetPhysAddr** 应将调用转发给相应的以太网控制器驱动程序。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **PhysAddrPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.8. EthIf_SetPhysAddr

**说明**: 设置被索引控制器所使用的物理源地址。本服务为同步调用，对相同的 **CtrlIdx** 不可重入，对不同的 **CtrlIdx** 可重入。参数 CtrlIdx（in）：以太网驱动程序上下文中以太网控制器的索引。参数 PhysAddrPtr（in）：指向存储网络字节序物理源地址（**MAC** 地址）的内存的指针。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_SetPhysAddr ( uint8 CtrlIdx, const uint8* PhysAddrPtr )
```

函数 **EthIf_SetPhysAddr** 应将调用转发给相应的以太网控制器驱动程序。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **PhysAddrPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.9. EthIf_UpdatePhysAddrFilter

**说明**: 向被索引控制器的过滤器中添加物理源地址或从中移除物理源地址。如果以太网控制器不具备过滤能力，则必须由软件来完成。本服务为同步调用，对相同的 **CtrlIdx** 不可重入，对不同的 **CtrlIdx** 可重入。参数 CtrlIdx（in）：以太网驱动程序上下文中以太网控制器的索引。参数 PhysAddrPtr（in）：指向存储网络字节序物理目的地址（**MAC** 地址）的内存的指针。这是第 2 层以太网数据包的多播目的地址。参数 Action（in）：向以太网控制器的过滤器中添加或移除该地址。返回值 **Std_ReturnType**：**E_OK**：过滤器成功更改；**E_NOT_OK**：无法更改过滤器。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_UpdatePhysAddrFilter ( uint8 CtrlIdx, const uint8* PhysAddrPtr, Eth_FilterActionType Action )
```

函数 **EthIf_SetPhysAddrFilter** 应将调用转发给相应的以太网控制器驱动程序。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **PhysAddrPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.10. EthIf_GetPortMacAddr

**说明**: 获取可以通过其到达该 **MAC** 地址的端口。本服务为同步调用，不可重入。参数 MacAddrPtr（in）：要搜索交换机端口的 **MAC** 地址，通过该端口可以到达具有此 **MAC** 地址的节点。参数 SwitchIdxPtr（out）：指向交换机索引的指针。参数 PortIdxPtr（out）：指向端口索引的指针。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：发生错误，例如找到了多个端口。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetPortMacAddr ( const uint8* MacAddrPtr, uint8* SwitchIdxPtr, uint8* PortIdxPtr )
```

函数 **EthIf_GetPortMacAddr** 应返回可以通过其到达给定 **MAC** 地址的交换机和端口索引。如果可能有多个端口或没有端口，此 **API** 调用将返回 **E_NOT_OK**。将为所有以太网交换机驱动程序调用 **EthSwt_GetPortMacAddr**。

该函数应可通过配置参数 **EthIfGetPortMacAddrApi** 在编译前（**pre compile time**）进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **MacAddrPtr**、**SwitchIdxPtr** 和 **PortIdxPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.11. EthIf_GetArlTable

**说明**: 获取交换机的地址解析表（**address resolution table**）并将该列表复制到用户提供的缓冲区中。该函数会将所有条目或 **numberOfElements** 个条目复制到输出列表中。如果输入的 **numberOfElements** 值为 0，该函数不会复制任何数据，而只返回缓存中有效条目的数量。在这种情况下，**arlTableListPointer** 可以为 **NULL_PTR**。本服务为同步调用，不可重入。参数 switchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 numberOfElements（inout）：输入：可写入地址解析表的最大元素数量；输出：当前可用的元素数量。参数 arlTableListPointer（out）：返回指向内存的指针，其中存放由 **MAC** 地址、**VLAN-ID** 和端口组成的结构体列表构成的交换机地址解析表。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：请求的 **switchIdx** 无效或未激活。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetArlTable ( uint8 switchIdx, uint16* numberOfElements, Eth_MacVlanType* arlTableListPointer )
```

函数 **EthIf_GetArlTable** 应为被索引的交换机返回一个由 **MAC** 地址、**VLAN-ID** 和端口构成的结构体列表。

函数 **EthIf_GetArlTable** 应将调用转发给相应以太网交换机驱动程序的 **EthSwt_GetArlTable** 函数。

该函数应可通过配置参数 **EthIfGetArlTable** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **arlTableListPointer** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.12. EthIf_GetCtrlIdxList

**说明**: 返回所有激活的以太网控制器的数量和索引。本服务为异步调用，不可重入。参数 NumberOfCtrlIdx（inout）：输入：**CtrlIdxListPtr** 中控制器的最大数量，为 0 时仅返回控制器数量而不填充 **CtrlIdxListPtr**；输出：激活控制器的数量。参数 CtrlIdxListPtr（out）：激活控制器索引的列表。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetCtrlIdxList ( uint8* NumberOfCtrlIdx, uint8* CtrlIdxListPtr )
```

可选的 **EthIf_GetCtrlIdxList API** 应只返回处于激活状态的 **NumberOfCtrlIdx**。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：仅当输出参数 **NumberOfCtrlIdx** 大于 0x00 时，该函数才应检查输出参数 **CtrlIdxListPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.13. EthIf_GetVlanId

**说明**: 返回所请求以太网控制器的 **VLAN** 标识符。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 VlanIdPtr（out）：用于存储以太网控制器 **VLAN** 标识符（**VID**）的指针。如果以太网控制器不表示虚拟网络（**VLAN**），则为 0。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetVlanId ( uint8 CtrlIdx, uint16* VlanIdPtr )
```

可选的 **EthIf_GetVlanId API** 应返回所请求 **CtrlIdx** 的 **VlanId**。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **VlanIdPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.14. EthIf_GetAndResetMeasurementData

**说明**: 允许出于诊断目的读取和重置详细的测量数据。不支持一次获取所有 **MeasurementIdx**。**ETHIF_MEAS_ALL** 只应用于一次重置所有 **MeasurementIdx**；在这种情况下应为 **MeasurementDataPtr** 提供 **NULL_PTR**。本服务为同步调用，可重入。参数 MeasurementIdx（in）：测量数据的数据索引。参数 MeasurementResetNeeded（in）：触发测量数据重置的标志。参数 MeasurementDataPtr（out）：用于复制测量数据的数据缓冲区引用。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetAndResetMeasurementData ( EthIf_MeasurementIdxType MeasurementIdx, boolean MeasurementResetNeeded, uint32* MeasurementDataPtr )
```

**EthIf_GetAndResetMeasurementData** 应返回所选测量索引的测量数据。

对于测量索引 **ETHIF_MEAS_DROP_CRTLIDX**，该函数应返回由无效的控制器索引/**VLAN** 导致的所有被丢弃数据报的数量。如果 **VLAN** 未启用，则所有接收到的带 **VLAN** 标签的数据报都是无效的，也应被计数。

如果所请求的测量索引不受支持，该函数应返回 **E_NOT_OK**。

如果 **MeasurementResetNeeded** 为 **true** 且测量索引被设置为 **ETHIF_MEAS_ALL**，则该函数应将所有现有的测量数据重置为 0。

所有对数据进行计数的测量数据都不应溢出（**overrun**）。

该函数应接受 **NULL_PTR**。在这种情况下不应复制测量数据。

该函数应可通过配置参数 **EthIfGetAndResetMeasurementDataApi** 在编译前进行开/关配置。

如果 **VLAN** 未激活，以太网接口应递增相应的测量数据并过滤该报文。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 **ETHIF_E_NOTINIT**。

#### 7.3.15. EthIf_StoreConfiguration

**说明**: 以持久的方式触发存储/重置交换机所学习的 **MAC**/端口表的配置，例如将由 **CDD** 使用。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。返回值 **Std_ReturnType**：**E_OK**：存储/重置请求已被接受；**E_NOT_OK**：存储/重置请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_StoreConfiguration ( uint8 SwitchIdx )
```

函数 **EthIf_StoreConfiguration** 应触发存储以太网交换机所学习的 **MAC**/端口表。

该函数应可通过配置参数 **EthIfStoreConfigurationApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

#### 7.3.16. EthIf_ResetConfiguration

**说明**: 该函数应以持久的方式请求重置以太网交换机所学习的 **MAC**/端口表的配置。例如可供 **CDD** 使用。静态配置的条目仍应保留。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。返回值 **Std_ReturnType**：**E_OK**：持久重置 **MAC**/端口表的请求已被接受；**E_NOT_OK**：持久重置 **MAC**/端口表的请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_ResetConfiguration ( uint8 SwitchIdx )
```

函数 **EthIf_ResetConfiguration** 应触发重置以太网交换机所学习的 **MAC**/端口表。

该函数应可通过配置参数 **EthIfResetConfigurationApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

#### 7.3.17. EthIf_GetCurrentTime

**说明**: 根据 **HW** 的能力，从 **HW** 寄存器返回一个时间值。如果 **HW** 的分辨率低于 **Eth_TimeStampType** 的分辨率或范围，剩余的位将用 0 填充。重要提示：**EthIf_GetCurrentTime** 可能会在一个独占区（**exclusive area**）内被调用。本服务为同步调用，不可重入。参数 CtrlIdx（in）：所寻址 **ETH** 控制器的索引。参数 timeQualPtr（out）：**HW** 时间戳的质量，例如基于当前的漂移。参数 timeStampPtr（out）：当前时间戳。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetCurrentTime ( uint8 CtrlIdx, Eth_TimeStampQualType* timeQualPtr, Eth_TimeStampType* timeStampPtr )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **timeQualPtr** 和 **timeStampPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

该函数应可通过配置参数 **EthIfGlobalTimeSupport** 在编译前进行开/关配置。

**EthIf** 模块应采用适当的机制，以允许从其主函数之外的其他分区调用 **EthIf_GetCurrentTime API**，例如通过提供一个 **EthIf** 卫星（**satellite**）。

#### 7.3.18. EthIf_GetCurrentTimeTuple

**说明**: 在一个原子操作中读取时间戳时钟的当前时间和 **PHC** 的当前时间。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中拥有该时钟单元的以太网控制器的索引。参数 ClkUnitIdx（in）：以太网接口上下文中用于提供时间元组（**time tuple**）的时钟单元的索引。参数 currentTimeTuplePtr（out）：当前时间元组，包含用于时间戳的自由运行时钟的值和可调节 **PHC** 的值。返回值 **Std_ReturnType**：**E_OK**：成功获取当前时间；**E_NOT_OK**：无法获取当前时间。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetCurrentTimeTuple ( uint8 CtrlIdx, uint8 ClkUnitIdx, TimeTupleType* currentTimeTuplePtr )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ClkUnitIdx** 是否有效。如果检查失败，该函数应引发开发错误 **ETHIF_E_INV_CLKUNIT_IDX**。

如果启用了开发错误检测：该函数应检查参数 **currentTimeTuplePtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

函数 **EthIf_GetCurrentTimeTuple** 应将调用转发给函数 **&lt;EthDrv&gt;_GetCurrentTimeTuple**，其中 **CtrlIdx** 设置为相应 [**EthIfPhysController**](#926-ethifphyscontroller) 通过 **EthIfEthCtrlRef** 引用的以太网控制器，**ClkUnitIdx** 设置为给定 **ClkUnitIdx** 通过 **EthIfClkUnitRef** 引用的以太网控制器时钟单元。

该函数应可通过配置参数 **EthIfGlobalTimeSupport** 在编译前进行开/关配置。

**EthIf** 模块应采用适当的机制，以允许从其主函数之外的其他分区调用 **EthIf_GetCurrentTimeTuple API**，例如通过提供一个 **EthIf** 卫星。

#### 7.3.19. EthIf_SetPhcTime

**说明**: 设置 **PHC** 的绝对时间。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中拥有该时钟单元的以太网控制器的索引。参数 ClkUnitIdx（in）：以太网接口上下文中用于提供时间元组的时钟单元的索引。参数 timeStampPtr（in）：**PHC** 应被设置到的时间值。返回值 **Std_ReturnType**：**E_OK**：**PHC** 设置成功；**E_NOT_OK**：无法设置 **PHC**。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPhcTime ( uint8 CtrlIdx, uint8 ClkUnitIdx, const TimeStampType* timeStampPtr )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ClkUnitIdx** 是否有效。如果检查失败，该函数应引发开发错误 **ETHIF_E_INV_CLKUNIT_IDX**。

该函数应可通过配置参数 **EthIfPhcSupport** 在编译前进行开/关配置。

函数 **EthIf_SetPhcTime** 应将调用转发给函数 **&lt;EthDrv&gt;_SetPhcTime**，其中 **CtrlIdx** 设置为相应 [**EthIfPhysController**](#926-ethifphyscontroller) 通过 **EthIfEthCtrlRef** 引用的以太网控制器，**ClkUnitIdx** 设置为给定 **ClkUnitIdx** 通过 **EthIfClkUnitRef** 引用的以太网控制器时钟单元。

**EthIf** 模块应采用适当的机制，以允许从其主函数之外的其他分区调用 **EthIf_SetPhcTime API**，例如通过提供一个 **EthIf** 卫星。

#### 7.3.20. EthIf_SetPhcCorrection

**说明**: 设置 **PHC** 参数以调整 **PHC** 的速率和偏移。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中拥有该时钟单元的以太网控制器的索引。参数 ClkUnitIdx（in）：以太网接口上下文中用于提供时间元组的时钟单元的索引。参数 rateDeviation（in）：请求 **PHC** 被校正的速率偏差（分辨率：2⁻⁴¹）。参数 offset（in）：请求 **PHC** 被更新的时间偏移。返回值 **Std_ReturnType**：**E_OK**：**PHC** 设置成功；**E_NOT_OK**：无法设置 **PHC**。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPhcCorrection ( uint8 CtrlIdx, uint8 ClkUnitIdx, sint32 rateDeviation, sint32 offset )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ClkUnitIdx** 是否有效。如果检查失败，该函数应引发开发错误 **ETHIF_E_INV_CLKUNIT_IDX**。

该函数应可通过配置参数 **EthIfPhcSupport** 在编译前进行开/关配置。

函数 **EthIf_SetPhcCorrection** 应将调用转发给函数 **&lt;EthDrv&gt;_SetPhcTime**，其中 **CtrlIdx** 设置为相应 [**EthIfPhysController**](#926-ethifphyscontroller) 通过 **EthIfEthCtrlRef** 引用的以太网控制器，**ClkUnitIdx** 设置为给定 **ClkUnitIdx** 通过 **EthIfClkUnitRef** 引用的以太网控制器时钟单元。

**EthIf** 模块应采用适当的机制，以允许从其主函数之外的其他分区调用 **[EthIf_SetPhcTime](#7319-ethif_setphctime) API**，例如通过提供一个 **EthIf** 卫星。

#### 7.3.21. EthIf_GetPhcTime

**说明**: 从 **PHC** 的 **HW** 寄存器中返回当前时间值。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中拥有该时钟单元的以太网控制器的索引。参数 ClkUnitIdx（in）：以太网接口上下文中用于提供时间元组的时钟单元的索引。参数 timeQualPtr（in）：**HW** 时间戳的质量，例如基于当前的漂移。参数 timeStampPtr（in）：当前时间戳。返回值 **Std_ReturnType**：**E_OK**：成功获取 **PHC** 值；**E_NOT_OK**：无法获取 **PHC** 值。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetPhcTime ( uint8 CtrlIdx, uint8 ClkUnitIdx, TimeStampQualType timeQualPtr, TimeStampType timeStampPtr )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ClkUnitIdx** 是否有效。如果检查失败，该函数应引发开发错误 **ETHIF_E_INV_CLKUNIT_IDX**。

如果启用了开发错误检测：该函数应检查参数 **timeQualPtr** 和 **timeStampPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **timeStampPtr** 和 **timeStampPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

该函数应可通过配置参数 **EthIfPhcSupport** 在编译前进行开/关配置。

函数 **EthIf_GetPhcTime** 应将调用转发给函数 **&lt;EthDrv&gt;_GetPhcTime**，其中 **CtrlIdx** 设置为相应 [**EthIfPhysController**](#926-ethifphyscontroller) 通过 **EthIfEthCtrlRef** 引用的以太网控制器，**ClkUnitIdx** 设置为给定 **ClkUnitIdx** 通过 **EthIfClkUnitRef** 引用的以太网控制器时钟单元。

**EthIf** 模块应采用适当的机制，以允许从其主函数之外的其他分区调用 **EthIf_GetPhcTime API**，例如通过提供一个 **EthIf** 卫星。

#### 7.3.22. EthIf_SetPpsSignalMode

**说明**: 启用/禁用 **PPS** 信号的生成。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中拥有该时钟单元的以太网控制器的索引。参数 ClkUnitIdx（in）：以太网接口上下文中用于提供时间元组的时钟单元的索引。参数 signalMode（in）：**TRUE**：**PPS** 信号生成已启用；**FALSE**：**PPS** 信号生成已禁用。返回值 **Std_ReturnType**：**E_OK**：**PPS** 信号生成成功启用/禁用；**E_NOT_OK**：启用/禁用 **PPS** 信号生成失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPpsSignalMode ( uint8 CtrlIdx, uint8 ClkUnitIdx, boolean signalMode )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

该函数应可通过配置参数 **EthIfPhcSupport** 在编译前进行开/关配置。

函数 **EthIf_SetPpsSignalMode** 应将调用转发给函数 **&lt;EthDrv&gt;_SetPpsSignalMode**，其中 **CtrlIdx** 设置为相应 [**EthIfPhysController**](#926-ethifphyscontroller) 通过 **EthIfEthCtrlRef** 引用的以太网控制器，**ClkUnitIdx** 设置为给定 **ClkUnitIdx** 通过 **EthIfClkUnitRef** 引用的以太网控制器时钟单元。

#### 7.3.23. EthIf_EnableEgressTimeStamp

**说明**: 在专用的报文对象上激活发送方向时间戳（**egress time stamping**）。一些 **HW** 只存储一次发送方向时间戳标记，而另一些 **HW** 在每次发送之前都需要它。由于报文类型在网络设计上始终是「带时间戳的」，因此不存在「禁用」功能。本服务为同步调用，不可重入。参数 CtrlIdx（in）：所寻址 **ETH** 控制器的索引。参数 BufIdx（in）：应用程序期望发送方向时间戳的报文缓冲区的索引。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_EnableEgressTimeStamp ( uint8 CtrlIdx, Eth_BufIdxType BufIdx )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

该函数应可通过配置参数 **EthIfGlobalTimeSupport** 在编译前进行开/关配置。

#### 7.3.24. EthIf_GetEgressTimeStamp

**说明**: 在专用的报文对象上读回发送方向时间戳。必须在 **TxConfirmation()** 函数内调用。本服务为同步调用，不可重入。参数 CtrlIdx（in）：所寻址 **ETH** 控制器的索引。参数 BufIdx（in）：上层期望发送方向时间戳的报文缓冲区的索引。参数 timeQualPtr（out）：**HW** 时间戳的质量，例如基于当前的漂移。参数 timeStampPtr（out）：当前时间戳。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：读取时间戳失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetEgressTimeStamp ( uint8 CtrlIdx, Eth_BufIdxType BufIdx, Eth_TimeStampQualType* timeQualPtr, Eth_TimeStampType* timeStampPtr )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **timeQualPtr** 和 **timeStampPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

该函数应可通过配置参数 **EthIfGlobalTimeSupport** 在编译前进行开/关配置。

#### 7.3.25. EthIf_GetIngressTimeStamp

**说明**: 在专用的报文对象上读回接收方向时间戳（**ingress time stamp**）。必须在 **RxIndication()** 函数内调用。本服务为同步调用，不可重入。参数 CtrlIdx（in）：所寻址 **ETH** 控制器的索引。参数 DataPtr（in）：应用程序期望接收方向时间戳的报文缓冲区的指针。参数 timeQualPtr（out）：**HW** 时间戳的质量，例如基于当前的漂移。参数 timeStampPtr（out）：当前时间戳。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：读取时间戳失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetIngressTimeStamp ( uint8 CtrlIdx, const Eth_DataType* DataPtr, Eth_TimeStampQualType* timeQualPtr, Eth_TimeStampType* timeStampPtr )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **DataPtr**、**timeQualPtr** 和 **timeStampPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

该函数应可通过配置参数 **EthIfGlobalTimeSupport** 在编译前进行开/关配置。

#### 7.3.26. EthIf_SwitchPortGroupRequestMode

**说明**: 为 **EthIfSwtPortGroup** 请求一个模式。应通过为端口组引用的所有 **EthSwtPort** 调用 **EthSwt_SetSwitchPortMode** 将该调用转发给 **EthSwt**。本服务为异步调用，不可重入。参数 PortGroupIdx（in）：以太网接口上下文中端口组的索引。参数 PortMode（in）：**ETH_MODE_DOWN**：禁用以太网交换机端口组；**ETH_MODE_ACTIVE**：启用以太网交换机端口组；**ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**：启用端口组并请求网络上的唤醒。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法更改端口组模式。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGroupRequestMode ( EthIf_SwitchPortGroupIdxType PortGroupIdx, Eth_ModeType PortMode )
```

注意：实现必须确保只有当之前所有的激活请求都已被撤回时，[**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 内的 **EthSwtPort** 才会被禁用。例如，这可以通过计数器机制来实现。

理由：通过 **EthIfSwitchOffPortTimedelay** 延迟关闭 **EthSwtPort** 是必要的，以确保以太网交换机端口与所连接通信伙伴的以太网硬件（**PHY** 或另一个以太网交换机）同时关闭：

1. 如果所连接通信伙伴的以太网硬件是 **PHY**，则 **EthIfSwitchOffPortTimedelay** 覆盖了由于 **NM** 处理而需要直到所连接通信伙伴的 **PHY** 被关闭的时间。
2. 如果所连接通信伙伴的以太网硬件是以太网交换机，则两个 **EthSwtPort** 应在同一时间点被关闭，以避免链路断开（**link down**）被识别。

如果以 **ETH_MODE_DOWN** 调用了 **EthIf_SwitchPortGroupRequestMode**，且对于引用该端口的所有 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 都已请求了 **ETH_MODE_DOWN** 模式、而当前模式为 **ETH_MODE_ACTIVE**，则 **EthIf** 应为相应 **EthIf_SwitchPortGroup** 的所有端口启动一个时长为 **EthIfSwitchOffPortTimedelay** 的定时器。

如果某个端口的关闭端口定时器（参见上一条需求）到期，**EthIf** 应按给定顺序为相应的 **EthSwtPort** 调用以下函数：

1. 以 **ETHTRCV_LINK_STATE_DOWN** 调用 **EthSwt_PortLinkStateRequest**
2. 以 **ETH_MODE_DOWN** 调用 **EthSwt_SetSwitchPortMode**

理由：避免本应由 [**EthIfController**](#924-ethifcontroller) 控制的 [**EthIfSwitchPortGroup**](#9211-ethifswitchportgroup) 被 **BswM** 意外调用。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查所提供的参数 **PortGroupIdx** 是否寻址了一个未被任何 [**EthIfController**](#924-ethifcontroller) 引用的端口组。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PORT_GROUP_IDX**](#631-开发错误)。

#### 7.3.27. EthIf_StartAllPorts

**说明**: 请求将所有已配置且受影响的 **EthSwtPort** 置为 **ETH_MODE_ACTIVE**。本服务为异步调用，可重入。该服务无参数。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求被拒绝。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_StartAllPorts ( void )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

#### 7.3.28. EthIf_SetSwitchMgmtInfo

**说明**: 随以太网帧一起提供额外的管理信息，该帧在交换机内需要特殊处理。必须在相关帧的 **[EthIf_ProvideTxBuffer](#7350-ethif_providetxbuffer)()** 和 **[EthIf_Transmit](#7351-ethif_transmit)()** 之间调用。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口控制器的索引。参数 BufIdx（in）：以太网发送缓冲区索引。参数 MgmtInfoPtr（in）：指向管理信息的指针。返回值 **Std_ReturnType**：**E_OK**：管理信息设置成功；**E_NOT_OK**：管理信息设置失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetSwitchMgmtInfo ( uint8 CtrlIdx, Eth_BufIdxType BufIdx, EthSwt_MgmtInfoType* MgmtInfoPtr )
```

该函数应可通过配置参数 **EthIfSwitchManagementSupport** 在编译前进行开/关（**ON/OFF**）配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 **[EthIf_Init](#731-ethif_init)()**。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **MgmtInfoPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.29. EthIf_GetRxMgmtObject

**说明**: 请求（在此上下文中）唯一的 **DataPtr** 的管理对象（**MgmtObject**）。本服务为同步调用，可重入。参数 CtrlIdx（in）：以太网接口控制器的索引。参数 DataPtr（in）：以太网数据指针。参数 MgmtObjectPtr（out）：指向管理对象的指针。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法获取管理对象。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetRxMgmtObject ( uint8 CtrlIdx, Eth_DataType* DataPtr, EthSwt_MgmtObjectType** MgmtObjectPtr )
```

#### 7.3.30. EthIf_GetTxMgmtObject

**说明**: 请求（在此上下文中）唯一的 **BufIdx** 的管理对象。本服务为同步调用，可重入。参数 CtrlIdx（in）：以太网接口控制器的索引。参数 BufIdx（in）：以太网接收缓冲区索引。参数 MgmtObjectPtr（out）：指向管理对象的指针。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法获取管理对象。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetTxMgmtObject ( uint8 CtrlIdx, Eth_BufIdxType BufIdx, EthSwt_MgmtObjectType** MgmtObjectPtr )
```

#### 7.3.31. EthIf_SwitchEnableTimeStamping

**说明**: 在由 **CtrlIdx** 和 **BufIdx** 寻址的专用报文对象上激活发送方向时间戳。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 BufIdx（in）：应用程序期望发送方向时间戳的报文缓冲区的索引。参数 MgmtInfo（out）：管理信息。返回值 **Std_ReturnType**：**E_OK**：发送方向时间戳成功启用；**E_NOT_OK**：启用发送方向时间戳失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchEnableTimeStamping ( uint8 CtrlIdx, Eth_BufIdxType BufIdx, EthSwt_MgmtInfoType* MgmtInfo )
```

如果调用了 **EthIf_SwitchEnableTimeStamping**，则 **EthIf** 应为组中的每个端口调用 **EthSwt_PortEnableTimeStamp**。

该函数应可通过配置参数 **EthIfGlobalTimeSupport** 在编译前进行开/关（**ON/OFF**）配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 **Eth_Init**。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

#### 7.3.32. EthIf_VerifyConfig

**说明**: 转发给 **EthSwt_VerifyConfig**。**EthSwt_VerifyConfig** 根据 **HW** 架构、**HW** 能力和该验证的预期精度来验证交换机配置。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网接口上下文中交换机的索引。参数 Result（out）：验证结果，**TRUE**：配置验证通过；**FALSE**：发现配置值损坏。返回值 **Std_ReturnType**：**E_OK**：配置验证成功；**E_NOT_OK**：配置验证未成功。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_VerifyConfig ( uint8 SwitchIdx, boolean* Result )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

该函数应可通过配置参数 **EthIfVerifyConfigApi** 在编译期（**compile time**）进行开/关配置。

#### 7.3.33. EthIf_SetForwardingMode

**说明**: 验证交换机配置。如果配置无效，则重新配置交换机。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 mode（in）：**True**：转发已启用；**False**：转发已禁用。返回值 **Std_ReturnType**：**E_OK**：停止帧转发成功；**E_NOT_OK**：停止帧转发未成功。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetForwardingMode ( uint8 SwitchIdx, boolean mode )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

该函数应可通过配置参数 **EthIfSetForwardingModeApi** 在编译期进行开/关配置。

#### 7.3.34. EthIf_GetTrcvSignalQuality

**说明**: 获取给定以太网收发器链路的信号质量。本服务为同步调用，对不同的 **TrcvIdx** 可重入，对相同的 **TrcvIdx** 不可重入。参数 TrcvIdx（in）：以太网接口上下文中收发器的索引。参数 ResultPtr（out）：指向应以百分比存储信号质量的内存的指针。返回值 **Std_ReturnType**：**E_OK**：成功获取信号质量；**E_NOT_OK**：未能成功获取信号质量。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetTrcvSignalQuality ( uint8 TrcvIdx, EthIf_SignalQualityResultType* ResultPtr )
```

函数 **EthIf_GetTrcvSignalQuality** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_GetPhySignalQuality** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ResultPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.35. EthIf_GetSwitchPortSignalQuality

**说明**: 获取给定以太网交换机端口链路的信号质量。本服务为同步调用，对不同的以太网交换机索引和以太网交换机端口索引可重入，对相同的 **SwitchPortIdx** 不可重入。参数 SwitchIdx（in）：以太网接口上下文中以太网交换机的索引。参数 SwitchPortIdx（in）：以太网接口上下文中以太网交换机端口的索引。参数 ResultPtr（out）：指向应以百分比存储信号质量的内存的指针。返回值 **Std_ReturnType**：**E_OK**：成功获取信号质量；**E_NOT_OK**：未能成功获取信号质量。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetSwitchPortSignalQuality ( uint8 SwitchIdx, uint8 SwitchPortIdx, EthIf_SignalQualityResultType* ResultPtr )
```

函数 **EthIf_GetSwitchPortSignalQuality** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetPortSignalQuality** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **SwitchIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_SWT_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **SwitchPortIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PORT_IDX**](#631-开发错误)，否则（如果 **DET** 被禁用）返回 **E_NOT_OK**。

如果启用了开发错误检测：该函数应检查参数 **ResultPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.36. EthIf_ClearTrcvSignalQuality

**说明**: 清除给定以太网收发器链路的已存储信号质量。本服务为同步调用，对不同的 **TrcvIdx** 可重入，对相同的 **TrcvIdx** 不可重入。参数 TrcvIdx（in）：以太网接口上下文中收发器的索引。返回值 **Std_ReturnType**：**E_OK**：信号质量清除成功；**E_NOT_OK**：信号质量清除未成功。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_ClearTrcvSignalQuality ( uint8 TrcvIdx )
```

函数 **EthIf_ClearTrcvSignalQuality** 应清除由 **TrcvIdx** 给出的 [**EthIfTransceiver**](#9212-ethiftransceiver) 的已存储信号质量值（参见 [**EthIf_SignalQualityResultType**](#724-ethif_signalqualityresulttype)）。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

#### 7.3.37. EthIf_ClearSwitchPortSignalQuality

**说明**: 清除给定以太网交换机端口链路的已存储信号质量。本服务为同步调用，对不同的以太网交换机索引和以太网交换机端口索引可重入，对相同的 **SwitchPortIdx** 不可重入。参数 SwitchIdx（in）：以太网接口上下文中以太网交换机的索引。参数 SwitchPortIdx（in）：以太网接口上下文中以太网交换机端口的索引。返回值 **Std_ReturnType**：**E_OK**：信号质量清除成功；**E_NOT_OK**：信号质量清除未成功。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_ClearSwitchPortSignalQuality ( uint8 SwitchIdx, uint8 SwitchPortIdx )
```

函数 **EthIf_ClearSwitchPortSignalQuality** 应清除由 **SwitchIdx** 和 **SwitchPortIdx** 给出的 **EthSwtPort** 的已存储信号质量值（参见 [**EthIf_SignalQualityResultType**](#724-ethif_signalqualityresulttype)）。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **SwitchIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_SWT_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **SwitchPortIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PORT_IDX**](#631-开发错误)，否则（如果 **DET** 被禁用）返回 **E_NOT_OK**。

#### 7.3.38. EthIf_SetPhyTestMode

**说明**: 激活给定的测试模式。本服务为同步调用，对不同的 **TrcvIdx** 可重入，对相同的 **TrcvIdx** 不可重入。参数 TrcvIdx（in）：以太网接口上下文中收发器的索引。参数 Mode（in）：要激活的测试模式。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPhyTestMode ( uint8 TrcvIdx, EthTrcv_PhyTestModeType Mode )
```

函数 **EthIf_SetPhyTestMode** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_SetPhyTestMode** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

#### 7.3.39. EthIf_SetPhyLoopbackMode

**说明**: 激活给定的环回模式（**loopback mode**）。本服务为同步调用，对不同的 **TrcvIdx** 可重入，对相同的 **TrcvIdx** 不可重入。参数 TrcvIdx（in）：以太网接口上下文中收发器的索引。参数 Mode（in）：要激活的环回模式。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPhyLoopbackMode ( uint8 TrcvIdx, EthTrcv_PhyLoopbackModeType Mode )
```

函数 **EthIf_SetPhyLoopbackMode** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_SetPhyLoopbackMode** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

#### 7.3.40. EthIf_SetPhyTxMode

**说明**: 激活给定的发送模式。本服务为同步调用，对不同的 **TrcvIdx** 可重入，对相同的 **TrcvIdx** 不可重入。参数 TrcvIdx（in）：以太网接口上下文中收发器的索引。参数 Mode（in）：要激活的发送模式。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPhyTxMode ( uint8 TrcvIdx, EthTrcv_PhyTxModeType Mode )
```

函数 **EthIf_SetPhyTxMode** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_SetPhyTxMode** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

#### 7.3.41. EthIf_GetCableDiagnosticsResult

**说明**: 获取给定收发器的电缆诊断结果。本服务为同步调用，对不同的 **TrcvIdx** 可重入，对相同的 **TrcvIdx** 不可重入。参数 TrcvIdx（in）：以太网接口上下文中收发器的索引。参数 ResultPtr（out）：指向应存储电缆诊断结果的位置的指针。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetCableDiagnosticsResult ( uint8 TrcvIdx, EthTrcv_CableDiagResultType* ResultPtr )
```

函数 **EthIf_GetCableDiagnosticsResult** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_GetCableDiagnosticsResult** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ResultPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.42. EthIf_GetPhyIdentifier

**说明**: 按照 IEEE 802.3-2015 第 22.2.4.3.1 节 PHY 标识符（**PHY Identifier**）的规定获取以太网接口的 **PHY** 标识符。本服务为同步调用，对不同的 **TrcvIdx** 可重入，对相同的 **TrcvIdx** 不可重入。参数 TrcvIdx（in）：以太网接口上下文中收发器的索引。参数 OrgUniqueIdPtr（out）：指向应存储组织唯一标识符（**Organizationally Unique Identifier**）的内存的指针。参数 ModelNrPtr（out）：指向应存储制造商型号编号（**Manufacturer's Model Number**）的内存的指针。参数 RevisionNrPtr（out）：指向应存储版本编号（**Revision Number**）的内存的指针。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetPhyIdentifier ( uint8 TrcvIdx, uint32* OrgUniqueIdPtr, uint8* ModelNrPtr, uint8* RevisionNrPtr )
```

函数 **EthIf_GetPhyIdentifier** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_GetPhyIdentifier** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **OrgUniqueIdPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ModelNrPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **RevisionNrPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.43. EthIf_GetBufWRxParams

**说明**: 读出与所接收数据包的收发器接收方向相关的值。例如，这可以是属于单个数据包的 **RSSI** 或信道（**Channel**）。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 RxParamIds（in）：要读取的参数的 **ID**。参数 NumParams（in）：参数的数量。参数 ParamValues（out）：所请求参数的值。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：读取参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetBufWRxParams ( uint8 CtrlIdx, const WEth_BufWRxParamIdType* RxParamIds, uint32* ParamValues, uint8 NumParams )
```

函数 **EthIf_GetBufWRxParams** 应将调用转发给相应无线以太网控制器驱动程序的 **WEth_GetBufWRxParams** 函数。

该函数应可通过配置参数 **EthIfEnableWEthApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **RxParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

注意：该函数要求事先已进行接收（[**EthIf_RxIndication**](#741-ethif_rxindication)）。

#### 7.3.44. EthIf_GetBufWTxParams

**说明**: 读出与所发送数据包的收发器发送方向相关的值。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 TxParamIds（in）：所请求参数的 **ID**。参数 NumParams（in）：所请求参数的数量。参数 ParamValues（out）：所请求参数的值。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：读取参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetBufWTxParams ( uint8 CtrlIdx, const WEth_BufWTxParamIdType* TxParamIds, uint32* ParamValues, uint8 NumParams )
```

函数 **EthIf_GetBufWTxParams** 应将调用转发给相应无线以太网控制器驱动程序的 **WEth_GetBufWTxParams** 函数。

该函数应可通过配置参数 **EthIfEnableWEthApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TxParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

注意：该函数要求事先已进行发送（[**EthIf_Transmit**](#7351-ethif_transmit)）。

#### 7.3.45. EthIf_SetBufWTxParams

**说明**: 为特定缓冲区（要发送的数据包）设置与收发器发送方向相关的值。例如，这可以是期望的发送功率或属于单个数据包的信道。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 BufIdx（in）：缓冲区资源的索引。参数 TxParamIds（in）：提供给发送射频的参数的 **ID**。参数 ParamValues（in）：提供给发送射频的参数的值。参数 NumParams（in）：提供给发送射频的参数的数量。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：设置参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetBufWTxParams ( uint8 CtrlIdx, Eth_BufIdxType BufIdx, const WEth_BufWTxParamIdType* TxParamIds, const uint32* ParamValues, uint8 NumParams )
```

函数 **EthIf_SetBufWTxParams** 应将调用转发给相应无线以太网控制器驱动程序的 **WEth_SetBufWTxParams** 函数。

该函数应可通过配置参数 **EthIfEnableWEthApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TxParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

注意：该函数要求事先已进行缓冲区请求（[**EthIf_ProvideTxBuffer**](#7350-ethif_providetxbuffer)）。

#### 7.3.46. EthIf_SetRadioParams

**说明**: 设置与收发器的无线射频相关的值。例如，这可以是射频设置（信道等）的选择。本服务为同步调用，不可重入。参数 TrcvId（in）：收发器的索引。参数 ParamIds（in）：要设置的参数的 **ID**。参数 ParamValue（in）：要设置的参数的值。参数 NumParams（in）：要设置的参数的数量。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：写入参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetRadioParams ( uint8 TrcvId, const WEthTrcv_SetRadioParamIdType* ParamIds, const uint32* ParamValue, uint8 NumParams )
```

函数 **EthIf_SetRadioParams** 应将调用转发给相应无线以太网收发器驱动程序的 **WEthTrcv_SetRadioParams** 函数。

该函数应可通过配置参数 **EthIfEnableWEthApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvId** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValue** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.47. EthIf_SetChanRxParams

**说明**: 设置与收发器无线信道接收方向相关的值。例如，这可以是诸如频率之类的信道参数。本服务为同步调用，不可重入。参数 TrcvId（in）：收发器的索引。参数 RadioId（in）：收发器射频（包括信道）的索引。参数 ParamIds（in）：要设置的参数的 **ID**。参数 ParamValues（in）：要设置的参数的值。参数 NumParams（in）：要设置的参数的数量。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：写入参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetChanRxParams ( uint8 TrcvId, uint8 RadioId, const WEthTrcv_SetChanRxParamIdType* ParamIds, const uint32* ParamValues, uint8 NumParams )
```

函数 **EthIf_SetChanRxParams** 应将调用转发给相应无线以太网收发器驱动程序的 **WEthTrcv_SetChanRxParams** 函数。

函数 **EthIf_SetChanRxParams** 应可通过配置参数 **EthIfEnableWEthApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvId** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **RadioId** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.48. EthIf_SetChanTxParams

**说明**: 设置与收发器无线信道发送方向相关的值。例如，这可以是信道的比特率。本服务为同步调用，不可重入。参数 TrcvId（in）：收发器的索引。参数 RadioId（in）：收发器射频（包括信道）的索引。参数 TxParamIds（in）：要设置的参数的 **ID**。参数 ParamValues（in）：要设置的参数的值。参数 NumParams（in）：要设置的参数的数量。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：写入参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetChanTxParams ( uint8 TrcvId, uint8 RadioId, const WEthTrcv_SetChanTxParamIdType* TxParamIds, const uint32* ParamValues, uint8 NumParams )
```

函数 **EthIf_SetChanTxParams** 应将调用转发给相应无线以太网收发器驱动程序的 **WEthTrcv_SetChanTxParams** 函数。

该函数应可通过配置参数 **EthIfEnableWEthApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvId** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **RadioId** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TxParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.49. EthIf_GetChanRxParams

**说明**: 读取与收发器接收方向相关的值。例如，这可以是信道繁忙比率（**CBR**）或平均信道空闲时间（**CIT**）。本服务为同步调用，不可重入。参数 TrcvId（in）：收发器的索引。参数 RadioId（in）：收发器射频（包括信道）的索引。参数 ParamIds（in）：要读取的参数的 **ID**。参数 NumParams（in）：要读取的参数的数量。参数 ParamValues（out）：所请求参数的值。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：读取参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetChanRxParams ( uint8 TrcvId, uint8 RadioId, const WEthTrcv_GetChanRxParamIdType* ParamIds, uint32* ParamValues, uint8 NumParams )
```

函数 **EthIf_GetChanRxParams** 应将调用转发给相应无线以太网收发器驱动程序的 **WEthTrcv_GetChanRxParams** 函数。

该函数应可通过配置参数 **EthIfEnableWEthApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvId** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_TRCV_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **RadioId** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.50. EthIf_ProvideTxBuffer

**说明**: 提供对指定以太网控制器的发送缓冲区的访问。本服务为同步调用，可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 FrameType（in）：以太网帧类型（**EtherType**）。参数 Priority（in）：应用于 **VLAN** 标签 3 位 **PCP** 字段的优先级值。参数 LenBytePtr（inout）：输入：期望的长度（字节）；输出：被授予的长度（字节）。参数 BufIdxPtr（out）：被授予缓冲区资源的索引。用于后续请求。参数 BufPtr（out）：指向被授予缓冲区的指针。返回值 **BufReq_ReturnType**：**BUFREQ_OK**：成功；**BUFREQ_E_NOT_OK**：检测到开发错误；**BUFREQ_E_BUSY**：所有缓冲区都在使用中；**BUFREQ_E_OVFL**：请求的缓冲区过大。可通过**EthIf.h**获得。

```C
BufReq_ReturnType EthIf_ProvideTxBuffer ( uint8 CtrlIdx, Eth_FrameType FrameType, uint8 Priority, Eth_BufIdxType* BufIdxPtr, uint8** BufPtr, uint16* LenBytePtr )
```

如果 **CtrlIdx** 指向一个未配置 **EthIfVlanID** 的 **EthIfCtrl**，则参数 **FrameType** 和 **Priority** 不被使用。

如果使用了 **VLAN**：

* **EthIf** 应在调用以太网驱动程序模块之前将输入的期望长度增加 4 字节
* **EthIf** 应将 **PCP**（**Priority** 参数）、**CFI**（始终为 0）、**VID**（所配置的 **VLAN ID**）和 **FrameType** 参数的值存储在从 **&lt;EthDrv&gt;_ProvideTxBuffer** 接收到的缓冲区的开头
* **EthIf** 在返回被授予的缓冲区时应将 **BufPtr** 增加 4 字节
* **EthIf** 应将输出的被授予长度减少 4 字节

如果给定 [**EthIfController**](#924-ethifcontroller) 最近一次被接受的控制器模式为 **ETH_MODE_ACTIVE** 或 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**，则函数 **EthIf_ProvideTxBuffer** 应将调用转发给相应的以太网控制器驱动程序或 **CanXL** 控制器驱动程序。否则该函数应拒绝发送缓冲区请求并以 **E_NOT_OK** 返回。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdxPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **LenBytePtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.51. EthIf_Transmit

**说明**: 触发对之前已填充的发送缓冲区的发送。本服务为同步调用，对不同的缓冲区索引和控制器索引可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 BufIdx（in）：缓冲区资源的索引。参数 FrameType（in）：以太网帧类型。参数 TxConfirmation（in）：激活发送确认。参数 LenByte（in）：数据长度（字节）。参数 PhysAddrPtr（in）：网络字节序的物理目的地址（**MAC** 地址）。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：发送失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_Transmit ( uint8 CtrlIdx, Eth_BufIdxType BufIdx, Eth_FrameType FrameType, boolean TxConfirmation, uint16 LenByte, const uint8* PhysAddrPtr )
```

如果 **CtrlIdx** 指向一个配置了 **EthIfVlanID** 的 **EthIfCtrl**，则不使用参数 **FrameType**，而是将 0x8100 提供给 **&lt;EthDrv&gt;_Transmit**。

如果给定 [**EthIfController**](#924-ethifcontroller) 最近一次被接受的控制器模式为 **ETH_MODE_ACTIVE** 或 **ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**，则函数 **EthIf_Transmit** 应将调用转发给相应的以太网控制器驱动程序。否则该函数应拒绝发送请求并以 **E_NOT_OK** 返回。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **PhysAddrPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.52. EthIf_ImmediateTransmit

**说明**: 请求发送一个 **PDU**。本服务为同步调用，对不同的 **PduId** 可重入，对相同的 **PduId** 不可重入。参数 TxPduId（in）：要发送的 **PDU** 的标识符。参数 PduInfoPtr（in）：**PDU** 数据的长度和指针，以及指向元数据的指针。返回值 **Std_ReturnType**：**E_OK**：发送请求已被接受；**E_NOT_OK**：发送请求已被拒绝。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_ImmediateTransmit ( PduIdType TxPduId, const PduInfoType* PduInfoPtr )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **DataPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.53. EthIf_ReleaseRxBuffer

**说明**: 来自上层的指示，用于释放底层的接收缓冲区。本服务为同步调用，对不同的 **PduId** 可重入，对相同的 **PduId** 不可重入。参数 RxPduId（in）：所接收 **PDU** 的标识符。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_ReleaseRxBuffer ( PduIdType RxPduId )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **DataPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.54. EthIf_GetVersionInfo

**说明**: 返回本模块的版本信息。本服务为同步调用，可重入。参数 VersionInfoPtr（out）：本模块的版本信息。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_GetVersionInfo ( Std_VersionInfoType* VersionInfoPtr )
```

如果启用了开发错误检测：该函数应检查参数 **VersionInfoPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.55. EthIf_GetSwitchPortMode

**说明**: 获取被索引交换机端口的模式。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 PortModePtr（out）：**ETH_MODE_DOWN**：给定以太网交换机的以太网交换机端口被禁用；**ETH_MODE_ACTIVE**：给定以太网交换机的以太网交换机端口被启用。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法获取被索引交换机端口的模式，或者该函数在 **ETHSWT_STATE_UNINIT** 或 **ETHSWT_STATE_INIT** 状态下被调用。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetSwitchPortMode ( uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_ModeType* PortModePtr )
```

函数 **EthIf_GetSwitchPortMode** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetSwitchPortMode** 函数。

#### 7.3.56. EthIf_GetTransceiverMode

**说明**: 获取被索引收发器的状态。本服务为同步调用，不可重入。参数 TrcvIdx（in）：以太网收发器驱动程序上下文中收发器的索引。参数 TrcvModePtr（out）：**ETH_MODE_DOWN**：收发器被禁用；**ETH_MODE_ACTIVE**：收发器被启用。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：收发器无法初始化。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetTransceiverMode ( uint8 TrcvIdx, Eth_ModeType* TrcvModePtr )
```

函数 **EthIf_GetTransceiverMode** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **&lt;EthTrcv&gt;_GetTransceiverMode** 函数。

#### 7.3.57. EthIf_SwitchPortGetLinkState

**说明**: 获取被索引交换机端口的链路状态。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 LinkStatePtr（out）：**ETHTRCV_LINK_STATE_DOWN**：交换机端口已断开；**ETHTRCV_LINK_STATE_ACTIVE**：交换机端口已连接。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法获取被索引交换机端口的链路状态，或者该函数在 **ETHSWT_STATE_UNINIT** 或 **ETHSWT_STATE_INIT** 状态下被调用。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetLinkState ( uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_LinkStateType* LinkStatePtr )
```

函数 **EthIf_SwitchPortGetLinkState** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetLinkState** 函数。

#### 7.3.58. EthIf_TransceiverGetLinkState

**说明**: 获取被索引收发器的链路状态。本服务为同步调用，不可重入。参数 TrcvIdx（in）：以太网收发器驱动程序上下文中收发器的索引。参数 LinkStatePtr（out）：**ETHTRCV_LINK_STATE_DOWN**：收发器已断开；**ETHTRCV_LINK_STATE_ACTIVE**：收发器已连接。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：收发器无法初始化。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_TransceiverGetLinkState ( uint8 TrcvIdx, EthTrcv_LinkStateType* LinkStatePtr )
```

函数 **EthIf_TransceiverGetLinkState** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **&lt;EthTrcv&gt;_GetLinkState** 函数。

#### 7.3.59. EthIf_SwitchPortGetBaudRate

**说明**: 获取被索引交换机端口的波特率。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 BaudRatePtr（out）：**ETHTRCV_BAUD_RATE_10MBIT**：10MBit 连接；**ETHTRCV_BAUD_RATE_100MBIT**：100MBit 连接；**ETHTRCV_BAUD_RATE_1000MBIT**：1000MBit 连接；**ETHTRCV_BAUD_RATE_2500MBIT**：2500MBit 连接。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法获取被索引交换机端口的波特率，或者该函数在 **ETHSWT_STATE_UNINIT** 或 **ETHSWT_STATE_INIT** 状态下被调用。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetBaudRate ( uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_BaudRateType* BaudRatePtr )
```

函数 **EthIf_SwitchPortGetBaudRate** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetBaudRate** 函数。

#### 7.3.60. EthIf_TransceiverGetBaudRate

**说明**: 获取被索引收发器的波特率。本服务为同步调用，不可重入。参数 TrcvIdx（in）：以太网收发器驱动程序上下文中收发器的索引。参数 BaudRatePtr（out）：**ETHTRCV_BAUD_RATE_10MBIT**：10MBit 连接；**ETHTRCV_BAUD_RATE_100MBIT**：100MBit 连接；**ETHTRCV_BAUD_RATE_1000MBIT**：1000MBit 连接；**ETHTRCV_BAUD_RATE_2500MBIT**：2500MBit 连接。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：收发器无法初始化。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_TransceiverGetBaudRate ( uint8 TrcvIdx, EthTrcv_BaudRateType* BaudRatePtr )
```

函数 **EthIf_TransceiverGetBaudRate** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_GetBaudRate** 函数。

#### 7.3.61. EthIf_SwitchPortGetDuplexMode

**说明**: 获取被索引交换机端口的双工模式（**duplex mode**）。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 DuplexModePtr（out）：**ETHTRCV_DUPLEX_MODE_HALF**：半双工连接；**ETHTRCV_DUPLEXMODE_FULL**：全双工连接。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法获取被索引交换机端口的双工模式，或者该函数在 **ETHSWT_STATE_UNINIT** 或 **ETHSWT_STATE_INIT** 状态下被调用。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetDuplexMode ( uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_DuplexModeType* DuplexModePtr )
```

函数 **EthIf_SwitchPortGetDuplexMode** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetDuplexMode** 函数。

#### 7.3.62. EthIf_TransceiverGetDuplexMode

**说明**: 获取被索引收发器的双工模式。本服务为同步调用，不可重入。参数 TrcvIdx（in）：以太网收发器驱动程序上下文中收发器的索引。参数 DuplexModePtr（out）：**ETHTRCV_DUPLEX_MODE_HALF**：半双工连接；**ETHTRCV_DUPLEX_MODE_FULL**：全双工连接。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：收发器无法初始化。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_TransceiverGetDuplexMode ( uint8 TrcvIdx, EthTrcv_DuplexModeType* DuplexModePtr )
```

函数 **EthIf_TransceiverGetDuplexMode** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_GetDuplexMode** 函数。

#### 7.3.63. EthIf_SwitchPortGetCounterValues

**说明**: 读取交换机相应端口的丢弃计数器值列表。这些值的含义在 **Eth_CounterType** 中描述。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 CounterPtr（out）：符合 IETF RFC 1757、RFC 1643 和 RFC 2233 的计数器值。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：计数器值读取失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetCounterValues ( uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_CounterType* CounterPtr )
```

函数 **EthIf_SwitchPortGetCounterValues** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetCounterValues** 函数。

#### 7.3.64. EthIf_SwitchPortGetRxStats

**说明**: 返回以 **Eth_RxStatsType** 定义的一系列统计计数器。这些计数器中的大多数来自 IETF RFC 2819。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 RxStatsPtr（out）：符合 IETF RFC 2819（远程网络监控管理信息库）的值列表。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：无法获取丢弃计数器。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetRxStats ( uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_RxStatsType* RxStatsPtr )
```

函数 **EthIf_SwitchPortGetRxStats** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetRxStats** 函数。

#### 7.3.65. EthIf_SwitchPortGetTxStats

**说明**: 用于读取发送统计值的值列表。本服务为异步调用，不可重入。参数 SwitchIdx（in）：-。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 TxStatsPtr（out）：用于读取发送统计值的值列表。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOTOK**：无法获取发送统计信息。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetTxStats ( uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_TxStatsType* TxStatsPtr )
```

函数 **EthIf_SwitchPortGetTxStats** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetTxStats** 函数。

#### 7.3.66. EthIf_SwitchPortGetTxErrorCounterValues

**说明**: 用于读取发送统计错误计数器值的值列表。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 TxStatsPtr（out）：用于读取发送统计错误计数器值的值列表。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOTOK**：无法获取发送统计信息。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetTxErrorCounterValues ( uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_TxErrorCounterValuesType* TxStatsPtr )
```

函数 **EthIf_SwitchPortGetTxErrorCounterValues** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetTxErrorCounterValues** 函数。

#### 7.3.67. EthIf_SwitchPortGetMacLearningMode

**说明**: 返回 **MAC** 学习模式，即 1.) 硬件学习已启用；2.) 硬件学习已禁用；3.) 软件学习已启用。注意：该特性依赖于硬件，即交换机硬件需要支持不同的学习模式。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 MacLearningModePtr（out）：定义是否应学习 **MAC** 地址，以及应在软件中学习还是在硬件中学习。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：配置可能被持久重置。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetMacLearningMode ( uint8 SwitchIdx, uint8 SwitchPortIdx, EthSwt_MacLearningType* MacLearningModePtr )
```

函数 **EthIf_SwitchPortGetMacLearningMode** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetMacLearningMode** 函数。

#### 7.3.68. EthIf_GetSwitchPortIdentifier

**说明**: 此函数获取被索引以太网交换机端口的 **OUI**（24 位）。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 OrgUniqueIdPtr（out）：指向应存储组织唯一标识符（**OUI**）的内存的指针。参数 ModelNrPtr（out）：指向应存储制造商型号编号的内存的指针。参数 RevisionNrPtr（out）：指向应存储版本编号的内存的指针。返回值 **Std_ReturnType**：**E_OK**：以太网收发器的组织唯一标识符可被读取；**E_NOT_OK**：无法获取以太网收发器的组织唯一标识符（即 **OUI** 不可用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetSwitchPortIdentifier ( uint8 SwitchIdx, uint8 SwitchPortIdx, uint32* OrgUniqueIdPtr, uint8* ModelNrPtr, uint8* RevisionNrPtr )
```

函数 **EthIf_GetSwitchPortIdentifier** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetPortIdentifier** 函数。

#### 7.3.69. EthIf_GetSwitchIdentifier

**说明**: 获取由 IEEE 为被索引以太网交换机给出的组织唯一标识符。此函数应提供以太网交换机的 **OUI**。**OUI** 的大小为 24 位。如果以太网交换机可以提供 **OUI**，则 **OUI** 的 8 个最高有效位应设置为 0x00xxxxxx。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 OrgUniqueIdPtr（out）：指向应存储组织唯一标识符的内存的指针。返回值 **Std_ReturnType**：可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetSwitchIdentifier ( uint8 SwitchIdx, uint32* OrgUniqueIdPtr )
```

函数 **EthIf_GetSwitchIdentifier** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetSwitchIdentifier** 函数。

#### 7.3.70. EthIf_WritePortMirrorConfiguration

**说明**: 将给定的端口镜像配置存储在以太网交换机驱动程序中给定 **MirroredSwitchIdx** 的影子缓冲区（**shadow buffer**）中。本服务为同步调用，不可重入。参数 MirroredSwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引，需要被镜像的以太网交换机端口位于该交换机上。参数 PortMirrorConfigurationPtr（in）：-。返回值 **Std_ReturnType**：**E_OK**：被索引以太网交换机端口的端口镜像配置已写入；**E_NOT_OK**：被索引以太网交换机端口的端口镜像配置未写入（即以太网交换机不可用）；**ETHSWT_PORT_MIRRORING_CONFIGURATION_NOT_SUPPORTED**：以太网交换机驱动程序或以太网交换机不支持端口镜像配置。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_WritePortMirrorConfiguration ( uint8 MirroredSwitchIdx, const EthSwt_PortMirrorCfgType* PortMirrorConfigurationPtr )
```

函数 **EthIf_WritePortMirrorConfiguration** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_WritePortMirrorConfiguration** 函数。

#### 7.3.71. EthIf_ReadPortMirrorConfiguration

**说明**: 获取给定以太网交换机的端口镜像配置。本服务为同步调用，不可重入。参数 MirroredSwitchIdx（in）：以太网交换机驱动程序上下文中以太网交换机的索引，需要被镜像的以太网交换机端口位于该交换机上。参数 PortMirrorConfigurationPtr（out）：指向应存储端口配置的内存的指针。返回值 **Std_ReturnType**：**E_OK**：被索引以太网交换机端口的端口镜像配置读取成功；**E_NOT_OK**：被索引以太网交换机端口的端口镜像配置未读取成功。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_ReadPortMirrorConfiguration ( uint8 MirroredSwitchIdx, EthSwt_PortMirrorCfgType* PortMirrorConfigurationPtr )
```

函数 **EthIf_ReadPortMirrorConfiguration** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_ReadPortMirrorConfiguration** 函数。

#### 7.3.72. EthIf_DeletePortMirrorConfiguration

**说明**: 删除给定 **MirroredSwitchIdx** 的已存储端口镜像配置。如果没有找到给定 **MirroredSwitchIdx** 的端口镜像配置，则返回值应为 **E_OK**。本服务为同步调用，对不同的 **MirroredSwitchIdx** 可重入，对相同的 **SwitchIdx** 不可重入。参数 MirroredSwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。返回值 **Std_ReturnType**：**E_OK**：端口镜像配置删除成功；**E_NOT_OK**：端口镜像配置删除未成功（例如端口镜像已启用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_DeletePortMirrorConfiguration ( uint8 MirroredSwitchIdx )
```

函数 **EthIf_DeletePortMirrorConfiguration** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_DeletePortMirrorConfiguration** 函数。

#### 7.3.73. EthIf_GetPortMirrorState

**说明**: 获取被索引以太网交换机端口的端口镜像当前状态。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 PortIdx（in）：被寻址交换机上端口的索引。参数 PortMirrorStatePtr（out）：指向应存储给定以太网交换机端口端口镜像状态（**PORT_MIRRORING_ENABLED** 或 **PORT_MIRRORING_DISABLED**）的内存的指针。返回值 **Std_ReturnType**：**E_OK**：被索引以太网交换机端口的端口镜像状态返回成功；**E_NOT_OK**：被索引以太网交换机端口的端口镜像配置返回未成功（即被索引以太网交换机端口不可用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetPortMirrorState ( uint8 SwitchIdx, uint8 PortIdx, EthSwt_PortMirrorStateType* PortMirrorStatePtr )
```

#### 7.3.74. EthIf_SetPortMirrorState

**说明**: 请求为给定的以太网交换机设置端口镜像配置的给定端口镜像状态。本服务为同步调用，不可重入。参数 MirroredSwitchIdx（in）：以太网交换机驱动程序上下文中以太网交换机的索引，需要被启用和禁用（重复）的端口镜像配置位于该交换机上。参数 PortIdx（in）：被寻址交换机上端口的索引。参数 PortMirrorState（in）：包含所请求的端口镜像状态，**PORT_MIRRORING_ENABLED** 或 **PORT_MIRRORING_DISABLED**。返回值 **Std_ReturnType**：**E_OK**：被索引以太网交换机端口的所请求端口镜像状态设置成功；**E_NOT_OK**：被索引以太网交换机的所请求端口镜像状态未设置成功（即被索引以太网交换机不可用，或没有可用的端口镜像配置）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPortMirrorState ( uint8 MirroredSwitchIdx, uint8 PortIdx, EthSwt_PortMirrorStateType PortMirrorState )
```

函数 **EthIf_SetPortMirrorState** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_SetPortMirrorState** 函数。

#### 7.3.75. EthIf_SetPortTestMode

**说明**: 激活被索引以太网交换机端口的给定测试模式。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 PortIdx（in）：被寻址交换机上端口的索引。参数 Mode（in）：要激活的测试模式。返回值 **Std_ReturnType**：**E_OK**：被索引以太网交换机端口的端口测试模式设置成功；**E_NOT_OK**：被索引以太网交换机的端口测试模式未设置成功（即被索引以太网交换机端口不可用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPortTestMode ( uint8 SwitchIdx, uint8 PortIdx, EthTrcv_PhyTestModeType Mode )
```

函数 **EthIf_SetPortTestMode** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_SetPortTestMode** 函数。

#### 7.3.76. EthIf_SetPortLoopbackMode

**说明**: 激活被索引以太网交换机端口的给定测试环回模式。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 PortIdx（in）：被寻址交换机上端口的索引。参数 Mode（in）：要激活的环回模式。返回值 **Std_ReturnType**：**E_OK**：被索引以太网交换机端口的端口镜像环回模式激活成功；**E_NOT_OK**：被索引以太网交换机端口的端口镜像环回模式激活未成功（即被索引以太网交换机端口不可用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPortLoopbackMode ( uint8 SwitchIdx, uint8 PortIdx, EthTrcv_PhyLoopbackModeType Mode )
```

函数 **EthIf_SetPortLoopbackMode** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_SetPortLoopbackMode** 函数。

#### 7.3.77. EthIf_SetPortTxMode

**说明**: 激活被索引以太网交换机端口的给定发送模式。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 PortIdx（in）：被寻址交换机上端口的索引。参数 Mode（in）：要激活的发送模式。返回值 **Std_ReturnType**：**E_OK**：被索引以太网交换机端口的端口发送模式激活成功；**E_NOT_OK**：被索引以太网交换机端口的端口发送模式激活未成功（即被索引以太网交换机端口不可用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetPortTxMode ( uint8 SwitchIdx, uint8 PortIdx, EthTrcv_PhyTxModeType Mode )
```

函数 **EthIf_SetPortTxMode** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_SetPortTxMode** 函数。

#### 7.3.78. EthIf_GetPortCableDiagnosticsResult

**说明**: 获取被索引以太网交换机端口的电缆诊断结果。本服务为同步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 PortIdx（in）：被寻址交换机上端口的索引。参数 ResultPtr（out）：指向应存储电缆诊断结果的位置的指针。返回值 **Std_ReturnType**：**E_OK**：被索引以太网交换机端口的端口电缆诊断结果获取成功；**E_NOT_OK**：被索引以太网交换机端口的端口电缆诊断结果获取未成功（即被索引以太网交换机端口不可用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetPortCableDiagnosticsResult ( uint8 SwitchIdx, uint8 PortIdx, EthTrcv_CableDiagResultType* ResultPtr )
```

函数 **EthIf_GetPortCableDiagnosticsResult** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetPortCableDiagnosticsResult** 函数。

#### 7.3.79. EthIf_RunPortCableDiagnostic

**说明**: 通过调用所引用以太网收发器的 **EthTrcv_RunCableDiagnostic** 触发给定以太网交换机端口（**PortIdx**）的电缆诊断。本服务为同步调用，对不同的 **SwitchIdx** 和 **PortIdx** 可重入，对相同的 **SwitchIdx** 和 **PortIdx** 不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 PortIdx（in）：被寻址交换机上端口的索引。返回值 **Std_ReturnType**：**E_OK**：运行电缆诊断的触发已被接受；**E_NOT_OK**：运行电缆诊断的触发未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_RunPortCableDiagnostic ( uint8 SwitchIdx, uint8 PortIdx )
```

如果调用了函数 **EthIf_RunPortCableDiagnostic**，**EthIf** 应确保相应的 [**EthIfController**](#924-ethifcontroller) 处于 **ETH_MODE_ACTIVE** 模式，并将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_RunPortCableDiagnostic** 函数。

#### 7.3.80. EthIf_RunCableDiagnostic

**说明**: 触发给定以太网收发器的电缆诊断。本服务为同步调用，对不同的 **TrcvIdx** 可重入，对相同的 **TrcvIdx** 不可重入。参数 TrcvIdx（in）：以太网收发器驱动程序上下文中以太网收发器的索引。返回值 **Std_ReturnType**：**E_OK**：触发已被接受；**E_NOT_OK**：触发未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_RunCableDiagnostic ( uint8 TrcvIdx )
```

如果调用了函数 **EthIf_RunCableDiagnostic**，**EthIf** 应确保相应的 [**EthIfController**](#924-ethifcontroller) 处于 **ETH_MODE_ACTIVE** 模式，并将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_RunCableDiagnostic** 函数。

#### 7.3.81. EthIf_SwitchGetCfgDataRaw

**说明**: 以可变长度获取被索引以太网交换机内存中的数据。本服务为异步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中以太网交换机的索引。参数 Offset（in）：以太网交换机内存中开始读取的偏移量。参数 Length（in）：要复制的数据长度（字节）。参数 BufferPtr（out）：指向应复制数据的位置的指针。返回值 **Std_ReturnType**：**E_OK**：数据读取触发成功；**E_NOT_OK**：数据读取触发未成功（即被索引以太网交换机不可用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchGetCfgDataRaw ( uint8 SwitchIdx, uint32 Offset, uint16 Length, uint8* BufferPtr )
```

函数 **EthIf_SwitchGetCfgDataRaw** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetCfgDataRaw** 函数。

#### 7.3.82. EthIf_SwitchGetCfgDataInfo

**说明**: 获取被索引以太网交换机的数据总大小和内存起始地址。本服务为异步调用，可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中以太网交换机的索引。参数 DataSizePtr（out）：指向应复制配置数据总大小的位置的指针。参数 DataAdressPtr（out）：指向应复制配置寄存器起始地址的位置的指针。返回值 **Std_ReturnType**：**E_OK**：数据获取成功；**E_NOT_OK**：数据获取未成功（即被索引以太网交换机不可用）。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchGetCfgDataInfo ( uint8 SwitchIdx, uint32* DataSizePtr, uint32* DataAdressPtr )
```

函数 **EthIf_SwitchGetCfgDataInfo** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetCfgDataInfo** 函数。

#### 7.3.83. EthIf_SwitchPortGetMaxFIFOBufferFillLevel

**说明**: 该函数获取被索引以太网交换机发送（**egress**）端口分配的 **FIFO** 缓冲区的最大数量。如果以太网交换机硬件不支持基于以太网交换机端口的最大 **FIFO** 缓冲区水位，则 **SwitchPortEgressFifoBufferLevelPtr** 的内容应设置为 0xFFFFFFFF。本 **API** 可…（源文档此处截断）。本服务为异步调用，对不同的 **SwitchIdx** 和 **PortIdx** 可重入，对相同的 **SwitchIdx** 和 **PortIdx** 不可重入。参数 SwitchPortIdx（in）：以太网交换机驱动程序上下文中以太网交换机的索引。参数 PortIdx（in）：被寻址交换机上端口的索引。参数 SwitchPortEgressFifoIdx（in）：发送 **FIFO** 的索引。参数 SwitchPortEgressFifoBufferLevelPtr（out）：指向应存储最大缓冲区水位的内存的指针。返回值 **Std_ReturnType**：可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchPortGetMaxFIFOBufferFillLevel ( uint8 SwitchPortIdx, uint8 PortIdx, uint8 SwitchPortEgressFifoIdx, uint32* SwitchPortEgressFifoBufferLevelPtr )
```

函数 **EthIf_SwitchPortGetMaxFIFOBufferFillLevel** 应将调用转发给相应以太网交换机驱动程序（**EthIfSwitchIdx**）的 **EthSwt_GetMaxFIFOBufferFillLevel** 函数。

#### 7.3.84. EthIf_TransceiverGetMacMethod

**说明**: 获取收发器的介质访问模式。本服务为同步调用，不可重入。参数 TrcvIdx（in）：以太网收发器驱动程序上下文中收发器的索引。参数 MacModePtr（out）：**ETHTRCV_MAC_TYPE_CSMA_CD**：带冲突检测的载波侦听多路访问；**ETHTRCV_MAC_TYPE_PLCA**：物理层冲突避免。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：收发器请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_TransceiverGetMacMethod ( uint8* TrcvIdx, EthTrcv_MacMethodType* MacModePtr )
```

函数 **EthIf_TransceiverGetMacMethod** 应将调用转发给相应以太网收发器驱动程序（**EthIfTransceiverIdx**）的 **EthTrcv_GetMacMethod** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TrcvIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **MacModePtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.85. EthIf_EthGetSpiStatus

**说明**: 当使用 **MACPHY** 控制器时，获取 **SPI** 接口状态。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网控制器驱动程序上下文中控制器的索引。参数 SpiStatusPtr（out）：**SPI** 接口的状态。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：控制器请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_EthGetSpiStatus ( uint8* CtrlIdx, Eth_SpiStatusType* SpiStatusPtr )
```

函数 **EthIf_EthGetSpiStatus** 应将调用转发给相应以太网驱动程序（**CtrlIdx**）的 **Eth_GetSpiStatus** 函数。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **SpiStatusPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.86. EthIf_GetBufCV2xPC5RxParams

**说明**: 读出与所接收数据包的蜂窝 **V2X** 接收方向相关的值。例如，这可以是属于单个数据包的 **CBR**。本服务为同步调用，不可重入。参数 CtrlId（in）：以太网接口上下文中以太网控制器的索引。参数 RxParamIds（in）：要读取的参数的 **ID**。参数 NumParams（in）：参数的数量。参数 ParamValues（out）：所请求参数的值。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：读取参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetBufCV2xPC5RxParams ( uint8 CtrlId, const CV2x_BufCV2xPC5RxParamIdType* RxParamIds, uint16* ParamValues, uint8 NumParams )
```

函数 **EthIf_GetBufCV2xPC5RxParams** 应将调用转发给相应蜂窝 **V2X** 驱动程序的 **CV2x_GetBufCV2xPC5RxParams** 函数。

函数 **EthIf_GetBufCV2xPC5RxParams** 应可通过配置参数 **EthIfEnableCV2xApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **RxParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。注意：该函数要求事先已进行传输（[**EthIf_RxIndication**](#741-ethif_rxindication)）。

#### 7.3.87. EthIf_GetBufCV2xPC5TxParams

**说明**: 读出与所发送数据包的蜂窝 **V2X** 发送方向相关的值。例如，这可以是属于单个数据包的事务 **ID**。本服务为同步调用，不可重入。参数 CtrlId（in）：以太网接口上下文中以太网控制器的索引。参数 TxParamIds（in）：要获取的参数的 **ID**。参数 NumParams（in）：参数的数量。参数 ParamValues（out）：所请求参数的值。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：读取参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_GetBufCV2xPC5TxParams ( uint8 CtrlId, const CV2x_BufCV2xPC5TxParamIdType* TxParamIds, uint16* ParamValues, uint8 NumParams )
```

函数 **EthIf_GetBufCV2xPC5TxParams** 应将调用转发给相应蜂窝 **V2X** 驱动程序的 **CV2x_GetBufCV2xPC5TxParams** 函数。

函数 **EthIf_GetBufCV2xPC5TxParams** 应可通过配置参数 **EthIfEnableCV2xApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TxParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。注意：该函数要求事先已进行传输（[**EthIf_Transmit**](#7351-ethif_transmit)）。

#### 7.3.88. EthIf_SetBufCV2xPC5TxParams

**说明**: 为特定缓冲区（要发送的数据包）设置与蜂窝 **V2X** 发送方向相关的值。例如，这可以是属于单个数据包的期望的 ProSe 逐包优先级（**ProSe per-packet priority**）。本服务为同步调用，不可重入。参数 CtrlId（in）：以太网接口上下文中以太网控制器的索引。参数 BufIdx（in）：缓冲区资源的索引。参数 TxParamIds（in）：要设置的参数的 **ID**。参数 ParamValues（in）：要设置的参数的值。参数 NumParams（in）：参数的数量。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：设置参数失败。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SetBufCV2xPC5TxParams ( uint8 CtrlId, uint8 BufIdx, const CV2x_BufCV2xPC5TxParamIdType* TxParamIds, const uint16* ParamValues, uint8 NumParams )
```

函数 **EthIf_SetBufCV2xPC5TxParams** 应将调用转发给相应蜂窝 **V2X** 驱动程序的 **CV2x_SetBufCV2xPC5TxParams** 函数。

函数 **EthIf_SetBufCV2xPC5TxParams** 应可通过配置参数 **EthIfEnableCV2xApi** 在编译前进行开/关配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **TxParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

注意：该函数要求事先已进行传输（[**EthIf_ProvideTxBuffer**](#7350-ethif_providetxbuffer)）。

#### 7.3.89. EthIf_GetChanCV2xPC5TxParams

**说明**: 读取与信道接收方向相关的值。例如，这可以是信道繁忙比率（**CBR**）。本服务为同步调用，不可重入。参数 CtrlId（in）：蜂窝 **V2X** 驱动程序上下文中控制器的索引（收发器 **ID**）。参数 ChannelId（in）：收发器射频信道的索引。参数 ParamIds（in）：要读取的参数的 **ID**。参数 NumParams（in）：要读取的参数的数量。参数 ParamValues（out）：所请求参数的值。返回值 **Std_ReturnType**：**E_OK**：成功；**E_NOT_OK**：设置参数失败。

```C
Std_ReturnType EthIf_GetChanCV2xPC5TxParams ( uint8 CtrlId, uint8 ChannelId, const CV2x_GetChanTxParamIdType* ParamIds, uint32* ParamValues, uint8 NumParams )
```

函数 **EthIf_GetChanCV2xPC5TxParams** 应将调用转发给相应蜂窝 **V2X** 驱动程序的 **Cv2x_GetChanTxParams** 函数。

函数 **EthIf_GetChanCV2xPC5TxParams** 应可通过配置参数 **EthIfEnableCV2xApi** 在编译前进行开/关（**ON/OFF**）配置。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ChannelId** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamIds** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **ParamValues** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

#### 7.3.90. EthIf_SwitchMacSecUpdateSecY

**说明**: 请求以太网交换机使用所提供的参数更新所提供端口的 **SecY/PAC**。在首次调用时应配置一个带有所提供 **SCI** 的传输安全通道（**Transmission Secure Channel**）。应提供指向 **MACsec** 基本参数配置文件的指针以创建安全通道。本服务为异步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 MACsecCfgPtr（in）：指向用于配置 **MACsec** 实体（**SecY**）的结构的指针。参数 TxSci（in）：**MACsec** 传输安全通道的安全通道标识符。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecUpdateSecY ( const EthSwt_MgmtInfoType* MgmtInfoPtr, const Mka_MacSecConfigType* MACsecCfgPtr, uint64 TxSci )
```

#### 7.3.91. EthIf_MacSecUpdateSecY

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器使用所提供的参数更新 **PHY** 的 **SecY/PAC**。在首次调用时应配置一个带有所提供 **SCI** 的传输安全通道。应提供指向 **MACsec** 基本参数配置文件的指针以创建安全通道。本服务为异步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 MACsecCfgPtr（in）：指向用于配置 **MACsec** 实体（**SecY**）的结构的指针。参数 TxSci（in）：**MACsec** 传输安全通道的安全通道标识符。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecUpdateSecY ( uint8 CtrlIdx, const Mka_MacSecConfigType* MACsecCfgPtr, uint64 TxSci )
```

#### 7.3.92. EthIf_SwitchMacSecUpdateSecYNotification

**说明**: 通知 [**EthIf_SwitchMacSecUpdateSecY**](#7390-ethif_switchmacsecupdatesecy) 已完成的回调。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_SwitchMacSecUpdateSecYNotification ( const EthSwt_MgmtInfoType* MgmtInfoPtr )
```

#### 7.3.93. EthIf_MacSecUpdateSecYNotification

**说明**: 通知 [**EthIf_SwitchMacSecUpdateSecY**](#7390-ethif_switchmacsecupdatesecy) 已完成的回调。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_MacSecUpdateSecYNotification ( uint8 CtrlIdx )
```

#### 7.3.94. EthIf_SwitchMacSecInitRxSc

**说明**: 请求以太网交换机驱动程序为给定的安全通道标识符配置一个接收安全通道（**Reception Secure Channel**）。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 Sci（in）：**MACsec** 接收安全通道的安全通道标识符。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecInitRxSc ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint64 Sci )
```

#### 7.3.95. EthIf_MacSecInitRxSc

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序为给定的安全通道标识符配置一个接收安全通道。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 Sci（in）：**MACsec** 接收安全通道的安全通道标识符。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecInitRxSc ( uint8 CtrlIdx, uint64 Sci )
```

#### 7.3.96. EthIf_SwitchMacSecResetRxSc

**说明**: 请求以太网交换机驱动程序将给定安全通道标识符的接收安全通道的 **MACsec** 值重置为默认值。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 Sci（in）：**MACsec** 接收安全通道的安全通道标识符。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecResetRxSc ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint64 Sci )
```

#### 7.3.97. EthIf_MacSecResetRxSc

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序将给定安全通道标识符的接收安全通道的 **MACsec** 值重置为默认值。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 Sci（in）：**MACsec** 接收安全通道的安全通道标识符。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecResetRxSc ( uint8 CtrlIdx, uint64 Sci )
```

#### 7.3.98. EthIf_SwitchMacSecAddTxSa

**说明**: 请求以太网交换机驱动程序在所提供的端口中创建一个传输安全关联（**Transmission Secure Association**）。包含短安全通道标识符以支持 **XPN** 配置。本服务为异步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 An（in）：在 **MACsec** 传输安全关联中使用的关联编号。参数 NextPn（in）：**MACsec** 传输安全关联中下一个被接受的包编号。参数 Ssci（in）：在 **MACsec** 传输安全关联中使用的短安全通道标识符。参数 KeysPtr（in）：指向要在 **MACsec** 传输安全关联中使用的 **SAK** 密钥（及所需密钥信息）的指针。参数 Active（in）：用于启用/禁用 **MACsec** 传输安全关联的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecAddTxSa ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint8 An, uint64 NextPn, uint32 Ssci, const Mka_SakKeyPtrType* KeysPtr, boolean Active )
```

#### 7.3.99. EthIf_MacSecAddTxSa

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序在收发器中创建一个传输安全关联。包含短安全通道标识符以支持 **XPN** 配置。本服务为异步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 An（in）：在 **MACsec** 传输安全关联中使用的关联编号。参数 NextPn（in）：**MACsec** 传输安全关联中下一个被接受的包编号。参数 Ssci（in）：在 **MACsec** 传输安全关联中使用的短安全通道标识符。参数 KeysPtr（in）：指向要在 **MACsec** 传输安全关联中使用的 **SAK** 密钥（及所需密钥信息）的指针。参数 Active（in）：用于启用/禁用 **MACsec** 传输安全关联的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecAddTxSa ( uint8 CtrlIdx, uint8 An, uint64 NextPn, uint32 Ssci, const Mka_SakKeyPtrType* KeysPtr, boolean Active )
```

#### 7.3.100. EthIf_SwitchMacSecAddTxSaNotification

**说明**: 通知 [**EthIf_SwitchMacSecAddTxSa**](#7398-ethif_switchmacsecaddtxsa) 已完成的回调。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_SwitchMacSecAddTxSaNotification ( const EthSwt_MgmtInfoType* MgmtInfoPtr )
```

#### 7.3.101. EthIf_MacSecAddTxSaNotification

**说明**: 通知 [**EthIf_MacSecAddTxSa**](#7399-ethif_macsecaddtxsa) 已完成的回调。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_MacSecAddTxSaNotification ( uint8 CtrlIdx )
```

#### 7.3.102. EthIf_SwitchMacSecUpdateTxSa

**说明**: 请求以太网交换机驱动程序使用给定的包编号更新传输安全关联。**Active** 参数用于更改指定 **AN** 的状态。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 An（in）：在 **MACsec** 传输安全关联中使用的关联编号。参数 NextPn（in）：**MACsec** 传输安全关联中下一个被接受的包编号。参数 Active（in）：用于启用/禁用 **MACsec** 传输安全关联的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecUpdateTxSa ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint8 An, uint64 NextPn, boolean Active )
```

#### 7.3.103. EthIf_MacSecUpdateTxSa

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序使用给定的包编号更新传输安全关联。**Active** 参数用于更改指定 **AN** 的状态。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 An（in）：在 **MACsec** 传输安全关联中使用的关联编号。参数 NextPn（in）：**MACsec** 传输安全关联中下一个被接受的包编号。参数 Active（in）：用于启用/禁用 **MACsec** 传输安全关联的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecUpdateTxSa ( uint8 CtrlIdx, uint8 An, uint64 NextPn, boolean Active )
```

#### 7.3.104. EthIf_SwitchMacSecDeleteTxSa

**说明**: 请求以太网交换机驱动程序移除由所提供的关联编号标识的传输安全关联。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 An（in）：在 **MACsec** 传输安全关联中使用的关联编号。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecDeleteTxSa ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint8 An )
```

#### 7.3.105. EthIf_MacSecDeleteTxSa

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序移除由所提供的关联编号标识的传输安全关联。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 An（in）：在 **MACsec** 传输安全关联中使用的关联编号。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecDeleteTxSa ( uint8 CtrlIdx, uint8 An )
```

#### 7.3.106. EthIf_SwitchMacSecAddRxSa

**说明**: 请求以太网交换机驱动程序在所提供的端口中创建一个接收安全关联（**Reception Secure Association**）。包含短安全通道标识符以支持 **XPN** 配置。本服务为异步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 An（in）：在 **MACsec** 接收安全关联中使用的关联编号。参数 LowestPn（in）：**MACsec** 接收安全关联中被接受的最低包编号。参数 Ssci（in）：在 **MACsec** 接收安全关联中使用的短安全通道标识符。参数 KeysPtr（in）：指向要在 **MACsec** 接收安全关联中使用的 **SAK** 密钥（及所需密钥信息）的指针。参数 Active（in）：用于启用/禁用 **MACsec** 接收安全关联的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecAddRxSa ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint8 An, uint64 LowestPn, uint32 Ssci, const Mka_SakKeyPtrType* KeysPtr, boolean Active )
```

#### 7.3.107. EthIf_MacSecAddRxSa

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序在收发器中创建一个接收安全关联。包含短安全通道标识符以支持 **XPN** 配置。本服务为异步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 An（in）：在 **MACsec** 接收安全关联中使用的关联编号。参数 LowestPn（in）：**MACsec** 接收安全关联中被接受的最低包编号。参数 Ssci（in）：在 **MACsec** 接收安全关联中使用的短安全通道标识符。参数 KeysPtr（in）：指向要在 **MACsec** 接收安全关联中使用的 **SAK** 密钥（及所需密钥信息）的指针。参数 Active（in）：用于启用/禁用 **MACsec** 接收安全关联的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecAddRxSa ( uint8 CtrlIdx, uint8 An, uint64 LowestPn, uint32 Ssci, const Mka_SakKeyPtrType* KeysPtr, boolean Active )
```

#### 7.3.108. EthIf_SwitchMacSecAddRxSaNotification

**说明**: 通知 [**EthIf_SwitchMacSecAddRxSa**](#73106-ethif_switchmacsecaddrxsa) 已完成的回调。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_SwitchMacSecAddRxSaNotification ( const EthSwt_MgmtInfoType* MgmtInfoPtr )
```

#### 7.3.109. EthIf_MacSecAddRxSaNotification

**说明**: 通知 [**EthIf_MacSecAddRxSa**](#73107-ethif_macsecaddrxsa) 已完成的回调。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_MacSecAddRxSaNotification ( uint8 CtrlIdx )
```

#### 7.3.110. EthIf_SwitchMacSecUpdateRxSa

**说明**: 请求以太网交换机驱动程序使用给定的包编号更新接收安全关联。**Active** 参数用于更改指定 **AN** 的状态。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 An（in）：在 **MACsec** 接收安全关联中使用的关联编号。参数 LowestPn（in）：**MACsec** 接收安全关联中被接受的最低包编号。参数 Active（in）：用于启用/禁用 **MACsec** 接收安全关联的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecUpdateRxSa ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint8 An, uint64 LowestPn, boolean Active )
```

#### 7.3.111. EthIf_MacSecUpdateRxSa

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序使用给定的包编号更新接收安全关联。**Active** 参数用于更改指定 **AN** 的状态。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 An（in）：在 **MACsec** 接收安全关联中使用的关联编号。参数 LowestPn（in）：**MACsec** 接收安全关联中被接受的最低包编号。参数 Active（in）：用于启用/禁用 **MACsec** 接收安全关联的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecUpdateRxSa ( uint8 CtrlIdx, uint8 An, uint64 LowestPn, boolean Active )
```

#### 7.3.112. EthIf_SwitchMacSecDeleteRxSa

**说明**: 请求以太网交换机驱动程序移除由所提供的关联编号标识的接收安全关联。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 An（in）：在 **MACsec** 接收安全关联中使用的关联编号。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecDeleteRxSa ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint8 An )
```

#### 7.3.113. EthIf_MacSecDeleteRxSa

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序移除由所提供的关联编号标识的接收安全关联。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 An（in）：在 **MACsec** 接收安全关联中使用的关联编号。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecDeleteRxSa ( uint8 CtrlIdx, uint8 An )
```

#### 7.3.114. EthIf_SwitchMacSecGetTxSaNextPn

**说明**: 请求以太网交换机驱动程序返回给定传输安全关联中用于下一个数据包的包编号。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 An（in）：在 **MACsec** 传输安全关联中使用的关联编号。参数 NextPnPtr（out）：指向从 **MACsec** 实体（**SecY**）读出的下一个包编号的指针。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecGetTxSaNextPn ( const EthSwt_MgmtInfoType* MgmtInfoPtr, uint8 An, uint64* NextPnPtr )
```

#### 7.3.115. EthIf_MacSecGetTxSaNextPn

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序返回给定传输安全关联中用于下一个数据包的包编号。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 An（in）：在 **MACsec** 传输安全关联中使用的关联编号。参数 NextPnPtr（out）：指向从 **MACsec** 实体（**SecY**）读出的下一个包编号的指针。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecGetTxSaNextPn ( uint8 CtrlIdx, uint8 An, uint64* NextPnPtr )
```

#### 7.3.116. EthIf_SwitchMacSecGetMacSecStats

**说明**: 请求以太网交换机驱动程序提供 **MACsec** 统计信息。结果通过 [**EthIf_SwitchMacSecGetMacSecStatsNotification**](#73118-ethif_switchmacsecgetmacsecstatsnotification) 返回。本服务为异步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecGetMacSecStats ( const EthSwt_MgmtInfoType* MgmtInfoPtr )
```

#### 7.3.117. EthIf_MacSecGetMacSecStats

**说明**: 请求以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序提供 **MACsec** 统计信息。结果通过 [**EthIf_MacSecGetMacSecStatsNotification**](#73119-ethif_macsecgetmacsecstatsnotification) 返回。本服务为异步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecGetMacSecStats ( uint8 CtrlIdx )
```

#### 7.3.118. EthIf_SwitchMacSecGetMacSecStatsNotification

**说明**: 通知 [**EthIf_SwitchMacSecGetMacSecStats**](#73116-ethif_switchmacsecgetmacsecstats) 已完成并提供所请求统计信息的回调。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 MacSecStatsPtr（in）：指向包含 **MKA** 参与者（**participant**）**MACsec** 统计信息的结构的指针。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_SwitchMacSecGetMacSecStatsNotification ( const EthSwt_MgmtInfoType* MgmtInfoPtr, const Mka_Stats_SecYType* MacSecStatsPtr )
```

#### 7.3.119. EthIf_MacSecGetMacSecStatsNotification

**说明**: 通知 [**EthIf_MacSecGetMacSecStats**](#73117-ethif_macsecgetmacsecstats) 已完成并提供所请求统计信息的回调。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 MacSecStatsPtr（in）：指向包含 **MKA** 参与者 **MACsec** 统计信息的结构的指针。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_MacSecGetMacSecStatsNotification ( uint8 CtrlIdx, const Mka_Stats_SecYType* MacSecStatsPtr )
```

#### 7.3.120. EthIf_SwitchMacSecOperational

**说明**: 通知 **EthIf** **MACsec** 已可运行（**operational**）且可以通知 **EthSM**。（交换机情况）本服务为同步调用，可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 MacSecOperational（in）：用于通知 **MACsec** 是否可运行的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecOperational ( const EthSwt_MgmtInfoType* MgmtInfoPtr, boolean MacSecOperational )
```

#### 7.3.121. EthIf_MacSecOperational

**说明**: 通知 **EthIf** **MACsec** 已可运行且可以告知 **EthSM**。（以太网接口（软件实现的 **MACsec**）或以太网收发器驱动程序）本服务为同步调用，可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 MacSecOperational（in）：用于通知 **MACsec** 是否可运行的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecOperational ( uint8 CtrlIdx, boolean MacSecOperational )
```

#### 7.3.122. EthIf_SwitchMacSecSetControlledPortEnabled

**说明**: 请求设置 **PAE** 的受控端口启用（**Controlled Port enabled**）参数。本服务为同步调用，对不同的 **MgmtInfoPtr** 可重入，对相同的 **MgmtInfoPtr** 不可重入。参数 MgmtInfoPtr（in）：指向以太网交换机驱动程序上下文中管理信息的指针。**SwitchIdx** 在 **EthIf** 上下文中，**PortIdx** 在 **EthSwt** 上下文中。参数 ControlledPortEnabled（in）：用于激活 **PAE** 受控端口的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_SwitchMacSecSetControlledPortEnabled ( const EthSwt_MgmtInfoType* MgmtInfoPtr, boolean ControlledPortEnabled )
```

#### 7.3.123. EthIf_MacSecSetControlledPortEnabled

**说明**: 请求设置 **PAE** 的受控端口启用参数。本服务为同步调用，对不同的 **CtrlIdx** 可重入，对相同的 **CtrlIdx** 不可重入。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 ControlledPortEnabled（in）：用于激活 **PAE** 受控端口的布尔值。返回值 **Std_ReturnType**：**E_OK**：请求已被接受；**E_NOT_OK**：请求未被接受。可通过**EthIf.h**获得。

```C
Std_ReturnType EthIf_MacSecSetControlledPortEnabled ( uint8 CtrlIdx, boolean ControlledPortEnabled )
```

#### 7.3.124. EthIf_GetStreamHandleIdxStatistics

**说明**: 此函数由防火墙模块调用，用于从交换机获取桶计数器（**bucket counter**）统计信息。本服务为同步调用，可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_GetStreamHandleIdxStatistics ( uint8 SwitchIdx )
```

#### 7.3.125. EthIf_SetStreamHandleIdxConfiguration

**说明**: 此函数由防火墙模块调用，用于控制交换机中某个 **StreamHandleIdx** 的活动状态。本服务为同步调用，可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 StreamHandleIdxPtr（in）：指向应设置状态的 **StreamHandleIdx** 的指针。参数 StreamHandleIdxActivityStatus（in）：要设置的 **StreamHandleIdx** 的活动状态（**True** = 活动状态，**False** = 非活动状态）。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_SetStreamHandleIdxConfiguration ( uint8 SwitchIdx, uint8 StreamHandleIdxPtr, boolean StreamHandleIdxActivityStatus )
```

### 7.4. 回调通知

这是提供给其他模块的函数列表。

#### 7.4.1. EthIf_RxIndication

**说明**: 由被索引控制器接收到的以太网帧的接收指示。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中物理以太网控制器的索引。参数 FrameType（in）：所接收以太网帧的帧类型。参数 IsBroadcast（in）：用于指示广播帧的参数。参数 PhysAddrPtr（in）：指向所接收以太网帧的物理源地址（网络字节序的 **MAC** 地址）的指针。参数 DataPtr（in）：指向所接收以太网帧有效载荷的指针。参数 DataLen（in）：所接收帧中有效载荷的长度（字节）。参数 IngressTimeTuplePtr（in）：以时间元组形式提供的接收方向时间戳的指针。参数 RxHandleId（in）：由以太网驱动程序提供的唯一接收句柄 **ID**，用于逐标识入方向队列元素。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_RxIndication ( uint8 CtrlIdx, Eth_FrameType FrameType, boolean IsBroadcast, const uint8* PhysAddrPtr, const Eth_DataType* DataPtr, uint16 DataLen, TimeTupleType* IngressTimeTuplePtr, uint8 RxHandleId )
```

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **DataPtr** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_PARAM_POINTER**](#631-开发错误)。

以太网驱动程序应通过参数 **IsBroadcast** 向以太网接口指示广播报文。

如果 **VLAN** 未激活，以太网接口应递增相应的测量数据并过滤该报文。

#### 7.4.2. EthIf_TxConfirmation

**说明**: 确认由被索引控制器进行的帧发送。本服务为同步调用，不可重入。参数 CtrlIdx（in）：以太网接口上下文中物理以太网控制器的索引。参数 BufIdx（in）：已发送缓冲区的索引。参数 Result（in）：**E_OK**：发送成功；**E_NOT_OK**：发送失败。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_TxConfirmation ( uint8 CtrlIdx, Eth_BufIdxType BufIdx, Std_ReturnType Result )
```

**EthIf_TxConfirmation** 应将在 **EthIf_TxConfirmation** 内接收到的 **Result** 通过 **&lt;UL&gt;_TxConfirmation** 传递给所配置的上层。

如果启用了开发错误检测：该函数应检查之前是否已调用过服务 [**EthIf_Init**](#731-ethif_init)。如果检查失败，该函数应引发开发错误 [**ETHIF_E_UNINIT**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **CtrlIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_CTRL_IDX**](#631-开发错误)。

如果启用了开发错误检测：该函数应检查参数 **BufIdx** 是否有效。如果检查失败，该函数应引发开发错误 [**ETHIF_E_INV_PARAM**](#631-开发错误)。

#### 7.4.3. EthIf_CtrlModeIndication

**说明**: 在模式被读取出来时异步调用。由之前的 **&lt;EthDrv&gt;_SetControllerMode** 调用触发。可以在触发函数内直接调用。本服务为同步调用，对相同的 **CtrlIdx** 不可重入，对不同的 **CtrlIdx** 可重入。参数 CtrlIdx（in）：以太网接口上下文中物理以太网控制器的索引。参数 CtrlMode（in）：被通知的以太网控制器模式。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_CtrlModeIndication ( uint8 CtrlIdx, Eth_ModeType CtrlMode )
```

该函数应调用 **EthSM_CtrlModeIndication**。

#### 7.4.4. EthIf_TrcvModeIndication

**说明**: 在模式变更被读取出来时异步调用。如果该函数由之前调用的 **EthTrcv_SetTransceiverMode** 触发，则可以在触发函数内直接调用。本服务为同步调用，对相同的 **CtrlIdx** 不可重入，对不同的 **CtrlIdx** 可重入。参数 TrcvIdx（in）：以太网接口上下文中以太网收发器的索引。参数 TrcvMode（in）：被通知的以太网收发器模式。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_TrcvModeIndication ( uint8 TrcvIdx, Eth_ModeType TrcvMode )
```

#### 7.4.5. EthIf_SwitchPortModeIndication

**说明**: **EthIf** 应根据 **EthSwtPort** 配置确定预期的通知。如果 **EthSwtPort** 引用一个 **EthTrcv**，则 **EthIf** 期望来自 **EthTrcv** 的通知，通过 **API** **[EthIf_TrcvModeIndication](#744-ethif_trcvmodeindication)()**。否则 **EthIf** 期望来自 **EthSwt** 的通知，通过 **API** **EthIf_SwitchPortModeIndication()**。本服务为异步调用，不可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 SwitchPortIdx（in）：被寻址交换机上端口的索引。参数 PortMode（in）：被通知的以太网交换机端口模式。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_SwitchPortModeIndication ( uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_ModeType PortMode )
```

#### 7.4.6. EthIf_SleepIndication

**说明**: 如果在网络中检测到睡眠指示（**sleep indication**），则由相应的 **EthTrcv** 调用此 **API**。例如，这可用于符合 OA **TC10** 的以太网硬件。在这种情况下，以太网硬件（**PHY**）检测到由睡眠请求（**Sleep.Request**）触发的睡眠指示（**Sleep.Indication**）。本服务为同步调用，可重入。参数 TrcvIdx（in）：以太网接口上下文中以太网收发器的索引。该服务无返回值。可通过**EthIf.h**获得。

```C
void EthIf_SleepIndication ( uint8 TrcvIdx )
```

该函数应使用相应的 **EthIfCtrl** 调用 **EthSM_SleepIndication**。

#### 7.4.7. EthIf_StreamHandleIdxConfiguration

**说明**: 一旦 **EthSwtDrv** 在交换机中成功设置了 **StreamHandleIdx** 活动状态，该函数就由 **EthSwtDrv** 调用。本服务为同步调用，可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 StreamHandleIdxPtr（in）：指向返回其当前状态的 **StreamHandleIdx** 的指针。参数 StreamHandleIdxActivityStatus（in）：**StreamHandleIdx** 的活动状态（**True** = 活动状态，**False** = 非活动状态）。该服务无返回值。可通过**EthIf_Cbk.h**获得。

```C
void EthIf_StreamHandleIdxConfiguration ( uint8 SwitchIdx, uint8 StreamHandleIdxPtr, boolean StreamHandleIdxActivityStatus )
```

#### 7.4.8. EthIf_StreamHandleIdxStatistics

**说明**: 一旦 **EthSwtDrv** 成功地从交换机中获取了桶计数器值，该函数就由 **EthSwtDrv** 调用。本服务为同步调用，可重入。参数 SwitchIdx（in）：以太网交换机驱动程序上下文中交换机的索引。参数 NumberOfBuckets（in）：交换机中计数桶的数量。参数 StreamHandleIdxStatisticsPtr（in）：指向桶计数器值的指针。该服务无返回值。可通过**EthIf_Cbk.h**获得。

```C
void EthIf_StreamHandleIdxStatistics ( uint8 SwitchIdx, uint8 NumberOfBuckets, const uint8* StreamHandleIdxStatisticsPtr )
```

### 7.5. 调度函数

这些函数由基础软件调度器（**Basic Software Scheduler**）直接调用。以下函数应没有返回值和参数。所有函数均应不可重入。

#### 7.5.1. EthIf_MainFunctionRx

**说明**: 该函数检查新接收的帧，并以轮询模式发出接收指示。可通过**SchM_EthIf.h**获得。

```C
void EthIf_MainFunctionRx ( void )
```

接收帧检查应可通过配置参数 **EthIfEnableRxInterrupt** 在编译前进行开/关配置。

#### 7.5.2. EthIf_MainFunctionRx_&lt;PriorityProcessing ShortName&gt;

**说明**: 该函数通过使用相应的 **FifoIdx** 调用 **&lt;EthDrv&gt;_Receive()**，检查相关以太网控制器或 **CanXL** 控制器及接收队列处的新接收帧。[**EthIf_MainFunctionRx**](#751-ethif_mainfunctionrx) 应从所有未通过 **EthIfPhysCtrlRxMainFunctionPriorityProcessing** 分配用于处理的 **FIFO** 中接收帧。可通过**EthIf_SchM.h**获得。

```C
void EthIf_MainFunctionRx_<PriorityProcessing ShortName> ( void )
```

#### 7.5.3. EthIf_MainFunctionRx_&lt;IngressQueueProcessing ShortName&gt;

**说明**: 该函数在相关以太网控制器及通过 **EthIfPhysCtrlRxIngressQueueRef** 引用的相关入方向队列处，或在相关 **Can XL** 控制器及通过 **EthIfCanXLCtrlRxIngressFifoRef** 引用的相关入方向 **FIFO** 处，检查新接收的以太网帧。对于以太网控制器，调用 **Eth…**（源文档此处截断）。可通过**EthIf.h**获得。

```C
void EthIf_MainFunctionRx_<IngressQueueProcessing ShortName> ( void )
```

#### 7.5.4. EthIf_MainFunctionTx

**说明**: 该函数以轮询模式发出发送确认。它还检查收发器状态变化。可通过**SchM_EthIf.h**获得。

```C
void EthIf_MainFunctionTx ( void )
```

发送确认检查应可通过配置参数 **EthIfEnableTxInterrupt** 在编译前进行开/关配置。

轮询收发器状态变化的频率应可通过配置参数 **EthIfTrcvLinkStateChgMainReload** 进行配置。

#### 7.5.5. EthIf_MainFunctionState

**说明**: 该函数轮询不同的通信硬件（以太网收发器、以太网交换机端口）相关信息，例如链路状态、信号质量。本服务为异步调用，不可重入。该服务无参数。该服务无返回值。可通过**EthIf_SchM.h**获得。

```C
void EthIf_MainFunctionState ( void )
```

函数 **EthIf_MainFunctionState** 应以 **EthIfMainFunctionStatePeriod** 的周期轮询以太网通信硬件相关信息。

对于每个链路状态为 **ETHTRCV_LINK_STATE_ACTIVE** 且引用以太网收发器的以太网交换机端口，该函数应通过调用 **EthSwt_GetPortSignalQuality** 轮询信号质量。

对于每个链路状态为 **ETHTRCV_LINK_STATE_ACTIVE** 的以太网收发器，该函数应通过调用 **EthTrcv_GetPhySignalQuality** 轮询信号质量。

所获取的信号质量值应存储为 [**EthIf_SignalQualityResultType**](#724-ethif_signalqualityresulttype) 类型。该值应始终存储为 **ActualSignalQuality**。如果所获取的信号质量高于已存储的最高信号质量（**HighestSignalQuality**），则应使用所获取的信号质量更新 **HighestSignalQuality**。如果所获取的信号质量低于最低信号质量（**LowestSignalQuality**），则应使用所获取的信号质量更新 **LowestSignalQuality**。

**EthIf** 应检查其维护的以太网硬件（以太网交换机端口、以太网收发器）在以下条件下是否已达到所请求的模式和所请求的链路状态：

* 关闭 **EthSwtPort** 的定时器（参见 **EthIfSwitchOffPortTimeDelay**）未在运行，且
* 保持 **EthSwtPort** 处于 **ETH_MODE_ACTIVE** 的定时器（参见 **EthIfPortStartupActiveTime**）未在运行，且该 **EthSwtPort** 未被以 **ETH_MODE_ACTIVE** 请求

如果 **EthIf** 检测到所请求的模式和/或所请求的链路状态尚未达到，**EthIf** 应分别重新触发所请求的模式和链路状态。

注意：

1. 如果使用例如符合 OA **TC10** 的硬件（参见 [5, OPEN Sleep/Wake-up Specification for Automotive Ethernet]），这应确保在网络中重新触发唤醒。
2. 此外，如果关闭 **EthSwtPort** 的定时器（通过 **EthIfSwitchOffPortTimeDelay** 请求）或保持 **EthSwtPort** 活动的定时器（通过 **EthIfPortStartupActiveTime** 请求）正在运行，则该检查不应尝试重新建立所请求的模式。在 **EthIf** …之后关闭以太网交换网络中的以太网硬件（源文档此处截断）。

对于所引用 **EthTrcv** 充当被动通信从属（**passive communication slave**）（**EthTrcvActAsSlavePassiveEnabled** 设置为 **TRUE**）的 [**EthIfTransceiver**](#9212-ethiftransceiver)，**EthIf** 应检查意外的链路断开。如果意外链路断开（链路状态被以 **ETHTRCV_LINK_STATE_ACTIVE** 请求，但当前链路状态为 **ETHTRCV_LINK_STATE_DOWN**）持续了 **EthIfQualifiedUnexptecedLinkDownTime** 中指定的时间，**EthIf** 应通过调用 **EthSM_SleepIndication** 触发释放受影响的通信通道。如果检测到意外链路断开，则应通过 **EthSM_TrcvLinkStateChg** 立即向 **EthSM** 发出指示，而不考虑 **EthIfQualifiedUnexpectedLinkDownTime**。

注意：该需求应保证充当被动通信通道的通信通道即使通信主站（**communication master**）无法通过网络传输睡眠（例如硬件故障、充当通信主站的 **ECU** 意外关闭等）也会关闭。

### 7.6. 期望接口

在本章中列出了从其他模块要求的所有接口。

#### 7.6.1. 强制接口

注意：本节定义了实现模块核心功能所要求的全部接口。

| API 函数 | 头文件 | 描述 |
| --- | --- | --- |
| 没有强制接口。 |  |  |

#### 7.6.2. 可选接口

本节定义了实现模块可选功能所要求的全部接口。

| API 函数 | 头文件 | 描述 |
| --- | --- | --- |
| BswM_EthIf_PortGroupLinkStateChg | BswM_EthIf.h | 由 **EthIf** 调用的函数，用于指示某个以太网交换机端口组的链路状态变化。 |
| CanXL_GetControllerMode | CanXL.h | 获取被索引控制器的通信状态 |
| CanXL_GetPhysAddr | CanXL.h | 获取被索引控制器所使用的物理源地址 |
| CanXL_ProvideTxBuffer | CanXL.h | 提供对与指定优先级相关的队列的发送缓冲区的访问 |
| CanXL_Receive | CanXL.h | 从相关队列接收一帧。 |
| CanXL_SetControllerMode | CanXL.h | 启用/禁用被索引控制器的 **Rx/Tx** 通信 |
| CanXL_Transmit | CanXL.h | 触发对之前已填充的发送缓冲区的发送 |
| CanXL_TxConfirmation | CanXL.h | 触发帧发送确认 |
| CanXLTrcv_GetLinkState | CanXLTrcv.h | 获取被索引收发器的链路状态 |
| CanXLTrcv_GetTransceiverMode | CanXLTrcv.h | 获取被索引收发器的状态 |
| CanXLTrcv_SetTransceiverMode | CanXLTrcv.h | 启用/禁用被索引收发器 |
| CV2x_GetBufCV2xPC5RxParams | CV2x.h | 读出与所接收数据包相关的值。例如，这可以是属于单个数据包的 **CBR**。此 **API** 仅在 **CV2x_Receive** 的上下文内有效 |
| CV2x_GetBufCV2xPC5TxParams | CV2x.h | 读出与所发送数据包接收方向相关的值。例如，这可以是属于单个数据包的事务 **ID**。此 **API** 仅在 **CV2x_TxConfirmation** 的上下文内有效 |
| CV2x_GetChanCV2xPC5TxParams | CV2x.h | 读取与信道接收方向相关的值。例如，这可以是信道繁忙比率（**CBR**） |
| CV2x_SetBufCV2xPC5TxParams | CV2x.h | 为特定缓冲区（要发送的数据包）设置与发送方向相关的值。例如，这可以是属于单个数据包的 **PPPP** |
| Eth_GetControllerMode | Eth.h | 获取被索引控制器的通信状态 |
| Eth_GetCurrentTimeTuple | Eth.h | 在一个原子操作中读取时间戳时钟当前时间和 **PHC** 当前时间的时间元组。如果不支持 **PHC**，则 **PHC** 值将是时间戳时钟值的副本。 |
| Eth_GetPhcTime | Eth.h | 从 **PHC** 的 **HW** 寄存器中返回当前时间值。 |
| Eth_GetPhysAddr | Eth.h | 获取被索引控制器所使用的物理源地址 |
| Eth_ImmediateTransmit | EthIf.h | 请求发送一个以太网帧，其中每个上层将报头部分作为单链表的一个元素。所有报头与有效载荷一起构成一个完整的以太网帧 |
| Eth_ProvideTxBuffer | Eth.h | 提供对与指定优先级相关的队列的发送缓冲区的访问 |
| Eth_ReadMii | Eth.h | 读取收发器寄存器 |
| Eth_Receive | Eth.h | 从相关队列接收一帧。 |
| Eth_ReleaseRxBuffer | EthIf.h | 来自上层的指示，用于释放给定物理以太网控制器的接收缓冲区（入方向队列元素）。 |
| Eth_SetControllerMode | Eth.h | 启用/禁用被索引控制器的 **Rx/Tx** 通信 |
| Eth_SetPhcCorrection | Eth.h | 设置 **PHC** 参数以调整 **PHC** 的速率和偏移。 |
| Eth_SetPhcTime | Eth.h | 设置 **PHC** 的绝对时间。 |
| Eth_SetPpsSignalMode | Eth.h | 启用/禁用 **PPS** 信号的生成 |
| Eth_Transmit | Eth.h | 触发对之前已填充的发送缓冲区的发送 |
| Eth_TxConfirmation | Eth.h | 触发帧发送确认 |
| Eth_WriteMii | Eth.h | 配置收发器寄存器或触发收发器提供的功能 |
| EthSM_CtrlModeIndication | EthSM.h | 在模式被读取出来时调用。由之前的 [**EthIf_GetControllerMode**](#733-ethif_getcontrollermode) 或 [**EthIf_SetControllerMode**](#732-ethif_setcontrollermode) 调用触发。可以在触发函数内直接调用。 |
| EthSM_SleepIndication | EthSM.h | 此 **API** 由 **EthIf** 调用，指示在网络中检测到了睡眠指示。仅当 **ECU** 在相应通信通道上充当被动通信从属（受影响 **EthIfTr** 的被引用 **EthTrcv**…（源文档此处截断） |
| EthSM_TrcvLinkStateChg | EthSM.h | 此服务由以太网接口调用，用于报告收发器链路状态变化。 |
| EthSwt_ExtractStreamHandleIdx | EthSwt.h | 从网络数据包报头的交换机供应商特定部分提取 **StreamHandleIdx** |
| EthSwt_GetStreamHandleIdxStatistics | EthSwt.h | 向交换机请求桶计数器值 |
| EthSwt_PortEnableTimeStamp | EthSwt.h | 如果端口的 **EthSwtPortTimeStampSupport** 设置为 **TRUE**，则在交换机的专用端口上的专用报文对象上激活发送方向时间戳。对专用报文对象时间戳的选择性激活减少了通知调用的数量 |
| EthSwt_SetMgmtInfo | EthSwt.h | 使用管理信息扩展之前由 **EthSwt_EthTxPrepareFrame()** 准备的以太网帧，以实现仅在特定端口上的传输。 |
| EthSwt_SetStreamHandleIdxConfiguration | EthSwt.h | 此函数由 **EthIf** 模块调用，用于控制交换机中某个 **StreamHandleIdx** 的活动状态。 |
| EthTrcv_GetBaudRate | EthTrcv.h | 获取被索引收发器的波特率 |
| EthTrcv_GetDuplexMode | EthTrcv.h | 获取被索引收发器的双工模式 |
| EthTrcv_GetLinkState | EthTrcv.h | 获取被索引收发器的链路状态 |
| EthTrcv_GetTransceiverMode | EthTrcv.h | 获取被索引收发器的状态 |
| EthTrcv_SetTransceiverMode | EthTrcv.h | 启用/禁用被索引收发器 |
| EthTrcv_StartAutoNegotiation | EthTrcv.h | 重新启动被索引收发器所使用的传输参数的协商 |
| Fw_InspectPacket | Fw.h | 此函数根据预定义的防火墙规则列表检查网络数据包，并在 **InspectionResultPtr** 中返回检查结果。 |
| Fw_StreamHandleIdxConfiguration | Fw_Cbk.h | 一旦 **EthIf** 在交换机中成功设置了 **StreamHandleIdx**，就由 **EthIf** 调用该函数。 |
| Fw_StreamHandleIdxStatistics | Fw_Cbk.h | 一旦 **EthIf** 成功从交换机中获取了桶计数器值，就由 **EthIf** 调用该函数。 |
| IdsM_SetSecurityEvent | IdsM.h | 此 **API** 是向 **IdsM** 报告安全事件的应用程序接口。 |
| IdsM_SetSecurityEventWithContextData | IdsM.h | 此 **API** 是向 **IdsM** 报告带有上下文数据的安全事件的应用程序接口。 |
| WEth_GetBufWRxParams | WEth.h | 读出与所接收数据包接收方向相关的值。例如，这可以是属于单个数据包的 **RSSI** 或信道。此 **API** 仅在 **WEth_Receive** 的上下文内有效 |
| WEth_GetBufWTxParams | WEth.h | 读出与所发送数据包发送方向相关的值。此 **API** 仅在 **WEth_TxConfirmation** 的上下文内有效。 |
| WEth_SetBufWTxParams | WEth.h | 为特定缓冲区（要发送的数据包）设置与发送方向相关的值。例如，这可以是期望的发送功率或属于单个数据包的信道。 |
| WEthTrcv_GetChanRxParams | WEthTrcv.h | 读取与收发器接收方向相关的值。例如，这可以是信道繁忙比率（**CBR**）或平均信道空闲时间（**CIT**）。 |
| WEthTrcv_SetChanRxParams | WEthTrcv.h | 设置与收发器无线信道接收方向相关的值。例如，这可以是诸如频率之类的信道参数。 |
| WEthTrcv_SetChanTxParams | WEthTrcv.h | 设置与收发器无线信道发送方向相关的值。例如，这可以是信道的比特率。 |
| WEthTrcv_SetRadioParams | WEthTrcv.h | 设置与收发器无线射频相关的值。例如，这可以是射频设置（信道等）的选择。 |

#### 7.6.3. 可配置接口

在本节中，列出了目标函数可以配置的所有接口。目标函数通常是一个回调函数。此类接口的名称不是固定的，因为它们是可配置的。

##### 7.6.3.1. &lt;User&gt;_RxIndication

**说明**: 指示一个以太网帧的接收。本服务为同步调用，重入性无关（**Dont care**）。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 FrameType（in）：所接收以太网帧的帧类型。参数 IsBroadcast（in）：用于指示广播帧的参数。参数 PhysAddrPtr（in）：指向所接收以太网帧的物理源地址（网络字节序的 **MAC** 地址）的指针。参数 DataPtr（in）：指向所接收以太网帧有效载荷的指针（即不提供以太网报头）。参数 LenByte（in）：所接收数据的长度。该服务无返回值。可通过**configurable**获得。

```C
void <User>_RxIndication ( uint8 CtrlIdx, Eth_FrameType FrameType, boolean IsBroadcast, const uint8* PhysAddrPtr, const uint8* DataPtr, uint16 LenByte )
```

该回调函数应可通过配置参数 **EthIfRxIndicationFunction** 进行配置。

##### 7.6.3.2. &lt;UL&gt;_TxConfirmation

**说明**: 确认一个以太网帧的发送。本服务为同步调用，重入性无关（**Dont care**）。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 BufIdx（in）：缓冲区资源的索引。参数 Result（in）：-。该服务无返回值。可通过**configurable**获得。

```C
void <UL>_TxConfirmation ( uint8 CtrlIdx, Eth_BufIdxType BufIdx, Std_ReturnType Result )
```

该回调函数应可通过配置参数 **EthIfTxConfirmationFunction** 进行配置。

##### 7.6.3.3. &lt;User&gt;_TrcvLinkStateChg

**说明**: 指示收发器状态的变化。本服务为同步调用，重入性无关（**Don't care**）。参数 CtrlIdx（in）：以太网接口上下文中以太网控制器的索引。参数 TrcvLinkState（in）：**ETHTRCV_LINK_STATE_DOWN**：收发器链路断开；**ETHTRCV_LINK_STATE_ACTIVE**：收发器链路接通。该服务无返回值。可通过**configurable**获得。

```C
void <User>_TrcvLinkStateChg ( uint8 CtrlIdx, EthTrcv_LinkStateType TrcvLinkState )
```

该回调函数应可通过配置参数 **EthIfTrcvLinkStateChgFunction** 进行配置。

未引用以太网收发器的 [**EthIfController**](#924-ethifcontroller)，即未配置有效的 **EthIfEthTrcvRef** 或 **EthIfCanXLTrcvRef**，应表现得如同收发器存在且收发器状态为 **ETHTRCV_LINK_STATE_ACTIVE**。

在链路状态发生变化时，应为每个受影响的 [**EthIfController**](#924-ethifcontroller) 调用 **&lt;User&gt;_TrcvLinkStateChg**。

术语和定义：

可重入接口是可重入的。

无关（**Don't care**）：接口的重入性与本模块无关（一般来说，在这种情况下它不可重入）。

## 8. 时序图

时序图展示了运行期间执行的基本操作。它们展示了以太网接口与上层 **BSW** 模块以及底层以太网控制器驱动程序之间的交互。

请注意，时序图是为了便于理解本规范而提供的说明性扩展。

### 8.1. 初始化

![Figure9-1](Figure9-1.png)

### 8.2. 通信初始化

![Figure9-2](Figure9-2.png)

### 8.3. 交换机初始化

![Figure9-3](Figure9-3.png)

### 8.4. 数据发送

![Figure9-4](Figure9-4.png)

在每次调用 [**EthIf_MainFunctionTx**](#754-ethif_mainfunctiontx) 时，组件应为所有以太网控制器驱动程序调用 **&lt;EthDrv&gt;_TxConfirmation**。

注意：以太网接口期望每个以太网控制器驱动程序使用回调函数 [**EthIf_TxConfirmation**](#742-ethif_txconfirmation) 为所有已发送的帧发出确认。

[**EthIf_TxConfirmation**](#742-ethif_txconfirmation) 应将确认转发给已注册的回调函数 **&lt;User&gt;_TxConfirmation**。

![Figure9-5](Figure9-5.png)

### 8.5. 数据接收

![Figure9-6](Figure9-6.png)

![Figure9-7](Figure9-7.png)

### 8.6. 链路状态变化

![Figure9-8](Figure9-8.png)

### 8.7. 无端口组的链路状态变化

![Figure9-9](Figure9-9.png)

### 8.8. 带端口组的链路状态变化

![Figure9-10](Figure9-10.png)

### 8.9. 带端口组和部分网络集群的链路状态变化

![Figure9-11](Figure9-11.png)

### 8.10. 交换机管理支持

![Figure9-12](Figure9-12.png)

![Figure9-13](Figure9-13.png)

## 9. 配置规范

一般而言，本章定义配置参数及其到容器（**container**）中的聚类。为支持该规范，第 9.1 章描述了基础知识。它还规定了应用于参数规范的一个模板（表）。

第 9.2 章规定以太网接口模块的结构（容器）和参数。

第 9.3 章规定以太网接口模块的发布信息（**published information**）。

### 9.1. 如何阅读本章

详细信息请参阅 **SWS_BSWGeneral** [\[6\]](#ref-6) 的第 10.1 章「配置规范简介」（**Introduction to configuration specification**）。

### 9.2. 容器与配置参数

以下章节汇总了所有配置参数。参数的详细含义在第6章和第7章中描述。

以太网接口的概览如图10.1所示。

![Figure10-1](Figure10-1.png)

以太网接口通用配置结构如图10.2和图10.3所示。

![Figure10-2](Figure10-2.png)

![Figure10-3](Figure10-3.png)

以太网接口接口配置结构如图10.4和图10.5所示。

![Figure10-4](Figure10-4.png)

![Figure10-5](Figure10-5.png)

以太网接口交换机配置结构如图10.6所示。

![Figure10-6](Figure10-6.png)

以太网接口交换机端口组配置结构如图10.7所示。

![Figure10-7](Figure10-7.png)

以太网接口物理控制器配置结构如图10.8所示。

![Figure10-8](Figure10-8.png)

以太网接口收发器配置结构如图10.9所示。

![Figure10-9](Figure10-9.png)

以太网安全事件引用如图10.10所示。

![Figure10-10](Figure10-10.png)

#### 9.2.1. EthIf

| SWS 条目 | [ECUC_EthIf_00049] |
| --- | --- |
| 模块名称 | EthIf |
| 描述 | **EthIf**（以太网接口）模块的配置。 |
| 构建后变体支持 | true |
| 支持的配置变体 | VARIANT-LINK-TIME、VARIANT-POST-BUILD、VARIANT-PRE-COMPILE |

**包含的容器**

| 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- |
| EthIfConfigSet | 1 | 收集所有具有构建后配置类的参数的容器。 |
| EthIfGeneral | 1 | 此容器包含以太网接口的通用配置参数。 |

#### 9.2.2. EthIfGeneral

| SWS 条目 | [ECUC_EthIf_00001] |
| --- | --- |
| 容器名称 | EthIfGeneral |
| 父容器 | EthIf |
| 描述 | 此容器包含以太网接口的通用配置参数。 |

| SWS 条目 | [ECUC_EthIf_00004] |
| --- | --- |
| 参数名称 | EthIfDevErrorDetect |
| 父容器 | EthIfGeneral |
| 描述 | 打开或关闭开发错误检测和通知。* **true**：检测和通知已启用。* **false**：检测和通知已禁用。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00091] |
| --- | --- |
| 参数名称 | EthIfEnableCV2xApi |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **CV2x** 的 **API**。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00005] |
| --- | --- |
| 参数名称 | EthIfEnableRxInterrupt |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用接收中断。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00079] |
| --- | --- |
| 参数名称 | EthIfEnableSecurityEventReporting |
| 父容器 | EthIfGeneral |
| 描述 | 切换是否向 **IdsM** 报告安全事件：* **true**：报告已启用。* **false**：报告已禁用。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00076] |
| --- | --- |
| 参数名称 | EthIfEnableSignalQualityApi |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用读取和清除信号质量的 **API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00006] |
| --- | --- |
| 参数名称 | EthIfEnableTxInterrupt |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用发送中断。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00075] |
| --- | --- |
| 参数名称 | EthIfEnableWEthApi |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **WEth** / **WEthTrcv** 的 **API**。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00094] |
| --- | --- |
| 参数名称 | EthIfFwSupport |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用防火墙的使用。 |
| 多重性 | 1 |
| 类型 | EcucEnumerationParamDef |
| 取值范围 | **FIREWALL_WITHOUT_PERSTREAMFILTERING**：使用防火墙。网络数据包被转发到防火墙模块进行检查。**FIREWALL_WITH_PERSTREAMFILTERING**：在交换机核心中使用带有逐流过滤（**per stream filtering**）的防火墙。网络数据包将先被转发到 **EthSwt** 驱动程序以提取 **StreamHandleIdx**，然后再被转发到防火墙模块。**NO_FIREWALL**：不使用防火墙。 |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00072] |
| --- | --- |
| 参数名称 | EthIfGetAndResetMeasurementDataApi |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用获取并重置测量数据 **API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00034] |
| --- | --- |
| 参数名称 | EthIfGetBaudRate |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **GetBaudRate API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00035] |
| --- | --- |
| 参数名称 | EthIfGetCounterState |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **GetCounterState API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00070] |
| --- | --- |
| 参数名称 | EthIfGetCtrlIdxList |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **GetCtrlIdxList API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00071] |
| --- | --- |
| 参数名称 | EthIfGetVlanIdSupport |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **GetVlanId API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00039] |
| --- | --- |
| 参数名称 | EthIfGlobalTimeSupport |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用以太网全局时间同步等所使用的全局时间 **API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00023] |
| --- | --- |
| 参数名称 | EthIfMainFunctionPeriod |
| 父容器 | EthIfGeneral |
| 描述 | 以秒为单位指定主函数 **EthIf_MainFunctionRx** 和 **EthIf_MainFunctionTx** 的周期。以太网接口不需要此信息，但 **BSW** 调度器需要。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | ]0 .. INF[ |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00056] |
| --- | --- |
| 参数名称 | EthIfMainFunctionStatePeriod |
| 父容器 | EthIfGeneral |
| 描述 | 以秒为单位指定主函数 **EthIf_MainFunctionState** 的周期。以太网接口不需要此信息，但 **BSW** 调度器需要。 |
| 多重性 | 0..1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | ]0 .. INF[ |
| 默认值 | - |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local 依赖：如果定义了此参数，则应生成 **EthIf_MainFunctionState**。 |

| SWS 条目 | [ECUC_EthIf_00003] |
| --- | --- |
| 参数名称 | EthIfMaxTrcvsTotal |
| 父容器 | EthIfGeneral |
| 描述 | 限制收发器的总数。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 1 .. 255 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00102] |
| --- | --- |
| 参数名称 | EthIfPhcSupport |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **PTP** 硬件时钟（**PHC**）。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00055] |
| --- | --- |
| 参数名称 | EthIfPortStartupActiveTime |
| 父容器 | EthIfGeneral |
| 描述 | 表示通过 **EthIf_StartAllPorts** 请求所有 **EthIfSwitchPort** 的「**ETH_MODE_ACTIVE**」模式之后的时间延迟。这仅用于未被任何 **EthIfController** 引用的 **EthIfSwtPortGroup** 中的端口。 |
| 多重性 | 0..1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0.001 .. 65.535] |
| 默认值 | - |
| 构建后变体多重性 | true |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME、VARIANT-POST-BUILD）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00024] |
| --- | --- |
| 参数名称 | EthIfPublicCddHeaderFile |
| 父容器 | EthIfGeneral |
| 描述 | 定义在 **CDD** 情况下应包含的回调函数头文件。字符范围为 1..32。 |
| 多重性 | 0..* |
| 类型 | EcucStringParamDef |
| 默认值 | - |
| 长度 | 1-32 |
| 正则表达式 | - |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00030] |
| --- | --- |
| 参数名称 | EthIfRxIndicationIterations |
| 父容器 | EthIfGeneral |
| 描述 | 在 **EthIf_MainFunctionRx** 内从以太网驱动程序轮询的每个以太网控制器的最大以太网帧数。 |
| 多重性 | 0..1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 65535 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00062] |
| --- | --- |
| 参数名称 | EthIfSetForwardingModeApi |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **EthIf_SetForwardingMode API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00077] |
| --- | --- |
| 参数名称 | EthIfSignalQualityCheckPeriod |
| 父容器 | EthIfGeneral |
| 描述 | 以秒为单位指定在 **EthIf_MainFunctionState** 上下文中轮询信号质量的周期。该值应为 **EthIfMainFunctionStatePeriod** 的整数倍。 |
| 多重性 | 0..1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [-INF .. INF] |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local 依赖：如果定义了此参数，则应生成 **EthIf_MainFunctionState**，且参数 **EthIfEnableSignalQualityApi** 应设置为 **TRUE**。 |

| SWS 条目 | [ECUC_EthIf_00033] |
| --- | --- |
| 参数名称 | EthIfStartAutoNegotiation |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **StartAutoNegotiation API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00064] |
| --- | --- |
| 参数名称 | EthIfSwitchManagementSupport |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用交换机管理 **API**，以支持交换机端口特定的通信属性访问。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00054] |
| --- | --- |
| 参数名称 | EthIfSwitchOffPortTimeDelay |
| 父容器 | EthIfGeneral |
| 描述 | 表示 **EthIfSwitchPortGroup** 的「**ETH_MODE_DOWN**」模式将被执行之后的时间延迟。这仅用于未被任何 **EthIfController** 引用的 **EthIfSwtPortGroup**。该时间延迟应大于 **UdpNm** 的时序，因为 **UdpNm** 需要完成其关闭处理（重复报文状态、准备总线睡眠状态、总线睡眠…（源文档此处截断））。 |
| 多重性 | 0..1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0.001 .. 65.535] |
| 默认值 | - |
| 构建后变体多重性 | true |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME、VARIANT-POST-BUILD）；Post-build time：- |
| 作用域/依赖 | scope: local 依赖：EthIfSwitchOffPortTimeDelay > (UdpNmTimeoutTime + UdpNmWaitBusSleepTime) |

| SWS 条目 | [ECUC_EthIf_00009] |
| --- | --- |
| 参数名称 | EthIfTrcvLinkStateChgMainReload |
| 父容器 | EthIfGeneral |
| 描述 | 指定在主函数 **EthIf_MainFunctionTx** 的每个周期内收发器链路状态变化检查的频率。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 1 .. 255 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00063] |
| --- | --- |
| 参数名称 | EthIfVerifyConfigApi |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用 **EthIf_VerifyConfig API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00007] |
| --- | --- |
| 参数名称 | EthIfVersionInfoApi |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用版本信息 **API**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00008] |
| --- | --- |
| 参数名称 | EthIfVersionInfoApiMacro |
| 父容器 | EthIfGeneral |
| 描述 | 启用/禁用版本信息 **API** 的宏实现。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00040] |
| --- | --- |
| 参数名称 | EthIfWakeUpSupport |
| 父容器 | EthIfGeneral |
| 描述 | 配置是否支持唤醒处理：**TRUE**：支持唤醒处理；**FALSE**：不支持唤醒处理。此配置参数还在编译前（**Pre-Compile-Time**）启用其他特定的 **API**，例如 **EthIf_CheckWakeup**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

**包含的容器**

| 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- |
| EthIfSecurityEventRefs | 0..1 | 引用 **IdsMEvent** 元素的容器，这些元素表示当相应安全相关事件发生时（且 **EthIfEnableSecurityEventReporting** 设置为「true」时），**EthIf** 模块应向 **IdsM** 报告的安全事件。此容器中的标准化安全事件可以通过供应商特定的安全事件进行扩展。 |

#### 9.2.3. EthIfConfigSet

| SWS 条目 | [ECUC_EthIf_00010] |
| --- | --- |
| 容器名称 | EthIfConfigSet |
| 父容器 | EthIf |
| 描述 | 收集所有具有构建后配置类的参数的容器。 |

**包含的容器**

| 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- |
| EthIfController | 1..* | 此容器包含 **EthIfController** 的配置。 |
| EthIfFrameOwnerConfig | 1..* | 以太网帧所有者的配置。 |
| EthIfPhysController | 1..* | 此容器包含 **EthIfPhysController** 的配置。**EthIfEthCtrlRef**、**EthIfCanXLCtrlRef**、**EthIfWEthCtrlRef** 和 **EthIfCV2xCtrlRef** 的使用是互斥的。 |
| EthIfRxIndicationConfig | 1..* | 接收回调函数的配置。 |
| EthIfSwitch | 0..* | 此容器包含 **EthIfSwitch** 的配置。 |
| EthIfSwitchPortGroup | 0..* | 此容器包含 **EthIfSwitchPortGroup** 的配置。如果 **EthIfSwitchPortGroup** 由 **PNC** 控制，则每个 **PNC** 应存在一个 **EthIfSwitchPortGroup**。主机端口应是所有 **EthIfSwitchPortGroup** 的一部分。主交换机的上行端口和从交换机的上行端口应是所有包含属于从交换机的 **EthSwtPort** 的 **EthIfSwitchPortGroup** 的一部分。 |
| EthIfTransceiver | 0..* | 此容器包含 **EthIfTransceiver** 的配置。**EthIfEthTrcvRef**、**EthIfCanXLTrcvRef** 和 **EthIfWEthTrcvRef** 的使用是互斥的。 |
| EthIfTrcvLinkStateChgConfig | 1..* | 指定链路状态变化回调函数。 |
| EthIfTxConfirmationConfig | 0..* | 发送指示回调函数的配置。 |

#### 9.2.4. EthIfController

| SWS 条目 | [ECUC_EthIf_00025] |
| --- | --- |
| 容器名称 | EthIfController |
| 父容器 | EthIfConfigSet |
| 描述 | 此容器包含 **EthIfController** 的配置。 |

| SWS 条目 | [ECUC_EthIf_00026] |
| --- | --- |
| 参数名称 | EthIfCtrlIdx |
| 父容器 | EthIfController |
| 描述 | 此参数提供以太网通信控制器的从零开始的连续索引。上层 **BSW** 模块和 **EthIf** 自身使用此索引来标识以太网通信控制器。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为此参数生成符号名称） |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU withAuto = true |

| SWS 条目 | [ECUC_EthIf_00032] |
| --- | --- |
| 参数名称 | EthIfCtrlMtu |
| 父容器 | EthIfController |
| 描述 | 以字节为单位指定 **EthIfCtrl** 的最大传输单元（**MTU**）。注意：如果 **EthIfCtrl** 使用 **VLAN** 标签，以太网帧的帧长度将增加 4 字节。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 64 .. 9000 |
| 默认值 | - |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU 依赖：1) **EthIfVlanId**。2) 如果 **EthIfController.EthIfMacSecSupport** 设置为 **HW_MACSEC** 或 **SW_MACSEC**，则 **MTU** 将需要适当调整 **MTU** 大小（**MTU** 大小必须减少 24 字节，以避免数据包具有更大的尺寸…（源文档此处截断））。 |

| SWS 条目 | [ECUC_EthIf_00089] |
| --- | --- |
| 参数名称 | EthIfMacSecSupport |
| 父容器 | EthIfController |
| 描述 | 以太网接口控制器的 **MACsec** 支持。 |
| 多重性 | 0..1 |
| 类型 | EcucEnumerationParamDef |
| 取值范围 | **HW_MACSEC**：-；**NO_MACSEC**：-；**SW_MACSEC**：- |
| 默认值 | NO_MACSEC |
| 构建后变体多重性 | true |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00002] |
| --- | --- |
| 参数名称 | EthIfMaxTxBufsTotal |
| 父容器 | EthIfController |
| 描述 | 限制发送缓冲区的总数。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 1 .. 4294967295 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00029] |
| --- | --- |
| 参数名称 | EthIfVlanId |
| 父容器 | EthIfController |
| 描述 | 虚拟 **LAN** 根据此属性按照 IEEE 802.1Q 进行标识。 |
| 多重性 | 0..1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 4095 |
| 默认值 | - |
| 构建后变体多重性 | true |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00028] |
| --- | --- |
| 参数名称 | EthIfEthTrcvRef |
| 父容器 | EthIfController |
| 描述 | 对由以太网接口处理的以太网收发器的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 EthIfTransceiver 的符号名引用 |
| 构建后变体多重性 | true |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00090] |
| --- | --- |
| 参数名称 | EthIfPaeInstanceRef |
| 父容器 | EthIfController |
| 描述 | 对 **MkaPaeInstance** 的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 MkaPaeInstance 的符号名引用 |
| 构建后变体多重性 | true |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00027] |
| --- | --- |
| 参数名称 | EthIfPhysControllerRef |
| 父容器 | EthIfController |
| 描述 | 对由以太网接口处理的物理以太网控制器的引用。 |
| 多重性 | 1 |
| 类型 | 对 EthIfPhysController 的符号名引用 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU 依赖：如果为某个 **EthIfController** 配置了 **EthIfEthTrcvRef**，则所有通过 **EthIfPhysControllerRef** 引用同一物理控制器的 **EthIfController** 都应通过 **EthIfEthTrcvRef** 引用同一个 **EthIfTrcv**。 |

| SWS 条目 | [ECUC_EthIf_00048] |
| --- | --- |
| 参数名称 | EthIfSwitchRefOrPortGroupRef |
| 父容器 | EthIfController |
| 描述 | 该选择引用允许配置 **EthIfController** 是引用 **EthIfSwitch** 还是 **EthIfSwitchPortGroup**。如果 **EthIfSwitchPortGroup** 由 **BswM** 控制（例如根据特定的 **PNC** 请求），则 **EthIfSwitchPortGroupRefSemantics** 应具有值 **ETHIF_SWITCH_PORT_GROUP_LINK_INFO**。如果 **EthIfSwitchPortGroup** 由 **EthIfController** 控制，则 **EthIfSwitchPortGroupRefSemantics** 应具有值 **ETHIF_SWITCH_PORT_GROUP_CONTROL**。 |
| 多重性 | 0..1 |
| 类型 | 对 [ EthIfSwitch, EthIfSwitchPortGroup ] 的选择引用 |
| 构建后变体多重性 | true |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local 依赖：* 仅当此 **EthIfController** 未配置 **EthIfEthTrcvRef** 时，**EthIfSwitchRefOrPortGroupRef** 的配置才有效。* 如果配置了 **EthIfSwitchPortGroup**，则所有引用同一 **EthIfPhysController** 的 **EthIfController** 都应引用一个 **EthIfSwitchPortGroup**。* 如果配置了 **EthIfSwitchPortGroup**，则还应根据相应的 **EthSwtConfig** 配置 **EthIfSwitch**。这些 **EthIfSwitch** 不应被任何 **EthIfController** 引用。（请注意：**EthIfSwitch** 用于在相应 **API** 调用的上下文中提供相应的 **EthIfSwitchIdx**…（源文档此处截断）） |

#### 9.2.5. EthIfFrameOwnerConfig

| SWS 条目 | [ECUC_EthIf_00011] |
| --- | --- |
| 容器名称 | EthIfFrameOwnerConfig |
| 父容器 | EthIfConfigSet |
| 描述 | 以太网帧所有者的配置。 |

| SWS 条目 | [ECUC_EthIf_00012] |
| --- | --- |
| 参数名称 | EthIfFrameType |
| 父容器 | EthIfFrameOwnerConfig |
| 描述 | 选择以太网帧类型。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 65535 |
| 默认值 | - |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00013] |
| --- | --- |
| 参数名称 | EthIfOwner |
| 父容器 | EthIfFrameOwnerConfig |
| 描述 | 选择以太网帧类型的所有者。所有者是基于零的、指向回调函数配置「**EthIfRxIndicationConfig**」的索引。即索引 0 处的 **IPv4**（0x800）类型的以太网帧将调用「**EthIfRxIndicationConfig**」中配置的第一个回调函数。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

**包含的容器**

| 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- |
| EthIfFrameOwnerPdu | 0..* | 此容器可选地定义表示供上层模块使用的特定 **EthIfFrameType PDU** 的 **EcuC PDU**。可以基于以下标准定义多个容器实例：* **Tx** 和 **Rx PDU** 定义 * 可选的不同的 **EthIfPhysController** 关系。仅当上层模块使用基于 **PDU** 的 **API**（例如 **LSduR**）时才需要此定义。 |

##### 9.2.5.1. EthIfFrameOwnerPdu

| SWS 条目 | [ECUC_EthIf_00095] |
| --- | --- |
| 容器名称 | EthIfFrameOwnerPdu |
| 父容器 | EthIfFrameOwnerConfig |
| 描述 | 此容器可选地定义表示供上层模块使用的特定 **EthIfFrameType PDU** 的 **EcuC PDU**。可以基于以下标准定义多个容器实例：* **Tx** 和 **Rx PDU** 定义 * 可选的不同的 **EthIfPhysController** 关系。仅当上层模块使用基于 **PDU** 的 **API**（例如 **LSduR**）时才需要此定义。 |
| 构建后变体多重性 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |

| SWS 条目 | [ECUC_EthIf_00099] |
| --- | --- |
| 参数名称 | EthIfFrameOwnerPduDirection |
| 父容器 | EthIfFrameOwnerPdu |
| 描述 | 定义 **PDU** 是被接收还是被发送。 |
| 多重性 | 1 |
| 类型 | EcucEnumerationParamDef |
| 取值范围 | **RX**：使用定义的 **EthIfFrameType** 接收帧，并作为 **PDU** 转发给上层。**TX**：**PDU** 由上层移交，并作为具有定义的 **EthIfFrameType** 的帧发送。 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00100] |
| --- | --- |
| 参数名称 | EthIfFrameOwnerTxPriority |
| 父容器 | EthIfFrameOwnerPdu |
| 描述 | 定义用于发送的 **VLAN** 优先级。 |
| 多重性 | 0..1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 7 |
| 默认值 | - |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00101] |
| --- | --- |
| 参数名称 | EthIfFrameOwnerControllerRef |
| 父容器 | EthIfFrameOwnerPdu |
| 描述 | 对 **EthIfController** 的可选引用。如果定义了此引用，则只有到/来自该 **EthIfController** 的报文才会分配给该 **PDU**。通过此设置，可以为专用的 **EtherType** 定义 **VLAN** 特定的 **PDU**。 |
| 多重性 | 0..1 |
| 类型 | 对 EthIfController 的引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

**包含的容器**

| 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- |
| EthIfFrameOwnerPduPoolEntry | 0..* | 该容器定义 **EthIfFrameOwnerPdu** 的 **PDU** 池中用于传输专用 **EthIfFrameOwnerPdu** 帧的一个条目。支持的 **Rx** 元数据条目：* **TIMETUPLE_TYPE_PTR**。支持的 **Tx** 元数据条目：* **ETHERNET_MAC_64** * **TIMETUPLE_TYPE_PTR** * **LISTELEM_PTR**。 |

###### 9.2.5.1.1. EthIfFrameOwnerPduPoolEntry

| SWS 条目 | [ECUC_EthIf_00096] |
| --- | --- |
| 容器名称 | EthIfFrameOwnerPduPoolEntry |
| 父容器 | EthIfFrameOwnerPdu |
| 描述 | 该容器定义 **EthIfFrameOwnerPdu** 的 **PDU** 池中用于传输专用 **EthIfFrameOwnerPdu** 帧的一个条目。支持的 **Rx** 元数据条目：* **TIMETUPLE_TYPE_PTR**。支持的 **Tx** 元数据条目：* **ETHERNET_MAC_64** * **TIMETUPLE_TYPE_PTR** * **LISTELEM_PTR**。 |
| 构建后变体多重性 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |

| SWS 条目 | [ECUC_EthIf_00098] |
| --- | --- |
| 参数名称 | EthIfFrameOwnerPduId |
| 父容器 | EthIfFrameOwnerPduPoolEntry |
| 描述 | 定义表示上层模块的句柄 **PDU ID**。 |
| 多重性 | 0..1 |
| 类型 | EcucIntegerParamDef（为此参数生成符号名称） |
| 取值范围 | 0 .. 65535 |
| 默认值 | - |
| 构建后变体多重性 | false |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00097] |
| --- | --- |
| 参数名称 | EthIfFrameOwnerPduRef |
| 父容器 | EthIfFrameOwnerPduPoolEntry |
| 描述 | 对表示供上层模块使用的特定 **EthIfFrameType PDU** 的 **EcuC PDU** 的引用。 |
| 多重性 | 1 |
| 类型 | 对 Pdu 的引用 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

#### 9.2.6. EthIfPhysController

| SWS 条目 | [ECUC_EthIf_00045] |
| --- | --- |
| 容器名称 | EthIfPhysController |
| 父容器 | EthIfConfigSet |
| 描述 | 此容器包含 **EthIfPhysController** 的配置。**EthIfEthCtrlRef**、**EthIfCanXLCtrlRef**、**EthIfWEthCtrlRef** 和 **EthIfCV2xCtrlRef** 的使用是互斥的。 |
| 构建后变体多重性 | false |

| SWS 条目 | [ECUC_EthIf_00046] |
| --- | --- |
| 参数名称 | EthIfPhysControllerIdx |
| 父容器 | EthIfPhysController |
| 描述 | 此参数提供物理以太网控制器的从零开始的连续索引。上层 **BSW** 模块和以太网接口自身使用此索引来标识物理以太网控制器。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为此参数生成符号名称） |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU withAuto = true |

| SWS 条目 | [ECUC_EthIf_00085] |
| --- | --- |
| 参数名称 | EthIfCanXLCtrlRef |
| 父容器 | EthIfPhysController |
| 描述 | 对由特定 **CAN XL** 驱动程序处理的物理 **CAN XL** 控制器的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 CanController 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU 依赖：被引用的 **CanController** 必须包含一个 **CanXLController**。 |

| SWS 条目 | [ECUC_EthIf_00093] |
| --- | --- |
| 参数名称 | EthIfCV2xCtrlRef |
| 父容器 | EthIfPhysController |
| 描述 | 对由特定蜂窝 **V2X** 控制器驱动程序处理的物理蜂窝 **V2X** 控制器的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 CV2xCtrlConfig 的符号名引用 |
| 构建后变体多重性 | true |
| 构建后变体值 | true |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00047] |
| --- | --- |
| 参数名称 | EthIfEthCtrlRef |
| 父容器 | EthIfPhysController |
| 描述 | 对由特定以太网控制器驱动程序处理的物理以太网控制器的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 EthCtrlConfig 的符号名引用 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00073] |
| --- | --- |
| 参数名称 | EthIfWEthCtrlRef |
| 父容器 | EthIfPhysController |
| 描述 | 对由特定无线以太网控制器驱动程序处理的物理无线以太网控制器的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 WEthCtrlConfig 的符号名引用 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

**包含的容器**

| 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- |
| EthIfClkUnit | 0..* | 此容器包含以太网控制器中 **HW** 时钟单元的配置。 |
| EthIfPhysCtrlRxMainFunctionIngressQueueProcessing | 0..* | 该函数在相关以太网控制器及通过 **EthIfPhysCtrlRxIngressQueueRef** 引用的相关入方向队列处，或在相关 **CanXL** 控制器及通过 **EthIfCanXLCtrlRxIngressFifoRef** 引用的相关入方向 **FIFO** 处，检查新接收的以太网帧。对于以太网控制器，使用相应的 **QueueIdx** 调用 **Eth_Receive()**。对于 **CanXL** 控制器，使用相应的 **FifoIdx** 调用 **CanXL_Receive()**。 |

#### 9.2.7. EthIfPhysCtrlRxMainFunctionIngressQueueProcessing

| SWS 条目 | [ECUC_EthIf_00106] |
| --- | --- |
| 容器名称 | EthIfPhysCtrlRxMainFunctionIngressQueueProcessing |
| 父容器 | EthIfPhysController |
| 描述 | 该函数在相关以太网控制器及通过 **EthIfPhysCtrlRxIngressQueueRef** 引用的相关入方向队列处，或在相关 **CanXL** 控制器及通过 **EthIfCanXLCtrlRxIngressFifoRef** 引用的相关入方向 **FIFO** 处，检查新接收的以太网帧。对于以太网控制器，使用相应的 **QueueIdx** 调用 **Eth_Receive()**。对于 **CanXL** 控制器，使用相应的 **FifoIdx** 调用 **CanXL_Receive()**。 |
| 构建后变体多重性 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |

| SWS 条目 | [ECUC_EthIf_00052] |
| --- | --- |
| 参数名称 | EthIfPhysCtrlRxIndicationIterations |
| 父容器 | EthIfPhysCtrlRxMainFunctionIngressQueueProcessing |
| 描述 | 每次主函数调用轮询的最大以太网帧数。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 18446744073709551615 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00051] |
| --- | --- |
| 参数名称 | EthIfPhysCtrlRxMainFunctionPeriod |
| 父容器 | EthIfPhysCtrlRxMainFunctionIngressQueueProcessing |
| 描述 | 以秒为单位指定主函数的周期。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [-INF .. INF] |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00087] |
| --- | --- |
| 参数名称 | EthIfCanXLCtrlRxIngressFifoRef |
| 父容器 | EthIfPhysCtrlRxMainFunctionIngressQueueProcessing |
| 描述 | 对接收 **FIFO** 的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 CanXLEthIngressFifo 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local 依赖：与 **EthIfPhysCtrlRxIngressQueueRef** 互斥。两个参数中必须提供一个。 |

| SWS 条目 | [ECUC_EthIf_00053]（废弃） |
| --- | --- |
| 参数名称 | EthIfPhysCtrlRxIngressFifoRef |
| 父容器 | EthIfPhysCtrlRxMainFunctionIngressQueueProcessing |
| 描述 | 对接收 **FIFO** 的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 EthCtrlConfigIngressFifo 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local 依赖：与 **EthIfCanXLCtrlRxIngressFifoRef** 互斥。两个参数中必须提供一个。 |

| SWS 条目 | [ECUC_EthIf_00107] |
| --- | --- |
| 参数名称 | EthIfPhysCtrlRxIngressQueueRef |
| 父容器 | EthIfPhysCtrlRxMainFunctionIngressQueueProcessing |
| 描述 | 对入方向队列的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 EthCtrlConfigIngressQueue 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local 依赖：与 **EthIfCanXLCtrlRxIngressFifoRef** 互斥。两个参数中必须提供一个。 |

#### 9.2.8. EthIfClkUnit

| SWS 条目 | [ECUC_EthIf_00105] |
| --- | --- |
| 容器名称 | EthIfClkUnit |
| 父容器 | EthIfPhysController |
| 描述 | 此容器包含以太网控制器中 **HW** 时钟单元的配置。 |
| 构建后变体多重性 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |

| SWS 条目 | [ECUC_EthIf_00104] |
| --- | --- |
| 参数名称 | EthIfClkUnitIdx |
| 父容器 | EthIfClkUnit |
| 描述 | 以太网控制器中 **HW** 时钟单元的从零开始的连续索引。上层 **BSW** 模块和 **Eth** 自身使用此索引来标识以太网控制器中的时钟。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为此参数生成符号名称） |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00103] |
| --- | --- |
| 参数名称 | EthIfClkUnitRef |
| 父容器 | EthIfClkUnit |
| 描述 | 对以太网控制器提供的、用于帧的接收/发送方向时间戳并可选地用于跟随 **PTP** 时间的 **HW** 时钟单元的引用。 |
| 多重性 | 1 |
| 类型 | 对 EthClkUnit 的符号名引用 |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

#### 9.2.9. EthIfRxIndicationConfig

| SWS 条目 | [ECUC_EthIf_00014] |
| --- | --- |
| 容器名称 | EthIfRxIndicationConfig |
| 父容器 | EthIfConfigSet |
| 描述 | 接收回调函数的配置。 |

| SWS 条目 | [ECUC_EthIf_00015] |
| --- | --- |
| 参数名称 | EthIfRxIndicationFunction |
| 父容器 | EthIfRxIndicationConfig |
| 描述 | 指定接收指示回调函数。 |
| 多重性 | 1 |
| 类型 | EcucFunctionNameDef |
| 默认值 | - |
| 正则表达式 | - |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

#### 9.2.10. EthIfSwitch

| SWS 条目 | [ECUC_EthIf_00036] |
| --- | --- |
| 容器名称 | EthIfSwitch |
| 父容器 | EthIfConfigSet |
| 描述 | 此容器包含 **EthIfSwitch** 的配置。 |

| SWS 条目 | [ECUC_EthIf_00037] |
| --- | --- |
| 参数名称 | EthIfSwitchIdx |
| 父容器 | EthIfSwitch |
| 描述 | 此参数提供以太网接口交换机的从零开始的连续索引。上层 **BSW** 模块和 **EthIf** 自身使用此索引来标识以太网交换机。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为此参数生成符号名称） |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00038] |
| --- | --- |
| 参数名称 | EthIfSwitchRef |
| 父容器 | EthIfSwitch |
| 描述 | 对由特定以太网交换机驱动程序处理的以太网交换机的引用。 |
| 多重性 | 1 |
| 类型 | 对 EthSwtConfig 的符号名引用 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

#### 9.2.11. EthIfSwitchPortGroup

| SWS 条目 | [ECUC_EthIf_00057] |
| --- | --- |
| 容器名称 | EthIfSwitchPortGroup |
| 父容器 | EthIfConfigSet |
| 描述 | 此容器包含 **EthIfSwitchPortGroup** 的配置。如果 **EthIfSwitchPortGroup** 由 **PNC** 控制，则每个 **PNC** 应存在一个 **EthIfSwitchPortGroup**。主机端口应是所有 **EthIfSwitchPortGroup** 的一部分。主交换机的上行端口和从交换机的上行端口应是所有包含属于从交换机的 **EthSwtPort** 的 **EthIfSwitchPortGroup** 的一部分。 |

| SWS 条目 | [ECUC_EthIf_00058] |
| --- | --- |
| 参数名称 | EthIfSwitchPortGroupIdx |
| 父容器 | EthIfSwitchPortGroup |
| 描述 | 此参数提供以太网交换机端口组的从零开始的连续索引。上层 **BSW** 模块和 **EthIf** 自身使用此索引来标识以太网交换机端口组。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为此参数生成符号名称） |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00059] |
| --- | --- |
| 参数名称 | EthIfSwitchPortGroupRefSemantics |
| 父容器 | EthIfSwitchPortGroup |
| 描述 | 定义指向 **EthIfSwitchPortGroup** 的 **EthIfSwitchRefOrPortGroupRef** 应如何解释。 |
| 多重性 | 0..1 |
| 类型 | EcucEnumerationParamDef |
| 取值范围 | **ETHIF_SWITCH_PORT_GROUP_CONTROL**：用于该组中的所有端口都由 **EthIfController** 控制的情况。**ETHIF_SWITCH_PORT_GROUP_LINK_INFO**：用于该组中的所有端口都通过 **EthIf_SwitchPortGroupRequestMode** 控制的情况。 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local 依赖：仅当 **EthIfSwitchRefOrPortGroupRef** 指向 **EthIfSwitchPortGroup** 时有效。 |

| SWS 条目 | [ECUC_EthIf_00060] |
| --- | --- |
| 参数名称 | EthIfPortRef |
| 父容器 | EthIfSwitchPortGroup |
| 描述 | 对以太网交换机端口的引用。 |
| 多重性 | 1..* |
| 类型 | 对 EthSwtPort 的符号名引用 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

#### 9.2.12. EthIfTransceiver

| SWS 条目 | [ECUC_EthIf_00042] |
| --- | --- |
| 容器名称 | EthIfTransceiver |
| 父容器 | EthIfConfigSet |
| 描述 | 此容器包含 **EthIfTransceiver** 的配置。**EthIfEthTrcvRef**、**EthIfCanXLTrcvRef** 和 **EthIfWEthTrcvRef** 的使用是互斥的。 |
| 构建后变体多重性 | false |

| SWS 条目 | [ECUC_EthIf_00078] |
| --- | --- |
| 参数名称 | EthIfQualifiedUnexpectedLinkDownTime |
| 父容器 | EthIfTransceiver |
| 描述 | 以秒为单位指定意外链路断开的判定时间。此参数仅用于 **ECU** 充当被动通信从属的以太网通道（被引用的 **EthTrcv** 设置 **EthTrcvActAsSlavePassiveEnabled** = **TRUE**）。该值应为 **EthIf_MainFunctionState** 的整数倍。 |
| 多重性 | 0..1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | ]0 .. INF[ |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU 依赖：1) 如果设置了此参数，**EthIf_MainFunctionState** 必须可用。2) 仅适用于被引用的 **EthTrcv** 设置了 **EthTrcvActAsSlavePassive** 的情况…（源文档此处截断）。 |

| SWS 条目 | [ECUC_EthIf_00043] |
| --- | --- |
| 参数名称 | EthIfTransceiverIdx |
| 父容器 | EthIfTransceiver |
| 描述 | 此参数提供以太网收发器的从零开始的连续索引。上层 **BSW** 模块和以太网接口自身使用此索引来标识以太网收发器。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为此参数生成符号名称） |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| 构建后变体值 | false |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00086] |
| --- | --- |
| 参数名称 | EthIfCanXLTrcvRef |
| 父容器 | EthIfTransceiver |
| 描述 | 对由特定 **CAN XL** 收发器驱动程序处理的 **CAN XL** 收发器的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 CanTrcvChannel 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU 依赖：被引用的 **CanTrcvChannel** 必须包含一个 **CanTrcvXLChannel**。 |

| SWS 条目 | [ECUC_EthIf_00044] |
| --- | --- |
| 参数名称 | EthIfEthTrcvRef |
| 父容器 | EthIfTransceiver |
| 描述 | 对由特定以太网收发器驱动程序处理的以太网收发器的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 EthTrcvConfig 的符号名引用 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_EthIf_00074] |
| --- | --- |
| 参数名称 | EthIfWEthTrcvRef |
| 父容器 | EthIfTransceiver |
| 描述 | 对由特定无线以太网收发器驱动程序处理的无线以太网收发器的引用。 |
| 多重性 | 0..1 |
| 类型 | 对 WEthTrcvConfig 的符号名引用 |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: ECU |

#### 9.2.13. EthIfTrcvLinkStateChgConfig

| SWS 条目 | [ECUC_EthIf_00018] |
| --- | --- |
| 容器名称 | EthIfTrcvLinkStateChgConfig |
| 父容器 | EthIfConfigSet |
| 描述 | 指定链路状态变化回调函数。 |

| SWS 条目 | [ECUC_EthIf_00019] |
| --- | --- |
| 参数名称 | EthIfTrcvLinkStateChgFunction |
| 父容器 | EthIfTrcvLinkStateChgConfig |
| 描述 | 指定链路状态变化回调函数。 |
| 多重性 | 1 |
| 类型 | EcucFunctionNameDef |
| 默认值 | - |
| 正则表达式 | - |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

#### 9.2.14. EthIfTxConfirmationConfig

| SWS 条目 | [ECUC_EthIf_00016] |
| --- | --- |
| 容器名称 | EthIfTxConfirmationConfig |
| 父容器 | EthIfConfigSet |
| 描述 | 发送指示回调函数的配置。 |

| SWS 条目 | [ECUC_EthIf_00017] |
| --- | --- |
| 参数名称 | EthIfTxConfirmationFunction |
| 父容器 | EthIfTxConfirmationConfig |
| 描述 | 指定发送指示回调函数。 |
| 多重性 | 1 |
| 类型 | EcucFunctionNameDef |
| 默认值 | - |
| 正则表达式 | - |
| 构建后变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：X（VARIANT-POST-BUILD） |
| 作用域/依赖 | scope: local |

#### 9.2.15. EthIfSecurityEventRefs

| SWS 条目 | [ECUC_EthIf_00080] |
| --- | --- |
| 容器名称 | EthIfSecurityEventRefs |
| 父容器 | EthIfGeneral |
| 描述 | 引用 **IdsMEvent** 元素的容器，这些元素表示当相应安全相关事件发生时（且 **EthIfEnableSecurityEventReporting** 设置为「true」时），**EthIf** 模块应向 **IdsM** 报告的安全事件。此容器中的标准化安全事件可以通过供应商特定的安全事件进行扩展。 |
| 构建后变体多重性 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |

| SWS 条目 | [ECUC_EthIf_00083] |
| --- | --- |
| 参数名称 | SEV_ETH_DROP_INV_VLAN |
| 父容器 | EthIfSecurityEventRefs |
| 描述 | 由于无效的控制器索引/**VLAN** 而丢弃了以太网数据报。 |
| 多重性 | 0..1 |
| 类型 | 对 IdsMEvent 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00084] |
| --- | --- |
| 参数名称 | SEV_ETH_DROP_MAC_COLLISION |
| 父容器 | EthIfSecurityEventRefs |
| 描述 | 由于本地 **MAC** 与传入帧中的源 **MAC** 相同而丢弃了以太网数据报。 |
| 多重性 | 0..1 |
| 类型 | 对 IdsMEvent 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00081] |
| --- | --- |
| 参数名称 | SEV_ETH_DROP_UNKNOWN_ETHERTYPE |
| 父容器 | EthIfSecurityEventRefs |
| 描述 | 由于 **EtherType** 未知而丢弃了以太网数据报。 |
| 多重性 | 0..1 |
| 类型 | 对 IdsMEvent 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_EthIf_00082] |
| --- | --- |
| 参数名称 | SEV_ETH_DROP_VLAN_DOUBLE_TAG |
| 父容器 | EthIfSecurityEventRefs |
| 描述 | 由于双重 **VLAN** 标签而丢弃了以太网数据报。 |
| 多重性 | 0..1 |
| 类型 | 对 IdsMEvent 的符号名引用 |
| 构建后变体多重性 | false |
| 构建后变体值 | false |
| 多重性配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：X；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

### 9.3. 发布信息

详细信息请参阅 **SWS_BSWGeneral** [\[6\]](#ref-6) 的第 10.3 章「发布信息」（**Published Information**）。

## B. AUTOSAR 可追溯项变更历史

请注意，本章中的列表还包括在后续版本中已从规范中移除的约束和规格项。这些约束和规格项在文档中不作为超链接出现。

### B.1. 本文档按 AUTOSAR 发布版本 R22-11 的变更历史

#### B.1.1. R22-11 中新增的规格项

```
SWS_EthIf_00520 SWS_EthIf_00521 SWS_EthIf_00522 SWS_EthIf_00523 SWS_EthIf_00524
SWS_EthIf_00525 SWS_EthIf_00526 SWS_EthIf_00531 SWS_EthIf_00532 SWS_EthIf_00533
SWS_EthIf_00534 SWS_EthIf_00535 SWS_EthIf_00536 SWS_EthIf_00541 SWS_EthIf_00542
SWS_EthIf_00543 SWS_EthIf_00544 SWS_EthIf_00545 SWS_EthIf_00546 SWS_EthIf_00547
SWS_EthIf_00551 SWS_EthIf_00552 SWS_EthIf_00553 SWS_EthIf_00554 SWS_EthIf_00555
SWS_EthIf_00556 SWS_EthIf_00557 SWS_EthIf_00560 SWS_EthIf_00561 SWS_EthIf_00562
SWS_EthIf_00563 SWS_EthIf_00564 SWS_EthIf_00565 SWS_EthIf_00566 SWS_EthIf_00567
SWS_EthIf_00568 SWS_EthIf_00569 SWS_EthIf_00570 SWS_EthIf_00571 SWS_EthIf_00572
SWS_EthIf_00573 SWS_EthIf_00574 SWS_EthIf_00575 SWS_EthIf_00576 SWS_EthIf_00577
SWS_EthIf_00578 SWS_EthIf_00579 SWS_EthIf_00580 SWS_EthIf_00581 SWS_EthIf_00582
SWS_EthIf_00583 SWS_EthIf_00584 SWS_EthIf_91201 SWS_EthIf_91202 SWS_EthIf_91203
SWS_EthIf_91204 SWS_EthIf_91205 SWS_EthIf_91206 SWS_EthIf_91207 SWS_EthIf_91208
SWS_EthIf_91209 SWS_EthIf_91210 SWS_EthIf_91211 SWS_EthIf_91212 SWS_EthIf_91213
SWS_EthIf_91214 SWS_EthIf_91215 SWS_EthIf_91216 SWS_EthIf_91217 SWS_EthIf_91218
SWS_EthIf_91219 SWS_EthIf_91220 SWS_EthIf_91221 SWS_EthIf_91222 SWS_EthIf_91223
SWS_EthIf_91224 SWS_EthIf_91225 SWS_EthIf_91226 SWS_EthIf_91227 SWS_EthIf_91228
SWS_EthIf_91229 SWS_EthIf_91230 SWS_EthIf_91231 SWS_EthIf_91232 SWS_EthIf_91233
SWS_EthIf_91234 SWS_EthIf_91235 SWS_EthIf_91236 SWS_EthIf_91237 SWS_EthIf_91238
SWS_EthIf_CONSTR_00001
```

#### B.1.2. R22-11 中变更的规格项

```
SWS_EthIf_00017 SWS_EthIf_00023 SWS_EthIf_00024 SWS_EthIf_00034 SWS_EthIf_00035
SWS_EthIf_00039 SWS_EthIf_00040 SWS_EthIf_00061 SWS_EthIf_00067 SWS_EthIf_00068
SWS_EthIf_00075 SWS_EthIf_00082 SWS_EthIf_00085 SWS_EthIf_00091 SWS_EthIf_00097
SWS_EthIf_00103 SWS_EthIf_00104 SWS_EthIf_00106 SWS_EthIf_00108 SWS_EthIf_00113
SWS_EthIf_00115 SWS_EthIf_00130 SWS_EthIf_00132 SWS_EthIf_00139 SWS_EthIf_00147
SWS_EthIf_00149 SWS_EthIf_00154 SWS_EthIf_00160 SWS_EthIf_00166 SWS_EthIf_00172
SWS_EthIf_00190 SWS_EthIf_00196 SWS_EthIf_00214 SWS_EthIf_00219 SWS_EthIf_00229
SWS_EthIf_00231 SWS_EthIf_00232 SWS_EthIf_00244 SWS_EthIf_00245 SWS_EthIf_00250
SWS_EthIf_00263 SWS_EthIf_00266 SWS_EthIf_00275 SWS_EthIf_00417 SWS_EthIf_00421
SWS_EthIf_00479 SWS_EthIf_00484 SWS_EthIf_00497 SWS_EthIf_00498 SWS_EthIf_00503
SWS_EthIf_00504 SWS_EthIf_91002 SWS_EthIf_91003 SWS_EthIf_91004 SWS_EthIf_91005
SWS_EthIf_91006 SWS_EthIf_91007 SWS_EthIf_91010 SWS_EthIf_91011 SWS_EthIf_91012
SWS_EthIf_91013 SWS_EthIf_91014 SWS_EthIf_91016 SWS_EthIf_91017 SWS_EthIf_91018
SWS_EthIf_91020 SWS_EthIf_91021 SWS_EthIf_91022 SWS_EthIf_91026 SWS_EthIf_91034
SWS_EthIf_91042 SWS_EthIf_91050 SWS_EthIf_91051 SWS_EthIf_91052 SWS_EthIf_91053
SWS_EthIf_91054 SWS_EthIf_91055 SWS_EthIf_91056 SWS_EthIf_91057 SWS_EthIf_91058
SWS_EthIf_91059 SWS_EthIf_91060 SWS_EthIf_91061 SWS_EthIf_91101 SWS_EthIf_91102
SWS_EthIf_91103 SWS_EthIf_91104 SWS_EthIf_91105 SWS_EthIf_91106 SWS_EthIf_91107
SWS_EthIf_91108 SWS_EthIf_91109 SWS_EthIf_91110 SWS_EthIf_91111 SWS_EthIf_91112
SWS_EthIf_91113 SWS_EthIf_91114 SWS_EthIf_91115 SWS_EthIf_91116 SWS_EthIf_91117
SWS_EthIf_91118 SWS_EthIf_91119 SWS_EthIf_91120 SWS_EthIf_91121 SWS_EthIf_91122
SWS_EthIf_91123 SWS_EthIf_91124 SWS_EthIf_91125 SWS_EthIf_91126 SWS_EthIf_91127
SWS_EthIf_91128 SWS_EthIf_91129 SWS_EthIf_91131 SWS_EthIf_91132 SWS_EthIf_91133
SWS_EthIf_91134
```

#### B.1.3. R22-11 中删除的规格项

无。

#### B.1.4. R22-11 中新增的约束

无。

#### B.1.5. R22-11 中变更的约束

无。

#### B.1.6. R22-11 中删除的约束

无。

### B.2. 本文档按 AUTOSAR 发布版本 R23-11 的变更历史

#### B.2.1. R23-11 中新增的规格项

```
SWS_EthIf_00102 SWS_EthIf_00585 SWS_EthIf_00586 SWS_EthIf_00587 SWS_EthIf_00588
SWS_EthIf_00589 SWS_EthIf_00590 SWS_EthIf_00591 SWS_EthIf_00592 SWS_EthIf_00593
SWS_EthIf_00600 SWS_EthIf_00601 SWS_EthIf_00602 SWS_EthIf_00603 SWS_EthIf_00604
SWS_EthIf_00605 SWS_EthIf_00606 SWS_EthIf_00607 SWS_EthIf_00608 SWS_EthIf_00609
SWS_EthIf_00610 SWS_EthIf_00611 SWS_EthIf_00612 SWS_EthIf_00614 SWS_EthIf_00615
SWS_EthIf_00616 SWS_EthIf_00617 SWS_EthIf_00618 SWS_EthIf_00619 SWS_EthIf_00620
SWS_EthIf_00621 SWS_EthIf_00622 SWS_EthIf_00623 SWS_EthIf_00624 SWS_EthIf_00625
SWS_EthIf_00626 SWS_EthIf_00627 SWS_EthIf_00628 SWS_EthIf_00629 SWS_EthIf_00630
SWS_EthIf_00631 SWS_EthIf_00632 SWS_EthIf_00633 SWS_EthIf_00634 SWS_EthIf_00635
SWS_EthIf_00636 SWS_EthIf_00637 SWS_EthIf_00638 SWS_EthIf_00639 SWS_EthIf_00640
SWS_EthIf_00641 SWS_EthIf_00642 SWS_EthIf_00643 SWS_EthIf_00644 SWS_EthIf_00645
SWS_EthIf_00646 SWS_EthIf_00647 SWS_EthIf_00648 SWS_EthIf_91023 SWS_EthIf_91024
SWS_EthIf_91025 SWS_EthIf_91027 SWS_EthIf_91062 SWS_EthIf_91063 SWS_EthIf_91064
SWS_EthIf_91065 SWS_EthIf_91066 SWS_EthIf_91136 SWS_EthIf_91137 SWS_EthIf_91138
SWS_EthIf_91139
```

#### B.2.2. R23-11 中变更的规格项

```
SWS_EthIf_00023 SWS_EthIf_00085 SWS_EthIf_00103 SWS_EthIf_00154 SWS_EthIf_00155
SWS_EthIf_00156 SWS_EthIf_00157 SWS_EthIf_00158 SWS_EthIf_00245 SWS_EthIf_00473
SWS_EthIf_00500 SWS_EthIf_00503 SWS_EthIf_91026 SWS_EthIf_91034 SWS_EthIf_91051
SWS_EthIf_91054 SWS_EthIf_91107 SWS_EthIf_91109 SWS_EthIf_91111 SWS_EthIf_91113
SWS_EthIf_91116 SWS_EthIf_91119 SWS_EthIf_91123 SWS_EthIf_91131 SWS_EthIf_91132
```

#### B.2.3. R23-11 中删除的规格项

无。

#### B.2.4. R23-11 中新增的约束

```
SWS_EthIf_CONSTR_00002 SWS_EthIf_CONSTR_00003 SWS_EthIf_CONSTR_00004 SWS_EthIf_CONSTR_00005
```

#### B.2.5. R23-11 中变更的约束

无。

#### B.2.6. R23-11 中删除的约束

无。
