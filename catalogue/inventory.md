# Coarse inventory — C:\Project

**Source:** Cycle 0 baseline + Cycle 1 deepen from `sessions/2026.09.09-1009/02-research/codebase-findings.md`  
**Scan date:** 2026-09-09  
**Method:** top-level listing + **cheap size bands** + nested `.git` discovery. Cycle 2 moved three Early/simple folders under `archive` / `paused` (see path notes below).  
**Secrets:** path presence only — contents not read.  
**Date labels:** **CreationTime wins** for proposed `yyyy.mm.dd` prefixes (see [`taxonomy.md`](taxonomy.md)); LastWrite = activity / next only.

## Scan limits

| Limit | Value |
| --- | --- |
| Top-level only for bands / timestamps | Yes — one row per `C:\Project` child |
| Git discovery depth | **0–2** under each top-level; skip named cache/dep dirs when walking |
| Size metric | **Cheap payload** — file-byte sum **excluding** `node_modules`, `.git`, `.next`, `dist`, `build`, `coverage`, `.cache`, `.pytest_cache`, `__pycache__`, `.turbo`, `.vercel` (understates true on-disk size when deps/git dominate) |
| Size band cutoffs | **S** &lt; 1 MB · **M** 1–&lt;50 MB · **L** 50–&lt;500 MB · **XL** ≥ 500 MB |
| Deep `node_modules` / cache inventory | **Skipped** (root orphan `node_modules` presence only) |
| Secret contents | **Not read** |
| Git-root count | Treat **32** as a **lower bound**. Re-scan the target folder at the start of any later move cycle. |

## Corpus summary

| Signal | Value |
| --- | --- |
| `C:\Project` itself a git root? | **No** |
| Top-level entries | **28** (24 dirs + 4 files) after Cycle 2 — three moved under `archive`/`paused`; parents `archive`/`paused` added |
| Creation-year mix (top-level) | **2025: 24**, **2026: 5** |
| Size-band mix (cheap) | **S=17**, **M=9**, **L=1** (`ProjetOrif`), **XL=2** (`WorkSpace`, `Obsidian`) |
| LastWrite activity (newest → older notable) | Org repo (2026-09-09) → ZedTest → CursorMobileWorkspace → WorkSpace → Obsidian → ProjetOrif → WebCatalogue → … → Simpl / HTTP Battles (2025-06-05) |
| Candidate git roots (depth ≤2) | **32** (**lower bound**; deeper not scanned) |

## Default-protect

`C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` — organisation / FAW host repo. Locked default-protect. Draft candidates beyond this path: [`must-preserve.md`](must-preserve.md).

## Explicit exclusions

- No deep documentation of `node_modules`, build caches, or OS junk trees (parent presence only).
- No secret file contents (`.env` may appear as path only).
- This inventory is **not** a complete deep scan of every file under `C:\Project`.

## Top-level map

| Name | Created | LastWrite | Cheap MB | Band | Wrapper / git class | Activity / next hint |
| --- | --- | --- | --- | --- | --- | --- |
| `.vscode` | 2025-08-07 | 2025-09-05 | ~0 | S | no-git | Hygiene |
| `2026.09.09 - Organisation` | 2026-09-09 | 2026-09-09 | 0.34 | S | thin-wrapper-1git | **Default-protect**; freshest LastWrite |
| `AngularTest` | 2025-08-07 | 2025-08-07 | 5.21 | M | no-git | Early/simple |
| `CursorMobileWorkspace` | 2026-06-17 | 2026-06-17 | 11.15 | M | thin-wrapper-1git | Medium wrapper; recent |
| `epsic` | 2025-12-10 | 2025-12-17 | 22.79 | M | no-git | Early/simple; course-like |
| `GitTest` | 2025-08-08 | 2025-08-08 | 0.29 | S | multi-nested (2) | Multi-experiment |
| `HTTP Battles` | 2025-06-05 | 2025-06-05 | 26.82 | M | **top-git+nested** | Empty parent (0 commits); classify before move |
| `IA` | 2025-12-12 | 2025-12-12 | 0.01 | S | no-git | Early/simple |
| `NextPWATraining` | 2025-06-23 | 2025-06-23 | 0.10 | S | thin-wrapper-1git | Medium; `.env` **path present** |
| `NextTest` | 2025-06-23 | 2025-06-23 | 1.58 | M | thin-wrapper-1git | Medium wrapper |
| `node_modules` | 2025-06-24 | 2025-11-18 | 25.78 | M | no-git (orphan) | Hygiene — presence only |
| `Obsidian` | 2026-04-13 | 2026-05-26 | 1576.87 | **XL** | multi-nested (4 incl. worktrees) | **After git-strategy**; high must-preserve candidate |
| `PlayTestTristan` | 2025-06-23 | 2025-06-23 | 0.18 | S | no-git | Early/simple → **moved Cycle 2** to `C:\Project\archive\2025.06.23 - PlayTestTristan` |
| `PostManResponses` | 2025-10-01 | 2025-10-01 | 0.04 | S | no-git | Early/simple → **moved Cycle 2** to `C:\Project\archive\2025.10.01 - PostManResponses` |
| `ProjetOrif` | 2025-08-07 | 2026-01-07 | 187.86 | **L** | multi-nested (7 @ depth 2) | High complexity; after git-strategy |
| `PWAExemple` | 2025-06-25 | 2025-06-30 | 5.09 | M | multi-nested (2) | Multi-experiment |
| `PWAExempleTristan` | 2025-07-04 | 2025-07-04 | 1.58 | M | thin-wrapper-1git | Medium wrapper |
| `ReactRouterTest` | 2025-08-12 | 2025-08-12 | 0.22 | S | thin-wrapper-1git | Medium wrapper |
| `Simpl` | 2025-06-05 | 2025-06-05 | 0.89 | S | thin-wrapper-1git | Medium wrapper; oldest LastWrite tier |
| `Simpl_Next` | 2025-06-23 | 2025-06-23 | 1.75 | M | thin-wrapper-1git | Medium wrapper |
| `TestRyan` | 2025-06-25 | 2025-06-25 | 0.20 | S | thin-wrapper-1git | Medium wrapper |
| `WebCatalogue` | 2025-11-07 | 2025-12-22 | 0.02 | S | **top-git-flat** | Special git; active-looking project |
| `WorkSpace` | 2026-05-29 | 2026-06-10 | 2308.43 | **XL** | multi-nested (3) | Multi-experiment; large cheap payload |
| `WorkStationPWA` | 2025-07-01 | 2025-08-12 | 0.62 | S | multi-nested (2) | Multi-experiment |
| `ZedTest` | 2026-06-30 | 2026-07-01 | ~0 | S | no-git | Early/simple → **moved Cycle 2** to `C:\Project\paused\2026.06.30 - ZedTest` |
| `.dockerignore` | 2025-09-05 | 2025-09-05 | — | S | orphan file | Hygiene |
| `Dockerfile` | 2025-09-05 | 2025-09-05 | — | S | orphan file | Hygiene |
| `package-lock.json` | 2025-06-24 | 2025-11-18 | — | S | orphan file | Hygiene w/ root `node_modules` |
| `package.json` | 2025-06-24 | 2025-11-18 | — | S | orphan file | Hygiene |

