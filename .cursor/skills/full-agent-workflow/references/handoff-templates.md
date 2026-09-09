# Handoff templates

Orchestrator fills placeholders then launches the named subagent via Task.

## prompt-betterment

```
Session phase dir: <abs>/01-prompt-betterment/
Raw user goal:
<paste>
Program context (if any): cycle id, program/ROADMAP.md row locked by orchestrator, prior session, mutation class docs_only|fs_mutation
Pending user gates from prior cycle (if any): taxonomy final sign-off? must-preserve review? batch subset?

Write online-prompt-tips.md, ask clarifying questions (or use answers below), then refined-prompt.md and notes.md.
Clarifying questions MUST include: plain-language explanation of what is asked + what “yes” commits to, and pros/cons (tradeoffs) per option. Do not assume jargon literacy; define gate terms in one sentence if used.
If goal is publish / git add-commit-push: use references/publish-cycle.md question pack; hard AC = this org-repo git root only (never stage sibling C:\\Project trees).
If goal is git pull / sync from origin: use references/pull-cycle.md question pack; hard AC = org-repo root only; FAW default dirty = order-aware allowlisted autonomy + --ff-only (behind+allowlisted → stash→ff→pop / Q3c; else commit-then-pull; abort only for unrelated → blocker_type dirty_working_tree); GfW for status gate, allowlist commit/stash, and pull.
If user answers "Choose" OR leaves pack items unanswered after a partial reply → you decide using disclosed defaults, lock in notes.md Answers (Source Choose / unanswered→default), encode in AC — do not leave blanks for later phases.
Taxonomy/must-preserve language: proposed-ratified — ready for user sign-off; draft — not auto-locked (never claim final without explicit approval).
Prior answers (if any):
<paste or none>
```

## researcher

```
Session phase dir: <abs>/02-research/
Read refined prompt: <abs>/01-prompt-betterment/refined-prompt.md
Produce codebase-findings.md, online-findings.md, research-brief.md.
Corpus/inventory goals: coarse map; flag git roots; do not deep-document node_modules/caches; secrets = path presence only.
Early/simple prep: if next cycle may move, note cheap batch candidates + must-preserve collisions — do not invent final ratification.
If the goal includes git push / remote publish — dual preflight (user can push ≠ agent ready):
- remote scheme + tracking
- agent git path (Get-Command / where); credential.helper per binary; prefer GfW over MSYS on Windows HTTPS when default lacks GCM
- GCM evidence boolean (fill/dry-run success, no secret output); gh present? (optional, not sole signal)
- optional user-terminal note; blocker_type agent_environment vs user_credentials
Never "blockers: none" when agent cannot push non-interactively. Never log fill passwords or full Env:.
If the goal includes git pull / sync — same dual preflight + GfW for porcelain gate, allowlist commit/stash, and pull; classify allowlist vs unrelated dirty vs auth; record ahead/behind:
- unrelated dirty abort → blocker_type dirty_working_tree (auth may be green)
- allowlisted-only + behind>0 → stash→ff→pop path (not “sync not ready”; flag commit-while-behind risk if plan still commit-first)
- allowlisted-only + not behind → agent may auto-commit then pull
- wrong binary / sandbox → agent_environment; true login fail → user_credentials
Do not claim sync ready when WT has unrelated dirty under abort policy.
```

## planner

```
Session phase dir: <abs>/03-plan/
Read:
- <abs>/01-prompt-betterment/refined-prompt.md
- <abs>/02-research/research-brief.md
Write plan.md. Set ready_to_implement.
Set mutation class docs_only|fs_mutation; if fs_mutation: user approval gate + git-root atomicity + opaque secrets/deps + "What the user is approving" (plain language + path map + pros/cons) for orchestrator plan-gate relay.
Proposed-ratified ≠ final; must-preserve draft ≠ locked. First move/Early-simple: fail-closed without taxonomy sign-off/waiver + must-preserve review/waiver + batch approval.
Optional signals ("if available") must not be hard AC checkboxes.
Push goals: dual preflight step; ready_to_implement no only when agent cannot push / credentials unverified — not merely missing gh when GCM verified.
Pull goals: dual preflight + dirty gate; encode order-aware allowlist path (Q3c stash when behind) + unrelated dirty_working_tree abort + expected non-ff fail-closed; ready_to_implement may be yes when fail-closed non-ff or unrelated abort is an allowed implement outcome.
```

## implementer

```
Session phase dir: <abs>/04-implementation/
Execute plan at: <abs>/03-plan/plan.md
Respect acceptance criteria in refined-prompt.md.
User batch approval (fs_mutation only): <approved|pending|n/a — cite SESSION/plan>
Write log.md and changes.md. Do not expand scope.
docs_only → zero-move attestation; fs_mutation → approved batch only; git roots atomic; no secret contents; reverse-move notes for each successful move.
Do not upgrade proposed-ratified/draft labels to "final"/"locked" unless plan AC and session evidence say so.
Push goals: prefer GfW absolute git on Windows HTTPS (not PATH/MSYS alone); confirm rev-parse toplevel = org root before stage; blocker_type agent_environment vs user_credentials; no secret logging.
Pull goals: same GfW for status --porcelain, allowlist commit/stash, and pull; unrelated dirty abort → blocked + dirty_working_tree; behind+allowlisted → stash→ff→pop; not-behind allowlist → auto-commit then --ff-only; non-ff → blocked + other/non_ff (keep WIP/stash); never claim pull success on block; auth/env types unchanged.
```

## auditor

```
Session phase dir: <abs>/05-audit/
Verify against refined-prompt.md, plan.md, and 04-implementation artifacts.
Write report.md. Return verdict, rework_needed, and rework_owner (implementer | user | …).
docs_only: verify zero corpus FS mutation + attestation; proposed-ratified wording; must-preserve draft label.
fs_mutation: verify user approval, batch bounds, git atomicity, no secret quotes; first-move gates (sign-off/waiver); reverse-move notes present when moves succeeded.
Push goals: Option A docs + optional GfW smoke; true credential gaps → rework_owner: user; wrong-git/sandbox may be agent_environment (user settings, not re-login alone). Fail if session marked complete with unmet push criterion.
Pull goals: unrelated dirty-abort or expected non-ff with unmet sync AC → process pass + session blocked (+ rework_owner user for unrelated dirty only) is valid; fail if session marked complete after unmet pull AC. Allowlisted commit then pull attempted = correct. Flag Low if SESSION still in_progress while implementer recommended blocked.
Single-commit publish: expected post-push dirty finalize on session logs only → Low, not rework_needed.
```

## self-improver

```
Session root: <abs>/
Read SESSION.md and all phase artifacts especially 05-audit/report.md.
1) audit-realization.md (good + bad)
2) proposals.md (incl. short online best-practice check)
3) implement safe improvements to .cursor/agents, skill, rules, templates
4) changes-applied.md + backlog.md
This step is mandatory.
Focus when relevant: publish/pull question packs / Q3c behind+allowlisted stash path / allowlisted auto-commit / git-root staging / GfW vs MSYS / dirty_working_tree (unrelated) vs non_ff/other vs agent_environment vs user_credentials / SESSION blocked bookkeeping on implementer return / unanswered→Choose defaults / post-push dirty=Low; proposed-ratified vs final; draft must-preserve; ROADMAP continuity; informed-consent asks if jargon friction appeared.
```
