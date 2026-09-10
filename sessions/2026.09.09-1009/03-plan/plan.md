# Plan — Cycle 1 Docs follow-ups

Session: `sessions/2026.09.09-1009/`  
Authoritative inputs: `../01-prompt-betterment/refined-prompt.md`, `../02-research/research-brief.md`, `../02-research/codebase-findings.md`  
Mutation class: **`docs_only`**

## Goal

Deepen organisation-repo catalogue and program docs for Cycle 1 only: mark taxonomy **proposed-ratified — ready for user sign-off** with locked Cycle 1 decisions (status axis, spaces in ShortName, CreationTime wins, wrapper=canonical / nested git=child atomic); deepen inventory with cheap size bands, clearer git notes, and LastWrite activity hints; add a must-preserve **draft** candidate list; sync INDEX legend + What’s next; mark ROADMAP Cycle 1 done with **Early/simple** as primary next and Git-strategy as hard-gate reminder. Prove **zero** intentional FS mutation under `C:\Project`. No push/publish. Do not execute Early/simple or git-strategy bodies.

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`docs_only`** |
| Corpus FS | **Zero intentional** moves / renames / deletes / mkdir-reorg under `C:\Project` |
| Allowed writes | Organisation repo docs only: `catalogue/*`, `program/*` (minimal), `sessions/2026.09.09-1009/04-implementation/*` |
| Implementer attest | In `04-implementation/log.md` + `changes.md`: list every touched path; state explicitly “no corpus path mutations”; auditor re-checks with git status / path list |
| User approval before implementer | **Not required** for this cycle (docs_only; no move/rename/delete batch) |

## Acceptance criteria

- [ ] `catalogue/taxonomy.md` status line is **proposed-ratified — ready for user sign-off** (must **not** claim final user ratification).
- [ ] Taxonomy documents locked rules: status `active` / `paused` / `archive` + INDEX specials `protect` / `hygiene` (**not** PARA-lite); ShortName **keeps spaces**; date default **CreationTime wins**; wrapper = canonical dated label / nested `.git` = child atomic units; empty-parent / multi-root stay in a short **still open / classify before move** note.
- [ ] Clear **decided vs open** sections in taxonomy (open items do not re-open locked Cycle 0/1 decisions).
- [ ] `catalogue/INDEX.md` legend uses the same status vocabulary; proposed date labels remain **proposals** (caveat retained); What’s next reflects Cycle 1 complete + Early/simple primary + Git-strategy hard gate.
- [ ] `catalogue/inventory.md` deepened vs Cycle 0 with: size-band cutoffs + per-row bands (S/M/L/XL) where research already computed them; clearer wrapper/git-class notes + scan limits (depth ≤2, lower bound); LastWrite as activity / next hints; secrets path-only; deep deps skipped (noted).
- [ ] New `catalogue/must-preserve.md` exists, labelled **draft — not auto-locked**, with candidates beyond org-repo default-protect (from research); no secret contents.
- [ ] `program/ROADMAP.md`: Cycle 1 done note; **primary next = Early/simple**; Git-strategy remains hard-gate reminder (not the primary next row).
- [ ] `program/organisation-approach.md` (and CHARTER only if needed) consistent with locked status axis / Cycle 1 boundary — no PARA-lite as open alternative for this program.
- [ ] Session `04-implementation/log.md` + `changes.md` written.
- [ ] Auditor can verify: **zero** intentional moves/renames/deletes under `C:\Project` attributable to this cycle; no `.env` / credential contents in logs.

**Not hard AC (include when cheap / already in research):** absolute cheap-MB numbers in every INDEX row; provisional mass-replacement of INDEX `TBD` statuses; re-scanning the corpus (prefer promote research tables).

## Ordered steps

### 1. Update `catalogue/taxonomy.md` → proposed-ratified

