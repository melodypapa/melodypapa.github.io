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
