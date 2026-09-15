# Codebase findings — Cycle 14 (Appendix A move-map evidence)

**Session:** `sessions/2026.09.11/02-research/`  
**Continuity:** **B** locked — scoped Appendix A `fs_mutation` plan (STAGE 1 research only; zero corpus moves this phase)  
**Probe method:** Shell `Test-Path` / `Get-ChildItem` / recursive `.git` discovery / `git remote -v` / `git worktree list` / `git ls-files` / size `Measure-Object` (2026-09-11 live)

---

## INDEX path truth (disk vs catalogue)

| Unit | INDEX current path | Disk | Verdict |
| --- | --- | --- | --- |
| `WorkSpace` (whole tree) | `C:\Project\WorkSpace` (`catalogue/INDEX.md`) | **True** at root | Still live at INDEX root — **not** at archive/paused; **verify-only for whole-tree** (do **not** re-move / do **not** invent whole-tree archive) |
| Dated whole-tree dest `archive\2026.05.29 - WorkSpace` | N/A (not current) | **False** | Confirms whole-tree never moved |
| Dated whole-tree dest `paused\2026.05.29 - WorkSpace` | N/A | **False** | Same |
| Appendix A illustrative dests under `archive\hygiene\…` | Not in INDEX as current WorkSpace path | Parent `C:\Project\archive\hygiene` **False**; Cycle 10 dated leaf names **False**; Cycle 14 dated leaf names **False** | **Destinations free** — planner may create parent + dated leaves |
| Archived peers `GitTest`, `WorkStationPWA`, `PWAExemple` | Archive paths in INDEX | All **True** at archive | **Verify-only** — never re-propose as sources |
| `_backups` / `_quarantine` | Not separate INDEX rows (live under WorkSpace) | Still under WorkSpace (below) | **Still live sources** for Appendix A — not already-at-dest |

**Catalogue notes:** INDEX / inventory still describe WorkSpace nested **7**, Cycles 10–13 docs_only, hazards classified ≠ cleared. No INDEX row claims `_backups`/`_quarantine` already at hygiene destinations.

---

## Live path truth — in-scope parents

| Path | Exists | Role |
| --- | --- | --- |
| `C:\Project\WorkSpace` | True | Live Multi-experiment remaining candidate (whole-tree **clearance NO**) |
| `C:\Project\WorkSpace\OS-IA` | True | Primary nested root #1 — **keep in place** |
| `C:\Project\WorkSpace\TestNewWorkspaceAgent` | True | Primary nested root #2 — **keep in place** |
| `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` | True | Primary nested root #3 (live hermes) — **keep in place** |
| `…\Projects\…\orchestrateur` | True | Primary nested root #4 — **keep in place** |
| `…\Projects\…\WorkshopOrif` | True | Primary nested root #5 — **keep in place** |
| `…\TestNewWorkspaceAgent\_backups` | True | **Appendix A source parent** (~1662 MB) |
| `…\TestNewWorkspaceAgent\_quarantine` | True | **Appendix A source parent** (~1662 MB) |

WorkSpace top children: `OS-IA`, `TestNewWorkspaceAgent` only.  
`C:\Project\archive` True; `C:\Project\paused` True; `C:\Project\active` False.

---

## Nested `.git` roots (count + locations)

**Total under WorkSpace: 7** (unchanged vs Cycles 9–13).

| # | Root path | Class | Move this cycle? |
| --- | --- | --- | --- |
| 1 | `…\WorkSpace\OS-IA` | Primary | No — keep |
| 2 | `…\WorkSpace\TestNewWorkspaceAgent` | Primary | No — keep |
| 3 | `…\TestNewWorkspaceAgent\hermes-agent` | Primary (live hermes) | No — keep |
| 4 | `…\Projects\…\orchestrateur` | Primary | No — keep |
| 5 | `…\Projects\…\WorkshopOrif` | Primary | No — keep |
| 6 | `…\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent` | Clone under backups | **Yes — moves atomically with `_backups` parent** |
| 7 | `…\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent` | Clone under quarantine | **Yes — moves atomically with `_quarantine` parent** |

