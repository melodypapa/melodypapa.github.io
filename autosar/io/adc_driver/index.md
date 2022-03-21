<section id="title">AUTOSAR ADC Driver（模数转换器驱动）</section>

# 1. 简介和功能概述

本文介绍了**AUTOSAR**基础软件模块**ADC**驱动程序的功能、**API**和配置。**ADC**驱动程序的目标是逐次逼近**ADC**硬件数值。但**Delta Sigma ADC**转换用例超出了AUTOSAR ADC驱动的范畴。

**ADC**驱动模块主要负责初始化和控制**MCU**内部的模数转换器单元（**Analogue Digital Converter Unit**）。为此**ADC**驱动模块提供了启动和停止转换服务，以实现启用和禁用ADC转换的触发。此外也提供通知机制（**notification mechanism**）以及查询转换状态和结果的服务。

**ADC**模块工作在**ADC**通道组（**ADC Channel Group**）上。这些通道组是由多条**ADC**通道（**ADC Channel**）构成。**ADC**通道组将模拟输入引脚（即：ADC通道）、所需的ADC电路本身和转换结果寄存器组合成一个实体，实现可通过**ADC**模块独立的控制及访问。

# 2. 缩略语

**DET**
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。

**DEM**
> 诊断事件管理器（**Diagnostic Event Manager**）。

**ADC**
> 模数转换器（**Analogue Digital Converter**）

**MCU**
> 微控制器单元（**Microcontroller Unit**）

**ADC HW Unit**
> 微控制器的输入电子设备，包括执行模拟到数字转换所需的所有部件。

**ADC Module**
> ADC的基础软件模块ADC驱动模块（**ADC Driver**）

**ADC Channel**
> **ADC**通道。指绑定到一个端口引脚的逻辑**ADC**实体。同时多个**ADC**实体也可以映射到同一个端口引脚。

**ADC Channel Group**
> 一组**ADC**通道链接到同一个**ADC**硬件单元（**ADC HW Unit**）。例如：一个采样点对应一个**A/D**转换器。整个组的转换由一个触发源触发。

**ADC Result Buffer**
> 也称为**ADC Streaming Buffer**或者**ADC Stream Buffer**。**ADC**驱动程序的用户必须为每个组提供一个缓冲区。如果选择流式访问模式（**streaming access mode**），此缓冲区可以保存同一组通道的多个样本。如果选择单一访问模式（），每个组通道的一个样本将保存在缓冲区中。

