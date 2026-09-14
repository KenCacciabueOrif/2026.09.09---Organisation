# AGENTS.md

Portable project law for this organisation repo (Cursor and other agent harnesses).

## Default workflow

For non-trivial goals, run the **full agent workflow**:

1. Act as **orchestrator only** (see `.cursor/agents/orchestrator.md` and skill `full-agent-workflow`).
2. Delegate in order: `prompt-betterment` → `researcher` → `planner` → `implementer` → `git-manager` (mid, optional/early) → `auditor` → **`self-improver` (mandatory)** → **`git-manager` (final closing pass, mandatory when allowlisted late dirt remains)**.
3. Document everything under `sessions/yyyy.mm.dd/` (collision: `yyyy.mm.dd-HHMM`). If the user names an **incomplete** (`in_progress`) session as prior/resume, **resume that folder** instead of creating a parallel session for the same cycle.

Do not skip self-improvement after a cycle. Do not mark session `complete` while final closing-pass git was skipped and allowlisted late dirt (`06-audit/**`, `07-self-improvement/**`, `SESSION.md` close, cycle `.cursor/**`) remains — mid-only push does not satisfy the gate; honest final `blocked` → session `blocked`.

## Session docs

- Templates: `sessions/_templates/`
- Layout: `.cursor/skills/full-agent-workflow/references/session-structure.md`

## Agent roles

| Agent | Does | Does not |
| --- | --- | --- |
| orchestrator | Session bootstrap, handoffs, routing | Research, plan body, implement, audit |
| prompt-betterment | Questions + prompt refine + prompt-engineering search | Domain solution design |
| researcher | Codebase + online evidence | Plan / code |
| planner | `plan.md` | Code |
| implementer | Execute plan | Scope expansion |
| git-manager | Mid / final / leftover stage-commit-push (allowlist + GfW/GCM) | Product code, plan edits, audit |
| auditor | Verify vs criteria | Silent fixes |
| self-improver | Audit process; improve agents/skills/rules/templates | Ignore end-of-cycle |

## Commands / verification

