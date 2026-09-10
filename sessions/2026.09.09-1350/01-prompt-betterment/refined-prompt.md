# Refined prompt — Pull-autonomy

## Goal

1. **Fix FAW git dirty-tree deadlock:** Update organisation-repo workflow so agent `git pull` / `git push` (publish) cycles can complete **without requiring the user to clean FAW session dirt**. Replace pull-cycle’s abort-only default for expected FAW dirt with **path-scoped auto-commit** of an explicit allowlist, then sync — still **fail-closed** (no force push, hard reset, or `--no-verify`).
2. **Same session:** After the policy/docs update lands, run **agent Shell** `git pull --ff-only` from `origin` into `main`/`origin/main` tracking inside the org-repo only, incorporating remote changes (including a session made elsewhere) under the new dirty policy.

## Constraints

- **Git root only:** `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` (`git rev-parse --show-toplevel`). Never sibling trees under `C:\Project`.
- **No** force push, hard reset, `--no-verify`, or git config changes.
- **Secrets** never logged or committed intentionally.
- **Taxonomy / must-preserve** gates: out of scope — do not block.
- **Mutation class:** `docs_only` + org-repo git ops (no corpus moves/renames/deletes).
- **Windows:** Dual preflight (remote + agent git/GCM). Prefer Git for Windows absolute `...\Git\cmd\git.exe` when PATH `git` is MSYS without helper. Use the **same** GfW binary for `status --porcelain`, allowlisted commit, and pull.
- **Combine strategy:** `git pull --ff-only` (or fetch + ff-only merge) after the tree is pullable.
- **Conflict / failure:** Fail-closed; keep any WIP allowlist commit recoverable; never `stash drop` / force / hard reset; typed `blocker_type`; session `blocked` (never false `complete`); **self-improver still runs**.
- Prefer **commit over stash/autostash** for automation (do not introduce stash/autostash as the default dirty handler).

## Context pointers

- Prior blocked pull: `sessions/2026.09.09-1332/` (`dirty_working_tree`, Q3=A abort)
- Pull pack (update): `.cursor/skills/full-agent-workflow/references/pull-cycle.md`
- Publish pack (mirror dirty autonomy): `.cursor/skills/full-agent-workflow/references/publish-cycle.md`
- Also align as needed: `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/rules/full-agent-workflow.mdc`, `.cursor/agents/{prompt-betterment,researcher,planner,implementer,auditor,orchestrator}.md`, `AGENTS.md`, handoff/session-structure refs that still say “default dirty = abort”
- This session: `sessions/2026.09.09-1350/`
- Prompt notes: `sessions/2026.09.09-1350/01-prompt-betterment/notes.md`

## Locked dirty allowlist (explicit)

When porcelain is non-empty before pull (or before publish when applying Q9 mirror), the agent **may auto-commit only**:

| Include | Paths |
| --- | --- |
| Sessions | `sessions/**` |
| FAW meta | `.cursor/skills/full-agent-workflow/**` |
| FAW meta | `.cursor/agents/**` |
| FAW meta | `.cursor/rules/**` (workflow rule edits from this cycle) |
| FAW meta | `AGENTS.md` |
| FAW meta | `sessions/_templates/**` (if dirty) |

**Outside allowlist** → do **not** auto-commit or stash; **abort** with listed paths and `blocker_type: dirty_working_tree`; session `blocked`.

Auto-commit message: agent-drafted, why-focused, repo style, BOM-safe on Windows PowerShell; no secrets.

## Acceptance criteria / verification

### A — Workflow docs (implement first)

1. `pull-cycle.md` Q3 / dirty policy updated: FAW default = **allowlisted auto-commit then pull**; abort retained **only** for unrelated (non-allowlist) dirty. Disclosed Choose default and `blocker_type` text updated accordingly (abort is no longer the universal FAW default).
2. `publish-cycle.md` (and related skill/rule/agent/handoff text as needed) **mirrors** the same allowlist autonomy for push/publish dirty handling; unrelated dirty still aborts.
3. Allowlist paths above are **documented** in the updated references (and match this AC).
4. Standing constraints preserved: org-repo root only; GfW same-binary gate; fail-closed; no force/hard reset/`--no-verify`; self-improver still runs on block.
5. Auditor/implementer guidance no longer treats “any dirty → always user cleanup” as the only correct pull path when dirt is allowlisted.

### B — Same-session agent pull (after A)

6. Dual preflight green (or fail-closed with typed blocker if not).
7. If dirty ⊆ allowlist only: agent creates allowlist commit(s) as needed so porcelain for non-allowlist is empty / tree is pullable per policy; then agent runs `git pull --ff-only` (GfW) of `origin` into current `main`↔`origin/main` tracking.
8. If any non-allowlist dirty remains: abort pull, list paths, `blocker_type: dirty_working_tree`, session `blocked` — do not claim pull success.
9. On pull conflict or non-ff failure: fail-closed per Q3b/Q6; WIP allowlist commit left recoverable; session `blocked` with accurate `blocker_type`; never mark `complete`.
10. Success = agent Shell pull succeeded (ff-only) **or** correctly blocked with typed blocker; remote session-elsewhere changes incorporated when pull succeeds; full FAW artifacts under `sessions/2026.09.09-1350/`.
11. User terminal pull alone is **not** success (Q5 A).

## Out of scope

- Corpus moves/renames/deletes; taxonomy final ratification; must-preserve lock
- Auto-committing or stashing non-allowlist paths; commit-all WIP; stash/autostash as default dirty handler
- Force push, hard reset, `--no-verify`, rebase-as-default, merge commits (unless a later user-approved cycle changes Q2)
- Sibling `C:\Project` git ops
- Treating prior session’s Q3=A Choose as binding continuity for this cycle (explicitly superseded)

## Definition of done (one-liner)

FAW pull/publish docs default to allowlisted session/FAW-meta auto-commit then `--ff-only`, and this session’s agent successfully pulls (or correctly fail-closes) without asking the user to clean session dirt.
