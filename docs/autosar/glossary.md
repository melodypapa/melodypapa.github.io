---
title: "AUTOSAR 术语表（缩略语与缩写）"
---

本页汇总各 AUTOSAR 模块文章以及 AUTOSAR TR 术语表（Foundation）的术语，按字母排序。

## A


**Acquisition Time**
> 采集时间 = 采样时间（**Sample Time**）+ 转换时间（**Conversion Time**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC**
> 模数转换器（**Analogue Digital Converter**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Channel**
> **ADC**通道是指绑定到一个端口引脚的逻辑**ADC**实体。同时多个**ADC**实体也可以映射到同一个端口引脚。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Channel Group**
> **ADC**通道组是指由一组**ADC**通道链接到同一个**ADC**硬件单元（**ADC HW Unit**）。例如：一个采样保持器（**Sample & Hold**）和一个**A/D**转换器。整个组的转换由一个触发源触发。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC HW Unit**
> 微控制器的输入电子设备，包括执行模拟到数字转换所需的所有部件。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Module**
> ADC的基础软件模块ADC驱动模块（**ADC Driver**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Result Buffer**（**ADC Streaming Buffer**，**ADC Stream Buffer**）
> **ADC**驱动程序的用户必须为每个组提供一个缓冲区。如果选择流式访问模式（**streaming access mode**），此缓冲区可以保存同一组通道的多个样本。如果选择单一访问模式（**Single Access Mode**），每个组通道的一个样本将保存在缓冲区中。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**AI**
> 存活指示（**Alive Indication**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Alive Counter**
> **WdgM** 中在**检查点**上下文内的独立数据资源，用于跟踪和处理该**检查点**的**存活指示**数量。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Alive Indication**
> 由**被监督实体**的**检查点**提供的指示，用于向**WdgM** 标识其存活状态。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Alive Supervision**
> 一种监督，用于检查**被监督实体**的执行是否足够频繁且不过于频繁（包括容差）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**API**
> 应用编程接口（**Application Programming Interface**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**Atomic sequence/ atomic piece**
> 原子序列是一段不得被中断的测试。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
## B


