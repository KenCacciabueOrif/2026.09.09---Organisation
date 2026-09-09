# Research brief — Finish sync / Q3b=B combined-best (`sessions/2026.09.09-1453`)

## Goal (from refined prompt)

Finish org-repo sync: **merge `origin/main` into current tip** (Q2=B), resolve every FAW-allowlist conflict under **Q3b=B** using **R1 = combined / judgment-per-hunk (`combined-best`)** (study both sides; keep most appropriate per hunk — not blind ours/theirs), complete merge so **HEAD incorporates `origin/main`**, fail-closed if blocked. Mutation: **`docs_only`**. Taxonomy / corpus moves: out of scope.

Git root only: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`.

## Recommended approach options (max 3)

### Option A — Allowlist commit → GfW merge → combined-best resolve (**recommended**)

1. Dual preflight with absolute GfW: `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (same binary for porcelain, commit, fetch, merge, resolve).
2. Classify porcelain (**GfW**). Unrelated → abort `dirty_working_tree`. Today: **allowlisted only** (19 / 0).
3. **Allowlist commit** current dirt (includes dirty overlap on 3 of 4 conflict paths + `sessions/2026.09.09-1453/`). BOM-safe message; no `--no-verify`. Re-fetch; re-check ahead/behind / optional merge-tree.
4. `git merge origin/main` (not `--ff-only`; not rebase; no `-s ours`).
5. Gate: every unmerged path ⊆ FAW allowlist. If any outside → `merge --abort`, session `blocked`, `other`/`merge_conflict`.
6. For each allowlist conflict: open both sides per hunk; apply **combined-best**; remove markers; `git add`. Log which side(s) won per file in implementation log.
7. Complete merge commit; verify HEAD is descendant of / incorporates `origin/main` (e.g. merge parents or `git merge-base --is-ancestor origin/main HEAD`).

**Tradeoffs:** Matches locks (Q2=B, Q3b=B, R1). Auth green. Conflicts expected but **resolvable** this cycle. Slight risk of imperfect hunk judgment — mitigate with study-both + judgment trail. Extra tip commit before merge is OK while already diverged.

### Option B — Path-scoped stash → merge → resolve → stash pop

Stash allowlist dirt, merge+resolve on clean tip, pop.

**Tradeoffs:** Avoids pre-merge tip commit, but pop can re-conflict on same FAW files and muddy the judgment trail. Prefer Option A while dirt already overlaps conflict paths and session docs need durable checkpoint.

### Option C — Blind `--ours` / `--theirs` whole-file

**Rejected** — contradicts refined prompt R1 / user “study both… keep most appropriate.”

## Required facts (verified this session)

| Fact | Evidence |
| --- | --- |
| Git root | GfW `rev-parse --show-toplevel` → org path |
| Remote | HTTPS `origin` → `KenCacciabueOrif/2026.09.09---Organisation.git` |
| Tracking | `main` ↔ `origin/main` |
| Local HEAD | `f3e1119b7f4dbcf0a62b509a44bdeb1fcc48186e` |
| `origin/main` | `489f03a6ab96523ac4551f12c4fcee31603ca544` |
| Merge-base | `f5012d6f2d15008e4c211a3167a6682f0a1c7b07` |
| Ahead / behind | **2 / 1** (diverged) |
| MERGE in progress? | **no** |
| GfW porcelain | 19 allowlisted (incl. `?? sessions/2026.09.09-1453/`); **0 unrelated** |
| Dirty ∩ conflict paths | 3 of 4 dirty (`01-notes.md` clean) |
| PATH git | MSYS first; helper empty |
| GfW | `...\AppData\Local\Programs\Git\cmd\git.exe` 2.54.0.windows.1; helper `manager` |
| Credential fill | **pass** (keys present only; secrets not logged) |
| Fetch | **pass** |
| `gh` | absent (optional) |
| `pull.rebase` | `false` |
| merge-tree conflicts | **same 4 FAW paths** as 1435 |
| Prior | 1435 blocked Q3b=A after conflict; aborted cleanly |

### Predicted conflicts + which side may win (planner hints)

| Path | Hunks | Combined-best lean |
| --- | --- | --- |
| `.cursor/agents/prompt-betterment.md` | 1 | Merge HEAD *unanswered→default* **+** origin *Choose all* / ask-summary |
| `.cursor/rules/full-agent-workflow.mdc` | 1 | Prefer HEAD pull/dirty/Q3c/SESSION; fold origin docs_only scaffolding phrase |
| `.../handoff-templates.md` | 2 | Keep HEAD pack/Q3c lines **+** origin Choose-all/ask-summary/docs_only focus; audit auto-merges |
| `sessions/_templates/01-notes.md` | 1 | HEAD unanswered Source language **+** origin Choose-all / ask-summary |

