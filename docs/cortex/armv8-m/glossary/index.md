---
title: "术语表（Glossary）"
---

本文译自 Part G《术语表》（Glossary）。

本页是 Armv8-M 架构参考手册（**DDI0553B.y**，文档 ID **ID09082024**）Part G 术语表的翻译。词条沿用源手册的字母顺序与条目划分，术语名保持英文原文，释义为中文。源手册内部的章节交叉引用（如 `B7.2.3`）保留原编号以便与原书对照，跨文章引用不重新编号。

## A

**AAPCS**
> Arm 架构过程调用标准（**Procedure Call Standard for the Arm Architecture**）。

**Additional floating-point context registers**
> 附加浮点上下文寄存器（Additional floating-point context registers）即附加浮点状态上下文寄存器，包括：
>
> - **S16** 到 **S31**。
>
> 参见：浮点上下文（Floating-point context）。

**Additional state context registers**
> 附加状态上下文寄存器（Additional state context registers）包括：
>
> - **R4** 到 **R11**。
> - 完整性签名（Integrity Signature）。
>
> 参见：状态上下文寄存器（State context registers）。

**Address dependency**
> 当地址依赖（Address dependency）存在时，一次读取返回的值用于计算后续访问的地址。即使第一次读取返回的值并未改变第二次读或写的地址，地址依赖仍然成立。
>
> 参见 B7.2.3 排序与可观测性。

**Addressing mode**
> 寻址模式（Addressing mode）指生成加载/存储指令所用内存地址的方法。

**Aligned**
> 对齐（Aligned）指数据项存储在一个地址上，该地址可被恰好整除其字节大小的 2 的最高次幂整除。因此，对齐的半字、字和双字的地址分别可被 2、4 和 8 整除。
>
> 对齐访问（aligned access）是指该访问的地址按访问中每个元素的大小对齐。

**Application Program Status Register (APSR)**
> 应用程序状态寄存器（APSR）是包含传递指令结果状态信息那些位的寄存器，即 **XPSR** 的 **N**、**Z**、**C** 和 **V** 位。在包含 DSP 扩展的实现中，**APSR** 还包含从 DSP 操作提供状态信息的 **GE** 位。
>
> 参见 B3.5 XPSR、APSR、IPSR 和 EPSR。

**APSR**
> 参见：应用程序状态寄存器（Application Program Status Register）。

**Architecturally executed**
> 只有当一条指令在程序的简单顺序执行中会被执行时，该指令才是架构执行的（architecturally executed）。当这样一条指令被执行并退役时，它已被架构执行。在程序的简单顺序执行中因未通过条件码检查而被视为 **NOP** 的任何指令，也是架构执行的指令。
>
> 在执行推测执行（**Speculative execution**）的 PE 中，如果 PE 丢弃了推测执行的结果，则该指令不是架构执行的。
>
> 参见：条件码检查（Condition code check）、简单顺序执行（Simple sequential execution）。

**Architecturally UNKNOWN**
> 架构未知值（Architecturally UNKNOWN）是指架构未定义、但必须满足 **UNKNOWN** 定义要求的值。实现可以定义该字段的值，但并非必须。
>
> 参见：实现定义（IMPLEMENTATION DEFINED）。

**Architecture tick**
> 架构节拍（Architecture tick）是执行的原子单位。在 Armv8.0-M 架构中，大多数指令都被视为执行的原子单位（它们要么被执行，要么不被执行）。最显著的例外是支持 ICI 行为的指令。

**Associativity**
> 关联性（Associativity）：参见缓存关联性（Cache associativity）。

**Asynchronous exception**
> 异步异常（Asynchronous exception）是指满足下列任一条件的异常：
>
> - 该异常不是直接执行或试图执行指令流所产生的结果。
> - 呈现给异常处理程序的返回地址不保证指示导致该异常的指令。
> - 该异常是非精确的。
>
> 参见：非精确异常（Imprecise exception）、同步异常（Synchronous exception）。

**Atomicity**
> 原子性（Atomicity）描述单副本原子性（single-copy atomicity）或多副本原子性（multi-copy atomicity）。B7.2.1 单副本原子性为 Arm 架构定义了这些原子性形式。
>
> 参见：多副本原子性（Multi-copy atomicity）、单副本原子性（Single-copy atomicity）。

**Attributability**
> 由正在对 PMU 事件计数的 PE 引发的 PMU 事件是可归属的（Attributable）。若 PMU 事件由计数 PMU 事件的 PE 之外的代理引发，则该 PMU 事件是不可归属的（Unattributable）。
>
> PMU 事件要么是可归属的，要么是不可归属的。若 PMU 事件是可归属的，还需进一步定义该 PMU 事件可归属于：
>
> - PE 当前的安全状态。
> - 特权级别。
> - 当 PE 处于调试状态时，调试器通过外部调试接口向 PE 发出的操作。

**Attribution Unit (AU)**
> 归属单元（**Attribution Unit**，**AU**）是安全归属单元（**SAU**）与实现定义归属单元（**IDAU**）的组合。
>
> 参见 B10 章 Armv8-M 受保护内存系统架构。

**AU**
> 参见：归属单元（Attribution unit）。

**Availability**
> 可用性（Availability）是指为正确服务做好准备的程度。

## B

**Background state**
> 后台状态（Background state）是指上一次（前一次）抢占发生之前的 PE 状态。

**Banked register**
> 分组寄存器（Banked register）是具有多个实例的寄存器，使用哪个实例取决于 PE 模式、安全状态或其他 PE 状态。

**Base register**
> 基址寄存器（Base register）是加载/存储指令指定的寄存器，用作该指令地址计算的基准值。根据指令及其寻址模式，可以从基址寄存器的值中加上或减去一个偏移量，以形成发送到内存的地址。

**Base register Write-Back**
> 基址寄存器回写（Base register Write-Back）描述将修改后的值写回地址计算中所用的基址寄存器。

**Baseboard Management Controller**
> 基板管理控制器（Baseboard Management Controller）是专用于系统控制与监控的 PE。

**Beat**
> 节拍（Beat）是对 MVE 向量操作四分之一部分的执行。由于向量长度为 128 位，向量加法指令的一个节拍相当于计算 32 位结果数据。这与通道宽度无关。例如，若通道宽度为 8 位，则向量加法指令的单个节拍将执行四次 8 位加法。
>
> 参见 B5.4 节拍。

**Behaves as if**
> 行为如同（Behaves as if）：当本手册指出 PE 的行为如同（behaves as if）某一条件成立时，必须结合该条件以及影响操作的其他任何条件，重新评估对 PE 操作的所有描述。

**BF branch point**
> BF 分支点（BF branch point）是指两条指令之间的间隙。具体而言，是指紧接在 BF 指令的 `<b_label>` 处指令之前的那条指令，与 BF 指令 `<b_label>` 所标识的指令之间的间隙。
>
> 参见 B3.29 未来分支。

**Big-endian memory**
> 大端内存（Big-endian memory）意味着，例如：
>
> - 字对齐地址处的字节或半字是该地址处字中的最高有效字节或半字。
> - 半字对齐地址处的字节是该地址处半字中的最高有效字节。
>
> 参见 B7.5 字节序、小端内存（Little-endian memory）。

**Blocking**
> 阻塞（Blocking）描述一种不允许后续指令在该操作完成之前执行的操作。非阻塞操作可以允许后续指令在其完成之前执行，并且在遇到异常时不向 PE 发出异常信号。这使实现能够在非阻塞操作执行期间让后续指令退役，而无需保留精确的 PE 状态。

**Branch prediction**
> 分支预测（Branch prediction）是指 PE 选择要沿其取指的将来执行路径。例如，在分支指令之后，PE 可以选择推测性地取指分支之后的指令或分支目标处的指令。
>
> 参见：预取（Prefetching）。

**Breakpoint**
> 断点（Breakpoint）是由执行特定指令触发的调试事件，该指令由指令地址与执行该指令时 PE 的状态中的一项或两项来指定。

**BTI**
> 分支目标识别（**Branch Target Identification**）。用于创建和识别有效分支落点（branch landing pad）的机制。

**BTI clearing**
> 分支目标识别清除指令（Branch Target Identification clearing instruction），即任何将 **EPSR.B** 位清零的指令。

**BTI setting**
> 分支目标识别设置指令（Branch Target Identification setting instruction），即任何将 **EPSR.B** 位置一的指令。

**Byte**
> 字节（Byte）是 8 位数据项。

## C

**Cache associativity**
> 缓存关联性（Cache associativity）是指一个缓存组（cache set）中可分配某一地址的位置数量。每个位置由其路（way）值标识。

