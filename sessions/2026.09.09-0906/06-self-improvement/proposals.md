# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | implementer | Post-push log lines cannot be in the same “exactly one commit” publish; left Medium audit issue | Encode: write pre-push log/changes **before** commit; after push either (A) leave post-push lines dirty as **known tradeoff** or (B) optional tiny follow-up commit for session finalize when plan allows | `.cursor/agents/implementer.md` |
| P2 | auditor | Medium on expected chicken-egg dirty session files | Treat intentional single-commit + dirty post-push `04-implementation/*` / `SESSION.md` as **Low / expected** when hash+push verified live; only Medium if pre-push log never committed | `.cursor/agents/auditor.md`, `sessions/_templates/05-report.md` |
| P3 | skill / plan template | Plans say “one commit” without finalize tradeoff | One short bullet under push + plan risk row for single-commit vs session finalize | `SKILL.md`, `sessions/_templates/03-plan.md`, `session-structure.md` |
| P4 | AGENTS.md | Portable law missing this nuance | One-line note: session post-push notes may stay dirty or need follow-up commit | `AGENTS.md` |
| P5 | planner | Plans may over-constrain “exactly one commit” when session docs need closure | Prefer AC: “one product/publish commit”; optional “session-finalize commit allowed if plan says so” | `.cursor/agents/planner.md` (defer if P1–P4 enough) |
| P6 | handoff | Implementer handoff silent on finalize order | Add one line to implementer handoff template | `handoff-templates.md` (defer — low urgency) |

## Online best-practice notes

- **Focused subagents, concise prompts** — Cursor docs: single responsibility; long rambling agent files dilute focus. Adopted: keep P1–P4 as short bullets, not a new agent. https://cursor.com/docs/subagents
- **Skills as canonical checklists** — Prefer skill/reference as source of truth; agents point at it. Adopted: put tradeoff in `SKILL.md` + `session-structure.md`, mirror briefly in implementer/auditor. https://cursor.com/docs/skills
- **Subagents vs skills** — Don’t spawn new agents for a one-shot process rule; encode in skill/agent markdown. Reinforced decision to patch existing files only. https://philliant.com/posts/20260808-parallel-subagents-when-to-use-them-vs-skills/

## Apply now vs defer

- **Now:** P1, P2, P3, P4 (highest value for next publish cycle; low risk).
- **Defer:** P5, P6.
