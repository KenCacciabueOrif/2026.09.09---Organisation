# Session

- **Date folder:** `yyyy.mm.dd` (or `yyyy.mm.dd-HHMM` on collision)
- **Status:** `in_progress` | `blocked` | `complete`
- **Blocker (if blocked):** `dirty_working_tree` | `agent_environment` | `user_credentials` | `other` (e.g. non-ff / merge_conflict) | … (or n/a)
- **Raw goal:**
- **Resume:** no | yes — path / note
- **Refined prompt:** `01-prompt-betterment/refined-prompt.md`
- **Audit verdict:**
- **Self-improvement:** `07-self-improvement/changes-applied.md`

Note: When implementer returns `blocked` / `aborted_dirty` / `non_ff`, orchestrator sets **Status** to `blocked` in that turn (do not leave `in_progress` until audit). Correct unrelated dirty-abort or expected `other`/`non_ff` = process may pass audit while session stays **`blocked`** — never claim pull succeeded. For `non_ff`, remediation is a **new** cycle (Choose Q2 B/C or recover allowlist tip + Q3c stash→ff→pop) — not silent merge under Q2=A. Mid-cycle re-invoke / **retry** that names **this** incomplete folder as prior → **resume here** (orchestrator continues next unchecked phase); if `04-implementation/` already **complete**, **skip** re-implementer. Do not bootstrap a parallel dated session for the same cycle. Auditor is readonly — orchestrator **always** persists returned `06-audit/report.md` body (bookkeeping). After planner: **`docs_only` or `product_settings` + `ready_to_implement: yes`** → same-run implement→mid git→audit→self-improve→**final closing-pass git**→Close (no mandatory corpus plan gate); `fs_mutation` / Continuity **X** hybrid **D/M/D+M** / **`escalate_break_loop`** / not ready → stop at plan or Continuity gate. **`ready_to_implement: no` (escalate):** skip implementer + mid git; after Continuity recorded (Step 3: notes + SESSION + ROADMAP Next FAW hint) still audit→SI→**final git**→Close. **Continuity X** = next FAW dedicated XL/whole-tree git-strategy + plan gate; still WorkSpace only / not Complete. **Continuity X dedicated:** hybrid gate **D/M/D+M**; **D+M** = docs first then `path_batch`; OS-IA alone never Completes / never Primary next; post–OS-IA Next FAW = WorkSpace **TNA** + continue Continuity X clearance / keep-at-root. **Clearance #4 / parent-surgery:** `program/git-strategy-tna-parent-surgery.md`; DRAFT written vs approved; docs gate ≠ nest-move; #4 draft ≠ whole-tree yes; nest extract only after #4 approved + dedicated gate. **STAGE 1 → STAGE 2:** `fs_mutation` / Continuity X STAGE 1 holds gate; after **D/M/D+M** / yes (+ amendments) resume **this** session for implement→mid git→audit→self-improve→**final git**→Close. Named Continuity B / stop docs_only re-attest → lock `fs_mutation` (not Continuity A theater). Anti-loop no-delta → **`escalate_break_loop`**. **Before each next-phase launch:** flip **Workflow progress + Phase checklist + Phase summaries** (status + one-liner) for the completed phase (esp. after mid git-manager before auditor, after auditor persist before self-improver, and after final git before Close). **Complete gate:** do **not** set Status `complete` if the final closing-pass git was skipped while allowlisted late dirt remains (`06-audit/**`, `07-self-improvement/**`, `SESSION.md` close, cycle `.cursor/**`); mid-only push does not satisfy the gate; honest final `blocked` → session `blocked` (never false complete).

## Program framing (optional)

Use when this FAW is one cycle of a larger program (e.g. corpus organisation).

- **Program / roadmap:** `program/ROADMAP.md` (or n/a)
- **Cycle id:** (e.g. Cycle 0 charter | Cycle N folder-batch)
- **ROADMAP row locked:** (exact row / thread orchestrator chose or user named)
- **Mutation class:** `docs_only` | `product_settings` | `fs_mutation` | `escalate_break_loop` | hybrid Continuity X **D** / **M** / **D+M**
- **Batch approval:** `n/a` | `pending` | `approved` (date/note) | Continuity gate `X`/`P`/`N`/`H` (escalate) | Continuity X plan gate `D`/`M`/`D+M`
- **Pending user gates:** (e.g. taxonomy final sign-off | must-preserve review | Continuity X/P/N | Continuity X D/M/D+M | none | waived: …)
- **Prior session / locked answers:** (path or n/a)
- **WorkSpace strategy artifact (if WorkSpace-only):** `program/git-strategy-workspace-hazards.md` (+ optional `program/git-strategy-tna-parent-surgery.md`) (or n/a if not yet written)
- **Clearance #4 status (if Continuity X / TNA):** n/a | DRAFT written / approval pending | approved (nest path_batch gate)
- **Consent UX note:** clarifying Qs and plan gates must ship with plain-language explanation + pros/cons (orchestrator relays the same)
- **STAGE:** (e.g. STAGE 1 hold at plan gate | STAGE 2 resume same session after D+M | prompt-betterment | escalate Continuity gate → close without implementer)
- **Next FAW lock hint:** (e.g. WorkSpace only (TNA) + continue Continuity X clearance / keep-at-root | WorkSpace only + Continuity X XL/git-strategy | n/a)

## Workflow progress

- [ ] 0. Session bootstrap
- [ ] 1. prompt-betterment → 01-prompt-betterment/
- [ ] 2. researcher → 02-research/
- [ ] 3. planner → 03-plan/
- [ ] 4. User plan gate → n/a (`docs_only` | `product_settings`) | pending | approved
- [ ] 5. implementer → 04-implementation/
- [ ] 6. git-manager (mid) → 05-git/ (optional/early for implementer work)
- [ ] 7. auditor → 06-audit/
- [ ] 8. self-improver → 07-self-improvement/  (MANDATORY)
- [ ] 9. git-manager (final closing pass) → 05-git/ (MANDATORY when allowlisted late dirt remains)
- [ ] 10. Close SESSION.md

## Phase checklist

- [ ] 01 prompt-betterment
- [ ] 02 research
- [ ] 03 plan
- [ ] 04 implementation
- [ ] 05 git (mid + final sections in same log when both run)
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
