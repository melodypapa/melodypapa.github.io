# Todo files — batch queue format and rules

The translation program's todo is a set of **persistent batch-queue files**
(SKILL.md Step 4), modelled on py-armodel `sync-autosar-class`'s Group files
(Rules 0016.6/0016.7/0018 there), adapted to one article per run.

- **Status ledger** = `docs/autosar/TODO.md` — what each article currently IS
  (✅/🔶/⚠️/⛔/❌/📖) and site-wide counts.
- **Execution queue** = `docs/autosar/sync-todo/` — what to do next: one
  `Group-<section>.md` per batch, one row per document; `index.md` holds the
  recommended batch order.

Both live in the repo, excluded from the site build (`exclude_docs`), updated
in the same PR as the article.

## Files

```
docs/autosar/sync-todo/
  index.md            # batch order + counts + resume rules
  Group-io.md         # one batch file per section/topic
  Group-general.md
  ...
  Group-exp.md
```

**Resume rule:** pick the batch (user names it, or the first unfinished batch
in index order) → read the file → take the **first row still `[ ]`** → run the
6 steps. Do not re-derive scope from TODO.md or the source tree; do not re-ask
decisions already in the row's Notes.

## Row format

```markdown
- [ ] <article-dir-or-slug> (<SWS_Name> · R23-11 markdown · <status/gap>)
  - Note: <known gaps — from TODO.md row + prior audits; run findings appended>
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
```

- The parenthetical carries the short fixed fields only: specification name ·
  source · status tag (✅ alignment only / ⚠️ gaps / ⛔ stub — full
  translation / ❌ new article / 📖 skeleton-exempt).
- **Findings, counts and decisions go on `- Note:` bullets under the row**,
  never on the checkbox line — long markup-heavy lines break the exact-line
  toggle (the py-armodel Group 4 incident). A line past ~200 characters is a
  violation to split before touching the row.
- One verifiable action per step; **tick in the file the moment a step
  passes** — never batch at the end. A legitimately N/A step is ticked with
  the reason (`- [x] Step 4 — … (N/A: pure alignment, no new content)`), not
  deleted.
- Step 6's note records the commit hash and PR link. The row flips `[ ]` →
  `[x]` only then — **no `[x]` before the commit exists** (py-armodel Rule
  0017.2).
- **Reopen**: to redo a finished row (new release, drift, user request), reset
  it to `[ ]` with `- Note: reopen <reason> <date>` — never delete the
  finished state.
- The **Not queued** section per file records deliberate exclusions (exempt 📖/📄
  articles, topic articles/historical snapshots) so a resumed session never
  re-flags them.
- **Never work around a failed row edit** with a side section ("已确认",
  "batch confirmation") elsewhere in the file — fix the row shape (split the
  long line), then flip the row in place.

## Language

Queue files are written in **English** (headings, prose, Notes, step labels).
Quoted Chinese strings are allowed only when they name a Chinese article
heading or a site-canonical term — e.g. `4.2 "对汽车域的适用性" → "汽车域的适用性"` —
because those strings are the article content, not queue prose.

## Historical format

`dio_driver.md` in this directory is a completed run in the earlier
per-article format (superseded by batch rows); kept as an audit trail and
format example.