**Cache level**
> 缓存层级（Cache level）是指缓存位于缓存层次结构中的位置。在 Arm 架构中，编号较低的层级最靠近 PE。更多信息参见 B7.19 缓存。

**Cache line**
> 缓存行（Cache line）是缓存中的基本存储单元。其按字计的大小始终为 2 的幂，通常为四个或八个字。缓存行必须对齐到适当的内存边界。内存缓存行是与缓存行具有相同大小和对齐方式的一块内存位置。内存缓存行有时被宽泛地称为缓存行。

**Cache sets**
> 缓存组（Cache sets）是缓存中的区域，缓存被划分以简化和加速确定是否发生缓存命中的过程。缓存组的数量始终为 2 的幂。术语 cache sets 是描述缓存存储器的通行约定，该描述不得被视为定义缓存的某种属性。

**Cache way**
> 缓存路（Cache way）由来自每个缓存组的一条缓存行组成。缓存路从 0 编号到（关联性 − 1）。缓存路中的每条缓存行都选择具有与该缓存路相同的索引。例如，缓存路 n 由来自每个缓存组中索引为 n 的缓存行组成。术语 cache way 是描述缓存存储器的通行约定，该描述不得被视为定义缓存的某种属性。

**Cache write-back granule**
> 缓存回写粒度（Cache write-back granule）是指可被覆盖的内存的最大大小。在某些实现中，**CTR** 标识缓存回写粒度。

**Catastrophic failure**
> 灾难性故障（Catastrophic failure）是指其有害后果比正确提供服务所带来的收益高出几个数量级、甚至无法相提并论的故障。

**Chained vector instruction**
> 链式向量指令（Chained vector instruction）是指受逐节拍执行约束的指令。

**Coherence order**
> 一致性顺序（Coherence order）：参见一致性（Coherent）。

**Coherent**
> 若一组观察者对该字节的访问与该组观察者全体对该字节的所有写入存在单一全序这一情形相一致，则该组观察者对内存中某一字节的数据访问是一致性的（coherent）。对该内存位置所有写入的这一单一全序即为该字节的一致性顺序（coherence order）。

**Completer**
> 完成者（Completer）是计算系统中响应并完成由请求者（**Requester**）发起的内存事务的代理。
>
> 参见：请求者（Requester）。

**Condition code check**
> 条件码检查（Condition code check）是确定条件指令正常执行还是被视为 **NOP** 的过程。对于包含条件码字段的指令，将该字段与条件标志比较，以确定该指令是否正常执行。对于 IT 块中的 T32 指令，由 **EPSR.IT** 的值确定该指令是否正常执行。
>
> 参见：条件码字段（Condition code field）、条件标志（Condition flags）、条件执行（Conditional execution）。

**Condition code field**
> 条件码字段（Condition code field）是指令中的 4 位字段，指定该指令执行所依据的条件。
>
> 参见：条件码检查（Condition code check）。

**Condition flags**
> 条件标志（Condition flags）是 **APSR** 或 **XPSR** 的 **N**、**Z**、**C** 和 **V** 位。更多信息参见 B3.5 XPSR、APSR、IPSR 和 EPSR。
>
> 参见：条件码检查（Condition code check）。

**Conditional execution**
> 条件执行（Conditional execution）：当条件指令开始执行时，若条件码检查返回 TRUE，则该指令正常执行；否则被视为 **NOP**。参见 C1.3 条件执行。
>
> 参见：条件码检查（Condition code check）。

**Configuration**
> 配置（Configuration）是指在复位时或紧接复位之后进行的设置，通常预期在程序执行期间保持静态。

**CONSTRAINED UNPREDICTABLE**
> 当一条指令可能导致 **UNPREDICTABLE** 行为时，Armv8 架构规定了一个允许行为的狭窄范围。该范围即 **CONSTRAINED UNPREDICTABLE** 行为的范围。所有符合架构的实现都必须在针对每种具体情况所定义的限值内遵循 **CONSTRAINED UNPREDICTABLE** 行为，且该行为可能有所变化。
>
> 在正文中，术语 **CONSTRAINED UNPREDICTABLE** 以小型大写字母显示。
>
> 参见：不可预测（UNPREDICTABLE）。

**Containable**
> 可抑制的（Containable）是指未被抑制的错误。可抑制错误也称为已抑制错误（Contained error）。

**Context switch**
> 上下文切换（Context switch）是指在不同的线程或进程之间切换时保存和恢复计算状态。在本手册中，术语 context switch 描述操作系统切换上下文的任何情形，其中可能包括也可能不包括地址空间的更改。

**Context synchronization event**
> 上下文同步事件（Context synchronization event）保证对架构中所述任何寄存器的任何更改的可见性。在上下文同步事件之后，对寄存器的已完成写入对于在程序顺序中出现在该上下文同步事件之后的指令的间接读取是可见的。

**Control dependency**
> 当一次读访问返回的数据值决定条件标志，而标志的值又决定后续读访问的地址时，即存在控制依赖（Control dependency）。该地址的确定可能通过条件执行或通过分支求值实现。

**Corrected**
> 已纠正（Corrected）是指由硬件检测到且硬件可纠正的错误。这也称为可纠正错误（Correctable error）。

**Countable error**
> 可计数错误（Countable error）是指由硬件通过递增计数器来检测并记录的错误。

**Cross beat**
> 跨节拍（Cross beat）是指需要来自不同节拍的操作数来产生单个节拍输出的操作。例如，向量加宽操作是跨节拍的，而向量加法不是。

**Cross Trigger Interface**
> 交叉触发接口（Cross Trigger Interface）是一种调试组件，不属于 Armv8-M 架构的组成部分。

**CTI**
> 参见：交叉触发接口（Cross Trigger Interface）。

## D

**DAP**
> 调试访问端口（**Debug Access Port**）。

**Data independent timing**
> 数据无关时序（Data independent timing）是指执行一段代码所需的时间不是所操作数据的函数。
>
> 参见 B3.34 数据无关时序。

**Data Watchpoint and Trace (DWT)**
> 数据观察点与跟踪单元（**Data Watchpoint and Trace**，**DWT**）是 Armv8-M 调试的组件，可选地提供若干跟踪、采样与性能分析功能。
>
> 参见 B14.2 数据观察点与跟踪单元。

**DCB**
> 参见：调试控制块（Debug Control Block）。

**Debug Control Block (DCB)**
> 调试控制块（**Debug Control Block**，**DCB**）是系统控制空间中分配给支持调试功能的寄存器的区域。
>
> 参见：系统控制空间（System Control Space）。

**Debugger**
> 在本手册的大部分内容中，调试器（debugger）指执行调试的任何代理。但手册的某些部分需要更严格的定义，并在局部定义调试器。参见 B13 章 调试。

**Deferred**
> 延迟的（Deferred）是指尚未被静默传播、但不要求生产者立即采取行动的错误。该错误可能已从生产者传递到消费者。

**Deprecated**
> 弃用的（Deprecated）是指为向后兼容而保留在 Arm 架构中的特性。软件应尽可能避免使用弃用的特性。被弃用但并非可选的特性存在于 Arm 架构的当前实现中，但在 Arm 架构的未来版本中可能不存在，或可能被弃用并成为可选的（**OPTIONAL**）。
>
> 参见：可选的（OPTIONAL）。

**Detected**
> 已检测的（Detected）是指已被检测到并向消费者发出信号的错误。

**Detected Uncorrectable**
> 已检测不可纠正（Detected Uncorrectable）是指已检测到、无法纠正并导致故障的错误。

**Digital signal processing (DSP)**
> 数字信号处理（**Digital signal processing**，**DSP**）是处理经采样并转换为数字形式的信号的算法。DSP 算法经常使用饱和运算。

**Direct access**
> 直接访问（Direct access）是指对寄存器的读或写。

**DIT**
> 参见：数据无关时序（Data independent timing）。

**Domain**
> 在 Arm 架构中，域（domain）用于以下语境。
>
> - 共享域（Shareability domain）：定义一个观察者集合，对该集合而言，共享性属性使数据缓存或统一缓存对数据访问透明。
> - 电源域（Power domain）：定义一个具有单一公共电源的逻辑块。

**Double-precision value**
> 双精度值（Double-precision value）由两个连续的 32 位字组成，按 IEEE 浮点算术标准解释为基本双精度浮点数。

**Doubleword**
> 双字（Doubleword）是 64 位数据项。在 Arm 系统中，双字通常至少是字对齐的。

**Doubleword-aligned**
> 双字对齐（Doubleword-aligned）是指地址可被 8 整除。

**DSP**
> 参见：数字信号处理（Digital signal processing）。

