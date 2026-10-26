# RTE run plan — SWS_RTE (Step 1 output)

> Queue row: `Group-rte-swarch.md` → `rte`. Base release R23-11.
> Source: `~/Workspace/autosar_standard/markdown/Classic_Platform/Releases/R23-11/RTE/AUTOSAR_CP_SWS_RTE.md`
> (verified: 43,058 lines · 9.4 MB · 1,642 image references → 227 distinct content diagrams + 9 page-decoration hashes).
> Generated: 2026-10-25 · Step 1 complete. Decisions D1–D5 taken by the user on 2026-10-25 (recorded below).

## 0. Decisions applied

| # | Decision | Answer |
| --- | --- | --- |
| D1 | Section directory | **`docs/autosar/rte/`** — the article is `docs/autosar/rte/index.md`, registered directly in the nav (no section landing page, `power/` style). The ARTI row will add its own directory (`docs/autosar/arti/index.md`) or a shared landing page when it runs. |
| D2 | Article structure | **Type A 7-chapter skeleton per `STANDARD.md`** — no new exemption. Source chapters are remapped and renumbered like every other article (§1–§8 mapping below). |
| D3 | Page split | **Single page** — `docs/autosar/rte/index.md`, ≈ 28,000 lines. |
| D4 | Appendices D + E | **In scope** (source D *Referenced Meta Classes*, source E *Referenced ECUC Configuration Parameters* translate fully). |
| D5 | This run | **Plan only** — the plan is recorded here and in the queue row; translation starts in the next run. |

## 1. Source inventory

| Source unit | Lines | Prose | Table | Images | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| front `References` [1]–[35] | 55 | 55 | 0 | 1 | 35 entries; [21] ASAM MCD-2 MC is a plain-text URL |
| `Note on XML examples` | 4 | 4 | 0 | 0 | short notice → §1 |
| `1 Introduction` | 778 | 101 | 399 | 71 | 1.3 缩略语 has **no table** (points to the AUTOSAR glossary); 1.4 Technical Terms = **97 rows** (the earlier count included the header row); 1.5 Document Conventions; 1.6 Requirements Tracing = droppable |
| `2 RTE Overview` | 144 | 70 | 0 | 6 | 2.1–2.4 → §1 |
| `3 RTE Generation Process` | 517 | 250 | 0 | 27 | 3.1–3.7 → §6.1 |
| `4 RTE Functional Specification` | 9,140 | 4,008 | 743 | 427 | 4.1–4.10 → §6.2, core chapter |
| `5 RTE Reference` | 8,723 | 4,231 | 413 | 281 | 5.1–5.11 → §7.1: 5.5 API data types, **5.6 = 43 API functions**, 5.7 runnable entity reference, 5.8 lifecycle, 5.9 call-backs, 5.10 expected interfaces, 5.11 VFB tracing |
| `6 BSW Scheduler Reference` | 1,963 | 943 | 70 | 58 | 6.1–6.7 → §7.2, 6.5 = **14 SchM API functions** |
| `7 RTE Implementation Plug-Ins Reference` | 4,627 | 1,950 | 647 | 185 | 7.1–7.3 → §6.3 |
| `8 RTE ECU Configuration` | 4,233 | 427 | 2,733 | 193 | 8.1–8.17 → §8, table-dominated |
| `A Metamodel Restrictions` | 340 | 170 | 0 | 14 | A.1–A.22 → §4.1 |
| `B External Requirements` | 6 | 2 | 0 | 1 | → appendix A |
| `C MISRA C Compliance` | 75 | 13 | 36 | 2 | → appendix B |
| `D Referenced Meta Classes` | 5,141 | 486 | 3,386 | 183 | → appendix C |
| `E Referenced ECUC Configuration Parameters` | 4,034 | 130 | 3,277 | 98 | → appendix D |
| `F Examples` | 1,289 | 616 | 54 | 28 | → appendix E |
| `G Change history` | 1,015 | 300 | 327 | 38 | → appendix F (`可追溯项变更历史`) |

Totals: **2,716 distinct `SWS_Rte_*` items**, 290 `Section x.y` + 62 `Chapter n` cross-references,
227 content diagrams, 0 existing articles.
Volume estimate at the site ratio (EcuM: 5,867 → 3,843 lines, 0.66): **≈ 28,000 article lines**.

## 2. Chapter mapping (Type A)

