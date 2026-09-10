# Prompt betterment notes

**Session:** `sessions/2026.09.09-1435/01-prompt-betterment/`  
**Raw goal:** `/full-agent-workflow git pull merge`  
**Status:** **locked** — user replied **Choose** (`CHoose`); all pack items decided. `waiting_on_user: no`.

## Clarifying questions

Batch asked once with plain language + pros/cons (fail-closed, dirty working tree, allowlist, merge commit defined inline). Informed consent recorded — no jargon-explanation debt for phase 06.

## Answers

| # | Decision | Source | Rationale |
| --- | --- | --- | --- |
| **Q1** | **A — `origin` ↔ current tracking (`main`↔`origin/main`)** | Choose | Disclosed default; matches `1350` diverge vs `origin/main` |
| **Q2** | **B — allow merge commit** | Orchestrator lock / user “git pull merge” | Continuity; finish sync after `non_ff` (1/1); do not re-litigate to ff-only |
| **Q3 / Q3c** | **Order-aware allowlist autonomy → then merge** (diverged / **C-like**: dirty handling then merge, or clean merge) | Choose | Disclosed merge-favoring default; already diverged so stash→ff-only is not the finish path |
| **Q3b** | **A — fail-closed on conflict; keep WIP commit and/or stash recoverable** | Choose | Disclosed default; no force/hard reset/`stash drop` |
| **Q4** | **A — org-repo git root only** | Choose | Hard boundary; no sibling trees |
| **Q5** | **A — agent Shell pull/merge must succeed** | Choose | Dual preflight GfW+GCM; user terminal alone ≠ complete |
| **Q6** | **A — fail-closed + typed `blocker_type` + still self-improver** | Choose | Never false `complete`; no aggressive force/rebase override |
| **Q7** | **A — full FAW session artifacts** | Choose | Audit trail for merge sync cycle |

User reply: **Choose** (typo `CHoose`) → every remaining open item locked to disclosed default (Source `Choose`).

## Continuity (locked — do not re-ask)

- **Cycle id:** Pull-merge — finish sync after `1350` non_ff via merge
- **Prior session:** `sessions/2026.09.09-1350/` — `blocked` `other`/`non_ff`; HEAD was `7ac4783` vs `origin/main` `489f03a` (1/1); allowlist commit kept; backlog B1
- **Q2 = B (merge)** — continuity
- **Mutation class:** `docs_only`
- **Org root ONLY:** `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`
- **Taxonomy / must-preserve:** OUT OF SCOPE
- **ROADMAP:** n/a (git ops)

## Assumptions

- “Choose” applies to all remaining pack items; Q2 unchanged B.
- FAW dirty allowlist applies for pre-merge dirty handling; unrelated dirty → `dirty_working_tree` abort.
- Windows agent uses Git for Windows + GCM (same binary for porcelain, allowlist commit/stash, and merge pull).

## Open risks

- Merge conflict → Q3b A leaves sync unmet until a later cycle; WIP/stash must stay recoverable.
- Unrelated dirty still aborts despite Q2=B.
- Post-merge session dirt from finalize notes is expected (not rework) if sync AC already met.

## Self-improvement backlog (if any)

- None for consent UX (explanations were given before Choose).

## Key alignment changes (raw → refined)

- Raw `/full-agent-workflow git pull merge` → locked Pull-merge brief: Q1A, Q2B, Q3/Q3c merge-path dirty autonomy, Q3bA, Q4–Q7 A.
- Success = HEAD incorporates `origin/main` via merge (agent GfW) **or** correctly `blocked` with typed blocker.
- Taxonomy/moves out of scope; `refined-prompt.md` finalized.
