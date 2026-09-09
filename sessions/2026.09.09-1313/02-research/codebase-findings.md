# Codebase findings

**Goal:** Create root `Notes/` + `Notes/README.md` only (ad-hoc; not ROADMAP/corpus).  
**Scan date:** 2026.09.09 — organisation repo root only (coarse).

## Does `Notes/` already exist?

| Check | Result |
| --- | --- |
| `Notes/` at repo root | **No** (`Test-Path` false) |
| `notes/`, `Note/`, `note/` at root | **No** |
| Recursive dirs named `Notes` / `Note` (case-insensitive) | **None** found |
| Product/corpus refs to a root Notes area | **None** in `catalogue/` or `program/` (ROADMAP “Notes” column is table header only) |

**Implication for Q9:** Path is free — implementer may create. Re-verify immediately before create (race with parallel work).

Session-local `*/notes.md` files (prompt-betterment artifacts) are **not** a notes folder and do not conflict.

## Org repo root — coarse map

| Name | Type | Role | Git root? |
| --- | --- | --- | --- |
| `.git/` | dir (hidden) | This organisation repo’s VCS | **Yes — sole git root** |
| `.cursor/` | dir | Agents, skills, rules | no |
| `catalogue/` | dir | Corpus index / inventory / taxonomy / must-preserve | no |
| `program/` | dir | CHARTER, ROADMAP, organisation-approach | no |
| `sessions/` | dir | FAW cycle artifacts + `_templates/` | no |
| `AGENTS.md` | file | Portable project law | — |
| `AGENT-AND-WORKFLOW-BEST-PRACTICES.md` | file | Deeper workflow guide | — |
| `README.md` | file | Repo overview + architecture table | — |

**Not present at root:** `Notes/`, `docs/`, apps, `node_modules`, caches.

**Secrets (path presence only):** No `.env`, credential, or key-like files under tracked top-level areas (scan excluded `.git`; no hits outside session noise). Do not invent contents.

**Deep deps/caches:** None at org root; nothing to deep-document.

## Layout conventions (top-level folders)

- Top-level areas are **purpose-named plural or domain nouns**: `catalogue`, `program`, `sessions` (plus tooling `.cursor`).
- Each documented area tends to have a **short human README or INDEX** at its entry:
  - Root [`README.md`](../../../README.md) — architecture table; lists `.cursor`, `sessions`, `AGENTS.md`, program/catalogue paths; **does not** mention `Notes/`.
  - [`sessions/README.md`](../../../sessions/README.md) — 3 short paragraphs: what the folder is, naming, pointer to templates/skill.
  - `catalogue/` uses `INDEX.md` (not README) as the navigation surface for **C:\Project** corpus work.
  - `program/` has no folder README; docs are named files (`CHARTER.md`, `ROADMAP.md`, …).
- Date style already used in sessions: `yyyy.mm.dd` / `yyyy.mm.dd-HHMM` — aligns with locked note filename habit `yyyy.mm.dd-topic.md`.

## Conflict with catalogue / program / sessions?

| Area | Purpose | Conflict with root `Notes/`? |
| --- | --- | --- |
| `catalogue/` | Durable corpus navigation for `C:\Project` | **No** — different corpus; Notes is personal `.md` scratch in the **org repo** |
| `program/` | Multi-cycle organisation roadmap/charter | **No** — this goal is explicitly **not** a ROADMAP row / Early-simple cycle |
| `sessions/` | Agent cycle documentation | **No** — sessions are workflow artifacts; Notes is user-owned ongoing notes |
| Root `README.md` | Lists known top-level purposes | **Soft gap only** — omitting a one-line pointer this cycle is **allowed** (refined: default do not edit root README) |

Creating `Notes/` does **not** require editing catalogue, program, ROADMAP, or `.cursor/`. Mutation class: small FS create in org repo, **not** corpus move/rename/delete.

## Prior art for README-only folders

- Closest pattern: `sessions/README.md` — purpose + how naming works + where to look next; no sample session content in the README folder itself.
- Refined prompt already locks: README tracks the folder → **no `.gitkeep`**.

## Must-read paths for planner / implementer

- `sessions/2026.09.09-1313/01-prompt-betterment/refined-prompt.md` — AC + constraints
- `sessions/2026.09.09-1313/01-prompt-betterment/notes.md` — locked Q1–Q9
- `README.md` (root) — sibling table style (do not edit unless later asked)
- `sessions/README.md` — brevity model for `Notes/README.md`
- `AGENTS.md` — commit-only-when-asked; not a ROADMAP FS cycle
