# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | pull-cycle pack | Q2=B unlocks merge but Q3b=A aborts on **allowlist-only** FAW doc conflicts → sync unmet with no Choose path to finish | Expand **Q3b**: A=abort (default); **B=allowlist-only resolve** (ours/theirs/combined + documented rule in `notes.md`) when all conflict paths ⊆ allowlist; any non-allowlist conflict → fail-closed. Keep unrelated paths hard-abort | `references/pull-cycle.md`, `prompt-betterment.md`, `handoff-templates.md` |
| P2 | blocker vocabulary | `other`/`merge_conflict` used well this cycle but standing docs stress `non_ff` more | Document **`blocker_type: other`** vocabulary **`merge_conflict`** (and outcome `blocked_conflict`) alongside `non_ff`; auditor/implementer/orchestrator recognize both; never claim sync success | `pull-cycle.md`, `implementer.md`, `orchestrator.md`, `auditor.md`, `SKILL.md`, `AGENTS.md`, rule `.mdc` |
| P3 | finish-sync backlog | Next cycle needs an explicit path after this abort | Backlog B1: new FAW cycle with Q2=B + **Q3b=B** (allowlist resolve) **or** user resolves 4 paths then agent pull/merge; never silent resolve under old Q3b=A lock | `06-self-improvement/backlog.md` (session) |
| P4 | templates | Plan template mentions push preflight more than pull conflict outcomes | Tiny note on pull plans: document success vs `blocked_conflict` / `other`+`merge_conflict` | `sessions/_templates/03-plan.md` |
| P5 | deferred | Auto-default Q3b=B when merge-tree predicts only allowlist conflicts | Too aggressive for Choose defaults; keep default **A** until user opts in | (none now) |

## Online best-practice notes

- **Skills stay modular; detailed runbooks in references** — Cursor skills docs: keep `SKILL.md` focused; put pack detail in reference files (adopted: extend `pull-cycle.md`, not balloon SKILL). https://cursor.com/docs/skills
- **Focused subagents + concise prompts** — Subagents best practices: single responsibility, avoid overlong prompts (adopted: small additive blocker/Q3b lines in agents, not rewrite). https://cursor.com/docs/subagents
- **Explicit file-boundary / conflict policy** — Community guidance: conflicts need explicit path rules and human Choose before merge accept (adopted: allowlist-only resolve only when Choose says so; fail-closed outside allowlist). https://dredyson.com/how-i-solved-the-multitask-in-agents-window-problem-a-complete-step-by-step-beginners-guide-to-parallel-agent-work-byok-fixes-and-conflict-resolution/

## Apply this cycle

- **Apply now:** P1, P2, P4 (small safe docs).
- **Defer:** P3 as session backlog text (documented, not code); P5 remains deferred.
