# Research brief — Pull-autonomy (`sessions/2026.09.09-1350`)

## Goal (from refined prompt)

1. Update FAW **pull** + **publish** dirty policy: allowlisted auto-commit then `git pull --ff-only` / push readiness; abort only for **unrelated** dirty.  
2. Same session: after docs land, agent Shell allowlist-commit if needed, then GfW `git pull --ff-only` of `origin` into `main`↔`origin/main`.  

Git root only: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`. Mutation: **`docs_only`** + org-repo git ops. Taxonomy / must-preserve: out of scope.

Locked Choose (notes.md): Q1–Q9 defaults; Q3 = **E→B** allowlist then pull; Q3b = fail-closed keep WIP commit; Q8 = docs first then same-session pull; Q9 = mirror on publish.

## Recommended approach options (max 3)

### Option A — Docs → allowlist commit → GfW `pull --ff-only` (**recommended**)

1. Update `pull-cycle.md` Q3/defaults/blocker text + allowlist table; mirror in `publish-cycle.md`; align `SKILL.md`, rule, `AGENTS.md`, agents, handoff/session-structure (remove “any dirty → user cleanup only”).  
2. Dual preflight with **GfW** absolute path (same binary for porcelain, commit, pull).  
3. Classify porcelain: if any **unrelated** → abort `dirty_working_tree`, session `blocked`.  
4. If dirty ⊆ allowlist (today: **23 / 0**): stage allowlist only; BOM-safe why-focused commit (repo style); no `--no-verify`.  
5. `git pull --ff-only` via GfW. On non-ff / conflict: fail-closed (Q3b/Q6); leave allowlist commit recoverable; typed blocker; session `blocked`; **self-improver still runs**.  
6. Never mark `complete` on user-terminal pull alone (Q5=A).

**Tradeoffs:** Matches all locks and AC ordering. **Auth green; unrelated dirty = 0.** After allowlist commit while remote is at `489f03a`, local and remote **diverge** → `--ff-only` is **unlikely to succeed** this turn — but AC 9–10 allow correct fail-closed as success-of-process. Does not invent stash/merge/rebase.

### Option B — Pull-while-dirty then commit

Try `pull --ff-only` before committing WIP, then commit allowlist.

**Tradeoffs:** **Rejected for this tree.** Seven dirty paths overlap `HEAD..origin/main` files → overwrite abort. Also conflicts with locked “commit over stash” autonomy framing and Q8 docs-first commit of policy edits.

### Option C — Allowlist commit then merge/rebase to absorb `489f03a`

**Tradeoffs:** Would likely sync remote session `1313`, but **violates Q2=A** and out-of-scope (no rebase-as-default / merge commits unless later cycle). Forbidden without new user Choose.

## Required facts (verified this session)

| Fact | Evidence |
| --- | --- |
| Git root | Org path (GfW `rev-parse --show-toplevel` OK) |
| Remote scheme | **https** → `github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| Tracking | `main` → `origin/main` |
| Local HEAD | `f5012d6` |
| Remote tip | **`489f03a`** (`ls-remote` + fetch) |
| Ahead/behind (post-fetch, pre-commit) | **0 / 1** |
| GfW porcelain | **23** lines |
| Allowlisted / unrelated | **23 / 0** |
| Dirty↔remote file overlap | **7** paths (see codebase-findings) |
| PATH `git` | `C:\msys64\usr\bin\git.exe`; `where`: MSYS then GfW |
| PATH `credential.helper` | **none** (get-regexp empty) |
| GfW `git` | `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (2.54.0.windows.1) |
| GfW helper | `credential.helper manager` |
| GfW `credential fill` | **pass** — `has_username=True`, `has_password=True` (values **not** logged) |
| GfW `fetch` / dry-run | **pass** — `f5012d6..489f03a` |
| `gh` | **absent** (optional only) |
| `GITHUB_TOKEN` present | **True** (boolean only; not sole auth path) |
| Prior 1332 | Blocked `dirty_working_tree` under Q3=A; 15 paths; introduced abort-default `pull-cycle.md` |
| MSYS porcelain | **112** — do not use for gate |

### Allowlist (locked)

`sessions/**`, `.cursor/skills/full-agent-workflow/**`, `.cursor/agents/**`, `.cursor/rules/**`, `AGENTS.md`, `sessions/_templates/**`.

## Pull / auth dual preflight (mandatory)

| Field | Value |
| --- | --- |
| Remote URL scheme | **https** |
| Tracking branch | `main` → `origin/main` |
| Agent git (`Get-Command`) | `C:\msys64\usr\bin\git.exe` |
| `where.exe git` | (1) MSYS (2) GfW |
| PATH binary `credential.helper` | **none** |
| Prefer GfW (Windows HTTPS)? | **yes** — `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| GCM / non-interactive evidence | **pass** (fill + fetch; no secrets logged) |
| `gh` present? | **no** (optional only) |
| User-terminal note | Historical push success ≠ agent-ready alone |
| Agent **auth** ready (GfW)? | **yes** |
| Allowlisted dirty count | **23** |
| Unrelated dirty count | **0** |
| Agent **ff-only pull** ready right now (clean fast-forward)? | **no** — behind 1 + dirty overlaps; after allowlist commit → **diverged** vs `489f03a` |
| `blocker_type` (auth) | **none** |
| `blocker_type` (unrelated dirty under new policy) | **none** (unrelated = 0) |
| Expected post-commit pull outcome | **`pull --ff-only` fail** → fail-closed; classify as non-ff / history diverge (**not** `dirty_working_tree`, **not** missing credentials). Use implementer vocabulary already allowed (`blocked` + accurate type / outcome e.g. `non_ff` / `other` as plan encodes) |
| If PATH/MSYS forced for auth ops | **`agent_environment`** |

**Do not claim `blockers: none` for the pull goal** while ff-only sync cannot succeed. Auth is green; allowlist policy unblocks the *dirty-abort* deadlock, but **does not** make ff-only succeed against an already-advanced remote once a local allowlist commit exists.

## Unknowns

- Exact merge conflicts if a future cycle allows merge/rebase onto `489f03a` (out of scope now).  
- Whether implement-time porcelain gains non-allowlist paths (re-classify at implement).  
- Whether remote gains more commits before implement pull attempt.

## Risks and blockers

| Item | Severity | Classification | Notes |
| --- | --- | --- | --- |
| Divergent history after allowlist commit vs `489f03a` | **High for pull success** | fail-closed non-ff (Q2/Q3b) | Expected under Option A; do not force/merge/rebase |
| Overlap dirty vs remote (7 files) | High if pull-before-commit | process | Reinforces commit-first |
| Unrelated dirty appearing mid-cycle | Medium | `dirty_working_tree` | Abort; list paths |
| PATH/MSYS used for gate/pull | High if used | `agent_environment` | Empty helper; porcelain skew |
| Auth / GCM failure | High if appears | `user_credentials` or `agent_environment` | Today fill+fetch **pass** |
| Docs still say “abort any dirty / user cleanup” | Medium | plan completeness | AC A must rewrite auditor/orchestrator remediation |
| Secrets in allowlist commit | High if done | process | Never commit secrets; scan stage list |
| Taxonomy / must-preserve | None | out of scope | Do not gate |

## Canonical references

- Refined prompt: `sessions/2026.09.09-1350/01-prompt-betterment/refined-prompt.md`  
- Notes (locks): `sessions/2026.09.09-1350/01-prompt-betterment/notes.md`  
- Codebase findings: `sessions/2026.09.09-1350/02-research/codebase-findings.md`  
- Online findings: `sessions/2026.09.09-1350/02-research/online-findings.md`  
- Prior blocked pull: `sessions/2026.09.09-1332/`  
- Targets: `references/pull-cycle.md`, `references/publish-cycle.md`, skill/rule/agents/`AGENTS.md`/handoffs  
- https://git-scm.com/docs/git-pull  
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md  

## Ready for planner

**`ready_to_implement: yes`** for Option A:

1. **Docs first** (AC A) — mutation `docs_only`; no corpus plan-gate.  
2. **Re-run GfW dual preflight + allowlist classification** at implement.  
3. **Allowlist commit** when unrelated = 0.  
4. **Attempt** GfW `pull --ff-only`; record SHAs / exit.  
5. If non-ff: session **`blocked`**, accurate blocker (not false `complete`); self-improver still runs.  
6. If somehow ff succeeds: verify HEAD == remote tip; continue audit.

**Planner should disclose:** under current remote tip `489f03a`, same-session **pull success is unlikely** after the required allowlist commit; **correct fail-closed** still meets AC 9–10. Do not expand to merge/rebase without a new user decision.

**Orchestrator summary fields**

- Auth readiness: **green** (GfW+GCM)  
- Allowlisted dirty: **23**  
- Unrelated dirty: **0**  
- `blocker_type` now (new policy): **none** for dirty/auth  
- Pull ff-only readiness: **not ready** (behind + post-commit diverge expected)  
- Recommendation: **ready_to_implement yes** (docs + allowlist commit + ff-only attempt / fail-closed)
