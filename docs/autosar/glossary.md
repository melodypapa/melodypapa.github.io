---
title: "AUTOSAR 术语表（缩略语与缩写）"
---

本页汇总各 AUTOSAR 模块文章以及 AUTOSAR TR 术语表（Foundation）的术语，按字母排序。

## A


**Accuracy**
> 精度（**Accuracy**）取决于用于采样或者生成的硬件外围设备。如：**ADC**转换器可以是 8/10/12/16 位转换器
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

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
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Atomic sequence/ atomic piece**
> 原子序列是一段不得被中断的测试。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Attributes**
> 属性（**Attributes**）是**ECU**中存在的每个**ECU**信号所包含的软件或者硬件特性。一些属性是固定的，由端口定义决定。还有一些属性是可以在**I/O**硬件抽象中进行配置的。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**AUTOSAR**
> 汽车开放系统架构（**AUTomotive Open System ARchitecture**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

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
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**BswM**
> 基础软件模式管理器（**Basic Software Mode Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**BSWMD**
> 基本软件模块说明（**Basic SoftWare Module Description**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

## C


**Callback**
> 术语回调函数（**Callback**）主要用于**API**服务，实现通知其他**BSW**模块。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Caller/calling entity**
> 调用者/调用实体位于较高的 **AUTOSAR** 或 **ISO** 层。它是 **API** 调用的用户。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**Callout**
> **Callout**是一种函数**Stub**。主要在配置时进行填写，目的是向提供**Callout**函数的模块添加功能。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Class**
> 一个类（**Class**）代表一组具有相似电气特性的信号。如：模拟类（**Analogue class**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Client-Server communication**
> 客户端-服务器通信（**Client-Server communication**）涉及两个实体。客户端是要求服务的一方，服务器是提供服务的一方。客户端发起通信，请求服务器执行服务，必要时传输参数集合。服务器以**RTE**的形式，等待来自客户端的传入通信请求，执行请求的服务并发送对客户端请求的响应。因此服务启动的方向是用来对**AUTOSAR**软件组件是客户端还是服务器分类的主要标识。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Checkpoint**
> **被监督实体**控制流中的一个点，在该处向**WdgM** 报告活动。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

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

**C/S**
> 客户端/服务器（**Client/Server**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**CSUM/Checksum/signature**
> 测试执行结果的数值表示。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

## D


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

**DET**
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

## E


**EAI**
> 期望存活指示（**Expected Alive Indications**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**ECU**
> 电子控制单元（**Electronic Control Unit**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ECU pin**
> ECU引脚（**ECU pin**）是**ECU**与电子系统其余部分的电气硬件连接。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ECU Signal**
> ECU信号（**ECU Signal**）是电信号的软件表示。一个**ECU**信号具有一些属性（**Attribute**）和一个符号名称（**Symbolic name**）。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**ECU Signal Group**
> ECU信号组（**ECU Signal Group**）是一组电信号的软件表示。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**EcuM**
> **ECU** 状态管理器（**ECU State Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Electrical Signal**
> 电信号（**Electrical Signal**）代表**ECU**引脚上的物理信号。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

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
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

## I


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

**Inversion**
> 物理值与逻辑值的反转（**Inversion**）。此属性不可见，但可以由**I/O**硬件抽象来实现，并向用户传递预期值。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**IoHwAb**
> 输入/输出硬件抽象（**Input/Output Hardware Abstraction**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**IRQ**
> 中断请求（**Interrupt Request**）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**ISR**
> 中断服务程序（**Interrupt Service Routine**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

## L


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
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

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


**NOP, nop**
> 空操作（**Null Operation**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## O


**OS**
> 操作系统（**Operating System**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

## P


**Partial test**
> 部分测试定义为一个或多个「硬件资源」的测试。（部分测试是可中断的，因为它在后台模式下执行。）
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

## R


**Range**
> 范围（**Range**）在这里是一个功能范围（**functional range**），而不是电气范围（**electrical range**）。所有范围都用于功能的需要或者诊断的检测。对于模拟**ECU**信号，可以定义上下限值 [lowerLimit...upperLimit]（电压、电流）。对于电阻信号和时序信号（周期）的特殊情况，下限值（**lowerLimit**）不能为负。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Resolution**
> 分辨率（**Resolution**）属性适用于依赖于范围和数据类型的许多类别。如：(upperLimit - lowerLimit) / (2<sup>datatypelength</sup> -1)。 对于其他类别，它可能是已知和被定义的。如：[-12 Volts…+12Volts]，数据类型: 16 bits，**Resolution** 为 24 / 65535。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Resource**
> 「硬件资源」是 **CoreTest** 驱动程序用户可以选择的最小单元（实例）。它可以在一个或多个原子序列中被测试。它是执行特定功能（例如 **IRQ** 控制器）的内核内部单元。
> 来源：[AUTOSAR CoreTest（内核测试）](mcal/core_test/index.md)（SWS_CoreTest · R23-11）

**RTE**
> 运行时环境（**Runtime Environment**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
## S


**Sampling rate**
> 采样率（**Sampling rate**）是获得信号值所需的时间段。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Sampling Time, Sample Time**
> 采样时间是指对模拟值进行采样的时间（例如：加载电容器，……）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SC**
> 监督周期（**Supervision Cycle**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**SE**
> 被监督实体（**Supervised Entity**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**Sender-receiver communication**
> 发送方-接收方通信涉及原子数据元素组成的信号的发送和接收，这些原子数据元素由一个组件发送给另一个或多个组件。发送方-接收方接口可以包含多个数据元素。发送方-接收方通信是单向的 接收方发送的任何回复都可以视为一个单独的发送方-接收方通信。接收方组件的端口可以读取接口描述定义的数据元素，而提供方组件的端口可以按照接口描述定义写入数据元素。
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**SFR**
> 特殊功能寄存器（**Special Function Register**），**MCU** 寄存器
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）

**Software Trigger**
> 软件触发是一个软件**API**调用，用于启动转换一个**ADC**通道组或一系列连续**ADC**通道组转换的。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**S/R**
> 发送方/接收方（**Sender/Receiver**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

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
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**SW-C**
> 软件组件（**Software Component**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

**SWC**
> 软件组件（**SoftWare Component**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

**Symbolic name**
> ECU信号的符号名称（**Symbolic name**）在**I/O**硬件抽象模块中是用来建立链接的。（包括：功能、引脚等）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）

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
## U


**uC**
> 微控制器（**Microcontroller**）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
## W

**WdgM**
> 看门狗管理器（**Watchdog Manager**）
> 来源：[AUTOSAR Watchdog Manager（看门狗管理器）](safety/watchdog_manager/index.md)（SWS_WatchdogManager · R23-11）

## X


**XML**
> 可扩展标记语言（**eXtensible Markup Language**）
> 来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](io/iohwab/index.md)（SWS_IOHardwareAbstraction · R23-11）
