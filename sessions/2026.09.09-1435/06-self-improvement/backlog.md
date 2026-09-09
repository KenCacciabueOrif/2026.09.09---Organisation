# Deferred backlog

| ID | Proposal | Why deferred / next action |
| --- | --- | --- |
| **B1 Finish sync** | New FAW pull/merge cycle to incorporate `origin/main` (`489f03a`) into local tip (`f3e1119`, ahead/behind 2/1). **Path A:** Choose **Q2=B** + **Q3b=B** with explicit resolve rule (`ours` / `theirs` / `combined`) for the 4 FAW paths (`.cursor/agents/prompt-betterment.md`, `.cursor/rules/full-agent-workflow.mdc`, `.cursor/skills/full-agent-workflow/references/handoff-templates.md`, `sessions/_templates/01-notes.md`). **Path B:** User resolves those conflicts (or edits) then agent continues merge/verify (Q3b=C). Still fail-closed if any non-allowlist conflict appears. Never claim sync success until HEAD incorporates `origin/main`. | This session locked Q3b=A — resolve not authorized here |
| B2 | Auto-default Q3b=B when merge-tree predicts only allowlist conflicts | Too aggressive; keep default A until user opts in (P5) |
| B3 | Optional follow-up allowlist commit of post-abort session finalize dirt | Cosmetic; Low / expected — not required for process pass |

## Suggested user ask for next cycle

Plain language: “Finish the interrupted merge. Conflicts are only workflow docs. Should the agent combine them with a stated rule (keep ours / take theirs / merge both), or will you fix the four files first?”
