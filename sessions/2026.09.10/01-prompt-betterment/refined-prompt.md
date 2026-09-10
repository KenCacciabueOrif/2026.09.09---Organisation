# Refined prompt — Cycle 7 Multi-experiment (first subset)

## Goal

Run the next organisation FAW cycle for **`C:\Project`**: **Cycle 7 — Multi-experiment (first subset)**. Research, plan, and (only after a separate user **plan gate**) execute moves for a **small first slice** of Multi-experiment candidates, then update catalogue / ROADMAP Notes for remaining names.

**Choose / Continuity is not move approval.** Implementer must not move anything until the user explicitly approves the concrete from→to plan map for this batch.

## Constraints

- **ROADMAP row (locked):** Primary next → **Multi-experiment** — candidates only: `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace`.
- **Subset size (Q1=A):** Target **1–2** folders this cycle; research selects lower-risk peers (document which + why). Remaining candidates stay on the Multi-experiment row (update ROADMAP Notes — do **not** claim row Complete until all four are done or dropped by user).
- **Do not reopen** Medium wrappers (Cycle 6 Complete) or Early/simple archives/paused paths as move **sources**.
- **Multi nested-git caution (Q2=A):** Each nested `.git` stays **atomic** (intact tree move). **Fail-closed:** skip/defer any candidate with linked worktrees, messy multi-remote, or unexpected extra roots; log reason; do not force.
- **SSH / remotes (Q3=A):** **Path-only** moves — never rewrite `origin` (or other remotes) this cycle. Dedicated git-strategy cycle only if user later opts in.
- **Carry Continuity (Q4=A):**
  - Destination layout: `archive` / `paused` / `active` under catalogue taxonomy (same pattern as Cycles 2–6).
  - **Opaque `.env`:** path presence only; never read, quote, or log secret contents.
  - Taxonomy: **proposed-ratified — ready for user sign-off** (not final without explicit approval); do not re-block solely to re-litigate.
  - Must-preserve: **draft — not auto-locked / for user review**; do not re-block solely to re-litigate.
  - **90-day** status heuristic (research confirms from disk timestamps); verify / rollback notes as prior cycles.
  - `catalogue/INDEX.md` must reflect **current** paths honestly after moves.
- **Mutation class:** `fs_mutation` — mandatory **per-batch plan gate** before implementer (separate from this Continuity Choose).
- **Org-repo / protect:** Do not casually move `2026.09.09 - Organisation`; stage/commit only inside org git root if any org-repo docs update is needed.
- No secrets in session logs or commits.

## Context pointers

- `program/ROADMAP.md`, `program/CHARTER.md`, `catalogue/INDEX.md`
- Prior session (Medium Complete): `sessions/2026.09.09-1612/`
- This phase: `sessions/2026.09.10/01-prompt-betterment/notes.md` (Answers + Continuity locks)
- Continuity language: taxonomy **proposed-ratified — ready for user sign-off**; must-preserve **draft — not auto-locked / for user review**

## Acceptance criteria

- [ ] Research live-checks only Multi-experiment candidates (`PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace`) and proposes a **1–2** folder first subset with lower-risk rationale; documents deferred names if any.
- [ ] Plan is `fs_mutation` with a concrete from→to map, status destinations (90-day Continuity), nested-git atomicity notes, opaque-`.env` note, and SSH path-only (no remote rewrite).
- [ ] Plan includes a clear “What the user is approving” block for the orchestrator plan-gate relay.
- [ ] **No moves until user plan-gate approval** for this batch’s map — Continuity Choose all does **not** satisfy this.
- [ ] After approval: only approved subset folders moved intact; no Medium/Early reopen; no origin rewrite; no secret contents read/logged.
- [ ] Fail-closed items skipped with logged reason; subset may shrink without inventing unsafe moves.
- [ ] `catalogue/INDEX.md` (and ROADMAP Notes for remaining Multi-experiment names) updated to match reality; row not marked Complete if names remain.
- [ ] Auditor can verify path presence, INDEX honesty, and Continuity locks without needing chat history.

## Out of scope

- Moving all four Multi-experiment folders unless research + plan gate later expand (this cycle locked to **1–2**).
- Reopening or re-moving Medium / Early/simple destinations as sources.
- Rewriting git remotes / history / filter-repo / worktree repair.
- Obsidian, ProjetOrif, WebCatalogue, HTTP Battles, hygiene root batches, or dedicated git-strategy cycle (unless a fail-closed finding explicitly recommends scheduling one later — not executing it here).
- Treating taxonomy or must-preserve as **final** without explicit user sign-off.
- Git push/publish of org-repo unless a later explicit publish goal (not this Continuity pack).
