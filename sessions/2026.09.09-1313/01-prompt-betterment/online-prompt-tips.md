# Online prompt tips

Actionable practices for scoping a small “create a markdown notes folder” brief so later phases do not invent structure, naming, or git behavior.

1. **State a concrete goal plus hard constraints** — Name the folder path, what may/may not be created (empty dir vs starter files), and what must not change elsewhere. Vague “create a notes area” invites overbuilding.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

2. **Force clarifying questions before any file writes** — Require the agent to resolve naming, location, starter content, and “done” checks first; do not assume defaults for path or README.  
   Source: [Cursor docs — Plan Mode](https://cursor.com/docs/agent/plan-mode)

3. **Write acceptance criteria as checkable facts** — Prefer “folder `Notes/` exists at repo root with a short README explaining how to add `.md` files” over “a place for notes.”  
   Source: [PRD workflow for Cursor agents](https://developertoolkit.ai/en/cursor-ide/quick-start/prd-workflow/)

4. **Declare out of scope explicitly** — List non-goals (no note app, no taxonomy moves, no ROADMAP cycle) so implementers do not expand into organisation-program work.  
   Source: [PRD workflow for Cursor agents](https://developertoolkit.ai/en/cursor-ide/quick-start/prd-workflow/)

5. **If a folder README is wanted, define its contract** — Purpose, how to add notes, what not to put there — keeps the starter file useful without becoming a mini-product.  
   Source: [The Prompt README Pattern](https://prodsens.live/2026.03.08/the-prompt-readme-pattern-make-ai-workflows-maintainable/)

6. **Prefer simple, grep-friendly names** — Lowercase or clear singular/plural folder names and hyphenated note filenames beat ambiguous labels like `Note` vs `Notes` left undecided.  
   Source: [Organize AI prompts on disk](https://mqdir.com/blog/workflows/organize-ai-prompts-on-disk)

7. **Keep the plan reviewable and small** — For a one-folder create, still lock path + starter files + verification in the brief; revert and re-plan if the wrong structure lands.  
   Source: [Introducing Plan Mode · Cursor](https://cursor.com/blog/plan-mode)
