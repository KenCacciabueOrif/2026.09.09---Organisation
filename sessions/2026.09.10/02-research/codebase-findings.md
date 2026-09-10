# Codebase findings — Cycle 7 Multi-experiment (first subset)

**Session:** `sessions/2026.09.10/02-research/`  
**Scope:** Live-check only Multi-experiment candidates `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace`.  
**Not sources:** Medium / Early archive & paused destinations (verify-only).  
**Probe date:** 2026-09-10. Cutoff for 90-day Continuity: **2026-06-12**.

## INDEX path truth (Test-Path)

| Candidate | INDEX current path | Disk | Verdict |
| --- | --- | --- | --- |
| `PWAExemple` | `C:\Project\PWAExemple` | **present** | Path honest — **move candidate** (not verify-only) |
| `GitTest` | `C:\Project\GitTest` | **present** | Path honest — **move candidate** |
| `WorkStationPWA` | `C:\Project\WorkStationPWA` | **present** | Path honest — **move candidate** |
| `WorkSpace` | `C:\Project\WorkSpace` | **present** | Path honest — but **fail-closed defer** (hazards below) |

No candidate already lives under `archive` / `paused` / `active` with INDEX still showing root → **no verify-only / catalogue-only fix** among the four. Do **not** re-move Medium/Early destinations.

### Medium / Early siblings (verify-only — never re-propose as sources)

| Path | Exists | Role |
| --- | --- | --- |
| `C:\Project\archive\2025.07.04 - PWAExempleTristan` | yes | Cycle 5 archive |
| `C:\Project\PWAExempleTristan` | **no** | root cleared |
| `C:\Project\archive\2025.06.23 - NextPWATraining` | yes | Cycle 6 archive |
| `C:\Project\NextPWATraining` | **no** | root cleared |
| `C:\Project\paused\2026.06.17 - CursorMobileWorkspace` | yes | Cycle 6 paused |
| `C:\Project\CursorMobileWorkspace` | **no** | root cleared |

**Name collision note (informational):** `GitTest\NextTest` is a nested folder under the Multi-experiment wrapper; archived Medium `NextTest` is a **different** tree at `archive\2025.06.23 - NextTest`. Do not reopen the archive as a source.

## Destination parents / collisions

| Parent | Exists |
| --- | --- |
| `C:\Project\archive` | yes |
| `C:\Project\paused` | yes |
| `C:\Project\active` | **no** (unused this cycle if all → archive) |

Proposed dated destinations (CreationTime labels match INDEX proposals) — **all absent** (no collision):

| Proposed dest | Present? |
| --- | --- |
| `archive\2025.06.25 - PWAExemple` | no |
| `archive\2025.08.08 - GitTest` | no |
| `archive\2025.07.01 - WorkStationPWA` | no |
| `archive\2026.05.29 - WorkSpace` | no |

Same names under `paused` / `active` also absent.

## 90-day status heuristic (folder LastWriteTime)

| Folder | CreationTime | LastWrite | Days before 2026-09-10 | Heuristic status |
| --- | --- | --- | --- | --- |
| `PWAExemple` | 2025-06-25 | 2025-06-30 | 436 | **archive** |
| `GitTest` | 2025-08-08 | 2025-08-08 | 397 | **archive** |
| `WorkStationPWA` | 2025-07-01 | 2025-08-12 | 393 | **archive** |
| `WorkSpace` | 2026-05-29 | 2026-06-10 | 91 | **archive** (1 day past cutoff; not “recent → paused”) |

## Coarse structure + nested `.git` map

All `.git` entries below are **directories** (`Get-Item -Force`), not worktree gitfiles. `git worktree list` → **one main worktree** each (no linked worktrees). Remotes noted for path-only Continuity (**no rewrite**).

### `GitTest` — lower-risk peer (recommended subset)

- Top children: `NextTest`, `test` (no top-level `.git`).
- Nested roots (**2** — matches INDEX “2 nested”):

| Nested path | Remotes | Scheme | Worktrees |
| --- | --- | --- | --- |
| `GitTest\NextTest\.git` | `origin` only | HTTPS | 1 (main) |
| `GitTest\test\.git` | `origin` only | HTTPS | 1 (main) |

- `.env` path presence: **none**
- Inventory size band: **S** (~0.29 MB)
- Must-preserve draft: **not listed**
- Hard fail-closed screen: **clean**

### `WorkStationPWA` — lower-risk peer (recommended subset)

- Top children: `WorkStationPWA`, `WorkStationRouterPWA`, `favicon_io(3)` (+ zip) — coarse only.
- Nested roots (**2** — matches INDEX “nested”):

| Nested path | Remotes | Scheme | Worktrees |
| --- | --- | --- | --- |
| `WorkStationPWA\WorkStationPWA\.git` | `origin` only | HTTPS | 1 (main) |
| `WorkStationPWA\WorkStationRouterPWA\workstation-app\.git` | `origin` only | **SSH** (`git@github.com:…`) | 1 (main) |

