# Plan — Cycle 8 Multi-experiment (remaining subset, fs_mutation)

**Session:** `sessions/2026.09.10-0811/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md` (+ `codebase-findings.md`)  
**Approach:** Research **Option A** — remaining executable map = **`PWAExemple` only** → `archive`. Sequential same-volume `Move-Item` (whole wrapper + all **3** nested `.git`; opaque `.env`×4 unread). **Fail-closed defer `WorkSpace`** (not in move map). Prefer single `Move-Item`; on Windows nested-`.git` lock → Continuity recovery (reunify + `robocopy /E /MOVE`; empty `.git` shells only; re-attest). After success → update INDEX (+ nested-count 2→3) + ROADMAP **Notes** for remaining **`WorkSpace` only** (nearly-complete / soft-deferred fail-closed style); row stays **in progress** — **do not** mark Multi-experiment Complete while `WorkSpace` remains.

---

## Goal

Execute ROADMAP **Primary next → Multi-experiment** as a **scoped remaining subset**: relocate only `PWAExemple` under `C:\Project\archive\` with CreationTime date label `2025.06.25 - PWAExemple`, keeping all **3** nested `.git` under the wrapper as one atomic unit, leaving remotes (including the one SSH `origin` on `PWAFrontAuthTest`) **path-only** (no URL rewrite), and carrying opaque `.env`×4 unread. Update `catalogue/INDEX.md` (+ inventory as needed) for that row (fix nested-count drift), attest destination nested-git + opaque `.env` paths via `Test-Path`, log forward path with reverse-move notes, then update `program/ROADMAP.md` Notes to show **partial Multi-experiment progress** (Cycle 7 + Cycle 8 moved; **remaining:** `WorkSpace` fail-closed / git-strategy candidate — nearly complete, not Complete). Do not reopen Medium/Early as move sources; do not re-move Cycle 7 archives (`GitTest`, `WorkStationPWA`); do not move `WorkSpace`. Moves run only after the orchestrator obtains **explicit user plan-gate approval** of this map. No agent push/pull.

---

## What the user is approving (plan gate)

You are approving **this exact one-folder move map** (not “finish Multi-experiment” in the abstract, and not the Continuity Choose-all on Q1–Q4). After you say **yes**, the implementer will relocate `PWAExemple` on disk, update catalogue paths for it, and record that **`WorkSpace` remains** on the Multi-experiment ROADMAP row (still in progress / nearly complete — **not** Complete).

| Approve? | Meaning |
| --- | --- |
| **Yes** | Ensure parent `C:\Project\archive` exists (already present per research; create only if missing); move `PWAExemple` to the destination below **including** all 3 nested git repos and opaque `.env`×4 unread; leave SSH/HTTPS remotes **unchanged**; on Windows nested-`.git` lock follow Continuity recovery (reunify + robocopy; empty shells only); update INDEX (+ inventory nested count 2→3); update ROADMAP Notes for **partial progress** (remaining: **`WorkSpace` only**, fail-closed); leave Medium/Early archives, Cycle 7 archives, `WorkSpace`, must-preserve draft paths, and the org repo alone. |
| **No / edit** | No moves; revise the map (e.g. defer `PWAExemple` too / zero moves), or wait for a new plan. Multi-experiment stays with remaining `PWAExemple` + `WorkSpace` until a later approved batch. |

**Exact path map**

| # | From | To |
| --- | --- | --- |
| 1 | `C:\Project\PWAExemple` | `C:\Project\archive\2025.06.25 - PWAExemple` |

**Not in map (explicit)**

| Folder | Disposition |
| --- | --- |
| `C:\Project\WorkSpace` | **Fail-closed defer** — messy multi-remote + unexpected `_backups`/`_quarantine` roots; XL; must-preserve draft Medium flag only; later **git-strategy** candidate — **do not move** this cycle |
| Cycle 7 archives (`GitTest`, `WorkStationPWA`) | Verify-only — **do not re-move** |
| Medium / Early archive & paused paths | Verify-only — **do not re-open as sources** |

**Pros**

- Moves the only **green** remaining Multi-experiment candidate under Q1=A Continuity.
- Status matches Continuity 90-day heuristic → **archive**.
- Leaves fail-closed `WorkSpace` deferred with a logged reason — avoids inventing unsafe or mid-batch git-strategy work.
- Catalogue paths catch up so INDEX stops showing a stale root location; nested-count honesty (3 vs undercounted 2) is corrected.
- Does **not** reopen Medium/Early or re-touch Cycle 7 archives.

**Cons / tradeoffs**

- **Paths change** — bookmarks, open terminals, IDE workspaces, or scripts pointing at `C:\Project\PWAExemple` will break until updated.
- **Nested SSH `origin` stays as-is** (`git@github.com:…` under `PWAFrontAuthTest`) — path-only move; no remote URL rewrite. Residual risk if local SSH tooling assumed the old disk path; agent will not push/pull or rewrite remotes.
- **Opaque `.env`×4** ride with the tree unread — if recovery/`robocopy` is needed, implementer must still never open/log secret contents; attestation is path presence only.
- **Windows nested-`.git` lock** possible with 3 roots (Cycle 7 precedent) — recovery Continuity may briefly leave a split tree until reunify + robocopy finishes; logged as process deviation, not a new map.
- Multi-experiment row will **still be open** after this cycle (`WorkSpace` remaining, fail-closed) — you are **not** approving “done with Multi-experiment” or jumping Primary next.

Prior Continuity / Choose-all / starting this FAW is **not** this approval. Orchestrator must pause here and obtain an explicit yes on this plan/map before launching implementer.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | `fs_mutation` |
| Batch name | Cycle 8 Multi-experiment — remaining subset (`PWAExemple` only) |
| Corpus FS | Intentional move of the one approved wrapper tree only (all 3 nested `.git` included; opaque `.env`×4 unread); parent `archive` already exists (create only if missing) |
| User approval before implementer | **Required** — plan-gate on this map (orchestrator pause) |
| Docs attestation after moves | INDEX (+ inventory nested 2→3) updated for `PWAExemple`; ROADMAP Notes → **partial progress** (remaining **`WorkSpace` only**); row **not** Complete |
| Push / remote publish | **Not required** — dual auth/preflight N/A |

### Continuity / later-row gates (documented — do not upgrade labels)

Per refined prompt + Continuity (do **not** re-litigate global taxonomy/must-preserve solely to unblock this Multi-experiment remaining subset; do **not** claim final ratification):

| Gate | Status for this cycle |
| --- | --- |
| Taxonomy | **Satisfied via Continuity** — remains **proposed-ratified — ready for user sign-off** (not final without explicit user sign-off); Early/simple/Medium-style binding reused — **not** global final corpus ratification |
| Must-preserve | **Satisfied via Continuity** — remains **draft — not auto-locked / for user review**; `PWAExemple` **not** on draft list; `WorkSpace` is on draft Medium but is **out of this map** (fail-closed defer — flag only, do not invent final lock) |
| Per-batch path list | **This plan’s move map** — still needs **explicit user plan-gate yes** before implementer |

**Remaining gate before implementer:** user plan-map approval only (see section above).

---

## Explicit move map (matches research Option A — no deviation)

| # | Source | Status (90d) | Destination | Nested `.git` stays under (atomic) |
| --- | --- | --- | --- | --- |
| 1 | `C:\Project\PWAExemple` | `archive` | `C:\Project\archive\2025.06.25 - PWAExemple` | `…\PWAExempleAuth\PWAExempleAuth\PWAExempleAuth\.git` (HTTPS), `…\PWAExempleNext\.git` (HTTPS), `…\PWAFrontAuthTest\.git` (**SSH**) |

**Parents:** `C:\Project\archive` exists (research); create only if missing at implement. `paused` / `active` not required for this batch.

**Unit:** whole top-level wrapper tree (`Move-Item -LiteralPath`), including **all** nested `.git` and non-git children + opaque `.env` paths. Prefer rename/move over copy+delete; never delete payload to “clean up.” Secrets/deps opaque — do not open `.env` (path-only logging OK). **No SSH/remote URL rewrite** (path-only).

### Windows nested-`.git` lock recovery (Continuity — allowed deviation)

Prefer single `Move-Item`. On `PermissionDenied` / mid-move split:

1. Reunify remaining children into the destination dated folder.
2. Finish remaining children with `robocopy /E /MOVE`.
3. Remove **only empty** leftover `.git` shells (0 children); **never** delete non-empty payload.
4. Re-attest all 3 destination nested `.git` + opaque `.env`×4 via `Test-Path`.
5. Log as **process deviation** (not scope expansion / not a new map).

### Deferred / remaining (not in this map)

| Folder | Role | Plan action |
| --- | --- | --- |
| `WorkSpace` | **Fail-closed defer** (still) | Do not move; log multi-remote + unexpected `_backups`/`_quarantine` roots + XL; later **git-strategy** candidate — not this batch |
| `GitTest`, `WorkStationPWA` | Cycle 7 archives | Verify-only at archive paths; **never re-propose** as sources |
| Medium / Early archive & paused paths | Verify-only | Confirm present; **never** re-propose as sources |

### Secrets / opaque payload (path-only; never read)

| Item | Research finding | Handling |
| --- | --- | --- |
| `PWAExemple` | **4** opaque `.env*` paths | Move with tree; **never read or log contents**; post-move `Test-Path` destination paths only |

Expected opaque paths (relative under wrapper → under destination after move):

| Pre-move (under `C:\Project\PWAExemple\`) | Post-move (under `C:\Project\archive\2025.06.25 - PWAExemple\`) |
| --- | --- |
| `PWAExempleAuth\PWAExempleAuth\PWAExempleAuth\pwa-exemple-auth-app\.env` | same relative under destination |
| `PWAExempleNext\pwa-test-app\.env` | same relative under destination |
| `PWAExempleNext\pwa-test-app\.env.local` | same relative under destination |
| `PWAFrontAuthTest\pwa-front-auth-test-app\.env` | same relative under destination |

### Destination attestation (implementer AC — required)

After successful move (or after lock recovery), attest with `Test-Path` (boolean only; no file open):

| Destination nested `.git` | Destination opaque `.env*` |
| --- | --- |
| `C:\Project\archive\2025.06.25 - PWAExemple\PWAExempleAuth\PWAExempleAuth\PWAExempleAuth\.git` | `…\PWAExempleAuth\PWAExempleAuth\PWAExempleAuth\pwa-exemple-auth-app\.env` |
| `C:\Project\archive\2025.06.25 - PWAExemple\PWAExempleNext\.git` | `…\PWAExempleNext\pwa-test-app\.env` |
| `C:\Project\archive\2025.06.25 - PWAExemple\PWAFrontAuthTest\.git` | `…\PWAExempleNext\pwa-test-app\.env.local` |
| — | `…\PWAFrontAuthTest\pwa-front-auth-test-app\.env` |

Log: path + `True`/`False` only. If expected nested `.git` missing post-move → Critical. If an opaque `.env*` was present pre-move and absent post-move → Critical.

### Fail-closed unexpected hazards (implementer re-scan)

Immediately before the move, re-check. On any of the following → **skip + log**; do **not** invent git-strategy mid-batch; do **not** expand the map to `WorkSpace` / Medium / Early / Cycle 7 archives:

- Destination already exists (no overwrite / merge)
- Source missing
- Unexpected **extra** nested `.git` beyond the expected three (or linked worktrees / messy multi-remote that was not present at research)
- Any path outside this approved map

**SSH alone is not hard fail-closed** for `PWAFrontAuthTest` under Continuity (path-only; residual informational risk).

Hard fail-closed items stay deferred/skipped; do not substitute other folders without a new plan gate. Subset may shrink to **zero** if `PWAExemple` fails preflight — still do not force `WorkSpace`.

### Verify only — do not move

| Path / set | Action |
| --- | --- |
| Cycle 7: `archive\2025.08.08 - GitTest`, `archive\2025.07.01 - WorkStationPWA` | Confirm still present; roots absent; **no re-move** |
| Medium Cycle 4–6 archive/paused destinations | Confirm still present; **no re-move** |
| Early/simple archive/paused destinations | Confirm still present; **no re-move** |
| `C:\Project\WorkSpace` | Confirm still at root; **no move this cycle** |

**Out of map (do not move):** `WorkSpace`; Cycle 7 archives as sources; Medium/Early trees; must-preserve draft paths; organisation repo; hygiene orphans; Obsidian / ProjetOrif / special-git rows.

---

## Acceptance criteria

### Before implementer (orchestrator / plan gate)

- [ ] Continuity / Answers lock Q1–Q4 (prefer green `PWAExemple`; `WorkSpace` fail-closed; multi-git caution; SSH path-only; Continuity carry).
- [ ] Research live-checked only remaining Multi-experiment candidates (`PWAExemple`, `WorkSpace`); Option A map with deferred `WorkSpace` + reason documented.
- [ ] Plan shortlist is explicit: **`PWAExemple` only** (shrink only on fail-closed skip).
- [ ] Plan contains the exact one-row move map above, declares `fs_mutation`, and states atomic nested-git (×3) + opaque-secrets (×4) + SSH path-only (no remote rewrite) + Windows lock-recovery Continuity.
- [ ] Plan includes “What the user is approving” (plain language + path map + pros/cons).
- [ ] Taxonomy wording stays **proposed-ratified — ready for user sign-off**; must-preserve stays **draft — not auto-locked / for user review** (no label upgrade).
- [ ] User **explicitly** approved this plan/map in-session (plan gate). Continuity Choose ≠ this approval.

### After implementer (auditor-checkable)

- [ ] Exactly the approved folder moved once (unless fail-closed skip); **no** extras outside the approved map; **no** Medium/Early re-moves; **no** re-move of `GitTest` / `WorkStationPWA`; **no** `WorkSpace` move.
- [ ] Preflight at implement: source existed; target did not; wrapper still contains its expected nested `.git`×3 after move (if present pre-move).
- [ ] Post: source absent; target present at destination above (or user-approved edits only).
- [ ] **Destination nested-git attestation:** `Test-Path` True for each of the 3 expected destination `.git` paths above.
- [ ] **Opaque `.env`:** all 4 destination `Test-Path` True and **no secret contents** in session logs.
- [ ] If Windows nested-`.git` lock occurred: reunify + `robocopy /E /MOVE` Continuity followed; only empty leftover `.git` shells removed; re-attest; logged as deviation (not silent payload delete).
- [ ] Unexpected hazards → item **skipped + logged** (fail-closed; no git-strategy invent; no map expansion to `WorkSpace`).
- [ ] Parent `C:\Project\archive` exists as needed.
- [ ] `catalogue/INDEX.md`: Status / date label / **current path** updated for `PWAExemple` → archive path; nested note **3** (not 2); `WorkSpace` row still honest at root; Cycle 7 / Medium / Early archive rows unchanged.
- [ ] `catalogue/inventory.md` path/status/nested notes refreshed for `PWAExemple` when they still imply root-only or undercounted nesting (2→3).
- [ ] Optional Continuity note only: keep taxonomy **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
- [ ] `program/ROADMAP.md`: Multi-experiment Notes show **partial progress** — Cycle 7 moved `GitTest`, `WorkStationPWA`; Cycle 8 moved `PWAExemple` → `archive`; **remaining:** **`WorkSpace` only** (fail-closed / git-strategy later; nearly-complete style OK). Row stays **Primary next / in progress** — **do not** mark Complete; **do not** jump Primary next away from Multi-experiment while `WorkSpace` remains.
- [ ] Implementation log lists `from → to`, nested-git + `.env` attestations, any lock-recovery deviation, skip reasons, Medium/Early + Cycle 7 verify-only notes, SSH-left-as-is note, deferred `WorkSpace`, and **reverse-move** notes.
- [ ] Org repo tree and must-preserve draft list unchanged (no rewrite of draft entries).
- [ ] On Critical fail: reverse-move documented (and applied if needed); cycle not marked complete with unmet AC.
- [ ] No agent `git push` / `git pull` / remote publish attempted for this cycle.
- [ ] No SSH/remote URL rewrite on any nested remote.

**Not hard AC (optional / if cheap):** size / band metadata, inventory size lag vs live, remote-scheme “informational” notes beyond path-only attestation — include when cheap; do not false-fail audit on size fields or optional metadata.

---

## Ordered steps

### Step 0 — Orchestrator plan gate (blocking)

- **Paths:** this `plan.md`
- **Action:** Present move map + “What the user is approving” (plain language + pros/cons, including nested SSH origin stays as-is; `.env` opaque; row stays in progress with remaining `WorkSpace`). Obtain explicit yes (or edited map). Do **not** start implementer without yes.
- **Verify:** Session note or handoff records plan-gate approval.

### Step 1 — Implementer preflight (fail-closed)

- **Paths:** source + destination + `C:\Project\archive`; expected nested `.git`×3; opaque `.env`×4; Cycle 7 archive destinations (verify-only); Medium/Early archive/paused destinations (verify-only); `WorkSpace` (confirm not targeted)
- **Action:** `Test-Path` source exists; destination absent; parent will be directory. Confirm expected nested `.git` still present (exactly three unless research-aligned). Record pre-move opaque `.env*` `Test-Path` for all four (boolean only). Re-probe worktree/remote hazard screen lightly (or equivalent recurse + `git worktree list` / `remote -v` at nested roots). If unexpected extra `.git` / linked worktrees / multi-remote / collision → **skip**, log, do not invent git-strategy, do not substitute `WorkSpace`/Medium/Early/Cycle 7 archives. Confirm Cycle 7 + Medium/Early destinations present and not re-targeted. Do **not** rewrite remotes.
- **Verify:** Preflight table in `04-implementation/log.md`.

### Step 2 — Create status parent if needed

- **Paths:** `C:\Project\archive`
- **Action:** `New-Item -ItemType Directory` if missing. Do not create `paused` / `active` for this batch.
- **Verify:** `archive` exists as a directory.

### Step 3 — Move tree

- **Paths:** move map row 1 (`PWAExemple`)
- **Action:** Prefer `Move-Item -LiteralPath <source> -Destination <destination>` (rename-in-move into parent). Same volume; whole wrapper including all nested `.git` + opaque `.env`×4; no copy-delete; secrets/deps opaque (do not open); **no remote URL rewrite**.
- **Windows lock recovery (if needed):** On `PermissionDenied` / mid-move split → reunify into destination; `robocopy /E /MOVE` for remaining children; remove **only empty** leftover `.git` shells; never delete non-empty payload; re-attest; log as Continuity process deviation (not a new map).
- **On failure without recovery success:** stop; reverse if Critical (see rollback).
- **Verify:** Source gone; destination present; nested `.git`×3 under expected relative child paths; all four `.env*` destination `Test-Path` True.

### Step 4 — Destination attestation

- **Paths:** destination nested `.git`×3 + opaque `.env`×4 table above
- **Action:** `Test-Path` each listed path; record True/False in log only (no file open/read). Optionally note `PWAFrontAuthTest` nested remote still SSH (read `remote -v` URLs only — do not rewrite).
- **Verify:** All expected nested `.git` True; all four opaque `.env*` True.

### Step 5 — Catalogue updates (org repo docs only)

- **Paths:**
  - `catalogue/INDEX.md` — `PWAExemple` row: Status `archive`; date label applied (drop “proposed” / TBD markers); **current path** → destination; nested note **3** (fix 2→3 drift); leave `WorkSpace` at root honestly; leave Cycle 7 / Medium / Early archive rows as-is; refresh “What’s next” so Multi-experiment shows remaining **`WorkSpace` only** (not Complete).
  - `catalogue/inventory.md` — refresh path/status/nested notes for `PWAExemple` (2→3 nesting); optional size-band honesty if cheap (M-band).
  - `catalogue/taxonomy.md` — optional Continuity note only; keep **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.
  - `catalogue/must-preserve.md` — **do not** rewrite / “lock” draft; `WorkSpace` stay draft Medium flag only.
- **Action:** Edit docs to match disk; no other catalogue churn.
- **Verify:** Grep/read shows new archive path for `PWAExemple` with nested 3; `WorkSpace` still root; Cycle 7 / Medium / Early archives unchanged; org-repo protect row unchanged.

### Step 6 — ROADMAP partial progress (not Complete)

- **Paths:** `program/ROADMAP.md`
- **Action:** Update Multi-experiment Notes for **partial progress**: Cycle 7 moved `GitTest`, `WorkStationPWA` → `archive`; Cycle 8 moved `PWAExemple` → `archive`; **remaining:** **`WorkSpace` only** (fail-closed / git-strategy later; nearly-complete / soft-deferred style wording OK). Keep row as **Primary next → Multi-experiment** / in progress. **Do not** mark Multi-experiment Complete while `WorkSpace` remains. **Do not** reopen Medium wrappers or Early/simple. Update “How the next cycle starts” to lock **same row / remaining name** (`WorkSpace` or dedicated git-strategy — not Primary next jump).
- **Verify:** Notes show remaining **`WorkSpace`**; no Complete claim; Primary next still Multi-experiment.

### Step 7 — Session implementation log

- **Paths:** `sessions/2026.09.10-0811/04-implementation/log.md` (+ `changes.md` as usual)
- **Action:** Record `from → to`, nested `.git`×3 + `.env`×4 attestations, any Windows lock-recovery deviation, skip reasons, Cycle 7 + Medium/Early verify-only notes, SSH-left-as-is note for `PWAFrontAuthTest`, deferred `WorkSpace` reason, and **reverse-move** command/path (table below). Attest: zero intentional moves outside the approved map; zero corpus deletes of payload; no secret contents logged; no push/pull; no remote rewrite; ROADMAP not marked Complete.
- **Verify:** Log complete before claiming implementation done.

### Step 8 — Auditor

- **Action:** Check acceptance criteria checklist against disk + catalogue + ROADMAP + log.
- **Verify:** Pass / fail with evidence; Critical unmet → not complete.

**Push / pull preflight:** skipped (N/A — no remote publish).

---

## Non-goals

- Moving `WorkSpace` in this batch (or forcing a dedicated git-strategy **execution** unless a later approved plan clears hazards)
- Marking Multi-experiment ROADMAP row **Complete** while `WorkSpace` remains unmoved/deferred
- Jumping Primary next / Special git / Obsidian / ProjetOrif / WebCatalogue / HTTP Battles / hygiene this cycle
- Reopening or re-moving Medium wrappers (Cycle 4–6) or Early/simple (Cycle 2–3) destinations as sources
- Re-moving or “fixing up” Cycle 7 archive destinations for `GitTest` / `WorkStationPWA`
- Rewriting git remotes / history / filter-repo / worktree repair / splitting wrappers from nested git
- Treating unexpected multi-git hazards as anything other than skip+log (no mid-batch git-strategy invent)
- Touching must-preserve draft paths as move sources; upgrading taxonomy or must-preserve to final without explicit user sign-off
- Relocating or restructuring the organisation repo
- Agent remote push, pull, or publish
- Reading or logging secret file contents
- Making optional size/band/metadata signals into hard AC checkboxes
- Deleting non-empty leftover trees during lock recovery (empty `.git` shells only)

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Unexpected nested `.git` / worktree / multi-remote at implement time | Fail-closed: skip; log; no git-strategy; no map expansion to `WorkSpace` |
| Target collision | Skip overwrite; log; do not merge |
| Windows nested-`.git` lock / mid-move split | Continuity: reunify + `robocopy /E /MOVE`; empty shells only; re-attest; log deviation |
| Secret leakage via logs | Path-only for `.env*`; never open/read contents; attestation = `Test-Path` boolean |
| SSH residual (`PWAFrontAuthTest`) | Path-only; leave origin URL as-is; no agent push/pull; called out in plan-gate cons |
| INDEX nested-count drift (2 vs 3) | Step 5 hard requirement to record **3** after reality |
| Catalogue / ROADMAP drift after FS move | Steps 5–7 same acceptance batch as moves; ROADMAP partial only (`WorkSpace` remaining) |
| Accidental Medium/Early / Cycle 7 / WorkSpace move | Explicit non-goals + Step 1 verify-only |
| Path bookmarks break | Called out in plan-gate pros/cons; user accepts by approving |
| False Complete | Never mark Multi-experiment Complete while `WorkSpace` remains |

### Reverse-move notes (encode in implementation log)

| Forward | Reverse (do not delete payload) |
| --- | --- |
| `C:\Project\PWAExemple` → `C:\Project\archive\2025.06.25 - PWAExemple` | Move dated folder back to `C:\Project\PWAExemple` |

Empty `archive` parent may remain after reverse (harmless). Nested `.git`×3 and opaque `.env`×4 ride with the wrapper on reverse (same atomic unit). Remote URLs remain whatever they were (no rewrite on reverse either).

**Critical rollback policy:** If a move succeeds then a later hard failure leaves AC unmet, reverse using the table above, document in log, do not mark cycle complete.

---

## Verification checklist (auditor quick list)

1. Source absent; destination present for non-skipped approved row.  
2. Nested `.git`×3 intact under expected relative children; destination `Test-Path` attested.  
3. Opaque `.env`×4 destination `Test-Path` True; no secret contents in logs.  
4. If lock recovery used: reunify + robocopy Continuity; empty shells only; deviation logged.  
5. Skipped row (if any) has hazard/collision evidence in log; no silent map expansion to `WorkSpace`/Medium/Early/Cycle 7.  
6. Cycle 7 + Medium/Early archive/paused destinations untouched; `WorkSpace` still at root.  
7. INDEX + inventory updated for `PWAExemple` (path + nested **3**).  
8. ROADMAP: partial Notes (**remaining: `WorkSpace` only**); Multi-experiment **not** Complete; Primary next still Multi-experiment.  
9. Org repo / must-preserve draft list untouched as move sources; Continuity labels not upgraded to final.  
10. Reverse-move notes present for successful move.  
11. No push/pull attempted; no SSH/remote URL rewrite.  

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
