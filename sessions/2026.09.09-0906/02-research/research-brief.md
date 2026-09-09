# Research brief

## Goal (from refined prompt)

Stage **all** dirty + untracked files (secrets gate only), create **one** auto-generated commit on `main`, **push** to `origin` from agent Shell (no PR). Prefer **Git for Windows + GCM** when PATH git is MSYS / lacks helper. Dual preflight required; fail-closed with `blocker_type`.

## Recommended approach options

### Option A — Stage all → one commit → push with GfW absolute `git.exe` (recommended)

1. Dual-preflight already green for GfW (see table below).
2. Secrets gate: clear on current tree; re-scan porcelain names before `git add`.
3. `git add -A` (or equivalent full-tree stage) from repo root.
4. Auto commit message from staged diff + recent log style (imperative, why-focused); BOM-safe PowerShell here-string `-m` (or utf8NoBOM `-F`).
5. Push with **`C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe`** (not PATH/MSYS): `git push origin main` (or `HEAD` while on `main`); no `--force`.
6. Report commit hash, push OK, final `git status`.

**Tradeoffs:** Matches refined prompt and live agent evidence; no PATH rewrite; no PR; missing `gh` irrelevant. Must discipline binary choice every push.

### Option B — Install `gh` + `credential.helper '!gh auth git-credential'` (fallback)

**Tradeoffs:** Useful if GfW+GCM regresses; requires user install/login; heavier than A. Do **not** choose first while GCM fill/dry-run succeed.

### Option C — Switch `origin` to SSH (fallback)

**Tradeoffs:** Avoids HTTPS helper; needs SSH agent in agent Shell; refined prompt forbids default rewrite. Only if A fails after GfW attempt.

## Required facts (verified this session)

| Fact | Evidence |
| --- | --- |
| Branch | `main` → `[origin/main]`; ahead/behind **0/0** at `9708f2e` |
| Dirty | 22 modified + untracked `sessions/2026.09.09-0850/`, `sessions/2026.09.09-0906/` |
| Diff theme | Option A push/docs + session artifacts + 0831 retrofits (~270/40 on tracked) |
| Remote | HTTPS `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| PATH `git` | `C:\msys64\usr\bin\git.exe` (also listed: GfW after it on `where.exe`) |
| PATH helper | **none** (exit 1 on get-regexp) |
| GfW `git` | `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` — `git version 2.54.0.windows.1` |
| GfW helper | system `credential.helper manager` (`...\Git\etc\gitconfig`) |
| GfW `credential fill` | **pass** — exit 0; `has_username=True`; `has_password=True` (**values not logged**) |
| GfW `push --dry-run` | **pass** — exit 0; `Everything up-to-date` |
| MSYS dry-run + `GIT_TERMINAL_PROMPT=0` | **fail** exit 128 — `terminal prompts disabled` |
| `gh` | **not installed** (optional signal only) |
| `GITHUB_TOKEN` in agent env | **present** (boolean only; do not rely on / log value) |
| Secrets-like dirty paths | **none** |
| Recent commit style | Short imperative subjects |

## Unknowns

- Whether a future Cursor sandbox/Run Mode change could block GCM DPAPI even via GfW (today’s agent Shell: fill + dry-run OK without special PATH rewrite).
- Exact final commit subject wording until staged diff is frozen (theme known; implementer auto-generates).
- Whether session `0906` late-phase files created after this research need inclusion (stage-all at implement time covers them).

## Risks and blockers

| Item | Severity | `blocker_type` | Notes |
| --- | --- | --- | --- |
| Using PATH/MSYS `git push` | High if ignored | `agent_environment` | Proven fatal without TTY |
| Accidental secret staging | High if mishandled | halt (secrets gate) | Re-scan before add; none now |
| UTF-8 BOM in commit subject | Medium | process | Use here-string / utf8NoBOM |
| Force-push / amend / config edits | High if done | out of scope | Forbidden by refined prompt |
| Missing `gh` | None for Option A | — | Not a credential failure while GCM works |

### Publish / push dual preflight (mandatory)

| Field | Value |
| --- | --- |
| Remote URL scheme | **https** |
| Tracking branch | `main` → `origin/main` |
| Agent git path (`Get-Command`) | `C:\msys64\usr\bin\git.exe` |
| `where.exe git` | (1) MSYS `...\msys64\usr\bin\git.exe` (2) GfW `...\Programs\Git\cmd\git.exe` |
| Agent `credential.helper` (default/PATH binary) | **none** |
| Prefer GfW path (Windows HTTPS)? | **yes** — `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| GCM / non-interactive evidence | **pass** (GfW fill + `push --dry-run`; no secrets logged) |
| `gh` present? | **no** (optional only) |
| User-terminal push note | Prior cycles: user terminal could push while agent MSYS failed; **not** treated as agent-ready alone |
| Agent push ready (with GfW)? | **yes** |
| Agent push ready (PATH/MSYS as-is)? | **no** |
| `blocker_type` (for Option A implement path) | **none** |
| `blocker_type` (if implementer uses PATH git) | **agent_environment** |
| Blocker / remediation | Use GfW absolute path for commit-adjacent push/preflight; do not mark complete if push fails |

**Orchestrator blockers list for Option A:** `none` (agent can push via GfW). Do **not** claim credentials missing solely because `gh` is absent.

## Canonical references

- Refined prompt: `sessions/2026.09.09-0906/01-prompt-betterment/refined-prompt.md`
- Codebase findings: `sessions/2026.09.09-0906/02-research/codebase-findings.md`
- Online findings: `sessions/2026.09.09-0906/02-research/online-findings.md`
- Prior Option A proof: `sessions/2026.09.09-0850/02-research/research-brief.md`
- Implementer law: `.cursor/agents/implementer.md`
- Skill Critical: `.cursor/skills/full-agent-workflow/SKILL.md`
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/environment.md
- https://forum.cursor.com/t/agent-cannot-run-git-push-or-other-authenticated-commands-no-access-to-user-credentials/151256

## Ready for planner

**Yes** — recommend **Option A**. Acceptance criteria are implementable: stage-all (secrets clear), one BOM-safe commit on `main`, push via GfW, report hash + status; fail-closed only if live push regresses.
