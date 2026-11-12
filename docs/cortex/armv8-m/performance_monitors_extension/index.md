---
title: "性能监视扩展（The Performance Monitors Extension）"
---

本章规定可选的 **Armv8.1-M** 性能监视扩展规则。

适用于 **Armv8.1-M** 及以后架构版本的实现。

## 1. 计数器

**性能监视扩展**描述一个可选的**非侵入式调试**组件，用于识别并计数**性能事件**。该扩展的一个实现称为**性能监视单元**（PMU）。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

PMU 中最多可容纳 31 个 **IMPLEMENTATION DEFINED** 事件计数器。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

每个性能事件计数器是 16 位通用计数器。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

通过成对**链接**计数器，可以在计数器数量减半的情况下增大计数范围。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

若实现了 PMU，则至少需要两个 16 位性能事件计数器和一个 32 位周期计数器。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

每个性能事件计数器可以配置为计数实现所支持的任一性能事件。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

`PMU_EVCNTRn` 是否支持产生中断，是 **IMPLEMENTATION DEFINED** 的。若不支持中断，则 `PMU_INTENSET.Pn` 为 RAZ/WI。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

每个性能事件计数器可以配置为在指定性能事件每次发生时递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

专用的 32 位周期计数器硬连线为计数周期。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - MVE。

在**计数器链**事件中，架构保证：若 `PMU_CTRL.FZO` 为 0，则计数器低半部分的无符号溢出与其高半部分的随之递增在同一周期内完成计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

在**计数器链**事件中，若 `PMU_CTRL.FZO` 为 1，则计数器低半部分无符号溢出后高半部分是否递增是 **UNPREDICTABLE** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

若计数器被配置为某个特定实现不支持的性能事件，则计数器值为 **UNKNOWN**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

## 2. 性能计数器的精度

**性能监视器**提供大体准确的、具有统计意义的计数信息。为降低实现与验证成本，计数上一定程度的合理误差是可以接受的。**Arm** 未定义合理误差的程度，但建议遵循以下准则：

- 在正常工作条件下，计数器给出准确的计数值。
- 在特殊情形下，例如安全状态变化或其他边界条件，计数不准确是可以接受的。
- 在极不寻常、非重复的病态情形下，计数可能不准确。这类情形很可能由异步异常（如中断）引起，此时出现系统性计数错误的可能性极低。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

只要不在正常工作条件下造成系统性偏差，PMU 中一定程度的合理误差是允许的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

在正常工作条件下：

- 当子类别提供完整覆盖时，某类 PMU 事件的顶层计数器将反映其子类别中的各项正交内容。例如，`MEM_ACCESS` 事件将是各计数高速缓存访问的事件之和。
- 当子类别未提供全面覆盖时，顶层计数器将大于或等于各子类别之和。
- 架构级事件将被一致地应用，但在使能或禁用计数器时应考虑边界条件。
- **Arm** 建议在使能或禁用 PMU 或单个计数器时使用屏障指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

参见：

- 第 B7.2.9 节《内存屏障》。

## 3. 安全状态、访问与模式

通过 **DAP** 访问 PMU 的方式与访问 DWT 相同。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

以下情况下计数器不递增：

- **PE** 处于 **Secure** 状态且特权模式，且 `SecureNoninvasiveDebugAllowed(TRUE) == FALSE`。
- **PE** 处于 **Secure** 状态且非特权模式，且 `SecureNoninvasiveDebugAllowed(FALSE) == FALSE`。
- **PE** 处于 **Non-secure** 状态且特权模式，且 `NoninvasiveDebugAllowed(TRUE) == FALSE`。
- **PE** 处于 **Non-secure** 状态且非特权模式，且 `NoninvasiveDebugAllowed(FALSE) == FALSE`。
- **PE** 处于**调试状态**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。注意，**Secure** 状态要求 S。

PMU 事件计数器在低功耗状态下是递增还是保持原值，是 **IMPLEMENTATION DEFINED** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

处于 **Lockup** 时，计数器是否递增是 **UNKNOWN** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

若 `PMU_CTRL.DP` 为 0，则 PMU 周期计数器不论 **PE** 的安全状态如何都递增。否则，**PE** 处于 **Secure** 状态时 PMU 周期计数器停止递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && S。

参见：

- 第 B14.2 节《Data Watchpoint and Trace 单元》。
- 第 B13.5 节《调试状态》。

## 4. 可归属性

由正在计数该事件的 **PE** 引起的事件是**可归属的**（Attributable）。若事件由正在计数事件的 **PE** 之外的代理引起，则这些事件是**不可归属的**（Unattributable）。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

除 PMU 事件列表中另有说明外，所有架构定义的事件都是**可归属的**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

由指令执行引起的事件，归属于该指令执行时所处的**安全状态**与**特权模式**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && S。

若以下任一为真，则事件不被计数：

- 事件归属于 **Secure** 状态且特权模式，且 `SecureNoninvasiveDebugAllowed(TRUE) == FALSE`。
- 事件归属于 **Secure** 状态且非特权模式，且 `SecureNoninvasiveDebugAllowed(FALSE) == FALSE`。
- 事件归属于 **Non-secure** 状态且特权模式，且 `NoninvasiveDebugAllowed(TRUE) == FALSE`。
- 事件归属于 **Non-secure** 状态且非特权模式，且 `NoninvasiveDebugAllowed(FALSE) == FALSE`。

归属于 **Secure** 状态的事件，若 `SecureNoninvasiveDebugAllowed() == FALSE`，则不被计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

由以下情况引起的**可归属**事件，归属于该访问的 **NS-Req** 与特权：

- **向量取指**。
- 硬件在以下任一时机对寄存器的压栈或出栈：
  - 异常进入。
  - 异常退出。
  - 函数调用进入。
  - 函数返回。
  - 惰性状态保存。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。注意，**Secure** 状态要求 S。

对于每个**不可归属**事件，在禁止计数**可归属**事件时是否计数该不可归属事件，是 **IMPLEMENTATION DEFINED** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

参见：

- 第 B15.10 节《公共事件描述》。

## 5. 与 DWT 性能监视器的共存

PMU 周期计数器 `PMU_CCNTR` 是 `DWT_CYCCNT` 寄存器的别名。只要 PMU 使能周期计数器，所有派生的 PMU 功能就都可用。若同时实现了 PMU 与 DWT，则 `DWT_CTRL.NOCYCCNT` 为 RAZ。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DWTD。

当 `PMU_CTRL.E == 1` 时：

- 读取 `DWT_CPICNT`、`DWT_EXCCNT`、`DWT_FOLDCNT`、`DWT_LSUCNT` 与 `DWT_SLEEPCNT` 返回 **UNKNOWN** 值。
- `DWT_CPICNT`、`DWT_EXCCNT`、`DWT_FOLDCNT`、`DWT_LSUCNT` 与 `DWT_SLEEPCNT` 可能随机递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DWTT。

当 `DWT_CTRL.FOLDEVTENA`、`DWT_CTRL.LSUEVTENA`、`DWT_CTRL.SLEEPEVTENA`、`DWT_CTRL.EXCEVTENA`、`DWT_CTRL.CPIEVTENA` 中任一为 1 时：

- 读取任一 `PMU_EVCNTRn` 计数器返回 **UNKNOWN** 值。
- 读取 `PMU_OVSSET` 与 `PMU_OVSCLR` 中的 PMU 溢出标志返回 **UNKNOWN** 值。
- `PMU_EVCNTRn` 计数器可能随机递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DWTT。

当 `PMU_CTRL.E == 1` 且 `DWT_CTRL.CYCEVTENA`、`DWT_CTRL.FOLDEVTENA`、`DWT_CTRL.LSUEVTENA`、`DWT_CTRL.SLEEPEVTENA`、`DWT_CTRL.EXCEVTENA`、`DWT_CTRL.CPIEVTENA` 中任一为 1 时：

- DWT 产生**事件计数器**包的行为是 **UNPREDICTABLE** 的。
- 若 `PMU_INTENSET.Pn` 中任一标志置 1，则中断的产生是 **UNPREDICTABLE** 的。
- 若 `PMU_CTRL.TRO == 1`，则 PMU 产生**事件计数器**包的行为是 **UNPREDICTABLE** 的。
- PMU 与 DWT 计数器可能随机递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DWTT。

在使能 PMU 并禁用 DWT，或使能 DWT 并禁用 PMU 时，允许实现覆盖跟踪缓冲区中保留的任何包，而不要求软件先把输出冲刷到跟踪汇点或 **TPIU**。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DWTT。

任何时候：

- 对 `DWT_CPICNT`、`DWT_EXCCNT`、`DWT_FOLDCNT`、`DWT_LSUCNT` 或 `DWT_SLEEPCNT` 的写（包括在向 `DWT_CTRL.CYCEVTENA`、`FOLDEVTENA`、`LSUEVTENA`、`SLEEPEVTENA`、`EXCEVTENA`、`CPIEVTENA` 中任一写 1 时的隐式写 0），都会把 `PMU_EVCNTRn` 置为 **UNKNOWN** 值。
- 对 `PMU_EVCNTRn` 的写（包括在向 `PMU_CTRL.P` 写 1 时的隐式写 0），都会把 `DWT_CPICNT`、`DWT_EXCCNT`、`DWT_FOLDCNT`、`DWT_LSUCNT` 与 `DWT_SLEEPCNT` 置为 **UNKNOWN** 值。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DWTT。

允许 PMU 与 DWT 的事件计数器互为别名。周期计数器 `PMU_CCNTR` 与 `DWT_CYCCNT` 始终互为别名。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DWTT。

参见：

- 第 B14.4 节《跟踪端口接口单元》（Trace Port Interface Unit）。

## 6. 中断与调试事件

计数器可以配置为在溢出时产生中断或调试事件。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

若计数器配置为在溢出时产生中断，且以下任一适用，则置位 `DEMCR.MON_PEND`，以挂起 `DFSR.PMU` 置 1 的 **DebugMonitor** 异常：

- 计数器配置为计数归属于非特权模式的事件，且 `DEMCR.UMON_EN` 置 1。
- 计数器配置为计数归属于特权模式的事件，且 `DEMCR.MON_EN` 置 1。

