# Changes applied

Session: `sessions/2026.09.09-0929/06-self-improvement/`  
Applied proposals: **P1–P7** (P8 deferred).

## Applied

| Path | What | Why |
| --- | --- | --- |
| `.cursor/agents/orchestrator.md` | Multi-cycle bootstrap (ROADMAP, one session/cycle); mandatory plan gate for corpus FS mutation | Continuity + approval for later move cycles |
| `.cursor/skills/full-agent-workflow/SKILL.md` | Step 4 plan gate mandatory for FS mutation; program framing on bootstrap | Encode Cycle 0 user rule into workflow skill |
| `.cursor/rules/full-agent-workflow.mdc` | New bullet 7: multi-cycle + mutation approval + git atomicity | Always-apply law for future FAWs |
| `.cursor/agents/planner.md` | Required `docs_only` \| `fs_mutation`; optional-signal ≠ hard AC | Prevent size-style AC drift; gate moves |
| `.cursor/agents/implementer.md` | Approval check; zero-move attestation; git-root / opaque secrets rules | Make Cycle 0 discipline reusable |
| `.cursor/agents/auditor.md` | Docs-only / FS-mutation verification checklist | Match auditor to program gates |
| `.cursor/agents/prompt-betterment.md` | Corpus / multi-cycle clarifying question cue | Faster Cycle 1+ alignment |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | Program + mutation + attestation cues in handoffs | Orchestrator handoffs carry gates |
| `.cursor/skills/full-agent-workflow/references/session-structure.md` | Program framing fields documented | SESSION hygiene for multi-cycle |
| `sessions/_templates/SESSION.md` | Program framing section | New sessions track cycle/approval |
| `AGENTS.md` | Multi-cycle / corpus FS verification bullet | Portable harness law |

## No safe improvement

N/A — improvements applied.

## Intentionally not changed

- Product artefacts under `program/` / `catalogue/` (user goal; already audited pass).
- Orchestrator remains non-implementing for user product goals.
- No secrets; no corpus FS moves in this self-improve step.
