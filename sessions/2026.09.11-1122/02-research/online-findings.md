# Online findings — Cycle 17

Short pass on late-cycle / session-artifact finalize (supporting mid + mandatory final git design). Prefer official Cursor guidance; agent-auto-commit patterns as secondary.

---

## Citations

### 1. Best practices for coding with agents (Cursor Blog)
- **URL:** https://cursor.com/blog/agent-best-practices
- **Takeaway:** Keep reusable workflows in **Skills**; put short always-on conventions in **Rules / AGENTS.md** and **check them into git**. Plan artifacts should be saved so later agents can resume — maps to committing session/process docs, not leaving them only on disk.

### 2. Cursor Hooks docs (`sessionEnd` / `stop` / `subagentStop`)
- **URL:** https://cursor.com/docs/hooks
- **Takeaway:** Lifecycle hooks (`sessionEnd`, `stop`, `subagentStop`) exist to run work at **end of agent/session**, including team-shared hooks committed under `.cursor/`. Supports the idea of a **closing** git pass after late phases, not only mid-cycle.

### 3. Cursor Skills docs (via Cursor agent best-practices ecosystem)
- **URL:** https://cursor.com/docs/skills (linked from Cursor best practices / skills guides)
- **Takeaway:** Version-controlled `SKILL.md` procedures should encode repeatable cycles end-to-end; a skill that stops before persisting audit/self-improve outputs is an incomplete procedure.

### 4. Per-task / end-of-work commit pattern (GSD executor example)
- **URL:** https://github.com/projeyoneti/proje.ai/blob/main/.cursor/agents/gsd-executor.md
- **Takeaway:** After verification, **commit immediately** and record the hash in the summary — prefer small scoped commits over leaving finished work unstaged. Analog for FAW: final closing commit after self-improver verification artifacts exist.

### 5. Retrospective + agent-memory commit (example PR)
- **URL:** https://github.com/jsturtevant/rally/pull/122
- **Takeaway:** Process retrospectives and agent history updates are treated as **first-class commit content** alongside code — same class as FAW `07-self-improvement/**` + agent/skill edits.

---

## Synthesis for Cycle 17 (keep short)

| Practice | Implication for FAW |
| --- | --- |
| Skills/rules in VCS | Mid-cycle push of product/docs is fine; **cycle-end** skill/agent/template edits must also land in git |
| End-of-session hooks / stop | Architectural precedent for a **mandatory closing** action after late phases |
| Small task-scoped commits | **Q1=A** mid (implementer) + final (06/07/SESSION/`.cursor`) beats one early commit that orphans late artifacts |
| Do not stage blindly | Keep allowlist + explicit paths (Cycle 16 already correct on secrets; wrong on labeling allowlist as unrelated) |

**Not adopted here:** External transcript-only session repos (ai-session) or every-turn autocommit (turbocommit) — heavier than Continuity Q1; FAW stays allowlisted dual-pass inside org-repo.
