# Improvement proposals — Cycle 14

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | prompt-betterment / orchestrator | After repeated docs_only re-attests, defaults can still drift toward Continuity A unless handoff is perfect | When user names **Continuity B** / Appendix A execute / “stop docs_only re-attest”, **lock Q1=B** (`fs_mutation`); **forbid** docs_only as this cycle’s path; do not re-offer A/C as defaults | `.cursor/agents/prompt-betterment.md`, `orchestrator.md`, skill/handoff, rules, `AGENTS.md` |
| P2 | planner / implementer / hazards | `git worktree list` on parent `_backups`/`_quarantine` resolves to outer TNA — false linked-worktree signal | Encode rule 5: probe **nested clone paths** only; never treat parent-dir worktree list as nested-clone probe | `program/git-strategy-workspace-hazards.md`, `implementer.md`, `planner.md`, handoff |
| P3 | orchestrator / skill | STAGE 1 hold + STAGE 2 resume lived in raw goal only | Encode: `fs_mutation` STAGE 1 = stop at plan gate; after gate yes (+ amendments) **resume same session** for implement→audit→self-improve | `orchestrator.md`, `SKILL.md`, `SESSION.md` template |
| P4 | implementer / planner | Parent-repo dirty WT after removing tracked nested paths — risk of auto-commit | Standing law: disclose dirt; **`NO_AUTO_COMMIT`**; reverse-move notes per successful parent move | `implementer.md`, `planner.md`, handoff |
| P5 | orchestrator / ROADMAP lock | Post–Appendix A could be misread as Multi-experiment Complete | Explicit: after scoped isolation, still lock **WorkSpace only**; never Complete while WorkSpace / live multi-remote remain | `orchestrator.md`, handoff self-improver focus |
| P6 | auditor persist | Already fixed Cycle 13; reaffirm only | No new change unless drift | (verify only) |

## Online best-practice notes

- **Subagents vs skills:** Use subagents for context isolation and independent verification; keep skills for repeatable how-to — FAW already matches (orchestrator + phase agents + skill). Adopt: keep handoffs structured and single-responsibility. — https://cursor.com/docs/subagents
- **Orchestrator + specialists:** Parent coordinates; specialists stay scoped; verifier independent — reinforces auditor readonly + orchestrator persist of `05-audit/report.md`. — https://cheesecakelabs.com/blog/skills-and-subagents/
- **Project skills in `.cursor/skills/`:** Version workflow with the repo — continue encoding Continuity/STAGE defaults in skill + agents, not chat memory. — https://www.learncursor.dev/learn/cursor-agents/cursor-agent-skills

**Adopted this cycle:** Strengthen Continuity B / STAGE 1→2 / nested-clone worktree probe in agents+skill (P1–P4); keep auditor readonly→orchestrator persist (already aligned with docs).
