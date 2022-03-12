<section id="title">AUTOSAR FLS（闪存驱动程序）</section>

# 1. 介绍

本文介绍了**AUTOSAR**基础软件模块闪存驱动程序（**Flash Driver**）的功能、**API**和配置，AUTOSAR的闪存驱动程序同时适用于内部和外部闪存设备。

通过底层硬件支持，闪存驱动程序提供了读取、写入和擦除闪存的服务，以及用于设置或者重置关于写入及擦除保护的配置接口。

在**ECU**的应用程序模式下，**Flash**驱动程序仅供**Flash EEPROM emulation**模块用于写入数据使用。**Flash**驱动程序并未打算提供在应用程序模式下把程序代码写入闪存的服务，此部分应在**AUTOSAR**范围之外的引导模式下完成，如**Flash Bootloader**中实现。

内部闪存驱动程序可以直接访问微控制器（**microcontroller**）硬件，它位于**MCAL**微控制器抽象层（**Microcontroller Abstraction Layer**）。然而外部闪存通常连接到微控制器的数据/地址总线，通过内存映射访问，通常闪存驱动程序使用这些总线的处理程序/驱动程序来访问外部闪存设备，所以外部闪存设备的驱动程序位于ECU抽象层（**ECU Abstraction Layer**）。

对于内部和外部驱动程序的功能要求和功能范围是相同的，所以在语义上API的定义应该也是相同的。

# 2. 缩略语

**DET**
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。

**DEM**
> 诊断事件管理器（**Diagnostic Event Manager**）。

**Fls, FLS**
> AUTOSAR闪存驱动程序的官方缩写

**AC**
> 闪存访问代码（**access code**）的缩写。

**闪存扇区**
> 闪存扇区（**Flash sector**）是一次可以擦除的最小闪存量。闪存扇区的大小取决于闪存技术，因此取决于硬件。

**闪存页**
> 闪存页面（**Flash page**）是一次可以编程的最小闪存量。闪存页面的大小取决于闪存技术，因此取决于硬件。

**闪存访问代码**
> 由主函数（作业处理函数）调用的内部闪存驱动程序例程，用于擦除或写入闪存硬件。

# 3. 相关文档

## 3.1. 输入文件

[1] List of Basic Software Modules
> AUTOSAR_TR_BSWModuleList.pdf

[2] Layered Software Architecture,
> AUTOSAR_EXP_LayeredSoftwareArchitecture.pdf

[3] General Requirements on Basic Software Modules,
> AUTOSAR_SRS_BSWGeneral.pdf

[4] General Requirements on SPAL,
> AUTOSAR_SRS_SPALGeneral.pdf

[5] Requirements on Flash Driver
> AUTOSAR_SRS_FlashDriver.pdf

[6] Requirements on Memory Hardware Abstraction Layer
> AUTOSAR_SRS_MemoryHWAbstractionLayer.pdf

[7] Specification of ECU Configuration
> AUTOSAR_TPS_ECUConfiguration.pdf

[8] Basic Software Module Description Template
> AUTOSAR_TPS_BSWModuleDescriptionTemplate.pdf

[9] General Specification of Basic Software Modules
> AUTOSAR_SWS_BSWGeneral.pdf

## 3.2. 相关规范

AUTOSAR提供了基础软件模块的通用规范[9]，它同样也适用于**Flash**驱动程序。

因此基础软件模块的通用规范[9]也应被视为**Flash**驱动程序的附加和必需的规范。

# 4. 约束和假设

## 4.1. 限制

闪存驱动程序仅擦除或编程（**programm**）完整的闪存扇区和闪存页面。也就是说因为闪存驱动程序不使用任何内部缓冲区，所以它也不提供任何类型的重写策略。

同时，闪存驱动程序也不提供提供数据完整性的机制。例如：校验和（**checksums**）、冗余存储（**redundant storage**）等。

# 5. 对其他模块的依赖

## 5.1. 系统时钟（System clock）

如果内部闪存的硬件依赖于系统时钟，系统时钟的改变（例如：**PLL On**切换到**PLL Off**）也可能影响到闪存硬件的时钟设置。

## 5.2. 通信或I/O驱动程序

如果闪存位于外部设备，则需要通过相应的I/O驱动程序实现对该设备的通信访问。

# 6. 功能规格

## 一般设计规则

**FLS**模块应为闪存操作（包括：读/写/擦除）提供异步（**asynchronous**）服务。

**FLS**模块无需对数据进行额外的缓存，它只需通过API传递的指针参数引用应用程序的数据缓冲区即可。同时**FLS**模块也无需确保应用程序缓冲区数据的一致性。但**FLS**模块需负责确保闪存读取或写入操作期间闪存数据的一致性。

**FLS**模块需负责静态检查所有的静态配置参数是否正确（最迟在编译期间）。

**FLS**模块需将所有可用的闪存区域组合成一个线性地址空间（通过参数**FlsBaseAddress**和**FlsTotalSize**表示）。

**FLS**模块需根据闪存区域的物理结构将读取、写入、擦除和比较功能的地址和长度参数作为“虚拟”地址映射到物理地址。

