<section id="title">Cortex-M7 程序状态寄存器</section>

程序状态寄存器**PSR**（**Program Status Register**）包含了：

* 应用程序状态寄存器**APSR**（**Application Program Status Register**）。
* 中断程序状态寄存器**IPSR**（**Interrupt Program Status Register**）。
* 执行程序状态寄存器**EPSR**（**Execution Program Status Register**）。

这些寄存器是 **32** 位 **PSR** 中互斥的位域。位分配是：

![](psr_figure_1.png)