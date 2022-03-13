<section id="title">Full-CAN vs. Basic-CAN</section>

# 1. 历史

**Basic CAN**和**Full CAN**这两个词起源于CAN网络的早期。

曾几何时**Intel 82526**的CAN控制器为开发人员提供了5个消息缓冲区的**DPRAM**样式的接口。紧随其后的**Intel 82527**具有15个消息缓冲区。

然后飞利浦试图降低成本，生产更便宜的版本，从而推出了**82C200**，它由两个接收缓冲区和一个发送缓冲区，当然还有部分掩码匹配过滤。它使用了面向**FIFO**（队列）的编程模型和有限的过滤能力。 

为了区分这两种CAN控制器，有些人开始将原始的**Intel**的版本称为**Full CAN**，将低成本的**Philips**的版本称为**Basic CAN**。

# 2. 定义

其实在标准规范中并没有关于**Full CAN**和**Basic CAN**的真正定义，只有制造商才有。**Full CAN**实际上应该称为**DPRAM 模式**，因为它底层范例是DPRAM。而**Basic CAN**应该真正称为**FIFO 模式**。同时请注意，**Full CAN**也绝不是比**Basic CAN**更完整的实现了CAN协议。

新的CAN控制器扩展了基本功能，例如：它们具有多达32个对象缓冲区作为**Full CAN**的实现，或者它们具有用于多个消息的大型**FIFO**，如:飞利浦**SJA1000**，称为**PeliCAN**，作为**Basic CAN**的实现。

使用多个控制器，您可以混合使用这些控制器。它们基本上是作为**Full CAN**实现的，但您可以使用一些对象缓冲区来构建**FIFO**并将它们用作**Baisc CAN**。

# 3. 哪个CAN控制器最好用

**Full CAN**和**Basic CAN**其实是CAN控制器架构中的两个不同设计策略。

**Full CAN**控制器通常具有多个所谓的消息对象缓冲区。接受寄存器可以这样编程，只有一个特定的消息（或一组）被传递到这个对象缓冲区。大多数实现不会在接收队列中缓冲同类的对象消息，这意味着通过接受过滤器的后续消息将替换前一个消息，并且旧消息将丢失。如果两条**ID**相同但数据不同的消息，发送速度非常快（考虑：11位ID，2个数据字节，1Mbit/s, 大概时间为**70us**），CPU必须在第二条消息到达之前，传递消息缓冲区的已接收的内容，否则前一个消息就会被覆盖。

典型的**Basic CAN**控制器（飞利浦 **SJA1000**）只有一个接收队列，本身没有消息缓冲区的概念，采用FIFO先入先出的机制。

哪个策略更好主要取决于应用程序。如果应用程序使用的不同消息数量比硬件中的消息对象数量缓冲区少，那么**Full CAN**可能是更好些的。如集成了两个CAN控制器，同时这两个CAN控制器可以共享相同的**RX/TX**引脚，那就有32个消息对象缓冲区。但另一方面，如果您想接收到系统中的**所有**消息，不需要相同ID数据被覆盖，您应该使用**FIFO**样式**Basic CAN**的控制器。

CAN的最大定义速度为**1Mbit/s**，您可能会每隔大约**55 us**（没有数据的帧）获得一次中断。这取决于系统负载（以太网、串行、 PID-loop等）。同时这些设备的所带来的中断延迟和不同的优先级都会造成CAN总线接收影响。

新型CAN控制器支持两种方式同时使用，像英飞凌**SAK82C900**这样，使用每个可用的（82C900 上为 32 个）消息对象缓冲区作为类似于**Full CAN**的缓冲区，也可以配置2、4、8、16 或32个消息缓冲区，来构建一个 FIFO 缓冲区。因此它能够同时兼具了两个方案的优点。

# 4. 总结

今天，大多数CAN控制器都允许这两种编程模型，因此没啥理由需要继续使用术语**Full CAN**和**Basic CAN**。事实上，这些术语可能会引起混淆，应该避免使用。

当然，**Full CAN**控制器可以与**Basic CAN**控制器通信，反之亦然。不存任何兼容性的问题。

# 5. 参考信息

[1] [http://www.port.de/cgi-bin/CAN/CanFaqBasicFullCAN](http://www.port.de/cgi-bin/CAN/CanFaqBasicFullCAN)

[2] [Difference between Full CAN and Basic CAN Mailbox - KBA86565](https://community.infineon.com/t5/Knowledge-Base-Articles/Difference-between-Full-CAN-and-Basic-CAN-Mailbox-KBA86565/ta-p/259191)

<section id="wechat">

<h4>微信扫一扫，获取更多及时资讯</h4>

<img src="wechat.png" alt="微信扫一扫"/>

</section>