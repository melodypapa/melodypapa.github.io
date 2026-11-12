# S32G3 sync-todo — batch order

Execution queue for the `nxp-translate` skill. One row = one chapter = one run.
**Resume rule:** take the first row still `[ ]` in chapter order; do not
re-derive scope from the source tree or re-ask decisions already recorded in
the row's Notes.

| Batch | Chapters | File |
| --- | --- | --- |
| 1 | 1-4 (front matter) | `Group-front-matter.md` |
| 2 | 5-23 (System Modules) | `Group-system-modules.md` |
| 3 | 24-28 (Clocking) | `Group-clocking.md` |
| 4 | 29-31 (Reset and Boot) | `Group-reset.md` |
| 5 | 32-35 (Power Management) | `Group-power-management.md` |
| 6 | 36-40 (Memories and Memory I/Fs) | `Group-memories.md` |
| 7 | 41-45 (Timers) | `Group-timers.md` |
| 8 | 46-57 (Communication Modules) | `Group-communication.md` |
| 9 | 58-60 (Analog Modules) | `Group-analog.md` |
| 10 | 61-65 (Security) | `Group-security.md` |
| 11 | 66-77 (Safety) | `Group-safety.md` |
| 12 | 78-81 (Debug) | `Group-debug.md` |

All 12 batch queue files exist; each lists one row per chapter. A row gets a
6-step sub-checklist when its chapter is picked up. Full queue created
2026-11-12 (earlier runs created files lazily). Baseline: S32G3RM Rev. 5,
2025-09-17.
