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
- [ ] 4. User plan gate → then implementer (mandatory if plan mutates corpus FS)
- [ ] 5. implementer → 04-implementation/
- [ ] 6. auditor → 05-audit/ (rework loop if critical fail)
- [ ] 7. self-improver → 06-self-improvement/  (MANDATORY)
- [ ] 8. Close SESSION.md
```

### 0. Session bootstrap

1. Date folder: `sessions/yyyy.mm.dd` (collision → `sessions/yyyy.mm.dd-HHMM`).
2. Create phase subfolders `01`–`06` as named in [session-structure.md](references/session-structure.md).
3. Seed files from `sessions/_templates/`.
4. Write `SESSION.md` with raw goal + checklist. If this is a **program cycle**, fill Program framing (cycle id, docs-only vs mutation, `program/ROADMAP.md` pointer, **locked ROADMAP row**, prior session + **pending user gates**). One session per cycle; do not start moves inside a docs-only FAW after it passes.
5. If the user did not name the row, **orchestrator chooses** the ROADMAP primary-next (or next sensible slice), documents it, and passes it to prompt-betterment — do not re-litigate mid-cycle.

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

Pause for user answers during prompt-betterment. If answers include **Choose**, prompt-betterment must decide and document — do not forward “Choose” downstream.

**Informed consent (all user pauses):**

- Do **not** assume the user knows FAW jargon (`taxonomy`, `must-preserve`, `plan gate`, `fs_mutation`, `fail-closed`, …).
- Every clarifying question and every orchestrator-relayed gate must include: short **plain-language explanation** (what is asked + what “yes” commits to) and **pros / cons or tradeoffs** for options.
- Planner `fs_mutation` plans must include a “What the user is approving” intent-preview block the orchestrator can relay.

**User plan gate (step 4):**

- **Mandatory** when the plan includes moves/renames/deletes (or other corpus FS mutation) outside organisation-repo docs/index work — wait for explicit per-batch approval before implementer.
- **Optional** for docs-only / index / charter cycles when `ready_to_implement: yes` (still pause if the user asked to review the plan).
- Never treat a prior cycle’s approval as approval for a new batch.
- **Early/simple / first move:** also confirm taxonomy final sign-off or explicit waiver, and must-preserve draft review or waiver, before launching implementer on `fs_mutation` — with the same explanation + tradeoffs rule (not jargon-only).

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
- **Single-commit vs session finalize:** write pre-push `04-implementation` notes before commit; post-push hash/status lines cannot be in that commit — leave them dirty (known tradeoff) or allow a tiny follow-up session-only commit if the plan/user permits. Auditor: expected dirty finalize = Low, not rework.

### Done criteria

- All phase folders have their primary artifacts (or explicit blocked notes).
- `06-self-improvement/changes-applied.md` exists.
- User receives session path + audit verdict + self-improvement summary (and blocked reason if any).

## References

- [session-structure.md](references/session-structure.md)
- [handoff-templates.md](references/handoff-templates.md)
- Agents: `.cursor/agents/*.md`
- Best practices: `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`
