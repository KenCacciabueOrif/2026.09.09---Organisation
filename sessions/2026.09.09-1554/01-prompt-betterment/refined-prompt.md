# Refined prompt — Cycle 5 Medium wrappers (remaining, fs_mutation)

**Session:** `sessions/2026.09.09-1554/`  
**mutation_class:** `fs_mutation`  
**Cycle:** Cycle 5 — Medium wrappers (**remaining**)  
**ROADMAP row:** Medium wrappers — **in progress** (do **not** jump Primary next; do **not** reopen Early/simple or re-move Cycle 4 archives)  
**Answers:** Q1–Q4 locked via user **Choose all** (see `notes.md`).

**Taxonomy (Q3=A):** Continuity of Cycle 1–4 proposed-ratified rules **for Medium this cycle**; status **proposed-ratified — ready for user sign-off** — **not** global final corpus ratification.  
**Must-preserve (Q3=A):** draft list untouched (**draft — not auto-locked / for user review**); remaining Medium candidates are **not** must-preserve; org repo **protect**.

## Goal

Continue the Medium wrappers ROADMAP row with a **safer-three remaining subset** (never re-propose Cycle 4 moves; soft-defer higher-risk pair):

1. Research the **in-scope pool** at `C:\Project` root (existence, nested `.git`, worktrees/multi-remote hazards, target collisions, parent folders). **Live-check INDEX vs disk**; ignore stale INDEX paths when deciding this batch. Note soft-deferred peers remain at root (do not move them).
2. Under Q1=A + Q2=A + Q4=A: propose **2–3** from `NextTest`, `Simpl_Next`, `PWAExempleTristan` — **typically all three** if live-check is green; shrink only on fail-closed hazards (do not silently fill with soft-deferred names).
3. Planner writes an explicit **batch move map** + verify/rollback (`fs_mutation`), including atomic wrapper+nested-`.git` moves.
4. **Mandatory plan gate:** user explicitly approves that map in-session (Choose all / Continuity / starting this FAW is **not** sufficient).
5. Implementer moves **only** approved paths, creates status parents if missing, updates catalogue (`INDEX.md`, inventory as needed), logs each move with reverse-move notes.
6. Auditor checks acceptance criteria below.
7. After the batch: update `program/ROADMAP.md` Notes — Medium row stays **in progress** with remaining soft-deferred names (`NextPWATraining`, `CursorMobileWorkspace`) unless user later expands scope.

### Remaining at root (orchestrator)

| Source (expected) | Role this cycle |
| --- | --- |
| `C:\Project\NextTest` | **In-scope pool** |
| `C:\Project\Simpl_Next` | **In-scope pool** |
| `C:\Project\PWAExempleTristan` | **In-scope pool** |
| `C:\Project\CursorMobileWorkspace` | **Soft-deferred (Q2=A)** — do not move |
| `C:\Project\NextPWATraining` | **Soft-deferred (Q2=A)** — do not move; `.env` opaque if ever included later |

**Already moved / forbidden as sources:** `TestRyan`, `ReactRouterTest`, `Simpl` (Cycle 4 → archive). Do not re-propose.

**In-scope batch (Q1=A / Q2=A / Q4=A — locked):** research/plan targets **2–3** from the safer three (prefer **all three** when green). Exact destinations/statuses are **research/plan outputs** until **plan gate** approval — Choose all does **not** approve the from→to map.

Statuses and exact date labels use the locked 90-day rule (cycle date `2026.09.09`).

## Constraints