| Article | Source | Renumber |
| --- | --- | --- |
| `## 1. 简介和功能概述` | 1 intro + 1.1 Scope + 1.5 Document Conventions + 2 RTE Overview (2.1–2.4) | 1.1→1.1, 1.5→1.2, 2.x→1.3–1.6 |
| `## 2. 定义和缩略语` | `### 2.1. 定义` ← 1.4 (98 rows, order verbatim); `### 2.2. 缩略语` ← 1.3 (0 rows, glossary pointer) | — |
| `## 3. 相关文档` | `### 3.1. 输入文件和相关标准与规范` ← References [1]–[35]; `### 3.2. 相关规范` ← [21] ASAM MCD-2 MC, [29] MISRA C | — |
| `## 4. 约束和假设` | `### 4.1. 限制` ← appendix A (A.1–A.22 → 4.1.1–4.1.22); `### 4.2. 汽车域的适用性` ← source has none → one sentence saying so | A.x→4.1.x |
| `## 5. 对其他模块的依赖` | 1.2 Dependency to other AUTOSAR specifications | 1.2→5 |
| `## 6. 功能规格` | `### 6.1. RTE 生成过程` ← 3; `### 6.2. RTE 功能规格` ← 4; `### 6.3. RTE 实现插件` ← 7 | 4.x→6.2.x, 7.x→6.3.x; ch.3: the two **unnumbered** role sections become 6.1.1/6.1.2, so 3.1–3.7 → 6.1.3–6.1.9 (i.e. 3.x → 6.1.(x+2)) |
| `## 7. API规范` | `### 7.1. RTE 参考` ← 5; `### 7.2. 基础软件调度器参考` ← 6 | 5.x→7.1.x, 6.x→7.2.x |
| `## 8. 配置规范` | 8 RTE ECU Configuration (no 时序图 chapter in the source → 配置规范 takes 8) | unchanged |
| `## A. 外部需求` | source B | — |
| `## B. MISRA C 合规性` | source C | — |
| `## C. 引用的元类` | source D | — |
| `## D. 引用的 ECUC 配置参数` | source E | — |
| `## E. 示例` | source F | — |
| `## F. AUTOSAR 可追溯项变更历史` | source G (item-ID lists verbatim in code fences, "none" → 无) | — |

Dropped: 1.6 Requirements Tracing only (the mandated droppable set; RTE has no *Not applicable requirements* appendix).

### Consequences of the Type A mapping (recorded, not silently accepted)

1. **Heading depth.** Article level = numeric depth + 1, Markdown stops at `h6`. After remapping,
   source headings at depth ≥ 4 exceed the limit: **583 headings** (ch.4 238, ch.5 198, ch.6 19,
   ch.7 128) render as bold numbered lead-in lines (`**4.2.2.6.1.1 场景 1**`) under their `h6` parent.
   Source-faithful numbering would have cost only the 43 depth-6 headings — accepted trade-off for
   skeleton compliance.
2. **Cross-references.** 352 explicit `Section x.y` / `Chapter n` references are renumbered with the
   mapping table above and, where the target heading exists, turned into same-page anchor links.
   (Existing articles — e.g. EcuM — left source numbers in prose and now carry stale references;
   RTE fixes them mechanically instead.)
3. **Appendix letters shift** (source B–G → A–F) because appendix A is absorbed into §4. The change
   history lands on `## F.`, so Phase A check 2's "`## B.` only for change history" is adapted for
   this article (letters A–F are all content appendices here).

## 3. Site placement and nav

```yaml
- "RTE（运行时环境）": autosar/rte/index.md
```

placed in `CP AUTOSAR` after 系统服务, before 模板. Front matter:

```yaml
title: "AUTOSAR RTE（运行时环境）"
spec: AUTOSAR_CP_SWS_RTE
release: R23-11
```

## 4. Translation stages (single page, appended in article order)

