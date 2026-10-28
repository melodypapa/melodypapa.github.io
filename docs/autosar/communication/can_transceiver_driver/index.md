---
title: "AUTOSAR CAN Transceiver Driver"
spec: AUTOSAR_CP_SWS_CANTransceiverDriver
release: R23-11
---




## 1. 简介和功能概述

本规范描述了CAN收发器驱动模块（**CAN Transceiver Driver**）的功能、API 和配置。CAN收发器驱动模块负责处理ECU上的CAN收发器硬件芯片。

CAN收发器是一种硬件设备，它将CAN总线上使用的信号电平调整为微控制器识别的逻辑（数字）信号电平。

此外，收发器能够检测电气故障，如接线问题、接地偏移或长显性信号的传输。根据与微控制器的接口，它们标记由单个端口引脚检测到的错误或由SPI检测到的详细错误的汇总。

一些收发器支持电源控制和通过CAN总线的唤醒。市场上通常有不同的唤醒/睡眠和电源概念。

在汽车环境中，主要使用三种不同的CAN总线物理特性。这些是用于高速CAN（高达：1Mbits/s）的**ISO11898**，用于低速 CAN（高达：125Kbits/s）的**ISO11519**，和用于单线CAN的**SAE J2411**。

最新发展包括SBC系统基础芯片（**System Basis Chips**），其中除了CA 之外还实现了电源控制和高级看门狗。它们封装在一个外壳中，并通过单一接口（例如通过 SPI）进行控制。

![](Figure_1.png)

### 1.1. CAN收发器驱动程序的目标

AUTOSAR CAN收发器驱动程序的目标是为适用于大多数当前和未来CAN收发器设备定义接口和行为。CAN收发器驱动程序抽象了CAN收发器硬件。它为更高层提供了一个独立于硬件的接口。 它通过使用**MCAL**层的API来访问CAN收发器硬件，以便实现ECU布局中的抽象化。

### 1.2. 明确未覆盖的CAN收发器功能

一些CAN总线收发器提供附加功能，例如：用于诊断的ECU自检或者错误检测功能。**ECU**自检和错误检测并未在AUTOSAR标准中定义，AUTOSAR所需要实现的功能主要锁定在大多数当前使用的收发器硬件芯片。因此，也不支持接地偏移检测（**ground shift detection**）、选择性唤醒（**selective wake up**）、斜率控制模式（**slope control**）等功能。

AUTOSAR不支持根据**SAE J2411**的单线CAN收发器。

### 1.3. 符合SAE J2411的单线CAN收发器

AUTOSAR不支持符合**SAE J2411**的单线**CAN**。

## 2. 缩略语

**ComM**         
> Communication Manager

**DEM**      
> Diagnostic Event Manager

**DET**
> Default Error Tracer 

**DIO**
> Digital Input Output (SPAL module)

**EB**
> 外部缓冲通道。位于SPI处理程序/驱动程序之外，包含要传输的数据的缓冲区。

**EcuM**
> ECU State Manager
    
**IB**
> 内部缓冲通道。位于 SPI 处理程序/驱动程序内部，包含要传输的数据的缓冲区。

**ISR**
> Interrupt Service Routine 中断服务程序 

**MCAL**
> Micro Controller Abstraction Layer 

**Port**
> Port module (SPAL module)

**SBC** 
> System Basis Chip 系统基础芯片。集成了例如 CAN 和/或 LIN 收发器、看门狗和电源控制。

**SPAL**         
> 标准外设抽象 

**SPI Channel**
> 一个通道是使用相同标准定义的软件数据交换介质。请参阅SPI驱动程序规范 
    
**SPI Job**
> 一个作业由一个或多个具有相同片选的通道组成。作业被认为是原子的，因此不能被中断。 作业也具有指定的优先级。 有关详细信息，请参阅SPI驱动程序规范。

**SPI Sequence** 
> 一个序列是要传输的多个连续作业。 序列取决于静态配置。 有关详细信息，请参阅 SPI 驱动程序规范。 

**CAN Channel**
> 从**CAN**控制器通过**CAN**收发器连接到**CAN**网络的物理通道。

**API**
> 应用编程接口（**Application Programming Interface**）。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

[1] Glossary
> AUTOSAR_FO_TR_Glossary

[2] Layered Software Architecture
> AUTOSAR_CP_EXP_LayeredSoftwareArchitecture

[3] General Specification of Basic Software Modules
> AUTOSAR_CP_SWS_BSWGeneral

