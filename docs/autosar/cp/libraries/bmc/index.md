---
title: "Specification of Basic Software Multicore Library（基础软件多核库规范）"
spec: AUTOSAR_CP_SWS_BSWMulticoreLibrary
release: R23-11
---

## 1. 简介和功能概述

本规范描述了用于原子例程的 **AUTOSAR** 库的功能、**API** 和配置。

该库（**Bmc**）包含以下例程：

- 标志测试与置位（**flag test and set**）
- 标志清除（**flag clear**）
- 存储（**store**）
- 加载（**load**）
- 交换（**exchange**）
- 比较与交换（**compare and exchange**）
- 取数加（**fetch and add**）
- 取数减（**fetch and subtract**）
- 取数或（**fetch and or**）
- 取数异或（**fetch and xor**）
- 取数与（**fetch and and**）
- 线程栅栏（**thread fence**）

所有例程都是可重入的，可以同时被多个 runnable 使用。

## 2. 缩略语

下面的术语表包含了与 **Bmc** 模块相关、但未包含在 [\[1, AUTOSAR 术语表\]](#ref-1) 中的缩略语和缩写。

**Bmc**
> 基础软件多核库（**Basic Software Multicore Library**）。

**DET**
> 默认错误跟踪器（**Default Error Tracer**）。

**s16**
> **sint16** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**s32**
> **sint32** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**s64**
> **sint64** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**s8**
> **sint8** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**u16**
> **uint16** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**u32**
> **uint32** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**u64**
> **uint64** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**u8**
> **uint8** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

<a id="ref-1"></a>[1] Glossary
> AUTOSAR_FO_TR_Glossary

<a id="ref-2"></a>[2] General Specification of Basic Software Modules
> AUTOSAR_CP_SWS_BSWGeneral

<a id="ref-3"></a>[3] General Requirements on Basic Software Modules
> AUTOSAR_CP_SRS_BSWGeneral

<a id="ref-4"></a>[4] Requirements on Libraries
> AUTOSAR_CP_SRS_Libraries

### 3.2. 相关规范

**AUTOSAR** 提供了基础软件模块通用规范 [\[2\]](#ref-2)（**SWS BSW General**），该规范同样适用于 **BSWMulticoreLibrary**。

因此，**SWS BSW General** 规范应被视为 **BSWMulticoreLibrary** 的附加必需规范。

## 4. 约束和假设

### 4.1. 限制

无限制。

### 4.2. 汽车域的适用性

无限制。

## 5. 对其他模块的依赖

**Bmc** 模块应提供以下文件：

* **C** 文件，Bmc\_&lt;name&gt;.c，用于实现该库。所有 **C** 文件都应以「Bmc_」为前缀。

头文件 Bmc.h 提供 **Bmc** 库规范定义的所有公共函数原型和类型。

例程的实现与按 **C** 文件的分组建议按照下面描述的选项之一完成，且不强制遵循这些建议。

选项 1：&lt;Name&gt; 可以是函数名，即每个函数一个 **C** 文件，

例如：Bmc\_FlagClear.c 等。

选项 2：&lt;Name&gt; 可以是一组函数的通用名称：

* 2.1 按例程族分组：

例如：Bmc\_Flag.c、Bmc\_Fetch.c

* 2.2 按其他方法分组：（允许单独分组）

选项 3：&lt;Name&gt; 可以去掉，使得单个 **C** 文件包含所有 **Bmc** 函数，例如：Bmc.c。

使用上述选项可以灵活地选择合适的粒度并减少 **C** 文件的数量。在某些选项下，按需链接也是可能的。

## 6. 功能规格

### 6.1. 错误分类

《**General Specification of Basic Software Modules**》（基础软件模块通用规范）一文的「**Error Handling**」（错误处理）一节详细描述了基础软件的错误处理。其中最重要的是，它构成了一个由 **BSW** 模块中可能发生的五种错误类型组成的分类方案。

在此基础上，下文按相应的小节规定了具体的错误。

#### 6.1.1. 开发错误

不存在开发错误。

#### 6.1.2. 运行时错误

不存在运行时错误。

#### 6.1.3. 瞬态故障

不存在瞬态故障。

#### 6.1.4. 生产错误

不存在生产错误。

#### 6.1.5. 扩展生产错误

不存在扩展生产错误。

### 6.2. 初始化和关闭（**Initialization and Shutdown**）

**Bmc** 库不应需要初始化阶段。库函数可以在 **ECU** 初始化的第一步就被调用，例如甚至由 **OS** 或 **EcuM** 调用，因此该库应是就绪的。

**Bmc** 库不应需要关闭操作阶段。

### 6.3. 库 API 的使用（**Using Library API**）

**Bmc API** 可以从 **BSW** 模块或 **SWC** 直接调用。不需要端口定义。它是纯粹的函数调用。

库的使用应有文档记录。如果 **BSW** 模块或 **SWC** 使用了某个库，开发者应在 **BSW**/**SWC** 模板中添加一个 ImplementationDependencyOnArtifact。minVersion 和 maxVersion 参数对应于供应商版本。对于 **AUTOSAR** 库，这些参数可以留空，因为 **SWC** 或 **BSW** 模块可能依赖于库的行为，而不是依赖于某个供应商的实现。然而，**SWC** 或 **BSW** 模块应与其所集成的 **AUTOSAR** 平台兼容。

用户必须确保原子数据被分配在允许原子访问的内存中。因此，在内存分配关键字（**MAKW**）或相应的软件寻址方法（**SwAddrMethod**）中使用供应商特定且唯一的 {refinement} 关键字可能会很有用，该关键字可用于推导出相应的 MemoryAllocation 选项以进行映射。

### 6.4. 库的实现（**Library Implementation**）

**Bmc** 库的实现方式应使代码可以在不同内存分区中的调用者之间共享。

应避免使用宏。函数应声明为函数或内联函数。

库函数不得调用任何 **BSW** 模块函数，例如 **DET**。库函数可以调用其他库函数，因为库函数应是可重入的；而其他 **BSW** 模块函数则不一定可重入。

用 **C** 编程语言编写的库应符合 **MISRA C** 标准。更多详情请参见 SWS\_BSW\_00115。

每个 **AUTOSAR** 库模块实现 &lt;library&gt;*.c 和 &lt;library&gt;*.h 都应使用 **AUTOSAR** 内存映射机制将其代码映射到内存段。

每个 **AUTOSAR** 库模块实现 &lt;library&gt;*.c，凡使用了 **AUTOSAR** 整数数据类型和/或标准返回类型的，都应包含头文件 Std_Types.h。

所有 **AUTOSAR** 库模块都应使用 **AUTOSAR** 数据类型（整数、布尔）而不是原生 **C** 数据类型，除非该库被明确标识为仅与某个平台兼容。

所有 **AUTOSAR** 库模块都应避免直接使用编译器和平台特定的关键字，除非该库被明确标识为仅与某个平台兼容。

## 7. API规范

### 7.1. 导入的类型

在本章中，列出了从以下文件包含的所有类型。

| 模块 | 头文件 | 导入类型 |
|---|---|---|
| Std | Std_Types.h | Std_VersionInfoType |

### 7.2. 类型定义

**注意：** **Bmc** 原子类型很可能就是微控制器的原生数据类型（例如 32 位微控制器的 uint32/sint32）。

#### 7.2.1. Bmc_AtomicUType

类型，派生自 **uint**。范围为 - —— Bmc_AtomicUType 应始终映射到相应硬件平台能够实现原子操作的平台特定类型，以确保对该类型执行的所有操作都是无锁（**lock-free**）的。该类型应用于 **Bmc** 库函数使用的所有无符号数据项。可通过 **Bmc.h** 获得。

#### 7.2.2. Bmc_AtomicSType

类型，派生自 **sint**。范围为 - —— Bmc_AtomicSType 应始终映射到相应硬件平台能够实现原子操作的平台特定类型，以确保对该类型执行的所有操作都是无锁（**lock-free**）的。该类型应用于 **Bmc** 库函数使用的所有有符号数据项。可通过 **Bmc.h** 获得。

#### 7.2.3. Bmc_AtomicFlagType

类型，派生自 **boolean**。范围为 - —— Bmc_AtomicFlagType 应始终映射到相应硬件平台能够实现原子操作的平台特定类型，以确保对该类型执行的所有操作都是无锁（**lock-free**）的。该类型应用于 **Bmc** 库函数使用的所有标志（**Flag**）数据项。可通过 **Bmc.h** 获得。

### 7.3. 宏定义

**Bmc** 模块没有宏定义。

### 7.4. 函数定义（**Function definitions**）

**注意：** 所有原子操作都将提供顺序一致的排序（**sequentially consistent ordering**）（参见 <https://en.cppreference.com/w/c/atomic/memory_order#Sequentially-consistent_ordering>）。

#### 7.4.1. 标志例程（**Flag Routines**）

##### 7.4.1.1. Bmc_FlagTestAndSet

**说明**: 该函数原子地将 Object 所指向的值设置为 true。服务 ID 0x01。本服务为同步调用，可重入。参数（in）：无。参数 Object（inout）：-。参数（out）：无。返回值：boolean，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
boolean Bmc_FlagTestAndSet ( volatile Bmc_AtomicFlagType* Object )
```

函数 Bmc_FlagTestAndSet 原子地将 Object 所指向的值置为 **TRUE**。它返回操作之前的值，即如果该值已被置位则返回 **TRUE**，否则返回 **FALSE**。

##### 7.4.1.2. Bmc_FlagClear

**说明**: 该函数原子地将 Object 所指向的值设置为 false。服务 ID 0x02。本服务为同步调用，可重入。参数（in）：无。参数 Object（inout）：-。参数（out）：无。返回值：无。可通过 **Bmc.h** 获得。

```C
void Bmc_FlagClear ( volatile Bmc_AtomicFlagType* Object )
```

函数 Bmc_FlagClear 原子地将 Object 所指向的值置为 **FALSE**。

#### 7.4.2. 加载与存储例程（**Load and Store Routines**）

所有加载和存储例程都应隐式地使用 [Bmc_ThreadFence](#7441-bmc_threadfence) 所显式引入的机制。

##### 7.4.2.1. Bmc_Load

###### 7.4.2.1.1. Bmc_Load_u

**说明**: 该函数原子地加载 Object 所指向的值并将其返回。服务 ID 0x10 至 0x13。本服务为同步调用，可重入。参数（in）：无。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicUType](#721-bmc_atomicutype)，Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicUType Bmc_Load_u ( const volatile Bmc_AtomicUType* Object )
```

###### 7.4.2.1.2. Bmc_Load_s

**说明**: 该函数原子地加载 Object 所指向的值并将其返回。服务 ID 0x14 至 0x17。本服务为同步调用，可重入。参数（in）：无。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicSType](#722-bmc_atomicstype)，Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicSType Bmc_Load_s ( const volatile Bmc_AtomicSType* Object )
```

##### 7.4.2.2. Bmc_Store

###### 7.4.2.2.1. Bmc_Store_u

**说明**: 该函数原子地用 Desired 的值替换 Object 所指向的值。服务 ID 0x20 至 0x23。本服务为同步调用，可重入。参数 Desired（in）：要存储的值。参数 Object（inout）：-。参数（out）：无。返回值：无。可通过 **Bmc.h** 获得。

```C
void Bmc_Store_u ( volatile Bmc_AtomicUType* Object, Bmc_AtomicUType Desired )
```

###### 7.4.2.2.2. Bmc_Store_s

**说明**: 该函数原子地用 Desired 的值替换 Object 所指向的值。服务 ID 0x24 至 0x27。本服务为同步调用，可重入。参数 Desired（in）：要存储的值。参数 Object（inout）：-。参数（out）：无。返回值：无。可通过 **Bmc.h** 获得。

```C
void Bmc_Store_s ( volatile Bmc_AtomicSType* Object, Bmc_AtomicSType Desired )
```

##### 7.4.2.3. Bmc_Exchange

###### 7.4.2.3.1. Bmc_Exchange_u

**说明**: 该函数原子地用 Desired 的值替换 Object 所指向的值，并返回操作生效前 Object 所指向的值。服务 ID 0x30 至 0x33。本服务为同步调用，可重入。参数 Desired（in）：要存储的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicUType](#721-bmc_atomicutype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicUType Bmc_Exchange_u ( volatile Bmc_AtomicUType* Object, Bmc_AtomicUType Desired )
```

###### 7.4.2.3.2. Bmc_Exchange_s

**说明**: 该函数原子地用 Desired 的值替换 Object 所指向的值，并返回操作生效前 Object 所指向的值。服务 ID 0x34 至 0x37。本服务为同步调用，可重入。参数 Desired（in）：要存储的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicSType](#722-bmc_atomicstype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicSType Bmc_Exchange_s ( volatile Bmc_AtomicSType* Object, Bmc_AtomicSType Desired )
```

##### 7.4.2.4. Bmc_CompareExchange

###### 7.4.2.4.1. Bmc_CompareExchange_u

**说明**: 该函数原子地将 Object 所指向的值与 Expected 中的值进行相等比较，若相等，则用 Desired 替换 Object 所指向的值；若不相等，则用 Object 所指向的值更新 Expected 中的值。服务 ID 0x40 至 0x43。本服务为同步调用，可重入。参数 Desired（in）：要存储的值。参数 Object（inout）：-。参数 Expected（inout）：要存储的值。参数（out）：无。返回值：boolean，比较的结果。可通过 **Bmc.h** 获得。

```C
boolean Bmc_CompareExchange_u ( volatile Bmc_AtomicUType* Object, Bmc_AtomicUType* Expected, Bmc_AtomicUType Desired )
```

###### 7.4.2.4.2. Bmc_CompareExchange_s

**说明**: 该函数原子地将 Object 所指向的值与 Expected 中的值进行相等比较，若相等，则用 Desired 替换 Object 所指向的值；若不相等，则用 Object 所指向的值更新 Expected 中的值。服务 ID 0x44 至 0x47。本服务为同步调用，可重入。参数 Desired（in）：要存储的值。参数 Object（inout）：-。参数 Expected（inout）：要存储的值。参数（out）：无。返回值：boolean，比较的结果。可通过 **Bmc.h** 获得。

```C
boolean Bmc_CompareExchange_s ( volatile Bmc_AtomicSType* Object, Bmc_AtomicSType* Expected, Bmc_AtomicSType Desired )
```

#### 7.4.3. 提取例程（**Fetch Routines**）

所有提取例程都应隐式地使用 [Bmc_ThreadFence](#7441-bmc_threadfence) 所显式引入的机制。

##### 7.4.3.1. Bmc_FetchAdd

###### 7.4.3.1.1. Bmc_FetchAdd_u

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用加法所得的结果替换 Object 所指向的值。服务 ID 0x50 至 0x53。本服务为同步调用，可重入。参数 Operand（in）：操作的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicUType](#721-bmc_atomicutype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicUType Bmc_FetchAdd_u ( volatile Bmc_AtomicUType* Object, Bmc_AtomicUType Operand )
```

###### 7.4.3.1.2. Bmc_FetchAdd_s

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用加法所得的结果替换 Object 所指向的值。服务 ID 0x54 至 0x57。本服务为同步调用，可重入。参数 Operand（in）：操作的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicSType](#722-bmc_atomicstype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicSType Bmc_FetchAdd_s ( volatile Bmc_AtomicSType* Object, Bmc_AtomicSType Operand )
```

##### 7.4.3.2. Bmc_FetchSub

###### 7.4.3.2.1. Bmc_FetchSub_u

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用减法所得的结果替换 Object 所指向的值。服务 ID 0x60 至 0x63。本服务为同步调用，可重入。参数 Operand（in）：操作的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicUType](#721-bmc_atomicutype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicUType Bmc_FetchSub_u ( volatile Bmc_AtomicUType* Object, Bmc_AtomicUType Operand )
```

###### 7.4.3.2.2. Bmc_FetchSub_s

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用减法所得的结果替换 Object 所指向的值。服务 ID 0x64 至 0x67。本服务为同步调用，可重入。参数 Operand（in）：操作的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicSType](#722-bmc_atomicstype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicSType Bmc_FetchSub_s ( volatile Bmc_AtomicSType* Object, Bmc_AtomicSType Operand )
```

##### 7.4.3.3. Bmc_FetchOr

###### 7.4.3.3.1. Bmc_FetchOr_u

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用或运算所得的结果替换 Object 所指向的值。服务 ID 0x70 至 0x73。本服务为同步调用，可重入。参数 Operand（in）：操作的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicUType](#721-bmc_atomicutype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicUType Bmc_FetchOr_u ( volatile Bmc_AtomicUType* Object, Bmc_AtomicUType Operand )
```

###### 7.4.3.3.2. Bmc_FetchOr_s

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用或运算所得的结果替换 Object 所指向的值。服务 ID 0x74 至 0x77。本服务为同步调用，可重入。参数 Operand（in）：操作的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicSType](#722-bmc_atomicstype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicSType Bmc_FetchOr_s ( volatile Bmc_AtomicSType* Object, Bmc_AtomicSType Operand )
```

##### 7.4.3.4. Bmc_FetchXor

###### 7.4.3.4.1. Bmc_FetchXor_u

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用异或运算所得的结果替换 Object 所指向的值。服务 ID 0x80 至 0x83。本服务为同步调用，可重入。参数 Operand（in）：操作的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicUType](#721-bmc_atomicutype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicUType Bmc_FetchXor_u ( volatile Bmc_AtomicUType* Object, Bmc_AtomicUType Operand )
```

###### 7.4.3.4.2. Bmc_FetchXor_s

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用异或运算所得的结果替换 Object 所指向的值。服务 ID 0x84 至 0x87。本服务为同步调用，可重入。参数 Operand（in）：操作的值。参数 Object（inout）：-。参数（out）：无。返回值：[Bmc_AtomicSType](#722-bmc_atomicstype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicSType Bmc_FetchXor_s ( volatile Bmc_AtomicSType* Object, Bmc_AtomicSType Operand )
```

##### 7.4.3.5. Bmc_FetchAnd

###### 7.4.3.5.1. Bmc_FetchAnd_u

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用与运算所得的结果替换 Object 所指向的值。服务 ID 0x90 至 0x93。本服务为同步调用，可重入。参数（in）：无。参数 Object（inout）：-。参数 Operand（inout）：操作的值。参数（out）：无。返回值：[Bmc_AtomicUType](#721-bmc_atomicutype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicUType Bmc_FetchAnd_u ( volatile Bmc_AtomicUType* Object, Bmc_AtomicUType Operand )
```

###### 7.4.3.5.2. Bmc_FetchAnd_s

**说明**: 该函数原子地用对 Object 所指向的值与给定 Operand 应用与运算所得的结果替换 Object 所指向的值。服务 ID 0x94 至 0x97。本服务为同步调用，可重入。参数（in）：无。参数 Object（inout）：-。参数 Operand（inout）：操作的值。参数（out）：无。返回值：[Bmc_AtomicSType](#722-bmc_atomicstype)，操作生效前 Object 所指向的值。可通过 **Bmc.h** 获得。

```C
Bmc_AtomicSType Bmc_FetchAnd_s ( volatile Bmc_AtomicSType* Object, Bmc_AtomicSType Operand )
```

#### 7.4.4. 栅栏例程（**Fence Routines**）

##### 7.4.4.1. Bmc_ThreadFence

**说明**: 该函数创建一个顺序一致的获取（**acquire**）与释放（**release**）栅栏。获取与释放栅栏指令可防止程序序中位于其之前的任何读或写操作与位于其之后的任何读或写操作之间发生内存重排序。服务 ID 0x03。本服务为同步调用，可重入。参数（in）：无。参数（inout）：无。参数（out）：无。返回值：无。可通过 **Bmc.h** 获得。

```C
void Bmc_ThreadFence ( void )
```

函数 Bmc_ThreadFence 创建一个顺序一致的获取与释放栅栏。

**注意：** 它还可以用作编译器栅栏（**compiler barrier**），阻止编译器为了优化而以任何方向将指令移动跨越该栅栏。程序序中位于本指令之前的任何指令都不会被重排到本指令之后。位于本指令之后的每一条指令都不会被重排到本指令之前。

#### 7.4.5. 版本 API（**Version API**）

##### 7.4.5.1. Bmc_GetVersionInfo

**说明**: 该函数返回本库的版本信息。服务 ID 0xFF。本服务为同步调用，可重入。参数（in）：无。参数（inout）：无。参数 Versioninfo（out）：指向存储本模块版本信息的位置，格式遵循 [BSW00321] 的规定。返回值：无。可通过 **Bmc.h** 获得。

```C
void Bmc_GetVersionInfo ( Std_VersionInfoType* Versioninfo )
```

如果 Bmc_GetVersionInfo 的调用方与被调用方的源代码均可用，**Bmc** 库应将 Bmc_GetVersionInfo 实现为在模块头文件中定义的宏。

### 7.5. 回调通知

**Bmc** 模块没有回调通知。

### 7.6. 调度函数

**Bmc** 库没有调度函数。

### 7.7. 期望接口

在本章中，列出了本模块需要从其他模块获得的所有接口。

#### 7.7.1. 强制接口

无强制接口。

#### 7.7.2. 可选接口

无可选接口。

#### 7.7.3. 可配置接口

无可配置接口。

## 8. 配置规范

### 8.1. 发布信息（**Published Information**）

**Bmc** 模块应在头文件中发布基础软件模块通用要求 [\[3\]](#ref-3) 所要求的标准化公共发布参数，并需要在 **BSW** 模块描述中提供这些参数。相应的模块缩写可在基础软件模块列表中找到。

如适用，下面列出了其他模块特有的发布参数。

### 8.2. 配置选项（**Configuration Option**）

**Bmc** 库不应具有任何可能影响例程功能行为的配置选项。即对于给定的一组输入参数，输出应始终相同。例如，发生错误时返回的值不应是可配置的。

然而，允许库供应商添加与库实现相关的特定配置选项，例如用于资源消耗优化。

## B. AUTOSAR 可追溯项变更历史

请注意，本章中的列表还包含在后续版本中已从规范中删除的约束和规范项。这些约束和规范项在文档中不显示为超链接。

### B.1. 本文档按照 AUTOSAR 发行版 R22-11 的变更历史

#### B.1.1. R22-11 中新增的规范项

```
[SWS_BMC_00046] [SWS_BMC_00047] [SWS_Bmc_91016] [SWS_Bmc_91017] [SWS_Bmc_91018] [SWS_Bmc_91019] [SWS_Bmc_91020] [SWS_Bmc_91021] [SWS_Bmc_91022] [SWS_Bmc_91023] [SWS_Bmc_91024] [SWS_Bmc_91025] [SWS_Bmc_91026] [SWS_Bmc_91027] [SWS_Bmc_91028] [SWS_Bmc_91029] [SWS_Bmc_91030] [SWS_Bmc_91031] [SWS_Bmc_91032] [SWS_Bmc_91033] [SWS_Bmc_91034] [SWS_Bmc_91035] [SWS_Bmc_91036]
```

#### B.1.2. R22-11 中变更的规范项

```
[SWS_BMC_00013] [SWS_BMC_00014] [SWS_BMC_00016] [SWS_Bmc_91003] [SWS_Bmc_91004] [SWS_Bmc_91014] [SWS_Bmc_91015]
```

#### B.1.3. R22-11 中删除的规范项

```
[SWS_BMC_00017] [SWS_BMC_00023] [SWS_BMC_00025] [SWS_BMC_00027] [SWS_BMC_00029] [SWS_BMC_00031] [SWS_BMC_00033] [SWS_BMC_00035] [SWS_BMC_00037] [SWS_BMC_00039] [SWS_Bmc_91005] [SWS_Bmc_91006] [SWS_Bmc_91007] [SWS_Bmc_91008] [SWS_Bmc_91009] [SWS_Bmc_91010] [SWS_Bmc_91011] [SWS_Bmc_91012] [SWS_Bmc_91013]
```

### B.2. 本文档按照 AUTOSAR 发行版 R23-11 的变更历史

#### B.2.1. R23-11 中新增的规范项

```
[SWS_Bmc_91000] [SWS_Bmc_91001] [SWS_Bmc_91002]
```

#### B.2.2. R23-11 中变更的规范项

```
[SWS_Bmc_91025] [SWS_Bmc_91026]
```

#### B.2.3. R23-11 中删除的规范项

无
