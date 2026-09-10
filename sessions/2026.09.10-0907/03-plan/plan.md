# Plan — Cycle 10 Multi-experiment (`WorkSpace` only + hazard remediation docs)

**Session:** `sessions/2026.09.10-0907/03-plan/`  
**Inputs:** `01-prompt-betterment/refined-prompt.md`, `02-research/research-brief.md` (+ findings)  
**Approach:** Research **Option A** (Continuity **Q2=A** docs-first) — durable **git-strategy / WorkSpace hazard remediation** artifact + INDEX/ROADMAP honesty. **Mutation class `docs_only`.** Zero corpus moves this cycle. Whole-tree archive **OUT OF SCOPE**. Multi-experiment stays **in progress** with **Remaining: `WorkSpace` only**. Optional scoped `_backups` / `_quarantine` isolation map is an **appendix draft only** (not executed; not this cycle’s mutation class).

---

## Goal

Close Continuity **Q1=A / Q2=A** for the orchestrator-locked ROADMAP row **Multi-experiment / `WorkSpace` only** by **solving via documentation**: write a durable remediation artifact that classifies live hazards (5 primary + 2 backup/quarantine nested roots; multi-remote `origin`+`cada` on live and clone hermes-agent; XL; opaque `.env*` path presence; must-preserve draft Medium caution), records recommended fate of `_backups` / `_quarantine` (isolate preferred / keep / defer — never delete by default), and encodes **safe relocation / isolation rules** for a **future plan-gated** cycle. Refresh INDEX/ROADMAP honesty for Cycle 10. Leave `C:\Project\WorkSpace` at its root path with **zero** intentional corpus moves. Do **not** mark Multi-experiment Complete or jump Primary next while WorkSpace remains.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`docs_only`** |
| Corpus FS | **Zero** intentional corpus moves/renames/deletes — do not touch `C:\Project\WorkSpace`, `_backups`, `_quarantine`, or any other catalogue-backed folder path |
| Org-repo disk writes | Allowed: new durable artifact under `program/` (and optional short pointer in `catalogue/`); honesty edits to `program/ROADMAP.md`, `catalogue/INDEX.md`, `catalogue/inventory.md`; session logs under `sessions/2026.09.10-0907/` — all inside this organisation git root only |
| User approval before implementer | **Not required** (`docs_only`) — see orchestrator note |
| First-move / Early-simple gates | **N/A** — no executed `fs_mutation`; appendix map is non-binding draft |
| Push / remote publish | **Not required** — dual auth/preflight **N/A** |

### Orchestrator note (plan gate)

**No mandatory plan-gate pause** before implementer. Continuity Q2=A already locked docs-first remediation; there is **no** corpus path map to approve this cycle. Proceed to implementer on this plan as written.

If a **future** cycle wants to execute Appendix A (scoped `_backups` / `_quarantine` isolation), that cycle must set `mutation_class: fs_mutation`, include a full “What the user is approving” section, and wait for a **separate** plan-gate yes — Continuity / Choose from this cycle does **not** authorize that execute.

### Implementer attestation (zero corpus FS)

After docs steps, implementer must attest in the implementation log:

1. `Test-Path C:\Project\WorkSpace` → still **True** at root (unchanged location).
2. `Test-Path` on `…\TestNewWorkspaceAgent\_backups` and `…\_quarantine` → still **True** under WorkSpace (unchanged location).
3. No `Move-Item` / `robocopy` / rename targeting WorkSpace or any other corpus folder this cycle.
4. Dated whole-tree destinations `C:\Project\archive\2026.05.29 - WorkSpace` and paused/active equivalents remain **absent**.
5. No `.env` contents read or logged (opaque path mentions OK only as counts / relative paths already in research).
6. No `git remote set-url` / remote rewrite / history rewrite on any WorkSpace nested root.

---

## What the user is approving

**N/A — docs_only remediation attestation.** There is no corpus move map and no separate plan-gate ask this cycle.

Material user-facing changes are **org-repo documentation only** (durable hazard/remediation rules + INDEX/ROADMAP honesty). They do **not** relocate files on disk and do **not** claim Multi-experiment Complete or jump Primary next. Appendix A is informational for a future gated cycle only.

