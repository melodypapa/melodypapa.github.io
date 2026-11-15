---
title: "Armv8-M 架构参考手册"
---

本专题收录《Armv8-M Architecture Reference Manual》(DDI0553B B.y) 的章节中文翻译，按手册原章节顺序排列（Part A 简介与概述、Part B 架构规则、Part C 指令，其后为 Part D–F 参考资料与 Part G 术语表）。

## 1. 章节

### Part A — Armv8-M 架构简介与概述（Armv8-M Architecture Introduction and Overview）

1. [简介（Introduction）](part-a/introduction/index.md)

### Part B — Armv8-M 架构规则（Armv8-M Architecture Rules）

2. [复位（Resets）](part-b/resets/index.md)
3. [电源管理（Power Management）](part-b/power_management/index.md)
4. [程序员模型（Programmers' Model）](part-b/programmers_model/index.md)
5. [浮点支持（Floating-point Support）](part-b/floating_point_support/index.md)
6. [向量扩展（Vector Extension）](part-b/vector_extension/index.md)
7. [指针认证与分支目标识别扩展（Pointer authentication and branch target identification Extension）](part-b/pacbti/index.md)
8. [内存模型（Memory Model）](part-b/memory_model/index.md)
9. [系统地址映射（The System Address Map）](part-b/system_address_map/index.md)
10. [同步与信号量（Synchronization and Semaphores）](part-b/synchronization_and_semaphores/index.md)
11. [受保护内存系统架构（The Armv8-M Protected Memory System Architecture）](part-b/protected_memory_system_architecture/index.md)
12. [系统定时器，SysTick（The System Timer, SysTick）](part-b/system_timer_systick/index.md)
13. [嵌套向量中断控制器（Nested Vectored Interrupt Controller）](part-b/nested_vectored_interrupt_controller/index.md)
14. [调试（Debug）](part-b/debug/index.md)
15. [调试与跟踪组件（Debug and Trace Components）](part-b/debug_and_trace_components/index.md)
16. [性能监视扩展（The Performance Monitors Extension）](part-b/performance_monitors_extension/index.md)
17. [可靠性、可用性与可服务性扩展（Reliability, Availability, and Serviceability (RAS) Extension）](part-b/ras_extension/index.md)

### Part C — Armv8-M 指令（Armv8-M Instructions）

18. [指令集概览（Instruction Set Overview）](part-c/instruction_set_overview/index.md)
19. [指令规范（Instruction Specification）](part-c/instruction_specification/index.md)

### Part D — Armv8-M 寄存器与有效载荷规范（Armv8-M Registers and Payload Specification）

20. [寄存器与有效载荷规范（Register and Payload Specification）](part-d/registers_and_payload_specification/index.md)

### Part E — Armv8-M 伪代码（Armv8-M Pseudocode）

21. [Arm 伪代码定义（Arm Pseudocode Definition）](part-e/arm_pseudocode_definition/index.md)
22. [伪代码规范（Pseudocode Specification）](part-e/pseudocode_specification/index.md)

### Part F — 调试包协议（Debug Packet Protocols）

23. [ITM 与 DWT 包协议规范（ITM and DWT Packet Protocol Specification）](part-f/itm_and_dwt_packet_protocol/index.md)

### Part G — 术语表（Glossary）

24. [术语表（Glossary）](part-g/glossary/index.md)

## 2. 相关内容

- [Armv7-M 架构参考手册（DDI0403E E.e）](../armv7-m/index.md) — 上一代 M-Profile 架构参考手册的对应译文。
- 本手册 Part C 的指令集概览（C1）已译入，指令规范（C2）已译入 C2.1–C2.3；Part D 寄存器与有效载荷规范、Part E 伪代码、Part F 调试包协议为参考资料，目录与章节标题页已建、译文待后续同步；Part G 术语表已译入本站术语表页。各章进度见 `sync-todo/ARMv8-M.md` 中的队列。
