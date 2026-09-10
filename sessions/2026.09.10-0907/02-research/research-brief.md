# Research brief — Cycle 10 Multi-experiment (`WorkSpace` only + hazard remediation)

**Session:** `sessions/2026.09.10-0907/02-research/`  
**Goal:** Dedicated **git-strategy / hazard remediation** research for `C:\Project\WorkSpace` under Continuity **Q1=A** (remediation track), **Q2=A** (docs-first; optional scoped isolation map), **Q3=A** (carry Continuity).  
**No plan file. No implementation. No whole-tree archive. No peer reopen.**

## One-line outcome

Hazards **re-confirmed and classified**; recommend **`docs_only` strategy artifacts by default**, with an **optional research-supported scoped isolation map** for named `_backups` / `_quarantine` trees only (plan-gated) — **not** whole-tree Multi-experiment archive as “solved.”

## Hazard classification (live 2026-09-10)

| Hazard | Classification | Evidence |
| --- | --- | --- |
| Multi-remote | **Live primary + clones** | `hermes-agent` (live, `_backups`, `_quarantine`) each have remotes **`origin` + `cada`** (HTTPS); other five roots single `origin` HTTPS |
| Unexpected nested roots | **Backup clone + quarantine clone** | Extra `.git` under `_backups\…\hermes-agent` and `_quarantine\…\hermes-agent` |
| Primary vs clone | **5 primary / 2 clone** | Live hermes HEAD `4fbff573…`; backup+quarantine share `8d60d929…` (not ancestor of live) |
| Nested-root count | **7** (unchanged vs Cycle 9) | Inventory undercount “3” = docs drift only |
| Linked worktrees | **None** | Not a blocker |
| Size | **XL ~5786 MB** | `_backups` ~1662 MB; `_quarantine` ~1662 MB |
| Opaque `.env*` | **17 paths** unread | Presence only |
| Must-preserve | **Draft Medium** caution | Not auto-locked; not sole gate |
| SSH origin rewrite | **N/A on this tree** | All HTTPS; Continuity still forbids rewrite |

### Recommended fate of `_backups` / `_quarantine` git roots

| Unit | Fate | Rationale |
| --- | --- | --- |
| `…\_backups` (whole parent tree) | **Isolate** (preferred) / keep / defer — **do not delete by default** | Labeled backup; contains dual-remote hermes clone + opaque `.env*`; ~1.6 GB |
| `…\_quarantine` (whole parent tree) | **Isolate** (preferred) / keep / defer — **do not delete by default** | Labeled quarantine; hermes clone HEAD matches backup; dual-remote + opaque `.env*` |
| Live primary roots (incl. live `hermes-agent`) | **Keep in place** this cycle | Isolation of clones does not clear live multi-remote; whole-tree OOS |

Isolation means relocating the **named parent trees** intact to a dedicated quarantine/isolation destination (planner names concrete from→to if proposing `fs_mutation`) — **not** merging into live hermes, **not** remote URL rewrite, **not** history rewrite.

## Safe relocation / isolation rules (docs for future or gated use)

1. **Atomic nested git** — move intact trees that contain `.git`; never strip history / `filter-repo` / force-push.  
2. **Named units only for scoped FS** — prefer whole `_backups` and/or `_quarantine` parents; do not cherry-pick empty `.git` shells.  
3. **Opaque `.env*`** — path presence only; never read/quote/log contents; include paths in intent-preview as unread.  
4. **Remotes path-only** — inventory names + schemes; **no** `git remote set-url` / origin rewrite this cycle unless a later gated step explicitly says so (default: document only).  
5. **No linked-worktree surprise** — re-run `worktree list` immediately before any approved move; if >1 worktree appears, fail-closed.  
6. **Windows lock recovery** — prefer single move; on PermissionDenied/split → reunify + `robocopy /E /MOVE`; remove **only empty** leftover `.git` shells; re-attest; log deviation.  
7. **Whole XL `WorkSpace` → ordinary Multi-experiment archive** — **OUT OF SCOPE**; never claim “solved” via that path this cycle.  
8. **Consent** — Continuity / Choose ≠ plan-gate approval; any `fs_mutation` map needs separate gate + intent-preview.  
9. **Row honesty** — after any scoped isolation (or docs-only pass), Multi-experiment stays **in progress** with **Remaining: `WorkSpace` only** while the XL tree (and live multi-remote) remain; **never** Complete / Primary-next jump.  
10. **Peers** — never reopen Medium/Early or re-propose archived `PWAExemple` / `GitTest` / `WorkStationPWA` as sources.

## Recommended approach options (max 3)

### Option A (recommended): `docs_only` strategy pass + optional gated scoped map note

