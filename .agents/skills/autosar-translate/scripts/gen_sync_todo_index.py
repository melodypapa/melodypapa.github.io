#!/usr/bin/env python3
"""Generate the translation-queue index report (SyncTodoIndex.md).

Aggregates every Group-*.md queue file in docs/autosar/sync-todo/ into one
per-group status table, in the same shape as py-armodel's
docs/plan/sync-todo/SyncTodoIndex.md:

    ## GroupN
    Status: **M/N** completed
    | Article | Status | Commit ID |

Status values:
  [x] Done      — all 6 queue steps complete (row `[x]`)
  [ ] Aligned   — the article already exists on the site but the queue steps
                  are not ticked; the marker (✅/🔶/⚠️/📖) from the row
                  annotation is kept when present
  [ ] Pending   — the article does not exist yet

Commit ID: the commit sha(s) recorded on the row (or its Step 6), else the
PR number, else the commit that added the article's index.md, else N/A.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
QUEUE_DIR = os.path.join(ROOT, "docs", "autosar", "sync-todo")
OUT = os.path.join(QUEUE_DIR, "SyncTodoIndex.md")


def git(*args):
    try:
        return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True,
                              check=True).stdout.strip()
    except subprocess.CalledProcessError:
        return ""


_ls = None


def article_exists(name):
    global _ls
    if _ls is None:
        _ls = git("ls-files", "docs/autosar").splitlines()
    return any(l.endswith(f"/{name}/index.md") for l in _ls)


def article_add_commit(name):
    path = next((l for l in (git("ls-files", "docs/autosar").splitlines())
                 if l.endswith(f"/{name}/index.md")), "")
    if not path:
        return ""
    return git("log", "--diff-filter=A", "--format=%h", "-1", "--", path)


def parse_group(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    rows = []
    i = 0
    while i < len(lines):
        m = re.match(r"^- \[([ x])\] (?!Step\b)(.+?)$", lines[i])
        if not m:
            i += 1
            continue
        done = m.group(1) == "x"
        rest = m.group(2).strip()
        name = rest.split(" (", 1)[0].strip()
        # block = the row line + indented Step/Note lines
        block = [lines[i]]
        j = i + 1
        while j < len(lines) and lines[j].startswith(("  -", "    ")):
            block.append(lines[j])
            j += 1
        if done:
            status = "Done"
        else:
            exists = article_exists(name)
            mm = re.search(r"[·\s](✅|🔶|⚠️|📖)", rest)
            if exists:
                status = f"Aligned {mm.group(1)}" if mm else "Aligned"
            else:
                status = "Pending"
        rows.append((name, done, status, "\n".join(block)))
        i = j
    return title, rows


def commit_ref(done, name, block):
    m = re.search(r"commits? ([0-9a-f]{7,40}(?:\s*/\s*[0-9a-f]{7,40})*)", block)
    if m:
        return "/".join(s[:10] for s in re.split(r"/\s*", m.group(1)))
    m = re.search(r"PR #(\d+)", block)
    if m:
        return f"PR #{m.group(1)}"
    if done or article_exists(name):
        c = article_add_commit(name)
        if c:
            return c
    return "N/A"


def main():
    files = sorted(f for f in os.listdir(QUEUE_DIR) if re.match(r"Group-.*\.md$", f))
    out = []
    out.append("# All Sync Todo Articles by Group\n")
    out.append("Generated from all Group files in `docs/autosar/sync-todo/` — "
               "articles ordered by group, then by appearance order within each group. "
               "Regenerate with `python .agents/skills/autosar-translate/scripts/gen_sync_todo_index.py`.\n")
    out.append("Status `Done` = all 6 queue steps complete (translation merged). "
               "Status `Aligned` = the article already exists on the site but the queue steps "
               "are not ticked — the remaining steps are an alignment pass, not a fresh "
               "translation (the row's ✅/🔶/⚠️/📖 marker is kept). Status `Pending` = the article "
               "does not exist yet. Commit ID = the translation commit sha(s) or PR recorded on "
               "the queue row (falling back to the commit that added the article); "
               "`N/A` = work not started.\n")

    total_done = total = 0
    for f in files:
        title, rows = parse_group(os.path.join(QUEUE_DIR, f))
        if not rows:
            continue
        gname = re.sub(r"^Sync todo:\s*", "", title) if title else f[:-3]
        done = sum(1 for _, d, *_ in rows if d)
        total_done += done
        total += len(rows)
        out.append(f"## {gname}\n")
        out.append(f"Status: **{done}/{len(rows)}** completed\n")
        w = max(len(r[0]) for r in rows) + 2
        out.append(f"| {'Article'.ljust(w)} | Status | Commit ID |")
        out.append(f"| {'-' * (w + 1)} | -------- | ---------- |")
        for name, done_f, status, block in rows:
            mark = "[x]" if done_f else "[ ]"
            out.append(f"| `{name}`".ljust(w + 4)
                       + f" | {mark} {status} | {commit_ref(done_f, name, block)} |")
        out.append("")
    out.append(f"**Total: {total_done}/{total} queue rows complete.**\n")
    open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"wrote {OUT}: {total_done}/{total} rows across {len(files)} groups")


if __name__ == "__main__":
    sys.exit(main())