| Stage | Content | Source lines | Est. article lines |
| --- | --- | ---: | ---: |
| S1 | front matter + nav + §1 (source 1/1.1/1.5 + ch.2) + §2 (97 terms) + §3 + §4 (← appendix A) + §5 | ~1,400 | ~900 |
| S2 | §6.1 RTE 生成过程 (source ch.3) | 517 | ~460 |
| S3–S7 | §6.2 RTE 功能规格 (source 4.1–4.2 / 4.3 / 4.4–4.6 / 4.7–4.8 / 4.9–4.10) | 9,140 | ~6,000 |
| S8–S9 | §6.3 RTE 实现插件 (source 7.1–7.2 / 7.3) | 4,627 | ~3,000 |
| S10–S11 | §7.1 RTE 参考 (source 5.1–5.5 / 5.6–5.11) | 8,723 | ~5,700 |
| S12 | §7.2 基础软件调度器参考 (source 6) | 1,963 | ~1,300 |
| S13–S14 | §8 配置规范 (source 8.1–8.9 / 8.10–8.17) | 4,233 | ~2,800 |
| S15 | appendix A, B, E, F (source B, C, F, G) | ~2,400 | ~1,600 |
| S16–S17 | appendix C, D (source D, E — tables) | 9,175 | ~4,500 |

≈ 17 sessions, one commit per stage on the article branch; the queue row stays `[ ]` until the last
stage, Phase A/B gates run per stage, the full gate (skill Step 7) runs at the end.

### 4.1 Progress log

