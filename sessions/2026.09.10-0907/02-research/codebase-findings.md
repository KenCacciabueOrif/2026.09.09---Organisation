# Codebase findings — Cycle 10 Multi-experiment (`WorkSpace` only + hazard remediation)

**Session:** `sessions/2026.09.10-0907/02-research/`  
**Scope:** Live re-probe **only** `C:\Project\WorkSpace` for dedicated git-strategy / hazard classification. Verify archived Multi-experiment peers and Medium roots stay **verify-only** (never re-propose as sources).  
**No moves. No plan body. No push/pull. No `.env` content reads. No remote URL rewrite.**

## INDEX live path truth

| Name | INDEX current path | Disk | Verdict |
| --- | --- | --- | --- |
| `WorkSpace` | `C:\Project\WorkSpace` | **present** | Path honest — still at root; hazards classified below |
| proposed archive | `C:\Project\archive\2026.05.29 - WorkSpace` | **absent** | Free for a **future** whole-tree map only if hazards cleared / gated strategy says so — **OUT OF SCOPE** this cycle as ordinary Multi-experiment archive |
| proposed paused / active | dated WorkSpace under `paused\` / `active\` | **absent** | No drift |
| `PWAExemple` | `C:\Project\archive\2025.06.25 - PWAExemple` | archive **present**; root **absent** | **verify-only** — never re-propose |
| `GitTest` | `C:\Project\archive\2025.08.08 - GitTest` | archive **present**; root **absent** | **verify-only** |
| `WorkStationPWA` | `C:\Project\archive\2025.07.01 - WorkStationPWA` | archive **present**; root **absent** | **verify-only** |

Parents: `C:\Project\archive` **yes**; `C:\Project\paused` **yes**; `C:\Project\active` **no**.

### Medium / Early roots (must stay closed)

Sampled Medium short-name roots under `C:\Project\` are **absent** (`NextTest`, `Simpl`, `Simpl_Next`, `TestRyan`, `ReactRouterTest`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining`). Do **not** reopen as move sources.

## Status heuristic (90-day)

| Folder | CreationTime | LastWriteTime | Cutoff live | Heuristic layout |
| --- | --- | --- | --- | --- |
| `WorkSpace` | 2026-05-29 | 2026-06-10 | 2026-06-12 | **archive** (past cutoff; not “recent → paused”) |

Date label if a future whole-tree map ever exists: `2026.05.29 - WorkSpace` (INDEX proposal). **Not** a green map this cycle.

## Top-level structure

Children under `C:\Project\WorkSpace`:

- `OS-IA`
- `TestNewWorkspaceAgent`

No top-level `WorkSpace\.git`.

## Nested `.git` roots (7, excl. `node_modules`) — live re-probe

Probe binary: PATH `C:\msys64\usr\bin\git.exe` (counts/remotes authoritative; worktree paths MSYS-style). Linked `.git` **files**: **none**. Linked worktrees: **none** on all seven roots.

| # | Nested path | Class | Remotes (names + scheme) | Worktrees | HEAD note |
| --- | --- | --- | --- | --- | --- |
| 1 | `OS-IA\.git` | **Primary** project root | `origin` HTTPS | 1 main | OK shape |
| 2 | `TestNewWorkspaceAgent\.git` | **Primary** container root | `origin` HTTPS | 1 main | OK shape |
| 3 | `TestNewWorkspaceAgent\hermes-agent\.git` | **Primary live** hermes-agent | **`origin` + `cada`** HTTPS | 1 main | `4fbff573…` — **messy multi-remote** |
| 4 | `…\Projects\…\orchestrateur\.git` | **Primary** deeper project | `origin` HTTPS | 1 main | OK shape |
| 5 | `…\Projects\…\WorkshopOrif\.git` | **Primary** deeper project | `origin` HTTPS | 1 main | OK shape |
| 6 | `…\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent\.git` | **Backup clone** | **`origin` + `cada`** HTTPS | 1 main | `8d60d929…` — unexpected extra root |
| 7 | `…\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent\.git` | **Quarantine clone** | **`origin` + `cada`** HTTPS | 1 main | `8d60d929…` — same HEAD as backup; unexpected extra root |

**Nested-root count vs prior:** live **7** — unchanged vs Cycle 9; still above older inventory undercount “3” (docs honesty only; never invent a re-move).

### Primary vs backup/quarantine classification

- **Primary (5):** `#1–#5` — live working trees under `OS-IA`, `TestNewWorkspaceAgent`, live `hermes-agent`, `orchestrateur`, `WorkshopOrif`.
- **Backup/quarantine clones (2):** `#6–#7` — labeled folder trees; **not** the live hermes working copy. Backup and quarantine hermes-agent share identical HEAD (`8d60d929…`); live hermes is a **different** HEAD (`4fbff573…`). `merge-base --is-ancestor` (backup → live) **failed** — do **not** treat backup/quarantine as a simple linear ancestor snapshot; treat as **independent clone trees** under backup/quarantine labels.
- **Remote inventory (names only):** across roots, remote **names** seen = `origin`, `cada`. Schemes = **HTTPS only** on this tree (no SSH `origin` to rewrite). **Never rewrite** URLs this cycle.

### `_backups` / `_quarantine` parent trees (named hazard units)

