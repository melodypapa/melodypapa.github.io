# AUTOSAR Article Structure Standard (Type A)

> Scope: **module articles** under `docs/autosar/` (Chinese translations of AUTOSAR specification documents).
> Not applicable to: section landing pages (see below), guide/EXP-type articles, and directories outside `docs/autosar/` (`nxp/`, `eb_tresos/`, etc.).
> This file takes no part in the site build (see `exclude_docs` in `mkdocs.yml`); it exists for writing and review reference only.
> Decision record: established by the site author on 2026-10-23; conversion history in PR #51 (issue #50). 2026-10-24: source chapter *Scheduled functions* named 「调度函数」 (previously listed 「周期函数」) and *Applicability to car domains* named 「汽车域的适用性」 (previously listed 「适用于汽车领域」); see issue #52. 2026-10-24: source chapter *Configurable Interfaces* named 「可配置接口」 (previously listed 「可配置的接口」; all 5 IO articles on the site use the former); see issue #54. 2026-10-24: the 配置规范 ban lifted (user decision) — the source's ch.10 *Configuration specification* translates as the optional article chapter `## 8. 配置规范` when present; see the config-spec rules in the autosar-translate skill (Step 5). 2026-10-24: sequence diagrams allowed (user decision) — the source's ch.9 *Sequence diagrams* translates as the optional article chapter `## 8. 时序图` when present, and 配置规范 shifts to `## 9.` when both are present. 2026-10-25: chapter headings are direct translations of their source headings — §3.1 renamed 「输入文件」→「输入文件和相关标准与规范」 (*Input documents & related standards and norms* translated in full, never shortened; site-wide realignment queued in TODO.md). 2026-10-25 (EcuM completion): the droppable set is exactly two — requirement tracing and appendix A; everything else translates (Known Limitations → unnumbered 已知限制, appendix B with verbatim item-ID fences, port-interface chapters, all content diagrams); ch.2 mirrors the source's Definitions/Abbreviations split. 2026-10-25 (EcuM StartPreOS request): source tables translate as markdown GFM tables — the tables-as-images convention (`Table*.png`) is retired; see §4. 2026-10-26: numbered continuation chapters (§10+) added to §1 — a source chapter 11+ or a content annex that is not the droppable NA-requirements appendix continues the article numbering instead of taking a letter (user decision, watchdog_manager annex A → `## 10. 存活监督算法示例实现`); the lettered form stays reserved for the droppable appendix and appendix B. 2026-10-28 (placeholder sections, KeyM precedent, generalized to every section class on the user's instruction): a source section whose **entire content is a placeholder** (`None.` / `N.A.`) is omitted from the article entirely — no heading with a lone 无/不适用 body; see the placeholder exception in §1.

## 1. Chapter skeleton (mandatory)

Every module article must contain the following seven core top-level chapters — numbering continuous, heading wording matching precisely — plus the optional chapters 8–9 when the source document has them:

| # | Chapter | Content |
| --- | --- | --- |
| 1 | `## 1. 简介和功能概述` | Module overview (translation of the SWS Functional Overview) |
| 2 | `## 2. 缩略语` *(or `## 2. 定义和缩略语` when the source ch.2 is *Definitions and Abbreviations*)* | Bold term + blockquote definition (no GFM table; the source table is reflowed too); subsections mirror the source ch.2 (`### 2.1. 定义` / `### 2.2. 缩略语` when the source has Definitions); row set and row order identical to the source tables |
| 3 | `## 3. 相关文档` | `### 3.1. 输入文件和相关标准与规范` (`[n]` + file-name list), `### 3.2. 相关规范` |
| 4 | `## 4. 约束和假设` | `### 4.1. 限制`, `### 4.2. 汽车域的适用性` |
| 5 | `## 5. 对其他模块的依赖` | One `###` per dependent module |
| 6 | `## 6. 功能规格` | Functional specification body, `###`/`####` sub-sections |
| 7 | `## 7. API规范` | See section 3 below |
| 8 | `## 8. 时序图` *(optional)* | Translation of the source ch.9 *Sequence diagrams* — present iff the source document has it **with actual content** (an `N/A.`-only chapter is omitted — §1 placeholder exception; a surviving following chapter takes the lower number); source 9.x renumbered to 8.x; figures per the site figure convention (local PNG, or a mermaid `sequenceDiagram` redraw per icu_driver when no PNG exists) |
| 9 | `## 9. 配置规范` *(optional)* | Translation of the source ch.10 *Configuration specification* — present iff the source document has it **with actual content** (an `N/A.`-only chapter is omitted — §1 placeholder exception; a surviving chapter takes the lower number); source 10.x renumbered to 8.x when no 时序图 chapter is present, else 9.x; see the skill's config-spec rules |
| 10+ | `## 10. <源章节标题>` *(optional)* | **Numbered continuation** for source content that follows ch.10 — a source chapter 11+ or a content annex that is *not* the droppable *Not applicable requirements* appendix. Numbering continues directly after §9 (no letter); the heading is a direct translation of the source's own title. Precedent: operating_system (§10–13, source ch.11–14) and watchdog_manager (§10, source annex A) |

