# Plan — Publish cycle (`sessions/2026.09.09-1246`)

## Goal

Publish the organisation repository by staging **all non-secret** modified and untracked work **inside this git root only**, creating **exactly one** agent-drafted why-focused commit (BOM-safe on Windows), and having **agent Shell** successfully non-force push to **`origin/main`**. Use dual preflight preferring Git for Windows + GCM; fail-closed (session `blocked`, typed `blocker_type`) if agent push fails. Mutation class **`docs_only`** — git ops and session log writes only; **zero intentional corpus FS mutations** (no moves/renames/deletes).

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`docs_only`** |
| Corpus FS | **Zero intentional corpus FS mutations.** Implementer may only write/edit session artifacts under `sessions/2026.09.09-1246/` (and normal git index/commit/push). No move/rename/delete of corpus paths. |
| User approval before implementer | **Not required** for corpus moves (none planned). Plan-gate for FS mutation is **optional / skipped**. |
| First-move gates | **N/A** — this is not an Early/simple or first `fs_mutation` batch. |
| Implementer attestation | Before staging, log in `04-implementation/log.md`: “attested: zero intentional corpus FS mutations this cycle.” |

### Taxonomy / must-preserve (out of scope)

Do **not** update ratification or lock status. Program-level language remains: taxonomy **proposed-ratified — ready for user sign-off** (not final ratified); must-preserve **draft — not auto-locked**. No AC claims final sign-off.

## What the user is approving

**N/A for FS mutation** — no path map. Orchestrator may optionally confirm publish intent, but **no mandatory plan gate** before implementer.

If asked informally: “yes” means one catch-up commit of all non-secret dirty work in this org repo pushed to `origin/main`; “no” means do not commit/push.

## Acceptance criteria

- [ ] All git operations confined to `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`; nothing outside this root is staged or committed.
- [ ] All non-secret project work under the root is staged; only default secret/junk exclusions; staged paths spot-checked for secrets (name scan).
- [ ] Required `sessions/2026.09.09-1246/` (and other in-root session) artifacts that belong in this publish are written **before** `git commit`.
- [ ] Exactly **one** new commit contains the staged set.
- [ ] Commit message is agent-drafted **after** staging, why-focused, repo-style (imperative, ≤ ~72 chars subject), **no UTF-8 BOM**.
- [ ] Dual preflight completed for agent push (remote + GfW/GCM); remote name and branch printed before push.
- [ ] Non-force `git push` to **`origin/main`** succeeds from **agent Shell** using GfW absolute path (not PATH/MSYS alone).
- [ ] If push fails: session marked **blocked** (not complete); `blocker_type` set (`agent_environment` vs `user_credentials`); do not claim publish success.
- [ ] After success: `git status -sb` shows clean tracking **or** only expected post-push session dirtiness; `git log -1` and upstream reflect the new commit on `origin/main`.
- [ ] Implementation log attests **zero intentional corpus FS mutations**.

**Soft / include-when-cheap (not hard AC):** exact file count in log; `gh` presence note; optional post-push finalize note left dirty (Q7=A).

## Steps

### 1. Dual auth / preflight (mandatory before commit+push)

**Paths:** repo root only; git binary `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (alias `$gfw` in log).

**Action:**

1. Confirm `git rev-parse --show-toplevel` is this org root.
2. Print remote: `origin` → `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` (HTTPS); branch `main` tracking `origin/main`.
3. Record PATH `git` (`where.exe git`) — expect MSYS first (`C:\msys64\usr\bin\git.exe`) with **no** `credential.helper` → **do not use for push**.
4. Prefer GfW: `$gfw = 'C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe'`; confirm `credential.helper` includes `manager`.
5. Non-secret GCM check: GfW `credential fill` for `https://github.com` → booleans only (`has_username` / `has_password`); **never log secrets**.
6. GfW `push --dry-run origin main` with `GIT_TERMINAL_PROMPT=0` → expect exit 0.
7. Note `gh` absent = **optional only**; not a credential blocker while GCM works.
8. Note: user-terminal push history ≠ agent-ready alone.

**Verify:** Agent can push non-interactively via GfW. If live preflight regresses → **stop**, set `blocker_type`, mark session blocked; do not proceed hoping PATH/MSYS will work.

| Outcome | `blocker_type` |
| --- | --- |
| Wrong/MSYS git used / sandbox blocks GCM | `agent_environment` |
| GCM fill fails / no stored creds / need login | `user_credentials` |
| Missing `gh` only, GCM OK | **none** (continue) |

### 2. Write pre-commit session logs

**Paths:** `sessions/2026.09.09-1246/04-implementation/log.md` (and any other required phase stubs that should land in the publish commit).

**Action:** Fill implementation log with: preflight results (booleans), attested zero corpus FS mutations, intended stage scope summary, push plan (GfW absolute path). Write **before** `git commit`.

**Verify:** Log file exists and is non-stub for preflight + attestation sections.

### 3. Secrets / junk re-scan

**Paths:** full porcelain under this root (`git status --porcelain`).

