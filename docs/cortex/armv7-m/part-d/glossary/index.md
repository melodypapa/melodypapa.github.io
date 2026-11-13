---
title: "术语表（Glossary）"
---

本文译自 Part D《附录》（Appendices） 的 Glossary。

本页是 Armv7-M 架构参考手册（**DDI0403E.e**，文档 ID **ID021621**）Glossary 章节的翻译。词条沿用源手册的字母顺序与条目划分，术语名保持英文原文，释义为中文。源手册内部的章节与页码引用（如 `A3-79`）保留原编号以便与原书对照。

## A

**AAPCS**
> Arm 架构过程调用标准（**Procedure Call Standard for the Arm Architecture**）。

**Addressing mode**
> 寻址模式（Addressing mode）指生成加载/存储指令所用内存地址的方法。

**Aligned**
> 对齐（Aligned）指数据项存储在一个地址上，该地址可被恰好整除其字节大小的 2 的最高次幂整除。因此，对齐的半字、字和双字的地址分别可被 2、4 和 8 整除。
>
> 对齐访问（aligned access）是指该访问的地址按访问中每个元素的大小对齐。

**APSR**
> 参见：应用程序状态寄存器（Application Program Status Register）。

**Application Program Status Register (APSR)**
> 应用程序状态寄存器（APSR）是包含传递指令结果状态信息那些位的寄存器，即 **xPSR** 的 **N**、**Z**、**C** 和 **V** 位。在包含 DSP 扩展的实现中，**APSR** 还包含从 DSP 操作提供状态信息的 **GE** 位。
>
> 参见：执行程序状态寄存器（EPSR）、中断程序状态寄存器（IPSR）、程序状态寄存器（xPSR）。

**Arm core registers**
> Arm 内核寄存器（Arm core registers）是 32 位通用寄存器 **R0**–**R12**、**SP**（**R13**）、**LR**（**R14**）和 **PC**（**R15**）的统称。
>
> 参见：通用寄存器（General-purpose register）。

**Atomicity**
> 原子性（Atomicity）是描述单副本原子性或多副本原子性的术语。Arm 架构中所使用的原子性形式定义于 A3-79 页的「Arm 架构中的原子性」。
>
> 参见：多副本原子性（Multi-copy atomicity）、单副本原子性（Single-copy atomicity）。

## B

**Banked register**
> 分组寄存器（Banked register）是具有多个实例的寄存器，使用哪个实例取决于处理器模式、安全状态或其他处理器状态。

**Base register**
> 基址寄存器（Base register）是加载/存储指令指定的寄存器，用作该指令地址计算的基准值。根据指令及其寻址模式，可以从基址寄存器的值中加上或减去一个偏移量，以形成发送到内存的地址。

**Base register writeback**
> 基址寄存器回写（Base register writeback）描述将修改后的值写回地址计算中所用的基址寄存器。

**Big-endian memory**
> 大端内存（Big-endian memory）意味着：
>
> - 字对齐地址处的字节或半字是该地址处字中的最高有效字节或半字。
> - 半字对齐地址处的字节是该地址处半字中的最高有效字节。

**Blocking**
> 阻塞（Blocking）描述一种不允许后续指令在该操作完成之前执行的操作。非阻塞操作可以允许后续指令在其完成之前执行，并且在遇到异常时不向处理器发出异常信号。这使实现能够在非阻塞操作执行期间让后续指令退役，而无需保留精确的处理器状态。

**Branch prediction**
> 分支预测（Branch prediction）是指处理器选择要沿其预取的将来执行路径（参见预取）。例如，在分支指令之后，处理器可以选择预取分支之后的指令或分支目标处的指令。

**Breakpoint**
> 断点（Breakpoint）是由执行特定指令触发的调试事件，该指令由指令地址与执行该指令时处理器的状态中的一项或两项来指定。

**Byte**
> 字节（Byte）是 8 位数据项。

## C

**Callee-save registers**
> 被调用者保存寄存器（Callee-save registers）是被调用过程必须保留的寄存器。为保留被调用者保存寄存器，被调用过程通常要么完全不使用该寄存器，要么在过程入口将其存储到栈上、并在过程出口从栈上重新加载。

