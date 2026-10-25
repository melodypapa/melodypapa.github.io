# AGENTS.md — melodypapa.github.io

Personal knowledge base 「米多papa的小屋」: a Material-for-MkDocs site (Chinese content, automotive embedded software focus) deployed to GitHub Pages at https://melodypapa.github.io/.

## Layout

- `docs/` — ALL site content. **MkDocs nav paths in `mkdocs.yml` are relative to `docs/`, not the repo root.**
- `mkdocs.yml` — site config + explicit `nav`. Every page must be registered here or `--strict` fails; removing a page requires removing its nav entry.
- `overrides/` — Material theme customization (sidebar 常用链接 block).
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
- Headings: front-matter `title` is the only h1 source — **never write `# ` in a page body** (Material TOC breaks). Chapters are `## N. 标题` (number + trailing dot); heading level = numeric depth + 2. English terms bolded, code identifiers untranslated, API entries use `**说明**:` + ```C blocks.
- Section landing pages: front-matter title + intro + `## 文章` link list + `## 相关内容`; registered as the unlabeled first nav entry under their section (`navigation.indexes`).
- WeChat QR footer (where present): `<section id="wechat">` + `<h4>` — never a markdown heading.

## Git workflow

- Convention: feature branch (`feature/<topic>`) + tracking issue + PR; commits `docs:` / `feat:` / `fix:` with `Closes #N`. Use heredocs for multi-line `gh issue/pr create` bodies.
- **Issue and PR titles + bodies are written in English** (user rule, 2026-10-25). Chinese stays in the diff and in quoted content identifiers (chapter names like `## 2. 定义和缩略语`, article text) — describe the work around them in English. PR/issue content rules: lead with a summary, group changes per area (article / skill+script / other), and end with a verification list including the strict-build result.
- GitHub auto-deletes merged remote branches; delete merged local branches with `git branch -d`.
- `github.com` over HTTPS is intermittently flaky (fetch/push timeouts). Use the SSH URL `git@github.com:melodypapa/melodypapa.github.io.git` for git transport; the `gh` CLI (api.github.com) always works.
- A failed fetch can leave `refs/remotes/origin/master` broken; repair with `git update-ref refs/remotes/origin/master <sha>`.
- `master` is branch-protected — merge via PR only. Deployment happens automatically on merge; verify the strict build locally first.

## Known gotchas

- `.gitignore` contains stale root-anchored patterns from the Jekyll era (`eb_tresos/safety_os`, `nxp/saf`, `reference`) that do **not** match anything under `docs/` — `git check-ignore` results can mislead; trust `git ls-files`.
- `docs/autosar/template/timimg_extension/indx.md` — directory and filename typos that are load-bearing: `mkdocs.yml` nav references `indx.md` explicitly. Fixing the name requires a nav change in the same commit.
