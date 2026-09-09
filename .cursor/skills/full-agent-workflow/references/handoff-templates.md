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
If user answers "Choose" / "Choose all" → you decide, lock in notes.md Answers (+ one-line ask summary per Q), encode in AC — do not leave Choose for later phases.
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
```

## planner

```
Session phase dir: <abs>/03-plan/
Read:
- <abs>/01-prompt-betterment/refined-prompt.md
- <abs>/02-research/research-brief.md
Write plan.md. Set ready_to_implement.
Set mutation class docs_only|fs_mutation. docs_only = zero corpus moves; **includes** org-repo scaffolding creates (folders/READMEs) — not an automatic plan gate. fs_mutation = corpus/catalogue path batches: user approval gate + git-root atomicity + opaque secrets/deps + "What the user is approving" (plain language + path map + pros/cons) for orchestrator plan-gate relay.
Proposed-ratified ≠ final; must-preserve draft ≠ locked. First move/Early-simple: fail-closed without taxonomy sign-off/waiver + must-preserve review/waiver + batch approval.
Optional signals ("if available") must not be hard AC checkboxes.
Push goals: dual preflight step; ready_to_implement no only when agent cannot push / credentials unverified — not merely missing gh when GCM verified.
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
Push goals: prefer GfW absolute git on Windows HTTPS; blocker_type agent_environment vs user_credentials; no secret logging.
```

## auditor

```
Session phase dir: <abs>/05-audit/
Verify against refined-prompt.md, plan.md, and 04-implementation artifacts.
Write report.md. Return verdict, rework_needed, and rework_owner (implementer | user | …).
docs_only: verify zero corpus FS mutation + attestation; proposed-ratified wording; must-preserve draft label.
fs_mutation: verify user approval, batch bounds, git atomicity, no secret quotes; first-move gates (sign-off/waiver); reverse-move notes present when moves succeeded.
Push goals: Option A docs + optional GfW smoke; true credential gaps → rework_owner: user; wrong-git/sandbox may be agent_environment (user settings, not re-login alone). Fail if session marked complete with unmet push criterion.
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
Focus when relevant: proposed-ratified vs final; draft must-preserve; ROADMAP continuity; Choose→decide (incl. Choose-all); ad-hoc org-repo scaffolding vs corpus fs_mutation (docs_only clarity); informed-consent asks (explanation + pros/cons) if user jargon friction appeared.
```
