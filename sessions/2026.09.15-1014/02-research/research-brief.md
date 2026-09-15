# Research brief — Cycle 19 Continuity X (WorkSpace XL / whole-tree git-strategy)

**Session:** `sessions/2026.09.15-1014/02-research/`  
**Goal:** STAGE 1 evidence for dedicated **XL / whole-tree git-strategy** — extend [`program/git-strategy-workspace-hazards.md`](../../../program/git-strategy-workspace-hazards.md); document **keep-vs-split / fate** options; optionally attach a **gated `fs_mutation` map held** for plan gate. Continuity **X ≠ execute**.  
**Locks:** Continuity **X**; Q1=**A**; Q2=**A**; Q3=**A**.  
**Not this phase:** implementer, path/remote execute, Complete / Primary next, Continuity A theater, history rewrite.

## One-line outcome

Live hazards **unchanged** vs Cycle 18 / strategy (nested **5**, multi-remote **CLEARED**, whole-tree clearance **NO**, ~**1086 MB** XL). Continuity X advance = **strategy decisions** (keep / split / eventual archive + clearance criteria), not a new narrow hazard fix. Recommend **hybrid docs**: extend artifact with fate matrix; **optional held map = OS-IA-only** (or none if planner wants fate-first).

---

## Key evidence

| Field | Live evidence |
| --- | --- |
| Probe method | Shell succeeded: `Test-Path`; recursive `.git` / `.env*`; MSYS git remotes/worktrees/porcelain; cheap size |
| Strategy artifact | **EXISTS** — **extend** (do not rewrite from scratch) |
| INDEX WorkSpace path | `C:\Project\WorkSpace` **exists** (root) — verify-only |
| nested_git_count | **5** (atomic units listed in codebase-findings) |
| multi_remote_status | **CLEARED** — live hermes sole `origin`; **no `cada`** |
| appendix_a_parents | Archive hygiene leaves **present**; live parents **absent** |
| Linked worktrees | **1** each (main only) |
| Opaque `.env*` live | **7** (presence only) |
| Size (cheap) | ~**1086 MB** excl `.git` (~**716 MB** excl `node_modules`) — still **XL** |
| Dirty WT | TNA **2307**, OS-IA **921**, hermes **56**, orchestrateur **60**, WorkshopOrif **119** — **disclose / NO_AUTO_COMMIT** |
| clearance_whole_tree | **NO** |
| Push/pull dual preflight | **N/A** (no org-repo sync this cycle) |

Details: [`codebase-findings.md`](./codebase-findings.md) · online: [`online-findings.md`](./online-findings.md)

---

## Already decided vs still open (Continuity X)

### Artifact already decides

- WorkSpace-only lock; peers verify-only  
- Appendix A executed; live multi-remote cleared  
- Nested **5**; keep primaries interim; ordinary whole-tree archive OOS / clearance **NO**  
- Safe relocation rules (atomic nests, path-only remotes, opaque env, worktree probe, row honesty)

### Continuity X must still decide (material advance = documenting these)

1. **Fate options** for wrapper + each atomic unit: keep-at-root / split-by-nested-root / eventual archive under dedicated gate / hybrid  
2. **Clearance criteria** that would flip whole-tree clearance **NO → yes** (beyond multi-remote)  
3. Whether STAGE 1 attaches an **optional held gated map** (proposal-only) vs pure strategy docs  
4. Parent-surgery policy if splitting nests **inside** dirty TNA

---

## Nested roots as atomic units (planner must name these)

| # | Unit | Envelope note |
| --- | --- | --- |
| 1 | `OS-IA` | Sibling of TNA — cleanest first-split candidate |
| 2 | `TestNewWorkspaceAgent` (TNA) | Parent wrapper repo; dirty **2307** |
| 3 | `hermes-agent` | Nested under TNA |
| 4 | `orchestrateur` | Nested under TNA |
| 5 | `WorkshopOrif` | Nested under TNA |

