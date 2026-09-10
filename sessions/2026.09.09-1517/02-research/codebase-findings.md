# Codebase findings — Cycle 3 Early/simple remaining

**Session:** `sessions/2026.09.09-1517/02-research/`  
**Scan date (agent):** 2026-09-09  
**Corpus root:** `C:\Project`  
**Cycle date for 90-day rule:** `2026.09.09` → cutoff `2026-06-11`

## Locked answers (from `01-prompt-betterment/notes.md`)

Q1–Q6 locked via **Choose** / **Choose all**: layout Continuity with Cycle 2; batch = IA + AngularTest + epsic; taxonomy Early/simple binding; must-preserve draft untouched; 90-day status rule; Cycle 2 verify/rollback. Plan gate still required.

## Status parents

| Path | Exists | Notes |
| --- | --- | --- |
| `C:\Project\archive` | **Yes** | Created Cycle 2; children: `2025.06.23 - PlayTestTristan`, `2025.10.01 - PostManResponses` |
| `C:\Project\paused` | **Yes** | Created Cycle 2; child: `2026.06.30 - ZedTest` |
| `C:\Project\active` | **No** | Not required for this batch (all three → `archive`) |

## In-scope sources (verified)

| Folder | Exists at root | CreationTime | Proposed label | LastWriteTime | Within 90d of 2026.09.09? | Proposed status | Top `.git` | Nested `.git` (recurse) | Collision at dest |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `IA` | Yes `C:\Project\IA` | 2025-12-12 09:37:17 | `2025.12.12 - IA` | 2025-12-12 09:38:14 | No | **archive** | No | 0 | No — `C:\Project\archive\2025.12.12 - IA` absent |
| `AngularTest` | Yes `C:\Project\AngularTest` | 2025-08-07 08:13:07 | `2025.08.07 - AngularTest` | 2025-08-07 08:18:40 | No | **archive** | No | 0 | No — `C:\Project\archive\2025.08.07 - AngularTest` absent |
| `epsic` | Yes `C:\Project\epsic` | 2025-12-10 08:03:40 | `2025.12.10 - epsic` | 2025-12-17 16:38:32 | No | **archive** | No | 0 | No — `C:\Project\archive\2025.12.10 - epsic` absent |

CreationTime labels match catalogue INDEX hypotheses and inventory rows.

## Move unit (whole tree)

| Folder | Top-level contents | Inventory band | Move unit |
| --- | --- | --- | --- |
| `IA` | `Teams-Messages\` | S (~0.01) | Whole `IA` directory |
| `AngularTest` | `first-app_01-hello-world\` + `first-app_01-hello-world.zip` | M (~5.21) | Whole `AngularTest` (zip + extract together) |
| `epsic` | `BDD\`, `HTML\`, `BDD.zip` | M (~22.79) | Whole `epsic` (zip + extract together) |

## ZedTest re-verify (do not re-move)

| Check | Result |
| --- | --- |
| `C:\Project\ZedTest` | **Absent** (not drifted back to root) |
| `C:\Project\paused\2026.06.30 - ZedTest` | **Present** — matches INDEX |
| Top `.git` | No |
| Payload sample | `.pytest_cache\`, `results.json`, `sample.html`, `scraper.py` |

**Catalogue:** INDEX Current path already correct — **no corrective move**; catalogue-only touch only if other fields change (not required for path drift).

## Cycle 2 destinations (out of move scope)

- `C:\Project\archive\2025.10.01 - PostManResponses` — present
- `C:\Project\archive\2025.06.23 - PlayTestTristan` — present

## Catalogue / program paths that matter

| Path | Why |
| --- | --- |
| `catalogue/INDEX.md` | Current paths for IA / AngularTest / epsic still root; status TBD; ZedTest already paused |
| `catalogue/inventory.md` | Size bands S/M/M; CreationTime/LastWrite align with disk; Early/simple list |
| `catalogue/taxonomy.md` | Layout + CreationTime + spaces; Early/simple user-validated continuity |
| `catalogue/must-preserve.md` | Batch names not listed; draft hands-off (Q4=A) |
| `program/ROADMAP.md` | Early/simple primary row; remaining three called out in INDEX “What’s next” |
| `sessions/2026.09.09-1032/` | Cycle 2 prior art: parents created; Move-Item pattern; verify/rollback |

## Fail-closed `.git`

Recursive scan found **no** `.git` directories or `.git` files under IA, AngularTest, or epsic. Implementer must re-scan immediately before each move.
