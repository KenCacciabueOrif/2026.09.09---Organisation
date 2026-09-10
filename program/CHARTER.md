# Program charter — C:\Project organisation

**Cycle framing:** 0+1 docs (charter / catalogue deepen); physical moves not started  
**Host repo:** `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`  
**Corpus:** `C:\Project`  
**Living navigation:** [`catalogue/INDEX.md`](../catalogue/INDEX.md)

## Purpose / end-state

Across multiple full-agent-workflow (FAW) cycles, produce:

1. A **dated view** of what happened under `C:\Project`.
2. A clear sense of **what would be next** (actionable triage).
3. **Easy navigation** across projects (index + eventual status×date layout).

Choosing and refining the organisation method is part of the program. Material that is organised stays under `C:\Project`. Index, charter, roadmap, and catalogue docs live in this organisation repo.

## Non-goals

- Do **not** break project functionality or lose information.
- Do **not** perform unsupervised filesystem mutation under `C:\Project`.
- Cycle 0 does **not** finish physical organisation of the corpus.
- Cycle 0 does **not** require publish/`git push` of organisation artefacts.

## Safety

| Rule | Detail |
| --- | --- |
| Docs cycles (0–1) FS | **Zero** moves, renames, or deletes under `C:\Project` (org-repo docs only). |
| Later moves | Agent-executed **only after per-batch user approval**. |
| Secrets | Never open/read `.env` or credential **contents**. Path presence may be noted. On move, treat secrets as **opaque payload**. |
| Deps / caches | Do not deep-document `node_modules` / build-cache trees. When moving a project, **include** them so functionality is preserved. |
| Fail-closed | Prefer stop over risky moves when must-preserve or git strategy is unclear. |

## Atomic git units

Each folder that contains its own `.git` is one **project / atomic unit**. Do not split a git root across moves without an explicit plan. Linked worktrees (e.g. Obsidian) must be handled as a coordinated set after a dedicated git-strategy cycle.

## Default-protect / must-preserve

**Default-protect** (locked):

`C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`

Do not casually batch-move this path. Draft candidates beyond default-protect: [`../catalogue/must-preserve.md`](../catalogue/must-preserve.md) (**draft — not auto-locked**; user reviews before the first move-capable cycle).

## Cycle model

- Rounds are **adaptive** (no fixed N), sliced primarily by **top-level folder** under `C:\Project`.
- Each move-capable cycle: classify → propose batch map → **user approves** → agent executes → update `catalogue/INDEX.md`.
- Insert a dedicated **multi-repo git-strategy planning** FAW cycle **before** any cycle that relocates git roots, worktrees, or multi-root containers.

Suggested order and gates: [`ROADMAP.md`](ROADMAP.md). Approach options: [`organisation-approach.md`](organisation-approach.md).

## How to invoke the next cycle

1. Open Agent chat in this organisation repo.
2. Run `/full-agent-workflow` (or equivalent full-cycle request).
3. State a goal that references the next suggested slice in [`ROADMAP.md`](ROADMAP.md) (e.g. Early/simple batch after approval, or git-strategy before complex git moves).
4. A new `sessions/yyyy.mm.dd…` folder will hold that cycle’s artefacts.

## Artefact home rule

| Kind | Home |
| --- | --- |
| Organised *material* | Under `C:\Project` (when moves happen in later cycles) |
| *Outputs / index / docs* | This organisation repo (`program/`, `catalogue/`, `sessions/`) |

## Open decisions (post–Cycle 1)

1. User sign-off of taxonomy (**proposed-ratified**) and review/edit of [`../catalogue/must-preserve.md`](../catalogue/must-preserve.md) draft.
2. Which Early/simple subset becomes the first approved move batch.
3. Keep vs split multi-project containers; zip sidecar policy; root orphan ownership; empty-parent (`HTTP Battles`) classify-before-move.

**Locked (do not re-open):** status axis `active`/`paused`/`archive` (+ INDEX `protect`/`hygiene`) — not PARA-lite; ShortName keeps spaces; **CreationTime wins** for proposed labels; wrapper = canonical label / nested `.git` = child atomic units.
