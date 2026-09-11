# Online prompt tips

Actionable tips for this Continuity / gated-strategy cycle (WorkSpace-only, post–multi-remote). Sources accessed 2026-09-11.

1. **Plan before irreversible work** — For multi-path / high-risk work, research + clarifying questions + a reviewable plan first; approve before build. Maps to FAW STAGE 1 (phases 1–3) then plan gate for any `fs_mutation`.  
   Source: https://cursor.com/docs/agent/plan-mode · https://cursor.com/blog/plan-mode

2. **Specific goal + constraints + verification** — State outcome, what must not happen, and how success is checked (paths, statuses, docs diffs)—not vague “organise WorkSpace.”  
   Source: https://cursor.com/blog/agent-best-practices · https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts

3. **Observable, atomic, bounded acceptance criteria** — Each AC should be pass/fail with one clear evidence artifact (e.g. “hazard doc section updated”; “ROADMAP still WorkSpace-only”; “zero corpus path moves”).  
   Source: https://tekk.coach/spec-driven-development/acceptance-criteria-agents-can-actually-execute/ · https://www.braingrid.ai/blog/how-to-write-acceptance-criteria-ai-agent-can-verify

4. **Explicit Not Included / Never** — Agents expand scope when boundaries are missing; forbid whole-tree archive, re-clearing cleared remotes, Complete/Primary-next jumps unless evidence regresses.  
   Source: https://www.augmentcode.com/guides/ai-spec-template · https://www.inflectra.com/Ideas/Topic/AI-Agent-Prompt-Engineering.aspx

5. **Clarify Ambiguous / Ask First vs Never** — Distinguish Always (docs honesty), Ask First (scoped `fs_mutation` / remote-config), Never (invent whole-tree archive; force-move XL WorkSpace). Continuity Choose ≠ plan-gate execute.  
   Source: https://www.inflectra.com/Ideas/Topic/AI-Agent-Prompt-Engineering.aspx · https://blogs.oracle.com/fusioncoe/best-practices-for-prompts-in-ai-agent-studio

6. **Revert + refine plan over compounding fixes** — If a gated mutation goes wrong, stop and refine the plan rather than stacking corrective prompts.  
   Source: https://cursor.com/learn/creating-features · https://prod.cursor.com/docs/agent/plan-mode

7. **Point at durable context files** — Prefer `@` / path pointers (`program/git-strategy-workspace-hazards.md`, prior session, ROADMAP) over pasting long histories into the refined prompt.  
   Source: https://cursor.com/blog/agent-best-practices · https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts

8. **Docs-only continue-strategy AC** — When mutation class is `docs_only`, require pass/fail evidence of a **material honesty delta** (updated section, cleared/regressed probe result) **or** an explicit “no material delta” attestation — never silent Complete / theater re-attest.  
   Source: https://tekk.coach/spec-driven-development/acceptance-criteria-agents-can-actually-execute/ · https://www.braingrid.ai/blog/how-to-write-acceptance-criteria-ai-agent-can-verify
