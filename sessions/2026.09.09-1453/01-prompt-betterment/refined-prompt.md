# Refined prompt

**Status:** FINAL — ready for researcher → planner → implementer.

## Goal

Finish sync of this organisation repo from `origin`: merge `origin/main` into the current tip (prior cycle `2026.09.09-1435` blocked on allowlist-only conflicts), resolve every FAW-allowlist conflict by **studying both versions per file/hunk and keeping the most appropriate content** (`combined / judgment-per-hunk`), complete the merge so HEAD incorporates `origin/main`, and fail-closed (never false `complete`) if blocked.

## Constraints

- **docs_only** — no corpus moves/renames/deletes; taxonomy / must-preserve OOS
- Git ops only in org-repo root: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` (`git rev-parse --show-toplevel`)
- **Q1=A** — pull/merge `origin` into current tracking (usually `main`↔`origin/main`)
- **Q2=B** — merge commit allowed (not ff-only-only)
- **Q3** — allowlist then merge; unrelated (non-allowlist) dirty → abort `dirty_working_tree`
- **Q3b=B** — allowlist-only resolve; any non-allowlist unmerged path → abort like Q3b=A
- **R1 = combined / judgment-per-hunk (`combined-best`)** — not blind `--ours` / `--theirs`; for each conflicted region read both sides and keep the most appropriate (local, remote, or a coherent merge of both). Goal: best FAW docs + finished sync with less future user cleanup
- **Q4=A** org-repo only · **Q5=A** agent Shell must succeed · **Q6=A** fail-closed + typed blocker · **Q7=A** full session docs
- No `-s ours`; no force-push; no hard reset; no `--no-verify`; no `stash drop` on conflict
- Windows: prefer Git for Windows + GCM when PATH git lacks helper; same binary for dirty gate and merge

## Context pointers

- Prior: `sessions/2026.09.09-1435/` (`blocked`, `other`/`merge_conflict`); tip notes `f3e1119` vs `origin/main` `489f03a` — **verify live**
- Expected conflict paths (resolve under R1; verify live; same rule for any *new* allowlist-only conflicts):
  - `.cursor/agents/prompt-betterment.md`
  - `.cursor/rules/full-agent-workflow.mdc`
  - `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
  - `sessions/_templates/01-notes.md`
- Pack: `.cursor/skills/full-agent-workflow/references/pull-cycle.md`
- Phase notes: `sessions/2026.09.09-1453/01-prompt-betterment/notes.md`
- Tips: `sessions/2026.09.09-1453/01-prompt-betterment/online-prompt-tips.md`

## Acceptance criteria

- [ ] Dual preflight green (or typed env/credentials block): remote/tracking + agent git/GCM; porcelain classified allowlist vs unrelated
- [ ] Under Q2=B, merge of `origin/<tracking>` proceeds from current tip
- [ ] Every unmerged path is ⊆ FAW dirty allowlist (`sessions/**`, `.cursor/skills/full-agent-workflow/**`, `.cursor/agents/**`, `.cursor/rules/**`, `AGENTS.md`, `sessions/_templates/**`); **if any path is outside → abort**, keep recoverable state, `blocker_type` `other`/`merge_conflict` (or dirty as applicable), session `blocked`, never claim pull succeeded
- [ ] For each allowlist conflict file (the 4 prior paths and any new allowlist-only conflicts): agent **studies both versions per conflicted hunk**, keeps the **most appropriate** content (local, remote, or coherent merge), removes markers, `git add`
- [ ] Implementation log briefly notes per conflict file which side(s) were kept / how merged (judgment trail)
- [ ] Merge completed successfully; **HEAD incorporates `origin/main`** (sync AC met)
- [ ] On auth/env/unrelated-dirty/non-allowlist-conflict failure: session `blocked` + typed `blocker_type`; no force/hard reset/`--no-verify`
- [ ] Self-improver **mandatory**; mandate: **diminish user workload** — encode autonomy in agents/skills/rules so recurring sync/conflict cleanup is not dumped on the user as constant checks/tasks

## Out of scope

- Taxonomy ratification; must-preserve lock; corpus FS mutation
- Blind whole-file ours/theirs without reading both sides
- Resolving non-allowlist conflict paths
- Treating user-terminal pull as agent success
- False session `complete` when sync unmet
