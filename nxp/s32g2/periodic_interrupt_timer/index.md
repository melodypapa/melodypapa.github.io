<section id="title">周期性中断定时器 (**PIT**)</section>

# 1. 芯片特定的 PIT 信息

## PIT 模块实例详情

在此芯片中，除了用于引发中断和触发 DMA 通道的定时器通道外，PIT 模块是以下应用来源：

* FlexCAN 自由运行定时器的外部时间滴答（**The external time tick for the FlexCAN free-running timer**）
* FlexRay 秒表计数器的外部操作系统刻度（**The external OS tick for the FlexRay stopwatch counter**）

