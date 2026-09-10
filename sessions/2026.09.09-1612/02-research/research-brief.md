# Research brief — Cycle 6 Medium wrappers (soft-deferred finalization)

**Session:** `sessions/2026.09.09-1612/02-research/`  
**Goal:** Live-check both remaining soft-deferred Medium wrappers; propose move map for green items; skip only on hard fail-closed (Q5=A). **No moves.** **No push/pull.** Do **not** re-propose Cycle 4/5 archives.

## Recommended approach

**Option A (recommended): finalize both — NextPWA → `archive`, CursorMobile → `paused`**

Both folders exist at INDEX root paths, CreationTime labels match INDEX proposals, statuses follow the locked 90-day rule, each is thin-wrapper-1git with a single main worktree and a single `origin`, no target collisions, parents `archive`/`paused` exist. Hard fail-closed screen (extra worktrees / multi-remote / unclear strategy / collisions) is **clean** for both.

| From | To | Nested `.git` stays under |
| --- | --- | --- |
| `C:\Project\NextPWATraining` | `C:\Project\archive\2025.06.23 - NextPWATraining` | `...\blogr-nextjs-prisma\.git` |
| `C:\Project\CursorMobileWorkspace` | `C:\Project\paused\2026.06.17 - CursorMobileWorkspace` | `...\CursorMobileWorkspace\.git` |

- Atomic unit = whole wrapper (including nested git + any `.env`). Prefer `Move-Item` / rename over copy+delete.  
- **Secrets (Q4=A):** NextPWA `.env` path present — include unread; never open/log contents. CursorMobile: no `.env` found depth≤5.  
- **SSH (NextPWA):** keep URL as-is (path-only; no rewrite). Residual informational risk only; Cycle 4 treated SSH alone as soft-prefer defer, not hard abort.  
- Catalogue: update INDEX (+ inventory if plan requires) for both rows after moves.  
- ROADMAP: after **both** succeed → Medium **Complete**; Primary next → **Multi-experiment**.  
- **Plan gate** required before implementer (Choose-all Continuity ≠ map approval).

## Options considered

1. **Option A — both remaining (recommended)**  
   - Pros: matches Q1=A finalize-both; clears Medium row; statuses match 90-day evidence; no hard fail-closed.  
   - Cons: NextPWA is L-band (~380 MB) + SSH remote + opaque `.env` (allowed); dual status parents (`archive` + `paused`).

2. **Option B — CursorMobile only (strict “any SSH = skip”)**  
   - Pros: if plan gate adopts refined-prompt hazard list literally for SSH presence, Q5=A allows deferring NextPWA only.  
   - Cons: re-soft-defers NextPWA without a new hard hazard vs Cycle 4/5 evidence; Medium stays in progress; conflicts with “do not re-soft-defer by default.” **Not recommended** unless user forces that stricter reading at plan gate.

3. **Option C — abort both / all-or-nothing**  
   - **Rejected under Q5=A:** default allows at most one defer; both are green under Continuity hard screen.

## Recommended subset (explicit)

1. `NextPWATraining` → `archive\2025.06.23 - NextPWATraining`  
2. `CursorMobileWorkspace` → `paused\2026.06.17 - CursorMobileWorkspace`

## Proposed move map (hypothesis until plan gate)

- `C:\Project\NextPWATraining` → `C:\Project\archive\2025.06.23 - NextPWATraining` (**archive**)  
- `C:\Project\CursorMobileWorkspace` → `C:\Project\paused\2026.06.17 - CursorMobileWorkspace` (**paused**)

Pre: sources exist; targets absent (live-checked). Post verify: sources absent; targets present; nested `.git` intact; `.env` path still present under NextPWA destination (unread). Reverse = move dated folder back to original root short name.

## Skipped / deferred

| Folder | Role | Reason |
| --- | --- | --- |
| *(none fail-closed)* | — | Both green under hard screen |
| `TestRyan`, `ReactRouterTest`, `Simpl` | Cycle 4 archives | Roots absent; archive present — **verify-only**; never re-propose |
| `NextTest`, `Simpl_Next`, `PWAExempleTristan` | Cycle 5 archives | Roots absent; archive present — **verify-only**; never re-propose |

**No hard fail-closed skip** among the two soft-deferred names.

## Required facts

- Both candidates exist at `C:\Project\<Name>`; INDEX paths current.  
- Date labels from CreationTime: `2025.06.23 - NextPWATraining`, `2026.06.17 - CursorMobileWorkspace`.  
- Cutoff `2026-06-11`: NextPWA → **archive**; CursorMobile → **paused** (matches prior expectation).  
- `archive` / `paused` parents exist; `active` does not (unused).  
- Cycle 4/5 destinations present under `archive` — not sources.  
- Org repo / must-preserve draft / hygiene / multi-experiment / special-git — out of scope.  
- Inventory size for NextPWA lags live L (~380 MB); duration note only.

## Unknowns / blockers

| Item | Status |
| --- | --- |
| User plan-gate approval of exact map | **Pending** (implementer gate; not a research blocker) |
| Worktree / multi-remote hard hazards | **None** on live-check |
| Push/pull | **N/A** (no agent remote ops expected) |
| Strict SSH=fail-closed policy | Optional plan-gate override only; research does **not** skip NextPWA |

### Push/auth dual preflight

**N/A** — refined prompt: no agent remote push/pull for this cycle. Path-only FS moves only.

## Risks

- NextPWA L-band move duration / interrupted `Move-Item` — verify nested `.git` + `.env` path post-move; reverse-move documented.  
- Opaque `.env` — any read/log is Critical process failure.  
- Implementer must **re-scan** nested `.git` / worktrees immediately before each move (fail-closed if new hazards).  
- If plan gate forces Option B, ROADMAP stays Medium in progress with `NextPWATraining` remaining (Q5=A).

## Canonical references

- `sessions/2026.09.09-1612/01-prompt-betterment/refined-prompt.md`  
- `sessions/2026.09.09-1612/02-research/codebase-findings.md`  
- `sessions/2026.09.09-1612/02-research/online-findings.md`  
- `catalogue/INDEX.md`, `catalogue/taxonomy.md`, `catalogue/inventory.md`  
- `program/ROADMAP.md`  
- Prior: `sessions/2026.09.09-1535/02-research/`, `sessions/2026.09.09-1554/02-research/`  
- https://git-scm.com/docs/git-worktree.html
