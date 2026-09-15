# Online findings — Cycle 19 Continuity X (XL / multi-repo-adjacent relocation)

**Session:** `sessions/2026.09.15-1014/02-research/`  
**Focus:** best practices for relocating nested / multi-repo-adjacent XL trees **without** history rewrite; keep-vs-split framing.  
**Out of scope for this Continuity:** `filter-repo`, force-push, origin URL rewrite (refined prompt forbids).

---

## Citations

### 1. Relocate an ordinary repo by moving the whole directory (history intact)

- **Title:** Change Git repository directory location (community consensus, widely cited)  
- **URL:** https://stackoverflow.com/questions/11384928/change-git-repository-directory-location  
- **Takeaway:** Copy/move the **entire** working tree including `.git`; remotes and history stay valid — no rewrite required. Matches program safe rule “atomic nested git.”

### 2. Moving a git repository (same principle + caveats)

- **Title:** Moving a git repository  
- **URL:** https://stackoverflow.com/questions/7949036/moving-a-git-repository  
- **Takeaway:** For a normal single-worktree repo, relocating the folder is enough; complications arise with **submodules** / absolute links — re-check after move. Reinforces why Continuity probes `worktree list` on **clone paths** before any gated FS move.

### 3. Official — linked worktrees and path moves

- **Title:** Git - git-worktree Documentation  
- **URL:** https://git-scm.com/docs/git-worktree  
- **Takeaway:** Unexpected linked worktrees break naive folder moves; use `git worktree list` before relocate; if a main/linked tree is moved manually, `git worktree repair` may be needed. Live WorkSpace nests currently show **1 worktree each** (main only) — low surprise risk today, still re-probe immediately before STAGE 2 execute.

### 4. Nested multi-repo management (manifest / move without dissolving `.git`)

- **Title:** git-nest docs — move a subproject  
- **URL:** https://github.com/f-steff/git-nest/blob/d0d0d1d0/docs/examples.md  
- **Takeaway:** Mature nested-repo tooling moves a subproject by **filesystem move + manifest update**, keeping the checkout’s full history; remotes are not rewritten by ordinary `move`/`detach`. Useful analogy for WorkSpace: treat each of the 5 roots as an atomic unit; do **not** “inline” (dissolve `.git`) into a parent.

### 5. When history rewrite *is* used (contrast — **do not apply** this cycle)

- **Title:** Splitting a subfolder out into a new repository (GitHub Docs)  
- **URL:** https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository  
- **Takeaway:** `git filter-repo` / subdirectory-filter creates a **new rewritten** history from a folder that was **not** already its own repo. Relevant only if someone later wants to carve history *out of* a single monorepo. **WorkSpace nests already have their own `.git`** — prefer intact relocate; Continuity X explicitly forbids history rewrite / force-push.

### 6. filter-repo operational warnings (why we refuse it here)

- **Title:** How to Split a Git Repository with git filter-repo  
- **URL:** https://how2.sh/posts/how-to-split-git-repositories/  
- **Takeaway:** filter-repo is destructive on the clone it runs against, often drops/repoints remotes, and implies force-push coordination. Wrong tool for “move XL WorkSpace nests as atomic units.”

---

## Synthesis for Continuity X planning

| Practice | Apply to WorkSpace? |
| --- | --- |
| Move directory + `.git` intact | **Yes** — primary relocation pattern for any gated map |
| Re-probe `worktree list` on each nest before move | **Yes** — already in hazard safe rules |
| Remotes path-only (no `set-url`) | **Yes** — Continuity / program lock |
| Use filter-repo / subtree-split to “split” nests | **No** this cycle — nests already independent repos; rewrite forbidden |
| Dissolve nested `.git` into parent (inline) | **No** — destroys atomic units |
| Split decision by ownership / deploy boundary | **Yes (docs)** — OS-IA vs TNA envelope vs inner clones are natural boundaries |
| Dirty WT auto-commit before move | **No** — Q3=A NO_AUTO_COMMIT; disclose only; plan must assume dirty |

**Keep vs split framing (industry-adjacent):** keep projects that share an ownership/workflow envelope together; split only at **existing git-root boundaries**. For WorkSpace that means fate options per atomic unit #1–#5 (and the non-git WorkSpace wrapper folder), not inventing history surgery inside TNA.
