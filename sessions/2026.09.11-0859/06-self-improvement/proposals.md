# Improvement proposals

**Session:** `sessions/2026.09.11-0859/`  
**Priority lens:** encode Cycle 15 lessons; diminish user re-asks; keep fail-closed for unrelated / non-allowlist; **do not** mark Multi-experiment Complete.

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | planner / skill / templates | `fs_mutation` reads as path-only; `git remote remove` risked being misclassed | Add **remote-config** mutation kind (gated; zero path moves; still plan gate; exact command map) | `planner.md`, `SKILL.md`, `03-plan.md` template, `handoff-templates.md` |
| P2 | orchestrator / AGENTS / rules | Plan gate text says moves/renames/deletes only | Explicitly include remote-config / nested `.git` remote edits as gated `fs_mutation` | `orchestrator.md`, `AGENTS.md`, `full-agent-workflow.mdc` |
| P3 | prompt-betterment | After Appendix A + stop docs_only, pack can re-default to docs continue-strategy | **Advance mandate:** when stop docs_only / remaining live hazard named, prefer narrow remote-config (or other scoped) `fs_mutation` over re-attest; after multi-remote clear still WorkSpace only | `prompt-betterment.md`, `orchestrator.md` |
| P4 | implementer / auditor | Remote-config execute + nested dirt + verify remotes underspecified | Implementer: execute only approved remote command; disclose nested+parent dirt `NO_AUTO_COMMIT`; Auditor: remote-config checklist + Read of `.git/config` when Shell blocked | `implementer.md`, `auditor.md`, handoffs |
| P5 | researcher | Multi-remote remediation could dump “user fix remotes” | Recommend evidence-backed gated Option A (remove wrong remote) as agent-owned plan candidate | `researcher.md` |
| P6 | self-improver handoff | Focus list missing remote-config / post–multi-remote clear | Extend focus bullets for next cycles | `handoff-templates.md` |
| P7 | deferred | Historical Cycle 10–13 blocks in hazards.md confuse readers | Optional one-line “history; live table authoritative” banner — product doc, low urgency | `program/git-strategy-workspace-hazards.md` (defer — product/strategy doc) |
| P8 | deferred | Auditor Shell sandbox still blocks porcelain | Broader agent-mode Shell for audit probes — harness/policy, not FAW text alone | backlog |

## Apply this cycle

**P1–P6** (small diffs). Defer **P7–P8**.

## Online best-practice notes

- **File blackboard + orchestrator-owned global state** — subagents write phase folders; orchestrator persists/accepts (matches auditor readonly → orchestrator write). [orchestration-playbook](https://github.com/p3nchan/orchestration-playbook)
- **STAGE / HITL gates between phases** — human escalation for side effects (remote remove) is a feature; Continuity ≠ execute. [HITL / forum orchestration](https://forum.cursor.com/t/multi-agent-orchestration-in-cursor-coordinating-specialized-agents/150022)
- **Skills for procedures, rules for always-on law; phase verification before proceed** — keep remote-config procedure in skill/agents, not chat memory. [Learn Cursor skills](https://www.learncursor.dev/learn/cursor-agents/cursor-agent-skills); [multi-agent workflows forum](https://forum.cursor.com/t/how-i-set-up-multi-agent-workflows-in-cursor-with-reusable-skills-and-agents/166742)
- **Structured partial results on capability gaps** (Shell unavailable → Read/Glob + Low) — coordinator salvages rather than fail-storm. [Multi agent error handling](https://aiskillcerts.com/concepts/agentic-architecture/multi-agent-error-handling-and-routing)

**Adopted now:** remote-config as first-class gated mutation; post–multi-remote WorkSpace-only lock; advance mandate vs docs theater; Shell→Read Low; orchestrator persist audit.
