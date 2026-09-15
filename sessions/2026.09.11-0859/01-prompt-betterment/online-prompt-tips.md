# Online prompt tips — Cycle 15 (WorkSpace-only, post–Appendix A)

Actionable prompting practices for this Continuity / strategy-docs cycle (not domain research).

1. **Lead with one clear objective** — State the single outcome first (e.g. “continue WorkSpace hazard strategy docs after Appendix A”), then constraints. Agents over-scope when the goal line is vague.  
   Source: https://prodmoh.com/blog/10-best-practices-for-cursor-users

2. **Use structured sections** — Prefer Goal / Context / Constraints / Acceptance criteria / Out of scope over paragraph briefs so later phases do not invent scope.  
   Source: https://eastondev.com/blog/en/posts/dev/20260129-cursor-prompt-engineering/

3. **Name exact files and “do not touch” paths** — Point at `program/git-strategy-workspace-hazards.md`, prior session `sessions/2026.09.11/`, and forbid archived peers / whole-tree archive as explicit constraints.  
   Source: https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts

4. **Plan before mutating** — For non-trivial or irreversible FS work, require a reviewable plan and a separate human gate; Continuity Choose ≠ execute. Matches STAGE 1 hold for any `fs_mutation`.  
   Source: https://cursor.com/blog/agent-best-practices

5. **Verifiable acceptance criteria** — Encode checks agents can prove (nested count honesty, no Complete while WorkSpace remains, docs_only vs fs_mutation stop rules) instead of “make it better.”  
   Source: https://www.learncursor.dev/guides/prompt-engineering-for-developers

6. **Constraints half of the prompt** — Explicitly state what not to do (no force-move XL WorkSpace, no re-move already-isolated `_backups`/`_quarantine` unless they reappear, no Primary-next jump). Reduces improvisation.  
   Source: https://eastondev.com/blog/en/posts/dev/20260129-cursor-prompt-engineering/

7. **One task / one Continuity path per cycle** — Keep this FAW on WorkSpace-only continue-strategy vs one further scoped map; defer TNA dirty hygiene to a later Continuity unless chosen.  
   Source: https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts
