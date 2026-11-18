---
title: "Armv7-M 中的已弃用特性（Deprecated Features in Armv7-M）"
---

本附录列出 **Armv7-M** 体系结构中**已弃用**（**deprecated**）的特性。本章包含以下小节：

* 第 D3-778 页的 **Armv7-M 体系结构的已弃用特性**。

## 1. Armv7-M 体系结构的已弃用特性

本附录描述 **Armv7-M** 体系结构中为向后兼容而保留的特性。这些特性在 Arm 体系结构的未来版本中可能不再支持。Arm 强烈建议软件不要使用或依赖这些特性。

### 1.1. 已弃用的体系结构特性

本小节列出 **Armv7-M** 体系结构中已弃用的特性。另参见 **Armv7-M Thumb 指令集的已弃用特性**。

#### 1.1.1. 四字节栈对齐

**注意：** **Armv7-M** 实现是否支持四字节栈对齐为实现定义（**IMPLEMENTATION DEFINED**）。

某些 **Armv7-M** 实现支持四字节栈对齐，由 CCR.STKALIGN 位控制。Arm 反对任何对四字节栈对齐的使用。更多信息参见第 B1-535 页的**异常进入时的栈对齐**。

#### 1.1.2. 通过不压栈 LR 优化上下文切换

在某些情况下，上下文切换机制可能不把 LR 压栈，以小幅节省上下文切换时间。Arm 反对任何对这项优化的使用。更多信息参见第 B1-537 页的**进程切换时保存上下文**。

#### 1.1.3. 同时把 DWT_CTRL.PCSAMPLENA 与 DWT_CTRL.CYCEVTENA 置 1

软件可以把 POSTCNT 定时器配置为用于：

* 生成 **PC 采样包**：把 DWT_CTRL.PCSAMPLENA 置 1。
* 生成**事件计数包**：把 DWT_CTRL.CYCEVTENA 置 1。

在早期的 **Armv7-M** 实现中，同时把 DWT_CTRL.PCSAMPLENA 与 DWT_CTRL.CYCEVTENA 置 1 的效果，与把 DWT_CTRL.PCSAMPLENA 置 1、DWT_CTRL.CYCEVTENA 置 0 相同。Arm 反对把这两位同时置 1，并强烈建议软件只执行下列之一：

* 把两位都置 0，以禁用 POSTCNT 定时器。
* 把其中一位置 1、另一位置 0，以启用 POSTCNT 定时器的某种特定用途。

更多信息参见第 C1-732 页的 **POSTCNT 定时器**。

### 1.2. Armv7-M Thumb 指令集的已弃用特性

**Armv7-M Thumb** 指令集是唯一的 **Armv7 Thumb** 指令集的一个版本。该指令集的某些特性在 **Armv7** 中已弃用。**Armv7-M** 所支持指令的已弃用特性包括：

* 在 16 位 `ADD`（SP 加寄存器）指令中把 PC 用作 `&lt;Rd&gt;` 或 `&lt;Rm&gt;`。
* 在下列指令中把 SP 用作 `&lt;Rm&gt;`：
    * 16 位 `ADD`（SP 加寄存器）指令。
    * 16 位 `CMP`（寄存器）指令。
* 使用 `&lt;Rd&gt;` 与 `&lt;Rm&gt;` 同时为 SP 或 PC 的 `MOV`（寄存器）指令。
* 在带基址寄存器回写的 16 位 `STM` 指令的寄存器列表中，把 `&lt;Rn&gt;` 用作编号最小的寄存器。
* 在 `MSR` 指令中把不带 `_<bits>` 限定符的 APSR 用作参数，作为 APSR-`_nzcvq` 的别名。
