# Plan — Cycle 4 Medium wrappers (first subset, fs_mutation)

**Session:** `sessions/2026.09.09-1535/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md` (+ `codebase-findings.md`)  
**Approach:** Research **Option A** — sequential same-volume `Move-Item` of three whole wrapper trees (nested `.git` included), with existence / collision / nested-git hazard re-scan immediately before each move.

---

## Goal

Start ROADMAP **Medium wrappers** with a **small first move batch**: relocate exactly three lower-hazard corpus-root folders (`TestRyan`, `ReactRouterTest`, `Simpl`) under `C:\Project\archive\` with CreationTime date labels, keeping each nested `.git` under the wrapper as one atomic unit. Update catalogue INDEX (+ inventory) for those three rows only, and log each forward path with reverse-move notes. Defer the other five Medium wrappers to a later cycle. Moves run only after the orchestrator obtains **explicit user plan-gate approval** of this map. No agent push/pull.

---

## What the user is approving (plan gate)

You are approving **this exact three-folder move map** (not “finish Medium wrappers,” and not the earlier Choose-all on Q1–Q7). After you say **yes**, the implementer will relocate these folders on disk and update catalogue docs to match.

| Approve? | Meaning |
| --- | --- |
| **Yes** | Ensure `C:\Project\archive` exists (create if missing); move the three sources to the destinations below **including** each nested git repo; update INDEX (+ inventory) for those three rows; leave the five deferred Medium folders, Early/simple destinations, must-preserve draft paths, and the org repo alone. |
| **No / edit** | No moves; revise the map or defer until a new plan. |

**Pros**

- Starts Medium with the three simplest thin wrappers (S-band; single nested HTTPS `.git`; no worktree/multi-remote fails on research scan).
- Same dated `archive\` layout as Early/simple siblings — consistent filing.
- Catalogue paths catch up so INDEX stops showing stale root locations for these three.
- Leaves higher-hazard / optional must-preserve Medium peers (`CursorMobileWorkspace`, `NextPWATraining`, etc.) for a later, smaller review.

**Cons / tradeoffs**

- **Paths change** — bookmarks, open terminals, IDE workspaces, or scripts pointing at `C:\Project\TestRyan`, `C:\Project\ReactRouterTest`, or `C:\Project\Simpl` will break until updated.
- Nested remotes stay as-is (no rewrite); local clone paths change only on disk — any absolute local tooling paths may need refresh.
- `Simpl` carries an opaque `.env` path under the nested tree — it moves with the folder **unread** (path may still appear in logs as a path string only).
- Batch is **not transactional** across three rows: if one fails mid-way, already-moved items may need reverse-move (documented per row).
- Five Medium wrappers remain at root until a later cycle.

Prior “Choose all” / Continuity / starting this FAW is **not** this approval. Orchestrator must pause here and obtain an explicit yes on this plan/map before launching implementer.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | `fs_mutation` |
| Batch name | Cycle 4 Medium wrappers — first subset (TestRyan, ReactRouterTest, Simpl) |
| Corpus FS | Intentional moves of the three approved wrapper trees only (nested `.git` included); create `C:\Project\archive` if missing |
| User approval before implementer | **Required** — plan-gate on this map (orchestrator pause) |
| Docs attestation after moves | INDEX (+ inventory) updated for the three moved rows; five deferred Medium rows remain root/`TBD` until later |
| Push / remote publish | **Not required** — dual auth/preflight N/A |

### Continuity / first-move gates (documented)

Per refined prompt + `01-prompt-betterment/notes.md` Answers (do **not** re-litigate global taxonomy/must-preserve for this Medium continuity cycle):

| Gate | Status for this cycle |
| --- | --- |
| Taxonomy binding for Medium moves | **Satisfied via Continuity Q3=A** — **proposed-ratified — ready for user sign-off**; Early/simple-style binding reused for Medium this cycle — **not** global final corpus ratification |
| Must-preserve | **Satisfied via Continuity Q4=A** — draft list **untouched** / **draft — not auto-locked / for user review**; batch folders **not** on draft list; org repo **protect**; soft-deferred optional draft peers (`CursorMobileWorkspace`, `NextPWATraining`) stay out of this map |
| Per-batch path list | **This plan’s move map** — still needs **explicit user plan-gate yes** before implementer |

**Remaining gate before implementer:** user plan-map approval only (see section above).

---

## Explicit move map (matches research — no deviation)

| # | Source | Status (Q5) | Destination | Nested `.git` stays under |
| --- | --- | --- | --- | --- |
| 1 | `C:\Project\TestRyan` | `archive` | `C:\Project\archive\2025.06.25 - TestRyan` | `...\python-mini-jeux\.git` |
| 2 | `C:\Project\ReactRouterTest` | `archive` | `C:\Project\archive\2025.08.12 - ReactRouterTest` | `...\ReactRouterTest\.git` |
| 3 | `C:\Project\Simpl` | `archive` | `C:\Project\archive\2025.06.05 - Simpl` | `...\Project-Simpl\.git` |

**Parents:** create `C:\Project\archive` **if missing** (research: already present). `paused` / `active` not required for this batch (all three → `archive`).

**Unit:** whole top-level wrapper tree per row (`Move-Item -LiteralPath`), including the single nested `.git`. Prefer rename/move over copy+delete; never delete payload to “clean up.” Secrets/deps opaque — do not open `.env` under `Simpl` (path-only logging OK).

### Secrets / opaque payload

| Item | Handling |
| --- | --- |
| `Simpl\Project-Simpl\simpl-app\api\env\.env` | Move with tree; **never read or log contents**; destination path may be noted as path string only |
| `TestRyan` / `ReactRouterTest` | Research: no `.env` path — still do not fish for secrets |

### Fail-closed unexpected hazards (implementer re-scan)

Immediately before each move, re-check. On any of the following → **skip that item + log**; do **not** invent git-strategy mid-batch; do **not** expand the map:

- Destination already exists (no overwrite / merge)
- Source missing
- Unexpected **extra** nested `.git` beyond the expected single child repo
- Linked extra worktrees / multi-remote / unclear git layout that was not present at research
- Any path outside this approved map

Hard fail-closed items stay deferred/skipped; do not substitute another Medium folder without a new plan gate.

### Deferred Medium wrappers (remain at root — non-goals for this cycle)

| Folder | Reason (research) |
| --- | --- |
| `NextTest` | M-band + `.env`; not needed when safer S peers fill the 3-slot |
| `Simpl_Next` | M + `.env`; batch after first subset proves Medium moves |
| `PWAExempleTristan` | M + `.env`; second Medium batch |
| `CursorMobileWorkspace` | Within 90d → would need `paused\`; larger M; optional must-preserve draft — soft defer |
| `NextPWATraining` | SSH remote + INDEX-flagged `.env` + optional must-preserve draft — not this shortlist |

### Verify only — do not move

| Path | Action |
| --- | --- |
| Early/simple archive/paused destinations (Cycle 2–3) | Confirm still present; **no re-move** |
| Five deferred Medium roots above | Confirm still at root; **no move this cycle** |

**Out of map (do not move):** deferred five; Early/simple trees; must-preserve draft paths; organisation repo; hygiene orphans; multi-experiment / Obsidian / ProjetOrif / special-git rows.

---

## Acceptance criteria

### Before implementer (orchestrator / plan gate)

- [ ] `notes.md` Answers lock Q1–Q7 (no open “Choose”).
- [ ] Research live-checked candidates; INDEX vs disk noted; Early/simple not treated as Medium sources.
- [ ] Plan shortlist is explicit: `TestRyan`, `ReactRouterTest`, `Simpl` (Option A rationale).
- [ ] Plan contains the exact three-row move map above, declares `fs_mutation`, and states atomic nested-git + opaque-secrets handling.
- [ ] Deferred five listed with reasons; shortlist does not silently expand past plan-gate visibility.
- [ ] User **explicitly** approved this plan/map in-session (plan gate).

### After implementer (auditor-checkable)

- [ ] Exactly the three approved folders moved once; **no** extras outside the approved map.
- [ ] Preflight at implement: sources existed; targets did not; each wrapper still contains its expected nested `.git` after move (if present pre-move).
- [ ] Post: sources absent; targets present at destinations above (or user-approved edits only).
- [ ] Unexpected hazards → item **skipped + logged** (fail-closed; no git-strategy invent; no silent substitute).
- [ ] Parent `C:\Project\archive` exists (created if it was missing).
- [ ] `Simpl` opaque `.env`: if present at source, present under destination tree; **no secret contents** in session logs.
- [ ] `catalogue/INDEX.md`: Status `archive`; date label applied (drop “proposed”); **current path** → destinations for the three moved rows; deferred Medium rows unchanged at root/`TBD`.
- [ ] `catalogue/inventory.md` path/status notes refreshed for the three moved rows (and nested-path bullets if they still imply root-only wrappers).
- [ ] Optional taxonomy note only: Continuity for Medium; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- [ ] Implementation log lists each `from → to` and **reverse-move** notes; skips explained.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied for already-moved rows); cycle not marked complete with unmet AC.
- [ ] No agent `git push` / `git pull` / remote publish attempted for this cycle.

**Not hard AC:** size / cheap-band metadata “if available” — include when cheap; do not false-fail audit on size fields.

---

## Ordered steps

### Step 0 — Orchestrator plan gate (blocking)

- **Paths:** this `plan.md`
- **Action:** Present move map + “What the user is approving” (plain language + pros/cons); obtain explicit yes (or edited map). Do **not** start implementer without yes.
- **Verify:** Session note or handoff records plan-gate approval.

### Step 1 — Implementer preflight (fail-closed)

- **Paths:** three sources + three destinations + `C:\Project\archive`; expected nested `.git` paths from the move map
- **Action:** For each move row: `Test-Path` source exists; destination absent; parent will be directory. Confirm expected nested `.git` still present under the sole child. Re-probe worktree/remote hazard screen lightly (or equivalent recurse + `git worktree list` / `remote -v` at nested root). If unexpected `.git` / worktrees / multi-remote / collision → **skip that item**, log, do not invent git-strategy, do not substitute another folder. Confirm deferred five still at root (log only). Confirm Early/simple destinations not re-targeted.
- **Verify:** Preflight table in `04-implementation/log.md`.

### Step 2 — Create archive parent if needed

- **Paths:** `C:\Project\archive`
- **Action:** `New-Item -ItemType Directory` if missing. Do not create `paused` / `active` for this batch.
- **Verify:** `archive` exists as a directory.

### Step 3 — Move trees (sequential)

- **Paths:** move map rows 1 → 2 → 3
- **Action:** Prefer `Move-Item -LiteralPath <source> -Destination <destination>` (rename-in-move into parent). Same volume; whole wrapper including nested `.git`; no copy-delete; secrets/deps opaque (do not open). On failure: stop further moves; reverse already-successful rows if Critical (see rollback).
- **Verify:** After each row: source gone; destination present; nested `.git` still under expected relative child path.

### Step 4 — Catalogue updates (org repo docs only)

- **Paths:**
  - `catalogue/INDEX.md` — three rows: Status `archive`; date label applied; current path → destinations; leave deferred Medium rows at root/`TBD`; do not reopen Early/simple Completed wording incorrectly.
  - `catalogue/inventory.md` — refresh path/status notes for TestRyan / ReactRouterTest / Simpl (and nested-path bullets that still list root-relative wrappers for those three).
  - `catalogue/taxonomy.md` — optional Continuity note only; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- **Action:** Edit docs to match disk; no other catalogue churn; do not touch must-preserve draft list; do not claim Medium row Complete (five remain).
- **Verify:** Grep/read shows three new archive paths; deferred five still root; org-repo protect row unchanged.

### Step 5 — Session implementation log

- **Paths:** `sessions/2026.09.09-1535/04-implementation/log.md` (+ `changes.md` as usual)
- **Action:** Record each `from → to`, nested `.git` verify, skip reasons, deferred-five note, and **reverse-move** commands/paths (table below). Attest: zero intentional moves outside the approved map; zero corpus deletes of payload; no secret contents logged.
- **Verify:** Log complete before claiming implementation done.

### Step 6 — Auditor

- **Action:** Check acceptance criteria checklist against disk + catalogue + log.
- **Verify:** Pass / fail with evidence; Critical unmet → not complete.

**Push / pull preflight:** skipped (N/A — no remote publish).

---

## Non-goals

- Moving the deferred five: `NextTest`, `Simpl_Next`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining`
- Completing the entire Medium wrappers ROADMAP row this cycle
- Reopening or re-moving Early/simple Cycle 2–3 destinations
- Touching must-preserve draft paths (Obsidian, ProjetOrif, WebCatalogue, WorkSpace, HTTP Battles, …)
- Relocating or restructuring the organisation repo
- Git-strategy / treating unexpected hazards as anything other than skip+log
- Hygiene orphans, multi-experiment / Obsidian / ProjetOrif / special-git batches
- Agent remote push, pull, or history rewrite / filter-repo / splitting wrapper from nested git
- Claiming global final taxonomy or must-preserve ratification beyond Continuity wording
- Fixing all INDEX drift for non-batch Medium rows (honesty only)

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Unexpected nested `.git` / worktree / multi-remote at implement time | Fail-closed: skip that item; log; no git-strategy; no substitute folder |
| Target collision | Skip overwrite; log; do not merge |
| File lock during move | Retry once or skip+log |
| Partial batch (1–2 of 3 moved) | Per-row reverse-move; on Critical failure reverse already-moved rows before marking complete |
| Secret leakage via logs | Path-only for `.env`; never open/read contents |
| Catalogue drift after FS move | Steps 4–5 same acceptance batch as moves |
| Accidental deferred / Early/simple move | Explicit non-goals + Step 1 verify-only |
| Path bookmarks break | Called out in plan-gate pros/cons; user accepts by approving |

