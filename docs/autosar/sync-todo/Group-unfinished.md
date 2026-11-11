# Sync todo: unfinished rows — open work

Consolidated 2026-11-11 from the former per-batch `Group-<section>.md` queue files. **Resume = the first row still `[ ]` in this file** (todo-format.md). Format and tick rules: `references/todo-format.md` (autosar-translate skill). The status ledger is [`../TODO.md`](../TODO.md).

---

## CP methodology and templates (from Group-cp-methodology.md)

# Sync todo: Group cp-methodology — CP R23-11 methodology and template documents (17 — rows 1–10 delivered by PR #366, 7 remain)

Base: R23-11 (`~/Workspace/autosar_standard/markdown/Classic_Platform/Releases/R23-11/MethodologyAndTemplates/`) · Generated: 2026-11-06 · Queue order = row order (source size ascending)
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit
> Scope (user request 2026-11-06): the 17 non-SWS CP documents of the `MethodologyAndTemplates` folder — 6 RS + 7 TPS + 4 TR — deliberately outside the original CP 148 scope when the queue was bootstrapped 2026-10-24 (index.md recorded only "1 TPS template exempt"; BSWMDT's exempt line lived in [Group-exp.md](Group-exp.md) "Not queued"). This batch closes that gap; the Group-exp exempt line now points here.
> Source path: `Classic_Platform/Releases/R23-11/MethodologyAndTemplates/AUTOSAR_CP_<Type>_<Name>.md` (SKILL.md Step 1 names the Classic Platform tree — this is the same tree, non-SWS folder). No PDFs are bundled under `docs/autosar_pdf/`; the raw PDFs are in the corpus repo `~/Workspace/autosar_standard/Classic_Platform/Releases/R23-11/MethodologyAndTemplates/` (Git LFS) — same garbled-cell recovery route as the Foundation runs.
> Article shape: **all documents are skeleton-exempt** (STANDARD.md §7 — RS/TPS/TR are not module SWS): mirror the source's own chapter numbering, EXP-guide flow (Group-exp / Group-foundation-exp precedent: doc-meta chrome dropped, references chapter kept as an unnumbered `## 参考文献` registry so `[n]` citations link, figures deduplicated by content hash, source tables as GFM).
> Target dir: `cp/methodology_templates/<slug>/` (the section landing and nav subgroup 方法论与模板 exist since the BSWMDT article). Each run adds its article to the section landing `## 文章`, the nav (`方法论与模板` subgroup of the CP tab, label = short name), and runs `check_indexes.py`.
> Slug rule: the Foundation precedent `<type>_<snake_name>` disambiguates the same-named RS/TPS pairs (BSWModuleDescriptionTemplate, DiagnosticExtractTemplate, ECUConfiguration, ECUResourceTemplate, SoftwareComponentTemplate, SystemTemplate). The existing `basic_software_module_description_template` article KEEPS its slug (no rename, no redirect churn). The slug is a proposal: an ambiguous name still goes to the user at Step 1 (mapping.md naming rule). Front-matter `spec:` = `AUTOSAR_CP_<Type>_<Name>`, `release: R23-11`.
> OPEN decision (confirm at the first run's Step 1, Foundation precedent proposed as default): item IDs are DROPPED, titles translate only — the 2026-11-03 Foundation decision (recorded in Group-foundation-rs-prs.md). These CP RS/TPS/TR documents consist of identified items just like their FO counterparts; applying the same rule keeps the corpus consistent, but it is not yet user-confirmed for CP.

## Queue

- [ ] tps_timing_extensions (AUTOSAR_CP_TPS_TimingExtensions · MethodologyAndTemplates · R23-11 markdown · ❌ new article · 📖 skeleton-exempt)
  - Note: Timing Extensions（时序扩展）; target `cp/methodology_templates/tps_timing_extensions/`; template specification (TPS) — meta-model class tables, constraints and ARXML examples (template-type)
  - Note: source `MethodologyAndTemplates/AUTOSAR_CP_TPS_TimingExtensions.md` — 8,752 lines, 384 figure refs, 113 item IDs
  - Note: related site content: none (the Foundation RS_TimingExtensions counterpart is queued in Group-foundation-rs-prs.md — cross-link candidates, report-only until the run decides)
  - Note: Step 1 (2026-11-12): resumed from the preserved partial (参考文献 + §1–§3.2 prose); gap = 表3.7–3.12 caption-only placeholders + src §3.3–§3.4/ch.4/annexes A–G untranslated
  - Note: figure forensics (2026-11-12): prior extraction had 10 logo-contaminated/missing figure files (3.5/3.28/3.41/3.46/3.53/3.54/3.55/3.56/4.19/4.22 — pairs 3.41/3.42 and 3.55/3.56 were cross-assigned) and never extracted the 9 annex figures (B.1–B.7, C.1) + 4 listing renders (C.2/C.3/C.6/C.9 rasterized listings); all 93 figures now extracted, content-verified, margin-padded
  - Note: Step 2 (2026-11-12): full translation ch.1–4 + annexes A–G (6,546 lines); annex C listings mechanically reconstructed (C.13/C.15 hand-formatted; C.19 truncated at source, noted in place); annex D = 65 mentioned class tables, class notes translated, attribute Note cells verbatim English (tr_modeling_show_cases precedent, batch-gate decision pending); annex G change histories per TPS_APSD precedent (titles-only, Number column dropped); annex A.3 tracing omitted per ASWS precedent; item IDs dropped per 2026-11-03 Foundation decision (OPEN CP decision adopted as proposed default — flag at batch gate); [TPS_SYST_01003] inline in §4.3 and [RS_ECUC_00079] inside a verbatim annex-D attribute cell retained per the 2026-11-07 sanctioned-variant rule
  - Note: Step 3 (2026-11-12): strict build exit 0 / 0 WARNING; 4 stale forward anchors fixed to build-derived slugs, all 26 intra-page links resolve; check_indexes OK (375 nav targets, 0 broken); check_heading_lang OK; hygiene 0 × ^# / \< / {DRAFT}; link census: 22 chapter refs (21 pre-linked during translation + 1 applied, idempotent re-run 0 lines), 18/18 citations linked, census UNRESOLVED: B.2.2 annex ref (letter-prefixed number not in the tool's numeric grammar — left prose, user decision); cross-article mentions report-only (PORT ×20, BswM ×1, ComM/Nm no article)
  - Note: Step 5 replaced by the 2026-11-12 batch instruction: user asked for one-by-one commits WITHOUT per-article confirmation and a single combined confirmation gate at the end of the batch — deviations to verify at that gate: item-ID drop adopted for CP, annex-D attribute notes verbatim English, annex D table numbering renumbered sequentially, Response glossary term NOT added (SOME/IP meaning differs — second-definition needs user decision), annex B/C figure gaps recovered from prior partial
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate (batch gate at end of rows 11–17, per user instruction 2026-11-12)
  - [x] Step 6 — TODO.md row + commit/PR (2026-11-12: commit 8f06413 on feature/cp-methodology-rows-11-17, PR at batch end)

- [ ] tps_ecu_configuration (AUTOSAR_CP_TPS_ECUConfiguration · MethodologyAndTemplates · R23-11 markdown · ❌ new article · 📖 skeleton-exempt)
  - Note: ECU Configuration（ECU 配置）; target `cp/methodology_templates/tps_ecu_configuration/`; template specification (TPS) — meta-model class tables, constraints and ARXML examples (template-type)
  - Note: source `MethodologyAndTemplates/AUTOSAR_CP_TPS_ECUConfiguration.md` — 9,579 lines, 408 figure refs, 296 item IDs
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

- [ ] basic_software_module_description_template (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · MethodologyAndTemplates · R23-11 markdown · 🔶 existing article · 📖 skeleton-exempt)
  - Note: BSW Module Description Template（基础软件模块描述模板）; target = the existing `cp/methodology_templates/basic_software_module_description_template/` (row name = the actual article dir so the index resolves it; a type-prefixed slug is NOT adopted — no rename, no redirect churn); template specification (TPS) — meta-model class tables, constraints and ARXML examples
  - Note: source `MethodologyAndTemplates/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md` — 10,999 lines, 480 figure refs, 237 item IDs
  - Note: pre-queue translation (Group-exp.md formerly carried the exempt 📄 line) — this row is an ALIGNMENT pass: verify the article against the R23-11 source and fill any drift; prior exempt note "methodology_templates/basic_software_mode_manager template" carried a name typo
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

- [ ] tr_methodology (AUTOSAR_CP_TR_Methodology · MethodologyAndTemplates · R23-11 markdown · ❌ new article · 📖 skeleton-exempt)
  - Note: Methodology（方法论）; target `cp/methodology_templates/tr_methodology/`; technical report (TR) — informational, no numbered requirement items
  - Note: source `MethodologyAndTemplates/AUTOSAR_CP_TR_Methodology.md` — 13,206 lines, 751 figure refs, 208 item IDs
  - Note: related site content: foundation Methodology articles (rs_methodology etc. in Group-foundation-rs-prs.md — cross-link candidates, report-only until the run decides)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

- [ ] tps_diagnostic_extract_template (AUTOSAR_CP_TPS_DiagnosticExtractTemplate · MethodologyAndTemplates · R23-11 markdown · ❌ new article · 📖 skeleton-exempt)
  - Note: Diagnostic Extract Template（诊断提取模板）; target `cp/methodology_templates/tps_diagnostic_extract_template/`; template specification (TPS) — meta-model class tables, constraints and ARXML examples (template-type)
  - Note: source `MethodologyAndTemplates/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md` — 29,451 lines, 1,150 figure refs, 296 item IDs (giant)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

- [ ] tps_software_component_template (AUTOSAR_CP_TPS_SoftwareComponentTemplate · MethodologyAndTemplates · R23-11 markdown · ❌ new article · 📖 skeleton-exempt)
  - Note: Software Component Template（软件组件模板）; target `cp/methodology_templates/tps_software_component_template/`; template specification (TPS) — meta-model class tables, constraints and ARXML examples (template-type)
  - Note: source `MethodologyAndTemplates/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md` — 39,695 lines, 1,734 figure refs, 1,021 item IDs (giant)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

- [ ] tps_system_template (AUTOSAR_CP_TPS_SystemTemplate · MethodologyAndTemplates · R23-11 markdown · ❌ new article · 📖 skeleton-exempt)
  - Note: System Template（系统模板）; target `cp/methodology_templates/tps_system_template/`; template specification (TPS) — meta-model class tables, constraints and ARXML examples (template-type)
  - Note: source `MethodologyAndTemplates/AUTOSAR_CP_TPS_SystemTemplate.md` — 76,751 lines, 3,024 figure refs, 759 item IDs (giant — largest source in the whole queue)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

> Delivery: rows 1–10 (rs_ecu_resource_template … tr_modeling_show_cases) done 2026-11-10/11 and merged via PR #366 (issue #365, commits 79587d7…d1f2094) — condensed records in [Group-finished.md](Group-finished.md). Resume = row 11 (tps_timing_extensions).

---

## Sync todo: Group foundation exp — Foundation R23-11 guide/template/report documents (20) (from Group-foundation-exp.md)

> In flight: this row is fully worked (Steps 1–6 ticked) — the article is translated and PR #320 (issue #319) is open against master; the row stays `[ ]` until that PR merges (todo-format rule). Resume context: worktree `~/Workspace/melodypapa-gst`, branch `feature/foundation-exp-gst`.

- [ ] tps_generic_structure_template (AUTOSAR_FO_TPS_GenericStructureTemplate · MethodologyAndTemplates · R23-11 markdown · ❌ new article · 📖 skeleton-exempt)
  - Note: Generic Structure Template（通用结构模板）; target `foundation/methodology_templates/tps_generic_structure_template/`; template specification (TPS) — meta-model class tables, constraints and ARXML examples (template-type, cf. BSWMDT exemption)
  - Note: source `MethodologyAndTemplates/AUTOSAR_FO_TPS_GenericStructureTemplate.md` — 15,110 lines, 663 figure refs, 578 item IDs; **giant source** — segment plan before Step 2 (OS/RTE precedent)
  - Note: related site content: cp/template/generic_structure (one-paragraph summary page, deleted 2026-11-04 — this row is the full FO document) (cross-link candidates, report-only until the run decides)
  - Note: Step 1 (2026-11-07): source confirmed `MethodologyAndTemplates/AUTOSAR_FO_TPS_GenericStructureTemplate.md` 15,109 lines / 663 figure refs / 578 item IDs; no article exists → full translation; chapter map: References + ch.1–14 (2 UML usage, 3 top-level structure, 4 general template classes incl. Formula Language/ARMQL, 5 AbstractStructure, 6 patterns, 7 variant handling, 8 splitable, 9 documentation support, 10 build action manifest, 11 roles and rights, 12 life cycle, 13 collections, 14 mapping views) + annexes A Glossary / B Reference Material / C Variation Points / D Splitable in this Template / E Mentioned Class Tables / F Examples / G Change History (G.1–G.16); chrome = doc-meta tables + Disclaimer + Contents; batch decisions carry over from tps_standardization_template (item-ID headings → translated titles, nominal [TPS_GST_*] prose refs retained, {DRAFT} as entities, change-history Number column dropped)
  - Note: Seg 1 (2026-11-07) 参考文献 + ch.1 translated: registry ref-1..24 with anchors (applied form); 2 content figures (1eb882e4 109KB→Figure1-1, 535fa34f 121KB→Figure1-2, hash census: f5f4bf49 ×255 + 31a8ee06 ×34 + 2 singles = deco); ANOMALY for Phase B: source §1.2's example class table for top-level element AUTOSAR is MISSING from the markdown (only deco-size images at that position) — recover from PDF ground truth or annotate at the gate
  - Note: User decision 2026-11-07 (figure margins): converter artifact PNGs are flush — every embedded figure gets border-whitespace measured at review and pad/replaced under ~1% margin (white border ~2% pixel width, min 12px); codified in autosar-translate SKILL.md Step 5. GST Figures 1-1/1-2/2-1/2-2/2-3/2-4 padded 12–17px in place at copy time.
  - Note: Seg 2–4 progress (2026-11-07, branch feature/foundation-exp-gst): ch.1–4.14 translated (~4,700 article lines; src 1–4373/15109 ≈ 29%); figures padded at embed time per the 2026-11-07 margin decision (Figure1-1..4-19 = 21 content diagrams embedded; hash census f5f4bf49 ×255 / 31a8ee06 ×34 / cad1600a ×121 / 8c27c74a ×53 = deco); ANOMALIES for the gate: (a) source §1.2 example class table for element AUTOSAR missing from markdown; (b) §2.4.1 atp.StatusRevisionEnd source text repeats the StatusRevisionBegin wording ('from which on') though it pairs with periodEnd — translated faithfully; (c) source typos [TPS_-STDT_00064]/[TR_-PDN_00003] normalized to [TPS_STDT_00064]/[TR_PDN_00003]; (d) source 'Acccess'/'SpeicalData'/'Adminstrative'/'similiar'/'Defintion' typos preserved where inside table cells, corrected in prose where clearly conversion artifacts; strict build + check_heading_lang PASS per segment; remaining src: ch.5–14 (4374–10883) + annexes A–G (10884–15109)
  - Note: Seg 5–6 progress (2026-11-07/08, worktree ~/Workspace/melodypapa-gst — main checkout moved to a parallel cortex branch, GST continues in the worktree): ch.5–7 fully translated (article 7,687 lines; src 1–7171/15109 ≈ 47%); figures Figure5-1..5-10, 6-1..6-9, 7-1..7-16 embedded padded; ch.7 covered all 4 variation patterns + VariationPoint structure (表7.1–7.28) + EvaluatedVariants + 4 worked examples (清单7.4–7.10); strict build + check_heading_lang PASS per commit; remaining: ch.8–14 (7172–10883) + annexes A–G (10884–15109)
  - Note: Seg 7 progress (2026-11-08): ch.8–14 fully translated (article 11,106 lines; src 1–10883/15109 = 72%); figures 8-1..8-5, 9-1..9-15, 10-1..10-7, 11-1..11-2, 12-1..12-2, 13-1..13-2, 14-1 embedded padded (figures 9.16–9.18 have no content image — their content is the document excerpt text itself); ch.9 complete incl. OasisExchangeTable model, MsrQuery mechanism, LEnum 137 literals (merged 8-column table, literal set identical); ch.10–14 complete (BuildActionManifest, RolesAndRights, LifeCycles, Collections, ViewMaps); strict build + check_heading_lang PASS per commit; remaining: annexes A–G (10884–15109)
  - Note: Seg 8a progress (2026-11-08): annexes A–D translated and committed (A Glossary 29 terms in blockquote format; B Reference Material = conversion stub, page-chrome only → omitted under droppable set with 省略注记 for the gate to verify against the PDF; C = 表C.1 all ~330 variation-point entries; D = 表D.1 all 33 splitable entries); RESUME POINT for Seg 8b: annex E Mentioned Class Tables (src 11622–13183, ~105 tables E.1–E.105, extraction at /tmp/gst_annexE.md — dedupe script in earlier commit history; translate Note prose cells, keep identifiers/Tags verbatim) → F Examples (13184–13784, incl. listings F.1–F.31 + F.5–F.11 ARXML files) → G Change History (13785–15109, G.1–G.16, Number column dropped per batch decision). Then full Phase A/B gate + Step 8.
  - Note: Seg 8b–8d completion (2026-11-08): annexes E–G translated; E = 84 mentioned class tables (E.1–E.84, prose translated, identifiers/Tags verbatim); F = examples F.1–F.3 (listings F.1–F.31 rebuilt as fences); G = change history G.1–G.16 rendered per tps_standardization_template precedent (single-column 标题 tables, heading text verbatim as data, Number column dropped, 56 tables); nav registered (mkdocs.yml MethodologyAndTemplates group), landing page ## 文章 entry added + 待翻译 row removed, foundation overview entry added; final gates: strict build exit 0 / 0 WARNING / 0 INFO for this page (3 XSD-pattern cells wrapped in inline code per sibling precedent), check_indexes OK (322 nav targets, 240 tab pages, 0 broken), check_heading_lang OK, gen_api_list --check up to date, hygiene 0 × ^# / \< (1 {DRAFT} hit was in the provenance HTML comment — reworded), link census: 56/56 citations linked; 11 'unresolved [n]' are ARMQL interval expressions ([1,3] etc., not citations — census false positives), [16] in annex-E table cell left unlinked (tables stay definitional); figure review rule applied at embed time: 101 figures measured, 0 below 12px margin
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate (2026-11-08: user pre-approved continuation 'confirmed and continue until all article is translated'; final evidence presented at PR)
  - [x] Step 6 — TODO.md row + commit/PR (2026-11-08: issue #319 · PR #320 open against master; worktree ~/Workspace/melodypapa-gst, branch feature/foundation-exp-gst)

