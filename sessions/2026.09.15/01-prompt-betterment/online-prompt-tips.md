# Online prompt tips — Cycle 18 (WorkSpace anti-loop / STAGE 1)

Actionable tips for refining Continuity + STAGE 1 plan briefs when a multi-cycle program risks **docs-only re-probe loops**.

| # | Tip | Why it helps here | Source |
| --- | --- | --- | --- |
| 1 | **Plan before irreversible work; approve a named path** | STAGE 1 stops after planner; any later `fs_mutation` needs a separate plan gate — Continuity ≠ execute. | [Cursor Plan Mode](https://cursor.com/docs/agent/plan-mode), [Introducing Plan Mode](https://cursor.com/blog/plan-mode) |
| 2 | **Write verifiable acceptance criteria and non-goals** | “Next reorg” is too vague; AC must say WorkSpace-only, no Complete while XL remains, no whole-tree archive by default, STAGE 1 stop. | [Cursor agent best practices](https://cursor.com/blog/agent-best-practices), [OTF: plan, scope, verify](https://otf-kit.dev/blog/cursor-agent-best-practices) |
| 3 | **Define explicit stop / escalate terminal states** | Anti-loop: if research would only restate Cycle 16 “no material delta”, stop and escalate options to the human — do not iterate Continuity A theater. | [Clear stop conditions](https://newprompt.net/guides/give-an-ai-agent-clear-stop-conditions), [No-progress guard](https://viralruparel.com/blog/agent-loop-no-progress-detection-guard) |
| 4 | **Treat irreversible actions as structural gates** | Scoped moves / remote-config need orchestration plan-gate + intent-preview; agent “self-approval” is not enough. | [Human-in-the-loop approval gates](https://www.openlegion.ai/en/learn/human-in-the-loop-ai-agents) |
| 5 | **Detect stagnant domain state, not busy transcripts** | Another polished attestation with the same clearance **NO** is a loop even if wording changes — require material delta or escalate. | [LoopGuard](https://github.com/mahimathacker/loopguard), [No-progress guard](https://viralruparel.com/blog/agent-loop-no-progress-detection-guard) |
| 6 | **Keep context bounded; point at durable artifacts** | Prefer `program/git-strategy-workspace-hazards.md` + prior session paths over re-dumping Cycles 9–16 narrative. | [Cursor agent best practices](https://cursor.com/blog/agent-best-practices) |
| 7 | **Ask clarifying questions only when the answer changes safety or outcome** | Carry taxonomy/must-preserve + dirty-hygiene Continuity; the one blocking ask is advance vs break-the-cycle under anti-loop. | [Plan Mode](https://cursor.com/docs/agent/plan-mode), [Agent prompt engineering 2026](https://www.inflectra.com/Ideas/Topic/AI-Agent-Prompt-Engineering.aspx) |

## Domain note (this cycle)

Post–Appendix A (Cycle 14) and post–multi-remote clear (Cycle 15), residual blockers are **whole-tree / XL** (classified ≠ cleared). Continuity **A** `docs_only` re-probe already ran as Cycle 16 with **no material delta**. Standing anti-loop forbids repeating that theater by default.
