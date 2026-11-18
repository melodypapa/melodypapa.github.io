---
title: "Armv7-M CoreSight 基础设施 ID（Armv7-M CoreSight Infrastructure IDs）"
---

本附录描述 **Armv7-M** 对 **CoreSight** 管理寄存器与**基础设施 ID**（**Infrastructure IDs**）的实现。本章包含以下小节：

* 第 D1-766 页的 **Armv7-M 实现的 CoreSight 基础设施 ID**。

## 1. Armv7-M 实现的 CoreSight 基础设施 ID

**Armv7-M** 实现支持 **SCS**、**FPB**、**DWT** 与 **ITM** 单元，以及一张 **ROM** 表，参见第 C1-686 页的表 C1-3。《Arm® CoreSight™ 体系结构规范》（Arm® CoreSight™ Architecture Specification）定义了 **CoreSight** 体系结构的程序员模型，它为每个 **CoreSight** 组件定义一个 4KB 寄存器块。每个 4KB 寄存器块细分为下列区域：

* **组件 ID**（**Component ID**），位于偏移 0xFF0 到 0xFFF。
* **外设 ID**（**Peripheral ID**），位于偏移 0xFD0 到 0xFEF。
* **CoreSight** 管理寄存器，位于偏移 0xF00 到 0xFCF。
* 器件特定寄存器，位于偏移 0x000 到 0xEFF。

对 **Armv7-M**，**ROM** 表必须实现组件 ID 寄存器，且 **DWT**、**ITM**、**FPB** 与 **TPIU** 单元必须实现符合 **CoreSight** 的管理锁访问机制。除此之外，所有 ID 与管理寄存器均为保留，建议把它们实现为符合 **CoreSight** 或 RAZ，以促进各调试工具链支持方式的一致性。

**注意：** 符合 **CoreSight** 的锁访问机制实现为 RAZ。锁机制仅适用于处理器对被影响单元的软件访问。通过 **DAP** 的访问始终允许，这意味着锁状态寄存器从 **DAP** 侧访问时必须为 RAZ。

为确定 **Armv7-M** 调试基础设施的拓扑，**ROM** 表项指示某个单元是否存在。单元存在即保证支持 **Armv7-M** 对 **DWT**、**ITM**、**FPB** 与 **TPIU** 的编程要求。附加功能需要附加支持，此时推荐以 **CoreSight** 作为框架。

确定处理器支持的体系结构变体与特性细节时，必须使用 **SCS** 中的 **CPUID** 支持。

表 D1-1 给出组件 ID 与外设 ID 寄存器格式。

表 D1-1 组件与外设 ID 寄存器格式：

| 地址偏移 | 取值ᵃ | 名称 | 描述 | 参考 |
| --- | --- | --- | --- | --- |
| 0xFFC | 0x000000B1 | CID3 | Component ID3 | 前导码 |
| 0xFF8 | 0x00000005 | CID2 | Component ID2 | 前导码 |
| 0xFF4 | 0x000000X0 | CID1 | Component ID1 | Bits[7:4] Component Class<br>Bits[3:0] 前导码 |
| 0xFF0 | 0x0000000D | CID0 | Component ID0 | 前导码 |
| 0xFEC | 0x000000YY | PID3 | Peripheral ID3 | Bits[7:4] RevAnd，次修订字段<br>Bits[3:0] 若为非零，表示客户修改过的块 |
| 0xFE8 | 0x000000YX | PID2 | Peripheral ID2 | Bits[7:4] Revision<br>bit[3] == 1：JEDEC 分配的 ID 字段<br>Bits[2:0] JEP106 ID code[6:4] |
| 0xFE4 | 0x000000XY | PID1 | Peripheral ID1 | Bits[7:4] JEP106 ID code[3:0]<br>Bits[3:0] Part Number[11:8] |
| 0xFE0 | 0x000000YY | PID0 | Peripheral ID0 | Part Number[7:0] |
| 0xFDC | 0x00000000 | PID7 | Peripheral ID7 | 保留 |
| 0xFD8 | 0x00000000 | PID6 | Peripheral ID6 | 保留 |
| 0xFD4 | 0x00000000 | PID5 | Peripheral ID5 | 保留 |
| 0xFD0 | 0x000000YX | PID4 | Peripheral ID4 | Bits[7:4] 4KB count<br>Bits[3:0] JEP106 continuation code |

a. 对 Value 列中的表项，标记为 X 的位由《Arm® CoreSight™ 体系结构规范》定义，标记为 Y 的位为实现定义（**IMPLEMENTATION DEFINED**）。

在 **Armv7-M** 中，所有 **CoreSight** 寄存器都按字访问。对《Arm® CoreSight™ 体系结构规范》中定义的任何 8 位或 16 位寄存器，均按零扩展的字访问。

关于寄存器及其位字段的更多信息，参见《Arm® CoreSight™ 体系结构规范》中的 **CoreSight** 程序员模型。

**注意：** JEDEC 定义的字段指块设计者的 JEDEC JEP106 代码。部件号、设计者与组件类字段的组合必须唯一。

表 D1-2 列出 **CoreSight** 锁访问机制寄存器。

表 D1-2 CoreSight 软件锁寄存器：

| 地址偏移 | 类型 | 寄存器名称 | 备注 |
| --- | --- | --- | --- |
| 0xFB4 | RO | Lock Status（LSR） | 若未实现，该位置为 RAZ。 |
| 0xFB0 | WO | Lock Access（LAR） | 读取为 UNKNOWN。 |

Arm 建议所有保留寄存器空间实现为符合 **CoreSight** 或 RAZ。

**CoreSight** 管理寄存器的完整描述参见《Arm® CoreSight™ 体系结构规范》。
