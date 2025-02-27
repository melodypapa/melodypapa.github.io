<section id="title">AUTOSAR Operating System（操作系统）</section>

# 1. 简介和功能概述

本文档描述了 **AUTOSAR** 操作系统的基本要求，以满足 **AUTOSAR SRS** [1] 中提出的顶级需求。

一般来说，操作系统可以根据其特性分为不同的组，例如：静态配置与动态管理。对**AUTOSAR OS**进行分类，以下是**OS**的基本特征：

* 可以静态配置和扩展的。
* 可以适应实时性能的推理。
* 可以提供基于优先级的调度策略。
* 在运行时可以提供保护功能（如：内存、时序等）。
* 可以部署在低端控制器，而无需外部资源。

本功能集定义了当代汽车 **ECU** 中，除了远程信息处理（**Telematic**）和信息娱乐（**Infotainment**）系统以外的常用操作系统类型。因为远程信息处理以及信息娱乐系统会继续使用 **AUTOSAR** 框架下的专有操作系统（如：**Windows CE**、**VxWorks**、**QNX**等）。如果需要在这些专有操作系统上运行 **AUTOSAR** 组件，则本文档中定义的接口需作为操作系统抽象层 OSAL（**Operating System Abstraction Layer**）来提供支持。

本文档使用行业标准[2](**ISO 17356-3**) 作为 **AUTOSAR OS** 的基础。在阅读本文件前需熟悉此标准规范。本文档仅仅描述了参考文档[2]的扩展和限制。

# 2. 缩略语

下面的词汇表包括与参考文档[3](AUTOSAR 词汇表) 中未包含的 **AUTOSAR** 操作系统模块相关的首字母缩略词和缩略语。

**API** 
> 应用程序接口（**Application Programming Interface**）

**AR** 
> AUTOSAR

**ARTI** 
> AUTOSAR 运行时接口（**AUTOSAR Run-time interface**）

**BSW** 
> 基础软件（**Basic Software**）

**BSWMD**
> 基础软件模块说明（**Basic Software Module Description**）

**CDD**
> 复杂驱动程序（**Complex Driver**）

**COM** 
> 通讯（**Communication**）

**ECC** 
> 扩展一致性等级（**Extended Conformance Class**）

**ECU** 
> 电子控制单元（Electronic Control Unit）

**HW** 
> 硬件（**Hardware**）

**ID** 
> 标识符（**Identifier**）

**IOC** 
> 操作系统间应用程序通信器（**Inter OS-Application communicator**）

**ISR** 
> 中断服务程序（**Interrupt Service Routine**）

**LE** 
> 可定位实体（**locatable entity**）是一个不同的软件，无论它位于哪个内核，都具有相同的效果。

**MC** 
> 多核（**Multi-Core**）

**MCU** 
> 微控制器单元（**Microcontroller Unit**）

**ME** 
> 互斥（**Mutual exclusion**）

**MPU** 
> 内存保护单元（**Memory Protection Unit**）

**NMI** 
> 不可屏蔽中断（**Non maskable interrupt**）

**OIL** 
> OSEK 实现语言（**OSEK Implementation Language**）

**OS** 
> 操作系统（**Operating System**）

**OSEK/VDX** 
> 用于机动车辆电子设备的开放系统及其接口（**Offene Systeme und deren Schnittstellen für die Elektronik im Kraftfahrzeug**）

**RTE** 
> 运行环境（**Run-Time Environment**）

**RTOS** 
> 实时操作系统（**Real Time Operating System**）

**SC** 
> 单核（**Single-Core**）

**SLA** 
> 软件分层架构（**Software Layered Architecture**）

**SW** 
> 软件（**Software**）

**SWC** 
> 软件组件（**Software Component**）

**SWFRT** 
> 软件自由运行定时器（**Software FreeRunningTimer**）

# 3. 相关文档

## 3.1. 输入文件及相关标准和规范

[1] Requirements on Operating System
> AUTOSAR_SRS_OS
 
[2] ISO 17356-3: 
> Road vehicles – Open interface for embedded automotive applications – Part 3: OSEK/VDX Operating System (OS)

[3] Glossary
> AUTOSAR_TR_Glossary

[4] General Specification of Basic Software Modules
> AUTOSAR_SWS_BSWGeneral

[5] Virtual Functional Bus
> AUTOSAR_EXP_VFB

[6] General Requirements on Basic Software Modules
> AUTOSAR_SRS_BSWGeneral

[7] Requirements on Free Running Timer
> AUTOSAR_SRS_FreeRunningTimer

[8] ISO 17356-6: 
> Road vehicles – Open interface for embedded automotive applications – Part 6: OSEK/VDX Implementation Language (OIL)

[9] Specification of AUTOSAR Run-Time Interface
> AUTOSAR_SWS_ClassicPlatformARTI

[10] Specification of RTE Software
> AUTOSAR_SWS_RTE

[11] Software Component Template
> AUTOSAR_TPS_SoftwareComponentTemplate

[12] Specification of Memory Mapping
> AUTOSAR_SWS_MemoryMapping

## 3.2. 相关规范

因为**AUTOSAR**提供了基础软件模块的通用规范[4]**SWS BSW General**，它也适用于**AUTOSAR**操作系统。所以参考文献规范[4]**SWS BSW General**应被视为 **AUTOSAR** 操作系统的附加和必需规范。

所有与 **OSEK OS** 相关的类型、定义和函数都可以在参考文献[2]中找到。

# 4. 约束和假设

## 4.1. 现有标准

本文件对引用的相关标准和规范做出以下假设：

* 参考文献[2]提供了足够灵活的调度策略来调度 **AUTOSAR** 系统。
* 参考文献[2]是一个成熟的规范，并在全球数百万个 **ECU** 中使用。
* 参考文献[2]没有为在运行时隔离多源软件组件提供足够的支持。
* 参考文献[2]没有提供足够的运行时支持来证明在安全案例中不存在某些类别的故障传播。

## 4.2. 术语

当需求指定多个术语时，规范使用以下运算符：

* **NOT**: 对单个术语的否定，例如：不是周末（**NOT Weekend**）。
* **AND**: 两个术语的结合，例如：周末和周六（**Weekend AND Saturday**）
* **OR** : 两个术语的分离，例如：星期一或星期二（**Monday OR Tuesday**）

但一条需求包含多个术语时，按从左到右评估。优先规则如下：

* 最高优先级**NOT**
* 最低优先级**AND OR**
  
表达式 **NOT X AND Y** 表示 **(NOT X) AND (Y)**。在同一句子中使用相同优先级的运算符时，使用逗号来消除歧义。表达式 **X AND Y, OR Z** 表示 **(X AND Y) OR Z**。

## 4.3. 与 RTE 的互动

**AUTOSAR**系统[5]的配置将软件组件的可运行实体（**runnable**）映射到操作系统调度的（一个或多个）Task任务。Task任务中的所有可运行实体共享相同的保护边界。在 **AUTOSAR** 中，因为软件组件不得包含中断处理程序，所以软件组件被实现为仅在Task任务主体或Task任务集内执行的可运行实体。

可运行实体可以通过 **AUTOSAR RTE** 访问硬件来源的数据。**RTE** 提供了可运行实体和基础软件模块之间的运行时接口。基础软件模块还包括许多由操作系统调度的**Task任务**和 **ISR**。

