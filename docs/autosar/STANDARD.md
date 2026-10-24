# AUTOSAR Article Structure Standard (Type A)

> Scope: **module articles** under `docs/autosar/` (Chinese translations of AUTOSAR specification documents).
> Not applicable to: section landing pages (see below), guide/EXP-type articles, and directories outside `docs/autosar/` (`nxp/`, `eb_tresos/`, etc.).
> This file takes no part in the site build (see `exclude_docs` in `mkdocs.yml`); it exists for writing and review reference only.
> Decision record: established by the site author on 2026-10-23; conversion history in PR #51 (issue #50). 2026-10-24: source chapter *Scheduled functions* named 「调度函数」 (previously listed 「周期函数」) and *Applicability to car domains* named 「汽车域的适用性」 (previously listed 「适用于汽车领域」); see issue #52. 2026-10-24: source chapter *Configurable Interfaces* named 「可配置接口」 (previously listed 「可配置的接口」; all 5 IO articles on the site use the former); see issue #54.

## 1. Chapter skeleton (mandatory)

Every module article must contain exactly the following seven top-level chapters — numbering continuous, heading wording matching precisely:

| # | Chapter | Content |
| --- | --- | --- |
| 1 | `## 1. 简介和功能概述` | Module overview (translation of the SWS Functional Overview) |
| 2 | `## 2. 缩略语` | Bold term + blockquote definition (no GFM table; the source table is reflowed too); row set and row order identical to the source table |
| 3 | `## 3. 相关文档` | `### 3.1. 输入文件` (`[n]` + file-name list), `### 3.2. 相关规范` |
| 4 | `## 4. 约束和假设` | `### 4.1. 限制`, `### 4.2. 汽车域的适用性` |
| 5 | `## 5. 对其他模块的依赖` | One `###` per dependent module |
| 6 | `## 6. 功能规格` | Functional specification body, `###`/`####` sub-sections |
| 7 | `## 7. API规范` | See section 3 below |

**Forbidden chapters**: requirement traceability (需求可追溯性 / 需求追踪), sequence diagrams (时序图), configuration specification (配置规范), letter-numbered appendices (`## A.` / `## B.`), and any chapter 8 or later content.

## 2. Chapter heading wording (canonical)

One source chapter uses exactly one rendering site-wide:

- ✅ `简介和功能概述` (not 介绍 / 概述 / 介绍和功能概述)
- ✅ `缩略语` (not 术语 / 缩写词和术语 / 首字母缩略词和缩写 / 定义和缩写)
- ✅ `相关文档` (not 相关的文档)
- ✅ `约束和假设` → `限制` / `汽车域的适用性` (not 适用于汽车领域 / 适用车型域 / 对汽车域的适用性)
- ✅ `对其他模块的依赖`
- ✅ `功能规格` (not 功能规范 / 功能说明)
- ✅ `API规范` → `函数定义` / `调度函数` (not 周期函数 / Scheduled 函数) / `回调通知` / `可配置接口` (not 可配置的接口) / `期望接口`

## 3. API chapter internal structure

- Per function: `#### 7.1.x. <function name>` + `**说明**: …` + a ```C signature code block
- Grouped as in the source document: `### 7.1. 函数定义`, `### 7.2. 调度函数`, `### 7.3. 回调通知`, etc. (write a group only if the source has it)
- When there are no callbacks, state it in one sentence such as `**BswM**中没有回调通知。` — never omit the chapter

## 4. Formatting rules

- **The front-matter `title` is the page's only h1 source** — `# ` level-1 headings are forbidden in the body (they break the Material TOC)
- Heading numbering `## N. <标题>` (digit + trailing dot); heading level = numeric depth + 2 (`x.y` → `###`, `x.y.z` → `####`, and so on)
- Bold English terms (`**BswM**`); code identifiers stay untranslated (`Sd_ClientServiceSetState()`)
- No source requirement IDs (`[SWS_Adc_00122]` and the like); `{DRAFT}` markers are dropped
- Notes/tips use `**注意：**` / `**提示：**` paragraphs; tables use GFM tables; images are local PNGs inside the article directory
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

- `mode_management/guide_to_mode_management` (EXP guide structure)
- `memory/nv_data_handling_guideline` (guide structure)
- `power` (topic article, custom 11 chapters)
- `methodology_templates/basic_software_module_description_template`, `template/` (template/methodology type)
- `docs/autosar/glossary.md` (glossary — generated by `.agents/skills/autosar-translate/scripts/gen_glossary.py` from every article's chapter 2; never hand-edit; regenerate after any article's ch.2 changes)
- `docs/autosar/api_reference.md` (API list — generated by `.agents/skills/autosar-translate/scripts/gen_api_list.py` from chapter 8 of the R23-11 source documents; never hand-edit; regenerate after front-matter `spec:`/`release:` changes)
