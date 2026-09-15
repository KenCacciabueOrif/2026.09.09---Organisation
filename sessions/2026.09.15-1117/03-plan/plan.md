# Plan — Cycle 20 STAGE 1 (TNA parent-surgery docs / clearance #4)

**Session:** `sessions/2026.09.15-1117/`  
**Phase:** `03-plan/`  
**STAGE:** **STAGE 1 ONLY** — stop after this plan; **user gate required** before any STAGE 2 implement.  
**Continuity locks:** Q1=**A**, Q2=**A**, Q3=**A** (**NO_AUTO_COMMIT**). Continuity ≠ plan-gate execute.

---

## Goal

Continue **Continuity X** for Multi-experiment **remaining `WorkSpace` only** (TNA envelope; live nested **4**) by producing a **material clearance-#4 advance**: write a dedicated **parent-surgery policy** for extracting **ignored nested clones** from the dirty **TestNewWorkspaceAgent (TNA)** tree, and point criterion **#4** in `program/git-strategy-workspace-hazards.md` to **DRAFT written / approval pending**.

This cycle’s execute map is **org-repo docs only** — **zero** corpus nest moves, **zero** TNA envelope relocation, **zero** remote-config. Writing the policy satisfies the **“written”** half of clearance #4; **“approved”** remains deferred to a later dedicated nest `path_batch` plan gate. Whole-tree clearance stays **NO**. Multi-experiment stays **not Complete**.

---

## Mutation class

**`docs_only`**

