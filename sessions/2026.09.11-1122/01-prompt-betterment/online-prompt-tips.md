# Online prompt tips

Actionable practices for this cycle (workflow-definition / multi-phase agent amendment + plan gate).

1. **Name goal + constraint + verify** — State the outcome, what must not change, and how success is checked (files touched, commands, checklist). Vague one-liners yield vague edits.  
   Source: https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts

2. **Treat acceptance criteria as stop conditions** — Prefer checkable bullets (expected artifacts, edge cases, prohibited changes) over subjective “clean/done.” Agents cannot fix what is not specified.  
   Source: https://cursor.com/blog/agent-best-practices

3. **Plan before multi-file edits** — For workflow/order changes that touch skill + agents + rules + templates, research → clarify → plan → human approve → build (matches this cycle’s STAGE 1 → Hermes gate).  
   Source: https://cursor.com/docs/agent/plan-mode

4. **Put “what NOT to do” in Constraints** — Explicit non-goals (no WorkSpace moves, no Complete, no same-run implement) reduce improvisation more than restating the goal.  
   Source: https://eastondev.com/blog/en/posts/dev/20260129-cursor-prompt-engineering/

5. **Use phase-boundary contracts** — For each phase transition, name owned inputs/outputs and evidence required before the next phase (e.g. mid-cycle git vs mandatory final closing pass after self-improver).  
   Source: https://github.com/caioribeiroclw-pixel/pluribus/blob/main/docs/phase-boundary-contracts.md

6. **Keep role I/O contracts deterministic** — Multi-agent delivery works when each agent has a fixed handoff shape and the orchestrator validates artifacts before advancing (git-manager owns close, not auditor).  
   Source: https://github.com/q3ok/coordinated-agent-team

7. **Serialize git ownership** — One owner for stage/commit/push at defined checkpoints; avoid “commit early then leave late artifacts orphaned.” Prefer optional mid-cycle + mandatory final close over single early push only.  
   Source: https://www.augmentcode.com/guides/how-to-run-a-multi-agent-coding-workspace
