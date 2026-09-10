# Plan — Cycle 6 Medium wrappers (soft-deferred finalization, fs_mutation)

**Session:** `sessions/2026.09.09-1612/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md` (+ `codebase-findings.md`)  
**Approach:** Research **Option A** — finalize both remaining soft-deferred wrappers: `NextPWATraining` → `archive`, `CursorMobileWorkspace` → `paused`. Sequential same-volume `Move-Item` (whole wrapper + nested `.git` + opaque `.env`), with existence / collision / nested-git hazard re-scan immediately before each move. After **both** succeed → Medium **Complete**; Primary next → **Multi-experiment**.

---

## Goal

Finalize ROADMAP **Medium wrappers** (**nearly complete**) by moving the **two soft-deferred remaining** folders only: relocate `NextPWATraining` under `C:\Project\archive\` and `CursorMobileWorkspace` under `C:\Project\paused\` with CreationTime date labels, keeping each nested `.git` under the wrapper as one atomic unit, carrying NextPWA’s opaque `.env` unread, and leaving SSH remotes path-only (no URL rewrite). Update catalogue INDEX (+ inventory) for those two rows, attest destination nested-git and `.env` paths via `Test-Path`, log each forward path with reverse-move notes, then mark Medium wrappers **Complete** and set Primary next → **Multi-experiment**. Do not re-move Cycle 4/5 archives; do not re-soft-defer by default. Moves run only after the orchestrator obtains **explicit user plan-gate approval** of this map. No agent push/pull.

---

## What the user is approving (plan gate)

You are approving **this exact two-folder move map** (not “finish Medium” in the abstract, and not the earlier Choose-all / Continuity on Q1–Q5). After you say **yes**, the implementer will relocate these folders on disk, update catalogue paths, and — if both moves succeed — mark the Medium wrappers ROADMAP row **Complete** and advance Primary next to **Multi-experiment**.

| Approve? | Meaning |
| --- | --- |
| **Yes** | Ensure parents `C:\Project\archive` and `C:\Project\paused` exist (already present per research; create only if missing); move the two sources to the destinations below **including** each nested git repo and NextPWA’s `.env` (unread); leave SSH `origin` on NextPWA **unchanged**; update INDEX (+ inventory) for those two rows; mark Medium **Complete** and Primary next → **Multi-experiment**; leave Cycle 4/5 archives, must-preserve draft paths, and the org repo alone. |
| **No / edit** | No moves; revise the map, drop one name, or defer until a new plan. Medium stays in progress until a later approved batch. |

**Pros**

- Clears the last two Medium soft-deferred names and completes the Medium wrappers ROADMAP row.
- Statuses match the locked 90-day rule (NextPWA → `archive`; CursorMobile → `paused`).
- Live-check hard fail-closed screen is clean for both (single nested `.git`, single main worktree, single `origin`, no target collisions).
- Catalogue paths catch up so INDEX stops showing stale root locations for these two.
- Unlocks the program’s next Primary row (**Multi-experiment**) without reopening Early/simple or re-touching Cycle 4/5 archives.

**Cons / tradeoffs**

- **Paths change** — bookmarks, open terminals, IDE workspaces, or scripts pointing at `C:\Project\NextPWATraining` or `C:\Project\CursorMobileWorkspace` will break until updated.
- **NextPWA SSH `origin` stays as-is** (`git@github.com:…`) — path-only move; no remote URL rewrite. Residual risk if local SSH tooling assumed the old disk path; agent will not push/pull or rewrite remotes.
- NextPWA carries an opaque `.env` under the nested tree — it moves **unread** (path strings only in logs). Any accidental open/read is a Critical process failure.
- NextPWA is **L-band (~380 MB)** — longer `Move-Item` than CursorMobile (~17 MB); prefer single atomic rename, avoid partial copy.
- Batch is **not transactional** across two rows: if one fails mid-way, already-moved items may need reverse-move (documented per row). Under Q5=A, at most one item may be skipped; then Medium stays **in progress** with that name remaining (no Complete / no Primary jump).
- Dual status parents (`archive` + `paused`) — intentional under Continuity status rule; not a single-bucket batch.

Prior “Choose all” / Continuity / starting this FAW is **not** this approval. Orchestrator must pause here and obtain an explicit yes on this plan/map before launching implementer.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | `fs_mutation` |
| Batch name | Cycle 6 Medium wrappers — soft-deferred finalization (NextPWATraining, CursorMobileWorkspace) |
| Corpus FS | Intentional moves of the two approved wrapper trees only (nested `.git` + opaque `.env` included); parents `archive` / `paused` already exist (create only if missing) |
| User approval before implementer | **Required** — plan-gate on this map (orchestrator pause) |
| Docs attestation after moves | INDEX (+ inventory) updated for the two moved rows; ROADMAP Medium → **Complete**; Primary next → **Multi-experiment** (only if both succeed) |
| Push / remote publish | **Not required** — dual auth/preflight N/A |

### Continuity / first-move gates (documented)

Per refined prompt + `01-prompt-betterment/notes.md` Answers (do **not** re-litigate global taxonomy/must-preserve for this Medium continuity cycle):

| Gate | Status for this cycle |
| --- | --- |
| Taxonomy binding for Medium moves | **Satisfied via Continuity Q2=A** — **proposed-ratified — ready for user sign-off**; Early/simple-style binding reused for Medium this cycle — **not** global final corpus ratification |
| Must-preserve | **Satisfied via Continuity Q2=A** — draft list **untouched** / **draft — not auto-locked / for user review**; batch folders **not** on draft list; org repo **protect** |
| Per-batch path list | **This plan’s move map** — still needs **explicit user plan-gate yes** before implementer |

**Remaining gate before implementer:** user plan-map approval only (see section above).

---

## Explicit move map (matches research Option A — no deviation)

| # | Source | Status (90d rule) | Destination | Nested `.git` stays under |
| --- | --- | --- | --- | --- |
| 1 | `C:\Project\NextPWATraining` | `archive` | `C:\Project\archive\2025.06.23 - NextPWATraining` | `...\blogr-nextjs-prisma\.git` |
| 2 | `C:\Project\CursorMobileWorkspace` | `paused` | `C:\Project\paused\2026.06.17 - CursorMobileWorkspace` | `...\CursorMobileWorkspace\.git` |

**Parents:** `C:\Project\archive` and `C:\Project\paused` exist (research); create only if missing at implement. `active` not required for this batch.

**Unit:** whole top-level wrapper tree per row (`Move-Item -LiteralPath`), including the single nested `.git` and any `.env`. Prefer rename/move over copy+delete; never delete payload to “clean up.” Secrets/deps opaque — do not open `.env` (path-only logging OK). **No SSH/remote URL rewrite** (path-only).

### Secrets / opaque payload (path-only; never read)

| Item | Opaque path (relative under source wrapper) | Handling |
| --- | --- | --- |
| NextPWATraining | `blogr-nextjs-prisma\.env` | Move with tree; **never read or log contents**; post-move `Test-Path` destination path only |
| CursorMobileWorkspace | *(none found depth≤5 at research)* | No `.env` attestation required unless preflight finds a path; if found, same opaque rules |

### Destination attestation (implementer AC — required)

After each successful move, attest with `Test-Path` (boolean only; no file open):

| Destination nested `.git` | Destination opaque `.env` |
| --- | --- |
| `C:\Project\archive\2025.06.23 - NextPWATraining\blogr-nextjs-prisma\.git` | `C:\Project\archive\2025.06.23 - NextPWATraining\blogr-nextjs-prisma\.env` |
| `C:\Project\paused\2026.06.17 - CursorMobileWorkspace\CursorMobileWorkspace\.git` | N/A unless preflight found `.env` (then path-only `Test-Path`) |

Log: path + `True`/`False` only. If nested `.git` missing post-move → Critical for that row. If NextPWA `.env` was present pre-move and absent post-move → Critical for that row.

### Fail-closed unexpected hazards (implementer re-scan)

Immediately before each move, re-check. On any of the following → **skip that item + log** (Q5=A: at most one defer); do **not** invent git-strategy mid-batch; do **not** expand the map; do **not** re-soft-defer both by default:

- Destination already exists (no overwrite / merge)
- Source missing
- Unexpected **extra** nested `.git` beyond the expected single child repo
- Linked extra worktrees / multi-remote / unclear git layout that was not present at research
- Any path outside this approved map

**SSH alone is not hard fail-closed** for NextPWA under Continuity (path-only; residual informational risk). Only skip NextPWA for SSH if the user forces Option B (“any SSH = skip”) at plan gate.

Hard fail-closed items stay deferred/skipped; do not substitute Cycle 4/5 archives or other Medium names without a new plan gate.

### Verify only — do not move

| Path / set | Action |
| --- | --- |
| Cycle 4 archives: `archive\2025.06.25 - TestRyan`, `archive\2025.08.12 - ReactRouterTest`, `archive\2025.06.05 - Simpl` | Confirm still present; **no re-move** |
| Cycle 5 archives: `archive\2025.06.23 - NextTest`, `archive\2025.06.23 - Simpl_Next`, `archive\2025.07.04 - PWAExempleTristan` | Confirm still present; **no re-move** |
| Early/simple archive/paused destinations | Confirm still present; **no re-move** |

**Out of map (do not move):** Cycle 4/5 / Early-simple trees; must-preserve draft paths; organisation repo; hygiene orphans; multi-experiment / Obsidian / ProjetOrif / special-git rows.

---

## Acceptance criteria

### Before implementer (orchestrator / plan gate)

- [ ] `notes.md` Answers lock Q1–Q5 (no open “Choose”).
- [ ] Research live-checked both candidates; INDEX vs disk noted; Cycle 4/5 archives not treated as move sources.
- [ ] Plan shortlist is explicit: `NextPWATraining`, `CursorMobileWorkspace` (both; shrink only on Q5=A fail-closed skip).
- [ ] Plan contains the exact two-row move map above, declares `fs_mutation`, and states atomic nested-git + opaque-secrets + no SSH rewrite.
- [ ] No re-soft-defer-both as default; hazard skips (if any) have reasons.
- [ ] User **explicitly** approved this plan/map in-session (plan gate).

### After implementer (auditor-checkable)

- [ ] Exactly the approved folders moved once (both, unless one Q5 skip); **no** extras outside the approved map; **no** Cycle 4/5 re-moves.
- [ ] Preflight at implement: sources existed; targets did not; each wrapper still contains its expected nested `.git` after move (if present pre-move).
- [ ] Post: sources absent; targets present at destinations above (or user-approved edits only).
- [ ] **Destination nested-git attestation:** `Test-Path` True for each expected destination `.git` path above.
- [ ] **Opaque `.env` attestation:** NextPWA destination `.env` `Test-Path` True if pre-move was True; **no secret contents** in session logs.
- [ ] Unexpected hazards → item **skipped + logged** (fail-closed; no git-strategy invent; at most one defer under Q5=A).
- [ ] Parents `C:\Project\archive` and `C:\Project\paused` exist as needed.
- [ ] `catalogue/INDEX.md`: Status / date label / **current path** updated for moved rows (NextPWA → archive path; CursorMobile → paused path).
- [ ] `catalogue/inventory.md` path/status notes refreshed for the two moved rows (and nested-path bullets if they still imply root-only wrappers).
- [ ] Optional taxonomy note only: Continuity for Medium; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- [ ] `program/ROADMAP.md`: if **both** remaining moved → Medium row **Complete**; Primary next → **Multi-experiment** (no phantom “remaining (0)”). If one Q5 skip → Medium stays **in progress** with remaining name noted; do **not** jump Primary next.
- [ ] Implementation log lists each `from → to`, nested-git + `.env` attestations, skip reasons, Cycle 4/5 verify-only notes, and **reverse-move** notes.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied for already-moved rows); cycle not marked complete with unmet AC.
- [ ] No agent `git push` / `git pull` / remote publish attempted for this cycle.
- [ ] No SSH/remote URL rewrite on NextPWA (or CursorMobile).

**Not hard AC:** size / cheap-band metadata “if available” — include when cheap (NextPWA live L ~380 MB is duration signal only); do not false-fail audit on size fields. Inventory size lag vs live is duration note only.

---

## Ordered steps

### Step 0 — Orchestrator plan gate (blocking)

- **Paths:** this `plan.md`
- **Action:** Present move map + “What the user is approving” (plain language + pros/cons, including SSH origin stays as-is on NextPWA); obtain explicit yes (or edited map). Do **not** start implementer without yes.
- **Verify:** Session note or handoff records plan-gate approval.

### Step 1 — Implementer preflight (fail-closed)

- **Paths:** two sources + two destinations + `C:\Project\archive` + `C:\Project\paused`; expected nested `.git` and opaque `.env` paths from the move map; Cycle 4/5 archive destinations
- **Action:** For each move row: `Test-Path` source exists; destination absent; parent will be directory. Confirm expected nested `.git` still present under the sole child. Record pre-move opaque `.env` `Test-Path` for NextPWA (boolean only). Re-probe worktree/remote hazard screen lightly (or equivalent recurse + `git worktree list` / `remote -v` at nested root). If unexpected `.git` / worktrees / multi-remote / collision → **skip that item**, log, do not invent git-strategy, do not substitute other folders. Confirm Cycle 4/5 archive destinations present and not re-targeted. Do **not** rewrite remotes.
- **Verify:** Preflight table in `04-implementation/log.md`.

### Step 2 — Create status parents if needed

- **Paths:** `C:\Project\archive`, `C:\Project\paused`
- **Action:** `New-Item -ItemType Directory` if either missing. Do not create `active` for this batch.
- **Verify:** Both parents exist as directories.

### Step 3 — Move trees (sequential)

- **Paths:** move map rows 1 → 2 (NextPWA then CursorMobile)
- **Action:** Prefer `Move-Item -LiteralPath <source> -Destination <destination>` (rename-in-move into parent). Same volume; whole wrapper including nested `.git` + opaque `.env`; no copy-delete; secrets/deps opaque (do not open); **no remote URL rewrite**. Expect longer duration for NextPWA (L-band ~380 MB). On failure: stop further moves; reverse already-successful rows if Critical (see rollback).
- **Verify:** After each row: source gone; destination present; nested `.git` still under expected relative child path; NextPWA destination `.env` `Test-Path` matches pre-move presence.

### Step 4 — Destination attestation

- **Paths:** destination nested `.git` + NextPWA `.env` table above
- **Action:** `Test-Path` each listed path; record True/False in log only (no file open/read). Optionally note NextPWA nested remote still SSH (read `remote -v` URLs only — do not rewrite).
- **Verify:** All expected nested `.git` True; NextPWA `.env` True if pre-move was True.

### Step 5 — Catalogue updates (org repo docs only)

- **Paths:**
  - `catalogue/INDEX.md` — two rows: Status (`archive` / `paused`); date label applied (drop “proposed” / soft-deferred markers); **current path** → destinations; leave Cycle 4/5 archive rows as-is; refresh “What’s next” so Medium is no longer “remaining soft-deferred.”
  - `catalogue/inventory.md` — refresh path/status notes for NextPWATraining / CursorMobileWorkspace (and nested-path bullets that still list root-relative wrappers for those two); optional size-band honesty if cheap (NextPWA L ~380 MB).
  - `catalogue/taxonomy.md` — optional Continuity note only; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- **Action:** Edit docs to match disk; no other catalogue churn; do not touch must-preserve draft list.
- **Verify:** Grep/read shows two new status paths; Cycle 4/5 archives unchanged; org-repo protect row unchanged.

### Step 6 — ROADMAP Complete + Primary next

- **Paths:** `program/ROADMAP.md`
- **Action:** If **both** moves succeeded: mark Medium wrappers row **Complete**; set **Primary next → Multi-experiment**; clear remaining soft-deferred names (no phantom “remaining (0)”). Update “How the next cycle starts” accordingly. If one Q5 skip: keep Medium **in progress** with remaining name noted; do **not** mark Complete; do **not** jump Primary next.
- **Verify:** On full success — Medium Complete + Primary next Multi-experiment. On partial — remaining name explicit; row not Complete.

### Step 7 — Session implementation log

- **Paths:** `sessions/2026.09.09-1612/04-implementation/log.md` (+ `changes.md` as usual)
- **Action:** Record each `from → to`, nested `.git` + `.env` attestations, skip reasons, Cycle 4/5 verify-only notes, SSH-left-as-is note for NextPWA, and **reverse-move** commands/paths (table below). Attest: zero intentional moves outside the approved map; zero corpus deletes of payload; no secret contents logged; no push/pull; no remote rewrite.
- **Verify:** Log complete before claiming implementation done.

### Step 8 — Auditor

- **Action:** Check acceptance criteria checklist against disk + catalogue + ROADMAP + log.
- **Verify:** Pass / fail with evidence; Critical unmet → not complete.

**Push / pull preflight:** skipped (N/A — no remote publish).

---

## Non-goals

- Re-soft-deferring both remaining names as the default outcome
- Re-moving or re-proposing Cycle 4 archives (`TestRyan`, `ReactRouterTest`, `Simpl`)
- Re-moving or re-proposing Cycle 5 archives (`NextTest`, `Simpl_Next`, `PWAExempleTristan`)
- Reopening or re-moving Early/simple Cycle 2–3 destinations
- Jumping to Multi-experiment while either remaining Medium name is still in-scope and unmoved (unless user drops from scope)
- Touching must-preserve draft paths (Obsidian, ProjetOrif, WebCatalogue, WorkSpace, HTTP Battles, …)
- Relocating or restructuring the organisation repo
- Git-strategy / treating unexpected hazards as anything other than skip+log
- Hygiene orphans, multi-experiment / Obsidian / ProjetOrif / special-git batches (until Medium Complete)
- Agent remote push, pull, or history rewrite / filter-repo / splitting wrapper from nested git / rewriting SSH or HTTPS remote URLs
- Claiming global final taxonomy or must-preserve ratification beyond Continuity wording
- Fixing all INDEX drift for non-batch rows (honesty only)
- Reading or logging secret file contents

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Unexpected nested `.git` / worktree / multi-remote at implement time | Fail-closed: skip that item; log; no git-strategy; Q5=A at most one defer |
| Target collision | Skip overwrite; log; do not merge |
| File lock / long L-band NextPWA move | Prefer single `Move-Item`; retry once or skip+log; do not copy+delete |
| Partial batch (1 of 2 moved) | Per-row reverse-move; on Critical failure reverse already-moved rows; if Q5 skip only → ROADMAP stays in progress with remaining name |
| Secret leakage via logs | Path-only for `.env`; never open/read contents; attestation = `Test-Path` boolean |
| SSH residual (NextPWA) | Path-only; leave origin URL as-is; no agent push/pull; called out in plan-gate cons |
| Catalogue / ROADMAP drift after FS move | Steps 5–7 same acceptance batch as moves |
| Accidental Cycle 4/5 re-move | Explicit non-goals + Step 1 verify-only |
| Path bookmarks break | Called out in plan-gate pros/cons; user accepts by approving |
| False Complete with unmet AC | Only mark Medium Complete when both succeed; else remaining name + blocked/partial |

### Reverse-move notes (encode in implementation log)

| Forward | Reverse (do not delete payload) |
| --- | --- |
| `C:\Project\NextPWATraining` → `C:\Project\archive\2025.06.23 - NextPWATraining` | Move dated folder back to `C:\Project\NextPWATraining` |
| `C:\Project\CursorMobileWorkspace` → `C:\Project\paused\2026.06.17 - CursorMobileWorkspace` | Move dated folder back to `C:\Project\CursorMobileWorkspace` |

Empty `archive` / `paused` parents may remain after reverse (harmless). Nested `.git` and opaque `.env` ride with the wrapper on reverse (same atomic unit). SSH remote URL remains whatever it was (no rewrite on reverse either).

**Critical rollback policy:** If a move succeeds then a later hard failure leaves AC unmet, reverse already-moved rows using the table above, document in log, do not mark cycle complete.

---

## Verification checklist (auditor quick list)

1. Sources absent; destinations present for all non-skipped approved rows.  
2. Nested `.git` intact under expected relative child; destination `Test-Path` attested.  
3. NextPWA opaque `.env` destination `Test-Path` matches pre-move presence; no secret contents in logs.  
4. Skipped rows (if any) have hazard/collision evidence in log; no silent map expansion; at most one Q5 defer.  
5. Cycle 4/5 archive destinations untouched.  
6. INDEX + inventory updated for the two moved rows.  
7. ROADMAP: both moved → Medium **Complete** + Primary next **Multi-experiment**; else remaining name + not Complete.  
8. Org repo / must-preserve draft paths untouched.  
9. Reverse-move notes present for each successful move.  
10. No push/pull attempted; no SSH/remote URL rewrite.  

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
