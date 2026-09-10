# Realization & process audit

## Good points

- **Root cause with live evidence:** Researcher proved agent Shell used MSYS git (`C:\msys64\usr\bin\git.exe`) with no `credential.helper`, while Git for Windows + GCM (`manager`) succeeded on fill and `push --dry-run` — not “missing credentials” and not solely missing `gh` (`02-research/research-brief.md`).
- **Option A scope discipline:** Plan stayed docs-only (agents/skill/rules/templates/`AGENTS.md`); skipped optional helper script; no secrets; no PATH rewrite (`03-plan/plan.md`, `04-implementation/changes.md`).
- **Consistent surface:** Dual preflight, GfW preference, `agent_environment` vs `user_credentials`, fail-closed, and `gh`≠sole signal land in implementer/researcher/planner/orchestrator/auditor + skill Critical + rules + handoffs + templates (`04-implementation/changes.md`, auditor spot-check).
- **Fail-closed honesty preserved:** Session/process still requires `blocked` + self-improver when push cannot proceed; auditor verified smoke without false `complete`.
- **Audit quality:** PASS with criteria mapped to refined prompt and plan; re-ran GfW dry-run; flagged only Low housekeeping (uncommitted tooling, empty SESSION fields, pre-seeded 06 stubs) (`05-audit/report.md`).

## Bad points

- **User-facing discoverability gap:** `README.md` Quick start / Architecture never mentions Windows HTTPS push, GfW vs MSYS, or where to look (`AGENTS.md` has the law; humans opening README miss it).
- **prompt-betterment silent on publish:** Phase 1 does not prompt for push/auth / agent-vs-user Shell when the goal involves remote publish — that ambiguity delayed correct framing until research (prior 0831 misclassified toward credentials/`gh`).
- **Optional PATH tip absent:** Docs correctly prefer absolute GfW `git.exe`, but neither README nor portable law notes the optional user tip (put GfW `cmd` before MSYS on PATH) for interactive shells and default `git`.
- **06 stubs before self-improver:** Bootstrap seeds empty `06-self-improvement/*` while checklist shows 06 pending — auditor Low finding; easy to misread as “self-improvement done” (`05-audit/report.md`).
- **SESSION.md lag:** Audit/self-improvement fields still empty at audit time; orchestrator bookkeeping unfinished until phase 06/close (`SESSION.md`, audit Recommended next actions).
- **Tooling uncommitted:** Expected per plan; residual process risk that Option A docs exist only locally until user requests commit + GfW push.

## Evidence

| Claim | Pointer |
| --- | --- |
| MSYS vs GfW root cause | `02-research/research-brief.md` Required facts + dual preflight table |
| Option A applied (12 paths) | `04-implementation/changes.md` |
| Smoke pass | `04-implementation/log.md`; `05-audit/report.md` Push / Option A checklist |
| Audit PASS / no rework | `05-audit/report.md` Verdict |
| README silent on push | repo `README.md` (Quick start ends at session folders) |
| prompt-betterment no push Qs | `.cursor/agents/prompt-betterment.md` Process §2 |
| Pre-seeded empty 06 | `06-self-improvement/*` stubs at audit; `05-audit/report.md` Severity Low |