**DWT**
> 参见：数据观察点与跟踪单元（Data Watchpoint and Trace）。

## E

**ECC**
> 纠错码（**Error Correction Code**）。

**EDC**
> 检错码（**Error Detection Code**）。

**Effective Value**
> 有效值（Effective Value）：寄存器控制字段，即寄存器中控制行为某一方面的字段，可以描述为具有有效值：
>
> - 在某些情况下，对某一特定控制 a 的描述规定：当控制 a 生效时，它使得寄存器控制字段 b 除对包含控制字段 b 的寄存器的直接读取、或直接读取与直接写入之外，在所有用途上都被视为具有固定值。当控制 a 生效时，该固定值即称为寄存器控制字段 b 的有效值。
> - 在另一些情况下，寄存器控制字段 b 未被实现或不可访问，但 PE 的行为如同控制字段 b 已实现、可访问且具有某一特定值。此时该值即为寄存器控制字段 b 的有效值。
>
> 当某一寄存器控制字段在架构的某一特定版本中引入、而未在更早的架构版本中实现时，它通常在该更早的架构版本中具有有效值。
>
> - 否则，寄存器控制字段的有效值就是该字段的值。

**Element**
> 元素（Element）是指放入通道（lane）中的数据。
>
> 参见：通道（Lane）。

**Embedded Trace Macrocell (ETM)**
> 嵌入式跟踪宏单元（**Embedded Trace Macrocell**，**ETM**）是 Arm CoreSight 调试与跟踪解决方案的组件。ETM 提供对 PE 操作的非侵入式跟踪。
>
> 参见 B14.3 嵌入式跟踪宏单元。

**Endianness**
> 字节序（Endianness）是系统内存映射的一个方面。更多信息参见 B7.5 字节序。
>
> 参见：大端内存（Big-endian memory）与小端内存（Little-endian memory）。

**EPSR**
> 参见：执行程序状态寄存器（Execution Program Status Register）。

**Error**
> 错误（Error）是指偏离正确服务或正确值。

**Error propagation**
> 错误传播（Error propagation）是指将错误从生产者传递到消费者。

**Error record**
> 错误记录（Error record）是指关于某一错误所记录的数据，通常由硬件记录。

**ETM**
> 参见：嵌入式跟踪宏单元（Embedded Trace Macrocell）。

**Exception**
> 异常（Exception）处理某一事件。例如，异常可以处理外部中断或未定义指令。

**Exception vector**
> 异常向量（Exception vector）是包含相应异常处理程序第一条指令地址的固定地址。

**Exception-continuable instruction**
> 异常可继续指令（Exception-continuable instruction）是指任何可导致 PE 置位 **EPSR.ECI** 字段的指令。

**Execution Program Status Register (EPSR)**
> 执行程序状态寄存器（**Execution Program Status Register**，**EPSR**）是包含执行状态位、属于 **XPSR** 一部分的寄存器。
>
> 参见 B3.5 XPSR、APSR、IPSR 和 EPSR。

**Execution stream**
> 执行流（Execution stream）是指按程序的顺序执行本应执行的指令流。

**Explicit access**
> 显式访问（Explicit access）是指由 PE 执行的加载或存储指令所产生的、对内存或内存映射寄存器的读取或写入，或调试器的一次访问。

## F

**Failure**
> 失效（Failure）是指偏离正确服务的事件。

**Fault**
> 故障（Fault）是指因某种形式的系统错误而产生的异常。**BusFault** 可以是 RAS 故障。

**Fault injection**
> 故障注入（Fault injection）是指为测试目的而故意向系统注入故障。

**Fault prevention**
> 故障预防（Fault prevention）是指将系统设计为避免故障。

**Fault removal**
> 故障消除（Fault removal）是指用于检测故障并纠正或规避其影响的逻辑或其他机制。

**Field Replaceable Unit**
> 现场可更换单元（**Field Replaceable Unit**）是指无需返回基地即可更换的最小单元。

**Flash Patch and Breakpoint Unit**
> 闪存补丁与断点单元（**Flash Patch and Breakpoint Unit**）支持在取指时设置断点。
>
> 参见 B14.5 闪存补丁与断点单元。

**Floating-point context**
> 浮点上下文（Floating-point context）如下：
>
> - **S0** 到 **S15**。
> - **FPSCR**。
> - **VPR**。
>
> 参见：附加浮点状态上下文寄存器（Additional floating-point state context registers）。

**Flush-to-zero mode**
> 清零模式（Flush-to-zero mode）是一种处理模式，通过将非规格化操作数与中间结果替换为零来优化某些浮点算法的性能，同时不显著影响其最终结果的精度。

**FPB**
> 参见：闪存补丁与断点单元（Flash Patch and Breakpoint Unit）。

**FRU**
> 参见：现场可更换单元（Field Replaceable Unit）。

## G

**General-purpose registers**
> 通用寄存器（General-purpose registers）是基础指令用于处理的寄存器：
>
> - 通用寄存器为 **R0** 到 **R12**。**R13**、**R14** 分别为 **SP** 和 **LR**。更多信息参见 B3.3 寄存器。
>
> 参见：高寄存器（High registers）、低寄存器（Low registers）。

## H

**Halfword**
> 半字（Halfword）是 16 位数据项。在 Arm 系统中，半字通常是半字对齐的。

**Halfword-aligned**
> 半字对齐（Halfword-aligned）是指地址可被 2 整除。

**Hardware fault**
> 硬件故障（Hardware fault）是指源于硬件或影响硬件的故障。

**High registers**
> 高寄存器（High registers）是指通用寄存器 **R8** 到 **R14**。大多数 16 位 T32 指令无法访问高寄存器。
>
> **注意：** 在某些语境中，高寄存器指 **R8** 到 **R15**，即 **R8** 到 **R14** 以及 **PC**。
>
> 参见：通用寄存器（General-purpose registers）、低寄存器（Low registers）。

## I

**ICI**
> 参见：中断可继续指令（Interrupt-continuable instruction）。

**If-Then block (IT block)**
> If-Then 块（**IT 块**）是指 If-Then（**IT**）指令之后最多四条指令构成的块。块中的每条指令都是条件指令。这些指令的条件要么完全相同，要么部分互为相反。

**Immediate and offset fields**
> 立即数与偏移字段（Immediate and offset fields）除非另有说明，否则为无符号。

**Immediate value**
> 立即数值（Immediate value）是指直接编码在指令中并在执行该指令时用作数值数据的值。许多 T32 指令可以与立即数参数一起使用。

**IMP DEF**
> 实现定义（**IMP DEF**）是一种缩写，用于在图中指示一个或多个位具有**实现定义**行为。

**IMPLEMENTATION DEFINED**
> 实现定义（**IMPLEMENTATION DEFINED**）是指该行为不由架构定义，但必须由各个实现定义并记录在文档中。
>
> 在正文中，术语 **IMPLEMENTATION DEFINED** 以小型大写字母显示。

**Implicit access**
> 隐式访问（Implicit access）是指不属于显式访问的访问。例如：
>
> - 取指。
> - 因异常被引发而设置某一症状标志。
>
> 参见：显式访问（Explicit access）。

**Imprecise exception**
> 非精确异常（Imprecise exception）是指因系统错误而产生的异常。非精确异常在与导致它的指令异步的时刻报告。

**Index register**
> 索引寄存器（Index register）是指某些加载和存储指令中指定的寄存器。该寄存器的值用作偏移量，与基址寄存器的值相加或相减，以形成发送到内存的地址。某些指令形式允许在相加或相减之前对索引寄存器的值进行移位。

**Indirect access**
> 间接访问（Indirect access）是指不属于直接访问的寄存器读取或写入。
>
> 例如，对寄存器的间接写入可能作为执行某条指令的副作用出现，而该指令并不对该寄存器执行直接写入；也可能因外部代理执行的某些操作而出现。
>
> 参见：直接访问（Direct access）。

**Infected**
> 已感染（Infected）是指处于错误状态。

**Inline literals**
> 内联字面量（Inline literals）是保存在与软件本身相同区域中的常量地址和其他数据项。它们由编译器自动生成，也可以出现在汇编代码中。

**Instrumentation Trace Macrocell (ITM)**
> 插桩跟踪宏单元（**Instrumentation Trace Macrocell**，**ITM**）是 Arm CoreSight 调试与跟踪解决方案的组件。ITM 提供内存映射寄存器接口，应用程序可通过它向跟踪汇聚点写入日志字或事件字。
>
> 参见 B14.1 插桩跟踪宏单元。