`PMU_OVSSET` 或 `PMU_OVSCLR` 中的相应字段指示是哪个计数器触发了该异常。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

对于每个已实现的事件计数器 m 与周期计数器，若以下全部条件成立，则计数器的无符号溢出使 **PE** 停止：

- 事件计数器的 `PMU_INTENSETm` 置 1，或周期计数器的 `PMU_INTENSET.C` 置 1。
- `DHCSR.C_PMOV` 置 1。
- `CanHaltOnEvent()` 对正在计数的事件所处的安全状态与特权模式返回 TRUE。

上述条件导致：

- `DHCSR.C_HALT` 置 1。
- `DFSR.PMU` 置 1。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE && UDE。注意，非特权事件需要 UDE。

对于每个已实现的事件计数器 m 与周期计数器，若计数器的无符号溢出未使 **PE** 停止，且以下全部条件成立，则挂起 **DebugMonitor** 异常：

- 事件计数器的 `PMU_INTENSETm` 置 1，或周期计数器的 `PMU_INTENSET.C` 置 1。
- 对特权事件 `DEMCR.MON_EN` 置 1，或对非特权事件 `DEMCR.UMON_EN` 置 1。
- **PE** 处于 **Non-secure** 状态，或 `DEMCR.SDME` 置 1。
- **DebugMonitor** 异常的组优先级不足以抢占当前执行优先级。若 **DebugMonitor** 异常的优先级不足以抢占执行，则 **PE** 会把 `DEMCR.MON_PEND` 置 1。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**CTI** 把 PMU 用作事件源。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

参见：

- `PMU_HandleOverflow()`。
- 第 B13 章《调试》。

## 7. 性能监视器与调试状态

计数周期的事件在**调试状态**下不计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

归属于调试器通过外部调试接口发出的操作的事件，在**调试状态**下不计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

对于每个**不可归属**事件，**PE** 处于**调试状态**时是否计数该事件，是 **IMPLEMENTATION DEFINED** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

## 8. 支持的架构级与微架构级事件列表

**Arm** 建议基于底层微架构的性能行为使用实现特定的事件。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

事件 `0x0000`–`0xBFFF` 已定义或保留给未来的公共事件。实现可以实现其中任何事件。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

实现可以在规定的保留空间之外定义特定于该实现的附加事件。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

PMU 的公共事件列表如下。事件类型为：

- **Arch**：架构级事件（Architectural event）。这些事件在所有实现中都相同。
- **uArch**：微架构级事件（Microarchitectural event）。这些事件可能因实现不同而变化。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

本节中：

**Architecturally executed（架构上执行）**：**Instruction architecturally executed** 是一类事件，对指定类型的每条指令计数。架构上执行意味着：程序流属于这样一类流——被计数的指令在程序的**简单顺序执行**（Simple sequential execution）中将被执行。因此，已执行并退役的指令即定义为架构上执行，即使 **PE** 丢弃了推测执行的结果。

若一条在程序的**简单顺序执行**中将被执行、且会产生同步异常的指令，是否被计数是 **IMPLEMENTATION DEFINED** 的。每条架构上执行的指令只计一次，即使实现把该指令拆分为多个操作。对 **PE** 架构状态没有可见影响的指令，若构成架构上执行程序流的一部分，则也是架构上执行。这类指令在何处退役是 **IMPLEMENTATION DEFINED** 的。

没有可见影响的指令示例：

- 一条 **NOP**。
- 未通过**条件码检查**的条件指令。
- 不跳转的 Compare and Branch on Zero（`CBZ`）指令。
- 不跳转的 Compare and Branch on Nonzero（`CBNZ`）指令。

事件导致事件计数器更新发生的位置未定义。

**Instruction architecturally executed, Condition code check pass（指令架构上执行，条件码检查通过）**：条件码检查通过是一类显式不发生在以下情形的事件：

- 未通过**条件码检查**的条件指令。
- 不跳转的 Compare and Branch on Zero（`CBZ`）指令。
- 不跳转的 Compare and Branch on Nonzero（`CBNZ`）指令。
- 不写入内存的 Store-Exclusive 指令。

除此之外，「架构上执行」的定义与指令架构上执行相同。

一条架构上执行且条件码检查通过的分支，也称为**跳转的分支**（branch taken）。

**Instruction memory access（指令内存访问）**：**PE** 通过指令取指获取要执行的指令。指令取指可能由以下原因引起：

- 取指架构上执行的指令。
- 执行 `PLI` 指令的结果。
- 对某条指令将来可能被执行的推测。

单条指令的取指与一次指令内存访问之间的关系是 **IMPLEMENTATION DEFINED** 的。例如，实现可能在一次指令内存访问中取指多条指令，其中包含非整数条指令。

**Memory-read operations（内存读操作）**：**PE** 通过内存读操作与内存写操作访问内存。内存读操作可能由以下原因引起：

- 架构上执行的内存读指令的结果。
- 推测执行的内存读指令的结果。

对于 Level 1 高速缓存之外的各级高速缓存层次，内存读操作还包括作为更靠近 **PE** 的另一高速缓存**重填**（refill）的一部分而进行的访问。这类重填可能由以下非穷尽列表中的任一原因引起：

- 在高速缓存中缺失的内存读操作或内存写操作。
- 预加载数据（`PLD`）指令的执行。
- 在统一高速缓存上执行指令预加载（`PLI`）指令。
- 高速缓存维护操作的执行。预加载指令或高速缓存维护操作本身并不是对该高速缓存的访问。但预加载指令或高速缓存维护操作可能产生高速缓存重填，这些重填随后被视为该高速缓存之外的内存读操作。
- 对未来某条指令可能访问该内存位置的推测。
- 指令内存访问。

内存读指令与内存读操作之间的关系是 **IMPLEMENTATION DEFINED** 的。

**Memory-write operations（内存写操作）**：内存写操作可能由以下原因引起：

- 架构上执行的内存写指令的结果。
- 推测执行的内存写指令的结果。

未成为架构上执行的推测执行内存写指令不得改变架构定义的内存视图。不过，它们可以产生一个内存写操作，该操作随后以某种实现特定的方式被撤销。

对于 Level 1 高速缓存之外的各级高速缓存层次，内存写操作还包括作为更靠近 **PE** 的另一高速缓存**写回**（write-back）的一部分而进行的访问。这类写回可能由以下非穷尽列表中的任一原因引起：

- 从高速缓存中逐出脏行，以便为高速缓存重填分配一行。
- 高速缓存维护操作的执行。高速缓存维护操作本身并不是对该高速缓存的访问。但高速缓存维护操作可能产生写回，这些写回随后被视为该高速缓存之外的内存写操作。
- 来自另一 **PE** 的一致性请求的结果。

内存写指令与内存写操作之间的关系是 **IMPLEMENTATION DEFINED** 的。

从与其他 **PE** 共享的高速缓存写回的数据，可能并不是执行导致该写回的操作的 **PE** 所写的数据。尽管如此，该事件仍作为该 **PE** 的写回事件计数。

**Microarchitectural operation（微架构操作）**：**PE** 的实现可以把指令分解为独立的、更小的操作。**微架构操作**（micro-op）的使用是 **IMPLEMENTATION DEFINED** 的。一条指令可能在执行流水线的任何位置产生一个或多个 micro-op。就事件计数而言，计数的是 micro-op。micro-op 的定义是实现特定的。一条架构指令可能产生多于一个 micro-op。micro-op 也可能在执行流中被移除或合并，因此一条架构指令可能产生零个 micro-op。允许把指令任意转换为等价的 micro-op 序列。无论底层如何把指令划分为 micro-op，**PE** 都必须严格遵循架构可见行为。

操作计数可以指示 **PE** 上的工作负载。但并未要求各操作代表相近的工作量，不同微架构之间的直接比较没有意义。

例如，实现可能把六寄存器的 `LDM` 指令拆分为六个 micro-op（每次加载一个），外加第七个地址生成操作，用于确定基地址或写回地址。因此一条指令可能被拆分为多个可计数的事件。

**Operations speculatively executed（推测执行的操作）**：推测执行的 micro-op 与架构上执行的指令之间没有架构保证的关系。若在分支预测错误后发现该操作并不需要，这类操作的结果也可能被丢弃。因此，**Armv8-M** 在适当处把这些事件定义为推测执行的操作。

**Slot（槽位）**：**PE** 的实现可能能够在单个处理器周期内执行多个 micro-op。可执行的 micro-op 最大数量在执行流水线的不同位置可能不同。为了能够剖析 **PE** 资源的利用率，实现会在执行流水线中选择一个实现特定的位置，该位置上可执行的 micro-op 最大数量是一个 **IMPLEMENTATION DEFINED** 的固定值。

**Software change of the PC（PC 的软件修改）**：某些事件与导致 **PC** 发生软件修改的指令有关。这包括所有：

- 分支指令。
- 显式写入 **PC** 的内存读指令。
- 显式写入 **PC** 的数据处理指令。
- 异常返回指令。

以下各项是否被视为 **PC** 的软件修改，是 **IMPLEMENTATION DEFINED** 的：

- `BKPT`。
- **UNDEFINSTR** 故障。
- **上下文同步屏障** `ISB` 指令。

**Speculatively executed（推测执行）**：许多事件与推测执行的操作有关。这里的推测执行是指 **PE** 做了一些与一条或多条指令相关的工作，但这些指令不一定架构上执行。

「推测执行」的定义并不意味着只包括那些被推测执行、随后（例如因分支预测错误或故障）被放弃的操作。也就是说，推测执行的操作必须同时计数错误执行路径与正确执行路径上的操作。

不同的事件组可以有不同的 **IMPLEMENTATION DEFINED** 的「推测执行」定义。这些组共享一个共同的基础类型，由事件名表示。上例中的每个事件都属于基础类型「推测执行的操作」。对于具有共同基础类型的事件组，推测执行的操作都按同一基准计数，通常意味着在流水线上的同一位置计数。这样就可以比较计数，并对被剖析的程序得出有意义的观察结论。

在这些组内，事件通常参照某条特定架构指令或指令组来定义。对于推测执行的操作，这意味着其语义映射到该类型指令的操作。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

