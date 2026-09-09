# Refined prompt

**Status:** LOCKED — user answered Choose all; phase-1 decisions recorded in `notes.md`.

## Goal

Create a personal Markdown notes area in this organisation repository: a root-level folder `Notes/` with a short `README.md` so the user can add `.md` notes using a clear, documented convention.

## Constraints

- Ad-hoc goal only — **not** a `program/ROADMAP.md` corpus-organisation cycle; do **not** lock ROADMAP rows; do **not** move/rename existing corpus files.
- Create **only**:
  - `Notes/` at repo root (`c:\LocalProjects\2026.09.09---Organisation\Notes\`)
  - `Notes/README.md` (purpose, how to add notes, recommended filenames, what not to put there)
- Do **not** add sample/welcome note files, scripts, templates engines, or apps.
- Do **not** edit `.cursor/`, `program/`, `catalogue/`, or other top-level areas except as needed to create `Notes/`.
- Do **not** commit or push (working-tree changes only).
- If `Notes/` already exists: **stop and ask** — do not overwrite or merge silently.

## Context pointers

- Repo root: `c:\LocalProjects\2026.09.09---Organisation\`
- Sibling areas: `.cursor/`, `catalogue/`, `program/`, `sessions/`, `AGENTS.md`, `README.md`
- Session: `sessions\2026.09.09-1313\01-prompt-betterment\`
- Decisions: `sessions\2026.09.09-1313\01-prompt-betterment\notes.md`

## Acceptance criteria

- [ ] Directory `Notes/` exists at the organisation repo root.
- [ ] File `Notes/README.md` exists and includes, briefly:
  - purpose (place for user `.md` notes),
  - how to add a note (create a new `.md` file in this folder),
  - recommended filename pattern `yyyy.mm.dd-topic.md`,
  - reminder this is not catalogue/corpus reorganisation storage.
- [ ] No other new files under `Notes/` (no sample notes, no `.gitkeep` required because README tracks the folder).
- [ ] No changes to `program/ROADMAP.md`, catalogue layout, or `.cursor/` workflow files.
- [ ] Working tree only — no git commit and no push performed by the agent.
- [ ] If `Notes/` pre-existed before this cycle: implementer stopped and reported instead of overwriting.
- [ ] Verification: list `Notes/` and confirm README sections above are present (read file / path check).

## Out of scope

- Notes apps, CMS, search tooling, or automation beyond creating the folder + README
- Catalogue / corpus moves, renames, deletes, or inventory cycles
- ROADMAP / Early-simple / taxonomy / must-preserve work from other sessions
- Committing, pushing, or opening a PR
- Changing root `README.md` unless a later explicit ask requires a one-line pointer (default: **do not** edit root README this cycle)
