<section id="title">多级缓存架构（Multilevel Cache Organisation）</section>

# 1. 多级缓存

高速缓存（**Cache**）是 **CPU** 用来减少访问内存的平均时间的随机存取存储器。

多级缓存（**Multilevel Caches**）是通过减少未命中惩罚（**MISS PENALTY**）来提高缓存性能的技术之一。 未命中惩罚（**Miss Penalty**）是指每当缓存中出现未命中时，将数据从主内存带入缓存所需的额外时间。

为了清楚地理解，让我们考虑一个示例，其中 **CPU** 需要 **10** 个内存引用来访问所需的信息，并在以下3种系统设计案例中考虑这种情况：

## 1.1. 案例 1：没有高速缓存的系统设计

![Figure1-1](Figure1-1.png)

这里 CPU 直接与主存通信，不涉及缓存。

在这种情况下，**CPU** 需要访问主存储器 **10** 次才能访问所需的信息。

## 1.2. 案例 2：带有高速缓存的系统设计

![Figure1-2](Figure1-2.png)

在这里，**CPU** 首先检查缓存内存中是否存在所需的数据，即缓存中是否存在命中（**hit in the cache**）或未命中（**miss in the cache**）。假设缓存内存中有**3**次未命中，那么主内存将仅被访问**3**次。我们可以看到，这里的未命中惩罚（**Miss Penalty**）减少了，因为主内存的访问次数比前一种情况少。

## 1.3. 案例 3：具有多级高速缓存的系统设计

![Figure1-3](Figure1-3.png)

这里通过引入多级缓存进一步优化了缓存性能。如上图所示，我们正在考虑2级缓存设计。假设在 **L1** 缓存内存中有 **3** 次未命中，而在这 **3** 次未命中中，**L2** 缓存内存中有 **2** 次未命中，则主存储器将仅被访问 **2** 次。很明显，这里的未命中惩罚（**Miss Penalty**）比前一种情况显着减少，从而提高了高速缓存的性能。

**注意：**

从以上 **3** 种情况我们可以看出，我们正在尝试减少主内存引用的数量，从而减少未命中惩罚（**Miss Penalty**）以提高整体系统性能。此外，需要注意的是，在多级缓存设计中，**L1** 缓存是附加在 **CPU** 上的，它体积小但速度快。虽然，**L2** 缓存附加到主缓存，即 **L1** 缓存，它的大小更大且速度较慢，但仍比主内存快。

```
Effective Access Time = Hit rate * Cache access time
                      + Miss rate * Lower level access time
```

多级缓存的平均访问时间：（T<sub>avg</sub>）

T<sub>avg</sub> = H<sub>1</sub> * C<sub>1</sub> + (1 – H<sub>1</sub>) * (H<sub>2</sub> * C<sub>2</sub> +(1 – H<sub>2</sub>) *M ) 

* **H**<sub>1</sub> 是 **L1** 缓存中的命中率。
* **H**<sub>2</sub> 是 **L2** 缓存中的命中率。
* **C**<sub>1</sub> 是访问 **L1** 缓存中信息的时间。
* **C**<sub>2</sub> 是将信息从 **L2** 缓存传输到 **L1** 缓存的未命中惩罚。
* **M** 是将信息从主存储器传输到 **L2** 高速缓存的未命中惩罚。

**示例：**

求具有 **2ns** 时钟周期时间、每条指令 **0.04** 次未命中率、**25** 个时钟周期的未命中惩罚和 **1** 个时钟周期的高速缓存访问时间（包括命中检测）的处理器的平均内存访问时间。 此外，假设读取和写入未命中惩罚相同，并忽略其他写入停顿。

**解决方案**

平均内存访问时间AMAT（**Average Memory access time**）= 命中时间（**Hit Time**） + 未命中率（**Miss Rate**） * 未命中惩罚（**Miss Penalty**）。

命中时间（**Hit Time**） = 1个时钟周期（Hit time = Hit rate * access time），但是这里命中时间（**Hit Time**）是直接给定的，

未命中率 = 0.04

未命中惩罚（**Miss Penalty**）= 25个时钟周期（这是上一级内存命中后所用的时间）

所以，**AMAT** = 1 + 0.04 * 25。

**AMAT** = 2 个时钟周期

根据问题 1 时钟周期 = 2 ns ， AMAT = 4ns。

## 1.4. 原文出处

* [https://www.geeksforgeeks.org/multilevel-cache-organisation/](https://www.geeksforgeeks.org/multilevel-cache-organisation)