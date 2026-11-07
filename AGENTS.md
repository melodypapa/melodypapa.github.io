# AGENTS.md — melodypapa.github.io

Personal knowledge base 「米多papa的小屋」: a Material-for-MkDocs site (Chinese content, automotive embedded software focus) deployed to GitHub Pages at https://melodypapa.github.io/.

## Layout

- `docs/` — ALL site content. **MkDocs nav paths in `mkdocs.yml` are relative to `docs/`, not the repo root.**
- `docs/autosar/` — one subtree per AUTOSAR platform (since 2026-11-02): `cp/<section>/<article>/` for Classic Platform (SWS/EXP/TPS translations + the generated API listing `cp/api/`), `foundation/<topic>/<article>/` for Foundation (RS/PRS/TPS/TR/EXP; 10 topic landings, TR Glossary translated), plus the hub `index.md`, the shared `glossary.md`, and the excluded working files (`STANDARD.md`, `TODO.md`, `sync-todo/`). Nav: one `AUTOSAR` tab → `CP（经典平台）` / `Foundation（基础标准）` groups. Old pre-move URLs are served by `mkdocs-redirects` (`redirect_maps` in `mkdocs.yml`; pinned `==1.2.2` — 1.2.3 pulls in the `properdocs` fork).
- `mkdocs.yml` — site config + explicit `nav`. Every page must be registered here or `--strict` fails; removing a page requires removing its nav entry.
- `overrides/` — Material theme customization (sidebar 常用链接 block).
- `private-docs/` — internal/unpublished corpus (S32K5/ARM study notes, NXP RM PDFs). **Git submodule** → `melodypapa/private-docs` (private; binaries pdf/pptx/xlsx/zip via Git LFS). Content work happens inside `private-docs/` and is pushed there separately (SSH remote, branch `main`). Cloning the parent needs `--recurse-submodules`, but CI builds never read `private-docs/`, so the deploy workflow runs without submodules. (Renamed from `.private/` on 2026-11-07.)
- `.github/workflows/ci.yml` — deploy. **Triggers on push to `master` only; PRs build nothing.**
- `.zcode/` — gitignored agent workspace; implementation plans live in `.zcode/plans/`.
- `site/` — build output, gitignored.

## Commands

There is no lint/test toolchain — the only quality gate is the strict build, which you MUST run before every commit (CI does not run on PRs):

```bash
# venv (no permanent one; /tmp evicts on macOS cleanup — recreate as needed, ~30s)
python3 -m venv /tmp/mkdocs-venv && /tmp/mkdocs-venv/bin/pip install -r requirements.txt

# gate: must exit 0 with zero WARNINGs
/tmp/mkdocs-venv/bin/python -m mkdocs build --strict --site-dir /tmp/mkdocs-check

# local preview
/tmp/mkdocs-venv/bin/python -m mkdocs serve
```

Pre-existing INFO-level anchor notices in build output are known and do not fail `--strict`. WARNINGs do.

## Content conventions (`docs/`)

- AUTOSAR module articles are **faithful Chinese translations** of AUTOSAR standard documents. Their mandatory structure, wording, and formatting rules are codified in **`docs/autosar/STANDARD.md`** (Type A: 7-chapter skeleton; no 需求可追溯性/时序图/配置规范 chapters or lettered appendices). **`docs/autosar/TODO.md`** tracks per-article translation progress — update it in the same PR after every sync. Read both before creating or editing any article under `docs/autosar/`; both are excluded from the site build via `exclude_docs` in `mkdocs.yml`.
- Before flagging a translation as wrong, check the source in `~/Workspace/autosar_standard/markdown/...` — the SWS (not SRS) is the structural source and the two genuinely differ in places (e.g. ADC driver "works on channel groups" is SWS-faithful).
- Translation is never delegated to subagents — the session running the translation translates the source itself, sequentially, regardless of source length (codified in the autosar-translate skill, Step 5).
- Headings: front-matter `title` is the only h1 source — **never write `# ` in a page body** (Material TOC breaks). Chapters are `## N. 标题` (number + trailing dot); heading level = numeric depth + 2. English terms bolded, code identifiers untranslated, API entries use `**说明**:` + ```C blocks.
- Section landing pages: front-matter title + intro + `## 文章` link list + `## 相关内容`; registered as the unlabeled first nav entry under their section (`navigation.indexes`).
- WeChat QR footer (where present): `<section id="wechat">` + `<h4>` — never a markdown heading.

## Git workflow

- Convention: feature branch (`feature/<topic>`) + tracking issue + PR; commits `docs:` / `feat:` / `fix:` with `Closes #N`. Use heredocs for multi-line `gh issue/pr create` bodies.
- **No co-work attribution in commits, PRs or issues** (user rule, 2026-10-28): never add `Co-Authored-By:` / `Co-worked-by:` trailers, "Generated with …" footers, or any mention of the agent/session that did the work. Commit messages and PR/issue text describe the change only.
- **Issue and PR titles + bodies are written in English** (user rule, 2026-10-25). Chinese stays in the diff and in quoted content identifiers (chapter names like `## 2. 定义和缩略语`, article text) — describe the work around them in English. PR/issue content rules: lead with a summary, group changes per area (article / skill+script / other), and end with a verification list including the strict-build result.
- GitHub auto-deletes merged remote branches; delete merged local branches with `git branch -d`.
- `github.com` over HTTPS is intermittently flaky (fetch/push timeouts). Use the SSH URL `git@github.com:melodypapa/melodypapa.github.io.git` for git transport; the `gh` CLI (api.github.com) always works.
- A failed fetch can leave `refs/remotes/origin/master` broken; repair with `git update-ref refs/remotes/origin/master <sha>`.
- `master` is branch-protected — merge via PR only. Deployment happens automatically on merge; verify the strict build locally first.

## Known gotchas

- The Jekyll-era stale `.gitignore` patterns (`_site`, `.sass-cache`, `.jekyll-cache`, `.jekyll-metadata`, `vendor`, `nxp/saf`, `eb_tresos/*`, `reference`) were removed on 2026-11-02 along with the `_site/` build, `.bundle/config`, and the default Jekyll welcome post — the repo is now mkdocs-only.
- `docs/autosar/cp/template/` holds only its landing page since 2026-11-04 (the `generic_structure` and `timimg_extension` pages were removed); `cp/others/` hosts topic articles outside a module section, currently the Full-CAN vs Basic-CAN comparison.
