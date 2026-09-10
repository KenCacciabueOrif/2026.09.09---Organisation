# Online prompt tips — Cycle 10 WorkSpace hazard remediation

Actionable tips from current agent-prompting practice, scoped to clarifying packs + gated remediation briefs (not domain git research).

1. **Ask clarifying questions before research/plan** — Cursor Plan Mode and agent best practices: surface requirements first, then investigate, then produce a reviewable plan. Vague Continuity answers produce coherent-but-wrong remediation maps.  
   Sources: https://cursor.com/docs/agent/plan-mode · https://cursor.com/blog/agent-best-practices

2. **Separate “think” from “do” with an explicit approval gate** — Prefer a reviewable plan (intent + from→to if any) before any corpus mutation; Continuity “yes” must not equal execute.  
   Sources: https://cursor.com/docs/agent/plan-mode · https://www.learncursor.dev/learn/cursor-agents/agent-plan-mode

3. **Specific answers beat two-word nods** — Short yes/Choose is fine when defaults were disclosed; otherwise push for concrete choices (docs-only vs scoped FS map) so research targets the right hazards.  
   Source: https://www.learncursor.dev/learn/cursor-agents/agent-plan-mode

4. **State success criteria and failure handling explicitly** — Testable AC (“hazards classified; INDEX honest; no force-move”) plus fail-closed branches beat “make it safe.”  
   Sources: https://newprompt.net/resources/agent-task-template · https://agentscamp.com/guides/prompting/designing-system-prompts

5. **Pair prohibitions with the allowed path** — e.g. “Do not force-move the whole XL tree; instead classify remotes / isolate named hazards under a plan gate.” Affirmative + out reduces silent wrong action.  
   Source: https://agentscamp.com/guides/prompting/designing-system-prompts

6. **Put out-of-scope and stop conditions in the brief** — Negative constraints (“don’t reopen Medium peers”; “stop if unexpected worktrees”) prevent most cleanup debt.  
   Sources: https://www.reddit.com/r/cursor/comments/1qxkvlb/anyone_else_doing_prompt_engineering_differently/ · https://blckalpaca.at/en/knowledge-base/ai-agents/prompt-engineering-for-agents/system-prompts-design-patterns

7. **Escalate irreversible FS / secret-touching decisions to humans** — Governance pattern: human approval at mutation gates; opaque `.env` / remote rewrite = escalate, don’t invent.  
   Source: https://code.mil/AI4SDLC/plays/ai_sdlc_workflows-play/
