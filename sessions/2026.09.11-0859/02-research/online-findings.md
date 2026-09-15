# Online findings — Cycle 15 (multi-remote remediation)

**Session:** `sessions/2026.09.11-0859/02-research/`  
**Scope:** Best practices for removing a wrong/duplicate remote and worktree isolation **without** history rewrite / force-push.

---

## Citations

### 1. Git — `git-remote` documentation

- **Title:** Git - git-remote Documentation  
- **URL:** https://git-scm.com/docs/git-remote  
- **Takeaway:** `git remote remove <name>` (alias `rm`) deletes that remote’s configuration **and** its remote-tracking branches. This is local config/ref cleanup — it does **not** rewrite commit history or force-push. Prefer inventory (`remote -v`, `remote show -n`) before remove. `set-url` changes URLs for an existing name; official note: if fetch and push should differ in purpose, use **two remotes**, not mismatched push/fetch on one name.

### 2. Pro Git — Working with Remotes

- **Title:** Git Basics — Working with Remotes  
- **URL:** https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
- **Takeaway:** Multiple remotes are a normal collaboration pattern when each name points at a **meaningful** related repository. Remotes that are no longer valid (or wrongly added) are removed with `git remote remove`; associated tracking refs go away with the name. Removing a remote does not modify working-tree files or rewrite commits.

### 3. Git — `git-worktree` documentation

- **Title:** Git - git-worktree Documentation  
- **URL:** https://git-scm.com/docs/git-worktree.html  
- **Takeaway:** Linked worktrees share one repository object store and **one remotes configuration**. Adding a worktree isolates a **checkout**, not remotes — it does **not** clear a multi-remote hazard on the same `.git`. Useful for parallel branches; wrong tool for “remove wrong remote.”

### 4. Pro Git — Remote Branches

- **Title:** Git Branching — Remote Branches  
- **URL:** https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches  
- **Takeaway:** Remote-tracking branches are bookmarks updated by fetch; they are not local history rewrites. After removing a remote, those bookmarks under `refs/remotes/<name>/` are gone; local branches and commits remain. Always confirm which remote a branch **tracks** (`branch -vv`) before remove so upstreams are not orphaned unexpectedly.

---

## Practice notes mapped to this cycle

| Pattern | Online guidance | Live hermes application |
| --- | --- | --- |
| Remove wrong remote | Official `remote remove` — config + tracking refs only | `cada` points at **parent TNA repo**, unrelated tree; no branch tracks it → safe candidate for remove |
| Keep correct upstream | Leave `origin` URL/fetch intact | `origin` = NousResearch hermes; `main` tracks `origin/main` |
| Avoid history rewrite | No filter-repo / force-push needed for remote cleanup | Matches Continuity forbids |
| Worktree isolation | Per-checkout only; remotes shared | Does **not** clear multi-remote; optional non-goal |
| set-url redirect | Valid when URL wrong but name should stay | Only if a correct hermes-related URL were known; **no evidence** of a cada hermes-fork URL here |

---

## Non-authoritative / skip

Bare-repo “hub” worktree blog setups (DEV/LinkedIn tooling) are unrelated to clearing a misconfigured second remote on an existing clone; do not invent a bare-hub relocation for this hazard.
