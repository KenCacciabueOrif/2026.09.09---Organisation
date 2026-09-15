# Codebase findings — Cycle 18 Multi-experiment (`WorkSpace` only)

**Session:** `sessions/2026.09.15/02-research/`  
**Probe date:** 2026-09-15  
**Method:** Shell `Test-Path`; recursive `dir /s /b` for `.git` and `.env*`; MSYS `git` (`C:\msys64\usr\bin\git.exe`) for `remote -v`, `worktree list`, `status --porcelain`, `branch -vv` (read-only). GfW `Program Files\Git\cmd\git.exe` **absent** on agent — fine for read-only; future mutation still prefer GfW.  
**Secrets:** path presence only — `.env*` contents unread.

---

## Path truth vs INDEX

| Claim | Live | Verdict |
| --- | --- | --- |
| INDEX current path `C:\Project\WorkSpace` | **Exists** (`Test-Path` True) | **verify-only** — still at root; **never re-move** |
| Live `…\TestNewWorkspaceAgent\_backups` | **Absent** | Appendix A still holds |
| Live `…\TestNewWorkspaceAgent\_quarantine` | **Absent** | Appendix A still holds |
| Archive `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_backups` | **Exists** | verify-only |
| Archive `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_quarantine` | **Exists** | verify-only |

**Peers (verify-only — never re-propose as sources):** archived Multi-experiment (`PWAExemple`, `GitTest`, `WorkStationPWA`) and Medium/Early rows — out of this probe’s move map.

---

## Nested `.git` (live WorkSpace)

**Count: 5** (matches Cycle 14–16 baseline)

| # | Path |
| --- | --- |
| 1 | `C:\Project\WorkSpace\OS-IA\.git` |
| 2 | `C:\Project\WorkSpace\TestNewWorkspaceAgent\.git` |
| 3 | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent\.git` |
| 4 | `C:\Project\WorkSpace\TestNewWorkspaceAgent\Projects\Project Atelier IA\Projet Adrien\orchestrateur\.git` |
| 5 | `C:\Project\WorkSpace\TestNewWorkspaceAgent\Projects\Project Atelier IA\Workshop\WorkshopOrif\.git` |

No file-type `.git` worktree links under live WorkSpace. Live `hermes-agent\skills\…\hermes-agent\.git` **absent** (archive hygiene clones may still nest; verify-only).

Top-level children of WorkSpace: **`OS-IA`**, **`TestNewWorkspaceAgent`** only.

---

## Remotes / worktrees / dirty (disclose)

| Root | Remotes | Worktrees | Porcelain lines |
| --- | --- | --- | --- |
| OS-IA | sole `origin` HTTPS `KenCacciabueOrif/Projet-OS-IA` | 1 (main) | **921** |
| TestNewWorkspaceAgent (TNA) | sole `origin` HTTPS `KenCacciabueOrif/TestNewWorkspaceAgent` | 1 | **2307** |
| hermes-agent (live) | sole `origin` HTTPS `NousResearch/hermes-agent` — **`cada` absent** | 1 (main) | **56** |
| orchestrateur | sole `origin` HTTPS `AdWav/orchestrateur` | 1 | **60** |
| WorkshopOrif | sole `origin` HTTPS `C0D3X-25/WorkshopOrif` | 1 | **119** |

**Live multi-remote status:** **CLEARED** — no `cada` regression on live hermes (Cycle 15 clearance holds; Cycle 16 / Cycle 18 confirm).  
**Linked worktrees:** none unexpected (1 each on nested clone paths).  
**Dirty WT:** heavy porcelain on TNA / OS-IA / hermes — **disclose only**; Continuity **Q3=A** → **NO_AUTO_COMMIT**. Nested+parent dirty: do not auto-commit either tree.

### Archive hygiene hermes (verify-only / out of live map)

Under both hygiene parents, hermes clones still show **`origin` + `cada`** (wrong-target HTTPS to TNA). Strategy artifact already classifies these as **Out of map — not mutated** (Cycle 15). Mutating archive remotes is **not** a live WorkSpace clearance advance.

---

## Opaque `.env*` (presence only)

**7 live paths** (matches Cycle 16):

1. `…\hermes-agent\.env.example`
2. `…\hermes-agent\.envrc`
3. `…\orchestrateur\.env`
4. `…\orchestrateur\.env.example`
5. `…\orchestrateur\ui\.env.example`
6. `…\WorkshopOrif\.env`
7. `…\WorkshopOrif\.env.example`

---

## Size (cheap)

- ~**1086 MB** excl `.git`
- ~**716 MB** also excl `node_modules`  
Still **XL** / fail-closed for ordinary whole-tree archive. Shrink ≠ clearance.

---

## False “new” candidates checked (rejected)

| Candidate | Why not a Cycle 18 new gated advance |
| --- | --- |
| Re-isolate `_backups`/`_quarantine` | **Done** Cycle 14; live parents absent |
| Re-remove live hermes `cada` | **Done** Cycle 15; **no regression** |
| `docs_only` re-attest / Continuity A | Anti-loop **forbidden**; **no material delta** vs Cycle 16 |
| Remove `cada` on **archive** hygiene hermes | Strategy **Out of map** / verify-only; not live hazard; invents archive remote-config theater |
| Move/split live primaries #1–#5 or whole `WorkSpace` → archive | Strategy **Keep in place** / **OUT OF SCOPE** until dedicated XL/git-strategy |
| Isolate TNA `_logs` / `_research-cache` / `.hermes` | **No** nested `.git`; not named hazard parents in strategy; weak map to avoid escalate |

---

## Catalogue / program pointers (why they matter)

| Path | Why |
| --- | --- |
| `program/git-strategy-workspace-hazards.md` | Authoritative hazard baseline + post–14/15/16 attestations; safe rules; whole-tree OOS |
| `program/ROADMAP.md` | Multi-experiment **Remaining: WorkSpace only** / not Complete; Next FAW lock hint |
| `catalogue/INDEX.md` | WorkSpace still `C:\Project\WorkSpace`; nested 5; multi-remote Cleared |
| `catalogue/inventory.md` | Cleared multi-remote honesty already (Cycle 16); XL / clearance NO |
| `sessions/2026.09.11/` | Cycle 14 Appendix A execute |
| `sessions/2026.09.11-0859/` | Cycle 15 Option A remote-config |
| `sessions/2026.09.11-1038/` | Cycle 16 docs_only / no material hazard delta |
| `sessions/2026.09.15/01-prompt-betterment/` | Continuity Q1=B→E, Q2=A, Q3=A locks |

---

## Material delta vs strategy / Cycle 16

**None.** Nested **5**; live multi-remote **CLEARED**; Appendix A parents stay archived; whole-tree clearance **NO**; size/env band unchanged. No new named path-move or remote-config step that is both (a) evidence-backed and (b) not already covered/executed/deferred as dedicated XL/git-strategy.
