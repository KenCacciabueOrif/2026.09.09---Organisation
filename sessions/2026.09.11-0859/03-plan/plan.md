# Plan — Cycle 15 STAGE 1: live hermes multi-remote (Option A)

**Session:** `sessions/2026.09.11-0859/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md`, `02-research/codebase-findings.md`  
**Strategy artifact:** `program/git-strategy-workspace-hazards.md`  
**Continuity locks:** Q1=B · Q2=A (taxonomy/must-preserve re-litigation waived) · Q3=A (TNA dirty deferred)

---

## Goal

Clear the last named **live hermes multi-remote** hazard under Multi-experiment **`WorkSpace` only** by a **narrow remote-config** mutation on the live hermes clone only: remove the wrong-target remote name **`cada`** (HTTPS → `KenCacciabueOrif/TestNewWorkspaceAgent`) while leaving **`origin`** (`NousResearch/hermes-agent`) untouched. No corpus path moves. After a future gated execute, honesty-update strategy + INDEX/ROADMAP notes; WorkSpace stays at root and Multi-experiment stays **in progress / Remaining WorkSpace only**.

**STAGE 1 note:** Orchestrator **stops after this plan** for the **Hermes plan gate**. Continuity ≠ execute. Do **not** assume implement / audit / self-improve in this run. STAGE 2 resumes the **same session** only after Hermes **yes** (+ any amendments).

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`fs_mutation`** |
| Mutation kind | **remote-config** (live hermes `.git` remotes / `refs/remotes/cada/*` only) |
| Corpus path moves | **Zero** — no `Move-Item` / rename / delete of WorkSpace, primaries #1–#5, or any catalogue path |
| User approval before implementer | **Required** (Hermes plan gate) — even though there are no path moves |
| Taxonomy / must-preserve first-move gates | **Waived re-litigation (Q2=A)** — do **not** fail-closed on taxonomy final sign-off or must-preserve draft review this cycle; carry **proposed-ratified — ready for user sign-off** and **draft — not auto-locked** |
| Batch / map approval | **This plan’s remote-config map** must be Hermes-approved before implementer |

`fs_mutation` for gate purposes: corpus/git-config mutation under WorkSpace (remote remove on a live nested `.git`), not `docs_only` re-attest.

---

## What the user is approving (intent-preview — Hermes plan gate)

**Plain language:** Research found that the nested clone `hermes-agent` has two remotes. `origin` correctly points at the real hermes upstream. `cada` points at the **wrong** GitHub repo (the parent TestNewWorkspaceAgent project), is unused by any local branch, and is the multi-remote hazard still listed after Appendix A. Saying **yes** authorizes the implementer (STAGE 2, same session) to run **one** command that deletes only that wrong remote name from that clone’s git config — nothing is moved on disk, and the correct upstream stays.

### Exact scope (path + commands)

| Item | Value |
| --- | --- |
| Clone cwd | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` |
| Git binary (prefer) | `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| Approved command | `git remote remove cada` |
| Forbidden siblings | `git remote remove origin`; any `set-url`; force-push; history rewrite; path moves |

**Exact path map (remote-config — not FS moves):**

| Action | Target | Notes |
| --- | --- | --- |
| REMOVE remote name `cada` | Live hermes only (path above) | URL today: `https://github.com/KenCacciabueOrif/TestNewWorkspaceAgent.git` |
| KEEP remote `origin` | Same clone | URL: `https://github.com/NousResearch/hermes-agent.git` — **no** `set-url`, **no** remove |
| Path moves | **None** | Primaries #1–#5 stay; WorkSpace stays at `C:\Project\WorkSpace` |
| Archive parents | **Out of map** | `_backups` / `_quarantine` already under `C:\Project\archive\hygiene\2026.09.11…` — verify-only; do not re-propose |
| Archived hygiene hermes remotes | **Out of map** | Do not mutate archive clones’ remotes this cycle |

### What “yes” commits to

- STAGE 2 implementer may run the approved command after preflight re-check.
- Post-success: honesty edits to `program/git-strategy-workspace-hazards.md`, `catalogue/INDEX.md`, and `program/ROADMAP.md` Notes (live multi-remote cleared; nested still 5; row still WorkSpace only / not Complete).
- Does **not** authorize whole-tree archive, Multi-experiment Complete, Primary next, Special git, primary moves, or TNA dirty hygiene.

### What “no / edit” means

- No remote remove; no honesty claim that the hazard is cleared; plan revised or fail-closed with concrete blocker — **not** another `docs_only` re-attest theater cycle.

### Pros / cons (tradeoffs)

