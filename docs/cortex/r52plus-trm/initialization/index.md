---
title: "初始化（Initialization）"
---

本章介绍 Cortex®-R52+ 处理器的初始化注意事项。

## 1. 初始化

Cortex®-R52+ 处理器提供了一种在复位后初始化所有程序可见寄存器的机制，包括那些没有架构定义复位值的寄存器。

Cortex®-R52+ 处理器中的大多数架构寄存器，例如 r0-r14，以及包含 **Advanced SIMD** 时的 s0-s31 和 d0-d31，在复位后具有 **UNKNOWN** 值。因此，在使用这些寄存器之前，必须针对所有模式使用立即数 **MOV** 指令或 PC 相对加载指令对它们进行初始化。

**当前程序状态寄存器（Current Program Status Register, CPSR）** 以及部分系统寄存器字段在复位时被赋予已知值，更多信息请参见《ARM® Architecture Reference Manual for A-profile architecture》。

Cortex®-R52+ 处理器提供了一种在复位后将所有程序可见寄存器初始化为固定值的机制，如第 54 页的 4.2 Register summary 所述。该机制由 **CFGINITREG** 控制。有关 **CFGINITREG** 的更多信息，请参见《Arm® Cortex®-R52+ Processor Integration Manual》。

此外，在运行应用程序之前，你可能希望：

* 将特定值编程到各种寄存器，例如栈指针。
* 使能各种特性，例如纠错。
* 将特定值编程到内存，例如 **TCM**。

本节包含以下小节：

* 1.1 MPU。
* 1.2 浮点单元。
* 1.3 缓存。
* 1.4 推测。

### 1.1. MPU

在使用 **MPU** 之前，必须编程并使能至少一个区域，并在 **SCTLR** 或 **HSCTLR** 中使能 **MPU**。

除非至少有一个 **MPU** 区域已编程并处于活动状态，否则不要使能 **MPU**。如果使能了 **MPU**，则在使用 **TCM** 之前，必须编程覆盖 **TCM** 区域的 **MPU** 区域，以便为它们授予访问权限。

### 1.2. 浮点单元

在执行浮点指令之前，必须使能 **Advanced SIMD** 或**浮点单元（Floating-point Unit, FPU）**。

按如下方式使能 **FPU**：

* 在第 82 页的 4.3.1 **架构特性访问控制寄存器（Architectural Feature Access Control Register）** 中使能对 **FPU** 的访问。
* 通过设置 **FPEXC** 寄存器中的 **EN** 位使能 **FPU**。

### 1.3. 缓存

如果 Cortex®-R52+ 处理器构建时包含指令缓存或数据缓存，则在处理器使用它们之前会自动无效化，除非 **CFGL1CACHEINVDISx** 被拉高。

此操作永远不会报告任何 **ECC** 错误。

### 1.4. 推测

Cortex®-R52+ 核可以在复位后禁用多种形式的推测（**speculation**），直到显式使能它们。

该机制由 **CFGSAFETYBOOTx** 引脚控制，该引脚仅在复位后采样。

下表列出了引脚置位时被禁用的推测类型，以及受影响的位域及其对应值。

| 推测类型 | 受影响的位域 | 引脚置位时的位域值 |
| --- | --- | --- |
| 指令侧推测访问（**Instruction side Speculative access**） | **CPUACTLR.L1IPFCTL** | 0b0 |
| 数据侧推测访问（**Data side Speculative access**） | **CPUACTLR.L1DPFCTL** | 0b000 |
| 指令预取（**Instruction prefetch**） | **CPUACTLR.ISPECDIS** | 0b1 |
| 数据预取（**Data prefetch**） | **CPUACTLR.DSPECDIS** | 0b1 |
| 动态分支预测（**Dynamic branch prediction**） | **IMP_BPCTLR.DBPEL0DIS**、**IMP_BPCTLR.DBPEL1DIS**、**IMP_BPCTLR.DBPEL2DIS** | 0b1 |

开启推测通常能显著提升性能，无论是为分支提供正确的预测，还是提前预取程序所需的指令或数据。因此，只要条件允许，就应使能这些推测形式，以获得更高的每周期指令数。

有关这些寄存器的更多信息，请参见第 99 页的 4.3.19 CPU Auxiliary Control Register 和第 87 页的 4.3.10 Branch Predictor Control Register。

## 2. TCM

**TCM** 既可用于指令也可用于数据。还可以将 Cortex®-R52+ 处理器配置为复位后即使用 **ATCM**。

本节包含以下小节：

* 2.1 预加载 TCM。
* 2.2 带 ECC 的 TCM 预加载。
* 2.3 复位后使用 TCM。

### 2.1. 预加载 TCM

可以使用存储指令或 **AXIS** 接口将数据写入 **TCM**。

取决于所选择的方法，可能需要：

* 所用 **SoC** 上的特定硬件，例如 **DMA** 引擎。
* 引导代码。
* 连接到处理器的调试器。

预加载 **TCM** 的方法包括：

