---
title: "AUTOSAR Port Driver（端口驱动）"
---

## 1. 简介和功能概述

本规范规定了**AUTOSAR**基础软件模块**PORT**驱动程序的功能、**API**和配置。

本驱动程序规范适用于片上端口和端口引脚。

本模块应提供初始化微控制器整个**PORT**结构的服务。许多端口和端口引脚可以被分配给各种功能，例如：

* 通用**I/O**
* **ADC**
* **SPI**
* **SCI**
* **PWM**
* **CAN**
* **LIN**
* 等等

因此，应对此端口结构进行整体配置和初始化。这些端口引脚的配置和模式取决于微控制器和**ECU**。

端口初始化数据应尽可能高效地写入每个端口。

本**PORT**驱动程序模块应完成**DIO**驱动程序模块中使用的端口结构的整体配置和初始化。因此，**DIO**驱动程序作用于由**PORT**驱动程序配置的引脚和端口。

**PORT**驱动程序应在使用**DIO**函数之前初始化。否则**DIO**函数将表现出未定义的行为。

下图标识了**PORT**驱动程序的功能，以及**PORT**驱动程序和**DIO**驱动程序在**MCAL**软件层中的结构[1]。

![Figure1-1](Figure1-1.png)

## 2. 缩略语和缩写

下表总结了**PORT**驱动程序中使用的表述。

| 缩写/首字母缩写 | 描述 |
|---|---|
| DEM | 诊断事件管理器（Diagnostic Event Manager）[2] |
| DET | 默认错误跟踪器（Default Error Tracer）[3] |
| MCU | 微控制器单元（MicroController Unit） |
| Port Pin | 表示**MCU**器件上单个可配置的输入或输出引脚。 |
| Port | 表示**MCU**器件上整个可配置的端口。 |
| Physical Level (Input) | 两种可能的状态：**LOW**/**HIGH** |
| Physical Level (Output) | 两种可能的状态：**LOW**/**HIGH** |

## 3. 相关文档

### 3.1. 输入文件

[1] Layered Software Architecture
AUTOSAR_CP_EXP_LayeredSoftwareArchitecture

[2] Specification of Diagnostic Event Manager
AUTOSAR_CP_SWS_DiagnosticEventManager

[3] Specification of Default Error Tracer
AUTOSAR_CP_SWS_DefaultErrorTracer

[4] General Specification of Basic Software Modules
AUTOSAR_CP_SWS_BSWGeneral

[5] General Requirements on Basic Software Modules
AUTOSAR_CP_SRS_BSWGeneral

[6] General Requirements on SPAL
AUTOSAR_CP_SRS_SPALGeneral

[7] Requirements on Port Driver
AUTOSAR_CP_SRS_PortDriver

[8] Specification of MCU Driver
AUTOSAR_CP_SWS_MCUDriver

### 3.2. 相关标准和规范

1. IEC 7498-1 The Basic Model, IEC Norm, 1994

### 3.3. 相关规范

**AUTOSAR**提供了基础软件模块通用规范[4]（**SWS BSW General**），该规范同样适用于**Port**驱动程序。

因此，**SWS BSW General**规范应被视为**Port**驱动程序的附加必需规范。

## 4. 约束和假设

### 4.1. 限制

**PORT**驱动程序的限制规定如下：

* 用户有责任确保同一系统中不同的实体不会并行访问同一端口/端口引脚，例如两个任务配置同一端口、两个任务配置同一引脚，或两个任务配置同一端口上的不同引脚。

### 4.2. 对汽车域的适用性

无限制

## 5. 对其他模块的依赖

其他驱动模块可能依赖于**PORT**驱动程序，具体取决于**MCU**上单个端口引脚的可用功能。例如，一个**MCU**引脚可能可配置为**DIO**或**SPI**引脚。因此，**DIO**和/或**SPI**驱动模块可能依赖**PORT**模块将引脚配置为所需的功能。

### 5.1. 文件结构

#### 5.1.1. 代码文件结构

详情请参阅[4]中第 5.1.6 章"Code file structure"。

## 6. 需求可追溯性

本章引用了适用于本软件模块的**SRS**文档（软件需求规范[5]、[6]、[7]）中规定的输入需求。

下表列出了**PORT**驱动程序**SWS**文档中满足输入需求的规范条目。仅引用功能性需求。