| Field | Value |
| --- | --- |
| Corpus FS (moves/renames/deletes under `C:\Project` nests / WorkSpace / TNA) | **Zero intentional** — out of execute map |
| Org-repo disk writes | **Allowed** — create `program/git-strategy-tna-parent-surgery.md`; amend `program/git-strategy-workspace-hazards.md` (#4 pointer + nested-4 honesty); optional ROADMAP Notes / INDEX / inventory one-liners |
| Implementer attestation | Log probe method + confirm `Test-Path` / Read that nests were **not** moved; list only org-repo paths touched |
| Plan-gate pause for corpus | **N/A** for nest FS (none planned). **User gate still required** this STAGE 1 before STAGE 2 docs implement (Continuity hold) |
| Future nest extract | **Held** — separate `fs_mutation` `path_batch` + dedicated plan gate after #4 **approved** |

---

## Continuity / locks (carry — do not re-litigate)

| Lock | Value |
| --- | --- |
| ROADMAP | **Primary next → Multi-experiment** / **Remaining: `WorkSpace` only** — **in progress / not Complete** |
| Strategy baseline | `program/git-strategy-workspace-hazards.md` (cite; extend pointer — do not rewrite Cycle 10–19 classification from scratch) |
| Nested live | **4**: TNA + `hermes-agent` + `orchestrateur` + `WorkshopOrif` (all under TNA); OS-IA archive **verify-only** |
| Nest model | **Gitignored nested clones** (not submodules; no `.gitmodules`) |
| Dirty TNA | **~2307** — disclose only; **NO_AUTO_COMMIT** / no stash-as-cleanup |
| Taxonomy / must-preserve | **proposed-ratified / draft** — Q2=A waive; do not claim final sign-off |
| Forbidden | Appendix A re-propose; OS-IA re-move/re-archive; Medium / Early / archived `PWAExemple` peers; silent whole-tree archive; Complete / Primary next / Special git while WorkSpace remains; nest or TNA envelope move this cycle; invent submodule teardown |

---

## Acceptance criteria

### STAGE 1 (this planner deliverable — before gate)

- [x] Mutation class **`docs_only`**; nest/envelope FS **out of execute map**
- [x] Material #4 content specified (not empty Continuity A re-attest) — Option P dedicated artifact
- [x] STAGE 1 **STOP** after planner; Continuity ≠ execute
- [x] Hard forbids encoded (Appendix A, OS-IA, Complete, nest/TNA move, NO_AUTO_COMMIT)
- [x] Next FAW lock hint remains **WorkSpace only** + continue Continuity X clearance / keep-at-root
- [x] `ready_to_implement: no` until user gate **yes**

### STAGE 2 (after gate **yes** — docs implement only)

**Parent-surgery policy artifact (`program/git-strategy-tna-parent-surgery.md`) — “DRAFT written / approval pending” for clearance #4**

The artifact **must** include all of the following sections (anti-loop: procedure substance, not a one-line stub):

- [ ] **Scope / nest table** — named live nested **4** with absolute paths; role (envelope vs in-TNA nest); note OS-IA archived verify-only; classify nests as **ignored nested clones** (cite TNA `.gitignore` lines), **not** submodules
- [ ] **Clearance #4 definition** — **Written** = this policy exists with procedure + fail-closed rules; **Approved** = later dedicated plan-gate **yes** for a named nest `path_batch` (or explicit waiver); Continuity / Choose / STAGE 1 docs / this Cycle 20 docs gate **≠** nest-move approval; writing alone **≠** flip whole-tree clearance **NO → yes**
- [ ] **Preflight (per nest, nest path only)** — `Test-Path` source + destination free; `git worktree list` on **nested clone path** only (fail-closed if unexpected linked worktrees); remotes inventory (names + schemes; path-only); porcelain recount (disclose; do not auto-commit); confirm still ignored / not tracked / not submodule
- [ ] **Atomic nest relocate procedure** — intact OS move of entire nest including `.git`; no history rewrite, no dissolve into parent, no remote URL rewrite; Windows lock recovery per hazards safe rules (reunify / `robocopy /E /MOVE`; empty leftover `.git` shells only)
- [ ] **Parent TNA handling under NO_AUTO_COMMIT** — because nests are gitignored, extract typically does **not** require submodule teardown or a parent commit; **forbid** stash/commit/clean of the ~2307 WT “to enable” the move; allow leave dirty; optional empty-dir cleanup; optional `.gitignore` hygiene only under a future gated step that explicitly allows parent file edits (**not** auto-commit of the bulk WT); residual risk: non-git absolute references — presence-only inventory before execute (do not invent paths now)
- [ ] **Fail-closed conditions** — unexpected linked worktree; path lock unresolved; nest unexpectedly tracked / submodule surprise; destination collision; attempt to move dirty **TNA envelope** or whole `WorkSpace` under this policy without a separate whole-tree / envelope gate
- [ ] **Post-move attest (future execute cycle)** — nest `rev-parse --show-toplevel` at destination; remotes unchanged; worktree list OK; source gone; INDEX/inventory honesty; nested count under WorkSpace updated; Multi-experiment still **not** Complete
- [ ] **Explicit non-goals** — Appendix A; OS-IA reverse/re-archive; Medium/Early/PWAExemple; silent whole-tree archive; remote `set-url` / force-push; auto-commit TNA; claiming clearance_whole_tree **yes** after docs alone
- [ ] **Held defaults for later gates (document, do not execute)** — destination class options (archive vs paused vs sibling under `C:\Project`) marked **held / choose at nest path_batch gate**; empty parent-dir delete preference marked open

**Hazards pointer**

- [ ] `program/git-strategy-workspace-hazards.md` Continuity X / clearance #4 updated to: **DRAFT written (Cycle 20) / approval pending** + link to `program/git-strategy-tna-parent-surgery.md`
- [ ] Nested live count / TNA-only envelope honesty refreshed to **4** (post–OS-IA) where Cycle 19 attestation still says **5** live under WorkSpace in outdated rows — amend without rewriting full Cycle 10–18 history
- [ ] **Clearance for whole-tree archive** remains **NO** (explicit statement that #4 draft ≠ all criteria #1–#6)

**Program / catalogue honesty (as needed)**

- [ ] `program/ROADMAP.md` Notes (if present): Cycle 20 parent-surgery **DRAFT**; Remaining **WorkSpace only**; **not** Complete; Next FAW = WorkSpace only + continue Continuity X clearance / keep-at-root
- [ ] `catalogue/INDEX.md` / `catalogue/inventory.md` — optional one-liner pointing at surgery draft; must **not** claim Complete, whole-tree cleared, or nest moves done
- [ ] Implementer log attests **zero** corpus nest/TNA/WorkSpace path mutations (probe method recorded)

**Hard forbids (STAGE 2 verify)**

- [ ] No nest or TNA envelope move/rename/delete
- [ ] No Appendix A / OS-IA re-propose or execute
- [ ] No Multi-experiment Complete / Primary next / Special git
- [ ] No auto-commit / stash-clean of dirty TNA
- [ ] No claiming clearance #4 **approved** or whole-tree clearance **yes**

---

## Ordered steps

### STAGE 1 (complete at planner — no implement)

| Step | Action | Verification |
| --- | --- | --- |
| 0 | Persist this `plan.md`; orchestrator relays gate | File exists under `03-plan/` |
| 1 | **STOP** — await user answer to Exact user-gate question | No `04-implementation/` product work until gate **yes** |

`ready_to_implement` **now:** **no** (pending gate).

### STAGE 2 (only after gate **yes** — same session resume OK)

| Step | Files / paths | Action | Verification |
| --- | --- | --- | --- |
| 2 | `program/git-strategy-tna-parent-surgery.md` | **Create** full policy covering all AC sections above (scope table with paths below; procedure; NO_AUTO_COMMIT; gate/approval; fail-closed; post-attest; non-goals; held destination defaults) | File exists; sections present; no execute commands run against corpus |
| 3 | `program/git-strategy-workspace-hazards.md` | **Amend** Continuity X: criterion **#4** → **DRAFT written (Cycle 20) / approval pending** + relative link to dedicated file; refresh nested **4** / TNA-only envelope where Cycle 19 live attestation still shows **5**; state whole-tree clearance still **NO** | Diff shows pointer + honesty; no invented Complete; Cycle 10–18 history retained |
| 4 | `program/ROADMAP.md` | Update Notes / Next FAW hint: Cycle 20 surgery **DRAFT**; Remaining WorkSpace only; **not** Complete; continue Continuity X clearance / keep-at-root | Row not Complete; no Primary next jump |
| 5 | `catalogue/INDEX.md`, `catalogue/inventory.md` (optional) | One-liner honesty: parent-surgery draft exists; nests still at live paths; OS-IA archive verify-only | Paths unchanged on disk; no false “moved” claims |
| 6 | `sessions/2026.09.15-1117/04-implementation/` | Log changes + **zero corpus FS** attestation (Read/Glob/`Test-Path` method) | Log lists only org-repo paths; nests still at sources below |
| 7 | Mid git → audit → self-improver → **final closing-pass git** | Per FAW (allowlisted org-repo dirt only) | Session close rules; never claim nest moves |

**Live nest paths (docs table only — do not move):**

| Unit | Absolute path | Role |
| --- | --- | --- |
| TNA | `C:\Project\WorkSpace\TestNewWorkspaceAgent` | Envelope (dirty ~2307; NO_AUTO_COMMIT) |
| hermes-agent | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` | In-TNA nest (ignored) |
| orchestrateur | `C:\Project\WorkSpace\TestNewWorkspaceAgent\Projects\Project Atelier IA\Projet Adrien\orchestrateur` | In-TNA nest (ignored) |
| WorkshopOrif | `C:\Project\WorkSpace\TestNewWorkspaceAgent\Projects\Project Atelier IA\Workshop\WorkshopOrif` | In-TNA nest (ignored) |
| OS-IA | `C:\Project\archive\2026.09.15 - OS-IA` | Archived Cycle 19 — **verify-only** |

**Wrapper:** `C:\Project\WorkSpace` — keep at root; never silent whole-tree archive.

---

## Non-goals

- Any nest extract / TNA envelope / WorkSpace whole-tree move this cycle
- Flipping clearance #4 to **approved** or whole-tree clearance to **yes**
- Appendix A parents; OS-IA reverse or re-archive; Medium / Early / archived Multi-experiment peers as sources
- Remote-config (`git remote remove` / `set-url` / force-push)
- Taxonomy final sign-off / must-preserve final lock
- Auto-commit or stash-clean of dirty TNA (~2307)
- Inventing absolute-path consumer lists or destination picks as execute decisions
- Org-repo publish as a required AC (mid/final git only for allowlisted session/program docs dirt if orchestrator continues full close)

---

## What the user is approving

**Plain language:** Approving **yes** means: after this gate, agents may **write documentation only** — create the TNA parent-surgery policy file and update the hazards pointer (#4 = draft written, approval for *moves* still pending). It does **not** move any folders under `C:\Project\WorkSpace`, does **not** archive WorkSpace, and does **not** authorize extracting hermes / orchestrateur / WorkshopOrif yet.

| Answer | Meaning |
| --- | --- |
| **yes** | Proceed STAGE 2 `docs_only` implement (create `program/git-strategy-tna-parent-surgery.md` + hazards #4 pointer + honesty). Nest FS remains forbidden until a **later** dedicated move gate. |
| **no / hold** | Stop; leave #4 as stub; session may close blocked/held without docs implement. |
| **amend …** | Same docs path with named edits to policy scope/wording before implement. |

### Pros

- Concrete Continuity X advance toward clearance criterion **#4** (anti-loop satisfied)
- Reversible; dirty TNA and nests untouched
- Separates “policy written” from “nest move approved” so future extract gates are clearer
- Encodes ignored-nest (not submodule) procedure so wrong surgery is less likely later

### Cons / tradeoffs

- No folder moves this cycle; whole-tree archive still blocked
- Two program files to maintain (dedicated surgery doc + hazards pointer)
- #4 still **not approved** for nest moves — another gate will be required before any extract
- Absolute-path breakage risk under TNA remains **unknown** until a future pre-execute scan

---

## Exact user-gate question

**(copy-paste ready for orchestrator)**

> **Cycle 20 plan gate — STAGE 1 → STAGE 2 docs only**
>
> **What this asks:** May we implement the Cycle 20 **`docs_only`** plan: create `program/git-strategy-tna-parent-surgery.md` (full parent-surgery policy for dirty TNA ignored nests) and update `program/git-strategy-workspace-hazards.md` so clearance criterion **#4** reads **DRAFT written (Cycle 20) / approval pending**, plus light ROADMAP/INDEX honesty as needed?
>
> **What “yes” commits to:** Org-repo documentation writes only. **No** moves of `WorkSpace`, TNA, hermes-agent, orchestrateur, WorkshopOrif, or OS-IA. **No** Multi-experiment Complete. **No** auto-commit of dirty TNA (~2307). Nest extracts stay **forbidden** until a later dedicated move gate (“approved” half of #4). Whole-tree clearance stays **NO**.
>
> **Pros:** Real clearance-#4 advance; reversible; nests stay put.  
> **Cons:** No path progress this cycle; another gate still needed before any nest extract; two strategy files to keep in sync.
>
> Reply **yes** (as-is), **no** / **hold**, or **amend** with specific wording changes.

---

## Rollback / risk notes

| Risk | Mitigation |
| --- | --- |
| Accidental nest FS | Hard-forbid in AC; implementer zero-move attestation; auditor checks paths |
| Treating nests as submodules | Policy must state ignored-nested model; forbid `.gitmodules` surgery |
| Claiming clearance flipped | Explicit “DRAFT / approval pending”; whole-tree still **NO** |
| Empty theater docs | AC requires full procedure sections; escalate only if substance omitted |
| Dirty TNA absolute-path unknowns | Document as open; presence-only scan deferred to pre-execute |
| Outdated hazards “5 live” | Step 3 honesty refresh to **4** without erasing history |
| Rollback of docs | Revert org-repo commits / delete new program file; corpus unchanged |

---

## Blocking questions

**none** for docs content (research blockers: none).  

**Gate pending:** Exact user-gate question above — until **yes**, do not start implementer.

---

## Planner status

| Field | Value |
| --- | --- |
| **ready_to_implement** | **no** (STAGE 1 hold — pending user gate **yes**) |
| **After gate yes** | `docs_only` may proceed same-run STAGE 2 (implement → mid git → audit → self-improver → final git) per FAW docs_only auto-continue |
| **After gate no/hold** | Skip implementer + mid git; still may audit/self-improve/final git for session artifacts per orchestrator; do not claim #4 written |
| **concrete_advance** | parent-surgery docs (Option P) — **not** escalate |
| **Next FAW lock hint** | Multi-experiment / **WorkSpace only** + continue Continuity X clearance / keep-at-root |