**Interrupt Program Status Register (IPSR)**
> 中断程序状态寄存器（**Interrupt Program Status Register**，**IPSR**）是提供处理器上正在执行的是应用线程还是异常处理程序这一状态信息的寄存器。若正在执行异常处理程序，该寄存器提供有关异常类型的信息。该寄存器是 **XPSR** 的一部分。
>
> 参见 B3.5 XPSR、APSR、IPSR 和 EPSR。

**Interrupt Service Routine**
> 中断服务例程（**Interrupt Service Routine**）是处理中断的过程。

**Interrupt-continuable instruction**
> 中断可继续指令（Interrupt-continuable instruction）是指可在执行中途被中断的多周期加载或存储指令。中断服务例程完成后，可恢复部分执行的指令的执行，而该指令无需从头重新开始。多周期加载或存储指令的中断将使 PE 置位 **EPSR.ICI** 字段。
>
> 参见：异常可继续指令（Exception-continuable instruction）。

**Interworking**
> 交互工作（Interworking）是指允许在 Armv8-A 架构中使用 A32 与 T32 指令集的软件之间进行分支的方法。对于 Armv8-M，交互工作在 C1.4.7 指令集、交互工作与状态交互支持 中描述。

**IPSR**
> 参见：中断程序状态寄存器（Interrupt Program Status Register）。

**Isolation**
> 隔离（Isolation）是指将错误的影响仅限制在真正尝试使用已损坏数据的组件上。

**ISR**
> 参见：中断服务例程（Interrupt Service Routine）。

**ITM**
> 参见：插桩跟踪宏单元（Instrumentation Trace Macrocell）。

## L

**Landing pad**
> 落点（Landing pad）是指 BTI 落点指令。落点指令是 BTI 清除指令。
>
> 并非所有将 **EPSR.B** 位清零的操作都是落点。例如，**EPSR.B** 在异常进入时被自动清零，但该操作不是落点，也不是 BTI 清除指令。
>
> 下列指令是有效的 BTI 落点：
>
> - **BTI**。
> - **SG**。
> - **PACBTI**。

**Lane**
> 通道（Lane）是向量寄存器或向量操作的一个区段。

**Latent fault**
> 潜在故障（Latent fault）是指存在于系统中但尚未被检测到的错误。

**Level**
> 层级（Level）：参见缓存层级（Cache level）。

**Level of Coherence (LoC)**
> 一致性层级（**Level of Coherence**，**LoC**）是指清理或无效化到一致性点时，必须被清理或无效化的最后一级缓存。
>
> 参见：缓存层级（Cache level）、一致性点（Point of Coherency）。

**Level of Unification, Inner Shareable (LoUIS)**
> 内部共享统一层级（**Level of Unification, Inner Shareable**，**LoUIS**）是指清理或无效化到内部共享共享域的统一点时，必须被清理或无效化的最后一级缓存。
>
> 参见：缓存层级（Cache level）、统一点（Point of Unification）。

**Level of Unification, uniprocessor (LoUU)**
> 单处理器统一层级（**Level of Unification, uniprocessor**，**LoUU**）对于某一 PE 而言，是指清理或无效化到该 PE 的统一点时，必须被清理或无效化的最后一级缓存。
>
> 参见：缓存层级（Cache level）、统一点（Point of Unification）。

**Line**
> 行（Line）：参见缓存行（Cache line）。

**Little-endian memory**
> 小端内存（Little-endian memory）意味着，例如：
>
> - 字对齐地址处的字节或半字是该地址处字中的最低有效字节或半字。
> - 半字对齐地址处的字节是该地址处半字中的最低有效字节。
>
> 参见：大端内存（Big-endian memory）、B7.5 字节序。

**Load/store architecture**
> 加载/存储架构（Load/store architecture）是指数据处理操作仅作用于寄存器内容、而不直接作用于内存内容的架构。

**LoC**
> 参见：一致性层级（Level of Coherence）。

**Lockup**
> 锁死（Lockup）是指一种 PE 状态：PE 因某一错误而停止执行指令，且由于当前执行优先级，无法将错误上报给适当的 **HardFault** 处理程序。更多信息参见 B3.33 锁死。

**LoUIS**
> 参见：内部共享统一层级（Level of Unification, Inner Shareable）。

**LoUU**
> 参见：单处理器统一层级（Level of Unification, uniprocessor）。

**Low registers**
> 低寄存器（Low registers）是指通用寄存器 **R0** 到 **R7**。与高寄存器不同，所有 T32 指令都可访问低寄存器。

**LR hazard**
> LR 冒险（LR hazard）是指当另一条指令（**LE** 或 **LETP** 除外）正在访问 **LR** 时写入 **LR** 的情形。

## M

**M-Profile Vector Extension**
> M 类向量扩展（**M-Profile Vector Extension**）是 Armv8.1-M 架构的可选部分，同时支持整数与浮点数据类型。

**Memory barriers**
> 内存屏障（Memory barriers）是对强制 PE 在退役加载/存储指令方面产生同步事件的指令或指令序列的统称。更多信息参见 B7.2.9 内存屏障。

**Memory coherency**
> 内存一致性（Memory coherency）是指确保当某个内存位置被读取（无论是数据读取还是取指）时，实际获得的值始终是最近写入该位置的值这一问题。当存在多个可能的物理位置（例如主存以及写缓冲和一个或多个缓存层级中的至少一个）时，这可能很困难。

**Memory hint**
> 内存提示（Memory hint）指令向内存系统提供有关将来内存访问的提前信息，而实际上并不向寄存器堆加载或存储任何数据。**PLD** 和 **PLI** 是 Armv8-M 中定义的仅有的内存提示指令。

**Memory Protection Unit (MPU)**
> 内存保护单元（**Memory Protection Unit**，**MPU**）是一种硬件单元，其寄存器对内存中数量有限的一些保护区域提供简单控制，更多信息参见 B10 章 Armv8-M 受保护内存系统架构。

**Minor failure**
> 轻微失效（Minor failure）是指其有害后果与正确提供服务所带来的收益代价相当的失效。

**MPU**
> 参见 B10 章 Armv8-M 受保护内存系统架构。

**Multi-copy atomicity**
> 多副本原子性（Multi-copy atomicity）是 B7.2.2 多副本原子性 中描述的原子性形式。
>
> 参见：原子性（Atomicity）、单副本原子性（Single-copy atomicity）。

**MVE**
> 参见：M 类向量扩展（M-Profile Vector Extension）。

## N

**NaN**
> 非数（**Not a Number**，**NaN**）是指既不适合用数值、也不适合用无穷表示时可使用的浮点值。NaN 可以是安静 NaN（quiet NaN），它在大多数浮点操作中传播；也可以是信号 NaN（signaling NaN），它在被使用时引发无效操作浮点异常。更多信息参见 IEEE 浮点算术标准。

**Node**
> 节点（Node）是指检测到错误的组件。

**Non-Return-to-Zero (NRZ)**
> 不归零（**Non-Return-to-Zero**，**NRZ**）是一种用于异步通信端口的物理层信号方案。

**NRZ**
> 参见：不归零（Non-Return-to-Zero）。

## O

**Obsolete**
> 过时（Obsolete）表示 Arm 不再支持的事物。当某一架构特性被描述为过时时，表示架构不再支持该特性，尽管架构的较早版本曾支持它。

**Offset addressing**
> 偏移寻址（Offset addressing）是指通过向基址寄存器的值加上或减去偏移量来形成内存地址。

**OPTIONAL**
> 当用于某一架构特性时，**OPTIONAL**（可选的）表示该特性是 Arm 架构实现中非必需的特性：
>
> - 若某一特性是 **OPTIONAL** 且已被弃用，则表示该特性正在被逐步淘汰出架构。Arm 期望此类特性仅在有已知的向后兼容理由时才被纳入新的实现中。既为 **OPTIONAL** 又已弃用的特性在架构的未来版本中可能不存在。
> - 既为 **OPTIONAL** 又未被弃用的特性，通常是 Arm 架构某一版本在该版本首次发布之后新增的特性。Arm 建议在架构的所有新实现中纳入此类特性。
>
> 在正文中，术语 **OPTIONAL** 的这些含义以小型大写字母显示。
>
> **注意：** 不要将 **OPTIONAL** 的这些 Arm 专有用法与 **OPTIONAL** 的其他用法混淆，后者具有其通常含义。这些用法包括：
>
> - 许多指令语法中的可选参数。
> - 由实现选择所决定的行为。
>
> 参见：弃用的（Deprecated）。

## P

**PAC**
> 指针认证码（**Pointer Authentication Code**）是由密码算法生成的散列值。PAC 也指用于生成该散列值的过程。

**PE**
> 参见：处理单元（Processing element）。