| | |
| --- | --- |
| **Paths** | `catalogue/taxonomy.md` |
| **Action** | Rewrite status header to **proposed-ratified — ready for user sign-off**. Lock decision table: status axis (no PARA-lite); ShortName with spaces (`yyyy.mm.dd - ShortName`); **CreationTime wins** over earliest commit and LastWrite (user memory may override later if explicitly stated); LastWrite = activity only; wrapper = top-level move unit / canonical label; nested `.git` = child atomic units. Move prior “open” items that are now locked into a **Decided (Cycle 1)** section. Keep a short **Still open / classify before move** for: empty-parent (`HTTP Battles`), multi-root keep-vs-split, zip sidecars, root-orphan hygiene labelling, deeper-than-2 git. Retain non-actions: no FS renames; proposed labels ≠ applied names. |
| **Verify** | Grep/read: “proposed-ratified”, “CreationTime wins”, “PARA-lite” absent as open choice, wrapper/nested rule present, “ready for user sign-off” present, “final ratified” / “user ratified” absent. |

### 2. Deepen `catalogue/inventory.md`

| | |
| --- | --- |
| **Paths** | `catalogue/inventory.md` (source tables: `sessions/2026.09.09-1009/02-research/codebase-findings.md`) |
| **Action** | Update method/scan-limits block (depth ≤2; cheap size excl. node_modules/.git/caches; band cutoffs S &lt;1MB · M &lt;50MB · L &lt;500MB · XL ≥500MB; count lower bound **32**). Extend top-level map with columns: **Cheap MB** (when known), **Band**, **Wrapper / git class**, **Activity / next hint**. Promote size-band mix summary (S=17, M=9, L=1 ProjetOrif, XL=2 WorkSpace/Obsidian). Clarify git-root section with wrapper pattern table (thin-wrapper-1git / multi-nested / top-git-flat / top-git+nested / no-git). Note HTTP Battles empty parent; `.env` path-only under NextPWATraining. Do **not** re-open secrets or deep-walk deps. Prefer copy/adapt from research — no new corpus mutation. |
| **Verify** | Inventory has band cutoffs + per-row bands for the 29 top-levels; scan limits explicit; secrets still path-only; date language says CreationTime wins for proposed labels. |

### 3. Add must-preserve draft

| | |
| --- | --- |
| **Paths** | **New:** `catalogue/must-preserve.md` · light cross-links from `catalogue/INDEX.md` (and optionally one line in `program/CHARTER.md` Default-protect section) |
| **Why this path** | Catalogue-facing candidate list for move fail-closed review; sits beside INDEX/inventory. Program charter keeps locked default-protect rule and **points** to the draft rather than owning the long candidate table. |
| **Action** | Create draft labelled **draft — not auto-locked / for user review**. Include: locked default-protect org repo; High: Obsidian, ProjetOrif; Medium-high: WebCatalogue; Medium: WorkSpace, HTTP Battles (+ nested); Optional: CursorMobileWorkspace, NextPWATraining (opaque `.env`). State fail-closed until user reviews before first move-capable cycle. No secret contents. |
| **Verify** | File exists; draft language clear; default-protect called out separately from draft candidates. |

### 4. Update `catalogue/INDEX.md`

| | |
| --- | --- |
| **Paths** | `catalogue/INDEX.md` |
| **Action** | Sync **Legend** to taxonomy vocabulary (`active`/`paused`/`archive`/`protect`/`hygiene`); note statuses remain provisional until user assigns/ratifies. Keep “proposed labels ≠ renames” caveat. Optionally add a short note pointing to inventory size bands / must-preserve draft (do **not** require new columns for size if noisy — prefer notes or a one-line “see inventory”). Refresh **What’s next**: (1) user sign-off taxonomy + review must-preserve draft; (2) **primary next program row = Early/simple** after per-batch approval; (3) Git-strategy hard gate before Obsidian/ProjetOrif/worktrees. **Do not** mass-replace `TBD` with guessed statuses (optional later; avoid over-claiming). Row notes may lightly echo Early/simple / after-git-strategy where already present. |
| **Verify** | Legend matches taxonomy; What’s next names Early/simple primary + Git-strategy gate; Cycle 0-only “optional Cycle 1” text removed/updated. |

### 5. Update `program/ROADMAP.md`