All ⊆ allowlist → Q3b=B may proceed.

## Pull / auth dual preflight (mandatory)

| Field | Value |
| --- | --- |
| Remote URL scheme | **https** |
| Tracking branch | `main` → `origin/main` |
| Agent PATH git | `C:\msys64\usr\bin\git.exe` (no helper) |
| Prefer GfW? | **yes** — `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| GCM / non-interactive evidence | **pass** (`credential fill`; username/password keys present; values not logged) |
| `gh` present? | **no** (optional only) |
| User-terminal note | Prior cycle history ≠ substitute for this agent merge success (Q5=A) |
| Agent **auth** ready (GfW)? | **yes** |
| Allowlisted dirty | **yes** (19) |
| Unrelated dirty | **0** |
| Diverge SHAs | local `f3e1119` / remote `489f03a` / base `f5012d6`; ahead/behind **2/1** |
| Agent **merge** ready (auth + dirty policy)? | **yes** after allowlist commit of current dirt |
| Sync success likely with Q3b=B + combined-best? | **yes** (conflicts expected but allowlist-only and authorized to resolve) |
| `blocker_type` (auth) | none |
| `blocker_type` (unrelated dirty) | none |
| `blocker_type` (if MSYS used for gate/merge) | **`agent_environment`** |
| If non-allowlist conflict appears live | `other`/`merge_conflict` + abort; never claim pull succeeded |

### Orchestrator summary fields

- **readiness (auth):** green (GfW+GCM)
- **readiness (dirty):** allowlisted only — autonomy OK; unrelated = 0
- **diverge SHAs:** `f3e1119` vs `489f03a` (base `f5012d6`); ahead/behind **2/1**
- **dirty classification:** allowlisted / unrelated = **19 / 0**
- **predicted conflicts:** 4 FAW paths (same as 1435); all allowlist-eligible under Q3b=B
- **blocker_type now:** none for auth or unrelated dirty
- **ready_to_implement:** **yes** (Option A)

## Unknowns

- Whether allowlist-commit of current WT edits changes conflict hunk text (re-run merge-tree or inspect after commit).
- Whether remote gains new commits between research and implement (re-fetch).
- Exact final wording of combined hunks (implementer judgment; log trail required).

## Risks and blockers

| Item | Severity | Classification | Notes |
| --- | --- | --- | --- |
| Content conflicts on 4 FAW paths | Expected; **resolvable** | process under Q3b=B | Combined-best required |
| Dirty overlap with conflict paths | Medium | process | Commit/stash before merge |
| Poor hunk judgment | Medium | quality | Study both; log winners; prefer coherent FAW law |
| Auto-merged regions dropping pull guidance | Medium | quality | Review full files after resolve, not only marked hunks |
| Non-allowlist conflict appears | High if appears | `other`/`merge_conflict` | Abort |
| MSYS used for gate/merge | High if used | `agent_environment` | GfW only |
| Auth / GCM failure mid-op | High if appears | `user_credentials` or `agent_environment` | Today green |
| Unrelated dirty mid-cycle | Medium | `dirty_working_tree` | Abort; list paths |
| Force / hard reset / `--no-verify` / `stash drop` | High if used | policy violation | Forbidden |
| Secrets in allowlist commit | High if done | process | Scan stage; never log fill passwords |

**Blockers for starting implement:** none (auth green, dirty ⊆ allowlist, Q3b=B + R1 locked).

Do **not** claim sync already complete — merge has not been re-run this cycle.

## Canonical references

- Refined prompt: `sessions/2026.09.09-1453/01-prompt-betterment/refined-prompt.md`
- Notes: `sessions/2026.09.09-1453/01-prompt-betterment/notes.md`
- Codebase findings: `sessions/2026.09.09-1453/02-research/codebase-findings.md`
- Online findings: `sessions/2026.09.09-1453/02-research/online-findings.md`
- Prior: `sessions/2026.09.09-1435/` (SESSION, impl log, research)
- Pack: `.cursor/skills/full-agent-workflow/references/pull-cycle.md`
- https://git-scm.com/docs/git-merge
- https://git-scm.com/docs/git-merge-tree
- https://git-scm.com/docs/git-pull
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md
- https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git?platform=windows
