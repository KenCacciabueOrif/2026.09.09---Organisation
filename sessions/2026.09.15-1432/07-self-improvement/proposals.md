# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | rules / AGENTS / skill | #4 law is binary DRAFT vs approved; Cycle 23 needed **approved-for-named-map ≠ nest-execute** | Encode three #4 states: DRAFT written → approved-for-named-map → nest-execute | `AGENTS.md`, `.cursor/rules/full-agent-workflow.mdc`, `SKILL.md`, `handoff-templates.md` |
| P2 | planner / orchestrator / PB | Plan gate A+E “not chosen” can be misread as declined | Encode **A+E reserved** (user-held later execute) ≠ declined; A = docs flip only | `.cursor/agents/planner.md`, `orchestrator.md`, `prompt-betterment.md` |
| P3 | planner / implementer | Same-cycle A+E under dirty TNA + large absolute-path consumer surface is high risk | Default prefer **A** then dedicated execute gate when dirty TNA consumer surface is large | `planner.md`, `implementer.md`, `auditor.md` |
| P4 | Next FAW / rotation | Post–#4 map approval, Next FAW must stay WorkSpace Continuity X; hermes execute is the natural candidate | Lock hint: WorkSpace only + Continuity X; candidate = dedicated hermes A+E/execute (user-reviewed) **or** other justified advance; never dashboard; never Complete while WorkSpace remains | agents + templates `SESSION.md` |
| P5 | templates | SESSION Clearance #4 status enum lacks approved-for-named-map | Extend status enum + plan-template A/A+E note | `sessions/_templates/SESSION.md`, `03-plan.md` |
| P6 | auditor | Checklist still greps binary “approved” | Accept approved-for-named-map; require nest-execute evidence only when A+E/path_batch claimed | `auditor.md` |

## Online best-practice notes

- **Rules vs skills vs subagents:** Keep always-on constraints in rules/`AGENTS.md`; put procedural workflows in skills; use subagents for isolated specialist phases — matches FAW orchestrator→specialists. https://cursor.com/docs/subagents.md · https://cursor.com/blog/agent-best-practices
- **Progressive disclosure / concise skills:** Prefer short skill bodies + references over megaprompts; encode Cycle 23 distinctions as compact law phrases, not new essays. https://cursor.com/docs/skills · https://singhajit.com/how-to-create-and-use-skills-in-cursor/
- **Adopted here:** Tighten always-on #4 / A vs A+E vocabulary in rules + agent prompts (P1–P4); keep SESSION/plan templates as lightweight enums (P5) — no new skill file.
