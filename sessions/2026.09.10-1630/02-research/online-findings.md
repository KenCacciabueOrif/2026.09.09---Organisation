# Online findings — Cycle 13 Multi-experiment (`WorkSpace` only / continue strategy)

**Session:** `sessions/2026.09.10-1630/02-research/`  
**Purpose:** Brief authoritative notes for **documenting** nested-git / multi-remote hazards — **not** a move plan. Continuity forbids remote URL rewrite and whole-tree archive this cycle.

## Citations

### 1. Git worktrees (linked checkouts of one repo)

- **Title:** Git - git-worktree Documentation  
- **URL:** https://git-scm.com/docs/git-worktree.html  
- **Takeaway:** A repo can have one main worktree plus zero or more **linked** worktrees; metadata lives under `$GIT_DIR/worktrees`. Linked worktrees are a relocation hazard if present — Cycle 13 live re-probe still shows **none** on WorkSpace roots (`worktree list` count = 1 main only). Re-probe before any future approved move remains the safe rule.

### 2. Working with remotes (multiple remotes are normal, not “one URL”)

- **Title:** Git Basics — Working with Remotes (Pro Git)  
- **URL:** https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
- **Takeaway:** A single clone may track **several remotes** (shortnames + URLs); inventory is via `git remote -v`. Multi-remote on live + backup/quarantine hermes (`origin` + `cada`) is a **documented configuration class**, not automatic clearance for whole-tree archive. Document names + schemes; do not treat Continuity path-only as license to rewrite URLs.

### 3. `git remote` management (incl. `set-url`)

- **Title:** Git - git-remote Documentation  
- **URL:** https://git-scm.com/docs/git-remote.html  
- **Takeaway:** `git remote set-url` / `--add` / `--delete` change tracked URLs. For this program’s Continuity (**SSH/HTTPS path-only**), strategy docs should inventory remotes and **avoid** `set-url` unless a later gated strategy step explicitly authorizes it. Cycle 13: document-only; all observed remotes remain HTTPS.

### 4. Nested repositories vs siblings / worktrees (hazard framing)

- **Title:** Two git repositories in one directory? (Codemia knowledge hub)  
- **URL:** https://codemia.io/knowledge-hub/path/two_git_repositories_in_one_directory  
- **Takeaway:** Nested `.git` trees under one parent folder are valid but must be handled as **independent repos** (or submodules/siblings by design). Backup/quarantine hermes clones under `_backups` / `_quarantine` are unexpected extra roots relative to a “clean” single-project tree — supports **named parent isolation** as a future gated option, not silent merge or whole-tree “archive as solved.”

### 5. Windows atomic tree moves (future scoped FS only)

- **Title:** robocopy (Microsoft Learn)  
- **URL:** https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
- **Takeaway:** Continuity Windows lock recovery (`robocopy /E /MOVE` after PermissionDenied/split) remains relevant **only if** a future plan-gated scoped move runs. Not actionable under Cycle 13 `docs_only`.

## Relevance to this cycle

| Online theme | How it informs Cycle 13 docs |
| --- | --- |
| Linked worktrees | Confirm still absent; keep “re-probe before move” in strategy |
| Multi-remote | Keep classifying `origin`+`cada` as live hazard; document ≠ clear |
| `set-url` | Reinforces path-only / no rewrite this cycle |
| Nested roots | Reinforces atomic intact trees + named `_backups`/`_quarantine` parents for **future** Appendix A only |
| robocopy | Future gated FS only — out of Continuity Q1=A |

**No move/execute recommendations from online sources this cycle** — Continuity Q1=A locks `docs_only` continue strategy.