| 需求 | 描述 | 满足项 |
|---|---|---|
| [SRS_BSW_00101] | 基础软件模块应能够在单独的初始化函数中初始化变量和硬件 | [SWS_Port_00001] [SWS_Port_00002] [SWS_Port_00041] [SWS_Port_00042] |
| [SRS_BSW_00159] | **AUTOSAR**基础软件的所有模块应支持基于工具的配置 | [SWS_Port_00004] |
| [SRS_BSW_00323] | 所有**AUTOSAR**基础软件模块应检查传入的**API**参数的有效性 | [SWS_Port_00087] |
| [SRS_BSW_00327] | 错误值命名约定 | [SWS_Port_00051] |
| [SRS_BSW_00337] | 开发错误分类 | [SWS_Port_00051] |
| [SRS_BSW_00358] | **AUTOSAR**基础软件模块实现的**init()**函数的返回类型应为**void** | [SWS_Port_00140] |
| [SRS_BSW_00385] | 列出可能的错误通知 | [SWS_Port_00051] |
| [SRS_BSW_00404] | **BSW**模块应支持后构建（post-build）配置 | [SWS_Port_00041] |
| [SRS_BSW_00406] | 表示**BSW**模块是否已初始化的静态状态变量，在调用该**BSW**模块的任何**API**之前应以值 0 初始化 | [SWS_Port_00051] [SWS_Port_00087] |
| [SRS_BSW_00414] | **Init**函数应将指向配置结构的指针作为单一参数 | [SWS_Port_00121] |
| [SRS_Port_12001] | **Port**驱动程序应允许对每个端口静态配置以下选项 | [SWS_Port_00004] [SWS_Port_00079] |
| [SRS_Port_12300] | 未使用的端口和端口引脚应被设置为确定的状态 | [SWS_Port_00005] |
| [SRS_Port_12302] | **Port**驱动程序应允许端口引脚名称的静态配置 | [SWS_Port_00006] |
| [SRS_Port_12405] | **Port**驱动程序应提供在运行时设置端口引脚方向的服务 | [SWS_Port_00063] [SWS_Port_00086] [SWS_Port_00138] |
| [SRS_Port_12406] | **Port**驱动程序应提供刷新所有已配置端口方向的服务 | [SWS_Port_00060] [SWS_Port_00061] |
| [SRS_SPAL_12057] | 所有驱动模块应实现初始化接口 | [SWS_Port_00041] [SWS_Port_00042] [SWS_Port_00043] |
| [SRS_SPAL_12125] | 所有驱动模块应仅初始化已配置的资源 | [SWS_Port_00041] [SWS_Port_00042] |
| [SRS_SPAL_12163] | 所有驱动模块应实现去初始化接口 | [SWS_Port_00003] |
| [SRS_SPAL_12263] | 所有驱动模块的实现应允许在链接时配置特定模块参数类型 | [SWS_Port_00041] |
| [SRS_SPAL_12448] | 所有驱动模块在检测到开发错误后应具有特定行为 | [SWS_Port_00077] |
| [SRS_SPAL_12461] | 关于控制器寄存器初始化的特定规则应适用于所有驱动实现 | [SWS_Port_00113] [SWS_Port_00214] [SWS_Port_00215] [SWS_Port_00217] [SWS_Port_00218] |

## 7. 功能规格

### 7.1. 一般行为

#### 7.1.1. 背景与原理

[SWS_Port_00001] **PORT**驱动程序模块应初始化微控制器的整个端口结构。

注意：定义端口和端口引脚的配置顺序是配置工具的任务。

#### 7.1.2. 需求

##### 7.1.2.1. 端口引脚属性的配置

[SWS_Port_00004] **PORT**驱动程序模块应允许为每个端口和端口引脚配置不同的功能，例如**ADC**、**SPI**、**DIO**等。

端口（即整个端口或单个端口引脚）的配置取决于微控制器。

[SWS_Port_00079] **PORT**驱动程序模块应为**MCU**端口/端口引脚提供以下附加配置：

* 引脚方向（输入/输出）
* 引脚电平初始值
* 引脚方向是否可在运行时更改（是/否）。
* 端口模式是否可在运行时更改。

[SWS_Port_00081] **PORT**驱动程序模块应为**MCU**端口和端口引脚提供一些可选配置（如果硬件支持）：

* 斜率（Slew rate）控制
* 内部上拉的激活
* 输入阈值
* 引脚驱动模式（推挽/开漏）。
* 回读支持的类型（引脚电平、输出寄存器值）。

[SWS_Port_00082] **PORT**驱动程序模块不应提供配置引脚电平反转的功能。应设置默认值（即不反转）。

注意：**I/O**硬件抽象层应执行电平反转。

##### 7.1.2.2. 切换端口引脚方向

[SWS_Port_00137] 对于使用配置工具配置为可更改的端口引脚，**PORT**驱动程序应允许用户在运行时更改端口引脚的方向。

[SWS_Port_00138] 如果**MCU**端口控制硬件提供用于在端口引脚上设置输出电平的输出锁存器，切换端口引脚方向不应改变此输出锁存器中设置的电平。

##### 7.1.2.3. 刷新端口方向

[SWS_Port_00066] 为了在微控制器上刷新端口，**PORT**驱动程序应允许用户刷新那些方向由配置设置且不能动态更改的端口引脚的方向。

##### 7.1.2.4. 未使用的端口和端口引脚的配置

[SWS_Port_00005] **PORT**驱动程序模块应将所有未使用（既不用作**GPIO**也不用作特殊用途**IO**）的端口和端口引脚配置为由**PORT**驱动程序模块配置设置为确定的状态。

##### 7.1.2.5. 符号名称的配置

[SWS_Port_00006] **PORT**驱动程序模块的用户应配置**MCU**端口引脚的符号名称。

[SWS_Port_00207] 单个端口引脚的这些符号名称（例如**PORT_A_PIN_0**）应在配置工具中定义。

[SWS_Port_00208] **PORT**驱动程序模块的实现者应通过文件**Port.h**发布这些符号名称。

##### 7.1.2.6. 端口访问的原子性

[SWS_Port_00075] **PORT**驱动程序模块应提供对所有端口和端口引脚的原子访问。

注意：

原子访问是通过使用原子指令或使用由基础软件调度程序模块提供的独占区域（例如禁用中断）对微控制器寄存器的不可中断访问。

#### 7.1.3. 版本检查

##### 7.1.3.1. 背景和原理

