# Online findings — Cycle 5 Medium wrappers (safer three)

Brief citations — no agent push/pull; focus = atomic wrapper + nested-`.git` relocate (not history rewrite).

## Citations

1. **git-worktree (official)** — https://git-scm.com/docs/git-worktree  
   Extra linked worktrees store path metadata; relocating without care can break absolute links. Live-check: each in-scope nested repo has **one** main worktree only → ordinary directory move of the wrapper is appropriate; fail-closed if a pre-move re-scan finds `.git/worktrees` or a `.git` file pointer.

2. **GitHub: splitting a subfolder into a new repository** — https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository  
   Documents `git filter-repo` / subdirectory extraction. **Out of scope** for this cycle: program Continuity forbids history rewrite and splitting wrapper from nested git. Cited to mark the anti-pattern — do **not** use filter-repo here.

3. **Prior program Continuity (local)** — `catalogue/taxonomy.md`, Cycle 4 `sessions/2026.09.09-1535/02-research/`  
   CreationTime date labels; wrapper = dated move unit; nested `.git` moves atomically; LastWrite within 90 days of `2026.09.09` → `paused`, else `archive`.

## Takeaway for planner

Green path for all three safer wrappers: `Move-Item` / rename of the top-level folder into `archive\yyyy.mm.dd - ShortName`, preserving nested `.git` and opaque `.env` paths. No online requirement for git-strategy FAW on these three. Soft-deferred peers stay untouched (`NextPWATraining` SSH + `.env`; `CursorMobileWorkspace` paused-class).
