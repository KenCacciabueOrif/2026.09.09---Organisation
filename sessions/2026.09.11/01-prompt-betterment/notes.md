# Prompt betterment notes — Cycle 14

**Session phase:** `sessions/2026.09.11/01-prompt-betterment/`  
**Pack type:** Post–hazard-strategy WorkSpace-only Continuity pack — **Appendix A execute (Continuity B)**  
**Raw goal (orchestrator):** `/full-agent-workflow` next reorg cycle; prior `sessions/2026.09.10-1630` complete; user **explicit Continuity B** + STAGE 1 stop at plan gate (Hermes).

**Informed consent:** Questions below were drafted with plain-language explanation + pros/cons. Answers locked from **user-explicit** Continuity B + STAGE 1 directive (no blocking chat round-trip). Explanation debt: **none** for this phase (asks documented; answers pre-supplied by user/orchestrator handoff).

---

## Clarifying questions (short Continuity pack — recorded for audit)

### Q1 — Path this cycle (Continuity)

**Plain language:** Do we keep writing/updating strategy docs only, or draft a real move plan to relocate the labeled `_backups` and `_quarantine` parent folders out of the live WorkSpace tree?  
**Terms:** `fs_mutation` = a plan that moves/renames/deletes corpus paths. `plan gate` = your separate yes before anyone runs those moves. Continuity choice ≠ that yes.

| Option | Commits to | Pros | Cons |
| --- | --- | --- | --- |
| **A** Continue strategy (`docs_only`) | Re-probe / refine hazard docs; **zero** corpus moves | Safest; no FS risk | Cycles 10–13 already attested no material delta four times — repeats stall progress |
| **B** Appendix A scoped isolation Continuity | Planner drafts `fs_mutation` move map for `_backups` + `_quarantine` parents per `program/git-strategy-workspace-hazards.md`; **still needs plan gate** before implement | Progress on preferred fate; shrinks live XL tree ~3.3 GB if both move | Real FS risk; live hermes multi-remote **not** cleared; row stays in progress |
| **C** Pure research+defer honesty pass | Docs-only no-op re-attest | Minimal churn | Explicitly unwanted this cycle |

### Q2 — Carry prior Continuity locks?

**Plain language:** Keep the same safety rules from earlier Multi-experiment cycles (layout, atomic nested git, path-only remotes, opaque secrets, honesty language), or reopen them?

| Option | Commits to | Pros | Cons |
| --- | --- | --- | --- |
| **A** Carry | Lock layout / atomic nested-git / SSH-or-HTTPS origin path-only (no rewrite) / opaque `.env*` / taxonomy+must-preserve wording / never whole-tree force-move / never Complete while WorkSpace remains / no peer reopen / no history rewrite / Windows nested-`.git` lock recovery / INDEX honesty / agent-owned (no user PATH chores) | Consistency; less re-litigation | Harder to change mid-cycle without new Continuity |
| **B** Change Continuity | User renames which locks to alter | Flexibility | Requires explicit new answers; risk of accidental rewrite/history ops |

### Q3 — Taxonomy / must-preserve re-litigation?

**Plain language:** Taxonomy = proposed folder-type labels (**proposed-ratified — ready for user sign-off**, not final). Must-preserve = draft keep-list (**draft — not auto-locked / for user review**). Re-debate them this cycle, or waive and proceed on Continuity B map?

| Option | Commits to | Pros | Cons |
| --- | --- | --- | --- |
| **A** Waive re-litigation | Carry prior wording; do not block STAGE 1 on fresh taxonomy/must-preserve debate | Unblocks plan draft | Sign-off still open later if needed for other gates |
| **B** Re-open sign-off now | Pause Continuity B planning until taxonomy/must-preserve resolved | Stronger consent trail | Delays Appendix A plan; user asked not to stall on docs re-attest |

---

## Ask summary (one line per Q)

1. **Q1:** Continuity path — docs-only continue-strategy (A) vs Appendix A scoped isolation Continuity (B) vs pure research+defer (C).  
2. **Q2:** Carry Multi-experiment / WorkSpace Continuity locks vs change them.  
3. **Q3:** Waive taxonomy/must-preserve re-litigation vs re-open sign-off this cycle.