[4] Specification of CAN Interface
> AUTOSAR_CP_SWS_CANInterface

[5] Specification of CAN XL Transceiver Driver
> AUTOSAR_CP_SWS_CANXLTransceiverDriver

[6] Specification of ECU State Manager
> AUTOSAR_CP_SWS_ECUStateManager

### 3.2. 相关规范

AUTOSAR提供了基础软件模块的通用规范[3, SWS BSW General]，它也适用于**CAN**收发器驱动程序。

因此，规范**SWS BSW General**应被视为**CAN**收发器驱动程序的附加和必需规范。

## 4. 约束和假设

### 4.1. 限制

**CAN**总线收发器硬件应提供可映射到**AUTOSAR CAN**收发器驱动程序操作模式模型的功能和接口。

另见第6.1节。

### 4.2. 汽车域的适用性

该驱动程序可能适用于所有使用**CAN**进行通信的汽车域。

## 5. 对其他模块的依赖

| 模块 | 依赖关系 |
| --- | --- |
| CanIf | 所有**CAN**收发器驱动程序都位于**CanIf**之下。 |
| ComM | **ComM**通过**CanIf**控制**CAN**收发器驱动程序的通信模式。每个**CAN**收发器驱动程序都是独立控制的。 |
| DET | **DET**从**CAN**收发器驱动程序获取开发错误信息。 |
| DEM | **DEM**从**CAN**收发器驱动程序获取生产错误信息。 |
| DIO | **DIO**模块用于访问通过端口连接的**CAN**收发器设备。 |
| EcuM | **EcuM**通过**CanIf**从**CAN**收发器驱动程序获取唤醒事件信息。 |
| SPI | **SPI**模块用于访问通过**SPI**连接的**CAN**收发器设备。 |

### 5.1. 文件结构

#### 5.1.1. 代码文件结构

**AUTOSAR**规定的命名约定适用于**CanTrcv**模块的所有文件。

| 文件名 | 需求 | 描述 |
| --- | --- | --- |
| CanTrcv.c | SWS_CanTrcv_00069 | 通用实现C文件。它不包含中断例程。 |
| CanTrcv.h | SWS_CanTrcv_00052 | 它仅包含与其他**BSW**模块相关的信息（API）。根据配置的不同API差异被封装起来。 |

**CanTrcv**模块由这些文件组成。

## 6. 功能规格

### 6.1. CAN收发器驱动操作模式

CanTrcv模块需实现如下所示的状态图，并独立于每个配置的收发器。

![](Figure_7_1.png)

此图的主要思想是通过使用通用方案，来支持众多的迄今为止可用的CAN总线收发器。根据CAN收发器硬件的不同，模型可能具有超出给定 CAN收发器硬件所需的一个或两个状态，但这显然会将**ComM**和**EcuM**与使用的硬件分离。

**1. POWER_ON**

> **ECU**已完全通电。

**2. NOT_ACTIVE**
> CAN收发器硬件的状态取决于ECU硬件以及**Dio**和**Port**驱动程序配置。CAN收发器驱动程序未初始化，因此未激活。

**3. ACTIVE**

> 函数**CanTrcv_Init**已被调用。CAN收发器驱动程序进入活动状态。根据配置，CAN收发器驱动程序进入状态**CANTRCV_TRCVMODE_SLEEP**或**CANTRCV_TRCVMODE_STANDBY**。

**4. CANTRCV_TRCVMODE_NORMAL**

> 总线处于全通信。如果CAN收发器硬件控制ECU电源，则ECU完全供电。CAN收发器驱动程序未检测到进一步的唤醒信息。

**5. CANTRCV_TRCVMODE_STANDBY**

> 可能无通信。如果CAN收发器硬件控制ECU电源，ECU仍然供电。 仅在此模式下，才能到**CANTRCV_TRCVMODE_SLEEP**的转换。可以通过总线或本地唤醒事件唤醒。

**6. CANTRCV_TRCVMODE_SLEEP**

> 可能无通信。ECU可能没有电源，依赖于谁复杂电源控制。可以通过总线或本地唤醒事件唤醒。

函数**CanTrcv_Init**会使收发器的状态更改为**CANTRCV_TRCVMODE_SLEEP**或**CANTRCV_TRCVMODE _STANDBY**。这取决于配置，并且可以为每个收发器独立配置。

如果一个CAN收发器驱动程序覆盖多个CAN收发器（配置为通道），则所有收发器（通道）要么处于 **NOT_ACTIVE**状态，要么处于**ACTIVE**状态。在状态**ACTIVE**中，每个收发器可能处于不同的子状态。