| Tree | Exists | Cheap size band | Contains nested `.git` | Opaque `.env*` paths (subset of total) |
| --- | --- | --- | --- | --- |
| `TestNewWorkspaceAgent\_backups` | yes | ~**1662 MB** | yes (`…\hermes-agent\.git`) | yes (bak / example / envrc) |
| `TestNewWorkspaceAgent\_quarantine` | yes | ~**1662 MB** | yes (`…\hermes-agent\.git`) | yes |

These two **named parent folders** are the natural isolation units (move intact trees), not cherry-picked `.git` shells alone.

## Opaque secrets (path presence only)

`.env` / `.env.*` / `.envrc` path count under WorkSpace (excl. `node_modules`): **17** (unchanged vs Cycle 9). Relative paths present (contents **never** read):

- `TestNewWorkspaceAgent\_backups\.env.20260710-110530.bak`
- `TestNewWorkspaceAgent\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent\.env.example`
- `TestNewWorkspaceAgent\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent\.envrc`
- `TestNewWorkspaceAgent\_backups\2026-07-02_pre-cleanup\hermes-vscode\backups_20260630\.env.20260630_094235`
- `TestNewWorkspaceAgent\_backups\2026-07-02_pre-cleanup\hermes-vscode\backups_20260630\dot_hermes\.env.20260630_094235`
- `TestNewWorkspaceAgent\_quarantine\stale-backups-hermes-home\.env.bak_20260630`
- `TestNewWorkspaceAgent\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent\.env.example`
- `TestNewWorkspaceAgent\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent\.envrc`
- `TestNewWorkspaceAgent\_quarantine\vscode-extension-artifacts\hermes-vscode\backups_20260630\.env.20260630_094235`
- `TestNewWorkspaceAgent\_quarantine\vscode-extension-artifacts\hermes-vscode\backups_20260630\dot_hermes\.env.20260630_094235`
- `TestNewWorkspaceAgent\hermes-agent\.env.example`
- `TestNewWorkspaceAgent\hermes-agent\.envrc`
- `TestNewWorkspaceAgent\Projects\Project Atelier IA\Projet Adrien\orchestrateur\.env`
- `TestNewWorkspaceAgent\Projects\Project Atelier IA\Projet Adrien\orchestrateur\.env.example`
- `TestNewWorkspaceAgent\Projects\Project Atelier IA\Projet Adrien\orchestrateur\ui\.env.example`
- `TestNewWorkspaceAgent\Projects\Project Atelier IA\Workshop\WorkshopOrif\.env`
- `TestNewWorkspaceAgent\Projects\Project Atelier IA\Workshop\WorkshopOrif\.env.example`

## Size / preserve flags

- Cheap size this probe: ~**5786 MB** total (`OS-IA` ~222 + `TestNewWorkspaceAgent` ~5564) → **XL** (same band as Cycle 9).
- `catalogue/must-preserve.md`: **Medium** draft for `C:\Project\WorkSpace` — **draft — not auto-locked / for user review**; caution only, not sole gate.

## Recommended fate (evidence-backed; docs / gated only)

| Target | Recommended fate | Why |
| --- | --- | --- |
| Live primary roots `#1–#5` | **Keep in place** this cycle | Whole-tree archive OOS; live multi-remote still uncleared for ordinary Multi-experiment finalize |
| `_backups` tree (incl. nested hermes clone) | **Isolate** (prefer) / keep / defer — **not delete** by default | Labeled backup; dual-remote clone; opaque `.env*`; ~1.6 GB |
| `_quarantine` tree (incl. nested hermes clone) | **Isolate** (prefer) / keep / defer — **not delete** by default | Labeled quarantine; duplicate HEAD vs backup hermes; dual-remote; opaque `.env*` |
| Whole `C:\Project\WorkSpace` → archive | **OUT OF SCOPE** | Never propose ordinary Multi-experiment whole-tree archive as “solved” |

## Clearance / remediation verdict

| Hazard | Live status | Whole-tree archive? | Scoped named isolation? |
| --- | --- | --- | --- |
| Multi-remote live `hermes-agent` (`origin`/`cada`) | **Present** | Blocks ordinary whole-tree | Remains after isolating backups |
| Backup/quarantine extra roots | **Present** (classified) | Blocks “clean” whole-tree | **Research-supported** optional scoped map |
| Nested count 7 / XL / draft Medium | **Present** | Caution | Isolation reduces roots 7→5 and ~3.3 GB if both parent trees move |
| Linked worktrees | **None** | N/A | N/A |

→ Hazards **not cleared for whole-tree**. Cycle goal = **classify + safe rules** (`docs_only` default). Optional **scoped** isolation of named `_backups` / `_quarantine` trees is **research-supported** for planner draft **only after plan gate** — does **not** mark Multi-experiment Complete.

## Program / catalogue paths that matter

| Path | Why |
| --- | --- |
| `program/ROADMAP.md` | Lock Multi-experiment **in progress**; Remaining **`WorkSpace` only**; **not** Complete; no Primary-next jump |
| `catalogue/INDEX.md` | Honest root path; peers archive; nested-count honesty |
| `catalogue/must-preserve.md` | Draft Medium — flag only |
| `sessions/2026.09.10-0848/02-research/` | Cycle 9 defer baseline (same hazard classes) |
| `sessions/2026.09.10-0907/01-prompt-betterment/` | Q1=A remediation; Q2=A docs-first + optional scoped map |

## Org-repo protect

`C:\Project\2026.09.09 - Organisation` — default-preserve; session docs stay inside org git root.

## Do not deep-document

`node_modules`, build caches, heavy payloads — root/remote/secret **path presence** only.
