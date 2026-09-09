# Changes applied

## Applied

- `.cursor/agents/researcher.md` — mandatory push/auth preflight in research brief blockers when goal includes remote publish.
- `.cursor/agents/planner.md` — auth step + `ready_to_implement: no` / blocking question when credentials unverified.
- `.cursor/agents/implementer.md` — BOM-safe PowerShell commit guidance; `blocked` + `blocker_type: user_credentials` instead of false complete.
- `.cursor/agents/orchestrator.md` — credential-blocker path: `SESSION.md` blocked, no implementer relaunch, still self-improve.
- `.cursor/agents/auditor.md` — `rework_owner` field; user-owned auth rework vs implementer rework.
- `.cursor/skills/full-agent-workflow/SKILL.md` — rework rules for user credential Criticals; never false complete.
- `.cursor/skills/full-agent-workflow/references/handoff-templates.md` — researcher auth preflight + auditor `rework_owner`.
- `.cursor/rules/full-agent-workflow.mdc` — blocked/auth honesty + self-improve on blocked.
- `sessions/_templates/02-research-brief.md` — push/auth preflight slot under Unknowns/blockers.
- `sessions/_templates/03-plan.md` — auth/preflight step + auth risk row.
- `AGENTS.md` — early push-auth verification + PowerShell BOM-safe commit note.

## Why

This cycle failed on foreseeable GitHub HTTPS auth and a PowerShell UTF-8 BOM on the commit subject. Workflow docs previously green-lit implement and implied Critical → always relaunch implementer. Updates make preflight early, BOM-safe commits default, and blocked-on-credentials an explicit non-complete path.

## No safe improvement

N/A — improvements applied.