**Background test**
> 后台测试由 **SW** 调度器/**RTOS** 周期性调用。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**BIST**
> 内建自测试（**Built in Self Test**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**BSW**
> 基础软件（**Basic Software**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**BswM**
> 基础软件模式管理器（**Basic Software Mode Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
## C


**Caller/calling entity**
> 调用者/调用实体位于较高的 **AUTOSAR** 或 **ISO** 层。它是 **API** 调用的用户。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Checkpoint**
> **被监督实体**控制流中的一个点，在该处向**WdgM** 报告活动。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Com**
> 通信（**Communication**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**Conversion Mode**
> One-Shot：**ADC**通道组的转换在触发后执行一次，结果写入所分配的结果缓冲区。触发可以是软件**API**调用或硬件事件。Continuous：**ADC**通道组的转换在软件**API**调用（启动）后连续执行，结果写入所分配的结果缓冲区。转换本身自动运行（由硬件/中断控制）。连续转换可通过软件**API**调用（停止）停止。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Conversion Time**
> 转换时间是指将采样的模拟值转换为数值所需的时间。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Core**
> **CPU** 及其紧邻的功能资源。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**CPU**
> 中央处理器（**Central Processing Unit**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Cross-Cluster External Graph**
> 一种特殊的**外部图**，在集群式软件架构下跨越多个**软件集群**（**Software Cluster**）。其配置依赖于模式（由**宿主软件集群**（**Host Software Cluster**）控制），并且另外具有专门的配置结构。注意：单个**软件集群**内的**外部图**可以在不使用集群式软件架构专门配置结构的情况下建模。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**CSUM/Checksum/signature**
> 测试执行结果的数值表示。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

## D


**DCM**
> 诊断通信管理器（**Diagnostic Communication Manager**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**Deadline End Checkpoint**（**Deadline Stop Checkpoint**）
> 为其配置了**截止时间监督**、并且是某个特定**截止时间监督**终点的**检查点**。一个**检查点**可以同时是**截止时间起始检查点**和**截止时间结束检查点**——即当**截止时间监督**被串联时。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Deadline Start Checkpoint**
> 为其配置了**截止时间监督**、并且是某个特定**截止时间监督**起点的**检查点**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Deadline Supervision**
> 一种监督，用于检查两个**检查点**之间的执行时间是否小于给定的执行时间上限。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**DEM**
> 诊断事件管理器（**Diagnostic Event Manager**）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**DET**
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**DIP**
> 数字输入/输出（**Digital Input/Output**）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

## E


**EAI**
> 期望存活指示（**Expected Alive Indications**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**ECU**
> 电子控制单元（**Electronic Control Unit**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**EcuC**
> **ECU** 配置（**ECU Configuration**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**EcuM**
> **ECU** 状态管理器（**ECU State Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**e.g.**
> （拉丁语）exempli gratia =（英语）for example，即「例如」。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**i.e.**
> （拉丁语）id est =（英语）that is，即「也就是说」。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**Expired Supervision Cycle**
> 一个**监督周期**，其中**存活监督**已失败其两个升级步骤（**存活计数器**失败的**期望存活指示**数量（包括容差）超过允许的失败参考周期次数）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**External device**
> 物理外部实体；例如另一个微控制器。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**External Graph**
> 可能涉及多于一个**被监督实体**的**图**。其配置依赖于模式。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**External Transition**
> **外部转换**是两个**检查点**之间的**转换**，其中这两个**检查点**属于不同的**被监督实体**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
## F


**Fast-Mode**
> 对看门狗硬件的触发必须以较短的超时期限完成。例如，该模式可用于 **ECU** 的正常运行。例如，看门狗硬件被配置为窗口模式（触发看门狗必须发生在超时期限内的特定最小/最大边界中）且超时期限为 5 毫秒。
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**Failed Supervision Reference Cycle**
> 一个**监督参考周期**，其结束时刻检测到**存活计数器**与**期望存活指示**数量之间存在偏差（包括容差）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**FiM**
> 功能抑制管理器（**Function Inhibition Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Foreground test**
> 前台测试是同步测试，不得被中断。它通过用户应用程序调用。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

## G


**Global Supervision Status**
> 汇总所有**被监督实体****局部监督状态**的状态。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Golden (Ref.) Value**
> 用于与先前计算出的测试结果值进行比较的参考值（例如校验和/签名）。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Good Case**
> 执行完成且未报告错误。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**GPT**
> 通用定时器（**General Purpose Timer**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**GPT Predef Timer**
> **GPT Predef Timer** 是 **GPT** 驱动程序提供的自由运行递增计数器。哪些 **GPT Predef Timer** 可用取决于硬件（时钟、硬件定时器、预分频器、定时器寄存器宽度等）和配置。**GPT Predef Timer** 具有预定义的物理时间单位和范围。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**Graph**
> 控制流图（**Control Flow Graph**）。一组通过**转换**相连的**检查点**，其中至少有一个**检查点**是**初始检查点**。在该**图**的任意两个**检查点**之间都存在一条（通过**转换**的）路径。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
## H


**Hardware Trigger**
> 硬件触发是**ADC**内部触发信号，用于启动ADC通道组的一次转换。**ADC**硬件触发在ADC硬件内部生成（例如：基于**ADC**定时器或触发沿信号）。触发硬件是强耦合或者直接集成在**ADC**的硬件中。当检测到硬件触发后，无需软件即可启动**ADC**通道组转换。**注意：**即使**ADC**硬件不支持硬件触发，也可以通过软件触发结合**GPT/ICU**驱动程序来实现类似的行为。（例如：在GPT定时器通知函数中，启动软件触发的**ADC**通道组的转换）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**HW**
> 硬件（**Hardware**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

## I


**I-PDU**
> 交互层 **PDU**（**Interaction Layer PDU**）。在 **AUTOSAR** 中，交互层等价于通信服务层。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**ICU**
> 输入捕获单元（**Input Capture Unit**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**ID**
> 标识符（**Identifier**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Internal Graph**
> 不跨越若干**被监督实体**的**图**。其配置与模式无关，并且可以通过禁用对应的**被监督实体**而被禁用。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Internal Transition**
> **内部转换**是同一个**被监督实体**内两个**检查点**之间的**转换**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**IRQ**
> 中断请求（**Interrupt Request**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
## L


**L-PDU**
> 数据链路层 **PDU**（**Data Link Layer PDU**）。在 **AUTOSAR** 中，数据链路层等价于通信硬件抽象和微控制器抽象层。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**L1**
> 第一级存储器（**1st level memory**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**L2**
> 第二级存储器（**2nd level memory**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Local Supervision Status**
> 表示单个**被监督实体**当前存活监督结果的状态。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Logical Supervision**
> 一种对软件的在线监督，用于检查软件（**被监督实体**或一组**被监督实体**）是否按程序员（即已开发的代码）定义的顺序执行。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
## M


**MCAL**
> 微机抽象层（**Microcomputer Abstraction Layer**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**MCU**
> 微控制器单元（**Microcontroller Unit**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Mode**
> 模式是车辆中运行的各个状态机的特定状态集合，这些状态与某个特定实体相关，例如 **SW-C**、**BSW** 模块、应用或整个车辆。在其生命周期内，一个实体在一组互斥的模式之间切换。这些切换由环境数据触发，例如信号接收、操作调用。在**看门狗管理器**的上下文中，一个模式由一组配置选项定义。被监督的**被监督实体**集合可以随模式而变化。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**MPU**
> 内存保护单元（**Memory Protection Unit**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
## N


**N-PDU**
> 网络层 **PDU**（**Network Layer PDU**）。在 **AUTOSAR** 中，网络层等价于传输协议。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**NOP, nop**
> 空操作（**Null Operation**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## O


**Off-Mode**
> 看门狗硬件被禁用/关闭。这样做可能是为了关闭整个 **ECU**，而不遭受仍在运行的外部看门狗的周期性复位。对于安全关键系统，该模式可能不被允许。在这种情况下，必须将 **Wdg** 模块配置为禁止切换到此模式。
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**OSEK/VDX**
> 1993 年 5 月，**OSEK** 作为德国汽车工业的一个联合项目创立，旨在为车辆内分布式控制单元的开放式架构建立一个行业标准。**OSEK** 是德语术语「Offene Systeme und deren Schnittstellen für die Elektronik im Kraftfahrzeug」（英语：Open Systems and the Corresponding Interfaces for Automotive Electronics）的缩写。初始项目合作伙伴为 **BMW**、**Bosch**、**Daimler Chrysler**、**Opel**、**Siemens**、**VW** 以及作为协调方的卡尔斯鲁厄大学 **IIIT**。法国汽车制造商 **PSA** 和 **Renault** 于 1994 年加入 **OSEK**，引入了他们的 **VDX**（**Vehicle Distributed eXecutive**）方案——法国汽车工业内的一个类似项目。在 1995 年 10 月的第一次研讨会上，**OSEK/VDX** 小组展示了 **OSEK** 与 **VDX** 之间协调一致的规范成果。1997 年 10 月第 2 届国际 **OSEK/VDX** 研讨会之后，发布了规范的第二版。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**OS**
> 操作系统（**Operating System**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## P


**Partial test**
> 部分测试定义为一个或多个「硬件资源」的测试。（部分测试是可中断的，因为它在后台模式下执行。）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**PDU**
> 协议数据单元（**Protocol Data Unit**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

## R


**Resource**
> 「硬件资源」是 **CoreTest** 驱动程序用户可以选择的最小单元（实例）。它可以在一个或多个原子序列中被测试。它是执行特定功能（例如 **IRQ** 控制器）的内核内部单元。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**RTE**
> 运行时环境（**Runtime Environment**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
## S


**Sampling Time, Sample Time**
> 采样时间是指对模拟值进行采样的时间（例如：加载电容器，……）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SC**
> 监督周期（**Supervision Cycle**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**SDU**
> 服务数据单元（**Service Data Unit**）——**PDU** 的载荷。
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）

**SE**
> 被监督实体（**Supervised Entity**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**SFR**
> 特殊功能寄存器（**Special Function Register**），**MCU** 寄存器
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）

**Slow-Mode**
> 对看门狗硬件的触发可以以较长的超时期限完成。例如，该模式可用于系统启动/初始化阶段。例如，看门狗硬件被配置为翻转模式（对触发的时间点没有约束）且超时期限为 20 毫秒。
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**Software Trigger**
> 软件触发是一个软件**API**调用，用于启动转换一个**ADC**通道组或一系列连续**ADC**通道组转换的。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SPI**
> 串行外设接口（**Serial Peripheral Interface**）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**SRC**
> 监督参考周期（**Supervision Reference Cycle**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervised Entity**
> 被纳入**WdgM** 监督的软件实体。每个**被监督实体**恰好具有一个标识符。**被监督实体**表示软件组件类型或基础软件模块某个实例内的一组**检查点**。在一个软件组件类型或基础软件模块的实例中，可以有零个、一个或多个**被监督实体**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervised Entity Identifier**
> 在一个应用内唯一标识某个**被监督实体**的**标识符**。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervision Counter**
> 在**被监督实体**上下文内的独立数据资源，由**WdgM** 在每个**监督周期**期间更新，并被**存活监督**算法用于执行对已计数**存活指示**的检查。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervision Cycle**
> **WdgM****监督参考周期**的时基，在其中执行周期性的**存活监督**。它同时也是更新**全局监督状态**以及执行由此产生的恢复动作的间隔。这在所属 **WdgM** 的主函数每次被调用时完成，并且依赖于模式（在切换模式时可能变化）。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Supervision Reference Cycle**
> **存活监督**用于执行已计数**存活指示**检查所使用的**监督周期**数量（对每个**被监督实体**分别确定），并且依赖于模式。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**SW**
> 软件（**Software**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SW-C**
> 软件组件（**Software Component**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
## T


**Target time**
> 目标时间：到达该值时应有某事发生。其行为取决于配置和已启用的功能。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**test interval**
> **CoreTest** 测试间隔：在配置为构成一个完整内核测试的硬件资源上（后台模式下执行的）所有部分测试的总和。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Test Interval Id**
> 测试间隔的标识符，每开始一个新的测试间隔时应递增。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Tick**
> 定义定时器分辨率，即定时器一次递增的持续时间。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**Timer channel**
> 表示分配给一个定时器硬件的逻辑定时器实体。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**TP**
> 传输协议（**Transport Protocol**）
> 来源：[AUTOSAR Communication Stack Types（通信栈类型）](general/communication_stack_types/index.md)（SWS_CommunicationStackTypes · R23-11）
## U


**uC**
> 微控制器（**Microcontroller**）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
## W

**WDG**
> 看门狗（**Watchdog**，模块特定前缀）
> 来源：[AUTOSAR Watchdog Driver（看门狗驱动）](safety/watchdog_driver/index.md)（SWS_WatchdogDriver · R23-11）

**WdgM**
> 看门狗管理器（**Watchdog Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