PMU 的公共事件列表如下。

| 事件编号 | 事件类型 | 事件助记符 | 描述 |
| --- | --- | --- | --- |
| 0x0000 | Arch | `SW_INCR` | 架构上执行的指令，条件码检查通过，软件递增 |
| 0x0001 | uArch | `L1I_CACHE_REFILL` | 可归属的 Level 1 指令高速缓存重填 |
| 0x0003 | uArch | `L1D_CACHE_REFILL` | 可归属的 Level 1 数据高速缓存重填 |
| 0x0004 | uArch | `L1D_CACHE` | 可归属的 Level 1 数据高速缓存访问 |
| 0x0006 | Arch | `LD_RETIRED` | 架构上执行的指令，条件码检查通过，加载 |
| 0x0007 | Arch | `ST_RETIRED` | 架构上执行的指令，条件码检查通过，存储 |
| 0x0008 | Arch | `INST_RETIRED` | 架构上执行的指令 |
| 0x0009 | Arch | `EXC_TAKEN` | 已接受的异常 |
| 0x000A | Arch | `EXC_RETURN` | 架构上执行的指令，条件码检查通过，异常返回 |
| 0x000C | Arch | `PC_WRITE_RETIRED` | 架构上执行的指令，条件码检查通过，PC 的软件修改 |
| 0x000D | Arch | `BR_IMMED_RETIRED` | 架构上执行的指令，立即数分支 |
| 0x000E | Arch | `BR_RETURN_RETIRED` | 架构上执行的指令，条件码检查通过，过程返回 |
| 0x000F | Arch | `UNALIGNED_LDST_RETIRED` | 架构上执行的指令，条件码检查通过，非对齐加载或存储 |
| 0x0010 | uArch | `BR_MIS_PRED` | 推测执行的预测错误或未预测分支 |
| 0x0011 | uArch | `CPU_CYCLES` | 周期 |
| 0x0012 | uArch | `BR_PRED` | 推测执行的可预测分支 |
| 0x0013 | uArch | `MEM_ACCESS` | 数据内存访问 |
| 0x0014 | uArch | `L1I_CACHE` | 可归属的 Level 1 指令高速缓存访问 |
| 0x0015 | uArch | `L1D_CACHE_WB` | 可归属的 Level 1 数据高速缓存写回 |
| 0x0016 | uArch | `L2D_CACHE` | 可归属的 Level 2 数据高速缓存访问 |
| 0x0017 | uArch | `L2D_CACHE_REFILL` | 可归属的 Level 2 数据高速缓存重填 |
| 0x0018 | uArch | `L2D_CACHE_WB` | 可归属的 Level 2 数据高速缓存写回 |
| 0x0019 | uArch | `BUS_ACCESS` | 可归属的总线访问 |
| 0x001A | uArch | `MEMORY_ERROR` | 本地内存错误 |
| 0x001B | uArch | `INST_SPEC` | 推测执行的操作 |
| 0x001D | uArch | `BUS_CYCLES` | 总线周期 |
| 0x001E | Arch | `CHAIN` | 对于奇数编号计数器，当同一 PE 上相邻的偶数编号计数器发生溢出时递增 |
| 0x001F | uArch | `L1D_CACHE_ALLOCATE` | 可归属的 Level 1 数据高速缓存分配（无重填） |
| 0x0020 | uArch | `L2D_CACHE_ALLOCATE` | 可归属的 Level 2 数据高速缓存分配（无重填） |
| 0x0021 | Arch | `BR_RETIRED` | 架构上执行的指令，分支 |
| 0x0022 | uArch | `BR_MIS_PRED_RETIRED` | 架构上执行的指令，预测错误的分支 |
| 0x0023 | uArch | `STALL_FRONTEND` | 因前端而无操作发射 |
| 0x0024 | uArch | `STALL_BACKEND` | 因后端而无操作发射 |
| 0x0027 | uArch | `L2I_CACHE` | 可归属的 Level 2 指令高速缓存访问 |
| 0x0028 | uArch | `L2I_CACHE_REFILL` | 可归属的 Level 2 指令高速缓存重填 |
| 0x0029 | uArch | `L3D_CACHE_ALLOCATE` | 可归属的 Level 3 数据高速缓存分配（无重填） |
| 0x002A | uArch | `L3D_CACHE_REFILL` | 可归属的 Level 3 数据高速缓存重填 |
| 0x002B | uArch | `L3D_CACHE` | 可归属的 Level 3 数据高速缓存访问 |
| 0x002C | uArch | `L3D_CACHE_WB` | 可归属的 Level 3 数据高速缓存写回 |
| 0x0036 | uArch | `LL_CACHE_RD` | 末级数据高速缓存读取 |
| 0x0037 | uArch | `LL_CACHE_MISS_RD` | 末级数据高速缓存读取缺失 |
| 0x0039 | uArch | `L1D_CACHE_LMISS_RD` | Level 1 数据高速缓存长延迟读取缺失 |
| 0x003A | uArch | `OP_RETIRED` | 架构上执行的微操作 |
| 0x003B | uArch | `OP_SPEC` | 推测执行的微操作 |
| 0x003C | uArch | `STALL` | 无操作被发送执行 |
| 0x003D | uArch | `STALL_SLOT_BACKEND` | 因后端导致某槽位无操作被发送执行 |
| 0x003E | uArch | `STALL_SLOT_FRONTEND` | 因前端导致某槽位无操作被发送执行 |
| 0x003F | uArch | `STALL_SLOT` | 某槽位无操作被发送执行 |
| 0x0040 | uArch | `L1D_CACHE_RD` | Level 1 数据高速缓存读取 |
| 0x0100 | uArch | `LE_RETIRED` | 架构上执行的循环结束指令，且在 `LO_BRANCH_INFO` 缓存中登记条目 |
| 0x0101 | uArch | `LE_SPEC` | 推测执行的循环结束指令，且在 `LO_BRANCH_INFO` 缓存中登记条目 |
| 0x0104 | uArch | `BF_RETIRED` | 架构上执行的分支未来指令，条件码检查通过，且在 `LO_BRANCH_INFO` 缓存中登记条目 |
| 0x0105 | uArch | `BF_SPEC` | 推测执行的分支未来指令，条件码检查通过，且在 `LO_BRANCH_INFO` 缓存中登记条目 |
| 0x0108 | uArch | `LE_CANCEL` | `LO_BRANCH_INFO` 缓存含有有效循环条目时被清除，且该清除并不在循环的最后一次迭代 |
| 0x0109 | uArch | `BF_CANCEL` | `LO_BRANCH_INFO` 缓存含有有效 BF 条目时被清除，且相关分支未被跳转 |
| 0x0114 | Arch | `SE_CALL_S` | 对 Secure 函数的调用，导致安全状态切换 |
| 0x0115 | Arch | `SE_CALL_NS` | 对 Non-secure 函数的调用，导致安全状态切换 |
| 0x0118 | Arch | `DWT_CMPMATCH0` | DWT 比较器 0 匹配 |
| 0x0119 | Arch | `DWT_CMPMATCH1` | DWT 比较器 1 匹配 |
| 0x011A | Arch | `DWT_CMPMATCH2` | DWT 比较器 2 匹配 |
| 0x011B | Arch | `DWT_CMPMATCH3` | DWT 比较器 3 匹配 |
| 0x011C | Arch | `DWT_CMPMATCH4` | DWT 比较器 4 匹配 |
| 0x011D | Arch | `DWT_CMPMATCH5` | DWT 比较器 5 匹配 |
| 0x011E | Arch | `DWT_CMPMATCH6` | DWT 比较器 6 匹配 |
| 0x011F | Arch | `DWT_CMPMATCH7` | DWT 比较器 7 匹配 |
| 0x0130 | uArch | `PAC_RETIRED` | 架构上执行的 PAC 指令 |
| 0x0131 | uArch | `PAC_SPEC` | 推测执行的 PAC 指令 |
| 0x0134 | uArch | `AUT_RETIRED` | 架构上执行的 AUT 指令 |
| 0x0135 | uArch | `AUT_SPEC` | 推测执行的 AUT 指令 |
| 0x013C | uArch | `STALL_BACKEND_PAC` | 由 PAC 操作引起的停顿周期 |
| 0x0200 | Arch | `MVE_INST_RETIRED` | 架构上执行的 MVE 指令 |
| 0x0201 | uArch | `MVE_INST_SPEC` | 推测执行的 MVE 指令 |
| 0x0204 | Arch | `MVE_FP_RETIRED` | 架构上执行的 MVE 浮点指令 |
| 0x0205 | uArch | `MVE_FP_SPEC` | 推测执行的 MVE 浮点指令 |
| 0x0208 | Arch | `MVE_FP_HP_RETIRED` | 架构上执行的 MVE 半精度浮点指令 |
| 0x0209 | uArch | `MVE_FP_HP_SPEC` | 推测执行的 MVE 半精度浮点指令 |
| 0x020C | Arch | `MVE_FP_SP_RETIRED` | 架构上执行的 MVE 单精度浮点指令 |
| 0x020D | uArch | `MVE_FP_SP_SPEC` | 推测执行的 MVE 单精度浮点指令 |
| 0x0214 | Arch | `MVE_FP_MAC_RETIRED` | 架构上执行的 MVE 浮点乘法或乘加指令 |
| 0x0215 | uArch | `MVE_FP_MAC_SPEC` | 推测执行的 MVE 浮点乘法或乘加指令 |
| 0x0224 | Arch | `MVE_INT_RETIRED` | 架构上执行的 MVE 整数指令 |
| 0x0225 | uArch | `MVE_INT_SPEC` | 推测执行的 MVE 整数指令 |
| 0x0228 | Arch | `MVE_INT_MAC_RETIRED` | 架构上执行的 MVE 整数乘法或乘加指令 |
| 0x0229 | uArch | `MVE_INT_MAC_SPEC` | 推测执行的 MVE 整数乘法或乘加指令 |
| 0x0238 | Arch | `MVE_LDST_RETIRED` | 架构上执行的 MVE 加载或存储指令 |
| 0x0239 | uArch | `MVE_LDST_SPEC` | 推测执行的 MVE 加载或存储指令 |
| 0x023C | Arch | `MVE_LD_RETIRED` | 架构上执行的 MVE 加载指令 |
| 0x023D | uArch | `MVE_LD_SPEC` | 推测执行的 MVE 加载指令 |
| 0x0240 | Arch | `MVE_ST_RETIRED` | 架构上执行的 MVE 存储指令 |
| 0x0241 | uArch | `MVE_ST_SPEC` | 推测执行的 MVE 存储指令 |
| 0x0244 | uArch | `MVE_LDST_CONTIG_RETIRED` | 架构上执行的 MVE 连续加载或存储指令 |
| 0x0245 | uArch | `MVE_LDST_CONTIG_SPEC` | 推测执行的 MVE 连续加载或存储指令 |
| 0x0248 | uArch | `MVE_LD_CONTIG_RETIRED` | 架构上执行的 MVE 连续加载指令 |
| 0x0249 | uArch | `MVE_LD_CONTIG_SPEC` | 推测执行的 MVE 连续加载指令 |
| 0x024C | uArch | `MVE_ST_CONTIG_RETIRED` | 架构上执行的 MVE 连续存储指令 |
| 0x024D | uArch | `MVE_ST_CONTIG_SPEC` | 推测执行的 MVE 连续存储指令 |
| 0x0250 | uArch | `MVE_LDST_NONCONTIG_RETIRED` | 架构上执行的 MVE 非连续加载或存储指令 |
| 0x0251 | uArch | `MVE_LDST_NONCONTIG_SPEC` | 推测执行的 MVE 非连续加载或存储指令 |
| 0x0254 | uArch | `MVE_LD_NONCONTIG_RETIRED` | 架构上执行的 MVE 非连续加载指令 |
| 0x0255 | uArch | `MVE_LD_NONCONTIG_SPEC` | 推测执行的 MVE 非连续加载指令 |
| 0x0258 | uArch | `MVE_ST_NONCONTIG_RETIRED` | 架构上执行的 MVE 非连续存储指令 |
| 0x0259 | uArch | `MVE_ST_NONCONTIG_SPEC` | 推测执行的 MVE 非连续存储指令 |
| 0x025C | Arch | `MVE_LDST_MULTI_RETIRED` | 架构上执行的、面向多个寄存器的 MVE 内存指令 |
| 0x025D | uArch | `MVE_LDST_MULTI_SPEC` | 推测执行的、面向多个寄存器的 MVE 内存指令 |
| 0x0260 | Arch | `MVE_LD_MULTI_RETIRED` | 架构上执行的、面向多个寄存器的 MVE 内存加载指令 |
| 0x0261 | uArch | `MVE_LD_MULTI_SPEC` | 推测执行的、面向多个寄存器的 MVE 内存加载指令 |
| 0x0264 | Arch | `MVE_ST_MULTI_RETIRED` | 架构上执行的、面向多个寄存器的 MVE 内存存储指令 |
| 0x0265 | uArch | `MVE_ST_MULTI_SPEC` | 推测执行的、面向多个寄存器的 MVE 内存存储指令 |
| 0x028C | uArch | `MVE_LDST_UNALIGNED_RETIRED` | 架构上执行的 MVE 非对齐内存加载或存储指令 |
| 0x028D | uArch | `MVE_LDST_UNALIGNED_SPEC` | 推测执行的 MVE 非对齐内存加载或存储指令 |
| 0x0290 | uArch | `MVE_LD_UNALIGNED_RETIRED` | 架构上执行的 MVE 非对齐加载指令 |
| 0x0291 | uArch | `MVE_LD_UNALIGNED_SPEC` | 推测执行的 MVE 非对齐加载指令 |
| 0x0294 | uArch | `MVE_ST_UNALIGNED_RETIRED` | 架构上执行的 MVE 非对齐存储指令 |
| 0x0295 | uArch | `MVE_ST_UNALIGNED_SPEC` | 推测执行的 MVE 非对齐存储指令 |
| 0x0298 | uArch | `MVE_LDST_UNALIGNED_NONCONTIG_RETIRED` | 架构上执行的 MVE 非对齐非连续加载或存储指令 |
| 0x0299 | uArch | `MVE_LDST_UNALIGNED_NONCONTIG_SPEC` | 推测执行的 MVE 非对齐非连续加载或存储指令 |
| 0x02A0 | Arch | `MVE_VREDUCE_RETIRED` | 架构上执行的 MVE 向量归约指令 |
| 0x02A1 | uArch | `MVE_VREDUCE_SPEC` | 推测执行的 MVE 向量归约指令 |
| 0x02A4 | Arch | `MVE_VREDUCE_FP_RETIRED` | 架构上执行的 MVE 浮点向量归约指令 |
| 0x02A5 | uArch | `MVE_VREDUCE_FP_SPEC` | 推测执行的 MVE 浮点向量归约指令 |
| 0x02A8 | Arch | `MVE_VREDUCE_INT_RETIRED` | 架构上执行的 MVE 整数向量归约指令 |
| 0x02A9 | uArch | `MVE_VREDUCE_INT_SPEC` | 推测执行的 MVE 整数向量归约指令 |
| 0x02B8 | uArch | `MVE_PRED` | 有一个或多个谓词化 beat 架构上执行的周期 |
| 0x02CC | uArch | `MVE_STALL` | 由 MVE 指令引起的停顿周期 |
| 0x02CD | uArch | `MVE_STALL_RESOURCE` | 由 MVE 指令因资源冲突引起的停顿周期 |
| 0x02CE | uArch | `MVE_STALL_RESOURCE_MEM` | 由 MVE 指令因存储器资源冲突引起的停顿周期 |
| 0x02CF | uArch | `MVE_STALL_RESOURCE_FP` | 由 MVE 指令因浮点资源冲突引起的停顿周期 |
| 0x02D0 | uArch | `MVE_STALL_RESOURCE_INT` | 由 MVE 指令因整数资源冲突引起的停顿周期 |
| 0x02D3 | uArch | `MVE_STALL_BREAK` | 由 MVE 链断裂引起的停顿周期 |
| 0x02D4 | uArch | `MVE_STALL_DEPENDENCY` | 由 MVE 寄存器依赖引起的停顿周期 |
| 0x4007 | uArch | `ITCM_ACCESS` | 指令 TCM 访问 |
| 0x4008 | uArch | `DTCM_ACCESS` | 数据 TCM 访问 |
| 0x4010 | uArch | `TRCEXTOUT0` | ETM 外部输出 0 |
| 0x4011 | uArch | `TRCEXTOUT1` | ETM 外部输出 1 |
| 0x4012 | uArch | `TRCEXTOUT2` | ETM 外部输出 2 |
| 0x4013 | uArch | `TRCEXTOUT3` | ETM 外部输出 3 |
| 0x4018 | uArch | `CTI_TRIGOUT4` | 交叉触发接口输出触发 4 |
| 0x4019 | uArch | `CTI_TRIGOUT5` | 交叉触发接口输出触发 5 |
| 0x401A | uArch | `CTI_TRIGOUT6` | 交叉触发接口输出触发 6 |
| 0x401B | uArch | `CTI_TRIGOUT7` | 交叉触发接口输出触发 7 |

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

