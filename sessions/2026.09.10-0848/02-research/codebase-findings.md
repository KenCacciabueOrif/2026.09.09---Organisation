# Codebase findings — Cycle 9 Multi-experiment (`WorkSpace` only)

**Session:** `sessions/2026.09.10-0848/02-research/`  
**Scope:** Live-check **only** `C:\Project\WorkSpace`. Verify archived Multi-experiment peers and Medium roots are **not** re-proposed as sources.  
**No moves. No plan. No push/pull.**

## INDEX live path truth

| Name | INDEX current path | Disk | Verdict |
| --- | --- | --- | --- |
| `WorkSpace` | `C:\Project\WorkSpace` | **present** | Path honest — **fail-closed defer** (hazards below) |
| proposed archive | `C:\Project\archive\2026.05.29 - WorkSpace` | **absent** | Destination free if a future cleared/git-strategy cycle proposes it |
| proposed paused / active | `paused\` / `active\` dated WorkSpace | **absent** | No drift |
| `PWAExemple` | `C:\Project\archive\2025.06.25 - PWAExemple` | archive **present**; root **absent** | **verify-only** — never re-propose as source |
| `GitTest` | `C:\Project\archive\2025.08.08 - GitTest` | archive **present**; root **absent** | **verify-only** |
| `WorkStationPWA` | `C:\Project\archive\2025.07.01 - WorkStationPWA` | archive **present**; root **absent** | **verify-only** |

Parents: `C:\Project\archive` **yes**; `C:\Project\paused` **yes**; `C:\Project\active` **no**.

### Medium / Early root sample (must stay closed)

All sampled Medium short-name roots under `C:\Project\` are **absent** (`NextTest`, `Simpl`, `Simpl_Next`, `TestRyan`, `ReactRouterTest`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining`). Do **not** reopen as move sources.

## Status heuristic (90-day)

| Folder | CreationTime | LastWriteTime | Days since LastWrite | Heuristic layout |
| --- | --- | --- | --- | --- |
| `WorkSpace` | 2026-05-29 | 2026-06-10 | 92 | **archive** (cutoff live `2026-06-12`; still past cutoff; not “recent → paused”) |

Date label for any future map: `2026.05.29 - WorkSpace` (matches INDEX proposal).

## Top-level structure

Children under `C:\Project\WorkSpace`:

- `OS-IA`
- `TestNewWorkspaceAgent`

## Nested `.git` roots (7, excl. `node_modules`)

| Nested path | Remotes | Worktrees | Notes |
| --- | --- | --- | --- |
| `OS-IA\.git` | 1× HTTPS `origin` | 1 main | OK shape |
| `TestNewWorkspaceAgent\.git` | 1× HTTPS `origin` | 1 main | OK shape |
| `TestNewWorkspaceAgent\hermes-agent\.git` | **2** (`origin` + `cada`) | 1 main | **messy multi-remote** |
| `…\Projects\…\orchestrateur\.git` | 1× HTTPS | 1 main | deeper project |
| `…\Projects\…\WorkshopOrif\.git` | 1× HTTPS | 1 main | deeper project |
| `…\_backups\…\hermes-agent\.git` | **2** remotes | 1 main | **unexpected extra root** (backup clone) |
| `…\_quarantine\…\hermes-agent\.git` | **2** remotes | 1 main | **unexpected extra root** (quarantine clone) |

Probe binary this session: PATH `C:\msys64\usr\bin\git.exe` (MSYS path display in `worktree list`; counts/remotes still authoritative). Linked worktrees: **none** on all seven roots.

Remote schemes: all HTTPS on this tree — **no SSH `origin` to rewrite**; Continuity SSH path-only still applies if a future cycle touches remotes elsewhere. **Never rewrite** remote URLs.

Inventory/INDEX nested-count drift: inventory still says multi-nested **(3)**; live = **7** — docs fix only; **never invent a re-move**.

## Opaque secrets (path presence only)

`.env` / `.env.*` / `.envrc` path count under WorkSpace (excl. `node_modules`): **17**. Examples of relative path presence only (contents **never** read):

- `TestNewWorkspaceAgent\Projects\…\orchestrateur\.env`
- `TestNewWorkspaceAgent\Projects\…\WorkshopOrif\.env`
- Multiple `.env.example` / `.envrc` / backup-quarantine `.env*` names under `_backups` / `_quarantine` / `hermes-agent`

## Size / preserve flags

- Cheap size this probe: ~**5786 MB** band (**XL**; prior inventory ~2308 MB — still XL; do not deep-walk payload trees).
- `catalogue/must-preserve.md`: **Medium** draft for `C:\Project\WorkSpace` — flag / caution only; **not** auto-locked; Continuity draft wording stands.

## Clearance verdict

Hazards **re-confirmed** (same class as Cycles 7–8):

1. Messy **multi-remote** on live `hermes-agent` (+ backup/quarantine clones).
2. **Unexpected extra roots** under `_backups` / `_quarantine`.
3. **XL** payload + draft must-preserve Medium (caution, not sole gate).
4. Nested complexity (7 roots) above catalogue undercount.

→ Hazards **not cleared** → **fail-closed defer** / git-strategy **candidate for a future opt-in cycle only**. **No green move map** this cycle. **Never force-move.**

## Program / catalogue paths that matter

| Path | Why |
| --- | --- |
| `program/ROADMAP.md` | Locked Multi-experiment **in progress**; Remaining **`WorkSpace` only**; **not** Complete; no Primary-next jump |
| `catalogue/INDEX.md` | Honest root path for WorkSpace; peers already archive |
| `catalogue/inventory.md` | XL band; nested undercount 3→7 |
| `catalogue/must-preserve.md` | Draft Medium — flag only |
| `sessions/2026.09.10/02-research/` | Cycle 7 WorkSpace fail-closed baseline |
| `sessions/2026.09.10-0811/02-research/` | Cycle 8 re-confirm; PWAExemple moved |
| `sessions/2026.09.10-0848/01-prompt-betterment/` | Q1=A research+defer; no git-strategy B |

## Org-repo protect

`C:\Project\2026.09.09 - Organisation` — default-preserve; docs-only edits stay inside org git root.

## Do not deep-document

`node_modules`, build caches, heavy payload under WorkSpace — path presence of roots/secrets only.
