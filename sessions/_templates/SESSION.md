# Session

- **Date folder:** `yyyy.mm.dd` (or `yyyy.mm.dd-HHMM` on collision)
- **Status:** `in_progress` | `blocked` | `complete`
- **Blocker (if blocked):** `dirty_working_tree` | `agent_environment` | `user_credentials` | `other` (e.g. non-ff / merge_conflict) | … (or n/a)
- **Raw goal:**
- **Resume:** no | yes — path / note
- **Refined prompt:** `01-prompt-betterment/refined-prompt.md`
- **Audit verdict:**
- **Self-improvement:** `07-self-improvement/changes-applied.md`

Note: When implementer returns `blocked` / `aborted_dirty` / `non_ff`, orchestrator sets **Status** to `blocked` in that turn (do not leave `in_progress` until audit). Correct unrelated dirty-abort or expected `other`/`non_ff` = process may pass audit while session stays **`blocked`** — never claim pull succeeded. For `non_ff`, remediation is a **new** cycle (Choose Q2 B/C or recover allowlist tip + Q3c stash→ff→pop) — not silent merge under Q2=A. Mid-cycle re-invoke that names **this** incomplete folder as prior → **resume here** (orchestrator continues next unchecked phase); do not bootstrap a parallel dated session for the same cycle. Auditor is readonly — orchestrator **always** persists returned `06-audit/report.md` body (bookkeeping). After planner: **`docs_only` + `ready_to_implement: yes`** → same-run implement→audit→self-improve (no mandatory pause); `fs_mutation` / not ready → stop at plan gate. **STAGE 1 → STAGE 2:** `fs_mutation` STAGE 1 holds gate; after yes (+ amendments) resume **this** session for implement→audit→self-improve. Named Continuity B / stop docs_only re-attest → lock `fs_mutation` (not Continuity A theater). **Before each next-phase launch:** flip Workflow progress + Phase checklist for the completed phase (esp. after git-manager before auditor).

## Program framing (optional)

Use when this FAW is one cycle of a larger program (e.g. corpus organisation).

- **Program / roadmap:** `program/ROADMAP.md` (or n/a)
- **Cycle id:** (e.g. Cycle 0 charter | Cycle N folder-batch)
- **ROADMAP row locked:** (exact row / thread orchestrator chose or user named)
- **Mutation class:** `docs_only` | `fs_mutation`
- **Batch approval:** `n/a` | `pending` | `approved` (date/note)
- **Pending user gates:** (e.g. taxonomy final sign-off | must-preserve review | none | waived: …)
- **Prior session / locked answers:** (path or n/a)
- **WorkSpace strategy artifact (if WorkSpace-only):** `program/git-strategy-workspace-hazards.md` (or n/a if not yet written)
- **Consent UX note:** clarifying Qs and plan gates must ship with plain-language explanation + pros/cons (orchestrator relays the same)
- **STAGE:** (e.g. prompt-betterment | research → plan → same-run implement if docs_only ready)

## Workflow progress

- [ ] 0. Session bootstrap
- [ ] 1. prompt-betterment → 01-prompt-betterment/
- [ ] 2. researcher → 02-research/
- [ ] 3. planner → 03-plan/
- [ ] 4. User plan gate → n/a (`docs_only`) | pending | approved
- [ ] 5. implementer → 04-implementation/
- [ ] 6. git-manager → 05-git/
- [ ] 7. auditor → 06-audit/
- [ ] 8. self-improver → 07-self-improvement/  (MANDATORY)
- [ ] 9. Close SESSION.md

## Phase checklist

- [ ] 01 prompt-betterment
- [ ] 02 research
- [ ] 03 plan
- [ ] 04 implementation
- [ ] 05 git
- [ ] 06 audit
- [ ] 07 self-improvement

## Phase summaries

| Phase | Status | One-line summary | Artifacts |
| --- | --- | --- | --- |
| 01 | | | `01-prompt-betterment/` |
| 02 | | | `02-research/` |
| 03 | | | `03-plan/` |
| 04 | | | `04-implementation/` |
| 05 | | | `05-git/` |
| 06 | | | `06-audit/` |
| 07 | | | `07-self-improvement/` |
