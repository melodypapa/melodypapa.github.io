---
title: "Full-CAN 与 Basic-CAN 的区别"
---



## 1. 简介和功能概述

本文介绍了 **CAN** 控制器硬件发展中形成的两种经典架构策略——**Full CAN**（**DPRAM** 模式）与 **Basic CAN**（**FIFO** 模式）——的历史起源、定义、技术差异及选型建议。

**注意：** AUTOSAR 等标准规范中并没有关于 **Full CAN** 和 **Basic CAN** 的正式定义，这两个术语仅用于区分早期 **CAN** 控制器的两种编程模型，且 **Full CAN** 绝不是比 **Basic CAN** 更完整地实现了 **CAN** 协议。

## 2. 缩略语

**CAN**
> 控制器局域网（**Controller Area Network**），一种广泛应用于汽车电子与工业控制的串行通信总线。

**DPRAM**
> 双端口随机存取存储器（**Dual Port RAM**），可同时被 **CPU** 与 **CAN** 控制器核心访问，是 **Full CAN** 架构的底层范例。

**FIFO**
> 先进先出队列（**First In First Out**），**Basic CAN** 架构采用的编程模型。

**Full CAN**
> 基于消息对象缓冲区（**Message Object Buffer**）的 **CAN** 控制器架构，底层范例为 **DPRAM**，因此也称为 **DPRAM 模式**。

**Basic CAN**
> 基于接收 **FIFO** 队列的 **CAN** 控制器架构，因此也称为 **FIFO 模式**。

**Message Object**
> 消息对象，**Full CAN** 架构中可独立配置 **ID** 过滤的接收/发送缓冲单元。

**RX / TX**
> 接收（**Receive**）/ 发送（**Transmit**）。

## 3. 历史

**Basic CAN** 和 **Full CAN** 这两个词起源于 **CAN** 网络的早期。

曾几何时，**Intel 82526** 的 **CAN** 控制器为开发人员提供了 **5** 个消息缓冲区的 **DPRAM** 样式的接口。紧随其后的 **Intel 82527** 具有 **15** 个消息缓冲区。

然后飞利浦试图降低成本，生产更便宜的版本，从而推出了 **82C200**：它由两个接收缓冲区和一个发送缓冲区，当然还有部分掩码匹配过滤。它使用了面向 **FIFO**（队列）的编程模型和有限的过滤能力。

为了区分这两种 **CAN** 控制器，有些人开始将 **Intel** 的原始版本称为 **Full CAN**，将低成本的 **Philips** 版本称为 **Basic CAN**。

## 4. 定义

其实在标准规范中并没有关于 **Full CAN** 和 **Basic CAN** 的真正定义，只有制造商才有。**Full CAN** 实际上应该称为 **DPRAM 模式**，因为它底层范例是 **DPRAM**。而 **Basic CAN** 应该真正称为 **FIFO 模式**。

新的 **CAN** 控制器扩展了基本功能，例如：它们具有多达 **32** 个对象缓冲区作为 **Full CAN** 的实现，或者它们具有用于多个消息的大型 **FIFO**，如：飞利浦 **SJA1000**，称为 **PeliCAN**，作为 **Basic CAN** 的实现。

使用多个控制器，您可以混合使用这些控制器。它们基本上是作为 **Full CAN** 实现的，但您可以使用一些对象缓冲区来构建一个 **FIFO**，并将它们用作 **Basic CAN**。

## 5. Full CAN 与 Basic CAN 的差异

**Full CAN** 和 **Basic CAN** 其实是 **CAN** 控制器架构中的两个不同设计策略。

