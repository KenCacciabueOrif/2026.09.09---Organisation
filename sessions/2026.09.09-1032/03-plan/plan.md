# Plan — Cycle 2 Early/simple subset (fs_mutation)

**Session:** `sessions/2026.09.09-1032/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md`  
**Approach:** Research Option A — sequential same-volume `Move-Item` (whole trees), with embed pre-checks (existence, collision, `.git` re-scan).

---

## Goal

Execute the first real corpus move slice for ROADMAP **Early/simple**: move exactly three low-risk folders under `C:\Project` into dated status parents (`archive` / `paused`), update catalogue rows for those three only, and log each forward path with reverse-move notes. No other Early/simple folders, must-preserve paths, or org-repo changes. Moves run only after the orchestrator obtains **explicit user plan-gate approval** of this map.

---

## What the user is approving (plan gate)

You are approving **this exact three-folder move map** (not “do the cycle” in general). After you say yes, the implementer will rename/relocate these folders on disk and update catalogue docs to match.

| Approve? | Meaning |
| --- | --- |
| **Yes** | Create `C:\Project\archive` and `C:\Project\paused` if missing; move the three sources to the destinations below; update INDEX (+ inventory); leave deferred folders and must-preserve paths alone. |
| **No / edit** | No moves; revise map or defer. |

**Pros**

- Dated, status-bucketed paths (`archive` / `paused`) match the taxonomy layout and make old vs recent experiments easier to navigate.
- Smallest/safest first batch (tiny trees, no `.git` found in research).

**Cons / tradeoffs**

- **Paths change** — bookmarks, shortcuts, open terminals, or scripts pointing at the old `C:\Project\…` roots will break until updated.
- Parents `archive` / `paused` appear under `C:\Project` (new top-level folders).
- Batch is not all-or-nothing across three rows: if one fails mid-way, already-moved items may need reverse-move (documented per row).

Prior “do next cycle” / taxonomy consent is **not** this approval. Orchestrator must pause here and obtain an explicit yes on this plan/map before launching implementer.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | `fs_mutation` |
| Batch name | Cycle 2 Early/simple subset-of-3 (PostManResponses, PlayTestTristan, ZedTest) |
| Corpus FS | Intentional moves of the three approved source trees only; create `archive` / `paused` parents if missing |
| User approval before implementer | **Required** — plan-gate on this map (orchestrator pause) |
| Docs attestation after moves | INDEX (+ inventory) updated for moved rows only |
| Push / remote publish | **Not required** — dual auth/preflight N/A |

### First-move gates (documented — already satisfied for planning)

Per refined prompt + `01-prompt-betterment/notes.md` Answers (do not re-litigate):

| Gate | Status for this cycle |
| --- | --- |
| Taxonomy binding for Early/simple moves | **Satisfied** — proposed-ratified rules **binding** for this batch; post-success docs may note **user-validated for Early/simple (2026.09.09)** — **not** global “final forever” corpus ratification |
| Must-preserve | **Satisfied for scope** — batch folders **not** on draft list; draft list **untouched** / **draft — not auto-locked**; org repo **protect** |
| Per-batch path list | **This plan’s move map** — still needs **explicit user plan-gate yes** before implementer |

**Remaining gate before implementer:** user plan-map approval only (see section above). First-move taxonomy/must-preserve preconditions for this Early/simple subset are documented as met; do **not** block planning on them again.

---

## Explicit move map (matches research — no deviation)

| # | Source | Status | Destination |
| --- | --- | --- | --- |
| 1 | `C:\Project\PostManResponses` | `archive` | `C:\Project\archive\2025.10.01 - PostManResponses` |
| 2 | `C:\Project\PlayTestTristan` | `archive` | `C:\Project\archive\2025.06.23 - PlayTestTristan` |
| 3 | `C:\Project\ZedTest` | `paused` | `C:\Project\paused\2026.06.30 - ZedTest` |

