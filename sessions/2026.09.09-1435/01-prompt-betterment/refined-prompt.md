# Refined prompt

## Goal

Finish org-repo sync after session `2026.09.09-1350` (`blocked` / `other`/`non_ff`, 1/1 diverge): via **agent Shell** using **Git for Windows + GCM**, combine the local tip with **`origin/main`** using an **allowed merge commit** (Q2=B), so sync acceptance criteria are met—or correctly fail-closed with a typed blocker (never false `complete`).

## Constraints

- Git ops only inside org-repo root: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` (Q4=A)
- Remote/branch: `origin` ↔ current tracking, usually `main`↔`origin/main` (Q1=A)
- Combine strategy: **merge commit allowed** (Q2=B) — do not fall back to ff-only-only or silent rebase
- Dirty handling: order-aware FAW allowlist autonomy, then merge (Q3/Q3c C-like for already-diverged state); unrelated dirty → abort `dirty_working_tree`
- On conflict: fail-closed; keep WIP commit and/or stash recoverable; no force, hard reset, `--no-verify`, or `stash drop` (Q3b=A)
- Same GfW binary for dirty gate, allowlist commit/stash, and pull/merge
- Secrets never logged in session artifacts or commits
- Mutation class: `docs_only` (no corpus moves)
- Taxonomy / must-preserve: out of scope
- Agent Shell success required for `complete` (Q5=A); user terminal alone insufficient
- On failure: fail-closed + typed `blocker_type` + self-improver still runs (Q6=A)
- Session docs: full FAW artifacts under this session (Q7=A)

## Context pointers

- Prior: `sessions/2026.09.09-1350/` — HEAD was `7ac4783` vs `origin/main` `489f03a` (1/1); allowlist WIP kept; backlog B1
- Pack: `.cursor/skills/full-agent-workflow/references/pull-cycle.md`
- This session: `sessions/2026.09.09-1435/`
- Locks: `01-prompt-betterment/notes.md` (Answers)

## Acceptance criteria

- [ ] All git ops confined to org-repo root (Q4=A); no sibling trees
- [ ] Dual preflight (remote/tracking + agent GfW/GCM); same GfW binary for porcelain, allowlist commit/stash, and merge pull
- [ ] Dirty ⊆ allowlist handled order-aware then **merge** (or clean merge if no dirt); unrelated dirty → `blocked` / `dirty_working_tree` (sync unmet)
- [ ] Agent pull with **merge** (Q2=B) succeeds: **HEAD incorporates `origin/main` via merge** (sync AC met)
- [ ] On merge conflict or other failure: fail-closed (Q3b=A / Q6=A); WIP/stash recoverable; typed `blocker_type`; session `blocked`; never claim pull succeeded
- [ ] No force-push, hard reset, `--no-verify`, or `stash drop` on conflict
- [ ] Secrets never present in logs/commits
- [ ] Full FAW session artifacts written (Q7=A)
- [ ] Session `complete` **only** if sync AC met; else `blocked` (never false complete); self-improver still runs either way
- [ ] Taxonomy / must-preserve / corpus FS moves untouched

## Out of scope

- Corpus FS moves / taxonomy ratification / must-preserve lock
- Force / hard reset / `--no-verify` / `stash drop` on conflict
- Re-litigating Q2 to ff-only or silent rebase
- Sibling trees under multi-root workspace
- Treating user-terminal-only pull as agent success
