# Refined prompt — Cycle 17 (BINDING)

**Status:** BINDING — Continuity locked · `ready_for_researcher: yes`  
**stage_1_hold:** yes — same-run implement **FORBIDDEN**  
**mutation_class:** `docs_only` (org-repo FAW definition + allowlisted finish-sync; zero WorkSpace corpus moves / zero WorkSpace remote-config)

### Continuity locks (do not re-litigate)

| ID | Lock |
| --- | --- |
| **Q1** | **A** — optional/early mid-cycle `git-manager` for implementer work **+ mandatory final closing pass** after self-improver that stages/commits/pushes `06-audit/**`, `07-self-improvement/**`, `.cursor/**` cycle edits, and `SESSION.md` close (same allowlist + GfW/GCM rules) |
| **Q2** | **A** — Cycle 16 leftover finish-sync is the **first STAGE 2 git pass** |
| **Q3a** | **A** — carry taxonomy/must-preserve **waive re-litigation** (proposed-ratified / draft — not final sign-off) |
| **Q3b** | **A** — carry TNA dirty **defer / NO_AUTO_COMMIT** |

---

## Goal

Amend the Full Agent Workflow (FAW) so **`git-manager` owns all cycle outputs end-to-end**: after self-improvement, a **mandatory final closing pass** stages, commits, and pushes every cycle artifact that today’s mid-cycle (phase-5) push leaves behind — especially `06-audit/**`, `07-self-improvement/**`, `.cursor/**` cycle edits, and `SESSION.md` close — using the same allowlist and Git-for-Windows / GCM rules.

Apply that amended workflow to **this** cycle (Cycle 17): after Hermes plan-gate **yes**, (1) finish-sync leftover Cycle 16 allowlisted dirt as the **first STAGE 2 git pass**, (2) implement the workflow amendment, (3) run Cycle 17 under the amended order including the **mandatory final closing pass**.

ROADMAP remains Multi-experiment **`WorkSpace` only** (not Complete). Primary work is org-repo workflow amendment — **not** a WorkSpace move.

---

## Constraints

- **Orchestrator-only** realization via FAW phases; prompt-betterment / researcher / planner do not implement.
- **STAGE 1 ONLY** until Hermes: prompt-betterment → researcher → planner → **stop at Hermes plan gate**. Do **not** same-run implement even if plan is `docs_only` + `ready_to_implement: yes`. STAGE 2 resumes **same session folder** (`sessions/2026.09.11-1122/`) after gate yes (+ amendments).
- Plan must include a **“What the user is approving”** intent-preview block suitable for Hermes.
- **Q1=A:** keep optional mid-cycle git pass; **require** mandatory final closing pass after self-improver.
- **Q2=A:** STAGE 2 first git action = Cycle 16 leftover allowlisted finish-sync, then amend FAW, then Cycle 17 phases with final close.
- **Q3a=A / Q3b=A:** do not re-litigate taxonomy/must-preserve; do not auto-commit TNA / non-allowlist dirt.
- **Zero** WorkSpace corpus moves/renames/deletes; **zero** inventing whole-tree archive; **never** mark Multi-experiment **Complete**; **never** jump Primary next / Special git; **never** reopen Medium / archived Multi-experiment peers as sources.
- Git ops: **this org-repo git root only**; allowlisted paths only; no secrets in commits/logs; no force-push; prefer GfW absolute `git.exe` when PATH git lacks GCM.
- Taxonomy language if mentioned: **proposed-ratified — ready for user sign-off**; must-preserve **draft — not auto-locked**.
- Continuity approval ≠ Hermes plan-gate execute.

---

## Context pointers

- Prior complete session (leftovers): `sessions/2026.09.11-1038/` — at least `06-audit/`, `07-self-improvement/`, `SESSION.md`; plus dirty `.cursor/**` agents/skill/rules and `sessions/_templates/**` as applicable
- This session: `sessions/2026.09.11-1122/`
- Continuity answers: `01-prompt-betterment/notes.md`
- ROADMAP: `program/ROADMAP.md` (Multi-experiment remaining WorkSpace only)
- Strategy artifact: `program/git-strategy-workspace-hazards.md` (EXISTS — honor Next FAW lock hint; do not force-move)
- FAW definition surfaces (amend as needed): `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/agents/orchestrator.md`, `.cursor/agents/git-manager.md`, `.cursor/skills/full-agent-workflow/references/handoff-templates.md`, `sessions/_templates/**` (incl. SESSION template), `AGENTS.md`, `.cursor/rules/full-agent-workflow.mdc`
- Publish/allowlist rules: skill Critical auth/dirty policy; `references/publish-cycle.md` as needed for STAGE 2 git passes

---

