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
* 

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
* MCU上的特权和非特权模式（**Privileged and non-privileged modes on the MCU**）：保护操作系统免受由写入操作系统控制的寄存器引起的内部损坏。此模式不得允许操作系统应用程序绕过保护（例如：写入管理内存保护的寄存器、写入处理器状态字等）。特权模式必须在受保护操作系统的完全控制下，该操作系统在内部使用该模式并将控制权从不受信任的操作系统应用程序来回转移到受信任的操作系统应用程序。微处理器必须支持使处理器进入这种特权模式的受控方式。
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

## 6.2. 需求

**AUTOSAR** 操作系统模块应提供与 **OSEK OS API** 向后兼容的 **API**。

### 6.2.1. OSEK 操作系统的限制

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

### 6.2.2. OSEK OS 中的未定义行为

在许多情况下，**OSEK OS** 的行为是未定义的。这些情况表现了其移植性上的障碍。**AUTOSAR OS** 通过定义所需的行为来收紧 **OSEK OS** 此类规范。

1. 如果在对 **SetRelAlarm** 的调用中，参数**increment**设置为零，则服务应以标准和扩展状态返回 **E_OS_VALUE**。
2. 对 **StartOS**（用于启动操作系统）的第一次调用不应返回。
3. 如果调用 **ShutdownOS** 并且 **ShutdownHook** 返回，则操作系统模块需禁用所有中断并进入无限循环。

### OSEK OS 的扩展

操作系统模块应在调用 **StartOS** 之前和调用 **ShutdownOS** 之后提供 **DisableAllInterrupts**、**EnableAllInterrupts**、**SuspendAllInterrupts**、**ResumeAllInterrupts** 服务。

操作系统模块应提供增加软件计数器的能力，作为警报到期时的替代操作。 操作系统模块提供 API 服务 IncrementCounter 来增加软件计数器。

操作系统模块应允许在操作系统启动期间自动启动预配置的绝对警报。

是 OSEK OS 的扩展，它只允许相关警报。

操作系统 API 应在扩展模式下检查所有指针参数是否为 NULL 指针，如果此类参数为 NULL，则以扩展状态返回 E_OS_PARAM_POINTER。