应避免不兼容文件的集成。最低实现是在**.c**文件内检查头文件的版本（**.c**和**.h**文件的版本号应相同）。

##### 7.1.3.2. 需求

**Port**模块应通过以下预处理器检查避免不兼容文件的集成：

详情请参阅[4]（**SWS BSW General**）中第 5.1.8 章"Version Check"。

### 7.2. 错误分类

[SWS_Port_00051] **Port**模块中开发错误的定义

| 错误类型 | 相关错误代码 | 错误值 |
|---|---|---|
| 请求的端口引脚 ID 无效 | PORT_E_PARAM_PIN | 0x0A |
| 端口引脚未配置为可更改 | PORT_E_DIRECTION_UNCHANGEABLE | 0x0B |
| **API Port_Init**服务以错误参数调用 | PORT_E_INIT_FAILED | 0x0C |
| 当模式不可更改时调用**API Port_SetPinMode**服务 | PORT_E_PARAM_INVALID_MODE | 0x0D |
| 当模式不可更改时调用**API Port_SetPinMode**服务 | PORT_E_MODE_UNCHANGEABLE | 0x0E |
| 未经模块初始化调用**API**服务 | PORT_E_UNINIT | 0x0F |
| 以空指针调用**API** | PORT_E_PARAM_POINTER | 0x10 |

#### 7.2.1. 运行时错误

没有运行时错误。

#### 7.2.2. 瞬态故障

没有瞬态故障。

#### 7.2.3. 生产错误

没有生产错误。

#### 7.2.4. 扩展生产错误

没有扩展生产错误。

### 7.3. API 参数检查

[SWS_Port_00077] 如果启用了开发错误检测，**Port**驱动程序模块应按参数传递的顺序检查函数参数，如果一项检查失败则跳过后续的参数检查。

示例：对于函数**Port_SetPinDirection**，传递的第一个参数是引脚**ID**。此参数应标识**MCU**端口的相关端口引脚。传递的第二个参数对应于要在端口引脚上更改的方向。

[SWS_Port_00087] 如果启用了开发错误检测且**Port**驱动程序模块检测到错误，应跳过所需功能，请求的服务应直接返回，不执行任何动作。

参见下表，了解每个函数报告的**Det**错误列表。

| 函数 | 错误条件 | 相关错误值 |
|---|---|---|
| Port_SetPinDirection | 传入的端口引脚 ID 不正确 | PORT_E_PARAM_PIN |
| Port_SetPinDirection | 端口引脚未配置为可更改 | PORT_E_DIRECTION_UNCHANGEABLE |
| Port_Init | Port_Init 服务以错误参数调用。 | PORT_E_INIT_FAILED |
| Port_SetPinMode | 传入的端口引脚 ID 不正确 | PORT_E_PARAM_PIN |
| Port_SetPinMode | 传入的端口引脚模式无效 | PORT_E_PARAM_INVALID_MODE |
| Port_SetPinMode | 当模式不可更改时调用**Port_SetPinMode**服务 | PORT_E_MODE_UNCHANGEABLE |
| Port_SetPinDirection, Port_SetPinMode, Port_RefreshPortDirection | 在模块初始化之前调用**API**服务 | PORT_E_UNINIT |
| Port_GetVersionInfo | 以空指针参数调用**API** | PORT_E_PARAM_POINTER |

## 8. API规范

### 8.1. 导入的类型

本章列出了从以下模块包含的所有类型：

[SWS_Port_00129] **Port**模块的导入数据类型定义

| 模块 | 头文件 | 导入的类型 |
|---|---|---|
| Std_Types.h | Std_ReturnType | Std |
| Std_Types.h | Std_VersionInfoType | |

### 8.2. 类型定义

#### 8.2.1. Port_ConfigType

[SWS_Port_00228] 数据类型**Port_ConfigType**的定义

| 名称 | Port_ConfigType |
|---|---|
| 类型 | Structure |
| 硬件相关结构元素 | 类型 –。注释：初始化数据结构的内容特定于微控制器。 |
| 描述 | 包含本模块初始化数据的外部数据结构的类型。可通过**Port.h**获得 |

#### 8.2.2. Port_PinType

[SWS_Port_00229] 数据类型**Port_PinType**的定义

| 名称 | Port_PinType |
|---|---|
| 类型 | Type |
| 派生自 | uint |
| 范围 | 0 - <端口引脚数量>：应覆盖所有可用的端口引脚。该类型应为特定**MCU**平台选择（最佳性能）。 |
| 描述 | 端口引脚符号名称的数据类型。可通过**Port.h**获得 |

[SWS_Port_00013] **Port_PinType**类型应用于端口引脚的符号名称。

[SWS_Port_00219] **Port_PinType**类型应为**uint8**、**uint16**或**uint32**，基于特定**MCU**平台。

注意：用户应使用配置工具提供的符号名称。

#### 8.2.3. Port_PinDirectionType

[SWS_Port_00230] 数据类型**Port_PinDirectionType**的定义

| 名称 | Port_PinDirectionType |
|---|---|
| 类型 | Enumeration |
| PORT_PIN_IN | 0x00，将端口引脚设置为输入。范围 |
| PORT_PIN_OUT | 0x01，将端口引脚设置为输出。 |
| 描述 | 端口引脚可能的方向。可通过**Port.h**获得 |

[SWS_Port_00046] **Port_PinDirectionType**是定义端口引脚方向的类型。

