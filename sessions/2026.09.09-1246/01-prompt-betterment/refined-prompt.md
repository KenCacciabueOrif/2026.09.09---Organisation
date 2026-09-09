# Refined prompt

## Goal

Publish the organisation repository by staging all non-secret project work **inside this git root only**, creating **exactly one** commit with an agent-drafted why-focused message, and having the **agent Shell** successfully push to **`origin/main`** (non-force) — with dual Windows GfW/GCM preflight and **fail-closed** if push fails. No corpus file moves/renames/deletes.

**One-liner:** Git add → one commit → agent push of this org repo only to `origin/main`; fail closed if agent push cannot complete.

## Constraints

- **Git root boundary (hard):** Operate only in `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`. Do **not** `git add`, commit, or push anything from other folders under `C:\Project` or any other path outside this repository.
- Mutation class: **docs_only** (git ops + session log writes as needed). No corpus FS moves/renames/deletes.
- Stage **all** non-secret modified and untracked project work under this root (default secret/junk exclusions only).
- Include `sessions/2026.09.09-1246/` artifacts that exist at commit time; write required session/implementation logs **before** `git commit`.
- Exactly **one** commit for this publish, then push.
- Commit message: agent drafts **after** staging — why-focused, match recent repo style, subject ≤ ~72 chars; Windows PowerShell message file **without UTF-8 BOM**.
- No secrets in the commit (scan staged paths; never stage `.env`, credentials, private keys, or obvious junk).
- No force-push; no `--no-verify` / hook skip; do not amend already-pushed commits; do not change git config.
- **Agent Shell must push:** dual preflight — (1) remote/`origin` health, (2) agent `git` + credential helper; prefer **Git for Windows + GCM** when PATH `git` is MSYS without helper. Missing `gh` alone ≠ missing credentials when GCM works.
- **Fail-closed:** if agent push fails, mark session **blocked** (`blocker_type`: `agent_environment` vs `user_credentials`); never mark complete on local-only commit.
- Taxonomy / must-preserve: **out of scope** (do not claim final ratification; any future lists stay **proposed-ratified — ready for user sign-off** / **draft — not auto-locked**).

## Context pointers

- Repo root: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`
- `program/ROADMAP.md`, `program/CHARTER.md` (this cycle is Publish, not a ROADMAP Early/simple row)
- Prior sessions: `sessions/2026.09.09-1009/`, `sessions/2026.09.09-1032/`
- This session: `sessions/2026.09.09-1246/`
- Workflow law: `AGENTS.md`, `.cursor/skills/full-agent-workflow/SKILL.md`
- Tracking: `main` ↔ `origin/main`; remote `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git`
- Locked answers: `sessions/2026.09.09-1246/01-prompt-betterment/notes.md`

## Acceptance criteria / verification

- [ ] All git operations confined to this org-repo git root; nothing outside the root is staged or committed.
- [ ] All non-secret project work under the root is staged; only default secret/junk exclusions applied; staged paths spot-checked for secrets.
- [ ] Required `sessions/2026.09.09-1246/` (and other session) logs that belong in this publish are written **before** `git commit`.
- [ ] Exactly **one** new commit contains the staged set.
- [ ] Commit message is agent-drafted after staging, why-focused, repo-style, no BOM.
- [ ] Dual preflight completed for agent push (remote + GfW/GCM as needed); remote name and branch printed before push.
- [ ] Non-force `git push` to **`origin/main`** succeeds from **agent Shell**.
- [ ] If push fails: session marked **blocked** (not complete); blocker typed; do not claim publish success.
- [ ] Verify after success: `git status -sb` shows clean tracking (or only expected post-push session dirtiness); `git log -1` and upstream reflect the new commit on `origin/main`.

## Out of scope

- Any path outside this organisation git root (other `C:\Project\...` trees)
- Corpus inventory moves, renames, deletes; taxonomy ratification; must-preserve locking
- Force-push, history rewrite, amending published commits, skipping hooks, changing git config
- Creating a PR
- Multiple commits for this publish
- Treating “user terminal can push” as success when agent push failed
- Marking complete if only a local commit exists without successful agent push