## Wrapper / git class patterns

| Pattern | Meaning | Examples |
| --- | --- | --- |
| thin-wrapper-1git | Canonical dated label = **wrapper**; nested `.git` = **child atomic unit** | `Simpl`, `NextTest`, `CursorMobileWorkspace`, org folder, … |
| multi-nested | Wrapper still top-level move unit; children stay atomic; may need sub-batches / keep-vs-split | `ProjetOrif`, `GitTest`, `PWAExemple`, `WorkSpace`, `Obsidian`, `WorkStationPWA` |
| top-git-flat | Wrapper ≡ git root | `WebCatalogue` |
| top-git+nested | Classify before move (empty parent vs child); default wrapper label still on top folder | `HTTP Battles` |
| no-git | Safe for Early/simple without git-strategy | Early/simple set + orphans |

## Candidate git roots (depth 0–2)

**Depth limit:** roots deeper than 2 were not scanned. Treat **32** as a **lower bound**. Re-scan the target folder at the start of each later top-level cycle.

### Depth 0 (top-level `.git`)

- `HTTP Battles` — empty parent repo (**0** commits); nested real repo at depth 1
- `WebCatalogue` — flat project root

### Depth 1

- `2026.09.09 - Organisation\2026.09.09---Organisation` (**default-protect**)
- `CursorMobileWorkspace\CursorMobileWorkspace`
- `GitTest\NextTest`, `GitTest\test`
- `HTTP Battles\http-battles`
- `NextPWATraining\blogr-nextjs-prisma`
- `NextTest\NextTest`
- `Obsidian\Obsidian` (main vault; worktrees linked)
- `PWAExemple\PWAExempleNext`, `PWAExemple\PWAFrontAuthTest`
- `PWAExempleTristan\PWATristan`
- `ReactRouterTest\ReactRouterTest`
- `Simpl\Project-Simpl`
- `Simpl_Next\SimplNext`
- `TestRyan\python-mini-jeux`
- `WorkSpace\OS-IA`, `WorkSpace\TestNewWorkspaceAgent`
- `WorkStationPWA\WorkStationPWA`

### Depth 2 (notable)

- `Obsidian\worktrees\*` — additional linked worktree checkouts
- `ProjetOrif\frontBack\template_frontback` (+ Clean / TestAzure / `_test` variants)
- `ProjetOrif\springAuth\spring-auth`
- `ProjetOrif\testSpringDoc\gs-rest-service`, `gs-testing-restdocs`
- `WorkSpace\TestNewWorkspaceAgent\hermes-agent`
- `WorkStationPWA\WorkStationRouterPWA\workstation-app`

## Secrets (path presence only)

| Path | Note |
| --- | --- |
| `NextPWATraining\blogr-nextjs-prisma\.env` | Presence only — **never** open or quote contents |

## Root orphans (presence only)

`package.json`, `package-lock.json`, `Dockerfile`, `.dockerignore`, top-level `node_modules/` — candidate for a later approved hygiene mini-batch; ownership TBD.

## Patterns for later cycles

1. Many top-level folders are **thin wrappers** around one nested project (canonical label on wrapper).
2. **Containers** (`ProjetOrif`, `PWAExemple`, `WorkSpace`, `WorkStationPWA`, `GitTest`) need keep-vs-split decisions.
3. **Obsidian** worktrees must move as a linked set (after git-strategy).
4. **HTTP Battles** empty parent vs real child — classify before rename/move.
5. **CreationTime wins** for proposed date labels; LastWrite ≈ activity for “next.”
6. Early/simple (no-git): `PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest`.