[SWS_Port_00220] **Port_PinDirectionType**应为枚举类型，其范围为**PORT_PIN_IN**和**PORT_PIN_OUT**。

#### 8.2.4. Port_PinModeType

[SWS_Port_00231] 数据类型**Port_PinModeType**的定义

| 名称 | Port_PinModeType |
|---|---|
| 类型 | Type |
| 派生自 | uint |
| 范围 | 实现特定 —— 由于一个引脚上应可配置多个端口引脚模式，范围应由实现确定。 |
| 描述 | 不同的端口引脚模式。可通过**Port.h**获得 |

[SWS_Port_00124] 端口引脚应可配置多个端口引脚模式（**Port_PinModeType**类型）。

[SWS_Port_00212] **Port_PinModeType**类型应与函数调用**Port_SetPinMode**一起使用。

[SWS_Port_00221] **Port_PinModeType**类型应为**uint8**、**uint16**或**uint32**。

### 8.3. 函数定义

以下是提供给上层模块的函数列表。

#### 8.3.1. Port_Init

[SWS_Port_00140] **API**函数**Port_Init**的定义

| 服务名称 | Port_Init |
|---|---|
| 语法 | void Port_Init (const Port_ConfigType * ConfigPtr) |
| 服务 ID [十六进制] | 0x00 |
| 同步/异步 | 同步 |
| 可重入性 | 不可重入 |
| 参数（in） | ConfigPtr：指向配置集的指针 |
| 参数（inout） | 无 |
| 参数（out） | 无 |
| 返回值 | 无 |
| 描述 | 初始化**Port**驱动程序模块。可通过**Port.h**获得 |

```C
void Port_Init ( const Port_ConfigType * ConfigPtr )
```

[SWS_Port_00041] 函数**Port_Init**应使用参数**ConfigPtr**指向的配置集初始化所有端口和端口引脚。

[SWS_Port_00078] **Port**驱动程序模块的环境应首先调用函数**Port_Init**以初始化端口供使用。

[SWS_Port_00213] 如果未首先调用**Port_Init**函数，则无法对**MCU**端口和端口引脚执行任何操作。

[SWS_Port_00042] 函数**Port_Init**应初始化所有已配置的资源。

函数**Port_Init**应遵循以下关于控制器寄存器初始化的规则。

* [SWS_Port_00113] 如果硬件只允许寄存器的一次使用，则实现该功能的驱动模块负责初始化该寄存器。
* [SWS_Port_00214] 如果寄存器可以影响多个硬件模块且它是**I/O**寄存器，则它应由此**PORT**驱动程序初始化。
* [SWS_Port_00215] 如果寄存器可以影响多个硬件模块且它不是**I/O**寄存器，则它应由**MCU**驱动程序[8]初始化。
* [SWS_Port_00217] 需要在复位后直接初始化的单次可写寄存器应由启动代码初始化。
* [SWS_Port_00218] 所有其他未提及的寄存器应由启动代码初始化。

[SWS_Port_00043] 函数**Port_Init**应避免在受影响的端口引脚上产生毛刺和尖峰。

[SWS_Port_00071] **Port**驱动程序模块的环境应在复位后调用函数**Port_Init**，以重新配置**MCU**的端口和端口引脚。

[SWS_Port_00002] 函数**Port_Init**应将**PORT**驱动程序模块使用的所有变量初始化为初始状态。

[SWS_Port_00003] **Port**驱动程序模块的环境也可以使用函数**Port_Init**来初始化驱动程序软件，并根据传递给此函数的配置集将端口和端口引脚重新初始化为另一个已配置状态。

注意：在某些情况下，**MCU**端口控制硬件提供输出锁存器，用于在可用作**DIO**端口引脚的端口引脚上设置输出电平。

[SWS_Port_00055] 函数**Port_Init**应在将端口引脚方向设置为输出之前，将端口引脚输出锁存器设置为默认电平（在配置期间定义）。

需求[SWS_Port_00055]确保当端口引脚被设置为输出端口引脚时，默认电平立即输出到端口引脚上。

示例：在某些**MCU**上，上电复位后，可配置为**DIO**的端口引脚将被配置为输入引脚。如果端口引脚所需的配置是输出引脚，则函数**Port_Init**应确保在将端口引脚功能从输入切换到输出之前设置默认电平。

[SWS_Port_00121] 函数**Port_Init**应始终具有一个指针作为参数，即使对于配置变体**VARIANT-PRE-COMPILE**，也不会给出配置集。在这种情况下，**Port**驱动程序模块的环境应向函数**Port_Init**传递**NULL**指针。

**Port**驱动程序模块的环境不应在运行操作期间调用函数**Port_Init**。这仅在**PORT**模块有多个调用者时适用。

**Port_Init**的配置：所有端口引脚及其功能、以及备用功能都应由配置工具配置。

#### 8.3.2. Port_SetPinDirection

[SWS_Port_00141] **API**函数**Port_SetPinDirection**的定义

| 服务名称 | Port_SetPinDirection |
|---|---|
| 语法 | void Port_SetPinDirection (Port_PinType Pin, Port_PinDirectionType Direction) |
| 服务 ID [十六进制] | 0x01 |
| 同步/异步 | 同步 |
| 可重入性 | 可重入 |
| 参数（in） | Pin：端口引脚 ID 编号；Direction：端口引脚方向 |
| 参数（inout） | 无 |
| 参数（out） | 无 |
| 返回值 | 无 |
| 描述 | 设置端口引脚方向。可通过**Port.h**获得 |