#### 6.1.1. 操作模式切换

可以通过调用函数**CanTrcv_SetOpMode**请求模式切换。允许对当前模式的模式切换请求，并且即使启用了DET，也不应该导致错误。

对于每次调用 **CanTrcv_SetOpMode**的模式切换请求，在到达请求的模式后，CanTrcv模块需要使用**CanIf**的**TransceiverId**引用相应的CAN收发器，调用回调函数**CanIf_TrcvModeIndication**通知上层模块。

### 6.2. CAN收发器硬件操作模式

实际的CAN收发器硬件可能支持比上面状态图中显示的更多的模式转换。此章节会解释了这种依赖关系和推荐的实现行为。

决定CAN收发器硬件状态通过CAN收发器驱动程序哪个软件状态覆盖是由具体实现决定的。同时实现也必须确保所描述的CAN收发器驱动程序软件状态的全部功能会由实现达成。

#### 6.2.1. 临时进入睡眠（Go-To-Sleep）模式的示例

通常称为进入睡眠（**Go-to-sleep**）的模式是从正常切换到睡眠时的临时模式。驱动程序将这种临时模式封装在CAN收发器驱动程序软件状态之一中。 此外，CAN 收发器驱动程序首先从正常切换到待机，然后通过额外的 API 调用从待机切换到睡眠。

#### 6.2.2. PowerOn/ListenOnly模式示例

通常称为PowerOn或ListenOnly的模式是CAN收发器硬件只能接收消息但不能发送消息的模式。此外，在接收消息期间确认位的发送被抑制。此模式不被支持，因为它不属于CAN标准，并且并非所有CAN收发器硬件芯片都支持。

### 6.3. CAN收发器唤醒类型

有三种不同的场景通常被称为唤醒：

**场景一：**
1. MCU未通电。
2. 包括CAN收发器硬件在内的部分ECU已上电。
3. 所需考虑的CAN收发器处于**SLEEP**模式。
4. CAN收发器硬件检测到CAN总线上的唤醒事件。
5. CAN收发器硬件让MCU上电。

就AUTOSAR而言，这可以被认为是冷启动，而不是唤醒。

**场景二：**
1. MCU处于低功耗模式。
2. 包括CAN收发器硬件在内的部件ECU已上电。
3. 所关心的CAN收发器处于待机（**STANDBY**）模式。
4. CAN收发器硬件检测到CAN总线上的唤醒事件。
5. CAN 收发器硬件会触发唤醒的软件中断（**SW interrupt**）。
   
就AUTOSAR而言，这可以被认为是CAN通道和MCU的唤醒。

**场景三：**
1. MCU处于全功率模式。
2. 至少包括CAN收发器硬件在内的部分ECU已上电。
3. 所关心的CAN收发器处于待机（**STANDBY**）模式。
4. CAN收发器硬件检测到CAN总线上的唤醒事件。
5. CAN收发器硬件会使能唤醒事件的SW中断或者通过周期性轮询唤醒事件。
   
就AUTOSAR而言，这可以被认为CAN通道的唤醒。

### 6.4. 启用/禁用唤醒通知

CanTrcv驱动程序需要使用ICU驱动程序，提供的以下API来启用和禁用唤醒事件通知：

* **Icu_EnableNotification**
* **Icu_DisableNotification**
  
只有配置了参数**CanTrcvIcuChannelRef**，CanTrcv驱动程序才能启用/禁用ICU通道。

CanTrcv驱动程序需注意以下内容以避免唤醒事件的丢失：
* 当收发器转换到待机模式（**CANTRCV_STANDBY**）时，它需要启用ICU通道。
* 当收发器转换到正常模式 (**CANTRCV_NORMAL**) 时，它需要禁用ICU通道。

### 6.5. CAN收发器唤醒模式

CAN收发器驱动程序提供两种唤醒模式：NOT_SUPPORTED模式和POLLING模式

#### 6.5.1. NOT_SUPPORTED模式

在**NOT_SUPPORTED**模式下，CAN收发器驱动程序不会产生唤醒。 所有CAN收发器硬件类型都支持此模式。

#### 6.5.2. POLLING模式

在**POLLING**模式下，CAN收发器驱动程序产生的唤醒可能会导致CAN通道唤醒。在此模式下，无法唤醒MCU。该模式由需依赖使用的CAN收发器硬件类型。 **POLLING**唤醒模式会在函数**CanTrcv_CheckWakeup**和主函数**CanTrcv_MainFunction**中支持实现。

