<section id="title">内存保护单元（Memory Protection Unit）</section>

本章介绍 **MPU**。

# 1. 关于 MPU

**Cortex®-R52+** 处理器具有两个可编程 **MPU**，由 **EL1** 和 **EL2** 控制。每个 **MPU** 允许将 **4GB** 内存地址范围细分为多个区域。

每个内存区域定义了基地址（**base address**）、限制地址（**limit address**）、访问权限（**access permissions**）和内存属性（**memory attributes**）。

有关 MPU 的更多信息，请参阅 Arm® 架构Armv8补充参考手册 （**Arm® Architecture Reference Manual Supplement Armv8**），了解更多 **Armv8-R AArch32** 架构配置文件。

对于数据访问，MPU 检查当前转换机制（**current translation regime**）是否允许对某个区域进行访问（读取或写入）。对于指令访问，MPU 检查该区域是否允许访问，以及转换机制是否允许执行。对于数据和指令访问，如果允许访问，MPU 将分配为该区域定义的内存属性。如果不允许访问，则发生权限错误。发生转换错误的原因如下：

* 如果访问命中其中一个 **MPU** 中的多个区域。
* 如果访问未命中任何 **MPU** 区域，并且无法使用背景区域（基于 **MPU** 配置和当前特权级别）。

由于流水线操作，处理器会尝试预测程序流（**program flow**）和未来的数据访问（**future data accesses**），所以它会在使用数据和指令之前获取它们。除非或直到流水线完成相应指令的执行，否则这些事务被称为推测事务（**speculative transactions**）。这可能会导致处理器生成允许区域之外的地址，或者没有权限尝试访问。在这些情况下，**MPU** 会阻止推测访问生成总线事务(**bus transactions**)，但不会引起转换或权限错误。

每个处理器内核都有一个 **EL1** 控制的 **MPU**，具有 **16**、**20** 或 **24** 个可编程区域，以及一个 **EL2** 控制的 **MPU**，后者可选地支持 **0**、**16**、**20** 或 **24** 个可编程区域。当 **EL2** 控制的 **MPU** 和虚拟化被使能时，所有使用 **EL0/EL1** 转换机制的事务都会在两个 **MPU** 中执行查找。将生成的属性组合起来，以便最少权限的属性（**least permissive attributes**）被采用。这两个阶段的保护允许虚拟机管理程序保留对 **EL0/EL1** 转换机制的控制，从而实现对虚拟化的支持。当软件执行使用 **EL2** 转换机制时，仅 **EL2** 控制的 **MPU**被使用。

#  2. MPU 区域

区域是从基地址（**base address**）开始延伸到限制地址（**limit address**）（包括：限制地址）的连续地址范围。

基地址由 **PRBAR** （**EL2** 控制的 **MPU** 的 **HPBAR**）配置。限制地址由 **PRLAR**（**EL2** 控制的 **MPU** 的 配置）配置。基地址与 **64** 字节边界对齐，限制地址与 **64** 字节边界以下的字节对齐。基地址和限制地址都包括在内，这意味着区域内的地址由以下公式给出：

```C
PRBAR.BASE:0b000000 <= address <= PRLAR.LIMIT:0b111111
```

其中冒号（**：**）是位连接运算符。

区域的最小为 **64** 个字节。

**PRBAR** 和 **PRLAR** 还包含：

| 名称           | 含义                                   |
| -------------- | -------------------------------------- |
| PRBAR.AP       | 访问权限（access permissions）         |
| PRBAR.SH       | 可共享性（shareability）               |
| PRBAR.XN       | 从不执行位（Execute-never bit）        |
| PRLAR.AttrIndx | 内存属性索引（memory attribute index） |

通过使用 **PRLAR.AttrIndx** 索引内存属性间接寄存器**MAIRx**（**Memory Attribute Indirection Registers**）来确定内存属性。

通过设置或清除区域启用位 (**PRLAR.EN**) 来启用或禁用区域。在 **EL2** 控制的 **MPU** 中，还可以通过写入 **Hypervisor MPU 区域启用寄存器 HPRENR** (**Hypervisor MPU Region Enable Register**) 来启用或禁用区域。

## 2.1. EL1 控制的MPU背景区域

当MPU被禁用（**SCTLR.M=0**）时，**EL1** 控制的MPU背景区域用作默认内存映射。

当MPU启用时，可以通过设置 **SCTLR.BR** 来启用背景区域。在这种情况下，来自 EL1 转换机制的访问如果未触及任何可编程区域，则将使用背景区域。当 MPU 启用时，来自 EL0 转换机制的访问将出现故障。

![SCTLR.M](SCTLR.M.png)

![SCTLR.BR](SCTLR.BR.png)

### 2.1.1. EL1 控制的MPU背景区域，指令访问

下表显示了EL1控制的MPU背景区域的指令访问。

![Table9-1](Table9-1.png)

### 2.1.2. EL1 控制的MPU背景区域，数据访问

下表显示了EL1控制的MPU背景区域的数据访问。

![Table9-2](Table9-2.png)

## 2.2. EL2控制的MPU背景区域

当EL2控制的MPU被禁用（**HSCTLR.M=0**）时，**EL2** 控制的背景区域用作所有访问的默认内存映射。

当EL2控制的MPU启用时，通过设置背景区域启用（**HSCTLR.BR=1**），它还可用于未命中任何可编程区域的 EL2 访问。当 EL2 控制的 MPU 启用时，来自 EL0/EL1 转换机制的访问如果未命中 EL2 可编程区域，则会产生转换故障。这是两阶段转换的结果。

