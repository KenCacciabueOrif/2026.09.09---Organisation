# Refined prompt

> **Status:** finalized — all clarifying questions answered.

## Goal

Stage **all** current dirty and untracked files in `c:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` (including `README.md`, `.cursor/`, `AGENTS.md`, `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`, `sessions/`, and any other present changes), create **one** git commit on `main` with an auto-generated message from the staged diff (repo style; no fixed user-supplied message), then **push** `main` to `origin` only (no PR). Return commit hash, push success, and `git status`.

## Constraints

- User **explicitly** requested add + commit + push — proceed only within that scope.
- **Stage everything** in the working tree (tracked modifications + untracked); no path exclusions except the secrets gate.
- **Commit and push on `main`**; do not create a feature branch.
- **Push only to `origin`**; do not open a PR / do not use `gh pr create`.
- **Commit message:** auto-generate from the staged diff and recent log style (plain, why-focused; match existing history such as `Initial commit`); do not ask for or wait on a fixed user message.
- Follow user/repo git safety: never update `git config`; never force-push; never `--no-verify` / skip hooks; no amend unless the usual amend-safety rules are fully met (prefer a new commit if hooks reject).
- On Windows PowerShell, pass the commit message in a HEREDOC-equivalent safe multi-line form (user rule: HEREDOC-style); do not use interactive git (`-i`).
- **Secrets gate still applies:** never stage or commit secrets (`.env`, credentials, keys, tokens). If suspected secrets appear, **stop** and report paths — do not commit or push. No extra must-exclude paths beyond that.
- Do not change application/product code beyond what is already in the working tree for this publish task.
- Do not rewrite history; do not delete remote branches.
- **Verification:** commit hash + push OK + `git status` only — no remote/`gh`/Actions verification.

## Context pointers

- Repo root: `c:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`
- Branch: `main` tracking `origin/main`
- Remote: `origin` → `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git`
- Recent style sample: single commit `9e00fd9 Initial commit`
- Expected staging set (re-check at implement time): modified `README.md`; untracked `.cursor/`, `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`, `AGENTS.md`, `sessions/`, plus any other dirty/untracked present then
- Safety docs: `AGENTS.md`, user committing-changes / push rules
- Session artifacts: `sessions/2026.09.09-0831/`

## Acceptance criteria

- [ ] `git status` / `git diff` / `git log` reviewed before staging.
- [ ] All dirty and untracked paths staged (full tree), except any secret/credential-like files which must be left out and reported with a halt.
- [ ] No secret or credential-like files in the index; if found among candidates, halt with a clear report (no commit/push).
- [ ] Exactly one new commit on `main` with a concise, why-focused message auto-derived from the staged diff and aligned to repo log style.
- [ ] Commit created via non-interactive, HEREDOC-style message; hooks not skipped.
- [ ] `main` pushed to `origin` successfully without `--force` / `--force-with-lease`.
- [ ] Final report includes: commit hash, confirmation that push succeeded, and post-push `git status` (no `gh`/remote page checks required).

## Out of scope

- Opening a pull request / using `gh pr create`
- Creating a feature branch
- Force-push, rebase, reset, amend of others’ commits, or git config changes
- Implementing new product features or fixing unrelated bugs
- Extra remote verification (`gh`, Actions, browsing GitHub)
- Deep domain research beyond what is needed to write an accurate commit message from the diff
