# Research brief — Cycle 7 Multi-experiment (first subset)

**Session:** `sessions/2026.09.10/02-research/`  
**Goal:** Live-check Multi-experiment candidates; recommend **1–2** lower-risk peers for the first `fs_mutation` batch; document fail-closed / remaining names. **No moves. No push/pull. No plan file.**

## Recommended approach

**Option A (recommended): first subset = `GitTest` + `WorkStationPWA` → `archive`**

Both exist at honest INDEX root paths; CreationTime labels match INDEX proposals; 90-day heuristic → **archive**; each has **exactly two** nested `.git` dirs (INDEX-aligned), **one main worktree** each, **single remote** each; no `.env`; S-band; not on must-preserve draft; destination parents exist; proposed dated targets **absent**. SSH on one WorkStation nested remote is **path-only** (no rewrite) — Continuity soft informational, not hard abort.

| From | To | Nested `.git` stays under (atomic) |
| --- | --- | --- |
| `C:\Project\GitTest` | `C:\Project\archive\2025.08.08 - GitTest` | `...\NextTest\.git`, `...\test\.git` |
| `C:\Project\WorkStationPWA` | `C:\Project\archive\2025.07.01 - WorkStationPWA` | `...\WorkStationPWA\.git`, `...\WorkStationRouterPWA\workstation-app\.git` |

- Atomic unit = whole top-level wrapper (all nested git + non-git children). Prefer `Move-Item` / rename over copy+delete.  
- Secrets: none found under these two — still never open any `.env*` if a pre-move re-scan finds one.  
- Remotes: note schemes (HTTPS / SSH); **never rewrite**.  
- Catalogue: update INDEX (+ inventory nested counts if plan requires) after moves.  
- ROADMAP Notes: remaining Multi-experiment names = **`PWAExemple`, `WorkSpace`** (row stays **in progress** — not Complete).  
- **Plan gate** required before implementer (Choose-all Continuity ≠ map approval).

## Options considered

1. **Option A — GitTest + WorkStationPWA (recommended)**  
   - Pros: lowest hard-hazard surface; S-band; INDEX nested counts match; no `.env`; clean worktrees/remotes.  
   - Cons: leaves two names on the row; WorkStation has one SSH remote (path-only OK).

2. **Option B — GitTest + PWAExemple**  
   - Pros: still 1–2 subset; PWAExemple is movable (no linked worktrees / no multi-remote).  
   - Cons: 3 nested roots (INDEX said 2), multiple opaque `.env`, one SSH, M-band — higher verify surface than WorkStationPWA. **Not preferred** while WorkStationPWA is greener.

3. **Option C — GitTest only (most conservative)**  
   - Pros: minimal blast radius.  
   - Cons: under-uses Q1=A “1–2” capacity; WorkStationPWA is equally green under the hard screen. Prefer A unless plan gate shrinks.

**Rejected for this first subset:** moving all four; including `WorkSpace` (fail-closed).

## Recommended subset (explicit)

1. `GitTest` → `archive\2025.08.08 - GitTest`  
2. `WorkStationPWA` → `archive\2025.07.01 - WorkStationPWA`

## Proposed move map (hypothesis until plan gate)

- `C:\Project\GitTest` → `C:\Project\archive\2025.08.08 - GitTest` (**archive**)  
- `C:\Project\WorkStationPWA` → `C:\Project\archive\2025.07.01 - WorkStationPWA` (**archive**)

Pre: sources exist; targets absent (live-checked). Post verify: sources absent; targets present; nested `.git` intact. Reverse = move dated folder back to original root short name.

## Skipped / deferred / remaining

| Folder | Role | Reason |
| --- | --- | --- |
| `WorkSpace` | **Fail-closed defer** | Messy **multi-remote** on `hermes-agent` (+ backup/quarantine clones); **unexpected extra roots** under `_backups` / `_quarantine`; XL; must-preserve **draft** Medium — flag only, do not invent final lock; consider later git-strategy |
| `PWAExemple` | Remaining on Multi-experiment row | Not fail-closed; deferred from **first 1–2** as higher-complexity peer (3 roots, opaque `.env`×4, one SSH) |
| Medium/Early archive & paused paths | Verify-only | Roots absent / dest present — **never re-propose as sources** |

## Required facts

- All four candidates exist at `C:\Project\<Name>`; INDEX paths current (not already-moved).  
- Date labels from CreationTime: `2025.08.08 - GitTest`, `2025.07.01 - WorkStationPWA`, `2025.06.25 - PWAExemple`, `2026.05.29 - WorkSpace`.  
- Cutoff `2026-06-12`: all four → heuristic **archive** (WorkSpace LastWrite 2026-06-10 = 91 days).  
- `archive` / `paused` parents exist; `active` does not.  
- Org-repo protect; taxonomy **proposed-ratified — ready for user sign-off**; must-preserve **draft — not auto-locked / for user review**.  
- Mutation class: `fs_mutation`; per-batch plan gate mandatory.

## Unknowns / blockers

| Item | Status |
| --- | --- |
| User plan-gate approval of exact map | **Pending** (implementer gate; not a research blocker) |
| WorkSpace hard hazards | **Documented** — deferred (not in subset) |
| Linked worktrees on recommended peers | **None** on live-check |
| Push/pull | **N/A** (no agent remote ops expected) |
| Final taxonomy / must-preserve ratification | Not required to re-block; WorkSpace still fail-closed on git hazards |

### Push/auth dual preflight

**N/A** — refined prompt: no agent remote push/pull for this cycle. Path-only FS moves only.  
(Agent PATH git observed as MSYS `C:\msys64\usr\bin\git.exe`; user-local Git also at `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe`. Irrelevant for path-only corpus moves.)

## Risks

- Implementer must **re-scan** nested `.git` / worktrees / remotes immediately before each move (fail-closed if new hazards).  
- Name confusion: `GitTest\NextTest` ≠ archived Medium `NextTest` — do not touch archives.  
- INDEX/inventory nested-count drift (PWAExemple 3 vs 2; WorkSpace 7 vs ~3) — fix docs after reality, do not invent re-moves.  
- Opaque `.env` on later `PWAExemple` / `WorkSpace` batches — path presence only; any read/log is Critical process failure.  
- Continuity / Choose ≠ move approval.

## Canonical references

- `sessions/2026.09.10/01-prompt-betterment/refined-prompt.md`  
- `sessions/2026.09.10/01-prompt-betterment/notes.md`  
- `sessions/2026.09.10/02-research/codebase-findings.md`  
- `sessions/2026.09.10/02-research/online-findings.md`  
- `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/must-preserve.md`, `catalogue/taxonomy.md`  
- `program/ROADMAP.md`  
- Prior: `sessions/2026.09.09-1612/02-research/`  
- https://git-scm.com/docs/git-worktree.html  
- https://codemia.io/knowledge_hub/path/change_git_repository_directory_location  
- https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository (anti-pattern citation)
