# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | planner / skill / templates | Future planners may treat any disk create (e.g. org-repo `Notes/`) as `fs_mutation` needing a corpus plan gate | Explicitly define: **`docs_only` includes scaffolding creates inside this organisation git root** (folders, README/docs) when there are **zero corpus moves/renames/deletes**; `fs_mutation` = corpus / catalogue-backed path mutations (typically under `C:\Project` or move batches). Org-repo create ≠ automatic plan gate. | `.cursor/agents/planner.md`, `.cursor/skills/full-agent-workflow/SKILL.md`, `sessions/_templates/03-plan.md`, handoff-templates.md |
| P2 | prompt-betterment | Choose-all leaves full Q option/tradeoff tables only in chat history | When user says Choose / Choose all: keep a **short durable ask summary** (one line per Q: what was asked) plus the decision table already required — so later phases/audit do not need chat. | `.cursor/agents/prompt-betterment.md`, optionally `sessions/_templates/01-notes.md` |
| P3 | handoff / skill | Self-improver focus list under-emphasizes ad-hoc org-repo vs ROADMAP confusion | Add focus hint: ad-hoc org-repo scaffolding vs program `fs_mutation`; Choose-all friction; informed-consent jargon. | `handoff-templates.md` (self-improver block) |
| P4 | prompt-betterment | Trivial create goals still get max Q volume | Soft guidance: for clearly trivial single-folder/docs creates, prefer ≤5–7 Qs unless push/corpus/program applies. | `.cursor/agents/prompt-betterment.md` |
| P5 | orchestrator / SESSION | Duplicate Workflow progress checklist left in SESSION | When updating SESSION, replace the progress block — do not append a second unchecked copy. | `.cursor/agents/orchestrator.md` or skill bootstrap note |
| P6 | AGENTS.md / rules | Portable law says docs_only vs fs_mutation but not org-repo create | One clarifying phrase matching P1 (keep short). | `AGENTS.md`, `.cursor/rules/full-agent-workflow.mdc` |

## Priority for this cycle

- **Apply now (safe):** P1, P2 (agent + template one-liners), P3, P6 (minimal).
- **Defer:** P4 (soft Q-cap — judgment call, avoid over-constraining), P5 (orchestrator hygiene — low impact this cycle).

## Online best-practice notes

Checked recent Cursor subagent/skill guidance:

- **Focused subagents + invest in descriptions; keep prompts concise** — [Cursor Subagents docs](https://cursor.com/docs/subagents.md). Adopted as constraint: small clarifications to existing agents, not new generic helpers or long rewrites.
- **Skills for repeatable checklists; subagents for role isolation** — [Learn Cursor — Agent Skills](https://www.learncursor.dev/learn/cursor-agents/cursor-agent-skills); [philliant — parallel subagents vs skills](https://philliant.com/posts/20260808-parallel-subagents-when-to-use-them-vs-skills/). Adopted: put the mutation-class definition in planner + skill/templates (canonical checklist), not a new subagent.
- **Independent verification / readonly auditors** — [Agentic Thinking — Subagents](https://agenticthinking.ai/blog/subagents-fresh-context/). No change needed; auditor already separate. Reinforces not collapsing self-improver into product implementer.
