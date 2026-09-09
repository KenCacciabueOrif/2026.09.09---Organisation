# AGENTS.md

Portable project law for this organisation repo (Cursor and other agent harnesses).

## Default workflow

For non-trivial goals, run the **full agent workflow**:

1. Act as **orchestrator only** (see `.cursor/agents/orchestrator.md` and skill `full-agent-workflow`).
2. Delegate in order: `prompt-betterment` → `researcher` → `planner` → `implementer` → `auditor` → **`self-improver` (mandatory)**.
3. Document everything under `sessions/yyyy.mm.dd/` (collision: `yyyy.mm.dd-HHMM`).

Do not skip self-improvement after a cycle.

## Session docs

- Templates: `sessions/_templates/`
- Layout: `.cursor/skills/full-agent-workflow/references/session-structure.md`

## Agent roles

| Agent | Does | Does not |
| --- | --- | --- |
| orchestrator | Session bootstrap, handoffs, routing | Research, plan body, implement, audit |
| prompt-betterment | Questions + prompt refine + prompt-engineering search | Domain solution design |
| researcher | Codebase + online evidence | Plan / code |
| planner | `plan.md` | Code |
| implementer | Execute plan | Scope expansion |
| auditor | Verify vs criteria | Silent fixes |
| self-improver | Audit process; improve agents/skills/rules/templates | Ignore end-of-cycle |

## Commands / verification

- Prefer explicit acceptance criteria in the plan before implementation.
- After implementation, prefer tests/typecheck/lint named in the plan.
- Prefer revert + better plan over compounding a bad run.
- **Multi-cycle / corpus FS:** Prefer one FAW session per program cycle (`program/ROADMAP.md` when present). Orchestrator locks the ROADMAP row (chooses if user said “next”) and carries pending sign-off gates. Plans declare `docs_only` vs `fs_mutation`; **user approval is mandatory** before implementer for move/rename/delete batches; git roots are atomic unless a dedicated git-strategy plan says otherwise. User **Choose** → prompt-betterment decides and documents. Taxonomy **proposed-ratified** and must-preserve **draft** are not final until user sign-off or explicit waiver; first move / Early-simple fail-closed on those gates.
- **Informed consent asks:** Clarifying questions and plan-gate (or other) approvals must include short **plain-language explanation** (what is asked + what “yes” commits to) and **pros/cons or tradeoffs**. Do not assume the user already knows workflow jargon.
- Goals that require `git push` or `git pull`: early dual preflight (remote + **agent** git/GCM — on Windows prefer Git for Windows when PATH git is MSYS without helper); user terminal success ≠ agent ready; missing `gh` alone ≠ missing credentials when GCM works. Fail-closed: never mark complete if agent push/pull failed, unrelated dirty-aborted, or non-ff refused; `blocker_type` `dirty_working_tree` (unrelated only) vs `agent_environment` vs `user_credentials` vs `other`/non-ff; still run self-improver. Optional user tip: put Git for Windows `cmd` before MSYS on PATH; agents still invoke GfW via absolute path when needed.
- **Publish / pull / org-repo only:** stage and commit / pull only inside this repo’s git root (`rev-parse --show-toplevel`); never sibling trees under a multi-root workspace. Prompt-betterment uses the publish pack in `.cursor/skills/full-agent-workflow/references/publish-cycle.md` or the pull pack in `references/pull-cycle.md`; unanswered pack items with disclosed defaults → Choose those defaults. FAW dirty default = allowlisted auto-commit (`sessions/**`, FAW skill/agents/rules, `AGENTS.md`, `sessions/_templates/**`) then `--ff-only`; abort only for unrelated dirty → session `blocked`, not false complete. Expected post-allowlist non-ff → `blocked` + keep WIP commit (no merge/rebase unless user changes combine strategy).
- Single-commit publish: write implementation log **before** commit; post-push hash/status notes may stay uncommitted (known tradeoff) or use a tiny session-only follow-up commit if allowed — do not fail the cycle solely for that dirtiness (auditor: expected dirty finalize = Low, not rework).
- On Windows PowerShell, write commit message files **without** a UTF-8 BOM (`utf8NoBOM` / `UTF8Encoding($false)` / here-string `-m`); Windows PS 5.1 `Set-Content -Encoding utf8` adds a BOM.

## Safety

- No secrets in commits or session logs.
- Small diffs; no force-push; commit only when the user asks.

## Deeper guidance

See `AGENT-AND-WORKFLOW-BEST-PRACTICES.md` for Cursor mode, rules, skills, hooks, and maturity ladder.
