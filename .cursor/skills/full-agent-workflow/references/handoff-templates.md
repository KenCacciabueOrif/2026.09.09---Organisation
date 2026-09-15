# Handoff templates

Orchestrator fills placeholders then launches the named subagent via Task.

## prompt-betterment

```
Session phase dir: <abs>/01-prompt-betterment/
Raw user goal:
<paste>
Program context (if any): cycle id, program/ROADMAP.md row locked by orchestrator, prior session, mutation class docs_only|fs_mutation
Pending user gates from prior cycle (if any): taxonomy final sign-off? must-preserve review? batch subset?
If ROADMAP marks prior row Complete: lock Primary next (e.g. next Suggested-order row) — do not reopen finished Early/simple. After Medium **Complete**: lock **Multi-experiment** (small first subset; multi nested-git caution; SSH path-only) — do not reopen Medium. If Medium/Multi-experiment (or other multi-batch) is **in progress**: lock **remaining** names only; carry Continuity; do not re-ask first-batch pack. After Multi-experiment **partial** (e.g. remaining `PWAExemple`, `WorkSpace`): same row / remaining only — prefer `PWAExemple` when green; **`WorkSpace` fail-closed / git-strategy candidate** until cleared — do not jump Primary next or reopen Medium. After Multi-experiment **`WorkSpace` only**: lock **`WorkSpace` only** — do **not** re-propose `PWAExemple`; do **not** mark Complete / jump Primary next / Special git; **never invent whole-tree archive**. **Pre–strategy** (no `program/git-strategy-workspace-hazards.md`): default Continuity = research+defer unless cleared **or** dedicated git-strategy opt-in; repeated research+defer valid. **Post–hazard-strategy docs** (artifact exists): **point** pack + handoffs at `program/git-strategy-workspace-hazards.md`; default = **continue strategy** (docs) **or** explicit **Appendix A execute** Continuity (mandatory plan gate) — do **not** re-default pure Cycle 9 defer after strategy docs; “solve hazards” after docs ≠ Complete / ≠ silent whole-tree. **Named Continuity B / stop docs_only re-attest** → lock Q1=B (`fs_mutation` Appendix A and/or remaining live-hazard **remote-config**); do **not** propose Continuity A/C as this cycle’s path. **Anti-loop / B→E / no material delta** → escalate (`escalate_break_loop`); Continuity gate **X/P/N/H**; Continuity **X** = next FAW XL/git-strategy + plan gate; still WorkSpace only / not Complete. **Continuity X dedicated cycle:** hybrid gate **D/M/D+M**; STAGE 1 hold → STAGE 2 same session; **D+M** docs-first then OS-IA (or next) `path_batch`; OS-IA alone never Completes / never Primary next; post–OS-IA Next FAW = WorkSpace **TNA** + continue Continuity X clearance / keep-at-root. **Post–Appendix A / post–multi-remote clear:** still lock `WorkSpace` only; never Complete while WorkSpace remains; never invent whole-tree archive. If only **movable soft-deferred** remain (nearly complete): lock those names; default = finalize this cycle (do not re-soft-defer by default); short pack only; plan gate still separate. Medium first-batch → subset default + nested-git atomic + .env opaque; plan gate still separate from Choose. Optional: clear plan-gate near-miss typo (e.g. “sey”→yes) may count when map was just presented — record raw reply. Continuity pack bare **yes** / **ok** / **oui** (or clear near-miss) after disclosed defaults → **yes→defaults** (Choose-all equivalent); Continuity yes ≠ move approval.

Write online-prompt-tips.md, ask clarifying questions (or use answers below), then refined-prompt.md and notes.md.
Clarifying questions MUST include: plain-language explanation of what is asked + what “yes” commits to, and pros/cons (tradeoffs) per option. Do not assume jargon literacy; define gate terms in one sentence if used.
If goal is publish / git add-commit-push: use references/publish-cycle.md question pack; hard AC = this org-repo git root only (never stage sibling C:\\Project trees).
If goal is git pull / sync from origin: use references/pull-cycle.md question pack; hard AC = org-repo root only; FAW default dirty = order-aware allowlisted autonomy + --ff-only (behind+allowlisted → stash→ff→pop / Q3c; else commit-then-pull; abort only for unrelated → blocker_type dirty_working_tree); Q3b generic default A; **finish-sync continuity** (prior allowlist-only merge_conflict or user said merge+resolve) → lock Q3b=B + R1 combined-best (do not dump user-resolve chores); GfW for status gate, allowlist commit/stash, and pull.
If user answers "Choose" / "Choose all" OR bare Continuity **yes→defaults** OR leaves pack items unanswered after a partial reply → you decide using disclosed defaults, lock in notes.md Answers (Source Choose / unanswered→default / yes→defaults) (+ one-line ask summary per Q), encode in AC — do not leave blanks for later phases.
Taxonomy/must-preserve language: proposed-ratified — ready for user sign-off; draft — not auto-locked (never claim final without explicit approval).
Prior answers (if any):
<paste or none>
```

