# Research brief — Cycle 17

**Session:** `sessions/2026.09.11-1122/02-research/`  
**Goal:** Map FAW orphan-after-phase-5 gap; inventory Cycle 16 allowlisted leftovers; recommend mid+final git-manager design; confirm WorkSpace unmoved.  
**mutation_class:** `docs_only` · **STAGE 1 hold** · zero WorkSpace corpus moves  
**Continuity:** Q1=A mid+final · Q2=A leftover finish-sync first · Q3a=A taxonomy waive · Q3b=A TNA defer

---

## Recommended approach options (max 3)

### Option A — **Recommended:** Mid optional + mandatory final (Q1=A) + STAGE 2 leftover-first (Q2=A)

1. **STAGE 2 first git pass:** finish-sync Cycle 16 allowlisted orphans (see stage set below).  
2. **Amend FAW** surfaces so orchestrator always runs git-manager **after self-improver** when allowlisted late dirt remains; mid phase-5 stays optional/early.  
3. **Run Cycle 17** under amended order ending with successful final close (or honest `blocked`).

| Pros | Cons |
| --- | --- |
| Matches locked Continuity; fixes root cause in law + clears existing orphans | Two git launches per mutating cycle; possible tiny post-final log dirt (Low) |
| Fail-closed: cannot mark `complete` with orphaned 06/07/SESSION | Must update several definition surfaces for consistency |

### Option B — Final-only (reject Continuity)

Drop mid-cycle git; only close at end. **Rejected:** Continuity **Q1=A** locks mid+final.

### Option C — Docs-only amendment without leftover finish-sync (reject Continuity)

Amend workflow text but leave Cycle 16 orphans dirty. **Rejected:** Continuity **Q2=A**.

---

## leftover_paths summary

**Authoritative probe:** GfW `…\Git\cmd\git.exe`; `main` == `origin/main` (0/0).

### STAGE 2 first-pass stage set (proposed — all allowlisted)

```
sessions/2026.09.11-1038/05-git/log.md
sessions/2026.09.11-1038/06-audit/report.md
sessions/2026.09.11-1038/07-self-improvement/audit-realization.md
sessions/2026.09.11-1038/07-self-improvement/backlog.md
sessions/2026.09.11-1038/07-self-improvement/changes-applied.md
sessions/2026.09.11-1038/07-self-improvement/proposals.md
sessions/2026.09.11-1038/SESSION.md
.cursor/agents/auditor.md
.cursor/agents/implementer.md
.cursor/agents/orchestrator.md
.cursor/agents/prompt-betterment.md
.cursor/agents/researcher.md
.cursor/skills/full-agent-workflow/SKILL.md
AGENTS.md
sessions/_templates/03-plan.md
sessions/_templates/SESSION.md
```

**Optional later (allowlisted, not Cycle 16 core):** `?? sessions/2026.09.11-0859/`, `?? sessions/2026.09.11/` — plan may include or defer.  
**Exclude from first pass:** `?? sessions/2026.09.11-1122/` (this cycle).  
**Unrelated / Q3b:** no TNA paths in org-repo porcelain; nested TNA remains NO_AUTO_COMMIT.

---

## workflow_files_to_edit

1. `.cursor/skills/full-agent-workflow/SKILL.md` — dual git steps; Done/complete gate  
2. `.cursor/agents/orchestrator.md` — mid + mandatory final; Completion fail-closed  
3. `.cursor/agents/git-manager.md` — mid/final modes; late stage set  
4. `.cursor/skills/full-agent-workflow/references/handoff-templates.md` — final closing handoff  
5. `sessions/_templates/SESSION.md` — workflow step + no-complete-with-late-dirt note  
6. `AGENTS.md` — insert git-manager; mid+final law  
7. `.cursor/rules/full-agent-workflow.mdc` — same dual-pass + complete gate  
8. Optional: `sessions/_templates/05-git-log.md` — mid/final sections  

---

## recommended_mid_final_design notes