- Layout (Q3=A Continuity): `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\` (create parents if missing).
- Naming: CreationTime wins for date labels; spaces kept; wrapper is the dated move unit.
- Nested git (Q3=A): move **entire top-level wrapper including nested `.git`** atomically; **no** history rewrite / filter-repo; **no** splitting wrapper from nested repo.
- Status rule (Q3=A): default `archive`; LastWrite within 90 days of `2026.09.09` → `paused`; research proposes per folder.
- Secrets (Q3=A Continuity): do not read `.env` / credentials; include them in any move; deps opaque. (NextPWATraining not in this batch.)
- Hazards: worktrees / multi-remote / unclear git strategy → **fail-closed** — skip/defer that item; do **not** start a dedicated git-strategy FAW inside this cycle; do **not** substitute soft-deferred folders to “fill quota.”
- **Fail-closed** on unexpected conditions; log skips.
- **Mandatory plan gate** with explicit batch map approval before any move.
- **Do not touch:** organisation repo; must-preserve draft paths; hygiene orphans; multi-experiment / Obsidian / ProjetOrif / special-git rows; Cycle 4 / Early/simple destinations (except catalogue path honesty if INDEX lags); soft-deferred `NextPWATraining` / `CursorMobileWorkspace`.
- No agent remote push/pull expected.
- Prefer move/rename over delete+copy; never delete payload to “clean up.”

## Context pointers

- `program/ROADMAP.md`, `program/CHARTER.md`
- `catalogue/INDEX.md`, `catalogue/taxonomy.md`, `catalogue/must-preserve.md`, `catalogue/inventory.md`
- Prior Medium first subset: `sessions/2026.09.09-1535/` (Cycle 4 Choose-all Continuity)
- Prior Early/simple: `sessions/2026.09.09-1032/` (Cycle 2), `sessions/2026.09.09-1517/` (Cycle 3)
- Locked answers: `sessions/2026.09.09-1554/01-prompt-betterment/notes.md`
- Prompt tips: `sessions/2026.09.09-1554/01-prompt-betterment/online-prompt-tips.md`

## Acceptance criteria / verification

**Before implementer:**

- [ ] `notes.md` Answers lock Q1–Q4 (no open “Choose” / no blanks).
- [ ] Research live-checked in-scope candidates on disk; INDEX vs disk noted; Cycle 4 archives and soft-deferred pair not treated as move sources.
- [ ] In-scope shortlist is explicit in the plan: 2–3 from `NextTest`, `Simpl_Next`, `PWAExempleTristan` only (prefer all three if green).
- [ ] Plan contains the exact move map (or user-edited map), declares `fs_mutation`, and states atomic nested-git handling.
- [ ] Hazard items deferred with reason (fail-closed), not silently forced; soft-deferred names not silently added.
- [ ] User explicitly approved that plan/map in-session (**plan gate**).

**After implementer (auditor-checkable) — Q3=A Continuity verify:**

- [ ] Exactly the approved folders moved once; no extras outside the approved map; no Cycle 4 re-moves; no soft-deferred moves.
- [ ] Pre: sources existed; targets did not; each moved wrapper still contains its nested `.git` (if present pre-move).
- [ ] Post: sources absent; targets present at approved paths; nested `.git` intact under new path.
- [ ] Unexpected hazards → item skipped + logged (fail-closed).
- [ ] Parents under `C:\Project\{archive|paused|active}` exist as needed.
- [ ] `catalogue/INDEX.md` Status / date label / **current path** updated for moved rows.
- [ ] Inventory (or equivalent) updated if the plan required it.
- [ ] `program/ROADMAP.md` Notes updated: remaining Medium names include soft-deferred pair (row not Complete solely from this subset).
- [ ] Implementation log lists each `from → to` and **reverse-move** notes; skips explained.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied if plan required); cycle not marked complete with unmet AC.

## Out of scope

- Reopening Early/simple finished scope
- Re-moving / re-proposing `TestRyan`, `ReactRouterTest`, `Simpl`
- Moving `NextPWATraining` or `CursorMobileWorkspace` this cycle (Q2=A)
- Jumping to Multi-experiment / Primary next while Medium soft-deferred names remain
- Multi-experiment / Obsidian / ProjetOrif / hygiene / special-git batches
- Dedicated git-strategy planning cycle
- Claiming global final taxonomy or must-preserve ratification without explicit user sign-off language
- Agent git push/pull
- Reading or logging secret file contents
- History rewrite / splitting nested git from wrapper

## Non-goals

- Redesigning taxonomy from scratch
- Fixing all INDEX drift outside this batch’s rows (beyond live-check honesty for decisions)
- Completing the entire Medium wrappers ROADMAP row in this cycle (higher-risk pair deferred)
