# Refined prompt

## Goal

Make future `/full-agent-workflow` cycles able to run `git push` successfully from the **agent Shell** when the interactive user terminal can already push (credentials present via Git Credential Manager / user environment), without storing secrets in the repo.

Primary approach preference (unless research disproves it): document and enforce correct **Shell invocation / permissions / credential-helper inheritance / non-interactive push preflight and fail-closed blocked handling** in organisation workflow tooling. Treat HTTPS→SSH remote rewrite or requiring `gh` on PATH as **secondary options** only if research shows agent Shell cannot use existing GCM credentials.

## Constraints

- Scope: organisation repo tooling only — `.cursor/agents/`, `.cursor/skills/full-agent-workflow/`, `.cursor/rules/`, `sessions/_templates/`, `AGENTS.md`, and related handoff/session docs. No new product apps unless a tiny helper script is clearly justified.
- **Do not** commit, log, or template secrets, PATs, tokens, or credential files.
- Do not force-push; do not change git user config globally as a “fix” unless research proves a minimal, documented, user-owned setup step is required (prefer documenting user remediation over silent global config mutation by agents).
- Preserve existing honesty rules: failed push auth → session `blocked`, never `complete`; still run `self-improver`.
- Windows + PowerShell is the observed environment; solutions must be workable there (and ideally portable notes for other OS).
- Prefer small, reviewable diffs to agents/skills/rules/templates over large rewrites.

## Context pointers (known)

- Prior session: `sessions/2026.09.09-0831/` — implementer commit `9708f2e`; agent push failed with:
  - `fatal: could not read Username for 'https://github.com': terminal prompts disabled`
  - `gh` missing in agent environment
- User Cursor/PowerShell terminal: `git push origin main` succeeded (`9e00fd9..9708f2e main -> main`) **without** re-authentication.
- Inference: credentials exist for interactive user shell / GCM; agent Shell path did not obtain them.
- Existing push/auth workflow surface (update as needed):
  - `.cursor/agents/implementer.md` (status honesty / `blocker_type: user_credentials`)
  - `.cursor/agents/orchestrator.md` (blocked on auth)
  - `.cursor/agents/planner.md` / `researcher.md` (push preflight)
  - `.cursor/agents/auditor.md` (`rework_owner: user`)
  - `.cursor/skills/full-agent-workflow/SKILL.md`
  - `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
  - `.cursor/rules/full-agent-workflow.mdc`
  - `AGENTS.md`

## Acceptance criteria / verification

- [ ] Researcher documents **why** agent Shell push failed while user terminal succeeded (env, permissions, credential helper, PATH/`gh`, HTTPS vs SSH), with evidence commands.
- [ ] Plan + implementation update workflow docs so publish steps include a **non-interactive push path** that can use existing machine credentials when available (or an explicit, secret-free fallback path chosen by research).
- [ ] Implementer/orchestrator/planner/researcher guidance includes **early preflight** for push goals and **fail-closed** `blocked` + user remediation when push cannot proceed non-interactively.
- [ ] No secrets added to the repository or session logs.
- [ ] Auditor can verify by checklist: docs/rules/agents mention the durable fix; optional smoke: agent-invoked `git push` (or dry preflight that proves credential helper works) succeeds or correctly blocks with remediation — not a false `complete`.
- [ ] Self-improver still runs at cycle end.

## Out of scope

- Inventing unrelated product features or apps.
- Storing GitHub PATs/tokens in the repo or committing credential stores.
- Requiring interactive TTY login prompts inside agent Shell as the primary design.
- Rewriting remotes to SSH **by default** without research justification.
- Marking prior `2026.09.09-0831` session retroactively “complete” without a durable workflow change.
- Cloud Agent / separate VM auth setups beyond a short note if local agent Shell is the actual failure mode.

## Suggested research questions (for researcher, not blockers for this prompt)

1. Does Cursor agent Shell sandbox or strip GCM / `credential.helper` / askpass env on Windows?
2. Which Shell permission / “all” / network flags (if any) allow credential helper access without embedding secrets?
3. Is installing/`gh auth git-credential` or SSH a more reliable durable path on this machine?
4. What minimal preflight (`git ls-remote`, `git credential fill`, `gh auth status`) should the workflow mandate before commit+push?
