# Research brief — Cycle 4 Medium wrappers (first subset)

**Session:** `sessions/2026.09.09-1535/02-research/`  
**Goal:** Propose **2–3** lower-hazard Medium wrappers for the first `fs_mutation` batch; defer the rest with reasons. **No moves** this phase. **No push/pull.**

## Recommended approach

**Option A (recommended): first subset = `TestRyan` + `ReactRouterTest` + `Simpl` → all `archive`**

Move the three simplest thin wrappers (S-band; single nested `.git`; single HTTPS `origin`; no extra worktrees; no target collisions). Prefer the two with **no** `.env`, then one S-band with opaque `.env` path (`Simpl`) rather than starting with `NextPWATraining`.

| From | To | Nested `.git` stays under |
| --- | --- | --- |
| `C:\Project\TestRyan` | `C:\Project\archive\2025.06.25 - TestRyan` | `...\python-mini-jeux\.git` |
| `C:\Project\ReactRouterTest` | `C:\Project\archive\2025.08.12 - ReactRouterTest` | `...\ReactRouterTest\.git` |
| `C:\Project\Simpl` | `C:\Project\archive\2025.06.05 - Simpl` | `...\Project-Simpl\.git` |

- Atomic unit = whole wrapper tree (including nested git). Prefer `Move-Item` / rename over copy+delete.  
- Parents: `archive` exists; `active` not needed.  
- Secrets: if any `.env` under `Simpl`, move opaque — path-only logging.  
- Catalogue: update INDEX (and inventory if plan requires) **only** for these three rows after moves.  
- **Plan gate** required before implementer.

## Options considered

1. **Option A — TestRyan + ReactRouterTest + Simpl (recommended)**  
   - Pros: lowest hazard; all archive; S-band; no worktree/multi-remote fails; avoids SSH / NextPWATraining / paused CursorMobile; aligns with “prefer simpler.”  
   - Cons: leaves five Medium at root for later cycles; `Simpl` carries an opaque `.env` path (acceptable under Q6).

2. **Option B — TestRyan + ReactRouterTest only (size 2)**  
   - Pros: zero `.env` in batch; smallest surface.  
   - Cons: under-uses Q1 allowance of up to 3; slower Medium progress.

3. **Option C — TestRyan + ReactRouterTest + NextTest**  
   - Pros: still archive/single-nested HTTPS; skips must-preserve optionals.  
   - Cons: `NextTest` is M-band and has `.env`; no clear advantage over `Simpl` (S).

## Recommended subset (explicit)

1. `TestRyan` → `archive\2025.06.25 - TestRyan`  
2. `ReactRouterTest` → `archive\2025.08.12 - ReactRouterTest`  
3. `Simpl` → `archive\2025.06.05 - Simpl`

## Proposed move map (hypothesis until plan gate)

- `C:\Project\TestRyan` → `C:\Project\archive\2025.06.25 - TestRyan`  
- `C:\Project\ReactRouterTest` → `C:\Project\archive\2025.08.12 - ReactRouterTest`  
- `C:\Project\Simpl` → `C:\Project\archive\2025.06.05 - Simpl`

Pre: sources exist; targets absent (live-checked). Post: reverse = move dated folder back to original root name.

## Deferred (remain at root; later Medium cycle)

| Folder | Reason |
| --- | --- |
| `NextTest` | Structurally fine; M + `.env`; not needed when Safer S peers fill the 3-slot |
| `Simpl_Next` | M + `.env`; same pattern as Simpl — batch after first subset proves Medium moves |
| `PWAExempleTristan` | M + `.env`; defer for second Medium batch |
| `CursorMobileWorkspace` | LastWrite within 90d → would need **`paused\`** parent; larger M (~11); **optional** must-preserve draft — soft defer |
| `NextPWATraining` | Prefer not first: INDEX-flagged `.env`, **SSH** remote, optional must-preserve draft — opaque move OK later, not this shortlist |

**No hard fail-closed defer** among the eight for worktree/multi-remote (all single main WT, single remote). Soft process deferrals only as above.

## Required facts

- All eight candidates exist at `C:\Project\<Name>`; INDEX root paths are **current** for Medium.  
- CreationTime labels match INDEX/inventory hypotheses.  
- 90-day cutoff `2026-06-11`: only `CursorMobileWorkspace` → `paused`; recommended three → `archive`.  
- `archive` / `paused` parents exist; `active` does not.  
- Early/simple destinations present; roots absent — **verify-only**, not Medium sources.  
- Org repo / must-preserve draft / hygiene / multi-experiment / special-git — out of scope.

## Unknowns / blockers

| Item | Status |
| --- | --- |
| User plan-gate approval of exact map | **Pending** (blocker for implementer, not for research completeness) |
| Worktree/multi-remote among shortlist | **None found** on live-check |
| Push/pull | **N/A** — not in goal |
| Soft deferrals | Documented; do not expand shortlist past plan-gate visibility |

### Push/auth dual preflight

**Skipped** — refined prompt: no agent remote push/pull expected.

| Field | Value |
| --- | --- |
| Remote URL scheme | n/a |
| Tracking branch | n/a |
| Agent git path | n/a (not required) |
| Prefer GfW path? | n/a |
| GCM / non-interactive evidence | n/a |
| `gh` present? | n/a |
| `blocker_type` | **none** (for this research scope) |
| Blocker / remediation | Plan gate before moves |

## Risks

- Implementer must **re-scan** nested `.git` / worktrees immediately before each move (fail-closed if new hazards appear).  
- Do not log `.env` contents if touching `Simpl`.  
- Do not reopen Early/simple or expand past approved map.  
- INDEX drift for non-batch Medium rows may remain until later cycles (honesty only).

## Canonical references

- Refined prompt: `sessions/2026.09.09-1535/01-prompt-betterment/refined-prompt.md`  
- Live matrix: `sessions/2026.09.09-1535/02-research/codebase-findings.md`  
- Online: `sessions/2026.09.09-1535/02-research/online-findings.md`  
- `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/taxonomy.md`, `catalogue/must-preserve.md`  
- `program/ROADMAP.md` — Medium wrappers Primary next  
- git-worktree docs: https://git-scm.com/docs/git-worktree
