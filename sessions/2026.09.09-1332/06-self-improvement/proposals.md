# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | skill / prompt-betterment | No standing pull question pack; ad-hoc Qs each cycle | Add `pull-cycle.md` mirroring `publish-cycle.md` (org root, ff-only, dirty policy, agent Shell, fail-closed, GfW) | `references/pull-cycle.md`, `prompt-betterment.md`, `SKILL.md`, `handoff-templates.md` |
| P2 | agents / rules | `dirty_working_tree` used in cycle but missing from blocker taxonomy | Add third git blocker: `dirty_working_tree` (≠ `agent_environment` / `user_credentials`); dirty-abort → `blocked`, never false `complete`; `rework_owner: user` | `implementer.md`, `orchestrator.md`, `auditor.md`, `AGENTS.md`, `full-agent-workflow.mdc`, `SKILL.md` |
| P3 | orchestrator | SESSION stayed `in_progress` after implementer `blocked` | Require immediate SESSION status/checklist update when implementer returns `blocked` / `aborted_dirty` (Low bookkeeping) | `orchestrator.md`, `SESSION.md` template, `handoff-templates.md` |
| P4 | implementer / auditor | Push-only GfW + status honesty | Extend GfW absolute path + dual preflight + fail-closed honesty to **pull**; auditor: process pass + unmet sync AC + user rework is valid | `implementer.md`, `auditor.md`, handoffs |
| P5 | informed consent | No debt this cycle; keep pull pack plain-language | In pull pack: define dirty abort / fail-closed / ff-only in one sentence; pros/cons on dirty options | `pull-cycle.md` |
| P6 | deferred | Auto-stash / user dirty-cleanup helper cycle | Separate FAW only if user asks; do not invent stash in pull default | backlog |

## Online best-practice notes

- **Focused subagents + concise prompts** — Cursor docs: single clear responsibility; long prompts dilute focus. Adopted: add a **skill reference** (`pull-cycle.md`) rather than bloating agent bodies. Source: [Subagents](https://cursor.com/docs/subagents).
- **Filesystem as handoff channel** — Prefer durable markdown artifacts over retelling in prompts (same pattern as publish pack). Source: [Towards AI — subagents in agent coding](https://pub.towardsai.net/subagents-in-agent-coding-what-they-are-why-you-need-them-and-how-they-differ-in-cursor-vs-1c81e4f32b8d).
- **Parent as manager; one-level delegation** — Orchestrator updates SESSION after each phase return (bookkeeping), does not re-implement. Source: [Cursor forum — layering/managing agents](https://forum.cursor.com/t/layering-managing-agents/158222/3).

### Apply now vs defer

- **Now:** P1–P5 (docs/agents/skill/rules/templates only).
- **Defer:** P6 (product/git behavior change needs user ask).
