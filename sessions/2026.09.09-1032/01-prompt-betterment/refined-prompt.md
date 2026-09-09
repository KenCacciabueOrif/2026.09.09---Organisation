# Refined prompt — Cycle 2 Early/simple subset (fs_mutation)

**Session:** `sessions/2026.09.09-1032/`  
**mutation_class:** `fs_mutation`  
**Cycle:** Cycle 2 — Early/simple (**subset of 3**, not full six)  
**Taxonomy for this cycle:** proposed-ratified rules are **binding** for these renames/moves; after successful cycle docs may note **user-validated for Early/simple (2026.09.09)** (not “final forever” corpus ratification).  
**Must-preserve:** draft list untouched; batch folders are **not** must-preserve; org repo **protect**.

## Goal

Execute the first real move-capable slice of the Early/simple ROADMAP row:

1. Research the **in-scope subset** (existence, unexpected `.git`, target collisions, parent folders).
2. Planner writes an explicit **batch move map** + verify/rollback steps (`fs_mutation`).
3. **Mandatory plan gate:** user explicitly approves that map in-session (prior “do next cycle” / taxonomy consent is **not** sufficient).
4. Implementer moves **only** approved subset paths, creates status parents if missing, updates catalogue (`INDEX.md`, inventory as needed), logs each move with reverse-move notes.
5. Auditor checks acceptance criteria below.

### In-scope batch (locked)

| Source | Status | Target |
| --- | --- | --- |
| `C:\Project\PostManResponses` | `archive` | `C:\Project\archive\2025.10.01 - PostManResponses` |
| `C:\Project\PlayTestTristan` | `archive` | `C:\Project\archive\2025.06.23 - PlayTestTristan` |
| `C:\Project\ZedTest` | `paused` | `C:\Project\paused\2026.06.30 - ZedTest` |

**Why this subset:** smallest/safest first move — S-band / near-zero size, catalogue no-git, low coupling.  
**Deferred (out of this cycle):** `IA`, `AngularTest`, `epsic` — later Early/simple cycle.

**Status rule used:** Early/simple experiments → default `archive`; if LastWrite within 90 days of `2026.09.09` → `paused`. ZedTest LastWrite `2026-07-01` → `paused`; the other two → `archive`.

## Constraints

- Layout: `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\` (create parents if missing).
- Naming: catalogue CreationTime labels; spaces kept.
- **Fail-closed** on unexpected `.git` (skip that item; log; do not invent git-strategy).
- **Mandatory plan gate** with explicit batch map approval before any move.
- **Do not touch:** organisation repo (`C:\Project\2026.09.09 - Organisation\…`); must-preserve draft paths (Obsidian, ProjetOrif, WebCatalogue, WorkSpace, HTTP Battles, optional CursorMobileWorkspace / NextPWATraining, …); deferred Early/simple folders; hygiene orphans; anything outside the approved map.
- No history rewrite; no agent remote push expected.
- Secrets/deps opaque; prefer move/rename over delete+copy; never delete payload to “clean up.”

## Context pointers

- `program/ROADMAP.md`, `program/CHARTER.md`
- `catalogue/INDEX.md`, `catalogue/taxonomy.md`, `catalogue/must-preserve.md`, `catalogue/inventory.md`
- Prior sessions: `sessions/2026.09.09-0929/`, `sessions/2026.09.09-1009/`
- Locked answers: `sessions/2026.09.09-1032/01-prompt-betterment/notes.md`

## Acceptance criteria / verification

**Before implementer:**

- [ ] Plan contains the exact three-row move map (or an edited map the user approved) and declares `fs_mutation`.
- [ ] User explicitly approved that plan/map in-session.
- [ ] Research noted pre-check intent: sources exist; targets absent; `.git` re-scan planned.

**After implementer (auditor-checkable):**

- [ ] Exactly the approved folders moved once; no extras (esp. not IA / AngularTest / epsic).
- [ ] Pre: sources existed; targets did not; unexpected `.git` → item skipped + logged (fail-closed).
- [ ] Post: sources absent; targets present at paths above (or approved edits).
- [ ] Parents `C:\Project\archive` and/or `C:\Project\paused` exist as needed.
- [ ] `catalogue/INDEX.md` Status / date label / **current path** updated for the three; deferred rows unchanged as current paths.
- [ ] Inventory (or equivalent) updated if the plan required it for moved rows.
- [ ] Implementation log lists each `from → to` and **reverse-move** notes; skips explained.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied if plan required); cycle not marked complete with unmet AC.

## Out of scope

- Moving the deferred three Early/simple folders
- Full six-folder batch
- Git-strategy; Obsidian / ProjetOrif / worktree / medium / multi-experiment / hygiene batches
- Editing agent/skill files for the explanations debt (self-improver only)
- Claiming global final taxonomy ratification beyond Early/simple validation note

## Handoff note for researcher / planner / implementer

All **Choose** decisions are locked in `notes.md` Answers — do not re-ask or re-litigate.  
Planner: `ready_to_implement: no` until user plan-gate approval; then implementer only.  
Self-improver: mandatory backlog item — clarifying questions must include plain-language explanations + pros/cons (see `notes.md`).
