---
title: "Part B 系统级架构（System level architecture）"
---

Part B 描述本架构的系统级视图。它包含以下章节：

## 1. 章节

1. [系统内存模型（System Memory Model）](system_memory_model/index.md) — Chapter B2，提供 **Armv7-M** 内存模型的伪代码描述。
2. [系统地址映射](system_address_map/index.md) — Chapter B3（B3.1–B3.4），描述 **Armv7-M** 系统地址映射，包括内存映射寄存器；Chapter B3.3 为 SysTick，Chapter B3.4 为 NVIC。
3. [CPUID 方案（The CPUID Scheme）](cpuid_scheme/index.md) — Chapter B4，描述 CPUID 方案。它提供标识架构版本与处理器实现的诸多特性的寄存器。
4. [系统指令详情（System Instruction Details）](system_instructions/index.md) — Chapter B5，提供系统级指令的详细参考材料。
5. [程序员模型（Programmers Model）](../../m7-trm/programmers_model/index.md) — Chapter B1.5，给出 **Armv7-M** 程序员模型的系统级视图，包括异常模型。该节与 Cortex-M7 TRM 的实现章节合为一篇，归在 Cortex-M7 TRM 专题。
6. [内存保护单元（Memory Protection Unit）](../../m7-trm/mpu/index.md) — Chapter B3.5，可选的受保护内存系统架构（PMSAv7）。该节与 Cortex-M7 TRM 的实现章节合为一篇，归在 Cortex-M7 TRM 专题。

Chapter B1《系统级程序员模型》（System Level Programmers' Model）的其余小节尚未翻译，见 `sync-todo/ARMv7-M.md` 队列。

## 2. 相关内容

- [Armv7-M 架构参考手册](../index.md) — 本手册的文档落地页。
