# Sync todo: Group safety — safety section (new section)

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit
> This batch must first create the section landing page `docs/autosar/safety/index.md` (STANDARD.md §6 format) and register it in the nav — folded into the first row's Step 2.

## Queue

- [ ] wdgm (SWS_WatchdogManager · R23-11 markdown · ❌ new article, short name WdgM)
  - Note: the first run also creates the `safety/` landing page + nav registration
  - Note: Step 1 done 2026-10-26 — source `Safety/AUTOSAR_CP_SWS_WatchdogManager.md` (R23-11) 3,877 lines, 168 requirement blocks, 35 content diagrams (54 unique hashes / 3 recurring deco strips dropped), ch.10 = 21 containers / 46 parameter tables, ch.2 = 18 acronym rows + 24 term rows. Article = full Type A translation (new) + new `safety/` section landing page + nav
  - Note: source→article chapter map — src 1→§1, 2→§2, 3→§3, 4→§4, 5→§5, **6 (Requirements Tracing) DROPPED**, 7→§6 功能规格, 8→§7 API规范, 9→§8 时序图, 10→§9 配置规范; src annex "Example Implementation of Alive Supervision Algorithm" → appendix (see decision); src "Not applicable requirements" → dropped (the second droppable item)
  - Note: no Known Limitations chapter in the source → no `## 已知限制`; source ch.4.1 `{DRAFT}` markers dropped; source ch.7/8/10 requirement IDs dropped, requirement text kept as paragraphs
  - Note: §2 = 42 rows (18 acronyms + 24 terms) in source order, flat bold-term + blockquote (GPT-driver precedent for a source ch.2 with an acronym table AND a terms table); 6 acronyms already in glossary.md (BSW, DEM, DET, HW, MCU, OS) → 来源 line appended, 36 new entries added
  - Note: §5 = 9 dependent modules promoted to `### 5.1`–`### 5.9` (STANDARD.md §1 "one ### per dependent module"; GPT/OCU/DIO/ICU precedent); source 5.1/5.1.1/5.2 (File Structure / Code File Structure / Version Check) shift to 5.10/5.10.1/5.11
  - Note: src ch.8 API → §7 with source-8.N→article-7.N mapping (8.1→7.1 导入的类型, 8.2→7.2 类型定义 = 1 type WdgM_ConfigType, 8.3→7.3 函数定义 = 10 functions, 8.4→7.4 回调通知 = Not Applicable, 8.5→7.5 调度函数 = WdgM_MainFunction, 8.6→7.6 期望接口 = 强制/可选/可配置, 8.7→7.7 服务接口 incl. the 5 ImplementationDataTypes + ModeDeclarationGroup WdgM_Mode); check_api_sync.py applies (source 8.2.x=1 type, 8.3.x=10 functions)
  - Note: src ch.10 → §9 配置规范 with 9.1 参数区分 (10.1.1–10.1.3) / 9.2 容器与配置参数 (9.2.1–9.2.21) / 9.3 发布信息; ECUC ids dropped per hygiene rule → `| SWS 条目 |  |` cell (ICU/DIO/OCU/PORT/Port precedent)
  - Note: src annex A formulas are lost in the R23-11 markdown (`<!-- formula-not-decoded -->` ×7) → restore the 7 formula bodies from the bundled R22-11 PDF (`docs/autosar_pdf/AUTOSAR_CP/R22-11/Safety/AUTOSAR_SWS_WatchdogManager.pdf` p.162-165); src ch.4.1's mangled condition list nesting restored from the same PDF p.20 (content identical, structure garbled by the converter)
  - Note: **user decisions 2026-10-26** — (a) the source's content annex A (*Example Implementation of Alive Supervision Algorithm*) becomes the numbered continuation `## 10. 存活监督算法示例实现` (not a lettered `## A.`); STANDARD.md §1 amended with the numbered-continuation case in the same PR (precedent: operating_system §10–13). (b) `gen_api_list.py` misclassified `WdgM_Init` as a type — the R23-11 markdown places `## 8.3.1 WdgM_Init` *before* `## 8.3 Function definitions` (PDF-conversion artifact), so the generator's positional scan filed it under 8.2; generator patched to classify by each heading's own number prefix (verified: exactly 1 document changes corpus-wide) — `api_reference.md` now lists WdgM_Init as 函数
  - Note: Step 2 done 2026-10-26 — article `docs/autosar/safety/watchdog_manager/index.md` written (2,680 lines) + `docs/autosar/safety/index.md` landing page + nav registration (安全（Safety）group, after 系统服务)
  - Note: figures — 35 content diagrams copied as `Figure7-1..12`, `Figure8-1..3`, `Figure9-1`, `Figure10-1..17`, `FigureA-1..2`; source ch.1 has **no** content diagram (the PDF list-of-figures starts at *Overview of Watchdog Manager Supervision* = source Figure 7.1) — the three small strips in ch.1 are decoration
  - Note: `| SWS 条目 |` cells filled with the ECUC id (MCU/GPT/CoreTest/EcuM precedent, 2026-10-26 batch) rather than left empty (ICU/DIO/OCU/PORT/PWM/OS) — decided by the most recent site practice; recorded here so the next run is consistent
  - Note: Phase A check 9 census (recorded, not silent) — applied class: 176 identifier-mention lines (functions 159 / error codes 30 / type 1) across §4·§6·§7·§9; `--apply` inserted the intra-article links and the `[n]` citation links (4 citations + 9 registry anchors, applied with the citation-linking rule added by the parallel RTE session) and is idempotent (2nd run = 0 lines); report-only: 0 §7.2 constant bullets, 35 参见/参考/详见 lines, prose `[n]` hop-2 resolutions ([1] IEC 61508 + [2] ISO 26262 EXTERNAL, [3] SWS_BSWGeneral EXTERNAL, [4] EcuM SITE, [8] SWS_MCUDriver EXTERNAL, [9] SWS_RTE EXTERNAL), cross-article module mentions (Mcu ×14 no article, DEM ×6 SITE, Det ×2 no article, EcuM ×1 SITE, BswM ×1 SITE) — the cross-article and hop-2 classes stay unlinked (user decision, queued in TODO.md's Backlog)
  - Note: **2026-10-26 delivery** — committed on `feature/watchdog-manager` (worktree off origin/master 3f59e79; commit **fdbffbb**) → **issue #117**, PR pending. Working-tree note: a parallel session merged its RTE work (PR #116) mid-run and reset `mkdocs.yml`; the safety nav entry was re-applied on top of the merged master before the commit
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate
  - [x] Step 6 — TODO.md row + commit/PR
- [ ] wdgif (SWS_WatchdogInterface · R23-11 markdown · ❌ new article, short name WdgIf)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] wdg (SWS_WatchdogDriver · R23-11 markdown · ❌ new article, short name Wdg)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