Plus non-git wrapper folder `C:\Project\WorkSpace` (holds #1+#2 only).

---

## Recommended approach options (max 3)

### Option H (recommended): Hybrid strategy extension + optional OS-IA held map

- **Mutation class:** `docs_only` body (extend hazard artifact with keep-vs-split / fate / clearance criteria) **+** optional `fs_mutation` map **held** for plan gate (not execute).  
- **`ready_to_implement`:** **no** for path/remote mutation until plan-gate yes (STAGE 1 stop after planner).  
- **Strategy direction:** Default **keep-at-root** for TNA envelope (#2–#5) until user picks split/archive; document **eventual archive** only as gated future fate after clearance criteria; attach **optional held map: OS-IA (#1) intact → dated `archive` or `paused`** as first subset.  
- **Pros:** Matches Continuity X + Q1=A; material decision advance (not Continuity A theater); first map is evidence-backed and does not tear TNA; preserves atomic git roots / no history rewrite.  
- **Cons:** Heavier plan review; OS-IA move (if later approved) still leaves WorkSpace / Multi-experiment incomplete; dirty WT remains disclosed-only.

### Option D: Docs-only fate matrix (no `fs_mutation` map yet)

- **Mutation class:** `docs_only` only.  
- **Pros:** Smaller gate surface; pure strategy.  
- **Cons:** Another cycle before any concrete gated map; slightly weaker vs Q1=A “may attach map” default — still acceptable if planner chooses fate-first.

### Option W: Whole-tree / full-split map held now (rejected as primary)

- Propose moving all of WorkSpace or extracting #3–#5 immediately in the held map.  
- **Rejected as primary:** clearance_whole_tree still **NO**; #3–#5 extraction = TNA parent surgery under NO_AUTO_COMMIT + 2307 porcelain — needs dedicated parent plan, not Continuity X first map. Whole-tree archive still forbidden without clearance + explicit gate.

---

## optional_gated_map

| Value | Detail |
| --- | --- |
| **describe (recommended)** | **OS-IA only** — intact atomic relocate from `C:\Project\WorkSpace\OS-IA` → dated destination under `C:\Project\archive\…` or `C:\Project\paused\…` (planner picks class + naming); remotes path-only unchanged; re-probe worktree immediately before STAGE 2; opaque `.env*` N/A on OS-IA for listed 7 (none on OS-IA in live list); **held for plan gate — Continuity X ≠ execute** |
| Alternative | **none** — if planner prefers Option D (fate docs first, map in a later cycle) |

**Not optional_gated_map:** whole WorkSpace archive; re-Appendix A; live hermes remote-config; archive-hygiene `cada`; TNA-internal nest extraction without parent plan.

---

## Clearance status

| Scope | Status |
| --- | --- |
| Live hermes multi-remote | **CLEARED** |
| Appendix A parents | **Isolated** — verify-only |
| Whole-tree WorkSpace archive | **NO** — classified ≠ cleared |
| Multi-experiment row | Stays **in progress / Remaining: WorkSpace only** — even after optional OS-IA map execute (future) |

---

## Planner guidance (STAGE 1)

| Requirement | Detail |
| --- | --- |
| Mutation class | Honest: **`docs_only` strategy extension** ± **`fs_mutation` map held** (Q1=A) |
| Continuity X | ≠ execute; stop after planner for **mandatory plan gate** |
| Extend | `program/git-strategy-workspace-hazards.md` — add Continuity X section: fate matrix, clearance criteria, optional OS-IA map pointer; keep prior attestations |
| Encode | nested **5**; multi_remote **CLEARED**; clearance_whole_tree **NO**; dirty disclose NO_AUTO_COMMIT; never Complete / Primary next |
| Forbidden | Continuity A theater; silent whole-tree archive; force-move; history rewrite; peer reopen; re-Appendix A; re-clear multi-remote without regression |
| Taxonomy / must-preserve | Carry Q2=A |

### One-line for planner

**Extend hazards with keep/split/eventual-archive fate + clearance criteria; STAGE 1 `docs_only` + optional held OS-IA-only `fs_mutation` map; `ready_to_implement: no` until plan-gate yes; row stays Remaining WorkSpace / not Complete.**

---

## Required facts

- Continuity **X**, Q1=**A**, Q2=**A**, Q3=**A** locked.  
- Hazard artifact authoritative baseline; Cycles 14–15 consumed narrow advances; Cycle 18 escalated to X.  
- Nested roots are already separate repos — relocate intact; do not filter-repo.  
- Classified ≠ cleared for whole-tree.  
- Continuity / Choose ≠ plan-gate execute.

## Unknowns / blockers

| Item | Status |
| --- | --- |
| User fate preference (keep / split / eventual archive) | **Open** — plan gate / Continuity X deliverable |
| Destination class for any future OS-IA move | **Open** — archive vs paused (held map must propose) |
| When whole-tree clearance flips | **Open** — planner must propose criteria (not invent silent clear) |
| Multi-remote regression | **None** |
| Org-repo auth / dirty sync | **N/A** |
| Nested dirty WT | Disclose only — not an execute blocker under Q3=A, but blocks silent hygiene |

### Push / pull dual preflight

**N/A** — refined prompt excludes publish/pull.

---

## Risks

| Risk | Mitigation |
| --- | --- |
| Treating Continuity X as execute authority | STAGE 1 stop; `ready_to_implement: no` until gate |
| Continuity A docs re-attest theater | Fate matrix + optional map = material advance; forbid empty re-attest |
| Silent whole-tree archive | clearance **NO**; map must not invent it |
| First map tears dirty TNA | Prefer OS-IA-only; defer #3–#5 until parent plan |
| Marking Multi-experiment Complete after OS-IA | Fail-closed — WorkSpace / TNA remain |
| History rewrite temptation | Out of scope; online contrast documented |

---

## Canonical references

- [`program/git-strategy-workspace-hazards.md`](../../../program/git-strategy-workspace-hazards.md)  
- [`program/ROADMAP.md`](../../../program/ROADMAP.md)  
- [`catalogue/INDEX.md`](../../../catalogue/INDEX.md)  
- [`catalogue/inventory.md`](../../../catalogue/inventory.md)  
- Cycle 18: [`sessions/2026.09.15/02-research/`](../../2026.09.15/02-research/)  
- Continuity locks: [`../01-prompt-betterment/notes.md`](../01-prompt-betterment/notes.md) · [`refined-prompt.md`](../01-prompt-betterment/refined-prompt.md)  
- Online: [`online-findings.md`](./online-findings.md)
