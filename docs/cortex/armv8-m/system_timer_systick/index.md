---
title: "系统定时器，SysTick（The System Timer, SysTick）"
---

本章规定 **Armv8-M** 系统定时器规则。

## 1. 系统定时器，SysTick

在不带 **Main Extension** 且不带 **Security Extensions** 的 **PE** 中，以下之一成立：

- 未实现任何系统定时器。
- 实现了一个系统定时器 **SysTick**。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - !M && !S。

在不带 **Main Extension** 但带 **Security Extension** 的 **PE** 中，以下之一成立：

- 未实现任何系统定时器。
- 实现一个系统定时器 **SysTick**，由 `ICSR.STTNS` 决定该 **SysTick** 归哪个**安全状态**所有。
- 实现两个系统定时器：
  - **SysTick**，**Secure** 实例。
  - **SysTick**，**Non-secure** 实例。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - !M && S。

在带 **Main Extension** 但不带 **Security Extension** 的 **PE** 中，实现一个系统定时器 **SysTick**。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - M && !S。

在带 **Main Extension** 与 **Security Extensions** 的 **PE** 中，实现两个系统定时器：

- **SysTick**，**Secure** 实例。
- **SysTick**，**Non-secure** 实例。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - M && S。

存在以下 **SysTick** 寄存器：

- **SysTick 控制与状态寄存器**（SysTick Control and Status Register，`SYST_CSR`）。
- **SysTick 重装载值寄存器**（SysTick Reload Value Register，`SYST_RVR`）。
- **SysTick 当前值寄存器**（SysTick Current Value Register，`SYST_CVR`）。
- **SysTick 校准值寄存器**（SysTick Calibration Value Register，`SYST_CALIB`）。

在带 **Security Extension** 且每个**安全状态**都专用一个 **SysTick** 实例的 **PE** 中，这些寄存器是分存储体的。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST。

每个已实现的 **SysTick** 都是一个 24 位、递减、归零回绕、写入清零的计数器：

- 使能时，计数器从 `SYST_CVR` 中的值开始递减。到达零时，`SYST_CVR` 在下一个时钟边沿被重新装载为 `SYST_RVR` 中保存的值。
- 读取 `SYST_CVR` 返回该读访问时刻计数器的值。
- 计数器到达零时，将 `SYST_CSR.COUNTFLAG` 置 1。读取 `SYST_CSR.COUNTFLAG` 会将其清为 0。
- 对 `SYST_CVR` 的写入把 `SYST_CVR` 与 `SYST_CSR.COUNTFLAG` 都清为 0。随后 `SYST_CVR` 在下一个时钟边沿被重新装载为 `SYST_RVR` 中保存的值。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST。

向 `SYST_RVR` 写入 0 会使 **SysTick** 在下次归零回绕时被禁用。回绕之后计数器保持为零。即使 `SYST_CSR.ENABLE` 为 1，也是如此。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST。

对 `SYST_CVR` 的写入不会引起 **SysTick** 异常。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST。

将 `SYST_CSR.TICKINT` 置 1，会使 **SysTick** 到达零时 **SysTick** 异常变为挂起。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST。

**Arm** 建议，在通过 `SYST_CSR.ENABLE` 使能 **SysTick** 之前，软件先把所需的计数值写入 `SYST_RVR`，然后写入 `SYST_CVR` 以把 `SYST_CVR` 清为零。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST。

软件可以选择使用 `SYST_CALIB.TENMS`，在计数器的动态范围内把计数器换算到其他时钟频率。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST。

当 **PE** 在调试状态下停机时，任何已实现的 **SysTick** 都不递减。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST && HDBG。

每个已实现的 **SysTick** 都由一个参考时钟驱动，即 **PE** 时钟或外部系统时钟。使用哪一个时钟作为外部参考时钟是 **IMPLEMENTATION DEFINED** 的。**Arm** 建议，若使用外部系统时钟，则应记录 **PE** 时钟与外部时钟之间的关系，以便在计算系统时序时把亚稳态、时钟偏移与抖动考虑在内。

适用于 **Armv8.0-M** 及以后架构版本的实现。扩展要求为 - ST。
