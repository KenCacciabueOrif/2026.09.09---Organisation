# Refined prompt — Cycle 6 Medium wrappers (soft-deferred finalization, fs_mutation)

**Session:** `sessions/2026.09.09-1612/`  
**mutation_class:** `fs_mutation`  
**Cycle:** Cycle 6 — Medium wrappers (**soft-deferred finalization**)  
**ROADMAP row:** Medium wrappers — **in progress — nearly complete** (do **not** jump Primary next until remaining names move or are dropped from scope; do **not** reopen Early/simple; do **not** re-move Cycle 4/5 archives)  
**Answers:** Q1–Q5 locked via user **Choose all** (see `notes.md`). **Plan gate still mandatory** before any moves.

**Taxonomy (Q2=A):** Continuity of Cycle 1–5 proposed-ratified rules **for Medium this cycle**; status **proposed-ratified — ready for user sign-off** — **not** global final corpus ratification.  
**Must-preserve (Q2=A):** draft list untouched (**draft — not auto-locked / for user review**); remaining Medium candidates are **not** must-preserve; org repo **protect**.

## Goal

Finalize the Medium wrappers ROADMAP row by moving the **two soft-deferred remaining** folders (never re-propose Cycle 4/5 archives; do **not** re-soft-defer by default):

1. Research **both** candidates at `C:\Project` root (existence, nested `.git`, worktrees/SSH/multi-remote hazards, target collisions, parent folders, LastWrite for status). **Live-check INDEX vs disk**; ignore stale INDEX paths when deciding this batch.
2. Under Q1=A: propose a move map for **`NextPWATraining`** and **`CursorMobileWorkspace`**. Under Q5=A: if live-check fail-closes **one** item, defer only that item with reason; still plan/gate the green one. Do **not** silently soft-defer both as default.
3. Planner writes an explicit **batch move map** + verify/rollback (`fs_mutation`), including atomic wrapper+nested-`.git` moves and opaque-secret handling (**never read** `NextPWATraining` `.env`).
4. **Mandatory plan gate:** user explicitly approves that map in-session (Choose all / Continuity / starting this FAW is **not** sufficient).
5. Implementer moves **only** approved paths, creates status parents if missing, updates catalogue (`INDEX.md`, inventory as needed), logs each move with reverse-move notes.
6. Auditor checks acceptance criteria below.
7. After successful moves of **both** remaining names: update `program/ROADMAP.md` — mark Medium wrappers **Complete**; next Primary next → **Multi-experiment**. If one deferred (Q5=A), keep Medium **in progress** with the remaining name noted.

### Remaining at root (orchestrator-verified)

| Source (expected) | Role this cycle |
| --- | --- |
| `C:\Project\NextPWATraining` | **Finalize (Q1=A)** — `.env` **opaque / never read**; likely status `archive` under 90-day rule |
| `C:\Project\CursorMobileWorkspace` | **Finalize (Q1=A)** — path-only move; no remote rewrite; likely status `paused` under 90-day rule |

**Already moved / forbidden as sources (do not re-propose):**

- Cycle 4 → archive: `TestRyan`, `ReactRouterTest`, `Simpl`
- Cycle 5 → archive: `NextTest`, `Simpl_Next`, `PWAExempleTristan`

**In-scope batch (Q1=A / Q5=A — locked):** both remaining folders; shrink only if live-check fail-closes one (log + skip that item; still finish the other after plan gate). Exact destinations/statuses are **research/plan outputs** until **plan gate** approval — Choose all does **not** approve the from→to map.

Statuses and exact date labels use the locked 90-day rule (cycle date `2026.09.09`).

## Constraints

