# Plan — Pull-autonomy (`sessions/2026.09.09-1350`)

## Goal

Fix the FAW dirty-tree deadlock so agent `git pull` / publish cycles no longer require the user to clean expected session/FAW-meta dirt. First, update org-repo workflow docs so the FAW default is **allowlisted auto-commit then `git pull --ff-only`** (abort only for unrelated dirty), and mirror the same allowlist autonomy on publish. Then, in this same session, use Git for Windows only inside the org-repo root: classify porcelain, auto-commit allowlisted paths if needed, and **attempt** `git pull --ff-only` of `origin` into `main`↔`origin/main`. Fail-closed on conflict / non-ff / unrelated dirty (no force, hard reset, `--no-verify`, merge, or rebase). Correct process success includes either a successful ff-only pull **or** a typed fail-closed block (expected after allowlist commit vs remote tip `489f03a`).

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`docs_only`** |
| Corpus FS | **Zero intentional corpus FS mutations** (no `catalogue/**`, `program/**`, or other corpus moves/renames/deletes) |
| User approval before implementer | **Not required** (docs_only; no corpus plan-gate) |
| First-move / Early-simple gates | **N/A** — this cycle is not an `fs_mutation` / first-move batch |
| Taxonomy / must-preserve | **Out of scope** — do not gate; do not claim final ratification or must-preserve lock |

**Implementer attestation (docs_only):** After Phase A doc edits and Phase B git ops, confirm in `04-implementation/log.md` that **no** intentional corpus path moves/renames/deletes occurred. Org-repo git commit + pull attempt are allowed git ops under this class, not corpus FS mutation.

**Corpus plan-gate needed?** **No.**

## What the user is approving

**N/A — no corpus plan-gate.** Orchestrator may proceed to implementer without a move/rename/delete approval pause. (Git allowlist commit + pull attempt are locked by Choose Q1–Q9 in `01-prompt-betterment/notes.md`.)

## Locked policy (do not re-decide)

| Lock | Value |
| --- | --- |
| Dirty handler | Allowlist **auto-commit** then `git pull --ff-only` |
| Allowlist | `sessions/**`, `.cursor/skills/full-agent-workflow/**`, `.cursor/agents/**`, `.cursor/rules/**`, `AGENTS.md`, `sessions/_templates/**` |
| Order | Update pull-cycle (+ publish-cycle / agents / skill / rules / AGENTS / templates as needed) **FIRST**, then same-session allowlist commit + pull |
| Combine | Q2=**A** — `--ff-only` only; **no** merge/rebase fallback |
| Failure | Fail-closed; keep WIP allowlist commit recoverable; no force / hard reset / `--no-verify` / stash-drop |
| Git binary | GfW absolute path for status, commit, and pull; org root only |
| Success bar | Agent Shell (not user terminal alone) |

## Expected pull outcomes (document in implementation log)

Research baseline (pre-implement; re-verify at implement):

| State | Value |
| --- | --- |
| Local HEAD | `f5012d6` |
| Remote tip | `489f03a` (`origin/main`) |
| Ahead / behind (pre-commit) | 0 / 1 |
| Allowlisted / unrelated dirty (research) | 23 / 0 |

| Outcome | When | Session status | `blocker_type` / notes |
| --- | --- | --- | --- |
| **Pull success** | After allowlist commit, local tip is still a strict ancestor of `origin/main` and ff-only advances HEAD to remote tip | May be `complete` only if all AC met | Record SHAs; verify HEAD == `origin/main` tip |
| **Blocked `non_ff` / diverge** (**expected this turn**) | Allowlist commit creates local tip that **diverges** from `489f03a` (both children of `f5012d6`) → `--ff-only` refuses | **`blocked`** — never false `complete` | Prefer `blocker_type: other` with outcome note `non_ff` / history diverge (or plan vocabulary already on implementer: accurate typed block). **Not** `dirty_working_tree`, **not** credentials |
| **Blocked `dirty_working_tree`** | Any porcelain path outside allowlist | **`blocked`** | List paths; no auto-commit of those paths; no pull |
| **Blocked auth/env** | GfW/GCM fail or wrong binary forced | **`blocked`** | `user_credentials` or `agent_environment` |

**Do not** switch to merge/rebase to absorb `489f03a` unless a later user Choose changes Q2 (current AC forbid it).

## Acceptance criteria

### A — Workflow docs (implement first)

- [ ] **AC1** `pull-cycle.md` Q3 / dirty policy: FAW default = **allowlisted auto-commit then pull**; abort **only** for unrelated (non-allowlist) dirty; disclosed Choose default and `blocker_type` text updated (abort is no longer the universal FAW dirty default).
- [ ] **AC2** `publish-cycle.md` (and related skill/rule/agent/handoff text as needed) **mirrors** the same allowlist autonomy for push/publish dirty handling; unrelated dirty still aborts.
- [ ] **AC3** Allowlist paths documented in updated references and match the locked table above.
- [ ] **AC4** Standing constraints preserved: org-repo root only; GfW same-binary gate; fail-closed; no force / hard reset / `--no-verify`; self-improver still runs on block.
- [ ] **AC5** Auditor / implementer / orchestrator / researcher / prompt-betterment / handoff / session-structure guidance no longer treat “any dirty → always user cleanup” as the only correct pull path when dirt ⊆ allowlist.

