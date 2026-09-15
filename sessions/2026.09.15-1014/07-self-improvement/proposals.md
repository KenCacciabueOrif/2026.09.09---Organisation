# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | Orchestrator / skill / rules | Continuity X law stops at “next FAW = XL strategy”; dedicated X cycle hybrid **D/M/D+M** + STAGE 1 hold → STAGE 2 same session under-specified | Encode Continuity X dedicated-cycle: plan gate **D** / **M** / **D+M** / hold; STAGE 1 stop; STAGE 2 resume same folder; **D+M** = docs first then `path_batch` | `orchestrator.md`, `SKILL.md`, `full-agent-workflow.mdc`, `AGENTS.md` |
| P2 | Planner / prompt-betterment | Hybrid mutation class and OS-IA-first subset not named as Continuity X defaults | Continuity X plans: extend hazard docs + optional held OS-IA map; gate options D/M/D+M; `ready_to_implement: no` until gate; clearance criteria; **OS-IA alone ≠ Complete** | `planner.md`, `prompt-betterment.md`, handoff-templates |
| P3 | Implementer / researcher / auditor | Post–OS-IA honesty / Next FAW lock easy to miss after a “successful” archive | Docs-first then path_batch; live dirty recount; never Complete/Primary next; Next FAW = **WorkSpace only (TNA)** + continue Continuity X clearance / keep-at-root | `implementer.md`, `researcher.md`, `auditor.md` |
| P4 | Session template | Mutation class / Next FAW hint examples omit hybrid D+M and post–OS-IA TNA | Add hybrid **D+M** + STAGE fields; Next FAW example WorkSpace TNA + Continuity X clearance | `sessions/_templates/SESSION.md` |
| P5 | Process | Research dirty count vs pre-move porcelain can drift | Low: prefer implementer live recount (already practiced) — reinforce one line in implementer; no new user chore | `implementer.md` (with P3) |
| P6 | Deferred | SESSION mid-git checklist lag | Keep as Low bookkeeping; no new rule churn this cycle | backlog |

## Prioritized apply now

**P1–P4** (high value, low risk, agent-owned Continuity X law). **P5** folded into implementer. **P6** deferred.

## Online best-practice notes

- **Skills vs rules:** Skills for repeatable workflows; rules for always-on constraints — keep Continuity X procedure in skill/agents, one-line law in alwaysApply rule ([Cursor agent best practices](https://cursor.com/blog/agent-best-practices), [Skills docs](https://cursor.com/docs/skills)).
- **Subagents + handoffs:** Role isolation + structured parent handoffs match FAW phase agents ([Subagents](https://cursor.com/docs/subagents.md); community multi-agent skills pattern [forum](https://forum.cursor.com/t/how-i-set-up-multi-agent-workflows-in-cursor-with-reusable-skills-and-agents/166742)).
- **Adopted here:** Encode Continuity X as skill/agent procedure (not jargon-only rule dump); keep STAGE 1→2 resume in orchestrator skill path so context stays phase-isolated.
