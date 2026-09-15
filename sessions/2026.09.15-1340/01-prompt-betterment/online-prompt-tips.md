# Online prompt tips — Cycle 22 (workstream Choose + concrete advance)

Actionable prompting practices for multi-workstream FAW briefs (clarify → research proposes → plan gate → verify). Sources checked 2026-09-15.

1. **Clarify, then plan, then build** — For complex or multi-option work, ask focused clarifying questions first; produce a reviewable plan with paths and checks; wait for approval before irreversible steps.  
   Source: [Cursor Plan Mode](https://cursor.com/docs/agent/plan-mode); [Introducing Plan Mode](https://cursor.com/blog/plan-mode)

2. **Goal + constraints + testable done** — Name the outcome, what must not change, and pass/fail checks (commands, smoke tests, evidence). Vague wishes produce vague work.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts); [Make AI Follow Acceptance Criteria](https://newprompt.net/guides/make-ai-follow-acceptance-criteria)

3. **State non-goals / out of scope** — Explicitly list related work this cycle must not do (archived peers, whole-tree archive, empty re-attest) so later phases do not wander.  
   Source: [Prompt Design — state non-goals](https://llmbestpractices.com/prompt-engineering/prompt-design); [AI Agent Prompt Design Guide](https://promptly.cloud/ai-agent-prompt-design-guide)

4. **Acceptance criteria as inspectable finish lines** — Must-haves, must-nots, evidence, and blocked-state behavior; distinguish “proposed at plan gate” from “executed after approval.”  
   Source: [AI Agent Acceptance Criteria](https://fondsites.com/ai-agents/guidebooks/agent-acceptance-criteria/); NewPrompt AC guide above

5. **One primary task; escalate when stuck** — Keep the cycle to one concrete advance; define escalation / stop rules when research would only repeat prior findings (anti-loop).  
   Source: [System Prompts — escalation & stop](https://llmbestpractices.com/ai-agents/system-prompts); Cursor Plan Mode “start over from the plan”

6. **Point at durable artifacts, not megaprompts** — Reference ROADMAP, prior SESSION, refinement plan, and `program/git-strategy-*.md` instead of pasting long history.  
   Source: [Cursor agent best practices](https://otf-kit.dev/blog/cursor-agent-best-practices); Learn Cursor good prompts

7. **Continuity choose ≠ execute** — Pack answers lock *intent*; plan gate (and #4 nest approval) still required before corpus FS / nest extract. Prefer reversible defaults when user says Choose.  
   Source: Local FAW law; Cursor Plan Mode approval step
