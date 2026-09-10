# Plan

## Goal

Create a personal Markdown notes area in the organisation repository: a root-level folder `Notes/` containing only a short `Notes/README.md` that states purpose, how to add a note, the recommended `yyyy.mm.dd-topic.md` filename pattern, and that this folder is not catalogue/corpus/session storage. Working-tree create only — no sample notes, no commit/push, and no edits to `program/`, `catalogue/`, `.cursor/`, or root `README.md`.

## Mutation class

| Field | Value |
| --- | --- |
| Class | `docs_only` |
| Corpus FS | **Zero intentional corpus FS mutations** — no moves/renames/deletes under `C:\Project`, `catalogue/`, or any ROADMAP batch. Only create `Notes/` + `Notes/README.md` inside this organisation git root. |
| User approval before implementer | **Not required** for the corpus / first-move plan gate (this is not an `fs_mutation` move batch). Orchestrator may proceed to implementer after plan hand-off. |
| First-move gates | **N/A** — not a corpus Early-simple / first-move batch; taxonomy and must-preserve untouched. |
| Taxonomy / must-preserve | **N/A** — do not update; do not claim proposed-ratified or draft lock. |

### Why `docs_only` (not `fs_mutation`)

Workflow `fs_mutation` means corpus path mutations (moves/renames/deletes or other catalogue-backed path changes) that need a mandatory user plan gate. This cycle only **creates documentation scaffolding** in the org repo (`Notes/README.md`). That is intentional disk write, but it is **not** a corpus FS batch. Implementer will attest: no paths outside `Notes/` were created or edited (except session logs already owned by FAW), and no git commit/push.

If a future cycle moves/renames corpus content into or out of `Notes/`, that cycle must use `fs_mutation` with a full path map and plan gate.

### What the user is approving

**Plan-gate pause: not applicable** for this cycle (docs_only / non-corpus create). No separate “approve moves” ask is required before implementer.

For transparency (informational only — not a blocking gate):

- **What will happen on disk:** Create `c:\LocalProjects\2026.09.09---Organisation\Notes\` and write `Notes/README.md`. Nothing else at repo root.
- **What will not happen:** No sample notes; no root README edit; no `program/` / `catalogue/` / `.cursor/` edits; no commit; no push; no `C:\Project` changes.
- **Pros:** Dedicated place for personal `.md` notes with a clear naming habit; README tracks the folder in git without `.gitkeep`.
- **Cons / tradeoffs:** Root `README.md` architecture table will not list `Notes/` until a later optional ask; users discovering the repo only from the root README may miss the folder until then.

## Acceptance criteria

- [ ] Directory `Notes/` exists at organisation repo root (`c:\LocalProjects\2026.09.09---Organisation\Notes\`).
- [ ] File `Notes/README.md` exists and briefly covers: purpose (user `.md` notes); how to add (new `.md` in this folder); recommended pattern `yyyy.mm.dd-topic.md`; reminder this is **not** catalogue/corpus reorganisation storage (and preferably ≠ FAW `sessions/*/notes.md` artifacts).
- [ ] No other new files under `Notes/` (no sample notes, no `.gitkeep`).
- [ ] No changes to `program/` (including `ROADMAP.md`), `catalogue/`, `.cursor/`, or root `README.md`.
- [ ] Working tree only — implementer performed **no** `git commit` and **no** `git push`.
- [ ] If `Notes/` already existed at implement time: implementer **stopped and asked** — did not overwrite or merge silently.
- [ ] Verification recorded: list `Notes/` contents; confirm README sections above by reading the file.

## Steps

1. **Pre-create existence check** — path: `c:\LocalProjects\2026.09.09---Organisation\Notes` (also treat case-variant root `notes` / `Note` / `note` as collision if present) — action: `Test-Path` / list; if exists → **stop**, report to orchestrator/user, do not write — verify: clear path before any create.
2. **Create folder** — path: `Notes/` at org repo root — action: create directory only — verify: directory exists.
3. **Write README** — path: `Notes/README.md` — action: write a short README modeled on length/tone of `sessions/README.md`, covering the four content bullets in AC; do not add sample note files — verify: file exists; content includes purpose, how-to-add, `yyyy.mm.dd-topic.md`, and not-catalogue/corpus reminder.
4. **Scope attestation** — paths: repo root siblings — action: confirm git status / path checks show only `Notes/` (+ expected session docs); no edits under `program/`, `catalogue/`, `.cursor/`, root `README.md` — verify: attestation in `04-implementation/log.md` or `changes.md`.
5. **No publish** — action: do **not** run commit or push (push/auth dual preflight **N/A**) — verify: no new commit created by this cycle’s implementer.

## Non-goals

- Sample/welcome note files, templates engines, scripts, apps, CMS, search tooling
- Editing root `README.md` (optional one-line pointer deferred)
- Any `catalogue/` / `program/` / ROADMAP / taxonomy / must-preserve / Early-simple work
- Corpus moves, renames, deletes under `C:\Project` or elsewhere
- Committing, pushing, or opening a PR
- Placing notes under `sessions/` or inventing a separate `docs/` top-level area

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| `Notes/` appears between research and implement | Step 1 stop-and-ask; do not overwrite |
| Scope creep into root README or workflow files | Explicit non-goals + attestation step |
| Accidental commit/push | AC forbids; implementer must not invoke commit/push |
| Confusing with `sessions/*/notes.md` | README states personal notes ≠ session FAW artifacts |
| Rollback | Delete `Notes/README.md` and empty `Notes/` if unused; no other files should exist to clean |

## Push / auth

**N/A** — create only; dual preflight skipped. `blocker_type`: none.

## Ready to implement

**yes**

## Blocking questions

none
