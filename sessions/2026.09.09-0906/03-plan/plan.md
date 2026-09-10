# Plan

## Goal

Stage **all** dirty and untracked files in the organisation repo (secrets gate only), create **exactly one** commit on `main` with an auto-generated, why-focused message from the staged diff and recent log style, then **push** `main` to `origin` from agent Shell using the locked Git for Windows absolute binary `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (GCM). No PR, no force, no `--no-verify`, no git config changes. Report commit hash, push success, and post-push `git status`. Fail-closed with `blocker_type` if agent push regresses.

## Acceptance criteria

- [ ] Dual preflight recorded before commit+push: remote/tracking + agent git path/helper/GCM evidence; `gh` presence noted but not sole credential signal.
- [ ] `git status` / `git diff` / `git log` reviewed before staging (prefer GfW binary for commit/push-adjacent ops).
- [ ] All dirty and untracked paths staged (full tree), except any secret/credential-like files left out and reported with a halt.
- [ ] No secret or credential-like files in the index; no secrets written to session logs.
- [ ] Exactly one new commit on `main` with a concise, why-focused message auto-derived from the staged diff and aligned to repo log style.
- [ ] Commit message applied BOM-safe / non-interactive; hooks not skipped (`--no-verify` forbidden).
- [ ] `main` pushed to `origin` successfully via agent Shell without `--force` / `--force-with-lease`, using locked GfW path:
  `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe`
- [ ] Final report includes: commit hash, push succeeded, and post-push `git status` (no `gh`/remote page checks required).
- [ ] If push cannot proceed non-interactively: status `blocked` + correct `blocker_type` (`agent_environment` vs `user_credentials`); never mark `complete`; self-improver still runs.

## Steps

1. **Dual auth/preflight (mandatory before commit+push)** — Repo root `c:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`. Using GfW:
   `$gfw = 'C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe'`
   - Confirm `main` tracks `origin/main`; `git remote -v` shows HTTPS `origin`.
   - Record PATH git (`Get-Command` / `where.exe`) vs GfW; PATH helper none vs GfW `credential.helper manager`.
   - Re-run non-secret GCM probe: GfW `credential fill` and/or `push --dry-run` (exit codes + booleans only; **never** log passwords/tokens/`GITHUB_TOKEN` value).
   - Note `gh` absent (optional only); do **not** treat as credential failure.
   - Do **not** set `GCM_INTERACTIVE=0` / `GIT_TERMINAL_PROMPT=0` on the GCM probe (those flags OK for MSYS fail-fast only).
   - Research already green; if live probe fails → stop, classify `agent_environment` vs `user_credentials`, do not proceed to push.  
   — verify: preflight notes in `04-implementation/` (or handoff) show HTTPS + GfW ready; `blocker_type: none` or halt.

2. **Review working tree** — Same GfW binary preferred. Run in parallel:
   - `git status`
   - `git diff` / `git diff --stat` (and untracked listing)
   - `git log -5 --oneline` (imperative short subjects)  
   — verify: implementer understands diff theme (Option A tooling + session artifacts) before staging.

3. **Secrets gate** — Scan porcelain / untracked names for `.env`, credentials, keys, tokens, private key material, credential dumps. Research: none at brief time; **re-scan at implement time**. If any suspected → **stop**, report paths, stage nothing secret, do not commit.  
   — verify: no secret-like paths staged; session logs contain no secret values.

4. **Stage all** — From repo root: `git add -A` (full tree). No path exclusions except secrets halt from step 3. Include late `sessions/2026.09.09-0906/` artifacts created after research.  
   — verify: `git status` shows intended paths staged; empty secrets-like set in index.

5. **Auto commit message + one commit on `main`** — Still on `main` (no feature branch). Draft concise why-focused subject from staged diff + recent log style (imperative). Commit **BOM-safe** on Windows PowerShell:
   - Prefer: `git commit -m @'...message...'@` (here-string), or message file via `utf8NoBOM` / `UTF8Encoding($false)`.
   - **Forbidden:** `Set-Content -Encoding utf8` (PS 5.1 BOM).
   - Use GfW for commit if PATH/MSYS would diverge; hooks run normally — **no** `--no-verify`, **no** amend unless amend-safety rules fully met (prefer new commit if hook rejects).
   - Never `git config` updates.  
   — verify: exactly one new commit; `git rev-parse HEAD` recorded; message has no leading BOM; hooks not skipped.

6. **Push `main` to `origin` (GfW only)** — Invoke locked binary only:
   `& 'C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe' push origin main`
   (or `push origin HEAD` while on `main`). No `--force` / `--force-with-lease`. Do **not** use PATH/MSYS git for push. No `gh pr create`.  
   — verify: push exit 0; record success in implementation log.

7. **Final report** — Capture and return:
   - Commit hash
   - Push succeeded (yes/no)
   - Post-push `git status`  
   No remote page / Actions / `gh` verification. Write session implementation notes under `sessions/2026.09.09-0906/04-implementation/`. On push failure: mark session `blocked` with correct `blocker_type`; leave local commit; never false `complete`.  
   — verify: acceptance checklist items closed or honest block documented.

## Non-goals

- Opening a pull request / `gh pr create`
- Creating a feature branch
- Force-push, rebase, hard reset, unsafe amend, or `git config` changes
- Using PATH/MSYS `git` for the authenticated push
- Rewriting `origin` to SSH by default (fallback only if GfW push fails after attempt)
- Installing/`gh`-based credential helper as primary path
- Extra remote verification (`gh`, Actions, browsing GitHub)
- Implementing new product features or fixing unrelated bugs
- Re-encoding Option A docs unless a material gap blocks this push

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| PATH/MSYS `git push` (no helper / no TTY) | **Locked:** always use GfW absolute path for credential probe + push; classify miss as `agent_environment` |
| Accidental secret staging | Re-scan before `git add`; halt and report paths |
| UTF-8 BOM in commit subject | Here-string `-m` or utf8NoBOM file; never PS 5.1 `Set-Content -Encoding utf8` |
| Force / `--no-verify` / config edits | Explicitly forbidden; auditor checks |
| Push fails after local commit | Leave commit; `blocked` + `blocker_type`; do not mark complete; self-improver still runs |
| Missing `gh` misread as auth failure | Optional signal only; GCM fill/dry-run is the credential evidence |
| Sandbox/GCM regression mid-run | Fail-closed; `agent_environment` vs `user_credentials`; do not invent SSH rewrite as default |
| Rollback | If commit unwanted before push: user-directed revert only (no force on remote). After successful push: revert commit + normal push (no force). |

## Ready to implement

**yes**

Research dual preflight: GfW `credential fill` + `push --dry-run` pass in agent Shell; HTTPS `origin`; secrets gate clear. Locked GfW path for push. No user credential blocking question. Missing `gh` is not a blocker.

## Blocking questions

none