软件组件模板和基础软件模块的描述提供了有关所需运行时行为的足够信息，以便能够指定配置操作系统所需的任务的属性。

## 4.4. 操作系统抽象层 (OSAL)

不使用 **AUTOSAR** 中定义的操作系统的系统可以使用操作系统抽象层为执行 **AUTOSAR** 软件组件提供平台。**OSAL** 的接口正是为 **AUTOSAR OS** 定义的接口。

## 4.5. 多核硬件假设

目前有几种现有的和建议的多核微处理器硬件架构<sup>1</sup>。由于这些架构提供的功能有相当大的差异，所以本节试图捕捉多核所需的一组通用架构特性。

硬件假设需继续保持假设，而不应成为官方的 **AUTOSAR** 要求。

### 4.5.1. CPU核心功能

1. 在同一块硅片（**silicon**）上会存在多个内核（**core**）。
2. 硬件提供了一种可供软件用来识别不同内核的方法。
3. 硬件支持访问硬件的固定字长的原子读和写操作（**atomic read and atomic write operations**）。
4. 硬件支持一些原子的测试和设置（**AtomicTest-And-Set**）或者类似的功能，可用于构建内核之间共享的临界区。可能还有其他原子操作也存在。
5. 内核可以有相同的指令集。至少在所有内核都会有一讨通用的基本指令集。特定于内心的附加组件可能存在，但无需考虑它们。
6. 内核具有相同的数据表示。例如：相同大小的整数，相同的字节和位顺序等。
7. 如果每个内核存在缓存，**AUTOSAR** 需要硬件或软件中可以支持内存和缓存（**RAM - Cache**）的一致性。软件的支持意味着高速缓存控制器可以通过软件进行编程控制，以便于高速缓存行（**cache lines**）无效或从高速缓存中排除某些内存区域。
8. 如果发生异常（例如：非法的内存引用或被零除），异常需发生在引入异常的内核上。
9. 出于通知目的，可以在任何内核上触发中断/陷阱。

### 4.5.2. 内存功能

* 共享 RAM 可用于所有内核；至少所有内核都可以共享大部分内存。
* Flash闪存至少应在所有内核之间共享。但是如果可以对**Flash/RAM**进行分区，以便从内核到**Flash**有单独的路径，则可以提高性能。
* 假设存在一个单一的地址空间，至少在内存地址空间的共享部分是这样的。
* **AUTOSAR** 多核架构应能够在支持和不支持内存保护的系统上运行。如果存在内存保护，则所有内核都可以被基于硬件的内存保护所覆盖。

### 4.5.3. 多核限制

* 在 **AUTOSAR R4.0** 中，不支持在操作系统启动后激活受 **AUTOSAR** 控制的其他内核。
* 调度算法不会动态地将Task任务分配给不同的内核。
* **AUTOSAR OS** 资源算法不支持跨内核。资源可以在被本地使用，或者被绑定到同一个内核的Task任务之间。但资源不能被绑定到不同内核的Task任务或者ISR之间使用。

## 4.6. 限制

### 4.6.1. 硬件

核心 **AUTOSAR** 操作系统假定可以自由访问由操作系统本身管理的硬件资源，包括但不限于以下硬件：

* 中断控制寄存器（**interrupt control registers**）
* 处理器状态字（**processor status words**）
* 堆栈指针（**stack pointers**）

核心操作系统的特定（扩展）特性扩展了对硬件资源的要求。以下列表概述了有硬件需求的功能。如果不使用这些操作系统功能的系统，可以无需关心以下这些硬件需求。

* 内存保护（**Memory Protection**）：依赖硬件内存保护单元。所有具有写入结果的内存访问（例如，具有写入内存位置的副作用的读取）都应被视为写入。
* 时间保护（**Time Protection**）：用于监控执行时间和到达率的计时器硬件。
* MCU上的特权和非特权模式（**Privileged and non-privileged modes on the MCU**）：保护操作系统免受由写入操作系统控制的寄存器引起的内部损坏。此模式不得允许**OS-Applications**绕过保护（例如：写入管理内存保护的寄存器、写入处理器状态字等）。特权模式必须在受保护操作系统的完全控制下，该操作系统在内部使用该模式并将控制权从不受信任的**OS-Applications**来回转移到受信任的**OS-Applications**。微处理器必须支持使处理器进入这种特权模式的受控方式。
* 本地/全局时间同步（**Local/Global Time Synchronization**）：需要一个全局的时间源。

通常处理器中的硬件故障并不会被操作系统检测到。如果发生硬件故障，操作系统的正确运行则将无法被保证。

由特定操作系统实现管理的资源必须在操作系统的适当配置文件中定义。

### 4.6.2. 编程语言

**AUTOSAR** 操作系统的 **API** 被定义为 **C** 函数调用或宏。如果使用其他语言，则必须适应 **C** 接口。

### 4.6.3. 其他

**AUTOSAR** 操作系统不提供动态内存管理服务。

## 4.7. 适用于汽车领域

因为操作系统在大小和可伸缩性方面具有与参见文档[2]的设计相同的设计约束，所以当前的直接适用领域是车身、底盘和动力传动系ECU（**body, chassis and power train ECUs**）。但是没有理由不可以使用此操作系统来实现信息娱乐应用的 **ECU**。

# 5. 对其他模块的依赖

**AUTOSAR** 操作系统对其他模块没有强制依赖，但是：

* 假设操作系统可以直接使用定时器单元来驱动计数器。
* 如果用户需要直接从全局时间来驱动调度，则全局时间中断是必须的。
* 如果用户需要将ScheduleTable的处理同步到全局时间，操作系统需要使用 **SyncScheduleTable** 服务来获知全局时间。
* 本文档中描述的 **IOC** 提供 **OSApplication** 之间的通信。**IOC** 生成基于 **RTE** 生成器生成的配置信息。另一方面，**RTE** 使用 **IOC** 生成的函数来传输数据。

## 5.1. 文件结构

### 5.1.1. 代码文件结构

操作系统模块的代码文件结构不是固定的，除了参考文档[6] **AUTOSAR_SRS_BSWGeneral** 中要求的。

### 5.1.2. 头文件结构

**IOC** 生成器生成一个附加的头文件 **Ioc.h**。**Ioc.h** 的用户应包括 **Ioc.h** 文件。如果 **IOC** 的实现需要额外的头文件，可以自由地包含它们。头文件是自包含的，这意味着它们将包含所有其他需要的头文件。

### 5.1.3. ARTI 文件结构

为了支持基于 **ARTI** 的调试和跟踪，所有带有 **ARTI** 钩子宏（**ARTI hook macros**）的源文件都应包含一个 **arti.h** 文件。该文件连同相应的 **arti.c** 文件将由 **ARTI** 钩子实现者（即：Tracing工具）提供。 在构建最终的可执行文件时，链接器也会拉入已编译的 **arti.c** 文件。 **ARTI** 钩子宏的使用是可配置的。如果操作系统配置为不使用 **ARTI**，则可以省略包含**arti.h**，并且 **ARTI** 钩子宏可以扩展为空的宏。

# 6. 功能规格

## 6.1. 核心操作系统

### 6.1.1. 背景与理由

**OSEK/VDX** 的操作系统[2]广泛用于汽车行业，并已在当代车辆中能被发现的所有类别的 **ECU** 中得到证明。被引入的 **OSEK OS** 的概念已广为人知，汽车行业在基于 **OSEK OS** 的系统工程方面拥有多年积攒的经验。