#### 6.5.3. 唤醒模式处理

主函数**CanTrcv_MainFunction**由BSW调度程序调用，**CanTrcv_CheckWakeup**由**CanIf**模块调用。

唤醒模式的选择由配置参数**CanTrcvWakeUpSupport**实现。可以通过配置参数**CanTrcvWakeupByBusUsed**为每个单独CAN收发器的唤醒设置打开和关闭的支持。

注意：在这两种唤醒模式下，功能**CanTrcv_CheckWakeup**都需要存在，但功能应基于配置的唤醒模式（**NOT_SUPPORTED**或**POLLING**）。

在检测到唤醒后，如果CAN收发器需要由软件启动特定状态转换（例如：睡眠->正常），这可以由CanTrcv模块在执行**CanTrcv_CheckWakeup**期间完成，此行为是特定于实现的。

当收发器需要特定的状态转换时，必须通过配置这些涉及唤醒过程模块（EcuM、CanIf、ICU 等）来确保**CanTrcv_CheckWakeup**被调用。

### 6.6. 错误分类

文档[3]「基础软件模块通用规范」的「错误处理」（**Error Handling**）章节详细描述了基础软件的错误处理。其中最重要的是，它构成了一个由五种错误类型组成的分类方案，这些错误类型可能发生在**BSW**模块中。

基于此基础，以下章节在相应的小节中规定特定的错误。

#### 6.6.1. 开发错误

| 错误类型 | 相关错误码 | 错误值 |
| --- | --- | --- |
| 使用错误的**CAN**收发器参数调用API | CANTRCV_E_INVALID_TRANSCEIVER | 1 |
| 使用空指针参数调用API | CANTRCV_E_PARAM_POINTER | 2 |
| 未进行初始化就使用API服务 | CANTRCV_E_UNINIT | 11 |
| 在错误的收发器操作模式下调用API服务（期望为 **STANDBY**） | CANTRCV_E_TRCV_NOT_STANDBY | 21 |
| 在错误的收发器操作模式下调用API服务（期望为 **NORMAL**） | CANTRCV_E_TRCV_NOT_NORMAL | 22 |
| 使用 **Trcv WakeupMode** 的无效参数调用API服务 | CANTRCV_E_PARAM_TRCV_WAKEUP_MODE | 23 |
| 使用 **Op Mode** 的无效参数调用API服务 | CANTRCV_E_PARAM_TRCV_OPMODE | 24 |
| 收发器不支持配置的波特率 | CANTRCV_E_BAUDRATE_NOT_SUPPORTED | 25 |
| 模块初始化失败，例如在编译后（**postbuild**）使用无效指针调用 **CanTrcv_Init()**。 | CANTRCV_E_INIT_FAILED | 27 |

#### 6.6.2. 运行时错误

| 错误类型 | 相关错误码 | 错误值 |
| --- | --- | --- |
| 与收发器无通信/通信不正确。 | CANTRCV_E_NO_TRCV_CONTROL | 26 |

#### 6.6.3. 瞬态故障

没有瞬态故障。

#### 6.6.4. 生产错误

没有生产错误。

#### 6.6.5. 扩展生产错误

| 错误名称 | CANTRCV_E_BUS_ERROR |
| --- | --- |
| 简要描述 | 通信期间发生**CAN**总线错误。 |
| 详细描述 | 当收发器在**CAN**通信期间检测到总线故障时，应报告该扩展生产错误。 |
| 检测条件（**Failed**） | 当设置了与总线故障对应的标志时，应以参数 **EventId** 为 **CANTRCV_E_BUS_ERROR**、**EventStatus** 为 **DEM_EVENT_STATUS_FAILED** 报告 **Dem_SetEventStatus**。 |
| 检测条件（**Passed**） | 当未设置与总线故障对应的标志时，应以参数 **EventId** 为 **CANTRCV_E_BUS_ERROR**、**EventStatus** 为 **DEM_EVENT_STATUS_PASSED** 报告 **Dem_SetEventStatus**。 |
| 次要参数 | N/A |
| 所需时间 | N/A |
| 监控频率 | 连续（**continuous**） |

当设置了总线错误（**BUSERR**）标志时，**CAN**收发器模块应能检测到扩展生产错误 **CANTRCV_E_BUS_ERROR**（由 **DEM** 分配值），具体取决于它是否已配置并受硬件支持。

