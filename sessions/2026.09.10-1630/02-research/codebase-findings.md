# Codebase findings — Cycle 13 Multi-experiment (`WorkSpace` only / continue strategy)

**Session:** `sessions/2026.09.10-1630/02-research/`  
**Scope:** Re-probe live `C:\Project\WorkSpace` **against** `program/git-strategy-workspace-hazards.md` (Cycle 10 baseline + Cycles 11–12 attestations). Deltas only — do not re-litigate classification from scratch.  
**Mutation class:** **`docs_only`**. No corpus moves. No Appendix A execute. No peer reopen. No `.env` content quotes. No remote URL rewrite.

**Probe method:** Interactive **Shell** (`Test-Path`, recursive `.git` discovery excl. `node_modules`/caches, `git rev-parse` / `git remote -v` / `git worktree list`, cheap size `Measure-Object`). PATH git this turn: `C:\msys64\usr\bin\git.exe` (counts/remotes/HEADs authoritative). Cross-checked INDEX destinations with `Test-Path`.

## Strategy artifact (anchor)

| Path | Role |
| --- | --- |
| `program/git-strategy-workspace-hazards.md` | **Primary Continuity baseline** — Cycle 10 classification + Cycles 11–12 attestations + safe rules + fate table |
| `sessions/2026.09.10-1247/` | Cycle 12 continue-strategy re-attest; clearance **NO**; Appendix A unused |
| `sessions/2026.09.10-1047/` | Cycle 11 continue-strategy re-attest |
| `sessions/2026.09.10-0907/` | Cycle 10 wrote the artifact; Appendix A draft only |
| `sessions/2026.09.10-0848/` | Cycle 9 defer — **do not** re-default as primary narrative |

## INDEX live path truth