- Layout (Q2=A Continuity): `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\` (create parents if missing).
- Naming: CreationTime wins for date labels; spaces kept; wrapper is the dated move unit.
- Nested git (Q2=A): move **entire top-level wrapper including nested `.git`** atomically; **no** history rewrite / filter-repo; **no** splitting wrapper from nested repo; **no** SSH/remote URL rewrite (path-only).
- Status rule (Q3=A): default `archive`; LastWrite within 90 days of `2026.09.09` → `paused`; research proposes per folder (expect CursorMobile ≈ paused, NextPWA ≈ archive unless evidence differs).
- Secrets (Q4=A): **never read or log** `.env` / credentials (especially **NextPWATraining**); include them unread in any move; deps opaque.
- Hazards: worktrees / SSH / multi-remote / unclear git strategy → **fail-closed** — skip/defer that item (Q5=A: at most one); do **not** start a dedicated git-strategy FAW inside this cycle; do **not** re-soft-defer both by default.
- **Fail-closed** on unexpected conditions; log skips.
- **Mandatory plan gate** with explicit batch map approval before any move.
- **Do not touch:** organisation repo; must-preserve draft paths; hygiene orphans; multi-experiment / Obsidian / ProjetOrif / special-git rows; Cycle 4 / Cycle 5 / Early/simple destinations (except catalogue path honesty if INDEX lags).
- No agent remote push/pull expected.
- Prefer move/rename over delete+copy; never delete payload to “clean up.”

## Context pointers

- `program/ROADMAP.md`, `program/CHARTER.md`
- `catalogue/INDEX.md`, `catalogue/taxonomy.md`, `catalogue/must-preserve.md`, `catalogue/inventory.md`
- Prior Medium first subset: `sessions/2026.09.09-1535/` (Cycle 4 Choose-all Continuity)
- Prior Medium remaining: `sessions/2026.09.09-1554/` (Cycle 5 — soft-deferred this pair)
- Prior Early/simple: `sessions/2026.09.09-1032/` (Cycle 2), `sessions/2026.09.09-1517/` (Cycle 3)
- Locked answers: `sessions/2026.09.09-1612/01-prompt-betterment/notes.md`
- Prompt tips: `sessions/2026.09.09-1612/01-prompt-betterment/online-prompt-tips.md`

## Acceptance criteria / verification

**Before implementer:**

- [ ] `notes.md` Answers lock Q1–Q5 (no open “Choose” / no blanks).
- [ ] Research live-checked both candidates on disk; INDEX vs disk noted; Cycle 4/5 archives not treated as move sources.
- [ ] In-scope shortlist is explicit in the plan: `NextPWATraining` and `CursorMobileWorkspace` (both; shrink only on Q5=A fail-closed skip).
- [ ] Plan contains the exact move map (or user-edited map), declares `fs_mutation`, states atomic nested-git + opaque-secret handling, and never requires reading `.env`.
- [ ] Hazard items deferred with reason (fail-closed), not silently forced; no re-soft-defer-both as default.
- [ ] User explicitly approved that plan/map in-session (**plan gate**).

**After implementer (auditor-checkable) — Continuity verify:**

- [ ] Exactly the approved folders moved once; no extras outside the approved map; no Cycle 4/5 re-moves.
- [ ] Pre: sources existed; targets did not; each moved wrapper still contains its nested `.git` (if present pre-move).
- [ ] Post: sources absent; targets present at approved paths; nested `.git` intact under new path.
- [ ] No secret file contents in logs/session docs.
- [ ] Unexpected hazards → item skipped + logged (fail-closed); at most one defer under Q5=A.
- [ ] Parents under `C:\Project\{archive|paused|active}` exist as needed.
- [ ] `catalogue/INDEX.md` Status / date label / **current path** updated for moved rows.
- [ ] Inventory (or equivalent) updated if the plan required it.
- [ ] `program/ROADMAP.md` updated: if **both** remaining moved, Medium row **Complete** and Primary next → **Multi-experiment**; else Notes show remaining name(s) after Q5 skip.
- [ ] Implementation log lists each `from → to` and **reverse-move** notes; skips explained.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied if plan required); cycle not marked complete with unmet AC.

## Out of scope

- Reopening Early/simple finished scope
- Re-moving / re-proposing Cycle 4 or Cycle 5 Medium archives
- Re-soft-deferring both remaining names as the default outcome
- Jumping to Multi-experiment while either remaining Medium name is still in-scope and unmoved
- Multi-experiment / Obsidian / ProjetOrif / hygiene / special-git batches (until Medium Complete)
- Dedicated git-strategy planning cycle (unless user expands)
- Claiming global final taxonomy or must-preserve ratification without explicit user sign-off language
- Agent git push/pull
- Reading or logging secret file contents
- History rewrite / splitting nested git from wrapper / rewriting remote URLs

## Non-goals

- Redesigning taxonomy from scratch
- Fixing all INDEX drift outside this batch’s rows (beyond live-check honesty for decisions)
- Quietly parking both soft-deferred folders again without live-check fail-closed (Q5=A)