- **Mid (phase 5, Q1 optional/early):** After implementer; stage implementer outputs + early session seeds; push when cycle has file changes (existing permanent-phase rules).  
- **Final (mandatory after self-improver):** When allowlisted dirt remains in `06-audit/**`, `07-self-improvement/**`, `SESSION.md` (close), and/or cycle `.cursor/**` (agents/skill/rules) / other allowlist cycle paths → launch git-manager again; same allowlist + GfW/GCM; explicit path stage; push; verify ahead/behind.  
- **Complete gate:** Orchestrator must **not** set `SESSION.md` Status `complete` if final closing pass was skipped while that late allowlisted dirt remains; on push/auth/unrelated failure → `blocked` + `blocker_type` (never false complete).  
- **Known Low:** Post-final touch to the final git log may stay dirty once — same “single-commit vs finalize” tradeoff; auditor grades Low if policy says so.  
- **STAGE 2 order (binding):** (1) Cycle 16 leftover finish-sync → (2) implement FAW amendment → (3) Cycle 17 phases under amended order including final close.  
- **WorkSpace:** verify-only; still at `C:\Project\WorkSpace`; clearance whole-tree **NO**; never Complete Multi-experiment / invent archive.

---

## Required facts

- Phase order today is implementer → **git-manager** → auditor → self-improver → Close; **no** final git.  
- Cycle 16 `9f09dc7` pushed before real 06/07/SESSION/self-improve `.cursor` edits; session still marked complete.  
- Allowlist includes `sessions/**`, `.cursor/agents/**`, `.cursor/skills/full-agent-workflow/**`, `.cursor/rules/**`, `AGENTS.md`, `sessions/_templates/**`.  
- Cycle 16 git log misclassified `AGENTS.md` + templates as unrelated.  
- PATH git = MSYS; agent publish must use GfW absolute path (helper `manager`).  
- WorkSpace still root; ROADMAP Remaining WorkSpace only; strategy artifact exists.

## Unknowns (non-blocking for STAGE 1 plan)

- Whether STAGE 2 first pass should also add untracked `2026.09.11-0859/` and `2026.09.11/` (planner Choose/default).  
- Exact numbering of SESSION checklist (9 vs 10) after inserting final git — cosmetic; law matters more than number.  
- Whether final pass writes to same `05-git/log.md` (append section) vs separate `05-git-final` — prefer append section in existing `05-git/log.md` unless planner prefers otherwise.

## Risks and blockers

| Risk | Mitigation |
| --- | --- |
| Same-run implement despite STAGE 1 hold | Orchestrator stop at Hermes; `stage_1_hold: yes` |
| Leaving Cycle 16 orphans while only editing docs | Q2=A first git pass |
| False complete after Cycle 17 | Complete gate in skill/orchestrator/SESSION template |
| Staging `1122` mid-cycle in leftover pass | Exclude from first-pass set |
| TNA auto-commit | Q3b=A; not in org porcelain |
| Accidental WorkSpace Complete / move | Zero corpus moves; verify-only |

**blockers:** **none** for STAGE 1 research→plan (auth green for later STAGE 2 git via GfW+GCM; no unrelated org-repo dirt blocking allowlist finish-sync; WorkSpace not a blocker for this `docs_only` goal).

---

## Canonical references

- Local: `codebase-findings.md`, `online-findings.md`, refined prompt + notes in `01-prompt-betterment/`  
- Cycle 16: `sessions/2026.09.11-1038/05-git/log.md`  
- Online: Cursor [agent best practices](https://cursor.com/blog/agent-best-practices), [Hooks](https://cursor.com/docs/hooks)

---

## Return summary (orchestrator)

```markdown
## Research result
- research_brief_path: sessions/2026.09.11-1122/02-research/research-brief.md
- recommended_option: A (mid optional + mandatory final; STAGE 2 leftover-first)
- blockers: none
- leftover_paths: see STAGE 2 first-pass stage set above (16 allowlisted paths; exclude 1122; optional prior ?? sessions)
- workflow_files_to_edit: SKILL.md, orchestrator.md, git-manager.md, handoff-templates.md, SESSION template, AGENTS.md, full-agent-workflow.mdc (+ optional 05-git-log template)
- recommended_mid_final_design: keep phase-5 mid; mandatory final after self-improver for 06/07/SESSION/.cursor; no complete with late allowlisted dirt
- must_read_paths:
  - sessions/2026.09.11-1122/01-prompt-betterment/refined-prompt.md
  - sessions/2026.09.11-1038/05-git/log.md
  - .cursor/skills/full-agent-workflow/SKILL.md
  - .cursor/agents/orchestrator.md
  - .cursor/agents/git-manager.md
  - .cursor/skills/full-agent-workflow/references/handoff-templates.md
  - sessions/_templates/SESSION.md
  - AGENTS.md
  - .cursor/rules/full-agent-workflow.mdc
  - program/ROADMAP.md
```