**Caller-save registers**
> 调用者保存寄存器（Caller-save registers）是被调用过程无需保留的寄存器。若调用过程要求保留它们的值，则必须自行存储并重新加载。

**Completer**
> 完成者（Completer）是计算系统中响应并完成由请求者（**Requester**）发起的内存事务的代理。
>
> 参见：请求者（Requester）。

**Conditional execution**
> 条件执行（Conditional execution）指指令的执行以条件标志的值为条件。若所需条件不满足，则该指令不执行任何操作。

**Configuration**
> 配置（Configuration）是指在复位时或紧接复位之后进行的设置，通常预期在程序执行期间保持静态。

**Context switch**
> 上下文切换（Context switch）是指在不同的线程或进程之间切换时保存和恢复计算状态。在本手册中，术语 context switch 用于描述操作系统切换上下文的任何情形，其中可能包括也可能不包括地址空间的更改。

**Context synchronization event**
> 上下文同步事件（Context synchronization event）为下列之一：
>
> - 执行 **ISB** 操作。当 **ISB** 指令被执行且未通过其条件码检查时，即完成一次 **ISB** 操作。
> - 进入异常。
> - 从异常返回。
>
> 架构要求以上下文同步事件来保证对系统控制寄存器任何更改的可见性。

## D

**Data Watchpoint and Trace (DWT)**
> 数据观察点与跟踪单元（**Data Watchpoint and Trace**，**DWT**）是 Armv7-M 调试的组件，可选地提供若干跟踪、采样与性能分析功能。

**DCB**
> 参见：调试控制块（Debug Control Block）。

**Debug Control Block (DCB)**
> 调试控制块（**Debug Control Block**，**DCB**）是系统控制空间中分配给支持调试功能的寄存器的区域。
>
> 参见：系统控制空间（System Control Space）。

**Digital signal processing (DSP)**
> 数字信号处理（**Digital signal processing**，**DSP**）指用于处理经采样并转换为数字形式的信号的各种算法。此类算法经常使用饱和算术。

**Direct Memory Access**
> 直接内存访问（Direct Memory Access）是指直接访问主存、而处理器不对相关数据执行任何访问的操作。

**Do-Not-Modify fields (DNM)**
> 不可修改字段（**Do-Not-Modify**，**DNM**）表示该值不得由软件更改。DNM 字段读取为 **UNKNOWN** 值，且只能写入从同一处理器上同一字段读出的相同值。

**Doubleword**
> 双字（Doubleword）是 64 位数据项。在 Arm 系统中，双字通常至少是字对齐的。

**Doubleword-aligned**
> 双字对齐（Doubleword-aligned）是指地址可被 8 整除。

**DSP**
> 参见：数字信号处理（Digital signal processing）。

**DWT**
> 参见：数据观察点与跟踪单元（Data Watchpoint and Trace）。

## E

**Embedded Trace Macrocell (ETM)**
> 嵌入式跟踪宏单元（**Embedded Trace Macrocell**，**ETM**）是 Arm CoreSight 调试与跟踪解决方案的组件。ETM 提供对处理器操作的非侵入式跟踪。

**Endianness**
> 字节序（Endianness）是系统内存映射的一个方面。参见大端（big-endian）与小端（little-endian）。

**EPSR**
> 参见：执行程序状态寄存器（Execution Program Status Register）。

**ETM**
> 参见：嵌入式跟踪宏单元（Embedded Trace Macrocell）。

**Exception**
> 异常（Exception）处理某一事件。例如，异常可以处理外部中断或未定义指令。

**Execution Program Status Register (EPSR)**
> 执行程序状态寄存器（**Execution Program Status Register**，**EPSR**）是包含执行状态位、属于 **xPSR** 一部分的寄存器。
>
> 参见：应用程序状态寄存器（APSR）、中断程序状态寄存器（IPSR）、程序状态寄存器（xPSR）。

**Execution stream**
> 执行流（Execution stream）是指按程序的顺序执行本应执行的指令流。

**Explicit access**
> 显式访问（Explicit access）是指由在 **CPU** 中执行的加载或存储指令所产生的对内存的读取或写入。

## F

**Fault**
> 故障（Fault）是指因某种形式的系统错误而产生的异常。

