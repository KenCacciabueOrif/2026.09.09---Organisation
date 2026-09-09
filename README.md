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

## Project corpus program

Cycle 0+ documentation for analysing and (later) organising `C:\Project`:

| Path | Role |
| --- | --- |
| [`program/CHARTER.md`](program/CHARTER.md) | Program purpose, safety, cycle model |
| [`program/ROADMAP.md`](program/ROADMAP.md) | Adaptive multi-cycle roadmap + approval gates |
| [`program/organisation-approach.md`](program/organisation-approach.md) | Organisation options + preferred hybrid approach |
| [`catalogue/INDEX.md`](catalogue/INDEX.md) | Whole-corpus navigation index |
| [`catalogue/inventory.md`](catalogue/inventory.md) | Coarse inventory |
| [`catalogue/taxonomy.md`](catalogue/taxonomy.md) | `yyyy.mm.dd - Name` naming proposal |

## Windows git push (agent Shell)

Goals that `git push` from the **agent** (not only your interactive terminal) need Git Credential Manager via **Git for Windows**, not MSYS git without a helper. Agents prefer the GfW absolute `git.exe` path; optional tip: put `...\Git\cmd` **before** MSYS on your user PATH so default `git` matches. Details: `AGENTS.md` (Commands / verification). Missing `gh` alone is not a credential failure when GCM works.