```C
void Port_SetPinDirection ( Port_PinType Pin, Port_PinDirectionType Direction )
```

[SWS_Port_00063] 函数**Port_SetPinDirection**应在运行时设置端口引脚方向。

[SWS_Port_00054] 如果访问独立于端口的不同引脚，函数**Port_SetPinDirection**应是可重入的。

[SWS_Port_00086] 只有当预编译参数**PortSetPinDirectionApi**设置为**TRUE**时，函数**Port_SetPinDirection**才可提供给用户使用。如果设置为**FALSE**，则函数**Port_SetPinDirection**不可用。

**Port_SetPinDirection**的配置：所有端口和端口引脚应由配置工具配置。参见**PORT117**。

#### 8.3.3. Port_RefreshPortDirection

[SWS_Port_00142] **API**函数**Port_RefreshPortDirection**的定义

| 服务名称 | Port_RefreshPortDirection |
|---|---|
| 语法 | void Port_RefreshPortDirection (void) |
| 服务 ID [十六进制] | 0x02 |
| 同步/异步 | 同步 |
| 可重入性 | 不可重入 |
| 参数（in） | 无 |
| 参数（inout） | 无 |
| 参数（out） | 无 |
| 返回值 | 无 |
| 描述 | 刷新端口方向。可通过**Port.h**获得 |

```C
void Port_RefreshPortDirection ( void )
```

[SWS_Port_00060] 函数**Port_RefreshPortDirection**应将所有已配置端口的方向刷新为配置的方向（**PortPinDirection**）。

[SWS_Port_00061] 函数**Port_RefreshPortDirection**应将那些配置为"引脚方向可在运行时更改"的端口引脚排除在刷新之外。

配置工具应为每个配置的端口引脚提供名称。

#### 8.3.4. Port_GetVersionInfo

[SWS_Port_00143] **API**函数**Port_GetVersionInfo**的定义

| 服务名称 | Port_GetVersionInfo |
|---|---|
| 语法 | void Port_GetVersionInfo (Std_VersionInfoType* versioninfo) |
| 服务 ID [十六进制] | 0x03 |
| 同步/异步 | 同步 |
| 可重入性 | 可重入 |
| 参数（in） | 无 |
| 参数（inout） | 无 |
| 参数（out） | versioninfo：指向存储本模块版本信息位置的指针 |
| 返回值 | 无 |
| 描述 | 返回本模块的版本信息。可通过**Port.h**获得 |

```C
void Port_GetVersionInfo ( Std_VersionInfoType* versioninfo )
```

[SWS_Port_00225] 如果启用了**Det**，应检查参数**versioninfo**是否为**NULL**。如果值为**NULL**指针，应报告错误**PORT_E_PARAM_POINTER**。

#### 8.3.5. Port_SetPinMode

[SWS_Port_00145] **API**函数**Port_SetPinMode**的定义

| 服务名称 | Port_SetPinMode |
|---|---|
| 语法 | void Port_SetPinMode (Port_PinType Pin, Port_PinModeType Mode) |
| 服务 ID [十六进制] | 0x04 |
| 同步/异步 | 同步 |
| 可重入性 | 可重入 |
| 参数（in） | Pin：端口引脚 ID 编号；Mode：要在端口引脚上设置的新端口引脚模式 |
| 参数（inout） | 无 |
| 参数（out） | 无 |
| 返回值 | 无 |
| 描述 | 设置端口引脚模式。可通过**Port.h**获得 |

```C
void Port_SetPinMode ( Port_PinType Pin, Port_PinModeType Mode )
```

[SWS_Port_00125] 函数**Port_SetPinMode**应在运行时设置引用引脚的端口引脚模式。

[SWS_Port_00128] 如果访问独立于端口的不同引脚，函数**Port_SetPinMode**应是可重入的。

[SWS_Port_00223] 如果启用了**Det**，当参数**PortPinModeChangeable**设置为**FALSE**时，函数**Port_SetPinMode**应报告**PORT_E_MODE_UNCHANGEABLE**错误并直接返回，不执行任何其他动作。

**Port_SetPinMode**的配置：所有端口和端口引脚应由配置工具配置。参见**PORT117**。

### 8.4. 回调通知

**PORT**驱动程序没有回调通知。回调通知在其他模块（**ICU**驱动程序和/或复杂驱动程序）中实现。

### 8.5. 调度函数

**PORT**驱动程序中没有调度函数。

### 8.6. 期望接口

本章列出了需要从其他模块获得的所有接口。

#### 8.6.1. 强制接口

无

#### 8.6.2. 可选接口

本章定义了为实现模块的可选功能而需要的所有接口。

[SWS_Port_00146] **Port**模块中可选接口的定义

| API 函数 | 头文件 | 描述 |
|---|---|---|
| Det_ReportError | Det.h | 报告开发错误的服务 |

#### 8.6.3. 可配置接口

无

## 9. 时序图

### 9.1. 端口的整体配置

![Figure9-1](Figure9-1.png)

### 9.2. 设置端口引脚的方向

![Figure9-2](Figure9-2.png)

### 9.3. 刷新所有端口引脚的方向

![Figure9-3](Figure9-3.png)

### 9.4. 更改端口引脚的模式

![Figure9-4](Figure9-4.png)

