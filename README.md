# Organisation — full agent workflow

This repo defines an **orchestrator-led** Cursor agent cycle aligned with `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`.

## Quick start

1. Open Agent chat in this project.
2. Run `/full-agent-workflow` (or state a goal and ask to use the full workflow).
3. Answer clarifying questions from **prompt-betterment**.
4. Optionally approve the plan, then let implement → audit → **self-improve** finish.
5. Review artifacts under `sessions/yyyy.mm.dd/`.

## Architecture

```
User goal
   ↓
orchestrator (direct only)
   ├─ prompt-betterment
   ├─ researcher
   ├─ planner
   ├─ implementer
   ├─ auditor
   └─ self-improver  ← every cycle
```

| Path | Purpose |
| --- | --- |
| `.cursor/agents/` | Orchestrator + phase subagents |
| `.cursor/skills/full-agent-workflow/` | Slash/auto workflow skill |
| `.cursor/rules/full-agent-workflow.mdc` | Always-on orchestration law |
| `sessions/` | Dated session documentation |
| `AGENTS.md` | Portable project law |
| `AGENT-AND-WORKFLOW-BEST-PRACTICES.md` | Source best-practices guide |

## Session folders

Named `yyyy.mm.dd` (example `2026.09.09`). Same-day collision uses `yyyy.mm.dd-HHMM`.