| Pros | Cons |
| --- | --- |
| Clears the last named live multi-remote hazard with evidence (wrong-repo, 0 branch tracks) | Loses local convenience refs under `refs/remotes/cada/*` (3 tips on the **wrong** repo) |
| Official Git behavior; no XL path move; reversible (re-add URL below) | Does **not** clear whole-tree / other program gates — Multi-experiment stays in progress |
| Keeps correct `origin`; no force-push / history rewrite | If some undocumented workflow still needed `cada` fetch bookmarks, user must re-add after undo |
| Narrowest Continuity Q1=B scope | Hermes gate is mandatory — Continuity choose ≠ execute |

---

## Explicit forbids (this cycle — implementer must refuse)

- Whole-tree WorkSpace archive or move.
- Moving live primaries **#1–#5** (including hermes-agent path relocation).
- Re-proposing `_backups` / `_quarantine` as move sources (they did **not** reappear under live WorkSpace).
- History rewrite / filter-repo / interactive rebase invent.
- Force-push to any remote.
- Nested `.git` integrity changes beyond the approved remote remove (no rewrite of `origin`; no packing invent; no delete of `.git`).
- `git remote remove origin` or any `set-url` on `origin` or `cada`.
- Marking Multi-experiment **Complete** or jumping Primary next / Special git while WorkSpace remains.
- Reopening archived Multi-experiment peers / Medium / Early as move sources.
- Mutating archived hygiene hermes remotes as part of this map.
- Substituting `docs_only` re-attest for this gated execute.

---

## Acceptance criteria

- [ ] Preflight (STAGE 2): from hermes cwd, `git remote -v` still shows `origin` + `cada` with research URLs; `git branch -vv` shows **no** local branch tracking `cada/*`; abort if a branch now tracks `cada` or if `cada` already absent (log + stop — no invent).
- [ ] After `git remote remove cada`: `git remote -v` shows **only** `origin` → `https://github.com/NousResearch/hermes-agent.git` (fetch+push).
- [ ] `main` still tracks `origin/main` (`git branch -vv`).
- [ ] Nested `.git` count under live WorkSpace remains **5** (probe method logged: recursive discovery and/or prior INDEX cross-check).
- [ ] **Zero** corpus path moves: `Test-Path` / equivalent confirms WorkSpace still `C:\Project\WorkSpace`; primaries #1–#5 paths unchanged; live `_backups`/`_quarantine` still absent.
- [ ] Honesty docs updated **after** successful remove only: `program/git-strategy-workspace-hazards.md` (live multi-remote cleared via Option A; cite this session); `catalogue/INDEX.md` (WorkSpace row — multi-remote note + nested 5); `program/ROADMAP.md` Notes (Remaining WorkSpace only; **not** Complete; **not** Primary next).
- [ ] WorkSpace remains at root; Multi-experiment **not** Complete.
- [ ] No force-push, no history rewrite, no `origin` URL change; implementer log records GfW path used and probe methods.
- [ ] TNA / hermes dirty WT: disclose only if encountered; **NO_AUTO_COMMIT** parent (or hermes) dirt (Q3=A).
- [ ] Taxonomy remains **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked** (no false final claims).

---

## Ordered steps

### STAGE 1 (this run) — plan only

0. **Orchestrator plan gate** — Relay intent-preview above to Hermes; **STOP**. Do not launch implementer until **yes** (+ amendments). `ready_to_implement: yes` means the map is safe to execute **after** gate, not that STAGE 1 may continue.

### STAGE 2 (same session — only after Hermes yes)

1. **Preflight re-inventory (live hermes only)**  
   - **Paths:** `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent`  
   - **Action:** Prefer GfW `git.exe`; `git remote -v`; `git branch -vv`; confirm no branch tracks `cada`; confirm `origin` URL unchanged. Optional: quick `Test-Path` WorkSpace + live `_backups`/`_quarantine` absent.  
   - **Verify:** Remotes still match research; if `cada` already gone → log “already clear,” skip remove, still do honesty if needed; if a branch tracks `cada` → **abort** (concrete blocker — needs Continuity amendment).  
   - **Disclose:** hermes dirty WT presence only (Q3=A — no hygiene).

2. **Execute Option A**  
   - **Paths:** hermes cwd above.  
   - **Action:** `git remote remove cada` only (exact remote name).  
   - **Verify:** `git remote -v` → sole `origin`; `git branch -vv` → `main` → `origin/main`.

3. **Integrity / count attestation**  
   - **Paths:** live `C:\Project\WorkSpace` nested `.git` roots.  
   - **Action:** Re-count nested roots (expect **5**); confirm no path moves of primaries.  
   - **Verify:** nested_git_count_live = 5; WorkSpace still at root; log probe method.

4. **Honesty — strategy artifact**  
   - **Paths:** `program/git-strategy-workspace-hazards.md`  
   - **Action:** Record Cycle 15 Option A: live hermes multi-remote cleared (`cada` removed); `origin` kept; nested still 5; Appendix A unchanged; whole-tree still OOS; Multi-experiment still WorkSpace only. Cite `sessions/2026.09.11-0859/`. Do not rewrite entire strategy from scratch — amend clearance status.  
   - **Verify:** Doc no longer claims live multi-remote uncleared; does not claim Complete / whole-tree clear.