**OSEK OS** 是一个事件触发的操作系统（**event-triggered operating system**）。这为基于 **AUTOSAR** 的系统的设计和维护提供了高度的灵活性。事件触发为在运行时选择事件以驱动调度提供了自由，例如：角旋转、本地时间源、全局时间源、错误发生等。

由于这些原因，**AUTOSAR OS** 的核心功能需基于 **OSEK OS**。 特别是 **OSEK OS** 提供以下功能来支持 **AUTOSAR** 中的概念：

* 基于固定优先级的调度（**fixed priority-based scheduling**）
* 处理中断的设施（**facilities for handling interrupts**）
* 只有优先级高于任务的中断（**only interrupts with higher priority than Tasks**）
* 对不正确使用操作系统服务的一些保护（**some protection against incorrect use of OS services**）
* 通过 StartOS 和 StartupHook 的启动界面（**a startup interface through StartOS and the StartupHook**）
* 通过 ShutdownOS 和 ShutdownHook 的关机接口（**a shutdown interface through ShutdownOS and the ShutdownHook**）

除了这些之外，**OSEK OS**还提供了许多功能。可查阅规范[2]了解详细信息。

基于 **OSEK OS** 的 **AUTOSAR OS** 意味着遗留应用程序（**legacy applications**）可以向后兼容 - 即为 **OSEK OS** 编写的应用程序将可在 **AUTOSAR OS** 上运行。 但是**AUTOSAR OS** 引入的一些功能需求限制了使用现有的部分 **OSEK OS** 功能，并扩展现有的部分 **OSEK OS** 功能。

### 6.1.2. 需求

**AUTOSAR** 操作系统模块应提供与 **OSEK OS API** 向后兼容的 **API**。

#### 6.1.2.1. OSEK 操作系统的限制

由于 **OSEK OS** 效率太低，无法为警报回调函数（**alarm callback**）实现时序和内存保护。所以它们在一些特定的可伸缩性类中是不被允许使用的。

**AUTOSAR** 操作系统模块仅允许可扩展性等级1中的警报回调函数。

当系统中仅需要内部通信时，**OSEK OS** 需要根据 **OSEK COM** 规范提供处理Task任务间通信（即：内部通信）的功能。在 **AUTOSAR** 中，内部通信由 **AUTOSAR RTE** 或 **AUTOSAR COM** 提供，至少其中一个将存在于所有 **AUTOSAR ECU**。

当**AUTOSAR OS** 在用于 **AUTOSAR** 系统时，不需要支持内部通信。

如果定义了符号 **LOCALMESSAGESONLY**，则 **OSEK OS** 必须实现内部通信。**AUTOSAR OS** 即使在未定义 **LOCALMESSAGESONLY** 的环境中，确保内部通信始终存在，来弃用实现 **OSEK COM** 功能，并保持与 **OSEK** 规范的兼容性的需要。

**OSEK OS** 有一个称为 **RES_SCHEDULER** 的特殊资源。此资源有**2**个具体方面：

1. 即使未配置，它也始终存在于系统中。这意味着 **RES_SCHEDULER** 始终为操作系统所知。
2. 它始终具有最高的Task任务优先级。这意味着分配此资源的Task任务不能被其他任务抢占。

由于一些特殊情况总是难以处理。例如：在**RES_SCHEDULER**这种情况下与时序保护有关的情况。所以**AUTOSAR OS** 将 **RES_SCHEDULER** 处理为任何其他资源。这意味着不会自动创建 **RES_SCHEDULER**。

**注意：**

在多核系统上，调度发生在每个内核上。 第6.9.22 章包含有关在此类系统中处理资源的更多信息。

在 **OSEK OS** 中，用户必须用特定的宏（**Macro**）来声明操作系统对象。例如：DeclareTask()等。而 **AUTOSAR OS** 实现不应依赖于此类声明，并且需为了向后兼容提供没有功能的此类宏声明。

#### 6.1.2.2. OSEK OS 中的未定义行为

在许多情况下，**OSEK OS** 的行为是未定义的。这些情况表现了其移植性上的障碍。**AUTOSAR OS** 通过定义所需的行为来收紧 **OSEK OS** 此类规范。

1. 如果在对 **SetRelAlarm** 的调用中，参数**increment**设置为零，则服务应以标准和扩展状态返回 **E_OS_VALUE**。
2. 对 **StartOS**（用于启动操作系统）的第一次调用不应返回。
3. 如果调用 **ShutdownOS** 并且 **ShutdownHook** 返回，则操作系统模块需禁用所有中断并进入无限循环。

#### 6.1.2.3. OSEK OS 的扩展

操作系统模块应在调用 **StartOS** 之前和调用 **ShutdownOS** 之后提供 **DisableAllInterrupts**、**EnableAllInterrupts**、**SuspendAllInterrupts**、**ResumeAllInterrupts** 服务。

操作系统模块应提供增加软件计数器（**Software Counter**）的能力，作为警报到期（**alarm expiry**）的替代操作。操作系统模块需提供 **API** 服务 **IncrementCounter** 来增加软件计数器（**Software Counter**）。

操作系统模块需允许在操作系统启动期间自动启动预配置的绝对警报（**absolute alarm**）。绝对警报是对 **OSEK OS** 的扩展，OSEK OS只允许相关警报（**relative alarm**）。

操作系统 **API** 需在扩展模式下检查所有指针参数是否为 **NULL** 空指针，如果此类参数为 **NULL**，则以扩展状态返回 **E_OS_PARAM_POINTER**。

## 6.2. 软件自由运行定时器

因为计时器的数量通常非常有限，所以需添加了一些功能和配置以扩展定时器的重用。例如: 允许定时器测量。有关更多详细信息，另请参阅参考文档[7] (SWFRT)。

操作系统模块需处理由操作系统模块直接使用，并且不是由 **GPT** 驱动程序处理的所有定时器的初始化和配置。

操作系统模块需提供 **API** 服务 **GetCounterValue** 以读取计数器（**Counter**）的当前计数值。如果计数器（**Counter**）由硬件驱动，则返回硬件计时器滴答值（**tick**）；如果计数器（**Counter**）是用户驱动，则返回软件滴答值（**tick**）。

操作系统模块需提供 **API** 服务 **GetElapsedValue** 以获取当前滴答值和先前读取的滴答值之间的滴答的差值。

操作系统模块需调整硬件定时器驱动计数器的读出值，使最小值为零。并在连续读取时能够返回一个递增的计数值，直到计时器以其模数结束。

## 6.3. 调度表

### 6.3.1. 背景与理由

可以使用 **OSEK** 计数器（**Counter**）和一系列自动启动的警报（**Alarms**）来实现静态定义的任务（**Task**）激活机制。在简单的情况下，这可以通过指定一旦启动就不会被修改的警报（**Alarm**）来实现。运行时修改只有在警报之间的相对同步可以保证的情况下才能进行。这通常意味着只有在禁用相关的计数器（**Counter**）滴答中断的时候，才能修改警报。

调度表（**ScheduleTables**) 通过提供一组静态定义的到期点（**expiry points**）的封装来解决同步问题。每个到期点定义：

* 处理时必须发生的一个或多个动作，其中动作是任务（**Task**）的激活或事件（**event**）的设置。
* 从调度表（**ScheduleTable**）开始点一个以滴答为单位的偏移量。

