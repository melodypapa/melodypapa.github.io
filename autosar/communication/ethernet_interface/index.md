<section id="title">AUTOSAR Ethernet Interface（以太网接口）</section>

# 1. 简介和功能概述

此规范指定了 **AUTOSAR** 基本软件模块以太网接口的功能、API 和配置。

在AUTOSAR分层软件架构[1]中，以太网接口（EthIf）属于ECU抽象层。或者更准确地说，它属于通信硬件抽象。

这表示以太网接口的主要任务：

向上层提供以太网通信系统的硬件独立接口，包括多个不同的有线或无线以太网控制器和收发器。此接口对于所有以太网控制器和收发器以及蜂窝 V2X 控制器需被统一。因此上层模块（**TCP/IP** [2]、**EthSM** [3]、**CDD**、**V2x** 等模块）可以以统一的方式访问底层总线系统。

以太网接口不直接访问以太网硬件（包括：以太网通信控制器和以太网收发器），而是通过一个或多个特定于硬件的驱动程序模块。

为了访问以太网控制器（**Ethernet controller**），以太网接口需要使用一个或多个以太网驱动程序（**Ethernet Driver**）模块，并且这些模块需抽象出相应的以太网控制器的特定功能和接口。

为了访问以太网收发器（**Ethernet transceiver**），以太网接口需要使用一个或多个以太网收发器驱动程序（**Ethernet Transceiver Driver**）模块，并且这些模块需抽象出相应的以太网收发器的特定功能和接口。

为了访问以太网交换机（**Ethernet switch**），以太网接口需要使用一个或多个以太网交换机驱动程序（**Ethernet Switch Driver**）模块，并且这些模块抽象出相应以太网交换机的特定功能和接口。

因此，以太网接口的可执行代码（不包括：运行时使用的配置）需完全独立于以太网通信控制器（**Ethernet Communication Controller**）。

![Figure1-1](Figure1-1.png)

注意：因为以太网接口的指定方式允许代码模块的目标代码交付，遵循“一刀切”原则，即以太网接口的整个配置可以在不修改任何源代码的情况下进行。所以以太网接口的配置在很大程度上可以在不详细了解底层硬件的情况下进行。

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

**AUTOSAR** 提供了基本软件模块的一般规范[6，SWS BSW通用]，该规范也适用于以太网接口。

所以，SWS BSW 通用规范应被视为以太网接口的附加和必需规范。

# 4. 约束和假设

## 4.1. 局限性

以太网接口在概念上能够访问一个或多个以太网驱动程序和一个或多个以太网收发器驱动程序。

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

### 6.1.1. 以太网控制器的分度方案

如果用**CAN XL**作为物理介质，则配置需包含**EthIfEthCanXLCtrlRef**来替代**EthIfEthCtrlRef**，以及**EthIfCanXLTrcvRef**来替代**EthIfEthTrcvRef**在这种情况下，表示为**\<EthDrv\>_Xxx** 的 API 将会使用**CanXL_Xxx**被调用，而不是使用**Eth_Xxx**被调用。同样，表示为**\<EthTrcv\>_Yyy** 的 API 将会使用**CanXLTrcv_Yyy**被调用，而不是使用**EthTrcv_Yyy**比调用。

以太网接口的用户使用索引方案识别以太网控制器资源，如图 7.2 所示。

![Figure7-2](Figure7-2.png)

因为以太网接口使用索引（**EthIfCtrlIdx**），从以太网控制器和以太网收发器的底层通信系统中抽象出对 **VLAN** 的访问。所以以太网接口应实现从以太网接口控制器（**EthIfCtrlIdx**）到相应硬件资源控制器（**EthCtrlId** + **EthTrcvId**）的映射。

### 6.1.2. 以太网交换机的索引方案

由于**EthIf**不涉及属于单个以太网交换机的单个**EthSwtPorts**，所以**EthIf**中不需要**EthSwtPorts**的索引方案。任何与**EthSwtPorts**交互的BSW模块都可以直接引用**EthSwtPort**的ECU配置进行索引。

**EthIf** 应将 **EthIfSwitchIdx** 索引的所有访问分派到具有 **EthSwtIdx** 值的相应 **EthSwt** 驱动程序模块。

