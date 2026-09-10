# Refined prompt

## Goal

Run **Cycle 0 (Program charter)** of a multi-cycle full-agent-workflow program to analyse, classify, and (later) reorganise years of work under `C:\Project`.

**Program end-state (all cycles):** a clear **dated view** of what happened and what would be next, with **easy navigation** across projects. Choosing the best organisation method to achieve that is part of the program. **Must never** break project functionality or lose information.

**This cycle (Cycle 0) delivers only:**

1. A short **program charter** (purpose, non-goals, safety rules, adaptive cycle model).
2. A **coarse inventory** of `C:\Project` (top-level / near-top entries; size/date signals; project vs junk signals; **candidate git roots** via presence of `.git`) — not a full deep tree walk of every file unless cheap and safe. Do **not** inventory `node_modules` / dependency-cache trees in detail.
3. A **draft taxonomy / naming scheme** aligned to user preference: **`yyyy.mm.dd` + project/folder/file name** (same date format as sessions), plus rules for applying it.
4. A **first-cut recommendation** for achieving “dated view + next + navigation” (organisation approach options and a preferred direction) — **without executing moves**.
5. An **adaptive multi-cycle roadmap** sliced primarily by **top-level folder**, with explicit **per-batch user approval** before any agent-executed moves, and a **dedicated planning thread for multi-repo git strategy** before any move cycle that touches git roots.

Cycle 0 documentation/index artefacts live in this **organisation repo**; later physical organisation of material stays under **`C:\Project`** (this repo is already there).

## Constraints

- Host workflow repo: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`
- Corpus root: `C:\Project`
- Follow full-agent-workflow: orchestrator delegates; document under `sessions/2026.09.09-0929/` (later cycles: `sessions/yyyy.mm.dd…`).
- **Zero moves / renames / deletes** under `C:\Project` in Cycle 0.
- Do not change project functionality or lose information in any cycle.
- Prefer small, reviewable diffs in the organisation repo; no secrets in commits or session logs.
- **Inventory detail exclusions:** do not deeply document dependency/cache trees (`node_modules`, typical build/cache dirs, OS junk). Note parent project presence instead.
- **Move semantics (later cycles):** when a project moves, **include** dependency/cache trees and secret files (e.g. `.env`) with the project so functionality is preserved — but **never open/read** secret contents.
- **Secrets:** may record path presence of `.env`-like files; must not open, quote, or commit their contents.
- **Must-preserve paths:** **TBD** (open decision). Until decided, **default-protect** this organisation repo path: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`.
- **Naming / taxonomy:** prefer `yyyy.mm.dd` + descriptive name for organised project/folder/file labels.
- **Later physical work:** agent-executed moves **only after explicit per-batch approval**.
- **Cycle slicing:** by **top-level folder**; number of rounds is **adaptive** (determined as work proceeds), not a fixed N.
- **Artefact home:** organised material remains / will be organised under `C:\Project`; maintain a whole-corpus **index and documentation** in this organisation repo.
- **Git:** many repos under `C:\Project`. Each folder with its own `.git` = its own project / **atomic unit**. Do not split a git root across moves without an explicit plan. Git strategy (remotes, push, history, nested repos) is complex — roadmap must include a **dedicated multi-repo git planning thread** before move cycles that touch git roots. Cycle 0 does **not** require publishing/push of organisation artefacts unless separately requested.
- Inventory must flag **candidate git roots** (`.git` present) at coarse level.

## Context pointers

- Workflow law: `AGENTS.md`, `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/agents/orchestrator.md`
- This cycle session: `sessions/2026.09.09-0929/`
- Prompt-betterment outputs: `sessions/2026.09.09-0929/01-prompt-betterment/`
- Corpus (do not relocate in Cycle 0): `C:\Project`
- User intent: multi-year corpus → **multiple sequential FAW cycles**, not one mega-run

## Acceptance criteria (Cycle 0 only)

- [ ] **Program charter** exists (session and/or durable index docs in this organisation repo) stating: end-state (dated view + next + navigation), non-goals (no functionality loss / no info loss), Cycle 0 vs later cycles, safety (no unsupervised FS mutation), adaptive top-level-folder cycle model, and how to invoke the next cycle.
- [ ] **Inventory artefact** exists: coarse map of `C:\Project` top-level (and useful near-top) entries with metadata (type guess, size/date signals if available, notes); dependency/cache trees not documented in detail; **candidate git roots** identified (`.git` presence); no secret contents pasted.
- [ ] **Taxonomy / naming proposal** exists using `yyyy.mm.dd` + name, with application rules, examples, and remaining ambiguities called out.
- [ ] **Organisation-approach recommendation** exists: options for “dated view + next + easy navigation,” with a first-cut preferred approach — **no moves executed**.
- [ ] **Adaptive multi-cycle roadmap** exists: cycles primarily by **top-level folder**; flexible count; each move-capable cycle has an explicit **user approval gate**; includes a **dedicated multi-repo git strategy planning thread** before any cycle that moves git roots; treats git roots as atomic units.
- [ ] Auditor can verify: **zero** intentional moves/renames/deletes under `C:\Project` attributable to this cycle.
- [ ] Index/documentation of Cycle 0 outputs is maintained in this organisation repo (not only ephemeral chat).

## Out of scope (Cycle 0)

- Relocating, renaming, or deleting anything under `C:\Project`
- Deep inventory of `node_modules` / cache trees
- Opening or quoting `.env` / credential file contents
- Executing project moves (even “small” ones)
- Finalising the full must-preserve path list (document as open; default-protect organisation repo)
- Implementing a complete multi-repo git migration (only plan/flag the thread for later)
- “Organisation finished” as a single-session outcome
- Starting a move cycle inside this FAW without a new cycle after user review

## Suggested later-cycle shape (roadmap to refine)

- **Cycle 1+ (docs):** deepen inventory / ratify taxonomy / flesh organisation approach as needed
- **Git-strategy planning cycle (mandatory before git-root moves):** remotes, atomic moves, history, nested repos, agent vs user push
- **Per top-level-folder cycles:** classify → propose batch move map → **user approves** → agent executes move (including deps/secrets as opaque payload) → update organisation-repo index
- Adaptive: add/split/skip cycles based on inventory findings

## Hand-off for orchestrator

User answers are locked in `notes.md`. Proceed to researcher with this refined prompt; do not re-ask answered questions. Remaining open decision: full must-preserve path list (beyond default-protecting this organisation repo).
