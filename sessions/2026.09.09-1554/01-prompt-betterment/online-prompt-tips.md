# Online prompt tips — Cycle 5 Medium wrappers (remaining)

Actionable practices for clarifying packs and irreversible FS batches. Sources accessed 2026-09-09.

1. **Clarify before mutate** — For multi-path work, research → ask targeted questions → write a reviewable plan → wait for approval before building. Do not treat Continuity / “next cycle” as move approval.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

2. **Ask only what the user alone can decide** — Do not re-ask facts agents can live-check on disk (INDEX vs root). Reserve questions for batch size, risk appetite, and “still OK?” Continuity.  
   Source: [Agent Patterns — Interactive clarification](https://agentpatterns.ai/patterns/agent-design/interactive-clarification-underspecified-tasks/)

3. **Fewer, high-value questions beat a long pack** — On remaining-subset cycles, a short Continuity pack (subset size, defer high-risk, confirm carried locks) outperforms replaying the full first-batch questionnaire.  
   Source: same [Agent Patterns](https://agentpatterns.ai/patterns/agent-design/interactive-clarification-underspecified-tasks/) (targeted > broad)

4. **Match gate strength to reversibility** — Surface assumptions for cheap docs; **block** on high-blast-radius folder moves. A separate plan gate after the map is the right HITL for `fs_mutation`.  
   Source: [Agentic Workflow — plan + human checkpoint](https://aidenapp.org/agentic-workflow); [AI agents — approval gates](https://blog.datavessel.io/ai-agents-busy-work-smb/)

5. **Put checkable acceptance criteria in the prompt** — Must-haves, must-nots, and edge cases (e.g. nested `.git` intact, `.env` opaque, INDEX current-path honesty) so auditor/verification have a stopping condition.  
   Source: [NewPrompt — Make AI follow acceptance criteria](https://newprompt.net/guides/make-ai-follow-acceptance-criteria); [Agentic Workflow — no AC antipattern](https://aidenapp.org/agentic-workflow)

6. **Scope the batch in the refined prompt** — Name remaining candidates, exclude already-moved peers, and state out-of-scope rows so later phases cannot reopen Cycle 4 archives or jump Primary next.  
   Source: [OTF — Cursor agent best practices (plan, scope, verify)](https://otf-kit.dev/blog/cursor-agent-best-practices)

7. **Blocking ask / plan approval when the harness supports it** — Prefer explicit multi-choice + plan approval so “Choose all” on Continuity is not confused with map approval.  
   Source: [Cursor ACP — ask_question / create_plan](https://cursor.com/docs/cli/acp)