## 9. 通用架构级与微架构级事件

本节给出适用于多个事件的描述。

### 9.1 CTI_TRIGOUT（交叉触发接口输出触发，n = 4 至 7）

计数器对来自 **CTI** 输出触发 <n> 的每个事件计数。注意，**CTI** 输出触发是 PMU 与 **PE 跟踪单元**的输入事件。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

### 9.2 TRCEXTOUT（PE 跟踪单元外部输出，n = 0 至 3）

计数器对 **ETM** 外部事件 <n> 所指示的每个事件计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

### 9.3 DWT_CMPMATCH（DWT 比较器匹配，n = 0 至 7）

计数器对 **DWT** 比较器 <n> 指示的每次成功比较器匹配递增。若未实现该比较器或该比较器被禁用，则计数器不递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

### 9.4 L\<n\>I_CACHE_REFILL（Level \<n\> 指令高速缓存重填）

计数器计数由 `L<n>I_CACHE` 计数的、从 Level <n> 指令高速缓存之外返回指令的每次访问。这里的「之外」是指 Level <m> 高速缓存（m>n）或内存。

该事件向软件表明：该访问在 Level <n> 指令高速缓存中缺失，相对于在 Level <n> 指令高速缓存中命中的访问，可能因额外延迟而对性能有显著影响。

Level <n> 高速缓存的定义是 **IMPLEMENTATION DEFINED** 的，不一定对应于 **CLIDR** 机制定义的各级高速缓存。相反，<n> 值越大，对应越大的平均额外延迟。

计数器不计数：

- 缺失对性能没有显著影响的访问。
- 不导致新的高速缓存重填、而由先前缺失满足的缺失。

若高速缓存是共享的，则只计数**可归属**于该 **PE** 的访问。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

### 9.5 L\<n\>D_CACHE_REFILL（Level \<n\> 数据高速缓存重填）

计数器计数由 `L<n>D_CACHE` 计数的、从 Level <n> 数据高速缓存之外返回数据的每次访问。这里的「之外」是指 Level <m> 高速缓存（m>n）或内存。

对导致新行填充（linefill）的高速缓存行的每次访问都计数，包括来自产生多次访问的指令（例如加载/存储多寄存器指令）以及 `PUSH` 与 `POP` 指令的访问。特别地，计数器计数导致 Level <n> 高速缓存重填的对 Level <n> 高速缓存的访问。重填包括任何导致数据从 Level 1 之外取到 Level <n> 高速缓存的访问，即使该数据最终未分配到 Level <n> 高速缓存。

Level <n> 高速缓存的定义是 **IMPLEMENTATION DEFINED** 的，不一定对应于 **CLIDR** 机制定义的各级高速缓存。相反，<n> 值越大，对应越大的平均额外延迟。

计数器不计数：

- 不导致新的 Level <n> 高速缓存重填、而由先前缺失的重填数据满足的访问。
- 产生内存访问但不产生新行填充的高速缓存行访问，例如在高速缓存中命中的写直达（Write-Through）写。
- 高速缓存维护指令。
- 把整行写入高速缓存、且不从 Level <n> 高速缓存之外取任何数据的写。
- 在高速缓存中缺失、并写直达该高速缓存而不分配行的写。

