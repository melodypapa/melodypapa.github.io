---
title: "Specification of Fixed Point Math Routines（定点数学例程规范）"
spec: AUTOSAR_CP_SWS_MFXLibrary
release: R23-11
---

## 1. 简介和功能概述

本规范规定了专用于定点值算术例程的 **AUTOSAR** 库的功能、**API** 和配置。

该数学库（**MFX**）包含以下例程：

- 加法（**addition**）
- 减法（**subtraction**）
- 绝对值（**absolute value**）
- 差值的绝对值（**absolute value of differences**）
- 乘法（**multiplication**）
- 除法（**division**）
- 乘法与除法的组合（**combination of multiplication and division**）
- 乘法与右移的组合（**combination of multiplication and shift right**）
- 除法与左移的组合（**combination of division and shift left**）
- 取模（**modulo**）
- 限幅（**limitation**）

其中一些函数同样为 2<sup>n</sup> 缩放整数（**2n Scaled Integers**）而提供：

- 加法（**addition**）
- 减法（**subtraction**）
- 绝对值（**absolute value**）
- 差值的绝对值（**absolute value of differences**）
- 乘法（**multiplication**）
- 除法（**division**）
- 转换（**conversion**，2<sup>n</sup> 缩放整数特有）

所有例程都是可重入的，可以同时被多个 runnable 使用。

## 2. 缩略语

