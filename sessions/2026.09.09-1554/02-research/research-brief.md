# Research brief — Cycle 5 Medium wrappers (safer three remaining)

**Session:** `sessions/2026.09.09-1554/02-research/`  
**Goal:** Live-check in-scope safer three; propose **2–3** (prefer all three if green) with status buckets and move map. Soft-defer pair confirmed at root. **No moves.** **No push/pull.**

## Recommended approach

**Option A (recommended): move all three → `archive`**

All in-scope folders are green: exist at INDEX paths, CreationTime labels match prior proposals, LastWrite outside 90-day window → **archive**, single nested `.git`, single HTTPS `origin`, single main worktree, no target collisions. Opaque `.env` paths present on all three — include in move; never read.

| From | To | Nested `.git` stays under |
| --- | --- | --- |
| `C:\Project\NextTest` | `C:\Project\archive\2025.06.23 - NextTest` | `...\NextTest\.git` |
| `C:\Project\Simpl_Next` | `C:\Project\archive\2025.06.23 - Simpl_Next` | `...\SimplNext\.git` |
| `C:\Project\PWAExempleTristan` | `C:\Project\archive\2025.07.04 - PWAExempleTristan` | `...\PWATristan\.git` |

- Atomic unit = whole wrapper (including nested git + any `.env`). Prefer `Move-Item` / rename over copy+delete.  
- Parent: `archive` exists; `active` not needed; `paused` unused for this subset.  
- Catalogue: update INDEX (and inventory if plan requires) for these three rows after moves.  
- ROADMAP Notes: Medium row stays **in progress**; remaining soft-deferred `NextPWATraining`, `CursorMobileWorkspace`.  
- **Plan gate** required before implementer (Choose-all Continuity ≠ map approval).

## Options considered

1. **Option A — all three → archive (recommended)**  
   - Pros: fills Q1 2–3 with prefer-all-three; no fail-closed hazards; matches Continuity status rule; clears safer pool so next Medium cycle can address soft-deferred only.  
   - Cons: L-band (~600 MB each) — longer moves; all three carry opaque `.env` paths (allowed).

2. **Option B — size 2 (drop heaviest or any one)**  
   - Pros: slightly smaller surface if implementer time/risk budget is tight.  
   - Cons: no hazard-driven reason to shrink; leaves one green folder at root without Continuity justification.

3. **Option C — substitute soft-deferred to “fill”**  
   - **Rejected:** Q2=A forbids moving `NextPWATraining` / `CursorMobileWorkspace` this cycle; do not silently fill quota with deferred names.

## Recommended subset (explicit)

1. `NextTest` → `archive\2025.06.23 - NextTest`  
2. `Simpl_Next` → `archive\2025.06.23 - Simpl_Next`  
3. `PWAExempleTristan` → `archive\2025.07.04 - PWAExempleTristan`

## Proposed move map (hypothesis until plan gate)

- `C:\Project\NextTest` → `C:\Project\archive\2025.06.23 - NextTest` (**archive**)  
- `C:\Project\Simpl_Next` → `C:\Project\archive\2025.06.23 - Simpl_Next` (**archive**)  
- `C:\Project\PWAExempleTristan` → `C:\Project\archive\2025.07.04 - PWAExempleTristan` (**archive**)

Pre: sources exist; targets absent (live-checked). Post verify: sources absent; targets present; nested `.git` intact. Reverse = move dated folder back to original root short name.

## Deferred

| Folder | Role | Reason |
| --- | --- | --- |
| `NextPWATraining` | soft-deferred (Q2=A) | Still at root; SSH remote + `.env`; **do not move** this cycle |
| `CursorMobileWorkspace` | soft-deferred (Q2=A) | Still at root; LastWrite within 90d → would be `paused`; **do not move** |
| `TestRyan`, `ReactRouterTest`, `Simpl` | Cycle 4 archives | Roots absent; archive present — **verify-only**; never re-propose |

**No hard fail-closed skip** among the safer three.

## Required facts

- In-scope three + soft-deferred two all exist at `C:\Project\<Name>`; INDEX paths current.  
- Date labels from CreationTime match INDEX proposals.  
- Cutoff `2026-06-11`: in-scope three → **archive**; only soft-deferred `CursorMobileWorkspace` would be `paused` (not in this batch).  
- `archive` / `paused` parents exist; `active` does not.  
- Cycle 4 destinations present under `archive` — not sources.  
- Org repo / must-preserve draft / hygiene / multi-experiment / special-git — out of scope.  
- Inventory size bands lag live L (~600 MB); treat as duration note only.

## Unknowns / blockers

| Item | Status |
| --- | --- |
| User plan-gate approval of exact map | **Pending** (implementer gate; not a research blocker) |
| Worktree / multi-remote on shortlist | **None** on live-check |
| Push/pull | **N/A** |
| Soft-deferred expansion | Forbidden this cycle |

### Push/auth dual preflight

**Skipped** — refined prompt: no agent remote push/pull expected.

| Field | Value |
| --- | --- |
| Remote URL scheme | n/a (corpus moves only) |
| Tracking branch | n/a |
| Agent git / GCM | n/a |
| `gh` | n/a |
| `blocker_type` | **none** (research scope) |
| Note | Nested remotes observed as HTTPS (in-scope) / SSH (NextPWA soft-deferred only) — informational |

## Risks

- Re-scan nested `.git` / worktrees immediately before each move (fail-closed if new hazards).  
- Do not log `.env` contents.  
- Do not touch soft-deferred or Cycle 4 archive peers.  
- Large trees: prefer single atomic rename; avoid partial copy.  
- After batch, ROADMAP must keep Medium **in progress** with remaining soft-deferred names.

## Canonical references

- Refined prompt: `sessions/2026.09.09-1554/01-prompt-betterment/refined-prompt.md`  
- Live matrix: `sessions/2026.09.09-1554/02-research/codebase-findings.md`  
- Online: `sessions/2026.09.09-1554/02-research/online-findings.md`  
- Prior Medium: `sessions/2026.09.09-1535/02-research/`  
- `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/taxonomy.md`  
- `program/ROADMAP.md` — Medium wrappers in progress  
- https://git-scm.com/docs/git-worktree
