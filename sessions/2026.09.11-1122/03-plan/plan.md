# Plan — Cycle 17 (FAW final closing pass + Cycle 16 finish-sync)

**Session:** `sessions/2026.09.11-1122/`  
**Continuity:** Q1=A · Q2=A · Q3a=A · Q3b=A (locked — do not re-litigate)  
**stage_1_hold:** **yes** — Hermes plan gate **mandatory**; same-run implement **FORBIDDEN** even though `ready_to_implement: yes`  
**STAGE 2 resume:** same folder after Hermes **yes** (+ amendments)

---

## Goal

Amend Full Agent Workflow so **git-manager owns cycle outputs end-to-end**: keep optional mid-cycle (phase-5) git for implementer work, and add a **mandatory final closing pass after self-improver** that stages/commits/pushes allowlisted late dirt — especially `06-audit/**`, `07-self-improvement/**`, cycle `.cursor/**` edits, and `SESSION.md` close — under the same allowlist + Git-for-Windows / GCM rules. Orchestrator must **not** mark a session `complete` while that late allowlisted dirt remains (unless final pass honestly returned `blocked`).

After Hermes gate **yes**, STAGE 2 runs in order: **(1)** finish-sync Cycle 16 leftover allowlisted paths as the first git pass (**Q2=A**), **(2)** implement the FAW definition edits, **(3)** continue Cycle 17 under the amended order including the mandatory final closing pass. ROADMAP stays Multi-experiment **WorkSpace only** (not Complete). Zero WorkSpace corpus moves / remote-config. Taxonomy remains **proposed-ratified — ready for user sign-off**; must-preserve remains **draft — not auto-locked**. TNA / non-allowlist: **NO_AUTO_COMMIT**.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`docs_only`** |
| Mutation kind | N/A (not `fs_mutation`) |
| Corpus FS | **Zero** intentional corpus moves/renames/deletes under `C:\Project` / catalogue batches; **zero** WorkSpace remote-config |
| Org-repo disk | FAW definition file edits + allowlisted `git add` / commit / push inside **this** organisation git root only |
| User approval before implementer | **Hermes plan gate required** (Continuity override of usual docs_only same-run auto-continue) |
| First-move gates | N/A — no corpus first move; taxonomy/must-preserve **not** upgraded |

**Implementer attestation (STAGE 2):** Log `Test-Path C:\Project\WorkSpace` still true; no WorkSpace path mutation; Multi-experiment **not** marked Complete; no Primary next / Special git jump; no non-allowlist / secret paths staged.

---

## STAGE 1 hold (orchestrator law)

| Field | Value |
| --- | --- |
| `stage_1_hold` | **yes** |
| Same-run implement | **FORBIDDEN** |
| Despite | `docs_only` + `ready_to_implement: yes` (content-ready) |
| Stop after | This plan → **Hermes plan gate** |
| Resume | **Same session** `sessions/2026.09.11-1122/` for STAGE 2 after user **yes** (+ amendments) |
| Continuity ≠ Hermes | Continuity Choose already locked Q1–Q3; this gate is **execute approval** for STAGE 2 |

---

## What the user is approving (Hermes intent-preview)

**Plain language:** Saying **yes** authorizes STAGE 2 in this session folder: first commit/push leftover Cycle 16 allowlisted files that were orphaned after the mid-cycle push; then edit FAW skill/agents/rules/templates so every future cycle runs a **final** git-manager pass after self-improvement; then finish Cycle 17 under that new order (including a final close for this cycle’s own artifacts). Saying **no / edit** means nothing is committed or amended until you revise the plan — Continuity locks stay, but STAGE 2 does not start.

### File / command map (yes commits to)

**A — STAGE 2 step 1: Cycle 16 leftover finish-sync (first git pass, Q2=A)**

Org-repo root only. Prefer GfW absolute `git.exe` + GCM. Explicit path stage (no `git add -A`).

| # | Path |
| --- | --- |
| 1 | `sessions/2026.09.11-1038/05-git/log.md` |
| 2 | `sessions/2026.09.11-1038/06-audit/report.md` |
| 3 | `sessions/2026.09.11-1038/07-self-improvement/audit-realization.md` |
| 4 | `sessions/2026.09.11-1038/07-self-improvement/backlog.md` |
| 5 | `sessions/2026.09.11-1038/07-self-improvement/changes-applied.md` |
| 6 | `sessions/2026.09.11-1038/07-self-improvement/proposals.md` |
| 7 | `sessions/2026.09.11-1038/SESSION.md` |
| 8 | `.cursor/agents/auditor.md` |
| 9 | `.cursor/agents/implementer.md` |
| 10 | `.cursor/agents/orchestrator.md` |
| 11 | `.cursor/agents/prompt-betterment.md` |
| 12 | `.cursor/agents/researcher.md` |
| 13 | `.cursor/skills/full-agent-workflow/SKILL.md` |
| 14 | `AGENTS.md` |
| 15 | `sessions/_templates/03-plan.md` |
| 16 | `sessions/_templates/SESSION.md` |

