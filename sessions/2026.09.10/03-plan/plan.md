# Plan — Cycle 7 Multi-experiment (first subset, fs_mutation)

**Session:** `sessions/2026.09.10/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md` (+ `codebase-findings.md`)  
**Approach:** Research **Option A** — first subset = `GitTest` + `WorkStationPWA` → `archive`. Sequential same-volume `Move-Item` (whole wrapper + all nested `.git`; no `.env` expected). Fail-closed defer `WorkSpace`; hold `PWAExemple` for a later Multi-experiment sub-batch. After success → update INDEX + ROADMAP **Notes** for remaining names (`PWAExemple`, `WorkSpace`); row stays **in progress** — **do not** mark Multi-experiment Complete.

---

## Goal

Execute ROADMAP **Primary next → Multi-experiment** as a **scoped first subset** only: relocate `GitTest` and `WorkStationPWA` under `C:\Project\archive\` with CreationTime date labels, keeping every nested `.git` under each wrapper as one atomic unit, leaving remotes (including WorkStation’s one SSH `origin`) **path-only** (no URL rewrite), and carrying any `.env` unread if a pre-move re-scan finds one. Update `catalogue/INDEX.md` (+ inventory as needed) for those two rows, attest destination nested-git paths via `Test-Path`, log each forward path with reverse-move notes, then update `program/ROADMAP.md` Notes to show **partial Multi-experiment progress** (2 moved / 2 remaining: `PWAExemple`, `WorkSpace`) — **do not** mark the row Complete. Do not reopen Medium/Early as move sources; do not move `WorkSpace` or `PWAExemple` this cycle. Moves run only after the orchestrator obtains **explicit user plan-gate approval** of this map. No agent push/pull.

---

## What the user is approving (plan gate)

You are approving **this exact two-folder move map** (not “finish Multi-experiment” in the abstract, and not the Continuity Choose-all on Q1–Q4). After you say **yes**, the implementer will relocate these two folders on disk, update catalogue paths for them, and record that **`PWAExemple` and `WorkSpace` remain** on the Multi-experiment ROADMAP row (still in progress — not Complete).

| Approve? | Meaning |
| --- | --- |
| **Yes** | Ensure parent `C:\Project\archive` exists (already present per research; create only if missing); move the two sources to the destinations below **including** all nested git repos (and any `.env` found unread); leave SSH/HTTPS remotes **unchanged**; update INDEX (+ inventory) for those two rows; update ROADMAP Notes for **partial progress** (remaining: `PWAExemple`, `WorkSpace`); leave Medium/Early archives, `WorkSpace`, `PWAExemple`, must-preserve draft paths, and the org repo alone. |
| **No / edit** | No moves; revise the map (e.g. GitTest-only), drop a name, or defer until a new plan. Multi-experiment stays at full four-name list until a later approved batch. |

**Exact path map**

| # | From | To |
| --- | --- | --- |
| 1 | `C:\Project\GitTest` | `C:\Project\archive\2025.08.08 - GitTest` |
| 2 | `C:\Project\WorkStationPWA` | `C:\Project\archive\2025.07.01 - WorkStationPWA` |

**Pros**

- Starts Multi-experiment with the **lowest-risk** peers (S-band; INDEX nested counts match; no `.env` at research; clean worktrees / single-remote each).
- Statuses match Continuity 90-day heuristic → both **archive**.
- Leaves higher-complexity `PWAExemple` and fail-closed `WorkSpace` for later — avoids forcing unsafe or heavier moves into the first batch.
- Catalogue paths catch up so INDEX stops showing stale root locations for these two.
- Does **not** reopen Medium/Early destinations as sources.

**Cons / tradeoffs**

- **Paths change** — bookmarks, open terminals, IDE workspaces, or scripts pointing at `C:\Project\GitTest` or `C:\Project\WorkStationPWA` will break until updated.
- **WorkStation nested SSH `origin` stays as-is** (`git@github.com:…` under `WorkStationRouterPWA\workstation-app`) — path-only move; no remote URL rewrite. Residual risk if local SSH tooling assumed the old disk path; agent will not push/pull or rewrite remotes.
- **Name confusion risk:** `GitTest\NextTest` is a nested folder — **not** the archived Medium `NextTest` at `archive\2025.06.23 - NextTest`. Approving this map does not re-touch that archive.
- Batch is **not transactional** across two rows: if one fails mid-way, already-moved items may need reverse-move (documented per row). A fail-closed skip shrinks the subset without inventing substitute folders.
- Multi-experiment row will **still be open** after this cycle (2 remaining) — you are not approving “done with Multi-experiment.”

Prior Continuity / Choose-all / starting this FAW is **not** this approval. Orchestrator must pause here and obtain an explicit yes on this plan/map before launching implementer.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | `fs_mutation` |
| Batch name | Cycle 7 Multi-experiment — first subset (`GitTest`, `WorkStationPWA`) |
| Corpus FS | Intentional moves of the two approved wrapper trees only (all nested `.git` included; opaque `.env` if any); parent `archive` already exists (create only if missing) |
| User approval before implementer | **Required** — plan-gate on this map (orchestrator pause) |
| Docs attestation after moves | INDEX (+ inventory) updated for the two moved rows; ROADMAP Notes → **partial progress** (remaining `PWAExemple`, `WorkSpace`); row **not** Complete |
| Push / remote publish | **Not required** — dual auth/preflight N/A |

### Continuity / Medium-style gates (documented — do not upgrade labels)

Per refined prompt + Continuity Q4=A (do **not** re-litigate global taxonomy/must-preserve solely to unblock this Multi-experiment subset; do **not** claim final ratification):

| Gate | Status for this cycle |
| --- | --- |
| Taxonomy | **Satisfied via Continuity** — remains **proposed-ratified — ready for user sign-off** (not final without explicit user sign-off); Early/simple/Medium-style binding reused — **not** global final corpus ratification |
| Must-preserve | **Satisfied via Continuity** — remains **draft — not auto-locked / for user review**; batch folders **not** on draft list; `WorkSpace` is on draft Medium but is **out of this map** (fail-closed defer — flag only, do not invent final lock) |
| Per-batch path list | **This plan’s move map** — still needs **explicit user plan-gate yes** before implementer |

**Remaining gate before implementer:** user plan-map approval only (see section above).

---

## Explicit move map (matches research Option A — no deviation)

| # | Source | Status (90d) | Destination | Nested `.git` stays under (atomic) |
| --- | --- | --- | --- | --- |
| 1 | `C:\Project\GitTest` | `archive` | `C:\Project\archive\2025.08.08 - GitTest` | `...\NextTest\.git`, `...\test\.git` |
| 2 | `C:\Project\WorkStationPWA` | `archive` | `C:\Project\archive\2025.07.01 - WorkStationPWA` | `...\WorkStationPWA\.git`, `...\WorkStationRouterPWA\workstation-app\.git` |

**Parents:** `C:\Project\archive` exists (research); create only if missing at implement. `paused` / `active` not required for this batch.

**Unit:** whole top-level wrapper tree per row (`Move-Item -LiteralPath`), including **all** nested `.git` and any non-git children. Prefer rename/move over copy+delete; never delete payload to “clean up.” Secrets/deps opaque — do not open `.env` (path-only logging OK). **No SSH/remote URL rewrite** (path-only).

### Deferred / remaining (not in this map)

| Folder | Role | Plan action |
| --- | --- | --- |
| `WorkSpace` | **Fail-closed defer** | Do not move; log multi-remote + unexpected `_backups`/`_quarantine` roots; consider later **git-strategy** cycle — not this batch |
| `PWAExemple` | Remaining Multi-experiment | Hold for later sub-batch (3 nested roots, opaque `.env`×4, one SSH) — not fail-closed |
| Medium / Early archive & paused paths | Verify-only | Confirm present; **never** re-propose as sources |

### Secrets / opaque payload (path-only; never read)

| Item | Research finding | Handling |
| --- | --- | --- |
| GitTest | No `.env` (depth scan) | If preflight finds any `.env*`, move with tree; **never read or log contents**; post-move `Test-Path` destination path only |
| WorkStationPWA | No `.env` (depth scan) | Same opaque rules if found |

### Destination attestation (implementer AC — required)

After each successful move, attest with `Test-Path` (boolean only; no file open):

| Destination nested `.git` | Destination opaque `.env` |
| --- | --- |
| `C:\Project\archive\2025.08.08 - GitTest\NextTest\.git` | N/A unless preflight found `.env` |
| `C:\Project\archive\2025.08.08 - GitTest\test\.git` | N/A unless preflight found `.env` |
| `C:\Project\archive\2025.07.01 - WorkStationPWA\WorkStationPWA\.git` | N/A unless preflight found `.env` |
| `C:\Project\archive\2025.07.01 - WorkStationPWA\WorkStationRouterPWA\workstation-app\.git` | N/A unless preflight found `.env` |

Log: path + `True`/`False` only. If expected nested `.git` missing post-move → Critical for that row. If an opaque `.env` was present pre-move and absent post-move → Critical for that row.

### Fail-closed unexpected hazards (implementer re-scan)

Immediately before each move, re-check. On any of the following → **skip that item + log**; do **not** invent git-strategy mid-batch; do **not** expand the map to `PWAExemple` / `WorkSpace` / Medium / Early:

- Destination already exists (no overwrite / merge)
- Source missing
- Unexpected **extra** nested `.git` beyond the expected two per wrapper (or linked worktrees / messy multi-remote that was not present at research)
- Any path outside this approved map

**SSH alone is not hard fail-closed** for WorkStation under Continuity Q3=A (path-only; residual informational risk).

Hard fail-closed items stay deferred/skipped; do not substitute other Multi-experiment names without a new plan gate.

### Verify only — do not move

| Path / set | Action |
| --- | --- |
| Medium Cycle 4–6 archive/paused destinations (e.g. `archive\2025.06.23 - NextTest`, `archive\2025.07.04 - PWAExempleTristan`, `archive\2025.06.23 - NextPWATraining`, `paused\2026.06.17 - CursorMobileWorkspace`, …) | Confirm still present; **no re-move** |
| Early/simple archive/paused destinations | Confirm still present; **no re-move** |
| `C:\Project\PWAExemple`, `C:\Project\WorkSpace` | Confirm still at root; **no move this cycle** |

**Out of map (do not move):** `PWAExemple`; `WorkSpace`; Medium/Early trees; must-preserve draft paths; organisation repo; hygiene orphans; Obsidian / ProjetOrif / special-git rows.

---

## Acceptance criteria

### Before implementer (orchestrator / plan gate)

- [ ] Continuity / Answers lock Q1–Q4 (no open “Choose” for subset size, multi-git caution, SSH path-only, Continuity carry).
- [ ] Research live-checked only Multi-experiment candidates; proposed 1–2 subset with rationale; deferred `WorkSpace` + held `PWAExemple` documented.
- [ ] Plan shortlist is explicit: `GitTest`, `WorkStationPWA` only (shrink only on fail-closed skip).
- [ ] Plan contains the exact two-row move map above, declares `fs_mutation`, and states atomic nested-git + opaque-secrets + SSH path-only (no remote rewrite).
- [ ] Plan includes “What the user is approving” (plain language + path map + pros/cons).
- [ ] Taxonomy wording stays **proposed-ratified — ready for user sign-off**; must-preserve stays **draft — not auto-locked / for user review** (no label upgrade).
- [ ] User **explicitly** approved this plan/map in-session (plan gate). Continuity Choose ≠ this approval.

### After implementer (auditor-checkable)

- [ ] Exactly the approved folders moved once (both, unless fail-closed skip); **no** extras outside the approved map; **no** Medium/Early re-moves; **no** `PWAExemple` / `WorkSpace` moves.
- [ ] Preflight at implement: sources existed; targets did not; each wrapper still contains its expected nested `.git` paths after move (if present pre-move).
- [ ] Post: sources absent; targets present at destinations above (or user-approved edits only).
- [ ] **Destination nested-git attestation:** `Test-Path` True for each expected destination `.git` path above.
- [ ] **Opaque `.env`:** if any found pre-move, destination `Test-Path` True and **no secret contents** in session logs; if none found, attest absence (boolean) — do not invent reads.
- [ ] Unexpected hazards → item **skipped + logged** (fail-closed; no git-strategy invent; no map expansion).
- [ ] Parent `C:\Project\archive` exists as needed.
- [ ] `catalogue/INDEX.md`: Status / date label / **current path** updated for moved rows (`GitTest`, `WorkStationPWA` → archive paths); `PWAExemple` / `WorkSpace` rows still honest at root (or unchanged).
- [ ] `catalogue/inventory.md` path/status notes refreshed for the two moved rows when they still imply root-only wrappers (nested-path bullets as needed).
- [ ] Optional Continuity note only: keep taxonomy **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- [ ] `program/ROADMAP.md`: Multi-experiment Notes show **partial progress** — e.g. Cycle 7 moved `GitTest`, `WorkStationPWA` → `archive`; **remaining:** `PWAExemple`, `WorkSpace`. Row stays **Primary next / in progress** — **do not** mark Complete; **do not** jump Primary next away from Multi-experiment.
- [ ] Implementation log lists each `from → to`, nested-git (+ `.env` if any) attestations, skip reasons, Medium/Early verify-only notes, SSH-left-as-is note for WorkStation, and **reverse-move** notes.
- [ ] Org repo tree and must-preserve draft list unchanged (no rewrite of draft entries).
- [ ] On Critical fail: reverse-move documented (and applied for already-moved rows); cycle not marked complete with unmet AC.
- [ ] No agent `git push` / `git pull` / remote publish attempted for this cycle.
- [ ] No SSH/remote URL rewrite on any nested remote.

**Not hard AC (optional / if cheap):** size / band metadata, inventory size lag vs live, remote-scheme “informational” notes beyond path-only attestation — include when cheap; do not false-fail audit on size fields or optional metadata.

---

## Ordered steps

### Step 0 — Orchestrator plan gate (blocking)

- **Paths:** this `plan.md`
- **Action:** Present move map + “What the user is approving” (plain language + pros/cons, including WorkStation SSH origin stays as-is; row stays in progress with remaining names). Obtain explicit yes (or edited map). Do **not** start implementer without yes.
- **Verify:** Session note or handoff records plan-gate approval.

### Step 1 — Implementer preflight (fail-closed)

- **Paths:** two sources + two destinations + `C:\Project\archive`; expected nested `.git` paths from the move map; Medium/Early archive/paused destinations (verify-only); `PWAExemple` / `WorkSpace` (confirm not targeted)
- **Action:** For each move row: `Test-Path` source exists; destination absent; parent will be directory. Confirm expected nested `.git` still present (exactly two per wrapper unless research-aligned). Record pre-move opaque `.env*` `Test-Path` if any (boolean only). Re-probe worktree/remote hazard screen lightly (or equivalent recurse + `git worktree list` / `remote -v` at nested roots). If unexpected extra `.git` / linked worktrees / multi-remote / collision → **skip that item**, log, do not invent git-strategy, do not substitute `PWAExemple`/`WorkSpace`/Medium/Early. Confirm Medium/Early destinations present and not re-targeted. Do **not** rewrite remotes.
- **Verify:** Preflight table in `04-implementation/log.md`.

### Step 2 — Create status parent if needed

- **Paths:** `C:\Project\archive`
- **Action:** `New-Item -ItemType Directory` if missing. Do not create `paused` / `active` for this batch.
- **Verify:** `archive` exists as a directory.

### Step 3 — Move trees (sequential)

- **Paths:** move map rows 1 → 2 (`GitTest` then `WorkStationPWA`)
- **Action:** Prefer `Move-Item -LiteralPath <source> -Destination <destination>` (rename-in-move into parent). Same volume; whole wrapper including all nested `.git` + any opaque `.env`; no copy-delete; secrets/deps opaque (do not open); **no remote URL rewrite**. On failure: stop further moves; reverse already-successful rows if Critical (see rollback).
- **Verify:** After each row: source gone; destination present; nested `.git` still under expected relative child paths; any pre-move `.env` destination `Test-Path` matches pre-move presence.

### Step 4 — Destination attestation

- **Paths:** destination nested `.git` (+ `.env` if any) table above
- **Action:** `Test-Path` each listed path; record True/False in log only (no file open/read). Optionally note WorkStation nested remote still SSH (read `remote -v` URLs only — do not rewrite).
- **Verify:** All expected nested `.git` True; opaque `.env` True iff pre-move was True.

### Step 5 — Catalogue updates (org repo docs only)

- **Paths:**
  - `catalogue/INDEX.md` — two rows: Status `archive`; date label applied (drop “proposed” / TBD markers); **current path** → destinations; leave `PWAExemple` / `WorkSpace` at root honestly; leave Medium/Early archive rows as-is; refresh “What’s next” so Multi-experiment shows remaining names (not Complete).
  - `catalogue/inventory.md` — refresh path/status notes for `GitTest` / `WorkStationPWA` (and nested-path bullets that still list root-relative wrappers for those two); optional size-band honesty if cheap (S-band).
  - `catalogue/taxonomy.md` — optional Continuity note only; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
  - `catalogue/must-preserve.md` — **do not** rewrite / “lock” draft; `WorkSpace` stay draft Medium flag only.
- **Action:** Edit docs to match disk; no other catalogue churn.
- **Verify:** Grep/read shows two new archive paths; remaining Multi-experiment root paths still honest; Medium/Early archives unchanged; org-repo protect row unchanged.

### Step 6 — ROADMAP partial progress (not Complete)

- **Paths:** `program/ROADMAP.md`
- **Action:** Update Multi-experiment Notes for **partial progress**: Cycle 7 moved `GitTest`, `WorkStationPWA` → `archive`; **remaining:** `PWAExemple`, `WorkSpace` (with `WorkSpace` noted fail-closed / git-strategy later if useful). Keep row as **Primary next → Multi-experiment** / in progress. **Do not** mark Multi-experiment Complete. **Do not** reopen Medium wrappers or Early/simple. Update “How the next cycle starts” to lock **same row / remaining names** (`PWAExemple`, then `WorkSpace` or git-strategy as appropriate).
- **Verify:** Notes show N moved / M remaining with names; no Complete claim; Primary next still Multi-experiment.

### Step 7 — Session implementation log

- **Paths:** `sessions/2026.09.10/04-implementation/log.md` (+ `changes.md` as usual)
- **Action:** Record each `from → to`, nested `.git` (+ `.env` if any) attestations, skip reasons, Medium/Early verify-only notes, SSH-left-as-is note for WorkStation, deferred `WorkSpace` / held `PWAExemple`, and **reverse-move** commands/paths (table below). Attest: zero intentional moves outside the approved map; zero corpus deletes of payload; no secret contents logged; no push/pull; no remote rewrite; ROADMAP not marked Complete.
- **Verify:** Log complete before claiming implementation done.

### Step 8 — Auditor

- **Action:** Check acceptance criteria checklist against disk + catalogue + ROADMAP + log.
- **Verify:** Pass / fail with evidence; Critical unmet → not complete.

**Push / pull preflight:** skipped (N/A — no remote publish).

---

## Non-goals

- Moving all four Multi-experiment folders this cycle
- Moving `PWAExemple` or `WorkSpace` in this batch
- Marking Multi-experiment ROADMAP row **Complete** while names remain
- Reopening or re-moving Medium wrappers (Cycle 4–6) or Early/simple (Cycle 2–3) destinations as sources
- Rewriting git remotes / history / filter-repo / worktree repair / splitting wrappers from nested git
- Treating unexpected multi-git hazards as anything other than skip+log (no mid-batch git-strategy invent)
- Executing a dedicated git-strategy cycle here (may be **scheduled later** for `WorkSpace` — not executed)
- Touching must-preserve draft paths as move sources; upgrading taxonomy or must-preserve to final without explicit user sign-off
- Relocating or restructuring the organisation repo
- Hygiene orphans, Obsidian, ProjetOrif, WebCatalogue, HTTP Battles
- Agent remote push, pull, or publish
- Reading or logging secret file contents
- Making optional size/band/metadata signals into hard AC checkboxes

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Unexpected nested `.git` / worktree / multi-remote at implement time | Fail-closed: skip that item; log; no git-strategy; no map expansion |
| Target collision | Skip overwrite; log; do not merge |
| File lock / move failure | Prefer single `Move-Item`; retry once or skip+log; do not copy+delete |
| Partial batch (1 of 2 moved) | Per-row reverse-move; on Critical failure reverse already-moved rows; ROADMAP Notes list what actually moved + remaining |
| Secret leakage via logs | Path-only for `.env*`; never open/read contents; attestation = `Test-Path` boolean |
| SSH residual (WorkStation nested) | Path-only; leave origin URL as-is; no agent push/pull; called out in plan-gate cons |
| Name confusion (`GitTest\NextTest` vs archived Medium `NextTest`) | Explicit verify-only + non-goals; do not touch `archive\2025.06.23 - NextTest` |
| Catalogue / ROADMAP drift after FS move | Steps 5–7 same acceptance batch as moves; ROADMAP partial only |
| Accidental Medium/Early / PWAExemple / WorkSpace move | Explicit non-goals + Step 1 verify-only |
| Path bookmarks break | Called out in plan-gate pros/cons; user accepts by approving |
| False Complete | Never mark Multi-experiment Complete while remaining names exist |

### Reverse-move notes (encode in implementation log)

| Forward | Reverse (do not delete payload) |
| --- | --- |
| `C:\Project\GitTest` → `C:\Project\archive\2025.08.08 - GitTest` | Move dated folder back to `C:\Project\GitTest` |
| `C:\Project\WorkStationPWA` → `C:\Project\archive\2025.07.01 - WorkStationPWA` | Move dated folder back to `C:\Project\WorkStationPWA` |

Empty `archive` parent may remain after reverse (harmless). Nested `.git` (and any opaque `.env`) ride with the wrapper on reverse (same atomic unit). Remote URLs remain whatever they were (no rewrite on reverse either).

**Critical rollback policy:** If a move succeeds then a later hard failure leaves AC unmet, reverse already-moved rows using the table above, document in log, do not mark cycle complete.

---

## Verification checklist (auditor quick list)

1. Sources absent; destinations present for all non-skipped approved rows.  
2. Nested `.git` intact under expected relative children; destination `Test-Path` attested (4 expected paths).  
3. Opaque `.env` (if any) destination `Test-Path` matches pre-move; no secret contents in logs.  
4. Skipped rows (if any) have hazard/collision evidence in log; no silent map expansion to `PWAExemple`/`WorkSpace`/Medium/Early.  
5. Medium/Early archive/paused destinations untouched; `PWAExemple`/`WorkSpace` still at root.  
6. INDEX + inventory updated for the two moved rows.  
7. ROADMAP: partial Notes (remaining names); Multi-experiment **not** Complete; Primary next still Multi-experiment.  
8. Org repo / must-preserve draft list untouched as move sources; Continuity labels not upgraded to final.  
9. Reverse-move notes present for each successful move.  
10. No push/pull attempted; no SSH/remote URL rewrite.  

---

## Ready to implement

| Field | Value |
| --- | --- |
| Plan complete | **yes** |
| `ready_to_implement` | **yes** *(plan artifact complete — implementer still blocked until plan gate)* |
| `requires_user_plan_gate` | **yes** |
| `mutation_class` | `fs_mutation` |
| Research blockers | none |
| Push blockers | none (N/A) |

**Orchestrator rule:** Even though `ready_to_implement: yes`, **do not** launch implementer until the user explicitly approves this plan/move map in-session. Continuity Choose-all is insufficient.

## Blocking questions

**none** for plan content.  
**Process:** awaiting user plan-gate approval (orchestrator).
