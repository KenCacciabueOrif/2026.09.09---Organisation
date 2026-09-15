# Research brief — Cycle 14 Multi-experiment (`WorkSpace` only / Appendix A)

**Session:** `sessions/2026.09.11/02-research/`  
**Goal:** STAGE 1 evidence for Continuity **B** — planner `fs_mutation` map to relocate intact `_backups` and `_quarantine` parent trees out of live `C:\Project\WorkSpace` per `program/git-strategy-workspace-hazards.md`.  
**Not this phase:** implementer, corpus moves, docs_only re-attest as cycle outcome, whole-tree archive, peer reopen, publish/pull.

## One-line outcome

Live re-probe confirms sources still under WorkSpace, destinations free, nested **7** with **1+1** clone roots inside the two parents; recommend **Option A — Continuity B `fs_mutation` Appendix A move map** (plan gate held in Hermes). Whole-tree clearance remains **NO**.

---

## Key evidence for Appendix A move map

| Field | Live evidence (2026-09-11) |
| --- | --- |
| Probe method | Shell `Test-Path`, recursive `.git` discovery, `git remote -v` / `worktree list` / `ls-files`, size bands |
| Source `_backups` | `C:\Project\WorkSpace\TestNewWorkspaceAgent\_backups` — **exists** (~1662 MB) |
| Source `_quarantine` | `C:\Project\WorkSpace\TestNewWorkspaceAgent\_quarantine` — **exists** (~1662 MB) |
| Nested `.git` in sources | 1 under backups + 1 under quarantine (directory `.git`); move with parents |
| Expect after both moves | Nested count **7→5**; ~**3.3 GB** out of live tree |
| Live primaries `#1–#5` | All present — **keep in place** |
| Suggested dest parent | `C:\Project\archive\hygiene\` (**absent** — free to create) |
| Suggested leaves (re-dated) | `…\2026.09.11 - WorkSpace-_backups` and `…\2026.09.11 - WorkSpace-_quarantine` (**absent**). Cycle 10 `2026.09.10 - …` names also absent (hints only) |
| Already-at-dest? | **No** — sources still live under WorkSpace; hygiene leaves absent → **move map valid** (not verify-only / catalogue-only) |
| Remotes on clones | `origin` + `cada` HTTPS — document only; **no rewrite** |
| HEAD class | Live hermes `4fbff573…` ≠ clones `8d60d929…` (unchanged) |
| Linked worktrees | None unexpected on live/backup/quarantine hermes |
| Opaque `.env*` | **17** total unread; **5** in backups + **5** in quarantine move with parents |
| Parent index coupling | `TestNewWorkspaceAgent` tracks **1157** `_backups` + **1150** `_quarantine` paths → expect post-move dirty parent WT; disclose; do not auto-commit/rewrite |

### Proposed from→to (for planner — destinations free)

| Unit | From | To (recommended; free as of probe) |
| --- | --- | --- |
| Backups parent | `C:\Project\WorkSpace\TestNewWorkspaceAgent\_backups` | `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_backups` |
| Quarantine parent | `C:\Project\WorkSpace\TestNewWorkspaceAgent\_quarantine` | `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_quarantine` |

Create `archive\hygiene` if missing. Prefer whole-parent `Move-Item` (or equivalent); on Windows lock → reunify + `robocopy /E /MOVE` per strategy rule 6.

---

## Clearance status

| Scope | Status |
| --- | --- |
| Whole-tree WorkSpace | **NO** — classified ≠ cleared; never recommend whole-tree archive this cycle |
| Scoped Appendix A (`_backups` + `_quarantine`) | **Ready for plan draft** under Continuity B; **execute blocked** until Hermes plan-gate yes |
| Live hermes multi-remote | **Uncleared** even after isolation |

---

## Recommended approach options (max 3)

### Option A (recommended): Continuity B — `fs_mutation` Appendix A move map

- Planner produces `mutation_class: fs_mutation` with exact from→to above (or equivalent free dated hygiene leaves), full “What the user is approving” intent-preview, cites safe rules 1–10, Windows lock recovery, opaque `.env*` unread list, remotes unchanged, nested 7→5, parent dirty disclosure, Multi-experiment stays in progress / Remaining WorkSpace only.  
- Orchestrator STAGE 1 **stops at plan gate** (Hermes); no implementer in this run.  
- Pros: Matches locked Continuity B; shrinks live XL tree; removes unexpected clone roots from live tree; grounded in live probe + strategy artifact.  
- Cons: Real FS risk (~3.3 GB Windows move); bookmarks under old paths break; parent TNA index dirtiness; live multi-remote remains.

### Option B: Docs_only re-attest / continue-strategy only

- Rejected as **cycle path** — Cycles 10–13 already re-attested no material delta four times; Continuity B forbids this as the chosen outcome. (Honesty updates after a future execute remain fine.)

### Option C: Whole-tree WorkSpace archive or Primary-next jump

- **Rejected** — clearance NO; ROADMAP law; refined-prompt AC; never Complete while WorkSpace remains; never reopen Medium/peers.

**Rejected always:** remote rewrite; history rewrite; delete backup/quarantine by default; cherry-pick empty `.git` shells; move live primaries `#1–#5`; agent PATH/credential chores as Continuity requirements.