**Droppable content — the complete list (user decision 2026-10-25, EcuM completion)**: requirement traceability (需求可追溯性 / 需求追踪) and appendix A (*Not applicable requirements*). **Placeholder exception (user decision 2026-10-28)**: a source section whose **entire content is a placeholder** — `None.`, `N/A.` — carries no information and is omitted from the article entirely: no heading, no lone 无/不适用 body. This covers pre-chapters (*Known Limitations* `None.` — KeyM precedent), the optional 时序图/配置规范 chapters whose source is `N/A.`, and placeholder sub-sections inside a chapter that has other real content; dropping an optional chapter may force a renumber of the following one (grep inbound anchors in the same commit). Every omission applied under this exception is **reported** in the queue row note and PR text, and the user reminded to verify it (Step 8 gate) — an omission is never silent. The mandatory `## 7. API规范` chapter is never dropped — when the source API chapter carries no content, keep the chapter with a one-sentence statement (§3). A 无 **value** inside a section with other real content (appendix B release lists, table cells, one-sentence no-callback statements) still translates. **Every other source section translates**, including: pre-chapters such as *Known Limitations* (→ unnumbered `## 已知限制` before §1, when it has actual content), appendix B (*Change history of AUTOSAR traceable items* → `## B. AUTOSAR 可追溯项变更历史`, added/changed/deleted item-ID lists kept verbatim in code fences — the one sanctioned place requirement IDs remain, as data; "none" → 无), expected/port-interface chapters, and every content diagram of a translated chapter (deduplicated by content hash; the converter's repeated page-decoration images are dropped).

**Numbered continuation vs. lettered appendix**: a source annex that carries *content* (not the droppable NA-requirements list) continues the article's numbering (`## 10.`, `## 11.`, …) rather than taking a letter — this keeps the numbering audit (§1: chapters 1.–7. plus the optional 8–9 plus continuation 10+) unambiguous. The lettered form (`## A.`, `## B.`) is reserved for the two cases the standard names explicitly: the droppable NA-requirements appendix (never translated) and appendix B (*Change history of AUTOSAR traceable items* → `## B. AUTOSAR 可追溯项变更历史`). Precedent for the lettered form outside appendix B: rte (§A.–§E., its own source's lettered annexes).

## 2. Chapter heading wording (canonical)

One source chapter uses exactly one rendering site-wide:

- ✅ `简介和功能概述` (not 介绍 / 概述 / 介绍和功能概述)
- ✅ `缩略语` (not 术语 / 缩写词和术语 / 首字母缩略词和缩写 / 定义和缩写); when the source ch.2 is *Definitions and Abbreviations*: `定义和缩略语` → `定义` / `缩略语` (EcuM precedent, 2026-10-25)
- ✅ `相关文档` → `输入文件和相关标准与规范` / `相关规范` (not `输入文件` — the source heading *Input documents & related standards and norms* is translated in full / not 相关的文档)
- ✅ `约束和假设` → `限制` / `汽车域的适用性` (not 适用于汽车领域 / 适用车型域 / 对汽车域的适用性)
- ✅ `对其他模块的依赖`
- ✅ `功能规格` (not 功能规范 / 功能说明)
- ✅ `API规范` → `函数定义` / `调度函数` (not 周期函数 / Scheduled 函数) / `回调通知` / `可配置接口` (not 可配置的接口) / `期望接口`
- ✅ `配置规范` (Configuration specification — the optional chapter after 时序图 when present; source 10.x → 9.x, else 8.x)
- ✅ `时序图` (Sequence diagrams — the optional ch.8 title; source 9.x → 8.x)

## 3. API chapter internal structure

- Per function: `#### 7.1.x. <function name>` + `**说明**: …` + a ```C signature code block
- If the source API or scheduled-function table defines `Service ID [hex]`, retain the exact ID value in that entry's `**说明**` as `服务 ID 0xNN`; this API metadata is not a source requirement ID.
- Grouped as in the source document: `### 7.1. 函数定义`, `### 7.2. 调度函数`, `### 7.3. 回调通知`, etc. (write a group only if the source has it)
- When there are no callbacks, state it in one sentence such as `**BswM**中没有回调通知。` — never omit the chapter. This sentence is content (the source states it in prose), not a `None.` placeholder — the §1 placeholder exception does not apply to it. When the source's whole API chapter is `N/A.` (types-only documents), keep `## 7. API规范` with a one-sentence 不适用 statement — the skeleton chapter itself is never dropped