![HSCTLR.M](HSCTLR.M.png)

![HSCTLR.BR](HSCTLR.BR.png)

### 2.1.1. EL2控制的MPU背景区域，指令访问

下表显示了用于指令访问的EL2控制的MPU背景区域。

![Table9-3](Table9-3.png)

### 2.1.2. EL2控制的MPU背景区域，数据访问

下表显示了用于数据访问的EL2控制的MPU背景区域。

![Table9-4](Table9-4.png)

## 2.3. 默认缓存能力

启用默认缓存能力 (**HCR.DC=1**) 后，使用 **EL1** 控制的 **MPU** 后台区域的事务将包含：**正常**(**Normal**)、**内部回写**(**Inner Write-Back**)、**外部回写**(**Outer Write-Back**)、**不可共享**(**Non-Shareable**)属性，同时启用**读取分配**(**Read-Allocate**)和**写入分配**(**Write-Allocate**)。当 **HCR.DC=1** 时，在后台区域中命中的指令访问始终可执行。

默认属性是最宽松的，这意味着当与来自 **EL2** 控制的 **MPU** 的任何属性结合时，生成的属性与 **EL2** 控制的 **MPU** 属性相同。这允许 **EL2** 控制的 **MPU** 有效地使 **EL1** 控制的 **MPU** 对来自后台区域中命中的 **EL1** 转换机制的事务透明。当 **HCR.DC=1** 时，来自 **EL0/EL1** 转换机制的所有转换都会执行两阶段 **MPU** 查找，处理器的行为就像设置了 **HCR.VM** 一样。

# 3. 虚拟化支持

为了支持虚拟化，需要执行两个阶段的MPU查找(**MPU lookup**)。

虚拟化允许在 **EL1** 和 **EL0** 上运行的进程（通常是一个或者多个客户操作系统及其应用程序）被在 **EL2** 上运行的进程（通常是单个虚拟机管理程序）进行管理。

* **EL1** 控制的 **MPU** 检查在 **EL0** 或 **EL1** 上运行的进程的事务，并由在 **EL1** 或 **EL2** 上运行的进程进行编程。
* 当启用虚拟化时，**EL2** 控制的 **MPU** 还会检查从 **EL0/EL1** 转换机制执行的事务，并由 **EL2** 上的软件进行编程。
* 在 **EL2** 转换机制下执行的事务仅使用 **EL2** 控制的 **MPU**。

当启用虚拟化（**HCR.VM=1**），并且启用 **EL2** 控制的 **MPU**（**HSCTLR.M=1**）时，**EL1** 控制的 **MPU** 允许的事务将由 **EL2** 控制的MPU检查，作为两阶段查找的一部分。如果两个 **MPU** 都允许该事务，则第1阶段的内存属性将与第2阶段中匹配区域的属性相结合，并将两组中更严格的属性应用于该事务。

## 3.1. 合并MPU内存属性

执行两阶段查找时，每个 **MPU** 的内存类型(**memory type**)、可缓存性(**cacheability**)和可共享性(**shareability**)属性会被合并。

**合并内存类型属性**

下表显示了内存类型分配如何作为两阶段查找的一部分进行组合。

![Table9-5](Table9-5.png)

**合并可缓存性属性**

下表显示了如何将可缓存性分配合并为两阶段查找的一部分。

![Table9-6](Table9-6.png)

**合并可共享性属性**

下表显示了如何将可共享性分配合并为两阶段查找的一部分。

![Table9-7](Table9-7.png)

# 4. MPU register access

The MPU base and limit registers can be accessed indirectly or directly. 

**Indirectly**

A region is selected by writing to the PRSELR (HPRSELR for EL2 MPU). The selected region is programmed by writing to the PRBAR and PRLAR (HPRBAR and HPRLAR for EL2 MPU). 

**Directly**

The base and limit registers, for region n, are directly accessed by encoding the region number into CRm and opcode2 of the following system register access instructions:

# 5. MPU Register summary

## 5.1. Protection Region Selection Register（PRSELR）

The PRSELR indicates, and selects the current EL1-controlled MPU region registers, PRBAR, and PRLAR.

**Usage constraints**

This register is accessible as follows:

| EL0 | EL1 | EL2 |
| --- | --- | --- |
| -   | RW  | RW  |

**Traps and enables**

The PRSELR is accessible from EL2, and from EL1 when VSCTLR.MSA is 0. 

**Configurations**

This register is available in all build configurations.

**Attributes**

PRSELR is a 32-bit register.

**0 or 16 EL2-controlled MPU regions**

The following figure shows the PRSELR bit assignments if 0 or 16 EL2-controlled MPU regions are implemented.

![Figure4_78](Figure4_78.png)

The following table shows the PRSELR bit assignments if 0 or 16 EL2-controlled MPU regions are implemented.

![Table4-201](Table4-201.png)

**20 or 24 EL2-controlled MPU regions**

The following figure shows the PRSELR bit assignments if 20 or 24 EL2-controlled MPU regions are implemented.

![Figure4_79](Figure4_79.png)

The following table shows the PRSELR bit assignments if 20 or 24  EL2-controlled MPU regions are implemented.

![Table4-202](Table4-202.png)

**To access the PRSELR:**

```arm
MRC p15, 0, <Rt>, c6, c2, 1 ; Read PRSELR into Rt
MCR p15, 0, <Rt>, c6, c2, 1 ; Write Rt to PRSELR
```

## 5.2. Protection Region Base Address Register（PRBAR）

## 5.3. Protection Region Limit Address Register（PRLAR）

## 5.4. Hyp Protection Region Base Address Register（）