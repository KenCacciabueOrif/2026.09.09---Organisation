# Plan — Cycle 14 Multi-experiment (`WorkSpace` only / Continuity B Appendix A)

**Session:** `sessions/2026.09.11/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `01-prompt-betterment/notes.md`, `02-research/research-brief.md`, `codebase-findings.md`, `online-findings.md`  
**Primary rules:** `program/git-strategy-workspace-hazards.md` (safe relocation rules 1–10 + Appendix A / recommended fate)  
**Approach:** Research **Option A** — Continuity **B** scoped isolation: relocate intact `_backups` and `_quarantine` parent trees out of live `C:\Project\WorkSpace`. **Mutation class `fs_mutation`.**

---

## Goal

Execute (only after a **separate Hermes plan-gate yes**) Continuity **B** / Appendix A isolation for ROADMAP row **Multi-experiment / Remaining `WorkSpace` only**: move the whole parent trees `TestNewWorkspaceAgent\_backups` and `TestNewWorkspaceAgent\_quarantine` intact to dated leaves under `C:\Project\archive\hygiene\`, shrinking the live XL tree by ~3.3 GB and nested `.git` count **7→5**, without archiving or moving the whole WorkSpace tree, without touching live primary roots `#1–#5`, without remote or history rewrite, and without marking Multi-experiment Complete. Continuity B authorizes drafting this map only — **Continuity ≠ execute**. STAGE 1 stops at the human plan gate in Hermes even if this plan is complete.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`fs_mutation`** |
| Batch | Continuity **B** / Appendix A scoped isolation — named parents `_backups` + `_quarantine` only |
| Corpus FS | **Two** intentional whole-parent moves (after plan-gate yes); create `C:\Project\archive\hygiene\` if missing |
| Org-repo disk writes | Honesty: `catalogue/INDEX.md`, `catalogue/inventory.md` (as needed), `program/ROADMAP.md` Notes; optional honesty touch to `program/git-strategy-workspace-hazards.md`; session logs under `sessions/2026.09.11/` |
| User approval before implementer | **Mandatory** — plan gate **human-held in Hermes**; orchestrator STAGE 1 **STOPS** here even when `ready_to_implement: yes` |
| First-move / Early-simple gates | Taxonomy **proposed-ratified** / must-preserve **draft** — **Q3=A waived** re-litigation this cycle (Continuity carry); **this batch’s path map** still requires plan-gate yes |
| Push / remote publish | **Not required** — dual auth/preflight **N/A** |

### Continuity B scoped isolation?

**Yes** — this plan’s execute map is only `_backups` + `_quarantine` out of live WorkSpace. It is **not** docs_only re-attest, **not** whole-tree archive, **not** live-primary moves.

### Orchestrator note (plan gate — STAGE 1)

- **`ready_to_implement: yes`** means the Appendix A map is complete and evidence-backed.
- Orchestrator **must not** launch implementer in STAGE 1.
- Plan gate remains **human-held in Hermes chat**.
- Continuity / Choose **≠** plan-gate approval.
- If the user rejects or the plan drifts off Continuity B scoped isolation → **stop**; do not auto-continue as docs_only or whole-tree.

---

## What the user is approving

**Plain language:** Saying **yes** at the Hermes plan gate authorizes the implementer to **physically relocate** two labeled folders (`_backups` and `_quarantine`) out of the live WorkSpace tree into dated hygiene archive folders. Saying **no** (or not answering) means **nothing moves** — Continuity B only drafted this map.

**What “yes” commits to**

- Create `C:\Project\archive\hygiene\` if it does not exist.
- Move each **whole parent tree** intact (including nested hermes-agent clone `.git` directories and opaque `.env*` files as unread payload).
- Update catalogue/ROADMAP honesty so WorkSpace stays at root, nested count becomes **5**, Multi-experiment stays **in progress** / Remaining **WorkSpace only**.
- Accept expected **dirty working tree** on parent repo `TestNewWorkspaceAgent` (tracked paths under those folders will look deleted) — **no auto-commit** of that dirt this cycle.

**What “yes” does *not* authorize**

- Moving or archiving all of `C:\Project\WorkSpace`.
- Moving live primary nested roots `#1–#5`.
- Rewriting remotes (`origin` / `cada`), rewriting history, force-push, or `filter-repo`.
- Deleting `_backups` / `_quarantine` instead of relocating.
- Marking Multi-experiment **Complete** or jumping Primary next / Special git.
- Clearing the live hermes multi-remote hazard (isolation does not clear it).