**Performance Monitoring Unit**
> 性能监控单元（Performance Monitoring Unit）是可选的非侵入式调试组件，允许识别并计数事件。参见 B15 章 性能监控器扩展。

**Persistent fault**
> 持久故障（Persistent fault）是指非瞬态的故障。

**Physical address (PA)**
> 物理地址（**Physical address**，**PA**）是标识物理内存映射中某一位置的地址。

**PMU**
> 参见：性能监控单元（Performance Monitoring Unit）。

**PoC**
> 参见：一致性点（Point of Coherency）。

**Point of coherency (PoC)**
> 对于某一特定 PA，一致性点（**Point of coherency**，**PoC**）是指所有可访问内存的代理都保证能看到某一内存位置的同一副本的那个点。

**Point of unification (PoU)**
> 对于某一特定 PE，统一点（**Point of unification**，**PoU**）是指该 PE 的指令缓存与数据缓存保证能看到某一内存位置的同一副本的那个点。

**Poisoned**
> 已污染（Poisoned）是指已被标记为处于错误状态，从而使该状态的后续消耗向消费者发出已检测错误的信号。

**Post-indexed addressing**
> 后变址寻址（Post-indexed addressing）是指内存地址即基址寄存器的值，但会向基址寄存器的值加上或减去偏移量，并将结果写回基址寄存器。

**PoU**
> 参见：统一点（Point of Unification）。

**PPB**
> 私有外设总线（**Private Peripheral Bus**）。

**Pre-indexed addressing**
> 前变址寻址（Pre-indexed addressing）是指内存地址按与偏移寻址相同的方式形成，但该内存地址也会写回基址寄存器。

**Precise exception**
> 当异常处理程序收到的 PE 状态与内存系统状态，与 PE 已执行指令流中直至（但不包括）取证异常之处为止的所有指令、而未执行其后的任何指令这一情形相一致时，该异常被描述为精确的（precise）。

**Prefetching**
> 预取（Prefetching）是指从内存系统推测性地取指或取数据。特别地，指令预取是指在程序的简单顺序执行中先于其的指令尚未执行完毕之前从内存取指的过程。预取一条指令并不意味着该指令必须被执行。
>
> 在本手册中，除非上下文明确表示另有含义，否则对指令或数据取指的引用也适用于预取。
>
> 参见：简单顺序执行（Simple sequential execution）。

**Privileged access**
> 特权访问（Privileged access）：内存系统通常区分特权访问与非特权访问，并对非特权访问支持更严格的权限。某些指令只能由特权软件使用。

**Processing element (PE)**
> 处理单元（**Processing element**，**PE**）是 Arm 架构中定义的抽象机器，如 Arm 架构参考手册所述。符合 Arm 架构的 PE 实现必须遵循相应 Arm 架构参考手册中所述的行为。

**Program Status Registers (XPSR)**
> 程序状态寄存器（**Program Status Registers**，**XPSR**）是用于描述将 **APSR**、**EPSR** 和 **IPSR** 组合为单个 32 位程序状态寄存器的术语。
>
> 参见 B3.5 XPSR、APSR、IPSR 和 EPSR。

**Protection granule**
> 保护粒度（Protection granule）是指 **EDC** 或 **ECC** 为其提供检测或纠正的内存单位。

**Protection region**
> 保护区域（Protection region）是指其位置、大小及其他属性由内存保护单元寄存器定义的内存区域。

**Protection Unit**
> 保护单元（Protection Unit）：参见内存保护单元（Memory Protection Unit）。

**Pseudo-instruction**
> 伪指令（Pseudo-instruction）是指汇编为某一指令编码、且预期反汇编为另一种汇编语法的 UAL 汇编语法，并在本手册中按该另一种语法描述。例如，`MOV<Rd>,<Rm>,LSL #<n>` 是一条伪指令，预期反汇编为 `LSL <Rd>,<Rm>,#<n>`。
>
> 参见 C1 章 指令集概述。

## Q

**Quadword**
> 四字（Quadword）是 128 位数据项。在 Arm 系统中，四字通常至少是字对齐的。

**Quadword-aligned**
> 四字对齐（Quadword-aligned）是指地址可被 16 整除。

**Quiet NaN**
> 安静 NaN（Quiet NaN）是指在大多数浮点操作中保持不变地传播的 NaN。

## R

**RAO**
> 参见：读取为一（Read-As-One）。

**RAO/SBOP**
> 在 Armv8 之前的 Arm 架构版本中，指读取为一、写入时应为一或保持（Read-As-One, Should-Be-One-or-Preserved on writes）。在 Armv8 中，**RES1** 取代了这一描述。
>
> 参见：UNK/SBOP、读取为一（Read-As-One）、**RES1**、写入时应为零或保持（Should-Be-One-or-Preserved, SBOP）。

**RAO/WI**
> 读取为一、写入忽略（Read-As-One, Writes Ignored）。
>
> 硬件必须将该字段实现为读取为一，并必须忽略对该字段的写入。
>
> 软件可以依赖该字段读取为全 1，并依赖写入被忽略。
>
> 该描述可适用于读取为 1 的单个位，或读取为全 1 的字段。
>
> 参见：读取为一（Read-As-One）。

**RAS**
> 可靠性、可用性与可维护性（**Reliability, Availability, and Serviceability**）。参见 B16 章 可靠性、可用性与可维护性（RAS）扩展。

**RAZ**
> 参见：读取为零（Read-As-Zero）。

**RAZ/SBZP**
> 在 Armv8 之前的 Arm 架构版本中，指读取为零、写入时应为零或保持（Read-As-Zero, Should-Be-Zero-or-Preserved on writes）。在 Armv8 中，**RES0** 取代了这一描述。
>
> 参见：UNK/SBZP、读取为零（Read-As-Zero）、**RES0**、写入时应为零或保持（Should-Be-Zero-or-Preserved, SBZP）。

**RAZ/WI**
> 读取为零、写入忽略（Read-As-Zero, Writes Ignored）。
>
> 硬件必须将该字段实现为读取为零，并必须忽略对该字段的写入。
>
> 软件可以依赖该字段读取为全 0，并依赖写入被忽略。
>
> 该描述可适用于读取为 0 的单个位，或读取为全 0 的字段。
>
> 参见：读取为零（Read-As-Zero）。

**Read, modify, write**
> 读-改-写（Read, modify, write）指令序列是指：将某一值读入通用寄存器，在该寄存器中更新相关字段，然后写回新值。

**Read-allocate cache**
> 读分配缓存（Read-allocate cache）是指在读取数据发生缓存未命中时，导致向缓存中分配一条缓存行的缓存。

**Read-As-One (RAO)**
> 读取为一（**Read-As-One**，**RAO**）：硬件必须将该字段实现为读取为全 1。
>
> 软件：
>
> - 可以依赖该字段读取为全 1。
> - 必须使用 SBOP 策略写入该字段。
>
> 该描述可适用于读取为 1 的单个位，或读取为全 1 的字段。它仅适用于只读的位或字段。
>
> 参见：RAO/SBOP、RAO/WI、**RES1**。

**Read-As-Zero (RAZ)**
> 读取为零（**Read-As-Zero**，**RAZ**）：硬件必须将该字段实现为读取为全 0。
>
> 软件：
>
> - 可以依赖该字段读取为全 0。
> - 必须使用 SBZP 策略写入该字段。
>
> 该描述可适用于读取为 0 的单个位，或读取为全 0 的字段。它仅适用于只读的位或字段。
>
> 参见：RAZ/SBZP、RAZ/WI、**RES0**。

**Recoverable**
> 可恢复（Recoverable）是指必须被纠正、以使系统或系统较小部分的正确运行得以继续的可抑制错误。
>
> 参见 B16.3 产生错误异常。

**Register data dependency**
> 当满足下列任一条件时，第一个数据值与第二个数据值之间即存在寄存器数据依赖（Register data dependency）：
>
> - 保存第一个数据值的寄存器用于计算第二个数据值，且第一个数据值与第二个数据值之间的计算不包含下列任一项：
>   - 条件由第一个数据值决定的条件分支。
>   - 条件由第一个数据值决定的条件选择、移动或运算，且该选择、移动或运算的输入数据值与第一个数据值之间不存在数据依赖。
> - 第一个数据值与第三个数据值之间、以及第三个数据值与第二个数据值之间均存在寄存器数据依赖。
>
> 参见 B7.2.3 排序与可观测性。

**Reliability**
> 可靠性（Reliability）是指正确服务的连续性。

**Requester**
> 请求者（Requester）是计算系统中能够发起内存事务的代理。
>
> 参见：完成者（Completer）。

