# Improvement proposals — session `2026.09.09-1554`

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | orchestrator handoffs | Next “next cycle” could re-soft-defer or re-scan all Medium names | Soft-deferred-only remaining → lock **named remaining pair**; treat row as **nearly complete**; after last move → Complete → Primary next | `.cursor/agents/orchestrator.md`, `SKILL.md`, `handoff-templates.md` |
| P2 | phase agent prompts (PB) | Remaining-subset cue still offers soft-defer-again as normal ask | **Soft-deferred finalization Continuity:** default = finalize remaining this cycle; do not re-ask soft-defer as default A; carry layout/git/env/taxonomy Continuity; short pack (both vs one; status/SSH awareness) | `.cursor/agents/prompt-betterment.md`, `sessions/_templates/01-notes.md` |
| P3 | planner | Finalization map must include paused vs archive + SSH opaque without inventing git-strategy | Soft-deferred finalization plans: default both remaining; 90d → paused for CursorMobile; SSH remotes stay as-is; ROADMAP Complete only when last names done | `.cursor/agents/planner.md` |
| P4 | rules / AGENTS | Always-on law lacks soft-deferred finalization one-liner | Thin Continuity line: soft-deferred-only remaining → same row / finalize remaining (not re-defer by default) | `.cursor/rules/full-agent-workflow.mdc`, `AGENTS.md` |
| P5 | verification | ROADMAP already updated — verify only | Confirm Notes + How-next match INDEX remaining two; no false Complete | `program/ROADMAP.md` (verify; tweak only if drift) |
| P6 | deferred | Org porcelain / EOL churn | Leave to publish-cycle hygiene; not Cycle 5 AC | backlog |

## Online best-practice notes

- **Focused subagents + concise prompts** — Cursor docs: one responsibility per agent; avoid rambling Continuity dumps; encode new case as a short named pack. Adopted as P1–P2 (finalization Continuity bullet, not a new agent). — https://cursor.com/docs/subagents.md
- **Skills for repeatable workflow; progressive disclosure** — Keep SKILL bootstrap thin; push detail to agents/references. Adopted as P1 skill one-liner + handoff cue. — https://cursor.com/docs/skills
- **Agent Skills / agentskills.io** — One skill one job; descriptions as trigger conditions. No new skill folder (FAW already owns this); reinforce Continuity in existing FAW skill. — https://meshlaunch.com/en/blog/2026-cursor-agent-skills-complete-guide.html

## Apply now vs defer

- **Now:** P1–P5 (verify ROADMAP; implement Continuity law).
- **Defer:** P6.
