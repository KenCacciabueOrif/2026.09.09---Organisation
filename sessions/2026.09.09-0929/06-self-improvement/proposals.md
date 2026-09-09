# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | orchestrator handoffs | Multi-cycle programs lack first-class continuity (new session, ROADMAP next slice, no moves in docs FAW) | Add **program / multi-cycle** bootstrap + completion rules: read `program/ROADMAP.md` when present; one FAW session per cycle; never start a move batch inside a docs-only cycle | `.cursor/agents/orchestrator.md`, `sessions/_templates/SESSION.md` |
| P2 | skill steps | User plan gate is optional; move batches need mandatory approval | Make **user plan gate mandatory** when plan includes FS moves/renames/deletes outside the org-repo docs set; keep optional for pure docs | `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/rules/full-agent-workflow.mdc` |
| P3 | planner | Plans can omit mutation class / approval / git-atomic wording | Require plan to classify **docs-only vs FS-mutation**; for mutation: explicit user-approval gate + git-root atomicity + opaque secrets/deps | `.cursor/agents/planner.md` |
| P4 | implementer | Zero-move / git-atomic discipline only in this cycle’s log, not agent law | Add **docs-only attestation** and **no unsupervised FS mutation** / atomic git-root rules | `.cursor/agents/implementer.md` |
| P5 | auditor | No reusable checklist for no-move / approval / git-atomic cycles | Add verification bullets for zero-move cycles and approved-move cycles | `.cursor/agents/auditor.md` |
| P6 | handoffs / prompt-betterment | Next-cycle handoffs may omit program pointers and corpus safety questions | Extend handoff templates + prompt-betterment corpus/multi-cycle question cues | `handoff-templates.md`, `.cursor/agents/prompt-betterment.md` |
| P7 | criteria hygiene | Soft AC wording (size “if available” vs required) caused Low audit noise | Prefer planner note: optional signals must not be hard AC checkboxes | `.cursor/agents/planner.md` (one bullet under P3) |
| P8 | session hygiene | Prior-session WT dirt confuses audit of later cycles | Defer: optional SESSION hygiene tip / backlog only this cycle | backlog |

## Online best-practice notes

Adopted / aligned ideas (this cycle):

- **Rules = static law; Skills = dynamic workflow** — keep multi-cycle/mutation gates in skill + orchestrator; thin always-apply rule — [Cursor agent best practices](https://cursor.com/blog/agent-best-practices).
- **Specialized subagents + parent orchestrator sequence; phase verification** — reinforce handoffs and auditor checklists rather than collapsing roles — [Cursor subagents docs](https://cursor.com/docs/subagents.md); [forum multi-agent skills pattern](https://forum.cursor.com/t/how-i-set-up-multi-agent-workflows-in-cursor-with-reusable-skills-and-agents/166742).
- **Shorter task-scoped cycles + durable state outside chat** — one FAW session per program cycle; persist progress in `program/ROADMAP.md` + `catalogue/` + `SESSION.md` (not transcript-only) — [cloud agent lessons](https://cursor.com/blog/cloud-agent-lessons); design-corpus / inventory authority patterns ([Misaligned design-corpus](https://cameron.tngl.io/misaligned/process/meta/)).
- **Owner-gated apply after inventory/dry-run** — mandatory user gate before FS mutation batches; dry-run/docs-first — [LoopX material lifecycle](https://huangruiteng.github.io/loopx/docs/capabilities/material-lifecycle/) (owner-gated apply + inventory before cutover).
- **Atomic units / no silent history rewrite** — git roots stay atomic until an explicit git-strategy cycle — aligns with program ROADMAP and git-workflow skill atomic-commit ethos ([Tash000/git-workflow-skill](https://github.com/Tash000/git-workflow-skill)).

Not adopted now (deferred): parallel best-of-N agents for inventory; SDK agent-state stores; automated dry-run migrator scripts.