### Exact path map (from → to)

Evidence: live re-probe 2026-09-11 (`02-research/`); destinations **absent / free**; sources **present** under WorkSpace.

| Unit | From (live source) | To (dated hygiene leaf) | Size band (cheap) |
| --- | --- | --- | --- |
| Backups parent | `C:\Project\WorkSpace\TestNewWorkspaceAgent\_backups` | `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_backups` | ~1662 MB |
| Quarantine parent | `C:\Project\WorkSpace\TestNewWorkspaceAgent\_quarantine` | `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_quarantine` | ~1662 MB |

**Parent create (if missing):** `C:\Project\archive\hygiene\`  
**Expect after both moves:** nested `.git` under WorkSpace **7→5**; ~**3.3 GB** out of live tree.

**Nested `.git` that move with parents (atomic intact):**

| # | Nested root (under source parent) | Disposition |
| --- | --- | --- |
| 6 | `…\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent` | Moves with `_backups` |
| 7 | `…\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent` | Moves with `_quarantine` |

**Keep in place (do not move):**

| # | Path class |
| --- | --- |
| 1–5 | Live primaries: `OS-IA`, `TestNewWorkspaceAgent`, live `hermes-agent`, `orchestrateur`, `WorkshopOrif` |
| Whole | `C:\Project\WorkSpace` remains at INDEX root |

**Remotes (document only — no rewrite):** backup + quarantine hermes clones keep `origin` + `cada` (HTTPS) unchanged after path move.

### Opaque `.env*` moving with parents (path presence only — contents unread)

Relative to `C:\Project\WorkSpace\` (Cycle 10 catalogue + Cycle 14 research count **5+5**; never open/quote/log contents):

**Under `_backups` (move with parent):**

1. `TestNewWorkspaceAgent\_backups\.env.20260710-110530.bak`
2. `TestNewWorkspaceAgent\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent\.env.example`
3. `TestNewWorkspaceAgent\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent\.envrc`
4. `TestNewWorkspaceAgent\_backups\2026-07-02_pre-cleanup\hermes-vscode\backups_20260630\.env.20260630_094235`
5. `TestNewWorkspaceAgent\_backups\2026-07-02_pre-cleanup\hermes-vscode\backups_20260630\dot_hermes\.env.20260630_094235`

**Under `_quarantine` (move with parent):**

6. `TestNewWorkspaceAgent\_quarantine\stale-backups-hermes-home\.env.bak_20260630`
7. `TestNewWorkspaceAgent\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent\.env.example`
8. `TestNewWorkspaceAgent\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent\.envrc`
9. `TestNewWorkspaceAgent\_quarantine\vscode-extension-artifacts\hermes-vscode\backups_20260630\.env.20260630_094235`
10. `TestNewWorkspaceAgent\_quarantine\vscode-extension-artifacts\hermes-vscode\backups_20260630\dot_hermes\.env.20260630_094235`

Any additional `.env*` discovered under those parents at execute time moves as opaque payload with the parent (path presence only; do not read). **~7** opaque paths remain under live WorkSpace (live hermes + project roots) — untouched.

### Parent-repo (TNA) dirty WT coupling (disclose)

`TestNewWorkspaceAgent` tracks **~1157** paths under `_backups` and **~1150** under `_quarantine`. After successful moves, that parent working tree will show massive deletions vs its index. **Disclose and leave dirty** — **do not** auto-commit, amend, rewrite history, or force-push that dirt this cycle. Optional later hygiene Continuity only.

### Pros / cons (tradeoffs)

| Pros | Cons |
| --- | --- |
| Removes unexpected clone roots from the live XL tree | Real FS risk (~1.6 GB × 2 Windows moves; locks possible) |
| Shrinks live WorkSpace by ~3.3 GB | Bookmarks / absolute paths under old locations break |
| Matches preferred fate in strategy artifact | Parent TNA index becomes dirty (no auto-commit) |
| Leaves live primaries and whole WorkSpace in place | Live hermes multi-remote **not** cleared |
| Progress beyond Cycles 10–13 docs_only re-attest | Row stays in progress — not “WorkSpace solved” |

---

## Safe relocation rules (cite — must follow)

From `program/git-strategy-workspace-hazards.md`:

1. **Atomic nested git** — move intact trees that contain `.git`; never strip history / `filter-repo` / force-push.  
2. **Named parent units only** — whole `_backups` and `_quarantine`; do not cherry-pick empty `.git` shells.  
3. **Opaque `.env*`** — path presence only; never read/quote/log contents.  
4. **Remotes path-only** — inventory only; no `git remote set-url` / origin rewrite.  
5. **No linked-worktree surprise** — re-run `worktree list` immediately before move on the **nested hermes-agent clone paths** (not the `_backups`/`_quarantine` parents — parents resolve to TNA); unexpected >1 → fail-closed. (**Hermes gate amendment 2026-09-11.**)  
6. **Windows lock recovery** — prefer single `Move-Item` (or equivalent); on PermissionDenied/split → reunify + `robocopy /E /MOVE`; remove **only empty** leftover `.git` shells; re-attest; log deviation.  
7. **Whole XL WorkSpace → ordinary archive** — **OUT OF SCOPE**.  
8. **Consent** — Continuity ≠ plan-gate; this plan needs Hermes **yes** before execute.  
9. **Row honesty** — after isolation, Multi-experiment stays **in progress** / Remaining **`WorkSpace` only**; never Complete / Primary next.  
10. **Peers** — never reopen Medium / Early or archived `PWAExemple` / `GitTest` / `WorkStationPWA` as sources.

---

## Explicit move map (this cycle)

| Folder | Disposition |
| --- | --- |
| `…\TestNewWorkspaceAgent\_backups` | **Move** → `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_backups` |
| `…\TestNewWorkspaceAgent\_quarantine` | **Move** → `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_quarantine` |
| `C:\Project\WorkSpace` (whole tree) | **Remain at root** — never archive this cycle |
| Live primary nested roots `#1–#5` | **Keep in place** |
| `PWAExemple`, `GitTest`, `WorkStationPWA` | Verify-only at archive — **never re-propose** as sources |
| Medium / Early | Verify-only — **never reopen** |

