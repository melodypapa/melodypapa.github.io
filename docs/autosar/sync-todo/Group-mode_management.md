# Sync todo: Group mode_management — mode management section

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [ ] basic_software_mode_manager (SWS_BSWModeManager · R23-11 markdown · ✅ alignment + 时序图)
  - Note: 4.2 "适用于汽车领域" → "汽车域的适用性"; 7.3 "周期函数" → "调度函数"
  - Note: QUEUE FIX 2026-10-24: this row's Steps 5/6 were found pre-marked [x] with ecu_state_manager's commit hash and PR #70 before any BswM work existed — reset to the real state (the dio lesson: the queue must not lie)
  - Note: 2026-10-24 Step 1 (issue #71, worktree run): source 6409 lines — the biggest yet. ch.2 10:10 ✓ (term-line verbatim nit: SWC / SW-C); ch.9 时序图 small (2 subsections, 2 figures); ch.10 配置规范 = 91 containers across ~3600 lines (10.2.1–10.2.90) — too large for this run, DEFERRED to its own follow-up run (TODO.md 待办 + row note)
  - [x] Step 1 — Source resolution + gap analysis (issue #71)
  - [x] Step 2 — In-place translation/completion (4.2 + 7.3 renamed; SWC / SW-C term line verbatim; new ## 8. 时序图 with Figure9-1/9-2.png checksum-verified against source artifacts)
  - [x] Step 3 — Phase A mechanical checks (strict build 0 WARNING; headings ## 1-8; stale-variant sweep 0; no requirement IDs/external links; glossary regenerated --check 0; api --check 0)
  - [x] Step 4 — Phase B coverage map + fidelity (source ch.1-8 ↔ §1-§7 pre-existing ✅ untouched; ch.9 → §8 fully; ch.10 deliberately deferred (91 containers) — recorded as the row's open scope; appendices omitted)
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [x] ecu_state_manager (SWS_ECUStateManager · R23-11 markdown · 🔶 alignment · commit 37ee564 · PR #70)
  - Note: ch.2 "定义和缩写" → "缩略语"; 4.2 "适用于汽车领域" → "汽车域的适用性"
  - Note: 2026-10-24 Step 1 (issue #69, worktree run): source 5866 lines (ModeManagement/, not SystemServices/); gaps = ch.2 (11 defs + 12 abbrevs), 4.2 wording, new ## 8. 时序图 (ch.9, ~200 lines, 16 figures) + ## 9. 配置规范 (ch.10, 1267 lines, ~17 containers / ~40 params); full scope user-confirmed at the Step 1 gate
  - Note: figure forensics — 40 distinct ch.9 images, 24 are page decorations (~8KB) vs 16 diagrams (>100KB); exactly 16 captions → 1:1 mapping, size filter + visual spot-check (Fig 9.5 embedded caption); 12 of 8.1's figures already in the article as Figure7-*.png
  - [x] Step 1 — Source resolution + gap analysis (issue #69)
  - [x] Step 2 — In-place translation/completion (ch.2 flattened 23 entries + 12 abbreviation fixes; §4.2 renamed; ## 8. 时序图 with 16 Figure9-*.png; ## 9. 配置规范 with ~40 param tables; internal refs renumbered, -- placeholders kept, broken "Figure 38" ref kept faithful — flagged)
  - [x] Step 3 — Phase A mechanical checks (strict build 0 WARNING after figure fix; headings ## 1-9; ch.2 23:23; no requirement IDs/external links; glossary regenerated --check 0; api --check 0)
  - [x] Step 4 — Phase B coverage map + fidelity (source ch.1-8 ↔ §1-§7 pre-existing; ch.9 → §8 section by section; ch.10 → §9 with two source-numbering anomalies normalized — 10.2.4 held two containers, EcuMShutdownCause/EcuMSetClockAllowedUsers had no numbers → 9.2.4-9.2.9 sequential; appendices omitted; NA-requirements spillover omitted)
  - Note: 2026-10-25 completion run (user: "ch.2 structure mirrors the source; only ch.6 Requirements Tracing + appendix A are droppable; every other section translates"): ch.2 → `## 2. 定义和缩略语` (2.1 定义 11 + 2.2 缩略语 12, blockquote format kept); new `## 已知限制` (source Known Limitations, unnumbered before §1); §3.1 → 输入文件和相关标准与规范; §7 completed — 7.1 导入的类型 + 7.2 类型定义 (source 8.1/8.2, 6 types), 7.7 期望接口 (8.7), 7.8 端口接口规范 (8.8.1–8.8.7); existing 7.1–7.4 renumbered 7.3–7.6 (inbound link #73-callout函数 → #75 updated); 调度表函数 → 调度函数; appendix B → `## B. AUTOSAR 可追溯项变更历史` (item-ID fences verbatim). Figure re-check: the 16 ch.9 figures were already complete — the prior run's forensics (40 refs = 24 deco ~8KB + 16 diagrams >100KB, 16 captions 1:1) is authoritative; this run's hash-based "5 missing" reclassification was wrong and its decoration insertions were reverted.
  - Note: 2026-10-25 link-analysis improvement (user: "help me improve the link analysis for EcuM"): (a) link_candidates.py — function/type defs now collected from identifier-titled headings at ANY level under §7.2–7.5 (the old #### -only rule matched EcuM's Chinese group titles 通用/状态管理/闹钟 as "functions" — 86 noise links — and missed the real ###### -level functions); error-code class generalized from the `6.6.` prefix to any 错误-titled §6 section (registers EcuM 6.12/6.13 ECUM_E_* and ADC's ADC_E_* at 6.5, which the old rule never saw); (b) article: §7.5 callout h6 headings renumbered 7.3.x.y → 7.5.x.y (stale from the 7.1–7.4→7.3–7.6 shift; source says 8.5.x.y; no inbound links anywhere); (c) --apply on EcuM: 107 lines linked (types + functions + callbacks + callouts + ECUM_E_* codes), all anchors resolve, idempotent (0 lines on re-run); regression censuses: DIO unchanged, PWM +1 / OCU +3 / ICU +9 / ADC +26 lines — all genuine X_E_Y error codes newly registered (census only; --apply not run on those articles, queued as Backlog); strict build 0 WARNING.
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- 📖 guide_to_mode_management — EXP_ModeManagementGuide (skeleton-exempt; a retranslation/update needs its own run)
