---
title: "Armv7-M 架构参考手册（DDI0403E E.e）"
---

本专题收录《Armv7-M Architecture Reference Manual》(DDI0403E E.e) 中与 Cortex-M7 相关的架构章节中文翻译，按手册原章节顺序排列（Part A 应用程序级模型在前，Part B 系统级程序员模型在后）。

## 1. 章节

1. [ARM架构的内存模式（Arm Architecture Memory Model）](arm_architecture_memory_mode/index.md)
2. [Thumb 指令集编码（Thumb Instruction Set Encoding）](thumb_instruction_set_encoding/index.md)
3. [浮点指令集编码（Floating-point Instruction Set Encoding）](fp_instruction_set_encoding/index.md)
4. [系统内存模型（System Memory Model）](system_memory_model/index.md)
5. [系统地址映射](system_address_map/index.md)
6. [CPUID 方案（The CPUID Scheme）](cpuid_scheme/index.md)
7. [系统指令详情（System Instruction Details）](system_instructions/index.md)

## 2. 相关内容

以下章节的译文同时覆盖本手册的对应架构章节，因与实现章节合为一篇，整篇归在 [Cortex-M7 TRM](../m7-trm/index.md) 专题：

- [程序员模型（Programmers Model）](../m7-trm/programmers_model/index.md) — 含 B1.5 异常模型
- [Cortex-M7 指令集](../m7-trm/instruction_set/index.md) — 含 A4 指令集
- [内存保护单元（Memory Protection Unit）](../m7-trm/mpu/index.md) — 含 B3.5 PMSAv7

未收录的 A1、A2、A7、C1 与附录 D 见 `sync-todo/armv7-m/` 中的延后清单。
