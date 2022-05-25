<section id="title">AUTOSAR FEE（闪存EEPROM仿真）</section>

# 1. 介绍

本文档描述了闪存EEPROM仿真（**Flash EEPROM Emulation**）模块的功能、API和配置。

**FEE**模块应从设备特定的寻址方案和分段中抽象出来，并为上层提供虚拟寻址方案和分段（**virtual addressing scheme and segment**）以及虚拟的无限数量的擦除周期。

# 2. 缩略语

**EA**
> EEPROM Abstraction

**EEPROM**
> Electrically Erasable and Programmable ROM (Read Only Memory)

**FEE**
> Flash EEPROM Emulation

**LSB**
> Least significant bit / byte (depending on context). Here, “bit” is meant.

**MemIf**
> Memory Abstraction Interface

**MSB**
> Most significant bit / byte (depending on context). Here, “bit” is meant.

**NvM**
> NVRAM Manager

**NVRAM**
> Non-volatile RAM (Random Access Memory)

**NVRAM block**
> Management unit as seen by the NVRAM Manager

**(Logical) block**
> Smallest writable / erasable unit as seen by the modules user. Consists of one or more virtual pages.

**Virtual page**
> May consist of one or several physical pages to ease handling of logical blocks and address calculation.

**Internal residue**
> Unused space at the end of the last virtual page if the configured block size isn’t an integer multiple of the virtual page size (see Figure 3)).

**Virtual address**
> Consisting of 16 bit block number and 16 bit offset inside the logical block.

**Physical address**
> Address information in device specific format (depending on the underlying EEPROM driver and device) that is used to access a logical block.

**Dataset**
> Concept of the NVRAM manager: A user addressable array of blocks of the same size. E.g. could be used to provide different configuration settings for the CAN driver (CAN IDs, filter settings, …) to an ECU which has otherwise identical application software (e.g. door module).

**Redundant copy**
> Concept of the NVRAM manager: Storing the same information twice to enhance reliability of data storage.

# 3. 功能规格

## 3.1. 一般行为

### 3.1.1. 寻址方案和分段

FEE模块为上层提供**32**位虚拟线性地址空间和统一分段方案。该虚拟**32**位地址应包括：

* **16**位块序号（**block number**）：理论上允许数量为**65536**个逻辑块。
* **16**位块偏移（**block offset**）：理论上每块数据块为**64K**字节的块大小。

16位块序号代表一种可配置的虚拟分页（**virtual paging**）机制。而地址对齐（**address alignment**）的值可以从底层闪存驱动程序和设备导出。虚拟分页（**virtual paging**）可通过参数**FeeVirtualPageSize**进行配置。

**FEE**模块的配置应使虚拟页面大小（在**FeeVirtualPageSize**中定义）需是物理页面大小的整数倍，即不允许配置比实际物理页面大小更小的虚拟页面。

**注意：**

AUTOSAR规范要求允许逻辑块的物理起始地址能被计算，而不是通过制作查找表（**Lookup table**）来进行地址映射。

**示例：**

因为虚拟页的大小被配置为8个字节，所以地址为8字节对齐。如果块序号为**1**的逻辑块会放置在物理地址**x**的地址，则块序号为**2**的逻辑块将被放置在**x+8**的地址，块序号**3**将被放置在**x+16**的地址。

每个配置的逻辑块需占用所配置的虚拟页面大小的整数倍。

**示例：**

通过将设置参数**FeeVirtualPageSize**设定为**8**，则地址对齐/虚拟分页配置为**8**个字节。 逻辑块编号 1 配置为具有 32 个字节的大小（参见图 3）。 这个逻辑块将使用 4 个虚拟页面。 因此，下一个逻辑块将获得块号 5，因为块号 2、3 和 4 被第一个逻辑块“阻塞”。 第二个块配置为 100 字节大小，占用 13 个虚拟页面，最后一页的 4 个字节未使用。 因此，下一个可用的逻辑块号将是 17。

![](2022-05-22-19-57-13.png)