# Codebase findings — Cycle 19 Continuity X (WorkSpace XL / whole-tree git-strategy)

**Session:** `sessions/2026.09.15-1014/02-research/`  
**Probe date:** 2026-09-15  
**Method:** Shell `Test-Path`; recursive live `.git` / `.env*` under `C:\Project\WorkSpace`; MSYS `git` (`C:\msys64\usr\bin\git.exe`) for `remote -v`, `worktree list --porcelain`, `status --porcelain` (read-only). GfW `Program Files\Git\cmd\git.exe` **absent** on agent — fine for research; any future STAGE 2 mutation still prefer GfW + GCM.  
**Secrets:** path presence only — `.env*` contents unread.  
**Baseline cited:** [`program/git-strategy-workspace-hazards.md`](../../../program/git-strategy-workspace-hazards.md) (FULL read); Cycle 18 [`sessions/2026.09.15/02-research/`](../../2026.09.15/02-research/).

---

## Path truth vs INDEX / strategy

| Claim | Live | Verdict |
| --- | --- | --- |
| INDEX current path `C:\Project\WorkSpace` | **Exists** | **verify-only** — still at program root; **never re-move** as “archive fix” |
| Live `…\TestNewWorkspaceAgent\_backups` | **Absent** | Appendix A still holds |
| Live `…\TestNewWorkspaceAgent\_quarantine` | **Absent** | Appendix A still holds |
| Archive `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_backups` | **Exists** | verify-only — **do not re-propose** isolation |
| Archive `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_quarantine` | **Exists** | verify-only — **do not re-propose** isolation |

**Peers (verify-only — never re-propose as move sources):** archived Multi-experiment (`PWAExemple`, `GitTest`, `WorkStationPWA`) and Medium / Early rows.

**Top-level children of WorkSpace:** `OS-IA`, `TestNewWorkspaceAgent` only.

---

## Nested roots inventory (5) — atomic strategy units

**Count: 5** — matches hazard artifact / Cycle 14–18 baseline. **No material delta.**

| # | Path (git root) | Role in XL tree | Envelope |
| --- | --- | --- | --- |
| 1 | `C:\Project\WorkSpace\OS-IA` | Independent sibling project | **Outside** TNA — only top-level child that is not under TNA |
| 2 | `C:\Project\WorkSpace\TestNewWorkspaceAgent` | Parent / wrapper repo (TNA) | Contains nests #3–#5 as on-disk children |
| 3 | `…\TestNewWorkspaceAgent\hermes-agent` | Nested clone (upstream Hermes) | **Inside** TNA working tree |
| 4 | `…\Projects\Project Atelier IA\Projet Adrien\orchestrateur` | Nested clone | **Inside** TNA |
| 5 | `…\Projects\Project Atelier IA\Workshop\WorkshopOrif` | Nested clone | **Inside** TNA |

**Atomic-unit rule (Continuity X):** any future gated relocate must move each listed tree **intact** (directory + `.git`); never strip history / filter-repo / force-push; never cherry-pick inner files out of a nest without a dedicated plan that treats that nest as the unit.

**Split implication:** relocating #3–#5 changes the **parent TNA** filesystem (and dirty WT). Relocating #1 does **not** tear TNA. Relocating whole WorkSpace moves the wrapper folder that is **not** itself a single git root (WorkSpace has no top-level `.git`).

---

## Remotes / worktrees / dirty (disclose)

| # | Root | Remotes | Worktrees | Porcelain lines |
| --- | --- | --- | --- |
| 1 | OS-IA | sole `origin` HTTPS `KenCacciabueOrif/Projet-OS-IA` | 1 (main) | **921** |
| 2 | TNA | sole `origin` HTTPS `KenCacciabueOrif/TestNewWorkspaceAgent` | 1 | **2307** |
| 3 | hermes-agent (live) | sole `origin` HTTPS `NousResearch/hermes-agent` — **`cada` absent** | 1 (main) | **56** |
| 4 | orchestrateur | sole `origin` HTTPS `AdWav/orchestrateur` | 1 | **60** |
| 5 | WorkshopOrif | sole `origin` HTTPS `C0D3X-25/WorkshopOrif` | 1 | **119** |

**Live multi-remote:** **CLEARED** — no `cada` regression (Cycle 15 clearance holds; Cycle 16/18/19 confirm).  
**Linked worktrees:** none unexpected (1 each on nested clone paths).  
**Dirty WT:** heavy porcelain especially TNA / OS-IA — Continuity **Q3=A** → **disclose + NO_AUTO_COMMIT**. Nested+parent dirty: do not auto-commit either tree.

Archive hygiene hermes under Appendix A parents may still show `origin`+`cada` — strategy **Out of map / verify-only**; not a Continuity X live advance.

---

## Opaque `.env*` (presence only)

**7 live paths** (unchanged vs Cycle 16/18):

1. `…\hermes-agent\.env.example`
2. `…\hermes-agent\.envrc`
3. `…\orchestrateur\.env`
4. `…\orchestrateur\.env.example`
5. `…\orchestrateur\ui\.env.example`
6. `…\WorkshopOrif\.env`
7. `…\WorkshopOrif\.env.example`

