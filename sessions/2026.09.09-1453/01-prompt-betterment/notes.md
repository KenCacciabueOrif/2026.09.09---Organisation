# Prompt betterment notes

**Status:** complete — R1 + pack locked; refined prompt final.

## Clarifying questions (user-facing batch — informed consent)

Questions were written with plain-language explanation + pros/cons per option (orchestrator relay). Jargon defined inline: **allowlist** = FAW-safe paths only (`sessions/**`, FAW skill/agents/rules, `AGENTS.md`, templates); **fail-closed** = stop safely, document, mark blocked (no force/hard reset). **Informed consent recorded:** R1 options explained before answer; pack defaults disclosed.

## Answers

| Item | Lock | Source | Rationale |
| --- | --- | --- | --- |
| R1 resolve rule | **combined / judgment-per-hunk** (`combined-best`) | User | “study both version and keep the most apropriate each time” — not blind ours/theirs; per conflicted region read both sides and keep most appropriate (local, remote, or coherent merge) |
| Q1 | A — `origin` → current tracking (`main`↔`origin/main`) | Choose (unanswered→default) | Disclosed; finish sync without extra ask |
| Q2 | **B — merge** | Orchestrator lock | Prior cycle + this goal |
| Q3 | Allowlist then merge (unrelated dirty → abort) | Choose (unanswered→default) | Disclosed for finish-sync under Q2=B |
| Q3b | **B — allowlist-only resolve** | Orchestrator lock | User “resolve conflict” |
| Q4 | A — org-repo git root only | Choose (unanswered→default) | Disclosed |
| Q5 | A — agent Shell must succeed | Choose (unanswered→default) | Disclosed |
| Q6 | A — fail-closed + typed blocker + self-improver | Choose (unanswered→default) | Disclosed |
| Q7 | A — full FAW session artifacts | Choose (unanswered→default) | Disclosed |

## Continuity (locked — do not re-ask)

- Prior session: `sessions/2026.09.09-1435/` — `blocked` / `other`/`merge_conflict`
- Tips: HEAD `f3e1119` vs `origin/main` `489f03a` (verify live before merge)
- Predicted conflict paths (FAW allowlist only):
  - `.cursor/agents/prompt-betterment.md`
  - `.cursor/rules/full-agent-workflow.mdc`
  - `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
  - `sessions/_templates/01-notes.md`
- Org root: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`
- Mutation class: **docs_only**
- Taxonomy / must-preserve / corpus moves: **out of scope**
- Q2 = B (merge)
- Q3b = B (allowlist-only resolve)
- R1 = **combined / judgment-per-hunk**
- Self-improvement priority: **diminish user workload** (encode autonomy; do not dump recurring checks on the user)

## Assumptions

- Live porcelain / ahead-behind may differ from prior tip — researcher/implementer re-check.
- Judgment-per-hunk may prefer local, remote, or merged text per region; goal is best FAW docs + finished sync.
- Any *new* conflict paths still require ⊆ allowlist or abort.

## Open risks

- Non-allowlist conflict → abort despite Q3b=B.
- Poor hunk judgment could drop a useful side — mitigate by studying both versions and logging which side won per file in implementation log.
- Merge already aborted in prior cycle — may need fresh merge attempt from current tip.

## Self-improvement backlog (if any)

- Encode judgment-per-hunk as standing option text next to combined in pull-cycle if it recurs.
- Self-improver: prefer autonomy that finishes sync over attributing cleanup tasks to the user.

## Key alignment changes (raw → refined)

- Raw pull/merge/resolve → Q2=B + Q3b=B + **combined / judgment-per-hunk** (study both; keep most appropriate).
- Pack remainder locked via Choose defaults.
- AC requires allowlist-only gate, complete merge into `origin/main`, and workload-diminishing self-improvement.
