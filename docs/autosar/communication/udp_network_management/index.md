---
title: "AUTOSAR UdpNm (UDP Network Management)"
spec: AUTOSAR_CP_SWS_UDPNetworkManagement
release: R23-11
---




## 1. 简介和功能概述

本文档描述了**AUTOSAR UDP**网络管理（**UdpNm**）的概念、核心功能、可选特性、接口和配置问题。 **UdpNm**主要设计成一个可选功能, 旨在与**TCP/IP**堆栈一起工作，独立于所使用的通信系统的物理层。**AUTOSAR UDP**网络管理是一个独立于硬件的协议，可用于基于**TCP/IP**的系统。其主要目的是协调网络正常运行和总线睡眠模式之间的转换。

除了核心功能之外，它还提供了一些可选功能，例如：实现一个服务来检测所有当前节点或检测所有其他节点是否准备好休眠。

UDP 网络管理（**UdpNm**）功能提供网络管理接口（**Nm**）和**TCP/IP**堆栈之间的适配。 有关AUTOSAR网络管理功能的一般理解，请参阅[\[1\]](#ref-1)。

![Extended AUTOSAR Communication Stack.](Figure_1.png)

## 2. 缩略语

下面的词汇表包括与**UdpNm**模块相关、且未包含在AUTOSAR术语表[\[2\]](#ref-2)中的首字母缩略词和缩写词。

**API**
> 应用编程接口（**Application Programming Interface**）

**BSW**
> 基础软件（**Basic Software**）

**CWU**
> 整车唤醒（**Car Wakeup**）

**EthIf**
> 以太网接口（**Ethernet Interface**）

**DET**
> 默认错误跟踪器（**Default Error Tracer**）

**IP**
> 互联网协议（**Internet Protocol**）

**NM**
> 网络管理（**Network Management**）

**PDU**
> 协议数据单元（**Protocol Data Unit**）

**PNL**
> 部分网络学习（**Partial Network Learning**）

**SDU**
> 服务数据单元（**Service Data Unit**）

**TCP**
> 传输控制协议（**Transmission Control Protocol**）

**TCP/IP**
> 计算机网络中使用的一族通信协议（**A family of communication protocols used in computer networks**）

**UDP**
> 用户数据报协议（**User Datagram Protocol**）

**PNI**
> 部分网络信息（**Partial Network Information**）

**UdpNm**
> UDP网络管理（**UDP Network Management**）

**PDU传输能力被禁用**（**PDU transmission ability is disabled**）
> 这意味着**NM**消息传输已被可选服务[**UdpNm_DisableCommunication**](#735-udpnm_disablecommunication)禁用。

**重复消息请求位指示**（**Repeat Message Request Bit Indication**）
> [**UdpNm_SoAdIfRxIndication**](#742-udpnm_soadifrxindication)在接收到的**NM**消息的控制位向量中找到重复消息位。

**NM PDU**
> 指在数据包中传输的有效载荷。它包含**NM**用户数据以及控制位向量和源节点标识符。

**NM Packet**
> 指一个以太网帧，除了由NM在有效载荷部分传输的数据（**PDU**）之外，还包含一个**IP**和一个**UDP**报头。

**NM Message**
> 最抽象的术语，指在NM算法的方法论中传输的任何单个信息项。

**Bus-Off state**
> 指没有电缆连接到以太网硬件的情况。

**顶级PNC协调员**（**Top-level PNC coordinator**）
> 顶级PNC协调器是一个**ECU**，它充当网络中的PNC网关，并在所有分配的通道上主动协调处理至少一个PNC。如果启用了同步PNC关闭，如果网络中没有其他ECU请求它们，顶级PNC协调器将为这些PNC触发关闭。**注意：**对于不同的**PNC**，可以有不同的顶级**PNC**协调器。但对于同一个**PNC**，仅支持一个顶级协调器。

**中间PNC协调员**（**Intermediate PNC coordinator**）
> 中间PNC协调器是一个**ECU**，它充当网络中的PNC网关，并在至少一个分配的通道上将至少一个PNC处理为被动协调。如果启用了同步PNC关闭，它会将收到的这些PNC的关闭请求转发到相应的主动协调通道，并相应地启动它们的关闭。

**PNC叶节点**（**PNC leaf node**）
> PNC叶节点是一个**ECU**，在网络中根本不充当PNC协调器。它像通常的NM消息一样处理PN关闭消息。

**PN关闭消息**（**PN shutdown message**）
> 顶级PNC协调器发送PN关闭消息以指示跨PN拓扑的同步PNC关闭。PN关闭消息是作为**NM**消息，它在控制位向量中具有**PNSR**位，并且所有被指示用于同步关闭的PNC都设置为**1**。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

<a id="ref-1"></a>[1] Specification of Network Management Interface
> AUTOSAR_CP_SWS_NetworkManagementInterface

<a id="ref-2"></a>[2] Glossary
> AUTOSAR_FO_TR_Glossary

<a id="ref-3"></a>[3] General Specification of Basic Software Modules
> AUTOSAR_CP_SWS_BSWGeneral

<a id="ref-4"></a>[4] Specification of the AUTOSAR Network Management Protocol
> AUTOSAR_FO_PRS_NetworkManagementProtocol

<a id="ref-5"></a>[5] General Requirements on Basic Software Modules
> AUTOSAR_CP_SRS_BSWGeneral

<a id="ref-6"></a>[6] Requirements on AUTOSAR Network Management
> AUTOSAR_FO_RS_NetworkManagement

<a id="ref-7"></a>[7] Specification of Communication Manager
> AUTOSAR_CP_SWS_COMManager

<a id="ref-8"></a>[8] Guide to Mode Management
> AUTOSAR_CP_EXP_ModeManagementGuide

<a id="ref-9"></a>[9] System Template
> AUTOSAR_CP_TPS_SystemTemplate

<a id="ref-10"></a>[10] Specification of ECU State Manager
> AUTOSAR_CP_SWS_ECUStateManager

### 3.2. 相关规范

AUTOSAR提供了基础软件模块的通用规范[\[3\]](#ref-3)（**SWS BSW General**），它也适用于UDP网络管理。

因此，规范**SWS BSW General**应被视为UDP网络管理的附加和必需规范。

## 4. 约束和假设

### 4.1. 限制

1. 一个**UdpNm**实例只与一个网络中的一个NM集群（**NM-Cluster**）相关联。 一个NM集群在一个节点中只能有一个**UdpNm**实例。
2. **UdpNm**的一个实例仅与同一ECU内的一个网络相关联。
3. **UdpNm**仅适用于基于**TCP/IP**的系统。

下图展示了属于两个UDP NM集群的示例ECU内的AUTOSAR NM堆栈。

![](Figure_2.png)

默认情况下AUTOSAR UdpNm算法应支持每个NM集群包含最多250个节点。

**注意**：AUTOSAR UdpNm算法可以支持每个NM集群任意数量的节点（如果需要：甚至超过每个集群默认250个节点的限制）。这只是配置问题，上限不是固定的，取决于为AUTOSAR UdpNm协调算法配置的响应时间、容错性和结果总线负载之间的权衡。 这可能取决于所使用的物理层。

### 4.2. 汽车域的适用性

不适用（**N/A**）。

## 5. 对其他模块的依赖

UDP网络管理（**UdpNm**）使用**TCP/IP**堆栈的服务，并向通用网络管理接口（**Nm**）提供服务。

### 5.1. 文件结构

#### 5.1.1. 代码文件结构

代码文件结构不应在本规范中完整定义。但是，代码文件结构应包含以下文件：

* UdpNm_Lcfg.c（用于链接时可配置参数）
* UdpNm_PBcfg.c（用于编译后（**post-build**）时可配置参数）

这些文件应包含所有链接时/编译后时可配置的参数。

### 5.2. 协议层依赖

UDP网络管理基于PRS NetworkManagementProtocol [4, Specification of the AUTOSAR Network Management Protocol]中提到的协议。

![](Figure_3.png)

## 6. 功能规格

### 6.1. 协调算法

**AUTOSAR UdpNm**基于去中心化（**decentralized**）的直接网络管理策略，这意味着每个网络节点仅根据通信系统内接收和/或传输的UD 数据包，执行自给自足的活动。

AUTOSAR UdpNm协调算法基于周期性的NM数据包（**Nm Packet**），通过广播传输被集群中的所有节点所接收。接收到NM数据包表明发送节点希望保持NM集群处于唤醒状态。如果任何节点准备好进入总线睡眠模式（**Bus-Sleep Mode**），它就会停止发送NM数据包。但只要收到来自其他节点的NM数据包，它就会推迟转换到总线睡眠模式。最后如果由于不再接收到NM数据包，而导致专用计时器超时，则每个节点都会启动到总线睡眠模式的转换。

如果NM集群（**NM-cluster**）中的任何节点需要总线通信，它可以通过发送NM数据包来保持 NM集群唤醒状态。有关唤醒过程本身的更多详细信息，可参阅[\[7\]](#ref-7)。

AUTOSAR UdpNm协调算法的主要概念，可以通过以下两个关键需求定义：
1. 只要需要总线通信，每个网络节点都应发送周期性的NM PDU。否则节点就不应发送NM PDU。
2. 如果**UdpNmStayInPbsEnabled**被禁用，UdpNm集群中的总线通信被释放，同时通过配置参数**UdpNmTimeoutTime** + **UdpNmWaitBusSleepTime**确定的可配置时间量内，总线上没有网络管理PDU，则节点应执行转换到总线睡眠模式。

从NM集群中单个节点的角度来看，AUTOSAR UdpNm状态机应包含AUTOSAR UdpNm协调算法所需的状态（**state**）、转换（**transition**）和触发（**trigger**）。

![](Figure_4.png)

### 6.2. 操作模式

**AUTOSAR UdpNm**应包含以下的三种操作模式：

1. 网络模式（**Network Mode**）
2. 准备总线睡眠模式（**Prepare Bus-Sleep Mode**）
3. 总线睡眠模式（**Bus-Sleep Mode**）

**AUTOSAR UdpNm**操作模式的变化需要通过回调函数通知上层模块。

#### 6.2.1. 网络模式（Network Mode）

网络模式应包括三个内部状态：

1. 重复消息状态（**Repeat Message State**） 
2. 正常运行状态（**Normal Operation State**）
3. 就绪睡眠状态（**Ready Sleep State**）

当从**Bus-Sleep Mode**或**Prepare Bus-Sleep Mode**进入**Network Mode**时，默认进入**Repeat Message State**，**NM-Timeout Timer**将被启动，同时**UdpNm**需要通过调用 **Nm_NetworkMode**通知上层模块。

在网络模式下，成功接收到**NM PDU**后（调用[**UdpNm_SoAdIfRxIndication**](#742-udpnm_soadifrxindication)），需要重新启动 **NM-Timeout Timer**。

在网络模式下，成功传输**NM PDU**后（使用E_OK调用[UdpNm_SoAdIfTxConfirmation](#741-udpnm_soadiftxconfirmation)），也需要重新启动**NM-Timeout Timer**。

**注意：**
由于无法从**SoAd**或**TCP/IP**堆栈获得传输确认，因此假设每个网络管理**PDU**传输请求都是我网络管理PDU传输成功。

**NM-Timeout Timer**在每次启动或重新启动时，都需要被重置。

如果某通道的参数**UdpNmDynamicPncToChannelMappingEnabled**被设置为**TRUE**，且**UdpNm**也处于网络模式，同时在此通道上[**UdpNm_PnLearningRequest**](#7319-udpnm_pnlearningrequest)函数被调用，则 **UdpNm**模块需要将此通道上的**CBV**中的部分网络学习位（**Partial Network Learning Bit**）设置为**1**，同时一并设置重复消息位（**Repeat Message Bit**）。接着切换到**Repeat Message State**或者重新启动**Repeat Message State**。

如果某通道的参数**UdpNmDynamicPncToChannelMappingEnabled**被设置为**TRUE**，且 **UdpNm**也处于网络模式，同时在此通道上接收到的部分网络学习（**Partial Network Learning**）和重复消息（**Repeat Message**）的请求均为**1**时，则**UdpNm**模块需要将在此通道上的**CBV**中的部分网络学习位（**Partial Network Learning Bit**）设置为**1**，接着切换到**Repeat Message State**或者重新启动**Repeat Message State**。

**注意：**
在前面所述的，重新启动**Repeat Message State**意味着**UdpNm**已经处于**Repeat Message State**，然后必须执行一次重复消息状态的完全重新进入。

###### 6.2.1.1. 重复消息状态（Repeat Message State）

对于非被动模式（**Not in passive Mode**）的节点，重复消息状态确保从**Bus-Sleep**或**Prepare Bus-Sleep**到**Network Mode**的任何状态的转换，对于网络上的其他节点都是可见的。 此外，它还确保任何节点在最短的时间内保持活动状态 (**UdpNmRepeatMessageTime**)。 可选地，它可以用于检测当前的节点。

当从**Bus-Sleep Mode**、**Prepare-Bus-Sleep Mode**、正常操作状态（**Normal Operation State**）或**Ready Sleep State**进入**Repeat Message State**状态时，除非启用了被动模式，否则必须重新启动**NM**报文的传输。

当**NM-Timeout Timer**在**Repeat Message State**超时时，**NM-Timeout Timer**需要重新启动。

**NM**应在由配置参数**UdpNmRepeatMessageTime**确定的可配置时间量内，保持在重复消息状态。但在那之后需要离开**Repeat Message State**。

当离开**Repeat Message State**时：

* 如果网络又被请求，则应进入正常操作状态（**Normal Operation State**）。
* 如果网络已被释放，则应进入**Ready Sleep State**。

如果**UdpNmNodeDetectionEnabled**设置为**TRUE**,**UdpNm**需在离开**Repeat Message State**时，清除重复消息位（**Repeat Message Bit**）。

如果**UdpNmDynamicPncToChannelMappingSupport**设置为**TRUE**, **UdpNm**需在离开**Repeat Message State**时，清除部分网络学习位（**Partial Network Learning Bit**）。

###### 6.2.1.2. 正常运行状态（Normal Operation State）

正常操作状态（**Normal Operation State**）需确保任何节点在需要网络功能时，都能保持NM集群（NM-cluster）处于被唤醒状态。

当**Ready Sleep State**转换到正常操作状态（**Normal Operation State**），除非已启用被动模式或禁用NM报文的传输能力，否则**NM PDU**需立即开始传输。

在正常操作状态（**Normal Operation State**）下：

* 当**NM-Timeout Timer**超时后，需要重新启动**NM-Timeout Timer**。
* 如果网络被释放，则需要离开在正常操作状态（**Normal Operation State**），而进入**Ready Sleep state**状态。
* 如果**UdpNmNodeDetectionEnabled**设置为**TRUE**，并且接收到重复消息请求位（**Repeat Message Request bit**），则**UdpNm**需进入重复消息状态（**Repeat Message State**）。
* 如果**UdpNmNodeDetectionEnabled**设置为**TRUE**，并且函数[**UdpNm_RepeatMessageRequest**](#7311-udpnm_repeatmessagerequest)被调用，则**UdpNm**需进入重复消息状态（**Repeat Message State**），并设置重复消息位（**Repeat Message Bit**）。

###### 6.2.1.3. 就绪睡眠状态（Ready Sleep State）

**Ready Sleep State**确保任意一个节点在等待转换到**Prepare Bus-Sleep Mode**时，其他节点需保持NM集群（**NM-cluster**）处于被唤醒状态。

当从**Repeat Message State**或**Normal Operation State**进入**Ready Sleep State**时，应停止**NM PDU**的传输。

**注意：**
如果启用了被动模式，由于**NM PDU**已经不被传输，所以无需执行任何操作。如果禁用了被动模式，在某些情况下，**NM PDU**必须在就绪睡眠状态（**Ready Sleep State**）下传输，以允许网络的同步关闭（**synchronized shutdown**），例如：重新传输PN关闭消息（**PN shutdown messages**）。

在就绪睡眠状态（**Ready Sleep State**）下：

* 如果**NM-Timeout Timer**超时后，应离开就绪睡眠状态（**Ready Sleep State**），并进入准备总线睡眠模式（**Prepare Bus-Sleep Mode**）。
* 如果收到网络请求时，应离开就绪睡眠状态（**Ready Sleep State**），并进入正常操作状态（**Normal Operation State**）。
* 如果**UdpNmNodeDetectionEnabled**设置为**TRUE**，并且接收到重复消息请求位（**Repeat Message Request bit**），则UdpNm应进入重复消息状态（**Repeat Message State**）。
* 如果**UdpNmNodeDetectionEnabled**设置为**TRUE**，并且函数[**UdpNm_RepeatMessageRequest**](#7311-udpnm_repeatmessagerequest)被调用，则**UdpNm**需进入重复消息状态（**Repeat Message State**），并设置重复消息位（**Repeat Message Bit**）。

#### 6.2.2. 准备总线睡眠模式（Prepare Bus-Sleep Mode）

准备总线睡眠（**Prepare Bus Sleep**）状态的目的是确保所有节点在进入总线睡眠（**Bus Sleep**）状态之前，都有时间停止其网络活动。 总线活动平静下来（即：队列中的消息已被传输以便清空所有Tx缓冲区），最后在准备总线睡眠模式（**Prepare Bus-Sleep Mode**）下总线上没有活动。

当进入准备总线睡眠模式（**Prepare Bus-Sleep Mode**）时，**UdpNm**应通过调用**Nm_PrepareBusSleepMode**通知上层模块。

如果**UdpNmStayInPbsEnabled**被禁用，UdpNm需在配置参数**UdpNmWaitBusSleepTime**确定的可配置时间内，保持在准备总线睡眠模式（**Prepare Bus-Sleep Mode**）。直到时间超时后，需离开准备总线睡眠模式（**Prepare Bus-Sleep Mode**），并进入总线睡眠模式（**Bus-Sleep Mode**）。

注意：
此需求隐含地包含了：如果启用了**UdpNmStayInPbsEnabled**，**UdpNm**将永远不会因为超时而离开，即**UdpNm**将停留在准备总线睡眠模式（**Prepare Bus-Sleep Mode**），直到 **ECU**进入电源关闭或任何原因的重新启动。

在准备总线睡眠模式（**Prepare Bus-Sleep Mode**）下：
* 如果成功接收到**NM PDU**后，应离开准备总线睡眠模式（**Prepare Bus-Sleep Mode**），进入网络模式（**Network Mode**）。 并进入重复消息状态（**Repeat Message State**）。
* 如果需要请求网络时，应离开准备总线睡眠模式（**Prepare Bus-Sleep Mode**），进入网络模式（**Network Mode**）。 并进入重复消息状态（**Repeat Message State**）。

在准备总线睡眠模式（**Prepare Bus-Sleep Mode**）下，网络被请求后，**UdpNm**模块已进入网络模式，如果配置参数**UdpNmImmediateRestartEnabled**为**TRUE**，则**UdpNm**模块应发送**NM PDU**。

**理由：**
因为集群中的其他节点仍处于准备总线睡眠模式（**Prepare Bus-Sleep Mode**），在上述异常情况下，应避免过渡到总线睡眠模式（**Bus-Sleep Mode**），并应尽快恢复总线通信。

由于**UdpNm**中**NM PDU**的传输存在偏移，第一个处于重复消息状态的网络管理PDU的传输可能会有明显的延迟。为了避免网络延迟重新启动，可以立即请求网络管理PDU的传输。

**注意：**
如果**UdpNmImmediateRestartEnabled**为**TRUE**，并且使用了唤醒线路，则如果所有网络节点都在准备总线睡眠模式下收到网络请求，则会发生网络管理PDU突发（**burst of Network Management PDUs**）。

#### 6.2.3. 总线睡眠模式（**Bus-Sleep Mode**）

总线睡眠（**Bus-Sleep**）状态的目的是为了在没有消息交换时，降低节点中的功耗。

通信控制器切换到睡眠模式，激活相应的唤醒机制，最后在总线睡眠模式下将功耗降低到足够的水平。

如果禁用**UdpNmStayInPbsEnabled**，同时为网络管理集群中的所有节点配置相同的时间（由配置参数**UdpNmTimeoutTime** + **UdpNmWaitBusSleepTime**确定），则网络管理集群中使用**AUTOSAR NM**算法协调的所有节点会在差不多相同的时间转换到总线睡眠模式（**Bus-Sleep Mode**）。

**注意：**
参数**UdpNmTimeoutTime**和**UdpNmWaitBusSleepTime**在NM集群的所有网络节点中应该具有相同的值。根据具体实施，转换到总线睡眠模式大约同时发生。

此转换所经历的时间抖动取决于以下因素：
* 内部时钟精度（振荡器漂移）。
* NM-Task周期时间（如果任务未通过全局时间同步）。
* **NM PDU**在Tx队列中的等待时间（如果在发送请求后立即进行发送确认）。

对于最佳情况估计，在可配置的时间量内主要需要考虑振荡器漂移。

当进入总线睡眠模式（**Bus-Sleep Mode**）时，**UdpNm**应通过调用**Nm_BusSleepMode**通知上层模块。如果在初始化时默认进入总线睡眠模式，则不需考虑这场景。

在总线睡眠模式（**Bus-Sleep Mode**）下，当**UdpNm**模块成功接收到网络管理PDU（调用[**UdpNm_SoAdIfRxIndication**](#742-udpnm_soadifrxindication)）时，**UdpNm**模块将通过调用回调函数**Nm_NetworkStartIndication**通知上层模块。

**基本原理：**
为避免网络和模式管理（**Mode Management**）之间的竞争条件和状态不一致，**UdpNm**不会自动执行从总线睡眠模式（**Bus-Sleep Mode**）到网络模式（**Network Mode**）的转换。**UdpNm**只会通知必须做出唤醒决定的上层模块。总线睡眠模式（**Bus-Sleep Mode**）下的**NM**数据包接收，必须依据ECU关闭（**shutdown**）或启动（**startup**）过程的当前状态进行处理。

在总线睡眠模式（**Bus-Sleep Mode**）或准备总线睡眠模式（**Prepare Bus-Sleep Mode**）下，如果[UdpNm_PassiveStartUp](#732-udpnm_passivestartup)被调用，则**UdpNm**模块应进入网络模式（**Network Mode**），并进入重复消息状态（**Repeat Message State**）。

**注意：**
在准备总线睡眠模式（**Prepare Bus-Sleep Mode**）和总线睡眠模式（**Bus-Sleep Mode**）下，假定网络被释放，除非有明确的总线通信请求。

在总线睡眠模式（**Bus-Sleep Mode**）下，当网络被请求，**UdpNm**模块应进入网络模式； 并进入重复消息状态（**Repeat Message State**）。

### 6.3. 网络状态（Network states）

网络状态（**Network states**）包含“被请求”（**requested**）和“被释放”（**released**），它是**AUTOSAR UdpNm**状态机的两个附加状态，并与状态机并行存在。网络状态表示了，软件模块是否需要在总线上进行通信（即：网络状态为被请求），或者软件模块是否无需在总线上通信（即：总线网络状态为被释放）。请注意，即使网络被释放，一个ECU仍然可以通信，因为其他一些ECU仍然请求网络。

可调用函数[**UdpNm_NetworkRequest**](#733-udpnm_networkrequest)请求网络。 即：**UdpNm**模块应将网络状态更改为“被请求”。可调用函数[**UdpNm_NetworkRelease**](#734-udpnm_networkrelease)释放网络。 即：**UdpNm**模块应将网络状态更改为“被释放”。

### 6.4. 初始化

UdpNm模块应该在**SoAd**初始化之后，并且在任何其他网络管理服务被调用之前初始化。在成功初始化后，网络管理状态为BusSleep模式。

初始化后默认情况下，**UdpNm**模块应将网络状态设置为“已释放”（**released**），并且进入总线睡眠模式（**Bus-Sleep Mode**）。

如果**AUTOSAR UdpNm**模块未初始化，则不应禁止总线通信流（**bus traffic**）。

函数[UdpNm_Init](#731-udpnm_init)可通过传递的配置指针参数选择活动配置集。

初始化后，NM消息的传输将停止，用户数据字节（**user data byte**）的每个字节都应设置为0xFF，控制位向量（**Control Bit Vector**）应设置为0x00。

在初始化期间，如果**UdpNmPnEnabled**为**TRUE**，UdpNm模块应将PNC位向量（**PNC bit vector**）的每个字节设置为0x00。

一个NM集群中不同ECU上的所有UDP NM实例应使用相同的UDP接收端口。

### 6.5. 执行（Execution）

#### 6.5.1. 处理器架构（Processor architecture）

**AUTOSAR UdpNm**协调算法应独立于处理器，这意味着它不应依赖于任何处理器的特定硬件支持，因此应可在AUTOSAR范围内的任何处理器架构上实现。

#### 6.5.2. 时序参数（Timing parameters）

* 配置参数**UdpNmTimeoutTime**：定义了**UdpNm**的定时参数NM超时时间。
* 配置参数**UdpNmRepeatMessageTime**：定义了**UdpNm**定时参数重复消息时间。
* 配置参数**UdpNmWaitBusSleepTime**：定义了**UdpNm**定时参数等待总线睡眠的时间
* 可选配置参数**UdpNmRemoteSleepIndTime**：定义了**UdpNm**定时参数定时远程睡眠指示时间。

### 6.6. 通信调度

#### 6.6.1. NM 消息传输

以下描述的传输机制仅在启用NM消息传输能力时才相关。

NM消息的传输应可通过**UdpNmPassiveModeEnabled**进行配置。被动节点不发送NM消息，即：它们不能主动影响关闭决策，但它们确实接收NM消息以便能够同步关闭。

**UdpNm**模块应提供周期性传输模式。在这种传输模式下，**UdpNm**模块将定期发送网络管理PDU。周期性传输模式可在“重复消息状态”（**Repeat Message State**）和“ 正常运行状态”（**Normal Operation State**）中使用。

如果未通过[**UdpNm_NetworkRequest**](#733-udpnm_networkrequest)进入重复消息状态或**UdpNmImmediateNmTransmissions**为**0**，则进入重复消息状态后，**NM PDU**的传输应延迟**UdpNmMsgCycleOffset**。

以上的情况也覆盖了，如果由于重复消息请求或重复消息位，状态从网络操作状态或就绪睡眠状态进入重复消息状态。这意味着在这种情况下不使用立即传输（即： **UdpNmImmediateNmTransmissions** > 0 并且独立于**UdpNmPnHandleMultipleNetworkRequests**的配置），**UdpNmMsgCycleOffset**将始终被应用 。这种机制可以防止NM消息的突发。

由于[UdpNm_NetworkRequest](#733-udpnm_networkrequest)()被调用（即：主动唤醒），状态从总线睡眠模式或准备总线睡眠模式进入重复消息状态时，如果**UdpNmImmediateNmTransmissions** > 0，则应使用 **UdpNmImmediateNmCycleTime**作为循环时间来发送**NM PDU**。 同时需要尽快地触发第一个**NM PDU**的传输。传输后，消息周期计时器（**Message Cycle Timer**）应重新加载**UdpNmImmediateNmCycleTime**。 在这种情况下不应使用参数**UdpNmMsgCycleOffset**。

**注意：**
在这种情况下，**UdpNmImmediateNmTransmissions**必须大于零，因为如果该值为零，则不发送立即的**NM PDU**。

如果**NM PDU**使用**UdpNmImmediateNmCycleTime**方式传输，则UdpNm应确保UdpNmImmediateNmTransmissions（包括第一次立即传输）在配置的时间内请求成功。如果对SoAd的传输请求失败（即：返回**E_NOT_OK**），**UdpNm**将在下一个主函数中重试传输请求。但之后**UdpNm**将继续使用**UdpNmMsgCycleTime**发送**NM PDU**。

**注意：**
当使用**UdpNmImmediateNmCycleTime**传输**NM PDU**时，不得传输其他**Nm PDU**（如：停止**UdpNmMsgCycleTime**传输周期）。

如果**NM PDU**的传输已经开始并且**UdpNm**消息周期计时器（**Message Cycle Timer**）超时，则应通过调用**SoAd_IfTransmit**，通过**SoAd**传输**NM PDU**。

如果**UdpNm**消息周期计时器超时，它应使用**UdpNmMsgCycleTime**重新启动。如果**NM PDU**的传输已停止，则应取消**UdpNm**消息周期计时器。

如果参数**UdpNmRetryFirstMessageRequest**为**TRUE**，并且如果从总线休眠到重复消息状态转换后的第一个传输请求未被**SoAd**接受，则应在下一个主函数中重复该消息请求，直到**SoAd**接受一个传输请求。

**注意：**
此功能可用于部分网络唤醒过滤器的情况，以避免在被动启动（**passive start-up**）的情况下阻塞所有消息，并且由于EthSM无法足够快地启用传输路径（例如：在异步收发器处理的情况）。

如果[**UdpNm_SoAdIfTxConfirmation**](#741-udpnm_soadiftxconfirmation)调用结果为**E_NOT_OK**，UdpNm将调用函数**Nm_TxTimeoutException**。

#### 6.6.2. 接收

如果成功接收到NM消息，**SoAd**模块将调用[**UdpNm_SoAdIfRxIndication**](#742-udpnm_soadifrxindication)。在调用[**UdpNm_SoAdIfRxIndication**](#742-udpnm_soadifrxindication)时，**UdpNm**模块应将函数参数中引用的网络管理PDU的数据复制到内部缓冲区。 

当接收到**NM PDU**时，如果**UdpNmPduRXIndicationEnabled**（配置参数）为**TRUE**，则应调用**Nm**函数**Nm_PduRxIndication**。

### 6.7. 附加的功能

#### 6.7.1. 远程睡眠指示检测（可选）

“远程睡眠指示”（**Remote Sleep Indication**）表示以下的场景。其中处于正常操作状态的节点发现集群中的所有其他节点都准备好进入睡眠状态。仍然处于“正常操作状态”的节点将仍然使总线保持清醒。

远程睡眠指示的检测需使用**UdpNmRemoteSleepIndEnabled**开关（配置参数），进行静态配置。如果在由**UdpNmRemoteSleepIndTime**（配置参数）确定的可配置时间量内，在正常操作状态下没有收到**NM PDU**，则**NM**应通过调用**Nm_RemoteSleepIndication**通知通用网络管理接口（**Generic Network Management Interface**），集群中的所有其他节点都准备好进入睡眠状态（即：所谓的“远程睡眠指示”）。

如果先前已检测到远程睡眠指示，此时在正常操作状态（**Normal Operation State**）或就绪睡眠状态（**Ready Sleep State**）下再次接收到**NM PDU**，则NM需要通过调用 **Nm_RemoteSleepCancelation**通知通用网络管理接口（**Generic Network Management Interface**），集群中的某些节点已不再准备睡眠（**ready to sleep**）（即：所谓的“远程睡眠取消”）。

如果先前已检测到远程睡眠指示，此时从正常操作状态（**Normal Operation State**）进入重复消息状态（**Repeat Message State**），则NM也需要通过调用 **Nm_RemoteSleepCancelation**通知通用网络管理接口（**Generic Network Management Interface**），集群中的某些节点已不再睡眠就绪（**ready to sleep**）（即：所谓的“远程睡眠取消”）。

NM应拒绝在总线睡眠模式、准备总线睡眠模式和重复消息状态下对远程睡眠指示的检查，服务不被执行，并返回**E_NOT_OK**。

#### 6.7.2. 用户数据（可选）

NM用户数据的支持需使用**UdpNmUserDataEnabled**开关（配置参数）进行静态配置。

通过调用[**UdpNm_SetUserData**](#737-udpnm_setuserdata)，可以实现对总线下一个发送的NM包里NM用户数据的设置。此函数会确保设置的Nm用户数据的一致性。

通过调用[**UdpNm_GetUserData**](#738-udpnm_getuserdata)，可以获取最近接收到的NM PDU的有效载荷中包含的NM用户数据。此函数会确保接收的Nm用户数据的一致性。

**注意:**
如果配置了Nm用户数据，它会在重复消息状态（**Repeat Message State**）下发送。但在就绪睡眠状态（**Ready Sleep State**），用户数据不会被发送。

如果启用了**UdpNmComUserDataSupport**，则函数[**UdpNm_SetUserData**](#737-udpnm_setuserdata)将不可用。

如果启用了**UdpNmComUserDataSupport**并且**NM-PDU**未配置为在 SoAd中触发传输（SoAdBswModules/SoAdIfTriggerTransmit = FALSE），则**UdpNm**会通过调用 **PduR_UdpNmTriggerTransmit**从引用的**NM I-PDU**中收集**NM**用户数据，并在每次请求传输相应的NM消息之前，把用户数据与NM的数据合并。

**注意：**
在触发传输的情况下，传输请求不需要数据，只需要长度。数据将在**UdpNm_TriggerTransmit**中收集。

如果启用了**UdpNmComUserDataSupport**，**UdpNm**处于重复消息状态（**Repeat Message State**）或 正常操作状态（**Normal Operation State**），并且调用了 [**UdpNm_Transmit**](#7318-udpnm_transmit)，则**UdpNm**将请求使用当前用户数据的**NM PDU**的附加传输。

#### 6.7.3. 被动模式（可选）

在被动模式下，节点只接收NM消息，但不发送任何NM消息。被动模式应可使用 **UdpNmPassiveModeEnabled**开关（配置参数）进行静态配置。被动模式应针对一个ECU 内的所有实例进行一致的静态配置。

如果使用被动模式（配置参数**UdpNmPassiveModeEnabled**），则不得使用以下选项：

* 总线同步（**Bus Synchronization**）。【配置参数：**UdpNmBusSynchronizationEnabled**】。
* 远程睡眠指示（**Remote Sleep Indication**）。【配置参数：**UdpNmRemoteSleepIndEnabled**】。
* 节点检测（**Node Detection**）。【配置参数：**UdpNmNodeDetectionEnabled**】。

#### 6.7.4. 状态变化通知（可选）

如果回调**Nm_StateChangeNotification**被启用（配置参数：**UdpNmStateChangeIndEnabled**为**TRUE**），则AUTOSAR UdpNm状态的所有变化都需要通过调用**Nm_StateChangeNotification**通知上层模块。

#### 6.7.5. 通讯控制（可选）

通信控制（**Communication Control**）需使用**UdpNmComControlEnabled**开关（配置参数）进行静态配置。

可选服务[**UdpNm_DisableCommunication**](#735-udpnm_disablecommunication)可禁用**NM PDU**传输能力。

**注意：**
如果禁用**NM PDU**传输能力，**NM**协调算法将无法正常工作。 因此，必须确保即使**NM PDU**传输能力被禁用，**ECU**也不会关闭（**shutdown**）。

如果[UdpNm_NetworkRelease](#734-udpnm_networkrelease)被调用，并且**NM PDU**传输能力也已被禁用，则**ECU**将关闭。 这确保了**ECU**也可以在以下的情况下关闭：

* 竞争条件（例如：在启用通信之前不久离开诊断会话）
* 错误使用通信控制的。

如果当前模式不是网络模式，可选服务[**UdpNm_DisableCommunication**](#735-udpnm_disablecommunication)应返回**E_NOT_OK**。

**当NM PDU传输能力被禁用时**：

* UdpNm模块需停止UdpNm消息周期定时器以停止**NM PDU**的传输。
* 需要停止NM超时定时器（**NM-Timeout Timer**）。
* 远程睡眠指示定时器（**Remote Sleep Indication Timer**）的检测将被暂停。
* 可选服务[**UdpNm_RequestBusSynchronization**](#7315-udpnm_requestbussynchronization)应返回**E_NOT_OK**。

**当NM PDU传输能力被启用时**：

* **NM PDU**的传输需最晚在下一个NM主函数中开始。
* 需重新启动NM超时定时器（**NM-Timeout Timer**）。
* 需恢复远程睡眠指示定时器（**Remote Sleep Indication Timer**）的检测。

#### 6.7.6. NM 协调器同步支持（可选）

当有多个协调器连接到同一总线时，CBV中有一个特殊位，**NmCoordinatorSleepReady位**用于指示主协调器请求启动关闭序列。该算法的主要功能可参考Nm模块中的描述。

如果**UdpNm**调用**NM_CoordReadyToSleepIndication**，并且仍处于网络模式，它应在第一次接收到带有**NmCoordinatorSleepReady位**的NM消息时调用 **Nm_CoordReadyToSleepCancellation**通知Nm，将其设置为**0**。

如果**UdpNm**已进入网络模式或调用**Nm_CoordReadyToSleepCancellation**，则它应在第一次收到NM消息时，调用**Nm_CoordReadyToSleepIndication**通知NM，并且**NmCoordinatorSleepReady位**设置为**1**。

如果**UdpNmCoodinatorSyncSupport**设置为**TRUE**，并且API [**UdpNm_SetSleepReadyBit**](#7317-udpnm_setsleepreadybit)被调用，**UdpNm**应设置**NmCoordinatorSleepReady位**,并触发单个**NM PDU**。

仅当**UdpNmCoordinatorSyncSupport**设置为**TRUE**时，程序接口[**UdpNm_SetSleepReadyBit**](#7317-udpnm_setsleepreadybit) 和**Coordinated Bus Shutdown**功能才可用。

### 6.8. 部分联网（Partial Networking）

#### 6.8.1. NM PDU的Rx处理

当**UdpNmPnEnabled**为**FALSE**，则**UdpNm**应执行正常的Rx指示处理，并且应禁用部分网络（**partial networking**）扩展。

当**UdpNmPnEnabled**为**TRUE**：
* 如果接收到的**NM-PDU**中的**PNI**位为**0**，并且**UdpNmAllNmMessagesKeepAwake**为**TRUE**，则**UdpNm**模块需执行正常的**Rx**指示处理，省略部分网络的扩展。
* 如果接收到的**NM-PDU**中的**PNI**位为**0**，并且**UdpNmAllNmMessagesKeepAwake**为**FALSE**，则**UdpNm**模块需忽略接收到的**NM-PDU**。
* 如果接收到的**NM-PDU**中的**PNI**位为**1**，则**UdpNm**模块需按照第[6.8.3](#683-nm-pdu过滤算法)至[6.8.5](#685-外部请求的部分网络的聚合)所述处理**NM-PDU**的部分网络信息。

#### 6.8.2. NM PDU的Tx处理

如果**UdpNmPnEnabled**为**TRUE**，则**UdpNm**模块需将**CBV**中发送的**PNI**位的值设置为**1**。

如果**UdpNmPnEnabled**为**FALSE**，则**UdpNm**模块需将**CBV**中发送的**PNI**位的值始终设置为**0**。

**注意：**
如果使用部分网络，则必须使用CBV。

#### 6.8.3. NM PDU过滤算法

接收到的**NM-PDU**中包含PN请求信息（**PN request information**）的范围，已字节位单位。它由**UdpNmPnInfoOffset**（字节）和**UdpNmPnInfoLength**（字节）定义。 此范围称为PN信息范围（**PN Info Range**）。

**例如:**

- UdpNmPnInfoOffset = 3
- UdpNmPnInfoLength = 2

表示NM消息中只有第3个字节和第4字节，包含PN请求信息。

PN信息范围的每一位代表一个部分网络（**Partial Network**）。如果该位设置为**1**，则请求部分网络。如果该位设置为**0**，则没有对该PN的请求。

通过配置参数**UdpNmPnFilterMaskByte**，UdpNm能够检测哪些**PN**与**ECU**相关，哪些不相关。**UdpNmPnFilterMaskByte**的每一位具有以下含义：

* 0：PN请求与ECU无关。即使在接收到的**NM-PDU**中设置了该位，ECU的通信堆栈也不会保持唤醒。
* 1：PN请求与ECU相关。如果在接收到的**NM-PDU**中设置了该位，则ECU的通信堆栈保持唤醒

每个PN过滤器掩码字节需按位与（**bitwise AND**）的方式映射到**NM**消息的PN信息范围内的相应字节。如果接收到的**NM-PDU**的PN信息范围内至少一位与NM过滤掩码中的一位匹配，则PN请求信息与ECU相关。

如果在接收到的**NM-PDU**中没有请求相关的PN，并且**UdpNmAllNmMessagesKeepAwake** 为**FALSE**，则UpdNm模块需丢弃该PDU。

如果在接收到的**NM-PDU**中没有请求相关的PN，并且**UdpNmAllNmMessagesKeepAwake**为**TRUE**，则UpdNm模块不应丢弃该**PDU**，并在进一步的Rx指示处理。

#### 6.8.4. 内部和外部请求的部分网络的聚合

由于部分网络的活动，每个使用此功能**ECU**都必须切换**I-PDU Group**。 例如：为了防止错误超时）。如果内部或外部请求相应的**PN**，则需打开**I-PDU Group**。直到所有内部和外部对相应**PN**的请求都被释放后，**I-PDU Group**才会被关闭。

切换**I-PDU Group**的逻辑由**ComM**实现。**UdpNm**模块仅提供是否请求PN的信息，COM模块用于将数据传输到上层。

为了在所有直接连接的ECU上同步切换**I-PDU Group**，UdpNm需要实现每个ECU几乎在同一时刻，向上层提供请求更改的信息。这就是为什么每次收到和发送的NM消息都会重新启动重置计时器。

内部和外部请求PN的聚合状态，称为（**EIRA**）。即：外部内部请求聚合（**External Internal Requests Aggregated**）。

如果**UdpNmPnEiraCalcEnabled**为**TRUE**，则**UdpNm**应提供在所有相关通道（即：所有**UdpNmPnEnabled**为**TRUE**的**UdpNm**通道）上组合存储外部和内部请求PN的可能性。在初始化时，所有PN的值应设置为**0**（未请求）。

如果外部请求满足以下条件，**UdpNm**需存储这些PN的请求信息，并把PN的值设置为**1**

* **UdpNmPnEiraCalcEnabled**为**TRUE**
* 接收到**NM-PDU**
* PN在此消息中被请求（即：相关位都已经设置为**1**）
* 请求的PN在配置的PN过滤器掩码中设置也都为**1**

如果内部请求满足以下条件，**UdpNm**也需存储这些PN的请求信息，并把PN的值设置为**1**

* **UdpNmPnEiraCalcEnabled**为**TRUE**
* UdpNM正在请求发送**NM-PDU**
* 在此消息中请求PN（即：相关位都已经设置为**1**）
* 请求的PN在配置的PN过滤器掩码中设置也都为**1**

如果**UdpNmPnEiraCalcEnabled**为TRUE，并且此PN仍然在至少一个相关通道上被外部或内部请求，则**UdpNm**模块需提供监视每个PN的可能性。

**注意：**
这意味着只需要一个计时器来处理多个连接的物理通道上的一个PN。例如：只需要8个EIRA重置定时器（**reset timer**）来处理具有6个物理通道和8个部分网络的网关的请求。这主要因为PN的**PDU Group**的切换是为ECU全局完成的，而不依赖于任何物理通道。

如果**UdpNmPnEiraCalcEnabled**为TRUE，并且在消息接收或发送时请求PN，则应根据**UdpNmPnResetTime**重新开始对该PN的监视。

**注意：**
**UdpNmPnResetTime**需配置为大于**UdpNmMsgCycleTime**的值。如果将 **UdpNmPnResetTime**配置为小于**UdpNmMsgCycleTime**的值，并且只有一个ECU请求PN，则请求状态在**EIRA**中切换。因为请求状态在请求的ECU能够发送下一个NM消息之前已停止。

同时**UdpNmPnResetTime**应配置为小于**UdpNmTimeoutTime**的值，以避免在NM已更改为准备总线睡眠（**Prepare Bus Sleep**）后，定时器可能会超时。

如果**UdpNmPnEiraCalcEnabled**为**TRUE**，并且在**UdpNmPnResetTime**时间内未再次请求PN，则该PN的相应存储值应设置为**0**（未请求）。

如果**UdpNmPnEiraCalcEnabled**为**TRUE**，并且存储的PN值设置为已请求或返回为未请求，**UdpNm**需通过调用**PduR_UdpNmRxIndication**通知上层关于配置的**EIRA PDU**（更改的**EIRA**信息需要传递给COM）。

如果**UdpNmPnEiraCalcEnabled**为**TRUE**，并且**UdpNmPnEraCalcEnabled**为**TRUE**，则PN状态信息必须分别存储为两份：**EIRA**和**ERA**信息。

#### 6.8.5. 外部请求的部分网络的聚合

此功能主要供网关（**gateway**）收集外部PN请求（**external PN request**）使用。外部PN请求被镜像回请求总线，并提供给中央网关的其他物理通道。

在子网关的情况下，请求位（**requests bit**）不得镜像回请求的物理通道，以避免中央网关和子网关之间的静态唤醒。 该逻辑应由**ComM**模块实现。

**UdpNm**模块提供是否从外部请求PN的信息。COM模块用于向上层传输数据。外部请求的PN的聚合状态称为ERA，即：外部请求聚合（**External Requests Aggregated**）。

如果**UdpNmPnEraCalcEnabled**为**TRUE**，则**UdpNM**应提供在每个相关通道上存储外部请求的**PN**的可能性。 在初始化时，所有PN的值应设置为**0**（未请求）。

如果以下条件满足，UdpNm 将存储这些PN的请求信息，并把PN的值设置为**1**。
* **UdpNmPnEraCalcEnabled**为**TRUE**。
* 接收到**NM-PDU**。
* 在此接收消息中请求PN（即：相关位都已经设置为**1**）。
* 请求的PN在配置的PN过滤器掩码中设置为**1**。

如果**UdpNmPnEraCalcEnabled**为**TRUE**，并且此PN仍然被外部请求，则**UdpNm**模块需提供监视每个相关通道和每个PN的可能性。

这意味着需要一个单独的计时器（**separate timer**）来处理多个物理通道上的一个PN。例如：需要48个ERA复位定时器来处理具有6个物理通道和8个部分网络的网关的请求。不能像 **EIRA**定时器那样组合复位定时器，因为外部请求不能通过子网关（**sub gateway**）镜像回请求总线。因此需要检测作为请求位源的物理通道。

如果**UdpNmPnEraCalcEnabled**为**TRUE**，并且消息接收请求PN，则应根据 **UdpNmPnResetTime**重新开始对该PN的监视。

**注意：**
**UdpNmPnResetTime**需配置为大于**UdpNmMsgCycleTime**的值。如果将 **UdpNmPnResetTime**配置为小于**UdpNmMsgCycleTime**的值，并且只有一个ECU请求PN，则请求状态在**ERA**中切换，因为请求状态在请求的ECU能够发送下一个**NM-PDU**之前已停止。

同时**UdpNmPnResetTime**应配置为小于**UdpNmTimeoutTime**的值，以避免在NM已更改为准备总线睡眠（**Prepare Bus Sleep**）后，定时器可能会超时。

如果**UdpNmPnEraCalcEnabled**为**TRUE**，并且在**UdpNmPnResetTime**时间内未再次请求PN，则该PN的相应存储值应设置为**0**（未请求）。

如果**UdpNmPnEraCalcEnabled**为**TRUE**，并且存储的PN值设置为已请求或返回为未请求，**UdpNm**需通过调用**PduR_UdpNmRxIndication**通知上层关于配置的**ERA PDU**（更改的**ERA**信息需要传递给COM）。

如果**UdpNmPnEiraCalcEnabled**为**TRUE**，并且**UdpNmPnEraCalcEnabled**为**TRUE**，则PN状态信息必须分别存储为两份：**EIRA**和**ERA**信息。

#### 6.8.6. 内部请求的部分网络集群的处理

所有内部**PNC**请求都由**ComM**维护。**ComM**将每个通道上聚合的内部**PNC**请求作为**PNC**位向量转发给**NmIf**。该**PNC**位向量承载所谓的「内部请求数组」（**Internal Request Array**，**IRA**）。**UdpNm**必须在每次传输**NM_PDU**时从**NmIf**获取最新的**IRA**。**NmIf**向**UdpNm**提供**IRA**信息并更新**PNC**重置计时器（每次传输相关**PNC**时，**PNC**重置计时器都会重新启动）。

**注意：**

对于**UdpNmPnEnabled**设置为**TRUE**的所有已配置**NM**通道，**UdpNm**将调用**Nm_PncBitVectorTxIndication**（&lt;NM通道&gt;，&lt;用于存储聚合内部**PNC**请求的未过滤**PNC**位向量的缓冲区&gt;）以指示传输，并根据配置的**NmPncBitVectorLength**获取作为**PNC**位向量的当前内部**PNC**请求。**UdpNm**会将接收到的内部**PNC**请求复制到**NM-PDU**的**PNC**位向量字节中。

#### 6.8.7. 通过UdpNm_NetworkRequest自发传输NM-PDU

如果**UdpNmPnHandleMultipleNetworkRequests**设置为**TRUE**，[**UdpNm_NetworkRequest**](#733-udpnm_networkrequest)接口被调用，并且**UdpNm**处于就绪睡眠状态（**Ready Sleep State**）、正常操作状态（**Normal Operation State**）或重复消息状态（**Repeat Message State**），则UdpNm将更改为或重新启动重复消息状态（**Repeat Message State**）。

**注意：**
如果**UdpNmPnHandleMultipleNetworkRequests**设置为**TRUE**，则**UdpNm**的立即传输（**Immediate Transmission**）功能是强制性的。

如果PN请求位发生变化，PN控制模块（例如：ComM）负责调用[**UdpNm_NetworkRequest**](#733-udpnm_networkrequest)。

### 6.9. 有效载荷（PDU）的结构

下图显示了n字节长度PDU的示例。

![](Figure_5.png)

网络管理PDU的长度是由全局ECUC模块（**global ECUC module**）中的PduLength参数定义。（请参阅EcuC的规范）。启用系统的字节数和长度之间的差异是用户数据字节（**user data bytes**）的数量。

* 源节点标识符（**Source Node Identifier**）的位置应可通过**UDPNM_PDU_NID_POSITION**配置为**字节0**、**字节1**或**关闭**。默认为字节0。
* 控制位向量（**Control Bit Vector**）的位置应可通过**UDPNM_PDU_CBV_POSITION** 配置为**字节0**、**字节1**或**关闭**。默认为字节1。

NM包的长度不能超过底层物理传输层的MTU（**Maximum Transmission Unit**）。

#### 6.9.1. 控制位向量（**Control Bit Vector**）

下图描述了控制位向量的格式：

![](Figure_6.png)

控制位向量应包括：
* 位0：重复消息请求。
  * 0：未请求重复消息状态；
  * 1：请求重复消息状态。
* 位1：保留用于将来的扩展。默认为0。
* 位2：保留用于将来的扩展。默认为0。
* 位3：NM协调器休眠位。
  * 0：主协调器未请求启动同步关机。
  * 1：主协调器请求启动同步关机。
* 位4: 主动唤醒位。
  * 0：节点未唤醒网络（被动唤醒）。
  * 1：节点已唤醒网络（主动唤醒）。
* 位5：保留用于将来的扩展。默认为0。
* 位6：部分网络信息位 (PNI)。
  * 0：NM消息不包含部分网络（**Partial Network**）请求信息。
  * 1：NM消息包含部分网络（**Partial Network**）请求信息。
* 位7：保留用于将来的扩展。默认为0。

控制位向量在初始化为**0x00**。

除非**UDPNM_PDU_NID_POSITION**设置为关闭，否则源节点标识符应使用配置参数**UDPNM_NODE_ID**设置。

如果**UdpNmActiveWakeupBitEnabled**参数为**TRUE**:

1. **UdpNm**由于调用 [**UdpNm_NetworkRequest**](#733-udpnm_networkrequest)（即由于主动唤醒）而执行从**Bus Sleep**状态或 **Prepare Bus Sleep**状态到**Network Mode**状态更改，则**UdpNm**需在CBV中设置**Active Wakeup Bit**。
2. **UdpNm**模块离开**Network Mode**，则**UdpNm**模块应清除CBV中的**Active Wakeup Bit**。

### 6.10. UdpNm API的功能需求

如果**UdpNmRepeatMsgIndEnabled**设置为**TRUE**且接收到设置为1的重复消息请求位，则**UdpNm**模块应调用回调函数**Nm_RepeatMessageIndication**。如果同时接收到部分网络学习位（**Partial Network Learning Bit**）且**UdpNmDynamicPncToChannelMappingEnabled**设置为**TRUE**，则该函数调用中的参数 **pnLearningBitSet** 应设置为**TRUE**，否则设置为**FALSE**。

### 6.11. 车辆唤醒

**NM-PDU**中车辆唤醒位（**Car Wakeup bit**）的位置由配置参数**UdpNmCarWakeUpBytePosition**和**UdpNmCarWakeUpBitPosition**定义。

针对无车辆唤醒过滤器的情况，如果满足下列的条件，**UdpNm**应调用**Nm_CarWakeUpIndication**，并执行标准接收指示处理。

* 接收到的任意**NM-PDU**中的车辆唤醒位为**1**，
* **UdpNmCarWakeUpRxEnabled**为**TRUE**，
* **UdpNmCarWakeUpFilterEnabled**为**FALSE**。

如果在**Nm_CarWakeUpIndication**的上下文中调用[**UdpNm_GetPduData**](#7312-udpnm_getpdudata)，并且**UdpNmNodeDetectionEnabled**或者**UdpNmUserDataEnabled**或者 **UdpNmNodeIdEnabled**设置为**TRUE**，**UdpNm**应返回引起 **Nm_CarWakeUpIndication**调用的PDU的数据。

**注意：**
这是使ECU识别有关车辆唤醒请求发送者的详细信息所必需的。

针对包含车辆唤醒过滤器的情况，如果满足下列的条件，**UdpNm**应调用**Nm_CarWakeUpIndication**，并执行标准接收指示处理。

* **UdpNmCarWakeUpFilterEnabled**为**TRUE**，
* 接收到的任意NM-PDU中的车辆唤醒位为**1**，
* **UdpNmCarWakeUpRxEnabled**为**TRUE**，
* 接收到的**NM-PDU**中的节点ID等于**UdpNmCarWakeUpFilterNodeId** 

注意：车辆唤醒过滤器是实现子网关（**sub gateway**）所必需的，它只考虑中央网关的车辆唤醒，以避免错误唤醒。

### 6.12. 错误分类

本节描述**UdpNm**模块在该基础软件的生命周期中必须如何管理可能发生的错误类别。

AUTOSAR的通用需求文档[5, General Requirements on Basic Software Modules]规定，所有基础软件模块必须（根据产品生命周期）区分两种错误类型：

* 开发错误（**Development errors**）：这些错误应在开发阶段被检测和修复。在大多数情况下，这些错误是软件错误。对于只应在开发期间发生的检测错误，可以针对生产代码将其关闭（通过静态配置，即预处理器开关）。
* 生产错误（**Production errors**）：这些错误是无法避免的硬件错误和软件异常，预计会出现在生产（即系列）代码中。这种错误通常被称为运行时错误（**run-time error**）。

#### 6.12.1. 开发错误

| 错误类型 | 相关错误码 | 错误值 |
| --- | --- | --- |
| 未进行模块初始化就使用API服务 | UDPNM_E_UNINIT | 0x01 |
| 使用错误的通道句柄调用API服务 | UDPNM_E_INVALID_CHANNEL | 0x02 |
| 使用错误的PDU ID调用API服务。 | UDPNM_E_INVALID_PDUID | 0x03 |
| **UdpNm**初始化失败，例如所选的配置集不存在 | UDPNM_E_INIT_FAILED | 0x04 |
| 空指针作为参数传入 | UDPNM_E_PARAM_POINTER | 0x12 |

开发错误不应由API函数返回；如果发生开发错误，相应的API函数将在适用的情况下返回**E_NOT_OK**。

#### 6.12.2. 运行时错误

| 错误类型 | 相关错误码 | 错误值 |
| --- | --- | --- |
| NM超时计时器在就绪睡眠状态（**Ready Sleep State**）之外超时（在重复消息状态或正常操作状态中） | UDPNM_E_NETWORK_TIMEOUT | 0x11 |
| 在由**ComM PNC**网关主动协调的通道上接收到设置了**PN**关闭请求位的**NM**消息。 | UDPNM_E_INVALID_PN_SYNC_SHUTDOWN_REQUEST | 0x20 |

当NM超时计时器在重复消息状态中超时，**UdpNm**模块应向默认错误跟踪器（**Default Error Tracer**）报告运行时错误**UDPNM_E_NETWORK_TIMEOUT**。

当NM超时计时器在正常操作状态中超时，**UdpNm**模块应向默认错误跟踪器报告运行时错误**UDPNM_E_NETWORK_TIMEOUT**。

#### 6.12.3. 瞬态故障

没有瞬态故障。

#### 6.12.4. 生产错误

没有生产错误。

#### 6.12.5. 扩展生产错误

没有扩展生产错误。

### 6.13. 主函数的调度

详情请参阅SWS_BSWGeneral中的章节8.5「调度函数」（**Scheduled functions**）。

### 6.14. 应用注释

#### 6.14.1. 唤醒通知

唤醒通知在**ECU**状态管理器规范[10, Specification of ECU State Manager]中有详细定义。

#### 6.14.2. 耦合网络的协调

需通过使用配置参数**UdpNmBusSynchronizationEnabled**开关（配置参数）进行静态配置，来支持按需的总线同步。

**注意：**

由于**UdpNm**的关闭可以随时进行，所以不支持调用API **Nm_SynchronizationPoint**。

### 6.15. 版本检查

详情请参阅SWS_BSWGeneral中的章节5.1.8「版本检查」（**Version Check**）。

### 6.16. 参数检查

如果通过**UDPNM_DEV_ERROR_DETECT**（配置参数）启用了开发错误检测，则每次**UDP NM API**服务调用都应对所有输入参数执行有效性检查。

参数类型检查应在编译时执行；如果类型不匹配，应停止编译过程，并在编译器支持的范围内返回相应的编译警告或错误。

参数值检查（针对常量值的参数）应在配置时执行；如果该值无效，应停止配置过程并报告相应的配置错误。

参数值检查（针对变量值的参数）应在执行时执行；如果该值无效，应拒绝执行服务并报告相应的开发错误。

### 6.17. 安全事件

该模块不报告安全事件。

## 7. API规范

**UdpNm**模块应拒绝执行使用无效参数调用的服务，并通知**DET**。

**AUTOSAR UdpNm API**由若干服务组成，这些服务是**UDP**特定的，可以在需要时随时调用；除[**UdpNm_Init**](#731-udpnm_init)外，每个服务仅针对一个**NM**通道。

生产错误不应由API函数返回；如果发生生产错误，相应的API函数将在适用的情况下返回**E_NOT_OK**。

当使用无效的网络句柄调用NM API服务时，被调用的函数不应执行，而是向默认错误跟踪器（**Default Error Tracer**）报告[**UDPNM_E_INVALID_CHANNEL**](#6121-开发错误)（如果启用了开发错误检测），否则向调用函数返回**E_NOT_OK**。

**注意：**

网络句柄无效是指它与允许的配置值不同。

当向**UDP Nm**服务传递了空指针时，被调用的函数不应执行，并在适用的情况下向调用函数返回**E_NOT_OK**。如果启用了开发错误检测（**UdpNmDevErrorDetect**设置为**TRUE**），则应向**DET**报告相应的错误[**UDPNM_E_PARAM_POINTER**](#6121-开发错误)。

当使用无效的**Pdu ID**调用**UdpNm**回调通知时，被调用的函数不应执行，并在可能的情况下返回**E_NOT_OK**。如果启用了开发错误检测，则**UdpNm**还应向默认错误跟踪器报告[**UDPNM_E_INVALID_PDUID**](#6121-开发错误)。

如果启用了**UdpNmComUserDataSupport**且**UdpNm**用户数据长度与被引用**I-PDU**的长度不匹配，则应在生成时报告错误。

**注意：**空指针检查在BSW General [3, General Specification of Basic Software Modules]中规定。

### 7.1. 导入的类型

导入以下 **Std_Types.h** 的类型：

boolean、uint8、uint16、uint32

| 模块 | 头文件 | 导入的类型 |
| --- | --- | --- |
| ComStack_Types | ComStack_Types.h | NetworkHandleType |
| ComStack_Types | ComStack_Types.h | PduIdType |
| ComStack_Types | ComStack_Types.h | PduInfoType |
| ComStack_Types | ComStack_Types.h | PduLengthType |
| Nm | NmStack_types.h | Nm_ModeType |
| Nm | NmStack_types.h | Nm_StateType |
| Std | Std_Types.h | Std_ReturnType |
| Std | Std_Types.h | Std_VersionInfoType |

### 7.2. 类型定义

#### 7.2.1. UdpNm_ConfigType

该类型应包含容器 **UdpNm_GlobalConfig** 及其子容器的参数。结构类型（**Structure**），元素为实现特定（**implementation specific**）。可通过**UdpNm.h**获得。

#### 7.2.2. UdpNm_PduPositionType

枚举类型（**Enumeration**），用于定义控制位向量在**NM**数据包（**NM PACKET**）中的位置。取值范围：**UDPNM_PDU_BYTE_0**（0x00，使用字节0）；**UDPNM_PDU_BYTE_1**（0x01，使用字节1）；**UDPNM_PDU_OFF**（0xFF，不使用节点标识）。可通过**UdpNm.h**获得。

### 7.3. 函数定义

#### 7.3.1. UdpNm_Init

**说明**: 初始化完整的 **UdpNm** 模块，即：配置时激活的所有通道都被初始化。并通过**TCP/IP**堆栈设置**UDP**套接字。注意事项（**Caveats**）：该函数必须在**TCP/IP**堆栈初始化之后调用。配置（**Configuration**）：必需（**Mandatory**）。可通过**UdpNm.h**获得。本服务为同步调用，不可重入。参数 UdpNmConfigPtr（in）：指向所选配置结构的指针。该服务无返回值。

```C
void UdpNm_Init( const UdpNm_ConfigType* UdpNmConfigPtr )
```

如果必须向**DET**指示错误，则应使用值0x00作为实例ID（**instance id**）。

**论据：**值0x00不是错误值，而是实例ID。

#### 7.3.2. UdpNm_PassiveStartUp

**说明**: **AUTOSAR UdpNm**的被动启动。它触发从总线睡眠模式（**Bus-Sleep Mode**）或准备总线睡眠模式（**Prepare Bus Sleep Mode**）到重复消息状态（**Repeat Message State**）的网络模式（**Network Mode**）的转换。注意事项（**Caveats**）：**UdpNm**已被正确初始化。可通过**UdpNm.h**获得。本服务为异步调用，可重入（但对于同一**NM**通道不可重入）。参数 nmChannelHandle（in）：**NM**通道的标识。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：网络管理的被动启动已失败。

```C
Std_ReturnType UdpNm_PassiveStartUp( NetworkHandleType nmChannelHandle )
```

如果在网络模式（**Network Mode**）中调用**UdpNm_PassiveStartUp**，则**UdpNm**模块不应执行该服务，并应返回**E_NOT_OK**。

#### 7.3.3. UdpNm_NetworkRequest

**说明**: 请求网络，因为**ECU**需要在总线上通信。网络状态应更改为「已请求」（**requested**）。注意事项（**Caveats**）：**UdpNm**已被正确初始化。配置（**Configuration**）：可选（仅在 **UdpNmPassiveModeEnabled** == false 时可用）。可通过**UdpNm.h**获得。本服务为异步调用，可重入（但对于同一**NM**通道不可重入）。参数 nmChannelHandle（in）：**NM**通道的标识。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：网络的请求已失败。

```C
Std_ReturnType UdpNm_NetworkRequest( NetworkHandleType nmChannelHandle )
```

#### 7.3.4. UdpNm_NetworkRelease

**说明**: 释放网络，因为**ECU**不必在总线上通信。网络状态应更改为「已释放」（**released**）。注意事项（**Caveats**）：**UdpNm**已被正确初始化。可通过**UdpNm.h**获得。本服务为异步调用，可重入（但对于同一**NM**通道不可重入）。参数 nmChannelHandle（in）：**NM**通道的标识。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：网络的释放已失败。

```C
Std_ReturnType UdpNm_NetworkRelease( NetworkHandleType nmChannelHandle )
```

#### 7.3.5. UdpNm_DisableCommunication

**说明**: 由于 **ISO14229** 通信控制（0x28）服务而禁用 **NM PDU** 传输能力。注意事项（**Caveats**）：**UdpNm**已被正确初始化。可通过**UdpNm.h**获得。本服务为异步调用，可重入（但对于同一**NM**通道不可重入）。参数 nmChannelHandle（in）：**NM**通道的标识。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：**NM PDU**传输能力的禁用已失败。

```C
Std_ReturnType UdpNm_DisableCommunication( NetworkHandleType nmChannelHandle )
```

如果模块在被动模式（**UdpNmPassiveModeEnabled**）下运行，则服务 **UdpNm_DisableCommunication** 应没有任何效果，并直接返回 **E_NOT_OK**。

#### 7.3.6. UdpNm_EnableCommunication

**说明**: 由于 **ISO14229** 通信控制（0x28）服务而启用 **NM PDU** 传输能力。注意事项（**Caveats**）：**UdpNm**已被正确初始化。可通过**UdpNm.h**获得。本服务为异步调用，可重入（但对于同一**NM**通道不可重入）。参数 nmChannelHandle（in）：**NM**通道的标识。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：**NM PDU**传输能力的启用已失败。

```C
Std_ReturnType UdpNm_EnableCommunication( NetworkHandleType nmChannelHandle )
```

可选服务 **UdpNm_EnableCommunication** 应在 **NM PDU** 传输能力被禁用时启用 **NM PDU** 传输能力。

可选服务 **UdpNm_EnableCommunication** 应在调用该服务时 **NM PDU** 传输能力已启用的情况下返回 **E_NOT_OK**。

如果当前模式不是网络模式（**Network Mode**），则服务 **UdpNm_EnableCommunication** 应返回 **E_NOT_OK**。

如果模块在被动模式（**UdpNmPassiveModeEnabled** 为 **TRUE**）下运行，则服务 **UdpNm_EnableCommunication** 应没有任何效果，并直接返回 **E_NOT_OK**。

#### 7.3.7. UdpNm_SetUserData

**说明**: 在此函数无错误返回后，为总线上传输的所有 **NM 消息**（**NM messages**）设置用户数据。注意事项（**Caveats**）：**UdpNm**已被正确初始化。配置（**Configuration**）：可选（仅在 **UdpNmUserDataEnabled**==true 且 **UdpNmPassiveModeEnabled**==false 时可用）。可通过**UdpNm.h**获得。本服务为同步调用，不可重入。参数 nmChannelHandle（in）：**NM**通道的标识；参数 nmUserDataPtr（in）：指向的地址，下一条传输的**NM**消息的用户数据将从该处复制。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：用户数据的设置已失败。

```C
Std_ReturnType UdpNm_SetUserData(
  NetworkHandleType nmChannelHandle, const uint8* nmUserDataPtr )
```

#### 7.3.8. UdpNm_GetUserData

**说明**: 从最近收到的 **NM 消息**（**NM messages**）中获取用户数据。注意事项（**Caveats**）：**UdpNm**已被正确初始化。配置（**Configuration**）：可选（仅在 **UdpNmUserDataEnabled** == true 时可用）。可通过**UdpNm.h**获得。本服务为同步调用，不可重入。参数 nmChannelHandle（in）：**NM**通道的标识；参数 nmUserDataPtr（out）：指向的地址，最近接收的**NM**消息中的用户数据将复制到该处。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：用户数据的获取已失败。

```C
Std_ReturnType UdpNm_GetUserData(
  NetworkHandleType nmChannelHandle, uint8* nmUserDataPtr )
```

#### 7.3.9. UdpNm_GetNodeIdentifier

**说明**: 从最近收到的 **NM PDU** 中获取节点标识符。可通过**UdpNm.h**获得。本服务为同步调用，可重入。参数 nmChannelHandle（in）：**NM**通道的标识；参数 nmNodeIdPtr（out）：指向的地址，最近接收的**NM PDU**中的源节点标识符将复制到该处。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：从最近接收的**NM PDU**中获取节点标识符已失败，或未针对此网络句柄配置。

```C
Std_ReturnType UdpNm_GetNodeIdentifier(
  NetworkHandleType nmChannelHandle, uint8* nmNodeIdPtr )
```

如果 **UdpNmNodeIdEnabled** 设置为 **TRUE**，则服务调用 **UdpNm_GetNodeIdentifier** 应提供最近接收的网络管理 **PDU** 中的节点标识符。

#### 7.3.10. UdpNm_GetLocalNodeIdentifier

**说明**: 获取为本地节点（**local node**）配置的节点标识符。可通过**UdpNm.h**获得。本服务为同步调用，可重入。参数 nmChannelHandle（in）：**NM**通道的标识；参数 nmNodeIdPtr（out）：指向的地址，本地节点的节点标识符将复制到该处。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：获取本地节点的节点标识符已失败，或未针对此网络句柄配置。

```C
Std_ReturnType UdpNm_GetLocalNodeIdentifier(
  NetworkHandleType nmChannelHandle, uint8* nmNodeIdPtr )
```

如果 **UdpNmNodeIdEnabled** 设置为 **TRUE**，则服务调用 **UdpNm_GetLocalNodeIdentifier** 应提供为本地主机节点配置的节点标识符。

#### 7.3.11. UdpNm_RepeatMessageRequest

**说明**: 在此函数无错误返回后，为总线上传输的所有**NM**消息设置重复消息请求位（**Repeat Message Request Bit**）。可通过**UdpNm.h**获得。本服务为异步调用，可重入（但对于同一**NM**通道不可重入）。参数 nmChannelHandle（in）：**NM**通道的标识。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：重复消息请求位的设置已失败，或未针对此网络句柄配置。

```C
Std_ReturnType UdpNm_RepeatMessageRequest(
  NetworkHandleType nmChannelHandle )
```

如果在重复消息状态（**Repeat Message State**）、准备总线睡眠模式（**Prepare Bus-Sleep Mode**）或总线睡眠模式（**Bus-Sleep Mode**）中调用服务 **UdpNm_RepeatMessageRequest**，则 **UdpNm** 模块不应执行该服务并返回 **E_NOT_OK**。

#### 7.3.12. UdpNm_GetPduData

**说明**: 从最近收到的 **NM 消息**中获取整个 **PDU** 数据。注意事项（**Caveats**）：**UdpNm**已被正确初始化。可通过**UdpNm.h**获得。本服务为同步调用，可重入。参数 nmChannelHandle（in）：**NM**通道的标识；参数 nmPduDataPtr（out）：指向的地址，**NM PDU** 将复制到该处。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：**NM PDU** 数据的获取已失败，或未针对此网络句柄配置。

```C
Std_ReturnType UdpNm_GetPduData(
  NetworkHandleType nmChannelHandle, uint8* nmPduDataPtr )
```

如果 **UdpNmNodeDetectionEnabled** 或 **UdpNmUserDataEnabled** 或 **UdpNmNodeIdEnabled** 设置为 **TRUE**，则服务调用 **UdpNm_GetPduData** 应提供最近接收的网络管理 **PDU** 的完整有效载荷（源节点ID、控制位向量和用户数据）。

#### 7.3.13. UdpNm_GetState

**说明**: 返回网络管理的状态和模式。注意事项（**Caveats**）：**UdpNm**已被正确初始化。可通过**UdpNm.h**获得。本服务为同步调用，可重入。参数 nmChannelHandle（in）：**NM**通道的标识；参数 nmStatePtr（out）：指向的地址，网络管理的状态将复制到该处；参数 nmModePtr（out）：指向的地址，网络管理的模式将复制到该处。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：**NM** 状态的获取已失败。

```C
Std_ReturnType UdpNm_GetState(
  NetworkHandleType nmChannelHandle,
  Nm_StateType* nmStatePtr,
  Nm_ModeType* nmModePtr )
```

#### 7.3.14. UdpNm_GetVersionInfo

**说明**: 该服务返回该模块的版本信息。可通过**UdpNm.h**获得。本服务为同步调用，可重入。参数 versioninfo（out）：指向存储该模块版本信息的位置的指针。该服务无返回值。

```C
void UdpNm_GetVersionInfo( Std_VersionInfoType* versioninfo )
```

如果 **UdpNm** 模块启用了 **DET**，则当参数 versioninfo 为 **NULL** 指针时，函数 **UdpNm_GetVersionInfo** 应引发 [**UDPNM_E_PARAM_POINTER**](#6121-开发错误) 并不做任何操作直接返回。

#### 7.3.15. UdpNm_RequestBusSynchronization

**说明**: 请求总线同步。注意事项（**Caveats**）：**UdpNm**已被正确初始化。配置（**Configuration**）：可选（仅在 **UdpNmBusSynchronizationEnabled**==true 且 **UdpNmPassiveModeEnabled**==false 时可用）。可通过**UdpNm.h**获得。本服务为异步调用，不可重入。参数 nmChannelHandle（in）：**NM**通道的标识。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：总线同步的请求已失败。

```C
Std_ReturnType UdpNm_RequestBusSynchronization( NetworkHandleType nmChannelHandle )
```

如果 **UdpNmPassiveModeEnabled**（配置参数）为 **FALSE**，则服务调用 **UdpNm_RequestBusSynchronization** 应触发单个网络管理 **PDU** 的传输。

**论据：**该服务通常用于支持 **NM** 网关扩展。

如果在总线睡眠模式（**BusSleep Mode**）和准备总线睡眠模式（**Prepare Bus-Sleep Mode**）中调用 **UdpNm_RequestBusSynchronization**，则 **UdpNm** 模块不应执行该服务，并应返回 **E_NOT_OK**。

#### 7.3.16. UdpNm_CheckRemoteSleepIndication

**说明**: 检查远程睡眠指示是否发生。注意事项（**Caveats**）：**UdpNm**已被正确初始化。可通过**UdpNm.h**获得。本服务为同步调用，可重入（但对于同一**NM**通道不可重入）。参数 nmChannelHandle（in）：**NM**通道的标识；参数 NmRemoteSleepIndPtr（out）：指向的地址，远程睡眠指示的检查结果将复制到该处。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：远程睡眠指示位的检查已失败。

```C
Std_ReturnType UdpNm_CheckRemoteSleepIndication( NetworkHandleType nmChannelHandle, boolean* NmRemoteSleepIndPtr )
```

服务调用 **UdpNm_CheckRemoteSleepIndication** 应提供关于远程睡眠指示（**Remote Sleep Indication**）当前状态的信息（即是否已检测到）。

#### 7.3.17. UdpNm_SetSleepReadyBit

**说明**: 设置控制位向量（**CBV**）中的 **NM** 协调器睡眠就绪位。可通过**UdpNm.h**获得。本服务为同步调用，不可重入。参数 nmChannelHandle（in）：**NM**通道的标识；参数 nmSleepReadyBit（in）：写入 **CBV** 中 **ReadySleep** 位的值。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：远程睡眠指示位的写入已失败。

```C
Std_ReturnType UdpNm_SetSleepReadyBit(
  NetworkHandleType nmChannelHandle, boolean nmSleepReadyBit )
```

#### 7.3.18. UdpNm_Transmit

**说明**: 请求传输 **PDU**。可通过**UdpNm.h**获得。本服务为同步调用，对于不同的 **PduId** 可重入，对于相同的 **PduId** 不可重入。参数 TxPduId（in）：要传输的 **PDU** 的标识符；参数 PduInfoPtr（in）：**PDU** 数据的长度和指针以及指向 **MetaData** 的指针。返回值为**Std_ReturnType**：E_OK：传输请求已被接受；E_NOT_OK：传输请求未被接受。

```C
Std_ReturnType UdpNm_Transmit(
  PduIdType TxPduId, const PduInfoType* PduInfoPtr )
```

如果 **UdpNmComUserDataSupport** 或 **UdpNmPnEnabled** 被启用，则 **UdpNm** 实现应提供API **UdpNm_Transmit**。

#### 7.3.19. UdpNm_PnLearningRequest

**说明**: 为总线上接下来传输的**NM**消息设置重复消息请求位和部分网络学习位。这将强制总线上的所有节点进入 **PNC** 学习阶段（**PNC Learning Phase**）。这是可选的动态 **PNC** 到通道映射（**Dynamic PNC-to-channel-mapping**）功能所需要的。可通过**UdpNm.h**获得。本服务为异步调用，可重入（但对于同一**NM**通道不可重入）。参数 nmChannelHandle（in）：**NM**通道的标识。返回值为**Std_ReturnType**：E_OK：无错误；E_NOT_OK：**PN**学习请求已失败，或未针对此网络句柄配置。

```C
Std_ReturnType UdpNm_PnLearningRequest( NetworkHandleType nmChannelHandle )
```

如果在「准备总线睡眠模式」（**Prepare Bus-Sleep Mode**）或「总线睡眠模式」（**Bus Sleep Mode**）中调用函数 **UdpNm_PnLearningRequest**，则不应执行任何功能，并应返回 **E_NOT_OK**。

只有当 **UdpNmDynamicPncToChannelMappingSupport** 设置为 **TRUE** 时，函数 **UdpNm_PnLearningRequest** 才可用。

#### 7.3.20. UdpNm_ActivateTxPnShutdownMsg

**说明**: **NM**指示激活给定**NM**通道上**PN**关闭消息的传输。这将导致传输 **PNSR** 位设置为1的 **NM-PDU**（**PN**关闭消息）。可通过**UdpNm.h**获得。本服务为同步调用，对于不同的nmChannelHandle可重入，对于相同的nmChannelHandle不可重入。参数 nmChannelHandle（in）：启动 **PNC** 关闭过程的 **NM** 通道的标识符。返回值为**Std_ReturnType**：E_OK：请求已被接受；E_NOT_OK：请求未被接受。

```C
Std_ReturnType UdpNm_ActivateTxPnShutdownMsg( NetworkHandleType nmChannelHandle )
```

如果 **UdpNmSynchronizedPncShutdownEnabled** 设置为 **TRUE**，则 **UdpNm** 实现应提供API **UdpNm_ActivateTxPnShutdownMsg**。

如果 **UdpNmSynchronizedPncShutdownEnabled** 设置为 **TRUE**，且使用有效的 **NM** 通道（nmChannelHandle）调用 **UdpNm_ActivateTxPnShutdownMsg**，则 **UdpNm** 模块应将 **PN** 关闭消息传输视为在给定 **NM** 通道上处于活动状态，将 **CBV** 中的 **PNSR** 位设置为1，并以 **E_OK** 返回。

#### 7.3.21. UdpNm_DeactivateTxPnShutdownMsg

**说明**: **NM**指示停用给定**NM**通道上**PN**关闭消息的传输。这将导致传输 **PNSR** 位设置为0的普通 **NM-PDU**。可通过**UdpNm.h**获得。本服务为同步调用，对于不同的nmChannelHandle可重入，对于相同的nmChannelHandle不可重入。参数 nmChannelHandle（in）：停止 **PNC** 关闭过程的 **NM** 通道的标识符。返回值为**Std_ReturnType**：E_OK：请求已被接受；E_NOT_OK：请求未被接受。

```C
Std_ReturnType UdpNm_DeactivateTxPnShutdownMsg( NetworkHandleType nmChannelHandle )
```

如果 **UdpNmSynchronizedPncShutdownEnabled** 设置为 **TRUE**，则 **UdpNm** 实现应提供API **UdpNm_DeactivateTxPnShutdownMsg**。

如果 **UdpNmSynchronizedPncShutdownEnabled** 设置为 **TRUE**，且使用有效的 **NM** 通道（nmChannelHandle）调用 **UdpNm_DeactivateTxPnShutdownMsg**，则 **UdpNm** 模块应将 **PN** 关闭消息传输视为在给定 **NM** 通道上处于非活动状态，将 **CBV** 中的 **PNSR** 位设置为0，并以 **E_OK** 返回。

#### 7.3.22. UdpNm_RepeatMessageIndication

**说明**: 指示已接收到设置了重复消息请求位的**NM**消息的服务。这是节点检测和 **PNC** 动态学习所需要的。本服务为异步调用，可重入。参数 nmNetworkHandle（in）：**NM**通道的标识。该服务无返回值、无输出参数。

```C
void UdpNm_RepeatMessageIndication( NetworkHandleType nmNetworkHandle )
```

### 7.4. 回调通知

#### 7.4.1. UdpNm_SoAdIfTxConfirmation

**说明**: 下层通信接口模块确认**PDU**的传输，或者**PDU**的传输失败。可通过**UdpNm.h**获得。本服务为同步调用，对于不同的 **PduId** 可重入，对于相同的 **PduId** 不可重入。参数 TxPduId（in）：已传输的 **PDU** 的ID；参数 result（in）：E_OK：**PDU**已传输；E_NOT_OK：**PDU**传输失败。该服务无返回值。

```C
void UdpNm_SoAdIfTxConfirmation( PduIdType TxPduId, Std_ReturnType result )
```

**注意：**回调函数 **UdpNm_SoAdIfTxConfirmation** 由 **SoAd** 调用，由 **UdpNm** 模块实现。

**注意：**回调函数 **UdpNm_SoAdIfTxConfirmation** 根据上下文要么在中断级（中断模式）被调用，要么在任务级（轮询模式）被调用。

通过API参数 TxPduId 传递给 **UdpNm** 的值应引用 **NM** 通道句柄，即不需要从 **PduId** 到 **NM** 通道句柄的映射。

如果启用了 **UdpNmComUserDataSupport**，则 **UdpNm** 应在由 **SoAd** 调用的消息传输确认函数 **UdpNm_SoAdIfTxConfirmation** 内，以 **SoAd** 传递的结果调用 **PduR_UdpNmTxConfirmation**。

#### 7.4.2. UdpNm_SoAdIfRxIndication

**说明**: 指示从较低层通信接口模块接收到的 **PDU**。可通过**UdpNm.h**获得。本服务为同步调用，对于不同的 **PduId** 可重入，对于相同的 **PduId** 不可重入。参数 RxPduId（in）：接收到的 **PDU** 的ID；参数 PduInfoPtr（in）：包含接收到的 **PDU** 的长度（**SduLength**）、指向包含该 **PDU** 的缓冲区的指针（**SduDataPtr**）以及与该 **PDU** 相关的 **MetaData**。该服务无返回值。

```C
void UdpNm_SoAdIfRxIndication(
  PduIdType RxPduId, const PduInfoType* PduInfoPtr )
```

回调函数 **UdpNm_SoAdIfRxIndication** 由 **SoAd** 调用，由 **UdpNm** 模块实现。它在 **SoAd** 的接收指示事件发生时被调用。

通过API参数 udpNmRxPduId 传递给 **UdpNm** 的值应引用 **UdpNm** 通道句柄，即不需要从 **PduId** 到 **UdpNm** 通道句柄的映射。

#### 7.4.3. UdpNm_SoAdIfTriggerTransmit

**说明**: 在此API中，上层模块将检查可用数据是否适合**PduInfoPtr->SduLength**报告的缓冲区大小。 如果合适，它将其数据复制到**PduInfoPtr->SduDataPtr**提供的缓冲区中，并更新实际复制数据的长度到**PduInfoPtr->SduLength**中。 如果不是，则返回**E_NOT_OK**而不更改**PduInfoPtr**。可通过**UdpNm.h**获得。本服务为同步调用，对于不同的 **PduId** 可重入，对于相同的 **PduId** 不可重入。参数 TxPduId（in）：请求传输的 **SDU** 的ID；参数 PduInfoPtr（inout）：包含指向缓冲区的指针（**SduDataPtr**，**SDU** 数据应复制到该缓冲区）以及 **SduLength** 中的可用缓冲区大小。返回时，该服务将在 **SduLength** 中指示复制的 **SDU** 数据的长度。返回值为**Std_ReturnType**：E_OK：**SDU**已被复制，**SduLength**指示已复制的字节数；E_NOT_OK：未复制任何 **SDU** 数据，不得使用 **PduInfoPtr**，因为它可能包含 **NULL** 指针或指向无效数据。

```C
Std_ReturnType UdpNm_SoAdIfTriggerTransmit(
  PduIdType TxPduId, PduInfoType* PduInfoPtr )
```

**注意：**在调用 **UdpNm_TriggerTransmit** 时不会更新 **PNC** 位向量，而是在每个 **NM** 消息传输请求之前更新。这确保了独立于 **SoAdTxPduTriggerTransmit** 设置（**TRUE** 或 **FALSE**）的统一处理。

如果调用了 **UdpNm_SoAdIfTriggerTransmit** 且 **UdpNmComUserDataSupport** 被启用，则 **UdpNm** 应通过调用 **PduR_UdpNmTriggerTransmit** 从被引用的 **NM I-PDU** 中收集 **NM** 用户数据，并将数据复制到 **NM-PDU** 的用户数据范围。

函数 **UdpNm_SoAdIfTriggerTransmit** 应复制由 TxPduId 请求的相应 **NM PDU** 的 **NM PDU** 数据。

**注意：**函数 **UdpNm_SoAdIfTriggerTransmit** 可能会由 **SoAd** 在中断上下文中调用。

### 7.5. 调度函数

#### 7.5.1. UdpNm_MainFunction_&lt;Instance Id&gt;

**说明**: 处理本文档中所描述算法的 **UdpNm** 主函数。例如：**UdpNm_MainFunction_0()** 表示 **UDP** 通道0的 **UdpNm** 实例；**UdpNm_MainFunction_1()** 表示 **UDP** 通道1的 **UdpNm** 实例。可通过**SchM_UdpNm.h**获得。该服务无返回值。

```C
void UdpNm_MainFunction<Instance_Id>( void )
```

### 7.6. 期望接口

在本章中列出了从其他模块所需的所有接口。

#### 7.6.1. 必需接口

本节定义了实现该模块核心功能所需的所有接口。

| API函数 | 头文件 | 说明 |
| --- | --- | --- |
| Det_ReportRuntimeError | Det.h | 报告运行时错误的服务。如果已配置回调（callout），则应调用该回调。 |
| Nm_BusSleepMode | Nm.h | 通知网络管理已进入总线睡眠模式（**Bus-Sleep Mode**）。 |
| Nm_NetworkMode | Nm.h | 通知网络管理已进入网络模式（**Network Mode**）。 |
| Nm_NetworkStartIndication | Nm.h | 通知在总线睡眠模式（**Bus-Sleep Mode**）中收到了**NM**消息，这表明网络中的某些节点已经进入了网络模式（**Network Mode**）。 |
| Nm_PrepareBusSleepMode | Nm.h | 通知网络管理已进入准备总线睡眠模式（**Prepare Bus-Sleep Mode**）。 |
| SoAd_IfTransmit | SoAd.h | 请求传输**PDU**。 |

#### 7.6.2. 可选接口

本节定义了实现该模块可选功能所需的所有接口。

| API函数 | 头文件 | 说明 |
| --- | --- | --- |
| Det_ReportError | Det.h | 报告开发错误的服务。 |
| Nm_CarWakeUpIndication | Nm.h | 该函数由&lt;Bus&gt;Nm调用，以指示接收到 **CWU** 请求。 |
| Nm_CoordReadyToSleepCancellation | Nm.h | 当控制位向量中的 **NM Coordinator Sleep Ready** 位被重新设置为0时，取消指示。 |
| Nm_CoordReadyToSleepIndication | Nm.h | 当控制位向量中的 **NM Coordinator Sleep Ready** 位被设置时，设置指示。 |
| Nm_ForwardSynchronizedPncShutdown | Nm.h | 通知网络管理已在特定**NM**通道上接收到**PN**关闭消息。这用于实现跨整个**PN**拓扑的近乎同步的**PNC**关闭。 |
| Nm_PduRxIndication | Nm.h | 通知已接收到**NM**消息。 |
| Nm_PncBitVectorRxIndication | Nm.h | 指示总线特定的网络管理已在特定**NM**通道上接收到包含**PNC**位向量的**NM**消息。这用于聚合外部**PNC**请求。该函数评估给定的**PNC**位向量中是否存在相关的**PNC**请求（**PNC**位设置为「1」）。如果存在相关的**PNC**请求（**PNC**位通过**PNC**位向量过滤器），则 **RelevantPncRequestDetectedPtr** 引用一个设置为 **TRUE** 的布尔值；否则引用一个设置为 **FALSE** 的布尔值。被调用的&lt;Bus&gt;Nm模块会评估 **RelevantPncRequestDetectedPtr**，以限定对接收到的 **NM-PDU** 的进一步处理。 |
| Nm_PncBitVectorTxConfirmation | Nm.h | 由&lt;Bus&gt;Nm调用的函数，用于确认给定**NM**通道上给定**PNC**位向量的传输状态。 |
| Nm_PncBitVectorTxIndication | Nm.h | 由&lt;Bus&gt;Nm调用的函数，用于请求聚合的内部**PNC**请求以便在**Nm**消息中传输。 |
| Nm_RemoteSleepCancellation | Nm.h | 通知网络管理已检测到并非网络上所有其他节点都仍然准备好进入总线睡眠模式（**Bus-Sleep Mode**）。 |
| Nm_RemoteSleepIndication | Nm.h | 通知网络管理已检测到网络上的所有其他节点都准备好进入总线睡眠模式（**Bus-Sleep Mode**）。 |
| Nm_RepeatMessageIndication | Nm.h | 指示已接收到设置了重复消息请求位的**NM**消息的服务。这是节点检测和动态**PNC**到通道映射功能所需要的。 |
| Nm_StateChangeNotification | Nm.h | 通知下层&lt;Bus&gt;Nm的状态已发生变化。 |
| Nm_TxTimeoutException | Nm.h | 指示发送**NM**消息的尝试失败的服务。 |
| PduR_UdpNmRxIndication | PduR_UdpNm.h | 指示从较低层通信接口模块接收到的**PDU**。 |
| PduR_UdpNmTriggerTransmit | PduR_UdpNm.h | 在此API中，上层模块将检查可用数据是否适合**PduInfoPtr->SduLength**报告的缓冲区大小。如果合适，它将其数据复制到**PduInfoPtr->SduDataPtr**提供的缓冲区中，并在**PduInfoPtr->SduLength**中更新实际复制数据的长度。如果不是，则返回**E_NOT_OK**而不更改**PduInfoPtr**。 |
| PduR_UdpNmTxConfirmation | PduR_UdpNm.h | 下层通信接口模块确认**PDU**的传输，或者**PDU**的传输失败。 |

#### 7.6.3. 可配置接口

不适用（**Not applicable**）。

### 7.7. 服务接口

不适用（**Not applicable**）。

### 7.8. UML状态图

下图显示了有关**API**规范的UML状态图。模式变更相关的转换以绿色表示，错误处理相关的转换以红色表示，可选的节点检测相关的转换以蓝色表示。

![Figure8_1.png](Figure8_1.png)

## 8. 时序图和转换表

### 8.1. UdpNm传输

![Figure9-1.png](Figure9-1.png)

### 8.2. UdpNm接收

| 调用方向 | 动作/判定 | 说明 |
| --- | --- | --- |
| SoAd->UdpNm | [UdpNm_SoAdIfRxIndication](#742-udpnm_soadifrxindication)() |  |

![Figure9-2.png](Figure9-2.png)

## 9. 配置规范

总体而言，本章定义配置参数及其到容器的聚类组织。为了支持本规范，第9.1节描述基础知识，并规定了应用于参数规范的模板（表）。我们有意将第9.1节保留在规范文档中以确保全面性。

第9.2节规定模块**UdpNm**的结构（容器）和参数。

第9.3节规定模块**UdpNm**的发布信息。

### 9.1. 阅读本章的方法

详情请参阅[\[3\]](#ref-3)中的章节10.1「配置规范简介」（**Introduction to configuration specification**）。

### 9.2. 容器与配置参数

本章定义的配置参数用于为**AUTOSAR**工具链创建数据模型。在代码中的实现是实现特定的。

配置参数分为：用于启用功能的参数、影响**UdpNm**所有实例的参数以及影响**UdpNm**各自实例的参数。

所有配置项都应位于模块内核之外。

容器**UdpNm_ChannelConfig**规定的配置参数应位于**UdpNm_ConfigType**类型的数据结构中。

容器**UdpNm_ChannelConfig**中列出的运行时可配置参数应针对每个**NM**集群单独进行配置。

#### 9.2.1. UdpNm

| SWS 条目 | [ECUC_UdpNm_00088] |
| --- | --- |
| 模块名称 | UdpNm |
| 描述 | **UdpNm**模块的配置。 |
| Post-Build 变体支持 | true |
| 支持的配置变体 | VARIANT-LINK-TIME, VARIANT-PRE-COMPILE |

| 包含的容器 | 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- | --- |
| 包含的容器 | UdpNmGlobalConfig | 1 | 该容器包含 **UDP NM** 的所有全局配置参数。这些参数以及子容器的参数应（在可能的情况下）映射到传递给 **UdpNm_Init** 函数的C数据类型 **UdpNm_ConfigType**。 |

#### 9.2.2. UdpNmGlobalConfig

| SWS 条目 | [ECUC_UdpNm_00001] |
| --- | --- |
| 容器名称 | UdpNmGlobalConfig |
| 父容器 | UdpNm |
| 描述 | 该容器包含 **UDP NM** 的所有全局配置参数。这些参数以及子容器的参数应（在可能的情况下）映射到传递给 **UdpNm_Init** 函数的C数据类型 **UdpNm_ConfigType**。 |
| 配置参数 | 见下方参数表 |

| SWS 条目 | [ECUC_UdpNm_00006] |
| --- | --- |
| 参数名称 | UdpNmBusSynchronizationEnabled |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用总线同步支持的预处理器开关。该功能仅网关节点需要。如果 **UdpNmPassiveModeEnabled**==true，则不得定义该参数。该参数应从 **NmBusSynchronizationEnabled** 派生。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00013] |
| --- | --- |
| 参数名称 | UdpNmComControlEnabled |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用通信控制（**Communication Control**）支持的预处理器开关。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: calculationFormula = If (UdpNmPassiveModeEnabled == False) then Equal(NmComControlEnabled) else Equal(False) |

| SWS 条目 | [ECUC_UdpNm_00055] |
| --- | --- |
| 参数名称 | UdpNmComUserDataSupport |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 启用/禁用用户数据支持。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 如果 **UdpNmPassiveModeEnabled** == **True**，或者**NM PDU**的所有字节都被**NM**系统字节和**PNC**位向量使用而没有为用户数据留下空间，则 **UdpNmComUserDataSupport** 应设置为 **False**。 |

| SWS 条目 | [ECUC_UdpNm_00059] |
| --- | --- |
| 参数名称 | UdpNmCoordinatorSyncSupport |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 启用/禁用协调器同步支持。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 如果 **UdpNmPassiveModeEnabled** 设置为 **TRUE**，则 **UdpNmCoordinatorSyncSupport** 必须设置为 **FALSE**。 |

| SWS 条目 | [ECUC_UdpNm_00002] |
| --- | --- |
| 参数名称 | UdpNmDevErrorDetect |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 开启或关闭开发错误检测与通知。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00094] |
| --- | --- |
| 参数名称 | UdpNmDynamicPncToChannelMappingSupport |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用动态**PNC**到通道映射处理的预编译开关。False：禁用动态**PNC**到通道映射；True：启用动态**PNC**到通道映射。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU；dependency: 仅当至少一个 **UdpNm** 通道的 **UdpNmPnEnabled** == true 且 **UdpNmPassiveModeEnabled** == false 时，才允许 **UdpNmDynamicPncToChannelMappingSupport** == **TRUE** |

| SWS 条目 | [ECUC_UdpNm_00009] |
| --- | --- |
| 参数名称 | UdpNmImmediateRestartEnabled |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于在准备总线睡眠模式中收到总线通信请求时立即传输**NM**数据包（**NM PACKET**）的预处理器开关。如果 **UdpNmPassiveModeEnabled**==true，则不得定义。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00014] |
| --- | --- |
| 参数名称 | UdpNmNumberOfChannels |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 一个**ECU**内允许的**NM**通道数量。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 1 .. 255 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00010] |
| --- | --- |
| 参数名称 | UdpNmPassiveModeEnabled |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用被动模式（**Passive Mode**）支持的预处理器开关。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00011] |
| --- | --- |
| 参数名称 | UdpNmPduRxIndicationEnabled |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用**PDU Rx**指示的预处理器开关。该参数应从 **NmPduRxIndicationEnabled** 派生。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00005] |
| --- | --- |
| 参数名称 | UdpNmRemoteSleepIndEnabled |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用远程睡眠指示支持的预处理器开关。该功能仅网关节点需要。如果 **UdpNmPassiveModeEnabled**==true，则不得定义该参数。该参数应从 **NmRemoteSleepIndEnabled** 派生。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00012] |
| --- | --- |
| 参数名称 | UdpNmStateChangeIndEnabled |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用 **UDP NM** 状态变化通知的预处理器开关。该参数应从 **NmStateChangeIndEnabled** 派生。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00004] |
| --- | --- |
| 参数名称 | UdpNmUserDataEnabled |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用用户数据支持的预处理器开关。该参数应从 **NmUserDataEnabled** 派生。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 如果**NM PDU**的所有字节都被**NM**系统字节和**PNC**位向量使用而没有为用户数据留下空间，则 **UdpNmUserDataEnabled** 应设置为 **FALSE**。否则，该参数应按照以下公式设置：calculationFormula = Equal(NmUserDataEnabled)。 |

| SWS 条目 | [ECUC_UdpNm_00003] |
| --- | --- |
| 参数名称 | UdpNmVersionInfoApi |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 用于启用版本信息**API**支持的预处理器开关。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

![Figure10-1.png](Figure10-1.png)

| 包含的容器 | 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- | --- |
| 包含的容器 | UdpNmChannelConfig | 1..* | 该容器包含 **UdpNm** 的通道特定配置参数。 |

#### 9.2.3. UdpNmChannelConfig

| SWS 条目 | [ECUC_UdpNm_00017] |
| --- | --- |
| 容器名称 | UdpNmChannelConfig |
| 父容器 | UdpNmGlobalConfig |
| 描述 | 该容器包含 **UdpNm** 的通道特定配置参数。 |
| 配置参数 | 见下方参数表 |

| SWS 条目 | [ECUC_UdpNm_00074] |
| --- | --- |
| 参数名称 | UdpNmActiveWakeupBitEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 启用/禁用 **UdpNm** 模块中对主动唤醒位（**Active Wakeup Bit**）的处理。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmPassiveModeEnabled** 为 **False** 时该参数有效。 |

| SWS 条目 | [ECUC_UdpNm_00089] |
| --- | --- |
| 参数名称 | UdpNmAllNmMessagesKeepAwake |
| 父容器 | UdpNmChannelConfig |
| 描述 | 规定 **UdpNm** 是否丢弃无关的 **NM PDU**。false：只有 **PNI** 位 = true 且包含针对本**ECU**的**PN**请求的 **NM PDU** 才触发标准的Rx指示处理；true：每个 **NM PDU** 都触发标准的Rx指示处理。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **NmPnEiraCalcEnabled** == true 或 **NmPnEraCalcEnabled** == true 时有效 |

| SWS 条目 | [ECUC_UdpNm_00087] |
| --- | --- |
| 参数名称 | UdpNmCarWakeUpBitPosition |
| 父容器 | UdpNmChannelConfig |
| 描述 | 规定 **CWU** 在 **NM PDU** 中的位位置。 |
| 多重性 | 0..1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 7 |
| 默认值 | - |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmCarWakeUpRxEnabled** == **TRUE** 时可用 |

| SWS 条目 | [ECUC_UdpNm_00086] |
| --- | --- |
| 参数名称 | UdpNmCarWakeUpBytePosition |
| 父容器 | UdpNmChannelConfig |
| 描述 | 规定 **CWU** 在 **NM PDU** 中的字节位置。 |
| 多重性 | 0..1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 7 |
| 默认值 | - |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmCarWakeUpRxEnabled** == **TRUE** 时可用；**UdpNmCarWakeupBytePosition** >= 启用的系统字节（CBV、NID）的数量 |

| SWS 条目 | [ECUC_UdpNm_00077] |
| --- | --- |
| 参数名称 | UdpNmCarWakeUpFilterEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 如果支持 **CWU** 过滤，则只有源节点标识符为 **UdpNmCarWakeUpFilterNodeId** 的 **NM PDU** 内的 **CWU** 位才被视为 **CWU** 请求。FALSE：不支持 **CWU** 过滤；TRUE：支持 **CWU** 过滤。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmCarWakeUpRxEnabled** == **TRUE** 时可用 |

| SWS 条目 | [ECUC_UdpNm_00078] |
| --- | --- |
| 参数名称 | UdpNmCarWakeUpFilterNodeId |
| 父容器 | UdpNmChannelConfig |
| 描述 | 用于 **CWU** 过滤的源节点标识符。如果支持 **CWU** 过滤，则只有源节点标识符为 **UdpNmCarWakeUpFilterNodeId** 的 **NM PDU** 内的 **CWU** 位才被视为 **CWU** 请求。 |
| 多重性 | 0..1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmCarWakeUpFilterEnabled** == **TRUE** 时可用 |

| SWS 条目 | [ECUC_UdpNm_00076] |
| --- | --- |
| 参数名称 | UdpNmCarWakeUpRxEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 启用或禁用对接收到的 **NM PDU** 中整车唤醒（**CarWakeUp**）位求值的支持。FALSE：不支持 **CarWakeUp**；TRUE：支持 **CarWakeUp**。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_UdpNm_00095] |
| --- | --- |
| 参数名称 | UdpNmDynamicPncToChannelMappingEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 用于启用动态**PNC**到通道映射功能的通道特定参数。False：禁用动态**PNC**到通道映射；True：启用动态**PNC**到通道映射。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmDynamicPncToChannelMappingSupport** 为 **TRUE** 时才应为 **TRUE** |

| SWS 条目 | [ECUC_UdpNm_00079] |
| --- | --- |
| 参数名称 | UdpNmImmediateNmCycleTime |
| 父容器 | UdpNmChannelConfig |
| 描述 | 定义立即 **NM PDU** 周期时间（以秒为单位），用于 **UdpNmImmediateNmTransmissions** 次 **NM PDU** 传输。 |
| 多重性 | 0..1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0.001 .. 65.535] |
| 默认值 | - |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmImmediateNmTransmissions** 大于1时该参数有效。 |

| SWS 条目 | [ECUC_UdpNm_00075] |
| --- | --- |
| 参数名称 | UdpNmImmediateNmTransmissions |
| 父容器 | UdpNmChannelConfig |
| 描述 | 定义应传输的立即 **NM PDU** 的数量。如果该值为零，则不传输立即 **NM PDU**。立即 **NM PDU** 的周期时间由 **UdpNmImmediateNmCycleTime** 定义。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 如果 **UdpNmImmediateRestartEnabled** = true，则 **UdpNmImmediateNmTransmissions** = 0；如果 **UdpNmPnHandleMultipleNetworkRequests** == True，则 **UdpNmImmediateNmTransmissions** 必须大于0。 |

| SWS 条目 | [ECUC_UdpNm_00032] |
| --- | --- |
| 参数名称 | UdpNmMainFunctionPeriod |
| 父容器 | UdpNmChannelConfig |
| 描述 | 相应实例的 **UdpNm_MainFunction_x** 的调用周期，单位为[s]。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | ]0 .. INF[ |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00029] |
| --- | --- |
| 参数名称 | UdpNmMsgCycleOffset |
| 父容器 | UdpNmChannelConfig |
| 描述 | 周期传输模式中的时间偏移。它决定传输的启动延迟。参数值 < **UdpNmMsgCycleTime**。仅当 **UdpNmPassiveModeEnabled** 被禁用时该参数有效。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0 .. 65.535] |
| 默认值 | - |
| Post-Build 变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00028] |
| --- | --- |
| 参数名称 | UdpNmMsgCycleTime |
| 父容器 | UdpNmChannelConfig |
| 描述 | **NM**消息的周期。它确定周期速率，并且是传输调度的基础。**NmTimeoutTime** = n * **UdpNmMsgCycleTime**。仅当 **UdpNmPassiveModeEnabled** 被禁用时该参数有效。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0.001 .. 65.535] |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_UdpNm_00090] |
| --- | --- |
| 参数名称 | UdpNmNodeDetectionEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 用于启用节点检测支持的预处理器开关。该参数应从 **NmNodeDetectionEnabled** 派生。仅当 **UdpNmNodeIdEnabled** == true 时才应启用该参数。calculationFormula: If(**UdpNmPduCbvPosition** != **UDPNM_PDU_OFF**) then Equal(NmNodeDetectionEnabled) else Equal(False)。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 如果 **UdpNmPassiveModeEnabled** 被启用则不可用 |

| SWS 条目 | [ECUC_UdpNm_00031] |
| --- | --- |
| 参数名称 | UdpNmNodeId |
| 父容器 | UdpNmChannelConfig |
| 描述 | 本地节点的节点标识符。 |
| 多重性 | 0..1 |
| 类型 | EcucIntegerParamDef |
| 取值范围 | 0 .. 255 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmNodeIdEnabled** == **True** 时该参数才相关。 |

| SWS 条目 | [ECUC_UdpNm_00091] |
| --- | --- |
| 参数名称 | UdpNmNodeIdEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 用于启用源节点标识符的预处理器开关。该参数应从 **NmNodeIdEnabled** 派生。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00026] |
| --- | --- |
| 参数名称 | UdpNmPduCbvPosition |
| 父容器 | UdpNmChannelConfig |
| 描述 | 定义控制位向量在**NM**数据包（**NM PACKET**）中的位置。该参数的值表示控制位向量在**NM PACKET**中的位置（**UDPNM_PDU_BYTE_0** 表示字节0，**UDPNM_PDU_BYTE_1** 表示字节1，**UDPNM_PDU_OFF** 表示控制位向量不是**NM PACKET**的一部分）。另请参见 **UdpNmPduNidPosition**。如果 (**UdpNmPduCbvPosition** != **UDPNM_PDU_OFF** 且 **UdpNmPduNidPosition** != **UDPNM_PDU_OFF**)，则 **UdpNmPduCbvPosition** != **UdpNmPduNidPosition**；如果 (**UdpNmPduCbvPosition** != **UDPNM_PDU_OFF** 且 **UdpNmPduNidPosition** == **UDPNM_PDU_OFF**)，则 **UdpNmPduCbvPosition** = **UDPNM_PDU_BYTE0**。 |
| 多重性 | 1 |
| 类型 | EcucEnumerationParamDef |
| 取值范围 | UDPNM_PDU_BYTE_0；UDPNM_PDU_BYTE_1；UDPNM_PDU_OFF |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00025] |
| --- | --- |
| 参数名称 | UdpNmPduNidPosition |
| 父容器 | UdpNmChannelConfig |
| 描述 | 定义源节点标识符在**NM**数据包（**NM PACKET**）中的位置。实现类型：**UdpNm_PduPositionType**。该参数的值表示源节点标识符在**NM PACKET**中的位置（**UDPNM_PDU_BYTE_0** 表示字节0，**UDPNM_PDU_BYTE_1** 表示字节1，**UDPNM_PDU_OFF** 表示源节点标识符不是**NM PACKET**的一部分）。另请参见 **UdpNmPduCbvPosition**。如果 (**UdpNmPduNidPosition** != **UDPNM_PDU_OFF** 且 **UdpNmPduCbvPosition** != **UDPNM_PDU_OFF**)，则 **UdpNmPduNidPosition** != **UdpNmPduCbvPosition**；如果 (**UdpNmPduNidPosition** != **UDPNM_PDU_OFF** 且 **UdpNmPduCbvPosition** == **UDPNM_PDU_OFF**)，则 **UdpNmPduNidPosition** = **UDPNM_PDU_BYTE0**。 |
| 多重性 | 1 |
| 类型 | EcucEnumerationParamDef |
| 取值范围 | UDPNM_PDU_BYTE_0（使用字节0）；UDPNM_PDU_BYTE_1（使用字节1）；UDPNM_PDU_OFF（不使用节点标识） |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00061] |
| --- | --- |
| 参数名称 | UdpNmPnEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 启用或禁用部分网络支持。false：不支持部分网络；true：支持部分网络。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00063] |
| --- | --- |
| 参数名称 | UdpNmPnHandleMultipleNetworkRequests |
| 父容器 | UdpNmChannelConfig |
| 描述 | false：**UdpNm_NetworkRequest** 在正常操作状态（**NO**）中被忽略；true：**UdpNm_NetworkRequest** 触发从正常操作状态（**NO**）到重复消息状态（**RM**）的转换。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmPnEnabled** == true 时可用 |

| SWS 条目 | [ECUC_UdpNm_00023] |
| --- | --- |
| 参数名称 | UdpNmRemoteSleepIndTime |
| 父容器 | UdpNmChannelConfig |
| 描述 | 远程睡眠指示的超时时间。它定义了识别所有其他节点已准备好睡眠所需的时间（以[s]为单位）。通常它应等于：n * **UdpNmMsgCycleTime**，其中 n 表示在检测到远程睡眠指示之前正常发送的**NM**数据包的数量。n 减1后的值决定了远程睡眠指示过程能够容忍的丢失**NM**数据包的数量。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0.001 .. 65.535] |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00022] |
| --- | --- |
| 参数名称 | UdpNmRepeatMessageTime |
| 父容器 | UdpNmChannelConfig |
| 描述 | 重复消息状态的超时时间。它定义了NM应在重复消息状态中停留的时间（以秒为单位）。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0 .. 65.535] |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: **UdpNmRepeatMessageTime** = n * **UdpNmMsgCycleTime**；**UdpNmRepeatMessageTime** > **UdpNmImmediateNmTransmissions** * **UdpNmImmediateNmCycleTime**。通常它应等于 n * **UdpNmMsgCycleTime**，其中 n 表示在重复消息状态中正常发送的**NM PDU**的数量。n 减1后的值决定了节点检测过程能够容忍的丢失**NM PDU**的数量。值0表示未配置重复消息状态。这意味着重复消息状态是瞬态的，即进入后立即离开。 |

| SWS 条目 | [ECUC_UdpNm_00092] |
| --- | --- |
| 参数名称 | UdpNmRepeatMsgIndEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 启用/禁用「已接收到重复消息请求位」的通知。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 如果 **UdpNmPassiveModeEnabled** == **TRUE**，或者 (**UdpNmNodeDetectionEnabled** == **FALSE** 且 **UdpNmDynamicPncToChannelMappingEnabled** == **FALSE**)，则 **UdpNmRepeatMsgIndEnabled** = **FALSE**。如果 **UdpNmDynamicPncToChannelMappingEnabled** == **TRUE**，则 **UdpNmRepeatMsgIndEnabled** = **TRUE**。 |

| SWS 条目 | [ECUC_UdpNm_00085] |
| --- | --- |
| 参数名称 | UdpNmRetryFirstMessageRequest |
| 父容器 | UdpNmChannelConfig |
| 描述 | 规定 **UdpNm** 中的首次消息请求是否重复发送，直到被 **SoAd** 接受。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 如果 **UdpNmPassiveModeEnabled** 为 **TRUE**，则 **UdpNmRetryFirstMessageRequest** = false |

| SWS 条目 | [ECUC_UdpNm_00093] |
| --- | --- |
| 参数名称 | UdpNmStayInPbsEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 如果禁用该参数，则准备总线睡眠模式（**Prepare Bus-Sleep Mode**）会在 **UdpNmWaitBusSleepTime** 之后离开。如果启用该参数，则只有在**ECU**断电或出现任何重启原因时才能离开准备总线睡眠模式。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00097] |
| --- | --- |
| 参数名称 | UdpNmSynchronizedPncShutdownEnabled |
| 父容器 | UdpNmChannelConfig |
| 描述 | 规定 **UdpNm** 是否处理**PN**关闭消息以支持跨**PN**拓扑的同步**PNC**关闭。这仅用于充当顶级**PNC**协调器或中间**PNC**协调器角色的**ECU**。因此，**PNC**网关功能被启用，因此使用**ERA**计算。FALSE：禁用同步**PNC**关闭；TRUE：启用同步**PNC**关闭。 |
| 多重性 | 0..1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 仅当 **UdpNmPnEnabled** == **TRUE** 且 **NmPnEraCalcEnabled** == **TRUE** 时可用。 |

| SWS 条目 | [ECUC_UdpNm_00020] |
| --- | --- |
| 参数名称 | UdpNmTimeoutTime |
| 父容器 | UdpNmChannelConfig |
| 描述 | **NM**数据包的网络超时时间。它表示NM应在网络模式（**Network Mode**）中停留多长时间（以[s]为单位），之后才转换到准备总线睡眠模式（**Prepare Bus-Sleep Mode**）。对于集群中的所有节点它应相等；它应大于 **UdpNmMsgCycleTime**。通常，它应等于 x * **UdpNmMsgCycleTime**，其中 n 表示在启动到总线睡眠模式的转换之前，就绪睡眠状态中**NM PACKET**周期时间的数量。n 减1后的值决定了协调算法能够容忍的丢失**NM**数据包的数量。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0.002 .. 65.535] |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_UdpNm_00021] |
| --- | --- |
| 参数名称 | UdpNmWaitBusSleepTime |
| 父容器 | UdpNmChannelConfig |
| 描述 | 总线冷却阶段（**bus calm down phase**）的超时时间。它表示NM应在准备总线睡眠模式中停留多长时间（以[s]为单位），之后才转换到总线睡眠模式（**Bus-Sleep Mode**）。对于集群中的所有节点它应相等；它应足够长以使所有**Tx**缓冲区清空。 |
| 多重性 | 0..1 |
| 类型 | EcucFloatParamDef |
| 取值范围 | [0.001 .. 65.535] |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local；dependency: 如果禁用了 **UdpNmStayInPbsEnabled**，则该参数 |

| SWS 条目 | [ECUC_UdpNm_00018] |
| --- | --- |
| 参数名称 | UdpNmComMNetworkHandleRef |
| 父容器 | UdpNmChannelConfig |
| 描述 | 该引用指向由 **ComMChannel** 定义的唯一通道，并提供对 **ComMChannelId** 中唯一通道索引值的访问。 |
| 多重性 | 1 |
| 类型 | 对 **ComMChannel** 的符号名称引用（**Symbolic name reference**） |
| Post-Build 变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| 包含的容器 | 容器名称 | 多重性 | 作用域/依赖 |
| --- | --- | --- | --- |
| 包含的容器 | UdpNmRxPdu | 1..* | 该容器描述 **UdpNm** 的Rx **PDU**。 |
| 包含的容器 | UdpNmTxPdu | 0..1 | 该容器描述 **UdpNm** 的Tx **PDU**。 |
| 包含的容器 | UdpNmUserDataTxPdu | 0..1 | 该容器描述 **UdpNm** 的用户数据Tx **PDU**。 |

#### 9.2.4. UdpNmRxPdu

| SWS 条目 | [ECUC_UdpNm_00038] |
| --- | --- |
| 容器名称 | UdpNmRxPdu |
| 父容器 | UdpNmChannelConfig |
| 描述 | 该容器描述 **UdpNm** 的Rx **PDU**。 |
| 配置参数 | 见下方参数表 |

| SWS 条目 | [ECUC_UdpNm_00043] |
| --- | --- |
| 参数名称 | UdpNmRxPduId |
| 父容器 | UdpNmChannelConfig |
| 描述 | 下层 **RxIndication** 将使用的 **RxPdu** 的ID。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为该参数生成符号名称） |
| 取值范围 | 0 .. 4294967296 |
| 默认值 | - |
| Post-Build 变体值 | true |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local，withAuto = true |

| SWS 条目 | [ECUC_UdpNm_00039] |
| --- | --- |
| 参数名称 | UdpNmRxPduRef |
| 父容器 | UdpNmChannelConfig |
| 描述 | 对 **AUTOSAR ECU** 配置规范中描述的全局 **PDU** 结构中的 **PDU** 的引用。**UdpNm** 模块将使用该引用来导出 **PDU Id**。 |
| 多重性 | 1 |
| 类型 | 对 **Pdu** 的引用（**Reference to Pdu**） |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |


无包含的容器。

#### 9.2.5. UdpNmTxPdu

| SWS 条目 | [ECUC_UdpNm_00036] |
| --- | --- |
| 容器名称 | UdpNmTxPdu |
| 父容器 | UdpNmChannelConfig |
| 描述 | 该容器描述 **UdpNm** 的Tx **PDU**。 |
| 配置参数 | 见下方参数表 |

| SWS 条目 | [ECUC_UdpNm_00042] |
| --- | --- |
| 参数名称 | UdpNmTxConfirmationPduId |
| 父容器 | UdpNmChannelConfig |
| 描述 | 下层 **TxConfirmation** 将使用的 **TxPdu** 的ID。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为该参数生成符号名称） |
| 取值范围 | 0 .. 4294967296 |
| 默认值 | - |
| Post-Build 变体值 | true |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local，withAuto = true |

| SWS 条目 | [ECUC_UdpNm_00037] |
| --- | --- |
| 参数名称 | UdpNmTxPduRef |
| 父容器 | UdpNmChannelConfig |
| 描述 | 对 **AUTOSAR ECU** 配置规范中描述的全局 **PDU** 结构中的 **PDU** 的引用。**UdpNm** 模块将使用该引用来导出 **PDU Id**。 |
| 多重性 | 1 |
| 类型 | 对 **Pdu** 的引用（**Reference to Pdu**） |
| Post-Build 变体值 | true |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |


无包含的容器。

#### 9.2.6. UdpNmUserDataTxPdu

| SWS 条目 | [ECUC_UdpNm_00056] |
| --- | --- |
| 容器名称 | UdpNmUserDataTxPdu |
| 父容器 | UdpNmChannelConfig |
| 描述 | 用于启用 **COM** 用户数据 **Tx** 路径的预处理器开关。用例：通过 **SWC** 设置 **NMUserData**。 |
| 配置参数 | 见下方参数表 |

| SWS 条目 | [ECUC_UdpNm_00058] |
| --- | --- |
| 参数名称 | UdpNmTxUserDataPduId |
| 父容器 | UdpNmChannelConfig |
| 描述 | 该参数定义**NM**用户数据 **I-PDU** 的句柄ID。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为该参数生成符号名称） |
| 取值范围 | 0 .. 65535 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_UdpNm_00057] |
| --- | --- |
| 参数名称 | UdpNmTxUserDataPduRef |
| 父容器 | UdpNmChannelConfig |
| 描述 | 对全局**PDU**集合中**NM**用户数据 **I-PDU** 的引用。 |
| 多重性 | 1 |
| 类型 | 对 **Pdu** 的引用（**Reference to Pdu**） |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：X（VARIANT-PRE-COMPILE）；Link time：X（VARIANT-LINK-TIME）；Post-build time：- |
| 作用域/依赖 | scope: local |


无包含的容器。

### 9.3. 发布信息

详情请参阅[\[3\]](#ref-3)中的章节10.3「发布信息」（**Published Information**）。

## B. AUTOSAR 可追溯项变更历史

请注意，本章中的列表还包括在后续版本中已从规范中移除的可追溯项。这些项不会在文档中显示为超链接。

### B.1. 本文档根据 AUTOSAR R23-11 版本的可追溯项历史

#### B.1.1. R23-11 中新增的规范条目

```
[SWS_UdpNm_00509] [SWS_UdpNm_91008] [SWS_UdpNm_91011]
```

#### B.1.2. R23-11 中变更的规范条目

```
[SWS_UdpNm_00013] [SWS_UdpNm_00074] [SWS_UdpNm_00075] [SWS_UdpNm_00088] [SWS_UdpNm_00470] [SWS_UdpNm_91006]
```

#### B.1.3. R23-11 中删除的规范条目

无。

<section id="wechat">

<h4>微信扫一扫，获取更多及时资讯</h4>

![](wechat.png)

</section>
