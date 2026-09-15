# Online prompt tips — Cycle 23

Actionable prompting practices for this FAW cycle (workstream selection + Continuity X / #4 + anti-loop). Sources checked 2026-09-15.

1. **Plan before irreversible work** — For multi-file / multi-path goals, research → clarifying questions → reviewable plan → human approval before build. Matches this cycle’s plan-gate law (Continuity ≠ execute).  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

2. **Put goal + constraints + verification in the prompt** — State desired outcome, hard forbids (here: never re-default dashboard; never whole-tree archive; nest extract only after #4 approved), and checkable acceptance criteria.  
   Source: [Learn Cursor — How to Write Good Prompts](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

3. **Explicit stop / escalate conditions** — Define when the agent must halt and escalate (missing inputs, no material delta vs prior attempt, out of scope) instead of looping. Encode anti-loop as a first-class exit.  
   Source: [NewPrompt — Clear stop conditions](https://newprompt.net/guides/give-an-ai-agent-clear-stop-conditions)

4. **Progress test between attempts** — On attempt ≥2, require a named delta vs the last plan/docs; if the plan is materially the same → `ESCALATE`, not another honesty pass. Direct map to “no empty re-attest” for WorkSpace/#4.  
   Source: [DEV — Stopping conditions that stop multi-agent loops](https://dev.to/dowhatmatters/stopping-conditions-that-actually-stop-multi-agent-loops-bnb)

5. **Bound the loop; do not confuse budgets with authorization** — Step/iteration caps prevent runaway; irreversible FS still needs a separate human gate. Continuity yes ≠ nest move approval.  
   Source: [aiarch.dev — Bounded agentic loop](https://aiarch.dev/patterns/bounded-agentic-loop)

6. **Prompt contract: invariants + out-of-scope** — Name what must not change (taxonomy Continuity, NO_AUTO_COMMIT on dirty TNA, Multi-experiment not Complete while WorkSpace remains) and anti-patterns (dashboard inherit, Appendix A re-do, OS-IA reopen).  
   Source: [Understanding Data — Prompt contracts](https://understandingdata.com/posts/prompt-contracts-specification-before-code/)

7. **Revert + refine plan over corrective thrash** — If implementation or research drifts, refine the plan and retry rather than stacking patches. Prefer escalate over theater when delta is empty.  
   Source: [Cursor Docs — Plan Mode](https://prod.cursor.com/docs/agent/plan-mode)
