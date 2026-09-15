# Online findings — Cycle 18 Multi-experiment (`WorkSpace` only)

**Session:** `sessions/2026.09.15/02-research/`  
**Scope:** Authoritative Git remote / nested-repo references supporting anti-loop escalate (no inventing weak remote-config or whole-tree merge theater).

---

## Citations

### 1. Git — `git remote remove` / `rm`

- **Title:** Git - git-remote Documentation  
- **URL:** https://git-scm.com/docs/git-remote  
- **Takeaway:** `git remote remove <name>` (alias `rm`) deletes the remote’s config and remote-tracking branches only — does not delete the server repo. Cycle 15 Option A already applied this to live hermes `cada`; re-running without regression is not a new advance.

### 2. Pro Git — Working with Remotes

- **Title:** Git Basics — Working with Remotes  
- **URL:** https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
- **Takeaway:** Removing a unused/wrong remote is a normal local bookkeeping step. Archive hygiene clones still carrying `cada` are **historical** trees — mutating them is optional archive hygiene, not clearance of live WorkSpace multi-remote (already CLEARED).

### 3. GitHub Docs — Managing remote repositories

- **Title:** Managing remote repositories  
- **URL:** https://docs.github.com/en/get-started/git-basics/managing-remote-repositories  
- **Takeaway:** `git remote rm` unlinks local remote config only. Confirms Cycle 15 was the correct narrow remote-config pattern; no further live `rm` is indicated without regression.

### 4. Nested repositories — parent cannot absorb nested `.git` as ordinary content

- **Title:** Question — `.git` subdirectories (git mailing list)  
- **URL:** http://public-inbox.org/git/20191031202015.u5l3wzvn64zypnad@camp.crustytoothpaste.net/T/  
- **Takeaway:** Git does not treat nested `.git` trees as ordinary tracked content of a parent without submodules/other strategies. Supports program law: nested roots stay **atomic**; do not invent merge/filter-repo whole-tree “archive” under ordinary Continuity.

### 5. Monorepo migration (contrast — out of scope here)

- **Title:** Migrating Git from multirepo to monorepo without losing history (Netlify)  
- **URL:** https://developers.netlify.com/guides/migrating-git-from-multirepo-to-monorepo-without-losing-history/  
- **Takeaway:** True history-preserving colocation uses `filter-repo` / unrelated-history merges — heavyweight and **explicitly out of FAW ordinary Continuity** (no history rewrite). Reinforces escalate → dedicated XL/git-strategy Continuity rather than inventing a Cycle 18 path move of live primaries.

---

## Relevance to Cycle 18 verdict

Online sources do **not** invent a new narrow WorkSpace step beyond what `program/git-strategy-workspace-hazards.md` already covers (Appendix A isolation done; live multi-remote remove done; whole-tree blocked until dedicated strategy). They support **honest escalate** when residual work is XL / program-gated, not another docs_only re-attest or archive-remote theater.
