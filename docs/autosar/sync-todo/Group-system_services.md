# Sync todo: Group system_services — system services section

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [ ] det (SWS_DefaultErrorTracer · R23-11 markdown · ❌ new article, small — do first)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] function_inhibition_manager (SWS_FunctionInhibitionManager · R23-11 markdown · 🔶 alignment)
  - Note: legacy heading "功能规范" → "功能规格"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] time_service (SWS_TimeService · R23-11 markdown · 🔶 alignment)
  - Note: delete the forbidden "配置规范" chapter; legacy ch.2 heading → "缩略语"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] comm (SWS_COMManager · R23-11 markdown · ❌ new article, short name ComM)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] swcluc (SWS_SoftwareClusterConnection · R23-11 markdown · ❌ new article, short name SwCluC)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] hwtestmanager (SWS_HWTestManager · R23-11 markdown · ❌ new article)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [x] operating_system (SWS_OS · R23-11 markdown · ⚠️ missing API chapter, 12k-line source — last)
  - Note: missing "API 规范" chapter; source is large, present the plan before translating per SKILL.md Step 3
  - Note: Step 1 gap analysis (2026-10-26, source `SystemServices/AUTOSAR_CP_SWS_OS.md` 12,476 lines vs article 816): article ends mid-§6.7.2 (source 7.7.2.1 background truncated mid-list). Aligned already: §1–§6.7.1 (source ch.1–7.7.1), ch.2 acronym rows 29/29. Missing: `### 2.1.` 术语表 (source 2.1 Glossary of Terms — table garbled by page-break dupes, true row set ≈44 terms needs reconstruction); §6.7.2 tail (source 7.7.2.2/7.7.2.3 + rest of 7.7.2.1); §6.7.3–6.17 (source 7.7.3–7.17); §7 API规范 entire (source ch.8: 8.1 常量, 8.2 宏, 8.3 类型定义 22 types, 8.4 函数定义 39 entries, 8.5 IOC, 8.6 期望接口, 8.7 hook functions, 8.8 服务接口); §8 时序图 (source ch.9, 9 diagrams); §9 配置规范 (source ch.10: 10.2 Os* 35 containers + 10.3 IOC 5 + 10.4 ARTI 20 + 10.5 published info); §10–13 (source ch.11 生成, 12 应用说明, 13 AUTOSAR 服务, 14 展望); appendix B (source B, R22-11→R23-11 diffs). No Known Limitations chapter in source. Scale: ≈10,200 source lines to translate — article grows 816→~8–9k lines; multi-stage agent plan (RTE segment pattern).
  - Note: alignment fixes queued in this run: §3.1 heading 「输入文件及相关标准和规范」→「输入文件和相关标准与规范」(canonical, TODO Backlog row); §4.7 「适用于汽车领域」→「汽车域的适用性」(forbidden variant); front-matter `spec: AUTOSAR_CP_SWS_OperatingSystem`→`AUTOSAR_CP_SWS_OS` (api_reference.md shows all SWS_OS entries 未翻译 because of this mismatch); delete `![Table7_1](Table7_1.png)` image ref — GFM table already present below it (tables rule; TODO Backlog row).
  - Note: figure inventory (content hashes after deco-dedupe, 4 deco hashes recur 177/50/49/29×): ch.7 39 (11 placed as Figure7_1–7_12 sans 7_8, ~28 to extract for 7.8–7.17), ch.8 14 (triage content vs table chrome), ch.9 9 (→Figure9_*), ch.10 23 (triage — config-table cells, likely chrome), ch.11–14 3. 4-component headings follow site majority `######` (435 vs 95).
  - Note: check_api_sync.py likely N/A for OS (source types are 8.3, functions 8.4 — script assumes source 8.2/8.3 → article 7.2/7.3); equivalent count/name/order check scripted manually in Phase A.
  - Note: run progress 2026-10-26 checkpoint 2 (article 3,237 lines, strict build clean): §6.9.14–6.9.30 stitched (seg3; Figure7_18–7_22); §6.10 IOC stitched (seg4; Figure7_23–25; ~345×38 strips dropped as chrome); §6.11–6.17 stitched (seg5; Figure7_26–30; tables 7.4/7.5 + 7.15 error table + 7.17.4 71-row service-call table PDF-verified); §3.1 REALIGNED to R23-11's 11-entry list (legacy had extra [7] SRS_FreeRunningTimer shifting [7]–[12]; [3] doc id fixed to AUTOSAR_FO_TR_Glossary; source's own stale citations kept as printed — body cites [12] ch.13.1 @2276, [7] hooks @6642 despite 3.1 ending at [11]); §6.2 legacy "参见文档[7] (SWFRT)" removed (not in R23-11 source); §7.1–7.3 written MANUALLY (22 type entries, EcuM folded-prose format; CoreIdType truncated description recovered from PDF "shall represent the logical CoreID"); §7.4.1–7.4.16 written MANUALLY (16 function entries, 说明-fold + C fences + per-requirement paragraphs). STASHED for later append: /tmp/os-stage5.md (§8 时序图, 56 lines, Figure9_1–9_8 copied), /tmp/os-stage7.md (§10–13 + B, 379 lines, Figure11_1 copied; B.1.6=无 from PDF). §7.4.17–7.4.39 written MANUALLY (23 entries; multi-name entries Read/Write/ModifyPeripheral8/16/32 as single sections with all signatures in one fence; isOsStarted DRAFT marker dropped, content translated). §7 API规范 39/39 function entries + 22 types complete. Provider concurrency cap intermittent — 5+ rejections total, serialize/manual fallback. §7.5–7.8 written MANUALLY (IOC API 6 function groups with 通用/参数/返回值/内部结构 bold lead-ins, ReceiverPullCB, ProtectionHook + 3 app-specific hooks, Os_Service port/CSI tables as GFM; §8 时序图 stash appended — article 4,039 lines, strict build clean, §7 API规范 COMPLETE 39 functions+22 types). cfg-1/2/3 STITCHED (§9.1 + §9.2.1–9.2.35 complete, 650+548+604 lines, Figure10_1–10_14 placed; agents PDF-verified config-class cells `Pre-compile time：X（All Variants）…` with uppercase X per this PDF, reconstructed OsTimeValue garbled table, OsTaskPeriod truncated description; cfg-2 correctly started at source 7966 where OsEvent actually begins). Article 5,838 lines. REMAINING: cfg-2 (7996–8692 → 9.2.14–9.2.22), cfg-3 (8693–9503 → 9.2.23–9.2.35), cfg-4 (9504–10340 → 9.3 IOC + 9.4.1–9.4.2), cfg-5 (10064–11236 → 9.4.3–9.4.14, may split), cfg-6 (11237–12136 → 9.4.15–9.4.20 + 9.5 发布信息) → append /tmp/os-stage7.md → Phase A/B + glossary + api_reference regen + Step 8 gate.
  - Note: user decisions 2026-10-26 (all confirmed): (a) 完整范围启动 multi-session sync; (b) source ch.11–14 → article §10–13 direct continuation — STANDARD.md §1 extended in the same PR; (c) appendix B title = direct translation 「B. 约束和规格项的历史」 — STANDARD.md B-entry wording generalized to "direct translation of the source appendix title" in the same PR; (d) `### 2.1. 术语表` (Glossary of Terms, direct translation, matches site glossary page title).
  - [x] Step 1 — Source resolution + gap analysis
    - Note: FINAL ASSEMBLY 2026-10-26: cfg-4 (396 lines agent, Figure10_15) + cfg-5 (827 lines MANUAL — quota limit replaced concurrency cap; 9.4.3–9.4.13, 4 XML examples reconstructed) + cfg-6 (633 lines MANUAL; 9.4.14–9.4.20 + 9.5 发布信息; ArtiOsTaskInstanceEcucRef source self-typo translated faithfully with inline note) + stage7 (§10–13 + B) all stitched. ARTICLE COMPLETE: 8,074 lines, §1–§13 + B, 55 figures. Phase A: build 0 WARNING; heading skeleton canonical; §2 forbidden-variant sweep 0; h1/DRAFT 0; acronym+glossary term lines 75 == 29+46 source rows exactly; figure refs all resolve; inbound-anchor check clean; check_api_sync N/A (noted earlier); gen_api_list regenerated + --check pass (57 OS entries now SITE-linked); link_candidates --list recorded (451 applied-class mentions, 0 constant bullets, 55 参见, 24 [n] citations: glossary×2 SITE rest EXTERNAL=user decisions; cross-article PORT/DEM/BswM SITE, Mcu/Det NO-ARTICLE) then --apply 305 lines + idempotency 0 + build clean. REMAINING: glossary.md OS-term extension (46 terms — BLOCKED by parallel session actively editing glossary.md; do at commit time or follow-up) + Step 5 gate + Step 6 commit (stage ONLY operating_system/, Group-system_services.md, TODO.md — NOT the parallel session's mcal/api_reference/glossary/RTE files).
- [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
