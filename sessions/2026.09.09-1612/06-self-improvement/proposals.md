# Improvement proposals — session `2026.09.09-1612`

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | orchestrator handoffs | Next “next cycle” could reopen Medium or miss Primary next | After Medium **Complete**, lock **Primary next → Multi-experiment** (`PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace`); never re-move Medium archive/paused | `.cursor/agents/orchestrator.md`, `SKILL.md`, `handoff-templates.md` |
| P2 | phase agent prompts (PB) | Multi-experiment has no first-batch Continuity pack | Short pack: small first subset (default 1–2); multi nested-git caution (atomic each root; fail-closed worktrees/multi-remote); carry Medium layout/git/env/taxonomy Continuity; SSH path-only | `.cursor/agents/prompt-betterment.md`, `sessions/_templates/01-notes.md` |
| P3 | planner | First Multi-experiment plan might map all four or invent git-strategy | Prefer scoped first-subset map; each nested `.git` atomic; SSH/HTTPS remotes path-only (no rewrite); ROADMAP partial progress until last names; no Medium re-moves | `.cursor/agents/planner.md` |
| P4 | orchestrator UX | “sey”→yes was undocumented | Optional **plan-gate typo tolerance**: clear near-miss affirmative (1-char typo of yes/ok/oui) may count as approval **only** when intent is unambiguous and the move map was just presented; still record the raw reply in SESSION | `.cursor/agents/orchestrator.md` |
| P5 | Continuity / rules | SSH path-only buried in soft-deferred Medium pack | Thin **SSH-origin path-only Continuity**: move intact; never rewrite `origin` URL unless user opts into git-strategy | `.cursor/rules/full-agent-workflow.mdc`, `AGENTS.md`, PB/planner bullets |
| P6 | deferred | must-preserve draft still lists pre-move roots for Cycle 6 folders | Optional later hygiene cycle to refresh draft paths — not auto-lock; do not block Multi-experiment | backlog |
| P7 | deferred | Inventory LastWrite short-name lag | Refresh on next catalogue touch; not Cycle 6 AC | backlog |

## Online best-practice notes

- **Focused subagents + concise prompts** — Cursor docs: one responsibility; avoid rambling Continuity dumps; encode new row as a short named pack. Adopted as P1–P3 (Multi-experiment Continuity, not a new agent). — https://cursor.com/docs/subagents
- **Skills for repeatable workflow; progressive disclosure** — Keep SKILL bootstrap thin; push detail to agents/references. Adopted as P1 skill/handoff one-liners. — https://cursor.com/docs/skills
- **Orchestrator pattern + structured handoffs** — Parent coordinates; specialists return structured output. Reinforces P1 handoff cues over rewriting product law mid-cycle. — https://agenticthinking.ai/blog/subagents-fresh-context/

## Apply now vs defer

- **Now:** P1–P5 (Multi-experiment lock + first-batch defaults + plan-gate typo note + SSH Continuity).
- **Defer:** P6–P7.