## researcher

```
Session phase dir: <abs>/02-research/
Read refined prompt: <abs>/01-prompt-betterment/refined-prompt.md
Produce codebase-findings.md, online-findings.md, research-brief.md.
Corpus/inventory goals: coarse map; flag git roots; do not deep-document node_modules/caches; secrets = path presence only.
Live INDEX path truth: for in-scope + recently moved siblings, Test-Path (or Read/Glob if Shell blocked/empty) INDEX current path vs disk — already at dest → verify-only / catalogue fix, never re-move. Note probe method when not Shell.
Early/simple prep: if next cycle may move, note cheap batch candidates + must-preserve collisions — do not invent final ratification.
If the goal includes git push / remote publish — dual preflight (user can push ≠ agent ready):
- remote scheme + tracking
- agent git path (Get-Command / where); credential.helper per binary; prefer GfW over MSYS on Windows HTTPS when default lacks GCM
- GCM evidence boolean (fill/dry-run success, no secret output); gh present? (optional, not sole signal)
- optional user-terminal note; blocker_type agent_environment vs user_credentials
Never "blockers: none" when agent cannot push non-interactively. Never log fill passwords or full Env:.
If the goal includes git pull / sync — same dual preflight + GfW for porcelain gate, allowlist commit/stash, and pull; classify allowlist vs unrelated dirty vs auth; record ahead/behind:
- unrelated dirty abort → blocker_type dirty_working_tree (auth may be green)
- allowlisted-only + behind>0 → stash→ff→pop path (not “sync not ready”; flag commit-while-behind risk if plan still commit-first)
- allowlisted-only + not behind → agent may auto-commit then pull
- wrong binary / sandbox → agent_environment; true login fail → user_credentials
Do not claim sync ready when WT has unrelated dirty under abort policy.
```

## planner

```
Session phase dir: <abs>/03-plan/
Read:
- <abs>/01-prompt-betterment/refined-prompt.md
- <abs>/02-research/research-brief.md
Write plan.md. Set ready_to_implement.
Set mutation class docs_only|product_settings|fs_mutation|escalate_break_loop. docs_only = zero corpus moves; **includes** org-repo scaffolding creates (folders/READMEs) — not an automatic plan gate. product_settings = editor extension/settings/local fixture/**local dist patch** (not corpus); plan-gate n/a; same-run when ready; name primary + Marketplace/Open VSX fallback IDs when relevant; dist-patch plans: backup + **re-apply after update** + Soft Reload tip; Python 42+flake8 Continuity → prefer ≤79 generator over Norminette-80 / ignore-first. fs_mutation = corpus/catalogue path batches **or** **remote-config** (e.g. git remote remove on pinned live nested clone — zero path moves, **still** plan gate): user approval + git-root atomicity + opaque secrets/deps + "What the user is approving" (plain language + path/command map + pros/cons) for orchestrator plan-gate relay. escalate_break_loop = anti-loop when concrete_advance_candidate none: Continuity gate X/P/N/H; ready_to_implement no; zero FS; forbid Continuity A theater; Continuity X = next FAW XL/git-strategy + plan gate (WorkSpace only / not Complete).
When Continuity names Appendix A / Continuity B / stop docs_only / advance live hazard: plan must be fs_mutation (scoped isolation and/or remote-config — not docs_only re-attest) **unless** research already returns none → then escalate_break_loop. Worktree Steps: git worktree list on **nested clone paths** only (not parent wrappers that resolve to outer repo). Disclose nested+parent dirty WT + NO_AUTO_COMMIT; reverse-move notes AC when paths move.
Proposed-ratified ≠ final; must-preserve draft ≠ locked. First move/Early-simple: fail-closed without taxonomy sign-off/waiver + must-preserve review/waiver + batch approval.
Optional signals ("if available") must not be hard AC checkboxes.
Path attestation AC: Test-Path or Read/Glob equivalent OK when Shell unavailable — require probe method in implementer log. Remote-config: Read `.git/config` OK when Shell blocked.
Push goals: dual preflight step; ready_to_implement no only when agent cannot push / credentials unverified — not merely missing gh when GCM verified.
Pull goals: dual preflight + dirty gate; encode order-aware allowlist path (Q3c stash when behind) + unrelated dirty_working_tree abort + expected non-ff fail-closed; ready_to_implement may be yes when fail-closed non-ff or unrelated abort is an allowed implement outcome.
```