**RES0**
> **RES0** 是指具有应为零或保持（Should-Be-Zero-or-Preserved）行为、或具有等效的只读或只写行为的保留位或保留字段。用于寄存器描述中的字段，以及保存在内存中的架构定义的数据结构中的字段。
>
> 在架构中，存在某些情形：某一寄存器位或字段：
>
> - 在某一已定义的架构语境中为 **RES0**。
> - 在不同的架构语境中具有不同的已定义行为。
>
> **注意：** **RES0** 不用于指令编码的描述。
>
> 这意味着读/写寄存器中字段的 **RES0** 定义为：
>
> 若某一位在所有语境中均为 **RES0**
>
> 对于读/写寄存器中的某一位，下列哪一情形成立是实现定义的：
>
> 1. 该位硬连线为 0。此时：
>    - 对该位的读取始终返回 0。
>    - 对该位的写入被忽略。
> 2. 该位可被写入。此时：
>    - 对寄存器的间接写入将该位置为 0。
>    - 对该位的读取返回最近一次通过直接或间接写入成功写入该位的值。若该位自复位以来未被成功写入，则该位的读取返回复位值（若有），否则返回 **UNKNOWN** 值。
>    - 对该位的直接写入必须更新与该位关联的存储位置。
>    - 除非本手册明确为该位定义附加属性，否则该位的值除决定从该位读回的值之外，不得对 PE 的操作产生任何影响。
>
> **RES0** 位或字段遵循行为 1 还是行为 2，是逐位实现定义的。
>
> 若某一位仅在某些语境中为 **RES0**
>
> 对于读/写寄存器中的某一位，当该位被描述为 **RES0** 时：
>
> - 对寄存器的间接写入将该位置为 0。
> - 对该位的读取必须返回最近一次成功写入该位的值（无论通过直接还是间接写入），与该位写入时寄存器的用途无关。若该位自复位以来未被成功写入，则该位的读取返回复位值（若有），否则返回 **UNKNOWN** 值。
> - 对该位的直接写入必须更新与该位关联的存储位置。
> - 当寄存器的用途使该位被描述为 **RES0** 时，除非本手册明确为该位定义附加属性，否则该位的值除决定从该位读回的值之外，不得对 PE 的操作产生任何影响。
>
> 仅考虑适用于某一特定实现的语境：若某一位在某一语境中被定义为 **RES0**、在另一语境中被定义为 **RES1**，且不存在该位被定义为功能位的语境，则下列哪一情形成立是实现定义的：
>
> - 对该位的写入被忽略，对该位的读取返回 **UNKNOWN** 值。
> - 该位的值可被写入，读取返回最近一次写入该位的值。
>
> **RES0** 的描述可适用于只读的位或字段，也可适用于只写的位或字段：
>
> - 对于只读位，**RES0** 表示该位读取为 0，但软件必须将该位视为 **UNKNOWN**。
> - 对于只写位，**RES0** 表示软件必须将该位视为 **SBZ**。
>
> 在某一语境中为 **RES0** 的位是为该语境中的将来用途而保留的。为保持向前兼容，软件：
>
> - 不得依赖该位读取为 0。
> - 必须使用 SBZP 策略写入该位。
>
> 该 **RES0** 描述可适用于单个位，也可适用于其每一位都必须被视为 **RES0** 的字段。
>
> 在正文中，术语 **RES0** 以小型大写字母显示。
>
> 参见：读取为零（Read-As-Zero）、**RES1**、应为零或保持（Should-Be-Zero-or-Preserved）、**UNKNOWN**。

**RES0H**
> **RES0H** 是指具有应为零或保持（**SBZP**）行为的保留位或保留字段。该行为使用 **RES0** 定义中"硬连线为 0"的子集。

**RES1**
> **RES1** 是指具有应为一或保持（Should-Be-One-or-Preserved）行为、或具有等效的只读或只写行为的保留位或保留字段。用于寄存器描述中的字段，以及保存在内存中的架构定义的数据结构中的字段。
>
> 在架构中，存在某些情形：某一寄存器位或字段：
>
> - 在某一已定义的架构语境中为 **RES1**。
> - 在不同的架构语境中具有不同的已定义行为。
>
> **注意：** **RES1** 不用于指令编码的描述。
>
> 这意味着读/写寄存器中字段的 **RES1** 定义为：
>
> 若某一位在所有语境中均为 **RES1**
>
> 对于读/写寄存器中的某一位，下列哪一情形成立是实现定义的：
>
> 1. 该位硬连线为 1。此时：
>    - 对该位的读取始终返回 1。
>    - 对该位的写入被忽略。
> 2. 该位可被写入。此时：
>    - 对寄存器的间接写入将该位置为 1。
>    - 对该位的读取返回最近一次通过直接或间接写入成功写入该位的值。若该位自复位以来未被成功写入，则该位的读取返回复位值（若有），否则返回 **UNKNOWN** 值。
>    - 对该位的直接写入必须更新与该位关联的存储位置。
>    - 除非本手册明确为该位定义附加属性，否则该位的值除决定从该位读回的值之外，不得对 PE 的操作产生任何影响。
>
> **RES1** 位或字段遵循行为 1 还是行为 2，是逐位实现定义的。
>
> 若某一位仅在某些语境中为 **RES1**
>
> 对于读/写寄存器中的某一位，当该位被描述为 **RES1** 时：
>
> - 对寄存器的间接写入将该位置为 1。
> - 对该位的读取必须返回最近一次成功写入该位的值，与该位写入时寄存器的用途无关。
>
> **注意：** 如本列表所示，该值可能由对寄存器的间接写入而写入。
>
> 若该位自复位以来未被成功写入，则该位的读取返回复位值（若有），否则返回 **UNKNOWN** 值。
>
> - 对该位的直接写入必须更新与该位关联的存储位置。
> - 当寄存器的用途使该位被描述为 **RES1** 时，除非本手册明确为该位定义附加属性，否则该位的值除决定从该位读回的值之外，不得对 PE 的操作产生任何影响。
>
> 仅考虑适用于某一特定实现的语境：若某一位在某一语境中被定义为 **RES0**、在另一语境中被定义为 **RES1**，且不存在该位被定义为功能位的语境，则下列哪一情形成立是实现定义的：
>
> - 对该位的写入被忽略，对该位的读取返回 **UNKNOWN** 值。
> - 该位的值可被写入，读取返回最近一次写入该位的值。
>
> **RES1** 的描述可适用于只读的位或字段，也可适用于只写的位或字段：
>
> - 对于只读位，**RES1** 表示该位读取为 1，但软件必须将该位视为 **UNKNOWN**。
> - 对于只写位，**RES1** 表示软件必须将该位视为 **SBO**。
>
> 在某一语境中为 **RES1** 的位是为该语境中的将来用途而保留的。为保持向前兼容，软件：
>
> - 不得依赖该位读取为 1。
> - 必须使用 SBOP 策略写入该位。
>
> 该 **RES1** 描述可适用于单个位，也可适用于其每一位都必须被视为 **RES1** 的字段。
>
> 在正文中，术语 **RES1** 以小型大写字母显示。
>
> 参见：读取为一（Read-As-One）、**RES0**、应为一或保持（Should-Be-One-or-Preserved）、**UNKNOWN**。

**RES1H**
> **RES1H** 是指具有应为一或保持（**SBOP**）行为的保留位或保留字段。该行为使用 **RES1** 定义中"硬连线为 1"的子集。

**Reserved**
> 保留（Reserved）除非另有说明，否则：
>
> - 保留的指令或访问保留寄存器的指令具有 **UNPREDICTABLE** 或 **CONSTRAINED UNPREDICTABLE** 行为。
> - 被描述为保留的位位置为：
>   - 在 RW 或 WO 寄存器中，为 **RES0**。
>   - 在 RO 寄存器中，为 **UNK**。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**RES0**、**RES1**、**UNDEFINED**、**UNK**、**UNPREDICTABLE**。

**Restartable**
> 可重启（Restartable）是指不立即影响正确运行的可抑制错误。通常这指系统的正确运行，但也可在其他语境中用于描述较小部分的正确运行。
>
> 参见 B16.3 产生错误异常。

**Return Link**
> 返回链接（Return Link）是指与返回地址相关的值。

**RISC**
> 精简指令集计算机（**Reduced Instruction Set Computer**）。

**Rounding error**
> 舍入误差（Rounding error）是指算术运算舍入结果的值减去该运算精确结果的值。

**Rounding mode**
> 舍入模式（Rounding mode）指定浮点运算的精确结果如何舍入为目标格式中可表示的值。舍入模式由 IEEE 浮点算术标准定义。

## S

