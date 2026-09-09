# Handoff templates

Orchestrator fills placeholders then launches the named subagent via Task.

## prompt-betterment

```
Session phase dir: <abs>/01-prompt-betterment/
Raw user goal:
<paste>

Write online-prompt-tips.md, ask clarifying questions (or use answers below), then refined-prompt.md and notes.md.
Prior answers (if any):
<paste or none>
```

## researcher

```
Session phase dir: <abs>/02-research/
Read refined prompt: <abs>/01-prompt-betterment/refined-prompt.md
Produce codebase-findings.md, online-findings.md, research-brief.md.
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
Push goals: dual preflight step; ready_to_implement no only when agent cannot push / credentials unverified — not merely missing gh when GCM verified.
```

## implementer

```
Session phase dir: <abs>/04-implementation/
Execute plan at: <abs>/03-plan/plan.md
Respect acceptance criteria in refined-prompt.md.
Write log.md and changes.md. Do not expand scope.
Push goals: prefer GfW absolute git on Windows HTTPS; blocker_type agent_environment vs user_credentials; no secret logging.
```

## auditor

```
Session phase dir: <abs>/05-audit/
Verify against refined-prompt.md, plan.md, and 04-implementation artifacts.
Write report.md. Return verdict, rework_needed, and rework_owner (implementer | user | …).
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
```
