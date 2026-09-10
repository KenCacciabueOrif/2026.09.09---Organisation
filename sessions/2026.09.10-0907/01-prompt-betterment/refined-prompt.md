# Refined prompt — Cycle 10 Multi-experiment (`WorkSpace` only + hazard remediation)

## Goal

Run one FAW program cycle for the orchestrator-locked ROADMAP row **Multi-experiment remaining: `WorkSpace` only**, under **dedicated hazard remediation / git-strategy Continuity** (user intent: solve WorkSpace hazards).

1. **Research** live state of `C:\Project\WorkSpace` focused on classifying known Cycle 9 hazards (multi-remote hermes-agent `origin`+`cada` on live and backup/quarantine clones; unexpected nested `.git` under `_backups`/`_quarantine`; nested-root count; XL size; opaque `.env` path presence only; must-preserve draft Medium caution). Verify archived Multi-experiment peers stay put and are not re-proposed as sources.
2. **Remediate via strategy (Q1=A / Q2=A):**
   - Produce classification of remotes and nested roots.
   - Decide/document recommended **fate** of `_backups` / `_quarantine` git roots (keep / isolate / defer — as evidence supports).
   - Document **safe relocation rules** for a future or gated move (atomic nested git; SSH path-only; opaque `.env`; Windows lock recovery).
   - Prefer **docs_only** deliverables (session docs, INDEX/ROADMAP honesty, strategy notes).
   - Planner **may** draft a **scoped** `fs_mutation` map **only** for **named hazard isolation** (not whole-tree archive) — **still blocked until separate plan gate approval**.
3. **Never force-move** the whole XL `WorkSpace` tree under ordinary Multi-experiment Continuity — whole-tree archive this cycle = **OUT OF SCOPE**.
4. **Never** mark Multi-experiment **Complete** or jump **Primary next** / Special git while `WorkSpace` remains.
5. **Never** reopen Medium / Early/simple or re-propose archived peers (`PWAExemple`, `GitTest`, `WorkStationPWA`) as move sources.
6. Continuity **Choose all ≠** move approval.

## Constraints

- **ROADMAP lock:** same Multi-experiment row / `WorkSpace` only — do not re-pick.
- **Continuity (Q3=A) carry:**
  - Layout: archive / paused / active per research status
  - Nested `.git`: **atomic** (intact trees; fail-closed unless remediation plan explicitly addresses a named root under plan gate)
  - Secrets: **opaque `.env`** — path presence only; never read/quote contents
  - Remotes: **SSH-origin path-only** — no `origin` URL rewrite this cycle unless a gated strategy step later says otherwise (default: document only)
  - Status: 90-day heuristic when classifying (confirm from disk)
  - Windows nested-`.git` lock recovery: prefer single move; on PermissionDenied/split → reunify + `robocopy /E /MOVE`; remove **only empty** leftover `.git` shells; re-attest; log deviation
  - INDEX honesty: document hazards / remediation progress; never claim moves that did not happen
  - Taxonomy wording: **proposed-ratified — ready for user sign-off** (not final without explicit user approval)
  - Must-preserve wording: **draft — not auto-locked / for user review**
- **Consent:** Continuity / Choose all **≠** move approval. If plan is `fs_mutation`, **mandatory separate plan gate** before implementer; include intent-preview.
- **Mutation class:** Prefer `docs_only`. Scoped `fs_mutation` only for named hazard isolation after plan gate. Whole XL tree archive under ordinary Multi-experiment Continuity = **OUT OF SCOPE**.
- **Org-repo git:** stage/commit only this organisation git root when publishing session docs; no sibling-tree ops.
- Small diffs; no secrets in commits or session logs; no force-push; no history rewrite / `filter-repo`.

## Context pointers