---

## Fail-closed conditions (abort move; session `blocked` or stop execute)

Abort **before or during** moves if any of:

1. Destination leaf **already exists** (non-empty collision).  
2. Source parent **missing** at expected path.  
3. Linked worktree probe shows unexpected **>1** on in-scope hermes trees.  
4. Nested `.git` **split unrecovered** after PermissionDenied (cannot reunify + robocopy cleanly; non-empty leftover `.git` would need delete — **forbidden**).  
5. Scope creep pressure toward whole-tree WorkSpace or live primaries `#1–#5`.  
6. Any instruction to rewrite remotes / history / force-push.

On abort: do not claim isolation complete; leave ROADMAP honesty accurate; still allow self-improver at cycle end.

---

## Acceptance criteria

- [ ] Mutation class is **`fs_mutation`**; Continuity **B** / Appendix A scope only (`_backups` + `_quarantine` parents).
- [ ] Hermes plan-gate **yes** recorded before any corpus move (STAGE 1 may end with gate pending — then implementer AC apply only post-gate).
- [ ] Both parents moved intact to the exact dated hygiene destinations (or fail-closed with no partial claim of success).
- [ ] Nested `.git` count under WorkSpace **7→5** after both moves (probe method logged: `Test-Path` and/or Read/Glob / recursive `.git` discovery).
- [ ] Live primaries `#1–#5` and whole `C:\Project\WorkSpace` still at prior paths.
- [ ] Remotes on moved clones unchanged (`git remote -v` inventory only — no `set-url`).
- [ ] No history rewrite / force-push / `filter-repo`; no `.env*` contents read or logged.
- [ ] Windows lock recovery (if used) logged as allowed deviation; only empty leftover `.git` shells removed.
- [ ] Parent TNA dirty WT disclosed in implementer log; **not** auto-committed.
- [ ] `catalogue/INDEX.md` honesty: WorkSpace still at `C:\Project\WorkSpace`; note hygiene isolation destinations for `_backups`/`_quarantine`; do **not** claim WorkSpace archived.
- [ ] `program/ROADMAP.md` Multi-experiment Notes: Cycle 14 Appendix A executed (or blocked); **Remaining: `WorkSpace` only**; nested root note **7→5** if both moved; status **in progress / not Complete**; no Primary-next jump.
- [ ] Taxonomy language remains **proposed-ratified — ready for user sign-off** (not final); must-preserve remains **draft — not auto-locked / for user review**; Q3=A waiver documented.
- [ ] Medium / Early / archived Multi-experiment peers **not** reopened as move sources.
- [ ] Implementer log records **probe method** for every path attestation (`Test-Path` **or** Read/Glob equivalent).
- [ ] Auditor can verify AC from session artifacts without chat history.