若高速缓存是共享的，则只计数**可归属**于该 **PE** 的访问。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

### 9.6 L\<n\>D_CACHE_MISS_RD（Level \<n\> 数据高速缓存读缺失）

计数器计数由 `L<n>D_CACHE_RD` 计数的、从 Level <n> 数据或统一高速缓存之外返回数据的每次访问。这里的「之外」是指 Level <m> 高速缓存（m>n）或内存。

该事件向软件表明：该访问在 Level <n> 数据或统一高速缓存中缺失，相对于在 Level <n> 数据或统一高速缓存中命中的访问，可能因额外延迟而对性能有显著影响。

Level <n> 高速缓存的定义是 **IMPLEMENTATION DEFINED** 的，不一定对应于 **CLIDR** 机制定义的各级高速缓存。相反，<n> 值越大，对应越大的平均额外延迟。

计数器不计数：

- 缺失对性能没有显著影响的访问。
- 不导致新的高速缓存重填、而由先前缺失满足的缺失。

若高速缓存是共享的，则只计数**可归属**于该 **PE** 的访问。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

### 9.7 L\<n\>D_CACHE_WB（Level \<n\> 数据高速缓存写回）

计数器计数从 Level <n> 数据或统一高速缓存写回的每次数据写回。

计数器计数导致数据从 Level <n> 高速缓存写到 Level <n> 高速缓存之外的每次写回。例如，计数器计数以下情形：

- 导致数据写入 Level <n+1> 高速缓存或内存的写回。
- 对最近取入、但尚未分配到 Level <n> 高速缓存的高速缓存行的写回。
- 因一致性请求而发生的、从 Level <n> 高速缓存到该高速缓存之外的数据传送。

对于同一多处理器簇内到其他 Level 高速缓存的传送，哪些情形被计数由 **IMPLEMENTATION DEFINED** 决定。

每次写回只计数一次，即使完成该写回需要多次访问。

因高速缓存维护指令而发生的写回是否计数，是 **IMPLEMENTATION DEFINED** 的。计数器不计数：

- 不向 Level <n+1> 高速缓存或内存写回的高速缓存行无效化。
- 从 **PE** 出发、写直达 Level <n> 高速缓存到其之外的写。

当 **PE** 之外的请求者发出导致写回的一致性请求时，产生一次**不可归属**写回事件。若高速缓存是共享的，则不计数**不可归属**写回事件；若高速缓存不共享，则计数该事件。非因从高速缓存中逐出某行而写入整个高速缓存行的写是否计数，是 **IMPLEMENTATION DEFINED** 的。

若高速缓存是共享的，则只计数**可归属**于该 **PE** 的访问。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

### 9.8 L\<n\>I_CACHE（Level \<n\> 指令高速缓存访问）

计数器计数至少到 Level <n> 指令高速缓存的每次**可归属**访问。对其他 Level <n> 指令存储结构（例如重填缓冲区）的每次访问也计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

### 9.9 L\<n\>D_CACHE（Level \<n\> 数据高速缓存访问）

计数器计数至少到 Level <n> 数据或统一高速缓存的每次**可归属**内存读或内存写访问。对高速缓存行的每次访问都计数，包括指令产生的多次访问，例如 `LDM` 或 `STM`。对其他 Level <n> 数据或统一高速缓存存储结构的每次访问也计数。

计数器不计数高速缓存维护指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

### 9.10 L\<n\>D_CACHE_RD（Level \<n\> 数据高速缓存访问，读）

计数器的工作方式与 `L<n>D_CACHE` 相同，唯一例外是计数器只计数内存读访问。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

## 10. 公共事件描述

本节定义 PMU 计数器可以支持的公共事件。对于这些公共特性，计数器通常对每个事件只递增一次；各事件描述中说明了例外情形。这些定义中，**Architecturally executed**（架构上执行）指指令流属于这样一类流——被计数的指令在简单顺序执行模型中将被执行。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**SW_INCR（0x0000，架构级）**

计数器在写入 `PMU_SWINC` 寄存器时递增。若 **PE** 在两次对 `PMU_SWINC` 寄存器的架构上执行写之间没有**上下文同步事件**，则计数器递增两次。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L1I_CACHE_REFILL（0x0001，微架构级）**

参见 `L<n>I_CACHE_REFILL`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L1D_CACHE_REFILL（0x0003，微架构级）**

参见 `L<n>D_CACHE_REFILL`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L1D_CACHE（0x0004，微架构级）**

参见 `L<n>D_CACHE`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**LD_RETIRED（0x0006，架构级）**

计数器对每条已执行的内存读指令递增。`LD_RETIRED` 不计数 Store-Exclusive 指令的返回状态值。以下预加载指令是否作为内存读指令计数，是 **IMPLEMENTATION DEFINED** 的：

- `PLD`（literal）。
- `PLD`、`PLDW`（immediate）。
- `PLI`（immediate、literal）。
- `PLI`（register）。

**Arm** 建议：若这些指令未实现为 **NOP**，则把它们作为内存读指令计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**ST_RETIRED（0x0007，架构级）**

计数器对每条已执行的内存写指令递增。对于失败的 Store-Exclusive 指令，计数器不递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**INST_RETIRED（0x0008，架构级）**

计数器对每条架构上执行的指令递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**EXC_TAKEN（0x0009，架构级）**

计数器在每次异常进入时递增。对于迟到异常或派生异常，计数器不再额外递增；但在**尾链**时会递增。这对应于对 `ActivateException()` 伪代码函数的调用。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**EXC_RETURN（0x000A，架构级）**

计数器在每次异常返回时递增。这发生在 **PE** 处于 **Handler 模式**，且执行以下之一并把 `EXC_RETURN` 值加载到 **PC** 时：

- 包含加载 **PC** 的 `POP` 或 `LDM`。
- 以 **PC** 为目的寄存器的 `LDR`。
- 以任意寄存器为操作数的 `BX`。

该计数器在**尾链**时也会递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**PC_WRITE_RETIRED（0x000C，架构级）**

计数器对每次 **PC** 的软件修改递增。这包括以下全部：

- 分支指令。
- 循环开始指令。
- 循环结束指令。
- 显式写入 **PC** 的内存读指令。
- 显式写入 **PC** 的数据处理指令。

若实现了 **PACBTI 扩展**，则计数器计数通过 PAC 检查的、架构上执行的 `BXAUT` 指令。

以下一项或全部是否使计数器递增，是 **IMPLEMENTATION DEFINED** 的：

- `BKPT` 指令。
- 因指令 **UNDEFINED** 而产生的异常。
- 产生异常的指令 `SVC` 与 `UDF`。

`ISB` 是否作为 **PC** 的软件修改计数，是 **IMPLEMENTATION DEFINED** 的。

除上述列表明确指出的异常外，计数器不因其他异常递增。条件分支仅在分支被跳转时计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BR_IMMED_RETIRED（0x000D，架构级）**

计数器计数所有架构上执行的立即数分支指令，包括任何 `B` 分支指令或 `CBNZ` 指令的立即数变体。条件分支无论是否跳转都始终计数。若把 `ISB` 作为 **PC** 的软件修改计数，则 `ISB` 是否作为立即数分支指令计数是 **IMPLEMENTATION DEFINED** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BR_RETURN_RETIRED（0x000E，架构级）**

计数器计数函数返回指令。例如，以下非穷尽列表给出被计数的指令：

- `BX LR`。
- `MOV PC, LR`。
- `POP ..., PC`。
- `LDR PC, [SP], #offset`。
- 以任意寄存器为操作数的 `BXNS`。
- 以 `FNC_RETURN` 为目标地址的任何间接分支。

若实现了 **PACBTI 扩展**，则计数器计数通过 PAC 检查的、架构上执行的 `BXAUT` 指令。

以下是不被计数的指令的非穷尽列表：

- 操作数不是 `LR` 的 `BX`。
- 写入的寄存器不是 `LR` 的任何 `MOV PC`。
- `LDM SP, ..., PC`，因为未指定写回。
- `LDR PC, [SP, #offset]`，因为其寻址模式不正确。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**UNALIGNED_LDST_RETIRED（0x000F，架构级）**

当 `CCR.UNALIGN_TRP` 为 1 时，计数器计数每次会产生 **UNALIGNED** UsageFault 的内存读或内存写指令访问。该事件是否计数产生故障的访问（包括确实产生 **UNALIGNED** UsageFault 的访问），是 **IMPLEMENTATION DEFINED** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BR_MIS_PRED（0x0010，微架构级）**

计数器计数每一次因分支预测资源的预测错误或未预测而发生的、对已预测程序流的纠正，且该纠正与被分支预测资源能够预测的指令有关。若未实现任何程序流预测资源，**Arm** 建议计数器计数所有未跳转的分支。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**CPU_CYCLES（0x0011，微架构级）**

计数器在每个周期递增。所有计数器都受时钟频率变化的影响，包括 `WFI` 或 `WFE` 指令停止时钟时。这意味着当 `WFI` 与 `WFE` 指令停止时钟时，`CPU_CYCLES` 是否继续递增是 **CONSTRAINED UNPREDICTABLE** 的。与 `PMU_CCNTR` 不同，该计数不受 `PMU_CTRL.DP` 或 `PMU_CTRL.C` 影响：

- 计数器在禁止区域内不递增，且不受 `PMU_CTRL.DP` 影响。
- 该计数器在事件计数器被 `PMU_CTRL.P` 复位时被复位，但绝不被 `PMU_CTRL.C` 复位。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BR_PRED（0x0012，微架构级）**

计数器计数分支预测资源能够预测的每个分支或程序流的其他变化。若所有分支都受预测，则所有分支都是**可预测分支**。若分支在分支预测器之前被译码，从而使分支预测逻辑只动态预测部分分支（例如条件分支与间接分支），则其他分支是否作为可预测分支计数是 **IMPLEMENTATION DEFINED** 的。**Arm** 建议计数所有分支。

