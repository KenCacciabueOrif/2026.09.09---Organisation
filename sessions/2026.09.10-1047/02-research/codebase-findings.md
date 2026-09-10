# Codebase findings — Cycle 11 Multi-experiment (`WorkSpace` only / continue strategy)

**Session:** `sessions/2026.09.10-1047/02-research/`  
**Scope:** Re-probe live `C:\Project\WorkSpace` **against** `program/git-strategy-workspace-hazards.md` (Cycle 10 baseline). Deltas only — do not re-litigate classification from scratch.  
**Mutation class:** **`docs_only`**. No corpus moves. No Appendix A execute. No peer reopen. No `.env` content quotes. No remote URL rewrite.

**Probe method note:** Interactive shell stdout was unavailable this researcher turn; path truth and hazard re-probe used filesystem `Read` of known Cycle 10 paths (directory-present vs file-not-found). Cheap size band **carried** from Cycle 10 (~5786 MB) — structure/HEADs/remotes unchanged → band presumed stable; do not invent a new size number.

## Strategy artifact (anchor)

| Path | Role |
| --- | --- |
| `program/git-strategy-workspace-hazards.md` | **Primary Continuity baseline** — Cycle 10 classification + safe rules + fate table |
| `sessions/2026.09.10-0907/` | Prior cycle that wrote the artifact; Appendix A **unused**; zero corpus moves |
| `sessions/2026.09.10-0848/` | Cycle 9 defer — **do not** re-default as primary narrative |

## INDEX live path truth

