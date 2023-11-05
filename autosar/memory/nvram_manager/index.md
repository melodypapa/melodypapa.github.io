<section id="title">AUTOSAR NVM（非易失性存储管理器）</section>

# 1. 简介和功能概述

本文档介绍了 **AUTOSAR** 基础软件模块 **NVRAM Manager** (**NvM**) 的功能、API以及配置。

**NvM** 模块需根据汽车环境中的个性化需求，提供确保 **NV** (**non volatile**) 即非易失性数据进行数据存储和维护的服务。**NvM** 模块应能够管理 **EEPROM** 和 **FLASH EEPROM** 仿真设备的 **NV** 数据。

**NvM** 模块需为NV数据的管理和维护，包括：初始化、读、写、控制，提供所需的同步或者异步服务。

不同块之间的关系可以如下图所示：

![Figure1_1](Figure1_1.png)

![Figure1_2](Figure1_2.png)

# 2. 缩略语

**基本存储对象（Basic Storage Object）**
> “基本存储对象” 是 **NVRAM** 块的最小实体。多个基本存储对象可用于构建 **NVRAM** 块。“基本存储对象”可以驻留在不同的内存位置，包括：**RAM**、**ROM**、NV内存（**NV memory**）中。

**NVRAM块（NVRAM Block）**
> “NVRAM块” 是管理和存储 NV 数据块所需的整个结构。

**NV数据（NV data）**
> “NV数据” 是指要存储在非易失性存储器中的数据。

**块管理类型（Block Management Type）**
> NVRAM块的类型。它取决于 NVRAM 块在不同强制/可选基本存储对象块中的（可配置）单独组合以及此 NVRAM 块的后续处理。

**RAM块（RAM Block）**
> “RAM块” 是 “基本存储对象”。它代表驻留在 **RAM** 中的 “NVRAM块” 的一部分。

**ROM块（ROM Block）** 
> “ROM块”是“基本存储对象”。它代表驻留在 **ROM** 中的 “NVRAM块” 的一部分。“**ROM块**”是“**NVRAM块**”的可选部分。

**NV块（NV Block）**
> “NV块”是“基本存储对象”。它代表驻留在 **NV内存** 中的 “NVRAM块” 的一部分。“**NV块**”是“**NVRAM块**”的强制性部分。

**NV块标头（NV Block Header）**
> 如果启用 “**静态块ID**” 机制，则**NV块**中包含的附加信息。

**管理块（Administrative Block）** 
> “管理块”是“基本存储对象”。它驻留在 **RAM** 中。“**管理块**”是“**NVRAM块**”的强制部分。

**默认错误跟踪器（DET）** 
> 默认错误跟踪器（**Default Error Tracer**）报告开发错误的模块。

**诊断事件管理器（DEM）** 
> 诊断事件管理器（**Diagnostic Event Manager**） 接受报告的相关错误的模块 

**非易失性（NV）** 
> 非易失性（**Non volatile**）

**FEE** 
> 闪存 EEPROM 仿真（Flash EEPROM Emulation）

**EA** 
> EEPROM 抽象（EEPROM Abstraction）

**FCFS** 
> 先到先服务（First come first served）

# 3. 相关文档

## 3.1. 输入文件及相关标准规范

[1] 词汇表 Glossary
> AUTOSAR_TR_Glossary

[2] 基础软件模块通用规范 (General Specification of Basic Software Modules)
> AUTOSAR_SWS_BSWGeneral

[3] 分层软件架构（Layered Software Architecture）
> AUTOSAR_EXP_LayeredSoftwareArchitecture

[4] EEPROM 抽象规范（Specification of EEPROM Abstraction）
> AUTOSAR_SWS_EEPROMAbstraction

[5] Flash EEPROM 仿真规范（Specification of Flash EEPROM Emulation）
> AUTOSAR_SWS_FlashEEPROMEmulation

[6] 内存抽象接口规范（Specification of Memory Abstraction Interface）
> AUTOSAR_SWS_MemoryAbstractionInterface

[7] CRC 例程规范（Specification of CRC Routines）
> AUTOSAR_SWS_CRCLibrary

[8] EEPROM驱动程序规格（Specification of EEPROM Driver）
> AUTOSAR_SWS_EEPROMDriver