每个调度表（**ScheduleTable**）都有一个以滴答为单位的持续时间。持续时间从零开始测量，并定义了调度表（**ScheduleTable**）的模数。

在运行时，操作系统模块将遍历调度表（**ScheduleTable**），依次处理每个到期点（**expiry points**）。迭代是被 **OSEK** 计数器（**Counter**）驱动。 因此计数器（**Counter**）的属性会影响可以在调度表（**ScheduleTable**）上配置的内容。

### 6.3.2. 需求

#### 6.3.2.1. 调度表的结构

![Figure7_1](Figure7_1.png)

一个调度表（**ScheduleTable**）至少有一个到期点（**expiry points**）。

一个到期点（**expiry points**）包含一组（可能为空）要激活的任务（**Task**）。

一个到期点（**expiry points**）需包含一组（可能为空）要设置的事件（**Event**）。

一个到期点需包含从调度表（**ScheduleTable**）开始的以滴答（**Ticks**）为单位偏移量。

#### 6.3.2.2. 到期点的限制

真实场景下，因为不存在空的到期点的用例，所以每个到期点都必须定义至少一个动作（**action**）。即：到期点需至少激活一个任务（**Task**）或设置至少一个事件（**Event**）。

因为操作系统需要知道处理到期点的顺序。所以有必要确保调度表（**ScheduleTable**）上的到期点可以完全排序。这是通过强制调度表（**ScheduleTable**）上的每个到期点必须具有唯一偏移量来保证的。给定调度表（**ScheduleTable**）上的每个到期点都需具有唯一的偏移量。

对调度表（**ScheduleTable**）上的到期点的迭代通过 **OSEK** 计数器来驱动。计数器（**Counter**）的特性（包括：**OsCounterMinCycle** 和 **OsCounterMaxAllowedValue**）对到期点偏移量施加约束。

初始的偏移量需为零或在底层计数器的**OsCounterMinCycle** 到 **OsCounterMaxAllowedValue**的范围之间。

类似地，此约束也适用于相邻到期点之间的延迟，以及到调度表（**ScheduleTable**）逻辑结束的延迟。相邻到期点之间的延迟也需底层计数器的**OsCounterMinCycle**到** OsCounterMaxAllowedValue**的范围之间。

#### 6.3.2.3. 处理调度表

操作系统模块需按照偏移量递增的顺序处理调度表（**ScheduleTable**）从初始到期点到最终到期点的每个到期点。

操作系统模块需允许同时处理多个调度表（**ScheduleTable**）。操作系统模块的一个调度表（**ScheduleTable**）应该由一个计数器（**Counter**）来驱动。操作系统模块需在任何给定时间，让每个计数器（**Counter**）能够处理至少一个调度表（**ScheduleTable**）。

操作系统模块需使用滴答（**Ticks**）来计时，以便计数器上的一个滴答值（**Ticks**）能够对应到调度表（**ScheduleTable**）上的一个滴答值（**Ticks**）。

可以在同一到期点（**expiry points**）上激活任务（**Task**）并为同一任务（**Task**）设置一个或多个唯一的事件（**Event**）。在到期点执行的任务（**Task**）激活的顺序和事件（**Event**）设置的顺序可能会导致不同的实现，并表现出不同的行为。例如：激活暂停的任务（**Task**），然后在此任务（**Task**）上事件的设置会执行成功。但如果顺序颠倒，则事件设置会失败。为了防止这种不确定性，有必要在到期点（**expiry points**）执行严格的操作顺序。

如果到期点（**expiry points**）包含激活任务（**Task**）的动作，以及为此任务设置一个或者多个事件，则操作系统模块需在相关事件设置之前先处理此任务的激活。无法对到期点（**expiry points**）的处理顺序做出进一步的假设。

调度表（**ScheduleTable**）始终具有定义的状态，下图说明了非同步调度表（**ScheduleTable**）的不同状态，以及它们之间的转换。

![Figure7_2](Figure7_2.png)

* 如果调度表（**ScheduleTable**）不活动，这意味着操作系统未处理，其状态为 **SCHEDULETABLE_STOPPED**。 
* 启动了调度表（**ScheduleTable**）后，进入 **SCHEDULETABLE_RUNNING** 状态，操作系统需处理到期点（**expiry points**）。 
* 如果切换调度表（**ScheduleTable**）的服务被调用，则调度表（**ScheduleTable**）进入 **SCHEDULETABLE_NEXT** 状态，并等待当前执行的调度表（**ScheduleTable**）执行结束。

#### 6.3.2.4. 重复调度表处理

在最终到期点被处理完之后，调度表（**ScheduleTable**）可能会也可能不会再被重复处理。

在这种情况下，允许两种类型的行为：

1. 单次（**single-shot**）：调度表（**ScheduleTable**）依次处理每个到期点，然后处理完最后一个到期点后停止。这对于触发分阶段的动作序列，以响应某些触发器的场景非常有用。
2. 重复（**repeating**）：调度表（**ScheduleTable**）依次处理每个到期点，处理完最后一个到期点后，循环回到最初的过期点。这对于构建执行重复处理的应用程序，或者需要处理同步驱动程序源的系统的场景非常有用。

重复的调度表（**ScheduleTable**）意味着每个到期点的重复周期，等同于调度表（**ScheduleTable**）的持续时间（**duration**）。

调度表（**ScheduleTable**）必须被配置成单次（**single-shot**）或者重复（**repeating**）的方式。

如果调度表（**ScheduleTable**）是单次的方式，则操作系统模块必须在处理完最后一个到期点后，停止处理调度表（**ScheduleTable**）最终延迟滴答计数（**Final Delay ticks**）。最终延迟滴答计数允许基于底层计数器，数值介于 **0 .. OsCounterMaxAllowedValue** 之间。

如果调度表（**ScheduleTable**）是重复的方式，最终延迟滴答计数的数值也和单次的方式类似，允许基于底层计数器，数值介于 **OsCounterMinCycle .. OsCounterMaxAllowedValue** 范围内。

在处理完最终的到期点之后，如果调度表（**ScheduleTable**）是重复，操作系统将在最终延迟（**Final Delay**）加上初始偏移（**Initial Offset**）滴答计数之后，处理下一个初始的到期点（**Initial Expiry Point**）。

#### 6.3.2.5. 控制 ScheduleTable 处理

应用程序负责开始和停止调度表（**ScheduleTable**）的处理。

操作系统模块提供 **StartScheduleTableAbs** 服务，以便于在底层计数器的绝对值开始（**Start**）点，开始处理调度表（**ScheduleTable**）。即：当底层计数器的值，等于 **Start + InitialOffset** 时，初始的到期点（**Initial Expiry Point**）必须被处理。

操作系统模块提供 **StartScheduleTableRel** 服务，以便于在底层计数器的相对于**Now**值的**Offset**处，开始处理调度表（**ScheduleTable**）。即：当底层计数器的值，等于 **Now + Offset + InitialOffset** 时，初始的到期点（**Initial Expiry Point**）必须被处理。

下图说明了由计数器（**Counter**）驱动的调度表（**ScheduleTable**）的两种不同方法。示例中的模数为 **65536**，即：**OsCounterMaxAllowedValue = 65535**。

![Figure7_3](Figure7_3.png)

操作系统模块提供 **StopScheduleTable**服务，以便于在调度表（**ScheduleTable**）运行的任何时候，立即取消对调度表（**ScheduleTable**）的处理。