实现可能包含其他预测分支的结构，例如把短距离后向直接分支预测为跳转的**循环缓冲区**。此类分支的每次执行都是一次可预测分支。结束循环可能产生一个由 `BR_MIS_PRED` 计数的预测错误事件。

若未实现任何程序流预测资源，则该事件是可选的，但 **Arm** 建议 `BR_PRED` 计数所有分支。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MEM_ACCESS（0x0013，微架构级）**

计数器计数 **PE** 发出的内存读或内存写操作。无论该访问导致对 Level 1 数据或统一高速缓存、Level 2 数据或统一高速缓存的访问，还是两者都不访问，计数器都递增。以下原因不使计数器递增：

- 指令内存访问。
- 高速缓存维护指令。
- 来自任何高速缓存的写回。
- 任何高速缓存的重填。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L1I_CACHE（0x0014，微架构级）**

参见 `L<n>I_CACHE`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L1D_CACHE_WB（0x0015，微架构级）**

参见 `L<n>D_CACHE_WB`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L2D_CACHE（0x0016，微架构级）**

参见 `L<n>D_CACHE`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L2D_CACHE_REFILL（0x0017，微架构级）**

参见 `L<n>D_CACHE_REFILL`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L2D_CACHE_WB（0x0018，微架构级）**

参见 `L<n>D_CACHE_WB`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BUS_ACCESS（0x0019，微架构级）**

计数器计数访问 **PE** 及其紧耦合高速缓存边界之外的内存读或内存写操作。该计数器不包括对 **TCM** 的访问或来自 **TCM** 的访问。这条边界相对于任何已实现高速缓存的位置是 **IMPLEMENTATION DEFINED** 的。

**总线访问**的定义是 **IMPLEMENTATION DEFINED** 的，但从物理上看它是一次单请求而非突发（即总线有效的每个总线周期）。

总线访问包括数据、指令与统一高速缓存的重填与写回。总线访问是否包括确实使用总线但不显式传输数据的操作，是 **IMPLEMENTATION DEFINED** 的。

当 **PE** 之外的请求者发出导致总线访问的请求（例如一致性请求）时，产生一次**不可归属**总线访问。若总线是共享的，则只计数**可归属**的总线访问；若总线不共享，则计数所有总线访问。

若实现在该边界有多条总线，则该事件计数所有总线上访问之和。若总线支持每周期多次访问（例如通过多通道），则计数器对每个在该周期活动的通道各递增一次，因此某一周期内可能递增多于一次。任一周期内的最大递增值是 **IMPLEMENTATION DEFINED** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MEMORY_ERROR（0x001A，微架构级）**

计数器计数由与该 **PE** 紧耦合的内存所指示的每次内存错误。**本地内存**的定义是 **IMPLEMENTATION DEFINED** 的，但包括高速缓存与紧耦合存储器。**内存错误**指硬件检测到的物理错误，例如奇偶校验或 **ECC** 错误。它包括可纠正与不可纠正的错误，不包括架构中定义的错误，例如 **MPU** 或 **SAU** 故障。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**INST_SPEC（0x001B，微架构级）**

计数器计数 **PE** 推测执行的指令，包括随后未架构上执行的指令。因此，该事件计数的指令数大于架构上执行的指令数。**推测执行**的定义是 **IMPLEMENTATION DEFINED** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BUS_CYCLES（0x001D，微架构级）**

计数器在 **PE** 外部内存接口的每个周期递增。若实现以与处理器硬件相同的速率给外部内存接口提供时钟，则计数器计数每个周期。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**CHAIN（0x001E，架构级）**

偶数编号计数器绝不因该事件递增。这意味着 **CHAIN** 事件把奇数编号计数器与其前面的偶数编号计数器链接起来，构成 32 位计数器。**CHAIN** 事件意味着系统可以提供 N 个 16 位计数器、N/2 个 32 位计数器，或 16 位与 32 位计数器的混合。两个计数器的递增相对软件或外部计数器访问是原子的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L1D_CACHE_ALLOCATE（0x001F，微架构级）**

计数器对每次**可归属**的写递增：该写把一整行写入 Level 1 高速缓存，且不从 Level 1 高速缓存之外取数，例如来自合并缓冲区的整行写。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L2D_CACHE_ALLOCATE（0x0020，微架构级）**

计数器对每次**可归属**的写递增：该写把一整行写入 Level 2 高速缓存，且不从 Level 1 或 Level 2 高速缓存之外取数，例如：

- 从 Level 1 到 Level 2 高速缓存的写回。
- 来自合并缓冲区的整行写。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BR_RETIRED（0x0021，架构级）**

计数器计数架构上执行路径上所有一旦预测错误就会付出代价的分支。以下各项是否包括在内是 **IMPLEMENTATION DEFINED** 的：

- 无条件直接分支指令。
- 产生异常的指令。
- 异常返回指令。
- 上下文同步指令。

条件分支无论是否跳转都始终计数。**Arm** 建议 `BR_RETIRED` 计数无条件直接分支指令。若同时实现了 `PC_WRITE_RETIRED` 与 `BR_RETIRED`，则 **PE** 必须对两个事件以相同方式对待以下类型的指令：

- `BKPT` 指令。
- **UNDEFINED** 指令。
- `SVC` 指令。
- 上下文同步屏障指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BR_MIS_PRED_RETIRED（0x0022，微架构级）**

计数器计数 `BR_RETIRED` 所计数但未被正确预测的所有指令。若未实现任何程序流预测资源，则该事件计数所有已退役的未跳转分支。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**STALL_FRONTEND（0x0023，微架构级）**

计数器对 `CPU_CYCLES` 事件计数的每个周期计数：在该周期内，由于前端没有可供该 **PE** 发射的操作，因而没有操作被发射。前端与后端之间的划分是 **IMPLEMENTATION DEFINED** 的。前端与后端事件在同一流水线位置计数。对于 Fetch > Decode > Issue > Execute > Retire 的简化流水线模型，**Arm** 建议在指令从 Decode 派发到 Issue 时计数这些事件。在某一周期内，若后端无法接受任何操作且前端也没有可供发射的操作，则两个事件都可能被计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**STALL_BACKEND（0x0024，微架构级）**

计数器对 `CPU_CYCLES` 事件计数的每个周期计数：在该周期内，由于以下任一原因而没有操作被发射：

- 后端无法接受该 **PE** 可供发射的任何操作。
- 后端无法接受任何操作。例如，后端可能因资源冲突或资源不可用而无法接受操作。

前端与后端之间的划分是 **IMPLEMENTATION DEFINED** 的。前端与后端事件在同一流水线位置计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L2I_CACHE（0x0027，微架构级）**

参见 `L<n>I_CACHE`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L2I_CACHE_REFILL（0x0028，微架构级）**

参见 `L<n>I_CACHE_REFILL`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L3D_CACHE_ALLOCATE（0x0029，微架构级）**

计数器对每次**可归属**的写递增：该写把一整行写入 Level 3 高速缓存，且不从 Level 1、Level 2 或 Level 3 高速缓存之外取数，例如：

- 从 Level 2 到 Level 3 高速缓存的写回。
- 来自合并缓冲区的整行写。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L3D_CACHE_REFILL（0x002A，微架构级）**

参见 `L<n>D_CACHE_REFILL`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L3D_CACHE（0x002B，微架构级）**

参见 `L<n>D_CACHE`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L3D_CACHE_WB（0x002C，微架构级）**

参见 `L<n>D_CACHE_WB`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**LL_CACHE_RD（0x0036，微架构级）**

参见 `L<n>D_CACHE_RD`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**LL_CACHE_MISS_RD（0x0037，微架构级）**

参见 `L<n>D_CACHE_MISS_RD`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L1D_CACHE_LMISS_RD（0x0039，微架构级）**

参见 `L<n>D_CACHE_MISS_RD`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**OP_RETIRED（0x003A，微架构级）**

计数器计数 `OP_SPEC` 所计数、且随后提交到该 **PE** 架构状态的每个操作。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**OP_SPEC（0x003B，微架构级）**

计数器计数该 **PE** 发送执行的**可归属**指令或操作的数量，包括未提交到该 **PE** 架构状态的那些。该事件可能是 `INST_SPEC` 的别名。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**STALL（0x003C，微架构级）**

计数器计数每个**可归属**周期：在该周期内，该 **PE** 没有**可归属**的指令操作被发送执行。前端与后端之间的划分是 **IMPLEMENTATION DEFINED** 的。`STALL`、`STALL_FRONTEND` 与 `STALL_BACKEND` 事件在同一流水线位置计数。对于 Fetch、Decode、Issue、Execute、Retire 的简化流水线模型，**Arm** 建议在指令从 Decode 派发到 Issue 时计数这些事件。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**STALL_SLOT_BACKEND（0x003D，微架构级）**

计数 `STALL_SLOT` 所计数的每个槽位：在该槽位上，由于以下任一原因而没有**可归属**的指令或操作被发送执行：

- 后端无法接受该 **PE** 在该槽位上可供使用的指令操作。
- 后端无法在该槽位上接受任何操作。

前端与后端之间的划分是 **IMPLEMENTATION DEFINED** 的。`STALL_SLOT`、`STALL_SLOT_FRONTEND` 与 `STALL_SLOT_BACKEND` 事件在同一流水线位置计数。在某一周期内，若后端无法接受任何操作且前端也没有可供发射的操作，则 `STALL_SLOT_FRONTEND` 与 `STALL_SLOT_BACKEND` 两个事件都可能被计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**STALL_SLOT_FRONTEND（0x003E，微架构级）**

计数 `STALL_SLOT` 所计数的每个槽位：在该槽位上，由于前端没有可供该 **PE** 在该槽位上发射的**可归属**指令或操作，因而没有**可归属**的指令或操作被发送执行。前端与后端之间的划分是 **IMPLEMENTATION DEFINED** 的。`STALL_SLOT`、`STALL_SLOT_FRONTEND` 与 `STALL_SLOT_BACKEND` 事件在同一流水线位置计数。在某一周期内，若后端无法接受任何操作且前端也没有可供发射的操作，则 `STALL_SLOT_FRONTEND` 与 `STALL_SLOT_BACKEND` 两个事件都可能被计数。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**STALL_SLOT（0x003F，微架构级）**

