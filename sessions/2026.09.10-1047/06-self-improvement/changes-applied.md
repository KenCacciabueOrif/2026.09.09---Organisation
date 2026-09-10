# Changes applied

## Applied

- `.cursor/agents/implementer.md` — **Path-presence / Shell fallback**: when Shell/`Test-Path` blocked or stdout empty, use `Read`/`Glob`; log probe method; do not stall; post-move opaque attestation allows Read/Glob equivalent.
- `.cursor/agents/auditor.md` — Same Shell fallback grading (**Low/process**, not Critical/rework when semantic AC holds); reinforce return **full** report body when write blocked.
- `.cursor/agents/orchestrator.md` — **Mandatory** ensure `05-audit/report.md` exists after auditor (persist returned body if needed); update SESSION audit fields before self-improver.
- `.cursor/agents/researcher.md` — INDEX path truth: Read/Glob OK when Shell unavailable; note probe method.
- `.cursor/agents/planner.md` — Opaque/`Test-Path` AC and WorkSpace zero-move attestations allow Read/Glob equivalent + probe method in log.
- `.cursor/skills/full-agent-workflow/references/handoff-templates.md` — researcher/planner/implementer/auditor/self-improver handoffs: Shell fallback + auditor full-body return + orchestrator persist focus.
- `sessions/_templates/04-log.md` — probe-method hint comment.
- `sessions/_templates/05-report.md` — Shell-unavailable Low/process hint under gaps.

## Why

Cycle 11 passed with correct Read path-presence when Shell was unavailable, but that was only a deviation note. Encoding the fallback keeps agent-owned attestation without user PATH/Shell chores and reduces false-fail risk. Auditor readonly write failure remains orchestrator bookkeeping (Cursor subagent file-output guidance ≈ persist, not new hooks).

## No safe improvement

n/a — improvements applied.
