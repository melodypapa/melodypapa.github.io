<section id="title">直写和回写缓存（Write Through and Write Back in Cache）</section>

# 1. 直写和回写缓存

高速缓存（**Cache**）是一种将数据副本临时存储在可快速访问的存储内存中的技术。缓存将最近使用的数据存储在小内存中，以提高访问数据的速度。它充当 **RAM** 和 **CPU** 之间的缓冲区，从而提高处理器可用数据的速度。

每当处理器想要写入一个字时，它都会检查它想要写入数据的地址是否存在于缓存中。如果地址存在于缓存中，即写入命中（**Write Hit**）。

我们可以更新缓存中的值并避免昂贵的主内存访问。但这会导致数据不一致（**Inconsistent Data**）问题。由于高速缓存和主存都有不同的数据，如在多处理器系统中，这将导致两个或多个共享主存的设备出现问题。

这就是直写（**Write Through**）和回写（**Write Back**）出现的地方。

## 1.1. 直写（Write Through）

![Figure1-1](Figure1-1.png)

在直写（**Write Through**）场景中，数据同时更新到缓存和内存（**simultaneously updated to cache and memory**）。这个过程更简单，更可靠。这用于没有频繁写入缓存的情况（写入操作的次数较少）。

它有助于数据恢复（在断电或系统故障的情况下）。因为我们必须写入两个位置（内存和缓存），数据写入将经历延迟。虽然它解决了不一致的问题，但它的问题是在写操作中使用缓存的优势，因为使用缓存的全部目的是避免对主内存的多次访问。

## 1.2. 回写（Write Back）

![Figure1-2](Figure1-2.png)

数据只在缓存中更新，稍后再更新到内存中。仅当缓存行准备好替换时，内存中的数据才会更新。

缓存行替换会使用以下算法：

* [Belady异常](https://www.geeksforgeeks.org/beladys-anomaly-in-page-replacement-algorithms)（**Belady’s Anomaly**）
* 最近最少使用（Least Recently Used Algorithm）
* 先进先出（**FIFO**）
* 后进先出（**LIFO**)
* 其他取决于应用程序的算法

回写也称为延迟写入。

变脏标志位（**Dirty Bit**）：缓存中的每个块都需要一个位来指示缓存中存在的数据是被修改（变脏的）还是未被修改（干净的）。如果它是干净的，则无需将其写入内存。它旨在减少对内存的写操作。如果缓存发生故障（**Cache fails**）或系统发生故障（**System fails**）或断电（**Power outages**），修改后的数据将丢失。因为如果数据丢失了，几乎不可能从缓存中恢复数据。

如果写入发生在缓存中不存在的位置（**Write Miss**），我们有两个选项：写分配（**Write Allocation**）和绕写法（**Write Around**）。

### 1.2.1. 写分配（Write Allocation）

![Figure1-3](Figure1-3.png)

在写分配（**Write Allocation**）中，数据从内存加载到缓存中，然后再更新。写分配（**Write Allocation**）同时适用于回写（**Write Back**）和直写（**Write Through**）。但它通常与回写（**Write Back**）一起使用，因为这样不需要将数据从内存中带入缓存，然后再把数据更新缓存和主内存中。从而直写（**Write Through**）通常与不写分配（**No Write Allocate**）一起使用。

### 1.2.2. 绕写法（Write Around）

![Figure1-4](Figure1-4.png)

这里数据直接写入或者更新到主存而不干扰缓存。当数据无需立即再次使用时，最好使用这种方法。

## 1.3. 原文出处

* [https://www.geeksforgeeks.org/write-through-and-write-back-in-cach](https://www.geeksforgeeks.org/write-through-and-write-back-in-cach)