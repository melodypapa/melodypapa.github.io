---
title: "寄存器索引（Register Index）"
---

本附录提供本手册中 **Arm** 寄存器描述的索引，涵盖 **Arm** 内核寄存器与内存映射寄存器。本章包含以下小节：

* 第 D8-842 页的 **Arm 内核寄存器**。
* 第 D8-843 页的**浮点扩展寄存器**。
* 第 D8-844 页的**内存映射的系统寄存器**。
* 第 D8-847 页的**内存映射的调试寄存器**。

## 1. Arm 内核寄存器

表 D8-1 是 **Armv7-M** 中定义的 **Arm** 内核寄存器主要描述的索引。

表 D8-1 Arm 内核寄存器索引：

| 寄存器 | 参见 |
| --- | --- |
| R0、R1、R2、R3、R4、R5、R6、R7、R8、R9、R10、R11、R12 | 第 B1-516 页的**寄存器** |
| SP_main、SP_process | 第 B1-516 页的 **SP 寄存器** |
| LR（R14） | 第 B1-516 页的**寄存器** |
| PC（R15） | 第 B1-516 页的**寄存器** |
| APSR | 第 B1-516 页的**特殊功能程序状态寄存器 xPSR** |
| IPSR | 第 B1-516 页的**特殊功能程序状态寄存器 xPSR** |
| EPSR | 第 B1-516 页的**特殊功能程序状态寄存器 xPSR** |
| PRIMASK | 第 B1-519 页的**特殊功能屏蔽寄存器** |
| FAULTMASK | 第 B1-519 页的**特殊功能屏蔽寄存器** |
| BASEPRI | 第 B1-519 页的**特殊功能屏蔽寄存器** |
| CONTROL | 第 B1-519 页的**特殊功能 CONTROL 寄存器** |

## 2. 浮点扩展寄存器

下列小节列出**浮点扩展**（**Floating-point Extension**）的寄存器：

* **浮点扩展系统寄存器**。
* **浮点扩展寄存器**。

浮点扩展还在处理器的内存映射**系统寄存器**空间中增加寄存器，参见第 D8-844 页的**内存映射的系统寄存器**。

### 2.1. 浮点扩展系统寄存器

浮点扩展在 CP10 与 CP11 寄存器空间中增加一个系统寄存器 FPSCR，参见第 A2-37 页的**浮点状态与控制寄存器，FPSCR**。

### 2.2. 浮点扩展寄存器

浮点扩展为其数据寄存器组提供两种视图：

* **单精度视图**（**single-precision view**）把寄存器视为 32 位的 S0-S31。
* **双字视图**（**doubleword view**）把寄存器视为 64 位的 D0-D15。

更多信息参见第 A2-35 页的 **FP 扩展寄存器**。

## 3. 内存映射的系统寄存器

表 D8-2 是 **Armv7-M** 中定义的内存映射系统控制寄存器主要描述的索引。表中 **Notes** 列的含义为：

* **CPUID**：该寄存器属于 **CPUID** 方案，参见第 B4 章的 **CPUID 方案**。每个 **Armv7-M** 处理器都实现这些寄存器。
* **FP extension**：该寄存器属于**浮点扩展**。**Armv7-M** 处理器仅在包含浮点扩展时才实现该寄存器。

表 D8-2 内存映射系统寄存器索引：

