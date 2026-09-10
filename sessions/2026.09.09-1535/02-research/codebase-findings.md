# Codebase findings — Cycle 4 Medium wrappers (first subset)

**Session:** `sessions/2026.09.09-1535/02-research/`  
**Scan date (agent):** 2026-09-09  
**Corpus root:** `C:\Project`  
**Cycle date for 90-day rule:** `2026.09.09` → cutoff `2026-06-11` (LastWrite ≥ cutoff → `paused`; else `archive`)  
**mutation_class:** `fs_mutation` (no moves this phase)

## Locked answers (from `01-prompt-betterment/notes.md`)

Q1–Q7 locked via **Choose all**: first subset of **2–3** Medium wrappers; layout Continuity; taxonomy Continuity proposed-ratified (not global final); must-preserve draft untouched; 90-day status; atomic wrapper+nested-`.git`; opaque secrets; plan gate mandatory. Exact shortlist = research/plan output until plan gate.

## Status parents

| Path | Exists | Notes |
| --- | --- | --- |
| `C:\Project\archive` | **Yes** | Cycle 2–3 Early/simple destinations present |
| `C:\Project\paused` | **Yes** | Holds `2026.06.30 - ZedTest` |
| `C:\Project\active` | **No** | Not required for recommended shortlist (all → `archive`) |

## INDEX vs disk (Medium candidates)

All eight INDEX rows still claim root paths — **live-check confirms all still at root**. INDEX proposed date labels match CreationTime for every candidate. Do **not** trust INDEX alone for Early/simple (already moved); those are verify-only below.

## Live-check matrix (all Medium candidates)