**Saturated arithmetic**
> 饱和算术（Saturated arithmetic）是指这样一种整数算术：结果若超出可表示的最大数，则置为可表示的最大数；结果若小于可表示的最小数，则置为可表示的最小数。有符号饱和算术常用于 DSP 算法。它与 Arm 处理器中所用的常规有符号整数算术形成对照——后者的溢出结果会从 +2³¹−1 回绕到 −2³¹ 或反向回绕。

**SBO**
> 参见：应为一（Should-Be-One）。

**SBOP**
> 参见：应为一或保持（Should-Be-One-or-Preserved）。

**SBZ**
> 参见：应为零（Should-Be-Zero）。

**SBZP**
> 参见：应为零或保持（Should-Be-Zero-or-Preserved）。

**Security hole**
> 安全漏洞（Security hole）是指这样一种机制：借助它，在当前特权级别执行的代码可以达成在使用非 **UNPREDICTABLE**、非 **CONSTRAINED UNPREDICTABLE** 指令的情况下于当前或更低特权级别无法达成的结果。Arm 架构禁止安全漏洞。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**UNPREDICTABLE**。

**Self-modifying code**
> 自修改代码（Self-modifying code）是指向内存写入一条或多条指令、随后执行这些指令的代码。使用自修改代码时，必须使用缓存维护与屏障指令以确保同步。

**Serial Wire Output (SWO)**
> 串行线输出（**Serial Wire Output**，**SWO**）是支持 NRZ 与曼彻斯特编码之一或其全部的异步 TPIU 端口。

**Serial Wire Viewer (SWV)**
> 串行线查看器（**Serial Wire Viewer**，**SWV**）是 SWO 与 DWT 单元或 ITM 中至少一个的组合，提供数据跟踪能力。

**Service failure mode**
> 服务失效模式（Service failure mode）是指为减轻错误严重程度而进入的模式。

**Serviceability**
> 可维护性（Serviceability）是指接受修改与修复的能力。

**Set**
> 组（Set）：参见缓存组（Cache sets）。

**Should-Be-One (SBO)**
> 应为一（**Should-Be-One**，**SBO**）：硬件必须忽略对该字段的写入。
>
> Arm 强烈建议软件将该字段写为全 1。若软件写入的值不是全 1，则必须预期得到 **UNPREDICTABLE** 或 **CONSTRAINED UNPREDICTABLE** 的结果。
>
> 该描述可适用于应写为 1 的单个位，或应写为全 1 的字段。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**UNPREDICTABLE**。

**Should-Be-One-or-Preserved (SBOP)**
> 应为一或保持（**Should-Be-One-or-Preserved**，**SBOP**）：自 Armv8 架构引入起，应为一或保持的描述已被 **RES1** 取代。
>
> 硬件必须忽略对该字段的写入。
>
> 若软件自实现该字段的 PE 上次复位并初始化以来已读取过该字段，则必须通过写入其先前从该字段读取的值来保持该字段的值；否则必须将该字段写为全 1。
>
> 若软件向该字段写入的值既不是先前为该字段读取的值、也不是全 1，则必须预期得到 **UNPREDICTABLE** 或 **CONSTRAINED UNPREDICTABLE** 的结果。
>
> 该描述可适用于应写为其保持值或写为 1 的单个位，或应写为其保持值或写为全 1 的字段。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**UNPREDICTABLE**。

**Should-Be-Zero (SBZ)**
> 应为零（**Should-Be-Zero**，**SBZ**）：硬件必须忽略对该字段的写入。
>
> Arm 强烈建议软件将该字段写为全 0。若软件写入的值不是全 0，则必须预期得到 **UNPREDICTABLE** 或 **CONSTRAINED UNPREDICTABLE** 的结果。
>
> 该描述可适用于应写为 0 的单个位，或应写为全 0 的字段。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**UNPREDICTABLE**。

**Should-Be-Zero-or-Preserved (SBZP)**
> 应为零或保持（**Should-Be-Zero-or-Preserved**，**SBZP**）：自 Armv8 架构引入起，应为零或保持的描述已被 **RES0** 取代。
>
> 硬件必须忽略对该字段的写入。
>
> 若软件自实现该字段的 PE 上次复位并初始化以来已读取过该字段，则必须通过写入其先前从该字段读取的值来保持该字段的值；否则必须将该字段写为全 0。
>
> 若软件向该字段写入的值既不是先前为该字段读取的值、也不是全 0，则必须预期得到 **UNPREDICTABLE** 或 **CONSTRAINED UNPREDICTABLE** 的结果。
>
> 该描述可适用于应写为其保持值或写为 0 的单个位，或应写为其保持值或写为全 0 的字段。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**UNPREDICTABLE**。

**Signaling NaNs**
> 信号 NaN（Signaling NaNs）在任何浮点运算把信号 NaN 作为操作数接收时引发无效操作异常。信号 NaN 可用于调试，以追查某些未初始化变量的使用。

**Signed data types**
> 有符号数据类型（Signed data types）使用补码格式表示范围为 −2<sup>N−1</sup> 到 +2<sup>N−1</sup>−1 的整数。

**Signed immediate and offset fields**
> 有符号立即数与偏移字段（Signed immediate and offset fields）除非另有说明，否则以补码记法编码。

**Silent data corruption**
> 静默数据损坏（Silent data corruption）是指未被硬件或软件检测到的错误。

**Silently propagated**
> 静默传播（Silently propagated）是指错误在传递过程中未被作为已检测错误发出信号。

**SIMD**
> 单指令多数据（**Single-Instruction, Multiple-Data**）。

**Simple sequential execution**
> 简单顺序执行（Simple sequential execution）是指这样一种实现的行为：取指、译码并完全执行每一条指令之后才继续下一条指令。此类实现不进行任何对内存（包括对指令内存）的推测访问。该实现不对执行的任何阶段进行流水化。在实践中，这是架构所基于的理论执行模型，Arm 并不期望该模型对应于架构的现实实现。

**Single peripheral**
> 单一外设（Single peripheral）是指由该外设定义的、大小为**实现定义**的内存区域。

**Single-copy atomicity**
> 单副本原子性（Single-copy atomicity）是 B7.2.1 单副本原子性 中描述的原子性形式。
>
> 参见：原子性（Atomicity）、多副本原子性（Multi-copy atomicity）。

**Single-precision value**
> 单精度值（Single-precision value）是指按 IEEE 浮点算术标准解释为基本单精度浮点数的 32 位字。

**Software fault**
> 软件故障（Software fault）是指源于软件并影响软件的故障。

**Spatial locality**
> 空间局部性（Spatial locality）是指这样一种观察到的效应：程序访问某一内存位置之后，很可能在不久的将来也访问附近的内存位置。具有多字缓存行的缓存利用该效应以提高性能。

**Special-purpose register**
> 专用寄存器（Special-purpose register）是指特定的一组寄存器之一：对该寄存器的所有直接与间接读写相对于其他指令都表现为按程序顺序发生，而无需任何显式同步。更多信息参见 B3.3 寄存器。

**Speculative writes**
> 推测写入（Speculative writes）以下情形均属之：
>
> - 由位于尚未经架构解决的分支之后、出现在执行流中的存储指令所产生的写入。
>
> - 由位于同步异常条件尚未经架构解决的指令之后、出现在执行流中的存储指令所产生的写入。
>
> - 由条件尚未经架构解决的条件存储指令所产生的写入。
>
> - 由所写数据来自尚未经架构提交的寄存器的存储指令所产生的写入。

**State context registers**
> 状态上下文寄存器（State context registers）如下：
>
> - **R0** 到 **R3**。
> - **R12**。
> - **LR**。
> - **RETPSR**。
> - 返回地址（ReturnAddress）。
>
> 参见：附加状态上下文寄存器（Additional state context registers）。

**Synchronous exception**
> 当下列条件全部成立时，异常被描述为同步的（synchronous）：
>
> - 该异常是直接执行或试图执行指令流所产生的结果。
> - 呈现给异常处理程序的返回地址保证指示导致该异常的指令。
> - 该异常是精确的。
>
> 参见：异步异常（Asynchronous exception）、精确异常（Precise exception）。

**System Control Block (SCB)**
> 系统控制块（**System Control Block**，**SCB**）是系统控制空间中的一个地址区域，用于与异常模型相关的关键特性控制与配置。
>
> 参见：系统控制空间（System Control Space）。

**System Control Space (SCS)**
> 系统控制空间（**System Control Space**，**SCS**）是内存映射中为系统控制与配置寄存器保留的区域。
>
> 参见：调试控制块（Debug Control Block）、B8.3 系统控制空间（SCS）。

## T

