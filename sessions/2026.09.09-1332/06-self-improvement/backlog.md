# Deferred backlog

| ID | Proposal | Why deferred |
| --- | --- | --- |
| P6 | Dedicated FAW / helper for dirty-tree cleanup (stash or commit WIP) before pull | Needs explicit user ask; default pull pack stays abort (Q3=A); avoid inventing stash |
| B1 | Optional `subagentStop` hook to auto-flip SESSION status on implementer blocked | Nice automation; rule/agent text is enough for now; hooks add harness complexity ([Cursor forum](https://forum.cursor.com/t/layering-managing-agents/158222/3)) |
| B2 | Machine-checkable SESSION status vs implementer outcome (script/lint) | Overkill until bookkeeping lag recurs after P3 |
| B3 | Expand pull pack with optional “fetch-only while dirty” probe for remote tip | Tradeoff vs fail-closed “no fetch while dirty”; leave as plan-optional per cycle |
| B4 | Commit/publish post-`1246` + this session SI dirt so a future pull can succeed | User remediation (clean/stash/commit) — out of SI scope; session stays blocked |
