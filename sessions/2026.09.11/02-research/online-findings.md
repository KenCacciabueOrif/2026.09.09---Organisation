# Online findings — Cycle 14 (relocate nested git / quarantine trees)

**Session:** `sessions/2026.09.11/02-research/`  
**Scope:** High-level best practices for relocating nested git repositories and large quarantine/backup trees **without** rewriting remotes or history. No exploit content.

---

## Citations

### 1. Git — Working with Remotes (Pro Git)

- **URL:** https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
- **Takeaway:** Remote shortnames and URLs live in each repository’s own config (`git remote -v`). Relocating a working tree on disk does **not** require changing remotes; inventory remotes after move to confirm URLs unchanged. `git remote set-url` / rename / remove are deliberate config edits — Continuity forbids them unless a later gated step says otherwise.

### 2. Git — `git-remote` documentation

- **URL:** https://git-scm.com/docs/git-remote.html  
- **Takeaway:** Official surface for inspecting and managing remotes. For this cycle: use **read-only** inventory (`remote -v` / `remote show`) before and after path moves; avoid mutate commands (`set-url`, `rm`, `rename`) as part of Appendix A isolation.

### 3. Community consensus — moving a standalone git repository

- **URL:** https://stackoverflow.com/questions/7949036/moving-a-git-repository  
- **Takeaway:** For a normal repo whose `.git` is a **directory** inside the tree, moving the **entire directory** preserves history and remote URLs. No history rewrite needed. Caveat called out online: **submodules** / gitfile-linked worktrees need extra path repairs — not the observed shape here (backup/quarantine hermes clones use directory `.git`).

### 4. Git — `git-mv` / submodule move notes

- **URL:** https://git-scm.com/docs/git-mv  
- **Takeaway:** `git mv` updates superproject index / submodule wiring when renaming **within** a tracked tree. Appendix A is an **OS-level parent-tree relocation out of** the live WorkSpace tree (isolation), not an in-repo submodule rename. Nested clones move as filesystem units; do not treat them as submodule surgery.

### 5. Microsoft Learn — Robocopy

- **URL:** https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
- **Takeaway:** `/E` copies subdirectories including empty ones; `/MOVE` moves files and directories (copy then delete from source). Aligns with strategy rule 6 Windows lock recovery: prefer a single atomic move; on PermissionDenied / split tree → reunify + `robocopy /E /MOVE`; remove only **empty** leftover `.git` shells; re-attest; log deviation. Prefer logging (`/LOG:`) on XL ~1.6 GB trees.

### 6. Git — `git-worktree`

- **URL:** https://git-scm.com/docs/git-worktree.html  
- **Takeaway:** Linked worktrees store extra path bindings. Strategy requires re-running `worktree list` immediately before any approved move; unexpected >1 → fail-closed. Live re-probe (2026-09-11): each hermes tree shows a single main worktree; no `.git/worktrees` dirs.

### 7. Git — Rewriting History (avoid)

- **URL:** https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History  
- **Takeaway:** History rewrite (`filter-branch` / interactive rebase / force-push patterns) is a separate, destructive class of operation. Continuity and strategy rule 1 explicitly forbid history rewrite / `filter-repo` / force-push for Appendix A isolation — path move only.

---

## Practice summary for planner (high-level)

1. **Move intact parent trees** that contain nested `.git` directories; do not strip or relocate `.git` alone.  
2. **Do not rewrite remotes** as part of the move; verify `git remote -v` identical after relocation.  
3. **Do not rewrite history**; filesystem relocation is sufficient for standalone nested repos.  
4. On Windows XL trees, plan **single-move first**, then **robocopy `/E /MOVE` recovery** per strategy artifact.  
5. Re-check **worktrees** immediately before execute.  
6. Expect a **superproject dirty index** if the parent repo tracked files under the moved paths (observed for `TestNewWorkspaceAgent`) — disclose in intent-preview; do not auto-commit/rewrite unless later gated.

---

## Not applicable / out of scope online topics

- Credential/PATH repair chores framed as Continuity requirements  
- Remote migration / hosting cutover guides  
- Force-push or filter-repo “cleanup” recipes