* **使用运行中的引导代码进行内存复制（Memory copy with running boot code）**：引导代码包含一个内存复制例程，它从外部内存读取数据并写入相应的 **TCM**。为此必须使能 **TCM**，并且可能需要在复制期间为 **TCM** 提供一个基地址，而在运行应用程序时提供另一个基地址。
* **从调试通信通道复制数据（Copy data from the Debug Communications Channel）**：引导代码包含一个从**调试通信通道（Debug Communications Channel, DCC）** 读取数据并写入 **TCM** 的例程。调试主机通过写入处理器 **APB** 调试接口上的相应寄存器，将用于此操作的数据送入 **DCC**。
* **在调试暂停状态下执行代码（Execute code in debug halt state）**：调试主机使 Cortex®-R52+ 处理器进入调试暂停状态，然后通过**指令传输寄存器（Instruction Transfer Register, EDITR）** 向其送入指令。Cortex®-R52+ 处理器执行这些指令，作为前述两种方法中使用引导代码的替代方案。
* **通过 DMA 写入 TCM（DMA into TCM）**：**SoC** 包含一个 **DMA** 设备，它从 **ROM** 读取数据并通过 **AXIS** 接口写入 **TCM**。

### 2.2. 带 ECC 的 TCM 预加载

如果 **TCM** RAM 中存在错误码位，Cortex®-R52+ 处理器不会初始化它们。在使能 **ECC** 的情况下读取 RAM 位置之前，必须先初始化错误码位。

要在不检测错误的情况下更新 **TCM** 位置，必须禁用 **ECC** 校验，或者写入的宽度必须与本节所述错误保护方案所保护的数据块相同且对齐。

可以使用 **CFGTCMBOOTx** 信号在退出复位时使能 **ATCM**，并使用 **CFGRAMPROTEN** 信号在退出复位时使能 **TCM**（以及缓存）**ECC**。内核运行期间，可以使用第 182 页的 4.3.76 **内存保护控制寄存器（Memory Protection Control Register）** 使能和禁用 **TCM ECC**。

可以按照以下规则，在开启或关闭错误检查的情况下初始化 **TCM** RAM。

* 如果使用 **AXIS** 接口在使能 **ECC** 的情况下初始化 **TCM**，则 **AXI** 从事务必须从 128 位对齐地址开始，写入连续的内存块，并使能块中的所有字节。
* 如果通过在 Cortex®-R52+ 处理器上运行代码来初始化，最好使用写满整个 **TCM** 内存的存储指令循环，如下所示：
  * 对于 **BTCM** 或 **CTCM**，使用 **Store Word（STR）**、**Store Two Words（STRD）** 或 **Store Multiple Words（STM）** 指令写入 32 位对齐地址。
  * 对于 **ATCM**，使用 **STRD**，或使用 **STM** 写入 64 位对齐地址。

**注意：** 可以使用 Cortex®-R52+ 处理器的对齐检查特性来帮助确保内存访问是 32 位对齐的，但没有针对 64 位对齐的检查。如果使用 **STRD** 或 **STM**，当地址不是 32 位对齐时会生成对齐故障。要获得与 **STR** 指令相同的行为，请通过设置第 203 页的 4.3.92 **系统控制寄存器（System Control Register）** 或第 147 页的 4.3.53 **Hyp 系统控制寄存器（Hyp System Control Register）** 中的 **A** 位来使能严格对齐检查。

### 2.3. 复位后使用 TCM

Cortex®-R52+ 处理器为每个内核提供一个主输入，当其被断言时，内核在复位后不会开始执行指令。这使得可以在内核启动之前预加载 **TCM**。

如果在该输入去断言之前发出外部调试请求，则内核在执行任何指令之前进入调试暂停状态。

可以使用 **CFGTCMBOOTx** 信号使能复位后的 **ATCM**。这使你可以将处理器配置为从 **TCM** 引导，但要做到这一点，必须首先将引导代码预加载到 **TCM**。

当处理器处于复位状态时，可以断言 **CPUHALTx** 输入，以防止处理器在退出复位后取指和执行指令。当处理器以这种方式暂停时，可以将相应数据预加载到 **TCM**。当 **CPUHALTx** 输入去断言时，处理器按常规方式从复位向量地址开始取指。

**注意：** 当 **CPUHALTx** 已去断言以启动处理器取指后，不得再次断言它，除非内核处于内核热复位或上电复位状态。

## 3. 进入 EL1

Cortex®-R52+ 处理器始终引导进入 **Hyp 模式（EL2）**。

如果不需要使用 **EL2**，可以对处理器进行编程并切换到 **EL1**，使其除通过复位外永远无法返回 **EL2**。这涉及将所有异常都设置为在 **EL1** 处理，并禁用 **HVC** 以及 **EL2** 控制的 **MPU**。

要进入 **EL1**：

* 编程 **HACTLR** 寄存器，因为它默认只允许 **EL2** 访问。**HACTLR** 控制 **EL1** 是否可以访问内存区域寄存器和 **CPUACTLR**。
* 在进入 **EL1** 之前编程 **SPSR**。
* 其他寄存器默认允许复位后从 **EL1** 访问。
* 将 **VBAR** 设置为向量表的正确位置。
* 通过将 **HCR.HCD** 置为 1 禁用 **HVC** 指令。
* 将 **ELR** 设置为指向 **EL1** 代码的入口点，并调用 **ERET**。
