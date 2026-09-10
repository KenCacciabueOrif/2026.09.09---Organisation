# Refined prompt

## Goal

Sync the organisation repo with `origin` by having the **agent** successfully run `git pull --ff-only` on `main` (tracking `origin/main`), only inside this repo’s git root, and document the outcome in the current FAW session.

## Constraints

- **Git root (hard):** All git ops only in `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`. Never stage, fetch, pull, or otherwise operate on sibling trees under `C:\Project`.
- **Remote/branch:** `origin` → local `main` / upstream tracking `origin/main`.
- **Strategy:** `git pull --ff-only` only (no merge strategy, no rebase).
- **Dirty tree:** If uncommitted changes exist, **abort** pull, list dirty paths, mark session **blocked** — do not stash/autostash unless a later user decision says so.
- **Agent success required:** Dual preflight (remote reachability + agent git/GCM). On Windows, prefer Git for Windows absolute `git.exe` when PATH `git` is MSYS without helper. User-terminal-only success does **not** count.
- **Fail-closed on pull failure:** Document error; session `blocked` with `blocker_type` (`agent_environment` vs `user_credentials` as appropriate); no force-push, no hard reset, no `--no-verify`, no git config changes. Still run self-improver.
- **Mutation class:** `docs_only` for corpus — no catalogue moves/renames/deletes. Git fetch/ff update of this repo is in scope.
- **Windows commit hygiene N/A** for this cycle (no commit required); if any session text files are written, follow repo BOM-safe habits where applicable.

## Context pointers

- Session root: `sessions/2026.09.09-1332/`
- Prompt artifacts: `sessions/2026.09.09-1332/01-prompt-betterment/` (`notes.md`, this file)
- Prior publish session: `sessions/2026.09.09-1246/` (commit `f5012d6` pushed to `origin/main` — re-verify live state)
- Program: `program/ROADMAP.md`, `program/CHARTER.md` (pull is user-named git-ops cycle; not a move-batch row)
- Workflow: `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/agents/orchestrator.md`
- Publish pack (related, not this cycle): `.cursor/skills/full-agent-workflow/references/publish-cycle.md`

## Acceptance criteria

- [ ] `git rev-parse --show-toplevel` equals `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` before any pull; no sibling `C:\Project` trees touched.
- [ ] Preflight: `git status` / short branch tracking; if working tree dirty → abort, document paths, status `blocked` (do not pull).
- [ ] If clean: agent runs `git pull --ff-only` against `origin` for `main`/`origin/main` tracking and it **succeeds** in agent Shell (or already up-to-date with exit 0 / equivalent verified sync).
- [ ] On non-ff divergence, auth failure, or other pull error: fail-closed — no merge fallback, no rebase, no force/hard reset; session `blocked` + `blocker_type`; self-improver still runs.
- [ ] Post-attempt verification recorded: `git status -sb`, ahead/behind vs `origin/main`, and HEAD SHA (before/after when a ff occurred).
- [ ] Full session artifacts written under `sessions/2026.09.09-1332/` documenting the pull outcome (research/plan/implementation/audit/self-improvement as FAW requires).
- [ ] Taxonomy final sign-off and must-preserve draft review **not** attempted and **not** used as blockers for this pull.

## Out of scope

- Taxonomy **final** ratification (remains **proposed-ratified — ready for user sign-off**)
- Must-preserve list lock (remains **draft — not auto-locked / for user review**)
- Corpus FS moves, renames, deletes
- `git push`, new commits for publish, force-push, amend of pushed commits
- Pulling other remotes/branches; merge or rebase pull strategies
- Autostash / agent conflict resolution
- Sibling repositories under `C:\Project`
- Changing git config

## Good vs bad outcomes

- **Good:** Clean tree; agent ff-only pull succeeds (or already synced); logs show org-root-only ops and SHAs; session completes or correctly blocks with evidence.
- **Bad:** Pull in wrong root; silent merge commit; stash without approval; mark complete after agent pull failed because “user can pull”; force/hard reset to “fix” divergence.
