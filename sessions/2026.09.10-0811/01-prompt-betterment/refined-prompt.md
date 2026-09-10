# Refined prompt — Cycle 8 Multi-experiment (remaining subset)

## Goal

Run the next organisation FAW cycle for **`C:\Project`**: **Cycle 8 — Multi-experiment remaining subset**. Research, plan, and (only after a separate user **plan gate**) execute allowed moves for remaining Multi-experiment names, then update catalogue / ROADMAP Notes.

**Choose / Continuity is not move approval.** Implementer must not move anything until the user explicitly approves the concrete from→to plan map for this batch.

## Constraints

- **ROADMAP row (locked):** Multi-experiment **remaining only** — candidates: `PWAExemple`, `WorkSpace`. Do **not** jump Primary next while names remain. Do **not** mark Multi-experiment Complete if either name remains unmoved/deferred.
- **Scope (Q1=A):** Prefer **`PWAExemple`** when research is green. Keep **`WorkSpace`** **fail-closed / git-strategy candidate** until hazards are cleared — do **not** force-move `WorkSpace` by default; do **not** start a dedicated git-strategy execution cycle unless research clears hazards and the plan explicitly schedules strategy work (default = defer `WorkSpace`, log reason).
- **Do not reopen** Medium wrappers or Early/simple archives/paused paths as move **sources**.
- **Do not re-propose** already-moved Cycle 7 peers as sources: `GitTest`, `WorkStationPWA` (already → archive).
- **Multi nested-git caution (Continuity):** Each nested `.git` stays **atomic** (intact tree move). **Fail-closed:** skip/defer any candidate with linked worktrees, messy multi-remote, or unexpected extra roots; log reason; do not force.
- **SSH / remotes (Continuity):** **Path-only** moves — never rewrite `origin` (or other remotes) this cycle.
- **Carry Continuity (Q2=A):**
  - Destination layout: `archive` / `paused` / `active` under catalogue taxonomy (same pattern as Cycles 2–7).
  - **Opaque `.env`:** path presence only; never read, quote, or log secret contents.
  - Taxonomy: **proposed-ratified — ready for user sign-off** (not final without explicit approval); do not re-block solely to re-litigate.
  - Must-preserve: **draft — not auto-locked / for user review**; do not re-block solely to re-litigate.
  - **90-day** status heuristic (research confirms from disk timestamps); verify / rollback notes as prior cycles.
  - `catalogue/INDEX.md` must reflect **current** paths honestly after moves.
  - **Windows nested-`.git` lock recovery:** Prefer single `Move-Item`. On `PermissionDenied` / mid-move split: reunify into destination; finish remaining children with `robocopy /E /MOVE`; remove **only empty** leftover `.git` shells (0 children); never delete non-empty payload; re-attest nested git; log as process deviation (not scope expansion).
- **Mutation class:** `fs_mutation` — mandatory **per-batch plan gate** before implementer (separate from this Continuity Choose).
- **Org-repo / protect:** Do not casually move `2026.09.09 - Organisation`; stage/commit only inside org git root if any org-repo docs update is needed.
- No secrets in session logs or commits.

## Context pointers

- `program/ROADMAP.md`, `program/CHARTER.md`, `catalogue/INDEX.md`
- Prior session (Cycle 7 complete): `sessions/2026.09.10/`
- This phase: `sessions/2026.09.10-0811/01-prompt-betterment/notes.md` (Answers + Continuity locks)
- Continuity language: taxonomy **proposed-ratified — ready for user sign-off**; must-preserve **draft — not auto-locked / for user review**

## Acceptance criteria

- [ ] Research live-checks only remaining Multi-experiment candidates (`PWAExemple`, `WorkSpace`) and proposes an executable map consistent with Q1=A (prefer green `PWAExemple`; keep `WorkSpace` fail-closed / git-strategy until cleared); documents deferred names + reasons.
- [ ] Research verifies Cycle 7 archives (`GitTest`, `WorkStationPWA`) and Medium/Early destinations are **not** re-proposed as move sources.
- [ ] Plan is `fs_mutation` with a concrete from→to map, status destinations (90-day Continuity), nested-git atomicity notes, opaque-`.env` note, SSH path-only (no remote rewrite), and Windows lock-recovery Continuity note.
- [ ] Plan includes a clear “What the user is approving” block for the orchestrator plan-gate relay.
- [ ] **No moves until user plan-gate approval** for this batch’s map — Continuity **Choose all** does **not** satisfy this.
- [ ] After approval: only approved remaining folders moved intact; no Medium/Early reopen; no re-move of `GitTest` / `WorkStationPWA`; no origin rewrite; no secret contents read/logged.
- [ ] Fail-closed items skipped with logged reason; subset may shrink (including to `PWAExemple`-only or zero) without inventing unsafe or substitute moves.
- [ ] On Windows nested-`.git` lock: recovery Continuity followed (reunify + `robocopy /E /MOVE`; empty shells only; re-attest); logged as deviation, not silent delete of payload.
- [ ] `catalogue/INDEX.md` (and ROADMAP Notes for remaining Multi-experiment names) updated to match reality; row not marked Complete if names remain deferred/unmoved.
- [ ] Auditor can verify path presence, INDEX honesty, and Continuity locks without needing chat history.

## Out of scope

- Jumping Primary next / Special git / Obsidian / ProjetOrif / WebCatalogue / HTTP Battles / hygiene root batches this cycle.
- Reopening or re-moving Medium / Early/simple destinations as sources.
- Re-moving or “fixing up” Cycle 7 archive destinations for `GitTest` / `WorkStationPWA`.
- Force-moving `WorkSpace` despite fail-closed hazards; rewriting git remotes / history / filter-repo / worktree repair.
- Dedicated git-strategy **execution** for `WorkSpace` unless research clears hazards and the approved plan explicitly includes it (Q1=A default = defer).
- Treating taxonomy or must-preserve as **final** without explicit user sign-off.
- Git push/publish of org-repo unless a later explicit publish goal (not this Continuity pack).
