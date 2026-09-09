# Pull cycle (org-repo git pull / sync from origin)

Use when the user asks to **pull**, **git pull**, **sync from remote**, or otherwise update this organisation repo **from** `origin`. Keep mutation class **`docs_only`** unless they also asked for corpus moves.

**Framing:** Success = agent Shell sync AC met **or** correctly fail-closed with typed blocker (never false `complete`). Unrelated (non-allowlist) dirty abort, auth/env fail, or non-ff refuse → session **`blocked`**. Do **not** claim pull succeeded when aborted or blocked.

## Git-root boundary (hard)

- Operate only inside this repo’s git root (`git rev-parse --show-toplevel`).
- Never run pull/fetch status gates against sibling trees (e.g. other folders under a multi-root `C:\Project` workspace).
- Encode as acceptance criteria: “all git ops confined to this org-repo root.”

## Dirty allowlist (FAW default)

When porcelain is non-empty before pull, the agent **may auto-commit only** these paths (then `git pull --ff-only`):

| Include | Paths |
| --- | --- |
| Sessions | `sessions/**` |
| FAW meta | `.cursor/skills/full-agent-workflow/**` |
| FAW meta | `.cursor/agents/**` |
| FAW meta | `.cursor/rules/**` |
| FAW meta | `AGENTS.md` |
| FAW meta | `sessions/_templates/**` |

**Outside allowlist** → do **not** auto-commit or stash; **abort** with listed paths and `blocker_type: dirty_working_tree`; session `blocked`. Prefer **commit over stash/autostash** for allowlisted dirt.

## Question pack (ask once; informed consent)

Ask a short batch. For **every** question: plain-language explanation + what each choice commits to + pros/cons. Prefer everyday words; define jargon in one sentence if used:

- **fail-closed** = stop safely, document, mark blocked; no force/hard reset/`--no-verify` to “make it work.”
- **ff-only** = update only if local history can move forward with no merge commit; otherwise abort.
- **dirty working tree** = uncommitted or untracked local changes; pulling may conflict or surprise-overwrite WIP.
- **allowlisted auto-commit** = agent commits only the FAW dirty allowlist above, then pulls; unrelated paths still abort.

| # | Topic | Typical options | Disclosed default if unanswered / Choose |
| --- | --- | --- | --- |
| Q1 | **Remote / branch** | A = pull `origin` into current tracking (usually `main`↔`origin/main`); B = other remote/branch | **A** if already on `main`↔`origin/main` |
| Q2 | **Combine strategy** | A = `git pull --ff-only` (or fetch + ff-only merge); B = allow merge commit; C = rebase | **A** for FAW pull goals — **no** merge/rebase fallback when A |
| Q3 | **Dirty working tree** | A = **allowlisted auto-commit then pull** (abort only for unrelated/non-allowlist dirty); B = abort any dirty (list paths, no stash); C = stash then pull; D = commit all WIP then pull | **A** (FAW default — agent clears session/FAW-meta dirt; unrelated still aborts) |
| Q3b | **On non-ff / conflict after allowlist commit** | A = fail-closed; keep WIP allowlist commit recoverable; no force/hard reset/merge/rebase; B = merge or rebase to absorb remote | **A** |
| Q4 | **Git root** | A = this org-repo root only; B = also touch sibling trees | **A** |
| Q5 | **Who must succeed** | A = agent Shell pull must succeed (dual preflight); B = user terminal OK as success | **A** for FAW pull goals |
| Q6 | **On failure** | A = fail-closed + typed `blocker_type` + still self-improver; B = retry with merge/rebase/force | **A** |
| Q7 | **Session docs** | A = full FAW artifacts under this session; B = minimal notes | **A** |

### Unanswered → Choose defaults

After the user answers the batch (even partially): any **unanswered** item that had a disclosed default → treat as **Choose→that default**. Lock in `notes.md` with Source `Choose (unanswered→default)` + one-line rationale. Do **not** leave “Choose” or blanks for researcher/planner/implementer. Re-ask only if the default would be irreversible corpus FS mutation (pull pack defaults are not).

## Windows agent pull (standing constraints)

- **Dual preflight** (same idea as publish): remote scheme + tracking; **agent** git/GCM. Prefer **Git for Windows** absolute `...\Git\cmd\git.exe` when PATH `git` is MSYS without helper.
- Use the **same GfW binary** for dirty gate (`status --porcelain`), allowlist commit, **and** pull — MSYS porcelain counts can skew and mis-trigger abort or false clean.
- Missing `gh` alone ≠ `user_credentials` when GCM works.
- **`blocker_type`:**
  - **`dirty_working_tree`** — porcelain has paths **outside** the allowlist (unrelated dirty) and policy aborts. Auth may still be green. Remediation: user clean/stash/commit those paths, then **new** pull cycle — do **not** relaunch implementer on the same unrelated dirty tree for the same goal. (**Not** used when dirt ⊆ allowlist — agent auto-commits then pulls.)
  - **`other`** (or plan vocabulary `non_ff`) — allowlist commit left local tip diverged from remote; `--ff-only` refused. Keep WIP commit recoverable; do **not** merge/rebase unless user later changes Q2. Session **`blocked`**; sync AC unmet.
  - **`agent_environment`** — wrong git binary / sandbox blocking GCM or non-interactive pull.
  - **`user_credentials`** — true credential/login failure (not “missing gh” alone when GCM works).
- Fail-closed: unrelated dirty-abort, non-ff refuse, or pull/auth fail → session **`blocked`** (never `complete`); **self-improver still runs**.
- Auditor:
  - Allowlisted dirt → agent commit then pull attempted = **correct path** (not “user must clean session dirt”).
  - Correct **unrelated** dirty-abort = **process pass** with sync AC **unmet**; `rework_owner: user` — not implementer defect.
  - Expected post-allowlist **non-ff** block = **process pass** + session `blocked` (sync AC unmet) — not implementer defect for refusing merge/rebase.

## Out of scope for a pure pull cycle

- Corpus moves/renames/deletes; taxonomy final ratification; must-preserve lock
- Force-push, hard reset, merge/rebase fallbacks when Q2=A, autostash unless user chose Q3=C
- Auto-committing or stashing **non-allowlist** paths; commit-all WIP as default
- Treating “user terminal can pull” as success when agent pull failed or aborted
- Marking session `complete` because auth was green while unrelated dirty or non-ff blocked sync