| | |
| --- | --- |
| **Paths** | `program/ROADMAP.md` |
| **Action** | Add **Cycle 1 complete** note (docs follow-ups done this session; taxonomy proposed-ratified pending user sign-off). Reorder / annotate suggested-order table so **primary next = Early/simple** (list the six folders). Keep **Git-strategy** as hard-gate section/reminder — **not** the primary next row. Retire “Docs follow-ups / Cycle 1+ optional” as the current next action (or mark done). Update “How the next cycle starts” for post–Cycle 1 (review sign-off + choose Early/simple batch or git-strategy when needed). State Cycle 1 did not execute moves. |
| **Verify** | Early/simple is clearly primary next; Git-strategy still mandatory before complex git moves; Cycle 1 marked done. |

### 6. Consistency touch — `organisation-approach.md` / `CHARTER.md`

| | |
| --- | --- |
| **Paths** | `program/organisation-approach.md` (required light edit); `program/CHARTER.md` (only if a one-line Cycle/must-preserve pointer is missing) |
| **Action** | **organisation-approach.md:** Align status buckets to locked `active`/`paused`/`archive` (+ INDEX specials); remove PARA-lite as an open program alternative (may note rejected/deferred). Add one-line Cycle 1 note: taxonomy proposed-ratified pending sign-off; still no moves. **CHARTER.md:** Touch only for consistency — e.g. cycle framing “0+1 docs”; link `catalogue/must-preserve.md` from Default-protect/must-preserve section if it still implies “list TBD only”. Do **not** rewrite charter end-state or re-open Cycle 0 locks. |
| **Verify** | No doc still presents PARA-lite as the open status choice; charter still forbids unsupervised FS mutation. |

### 7. Session implementation artefacts

| | |
| --- | --- |
| **Paths** | `sessions/2026.09.09-1009/04-implementation/log.md`, `changes.md` |
| **Action** | After edits: log what changed, sources used (research paths), mutation_class attestation (`docs_only`; zero corpus FS mutations), secrets policy followed, no push. `changes.md`: file-level bullet list of org-repo paths added/modified. |
| **Verify** | Both files non-empty; attestation present; no secret quotes. |

### Push / auth

**Not in scope.** No dual preflight. Do not commit or push unless the user separately asks (out of this plan’s AC).

## Non-goals

- Any FS mutation under `C:\Project` (moves, renames, deletes, mkdir reorg)
- Executing Early/simple move batch or git-strategy FAW deliverables
- Claiming **final** user ratification of taxonomy or locking must-preserve without user review
- Deep `node_modules` / cache inventory; opening `.env` / credentials
- Mass provisional INDEX status assignment (optional only; default leave `TBD`)
- Re-litigating Cycle 0 locks; marking the whole organisation program complete
- `git push` / remote publish

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Wording implies final taxonomy ratification | Use exact phrase **proposed-ratified — ready for user sign-off**; auditor greps for overclaim |
| Scope creep into move/git-strategy work | Steps are docs-only; ROADMAP pointers only |
| Proposed labels mistaken for renames | INDEX + taxonomy caveats retained |
| Cheap size understates disk | Document metric + exclusions in inventory |
| Must-preserve draft treated as auto-locked | Explicit draft label; CHARTER/INDEX fail-closed until review |
| Accidental corpus edit | Implementer only writes under org repo + session; auditor path check |
| Inconsistent PARA-lite leftover | Step 6 removes open PARA alternative |

**Rollback:** revert org-repo doc commits/files via git; no corpus rollback needed if docs_only held.

## Ready to implement

**yes**

## Blocking questions

**none** — Cycle 1 decisions locked in prompt/notes; research has no docs_only blockers; publish N/A.

## Hand-off notes for implementer

- Prefer promoting tables from `02-research/codebase-findings.md` over re-scanning.
- Size bands / activity signals are “include when cheap” — research already computed them; use those numbers.
- After planner → implementer: **no extra user approval gate** (docs_only). User sign-off of taxonomy / must-preserve happens **after** this cycle’s docs land.
- Primary next suggestion text for ROADMAP/INDEX: Early/simple set = `PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest`.
