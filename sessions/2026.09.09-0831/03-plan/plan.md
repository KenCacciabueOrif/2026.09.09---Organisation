# Plan

## Goal

Publish the organisation repo’s full agent-workflow scaffolding by staging **all** current dirty and untracked files at repo root `c:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` (secrets gate only), creating **exactly one** new commit on `main` with an auto-generated why-focused message aligned to existing history (`Initial commit` style), then pushing `main` to `origin` without force and without a PR. Done when the implementer reports commit hash, push success, and post-push `git status`.

## Acceptance criteria

- [ ] Pre-stage review: `git status`, `git diff` (unstaged), and `git log` inspected at implement time.
- [ ] Secrets gate passed: no `.env` / credentials / keys / tokens staged; if any found among candidates, halt with paths reported (no commit, no push).
- [ ] All dirty + untracked paths staged via full-tree add (`git add -A` or equivalent from repo root); no extra path excludes beyond secrets.
- [ ] Staged set re-checked (`git diff --staged --stat` / name-status) before commit.
- [ ] Exactly one new commit on `main`; message concise, why-focused, derived from staged diff (theme: add/publish full agent workflow scaffolding); hooks not skipped (`--no-verify` forbidden).
- [ ] Commit message passed non-interactively via PowerShell here-string **or** `git commit -F <file>` (no bash HEREDOC unless shell is bash; no interactive `-i`).
- [ ] `git push origin main` (or tracking push) succeeds with **no** `--force` / `--force-with-lease`.
- [ ] Final report includes: commit hash (`git rev-parse HEAD`), push OK, and post-push `git status` only (no `gh` / remote page / Actions checks).

## Steps

1. **Pre-flight snapshot** — repo root — Run in parallel: `git status`, `git diff`, `git log -5 --oneline` (confirm on `main`, tracking `origin/main`, note dirty/untracked set; may differ from research snapshot). — verify: branch is `main`; remote `origin` present; list of candidates captured for secrets gate.

2. **Secrets gate** — candidate paths from status (expect `README.md`, `.cursor/`, `AGENTS.md`, `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`, `sessions/`, plus any new dirt) — Scan filenames for secret-like patterns (`.env`, `credentials`, `*.pem`/`*.key`, `token`, `password`, `id_rsa`, `.p12`, `.pfx`, etc.); spot-check content if names are ambiguous. — verify: **halt** with clear path report if anything suspicious; otherwise proceed. Do not stage secrets.

3. **Stage everything** — repo root — `git add -A` (or `git add .`). — verify: `git status` shows intended paths staged; nothing secret in the index.

4. **Review staged diff** — index — `git diff --staged --stat` and `git diff --staged --name-status`. — verify: staging set matches “all non-secret changes”; coherent single-commit theme (workflow scaffolding + README + sessions).

5. **Draft commit message** — from staged diff + `git log` style — Prefer short plain subject, e.g. `Add full agent workflow scaffolding and session layout` (implementer may trim to match final diff). Optional one-line body if needed; avoid inventing Conventional Commits unless clearly better. — verify: message answers *why* (publish usable agent workflow), not a file laundry list.

6. **Commit once** — index → `main` — Create commit **without** `--no-verify`, using PowerShell (user shell):
   - Preferred: `git commit -m @'<newline>subject<newline><newline>EOF-style body if any<newline>'@` (literal here-string), **or**
   - Safer cross-shell: write message to a temp file then `git commit -F <msgfile>` and delete the file after.
   — verify: `git log -1 --format='%H %s'` shows new commit; exit code 0. If hooks reject: **do not amend** unless amend-safety rules fully apply; fix and create a **new** commit.

7. **Push to origin** — `main` → `origin/main` — `git push origin main` (no force flags). — verify: push exits 0. On auth/protection failure: report error; do not force; do not open a PR.

8. **Done report** — local git only — Capture `git rev-parse HEAD`, confirm push succeeded, run `git status`. — verify: clean or expected post-push state (typically clean working tree, `main` in sync with `origin/main`); return hash + push OK + status text to orchestrator/user. No `gh`, no browsing GitHub, no Actions checks.

## Non-goals

- Opening a PR / `gh pr create` / merge workflows
- Feature branch creation
- Force-push, rebase, reset, history rewrite, `git config` changes
- Skipping hooks (`--no-verify`)
- Extra excludes beyond the secrets gate
- Adding `.gitignore` (unless a secret forces a halt — then stop and report; do not silently expand scope)
- Product/application feature work unrelated to publishing the current tree
- Remote verification beyond push exit success

## Risks / rollback

| Risk | Mitigation / rollback |
| --- | --- |
| Secrets in tree | Halt before add/commit/push; report paths; never push secrets |
| Push rejected (auth / branch protection / secret scanning on GitHub) | Report failure; leave local commit in place; no force; user remediates auth/protection |
| PowerShell vs bash message corruption | Use PowerShell here-string or `git commit -F`; confirm `git log -1` |
| Working tree grows mid-session | Re-run status in step 1; stage full tree again after secrets gate |
| Bad commit already created but not pushed | Prefer new corrective commit over amend; amend only if user/amend-safety rules allow |
| Bad commit already pushed | Do not force-push; report and ask user for next steps |
| Large noisy `sessions/` stubs | Accepted by “stage everything”; keep message at scaffolding/session-layout level |

**Rollback note:** If commit succeeds but push fails, local history has one extra commit — leave it; do not reset unless user explicitly requests. If nothing was pushed, user can still discard locally with an explicit reset request (out of default implementer scope).

## Ready to implement

yes

## Blocking questions

none

## Approach note (research Option A)

Secrets gate → `git add -A` → one commit (PowerShell here-string or `-F`) → `git push origin main` (no force). Options B/C not used (B redundant; C forbidden by user).