---

## Planner guidance (STAGE 1)

| Requirement | Detail |
| --- | --- |
| Mutation class | `fs_mutation` |
| Scope | Named parents `_backups` + `_quarantine` only |
| Intent-preview | from→to, size bands (~1662 MB each), nested-git expectation 7→5, opaque `.env*` path list unread, remotes unchanged, parent TNA dirty after move, pros/cons |
| Encode | Atomic intact nested-git; no remote rewrite; no history rewrite; no whole-tree archive; keep primaries; row stays in progress |
| Cite | Strategy safe relocation rules **1–10** + Windows lock-recovery path |
| Destinations | Re-validated free this research; prefer Cycle 14 dated names under `archive\hygiene\` |
| `ready_to_implement` | May be `yes` for completeness; orchestrator **does not** launch implementer (Hermes gate) |
| Taxonomy / must-preserve | Keep **proposed-ratified** / **draft** wording; Q3=A waive re-litigation |
| INDEX after future execute | Update honesty for WorkSpace still at root; optionally note hygiene isolation destinations — do not claim WorkSpace archived |

---

## Required facts

- ROADMAP lock: Multi-experiment remaining **WorkSpace only** — in progress / not Complete.  
- Strategy artifact is authoritative for fate + rules.  
- Continuity B ≠ plan-gate approval.  
- Taxonomy proposed-ratified; must-preserve draft.  
- Org-repo session docs only this STAGE; zero corpus FS mutation in phases 1–3.  
- Push/pull dual preflight: **N/A** (no agent remote sync this cycle).

## Unknowns / blockers

| Item | Status |
| --- | --- |
| Destination free | **Clear** — hygiene parent + dated leaves absent |
| Source present | **Clear** — both parents still under WorkSpace |
| Whole-tree clearance | **Blocked** (constraint — out of scope, not a research fail) |
| Plan-gate execute | **Blocked until Hermes yes** (expected STAGE 1 hold) |
| Linked worktrees | **None** now; re-probe at execute time |
| Parent index dirty after move | **Known risk** — disclose; not a Continuity abort by itself |
| Auth / dirty_working_tree (org-repo pull) | **N/A** this cycle |

### Push / pull dual preflight

**N/A** — refined prompt excludes publish/pull.

---

## Risks

- Windows locks on ~1.6 GB parents → follow rule 6 robocopy recovery; never delete non-empty leftover `.git`.  
- Scope creep to whole-tree or live primaries.  
- Framing isolation as Multi-experiment Complete / multi-remote cleared.  
- Silent remote rewrite or history rewrite on clones or parent.  
- Auto-committing parent TNA deletions without a later gate.  
- Quoting `.env*` contents in session docs.  
- Using Cycle 10 dated dest names without re-check (re-check done; prefer 2026.09.11 dating).

---

## Canonical references

- `program/git-strategy-workspace-hazards.md`  
- `sessions/2026.09.11/01-prompt-betterment/refined-prompt.md`  
- `sessions/2026.09.11/01-prompt-betterment/notes.md`  
- `sessions/2026.09.11/02-research/codebase-findings.md`  
- `sessions/2026.09.11/02-research/online-findings.md`  
- `sessions/2026.09.10-0907/03-plan/plan.md` (Appendix A illustrative)  
- `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/must-preserve.md`  
- `program/ROADMAP.md`  
- https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
- https://git-scm.com/docs/git-remote.html  
- https://git-scm.com/docs/git-worktree.html  
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy
