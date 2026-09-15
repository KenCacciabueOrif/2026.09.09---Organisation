# Plan — Cycle 23: Clearance #4 approval (named hermes-agent map)

**Session:** `sessions/2026.09.15-1432/03-plan/`  
**ROADMAP lock:** Multi-experiment — **Remaining: `WorkSpace` only** (Continuity X)  
**Prior research:** `02-research/research-brief.md` — anti-loop **proceed**; material advance = #4 DRAFT→**approved** for named nest map  
**Continuity:** Q1–Q5 = **A**; Continuity ≠ execute; Q3=A **NO_AUTO_COMMIT**; Q4=A plan gate required  
**STAGE:** **1 — HOLD** at plan gate. Do **not** start implementer until user answers the Exact user-gate question.

---

## Goal restatement

Flip Clearance **#4** from **DRAFT written / approval pending** (Cycle 20) to **approved for one named nest map only**: intact relocate of `hermes-agent` → dated archive leaf `C:\Project\archive\2026.09.15 - hermes-agent`. Record that approval in surgery/hazards/ROADMAP/INDEX honesty docs **without** rewriting the full parent-surgery procedure. Nest filesystem mutation stays **held** unless the user also chooses **A+E** (approve **and** execute this STAGE 2). Never mark Multi-experiment Complete; never jump Primary next; never reopen dashboard; never silent whole-tree archive.

---

## Mutation class

| Slice | Class | When |
| --- | --- | --- |
| **Primary (gate A)** | `docs_only` | After plan-gate **A** — #4 status flip + honesty only; **zero** nest / TNA / WorkSpace path moves |
| **Optional (gate A+E)** | `fs_mutation` (`path_batch`) | After plan-gate **A+E** — same approval **plus** execute the named hermes intact move this STAGE 2 |
| **hold / amend** | n/a | No implementer; orchestrator records choice; session stays held / amended |

**Corpus FS attestation (docs_only):** implementer logs `Test-Path` (or Read/Glob equivalent) that source nest still exists at original path and destination leaf was **not** created this cycle.  
**Corpus FS attestation (A+E):** implementer runs surgery preflight → Move-Item → post-attest per `program/git-strategy-tna-parent-surgery.md`; reverse-move note; **NO_AUTO_COMMIT** on dirty TNA.

**ready_to_implement:** **`no`** until plan gate **A** or **A+E** (or explicit amend that still names an exact map).

---

## Named path map (exact)

