# Realization & process audit — Cycle 17 (`2026.09.11-1122`)

## Good points

- **Continuity → STAGE 1 hold → Hermes → STAGE 2 resume same folder** worked as designed: Q1–Q3 locked, plan `docs_only` with intent-preview, same-run implement forbidden until Hermes YES, then resume `sessions/2026.09.11-1122/` (no parallel session).
- **Q2=A leftover finish-sync first** cleared Cycle 16 orphans (`caec66d`, exact 16 paths, `1122/` excluded; `0859/` + bare `2026.09.11/` deferred) before FAW amendment — closes the orphan-after-mid-push problem that motivated this cycle.
- **FAW dual-git law landed consistently** across skill, orchestrator, git-manager, handoffs, SESSION template, AGENTS, rules, and optional `05-git-log` template (implementer Grep + auditor AC).
- **Mid ≠ final:** mid pushed amendment + early session (`55b7341` / `353cb7e`) while correctly excluding `06-audit/**` and `07-self-improvement/**` for the final closing pass; session stayed `in_progress` (no false complete).
- **ROADMAP / WorkSpace honesty:** Multi-experiment not Complete; WorkSpace still at root; strategy artifact present; zero corpus moves / remote-config; taxonomy/must-preserve not upgraded (Q3a waive).
- **Auditor readonly contract honored on resume:** orchestrator persisted `06-audit/report.md` and flipped mid-cycle SESSION lag (phases 04–06) before launching self-improver.
- **User-workload:** Continuity Choose + Hermes gate used informed-consent framing; no recurring PATH chores dumped on the user; GfW absolute path + GCM in git logs.

## Bad points

- **SESSION mid-cycle lag (auditor Low):** During STAGE 2, Workflow progress advanced for implementer + mid git while **Phase checklist / Phase summaries** still showed 04–07 pending — bookkeeping debt between mid git and auditor. Root cause: skill + SESSION template + mid handoff said “Workflow + Phase checklist” but **omitted Phase summaries**, while `orchestrator.md` already required all three — inconsistent surfaces invite lag.
- **Final closing pass still pending at audit** — expected by design (SI → final), but this is the first live cycle under the amended law; gate must actually run after this SI (mid must not substitute).
- **07 bootstrap stubs** sat until this phase — expected bootstrap pattern; checklist correctly stayed unchecked until overwrite.
- **Auditor could not re-run Shell porcelain** (Ask-readonly) — Low/process; relied on log attestation + Read/Glob. Acceptable under existing fallback law; still a recurring verification soft spot.
- **WorkSpace deep Glob timeout** — Low; presence via `Test-Path` / Read OK; do not elevate to Critical.

## Evidence

| Claim | Pointer |
| --- | --- |
| Continuity locks + STAGE 1 hold | `01-prompt-betterment/refined-prompt.md`; `SESSION.md` Program framing |
| Plan dual-git + leftover-first + Hermes preview | `03-plan/plan.md` |
| FAW amendment surfaces | `04-implementation/changes.md`, `04-implementation/log.md` |
| Leftover `caec66d` + mid `55b7341`/`353cb7e`; final pending | `05-git/log.md` |
| Verdict `pass_with_issues`; SESSION lag Low; final pending expected | `06-audit/report.md` |
| Resume + audit persist + checklist flip before SI | `SESSION.md` Workflow progress / Phase checklist / Phase summaries (post-orchestrator flip) |
| WorkSpace / ROADMAP honesty | `04-implementation/log.md` zero-move; auditor guardrails; `program/ROADMAP.md` (auditor AC) |
