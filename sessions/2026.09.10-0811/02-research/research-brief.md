# Research brief — Cycle 8 Multi-experiment (remaining subset)

**Session:** `sessions/2026.09.10-0811/02-research/`  
**Goal:** Live-check remaining Multi-experiment candidates (`PWAExemple`, `WorkSpace`); recommend executable map consistent with Q1=A (prefer green `PWAExemple`; keep `WorkSpace` fail-closed until cleared). **No moves. No push/pull. No plan file.**

## Recommended approach

**Option A (recommended): remaining executable map = `PWAExemple` only → `archive`**

`PWAExemple` exists at honest INDEX root path; CreationTime label matches INDEX proposal (`2025.06.25 - PWAExemple`); 90-day heuristic → **archive**; **3** nested `.git` dirs (INDEX undercount → fix docs after move), **one main worktree** each, **single remote** each (2× HTTPS + 1× SSH path-only); opaque `.env`×4 (unread); M-band; not on must-preserve draft; destination parent exists; proposed dated target **absent**. Hard fail-closed screen: **clean**.

`WorkSpace` hazards **re-confirmed** (not cleared): messy multi-remote on `hermes-agent` (+ backup/quarantine clones), unexpected extra roots under `_backups` / `_quarantine`, XL, must-preserve draft Medium — **fail-closed defer** / git-strategy candidate; do **not** force-move; do **not** start dedicated git-strategy **execution** by default.

| From | To | Nested `.git` stays under (atomic) |
| --- | --- | --- |
| `C:\Project\PWAExemple` | `C:\Project\archive\2025.06.25 - PWAExemple` | `…\PWAExempleAuth\PWAExempleAuth\PWAExempleAuth\.git`, `…\PWAExempleNext\.git`, `…\PWAFrontAuthTest\.git` |

- Atomic unit = whole top-level wrapper (all nested git + non-git children + opaque `.env` paths unread). Prefer single `Move-Item`; on Windows nested-`.git` lock → Continuity recovery (`robocopy /E /MOVE`, empty shells only, re-attest).  
- Remotes: note schemes (HTTPS / SSH); **never rewrite**.  
- Catalogue: update INDEX (+ inventory nested count 2→3) after move.  
- ROADMAP Notes: after success, remaining Multi-experiment name = **`WorkSpace`** (row stays **in progress** — **not** Complete).  
- **Plan gate** required before implementer (Choose-all Continuity ≠ map approval).

## Options considered

1. **Option A — PWAExemple only → archive (recommended)**  
   - Pros: matches Q1=A; only green remaining candidate; path-only SSH OK; opaque `.env` Continuity already proven on Medium cycles; leaves fail-closed `WorkSpace` deferred with logged reason.  
   - Cons: subset shrinks to one name; INDEX nested-count drift (3 vs 2) needs post-move doc fix; possible Windows lock recovery on 3 nested roots (process deviation Continuity, not scope expansion).

2. **Option B — PWAExemple + WorkSpace**  
   - Pros: could finish Multi-experiment row in one batch if WorkSpace were green.  
   - Cons: **rejected** — WorkSpace hard hazards **not cleared**; Q1=A forbids force-move; would invent unsafe/git-strategy work mid batch.

3. **Option C — defer both / zero moves**  
   - Pros: maximal caution.  
   - Cons: under-uses Continuity preference for green `PWAExemple`; no evidence requires blocking `PWAExemple`. Prefer A unless plan gate shrinks to zero on new pre-move hazards.

**Rejected:** re-proposing `GitTest` / `WorkStationPWA` or Medium/Early destinations as sources (already at archive/paused — verify-only).

## Recommended subset (explicit)

1. `PWAExemple` → `archive\2025.06.25 - PWAExemple`

## Proposed move map (hypothesis until plan gate)

- `C:\Project\PWAExemple` → `C:\Project\archive\2025.06.25 - PWAExemple` (**archive**)

Pre: source exists; target absent (live-checked). Post verify: source absent; target present; nested `.git`×3 intact; SSH/HTTPS remotes unchanged; `.env` paths present unread. Reverse = move dated folder back to `C:\Project\PWAExemple`.

## Skipped / deferred / remaining

| Folder | Role | Reason |
| --- | --- | --- |
| `WorkSpace` | **Fail-closed defer** (still) | Messy **multi-remote** on `hermes-agent` (+ backup/quarantine clones); **unexpected extra roots** under `_backups` / `_quarantine`; XL; must-preserve **draft** Medium — flag only; later **git-strategy** candidate; do **not** execute strategy this cycle by default |
| `GitTest`, `WorkStationPWA` | Verify-only | Already at Cycle 7 archive paths; roots cleared — **never re-propose** |
| Medium/Early archive & paused paths | Verify-only | Roots absent / dest present — **never re-propose as sources** |

## Required facts

- Remaining candidates exist at `C:\Project\PWAExemple` and `C:\Project\WorkSpace`; INDEX paths current (not already-moved).  
- Date labels from CreationTime: `2025.06.25 - PWAExemple`, `2026.05.29 - WorkSpace`.  
- Cutoff `2026-06-12`: both → heuristic **archive**.  
- `archive` / `paused` parents exist; `active` does not.  
- Cycle 7 archives present; root short names absent.  
- Org-repo protect; taxonomy **proposed-ratified — ready for user sign-off**; must-preserve **draft — not auto-locked / for user review**.  
- Mutation class: `fs_mutation`; per-batch plan gate mandatory.  
- `WorkSpace` fail-closed **not cleared** on this live re-probe.

## Unknowns / blockers

| Item | Status |
| --- | --- |
| User plan-gate approval of exact map | **Pending** (implementer gate; not a research blocker) |
| WorkSpace hard hazards | **Still present** — deferred (not in map) |
| Linked worktrees on `PWAExemple` | **None** on live-check |
| Push/pull | **N/A** (no agent remote ops expected) |
| Final taxonomy / must-preserve ratification | Not required to re-block; WorkSpace still fail-closed on **git** hazards (not solely draft preserve) |

### Push/auth dual preflight

**N/A** — refined prompt: no agent remote push/pull for this cycle. Path-only FS moves only.

## Risks

- Implementer must **re-scan** nested `.git` / worktrees / remotes immediately before move (fail-closed if new hazards).  
- Opaque `.env`×4 on `PWAExemple` — path presence only; any read/log is Critical process failure.  
- INDEX/inventory nested-count drift (`PWAExemple` 3 vs 2) — fix docs after reality.  
- Windows nested-`.git` lock possible (Cycle 7 precedent) — follow Continuity recovery; log deviation.  
- After `PWAExemple` move, Multi-experiment row still has **`WorkSpace` remaining** — do **not** mark Complete; do **not** jump Primary next.  
- Continuity / Choose ≠ move approval.

## Canonical references

- `sessions/2026.09.10-0811/01-prompt-betterment/refined-prompt.md`  
- `sessions/2026.09.10-0811/02-research/codebase-findings.md`  
- `sessions/2026.09.10-0811/02-research/online-findings.md`  
- Prior Cycle 7: `sessions/2026.09.10/02-research/`  
- `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/must-preserve.md`, `catalogue/taxonomy.md`  
- `program/ROADMAP.md`  
- https://git-scm.com/docs/git-worktree.html  
- https://codemia.io/knowledge_hub/path/change_git_repository_directory_location  
- https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository  
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