- Program: `program/ROADMAP.md`, `program/CHARTER.md`
- Catalogue: `catalogue/INDEX.md`, `catalogue/must-preserve.md` (draft)
- Prior cycle: `sessions/2026.09.10-0848/` (Cycle 9 — docs_only defer; hazards uncleared)
- This session: `sessions/2026.09.10-0907/`
- Continuity answers: `sessions/2026.09.10-0907/01-prompt-betterment/notes.md`
- Corpus candidate (only): `C:\Project\WorkSpace`
- Do **not** use as sources: archived Multi-experiment peers; Medium/Early archive or paused paths from prior cycles

## Acceptance criteria

- [ ] Research covers **`WorkSpace` only** as remediation candidate; archived peers verified not re-proposed as sources.
- [ ] Hazard classification is explicit for at least: multi-remote (`origin`/`cada`), `_backups`/`_quarantine` nested roots, nested-root count vs prior, XL/size note, opaque `.env` path presence (unread), must-preserve draft caution.
- [ ] Deliverables include **safe relocation / remediation rules** (docs) suitable for future or gated use — not silent execution.
- [ ] Implementation class is declared: **`docs_only`** by default, **or** `fs_mutation` **only** if a **scoped named-hazard isolation** map is proposed.
- [ ] If `docs_only`: **zero** corpus path moves; Multi-experiment row stays **in progress** with **Remaining: `WorkSpace` only**; INDEX/ROADMAP honesty updated.
- [ ] If scoped `fs_mutation` map proposed: plan includes concrete from→to + intent-preview; **orchestrator waits for plan-gate approval** before implementer; no silent execute from Continuity Choose.
- [ ] **No whole-tree archive / force-move** of `WorkSpace` under ordinary Multi-experiment Continuity this cycle.
- [ ] ROADMAP/INDEX **never** mark Multi-experiment **Complete** or **Primary next** jump while `WorkSpace` remains.
- [ ] Medium / Early / archived Multi-experiment peers **not** reopened as move sources.
- [ ] Opaque `.env`, atomic nested git, SSH path-only, Windows lock-recovery Continuity respected if any approved scoped move runs.
- [ ] Taxonomy / must-preserve language stays **proposed-ratified / draft** — not claimed final user ratification.
- [ ] No remote URL rewrite / history rewrite / `.env` content reads.
- [ ] Auditor can verify AC from session artifacts without chat history.

## Out of scope

- Whole XL `WorkSpace` tree archive / force-move under ordinary Multi-experiment Continuity
- Moving Special git / ProjetOrif / Obsidian / hygiene mini-batches
- Reopening Medium wrappers or Early/simple batches
- Re-moving or re-proposing `PWAExemple`, `GitTest`, `WorkStationPWA`
- Taxonomy final sign-off or must-preserve final lock (unless user explicitly starts that gate)
- Rewriting remotes, history rewrite, force-push, reading `.env` contents
- Marking Multi-experiment Complete while `WorkSpace` remains
- Treating Continuity “Choose all” as plan-gate move approval
- Dumping user chores to fix remotes/PATH as Continuity requirements

## Good vs bad outcomes

| Good | Bad |
| --- | --- |
| Remotes/roots classified; safe rules documented; INDEX/ROADMAP honest; row stays in progress | Force-move / whole-tree archive without plan gate |
| Optional scoped isolation map only after plan gate | Continuity Choose treated as move approval |
| Docs-first remediation progress | Mark Multi-experiment Complete / jump Primary next while WorkSpace remains |
| No peer reopen | Re-propose archived `PWAExemple` etc. as sources |
| Fail-closed when scoped FS still unsafe | Silent remote rewrite or `.env` reads |

## Locked choices (prompt-betterment)

| Item | Value | Source |
| --- | --- | --- |
| Q1 | **A** — dedicated hazard remediation / git-strategy Continuity (not pure defer) | `Choose all` |
| Q2 | **A** — classification + safe-rules docs first; scoped `fs_mutation` only for named hazard isolation after plan gate; whole-tree archive OOS | `Choose all` |
| Q3 | **A** — carry Continuity | `Choose all` |
| ROADMAP | Multi-experiment **`WorkSpace` only** | orchestrator lock |
| Consent | Continuity Choose ≠ plan-gate move approval | Continuity law |
