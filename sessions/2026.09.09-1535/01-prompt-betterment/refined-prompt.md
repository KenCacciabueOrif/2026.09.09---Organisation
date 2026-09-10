# Refined prompt — Cycle 4 Medium wrappers (first subset, fs_mutation)

**Session:** `sessions/2026.09.09-1535/`  
**mutation_class:** `fs_mutation`  
**Cycle:** Cycle 4 — Medium wrappers (**first subset**)  
**ROADMAP row:** Medium wrappers (Primary next — Early/simple **Complete**, do not reopen)  
**Answers:** Q1–Q7 locked via user **Choose all** (see `notes.md`).

**Taxonomy (Q3=A):** Continuity of Cycle 1/2/3 proposed-ratified rules **for Medium this cycle**; status **proposed-ratified — ready for user sign-off** — **not** global final corpus ratification.  
**Must-preserve (Q4=A):** draft list untouched (**draft — not auto-locked / for user review**); Medium candidates are **not** must-preserve; org repo **protect**.

## Goal

Start the Medium wrappers ROADMAP row with a **small first move batch** (not all eight):

1. Research **candidate** folders at `C:\Project` root (existence, nested `.git`, worktrees/multi-remote hazards, target collisions, parent folders). Live-check INDEX vs disk; **ignore** stale Early/simple INDEX paths when deciding this batch.
2. Under Q1=A, **propose which 2–3** wrappers to include (prefer lower hazard / simpler single-nested git; avoid deferring the whole batch for one hard item).
3. Planner writes an explicit **batch move map** + verify/rollback (`fs_mutation`), including atomic wrapper+nested-`.git` moves.
4. **Mandatory plan gate:** user explicitly approves that map in-session (Choose all / Continuity / starting this FAW is **not** sufficient).
5. Implementer moves **only** approved paths, creates status parents if missing, updates catalogue (`INDEX.md`, inventory as needed), logs each move with reverse-move notes. Secrets (esp. NextPWATraining `.env` if in batch) stay **opaque** (move without reading).
6. Auditor checks acceptance criteria below.

### Candidate set (orchestrator — all still at root per bootstrap)

| Source (expected) | Notes |
| --- | --- |
| `C:\Project\NextTest` | Medium wrapper; nested git expected |
| `C:\Project\Simpl` | Medium wrapper; nested git expected |
| `C:\Project\Simpl_Next` | Medium wrapper; nested git expected |
| `C:\Project\TestRyan` | Medium wrapper; nested git expected |
| `C:\Project\ReactRouterTest` | Medium wrapper; nested git expected |
| `C:\Project\PWAExempleTristan` | Medium wrapper; nested git expected |
| `C:\Project\CursorMobileWorkspace` | Medium wrapper; nested git expected |
| `C:\Project\NextPWATraining` | Medium wrapper; nested git expected; **`.env` opaque** |

**In-scope batch (Q1=A — locked):** research proposes **2–3** from the table above (prefer simpler / lower hazard). Exact shortlist is a **research/plan output** until **plan gate** approval — Choose all does **not** pick the three folders or approve destinations.

Statuses and exact date labels are **research/plan outputs** under the locked 90-day rule (cycle date `2026.09.09`). Any table of targets in the plan is a hypothesis until **plan gate** approval.

**Already done / out of move scope:** Early/simple Cycle 2–3 destinations; do not re-open that row. Remaining Medium candidates not in the approved shortlist stay at root for a later cycle.

## Constraints

- Layout (Q2=A): `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\` (create parents if missing).
- Naming: CreationTime wins for date labels; spaces kept; wrapper is the dated move unit.
- Nested git (Q2=A / Q6=A): move **entire top-level wrapper including nested `.git`** atomically; **no** history rewrite / filter-repo; **no** splitting wrapper from nested repo.
- Status rule (Q5=A): default `archive`; LastWrite within 90 days of `2026.09.09` → `paused`; research proposes per folder.
- Secrets (Q6=A): do not read `.env` / credentials; include them in the move; deps opaque.
- Hazards (Q6=A): worktrees / multi-remote / unclear git strategy → **fail-closed** — skip/defer that item; do **not** start a dedicated git-strategy FAW inside this cycle.
- **Fail-closed** on unexpected conditions; log skips.
- **Mandatory plan gate** with explicit batch map approval before any move.
- **Do not touch:** organisation repo; must-preserve draft paths; hygiene orphans; multi-experiment / Obsidian / ProjetOrif / special-git rows; Early/simple destinations (except catalogue path honesty if INDEX lags).
- No agent remote push/pull expected.
- Prefer move/rename over delete+copy; never delete payload to “clean up.”

## Context pointers

- `program/ROADMAP.md`, `program/CHARTER.md`
- `catalogue/INDEX.md`, `catalogue/taxonomy.md`, `catalogue/must-preserve.md`, `catalogue/inventory.md`
- Prior Early/simple sessions: `sessions/2026.09.09-1032/` (Cycle 2), `sessions/2026.09.09-1517/` (Cycle 3)
- Locked answers: `sessions/2026.09.09-1535/01-prompt-betterment/notes.md`
- Prompt tips: `sessions/2026.09.09-1535/01-prompt-betterment/online-prompt-tips.md`

## Acceptance criteria / verification

**Before implementer:**

- [ ] `notes.md` Answers lock Q1–Q7 (no open “Choose” / no blanks).
- [ ] Research live-checked candidates on disk; INDEX vs disk noted; Early/simple stale INDEX paths not treated as Medium sources.
- [ ] In-scope **2–3** shortlist is explicit in the plan (with rationale: simpler / lower hazard).
- [ ] Plan contains the exact move map (or user-edited map), declares `fs_mutation`, and states atomic nested-git + opaque-secrets handling.
- [ ] Hazard items deferred with reason (fail-closed), not silently forced; shortlist does not silently expand past plan-gate visibility.
- [ ] User explicitly approved that plan/map in-session (**plan gate**).

**After implementer (auditor-checkable) — Q7=A:**

- [ ] Exactly the approved folders moved once; no extras outside the approved map.
- [ ] Pre: sources existed; targets did not; each moved wrapper still contains its nested `.git` (if present pre-move).
- [ ] Post: sources absent; targets present at approved paths; nested `.git` intact under new path.
- [ ] NextPWATraining (if in batch): `.env` present at destination if it existed at source; no evidence of secret contents in session logs.
- [ ] Unexpected hazards → item skipped + logged (fail-closed).
- [ ] Parents under `C:\Project\{archive|paused|active}` exist as needed.
- [ ] `catalogue/INDEX.md` Status / date label / **current path** updated for moved rows.
- [ ] Inventory (or equivalent) updated if the plan required it.
- [ ] Implementation log lists each `from → to` and **reverse-move** notes; skips explained.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied if plan required); cycle not marked complete with unmet AC.

## Out of scope

- Reopening Early/simple finished scope
- Moving all eight Medium wrappers this cycle (Q1=A)
- Multi-experiment / Obsidian / ProjetOrif / hygiene / special-git batches
- Dedicated git-strategy planning cycle
- Claiming global final taxonomy or must-preserve ratification without explicit user sign-off language
- Agent git push/pull
- Reading or logging secret file contents
- History rewrite / splitting nested git from wrapper

## Non-goals

- Redesigning taxonomy from scratch
- Fixing all INDEX drift outside this batch’s rows (beyond live-check honesty for decisions)
- Completing the entire Medium wrappers ROADMAP row in one cycle
