# Codebase findings

Session: `sessions/2026.09.09-0850/` — agent Shell `git push` vs interactive terminal.

## Prior failure evidence

| Path | Why it matters |
| --- | --- |
| `sessions/2026.09.09-0831/04-implementation/log.md` | Implementer push failed: `fatal: could not read Username for 'https://github.com': terminal prompts disabled`; noted `gh` missing; left commit `9708f2e` local. |
| `sessions/2026.09.09-0831/05-audit/report.md` | Audit **fail** on push criterion; `git push --dry-run` hung awaiting credentials in audit env; recommended user auth (partially wrong diagnosis once user later pushed without re-login). |
| `sessions/2026.09.09-0831/02-research/research-brief.md` | Prior research listed push auth as “Unknown until push” / **blockers for planning: none** — late discovery of auth. |
| `sessions/2026.09.09-0831/06-self-improvement/*` | Already added early auth preflight, `blocked` + `blocker_type: user_credentials`, no false complete, BOM-safe commits — but **did not** distinguish wrong `git` binary / GCM inheritance. |
| `sessions/2026.09.09-0850/SESSION.md` + `01-prompt-betterment/refined-prompt.md` | Current goal: durable agent Shell push when user terminal already can; secret-free. |

## Current workflow surface (push / auth)

| Path | Current guidance | Gap vs this research |
| --- | --- | --- |
| `.cursor/agents/researcher.md` | Push preflight: remote scheme, `gh`, credential evidence; list credential blockers | Does not require `where git` / GfW vs MSYS / `credential.helper` probe; does not say “user can push ≠ agent can push”. |
| `.cursor/agents/planner.md` | Auth step; `ready_to_implement: no` if credentials unverified | Same — no PATH/git-binary / GCM preflight checklist. |
| `.cursor/agents/implementer.md` | On prompt-disabled / missing `gh` → `blocked` + `user_credentials` | Treats missing `gh` as primary signal; does not instruct preferring Git for Windows + GCM; no warning against dumping env (secrets). |
| `.cursor/agents/orchestrator.md` | Credential blocker → session `blocked`, no implementer relaunch, still self-improve | Needs nuance: sandbox/PATH misconfig may be **agent_environment** remediation, not only “user must re-login”. |
| `.cursor/agents/auditor.md` | `rework_owner: user` for credentials | Should allow classifying “agent used wrong git / sandbox” vs “no machine credentials”. |
| `.cursor/skills/full-agent-workflow/SKILL.md` | Credential Critical → no relaunch implementer | Same nuance for false `user_credentials` when GCM exists but agent PATH wrong. |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | Researcher must list credential blockers | Extend with agent-vs-user push preflight fields. |
| `.cursor/rules/full-agent-workflow.mdc` | Auth blockers → `blocked`, not complete | Keep honesty; add agent Shell git/GCM note. |
| `AGENTS.md` | Verify remote auth early; never complete if push failed for credentials | Add Windows: prefer GfW `git`, verify helper. |
| `sessions/_templates/02-research-brief.md` / `03-plan.md` | Auth/preflight placeholders | Flesh out dual preflight (user terminal vs agent Shell). |

## Live agent Shell evidence (this research pass)

Commands run from Cursor **agent Shell** (PowerShell), repo root.

| Check | Result |
| --- | --- |
| `git remote -v` | `origin` → `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` (HTTPS) |
| `git branch -vv` | `main` @ `9708f2e` tracking `origin/main` (in sync after user’s successful push) |
| `(Get-Command git).Source` | **`C:\msys64\usr\bin\git.exe`** (MSYS) — first on PATH |
| `where.exe git` | MSYS then `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| PATH order (git-related) | GitHubDesktop\bin → **msys64\usr\bin** → **Programs\Git\cmd** |
| MSYS `git config --get-regexp credential` | **empty** (no helper) |
| GfW system config | `credential.helper manager` in `…/Git/etc/gitconfig` |
| GCM binary | Present under `…\Programs\Git\mingw64\bin\git-credential-manager.exe` |
| `where.exe gh` / `gh auth status` | **`gh` not installed** |
| `GIT_TERMINAL_PROMPT` / `GCM_INTERACTIVE` / `GIT_ASKPASS` | Unset by default in agent Shell |
| `GITHUB_TOKEN` | **Present in agent env** (boolean only; **do not log value**) — plain `git` does not use it for HTTPS push |
| MSYS `git credential fill` + `GIT_TERMINAL_PROMPT=0` | Fail: `terminal prompts disabled` |
| MSYS `git push --dry-run` with prompts disabled | Fail: same error (matches 0831 log) |
| MSYS `git push --dry-run` **without** prompt disable | **Hangs** waiting for Username (no TTY usable) |
| GfW `git credential fill` **without** forcing non-interactive | **Success** — returns `protocol/host/username/password` keys (values not logged) |
| GfW `git push --dry-run origin main` without prompt disable | **Success** — `Everything up-to-date` |
| GfW fill/push with `GCM_INTERACTIVE=0` + `GIT_TERMINAL_PROMPT=0` | Fail: `Cannot prompt because user interactivity has been disabled` |
| `cmdkey /list` (targets redacted) | Windows Credential Manager has GitHub entry for user `https://github.com:KenCacciabueOrif` |
| `git ls-remote origin HEAD` | Succeeds without auth on public repo — **not** a push-auth proof |

## Interpretation

1. Machine **does** have usable GitHub HTTPS credentials via **Windows Credential Manager + Git Credential Manager** when using **Git for Windows**.
2. Default agent `git` is **MSYS**, which has **no credential helper** → must prompt → agent non-TTY / `GIT_TERMINAL_PROMPT=0` → exact 0831 failure.
3. Prior “missing credentials / install `gh`” remediation was **incomplete**: user terminal push worked without new login because GCM already had creds; agent simply used a different `git`.
4. Forcing `GIT_TERMINAL_PROMPT=0` / `GCM_INTERACTIVE=never` in agent preflight can **false-negative** even GfW+GCM; prefer a GfW credential fill / dry-run that allows GCM to read the store, with a timeout, then fail-closed.
5. This harness’s Shell tool schema (researcher session) does **not** expose a `required_permissions` parameter; Cursor product docs/forum still describe sandbox / Legacy Terminal / elevated runs. Document settings-based remediation when GCM cannot read the store from sandbox.

## Must-edit targets for implementer (docs only)

- `.cursor/agents/{researcher,planner,implementer,orchestrator,auditor}.md`
- `.cursor/skills/full-agent-workflow/SKILL.md` + `references/handoff-templates.md`
- `.cursor/rules/full-agent-workflow.mdc`
- `AGENTS.md`
- `sessions/_templates/02-research-brief.md`, `03-plan.md` (and optionally auditor checklist notes)
