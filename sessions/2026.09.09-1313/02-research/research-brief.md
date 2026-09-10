# Research brief

## Recommended approach

**Option 1 (recommended):** Create only `Notes/` at organisation repo root and a short `Notes/README.md` covering purpose, how to add a `.md` note, recommended `yyyy.mm.dd-topic.md` filenames, and explicit “not catalogue/corpus/session storage.” Re-check path absence immediately before create; if present, stop and ask (Q9). Working tree only — no commit/push. Do not edit root README, `catalogue/`, `program/`, `.cursor/`, or ROADMAP.

## Options considered

1. **Root `Notes/` + README only (locked / recommended)**  
   - Pros: Matches Choose-all; README tracks folder; mirrors `sessions/README.md` brevity; zero collision with existing paths.  
   - Cons: Root README won’t list `Notes/` until a later optional one-liner.

2. **Same create + one-line pointer in root `README.md`**  
   - Pros: Discovers Notes from the architecture table.  
   - Cons: Out of default refined scope; extra surface for auditor; defer unless user asks.

3. **Place notes under `sessions/` or invent `docs/`**  
   - Pros: None relative to locked Q1–Q2.  
   - Cons: Conflates FAW artifacts or invents a new top-level area; **rejected** by phase-1 answers.

## Required facts

- `Notes/`, `notes/`, `Note/`, `note/` **do not exist** at repo root; no recursive `Notes`/`Note` dirs found.
- Org root layout: `.cursor`, `catalogue`, `program`, `sessions` + root law/README files; **one** git root (`.git`).
- `catalogue/` / `program/` do not define a personal Notes area; ROADMAP “Notes” is a table column name only.
- Refined locks: create-only; no sample notes; no `.gitkeep`; no commit/push; not a ROADMAP/corpus move cycle.
- Date-first filenames align with existing session naming (`yyyy.mm.dd`).
- No secret-like paths at org root (presence scan empty for common patterns).

## Unknowns / blockers

| Item | Status |
| --- | --- |
| Path collision at implement time | **Re-verify** before create (currently clear) |
| User later wants singular/`notes` rename | Open risk only — follow-up cycle |
| Root README discovery gap | Accepted; optional later |
| Corpus / ROADMAP gates | **N/A** — not this cycle |
| Push/auth dual preflight | **Not required** — refined prompt: create only, **no commit/push**. Do **not** treat missing dual preflight as a blocker. Table below marked N/A. |

### Push/auth dual preflight

**Status: SKIPPED (N/A)** — goal explicitly excludes commit and push. Dual agent push preflight was **not** run and is **not** a planning or implementation blocker.

| Field | Value |
| --- | --- |
| Remote URL scheme | n/a (no publish) |
| Tracking branch | n/a |
| Agent git path | n/a — not evaluated |
| Agent `credential.helper` | n/a |
| Prefer GfW path (Windows HTTPS)? | n/a |
| GCM / non-interactive evidence | n/a — not run |
| `gh` present? | n/a (optional signal only; irrelevant) |
| User-terminal push note | n/a |
| `blocker_type` | **none** (publish not in scope) |
| Blocker / remediation | None for auth. Proceed on create-only path. |

## Risks and blockers (planning)

| Item | Severity | Notes |
| --- | --- | --- |
| Pre-existing `Notes/` at implement time | Medium if occurs | Stop and ask; do not overwrite |
| Scope creep into ROADMAP/catalogue | Low | Refined + notes.md forbid; planner must keep `docs_only`-ish / small create |
| Accidental commit/push | Low | Explicit AC forbid; implementer must not git commit |
| Confusing Notes with `sessions/*/notes.md` | Low | README should say personal notes ≠ session artifacts |

**Blockers for planning: none.**

## Canonical references

- GitHub Docs — About READMEs — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes — short purpose/how-to READMEs
- Directory-README pattern — https://kody-w.github.io/2026/04/24/directory-readme-pattern/ — belongs / does-not-belong / naming in folder README
- Stack Overflow — empty folders in git — https://stackoverflow.com/questions/14541253/commit-empty-folder-structure-with-git — README vs `.gitkeep`
- LetCodes — `.gitkeep` — https://letcodes.com/git/git-keep — prefer documenting README when intent matters
- Local: `sessions/README.md`, root `README.md`, `01-prompt-betterment/refined-prompt.md`, `01-prompt-betterment/notes.md`

## Hand-off for planner

- Mutation: create `Notes/` + `Notes/README.md` only; not corpus FS move batch; no mandatory ROADMAP plan-gate for moves.
- Verification: path list + README section presence; confirm no extra files under `Notes/`; confirm no edits outside create path (and no git commit).
- Suggested README model: length/tone of `sessions/README.md`; include the four AC bullets from refined prompt.