- Deliver classification, fate, safe rules, INDEX/ROADMAP honesty in session + catalogue notes.  
- **Zero** corpus moves unless user later approves a separate plan-gate map.  
- Planner **may** attach a **scoped** from→to draft for `_backups` and/or `_quarantine` only — **orchestrator waits for plan gate**; Continuity Choose does not authorize execute.  
- Pros: matches Q1=A / Q2=A; reversible; reduces confusion without pretending whole-tree is cleared.  
- Cons: live multi-remote + XL WorkSpace still remain; row stays open.

### Option B: Prioritize scoped `fs_mutation` isolation map this cycle (still gated)

- Same classification, but planner leads with concrete from→to for named `_backups` / `_quarantine` isolation destinations.  
- Pros: research-supported hazard reduction (7→5 roots; ~3.3 GB out of live tree).  
- Cons: still needs plan gate; does **not** clear live multi-remote; Windows XL move risk; must not be framed as Multi-experiment Complete.  
- **Acceptable as planner draft** under Q2=A — not preferred over docs-first packaging.

### Option C: Whole-tree archive `WorkSpace` → `archive\2026.05.29 - WorkSpace`

- **Rejected** — Continuity / refined prompt **OUT OF SCOPE**; hazards not cleared for ordinary Multi-experiment finalize; would falsely mark “solved.”

**Rejected always:** re-proposing archived peers / Medium / Early as sources; remote URL rewrite; `.env` reads; force-delete of backup/quarantine without isolate-keep policy; jumping Primary next / Complete while WorkSpace remains.

## Scoped `fs_mutation` map — research-supported?

| Question | Answer |
| --- | --- |
| Whole-tree archive map? | **No** — OOS; not “solved.” |
| Scoped isolation of named `_backups` and/or `_quarantine`? | **Yes — optional**, research-supported for planner draft after plan gate |
| Default mutation class this cycle? | **`docs_only`** (strategy + honesty); scoped map is **optional add-on**, not required to satisfy remediation Continuity |

Hypothetical scoped map shape (illustrative only — **not** a plan; destinations must be confirmed free at plan time):

- From: `C:\Project\WorkSpace\TestNewWorkspaceAgent\_backups`  
- From: `C:\Project\WorkSpace\TestNewWorkspaceAgent\_quarantine`  
- To: planner-chosen isolation destinations under org taxonomy (e.g. dated quarantine/archive **hygiene** paths) — **not** “move whole WorkSpace.”

## Required facts

- `WorkSpace` still at INDEX root path; dated archive/paused/active targets **absent**.  
- Remotes names: `origin`, `cada` (HTTPS); no SSH on this tree.  
- Taxonomy: **proposed-ratified — ready for user sign-off**; must-preserve: **draft — not auto-locked / for user review**.  
- Org-repo only for doc commits; no sibling-tree ops.  
- Push/pull dual preflight: **N/A** (no agent remote sync in refined prompt).

## Unknowns / blockers

| Item | Status |
| --- | --- |
| Whole-tree Multi-experiment archive | **Blocked** (live multi-remote + XL + Continuity OOS) |
| Scoped isolation execute | **Blocked until plan gate** if planner proposes map; research supports drafting |
| Dedicated remote surgery (`set-url`, drop `cada`) | **Out of scope** this cycle (document only) |
| Linked worktrees | **None** |
| Dirty / auth sync | **N/A** for corpus moves this research |
| User chores to “fix remotes/PATH” | **Not** a remediation requirement |

### Push/auth dual preflight

**N/A** — refined prompt: path/hazard research and strategy docs; no agent `git push` / `git pull` for corpus.

## Risks

- Framing scoped isolation as “WorkSpace done / Multi-experiment Complete.”  
- Inventing whole-tree archive despite Continuity OOS.  
- Treating Continuity Choose as move approval.  
- Deleting backup/quarantine instead of isolate-keep.  
- Reading `.env` contents or rewriting remotes.  
- Reopening Medium / archived peers.  
- Claiming pull/push readiness (N/A).

## Canonical references

- `sessions/2026.09.10-0907/01-prompt-betterment/refined-prompt.md`  
- `sessions/2026.09.10-0907/01-prompt-betterment/notes.md`  
- `sessions/2026.09.10-0907/02-research/codebase-findings.md`  
- `sessions/2026.09.10-0907/02-research/online-findings.md`  
- Prior: `sessions/2026.09.10-0848/02-research/`  
- `catalogue/INDEX.md`, `catalogue/must-preserve.md`, `program/ROADMAP.md`  
- https://git-scm.com/docs/git-worktree  
- https://git-scm.com/docs/git-remote  
- https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
