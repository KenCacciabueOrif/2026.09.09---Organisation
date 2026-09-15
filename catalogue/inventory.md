# Coarse inventory — C:\Project

**Source:** Cycle 0 baseline + Cycle 1 deepen from `sessions/2026.09.09-1009/02-research/codebase-findings.md`  
**Scan date:** 2026-09-09  
**Method:** top-level listing + **cheap size bands** + nested `.git` discovery. Cycles 2–3 moved all Early/simple folders under `archive` / `paused`; Cycles 4–6 moved all Medium wrappers under `archive` / `paused` (see path notes below).  
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
| Top-level entries | After Cycle 6 — Early/simple + all Medium wrappers under `archive`/`paused`; parents `archive`/`paused` remain |
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
| `AngularTest` | 2025-08-07 | 2025-08-07 | 5.21 | M | no-git | Early/simple → **moved Cycle 3** to `C:\Project\archive\2025.08.07 - AngularTest` |
| `CursorMobileWorkspace` | 2026-06-17 | 2026-06-17 | 11.15 | M | thin-wrapper-1git | Medium → **moved Cycle 6** to `C:\Project\paused\2026.06.17 - CursorMobileWorkspace` |
| `epsic` | 2025-12-10 | 2025-12-17 | 22.79 | M | no-git | Early/simple → **moved Cycle 3** to `C:\Project\archive\2025.12.10 - epsic` |
| `GitTest` | 2025-08-08 | 2025-08-08 | 0.29 | S | multi-nested (2) | Multi-experiment → **moved Cycle 7** to `C:\Project\archive\2025.08.08 - GitTest` |
| `HTTP Battles` | 2025-06-05 | 2025-06-05 | 26.82 | M | **top-git+nested** | Empty parent (0 commits); classify before move |
| `IA` | 2025-12-12 | 2025-12-12 | 0.01 | S | no-git | Early/simple → **moved Cycle 3** to `C:\Project\archive\2025.12.12 - IA` |
| `NextPWATraining` | 2025-06-23 | 2025-06-23 | 0.10 | S | thin-wrapper-1git | Medium → **moved Cycle 6** to `C:\Project\archive\2025.06.23 - NextPWATraining`; live on-disk ~L (~380 MB) incl. deps; cheap band still S; `.env` **path present** (opaque) |
| `NextTest` | 2025-06-23 | 2025-06-23 | 1.58 | M | thin-wrapper-1git | Medium → **moved Cycle 5** to `C:\Project\archive\2025.06.23 - NextTest` |
| `node_modules` | 2025-06-24 | 2025-11-18 | 25.78 | M | no-git (orphan) | Hygiene — presence only |
| `Obsidian` | 2026-04-13 | 2026-05-26 | 1576.87 | **XL** | multi-nested (4 incl. worktrees) | **After git-strategy**; high must-preserve candidate |
| `PlayTestTristan` | 2025-06-23 | 2025-06-23 | 0.18 | S | no-git | Early/simple → **moved Cycle 2** to `C:\Project\archive\2025.06.23 - PlayTestTristan` |
| `PostManResponses` | 2025-10-01 | 2025-10-01 | 0.04 | S | no-git | Early/simple → **moved Cycle 2** to `C:\Project\archive\2025.10.01 - PostManResponses` |
| `ProjetOrif` | 2025-08-07 | 2026-01-07 | 187.86 | **L** | multi-nested (7 @ depth 2) | High complexity; after git-strategy |
| `PWAExemple` | 2025-06-25 | 2025-06-30 | 5.09 | M | multi-nested (3) | Multi-experiment → **moved Cycle 8** to `C:\Project\archive\2025.06.25 - PWAExemple`; SSH nested origin path-only; `.env`×4 opaque |
| `PWAExempleTristan` | 2025-07-04 | 2025-07-04 | 1.58 | M | thin-wrapper-1git | Medium → **moved Cycle 5** to `C:\Project\archive\2025.07.04 - PWAExempleTristan` |
| `ReactRouterTest` | 2025-08-12 | 2025-08-12 | 0.22 | S | thin-wrapper-1git | Medium → **moved Cycle 4** to `C:\Project\archive\2025.08.12 - ReactRouterTest` |
| `Simpl` | 2025-06-05 | 2025-06-05 | 0.89 | S | thin-wrapper-1git | Medium → **moved Cycle 4** to `C:\Project\archive\2025.06.05 - Simpl`; oldest LastWrite tier |
| `Simpl_Next` | 2025-06-23 | 2025-06-23 | 1.75 | M | thin-wrapper-1git | Medium → **moved Cycle 5** to `C:\Project\archive\2025.06.23 - Simpl_Next` |
| `TestRyan` | 2025-06-25 | 2025-06-25 | 0.20 | S | thin-wrapper-1git | Medium → **moved Cycle 4** to `C:\Project\archive\2025.06.25 - TestRyan` |
| `WebCatalogue` | 2025-11-07 | 2025-12-22 | 0.02 | S | **top-git-flat** | Special git; active-looking project |
| `WorkSpace` | 2026-05-29 | 2026-06-10 | 2308.43 | **XL** | multi-nested (**4** live under WorkSpace after Cycle 19; was **5** post–Cycle 14 / **7** earlier) | Multi-experiment — remains at `C:\Project\WorkSpace` (TNA envelope); Cycle 9–16 strategy / Appendix A / multi-remote **Cleared**; Cycle 19 Continuity **X** (`sessions/2026.09.15-1014/`): fate/clearance docs + **OS-IA** → `C:\Project\archive\2026.09.15 - OS-IA`; Cycle 20 (`sessions/2026.09.15-1117/`): parent-surgery **DRAFT** ([`../program/git-strategy-tna-parent-surgery.md`](../program/git-strategy-tna-parent-surgery.md); #4 approval pending) — nests **not** moved; Cycle 23 (`sessions/2026.09.15-1432/`): #4 **approved-for-named-map** (hermes-agent → `C:\Project\archive\2026.09.15 - hermes-agent`); nest execute **held**; **A+E reserved**; hermes **still** under TNA; nested still **4**; whole tree **not** archived; still at root; row **Remaining: WorkSpace only** — **not** Complete; opaque `.env*` re-attest on remaining units as needed; clearance_whole_tree still **NO** (historical size cell optional) |
| `WorkStationPWA` | 2025-07-01 | 2025-08-12 | 0.62 | S | multi-nested (2) | Multi-experiment → **moved Cycle 7** to `C:\Project\archive\2025.07.01 - WorkStationPWA`; SSH nested origin path-only |
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
- `archive\2025.08.08 - GitTest\NextTest`, `archive\2025.08.08 - GitTest\test` (moved Cycle 7)
- `HTTP Battles\http-battles`
- `Obsidian\Obsidian` (main vault; worktrees linked)
- `archive\2025.06.25 - PWAExemple\PWAExempleNext`, `archive\2025.06.25 - PWAExemple\PWAFrontAuthTest` (moved Cycle 8); also nested `…\PWAExempleAuth\PWAExempleAuth\PWAExempleAuth`
- `archive\2025.06.23 - NextPWATraining\blogr-nextjs-prisma` (moved Cycle 6)
- `archive\2025.06.23 - NextTest\NextTest` (moved Cycle 5)
- `archive\2025.07.04 - PWAExempleTristan\PWATristan` (moved Cycle 5)
- `archive\2025.08.12 - ReactRouterTest\ReactRouterTest` (moved Cycle 4)
- `archive\2025.06.05 - Simpl\Project-Simpl` (moved Cycle 4)
- `archive\2025.06.23 - Simpl_Next\SimplNext` (moved Cycle 5)
- `archive\2025.06.25 - TestRyan\python-mini-jeux` (moved Cycle 4)
- `paused\2026.06.17 - CursorMobileWorkspace\CursorMobileWorkspace` (moved Cycle 6)
- `WorkSpace\TestNewWorkspaceAgent` (Cycle 19 live under WorkSpace after OS-IA split — TNA + depth-2 nests; `_backups`/`_quarantine` hermes clones remain under `archive\hygiene\`; depth ≤2 list remains lower bound)
- `archive\2026.09.15 - OS-IA` (moved Cycle 19 Continuity X from `WorkSpace\OS-IA`)
- `archive\2025.07.01 - WorkStationPWA\WorkStationPWA` (moved Cycle 7)

### Depth 2 (notable)

- `Obsidian\worktrees\*` — additional linked worktree checkouts
- `ProjetOrif\frontBack\template_frontback` (+ Clean / TestAzure / `_test` variants)
- `ProjetOrif\springAuth\spring-auth`
- `ProjetOrif\testSpringDoc\gs-rest-service`, `gs-testing-restdocs`
- `WorkSpace\TestNewWorkspaceAgent\hermes-agent`
- `archive\2025.07.01 - WorkStationPWA\WorkStationRouterPWA\workstation-app` (moved Cycle 7)

## Secrets (path presence only)

| Path | Note |
| --- | --- |
| `archive\2025.06.23 - NextPWATraining\blogr-nextjs-prisma\.env` | Presence only (moved Cycle 6 with wrapper) — **never** open or quote contents |
| `archive\2025.06.23 - NextTest\NextTest\app-test\.env` | Presence only (moved Cycle 5 with wrapper) — **never** open or quote contents |
| `archive\2025.06.23 - Simpl_Next\SimplNext\simpl-app\.env` | Presence only (moved Cycle 5 with wrapper) — **never** open or quote contents |
| `archive\2025.07.04 - PWAExempleTristan\PWATristan\pwa-tristan-app\.env` | Presence only (moved Cycle 5 with wrapper) — **never** open or quote contents |
| `archive\2025.06.05 - Simpl\Project-Simpl\simpl-app\api\env\.env` | Presence only (moved Cycle 4 with wrapper) — **never** open or quote contents |
| `archive\2025.06.25 - PWAExemple\PWAExempleAuth\PWAExempleAuth\PWAExempleAuth\pwa-exemple-auth-app\.env` | Presence only (moved Cycle 8 with wrapper) — **never** open or quote contents |
| `archive\2025.06.25 - PWAExemple\PWAExempleNext\pwa-test-app\.env` | Presence only (moved Cycle 8 with wrapper) — **never** open or quote contents |
| `archive\2025.06.25 - PWAExemple\PWAExempleNext\pwa-test-app\.env.local` | Presence only (moved Cycle 8 with wrapper) — **never** open or quote contents |
| `archive\2025.06.25 - PWAExemple\PWAFrontAuthTest\pwa-front-auth-test-app\.env` | Presence only (moved Cycle 8 with wrapper) — **never** open or quote contents |

## Root orphans (presence only)

`package.json`, `package-lock.json`, `Dockerfile`, `.dockerignore`, top-level `node_modules/` — candidate for a later approved hygiene mini-batch; ownership TBD.

## Patterns for later cycles

1. Many top-level folders are **thin wrappers** around one nested project (canonical label on wrapper).
2. **Containers** (`ProjetOrif`, `WorkSpace`; archived Cycle 7: `WorkStationPWA`, `GitTest`; archived Cycle 8: `PWAExemple`; archived Cycle 19 Continuity X: `OS-IA`) need keep-vs-split decisions for remaining roots. `WorkSpace` still root (TNA envelope) — Cycle 14 Appendix A isolated `_backups`/`_quarantine` only; Cycle 19 split OS-IA only; whole-tree still fail-closed.
3. **Obsidian** worktrees must move as a linked set (after git-strategy).
4. **HTTP Battles** empty parent vs real child — classify before rename/move.
5. **CreationTime wins** for proposed date labels; LastWrite ≈ activity for “next.”
6. Early/simple (no-git): **all moved** — Cycle 2: `PostManResponses`, `PlayTestTristan`, `ZedTest`; Cycle 3: `IA`, `AngularTest`, `epsic`.
7. Medium wrappers: **all moved** — Cycle 4: `TestRyan`, `ReactRouterTest`, `Simpl` → `archive`; Cycle 5: `NextTest`, `Simpl_Next`, `PWAExempleTristan` → `archive`; Cycle 6: `NextPWATraining` → `archive`; `CursorMobileWorkspace` → `paused`.