## 10. 配置规范

总体而言，本章定义配置参数以及它们到容器的聚集。为了支持规范，第 10.1 章描述基础知识。

它还规定了一个你应使用的参数规范模板（表格）。我们打算将第 10.1 章保留在规范中以保证理解。

第 10.2 章规定模块**PORT**的结构（容器）和参数。

第 10.3 章规定模块**PORT**的发布信息。

### 10.1. 如何阅读本章

详情请参阅[4]中第 10.1 章"Introduction to configuration specification"。

### 10.2. 容器和配置参数

以下章节总结了所有配置参数。参数的详细含义见第 7 章和第 8 章。

[SWS_Port_00232] **PORT**模块应拒绝实现不支持的包含分区映射的配置。

#### 10.2.1. PortConfigSet

**SWS 条目** [ECUC_Port_00121]

| 容器名称 | PortConfigSet |
|---|---|
| 父容器 | Port |
| 描述 | 此容器包含**AUTOSAR Port**模块的配置参数和子容器。 |

配置参数

包含的容器

| 容器名称 | 多重性 | 范围/依赖 |
|---|---|---|
| PortContainer | 1..* | 收集**PortPins**的容器。 |

#### 10.2.2. Port

**SWS 条目** [ECUC_Port_00135]

| 模块名称 | Port |
|---|---|
| 描述 | **Port**模块的配置。 |
| Post-Build 变体支持 | true |
| 支持的配置变体 | VARIANT-POST-BUILD, VARIANT-PRE-COMPILE |

包含的容器

| 容器名称 | 多重性 | 范围/依赖 |
|---|---|---|
| PortConfigSet | 1 | 此容器包含**AUTOSAR Port**模块的配置参数和子容器。 |
| PortGeneral | 1 | **PORT**驱动程序的模块范围配置参数。 |

![Figure10-1](Figure10-1.png)

#### 10.2.3. PortContainer

**SWS 条目** [ECUC_Port_00122]

| 容器名称 | PortContainer |
|---|---|
| 父容器 | PortConfigSet |
| 描述 | 收集**PortPins**的容器。 |

配置参数

**SWS 条目** [ECUC_Port_00124]

| 参数名称 | PortNumberOfPortPins |
|---|---|
| 父容器 | PortContainer |
| 描述 | 此**PortContainer**中指定的**PortPins**数量。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 范围 | 1 .. 65535 |
| 默认值 | – |
| Post-Build 变体值 | false |
| 值配置类 | 预编译时间 X（所有变体） |
| 链接时间 | – |
| Post-build 时间 | – |
| 范围/依赖 | scope: local |

包含的容器

| 容器名称 | 多重性 | 范围/依赖 |
|---|---|---|
| PortPin | 1..* | 单个端口引脚的配置。 |

![Figure10-2](Figure10-2.png)

#### 10.2.4. PortGeneral

**SWS 条目** [ECUC_Port_00117]

| 容器名称 | PortGeneral |
|---|---|
| 父容器 | Port |
| 描述 | **PORT**驱动程序的模块范围配置参数。 |

配置参数

**SWS 条目** [ECUC_Port_00123]

| 参数名称 | PortDevErrorDetect |
|---|---|
| 父容器 | PortGeneral |
| 描述 | 打开或关闭开发错误检测和通知。• true：启用检测和通知。• false：禁用检测和通知。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 – |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00131]

| 参数名称 | PortSetPinDirectionApi |
|---|---|
| 父容器 | PortGeneral |
| 描述 | 启用/禁用函数**Port_SetPinDirection()**使用的预处理器开关。**TRUE**：启用 - 函数**Port_SetPinDirection()**可用。**FALSE**：禁用 - 函数**Port_SetPinDirection()**不可用。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | – |
| Post-Build 变体值 | false |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 – |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00132]

| 参数名称 | PortSetPinModeApi |
|---|---|
| 父容器 | PortGeneral |
| 描述 | 启用/禁用函数**Port_SetPinMode()**使用的预处理器开关。**true**：启用 - 函数**Port_SetPinMode()**可用。**false**：禁用 - 函数**Port_SetPinMode()**不可用。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | – |
| Post-Build 变体值 | false |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 – |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00133]

| 参数名称 | PortVersionInfoApi |
|---|---|
| 父容器 | PortGeneral |
| 描述 | 启用/禁用读取模块版本信息的**API**的预处理器开关。**true**：版本信息**API**启用。**false**：版本信息**API**禁用。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 – |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00136]

| 参数名称 | PortEcucPartitionRef |
|---|---|
| 父容器 | PortGeneral |
| 描述 | 将**Port**驱动程序映射到零个或多个**ECUC**分区，以使模块的**API**在此分区中可用。 |
| 多重性 | 0..* |
| 类型 | 对 EcucPartition 的引用 |
| Post-Build 变体多重性 | true |
| Post-Build 变体值 | true |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 多重性配置类 | Post-build 时间 – |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 – |
| 范围/依赖 | scope: ECU |

无包含的容器。

顶层**Port**驱动程序容器持有应用于**PORT**配置的参数。

![Figure10-3](Figure10-3.png)

#### 10.2.5. PortPin

**SWS 条目** [ECUC_Port_00118]

| 容器名称 | PortPin |
|---|---|
| 父容器 | PortContainer |
| 描述 | 单个端口引脚的配置。 |

配置参数