## G

**General-purpose register**
> 通用寄存器（General-purpose register）是指 32 位通用整数寄存器 **R0** 到 **R12** 之一。在某些文档中，**SP**（**R13**）、**LR**（**R14**）和 **PC**（**R15**）也被描述为通用寄存器。

## H

**Halfword**
> 半字（Halfword）是 16 位数据项。在 Arm 系统中，半字通常是半字对齐的。

**Halfword-aligned**
> 半字对齐（Halfword-aligned）是指地址可被 2 整除。

**High registers**
> 高寄存器（High registers）是指 Arm 内核寄存器 **R8** 到 **R12**，某些 Thumb 指令无法访问它们。

## I

**Immediate values**
> 立即数值（Immediate values）是指直接编码在指令中并在执行该指令时用作数值数据的值。许多 Arm 和 Thumb 指令允许将小的数值作为立即数值编码在对其实施操作的指令中。在 Arm 架构中，除非指令描述中另有说明，否则立即数字段是无符号的。

**IMP**
> **IMP** 是图中使用的缩写，表示相关的一位或多位具有**实现定义**行为。

**IMPLEMENTATION DEFINED**
> 实现定义（**IMPLEMENTATION DEFINED**）是指该行为不由架构定义，但应由各个实现定义并记录在文档中。

**Index register**
> 索引寄存器（Index register）是指某些加载和存储指令中指定的寄存器。该寄存器的值用作偏移量，与基址寄存器的值相加或相减，以形成发送到内存的地址。某些寻址模式还允许在相加或相减之前对索引寄存器的值进行移位。

**Instrumentation Trace Macrocell (ITM)**
> 插桩跟踪宏单元（**Instrumentation Trace Macrocell**，**ITM**）是 Arm CoreSight 调试与跟踪解决方案的组件。ITM 提供内存映射寄存器接口，应用程序可通过它向跟踪汇聚点写入日志字或事件字。

**Interrupt Program Status Register (IPSR)**
> 中断程序状态寄存器（**Interrupt Program Status Register**，**IPSR**）是提供处理器上正在执行的是应用线程还是异常处理程序这一状态信息的寄存器。若正在执行异常处理程序，该寄存器提供有关异常类型的信息。该寄存器是 **xPSR** 的一部分。
>
> 参见：应用程序状态寄存器（APSR）、执行程序状态寄存器（EPSR）、程序状态寄存器（xPSR）。

**Interworking**
> 交互工作（Interworking）是一种工作方式，它允许在同时支持两种执行状态的架构变体中于 Arm 代码与 Thumb 代码之间进行分支。

**IPSR**
> 参见：中断程序状态寄存器（Interrupt Program Status Register）。

**If-Then block (IT block)**
> IT 块（If-Then block）是指 If-Then（**IT**）指令之后最多四条指令构成的块。块中的每条指令都是条件指令。这些指令的条件要么完全相同，要么部分互为相反。更多信息参见 A7-236 页的 **IT**。

**ITM**
> 参见：插桩跟踪宏单元（Instrumentation Trace Macrocell）。

## L

**Little-endian memory**
> 小端内存（Little-endian memory）意味着：
>
> - 字对齐地址处的字节或半字是该地址处字中的最低有效字节或半字。
> - 半字对齐地址处的字节是该地址处半字中的最低有效字节。

**Load/store architecture**
> 加载/存储架构（Load/store architecture）是指数据处理操作仅作用于寄存器内容、而不直接作用于内存内容的架构。

**Long branch**
> 长分支（Long branch）是指使用加载指令分支到 4GB 地址空间中的任意位置。

## M

**Memory barrier**
> 内存屏障（Memory barrier）：参见 A3-92 页的「内存屏障」。

**Memory coherency**
> 内存一致性（Memory coherency）是指确保当某个内存位置被读取（无论是数据读取还是取指）时，实际获得的值始终是最近写入该位置的值这一问题。

**Memory hint**
> 内存提示（Memory hint）指令允许向内存系统提供有关将来内存访问的提前信息，而实际上并不向寄存器堆加载或存储任何数据。**PLD** 和 **PLI** 是 Armv7-M 中定义的仅有的内存提示指令。