[9] Flash驱动程序规格（Specification of Flash Driver）
> AUTOSAR_SWS_FlashDriver

[10] I/O 硬件抽象需求（Requirements on I/O Hardware Abstraction）
> AUTOSAR_SRS_IOHWAbstraction

[11] 内存服务需求（Requirements on Memory Services）
> AUTOSAR_SRS_MemoryServices

[12] 基本软件模块的一般需求（General Requirements on Basic Software Modules）
> AUTOSAR_SRS_BSWGeneral

[13] 软件组件模板需求（Requirements on Software Component Template）
> AUTOSAR_RS_SoftwareComponentTemplate

[14] RTE软件规格（Specification of RTE Software）
> AUTOSAR_SWS_RTE

## 3.2. 相关规格

**AUTOSAR** 提供了基本软件模块的通用规范 [2，SWS BSW General]，该规范对于 NvM 模块也适用。所以基本软件模块的通用规范应被视为 NvM 的附加且必需的规范。

# 4. 约束和假设

## 4.1. 限制

限制主要在于块管理类型（**Block Management Types**）的有限数量及其对**NV数据**的单独处理。这些限制可以通过增强的用户自定义管理信息（**user defined management information**）来降低，用户自定义管理信息信息可以作为存储真实**NV数据**的结构化部分。在这种情况下，用户定义的管理信息至少必须由应用程序解释和处理。

## 4.2. 汽车领域的适用性

无限制。

## 4.3. 冲突

NvM 可配置为，使用其他软件模块或者集成代码的功能。如：使用 **Csm** 模块进行块数据的加解密。以及块数据的压缩。集成工程师有责任确保：

* NvM 在使用此功能时，所需的功能可用。例如：被调用的 Csm 已经初始化 [或尚未取消初始化]；被调用模块中所需的主函数被执行；等等。
* NvM 在使用此功能时，所需的时间可用。例如：加密算法可能需要一些时间，因此对于需要加密/解密的块，NvM的读/写功能可能需要更长的时间。

# 5. 对其他模块的依赖

本节描述与NvM模块和基础软件中其他模块的关系。

## 5.1. 文件结构

### 5.1.1. 头文件结构

包含文件结构需符合如下要求：

* **NvM**模块应包括**NvM.h**、**Dem.h**、**MemIf.h**。
* **NvM**模块的**上层模块**（**upper layer**）需仅包含 **NvM.h**。

## 5.2. 内存抽象模块

内存抽象模块（**memory abstraction modules**）从依赖于硬件的从属驱动程序中抽象出 **NvM** 模块 （参见：参考文档[3]）。内存抽象模块提供由 **NvM** 模块发起的每个块访问的运行时转换，以选择对于所有配置的 **EEPROM** 或闪存存储设备来说唯一的相应驱动程序功能。内存抽象模块是通过为每个 **NVRAM块** 配置的 **NVRAM块** 设备ID 来选择的。NvM通过内存抽象接口模块**Mem If**访问内存抽象模块。（参见：参考文档[4]、[5]、[6]）

## 5.3. CRC 模块

**NvM** 模块使用 **CRC** 生成例程（8/16/32 位）来检查并生成 **NVRAM** 块的 CRC，作为可配置选项。**CRC** 例程必须由外部提供。（参见：参考文档 [7]）

## 5.4. 底层驱动的能力

必须为每个配置的 **NVRAM** 设备，例如：内部或者外部EEPROM、闪存设备，提供一组底层驱动程序功能。每组驱动程序函数内的唯一驱动程序函数在运行时通过内存硬件抽象模块进行选择（参见：第5.2 章）。一组驱动程序功能必须包括写入、读取或维护（例如：擦除）配置的 NVRAM 设备所需的所有功能。 （参见：参考文档[8]、[9]）

# 6. 需求追踪

略

# 7. 功能说明

## 7.1. 基本架构指南

### 7.1.1. 分层软件架构

下图展示了NvM模块的通信交互。

![Figure7_1](Figure7_1.png)

### 7.1.2. 内存硬件抽象的寻址方案

内存抽象接口（**MemIf**）、底层闪存 EEPROM 仿真（**FEE**）和 EEPROM 抽象层（**EA**）为 **NvM** 模块提供虚拟线性 **32** 位地址空间，该空间由 **16** 位块号和 **16** 位块地址偏移组成。