### B — Same-session agent pull (after A)

- [ ] **AC6** Dual preflight green (or fail-closed with typed blocker if not).
- [ ] **AC7** If dirty ⊆ allowlist only: agent creates allowlist commit(s) as needed so non-allowlist porcelain is empty / tree is pullable per policy; then agent runs `git pull --ff-only` (GfW) of `origin` into current `main`↔`origin/main` tracking.
- [ ] **AC8** If any non-allowlist dirty remains: abort pull, list paths, `blocker_type: dirty_working_tree`, session `blocked` — do not claim pull success.
- [ ] **AC9** On pull conflict or non-ff failure: fail-closed per Q3b/Q6; WIP allowlist commit left recoverable; session `blocked` with accurate `blocker_type`; never mark `complete`.
- [ ] **AC10** Success-of-process = agent Shell pull succeeded (ff-only) **or** correctly blocked with typed blocker; remote session-elsewhere changes incorporated **when** pull succeeds; full FAW artifacts under `sessions/2026.09.09-1350/`.
- [ ] **AC11** User terminal pull alone is **not** success (Q5 A).

### Optional signals (not hard AC)

- Re-fetch ahead/behind counts, exact porcelain line counts, file-size notes: **include when cheap** in the implementation log; **do not** fail audit solely because a count drifted from research’s “23 dirty” snapshot.

## Ordered steps

### Step 0 — Dual preflight (before commit + pull; re-run at implement)

| | |
| --- | --- |
| **Paths** | Org-repo root only: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` |
| **Action** | Using GfW `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (do **not** use PATH/MSYS for gate): (1) `rev-parse --show-toplevel` → org root; (2) remote URL scheme + tracking (`main`→`origin/main`); (3) confirm GfW `credential.helper` / non-secret fill or fetch evidence (booleans only; no secrets logged); (4) note PATH `git` is MSYS without helper — prefer GfW; (5) `gh` present/absent = optional only (missing `gh` ≠ credentials missing when GCM works). |
| **Verify** | Auth green **or** typed `agent_environment` / `user_credentials` and stop Phase B pull with session `blocked`. Research snapshot: auth green. |

### Step 1 — Update `pull-cycle.md` (FIRST doc change)

| | |
| --- | --- |
| **Paths** | `.cursor/skills/full-agent-workflow/references/pull-cycle.md` |
| **Action** | Rewrite Q3 options/default: FAW default = allowlisted auto-commit then pull (encode locked allowlist table); abort only for unrelated dirty. Update framing, blocker_type text (`dirty_working_tree` = unrelated / non-allowlist abort), remediation (allowlist path = agent commit; unrelated = user / new cycle), auditor notes (correct unrelated abort vs allowlist commit path; correct non-ff block). Keep Q2=A ff-only; forbid merge/rebase fallbacks. Add Q3b fail-closed keep WIP commit if not already clear. |
| **Verify** | Grep: no “universal abort any dirty” as FAW default; allowlist paths listed; ff-only retained. |

### Step 2 — Mirror on `publish-cycle.md`

| | |
| --- | --- |
| **Paths** | `.cursor/skills/full-agent-workflow/references/publish-cycle.md` |
| **Action** | Add dirty-autonomy question / standing constraint mirroring the same allowlist for push/publish readiness; unrelated dirty aborts; prefer commit over stash; same GfW + org-root rules. |
| **Verify** | Publish pack documents allowlist auto-commit; unrelated abort remains. |

### Step 3 — Align skill, rule, AGENTS, agents, handoffs, templates

| | |
| --- | --- |
| **Paths** | `.cursor/skills/full-agent-workflow/SKILL.md`; `.cursor/rules/full-agent-workflow.mdc`; `AGENTS.md`; `.cursor/agents/{prompt-betterment,researcher,planner,implementer,auditor,orchestrator}.md`; `.cursor/skills/full-agent-workflow/references/{handoff-templates.md,session-structure.md}`; `sessions/_templates/**` only if they still say “default dirty = abort” as universal |
| **Action** | Replace “any dirty → user cleanup only” / “dirty-abort default” language with allowlist-first FAW default; keep fail-closed; distinguish `dirty_working_tree` (unrelated) vs `non_ff`/auth/env; implementer may auto-commit allowlist then pull; auditor: allowlisted dirt committed then pull attempted = correct path; unrelated abort = process pass + blocked + `rework_owner: user`; expected post-allowlist non-ff = process pass + blocked (sync AC unmet), not implementer defect for refusing merge. |
| **Verify** | Spot-grep for obsolete “default dirty = abort” / “any porcelain → pull not attempted” without allowlist exception; fix remaining hits in listed paths. |

### Step 4 — Session implementation notes (pre-commit)

