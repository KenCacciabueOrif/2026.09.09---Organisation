# Improvement proposals — session `2026.09.09-1535`

**Priority lens:** diminish recurring user work; agent-owned **partial** multi-batch continuity (remaining Medium subset); encode post-move nested-git + opaque-`.env` attestations so users do not re-verify by hand.

## Online check (adopted ideas)

| Idea | Source | Adopt? |
| --- | --- | --- |
| Keep durable multi-step policy in **Skills** + thin always-on **Rules**; focused agent prompts | [Cursor agent best practices](https://cursor.com/blog/agent-best-practices) | **Yes** — partial-row progress in agents; one-liners in SKILL/rule/AGENTS |
| Focused subagents; skills for single-purpose repeatables; progressive disclosure | [Cursor subagents](https://cursor.com/docs/subagents.md) · [Skills](https://cursor.com/docs/skills.md) | **Yes** — orchestrator owns remaining-subset lock; implementer owns dest attestations; auditor verifies |
| Prefer autonomous completion over repetitive Q&A for known workflows | Same best-practices | **Yes** — do not re-ask Cycle 4 Choose pack when Continuity already locked; still fresh plan gate for remaining map |

## Prioritized backlog

| ID | Area | Problem | Proposed change | Files likely touched | Apply now? |
| --- | --- | --- | --- | --- | --- |
| P1 | orchestrator / ROADMAP / SKILL | After a **partial** multi-batch subset, ROADMAP stayed silent; next FAW could treat Medium as untouched eight | **Partial-row continuity:** when subset done and folders remain, update ROADMAP Notes (N moved / M remain); next FAW **stays on same row** locking **remaining** names — do **not** mark Complete or jump Primary next | `orchestrator.md`, `program/ROADMAP.md`, `SKILL.md`, rule/AGENTS one-liner | **Yes** |
| P2 | prompt-betterment | Next Medium cycle may re-litigate Q1–Q7 first-batch pack | **Remaining Medium Continuity:** carry layout/atomic/opaque/taxonomy/must-preserve; ask only what’s new (remaining subset size / soft-defer peers); plan gate still separate | `prompt-betterment.md`, `01-notes` template, handoff | **Yes** |
| P3 | implementer | Nested-git + opaque `.env` checks were tribal this cycle | After each approved move: log **destination** nested-`.git` attestation (expected relative path + count); if plan listed opaque secrets, `Test-Path` only (never read) | `implementer.md` | **Yes** |
| P4 | auditor / planner | Audit happened to check dest `.git`/`.env` but checklist thin | FS-mutation checklist: dest nested-git attestation + opaque path spot-check when planned; planner may require ROADMAP partial progress note in Step docs | `auditor.md`, `planner.md` (tiny) | **Yes** |
| D1 | publish hygiene | Org porcelain sprawl / EOL churn | Allowlisted publish when user asks — not user chore | — | **Defer** |
| D2 | soft-defer peers | `CursorMobileWorkspace` / `NextPWATraining` optional draft peers | Keep soft-defer until user expands — no auto-include | — | **Defer** (policy already OK) |
| D3 | taxonomy / must-preserve sign-off | Still open globally | User optional; Continuity waives for Medium — do not re-block | — | **Defer** |

## Explicit non-goals this cycle

- Marking Medium wrappers **Complete** (five remain)
- Auto-approving remaining moves without a new plan gate
- Assigning “user must check ROADMAP / `.env` / nested git every time” as a chore
