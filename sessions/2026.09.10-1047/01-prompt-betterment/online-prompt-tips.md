# Online prompt tips — Cycle 11 (WorkSpace-only / continue strategy)

Actionable prompting practices for this cycle type: multi-phase agent brief, docs-first continuation after a durable strategy artifact, fail-closed irreversible FS gates.

## Tips

1. **Separate clarify → plan → approve → build**  
   For non-trivial work, force clarifying questions and a reviewable plan before side effects. Continuity answers lock *path*, not *execution* of moves.  
   Sources: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices), [Cursor Plan Mode docs](https://cursor.com/docs/agent/plan-mode)

2. **Structure briefs as Goal / Constraints / Context / Acceptance criteria / Out of scope**  
   Explicit “what not to do” stops over-improvisation (e.g. inventing whole-tree archive, jumping Primary next). Binary AC lets auditor verify without chat history.  
   Sources: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts), [Cursor Prompts: Context, Constraints, and Acceptance Criteria](https://eastondev.com/blog/en/posts/dev/20260129-cursor-prompt-engineering/)

3. **Point at durable artifacts by path; don’t paste entire trees**  
   Reference `program/git-strategy-workspace-hazards.md` and prior session paths so later phases re-probe from the strategy document instead of reinventing Cycle 9 defer narrative.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices) (reference files; keep context scoped)

4. **Classify side effects; require human approval for irreversible writes**  
   Treat `docs_only` as reversible; `fs_mutation` (folder moves) as high-impact — Continuity Choose ≠ execute. Fail-closed when approval or policy is missing.  
   Sources: [AI Agent Rollback Plan](https://dev.to/jackm-singularity/ai-agent-rollback-plan-undo-bad-actions-before-users-lose-trust-4927), [LLM Improper Output Handling](https://www.andyagentlab.com/articles/agent-security/llm-improper-output-handling/)

5. **Prefer reversible defaults when the user says “next” without naming execute**  
   Default to continue-strategy / docs refinement over scoped isolation moves; only escalate to Appendix A when Continuity explicitly chooses execute **and** a separate plan gate approves a from→to map.  
   Sources: [Agent state / human checkpoints](https://www.getreadyforagents.com/blog/agent-state-management-recovery-production/), [Cursor Plan Mode — clarify before build](https://www.learncursor.dev/learn/cursor-agents/agent-plan-mode)

6. **One job per cycle in the refined prompt**  
   Lock one ROADMAP remainder (`WorkSpace` only); forbid peer reopen and Complete-while-remaining. Vague “reorganise everything” prompts cause wrong-feature coherence.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts) (one task; scoped context)

7. **Verifiable success signals**  
   AC should name observable artifacts (strategy doc updates, INDEX honesty, zero corpus moves vs gated map) so implementer/auditor share the same done definition.  
   Source: [Cursor — Best practices](https://cursor.com/blog/agent-best-practices) (verifiable goals)