下面的术语表包含了与 **MFXLibrary** 模块相关、但未包含在 [\[1, AUTOSAR 术语表\]](#ref-1) 中的缩略语和缩写。

**Abs**
> 绝对值（**Absolute value**）。

**AbsDiff**
> 差值的绝对值（**Absolute value of a difference**）。

**Add**
> 加法（**Addition**）。

**AR**
> AUTOSAR（**Autosar**）。

**BSW**
> 基础软件（**Basic Software**）。

**DET**
> 默认错误跟踪器（**Default Error Tracer**）。

**Div**
> 除法（**Division**）。

**DivShLeft**
> 除法与左移的组合（**Combination of division and shift left**）。

**ECU**
> 电子控制单元（**Electronic Control Unit**）。

**Limit**
> 限幅例程（**Limitation routine**）。

**Max**
> 最大值（**Maximum**）。

**MFX/Mfx**
> 定点数学库（**Math - Fixed Point library**）。

**Min**
> 最小值（**Minimum**）。

**Minmax**
> 仅以一个值同时限定最小值和最大值（**Limitation with only one value for min and max**）。

**Mod**
> 取模例程（**Modulo routine**）。

**Mul**
> 乘法（**Multiplication**）。

**MulDiv**
> 乘法与除法的组合（**Combination of multiplication and division**）。

**MulShRight**
> 乘法与右移的组合（**Combination of multiplication and shift right**）。

**s16**
> **sint16** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**s32**
> **sint32** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**s8**
> **sint8** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**Sub**
> 减法（**Subtraction**）。

**SWS**
> 软件规范（**Software Specification**）。

**u16**
> **uint16** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**u32**
> **uint32** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

**u8**
> **uint8** 的助记符，规定于 AUTOSAR_SWS_PlatformTypes。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

<a id="ref-1"></a>[1] Glossary
> AUTOSAR_FO_TR_Glossary

<a id="ref-2"></a>[2] ISO/IEC 9899:1990 Programming Language - C
> https://www.iso.org

<a id="ref-3"></a>[3] General Specification of Basic Software Modules
> AUTOSAR_CP_SWS_BSWGeneral

<a id="ref-4"></a>[4] General Requirements on Basic Software Modules
> AUTOSAR_CP_SRS_BSWGeneral

<a id="ref-5"></a>[5] Requirements on Libraries
> AUTOSAR_CP_SRS_Libraries

### 3.2. 相关规范

**AUTOSAR** 提供了基础软件模块通用规范 [\[3, SWS BSW General\]](#ref-3)，该规范同样适用于 **MFXLibrary**。

因此，**SWS BSW General** 规范应被视为 **MFXLibrary** 的附加必需规范。

## 4. 约束和假设

### 4.1. 限制

- 对服务库没有要求：服务库可以以多种方式实现。许多小例程可以合并到一个实现文件中。对于较大的例程，一个文件应包含一个例程的实现。通常，从链接器优化的角度来看，建议每个目标文件一个例程。对于位处理例程，更多例程可以共同构成一个目标文件。这种分组未在 Release 4.0, Rev001 中实现，将在 Release 4.0, rev002 中解决。

### 4.2. 汽车域的适用性

无限制。

## 5. 对其他模块的依赖

### 5.1. 文件结构

**MFX** 模块应提供以下文件：

* **C** 文件，Mfx\_&lt;name&gt;.c，用于实现该库。所有 **C** 文件都应以「Mfx」为前缀。

例程的实现与按 **C** 文件的分组建议按照下面描述的选项之一完成，且不强制遵循这些建议。

选项 1：&lt;Name&gt; 可以是函数名，即每个函数一个 **C** 文件，

例如：Mfx\_Add\_u8u8\_u8.c 等。

选项 2：&lt;Name&gt; 可以是一组函数的通用名称：

* 2.1 按对象族分组：

例如：Mfx\_NomMath.c、Mfx\_ScaledMath.c

* 2.2 按例程族分组：

例如：Mfx\_Add.c

* 2.3 按方法族分组：如果合理的话

* 2.4 按体系结构分组：

例如：Mfx\_Add8.c

* 2.5 按其他方法分组：（允许单独分组）

选项 3：&lt;Name&gt; 可以去掉，使得单个 **C** 文件包含所有 **MFX** 函数，例如：Mfx.c。

使用上述选项可以灵活地选择合适的粒度并减少 **C** 文件的数量。在某些选项下，按需链接也是可能的。

## 6. 功能规格

### 6.1. 错误分类（**Error classification**）

《**General Specification of Basic Software Modules**》（基础软件模块通用规范）一文的第 7.1 节「**Error Handling**」（错误处理）详细描述了基础软件的错误处理。其中最重要的是，它构成了一个由 **BSW** 模块中可能发生的五种错误类型组成的分类方案。

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

### 6.2. 初始化和关闭（**Initialization and shutdown**）

**MFX** 库不应需要初始化阶段。库函数可以在 **ECU** 初始化的第一步就被调用，例如甚至由 **OS** 或 **EcuM** 调用，因此该库应是就绪的。

**MFX** 库不应需要关闭操作阶段。

### 6.3. 库 API 的使用（**Using Library API**）

**MFX API** 可以从 **BSW** 模块或 **SWC** 直接调用。不需要端口定义。它是纯粹的函数调用。

库的使用应有文档记录。如果 **BSW** 模块或 **SWC** 使用了某个库，开发者应在 **BSW**/**SWC** 模板中添加一个 Implementation-DependencyOnArtifact。

minVersion 和 maxVersion 参数对应于供应商版本。对于 **AUTOSAR** 库，这些参数可以留空，因为 **SWC** 或 **BSW** 模块可能依赖于库的行为，而不是依赖于某个供应商的实现。然而，**SWC** 或 **BSW** 模块应与其所集成的 **AUTOSAR** 平台兼容。

### 6.4. 库的实现（**Library implementation**）

**MFX** 库的实现方式应使代码可以在不同内存分区中的调用者之间共享。

应避免使用宏。函数应声明为函数或内联函数。不应使用宏 #define。

库函数不得调用任何 **BSW** 模块函数，例如 **DET**。库函数可以调用其他库函数。因为库函数应是可重入的，而其他 **BSW** 模块函数则不一定可重入。

用 **C** 编程语言编写的库应符合 **MISRA C** 标准。

更多详情请参见 SWS\_BSW\_00115。

每个 **AUTOSAR** 库模块实现 &lt;library&gt;*.c 和 &lt;library&gt;*.h 都应使用 **AUTOSAR** 内存映射机制将其代码映射到内存段。

每个 **AUTOSAR** 库模块实现 &lt;library&gt;*.c，凡使用了 **AUTOSAR** 整数数据类型和/或标准返回类型的，都应包含头文件 Std_Types.h。

所有 **AUTOSAR** 库模块都应使用 **AUTOSAR** 数据类型（整数、布尔）而不是原生 **C** 数据类型，除非该库被明确标识为仅与某个平台兼容。

所有 **AUTOSAR** 库模块都应避免直接使用编译器和平台特定的关键字，除非该库被明确标识为仅与某个平台兼容。

在实现 Mfx 服务时必须遵守整数提升（**integral promotion**）规则。因此，为了获得最大精度，中间结果不应被限制。

## 7. API规范

### 7.1. 导入的类型

在本章中，列出了从以下模块包含的所有类型：

| 模块 | 导入类型 |
|---|---|
| Std_Types.h | sint8、uint8、sint16、uint16、sint32、uint32 |

可以观察到，由于 **C** 语言提供的整数类型的大小是由实现定义的，因此每种整数类型可表示的值的范围在不同的实现之间会有所不同。

因此，为了提高软件的可移植性，这些类型定义在 Platform\_Types.h [6] 中。库例程名称中使用了以下助记符。

表8.1：基本类型（**Base Types**）

| 大小 | 平台类型 | 助记符 |
|---|---|---|
| 有符号 8 位 | sint8 | s8 |
| 有符号 16 位 | sint16 | s16 |
| 有符号 32 位 | sint32 | s32 |
| 无符号 8 位 | uint8 | u8 |
| 无符号 16 位 | uint16 | u16 |
| 无符号 32 位 | uint32 | u32 |

如 [6] 中所述，各基本类型的取值范围见表 8.2。

表8.2：基本类型的取值范围（**Ranges for Base Types**）

| 基本类型 | 取值范围 |
|---|---|
| uint8 | [ 0, 255 ] |
| sint8 | [ -128, 127 ] |
| uint16 | [ 0, 65535 ] |
| sint16 | [ -32768, 32767 ] |
| uint32 | [ 0, 4294967295 ] |
| sint32 | [ -2147483648, 2147483647 ] |

作为文档其余部分的约定：

* 助记符将用于例程的名称中（&lt;InTypeMn1&gt; 表示输入 1 的类型助记符）；
* 真实类型将用于例程原型的描述中（使用 &lt;InType1&gt; 或 &lt;OutType&gt;）。

### 7.2. 类型定义

**Mfx** 模块没有类型定义。

### 7.3. 关于舍入的说明（**Comment about rounding**）

可应用两种舍入类型：

结果被「四舍五入」（**rounded off**），即：

- 0 &lt;= X &lt; 0.5 舍入为 0
- 0.5 &lt;= X &lt; 1 舍入为 1
- -0.5 &lt; X &lt;= 0 舍入为 0
- -1 &lt; X &lt;= -0.5 舍入为 -1

结果向零舍入：

- 0 &lt;= X &lt; 1 舍入为 0
- -1 &lt; X &lt;= 0 舍入为 0

### 7.4. 关于例程优化的说明（**Comment about routines optimization**）

#### 7.4.1. 使用常量进行优化（**Optimized with constants**）

出于优化的目的，在某些例程中，函数的某个参数「必须是常量」是强制性的。

要求是该表达式必须在编译时完全求值。它可以是常量字面量、宏或可在编译时计算的算术表达式。它不得包含变量或函数调用。

例如，小数点位置的参数是常量表达式，因此可以在编译的预处理阶段之后被消除。当正确地实现为内联函数或宏时，所需移位次数的计算在编译时完成，而不是在运行时完成。当不使用常量表达式时，会产生 **ROM**/吞吐量方面的代价。

### 7.5. 数学例程定义（**Mathematical routines definitions**）

#### 7.5.1. 加法（**Additions**）

##### 7.5.1.1. Mfx_Add_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 本例程对两个参数进行加法运算。服务 ID 0x001 至 0x024。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_Add_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value )
```

本例程对两个参数进行加法运算：

```C
Return-value = x_value + y_value
```

发生负上溢或正上溢时，返回值应饱和到边界值。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x001 | uint8 Mfx_Add_u8u8_u8( uint8 , uint8); |
| 0x002 | uint8 Mfx_Add_u8s8_u8( uint8 , sint8); |
| 0x003 | sint8 Mfx_Add_u8s8_s8( uint8 , sint8); |
| 0x004 | uint8 Mfx_Add_s8s8_u8( sint8 , sint8); |
| 0x005 | sint8 Mfx_Add_s8s8_s8( sint8 , sint8); |
| 0x006 | uint16 Mfx_Add_u16u16_u16( uint16 , uint16); |
| 0x007 | uint16 Mfx_Add_u16s16_u16( uint16 , sint16); |
| 0x008 | sint16 Mfx_Add_u16s16_s16( uint16 , sint16); |
| 0x009 | uint8 Mfx_Add_s16s16_u8( sint16 , sint16); |
| 0x00A | sint8 Mfx_Add_s16s16_s8( sint16 , sint16); |
| 0x00B | uint16 Mfx_Add_s16s16_u16( sint16 , sint16); |
| 0x00C | sint16 Mfx_Add_s16s16_s16( sint16 , sint16); |
| 0x00D | sint8 Mfx_Add_u32u32_s8( uint32 , uint32); |
| 0x00E | sint16 Mfx_Add_u32u32_s16( uint32 , uint32); |
| 0x00F | uint32 Mfx_Add_u32u32_u32( uint32 , uint32); |
| 0x010 | sint32 Mfx_Add_u32u32_s32( uint32 , uint32); |
| 0x011 | uint32 Mfx_Add_u32s32_u32( uint32 , sint32); |
| 0x012 | sint32 Mfx_Add_u32s32_s32( uint32 , sint32); |
| 0x013 | uint32 Mfx_Add_s32s32_u32( sint32 , sint32); |
| 0x014 | sint32 Mfx_Add_s32s32_s32( sint32 , sint32); |
| 0x015 | uint8 Mfx_Add_s32s32_u8( sint32 , sint32); |
| 0x016 | sint8 Mfx_Add_s32s32_s8( sint32 , sint32); |
| 0x017 | uint16 Mfx_Add_s32s32_u16( sint32 , sint32); |
| 0x018 | sint16 Mfx_Add_s32s32_s16( sint32 , sint32); |
| 0x019 | sint16 Mfx_Add_u32s32_s16( uint32 , sint32); |
| 0x01A | sint8 Mfx_Add_u32s32_s8( uint32 , sint32); |
| 0x01B | uint16 Mfx_Add_u32s32_u16( uint32 , sint32); |
| 0x01C | uint8 Mfx_Add_u32s32_u8( uint32 , sint32); |
| 0x01D | uint16 Mfx_Add_u32u32_u16( uint32 , uint32); |
| 0x01E | uint8 Mfx_Add_u32u32_u8( uint32 , uint32); |
| 0x01F | sint16 Mfx_Add_u16u16_s16( uint16 , uint16); |
| 0x020 | uint8 Mfx_Add_u16u16_u8( uint16 , uint16); |
| 0x021 | uint8 Mfx_Add_u16s16_u8( uint16 , sint16); |
| 0x022 | sint8 Mfx_Add_u16u16_s8( uint16 , uint16); |
| 0x023 | sint8 Mfx_Add_u16s16_s8( uint16 , sint16); |
| 0x024 | sint8 Mfx_Add_u8u8_s8( uint8 , uint8); |

#### 7.5.2. 减法（**Subtractions**）

##### 7.5.2.1. Mfx_Sub_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 本例程对两个参数进行减法运算。服务 ID 0x025 至 0x054。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_Sub_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value )
```

本例程对两个参数进行减法运算：

```C
Return-value = x_value - y_value
```

发生负上溢或正上溢时，返回值应饱和到边界值。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x025 | uint8 Mfx_Sub_u8u8_u8( uint8 , uint8); |
| 0x026 | sint8 Mfx_Sub_u8u8_s8( uint8 , uint8); |
| 0x027 | uint8 Mfx_Sub_u8s8_u8( uint8 , sint8); |
| 0x028 | sint8 Mfx_Sub_s8u8_s8( sint8 , uint8); |
| 0x029 | sint8 Mfx_Sub_s8s8_s8( sint8 , sint8); |
| 0x02A | uint8 Mfx_Sub_u16u16_u8( uint16 , uint16); |
| 0x02B | sint8 Mfx_Sub_u16u16_s8( uint16 , uint16); |
| 0x02C | uint8 Mfx_Sub_s16s16_u8( sint16 , sint16); |
| 0x02D | sint8 Mfx_Sub_s16s16_s8( sint16 , sint16); |
| 0x02E | uint8 Mfx_Sub_s32s32_u8( sint32 , sint32); |
| 0x02F | sint8 Mfx_Sub_s32s32_s8( sint32 , sint32); |
| 0x030 | uint16 Mfx_Sub_u16u16_u16( uint16 , uint16); |
| 0x031 | uint16 Mfx_Sub_u16s16_u16( uint16 , sint16); |
| 0x032 | sint16 Mfx_Sub_s16u16_s16( sint16 , uint16); |
| 0x033 | sint16 Mfx_Sub_u16s16_s16( uint16 , sint16); |
| 0x034 | uint16 Mfx_Sub_s16s16_u16( sint16 , sint16); |
| 0x035 | sint16 Mfx_Sub_u16u16_s16( uint16 , uint16); |
| 0x036 | sint16 Mfx_Sub_s16s16_s16( sint16 , sint16); |
| 0x037 | uint8 Mfx_Sub_s32u32_u8( sint32 , uint32); |
| 0x038 | sint8 Mfx_Sub_u32s32_s8( uint32 , sint32); |
| 0x039 | uint16 Mfx_Sub_s32u32_u16( sint32 , uint32); |
| 0x03A | uint16 Mfx_Sub_u32u32_u16( uint32 , uint32); |
| 0x03B | sint16 Mfx_Sub_u32u32_s16( uint32 , uint32); |
| 0x03C | uint16 Mfx_Sub_s32s32_u16( sint32 , sint32); |
| 0x03D | sint16 Mfx_Sub_s32s32_s16( sint32 , sint32); |
| 0x03E | uint32 Mfx_Sub_u32u32_u32( uint32 , uint32); |
| 0x03F | uint32 Mfx_Sub_u32s32_u32( uint32 , sint32); |
| 0x040 | uint32 Mfx_Sub_s32u32_u32( sint32 , uint32); |
| 0x041 | sint32 Mfx_Sub_u32u32_s32( uint32 , uint32); |
| 0x042 | sint32 Mfx_Sub_s32u32_s32( sint32 , uint32); |
| 0x043 | sint32 Mfx_Sub_u32s32_s32( uint32 , sint32); |
| 0x044 | uint32 Mfx_Sub_s32s32_u32( sint32 , sint32); |
| 0x045 | sint32 Mfx_Sub_s32s32_s32( sint32 , sint32); |
| 0x046 | sint16 Mfx_Sub_s32u32_s16( sint32 , uint32); |
| 0x047 | sint8 Mfx_Sub_s32u32_s8( sint32 , uint32); |
| 0x048 | sint16 Mfx_Sub_u32s32_s16( uint32 , sint32); |
| 0x049 | uint16 Mfx_Sub_u32s32_u16( uint32 , sint32); |
| 0x04A | uint8 Mfx_Sub_u32s32_u8( uint32 , sint32); |
| 0x04B | sint8 Mfx_Sub_u32u32_s8( uint32 , uint32); |
| 0x04C | uint8 Mfx_Sub_u32u32_u8( uint32 , uint32); |
| 0x04D | uint16 Mfx_Sub_s16u16_u16( sint16 , uint16); |
| 0x04E | uint8 Mfx_Sub_u16s16_u8( uint16 , sint16); |
| 0x04F | uint8 Mfx_Sub_s16u16_u8( sint16 , uint16); |
| 0x050 | sint8 Mfx_Sub_u16s16_s8( uint16 , sint16); |
| 0x051 | sint8 Mfx_Sub_s16u16_s8( sint16 , uint16); |
| 0x052 | uint8 Mfx_Sub_s8u8_u8( sint8 , uint8); |
| 0x053 | uint8 Mfx_Sub_s8s8_u8( sint8 , sint8); |
| 0x054 | sint8 Mfx_Sub_u8s8_s8( uint8 , sint8); |

#### 7.5.3. 绝对值（**Absolute value**）

##### 7.5.3.1. Mfx_Abs_&lt;InTypeMn1&gt;_&lt;OutTypeMn&gt;

**说明**: 本例程计算一个有符号值的绝对值。服务 ID 0x055 至 0x05E。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_Abs_<InTypeMn1>_<OutTypeMn> ( <InType1> x_value )
```

本例程计算一个有符号值的绝对值：

```C
Return-value = | x_value |
```

发生负上溢或正上溢时，返回值应饱和到边界值。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x055 | uint8 Mfx_Abs_s8_u8( sint8 ); |
| 0x056 | sint8 Mfx_Abs_s8_s8( sint8 ); |
| 0x057 | uint8 Mfx_Abs_s32_u8( sint32 ); |
| 0x058 | uint16 Mfx_Abs_s16_u16( sint16 ); |
| 0x059 | sint16 Mfx_Abs_s16_s16( sint16 ); |
| 0x05A | sint16 Mfx_Abs_s32_s16( sint32 ); |
| 0x05B | uint32 Mfx_Abs_s32_u32( sint32 ); |
| 0x05C | sint32 Mfx_Abs_s32_s32( sint32 ); |
| 0x05D | sint8 Mfx_Abs_s32_s8( sint32 ); |
| 0x05E | uint16 Mfx_Abs_s32_u16( sint32 ); |

#### 7.5.4. 差值的绝对值（**Absolute value of a difference**）

##### 7.5.4.1. Mfx_AbsDiff_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 本例程计算两个值之差的绝对值。服务 ID 0x05F 至 0x082。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_AbsDiff_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value )
```

本例程计算两个值之差的绝对值：

```C
Return-value = | x_value - y_value |
```

发生上溢时，返回值应饱和到边界值。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x05F | uint8 Mfx_AbsDiff_u8u8_u8( uint8 , uint8); |
| 0x060 | uint16 Mfx_AbsDiff_u16u16_u16( uint16 , uint16); |
| 0x061 | uint8 Mfx_AbsDiff_s16s16_u8( sint16 , sint16); |
| 0x062 | uint16 Mfx_AbsDiff_s16s16_u16( sint16 , sint16); |
| 0x063 | uint8 Mfx_AbsDiff_u32s32_u8( uint32 , sint32); |
| 0x064 | uint16 Mfx_AbsDiff_u32s32_u16( uint32 , sint32); |
| 0x065 | uint32 Mfx_AbsDiff_u32s32_u32( uint32 , sint32); |
| 0x066 | uint32 Mfx_AbsDiff_u32u32_u32( uint32 , uint32); |
| 0x067 | uint8 Mfx_AbsDiff_s32s32_u8( sint32 , sint32); |
| 0x068 | sint16 Mfx_AbsDiff_s32s32_s16( sint32 , sint32); |
| 0x069 | sint32 Mfx_AbsDiff_s32s32_s32( sint32 , sint32); |
| 0x06A | sint8 Mfx_AbsDiff_s32s32_s8( sint32 , sint32); |
| 0x06B | uint16 Mfx_AbsDiff_s32s32_u16( sint32 , sint32); |
| 0x06C | uint32 Mfx_AbsDiff_s32s32_u32( sint32 , sint32); |
| 0x06D | uint16 Mfx_AbsDiff_u32u32_u16( uint32 , uint32); |
| 0x06E | uint8 Mfx_AbsDiff_u32u32_u8( uint32 , uint32); |
| 0x06F | sint8 Mfx_Absdiff_u32u32_s8( uint32 , uint32); |
| 0x070 | sint16 Mfx_Absdiff_u32u32_s16( uint32 , uint32); |
| 0x071 | sint32 Mfx_Absdiff_u32u32_s32( uint32 , uint32); |
| 0x072 | sint8 Mfx_Absdiff_u32s32_s8( uint32 , sint32); |
| 0x073 | sint16 Mfx_Absdiff_u32s32_s16( uint32 , sint32); |
| 0x074 | sint32 Mfx_Absdiff_u32s32_s32( uint32 , sint32); |
| 0x075 | uint16 Mfx_AbsDiff_u16s16_u16( uint16 , sint16); |
| 0x076 | sint16 Mfx_AbsDiff_u16u16_s16( uint16 , uint16); |
| 0x077 | sint16 Mfx_AbsDiff_u16s16_s16( uint16 , sint16); |
| 0x078 | sint16 Mfx_AbsDiff_s16s16_s16( sint16 , sint16); |
| 0x079 | uint8 Mfx_AbsDiff_u16u16_u8( uint16 , uint16); |
| 0x07A | uint8 Mfx_AbsDiff_u16s16_u8( uint16 , sint16); |
| 0x07B | sint8 Mfx_AbsDiff_u16u16_s8( uint16 , uint16); |
| 0x07C | sint8 Mfx_AbsDiff_u16s16_s8( uint16 , sint16); |
| 0x07D | sint8 Mfx_AbsDiff_s16s16_s8( sint16 , sint16); |
| 0x07E | uint8 Mfx_AbsDiff_u8s8_u8( uint8 , sint8); |
| 0x07F | uint8 Mfx_AbsDiff_s8s8_u8( sint8 , sint8); |
| 0x080 | sint8 Mfx_AbsDiff_u8u8_s8( uint8 , uint8); |
| 0x081 | sint8 Mfx_AbsDiff_u8s8_s8( uint8 , sint8); |
| 0x082 | sint8 Mfx_AbsDiff_s8s8_s8( sint8 , sint8); |

#### 7.5.5. 乘法（**Multiplications**）

##### 7.5.5.1. Mfx_Mul_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 本例程对两个参数进行乘法运算。服务 ID 0x083 至 0x0A7。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_Mul_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value )
```

本例程对两个参数进行乘法运算：

```C
Return-value = x_value * y_value
```

发生负上溢或正上溢时，返回值应饱和到边界值。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x083 | uint8 Mfx_Mul_u8u8_u8( uint8 , uint8); |
| 0x084 | uint8 Mfx_Mul_s8s8_u8( sint8 , sint8); |
| 0x085 | sint8 Mfx_Mul_s8s8_s8( sint8 , sint8); |
| 0x086 | uint16 Mfx_Mul_u16u16_u16( uint16 , uint16); |
| 0x087 | uint16 Mfx_Mul_s16s16_u16( sint16 , sint16); |
| 0x088 | uint8 Mfx_Mul_s16s16_u8( sint16 , sint16); |
| 0x089 | sint8 Mfx_Mul_s16s16_s8( sint16 , sint16); |
| 0x08A | sint16 Mfx_Mul_s16s16_s16( sint16 , sint16); |
| 0x08B | uint32 Mfx_Mul_u32u32_u32( uint32 , uint32); |
| 0x08C | sint32 Mfx_Mul_u32u32_s32( uint32 , uint32); |
| 0x08D | uint32 Mfx_Mul_s32s32_u32( sint32 , sint32); |
| 0x08E | uint8 Mfx_Mul_s32s32_u8( sint32 , sint32); |
| 0x08F | sint8 Mfx_Mul_u32u32_s8( uint32 , uint32); |
| 0x090 | sint8 Mfx_Mul_s32s32_s8( sint32 , sint32); |
| 0x091 | sint16 Mfx_Mul_u32u32_s16( uint32 , uint32); |
| 0x092 | sint16 Mfx_Mul_s32s32_s16( sint32 , sint32); |
| 0x093 | uint16 Mfx_Mul_s32s32_u16( sint32 , sint32); |
| 0x094 | sint32 Mfx_Mul_s32s32_s32( sint32 , sint32); |
| 0x095 | sint16 Mfx_Mul_u32s32_s16( uint32 , sint32); |
| 0x096 | sint8 Mfx_Mul_u32s32_s8( uint32 , sint32); |
| 0x097 | uint8 Mfx_Mul_u32s32_u8( uint32 , sint32); |
| 0x098 | uint16 Mfx_Mul_u32u32_u16( uint32 , uint32); |
| 0x099 | uint8 Mfx_Mul_u32u32_u8( uint32 , uint32); |
| 0x09A | uint8 Mfx_Mul_u8s8_u8( uint8 , sint8); |
| 0x09B | sint8 Mfx_Mul_u8s8_s8( uint8 , sint8); |
| 0x09C | uint16 Mfx_Mul_u16s16_u16( uint16 , sint16); |
| 0x09D | sint16 Mfx_Mul_u16s16_s16( uint16 , sint16); |
| 0x09E | sint32 Mfx_Mul_u16s16_s32( uint16 , sint16); |
| 0x09F | uint16 Mfx_Mul_u32s32_u16( uint32 , sint32); |
| 0x0A0 | uint32 Mfx_Mul_u32s32_u32( uint32 , sint32); |
| 0x0A1 | sint32 Mfx_Mul_u32s32_s32( uint32 , sint32); |
| 0x0A2 | sint16 Mfx_Mul_u16u16_s16( uint16 , uint16); |
| 0x0A3 | uint8 Mfx_Mul_u16u16_u8( uint16 , uint16); |
| 0x0A4 | uint8 Mfx_Mul_u16s16_u8( uint16 , sint16); |
| 0x0A5 | sint8 Mfx_Mul_u16u16_s8( uint16 , uint16); |
| 0x0A6 | sint8 Mfx_Mul_u16s16_s8( uint16 , sint16); |
| 0x0A7 | sint8 Mfx_Mul_u8u8_s8( uint8 , uint8); |

#### 7.5.6. 向 0 舍入的除法（**Divisions rounded towards 0**）

##### 7.5.6.1. Mfx_Div_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 这些例程对两个参数进行除法运算。服务 ID 0x0A8 至 0x0D7。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_Div_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value )
```

这些例程对两个参数进行除法运算：

```C
Return-value = x_value / y_value
```

发生负上溢或正上溢时，返回值应饱和到边界值。

除零后的结果定义为：

* 如果 x_value ≥ 0，则函数返回输出类型的最大值；
* 如果 x_value &lt; 0，则函数返回输出类型的最小值。

结果向 0 舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x0A8 | uint8 Mfx_Div_u8u8_u8( uint8 , uint8); |
| 0x0A9 | uint8 Mfx_Div_s8u8_u8( sint8 , uint8); |
| 0x0AA | uint8 Mfx_Div_u8s8_u8( uint8 , sint8); |
| 0x0AB | uint8 Mfx_Div_s8s8_u8( sint8 , sint8); |
| 0x0AC | sint8 Mfx_Div_u8s8_s8( uint8 , sint8); |
| 0x0AD | sint8 Mfx_Div_s8u8_s8( sint8 , uint8); |
| 0x0AE | sint8 Mfx_Div_s8s8_s8( sint8 , sint8); |
| 0x0AF | uint16 Mfx_Div_u16u16_u16( uint16 , uint16); |
| 0x0B0 | uint16 Mfx_Div_s16u16_u16( sint16 , uint16); |
| 0x0B1 | uint16 Mfx_Div_u16s16_u16( uint16 , sint16); |
| 0x0B2 | sint16 Mfx_Div_u16s16_s16( uint16 , sint16); |
| 0x0B3 | sint16 Mfx_Div_s16u16_s16( sint16 , uint16); |
| 0x0B4 | uint16 Mfx_Div_s16s16_u16( sint16 , sint16); |
| 0x0B5 | uint8 Mfx_Div_s16s16_u8( sint16 , sint16); |
| 0x0B6 | sint8 Mfx_Div_s16s16_s8( sint16 , sint16); |
| 0x0B7 | sint16 Mfx_Div_s16s16_s16( sint16 , sint16); |
| 0x0B8 | sint16 Mfx_Div_s32u32_s16( sint32 , uint32); |
| 0x0B9 | uint32 Mfx_Div_u32u32_u32( uint32 , uint32); |
| 0x0BA | uint32 Mfx_Div_s32u32_u32( sint32 , uint32); |
| 0x0BB | uint32 Mfx_Div_u32s32_u32( uint32 , sint32); |
| 0x0BC | sint32 Mfx_Div_u32s32_s32( uint32 , sint32); |
| 0x0BD | sint32 Mfx_Div_s32u32_s32( sint32 , uint32); |
| 0x0BE | uint32 Mfx_Div_s32s32_u32( sint32 , sint32); |
| 0x0BF | uint8 Mfx_Div_s32s32_u8( sint32 , sint32); |
| 0x0C0 | sint8 Mfx_Div_s32s32_s8( sint32 , sint32); |
| 0x0C1 | uint16 Mfx_Div_s32s32_u16( sint32 , sint32); |
| 0x0C2 | sint16 Mfx_Div_s32s32_s16( sint32 , sint32); |
| 0x0C3 | sint32 Mfx_Div_s32s32_s32( sint32 , sint32); |
| 0x0C4 | sint8 Mfx_Div_u32u32_s8( uint32 , uint32); |
| 0x0C5 | sint16 Mfx_Div_u32u32_s16( uint32 , uint32); |
| 0x0C6 | sint32 Mfx_Div_u32u32_s32( uint32 , uint32); |
| 0x0C7 | sint8 Mfx_Div_s32u32_s8( sint32 , uint32); |
| 0x0C8 | uint16 Mfx_Div_s32u32_u16( sint32 , uint32); |
| 0x0C9 | uint8 Mfx_Div_s32u32_u8( sint32 , uint32); |
| 0x0CA | sint16 Mfx_Div_u32s32_s16( uint32 , sint32); |
| 0x0CB | sint8 Mfx_Div_u32s32_s8( uint32 , sint32); |
| 0x0CC | uint16 Mfx_Div_u32s32_u16( uint32 , sint32); |
| 0x0CD | uint8 Mfx_Div_u32s32_u8( uint32 , sint32); |
| 0x0CE | uint16 Mfx_Div_u32u32_u16( uint32 , uint32); |
| 0x0CF | uint8 Mfx_Div_u32u32_u8( uint32 , uint32); |
| 0x0D0 | sint16 Mfx_Div_u16u16_s16( uint16 , uint16); |
| 0x0D1 | uint8 Mfx_Div_u16u16_u8( uint16 , uint16); |
| 0x0D2 | uint8 Mfx_Div_u16s16_u8( uint16 , sint16); |
| 0x0D3 | uint8 Mfx_Div_s16u16_u8( sint16 , uint16); |
| 0x0D4 | sint8 Mfx_Div_u16u16_s8( uint16 , uint16); |
| 0x0D5 | sint8 Mfx_Div_u16s16_s8( uint16 , sint16); |
| 0x0D6 | sint8 Mfx_Div_s16u16_s8( sint16 , uint16); |
| 0x0D7 | sint8 Mfx_Div_u8u8_s8( uint8 , uint8); |

#### 7.5.7. 四舍五入的除法（**Divisions rounded off**）

##### 7.5.7.1. Mfx_RDiv_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 这些例程对两个参数进行除法运算。服务 ID 0x0D8 至 0x107。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_RDiv_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value )
```

这些例程对两个参数进行除法运算：

```C
Return-value = x_value / y_value
```

发生负上溢或正上溢时，返回值应饱和到边界值。

除零后的结果定义为：

* 如果 x_value ≥ 0，则函数返回输出类型的最大值；
* 如果 x_value &lt; 0，则函数返回输出类型的最小值。

结果四舍五入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 : RDiv |
|---|---|
| 0x0D8 | uint8 Mfx_RDiv_u8u8_u8( uint8 , uint8); |
| 0x0D9 | uint8 Mfx_RDiv_s8u8_u8( sint8 , uint8); |
| 0x0DA | uint8 Mfx_RDiv_u8s8_u8( uint8 , sint8); |
| 0x0DB | uint8 Mfx_RDiv_s8s8_u8( sint8 , sint8); |
| 0x0DC | sint8 Mfx_RDiv_u8s8_s8( uint8 , sint8); |
| 0x0DD | sint8 Mfx_RDiv_s8u8_s8( sint8 , uint8); |
| 0x0DE | sint8 Mfx_RDiv_s8s8_s8( sint8 , sint8); |
| 0x0DF | uint16 Mfx_RDiv_u16u16_u16( uint16 , uint16); |
| 0x0E0 | uint16 Mfx_RDiv_s16u16_u16( sint16 , uint16); |
| 0x0E1 | uint16 Mfx_RDiv_u16s16_u16( uint16 , sint16); |
| 0x0E2 | sint16 Mfx_RDiv_u16s16_s16( uint16 , sint16); |
| 0x0E3 | sint16 Mfx_RDiv_s16u16_s16( sint16 , uint16); |
| 0x0E4 | uint16 Mfx_RDiv_s16s16_u16( sint16 , sint16); |
| 0x0E5 | uint8 Mfx_RDiv_s16s16_u8( sint16 , sint16); |
| 0x0E6 | sint8 Mfx_RDiv_s16s16_s8( sint16 , sint16); |
| 0x0E7 | sint16 Mfx_RDiv_s16s16_s16( sint16 , sint16); |
| 0x0E8 | sint16 Mfx_RDiv_s32u32_s16( sint32 , uint32); |
| 0x0E9 | uint32 Mfx_RDiv_u32u32_u32( uint32 , uint32); |
| 0x0EA | uint32 Mfx_RDiv_s32u32_u32( sint32 , uint32); |
| 0x0EB | uint32 Mfx_RDiv_u32s32_u32( uint32 , sint32); |
| 0x0EC | sint32 Mfx_RDiv_u32s32_s32( uint32 , sint32); |
| 0x0ED | sint32 Mfx_RDiv_s32u32_s32( sint32 , uint32); |
| 0x0EE | uint32 Mfx_RDiv_s32s32_u32( sint32 , sint32); |
| 0x0EF | uint8 Mfx_RDiv_s32s32_u8( sint32 , sint32); |
| 0x0F0 | sint8 Mfx_RDiv_s32s32_s8( sint32 , sint32); |
| 0x0F1 | uint16 Mfx_RDiv_s32s32_u16( sint32 , sint32); |
| 0x0F2 | sint16 Mfx_RDiv_s32s32_s16( sint32 , sint32); |
| 0x0F3 | sint32 Mfx_RDiv_s32s32_s32( sint32 , sint32); |
| 0x0F4 | sint8 Mfx_RDiv_u32u32_s8( uint32 , uint32); |
| 0x0F5 | sint16 Mfx_RDiv_u32u32_s16( uint32 , uint32); |
| 0x0F6 | sint32 Mfx_RDiv_u32u32_s32( uint32 , uint32); |
| 0x0F7 | sint8 Mfx_RDiv_s32u32_s8( sint32 , uint32); |
| 0x0F8 | uint16 Mfx_RDiv_s32u32_u16( sint32 , uint32); |
| 0x0F9 | uint8 Mfx_RDiv_s32u32_u8( sint32 , uint32); |
| 0x0FA | sint16 Mfx_RDiv_u32s32_s16( uint32 , sint32); |
| 0x0FB | sint8 Mfx_RDiv_u32s32_s8( uint32 , sint32); |
| 0x0FC | uint16 Mfx_RDiv_u32s32_u16( uint32 , sint32); |
| 0x0FD | uint8 Mfx_RDiv_u32s32_u8( uint32 , sint32); |
| 0x0FE | uint16 Mfx_RDiv_u32u32_u16( uint32 , uint32); |
| 0x0FF | uint8 Mfx_RDiv_u32u32_u8( uint32 , uint32); |
| 0x100 | sint16 Mfx_RDiv_u16u16_s16( uint16 , uint16); |
| 0x101 | uint8 Mfx_RDiv_u16u16_u8( uint16 , uint16); |
| 0x102 | uint8 Mfx_RDiv_u16s16_u8( uint16 , sint16); |
| 0x103 | uint8 Mfx_RDiv_s16u16_u8( sint16 , uint16); |
| 0x104 | sint8 Mfx_RDiv_u16u16_s8( uint16 , uint16); |
| 0x105 | sint8 Mfx_RDiv_u16s16_s8( uint16 , sint16); |
| 0x106 | sint8 Mfx_RDiv_s16u16_s8( sint16 , uint16); |
| 0x107 | sint8 Mfx_RDiv_u8u8_s8( uint8 , uint8); |

#### 7.5.8. 乘法与向 0 舍入除法的组合（**Combinations of multiplication and division rounded towards 0**）

##### 7.5.8.1. Mfx_MulDiv_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;&lt;InTypeMn3&gt;_&lt;OutTypeMn&gt;

**说明**: 这些例程对两个参数进行乘法运算，并除以第三个参数。服务 ID 0x108 至 0x121。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数 z_value（in）：第三个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_MulDiv_<InTypeMn1><InTypeMn2><InTypeMn3>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value, <InType3> z_value )
```

这些例程对两个参数进行乘法运算，并除以第三个参数：

```C
Return-value = x_value * y_value / z_value
```

发生负上溢或正上溢时，返回值应饱和到边界值。

除零后的结果定义为：

* 如果 x_value*y_value ≥ 0，则函数返回输出类型的最大值；
* 如果 x_value*y_value &lt; 0，则函数返回输出类型的最小值。

结果向 0 舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 : Div |
|---|---|
| 0x108 | uint16 Mfx_MulDiv_s32s32s32_u16( sint32 , sint32 , sint32); |
| 0x109 | sint16 Mfx_MulDiv_s32s32s32_s16( sint32 , sint32 , sint32); |
| 0x10A | uint16 Mfx_MulDiv_u32u32u16_u16( uint32 , uint32 , uint16); |
| 0x10B | sint16 Mfx_MulDiv_s32s32s16_s16( sint32 , sint32 , sint16); |
| 0x10C | uint16 Mfx_MulDiv_s16u16s16_u16( sint16 , uint16 , sint16); |
| 0x10D | uint16 Mfx_MulDiv_s16u16u16_u16( sint16 , uint16 , uint16); |
| 0x10E | uint16 Mfx_MulDiv_u16u16u16_u16( uint16 , uint16 , uint16); |
| 0x10F | sint16 Mfx_MulDiv_s16u16s16_s16( sint16 , uint16 , sint16); |
| 0x110 | sint16 Mfx_MulDiv_s16s16u16_s16( sint16 , sint16 , uint16); |
| 0x111 | sint16 Mfx_MulDiv_s16u16u16_s16( sint16 , uint16 , uint16); |
| 0x112 | sint16 Mfx_MulDiv_s16s16s16_s16( sint16 , sint16 , sint16); |
| 0x113 | uint32 Mfx_MulDiv_u32u32u32_u32( uint32 , uint32 , uint32); |
| 0x114 | uint32 Mfx_MulDiv_u32u32s32_u32( uint32 , uint32 , sint32); |
| 0x115 | uint32 Mfx_MulDiv_u32s32u32_u32( uint32 , sint32 , uint32); |
| 0x116 | uint32 Mfx_MulDiv_u32s32s32_u32( uint32 , sint32 , sint32); |
| 0x117 | sint32 Mfx_MulDiv_s32s32u32_s32( sint32 , sint32 , uint32); |
| 0x118 | sint32 Mfx_MulDiv_s32u32s32_s32( sint32 , uint32 , sint32); |
| 0x119 | sint32 Mfx_MulDiv_s32u32u32_s32( sint32 , uint32 , uint32); |
| 0x11A | sint32 Mfx_MulDiv_s32s32s32_s32( sint32 , sint32 , sint32); |
| 0x11B | uint16 Mfx_MulDiv_u32u32u32_u16( uint32 , uint32 , uint32); |
| 0x11C | uint16 Mfx_MulDiv_u16s16s16_u16( uint16 , sint16 , sint16); |
| 0x11D | uint16 Mfx_MulDiv_u16s16u16_u16( uint16 , sint16 , uint16); |
| 0x11E | sint16 Mfx_MulDiv_u16s16s16_s16( uint16 , sint16 , sint16); |
| 0x11F | sint16 Mfx_MulDiv_u16s16u16_s16( uint16 , sint16 , uint16); |
| 0x120 | sint32 Mfx_MulDiv_u32s32s32_s32( uint32 , sint32 , sint32); |
| 0x121 | sint32 Mfx_MulDiv_u32s32u32_s32( uint32 , sint32 , uint32); |

**注意：** 由于可交换性（**commutativity**）导致的冗余将在下一个版本中减少。

#### 7.5.9. 乘法与四舍五入除法的组合（**Combinations of multiplication and division rounded off**）

##### 7.5.9.1. Mfx_RMulDiv_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;&lt;InTypeMn3&gt;_&lt;OutTypeMn&gt;

**说明**: 这些例程对两个参数进行乘法运算，并除以第三个参数。服务 ID 0x122 至 0x13B。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数 z_value（in）：第三个参数。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_RMulDiv_<InTypeMn1><InTypeMn2><InTypeMn3>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value, <InType3> z_value )
```

这些例程对两个参数进行乘法运算，并除以第三个参数：

```C
Return-value = x_value * y_value / z_value
```

发生负上溢或正上溢时，返回值应饱和到边界值。

除零后的结果定义为：

* 如果 x_value*y_value ≥ 0，则函数返回输出类型的最大值；
* 如果 x_value*y_value &lt; 0，则函数返回输出类型的最小值。

结果四舍五入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 : RDiv |
|---|---|
| 0x122 | uint16 Mfx_RMulDiv_s32s32s32_u16( sint32 , sint32 , sint32); |
| 0x123 | sint16 Mfx_RMulDiv_s32s32s32_s16( sint32 , sint32 , sint32); |
| 0x124 | uint16 Mfx_RMulDiv_u32u32u16_u16( uint32 , uint32 , uint16); |
| 0x125 | sint16 Mfx_RMulDiv_s32s32s16_s16( sint32 , sint32 , sint16); |
| 0x126 | uint16 Mfx_RMulDiv_s16u16s16_u16( sint16 , uint16 , sint16); |
| 0x127 | uint16 Mfx_RMulDiv_s16u16u16_u16( sint16 , uint16 , uint16); |
| 0x128 | uint16 Mfx_RMulDiv_u16u16u16_u16( uint16 , uint16 , uint16); |
| 0x129 | sint16 Mfx_RMulDiv_s16u16s16_s16( sint16 , uint16 , sint16); |
| 0x12A | sint16 Mfx_RMulDiv_s16s16u16_s16( sint16 , sint16 , uint16); |
| 0x12B | sint16 Mfx_RMulDiv_s16u16u16_s16( sint16 , uint16 , uint16); |
| 0x12C | sint16 Mfx_RMulDiv_s16s16s16_s16( sint16 , sint16 , sint16); |
| 0x12D | uint32 Mfx_RMulDiv_u32u32u32_u32( uint32 , uint32 , uint32); |
| 0x12E | uint32 Mfx_RMulDiv_u32u32s32_u32( uint32 , uint32 , sint32); |
| 0x12F | uint32 Mfx_RMulDiv_u32s32u32_u32( uint32 , sint32 , uint32); |
| 0x130 | uint32 Mfx_RMulDiv_u32s32s32_u32( uint32 , sint32 , sint32); |
| 0x131 | sint32 Mfx_RMulDiv_s32s32u32_s32( sint32 , sint32 , uint32); |
| 0x132 | sint32 Mfx_RMulDiv_s32u32s32_s32( sint32 , uint32 , sint32); |
| 0x133 | sint32 Mfx_RMulDiv_s32u32u32_s32( sint32 , uint32 , uint32); |
| 0x134 | sint32 Mfx_RMulDiv_s32s32s32_s32( sint32 , sint32 , sint32); |
| 0x135 | uint16 Mfx_RMulDiv_u32u32u32_u16( uint32 , uint32 , uint32); |
| 0x136 | uint16 Mfx_RMulDiv_u16s16s16_u16( uint16 , sint16 , sint16); |
| 0x137 | uint16 Mfx_RMulDiv_u16s16u16_u16( uint16 , sint16 , uint16); |
| 0x138 | sint16 Mfx_RMulDiv_u16s16s16_s16( uint16 , sint16 , sint16); |
| 0x139 | sint16 Mfx_RMulDiv_u16s16u16_s16( uint16 , sint16 , uint16); |
| 0x13A | sint32 Mfx_RMulDiv_u32s32s32_s32( uint32 , sint32 , sint32); |
| 0x13B | sint32 Mfx_RMulDiv_u32s32u32_s32( uint32 , sint32 , uint32); |

**注意：** 由于可交换性（**commutativity**）导致的冗余将在下一个版本中减少。

#### 7.5.10. 乘法与右移的组合（**Combinations of multiplication and shift right**）

##### 7.5.10.1. Mfx_MulShRight_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 本例程对两个参数进行乘法运算，并应用由第三个参数定义的右移。服务 ID 0x13C 至 0x151。本服务为同步调用，可重入。参数 x_value（in）：第一个乘数。参数 y_value（in）：第二个乘数。参数 shift（in）：定点数结果的右移。必须是常量表达式。最大移位根据 SWS\_Mfx\_00057。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_MulShRight_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x_value, <InType2> y_value, uint8 shift )
```

本例程对两个参数进行乘法运算，并应用由第三个参数定义的右移：

```C
Return-value = (x_value * y_value) >> shift
```

需要说明的是，对于负数的右移，我们始终保留符号位。

发生负上溢或正上溢时，返回值应饱和到边界值。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 | 关联最大移位 |
|---|---|---|
| 0x13C | uint8 Mfx_MulShRight_s16s16u8_u8( sint16 , sint16 , uint8 ); | 30 |
| 0x13D | sint8 Mfx_MulShRight_s16s16u8_s8( sint16 , sint16 , uint8 ); | 30 |
| 0x13E | sint16 Mfx_MulShRight_s16s16u8_s16( sint16 , sint16 , uint8 ); | 30 |
| 0x13F | uint16 Mfx_MulShRight_s16s16u8_u16( sint16 , sint16 , uint8 ); | 30 |
| 0x140 | uint8 Mfx_MulShRight_u32s32u8_u8( uint32 , sint32 , uint8 ); | 63 |
| 0x141 | sint8 Mfx_MulShRight_u32s32u8_s8( uint32 , sint32 , uint8 ); | 63 |
| 0x142 | uint16 Mfx_MulShRight_u32s32u8_u16( uint32 , sint32 , uint8 ); | 63 |
| 0x143 | sint16 Mfx_MulShRight_u32s32u8_s16( uint32 , sint32 , uint8 ); | 63 |
| 0x144 | uint32 Mfx_MulShRight_u32s32u8_u32( uint32 , sint32 , uint8 ); | 63 |
| 0x145 | sint32 Mfx_MulShRight_u32s32u8_s32( uint32 , sint32 , uint8 ); | 63 |
| 0x146 | sint8 Mfx_MulShRight_s32s32u8_s8( sint32 , sint32 , uint8 ); | 62 |
| 0x147 | uint8 Mfx_MulShRight_s32s32u8_u8( sint32 , sint32 , uint8 ); | 62 |
| 0x148 | sint16 Mfx_MulShRight_s32s32u8_s16( sint32 , sint32 , uint8 ); | 62 |
| 0x149 | uint16 Mfx_MulShRight_s32s32u8_u16( sint32 , sint32 , uint8 ); | 62 |
| 0x14A | uint32 Mfx_MulShRight_s32s32u8_u32( sint32 , sint32 , uint8 ); | 62 |
| 0x14B | sint32 Mfx_MulShRight_s32s32u8_s32( sint32 , sint32 , uint8 ); | 62 |
| 0x14C | uint8 Mfx_MulShRight_u32u32u8_u8( uint32 , uint32 , uint8 ); | 63 |
| 0x14D | sint8 Mfx_MulShRight_u32u32u8_s8( uint32 , uint32 , uint8 ); | 63 |
| 0x14E | uint16 Mfx_MulShRight_u32u32u8_u16( uint32 , uint32 , uint8 ); | 63 |
| 0x14F | sint16 Mfx_MulShRight_u32u32u8_s16( uint32 , uint32 , uint8 ); | 63 |
| 0x150 | uint32 Mfx_MulShRight_u32u32u8_u32( uint32 , uint32 , uint8 ); | 63 |
| 0x151 | sint32 Mfx_MulShRight_u32u32u8_s32( uint32 , uint32 , uint8 ); | 63 |

如果要查看这些函数的使用示例，请参见第 [**7.7.1**](#771-乘法与右移的组合combinations-of-multiplication-and-shift-right) 小节。

#### 7.5.11. 除法与左移的组合（**Combinations of division and shift left**）

##### 7.5.11.1. Mfx_DivShLeft_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;u8_&lt;OutTypeMn&gt;

**说明**: 本例程对第一个参数应用由第三个参数定义的左移，然后除以第二个参数。服务 ID 0x152 至 0x16E。本服务为同步调用，可重入。参数 x_value（in）：分子。参数 y_value（in）：分母。参数 shift（in）：定点数结果的左移。必须是常量表达式。最大移位根据 SWS\_Mfx\_00064。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，商结果。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_DivShLeft_<InTypeMn1><InTypeMn2>u8_<OutTypeMn> ( <InType1> x_value, <InType2> y_value, uint8 shift )
```

本例程对第一个参数应用由第三个参数定义的左移，然后除以第二个参数：

```C
Return-value = (x_value << shift) / y_value
```

需要说明的是，对于负数的左移，我们始终保留符号位。

发生负上溢或正上溢时，返回值应饱和到边界值。

除零后的结果定义为：

* 如果 x_value ≥ 0，则函数返回输出类型的最大值；
* 如果 x_value &lt; 0，则函数返回输出类型的最小值。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 | 关联最大移位 |
|---|---|---|
| 0x152 | uint8 Mfx_DivShLeft_u8u8u8_u8( uint8 , uint8 , uint8 ); | 8 |
| 0x153 | uint8 Mfx_DivShLeft_u16u16u8_u8( uint16 , uint16 , uint8 ); | 16 |
| 0x154 | uint16 Mfx_DivShLeft_u16u16u8_u16( uint16 , uint16 , uint8 ); | 16 |
| 0x155 | sint16 Mfx_DivShLeft_s16s16u8_s16( sint16 , sint16 , uint8 ); | 16 |
| 0x156 | sint16 Mfx_DivShLeft_s16u16u8_s16( sint16 , uint16 , uint8 ); | 16 |
| 0x157 | uint16 Mfx_DivShLeft_u32u32u8_u16( uint32 , uint32 , uint8 ); | 31 |
| 0x158 | uint32 Mfx_DivShLeft_u32u32u8_u32( uint32 , uint32 , uint8 ); | 31 |
| 0x159 | sint32 Mfx_DivShLeft_s32s32u8_s32( sint32 , sint32 , uint8 ); | 31 |
| 0x15A | sint32 Mfx_DivShLeft_s32u32u8_s32( sint32 , uint32 , uint8 ); | 31 |
| 0x15B | uint8 Mfx_DivShLeft_u32s32u8_u8( uint32 , sint32 , uint8 ); | 31 |
| 0x15C | sint8 Mfx_DivShLeft_u32s32u8_s8( uint32 , sint32 , uint8 ); | 31 |
| 0x15D | uint16 Mfx_DivShLeft_u32s32u8_u16( uint32 , sint32 , uint8 ); | 31 |
| 0x15E | sint16 Mfx_DivShLeft_u32s32u8_s16( uint32 , sint32 , uint8 ); | 31 |
| 0x15F | uint32 Mfx_DivShLeft_u32s32u8_u32( uint32 , sint32 , uint8 ); | 31 |
| 0x160 | sint32 Mfx_DivShLeft_u32s32u8_s32( uint32 , sint32 , uint8 ); | 31 |
| 0x161 | sint8 Mfx_DivShLeft_s32s32u8_s8( sint32 , sint32 , uint8 ); | 31 |
| 0x162 | uint8 Mfx_DivShLeft_s32s32u8_u8( sint32 , sint32 , uint8 ); | 31 |
| 0x163 | sint16 Mfx_DivShLeft_s32s32u8_s16( sint32 , sint32 , uint8 ); | 31 |
| 0x164 | uint16 Mfx_DivShLeft_s32s32u8_u16( sint32 , sint32 , uint8 ); | 31 |
| 0x165 | uint32 Mfx_DivShLeft_s32s32u8_u32( sint32 , sint32 , uint8 ); | 31 |
| 0x166 | uint8 Mfx_DivShLeft_u32u32u8_u8( uint32 , uint32 , uint8 ); | 31 |
| 0x167 | sint8 Mfx_DivShLeft_u32u32u8_s8( uint32 , uint32 , uint8 ); | 31 |
| 0x168 | sint16 Mfx_DivShLeft_u32u32u8_s16( uint32 , uint32 , uint8 ); | 31 |
| 0x169 | sint32 Mfx_DivShLeft_u32u32u8_s32( uint32 , uint32 , uint8 ); | 31 |
| 0x16A | uint8 Mfx_DivShLeft_s32u32u8_u8( sint32 , uint32 , uint8 ); | 31 |
| 0x16B | sint8 Mfx_DivShLeft_s32u32u8_s8( sint32 , uint32 , uint8 ); | 31 |
| 0x16C | uint16 Mfx_DivShLeft_s32u32u8_u16( sint32 , uint32 , uint8 ); | 31 |
| 0x16D | sint16 Mfx_DivShLeft_s32u32u8_s16( sint32 , uint32 , uint8 ); | 31 |
| 0x16E | uint32 Mfx_DivShLeft_s32u32u8_u32( sint32 , uint32 , uint8 ); | 31 |

如果要查看这些函数的使用示例，请参见第 [**7.7.2**](#772-除法与左移的组合combinations-of-division-and-shift-left) 小节。

#### 7.5.12. 取模（**Modulo**）

##### 7.5.12.1. Mfx_Mod_&lt;TypeMn&gt;

**说明**: 如果 y_value 不为零，本例程返回 x_value / y_value 除法的余数。服务 ID 0x16F 至 0x178。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;Type&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<Type> Mfx_Mod_<TypeMn> ( <Type> x_value, <Type> y_value )
```

如果 y_value 为零，则结果为零。

在其他情况下：

```C
Return-value = x_value mod y_value
```

余数的符号与 x_value 的符号相同。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x16F | uint8 Mfx_Mod_u8( uint8 , uint8); |
| 0x170 | sint8 Mfx_Mod_s8( sint8 , sint8); |
| 0x171 | uint16 Mfx_Mod_u16( uint16 , uint16); |
| 0x172 | sint16 Mfx_Mod_s16( sint16 , sint16); |
| 0x173 | uint32 Mfx_Mod_u32( uint32 , uint32); |
| 0x174 | sint32 Mfx_Mod_s32( sint32 , sint32); |
| 0x175 | uint8 Mfx_Mod_u32u32_u8( uint32 , uint32) |
| 0x176 | sint8 Mfx_Mod_s32s32_s8( sint32 , sint32) |
| 0x177 | uint16 Mfx_Mod_u32u32_u16( uint32 , uint32) |
| 0x178 | sint16 Mfx_Mod_s32s32_s16( sint32 , sint32) |

#### 7.5.13. 限幅（**Limiting**）

##### 7.5.13.1. Mfx_Limit_&lt;TypeMn&gt;

**说明**: 本例程将输入值限制在下边界和上边界之间。服务 ID 0x179 至 0x17E。本服务为同步调用，可重入。参数 value（in）：输入值。参数 min_value（in）：下边界。min_value 不得严格大于 max_value。参数 max_value（in）：上边界。max_value 不得严格小于 min_value。参数（inout）：无。参数（out）：无。返回值：&lt;Type&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<Type> Mfx_Limit_<TypeMn> ( <Type> value, <Type> min_value, <Type> max_value )
```

```C
Return-value = min_value if value < min_value
Return-value = max_value if value > max_value
Return-value = value in the other cases
```

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x179 | uint8 Mfx_Limit_u8( uint8 , uint8, uint8); |
| 0x17A | sint8 Mfx_Limit_s8( sint8 , sint8, sint8); |
| 0x17B | uint16 Mfx_Limit_u16( uint16 , uint16, uint16); |
| 0x17C | sint16 Mfx_Limit_s16( sint16 , sint16, sint16); |
| 0x17D | uint32 Mfx_Limit_u32( uint32 , uint32, uint32); |
| 0x17E | sint32 Mfx_Limit_s32( sint32 , sint32, sint32); |

#### 7.5.14. 以单值限定最小值和最大值（**Limitations with only one value for minimum and maximum**）

##### 7.5.14.1. Mfx_Minmax_&lt;TypeMn&gt;

**说明**: 该例程将一个值限幅到取决于 minmax_value 符号的最小值或最大值。服务 ID 0x17F 至 0x184。本服务为同步调用，可重入。参数 value（in）：第一个参数。参数 minmax_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;Type&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<Type> Mfx_Minmax_<TypeMn> ( <Type> value, <Type> minmax_value )
```

结果值为：

```C
minmax_value if minmax_value ≥ 0 and value > minmax_value
minmax_value if minmax_value < 0 and value < minmax_value
value in the other cases
```

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x17F | uint8 Mfx_Minmax_u8( uint8 , uint8); |
| 0x180 | sint8 Mfx_Minmax_s8( sint8 , sint8); |
| 0x181 | uint16 Mfx_Minmax_u16( uint16 , uint16); |
| 0x182 | sint16 Mfx_Minmax_s16( sint16 , sint16); |
| 0x183 | uint32 Mfx_Minmax_u32( uint32 , uint32); |
| 0x184 | sint32 Mfx_Minmax_s32( sint32 , sint32); |

#### 7.5.15. 最小值与最大值（**Minimum and maximum**）

##### 7.5.15.1. Mfx_Min_&lt;TypeMn&gt;

**说明**: 本例程返回两个值中的最小值。服务 ID 0x185 至 0x18A。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;Type&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<Type> Mfx_Min_<TypeMn> ( <Type> x_value, <Type> y_value )
```

```C
Return-value = x_value if x_value < y_value
Return-value = y_value in the other case
```

##### 7.5.15.2. Mfx_Max_&lt;TypeMn&gt;

**说明**: 本例程返回两个值中的最大值。服务 ID 0x18B 至 0x190。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数 y_value（in）：第二个参数。参数（inout）：无。参数（out）：无。返回值：&lt;Type&gt;，计算结果。可通过 **Mfx.h** 获得。

```C
<Type> Mfx_Max_<TypeMn> ( <Type> x_value, <Type> y_value )
```

```C
Return-value = x_value if x_value > y_value
Return-value = y_value in the other case
```

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x185 | uint8 Mfx_Min_u8( uint8 , uint8); |
| 0x186 | sint8 Mfx_Min_s8( sint8 , sint8); |
| 0x187 | uint16 Mfx_Min_u16( uint16 , uint16); |
| 0x188 | sint16 Mfx_Min_s16( sint16 , sint16); |
| 0x189 | uint32 Mfx_Min_u32( uint32 , uint32); |
| 0x18A | sint32 Mfx_Min_s32( sint32 , sint32); |
| 0x18B | uint8 Mfx_Max_u8( uint8 , uint8); |
| 0x18C | sint8 Mfx_Max_s8( sint8 , sint8); |
| 0x18D | uint16 Mfx_Max_u16( uint16 , uint16); |
| 0x18E | sint16 Mfx_Max_s16( sint16 , sint16); |
| 0x18F | uint32 Mfx_Max_u32( uint32 , uint32); |
| 0x190 | sint32 Mfx_Max_s32( sint32 , sint32); |

#### 7.5.16. 符号函数（**Signum Function**）

##### 7.5.16.1. Mfx_Sgn_s32_s8

**说明**: 符号函数（**Signum function**）。提取整数值的符号。服务 ID 0x1dc。本服务为同步调用，可重入。参数 x_value（in）：第一个参数。参数（inout）：无。参数（out）：无。返回值：sint8，第一个参数的符号。可通过 **Mfx.h** 获得。

```C
sint8 Mfx_Sgn_s32_s8 ( sint32 x_value )
```

提取整数值的符号。其定义如下：

```C
Return-value = -1, if x_value < 0
Return-value =  0, if x_value == 0
Return-value =  1, if x_value > 0
```

### 7.6. 2<sup>n</sup> 缩放整数数学函数（**2n Scaled Integer Math Functions**）

对于以下所有函数，大写字母将用于操作数，小写字母将用于小数点（**radix**）。

例如：

- 「x」是操作数，「a」是表示其小数点的参数；
- 「C」是结果，「c」是其小数点的参数。

小数点（**Radix**）将始终是 16 位的有符号整数（sint16）。因此，为了使函数名称更短，小数点的助记符不会出现在函数名称中。

对于所有操作，有效范围仅供参考。实际上，参数超出有效范围的操作将在输出类型的范围内饱和。这有助于优化。

#### 7.6.1. 转换（**Conversion**）

##### 7.6.1.1. 16 位到 8 位 2<sup>n</sup> 缩放整数转换（**16-Bit to 8-Bit 2n Scaled Integer Conversion**）

###### 7.6.1.1.1. Mfx_ConvertP2_&lt;InTypeMn&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程将缩放的 16 位整数转换为缩放的 8 位整数。服务 ID 0x191 至 0x192。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 a（in）：定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-15 &lt;= (c - a) &lt;= 7。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，=2<sup>(c-a)</sup> * x。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_ConvertP2_<InTypeMn>_<OutTypeMn> ( <InType> x, sint16 a, sint16 c )
```

该函数返回定点转换的整数值（C），由 C = 2<sup>(c-a)</sup> * x 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x191 | uint8 Mfx_ConvertP2_u16_u8(uint16 x, sint16 a, sint16 c) |
| 0x192 | sint8 Mfx_ConvertP2_s16_s8(sint16 x, sint16 a, sint16 c) |

##### 7.6.1.2. 8 位到 16 位 2<sup>n</sup> 缩放整数转换（**8-Bit to 16-Bit 2n Scaled Integer Conversion**）

###### 7.6.1.2.1. Mfx_ConvertP2_&lt;InTypeMn&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程将缩放的 8 位整数转换为缩放的 16 位整数。服务 ID 0x193 至 0x194。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 a（in）：定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-7 &lt;= (c - a) &lt;= 15。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，=2<sup>(c-a)</sup> * x。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_ConvertP2_<InTypeMn>_<OutTypeMn> ( <InType> x, sint16 a, sint16 c )
```

该函数返回定点转换的整数值（C），由 C = 2<sup>(c-a)</sup> * x 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x193 | uint16 Mfx_ConvertP2_u8_u16(uint8 x, sint16 a, sint16 c) |
| 0x194 | sint16 Mfx_ConvertP2_s8_s16 (sint8 x, sint16 a, sint16 c) |

##### 7.6.1.3. 32 位到 16 位 2<sup>n</sup> 缩放整数转换（**32-Bit to 16-Bit 2n Scaled Integer Conversion**）

###### 7.6.1.3.1. Mfx_ConvertP2_&lt;InTypeMn&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程将缩放的 32 位整数转换为缩放的 16 位整数。服务 ID 0x195 至 0x196。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 a（in）：定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-31 &lt;= (c - a) &lt;= 15。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，=2<sup>(c-a)</sup> * x。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_ConvertP2_<InTypeMn>_<OutTypeMn> ( <InType> x, sint16 a, sint16 c )
```

该函数返回定点转换的整数值（C），由 C = 2<sup>(c-a)</sup> * x 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x195 | uint16 Mfx_ConvertP2_u32_u16 (uint32 x, sint16 a, sint16 c) |
| 0x196 | sint16 Mfx_ConvertP2_s32_s16 (sint32 x, sint16 a, sint16 c) |

##### 7.6.1.4. 16 位到 32 位 2<sup>n</sup> 缩放整数转换（**16-Bit to 32-Bit 2n Scaled Integer Conversion**）

###### 7.6.1.4.1. Mfx_ConvertP2_&lt;InTypeMn&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程将缩放的 16 位整数转换为缩放的 32 位整数。服务 ID 0x197 至 0x198。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 a（in）：定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-15 &lt;= (c - a) &lt;= 31。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，=2<sup>(c-a)</sup> * x。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_ConvertP2_<InTypeMn>_<OutTypeMn> ( <InType> x, sint16 a, sint16 c )
```

该函数返回定点转换的整数值（C），由 C = 2<sup>(c-a)</sup> * x 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x197 | uint32 Mfx_ConvertP2_u16_u32(uint16 x, sint16 a, sint16 c) |
| 0x198 | sint32 Mfx_ConvertP2_s16_s32(sint16 x, sint16 a, sint16 c) |

#### 7.6.2. 乘法（**Multiplication**）

##### 7.6.2.1. 16 位 2<sup>n</sup> 缩放整数乘法（**16-Bit Multiplication of 2n Scaled Integer**）

###### 7.6.2.1.1. Mfx_MulP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 16 位整数进行乘法运算，缩放系数由输入参数设置。服务 ID 0x199 至 0x19E。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-31 &lt;= (c - b - a) &lt;= 15。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，= 2<sup>(c-b-a)</sup> * [x * y]。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_MulP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点乘法的整数值（C），由 C = 2<sup>(c-b-a)</sup> * [x * y] 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x199 | uint16 Mfx_MulP2_u16u16_u16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x19A | uint16 Mfx_MulP2_u16s16_u16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x19B | uint16 Mfx_MulP2_s16s16_u16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x19C | sint16 Mfx_MulP2_u16u16_s16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x19D | sint16 Mfx_MulP2_u16s16_s16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x19E | sint16 Mfx_MulP2_s16s16_s16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |

##### 7.6.2.2. 32 位 2<sup>n</sup> 缩放整数乘法（**32-Bit Multiplication of 2n Scaled Integer**）

###### 7.6.2.2.1. Mfx_MulP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 32 位整数进行乘法运算，缩放系数由输入参数设置。服务 ID 0x19F 至 0x1A4。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-63 &lt;= (c - b - a) &lt;= 31。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，= 2<sup>(c-b-a)</sup> * [x * y]。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_MulP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点乘法的整数值（C），由 C = 2<sup>(c-b-a)</sup> * [x * y] 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x19F | uint32 Mfx_MulP2_u32u32_u32(uint32 x, uint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1A0 | uint32 Mfx_MulP2_u32s32_u32(uint32 x, sint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1A1 | uint32 Mfx_MulP2_s32s32_u32(sint32 x, sint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1A2 | sint32 Mfx_MulP2_u32u32_s32(uint32 x, uint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1A3 | sint32 Mfx_MulP2_u32s32_s32(uint32 x, sint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1A4 | sint32 Mfx_MulP2_s32s32_s32(sint32 x, sint32 y, sint16 a, sint16 b, sint16 c) |

#### 7.6.3. 除法（**Division**）

##### 7.6.3.1. 16 位 2<sup>n</sup> 缩放整数除法（**16-Bit Division of 2n Scaled Integer**）

###### 7.6.3.1.1. Mfx_DivP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 16 位整数进行除法运算，缩放系数由输入参数设置。服务 ID 0x1A5 至 0x1AC。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-15 &lt;= (c + b - a) &lt;= 31。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，= [2<sup>(c+b-a)</sup> * x] / y。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_DivP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点商的整数值（C），由 C = [2<sup>(c+b-a)</sup> * x] / y 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果除数 y 为零，则结果定义为：

* 如果 x ≥ 0，则函数返回输出类型的最大值；
* 如果 x &lt; 0，则函数返回输出类型的最小值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1A5 | uint16 Mfx_DivP2_u16u16_u16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1A6 | uint16 Mfx_DivP2_u16s16_u16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1A7 | uint16 Mfx_DivP2_s16u16_u16(sint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1A8 | uint16 Mfx_DivP2_s16s16_u16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1A9 | sint16 Mfx_DivP2_u16u16_s16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1AA | sint16 Mfx_DivP2_u16s16_s16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1AB | sint16 Mfx_DivP2_s16u16_s16(sint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1AC | sint16 Mfx_DivP2_s16s16_s16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |

##### 7.6.3.2. 32 位 2<sup>n</sup> 缩放整数除法（**32-Bit Division of 2n Scaled Integer**）

###### 7.6.3.2.1. Mfx_DivP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 32 位整数进行除法运算，缩放系数由输入参数设置。服务 ID 0x1AD 至 0x1B4。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-31 &lt;= (c + b - a) &lt;= 63。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，= [2<sup>(c+b-a)</sup> * x] / y。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_DivP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点商的整数值（C），由 C = [2<sup>(c+b-a)</sup> * x] / y 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果除数 y 为零，则结果定义为：

* 如果 x ≥ 0，则函数返回输出类型的最大值；
* 如果 x &lt; 0，则函数返回输出类型的最小值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1AD | uint32 Mfx_DivP2_u32u32_u32(uint32 x, uint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1AE | uint32 Mfx_DivP2_u32s32_u32(uint32 x, sint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1AF | uint32 Mfx_DivP2_s32u32_u32(sint32 x, uint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1B0 | uint32 Mfx_DivP2_s32s32_u32(sint32 x, sint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1B1 | sint32 Mfx_DivP2_u32u32_s32(uint32 x, uint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1B2 | sint32 Mfx_DivP2_u32s32_s32(uint32 x, sint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1B3 | sint32 Mfx_DivP2_s32u32_s32(sint32 x, uint32 y, sint16 a, sint16 b, sint16 c) |
| 0x1B4 | sint32 Mfx_DivP2_s32s32_s32(sint32 x, sint32 y, sint16 a, sint16 b, sint16 c) |

#### 7.6.4. 加法（**Addition**）

##### 7.6.4.1. 16 位 2<sup>n</sup> 缩放整数加法（**16-Bit Addition of 2n Scaled Integer**）

###### 7.6.4.1.1. Mfx_AddP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 16 位整数进行加法运算，缩放系数由输入参数设置。服务 ID 0x1B5 至 0x1BA。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：0 &lt;= |a - b| &lt;= 15，(c - b) &lt;= 15，(a - c) &lt;= 15（a ≥ b）；(c - a) &lt;= 15，(b - c) &lt;= 15（a &lt; b）。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，a ≥ b 时为 2<sup>(c-a)</sup> * [x + (y * 2<sup>(a-b)</sup>)]，a &lt; b 时为 2<sup>(c-b)</sup> * [(x * 2<sup>(b-a)</sup>) + y]。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_AddP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点和的整数值（C），由以下确定：

a ≥ b：C = 2<sup>(c-a)</sup> * [x + (y * 2<sup>(a-b)</sup>)]，

a &lt; b：C = 2<sup>(c-b)</sup> * [(x * 2<sup>(b-a)</sup>) + y]。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1B5 | uint16 Mfx_AddP2_u16u16_u16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1B6 | uint16 Mfx_AddP2_u16s16_u16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1B7 | uint16 Mfx_AddP2_s16s16_u16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1B8 | sint16 Mfx_AddP2_u16u16_s16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1B9 | sint16 Mfx_AddP2_u16s16_s16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1BA | sint16 Mfx_AddP2_s16s16_s16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |

##### 7.6.4.2. 32 位 2<sup>n</sup> 缩放整数加法（**32-Bit Addition of 2n Scaled Integer**）

###### 7.6.4.2.1. Mfx_AddP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 32 位整数进行加法运算，缩放系数由输入参数设置。服务 ID 0x1BB 至 0x1C0。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：0 &lt;= |a - b| &lt;= 31，(c - b) &lt;= 31，(a - c) &lt;= 31（a ≥ b）；(c - a) &lt;= 31，(b - c) &lt;= 31（a &lt; b）。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，a ≥ b 时为 2<sup>(c-a)</sup> * [x + (y * 2<sup>(a-b)</sup>)]，a &lt; b 时为 2<sup>(c-b)</sup> * [(x * 2<sup>(b-a)</sup>) + y]。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_AddP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点和的整数值（C），由以下确定：

a ≥ b：C = 2<sup>(c-a)</sup> * [x + (y * 2<sup>(a-b)</sup>)]，

a &lt; b：C = 2<sup>(c-b)</sup> * [(x * 2<sup>(b-a)</sup>) + y]。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1BB | uint32 Mfx_AddP2_u32u32_u32(uint32 x, uint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1BC | uint32 Mfx_AddP2_u32s32_u32(uint32 x, sint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1BD | uint32 Mfx_AddP2_s32s32_u32(sint32 x, sint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1BE | sint32 Mfx_AddP2_u32u32_s32(uint32 x, uint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1BF | sint32 Mfx_AddP2_u32s32_s32(uint32 x, sint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1C0 | sint32 Mfx_AddP2_s32s32_s32(sint32 x, sint32 y, sint32 a, sint32 b, sint32 c) |

#### 7.6.5. 减法（**Subtraction**）

##### 7.6.5.1. 16 位 2<sup>n</sup> 缩放整数减法（**16-Bit Subtraction of 2n Scaled Integer**）

###### 7.6.5.1.1. Mfx_SubP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 16 位整数进行减法运算，缩放系数由输入参数设置。服务 ID 0x1C1 至 0x1C8。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：0 &lt;= |a - b| &lt;= 15，(c - b) &lt;= 15，(a - c) &lt;= 15（a ≥ b）；(c - a) &lt;= 15，(b - c) &lt;= 15（a &lt; b）。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，a ≥ b 时为 2<sup>(c-a)</sup> * [x - (y * 2<sup>(a-b)</sup>)]，a &lt; b 时为 2<sup>(c-b)</sup> * [(x * 2<sup>(b-a)</sup>) - y]。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_SubP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点差的整数值（C），由以下确定：

a ≥ b：C = 2<sup>(c-a)</sup> * [x - (y * 2<sup>(a-b)</sup>)]，

a &lt; b：C = 2<sup>(c-b)</sup> * [(x * 2<sup>(b-a)</sup>) - y]。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1C1 | uint16 Mfx_SubP2_u16u16_u16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1C2 | uint16 Mfx_SubP2_u16s16_u16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1C3 | uint16 Mfx_SubP2_s16u16_u16(sint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1C4 | uint16 Mfx_SubP2_s16s16_u16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1C5 | sint16 Mfx_SubP2_u16u16_s16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1C6 | sint16 Mfx_SubP2_u16s16_s16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1C7 | sint16 Mfx_SubP2_s16u16_s16(sint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1C8 | sint16 Mfx_SubP2_s16s16_s16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |

##### 7.6.5.2. 32 位 2<sup>n</sup> 缩放整数减法（**32-Bit Subtraction of 2n Scaled Integer**）

###### 7.6.5.2.1. Mfx_SubP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 32 位整数进行减法运算，缩放系数由输入参数设置。服务 ID 0x1C9 至 0x1D0。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：0 &lt;= |a - b| &lt;= 31，(c - b) &lt;= 31，(a - c) &lt;= 31（a ≥ b）；(c - a) &lt;= 31，(b - c) &lt;= 31（a &lt; b）。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，a ≥ b 时为 2<sup>(c-a)</sup> * [x - (y * 2<sup>(a-b)</sup>)]，a &lt; b 时为 2<sup>(c-b)</sup> * [(x * 2<sup>(b-a)</sup>) - y]。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_SubP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点差的整数值（C），由以下确定：

a ≥ b：C = 2<sup>(c-a)</sup> * [x - (y * 2<sup>(a-b)</sup>)]，

a &lt; b：C = 2<sup>(c-b)</sup> * [(x * 2<sup>(b-a)</sup>) - y]。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1C9 | uint32 Mfx_SubP2_u32u32_u32(uint32 x, uint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1CA | uint32 Mfx_SubP2_u32s32_u32(uint32 x, sint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1CB | uint32 Mfx_SubP2_s32u32_u32(sint32 x, uint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1CC | uint32 Mfx_SubP2_s32s32_u32(sint32 x, sint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1CD | sint32 Mfx_SubP2_u32u32_s32(uint32 x, uint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1CE | sint32 Mfx_SubP2_u32s32_s32(uint32 x, sint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1CF | sint32 Mfx_SubP2_s32u32_s32(sint32 x, uint32 y, sint32 a, sint32 b, sint32 c) |
| 0x1D0 | sint32 Mfx_SubP2_s32s32_s32(sint32 x, sint32 y, sint32 a, sint32 b, sint32 c) |

#### 7.6.6. 2<sup>n</sup> 缩放整数的绝对差（**Absolute Difference of 2n Scaled Integer**）

##### 7.6.6.1. Mfx_AbsDiffP2_&lt;InTypeMn1&gt;&lt;InTypeMn2&gt;_&lt;OutTypeMn&gt;

**说明**: 该例程对两个 16 位整数进行减法并取绝对值，缩放系数由输入参数设置。服务 ID 0x1D1 至 0x1D6。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 y（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 b（in）：第二个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：0 &lt;= |a - b| &lt;= 15，(c - b) &lt;= 15，(a - c) &lt;= 15（a ≥ b）；(c - a) &lt;= 15，(b - c) &lt;= 15（a &lt; b）。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，a ≥ b 时为 2<sup>(c-a)</sup> * |x - (y * 2<sup>(a-b)</sup>)|，a &lt; b 时为 2<sup>(c-b)</sup> * |(x * 2<sup>(b-a)</sup>) - y|。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_AbsDiffP2_<InTypeMn1><InTypeMn2>_<OutTypeMn> ( <InType1> x, <InType2> y, sint16 a, sint16 b, sint16 c )
```

该函数返回定点绝对差的整数值（C），由以下确定：

a ≥ b：C = 2<sup>(c-a)</sup> * |x - (y * 2<sup>(a-b)</sup>)|，

a &lt; b：C = 2<sup>(c-b)</sup> * |(x * 2<sup>(b-a)</sup>) - y|。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1D1 | uint16 Mfx_AbsDiffP2_u16u16_u16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1D2 | uint16 Mfx_AbsDiffP2_u16s16_u16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1D3 | uint16 Mfx_AbsDiffP2_s16s16_u16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1D4 | sint16 Mfx_AbsDiffP2_u16u16_s16(uint16 x, uint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1D5 | sint16 Mfx_AbsDiffP2_u16s16_s16(uint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |
| 0x1D6 | sint16 Mfx_AbsDiffP2_s16s16_s16(sint16 x, sint16 y, sint16 a, sint16 b, sint16 c) |

#### 7.6.7. 绝对值（**Absolute Value**）

##### 7.6.7.1. 16 位 2<sup>n</sup> 缩放整数的绝对值（**16-Bit Absolute Value of 2n Scaled Integer**）

###### 7.6.7.1.1. Mfx_AbsP2_s16_&lt;OutTypeMn&gt;

**说明**: 该例程对一个 16 位整数取绝对值，缩放系数由输入参数设置。服务 ID 0x1D7 至 0x1D8。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-15 &lt;= (c - a) &lt;= 15。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，2<sup>(c-a)</sup> * |x|。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_AbsP2_s16_<OutTypeMn> ( <InType1> x, sint16 a, sint16 c )
```

该函数返回定点绝对值的整数值（C），由 C = 2<sup>(c-a)</sup> * |x| 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1D7 | uint16 Mfx_AbsP2_s16_u16(sint16 x, sint16 a, sint16 c) |
| 0x1D8 | sint16 Mfx_AbsP2_s16_s16(sint16 x, sint16 a, sint16 c) |

##### 7.6.7.2. 32 位 2<sup>n</sup> 缩放整数的绝对值（**32-Bit Absolute Value of 2n Scaled Integer**）

###### 7.6.7.2.1. Mfx_AbsP2_s32_&lt;OutTypeMn&gt;

**说明**: 该例程对一个 32 位整数取绝对值，缩放系数由输入参数设置。服务 ID 0x1D9 至 0x1DA。本服务为同步调用，可重入。参数 x（in）：定点操作数的整数值。参数 a（in）：第一个定点操作数的小数点位置。必须是常量表达式。参数 c（in）：定点结果的小数点位置。必须是常量表达式。有效范围：-31 &lt;= (c - a) &lt;= 31。参数（inout）：无。参数（out）：无。返回值：&lt;OutType&gt;，2<sup>(c-a)</sup> * |x|。可通过 **Mfx.h** 获得。

```C
<OutType> Mfx_AbsP2_s32_<OutTypeMn> ( <InType1> x, sint16 a, sint16 c )
```

该函数返回定点绝对值的整数值（C），由 C = 2<sup>(c-a)</sup> * |x| 确定。

发生负上溢或正上溢时，返回值应饱和到边界值。

如果需要对该等式的结果进行舍入，则向零舍入。

以下是已实现函数的列表：

| 函数 ID [hex] | 函数原型 |
|---|---|
| 0x1D9 | uint32 Mfx_AbsP2_s32_u32(sint32 x, sint16 a, sint16 c) |
| 0x1DA | sint32 Mfx_AbsP2_s32_s32(sint32 x, sint16 a, sint16 c) |

### 7.7. 函数使用示例（**Examples of use of functions**）

#### 7.7.1. 乘法与右移的组合（**Combinations of multiplication and shift right**）

将一个参数乘以给定范围的因子的函数，可以解释为乘法与右移的组合。

如果我们考虑该因子是 2 的幂：2<sup>n1</sup>；

如果我们考虑用于编码该因子的类型的最大值：2<sup>n2</sup>-1；

那么，我们应对乘法结果应用的右移由 (n2-n1) 给出。

例如，我们将一个 s8 值（argument1）乘以用 u8 编码的因子 1（2<sup>0</sup>）（Max(u8)=2<sup>8</sup>-1）。

该因子的物理范围为 [0, 0.996]。

结果为：

```C
Mfx_MulShRight_s16s16u8_s8(argument1, factor, 8)
```

#### 7.7.2. 除法与左移的组合（**Combinations of division and shift left**）

在动力总成（**power train**）领域，将两个参数相除以计算给定范围因子的函数，可以解释为除法与左移的组合。

如果我们考虑该因子是 2 的幂：2<sup>n1</sup>；

如果我们考虑用于编码结果（因子）的类型的最大值：2<sup>n2</sup>-1；

那么，我们应对除法结果应用的左移由 (n2-n1) 给出。

例如，我们将两个 u16 值（argument1 和 argument2）相除，以获得用 u16 编码的因子 1（2<sup>0</sup>）（Max(u16)=2<sup>16</sup>-1）。

结果的物理范围为 [0, 0.999985]。

结果为：

```C
Mfx_DivShLeft_u16u16u8_u16(argument1, argument2, 16)
```

### 7.8. 版本 API（**Version API**）

#### 7.8.1. Mfx_GetVersionInfo

**说明**: 返回本库的版本信息。服务 ID 0x1DB。本服务为同步调用，可重入。参数（in）：无。参数（inout）：无。参数 versioninfo（out）：指向存储本模块版本信息的位置，格式遵循 [BSW00321] 的规定。返回值：无。可通过 **Mfx.h** 获得。

```C
void Mfx_GetVersionInfo ( Std_VersionInfoType* versioninfo )
```

**BSW** 模块的版本信息通常包含：

- 模块 Id
- 供应商 Id
- 供应商特定的版本号。

如果 Mfx_GetVersionInfo 的调用方与被调用方的源代码均可用，**Mfx** 库应将 Mfx_GetVersionInfo 实现为在模块头文件中定义的宏。

### 7.9. 回调通知

**Mfx** 模块没有回调通知。

### 7.10. 调度函数

**MFX** 库没有调度函数。

### 7.11. 期望接口

#### 7.11.1. 强制接口

无强制接口。

#### 7.11.2. 可选接口

无可选接口。

#### 7.11.3. 可配置接口

无可配置接口。

### 7.12. 服务接口

**Mfx** 模块没有服务接口。

## 8. 配置规范

总体而言，本章定义配置参数及其到容器的聚类组织。为支持本规范，第 8.1 章描述基础知识，并规定了应用于参数规范的模板（表）。我们有意将第 8.1 章保留在规范中以保证可理解性。

第 8.2 章规定模块 **MFXLibrary** 的结构（容器）和参数。

第 8.3 章规定模块 **MFXLibrary** 的发布信息。

### 8.1. 如何阅读本章

详情请参阅 SWS\_BSWGeneral 中的第 10.1 章「Introduction to configuration specification」（配置规范简介）。

### 8.2. 容器与配置参数

**MFX** 库不应具有任何可能影响例程功能行为的配置选项。即对于给定的一组输入参数，输出应始终相同。例如，发生错误时返回的值不应是可配置的。

然而，允许库供应商添加与库实现相关的特定配置选项，例如用于资源消耗优化。

### 8.3. 发布信息

详情请参阅 SWS\_BSWGeneral 中的第 10.3 章「Published Information」（发布信息）。

**Mfx** 模块应在头文件中发布基础软件模块通用要求 [第 3.1 章] 中 SRS\_BSW\_00402 所要求的标准化公共发布参数，并需要在 **BSW** 模块描述中提供这些参数。相应的模块缩写可在基础软件模块列表 [第 3.1 章] 中找到。

如适用，下面列出了其他模块特有的发布参数。

## B. AUTOSAR 可追溯项变更历史

请注意，本章中的列表还包含在后续版本中已从规范中删除的规范项。这些规范项在文档中不显示为超链接。

### B.1. 本文档与 AUTOSAR R22-11 相比的规范项变更历史

#### B.1.1. R23-11 中新增的规范项

无

#### B.1.2. R23-11 中变更的规范项

无

#### B.1.3. R23-11 中删除的规范项

无
