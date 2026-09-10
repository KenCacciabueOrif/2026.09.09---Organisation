# Proposals — Cycle 9 self-improvement

## Prioritized backlog

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | Orchestrator / Continuity | After a successful Q1=A docs_only WorkSpace defer, next “next cycle” could misread process pass as Multi-experiment Complete / Primary next / Special git | Encode **post–docs_only defer**: still lock WorkSpace-only; **repeated research+defer valid** until cleared or Q1=B; never force-move | `orchestrator.md`, `SKILL.md`, `rules`, `AGENTS.md`, handoffs, templates |
| P2 | Prompt-betterment | User bare **yes** (not Choose all) worked this cycle but was informal | Encode Continuity-pack **yes→defaults** (parallel to plan-gate typo tolerance); Source `yes→defaults`; Continuity yes ≠ move approval | `prompt-betterment.md`, `orchestrator.md`, handoffs, `01-notes.md` |
| P3 | Researcher | Cycle 8 deferred P6; Cycle 9 proved WorkSpace-only research path | Add WorkSpace-only hazard live-check + fail-closed recommend; no peer re-propose; no user PATH chores | `researcher.md` |
| P4 | Planner / auditor | Defer success might drive Complete/Primary-next Steps or audit silence | Planner: repeated docs_only defer plans valid; Auditor: WorkSpace-only defer checklist (not Complete / not Primary next) | `planner.md`, `auditor.md` |
| P5 | Orchestrator housekeeping | SESSION checklist lag + duplicate empty rows | Defer — cosmetic; orchestrator already expected to refresh at close | (backlog) |
| P6 | Architecture | Continuity bullets duplicated across agents/skill/rules | Extract `references/continuity-locks.md` when more multi-batch rows appear — avoid large rewrite now | (backlog; Cursor: keep prompts concise) |

## Online check (short)

| Source | Takeaway adopted? |
| --- | --- |
| [Cursor subagents docs](https://cursor.com/docs/subagents.md) — focused responsibility; keep prompts concise; invest in descriptions | **Adopted:** small Continuity encodings across existing agents; no new generic agent; avoided large rewrite (P6 deferred) |
| [Skills vs Rules vs Subagents (forum)](https://forum.cursor.com/t/skills-vs-commands-vs-rules/148875) — rules for always-on law; skills for workflows | **Adopted:** mirrored Continuity in `full-agent-workflow.mdc` + skill bootstrap + agent files |
| [Agent skills / keep focused](https://github.com/hutchic/.cursor/blob/main/docs/cursor-skills.md) — progressive detail; avoid bloating SKILL body | **Adopted:** one-sentence post-defer / yes→defaults additions; no new mega-doc this cycle |

## Priority for apply-now

**P1–P4** (high value, low risk, agent-owned Continuity). Defer P5–P6.
