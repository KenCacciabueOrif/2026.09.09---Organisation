# Plan

## Goal

Encode **Option A** into organisation workflow tooling so future `/full-agent-workflow` cycles can `git push` from **agent Shell** when the machine already has GitHub HTTPS credentials via **Git Credential Manager (GCM)** — without storing secrets. Root cause of session `2026.09.09-0831` failure: agent default `git` is **MSYS** (`C:\msys64\usr\bin\git.exe`) with **no** `credential.helper`, so non-TTY push fails with `terminal prompts disabled`; **Git for Windows** (`…\Programs\Git\cmd\git.exe`) with `credential.helper manager` already succeeds in agent Shell (`credential fill` + `push --dry-run`). Update agents, skill, handoffs, rules, templates, and `AGENTS.md` for dual preflight (user can push ≠ agent can push), prefer GfW absolute path when PATH git is MSYS, fail-closed with `blocker_type` **`agent_environment`** vs **`user_credentials`**, and never treat missing `gh` alone as missing credentials when GCM works.

## Acceptance criteria

- [ ] Researcher/planner/implementer docs require **dual preflight** for push goals: remote scheme + tracking; **agent** git binary / `credential.helper` / GfW preference / non-secret fill or dry-run; optional user-terminal note; `gh` present/absent recorded but **not** sole credential signal.
- [ ] Implementer guidance: on Windows HTTPS, prefer Git for Windows `git.exe` (resolve via `where.exe git` / known GfW path) when default git lacks GCM; invoke that binary for push; do not force `GCM_INTERACTIVE=0` / `GIT_TERMINAL_PROMPT=0` on the GCM probe first (those flags OK for MSYS fail-fast only).
- [ ] Fail-closed: failed agent push/preflight → session `blocked` (never `complete`); `blocker_type` distinguishes **`agent_environment`** (wrong git on PATH, sandbox/Legacy Terminal) vs **`user_credentials`** (no store / need login / SSH setup); orchestrator does not relaunch implementer until remediation; **self-improver still runs**.
- [ ] Orchestrator, auditor, skill, rules, handoff templates, `AGENTS.md`, and `sessions/_templates/` aligned with the above; auditor checklist covers durable fix + optional smoke.
- [ ] No secrets, PATs, tokens, credential fill password lines, or full env dumps in repo or session logs (`GITHUB_TOKEN` existence may be noted boolean-only).
- [ ] No machine-wide PATH rewrite required; docs allow resolving/using GfW absolute path.
- [ ] SSH remote rewrite and `gh auth git-credential` documented only as **fallbacks** if Option A preflight fails after PATH/git fix.
- [ ] Optional smoke (implementer or auditor): agent Shell invokes **GfW** `git push --dry-run` (or `credential fill` without logging secrets) → success; document that default MSYS path remains unsafe for HTTPS push.
- [ ] Diffs stay small and reviewable (docs/templates only; optional tiny secret-free helper only if clearly useful).

## Steps

1. **Auth/preflight (this cycle — docs publish optional)** — Confirm research still holds before any commit/push of tooling changes: `git remote -v` (HTTPS); `(Get-Command git).Source` vs `where.exe git`; prefer GfW for any push/smoke; do **not** treat missing `gh` as blocker. Research already verified GfW fill + dry-run in agent Shell → **no user credential blocker**. If a later step must `git push` the doc commit, use GfW absolute path only; on failure classify `agent_environment` vs `user_credentials` and stop fail-closed. — verify: research-brief push table + optional re-run of GfW dry-run (exit 0, no secret output in logs).

2. **Implementer agent** — `.cursor/agents/implementer.md` — Expand status honesty / push section:
   - Prefer GfW over MSYS for HTTPS push on Windows; how to resolve binary.
   - Preflight before commit+push; never dump env / credential passwords.
   - Missing `gh` ≠ missing credentials if GCM fill/dry-run succeeds.
   - Extend `blocker_type` enum: `none | user_credentials | agent_environment | plan_gap | other` with short definitions and remediation examples (PATH/git vs re-login; Cursor Run Modes / Legacy Terminal note with links from online findings).
   - BOM-safe commit guidance unchanged.  
   — verify: file mentions GfW, dual signal, both blocker types; no secret examples with real tokens.

3. **Researcher agent** — `.cursor/agents/researcher.md` — Extend publish/push preflight checklist: `where`/`Get-Command` git; `credential.helper` per binary; GfW preference; “user pushed ≠ agent ready”; `gh` optional evidence; classify environment vs credential blockers; forbid logging fill passwords / full `Env:`. — verify: checklist items present; blockers cannot be “none” when agent git cannot push non-interactively.

