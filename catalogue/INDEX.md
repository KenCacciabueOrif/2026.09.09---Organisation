# Corpus index — C:\Project

**Role:** durable “dated view + what’s next + navigate” surface.  
**Paths:** **current** locations under `C:\Project` (Cycle 2 moved Early/simple subset of 3 into `archive` / `paused`).  
**Related:** [`../program/CHARTER.md`](../program/CHARTER.md) · [`../program/ROADMAP.md`](../program/ROADMAP.md) · [`taxonomy.md`](taxonomy.md) · [`inventory.md`](inventory.md) · [`must-preserve.md`](must-preserve.md)

## Legend

| Column | Meaning |
| --- | --- |
| Status | Vocabulary: `active` / `paused` / `archive` / `protect` / `hygiene` (aligned with [`taxonomy.md`](taxonomy.md)). Rows may still show `TBD` until the user assigns or ratifies. Statuses are **provisional** until user assignment/sign-off. |
| Date label | Current folder name if already dated; otherwise **proposed** `yyyy.mm.dd - Name` from **CreationTime** (illustrative). |
| Current path | Actual path today under `C:\Project`. |
| Git root? | Coarse: top-level `.git` and/or known nested roots (depth ≤2 scan). |
| Next / notes | Triage hints for later cycles. |

**Do not treat proposed date labels as completed renames.**  
Size bands (S/M/L/XL) and wrapper/git classes live in [`inventory.md`](inventory.md). Preserve candidates: [`must-preserve.md`](must-preserve.md) (**draft**).

## Index (top-level)

| Status | Date label (current or proposed) | Current path | Git root? | Next / notes |
| --- | --- | --- | --- | --- |
| protect | `2026.09.09 - Organisation` (current) | `C:\Project\2026.09.09 - Organisation` | nested (org repo) | **Default-protect**; never casual move |
| TBD | proposed `2025.08.07 - vscode-workspace` | `C:\Project\.vscode` | no | Hygiene / workspace config |
| TBD | proposed `2025.08.07 - AngularTest` | `C:\Project\AngularTest` | no (zip extract) | Early/simple batch |
| TBD | proposed `2026.06.17 - CursorMobileWorkspace` | `C:\Project\CursorMobileWorkspace` | nested depth 1 | Medium wrapper |
| TBD | proposed `2025.12.10 - epsic` | `C:\Project\epsic` | no | Early/simple; course-like |
| TBD | proposed `2025.08.08 - GitTest` | `C:\Project\GitTest` | 2 nested | Multi-experiment; sub-batches |
| TBD | proposed `2025.06.05 - HTTP Battles` | `C:\Project\HTTP Battles` | top + nested | Empty parent git — classify first |
| TBD | proposed `2025.12.12 - IA` | `C:\Project\IA` | no | Early/simple |
| TBD | proposed `2025.06.23 - NextPWATraining` | `C:\Project\NextPWATraining` | nested | `.env` opaque on move; medium wrapper |
| TBD | proposed `2025.06.23 - NextTest` | `C:\Project\NextTest` | nested | Medium wrapper |
| hygiene | (orphan) | `C:\Project\node_modules` | no | Root orphan — hygiene mini-batch |
| TBD | proposed `2026.04.13 - Obsidian` | `C:\Project\Obsidian` | nested + worktrees | **After git-strategy only** |
| archive | `2025.06.23 - PlayTestTristan` | `C:\Project\archive\2025.06.23 - PlayTestTristan` | no | Early/simple — moved Cycle 2 |
| archive | `2025.10.01 - PostManResponses` | `C:\Project\archive\2025.10.01 - PostManResponses` | no | Early/simple — moved Cycle 2; snippet candidate |
| TBD | proposed `2025.08.07 - ProjetOrif` | `C:\Project\ProjetOrif` | many nested | High complexity; after git-strategy |
| TBD | proposed `2025.06.25 - PWAExemple` | `C:\Project\PWAExemple` | 2 nested | Multi-experiment |
| TBD | proposed `2025.07.04 - PWAExempleTristan` | `C:\Project\PWAExempleTristan` | nested | Medium wrapper |
| TBD | proposed `2025.08.12 - ReactRouterTest` | `C:\Project\ReactRouterTest` | nested | Medium wrapper |
| TBD | proposed `2025.06.05 - Simpl` | `C:\Project\Simpl` | nested | Medium wrapper |
| TBD | proposed `2025.06.23 - Simpl_Next` | `C:\Project\Simpl_Next` | nested | Medium wrapper |
| TBD | proposed `2025.06.25 - TestRyan` | `C:\Project\TestRyan` | nested | Medium wrapper |
| TBD | proposed `2025.11.07 - WebCatalogue` | `C:\Project\WebCatalogue` | **yes** (top) | Special git; SSH remote sample |
| TBD | proposed `2026.05.29 - WorkSpace` | `C:\Project\WorkSpace` | nested (+ deeper) | Multi-experiment |
| TBD | proposed `2025.07.01 - WorkStationPWA` | `C:\Project\WorkStationPWA` | nested | Multi-experiment |
| paused | `2026.06.30 - ZedTest` | `C:\Project\paused\2026.06.30 - ZedTest` | no | Early/simple — moved Cycle 2 |
| hygiene | (orphan) | `C:\Project\.dockerignore` | — | Root Docker context |
| hygiene | (orphan) | `C:\Project\Dockerfile` | — | Root Docker context |
| hygiene | (orphan) | `C:\Project\package.json` | — | Root orphan tooling |
| hygiene | (orphan) | `C:\Project\package-lock.json` | — | Ties to root `node_modules` |

## What’s next (program)

1. **User sign-off:** review taxonomy (**proposed-ratified — ready for user sign-off**) and the [`must-preserve.md`](must-preserve.md) draft.
2. **Primary next program row:** remaining **Early/simple** — `IA`, `AngularTest`, `epsic` (Cycle 2 moved `PostManResponses`, `PlayTestTristan`, `ZedTest` into `archive` / `paused`).
3. **Hard gate (not primary next):** dedicated **Git-strategy** FAW **before** Obsidian / ProjetOrif multi-root / worktree moves.

## Scan caveat

Git-root flags come from a depth ≤2 research scan (**lower bound**). Re-scan each folder before its move cycle. Cheap size bands: see [`inventory.md`](inventory.md).
