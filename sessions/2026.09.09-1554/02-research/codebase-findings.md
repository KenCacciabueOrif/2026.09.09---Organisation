# Codebase findings — Cycle 5 Medium wrappers (safer three remaining)

**Session:** `sessions/2026.09.09-1554/02-research/`  
**Live-check date:** 2026.09.09 (cycle reference)  
**90-day cutoff:** LastWrite ≥ `2026-06-11` → `paused`; else default `archive`  
**No moves this phase.**

## INDEX vs disk (path truth)

| Folder | INDEX current path | Disk at claimed path? | Verdict |
| --- | --- | --- | --- |
| `NextTest` | `C:\Project\NextTest` | **yes** | live source OK |
| `Simpl_Next` | `C:\Project\Simpl_Next` | **yes** | live source OK |
| `PWAExempleTristan` | `C:\Project\PWAExempleTristan` | **yes** | live source OK |
| `NextPWATraining` | `C:\Project\NextPWATraining` | **yes** | soft-deferred; stay at root |
| `CursorMobileWorkspace` | `C:\Project\CursorMobileWorkspace` | **yes** | soft-deferred; stay at root |
| `TestRyan` | `archive\2025.06.25 - TestRyan` | root **absent**; archive **present** | Cycle 4 — **verify-only**; do not re-move |
| `ReactRouterTest` | `archive\2025.08.12 - ReactRouterTest` | root **absent**; archive **present** | Cycle 4 — **verify-only** |
| `Simpl` | `archive\2025.06.05 - Simpl` | root **absent**; archive **present** | Cycle 4 — **verify-only** |

INDEX Medium root paths for the remaining five match disk. No stale “still at root” claim for Cycle 4 peers.

## In-scope live matrix

| Folder | Exists | CreationTime → date label | LastWrite | Within 90d? | Proposed status | Nested `.git` | Remotes | Worktrees / gitfile | `.env` path (opaque) | Top-level kids | Approx size | Band | Target collision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NextTest` | yes | `2025.06.23 - NextTest` | 2025-06-23 | **no** | **archive** | `NextTest\NextTest\.git` | 1× HTTPS `origin` | single main WT; no `.git` file; no `worktrees/` | `...\NextTest\app-test\.env` | 1 (thin wrapper) | ~628 MB | **L** | none under `archive`/`paused`/`active` |
| `Simpl_Next` | yes | `2025.06.23 - Simpl_Next` | 2025-06-23 | **no** | **archive** | `Simpl_Next\SimplNext\.git` | 1× HTTPS `origin` | same | `...\SimplNext\simpl-app\.env` | 1 | ~663 MB | **L** | none |
| `PWAExempleTristan` | yes | `2025.07.04 - PWAExempleTristan` | 2025-07-04 | **no** | **archive** | `PWAExempleTristan\PWATristan\.git` | 1× HTTPS `origin` | same | `...\PWATristan\pwa-tristan-app\.env` | 1 | ~607 MB | **L** | none |

### Nested remotes (evidence only; no push)

- `NextTest\NextTest` → `https://github.com/KenCacciabueOrif/NextTest.git`
- `Simpl_Next\SimplNext` → `https://github.com/KenCacciabueOrif/SimplNext.git`
- `PWAExempleTristan\PWATristan` → `https://github.com/KenCacciabueOrif/PWATristan.git`

`git worktree list` each: **one** path (main checkout only).

### Hazard verdict (in-scope)

- **No** fail-closed worktree / multi-remote / unclear-git hazards among the safer three.
- Each is thin-wrapper-1git (matches `catalogue/inventory.md` class).
- `.env` **paths present** on all three — Continuity: include in move; never read contents; path-only logs.
- Size: live recurse (~600 MB) is **L** (likely `node_modules`); inventory earlier listed smaller M figures — treat live L as move-duration signal, **not** a skip reason.

## Soft-deferred (confirm at root; do **not** propose moves)

| Folder | At root? | CreationTime label | LastWrite / 90d | Nested `.git` | Remote note | `.env` | Why still deferred (Q2=A) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `NextPWATraining` | **yes** | `2025.06.23 - NextPWATraining` | outside → would be archive | `blogr-nextjs-prisma\.git` | **SSH** `git@github.com:...` | path present | higher-risk peer; SSH + flagged `.env`; not in safer-three pool |
| `CursorMobileWorkspace` | **yes** | `2026.06.17 - CursorMobileWorkspace` | **within 90d → paused** | `CursorMobileWorkspace\.git` | 1× HTTPS | none depth≤4 | would need `paused\`; soft-deferred by Choose |

## Parents / layout

| Path | Exists |
| --- | --- |
| `C:\Project\archive` | **yes** |
| `C:\Project\paused` | **yes** |
| `C:\Project\active` | **no** (not needed for this archive-only batch) |

## Catalogue / program pointers (why they matter)

| Path | Why |
| --- | --- |
| `catalogue/INDEX.md` | Current Medium root paths; Cycle 4 archive rows; What’s next lists remaining five |
| `catalogue/inventory.md` | thin-wrapper-1git class; nested paths; NextPWA `.env` presence note |
| `catalogue/taxonomy.md` | CreationTime labels; wrapper = move unit; nested git atomic |
| `catalogue/must-preserve.md` | draft — remaining Medium not must-preserve; do not auto-lock |
| `program/ROADMAP.md` | Medium row **in progress**; lock same row / remaining names |
| `sessions/2026.09.09-1535/02-research/` | Cycle 4 prior art: same Continuity rules; deferred these three intentionally |
| `sessions/2026.09.09-1554/01-prompt-betterment/refined-prompt.md` | This cycle AC + safer-three scope |

## Size-band note vs inventory

Inventory listed NextTest / Simpl_Next / PWAExempleTristan as **M** (~1–2 MB class figures). Live full recurse ≈ **600+ MB (L)** each. Planner/implementer: expect longer `Move-Item`; re-measure optional; do **not** treat as hazard skip.