---

## Answers

| Q | Locked | Source | Rationale |
| --- | --- | --- | --- |
| **Q1** | **B** — Appendix A scoped isolation Continuity (`fs_mutation` plan for `_backups` + `_quarantine` parent trees out of live WorkSpace; Continuity ≠ execute; separate plan gate mandatory, held in Hermes for STAGE 1) | **user-explicit** | Raw goal: “Take Continuity B… STAGE 1 ONLY… plan gate… human-held”; “do NOT run another docs_only re-attestation” |
| **Q2** | **A** — Carry Continuity locks listed above | **user-explicit** / **yes→defaults** style | Orchestrator: honor prior Continuity; user STAGE 1 Continuity B does not reopen layout/git/remote/history rules |
| **Q3** | **A** — Waive taxonomy/must-preserve re-litigation this cycle | **user-explicit** | Pending gates may remain open; waive re-litigation (Q3=A carry) |

**Raw directive excerpt:** Continuity B + Appendix A + `fs_mutation` + STAGE 1 stop at plan gate; Cycles 10–13 docs_only re-attest forbidden as cycle path.

---

## Continuity (locked — do not re-ask)

- **Cycle id:** Cycle 14 — Multi-experiment (**WorkSpace only**) — Continuity **B** Appendix A scoped isolation  
- **ROADMAP row:** Multi-experiment remaining **`WorkSpace` only** — **in progress / not Complete**  
- **Never:** jump Primary next / Special git; reopen Medium / Early; re-propose archived peers (`PWAExemple`, `GitTest`, `WorkStationPWA`); invent whole-tree WorkSpace archive; mark Multi-experiment Complete while WorkSpace remains  
- **Mutation class intent:** `fs_mutation` (Continuity B locked)  
- **Strategy artifact:** `program/git-strategy-workspace-hazards.md` (Appendix A + safe relocation rules)  
- **Prior session:** `sessions/2026.09.10-1630/` (Cycle 13 docs_only continue-strategy; Next FAW hint allowed B — **user chose B**)  
- **Carry:** layout; atomic intact nested-git; origin path-only (no remote rewrite); opaque `.env*`; no history rewrite; Windows nested-`.git` lock recovery; INDEX honesty; agent-owned (no user PATH/remote chores)  
- **Taxonomy language:** **proposed-ratified — ready for user sign-off** (not final)  
- **Must-preserve language:** **draft — not auto-locked / for user review**  
- **STAGE 1:** phases 1–3 only; plan gate **not** cleared by this agent / this run — held in Hermes chat  
- **If plan is NOT Continuity B scoped isolation:** stop at plan gate (orchestrator fail-closed)

---

## Assumptions

- Illustrative from→to in Cycle 10 `sessions/2026.09.10-0907/03-plan/plan.md` Appendix A is a **draft hint only** — researcher/planner must re-confirm destinations free and paths live.  
- Expect nested count **7→5** and ~3.3 GB out of live tree **if both** parents move — does **not** clear live hermes multi-remote.  
- `ready_to_implement` may be `yes` on the plan for planner completeness; orchestrator **still** holds plan gate (STAGE 1).  
- No publish/pull cycle this phase.

---

## Open risks

- Windows file locks on large `_backups` / `_quarantine` (~1.6 GB each) → need lock-recovery rules from strategy artifact.  
- Dual-remote hermes clones under those parents — move intact; never rewrite remotes.  
- Accidental scope creep to live primary roots or whole-tree archive — hard AC forbid.  
- Plan gate delayed in Hermes → implementer must not start until explicit yes.

---

## Self-improvement backlog (if any)

- None for informed-consent debt this phase.

---

## Key alignment changes (raw → refined)

- Locked **Continuity B** (not A/C); forbade docs_only re-attest as cycle path.  
- Scoped **WorkSpace only** / **Appendix A only** (`_backups` + `_quarantine` parents).  
- Encoded STAGE 1 + Hermes-held plan gate; Continuity ≠ execute.  
- Pointed all downstream phases at `program/git-strategy-workspace-hazards.md` safe relocation rules.  
- Waived taxonomy/must-preserve re-litigation (Q3=A) while keeping proposed-ratified / draft wording.
