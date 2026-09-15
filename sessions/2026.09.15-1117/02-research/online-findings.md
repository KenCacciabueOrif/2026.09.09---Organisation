# Online findings — Cycle 20 (nested git / parent-surgery adjacent)

**Session:** `sessions/2026.09.15-1117/02-research/`  
**Focus:** best practices for moving **independent nested clones** out of a **dirty parent** working tree without history rewrite; contrast submodule workflows (TNA nests are **gitignored**, not submodules).

---

## Citations

### 1. Git worktree — list / move / repair (official)

- **Title:** Git - git-worktree Documentation  
- **URL:** https://git-scm.com/docs/git-worktree.html  
- **Takeaway:** Always inspect with `git worktree list` before relocating a repo. Main worktree moves are OS-level; if linked worktrees exist, use `git worktree repair` after manual move. `git worktree move` does **not** move the main worktree. Matches program rule: probe **nested clone path** only, fail-closed on unexpected >1 worktree.

### 2. Nested repo inside parent without submodules (gitignore pattern)

- **Title:** Maintain git repo inside another git repo (Codemia synthesis of common practice)  
- **URL:** https://codemia.io/knowledge_hub/path/maintain_git_repo_inside_another_git_repo  
- **Takeaway:** Three deliberate models: ignored nested repo, submodule, or subtree. For **ignored nested** clones, histories stay separate; outer repo does not track inner content. Relocating the inner tree is a filesystem concern for the parent, not a submodule metadata edit — aligns with TNA’s `.gitignore` design.

### 3. Gitignore nested repository (when nest should not be persisted in parent)

- **Title:** How to gitignore a nested repository?  
- **URL:** https://stackoverflow.com/questions/79623198/how-to-gitignore-a-nested-repository  
- **Takeaway:** If the nested clone must remain independent and not tracked by the parent, ignore the **entire directory**. Parent then does not descend into it; removing/moving that directory is not a normal tracked deletion. Reinforces: TNA parent-surgery ≠ `git submodule deinit`.

### 4. Submodule move-out (contrast only — do not apply blindly)

- **Title:** Git submodule: Move submodule outside repository  
- **URL:** https://stackoverflow.com/questions/15087047/git-submodule-move-submodule-outside-repository  
- **Takeaway:** Submodule extraction needs `.gitmodules` / `.git/modules` / gitdir pointer surgery. **Out of scope for TNA nests** (no `.gitmodules`). Keep as negative checklist: if future nests ever become submodules, surgery class changes.

### 5. History-preserving relocate of a whole repo tree

- **Title:** (General practice; also Cycle 19 online) — move/copy entire working tree including `.git`  
- **URL:** https://git-scm.com/docs/git.html (repository = working tree + `.git`; no rewrite for plain relocate)  
- **Takeaway:** Intact relocate of a directory that contains `.git` preserves remotes and history; **do not** strip `.git`, `filter-repo`, or force-push. Matches program “atomic nested git” safe rule.

### 6. Nested repos without submodules — independence

- **Title:** Nested git repositories without submodules?  
- **URL:** https://stackoverflow.com/questions/2317652/nested-git-repositories-without-submodules  
- **Takeaway:** Parent and nested histories stay separate by design; do not invent merge/inline of nest into parent. Prefer keeping each `.git` atomic when the goal is split/extract.

---

## Synthesis for Continuity X parent-surgery policy

| Practice | Apply to TNA? |
| --- | --- |
| `git worktree list` on **each nest path** immediately before move | **Yes** — mandatory |
| Intact OS move of nest including `.git` | **Yes** — atomic root |
| Remotes path-only / no URL rewrite | **Yes** — program Continuity |
| No history rewrite / no dissolve `.git` into parent | **Yes** |
| Submodule deinit / `.git/modules` edit | **No** — nests are gitignored, not submodules |
| Auto-commit / stash-clean dirty parent to “make room” | **No** — Q3=A **NO_AUTO_COMMIT** |
| Treat parent porcelain change as optional hygiene, not blocker for nest extract when nests are ignored | **Yes** — document; still disclose dirty TNA |
| Absolute-path inventory (IDE, scripts, mounts) after move | **Yes** — non-git breakage risk |

**Anti-pattern to forbid in policy docs:** rewriting nest history to “fit” parent; registering nests as submodules solely to move them; claiming whole-tree clearance from writing the policy alone (criterion #4 is necessary but not sufficient — #1–#6 all required).
