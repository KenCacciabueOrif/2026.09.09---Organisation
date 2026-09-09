# Codebase findings — Cycle 2 Early/simple subset (fs_mutation)

**Session:** `sessions/2026.09.09-1032/02-research/`  
**Scope:** read-only pre-check of three folders under `C:\Project` (no moves).  
**Scan time:** 2026-09-09 (agent research phase).

## Program / catalogue anchors

| Path | Why it matters |
| --- | --- |
| `program/ROADMAP.md` | Early/simple is primary next move row; six-folder list; per-batch approval gate. |
| `program/CHARTER.md` | Org protect; move-capable cycle shape. |
| `catalogue/taxonomy.md` | Canonical `yyyy.mm.dd - ShortName`; CreationTime wins; status axis separate (`active`/`paused`/`archive`). Layout sketch shows `archive\2025.10.01 - PostManResponses\` (illustrative). |
| `catalogue/INDEX.md` | Current paths + proposed labels for all three; Status still `TBD`; Git root? `no`. |
| `catalogue/inventory.md` | CreationTime / LastWrite / size band / no-git class used for subset + ZedTest paused rule. |
| `catalogue/must-preserve.md` | Draft list — **none** of the three batch folders appear; org repo locked protect. |
| `sessions/2026.09.09-1032/01-prompt-betterment/refined-prompt.md` | Locked three-row move map + acceptance criteria. |
| `sessions/2026.09.09-1032/01-prompt-betterment/notes.md` | Gate glossary; status rule (archive default; LastWrite within 90d of 2026.09.09 → paused). |

## Source folder verification (disk)

| Source | Exists | CreationTime (FS) | LastWriteTime (FS) | Proposed label date | Contents class | Size (approx) | Top-level `.git` | Nested `.git` (recurse) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `C:\Project\PostManResponses` | yes | 2025-10-01 08:30:54 | 2025-10-01 08:31:08 | `2025.10.01` ✓ matches | Single HTML snippet (`response.html`) | ~39 KB | **no** | **none** |
| `C:\Project\PlayTestTristan` | yes | 2025-06-23 15:20:25 | 2025-06-23 15:20:46 | `2025.06.23` ✓ matches | Zip + extract: `RPG Textuel\` + `RPG Textuel.zip` | ~0.18 MB (~193 KB files) | **no** | **none** |
| `C:\Project\ZedTest` | yes | 2026-06-30 14:03:11 | 2026-07-01 09:38:42 | `2026.06.30` ✓ matches | Small Python scrape experiment (`scraper.py`, `sample.html`, `results.json`, `.pytest_cache`) | ~2 KB files | **no** | **none** |

**CreationTime vs catalogue:** All three FS CreationTime dates match inventory / proposed INDEX labels (day granularity). No date-label correction needed for this batch.

**Status rule check (notes.md):** Cycle date `2026.09.09`; 90-day window ≈ from `2026.06.11`.

- PostManResponses LastWrite `2025-10-01` → outside → **archive** ✓  
- PlayTestTristan LastWrite `2025-06-23` → outside → **archive** ✓  
- ZedTest LastWrite `2026-07-01` → inside (~70 days) → **paused** ✓  

## Destination parents

| Path | Exists (2026-09-09 research) |
| --- | --- |
| `C:\Project\archive` | **no** — must create before archive moves |
| `C:\Project\paused` | **no** — must create before ZedTest move |
| `C:\Project\active` | **no** — not required for this subset |

## Target collision check

| Proposed destination | Exists? |
| --- | --- |
| `C:\Project\archive\2025.10.01 - PostManResponses` | **no** |
| `C:\Project\archive\2025.06.23 - PlayTestTristan` | **no** |
| `C:\Project\paused\2026.06.30 - ZedTest` | **no** |

No name collisions under missing parents either (parents absent).

## Dependencies / move unit

- **Unit = whole top-level folder tree** for each of the three (no sibling paths to co-move).
- **PlayTestTristan:** keep `RPG Textuel\` and `RPG Textuel.zip` together under one dated wrapper (do not split zip from extract).
- **ZedTest:** include `.pytest_cache` as part of the tree (opaque cache; do not delete to “clean”).
- **No `.env` observed** at top level of these three (no need to open secrets).
- **Not must-preserve** per draft; **org repo** (`C:\Project\2026.09.09 - Organisation\…`) must remain untouched.
- **Deferred Early/simple (do not touch):** `IA`, `AngularTest`, `epsic` — still at root current paths in INDEX.

## Catalogue update implications (for planner, not executed here)

After moves, `catalogue/INDEX.md` rows for the three need:

- Status → `archive` / `archive` / `paused`
- Date label → applied (drop “proposed”)
- Current path → new destinations
- Deferred Early/simple rows unchanged

`inventory.md` paths / notes should be refreshed if the plan requires inventory currency for moved rows.

## Fail-closed git note

Re-scan at implementer pre-flight still required. Research found **no** `.git` at top level or nested under any of the three. If a `.git` appears later → skip that item + log (no inventing git-strategy).

## Push / publish

Not in scope for corpus FS moves (`mutation_class: fs_mutation` only). No agent remote push expected.