---

## Explicit move map (this cycle)

**None.** Empty by design (`docs_only`).

| Folder | Disposition this cycle |
| --- | --- |
| `C:\Project\WorkSpace` (whole tree) | **Remain at root** — document only; whole-tree archive OOS |
| `…\TestNewWorkspaceAgent\_backups` | **Remain** — classify + rules; isolation deferred to future plan gate |
| `…\TestNewWorkspaceAgent\_quarantine` | **Remain** — classify + rules; isolation deferred to future plan gate |
| Live primary nested roots `#1–#5` | **Keep in place** — document multi-remote on live hermes; no remote surgery |
| `PWAExemple`, `GitTest`, `WorkStationPWA` | Verify-only at archive paths — **never re-propose** as sources |
| Medium / Early archive & paused | Verify-only — **never reopen** as sources |

---

## Acceptance criteria

- [ ] Durable artifact exists (e.g. `program/git-strategy-workspace-hazards.md`) covering: hazard classification table; recommended fate of `_backups` / `_quarantine`; safe relocation / isolation rules (atomic nested git; opaque `.env*`; remotes path-only / no rewrite; no linked-worktree surprise; Windows lock recovery; consent; row honesty; peers); clear statement that whole-tree Multi-experiment archive is OOS until hazards cleared under a future gated strategy.
- [ ] Mutation class is **`docs_only`**; implementer log attests **zero** intentional corpus path moves (including no WorkSpace / `_backups` / `_quarantine` move).
- [ ] `C:\Project\WorkSpace` still exists at INDEX root path after implementation; `_backups` / `_quarantine` still under WorkSpace; dated whole-tree archive/paused targets remain absent.
- [ ] `program/ROADMAP.md` Multi-experiment Notes updated for **Cycle 10** (`sessions/2026.09.10-0907/`): hazard remediation **docs_only** pass + pointer to durable artifact; status remains **In progress**; **Remaining: `WorkSpace` only**; **not** Complete; **Primary next** does **not** jump to Special git while WorkSpace remains; “How the next cycle starts” points at remaining WorkSpace / optional future scoped isolation or further git-strategy — **not** soft-deferred force-finalize.
- [ ] `catalogue/INDEX.md` WorkSpace row stays at `C:\Project\WorkSpace` with Cycle 10 honesty (classified hazards + docs remediation pointer; still not moved); “What’s next” still shows Multi-experiment remaining `WorkSpace` only.
- [ ] `catalogue/inventory.md` WorkSpace notes refreshed for Cycle 10 docs remediation (nested **7** honesty retained; no invented move).
- [ ] Taxonomy language remains **proposed-ratified — ready for user sign-off** (not final); must-preserve remains **draft — not auto-locked / for user review**.
- [ ] Appendix A (scoped isolation draft) may be present in `plan.md` and/or referenced from the durable artifact as **non-executed / future plan-gate only** — implementer must **not** execute it.
- [ ] Medium / Early / archived Multi-experiment peers **not** reopened as move sources.
- [ ] No remote URL rewrite / history rewrite / `.env` content reads; no agent `git push` / `git pull` required.
- [ ] Auditor can verify all AC from session artifacts without chat history.

**Not hard AC (include when cheap):** absolute size MB bands already in research; optional one-line size refresh in inventory Notes.

---

## Steps

1. **Confirm research lock (read-only)** — paths: `02-research/research-brief.md`, `02-research/codebase-findings.md`, Continuity in `01-prompt-betterment/notes.md` / refined-prompt — action: restate Option A / Q2=A docs-first / empty execute map in implementation log header — verify: log cites mutation_class **`docs_only`**; hazards cleared for whole-tree = **NO**; Appendix A marked non-executed.

2. **Pre-flight presence (attest, do not move)** — paths: `C:\Project\WorkSpace`; `C:\Project\WorkSpace\TestNewWorkspaceAgent\_backups`; `C:\Project\WorkSpace\TestNewWorkspaceAgent\_quarantine`; archive peers `C:\Project\archive\2025.08.08 - GitTest`, `…\2025.07.01 - WorkStationPWA`, `…\2025.06.25 - PWAExemple` — action: `Test-Path` only — verify: WorkSpace + `_backups` + `_quarantine` **True** at current locations; peers **True** at archive; WorkSpace dated archive/paused targets **False**.

