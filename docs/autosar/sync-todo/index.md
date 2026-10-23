# AUTOSAR 翻译总队列 — 索引

> 生成：2026-10-24 · 基准：R23-11（`~/Workspace/autosar_standard/markdown/`）
> 模式：仿 py-armodel `sync-autosar-class` 的 Group 队列 — 每批次一个 `Group-<section>.md`，
> 一行一篇文档，行内 6 步子清单；**恢复 = 所选批次文件里第一个仍为 `[ ]` 的行**；
> 全部行 `[x]` = 该批次完成。格式与勾选规则：`references/todo-format.md`（autosar-translate 技能）。
> 状态台账（每篇文章是什么）在 [`../TODO.md`](../TODO.md)；本目录是执行队列（接下来做什么）。

## 批次顺序（建议）

| 序 | 批次文件 | 行数 | 内容 |
| --- | --- | ---: | --- |
| 1 | [Group-io.md](Group-io.md) | 7 | IO 分区收尾（1 已完成 + 对齐/缩略语转换 + iohwab 补齐 + adc 深补） |
| 2 | [Group-general.md](Group-general.md) | 4 | platform_types 空壳修复 + BSWGeneral（全局基础规范）等 3 篇缺失 |
| 3 | [Group-crypto.md](Group-crypto.md) | 4 | crypto_driver 补 API + Csm 对齐 + CryIf/KeyM |
| 4 | [Group-system_services.md](Group-system_services.md) | 7 | Det（小）+ ComM + OS 补 API（源 1.2 万行）+ FiM/time_service 对齐 |
| 5 | [Group-mode_management.md](Group-mode_management.md) | 2 | EcuM 对齐 + BswM 对齐（小） |
| 6 | [Group-diagnostics.md](Group-diagnostics.md) | 3 | Dem 补齐 + J1939Dcm + Dcm（源 2.4 万行，巨型殿后） |
| 7 | [Group-memory.md](Group-memory.md) | 12 | MemIf/Fee 补齐 + 空壳 + 4 篇对齐 + Ea/Eep 等 6 篇缺失 |
| 8 | [Group-communication.md](Group-communication.md) | 27 | 现有 18 篇补齐/对齐 + 通信主干 9 篇（Com/CanSM/CanTp/TcpIp/Nm/EthSM/IpduM/SomeIp×2） |
| 9 | [Group-mcal.md](Group-mcal.md) | 3 | Mcu、Gpt、CoreTest |
| 10 | [Group-globaltime.md](Group-globaltime.md) | 4 | StbM + CanTSyn/EthTSyn/FrTSyn |
| 11 | [Group-libraries.md](Group-libraries.md) | 9 | Crc、E2E 库等 9 篇 |
| 12 | [Group-safety.md](Group-safety.md) | 3 | WdgM/WdgIf/Wdg |
| 13 | [Group-security.md](Group-security.md) | 2 | Firewall、IdsM |
| 14 | [Group-rte-swarch.md](Group-rte-swarch.md) | 2 | RTE、ARTI |
| 15 | [Group-communication-2.md](Group-communication-2.md) | 38 | 通信其余缺失（CAN XL/LdCom/Dlt/DoIp/XCP/Spi/FlexRay 系/J1939 系/V2X 系…） |
| 16 | [Group-exp.md](Group-exp.md) | 21 | 20 篇缺失 EXP 指南 + TPS 模板（豁免骨架，流程同） |

合计 148 篇 = R23-11 全部 **127 篇 SWS**（io 7 + general 4 + crypto 4 + system_services 7 + mode_management 2 + diagnostics 3 + memory 12 + communication 65 + globaltime 4 + libraries 9 + mcal 3 + rte-swarch 2 + safety 3 + security 2，其中 1 篇已完成）+ **20 篇缺失 EXP** + 1 篇 TPS 模板（豁免不入队，见 Group-exp Not queued）。批次间顺序可按需调整；批内行序 = 建议执行序（小工作量/对齐在前，巨型源殿后）。

## 规则

- **一次一篇**：每次运行取一个行，走完 6 步（含用户确认门），翻转行 + 子清单，记录 commit hash，然后停（autosar-translate SKILL.md Step 6/7）。
- **已 `[x]` 行不重开**，除非用户新基准/漂移复审（`- Note: 重开 <原因>` 后置 `[ ]`）。
- 批内已对齐文章若带未修缺口，缺口写在行 Note 里 — Step 1 只需核实，不重推倒。
- 每批完成 → 更新本索引计数与 [`../TODO.md`](../TODO.md) 概览。
