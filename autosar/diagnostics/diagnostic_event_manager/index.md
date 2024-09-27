<section id="title">AUTOSAR Diagnostic Event Manager（诊断事件管理器）</section>

# 1. 简介和功能概述

诊断事件管理器 (**Dem**) 服务组件，主要负责处理和存储诊断事件（错误）以及与其相关数据。此外 **Dem** 还需向 **Dcm** 提供故障信息，（例如：从事件内存中读取所有存储的 **DTC**）。**Dem** 也需提供与应用层和其他 **BSW** 模块的接口。

**Dem** 规范文档的基本目标是为汽车制造商和组件供应商定义《诊断故障内存》（**diagnostic fault memory**）通用方法的能力。

本规范定义了 AUTOSAR 基本软件模块诊断事件管理器 (Dem) 的功能、API 和配置。部分内部行为是制造商特定的，并在**限制**一章中进行了详细描述。

# 首字母缩略词和缩写

以下词汇表包含与 **Dem** 模块相关的首字母缩略词和缩写，同时这些词汇表并未包含在【参考文档#4的AUTOSAR 词汇表】中。

# 2. 功能规格

**激活模式1（Activation Mode 1）**
> 无故障-MIL应闪烁一次。

**激活模式2（Activation Mode 2）**
> "on-demand-MI" - The MIL shall show blink for two flashes if the OBD system would command an on-demand-MI according to the discriminatory display strategy.

**激活模式3（Activation Mode 3）**
> "short-MI" - The MIL shall blink for three flashes if the OBD system would command a short-MI according to the discriminatory display strategy.

**激活模式4（Activation Mode 4（**
> "continuous-MI" - The MIL shall remain continuously ON ("continuous-MI") if the OBD system would command a continuous-MI according to the discriminatory display strategy. Aging Unlearning/deleting of a no longer failed event/DTC after a defined number of operation cycles from event memory.

Aging Counter
The "Aging Counter" or "Aging Cycle Counter" or "DTC Aging
Counter" specifies the counter which is used to perform Aging.
It counts the number of operation cycles until an event/DTC is
removed from event memory.

Class B1 counter 
Number of engine hours during which a Class B1 malfunction has
been Confirmed and TestFailed.

Combined DTC
Normal DTC, but referenced by multiple events reported by several
monitors (e.g. ECU Defect, consisting of different HW defects).
Continuous-MI counter Hours run by the engine while a continuous MI is commanded.

Cumulative Continuous-MI counter
Number of engine hours during which MI has been continuously
commanded to be on during its lifetime.
Debounce counter Internal counter for counter-based debouncing algorithm(s).
DemComponent / Monitored
Component
A monitored component is a part of the system, which is checked
for proper operation by one or several monitorings. (see chapter
7.5)
Dem-internal data value Some data values (e.g. the occurrence counter) are calculated
by the Dem module itself internally.
Denominator
The denominator of a specific monitor m (Denominatorm) is a
counter indicating the number of vehicle driving events, taking
into account conditions specific to that specific monitor.
Dependent / Secondary ECUs Dependent / Secondary (or dep. / sec. ) ECUs are always related
to a Master or a Primary ECU.
Directed acyclic graph Dependency graph without circular dependencies.
Displacement
Replacing the the most insignificant event memory entry by
a more significant event memory entry which needs to be
stored.

## 2.1. 启动行为

## 2.2. 监视的重新初始化

## 2.3. 诊断事件定义

## 2.4. 诊断故障代码定义

## 2.5. 受监控的组件定义

## 2.6. 运行周期管理

## 2.7. 事件内存的说明

## 2.8. BSW 错误处理

## 2.9. OBD特定功能

## 2.10. J1939特定功能

## 2.11. 与其他软件模块的交互

### 2.11.1. 与软件组件的交互 (SW-C)

### 2.11.2. 与诊断客户端的交互

### 2.11.3. 与J1939诊断管理器的交互

### 2.11.4. 与功能抑制管理器 (FIM) 的交互

### 2.11.5. 与NVRAM管理器 (NvM) 的交互

**Dem**模块使用非易失性内存块（**Nonvolatile Memory Blocks**）来实现**UDS**状态信息、事件相关数据和所需内部状态的永久存储。例如：在启动时获取事件的状态。

**Dem**模块可以通过**NVRAM**管理器[5]进行大小的配置。

**Dem**使用的每个非易失性内存块也需要进行配置，具体内容可参阅：**DemNvRamBlockId**。使用的非易失性存储块的数量、类型和内容没有规定。这些可根据具体实现进行处理。**NvM**的使用也可以通过配置**DemNvRamBlockId**进行禁用，这时**Dem**将仅基于**RAM**工作。

**Dem**模块应验证非易失性块的有效性（与块状态相关）、完整性（与**CRC**结果相关）和一般**NvM**读取错误（在使用相应数据之前）。通常这种验证是在 **Dem_Init**中，通过对这些NvM内存块使用**NvM_GetErrorStatus**来完成的，这些内存块由ECU状态管理器通过**NvM_ReadAll**读取。

注意：

对于**Dem**模块的非易失性数据，建议在**NvM**中配置一个**CRC**。

如果**NVM**模块无法读取**Dem**模块的某些非易失性数据，则**Dem**模块需使用其初始值初始化所有非易失性数据。

注意：

为了避免可读数据块和错误的数据块之间的不一致，所有非易失性数据都会被初始化。完成初始化后，应允许**NvM**模块的故障检测机制向**Dem**模块报告相应的读取错误（具体可参阅**Dem_SetEventStatus**）。 用于表示有缺陷的**NVRAM**。

**Dem_Init**完成后，**Dem**模块应完全可操作。

如果**DTC**配置为**DemNvStorageStrategy** = **IMMEDIATE_AT_FIRST_OCCURRENCE**，则在事件第一次发生时需立即存储相关数据，则当配置的用于存储数据的触发器 DemEventMemoryEntryStorageTrigger 第一次发生时，Dem 应触发将其事件相关数据存储到 NvM。

