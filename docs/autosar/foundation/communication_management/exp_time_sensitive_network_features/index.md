---
title: "Explanation of Time Sensitive Networking Features（时间敏感网络特性说明）"
spec: AUTOSAR_FO_EXP_TimeSensitiveNetworkFeatures
release: R23-11
---

<!-- 源文档 AUTOSAR_FO_EXP_TimeSensitiveNetworkFeatures（R23-11），说明文档（EXP），不受 Type A 七章骨架约束；章节结构镜像源文档自身编号（1–4）。封面表格、Disclaimer、Contents 属于文档框架信息，不译；源文档开头的 References 列表保留为文末不编号的「参考文献」注册表，使正文中的 [n] 引用可链接。源文档 [2.1](#21-缩略语) 的缩略语表为三列布局，其中 Acronym 列为 PDF 合并单元格遗留的空列，已按两列（缩略语 | 说明）规范化并以粗体术语行 + 引用块形式给出；表 4.1 的 9 行（含重复的 IEEE 802.1Qbv 行）严格按源文档行序保留。 -->

## 1. 简介和功能概述

### 1.1. 目标

时间敏感网络（**Time-Sensitive Networking**, TSN）是由 [\[1, IEEE 802.1 TSN Task Group\]](#ref-1) 规定的一组标准。它通过以太网提供极低时延、高可靠性的端到端数据传输。因此，TSN 被视为标准以太网上确定性通信的关键使能技术之一，并可进一步用于汽车以太网的精确计时与数据传输保证。

本文档的目的是概述相关的 TSN 特性，并给出如何将它们与 AUTOSAR 平台一起使用的示例。

### 1.2. 范围

本文档提供解释性信息，帮助汽车工程师理解基本的 TSN 特性，以及在汽车以太网上设计确定性网络的基本方法。

本文档的内容涉及以下主题：

- 约束和假设
- 概述
- 整形器的使用
- 时间同步的精度
- 时间同步质量（精度）的测量

## 2. 定义和缩略语

### 2.1. 缩略语

下表包含与 FO_RS_IEEE1722 相关、但未包含在 AUTOSAR TR 术语表中的缩略语和缩写。

**TSN**
> 时间敏感网络（**Time Sensitive Networking**）

**TSpec**
> 由 [\[2, IEEE Std 802.1Q-2018\]](#ref-2) 规定的流量规范（**Traffic specification**）

**AVTP**
> 由 [\[3, IEEE Std 1722-2016\]](#ref-3) 规定的音视频传输协议（**Audio/Video Transport Protocol**）

**AVTPDU**
> 由 [\[3, IEEE Std 1722-2016\]](#ref-3) 规定的音视频传输协议数据单元（**Audio/Video Transport Protocol Data Unit**）

**IIDC**
> 由 [\[3, IEEE Std 1722-2016\]](#ref-3) 规定的仪器与工业数字相机（**Instrumentation and Industrial Digital Camera**）

**61883_IIDC**
> 由 [\[3, IEEE Std 1722-2016\]](#ref-3) 规定的 IEC 61883/IIDC 格式

**AAF**
> 由 [\[3, IEEE Std 1722-2016\]](#ref-3) 规定的 AVTP 音频格式（**AVTP Audio Format**）

**CRF**
> 控制参考格式（**Control Reference Format**）

**TSCF**
> 时间敏感控制格式（**Time Sensitive Control Format**）

**NTSCF**
> 非时间敏感控制格式（**None Time Sensitive Control Format**）

**ACF**
> AVTP 控制格式（**AVTP Control Format**）

**ACF_CAN**
> 由 [\[3, IEEE Std 1722-2016\]](#ref-3) 规定的控制器局域网（**CAN**）/带灵活数据速率的 CAN（**CAN FD**）报文

**ACF_CAN_BRIEF**
> 由 [\[3, IEEE Std 1722-2016\]](#ref-3) 规定的缩略 CAN/CAN FD 报文

**ACF_LIN**
> 由 [\[3, IEEE Std 1722-2016\]](#ref-3) 规定的 LIN R© 报文

**RVF**
> 原始视频格式（**Raw Video Format**）

**gPTP**
> 通用精确时间协议（**generalized Precision Time Protocol**）[\[4, IEEE Std 802.1AS\]](#ref-4)

**PPS**
> 每秒脉冲（**Pulse Per Second**）物理信号

**1PPS**
> 每秒 1 脉冲（**1 Pulse Per Second**）物理线路

**GPS**
> 全球定位系统（**Global Positioning System**）

### 2.2. 术语定义

#### 2.2.1. 以太网报文（Ethernet packet）

定义："以太网报文"是由 [\[5, IEEE Std 802.3-2022\]](#ref-5) 规定的线上格式，包括以下部分：前导码（7 字节）、SFD（帧起始定界符，1 字节）、以太网帧（最多 2000 字节）、IPG（报文间间隔，12 字节时间）。

#### 2.2.2. 以太网帧（Ethernet frame）

定义："以太网帧"是由 [\[5, IEEE Std 802.3-2022\]](#ref-5) 规定的线上格式，包括以下部分：MAC 目的地址字段（6 字节）、MAC 源地址字段（6 字节）、类型字段（2 字节）、MAC 客户数据字段（含可选 Q-Tag（4 字节））（最多 1982 字节）、可选 PAD（填充字节）、FCS（帧校验序列，4 字节）。

#### 2.2.3. 流（Stream）

定义："流"表示多个按相似帧属性（例如 MAC 源地址）分组的以太网帧。

#### 2.2.4. 基于 IEEE1722 的流（IEEE1722-based stream）

定义："基于 IEEE1722 的流"表示多个将 EtherType 设置为 AVTP Ethertype（0x22F0）的以太网帧（参见 [\[3, IEEE Std 1722-2016\]](#ref-3)），它们携带 IEEE1722 规定的 AVTP 头部和一个 AVTP 流数据子类型（例如 AAF（AVTP 音频格式））。

#### 2.2.5. 流数据生产者（Stream data producer）

定义："流数据生产者"表示以太网网络中（持续）产生数据的终端节点。数据经由一条流传输，并由 1 个或多个终端节点（流数据消费者）接收。

#### 2.2.6. 流数据消费者（Stream data consumer）

定义："流数据消费者"表示以太网网络中（持续）消费数据的终端节点。数据经由一条流接收。

#### 2.2.7. AVTP 呈现时间（AVTP presentation time）

定义："AVTP 呈现时间"由 [\[3, IEEE1722-2016\]](#ref-3) 定义，表示 AVTPDU 有效载荷中被指定的数据被传送给流数据消费者的时间敏感应用时的全局同步时间。请注意：AVTP 呈现时间的计算方式为"TavtpPresentationTime" = "TcurrentGlobalTime" + "TmaxTransitTime"。

#### 2.2.8. 最大传输时间（Max transit time）

定义："最大传输时间"由 [\[3, IEEE1722-2016\]](#ref-3) 定义，表示从流数据生产者的数据被加入其出口队列、经由基于 IEEE1722 的流跨越网络传输、到该数据从接收方流数据消费者的入口队列被转发给时间敏感应用为止的最大可接受时延。

#### 2.2.9. 媒体时钟（Media clock）

定义："媒体时钟"由 [\[3, IEEE1722-2016\]](#ref-3) 定义，表示一个以恒定速率产生周期信号的实体（例如具有恒定速率（如 48kHz）的精确硬件时钟）。媒体时钟由媒体时钟提供者承载。

#### 2.2.10. 媒体时钟提供者（Media clock provider）

定义："媒体时钟提供者"是网络中承载媒体时钟的终端节点。媒体时钟提供者向 1 个或多个媒体时钟消费者发送基于 IEEE1722 的流。该流为时钟参考格式（**Clock Reference Format**, CRF）子类型，包含多个与媒体时钟速率相关的呈现时间戳。

#### 2.2.11. 媒体时钟消费者（Media clock consumer）

定义："媒体时钟消费者"是网络中从媒体时钟提供者接收 CRF 子类型基于 IEEE1722 之流的终端节点。媒体时钟消费者基于从媒体时钟提供者接收到的封装数据执行其媒体时钟（例如 PLL）的恢复。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

<a id="ref-1"></a>- [1] IEEE 802.1 TSN Task Group https://1.ieee802.org/tsn/
<a id="ref-2"></a>- [2] IEEE 802.1Q-2018 - IEEE Standard for Local and Metropolitan Area Network Bridges and Bridged Networks https://ieeexplore.ieee.org/
<a id="ref-3"></a>- [3] IEEE Standard 1722-2016 - IEEE Standard for a Transport Protocol for Time-Sensitive Applications in Bridged Local Area Networks
<a id="ref-4"></a>- [4] IEEE Standard 802.1AS-2011
<a id="ref-5"></a>- [5] IEEE 802.3-2022 https://www.ieee802.org/3/
<a id="ref-6"></a>- [6] IEEE Standard for Local and metropolitan area networks-Virtual Bridged Local Area Networks-Amendment 12: Forwarding and Queuing Enhancements for Time-Sensitive Streams https://ieeexplore.ieee.org/
<a id="ref-7"></a>- [7] IEEE Standard for Local and metropolitan area networks - Bridges and Bridged Networks - Amendment 25: Enhancements for Scheduled Traffic https://ieeexplore.ieee.org/
<a id="ref-8"></a>- [8] IEEE Standard for Local and Metropolitan Area Networks-Bridges and Bridged Networks - Amendment 31: Stream Reservation Protocol (SRP) Enhancements and Performance Improvements https://ieeexplore.ieee.org/
<a id="ref-9"></a>- [9] P802.1Qcr - Bridges and Bridged Networks Amendment: Asynchronous Traffic Shaping
<a id="ref-10"></a>- [10] Time Synchronization Protocol Specification AUTOSAR_FO_PRS_TimeSyncProtocol
<a id="ref-11"></a>- [11] Specification of Time Synchronization over Ethernet AUTOSAR_CP_SWS_TimeSyncOverEthernet
<a id="ref-12"></a>- [12] 802.1AS Recovered Clock Quality Testing https://avnu.org/wp-content/uploads/2014/05/Avnu-Testability-802.1ASRecovered-Clock-Quality-Measurement-1.0_Approved-for-Public-Release.pdf

## 4. AUTOSAR 中的时间敏感网络（Time Sensitive Network in AUTOSAR）

### 4.1. 约束和假设

AUTOSAR 不支持以下 TSN 特性：

- 时间感知整形器（**time aware shapers**）
- 主动流识别（**active stream identification**）
- 帧复制（**frame replication**）

AUTOSAR 假定网络中的所有以太网交换机都是支持 VLAN 的（**VLAN-aware**）。不支持不支持 VLAN 的以太网交换机。

### 4.2. 概述

TSN 是一组基于以太网的 IEEE 802 标准。它规定了一些功能，用于确保汽车或工业控制设施中的应用以有界的低时延和高可用性进行传输。时间关键帧的确定性传输可以通过 TSN 特性实现：通过流量整形、无缝冗余传输、过滤、基于优先级的调度、入口监管和速率限制，实现高可靠性、低时延和零丢包。

#### 4.2.1. IEEE 802.1AS

TSN 标准的基础是全局时间同步。它规定了以交换机为关键节点、基于数据链路层的时钟同步机制。IEEE 802.1AS [\[4, IEEE Std 802.1AS\]](#ref-4) 主要由 IEEE 1588（精确时间协议）的简化版本扩展而来，更适合车辆网络中要求高实时精度的通信传输场景。

#### 4.2.2. IEEE 802.1Qav

IEEE 802.1Qav [\[6, IEEE Std 802.Qav\]](#ref-6) 可用于确保传统异步以太网数据流量不干扰 AVB 的实时音视频流。为了避免普通数据流量与 AVB 流量之间对网络资源的竞争，AVB 交换机将时间敏感的音视频流与普通数据流区分开，将实时帧与异步帧分别排队，并将最高优先级分配给实时帧。因此可以使用所谓的基于信用的整形器（**Credit Based Shaper**, CBS）进行带宽限制，以汇聚时间敏感与时间不敏感的流量。

#### 4.2.3. IEEE 802.1Qbv

IEEE 802.1Qbv [\[7, IEEE Std 802.Qbv\]](#ref-7) 规定了时间感知整形特性，允许在时间触发窗口内调度不同优先级帧的传输。时间感知整形将时间划分为固定窗口，并根据帧的优先级在这些窗口内调度帧的传输。时间关键帧通常被赋予更高的优先级并在单独的窗口中传输，而较低优先级的帧在剩余时间内传输。

#### 4.2.4. IEEE 802.1Qcc

大多数网络需要在网络停机时进行配置，这不适合工业控制和汽车网络通信等应用。IEEE 802.1Qcc [\[8, IEEE Std 802.Qcc\]](#ref-8) 可用于引入集中式网络配置（**Centralized Network Configuration**, CNC）和集中式用户配置（**Centralized User Configuration**, CUC）以实现动态网络配置，在网络运行时灵活地配置新设备和数据流。

表4.1 给出了相关 TSN 标准的概览。

表4.1：TSN 标准清单（**List of TSN Standards**）

| TSN 标准 | 说明 |
|---|---|
| IEEE 802.1AS | 时序与同步。 |
| IEEE 802.1Qav | 时间敏感流的转发与排队增强 |
| IEEE 802.1Qbv | 计划流量（**Scheduled Traffic**） |
| IEEE 802.1Qbu | 带帧抢占的转发与排队 |
| IEEE 802.1Qbv | 带计划流量增强的转发与排队 |
| IEEE 802.1Qca | 路径控制与预留 |
| IEEE 802.1Qcc | 集中配置方法 |
| IEEE 802.1Qci | 基于时间的入口逐流过滤与监管 |
| IEEE 802.1CB | 通过帧复制与消除实现可靠性的无缝冗余 |

### 4.3. 网络中整形器的使用

#### 4.3.1. 异步流量整形

##### 4.3.1.1. 概述

异步流量整形（**Asynchronous Traffic Shaping**, ATS）由 [\[9, IEEE Std 802.1Qcr-2020\]](#ref-9) 规定，提供一种可为网络中的数据流提供有界时延的流量整形概念。它避免突发，并为从不同入口端口到达的流提供出口端口的公平使用。这是基于信用的整形器（**CBS**）与 ATS 之间的一个主要区别，因为 CBS 只考虑出口端口的特定流量类别。该算法大体上基于令牌桶算法，并对配置参数使用类似的术语。

ATS 分为两个主要功能块：其一为"ATS 资格时间指派"（**ATS Eligibility Time Assignment**），位于桥的入口侧，作用于由流过滤器使用 stream_handle 和优先级识别的流，包含整形函数的计算部分，即基于 ATS 算法为接收到的每一帧计算一个资格时间（**eligibility time**）。资格时间是帧在出口端口上获得传输资格的时间。另一功能块为"ATS 传输选择算法"（**ATS transmission selection algorithm**），位于出口侧，根据"ATS 资格时间指派"计算的结果对流量进行整形。由于来自不同接收端口的流的帧的资格时间可以处于非递减顺序，ATS 队列需要支持非 FIFO 队列。

##### 4.3.1.2. 配置参数

ATS 资格时间指派的配置参数：

- Scheduler Instance Table（EthSwtAtsInstanceTable）
- -EthSwtAtsInstanceEntry
- ∗ CommittedBurstSize（EthSwtPortATSCommitedBurstSize）
- ∗ CommittedInformationRate（EthSwtPortATSCommitedInformationRate）
- ∗ SchedulerGroupInstanceID（EthSwtPortAtsSchedulerGroupRef）
- Scheduler Group Instance Table（EthSwtAtsGroupInstanceTable）
- -EthSwtAtsGroupInstanceEntry
- ∗ MaxResidenceTime（EthSwtAtsGroupMaximumResidenceTime）

ATS 传输选择算法的配置参数：没有用于配置 ATS 传输选择算法的特定参数，但需要为用于传输打算使用 ATS 进行整形的帧的流量类别配置 ATS 传输选择算法。

##### 4.3.1.3. 配置指导

1. 使用 ATS 算法整形的流需要在桥的入口侧被识别。流过滤器（**Stream Filter**）用于识别流的帧并将其与相关功能关联。要使用流过滤器，需要配置流识别功能以识别流的帧。
2. 流过滤器可用于配置最大 SDU 大小过滤器，以保护后续处理阶段免受大于所论流格式良好帧的最大 SDU 大小的帧的影响。
3. 流过滤器可以使用流门（**stream gates**）提供的 IPV 指派将流重新映射到不同的流量类别。这是可选的，可用于对某些流赋予优先级。
4. 流过滤器为流指派调度器实例（**Scheduler Instance**），后者负责执行计算以得出流的每一帧的资格时间。
   1. CommittedInformationRate 是 ATS 算法用于累积"令牌"的速率（比特/秒），表示流的平均比特率。
   2. CommittedBurstSize 是可累积的最大"令牌"数量，因此定义了最大突发大小。它需要设置为大于由干扰流量可能产生的最大突发的值。
   3. SchedulerGroupInstanceID 引用"ATS 资格时间指派"所关联的 EthSwtAtsGroupInstanceEntry。从同一上游端口接收到的、具有相同流量类别的所有流都需要关联到同一个 SchedulerGroupInstanceID。这保证了在同一端口上接收到的、共享相同优先级的不同流的帧按到达顺序传输。
   4. EthSwtAtsGroupInstanceEntry 还用于配置调度器组的 EthSwtAtsGroupMaximumResidenceTime。该参数定义了计算出的资格时间可以具有的最晚时间点。超过最大驻留时间的帧（即计算出的资格时间晚于到达时间与 EthSwtAtsGroupMaximumResidenceTime 之和的帧）被丢弃。该值可以从该调度器组的帧在此桥中应经历的最大时延导出。
5. 要在出口侧使用 ATS 传输选择算法，需要将用于 ATS 流量的流量类别配置为使用 ATS 传输选择。为此，需要将 EthSwtPortEgressQueueTransmissionSelectionAlgorithm 设置为 ETH-SWT_TRANSMISSION_SELECTION_ALGORITHM_ATS。

#### 4.3.2. 基于信用的整形器

##### 4.3.2.1. 概述

基于信用的整形器（**Credit Based Shaper**, CBS）由 [\[6, IEEE Std 802.Qav\]](#ref-6) 规定，为高优先级、高数据速率的流提供流量整形概念。它作为音视频桥接（**Audio Video Bridging**, AVB）标准的一部分被规定。其行为与 ATS 类似，但 CBS 只作用于桥出口侧的流量类别。因此，在流量类别内部以及不同入口端口之间不存在个体流的区分。由此，基于信用的整形器严格按帧在所有端口上被接收的顺序运行，不会对不同端口接收的帧重新排序。基于信用的整形器将突发最小化，从而保护较低优先级流量免受高优先级 CBS 整形流量的影响。

CBS 只作为一个功能块（每个流量类别一个）存在，它位于桥端口的出口侧，基于信用值使帧可供传输选择。如果信用为零或为正，帧可供传输；如果信用为负，则相关流量类别的帧不可供传输选择。idleSlope 是定义信用累积和消耗速率的主要参数，从而直接控制端口上被指派流量类别的数据速率。

##### 4.3.2.2. 配置参数

基于信用的整形器的配置参数：

- idleSlope（EthSwtPortEgressQueueCreditBasedShaperIdleSlope）
- highCredit（EthSwtPortEgressQueueCreditBasedShaperUpperBoundary）
- lowCredit（EthSwtPortEgressQueueCreditBasedShaperLowerBoundary）

##### 4.3.2.3. 配置指导

1. 与 CBS 关联的帧由优先级识别。如果桥的某些端口将打算用于 CBS 流量的优先级用于其他流量，则需要通过配置优先级再生表（**priority regeneration table**）重新映射这些端口上的优先级。
2. CBS 的 idleSlope 根据该特定端口上以该流量类别发送的所有流的平均比特率设置。需要轻微的超额订阅（**oversubscription**）以考虑网络中不同桥的振荡器频率差异。信用随 idleSlope 增加并随 sendSlope 减少（sendSlope = idleSlope - portTransmitRate）。
3. highCredit 设置为队列中可累积的最大信用量。该值基于来自更高优先级流量类别的流量的最大干扰量和 idleSlope 参数计算。
4. lowCredit 是最低可能的流量额度，可以从该流量类别支持的最大帧大小和 sendSlope 参数导出。
5. 要使用 CBS 算法，需要将用于 CBS 的流量类别配置为使用 CBS 传输选择。为此，需要将 EthSwtPortEgressQueueTransmissionSelectionAlgorithm 设置为 ETH-SWT_TRANSMISSION_SELECTION_ALGORITHM_CBS。

### 4.4. 确保时间同步的精度

#### 4.4.1. 支持以太网网络中精度的建议

##### 4.4.1.1. 文档中反映精度的部分

在时间同步协议规范（**Time Synchronization Protocol Specification**）[\[10\]](#ref-10) 中：

时间主节点与时间从节点应按照 [\[4, IEEE 802.1 AS\]](#ref-4) 附录 B.1.2"时间测量粒度"中定义的时基参考时钟精度工作。

在以太网时间同步规范（**Specification of Time Synchronization over Ethernet**）[\[11\]](#ref-11) 中：

需要为 ECU 提供公共时基的汽车系统，无论 ECU 连接到哪种总线系统。

##### 4.4.1.2. 系统需求

TSN 使用 gPTP 协议（IEEE 802.1AS）为网络中的节点获取精确的时间戳。IEEE 802.1AS 还针对使用 100 Mb/s 链路的音视频桥接，在 7 跳之间的任意两个节点之间达到 +/-500ns 的精度。这意味着硬件必须支持端到端精度为 +/-500ns 的以太网全局时间，其中端到端描述的是从数据生产者到数据消费者（例如从音频源到音频汇）的网络路径。

### 4.5. 时间同步质量（精度）的测量

#### 4.5.1. 概述

需要测量时间同步的质量，以评估设备是否满足 gPTP 恢复时钟质量的需求。

测量时钟同步精度的传统方法是每秒 1 脉冲（**1 Pulse Per Second**, 1PPS）方法。PPS 信号必须由所有参与设备中的硬件时钟驱动，使其每一整秒产生一个脉冲。如果对分布式系统中的多个硬件时钟都这样做，则可以通过在示波器等测量设备上测量来自不同设备的 PPS 脉冲之间的距离来检查它们的同步精度。在时钟被正确同步后，每秒触发的 PPS 脉冲在成功的场景下应只有微小的时间距离。

然而，1PPS 方法在汽车环境中不可行，因为在 ECU 上使用单独的输出引脚来产生 1PPS 信号被认为代价高昂。此外，从设备内部时钟中可能存在静态偏移，并且可能被驱动 1PPS 输出的逻辑中的相反静态偏移抵消。这将导致使用 1PPS 测量方法无法观测到的错误状态。

为了缓解 1PPS 测量的缺陷，可以考虑诸如入口报告方法（**Ingress Reporting Method**）和反向同步方法（**Reverse Sync Method**）等先进方法作为替代的测量方法。关于入口报告方法和反向同步方法的更多细节，请参见 [\[12, 802.1AS Recovered Clock Quality Testing\]](#ref-12)。

#### 4.5.2. PPS 的使用

##### 4.5.2.1. 以太网控制器内 PPS 的配置

如果硬件支持该特性，AUTOSAR 支持配置 PPS 信号的产生。AUTOSAR 支持以下配置选项：

- 支持配置 PPS 的速率（例如 1Hz、2Hz、4Hz……）
- 支持配置 PPS 的占空比（例如当速率配置为 1Hz 时 50% == 500ms 高、500ms 低）
- 支持配置 PPS 的起始点（上升沿或下降沿）（请为 SysT 考虑此点）

##### 4.5.2.2. 使用 OCU 结合 PHC 配置 PPS

如果 OCU 由硬件驱动，则可以生成 PPS 作为以太网控制器中现有 PPS 硬件单元的替代。请注意：建议使用 PPS 硬件单元，因为 OCU 方法可能引入不精确性。

## 参考文献

<a id="ref-1"></a>[\[1\]](#ref-1) IEEE 802.1 TSN Task Group https://1.ieee802.org/tsn/

<a id="ref-2"></a>[\[2\]](#ref-2) IEEE 802.1Q-2018 - IEEE Standard for Local and Metropolitan Area Network Bridges and Bridged Networks https://ieeexplore.ieee.org/

<a id="ref-3"></a>[\[3\]](#ref-3) IEEE Standard 1722-2016 - IEEE Standard for a Transport Protocol for Time-Sensitive Applications in Bridged Local Area Networks

<a id="ref-4"></a>[\[4\]](#ref-4) IEEE Standard 802.1AS-2011

<a id="ref-5"></a>[\[5\]](#ref-5) IEEE 802.3-2022 https://www.ieee802.org/3/

<a id="ref-6"></a>[\[6\]](#ref-6) IEEE Standard for Local and metropolitan area networks-Virtual Bridged Local Area Networks-Amendment 12: Forwarding and Queuing Enhancements for Time-Sensitive Streams https://ieeexplore.ieee.org/

<a id="ref-7"></a>[\[7\]](#ref-7) IEEE Standard for Local and metropolitan area networks - Bridges and Bridged Networks - Amendment 25: Enhancements for Scheduled Traffic https://ieeexplore.ieee.org/

<a id="ref-8"></a>[\[8\]](#ref-8) IEEE Standard for Local and Metropolitan Area Networks-Bridges and Bridged Networks - Amendment 31: Stream Reservation Protocol (SRP) Enhancements and Performance Improvements https://ieeexplore.ieee.org/

<a id="ref-9"></a>[\[9\]](#ref-9) P802.1Qcr - Bridges and Bridged Networks Amendment: Asynchronous Traffic Shaping

<a id="ref-10"></a>[\[10\]](#ref-10) Time Synchronization Protocol Specification
> AUTOSAR_FO_PRS_TimeSyncProtocol

<a id="ref-11"></a>[\[11\]](#ref-11) Specification of Time Synchronization over Ethernet
> AUTOSAR_CP_SWS_TimeSyncOverEthernet

<a id="ref-12"></a>[\[12\]](#ref-12) 802.1AS Recovered Clock Quality Testing https://avnu.org/wp-content/uploads/2014/05/Avnu-Testability-802.1ASRecovered-Clock-Quality-Measurement-1.0_Approved-for-Public-Release.pdf
