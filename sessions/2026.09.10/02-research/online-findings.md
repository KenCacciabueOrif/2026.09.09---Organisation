# Online findings — Cycle 7 Multi-experiment (first subset)

Brief citations for nested-git atomic path moves, worktree fail-closed, and multi-remote caution. **No agent push/pull** this cycle (path-only FS moves; remotes unchanged).

## Citations

1. **git-worktree (official)** — https://git-scm.com/docs/git-worktree.html  
   Linked worktrees store path metadata; moving a main or linked tree casually can break absolute `gitdir` links (`worktree move` / `worktree repair`). Continuity fail-closed: if `worktree list` shows more than the main tree, **defer** rather than invent repair. Live-check: recommended peers (`GitTest`, `WorkStationPWA`) each nested repo has **one** main worktree only → ordinary intact wrapper `Move-Item` is appropriate. `WorkSpace` deferred for multi-remote / extra roots, not for linked worktrees.

2. **Moving a Git repository directory (Codemia summary of standard practice)** — https://codemia.io/knowledge_hub/path/change_git_repository_directory_location  
   For a normal repo, move the whole folder including `.git`; history and remotes stay unchanged; remotes do not need rewriting because the local path changed. Aligns with Q3=A **path-only / no origin rewrite**. Problems arise with worktrees / separate-git-dir — which we screen and fail-closed.

3. **GitHub: splitting a subfolder into a new repository** — https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository  
   Documents `filter-repo` / subdirectory extraction. **Anti-pattern for this cycle** — Continuity forbids history rewrite and splitting nested repos out of the wrapper. Nested roots stay atomic under the dated parent move.

4. **Prior program Continuity (local)** — `catalogue/taxonomy.md`; Cycle 6 research `sessions/2026.09.09-1612/02-research/`; Medium/Early sessions `2026.09.09-1535`, `2026.09.09-1554`  
   CreationTime date labels; wrapper = dated move unit; nested `.git` atomic; LastWrite older than 90 days → `archive`; SSH alone = soft informational under path-only Continuity (not hard abort when peers are otherwise clean); opaque `.env` = path presence only.

## Takeaway for planner

Recommend **path-only** intact moves of **`GitTest`** and **`WorkStationPWA`** into `archive` with CreationTime date labels. Do **not** open a dedicated git-strategy FAW for those two. **Defer `WorkSpace`** (multi-remote + unexpected backup/quarantine roots + XL + must-preserve draft flag) until a later cycle / possible git-strategy. Hold **`PWAExemple`** for the next Multi-experiment sub-batch (movable but not lowest-risk). Re-scan nested `.git` / `worktree list` / `remote` immediately before each approved move; fail-closed if new hazards appear. Never rewrite `origin` URLs.