### Reverse-move notes (encode in implementation log)

| Forward | Reverse (do not delete payload) |
| --- | --- |
| `C:\Project\TestRyan` → `C:\Project\archive\2025.06.25 - TestRyan` | Move dated folder back to `C:\Project\TestRyan` |
| `C:\Project\ReactRouterTest` → `C:\Project\archive\2025.08.12 - ReactRouterTest` | Move dated folder back to `C:\Project\ReactRouterTest` |
| `C:\Project\Simpl` → `C:\Project\archive\2025.06.05 - Simpl` | Move dated folder back to `C:\Project\Simpl` |

Empty `archive` parent may remain after reverse (harmless). Nested `.git` rides with the wrapper on reverse (same atomic unit).

**Critical rollback policy:** If a move succeeds then a later hard failure leaves AC unmet, reverse already-moved rows using the table above, document in log, do not mark cycle complete.

---

## Verification checklist (auditor quick list)

1. Sources absent; destinations present for all non-skipped approved rows.  
2. Nested `.git` intact under expected relative child for each successful move.  
3. Skipped rows (if any) have hazard/collision evidence in log; no silent map expansion.  
4. Deferred five still at `C:\Project\<Name>` root.  
5. INDEX + inventory updated for the three moved rows only.  
6. Org repo / must-preserve draft paths untouched; no secret contents in logs.  
7. Reverse-move notes present for each successful move.  
8. No push/pull attempted.

---

## Ready to implement

| Field | Value |
| --- | --- |
| Plan complete | **yes** |
| `ready_to_implement` | **yes** *(plan artifact complete — implementer still blocked until plan gate)* |
| `requires_user_plan_gate` | **yes** |
| Research blockers | none |
| Push blockers | none (N/A) |

**Orchestrator rule:** Even though `ready_to_implement: yes`, **do not** launch implementer until the user explicitly approves this plan/move map in-session. Choose all / Continuity consent is insufficient.

## Blocking questions

**none** for plan content.  
**Process:** awaiting user plan-gate approval (orchestrator).
