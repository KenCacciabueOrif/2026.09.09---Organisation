# Online prompt tips — Cycle 7 Multi-experiment (first subset)

Actionable prompting practices for scoped FS-mutation batches with a later human plan gate. Captured for this FAW phase (prompt-betterment), not domain research.

1. **Clarify before research, approve before mutation** — Force a short clarifying turn, then a reviewable plan with concrete paths; wait for explicit approval before any move. Matches Cursor’s Plan Mode posture (research → questions → editable plan → build).  
   Source: https://cursor.com/docs/agent/plan-mode · https://cursor.com/blog/agent-best-practices

2. **Name goal + constraints + out of scope in the same brief** — Vague “organise next” invites wrong blast radius; specific “move 1–2 Multi-experiment folders under catalogue layout; do not touch Medium archives / Obsidian” steers later phases.  
   Source: https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts

3. **Put acceptance criteria next to the goal (checkable sentences)** — Must-haves, must-nots, quality bar, and edge cases (e.g. fail-closed on multi-remote / worktrees) so auditor and implementer share one definition of done.  
   Source: https://newprompt.net/guides/make-ai-follow-acceptance-criteria

4. **Keep an explicit “Not Included” boundary** — Spec-driven agents expand when scope is silent; list non-goals (no Medium reopen, no origin rewrite, no secrets read) as hard AC.  
   Source: https://www.augmentcode.com/guides/ai-spec-template

5. **Prefer narrow batches over one mega-prompt** — Multi-agent / multi-step work degrades when one prompt carries all folders and edge cases; scoped first subset (1–2 of four) reduces wrong-feature confidence.  
   Source: https://llmdb.app/blog/orchestrating-multi-agent-workflows-with-langgraph-and-durable-execution-state

6. **Human gate = frozen plan, not Continuity Choose** — Treat plan-gate approval as a separate checkpoint; Continuity / “Choose” locks scope rules only — never skip or imply move permission.  
   Source: https://solana.garden/guides/llm-agent-durable-state-checkpointing-run-persistence-explained/ (human gates / frozen plan hash pattern)

7. **If the build misses, refine the plan and re-run — don’t patch blindly** — For corpus moves, prefer revert + better map over compounding a bad batch.  
   Source: https://cursor.com/blog/agent-best-practices · https://www.learncursor.dev/learn/cursor-agents/agent-plan-mode
