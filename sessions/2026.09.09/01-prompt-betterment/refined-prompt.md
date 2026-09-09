# Refined prompt

## Goal

Scaffold a Cursor full-agent workflow for this organisation repo: one orchestrator that only delegates; phase agents for prompt betterment, research, planning, implementation, audit; mandatory self-improver each cycle; all work logged under `sessions/yyyy.mm.dd/`.

## Constraints

- Follow `AGENT-AND-WORKFLOW-BEST-PRACTICES.md` (agents in `.cursor/agents/`, skill, rules, AGENTS.md)
- Orchestrator must not implement user goals
- Self-improvement must document good and bad points, propose, then implement workflow improvements

## Context pointers

- `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`
- Cursor docs: subagents, skills, rules

## Acceptance criteria

- [x] Orchestrator agent definition exists
- [x] Six phase/custom agents exist (prompt-betterment, researcher, planner, implementer, auditor, self-improver)
- [x] Skill `full-agent-workflow` documents the cycle
- [x] Always-apply rule + `AGENTS.md` + README
- [x] Session templates + dated session folder convention
- [x] Self-improver is mandatory in the cycle definition

## Out of scope

- Hooks / grind loops (maturity ladder stage 4 — later)
- Cloud agent deployment config