| 寄存器 | 参见 | 备注 |
| --- | --- | --- |
| ACTLR | [第 B3-618 页的辅助控制寄存器，ACTLR](../../part-b/system_address_map/index.md) | - |
| AFSR | [第 B3-614 页的辅助故障状态寄存器，AFSR](../../part-b/system_address_map/index.md) | - |
| AIRCR | [第 B3-601 页的应用程序中断与复位控制寄存器，AIRCR](../../part-b/system_address_map/index.md) | - |
| BFAR | [第 B3-614 页的 BusFault 地址寄存器，BFAR](../../part-b/system_address_map/index.md) | - |
| BFSR | [第 B3-610 页的 BusFault 状态寄存器，BFSR](../../part-b/system_address_map/index.md) | - |
| BPIALL | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| CCR | [第 B3-604 页的配置与控制寄存器，CCR](../../part-b/system_address_map/index.md) | - |
| CFSR | [第 B3-609 页的可配置故障状态寄存器，CFSR](../../part-b/system_address_map/index.md) | - |
| CPACR | [第 B3-614 页的协处理器访问控制寄存器，CPACR](../../part-b/system_address_map/index.md) | - |
| CPUID | [第 B3-598 页的 CPUID 基址寄存器](../../part-b/system_address_map/index.md) | - |
| DCCIMVAC | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| DCCISW | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| DCCMVAC | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| DCCMVAU | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| DCCSW | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| DCIMVAC | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| DCISW | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| FPCAR | [第 B3-617 页的浮点上下文地址寄存器，FPCAR](../../part-b/system_address_map/index.md) | FP 扩展 |
| FPCCR | [第 B3-615 页的浮点上下文控制寄存器，FPCCR](../../part-b/system_address_map/index.md) | FP 扩展 |
| FPDSCR | [第 B3-617 页的浮点默认状态控制寄存器，FPDSCR](../../part-b/system_address_map/index.md) | FP 扩展 |
| HFSR | [第 B3-612 页的 HardFault 状态寄存器，HFSR](../../part-b/system_address_map/index.md) | - |
| ICIALLU | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| ICIMVAU | [第 B2-577 页的缓存与分支预测器维护操作](../../part-b/system_memory_model/index.md) | - |
| ICSR | [第 B3-599 页的中断控制与状态寄存器，ICSR](../../part-b/system_address_map/index.md) | - |
| ICTR | [第 B3-618 页的中断控制器类型寄存器，ICTR](../../part-b/system_address_map/index.md) | - |
| ID_AFR0 | [第 B4-649 页的辅助特性寄存器 0，ID_AFR0](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_DFR0 | [第 B4-648 页的调试特性寄存器 0，ID_DFR0](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_ISAR0 | [第 B4-654 页的指令集属性寄存器 0，ID_ISAR0](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_ISAR1 | [第 B4-655 页的指令集属性寄存器 1，ID_ISAR1](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_ISAR2 | [第 B4-657 页的指令集属性寄存器 2，ID_ISAR2](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_ISAR3 | [第 B4-658 页的指令集属性寄存器 3，ID_ISAR3](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_ISAR4 | [第 B4-659 页的指令集属性寄存器 4，ID_ISAR4](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_MMFR0 | [第 B4-650 页的内存模型特性寄存器 0，ID_MMFR0](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_MMFR1 | [第 B4-651 页的内存模型特性寄存器 1，ID_MMFR1](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_MMFR2 | [第 B4-651 页的内存模型特性寄存器 2，ID_MMFR2](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_MMFR3 | [第 B4-651 页的内存模型特性寄存器 2，ID_MMFR2](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_PFR0 | [第 B4-646 页的处理器特性寄存器 0，ID_PFR0](../../part-b/cpuid_scheme/index.md) | CPUID |
| ID_PFR1 | [第 B4-646 页的处理器特性寄存器 1，ID_PFR1](../../part-b/cpuid_scheme/index.md) | CPUID |
| MMFAR | [第 B3-613 页的 MemManage 故障地址寄存器，MMFAR](../../part-b/system_address_map/index.md) | - |
| MMFSR | [第 B3-609 页的 MemManage 状态寄存器，MMFSR](../../part-b/system_address_map/index.md) | - |
| MPU_CTRL | 第 B3-637 页的 MPU 控制寄存器，MPU_CTRL | - |
| MPU_RASR | 第 B3-640 页的 MPU 区域属性与大小寄存器，MPU_RASR | - |
| MPU_RBAR | 第 B3-639 页的 MPU 区域基址寄存器，MPU_RBAR | - |
| MPU_RNR | 第 B3-638 页的 MPU 区域编号寄存器，MPU_RNR | - |
| MPU_TYPE | 第 B3-636 页的 MPU 类型寄存器，MPU_TYPE | - |
| MVFR0 | [第 B4-662 页的媒体与 FP 特性寄存器 0，MVFR0](../../part-b/cpuid_scheme/index.md) | FP 扩展 |
| MVFR1 | [第 B4-663 页的媒体与 FP 特性寄存器 1，MVFR1](../../part-b/cpuid_scheme/index.md) | FP 扩展 |
| NVIC_IABRn | [第 B3-630 页的中断活动位寄存器，NVIC_IABR0-NVIC_IABR15](../../part-b/system_address_map/index.md) | - |
| NVIC_ICERn | [第 B3-628 页的中断清使能寄存器，NVIC_ICER0-NVIC_ICER15](../../part-b/system_address_map/index.md) | - |
| NVIC_ICPRn | [第 B3-629 页的中断清未决寄存器，NVIC_ICPR0-NVIC_ICPR15](../../part-b/system_address_map/index.md) | - |
| NVIC_IPRn | [第 B3-630 页的中断优先级寄存器，NVIC_IPR0-NVIC_IPR123](../../part-b/system_address_map/index.md) | - |
| NVIC_ISERn | [第 B3-628 页的中断置使能寄存器，NVIC_ISER0-NVIC_ISER15](../../part-b/system_address_map/index.md) | - |
| NVIC_ISPRn | [第 B3-629 页的中断置未决寄存器，NVIC_ISPR0-NVIC_ISPR15](../../part-b/system_address_map/index.md) | - |
| SCR | [第 B3-603 页的系统控制寄存器，SCR](../../part-b/system_address_map/index.md) | - |
| SHCSR | [第 B3-607 页的系统处理程序控制与状态寄存器，SHCSR](../../part-b/system_address_map/index.md) | - |
| SHPR1 | [第 B3-606 页的系统处理程序优先级寄存器 1，SHPR1](../../part-b/system_address_map/index.md) | - |
| SHPR2 | [第 B3-606 页的系统处理程序优先级寄存器 2，SHPR2](../../part-b/system_address_map/index.md) | - |
| SHPR3 | [第 B3-607 页的系统处理程序优先级寄存器 3，SHPR3](../../part-b/system_address_map/index.md) | - |
| STIR | [第 B3-619 页的软件触发中断寄存器，STIR](../../part-b/system_address_map/index.md) | - |
| SYST_CALIB | [第 B3-623 页的 SysTick 校准值寄存器，SYST_CALIB](../../part-b/system_address_map/index.md) | - |
| SYST_CSR | [第 B3-621 页的 SysTick 控制与状态寄存器，SYST_CSR](../../part-b/system_address_map/index.md) | - |
| SYST_CVR | [第 B3-622 页的 SysTick 当前值寄存器，SYST_CVR](../../part-b/system_address_map/index.md) | - |
| SYST_RVR | [第 B3-622 页的 SysTick 重载值寄存器，SYST_RVR](../../part-b/system_address_map/index.md) | - |
| UFSR | [第 B3-611 页的 UsageFault 状态寄存器，UFSR](../../part-b/system_address_map/index.md) | - |
| VTOR | [第 B3-601 页的向量表偏移寄存器，VTOR](../../part-b/system_address_map/index.md) | - |

## 4. 内存映射的调试寄存器

表 D8-3 是 **Armv7-M** 调试扩展中定义的内存映射调试寄存器主要描述的索引。表中寄存器按本手册中的描述顺序排列。除这些寄存器之外，内存映射调试寄存器还可以包含通用的基础设施寄存器与 **CoreSight** 寄存器。关于这些寄存器的信息参见：

* 第 C1-686 页的 **Armv7-M ROM 表**。
* 附录 D1 **Armv7-M CoreSight 基础设施 ID**。
* 《CoreSight® 体系结构规范》（CoreSight® Architecture Specification）。

表 D8-3 内存映射调试寄存器索引：

| 寄存器ᵃ | 描述，参见 |
| --- | --- |
| DCRDR | [第 C1-704 页的调试内核寄存器数据寄存器，DCRDR](../../part-c/debug/index.md) |
| DCRSR | [第 C1-703 页的调试内核寄存器选择寄存器，DCRSR](../../part-c/debug/index.md) |
| DEMCR | [第 C1-706 页的调试异常与监视控制寄存器，DEMCR](../../part-c/debug/index.md) |
| DFSR | [第 C1-699 页的调试故障状态寄存器，DFSR](../../part-c/debug/index.md) |
| DHCSR | [第 C1-700 页的调试暂停控制与状态寄存器，DHCSR](../../part-c/debug/index.md) |
| DWT_COMPx | [第 C1-745 页的比较器寄存器，DWT_COMPn](../../part-c/debug/index.md) |
| DWT_CPICNT | [第 C1-741 页的 CPI 计数寄存器，DWT_CPICNT](../../part-c/debug/index.md) |
| DWT_CTRL | [第 C1-737 页的控制寄存器，DWT_CTRL](../../part-c/debug/index.md) |
| DWT_CYCCNT | [第 C1-741 页的周期计数寄存器，DWT_CYCCNT](../../part-c/debug/index.md) |
| DWT_EXCCNT | [第 C1-742 页的异常开销计数寄存器，DWT_EXCCNT](../../part-c/debug/index.md) |
| DWT_FOLDCNT | [第 C1-744 页的折叠指令计数寄存器，DWT_FOLDCNT](../../part-c/debug/index.md) |
| DWT_FUNCTIONx | [第 C1-746 页的比较器功能寄存器，DWT_FUNCTIONn](../../part-c/debug/index.md) |
| DWT_LSUCNT | [第 C1-743 页的 LSU 计数寄存器，DWT_LSUCNT](../../part-c/debug/index.md) |
| DWT_MASKx | [第 C1-745 页的比较器屏蔽寄存器，DWT_MASKn](../../part-c/debug/index.md) |
| DWT_PCSR | [第 C1-745 页的程序计数器采样寄存器，DWT_PCSR](../../part-c/debug/index.md) |
| DWT_SLEEPCNT | [第 C1-742 页的睡眠计数寄存器，DWT_SLEEPCNT](../../part-c/debug/index.md) |
| ETM 寄存器 | **ETM** 相关寄存器参见《嵌入式跟踪宏单元体系结构规范》（Embedded Trace Macrocell Architecture Specification）。 |
| FP_COMPn | [第 C1-758 页的闪存补丁比较器寄存器，FP_COMPn](../../part-c/debug/index.md) |
| FP_CTRL | [第 C1-756 页的闪存补丁控制寄存器，FP_CTRL](../../part-c/debug/index.md) |
| FP_REMAP | [第 C1-758 页的闪存补丁重映射寄存器，FP_REMAP](../../part-c/debug/index.md) |
| ITM_STIMn | [第 C1-714 页的激励端口寄存器，ITM_STIM0-ITM_STIM255](../../part-c/debug/index.md) |
| ITM_TCR | [第 C1-716 页的跟踪控制寄存器，ITM_TCR](../../part-c/debug/index.md) |
| ITM_TERn | [第 C1-714 页的跟踪使能寄存器，ITM_TER0-ITM_TER7](../../part-c/debug/index.md) |
| ITM_TPR | [第 C1-715 页的跟踪特权寄存器，ITM_TPR](../../part-c/debug/index.md) |
| TPIU_ACPR | [第 C1-752 页的异步时钟预分频寄存器，TPIU_ACPR](../../part-c/debug/index.md) |
| TPIU_CSPSR | [第 C1-751 页的当前并行端口大小寄存器，TPIU_CSPSR](../../part-c/debug/index.md) |
| TPIU_SPPR | [第 C1-752 页的所选引脚协议寄存器，TPIU_SPPR](../../part-c/debug/index.md) |
| TPIU_SSPSR | [第 C1-751 页的受支持并行端口大小寄存器，TPIU_SSPSR](../../part-c/debug/index.md) |
| TPIU_TYPE | [第 C1-753 页的 TPIU 类型寄存器，TPIU_TYPE](../../part-c/debug/index.md) |

a. 除表中列出的寄存器外，调试支持还包括 ICSR 中的若干位，参见第 B3-599 页的中断控制与状态寄存器，ICSR。