| Name | INDEX current path | Disk (`Test-Path`) | Verdict |
| --- | --- | --- | --- |
| `WorkSpace` | `C:\Project\WorkSpace` | **present** (`True`) | Path honest — still at root; **verify-only** for location; **never re-move** |
| proposed archive | `C:\Project\archive\2026.05.29 - WorkSpace` | **absent** (`False`) | Destination free; whole-tree archive still **OUT OF SCOPE** |
| proposed paused / active dated WorkSpace | under `paused\` / `active\` | **absent** (no dated WorkSpace tree; `active` parent absent) | No drift |
| `PWAExemple` | `C:\Project\archive\2025.06.25 - PWAExemple` | archive **present**; root `C:\Project\PWAExemple` **absent** | **verify-only** — never re-propose as source |
| `GitTest` | `C:\Project\archive\2025.08.08 - GitTest` | archive **present**; root **absent** | **verify-only** |
| `WorkStationPWA` | `C:\Project\archive\2025.07.01 - WorkStationPWA` | archive **present**; root **absent** | **verify-only** |

Parents: `C:\Project\archive` **yes**; `C:\Project\paused` **yes**; `C:\Project\active` **no** (same as Cycles 10–12).

### Medium / Early roots (must stay closed)

Sampled short-name roots under `C:\Project\` **absent** (`NextTest`, `Simpl`, `CursorMobileWorkspace`, `NextPWATraining`). Do **not** reopen Medium / Early or archived Multi-experiment peers as move sources.

**Multi-experiment remaining:** **`WorkSpace` only** — peers not live at `C:\Project\<name>`.

## Status heuristic (90-day) — re-confirmed from disk

| Folder | CreationTime | LastWriteTime | Heuristic layout |
| --- | --- | --- | --- |
| `WorkSpace` | 2026-05-29 | 2026-06-10 | **archive** label if a future whole-tree map ever exists — **not** a green map this cycle |

Date label remains `2026.05.29 - WorkSpace` (INDEX proposal only).

## Coarse map (WorkSpace)

Top-level children (unchanged):

- `OS-IA`
- `TestNewWorkspaceAgent`

No top-level `WorkSpace\.git` (`Test-Path` → `False`).

Named hazard parent trees still present:

- `TestNewWorkspaceAgent\_backups` — present
- `TestNewWorkspaceAgent\_quarantine` — present

Do **not** deep-document `node_modules` / caches.

## Nested `.git` roots — re-probe vs Cycle 10 / 11 / 12

All **seven** Cycle 10 roots still present. Linked worktrees: **`worktree list` count = 1** (main only) on each root; `.git/worktrees` dirs **absent** → linked worktrees still **none**.

| # | Nested path | Class | Remotes (names + scheme) | HEAD (short) | Delta vs Cycle 12 |
| --- | --- | --- | --- | --- | --- |
| 1 | `OS-IA\.git` | Primary | `origin` HTTPS | present (`master`) | **unchanged** |
| 2 | `TestNewWorkspaceAgent\.git` | Primary | `origin` HTTPS | present (`self-improvement-infra`) | **unchanged** |
| 3 | `TestNewWorkspaceAgent\hermes-agent\.git` | Primary live | **`origin` + `cada`** HTTPS | `4fbff573…` | **unchanged** |
| 4 | `…\Projects\Project Atelier IA\Projet Adrien\orchestrateur\.git` | Primary | `origin` HTTPS | present (`master`) | **unchanged** |
| 5 | `…\Projects\Project Atelier IA\Workshop\WorkshopOrif\.git` | Primary | `origin` HTTPS | present (`feature/formation-level-courses`) | **unchanged** |
| 6 | `…\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent\.git` | Backup clone | **`origin` + `cada`** HTTPS | `8d60d929…` | **unchanged** |
| 7 | `…\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent\.git` | Quarantine clone | **`origin` + `cada`** HTTPS | `8d60d929…` | **unchanged** (matches backup) |

**Nested-root count:** still **7**. Inventory older undercount “3” remains docs honesty only.

**Primary vs clone:** still **5 primary / 2 clone**; live hermes HEAD ≠ backup/quarantine HEAD.

**SSH origin rewrite:** still **N/A** on this tree (all HTTPS). Continuity still forbids URL rewrite unless a later gated step says otherwise.

## Opaque secrets (path presence only)

- Cycle 10 catalogued **17** `.env` / `.env.*` / `.envrc` paths (unread in session artifacts).
- Cycle 13 live re-count: **17** paths still present (names/paths only; **contents never read or quoted**).
- Treat secrets hazard as **still present / not cleared**.

## Size / preserve

- Cheap size re-measure: **XL ~5786 MB** total (`OS-IA` ~222 MB; `TestNewWorkspaceAgent` ~5564 MB); `_backups` ~1662 MB; `_quarantine` ~1662 MB — **identical band** to Cycle 10 (and carried through Cycles 11–12).
- `catalogue/must-preserve.md`: **Medium** draft for `C:\Project\WorkSpace` — **draft — not auto-locked / for user review**.

## Clearance / Appendix A

| Question | Live answer |
| --- | --- |
| Hazards classified? | **Yes** (Cycle 10 artifact; Cycles 11–13 re-probe confirm) |
| Material delta vs Cycle 12 attestation? | **No** |
| Material delta vs Cycle 11 / Cycle 10 classification? | **No** |
| Hazards cleared for whole-tree? | **NO** — classified ≠ cleared |
| Appendix A scoped isolation executed? | **NO** — still unused; Continuity this cycle is Q1=A continue strategy (**not** B) |
| Appendix A readiness (note only) | Illustrative from→to still in `sessions/2026.09.10-0907/03-plan/plan.md` Appendix A; parents still under WorkSpace; destinations must be re-confirmed free if a **future** Continuity B + plan gate selects execute — **not** this cycle |
| Whole-tree archive under ordinary Multi-experiment? | **OUT OF SCOPE** |
| Corpus FS mutation this cycle? | **None** — `docs_only` |

## Recommended docs_only refinements (for planner — not a plan)

Update honesty / strategy **text only**:

1. **`program/git-strategy-workspace-hazards.md`** — add Cycle 13 re-probe attestation (date + “no material delta” vs Cycle 12; HEADs/remotes/nested count/size/env count unchanged; clearance still **NO**; Appendix A still unused). Point Research links at this session.
2. **`catalogue/INDEX.md`** WorkSpace row — note Cycle 13 continue-strategy pass; still at `C:\Project\WorkSpace`; do **not** claim moved or cleared.
3. **`program/ROADMAP.md`** Multi-experiment row — append Cycle 13 (`sessions/2026.09.10-1630/`) docs_only continue-strategy; **Remaining: `WorkSpace` only**; **not** Complete; no Primary-next / Special git jump; Next FAW lock hint = continue strategy **or** Continuity B + plan gate.
4. Optional: `catalogue/inventory.md` WorkSpace note line for Cycle 13 (same honesty).
5. Do **not** invent whole-tree archive map; do **not** execute Appendix A; do **not** reopen peers.

## Program / catalogue paths that matter

| Path | Why |
| --- | --- |
| `program/git-strategy-workspace-hazards.md` | Anchor — refine, don’t replace |
| `program/ROADMAP.md` | Lock same row / Remaining WorkSpace only |
| `catalogue/INDEX.md` | Path honesty |
| `catalogue/must-preserve.md` | Draft Medium caution only |
| `sessions/2026.09.10-1630/01-prompt-betterment/` | Q1–Q3=A continue strategy locked |
| `sessions/2026.09.10-1247/` | Prior continue-strategy attestation (Cycle 12) |
| `sessions/2026.09.10-0907/03-plan/plan.md` Appendix A | Non-executed illustrative map only |

## Org-repo protect

Stage/commit only this organisation git root when publishing session docs; no sibling-tree ops under `C:\Project\WorkSpace` or archive peers.
