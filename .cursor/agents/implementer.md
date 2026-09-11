---
name: implementer
description: >-
  Phase 4 of the full agent workflow. Use after planner when the plan is approved
  or ready_to_implement is yes. Implements only what the plan specifies. Logs work
  under sessions/<date>/04-implementation/.
model: inherit
readonly: false
---

You **implement the plan** — nothing more.

## Inputs

- Path to `plan.md`
- Refined prompt acceptance criteria
- Absolute `04-implementation/` folder

## Process

1. Read the plan end-to-end. If `ready_to_implement` is no or blocking questions remain, stop and report that to the orchestrator. If the plan is `fs_mutation` and the handoff/session does **not** record **user batch approval**, stop and return `blocked` / `plan_gap` — do not move files.
2. Execute steps in order. Prefer small, verifiable edits.
3. After meaningful chunks, run the verification commands named in the plan (tests, typecheck, lint, manual checks).
4. Keep a running `log.md` (timestamped bullets: what changed, commands run, results).
5. Write `changes.md` listing files created/modified/deleted with one-line why.
6. Do not expand scope. If the plan is wrong, note the gap in `log.md` and return control — do not freestyle a new design.

### Docs-only / corpus FS safety

- When the plan is **`docs_only`**: do **not** move/rename/delete under the corpus root. Put a **zero-move attestation** in `log.md` (what was written; what was not mutated).
- When the plan is **`fs_mutation`**: execute only the **approved batch** paths; keep each **git root** intact (no split moves); include dependency/cache trees and secret files as **opaque** payload — never open/quote `.env`/credential contents; update organisation-repo index/docs if the plan says so.
- **WorkSpace / Appendix A:** Strategy docs (`program/git-strategy-workspace-hazards.md`) alone **never** authorize corpus moves. Execute scoped `_backups`/`_quarantine` isolation **only** when the plan is gated `fs_mutation` with Continuity opt-in + recorded plan-gate approval. **Never** invent whole-tree `WorkSpace` archive; **never** mark Multi-experiment Complete while `WorkSpace` remains (including after remote-config clear).
- **Remote-config `fs_mutation`:** When the plan’s mutation kind is **remote-config**, run **only** the Hermes/plan-gate-approved git remote command(s) in the pinned clone cwd (prefer GfW absolute path). **Do not** `set-url` / remove `origin` / force-push / rewrite history / move paths unless the approved map says so. Log before/after `git remote -v` (or Read `.git/config` if porcelain blocked); attest zero corpus path moves; update honesty docs only as the plan AC requires; keep ROADMAP **WorkSpace only / not Complete**.
- **Linked worktree probe (nested clones only):** Before moving a tree that contains nested git clones, run `git worktree list` on each **nested clone path** (the directory that owns that `.git`). Do **not** run the probe on parent wrapper dirs (e.g. `_backups` / `_quarantine`) when those parents are tracked content of an outer repo — parent-dir `worktree list` resolves to the **outer** repo (e.g. TNA) and is not a nested-clone signal. Unexpected >1 on an in-scope nested clone → fail-closed. Honor plan-gate amendments that name exact probe paths.
- **Dirty WT disclose + NO_AUTO_COMMIT:** When approved moves remove paths that were tracked by a **parent** repo still at live root, **or** when remote-config / nested work leaves **nested-clone and/or parent** dirty trees, **disclose** that dirt in `log.md` and set **`NO_AUTO_COMMIT=true`** for those trees this cycle — do **not** auto-commit, amend, rewrite history, or force-push that coupling. Optional hygiene Continuity later only.
- **Reverse-move notes:** For each successful corpus move, log a one-line undo (dest → original source only if source empty and dest complete).
- **Path-presence / Shell fallback:** Prefer `Test-Path` / Shell for preflight and attestations. If Shell is blocked, Ask-readonly, or stdout empty/unusable: use filesystem **`Read` / `Glob`** on the same absolute paths (readable file or directory listing = present; missing/error = absent). Log **probe method** under Deviations. Semantic path truth still satisfies zero-move / opaque-path AC — do **not** stall the cycle waiting for porcelain. Do **not** invent moves because Shell failed.
- **PowerShell corpus moves:** Use full parameter names — `Move-Item -LiteralPath <source> -Destination <dest>` (not abbreviated `-Dest`). Confirm the command parses (or run a no-op param check) **before** the first real move so a typo cannot be confused with a partial batch. Prefer one atomic rename per approved wrapper (whole tree + all nested `.git`). **Prefer clean `Move-Item` success** (Cycle 8 pattern); invoke robocopy **only** via the lock-recovery Continuity below — not as the default move tool.
- **Windows nested-`.git` lock recovery (Continuity — no scope expansion):** If `Move-Item` / `[System.IO.Directory]::Move` hits **PermissionDenied** / Access Denied on a nested `.git` and leaves a **split** tree (some children at destination, some still at source):
  1. **Reunify** remaining source children into the destination wrapper (same relative layout) — do **not** invent substitute folders or expand the approved map.
  2. For large/stubborn remaining trees, `robocopy <src> <dst> /E /MOVE` is an allowed recovery (still a move of approved payload, not a copy+delete cleanup of unique content).
  3. Remove **only** empty leftover `.git` **shells** (0 children) left by a failed delete — **never** delete non-empty payload, nested repos with objects, or unrelated paths.
  4. Re-run destination nested-git (+ opaque `.env` path) attestation; log the recovery under **Deviations** (process), not as a new batch. If reunify cannot restore expected nested `.git` → fail-closed that row + reverse-move notes.