| Folder | Exists @ root | CreationTime | Proposed dated name | LastWrite | Within 90d? | Proposed status | Top `.git` | Nested `.git` | `.env` path | Cheap band | Dest collision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NextTest` | Yes | 2025-06-23 09:21:14 | `2025.06.23 - NextTest` | 2025-06-23 09:28:04 | No | **archive** | No | 1: `NextTest\NextTest\.git` | Yes (under nested) | M (~1.58) | None |
| `Simpl` | Yes | 2025-06-05 08:09:23 | `2025.06.05 - Simpl` | 2025-06-05 16:17:42 | No | **archive** | No | 1: `Simpl\Project-Simpl\.git` | Yes (under nested) | S (~0.89) | None |
| `Simpl_Next` | Yes | 2025-06-23 11:10:22 | `2025.06.23 - Simpl_Next` | 2025-06-23 11:26:52 | No | **archive** | No | 1: `Simpl_Next\SimplNext\.git` | Yes | M (~1.75) | None |
| `TestRyan` | Yes | 2025-06-25 10:14:12 | `2025.06.25 - TestRyan` | 2025-06-25 10:14:23 | No | **archive** | No | 1: `TestRyan\python-mini-jeux\.git` | **No** | S (~0.20) | None |
| `ReactRouterTest` | Yes | 2025-08-12 11:08:57 | `2025.08.12 - ReactRouterTest` | 2025-08-12 11:10:17 | No | **archive** | No | 1: `ReactRouterTest\ReactRouterTest\.git` | **No** | S (~0.22) | None |
| `PWAExempleTristan` | Yes | 2025-07-04 15:02:02 | `2025.07.04 - PWAExempleTristan` | 2025-07-04 15:03:07 | No | **archive** | No | 1: `PWAExempleTristan\PWATristan\.git` | Yes | M (~1.58) | None |
| `CursorMobileWorkspace` | Yes | 2026-06-17 08:02:16 | `2026.06.17 - CursorMobileWorkspace` | 2026-06-17 08:04:28 | **Yes** | **paused** | No | 1: `...\CursorMobileWorkspace\.git` | No | M (~11.15) | None |
| `NextPWATraining` | Yes | 2025-06-23 08:03:48 | `2025.06.23 - NextPWATraining` | 2025-06-23 08:26:27 | No | **archive** | No | 1: `...\blogr-nextjs-prisma\.git` | **Yes** (INDEX-flagged) | S (~0.10) | None |

**`.env` path presence only (never opened):**

- `NextTest\NextTest\app-test\.env`
- `Simpl\Project-Simpl\simpl-app\api\env\.env`
- `Simpl_Next\SimplNext\simpl-app\.env`
- `PWAExempleTristan\PWATristan\pwa-tristan-app\.env`
- `NextPWATraining\blogr-nextjs-prisma\.env`

## Nested git hazards (fail-closed screen)

Probed with agent `git` at each nested root (`worktree list --porcelain`, `remote -v`, `.git/worktrees` subdir).

| Folder | Nested path | `.git` type | Extra worktrees? | Remotes | Protocol | Fail-closed? |
| --- | --- | --- | --- | --- | --- | --- |
| NextTest | `NextTest\NextTest` | directory | **No** (single main WT) | 1× `origin` | HTTPS | No |
| Simpl | `Simpl\Project-Simpl` | directory | **No** | 1× `origin` | HTTPS | No (more remote branches; still single remote) |
| Simpl_Next | `Simpl_Next\SimplNext` | directory | **No** | 1× `origin` | HTTPS | No |
| TestRyan | `TestRyan\python-mini-jeux` | directory | **No** | 1× `origin` | HTTPS | No |
| ReactRouterTest | `ReactRouterTest\ReactRouterTest` | directory | **No** | 1× `origin` | HTTPS | No |
| PWAExempleTristan | `PWAExempleTristan\PWATristan` | directory | **No** | 1× `origin` | HTTPS | No |
| CursorMobileWorkspace | `CursorMobileWorkspace\CursorMobileWorkspace` | directory | **No** | 1× `origin` | HTTPS | No (optional must-preserve draft) |
| NextPWATraining | `NextPWATraining\blogr-nextjs-prisma` | directory | **No** | 1× `origin` | **SSH** (`git@github.com:...`) | Soft defer preferred (SSH + flagged `.env` + optional must-preserve) — not a hard worktree/multi-remote abort |

**None** of the eight show linked multi-worktree layouts or multi-remote configs. Atomic move unit = **whole top-level wrapper** including the single nested `.git`.

## Wrapper structure (move unit)

Each candidate is a **thin wrapper** with exactly one child folder containing the nested repo:

| Wrapper | Sole child | Move unit |
| --- | --- | --- |
| `NextTest` | `NextTest\` | Whole `C:\Project\NextTest` |
| `Simpl` | `Project-Simpl\` | Whole `C:\Project\Simpl` |
| `Simpl_Next` | `SimplNext\` | Whole `C:\Project\Simpl_Next` |
| `TestRyan` | `python-mini-jeux\` | Whole `C:\Project\TestRyan` |
| `ReactRouterTest` | `ReactRouterTest\` | Whole `C:\Project\ReactRouterTest` |
| `PWAExempleTristan` | `PWATristan\` | Whole `C:\Project\PWAExempleTristan` |
| `CursorMobileWorkspace` | `CursorMobileWorkspace\` | Whole `C:\Project\CursorMobileWorkspace` |
| `NextPWATraining` | `blogr-nextjs-prisma\` | Whole `C:\Project\NextPWATraining` |

## Early/simple INDEX honesty (out of Medium move scope — verify-only)

| Name | INDEX path present | Root absent | Action |
| --- | --- | --- | --- |
| AngularTest / epsic / IA / PlayTestTristan / PostManResponses / ZedTest | Yes under `archive`/`paused` | Yes | **verify-only** — never re-move |

## Must-preserve / protect (do not touch)

| Path | Relevance |
| --- | --- |
| Org repo under `2026.09.09 - Organisation` | **protect** — out of scope |
| `must-preserve.md` draft | Medium candidates **not** locked preserve; **optional** draft mentions `CursorMobileWorkspace` and `NextPWATraining` → prefer defer those for first subset |
| Must-preserve draft list | Untouched this cycle (Q4=A) |

## Catalogue / program paths that matter

| Path | Why |
| --- | --- |
| `catalogue/INDEX.md` | Medium rows still root/`TBD`; update only approved moved rows after implementer |
| `catalogue/inventory.md` | Size bands + thin-wrapper-1git class align with live-check |
| `catalogue/taxonomy.md` | CreationTime date labels; wrapper = move unit; Continuity |
| `catalogue/must-preserve.md` | Optional CursorMobile / NextPWATraining → soft defer |
| `program/ROADMAP.md` | Medium wrappers = Primary next after Early/simple Complete |
| `sessions/2026.09.09-1032/`, `sessions/2026.09.09-1517/` | Prior Move-Item + verify/rollback patterns |

## Hazard ranking (simpler → defer)

1. **Lowest:** `TestRyan`, `ReactRouterTest` — S, no `.env`, single nested HTTPS git, archive, no collisions  
2. **Low:** `Simpl` — S, single nested HTTPS; opaque `.env` path present (OK under Q6)  
3. **Medium later:** `NextTest`, `Simpl_Next`, `PWAExempleTristan` — M and/or `.env`; still structurally fine  
4. **Prefer defer this cycle:** `CursorMobileWorkspace` (paused parent + larger M + optional must-preserve), `NextPWATraining` (SSH + INDEX-flagged `.env` + optional must-preserve)