如果调度表（**ScheduleTable**）处理在到达最终的到期点（**Final Expiry Point**）之前被取消，并随后重新启动。如果调用 **StartScheduleTableAbs** 或者 **StartScheduleTableRel** 服务，则调度表（**ScheduleTable**）将从开始点被重新启动。

操作系统模块提供 **NextScheduleTable**服务，处理从一个调度表（**ScheduleTable**）切换到另一个调度表（**ScheduleTable**）。

当请求调度表切换时，操作系统会继续处理当前调度表上的到期点。在最终的到期点（**Final Expiry Point**）之后，开始处理被切换到调度表（**ScheduleTable**）之前，将会有一个相当于 最终延迟（**Final Delay**）滴答计数的延迟。初始到期点（**Initial Expiry Point**）并将在初始偏移（**initial offset**）后被处理。

操作系统模块提供 **GetScheduleTableStatus** 服务，用来查询调度表（**ScheduleTable**）的状态。

调度表（**ScheduleTable**）可以被配置为在操作系统模块启动期间自动启动。如 **OSEK OS** 中的任务（**Task**）和警报（**Alarm**）一样。**OSEK OS** 定义了一个特定的顺序：在警报（**Alarm**）自动启动之前，执行任务（**Task**）的自动启动。**AUTOSAR OS** 使用调度表（**ScheduleTable**）扩展了这一点。

操作系统模块需在启动期间，完成任务（**Task**）和警报（**Alarm**）自动启动后，执行调度表（**ScheduleTable**）的自动启动。

## 6.4. 调度表同步

### 6.4.1. 背景与理由

处理调度表（**ScheduleTable**）上的初始到期点（**Initial Expiry Point**）的绝对时间是可以由用户控制。但是如果调度表（**ScheduleTable**）是重复的方式，则不能保证第一次处理初始到期点的绝对计数值与随后处理它的计数值相同。这是因为调度表（**ScheduleTable**）的持续时间不必等于计数器（**Counter**）模数。

在许多情况下，以底层计数器的特定绝对值处理 ScheduleTable 到期点可能很重要，这被称做为同步。

典型用例包括：

* 到期点需与用于电机管理的旋转角度同步。
* 将计算同步到全局（网络）时基（**Time base**）。请注意，在 **AUTOSAR** 中，操作系统并不提供全局（网络）时间源，原因如下：
  1. 很多情况下可能不需要全全局时间。
  2. 其他 **AUTOSAR** 模块，如 **FlexRay**，对操作系统来说是独立提供。
  3. 如果操作系统需要同步到多个全局（网络）时间源。例如：在两个时间触发网络（**time triggered networks**）之间建立网关（**Gateway**）时，操作系统不可能是唯一全局的时间源。

**AUTOSAR OS** 以两种方式提供对同步的支持：

* 隐式同步（**implicit synchronization**）：驱动调度表（**ScheduleTable**）的计数器（**Counter**），就是需要与之同步的计数器（**Counter**）。这种方式通常是如何实现与时间触发的网络技术（例如：**FlexRay**、**TTP**）的同步。底层硬件管理网络时间同步，并简单地将时间作为输出/比较计时器接口呈现给操作系统。下图7-4展示了具有隐式同步的调度表（**ScheduleTable**）的可能状态。
* 显式同步（**explicit synchronization**）：调度表（**ScheduleTable**）由操作系统计数器（**Operating System Counter**）驱动，该计数器不是需要同步的计数器。操作系统提供了额外的功能来保持由操作系统计数器驱动的调度表（**ScheduleTable**）处理与同步计数器（**Synchronization Counter**）之间的同步。这通常是与定期广播的全球时间同步的工作原理。下图7-5展示了显式同步的调度表（**ScheduleTable**）的状态。

![Figure7_4](Figure7_4.png)

![Figure7_5](Figure7_5.png)

### 6.4.2. 需求

操作系统模块需提供将调度表（**ScheduleTable**）的处理和已知的计数器（**Counter**）值同步的能力。

#### 6.4.2.1. 隐式同步

操作系统模块不需要为调度表（**ScheduleTable**）的隐式同步提供任何额外的支持。但是有必要限制调度表（**ScheduleTable**）的配置和运行时控制，以便配置的调度表（**ScheduleTable**）上的滴答值（**Tick**）可以与计数器（**Counter**）上的滴答值（**Tick**）对齐。 这要求调度表（**ScheduleTable**）的范围与计数器（**Counter**）的范围相同，即：调度表（**ScheduleTable**）和计数器（**Counter**）交互的要求，保证了每个滴答值（**Tick**）分辨率必须相等。

隐式同步的操作系统模块的调度表（**ScheduleTable**）应具有等于其关联 **OSEK OS** 计数器的 **OsCounterMaxAllowedValue + 1** 的持续时间。

为了同步调度表（**ScheduleTable**）的处理，它必须从一个已知的计数器值开始。这意味着需要隐式同步的调度表（**ScheduleTable**）只能以绝对计数器值启动，而不能以相对计数值启动。操作系统模块应防止隐式同步的调度表（**ScheduleTable**）以相对计数值启动。

当调度表（**ScheduleTable**）以绝对计数器值启动时，当计数器等于服务调用中指定的值加上到期点的偏移量时，将处理每个到期点。常见的用例是确保 调度表（**ScheduleTable**）配置中指定的偏移量对应于底层计数器的绝对值。这可以使用 **StartScheduleTableAbs(Tbl,0)** 轻松实现，如下所示。

![Figure7_6](Figure7_6.png)

#### 6.4.2.2. 显式同步

显式同步的调度表（**ScheduleTable**）需要操作系统模块的额外支持。调度表（**ScheduleTable**）正常情况下，由操作系统模块的计数器驱动，此类计数器被称为驱动计数器（**drive Counter**）。但处理过程需要与不属于操作系统模块的计数器对象的另一种计数器进行同步，此类进行同步的计数器被称为同步计数器（**synchronization Counter**）。

在调度表（**ScheduleTable**）、操作系统模块的计数器和同步计数器之间必须强制执行以下约束：

1. 约束1：显式同步的调度表（**ScheduleTable**）的持续时间不应大于驱动计数器（**drive Counter**）的模数。
2. 约束2：显式同步的调度表（**ScheduleTable**）的持续时间应等于同步计数器（**synchronization Counter**）的模数。
3. 约束3：同步计数器（**synchronization Counter**）应与调度表（**ScheduleTable**）相关联的驱动计数器**drive Counter**）具有相同的分辨率。 这意味着调度表（**ScheduleTable**）上的滴答与同步计数器（**synchronization Counter**）上的滴答具有相同的持续时间。

请注意，操作系统模块用户有责任验证其系统是否满足**约束2**和**约束3**。

显式同步的作用是让操作系统模块在同步计数器（**synchronization Counter**）的绝对值等于过期点的偏移量处继续处理每个到期点。这意味着显式同步始终假定调度表（**ScheduleTable**）的名义零必须与同步计数器（**synchronization Counter**）上的绝对值零同步。

为此用户必须告诉操作系统模块同步计数器的值。由于同步计数器（**synchronization Counter**）和调度表（**ScheduleTable**）的模数相同，操作系统模块可以使用这个信息来计算漂移。然后，操作系统模块会自动调整特殊配置的到期点之间的延迟，酌情延迟或提前，以确保保持同步。