**Exclude from this pass:** `?? sessions/2026.09.11-1122/` (this cycle — later mid/final).  
**Defer (optional later, not this first pass):** `?? sessions/2026.09.11-0859/`, `?? sessions/2026.09.11/`.  
**Commands (intent):** dual preflight → `git add` of the 16 paths → commit (utf8NoBOM message) → `git push` → verify ahead/behind; log under this session’s git artifacts as appropriate.

**B — Then: FAW definition edits (implementer)**

| File | Intent |
| --- | --- |
| `.cursor/skills/full-agent-workflow/SKILL.md` | Dual git: mid optional/early + **mandatory final** after self-improver; Done/complete gate |
| `.cursor/agents/orchestrator.md` | Mid + mandatory final; fail-closed Completion |
| `.cursor/agents/git-manager.md` | Mid/final modes; late stage set; `pass_kind` |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | Final closing-pass handoff |
| `sessions/_templates/SESSION.md` | Workflow step + no-complete-with-late-dirt |
| `AGENTS.md` | Insert git-manager; mid+final law |
| `.cursor/rules/full-agent-workflow.mdc` | Dual-pass + complete gate |
| Optional | `sessions/_templates/05-git-log.md` — mid/final sections if useful |

**C — Then: Cycle 17 phases under amended order** including mandatory final closing pass for this cycle’s allowlisted dirt (`1122` artifacts + any cycle `.cursor` edits from the amendment).

**Not in the map:** WorkSpace moves; Multi-experiment Complete; taxonomy/must-preserve upgrade; TNA auto-commit; force-push; sibling trees outside org-repo git root.

### Pros / cons (tradeoffs)

| Pros | Cons |
| --- | --- |
| Clears Cycle 16 orphans before fixing the workflow law | Two git launches on mutating cycles (mid + final) |
| Future cycles cannot “complete” with audit/self-improve only on disk | Tiny post-final `05-git` log dirt may remain once (known Low / existing FAW tradeoff) |
| Matches Continuity Q1=A / Q2=A; allowlist + GfW/GCM unchanged | Several definition surfaces must stay consistent |
| WorkSpace untouched; ROADMAP honesty preserved | Deferred `0859` / bare `2026.09.11` sessions stay untracked until a later finish-sync |

**What “no / edit” means:** No STAGE 2 git or FAW edits; plan revised; Continuity Q1–Q3 remain locked unless you reopen them.

---

## Continuity locks (encode — do not re-ask)

| ID | Lock |
| --- | --- |
| **Q1=A** | Optional mid-cycle git-manager (phase 5) **+ mandatory FINAL closing pass** after self-improver for `06-audit/**`, `07-self-improvement/**`, `.cursor/**` cycle edits, `SESSION.md` close; same allowlist + GfW/GCM; **do not mark complete** while that late allowlisted dirt remains |
| **Q2=A** | STAGE 2 **step 1** = git-manager finish-sync of the **16** Cycle 16 allowlisted paths above; exclude `1122/`; optional later `0859/` + `2026.09.11/` |
| **Q3a=A** | Taxonomy/must-preserve **waive re-litigation** — stay proposed-ratified / draft |
| **Q3b=A** | TNA dirty **defer / NO_AUTO_COMMIT** |
| ROADMAP | Multi-experiment **WorkSpace only** — never Complete this cycle; never Primary next / Special git; never reopen Medium / archived peers as sources |

---

## Acceptance criteria

### STAGE 1 (this run — plan + Hermes hold)

- [x] Continuity Q1=A, Q2=A, Q3a=A, Q3b=A locked in prompt-betterment notes
- [x] Research mapped orphan-after-phase-5 gap + leftover inventory + workflow edit list
- [ ] Plan is **`docs_only`** with Hermes **“What the user is approving”** intent-preview
- [ ] Plan encodes **Q1=A** (mid optional + mandatory final) and **Q2=A** leftover-first STAGE 2 order
- [ ] Orchestrator stops at Hermes (`stage_1_hold: yes`); same-run implement **FORBIDDEN**

### STAGE 2 — after Hermes **yes** only

#### Git pass 1 (Cycle 16 leftovers)