3. **Write durable remediation artifact** — path: **`program/git-strategy-workspace-hazards.md`** (create) — action: author a durable doc that includes at least:
   - Scope: Multi-experiment remaining `WorkSpace` only; Cycle 10 session pointer
   - Hazard classification (multi-remote live+clones; 5 primary / 2 clone; nested count **7**; XL; opaque `.env*` count unread; must-preserve **draft — not auto-locked**; linked worktrees none; HTTPS remotes `origin`/`cada` — no SSH rewrite applicable)
   - Recommended fate table (`_backups` / `_quarantine` → isolate preferred / keep / defer — do not delete by default; live primaries keep; whole-tree archive OOS)
   - Numbered **safe relocation / isolation rules** (from research-brief: atomic nested git; named parent units only; opaque `.env*`; remotes path-only; re-probe worktrees before any future move; Windows reunify + `robocopy /E /MOVE` on lock with empty-shell cleanup only; consent Continuity≠plan-gate; row honesty; peers closed)
   - Clear “how a future cycle proceeds” note: optional scoped isolation of named parents under **`fs_mutation` + plan gate**; live multi-remote remains after isolation; whole-tree archive still blocked until dedicated clearance
   - Pointer to research: `sessions/2026.09.10-0907/02-research/`
   - Taxonomy / must-preserve wording: **proposed-ratified — ready for user sign-off** / **draft — not auto-locked / for user review**
   — verify: file exists; no from→to execute instructions that imply implementer should move now; no Complete / Primary-next language.

4. **Update ROADMAP Notes** — path: `program/ROADMAP.md` (Multi-experiment row Notes + “How the next cycle starts” §2) — action: append Cycle 10 session `2026.09.10-0907` **docs_only hazard remediation** (classification + safe rules in `program/git-strategy-workspace-hazards.md`); keep **In progress (partial / nearly complete)**; **Remaining: `WorkSpace` only**; still fail-closed for whole-tree; optional future scoped isolation = separate plan gate; **not** Complete — verify: no “Complete”; no Primary-next jump that drops Multi-experiment while WorkSpace remains; no language treating Continuity Choose as move approval.

5. **Update INDEX honesty** — path: `catalogue/INDEX.md` (WorkSpace table row + “What’s next” item for Multi-experiment) — action: keep path `C:\Project\WorkSpace`; note Cycle 10 docs remediation + link/pointer to `program/git-strategy-workspace-hazards.md`; hazards classified not cleared for whole-tree; remaining = WorkSpace only; row not Complete — verify: no current-path claiming `archive\2026.05.29 - WorkSpace`; taxonomy/must-preserve not upgraded to final.

6. **Update inventory Notes** — path: `catalogue/inventory.md` (WorkSpace row / related nested notes) — action: Cycle 10 docs remediation pointer; retain nested **7** honesty; state still at root / not moved — verify: no false “moved Cycle 10”.

7. **Optional catalogue pointer (small)** — path: `catalogue/INDEX.md` Notes and/or a one-line cross-ref near WorkSpace row only — action: ensure durable artifact is discoverable from catalogue honesty without inventing a new catalogue database — verify: relative link to `../program/git-strategy-workspace-hazards.md` works from INDEX context (or absolute-from-repo path stated clearly).

8. **Session implementation artifacts** — paths: `sessions/2026.09.10-0907/04-implementation/log.md`, `changes.md` — action: record docs_only steps, zero-move attestation (incl. `_backups`/`_quarantine` still under WorkSpace), pointer to durable artifact, explicit “Appendix A not executed” — verify: explicit “corpus moves: 0”; opaque `.env` unread.

9. **Self-check before handoff** — action: grep/scan ROADMAP + INDEX + durable artifact for accidental “Complete”, Primary-next jump past Multi-experiment, WorkSpace archive path as **current**, or move commands — verify: remaining WorkSpace only; still in progress; appendix draft clearly non-executed.

**Skipped (explicit):** Auth/preflight for push/pull — **N/A**. Pull/sync — **N/A**. Any `Move-Item` / robocopy / remote surgery — **out of scope this cycle**. Appendix A execute — **deferred**.

