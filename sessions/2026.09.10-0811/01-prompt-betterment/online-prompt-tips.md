# Online prompt tips — Cycle 8 Multi-experiment (remaining subset)

Actionable prompting practices for a **partial-row** FS-mutation cycle (remaining names only) with Continuity carry + a separate human plan gate. Captured for prompt-betterment, not domain research.

1. **Clarify scope, then plan, then approve before mutation** — Short clarifying turn → reviewable plan with concrete from→to paths → explicit approval before any move. Continuity / “Choose” is not move permission.  
   Source: https://cursor.com/docs/agent/plan-mode · https://cursor.com/blog/agent-best-practices

2. **Four-block brief: Goal · Constraints · Acceptance · Out of scope** — One goal sentence; touch/no-touch names; checkable done; hard non-goals (no Medium reopen, no origin rewrite). Prevents the model from filling gaps with wrong blast radius.  
   Source: https://aitoolsguidebook.com/en/articles/coding-prompt-structure/

3. **Name invariants and untouchable paths** — Explicit “do not re-propose already-moved peers / do not reopen Early-Medium archives as sources” reduces scope creep on multi-cycle programs.  
   Source: https://understandingdata.com/posts/prompt-contracts-specification-before-code/

4. **Acceptance criteria must be checkable** — Prefer countable path presence, INDEX honesty, fail-closed deferrals with logged reason — not vague “organise remaining.”  
   Source: https://understandingdata.com/posts/prompt-contracts-specification-before-code/ · https://cursor.com/blog/agent-best-practices

5. **Constraints and guardrails beat overloaded context** — Carry Continuity locks in the refined prompt; don’t re-paste full prior-cycle chat. Prioritize remaining names + fail-closed rules.  
   Source: https://business.adobe.com/blog/prompting-ai-agents

6. **Durable session state over chat memory** — Lock answers and Continuity in `notes.md` / `refined-prompt.md` so later phases resume from files, not history.  
   Source: https://github.com/agentpatternscatalog/patterns/blob/main/patterns/durable-workflow-snapshot.md

7. **If the batch misses, refine the plan and re-run — don’t patch blindly** — For corpus moves, prefer revert + better map over compounding a bad batch.  
   Source: https://cursor.com/blog/agent-best-practices
