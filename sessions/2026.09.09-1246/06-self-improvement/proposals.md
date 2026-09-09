# Improvement proposals — `2026.09.09-1246`

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | prompt-betterment / skill refs | Publish Q pack reinvented each cycle | Add reusable **publish-cycle** question pack (stage scope / message / agent-push / branch / excludes / one-commit / include current session / **git-root-only**) + disclosed defaults | `references/publish-cycle.md` (new), `prompt-betterment.md`, handoff-templates, SKILL.md pointer |
| P2 | prompt-betterment | Unanswered Qs after a partial answer batch lack a Choose rule | Treat **unanswered** items that disclosed a default as **Choose→that default**; lock Source `Choose (unanswered→default)`; do not block | `prompt-betterment.md`, `01-notes.md` template |
| P3 | handoffs / AGENTS | Org-repo staging can confuse multi-root workspaces | Standing cue: never stage outside `rev-parse --show-toplevel` for this org repo | handoff-templates, `AGENTS.md` one line |
| P4 | implementer / auditor | Already strong GfW vs MSYS + Low dirty finalize | **No change** — confirm in audit; optional one-line self-improver handoff focus for publish cycles | handoff self-improver focus only |
| P5 | templates | Notes template lacks unanswered→Choose / publish continuity hooks | Light template bullets | `sessions/_templates/01-notes.md` |
| P6 | product/corpus | Mid-cycle stub hygiene / optional follow-up commit UX | Defer — user-optional; not workflow law | backlog |

## Prioritization (apply now)

1. **P1** (highest reuse) — reference file + agent/handoff hooks  
2. **P2** — unanswered→Choose defaults  
3. **P3** + **P5** — small standing cues  
4. **P4** — handoff focus line only  

Defer: **P6**.

## Online best-practice notes

Adopted / reinforced (not wholesale rewrites):

- **Keep prompts concise; put detail in skill references** — Cursor Skills docs recommend progressive loading via `references/` so `SKILL.md` stays focused. → New `publish-cycle.md` reference instead of bloating the main skill.  
  https://cursor.com/docs/skills.md
- **Focused subagents; invest in descriptions; avoid overly long agent bodies** — Cursor Subagents best practices. → Encode publish pack once in a reference + short agent hooks, not a second agent.  
  https://cursor.com/docs/subagents.md
- **Skills for repeatable procedures vs one-off subagents** — same docs. Publish question pack is procedural → skill reference, not a new subagent.

Not adopted this cycle: model bracket syntax / `is_background` experiments (out of scope for publish friction).
