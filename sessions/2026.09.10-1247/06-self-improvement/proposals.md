# Proposals — Cycle 12 self-improvement

## Online check (short)

Cursor guidance still favors: focused subagents + skills for deterministic multi-step workflows; orchestrator parent delegates specialists; persist structured outputs in files rather than chat-only ([Subagents](https://cursor.com/docs/subagents), [Skills](https://cursor.com/docs/skills)). Adopted: keep orchestrator non-implementing; encode resume + auditor-report persist in skill/law (file-backed session continuity); no new generic helper agents.

## Prioritized backlog

| ID | Area | Problem | Proposed change | Files likely touched | Priority |
| --- | --- | --- | --- | --- | --- |
| P1 | Orchestrator / skill / rules | Mid-cycle resume of incomplete session was practiced but not law — parallel folder risk | Prefer resume incomplete same-cycle SESSION when user names it as prior; do not bootstrap parallel collision folder | `orchestrator.md`, `SKILL.md`, `full-agent-workflow.mdc`, `AGENTS.md`, `session-structure.md`, `SESSION` template, handoff focus | **Apply now** |
| P2 | Skill | Auditor write-block persist lived only in agent; skill Done/Rework silent | Mirror orchestrator persist rule in SKILL Rework + Done | `SKILL.md` | **Apply now** |
| P3 | Templates / handoffs | Resume + persist not visible in SESSION seed / self-improver focus line | Note on template; add resume focus bullet | `_templates/SESSION.md`, `handoff-templates.md` | **Apply now** |
| P4 | Shell fallback | Already encoded Cycle 11; this cycle reconfirmed | No further agent text unless gaps appear | — | Defer (done) |
| P5 | WorkSpace Continuity / informed consent | Already encoded; cycle behaved correctly | No product/law expansion | — | Defer (stable) |
| P6 | Hooks | Auto-save auditor outputs via Cursor hooks | Optional infra; orchestrator persist sufficient | hooks | Carry backlog |
| P7 | Inventory MB column | WorkSpace size column vs Notes band | Product/docs optional | `catalogue/inventory.md` | Carry backlog |

## Not proposing

- User PATH / Shell chores every cycle — agent Read/Glob autonomy already preferred.
- Whole-tree archive or Complete while WorkSpace remains — fail-closed law stays.
