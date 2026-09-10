# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | README / discoverability | Humans miss Windows push/GCM guidance | Add short “Windows git push” note: agent prefers GfW absolute path; optional PATH tip; point to `AGENTS.md` | `README.md` |
| P2 | prompt-betterment | Publish goals skip agent-vs-user Shell / auth clarifying Qs | When goal mentions push/publish/PR remote: ask whether agent Shell must push, and note Windows MSYS vs GfW if known | `.cursor/agents/prompt-betterment.md` |
| P3 | AGENTS.md | Optional PATH tip only implied | One sentence: optional put GfW `cmd` before MSYS on PATH; agents still use absolute GfW when needed | `AGENTS.md` |
| P4 | session-structure | Empty 06 stubs look like finished self-improvement | Note: bootstrap may seed empty 06 templates; self-improver **must overwrite**; checklist 06 stays unchecked until then | `session-structure.md` |
| P5 | Dedup | Option A text repeated across many agents | Extract single `references/windows-git-push.md` and link from skill/agents | skill references + agents |
| P6 | Tooling | Optional `resolve-git-for-push.ps1` skipped | Add helper if absolute-path discipline fails in practice | `scripts/` + implementer |
| P7 | Orchestrator | SESSION audit fields lag until close | Explicit post-audit checklist: fill verdict before launching self-improver | `orchestrator.md` |

**Apply now (high value, low risk):** P1–P4.  
**Defer:** P5–P7 (larger refactor / unproven need / bookkeeping already implied).

## Online best-practice notes

- **Focused subagents + concise prompts; invest in `description`; check agents into VCS** — [Cursor Subagents](https://cursor.com/docs/subagents.md). Adopted: keep residual edits small; do not bloat every agent with full Option A again (README + prompt-betterment only).
- **Skills hold procedural truth; agents orchestrate; keep always-on rules thin** — [sbstjn: Skills, Rules, Agents](https://sbstjn.com/blog/cursor-skills-rules-agents-best-practices/), [philliant: efficient .cursor](https://philliant.com/posts/20260716-efficient-cursor-directory-for-token-efficiency/). Adopted: leave Option A Critical section in skill as canonical; README points to `AGENTS.md` rather than duplicating the full checklist.
- **Don’t duplicate skill checklists into every worker** — [philliant: parallel subagents](https://philliant.com/posts/20260808-parallel-subagents-when-to-use-them-vs-skills/). Deferred as P5 (single reference file) — isolation still justifies short per-agent push bullets for now.
