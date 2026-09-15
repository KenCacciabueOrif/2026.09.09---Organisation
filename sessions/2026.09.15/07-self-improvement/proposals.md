# Improvement proposals — Cycle 18

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | researcher / planner | Post-clear WorkSpace re-probes can fall back to Continuity A `docs_only` theater when there is no material delta | Encode anti-loop: if live re-probe vs hazard strategy has **no material delta** and no new gated step → `concrete_advance_candidate: none` → planner **`escalate_break_loop`** (forbidden Continuity A as cycle outcome) | `.cursor/agents/researcher.md`, `.cursor/agents/planner.md` |
| P2 | planner / orchestrator | Escalate path not a first-class mutation class; Continuity gate options not standardized | Add mutation class **`escalate_break_loop`**: Continuity gate **X / P / N / H** with plain language + pros/cons; Continuity ≠ execute; `ready_to_implement: no` for STAGE 1 | `.cursor/agents/planner.md`, `sessions/_templates/03-plan.md`, `.cursor/agents/orchestrator.md` |
| P3 | orchestrator / skill / rules | Continuity **X** not encoded as next-FAW lock | After gate **X**: next FAW = dedicated **XL / whole-tree git-strategy** Continuity; still **WorkSpace only / not Complete**; **mandatory plan gate** before any path mutation | `.cursor/agents/orchestrator.md`, `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/rules/full-agent-workflow.mdc`, `AGENTS.md` |
| P4 | orchestrator / skill | Unclear close path when `ready_to_implement: no` (escalate / Continuity gate only) | **Skip implementer + mid git**; still run **auditor → self-improver → final closing-pass git** same session after Continuity recorded (or after STAGE 1 stop + user answered gate) | `.cursor/agents/orchestrator.md`, `SKILL.md`, `sessions/_templates/SESSION.md` |
| P5 | orchestrator | Plan Step 3 Continuity recording was ad-hoc | Encode Step 3 as **orchestrator bookkeeping**: update `01-prompt-betterment/notes.md` (or SESSION Continuity), `SESSION.md` Next FAW hint, `program/ROADMAP.md` Next FAW hint — zero corpus FS | `.cursor/agents/orchestrator.md`, handoff-templates |
| P6 | prompt-betterment | WorkSpace-only pack still defaults Continuity A after multi-remote clear / exhausted narrow maps | Add **anti-loop / B→E** pack path: seek new gated advance else escalate; forbid A theater when prior cycles already re-attested with no delta | `.cursor/agents/prompt-betterment.md` |
| P7 | auditor | No checklist for escalate success | Add `escalate_break_loop` AC: mutation class, Continuity X/P/N/H recorded, zero FS, row not Complete, implementer skipped when ready no | `.cursor/agents/auditor.md` |
| P8 | templates | Mutation class enum omits escalate | Extend SESSION + plan templates with `escalate_break_loop` + Continuity gate fields | `sessions/_templates/SESSION.md`, `03-plan.md` |

## Online best-practice notes

- **Skills vs rules split** — Keep always-on Rules thin; put procedural FAW detail in the Skill + agent files so context stays loadable. Adopted: encode escalate law in agents/skill/rules briefly, not a new mega-rule. [Cursor agent best practices](https://cursor.com/blog/agent-best-practices) · [Cursor Skills docs](https://cursor.com/docs/skills)
- **One skill, one job; SKILL.md size** — Prefer concise skill steps + references over ballooning always-apply rules. Adopted: add escalate bullets to existing Multi-cycle / STAGE 1 sections rather than a parallel skill. [MESHLAUNCH 2026 Skills guide](https://meshlaunch.com/en/blog/2026-cursor-agent-skills-complete-guide.html)
- **AGENTS.md + scoped rules** — Portable law in `AGENTS.md`; Cursor-specific always-apply in `.cursor/rules/`. Adopted: mirror escalate Continuity X + skip-implementer close path in both. [AGENTS.md vs rules 2026](https://blog.buildbetter.ai/agents-md-vs-cursorrules-vs-claude-skills-2026-comparison/)

## Apply now vs defer

- **Apply now:** P1–P7 (and P8 templates) — low-risk encoding of Cycle 18 success path.
- **Defer:** INDEX What’s-next auto-line for escalate (needs Option H or explicit honesty Continuity); XL Glob cheap-probe preference (nice-to-have).
