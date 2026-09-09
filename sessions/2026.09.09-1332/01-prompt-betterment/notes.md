# Prompt betterment notes

**Phase status:** COMPLETE — Answers locked; `refined-prompt.md` finalized.

**Cycle:** Pull — organisation-repo `git pull` (sync with remote)  
**Mutation class:** `docs_only` (org-repo git ops only; no corpus FS moves/renames/deletes). *Docs_only* here means: no move/rename/delete of catalogue corpus files; git fetch/merge into this repo is allowed.  
**Session:** `sessions/2026.09.09-1332/01-prompt-betterment/`

## Informed consent

Questions were presented with plain-language explanation + pros/cons before the user replied. User answered **"Choose all"** → every Q1–Q7 resolved via disclosed defaults. No jargon-explanation debt.

## Continuity (locked — do not re-ask)

From publish session `sessions/2026.09.09-1246/` (carry into pull AC):

| Lock | Value | Source |
| --- | --- | --- |
| Git root | `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` only — never sibling `C:\Project` trees | Prior Q1 A + this cycle Q4 A |
| Preferred remote/branch | `origin` / `main` (tracking `origin/main`) | Prior prefer + this cycle Q1 A |
| Windows git helper | Prefer Git for Windows + GCM when PATH `git` is MSYS without helper | Prior GfW+GCM |
| Out of scope gates | Taxonomy **proposed-ratified — ready for user sign-off**; must-preserve **draft — not auto-locked** — do **not** block this pull session on those | Orchestrator handoff |

## Clarifying questions (asked; answered via Choose)

### Q1 — Remote/branch — **A**
### Q2 — Combine strategy — **A** (`--ff-only`)
### Q3 — Dirty working tree — **A** (abort)
### Q4 — Git root — **A** (org-repo only)
### Q5 — Who must succeed — **A** (agent Shell)
### Q6 — On failure — **A** (fail-closed)
### Q7 — Session docs — **A** (full artifacts)

(Full informed-consent wording retained in session history / prior notes revision; options A were the disclosed defaults.)

## Answers

| Q | Decision | Source | Rationale |
| --- | --- | --- | --- |
| Q1 | **A** — pull `origin` into `main` / tracking `origin/main` | Choose | Matches prior publish tracking; safest usual sync |
| Q2 | **A** — `git pull --ff-only` | Choose | Fail-closed on divergence; no surprise merge commits |
| Q3 | **A** — abort if dirty working tree; report paths; block | Choose | Avoids overwrite/conflict with local WIP |
| Q4 | **A** — org-repo git root only | Choose | Continuity + hard AC; never sibling `C:\Project` trees |
| Q5 | **A** — agent Shell pull must succeed (dual preflight; GfW if needed) | Choose | FAW discipline; proves agent can sync |
| Q6 | **A** — fail-closed: document, `blocked`, no force/hard reset/`--no-verify`; still run self-improver | Choose | Safe recovery path; clear audit |
| Q7 | **A** — write full session artifacts under `sessions/2026.09.09-1332/` | Choose | Auditor/self-improver can verify pull outcome |

User phrase: **"Choose all"** → Source for each row: `Choose` (equivalent to Choose / unanswered→default on disclosed defaults). **No Choose decision differs from the expected defaults listed by the orchestrator.**

## Assumptions

- Goal is sync-from-remote only (not push, not corpus moves).
- Live remote tip may differ from prior session tip `f5012d6`; researcher/implementer must re-verify.
- Taxonomy / must-preserve pending gates remain out of scope and must not delay pull.
- If already up to date under ff-only with a clean tree, success = verified clean sync (no error).

## Open risks

- Dirty tree or local commits ahead of / diverged from `origin/main` → ff-only or dirty policy blocks (by design).
- Agent git (MSYS vs GfW/GCM) may differ from user terminal → Q5 A may surface `blocker_type: agent_environment` (or `user_credentials` if auth).
- Multi-root workspace → accidental wrong cwd if plan/AC not enforced.

## Self-improvement backlog (if any)

- Add standing **pull-cycle.md** question pack next to `publish-cycle.md` (phase 06 candidate).

## Key alignment changes (raw → refined)

- Raw: “do git pull /full-agent-workflow”
- Refined: Agent-executed `git pull --ff-only` of `origin` into `main`/`origin/main` tracking, **only** inside org-repo git root; abort if dirty; fail-closed on pull failure; full session docs; taxonomy/must-preserve/corpus moves/push out of scope.