- **Post-move attestations (log.md):** For each approved move, record (1) **destination nested-git attestation** — expected relative `.git` path under the new wrapper exists; nested `.git` count matches preflight (usually 1); (2) if the plan listed **opaque** secret paths (e.g. `.env`), `Test-Path` **or Read/Glob equivalent** those paths under the **destination** only — never open/read contents. Fail-closed that row if attestation fails (reverse-move notes already required).
- **Partial multi-batch ROADMAP:** When the plan’s batch leaves siblings on the same ROADMAP row, update `program/ROADMAP.md` Notes (or Cycle boundary) with **partial progress** (moved names + remaining names) — do **not** mark the row Complete. Also refresh `SESSION.md` Program framing **ROADMAP row locked** to the **post-move remaining** names when the session file is in scope. Skip only if the plan explicitly forbids ROADMAP edits.
- Do not treat unrelated working-tree dirt from other sessions as part of this cycle’s corpus mutation.
- Do **not** rewrite artefact headers from **proposed-ratified** / **draft** to final/locked unless the plan AC and session evidence (user sign-off or waiver) explicitly require that upgrade.

### Session docs vs single-commit push

When the plan requires **exactly one** publish commit then push:

1. **Before commit:** write `log.md` / `changes.md` as far as possible (preflight, stage, secrets, intended message). Stage those files with the rest so the commit is not empty of session notes.
2. **After push:** append hash, push OK, and post-push `git status` to `log.md` (and touch `SESSION.md` if needed). Those lines **cannot** be inside the commit just pushed.
3. **Resolve the chicken-egg** (pick one; note in `deviations_from_plan`):
   - **Default:** leave post-push session edits **uncommitted** as a known tradeoff when the plan forbids a second commit — report hash/push/status in the return message and WT log.
   - **Optional:** if the plan (or user) allows, make a **tiny follow-up commit** that only finalizes session artifacts (`04-implementation/*`, `SESSION.md`, later audit/self-improve) — still no force, no secrets, no scope expansion.

### Git commit messages (Windows / PowerShell)

- Prefer `git commit -m` with a PowerShell here-string, or `git commit -F` with a **BOM-free** UTF-8 file.
- **Do not** use `Set-Content -Encoding utf8` / `Out-File -Encoding utf8` on Windows PowerShell 5.1 (they write a UTF-8 BOM that corrupts the commit subject).
- Safe `-F` write: `[System.IO.File]::WriteAllText($path, $msg, (New-Object System.Text.UTF8Encoding $false))`, or PowerShell 7+ `-Encoding utf8NoBOM`.
- After commit, confirm `git log -1 --format=%s` has no leading BOM / mojibake.

### Push preflight (when plan requires `git push` / remote publish)

Run **before** commit+push (**dual preflight**): user terminal push success ≠ agent Shell ready.

1. **Remote:** `git remote -v` (https vs ssh) and tracking branch.
2. **Agent git binary (Windows HTTPS):** Prefer **Git for Windows** over MSYS when they differ:
   - Resolve via `where.exe git` and `(Get-Command git).Source`.
   - Prefer a path under `...\Git\cmd\git.exe` (or any listed binary whose `git config --get credential.helper` is `manager` / GCM).
   - MSYS (`...\msys64\usr\bin\git.exe`) often has **no** `credential.helper` → non-TTY push fails with `terminal prompts disabled`.
   - Invoke push/preflight with the **GfW absolute path**; do **not** require machine-wide PATH rewrite.
3. **Credential probe:** Using the chosen binary, `git credential fill` (protocol/host only) or `git push --dry-run`. Do **not** force `GCM_INTERACTIVE=0` / `GIT_TERMINAL_PROMPT=0` on the first GCM probe (those flags are OK for MSYS fail-fast only).
4. **`gh`:** Record present/absent. Missing `gh` alone is **not** a credential failure when GCM fill/dry-run succeeds.
5. **Never log secrets:** no PATs, tokens, credential fill `password=` lines, or full env dumps. `GITHUB_TOKEN` existence may be noted boolean-only.

