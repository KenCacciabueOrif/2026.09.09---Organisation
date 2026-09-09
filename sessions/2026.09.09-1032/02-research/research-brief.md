# Research brief — Cycle 2 Early/simple subset (fs_mutation)

**Session:** `sessions/2026.09.09-1032/02-research/`  
**mutation_class:** `fs_mutation`  
**Publish/push:** not required (corpus local moves only).

## Verdict

All three in-scope sources **exist**, match catalogue CreationTime labels, have **no** top-level or nested `.git`, and proposed destinations are **absent**. Parents `archive` / `paused` **do not exist yet** and must be created. Status assignments in the refined prompt are consistent with the locked 90-day rule. **No research blockers** to planning; moves remain gated on **user plan-map approval**.

## Proposed move map (for planner)

| # | Source | Status | Destination | Notes |
| --- | --- | --- | --- | --- |
| 1 | `C:\Project\PostManResponses` | `archive` | `C:\Project\archive\2025.10.01 - PostManResponses` | Whole tree; 1 HTML file |
| 2 | `C:\Project\PlayTestTristan` | `archive` | `C:\Project\archive\2025.06.23 - PlayTestTristan` | Whole tree incl. `RPG Textuel\` + `.zip` |
| 3 | `C:\Project\ZedTest` | `paused` | `C:\Project\paused\2026.06.30 - ZedTest` | Whole tree incl. `.pytest_cache` |

**Parents to create (if still missing at implement time):**

- `C:\Project\archive`
- `C:\Project\paused`

(`C:\Project\active` not required for this subset.)

**Out of map (do not move):** `IA`, `AngularTest`, `epsic`; must-preserve draft paths; organisation repo; hygiene orphans.

## Recommended approach options (max 3)

### Option A — Direct same-volume `Move-Item` per row (recommended)

Create missing parents → re-scan `.git` / collision → `Move-Item -LiteralPath` source → exact destination path (rename-in-move) → update INDEX (+ inventory if planned) → log reverse paths.

- **Pros:** Fast on same `C:`; whole tree moves atomically per folder; matches Microsoft Move-Item semantics; simple reverse-move.
- **Cons:** Not transactional across the three rows (partial batch possible if #2/#3 fails mid-batch).
- **Mitigation:** Sequential moves; stop on first failure; reverse already-moved items if plan requires Critical rollback.

### Option B — `-WhatIf` dry-run script then live pass

Same as A but run identical commands with `-WhatIf` (or Test-Path checklist) once more after plan approval, then live.

- **Pros:** Extra confirmation layer for user-visible safety.
- **Cons:** Slightly more steps; still needs live re-check of existence/collision.

### Option C — Copy-verify-delete per folder

Copy tree → verify counts/sizes → delete source.

- **Pros:** Stronger if cross-volume or flaky media.
- **Cons:** Unnecessary on same volume; doubles disk briefly; higher chance of leaving duplicates if delete skipped; conflicts with “prefer move/rename over delete+copy” in refined prompt.
- **Not recommended** for this subset.

**Recommended:** **Option A**, with Option B’s pre-checks embedded (Test-Path + `.git` re-scan) without requiring a separate dry-run phase unless the user asks.

## Required facts

- Sources exist; CreationTimes match proposed dates.
- No `.git` found (top or nested) — fail-closed re-scan still mandatory at implementer start.
- Targets absent; parents absent → create.
- PlayTestTristan dependency = keep zip + extract together (whole folder).
- ZedTest → paused justified by LastWrite `2026-07-01` within 90 days of `2026.09.09`.
- Catalogue INDEX still shows Status `TBD` and root current paths for all three.
- Plan gate still required; prior “do next cycle” ≠ map approval.

## Unknowns / residual risks (non-blocking)

| Risk | Severity | Handling |
| --- | --- | --- |
| `.git` appears between research and move | Medium | Skip that item; log; do not invent git-strategy |
| File lock / open handle | Low (tiny trees) | Retry once or skip+log |
| Partial batch (1 of 3 moved) | Medium | Reverse-move notes per row; Critical → reverse as plan requires |
| Parent name collision with future unrelated files named `archive`/`paused` | Low now (absent) | Create as directories only |
| INDEX/inventory drift if docs update fails after FS move | Medium | Treat catalogue update as same acceptance batch |

## Blockers

**none** for research → planning.

Process gates (not research blockers):

- User must explicitly approve the three-row plan/map before implementer.
- Implementer must re-verify sources exist, targets absent, no unexpected `.git`.

### Push/auth dual preflight

**N/A** — goal does not include `git push` / remote publish for corpus moves.

| Field | Value |
| --- | --- |
| Remote URL scheme | n/a |
| Tracking branch | n/a |
| Agent git / GCM | n/a |
| `blocker_type` | none (publish not in scope) |

## Rollback notes (for planner to encode)

For each successful move, reverse is:

| Forward | Reverse |
| --- | --- |
| `…\PostManResponses` → `…\archive\2025.10.01 - PostManResponses` | Move back to `C:\Project\PostManResponses` |
| `…\PlayTestTristan` → `…\archive\2025.06.23 - PlayTestTristan` | Move back to `C:\Project\PlayTestTristan` |
| `…\ZedTest` → `…\paused\2026.06.30 - ZedTest` | Move back to `C:\Project\ZedTest` |

Do **not** delete payload to undo. Empty `archive`/`paused` parents may remain after reverse (harmless) or be left as created.

## Canonical references

- `sessions/2026.09.09-1032/01-prompt-betterment/refined-prompt.md`
- `sessions/2026.09.09-1032/01-prompt-betterment/notes.md`
- `catalogue/taxonomy.md`, `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/must-preserve.md`
- `program/ROADMAP.md`
- Microsoft Learn Move-Item — https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item
- PARA archive principle — https://fortelabs.com/blog/para/
- Sibling artefacts: `codebase-findings.md`, `online-findings.md`
