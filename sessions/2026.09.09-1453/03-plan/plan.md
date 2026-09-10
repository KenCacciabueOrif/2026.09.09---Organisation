# Plan

## Goal

Finish org-repo sync after session `2026.09.09-1435` blocked on allowlist-only merge conflicts: dual-preflight with Git for Windows, allowlist-commit any FAW dirty WIP, fetch, merge `origin/main` into current `main` tip (Q2=B), resolve every unmerged path under Q3b=B with **R1 = combined-best** (study both sides per hunk; keep the most appropriate content), complete the merge so HEAD incorporates `origin/main`, document judgment trail + session log/changes, and fail-closed (never false `complete`) on unrelated dirty or non-allowlist conflict. Self-improver (later phase) must diminish user workload—not dump recurring cleanup on the user.

## Mutation class

| Field | Value |
| --- | --- |
| Class | `docs_only` |
| Corpus FS | **Zero intentional corpus FS mutations** (no moves/renames/deletes under catalogue/corpus trees). Git ops touch only org-repo FAW allowlist / session docs. Implementer attests in `04-implementation/log.md`: no corpus path mutations performed. |
| User approval before implementer | **not required** (docs_only — **no corpus plan-gate**) |
| First-move gates (if fs_mutation) | n/a |

## What the user is approving

**n/a — docs_only; no corpus plan-gate.** Orchestrator may proceed straight to implementer.

## Locked policy (from notes — do not re-ask)

| Item | Lock |
| --- | --- |
| Q1 | A — `origin` → `main`↔`origin/main` |
| Q2 | **B — merge commit allowed** (not ff-only-only) |
| Q3 | Allowlist then merge; unrelated dirty → `dirty_working_tree` abort |
| Q3b | **B — allowlist-only resolve** |
| R1 | **combined / judgment-per-hunk (`combined-best`)** — not blind `--ours`/`--theirs` |
| Q4–Q7 | A (org root only; agent Shell success; fail-closed + typed blocker; full session docs) |
| Forbidden | `-s ours`; force-push; hard reset; `--no-verify`; `stash drop` on conflict; MSYS git for porcelain/merge gates |

**FAW dirty allowlist:** `sessions/**`, `.cursor/skills/full-agent-workflow/**`, `.cursor/agents/**`, `.cursor/rules/**`, `AGENTS.md`, `sessions/_templates/**`.

**Expected conflict paths (verify live):**

1. `.cursor/agents/prompt-betterment.md`
2. `.cursor/rules/full-agent-workflow.mdc`
3. `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
4. `sessions/_templates/01-notes.md`

## Acceptance criteria

- [ ] Dual preflight green (or typed `agent_environment` / `user_credentials` block): HTTPS remote + `main`↔`origin/main`; agent uses GfW absolute path + GCM evidence; `gh` absence alone ≠ credentials fail; porcelain classified allowlist vs unrelated
- [ ] All git ops confined to org-repo root (`git rev-parse --show-toplevel` = `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`); no sibling trees
- [ ] If porcelain non-empty and ⊆ allowlist → allowlist commit (BOM-safe message, no `--no-verify`) before merge; if any path outside allowlist → abort `dirty_working_tree`, session `blocked`, never claim pull succeeded
- [ ] After fetch, `git merge origin/main` proceeds under Q2=B (not `--ff-only`; not rebase; no `-s ours`)
- [ ] Every unmerged path ⊆ FAW allowlist; **if any outside → `merge --abort`**, `blocker_type` `other`/`merge_conflict`, session `blocked`, never claim sync complete
- [ ] For each allowlist conflict (the 4 expected + any new allowlist-only): agent studies both versions per hunk, applies **combined-best**, removes markers, `git add`
- [ ] Implementation log notes per conflict file which side(s) were kept / how merged (judgment trail)
- [ ] Merge completed; **HEAD incorporates `origin/main`** (e.g. `git merge-base --is-ancestor origin/main HEAD` succeeds)
- [ ] `04-implementation/log.md` + `changes.md` written; implementer attests **zero intentional corpus FS mutations**
- [ ] On auth/env/unrelated-dirty/non-allowlist-conflict: session `blocked` + typed `blocker_type`; no force/hard reset/`--no-verify`
- [ ] Self-improver **mandatory** later: mandate **diminish user workload** — encode autonomy in agents/skills/rules so recurring sync/conflict cleanup is not dumped on the user

## Steps

**Git binary (all steps):** `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (same binary for porcelain, commit, fetch, merge, resolve). Do not use PATH MSYS git for gates.

1. **Dual preflight** — paths: org root only  
   - Action: Confirm `rev-parse --show-toplevel`; remote URL scheme (HTTPS); `main` tracking `origin/main`; GfW version + `credential.helper` / non-interactive fill evidence (no secret values in logs); note `gh` present/absent (optional); optional user-terminal note that prior terminal success ≠ this agent merge. Classify `blocker_type` if fail: `agent_environment` vs `user_credentials`.  
   - Verify: auth green to proceed; else stop, session `blocked`, do not start merge.

