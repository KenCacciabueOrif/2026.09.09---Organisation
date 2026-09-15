# Codebase findings — Cycle 15 (live hermes multi-remote)

**Session:** `sessions/2026.09.11-0859/02-research/`  
**Probe date:** 2026-09-11  
**Probe tools:** `Test-Path -LiteralPath`; recursive `.git` discovery; Git for Windows `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (helper `manager`) preferred for hermes inventory; PATH also has MSYS git without helper.

---

## INDEX path truth (WorkSpace)

| Path | Test-Path | Notes |
| --- | --- | --- |
| `C:\Project\WorkSpace` | **True** | Matches `catalogue/INDEX.md` current path (still root; **not** archived) |
| `…\TestNewWorkspaceAgent\_backups` (live) | **False** | Appendix A parents did **not** reappear |
| `…\TestNewWorkspaceAgent\_quarantine` (live) | **False** | Same |
| `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_backups` | **True** | Verify-only destination |
| `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_quarantine` | **True** | Verify-only destination |
| Stray `_backups` / `_quarantine` name under live WorkSpace (depth ≤5) | **none** | |

**appendix_a_parents_reappeared:** **no**

---

## Live hermes clone location

| Field | Value |
| --- | --- |
| **hermes_clone_path** | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` |
| `.git` | directory present |
| HEAD | `4fbff573aefc8b792e408f5d177c2c0152c43cb8` (`4fbff573a`) |
| Branch | `main` tracking **`origin/main`** (`ahead 85`) |
| Dirty WT | many modified + untracked (local WIP — disclose only; **Q3=A** defers TNA dirty hygiene; do not expand scope) |

---

## Nested `.git` count (live WorkSpace)

**nested_git_count_live: 5** (matches INDEX / post–Appendix A expectation)

| # | Root path | Remotes (coarse) | Linked worktrees |
| --- | --- | --- | --- |
| 1 | `C:\Project\WorkSpace\OS-IA` | single `origin` HTTPS | 1 (main) |
| 2 | `C:\Project\WorkSpace\TestNewWorkspaceAgent` | single `origin` HTTPS → `…/TestNewWorkspaceAgent.git` | 1 |
| 3 | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` | **`origin` + `cada`** HTTPS | **1** (main only) |
| 4 | `…\Projects\Project Atelier IA\Projet Adrien\orchestrateur` | single `origin` HTTPS | 1 |
| 5 | `…\Projects\Project Atelier IA\Workshop\WorkshopOrif` | single `origin` HTTPS | 1 |

Live primaries **#1–#5** all **present** — keep in place (forbidden to move this cycle).

---

## Remotes evidence — live hermes only

### `git remote -v`

```
cada    https://github.com/KenCacciabueOrif/TestNewWorkspaceAgent.git (fetch)
cada    https://github.com/KenCacciabueOrif/TestNewWorkspaceAgent.git (push)
origin  https://github.com/NousResearch/hermes-agent.git (fetch)
origin  https://github.com/NousResearch/hermes-agent.git (push)
```

### Config / tracking

| Remote | Scheme | URL (org/repo) | Fetch refspec | Local remote-tracking refs | Current branch upstream |
| --- | --- | --- | --- | --- | --- |
| **origin** | HTTPS | `NousResearch/hermes-agent` | `+refs/heads/*:refs/remotes/origin/*` | **1329** | **`main` → `origin/main`** |
| **cada** | HTTPS | `KenCacciabueOrif/TestNewWorkspaceAgent` | `+refs/heads/*:refs/remotes/cada/*` | **3** (`HEAD`, `main`, `hermes-agent-cross-hallucination-fixes`) | **none** |

### Reachability (`git ls-remote --symref … HEAD`)

| Remote | Exit | Result |
| --- | --- | --- |
| origin | **0** | `refs/heads/main` → `b7d353fe…` (network reachable; tip ≠ local `origin/main` cache — normal stale cache) |
| cada | **0** | `refs/heads/main` → `64d81699e…` (network reachable) |

**Conclusion:** neither remote is “dead.” Classification is **active correct upstream (origin)** vs **reachable wrong-target remote (cada)**.

### Relatedness / wrong-target proof

| Check | Result |
| --- | --- |
| `cada` URL == parent TNA `origin` URL | **True** (exact string match) |
| `merge-base` `refs/remotes/cada/main` ↔ `HEAD` | **fails** (no common ancestor in this object DB) |
| `origin/main` ancestor of `HEAD` | **True** (`merge-base --is-ancestor` exit 0) |
| Tree sample `cada/main` | TNA-shaped (e.g. `AgentTemplate.md`, `Projects`, `.github.zip`) |
| Tree sample `HEAD` | hermes-shaped (e.g. `.dockerignore`, `Dockerfile`, `AGENTS.md`, `.env.example`) |
| Local branches tracking `cada` | **none** |

**Naming:** `cada` is **not** a hermes-fork duplicate of `origin`. It is a **cross-repo remote** pointing at the parent `TestNewWorkspaceAgent` GitHub repo, mistakenly configured on the nested hermes clone.

### Linked worktrees (nested clone only)

```
C:/Project/WorkSpace/TestNewWorkspaceAgent/hermes-agent  4fbff573a [main]
```

**Single main worktree** — no linked worktrees; isolation via `worktree add` would **not** remove multi-remote (remotes are per-repo).

---

## Archived hygiene hermes (verify-only)

Both still exist with the same `origin`+`cada` pair (unchanged remotes; path-only Continuity for archives):

| Path | HEAD short | Remotes |
| --- | --- | --- |
| `…\archive\hygiene\2026.09.11 - WorkSpace-_backups\…\hermes-agent` | `8d60d929c` | origin + cada (same URLs as Cycle 14) |
| `…\archive\hygiene\2026.09.11 - WorkSpace-_quarantine\…\hermes-agent` | `8d60d929c` | origin + cada |

**Do not** re-propose archive parents as move sources. Live multi-remote clearance is independent.

---

## Opaque `.env*` (path presence only)

Under live hermes: `.env.example`, `.envrc` (contents unread).  
Under whole live WorkSpace: **7** paths matching `.env*` (count only; contents unread).

---

## Prior art / program links

- Strategy baseline: `program/git-strategy-workspace-hazards.md` (Appendix A done; live multi-remote uncleared)
- ROADMAP: Multi-experiment **Remaining: WorkSpace only**
- Cycle 14: `sessions/2026.09.11/` — nested 7→5; remotes on live hermes left unchanged
- INDEX row: WorkSpace at root; nested **5**; live multi-remote uncleared

---

## Implications for planner (not a plan)

- Clearing the hazard = remove or otherwise retire **`cada`** on **live hermes only**; keep **`origin`** untouched.
- Prefer narrow git remote-config mutation over any path move of primary #3.
- Do not invent whole-tree archive / primary moves / `_backups` re-move.