计数器在每个**可归属**周期计数未被该 **PE** 的**可归属**指令或操作占用的指令或操作槽位数量。**槽位**的定义是 **IMPLEMENTATION DEFINED** 的，但每个周期可用的槽位数量 WIDTH 是固定的，因此公式 `STALL_SLOT / (CPU_CYCLES × WIDTH)` 给出该 **PE** 的**可归属**指令或操作对处理器槽位的利用率。每个槽位每周期最多容纳一条指令或一个操作。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**L1D_CACHE_RD（0x0040，微架构级）**

参见 `L<n>D_CACHE_RD`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**LE_RETIRED（0x0100，微架构级）**

计数器对每条架构上执行的循环结束（LE）指令递增，条件是该指令在 `LO_BRANCH_INFO` 缓存内登记了一个条目。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**LE_SPEC（0x0101，微架构级）**

计数器对每条推测执行的循环结束（LE）指令递增，条件是该指令在 `LO_BRANCH_INFO` 缓存内登记了一个条目。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BF_RETIRED（0x0104，微架构级）**

计数器对每条架构上执行的分支未来指令递增，条件是该指令在 `LO_BRANCH_INFO` 缓存内登记了一个条目。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BF_SPEC（0x0105，微架构级）**

计数器对每条推测执行的分支未来指令递增，条件是该指令在 `LO_BRANCH_INFO` 缓存内登记了一个条目。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**LE_CANCEL（0x0108，微架构级）**

`LO_BRANCH_INFO` 缓存含有由循环结束指令建立的有效循环条目时被清除，且该清除不与循环的最后一次迭代重合。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**BF_CANCEL（0x0109，微架构级）**

`LO_BRANCH_INFO` 缓存含有由分支未来指令建立的有效分支条目时被清除，且该清除不与一次被跳转的隐式分支重合。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**SE_CALL_S（0x0114，架构级）**

计数器对每条架构上执行、且导致安全状态由 **Non-secure** 切换到 **Secure** 的 `SG` 指令递增。**Arm** 建议该计数器递增时不受施加于 PMU 的安全状态过滤的影响。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**SE_CALL_NS（0x0115，架构级）**

计数器对每条架构上执行、且导致安全状态由 **Secure** 切换到 **Non-secure** 的 `BLXNS` 指令递增。**Arm** 建议该计数器递增时不受施加于 PMU 的安全状态过滤的影响。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DWT_CMPMATCH0（0x0118，架构级）**

参见 `DWT_CMPMATCH<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DWT_CMPMATCH1（0x0119，架构级）**

参见 `DWT_CMPMATCH<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DWT_CMPMATCH2（0x011A，架构级）**

参见 `DWT_CMPMATCH<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DWT_CMPMATCH3（0x011B，架构级）**

参见 `DWT_CMPMATCH<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DWT_CMPMATCH4（0x011C，架构级）**

参见 `DWT_CMPMATCH<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DWT_CMPMATCH5（0x011D，架构级）**

参见 `DWT_CMPMATCH<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DWT_CMPMATCH6（0x011E，架构级）**

参见 `DWT_CMPMATCH<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DWT_CMPMATCH7（0x011F，架构级）**

参见 `DWT_CMPMATCH<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**PAC_RETIRED（0x0130，微架构级）**

计数器计数 `INST_RETIRED` 所计数的每个操作，其中架构上执行的指令为 `PAC`、`PACBTI` 或 `PACG`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**PAC_SPEC（0x0131，微架构级）**

计数器计数 `INST_SPEC` 所计数的每个操作，其中推测执行的指令为 `PAC`、`PACBTI` 或 `PACG`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**AUT_RETIRED（0x0134，微架构级）**

计数器计数 `INST_RETIRED` 所计数的每个操作，其中架构上执行的指令为 `AUT` 或 `AUTG`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**AUT_SPEC（0x0135，微架构级）**

计数器计数 `INST_SPEC` 所计数的每个操作，其中推测执行的指令为 `AUT` 或 `AUTG`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**STALL_BACKEND_PAC（0x013C，微架构级）**

计数器计数 `STALL_BACKEND` 所计数的每个操作，其中因有 PAC 操作正在进行而无法发射操作。这包括由 `PAC`、`PACBTI`、`PACG`、`AUT` 与 `AUTG` 指令引起的 PAC 停顿。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_INST_RETIRED（0x0200，架构级）**

计数器对每条受 **beat 化执行**（beat-wise execution）约束的、架构上执行的 MVE 指令递增。这包括部分或完全谓词化的指令，以及从异常返回后恢复执行的指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_INST_SPEC（0x0201，微架构级）**

计数器对每条受 **beat 化执行**约束的、推测执行的 MVE 指令递增。这包括随后未架构上执行的指令。因此，该事件计数的指令数可能大于架构上执行的指令数。**推测执行**的定义是 **IMPLEMENTATION DEFINED** 的。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_FP_RETIRED（0x0204，架构级）**

计数器对 `MVE_INST_RETIRED` 所计数的、对浮点数据进行操作的每条架构上执行的 MVE 指令递增。这包括转换为浮点表示或由浮点表示转换的 MVE 转换指令，以及浮点向量比较与向量谓词指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_FP_SPEC（0x0205，微架构级）**

计数器对 `MVE_INST_SPEC` 所计数的、对浮点数据进行操作的每条推测执行的 MVE 指令递增。这包括转换为浮点表示或由浮点表示转换的 MVE 转换指令，以及浮点向量比较与向量谓词指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_FP_HP_RETIRED（0x0208，架构级）**

计数器对 `MVE_FP_RETIRED` 所计数的、对浮点数据进行操作、且额外对半精度数据进行操作的每条架构上执行的 MVE 浮点指令递增。这包括转换为半精度浮点表示或由其转换的 MVE 转换指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_FP_HP_SPEC（0x0209，微架构级）**

计数器对 `MVE_FP_SPEC` 所计数的、对浮点数据进行操作、且额外对半精度数据进行操作的每条推测执行的 MVE 浮点指令递增。这包括转换为半精度浮点表示或由其转换的 MVE 转换指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_FP_SP_RETIRED（0x020C，架构级）**

计数器对 `MVE_FP_RETIRED` 所计数的、对浮点数据进行操作、且额外对单精度数据进行操作的每条架构上执行的 MVE 浮点指令递增。这包括转换为单精度浮点表示或由其转换的 MVE 转换指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_FP_SP_SPEC（0x020D，微架构级）**

计数器对 `MVE_FP_SPEC` 所计数的、对浮点数据进行操作、且额外对单精度数据进行操作的每条推测执行的 MVE 浮点指令递增。这不包括转换为单精度浮点表示或由其转换的 MVE 转换指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_FP_MAC_RETIRED（0x0214，架构级）**

计数器对执行乘法或乘加操作的每条架构上执行的 MVE 浮点指令递增。这包括执行融合乘加（fused multiply-accumulation）的指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_FP_MAC_SPEC（0x0215，微架构级）**

计数器对执行乘法或乘加操作的每条推测执行的 MVE 浮点指令递增。这包括执行融合乘加的指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_INT_RETIRED（0x0224，架构级）**

计数器对每条架构上执行的 MVE beat 化整数或定点指令递增。这不包括任何浮点转换指令，但包括整数向量比较与向量谓词指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_INT_SPEC（0x0225，微架构级）**

计数器对每条推测执行的 MVE beat 化整数或定点指令递增。这不包括任何浮点转换指令，但包括整数向量比较与向量谓词指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_INT_MAC_RETIRED（0x0228，架构级）**

计数器对 `MVE_INT_RETIRED` 所计数的、且额外执行乘法或乘加操作的每条架构上执行的 MVE 整数或定点指令递增。这包括归约变体。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_INT_MAC_SPEC（0x0229，微架构级）**

计数器对 `MVE_INT_SPEC` 所计数的、且额外执行乘法或乘加操作的每条推测执行的 MVE 整数或定点指令递增。这包括归约变体。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_RETIRED（0x0238，架构级）**

计数器对每条架构上执行的、向 Q 寄存器写数据的 MVE 加载指令，或从 Q 寄存器取数据的存储指令递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_SPEC（0x0239，微架构级）**

计数器对每条推测执行的、向 Q 寄存器写数据的 MVE 加载指令，或从 Q 寄存器取数据的存储指令递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_RETIRED（0x023C，架构级）**

每当 `MVE_LDST_RETIRED` 因加载操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_SPEC（0x023D，微架构级）**

每当 `MVE_LDST_SPEC` 因加载操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_RETIRED（0x0240，架构级）**

每当 `MVE_LDST_RETIRED` 因存储操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_SPEC（0x0241，微架构级）**

每当 `MVE_LDST_SPEC` 因存储操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_CONTIG_RETIRED（0x0244，微架构级）**

每当一条连续内存加载或存储指令架构上执行、并产生最优数量的内存访问时，计数器递增。对提升为连续访问的 scatter-gather 指令，计数器也递增。无论是否对齐，计数器都递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_CONTIG_SPEC（0x0245，微架构级）**

每当一条连续内存加载或存储指令推测执行、并产生最优数量的内存访问时，计数器递增。对提升为连续访问的 scatter-gather 指令，计数器也递增。无论是否对齐，计数器都递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_CONTIG_RETIRED（0x0248，微架构级）**

每当 `MVE_LDST_CONTIG_RETIRED` 因加载操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_CONTIG_SPEC（0x0249，微架构级）**

每当 `MVE_LDST_CONTIG_SPEC` 因加载操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_CONTIG_RETIRED（0x024C，微架构级）**

每当 `MVE_LDST_CONTIG_RETIRED` 因存储操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_CONTIG_SPEC（0x024D，微架构级）**

每当 `MVE_LDST_CONTIG_SPEC` 因存储操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_NONCONTIG_RETIRED（0x0250，微架构级）**

每当一条非连续内存加载或存储指令架构上执行、且产生的访问数多于等价的连续操作时，计数器递增。无论完成该指令执行需要多少额外内存请求，计数器只递增一次。若 scatter-gather 指令被提升为连续内存访问，则计数器不递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_NONCONTIG_SPEC（0x0251，微架构级）**

