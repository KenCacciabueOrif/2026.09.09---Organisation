---
name: full-agent-workflow
description: >-
  Runs the project full agent cycle with a pure orchestrator that only delegates
  to prompt-betterment, researcher, planner, implementer, auditor, then mandatory
  self-improver. Use when the user asks for the full agent workflow, /full-agent-workflow,
  orchestrated delivery, or any non-trivial multi-phase goal in this organisation repo.
---

# Full agent workflow

## Role

When this skill applies, **you are the orchestrator**. Follow `.cursor/agents/orchestrator.md`.

- Do not research, plan, implement, or audit the user goal yourself.
- Create the dated session folder, delegate each phase subagent, connect outputs, update `SESSION.md`.
- Always end with `self-improver`.

## Trigger

User invokes `/full-agent-workflow`, `@orchestrator`, or states a goal that needs the full cycle.

## Steps

Copy and track:

```
Workflow progress:
- [ ] 0. Session bootstrap (sessions/yyyy.mm.dd/)
- [ ] 1. prompt-betterment → 01-prompt-betterment/
- [ ] 2. researcher → 02-research/
- [ ] 3. planner → 03-plan/
- [ ] 4. User plan gate (if user wants approval) → then implementer
- [ ] 5. implementer → 04-implementation/
- [ ] 6. auditor → 05-audit/ (rework loop if critical fail)
- [ ] 7. self-improver → 06-self-improvement/  (MANDATORY)
- [ ] 8. Close SESSION.md
```

### 0. Session bootstrap

1. Date folder: `sessions/yyyy.mm.dd` (collision → `sessions/yyyy.mm.dd-HHMM`).
2. Create phase subfolders `01`–`06` as named in [session-structure.md](references/session-structure.md).
3. Seed files from `sessions/_templates/`.
4. Write `SESSION.md` with raw goal + checklist.

### 1–6. Delegate

Launch each custom subagent with a handoff matching [handoff-templates.md](references/handoff-templates.md).

| Phase | Agent name |
| --- | --- |
| Prompt betterment | `prompt-betterment` |
| Research | `researcher` |
| Plan | `planner` |
| Implement | `implementer` |
| Audit | `auditor` |
| Self-improve | `self-improver` |

Pause for user answers during prompt-betterment. Optionally pause after plan for approval on large/risky work.

### Rework

- Audit `rework_needed: yes` with Critical → relaunch `implementer` (or earlier phase), then re-audit.
- Then still run `self-improver`.

### Done criteria

- All phase folders have their primary artifacts (or explicit blocked notes).
- `06-self-improvement/changes-applied.md` exists.
- User receives session path + audit verdict + self-improvement summary.

## References

- [session-structure.md](references/session-structure.md)
- [handoff-templates.md](references/handoff-templates.md)
- Agents: `.cursor/agents/*.md`
- Best practices: `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`
