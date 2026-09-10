# Research brief — Publish cycle (`sessions/2026.09.09-1246`)

## Goal (from refined prompt)

Stage **all non-secret** modified + untracked work **inside this org-repo git root only**, create **exactly one** agent-drafted why-focused commit, and **agent Shell** non-force push to **`origin/main`**. Mutation class: **docs_only**. Fail-closed if push fails. No corpus moves; no PR; no taxonomy/must-preserve mutation.

## Recommended approach options (max 3)

### Option A — Stage-all → one BOM-safe commit → push via GfW absolute path (**recommended**)

1. Re-confirm dual preflight at implement start (remote + GfW helper).
2. Write required `sessions/2026.09.09-1246/` implementation/session logs **before** commit.
3. Secrets name re-scan; `git add -A` (or equivalent) from **this root only**.
4. Draft commit message after staging (imperative, why-focused, ≤~72 chars; match `4de6aeb` style; **no BOM** — prefer here-string `-m`).
5. Push with **`C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe`**: print remote + branch, then `push origin main` (no `--force`).
6. Verify `git status -sb` / `git log -1` / upstream; accept known post-push session-log dirtiness (Q7=A).

**Tradeoffs:** Matches locked AC and live evidence; large mixed-topic catch-up commit (harder to revert by topic); requires discipline to never use PATH/MSYS for push.

### Option B — Install/login `gh` and use `gh` as credential helper (fallback)

**Tradeoffs:** Useful only if GfW+GCM regresses; heavier user setup. Do **not** choose while GCM fill + dry-run succeed. Missing `gh` today is **not** a blocker for Option A.

### Option C — Switch `origin` to SSH (fallback)

**Tradeoffs:** Avoids HTTPS helper; needs working SSH agent in agent Shell; refined prompt does not ask to rewrite remote. Only if A fails after GfW attempt and user approves.

## Required facts (verified this session)

| Fact | Evidence |
| --- | --- |
| Git root | `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` |
| Remote | HTTPS `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| Tracking | `main` → `origin/main`; ahead/behind **0/0** at `4de6aeb` |
| Dirty scope | ~46 modified + untracked `catalogue/`, `program/`, sessions `0929`/`1009`/`1032`/`1246` |
| Secrets-like paths | **none** found (name scan); no `.gitignore` |
| Commit style | Imperative why subjects; `9708f2e` shows BOM hazard |
| PATH `git` | `C:\msys64\usr\bin\git.exe` (MSYS 2.55.0); `where`: MSYS then GfW |
| PATH `credential.helper` | **none** (empty get-regexp / config list) |
| GfW `git` | `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (2.54.0.windows.1) |
| GfW helper | `credential.helper manager` (system) |
| GfW `credential fill` | **pass** — `has_username=True`, `has_password=True` (**values not logged**) |
| GfW `push --dry-run` | **pass** — exit 0; `Everything up-to-date` |
| MSYS `push --dry-run` + `GIT_TERMINAL_PROMPT=0` | **fail** — exit 128; `could not read Username … terminal prompts disabled` |
| `gh` | **not installed** (optional only) |
| `GITHUB_TOKEN` in agent env | **present** (boolean only; do not log value; do not treat as sole publish path) |
| User terminal | Historical successful `git push -u origin main` in terminal `1.txt`; **not** agent-ready alone |
| Docs_only / plan-gate | No corpus FS mutation → plan-gate before implementer **not** required for moves |

## Unknowns

- Exact final commit subject until staged set is frozen at implement time.
- Whether late-phase files under `sessions/2026.09.09-1246/` after research will expand the staged set (stage-all at commit time covers them).
- Whether a future Cursor sandbox change could break GCM DPAPI even via GfW (today: fill + dry-run OK).

## Risks and blockers

| Item | Severity | `blocker_type` | Notes |
| --- | --- | --- | --- |
| PATH/MSYS `git push` | High if used | `agent_environment` | Proven fail under `GIT_TERMINAL_PROMPT=0` |
| Accidental secret staging | High if mishandled | halt (secrets gate) | Re-scan; none now |
| UTF-8 BOM in subject | Medium | process | Avoid `Set-Content -Encoding utf8` on Win PS 5.1 |
| Mixed-topic single commit | Medium | product | Locked Q6=A; document in message “why” |
| Force-push / amend / config | High if done | out of scope | Forbidden |
| Missing `gh` | None for Option A | — | Not credential failure while GCM works |
| Claiming complete on local-only commit | High if done | process | Fail-closed per AC |

### Publish / push dual preflight (mandatory)

| Field | Value |
| --- | --- |
| Remote URL scheme | **https** |
| Tracking branch | `main` → `origin/main` |
| Agent git (`Get-Command`) | `C:\msys64\usr\bin\git.exe` |
| `where.exe git` | (1) MSYS `...\msys64\usr\bin\git.exe` (2) GfW `...\Programs\Git\cmd\git.exe` |
| PATH binary `credential.helper` | **none** |
| Prefer GfW (Windows HTTPS)? | **yes** — `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| GCM / non-interactive evidence | **pass** (GfW fill + `push --dry-run`; no secrets logged) |
| `gh` present? | **no** (optional only) |
| User-terminal note | User previously pushed successfully; **≠** agent-ready alone |
| Agent push ready (GfW Option A)? | **yes** |
| Agent push ready (PATH/MSYS as-is)? | **no** |
| `blocker_type` (Option A path) | **none** |
| `blocker_type` (if PATH git used for push) | **agent_environment** |

**Orchestrator blockers for recommended Option A:** `none` (agent can push non-interactively via GfW). Do **not** claim credentials missing solely because `gh` is absent. Do **not** say “blockers: none” if implementer were forced to use PATH/MSYS only.

## Canonical references

- Refined prompt: `sessions/2026.09.09-1246/01-prompt-betterment/refined-prompt.md`
- Notes (locks): `sessions/2026.09.09-1246/01-prompt-betterment/notes.md`
- Codebase findings: `sessions/2026.09.09-1246/02-research/codebase-findings.md`
- Online findings: `sessions/2026.09.09-1246/02-research/online-findings.md`
- Prior Option A brief: `sessions/2026.09.09-0906/02-research/research-brief.md`
- Law: `AGENTS.md`, `.cursor/skills/full-agent-workflow/SKILL.md`, `sessions/_templates/03-plan.md`
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/credstores.md
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-content?view=powershell-7.6

## Ready for planner

**Yes** — recommend **Option A**. `docs_only` publish plan: stage-all (secrets clear), one BOM-safe commit, push via GfW absolute path to `origin/main`, fail-closed with typed blocker only if live push regresses.
