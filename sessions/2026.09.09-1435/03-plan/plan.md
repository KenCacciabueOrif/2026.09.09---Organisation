# Plan — Pull-merge (`sessions/2026.09.09-1435`)

## Goal

Finish org-repo sync after session `2026.09.09-1350` (`blocked` / `other`/`non_ff`, 1/1 diverge): via **agent Shell** and **Git for Windows + GCM**, combine local tip with **`origin/main`** using an **allowed merge commit (Q2=B)**. Handle allowlisted dirty with autonomy (commit), then **fetch + merge** `origin/main` into `main`. On conflict, **fail-closed (Q3b=A)** — abort merge, keep WIP recoverable, typed blocker, session `blocked`; never false `complete`. Sync AC is met only when HEAD incorporates `origin/main` via a successful merge; a correct conflict abort is an allowed **process** outcome, not sync success.

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`docs_only`** |
| Corpus FS | **Zero intentional corpus FS mutations** (no `catalogue/**`, `program/**`, or other corpus moves/renames/deletes) |
| User approval before implementer | **Not required** (docs_only; **no corpus plan-gate**) |
| First-move / Early-simple gates | **N/A** — not an `fs_mutation` / first-move batch |
| Taxonomy / must-preserve | **Out of scope** — do not gate; do not claim final ratification or must-preserve lock |

**Implementer attestation (docs_only):** In `04-implementation/log.md`, confirm **no** intentional corpus path moves/renames/deletes. Allowlist commit + merge attempt are allowed **git ops** under this class, not corpus FS mutation.

**Corpus plan-gate needed?** **No.**

## What the user is approving

**N/A — no corpus plan-gate.** Orchestrator may proceed to implementer without a move/rename/delete approval pause. Git allowlist commit + merge attempt are already locked by Choose / continuity in `01-prompt-betterment/notes.md` (Q1–Q7).

## Locked policy (do not re-decide)

| Lock | Value |
| --- | --- |
| Q1 | **A** — `origin` ↔ `main`↔`origin/main` |
| Q2 | **B** — **merge commit allowed** (do not re-litigate to ff-only or silent rebase) |
| Q3 / Q3c | Order-aware **allowlist autonomy then merge** (already diverged → stash→ff-only is **not** the finish path) |
| Q3b | **A** — fail-closed on conflict; keep WIP commit and/or stash recoverable; **no agent conflict resolution** |
| Q4 | **A** — org-repo git root only |
| Q5 | **A** — agent Shell merge must succeed for `complete` |
| Q6 | **A** — fail-closed + typed `blocker_type` + self-improver still runs |
| Q7 | **A** — full FAW session artifacts |
| Allowlist | `sessions/**`, `.cursor/skills/full-agent-workflow/**`, `.cursor/agents/**`, `.cursor/rules/**`, `AGENTS.md`, `sessions/_templates/**` |
| Git binary | GfW absolute: `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` — same binary for porcelain, allowlist commit/stash, fetch, merge |
| Forbidden | force, hard reset, `--no-verify`, `stash drop` on conflict, MSYS for gate/merge |

## Expected merge outcomes (document in implementation log)

Research baseline (pre-implement; **re-verify** at implement):

| State | Value |
| --- | --- |
| Local HEAD | `7ac47835abd7ccb56195bae0daf364baef3e2580` (`7ac4783`) |
| `origin/main` | `489f03a6ab96523ac4551f12c4fcee31603ca544` (`489f03a`) |
| Merge-base | `f5012d6f2d15008e4c211a3167a6682f0a1c7b07` (`f5012d6`) |
| Ahead / behind | **1 / 1** (diverged) |
| Allowlisted / unrelated dirty (research) | all / **0** |
| `git merge-tree HEAD origin/main` | **4 content conflicts** (committed tips) |

Predicted conflict paths (tips only; WT edits may change set after allowlist commit):