**Not hard AC (include when cheap):** absolute MB re-measure; inventory one-line size refresh.

---

## Steps

1. **Confirm plan-gate clearance (orchestrator/implementer gate)** — paths: this `plan.md`; Hermes chat approval — action: proceed only if user **explicitly approved** this path map; if STAGE 1 / gate pending, **stop** (no moves) — verify: written yes in session notes or handoff; Continuity alone insufficient.

2. **Pre-flight presence + free destinations** — paths: both sources; `C:\Project\archive\hygiene\`; both dated destination leaves; live `C:\Project\WorkSpace` — action: attest with `Test-Path` **or** Read/Glob; create hygiene parent if absent; **fail-closed** if sources missing or dest leaves exist — verify: sources True; dest leaves False; log probe method.

3. **Re-probe linked worktrees (rule 5)** — **Hermes gate amendment (2026-09-11):** probing `_backups` / `_quarantine` **parent** dirs resolves to the TNA repo — always run `git worktree list` on the **NESTED CLONE paths explicitly**:
   - `…\_backups\2026-07-02_pre-cleanup\hermes-extension-pack\hermes-agent`
   - `…\_quarantine\vscode-extension-artifacts\hermes-extension-pack\hermes-agent`
   (as done in the gate audit). Do **not** treat parent-dir `worktree list` as the nested-clone probe. Unexpected >1 on those nested paths → fail-closed — verify: single main worktree each (or abort).

4. **Inventory remotes pre-move (rule 4)** — paths: nested hermes under `_backups` and `_quarantine` — action: `git remote -v` read-only; record names/schemes — verify: no `set-url` commands run.

5. **Move `_backups` parent (atomic)** — from→to per map — action: prefer `Move-Item` (or equivalent) of **whole parent**; on PermissionDenied/split → reunify + `robocopy /E /MOVE` (rule 6); remove **only empty** leftover `.git` shells; re-attest — verify: source absent under WorkSpace; dest present; nested `.git` intact under dest; log any robocopy deviation.

6. **Move `_quarantine` parent (atomic)** — same as Step 5 for quarantine map row — verify: same attestation pattern; nested count under WorkSpace now **5**.

7. **Post-move remote + path attestation** — paths: both dest nested hermes; WorkSpace nested count; live primaries — action: `remote -v` unchanged; `Test-Path`/Glob for sources False / dests True / primaries True; opaque `.env*` presence under dests only (no content read) — verify: remotes identical to pre-move inventory; probe method logged.

8. **Disclose parent TNA dirty WT** — path: `C:\Project\WorkSpace\TestNewWorkspaceAgent` — action: note expected deletions in implementer log; **do not** commit / rewrite — verify: log states dirty coupling + no auto-commit.

9. **Update INDEX honesty** — path: `catalogue/INDEX.md` — action: keep WorkSpace current path at root; note Cycle 14 Appendix A isolation destinations under `archive\hygiene\`; nested honesty **5** (or “7→5”); hazards / live multi-remote still uncleared; taxonomy/must-preserve wording unchanged (proposed-ratified / draft) — verify: no claim WorkSpace archived; no Complete.

10. **Update ROADMAP Notes** — path: `program/ROADMAP.md` (Multi-experiment row) — action: Cycle 14 session `2026.09.11` Continuity B Appendix A executed (or blocked); **Remaining: `WorkSpace` only**; nested **7→5** if both moved; **in progress / not Complete**; do **not** jump Primary next / Special git — verify: row not Complete; peers not reopened.

11. **Optional inventory / strategy honesty** — paths: `catalogue/inventory.md`; optionally short Cycle 14 note on `program/git-strategy-workspace-hazards.md` that Appendix A was executed under Continuity B (without rewriting whole strategy) — verify: nested count honesty; clearance for whole-tree still **NO**.

12. **Session implementation artifacts** — paths: `sessions/2026.09.11/04-implementation/log.md`, `changes.md` — action: record from→to, probe methods, remotes unchanged, lock-recovery deviation if any, TNA dirty disclosure, opaque unread, fail-closed outcomes if any — verify: auditor-usable trail.

13. **Self-check before handoff** — action: scan for accidental Complete / Primary-next / whole-tree archive language / remote rewrite / `.env` content — verify: Remaining WorkSpace only; isolation scoped.

**Skipped (explicit):** Auth/preflight for push/pull — **N/A**. Org-repo publish/pull — **N/A**. Whole-tree WorkSpace move — **forbidden**. Live primary moves — **forbidden**. Docs_only re-attest as cycle path — **forbidden**.

---

## Non-goals

- Docs_only Continuity A / Cycles 10–13-style re-attest theater as this cycle’s outcome  
- Whole-tree archive or move of `C:\Project\WorkSpace`  
- Moving or “fixing” live primary nested roots `#1–#5`  
- Marking Multi-experiment **Complete** or jumping Primary next / Special git  
- Reopening Medium / Early or archived Multi-experiment peers as sources  
- Remote URL rewrite, history rewrite, force-push, `filter-repo`, deleting backup/quarantine by default  
- Auto-committing parent TNA dirty WT  
- Clearing live hermes multi-remote via this isolation  
- Taxonomy final sign-off or must-preserve final lock (Q3=A waived re-litigation only)  
- Treating Continuity B as plan-gate execute approval  
- Agent PATH / credential chores as Continuity requirements  
- Publish/pull of org-repo this cycle  

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Windows lock / split nested `.git` | Rule 6: reunify + robocopy `/E /MOVE`; never delete non-empty `.git`; fail-closed if unrecovered |
| Partial move (one parent only) | Prefer both; if abort mid-batch, honesty must state which moved; do not claim 7→5 unless both done |
| Dest collision | Pre-flight fail-closed if dest exists |
| Scope creep to whole-tree / primaries | Hard AC + empty map for those paths |
| Silent remote / history rewrite | Steps forbid; auditor checks log for mutate commands |
| Framing isolation as row Complete / multi-remote cleared | ROADMAP/INDEX AC forbid |
| Secrets leak | Opaque path presence only |
| Parent TNA auto-commit | Explicit non-goal + Step 8 |
| Bookmarks break | Disclosed in pros/cons |