每当一条非连续内存加载或存储指令推测执行、且产生的访问数多于等价的连续操作时，计数器递增。无论完成该指令执行需要多少额外内存请求，计数器只递增一次。若 scatter-gather 指令被提升为连续内存访问，则计数器不递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_NONCONTIG_RETIRED（0x0254，微架构级）**

每当 `MVE_LDST_NONCONTIG_RETIRED` 因加载操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_NONCONTIG_SPEC（0x0255，微架构级）**

每当 `MVE_LDST_NONCONTIG_SPEC` 因加载操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_NONCONTIG_RETIRED（0x0258，微架构级）**

每当 `MVE_LDST_NONCONTIG_RETIRED` 因存储操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_NONCONTIG_SPEC（0x0259，微架构级）**

每当 `MVE_LDST_NONCONTIG_SPEC` 因存储操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_MULTI_RETIRED（0x025C，架构级）**

每当 `VLD2x`、`VST2x`、`VLD4x` 或 `VST4x` 指令架构上执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_MULTI_SPEC（0x025D，微架构级）**

每当 `VLD2x`、`VST2x`、`VLD4x` 或 `VST4x` 指令推测执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_MULTI_RETIRED（0x0260，架构级）**

每当 `VLD2x` 或 `VLD4x` 指令架构上执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_MULTI_SPEC（0x0261，微架构级）**

每当 `VLD2x` 或 `VLD4x` 指令推测执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_MULTI_RETIRED（0x0264，架构级）**

每当 `VST2x` 或 `VST4x` 指令架构上执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_MULTI_SPEC（0x0265，微架构级）**

每当 `VST2x` 或 `VST4x` 指令推测执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_UNALIGNED_RETIRED（0x028C，微架构级）**

当 `MVE_LDST_RETIRED` 因某条指令而递增、且该指令因非对齐而需要一次或多次额外内存访问时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_UNALIGNED_SPEC（0x028D，微架构级）**

当 `MVE_LDST_SPEC` 因某条指令而递增、且该指令因非对齐而需要一次或多次额外内存访问时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_UNALIGNED_RETIRED（0x0290，微架构级）**

当 `MVE_LDST_UNALIGNED_RETIRED` 因加载操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LD_UNALIGNED_SPEC（0x0291，微架构级）**

当 `MVE_LDST_UNALIGNED_SPEC` 因加载操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_UNALIGNED_RETIRED（0x0294，微架构级）**

当 `MVE_LDST_UNALIGNED_RETIRED` 因存储操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_ST_UNALIGNED_SPEC（0x0295，微架构级）**

当 `MVE_LDST_UNALIGNED_SPEC` 因存储操作而递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_UNALIGNED_NONCONTIG_RETIRED（0x0298，微架构级）**

当 `MVE_LDST_UNALIGNED_RETIRED` 与 `MVE_LDST_NONCONTIG_RETIRED` 同时递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_LDST_UNALIGNED_NONCONTIG_SPEC（0x0299，微架构级）**

当 `MVE_LDST_UNALIGNED_SPEC` 与 `MVE_LDST_NONCONTIG_SPEC` 同时递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_VREDUCE_RETIRED（0x02A0，架构级）**

每当一条对向量进行操作、产生存于通用寄存器的标量结果的 MVE 指令架构上执行时，计数器递增。这仅包括带「V」后缀的指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_VREDUCE_SPEC（0x02A1，微架构级）**

每当一条对向量进行操作、产生存于通用寄存器的标量结果的 MVE 指令推测执行时，计数器递增。这仅包括带「V」后缀的指令。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_VREDUCE_FP_RETIRED（0x02A4，架构级）**

当 `MVE_VREDUCE_RETIRED` 与 `MVE_FP_RETIRED` 同时递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_VREDUCE_FP_SPEC（0x02A5，微架构级）**

当 `MVE_VREDUCE_SPEC` 与 `MVE_FP_SPEC` 同时递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_VREDUCE_INT_RETIRED（0x02A8，架构级）**

当 `MVE_VREDUCE_RETIRED` 与 `MVE_INT_RETIRED` 同时递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_VREDUCE_INT_SPEC（0x02A9，微架构级）**

当 `MVE_VREDUCE_SPEC` 与 `MVE_INT_SPEC` 同时递增时，该计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_PRED（0x02B8，微架构级）**

计数器在每个**架构节拍**（Architecture tick）递增：在该节拍内，一条 MVE beat 化指令的一个或多个 beat 架构上完成，且其中一个或多个 beat 被 **VPR** 或循环尾部谓词化部分或完全置为假。若某个 beat 被异常中断因而未架构上完成，或该 beat 在异常后恢复执行时被 `EPSR.ECI` 屏蔽，则 **Arm** 建议计数器不递增。于是比值 `(MVE_PRED × BEATS_PER_TICK) / (4 × MVE_INST_RETIRED)` 可近似反映受谓词化影响的 MVE 指令比例，其中 `BEATS_PER_TICK` 是每个**架构节拍**执行的平均 beat 数（含来自不同重叠指令的 beat），由 **IMPLEMENTATION DEFINED** 决定。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_STALL（0x02CC，微架构级）**

计数器对 `CPU_CYCLES` 事件计数的每个周期计数：在该周期内，由于一条正在执行或试图执行的 MVE 指令，直接导致没有操作被发射。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_STALL_RESOURCE（0x02CD，微架构级）**

当 `MVE_STALL` 递增，且原因是 MVE 指令因 **PE** 中没有能够执行该指令的可用资源而无法执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_STALL_RESOURCE_MEM（0x02CE，微架构级）**

当 `MVE_STALL` 递增，且原因是 MVE 指令因 **PE** 中没有能够执行该指令的可用存储器资源而无法执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_STALL_RESOURCE_FP（0x02CF，微架构级）**

当 `MVE_STALL` 递增，且原因是 MVE 指令因 **PE** 中没有能够执行该指令的可用浮点资源而无法执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_STALL_RESOURCE_INT（0x02D0，微架构级）**

当 `MVE_STALL` 递增，且原因是 MVE 指令因 **PE** 中没有能够执行该指令的可用整数资源而无法执行时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_STALL_BREAK（0x02D3，微架构级）**

当 `MVE_STALL` 递增，且原因是等待一条在途 MVE 指令完成时，计数器递增。一个可能的例子是：在执行标量指令之前，一条可链接的 MVE 指令先完成。**Arm** 建议只有在无法确定其他具体的可归属原因时才使计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**MVE_STALL_DEPENDENCY（0x02D4，微架构级）**

当 `MVE_STALL` 递增，且原因是后续指令为解析寄存器 **RAW** 冲突而被延迟时，计数器递增。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**ITCM_ACCESS（0x4007，微架构级）**

计数器计数 **PE** 对指令 **TCM** 发出的内存读或内存写操作。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**DTCM_ACCESS（0x4008，微架构级）**

计数器计数 **PE** 对数据或统一 **TCM** 发出的内存读或内存写操作。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**TRCEXTOUT0（0x4010，微架构级）**

参见 `TRCEXTOUT<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

**TRCEXTOUT1（0x4011，微架构级）**

参见 `TRCEXTOUT<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

**TRCEXTOUT2（0x4012，微架构级）**

参见 `TRCEXTOUT<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

**TRCEXTOUT3（0x4013，微架构级）**

参见 `TRCEXTOUT<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

**CTI_TRIGOUT4（0x4018，微架构级）**

参见 `CTI_TRIGOUT<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

**CTI_TRIGOUT5（0x4019，微架构级）**

参见 `CTI_TRIGOUT<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

**CTI_TRIGOUT6（0x401A，微架构级）**

参见 `CTI_TRIGOUT<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

**CTI_TRIGOUT7（0x401B，微架构级）**

参见 `CTI_TRIGOUT<n>`。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU && DSPDE。

## 11. 必需的 PMU 事件

架构要求 PMU 至少支持以下公共事件：

- `0x0000` `SW_INCR`：架构上执行的指令，条件码检查通过，软件递增。
- `0x0003` `L1D_CACHE_REFILL`：可归属的 Level 1 数据高速缓存重填。
  - 仅当实现包含 Level 1 数据或统一高速缓存时，才要求该事件。
- `0x0004` `L1D_CACHE`：可归属的 Level 1 数据高速缓存访问。
  - 仅当实现包含 Level 1 数据或统一高速缓存时，才要求该事件。
- `0x0008` `INST_RETIRED`：架构上执行的指令。
- `0x0011` `CPU_CYCLES`：周期。
- `0x0021` `BR_RETIRED`：架构上执行的指令，分支。
  - 仅当实现包含程序流预测时，才要求该事件。
- `0x0022` `BR_MIS_PRED_RETIRED`：架构上执行的指令，预测错误的分支。
  - 仅当实现包含程序流预测时，才要求该事件。
- `0x0023` `STALL_FRONTEND`：因前端而无操作发射。
- `0x0024` `STALL_BACKEND`：因后端而无操作发射。
- `0x0200` `MVE_INST_RETIRED`：架构上执行的 MVE 指令。
  - 仅当实现包含 MVE 时，才要求该事件。
- `0x0238` `MVE_LDST_RETIRED`：架构上执行的 MVE 加载或存储指令。
  - 仅当实现包含 MVE 时，才要求该事件。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

## 12. IMPLEMENTATION DEFINED 事件编号

对于 **IMPLEMENTATION DEFINED** 事件编号，每个计数器被独立定义为以下之一：

- 对每个事件只递增一次。
- 计数事件持续的时间。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**Arm** 建议实现者为自己的 **IMPLEMENTATION DEFINED** 事件建立标准化编号方案，对所有实现采用公共定义与公共计数值。总体上，**Arm** 建议在具有公共特性的实现之间实现标准化。不过，**Arm** 也认识到，试图在过宽的实现范围内对微架构特性的编码进行标准化并不会产生良好效果。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。

**Arm** 强烈建议 **IMPLEMENTATION DEFINED** 事件应允许用户度量实现认为对系统性能重要的任何微架构特性的利用率，以及任何对最优性能的显著偏离。

适用于 **Armv8.1-M** 及以后架构版本的实现。扩展要求为 - PMU。
