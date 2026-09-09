# Plan — Pull cycle (`sessions/2026.09.09-1332`)

## Goal

Have the **agent** sync this organisation repo with `origin` by running `git pull --ff-only` on local `main` (tracking `origin/main`), **only** inside  
`C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`, after dual preflight (remote HTTPS reachability + agent Git for Windows / GCM). If the working tree is dirty, **abort without pulling**, list dirty paths, mark the session **blocked**, and still complete FAW docs through self-improver. No corpus path moves; taxonomy and must-preserve gates are out of scope.

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`docs_only`** |
| Corpus FS | **Zero intentional corpus FS mutations** (no catalogue/program inventory moves, renames, or deletes). In-scope git ops are fetch/ff-only update of **this org-repo git root only**. Session markdown under `sessions/2026.09.09-1332/` may be written as FAW artifacts. |
| User approval before implementer | **Not required** for corpus mutation (docs_only). Orchestrator may proceed to implementer without a corpus plan-gate pause. |
| First-move gates | **N/A** — this is not an Early-simple / first-move FS batch. |
| Implementer attestation | Implementation log must state: no intentional corpus moves/renames/deletes; only org-root git status/preflight/(conditional) pull + session docs. |

### Corpus plan-gate

**No.** Mutation class is `docs_only`. Do **not** pause the user for move-batch approval.

## What the user is approving

**N/A for corpus FS.** This cycle does not ask the user to approve path moves.

For clarity (not a plan-gate): implementing this plan means the agent will (1) re-confirm org git root + GfW dual preflight, (2) abort pull if dirty and mark `blocked`, or (3) if clean, run `git pull --ff-only` via GfW and record SHAs. No stash, merge, rebase, force, or hard reset.

## Acceptance criteria

Hard AC (auditor must check these):

- [ ] Before any fetch/pull: `git rev-parse --show-toplevel` (via **GfW** binary below) equals org root  
  `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` (slash-normalized OK). No sibling `C:\Project` trees touched.
- [ ] Dual preflight recorded in implementation log: remote scheme **https**; tracking `main` → `origin/main`; agent uses preferred GfW  
  `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe`; PATH/MSYS not used as sole status/pull binary; GCM / non-interactive evidence boolean (no secrets); `gh` present/absent noted as **optional only**.
- [ ] Dirty gate via **same GfW** binary (`git status --porcelain` and/or `git status -sb`). If any dirty/untracked → **abort pull**, list paths, session status **`blocked`**, `blocker_type` / process note **`dirty_working_tree`** (not auth). Do not stash/autostash.
- [ ] If clean at implement time: agent Shell runs `git pull --ff-only` (or equivalent fetch + ff-only merge) against `origin` / tracking `origin/main` and **succeeds** (exit 0), including already-up-to-date.
- [ ] On non-ff divergence, auth failure, or other pull error: fail-closed — **no** merge fallback, **no** rebase, **no** force, **no** hard reset, **no** `--no-verify`, **no** git config changes; session `blocked` + `blocker_type` (`agent_environment` vs `user_credentials` as appropriate).
- [ ] Post-attempt verification recorded: `git status -sb`, ahead/behind vs `origin/main` (after any real fetch if pull ran), HEAD SHA (before/after when a fast-forward occurred).
- [ ] Full session artifacts under `sessions/2026.09.09-1332/` for implement / audit / self-improvement as FAW requires; **self-improver still runs** if blocked.
- [ ] Taxonomy final sign-off and must-preserve draft review **not** attempted and **not** used as pull blockers. Taxonomy remains **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**.

Optional / “if available” (include when cheap; **not** hard AC — do not fail audit solely for missing these):

- Exact subject/body of remote tip `489f03a` (research noted unknown; re-inspect only after a successful clean pull).
- Size or file counts of dirty paths.
- User-terminal pull success notes beyond the research brief.
- `GITHUB_TOKEN` presence boolean (already researched; not sole auth path).

## Ordered steps

Use GfW for **all** status and pull commands in this cycle:

`$gfw = 'C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe'`  
Working directory: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`

### 1. Org-root lock

- **Paths:** org git root only.
- **Action:** `Set-Location` to org root; `& $gfw rev-parse --show-toplevel`. Confirm match to org path. Refuse to continue if mismatch.
- **Verify:** Toplevel string matches org repo; log command + result. No ops under sibling `C:\Project` trees.

### 2. Dual preflight (adapted for **pull**, not push)

- **Paths / facts:** remote `origin` HTTPS URL; branch tracking; agent git binary; credential helper; optional `gh`.
- **Action:** Re-check (boolean / non-secret only):
  - `remote get-url origin` → expect `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git`
  - `status -sb` / upstream → `main...origin/main`
  - Prefer GfW absolute path (PATH `git` is MSYS without helper — do not use for gate/pull)
  - GfW `credential.helper` → expect `manager`; optional non-secret fill / `fetch --dry-run` reachability if cheap
  - Note `gh` absent = optional; do **not** classify as `user_credentials` solely for missing `gh`
  - Classify auth readiness separately from dirty-tree readiness
- **Verify:** Log dual-preflight table. Research baseline: GfW auth **green**; pull ready **no** while dirty. If GfW auth fails at implement time → `blocked` + `blocker_type` (`agent_environment` if wrong binary/sandbox; `user_credentials` if GCM fill/login truly fails); do not pull.

### 3. Dirty-abort gate (Option A — **expected path today**)

- **Paths:** GfW porcelain list (research: 15 lines — post-`1246` SI dirt + current `sessions/2026.09.09-1332/`).
- **Action:** `& $gfw status --porcelain`. If non-empty:
  - Do **not** run pull/fetch that updates refs for the goal (dry-run already done in research is enough evidence of remote ahead).
  - List dirty paths in `04-implementation/log.md`.
  - Set session **`blocked`**; process blocker **`dirty_working_tree`** (distinct from auth).
  - Skip step 4; continue to verification snapshot (step 5) + handoff for auditor/self-improver.
- **Verify:** Implementation log states pull **not attempted** because dirty; no stash; no merge/rebase.

### 4. Conditional ff-only pull (only if step 3 is clean)

- **Action:** Record HEAD before (`rev-parse HEAD`). Run `& $gfw pull --ff-only` (tracking `origin/main`). On failure: document stderr; `blocked` + typed `blocker_type`; **no** fallback strategies.
- **Verify:** Exit 0; HEAD after matches expected remote tip when a ff occurred (research remote tip was `489f03a` — re-read live; do not hard-code as AC if tip moved). Already-up-to-date with exit 0 also satisfies AC.

### 5. Post-attempt verification

- **Action:** `& $gfw status -sb`; ahead/behind vs `origin/main`; HEAD SHA(s). If aborted dirty: still record current HEAD (`f5012d6` at research time) and note local `origin/main` cache may still be stale vs remote tip.
- **Verify:** Numbers and SHAs written to implementation log. Do not claim session `complete` if pull aborted or failed.

### 6. Session documentation + self-improver path

- **Paths:** `sessions/2026.09.09-1332/04-implementation/`, later `05-audit/`, `06-self-improvement/`, `SESSION.md` as FAW requires.
- **Action:** Write implementation log (BOM-safe on Windows if writing via PowerShell). Orchestrator continues auditor → **mandatory self-improver** even when `blocked`.
- **Verify:** Artifacts exist; status reflects blocked vs complete honestly.

## Non-goals

- Taxonomy **final** ratification (remains **proposed-ratified — ready for user sign-off**)
- Must-preserve list lock (remains **draft — not auto-locked**)
- Corpus FS moves / renames / deletes
- `git push`, new publish commits, amend of pushed commits
- Merge or rebase pull strategies; autostash; agent conflict resolution
- Sibling repositories under `C:\Project`
- Changing git config; force-push; hard reset
- Using PATH/MSYS git as the dirty gate or pull binary
- Marking complete because the user could pull in their own terminal

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Dirty tree blocks sync (remote at `489f03a`) | By design (Q3=A). Document abort; do not stash. Later user cycle may commit/stash then re-pull. |
| MSYS status skew (104 vs GfW 15) | Always pair status + pull on GfW; ignore MSYS alone for gate. |
| Wrong git root / sibling workspace | Step 1 toplevel check; fail-closed. |
| Auth / GCM regression | Dual preflight; `user_credentials` vs `agent_environment`; no false complete. |
| Non-ff divergence after clean | Abort; no merge/rebase fallback. |
| “Fix” with force/hard reset | Forbidden. Rollback = leave tree as-is; document only. |
| Missing `gh` misread as auth failure | Optional only while GCM works. |
| Overclaim taxonomy / must-preserve | Explicit out of scope; exact proposed-ratified / draft wording if mentioned. |

**Rollback:** No corpus mutations to undo. If a clean pull somehow ran incorrectly, do **not** hard-reset; stop and report — user decides. Dirty-abort leaves the tree unchanged.

## Ready to implement

**yes**

Rationale: Auth dual preflight for GfW Option A is green. Implementer is cleared to execute the **documented fail-closed path** (expect dirty-abort today → session `blocked` → still self-improve). If the tree is somehow clean at implement time, proceed with GfW `pull --ff-only`. No corpus plan-gate pause.

## Blocking questions

**none**

(Research already locked Choose answers; dirty-abort and GfW path are decided. Follow-up stash/commit of post-`1246` dirt is out of scope unless the user starts a new cycle.)