**SWS 条目** [ECUC_Port_00125]

| 参数名称 | PortPinDirection |
|---|---|
| 父容器 | PortPin |
| 描述 | 引脚的初始方向（**IN**或**OUT**）。如果方向不可更改，则此处配置的值是固定的。方向必须与引脚模式匹配。例如，用于**ADC**的引脚必须配置为输入端口。实现类型：**Port_PinDirectionType** |
| 多重性 | 1 |
| 类型 | EcucEnumerationParamDef |
| 范围 | **PORT_PIN_IN**：端口引脚方向设置为输入；**PORT_PIN_OUT**：端口引脚方向设置为输出 |
| Post-Build 变体值 | true |
| 预编译时间 | X（VARIANT-PRE-COMPILE） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 X（VARIANT-POST-BUILD） |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00126]

| 参数名称 | PortPinDirectionChangeable |
|---|---|
| 父容器 | PortPin |
| 描述 | 指示端口引脚方向是否可在运行时更改的参数。**true**：端口引脚方向可更改启用。**false**：端口引脚方向可更改禁用。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | – |
| Post-Build 变体值 | true |
| 预编译时间 | X（VARIANT-PRE-COMPILE） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 X（VARIANT-POST-BUILD） |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00127]

| 参数名称 | PortPinId |
|---|---|
| 父容器 | PortPin |
| 描述 | 端口引脚的引脚**ID**。此值将分配给从端口引脚容器短名称派生的符号名称。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为此参数生成符号名称） |
| 范围 | 1 .. 65535 |
| 默认值 | – |
| Post-Build 变体值 | false |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 – |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00128]

| 参数名称 | PortPinInitialMode |
|---|---|
| 父容器 | PortPin |
| 描述 | 与**Port_Init()**函数一起使用的模式列表中的端口引脚模式。 |
| 多重性 | 1 |
| 类型 | EcucEnumerationParamDef |
| 范围 | **PORT_PIN_MODE_ADC**：端口引脚由**ADC**使用；**PORT_PIN_MODE_CAN**：端口引脚用于**CAN**；**PORT_PIN_MODE_DIO**：端口引脚配置为**DIO**。应在**DIO**驱动程序的控制下使用；**PORT_PIN_MODE_DIO_GPT**：端口引脚配置为**DIO**。应在通用定时器驱动程序的控制下使用；**PORT_PIN_MODE_DIO_WDG**：端口引脚配置为**DIO**。应在看门狗驱动程序的控制下使用；**PORT_PIN_MODE_FLEXRAY**：端口引脚用于**FlexRay**；**PORT_PIN_MODE_ICU**：端口引脚由**ICU**使用；**PORT_PIN_MODE_LIN**：端口引脚用于**LIN**；**PORT_PIN_MODE_MEM**：端口引脚在存储器驱动程序的控制下用于外部存储器；**PORT_PIN_MODE_PWM**：端口引脚由**PWM**使用；**PORT_PIN_MODE_SPI**：端口引脚由**SPI**使用 |
| Post-Build 变体值 | true |
| 预编译时间 | X（VARIANT-PRE-COMPILE） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 X（VARIANT-POST-BUILD） |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00129]

| 参数名称 | PortPinLevelValue |
|---|---|
| 父容器 | PortPin |
| 描述 | 端口引脚列表中的端口引脚电平值。 |
| 多重性 | 1 |
| 类型 | EcucEnumerationParamDef |
| 范围 | **PORT_PIN_LEVEL_HIGH**：端口引脚电平为高；**PORT_PIN_LEVEL_LOW**：端口引脚电平为低 |
| Post-Build 变体值 | true |
| 预编译时间 | X（VARIANT-PRE-COMPILE） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 X（VARIANT-POST-BUILD） |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00130]

| 参数名称 | PortPinMode |
|---|---|
| 父容器 | PortPin |
| 描述 | 模式列表中的端口引脚模式。注意，默认允许多于一个模式。这样可以例如将**DIO**与另一种模式（如**ICU**）组合。 |
| 多重性 | 1..* |
| 类型 | EcucEnumerationParamDef |
| 范围 | **PORT_PIN_MODE_ADC**：端口引脚由**ADC**使用；**PORT_PIN_MODE_CAN**：端口引脚用于**CAN**；**PORT_PIN_MODE_DIO**：端口引脚配置为**DIO**。应在**DIO**驱动程序的控制下使用；**PORT_PIN_MODE_DIO_GPT**：端口引脚配置为**DIO**。应在通用定时器驱动程序的控制下使用；**PORT_PIN_MODE_DIO_WDG**：端口引脚配置为**DIO**。应在看门狗驱动程序的控制下使用；**PORT_PIN_MODE_FLEXRAY**：端口引脚用于**FlexRay**；**PORT_PIN_MODE_ICU**：端口引脚由**ICU**使用；**PORT_PIN_MODE_LIN**：端口引脚用于**LIN**；**PORT_PIN_MODE_MEM**：端口引脚在存储器驱动程序的控制下用于外部存储器；**PORT_PIN_MODE_PWM**：端口引脚由**PWM**使用；**PORT_PIN_MODE_SPI**：端口引脚由**SPI**使用 |
| Post-Build 变体多重性 | true |
| Post-Build 变体值 | true |
| 预编译时间 | X（VARIANT-PRE-COMPILE） |
| 链接时间 | – |
| 多重性配置类 | Post-build 时间 X（VARIANT-POST-BUILD） |
| 预编译时间 | X（VARIANT-PRE-COMPILE） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 X（VARIANT-POST-BUILD） |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00134]

