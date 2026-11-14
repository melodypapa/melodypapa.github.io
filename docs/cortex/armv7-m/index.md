---
title: "Armv7-M 架构参考手册"
---

本专题收录《Armv7-M Architecture Reference Manual》(DDI0403E E.e) 中与 Cortex-M7 相关的架构章节中文翻译，按手册原章节顺序排列（Part A 应用程序级模型在前，Part B 系统级程序员模型在后）。

手册共 Part A 7 章（A1–A7）、Part B 5 章（B1–B5）、Part C 1 章（C1）与 Part D 附录 D1–D8。当前收录 Part A 的 A3、A5、A6，Part B 的 B2–B5，以及 Part D 的术语表，共 8 篇；A4、B1.5、B3.5 的译文并入 Cortex-M7 TRM 专题（见下文）；A1、A2、A7、C1 与其余附录尚未翻译。

## 1. 章节

### Part A — 应用程序级架构（Application level architecture）

1. [ARM架构的内存模式（Arm Architecture Memory Model）](part-a/arm_architecture_memory_mode/index.md)
2. [Thumb 指令集编码（Thumb Instruction Set Encoding）](part-a/thumb_instruction_set_encoding/index.md)
3. [浮点指令集编码（Floating-point Instruction Set Encoding）](part-a/fp_instruction_set_encoding/index.md)

### Part B — 系统级架构（System level architecture）

4. [系统内存模型（System Memory Model）](part-b/system_memory_model/index.md)
5. [系统地址映射](part-b/system_address_map/index.md)
6. [CPUID 方案（The CPUID Scheme）](part-b/cpuid_scheme/index.md)
7. [系统指令详情（System Instruction Details）](part-b/system_instructions/index.md)

### Part D — 附录（Appendices）

8. [术语表（Glossary）](part-d/glossary/index.md)

## 2. 相关内容

以下章节的译文同时覆盖本手册的对应架构章节，因与实现章节合为一篇，整篇归在 [Cortex-M7 TRM](../m7-trm/index.md) 专题：

- [程序员模型（Programmers Model）](../m7-trm/programmers_model/index.md) — 含 B1.5 异常模型
- [Cortex-M7 指令集](../m7-trm/instruction_set/index.md) — 含 A4 指令集
- [内存保护单元（Memory Protection Unit）](../m7-trm/mpu/index.md) — 含 B3.5 PMSAv7

未收录的 A1、A2、A7、C1 与其余附录见 `sync-todo/ARMv7-M.md` 中的队列。
