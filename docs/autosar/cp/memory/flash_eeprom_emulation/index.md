---
title: "AUTOSAR FEE（闪存EEPROM仿真）"
spec: AUTOSAR_CP_SWS_FlashEEPROMEmulation
release: R23-11
---

## 1. 简介和功能概述

本文档描述了闪存EEPROM仿真（**Flash EEPROM Emulation**）模块的功能、**API**和配置。

![Figure1_1](Figure1_1.png)

**FEE**模块应从设备特定的寻址方案和分段中抽象出来，并为上层提供虚拟寻址方案和分段（**virtual addressing scheme and segmentation**）以及"虚拟"的无限数量的擦除周期。

## 2. 缩略语

以下术语表包含了与**Fee**模块相关的、未包含在[1, AUTOSAR术语表](#ref-1)中的缩略语和缩写。

**EA**
> EEPROM抽象（**EEPROM Abstraction**）

**Address Area**
> 逻辑地址空间中的连续内存区域，通常将多个物理存储器扇区组合成一个逻辑地址区域。

**EEPROM**
> 电可擦除可编程ROM（**Electrically Erasable and Programmable ROM**，只读存储器（**Read Only Memory**））。

**FEE**
> 闪存EEPROM仿真（**Flash EEPROM Emulation**）。

**LSB**
> 最低有效位/字节（**Least significant bit / byte**，取决于上下文；此处指"位"）。

**Mem**
> 内存驱动程序（**Memory Driver**）。

**MemAcc**
> 内存访问（**Memory Access**）。

**MemIf**
> 内存抽象接口（**Memory Abstraction Interface**）。

**MSB**
> 最高有效位/字节（**Most significant bit / byte**，取决于上下文；此处指"位"）。

**NvM**
> NVRAM管理器（**NVRAM Manager**）。

**NVRAM**
> 非易失性RAM（**Non-volatile RAM**，随机存取存储器（**Random Access Memory**））。

**NVRAM block**
> NVRAM管理器所见的管理单元。

**(Logical) block**
> 模块用户看到的最小可写/可擦除单元。由一个或多个虚拟页面（**Virtual page**）组成。

**Virtual page**
> 虚拟页面可能由一个或多个物理页面组成，以便于处理逻辑块和地址计算。

**Internal residue**
> 如果配置的块大小不是虚拟页面大小的整数倍，则最后一个虚拟页面末尾的未使用空间（参见图7.1）。

**Virtual address**
> 由16位块序号和逻辑块内的16位偏移量组成的地址。

**Physical address**
> 用于访问逻辑块的、设备特定格式（取决于底层EEPROM驱动程序和设备）的地址信息。

**Dataset**
> NVRAM管理器的一个概念：用户可寻址的相同大小的块数组。例如，可用于为具有其他方面完全相同的应用软件（例如车门模块）的**ECU**提供**CAN**驱动程序的不同配置设置（**CAN** ID、滤波器设置等）。

**Redundant copy**
> NVRAM管理器的一个概念：将相同的信息存储两次以提高数据存储的可靠性。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

<a id="ref-1"></a>[1] Glossary（术语表）
> AUTOSAR_FO_TR_Glossary

<a id="ref-2"></a>[2] General Specification of Basic Software Modules
> AUTOSAR_CP_SWS_BSWGeneral

<a id="ref-3"></a>[3] Specification of ECU State Manager
> AUTOSAR_CP_SWS_ECUStateManager

<a id="ref-4"></a>[4] Specification of Memory Abstraction Interface
> AUTOSAR_CP_SWS_MemoryAbstractionInterface

### 3.2. 相关规范

**AUTOSAR**提供了基础软件模块的通用规范[\[2, SWS BSW General\]](#ref-2)，它也适用于闪存EEPROM仿真。

因此，规范SWS BSW General需被视为闪存EEPROM仿真的附加和必需规范。

## 4. 约束和假设

### 4.1. 限制

无限制。

### 4.2. 汽车域的适用性

无限制。

## 5. 对其他模块的依赖

本模块依赖于底层闪存驱动程序的能力以及NVRAM管理器的配置。

## 6. 功能规格

### 6.1. 一般行为

#### 6.1.1. 寻址方案和分段

闪存EEPROM仿真（**FEE**）模块为上层提供**32**位虚拟线性地址空间和统一的分段方案。该虚拟**32**位地址应包括：

* **16**位块序号（**block number**）——理论上允许**65536**个逻辑块
* **16**位块偏移（**block offset**）——理论上每块为**64K**字节

**16**位块序号代表一种可配置的（虚拟）分页（**paging**）机制。该地址对齐的值可以从底层闪存驱动程序和设备的值导出。该虚拟分页应可通过参数**FeeVirtualPageSize**进行配置。

**FEE**模块的配置应使虚拟页面大小（在**FeeVirtualPageSize**中定义）为物理页面大小的整数倍，即不允许配置比实际物理页面大小更小的虚拟页面。

**注意：**

本规范需求允许计算逻辑块的物理起始地址，而不必借助查找表（**lookup table**）进行地址映射。

**示例：**

虚拟页面的大小配置为**8**个字节，因此地址对齐为**8**个字节。块序号为**1**的逻辑块放置在物理地址**x**处。那么块序号为**2**的逻辑块将放置在**x+8**处，块序号**3**将放置在**x+16**处。

每个已配置的逻辑块应占用所配置虚拟页面大小的整数倍（另见[第9章](#9-配置规范)配置参数**FeeVirtualPageSize**）。

**示例：**

通过相应地设置参数**FeeVirtualPageSize**，地址对齐/虚拟分页被配置为**8**个字节。逻辑块序号**1**配置为大小**32**个字节（参见图7.1）。该逻辑块将恰好使用**4**个虚拟页面。因此下一个逻辑块将获得块序号**5**，因为块序号**2**、**3**和**4**被第一个逻辑块"阻塞"。第二个块配置为大小**100**个字节，占用**13**个虚拟页面，最后一个页面的**4**个字节未使用。因此下一个可用的逻辑块序号将为**17**。

![Figure7_1](Figure7_1.png)

逻辑块不得相互重叠，也不得包含在彼此之内。

块序号**0x0000**和**0xFFFF**不得配置为逻辑块。

#### 6.1.2. 地址计算

依赖于**FEE**模块的实现和所使用的确切地址格式，**FEE**模块的函数应将**16**位块序号和**16**位地址偏移量组合起来，以推导出底层闪存驱动程序所需的物理闪存地址。

**注意：**

底层闪存驱动程序所需的确切地址格式，以及如何从给定的**16**位块序号和**16**位地址偏移量导出物理闪存地址的机制，取决于闪存设备和该模块的实现，因此不需要被标准化。

只有**16**位块序号中那些不表示特定数据集（**dataset**）或冗余副本（**redundant copy**）的位才应用于地址计算。

**注意：**

由于**NVRAM**管理器需要此类信息，因此可使用参数**NVM_DATASET_SELECTION_BITS**为**NVRAM**管理器配置用于编码的位数。

**示例：**

数据集信息配置为在**16**位块序号的四个**LSB**中进行编码（每个**NVRAM**块最多允许**16**个数据集，总共**4094**个**NVRAM**块）。实现者决定将**NVRAM**块的所有数据集直接相邻存储，并使用块的长度和指针来访问每个数据集。为了计算块的起始地址（第一个数据集的地址），她/他只使用**12**个**MSB**；为了访问特定的数据集，她/他在该起始地址上加上块大小乘以数据集索引（四个**LSB**）的乘积（图7.2）。

![Figure7_2](Figure7_2.png)

#### 6.1.3. 擦除周期的限制

**FEE**模块的配置应在配置参数**FeeNumberOfWriteCycles**中为每个逻辑块定义预期的擦除/写入周期数。

如果底层闪存设备或设备驱动程序不能提供至少所配置的每个物理存储单元的擦除/写入周期数，则**FEE**模块应提供分散写入访问的机制，使物理设备不会承受过大压力。这也适用于**FEE**模块内部使用的所有管理数据。

**示例：**

逻辑块序号**1**配置为预期的**500,000**个写入周期，而底层闪存设备和设备驱动程序仅规定**100,000**个擦除周期。在这种情况下，**FEE**模块必须提供（至少）五个独立的内存区域，并在内部交替访问这些区域，使每个物理内存位置的擦除次数不超过规定的**100,000**个周期。

#### 6.1.4. 处理"即时"数据

包含即时数据（**immediate data**）的块必须立即写入，即**FEE**模块必须确保它可以在无需擦除相应内存区域（例如通过使用预擦除内存）的情况下写入此类块，并且写请求不会被当前正在运行的模块内部管理操作所延迟。

**注意：**

在写入即时数据之前，**NVRAM**管理器应取消正在进行的较低优先级读取/擦除/写入或比较作业。**FEE**模块只需确保该写请求可以立即执行。

**注意：**

硬件上正在运行的操作（例如写入一个页面或擦除一个扇区）一旦启动通常无法中止。因此，即使对于即时数据，也必须接受最长硬件操作的最大时间作为延迟。

**示例：**

三个各**10**字节的块已配置为即时数据。**FEE**模块/配置工具保留这**30**个字节（如需要，加上每个块/页面的实现特定开销）仅供该即时数据使用。也就是说，该内存区域不得用于存储其他数据块。

现在，**NVRAM**管理器已请求**FEE**模块写入一个**100**字节的数据块。在该块写入期间，出现了一个（或多个）即时数据块需要写入的情况。因此**NVRAM**管理器取消正在进行的写请求，随后发出针对（第一个）包含即时数据的块的写请求。正在进行的写请求的取消由**FEE**模块同步执行，底层闪存驱动程序（即针对即时数据的写请求）可以立即启动，无需任何进一步延迟。然而，在即时数据的首个字节可以被写入之前，**FEE**模块或更确切地说底层闪存驱动程序必须等待来自前一个写请求的正在进行的硬件访问结束（例如写入页面、擦除扇区、通过**SPI**传输等）。

#### 6.1.5. 管理块正确性信息

**FEE**模块应为每个块管理该块从**FEE**模块的角度来看是否正确（即"未损坏"（**not corrupted**））的信息。该信息应仅涉及块的内部处理，而不涉及块的内容。

当块写入操作开始时，**FEE**模块应将相应的块标记为"损坏"（**corrupted**）<sup>1</sup>。

在块写入操作成功结束后，该块应（再次）被标记为"未损坏"。

**注意：**

此内部管理信息不应与块的有效性信息相混淆，后者可通过使用[**Fee_InvalidateBlock**](#737-fee_invalidateblock)服务来操作，即**FEE**应能够区分损坏的块和被上层故意标识为无效的块。

> 1 如果有其他手段可以检测逻辑块的一致性，这不一定意味着对物理设备进行写操作。

#### 6.1.6. 缓冲区对齐

**Fee**应将内部缓冲区对齐到**FeeBufferAlignmentValue**的值。

**Fee**应将读取请求对齐到**FeeMinimumReadPageSize**的值。

### 6.2. 错误分类

文档[\[2\]](#ref-2)"基础软件模块通用规范"（**General Specification of Basic Software Modules**）的"错误处理"（**Error Handling**）章节详细描述了基础软件的错误处理。其中，它构成了一个由五种错误类型组成的分类方案，这些错误类型可能发生在**BSW**模块中。

在此基础上，以下各小节按相应的类别规定了特定的错误。

#### 6.2.1. 开发错误

**Fee**模块中开发错误的定义：

| 错误类型 | 相关错误代码 | 错误值 |
|---|---|---|
| 模块未初始化时调用了**API**服务 | FEE_E_UNINIT | 0x01 |
| 调用**API**服务时给定的块序号无效 | FEE_E_INVALID_BLOCK_NO | 0x02 |
| 调用**API**服务时给定的块偏移无效 | FEE_E_INVALID_BLOCK_OFS | 0x03 |
| 调用**API**服务时给定的数据指针无效 | FEE_E_PARAM_POINTER | 0x04 |
| 调用**API**服务时给定的长度信息无效 | FEE_E_INVALID_BLOCK_LEN | 0x05 |

#### 6.2.2. 运行时错误

**Fee**模块中运行时错误的定义：

| 错误类型 | 相关错误代码 | 错误值 |
|---|---|---|
| 模块正忙于处理用户请求时调用了**API**服务 | FEE_E_BUSY | 0x06 |
| 在没有挂起作业时调用了[**Fee_Cancel**](#734-fee_cancel) | FEE_E_INVALID_CANCEL | 0x08 |

#### 6.2.3. 瞬态故障

没有瞬态故障。

#### 6.2.4. 生产错误

没有生产错误。

#### 6.2.5. 扩展生产错误

没有扩展生产错误。

## 7. API规范

### 7.1. 导入的类型

**Fee**模块导入的数据类型的定义：

| 模块 | 头文件 | 导入的类型 |
|---|---|---|
| MemAcc | MemAcc_GeneralTypes.h | MemAcc_AddressAreaIdType |
| MemAcc | MemAcc_GeneralTypes.h | MemAcc_AddressType |
| MemAcc | MemAcc_GeneralTypes.h | MemAcc_DataType |
| MemAcc | MemAcc_GeneralTypes.h | MemAcc_JobResultType |
| MemAcc | MemAcc_GeneralTypes.h | MemAcc_LengthType |
| MemIf | MemIf.h | MemIf_JobResultType |
| MemIf | MemIf.h | MemIf_StatusType |
| Std | Std_Types.h | Std_ReturnType |
| Std | Std_Types.h | Std_VersionInfoType |

上表所列的类型不得针对特定的**FEE**模块或硬件平台进行更改或扩展。

### 7.2. 类型定义

#### 7.2.1. Fee_ConfigType

结构类型。元素为实现特定。**Fee**模块的配置数据结构。可通过**Fee.h**获得。

### 7.3. 函数定义

#### 7.3.1. Fee_Init

**说明**: 服务 ID 0x00。初始化**FEE**模块的服务。可通过**Fee.h**获得。本服务为异步调用，不可重入。参数 ConfigPtr（in）：指向所选配置集的指针。参数（inout）：无。参数（out）：无。返回值：无。

```C
void Fee_Init ( const Fee_ConfigType* ConfigPtr )
```

如果初始化在**Fee_Init**内完成，则一旦初始化成功完成，函数**Fee_Init**应将模块状态从MEMIF_UNINIT设置为MEMIF_IDLE。

**注意：**

**FEE**模块的环境不得在**FEE**模块正在运行操作期间调用函数**Fee_Init**。

#### 7.3.2. Fee_Read

**说明**: 服务 ID 0x02。启动读取作业的服务。可通过**Fee.h**获得。本服务为异步调用，不可重入。参数 BlockNumber（in）：逻辑块的序号，也表示该块在闪存中的起始地址。参数 BlockOffset（in）：块内的读取地址偏移。参数 Length（in）：要读取的字节数。参数（inout）：无。参数（out）DataBufferPtr：指向数据缓冲区的指针。返回值：**Std_ReturnType**，**E_OK**：请求的作业已被模块接受；**E_NOT_OK**：请求的作业未被模块接受。

```C
Std_ReturnType Fee_Read (
    uint16 BlockNumber,
    uint16 BlockOffset,
    uint8* DataBufferPtr,
    uint16 Length )
```

函数**Fee_Read**应取块起始地址和偏移量，并计算出相应的内存读取地址。

**注意：**

地址偏移量和长度参数可以取给定类型范围内的任何值。这允许从逻辑块内的任意起始地址读取任意数量的字节。

如果当前模块状态为MEMIF_IDLE或当前模块状态为MEMIF_BUSY_INTERNAL，则函数**Fee_Read**应接受读取请求，将给定/计算出的参数复制到模块内部变量中，启动读取作业，将**FEE**模块状态设置为MEMIF_BUSY，将作业结果设置为MEMIF_JOB_PENDING，并以**E_OK**返回。

如果当前模块状态为MEMIF_UNINIT或MEMIF_BUSY，则函数**Fee_Read**应拒绝该作业请求并以**E_NOT_OK**返回。

**FEE**模块应在**FEE**模块的主函数中异步执行读取操作。

如果**Fee**模块的开发错误检测已启用：函数**Fee_Read**应检查模块状态是否为MEMIF_UNINIT。如果是这种情况，函数**Fee_Read**应引发开发错误[FEE_E_UNINIT](#621-开发错误)。

函数**Fee_Read**应检查模块状态是否为MEMIF_BUSY。如果是这种情况，函数**Fee_Read**应拒绝读取请求，引发运行时错误[FEE_E_BUSY](#622-运行时错误)并以**E_NOT_OK**返回。

如果**Fee**模块的开发错误检测已启用：函数**Fee_Read**应检查给定的块序号是否有效（即该块已被配置）。如果不是这种情况，函数**Fee_Read**应引发开发错误[FEE_E_INVALID_BLOCK_NO](#621-开发错误)。

如果**Fee**模块的开发错误检测已启用：函数**Fee_Read**应检查给定的块偏移量是否有效（即小于为该块配置的块长度）。如果不是这种情况，函数**Fee_Read**应引发开发错误[FEE_E_INVALID_BLOCK_OFS](#621-开发错误)。

如果**Fee**模块的开发错误检测已启用：函数**Fee_Read**应检查给定的数据指针是否有效（即不为**NULL**）。如果不是这种情况，函数**Fee_Read**应引发开发错误[FEE_E_PARAM_POINTER](#621-开发错误)。

如果**Fee**模块的开发错误检测已启用：函数**Fee_Read**应检查给定的长度信息是否有效，即请求的长度信息加上块偏移量不超过块的结束地址（块起始地址加上所配置的块长度）。如果不是这种情况，函数**Fee_Read**应引发开发错误[FEE_E_INVALID_BLOCK_LEN](#621-开发错误)。

如果读取请求被函数**Fee_Read**拒绝，即[FEE_E_UNINIT](#621-开发错误)、[FEE_E_BUSY](#622-运行时错误)、[FEE_E_INVALID_BLOCK_NO](#621-开发错误)、[FEE_E_INVALID_BLOCK_OFS](#621-开发错误)、[FEE_E_PARAM_POINTER](#621-开发错误)或[FEE_E_INVALID_BLOCK_LEN](#621-开发错误)所定义的开发/运行时错误适用的情况，函数**Fee_Read**不得改变当前的模块状态或作业结果。

函数**Fee_Read**应调用函数MemAcc_BlankCheck来提前确定给定的内存区域是否可以在不遇到例如**ECC**错误的情况下被读取，避免读取已擦除但未编程的闪存单元。

#### 7.3.3. Fee_Write

**说明**: 服务 ID 0x03。启动写入作业的服务。可通过**Fee.h**获得。本服务为异步调用，不可重入。参数 BlockNumber（in）：逻辑块的序号，也表示该块在闪存中的起始地址。参数 DataBufferPtr（in）：指向数据缓冲区的指针。参数（inout）：无。参数（out）：无。返回值：**Std_ReturnType**，**E_OK**：请求的作业已被模块接受；**E_NOT_OK**：请求的作业未被模块接受。

```C
Std_ReturnType Fee_Write (
    uint16 BlockNumber,
    const uint8* DataBufferPtr )
```

函数**Fee_Write**应取块起始地址并计算出相应的内存写入地址。块地址偏移量应固定为零。

如果当前模块状态为MEMIF_IDLE或当前模块状态为MEMIF_BUSY_INTERNAL，则函数**Fee_Write**应接受写入请求，将给定/计算出的参数复制到模块内部变量中，启动写入作业，将**FEE**模块状态设置为MEMIF_BUSY，将作业结果设置为MEMIF_JOB_PENDING，并以**E_OK**返回。

如果当前模块状态为MEMIF_UNINIT或MEMIF_BUSY，则函数**Fee_Write**应拒绝该作业请求并以**E_NOT_OK**返回。

**FEE**模块应在**FEE**模块的主函数中异步执行写入操作。

如果**Fee**模块的开发错误检测已启用：函数**Fee_Write**应检查模块状态是否为MEMIF_UNINIT。如果是这种情况，函数**Fee_Write**应引发开发错误[FEE_E_UNINIT](#621-开发错误)。

函数**Fee_Write**应检查模块状态是否为MEMIF_BUSY。如果是这种情况，函数**Fee_Write**应拒绝写入请求，引发运行时错误[FEE_E_BUSY](#622-运行时错误)并以**E_NOT_OK**返回。

如果**Fee**模块的开发错误检测已启用：函数**Fee_Write**应检查给定的块序号是否有效（即该块已被配置）。如果不是这种情况，函数**Fee_Write**应引发开发错误[FEE_E_INVALID_BLOCK_NO](#621-开发错误)。

如果**Fee**模块的开发错误检测已启用：函数**Fee_Write**应检查给定的数据指针是否有效（即不为**NULL**）。如果不是这种情况，函数**Fee_Write**应引发开发错误[FEE_E_PARAM_POINTER](#621-开发错误)。

如果写入请求被函数**Fee_Write**拒绝，即[FEE_E_UNINIT](#621-开发错误)、[FEE_E_BUSY](#622-运行时错误)、[FEE_E_INVALID_BLOCK_NO](#621-开发错误)或[FEE_E_PARAM_POINTER](#621-开发错误)所定义的开发/运行时错误适用的情况，函数**Fee_Write**不得改变当前的模块状态或作业结果。

#### 7.3.4. Fee_Cancel

**说明**: 服务 ID 0x04。调用底层闪存驱动程序的取消函数的服务。可通过**Fee.h**获得。本服务为异步调用，不可重入。参数（in）：无。参数（inout）：无。参数（out）：无。返回值：无。

```C
void Fee_Cancel ( void )
```

如果**Fee**模块的开发错误检测已启用：函数**Fee_Cancel**应检查模块状态是否为MEMIF_UNINIT。如果是这种情况，函数**Fee_Cancel**应引发开发错误[FEE_E_UNINIT](#621-开发错误)。

如果当前模块状态为MEMIF_BUSY（即取消挂起作业的请求被函数**Fee_Cancel**接受），则函数**Fee_Cancel**应调用底层闪存驱动程序的取消函数。

如果当前模块状态为MEMIF_BUSY（即取消挂起作业的请求被函数**Fee_Cancel**接受），则函数**Fee_Cancel**应重置**FEE**模块的内部变量，使模块准备好接受来自上层的新作业请求，即它应将模块状态设置为MEMIF_IDLE。

如果当前模块状态不是MEMIF_BUSY（即取消挂起作业的请求被函数**Fee_Cancel**拒绝），则函数**Fee_Cancel**不得改变当前的模块状态或作业结果。

如果当前模块状态不是MEMIF_BUSY（即没有要取消的作业，因此取消挂起作业的请求被函数**Fee_Cancel**拒绝），则函数**Fee_Cancel**应引发运行时错误[FEE_E_INVALID_CANCEL](#622-运行时错误)。

#### 7.3.5. Fee_GetStatus

**说明**: 服务 ID 0x05。返回状态的服务。可通过**Fee.h**获得。本服务为同步调用，不可重入。参数（in）：无。参数（inout）：无。参数（out）：无。返回值：**MemIf_StatusType**，**MEMIF_UNINIT**：**FEE**模块尚未初始化；**MEMIF_IDLE**：**FEE**模块当前空闲；**MEMIF_BUSY**：**FEE**模块当前繁忙；**MEMIF_BUSY_INTERNAL**：**FEE**模块正忙于内部管理操作。

```C
MemIf_StatusType Fee_GetStatus ( void )
```

如果模块尚未（或还未）初始化，函数**Fee_GetStatus**应返回MEMIF_UNINIT。

如果模块既未在处理来自上层的请求，也未在执行内部管理操作，函数**Fee_GetStatus**应返回MEMIF_IDLE。

如果模块当前正在处理来自上层的请求，函数**Fee_GetStatus**应返回MEMIF_BUSY。

如果当前正在执行内部管理操作，函数**Fee_GetStatus**应返回MEMIF_BUSY_INTERNAL。

**注意：**

内部管理操作例如可以是对所用闪存的重组（垃圾回收）。这可能意味着底层设备驱动程序（至少暂时）繁忙。

#### 7.3.6. Fee_GetJobResult

**说明**: 服务 ID 0x06。查询上层软件下发的最后一个被接受的作业的结果的服务。可通过**Fee.h**获得。本服务为同步调用，不可重入。参数（in）：无。参数（inout）：无。参数（out）：无。返回值：**MemIf_JobResultType**，**MEMIF_JOB_OK**：最后一个作业已成功完成；**MEMIF_JOB_PENDING**：最后一个作业正在等待执行或正在执行中；**MEMIF_JOB_CANCELED**：最后一个作业已被取消（这意味着它已失败）；**MEMIF_JOB_FAILED**：最后一个作业未成功完成（它已失败）；**MEMIF_BLOCK_INCONSISTENT**：所请求的块不一致，它可能包含已损坏的数据；**MEMIF_BLOCK_INVALID**：所请求的块已被标识为无效，无法执行所请求的读取操作。

```C
MemIf_JobResultType Fee_GetJobResult ( void )
```

如果最后一个作业已成功完成，函数**Fee_GetJobResult**应返回MEMIF_JOB_OK。

如果所请求的作业仍在等待执行或正在执行中，函数**Fee_GetJobResult**应返回MEMIF_JOB_PENDING。

如果最后一个作业已被上层取消，函数**Fee_GetJobResult**应返回MEMIF_JOB_CANCELED。

如果最后一个作业已失败，函数**Fee_GetJobResult**应返回MEMIF_JOB_FAILED。

如果发现所请求的块不一致，函数**Fee_GetJobResult**应返回MEMIF_BLOCK_INCONSISTENT。

块不一致的管理在[第6.1.5章](#615-管理块正确性信息)中规定。

如果所请求的块已被上层标识为无效，函数**Fee_GetJobResult**应返回MEMIF_BLOCK_INVALID。

只有那些由上层直接请求的作业才应对函数**Fee_GetJobResult**返回的作业结果产生影响。即**FEE**模块自身在内部管理操作过程中发出的作业不应改变该作业结果。

如果**Fee**模块的开发错误检测已启用：函数**Fee_GetJobResult**应检查模块状态是否为MEMIF_UNINIT。如果是这种情况，函数**Fee_GetJobResult**应引发开发错误[FEE_E_UNINIT](#621-开发错误)。

#### 7.3.7. Fee_InvalidateBlock

**说明**: 服务 ID 0x07。使逻辑块无效的服务。可通过**Fee.h**获得。本服务为异步调用，不可重入。参数 BlockNumber（in）：逻辑块的序号，也表示该块在闪存中的起始地址。参数（inout）：无。参数（out）：无。返回值：**Std_ReturnType**，**E_OK**：请求的作业已被模块接受；**E_NOT_OK**：请求的作业未被模块接受。

```C
Std_ReturnType Fee_InvalidateBlock ( uint16 BlockNumber )
```

函数**Fee_InvalidateBlock**应取块序号并计算出相应的内存块地址。

函数**Fee_InvalidateBlock**应通过调用底层设备驱动程序的擦除函数和/或相应地更改某些模块内部管理信息，来使所请求的块BlockNumber无效。

**注意：**

所请求的块被无效化的确切方式取决于模块的实现，本规范不再进一步详述。内部管理信息必须存储在NV存储器中，因为它必须能抗复位。该信息是什么以及如何存储，本规范不再进一步详述。

如果**Fee**模块的开发错误检测已启用：函数**Fee_InvalidateBlock**应检查模块状态是否为MEMIF_UNINIT。如果是这种情况，函数**Fee_InvalidateBlock**应引发开发错误[FEE_E_UNINIT](#621-开发错误)。

函数**Fee_InvalidateBlock**应检查模块状态是否为MEMIF_BUSY。如果是这种情况，函数**Fee_InvalidateBlock**应拒绝该请求，引发运行时错误[FEE_E_BUSY](#622-运行时错误)并以**E_NOT_OK**返回。

函数**Fee_InvalidateBlock**应检查模块状态是否为MEMIF_IDLE或MEMIF_BUSY_INTERNAL。如果是这种情况，模块应接受无效化请求并向调用者返回**E_OK**。块无效化应在模块完成内部管理操作后，在模块的主函数中异步执行。

**FEE**模块应在**FEE**模块的主函数中异步执行块无效化请求。

如果**Fee**模块的开发错误检测已启用：函数**Fee_InvalidateBlock**应检查给定的块序号是否有效（即该块已被配置）。如果不是这种情况，函数**Fee_InvalidateBlock**应引发开发错误[FEE_E_INVALID_BLOCK_NO](#621-开发错误)。

如果无效化请求被函数**Fee_InvalidateBlock**拒绝，即[FEE_E_UNINIT](#621-开发错误)、[FEE_E_INVALID_BLOCK_NO](#621-开发错误)或[FEE_E_BUSY](#622-运行时错误)所定义的开发/运行时错误适用的情况，函数**Fee_InvalidateBlock**不得改变当前的模块状态或作业结果。

#### 7.3.8. Fee_GetVersionInfo

**说明**: 服务 ID 0x08。返回**FEE**模块版本信息的服务。可通过**Fee.h**获得。本服务为同步调用，可重入。参数（in）：无。参数（inout）：无。参数（out）VersionInfoPtr：指向标准版本信息结构的指针。返回值：无。

```C
void Fee_GetVersionInfo ( Std_VersionInfoType* VersionInfoPtr )
```

如果**Fee**模块的开发错误检测已启用：函数**Fee_GetVersionInfo**应检查给定的数据指针是否有效（即不为**NULL**）。如果不是这种情况，函数**Fee_GetVersionInfo**应引发开发错误[FEE_E_PARAM_POINTER](#621-开发错误)。

#### 7.3.9. Fee_EraseImmediateBlock

**说明**: 服务 ID 0x09。擦除逻辑块的服务。可通过**Fee.h**获得。本服务为异步调用，不可重入。参数 BlockNumber（in）：逻辑块的序号，也表示该块在闪存中的起始地址。参数（inout）：无。参数（out）：无。返回值：**Std_ReturnType**，**E_OK**：请求的作业已被模块接受；**E_NOT_OK**：请求的作业未被模块接受。

```C
Std_ReturnType Fee_EraseImmediateBlock ( uint16 BlockNumber )
```

**注意：**

例如，诊断或类似的系统服务应在必要时调用函数**Fee_EraseImmediateBlock**，为即时数据预擦除相应的区域。

函数**Fee_EraseImmediateBlock**应取块序号并计算出相应的内存块地址。

函数**Fee_EraseImmediateBlock**应确保**FEE**模块可以写入即时数据。这是否涉及物理擦除内存区域并因此调用底层驱动程序的擦除函数，取决于模块的实现。

如果**Fee**模块的开发错误检测已启用：函数**Fee_EraseImmediateBlock**应检查模块状态是否为MEMIF_UNINIT。如果是这种情况，函数**Fee_EraseImmediateBlock**应引发开发错误[FEE_E_UNINIT](#621-开发错误)。

函数**Fee_EraseImmediateBlock**应检查模块状态是否为MEMIF_BUSY。如果是这种情况，函数**Fee_EraseImmediateBlock**应拒绝擦除请求，引发运行时错误[FEE_E_BUSY](#622-运行时错误)并以**E_NOT_OK**返回。

如果**Fee**模块的开发错误检测已启用：函数**Fee_EraseImmediateBlock**应检查所寻址的逻辑块是否被配置为包含即时数据（**FeeImmediateData** == TRUE）。如果不是，函数**Fee_EraseImmediateBlock**应引发开发错误[FEE_E_INVALID_BLOCK_NO](#621-开发错误)。

如果**Fee**模块的开发错误检测已启用：函数**Fee_EraseImmediateBlock**应检查给定的块序号是否有效（即该块已被配置）。如果不是这种情况，函数**Fee_EraseImmediateBlock**应引发开发错误[FEE_E_INVALID_BLOCK_NO](#621-开发错误)。

如果擦除请求被函数**Fee_EraseImmediateBlock**拒绝，即[FEE_E_UNINIT](#621-开发错误)、[FEE_E_INVALID_BLOCK_NO](#621-开发错误)或[FEE_E_BUSY](#622-运行时错误)所定义的开发/运行时错误适用的情况，函数**Fee_EraseImmediateBlock**不得改变当前的模块状态或作业结果。

### 7.4. 回调通知

本章列出了**Fee**模块提供给下层模块的所有函数。

**注意：**

根据组成NV存储器栈的各模块的实现，**FEE**模块提供的回调例程可能会在中断级被调用。因此**FEE**模块的实现必须确保这些例程的运行时间足够短，即回调可能会向上传播穿过多个软件层。回调例程是否可在中断级允许/可行取决于项目特定的需求（反应时间）和限制（中断上下文中的运行时间）。因此，系统设计必须确保所涉及模块的配置满足这些要求。

#### 7.4.1. Fee_JobEndNotification

**说明**: 服务 ID 0x10。向本模块报告异步操作成功结束的服务。可通过**Fee.h**获得。本服务为同步调用，不可重入。参数（in）：无。参数（inout）：无。参数（out）：无。返回值：无。

```C
void Fee_JobEndNotification ( void )
```

底层闪存驱动程序应调用函数**Fee_JobEndNotification**以报告异步操作的成功结束。

函数**Fee_JobEndNotification**应执行任何必要的块管理操作，随后调用上层模块的作业结束通知例程（如果已配置）。

如果作业结果当前为MEMIF_JOB_PENDING，则函数**Fee_JobEndNotification**应将作业结果设置为MEMIF_JOB_OK，否则应保持作业结果不变。

函数**Fee_JobEndNotification**应执行任何必要的块管理和错误处理操作，随后调用上层模块的作业错误通知例程（如果已配置）。

**注意：**

函数**Fee_JobEndNotification**应可在中断级被调用。

### 7.5. 调度函数

这些函数由基础软件调度程序（**Basic Software Scheduler**）直接调用。以下函数应没有返回值且没有参数。所有函数均不可重入。

#### 7.5.1. Fee_MainFunction

**说明**: 服务 ID 0x12。处理所请求的读取/写入/擦除作业和内部管理操作的服务。可通过**SchM_Fee.h**获得。

```C
void Fee_MainFunction ( void )
```

如果模块初始化（在函数[**Fee_Init**](#731-fee_init)中启动）在模块的主函数中完成，则一旦模块初始化成功完成，函数**Fee_MainFunction**应将模块状态从MEMIF_UNINIT设置为MEMIF_IDLE。

函数**Fee_MainFunction**应异步处理上层请求的读取/写入/擦除/无效化作业和内部管理操作。

函数**Fee_MainFunction**应检查所请求读取的块是否已被上层模块标识为无效。如果是，函数**Fee_MainFunction**应将作业结果设置为MEMIF_BLOCK_INVALID，并调用上层模块的错误通知例程（如果已配置）。

函数**Fee_MainFunction**应在通知调用者之前检查正在被读取的逻辑块的一致性。如果检测到读取数据的不一致性，或者找不到所请求的块，函数**Fee_MainFunction**应将作业结果设置为MEMIF_BLOCK_INCONSISTENT，并调用上层模块的错误通知例程（如果已配置）。

**注意：**

在这种情况下，上层不得使用数据缓冲区的内容。

### 7.6. 期望接口

本章列出了需要从其他模块获得的所有接口。

#### 7.6.1. 强制接口

本章定义了实现模块核心功能所需的所有接口。

| API函数 | 头文件 | 描述 |
|---|---|---|
| Det_ReportRuntimeError | Det.h | 用于报告运行时错误的服务。如果已配置callout，则应调用该callout。 |
| MemAcc_Cancel | MemAcc.h | 触发对addressAreaId所引用的地址区域的挂起作业的取消操作。取消仅影响处于挂起状态的作业。对于任何其他状态，该请求将被忽略。 |
| MemAcc_Compare (draft) | MemAcc.h | 触发一个作业，将传入的数据与所提供地址区域的存储器内容进行比较。如果所有字节都匹配或检测到差异，该作业终止。此服务的结果可通过MemAcc_GetJobResult() **API**获取。如果比较操作确定不匹配，则结果代码为MEMACC_INCONSISTENT。标签：atp.Status=draft |
| MemAcc_Erase | MemAcc.h | 触发对给定区域的擦除作业。触发对由targetAddress和length定义的给定区域的擦除作业。此服务的结果可通过Mem_GetJobResult **API**获取。如果擦除操作成功，则作业结果为MEM_JOB_OK。如果擦除操作失败（例如由于硬件问题），则作业结果为MEM_JOB_FAILED。 |
| MemAcc_GetJobResult | MemAcc.h | 返回addressAreaId所引用的地址区域的合并作业结果。 |
| MemAcc_Read | MemAcc.h | 触发读取作业，将数据从源地址复制到所引用的目标数据缓冲区中。此服务的结果可通过MemAcc_GetJobResult **API**获取。如果读取操作成功，则作业结果为MEMACC_OK。如果读取操作失败，则作业结果为一般错误时的MEMACC_FAILED，或可纠正/不可纠正**ECC**错误时的MEMACC_ECC_CORRECTED/MEMACC_ECC_UNCORRECTED。 |
| MemAcc_Write | MemAcc.h | 触发写入作业，将传入的数据以给定的地址和长度存储到所提供的地址区域。此服务的结果可通过MemAcc_GetJobResult **API**获取。如果写入操作成功，则作业结果为MEMACC_OK。如果写入数据时出现问题，则结果为MEMACC_FAILED。 |

#### 7.6.2. 可选接口

本章定义了实现模块可选功能所需的所有接口。

| API函数 | 头文件 | 描述 |
|---|---|---|
| Det_ReportError | Det.h | 用于报告开发错误的服务。 |
| MemAcc_BlankCheck | MemAcc.h | 检查传入的地址空间是否为空白，即已擦除且可写。此服务的结果可通过MemAcc_GetJobResult **API**获取。如果由targetAddress和length定义的地址区域为空白，则结果为MEMACC_OK，否则结果为MEMACC_INCONSISTENT。 |

#### 7.6.3. 可配置接口

本章列出了目标函数可被配置的所有接口。目标函数通常是回调函数。此类接口的名称不是固定的，因为它们是可配置的。

**注意：**

根据组成NV存储器栈的各模块的实现，**FEE**模块调用的回调例程可能会在中断级被调用。因此，提供这些例程的模块的实现者必须确保它们的运行时间足够短，即回调可能会向上传播穿过多个软件层。回调例程是否可在中断级允许/可行取决于项目特定的需求（反应时间）和限制（中断上下文中的运行时间）。因此，系统设计必须确保所涉及模块的配置满足这些要求。

**FEE**模块应在异步操作成功结束并执行所有必要的内部管理操作后，调用配置参数**FeeNvmJobEndNotification**中定义的函数：

* 读取作业完成且成功
* 写入作业完成且成功且块被标记为有效
* 即时数据的擦除作业完成且成功（参见[第7.3.9章](#739-fee_eraseimmediateblock)）
* 内存块的无效化完成且成功

在配置参数**FeeNvmJobEndNotification**中定义的函数应可在中断级被调用。

**FEE**模块应在异步操作失败并执行所有必要的内部管理和错误处理操作后，调用配置参数**FeeNvmJobEndNotification**中定义的函数：

* 读取作业完成且失败（例如块无效或不一致）
* 写入作业完成且失败且块被标记为无效
* 即时数据的擦除作业完成且失败（参见[第7.3.9章](#739-fee_eraseimmediateblock)）
* 内存块的无效化完成且失败

在配置参数**FeeNvmJobEndNotification**中定义的函数应可在中断级被调用。

## 8. 时序图

**注意：**

对于供应商特定的库，以下时序图仅在显示与调用模块（**Ecu_State Manager**[\[3\]](#ref-3)和内存抽象接口[\[4\]](#ref-4)）的关系方面有效。从内存抽象模块到底层驱动程序的调用关系对于供应商特定的库不相关/不具约束力。

### 8.1. Fee_Init

下图显示了[**Fee_Init**](#731-fee_init)例程的调用顺序。它不同于本模块所有其他服务的调用顺序，因为它不是由**NVRAM**管理器调用的，也不是通过内存抽象接口调用的。

![Figure9_1](Figure9_1.png)

### 8.2. Fee_Write

下图示例性地显示了[**Fee_Write**](#733-fee_write)服务的调用顺序。该时序图也适用于本模块的其他异步服务。

![Figure9_2](Figure9_2.png)

### 8.3. Fee_Cancel

下图显示了已取消的[**Fee_Write**](#733-fee_write)服务以及随后的新[**Fee_Write**](#733-fee_write)请求的调用顺序示例。该时序图表明，[**Fee_Cancel**](#734-fee_cancel)相对于底层硬件是异步的，而其本身是同步的。

![Figure9_3](Figure9_3.png)

![Figure9_4](Figure9_4.png)

## 9. 配置规范

### 9.1. 容器与配置参数

以下各节汇总了所有配置参数。各参数的详细含义在[第6章](#6-功能规格)和[第7章](#7-api规范)中描述。

#### 9.1.1. Fee

| SWS 条目 | [ECUC_Fee_00154] |
|---|---|
| 模块名称 | Fee |
| 描述 | **Fee**（闪存EEPROM仿真）模块的配置。 |
| Post-Build 变体支持 | false |
| 支持的配置变体 | VARIANT-PRE-COMPILE |

| 容器名称 | 多重性 | 作用域/依赖 |
|---|---|---|
| FeeBlockConfiguration | 1..* | 闪存EEPROM仿真模块的块特定参数的配置。 |
| FeeGeneral | 1 | 通用参数的容器。这些参数不特定于某个块。 |
| FeePublishedInformation | 1 | 公共发布信息（**Common PublishedInformation**）容器未涵盖的其他发布参数。注意：这些参数没有任何配置类设置，因为它们是发布信息。 |

![Figure10_1](Figure10_1.png)

#### 9.1.2. FeeGeneral

| SWS 条目 | [ECUC_Fee_00039] |
|---|---|
| 容器名称 | FeeGeneral |
| 父容器 | Fee |
| 描述 | 通用参数的容器。这些参数不特定于某个块。 |
| 配置参数 | 见下方参数表 |

| SWS 条目 | [ECUC_Fee_00111] |
|---|---|
| 参数名称 | FeeDevErrorDetect |
| 父容器 | FeeGeneral |
| 描述 | 打开或关闭开发错误检测和通知。true：启用检测和通知。false：禁用检测和通知。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00153] |
|---|---|
| 参数名称 | FeeMainFunctionPeriod |
| 父容器 | FeeGeneral |
| 描述 | 相邻两次主函数调用之间的周期，单位为秒。 |
| 多重性 | 1 |
| 类型 | EcucFloatParamDef |
| 范围 | ]0 .. INF[ |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_Fee_00156] |
|---|---|
| 参数名称 | FeeMinimumReadPageSize |
| 父容器 | FeeGeneral |
| 描述 | 最小页面大小。最小页面大小将是该最小页面大小的倍数。**Fee**应将读取请求对齐到该大小。标签：atp.Status=draft |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 范围 | 0 .. 65535 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00112] |
|---|---|
| 参数名称 | FeeNvmJobEndNotification |
| 父容器 | FeeGeneral |
| 描述 | 映射到上层模块（**NvM_JobEndNotification**）提供的作业结束通知例程。 |
| 多重性 | 0..1 |
| 类型 | EcucFunctionNameDef |
| 默认值 | - |
| 正则表达式 | - |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：x；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：x；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00113] |
|---|---|
| 参数名称 | FeeNvmJobErrorNotification |
| 父容器 | FeeGeneral |
| 描述 | 映射到上层模块（**NvM_JobErrorNotification**）提供的作业错误通知例程。 |
| 多重性 | 0..1 |
| 类型 | EcucFunctionNameDef |
| 默认值 | - |
| 正则表达式 | - |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：x；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：x；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00114] |
|---|---|
| 参数名称 | FeePollingMode |
| 父容器 | FeeGeneral |
| 描述 | 为本模块启用和禁用轮询模式的预处理器开关。true：启用轮询模式，禁用（提供给MemAcc模块的）回调函数。false：禁用轮询模式，启用（提供给MemAcc模块的）回调函数。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00115] |
|---|---|
| 参数名称 | FeeVersionInfoApi |
| 父容器 | FeeGeneral |
| 描述 | 启用/禁用读取模块版本信息的**API**的预处理器开关。true：版本信息**API**已启用。false：版本信息**API**已禁用。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | false |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00116] |
|---|---|
| 参数名称 | FeeVirtualPageSize |
| 父容器 | FeeGeneral |
| 描述 | 逻辑块应对齐到的字节大小。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 范围 | 0 .. 65535 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00157] |
|---|---|
| 参数名称 | FeeBufferAlignmentValue |
| 父容器 | FeeGeneral |
| 描述 | 该参数决定**Fee**缓冲区的起始地址所需的对齐方式。该值应继承自**MemAccBufferAlignmentValue**。 |
| 多重性 | 1 |
| 类型 | 对MemAccAddressAreaConfiguration的符号名引用 |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

无包含容器。

#### 9.1.3. FeeBlockConfiguration

| SWS 条目 | [ECUC_Fee_00040] |
|---|---|
| 容器名称 | FeeBlockConfiguration |
| 父容器 | Fee |
| 描述 | 闪存EEPROM仿真模块的块特定参数的配置。 |
| 配置参数 | 见下方参数表 |

| SWS 条目 | [ECUC_Fee_00150] |
|---|---|
| 参数名称 | FeeBlockNumber |
| 父容器 | FeeBlockConfiguration |
| 描述 | 块标识符（句柄）。块序号不得使用**0x0000**和**0xFFFF**（参见[第6.1.1章](#611-寻址方案和分段)）。范围：min = 2^NVM_DATASET_SELECTION_BITS，max = 0xFFFF - 2^NVM_DATASET_SELECTION_BITS。注意：根据为数据集选择预留的位数，还应省略其他几个块序号以便于实现。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef（为该参数生成符号名） |
| 范围 | 1 .. 65534 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_Fee_00148] |
|---|---|
| 参数名称 | FeeBlockSize |
| 父容器 | FeeBlockConfiguration |
| 描述 | 逻辑块的大小，单位为字节。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 范围 | 1 .. 65535 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_Fee_00151] |
|---|---|
| 参数名称 | FeeImmediateData |
| 父容器 | FeeBlockConfiguration |
| 描述 | 高优先级数据的标记。true：块包含即时数据。false：块不包含即时数据。 |
| 多重性 | 1 |
| 类型 | EcucBooleanParamDef |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: ECU |

| SWS 条目 | [ECUC_Fee_00110] |
|---|---|
| 参数名称 | FeeNumberOfWriteCycles |
| 父容器 | FeeBlockConfiguration |
| 描述 | 该块所需的写入周期数。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 范围 | 0 .. 4294967295 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Pre-compile time：x（All Variants）；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00155] |
|---|---|
| 参数名称 | FeeMemAccAddressArea |
| 父容器 | FeeBlockConfiguration |
| 描述 | 对**MemAccAddressAreaConfiguration**的引用。标签：atp.Status=draft |
| 多重性 | 0..1 |
| 类型 | 对MemAccAddressAreaConfiguration的符号名引用 |
| Post-Build 变体多重性 | false |
| Post-Build 变体值 | false |
| 多重性配置类 | Pre-compile time：x；Link time：-；Post-build time：- |
| 值配置类 | Pre-compile time：x；Link time：-；Post-build time：- |
| 作用域/依赖 | scope: local |

无包含容器。

![Figure10_2](Figure10_2.png)

### 9.2. 发布信息

#### 9.2.1. FeePublishedInformation

| SWS 条目 | [ECUC_Fee_00043] |
|---|---|
| 容器名称 | FeePublishedInformation |
| 父容器 | Fee |
| 描述 | 公共发布信息（**CommonPublishedInformation**）容器未涵盖的其他发布参数。注意：这些参数没有任何配置类设置，因为它们是发布信息。 |
| 配置参数 | 见下方参数表 |

| SWS 条目 | [ECUC_Fee_00117] |
|---|---|
| 参数名称 | FeeBlockOverhead |
| 父容器 | FeePublishedInformation |
| 描述 | 每个逻辑块的管理开销，单位为字节。注意：如果管理开销取决于块大小，则必须提供公式，使配置工具能够正确计算开销。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 范围 | 0 .. 65535 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Published Information：x（All Variants） |
| 作用域/依赖 | scope: local |

| SWS 条目 | [ECUC_Fee_00118] |
|---|---|
| 参数名称 | FeePageOverhead |
| 父容器 | FeePublishedInformation |
| 描述 | 每个页面的管理开销，单位为字节。注意：如果管理开销取决于块大小或块位置，则必须提供公式，使配置工具能够正确计算管理开销。 |
| 多重性 | 1 |
| 类型 | EcucIntegerParamDef |
| 范围 | 0 .. 65535 |
| 默认值 | - |
| Post-Build 变体值 | false |
| 值配置类 | Published Information：x（All Variants） |
| 作用域/依赖 | scope: local |

无包含容器。

<section id="wechat">

<h4>微信扫一扫，获取更多及时资讯</h4>

<img src="wechat.png" alt="微信扫一扫"/>

</section>
