---
title: "AUTOSAR 术语表（缩略语与缩写）"
---

本页汇总各 AUTOSAR 模块文章以及 AUTOSAR TR 术语表（Foundation）的术语，按字母排序。

## A

**Acquisition Time**
> 采集时间 = 采样时间（**Sample Time**）+ 转换时间（**Conversion Time**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC**
> 模数转换器（**Analogue Digital Converter**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Channel**
> **ADC**通道是指绑定到一个端口引脚的逻辑**ADC**实体。同时多个**ADC**实体也可以映射到同一个端口引脚。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Channel Group**
> **ADC**通道组是指由一组**ADC**通道链接到同一个**ADC**硬件单元（**ADC HW Unit**）。例如：一个采样保持器（**Sample & Hold**）和一个**A/D**转换器。整个组的转换由一个触发源触发。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC HW Unit**
> 微控制器的输入电子设备，包括执行模拟到数字转换所需的所有部件。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Module**
> ADC的基础软件模块ADC驱动模块（**ADC Driver**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**ADC Result Buffer**（**ADC Streaming Buffer**，**ADC Stream Buffer**）
> **ADC**驱动程序的用户必须为每个组提供一个缓冲区。如果选择流式访问模式（**streaming access mode**），此缓冲区可以保存同一组通道的多个样本。如果选择单一访问模式（**Single Access Mode**），每个组通道的一个样本将保存在缓冲区中。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**API**
> 应用编程接口（**Application Programming Interface**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

## B

**BSW**
> 基础软件（**Basic Software**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## C

**Conversion Mode**
> One-Shot：**ADC**通道组的转换在触发后执行一次，结果写入所分配的结果缓冲区。触发可以是软件**API**调用或硬件事件。Continuous：**ADC**通道组的转换在软件**API**调用（启动）后连续执行，结果写入所分配的结果缓冲区。转换本身自动运行（由硬件/中断控制）。连续转换可通过软件**API**调用（停止）停止。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**Conversion Time**
> 转换时间是指将采样的模拟值转换为数值所需的时间。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

## D

**DEM**
> 诊断事件管理器（**Diagnostic Event Manager**）。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）

**DET**
> 默认错误跟踪器（**Default Error Tracer**），实现报告开发错误的模块。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## E

**ECU**
> 电子控制单元（**Electronic Control Unit**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## G

**GPT**
> 通用定时器（**General Purpose Timer**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**GPT Predef Timer**
> **GPT Predef Timer** 是 **GPT** 驱动程序提供的自由运行递增计数器。哪些 **GPT Predef Timer** 可用取决于硬件（时钟、硬件定时器、预分频器、定时器寄存器宽度等）和配置。**GPT Predef Timer** 具有预定义的物理时间单位和范围。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## H

**Hardware Trigger**
> 硬件触发是**ADC**内部触发信号，用于启动ADC通道组的一次转换。**ADC**硬件触发在ADC硬件内部生成（例如：基于**ADC**定时器或触发沿信号）。触发硬件是强耦合或者直接集成在**ADC**的硬件中。当检测到硬件触发后，无需软件即可启动**ADC**通道组转换。**注意：**即使**ADC**硬件不支持硬件触发，也可以通过软件触发结合**GPT/ICU**驱动程序来实现类似的行为。（例如：在GPT定时器通知函数中，启动软件触发的**ADC**通道组的转换）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**HW**
> 硬件（**Hardware**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

## I

**ICU**
> 输入捕获单元（**Input Capture Unit**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## M

**MCU**
> 微控制器单元（**Microcontroller Unit**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## N

**NOP, nop**
> 空操作（**Null Operation**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## O

**OS**
> 操作系统（**Operating System**）
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## S

**Sampling Time, Sample Time**
> 采样时间是指对模拟值进行采样的时间（例如：加载电容器，……）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SFR**
> 特殊功能寄存器（**Special Function Register**），**MCU** 寄存器
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）

**Software Trigger**
> 软件触发是一个软件**API**调用，用于启动转换一个**ADC**通道组或一系列连续**ADC**通道组转换的。
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

**SW**
> 软件（**Software**）
> 来源：[AUTOSAR ADC Driver（模数转换器驱动）](io/adc_driver/index.md)（SWS_ADCDriver · R23-11）

## T

**Target time**
> 目标时间：到达该值时应有某事发生。其行为取决于配置和已启用的功能。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**Tick**
> 定义定时器分辨率，即定时器一次递增的持续时间。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

**Timer channel**
> 表示分配给一个定时器硬件的逻辑定时器实体。
> 来源：[AUTOSAR GPT Driver（通用定时器驱动）](mcal/gpt_driver/index.md)（SWS_GPTDriver · R23-11）

## U

**uC**
> 微控制器（**Microcontroller**）
> 来源：[AUTOSAR MCU Driver（微控制器单元驱动）](mcal/mcu_driver/index.md)（SWS_MCUDriver · R23-11）
