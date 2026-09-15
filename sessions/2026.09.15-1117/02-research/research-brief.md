# Research brief — Cycle 20 (Continuity X clearance #4 / TNA parent-surgery docs)

**Session:** `sessions/2026.09.15-1117/02-research/`  
**Goal:** STAGE 1 evidence for a **docs_only** **parent-surgery** artifact satisfying Continuity X whole-tree clearance criterion **#4** (policy **written**; **approved** deferred to later plan gate). Continuity ≠ execute.  
**Locks:** Q1=**A**; Q2=**A**; Q3=**A** (**NO_AUTO_COMMIT**). WorkSpace / TNA only; nested **4**; OS-IA verify-only.

## One-line outcome

Live nested **4** under TNA confirmed; dirty TNA still **2307**; nests are **gitignored** (not submodules). Criterion **#4** is still a stub — recommend **`docs_only`** held map writing dedicated **`program/git-strategy-tna-parent-surgery.md`** (+ hazards pointer). **`concrete_advance_candidate: parent-surgery docs`** (not escalate).

---

## Return card (orchestrator)

| Field | Value |
| --- | --- |
| **status** | research **complete** — material #4 delta available |
| **nested_inventory** | **4** live: TNA + hermes-agent + orchestrateur + WorkshopOrif (all under `C:\Project\WorkSpace\TestNewWorkspaceAgent`); OS-IA archived verify-only |
| **dirty_WT_note** | TNA **2307** (baseline match); hermes **56** / orchestrateur **60** / WorkshopOrif **119**; disclose **NO_AUTO_COMMIT** |
| **concrete_advance_candidate** | **parent-surgery docs** |
| **recommended_artifact_path** | `program/git-strategy-tna-parent-surgery.md` (+ short pointer / #4 status in `program/git-strategy-workspace-hazards.md`) |
| **one-line for planner** | STAGE 1 `docs_only` map: draft TNA parent-surgery policy (ignored-nest extract, worktree-first, NO_AUTO_COMMIT) as new program md + hazards #4 “DRAFT written / approval pending”; zero nest FS; stop at user gate; never Complete. |

---

## Key evidence

| Field | Live evidence |
| --- | --- |
| Probe method | Shell + recursive `.git`; remotes / worktree / porcelain; TNA ignore check |
| Strategy artifact | **EXISTS** — extend with pointer; **do not** re-litigate Cycle 10–19 classification |
| nested_git_count (WorkSpace) | **4** |
| Nest model | **Ignored nested clones** (TNA `.gitignore`); **no** `.gitmodules` |
| multi_remote | **CLEARED** (no regression on live nests) |
| Linked worktrees | **1** each (expected) |
| Dirty TNA | **2307** — Q3=A disclose only |
| clearance_whole_tree | Still **NO** (writing #4 policy alone ≠ flip all criteria) |
| Push/pull dual preflight | **N/A** (no org-repo sync goal this STAGE) |

Details: [`codebase-findings.md`](./codebase-findings.md) · [`online-findings.md`](./online-findings.md)

---

## What “parent-surgery” must cover

Moving a nested clone **out of** dirty TNA without breaking parent git / worktrees / absolute paths:

1. **Preflight (per nest, nest path only)**  
   - `Test-Path` source + destination free  
   - `git worktree list` — fail-closed if unexpected linked worktrees  
   - Remotes inventory (names + schemes only; path-only Continuity)  
   - Porcelain recount (disclose; do not auto-commit)  
   - Confirm still **ignored** by TNA (not accidentally tracked / submodule)

2. **Atomic nest relocate**  
   - Intact OS move of entire nest tree including `.git`  
   - No history rewrite, no dissolve into parent, no remote URL rewrite  
   - Windows lock recovery per existing hazards safe rules (reunify / robocopy; empty leftover `.git` shells only)

3. **Parent TNA handling under NO_AUTO_COMMIT**  
   - Because nests are **gitignored**, extract typically does **not** require submodule teardown or a parent commit  
   - **Forbidden:** stash/commit/clean TNA “to enable” the move  
   - Allowed: leave TNA dirty; optional empty-dir cleanup; optional `.gitignore` line hygiene (still a tracked change — only under a future gated docs/`fs_mutation` that explicitly allows parent file edits, **not** auto-commit of the 2307 WT)  
   - Document residual parent risk: non-git absolute references (scripts, IDE, docker) may break — require presence-only inventory before execute

4. **Post-move attest (future execute cycle)**  
   - Nest `rev-parse --show-toplevel` at destination; remotes unchanged; worktree list OK  
   - Source path gone; INDEX/inventory honesty; nested count under WorkSpace updated  
   - Multi-experiment still **not** Complete; WorkSpace / remaining units stay locked

5. **Approval definition (clearance #4)**  
   - **Written** = policy artifact exists with procedure + fail-closed rules (this cycle’s docs target)  
   - **Approved** = dedicated plan-gate yes for a named nest `path_batch` (or explicit waiver) — Continuity / Choose / STAGE 1 docs **≠** approved  
   - Whole-tree clearance still needs **all** of #1–#6

---

## Gaps vs Continuity X clearance #4

| Needed for “written” | Present today? |
| --- | --- |
| Named nests in scope + ignore/submodule classification | Partial (fate matrix numbers outdated post–OS-IA; no ignore classification) |
| Step-by-step extract procedure | **No** |
| Worktree / remotes / dirty preflight | Generic safe rules only — not TNA-specific surgery |
| NO_AUTO_COMMIT parent rules | Q3 carried in sessions; **not** encoded as surgery policy |
| Fail-closed conditions (linked WT, path lock, tracked nest surprise) | Partial (generic) |
| Approval / gate wording | Criterion says “approved”; no definition |
| Post-attest + row honesty | Generic |

**Anti-loop:** drafting the above = **material #4 content**. Empty re-attest of “still need parent-surgery” without procedure → **escalate** (`concrete_advance_candidate: none`).

---

## Recommended approach options (max 3)

### Option P (recommended): Dedicated parent-surgery doc + hazards pointer

- **Mutation class:** `docs_only`  
- **Create:** `program/git-strategy-tna-parent-surgery.md` with full policy (scope, nest table, procedure, NO_AUTO_COMMIT, gate/approval, fail-closed, post-attest, explicit non-goals)  
- **Amend:** `program/git-strategy-workspace-hazards.md` — short Continuity X note: #4 status **DRAFT written (Cycle 20) / approval pending**; link to dedicated file; refresh nested **4** / TNA-only envelope in attestation  
- **Optional honesty:** ROADMAP Notes / INDEX / inventory one-liners pointing at surgery draft (still Remaining WorkSpace / not Complete)  
- **Pros:** Visible material delta; keeps hazards readable; clear anti-loop artifact; matches Q1=A  
- **Cons:** Two files to maintain; #4 still not “approved” until later gate  

### Option H: Hazards-only section (no new file)

- Extend hazards with a long “Parent-surgery (TNA)” section only.  
- **Pros:** Single Continuity baseline file.  
- **Cons:** Hazards already long; harder to see Cycle 20 delta; slightly weaker anti-loop signal.  
- **Acceptable fallback** if planner prefers one file.

### Option E: Escalate (rejected as primary)

- Only if research found **no** new substance vs stub.  
- **Rejected:** ignore-vs-submodule classification + concrete procedure outline **is** new gated substance. Continuity Q1=A selected docs path.

---

## concrete_advance_candidate

| Value | Detail |
| --- | --- |
| **parent-surgery docs** | Draft Option P (or H) content in STAGE 1 plan as held `docs_only` map; implement only after later user gate (STAGE 1 this run stops at planner per Continuity) |
| **none → escalate** | **Not** recommended this cycle |

---

## Planner guidance (STAGE 1)

| Requirement | Detail |
| --- | --- |
| Mutation class | **`docs_only`** — nest/envelope FS **out of execute map** |
| `ready_to_implement` | **no** for path mutation; docs implement only after user gate if orchestrator continues STAGE 2 later — **this Continuity run stops after planner** |
| Held map | Create/extend parent-surgery policy artifact (recommended path above); **hold** any future nest `path_batch` |
| Encode | nested **4**; nests **gitignored**; dirty **2307** NO_AUTO_COMMIT; #4 DRAFT written ≠ approved ≠ whole-tree clear |
| Forbidden | Appendix A; OS-IA re-move; Medium/PWAExemple; Complete; silent whole-tree archive; nest move without approved surgery; auto-commit TNA |
| Next FAW hint | WorkSpace only + continue Continuity X clearance / keep-at-root |

---

## Risks and blockers

| Risk / blocker | Class | Note |
| --- | --- | --- |
| Accidental nest FS in STAGE 1 | Process | Plan must hard-forbid |
| Treating nests as submodules | Process | Evidence says ignored — wrong procedure would invent `.gitmodules` surgery |
| Claiming clearance_whole_tree yes after docs | Honesty | #4 written ≠ all criteria; still **NO** |
| Empty theater docs | Anti-loop | Plan AC must require procedure sections listed above |
| Dirty TNA absolute-path unknowns | Unknown | Presence-only scan deferred to pre-execute; do not invent paths |
| Auth / dirty_working_tree (org-repo) | N/A | Not in STAGE 1 goal |

**Blockers for recommended docs advance:** **none**.

---

## Required facts vs unknowns

**Facts:** nested 4 paths; remotes sole origin each; worktrees 1 each; TNA 2307; nests gitignored; OS-IA archived; #4 stub only; INDEX nested 4 matches disk.

**Unknowns (document as open, do not invent):** full list of absolute path consumers under TNA; whether empty parent dirs after extract should be deleted; preferred destination class per nest (archive vs paused vs sibling under `C:\Project`) — **planner may propose defaults held for later gate**, not execute.

---

## Canonical references

- [`program/git-strategy-workspace-hazards.md`](../../../program/git-strategy-workspace-hazards.md) — Continuity X + clearance #4  
- [`catalogue/INDEX.md`](../../../catalogue/INDEX.md) — WorkSpace / OS-IA rows  
- Cycle 19 research: [`sessions/2026.09.15-1014/02-research/research-brief.md`](../../2026.09.15-1014/02-research/research-brief.md)  
- Online: [`online-findings.md`](./online-findings.md) (git-worktree official; ignored-nested practice)
