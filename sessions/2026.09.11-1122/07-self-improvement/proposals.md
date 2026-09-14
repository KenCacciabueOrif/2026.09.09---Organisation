# Improvement proposals — Cycle 17

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | skill / templates / handoffs | Mid-cycle SESSION lag: Workflow updated but Phase checklist/summaries lagged; skill+template+handoff omit **Phase summaries** while orchestrator already requires them | Align all surfaces: before next-phase launch flip Workflow progress **+ Phase checklist + Phase summaries**; mid handoff + post-auditor persist/flip before SI; auditor Low flags summaries lag | `SKILL.md`, `sessions/_templates/SESSION.md`, `handoff-templates.md`, `auditor.md` |
| P2 | handoffs | After auditor return, persist+flip before SI was implicit; lag risk on resume | Explicit orchestrator line after auditor: persist `06-audit/report.md`, flip 06 in all three SESSION surfaces, then launch SI | `handoff-templates.md` |
| P3 | rules / AGENTS | Dual-git + complete gate already amended this cycle; residual wording drift risk | Spot-check only if P1 edits touch rules; no bulk rewrite | `.cursor/rules/full-agent-workflow.mdc`, `AGENTS.md` (defer unless drift found) |
| P4 | verification | Ask-readonly Shell blocks auditor porcelain re-verify | Keep Read/Glob fallback; defer product “grant Shell for readonly audit” | backlog (B3 carry) |
| P5 | harness | Optional cheaper worker models for implementer | Needs user opt-in; defer | backlog |
| P6 | program | WorkSpace whole-tree / XL clearance still uncleared | Not FAW meta; next lock WorkSpace only | backlog |

## Prioritization (apply now)

1. **P1 + P2** — highest value, low risk; directly remediates auditor Low and prevents recurrence under dual-git cycles.
2. P3–P6 — defer or skip.

## Online best-practice notes

- **Skills vs rules vs subagents:** Skills for on-demand workflows; rules for always-on law; subagents for isolated multi-step roles — matches FAW (skill = cycle procedure; rule = dual-git/complete gate; agents = phases). Adopted: keep dual-git in skill+rule+agent, not skill-only. — https://cursor.com/blog/agent-best-practices · https://cursor.com/docs/subagents.md
- **Parent verifies handoffs:** Parent/orchestrator must inspect returns and persist readonly auditor output — reinforces mandatory `06-audit/report.md` persist + SESSION flip before next launch. — https://cursor.com/docs/subagents.md · delegation-contract pattern (parent verifies, completion ≠ acceptance)
- **Narrow single-purpose agents:** Do not expand self-improver into product work; keep orchestrator non-implementing for user goals. — https://www.learncursor.dev/learn/cursor-agents/cursor-agent-skills