- `.env` path presence: **none**
- Inventory size band: **S** (~0.62 MB)
- Must-preserve draft: **not listed**
- SSH: informational only under Q3=A path-only (same Continuity as Cycle 6 NextPWA — not hard abort)
- Hard fail-closed screen: **clean**

### `PWAExemple` — remaining (later Multi-experiment sub-batch; not fail-closed)

- Top children: `PWAExempleAuth`, `PWAExempleNext`, `PWAFrontAuthTest`.
- Nested roots (**3** — INDEX/inventory previously said **2**; live scan found third):

| Nested path | Remotes | Scheme | Worktrees |
| --- | --- | --- | --- |
| `PWAExemple\PWAExempleAuth\PWAExempleAuth\PWAExempleAuth\.git` | `origin` only | HTTPS | 1 |
| `PWAExemple\PWAExempleNext\.git` | `origin` only | HTTPS | 1 |
| `PWAExemple\PWAFrontAuthTest\.git` | `origin` only | **SSH** | 1 |

- `.env` path presence (opaque — **paths only**, contents never read):
  - `…\PWAExempleAuth\…\pwa-exemple-auth-app\.env`
  - `…\PWAExempleNext\pwa-test-app\.env`
  - `…\PWAExempleNext\pwa-test-app\.env.local`
  - `…\PWAFrontAuthTest\pwa-front-auth-test-app\.env`
- Inventory size band: **M** (~5 MB)
- Not on must-preserve draft
- Why not first-subset: higher nested count than INDEX, multiple opaque `.env`, one SSH — still **movable** under Continuity, but not the lowest-risk 1–2 peers while cleaner peers exist
- Hard fail-closed: **no** (roots are ordinary single-remote mains; INDEX undercount is catalogue drift to fix after move, not “unexpected backup/quarantine roots”)

### `WorkSpace` — **fail-closed defer** this cycle

- Top children: `OS-IA`, `TestNewWorkspaceAgent` (coarse).
- Nested `.git` roots found (**7**, excl. `node_modules`/caches) — far above inventory “multi-nested (3)” / INDEX “nested (+ deeper)”:

| Nested path | Remotes | Notes |
| --- | --- | --- |
| `OS-IA\.git` | 1× HTTPS `origin` | OK shape |
| `TestNewWorkspaceAgent\.git` | 1× HTTPS `origin` | OK shape |
| `TestNewWorkspaceAgent\hermes-agent\.git` | **2** (`origin` + `cada`) | **messy multi-remote** |
| `…\Projects\…\orchestrateur\.git` | 1× HTTPS | deeper project |
| `…\Projects\…\WorkshopOrif\.git` | 1× HTTPS | deeper project |
| `…\_backups\…\hermes-agent\.git` | **2** remotes | **unexpected extra root** (backup copy) |
| `…\_quarantine\…\hermes-agent\.git` | **2** remotes | **unexpected extra root** (quarantine copy) |

- Linked worktrees: none on probed roots (each shows 1 main worktree).
- `.env` path presence: many under `TestNewWorkspaceAgent` (including `.env`, `.env.example`, `.envrc`, backup/quarantine `.env*` names) — **paths only; never open**.
- Inventory: **XL** (~2308 MB)
- Must-preserve draft: **Medium** priority (`catalogue/must-preserve.md`) — **flag collision / caution**; Continuity says draft is **not auto-locked** and do not re-block solely to re-litigate, but Q2=A multi-remote + unexpected extra roots already require **fail-closed skip** this cycle without inventing final preserve ratification.
- Hard fail-closed reasons: **messy multi-remote** (`hermes-agent` + backup/quarantine clones) + **unexpected extra roots** under `_backups` / `_quarantine` + XL blast radius. Dedicated **git-strategy** may be appropriate later; **do not** rewrite remotes or force-move here.

## Program / catalogue paths that matter

| Path | Why |
| --- | --- |
| `program/ROADMAP.md` | Locked row **Primary next → Multi-experiment**; Notes must list remaining names after subset |
| `catalogue/INDEX.md` | Current paths + proposed date labels; update after moves; fix nested-count notes |
| `catalogue/inventory.md` | Size bands / wrapper class; undercounts WorkSpace & PWAExemple nesting |
| `catalogue/must-preserve.md` | Draft — WorkSpace listed Medium; flag only |
| `catalogue/taxonomy.md` | archive / paused / active vocabulary |
| `sessions/2026.09.09-1612/` | Prior Medium Complete Continuity (SSH path-only, opaque `.env`, 90-day) |
| `sessions/2026.09.10/01-prompt-betterment/` | Q1–Q4 Choose-all locks |

## Org-repo protect

`C:\Project\2026.09.09 - Organisation` — default-protect; not in this batch. Any INDEX/ROADMAP edits stay inside org git root only.

## Do not deep-document

`node_modules`, build caches, and heavy payload trees under WorkSpace / PWA apps — path presence of roots and secrets only.
