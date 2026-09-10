# Research brief — Cycle 9 Multi-experiment (`WorkSpace` only)

**Session:** `sessions/2026.09.10-0848/02-research/`  
**Goal:** Live-check hazards on `C:\Project\WorkSpace` under Continuity **Q1=A** (research; move **only** if clearly cleared; else fail-closed defer). **No dedicated git-strategy** this cycle. **No moves. No plan file. No push/pull.**

## Hazard outcome (explicit)

**Hazards cleared?** → **NO**

**Recommendation:** **fail-closed defer** (expected). **No green from→to move map.**

Hard reasons (live re-probe 2026-09-10):

| Hazard | Evidence |
| --- | --- |
| Messy multi-remote | `TestNewWorkspaceAgent\hermes-agent` has **2** remotes (`origin` + `cada`); same dual-remote pattern on `_backups` and `_quarantine` hermes-agent clones |
| Unexpected extra roots | Nested `.git` under `_backups\…\hermes-agent` and `_quarantine\…\hermes-agent` (backup/quarantine copies) |
| Complexity / size | **7** nested roots (inventory undercount “3”); **XL** (~GB-scale) |
| Must-preserve draft | Medium flag in `catalogue/must-preserve.md` — caution only; **not** the sole gate; git hazards already require defer |

Linked worktrees: **none** (not the blocker). SSH origins on this tree: **none** (all HTTPS; path-only Continuity still applies elsewhere). Opaque `.env` paths: **17** present unread.

## Recommended approach

**Option A (recommended): `docs_only` fail-closed defer — zero corpus moves**

- Session artifacts + honest INDEX/ROADMAP notes: `WorkSpace` remains at `C:\Project\WorkSpace`; Multi-experiment **in progress**; **Remaining: `WorkSpace` only**.  
- Do **not** mark Complete; do **not** jump Primary next / Special git.  
- Do **not** start git-strategy plan body (Q1≠B).  
- Do **not** force-move. Do **not** reopen Medium / archived Multi-experiment peers as sources.  
- Pros: matches Q1=A + refined AC; honest catalogue; avoids unsafe relocation of multi-remote + backup/quarantine clones.  
- Cons: Multi-experiment row stays open until a future cleared probe or dedicated git-strategy Continuity.

## Options considered

1. **Option A — docs_only defer (recommended)** — above.  
2. **Option B — green map WorkSpace → `archive\2026.05.29 - WorkSpace`**  
   - Pros: would finish Multi-experiment if safe.  
   - Cons: **rejected** — hazards **not clearly cleared**; Q1=A forbids force-move; would invent git-strategy mid ordinary Continuity.  
3. **Option C — invent dedicated git-strategy execution this cycle**  
   - Pros: might eventually unblock WorkSpace.  
   - Cons: **rejected** — user Continuity Q1=A explicitly excludes Q1=B this cycle; refined prompt out of scope.

**Rejected:** re-proposing `PWAExemple` / `GitTest` / `WorkStationPWA` or Medium/Early paths as sources (archive/paused verify-only; roots cleared).

## Proposed move map

**None.** (No green map while uncleared.)

Hypothetical destination **only for a future cleared/git-strategy cycle** (not this plan):  
`C:\Project\WorkSpace` → `C:\Project\archive\2026.05.29 - WorkSpace` — **do not schedule** now.

## Skipped / deferred / remaining

| Folder | Role | Reason |
| --- | --- | --- |
| `WorkSpace` | **Fail-closed defer** (still) | Multi-remote + unexpected `_backups`/`_quarantine` roots + XL + draft Medium flag; git-strategy **later opt-in only** |
| `PWAExemple`, `GitTest`, `WorkStationPWA` | Verify-only | Already at Cycle 7/8 archive paths — **never re-propose** |
| Medium / Early archive & paused | Verify-only | Roots absent — **never reopen as sources** |

## Required facts

- `WorkSpace` exists at INDEX root path; dated archive/paused/active targets **absent** (no “already moved” drift).  
- CreationTime label `2026.05.29`; LastWrite `2026-06-10`; 90-day heuristic → **archive**.  
- Mutation class this cycle: **`docs_only`** (session + INDEX/ROADMAP honesty).  
- Taxonomy: **proposed-ratified — ready for user sign-off**; must-preserve: **draft — not auto-locked / for user review**.  
- Continuity / Choose ≠ move approval (moot while no map).  
- Org-repo only for any doc commits; no sibling-tree ops.

## Unknowns / blockers

| Item | Status |
| --- | --- |
| WorkSpace hard hazards | **Still present** — **blocker for move**; expected defer |
| Dedicated git-strategy Continuity | **Not chosen** this cycle (Q1=A) |
| Linked worktrees | **None** |
| Push/pull / auth dual preflight | **N/A** — no agent remote sync in refined prompt |
| Dirty working tree (corpus) | **N/A** for moves (zero moves); org-repo publish separate if requested later |
| Plan-gate for `fs_mutation` | **N/A** this cycle (no map); if a future cycle proposes a map, gate mandatory |

### Push/auth dual preflight

**N/A** — refined prompt: no agent `git push` / `git pull` for this cycle. Path research only.

## Risks

- Planner/implementer must **not** invent a move map or force-move despite Continuity “yes”.  
- Auditor must see **Remaining: WorkSpace only** and row **not** Complete.  
- Opaque `.env` — any read/log is Critical process failure.  
- Future git-strategy must be an **explicit** Continuity/Choose lock — not smuggled as ordinary Multi-experiment finalize.  
- INDEX/inventory nested-count drift (7 vs 3) — fix docs when editing honesty notes; never invent re-moves.

## Canonical references

- `sessions/2026.09.10-0848/01-prompt-betterment/refined-prompt.md`  
- `sessions/2026.09.10-0848/02-research/codebase-findings.md`  
- `sessions/2026.09.10-0848/02-research/online-findings.md`  
- Prior: `sessions/2026.09.10-0811/02-research/`, `sessions/2026.09.10/02-research/`  
- `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/must-preserve.md`  
- `program/ROADMAP.md`  
- https://git-scm.com/docs/git-worktree  
- https://git-scm.com/docs/git-remote  
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