| Stage | State | Notes |
| --- | --- | --- |
| S1 | **done** (2026-10-25) | `docs/autosar/rte/index.md` = 883 lines: front matter, §1 (source 1 + 1.1 + 1.5 + ch.2), §2 (97 terms + the acronyms pointer sentence), §3 (35 references), §4 (appendix A → 4.1.1–4.1.22, 4.2), §5 (source 1.2). Nav: `运行时环境 → RTE` under *CP AUTOSAR*, between 系统服务 and 模板. Strict build: exit 0, 0 WARNING. |
| S2 | **done** (2026-10-25) | §6 + §6.1 = 457 lines (source ch.3): 6.1.1/6.1.2 role sections, 6.1.3 contract (RTE + BSW scheduler), 6.1.4 PreBuild contract, 6.1.5 ECU config editing, 6.1.6 generation (BSW scheduler / RTE / cluster / BSWMD 6.1.6.4.1–3 / Com+LdCom users 6.1.6.5.1–2), 6.1.7 PreBuild, 6.1.8 PostBuild, 6.1.9 interaction with other BSW modules. 4 figures copied as `Figure3-1..4.png`. Strict build: exit 0, 0 WARNING. |
| S3 | **partial** (2026-10-25) | §6.2 架构概念 done: `#### 6.2.1.` complete (6.2.1.1–6.2.1.8, all h7+ depths folded to bold lead-ins), 8 figures `Figure4-1..8.png`. Progress inside S3: 6.2.2 + 6.2.2.1 done (source 4.2/4.2.1 incl. memory-mapping wrapping + task chains, Figures 4-9/4-10). Progress inside S3: 6.2.2.2 OS done (source 4.2.2 complete: OS objects, BswSchedulableEntity, runnable categories, RTE/Bsw events incl. tables 4.1/4.2, mapping scenarios 1–9 + figs 4.11–4.16, execution-time monitoring + figs/examples, TimingEvent sync, BackgroundEvent, InitEvent, OsTaskExecutionEvent). Progress inside S3: 6.2.2.3 (activation/start state machine + tables 4.3/4.4, figs 4.18–4.22, immediate restart, activation offset figs 4.23/4.24 + tables 4.5/4.6, activating-event feature) and 6.2.2.4 (cyclic execution + examples) done. Progress inside S3: 6.2.2.5 interrupt decoupling & notifications done (source 4.2.5 complete incl. the inline ECUC definitions RteEventToTaskMapping + 17 parameters and RteEventToIsrMapping + 5 parameters, normalized to one table per parameter; 3x duplicated PDF columns collapsed). **§6.2 COMPLETE** (2026-10-25): 6.2.2.6 data consistency, 6.2.2.7 multiple trigger, 6.2.2.8 parameter/data-element implementation (tables 4.7–4.9), 6.2.2.9 measurement & calibration (complete incl. 4.2.9.3 pointered/initRAM methods and 4.2.9.4 McSupportData export), 6.2.2.10 NVRAM access (dirty-flag strategies, NvM interfaces). Figures 4-25..4-39 added (15 PNG). Article now 4,768 lines. Progress in §6.3: 6.3.1 intro + 6.3.2.1 file structure + 6.3.2.2 API principles + 6.3.2.3 API data types done (source 7.1–7.2.3, figs 7-1/7-2). Progress in 6.3.2.4: implicit value/address access, FillFlushRoutine, explicit access protection (Start/StopRead/Write) done (source 7.2.4.1–7.2.4.4). Progress in 6.3.2.4: 7.2.4.5 explicit data access (Read/Write/DRead incl. return-value priority rules) done. Remaining: 7.2.4.6–7.2.4.15 (23443–25043) + 7.3 (25044–26924). Note: parallel subagent translation was attempted for the rest but hit the API usage limit — remaining chapters continue manually, one run each. |
| S3 (cont.) | **§6.3 progress** (2026-10-25) | **6.3.2.4.6–6.3.2.4.10 done** (source 7.2.4.6–7.2.4.10, src 23443–23915): 6.3.2.4.6 互斥区域保护 (Rte_Rips_Enter 0xE8 / Exit 0xE9 incl. the 4-case provision bullets), 6.3.2.4.7 模式队列保护 (EnterModeQueue 0xF4 / ExitModeQueue 0xF5), 6.3.2.4.8 跨软件集群模式通信 (Rte_Rips_SwitchNotificationStatusType value table + Switch 0xB0 + DequeueModeSwitch 0xB1), 6.3.2.4.9 DSMQ 调度同步 (Rte_DsmqStatusType + DsmqSwitch 0xF6 / DsmqTransitionStart 0xF7 / DsmqTransitionSync 0xF8 / DsmqTransitionEnd 0xF9), 6.3.2.4.10 服务器函数调用 (Invoke 0xEC with 8 return-value error codes / ReturnResult 0xED with 9 / InvocationHandler 0xEE). Article 5,900 lines. Strict build: exit 0, 0 WARNING. **Remaining in §6.3: source 7.2.4.11–7.2.4.15 (src 23915–25043: 13 Notify* transformer-signal entries incl. code examples, Trigger, Feedback/DataIsUpdated, Prm, lifecycle SchM_Init/Rte_Start/Rte_Stop/SchM_Deinit) + 7.3 (25044–26924). Next run. |
| S3 (cont.) | **§6.3 progress** (2026-10-25, parallel subagents) | **6.3.2.4.11–6.3.2.4.15 done** (source 7.2.4.11–7.2.4.15, src 23915–25043) — translated by 5 parallel subagents (segments A–E, stitched in order; the boundary entry 7.2.4.11.13 was deliberately covered by two segments and deduped): 6.3.2.4.11 变换器的信号通知 (13 Notify* entries 0xFA/0xFB/0xFC/0xFD/0xFE + 05303/05307/05312 families + TP copy/start-of-reception entries, incl. reconstructed C examples and N:1 C/S notes), 6.3.2.4.12 跨软件集群触发器通信 (Trigger), 6.3.2.4.13 数据和事件通知 (Feedback, DataIsUpdated, DataIsUpdated_EventActivation), 6.3.2.4.14 外部参数访问 (Prm), 6.3.2.4.15 RTE 实现插件生命周期 API (SchM_Init/Rte_Start/Rte_Stop/SchM_Deinit). **22 bold lead-in entries + 5 group headings = source count exactly.** Article 6,806 lines; strict build exit 0 / 0 WARNING; hygiene clean (no h1, no ID markers). **Remaining in §6.3: source 7.3 RTE Implementation Plug-Ins Functional Specification (src 25044–26924) → article 6.3.3. Next run. |
| S3 (cont.) | **§6.3 COMPLETE — S8 done** (2026-10-25, parallel subagents) | **6.3.3 RTE 实现插件功能规格 done** (source 7.3, src 25044–26924) — 5 parallel segment agents (A–E), stitched in order; heading-level fix applied to C (source 7.3.4.5–.9 → h6; deeper lead-ins stay bold). Coverage: 6.3.3.1 原子软件组件类型的特化, .2 与 VFB 跟踪的交互 (例7.3), .3 验证策略 (.1–.4), .4 数据通信 (.4.1–.4.9 incl. 状态/转换 requirement blocks, 表7.1/7.2/7.3 normalized, examples 7.4–7.13 as clean C fences), .5 互斥区域 (examples 7.14–7.17), .6 模式 (.6.1–.6.6.5), .7 参数, .8 兼容模式, .9 客户端-服务器通信, .10 触发器通信, .11 转换器, **.12 测量/.13 分区间通信/.14 旁路支持/.15 RTEEvent 和 BswEvent 的激活 — the segment-E agent found 7.3.12–7.3.15 beyond the plan's heading survey (source flattens all levels to ##) and translated them to the true end of ch.7**. Article 9,178 lines; strict build exit 0 / 0 WARNING; hygiene clean. **OPEN follow-up: §6.3.3 source figures (ch.7, 185 refs) not yet copied as Figure7-*.png — agents kept 图 7.x captions as plain text; audit + copy in a later pass (decoration-hash forensics as before). S8 complete → next stage S9 was merged into S8's completion; next = S10 (§7.1 RTE 参考, source ch.5). |****
| S10–S11 | **§7.1 COMPLETE** (2026-10-25, parallel subagents) | source ch.5 (src 11618–20334) → article §7.1 via 7 segment agents (A, B, C, D1, D2, E, F) stitched in order with clean boundary handoffs (5.6.22 covered by D2 after D1's range ended at 16856): 7.1.1 范围, 7.1.2 API 原则 (.1–.9), 7.1.3 RTE 模块 (.1–.10), 7.1.4 RTE 数据结构, 7.1.5 API 数据类型 (18-entry Std_ReturnType error tree), 7.1.6 API 参考 (**43 function entries = source 5.6.1–5.6.43 exact**), 7.1.7 可运行实体参考 (16 trigger events), 7.1.8 生命周期 API, 7.1.9 回调参考 (COM 7 + LdCom 8 + NVM 4), 7.1.10 期望接口 (表5.6–5.9), 7.1.11 VFB 跟踪参考. Heading fix: 7.1.2.7–.9 h5→h6. Article 16,771 lines; strict build 0 WARNING. Next = S12 §7.2 (source ch.6, src 20335–22297). |
| S12 (partial) | **§7.2 progress** (2026-10-25) | **7.2.1–7.2.3 done** (source 6.1–6.3): 7.2.1 范围, 7.2.2 API 原则 (.1 命名空间 incl. SchM_ 前缀/vi/ai 规则, .2 BSW 调度器名称前缀与节名称前缀 incl. 例6.1 ICC2 cluster C fence, .3 API 选项), 7.2.3 基础软件调度器模块 (.1 模块互链类型头文件 incl. 文件名/作用域/文件内容/模式, .2 模块互链头文件 incl. 入口点原型/BSW 调度器-BSW 模块接口/激活 Bsw 事件/SwcBswRunnableMapping/条件值宏, XML+C fences reconstructed). **Done MANUALLY — the model-concurrency cap blocked subagent dispatch all turn (5 attempts + 6min waits).** Article 17,054 lines; strict build exit 0 / 0 WARNING. Remaining in §7.2: source 6.4 (API 数据类型: SCHM_E_* 错误码树 + 基础软件模式 + 枚举/范围/位域类型, src 20704–21123) + 6.5 (14 SchM 函数) + 6.6 (BswModuleEntity 参考) + 6.7 (生命周期 API ×5), src 20704–22297. Next run. |
| S12 (cont.) | **§7.2 progress** (2026-10-25) | **7.2.4.1–7.2.4.2 done manually** (source 6.4.1–6.4.2): SCHM_E_* 错误码树 (表6.1 GFM + 7 per-code vertical tables incl. notes on value identity with RTE counterparts), 基础软件模式 (RTE_TRANSITION_*/RTE_MODE_* #ifndef defines reconstructed as C fences for both ALPHABETIC_ORDER and EXPLICIT_ORDER). Agent pool STILL capped (6th dispatch rejected). Article 17,202 lines; strict build exit 0 / 0 WARNING. Remaining in §7.2: source 6.4.3–6.4.5 (枚举/范围/位域类型, src 20934–21123) + 6.5 (14 SchM 函数, 21124–21915) + 6.6 (BswModuleEntity, 21960–22081) + 6.7 (生命周期 ×5, 22082–22297). Next run. |

Adaptations taken while writing S1 (deliberate, because the article renumbers everything):

- The source §1.1 "This document is structured as follows / the appendix consists of five parts" paragraph is
  written against the **article's** chapters and appendices (6.2 / 7.1 / 4.1; appendices A–F, six parts). The
  source's own text is stale there (it says "five parts" and then describes only A–C).
- Cross-references resolved at translation time: source 4.1.3 → 6.2.1.3, 4.2.2.3 → 6.2.2.3, 4.3 → 6.2.3,
  4.3.1.5 → 6.2.3.1.5, 4.3.1.14/15 → 6.2.3.1.14/15, 4.4.1 → 6.2.4.1, 4.4.2 → 6.2.4.2, 4.4.4 → 6.2.4.4,
  5.5.3 → 7.1.5.3, 5.7.5 → 7.1.7.5, 5.7.5.6 → 7.1.7.5.6, 6.4.2 → 7.2.4.2, ch.3 → 6.1, ch.5 → 7.1.
  Written as plain section numbers (no anchors yet); anchors can be added once the target headings exist.
- §1.2 文档约定 keeps the notation description in placeholder form (`[SRS_Rte_<n>]`, `[SWS_Rte_<nnnnn>]`,
  `[SWS_Rte_CONSTR_<XXXXX>]`); the source's concrete example ID is not reproduced (hygiene rule).
- §2.2 缩略语 carries only the source sentence (source 1.3 has no table) — no invented acronym list.
- §4.2 汽车域的适用性: one sentence stating that the document has no separate statement.

## 4.2 Loop execution map (2026-10-25, user: "refine plan and use the loop and subagent to translate all the page")

Remaining work = 11 segments (L1–L11), dispatched 2–3 per round (concurrency-cap aware), stitched strictly in order, gated (strict build) after each round. Source boundaries verified 2026-10-25:

| Seg | Source lines | Content | Article target |
| --- | --- |---|---|
| L1 | 20934–21123 | 6.4.3–6.4.5 (enum/range/bitfield types) | 7.2.4.3–7.2.4.5 |
| L2 | 21124–22297 | 6.5 (14 SchM functions) + 6.6 + 6.7 (lifecycle ×5) | 7.2.5–7.2.7 |
| L3 | 26925–29283 | ch.8 intro + 8.1–8.9 | `## 8. 配置规范` + 8.1–8.9 |
| L4 | 29284–31157 | 8.10–8.17 | 8.10–8.17 |
| L5 | 31498–31578 | appendix B (External Reqs) + C (MISRA) | `## A. 外部需求` + `## B. MISRA C 合规性` |
| L6 | 31579–34150 | appendix D part 1 | `## C. 引用的元类` (part 1) |
| L7 | 34151–36719 | appendix D part 2 | ## C. (part 2) |
| L8 | 36720–38736 | appendix E part 1 | `## D. 引用的 ECUC 配置参数` (part 1) |
| L9 | 38737–40753 | appendix E part 2 | ## D. (part 2) |
| L10 | 40754–42042 | appendix F (Examples) | `## E. 示例` |
| L11 | 42043–43058 | appendix G (Change history) | `## F. AUTOSAR 可追溯项变更历史` |

Rules per segment agent: source-range-only reads; the established format contract (vertical 2-col tables, bold lead-ins at depth ≥4, ID markers dropped, figures skipped, C fences reconstructed); appendix item-ID lists verbatim in code fences (G); config tables normalized (merged cells collapsed, parameter names verbatim). **Loop progress (2026-10-26):** L1 ✅ L2 ✅ (S12 complete: 14 SchM functions + 7.2.6 + 7.2.7; seam gap src 21303–21336 SchM_Result opening filled manually) L3 ✅ (98KB, 114 param tables) L4 ✅ (71KB) L5 ✅ (A 外部需求 + B MISRA 9 tables) L6 ✅ (C.1–C.161) L7 ✅ (C.162–C.312) L8 ✅ (D.1–D.3.1, 23 entries; ends mid-table at EcucDefaultBswPartition 类型 row) — **37,756/43,058 source lines = 87.7%**, article 30,116 lines, strict build 0 WARNING after every stitch. L9 ⬜ (must start with the EcucDefaultBswPartition table completion from src 38737) L10 ⬜ L11 ⬜ — 4,322 lines remain. Agent pool recovered on 2026-10-26 (sequential dispatch only; 3-parallel hits user-concurrency; one `exceed quota limit` on L9's first attempt).

**LOOP COMPLETE (2026-10-26):** L9 ✅ (D.3.1 completion → D.6.1, 14 leaf entries, mid-table seam handled) L10 ✅ (`## E. 示例`, E.1–E.5, 7 code listings) L11 ✅ (`## F. AUTOSAR 可追溯项变更历史`, 15 releases R4.0.2→R23-11, 4,365 source IDs ↔ 4,369 article IDs — 0 missing, +4 = hyphen-artifact repairs; constraint/renaming tables kept as 表 F.1–F.11). **ALL 11 SEGMENTS DONE — the article is fully translated: 34,329 lines, 13 `##` chapters/appendices (已知限制? no — §1–§8 + A–F), strict build exit 0 / 0 WARNING, hygiene clean (0 h1, 0 ID markers; 34 `[SWS_Rte_*]` inside verbatim C-comment code listings in §7.1 are code content, sanctioned).** Source coverage: 42,078/43,058 lines = 97.7% (the remaining 980 = TOC chrome + ch.1.6 Requirements Tracing, dropped by design). **NEXT RUN = finishing pass:** figure audit (ch.4/5/6/7 figure refs are caption-only — size/hash forensics → copy PNGs as Figure<N>-<k>.png), full Phase A (heading audit with the A–F appendix adaptation, §2 97-term count, link_candidates census, hygiene) + Phase B (coverage map per source unit, cell-by-cell checks), glossary.md +97 RTE terms, gen_api_list regen (RTE known-limitation: generator reads ch.8 = ECU config here), then the Step 5 confirmation gate → Step 6 commit/PR.

Stitch order L1→L11. After L11: figure-audit pass + full Phase A/B gates + glossary/api_reference + Step 5 gate (unchanged).

## 5. Special content rules

- **Requirement blocks (2,716 items)**: ID markers dropped (site hygiene); requirement prose and its
  Description/Rationale/Dependencies tables translated in place; look-alike duplicates kept separate.
- **API chapter** = source ch.5/ch.6, not ch.8 → `check_api_sync.py` (hardwired to source 8.2/8.3) is
  **N/A**; replaced by an ad-hoc check: source 5.6.1–5.6.43 ↔ function entries (count/name/order),
  5.5 API data types, 5.9 call-backs, 5.10 expected interfaces, 6.5.x (14).
- **Terms**: 97 definitions as bold-term + `>` blockquote, row set/order verbatim; §2.2 keeps the
  source's "all abbreviations are in the AUTOSAR glossary [11]" sentence with 0 rows.
- **Nested lists (formatting)**: continuation paragraphs and bullets inside a numbered item need a
   **blank line before them and 4 spaces of indentation**; without the blank line Python-Markdown absorbs
   the following `2.` into the previous paragraph (found and fixed in §4.1 while writing S1).
- **Figures**: 315 content references → 227 distinct PNGs (dedupe by content hash), copied into
  `docs/autosar/rte/` as `Figure<source-chapter>-<k>.png`; the 9 decoration hashes dropped.
- **Config chapter (source 8)**: generation-parameter tables translated faithfully as GFM tables;
  PDF merged-cell artifacts collapsed; `[SWS_*]`/`[ECUC_*]` IDs dropped, parameter names verbatim.
- **Appendices**: source D/E tables translated with `Class`/`Attribute`/`Type` cells verbatim;
  source G item-ID lists verbatim in code fences; "none" → 无.
- **Derived indexes**: RTE terms (97) added to `glossary.md` by hand **at the final stage** (Step 6), not per stage; `api_reference.md` regenerated after
  the front-matter `spec:`/`release:` lands. Note: `gen_api_list.py` reads source **chapter 8** (here
  ECU Configuration, not the API) → RTE's API extraction will be empty/wrong; record as a known
  limitation of the generator, not an article defect.

## 6. Gate plan (Phase A adaptations for this article)

1. `mkdocs build --strict` — zero WARNINGs (per stage).
2. Heading audit — Type A skeleton per mapping §2; exception: appendix letters A–F (see §2.3);
   §2 `不用` variant sweep as usual.
3. Hygiene — no `^# ` in body, no requirement IDs, no `{DRAFT}`.
4. Nav registration + anchor/link checks (single page → anchors only).
5. §2 term-line count = 97 (source 1.4) with row order checked line by line; `^| ` count 0 in the slice.
6. `gen_api_list.py --check`; glossary spot-check.
7. API sync — script N/A (see §5), ad-hoc count check instead.
8. Link audit — 1 plain-text URL (ASAM), rest internal anchors.
9. Potential-links census — `link_candidates.py --list`, record counts (RTE identifiers: 43 `Rte_*`
   functions, 14 `SchM_*`, dev-error codes, cross-article module mentions).

Phase B at the end: coverage map per source unit, cell-by-cell term/types/functions checks, fidelity
against the SWS (never the SRS), decisions reflected, links census.
