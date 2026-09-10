# Realization & process audit

Session `2026.09.09-1332` — organisation-repo **git pull** FAW. Outcome: **`blocked`** / `aborted_dirty` (pull **not** run). Audit verdict: **pass** (process). Sync AC unmet by design (Q3=A). Do **not** claim pull succeeded.

## Good points

- **Prompt pack + Choose discipline:** Q1–Q7 locked via Choose→all A with informed-consent wording; notes record no jargon-explanation debt (`01-prompt-betterment/notes.md`).
- **Research honesty:** Dual preflight separated auth (GfW+GCM green) from dirty readiness; MSYS vs GfW porcelain skew (104 vs 15) documented; Option A recommended (`02-research/research-brief.md`).
- **Plan AC quality:** Explicit `blocker_type` **`dirty_working_tree`**, GfW-only gate/pull, fail-closed, zero-move, taxonomy/must-preserve out of scope (`03-plan/plan.md`).
- **Implementer fail-closed:** Org-root lock; GfW dual preflight; dirty abort listed 15 paths; no pull/fetch/stash/merge/rebase; recommended SESSION `blocked`; secrets boolean-only (`04-implementation/log.md`).
- **Auditor framing:** Process **pass** + unmet pull-success AC + `rework_owner: user` (clean/stash) — never false `complete`; SI still mandatory (`05-audit/report.md`).

## Bad points

- **SESSION bookkeeping lag (Low):** At audit time `SESSION.md` still showed `in_progress` / phase 04 lag while implementer already recommended `blocked` — orchestrator should flip status when implementer returns `blocked` / `aborted_dirty`, not only at close (`05-audit/report.md` vs `04-implementation/log.md`).
- **No standing pull question pack:** Prompt-betterment invented an ad-hoc pack and flagged “add pull-cycle.md” as SI backlog (`01-prompt-betterment/notes.md`); publish already has `publish-cycle.md` — asymmetry.
- **Blocker taxonomy incomplete in agents/rules:** Cycle correctly used `dirty_working_tree`, but `implementer.md` / orchestrator / skill / AGENTS only listed `agent_environment` vs `user_credentials` for git blockers — risk of mis-typing dirty abort as auth/env.
- **Pull ≠ push in handoffs:** Handoff templates and auditor checklists were push-centric; pull GfW/dirty-abort path had to be re-derived from research/plan each time.
- **Stale remote cache note:** Without fetch while dirty (correct), local `origin/main` stayed at `f5012d6` while research remote tip was `489f03a` — easy to overclaim sync if status bookkeeping is sloppy (implementer logged it; keep as standing pitfall).

## Evidence

| Claim | Path |
| --- | --- |
| Choose→all A; no jargon debt; pull-cycle backlog | `01-prompt-betterment/notes.md` |
| Dirty 15 / auth green / remote `489f03a` | `02-research/research-brief.md` |
| `dirty_working_tree` AC + GfW | `03-plan/plan.md` |
| `aborted_dirty`; pull not attempted; HEAD `f5012d6` | `04-implementation/log.md`, `04-implementation/changes.md` |
| pass process; unmet sync AC; bookkeeping Low | `05-audit/report.md` |
| Session status `blocked` (post-audit framing) | `SESSION.md` |
