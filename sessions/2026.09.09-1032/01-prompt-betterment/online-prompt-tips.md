# Online prompt tips — Cycle 2 Early/simple (fs_mutation)

Session: `sessions/2026.09.09-1032/01-prompt-betterment/`  
Goal type: multi-cycle corpus organisation with **first move-capable** batch + mandatory approval gates.

## Actionable tips

1. **Goal + constraint + verify** — State the outcome (relocated Early/simple folders + updated INDEX), hard non-touch list (must-preserve, org repo), and binary checks (paths exist only at targets; sources gone; INDEX rows updated). Vague “organise next” prompts under-specify irreversible FS work.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

2. **Plan before mutate** — Treat move maps like Plan Mode: clarify → research → editable plan → **explicit user approve** → execute. Do not collapse propose and execute into one unattended step for first-move cycles.  
   Source: [Cursor Plan Mode docs](https://cursor.com/docs/agent/plan-mode)

3. **Name context pointers, not guesses** — Point at known artefacts (`program/ROADMAP.md`, `catalogue/taxonomy.md`, `must-preserve.md`, `INDEX.md`, prior sessions) and the exact six folder paths under `C:\Project`; avoid inventing target trees the user has not ratified.  
   Source: [Prompt Engineering for Developers](https://www.learncursor.dev/guides/prompt-engineering-for-developers)

4. **One task / one cycle boundary** — Keep this FAW to Early/simple only; defer git-strategy, Obsidian, ProjetOrif, medium wrappers. Side goals become separate sessions.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

5. **Encode verification that matches risk** — For FS moves: pre-move existence + no unexpected `.git`; post-move target listing; INDEX/status sync; documented rollback (move-back) expectation. Prefer observable path/INDEX checks over “looks organised.”  
   Source: [Promptyze — Agent Mode verification](https://promptyze.com/cursor-agent-mode-let-claude-build/)

6. **Approval language must be explicit** — Separate (a) taxonomy sign-off/waiver, (b) must-preserve review/waiver, (c) per-batch move-map approval. Prior-cycle “proposed-ratified” ≠ final lock.  
   Source: [Cursor Plan Mode — review before build](https://www.learncursor.dev/learn/cursor-agents/agent-plan-mode)

7. **If the run misses, refine the plan and re-run** — Prefer revert + sharper plan over compounding partial moves mid-batch.  
   Source: [Cursor Plan Mode docs](https://cursor.com/docs/agent/plan-mode)

## Clarifying questions (for user / orchestrator pause)

See `notes.md` — Questions section. Orchestrator should pause until answers land, then resume researcher with locked Answers.
