# Sync todo: Group diagnostics — diagnostics section

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [ ] diagnostic_event_manager (SWS_DiagnosticEventManager · R23-11 markdown · ❌ stub — near-full Type A build, source 16,739 ln)
  - Note: 2026-10-28 Step 1 measured — the ⚠️-gaps tag understated the work: the article is a 127-line legacy stub (front matter ✓ spec/release set; §1 intro translated; an unnumbered mislabeled `## 首字母缩略词和缩写` chapter whose body is the source 2.1/2.2 table spilled as loose prose incl. untranslated English; an EMPTY `## 2. 功能规格` skeleton of bare 2.1–2.11 headings; only 2.11.5 NvM interaction has translated paragraphs — legacy wording「首字母缩略词和缩写」violates §2, and TODO.md's Backlog "dem numbering gap" is this stub's broken structure). Source spans: ch.1–5 ≈ 280 ln · ch.7 functional spec 1109–5174 (7.1–7.13, ≈4.1k ln) · ch.8 API 5175–11159 (29 types 8.2.1.x; ~130 functions in 7 groups 8.3.1–8.3.7 incl. grouped sub-interfaces; 8.4 expected; 8.5 scheduled; 8.6 service interfaces — 23 impl data types, 37 C/S interfaces, 38 ports; ≈6k ln) · ch.9 sequence diagrams 13 subsections (~100 ln) · ch.10 配置规范 11262–16673 (10.2.1–10.2.10, ≈5.4k ln — the program's largest) · appendix B. ch.6 traceability DROPPED. ch.4.1 Limitations has real content (36 ln)
  - Note: 2026-10-28 plan (presented, >2000-line rule): Dem split across 4 runs — R-A: §1–§5 rebuild (incl. ch.2 blockquote reflow) + §6 from ch.7.1–7.6 · R-B: §6 continued ch.7.7–7.13 · R-C: §7 API from ch.8 + §8 时序图 (ch.9; figure PNGs by caption number) · R-D: §9 配置规范 from ch.10 + `## B.` appendix + glossary/api_reference/census + full Phase A/B + PR. Each run commits on the same branch; batched confirmation at the end (2026-10-27 pattern). USER CONFIRMED 2026-10-28 (4-run split, start now)
  - [x] Step 1 — Source resolution + gap analysis (findings + split plan above; user confirmation of the split pending before Step 2 starts)
  - Note: R-A DONE 2026-10-28 (commit c5b4a25, branch feature/group-diagnostics-sync) — §1–§5 rebuilt (§2 reflowed: 2.1 首字母缩略词 60 term rows + 2.2 缩写 42 rows, 0 tables; registry [1]–[24]; 4.1 限制 real content; Figure5_1 embedded) + §6.1–§6.6 from ch.7.1–7.6 (Figures 7_1–7_12 by caption number, mapped by size triage — deco set f5f4bf49/cad1600a/31a8ee06/8c27c74a/a133f680 + small recurring bee5fd45/8c27c74a ~8KB icons). Legacy stub's NvM paragraphs preserved in an HTML-comment holding block (source 7.11.5, re-home in R-B at §6.11.5). FINDING: source 7.4.1 "DTC kind" is an EMPTY heading (no body at all) — kept as empty `#### 6.4.1.`, flag for the R-D PDF census. Strict build exit 0 / 0 WARNING / 0 dem anchor notices. R-B scope: ch.7.7–7.13 (source 1769–5174, ~3.4k ln → §6.7–§6.13) + re-home the NvM block
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] j1939dcm (SWS_SAEJ1939DiagnosticCommunicationManager · R23-11 markdown · ❌ new article)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] diagnostic_communication_manager (SWS_DiagnosticCommunicationManager · R23-11 markdown · ⚠️ 24k-line source, giant — last)
  - Note: currently only the introduction + acronyms; present a chapter-by-chapter plan first per SKILL.md Step 3 (suggest splitting the 7-chapter skeleton across several runs)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
