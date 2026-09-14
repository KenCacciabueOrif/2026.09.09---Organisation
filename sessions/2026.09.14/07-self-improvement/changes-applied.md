# Changes applied

## Applied

- `.cursor/agents/planner.md` — Added `product_settings` mutation class (plan-gate n/a; same-run; primary+fallback extension IDs).
- `.cursor/agents/orchestrator.md` — Resume/**retry** skip re-implementer when 04 complete; `product_settings` same-run + no corpus plan gate (with `docs_only`).
- `.cursor/agents/implementer.md` — Open VSX/CLI not-found → plan fallback; soft Reload not a blocker; `product_settings` attestations.
- `.cursor/agents/auditor.md` — `product_settings` checklist; soft Reload = Low only.
- `.cursor/skills/full-agent-workflow/SKILL.md` — Resume/retry skip-04; `product_settings` gate/same-run; soft Reload tip.
- `.cursor/skills/full-agent-workflow/references/handoff-templates.md` — Planner/implementer/auditor/mid-flip reminders for product_settings + Marketplace fallback + mid SESSION flip; self-improver focus line updated.
- `.cursor/rules/full-agent-workflow.mdc` — Same-run includes `product_settings`; retry skip-04.
- `AGENTS.md` — Mutation taxonomy + same-run + retry skip-04.
- `sessions/_templates/SESSION.md` — Mutation class + note + plan-gate checkbox.
- `sessions/_templates/03-plan.md` — `product_settings` in class table/note.

## Why

This cycle was an ad-hoc editor-extension fix (`product_settings`) with Marketplace-only primary failure, interrupt/retry resume, and auditor Lows on soft Reload + mid-checklist lag. Encoding those patterns reduces false plan gates, rediscovery of Open VSX gaps, and user “retry” thrash.

## No safe improvement

n/a — improvements applied.
