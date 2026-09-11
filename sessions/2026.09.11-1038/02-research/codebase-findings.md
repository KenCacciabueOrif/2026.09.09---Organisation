# Codebase findings — Cycle 16 (WorkSpace / continue-strategy)

**Session:** `sessions/2026.09.11-1038/02-research/`  
**Continuity:** Q1=**A** `docs_only` continue-strategy from [`program/git-strategy-workspace-hazards.md`](../../../program/git-strategy-workspace-hazards.md)  
**Probe time:** 2026-09-11 (agent Shell — **succeeded**; not blocked/empty)  
**Git binary used:** `C:\msys64\usr\bin\git.exe` (PATH default). **Git for Windows** `C:\Program Files\Git\cmd\git.exe` **absent** on this agent — remotes are read-only inventory only this cycle.

---

## Strategy artifact (must-point)

| Path | Role |
| --- | --- |
| [`program/git-strategy-workspace-hazards.md`](../../../program/git-strategy-workspace-hazards.md) | **EXISTS** — Continuity baseline. Cycle 15 section: live multi-remote **CLEARED**; whole-tree clearance still **NO**; nested **5**. Re-probe deltas only — do not re-litigate classification from scratch. |
| Prior Cycle 15 research | [`sessions/2026.09.11-0859/02-research/`](../../2026.09.11-0859/02-research/) |
| Prior Appendix A | [`sessions/2026.09.11/`](../../2026.09.11/) |

---

## INDEX path truth (WorkSpace)

| Check | Result | Method |
| --- | --- | --- |
| INDEX current path | `C:\Project\WorkSpace` | Read `catalogue/INDEX.md` row |
| Disk presence | **True** (directory) | `Test-Path -LiteralPath` |
| Under `archive` / `paused` / `active` as whole-tree destination | **False** (no dated whole-tree archive leaf) | `Test-Path` on sample archive/paused/active paths |
| Verdict | **verify-only / catalogue honesty** — tree already at INDEX dest (root). **Never re-move.** | — |

INDEX Notes already record Cycle 14 Appendix A + Cycle 15 sole-`origin` clearance and “not Complete”. **No path-move drift.**

---

## Live nested `.git` count

**Method:** `Get-ChildItem -Recurse -Force -Filter '.git'` under `C:\Project\WorkSpace`, excluding `node_modules` / `.cache` / `__pycache__`.

| # | Live nested root |
| --- | --- |
| 1 | `C:\Project\WorkSpace\OS-IA\.git` |
| 2 | `C:\Project\WorkSpace\TestNewWorkspaceAgent\.git` |
| 3 | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent\.git` |
| 4 | `…\Projects\Project Atelier IA\Projet Adrien\orchestrateur\.git` |
| 5 | `…\Projects\Project Atelier IA\Workshop\WorkshopOrif\.git` |

**nested_live_count:** **5** (matches post–Appendix A / Cycle 15 baseline).

---

## Appendix A parents (verify-only — do not re-propose)

| Path | Live under WorkSpace? | Hygiene dest present? |
| --- | --- | --- |
| `…\TestNewWorkspaceAgent\_backups` | **False** | `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_backups` **True** (1 nested `.git`) |
| `…\TestNewWorkspaceAgent\_quarantine` | **False** | `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_quarantine` **True** (1 nested `.git`) |

**No reappearance** under live WorkSpace → **no** Appendix A re-proposal.

---

## Remote state (live roots)

**Method:** `git -C <root> remote -v` (MSYS binary).

| Root | Remotes | Notes |
| --- | --- | --- |
| **hermes-agent** (live) | **sole `origin`** → `https://github.com/NousResearch/hermes-agent.git` | **No `cada`** — **no multi-remote regression** vs Cycle 15 |
| TestNewWorkspaceAgent | sole `origin` HTTPS (`KenCacciabueOrif/TestNewWorkspaceAgent`) | — |
| OS-IA | sole `origin` HTTPS | — |
| orchestrateur | sole `origin` HTTPS | — |
| WorkshopOrif | sole `origin` HTTPS | — |

