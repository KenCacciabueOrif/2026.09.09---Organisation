# Improvement proposals — Cycle 20

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | planner / orchestrator | Clearance #4 “written” vs “approved” not in workflow law — next cycle may treat DRAFT or docs gate as nest-move authority | Encode #4 split: **DRAFT written** = `docs_only` surgery artifact; **approved** = later dedicated nest `path_batch` plan gate. Docs gate **yes** ≠ nest-move approval; #4 draft ≠ whole-tree clearance **yes** | `.cursor/agents/planner.md`, `orchestrator.md` |
| P2 | researcher / prompt-betterment | Post–OS-IA Continuity X pack still OS-IA-first oriented; surgery artifact + ignored-nest model under-specified | Point Continuity X post–OS-IA / TNA at `program/git-strategy-tna-parent-surgery.md` + hazards #4; classify nests as **ignored nested clones** (not submodules); default next material advance = continue #4 clearance / keep-at-root | `.cursor/agents/researcher.md`, `prompt-betterment.md` |
| P3 | implementer / auditor | Risk of nest extract under docs-only surgery cycle or claiming #4 approved after DRAFT | Docs-only surgery: zero nest/TNA moves; attest #4 **DRAFT written / approval pending** only. Nest extract only after #4 **approved** + dedicated `fs_mutation` gate. Auditor checklist for surgery md + #4 status + non-Complete | `.cursor/agents/implementer.md`, `auditor.md` |
| P4 | skill / rules / AGENTS | Portable law missing post–Cycle-20 surgery Continuity | One-line: after surgery DRAFT, Next FAW = WorkSpace only / TNA + continue Continuity X; nest extract only after #4 approved + dedicated gate | `SKILL.md`, `handoff-templates.md`, `full-agent-workflow.mdc`, `AGENTS.md` |
| P5 | session template | Strategy artifact field lists hazards only | Add optional surgery-policy pointer + #4 written/approved status | `sessions/_templates/SESSION.md` |
| P6 | orchestrator bookkeeping | Phase checklist lags Workflow mid (audit Low) | Defer — already noted in prior SI; reinforce only if cheap in handoff (no new user chore) | backlog |

## Online best-practice notes

- **Keep subagents narrow; encode durable law in skills/rules** — Cursor docs: invest in focused agent descriptions; put repeatable multi-phase pipelines in Skills so context stays clean ([Subagents](https://cursor.com/docs/subagents.md), [Agent best practices](https://cursor.com/blog/agent-best-practices)). Adopted: encode #4 written/approved + surgery-artifact Continuity in agents + skill/rule rather than relying on chat memory.
- **Skills for dynamic workflow; Rules for always-on law** — same blog: Rules = static every-turn; Skills = on-demand. Adopted: short alwaysApply line in `full-agent-workflow.mdc` + deeper bullets in agents/skill.
- **Orchestrator delegates; does not implement product goal** — forum guidance on root agent + specialized subagents ([forum thread](https://forum.cursor.com/t/workflow-long-running-multi-agent-orchestration-root-agent-parallel-sub-agents-separate-prs/160563)). Adopted: SI touches workflow agents only, not corpus FS.
