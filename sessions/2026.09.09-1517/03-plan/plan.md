# Plan — Cycle 3 Early/simple remaining (fs_mutation)

**Session:** `sessions/2026.09.09-1517/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md` (+ `codebase-findings.md`)  
**Approach:** Research Option A + embedded Option B pre-checks — sequential same-volume `Move-Item` (whole trees), with existence / collision / `.git` re-scan immediately before each move.

---

## Goal

Finish ROADMAP **Early/simple remaining** by moving exactly three corpus-root folders (`IA`, `AngularTest`, `epsic`) under `C:\Project\archive\` with CreationTime date labels, updating catalogue INDEX (+ inventory) for those rows, and logging each forward path with reverse-move notes. **Do not move ZedTest** (already at `paused`; INDEX path accurate). Moves run only after the orchestrator obtains **explicit user plan-gate approval** of this map. No agent push/pull.

---

## What the user is approving (plan gate)

You are approving **this exact three-folder move map** (not “finish the cycle” in general, and not the earlier Choose-all on Q1–Q6). After you say **yes**, the implementer will relocate these folders on disk and update catalogue docs to match.

| Approve? | Meaning |
| --- | --- |
| **Yes** | Ensure `C:\Project\archive` exists (create if missing); move the three sources to the destinations below; update INDEX (+ inventory); leave ZedTest, Cycle 2 destinations, must-preserve draft paths, and the org repo alone. |
| **No / edit** | No moves; revise the map or defer until a new plan. |

**Pros**

- Completes the Early/simple remaining row with the same dated `archive\` layout as Cycle 2 siblings.
- Research found no `.git` and no destination collisions; whole-tree moves keep zip + extract together for AngularTest / epsic.
- Catalogue paths catch up so INDEX stops showing stale root locations for these three.

**Cons / tradeoffs**

- **Paths change** — bookmarks, shortcuts, open terminals, or scripts pointing at `C:\Project\IA`, `C:\Project\AngularTest`, or `C:\Project\epsic` will break until updated.
- `archive` parent may already exist (Cycle 2); if missing it will be created under `C:\Project`.
- Batch is **not transactional** across three rows: if one fails mid-way, already-moved items may need reverse-move (documented per row).
- AngularTest / epsic are M-band (larger than typical Cycle 2 S-band) — longer move time / higher chance of a transient file lock.

Prior “Choose all” / starting this FAW / Cycle 2 approval is **not** this approval. Orchestrator must pause here and obtain an explicit yes on this plan/map before launching implementer.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | `fs_mutation` |
| Batch name | Cycle 3 Early/simple remaining (IA, AngularTest, epsic) |
| Corpus FS | Intentional moves of the three approved source trees only; create `C:\Project\archive` if missing |
| User approval before implementer | **Required** — plan-gate on this map (orchestrator pause) |
| Docs attestation after moves | INDEX (+ inventory) updated for moved rows; ZedTest path verify-only (no move) |
| Push / remote publish | **Not required** — dual auth/preflight N/A |

### First-move / Early-simple gates (documented)

Per refined prompt + `01-prompt-betterment/notes.md` Answers (do not re-litigate):

| Gate | Status for this cycle |
| --- | --- |
| Taxonomy binding for Early/simple moves | **Satisfied via Q3=A** — **proposed-ratified — ready for user sign-off**; Early/simple binding + optional continuity note **user-validated for Early/simple (2026.09.09)** — **not** global final corpus ratification |
| Must-preserve | **Satisfied via Q4=A** — draft list **untouched** / **draft — not auto-locked / for user review**; batch folders **not** on draft list; org repo **protect** |
| Per-batch path list | **This plan’s move map** — still needs **explicit user plan-gate yes** before implementer |

**Remaining gate before implementer:** user plan-map approval only (see section above).

---

## Explicit move map (matches research — no deviation)

| # | Source | Status (Q5) | Destination |
| --- | --- | --- | --- |
| 1 | `C:\Project\IA` | `archive` | `C:\Project\archive\2025.12.12 - IA` |
| 2 | `C:\Project\AngularTest` | `archive` | `C:\Project\archive\2025.08.07 - AngularTest` |
| 3 | `C:\Project\epsic` | `archive` | `C:\Project\archive\2025.12.10 - epsic` |

**Parents:** create `C:\Project\archive` **if missing** (research: already present from Cycle 2). `paused` / `active` not required for this batch.

**Unit:** whole top-level folder tree per row (`Move-Item -LiteralPath`). Keep AngularTest zip + extract together; keep epsic `BDD\` / `HTML\` / `BDD.zip` together; never delete payload to “clean up.”

### Verify only — do not move

| Path | Action |
| --- | --- |
| `C:\Project\paused\2026.06.30 - ZedTest` | Confirm still present; **no move** |
| `C:\Project\ZedTest` | Confirm absent; **no corrective move** |

**Out of map (do not move):** ZedTest; Cycle 2 destinations (`PostManResponses`, `PlayTestTristan`); must-preserve draft paths; organisation repo; hygiene orphans; any other ROADMAP row / Medium / multi-experiment / Obsidian / ProjetOrif.

---

## Acceptance criteria

### Before implementer (orchestrator / plan gate)

- [ ] `notes.md` Answers lock Q1–Q6 (no open “Choose”).
- [ ] Plan contains the exact three-row move map above and declares `fs_mutation`.
- [ ] User **explicitly** approved this plan/map in-session (plan gate).
- [ ] Research noted: sources exist; targets absent; `.git` re-scan planned; ZedTest at paused path (no move).

### After implementer (auditor-checkable)

- [ ] Exactly the three approved folders moved once; **not** ZedTest or any out-of-map path.
- [ ] Preflight at implement: sources existed; targets did not; unexpected `.git` → that item **skipped + logged** (fail-closed; no git-strategy invent).
- [ ] Post: sources absent; targets present at destinations above (or user-approved edits only).
- [ ] Parent `C:\Project\archive` exists (created if it was missing).
- [ ] `catalogue/INDEX.md`: Status `archive`; date label applied (drop “proposed”); **current path** → destinations for IA / AngularTest / epsic; ZedTest path remains `C:\Project\paused\2026.06.30 - ZedTest`.
- [ ] `catalogue/inventory.md` path/status notes refreshed for the three moved rows (and Early/simple list if it still implies root paths).
- [ ] Optional taxonomy note only: **user-validated for Early/simple (2026.09.09)** continuity; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- [ ] Implementation log lists each `from → to` and **reverse-move** notes; skips explained; ZedTest verify result recorded.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied for already-moved rows); cycle not marked complete with unmet AC.
- [ ] No agent `git push` / `git pull` / remote publish attempted for this cycle.

**Not hard AC:** size metadata “if cheap” — do not false-fail audit on size fields.

---

## Ordered steps

### Step 0 — Orchestrator plan gate (blocking)

- **Paths:** this `plan.md`
- **Action:** Present move map + “What the user is approving” (plain language + pros/cons); obtain explicit yes (or edited map). Do **not** start implementer without yes.
- **Verify:** Session note or handoff records plan-gate approval.

### Step 1 — Implementer preflight (fail-closed)

- **Paths:** three sources + three destinations + `C:\Project\archive`; ZedTest verify paths
- **Action:** Confirm ZedTest still at paused path / root absent (log only). For each move row: `Test-Path` source exists; destination absent; parent will be directory. Recurse-scan each source for `.git` (top or nested). If unexpected `.git` → **skip that item**, log, do not invent git-strategy. If destination exists → **do not overwrite**; skip + log.
- **Verify:** Preflight table in `04-implementation/log.md`.

### Step 2 — Create archive parent if needed

- **Paths:** `C:\Project\archive`
- **Action:** `New-Item -ItemType Directory` if missing. Do not create `paused` / `active` for this batch.
- **Verify:** `archive` exists as a directory.

### Step 3 — Move trees (sequential)

- **Paths:** move map rows 1 → 2 → 3
- **Action:** Prefer `Move-Item -LiteralPath <source> -Destination <destination>` (rename-in-move into parent). Same volume; whole tree; no copy-delete; secrets/deps opaque (do not open). On failure: stop further moves; reverse already-successful rows if Critical (see rollback).
- **Verify:** After each row: source gone, destination present.

### Step 4 — Catalogue updates (org repo docs only)

- **Paths:**
  - `catalogue/INDEX.md` — three rows: Status `archive`; date label applied; current path → destinations; ZedTest unchanged; refresh “What’s next” if Early/simple remaining is done.
  - `catalogue/inventory.md` — refresh path/status notes for IA / AngularTest / epsic (and Early/simple bullet if still listing them as root-only).
  - `catalogue/taxonomy.md` — optional continuity note only; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- **Action:** Edit docs to match disk; no other catalogue churn; do not touch must-preserve draft list.
- **Verify:** Grep/read shows three new archive paths; ZedTest still paused; org-repo protect row unchanged.

### Step 5 — Session implementation log

- **Paths:** `sessions/2026.09.09-1517/04-implementation/log.md` (+ `changes.md` as usual)
- **Action:** Record each `from → to`, skip reasons, ZedTest verify, and **reverse-move** commands/paths (table below). Attest: zero intentional moves outside the approved map; zero corpus deletes of payload.
- **Verify:** Log complete before claiming implementation done.

### Step 6 — Auditor

- **Action:** Check acceptance criteria checklist against disk + catalogue + log.
- **Verify:** Pass / fail with evidence; Critical unmet → not complete.

**Push / pull preflight:** skipped (N/A — no remote publish).

---

## Non-goals

- Moving or re-moving ZedTest / Cycle 2 archive destinations
- Touching must-preserve draft paths (Obsidian, ProjetOrif, WebCatalogue, WorkSpace, HTTP Battles, …)
- Relocating or restructuring the organisation repo
- Git-strategy / treating unexpected `.git` as anything other than skip+log
- Hygiene orphans, Medium / multi-experiment / Obsidian batches
- Agent remote push, pull, or history rewrite
- Claiming global final taxonomy or must-preserve ratification beyond Early/simple continuity wording

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Unexpected `.git` at implement time | Fail-closed: skip that item; log; no git-strategy |
| Target collision | Skip overwrite; log; do not merge |
| File lock (esp. larger epsic) | Retry once or skip+log |
| Partial batch (1–2 of 3 moved) | Per-row reverse-move; on Critical failure reverse already-moved rows before marking complete |
| Catalogue drift after FS move | Steps 4–5 same acceptance batch as moves |
| Accidental ZedTest re-move | Explicit non-goal + Step 1 verify-only |
| Path bookmarks break | Called out in plan-gate pros/cons; user accepts by approving |

### Reverse-move notes (encode in implementation log)

| Forward | Reverse (do not delete payload) |
| --- | --- |
| `C:\Project\IA` → `C:\Project\archive\2025.12.12 - IA` | Move back to `C:\Project\IA` |
| `C:\Project\AngularTest` → `C:\Project\archive\2025.08.07 - AngularTest` | Move back to `C:\Project\AngularTest` |
| `C:\Project\epsic` → `C:\Project\archive\2025.12.10 - epsic` | Move back to `C:\Project\epsic` |

Empty `archive` parent may remain after reverse (harmless).

**Critical rollback policy:** If a move succeeds then a later hard failure leaves AC unmet, reverse already-moved rows using the table above, document in log, do not mark cycle complete.

---

## Verification checklist (auditor quick list)

1. Sources absent; destinations present for all non-skipped rows.  
2. Skipped rows (if any) have `.git` or collision evidence in log.  
3. ZedTest still at `C:\Project\paused\2026.06.30 - ZedTest`; root `ZedTest` absent.  
4. INDEX + inventory updated for the three moved rows only.  
5. Org repo / must-preserve draft paths untouched.  
6. Reverse-move notes present for each successful move.  
7. No push/pull attempted.

---

## Ready to implement

| Field | Value |
| --- | --- |
| Plan complete | **yes** |
| `ready_to_implement` | **yes** *(plan artifact complete — implementer still blocked until plan gate)* |
| `requires_user_plan_gate` | **yes** |
| Research blockers | none |
| Push blockers | none (N/A) |

**Orchestrator rule:** Even though `ready_to_implement: yes`, **do not** launch implementer until the user explicitly approves this plan/move map in-session. Choose all / prior Cycle 2 consent is insufficient.

## Blocking questions

**none** for plan content.  
**Process:** awaiting user plan-gate approval (orchestrator).