| Role | Absolute path |
| --- | --- |
| **Source (nest)** | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` |
| **Destination (archive leaf)** | `C:\Project\archive\2026.09.15 - hermes-agent` |
| **Parent envelope (not moved)** | `C:\Project\WorkSpace\TestNewWorkspaceAgent` (TNA) |
| **Wrapper (not moved)** | `C:\Project\WorkSpace` |

**Remotes:** path-only (no `set-url` / origin rewrite / force-push).  
**Atomic unit:** entire nest tree including `.git`.  
**Out of map:** orchestrateur, WorkshopOrif, TNA envelope, whole WorkSpace, OS-IA, Appendix A parents, Medium/Early/archived Multi peers.

User may **amend** destination class (archive → paused/sibling) or leaf name at the gate; amend must restate exact source→dest before STAGE 2.

---

## What the user is approving (plain language)

This plan gate is **separate from Continuity** (Q1–Q5 A already locked). Continuity only chose the workstream; it did **not** approve nest moves or flip #4.

| Answer | Meaning of “yes” | What happens next |
| --- | --- | --- |
| **A** | You approve Clearance **#4** for **this named map only** (hermes-agent → dated archive leaf). Implementer updates org-repo honesty docs so #4 is **approved for that map**. Nest stays on disk where it is. | STAGE 2 = `docs_only`. Future FAW can propose execute without re-litigating #4 for **this same map** (still needs a dedicated execute gate unless you later pick A+E). |
| **A+E** | Same #4 approval **and** you authorize **execute now**: intact move of hermes-agent to the destination this STAGE 2. | STAGE 2 = `fs_mutation` after preflight (incl. absolute-path consumer scan). Nested live count under WorkSpace expected **4→3**. Still **not** Multi-experiment Complete. |
| **hold** | No approval, no docs flip, no move. | Cycle stops at gate; Next FAW remains WorkSpace / #4. |
| **amend** | You change the map (dest class, leaf name, or scope) before approving. | Planner/orchestrator revises map; new gate required — do not implement on stale map. |

**Important distinctions**

- **“Approved”** unlocks future extract for **this named map**; it does **not** by itself move files (**A**) and does **not** flip whole-tree clearance **NO→yes** (#1–#6 still bind).
- **A+E** means move **now** (higher risk: Windows locks, absolute-path consumers under dirty TNA).
- Approving #4 “in principle” without this exact map is **forbidden** (anti-loop / theater).

### Pros / cons (tradeoffs)

| Option | Pros | Cons |
| --- | --- | --- |
| **A** | Material #4 status flip; lowest FS risk; anti-loop clean; matches “named nest extract plan” deferred from Cycle 20 | Nest still under TNA until a later execute cycle; bookmarks/paths unchanged today |
| **A+E** | Maximum concrete progress (one nest out; 4→3); #4 approved + executed in one session | Needs consumer scan; Windows lock / reverse-move risk; higher consent burden; may break absolute-path refs under dirty TNA (~2307) — **NO_AUTO_COMMIT** still applies |
| **hold** | Zero change; time to rethink dest | No material advance this cycle |
| **amend** | Correct dest/scope before locking | Extra gate round; delay |

---

## Exact user-gate question (orchestrator copy-paste)

```text
Plan gate — Cycle 23 Clearance #4 (named hermes-agent map)

Plain language: Continuity already chose WorkSpace / Continuity X. This gate is separate.
We will NOT rewrite the full surgery procedure. We will NOT mark Multi-experiment Complete
or jump Primary next. Dirty TNA stays disclose-only (NO_AUTO_COMMIT).

Named map:
  FROM: C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent
  TO:   C:\Project\archive\2026.09.15 - hermes-agent
  (intact nested clone; remotes path-only; TNA + WorkSpace stay put)

Reply with ONE of:

  A     Approve Clearance #4 for this named map + honesty docs only
        (zero nest filesystem moves this cycle; “approved” unlocks future extract
         for this map, but does not move files now)

  A+E   Approve #4 for this map AND execute the intact hermes-agent → archive
        move this STAGE 2 (fs_mutation after preflight + consumer scan)

  hold  Do nothing this cycle (no approval flip, no move)

  amend <your exact source→dest or other change>
        (we will revise the plan and re-ask before any implement)

Pros/cons (short):
  A   = material #4 flip, lowest risk; nest stays until a later execute gate
  A+E = move now (4→3 nests); higher lock/consumer-breakage risk; still not Complete
  hold / amend = no or delayed advance

What does “yes” commit to?
  A   → docs flip #4 DRAFT→approved-for-this-map only
  A+E → that approval PLUS the move now
