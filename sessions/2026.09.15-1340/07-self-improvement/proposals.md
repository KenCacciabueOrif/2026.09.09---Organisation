# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | orchestrator / researcher / rules | Next FAW would inherit dashboard topic; user standing amendment forbids defaulting to dashboard after Cycle 22 | Encode **workstream rotation**: each cycle research must **justify** workstream vs `program/ROADMAP.md` (not inherit prior topic); after Cycle 22 dashboard is **done for now**; Next FAW default = WorkSpace Continuity X / `#4` approval (Q3=A) or research-justified alternative | `.cursor/agents/orchestrator.md`, `researcher.md`, `prompt-betterment.md`, `.cursor/rules/full-agent-workflow.mdc`, `AGENTS.md`, skill SKILL.md / handoffs |
| P2 | planner / skill / templates | `catalogue_product` used successfully but absent from mutation taxonomy → gate/class drift | Add **`catalogue_product`**: org-repo catalogue **code+data**; not corpus `fs_mutation`; **plan gate still required** when Continuity Q6=A (or material catalogue product change) | `planner.md`, SKILL.md, handoff-templates, SESSION template, `AGENTS.md`, implementer/auditor brief |
| P3 | planner / implementer | L-both learned in Cycle 22 only | Document **L-both** pattern: emit JSON (canonical) + classic JS module (`window.__…__`); HTML prefers module on `file://`, `fetch` JSON on HTTP; fatal UX on failure | `planner.md` (short), optional skill note |
| P4 | orchestrator bookkeeping | Plan-gate answer not mirrored to `01-prompt-betterment/notes.md`; mid checklist lag | Light reminder: after plan gate, append gate reply to notes **or** SESSION (already allowed); flip mid-git checklist before auditor | orchestrator.md (one line) — **defer if already covered** |
| P5 | auditor | Ask-readonly cannot re-run smoke | Keep FS+log evidence; do not invent Shell for auditor | backlog only |

## Online best-practice notes

- Keep always-on rules thin; put procedural detail in skills/agents — [efficient .cursor directory](https://dev.to/shrouwoods/an-efficient-cursor-directory-less-context-better-agents-kl0). Adopted: encode rotation + `catalogue_product` as short always-on bullets + agent detail, not a new mega-rule.
- Skills load on demand; invest in clear routing descriptions — [Cursor skills docs](https://cursor.com/docs/skills). Adopted: extend existing FAW skill plan-gate section rather than a new skill.
- Subagents for isolated phases; avoid duplicating single-purpose choreography — [Cursor subagents](https://cursor.com/docs/subagents.md). Adopted: researcher owns workstream justification; orchestrator only locks/hints Next FAW.

## Apply this cycle

- **P1, P2, P3** (high value, low risk).
- **P4** only if a one-line gap remains after reading orchestrator.
- **P5** deferred.
