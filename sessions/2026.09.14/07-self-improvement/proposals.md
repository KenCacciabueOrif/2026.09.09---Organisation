# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | skill / orchestrator / planner / templates | `product_settings` (editor extension + local fixture) not in mutation taxonomy → false plan-gate or pause | Add class: **not** corpus `fs_mutation`; plan-gate **n/a**; same-run continue when `ready_to_implement: yes` (like `docs_only`) | `SKILL.md`, `orchestrator.md`, `planner.md`, `sessions/_templates/SESSION.md`, `03-plan.md`, `AGENTS.md` (short) |
| P2 | implementer / skill | Cursor CLI often resolves Open VSX; Marketplace-only IDs fail → thrash | Document: try primary; on not-found/404 use **plan-named fallback**; log; optional soft user Marketplace UI only if no fallback | `implementer.md`, `SKILL.md` short note, handoff implementer blurb |
| P3 | orchestrator / skill | Interrupt mid-implementer + user “retry” risks re-running 04 when artifacts done | Resume same session; if `04-implementation/log.md` (and changes) already **complete** → **skip** implementer; continue at next incomplete phase (mid git → …) | `orchestrator.md`, `SKILL.md`, `SESSION.md` template note |
| P4 | orchestrator | Mid-cycle checklist lag after mid git (auditor Low) | Already law — reinforce handoff reminder one line; no new process | `handoff-templates.md` mid→auditor |
| P5 | auditor / implementer | Soft Reload after extension install treated like user debt | Soft tip only; Low; **not** Critical / not `rework_owner: user` chore; agent FS/`extensions.json` verify OK | `auditor.md`, `implementer.md` |
| P6 | auditor | product_settings checklist missing | Mirror docs_only zero-corpus + extension/settings attest; soft Reload Low | `auditor.md` |
| P7 | dual git | Already strong mid+final | No change — keep final closing pass after self-improver | — |
| P8 | user-workload | Prefer agent-owned defaults | Encode fallback + skip re-implement on retry; don’t invent PATH/Reload rituals as user backlog | (via P2–P5) |

## Online best-practice notes

Adopted (aligned, not wholesale rewrite):

- **Skills for procedural workflows; rules for always-on invariants; subagents for isolated roles** — keep FAW as skill + orchestrator subagent; encode `product_settings` in skill/agents rather than bloating always-on rules beyond a short pointer. Sources: [Cursor agent best practices](https://cursor.com/blog/agent-best-practices), [Subagents docs](https://cursor.com/docs/subagents.md).
- **Restartable on-disk state + structured handoffs** — reinforce resume-skip-04 when artifacts exist (session as durable state). Same sources + changelog framing for long-running agent work: [Cursor 2.4 changelog](https://cursor.com/changelog/2-4).
- **Keep prompts short and specific** — add narrow bullets for Marketplace fallback / product_settings; avoid new multi-page essays in agent files.

Not adopted: Best-of-N / worktree parallelism for FAW (orthogonal to org-repo orchestration).
