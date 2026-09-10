# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | implementer / auditor / researcher | Shell stdout empty or Ask-readonly Shell blocked → agents improvise Read path-presence; not encoded → future false-fail risk | Encode **path-presence fallback**: when Shell/`Test-Path`/porcelain unavailable, use filesystem `Read`/`Glob` on known paths; log probe method; semantic attestation holds → **Low/process**, not fail | `.cursor/agents/implementer.md`, `auditor.md`, `researcher.md` |
| P2 | planner | Plans hard-require `Test-Path` wording in zero-move / opaque attestations | Allow **`Test-Path` or Read/Glob equivalent**; name probe method in log AC | `.cursor/agents/planner.md` |
| P3 | orchestrator / handoffs | Auditor often cannot write `report.md`; persist rule exists but handoff still assumes write | Reinforce: after auditor return, **always** ensure `05-audit/report.md` exists (write from return if missing); handoff: return full report body when write blocked | `.cursor/agents/orchestrator.md`, `auditor.md`, `references/handoff-templates.md` |
| P4 | templates | `04-log` / `05-report` silent on probe method / Shell Low | Tiny template hints for probe method + Shell-unavailable = Low when semantic OK | `sessions/_templates/04-log.md`, `05-report.md` |
| P5 | Continuity law | Cycle 11 proved post–strategy defaults; no gap | **No change** — already encoded Cycle 10; only cite in audit | — |
| P6 | skill focus line | Self-improver focus list long; Shell fallback not listed | Add brief Shell/Read attestation fallback to self-improver focus bullet | `references/handoff-templates.md` |
| P7 | hooks (Cursor docs) | Docs suggest hooks for structured subagent file output | **Defer** — orchestrator persist is FAW equivalent; hooks are optional infra | backlog |

## Online best-practice notes

- **Focused subagents + concise prompts; avoid oversized agent bodies** — [Cursor Subagents](https://cursor.com/docs/subagents): keep edits small; one concern per file (adopted: P1–P4 only, no Continuity rewrite).
- **Skills load progressive references** — [Cursor Skills](https://cursor.com/docs/skills): prefer handoff/template tweaks over bloating `SKILL.md` body (adopted: handoff-templates + agents; SKILL.md untouched this pass).
- **Hooks for consistent file output from subagents** — same Subagents doc: FAW uses orchestrator persist for readonly auditor (P3 reinforce now; dedicated hooks deferred as P7).
- Independent verification via separate auditor context already matches “independent verification of work” guidance — keep auditor readonly + orchestrator persist.