**Memory-mapped I/O**
> 内存映射 I/O（Memory-mapped I/O）使用特殊的内存地址，对这些地址的加载或存储即提供 I/O 功能。

**Memory Protection Unit (MPU)**
> 内存保护单元（**Memory Protection Unit**，**MPU**）是一种硬件单元，其寄存器对内存中数量有限的一些保护区域提供简单控制。

**MPU**
> 参见：内存保护单元（Memory Protection Unit）。

**Multi-copy atomicity**
> 多副本原子性（Multi-copy atomicity）是 A3-80 页的「多副本原子性」中描述的原子性形式。
>
> 参见：原子性（Atomicity）、单副本原子性（Single-copy atomicity）。

## N

**NRZ**
> 不归零（Non-Return-to-Zero，**NRZ**）——用于异步通信端口的物理层信号方案。

## O

**Offset addressing**
> 偏移寻址（Offset addressing）是指通过向基址寄存器的值加上或减去偏移量来形成内存地址。在 Arm 架构中，除非指令描述中另有说明，否则偏移字段是无符号的。

## P

**Physical address**
> 物理地址（Physical address）标识一个主存位置。

**Post-indexed addressing**
> 后变址寻址（Post-indexed addressing）是指内存地址即基址寄存器的值，但会向基址寄存器的值加上或减去偏移量，并将结果写回基址寄存器。

**Prefetching**
> 预取（Prefetching）是指在先于某条指令的指令尚未执行完毕之前从内存取指的过程。预取一条指令并不意味着该指令必须被执行。

**Pre-indexed addressing**
> 前变址寻址（Pre-indexed addressing）是指内存地址按与偏移寻址相同的方式形成，但该内存地址也会写回基址寄存器。

**Privileged access**
> 特权访问（Privileged access）：内存系统通常区分特权访问与非特权访问，并支持更严格的非特权访问权限。某些指令只能由特权软件使用。

**Program Status Registers (xPSR)**
> 程序状态寄存器（**xPSR**）是用于描述将 **APSR**、**EPSR** 和 **IPSR** 组合为单个 32 位程序状态寄存器的术语。更多信息参见 B1-516 页的「专用程序状态寄存器 xPSR」。
>
> 参见：应用程序状态寄存器（APSR）、执行程序状态寄存器（EPSR）、中断程序状态寄存器（IPSR）。

**Protection region**
> 保护区域（Protection region）是指其位置、大小及其他属性由内存保护单元寄存器定义的内存区域。

**Protection Unit**
> 保护单元（Protection Unit）：参见内存保护单元（Memory Protection Unit）。

**Pseudo-instruction**
> 伪指令（Pseudo-instruction）是指汇编为某一指令编码、且预期反汇编为另一种汇编语法的 UAL 汇编语法，并在本手册中按该另一种语法描述。例如，`MOV<Rd>,<Rm>, LSL #<n>` 是一条伪指令，预期反汇编为 `LSL<Rd>,<Rm>,#<n>`。

**PSR**
> 参见：程序状态寄存器（Program Status Registers, xPSR）。

## R

**RAO**
> 参见：读取为一（Read-As-One）。

**RAZ**
> 参见：读取为零（Read-As-Zero）。

**RAO/SBOP**
> 读取为一、写入时应为一或保持（Read-As-One, Should-Be-One-or-Preserved on writes）。
>
> 在任何实现中，该位必须读取为 1（位字段则为全 1），且对该字段的写入必须被忽略。软件可以依赖该字段读取为 1（位字段则为全 1），但必须使用 SBOP 策略写入该字段。

**RAZ/SBZP**
> 读取为零、写入时应为零或保持（Read-As-Zero, Should-Be-Zero-or-Preserved on writes）。
>
> 在任何实现中，该位必须读取为 0（位字段则为全 0），且对该字段的写入必须被忽略。软件可以依赖该字段读取为零，但必须使用 SBZP 策略写入该字段。

**RAZ/WI**
> 读取为零、写入忽略（Read-As-Zero, Writes Ignored）。
>
> 在任何实现中，该位必须读取为 0（位字段则为全 0），且对该字段的写入必须被忽略。软件可以依赖该位读取为 0（位字段则为全 0），并依赖写入被忽略。

