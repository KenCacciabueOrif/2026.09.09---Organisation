# Proposals — session `2026.09.09-1453`

**Priority lens:** diminish **user** workload. Prefer FAW defaults / agent autonomy so the next finish-sync needs fewer Choose questions and no “user must resolve” backlog. Still fail-closed for unrelated / non-allowlist conflicts (no force / hard reset).

## Online check (adopted ideas)

| Idea | Source | Adopt? |
| --- | --- | --- |
| Put durable workflow policy in **Skills** (on-demand) + thin **Rules**; keep agent prompts focused | [Cursor agent best practices](https://cursor.com/blog/agent-best-practices) | **Yes** — encode finish-sync defaults in `pull-cycle.md` (skill ref); mirror one-liners in rule/agents |
| Focused subagents; invest in clear responsibility boundaries | [Cursor subagents docs](https://cursor.com/docs/subagents.md) | **Yes** — self-improver owns autonomy encoding; orchestrator carries continuity locks, does not implement resolve |
| Prefer autonomous agent completion over constant interactive Q&A for repetitive workflows | Same best-practices (skills for repetitive workflows) | **Yes** — continuity defaults for allowlist-only finish-sync |

## Prioritized backlog

| ID | Area | Problem | Proposed change | Files likely touched | Apply now? |
| --- | --- | --- | --- | --- | --- |
| P1 | pull-cycle pack | Q3b unanswered default stays **A**; finish-sync still re-asks / dumps Choose on user | **Continuity default:** when prior session `merge_conflict` with predicted/confirmed **allowlist-only** conflicts, **or** user said merge+resolve / finish-sync → disclosed default **Q3b=B** + R1 **`combined-best`** (judgment-per-hunk). Generic first-time pull stays Q3b=A. Document `combined-best` as standing resolve rule next to ours/theirs/combined. Next-cycle remediation = **agent continuity** (lock B+combined-best), not “user must resolve” | `references/pull-cycle.md` | **Yes** |
| P2 | prompt-betterment | Still frames B as “surface option” only | On finish-sync / continuity: **lock** Q3b=B + combined-best via Choose(unanswered→default) or continuity; skip re-asking R1/Q3b when locks already clear; do not invent user chores | `prompt-betterment.md` | **Yes** |
| P3 | orchestrator | Remediation text prefers “user Choose or user resolves” for allowlist-only conflicts | After allowlist-only `merge_conflict` under Q3b=A: next FAW carries continuity locks Q2=B (if merge already chosen) + Q3b=B + combined-best; **agent-owned**; user ask only if non-allowlist or strategy change needed | `orchestrator.md` | **Yes** |
| P4 | auditor / handoffs | Allowlist-only conflict abort can read as `rework_owner: user` | For allowlist-only `merge_conflict` under Q3b=A: `rework_owner: orchestrator` (next FAW continuity) — **not** user. Reserve `user` for unrelated dirty / non-allowlist conflict / true credentials | `auditor.md`, `handoff-templates.md` | **Yes** |
| P5 | self-improver + handoff | Mandate not standing law | Standing: prioritize diminishing user workload; agent-owned allowlist remediation; no backlog that assigns recurring user checks | `self-improver.md`, handoff self-improver block | **Yes** |
| P6 | rule / AGENTS / SKILL | Always-on law still “Q3b=B only when Choose” without continuity exception | One-line continuity default for finish-sync allowlist-only | `full-agent-workflow.mdc`, `AGENTS.md`, `SKILL.md` | **Yes** |
| P7 | templates | Continuity section silent on finish-sync locks | Brief pointer: finish-sync may lock Q3b=B + combined-best | `sessions/_templates/01-notes.md` | **Yes** |
| P8 | implementer | Combined-best preference when R1 unset under Q3b=B | If Q3b=B locked and R1 blank on finish-sync → default combined-best | `implementer.md` | **Yes** (tiny) |
| D1 | agent_environment | MSYS vs GfW PATH order | Optional user tip already exists; **do not** backlog recurring “user must check PATH every pull” — agent keeps absolute GfW | — | **Defer / drop as user chore** |
| D2 | merge-tree automation | Researcher could auto-flip Q3b default from merge-tree | Nice-to-have script/check; pack prose in P1 covers policy | — | **Defer (agent-owned later)** |

## Explicit non-goals this cycle

- Changing fail-closed for non-allowlist / unrelated dirty
- Force-push, hard reset, silent resolve under Q3b=A on a **first** generic ff-only pull
- Dumping “user should verify GfW / re-run merge-tree every time” into backlog
