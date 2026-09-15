# Online prompt tips — Cycle 19 (Continuity X / XL git-strategy)

Actionable tips for this goal type: agent workflow briefs that stop at a **plan gate** before irreversible filesystem / git-root moves.

1. **State goal + hard constraint in one breath** — Pair the outcome (“dedicated XL / whole-tree git-strategy for WorkSpace”) with the non-negotiable boundary (“no path mutation until plan gate yes”). Vague “organise WorkSpace” invites silent archive.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

2. **Use an explicit plan-before-build checkpoint** — Continuity X maps to Plan Mode: research → clarifying locks → reviewable plan → human approval → only then build. Treat the plan gate as the product, not a courtesy pause.  
   Source: [Cursor Plan Mode docs](https://cursor.com/docs/agent/plan-mode) · [Agent best practices](https://cursor.com/blog/agent-best-practices)

3. **Name verifiable acceptance criteria** — Prefer checkable AC (“cite hazard artifact”; “WorkSpace remains at root until gate”; “Multi-experiment not Complete”; “NO_AUTO_COMMIT on dirty WT”) over vibes (“do the right git thing”).  
   Source: [Cursor agent best practices](https://cursor.com/blog/agent-best-practices) · [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

4. **Point at durable context files, don’t paste them** — Reference `program/git-strategy-workspace-hazards.md`, ROADMAP row, Cycle 18 Continuity X lock; keep the refined prompt short so it stays authoritative.  
   Source: [Cursor agent best practices (rules / reference files)](https://cursor.com/blog/agent-best-practices)

5. **Template: Goal / Context / Constraints / Done / Out of scope** — Force keep-vs-split fate options and “what execute would mean” into Out of scope until gate; STAGE 1 stops after planner.  
   Source: [Prompt templates for AI coding agents](https://www.learncursor.dev/guides/prompt-templates-for-ai-coding-agents)

6. **Worktree / nested-root moves need repair semantics** — If any future gated map relocates linked worktrees or nested clones, prefer git-aware move/repair over blind `mv`; probe `worktree list` on nested clone paths only. Encode as plan risk language, not this-cycle execute.  
   Source: [git-worktree documentation](https://git-scm.com/docs/git-worktree) · [Worktrees traps guide](https://continuumcode.ai/guides/git-worktrees/)

7. **Be explicit when information is missing** — If research cannot clear whole-tree, say clearance **NO** and propose gated subsets or hold — do not invent silent whole-tree archive to fill the gap.  
   Source: [Prompt engineering best practices for 2026 (Anthropic)](https://claude.com/blog/best-practices-for-prompt-engineering)
