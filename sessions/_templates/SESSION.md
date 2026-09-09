# Session

- **Date folder:** `yyyy.mm.dd`
- **Status:** `in_progress` | `blocked` | `complete`
- **Blocker (if blocked):** `dirty_working_tree` | `agent_environment` | `user_credentials` | `other` (e.g. non-ff) | … (or n/a)
- **Raw goal:** 
- **Refined prompt:** `01-prompt-betterment/refined-prompt.md`
- **Audit verdict:** 
- **Self-improvement:** `06-self-improvement/changes-applied.md`

Note: When implementer returns `blocked` / `aborted_dirty` / `non_ff`, orchestrator sets **Status** to `blocked` in that turn (do not leave `in_progress` until audit). Correct unrelated dirty-abort or expected non-ff = process may pass audit while session stays **`blocked`** — never claim pull succeeded.

## Program framing (optional)

Use when this FAW is one cycle of a larger program (e.g. corpus organisation).

- **Program / roadmap:** `program/ROADMAP.md` (or n/a)
- **Cycle id:** (e.g. Cycle 0 charter | Cycle N folder-batch)
- **ROADMAP row locked:** (exact row / thread orchestrator chose or user named)
- **Mutation class:** `docs_only` | `fs_mutation`
- **Batch approval:** `n/a` | `pending` | `approved` (date/note)
- **Pending user gates:** (e.g. taxonomy final sign-off | must-preserve review | none | waived: …)
- **Prior session / locked answers:** (path or n/a)
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
