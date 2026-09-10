# Improvement proposals — Cycle 7 self-improvement

## Prioritized backlog

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | implementer Continuity | Nested `.git` file locks broke atomic `Move-Item`; recovery was invent-on-the-fly | Encode Windows lock Continuity: prefer `Move-Item`; on PermissionDenied/split → reunify into destination; `robocopy /E /MOVE` for remaining children; remove **only** empty leftover `.git` shells (0 children); never delete non-empty payload; re-attest nested git; log as deviation **not** scope expansion | `.cursor/agents/implementer.md` |
| P2 | prompt-betterment / orchestrator | After partial Multi-experiment, next FAW might jump Primary next, reopen Medium, or re-ask first-batch four-name pack | Named **Multi-experiment remaining** Continuity: lock **same row / remaining names only** (`PWAExemple`, `WorkSpace`); carry first-batch Continuity; short pack; do not reopen Medium/Early or re-move archived peers | `.cursor/agents/prompt-betterment.md`, `orchestrator.md`, handoff-templates, rules/AGENTS, `_templates/01-notes.md` |
| P3 | planner / PB Continuity | `WorkSpace` fail-closed (multi-remote / backup roots) — risk of force-including next cycle | Default remaining map may prefer **PWAExemple** first; `WorkSpace` stays git-strategy / fail-closed until dedicated plan — agent-owned, not user chore | `.cursor/agents/planner.md`, `prompt-betterment.md` |
| P4 | auditor | Process recovery vs AC could be re-litigated as Critical | One-liner: when end-state nested-git + paths meet AC, Move-Item→robocopy reunify = process Medium/Low (`pass_with_issues`), not fail-closed rework | `.cursor/agents/auditor.md` |
| P5 | skill bootstrap | SKILL/handoff lack lock-recovery cue | Thin pointer in implementer handoff + SI focus line | `handoff-templates.md`, optionally `SKILL.md` |
| P6 | docs (deferred) | Inventory size-band / LastWrite drift after moves | Optional later docs-only touch — not workflow machinery | `catalogue/inventory.md` (product; defer) |

## Online best-practice notes

Checked recent Cursor agent/skill guidance (2026):

- **[Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)** — Prefer plans + approval before irreversible work (matches our plan gate); keep Rules for always-on invariants and Skills for on-demand workflows; start fresh conversations per logical unit (one FAW session per cycle). **Adopted:** keep lock-recovery and remaining-row Continuity in agents/skill (dynamic when FAW runs), not a new product agent.
- **[Skills / Rules / Agents split](https://sbstjn.com/blog/cursor-skills-rules-agents-best-practices/)** — Skills load when description matches; agents orchestrate without duplicating skill bodies. **Adopted:** thin Continuity bullets in role agents + handoff cue; avoid bloating orchestrator with move recipes.
- **Focused Continuity packs** (prior cycles + forum Rules vs Skills) — Short, named packs beat re-asking full history. **Adopted:** explicit Multi-experiment **remaining** pack (mirror Medium remaining).

Not adopted: new subagent for FS moves (overkill); dumping “user close IDE locks” as recurring chore (encode agent recovery instead).
