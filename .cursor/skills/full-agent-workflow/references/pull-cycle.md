# Pull cycle (org-repo git pull / sync from origin)

Use when the user asks to **pull**, **git pull**, **sync from remote**, or otherwise update this organisation repo **from** `origin`. Keep mutation class **`docs_only`** unless they also asked for corpus moves.

**Framing:** Success = agent Shell sync AC met **or** correctly fail-closed with typed blocker (never false `complete`). Unrelated (non-allowlist) dirty abort, auth/env fail, or non-ff refuse → session **`blocked`**. Do **not** claim pull succeeded when aborted or blocked.

## Git-root boundary (hard)

- Operate only inside this repo’s git root (`git rev-parse --show-toplevel`).
- Never run pull/fetch status gates against sibling trees (e.g. other folders under a multi-root `C:\Project` workspace).
- Encode as acceptance criteria: “all git ops confined to this org-repo root.”

## Dirty allowlist (FAW default)

When porcelain is non-empty before pull, the agent may touch **only** these paths (commit and/or path-scoped stash — see order rules below):

| Include | Paths |
| --- | --- |
| Sessions | `sessions/**` |
| FAW meta | `.cursor/skills/full-agent-workflow/**` |
| FAW meta | `.cursor/agents/**` |
| FAW meta | `.cursor/rules/**` |
| FAW meta | `AGENTS.md` |
| FAW meta | `sessions/_templates/**` |

**Outside allowlist** → do **not** auto-commit or stash; **abort** with listed paths and `blocker_type: dirty_working_tree`; session `blocked`.

### Order when allowlisted dirty (avoid commit-while-behind diverge)

Fetch / compare ahead-behind **before** the dirty handler:

| Remote state | Allowlisted dirty handler (FAW default) | Why |
| --- | --- | --- |
| **Behind > 0** (remote has commits you lack) | **Stash allowlist → `git pull --ff-only` → stash pop** (then optional allowlist commit of remaining dirt). Never `stash drop` on conflict — fail-closed, leave stash recoverable. | Commit-first while behind creates a new local tip → **1/1 diverge** → `--ff-only` refuses → sync unmet (`other`/`non_ff`). |
| **Not behind** (ahead 0 or already even; or only ahead) | Prefer **allowlist commit then `--ff-only`** (durable checkpoint). | Commit-over-stash is fine when it will not diverge from remote tip. |

**Already diverged** (local tip and `origin/<branch>` both moved past a shared base — e.g. prior allowlist commit while behind): do **not** silent merge/rebase under Q2=A. Session **`blocked`**, `blocker_type` **`other`** / `non_ff`, WIP kept. Finish sync only in a **new** cycle after user Choose changes Q2 (B merge / C rebase) **or** recovers the allowlist-only tip (e.g. soft-reset + Q3c stash path) — never claim pull succeeded.

## Question pack (ask once; informed consent)

Ask a short batch. For **every** question: plain-language explanation + what each choice commits to + pros/cons. Prefer everyday words; define jargon in one sentence if used:

- **fail-closed** = stop safely, document, mark blocked; no force/hard reset/`--no-verify` to “make it work.”
- **ff-only** = update only if local history can move forward with no merge commit; otherwise abort.
- **dirty working tree** = uncommitted or untracked local changes; pulling may conflict or surprise-overwrite WIP.
- **allowlisted auto-commit** = agent commits only the FAW dirty allowlist above (safe when **not** behind); unrelated paths still abort.
- **behind + allowlisted dirty** = remote has commits you lack **and** WT dirt ⊆ allowlist — commit-first usually **diverges**; prefer stash→ff-only→pop (Q3c).
- **allowlist-only conflict resolve (Q3b=B)** = every conflict path is FAW meta/session allowlist; agent may finish the merge using a locked rule (`ours` / `theirs` / `combined`). Any non-allowlist conflict → abort like Q3b=A.

| # | Topic | Typical options | Disclosed default if unanswered / Choose |
| --- | --- | --- | --- |
| Q1 | **Remote / branch** | A = pull `origin` into current tracking (usually `main`↔`origin/main`); B = other remote/branch | **A** if already on `main`↔`origin/main` |
| Q2 | **Combine strategy** | A = `git pull --ff-only` (or fetch + ff-only merge); B = allow merge commit; C = rebase | **A** for FAW pull goals — **no** merge/rebase fallback when A |
| Q3 | **Dirty working tree (not behind / general)** | A = **allowlisted auto-commit then pull** when **not** behind (abort only for unrelated dirty); B = abort any dirty; C = stash then pull (any dirty in allowlist); D = commit all WIP then pull | **A** when ahead/behind shows **not behind**; unrelated still aborts |
| Q3c | **Behind remote + allowlisted dirty** | A = **stash allowlist → `--ff-only` pull → stash pop** (optional allowlist commit after); B = allowlist **commit first** then `--ff-only` (may diverge → `other`/`non_ff`); C = allowlist commit then **merge/rebase** (requires Q2 B or C) | **A** whenever behind>0 and dirt ⊆ allowlist (FAW default — avoids commit-while-behind deadlock) |
| Q3b | **On conflict during combine** (merge/rebase/stash-pop content conflicts) | A = fail-closed abort; keep WIP commit **or** stash recoverable; no agent conflict edit; no force/hard reset/`stash drop`. **B = allowlist-only resolve:** if **every** unmerged path ⊆ FAW dirty allowlist, agent may resolve with a **documented rule** locked in `notes.md` (`ours` = keep ours / `--ours`, `theirs` = take theirs / `--theirs`, or `combined` = manual merge keeping both intents); then `git add` + complete merge/rebase. If **any** conflict path is **outside** allowlist → treat as A (abort). **C = user resolves** conflicts (or edits) then agent continues verify/commit | **A** (safe default). Use **B** only when user Choose / explicit answer authorizes allowlist resolve — never silent-resolve under A |
| Q4 | **Git root** | A = this org-repo root only; B = also touch sibling trees | **A** |
| Q5 | **Who must succeed** | A = agent Shell pull must succeed (dual preflight); B = user terminal OK as success | **A** for FAW pull goals |
| Q6 | **On failure** | A = fail-closed + typed `blocker_type` + still self-improver; B = retry with merge/rebase/force | **A** |
| Q7 | **Session docs** | A = full FAW artifacts under this session; B = minimal notes | **A** |

