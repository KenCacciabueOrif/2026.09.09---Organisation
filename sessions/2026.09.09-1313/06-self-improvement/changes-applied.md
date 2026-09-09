# Changes applied

## Applied

- `.cursor/agents/planner.md` — Split `docs_only` vs `fs_mutation` definitions; explicitly include org-repo scaffolding creates (folders/READMEs) under `docs_only`; warn against conflating with ROADMAP move cycles. **Why:** this cycle correctly used `docs_only` for `Notes/`; future planners need that rule in agent law.
- `.cursor/skills/full-agent-workflow/SKILL.md` — Plan-gate step: mandatory only for `fs_mutation`; `docs_only` includes org-repo creates without automatic pause. **Why:** match planner clarification at orchestrator skill level.
- `.cursor/agents/orchestrator.md` — Plan-gate user-comms: same `docs_only` scaffolding vs `fs_mutation` corpus batch wording; also: update Workflow progress in place (no duplicate checklist). **Why:** orchestrator relays gates; avoid false pauses; this session had a duplicated progress block.
- `.cursor/skills/full-agent-workflow/references/handoff-templates.md` — Planner handoff + self-improver focus: `docs_only` scaffolding note; Choose-all / ad-hoc vs corpus focus. **Why:** handoffs are the practical checklist subagents see.
- `sessions/_templates/03-plan.md` — Note under Mutation class table clarifying org-repo creates ≠ `fs_mutation`. **Why:** template drives plan shape every cycle.
- `.cursor/agents/prompt-betterment.md` — Choose / Choose-all: require durable one-line ask summary per Q plus decision table. **Why:** mild Choose-all auditability friction (option tables only in chat).
- `sessions/_templates/01-notes.md` — Template reminder for Choose-all ask summaries. **Why:** match prompt-betterment change.
- `AGENTS.md` — One phrase: `docs_only` includes org-repo scaffolding; `fs_mutation` = corpus batches. **Why:** portable law.
- `.cursor/rules/full-agent-workflow.mdc` — Same one-line `docs_only` scaffolding clarification. **Why:** always-on rule mirrors AGENTS.

## No safe improvement

N/A — improvements applied.
