---
name: full-agent-workflow
description: >-
  Runs the project full agent cycle with a pure orchestrator that only delegates
  to prompt-betterment, researcher, planner, implementer, optional/early mid-cycle
  git-manager, auditor, mandatory self-improver, then mandatory final closing-pass
  git-manager. Use when the user asks for the full agent workflow, /full-agent-workflow,
  orchestrated delivery, or any non-trivial multi-phase goal in this organisation repo.
---

# Full agent workflow

## Role

When this skill applies, **you are the orchestrator**. Follow `.cursor/agents/orchestrator.md`.

- Do not research, plan, implement, or audit the user goal yourself.
- Create the dated session folder, delegate each phase subagent, connect outputs, update `SESSION.md`.
- Always end with `self-improver`, then a **final closing-pass** `git-manager` when allowlisted late dirt remains (before marking `complete`).

## Trigger

User invokes `/full-agent-workflow`, `@orchestrator`, or states a goal that needs the full cycle.

## Steps

Copy and track:

```
Workflow progress:
- [ ] 0. Session bootstrap (sessions/yyyy.mm.dd/)
- [ ] 1. prompt-betterment → 01-prompt-betterment/
- [ ] 2. researcher → 02-research/
- [ ] 3. planner → 03-plan/
- [ ] 4. User plan gate → then implementer (mandatory if plan mutates corpus FS)
- [ ] 5. implementer → 04-implementation/
- [ ] 6. git-manager (mid) → 05-git/ (optional/early for implementer work — same allowlist + GfW/GCM; not a substitute for final close)
- [ ] 7. auditor → 06-audit/ (rework loop if critical fail)
- [ ] 8. self-improver → 07-self-improvement/  (MANDATORY)
- [ ] 9. git-manager (final closing pass) → 05-git/ (MANDATORY when allowlisted late dirt remains: 06-audit/**, 07-self-improvement/**, SESSION.md close, cycle .cursor/** / other allowlisted cycle dirt)
- [ ] 10. Close SESSION.md
```

### 0. Session bootstrap

