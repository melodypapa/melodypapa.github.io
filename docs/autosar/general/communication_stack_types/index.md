---
title: "AUTOSAR Communication Stack Types（通信栈类型）"
spec: AUTOSAR_CP_SWS_CommunicationStackTypes
release: R23-11
---

## 1. 简介和功能概述

本文档规定 **AUTOSAR** 通信栈类型头文件。它包含基础软件通信栈中多个模块共同使用的所有类型，以及所有基础软件模块中与平台和编译器无关的所有类型。

强烈建议这些通信栈类型文件在 **AUTOSAR** 社区内保持唯一，以保证类型的唯一性，并避免从供应商 A 更换为供应商 B 时发生类型变更。

## 2. 缩略语

下述术语表包含与通信栈类型相关、但未包含在 [\[1\]](#ref-1)（**AUTOSAR** 术语表）中的缩略语和缩写。

**API**
> 应用编程接口（**Application Programming Interface**）

**DCM**
> 诊断通信管理器（**Diagnostic Communication Manager**）

**I-PDU**
> 交互层 **PDU**（**Interaction Layer PDU**）。在 **AUTOSAR** 中，交互层等价于通信服务层。

**L-PDU**
> 数据链路层 **PDU**（**Data Link Layer PDU**）。在 **AUTOSAR** 中，数据链路层等价于通信硬件抽象和微控制器抽象层。

**N-PDU**
> 网络层 **PDU**（**Network Layer PDU**）。在 **AUTOSAR** 中，网络层等价于传输协议。

**OSEK/VDX**
> 1993 年 5 月，**OSEK** 作为德国汽车工业的一个联合项目创立，旨在为车辆内分布式控制单元的开放式架构建立一个行业标准。**OSEK** 是德语术语「Offene Systeme und deren Schnittstellen für die Elektronik im Kraftfahrzeug」（英语：Open Systems and the Corresponding Interfaces for Automotive Electronics）的缩写。初始项目合作伙伴为 **BMW**、**Bosch**、**Daimler Chrysler**、**Opel**、**Siemens**、**VW** 以及作为协调方的卡尔斯鲁厄大学 **IIIT**。法国汽车制造商 **PSA** 和 **Renault** 于 1994 年加入 **OSEK**，引入了他们的 **VDX**（**Vehicle Distributed eXecutive**）方案——法国汽车工业内的一个类似项目。在 1995 年 10 月的第一次研讨会上，**OSEK/VDX** 小组展示了 **OSEK** 与 **VDX** 之间协调一致的规范成果。1997 年 10 月第 2 届国际 **OSEK/VDX** 研讨会之后，发布了规范的第二版。

**PDU**
> 协议数据单元（**Protocol Data Unit**）

**SDU**
> 服务数据单元（**Service Data Unit**）——**PDU** 的载荷。

**TP**
> 传输协议（**Transport Protocol**）

**Com**
> 通信（**Communication**）

**EcuC**
> **ECU** 配置（**ECU Configuration**）

**e.g.**
> （拉丁语）exempli gratia =（英语）for example，即「例如」。

**i.e.**
> （拉丁语）id est =（英语）that is，即「也就是说」。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

<a id="ref-1"></a>[1] 术语表
> AUTOSAR_FO_TR_Glossary

<a id="ref-2"></a>[2] 基础软件模块通用规范
> AUTOSAR_CP_SWS_BSWGeneral

<a id="ref-3"></a>[3] 通信需求
> AUTOSAR_CP_SRS_COM

### 3.2. 相关规范

**AUTOSAR** 提供了基础软件模块的通用规范 [\[2\]](#ref-2)（**SWS BSW General**），该规范同样适用于通信栈类型。

因此，规范 **SWS BSW General** 应被视为通信栈类型的附加且必需的规范。

## 4. 约束和假设

### 4.1. 限制

无限制。

### 4.2. 汽车域的适用性

无限制。

### 4.3. 安全相关环境的适用性

无限制，因为本规范的主题是一个规定类型的头文件。它不包含也不实现任何功能。

## 5. 对其他模块的依赖

通信栈类型头文件基于平台类型头文件 [PltfTypes]（Platform_Types.h）定义通信类型。为防止头文件被重复包含，通信栈头文件包含了标准类型头文件 [StdTypes]，该文件已经包含了上述另外两个文件。

## 6. 功能规格

### 6.1. 一般问题

不允许在该文件中添加任何项目或供应商特定的扩展。任何扩展都会使 **AUTOSAR** 符合性失效。

由于许多通信栈类型取决于相应的 **ECU**，因此该文件应针对每个 **ECU** 依据其特定的 **ECU** 配置独立生成。

[PduIdType](#711-pduidtype) 和 [PduLengthType](#712-pdulengthtype) 的值应分别派生自 EcuCPduCollection 容器的 PduIdTypeEnum 和 PduLengthTypeEnum。

### 6.2. 错误分类

文档 [\[2\]](#ref-2)《基础软件模块通用规范》的「错误处理」章节详细描述了基础软件的错误处理。其中，它构成了一个由 **BSW** 模块中可能发生的五种错误类型组成的分类方案。

在此基础上，下述各小节按其所属小节规定具体的错误。

#### 6.2.1. 开发错误

无开发错误。

#### 6.2.2. 运行时错误

无运行时错误。

#### 6.2.3. 瞬态故障

无瞬态故障。

#### 6.2.4. 生产错误

无生产错误。

#### 6.2.5. 扩展生产错误

无扩展生产错误。

### 6.3. 安全事件

本模块不报告安全事件。

## 7. API规范

### 7.1. 类型定义

#### 7.1.1. PduIdType

类型，派生自 uint16 或 uint8——该全局类型的大小取决于一个软件模块内使用的 **PDU** 的最大数量。范围为 0...<PduIdmax>——从零开始的整数。该参数应由生成工具根据 **EcuC** 虚拟层中配置的值生成，并生成在 ComStack_Cfg.h 文件中。例如：如果没有软件模块处理的 **PDU** 超过 256 个，该类型可设置为 uint8；如果至少有一个软件模块处理超过 256 个 **PDU**，则该类型必须全局设置为 uint16。该类型用于除总线驱动程序之外的整个 **AUTOSAR** 通信栈。可通过 **ComStack_Types.h** 获得。

该类型的变量用作一个软件模块或其集合内 **PDU** 的唯一标识符，也用于两个软件模块之间的交互，此时使用相应目标模块的 PduId 进行引用。

为了能够在软件模块内执行表索引，该类型的变量应从零开始且连续。一个模块中可能存在多个 PduId 范围，该模块内执行的每种操作类型（例如发送和接收）各对应一个范围。

PduIdmax（PduId 范围的最大编号）是该模块内相应操作类型所处理的 **PDU** 数量减 1。

#### 7.1.2. PduLengthType

类型，派生自 uint16、uint32 或 uint8——该全局类型的大小取决于一个 **ECU** 要发送的 **PDU** 的最大长度。范围为 0...<PduLengthmax>——从零开始的整数。该参数应由生成工具根据 **EcuC** 虚拟层中配置的值生成，并生成在 ComStack_Cfg.h 文件中。例如：如果不使用分段，该长度取决于底层通信系统一帧的最大载荷大小（**FlexRay** 的最大值为 255，因此为 uint8）；如果使用分段，则取决于分段 **N-PDU** 的最大长度（通常使用 uint16）。该类型应用于一个 **ECU** 中除总线驱动程序之外的整个 **AUTOSAR** 通信栈。可通过 **ComStack_Types.h** 获得。

该类型的变量用作 **PDU** 的长度信息。长度信息以字节数提供。

PduLengthmax（**PDU** 的最大长度）是该 **ECU** 要发送的最大（可能分段的）**PDU** 的长度。

#### 7.1.3. PduInfoType

结构类型。元素为：

* **SduDataPtr**（uint8*）：指向 **PDU** 的 **SDU**（即载荷数据）的指针。该指针的类型取决于编译时使用的内存模型。
* **MetaDataPtr**（uint8*）：指向 **PDU** 的元数据（例如 **CAN ID**、套接字 **ID**、诊断地址）的指针，由一系列元数据项组成。元数据项的长度和类型针对每个 **PDU** 静态配置。超过 8 位的元数据项使用平台字节序。
* **SduLength**（[PduLengthType](#712-pdulengthtype)）：**SDU** 的字节长度。

该类型的变量应用于存储任何类型 **PDU** 的基本信息，即指向其 **SDU**（载荷）的指针变量、指向 **PDU** 元数据的指针，以及以字节数表示的相应 **SDU** 长度。可通过 **ComStack_Types.h** 获得。

#### 7.1.4. PNCHandleType

类型，派生自 uint16。用于存储部分网络集群（**partial network cluster**）的标识符。可通过 **ComStack_Types.h** 获得。

#### 7.1.5. TPParameterType

枚举类型。指定要更改其值的参数（**BS** 或 **STmin**）。可通过 **ComStack_Types.h** 获得。

* **TP_STMIN**（0x00）：分隔时间（**Separation Time**）。
* **TP_BS**（0x01）：块大小（**Block Size**）。
* **TP_BC**（0x02）：**FlexRay** 传输协议模块中使用的带宽控制参数。

#### 7.1.6. BufReq_ReturnType

枚举类型。该类型的变量应用于存储缓冲区请求的结果。可通过 **ComStack_Types.h** 获得。

* **BUFREQ_OK**（0x00）：缓冲区请求成功完成。该状态的值应为 0。
* **BUFREQ_E_NOT_OK**（0x01）：缓冲区请求不成功。缓冲区无法访问。该状态的值应为 1。
* **BUFREQ_E_BUSY**（0x02）：暂时没有可用的缓冲区。由请求方在一定时间内重试请求。该状态的值应为 2。
* **BUFREQ_E_OVFL**（0x03）：无法提供所需长度的缓冲区。该状态的值应为 3。

#### 7.1.7. TpDataStateType

枚举类型。该类型的变量应用于存储 **TP** 缓冲区的状态。可通过 **ComStack_Types.h** 获得。

* **TP_DATACONF**（0x00）：**TP_DATACONF** 表示迄今为止已复制的所有数据均已被确认，可以从 **TP** 缓冲区中移除。本次 **API** 调用复制的数据除外，它们将在稍后被确认。
* **TP_DATARETRY**（0x01）：**TP_DATARETRY** 表示此 **API** 调用应复制已复制的数据，以便从错误中恢复。在这种情况下，TxTpDataCnt 指定本次 **API** 调用要复制的第一个字节的偏移量。
* **TP_CONFPENDING**（0x02）：**TP_CONFPENDING** 表示先前复制的数据必须保留在 **TP** 中。

#### 7.1.8. RetryInfoType

结构类型。元素为：

* **TpDataState**（[TpDataStateType](#717-tpdatastatetype)）：用于存储 **TP** 缓冲区状态的枚举类型。
* **TxTpDataCnt**（[PduLengthType](#712-pdulengthtype)）：从当前位置起的偏移量，标识要重传的字节数。

该类型的变量应用于存储关于 **TP** 缓冲区处理的信息。可通过 **ComStack_Types.h** 获得。

#### 7.1.9. NetworkHandleType

类型，派生自 uint8。范围为 0..255——从零开始的整数。NetworkHandleType 类型的变量应用于存储通信通道的标识符。可通过 **ComStack_Types.h** 获得。

#### 7.1.10. CbkHandleIdType

类型，派生自 uint16。用于 **Com** 和 **LdCom** 用户回调的句柄 **ID**。可通过 **ComStack_Types.h** 获得。

#### 7.1.11. TimeTupleType

结构类型。元素为：

* **timestampClockValue**（[TimeStampType](#7112-timestamptype)）：用于入口/出口时间戳记的时钟值。
* **disciplinedClockValue**（[TimeStampType](#7112-timestamptype)）：可调硬件时钟的值。
* **timeQuality**（[TimeStampQualType](#7113-timestampqualtype)）：时间元组的状态。

时间元组（**Time Tuple**）表示两个相关硬件时钟的时钟值：用于帧时间戳记的时钟的值，以及通过交叉时间戳记（**cross-timestamping**）导出的相应可调硬件时钟的值。可通过 **ComStack_Types.h** 获得。

#### 7.1.12. TimeStampType

结构类型。元素为：

* **nanoseconds**（uint32）：时间的纳秒部分。
* **seconds**（uint32）：时间 48 位秒部分的 32 位 **LSB**。
* **secondsHi**（uint16）：时间 48 位秒部分的 16 位 **MSB**。

该类型的变量用于表示时间戳，包括相对时间和绝对日历时间。绝对时间从 1970-01-01 开始。秒部分的值范围：0 .. (2^48-1)，即 0 到 3257812230 天 [0xFFFF FFFF FFFF]。纳秒部分的值范围：0 到 999999999 ns [0x3B9AC9FF]；纳秒中的无效值：[0x3B9ACA00] 到 [0x3FFFFFFF]；位 30 和位 31 保留，默认值：0。可通过 **ComStack_Types.h** 获得。

#### 7.1.13. TimeStampQualType

枚举类型。根据硬件的不同，可能支持与所评估时间戳相关的质量信息。如果不支持，该值应始终为 Valid。对于 Uncertain 和 Invalid 值，上层应丢弃该时间戳。可通过 **ComStack_Types.h** 获得。

* **VALID**（0）：时间戳有效。
* **INVALID**（1）：时间戳无效。
* **UNCERTAIN**（2）：时间戳状态不确定。

#### 7.1.14. ListElemStructType

结构类型。元素为：

* **DataLength**（uint16）：表示数据的长度。
* **DataPtr**（uint8*）：表示指向数据的指针。
* **NextListElemPtr**（ListElemStructType*）：指向下一个列表元素的指针。

该类型定义单向链表的一个元素。每个元素表示关联数据块的一部分。数据块例如可以构成一个以太网帧。每个元素寻址一个数据位置、数据长度和一个指向下一个元素的指针。最后一个节点（尾部）的 NextListElemPtr 设置为 NUL_PTR。数据块（例如以太网帧）的重构过程通过从第一个数据元素（头部）遍历到最后一个数据元素（尾部）来执行。单向链表按网络字节序（大端）链接。因此，头部元素表示数据块（例如以太网帧）的最高有效部分。可通过 **ComStack_Types.h** 获得。

### 7.2. 函数定义

不适用。

## 8. 时序图

不适用。

## 9. 配置规范

### 9.1. 发布信息

有关详情，请参阅 [\[2\]](#ref-2) 中的第 10.3 章「发布信息」。