**Parents to create if missing:** `C:\Project\archive`, `C:\Project\paused`  
(`C:\Project\active` not required.)

**Unit:** whole top-level folder tree per row (`Move-Item -LiteralPath`). Keep PlayTestTristan zip + extract together; include ZedTest `.pytest_cache` as opaque payload (do not delete to “clean”).

**Out of map (do not move):** `IA`, `AngularTest`, `epsic`; must-preserve draft paths; organisation repo; hygiene orphans; anything else under `C:\Project`.

---

## Acceptance criteria

### Before implementer (orchestrator / plan gate)

- [ ] Plan contains the exact three-row move map above and declares `fs_mutation`.
- [ ] User **explicitly** approved this plan/map in-session (plan gate).
- [ ] Research pre-check intent recorded: sources exist; targets absent; `.git` re-scan planned at implement time.

### After implementer (auditor-checkable)

- [ ] Exactly the three approved folders moved once; **not** IA / AngularTest / epsic.
- [ ] Preflight at implement: sources existed; targets did not; unexpected `.git` → that item **skipped + logged** (fail-closed; no git-strategy invent).
- [ ] Post: sources absent; targets present at destinations above (or user-approved edits only).
- [ ] Parents `C:\Project\archive` and `C:\Project\paused` exist as needed.
- [ ] `catalogue/INDEX.md`: Status / date label / **current path** updated for the three; deferred Early/simple rows still show root current paths.
- [ ] `catalogue/inventory.md` path/status notes refreshed for the three moved rows.
- [ ] Optional taxonomy note only: **user-validated for Early/simple (2026.09.09)** — **proposed-ratified — ready for user sign-off** wording preserved where relevant; do **not** claim final forever ratification.
- [ ] Implementation log lists each `from → to` and **reverse-move** notes; skips explained.
- [ ] Org repo tree and must-preserve draft paths unchanged.
- [ ] On Critical fail: reverse-move documented (and applied for already-moved rows); cycle not marked complete with unmet AC.
- [ ] No agent `git push` / remote publish attempted for this cycle.

**Not hard AC:** optional size metadata “if cheap” — do not false-fail audit on size fields.

---

## Ordered steps

### Step 0 — Orchestrator plan gate (blocking)

- **Paths:** this `plan.md`
- **Action:** Present move map + “what the user is approving”; obtain explicit yes (or edited map). Do **not** start implementer without yes.
- **Verify:** Session note or handoff records plan-gate approval.

### Step 1 — Implementer preflight (fail-closed)

- **Paths:** three sources + three destinations + parent dirs
- **Action:** For each row: `Test-Path` source exists; destination absent; parent will be directory. Recurse-scan each source for `.git` (top or nested). If unexpected `.git` → **skip that item**, log, continue others (or stop batch per Critical policy below — default: skip item, do not invent git-strategy). If destination exists → **do not overwrite**; skip + log.
- **Verify:** Preflight table in `04-implementation/log.md`.

### Step 2 — Create status parents

- **Paths:** `C:\Project\archive`, `C:\Project\paused`
- **Action:** `New-Item -ItemType Directory` if missing (do not create `active` unless needed later).
- **Verify:** Both exist as directories.

### Step 3 — Move trees (sequential)

- **Paths:** move map rows 1→2→3
- **Action:** Prefer `Move-Item -LiteralPath <source> -Destination <destination>` (rename-in-move into parent). Same volume; whole tree; no copy-delete; secrets/deps opaque (do not open). On failure: stop further moves; reverse already-successful rows if Critical (see rollback).
- **Verify:** After each row: source gone, destination present.

### Step 4 — Catalogue updates (org repo docs only)

- **Paths:**
  - `catalogue/INDEX.md` — three rows: Status `archive`/`archive`/`paused`; date label applied (drop “proposed”); current path → destinations; leave IA / AngularTest / epsic unchanged.
  - `catalogue/inventory.md` — refresh path/status for the three moved rows.
  - `catalogue/taxonomy.md` — optional one-line Early/simple validation note only (`user-validated for Early/simple (2026.09.09)`); keep **proposed-ratified — ready for user sign-off** framing; must-preserve remains **draft — not auto-locked**.