**Full CAN** 控制器通常具有多个所谓的消息对象缓冲区。接收寄存器可以这样编程：只有一个特定的消息（或一组消息）被传递到这个对象缓冲区。大多数实现不会在接收队列中缓冲同类的对象消息，这意味着通过接收过滤器的后续消息将覆盖前一条消息，旧消息将丢失。如果两条 **ID** 相同但数据不同的消息发送间隔非常短（例如：**11** 位 **ID**、**2** 字节数据、**1 Mbit/s** 时约为 **70 us**），**CPU** 必须在第二条消息到达之前，将消息缓冲区中已接收的内容取走，否则前一个消息就会被覆盖。

典型的 **Basic CAN** 控制器（飞利浦 **SJA1000**）只有一个接收队列，本身没有消息对象缓冲区的概念，采用 **FIFO** 先入先出的机制。

| 对比项 | Full CAN | Basic CAN |
|--------|----------|-----------|
| 底层范例 | **DPRAM**（消息对象缓冲区） | **FIFO** 接收队列 |
| 别称 | **DPRAM 模式** | **FIFO 模式** |
| 消息过滤 | 每个消息对象独立配置，仅指定 **ID**（或 **ID** 组）进入对应缓冲区 | 整条队列共享有限的掩码匹配过滤 |
| 相同 **ID** 的后续消息 | 覆盖前一条消息，旧消息丢失 | 全部入队，不会丢失 |
| 典型控制器 | **Intel 82526 / 82527** | **Philips 82C200 / SJA1000**（**PeliCAN**） |
| 成本 | 较高 | 较低（飞利浦方案即为降低成本而推出） |

## 6. 如何选择

哪个策略更好主要取决于应用程序。如果应用程序使用的不同消息数量比硬件中的消息对象缓冲区数量少，那么 **Full CAN** 可能是更好些的选择。例如：芯片集成了两个 **CAN** 控制器，且这两个 **CAN** 控制器可以共享相同的 **RX/TX** 引脚，那就有 **32** 个消息对象缓冲区。

另一方面，如果您想接收系统中的**所有**消息，并且不希望相同 **ID** 的数据被覆盖，您应该使用 **FIFO** 样式的 **Basic CAN** 控制器。

**CAN** 的最大定义速度为 **1 Mbit/s**，您可能会每隔大约 **55 us**（没有数据的帧）获得一次中断。这取决于系统负载（以太网、串行、**PID** 环路等）。此外，这些设备带来的中断延迟和中断优先级差异，都会对 **CAN** 总线接收处理造成影响。

新型 **CAN** 控制器支持两种方式同时使用，例如英飞凌的 **SAK82C900**：它使用每个可用的（**82C900** 上为 **32** 个）消息对象缓冲区作为类似于 **Full CAN** 的缓冲区，也可以配置 **2、4、8、16** 或 **32** 个消息缓冲区来构建一个 **FIFO** 缓冲区。因此它能够同时兼具两个方案的优点。

## 7. 总结

今天，大多数 **CAN** 控制器都允许这两种编程模型，因此没有理由继续使用 **Full CAN** 和 **Basic CAN** 这两个术语。事实上，这些术语可能会引起混淆，应该避免使用。

当然，**Full CAN** 控制器可以与 **Basic CAN** 控制器通信，反之亦然。不存在任何兼容性的问题。

## 8. 参考信息

[1] CAN FAQ - Basic CAN vs. Full CAN
> [http://www.port.de/cgi-bin/CAN/CanFaqBasicFullCAN](http://www.port.de/cgi-bin/CAN/CanFaqBasicFullCAN)

[2] Difference between Full CAN and Basic CAN Mailbox - KBA86565
> [https://community.infineon.com/t5/Knowledge-Base-Articles/Difference-between-Full-CAN-and-Basic-CAN-Mailbox-KBA86565/ta-p/259191](https://community.infineon.com/t5/Knowledge-Base-Articles/Difference-between-Full-CAN-and-Basic-CAN-Mailbox-KBA86565/ta-p/259191)

<section id="wechat">

<h4>微信扫一扫，获取更多及时资讯</h4>

<img src="wechat.png" alt="微信扫一扫"/>

</section>
