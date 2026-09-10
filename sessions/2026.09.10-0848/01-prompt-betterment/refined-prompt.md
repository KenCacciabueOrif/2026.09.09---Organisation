# Refined prompt — Cycle 9 Multi-experiment (`WorkSpace` only)

## Goal

Run one FAW program cycle for the orchestrator-locked ROADMAP row **Multi-experiment remaining: `WorkSpace` only** (fail-closed / git-strategy candidate).

1. **Research** live hazards on `C:\Project\WorkSpace` (nested git roots, worktrees, remotes/multi-remote, locks, unexpected structure) and verify archived Multi-experiment peers stay put.
2. **Decide path under Continuity Q1=A:**
   - If hazards are **clearly cleared** → may propose a concrete from→to move map for plan gate (still **no** execute until approved).
   - Otherwise → **fail-closed defer** (`docs_only`: session docs, honest INDEX/ROADMAP notes that `WorkSpace` remains; **zero** corpus moves).
3. **Never force-move** `WorkSpace` under ordinary Multi-experiment Continuity.
4. **Do not** start a dedicated git-strategy planning thread this cycle (user did not choose Q1=B).
5. **Never** mark Multi-experiment **Complete** or jump **Primary next** / Special git while `WorkSpace` remains.
6. **Never** reopen Medium / Early/simple or re-propose archived peers (`PWAExemple`, `GitTest`, `WorkStationPWA`) as move sources.

## Constraints

- **ROADMAP lock:** same Multi-experiment row / `WorkSpace` only — do not re-pick.
- **Continuity (Q2=A) carry:**
  - Layout: archive / paused / active per research status
  - Nested `.git`: **atomic** (intact trees; fail-closed on worktrees / multi-remote / unexpected roots)
  - Secrets: **opaque `.env`** — path presence only; never read/quote contents
  - Remotes: **SSH-origin path-only** — no `origin` URL rewrite
  - Status: 90-day heuristic when classifying (confirm from disk)
  - Windows nested-`.git` lock recovery: prefer single move; on PermissionDenied/split → reunify + `robocopy /E /MOVE`; remove **only empty** leftover `.git` shells; re-attest; log deviation
  - INDEX honesty: document deferrals/hazards; never claim moves that did not happen
  - Taxonomy wording: **proposed-ratified — ready for user sign-off** (not final without explicit user approval)
  - Must-preserve wording: **draft — not auto-locked / for user review**
- **Consent:** Continuity / user “yes” / Choose defaults **≠** move approval. If plan is `fs_mutation`, **mandatory separate plan gate** before implementer.
- **Org-repo git:** stage/commit only this organisation git root when publishing session docs; no sibling-tree ops.
- Small diffs; no secrets in commits or session logs; no force-push; no history rewrite / `filter-repo`.

## Context pointers

- Program: `program/ROADMAP.md`, `program/CHARTER.md`
- Catalogue: `catalogue/INDEX.md`, `catalogue/must-preserve.md` (draft)
- Prior cycle: `sessions/2026.09.10-0811/` (Cycle 8 — `PWAExemple` archived; `WorkSpace` fail-closed)
- This session: `sessions/2026.09.10-0848/`
- Continuity answers: `sessions/2026.09.10-0848/01-prompt-betterment/notes.md`
- Corpus candidate (only): `C:\Project\WorkSpace`
- Do **not** use as sources: archived Multi-experiment peers; Medium/Early archive or paused paths from prior cycles

## Acceptance criteria

- [ ] Research covers **`WorkSpace` only** as move candidate; archived peers verified not re-proposed as sources.
- [ ] Hazard outcome is explicit: **cleared** vs **fail-closed defer** (with concrete hazard reasons if deferred).
- [ ] If deferred: implementation is **`docs_only`** (session + INDEX/ROADMAP honesty); **zero** corpus path moves; Multi-experiment row stays **in progress** with **Remaining: `WorkSpace` only**.
- [ ] If cleared and a move map is proposed: plan declares **`fs_mutation`**; includes intent-preview; **orchestrator waits for plan-gate approval** before implementer; no silent execute from Continuity alone.
- [ ] **No force-move** of `WorkSpace` when hazards uncleared or when Continuity alone is cited as approval.
- [ ] **No dedicated git-strategy** plan body this cycle (Q1≠B).
- [ ] ROADMAP/INDEX **never** mark Multi-experiment **Complete** or **Primary next** jump while `WorkSpace` remains.
- [ ] Medium / Early / archived Multi-experiment peers **not** reopened as move sources.
- [ ] Opaque `.env`, atomic nested git, SSH path-only, Windows lock-recovery Continuity respected if any approved move runs.
- [ ] Taxonomy / must-preserve language stays **proposed-ratified / draft** — not claimed final user ratification.
- [ ] Auditor can verify AC from session artifacts without chat history.

## Out of scope

- Dedicated multi-repo **git-strategy** FAW cycle (unless a future Continuity chooses B)
- Moving Special git / ProjetOrif / Obsidian / hygiene mini-batches
- Reopening Medium wrappers or Early/simple batches
- Re-moving or re-proposing `PWAExemple`, `GitTest`, `WorkStationPWA`
- Taxonomy final sign-off or must-preserve final lock (unless user explicitly starts that gate)
- Rewriting remotes, history rewrite, force-push, reading `.env` contents
- Marking Multi-experiment Complete while `WorkSpace` remains
- Treating Continuity “yes” as plan-gate move approval

## Good vs bad outcomes

| Good | Bad |
| --- | --- |
| Hazards documented; defer with honest INDEX/ROADMAP; row stays in progress | Force-move despite uncleared hazards |
| Cleared + plan gate + approved map only if truly safe | Continuity yes treated as move approval |
| Docs-only process pass when deferred | Mark Multi-experiment Complete / jump Primary next while WorkSpace remains |
| No peer reopen | Re-propose archived `PWAExemple` etc. as sources |
| Git-strategy deferred to a future opt-in | Silent “git-strategy” that relocates the tree without plan gate |

## Locked choices (prompt-betterment)

| Item | Value | Source |
| --- | --- | --- |
| Q1 | **A** — research+defer unless cleared; no force-move; no git-strategy B | raw “yes” → Choose/defaults |
| Q2 | **A** — carry Continuity | raw “yes” → Choose/defaults |
| ROADMAP | Multi-experiment **`WorkSpace` only** | orchestrator lock |
