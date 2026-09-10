# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | prompt-betterment Continuity | After strategy docs exist, WorkSpace-only pack still defaults to Cycle 9 research+defer; “solve hazards” can re-defer or invent whole-tree | Split **pre-strategy** vs **post–hazard-strategy docs** packs; point at `program/git-strategy-workspace-hazards.md`; default A=continue strategy docs; B=explicit Appendix A execute Continuity (plan gate); never whole-tree; never Complete | `.cursor/agents/prompt-betterment.md` |
| P2 | orchestrator handoff | No post–Cycle-10 lock rule for strategy-docs success | Add **Post–hazard-strategy docs** bullet: keep WorkSpace lock; continue strategy or explicit Appendix A; never Complete/Primary-next; never invent whole-tree | `.cursor/agents/orchestrator.md` |
| P3 | researcher / planner | Research/plan may re-litigate hazards from scratch or default empty defer without durable artifact | Require read of `program/git-strategy-workspace-hazards.md` on WorkSpace-only; recommend continue-strategy or scoped isolation; empty whole-tree map | `researcher.md`, `planner.md` |
| P4 | auditor checklist | WorkSpace checklist only covers Q1=A defer; strategy-docs / Appendix A execute not called out | Extend docs_only WorkSpace checks: durable artifact pointer; never Complete while WorkSpace remains; Appendix execute needs evidence of Continuity + plan gate | `auditor.md` |
| P5 | skill / rules / AGENTS / handoffs | Law still says post–docs_only → repeated research+defer only | Add post–strategy Continuity clause + durable-artifact pointer (concise) | `SKILL.md`, `full-agent-workflow.mdc`, `AGENTS.md`, `handoff-templates.md` |
| P6 | implementer | Silent risk of treating strategy docs as authorize FS | One-liner: Appendix A only when Continuity + gated `fs_mutation` plan; never whole-tree from strategy alone | `implementer.md` |
| P7 | templates | SESSION Program framing omits strategy-artifact pointer | Optional bullet for WorkSpace durable artifact path | `sessions/_templates/SESSION.md` |
| P8 | inventory MB (product) | Size column vs Notes band | Defer to optional later docs cycle — not FAW law | (product) |

## Online best-practice notes

- **Focused subagents + clear Continuity in skills** — Cursor docs: specialize agents; put repeatable workflow in Skills; keep Rules lean. Adopted: encode post–strategy Continuity in skill/agents rather than relying on chat memory. https://cursor.com/docs/subagents.md
- **Skills as procedural recipes; orchestrator coordinates** — Agent best practices: Rules = static, Skills = dynamic workflows. Adopted: FAW skill step 0 Continuity text updated for WorkSpace post-strategy. https://cursor.com/blog/agent-best-practices
- **One concern per edit; description/triggers matter** — Keep SKILL under bloat; push detail to agent bullets. Adopted: concise Continuity clauses, not a new mega-skill. https://meshlaunch.com/en/blog/2026-cursor-agent-skills-complete-guide.html