- **Under `_backups`:** 1 nested `.git` (directory, not gitfile).  
- **Under `_quarantine`:** 1 nested `.git` (directory, not gitfile).  
- Expect nested count **7→5** if both parents move.  
- Do **not** cherry-pick empty `.git` shells; move whole named parents.

---

## Remotes / HEAD / worktrees (path-only inventory)

| Tree | Remotes (HTTPS) | HEAD (short) | Linked worktrees |
| --- | --- | --- | --- |
| Live hermes | `origin` + `cada` | `4fbff573aefc` | Single main; `.git/worktrees` absent |
| Backup hermes clone | `origin` + `cada` (same URLs) | `8d60d929ceaf` | Single main; no linked extras |
| Quarantine hermes clone | `origin` + `cada` (same URLs) | `8d60d929ceaf` | Single main; no linked extras |
| Parent `TestNewWorkspaceAgent` | `origin` only (HTTPS) | (not re-probed for HEAD this pass) | N/A for Appendix A unit |

**Clearance implication:** Isolating clones does **not** clear live hermes multi-remote. Continuity forbids `git remote set-url` / origin rewrite (document only).

**Re-probe before any future approved move:** `git worktree list` again; if unexpected >1, fail-closed (strategy rule 5).

---

## Parent-tree coarse structure (no deep caches)

**`_backups` children:** dated dirs `2026-07-02_pre-cleanup`, `2026-07-08_pre-observability`, `2026-07-13_roaming-settings-drift`, `zed-hermes-audit-20260702-153553`, plus several `*.bak` files at parent root (incl. opaque `.env.20260710-110530.bak`).

**`_quarantine` children:** `copilot-agent-system`, `duplicate-scripts`, `legacy-docs`, `misplaced-files`, `stale-backups-hermes-home`, `stale-backups-workspace`, `temp-probes-2026-07-10`, `vscode-extension-artifacts`, plus one discarded `.py` file.

Size bands: WorkSpace **~5786 MB**; `_backups` **~1662 MB**; `_quarantine` **~1662 MB** (~3.3 GB out of live tree if both move).

---

## Opaque `.env*` (path presence only — contents unread)

**17** paths under WorkSpace (unchanged count vs Cycle 13).

| Scope | Count | Note |
| --- | --- | --- |
| Under `_backups` | 5 | Moves with parent |
| Under `_quarantine` | 5 | Moves with parent |
| Remain under live WorkSpace after both moves | 7 | Live hermes + project roots — do not open/quote |

Planner must list unread paths in intent-preview (strategy rule 3).

---

## Parent git index coupling (planner risk)