---

## Size (cheap re-verify)

- ~**1086 MB** excl `.git`
- ~**716 MB** also excl `node_modules`  
Still **XL**. Shrink from historical ~5786 MB (pre–Appendix A) ≠ whole-tree clearance.

**clearance_whole_tree:** **NO** — classified ≠ cleared.

---

## What the hazard artifact already decides vs Continuity X must still decide

### Already decided (do not re-litigate as if new)

| Topic | Artifact status |
| --- | --- |
| Scope lock | WorkSpace only; peers verify-only |
| Appendix A `_backups` / `_quarantine` | **Executed** Cycle 14 — parents under `archive\hygiene\…`; **no re-proposal** |
| Live hermes multi-remote | **CLEARED** Cycle 15 (confirm 16+) — **no re-clear** without regression |
| Nested live count | **5** atomic roots |
| Live primaries fate (interim) | **Keep in place** pending dedicated XL strategy |
| Ordinary whole-tree Multi-experiment archive | **OUT OF SCOPE** / clearance **NO** until dedicated gated strategy |
| Safe rules | Atomic nested git; remotes path-only; opaque `.env*`; worktree check on clone paths; Windows lock recovery; Continuity ≠ plan-gate; row stays Remaining WorkSpace / not Complete |
| Taxonomy / must-preserve | Proposed-ratified / draft — Continuity Q2=A waive re-litigation |

### Continuity X must still decide (extend artifact — this cycle’s job)

| Decision | Why open |
| --- | --- |
| **Keep vs split vs eventual archive** for the XL wrapper and each of #1–#5 | Artifact says keep interim + whole-tree OOS; does **not** yet document a full fate matrix / clearance criteria for Continuity X |
| **What “cleared” means** for whole-tree / XL (program gates beyond multi-remote) | Multi-remote no longer the named blocker; XL size, dirty WT policy, nest envelope, catalogue honesty still block ordinary archive |
| **Whether any first gated subset** is justified now | Narrow advances already consumed; only new maps are XL-fate-class (not Continuity A theater) |
| **Parent-surgery rules** if splitting #3–#5 out of TNA | Not specified beyond “atomic nest”; TNA dirty **2307** makes this high-risk |
| **Destination classes** (dated `archive` vs `paused` vs sibling under `C:\Project`) | Not chosen for Continuity X |

**Forbidden this cycle:** Continuity A docs_only re-attest with no material advance; silent whole-tree archive; force-move without plan gate; mark Multi-experiment Complete; reopen peers.

---

## First gated subset map — justifiable?

| Candidate map | Justifiable as optional held map? | Rationale |
| --- | --- | --- |
| **OS-IA (#1) → dated archive or paused** (intact) | **Yes — weakest / cleanest first subset** | Sibling of TNA; sole independent top-level atomic root; sole `origin`; 1 worktree; does not tear TNA nests; shrinks WorkSpace surface without claiming row Complete |
| Extract hermes / orchestrateur / WorkshopOrif (#3–#5) to sibling destinations | **Not as “first” map without dedicated parent plan** | Nested **inside** dirty TNA (2307 porcelain); move = TNA WT surgery + NO_AUTO_COMMIT conflict; needs explicit parent handling |
| Move whole TNA (#2) including nests | **XL-class — not “narrow first subset”** | Moves #2–#5 together; still leaves OS-IA; still not Multi-experiment Complete unless OS-IA also handled |
| Whole `C:\Project\WorkSpace` → ordinary archive | **No — clearance still NO** | Forbidden as silent / ordinary archive; only under dedicated gate **after** clearance criteria met |
| Archive-hygiene `cada` remove | **No** | Out of map / not live clearance |
| Re-Appendix A | **No** | Already executed |

**Verdict for Q1=A:** Prefer **strategy-doc extension** as the primary Continuity X deliverable; **may** attach **optional held map: OS-IA-only atomic relocate** for plan gate (≠ execute). Pure strategy-docs-only (no map) remains valid if planner wants fate-choice before any path proposal — but Q1=A default allows the held OS-IA map.

---

## Material delta vs strategy / Cycle 18

**None on hazards.** Nested **5**; multi-remote **CLEARED**; Appendix A parents archived; size/env band unchanged; whole-tree clearance **NO**. Continuity X advance is **decision/docs** (keep-vs-split/fate + optional held map), not a new hazard discovery.

---

## Catalogue / program pointers

| Path | Why |
| --- | --- |
| `program/git-strategy-workspace-hazards.md` | Durable baseline to **extend** (not rewrite) with Continuity X fate matrix |
| `program/ROADMAP.md` | Multi-experiment Remaining WorkSpace only; Next FAW = Continuity X |
| `catalogue/INDEX.md` | WorkSpace still `C:\Project\WorkSpace`; nested 5; multi-remote Cleared |
| `catalogue/inventory.md` | Cleared multi-remote honesty; XL / clearance NO |
| `sessions/2026.09.15/02-research/` | Cycle 18 escalate → Continuity X handoff |
| `sessions/2026.09.15-1014/01-prompt-betterment/` | Continuity X / Q1=A / Q2=A / Q3=A locks |