提示：**NvM** 模块理论上允许最大 **65536** 个逻辑块，每个逻辑块的最大大小为 **64** KB。

同时**NvM** 模块需将 **16bit** Fee/Ea 区块号进一步细分为以下部分：

* 位宽为（**16 - NVM_DATASET_SELECTION_BITS**）的 NV块基数（**NV block base number**）（**NVM_NV_BLOCK_BASE_NUMBER**）
* 位宽为（**NVM_DATASET_SELECTION_BITS**）的数据索引（**Data index**）

冗余NVRAM块（**Redundant NVRAM blocks**）对内存硬件抽象进行的处理和寻址，需以和数据集NVRAM块（**Dataset NVRAM blocks**）采用相同的方式。即：冗余NV块需通过使用配置参数 **NvMDatasetSelectionBits** 进行管理。

NV块基数（**NVM_NV_BLOCK_BASE_NUMBER**）需位于Fee/Ea块号的最高有效位中。

配置工具需能进行块标识符（**block identifiers**）配置，**NvM**模块不应修改配置的块标识符。

#### 7.1.2.1. 示例

为了阐明前面描述的用于 NvM <-> 内存硬件抽象交互的寻址方案，以下示例将有助于理解：**NvM** 端的配置参数 **NvMNvBlockBase Number**、**NvMDatasetSelectionBits** 和 内存硬件抽象上的 **EA_BLOCK_NUMBER** / **FEE_BLOCK_NUMBER** 之间的相关性。

对于给定的示例A和B，使用了一个简单的公式：

FEE/EA_BLOCK_NUMBER = (NvMNvBlockBaseNumber << NvMDatasetSelectionBits) + DataIndex。

**示例 A:**

当把 **NvMDatasetSelectionBits** 配置参数配置为**2**。

* **14Bit位** 可用作配置参数 **NvMNvBlockBaseNumber** 的范围，即**NvMNvBlockBaseNumber** 范围：**0x1** .. **0x3FFE**
* 数据索引（**DataIndex**）范围：**0x0** .. **0x3**，其中 2ˆNvMDatasetSelectionBits - 1 = 3。
* FEE_BLOCK_NUMBER / EA_BLOCK_NUMBER 的范围：**0x4** .. **0xFFFB**

通过此配置，使用前面提到的公式计算的 FEE/EA_BLOCK_NUMBER 应如下例所示：

对于 **NvMNvBlockBaseNumber = 2** 的原生NVRAM块（**Native NVRAM block**），

* NV块通过 FEE/EA_BLOCK_NUMBER = 8 ( 2 * 2 ˆ NvMDatasetSelectionBits + 0) 进行访问。
 
对于 **NvMNvBlockBaseNumber = 3** 的冗余NVRAM块（**Redundant NVRAM block**）：

* 数据索引（**DataIndex**）为 0 的第一个 NV 块通过 FEE/EA_BLOCK_NUMBER = 12 （3 * 2 ˆ NvMDatasetSelectionBits + 0）进行访问。
* 数据索引（**DataIndex**）为 1 的第二个 NV 块通过 FEE/EA_BLOCK_NUMBER = 13 （3 * 2 ˆ NvMDatasetSelectionBits + 1）进行访问。
  
对于 **NvMNvBlockBaseNumber = 4**，且 **NvMNvBlockNum = 3** 的数据集NVRAM块（**Dataset NVRAM block**）：

* 具有数据索引 0 的 NV 块 #0 通过 FEE/EA_BLOCK_NUMBER = 16 进行访问
* 具有数据索引 1 的 NV 块 #1 通过 FEE/EA_BLOCK_NUMBER = 17 进行访问
* 具有数据索引 2 的 NV 块 #2 通过 FEE/EA_BLOCK_NUMBER = 18 进行访问
  
**示例 B:**

当把 **NvMDatasetSelectionBits** 配置参数配置为**4**。

* **12Bit位** 可用作配置参数 **NvMNvBlockBaseNumber** 的范围。
* **NvMNvBlockBaseNumber** 范围：0x1 .. 0xFFE
* 数据索引（**DataIndex**）范围：0x0 .. 0xF，其中 2ˆNvMDatasetSelectionBits-1 = 7。
* FEE_BLOCK_NUMBER / EA_BLOCK_NUMBER 的范围：0x10 .. 0xFFEF

