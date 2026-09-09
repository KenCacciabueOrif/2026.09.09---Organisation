# Improvement proposals

Session: `sessions/2026.09.09-1009/06-self-improvement/`

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | Orchestrator continuity | Next FAW may not inherit locked ROADMAP row + pending sign-offs | When choosing next ROADMAP row, document row id + pending user gates in SESSION + prompt-betterment handoff; one session per cycle | `.cursor/agents/orchestrator.md`, `handoff-templates.md`, `sessions/_templates/SESSION.md` |
| P2 | Prompt-betterment | User “Choose” left ambiguous for later agents | Rule: **Choose → agent decides, locks in notes.md, never leave “Choose” for researcher/planner** | `.cursor/agents/prompt-betterment.md`, `sessions/_templates/01-notes.md` |
| P3 | Status vocabulary | Proposed-ratified / draft must-preserve can be overclaimed | Encode: **proposed-ratified ≠ final user sign-off**; **draft must-preserve ≠ auto-locked**; AC must say “ready for sign-off / for user review” | `.cursor/agents/prompt-betterment.md`, `planner.md`, `auditor.md` |
| P4 | Early/simple next cycle | First move batch could skip pending taxonomy/must-preserve gates | Planner/auditor: for `fs_mutation` Early/simple (or first move), fail-closed unless session notes taxonomy signed off **or** explicit user waiver; must-preserve reviewed **or** waiver | `.cursor/agents/planner.md`, `auditor.md`, `SKILL.md` |
| P5 | Skill / rules / AGENTS | Continuity + Choose + draft language not in always-apply law | Short bullets: ROADMAP row lock; Choose→decide; proposed-ratified/draft | `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/rules/full-agent-workflow.mdc`, `AGENTS.md` |
| P6 | Plan template | `mutation_class` easy to omit | Add Mutation class section to `03-plan.md` template | `sessions/_templates/03-plan.md` |
| P7 | Handoffs | Self-improver / phase handoffs miss Cycle 1 focus cues | Add Choose/proposed-ratified/must-preserve/ROADMAP-next cues to handoffs | `handoff-templates.md` |
| P8 | Hygiene | Unrelated WT dirt confuses auditors | Optional tip only — defer | (none now) |
| P9 | Tooling | Auto ROADMAP→prompt skill | Higher scope — keep deferred from Cycle 0 P9 | (none now) |

## Online best-practice notes

Adopted / reinforced this cycle:

- **Focused subagents + concise prompts** — tighten cue bullets rather than long essays; keep one responsibility per agent. Source: [Cursor subagents docs](https://cursor.com/docs/subagents.md).
- **Rules = always-on law; Skills = on-demand workflow** — put Choose / proposed-ratified / ROADMAP continuity in both rule (short) and skill (procedural). Source: [Cursor agent best practices](https://cursor.com/blog/agent-best-practices).
- **Skills for repeatable process, subagents for isolated phases** — keep FAW phase agents; do not invent a trivial “Choose resolver” subagent. Source: [Bloss0m skills/subagents/commands/hooks](https://www.bloss0m.com/en/blog/29-agent-era-skills-subagents-commands-hooks/).

Not adopted now: parallel worktree multi-agent for inventory (premature); dedicated `program-cycle` slash skill (P9 deferred).
