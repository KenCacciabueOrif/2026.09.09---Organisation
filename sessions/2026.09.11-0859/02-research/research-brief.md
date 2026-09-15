# Research brief — Cycle 15 Multi-experiment (`WorkSpace` only / live hermes multi-remote)

**Session:** `sessions/2026.09.11-0859/02-research/`  
**Goal:** STAGE 1 evidence for Continuity **Q1=B** — inventory live hermes `origin`+`cada` and evidence-pick **one** safe remediation (or fail-closed + minimal gated unblock).  
**Not this phase:** implementer, corpus path moves, docs_only re-attest theater, whole-tree archive, peer reopen, publish/pull.

## One-line outcome

Live hermes at `…\hermes-agent` still has **two HTTPS remotes**: **`origin`** = active NousResearch hermes upstream; **`cada`** = reachable but **wrong-repo** pointer to parent `TestNewWorkspaceAgent` (unrelated histories; no branch tracks it). Recommend **Option A — gated `git remote remove cada`** on live hermes only (`fs_mutation` / remote-config; not docs_only).

---

## Key evidence

| Field | Live evidence |
| --- | --- |
| Probe method | `Test-Path`; nested `.git` discovery; GfW `git remote -v` / `branch -vv` / `worktree list` / `ls-remote` / merge-base / tree samples |
| INDEX WorkSpace path | `C:\Project\WorkSpace` **exists** (still root) |
| hermes_clone_path | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` |
| nested_git_count_live | **5** |
| appendix_a_parents_reappeared | **no** (live `_backups`/`_quarantine` absent; archive hygiene leaves present) |
| origin | HTTPS `NousResearch/hermes-agent` — **reachable**; `main` tracks `origin/main` (ahead 85); ~1329 tracking refs |
| cada | HTTPS `KenCacciabueOrif/TestNewWorkspaceAgent` — **reachable** but URL **==** parent TNA `origin`; tree = TNA; **no merge-base** with hermes `HEAD`; **0** local branches track it; 3 tracking refs |
| Linked worktrees (hermes) | **1** (main only) |
| Primaries #1–#5 | All present — keep |
| Push/pull dual preflight | **N/A** (no org-repo sync this cycle) |

Details: [`codebase-findings.md`](./codebase-findings.md) · online: [`online-findings.md`](./online-findings.md)

---

## Recommended approach options (max 3)

### Option A (recommended): Narrow gated remote-config — `git remote remove cada`

- **Mutation class for planner:** `fs_mutation` with **mutation kind = remote-config** (edit live hermes `.git` remotes/refs only — **no** corpus path move of primaries or WorkSpace).
- **Map:** On `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` only: `git remote remove cada` (GfW preferred). Leave `origin` URL/fetch untouched. No force-push, no history rewrite, no `set-url`.
- **Acceptance after future execute:** `git remote -v` shows **only** `origin`; `main` still tracks `origin/main`; nested count still **5**; WorkSpace still at root; Multi-experiment stays **in progress / Remaining WorkSpace only**.
- **Pros:** Directly clears the last named live multi-remote hazard; official Git behavior (config + `refs/remotes/cada/*` only); evidence-backed (wrong-repo, untracked by any branch); reversible by re-adding the remote name if needed; no XL path move.
- **Cons:** Removes convenience fetch bookmarks under `cada/*` (including `hermes-agent-cross-hallucination-fixes` tip on the **wrong** remote — still TNA history). Does **not** by itself authorize whole-tree archive / Multi-experiment Complete (other XL / must-preserve / program gates may remain — honesty only).
- **STAGE 1:** Planner drafts intent-preview + Hermes plan gate; orchestrator **stops** (no implement this run).

### Option B: Worktree / relocate live hermes primary

- **Rejected for this Continuity.** Linked worktrees share remotes — do not clear multi-remote. Moving hermes would move live primary **#3** — **hard-forbidden**. Whole-tree WorkSpace archive — **hard-forbidden**.

### Option C: `git remote set-url cada <hermes-fork>` or rename-keep

- **Not recommended.** No evidence of a correct hermes-related URL for the name `cada`. Redirecting to another URL without a known fork invents scope. Keeping a wrong-repo remote fails the hazard clearance goal.

**Fail-closed alternative (only if gate refuses Option A):** Concrete blocker = “Hermes withheld approval to remove `cada` despite wrong-repo evidence.” Minimal gated unblock = Hermes yes on Option A (or user supplies a **documented** hermes-related URL + explicit Continuity for `set-url` — still not docs_only theater). **Do not** substitute Cycles 10–13 re-attest.

---

## Explicit non-goals (this cycle)

- Whole-tree WorkSpace archive / move  
- Moving live primaries **#1–#5**  
- Re-proposing `_backups` / `_quarantine` (verify-only in archive hygiene)  
- History rewrite / force-push / filter-repo  
- Breaking nested `.git` integrity  
- docs_only re-attest as the cycle outcome  
- Marking Multi-experiment Complete / jumping Primary next / Special git  
- TNA dirty-tree hygiene (Q3=A)  
- Taxonomy / must-preserve re-litigation (Q2=A)  
- Changing `origin` URL  
- Mutating archived hygiene clones’ remotes  
- User “fix PATH/credentials” chores as Continuity substitutes  

---

## Clearance status

| Scope | Status |
| --- | --- |
| Live hermes multi-remote | **Clearable** via Option A after Hermes plan-gate yes |
| Whole-tree WorkSpace archive | Still **NO** — out of scope; classified ≠ cleared for ordinary archive |
| Appendix A parents | **Done** Cycle 14 — verify-only |
| Multi-experiment row | Stays **in progress / WorkSpace only** even after Option A |

---

## Planner guidance (STAGE 1)

| Requirement | Detail |
| --- | --- |
| Mutation class | `fs_mutation` (remote-config; zero corpus path moves) |
| Scope | Live hermes clone only — remove remote name `cada` |
| Intent-preview | What yes commits to: one `git remote remove cada`; origin kept; no path moves; multi-remote hazard cleared; row still not Complete; pros/cons |
| Encode | No set-url on origin; no force-push; no primary moves; no whole-tree; no `_backups` re-move |
| Preflight at execute | Re-run `remote -v`, `branch -vv`, confirm still no branch tracks `cada` |
| `ready_to_implement` | May be `yes`; orchestrator **must stop** at Hermes plan gate |
| ROADMAP / INDEX | Honesty updates **post-gate** only — do not claim Complete / Primary next |
| Taxonomy / must-preserve | Carry proposed-ratified / draft |

---

## Required facts

- Continuity Q1=**B**, Q2=**A**, Q3=**A** (locked in refined prompt).  
- Strategy artifact remains authoritative for whole-tree / primary rules.  
- Continuity ≠ plan-gate approval.  
- `cada` is **reachable** but **wrong-target** — not “dead remote,” not hermes-fork duplicate of `origin`.

## Unknowns / blockers

| Item | Status |
| --- | --- |
| Whether Hermes wants to keep wrong-repo `cada` for any undocumented workflow | **Unknown** — gate must confirm; evidence says unused by branch tracking |
| Whole-tree clearance | **Blocked by program law** (OOS), not by Option A |
| Plan-gate execute | **Blocked until Hermes yes** (expected STAGE 1) |
| Auth / dirty_working_tree (org-repo) | **N/A** |

### Push / pull dual preflight

**N/A** — refined prompt excludes publish/pull.

---

## Risks

- Scope creep to path-move hermes or whole WorkSpace.  
- Accidental `remote remove origin` — plan must name **`cada` only**.  
- Misreading “reachable” as “must keep” — reachability ≠ correct target.  
- Claiming Multi-experiment Complete after remote remove alone.

---

## Canonical references

- `program/git-strategy-workspace-hazards.md`  
- `program/ROADMAP.md` (Multi-experiment / WorkSpace only)  
- `catalogue/INDEX.md`  
- `sessions/2026.09.11/` (Cycle 14 Appendix A)  
- https://git-scm.com/docs/git-remote  
- https://git-scm.com/docs/git-worktree.html  
- https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