**multi_remote_status (live hermes):** **CLEARED** (sole `origin`; expect matched).

**Linked worktrees (hermes):** single main worktree only (`worktree list` → one entry; HEAD `4fbff573a`).

**Dirty WT (hermes):** porcelain **56** lines — disclose only; **NO_AUTO_COMMIT** (Q3=A). Parent TNA not force-hygiened.

Archived hygiene hermes remotes: **out of map** (verify-only; may still carry historical `cada` — not probed deeply; not mutated).

---

## Whole-tree / XL clearance

| Field | Evidence |
| --- | --- |
| **clearance_whole_tree** | **NO** |
| Why | Continuity A forbids inventing whole-tree archive; XL tree still at root; program gates (must-preserve draft Medium caution; taxonomy proposed-ratified ≠ final) remain |
| Size band (Cycle 16 cheap) | ~**1086 MB** excl `.git` objects (~**716 MB** also excl `node_modules`) — post–Appendix A shrink vs pre-isolation ~5.7 GB band; **still treat as XL / fail-closed** for ordinary Multi-experiment archive |
| Inventory historical size | `catalogue/inventory.md` still shows **2308.43 MB** (pre–Appendix A era band) — honesty optional refresh, not a clearance flip |

---

## Opaque `.env*` (path presence only)

**Method:** recurse `Filter '.env*'`, skip `node_modules`/caches; **contents unread**.

**Live count:** **7** paths (names only):

- `…\hermes-agent\.env.example`, `.envrc`
- `…\orchestrateur\.env`, `.env.example`, `ui\.env.example`
- `…\WorkshopOrif\.env`, `.env.example`

Strategy hazard table still cites **17** (Cycle 10 era, including `_backups`/`_quarantine`). **Honesty delta:** live opaque count **7** after Appendix A isolation.

---

## Coarse corpus map (WorkSpace)

**Top-level:** `OS-IA/`, `TestNewWorkspaceAgent/` only.

**TNA top-level (non-deep):** `hermes-agent`, `Projects`, `docs`, `scripts`, caches (`_research-cache`, `.pytest_cache`, `.hermes`), workflow dirs — **no** live `_backups` / `_quarantine`.

**Git roots:** five listed above — treat atomic. Do **not** deep-document `node_modules` / caches.

**Archived Multi-experiment peers (verify-only — never re-propose as sources):**

- `C:\Project\archive\2025.08.08 - GitTest` — present  
- `C:\Project\archive\2025.07.01 - WorkStationPWA` — present  
- `C:\Project\archive\2025.06.25 - PWAExemple` — present  

---

## Catalogue / ROADMAP honesty vs Cycle 15

| Artifact | Cycle 15 accuracy | Cycle 16 delta? |
| --- | --- | --- |
| `program/git-strategy-workspace-hazards.md` | Cycle 15 clearance recorded; clearance **NO** | Add **Cycle 16 re-probe attestation** (hazard state: **no material delta**); optional env-count / size-band honesty |
| `catalogue/INDEX.md` | Path + nested 5 + multi-remote cleared + not Complete | **No material path/status delta**; optional Cycle 16 re-probe footnote |
| `catalogue/inventory.md` | Nested 5 / Appendix A noted | **Material stale:** Notes still say **“live multi-remote uncleared”** — must flip to Cleared (Cycle 15; confirmed Cycle 16) |
| `program/ROADMAP.md` | Remaining WorkSpace only / not Complete | Keep; optional Cycle 16 docs_only note — **never** Complete / Primary next |

---

## Fail-closed reminders (evidence)

- No whole-tree archive map invented.  
- No Appendix A re-proposal (parents isolated + absent live).  
- No Primary next / Multi-experiment Complete.  
- Zero corpus path moves / remote-config this cycle (`docs_only`).
