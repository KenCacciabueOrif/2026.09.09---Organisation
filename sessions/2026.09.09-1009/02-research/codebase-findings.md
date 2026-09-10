# Codebase findings — Cycle 1 deepen

Session: `sessions/2026.09.09-1009/02-research/`  
Corpus root: `C:\Project`  
Scan date: 2026-09-09  
Method: refresh top-level listing + **cheap size bands** (file-byte sum excluding `node_modules`, `.git`, `.next`, `dist`, `build`, `coverage`, `.cache`, `.pytest_cache`, `__pycache__`, `.turbo`, `.vercel`) + nested `.git` discovery **depth ≤2** (same bound as Cycle 0). **No moves.** Secrets: path presence only.

**Deepens** `catalogue/inventory.md` / Cycle 0 `sessions/2026.09.09-0929/02-research/codebase-findings.md` — does not replace program locks.

## Scan limits (record explicitly)

| Limit | Value |
| --- | --- |
| Top-level only for bands / timestamps | Yes — one row per `C:\Project` child |
| Git discovery depth | **0–2** under each top-level; skip named cache/dep dirs when walking |
| Size metric | **Cheap payload** (excludes dep/cache/.git trees) — understates true on-disk size when `node_modules` / `.git` dominate |
| Size band cutoffs (documented for implementer) | **S** &lt; 1 MB · **M** 1–&lt;50 MB · **L** 50–&lt;500 MB · **XL** ≥ 500 MB |
| Deep `node_modules` / cache inventory | **Skipped** (presence of root orphan `node_modules` only) |
| Secret contents | **Not read** |

Treat git-root count **32** as a **lower bound**. Re-scan the target folder at the start of any later move cycle.

## Corpus summary (refreshed)

| Signal | Value |
| --- | --- |
| `C:\Project` itself a git root? | **No** |
| Top-level entries | **29** (25 dirs + 4 files) |
| Candidate git roots (depth ≤2) | **32** (unchanged vs Cycle 0) |
| Size-band mix (cheap) | **S=17**, **M=9**, **L=1**, **XL=2** |
| Creation-year mix | **2025: 24**, **2026: 5** |
| LastWrite activity (newest → older notable) | Org repo (2026-09-09) → ZedTest → CursorMobileWorkspace → WorkSpace → Obsidian → ProjetOrif → WebCatalogue → … → Simpl / HTTP Battles (2025-06-05) |

## Default-protect (locked)

`C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` — FAW host; nested git at depth 1.

## Top-level deepen map

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
| `PlayTestTristan` | 2025-06-23 | 2025-06-23 | 0.18 | S | no-git | Early/simple |
| `PostManResponses` | 2025-10-01 | 2025-10-01 | 0.04 | S | no-git | Early/simple; snippet |
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
| `ZedTest` | 2026-06-30 | 2026-07-01 | ~0 | S | no-git | Early/simple; recent LastWrite |
| `.dockerignore` | 2025-09-05 | 2025-09-05 | — | S | orphan file | Hygiene |
| `Dockerfile` | 2025-09-05 | 2025-09-05 | — | S | orphan file | Hygiene |
| `package-lock.json` | 2025-06-24 | 2025-11-18 | — | S | orphan file | Hygiene w/ root `node_modules` |
| `package.json` | 2025-06-24 | 2025-11-18 | — | S | orphan file | Hygiene |

**CreationTime → proposed date labels** (already used in INDEX; Cycle 1 lock: CreationTime wins over earliest commit / LastWrite). LastWrite is for **activity / “next”** only.

## Git roots (depth ≤2) — clearer notes

**Depth 0 (top-level `.git`):**

- `HTTP Battles` — parent empty (`rev-list --all --count` = **0**; untracked `http-battles/`); nested real repo at depth 1
- `WebCatalogue` — flat project root

**Depth 1:** same set as Cycle 0 inventory (org repo, thin wrappers, GitTest×2, Obsidian main, PWAExemple×2, WorkSpace×2, WorkStationPWA, etc.)

**Depth 2:** Obsidian `worktrees/*` (3 linked checkouts); ProjetOrif frontBack variants + springAuth + testSpringDoc; WorkSpace `hermes-agent`; WorkStationRouterPWA `workstation-app`

### Wrapper rule evidence (Cycle 1 locked docs rule)

| Pattern | Examples | Docs implication |
| --- | --- | --- |
| thin-wrapper-1git | `Simpl`, `NextTest`, `CursorMobileWorkspace`, org folder, … | Canonical dated label = **wrapper**; nested `.git` = **child atomic unit** |
| multi-nested | `ProjetOrif`, `GitTest`, `PWAExemple`, `WorkSpace`, `Obsidian`, `WorkStationPWA` | Wrapper still top-level move unit; children stay atomic; may need sub-batches / keep-vs-split note |
| top-git-flat | `WebCatalogue` | Wrapper ≡ git root |
| top-git+nested | `HTTP Battles` | **Still open / classify before move** (empty parent vs child) — default wrapper label still applies to top folder name until classified |
| no-git | Early/simple set + orphans | Safe for Early/simple without git-strategy |

## Secrets (path presence only)

| Path | Note |
| --- | --- |
| `NextPWATraining\blogr-nextjs-prisma\.env` | `Test-Path` = True — **never** open/quote contents |

## Must-preserve **draft** candidates (for user review — not auto-locked)

Beyond default-protect org repo, agent proposes:

| Priority hint | Path | Why proposed |
| --- | --- | --- |
| Locked default | `...\2026.09.09---Organisation` | FAW host / index home |
| High | `C:\Project\Obsidian` | Linked worktrees; XL; break risk without git-strategy |
| High | `C:\Project\ProjetOrif` | 7 nested roots @ depth 2; L band; professional container |
| Medium-high | `C:\Project\WebCatalogue` | Top-level git with remotes (Cycle 0 sample); likely “real” project |
| Medium | `C:\Project\WorkSpace` | XL cheap size; nested agent experiments + deeper `hermes-agent` |
| Medium | `C:\Project\HTTP Battles` (esp. nested `http-battles`) | Empty-parent oddity; real nested repo — classify before casual move |
| Optional review | `C:\Project\CursorMobileWorkspace` | Recent LastWrite; single nested git |
| Optional review | `C:\Project\NextPWATraining` | Opaque `.env` payload on any later move |

Label in catalogue: **draft — not auto-locked**. User may add/remove before first move-capable cycle.

## Early/simple set (roadmap primary next suggestion)

All **no-git** at depth ≤1; mostly **S/M**; no worktrees:

`PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest`

Rationale for suggesting this row **next** (after Cycle 1 docs): lowest git-strategy coupling; can practice approve→move→INDEX update while taxonomy is only proposed-ratified; Obsidian/ProjetOrif remain gated.

## Explicit non-actions this pass

- No FS mutation under `C:\Project`
- No deep `node_modules` / cache trees
- No secret file reads
- No full remote inventory (inherit Cycle 0 samples)
- No publish/push preflight (out of scope)

## Prior-art paths (org repo)

- `catalogue/INDEX.md`, `inventory.md`, `taxonomy.md` — Cycle 0 stubs to deepen / proposed-ratify
- `program/ROADMAP.md`, `CHARTER.md`, `organisation-approach.md` — Cycle 1 updates Early/simple + git-strategy hard gate
- `sessions/2026.09.09-0929/02-research/*` — Cycle 0 baseline
- `sessions/2026.09.09-1009/01-prompt-betterment/refined-prompt.md`, `notes.md` — locked Cycle 1 decisions
