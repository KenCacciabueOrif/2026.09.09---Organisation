# Online findings — Cycle 6 Medium wrappers (soft-deferred finalization)

Brief citations — no agent push/pull; focus = atomic wrapper + nested-`.git` relocate (not history rewrite).

## Citations

1. **git-worktree (official)** — https://git-scm.com/docs/git-worktree.html  
   Extra linked worktrees store path metadata; relocating the main tree without care can break absolute links to linked checkouts (`repair` exists for that case). Live-check: both nested repos have **one** main worktree only, no `.git/worktrees`, no gitfile → ordinary directory move of the wrapper is appropriate; fail-closed if a pre-move re-scan finds linked worktrees.

2. **GitHub: splitting a subfolder into a new repository** — https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository  
   Documents `git filter-repo` / subdirectory extraction. **Out of scope:** Continuity forbids history rewrite and splitting wrapper from nested git. Cited as anti-pattern — do **not** use here.

3. **Prior program Continuity (local)** — `catalogue/taxonomy.md`; Cycle 4–5 research under `sessions/2026.09.09-1535/` and `sessions/2026.09.09-1554/`  
   CreationTime date labels; wrapper = dated move unit; nested `.git` moves atomically; LastWrite within 90 days of `2026.09.09` → `paused`, else `archive`; SSH alone was soft-prefer defer when safer peers existed, not a hard worktree/multi-remote abort; path-only move with **no** remote URL rewrite.

## Takeaway for planner

Both soft-deferred wrappers are green for path-only `Move-Item` into status parents (`archive` for NextPWA; `paused` for CursorMobile), preserving nested `.git` and opaque `.env` (NextPWA path present — never read). No online requirement to open a dedicated git-strategy FAW for this pair. Re-scan worktrees immediately before each move; fail-closed only if new linked-worktree / multi-remote / unclear-git hazards appear.
