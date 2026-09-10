# Codebase findings — Cycle 8 Multi-experiment (remaining subset)

**Session:** `sessions/2026.09.10-0811/02-research/`  
**Scope:** Live-check **remaining only** — `PWAExemple`, `WorkSpace`.  
**Not sources:** Cycle 7 archives (`GitTest`, `WorkStationPWA`); Medium / Early archive & paused destinations (verify-only).  
**Probe date:** 2026-09-10. Cutoff for 90-day Continuity: **2026-06-12**.  
**Git binary:** `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (probes only; no push/pull).

## INDEX path truth (Test-Path)

| Candidate | INDEX current path | Disk | Verdict |
| --- | --- | --- | --- |
| `PWAExemple` | `C:\Project\PWAExemple` | **present** | Path honest — **move candidate** (green under Continuity) |
| `WorkSpace` | `C:\Project\WorkSpace` | **present** | Path honest — **fail-closed defer** (hazards unchanged vs Cycle 7) |

Neither remaining candidate already lives under `archive` / `paused` / `active` while INDEX shows root → **no verify-only / catalogue-only fix**; both are still at root.

### Cycle 7 peers (verify-only — never re-propose as sources)

| Path | Exists | Role |
| --- | --- | --- |
| `C:\Project\archive\2025.08.08 - GitTest` | **yes** | Cycle 7 archive |
| `C:\Project\GitTest` | **no** | root cleared |
| `C:\Project\archive\2025.07.01 - WorkStationPWA` | **yes** | Cycle 7 archive; SSH origin path-only |
| `C:\Project\WorkStationPWA` | **no** | root cleared |

### Medium / Early siblings (verify-only — never re-propose as sources)

| Path | Exists | Role |
| --- | --- | --- |
| `C:\Project\archive\2025.06.23 - NextPWATraining` | yes | Cycle 6 archive |
| `C:\Project\NextPWATraining` | **no** | root cleared |
| `C:\Project\paused\2026.06.17 - CursorMobileWorkspace` | yes | Cycle 6 paused |
| `C:\Project\CursorMobileWorkspace` | **no** | root cleared |
| `C:\Project\archive\2025.08.12 - ReactRouterTest` | yes | Cycle 4 archive |
| `C:\Project\ReactRouterTest` | **no** | root cleared |
| `C:\Project\archive\2025.06.05 - Simpl` | yes | Cycle 4 archive |
| `C:\Project\Simpl` | **no** | root cleared |

## Destination parents / collisions

| Parent | Exists |
| --- | --- |
| `C:\Project\archive` | yes |
| `C:\Project\paused` | yes |
| `C:\Project\active` | **no** (unused if → archive) |

Proposed dated destinations (CreationTime labels match INDEX proposals) — **all absent** (no collision):

| Proposed dest | Present? |
| --- | --- |
| `archive\2025.06.25 - PWAExemple` | no |
| `paused\2025.06.25 - PWAExemple` | no |
| `active\2025.06.25 - PWAExemple` | no |
| `archive\2026.05.29 - WorkSpace` | no |
| `paused\2026.05.29 - WorkSpace` | no |
| `active\2026.05.29 - WorkSpace` | no |

## 90-day status heuristic (folder LastWriteTime)

| Folder | CreationTime | LastWrite | Days before 2026-09-10 | Heuristic status |
| --- | --- | --- | --- | --- |
| `PWAExemple` | 2025-06-25 | 2025-06-30 | 436 | **archive** |
| `WorkSpace` | 2026-05-29 | 2026-06-10 | 91 | **archive** (1 day past cutoff; not “recent → paused”) |

## Coarse structure + nested `.git` map

All `.git` entries below are **directories** (`Get-Item -Force`), not worktree gitfiles. `git worktree list` → **one main worktree** each (no linked worktrees). Remotes noted for path-only Continuity (**no rewrite**).

### `PWAExemple` — **green** remaining move (recommended this cycle)

- Top children: `PWAExempleAuth`, `PWAExempleNext`, `PWAFrontAuthTest` (no top-level `.git`).
- Nested roots (**3** — INDEX/inventory still say **2**; catalogue drift to fix after move, not a hard abort):

| Nested path | Remotes | Scheme | Worktrees |
| --- | --- | --- | --- |
| `PWAExemple\PWAExempleAuth\PWAExempleAuth\PWAExempleAuth\.git` | `origin` only | HTTPS | 1 (main) |
| `PWAExemple\PWAExempleNext\.git` | `origin` only | HTTPS | 1 (main) |
| `PWAExemple\PWAFrontAuthTest\.git` | `origin` only | **SSH** (`git@github.com:…`) | 1 (main) |

- `.env` path presence (opaque — **paths only**, contents never read):
  - `…\PWAExempleAuth\…\pwa-exemple-auth-app\.env`
  - `…\PWAExempleNext\pwa-test-app\.env`
  - `…\PWAExempleNext\pwa-test-app\.env.local`
  - `…\PWAFrontAuthTest\pwa-front-auth-test-app\.env`
- Inventory size band: **M** (~5 MB)
- Must-preserve draft: **not listed**
- SSH: informational only under Continuity path-only (same as Cycle 6/7) — **not** hard abort
- Hard fail-closed screen: **clean** (ordinary single-remote mains; no linked worktrees; no backup/quarantine extra roots)
- Recommended dest: `C:\Project\archive\2025.06.25 - PWAExemple`

### `WorkSpace` — **fail-closed still** (not cleared)

Hazards **re-confirmed** live (unchanged class vs Cycle 7 research):

- Top children: `OS-IA`, `TestNewWorkspaceAgent`.
- Nested `.git` roots found (**7**, excl. `node_modules`/caches) — still far above inventory “multi-nested (3)” / INDEX “nested (+ deeper)”:

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
- `.env` path presence: many under `TestNewWorkspaceAgent` (`.env`, `.env.example`, `.envrc`, backup/quarantine `.env*` names) — **paths only; never open**.
- Inventory: **XL** (~2308 MB)
- Must-preserve draft: **Medium** (`catalogue/must-preserve.md`) — flag / caution only; Continuity says draft is **not auto-locked**; Q1=A + multi-remote + unexpected extra roots already require **fail-closed skip** without inventing final preserve ratification or a dedicated git-strategy **execution** this cycle.
- **Clearance verdict:** hazards **not** cleared → keep **fail-closed / git-strategy candidate**; default = **defer**, log reason; do **not** force-move.

## Program / catalogue paths that matter

| Path | Why |
| --- | --- |
| `program/ROADMAP.md` | Locked row **Multi-experiment** in progress; Notes must keep remaining names after this batch; **not** Complete while `WorkSpace` (or any name) remains |
| `catalogue/INDEX.md` | Current paths + proposed date labels; update `PWAExemple` after move; fix nested-count note (3 not 2) |
| `catalogue/inventory.md` | Size bands; undercounts `PWAExemple` nesting (2→3) and `WorkSpace` (3→7) |
| `catalogue/must-preserve.md` | Draft — `WorkSpace` listed Medium; flag only |
| `catalogue/taxonomy.md` | archive / paused / active vocabulary |
| `sessions/2026.09.10/02-research/` | Cycle 7 first-subset evidence + WorkSpace fail-closed baseline |
| `sessions/2026.09.10-0811/01-prompt-betterment/` | Q1=A prefer PWAExemple; WorkSpace fail-closed default |

## Org-repo protect

`C:\Project\2026.09.09 - Organisation` — default-protect; not in this batch. Any INDEX/ROADMAP edits stay inside org git root only.

## Do not deep-document

`node_modules`, build caches, and heavy payload trees under WorkSpace / PWA apps — path presence of roots and secrets only.
