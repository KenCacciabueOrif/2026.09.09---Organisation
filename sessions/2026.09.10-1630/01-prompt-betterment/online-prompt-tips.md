# Online prompt tips — Cycle 13 (WorkSpace continue-strategy / docs_only)

Actionable prompting practices relevant to Continuity-locked, docs-only, plan-then-maybe-implement agent cycles.

1. **Clarify before building; separate plan from execute**  
   Cursor agent best practice: research → clarifying questions → detailed plan with paths → wait for approval before irreversible work. For this cycle, Continuity locks path (`docs_only`) but still does **not** replace a plan gate if any future `fs_mutation` appears.  
   Source: https://cursor.com/blog/agent-best-practices

2. **Treat Plan Mode as reviewable scope, not a soft hint**  
   Plan Mode is meant to produce an editable Markdown plan before build. When staging is “phases 1–3 first,” encode that boundary in AC so later phases only auto-continue when `docs_only` + `ready_to_implement: yes` — never treat Continuity as silent build approval for corpus moves.  
   Source: https://cursor.com/docs/agent/plan-mode

3. **Name must-haves and must-nots in acceptance criteria**  
   Agent AC should state what must remain untouched (zero corpus moves, no Complete while WorkSpace remains, no peer reopen) as part of “done,” not only positive deliverables.  
   Source: https://fondsites.com/ai-agents/guidebooks/agent-acceptance-criteria/

4. **Grill for decision-relevant ambiguity only; lock reversible defaults**  
   Ask only when the answer changes scope/risk. Prefer documented defaults for reversible docs paths; do not invent irreversible FS defaults. User already named “continue strategy” → lock Q1=A without a blocking round-trip.  
   Source: https://dev.to/cherware/the-grilling-pattern-clarify-requirements-before-they-become-code-3e4e

5. **Offer 2–3 concrete options with pros/cons + recommended default**  
   Clarification packs should present options, impact, and a recommended choice — then record Source (`yes→defaults` / unanswered→default) so downstream agents never inherit “Choose.”  
   Source: https://github.com/Smithbox-ai/ControlFlow/blob/master/docs/agent-engineering/CLARIFICATION-POLICY.md

6. **Be specific in the refined prompt**  
   Prefer concrete pointers (artifact path, corpus candidate, mutation class, stage rules) over vague “organise next.” Specificity raises success rate for multi-phase agents.  
   Source: https://cursor.com/blog/agent-best-practices

7. **Pin docs_only / no-build boundaries in durable project law when stages matter**  
   Soft mode hints can drift; encode STAGE 1 vs auto-continue-on-docs_only in the refined prompt AC so orchestrator/implementer cannot “helpfully” mutate corpus without Continuity B + plan gate.  
   Source: https://forum.cursor.com/t/plan-mode-is-not-respected-by-the-agent/151802 (mode-boundary hardening pattern)