## implementer

```
Session phase dir: <abs>/04-implementation/
Execute plan at: <abs>/03-plan/plan.md
Respect acceptance criteria in refined-prompt.md.
User batch approval (fs_mutation only): <approved|pending|n/a — cite SESSION/plan>
Write log.md and changes.md. Do not expand scope.
docs_only → zero-move attestation; product_settings → zero corpus moves + extension/settings/fixture attest; local dist patch → backup + re-apply-after-update note + Soft Reload tip (not blocker); never stage `~\.cursor\extensions` into org-repo; Open VSX/CLI not-found on primary → use plan-named fallback, log IDs; soft Reload tip only (not blocker); fs_mutation → approved batch only (paths **or** remote-config commands); git roots atomic; no secret contents; reverse-move notes for each successful move.
Linked worktree probe: `git worktree list` on **nested clone paths** only — not parent wrappers that resolve to an outer repo (e.g. TNA).
Dirty WT (nested and/or parent after moves or remote-config): disclose + NO_AUTO_COMMIT (do not auto-commit that dirt this cycle).
Remote-config: only approved `git remote …` in pinned cwd; no origin/set-url/force-push/path moves unless mapped; before/after remotes + zero-move attestation; keep WorkSpace-only / not Complete.
Path-presence: prefer Test-Path/Shell; if Shell blocked/empty → Read/Glob same paths (remote-config: Read `.git/config`), log probe method under Deviations — semantic attestation OK (do not stall).
Windows nested-.git lock Continuity: prefer Move-Item; on PermissionDenied/split → reunify into dest + robocopy /E /MOVE for remaining; remove only empty leftover .git shells; re-attest; log deviation — do not expand map.
Do not upgrade proposed-ratified/draft labels to "final"/"locked" unless plan AC and session evidence say so.
Push goals: prefer GfW absolute git on Windows HTTPS (not PATH/MSYS alone); confirm rev-parse toplevel = org root before stage; blocker_type agent_environment vs user_credentials; no secret logging.
Pull goals: same GfW for status --porcelain, allowlist commit/stash, and pull; unrelated dirty abort → blocked + dirty_working_tree; behind+allowlisted → stash→ff→pop; not-behind allowlist → auto-commit then --ff-only; non-ff → blocked + other/non_ff; content-conflict abort under Q3b=A → blocked + other/merge_conflict (keep WIP/stash); Q3b=B resolve only if all conflicts ⊆ allowlist + R1 (continuity may supply combined-best); never claim pull success on block; auth/env types unchanged.
```

## git-manager (mid)

```
Session phase dir: <abs>/05-git/
pass_kind: mid
Read 04-implementation/log.md + changes.md and the cycle acceptance criteria.
Mid pass (optional/early after implementer): health-check (status/remotes/ahead-behind) → stage only cycle implementer / early session paths (no unrelated dirt, no secrets) → commit (small, clear messages; GfW binary on Windows; BOM-free -F) → push → verify push via ahead/behind, not exit text.
Mid is NOT a substitute for the final closing pass — leave 06-audit / 07-self-improvement / SESSION close for later.
Branches: create feature/<topic> / fix/<topic> when the work warrants; MERGE INTO MAIN BY DEFAULT when verified and conflict-free — do not let cycle work strand on long-lived branches; never force-push, never rewrite history, never delete unmerged branches.
Conflict/non-ff on merge or push → do NOT force; log conflict paths, return blocked with blocker_type (same taxonomy as implementer).
docs_only zero-mutation cycle with no allowlisted dirt → write zero-mutation attestation in 05-git/log.md and skip git ops.
Write/append ## Mid pass section in log.md (health snapshot + commits + push + merge record). Return pass_kind: mid.
Orchestrator: after mid return, flip SESSION Workflow progress + Phase checklist + Phase summaries for 05 mid **before** launching auditor.
```

## auditor