4. **Planner agent** — `.cursor/agents/planner.md` — Align push-goal rules with dual preflight and `agent_environment` vs `user_credentials`; `ready_to_implement: no` only when **agent** cannot push and remediation needs the user (or credentials truly unverified)—not merely because `gh` is absent when GCM verified. — verify: wording matches researcher/implementer.

5. **Orchestrator agent** — `.cursor/agents/orchestrator.md` — On auth/push failure: `blocked` + remediation by blocker type; do not relaunch implementer until remediated; still run self-improver; do not treat missing `gh` alone as user_credentials when notes say GCM/PATH. — verify: both blocker types + honesty preserved.

6. **Auditor agent** — `.cursor/agents/auditor.md` — Checklist: docs encode Option A; optional GfW smoke; `rework_owner: user` for true credential gaps; allow classifying wrong-git/sandbox as environment (may still be user-settings remediation without “re-login”); fail if session marked complete with unmet push criterion. — verify: checklist bullets exist.

7. **Skill + handoffs** — `.cursor/skills/full-agent-workflow/SKILL.md` and `references/handoff-templates.md` — Critical auth path: dual preflight fields in researcher handoff; orchestrator routing for `agent_environment` vs `user_credentials`; Windows GfW note; secret-logging ban. — verify: templates list agent-vs-user push fields; skill Critical section updated.

8. **Rules + AGENTS** — `.cursor/rules/full-agent-workflow.mdc` and `AGENTS.md` — Short durable rules: early agent push preflight; prefer GfW on Windows when PATH git lacks helper; fail-closed; no false complete; self-improver mandatory. — verify: both files mention agent Shell git/GCM or equivalent; keep concise.

9. **Session templates** — `sessions/_templates/02-research-brief.md`, `sessions/_templates/03-plan.md` (and auditor template only if one exists with auth placeholders) — Flesh dual preflight placeholders (remote, agent git path, helper, GCM evidence boolean, gh present?, user-terminal note, blocker_type). — verify: new session copies would force the fields.

10. **Optional helper (only if clearly useful)** — Prefer **docs-only** resolution steps. If implementer judges a tiny helper helps (e.g. `scripts/resolve-git-for-push.ps1` or a short note under skill `references/`), it must: print recommended `git.exe` path / helper status; exit non-zero if only MSYS-without-helper; **never** print credentials or tokens; **not** rewrite machine PATH. Skip if docs alone are enough. — verify: no secrets; not required for AC if docs complete.

11. **Fallbacks (docs only, secondary)** — In implementer and/or skill: short note — if GfW+GCM still fails after PATH fix: (B) install `gh` + `gh auth login` / `credential.helper '!gh auth git-credential'`; (C) SSH remote + key agent; Cursor Settings: less sandbox / Legacy Terminal / approve elevated run ([Run Modes](https://cursor.com/docs/agent/security/run-modes)). Do **not** rewrite `origin` to SSH by default. — verify: labeled fallback, not primary path.

12. **Verification + session log** — Implementer writes `sessions/2026.09.09-0850/04-implementation/` changes + log; run optional GfW dry-run smoke; grep-diff for accidental secrets; do **not** commit unless user/orchestrator requests; if push of this cycle’s commit is requested, use GfW only. — verify: acceptance checklist greppable in updated files; smoke pass or explicit block with correct `blocker_type`.

## Non-goals

- Storing PATs/tokens/credential files in the repo or session logs.
- Machine-wide PATH mutation as the required fix.
- Default HTTPS→SSH remote rewrite.
- Requiring `gh` on PATH as the primary design.
- Interactive TTY login inside agent Shell as the primary path.
- Cloud Agent / separate VM auth beyond a one-line out-of-scope note.
- Retroactively marking session `2026.09.09-0831` complete.
- Application/product code unrelated to workflow tooling.
- Silent global `git config` mutation by agents (document user-owned setup only).

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| False `user_credentials` when GCM works | Mandate `agent_environment` when wrong git/helper/sandbox; never “missing gh” alone |
| Secret leakage (`GITHUB_TOKEN`, fill passwords) | Explicit bans in agents/skill; log success/fail + key names only |
| Over-aggressive `GIT_TERMINAL_PROMPT=0` / `GCM_INTERACTIVE=0` | Use for MSYS fail-fast only; GCM probe allows store read |
| Sandbox blocks Credential Manager later | Fallback note: Legacy Terminal / Run Modes / elevated approval |
| Helper script scope creep | Optional; secret-free; skip if docs suffice |
| Doc drift across many files | Single Option A story; small parallel edits; auditor checklist |
| Rollback | Revert the tooling commit(s); prior honesty rules remain better than nothing |

## Ready to implement

**yes**

Research verified agent can push non-interactively via Git for Windows + GCM. Remaining work is encoding Option A in docs/templates (process blocker only). No user authentication blocking question.

## Blocking questions

none

## Diagram

See `plan-mermaid.md` (dual preflight + blocker classification).
