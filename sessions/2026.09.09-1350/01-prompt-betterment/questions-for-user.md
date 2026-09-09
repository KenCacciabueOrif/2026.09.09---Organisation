# Clarifying questions — Pull-autonomy

Reply with letters (e.g. `Q3 B, Q3b A, …`) or **Choose** / leave blank to accept the disclosed default noted under each question.

**Background (why we’re asking):** Last pull aborted because the working tree had uncommitted files (often from FAW session docs). You asked us to **stop requiring you to clean that up**, fix the workflow, then pull again — without force-push, hard reset, or skipping hooks.

---

### Q1 — Remote / branch

**Plain language:** Which remote branch should the agent update from?  
**What a choice commits to:** Agent runs fetch/pull only against that remote/branch pair inside the org-repo.

- **A** — `origin` into current tracking (usually `main` ↔ `origin/main`)  
  - Pros: Matches how this repo already tracks; fewest surprises.  
  - Cons: Wrong if you meant a feature branch.  
- **B** — Other remote/branch (say which)  
  - Pros: Explicit control.  
  - Cons: Easy to sync the wrong line of history.

**Disclosed default if unanswered / Choose: A**

---

### Q2 — How to combine remote history (after the tree is pullable)

**Plain language:** Once local WIP is safely parked (see Q3), how should remote commits land on your branch?  
**ff-only** = only move forward if your branch tip is a direct ancestor of remote; otherwise stop (no automatic merge commit).

- **A** — `git pull --ff-only` (or fetch + ff-only merge)  
  - Pros: Fail-closed on divergence; clean history.  
  - Cons: Blocks if you already have local commits that aren’t on remote (needs a follow-up plan, not force).  
- **B** — Allow a merge commit  
  - Pros: Can succeed when histories diverged.  
  - Cons: Extra merge commit; conflicts still possible.  
- **C** — Rebase onto remote  
  - Pros: Linear history.  
  - Cons: Rewrites local commits; riskier for automation; we still won’t force-push.

**Disclosed default if unanswered / Choose: A**

---

### Q3 — Dirty working tree (REFRAMED — autonomy required)

**Plain language:** Uncommitted or untracked local changes are a **dirty working tree**. Old default was **abort and wait for you**. You rejected that for FAW. How should the **agent** make the tree pullable **without your cleanup**, while staying **fail-closed** (stop safely; no force/hard reset/`--no-verify`)?

- **A** — Abort if dirty (list paths, block, no stash/commit) — *legacy; conflicts with your stated goal*  
  - Pros: Never touches WIP.  
  - Cons: Agent pull often impossible whenever a session folder exists; needs you.  
- **B** — **Auto-commit session/FAW-meta only** (`sessions/**` and agreed FAW meta paths), then pull  
  - Pros: Durable checkpoint (better than stash for agents); scoped blast radius; matches “FAW dirt is expected.”  
  - Cons: Creates commits on your branch; non-session dirty files still need a rule (see sub-note).  
- **C** — **Stash** (optionally path-limited) → pull → stash pop  
  - Pros: No permanent commit.  
  - Cons: Autostash/stash-pop can hide conflicts or lose work if mishandled; weaker for automation.  
- **D** — **Commit all** allowed WIP in org-repo, then pull  
  - Pros: Clears whole tree for pull; includes your “small project changes.”  
  - Cons: Broader auto-commit than sessions; may commit files you didn’t intend.  
- **E** — Split policy in docs: FAW pull/push default = autonomous path-scoped commit (B); abort (A) still applies for unrelated dirty outside that allowlist  
  - Pros: Fixes the deadlock and keeps a safety abort for surprise dirt.  
  - Cons: Slightly more policy to document; allowlist must be clear.

**If dirty remains outside the chosen path scope:** agent should (pick with your Q3 letter or add): escalate to D for this run / stash remainder / abort remainder only.

**Disclosed default if unanswered / Choose: E implemented as B for FAW allowlist + abort for unrelated dirty**  
(Equivalent package: path-scoped session/FAW-meta auto-commit, then `--ff-only`; unrelated dirty → fail-closed `dirty_working_tree` with paths listed — not user cleanup of session files.)

---

### Q3b — Conflict / failed re-apply after autonomous dirty step

**Plain language:** If pull or stash-pop/merge hits conflicts, what should the agent do?

- **A** — **Fail-closed:** stop, leave WIP commit or stash **recoverable** (never `stash drop` / never hard reset), document paths + `blocker_type`, mark session blocked, still run self-improver  
  - Pros: No silent data loss.  
  - Cons: May need a later human or new cycle for conflict resolution.  