---

## Appendix A — Deferred scoped isolation draft (NOT executed this cycle)

**Status:** Non-binding research-supported draft for a **future** `fs_mutation` cycle. **Do not implement in Cycle 10.** Continuity Choose / this plan’s docs_only approval **≠** authorization to run this map.

### Hypothetical from→to (destinations must be re-confirmed free at future plan time)

| Unit | From | To (illustrative hygiene / isolation destination) |
| --- | --- | --- |
| Backups parent | `C:\Project\WorkSpace\TestNewWorkspaceAgent\_backups` | e.g. `C:\Project\archive\hygiene\2026.09.10 - WorkSpace-_backups` (or dated quarantine isolation parent under `C:\Project\archive\` — planner of future cycle confirms free + taxonomy fit) |
| Quarantine parent | `C:\Project\WorkSpace\TestNewWorkspaceAgent\_quarantine` | e.g. `C:\Project\archive\hygiene\2026.09.10 - WorkSpace-_quarantine` (same confirmation rules) |

### Future-gate requirements (when someone promotes Appendix A)

- Set `mutation_class: fs_mutation` and include full **“What the user is approving”** (plain language + pros/cons + exact path map).
- Atomic move of each **named parent tree** (includes nested hermes clone `.git`); opaque `.env*`; remotes path-only; Windows lock recovery Continuity.
- Expect nested-root count **7→5** and ~3.3 GB out of live WorkSpace **if both** move — **does not** clear live hermes multi-remote; **does not** authorize whole-tree archive; Multi-experiment stays **in progress** / Remaining WorkSpace only.
- Pros: reduces unexpected clone roots under the live tree; clearer primary vs backup.  
- Cons: bookmarks/paths under WorkSpace break for those subtrees; XL Windows move risk; live multi-remote remains; must not be framed as row Complete.

---

## Non-goals

- Executing Appendix A or any corpus move/rename/delete this cycle
- Whole XL `WorkSpace` tree archive / force-move under ordinary Multi-experiment Continuity
- Marking Multi-experiment **Complete** or jumping **Primary next** / Special git while `WorkSpace` remains
- Reopening Medium / Early or re-proposing archived `PWAExemple` / `GitTest` / `WorkStationPWA` as sources
- Remote URL rewrite, dropping `cada`, history rewrite, force-push, reading `.env` contents
- Taxonomy final sign-off or must-preserve final lock
- Treating Continuity “Choose all” as plan-gate move approval
- Agent `git push` / `git pull` for this cycle
- Dumping user chores to “fix remotes/PATH” as Continuity requirements

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Implementer executes Appendix A despite docs_only | Empty execute map + AC + attestation; auditor fails on any corpus path change |
| Docs framed as Multi-experiment Complete / “WorkSpace solved” via whole-tree | Steps 3–9 forbid Complete / Primary-next jump; durable artifact states whole-tree still blocked |
| Scoped isolation framed as clearing live multi-remote | Artifact + ROADMAP must state live `origin`+`cada` remains after optional future isolation |
| Deleting backup/quarantine instead of isolate-keep policy | Fate table: isolate / keep / defer — **never delete by default** |
| Secrets leak into session docs | Opaque path presence only; no content reads |
| Taxonomy / must-preserve overclaimed as final | Exact proposed-ratified / draft wording in artifact + INDEX |
| Accidental sibling-tree git ops | Org-repo root only for doc writes |

**Rollback:** revert org-repo doc edits via git; no corpus rollback needed if attestation holds (nothing moved).

---

## Ready to implement

**yes**

## Blocking questions

**none**

---

## Plan result (for orchestrator)

- **plan_path:** `sessions/2026.09.10-0907/03-plan/plan.md`
- **ready_to_implement:** yes
- **mutation_class:** `docs_only`
- **plan_gate_needed:** no
- **blocking_questions:** none
- **step_count:** 9 (plus Appendix A non-executed draft)
- **one-line summary:** Docs-only Cycle 10: durable WorkSpace hazard/remediation rules + INDEX/ROADMAP honesty; zero moves; scoped `_backups`/`_quarantine` isolation deferred as appendix.
