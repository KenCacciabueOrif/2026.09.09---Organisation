# Online prompt tips — Cycle 4 Medium wrappers (first subset)

Actionable tips for scoping an irreversible folder-move batch with nested git and a mandatory plan gate.

| # | Tip | Why it matters here | Source |
| --- | --- | --- | --- |
| 1 | **Clarify before you mutate** — research requirements, ask focused questions, then plan; wait for approval before building. | Matches FAW: questions → research → plan → **plan gate** → moves. | [Cursor — Agent best practices](https://cursor.com/blog/agent-best-practices) |
| 2 | **Prefer Plan Mode–style artifacts** — editable plan with concrete paths; refine the plan rather than patching a bad run. | Move maps (`from → to`) must be reviewable and editable before implementer. | [Cursor — Plan Mode](https://cursor.com/docs/agent/plan-mode) |
| 3 | **Bound the change set** — name allowed sources, forbidden trees, and “stop if unexpected.” | Eight Medium wrappers vs a 2–3 subset; must-preserve / org repo hands-off; fail-closed on worktrees. | [OTF — plan, scope, verify](https://otf-kit.dev/blog/cursor-agent-best-practices) |
| 4 | **Write measurable acceptance criteria** — “done” = observable pre/post path facts + catalogue updates, not “looks moved.” | Auditor needs proof: source gone, target present, INDEX current path updated, reverse-move logged. | [OTF — acceptance checklist](https://otf-kit.dev/blog/ai-agent-acceptance-checklist) |
| 5 | **Separate known locks from inspect-needed facts** — mark Continuity vs “research must live-check.” | INDEX may still list Early/simple old paths; candidates still at `C:\Project` root — verify before planning. | [OTF — focused session prompts](https://otf-kit.dev/blog/cursor-prompts-agent-sessions) |
| 6 | **Human approval is per batch, not sticky** — approving one sensitive action does not auto-approve the next. | Starting FAW / Continuity / Choose ≠ approving this cycle’s move map. | [Agentcy — Approval flows](https://docs.agentcylabs.com/how-to/agents/approvals) |
| 7 | **Keep prompts specific and verifiable** — say what success looks like and what must not change (secrets opaque, atomic nested `.git`). | NextPWATraining `.env` must move without being read; wrapper + nested git stay one unit. | [Cursor — Agent best practices](https://cursor.com/blog/agent-best-practices) |

## How these tips shaped this phase

- Questions lead with **subset vs all eight** and Continuity for taxonomy / must-preserve (not re-blocking Early/simple forever).
- Refined prompt encodes **plan gate**, **fail-closed**, and **acceptance checks** as stopping conditions.
- Nested-git atomicity and `.env` opacity are constraints, not research topics for deep redesign.