### 6.7. 驱动程序初始化的前提条件

CanTrcv模块的环境应确保所有供CanTrcv模块使用的BSW驱动程序已被初始化，并且在调用**CanTrcv_Init**之前已可用。

CAN收发器驱动程序主要使用**Spi**和**Dio**驱动程序来控制CAN总线收发器硬件。因此在初始化CAN总线收发器驱动程序之前，这些驱动程序必须可用，并准备好运行。

CAN收发器驱动程序可能对初始化序列和对收发器设备的访问有时序要求，这些使用的底层驱动程序必须满足这些要求。对时序的要求可能包含：
1. CAN总线收发器驱动程序初始化的调用必须在上电后尽快的执行，以便能够为**ECU**的所有其他应用及时地从收发器硬件中读取到所有必要的信息。
2. 所使用的底层服务的运行时间需非常短并且是同步的，以使驱动程序能够满足自身硬件设备所需的时序需求地限制。
3. 驱动程序的运行时间可能会由于某些硬件设备配置端口引脚电平有效而延长。例如：等待50μs后，再次更改引脚电平，以达到某特定状态（睡眠）。

### 6.8. 实例概念

对于每种不同的CAN收发器硬件类型，ECU都有一个CAN收发器驱动程序实例。这个实例服务于所有相同类型的CAN收发器硬件。

### 6.9. 等待状态

为了改变操作模式，CAN收发器硬件可能必须执行等待状态。

CAN收发器驱动程序需使用时间服务（Time service）的**Tm_BusyWait1us16bit**接口来实现收发器状态变化的等待时间。

### 6.10. 具有选择性唤醒功能的收发器

部分联网（**Partial Networking**）是CAN系统中的一种状态。在这种状态下，网络中的一些节点处于低功耗模式，而其他节点却保持通信。这降低了整个网络的功耗。处于低功耗模式的节点会被预定义的唤醒帧唤醒。

除了普通收发器提供的**WUP**唤醒模式（**Wake Up Pattern**）唤醒之外，支持选择性唤醒的收发器还可以通过**WUF**唤醒帧（**Wake Up Frame**）唤醒。

如果收发器硬件支持选择性唤醒，则可以通过配置参数**CanTrcvHwPnSupport**来使能。

选择性唤醒功能可通过配置容器（**CanTrcvPartialNetwork**）和以下API获得支持：

* **CanTrcv_GetTrcvSystemData**
* **CanTrcv_ClearTrcvWufFlg**
* **CanTrcv_ReadTrcvTimeoutFlag**
* **CanTrcv_ClearTrcvTimeoutFlag**
* **CanTrcv_ReadTrcvSilenceFlag**
  
但是仅当**CanTrcvHwPnSupport = TRUE**时才进行配置和调用。

如果支持选择性唤醒，则CAN收发器需配置参数**CanTrcvPnFrameCanId**、**CanTrcvPnFrameCanIdMask**和**CanTrcvPnFrameDataMask** 实现被特定 CAN帧或一组CAN帧唤醒。

如果收发器具有识别总线故障的能力（区分：总线故障和其他硬件故障），则可以使用配置参数**CanTrcvBusErrFlag**来实现总线故障诊断功能。

**注意：**
对于支持选择性唤醒功能的CAN收发器，可以在正常模式（**CANTRCV_TRCVMODE_NORMAL**）期间检测唤醒帧。检测到的唤醒帧由收发器 **WUF Flag**标识。 这可确保在转换到待机模式（**CANTRCV_TRCVMODE_STANDBY**）期间不会丢失唤醒帧。

### 6.11. CAN XL扩展

**CAN XL**收发器驱动程序是作为现有**CAN**收发器驱动程序的扩展实现的（参见[5, Specification of Can XL]），非 **CAN XL** 硬件仍将使用基本的**CAN**收发器驱动程序实现。

**CAN XL**收发器驱动程序是**CAN**收发器驱动程序的扩展，它引入了额外的API以支持以太网接口，并向**CAN XL**收发器驱动程序提供模式接口（更多详情参见[5, Specification of Can XL]）。

### 6.12. 安全事件

该模块不报告安全事件。

## 7. API规范

### 7.1. 导入的类型

在本章中列出了从以下文件包含的所有类型：

