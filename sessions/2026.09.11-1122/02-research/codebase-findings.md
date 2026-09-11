# Codebase findings — Cycle 17

**Probe method:** Git for Windows `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (`credential.helper=manager`); PATH default is MSYS `C:\msys64\usr\bin\git.exe` (prefer GfW for porcelain). WorkSpace/INDEX via `Test-Path` + `Select-String`. Ahead/behind: `0 / 0` on `main...origin/main`.

---

## 1. Current FAW phase order vs orphan-after-push

### Canonical order today (phase-5 git only)

| Surface | Order stated | Gap vs Q1=A mid+final |
| --- | --- | --- |
| `.cursor/skills/full-agent-workflow/SKILL.md` Steps 0–9 | … implementer → **6. git-manager → 05-git** → **7. auditor → 06-audit** → **8. self-improver → 07** → **9. Close SESSION** | Single mid-cycle git; Done criteria require `06-audit/report.md` + `07-…/changes-applied.md` on disk but **no** post–self-improver commit/push; “Single-commit vs session finalize” explicitly tolerates post-push dirty session logs |
| `.cursor/agents/orchestrator.md` | Phases 1–7: … implementer → **git-manager (5)** → auditor (6) → self-improver (7); Completion: ensure audit → launch self-improver → mark `complete` | No mandatory **final** git-manager; can mark `complete` with allowlisted late dirt uncommitted |
| `.cursor/agents/git-manager.md` | Frontmatter: “Runs **after implementer and before auditor**” | Describes **one** mid-cycle pass only; no final-closing-pass duty or allowlist late-path set (`06/**`, `07/**`, SESSION close, cycle `.cursor/**`) |
| `references/handoff-templates.md` | `## git-manager` → `05-git/` then `## auditor` → `06-audit/` then `## self-improver` | No second git handoff / closing-pass template after self-improver |
| `AGENTS.md` | Short delegate list: `… implementer → auditor → self-improver` (**omits git-manager**) | Stale vs skill/rules; no final-close rule |
| `.cursor/rules/full-agent-workflow.mdc` | Delegate: `… implementer → git-manager → auditor → self-improver` | Mentions post-push dirty finalize as expected; **no** mandatory final closing pass; does not forbid `complete` while 06/07/SESSION dirt remains |
| `sessions/_templates/SESSION.md` | Workflow: … **6. git-manager** → 7 audit → 8 self-improve → **9. Close SESSION** | Checklist ends at close; no “10. final git-manager closing pass” / cannot-complete-with-late-dirt gate |

**Root cause:** Phase order puts the only mandatory git-manager **before** auditor and self-improver. Anything written after that push (real audit body, self-improvement edits, SESSION close, template/agent tweaks) is structurally orphaned unless a later finish-sync Continuity runs.

### Cycle 16 evidence (`sessions/2026.09.11-1038/`)

- Mid-cycle `05-git/log.md`: commit **`9f09dc7`** (`docs(cycle-16): WorkSpace hazard honesty + session artifacts`) staged implementer + **seeded** session tree (including stub `06-audit/`, `07-self-improvement/`, `SESSION.md`), pushed `main` → `origin/main` (verified 0/0).
- Log incorrectly labeled **allowlisted** dirt as “Unrelated”: `AGENTS.md`, `sessions/_templates/03-plan.md`, `sessions/_templates/SESSION.md` (these are on the FAW allowlist).
- After push: auditor wrote real `06-audit/report.md`; self-improver wrote `07-self-improvement/**` + edited `.cursor/agents/*`, `SKILL.md`, templates; orchestrator closed `SESSION.md`; `05-git/log.md` post-push finalize also dirtied.
- Session marked **`complete`** with those paths still dirty — exact orphan-after-phase-5 pattern Continuity Q1 targets.
- Self-improve **P7** deferred: “Optional finish-sync Continuity when only FAW-allowlist dirt remains after push” — Cycle 17 makes that **mandatory final pass** in workflow law.

---

## 2. Live leftover inventory (GfW porcelain)

### Allowlisted — Cycle 16 leftovers (STAGE 2 **first** git pass core)

| Path | Status | Why leftover |
| --- | --- | --- |
| `sessions/2026.09.11-1038/06-audit/report.md` | `M` | Real audit after `9f09dc7` (~+57 lines vs seed) |
| `sessions/2026.09.11-1038/07-self-improvement/audit-realization.md` | `M` | Post-push self-improve |
| `sessions/2026.09.11-1038/07-self-improvement/backlog.md` | `M` | Post-push self-improve |
| `sessions/2026.09.11-1038/07-self-improvement/changes-applied.md` | `M` | Post-push self-improve |
| `sessions/2026.09.11-1038/07-self-improvement/proposals.md` | `M` | Post-push self-improve |
| `sessions/2026.09.11-1038/SESSION.md` | `M` | Close / phase flips after mid-git |
| `sessions/2026.09.11-1038/05-git/log.md` | `M` | Expected post-push finalize of phase-5 log |
| `.cursor/agents/auditor.md` | `M` | Cycle 16 self-improve P4 |
| `.cursor/agents/implementer.md` | `M` | Cycle 16 self-improve P3 |
| `.cursor/agents/orchestrator.md` | `M` | Cycle 16 self-improve P1 |
| `.cursor/agents/prompt-betterment.md` | `M` | Cycle 16 self-improve P2 |
| `.cursor/agents/researcher.md` | `M` | Cycle 16 self-improve P3 |
| `.cursor/skills/full-agent-workflow/SKILL.md` | `M` | Cycle 16 self-improve touch |
| `AGENTS.md` | `M` | Allowlisted; mislabeled “unrelated” in Cycle 16 git log |
| `sessions/_templates/03-plan.md` | `M` | Allowlisted; mislabeled “unrelated” |
| `sessions/_templates/SESSION.md` | `M` | Allowlisted; Cycle 16 P5 template align |

**Proposed STAGE 2 first-pass stage set (Q2=A):** all paths in the table above (explicit `git add` path list; no `git add -A`). Message theme: finish-sync Cycle 16 allowlisted orphans (audit/self-improve/SESSION + FAW meta + templates).

### Allowlisted — other untracked sessions (not Cycle 16 core; decide in plan)

| Path | Status | Note |
| --- | --- | --- |
| `sessions/2026.09.11-0859/` | `??` | Prior Cycle 15 full session — allowlisted backlog; **optional** include in first pass or later |
| `sessions/2026.09.11/` | `??` | Older dated session — allowlisted backlog; **optional** |
| `sessions/2026.09.11-1122/` | `??` | **This** Cycle 17 in-progress session — **exclude** from Cycle 16 finish-sync; commit via Cycle 17 mid/final passes |

### Unrelated / out of org-repo finish-sync

| Item | Classification |
| --- | --- |
| TNA / hermes nested dirty WTs | Outside org-repo porcelain; **Q3b=A** → disclose only, **NO_AUTO_COMMIT** |
| Non-allowlist product/corpus paths | None currently in org-repo porcelain |
| `.cursor/rules/full-agent-workflow.mdc` | **Clean** (not dirty); still a **workflow amendment** surface for Cycle 17 implement |

**Unrelated dirty blocker:** none for org-repo allowlist finish-sync (`blocker_type` N/A for first pass if only paths above staged).

---

## 3. Recommended workflow edit map (mid + mandatory final)

| File | Recommended bullets / edits |
| --- | --- |
| `.cursor/skills/full-agent-workflow/SKILL.md` | Extend Workflow progress: keep **6. git-manager (mid, optional/early for implementer work)**; after **8. self-improver** add **9. git-manager final closing pass (MANDATORY when allowlisted late dirt)** → then **10. Close SESSION** (or keep Close then final git — prefer **final git before marking complete**). Done criteria: cannot claim done / orchestrator must not mark `complete` while allowlisted `06/**`, `07/**`, SESSION close, or cycle `.cursor/**` dirt remains unless final pass returned `blocked` with honest `blocker_type`. Clarify mid vs final in git-manager permanent-phase paragraph. |
| `.cursor/agents/orchestrator.md` | Dual git launches: mid after implementer (Q1 optional/early); **mandatory** final after self-improver when allowlisted late dirt. Completion §: final closing pass **before** `complete`; if skipped with late dirt → `blocked` / process fail. Align STAGE 1 same-run path to include final git after self-improve. |
| `.cursor/agents/git-manager.md` | Change “before auditor” → supports **mid** and **final** modes. Final mode stage set: `06-audit/**`, `07-self-improvement/**`, `SESSION.md` close, cycle `.cursor/**` edits, other allowlisted cycle dirt; same GfW/GCM/allowlist/secrets rules. Return field e.g. `pass_kind: mid \| final`. |
| `references/handoff-templates.md` | Add `## git-manager (final closing pass)` handoff after self-improver; mid handoff remains. Instruct orchestrator to pass leftover path list / allowlist gate. |
| `sessions/_templates/SESSION.md` | Add workflow step for final git-manager; Note: do not set Status `complete` if final closing pass skipped and allowlisted late dirt remains. |
| `AGENTS.md` | Insert `git-manager` in default delegate order; state mid optional + **mandatory final** after self-improver; fail-closed complete rule. |
| `.cursor/rules/full-agent-workflow.mdc` | Same dual-pass + no-false-complete with late allowlisted dirt; keep GfW/allowlist publish law. |
| Optional: `sessions/_templates/05-git-log.md` | Section headers for mid vs final pass if template exists. |

**Design note (Q1=A):** Mid pass still commits implementer / early session seeds; final pass owns audit + self-improve + SESSION close + FAW meta. Tiny post-final log dirt may remain (known Low) — minimize by writing final `05-git` (or `05-git-final`) log **before** the final commit when practical.

---

## 4. WorkSpace / ROADMAP (verify-only — zero moves)

| Check | Result |
| --- | --- |
| `Test-Path C:\Project\WorkSpace` | **True** — still at root |
| `archive` / `paused` / `active` WorkSpace | **False** — not moved |
| `catalogue/INDEX.md` | Current path `C:\Project\WorkSpace`; Notes: still at root, **not** archived; row **not** Complete; whole-tree clearance **NO** |
| `program/ROADMAP.md` | Multi-experiment **Remaining: WorkSpace only**; Next FAW lock hint WorkSpace-only; **not** Complete |
| `program/git-strategy-workspace-hazards.md` | **EXISTS**; Cycle 16 attestation — clearance whole-tree still **NO** |

**Recommendation:** Do **not** invent whole-tree archive; do **not** mark Multi-experiment Complete; Continuity work is org-repo FAW amendment + leftover finish-sync only.

---

## 5. Must-read paths

- `sessions/2026.09.11-1122/01-prompt-betterment/refined-prompt.md` + `notes.md`
- `sessions/2026.09.11-1038/05-git/log.md`, `SESSION.md`, `06-audit/report.md`, `07-self-improvement/proposals.md`
- `.cursor/skills/full-agent-workflow/SKILL.md`
- `.cursor/agents/orchestrator.md`, `git-manager.md`
- `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
- `sessions/_templates/SESSION.md`
- `AGENTS.md`, `.cursor/rules/full-agent-workflow.mdc`
- `program/ROADMAP.md`, `program/git-strategy-workspace-hazards.md`, `catalogue/INDEX.md`
