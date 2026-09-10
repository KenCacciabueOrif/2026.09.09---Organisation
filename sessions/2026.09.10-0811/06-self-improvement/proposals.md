# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | Continuity / orchestrator | Soft-deferred “finalize by default” can be misapplied to fail-closed `WorkSpace`-only remaining → force-move, false Complete, or Primary next | Encode **fail-closed / git-strategy nearly-complete**: lock remaining `WorkSpace` only; finalize/move only if hazards cleared **or** dedicated git-strategy plan; never force-move; never Complete / Primary next while it remains; never reopen Medium / archived Multi-experiment peers | `orchestrator.md`, `SKILL.md`, `full-agent-workflow.mdc`, `AGENTS.md` |
| P2 | prompt-betterment | Remaining-subset pack still exemplifies `PWAExemple`+`WorkSpace`; next cycle needs WorkSpace-only pack + agent-owned defaults | Add **Multi-experiment WorkSpace-only** Continuity pack: short Qs; default = research + defer unless cleared/git-strategy opt-in; do not re-propose `PWAExemple` | `prompt-betterment.md`, `handoff-templates.md`, `01-notes.md` |
| P3 | planner | Soft-deferred finalization plans assume movable Soft-deferred maps | Split: movable soft-deferred → finalize map; fail-closed remaining → map empty or git-strategy-only when Continuity clears; ROADMAP stays in progress | `planner.md` |
| P4 | orchestrator / implementer | SESSION Program framing remaining names lag after partial batch (audit Low) | After implementer returns, refresh SESSION lock line to post-move remaining names before audit/close | `orchestrator.md` (light); optional implementer note |
| P5 | implementer | Cycle 7 robocopy vs Cycle 8 clean Move-Item — reinforce preference | One-line: prefer clean `Move-Item`; robocopy only on documented lock recovery (already mostly true) | `implementer.md` (tiny) |
| P6 | backlog | Researcher has no Multi-experiment WorkSpace cue | Optional later: researcher bullet for WorkSpace-only live-check | deferred |

## Online best-practice notes

- **Orchestrator + structured handoffs** — Cursor docs recommend a parent coordinating specialist subagents with structured outputs per handoff (planner → implementer → verifier). Matches FAW; Continuity encoding belongs in agent prompts + handoff templates so the parent does not re-decide scope mid-cycle. https://cursor.com/docs/subagents
- **Focused agents, concise prompts** — Prefer single-responsibility agents and avoid overly long prompts; encode one new Continuity case as a short named bullet rather than rewriting whole files. https://cursor.com/docs/subagents
- **Skills for repeatable workflow** — Keep FAW steps in the skill; agents hold role Continuity. Adopted: update skill bootstrap lock language + agent Continuity packs together. https://cursor.com/docs/skills (via Cursor skills guidance / learncursor)

**Adopted this cycle:** P1–P5 (agent-owned Continuity for WorkSpace-only remaining; SESSION refresh; Move-Item preference). P6 deferred.