| 模块 | 头文件 | 导入的类型 |
| --- | --- | --- |
| Dem | Rte_Dem_Type.h | Dem_EventIdType |
| Dem | Rte_Dem_Type.h | Dem_EventStatusType |
| Dio | Dio.h | Dio_ChannelGroupType |
| Dio | Dio.h | Dio_ChannelType |
| Dio | Dio.h | Dio_LevelType |
| Dio | Dio.h | Dio_PortLevelType |
| Dio | Dio.h | Dio_PortType |
| EcuM | EcuM.h | EcuM_WakeupSourceType |
| Icu | Icu.h | Icu_ChannelType |
| Spi | Spi.h | Spi_ChannelType |
| Spi | Spi.h | Spi_DataBufferType |
| Spi | Spi.h | Spi_NumberOfDataType |
| Spi | Spi.h | Spi_SequenceType |
| Spi | Spi.h | Spi_StatusType |
| Std | Std_Types.h | Std_ReturnType |
| Std | Std_Types.h | Std_VersionInfoType |

### 7.2. 类型定义

#### 7.2.1. CanTrcv_ConfigType

结构类型（**Structure**），元素为实现特定（**Implementation specific**）。这是包含**CAN**收发器驱动程序整体初始化数据以及影响所有收发器的设置的外部数据结构的类型。此外，它还包含指向收发器配置结构的指针。初始化数据结构的内容是**CAN**收发器硬件特定的。可通过**CanTrcv.h**获得。

#### 7.2.2. CanTrcv_PNActivationType

枚举类型（**Enumeration**），用于描述**CanTrcv**中的**PN**唤醒功能是启用还是禁用。取值范围：**PN_ENABLED**：**CanTrcv**中的**PN**唤醒功能已启用；**PN_DISABLED**：**CanTrcv**中的**PN**唤醒功能已禁用。可通过**CanTrcv.h**获得。

#### 7.2.3. CanTrcv_TrcvFlagStateType

枚举类型（**Enumeration**），提供收发器硬件中标志的状态。取值范围：**CANTRCV_FLAG_SET**：标志在收发器硬件中被设置；**CANTRCV_FLAG_CLEARED**：标志在收发器硬件中被清除。可通过**CanTrcv.h**获得。

#### 7.2.4. CanTrcv_TrcvModeType

枚举类型（**Enumeration**），**CAN**收发器驱动程序的操作模式。取值范围：**CANTRCV_TRCVMODE_SLEEP**：收发器模式 **SLEEP**；**CANTRCV_TRCVMODE_STANDBY**：收发器模式 **STANDBY**；**CANTRCV_TRCVMODE_NORMAL**（0x00）：收发器模式 **NORMAL**。可通过**Can_GeneralTypes.h**获得。

#### 7.2.5. CanTrcv_TrcvWakeupModeType

枚举类型（**Enumeration**），该类型应用于控制**CAN**收发器的唤醒事件和唤醒通知。取值范围：**CANTRCV_WUMODE_ENABLE**（0x00）：在寻址的收发器上启用唤醒事件的通知；**CANTRCV_WUMODE_DISABLE**（0x01）：在寻址的收发器上禁用唤醒事件的通知；**CANTRCV_WUMODE_CLEAR**（0x02）：在寻址的收发器上清除存储的唤醒事件。可通过**Can_GeneralTypes.h**获得。

#### 7.2.6. CanTrcv_TrcvWakeupReasonType

枚举类型（**Enumeration**），该类型详细表示**CAN**收发器检测到的唤醒原因。取值范围：**CANTRCV_WU_ERROR**（0x00）：由于错误而未检测到唤醒原因。仅当错误事先报告给**DEM**时才可报告该值；**CANTRCV_WU_NOT_SUPPORTED**（0x01）：收发器不支持任何唤醒原因信息；**CANTRCV_WU_BY_BUS**（0x02）：收发器已检测到网络导致了**ECU**的唤醒；**CANTRCV_WU_INTERNALLY**（0x03）：收发器已检测到网络通过请求 **NORMAL** 模式唤醒了**ECU**；**CANTRCV_WU_RESET**（0x04）：收发器已检测到「唤醒」是由于**ECU**复位；**CANTRCV_WU_POWER_ON**（0x05）：收发器已检测到「唤醒」是由于上电后的**ECU**复位；**CANTRCV_WU_BY_PIN**（0x06）：收发器在收发器的某个引脚（而非**CAN**总线）上检测到了唤醒事件；**CANTRCV_WU_BY_SYSERR**（0x07）：收发器已检测到**ECU**的唤醒是由硬件相关设备故障引起的。可通过**Can_GeneralTypes.h**获得。

### 7.3. 函数定义