##### 6.4.2.2.1. 启动

启动显式同步的调度表（**ScheduleTable**）有两个选项：

1. 异步启动（**Asynchronous start**）：以同步计数器（**synchronization Counter**）的任意值启动调度表（**ScheduleTable**）。

2. 同步启动（**Synchronous start**）：只有在提供了同步计数后，才能在同步计数器（**synchronization Counter**）的绝对值为零处启动 调度表（**ScheduleTable**）。 这可能意味着第一次同步的等待具有不确定性。

异步启动（**Asynchronous start**）由现有的绝对和相对调度表（**ScheduleTable**）启动服务提供。这两个服务都使用驱动计数器（**drive Counter**）而不是同步计数器（**synchronization Counter**）以设置初始到期点的处理的起始点。这允许 ScheduleTable调度表（**ScheduleTable**）在获知同步计数器（**synchronization Counter**）的值之前，就可以开始运行。

同步启动（**Synchronous start**）需要额外的服务，该服务仅在操作系统模块被告知同步计数器（**synchronization Counter**）的数值后，才能启动调度表（**ScheduleTable**）。

操作系统模块提供 **StartScheduleTableSynchron** 服务，来同步启动显式同步的调度表（**ScheduleTable**）。在驱动计数器（**drive Counter**）的 **(Duration - Value) + Initial Offset** 滴答时间过去后，初始到期点（**Initial Expiry Point**）才会被处理。其中 **Value** 是提供给调度表（**ScheduleTable**）的同步计数器（**synchronization Counter**）的绝对值。

如果显式同步的调度表（**ScheduleTable**）是同步启动的，则操作系统模块需要保证在 StartScheduleTableSynchron服务调用返回前，它处于等待（**waiting**）的状态。

##### 6.4.2.2.2. 提供同步计数

操作系统模块必须被告知同步计数器的值。由于调度表（**ScheduleTable**）持续时间等于同步计数器的模数（**modulus**），所以操作系统模块可以使用它来确定调度表时间上的当前计数值与同步计数之间的偏移，并决定是否需要采取所需的动作来实现同步。

操作系统模块需提供服务 *SyncScheduleTable*()（请参阅 **SWS_Os_00199**），来为调度表提供同步计数并启动同步。

##### 6.4.2.2.3. 指定同步界限

默认情况下，调度表不应在所有到期点（**expiry points**）进行调整。只有通过显式配置才允许进行调整。操作系统模块在可调到期点可以进行的调整范围通过指定以下内容来控制:

* **OsScheduleTableMaxShorten**：可以从到期偏移量中减去的最大值。
* **OsScheduleTableMaxLengthen**：可以添加到到期点偏移量的最大值。

下图说明了依赖于 **OsScheduleTableMaxShorten** 和 **OsScheduleTableMaxLengthen** 的行为：

![Figure7_7](Figure7_7.png)

到期点应允许配置 **OsScheduleTableMaxShorten**，该 **OsScheduleTableMaxShorten** 定义了可以从到期点偏移量中减去的最大滴答数（**ticks**）。

到期点应允许配置 **OsScheduleTableMaxLengthen**，该 **OsScheduleTableMaxLengthen** 定义可以添加到到期点偏移量的最大滴答数（**ticks**）。

在执行同步同时，必须根据其偏移量定义的总排序来处理计划表上的到期点。这意味着 **OsScheduleTableMaxShorten** 和 **OsScheduleTableMaxLengthen** 的允许值范围必须确保下一个到期点不会延迟到过去或提前到计划表的多个迭代（**iteration**）之后。

到期点的（偏移量 - **OsScheduleTableMaxShorten**）的值应大于该过期点的（偏移量 + **OsCounterMinCycle**）。

**OsScheduleTableMaxLengthen** 的值应小于调度表的持续时间。

到期点的（**OsScheduleTableMaxLengthen** + **delay_from_previous_EP**）的值应小于基础计数器的 **OsCounterMaxAllowedValue** 。

显式同步的调度表允许允许调度表值和同步计数器值之间的一些偏移。此容差可以为零，表示除非值相同，否则不会将计划表视为同步。

调度表需定义精度界限，其值范围为**0**到持续时间（duration）。

#### 6.4.2.3. 执行同步

操作系统模块使用同步计数，通过计算对下一个到期点的延迟的调整，在每个到期点支持（重新）同步计划表。这提供了比在最终到期点执行操作更快的计划表重新同步。

When a new synchronization count is provided, the Operating System module shall calculate the current deviation between the explicitly synchronized scheduled table and the synchronization count. ⌋ (SRS_Os_11002)

It is meaningless to try and synchronise an explicitly synchronized schedule table before a synchronization count is provided.

The Operating System module shall start to synchronise an explicitly synchronized schedule table after a synchronization count is provided AND shall continue to adjust expiry points until synchronized.

The Operating System module shall set the state of an explicitly synchronized schedule table to “running and synchronous” if the deviation is less than or equal to the configured OsScheduleTblExplicitPrecision threshold.

The Operating System module shall set the state of an explicitly synchronized schedule table to “running” if the deviation is greater than the configured OsScheduleTblExplicitPrecision threshold.

## 6.5. 堆栈监视设施

### 6.5.1. 背景与理由

在不提供任何内存保护硬件的处理器上，可能仍然需要提供利用可用资源尽力而为（**best effort with available resources**）的方案，提供可检测的内存故障类别。堆栈监视（**Stack monitoring**）将识别任务（**Task**）或 **ISR** 在上下文切换时超出指定堆栈使用的位置。这可能意味着在系统出错（**system being in error**）和检测到故障（**fault being detected**）之间，有相当长的时间。类似地，错误可能在通知故障时已被清除。如：发生上下文切换时堆栈可能小于指定大小的情况。

仅仅监视系统的整个堆栈空间通常是不够的，因为它不一定是正在执行的任务（**Task**）或者 **ISR** 使用的堆栈空间超过了所需的，它可能是被抢占的较低优先级的对象。

通过让操作系统正确识别任务（**Task**）或者**类别 2 ISR**的错误，可以节省大量调试时间。

请注意，对于使用 **MPU** 和可扩展性等级3（**scalability class 3**）或者扩展性等级4（**scalability class 4**）的系统，堆栈溢出可能会在堆栈监控能够检测到故障之前导致内存异常。

### 6.5.2. 需求

操作系统模块应提供堆栈监视，以检测任务（**Task**）和**类别 2 ISR**的可能堆栈故障。

如果堆栈监控检测到堆栈故障并且没有配置 **ProtectionHook**，操作系统模块会调用状态为 **E_OS_STACKFAULT** 的 **ShutdownOS** 服务。

如果堆栈监控检测到堆栈故障并且配置了**ProtectionHook**，则操作系统模块会调用状态为**E_OS_STACKFAULT** 的 **ProtectionHook**函数。

## 6.6. OS-Application

### 6.6.1. 背景与理由

AUTOSAR OS 必须能够支持构成一个内聚功能单元的操作系统对象，包括：任务（**Task**）、ISR、警报（**Alarm**)、调度表（**ScheduleTable**）、计数器（**Counter**）的集合。这个对象集合称为**OS-Application**。