- **Action:** Edit docs to match disk; no other catalogue churn.
- **Verify:** Grep/read shows three new paths; deferred three still at `C:\Project\{IA|AngularTest|epsic}`.

### Step 5 — Session implementation log

- **Paths:** `sessions/2026.09.09-1032/04-implementation/log.md` (+ `changes.md` as usual)
- **Action:** Record each `from → to`, skip reasons, and **reverse-move** commands/paths (table below). Attest: zero intentional moves outside the approved map.
- **Verify:** Log complete before claiming implementation done.

### Step 6 — Auditor

- **Action:** Check acceptance criteria checklist against disk + catalogue + log.
- **Verify:** Pass / fail with evidence; Critical unmet → not complete.

**Push preflight:** skipped (N/A).

---

## Non-goals

- Moving deferred Early/simple folders: `IA`, `AngularTest`, `epsic`
- Full six-folder Early/simple batch
- Touching must-preserve draft paths (Obsidian, ProjetOrif, WebCatalogue, WorkSpace, HTTP Battles, optional CursorMobileWorkspace / NextPWATraining, …)
- Relocating or restructuring the organisation repo
- Git-strategy / treating unexpected `.git` as anything other than skip+log
- Hygiene orphans, medium / multi-experiment / Obsidian batches
- Agent remote push or history rewrite
- Editing agent/skill workflow files (self-improver explanations debt only)
- Claiming global final taxonomy ratification beyond Early/simple validation note

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Unexpected `.git` at implement time | Fail-closed: skip that item; log; no git-strategy |
| Target collision | Skip overwrite; log; do not merge |
| File lock / open handle | Retry once or skip+log |
| Partial batch (1–2 of 3 moved) | Per-row reverse-move; on Critical failure reverse already-moved rows before marking complete |
| Catalogue drift after FS move | Steps 4–5 same acceptance batch as moves |
| Path bookmarks break | Called out in plan-gate pros/cons; user accepts by approving |

### Reverse-move notes (encode in implementation log)

| Forward | Reverse (do not delete payload) |
| --- | --- |
| `C:\Project\PostManResponses` → `C:\Project\archive\2025.10.01 - PostManResponses` | Move back to `C:\Project\PostManResponses` |
| `C:\Project\PlayTestTristan` → `C:\Project\archive\2025.06.23 - PlayTestTristan` | Move back to `C:\Project\PlayTestTristan` |
| `C:\Project\ZedTest` → `C:\Project\paused\2026.06.30 - ZedTest` | Move back to `C:\Project\ZedTest` |

Empty `archive` / `paused` parents may remain after reverse (harmless).

**Critical rollback policy:** If a move succeeds then a later hard failure leaves AC unmet, reverse already-moved rows using the table above, document in log, do not mark cycle complete.

---

## Verification checklist (auditor quick list)

1. Sources absent; destinations present for all non-skipped rows.  
2. Skipped rows (if any) have `.git` or collision evidence in log.  
3. `IA`, `AngularTest`, `epsic` still at original root paths.  
4. INDEX + inventory updated for the three only.  
5. Org repo / must-preserve draft paths untouched.  
6. Reverse-move notes present for each successful move.  
7. No push attempted.

---

## Ready to implement

| Field | Value |
| --- | --- |
| Plan complete | **yes** |
| `ready_to_implement` | **yes** *(plan artifact complete — implementer still blocked until plan gate)* |
| `requires_user_plan_gate` | **yes** |
| Research blockers | none |
| Push blockers | none (N/A) |

**Orchestrator rule:** Even though `ready_to_implement: yes`, **do not** launch implementer until the user explicitly approves this plan/move map in-session. Prior cycle consent is insufficient.

## Blocking questions

**none** for plan content.  
**Process:** awaiting user plan-gate approval (orchestrator).
