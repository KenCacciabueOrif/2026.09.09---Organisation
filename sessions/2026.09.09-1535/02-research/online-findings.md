# Online findings — Cycle 4 Medium wrappers (first subset)

Brief citations only — no agent push/pull this cycle; nested-git move hazards are the relevant pattern.

## Citations

1. **git-worktree (official)** — https://git-scm.com/docs/git-worktree  
   Linked worktrees store path metadata; moving a repo with *extra* linked checkouts can break absolute links unless repaired. Live-check showed **no** extra worktrees under any Medium candidate (single main worktree each) → ordinary directory move of the wrapper is appropriate; fail-closed still applies if a re-scan finds `.git/worktrees`.

2. **Git 2.48+ relative worktree paths** — https://github.com/git/git/pull/1783 (and RelNotes referenced from libgit2 discussion)  
   Absolute worktree paths historically break on relocate; relative paths / `worktree repair` mitigate. Reinforces program rule: multi-worktree layouts → dedicated git-strategy, not this Medium first subset.

3. **Prior program Continuity (local)** — `catalogue/taxonomy.md`, Cycle 2–3 sessions  
   CreationTime date labels; wrapper is the dated move unit; nested `.git` moves with the wrapper atomically; 90-day LastWrite → `paused` vs `archive`.

## Takeaway for planner

No online blocker for moving single-nested thin wrappers with `Move-Item`. Soft-prefer HTTPS single-remote S-band folders without linked worktrees for the first Medium batch; defer SSH / optional must-preserve / paused-parent items when safer peers exist.
