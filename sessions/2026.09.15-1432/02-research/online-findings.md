# Online findings — Cycle 23 (WorkSpace / #4)

**Session:** `sessions/2026.09.15-1432/02-research/`  
**Scope:** Confirm ignored-nested-clone vs submodule practice for TNA parent-surgery approval framing. Prefer official / widely cited sources.

---

## Citations

### 1. Nested repos via `.gitignore` (not submodules)

- **Title:** Nested repos · Taffer.ca  
- **URL:** https://taffer.ca/posts/2024/nested-repos/  
- **Takeaway:** A common pattern is to clone a second repo inside a parent and append it to `.gitignore` so both stay ordinary independent repos (no submodule commands). Matches TNA’s “Nested git repositories (cloned projects — tracked separately)” model — extract is an OS/path move of an intact clone, not submodule teardown.

### 2. Nested folders: submodules vs ignore vs subtree (community)

- **Title:** Nested folder structure with multiple git repos: submodules, subtrees or .gitignore?  
- **URL:** https://stackoverflow.com/questions/75425606/nested-folder-structure-with-multiple-git-repos-submodules-subtrees-or-gitignore  
- **Takeaway:** When parent need not pin child commits, gitignored nested repos are used in practice; parent often stays “dirty” / non-reproducible for the nest — aligns with **NO_AUTO_COMMIT** on dirty TNA and no invented `.gitmodules` surgery.

### 3. Official submodule docs (contrast — what we are *not* doing)

- **Title:** Git - git-submodule Documentation  
- **URL:** https://git-scm.com/docs/git-submodule  
- **Takeaway:** Submodules require `.gitmodules`, gitlink commits, and commands such as `absorbgitdirs`. Live probe found **no** `.gitmodules` and `check-ignore` hits — fail-closed if a nest suddenly looks like a submodule; do not invent submodule procedure for ignored clones.

### 4. Subtree alternative (out of scope for this cycle)

- **Title:** Git Subtree: Alternative to Git Submodule \| Atlassian  
- **URL:** https://www.atlassian.com/git/tutorials/git-subtree  
- **Takeaway:** Subtree merges history into the parent — Continuity forbids history rewrite / dissolve into parent. Reinforces **intact nested-git relocate** (path-only remotes) as the correct extract model.

### 5. Worktree probe hygiene (carried from prior cycles)

- **Title:** Git - git-worktree Documentation  
- **URL:** https://git-scm.com/docs/git-worktree  
- **Takeaway:** Linked worktrees must be listed on the **nested clone path** (directory owning that `.git`). Parent-wrapper probes can resolve to the outer repo — surgery preflight already encodes this; re-probe before any approved move.

---

## Implication for Cycle 23

Online evidence does **not** invent a new surgery procedure (Cycle 20 already wrote it). It supports treating nests as **ignored clones**: #4 **approval** for a named intact `path_batch` is the next material gate; submodule/subtree tooling remains out of map unless live evidence changes.