### Unanswered → Choose defaults

After the user answers the batch (even partially): any **unanswered** item that had a disclosed default → treat as **Choose→that default**. Lock in `notes.md` with Source `Choose (unanswered→default)` + one-line rationale. Do **not** leave “Choose” or blanks for researcher/planner/implementer. Re-ask only if the default would be irreversible corpus FS mutation (pull pack defaults are not).

## Windows agent pull (standing constraints)

- **Dual preflight** (same idea as publish): remote scheme + tracking; **agent** git/GCM. Prefer **Git for Windows** absolute `...\Git\cmd\git.exe` when PATH `git` is MSYS without helper.
- Use the **same GfW binary** for dirty gate (`status --porcelain`), allowlist commit/stash, **and** pull — MSYS porcelain counts can skew and mis-trigger abort or false clean.
- Missing `gh` alone ≠ `user_credentials` when GCM works.
- **`blocker_type`:**
  - **`dirty_working_tree`** — porcelain has paths **outside** the allowlist (unrelated dirty) and policy aborts. Auth may still be green. Remediation: user clean/stash/commit those paths, then **new** pull cycle — do **not** relaunch implementer on the same unrelated dirty tree for the same goal. (**Not** used when dirt ⊆ allowlist — agent uses commit and/or Q3c stash path.)
  - **`other`** (plan/outcome vocabulary **`non_ff`** **or** **`merge_conflict`**) — two common sync-unmet cases (process may **pass**; session **`blocked`**; **never** claim pull succeeded; keep WIP/stash recoverable; no force/hard reset/`--no-verify`):
    - **`non_ff`** — histories diverged so `--ff-only` refused (often **commit-while-behind**, or tip not an ancestor of remote). **Do not** merge/rebase under Q2=A. **Next cycle:** Choose Q2 **B**/**C**, **or** recover allowlist-only tip + Q3c stash→ff→pop.
    - **`merge_conflict`** (outcome **`blocked_conflict`**) — combine started (Q2=B/C or stash pop) but content conflicts; Q3b=**A** (or non-allowlist conflict under Q3b=B) → prefer `merge --abort` / leave rebase stopped safely. **Next cycle:** Choose Q3b=**B** (allowlist-only resolve + documented ours/theirs/combined rule) **or** Q3b=**C** / user resolves the listed paths then agent continues — still fail-closed for unrelated conflict paths.
  - **`agent_environment`** — wrong git binary / sandbox blocking GCM or non-interactive pull.
  - **`user_credentials`** — true credential/login failure (not “missing gh” alone when GCM works).
- Fail-closed: unrelated dirty-abort, non-ff refuse, merge-conflict abort under Q3b=A, or pull/auth fail → session **`blocked`** (never `complete`); **self-improver still runs**.
- Auditor:
  - Allowlisted dirt → agent used **order-aware** path (stash→ff→pop when behind; commit-then-pull when not) = **correct path** (not “user must clean session dirt”).
  - Correct **unrelated** dirty-abort = **process pass** with sync AC **unmet**; `rework_owner: user` — not implementer defect.
  - Expected **`other`/`non_ff`** or **`other`/`merge_conflict`** block = **process pass** + session `blocked` (sync AC unmet) — not implementer defect for refusing merge/rebase under Q2=A or refusing resolve under Q3b=A.
  - Allowlist-only resolve under Q3b=**B** = **correct path** only when all conflict paths ⊆ allowlist and resolve rule was locked; any outside-allowlist conflict still fail-closed.
  - Commit-first while behind that predictably non-ffs = **process debt for pack defaults** (self-improver / next Choose), not silent implementer merge.

## Out of scope for a pure pull cycle

- Corpus moves/renames/deletes; taxonomy final ratification; must-preserve lock
- Force-push, hard reset, merge/rebase fallbacks when Q2=A; silent merge to “finish” a `non_ff` block in the same cycle
- Silent conflict resolution when Q3b=A; resolving **non-allowlist** conflict paths under Q3b=B
- Autostash / stash for **non-allowlist** paths; commit-all WIP as default; `stash drop` on conflict
- Commit-first while **behind** when Q3c default A applies (that path is superseded by stash→ff→pop)
- Treating “user terminal can pull” as success when agent pull failed or aborted
- Marking session `complete` because auth was green while unrelated dirty, non-ff, or merge-conflict abort blocked sync
