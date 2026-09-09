# Prompt betterment notes

**Status:** Answers locked. User said **Choose all** (Q1–Q9); phase-1 decided each option below. Refined prompt is complete.

**Informed-consent record:** Clarifying questions were asked with plain-language explanations and pros/cons before answers. User delegated all picks via Choose — decisions documented here with one-line rationales (user may disagree later).

**Program continuity (locked — do not re-ask):**
- Ad-hoc goal, **not** a `program/ROADMAP.md` corpus-organisation cycle.
- Do **not** lock a ROADMAP row; do **not** treat as Early/simple move batch.
- Prior taxonomy / must-preserve gates from other sessions: **out of scope** unless the user conflates them.
- Prior session for this goal: none.

---

## Clarifying questions

*(Full option tables with explanations/tradeoffs remain in session history / prior revision; summary of asks: Q1 name, Q2 path, Q3 starters, Q4 naming habit, Q5 done checks, Q6 non-goals, Q7 good/bad, Q8 git, Q9 conflict.)*

---

## Answers

| Q | Locked pick | Rationale (one line) |
| --- | --- | --- |
| **Q1** Folder name | **A. `Notes`** | Plural collection name is clearer than singular `Note` for many `.md` files. |
| **Q2** Location | **A. Repo root** → `Notes/` at organisation repo root | Easiest to find; keeps personal notes out of `sessions/` and `catalogue/`. |
| **Q3** Starters | **B. README only** | Documents purpose without sample clutter; reversible docs default over extra note files. |
| **Q4** Naming habit | **B. Date-first** → recommend `yyyy.mm.dd-topic.md` in README | Matches existing session date style; convention-only (no auto-rename). |
| **Q5** Done | **B. Path + README “how to add”** | Matches Q3; checkable handoff beyond “folder exists.” |
| **Q6** Non-goals | **A. Accept defaults** | Keeps cycle to minimal folder+README; no app/moves/ROADMAP/`.cursor`/taxonomy. |
| **Q7** Good vs bad | **Confirm Good A** | Success = `Notes/` + short README; rest of repo unchanged. |
| **Q8** Git | **A. Create files only; no commit** | Most reversible; matches project “commit only when asked”; user can commit later. |
| **Q9** If exists | **A. Stop and ask** | Fail-safe; no overwrite if path already present. |

### Non-goals locked (from Q6)

- Do not invent a notes app, templates system, or scripts.
- Do not move/rename existing corpus files.
- Do not change `program/ROADMAP.md` or run a ROADMAP cycle.
- Do not edit `.cursor/` agents/skills/rules unless explicitly requested later.
- Do not treat this as taxonomy / must-preserve work from other sessions.

## Continuity (locked — do not re-ask)

- Ad-hoc notes-folder goal; **not** a ROADMAP / corpus-organisation cycle.
- Do not lock ROADMAP rows; do not run Early/simple move batches.
- Path locked: `Notes/` at repo root with `Notes/README.md` only (plus conflict stop).
- Git: working-tree create only — no commit, no push this cycle.

## Assumptions

- Quick root scan found no existing `Note*` folder; researcher/implementer still re-verify before create (Q9).
- README is short: purpose, how to add notes, recommended date-first filenames, what not to put there.
- Mutation class: small FS create (`docs`-ish starter + folder), not corpus `fs_mutation` move batch — no plan-gate pause beyond normal FAW unless planner flags otherwise.

## Open risks

- User may prefer singular `Note` or lowercase `notes` after seeing the result — rename would be a follow-up.
- If `Notes/` already exists with content, cycle stops per Q9 (not a soft reuse).

## Self-improvement backlog (if any)

- None: questions had explanations; Choose-all resolved in-phase without leaving defaults for later agents.

## Key alignment changes (raw → refined)

- Raw “Note folder” → locked **`Notes/`** at **repo root**.
- Implied empty place → **README-only** starter with **date-first** naming guidance.
- Git unspecified → **create only, no commit/push**.
- Explicitly **not** ROADMAP/corpus/taxonomy work.
