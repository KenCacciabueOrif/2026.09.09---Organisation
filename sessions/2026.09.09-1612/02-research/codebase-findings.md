# Codebase findings — Cycle 6 Medium wrappers (soft-deferred finalization)

**Session:** `sessions/2026.09.09-1612/02-research/`  
**Live-check date:** 2026.09.09 (cycle reference)  
**90-day cutoff:** LastWrite ≥ `2026-06-11` → `paused`; else default `archive`  
**No moves this phase.**

## INDEX vs disk (path truth)

| Folder | INDEX current path | Disk at claimed path? | Verdict |
| --- | --- | --- | --- |
| `NextPWATraining` | `C:\Project\NextPWATraining` | **yes** | live source OK — in-scope finalize |
| `CursorMobileWorkspace` | `C:\Project\CursorMobileWorkspace` | **yes** | live source OK — in-scope finalize |
| `TestRyan` | `archive\2025.06.25 - TestRyan` | root **absent**; archive **present** | Cycle 4 — **verify-only**; do not re-move |
| `ReactRouterTest` | `archive\2025.08.12 - ReactRouterTest` | root **absent**; archive **present** | Cycle 4 — **verify-only** |
| `Simpl` | `archive\2025.06.05 - Simpl` | root **absent**; archive **present** | Cycle 4 — **verify-only** |
| `NextTest` | `archive\2025.06.23 - NextTest` | root **absent**; archive **present** | Cycle 5 — **verify-only** |
| `Simpl_Next` | `archive\2025.06.23 - Simpl_Next` | root **absent**; archive **present** | Cycle 5 — **verify-only** |
| `PWAExempleTristan` | `archive\2025.07.04 - PWAExempleTristan` | root **absent**; archive **present** | Cycle 5 — **verify-only** |

INDEX paths for the two remaining soft-deferred names match disk. Cycle 4/5 archives are **not** move sources.

## In-scope live matrix

| Folder | Exists | CreationTime → date label | LastWrite | Within 90d? | Proposed status | Nested `.git` | Remotes | Worktrees / gitfile | `.env` path (opaque) | Top-level kids | Approx size | Band | Target collision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NextPWATraining` | yes | `2025.06.23 - NextPWATraining` | 2025-06-23 | **no** | **archive** | `NextPWATraining\blogr-nextjs-prisma\.git` | 1× **SSH** `origin` | single main WT; no `.git` file; no `worktrees/`; `git-dir`=`git-common-dir` | **PRESENT** `...\blogr-nextjs-prisma\.env` (path only — never read) | 1 (`blogr-nextjs-prisma`) | ~379.5 MB | **L** | none under `archive`/`paused`/`active` |
| `CursorMobileWorkspace` | yes | `2026.06.17 - CursorMobileWorkspace` | 2026-06-17 | **yes** | **paused** | `CursorMobileWorkspace\CursorMobileWorkspace\.git` | 1× HTTPS `origin` | same (single main WT) | none depth≤5 | 1 (`CursorMobileWorkspace`) | ~17.1 MB | **M** | none |

### Nested remotes (evidence only; no push / no URL rewrite)

- `NextPWATraining\blogr-nextjs-prisma` → `git@github.com:KenCacciabueOrif/NextPWATraining.git` (fetch + push)
- `CursorMobileWorkspace\CursorMobileWorkspace` → `https://github.com/KenCacciabueOrif/CursorMobileWorkspace.git` (fetch + push)

`git worktree list` each: **one** path (main checkout only). No submodules reported. Wrapper roots have **no** top-level `.git`.

### Hazard verdict (hard fail-closed screen)

| Check | NextPWATraining | CursorMobileWorkspace |
| --- | --- | --- |
| Extra linked worktrees / `.git` gitfile / `.git/worktrees` | **none** | **none** |
| Multi-remote / pushurl divergence | **1 remote only** | **1 remote only** |
| Unclear git strategy (empty parent git, bare, split needed) | thin-wrapper-1git; clear | thin-wrapper-1git; clear |
| Target path collision | **none** | **none** |
| Hard fail-closed this cycle? | **no** | **no** |

**SSH note (NextPWATraining):** single SSH `origin` was a Cycle 4/5 *soft-prefer* defer (safer peers available), **not** a hard worktree/multi-remote abort (see `sessions/2026.09.09-1535/02-research/`). Continuity for this cycle: **path-only** move; **no** remote URL rewrite; **no** agent push/pull. Treat SSH as residual informational risk, not Q5 skip, unless plan gate adopts a stricter “any SSH = skip” reading (then Q5=A → skip NextPWA only).

**Secrets:** `.env` path present under NextPWA nested tree — include unread in move; never open/log contents. CursorMobile: no `.env` found depth≤5.

## Parents / layout

| Path | Exists |
| --- | --- |
| `C:\Project\archive` | **yes** |
| `C:\Project\paused` | **yes** |
| `C:\Project\active` | **no** (not needed; statuses are archive + paused) |

## Proposed destinations (hypothesis until plan gate)

| From | To | Status axis |
| --- | --- | --- |
| `C:\Project\NextPWATraining` | `C:\Project\archive\2025.06.23 - NextPWATraining` | archive |
| `C:\Project\CursorMobileWorkspace` | `C:\Project\paused\2026.06.17 - CursorMobileWorkspace` | paused |

Nested `.git` remains under the same relative child paths after wrapper move. Reverse-move = dated folder → original root short name.

## Catalogue / program pointers (why they matter)

| Path | Why |
| --- | --- |
| `catalogue/INDEX.md` | Both remaining Medium names still at root; Cycle 4/5 archive rows current |
| `catalogue/inventory.md` | thin-wrapper-1git; NextPWA `.env` presence note; nested paths |
| `catalogue/taxonomy.md` | CreationTime labels; wrapper = move unit; nested git atomic |
| `catalogue/must-preserve.md` | draft — these two are **not** must-preserve; do not auto-lock |
| `program/ROADMAP.md` | Medium **nearly complete**; Remaining (2 soft-deferred); finalize by default |
| `sessions/2026.09.09-1535/02-research/` | Cycle 4: SSH alone ≠ hard abort |
| `sessions/2026.09.09-1554/02-research/` | Cycle 5: soft-deferred this pair; safer three moved |
| `sessions/2026.09.09-1612/01-prompt-betterment/refined-prompt.md` | This cycle AC + Q1–Q5 locks |

## Size-band note vs inventory

Inventory listed NextPWA as **S** (~0.10 MB class) and CursorMobile as **M** (~11 MB). Live full recurse: NextPWA ≈ **380 MB (L)**; CursorMobile ≈ **17 MB (M)**. Planner/implementer: expect longer `Move-Item` for NextPWA; do **not** treat size as hazard skip.
