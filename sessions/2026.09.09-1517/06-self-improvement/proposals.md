# Improvement proposals — session `2026.09.09-1517`

**Priority lens:** diminish recurring user work; agent-owned ROADMAP continuity after a multi-batch row finishes; safer Medium wrappers first batch; fail-closed on stale INDEX paths.

## Online check (adopted ideas)

| Idea | Source | Adopt? |
| --- | --- | --- |
| Keep durable multi-step policy in **Skills** + thin always-on **Rules**; focused agent prompts | [Cursor agent best practices](https://cursor.com/blog/agent-best-practices) | **Yes** — row-completion + INDEX live-verify in agents; one-liners in SKILL/rule |
| Focused subagents with clear boundaries; progressive disclosure via refs | [Cursor subagents](https://cursor.com/docs/subagents.md) · [Skills](https://cursor.com/docs/skills.md) | **Yes** — researcher owns path truth; orchestrator owns next-row lock; PB owns Medium first-batch asks |
| Prefer autonomous completion over repetitive Q&A for known workflows | Same best-practices | **Yes** — do not re-ask Early/simple when ROADMAP marks Complete; lock Primary next |

## Prioritized backlog

| ID | Area | Problem | Proposed change | Files likely touched | Apply now? |
| --- | --- | --- | --- | --- | --- |
| P1 | orchestrator / SKILL / ROADMAP | After multi-batch row Complete, “next cycle” may re-open finished Early/simple via stale “prefer Early/simple” prose | **Row-completion continuity:** when ROADMAP marks a row **Complete**, next FAW locks **Primary next →** (here: Medium wrappers); do not re-litigate finished row; prefer Suggested-order primary-next over stale “How the next cycle starts” bullets; refresh that ROADMAP section | `orchestrator.md`, `SKILL.md`, `program/ROADMAP.md`, rule one-liner | **Yes** |
| P2 | researcher | INDEX can lag disk; risk of proposing re-moves | **Live path truth:** for in-scope + recently moved siblings, `Test-Path` INDEX current path vs disk; if source already at dest → verify-only / catalogue fix, never re-move | `researcher.md`, handoff cue | **Yes** |
| P3 | prompt-betterment | Medium wrappers (8, nested git, `.env`) lack first-batch defaults | When locked row = Medium wrappers: informed-consent asks for **subset** (default small no-/single-nested slice), atomic nested git, `.env` opaque, plan gate still separate; do not re-ask Early/simple | `prompt-betterment.md`, `01-notes` Continuity hint | **Yes** |
| P4 | planner | “First move / Early-simple gate” wording may re-block Medium after Continuity Q3/Q4 locks | Treat Continuity taxonomy/must-preserve locks from prior cycles as satisfying Early-simple gate for later rows; Medium plans: subset map, nested `.git` atomic, opaque `.env` | `planner.md` | **Yes** |
| P5 | implementer | PS param typo nearly confused retry | Corpus moves: `Move-Item -LiteralPath … -Destination …` (full param names); dry-check params before first move | `implementer.md` | **Yes** (tiny) |
| D1 | publish hygiene | Org porcelain sprawl | Allowlisted publish cycle when user asks — not user chore every session | — | **Defer** |
| D2 | taxonomy continuity wording | Cycle 2 subset wording in taxonomy | Optional Continuity refresh — not AC; leave until user asks | — | **Defer** |

## Explicit non-goals this cycle

- Changing fail-closed for unexpected `.git` / must-preserve
- Auto-approving Medium moves without plan gate
- Assigning “user must check INDEX every time” as a chore
