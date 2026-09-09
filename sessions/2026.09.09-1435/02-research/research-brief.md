# Research brief — Pull-merge (`sessions/2026.09.09-1435`)

## Goal (from refined prompt)

Via **agent Shell** + **Git for Windows + GCM**, finish org-repo sync after `2026.09.09-1350` non_ff: combine local tip with **`origin/main`** using an **allowed merge commit (Q2=B)**. Allowlist dirty autonomy then merge. Fail-closed on conflict (Q3b=A). Never false `complete`. Mutation: **`docs_only`**. Taxonomy / corpus moves: out of scope.

Git root only: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`.

## Recommended approach options (max 3)

### Option A — Allowlist commit → GfW fetch → merge `origin/main` (**recommended**)

1. Dual preflight with absolute GfW: `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (same binary for porcelain, commit/stash, merge).
2. Classify porcelain (**GfW only**). Unrelated → abort `dirty_working_tree`. Today: **allowlisted only**.
3. **Allowlist commit** remaining dirt (durable checkpoint; already diverged so stash→ff-only is not the finish path). BOM-safe message; no `--no-verify`.
4. `git fetch origin` then `git merge origin/main` (or `git pull --no-rebase origin main`). Do **not** use `--ff-only`.
5. On **conflict**: fail-closed (Q3b=A) — prefer `git merge --abort` to restore pre-merge tip; keep allowlist commit(s) / any stash recoverable; no force / hard reset / `stash drop`. Session **`blocked`**, typed blocker (e.g. `other` + conflict note). Self-improver still runs.
6. On **clean merge**: verify HEAD is a merge commit (or otherwise incorporates `origin/main`); sync AC met → proceed audit toward `complete`.

**Tradeoffs:** Matches Q2=B and continuity with 1350 B1. Auth green. **High probability of content conflicts** (see merge-tree) → likely **process-correct block** rather than sync success this turn unless implementer is later authorized to resolve conflicts (out of scope under Q3b=A fail-closed).

### Option B — Path-scoped stash → merge → stash pop

Stash allowlist dirt, merge, pop.

**Tradeoffs:** Avoids an extra tip commit before merge, but pop can re-conflict on the same FAW files. Prefer Option A while already 1/1 diverged and dirt is policy/session docs.

### Option C — Soft-reset recover tip + Q3c stash→ff→pop

Undo `7ac4783` as commit, then ff-only.

**Tradeoffs:** **Rejected** — user locked **Q2=B merge**; do not re-litigate to recover+ff. Soft-reset risks are out of Q3b spirit unless user explicitly chooses that recovery path.

## Required facts (verified this session)

| Fact | Evidence |
| --- | --- |
| Git root | GfW `rev-parse --show-toplevel` → org path |
| Remote | HTTPS `origin` → `KenCacciabueOrif/2026.09.09---Organisation.git` |
| Tracking | `main` ↔ `origin/main` |
| Local HEAD | `7ac47835abd7ccb56195bae0daf364baef3e2580` |
| `origin/main` | `489f03a6ab96523ac4551f12c4fcee31603ca544` (fetch + ls-remote agree) |
| Merge-base | `f5012d6f2d15008e4c211a3167a6682f0a1c7b07` |
| Ahead / behind | **1 / 1** (diverged) |
| GfW porcelain | Allowlisted dirty + `?? sessions/2026.09.09-1435/` |
| Allowlisted / unrelated | **all dirty / 0** |
| PATH git | MSYS first; helper empty |
| GfW | `...\AppData\Local\Programs\Git\cmd\git.exe` 2.54.0.windows.1; helper `manager` |
| Credential fill | **pass** (presence only logged) |
| Fetch | **pass** |
| `gh` | absent (optional) |
| `pull.rebase` | `false` |
| merge-tree conflicts | **4 files** (prompt-betterment.md, full-agent-workflow.mdc, handoff-templates.md, `sessions/_templates/01-notes.md`) |
| Prior | 1350 blocked non_ff; backlog B1 |

## Pull / auth dual preflight (mandatory)

