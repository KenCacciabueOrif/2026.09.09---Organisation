# Deferred backlog

| ID | Proposal | Why deferred |
| --- | --- | --- |
| B1 | **Finish sync for this tree** (`7ac4783` ↔ `origin/main` `489f03a`) | Requires **new** FAW pull cycle + user Choose: **Q2=B** (merge, no force) or **Q2=C** (rebase), **or** recover allowlist-only tip (e.g. soft-reset keep changes) then **Q3c** stash→ff→pop. Must not silent-merge under this session’s Q2=A lock. |
| B2 | Next pull cycle should **ask Q3c explicitly** with plain-language “already behind?” + pros/cons; unanswered→Choose **A** | Pack docs updated; live ask happens on next prompt-betterment run |
| B3 | Optional: after successful Q3c pull, allowlist-commit remaining session dirt in a tiny follow-up commit | Procedural nicety; not required for sync AC |
| B4 | P6 — light cross-ref in `publish-cycle.md` about behind+dirty (publish rarely needs stash-first) | Lower risk this turn; pull path was the deadlock |
| B5 | Optional `pull --autostash` as Q3c alternate wording | Prefer explicit path-scoped stash for agent auditability; revisit if GfW autostash proves cleaner |
| B6 | Dedicated `blocker_type: non_ff` enum vs overloading `other` | Vocabulary churn; `other` + outcome note `non_ff` already works — revisit if auditors confuse types |

## How next pull cycle should finish sync

1. Keep session `2026.09.09-1350` **`blocked`** (historical record); start a **new** dated session for sync finish.
2. Prompt-betterment: pull pack with **Q2** and **Q3c** surfaced; informed consent.
3. Prefer one of:
   - **Merge path:** Choose Q2=**B** → fetch + merge `origin/main` (no force); resolve conflicts fail-closed; keep WIP.
   - **Rebase path:** Choose Q2=**C** → rebase onto `origin/main` (no force-push).
   - **Recover + ff path:** If `7ac4783` is allowlist-only and acceptable to undo as a commit: soft-reset to pre-diverge parent, then **Q3c A** stash→`--ff-only`→pop, then optional allowlist commit.
4. Success = agent Shell HEAD matches remote tip (or correctly blocked again). Never mark complete on unmet sync.
