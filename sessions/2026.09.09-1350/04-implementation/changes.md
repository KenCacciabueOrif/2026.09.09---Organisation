# Changes — `sessions/2026.09.09-1350`

| Path | Action | Why |
| --- | --- | --- |
| `.cursor/skills/full-agent-workflow/references/pull-cycle.md` | create/update | FAW default = allowlisted auto-commit then `--ff-only`; abort only unrelated dirty |
| `.cursor/skills/full-agent-workflow/references/publish-cycle.md` | create/update | Mirror same allowlist autonomy for publish (Q8) |
| `.cursor/skills/full-agent-workflow/SKILL.md` | modify | Allowlist-first pull/publish; non-ff blocker guidance |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | modify | Remove universal dirty-abort handoffs |
| `.cursor/skills/full-agent-workflow/references/session-structure.md` | modify | Pull session notes: allowlist + non-ff |
| `.cursor/rules/full-agent-workflow.mdc` | modify | Align law with allowlist default |
| `AGENTS.md` | modify | Align portable law with allowlist default |
| `.cursor/agents/prompt-betterment.md` | modify | Pull pack = allowlist auto-commit default |
| `.cursor/agents/researcher.md` | modify | Partition allowlist vs unrelated dirty |
| `.cursor/agents/implementer.md` | modify | Auto-commit allowlist; typed non-ff |
| `.cursor/agents/auditor.md` | modify | Correct allowlist path vs unrelated abort |
| `.cursor/agents/orchestrator.md` | modify | Block bookkeeping for non-ff / unrelated |
| `sessions/_templates/SESSION.md` | modify | Blocker vocabulary includes other/non-ff |
| `sessions/2026.09.09-1350/**` | create/update | This cycle’s FAW artifacts |
| Other allowlisted `sessions/**` dirt | stage as present | Prior session finalize / templates already dirty ⊆ allowlist |

**Not mutated:** corpus FS (`catalogue/**`, `program/**` moves/renames/deletes); taxonomy/must-preserve labels.
