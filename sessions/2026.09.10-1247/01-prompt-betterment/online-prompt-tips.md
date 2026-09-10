# Online prompt tips — Cycle 12 (WorkSpace-only / continue strategy)

Relevant to multi-cycle agent briefs with Continuity defaults, docs-only vs mutation gates, and verifiable acceptance criteria.

## Actionable tips (3–7)

1. **Clarify before acting; lock reversible defaults without blocking** — Ask a short Continuity pack with plain-language options, then apply disclosed defaults when the user only says “next” and the default is reversible (`docs_only`). Do not wait for chat if irreversible FS mutation is not the default.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

2. **Separate Continuity from plan-gate approval** — Continuity chooses *path* (continue strategy vs Appendix A Continuity). A later **plan gate** is the only yes that may authorize a concrete from→to map. Encode that split in the refined prompt so later phases cannot conflate them.  
   Source: [Cursor Plan Mode docs](https://cursor.com/docs/agent/plan-mode)

3. **Scope the allowed change set** — Name which files/artifacts may change (`program/git-strategy-workspace-hazards.md`, INDEX, ROADMAP, session docs) and which must not (corpus moves; archived peers). Too much unrelated context increases wrong-path risk.  
   Source: [OTF — Cursor agent best practices](https://otf-kit.dev/blog/cursor-agent-best-practices)

4. **Make acceptance criteria pass/fail and auditor-checkable** — Each AC should be independently verifiable from session artifacts (zero moves? row still in progress? strategy anchored?). Avoid prose-only “done”.  
   Sources: [Scrum Alliance — Acceptance criteria](https://resources.scrumalliance.org/Article/need-know-acceptance-criteria); [Atlassian — Acceptance criteria](https://www.atlassian.com/work-management/project-management/acceptance-criteria)

5. **Prefer specific stopping conditions over vague “solve hazards”** — “Continue strategy: re-probe vs durable artifact; refine honesty; classified ≠ cleared; no whole-tree archive” beats “fix WorkSpace”.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

6. **Informed consent on every option set** — For each Continuity choice, state what yes commits to and tradeoffs (pros/cons). Define gate jargon in one sentence when used (`docs_only`, `fs_mutation`, plan gate, fail-closed).  
   Source: project FAW law + ClarifyGPT-style ask-before-act evidence summarized in [conversational specs / clarifying questions](https://levelup.gitconnected.com/ai-assisted-spec-writing-conversational-specs-5-techniques-and-spec-hallucination-sdd-a497a43b0d48)

7. **Fail-closed behavioral invariants** — Treat “never Complete while WorkSpace remains”, “never silent whole-tree archive”, and “Continuity ≠ execute Appendix A” as hard invariants in AC, not soft preferences.  
   Related verification framing: [agentverify](https://github.com/simukappu/agentverify) (assert tool/safety boundaries); [AgentProbe](https://github.com/NeuZhou/agentprobe) (behavioral contracts)

## Continuity pack (short — post–strategy WorkSpace-only) — for user relay

**Q1 — Path?** A = continue strategy from `program/git-strategy-workspace-hazards.md` (`docs_only`; default). B = Continuity to prepare/execute Appendix A scoped `_backups`/`_quarantine` isolation (still needs separate plan gate). C = pure research+defer no-op.  
**Q2 — Carry Continuity?** A = yes (default). B = change (must name what).  
**Q3 — Taxonomy/must-preserve?** A = waive re-litigation this cycle (default). B = pause for sign-off now.

**This cycle locked:** Q1–Q3 = **A** via `Choose (unanswered→default)` (“next reorganisation cycle”; Appendix A not named). Override next cycle if you want B.