### 7.1.3. 基本存储对象（Basic storage objects）

#### 7.1.3.1. NV块（NV block）

NV块是基本存储对象，表现为 NV用户数据、可选的CRC值、可选NV块标头组成的存储区域。

![Figure7_2](Figure7_2.png)

注意：上图并未显示**NV块**的物理内存布局。仅显示逻辑结构。

#### 7.1.3.2. RAM块（RAM block）

RAM块是基本存储对象，表现为一块RAM区域， 其中包含了：用户数据、可选CRC值、可选NV块标头。

RAM块上CRC使用的限制。仅当相应的NV块也具有CRC时，CRC才可用。CRC的类型必须与相应NV块的类型相同。

注意：有关 CRC 配置的更多信息，请参阅第 10.2.3 章。

RAM块的用户数据区域可以分配到与RAM块状态不同的RAM地址位置（全局数据部分）。

RAM块的数据区域需可被NvM和应用程序访问。数据可以和相应的NV块间进行数据交换。

![Figure7_3](Figure7_3.png)

注意：该图未显示**RAM块**的物理内存布局。 仅显示逻辑结构。

由于**NvM**模块不支持对齐，但是它可以通过配置来管理实现，即可以通过添加填充来扩大块长度以满足对齐要求。

**RAM块**数据需包含永久或临时分配的用户数据。对于永久分配的用户数据，**RAM块**数据的地址在配置期间是已知的；对于临时分配的用户数据，**RAM块**数据的地址在配置期间未知，并将在运行时传递到 **NvM** 模块。

因此可以在全局 RAM 区域中（**Global RAM area**）分配每个 **RAM块**，而不受地址的限制。 配置的**RAM块**的总数并不需要位于连续的地址空间中。

#### 7.1.3.3. ROM块（ROM block）

**ROM块**是基本存储对象，驻留在ROM中，用于在**NV块**为空或损坏的情况下提供默认数据。

![Figure7_4](Figure7_4.png)

#### 7.1.3.4. 管理块（Administrative block）

管理块应位于 **RAM** 中，并应包含与**数据集NV块**关联使用的块索引。此外，还应包含相应 **NVRAM** 块的属性、错误、状态信息。

在显式同步（无效/有效）的情况下，**NvM** 模块需使用**永久RAM块**或 **NvM** 模块中**RAM镜像**的状态信息来确定**永久RAM块**用户数据的有效性。

RAM块状态的“**无效**”表示相应**RAM块**的数据区域是无效的。RAM块状态的“**有效**”表示相应RAM块的数据区域是有效的。“无效”的值应当由除“有效”之外的所有其他值来表示。

管理块对于应用程序来说是不可见的，并且由 **NvM** 模块专门用于 **RAM块** 和 **NVRAM块** 本身的安全和管理目的。

**NvM** 模块需使用属性字段来管理 **NV块**的写保护，以便保护/取消保护**NV块数据字段**。

**NvM** 模块需使用错误、状态字段来管理上次请求的错误以及状态值。

#### 7.1.3.5. NV块标头（**NV Block Header**）

如果启用了静态块ID（**Static Block ID**）机制，则 NV块标头需包含在NV块的首部。

![Figure7_5](Figure7_5.png)

### 7.1.4. 块管理类型

#### 7.1.4.1. 块管理类型概述

**NvM** 模块实现需支持以下类型的 **NVRAM** 存储：

* NVM_BLOCK_NATIVE
* NVM_BLOCK_REDUNDANT
* NVM_BLOCK_DATASET

**NVM_BLOCK_NATIVE** 原生类型的**NVRAM**存储需由以下基本存储对象组成：

* 1 个 NV块（**NV Block**）
* 1 个 RAM块（**RAM Block**）
* 0 到 1 个 ROM块（**ROM Block**）
* 1 个 管理块（**Administrative Block**）

**NVM_BLOCK_REDUNDANT** 冗余类型的**NVRAM**存储需由以下基本存储对象组成：

* 2 个 NV块（**NV Block**）
* 1 个 RAM块（**RAM Block**）
* 0 到 1 个 ROM块（**ROM Block**）
* 1 个 管理块（**Administrative Block**）

**NVM_BLOCK_DATASET** 数据集类型的**NVRAM**存储需由以下基本存储对象组成：