**Rollback (best effort):** if a move fails mid-flight, prefer reunify to restore a consistent tree; do not invent new destinations. Full undo = move parents back to original paths only if dests are complete and sources empty — only under explicit recovery Continuity; default fail-closed stops further mutation.

---

## Taxonomy / must-preserve (wording lock)

- Taxonomy: **proposed-ratified — ready for user sign-off** (not final).  
- Must-preserve: **draft — not auto-locked / for user review**.  
- **Q3=A:** waive re-litigation this cycle (Continuity carry) — does **not** convert either to final/locked.

---

## Ready to implement

**yes** — Appendix A from→to map is complete and evidence-backed (sources present; destinations free; rules cited).  

**Orchestrator STAGE 1:** still **STOP at plan gate** (Hermes). Do **not** launch implementer until human yes.

## Blocking questions

**none** (path map locked from research; Continuity B + Q2/Q3 already answered). Plan-gate approval is a **consent hold**, not a planner blocking question.

---

## Plan result (for orchestrator)

- **plan_path:** `sessions/2026.09.11/03-plan/plan.md`
- **ready_to_implement:** yes
- **mutation_class:** `fs_mutation`
- **continuity_b_scoped_isolation:** yes
- **plan_gate_needed:** yes (Hermes human-held; STAGE 1 stop)
- **blocking_questions:** none
- **step_count:** 13
- **one-line summary:** Continuity B `fs_mutation`: move intact `_backups` + `_quarantine` to dated `archive\hygiene\` leaves; keep WorkSpace/live primaries; row stays in progress.