```
Session phase dir: <abs>/06-audit/
Verify against refined-prompt.md, plan.md, and 04-implementation artifacts.
Auditor is readonly — **expect Write blocked**. Always return the **full** report.md body in your message (`write_status: blocked_returned_inline`); orchestrator persists to 06-audit/report.md.
Return verdict, write_status, rework_needed, and rework_owner (implementer | user | orchestrator | …).
Shell unavailable: verify path presence via Read/Glob (remote-config: Read `.git/config`); implementer Read-equivalent attestation with semantic AC → Low/process, not Critical rework.
docs_only: verify zero corpus FS mutation + attestation; proposed-ratified wording; must-preserve draft label.
product_settings: zero corpus moves; plan-gate n/a; primary/fallback extension IDs; local dist patch → re-apply docs + Soft Reload=Low (not Critical / not rework_owner user for Reload alone); generator-over-ignore when Continuity; extensions.json/FS OK when CLI list blocked.
fs_mutation: verify user approval, batch bounds (paths **or** remote-config), git atomicity, no secret quotes; first-move gates (sign-off/waiver); reverse-move notes when moves succeeded; remote-config: wrong remote gone, origin intact, zero-move, WorkSpace-only not Complete. Move-Item→robocopy reunify with AC met + empty shells only → process Medium/Low (pass_with_issues OK), not Critical rework.
Push goals: Option A docs + optional GfW smoke; true credential gaps → rework_owner: user; wrong-git/sandbox may be agent_environment (user settings, not re-login alone). Fail if session marked complete with unmet push criterion.
Pull goals: unrelated dirty-abort or expected non-ff with unmet sync AC → process pass + session blocked (+ rework_owner user for unrelated dirty / non-allowlist conflict only) is valid; allowlist-only merge_conflict under Q3b=A → rework_owner orchestrator (next FAW continuity), not user; fail if session marked complete after unmet pull AC. Allowlisted commit then pull attempted = correct. Flag Low if SESSION still in_progress while implementer recommended blocked.
Single-commit publish: expected post-push dirty finalize on session logs only → Low, not rework_needed.
Fail / flag if session marked **complete** while final closing-pass git was skipped and allowlisted late dirt (06/07/SESSION/.cursor) remains.
Flag Low if SESSION mid-git checklist still unchecked while 05-git mid section already complete.
Flag Low if Workflow progress is checked but Phase checklist or Phase summaries still lag for the same phase.
Orchestrator (after auditor return, before self-improver): persist full report to 06-audit/report.md; flip Workflow progress + Phase checklist + Phase summaries for 06; set Audit verdict; then launch SI. Mid ≠ final — do not mark complete.

## self-improver

```
Session root: <abs>/
Read SESSION.md and all phase artifacts especially 06-audit/report.md.
1) audit-realization.md (good + bad)
2) proposals.md (incl. short online best-practice check)
3) implement safe improvements to .cursor/agents, skill, rules, templates
4) changes-applied.md + backlog.md
This step is mandatory.
**User-workload priority:** encode autonomy defaults so recurring sync/conflict cleanup is agent-owned; avoid backlog that assigns constant checks to the user; still fail-closed for unrelated/non-allowlist.
Focus when relevant: publish/pull question packs / Q3c behind+allowlisted stash path / Q3b finish-sync continuity (B + combined-best) / allowlisted auto-commit / git-root staging / GfW vs MSYS / dirty_working_tree (unrelated) vs non_ff|merge_conflict/other vs agent_environment vs user_credentials / SESSION blocked bookkeeping on implementer return / unanswered→Choose defaults / Continuity **yes→defaults** / **STAGE 1 same-run auto-continue when docs_only|product_settings + ready_to_implement yes** / **ready_to_implement no / escalate_break_loop → skip implementer + mid git; still auditor → SI → final git; Step 3 Continuity recording (notes + SESSION + ROADMAP Next FAW hint)** / **anti-loop no material delta → escalate_break_loop (not Continuity A theater); Continuity gate X/P/N/H; Continuity X = next FAW XL/git-strategy + plan gate; Continuity X dedicated = hybrid D/M/D+M + STAGE 1→2 same session; D+M docs-first then path_batch; OS-IA alone never Completes / never Primary next; post–OS-IA Next FAW = WorkSpace TNA + continue Continuity X clearance; still WorkSpace only / not Complete** / **interrupt/retry: skip re-implementer when 04 complete** / **Open VSX/CLI primary miss → plan fallback; soft Reload=Low tip** / **product_settings local dist patch + re-apply after Marketplace; Soft Reload after patch; Python 42 Norminette-80 vs flake8-79 → prefer ≤79 generator over ignore-first** / **dual mid+final git; no complete with late allowlisted dirt; mid ≠ final substitute** / **orchestrator always persist auditor 06-audit/report.md; mid-cycle SESSION flip Workflow+checklist+Phase summaries before next phase** / **STAGE 1 hold → STAGE 2 resume same session after fs_mutation plan-gate yes (+ amendments)** / **Named Continuity B / stop docs_only re-attest → lock fs_mutation (Appendix A and/or remote-config); do not re-propose Continuity A theater** / **Post–Appendix A / post–multi-remote clear → still WorkSpace only; never Complete while WorkSpace remains** / **remote-config fs_mutation (git remote remove) = gated; zero path moves ≠ waive plan gate** / **nested-clone worktree list (not parent dirs that resolve to outer repo)** / **nested+parent dirty WT disclose + NO_AUTO_COMMIT** / post-push dirty=Low; proposed-ratified vs final; draft must-preserve; ROADMAP row-completion → Primary next (no reopen finished row) / **Medium Complete → Multi-experiment** (small subset + multi nested-git + SSH path-only) / **Multi-experiment partial → same row + remaining names** (not Primary next; not Medium reopen; WorkSpace git-strategy candidate) / **Multi-experiment WorkSpace-only → lock WorkSpace; never Complete while it remains; pre-strategy research+defer unless cleared or git-strategy; post–hazard-strategy docs (`program/git-strategy-workspace-hazards.md`) → continue strategy or explicit Appendix A / remote-config Continuity (plan gate); never re-default Cycle 9 pure defer after strategy docs; never invent whole-tree archive; not Medium finalize; not re-propose PWAExemple** / **Shell/porcelain unavailable → Read/Glob / `.git/config` path-presence fallback** (log probe method; Low not fail when semantic AC holds) / **auditor readonly → always return full report; orchestrator always persist 06-audit/report.md** / **resume incomplete same-cycle SESSION when user names it as prior** (no parallel folder) / **Windows nested-.git lock → reunify / robocopy Continuity** (prefer clean Move-Item; no user PATH chores) / **partial multi-batch → same row + remaining names** / **movable soft-deferred finalization → finalize remaining (not re-defer by default)** / Medium remaining Continuity (no re-ask first pack) / INDEX live path truth (no re-move) / dest nested-git + opaque `.env` attestations / Choose→decide (incl. Choose-all); ad-hoc org-repo scaffolding vs corpus fs_mutation (docs_only clarity); informed-consent asks (explanation + pros/cons) if jargon friction appeared; plan-gate near-miss typo tolerance if relevant / **dual git-manager: mid optional/early + mandatory final closing pass after self-improver; no complete with late allowlisted dirt**.
```

## git-manager (final closing pass)

```
Session phase dir: <abs>/05-git/
pass_kind: final
MANDATORY when allowlisted late dirt remains after self-improver.
Late stage set (explicit paths; never git add -A): 
- <abs>/06-audit/**
- <abs>/07-self-improvement/**
- <abs>/SESSION.md (close / status)
- cycle .cursor/** edits (agents/skill/rules) and other allowlisted cycle dirt (AGENTS.md, sessions/_templates/**, …) as present
Optional leftover path list from Continuity/plan (if any remaining orphans): <paste or none>
Same allowlist + GfW absolute git.exe + GCM as mid/publish law; dual preflight; no secrets; no force-push; no non-allowlist / TNA.
Prefer append ## Final closing pass section in the SAME 05-git/log.md BEFORE the final commit when practical (tiny post-final log dirt = known Low).
Health-check → stage only listed allowlisted late paths → commit → push → verify ahead/behind.
Mid-only prior push does NOT satisfy this pass.
Return pass_kind: final; status complete | blocked (+ blocker_type). Orchestrator must NOT mark SESSION complete if this pass was skipped while late allowlisted dirt remains; honest blocked → session blocked (never false complete).
```

## git-manager (leftover / finish-sync)

```
Session phase dir: <abs>/05-git/
pass_kind: leftover
Explicit path set from Continuity/plan (orphaned allowlisted paths): <paste exact list>
Exclude: <paste>
Defer (optional later): <paste>
Same allowlist + GfW/GCM; explicit git add of listed paths only; commit + push; verify ahead/behind.
Append ## Leftover / finish-sync section in 05-git/log.md.
This does NOT replace this cycle’s final closing pass when 06/07/SESSION late dirt remains here.
Return pass_kind: leftover.
```