* 1 到 m 个 NV块（**NV Block**）
* 1 个 RAM块（**RAM Block**）
* 0 到 n 个 ROM块（**ROM Block**）
* 1 个 管理块（**Administrative Block**） NV 块

注意：m和n的最大值为**255**，同时m和n定义的数据集数量也取决于**NvMDatasetSelectionBits**配置参数。

#### 7.1.4.2. NVRAM块结构

**NVRAM块**组成包括了强制的基本存储对象：NV块、RAM块和管理块。但基本存储对象ROM块是可选的。

任何**NVRAM块**的组成在配置期间，通过相应的**NVRAM块描述符**（**NVRAM block descriptor**）固化了。

所有地址偏移量都是相对于NVRAM块描述符中 **RAM** 或 **ROM**的起始地址给出的。假设起始地址为零。

提示：如果需要，相应的设备驱动程序将添加设备特定的基地址或偏移量。有关**NVRAM块描述符**的详细信息，请参阅第 7.1.4.3 章节。

#### 7.1.4.3. NVRAM块描述符表（NVRAM block descriptor table）

要处理的每个**NVRAM块**，可由随后分配的**块ID**（**Block ID**），通过 **NvM** 模块 **API** 进行选择。

所有与**NVRAM块描述符表**及其在 ROM（闪存）中的地址相关的结构信息，都必须在 **NvM** 模块配置期间生成。

#### 7.1.4.4. 原生NVRAM块（Native NVRAM block）

**原生NVRAM块**是最简单的块管理类型。它允许以最小的开销存储到**NV内存**中，或者从**NV内存**检索并获取。

**原生NVRAM块**由单个的**NV块**、**RAM块**和**管理块**组成。

#### 7.1.4.5. 冗余NVRAM块（Redundant NVRAM block）

除了**原生NVRAM块**提供的功能之外，**冗余NVRAM块**还提供增强的容错性、可靠性和可用性。它增强了对数据损坏的抵抗力。

**冗余NVRAM块**由两个**NV块**、一个**RAM块**和一个**管理块**组成。

下图反映了**冗余NV块**的内部结构：

![Figure7_6](Figure7_6.png)

注意：该图未显示**冗余NVRAM块**的物理NV内存布局。仅显示逻辑结构。

如果与**冗余NVRAM块**关联的一个NV块被视为无效，例如：在读取期间。则应尝试使用来自未损坏**NV块**的数据来恢复此**NV块**。如果恢复失败，则需使用代码 **NVM_E_LOSS_OF_REDUNDANCY** 向 **DEM**模块报告此情况。

注意：恢复表示冗余的重新建立。这通常意味着将恢复的数据写回**NV块**。

#### 7.1.4.6. 数据集NVRAM块（Dataset NVRAM block）

**数据集NVRAM块**是大小相等的数据块 (NV/ROM) 的阵列数组（**array**）。应用程序可以在任意时刻访问其中的某个元素。

**数据集NVRAM块**由多个**NV用户数据**、可选的**CRC区域**、可选的**NV块标头**、**RAM块**和**管理块**组成。

**数据集NVRAM块**的索引位置（**index position**）是通过相应的管理块中的单独字段来标识的。

**NvM** 模块应能够读取所有被分配的**NV块**。当且仅当写保护被禁用时，**NVM** 模块才能够写入所有被分配的**NV块**。

如果选择基本存储对象ROM块作为可选部分，则通常选择数据集的索引范围被扩展到ROM，使得可以选择ROM块而不是NV块。该索引涵盖了可以构建**数据集NVRAM块**的所有 **NV/ROM** 块。

**NvM** 模块应只能读取可选**ROM块**，即：默认数据集。NvM 模块需将写入**ROM块**的操作视为写入受保护的**NV块**。

配置数据集（NV+ROM 块）的总数应在 **1..255** 范围内。对于可选**ROM块**，索引从**0**到**NvMNvBlockNum - 1**的数据区域，表示了**NV块**以及在**NV存储器**中的**CRC**。索引从 **NvMNvBlockNum** 到 **NvMNvBlockNum + NvMRomBlockNum - 1** 的数据区域表示**ROM块**。

![Figure7_7](Figure7_7.png)

注意：该图未显示**数据集NVRAM块**的物理NV内存布局。 仅显示逻辑结构。