| | |
| --- | --- |
| **Paths** | `sessions/2026.09.09-1350/04-implementation/log.md` (and related session files as needed) |
| **Action** | Record dual-preflight results, porcelain classification (allowlisted vs unrelated), docs-only attestation, and that Phase B will attempt ff-only knowing diverge is likely. Write **before** the allowlist commit so the commit includes the trail. |
| **Verify** | Log exists with preflight + classification; no secrets. |

### Step 5 — Classify porcelain (GfW, same binary)

| | |
| --- | --- |
| **Paths** | Working tree under org root |
| **Action** | `status --porcelain` via GfW. Partition into allowlist vs unrelated. If unrelated ≠ 0 → abort: list paths, `blocker_type: dirty_working_tree`, session `blocked`, skip commit/pull; still leave docs changes as WIP unless already committed. |
| **Verify** | Classification recorded; research expected unrelated = 0 (re-check live). |

### Step 6 — Allowlist commit (BOM-safe)

| | |
| --- | --- |
| **Paths** | Stage **only** allowlisted paths (Step 1–4 edits + other allowlisted dirty/untracked). Do **not** stage secrets or non-allowlist paths. |
| **Action** | Agent-drafted why-focused message, repo style. On Windows PowerShell: write commit message **without UTF-8 BOM** — use here-string `-m`, or `utf8NoBOM` / `UTF8Encoding($false)`. **Do not** use Windows PS 5.1 `Set-Content -Encoding utf8` (adds BOM). No `--no-verify`. No `git config` changes. Same GfW binary for `add`/`commit`. |
| **Verify** | Commit created; post-commit porcelain has **no** non-allowlist dirt; allowlist-only residual (e.g. post-commit log tweak) documented if any. |

### Step 7 — Attempt `git pull --ff-only` (GfW)

| | |
| --- | --- |
| **Paths** | Org root; remote `origin`; branch `main`↔`origin/main` |
| **Action** | Same GfW binary: `git pull --ff-only` (or fetch + ff-only merge equivalent). **Do not** merge/rebase on failure. Record exit code, local tip SHA, `origin/main` SHA, ahead/behind. |
| **Verify** | **Success path:** HEAD matches remote tip; session may proceed toward complete if all AC met. **Expected fail path:** non-ff / diverge → session `blocked`, typed blocker (`other`/`non_ff`), WIP allowlist commit recoverable, never force/hard reset; self-improver still runs. |

### Step 8 — Session finalize for auditor

| | |
| --- | --- |
| **Paths** | `sessions/2026.09.09-1350/SESSION.md`, `04-implementation/log.md` |
| **Action** | Set status accurately (`complete` only if ff pull succeeded **and** ACs met; otherwise `blocked` with `blocker_type`). Never mark complete for user-terminal pull alone. Orchestrator flips `blocked` as soon as implementer returns blocked. |
| **Verify** | SESSION status matches outcome; AC10 trail complete for auditor. |

## Non-goals

- Corpus moves/renames/deletes; taxonomy final ratification; must-preserve lock
- Auto-committing or stashing non-allowlist paths; commit-all WIP; stash/autostash as default dirty handler
- Force push, hard reset, `--no-verify`, rebase-as-default, merge commits (Q2=A)
- Sibling `C:\Project` git ops
- Treating prior session `2026.09.09-1332` Q3=A Choose as binding for this cycle (explicitly superseded)
- Expanding to merge/rebase to absorb `489f03a` in this cycle

## Risks / rollback

| Risk | Mitigation / rollback |
| --- | --- |
| Post-allowlist-commit diverge vs `489f03a` → ff-only fail | **Expected**; fail-closed; leave commit recoverable; session `blocked`; do **not** merge/rebase; document as process success under AC9–10 |
| Unrelated dirty appears mid-cycle | Abort; `dirty_working_tree`; list paths; no commit-all |
| PATH/MSYS used for porcelain/pull | Prefer GfW absolute; classify `agent_environment` if forced |
| Auth/GCM regression | Typed `user_credentials` / `agent_environment`; leave local commit; blocked not complete |
| Secrets in allowlist stage | Scan stage list; never commit secrets; no secret values in logs |
| Docs still claim universal dirty-abort | Step 3 grep pass before allowlist commit |
| Rollback of doc edits | Revert allowlist commit or restore files from pre-commit tree; never hard reset unless user explicitly asks in a later cycle |
| Partial doc update then crash | Prefer finish AC A before commit; if interrupted, resume docs then one allowlist commit |

## Ready to implement

**yes**

Rationale: Locks complete; mutation `docs_only` (no corpus plan-gate); auth green per research; unrelated dirty 0 at research time; ordering and fail-closed outcomes specified. Pull **sync** may fail ff-only after allowlist commit — that is an allowed blocked outcome, not a planner stop.

## Blocking questions

**none**

---

## Plan result (orchestrator)

- `plan_path`: `sessions/2026.09.09-1350/03-plan/plan.md`
- `ready_to_implement`: **yes**
- `mutation_class`: **docs_only**
- `corpus_plan_gate_needed`: **no**
- `blocking_questions`: none
- `step_count`: 9 (Steps 0–8)
- `one_line_summary`: Docs-first allowlist auto-commit + GfW `--ff-only` attempt; expect possible non-ff block vs `489f03a`, no corpus gate.