| 参数名称 | PortPinModeChangeable |
|---|---|
| 父容器 | PortPin |
| 描述 | 指示端口引脚模式是否可在运行时更改的参数。**True**：允许端口引脚模式更改。**False**：不允许端口引脚模式更改。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | – |
| Post-Build 变体值 | true |
| 预编译时间 | X（VARIANT-PRE-COMPILE） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 X（VARIANT-POST-BUILD） |
| 范围/依赖 | scope: local |

**SWS 条目** [ECUC_Port_00137]

| 参数名称 | PortPinEcucPartitionRef |
|---|---|
| 父容器 | PortPin |
| 描述 | 将端口引脚映射到零个或多个**ECUC**分区。引用的**ECUC**分区是**Port**驱动程序所映射到的**ECUC**分区的子集。 |
| 多重性 | 0..* |
| 类型 | 对 EcucPartition 的引用 |
| Post-Build 变体多重性 | true |
| Post-Build 变体值 | true |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 多重性配置类 | Post-build 时间 – |
| 预编译时间 | X（所有变体） |
| 链接时间 | – |
| 值配置类 | Post-build 时间 – |
| 范围/依赖 | scope: ECU |

无包含的容器。

![Figure10-4](Figure10-4.png)

### 10.3. 约束

[SWS_Port_CONSTR_00233] **PortPinEcucPartitionRef**引用的**ECUC**分区应是**PortEcucPartitionRef**引用的**ECUC**分区的子集。

[SWS_Port_CONSTR_00234] 如果**PortEcucPartitionRef**引用一个或多个**ECUC**分区，**PortPinEcucPartitionRef**应具有大于零的多重性，并同样引用这些**ECUC**分区中的一个或多个。

### 10.4. 发布信息

详情请参阅[4]中第 10.3 章"Published Information"。

## A. 不适用的需求

[SWS_Port_NA_00227] 这些需求不适用于本规范。（涉及**SRS_BSW_00005**、**SRS_BSW_00006**、**SRS_BSW_00007**、**SRS_BSW_00010**、**SRS_BSW_00160**、**SRS_BSW_00161**、**SRS_BSW_00162**、**SRS_BSW_00164**、**SRS_BSW_00167**、**SRS_BSW_00168**、**SRS_BSW_00170**、**SRS_BSW_00172**、**SRS_BSW_00307**、**SRS_BSW_00308**、**SRS_BSW_00309**、**SRS_BSW_00321**、**SRS_BSW_00325**、**SRS_BSW_00328**、**SRS_BSW_00330**、**SRS_BSW_00331**、**SRS_BSW_00333**、**SRS_BSW_00334**、**SRS_BSW_00335**、**SRS_BSW_00336**、**SRS_BSW_00341**、**SRS_BSW_00342**、**SRS_BSW_00343**、**SRS_BSW_00344**、**SRS_BSW_00347**、**SRS_BSW_00357**、**SRS_BSW_00359**、**SRS_BSW_00360**、**SRS_SPAL_12463**、**SRS_SPAL_12462**、**SRS_SPAL_12265**、**SRS_SPAL_12092**、**SRS_SPAL_12078**、**SRS_SPAL_12077**、**SRS_SPAL_12067**、**SRS_SPAL_12064**、**SRS_SPAL_12129**、**SRS_SPAL_12075**、**SRS_SPAL_12063**、**SRS_SPAL_12169**、**SRS_SPAL_00157**、**SRS_SPAL_12069**、**SRS_SPAL_12068**、**SRS_SPAL_12267**、**SRS_SPAL_12056**、**SRS_BSW_00440**、**SRS_BSW_00439**、**SRS_BSW_00437**、**SRS_BSW_00433**、**SRS_BSW_00432**、**SRS_BSW_00429**、**SRS_BSW_00428**、**SRS_BSW_00427**、**SRS_BSW_00426**、**SRS_BSW_00425**、**SRS_BSW_00424**、**SRS_BSW_00423**、**SRS_BSW_00419**、**SRS_BSW_00417**、**SRS_BSW_00416**、**SRS_BSW_00413**、**SRS_BSW_00398**、**SRS_BSW_00395**、**SRS_BSW_00378**、**SRS_BSW_00377**、**SRS_BSW_00375**、**SRS_BSW_00373**）

## B. AUTOSAR 可追踪条目的变更历史

### B.1. 本文档根据 AUTOSAR 发布 R23-11 的可追踪条目历史

#### B.1.1. R23-11 中新增的规范条目

无。

#### B.1.2. R23-11 中变更的规范条目

| 编号 | 标题 |
|---|---|
| [SWS_Port_00129] | Definition of imported datatypes of module Port |
| [SWS_Port_00146] | Definition of optional interfaces in module Port |
| [SWS_Port_00228] | Definition of datatype Port_ConfigType |
| [SWS_Port_00229] | Definition of datatype Port_PinType |
| [SWS_Port_00231] | Definition of datatype Port_PinModeType |
| [SWS_Port_NA_00227] | |

#### B.1.3. R23-11 中删除的规范条目

无。

#### B.1.4. R23-11 中新增的约束

无。

#### B.1.5. R23-11 中变更的约束

无。

#### B.1.6. R23-11 中删除的约束

无。