| Field | Value |
| --- | --- |
| Remote URL scheme | **https** |
| Tracking branch | `main` → `origin/main` |
| Agent PATH git | `C:\msys64\usr\bin\git.exe` |
| Prefer GfW? | **yes** — `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| GCM / non-interactive evidence | **pass** (fill + fetch; secrets not logged) |
| `gh` present? | **no** (optional only) |
| User-terminal note | Prior user/agent history ≠ substitute for this agent merge success (Q5=A) |
| Agent **auth** ready (GfW)? | **yes** |
| Allowlisted dirty | **yes** (multiple FAW/session paths + new session dir) |
| Unrelated dirty | **0** (GfW gate) |
| Diverge SHAs | local `7ac4783` / remote `489f03a` / base `f5012d6` |
| Agent **merge** ready (auth + dirty policy)? | **yes** to *attempt* |
| Agent **sync success** likely without conflict resolution? | **no** — merge-tree predicts conflicts |
| `blocker_type` (auth) | none |
| `blocker_type` (unrelated dirty) | none |
| `blocker_type` (if MSYS used for gate/merge) | **`agent_environment`** |
| Expected post-merge attempt if conflicts | session **`blocked`**; keep WIP; **not** `dirty_working_tree`; classify **`other`** (conflict / merge unmet) — do not claim pull succeeded |

**Do not claim `blockers: none` for the sync goal** while merge-tree shows conflicts that Q3b=A will not resolve. Auth and dirty gates are green for *starting* Option A.

### Orchestrator summary fields

- **readiness (auth):** green (GfW+GCM)
- **readiness (dirty):** allowlisted only — autonomy OK; unrelated = 0
- **diverge SHAs:** `7ac4783` vs `489f03a` (base `f5012d6`); ahead/behind **1/1**
- **dirty classification:** allowlisted / unrelated = all / **0**
- **blocker_type now:** none for auth or unrelated dirty; **predicted post-attempt:** `other` (merge conflict) unless conflicts auto-resolve unexpectedly
- **ready_to_implement:** **yes** (Option A — attempt merge; fail-closed on conflict)

## Unknowns

- Whether working-tree edits (post-1350 self-improver) change conflict set after allowlist commit (re-run merge-tree / merge at implement).
- Whether remote gains new commits between research and implement (re-fetch).
- Exact conflict hunks after commit of current dirty FAW files.

## Risks and blockers

| Item | Severity | Classification | Notes |
| --- | --- | --- | --- |
| Content conflicts on 4 FAW paths | **High for sync AC** | `other` (conflict) after fail-closed | Expected; Q3b=A |
| Dirty overlap with conflict paths | Medium | process | Commit/stash before merge |
| MSYS porcelain false unrelated | High if used | `agent_environment` | Gate with GfW only |
| Auth / GCM failure mid-merge | High if appears | `user_credentials` or `agent_environment` | Today green |
| Unrelated dirty appearing mid-cycle | Medium | `dirty_working_tree` | Abort; list paths |
| Force / hard reset temptation | High if used | policy violation | Forbidden |
| Secrets in allowlist commit | High if done | process | Scan stage; never log fill passwords |
| Taxonomy / must-preserve | None | out of scope | Do not gate |

## Canonical references

- Refined prompt: `sessions/2026.09.09-1435/01-prompt-betterment/refined-prompt.md`
- Notes: `sessions/2026.09.09-1435/01-prompt-betterment/notes.md`
- Codebase findings: `sessions/2026.09.09-1435/02-research/codebase-findings.md`
- Online findings: `sessions/2026.09.09-1435/02-research/online-findings.md`
- Prior: `sessions/2026.09.09-1350/` (SESSION, impl log, backlog B1)
- Pack: `.cursor/skills/full-agent-workflow/references/pull-cycle.md`
- https://git-scm.com/docs/git-merge
- https://git-scm.com/docs/git-pull
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md
- https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git?platform=windows

## Ready for planner

**`ready_to_implement: yes`** for Option A:

1. Re-run GfW dual preflight + allowlist classification at implement.
2. Allowlist-commit dirty (or path-stash if preferred mid-step).
3. Fetch + **merge** `origin/main` (Q2=B).
4. If conflicts: fail-closed (`merge --abort` preferred), typed blocker, session `blocked`, WIP recoverable; self-improver still runs.
5. If merge succeeds: verify HEAD incorporates `origin/main`; continue audit.
6. Never `complete` on unmet sync; never use MSYS for gate/merge.

**Planner should disclose:** merge-tree already shows **four content conflicts**; sync AC may remain unmet under Q3b=A even though auth/dirty gates are green. Correct fail-closed is an allowed process outcome—not false complete.
