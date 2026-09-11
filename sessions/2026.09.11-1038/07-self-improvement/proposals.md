# Proposals — Cycle 16 self-improvement

## Prioritized backlog

| ID | Area | Problem | Proposed change | Files likely touched | Priority |
| --- | --- | --- | --- | --- | --- |
| P1 | orchestrator handoffs | SESSION lag caused Low audit finding; phases looked unfinished mid-cycle | Require flip of Workflow progress **and** Phase checklist **before** launching the next phase (esp. git→auditor) | `.cursor/agents/orchestrator.md` | **Apply now** |
| P2 | prompt-betterment | Truncated Continuity replies (`A — continue st`) work ad hoc | Encode leading-letter + truncated option text as unambiguous option lock (record raw reply) | `.cursor/agents/prompt-betterment.md` | **Apply now** |
| P3 | researcher / implementer | Post–multi-remote clear left stale inventory “uncleared” until this cycle | Explicit Continuity A honesty: flag/flip stale uncleared → Cleared + still-at-root / **not** Complete | `.cursor/agents/researcher.md`, `implementer.md` | **Apply now** |
| P4 | auditor | XL Glob timeout + SESSION lag graded correctly but not standardized | Checklist: XL Glob timeout → Low via implementer Test-Path; mid-cycle SESSION lag → Low/process only | `.cursor/agents/auditor.md` | **Apply now** |
| P5 | session templates | `SESSION.md` template still omits `05-git` / wrong self-improve path | Align template with live 7-phase layout (git-manager permanent) | `sessions/_templates/SESSION.md` | **Apply now** |
| P6 | skill / AGENTS | Optional size-cell honesty confusion | One-line note: optional historical size refresh ≠ hard AC / not Complete cue | defer unless tiny | Deferred |
| P7 | user workload | Unrelated allowlist dirt accumulates across cycles | Optional finish-sync Continuity when only FAW-allowlist dirt remains after push | backlog | Deferred |

## Online check (Cursor agent / skill best practices)

Sources consulted (2026):

- [Best practices for coding with agents](https://cursor.com/blog/agent-best-practices) — plan before coding; structured context; skills for repeatable workflows vs always-on rules; start fresh conversations per logical unit (maps to one FAW session per cycle).
- [Cursor Subagents docs](https://cursor.com/docs/subagents.md) — specialized roles + isolated context; skills for single-purpose procedures; invest in descriptions; verify independently (auditor readonly).
- [Cursor Skills docs](https://cursor.com/docs/skills) — version-controlled `.cursor/skills/`; load on demand; keep procedures in skills not sprawling rules.

**Adopted this cycle:**

- Strengthen **orchestrator handoff bookkeeping** (structured status before next worker) — aligns with subagent isolation + parent aggregation.
- Keep improvements in **agent role files + one template** (skill/procedure), not a large rule rewrite — matches “skills/procedures over always-on bloat.”
- Preserve **auditor as independent verifier** with Read/Glob fallback when Shell blocked.

**Not adopted:** Model-pinning orchestrator vs workers (DeepakNess pattern) — out of scope / would change harness defaults without user ask.