2. **Dirty gate + allowlist commit if dirty** — paths: FAW allowlist only  
   - Action: GfW `status --porcelain`. Unrelated paths → abort `dirty_working_tree` (list paths). If allowlisted dirty (research: 19 / 0 unrelated, including `sessions/2026.09.09-1453/` and dirty overlap on 3/4 conflict files) → stage **only** allowlist paths, scan for secrets, commit with **BOM-safe** message (PowerShell: `utf8NoBOM` / `UTF8Encoding($false)` / here-string `-m`; never `Set-Content -Encoding utf8`). No `--no-verify`.  
   - Verify: working tree clean of allowlist dirt (or only intentional post-commit clean); HEAD advanced if commit made; unrelated still empty.

3. **Fetch** — `origin`  
   - Action: `git fetch origin`. Re-read `origin/main` SHA and ahead/behind (research tip: local `f3e1119` / remote `489f03a` / base `f5012d6`; ahead/behind 2/1 — **re-verify live**).  
   - Verify: fetch exit 0; remote tip known.

4. **Merge `origin/main`** — Q2=B  
   - Action: `git merge origin/main` (allow merge commit; not `--ff-only`; not rebase; no `-s ours`).  
   - Verify: either clean merge, or conflicts listed; if unexpected non-merge failure, fail-closed with typed blocker.

5. **Allowlist conflict gate**  
   - Action: List unmerged paths. If **any** path ∉ FAW allowlist → `git merge --abort`, keep recoverable tip, `blocker_type` `other`/`merge_conflict`, session `blocked`. If all ⊆ allowlist (expect the 4 FAW paths above; same rule for any *new* allowlist-only conflicts) → proceed to step 6.  
   - Verify: gate decision recorded in log; no silent resolve of non-allowlist paths.

6. **Combined-best resolve (R1)** — expected files + any new allowlist-only conflicts  
   - Action: For each conflicted file/hunk: open both sides (`<<<<<<<` / `=======` / `>>>>>>>`); study local vs remote; keep most appropriate (local, remote, or coherent merge of both). Research lean (hints only — re-judge live):  
     - `prompt-betterment.md` — HEAD unanswered→default **+** origin Choose-all / ask-summary  
     - `full-agent-workflow.mdc` — prefer HEAD pull/dirty/Q3c/SESSION; fold origin docs_only scaffolding phrase  
     - `handoff-templates.md` — HEAD pack/Q3c **+** origin Choose-all/ask-summary/docs_only; review auto-merged regions  
     - `sessions/_templates/01-notes.md` — HEAD unanswered Source language **+** origin Choose-all / ask-summary  
   - After markers removed, briefly review full file (not only marked hunks) so auto-merge did not drop pull guidance.  
   - Verify: no conflict markers remain in resolved files.

7. **Stage + complete merge**  
   - Action: `git add` each resolved path; complete merge commit (BOM-safe message if editor/file used; no `--no-verify`).  
   - Verify: no unmerged paths; `MERGE_HEAD` gone; merge commit created.

8. **Verify sync AC**  
   - Action: Confirm HEAD incorporates `origin/main` (e.g. `git merge-base --is-ancestor origin/main HEAD`); record parents / SHAs in log.  
   - Verify: ancestor check passes → sync AC met; else fail-closed, do not claim complete.

9. **Session artifacts** — `sessions/2026.09.09-1453/04-implementation/`  
   - Action: Write `log.md` (preflight, dirty/commit, fetch SHAs, conflict list, **per-file judgment trail**, merge result, ancestor verify, corpus-mutation attestation) and `changes.md` (files touched). Note self-improver mandate for later phase.  
   - Verify: artifacts present; judgment trail covers every conflict file.

### Fail-closed outcomes (never claim pull/sync succeeded)

| Condition | `blocker_type` | Action |
| --- | --- | --- |
| Unrelated dirty | `dirty_working_tree` | Abort before merge; list paths |
| Wrong git / GCM blocked | `agent_environment` | Abort; prefer GfW remediation note |
| True auth/login fail | `user_credentials` | Abort (missing `gh` alone ≠ this) |
| Non-allowlist unmerged path | `other` / `merge_conflict` | `merge --abort`; keep recoverable |
| Merge/auth fail mid-op | typed as above | Session `blocked`; self-improver still runs later |

## Non-goals

- Corpus moves/renames/deletes; taxonomy final ratification; must-preserve lock
- Blind whole-file `--ours` / `--theirs`; `-s ours`
- Resolving non-allowlist conflict paths
- Force-push, hard reset, `--no-verify`, `stash drop` on conflict
- Treating user-terminal pull as agent success (Q5=A)
- False session `complete` when sync unmet
- Push to remote (pull/merge only this cycle unless user later asks)

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| MSYS git used for porcelain/merge | Absolute GfW only; classify `agent_environment` if violated |
| Non-allowlist conflict appears live | `merge --abort`; `other`/`merge_conflict`; never claim sync complete |
| Poor hunk judgment drops useful side | Study both; log winners; prefer coherent FAW law; review full files after resolve |
| Dirty overlap lost if merge before commit | Step 2 allowlist commit first (Option A) |
| Remote moves between research and implement | Re-fetch in step 3; re-check conflict set |
| Secrets in allowlist commit | Stage scan; never log credential fill passwords |
| BOM in commit message (Windows PS) | utf8NoBOM / here-string `-m` |
| Rollback mid-merge | Prefer `merge --abort` while recoverable; no hard reset |

## Ready to implement

**yes**

## Blocking questions

**none**
