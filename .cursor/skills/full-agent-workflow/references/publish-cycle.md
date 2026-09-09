# Publish cycle (org-repo git add / commit / push)

Use when the user asks to **publish**, **git add/commit/push**, or otherwise sync this organisation repo to `origin`. Keep mutation class **`docs_only`** unless they also asked for corpus moves.

## Git-root boundary (hard)

- Operate only inside this repo’s git root (`git rev-parse --show-toplevel`).
- Never `git add` / commit / push paths from sibling trees (e.g. other folders under a multi-root `C:\Project` workspace).
- Encode as acceptance criteria: “all git ops confined to this org-repo root.”

## Dirty allowlist (FAW default — mirror of pull-cycle)

When porcelain blocks publish readiness and the goal is FAW session/meta work, the agent **may auto-commit only** these paths (prefer commit over stash):

| Include | Paths |
| --- | --- |
| Sessions | `sessions/**` |
| FAW meta | `.cursor/skills/full-agent-workflow/**` |
| FAW meta | `.cursor/agents/**` |
| FAW meta | `.cursor/rules/**` |
| FAW meta | `AGENTS.md` |
| FAW meta | `sessions/_templates/**` |

**Outside allowlist** → do **not** auto-commit or stash those paths; **abort** with listed paths and `blocker_type: dirty_working_tree`; session `blocked`. Unrelated dirty still requires user cleanup (or a narrower user-approved stage list).

## Question pack (ask once; informed consent)

Ask a short batch. For **every** question: plain-language explanation + what each choice commits to + pros/cons. Prefer everyday words; define `fail-closed` / `docs_only` / allowlisted auto-commit in one sentence if used.

| # | Topic | Typical options | Disclosed default if unanswered / Choose |
| --- | --- | --- | --- |
| Q1 | **Stage scope / git root** | A = this org-repo root only (all non-secret work); B = narrower path list | **A** |
| Q2 | **Commit message** | A = user supplies; B = agent drafts after staging (why-focused, repo style, ≤~72 chars, BOM-safe) | **B** |
| Q3 | **Who must push** | A = agent Shell must succeed (dual preflight); B = user terminal OK | **A** for FAW publish goals |
| Q4 | **Remote / branch** | A = non-force `origin/main` (or current tracking); B = other remote/branch | **A** if already on `main`↔`origin/main` |
| Q5 | **Excludes** | A = default secret/junk only; B = extra user exclude list | **A** |
| Q6 | **One commit vs split** | A = exactly one commit then push; B = topic-split commits | **A** for “add commit push” catch-up |
| Q7 | **Include current session** | A = write required session logs before commit; accept post-push dirty finalize; B = exclude this session folder | **A** |
| Q8 | **Dirty autonomy** | A = **allowlisted auto-commit** of session/FAW-meta paths (same allowlist as pull-cycle) then stage/push per Q1–Q7; abort only for unrelated dirty; B = abort any unexpected dirty (user cleans); C = stash then publish | **A** for FAW publish goals |

### Unanswered → Choose defaults

After the user answers the batch (even partially): any **unanswered** item that had a disclosed default → treat as **Choose→that default**. Lock in `notes.md` with Source `Choose (unanswered→default)` + one-line rationale. Do **not** leave “Choose” or blanks for researcher/planner/implementer. Re-ask only if the default would be irreversible corpus FS mutation (publish pack defaults are not).

## Windows agent push (standing constraints)

- Dual preflight: remote + agent git/GCM. Prefer **Git for Windows** absolute `...\Git\cmd\git.exe` when PATH `git` is MSYS without helper. Same GfW binary for status, allowlist commit, and push.
- Missing `gh` alone ≠ `user_credentials` when GCM works.
- Fail-closed: agent push fail → session `blocked` + `blocker_type` (`agent_environment` vs `user_credentials`); never mark complete on local-only commit. Unrelated dirty abort → `dirty_working_tree`; self-improver still runs.
- Single-commit + post-push session dirtiness: expected; auditor grades **Low**, not rework.
- No force-push, hard reset, or `--no-verify`.

## Out of scope for a pure publish cycle

- Corpus moves/renames/deletes; taxonomy final ratification; must-preserve lock
- Force-push, amend of already-pushed commits, `--no-verify`, git config changes
- Auto-committing or stashing **non-allowlist** paths as default
- Treating “user terminal can push” as success when agent push failed
