---
title: "Armv8-M 架构参考手册"
---

本专题收录《Armv8-M Architecture Reference Manual》(DDI0553B B.y) 中与 M-Profile 架构相关的章节中文翻译，按手册原章节顺序排列（Part A 简介与概述在前，Part B 架构规则在后）。

## 1. 章节

### Part A — Armv8-M 架构简介与概述（Armv8-M Architecture Introduction and Overview）

1. [简介（Introduction）](introduction/index.md)

### Part B — Armv8-M 架构规则（Armv8-M Architecture Rules）

2. [复位（Resets）](resets/index.md)
3. [电源管理（Power Management）](power_management/index.md)
4. [程序员模型（Programmers' Model）](programmers_model/index.md)
5. [浮点支持（Floating-point Support）](floating_point_support/index.md)
6. [向量扩展（Vector Extension）](vector_extension/index.md)
7. [指针认证与分支目标识别扩展（Pointer authentication and branch target identification Extension）](pacbti/index.md)
8. [内存模型（Memory Model）](memory_model/index.md)
9. [系统地址映射（The System Address Map）](system_address_map/index.md)
10. [同步与信号量（Synchronization and Semaphores）](synchronization_and_semaphores/index.md)
11. [受保护内存系统架构（The Armv8-M Protected Memory System Architecture）](protected_memory_system_architecture/index.md)
12. [系统定时器，SysTick（The System Timer, SysTick）](system_timer_systick/index.md)
13. [嵌套向量中断控制器（Nested Vectored Interrupt Controller）](nested_vectored_interrupt_controller/index.md)
14. [调试（Debug）](debug/index.md)
15. [调试与跟踪组件（Debug and Trace Components）](debug_and_trace_components/index.md)
16. [性能监视扩展（The Performance Monitors Extension）](performance_monitors_extension/index.md)
17. [可靠性、可用性与可服务性扩展（Reliability, Availability, and Serviceability (RAS) Extension）](ras_extension/index.md)

### Part C — Armv8-M 指令（Armv8-M Instructions）

18. [指令集概览（Instruction Set Overview）](instruction_set_overview/index.md)
19. [T32 指令编码：顶层与 16 位](instruction_encoding_16bit/index.md)
20. [32 位 T32 指令编码](instruction_encoding_32bit/index.md)
21. [指令列表（A–C 段）](instruction_list/index.md)

### Part G — 术语表（Glossary）

22. [术语表（Glossary）](glossary/index.md)

## 2. 相关内容

- [Armv7-M 架构参考手册（DDI0403E E.e）](../armv7-m/index.md) — 上一代 M-Profile 架构参考手册的对应译文。
- 本手册 Part C 的指令集概览（C1）与 T32 指令编码（C2.1–C2.3）已译入；C2.4 按字母顺序的指令列表、Part D 寄存器与有效载荷规范、Part E 伪代码、Part F 调试包协议为参考资料，暂不收录；Part G 术语表已译入本站术语表页。Part B 的 B1–B16 章节清单见 `sync-todo/ARMv8-M.md` 中的队列。