| Name | INDEX current path | Disk | Verdict |
| --- | --- | --- | --- |
| `WorkSpace` | `C:\Project\WorkSpace` | **present** (nested trees readable) | Path honest — still at root; **verify-only** for location; **never re-move** |
| proposed archive | `C:\Project\archive\2026.05.29 - WorkSpace` | **absent** | Destination free; whole-tree archive still **OUT OF SCOPE** |
| proposed paused / active dated WorkSpace | under `paused\` / `active\` | **absent** | No drift |
| `PWAExemple` | `C:\Project\archive\2025.06.25 - PWAExemple` | archive **present** (dir); root `C:\Project\PWAExemple` **absent** | **verify-only** — never re-propose as source |
| `GitTest` | `C:\Project\archive\2025.08.08 - GitTest` | archive **present**; root **absent** | **verify-only** |
| `WorkStationPWA` | `C:\Project\archive\2025.07.01 - WorkStationPWA` | archive **present**; root **absent** | **verify-only** |

Parents: `C:\Project\archive` **yes**; `C:\Project\paused` **yes**; `C:\Project\active` **no** (same as Cycle 10).

### Medium / Early roots (must stay closed)

Sampled short-name roots under `C:\Project\` **absent** (`NextTest`, `CursorMobileWorkspace`). Do **not** reopen Medium / Early or archived Multi-experiment peers as move sources.

## Status heuristic (90-day) — carry

| Folder | CreationTime (prior) | LastWriteTime (prior) | Heuristic layout |
| --- | --- | --- | --- |
| `WorkSpace` | 2026-05-29 | 2026-06-10 | **archive** label if a future whole-tree map ever exists — **not** a green map this cycle |

Date label remains `2026.05.29 - WorkSpace` (INDEX proposal only).

## Coarse map (WorkSpace)

Top-level children (unchanged):

- `OS-IA`
- `TestNewWorkspaceAgent`

No top-level `WorkSpace\.git`.

Named hazard parent trees still present:

- `TestNewWorkspaceAgent\_backups` — directory present
- `TestNewWorkspaceAgent\_quarantine` — directory present

Do **not** deep-document `node_modules` / caches.

## Nested `.git` roots — re-probe vs Cycle 10

All **seven** Cycle 10 roots still present (configs/`HEAD` readable). Linked `.git/worktrees` dir on live hermes: **absent** → linked worktrees still **none** on the primary multi-remote root (same class as Cycle 10).

| # | Nested path | Class | Remotes (names + scheme) | HEAD (main) | Delta vs Cycle 10 |
| --- | --- | --- | --- | --- | --- |
| 1 | `OS-IA\.git` | Primary | `origin` HTTPS | (present) | **unchanged** |
| 2 | `TestNewWorkspaceAgent\.git` | Primary | `origin` HTTPS | (present) | **unchanged** |
| 3 | `TestNewWorkspaceAgent\hermes-agent\.git` | Primary live | **`origin` + `cada`** HTTPS | `4fbff573…` | **unchanged** |
| 4 | `…\Projects\…\orchestrateur\.git` | Primary | `origin` HTTPS | (present) | **unchanged** |
| 5 | `…\Projects\…\WorkshopOrif\.git` | Primary | `origin` HTTPS | (present) | **unchanged** |
| 6 | `…\_backups\…\hermes-agent\.git` | Backup clone | **`origin` + `cada`** HTTPS | `8d60d929…` | **unchanged** |
| 7 | `…\_quarantine\…\hermes-agent\.git` | Quarantine clone | **`origin` + `cada`** HTTPS | `8d60d929…` | **unchanged** (matches backup) |

**Nested-root count:** still **7**. Inventory older undercount “3” remains docs honesty only.

**Primary vs clone:** still **5 primary / 2 clone**; live hermes HEAD ≠ backup/quarantine HEAD.

**SSH origin rewrite:** still **N/A** on this tree (all HTTPS). Continuity still forbids URL rewrite unless a later gated step says otherwise.

## Opaque secrets (path presence only)

- Cycle 10 catalogued **17** `.env` / `.env.*` / `.envrc` paths (unread).
- Cycle 11: bak / example / envrc paths under `_backups` / `_quarantine` / live hermes still **present** (path existence confirmed; **contents never quoted** in session artifacts).
- Treat count as **still present / not cleared** — do not claim secrets hazard gone.

## Size / preserve

- Cheap size: **XL** band — **carry Cycle 10 ~5786 MB** (`_backups` / `_quarantine` ~1662 MB each in Cycle 10). No evidence of tree relocation that would clear XL.
- `catalogue/must-preserve.md`: **Medium** draft for `C:\Project\WorkSpace` — **draft — not auto-locked / for user review**.

## Clearance / Appendix A

| Question | Live answer |
| --- | --- |
| Hazards classified? | **Yes** (Cycle 10 artifact; Cycle 11 re-probe confirms) |
| Hazards cleared for whole-tree? | **NO** — classified ≠ cleared |
| Appendix A scoped isolation executed? | **NO** — Cycle 10 SESSION: Appendix A unused; Continuity this cycle is Q1=A continue strategy (**not** B) |
| Whole-tree archive under ordinary Multi-experiment? | **OUT OF SCOPE** |
| Corpus FS mutation this cycle? | **None** — `docs_only` |

## Recommended docs_only refinements (for planner — not a plan)

Update honesty / strategy **text only**:

1. **`program/git-strategy-workspace-hazards.md`** — add Cycle 11 re-probe attestation (date + “no material delta”; HEADs/remotes/nested count unchanged; clearance still **NO**; Appendix A still unused).
2. **`catalogue/INDEX.md`** WorkSpace row — note Cycle 11 continue-strategy pass; still at `C:\Project\WorkSpace`; do **not** claim moved or cleared.
3. **`program/ROADMAP.md`** Multi-experiment row — append Cycle 11 (`sessions/2026.09.10-1047/`) docs_only continue-strategy; **Remaining: `WorkSpace` only**; **not** Complete; no Primary-next / Special git jump.
4. Optional: `catalogue/inventory.md` WorkSpace note line for Cycle 11 (same honesty).
5. Do **not** invent whole-tree archive map; do **not** execute Appendix A; do **not** reopen peers.

## Program / catalogue paths that matter

| Path | Why |
| --- | --- |
| `program/git-strategy-workspace-hazards.md` | Anchor — refine, don’t replace |
| `program/ROADMAP.md` | Lock same row / Remaining WorkSpace only |
| `catalogue/INDEX.md` | Path honesty |
| `catalogue/must-preserve.md` | Draft Medium caution only |
| `sessions/2026.09.10-1047/01-prompt-betterment/` | Q1=A continue strategy locked |
| `sessions/2026.09.10-0907/` | Strategy written; Appendix A unused |

## Org-repo protect

`C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` — default-preserve; session docs stay inside org git root only.