**Action:** Name-scan for `.env`, credentials, private keys, tokens, obvious junk. Default excludes only (Q5=A). Research found none; re-scan after step 2 writes.

**Verify:** No secret-like paths staged; any hits → halt and report (do not commit).

### 4. Stage all non-secret work (this root only)

**Paths (expected catch-up set — freeze at implement time):**

- Modified: `.cursor/agents/*`, `.cursor/rules/full-agent-workflow.mdc`, `.cursor/skills/full-agent-workflow/**`, `AGENTS.md`, `README.md`, prior sessions `0850`/`0906`, `sessions/_templates/*`
- Untracked: `catalogue/`, `program/`, `sessions/2026.09.09-0929/`, `1009/`, `1032/`, `1246/`

**Action:** From repo root only: `git add -A` (or equivalent). Never `cd` to parent `C:\Project` or stage outside this `.git`.

**Verify:** `git diff --cached --name-only` lists only paths under this root; includes `sessions/2026.09.09-1246/` logs written in step 2; no secret paths.

### 5. One BOM-safe commit

**Action:** After staging, draft why-focused subject (imperative, ≤ ~72 chars; match `4de6aeb` style — e.g. publish catch-up of FAW/catalogue/session history so `origin/main` matches local). Commit with PowerShell **here-string** `-m` or `UTF8Encoding($false)` — **never** Win PS 5.1 `Set-Content -Encoding utf8`. Exactly **one** commit. No `--no-verify`, no amend of already-pushed commits, no git config changes.

**Verify:** `git log -1 --format=%B` has no leading BOM/`﻿`; one new commit ahead of previous `origin/main`; `git status` shows clean index (working tree may still have nothing if all staged).

### 6. Push via GfW absolute path

**Action:**

1. Print remote URL and branch (`origin` / `main`).
2. Run: `& 'C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe' -C '<repo-root>' push origin main` (non-force). Prefer absolute GfW for **all** push-related commands in this step.
3. Do **not** use PATH/MSYS `git` for push.

**Verify:** Push exit 0; `git status -sb` shows `main...origin/main` in sync (or only expected post-push dirtiness); remote `git log -1` matches local.

### 7. Fail-closed handling (if step 6 fails)

**Action:** Mark session **blocked** (not complete). Classify `blocker_type` (`agent_environment` vs `user_credentials`). Leave local commit if already created; do **not** claim publish success; do **not** treat user-terminal push as substitute for agent success. Document in implementation log + session status.

**Verify:** Status artifacts say `blocked` + typed blocker; AC “push succeeded” remains unchecked.

### 8. Post-success finalize note (allowed dirty)

**Action:** Append push hash / verification to `04-implementation/log.md` (and auditor-facing notes if needed). Per Q7=A / AGENTS.md: **post-push session dirtiness is OK** — do not fail the cycle solely for that; optional tiny session-only follow-up commit is **out of scope** unless user later asks.

**Verify:** Success criteria met; dirty finalize files (if any) documented as expected.

## Non-goals

- Any path outside this organisation git root (other `C:\Project\...` trees)
- Corpus inventory moves, renames, deletes
- Taxonomy final ratification; must-preserve auto-lock
- Force-push, history rewrite, amending published commits, skipping hooks, changing git config
- Creating a PR
- Multiple commits for this publish
- Installing/configuring `gh` or switching remote to SSH (fallback only if Option A fails and user approves)
- Treating “user terminal can push” as success when agent push failed
- Marking complete if only a local commit exists without successful agent push

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| PATH/MSYS `git push` fails non-interactively | Always use GfW absolute path; classify misuse as `agent_environment` |
| Accidental secret staging | Re-scan before add; halt on hits |
| UTF-8 BOM in commit subject | Here-string `-m` / utf8NoBOM only |
| Mixed-topic single commit (hard to revert by topic) | Locked Q6=A; explain “why” in message |
| Claiming complete on local-only commit | Fail-closed AC; auditor checks remote |
| Post-push log dirtiness | Expected (Q7=A); do not fail cycle |
| GCM/DPAPI regression mid-run | Re-run step 1; stop with typed blocker |
| Missing `gh` | Not a blocker while GCM verified |

**Rollback:** If commit created but push failed — leave local commit; do not force-push or reset unless user explicitly asks. If bad commit before push — user may request reset; implementer must not force-push.

## Ready to implement

**yes**

Research verified GfW + GCM fill and `push --dry-run` succeed. Missing `gh` is not a blocker. Implementer must re-confirm dual preflight at start; if it regresses, stop and block (do not green-light hoping PATH git works).

## Blocking questions

**none**

## Plan meta (for orchestrator)

| Field | Value |
| --- | --- |
| `ready_to_implement` | **yes** |
| Mutation class | **`docs_only`** |
| User plan gate required | **no** (optional confirm only) |
| Recommended approach | Research Option A — stage-all → one BOM-safe commit → GfW push |
| Step count | **8** |
| AC count | **10** hard checkboxes (+ soft notes) |