**Read-As-One (RAO)**
> 读取为一（**Read-As-One**，**RAO**）：在任何实现中，该位必须读取为 1（位字段则为全 1）。

**Read-As-Zero (RAZ)**
> 读取为零（**Read-As-Zero**，**RAZ**）：在任何实现中，该位必须读取为 0（位字段则为全 0）。

**Read, modify, write (RMW)**
> 读-改-写（**Read, modify, write**，**RMW**）指令序列是指：将某一值读入通用寄存器，在该寄存器中更新相关字段，然后写回该寄存器的值。

**Requester**
> 请求者（Requester）是计算系统中能够发起内存事务的代理。
>
> 参见：完成者（Completer）。

**Reserved**
> 保留（Reserved）除非另有说明：
>
> - 保留的指令或访问保留寄存器的指令具有 **UNPREDICTABLE** 行为。
> - 被描述为保留的位位置为 **UNK/SBZP**。

**Return Link**
> 返回链接（Return Link）是指与返回地址相关的值。

**RISC**
> 精简指令集计算机（**Reduced Instruction Set Computer**）。

**RMW**
> 参见：读-改-写（Read, modify, write）。

**RO**
> 只读（**Read only**）寄存器或寄存器字段。RO 位在写访问时被忽略。

**Rounding error**
> 舍入误差（Rounding error）定义为算术运算舍入结果的值减去该运算精确结果的值。

**Rounding modes**
> 舍入模式（Rounding modes）指定浮点运算的精确结果如何舍入为目标格式中可表示的值。

**Round to Nearest (RN) mode**
> 就近舍入（**Round to Nearest**，**RN**）模式是指舍入结果为与未舍入结果最接近的可表示数。

**Round towards Plus Infinity (RP) mode**
> 向正无穷舍入（**Round towards Plus Infinity**，**RP**）模式是指舍入结果为大于或等于精确结果的最接近的可表示数。

**Round towards Minus Infinity (RM) mode**
> 向负无穷舍入（**Round towards Minus Infinity**，**RM**）模式是指舍入结果为小于或等于精确结果的最接近的可表示数。

**Round towards Zero (RZ) mode**
> 向零舍入（**Round towards Zero**，**RZ**）模式是指结果舍入为幅值不大于未舍入结果的最接近的可表示数。

## S

**Saturated arithmetic**
> 饱和算术（Saturated arithmetic）是指这样一种整数算术：结果若大于可表示的最大数，则置为可表示的最大数；结果若小于可表示的最小数，则置为可表示的最小数。有符号饱和算术常用于 DSP 算法。它与 Arm 处理器中所用的常规有符号整数算术形成对照——后者的溢出结果会从 +2<sup>31</sup>−1 回绕到 −2<sup>31</sup> 或反向回绕。

**SBO**
> 参见：应为一（Should-Be-One）。

**SBOP**
> 参见：应为一或保持（Should-Be-One-or-Preserved）。

**SBZ**
> 参见：应为零（Should-Be-Zero）。

**SBZP**
> 参见：应为零或保持（Should-Be-Zero-or-Preserved）。

**SCB**
> 参见：系统控制块（System Control Block）。

**SCS**
> 参见：系统控制空间（System Control Space）。

**Security hole**
> 安全漏洞（Security hole）是指绕过系统保护的机制。

**Serial Wire Output (SWO)**
> 串行线输出（**Serial Wire Output**，**SWO**）是支持 NRZ 与曼彻斯特编码之一或其全部的异步 TPIU 端口。

**Serial Wire Viewer (SWV)**
> 串行线查看器（**Serial Wire Viewer**，**SWV**）是 SWO 与 DWT 单元或 ITM 中至少一个的组合，提供数据跟踪能力。

**Self-modifying code**
> 自修改代码（Self-modifying code）是指向内存写入一条或多条指令、随后执行这些指令的代码。如果不使用屏障指令来确保同步，这类代码不可依赖。

**Should-Be-One (SBO)**
> 应为一（**Should-Be-One**，**SBO**）：软件必须将该位写为 1（位字段则为全 1）。写入 1 以外的值会产生 **UNPREDICTABLE** 结果。