操作系统模块负责调度共享处理器的**OS-Application**之间的可用处理资源。如果**OS-Application**被使用，所有的任务（**Task**）、ISR、警报（**Alarm**)、调度表（**ScheduleTable**）、计数器（**Counter**）必须属于一个**OS-Application**。属于同一个 **OS-Application** 的所有对象都可以相互访问。可以在配置期间授予从其他 **OS-Application** 访问对象的权限。如果可以为其设置事件（**Event**）的任务（**Task**）是可3访问的，则该事件（**Event**）也是可访问的。访问意味着这些操作系统对象被允许作为 **API** 服务的参数。

有两类 **OS-Application**：

1. 受信任的**OS-Applications**：受信任的**OS-Applications**可以在运行时禁用监控或保护功能的情况下运行。它们可以不受限制地访问内存、操作系统模块的 API，并且不需要在运行时强制执行它们的计时行为。当处理器支持时，它们可以在特权模式下运行。操作系统模块假定受信任的**OS-Applications**（和受信任的功能）不会导致与内存相关的保护故障。如果发生此类故障，系统稳定性可能会消失，关闭可能是唯一的选择。
2. 不受信任的**OS-Applications**：不受信任的**OS-Applications**不允许在运行时禁用监控或保护功能的情况下运行。它们对内存的访问受到限制，对操作系统模块的 API 的访问受到限制，并在运行时强制执行它们的计时行为。当处理器支持时，它们不允许在特权模式下运行。

**AUTOSAR OS**模块本身假设是受信任的。

**AUTOSAR OS**提供了一些服务，为调用者提供有关访问权限（**access rights**）和对象成员资格（**membership of objects**）的信息。这些服务旨在用于检查跨**OS-Application**间调用的访问权限以及参数。

**注意**：资源（**Resource**）对象不属于任何 **OS-Application** ，但对它们的访问权限必须被明确授予。同样的原理也适用于多核系统中的自旋锁。

正在运行的 **OS-Application** 定义为当前运行的任务（**Task**）或 **ISR** 所属的 **OS-Application**。以及在挂钩例程（hook routine）的情况下，导致挂钩例程调用的任务（**Task**）或 **ISR** 定义了正在运行的 **OS-Application**。

![Figure7_9](Figure7_9.png)

**OS-Application** 有一个状态，它定义了其他 **OS-Application** 对其操作系统对象的可访问性范围。每个 **OS-Application** 始终处于以下状态之一：

* **APPLICATION_ACCESSIBLE**：活动且可访问（**Active and accessible**）。操作系统对象可以从其他 **OS-Application** 访问。这是启动时的默认状态。
* **APPLICATION_RESTARTING**：在重启阶段（Restart phase）。操作系统对象无法被其他 **OS-Application** 访问。在**OS-Application**调用 **AllowAccess** 之前，状态是有效的。
* **APPLICATION_TERMINATED**：已终止且不可访问（**Terminated and not accessible**）。操作系统对象无法被其他 **OS-Application** 访问。状态不会改变。

下图显示了状态和可能的转换：

![Figure7_10](Figure7_10.png)

### 6.6.2. 需求

操作系统模块应支持 **OS-Application** ，这些**OS-Application**可以是受信任函数（**Trusted Function**）、任务（**Task**）、ISR、警报（**Alarm**）、调度表（**ScheduleTable**）、计数器（**Counter**）、挂钩（用于启动、错误和关闭）的可配置选择。

操作系统模块应支持受信任（**trusted**）和不受信任（**non-trusted**）**OS-Application**的概念。

受信任的**OS-Application**可以向其他（甚至不受信任的）**OS-Application**提供服务。此类服务就是受信任的服务（**trusted services**）。

操作系统模块提供服务 **GetApplicationID** 和 **GetCurrentApplicationID** 来确定当前正在执行的 **OS-Application**（需为每个**OS-Application**分配一个唯一的标识符）。

操作系统模块提供服务 **CheckObjectOwnership** 以确定给定任务（**Task**）、ISR、计数器、警报（**Alarm**)、调度表（**ScheduleTable**）属于哪个**OS-Application**。

操作系统模块提供服务 **CheckObjectAccess** 来确定允许哪些**OS-Application**在 **API** 调用中使用任务（**Task**）、ISR、计数器、警报（**Alarm**)、调度表（**ScheduleTable**）的 ID。

操作系统模块提供服务 **TerminateApplication** 来终止调用任务（**Task**）、类别2 ISR、应用程序特定错误挂钩所属的 **OS-Application**。这是 **TerminateTask** 服务的操作系统应用程序级别变体）

操作系统模块提供服务 **TerminateApplication** 来终止另一个 **OS-Application**，并且如果调用者不属于受信任的 **OS-Application**，则需忽略对该服务的调用。

如果操作系统模块需要终止一个 **OS-Application**，那么它应该：

* 终止此 **OS-Application** 的所有正在运行的（**running**）、就绪的（**ready**）和等待的（**waiting**）任务（**Task**）、ISR；
* 禁用此 **OS-Application** 的所有中断（**interrupts**）；
* 停止此 **OS-Application** 的所有活动的警报；
* 停止此 **OS-Application** 的所有调度表（**ScheduleTable**）。

操作系统模块应阻止受信任或不受信任的 **OS-Application** 访问不属于该 **OS-Application** 的对象，除非这些对象的访问权限由配置明确授予。

操作系统模块提供服务 **GetApplicationState** 来请求 **OS-Application** 的当前状态。

操作系统模块应在调用 **StartOS** 之后和调用任何 **StartupHook** 之前将所有 **OS-Applications** 的状态设置为 **APPLICATION_ACCESSIBLE**。

操作系统模块提供服务 **AllowAccess** 以将 **OS-Application** 的自身状态从 **APPLICATION_RESTARTING** 设置为 **APPLICATION_ACCESSIBLE**。

如果一个 **OS-Application** 被终止。例如：通过服务调用或通过保护挂钩（**protection hook**），并且没有请求重新启动，则操作系统模块应将此 **OS-Application** 的状态设置为 **APPLICATION_TERMINATED**。

如果一个 **OS-Application** 被终止。例如：通过服务调用或通过保护挂钩（**protection hook**），并且请求了重新启动，则操作系统模块应将此 **OS-Application** 的状态设置为 **APPLICATION_RESTARTING**。

操作系统模块应该拒绝其他 **OS-Application** 对不处于 **APPLICATION_ACCESSIBLE** 状态的 **OS-Application** 的操作系统对象（**Operating System objects**）的访问。

如果对一个操作系统对象的服务调用是由另一个 **OS-Application** 拥有的，同时 **OS-Application** 不处于 **APPLICATION_ACCESSIBLE** 状态，那么操作系统模块需返回 **E_OS_ACCESS**。例如：为了正在重新启动的 **OS-Application** 中的任务（**Task**）调用 **ActivateTask**。

## 6.7. 保护设施

保护仅适用于操作系统管理的对象。这意味着：

* 无法在类别1的ISR（**Category 1 ISR**）运行期间提供保护。因为操作系统不知道正在调用任何类别1的ISR（**Category 1 ISR**），所以如果需要任何保护，则必须避免使用类别1的ISR（**Category 1 ISR**）。如果 类别1的中断和 **OS-Application** 一起使用，则所有类别1的ISR（**Category 1 ISR**）必须属于受信任的 **OS-Application**。
* 无法为在从同一任务（**Task**）或者类别2的ISR（**Category 2 ISR**）的主体调用的函数之间提供保护。

### 6.7.1. 内存保护

#### 6.7.1.1. 背景与理由

