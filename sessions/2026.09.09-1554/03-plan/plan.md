# Plan — Cycle 5 Medium wrappers (safer-three remaining, fs_mutation)

**Session:** `sessions/2026.09.09-1554/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md` (+ `codebase-findings.md`)  
**Approach:** Research **Option A** — sequential same-volume `Move-Item` of all three green safer wrappers (nested `.git` + opaque `.env` included), with existence / collision / nested-git hazard re-scan immediately before each move. Soft-deferred pair stays at root.

---

## Goal

Continue ROADMAP **Medium wrappers** (**in progress**) with the **safer-three remaining** subset: relocate exactly `NextTest`, `Simpl_Next`, and `PWAExempleTristan` under `C:\Project\archive\` with CreationTime date labels, keeping each nested `.git` under the wrapper as one atomic unit and carrying opaque `.env` paths unread. Update catalogue INDEX (+ inventory) for those three rows, attest destination nested-git and `.env` paths via `Test-Path`, and log each forward path with reverse-move notes. Leave soft-deferred `NextPWATraining` and `CursorMobileWorkspace` at root; do not re-move Cycle 4 archives. After this batch, ROADMAP Notes must show **Medium remaining = 2** (soft-deferred). Moves run only after the orchestrator obtains **explicit user plan-gate approval** of this map. No agent push/pull.

---

## What the user is approving (plan gate)

You are approving **this exact three-folder move map** (not “finish Medium wrappers,” and not the earlier Choose-all / Continuity on Q1–Q4). After you say **yes**, the implementer will relocate these folders on disk and update catalogue + ROADMAP notes to match.

| Approve? | Meaning |
| --- | --- |
| **Yes** | Ensure `C:\Project\archive` exists (already present per research; create only if missing); move the three sources to the destinations below **including** each nested git repo and any `.env` files; update INDEX (+ inventory) for those three rows; update ROADMAP so Medium stays **in progress** with **two** soft-deferred remaining; leave `NextPWATraining`, `CursorMobileWorkspace`, Cycle 4 archives, must-preserve draft paths, and the org repo alone. |
| **No / edit** | No moves; revise the map or defer until a new plan. |

**Pros**

- Clears the safer Medium pool (all three live-check green: single nested HTTPS `.git`, no worktree/multi-remote hazards, no target collisions).
- Same dated `archive\` layout as Cycle 4 / Early-simple siblings — consistent filing.
- Catalogue paths catch up so INDEX stops showing stale root locations for these three.
- Leaves higher-risk soft-deferred peers (`NextPWATraining` SSH+`.env`, `CursorMobileWorkspace` within-90d → `paused`) for a later, scoped cycle.
- After this batch, Medium row can focus only on the remaining **two** soft-deferred names.

**Cons / tradeoffs**

- **Paths change** — bookmarks, open terminals, IDE workspaces, or scripts pointing at `C:\Project\NextTest`, `C:\Project\Simpl_Next`, or `C:\Project\PWAExempleTristan` will break until updated.
- Nested remotes stay as-is (no rewrite); local clone paths change only on disk — any absolute local tooling paths may need refresh.
- All three carry opaque `.env` paths under nested trees — they move with the folder **unread** (path strings only in logs).
- Trees are **L-band (~600 MB each)** — moves take longer than Cycle 4’s S-band subset; prefer single atomic rename, avoid partial copy.
- Batch is **not transactional** across three rows: if one fails mid-way, already-moved items may need reverse-move (documented per row).
- Medium wrappers row is **not Complete** after this — two soft-deferred folders remain at root.

Prior “Choose all” / Continuity / starting this FAW is **not** this approval. Orchestrator must pause here and obtain an explicit yes on this plan/map before launching implementer.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | `fs_mutation` |
| Batch name | Cycle 5 Medium wrappers — safer-three remaining (NextTest, Simpl_Next, PWAExempleTristan) |
| Corpus FS | Intentional moves of the three approved wrapper trees only (nested `.git` + opaque `.env` included); `C:\Project\archive` parent already exists (create only if missing) |
| User approval before implementer | **Required** — plan-gate on this map (orchestrator pause) |
| Docs attestation after moves | INDEX (+ inventory) updated for the three moved rows; soft-deferred two remain root/`TBD`; ROADMAP Notes → remaining = 2 soft-deferred; Cycle 4 archive rows verify-only |
| Push / remote publish | **Not required** — dual auth/preflight N/A |

### Continuity / first-move gates (documented)

Per refined prompt + `01-prompt-betterment/notes.md` Answers (do **not** re-litigate global taxonomy/must-preserve for this Medium continuity cycle):

| Gate | Status for this cycle |
| --- | --- |
| Taxonomy binding for Medium moves | **Satisfied via Continuity Q3=A** — **proposed-ratified — ready for user sign-off**; Early/simple-style binding reused for Medium this cycle — **not** global final corpus ratification |
| Must-preserve | **Satisfied via Continuity Q3=A** — draft list **untouched** / **draft — not auto-locked / for user review**; batch folders **not** on draft list; org repo **protect**; soft-deferred peers stay out of this map |
| Per-batch path list | **This plan’s move map** — still needs **explicit user plan-gate yes** before implementer |

**Remaining gate before implementer:** user plan-map approval only (see section above).

---

## Explicit move map (matches research Option A — no deviation)

| # | Source | Status (90d rule) | Destination | Nested `.git` stays under |
| --- | --- | --- | --- | --- |
| 1 | `C:\Project\NextTest` | `archive` | `C:\Project\archive\2025.06.23 - NextTest` | `...\NextTest\.git` |
| 2 | `C:\Project\Simpl_Next` | `archive` | `C:\Project\archive\2025.06.23 - Simpl_Next` | `...\SimplNext\.git` |
| 3 | `C:\Project\PWAExempleTristan` | `archive` | `C:\Project\archive\2025.07.04 - PWAExempleTristan` | `...\PWATristan\.git` |

**Parents:** `C:\Project\archive` exists (research); create only if missing at implement. `paused` / `active` not required for this batch (all three → `archive`).

**Unit:** whole top-level wrapper tree per row (`Move-Item -LiteralPath`), including the single nested `.git` and any `.env`. Prefer rename/move over copy+delete; never delete payload to “clean up.” Secrets/deps opaque — do not open `.env` (path-only logging OK).

### Secrets / opaque payload (path-only; never read)

| Item | Opaque path (relative under source wrapper) | Handling |
| --- | --- | --- |
| NextTest | `NextTest\app-test\.env` | Move with tree; **never read or log contents**; post-move `Test-Path` destination path only |
| Simpl_Next | `SimplNext\simpl-app\.env` | Same |
| PWAExempleTristan | `PWATristan\pwa-tristan-app\.env` | Same |

### Destination attestation (implementer AC — required)

After each successful move, attest with `Test-Path` (boolean only; no file open):

| Destination nested `.git` | Destination opaque `.env` |
| --- | --- |
| `C:\Project\archive\2025.06.23 - NextTest\NextTest\.git` | `C:\Project\archive\2025.06.23 - NextTest\NextTest\app-test\.env` |
| `C:\Project\archive\2025.06.23 - Simpl_Next\SimplNext\.git` | `C:\Project\archive\2025.06.23 - Simpl_Next\SimplNext\simpl-app\.env` |
| `C:\Project\archive\2025.07.04 - PWAExempleTristan\PWATristan\.git` | `C:\Project\archive\2025.07.04 - PWAExempleTristan\PWATristan\pwa-tristan-app\.env` |

Log: path + `True`/`False` only. If nested `.git` missing post-move → Critical for that row. If `.env` was present pre-move and absent post-move → Critical for that row.

### Fail-closed unexpected hazards (implementer re-scan)

Immediately before each move, re-check. On any of the following → **skip that item + log**; do **not** invent git-strategy mid-batch; do **not** expand the map; do **not** substitute soft-deferred names:

- Destination already exists (no overwrite / merge)
- Source missing
- Unexpected **extra** nested `.git` beyond the expected single child repo
- Linked extra worktrees / multi-remote / unclear git layout that was not present at research
- Any path outside this approved map

Hard fail-closed items stay deferred/skipped; do not substitute another Medium folder without a new plan gate.

### Soft-deferred (remain at root — non-goals for this cycle)

| Folder | Reason (Q2=A + research) |
| --- | --- |
| `NextPWATraining` | Soft-deferred; SSH remote + `.env`; **do not move** |
| `CursorMobileWorkspace` | Soft-deferred; LastWrite within 90d → would be `paused`; **do not move** |

**After this batch:** Medium remaining = **these two only**.

### Verify only — do not move

| Path / set | Action |
| --- | --- |
| Cycle 4 archives: `archive\2025.06.25 - TestRyan`, `archive\2025.08.12 - ReactRouterTest`, `archive\2025.06.05 - Simpl` | Confirm still present; **no re-move** |
| Soft-deferred two above | Confirm still at root; **no move this cycle** |
| Early/simple archive/paused destinations | Confirm still present; **no re-move** |

**Out of map (do not move):** soft-deferred two; Cycle 4 / Early-simple trees; must-preserve draft paths; organisation repo; hygiene orphans; multi-experiment / Obsidian / ProjetOrif / special-git rows.

---

## Acceptance criteria

### Before implementer (orchestrator / plan gate)

- [ ] `notes.md` Answers lock Q1–Q4 (no open “Choose”).
- [ ] Research live-checked in-scope safer three; INDEX vs disk noted; Cycle 4 archives and soft-deferred pair not treated as move sources.
- [ ] Plan shortlist is explicit: `NextTest`, `Simpl_Next`, `PWAExempleTristan` (Option A — all three green).
- [ ] Plan contains the exact three-row move map above, declares `fs_mutation`, and states atomic nested-git + opaque-secrets handling.
- [ ] Soft-deferred two listed with reasons; shortlist does not silently add them.
- [ ] User **explicitly** approved this plan/map in-session (plan gate).

### After implementer (auditor-checkable)

- [ ] Exactly the three approved folders moved once; **no** extras outside the approved map; **no** Cycle 4 re-moves; **no** soft-deferred moves.
- [ ] Preflight at implement: sources existed; targets did not; each wrapper still contains its expected nested `.git` after move (if present pre-move).
- [ ] Post: sources absent; targets present at destinations above (or user-approved edits only).
- [ ] **Destination nested-git attestation:** `Test-Path` True for each expected destination `.git` path above.
- [ ] **Opaque `.env` attestation:** for each row where source `.env` `Test-Path` was True pre-move, destination `.env` `Test-Path` True post-move; **no secret contents** in session logs.
- [ ] Unexpected hazards → item **skipped + logged** (fail-closed; no git-strategy invent; no silent substitute).
- [ ] Parent `C:\Project\archive` exists.
- [ ] `catalogue/INDEX.md`: Status `archive`; date label applied (drop “proposed”); **current path** → destinations for the three moved rows; soft-deferred two unchanged at root/`TBD`; Cycle 4 archive rows unchanged.
- [ ] `catalogue/inventory.md` path/status notes refreshed for the three moved rows (and nested-path bullets if they still imply root-only wrappers).
- [ ] Optional taxonomy note only: Continuity for Medium; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- [ ] `program/ROADMAP.md` Notes / “How the next cycle starts”: Medium row stays **in progress**; **remaining = 2** soft-deferred (`NextPWATraining`, `CursorMobileWorkspace`); do **not** mark Medium Complete; do **not** jump Primary next.
- [ ] Implementation log lists each `from → to`, nested-git + `.env` attestations, skip reasons, soft-deferred note, and **reverse-move** notes.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied for already-moved rows); cycle not marked complete with unmet AC.
- [ ] No agent `git push` / `git pull` / remote publish attempted for this cycle.

**Not hard AC:** size / cheap-band metadata “if available” — include when cheap (live L ~600 MB is duration signal only); do not false-fail audit on size fields.

---

## Ordered steps

### Step 0 — Orchestrator plan gate (blocking)

- **Paths:** this `plan.md`
- **Action:** Present move map + “What the user is approving” (plain language + pros/cons); obtain explicit yes (or edited map). Do **not** start implementer without yes.
- **Verify:** Session note or handoff records plan-gate approval.

### Step 1 — Implementer preflight (fail-closed)

- **Paths:** three sources + three destinations + `C:\Project\archive`; expected nested `.git` and opaque `.env` paths from the move map; soft-deferred two; Cycle 4 archive destinations
- **Action:** For each move row: `Test-Path` source exists; destination absent; parent will be directory. Confirm expected nested `.git` still present under the sole child. Record pre-move opaque `.env` `Test-Path` (boolean only). Re-probe worktree/remote hazard screen lightly (or equivalent recurse + `git worktree list` / `remote -v` at nested root). If unexpected `.git` / worktrees / multi-remote / collision → **skip that item**, log, do not invent git-strategy, do not substitute soft-deferred. Confirm soft-deferred two still at root (log only). Confirm Cycle 4 archive destinations present and not re-targeted.
- **Verify:** Preflight table in `04-implementation/log.md`.

### Step 2 — Create archive parent if needed

- **Paths:** `C:\Project\archive`
- **Action:** `New-Item -ItemType Directory` if missing. Do not create `paused` / `active` for this batch.
- **Verify:** `archive` exists as a directory.

### Step 3 — Move trees (sequential)

- **Paths:** move map rows 1 → 2 → 3
- **Action:** Prefer `Move-Item -LiteralPath <source> -Destination <destination>` (rename-in-move into parent). Same volume; whole wrapper including nested `.git` + opaque `.env`; no copy-delete; secrets/deps opaque (do not open). Expect longer duration (L-band). On failure: stop further moves; reverse already-successful rows if Critical (see rollback).
- **Verify:** After each row: source gone; destination present; nested `.git` still under expected relative child path; destination `.env` `Test-Path` matches pre-move presence.

### Step 4 — Destination attestation

- **Paths:** destination nested `.git` + `.env` table above
- **Action:** `Test-Path` each listed path; record True/False in log only (no file open/read).
- **Verify:** All expected nested `.git` True; `.env` True wherever pre-move was True.

### Step 5 — Catalogue updates (org repo docs only)

- **Paths:**
  - `catalogue/INDEX.md` — three rows: Status `archive`; date label applied; current path → destinations; leave soft-deferred two at root/`TBD`; leave Cycle 4 archive rows as-is; refresh “What’s next” Medium remaining count to soft-deferred two.
  - `catalogue/inventory.md` — refresh path/status notes for NextTest / Simpl_Next / PWAExempleTristan (and nested-path bullets that still list root-relative wrappers for those three).
  - `catalogue/taxonomy.md` — optional Continuity note only; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- **Action:** Edit docs to match disk; no other catalogue churn; do not touch must-preserve draft list; do not claim Medium row Complete.
- **Verify:** Grep/read shows three new archive paths; soft-deferred two still root; Cycle 4 archives unchanged; org-repo protect row unchanged.

### Step 6 — ROADMAP partial progress

- **Paths:** `program/ROADMAP.md`
- **Action:** Update Medium wrappers Notes + “How the next cycle starts”: Cycle 5 moved safer three → `archive`; **remaining (2):** `NextPWATraining`, `CursorMobileWorkspace` (soft-deferred). Keep row **in progress** / Primary next still Medium wrappers. Do **not** mark Complete; do **not** jump to Multi-experiment.
- **Verify:** Remaining names = soft-deferred pair only; row not Complete.

### Step 7 — Session implementation log

- **Paths:** `sessions/2026.09.09-1554/04-implementation/log.md` (+ `changes.md` as usual)
- **Action:** Record each `from → to`, nested `.git` + `.env` attestations, skip reasons, soft-deferred + Cycle 4 verify-only notes, and **reverse-move** commands/paths (table below). Attest: zero intentional moves outside the approved map; zero corpus deletes of payload; no secret contents logged.
- **Verify:** Log complete before claiming implementation done.

### Step 8 — Auditor

- **Action:** Check acceptance criteria checklist against disk + catalogue + ROADMAP + log.
- **Verify:** Pass / fail with evidence; Critical unmet → not complete.

**Push / pull preflight:** skipped (N/A — no remote publish).

---

## Non-goals

- Moving soft-deferred `NextPWATraining` or `CursorMobileWorkspace`
- Completing the entire Medium wrappers ROADMAP row this cycle
- Re-moving or re-proposing Cycle 4 archives (`TestRyan`, `ReactRouterTest`, `Simpl`)
- Reopening or re-moving Early/simple Cycle 2–3 destinations
- Jumping to Multi-experiment / Primary next while Medium soft-deferred names remain
- Touching must-preserve draft paths (Obsidian, ProjetOrif, WebCatalogue, WorkSpace, HTTP Battles, …)
- Relocating or restructuring the organisation repo
- Git-strategy / treating unexpected hazards as anything other than skip+log
- Hygiene orphans, multi-experiment / Obsidian / ProjetOrif / special-git batches
- Agent remote push, pull, or history rewrite / filter-repo / splitting wrapper from nested git
- Claiming global final taxonomy or must-preserve ratification beyond Continuity wording
- Fixing all INDEX drift for non-batch rows (honesty only)
- Reading or logging secret file contents

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Unexpected nested `.git` / worktree / multi-remote at implement time | Fail-closed: skip that item; log; no git-strategy; no soft-deferred substitute |
| Target collision | Skip overwrite; log; do not merge |
| File lock / long L-band move | Prefer single `Move-Item`; retry once or skip+log; do not copy+delete |
| Partial batch (1–2 of 3 moved) | Per-row reverse-move; on Critical failure reverse already-moved rows before marking complete |
| Secret leakage via logs | Path-only for `.env`; never open/read contents; attestation = `Test-Path` boolean |
| Catalogue / ROADMAP drift after FS move | Steps 5–7 same acceptance batch as moves |
| Accidental soft-deferred / Cycle 4 move | Explicit non-goals + Step 1 verify-only |
| Path bookmarks break | Called out in plan-gate pros/cons; user accepts by approving |

### Reverse-move notes (encode in implementation log)

| Forward | Reverse (do not delete payload) |
| --- | --- |
| `C:\Project\NextTest` → `C:\Project\archive\2025.06.23 - NextTest` | Move dated folder back to `C:\Project\NextTest` |
| `C:\Project\Simpl_Next` → `C:\Project\archive\2025.06.23 - Simpl_Next` | Move dated folder back to `C:\Project\Simpl_Next` |
| `C:\Project\PWAExempleTristan` → `C:\Project\archive\2025.07.04 - PWAExempleTristan` | Move dated folder back to `C:\Project\PWAExempleTristan` |

Empty `archive` parent may remain after reverse (harmless). Nested `.git` and opaque `.env` ride with the wrapper on reverse (same atomic unit).

**Critical rollback policy:** If a move succeeds then a later hard failure leaves AC unmet, reverse already-moved rows using the table above, document in log, do not mark cycle complete.

---

## Verification checklist (auditor quick list)

1. Sources absent; destinations present for all non-skipped approved rows.  
2. Nested `.git` intact under expected relative child; destination `Test-Path` attested.  
3. Opaque `.env` destination `Test-Path` matches pre-move presence; no secret contents in logs.  
4. Skipped rows (if any) have hazard/collision evidence in log; no silent map expansion.  
5. Soft-deferred two still at `C:\Project\<Name>` root.  
6. Cycle 4 archive destinations untouched.  
7. INDEX + inventory updated for the three moved rows only.  
8. ROADMAP Medium **in progress**; remaining = 2 soft-deferred; not Complete.  
9. Org repo / must-preserve draft paths untouched.  
10. Reverse-move notes present for each successful move.  
11. No push/pull attempted.

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
