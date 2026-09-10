# Online prompt tips — Cycle 6 Medium wrappers (soft-deferred finalization)

Actionable tips for this goal type (finalization batch + plan-gated FS moves). Sources accessed 2026-09-09.

1. **Plan first, approve before mutation** — Research → written plan with paths → wait for approval before any move. Continuity / Choose / starting FAW is not move approval.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

2. **Binary acceptance criteria up front** — Define checkable pass/fail conditions (sources gone, targets present, nested `.git` intact, INDEX current path) before implementer runs; do not invent the bar after the fact.  
   Source: [The Augmented Work — How to verify AI agent work](https://theaugmented.work/articles/how-to-verify-ai-agent-work)

3. **Tight scope + explicit out-of-scope** — Name only the two remaining folders; forbid re-proposing Cycle 4/5 archives; state what “done” means for the ROADMAP row.  
   Source: [OTF — Cursor agent best practices](https://otf-kit.dev/blog/cursor-agent-best-practices)

4. **Constraints beat improvisation** — Lead with must-nots: opaque `.env` (never read), atomic nested git, fail-closed on worktree/SSH/multi-remote, no history rewrite.  
   Source: [Easton — Cursor Prompts: Context, Constraints, and Acceptance Criteria](https://eastondev.com/blog/en/posts/dev/20260129-cursor-prompt-engineering/)

5. **Evidence over self-report** — Require implementation log with `from → to` + reverse-move notes and auditor-checkable disk/INDEX facts, not “moves succeeded” prose.  
   Source: [OTF — Cursor prompts that keep agent sessions focused](https://otf-kit.dev/blog/cursor-prompts-agent-sessions)

6. **Fail-closed + rollback readiness** — On hazard, skip/defer that item with a logged reason; keep reverse-move notes so Critical audit can roll back without guessing.  
   Source: [AIWG storage migration protocol](https://unpkg.com/aiwg@2026.9.5/docs/storage/migration-protocol.md) (approval binding + fail-closed receipts pattern)

7. **Mark Continuity vs open decisions** — Separate already-locked rules (layout, taxonomy Continuity) from this cycle’s finalize-scope ask so later phases do not re-litigate.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices) (clarify requirements; reference canonical files)
