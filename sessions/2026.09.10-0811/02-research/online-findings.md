# Online findings — Cycle 8 Multi-experiment (remaining subset)

Brief citations for nested-git atomic path moves, worktree fail-closed, multi-remote caution, and Windows move recovery. **No agent push/pull** this cycle (path-only FS moves; remotes unchanged).

## Citations

1. **git-worktree (official)** — https://git-scm.com/docs/git-worktree.html  
   Linked worktrees store path metadata; casual moves can break absolute `gitdir` links (`worktree move` / `worktree repair`). Continuity fail-closed: if `worktree list` shows more than the main tree, **defer** rather than invent repair. Live-check: `PWAExemple` nested repos each have **one** main worktree only → ordinary intact wrapper `Move-Item` is appropriate. `WorkSpace` is deferred for **multi-remote / unexpected backup-quarantine roots**, not for linked worktrees (none found).

2. **Moving a Git repository directory (Codemia summary of standard practice)** — https://codemia.io/knowledge_hub/path/change_git_repository_directory_location  
   For a normal repo, move the whole folder including `.git`; history and remotes stay unchanged; remotes do not need rewriting because only the local path changed. Aligns with Continuity **path-only / no origin rewrite** (including `PWAExemple`’s one SSH `origin`).

3. **GitHub: splitting a subfolder into a new repository** — https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository  
   Documents `filter-repo` / subdirectory extraction. **Anti-pattern for this cycle** — Continuity forbids history rewrite and splitting nested repos out of the wrapper. Nested roots stay atomic under the dated parent move.

4. **Microsoft: robocopy** — https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
   Continuity Windows nested-`.git` lock recovery: prefer single `Move-Item`; on `PermissionDenied` / mid-move split, reunify into destination and finish remaining children with `robocopy /E /MOVE`; remove **only empty** leftover `.git` shells; never delete non-empty payload; re-attest nested git. Cycle 7 used this pattern successfully on nested trees — expect possible recurrence on `PWAExemple` (3 nested roots).

5. **Prior program Continuity (local)** — `catalogue/taxonomy.md`; Cycle 7 `sessions/2026.09.10/02-research/`; Medium Complete `sessions/2026.09.09-1612/02-research/`  
   CreationTime date labels; wrapper = dated move unit; nested `.git` atomic; LastWrite older than 90 days → `archive`; SSH alone = soft informational under path-only Continuity; opaque `.env` = path presence only; Multi-experiment partial → same row / remaining names only.

## Takeaway for planner

Recommend **path-only** intact move of **`PWAExemple` only** → `archive\2025.06.25 - PWAExemple`. Carry opaque `.env`×4 unread; leave SSH `origin` on `PWAFrontAuthTest` unchanged. Keep **`WorkSpace` fail-closed** (multi-remote + `_backups`/`_quarantine` extra roots + XL + must-preserve draft Medium flag) — do **not** schedule dedicated git-strategy **execution** this cycle unless the approved plan explicitly opts in (Q1=A default = defer). Re-scan nested `.git` / `worktree list` / `remote` immediately before the approved move; fail-closed if new hazards appear. Never rewrite `origin` URLs. After a successful `PWAExemple` move, ROADMAP Notes must still list **`WorkSpace` remaining** — row **not** Complete.