**T32 instruction**
> T32 指令是指定 PE 要执行的操作的一个或两个半字。T32 指令必须是半字对齐的。更多信息参见 C1 章 指令集概述。
>
> T32 指令以前称为 Thumb 指令。

**Tail-chaining**
> 尾链（Tail-chaining）是一种消除出栈与压栈操作的优化。更多信息参见 B3.26 尾链。

**Temporal locality**
> 时间局部性（Temporal locality）是指这样一种观察到的效应：程序访问某一内存位置之后，很可能在不久的将来再次访问同一内存位置。缓存利用该效应以提高性能。

**TPIU**
> 参见：跟踪端口接口单元（Trace Port Interface Unit）。

**Trace Port Interface Unit (TPIU)**
> 跟踪端口接口单元（**Trace Port Interface Unit**，**TPIU**）是 Arm CoreSight 调试与跟踪解决方案的组件。TPIU 为处理器实现中的一个或多个跟踪源提供外部接口。
>
> 参见 B14.4 跟踪端口接口单元。

**Transient fault**
> 瞬态故障（Transient fault）是指非持久的故障。

## U

**UAL**
> 参见：统一汇编语言（Unified Assembler Language）。

**Unaligned**
> 非对齐（Unaligned）访问是指访问的地址未按访问中某个元素的大小对齐的访问。

**Unaligned memory accesses**
> 非对齐内存访问（Unaligned memory accesses）是指未按、或可能未按半字、字或双字适当对齐的内存访问。

**Unallocated**
> 除本手册另有说明外，若架构未为该指令的整个位模式分配特定功能，而是将其描述为 **CONSTRAINED UNPREDICTABLE**、**UNDEFINED**、**UNPREDICTABLE** 或未分配的提示指令，则该指令编码是未分配的（unallocated）。
>
> 若架构未为寄存器中的某一位分配功能，则该位是未分配的。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**UNPREDICTABLE**、**UNDEFINED**。

**Uncontainable**
> 不可抑制的（Uncontainable）是指已被或可能已被静默传播的错误。这也称为未抑制错误（Uncontained error）。
>
> 参见 B16.3 产生错误异常。

**UNDEFINED**
> **UNDEFINED**（未定义）表示产生未定义指令异常的指令。
>
> 在正文中，术语 **UNDEFINED** 以小型大写字母显示。
>
> 参见 C1 章 指令集概述。

**Undetected fault**
> 未检测故障（Undetected fault）：参见潜在故障（Latent fault）。

**Unified Assembler Language**
> 统一汇编语言（**Unified Assembler Language**）是随 Thumb-2 技术引入、本手册所使用的汇编语言。详情参见 C1 章 指令集概述。

**Unified cache**
> 统一缓存（Unified cache）是指同时用于处理取指与处理数据加载和存储的缓存。

**Unindexed addressing**
> 无变址寻址（Unindexed addressing）是指直接以基址寄存器的值作为发送到内存的地址、而不加上或减去偏移量的寻址方式。在大多数类型的加载/存储指令中，无变址寻址通过使用偏移量为 0 的立即数偏移寻址来实现。
>
> 在 M 类中，**LDC**、**LDC2**、**STC** 和 **STC2** 指令具有显式的无变址寻址模式，允许指令中的偏移字段指定附加的协处理器选项。

**UNK**
> **UNK** 是一种缩写，表示软件必须将该字段视为包含 **UNKNOWN** 值。
>
> 硬件必须将该位实现为读取为 0（多位字段则为全 0）。软件不得依赖该字段读取为零。
>
> 参见：**UNKNOWN**。

**UNK/SBOP**
> **UNK/SBOP**：硬件必须将该字段实现为读取为一，并必须忽略对该字段的写入。
>
> 软件不得依赖该字段读取为全 1，且除写回寄存器之外，必须将该值视为 **UNKNOWN**。软件必须使用 SBOP 策略写入该字段。
>
> 该描述可适用于应写为其保持值或写为 1 的单个位，或应写为其保持值或写为全 1 的字段。
>
> 参见：读取为一（Read-as-One）、应为一或保持（Should-Be-One-or-Preserved）、**UNKNOWN**。

**UNK/SBZP**
> **UNK/SBZP**：硬件必须将该位实现为读取为零，并必须忽略对该字段的写入。
>
> 软件不得依赖该字段读取为全 0，且除写回寄存器之外，必须将该值视为 **UNKNOWN**。软件必须使用 SBZP 策略写入该字段。
>
> 该描述可适用于应写为其保持值或写为 0 的单个位，或应写为其保持值或写为全 0 的字段。
>
> 参见：读取为零（Read-as-Zero）、应为零或保持（Should-Be-Zero-or-Preserved）、**UNKNOWN**。

**UNKNOWN**
> **UNKNOWN** 值不包含有效数据，且可能随时变化、随指令变化、随实现变化。**UNKNOWN** 值不得返回在当前或更低特权级别使用非 **UNPREDICTABLE**、非 **CONSTRAINED UNPREDICTABLE** 且不返回 **UNKNOWN** 值的指令无法访问的信息。
>
> 除非先前（在复位之外）已被赋给下列寄存器之一，否则 **UNKNOWN** 值可能随时变化、随指令变化：
>
> - 任一通用寄存器。
> - 任一高级 SIMD 与浮点寄存器。
> - **APSR.{N, Z, C, V}** 标志中的任一个。
>
> 不得将 **UNKNOWN** 值记录或宣传为具有已定义的值或效果。
>
> 在正文中，术语 **UNKNOWN** 以小型大写字母显示。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**UNDEFINED**、**UNK**、**UNPREDICTABLE**。

**UNPREDICTABLE**
> **UNPREDICTABLE**（不可预测）表示该行为不可依赖。**UNPREDICTABLE** 行为不得执行在当前或更低特权级别或安全状态下使用非 **UNPREDICTABLE** 指令所无法执行的任何功能。不得将 **UNPREDICTABLE** 行为记录或宣传为具有已定义的效果。
>
> 为 **UNPREDICTABLE** 的指令可以实现为 **UNDEFINED**。
>
> 在正文中，术语 **UNPREDICTABLE** 以小型大写字母显示。
>
> 参见：**CONSTRAINED UNPREDICTABLE**、**UNDEFINED**。

**Unrecoverable**
> 不可恢复（Unrecoverable）是指不可恢复的可抑制错误。继续正确运行通常不可能。通常这指系统的正确运行，但也可在其他语境中用于描述较小部分的正确运行。系统可能采用高级恢复技术来规避组件中不可恢复但仍被抑制的错误，从而使系统从该错误中恢复。
>
> 参见 B16.3 产生错误异常。

**Unsigned data types**
> 无符号数据类型（Unsigned data types）使用常规二进制格式表示范围为 0 到 +2<sup>N−1</sup>−1 的非负整数。

## W

**Watchpoint**
> 观察点（Watchpoint）是指由对内存的访问所触发的调试事件，该访问以被访问的内存位置的地址来指定。

**Way**
> 路（Way）：参见缓存路（Cache way）。

**WI**
> 写入忽略（**Writes Ignored**）。在软件可写入的寄存器中，施加于某一位或字段的 WI 属性表示该位或字段忽略软件写入的值，并保持该写入之前的值。
>
> 参见：RAO/WI、RAZ/WI、**RES0**、**RES1**。

**Word**
> 字（Word）是 32 位数据项。在 Arm 系统中，字通常是字对齐的。

**Word-aligned**
> 字对齐（Word-aligned）是指地址可被 4 整除。

**Write buffer**
> 写缓冲（Write buffer）是一块用于优化对主存存储操作的高速内存。

**Write-Allocate cache**
> 写分配缓存（Write-Allocate cache）是指在存储数据发生缓存未命中时，导致向缓存中分配一条缓存行的缓存。

**Write-back cache**
> 回写缓存（Write-back cache）是指在存储访问发生缓存命中时，数据仅写入缓存，因此缓存中的数据可能比主存中的数据更新。此类数据在缓存行被清理或重新分配时写回主存。回写缓存的另一个常见名称是 copy-back cache。

**Write-one-to-clear**
> 写 1 清零（Write-one-to-clear）指向相关位写入 1 即将其清零为 0。向该位写入 0 无任何效果。

**Write-one-to-set**
> 写 1 置一（Write-one-to-set）指向相关位写入 1 即将其置为 1。向该位写入 0 无任何效果。

**Write-Through cache**
> 直写缓存（Write-Through cache）是指在存储访问发生缓存命中时，数据同时写入缓存与主存。这通常借助写缓冲完成，以避免使 PE 变慢。

## X

**XPSR**
> 参见：程序状态寄存器（Program Status Registers, XPSR）。