**Should-Be-One-or-Preserved (SBOP)**
> 应为一或保持（**Should-Be-One-or-Preserved**，**SBOP**）：若所写入的值此前未被读取、或寄存器尚未初始化，则软件必须将该位写为 1（位字段则为全 1）。若同一处理器自上次复位以来曾读取该寄存器，则应通过写入此前读取到的相同值来保持该字段中的值。
>
> 硬件必须忽略对这些字段的写入。
>
> 若向该字段写入的值既不是 1（位字段则为全 1），也不是同一处理器上同一字段此前读取到的值，则结果为 **UNPREDICTABLE**。

**Should-Be-Zero (SBZ)**
> 应为零（**Should-Be-Zero**，**SBZ**）：软件必须将该位写为 0（位字段则为全 0）。写入 0 以外的值会产生 **UNPREDICTABLE** 结果。

**Should-Be-Zero-or-Preserved (SBZP)**
> 应为零或保持（**Should-Be-Zero-or-Preserved**，**SBZP**）：若所写入的值此前未被读取、或寄存器尚未初始化，则软件必须将该位写为 0（位字段则为全 0）。若同一处理器自上次复位以来曾读取该寄存器，则应通过写入此前读取到的相同值来保持该字段中的值。
>
> 硬件必须忽略对这些字段的写入。
>
> 若向该字段写入的值既不是 0（位字段则为全 0），也不是同一处理器上同一字段此前读取到的值，则结果为 **UNPREDICTABLE**。

**Signed data types**
> 有符号数据类型（Signed data types）使用补码格式表示范围为 −2<sup>N−1</sup> 到 +2<sup>N−1</sup>−1 的整数。

**Signed immediate and offset fields**
> 有符号立即数与偏移字段（Signed immediate and offset fields）除非另有说明，否则以补码记法编码。

**SIMD**
> 参见：单指令多数据（Single-Instruction, Multiple-Data）。

**Simple sequential execution**
> 简单顺序执行（Simple sequential execution）是指这样一种实现的行为：取指、译码并完全执行每一条指令之后才继续下一条指令。此类实现不进行任何对内存（包括对指令内存）的推测访问。该实现不对执行的任何阶段进行流水化。在实践中，这是架构所基于的理论执行模型，Arm 并不期望该模型对应于架构的现实实现。

**Single-copy atomicity**
> 单副本原子性（Single-copy atomicity）是 A3-79 页的「单副本原子性」中描述的原子性形式。
>
> 参见：原子性（Atomicity）、多副本原子性（Multi-copy atomicity）。

**Single-Instruction, Multiple-Data (SIMD)**
> 单指令多数据（**Single-Instruction, Multiple-Data**，**SIMD**）是一种由单条指令并行地对多组数据执行相同操作的机制。在 Arm 架构中，SIMD 指执行 SIMD 操作的那一组指令。

**Status registers**
> 状态寄存器（Status registers）：参见程序状态寄存器（Program Status Registers, xPSR）。

**SWO**
> 参见：串行线输出（Serial Wire Output）。

**SWV**
> 参见：串行线查看器（Serial Wire Viewer）。

**System Control Block (SCB)**
> 系统控制块（**System Control Block**，**SCB**）是系统控制空间中的一个地址区域，用于与异常模型相关的关键特性控制与配置。
>
> 参见：系统控制空间（System Control Space）。

**System Control Space (SCS)**
> 系统控制空间（**System Control Space**，**SCS**）是内存映射中为系统控制与配置寄存器保留的 4KB 区域。
>
> 参见：调试控制块（Debug Control Block）、系统控制空间（System Control Space）。

## T

**Thumb instruction**
> Thumb 指令是指定处理器要执行的操作的一个或两个半字。Thumb 指令必须是半字对齐的。

**TPIU**
> 参见：跟踪端口接口单元（Trace Port Interface Unit）。

**Trace Port Interface Unit (TPIU)**
> 跟踪端口接口单元（**Trace Port Interface Unit**，**TPIU**）是 Arm CoreSight 调试与跟踪解决方案的组件。TPIU 为处理器实现中的一个或多个跟踪源提供外部接口。

## U

