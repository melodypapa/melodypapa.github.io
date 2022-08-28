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
> Hardware

**ID** 
> Identifier

**IOC** 
> Inter OS-Application communicator

**ISR** 
> Interrupt Service Routine

**LE** 
> A locatable entity is a distinct piece of software that has the same effect regardless of which core it is located.

**MC** 
> Multi-Core

**MCU** 
> Microcontroller Unit

**ME** 
> Mutual exclusion

**MPU** 
> Memory Protection Unit

**NMI** 
> Non maskable interrupt

**OIL** 
> OSEK Implementation Language

**OS** 
> Operating System

**OSEK/VDX** 
> Offene Systeme und deren Schnittstellen für die Elektronik im Kraftfahrzeug

**RTE** 
> Run-Time Environment

**RTOS** 
> Real Time Operating System

**SC** 
> Single-Core

**SLA** 
> Software Layered Architecture

**SW** 
> Software

**SWC** 
> Software Component

**SWFRT** 
> Software FreeRunningTimer

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