## Acceptance criteria

### Continuity (done)

- [x] Q1=A, Q2=A, Q3a=A, Q3b=A locked in `notes.md` Answers (Source `user reply`)
- [x] This refined prompt is BINDING (no pending Continuity)

### STAGE 1 (this run — research → plan → Hermes hold)

- [ ] Research maps current phase order vs orphan-after-push problem; inventories Cycle 16 leftover allowlisted paths; lists exact FAW files to amend
- [ ] Plan is **`docs_only`**; includes Hermes **“What the user is approving”** intent-preview
- [ ] Plan encodes **Q1=A**: optional mid-cycle git + **mandatory final closing pass** after self-improver
- [ ] Plan sequences STAGE 2: **(1)** Cycle 16 leftover finish-sync (**Q2=A**, first git pass) → **(2)** implement FAW amendment → **(3)** Cycle 17 under amended order including final git-manager after self-improver
- [ ] Orchestrator stops at Hermes plan gate (`stage_1_hold: yes`); same-run implement **FORBIDDEN**

### STAGE 2 (after Hermes yes only)

- [ ] **First git pass:** commit/push leftover Cycle 16 allowlisted artifacts (`sessions/2026.09.11-1038/06-audit/`, `07-self-improvement/`, that `SESSION.md`; relevant `.cursor` agents/skill/rules edits; `sessions/_templates/*` if dirty) — same allowlist + GfW/GCM
- [ ] **Workflow definition amended** so git-manager runs a **final closing pass AFTER self-improver** that stages/commits/pushes: `06-audit/**`, `07-self-improvement/**`, `.cursor/**` cycle edits, `SESSION.md` close — same allowlist + GfW rules. Surfaces include as needed: skill, orchestrator, git-manager agent, handoff-templates, SESSION template, `AGENTS.md` / rules
- [ ] Mid-cycle phase-5 remains **optional/early** for implementer work (**Q1=A**); final close is **mandatory** when allowlisted 06/07/SESSION (or cycle `.cursor`) dirt remains
- [ ] Handoffs / SESSION template / AGENTS.md / rules updated so orchestrator cannot mark session **`complete`** while the final closing pass was skipped and allowlisted late dirt remains
- [ ] Cycle 17 uses the amended order and ends with a successful final closing pass (or fail-closed `blocked` with honest `blocker_type` — never false complete)
- [ ] **Zero** WorkSpace corpus moves; Multi-experiment **not** marked Complete; ROADMAP Next FAW lock hint still WorkSpace-only residual

### Verification (STAGE 2)

- [ ] Diff of amended FAW files shows final closing pass in skill + orchestrator + git-manager + handoff/SESSION templates (and AGENTS/rules as needed)
- [ ] After Cycle 17 close: allowlisted 06/07/SESSION (and this cycle’s `.cursor` edits) are committed and pushed, or session is honestly `blocked`
- [ ] No non-allowlist / secret paths staged; TNA dirt untouched (**Q3b=A**)

---

## Out of scope

- WorkSpace path moves, whole-tree archive, Appendix A re-execute, remote-config on nested WorkSpace remotes
- Marking Multi-experiment Complete or jumping Primary next / Special git
- Re-opening Medium / Early / archived Multi-experiment peers
- Final taxonomy/must-preserve user sign-off (waived re-litigation — **Q3a=A**)
- Committing TNA (or other non-allowlist) dirty working trees (**Q3b=A**)
- Same-run STAGE 2 / implement before Hermes plan-gate yes
- Deep catalogue/INDEX redesign beyond honesty required by zero-move Continuity
- Changing Q1 to final-only or mid-mandatory-only

---

## Good vs bad outcomes

| Good | Bad |
| --- | --- |
| After self-improver, git-manager closing pass commits audit + self-improve + SESSION close | Cycle “complete” with 06/07 only on disk, never pushed |
| Cycle 16 leftovers finished first in STAGE 2, then workflow fixed, then Cycle 17 final close | Workflow docs say “final close” but Cycle 16 orphans remain |
| Hermes sees clear intent-preview; user approves once; then STAGE 2 | Same-run implement despite STAGE 1 hold |
| WorkSpace untouched; row still Remaining WorkSpace only | Accidental Complete / Primary next / force-move |

---

## Notes for downstream

- **Researcher:** FAW definition surfaces + Cycle 16 leftover path inventory; do not deep-solve WorkSpace hazards.
- **Planner:** Encode Q1=A / Q2=A explicitly; mandatory final close; STAGE 2 order; Hermes intent-preview; `ready_to_implement` may be yes but **orchestrator still holds** for Hermes (`stage_1_hold: yes`).
- **Implementer / git-manager:** only after Hermes gate yes.