#### 7.3.1. CanTrcv_Init

**说明**: 初始化 CanTrcv 模块。

```C
void CanTrcv_Init ( const CanTrcv_ConfigType* ConfigPtr )
```

#### 7.3.2. CanTrcv_SetOpMode

**说明**: 将收发器的模式设置为值 OpMode。

```C
Std_ReturnType CanTrcv_SetOpMode ( 
    uint8 Transceiver, CanTrcv_TrcvModeType OpMode )
```

#### 7.3.3. CanTrcv_GetOpMode

**说明**: 获取收发器的模式，并保存在**OpMode**中返回。

```C
Std_ReturnType CanTrcv_GetOpMode ( 
    uint8 Transceiver, CanTrcv_TrcvModeType* OpMode )
```

#### 7.3.4. CanTrcv_GetBusWuReason

**说明**: 获取收发器的唤醒原因，并保存在参数**Reason**中返回。

```C
Std_ReturnType CanTrcv_GetBusWuReason ( 
    uint8 Transceiver, CanTrcv_TrcvWakeupReasonType* reason )
```

#### 7.3.5. CanTrcv_VersionInfo

**说明**: 获取模块的版本并保存在**VersionInfo**中返回。

```C
void CanTrcv_GetVersionInfo ( Std_VersionInfoType* versioninfo )
```

#### 7.3.6. CanTrcv_SetWakeupMode

**说明**: 根据TrcvWakeupMode启用、禁用或清除收发器的唤醒事件。。

```C
Std_ReturnType CanTrcv_SetWakeupMode ( 
    uint8 Transceiver, CanTrcv_TrcvWakeupModeType TrcvWakeupMode )
```

#### 7.3.7. CanTrcv_GetTrcvSystemData

**说明**: 读取收发器配置/状态数据，并通过参数**TrcvSysData**返回。 此API仅在**CanTrcvHwPnSupport = TRUE**时存在。

```C
Std_ReturnType CanTrcv_GetTrcvSystemData ( 
    uint8 Transceiver, uint32* TrcvSysData )
```

#### 7.3.8. CanTrcv_ClearTrcvWufFlag

**说明**: 清除收发器硬件中的WUF标志。该API只有在**CanTrcvHwPnSupport = TRUE**时才存在。

```C
Std_ReturnType CanTrcv_ClearTrcvWufFlag ( uint8 Transceiver )
```

#### 7.3.9. CanTrcv_ReadTrcvTimeoutFlag

**说明**: 从收发器硬件读取超时标志的状态。该API只有在**CanTrcvHwPnSupport = TRUE**时才存在。

```C
Std_ReturnType CanTrcv_ReadTrcvTimeoutFlag ( 
    uint8 Transceiver, CanTrcv_TrcvFlagStateType* FlagState )
```

#### 7.3.10. CanTrcv_ClearTrcvTimeoutFlag

**说明**: 清除收发器硬件中超时标志的状态。该API只有在**CanTrcvHwPnSupport = TRUE**时才存在。

```C
Std_ReturnType CanTrcv_ClearTrcvTimeoutFlag ( uint8 Transceiver )
```

#### 7.3.11. CanTrcv_ReadTrcvSilenceFlag

**说明**: 从收发器硬件读取沉默标志的状态。该API只有在**CanTrcvHwPnSupport = TRUE**时才存在。

```C
Std_ReturnType CanTrcv_ReadTrcvSilenceFlag ( 
    uint8 Transceiver, CanTrcv_TrcvFlagStateType* FlagState )
```

#### 7.3.12. CanTrcv_CheckWakeup

**说明**: 在检测到唤醒中断的情况下，CanIf调用的服务。

```C
Std_ReturnType CanTrcv_CheckWakeup ( uint8 Transceiver )
```

#### 7.3.13. CanTrcv_SetPNActivationState

**说明**: 次API将收发器的唤醒配置为待机和睡眠模式，CAN收发器由远程唤醒模式（标准CAN唤醒）或配置的远程唤醒帧唤醒。

```C
Std_ReturnType CanTrcv_SetPNActivationState ( 
    CanTrcv_PNActivationType ActivationState )
```

#### 7.3.14. CanTrcv_CheckWakeFlag

**说明**: 从收发器硬件请求检查唤醒标志的状态。

```C
Std_ReturnType CanTrcv_CheckWakeFlag (uint8 Transceiver )
```

#### 7.3.15. CanTrcv_DeInit

**说明**: 取消初始化CanTrcv模块。