5. **Honesty — INDEX**  
   - **Paths:** `catalogue/INDEX.md` (WorkSpace row)  
   - **Action:** Update live multi-remote / remotes note to reflect sole `origin` on hermes; keep path at root; nested **5**.  
   - **Verify:** No stale “origin+cada on live hermes”; no archive of WorkSpace claimed.

6. **Honesty — ROADMAP**  
   - **Paths:** `program/ROADMAP.md`  
   - **Action:** Notes: live hermes multi-remote hazard cleared (remote-config); **Remaining: WorkSpace only**; status stays **in progress** — **never** Complete / Primary next / Special git.  
   - **Verify:** Row not Complete; Primary next unchanged while WorkSpace remains.

7. **Implementer log**  
   - **Paths:** `sessions/2026.09.11-0859/04-implement/` (or session convention)  
   - **Action:** Log commands, before/after `remote -v`, nested count, probe methods, reverse notes applied if any undo, NO_AUTO_COMMIT attestation.  
   - **Verify:** Auditor can grep AC without re-running unsafe invent.

---

## Non-goals

- Same-run implement / audit / self-improve before Hermes yes (STAGE 1).
- TNA dirty-tree hygiene (Q3=A).
- Taxonomy / must-preserve final sign-off litigation (Q2=A waived).
- Whole-tree WorkSpace clearance / Multi-experiment Complete / Special git.
- Option B (relocate / worktree isolation of hermes primary) — hard-forbidden.
- Option C (`set-url` invent / keep wrong-repo remote).
- Changing `origin` URL; mutating archive hygiene remotes.
- Org-repo publish/pull (dual auth N/A).
- docs_only re-attest as the cycle outcome.

---

## Reverse / undo notes (remote remove)

If `cada` must be restored after remove (same URL as research evidence):

```text
cd /d C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent
"C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe" remote add cada https://github.com/KenCacciabueOrif/TestNewWorkspaceAgent.git
```

Optional: `git fetch cada` to rebuild `refs/remotes/cada/*` (not required for undo of config).  
**Does not** restore Multi-experiment hazard-cleared honesty claims — if undo, revert strategy/INDEX notes accordingly.  
Removing `cada` deletes remote-tracking refs under that name only; it does not delete local commits or change `origin`.

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Accidental `remote remove origin` | Steps name **`cada` only**; preflight lists remotes; abort on wrong name |
| Scope creep to path-move hermes / whole WorkSpace | Explicit forbids; AC zero path moves |
| Claiming Multi-experiment Complete after remove | ROADMAP step forbids Complete / Primary next |
| Branch starts tracking `cada` before execute | Preflight abort → Continuity amendment (not silent set-url) |
| Hermes dirty WT / parent TNA dirt | Disclose only; **NO_AUTO_COMMIT** (Q3=A) |
| Misread reachable `cada` as “must keep” | Evidence: wrong-target, unrelated histories, 0 tracks |
| Gate refused | Fail-closed: blocker = Hermes withheld approval; minimal unblock = Hermes yes on Option A (or documented hermes-related URL + explicit Continuity for `set-url`) — **not** docs_only theater |

---

## Ready to implement

**yes** — Option A is clear, evidence-backed, and safe under forbids (remote-config only; `origin` untouched; zero path moves).

**Orchestrator:** still **STOP** at Hermes plan gate (STAGE 1). Do not launch implementer until user **yes**.

---

## Blocking questions

**none** for plan quality / safety under Continuity locks.

Gate remaining (expected STAGE 1 process block, not a planner unknown):

- Hermes plan-gate approval of Option A intent-preview (Continuity ≠ yes).

---

## Fail-closed alternative (if gate refuses)

| Item | Detail |
| --- | --- |
| Concrete blocker | Hermes withheld approval to remove `cada` despite wrong-repo evidence |
| Minimal gated unblock | Hermes **yes** on this Option A map **or** user supplies a **documented** hermes-related URL + explicit Continuity for a narrow `set-url` plan (still `fs_mutation`, still gated) |
| Forbidden substitute | Cycles 10–13-style `docs_only` re-attest theater |

---

## Planner return fields (orchestrator)

| Field | Value |
| --- | --- |
| plan_path | `sessions/2026.09.11-0859/03-plan/plan.md` |
| mutation_class | `fs_mutation` (remote-config; zero corpus path moves) |
| ready_to_implement | **yes** (post-gate only) |
| recommended_action | Gated `git remote remove cada` on live hermes; keep `origin`; no path moves |
| STAGE 1 must stop | **yes** — fs_mutation Hermes plan gate |
