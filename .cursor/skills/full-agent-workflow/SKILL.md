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

- Audit `rework_needed: yes` with Critical and `rework_owner: implementer` (or earlier phase) → relaunch that phase, then re-audit.
- Audit Critical with `rework_owner: user` (true credential gaps / push auth) → **do not** relaunch implementer; set `SESSION.md` to `blocked` with remediation by `blocker_type`; still run `self-improver`.
- Never report the cycle as complete when Critical acceptance criteria remain unmet.
- Always run `self-improver` after audit (pass, fail, or blocked).

### Critical: auth / push (Windows HTTPS Option A)

- **Dual preflight** before commit+push: remote scheme + tracking; **agent** git path / `credential.helper` / prefer **Git for Windows** when PATH `git` is MSYS without GCM; optional user-terminal note; `gh` present/absent recorded but **not** sole credential signal when GCM works.
- Invoke agent push with GfW absolute `git.exe` when needed; do not require machine-wide PATH rewrite.
- Fail-closed: agent push/preflight fail → session `blocked` (never `complete`); `blocker_type` **`agent_environment`** vs **`user_credentials`**; do not relaunch implementer until remediated; **self-improver still runs**.
- **Never** log secrets, PATs, credential fill passwords, or full env dumps (`GITHUB_TOKEN` existence boolean-only).
- Fallbacks only if GfW+GCM fails after PATH/git fix: `gh auth git-credential`, or SSH remote + key (do not rewrite `origin` to SSH by default); Cursor Run Modes / Legacy Terminal if sandbox blocks GCM.

### Done criteria

- All phase folders have their primary artifacts (or explicit blocked notes).
- `06-self-improvement/changes-applied.md` exists.
- User receives session path + audit verdict + self-improvement summary (and blocked reason if any).

## References

- [session-structure.md](references/session-structure.md)
- [handoff-templates.md](references/handoff-templates.md)
- Agents: `.cursor/agents/*.md`
- Best practices: `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`