```

---

## Acceptance criteria

### Shared (all successful STAGE 2 paths)

- [ ] Plan-gate answer recorded in session notes (`01-prompt-betterment/notes.md` or SESSION) with exact map
- [ ] Clearance #4 **not** claimed “approved” without gate **A** or **A+E**
- [ ] Full surgery procedure in `program/git-strategy-tna-parent-surgery.md` **not** rewritten as “progress” (status / nest-table / Next FAW hint edits only)
- [ ] Multi-experiment remains **in progress / Remaining: `WorkSpace` only** — **not** Complete; **no** Primary next / Special git jump
- [ ] Whole-tree clearance still **NO** (even after A+E success)
- [ ] Taxonomy stays **proposed-ratified — ready for user sign-off** (not final); must-preserve **draft — not auto-locked**
- [ ] Dirty TNA: disclose porcelain; **`NO_AUTO_COMMIT=true`** — no stash/commit/clean of bulk TNA WT
- [ ] Dashboard / catalogue items 20–22 **not** reopened as this cycle’s topic
- [ ] OS-IA, Appendix A, Medium/Early/archived Multi peers **not** in move sources
- [ ] Dual mid+final git-manager (Q5=A) for allowlisted org-repo dirt after implement; fail-closed if agent push blocked — never false `complete`

### Slice A only (`docs_only`)

- [ ] `#4` status lines flipped to **approved for named hermes-agent → `C:\Project\archive\2026.09.15 - hermes-agent` map** (or equivalent precise wording) in:
  - `program/git-strategy-tna-parent-surgery.md`
  - `program/git-strategy-workspace-hazards.md` (criterion #4 row + related)
  - `program/ROADMAP.md` Notes / Next FAW honesty as needed
  - `catalogue/INDEX.md` and/or `catalogue/inventory.md` honesty as needed
- [ ] Nest table / policy still states execute requires dedicated gate **unless** this cycle already executed (N/A for A)
- [ ] **Zero** nest / TNA / WorkSpace path moves — implementer attests source still present; dest leaf **not** created by this cycle
- [ ] Next FAW hint: **WorkSpace only** + Continuity X continue (#4 approved-for-map; nest extract still pending **or** next named nest)

### Slice A+E (`fs_mutation` path_batch) — additional

- [ ] Preflight on **nested clone path only** (not TNA/WorkSpace wrappers): `Test-Path` source; dest parent exists; dest leaf free; `git worktree list` (expect 1); remotes names+schemes; porcelain disclose; ignore/not-submodule check; opaque `.env*` presence-only if listed
- [ ] **Absolute-path consumer scan** (presence-only) under dirty TNA before move — log method + findings; fail-closed or disclose residual risk per surgery policy
- [ ] Intact `Move-Item` (robocopy `/E /MOVE` only as Windows lock recovery; empty `.git` shells only)
- [ ] Post-attest: nest toplevel at destination; remotes unchanged; source gone/empty-shell cleaned; reverse-move note logged
- [ ] Honesty: nested live count under WorkSpace **4→3**; INDEX/inventory/ROADMAP Notes updated; Multi-experiment still **not** Complete
- [ ] No auto-commit of dirty TNA / coupled parent dirt

### hold / amend

- [ ] No #4 approval flip; no nest FS; orchestrator records choice; `ready_to_implement` stays **no**

---

## Ordered steps

### STAGE 1 — Plan gate (now)

| Step | Action | Files / paths | Verification |
| --- | --- | --- | --- |
| 0 | Orchestrator presents Exact user-gate question (copy-paste block above) with plain language + pros/cons | User chat; optional note in `SESSION.md` | User reply ∈ {A, A+E, hold, amend…} |
| 1 | Record gate answer + exact map (or amend) in session notes | `01-prompt-betterment/notes.md`, `SESSION.md` | Written; Continuity ≠ substitute for this answer |
| 2 | If **hold** → skip implementer + mid git; still auditor → self-improver → final git for session honesty if dirt exists. If **amend** → revise plan map; **re-ask** gate. If **A** or **A+E** → set `ready_to_implement: yes` and continue STAGE 2 same session | Session docs | Branch matches answer |

### STAGE 2A — After gate **A** (`docs_only`)

| Step | Action | Files / paths | Verification |
| --- | --- | --- | --- |
| 3 | Flip #4 status to **approved for named hermes-agent archive map**; cite Cycle 23 session; **do not** rewrite procedure sections | `program/git-strategy-tna-parent-surgery.md` | Status line + definition table; procedure body intact |
| 4 | Align hazards criterion #4 + related honesty (nested count unchanged) | `program/git-strategy-workspace-hazards.md` | #4 = approved-for-map; whole-tree still NO |
| 5 | ROADMAP Notes / Primary-next honesty: WorkSpace only remains; note #4 approved-for-hermes-map; extract still pending | `program/ROADMAP.md` | Not Complete; no Primary next jump |
| 6 | INDEX / inventory honesty as needed (status of nest location unchanged) | `catalogue/INDEX.md`, `catalogue/inventory.md` | Paths still show live hermes under TNA |
| 7 | Zero-move attestation in implementer log | `04-implementation/log.md` | Probe method logged |
| 8 | Mid git-manager (allowlisted org-repo) | `05-git/log.md` | Push ok or fail-closed blocked |
| 9 | Auditor → self-improver → **final** closing-pass git | `06-audit/`, `07-self-improvement/`, `05-git/` | No false complete if late dirt unpushed |

### STAGE 2B — After gate **A+E** (`fs_mutation`)

| Step | Action | Files / paths | Verification |
| --- | --- | --- | --- |
| 3 | Same #4 approval honesty as 2A **plus** execute map | surgery + hazards + ROADMAP + INDEX | Approved-for-map **and** nest relocated |
| 4 | Preflight on nest path only + consumer scan | `…\hermes-agent` | Fail-closed per surgery; log probes |
| 5 | Intact move to archive leaf; remotes path-only; reverse-move note | source → `C:\Project\archive\2026.09.15 - hermes-agent` | Post-attest AC |
| 6 | Disclose TNA dirt; **NO_AUTO_COMMIT**; optional empty-dir cleanup only if trivial and logged | TNA | No bulk commit |
| 7 | Honesty: nested **4→3**; remaining nests named; Multi-experiment not Complete | ROADMAP / INDEX / inventory | WorkSpace only Next FAW |
| 8–9 | Mid git → audit → self-improve → **final** git | as 2A | Same publish rules |

---

## Explicit non-goals

- Re-writing full `git-strategy-tna-parent-surgery.md` procedure as cycle “progress”
- Continuity A / empty DRAFT re-attest theater
- Dashboard / catalogue betterment (items 20–22)
- Whole-tree archive of WorkSpace; force-finalize Multi-experiment
- Marking Multi-experiment **Complete** or jumping Primary next / Special git while WorkSpace remains
- Reopening OS-IA, Appendix A, Medium / Early / archived Multi peers as sources
- Approving #4 without a named exact map
- Auto-commit / stash-clean of dirty TNA
- Remote URL rewrite / force-push / history rewrite
- Claiming whole-tree clearance **yes** after docs or after one nest move
- Treating Continuity Q1–Q5 A as plan-gate execute

---

## Rollback / risk notes

| Risk | Mitigation |
| --- | --- |
| User confuses Continuity with execute | Gate text + “What the user is approving”; Q4=A |
| A+E Windows lock / split tree | Surgery reunify + robocopy recovery; reverse-move notes; fail-closed if unresolved |
| Absolute-path breakage (A+E) | Mandatory presence-only consumer scan before move; disclose residual risk |
| Theater / anti-loop | Forbid procedure rewrite; require named map + real status flip |
| False Complete | AC + ROADMAP Step forbid Complete / Primary next while WorkSpace remains |
| Publish auth (MSYS vs GfW) | Prefer GfW absolute path + GCM; fail-closed session `blocked` if agent push fails |

**Rollback (A):** revert org-repo honesty commits / docs to DRAFT wording.  
**Rollback (A+E):** reverse-move dest → source **only if** source empty and dest complete (per surgery); then honesty recount.

---

## Context citations

- Surgery policy (cite; do not rewrite): `program/git-strategy-tna-parent-surgery.md`
- Hazards: `program/git-strategy-workspace-hazards.md`
- ROADMAP: `program/ROADMAP.md`
- Research: `sessions/2026.09.15-1432/02-research/research-brief.md`
- Continuity: `sessions/2026.09.15-1432/01-prompt-betterment/notes.md`

---

## Blocking questions

**None for planning** — map and options are concrete.  
**Blocking for implementer:** unanswered plan gate (**A / A+E / hold / amend**).

---

## Planner return fields

| Field | Value |
| --- | --- |
| **ready_to_implement** | **no** (until gate A or A+E) |
| **mutation_class** | Primary `docs_only` (A); optional `fs_mutation` path_batch (A+E) |
| **blocking_questions** | Plan-gate choice required (see Exact user-gate question) |
| **step_count** | STAGE 1: 3 steps; STAGE 2A: 7 implement+close steps; STAGE 2B: 7 implement+close steps (shared close pattern) |
