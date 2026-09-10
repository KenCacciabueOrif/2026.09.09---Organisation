# Session

- **Date folder:** `yyyy.mm.dd`
- **Status:** `in_progress` | `blocked` | `complete`
- **Blocker (if blocked):** `dirty_working_tree` | `agent_environment` | `user_credentials` | `other` (e.g. non-ff) | … (or n/a)
- **Raw goal:** 
- **Refined prompt:** `01-prompt-betterment/refined-prompt.md`
- **Audit verdict:** 
- **Self-improvement:** `06-self-improvement/changes-applied.md`

Note: When implementer returns `blocked` / `aborted_dirty` / `non_ff`, orchestrator sets **Status** to `blocked` in that turn (do not leave `in_progress` until audit). Correct unrelated dirty-abort or expected `other`/`non_ff` = process may pass audit while session stays **`blocked`** — never claim pull succeeded. For `non_ff`, remediation is a **new** cycle (Choose Q2 B/C or recover allowlist tip + Q3c stash→ff→pop) — not silent merge under Q2=A. Mid-cycle re-invoke that names **this** incomplete folder as prior → **resume here** (orchestrator continues next unchecked phase); do not bootstrap a parallel dated session for the same cycle. Auditor is readonly — orchestrator **always** persists returned `05-audit/report.md` body (bookkeeping). After planner: **`docs_only` + `ready_to_implement: yes`** → same-run implement→audit→self-improve (no mandatory pause); `fs_mutation` / not ready → stop at plan gate.

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

## Phase checklist

- [ ] 01 prompt-betterment
- [ ] 02 research
- [ ] 03 plan
- [ ] 04 implementation
- [ ] 05 audit
- [ ] 06 self-improvement

## Phase summaries

| Phase | Status | One-line summary | Artifacts |
| --- | --- | --- | --- |
| 01 | | | |
| 02 | | | |
| 03 | | | |
| 04 | | | |
| 05 | | | |
| 06 | | | |