**UAL**
> 参见：统一汇编语言（Unified Assembler Language）。

**Unaligned**
> 非对齐（Unaligned）访问是指访问的地址未按访问中某个元素的大小对齐的访问。

**Unaligned memory accesses**
> 非对齐内存访问（Unaligned memory accesses）是指未按、或可能未按半字、字或双字适当对齐的内存访问。

**Unallocated**
> 除本手册另有说明外，若架构未为该指令的整个位模式分配特定功能，而是将其描述为 **UNDEFINED**、**UNPREDICTABLE** 或未分配的提示指令，则该指令编码是未分配的（unallocated）。
>
> 若架构未为寄存器中的某一位分配功能，则该位是未分配的。

**UNDEFINED**
> **UNDEFINED**（未定义）表示产生未定义指令异常的指令。

**Unified Assembler Language**
> 统一汇编语言（**Unified Assembler Language**）是随 Thumb-2 技术引入、本文档所使用的汇编语言。详情参见 A4-104 页的统一汇编语言。

**Unindexed addressing**
> 无变址寻址（Unindexed addressing）是指直接以基址寄存器的值作为发送到内存的地址、而不加上或减去偏移量的寻址方式。在大多数类型的加载/存储指令中，无变址寻址通过使用偏移量为 0 的立即数偏移寻址来实现。**LDC**、**LDC2**、**STC** 和 **STC2** 指令具有显式的无变址寻址模式，允许指令中的偏移字段用于指定附加的协处理器选项。

**UNKNOWN**
> **UNKNOWN** 值不包含有效数据，且可能随时变化、随指令变化、随实现变化。**UNKNOWN** 值不得构成安全漏洞。不得将 **UNKNOWN** 值记录或宣传为具有已定义的值或效果。

**UNK/SBOP**
> 读取为 **UNKNOWN**、写入时应为一或保持（UNKNOWN on reads, Should-Be-One-or-Preserved on writes）。
>
> 在任何实现中，该位必须读取为 1（位字段则为全 1），且对该字段的写入必须被忽略。软件不得依赖该字段读取为 1（位字段则为全 1），且必须使用 SBOP 策略写入该字段。

**UNK/SBZP**
> 读取为 **UNKNOWN**、写入时应为零或保持（UNKNOWN on reads, Should-Be-Zero-or-Preserved on writes）。
>
> 在任何实现中，该位必须读取为 0（位字段则为全 0），且对该字段的写入必须被忽略。软件不得依赖该字段读取为 0（位字段则为全 0），且必须使用 SBZP 策略写入该字段。

**UNK**
> **UNK** 是一种缩写，表示软件必须将该字段视为包含 **UNKNOWN** 值。
>
> 在任何实现中，该位必须读取为 0（位字段则为全 0）。软件不得依赖该字段读取为零。

**UNPREDICTABLE**
> **UNPREDICTABLE**（不可预测）表示该行为不可依赖。**UNPREDICTABLE** 行为不得构成安全漏洞。**UNPREDICTABLE** 行为不得使处理器或系统的任何部分停止或挂起。不得将 **UNPREDICTABLE** 行为记录或宣传为具有已定义的效果。
>
> 为 **UNPREDICTABLE** 的指令可以实现为 **UNDEFINED**。

**Unsigned data types**
> 无符号数据类型（Unsigned data types）使用常规二进制格式表示范围为 0 到 +2<sup>N</sup>−1 的非负整数。

## W

**Watchpoint**
> 观察点（Watchpoint）是指由对内存的访问所触发的调试事件，该访问以被访问的内存位置的地址来指定。

**Word**
> 字（Word）是 32 位数据项。在 Arm 系统中，字通常是字对齐的。

**WO**
> 只写（**Write only**）寄存器或寄存器字段。WO 位在读取访问时为 **UNKNOWN**。

**Word-aligned**
> 字对齐（Word-aligned）是指地址可被 4 整除。

**WYSIWYG**
> 所见即所得（**What You See Is What You Get**），用于描述所生成输出的可预测行为。从显示形式到打印形式、从软件源代码到可执行代码都是常见的用途示例。

## X

**xPSR**
> 参见：程序状态寄存器（Program Status Registers, xPSR）。
