# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | researcher | Push auth discovered only at implement | For goals that include `git push` / publish to remote: preflight remote URL, `gh auth status` (if `gh` present), credential helper / non-interactive probe notes; list auth as blocker when unverified | `.cursor/agents/researcher.md`, `sessions/_templates/02-research-brief.md`, handoff template |
| P2 | planner | `ready_to_implement: yes` despite unknown push auth | Plans with push acceptance criteria must include an early auth/preflight step; if research marks credentials unverified/blocked, set `ready_to_implement: no` or blocking question for user auth | `.cursor/agents/planner.md`, `sessions/_templates/03-plan.md` |
| P3 | implementer | PowerShell UTF-8 BOM corrupts commit subject | Forbid `Set-Content -Encoding utf8` (Windows PS 5.1 BOM) for commit `-F` files; prefer here-string `git commit -m`, PS 7 `utf8NoBOM`, or `[System.IO.File]::WriteAllText(..., UTF8Encoding($false))`; verify `git log -1` has no BOM | `.cursor/agents/implementer.md` |
| P4 | implementer / orchestrator | Risk of false “complete” when push fails | On credential/auth push failure: status `blocked` (not `complete`); report remediation; never claim Done if push criterion unmet | `.cursor/agents/implementer.md`, `.cursor/agents/orchestrator.md` |
| P5 | skill / auditor | Critical rework always relaunches implementer | Credential/auth blockers → user remediation + `SESSION.md` `blocked`; do **not** relaunch implementer until auth exists; still run self-improver | `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/agents/auditor.md`, `.cursor/rules/full-agent-workflow.mdc` |
| P6 | templates | Research/plan templates omit auth + status vocabulary | Add Unknowns/blockers + preflight checklist hooks; plan Risks note for auth-blocked path | `sessions/_templates/02-research-brief.md`, `03-plan.md` |
| P7 | AGENTS.md | No Windows commit-message BOM note | One-line git hygiene: BOM-safe commit messages on PowerShell | `AGENTS.md` |
| P8 | deferred | Dirty post-commit session logs | Optional: stage session updates in a follow-up commit or document “session dirt after commit is expected” | backlog only this cycle |
| P9 | deferred | Amend/correct BOM on `9708f2e` | User-driven corrective commit after auth works — product/git fix, not workflow machinery | backlog / user |

## Online best-practice notes

Adopted this cycle:

- **Independent verification / skeptical auditor** — Cursor docs recommend a verifier that confirms claimed work actually succeeded and reports incomplete work honestly ([Cursor Subagents](https://cursor.com/docs/subagents.md)). Aligns with keeping audit fail on unmet push and not labeling cycles “complete.”
- **Skills for workflows; rules for always-on law** — Keep credential-blocker rework rules in the skill + a short always-on note ([Cursor agent best practices](https://cursor.com/blog/agent-best-practices)).
- **Focused subagents + clear handoffs** — Persist phase state in session markdown; pass explicit blockers in handoffs rather than assuming chat memory ([Cursor Subagents](https://cursor.com/docs/subagents.md); handoff patterns in community agent-handoff designs).
- **PowerShell UTF-8 BOM** — Windows PowerShell 5.1 `Set-Content -Encoding utf8` writes a BOM; use BOM-less APIs or PS7 `utf8NoBOM` for git commit message files ([Stack Overflow: UTF-8 without BOM](https://stackoverflow.com/questions/5596982/using-powershell-to-write-a-file-in-utf-8-without-the-bom)).

Not adopted now (deferred):

- Separate QA-handoff skill with multi-round verify loops (useful later; heavier than this cycle needs).
- Parallel subagent workstreams / worktrees (N/A for sequential git publish).