1. **Resume check:** If user names an **incomplete** (`in_progress` / unchecked later phases) session as prior/resume/continue/**retry** → **reuse that folder** and continue from the next incomplete phase; do **not** open a parallel dated folder for the same cycle. Completed prior for Continuity only → new folder as usual. If implementer was interrupted but `04-implementation/` artifacts already show **complete**, **skip** re-launching implementer — resume at mid git (or whatever phase is still open).
2. Else date folder: `sessions/yyyy.mm.dd` (collision → `sessions/yyyy.mm.dd-HHMM`).
3. Create phase subfolders `01`–`07` as named in [session-structure.md](references/session-structure.md) (skip on resume if already present).
4. Seed files from `sessions/_templates/` on **new** sessions only — never overwrite finished phase artifacts on resume.
5. Write/update `SESSION.md` with raw goal + checklist. If this is a **program cycle**, fill Program framing (cycle id, docs-only vs mutation, `program/ROADMAP.md` pointer, **locked ROADMAP row**, prior session + **pending user gates**). One session per cycle; do not start moves inside a docs-only FAW after it passes.
6. If the user did not name the row, **orchestrator chooses** the ROADMAP primary-next (or next sensible slice), documents it, and passes it to prompt-betterment — do not re-litigate mid-cycle. When a multi-batch row is already **Complete**, lock **Primary next →** — do not reopen the finished row. When Medium wrappers are **Complete**, lock **Multi-experiment** (small first subset + multi nested-git caution + SSH path-only Continuity) — do not reopen Medium. When the row is **in progress** (partial subset done), re-lock the **same** row scoped to **remaining** names — do not jump Primary next or re-propose already-moved folders (e.g. Multi-experiment remaining `PWAExemple` + `WorkSpace`; keep `WorkSpace` fail-closed / git-strategy candidate until cleared). When only **movable soft-deferred** names remain (**nearly complete**), lock those named remaining and default Continuity to **finalize** them (do not re-soft-defer by default); after last move → Complete → Primary next. When only **fail-closed / git-strategy** remaining (e.g. Multi-experiment **`WorkSpace` only**): lock that name; **never force-move**; **never** mark Complete or jump Primary next while it remains; **never** reopen Medium / archived Multi-experiment peers as sources. **Pre–strategy:** default Continuity = research then defer **unless** hazards cleared **or** dedicated git-strategy Continuity; **repeated research+defer is valid**. **Post–hazard-strategy docs** (`program/git-strategy-workspace-hazards.md` exists): point phases at that artifact; default Continuity = **continue strategy** (docs) **or** explicit **Appendix A execute** Continuity (plan gate required) — **do not** re-default to pure Cycle 9 defer after strategy docs; **do not** invent whole-tree archive; “solve hazards” after docs ≠ Complete. **Named Continuity B / stop docs_only re-attest** → lock `fs_mutation` Appendix A **and/or** remaining live-hazard remote-config; do not steer Continuity A theater. **Anti-loop / no material delta** → **`escalate_break_loop`** (not Continuity A); Continuity **X** = next FAW XL/git-strategy + plan gate; still WorkSpace only. **Continuity X dedicated cycle:** STAGE 1 hybrid gate **D/M/D+M** (`ready_to_implement: no` until answer); STAGE 2 same-session resume; **D+M** = docs first then held `path_batch` (OS-IA-first default); **OS-IA alone never Completes** Multi-experiment / never Primary next; post–OS-IA Next FAW = **WorkSpace only (TNA)** + continue Continuity X clearance / keep-at-root. **Post–Appendix A:** still lock `WorkSpace` only. **Post–multi-remote / remote-config clear:** still lock `WorkSpace` only — never Complete / Primary next while it remains; never invent whole-tree archive. After implementer shrinks remaining, refresh SESSION Program framing lock to post-move remaining names.

### 1–7. Delegate

Launch each custom subagent with a handoff matching [handoff-templates.md](references/handoff-templates.md).

| Phase | Agent name |
| --- | --- |
| Prompt betterment | `prompt-betterment` |
| Research | `researcher` |
| Plan | `planner` |
| Implement | `implementer` |
| Git management | `git-manager` |
| Audit | `auditor` |
| Self-improve | `self-improver` |

`git-manager` owns local+remote Git health — stage/commit cycle work (never unrelated dirt or secrets), push, branch creation, and **merge into main as the default outcome** (prioritize merging over leaving branches separated; only verified, conflict-free branches merge; never force). **Dual-pass law (Q1=A):**

- **Mid (phase 6, optional/early):** After implementer — commit/push implementer outputs and early session seeds when the cycle has file changes. Mid is **not** a substitute for the final close.
- **Final closing pass (phase 9, mandatory when late allowlisted dirt remains):** After self-improver — stage/commit/push at least `06-audit/**`, `07-self-improvement/**`, `SESSION.md` (close), cycle `.cursor/**` edits, and other allowlisted cycle dirt. Prefer appending mid/final sections in the same `05-git/log.md` (write final log section **before** the final commit when practical). Tiny post-final log dirt may remain once (known Low).
- **Leftover / finish-sync:** Explicit path-set pass when Continuity/plan names orphaned allowlisted paths from a prior cycle (same allowlist + GfW/GCM).
- Skip git entirely only for pure `docs_only` zero-mutation cycles with a recorded zero-mutation attestation **and** no allowlisted late dirt.

Handoff matches [handoff-templates.md](references/handoff-templates.md) and `.cursor/agents/git-manager.md`.

Pause for user answers during prompt-betterment. If answers include **Choose**, Continuity bare **yes→defaults**, or pack items stay **unanswered** after a partial reply with disclosed defaults, prompt-betterment must decide and document — do not forward “Choose”/blanks downstream. For publish / git add-commit-push goals, use [publish-cycle.md](references/publish-cycle.md) (question pack + org-repo git-root boundary). For **git pull / sync-from-origin** goals, use [pull-cycle.md](references/pull-cycle.md) (same pattern; FAW default = allowlisted dirty autonomy + `--ff-only`; **when behind+allowlisted dirty → stash→ff-only→pop** (Q3c); commit-then-pull when not behind; abort only for unrelated dirty; GfW for gate+commit/stash+pull).

**Informed consent (all user pauses):**

- Do **not** assume the user knows FAW jargon (`taxonomy`, `must-preserve`, `plan gate`, `fs_mutation`, `fail-closed`, …).
- Every clarifying question and every orchestrator-relayed gate must include: short **plain-language explanation** (what is asked + what “yes” commits to) and **pros / cons or tradeoffs** for options.
- Planner `fs_mutation` plans must include a “What the user is approving” intent-preview block the orchestrator can relay.

**User plan gate (step 4):**

- **Mandatory** when the plan is **`fs_mutation`**: moves/renames/deletes (or other corpus / catalogue-backed path mutations) **or** **remote-config** (e.g. `git remote remove` on a live nested `.git`) — wait for explicit per-batch approval before implementer. Zero path moves does **not** waive the gate for remote-config.
- **`docs_only` (no mandatory gate):** org-repo scaffolding creates (new folders/READMEs/docs/index inside this organisation git root) and charter/index cycles with **zero** corpus moves — proceed when `ready_to_implement: yes` (still pause if the user asked to review the plan). Creating paths in the org repo ≠ `fs_mutation`.
- **`product_settings` (no mandatory corpus gate):** editor/IDE extension install-switch, settings keys, **local installed-extension `dist/`/`src/` patches** (document **re-apply after Marketplace/Open VSX update**), and/or local evidence fixtures outside the catalogue — **not** corpus `fs_mutation`. Plan-gate **n/a**; proceed when `ready_to_implement: yes` (same-run). Soft **Reload window** after install/switch **or after dist patch** (and Marketplace UI only if CLI cannot install and no plan fallback) — tip once; do not treat Reload as Critical or invent recurring user chores. Python 42-header + flake8 Continuity: prefer **≤79 generator** over Norminette-80 / ignore-first.
- **STAGE 1 / same-run auto-continue:** After planner, if **`docs_only` or `product_settings`** + **`ready_to_implement: yes`** + no plan gate → continue implement → mid git (as appropriate) → audit → self-improver → **final closing-pass git** → Close **in the same run** (do not wait for a separate user “go” unless they asked to review). If `fs_mutation` (incl. remote-config), **`escalate_break_loop`**, or not ready → stop at plan / Continuity gate / blocking questions.
- **`ready_to_implement: no` / escalate close:** After Continuity/plan answers for **`escalate_break_loop`** (or any ready-no with no product work): **skip implementer + mid git**; still run **auditor → self-improver → final closing-pass git** → Close. Orchestrator **Step 3 bookkeeping:** record Continuity choice in notes + SESSION Next FAW hint + ROADMAP Next FAW hint (zero corpus FS). Continuity **X** → next FAW = dedicated XL/whole-tree git-strategy (still WorkSpace only / not Complete; mandatory plan gate before path mutation).
- **STAGE 1 hold → STAGE 2 resume:** When Continuity says STAGE 1 = phases 1–3 only for `fs_mutation` **or** Continuity **X** hybrid **D/M/D+M**, stop after planner. On later plan-gate **yes** / **D** / **M** / **D+M** (+ amendments / destination), **resume the same session** for implement → mid git → audit → self-improver → **final closing-pass git** → Close — do not bootstrap a parallel folder. Apply amendments in the implementer handoff; **D+M** = docs first then path_batch. Escalate **X/P/N** usually starts a **new** cycle under that Continuity (not silent whole-tree execute from the escalate plan); once inside dedicated Continuity X, STAGE 2 is same-folder resume.
- **Named Continuity B:** User names Continuity B / Appendix A execute / stop docs_only re-attest → lock `fs_mutation` path (scoped isolation **and/or** remaining live-hazard remote-config); do not steer toward Continuity A docs_only theater. Continuity B ≠ execute (gate still mandatory). **Anti-loop / no material delta:** research `concrete_advance_candidate: none` → planner **`escalate_break_loop`** (not Continuity A). **Post–multi-remote clear:** still lock `WorkSpace` only — never Complete while it remains; never invent whole-tree archive.
- Never treat a prior cycle’s approval as approval for a new batch.
- **Early/simple / first move:** also confirm taxonomy final sign-off or explicit waiver, and must-preserve draft review or waiver, before launching implementer on `fs_mutation` — with the same explanation + tradeoffs rule (not jargon-only).

### Rework

- Audit `rework_needed: yes` with Critical and `rework_owner: implementer` (or earlier phase) → relaunch that phase, then re-audit.
- Audit Critical with `rework_owner: user` (true credential gaps / push auth / **unrelated dirty-tree cleanup before pull**) → **do not** relaunch implementer; set `SESSION.md` to `blocked` with remediation by `blocker_type`; still run `self-improver`. Allowlisted session/FAW-meta dirt is agent auto-commit territory — not user cleanup by default.
- Never report the cycle as complete when Critical acceptance criteria remain unmet (including unmet pull-sync AC after correct unrelated dirty-abort, expected non-ff, or expected merge-conflict abort — process may **pass**, session stays **`blocked`**).
- Always run `self-improver` after audit (pass, fail, or blocked).
- **Orchestrator bookkeeping:** when implementer returns `blocked` / `aborted_dirty` / `non_ff` / `blocked_conflict`, flip `SESSION.md` to `blocked` **immediately** (do not leave `in_progress` until audit).
- **Mid-cycle SESSION flip:** before launching the next phase, mark the completed phase done in **Workflow progress + Phase checklist + Phase summaries** (status + one-liner) — especially after mid git-manager → before auditor, after auditor persist → before self-improver, and after final git-manager → before Close. Omitting Phase summaries while Workflow is checked = mid-cycle lag (auditor Low).
- **Auditor report persist:** Auditor is **`readonly: true`** — expect Write to fail. After auditor returns, **always** ensure `06-audit/report.md` holds the full report; **orchestrator writes** the returned body when the file is missing/stub/outdated (session bookkeeping, not product work), then updates `SESSION.md` audit verdict before self-improver.

### Critical: auth / push / pull (Windows HTTPS Option A)

- **Dual preflight** before commit+push **or** pull: remote scheme + tracking; **agent** git path / `credential.helper` / prefer **Git for Windows** when PATH `git` is MSYS without GCM; optional user-terminal note; `gh` present/absent recorded but **not** sole credential signal when GCM works.
- Invoke agent push/pull with GfW absolute `git.exe` when needed; use the **same** binary for dirty `status` gate, allowlist commit, and pull; do not require machine-wide PATH rewrite.
- **Dirty policy (FAW default):** allowlisted paths only (`sessions/**`, `.cursor/skills/full-agent-workflow/**`, `.cursor/agents/**`, `.cursor/rules/**`, `AGENTS.md`, `sessions/_templates/**`). **If behind remote + allowlisted dirty:** stash → `--ff-only` → stash pop (then optional allowlist commit). **If not behind:** allowlist auto-commit then `--ff-only`. Abort only for unrelated dirty → `dirty_working_tree`. Post-step non-ff → `other`/`non_ff`; content-conflict abort under Q3b=A → `other`/`merge_conflict`; keep WIP/stash recoverable; no merge/rebase unless user changes Q2; no silent conflict resolve unless Q3b=B (allowlist-only). **Finish-sync continuity** (prior allowlist-only `merge_conflict` or user said merge+resolve): lock Q3b=B + R1 `combined-best` (agent-owned; diminish user workload). Never claim pull success on block.
- Fail-closed: agent push/pull/preflight fail, unrelated dirty-abort, non-ff refuse, or merge-conflict abort → session `blocked` (never `complete`); `blocker_type` **`dirty_working_tree`** | **`agent_environment`** | **`user_credentials`** | **`other`** (e.g. `non_ff` or `merge_conflict`); do not relaunch implementer until remediated; **self-improver still runs**.
- **Never** log secrets, PATs, credential fill passwords, or full env dumps (`GITHUB_TOKEN` existence boolean-only).
- Fallbacks only if GfW+GCM fails after PATH/git fix: `gh auth git-credential`, or SSH remote + key (do not rewrite `origin` to SSH by default); Cursor Run Modes / Legacy Terminal if sandbox blocks GCM.
- **Single-commit vs session finalize:** write pre-push `04-implementation` notes before commit; post-push hash/status lines cannot be in that commit — leave them dirty (known tradeoff) or allow a tiny follow-up session-only commit if the plan/user permits. Auditor: expected dirty finalize = Low, not rework.

### Done criteria

- All phase folders have their primary artifacts (or explicit blocked notes) — including a real `06-audit/report.md` (orchestrator-persisted if needed).
- `07-self-improvement/changes-applied.md` exists.
- **Final closing-pass gate:** If allowlisted late dirt remains (`06-audit/**`, `07-self-improvement/**`, `SESSION.md` close, cycle `.cursor/**` / other allowlisted cycle dirt), the final `git-manager` pass must have run and returned `complete` (committed+pushed) **or** honest `blocked` with `blocker_type`. **Do not** mark `SESSION.md` Status `complete` while that late allowlisted dirt remains after a **skipped** final pass. Mid-only push does **not** satisfy this gate.
- User receives session path + audit verdict + self-improvement summary (and blocked reason if any).

## References

- [session-structure.md](references/session-structure.md)
- [handoff-templates.md](references/handoff-templates.md)
- [publish-cycle.md](references/publish-cycle.md) — org-repo publish question pack + git-root boundary
- [pull-cycle.md](references/pull-cycle.md) — org-repo pull/sync question pack + order-aware allowlisted dirty defaults (Q3c stash when behind) + GfW gate
- Agents: `.cursor/agents/*.md`
- Best practices: `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`
