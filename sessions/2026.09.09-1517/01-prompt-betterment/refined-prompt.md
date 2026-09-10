# Refined prompt — Cycle 3 Early/simple remaining (fs_mutation)

**Session:** `sessions/2026.09.09-1517/`  
**mutation_class:** `fs_mutation`  
**Cycle:** Cycle 3 — Early/simple (**remaining**)  
**Answers:** Q1–Q6 locked via user **Choose** / **Choose all** (see `notes.md`).

**Taxonomy (Q3=A):** Cycle 1/2 proposed-ratified rules are **binding for Early/simple** renames/moves; may note continuity of **user-validated for Early/simple (2026.09.09)** — **not** global final corpus ratification. Status: **proposed-ratified — ready for user sign-off**.  
**Must-preserve (Q4=A):** draft list untouched (**draft — not auto-locked / for user review**); batch folders are **not** must-preserve; org repo **protect**.

## Goal

Finish the Early/simple ROADMAP row for folders still at the corpus root:

1. Research **in-scope** folders (existence, unexpected `.git`, target collisions, parent folders) and **re-verify ZedTest** current path (INDEX may lag; do not double-move if already under `paused`).
2. Planner writes an explicit **batch move map** + verify/rollback (`fs_mutation`).
3. **Mandatory plan gate:** user explicitly approves that map in-session (Choose all / starting this FAW / prior Cycle 2 approval is **not** sufficient).
4. Implementer moves **only** approved paths, creates status parents if missing, updates catalogue (`INDEX.md`, inventory as needed), logs each move with reverse-move notes.
5. Auditor checks acceptance criteria below.

### In-scope batch (Q2=A — locked)

| Source (expected) | Status (Q5=A — research confirms) | Target hypothesis (research confirms CreationTime) |
| --- | --- | --- |
| `C:\Project\IA` | per 90-day rule (catalogue LastWrite → likely `archive`) | `C:\Project\archive\2025.12.12 - IA` |
| `C:\Project\AngularTest` | per 90-day rule (likely `archive`) | `C:\Project\archive\2025.08.07 - AngularTest` |
| `C:\Project\epsic` | per 90-day rule (likely `archive`) | `C:\Project\archive\2025.12.10 - epsic` |

Statuses and exact date labels are **research/plan outputs** under the locked 90-day rule (cycle date `2026.09.09`). The table is a catalogue hypothesis — **not** a user-approved move map.

**ZedTest:** research must confirm location (expected `C:\Project\paused\2026.06.30 - ZedTest`). If still at `C:\Project\ZedTest`, plan may include a corrective move; if already moved, catalogue-only fix if INDEX lags — **no** redundant move.

**Already done (out of move scope):** PostManResponses, PlayTestTristan (archive); ZedTest (paused) from Cycle 2.

## Constraints

- Layout (Q1=A): `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\` (create parents if missing).
- Naming: catalogue CreationTime labels; spaces kept.
- Status rule (Q5=A): default `archive`; LastWrite within 90 days of `2026.09.09` → `paused`.
- **Fail-closed** on unexpected `.git` (skip that item; log; do not invent git-strategy).
- **Mandatory plan gate** with explicit batch map approval before any move.
- **Do not touch:** organisation repo; must-preserve draft paths; hygiene orphans; other ROADMAP rows; Cycle 2 destinations (except catalogue corrections).
- No history rewrite; no agent remote push/pull expected.
- Secrets/deps opaque; prefer move/rename over delete+copy; never delete payload to “clean up.”

## Context pointers

- `program/ROADMAP.md`, `program/CHARTER.md`
- `catalogue/INDEX.md`, `catalogue/taxonomy.md`, `catalogue/must-preserve.md`, `catalogue/inventory.md`
- Prior sessions: `sessions/2026.09.09-1009/` (Cycle 1), `sessions/2026.09.09-1032/` (Cycle 2 moves)
- Locked answers: `sessions/2026.09.09-1517/01-prompt-betterment/notes.md`

## Acceptance criteria / verification

**Before implementer:**

- [ ] `notes.md` Answers lock Q1–Q6 (no open “Choose”).
- [ ] Plan contains the exact move map (or user-edited map) and declares `fs_mutation`.
- [ ] User explicitly approved that plan/map in-session (**plan gate**).
- [ ] Research noted: sources exist; targets absent; `.git` re-scan; ZedTest location verified.

**After implementer (auditor-checkable) — Q6=A:**

- [ ] Exactly the approved folders moved once; no extras outside the approved map.
- [ ] Pre: sources existed; targets did not; unexpected `.git` → item skipped + logged (fail-closed).
- [ ] Post: sources absent; targets present at approved paths.
- [ ] Parents under `C:\Project\{archive|paused|active}` exist as needed.
- [ ] `catalogue/INDEX.md` Status / date label / **current path** updated for moved rows; ZedTest path accurate if it was wrong.
- [ ] Inventory (or equivalent) updated if the plan required it.
- [ ] Implementation log lists each `from → to` and **reverse-move** notes; skips explained.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied if plan required); cycle not marked complete with unmet AC.

## Out of scope

- Re-moving Cycle 2 archive/paused folders that are already correct
- Medium / multi-experiment / Obsidian / ProjetOrif / hygiene batches
- Git-strategy planning cycle
- Claiming global final taxonomy or must-preserve ratification without explicit user sign-off language
- Agent git push/pull

## Handoff note for researcher / planner / implementer

All **Choose** / **Choose all** decisions are locked in `notes.md` Answers — do not re-ask or re-litigate.  
Planner: `ready_to_implement: no` until user plan-gate approval; then implementer only.  
Research: re-verify ZedTest path; confirm CreationTime and LastWrite for the three; propose final status per Q5 rule.  
**Choose all did not approve moves** — only scope and rules for this cycle.