- [ ] Dual auth/preflight: remote tracking; agent uses GfW absolute `git.exe` when PATH lacks GCM; GCM evidence; `gh` not sole signal
- [ ] Exact **16-path** stage set committed and pushed (or honest `blocked` + `blocker_type` — never false complete)
- [ ] `sessions/2026.09.11-1122/` **not** included in leftover pass
- [ ] Optional `0859/` / `2026.09.11/` **not** required in this pass (deferred)
- [ ] No non-allowlist / secrets staged; TNA untouched (**Q3b=A**)

#### FAW amendment

- [ ] `SKILL.md`, `orchestrator.md`, `git-manager.md`, `handoff-templates.md`, `sessions/_templates/SESSION.md`, `AGENTS.md`, `.cursor/rules/full-agent-workflow.mdc` updated for mid + **mandatory final** closing pass
- [ ] Optional `05-git-log` template updated if cheap
- [ ] Mid phase-5 remains **optional/early** for implementer work (**Q1=A**)
- [ ] Final pass stage set documented: `06-audit/**`, `07-self-improvement/**`, `SESSION.md` close, cycle `.cursor/**` / other allowlisted cycle dirt
- [ ] Complete gate: orchestrator **cannot** mark `complete` if final closing pass was skipped while late allowlisted dirt remains
- [ ] Prefer append mid/final sections in existing `05-git/log.md` (not a separate folder unless needed)

#### Cycle 17 under amended order

- [ ] Remaining Cycle 17 phases run with amended law (implementer if needed for amendment → mid git as appropriate → auditor → self-improver → **final git-manager** → Close)
- [ ] Final closing pass commits/pushes this cycle’s allowlisted `06`/`07`/`SESSION` / cycle `.cursor` dirt (or honest `blocked`)
- [ ] Session not marked `complete` while that late allowlisted dirt remains after a skipped final pass

#### Guardrails

- [ ] **Zero** WorkSpace corpus moves; `Test-Path C:\Project\WorkSpace` still true (or equivalent probe logged)
- [ ] Multi-experiment **not** Complete; ROADMAP Next FAW lock hint still WorkSpace-only residual
- [ ] Taxonomy not final-signed; must-preserve not auto-locked (**Q3a=A**)
- [ ] Diff of amended FAW files shows final closing pass in skill + orchestrator + git-manager + handoff/SESSION (and AGENTS/rules)

---

## Steps (ordered for STAGE 2 — execute only after Hermes yes)

### Step 0 — Hermes gate (orchestrator; STAGE 1)

- **Paths:** this `plan.md`; relay intent-preview to user  
- **Action:** Stop. Do **not** launch implementer/git-manager until user **yes** (+ amendments)  
- **Verify:** `stage_1_hold` honored; no same-run STAGE 2

### Step 1 — Dual auth / publish preflight (git-manager)

- **Paths:** org-repo git root only  
- **Action:** Confirm tracking vs `origin`; invoke GfW `…\Git\cmd\git.exe` when PATH git lacks helper; confirm `credential.helper` / GCM; note `gh` present/absent without treating absence alone as credentials failure  
- **Verify:** Agent can push non-interactively **or** fail-closed `blocked` with `blocker_type` `agent_environment` vs `user_credentials` (do not proceed hoping push works)

### Step 2 — Cycle 16 leftover finish-sync (**Q2=A**, first git pass)

- **Paths:** the **16** paths in the intent-preview table  
- **Action:** Explicit `git add` those paths only; commit with clear finish-sync message (PowerShell utf8NoBOM / here-string `-m`); push; append/update git log for this cycle’s git phase as appropriate  
- **Exclude:** `sessions/2026.09.11-1122/**`  
- **Defer:** `sessions/2026.09.11-0859/`, `sessions/2026.09.11/`  
- **Verify:** Those 16 paths clean (or only expected post-push log Low dirt); branch not falsely claimed synced on abort; no secrets; porcelain does not show leftover Cycle 16 core paths as still dirty after successful push

### Step 3 — Implement FAW definition amendment

- **Paths:**  
  - `.cursor/skills/full-agent-workflow/SKILL.md`  
  - `.cursor/agents/orchestrator.md`  
  - `.cursor/agents/git-manager.md`  
  - `.cursor/skills/full-agent-workflow/references/handoff-templates.md`  
  - `sessions/_templates/SESSION.md`  
  - `AGENTS.md`  
  - `.cursor/rules/full-agent-workflow.mdc`  
  - Optional: `sessions/_templates/05-git-log.md`  