- **B** — Agent attempts conflict resolution on session/docs files only, then continue  
  - Pros: More autonomy.  
  - Cons: Risk of wrong merges in docs; harder to audit.  
- **C** — Agent attempts conflict resolution on any conflicting paths  
  - Pros: Maximum “just finish pull.”  
  - Cons: Highest wrong-merge risk; still no force/hard reset.

**Disclosed default if unanswered / Choose: A**

---

### Q4 — Git root

**Plain language:** Which folder is allowed for git status/pull/commit?

- **A** — This organisation repo root only  
  - Pros: Hard boundary; no sibling tree accidents.  
  - Cons: Won’t sync other folders under `C:\Project`.  
- **B** — Also touch sibling trees  
  - Pros: Broader sync.  
  - Cons: Violates standing org safety; rejected by orchestrator AC.

**Disclosed default if unanswered / Choose: A** (hard constraint)

---

### Q5 — Who must succeed

**Plain language:** Does “pull worked” mean the **agent’s** Shell pull succeeded (with Windows Git for Windows + GCM preflight), or is your own terminal enough?

- **A** — Agent Shell must succeed  
  - Pros: Proves the fixed workflow works in the agent environment.  
  - Cons: May surface `agent_environment` / credentials blockers even if your terminal is fine.  
- **B** — User terminal OK as success  
  - Pros: Easier to mark done.  
  - Cons: Doesn’t validate agent autonomy (your goal).

**Disclosed default if unanswered / Choose: A**

---

### Q6 — On auth / environment / non-ff failure

**Plain language:** If pull still can’t complete for reasons other than “we refuse to touch dirty files,” what next?

- **A** — Fail-closed: document, typed `blocker_type`, session `blocked`, no force/hard reset/`--no-verify`; still self-improver  
  - Pros: Safe, auditable.  
  - Cons: Sync AC unmet until remediated.  
- **B** — Retry with merge/rebase/force-style escapes  
  - Pros: Might “make it work.”  
  - Cons: Violates hard constraints; unsafe.

**Disclosed default if unanswered / Choose: A**

---

### Q7 — Session documentation

**Plain language:** How much should this FAW session write under `sessions/2026.09.09-1350/`?

- **A** — Full artifacts (prompt → research → plan → implement → audit → self-improve)  
  - Pros: Verifiable cycle; improves next pull policy.  
  - Cons: More files (exactly the dirt this cycle is teaching the agent to handle).  
- **B** — Minimal notes only  
  - Pros: Less dirt.  
  - Cons: Weaker audit/self-improve; fights FAW norms.

**Disclosed default if unanswered / Choose: A**

---

### Q8 — Order: policy fix vs pull

**Plain language:** Do we change pull/push dirty-handling docs/defaults **before** pulling in this same cycle?

- **A** — Implement workflow docs/defaults first, then **same-session** agent pull under the new rules  
  - Pros: One cycle delivers both your asks; pull uses the fix.  
  - Cons: Larger implementer scope; pull depends on docs landing first.  
- **B** — Docs/defaults only this cycle; pull in a follow-up session  
  - Pros: Smaller slices.  
  - Cons: Delays incorporating remote session + your local changes.  
- **C** — Pull first with ad-hoc autonomy, document after  
  - Pros: Faster sync.  
  - Cons: Risk of one-off behavior not encoded for next time.

**Disclosed default if unanswered / Choose: A**

---

### Q9 — Push / publish dirty policy (same autonomy theme)

**Plain language:** You said git workflow without user involvement for pull **and** implied push. Should publish/push FAW cycles use the **same** autonomous dirty rule (path-scoped session commit), with abort still for unrelated dirt?

- **A** — Yes — mirror pull autonomy on publish for session/FAW-meta allowlist  
  - Pros: One coherent rule; future push won’t deadlock on session files.  
  - Cons: Broader docs change (pull-cycle + publish-cycle / agents).  
- **B** — Pull only this cycle; leave publish abort-or-manual as-is  
  - Pros: Narrower change.  
  - Cons: Push may still hit the same deadlock later.  
- **C** — Publish may auto-commit **all** org-repo WIP when publishing  
  - Pros: Always clean for push.  
  - Cons: Easy to publish unintended files.

**Disclosed default if unanswered / Choose: A**

---

## Continuity already locked (no need to re-answer)

- Org-repo git root only; never sibling `C:\Project`  
- No force push / hard reset / `--no-verify`  
- Secrets never in logs or commits intentionally  
- Taxonomy / must-preserve gates are **out of scope** (not blockers)  
- Dual preflight GfW+GCM on Windows; same binary for dirty gate and pull