## 4. Formatting rules

- **The front-matter `title` is the page's only h1 source** — `# ` level-1 headings are forbidden in the body (they break the Material TOC)
- Heading numbering `## N. <标题>` (digit + trailing dot); heading level = numeric depth + 2 (`x.y` → `###`, `x.y.z` → `####`, and so on)
- Bold English terms (`**BswM**`); code identifiers stay untranslated (`Sd_ClientServiceSetState()`)
- Angle-bracket placeholders in identifiers/prose (`EcuM_SlaveCore<X>_Task`, `Csm_<Service>()`, `IoHwAb_Init<Init_Id>`) render via HTML entities `&lt;…&gt;` (decision 2026-10-27 — the corpus's earlier `\<…\>` form shows a stray `\` in rendered HTML: python-markdown consumes `\>` but not `\<`; a bare `<X>` is worse — browsers drop it as an unknown tag). Never inside code fences/inline code, where backslashes and entities stay literal; in headings this changes the Material slug — sweep inbound anchors in the same commit
- No source requirement IDs (`[SWS_Adc_00122]` and the like); `{DRAFT}` markers are dropped
- Notes/tips use `**注意：**` / `**提示：**` paragraphs; **source tables translate as GFM tables, never as images** (decision 2026-10-25 — the tables-as-images convention `Table7-*.png` is retired; caption line above the table keeps the source numbering, e.g. `表7.1：StartPreOS 序列（**StartPreOS Sequence**）`; row set/order/cell values strictly match the source; cell cross-refs link to the article's own anchors; footnote markers carry over as `<sup>N</sup>` + `> N …` blockquotes; see the skill's table rule); other images are local PNGs inside the article directory
- WeChat QR-code footer (where an article has one): `<section id="wechat">` + `<h4>` + image, **never** a Markdown heading (it would pollute the TOC)
- Links resolve before commit: internal `…md` / `#…` targets verified in the build (a missing same-page anchor surfaces only as INFO — check the build output explicitly); external URLs curl-checked (2xx/3xx pass; a 4xx from a known anti-bot host is verified manually in a browser, never auto-removed); links come only from the source document or the site itself — no invented references

## 5. Translation principles

- Articles are **faithful translations** of the standard documents (SWS/EXP): no restructuring, no turning them into your own survey
- Before judging a translation right or wrong, check the **SWS** (the structural source) under `~/Workspace/autosar_standard/markdown/Classic_Platform/Releases/<release>/`; the SRS and the SWS wording can genuinely differ
- Missing content is translated in place from the standard's original text, inserted at the position the source document has it, following the existing format; chapter numbering stays stable

## 6. Section landing pages (index pages)

Each section's `index.md` (e.g. `docs/autosar/io/index.md`) does not follow the skeleton above; it uses a fixed format: front-matter title + one intro paragraph + a `## 文章` link list + `## 相关内容` cross-links; register it in `mkdocs.yml` as the first unlabeled entry under its section (`navigation.indexes`).

## 7. Exemption list

The following articles are guide/topic-type and **do not** follow the module skeleton (intentional — do not "fix" them):

- `foundation/general/tr_glossary` (Foundation TR reference — glossary structure: 简介/缩略语/如何阅读本文档/术语定义; ch.4 terms are `### 4.x. <Term>` + definition tables)
- `mode_management/guide_to_mode_management` (EXP guide structure)
- `memory/nv_data_handling_guideline` (guide structure)
- `power` (topic article, custom 11 chapters)
- `methodology_templates/basic_software_module_description_template`, `template/` (template/methodology type)
- `docs/autosar/glossary.md` (glossary — **manually extended during translation runs**: when an article or TR batch is translated, its terms are added here by the run with 来源 attribution; **one term is translated once** — repeat appearances in other documents append a 来源 line, not a second definition; never script-extracted from translations — user decisions 2026-10-24. **Entry format (2026-10-30)**: `**Term**` + `> 释义` + `>` separator + `> 来源：[Doc](path)（SPEC）、…` + `{: .glossary-source}` — the separator line is mandatory (without it the definition and the attribution merge into one paragraph), the release is stated once in the page intro rather than per line, and the `.glossary-source` class demotes the attribution visually; `scripts/rewrite_glossary.py` normalizes format, alphabetical order and duplicate handling)
- `docs/autosar/api_reference.md` (API list — generated by `.agents/skills/autosar-translate/scripts/gen_api_list.py` from chapter 8 of the R23-11 source documents; never hand-edit; regenerate after front-matter `spec:`/`release:` changes)