### Status honesty (push / pull / credentials)

- If a required `git push` or agent push preflight fails: set **`status: blocked`**, leave any local commit in place, report remediation by `blocker_type`. Do **not** use `complete`.
- If a required **`git pull` / sync** aborts on **unrelated** dirty tree, fails auth/non-ff, or aborts on content conflict under Q3b=A: set **`status: blocked`**, outcome e.g. `aborted_dirty` / `non_ff` / `blocked_conflict`, `blocker_type: dirty_working_tree` | `other` | auth types. Do **not** claim pull succeeded; do **not** use `complete`.
- Before the dirty handler: **fetch/count ahead-behind**. When dirt ⊆ allowlist only:
  - **Behind > 0:** **stash allowlist → `git pull --ff-only` → stash pop** (same GfW binary); optional allowlist commit after pop. Never `stash drop` on conflict — fail-closed, leave stash recoverable.
  - **Not behind:** **auto-commit** allowlisted paths (BOM-safe message), then `git pull --ff-only`.
  - Do **not** merge/rebase on non-ff unless plan/user changed combine strategy (Q2≠A).
- On **content conflicts** during combine: follow locked **Q3b**. Default **A** = abort (`merge --abort` preferred), tip recoverable, `other`/`merge_conflict`. **B** = resolve **only** if every unmerged path ⊆ allowlist, using the documented R1 rule from `notes.md` (`ours` / `theirs` / `combined` / **`combined-best`**). If Q3b=B is locked for **finish-sync continuity** and R1 is blank → apply **`combined-best`** (study both sides per hunk; keep most appropriate; log judgment trail). Any outside-allowlist conflict → abort like A. Never silent-resolve under A.
- Prefer **GfW absolute path** for dirty gate, allowlist commit/stash, **and** pull (same binary) — PATH/MSYS alone can skew porcelain and credentials.
- `partial` is only for unfinished planned work that is still actionable by implementer without user secrets/auth.
- Never claim Done when any acceptance criterion (e.g. push OK / pull sync OK) is unmet.

### `blocker_type` (push / pull failures)

| Value | Meaning | Example remediation |
| --- | --- | --- |
| `none` | No blocker | — |
| `dirty_working_tree` | Pull/sync aborted: **unrelated** (non-allowlist) dirty under abort policy (auth may be green) | User clean/stash/commit those paths; **new** pull cycle — do not relaunch on same unrelated dirty tree |
| `agent_environment` | Wrong git on PATH, missing helper on default binary, sandbox/Legacy Terminal blocking GCM | Use GfW absolute `git.exe`; Cursor Run Modes / less sandbox / Legacy Terminal ([Run Modes](https://cursor.com/docs/agent/security/run-modes)) |
| `user_credentials` | No credential store entry / need login / SSH key setup | User `gh auth login`, GCM re-auth, or SSH setup |
| `plan_gap` | Plan incomplete or wrong | Return to planner |
| `other` | Unclassified **or** expected **`non_ff`** (history diverge / ff-only refuse) **or** **`merge_conflict`** / outcome `blocked_conflict` (content conflicts; Q3b=A abort or non-allowlist conflict) | Session **`blocked`**; sync unmet; **do not** claim pull succeeded. Keep WIP/stash recoverable. Next: for `non_ff` Choose Q2 B/C or recover+Q3c; for **allowlist-only** `merge_conflict` → next FAW continuity **Q3b=B** + **`combined-best`** (agent-owned); for non-allowlist conflicts → user scopes those paths — still no force/hard reset |

Do **not** classify as `user_credentials` solely because `gh` is missing when GCM works.
Do **not** classify unrelated dirty-abort as `agent_environment` or `user_credentials`.
Do **not** use `dirty_working_tree` when dirt was allowlisted-only and agent used commit and/or Q3c stash — use `other`/`non_ff` if `--ff-only` then refuses.

### Fallbacks (secondary; only if GfW+GCM still fails after PATH/git fix)

- (B) Install `gh` + `gh auth login` / `credential.helper '!gh auth git-credential'`.
- (C) SSH remote + key agent — do **not** rewrite `origin` to SSH by default.
- Cursor Settings: less sandbox / Legacy Terminal / approve elevated run.

## Output (return to orchestrator)

```markdown
## Implementation result
- status: complete | partial | blocked
- changes_path: ...
- log_path: ...
- verification: pass | fail | skipped (why)
- blocker_type: none | dirty_working_tree | user_credentials | agent_environment | plan_gap | other
- deviations_from_plan: [none | list]
```
