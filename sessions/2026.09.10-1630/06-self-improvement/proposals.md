# Improvement proposals — Cycle 13

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | auditor + orchestrator | Auditor is `readonly: true`; Cursor blocks all writes. Cycles 12–13 both needed orchestrator persist, but agent text still says “write when possible / if blocked.” | State clearly: readonly → **expect** Write fail; **always** return full `report.md` body; include `write_status: blocked_returned_inline` (or `written` if ever writable). Orchestrator **always** verifies/persists `05-audit/report.md` from return body before self-improver. | `.cursor/agents/auditor.md`, `.cursor/agents/orchestrator.md`, `handoff-templates.md` |
| P2 | orchestrator + skill | STAGE 1 same-run auto-continue (docs_only + ready_to_implement yes) worked but is only Continuity/user-goal tribal knowledge. | Add explicit bullet: after planner, if `docs_only` + `ready_to_implement: yes` + no plan gate → continue implement→audit→self-improver **same run**; pause only for `fs_mutation` or not-ready / user-asked review. | `.cursor/agents/orchestrator.md`, `SKILL.md`, optionally `AGENTS.md` / rule one-liner |
| P3 | templates | SESSION template notes auditor persist but not STAGE same-run auto-continue. | Tiny note under plan-gate / mutation: docs_only ready → no mandatory pause. | `sessions/_templates/SESSION.md` |
| P4 | Continuity | yes→defaults for continue strategy already solid this cycle. | No change unless a gap appears — keep as-is. | — |
| P5 | WorkSpace-only law | Cycles 11–13 pattern held; law already in orchestrator/skill/rules. | No new product Continuity; optionally add STAGE to self-improver focus list. | `handoff-templates.md` self-improver focus |
| P6 | hooks (deferred) | Cursor docs suggest hooks to persist subagent outputs. | Defer — orchestrator persist is FAW equivalent; hooks = larger infra. | — |
| P7 | auditor writable (deferred) | Flip auditor to `readonly: false` so it can write only under `05-audit/`. | Defer — keeps verifier non-mutating by design; parent persist matches Cursor guidance for readonly agents. | — |

## Online best-practice notes

- **Readonly subagents cannot write anywhere** (including session artifacts / tmp) — intended pattern is return findings in the final message; parent aggregates/persists. Matches Cycles 12–13 FAW friction. Adopted into P1. — https://forum.cursor.com/t/explore-sub-agents-silently-cannot-complete-file-writing-tasks-e-g-write-to-tmp/162369
- **Custom subagent `readonly: true`** blocks file edits and state-changing shell; default for custom agents is writable (`false`). Auditor stays readonly for verification purity; orchestrator owns artifact files. — https://cursor.com/docs/subagents.md
- **Orchestrator + focused workers:** parent coordinates; specialists return structured results; hooks optional for auto-save. We keep agent-owned persist over user chores / hooks for now (P6 deferred). — https://cursor.com/docs/subagents.md ; https://deepakness.com/raw/cursor-orchestrator-worker/

## Priority this cycle

Apply **P1** + **P2** (+ light **P3**/**P5**) now. Defer P6–P7. Skip P4 (already good).
