# Improvement proposals — Cycle 2

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | prompt-betterment | Clarifying questions assume jargon literacy | Mandate: every question = plain-language explanation of what is asked + what “yes” commits to + pros/cons (or tradeoffs) per option | `.cursor/agents/prompt-betterment.md` |
| P2 | orchestrator | Plan-gate / blocking asks relayed without explanation | When surfacing phase-1 questions or FS plan gates, always include short explanation + pros/cons; never paste jargon-only options | `.cursor/agents/orchestrator.md` |
| P3 | skill | Plan-gate step silent on consent UX | Document informed-consent requirement for clarifying Qs and plan gates (plain language + tradeoffs) | `.cursor/skills/full-agent-workflow/SKILL.md` |
| P4 | rules / AGENTS | Law lists gates but not how to ask | Add one line: clarifying questions and plan gates must include explanation + pros/cons for informed consent | `.cursor/rules/full-agent-workflow.mdc`, `AGENTS.md` |
| P5 | handoffs / templates | No reminder structure → easy to regress | Cue prompt-betterment + planner + self-improver; expand `01-notes` + SESSION note on explained gates | `handoff-templates.md`, `sessions/_templates/01-notes.md`, `SESSION.md` |
| P6 | planner | Plan gate section was good this cycle but not mandated | Require “What the user is approving” block with plain meaning + pros/cons for every `fs_mutation` plan | `.cursor/agents/planner.md` |
| P7 | catalogue hygiene | Inventory pattern §6 still lists all six Early/simple | Optional polish in a later docs/micro cycle — not workflow law | (product docs — defer) |
| P8–P13 | prior backlog | Carried from Cycle 0/1 | Keep deferred unless urgency rises | `backlog.md` |

## Online best-practice notes (adopted)

Short check on agentic **informed consent / decision UX** (2026):

1. **Intent preview / plan summary** — Before significant action, show a clear plain-language preview of what will happen; avoid jargon; make it a decision point with intentional friction for high-stakes work.  
   — [Smashing Magazine: Designing For Agentic AI (control, consent, accountability)](https://www.smashingmagazine.com/2026/02/designing-agentic-ai-practical-ux-patterns/)

2. **Bounded delegation in plain language** — Say what authority is granted for this request only; make reversibility / risk explicit before irreversible steps.  
   — [ACM Interactions: When Systems Act for Users](https://interactions.acm.org/archive/view/september-october-2026/when-systems-act-for-users)

3. **Action preview + irreversibility / batch approval patterns** — Consent should be specific, scoped, and reviewable (approve / edit / refuse), not a jargon checkbox.  
   — [agent-consent-patterns (Action Preview, Irreversibility Gate, Batch Approval)](https://github.com/mrchaarlie/agent-consent-patterns)

4. **Plain language at the moment of choice** — Tell users what they need to know when they need to know it, without needing a dictionary.  
   — Privacy-led UX / TRUST “Translate” framing (Usercentrics, AI-era consent) — PDF: https://usercentrics.com/wp-content/uploads/2026/04/Privacy-Led-UX-in-the-AI-Era.pdf

**Adopted into this cycle’s workflow law:** every clarifying question and every orchestrator-relayed plan gate must ship with (a) plain-language explanation + what yes commits to, and (b) pros/cons or tradeoffs — matching Intent Preview + bounded batch approval. Do **not** assume the user already knows FAW/taxonomy jargon.

## Apply now vs defer

- **Apply now:** P1–P6 (workflow law + agent/skill/template cues).
- **Defer:** P7 (catalogue polish), prior P8–P13 (unchanged urgency).