内存保护只能在提供硬件支持内存保护的处理器上实现。

内存保护方案基于可执行程序的数据（**data**）、代码（**code**）和堆栈（**stack**）的部分。

**堆栈（Stack）**

一个 **OS-Application** 包含许多任务（**Task**）和 **ISR**。因为根据定义这些对象的堆栈只属于它的所有者对象，所以不需要在对象之间共享堆栈数据，即使这些对象属于同一个 **OS-Application**。

任务（**Task**）和 **ISR** 堆栈的内存保护非常有用，主要有两个原因：

1. 为任务（**Task**）或 **ISR** 提供比堆栈监控更直接的堆栈溢出和下溢检测。
2. 在 **OS-Application** 的组成部分之间提供保护，例如:满足一些安全约束。

**数据（Data）**

**OS-Applications** 可以有私有数据段，而任务（**Task**）或 **ISR** 也可以有私有数据段。**OS-Applications** 的私有数据部分由属于该 **OS-Applications** 的所有任务（**Task**）或 **ISR** 共享。

**代码（Code）**

代码部分要么是**OS-Application**私有的，要么可以在所有**OS-Application**之间共享（以使用共享库）。在不使用代码保护的情况下，执行不正确的代码最终会导致内存、时序或服务违规。

#### 6.7.1.2. 需求

**数据段和堆栈（Data Sections and Stack）**

操作系统模块应防止不受信任（**non-trusted**）的 **OS-Applications**，对其自己的数据部分和自己的堆栈进行写访问。

操作系统应提供限制受信任（**trusted**）的 **OS-Applications** 写入访问的可能性，就像对不受信任**OS-Applications**所做的那样。

这可以使用 **OsTrustedApplicationWithProtection** 进行配置。

**OS-Application的私有数据**

操作系统模块可能会阻止其他不受信任的**OS-Application**尝试对**OS-Application**的数据部分进行读取访问。

操作系统模块应允许**OS-Application**对该**OS-Application**自己的私有数据部分进行读写访问。

操作系统模块应防止其他不可信的**OS-Application**对**OS-Application**的私有数据部分进行写访问。

**任务/ISR 的私有堆栈**

操作系统模块应允许任务（**Task**）/ **类别2的ISR** 对该任务（**Task**）/ **类别2的ISR**自己的私有堆栈进行读写访问。

操作系统模块可能会阻止所有同一个**OS-Application**中的其他任务（**Task**）/ **ISR** 对非受信任**OS-Application**的任务（**Task**）/**类别2的ISR** 的私有堆栈进行写访问。

操作系统模块应防止从其他非受信任**OS-Application**对当前**OS-Application**的任务（**Task**）/**类别2的ISR** 的所有私有堆栈进行写访问。

**任务/ISR 的私有数据**

操作系统模块应允许（**Task**）/ **类别2的ISR**对该（**Task**）/ **类别2的ISR**自己的私有数据部分进行读写访问。

操作系统模块可能会阻止所有同一 个**OS-Application**中的其他（**Task**）/ **ISR** 对非受信任**OS-Application**的任务（**Task**）/**类别2的ISR** 的私有数据部分的写访问。

操作系统模块应防止从其他非受信任**OS-Application**对当前**OS-Application**的的任务（**Task**）/**类别2的ISR** 的所有私有数据部分进行写访问。

**代码段（Code Sections）**

操作系统模块可以为**OS-Application**提供保护其代码段不被非受信任的**OS-Application**执行的能力。

操作系统模块应提供在所有**OS-Application**可执行的共享库代码部分的能力。

**外围设备（Peripherals）**

如果 **OsTrustedApplicationWithProtection == FALSE**，则操作系统模块需允许受信任的**OS-Application**对外围设备进行读写访问。

操作系统模块应允许非受信任的 **OS-Application** 仅写入其分配的外围设备。（包括：具有写入内存位置的副作用的读取）。

**内存访问冲突（Memory Access Violation）**

如果检测到内存访问违规，操作系统模块需调用 **ProtectionHook**，并返回状态码 **E_OS_PROTECTION_MEMORY** 。

### 6.7.2. 时序保护（Timing Protection）

#### 6.7.2.1. 背景与理由

当一个任务（**Task**）或中断（**Interrupt**）在运行时错过了它的最后期限时，就会发生实时系统中的计时错误。

**AUTOSAR OS** 不提供时序保护的截止时间的监控（**deadline monitoring**）。因为监控截止时间并不能正确识别导致 **AUTOSAR** 系统中时序故障的那个任务（**Task**）或者**ISR**。当截止时间超时的时候，这可能是由于其他非监控的任务（**Task**）或者**ISR**的干扰或者阻塞时间过长，而最终引起了时序的错误。在这种情况下，错误在于这些非监控的不相关的任务（**Task**）或者**ISR**。接着它们通过系统的慢慢扩散，直到任务（**Task**）或者**ISR** 错过了截止时间。所以错过截止时间的任务（**Task**）或者**ISR** 不一定是在在运行时失败的那个任务（**Task**）或者 **ISR**。它只不过是被最早检测到时序的故障。

如果基于通过监控截止时间来识别的是否错过截止时间并采取行动，这可能会使用错误证据来终止了正确的 **OS-Application**，并同时不正确的**OS-Application**依旧被允许继续运行。

这个问题可以通过以下的例子来说明。考虑具有以下配置的系统：

![Table7_1](Table7_1.png)

| 任务Id | 优先级 | 执行时间 | 截止时间 (=任务周期） |
| ------ | ------ | -------- | --------------------- |
| A      | 高     | 1        | 5                     |
| B      | 中等   | 3        | 10                    |
| C      | 低     | 5        | 15                    |

假设所有任务（**Task**）在时间0都已经准备好运行，接着会执行以下调度，并且所有任务（**Task**）都将满足它们各自的截止时间。

![Figure7_11](Figure7_11.png)

现在考虑任务A（**Task A**）和任务B（**Task B**）行为不正确的情况。下图显示了任务A（**Task A**）和任务B（**Task B**）的执行时间都比指定的时间长，而任务B（**Task B**）的到达时间比指定的时间早 2 个滴答。任务A（**Task A**）和任务B（**Task B**）都按时完成。然而，任务C任务B（**Task C**）行为正确，但由于任务A（**Task A**）和任务B（**Task B**）的执行不正确，它未能在截止时间前完成。这是故障传播。即：系统中不相关部分的故障导致系统中正常运行的部分发生故障。

![Figure7_12](Figure7_12.png)

在 **AUTOSAR OS** 等固定优先级抢占式操作系统中，任务（**Task**）或者**ISR**是否满足其截止时间取决于以下因素：

* 系统中任务（**Task**）和**ISR**的执行时间。
* 任务（**Task**）和**ISR**因为较低优先级任务（**Task**）和**ISR**锁定共享资源或禁用中断，而遭受的阻塞时间。
* 系统中任务（**Task**）和**ISR**的到达间隔时间率（**interarrival rate**）。

为了安全和准确的时序保护，操作系统有必要在运行时控制这些因素，以确保任务（**Task**）和**ISR**能够满足它们各自的期限时间。

**AUTOSAR OS** 通过使用执行时间保护（**execution time protection**）来保证以下执行时间的静态配置上限（称为执行预算）来防止 (1) 中的计时错误：

* 任务（**Tasks**）。
* 类别2的ISR（**Category 2 ISRs**）。