1. `.cursor/agents/prompt-betterment.md`
2. `.cursor/rules/full-agent-workflow.mdc`
3. `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
4. `sessions/_templates/01-notes.md`

| Outcome | When | Session status | `blocker_type` / notes |
| --- | --- | --- | --- |
| **Merge success** | `git merge origin/main` completes cleanly; HEAD is a merge commit (or otherwise incorporates `origin/main`) | May be `complete` only if all sync AC met | Record pre/post SHAs; verify `origin/main` is ancestor of HEAD (or HEAD parents include remote tip) |
| **Blocked conflict** (**likely this turn**) | Merge stops with content conflicts; Q3b=A → prefer `git merge --abort`; no agent resolution | **`blocked`** — **never** claim sync / pull complete | Prefer `blocker_type: other` + outcome note `merge_conflict` / `blocked_conflict`. **Not** `dirty_working_tree`. Keep allowlist commit(s) / any stash recoverable |
| **Blocked `dirty_working_tree`** | Any porcelain path outside allowlist | **`blocked`** | List paths; no auto-commit of those paths; no merge |
| **Blocked auth/env** | GfW/GCM fail or MSYS used for gate/merge | **`blocked`** | `user_credentials` or `agent_environment` |

**Disclosure:** Auth and dirty gates are green for *attempting* Option A. Sync AC may remain unmet under Q3b=A even after a correct merge attempt. Correct fail-closed ≠ false complete.

## Acceptance criteria

- [ ] **AC1** All git ops confined to org-repo root `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` (Q4=A); no sibling trees under `C:\Project`.
- [ ] **AC2** Dual preflight (remote/tracking + agent GfW/GCM) re-run at implement; **same GfW binary** for porcelain, allowlist commit/stash, fetch, and merge. Missing `gh` alone ≠ credentials missing.
- [ ] **AC3** Dirty ⊆ allowlist: allowlist commit (BOM-safe message; no `--no-verify`) then merge; unrelated dirty → `blocked` / `dirty_working_tree` (sync unmet).
- [ ] **AC4** Agent runs **fetch** then **`git merge origin/main`** (Q2=B; **not** `--ff-only`). Do not silent-rebase.
- [ ] **AC5 — Sync success path:** HEAD incorporates `origin/main` via merge; verification SHAs recorded (pre-merge local, `origin/main`, post-merge HEAD, parents if merge commit).
- [ ] **AC6 — Conflict / failure path:** Fail-closed (Q3b=A / Q6=A); prefer `merge --abort`; WIP/stash recoverable; typed `blocker_type` (expect `other` + conflict note); session `blocked`; **do not claim pull/sync succeeded**.
- [ ] **AC7** No force-push, hard reset, `--no-verify`, or `stash drop` on conflict.
- [ ] **AC8** Secrets never present in logs/commits (credential fill: presence/booleans only).
- [ ] **AC9** Full FAW session artifacts under `sessions/2026.09.09-1435/` (Q7=A); implementation log documents outcome as **success** vs **blocked_conflict** (or other typed block).
- [ ] **AC10** Session `complete` **only** if sync AC met (AC5); else `blocked` (never false complete); self-improver still runs either way.
- [ ] **AC11** Taxonomy / must-preserve / corpus FS moves untouched; docs_only attestation recorded.
- [ ] **AC12** User terminal merge alone is **not** success (Q5=A).

### Optional signals (not hard AC)

- Exact porcelain line counts, merge-tree re-run conflict list after allowlist commit, file-size notes: **include when cheap** in the implementation log; **do not** fail audit solely because counts drifted from research’s snapshot.

## Ordered steps

### Step 0 — Dual preflight (re-run at implement; before commit + merge)

| | |
| --- | --- |
| **Paths** | Org-repo root only: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` |
| **Action** | Using GfW `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (do **not** use PATH/MSYS for gate): (1) `rev-parse --show-toplevel` → org root; (2) remote URL scheme (**https**) + tracking (`main`→`origin/main`); (3) confirm GfW `credential.helper` / non-secret fill or fetch evidence (booleans only; no secrets logged); (4) note PATH `git` is MSYS without helper — prefer GfW; (5) `gh` present/absent = optional only. |
| **Verify** | Auth green **or** typed `agent_environment` / `user_credentials` and stop with session `blocked`. Research snapshot: auth green. |

### Step 1 — Session implementation log (pre-commit)

| | |
| --- | --- |
| **Paths** | `sessions/2026.09.09-1435/04-implementation/log.md` (create/update); related session notes as needed |
| **Action** | Record dual-preflight results, diverge SHAs (`7ac4783` vs `489f03a` / base `f5012d6`), porcelain classification plan, docs_only attestation, merge-tree disclosure (4 predicted conflicts), and that Step 5 will attempt merge knowing **blocked_conflict** is likely. Write **before** the allowlist commit so the commit includes the trail when staged. |
| **Verify** | Log exists with preflight + classification intent; no secrets. |

### Step 2 — Classify porcelain (GfW, same binary)

| | |
| --- | --- |
| **Paths** | Working tree under org root |
| **Action** | `status --porcelain` via GfW. Partition into allowlist vs unrelated. If unrelated ≠ 0 → abort: list paths, `blocker_type: dirty_working_tree`, session `blocked`, skip commit/merge. |
| **Verify** | Classification recorded; research expected unrelated = 0 (re-check live). **Do not** trust MSYS porcelain (skew risk → false unrelated). |

### Step 3 — Allowlist commit if dirty (BOM-safe)

| | |
| --- | --- |
| **Paths** | Stage **only** allowlisted dirty/untracked (incl. `sessions/2026.09.09-1435/` and any FAW/session dirt). Do **not** stage secrets or non-allowlist paths. |
| **Action** | If porcelain empty after classification → skip. Else: agent-drafted why-focused message, repo style. On Windows PowerShell: commit message **without UTF-8 BOM** — here-string `-m`, or `utf8NoBOM` / `UTF8Encoding($false)`. **Do not** use Windows PS 5.1 `Set-Content -Encoding utf8` (adds BOM). No `--no-verify`. No `git config` changes. Same GfW for `add`/`commit`. Prefer durable allowlist commit over stash while already 1/1 diverged (Option A). |
| **Verify** | Commit created (or N/A clean); post-commit porcelain has **no** non-allowlist dirt; residual allowlist-only dirt documented if any. |

### Step 4 — Fetch `origin`

| | |
| --- | --- |
| **Paths** | Org root; remote `origin` |
| **Action** | Same GfW: `git fetch origin`. Re-read `origin/main` SHA and ahead/behind vs HEAD (may still be 1/1 or remote may have moved). Optionally re-run `git merge-tree HEAD origin/main` for logging only. |
| **Verify** | Fetch exit 0; record `origin/main` tip SHA. On fetch/auth fail → typed blocker; session `blocked`. |

### Step 5 — Merge `origin/main` (Q2=B)

| | |
| --- | --- |
| **Paths** | Org root; branch `main` |
| **Action** | Same GfW: `git merge origin/main` (or equivalent `git pull --no-rebase origin main`). **Do not** use `--ff-only`. **Do not** resolve conflicts; **do not** rebase. |
| **Verify — success:** Merge exit 0; HEAD incorporates `origin/main`; record merge commit SHA + parents. **Verify — blocked_conflict (likely):** Conflicts present → prefer `git merge --abort` to restore pre-merge tip; keep allowlist commit(s) recoverable; no force/hard reset/`stash drop`; session `blocked`, `blocker_type: other` + `blocked_conflict` / `merge_conflict` note; **never claim sync complete**. |

### Step 6 — Verification SHAs + outcome label

| | |
| --- | --- |
| **Paths** | `sessions/2026.09.09-1435/04-implementation/log.md` |
| **Action** | Record: pre-merge HEAD, `origin/main` at merge time, post-merge HEAD (or restored tip after abort), ahead/behind after attempt, outcome enum **`merge_success`** \| **`blocked_conflict`** \| **`dirty_working_tree`** \| **`agent_environment`** \| **`user_credentials`** \| other typed block. |
| **Verify** | Outcome label matches git state; sync success claimed **only** for `merge_success`. |

### Step 7 — Session finalize for auditor

| | |
| --- | --- |
| **Paths** | `sessions/2026.09.09-1435/SESSION.md`, `04-implementation/log.md` (+ `changes.md` as needed) |
| **Action** | Set status accurately: `complete` **only** if AC5 sync met; otherwise `blocked` with `blocker_type`. Orchestrator flips `blocked` as soon as implementer returns blocked_conflict / dirty-abort / auth fail. Post-success session dirt from finalize notes is expected (not rework) if sync already met. |
| **Verify** | SESSION status matches outcome; AC9–AC10 trail ready for auditor; self-improver still scheduled either way. |

## Non-goals

- Corpus moves/renames/deletes; taxonomy final ratification; must-preserve lock
- Agent conflict resolution / merge conflict editing under Q3b=A
- Re-litigating Q2 to ff-only or silent rebase; soft-reset recover tip + ff-only (Option C rejected)
- Force push, hard reset, `--no-verify`, `stash drop` on conflict
- Sibling `C:\Project` git ops; MSYS porcelain as authoritative gate
- Treating user-terminal-only merge as agent success
- Claiming sync / pull **complete** after conflict abort
- Expanding FAW policy docs beyond what is needed for this merge attempt (no mandatory docs rewrite cycle)

## Risks / rollback

| Risk | Mitigation / rollback |
| --- | --- |
| Content conflicts on ~4 FAW paths (merge-tree) | **Expected likely**; fail-closed Q3b=A; `merge --abort`; session `blocked` / `other`+conflict; do **not** claim sync complete |
| Dirty overlap with conflict paths | Allowlist-commit (or path-stash) **before** merge so merge can start cleanly |
| MSYS porcelain false unrelated | Gate/merge with GfW only; else `agent_environment` |
| Auth / GCM failure mid-fetch/merge | Typed `user_credentials` / `agent_environment`; leave local commit; blocked not complete |
| Unrelated dirty mid-cycle | Abort; `dirty_working_tree`; list paths |
| Force / hard reset temptation | Forbidden; policy violation if used |
| Secrets in allowlist commit | Scan stage list; never log fill passwords |
| Remote gains commits between research and implement | Re-fetch (Step 4); merge whatever current `origin/main` is |
| Rollback after clean merge | User-directed later cycle only; do not hard-reset in this cycle |
| Rollback after conflict | `merge --abort` restores pre-merge tip; allowlist commit(s) remain |

## Ready to implement

**yes**

Rationale: Locks complete (Q2=B, Q3b=A, GfW, org root); mutation `docs_only` (**no corpus plan-gate**); auth green; unrelated dirty 0 at research; ordered attempt + success vs **blocked_conflict** outcomes specified. Sync may fail on predicted conflicts — that is an allowed blocked outcome, not a planner stop.

## Blocking questions

**none**

---

## Plan result (orchestrator)

- `plan_path`: `sessions/2026.09.09-1435/03-plan/plan.md`
- `ready_to_implement`: **yes**
- `mutation_class`: **docs_only**
- `corpus_plan_gate_needed`: **no**
- `blocking_questions`: none
- `step_count`: 8 (Steps 0–7)
- `one_line_summary`: GfW allowlist-commit then merge `origin/main` (Q2=B); expect likely conflict block under Q3b=A; no corpus gate.