`TestNewWorkspaceAgent` (primary root #2) **tracks** paths under the move units:

- `git ls-files '_backups'` → **1157** tracked paths  
- `git ls-files '_quarantine'` → **1150** tracked paths  
- Not ignored by `.gitignore` (no matching ignore for those names)

Moving the trees off-disk will leave the parent working tree showing massive deletions relative to its index. Nested hermes clones remain separate `.git` directories and move intact; remotes inside those clones stay unchanged without rewrite.

**Planner must disclose** in “What the user is approving”: post-move parent dirtiness; default Continuity = **no** remote rewrite, **no** history rewrite, **no** force-push — so do **not** auto-commit / rewrite parent history unless a later gated step says so. Prefer document expected dirty state + optional later hygiene Continuity.

---

## Strategy artifact — Appendix A / safe relocation (authoritative)

**Source:** `program/git-strategy-workspace-hazards.md` (+ illustrative map in `sessions/2026.09.10-0907/03-plan/plan.md` Appendix A).

### Recommended fate (quoted/summarized)

| Unit | Fate |
| --- | --- |
| `_backups` whole parent | **Isolate** (preferred) / keep / defer — **do not delete by default** |
| `_quarantine` whole parent | **Isolate** (preferred) / keep / defer — **do not delete by default** |
| Live primary roots `#1–#5` | **Keep in place** |
| Whole `C:\Project\WorkSpace` → dated archive | **OUT OF SCOPE** until dedicated clearance |

### Safe relocation rules 1–10 (must cite in plan)

1. Atomic nested git — intact trees with `.git`; never strip history / `filter-repo` / force-push.  
2. Named parent units only — whole `_backups` and/or `_quarantine`; no empty-shell cherry-pick.  
3. Opaque `.env*` — path presence only; list unread in intent-preview.  
4. Remotes path-only — inventory only; no `set-url` unless later gated.  
5. No linked-worktree surprise — re-probe before move; >1 → fail-closed.  
6. Windows lock recovery — prefer single move; PermissionDenied → reunify + `robocopy /E /MOVE`; remove **only empty** leftover `.git` shells; re-attest; log deviation.  
7. Whole XL WorkSpace → ordinary Multi-experiment archive — **OOS**.  
8. Consent — Continuity ≠ plan-gate approval.  
9. Row honesty — after scoped isolation, Multi-experiment stays **in progress** / Remaining `WorkSpace` only; never Complete / Primary next.  
10. Peers — never reopen Medium/Early or archived Multi-experiment peers as sources.

### Illustrative destinations (hints only — re-confirmed free this probe)

| From | Illustrative To (Cycle 10 draft) | Cycle 14 free? |
| --- | --- | --- |
| `…\_backups` | `C:\Project\archive\hygiene\2026.09.10 - WorkSpace-_backups` | Yes (absent); prefer **re-date** e.g. `2026.09.11 - WorkSpace-_backups` for honesty |
| `…\_quarantine` | `C:\Project\archive\hygiene\2026.09.10 - WorkSpace-_quarantine` | Yes (absent); prefer `2026.09.11 - WorkSpace-_quarantine` |

Create `C:\Project\archive\hygiene\` as needed (taxonomy already uses `hygiene` status vocabulary). Dest parent under `archive\` fits isolation-out-of-live-tree without claiming whole WorkSpace archived.

### What NOT to do

- Whole-tree WorkSpace archive/move  
- Move or “fix” live primary roots `#1–#5`  
- Remote URL rewrite / history rewrite / force-push / `filter-repo`  
- Delete backup/quarantine by default  
- Cherry-pick only nested hermes folders or empty `.git` shells  
- Mark Multi-experiment Complete or jump Primary next while WorkSpace remains  
- Re-propose archived peers / reopen Medium  
- Execute moves in STAGE 1 (phases 1–3 only)

---

## Clearance status

| Scope | Status |
| --- | --- |
| Whole-tree WorkSpace archive | **NO** — classified ≠ cleared (multi-remote live hermes remains after isolation) |
| Scoped Appendix A isolation (`_backups` + `_quarantine` parents) | **Research-supported for Continuity B plan draft**; execute only after **separate Hermes plan gate** |
| Live hermes multi-remote clearance | **NO** even after successful isolation |

---

## Prior art paths (must-read for planner)

- `program/git-strategy-workspace-hazards.md` — primary rules + fate  
- `sessions/2026.09.10-0907/03-plan/plan.md` — Appendix A illustrative from→to  
- `sessions/2026.09.10-1630/02-research/` — Cycle 13 baseline (no material delta then; this cycle re-probed for execute map)  
- `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/must-preserve.md`  
- `program/ROADMAP.md` — Multi-experiment Remaining WorkSpace only  

---

## Delta vs Cycles 10–13

**No material structural delta** (still 7 roots; parents still under WorkSpace; sizes same band; remotes/HEAD class unchanged; Appendix A dests still free).  
**Process delta:** Continuity **B** — research outcome is **fs_mutation move-map evidence**, not another docs_only re-attest theater.