- **Action:** Encode **Q1=A**: mid optional/early after implementer; **mandatory final** after self-improver when allowlisted late dirt remains; complete-gate fail-closed; mid/final modes on git-manager; handoff template for final pass; insert git-manager in `AGENTS.md` delegate list  
- **Verify:** Grep/diff shows “final closing” (or equivalent) + no-complete-with-late-dirt on skill, orchestrator, git-manager, SESSION template, AGENTS, rules; handoff template has final section

### Step 4 — Mid-cycle git-manager for amendment outputs (optional/early per Q1=A)

- **Paths:** allowlisted amendment outputs + any early `1122` seeds as appropriate  
- **Action:** Standard mid pass (same allowlist + GfW/GCM); do **not** treat mid pass as substitute for final close  
- **Verify:** Implementer-facing changes committed/pushed when mid pass runs; late 06/07/SESSION still expected later

### Step 5 — Auditor (Cycle 17)

- **Paths:** `sessions/2026.09.11-1122/06-audit/report.md` (orchestrator persists if auditor readonly)  
- **Action:** Verify vs this plan’s AC; readonly auditor — no silent fixes  
- **Verify:** Report exists and scores AC honestly

### Step 6 — Self-improver (mandatory)

- **Paths:** `sessions/2026.09.11-1122/07-self-improvement/**`; may touch allowlisted `.cursor/**`  
- **Action:** Process audit; propose/apply workflow improvements within allowlist  
- **Verify:** Self-improvement artifacts present

### Step 7 — Final closing pass git-manager (**Q1=A mandatory**)

- **Paths:** allowlisted late dirt — at minimum this cycle’s `06-audit/**`, `07-self-improvement/**`, `SESSION.md` (close), cycle `.cursor/**` edits; other allowlisted cycle dirt as present  
- **Action:** Final mode stage/commit/push; prefer writing final section of `05-git/log.md` **before** commit when practical; same allowlist + GfW/GCM  
- **Verify:** Late allowlisted dirt committed/pushed **or** session `blocked` with honest `blocker_type`; **never** false `complete`

### Step 8 — Close SESSION

- **Paths:** `sessions/2026.09.11-1122/SESSION.md`  
- **Action:** Mark `complete` **only if** final closing pass succeeded (or honest blocked path already recorded); if final skipped with late dirt → do **not** complete  
- **Verify:** Status matches gate; ROADMAP/WorkSpace unchanged (still Remaining WorkSpace only)

### Step 9 — WorkSpace / ROADMAP honesty (verify-only)

- **Paths:** `C:\Project\WorkSpace`; `program/ROADMAP.md`; `catalogue/INDEX.md` as needed  
- **Action:** Probe only — **no** moves; do not invent archive; do not Complete Multi-experiment  
- **Verify:** WorkSpace still at root; row still Remaining WorkSpace only

---

## Non-goals

- WorkSpace path moves, whole-tree archive, Appendix A re-execute, nested WorkSpace remote-config  
- Marking Multi-experiment Complete or jumping Primary next / Special git  
- Re-opening Medium / Early / archived Multi-experiment peers as move sources  
- Final taxonomy / must-preserve user sign-off (**Q3a=A** waive)  
- Auto-committing TNA or other non-allowlist dirt (**Q3b=A**)  
- Including `1122/` in Cycle 16 leftover finish-sync  
- Requiring `0859/` / bare `2026.09.11/` in the first leftover pass  
- Changing Q1 to final-only or mid-mandatory-only  
- Same-run STAGE 2 before Hermes **yes**

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Same-run implement despite hold | Orchestrator enforces `stage_1_hold`; Hermes mandatory |
| Cycle 16 orphans left while only editing docs | Step 2 before Step 3 (**Q2=A**) |
| False complete after Cycle 17 | Complete gate in skill/orchestrator/SESSION; Step 7 before Step 8 |
| Staging `1122` in leftover pass | Explicit exclude list |
| Wrong git binary / no GCM | GfW absolute path; `blocker_type` `agent_environment` |
| Credentials missing | Fail-closed `blocked` / `user_credentials`; leave local commit if created; never force-push |
| Post-final log dirt | Known Low; write log before final commit when practical |
| Accidental WorkSpace Complete / move | Zero corpus moves; Step 9 verify-only |
| Allowlist mislabeled “unrelated” (Cycle 16 bug) | Explicit 16-path list; AGENTS + templates are allowlisted |

**Rollback:** Revert org-repo commits via normal non-force history if needed; WorkSpace untouched so no corpus rollback. Do not force-push.

---

## Ready to implement

**yes** (content-ready — Continuity locked; leftover set + edit surfaces known; no blocking questions)

**BUT:** `stage_1_hold: **yes**` — orchestrator must **not** same-run implement. Hermes plan-gate **yes** required before Steps 1–9.

---

## Blocking questions

**none**
