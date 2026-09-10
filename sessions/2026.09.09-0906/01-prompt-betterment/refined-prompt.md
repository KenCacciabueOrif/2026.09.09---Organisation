# Refined prompt

> **Status:** finalized — clarifying answers locked from `2026.09.09-0831` + Option A from `2026.09.09-0850`; no re-ask needed.

## Goal

Stage **all** current dirty and untracked files in the organisation repo, create **one** git commit on `main` with an auto-generated message from the staged diff (repo style), then **push** `main` to `origin` from **agent Shell** (no PR). Prefer **Git for Windows + GCM** when PATH `git` is MSYS / lacks a credential helper. Return commit hash, push success, and `git status`.

## Constraints

- User **explicitly** requested add + commit + push — proceed only within that scope.
- **Stage everything** in the working tree (tracked modifications + untracked); no path exclusions except the secrets gate.
- **Commit and push on `main`**; do not create a feature branch.
- **Push only to `origin`**; do not open a PR / do not use `gh pr create`.
- **Commit message:** auto-generate from the staged diff and recent log style (plain, why-focused); do not ask for a fixed user message.
- Follow git safety: never update `git config`; never force-push; never `--no-verify` / skip hooks; no amend unless amend-safety rules are fully met (prefer a new commit if hooks reject); no interactive git (`-i`).
- **Windows PowerShell commit message:** BOM-safe — use here-string `-m`, `utf8NoBOM`, or `UTF8Encoding($false)`; do **not** use Windows PS 5.1 `Set-Content -Encoding utf8` (adds BOM).
- **Option A agent push (mandatory for this goal):**
  - Early **dual preflight**: remote/tracking **and** agent git binary / `credential.helper` / GCM usability (fill or `push --dry-run` without printing secrets).
  - User-terminal push success ≠ agent ready.
  - On Windows HTTPS: if PATH git is MSYS or has no helper, invoke **Git for Windows** `git.exe` (absolute path) for credential probe and push.
  - Do **not** force `GCM_INTERACTIVE=0` / `GIT_TERMINAL_PROMPT=0` on the first GCM probe (those flags OK for MSYS fail-fast only).
  - Missing `gh` alone ≠ missing credentials when GCM works.
  - Fail-closed: if agent push fails, session `blocked` with `blocker_type` `agent_environment` vs `user_credentials`; never false `complete`; still run self-improver.
- **Secrets gate:** never stage/commit secrets (`.env`, credentials, keys, tokens). If suspected secrets appear, **stop** and report paths. **No secrets in session logs** (credential fill: success/fail + exit codes only).
- Do not rewrite history; do not delete remote branches; do not invent unrelated product work.
- **Verification:** commit hash + push OK + `git status` only — no remote/`gh`/Actions page checks.

## Context pointers

- Repo root: `c:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`
- Branch: `main` (expect tracking `origin/main`)
- Remote: `origin` (HTTPS GitHub; confirm at implement time)
- Prior publish defaults: `sessions/2026.09.09-0831/01-prompt-betterment/refined-prompt.md`
- Option A (GfW+GCM, dual preflight): `sessions/2026.09.09-0850/` (research brief, plan, implementer/skill/`AGENTS.md` updates)
- Workflow law: `AGENTS.md`, `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/agents/implementer.md`
- Session artifacts: `sessions/2026.09.09-0906/`

## Acceptance criteria

- [ ] Dual preflight recorded before commit+push: remote/tracking + agent git path/helper/GCM evidence; `gh` presence noted but not sole credential signal.
- [ ] `git status` / `git diff` / `git log` reviewed before staging (using the same git binary intended for commit/push when relevant).
- [ ] All dirty and untracked paths staged (full tree), except any secret/credential-like files left out and reported with a halt.
- [ ] No secret or credential-like files in the index; no secrets written to session logs.
- [ ] Exactly one new commit on `main` with a concise, why-focused message auto-derived from the staged diff and aligned to repo log style.
- [ ] Commit message applied BOM-safe / non-interactive; hooks not skipped.
- [ ] `main` pushed to `origin` successfully via agent Shell without `--force` / `--force-with-lease`, using GfW+GCM when PATH git is MSYS/no helper.
- [ ] Final report includes: commit hash, push succeeded, and post-push `git status` (no `gh`/remote page checks required).
- [ ] If push cannot proceed non-interactively: status `blocked` + correct `blocker_type`; never mark `complete`; self-improver still runs.

## Out of scope

- Opening a pull request / using `gh pr create`
- Creating a feature branch
- Force-push, rebase, reset, unsafe amend, or git config changes
- Implementing new product features or fixing unrelated bugs
- Extra remote verification (`gh`, Actions, browsing GitHub)
- Rewriting `origin` to SSH by default (fallback only if Option A preflight fails after GfW attempt)
- Re-encoding Option A docs (already done in `2026.09.09-0850`) unless a material gap blocks this push