```C
void CanTrcv_DeInit ( void )
```

### 7.4. 调度函数

本章列出 **CanTrcv** 模块提供的、由基础软件模块调度器（**BSW Module Scheduler**）直接调用的所有函数。

#### 7.4.1. CanTrcv_MainFunction

**说明**: 用于扫描所有总线以查找唤醒事件并执行这些事件的服务。

```C
void CanTrcv_MainFunction ( void )
```

#### 7.4.2. CanTrcv_MainFunctionDiagnostics

**说明**: 定期读取收发器诊断状态并相应报告生产或开发的错误。

```C
void CanTrcv_MainFunctionDiagnostics ( void )
```

### 7.5. 回调通知

由于 **CanTrcv** 是驱动程序模块，它不为下层模块提供任何回调函数。

### 7.6. 期望接口

本章列出模块 **CanTrcv** 需要从其他模块获得的所有函数。

#### 7.6.1. 必需接口

本章定义了实现该模块核心功能所需的所有接口。

| API函数 | 头文件 | 说明 |
| --- | --- | --- |
| CanIf_TrcvModeIndication | CanIf_CanTrcv.h | 该服务以抽象的 **CanIf TransceiverId** 指示相应**CAN**收发器的收发器状态转换。 |
| Det_ReportRuntimeError | Det.h | 报告运行时错误的服务。如果已配置回调（callout），则应调用该回调。 |

#### 7.6.2. 可选接口

本章定义了实现该模块可选功能所需的所有接口。

| API函数 | 头文件 | 说明 |
| --- | --- | --- |
| CanIf_CheckTrcvWakeFlagIndication | CanIf_CanTrcv.h | 该服务以抽象的 **CanIf TransceiverId** 指示相应**CAN**收发器已完成对其唤醒标志的检查。该指示用于应对异步的收发器通信。 |
| CanIf_ClearTrcvWufFlagIndication | CanIf_CanTrcv.h | 该服务以抽象的 **CanIf TransceiverId** 指示收发器已清除 **WufFlag**。 |
| CanIf_ConfirmPnAvailability | CanIf_CanTrcv.h | 该服务以抽象的 **CanIf TransceiverId** 指示收发器正以 **PN** 通信模式运行。 |
| Dem_SetEventStatus | Dem.h | 由**SW-C**或**BSW**模块调用，以向**DEM**报告监控状态信息。调用 **Dem_SetEventStatus** 的**BSW**模块可以安全地忽略返回值。仅当（{Dem/DemConfigSet/DemEventParameter/DemEventReportingType} == **STANDARD_REPORTING**）时该API才可用。 |
| Det_ReportError | Det.h | 报告开发错误的服务。 |
| Dio_ReadChannel | Dio.h | 返回指定 **DIO** 通道的值。 |
| Dio_ReadChannelGroup | Dio.h | 该服务读取端口中相邻位的一个子集。 |
| Dio_ReadPort | Dio.h | 返回该端口所有通道的电平。 |
| Dio_WriteChannel | Dio.h | 设置通道电平的服务。 |
| Dio_WriteChannelGroup | Dio.h | 将端口中相邻位的一个子集设置为指定电平的服务。 |
| Dio_WritePort | Dio.h | 设置端口值的服务。 |
| EcuM_SetWakeupEvent | EcuM.h | 设置唤醒事件。 |
| Icu_DisableNotification | Icu.h | 该函数禁用通道的通知。 |
| Icu_EnableNotification | Icu.h | 该函数启用给定通道的通知。 |
| Spi_GetStatus | Spi.h | 返回 **SPI** 处理程序/驱动程序软件模块状态的服务。 |
| Spi_ReadIB | Spi.h | 用于从参数指定的 **IB SPI** 处理程序/驱动程序通道同步读取一个或多个数据的服务。 |
| Spi_SetupEB | Spi.h | 为指定的 **EB SPI** 处理程序/驱动程序通道设置缓冲区和数据长度的服务。 |
| Spi_SyncTransmit | Spi.h | 在 **SPI** 总线上传输数据的服务。 |
| Spi_WriteIB | Spi.h | 用于向参数指定的 **IB SPI** 处理程序/驱动程序通道写入一个或多个数据的服务。 |

#### 7.6.3. 可配置接口

**CanTrcv**没有可配置接口。

<section id="wechat">

<h4>微信扫一扫，获取更多及时资讯</h4>

<img src="wechat.png" alt="微信扫一扫"/>

</section>