- Prefer explicit acceptance criteria in the plan before implementation.
- After implementation, prefer tests/typecheck/lint named in the plan.
- Prefer revert + better plan over compounding a bad run.
- **Dual git-manager (mid + final):** Mid after implementer is optional/early for implementer work. **Mandatory final closing pass** after self-improver stages/commits/pushes allowlisted late dirt (`06-audit/**`, `07-self-improvement/**`, `SESSION.md` close, cycle `.cursor/**` / other allowlisted cycle dirt) under the same allowlist + GfW/GCM. Prefer one `05-git/log.md` with mid/final sections. Orchestrator must not mark `complete` if final pass was skipped while that dirt remains.
- **Multi-cycle / corpus FS:** Prefer one FAW session per program cycle (`program/ROADMAP.md` when present). Orchestrator locks the ROADMAP row (chooses if user said “next”) and carries pending sign-off gates. When a multi-batch row is **Complete**, next lock = ROADMAP **Primary next →** (do not reopen the finished row). After Medium **Complete**, lock **Multi-experiment** (small first subset; multi nested-git caution; SSH-origin path-only — no remote rewrite) — do not reopen Medium. While a multi-batch row is **in progress**, next lock = **same row / remaining names** (ROADMAP Notes must show partial progress) — e.g. Multi-experiment after first subset → remaining only (`PWAExemple`, `WorkSpace`; WorkSpace may stay fail-closed / git-strategy). When only **movable soft-deferred** remain (**nearly complete**), lock those names; default Continuity = **finalize** them (do not re-soft-defer by default); after last move → Complete → Primary next. When only **fail-closed / git-strategy** remaining (e.g. **`WorkSpace` only**): lock that name; finalize/move only if cleared **or** dedicated git-strategy — do **not** force-move; do **not** mark Complete or jump Primary next while it remains; do **not** reopen Medium / archived Multi-experiment peers. **Post–docs_only defer pass:** next cycle still locks that remaining name; **repeated research+defer is valid** until cleared or git-strategy Continuity. **Post–hazard-strategy docs** (`program/git-strategy-workspace-hazards.md` exists): still lock `WorkSpace` only; Continuity default = continue strategy from that artifact **or** explicit Appendix A scoped isolation (plan gate) — do not re-default Cycle 9 pure defer after strategy docs; do not invent whole-tree archive; never Complete while WorkSpace remains. **Named Continuity B / stop docs_only re-attest:** lock `fs_mutation` (Appendix A and/or remaining live-hazard **remote-config**); do not steer toward Continuity A theater. **Post–Appendix A / post–multi-remote clear:** still lock WorkSpace only — never Complete while it remains; never invent whole-tree archive. **STAGE 1 hold → STAGE 2 resume** same session after plan-gate yes (+ amendments). Nested-clone `worktree list` on clone paths only (not parent wrappers → outer repo). Nested+parent dirty WT: disclose + NO_AUTO_COMMIT. Plans declare `docs_only` | `product_settings` | `fs_mutation` — `docs_only` includes org-repo scaffolding creates (folders/READMEs) with zero corpus moves; `product_settings` is editor extension/settings/local fixture/**local dist patch** (not corpus; plan-gate n/a; Soft Reload after patch; re-apply after Marketplace; Python 42+flake8 -> prefer <=79 generator over Norminette-80/ignore-first); `fs_mutation` is corpus/catalogue path batches **or** remote-config (`git remote remove` etc.). **User approval is mandatory** before implementer for move/rename/delete **and** remote-config batches (zero path moves ≠ waive gate); **`docs_only` or `product_settings` + `ready_to_implement: yes`** → same-run implement→mid git→audit→self-improve→**final closing-pass git** (no mandatory pause). Resume/**retry** with 04 already complete → skip re-implementer. Auditor is readonly — orchestrator always persists `06-audit/report.md` from the return body. Git roots are atomic unless a dedicated git-strategy plan says otherwise. User **Choose** / Continuity bare **yes→defaults** → prompt-betterment decides and documents. Taxonomy **proposed-ratified** and must-preserve **draft** are not final until user sign-off or explicit waiver; first move / Early-simple fail-closed on those gates.
- **Informed consent asks:** Clarifying questions and plan-gate (or other) approvals must include short **plain-language explanation** (what is asked + what “yes” commits to) and **pros/cons or tradeoffs**. Do not assume the user already knows workflow jargon.
- Goals that require `git push` or `git pull`: early dual preflight (remote + **agent** git/GCM — on Windows prefer Git for Windows when PATH git is MSYS without helper); user terminal success ≠ agent ready; missing `gh` alone ≠ missing credentials when GCM works. Fail-closed: never mark complete if agent push/pull failed, unrelated dirty-aborted, non-ff refused, or merge-conflict aborted; `blocker_type` `dirty_working_tree` (unrelated only) vs `agent_environment` vs `user_credentials` vs `other`/`non_ff` or `other`/`merge_conflict`; still run self-improver. Optional user tip: put Git for Windows `cmd` before MSYS on PATH; agents still invoke GfW via absolute path when needed.
- **Publish / pull / org-repo only:** stage and commit / pull only inside this repo’s git root (`rev-parse --show-toplevel`); never sibling trees under a multi-root workspace. Prompt-betterment uses the publish pack in `.cursor/skills/full-agent-workflow/references/publish-cycle.md` or the pull pack in `references/pull-cycle.md`; unanswered pack items with disclosed defaults → Choose those defaults. FAW dirty default = allowlisted autonomy (`sessions/**`, FAW skill/agents/rules, `AGENTS.md`, `sessions/_templates/**`) + `--ff-only`: **when behind+allowlisted dirty → stash→ff-only→pop** (Q3c); when not behind → allowlist auto-commit then pull; abort only for unrelated dirty → session `blocked`, not false complete. Expected `other`/`non_ff` or `other`/`merge_conflict` → `blocked` + keep WIP/stash (no merge/rebase unless user changes Q2; no silent conflict resolve unless Q3b=B allowlist-only). **Finish-sync continuity** after allowlist-only `merge_conflict` (or user already said merge+resolve): disclosed default **Q3b=B** + R1 **`combined-best`** — agent-owned next cycle; do not dump “user must resolve” for FAW-allowlist conflicts; still fail-closed for non-allowlist. Never claim pull succeeded.
- Single-commit publish: write implementation log **before** commit; post-push hash/status notes may stay uncommitted (known tradeoff) or use a tiny session-only follow-up commit if allowed — do not fail the cycle solely for that dirtiness (auditor: expected dirty finalize = Low, not rework).
- On Windows PowerShell, write commit message files **without** a UTF-8 BOM (`utf8NoBOM` / `UTF8Encoding($false)` / here-string `-m`); Windows PS 5.1 `Set-Content -Encoding utf8` adds a BOM.

## Safety

- No secrets in commits or session logs.
- Small diffs; no force-push; commit only when the user asks.

## Deeper guidance

See `AGENT-AND-WORKFLOW-BEST-PRACTICES.md` for Cursor mode, rules, skills, hooks, and maturity ladder.
