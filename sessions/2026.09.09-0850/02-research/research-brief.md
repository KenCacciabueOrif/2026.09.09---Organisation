# Research brief

## Goal (from refined prompt)

Enable future `/full-agent-workflow` cycles to `git push` from **agent Shell** when the interactive user terminal can already push (GCM / machine credentials), without storing secrets. Prefer documenting Shell/git/GCM/preflight/fail-closed behavior in org tooling; SSH/`gh` only as researched fallbacks.

## Recommended approach options

### Option A — Prefer Git for Windows + GCM in agent push path; dual preflight; fail-closed (recommended)

**What to implement (docs/rules/agents/templates only):**

1. **Windows push guidance:** For HTTPS GitHub on Windows, agents must prefer `C:\Users\<user>\AppData\Local\Programs\Git\cmd\git.exe` (or whatever `where.exe git` lists that has `credential.helper manager`) over MSYS (`C:\msys64\usr\bin\git.exe`) when those differ.
2. **Dual preflight** (researcher + planner + implementer before commit+push):
   - **Remote:** scheme (`https` vs `ssh`), tracking branch.
   - **Agent can push:** `(Get-Command git).Source`; `git config --show-origin --get-regexp credential`; prefer GfW; `git credential fill` or `git push --dry-run` **using that binary** without first forcing `GCM_INTERACTIVE=0` (allow GCM to read Windows Credential Manager). Do **not** print password lines; log only success/fail + key names / exit codes.
   - **User can push:** optional note if user already pushed from integrated terminal; never treat that alone as agent-ready.
   - **`gh`:** record present/absent; absence is **not** sufficient to declare credentials missing if GCM fill succeeds.
3. **Fail-closed:** If agent preflight fails → `blocked` with remediation that distinguishes:
   - `blocker_type`-style nuance in docs: **agent_environment** (wrong git on PATH, sandbox/Legacy Terminal) vs **user_credentials** (no store entry / need `gh auth login` / SSH setup).
4. **Do not** dump full `Get-ChildItem Env:` in session logs (agent may inject `GITHUB_TOKEN` / similar).
5. **Cursor settings note (short):** If GfW+GCM still fails only in agent Shell: disable sandbox auto-run / enable Legacy Terminal Tool / approve out-of-sandbox run when UI offers it ([Run Modes](https://cursor.com/docs/agent/security/run-modes), forum Legacy Terminal guidance).
6. Preserve honesty: never `complete` when push criterion unmet; still run `self-improver`.

**Tradeoffs:** Small, reviewable doc diffs; matches live proof that GfW+GCM works in agent Shell today; no secrets; no remote rewrite. Requires PATH/git discipline every push.

### Option B — Install `gh` + `credential.helper '!gh auth git-credential'` (fallback)

**Tradeoffs:** Portable across tools that ignore GfW system config; requires user install + `gh auth login`; heavier than Option A when GCM already works. Keep as documented fallback if Option A preflight fails after PATH fix.

### Option C — Rewrite `origin` to SSH (fallback)

**Tradeoffs:** Avoids HTTPS helper entirely; needs SSH key agent access (sandbox may still block `~/.ssh`); user setup; refined prompt says do **not** default to this without justification. Document only as fallback.

## Required facts (verified)

| Fact | Evidence |
| --- | --- |
| Remote | HTTPS `origin` → `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| Branch | `main` tracks `origin/main`; currently in sync at `9708f2e` |
| Prior agent push error | `terminal prompts disabled` (0831 implementer log) |
| User terminal later pushed | Same commit reached `origin` without re-auth (SESSION / refined prompt) |
| Default agent `git` | MSYS `C:\msys64\usr\bin\git.exe` — **no** `credential.helper` |
| GfW `git` | `…\Programs\Git\cmd\git.exe` — system `credential.helper manager` |
| GCM store usable from agent Shell via GfW | `credential fill` OK; `push --dry-run` → `Everything up-to-date` |
| MSYS in agent Shell | Prompt-disabled → fatal; interactive → **hang** |
| `gh` | Not on PATH |
| `GITHUB_TOKEN` in agent env | Present (value must never be logged); not relied on by plain git HTTPS |
| Shell `required_permissions` in this harness | **Not** exposed on Shell tool schema used here |
| Secrets in repo | Out of scope to add; none required for Option A |

## Unknowns

- Whether every Cursor Run Mode / sandbox policy on this machine will always allow GCM DPAPI/Credential Manager access (today’s Shell allowed GfW fill without an explicit `all` permission flag).
- Whether user interactive terminal uses GfW, GitHub Desktop git, or another binary (not probed in user terminal); irrelevant once agent is instructed to use GfW explicitly.
- Cloud Agents / separate VMs: out of scope beyond a short note (refined prompt).

## Risks and blockers

| Item | Severity | Notes |
| --- | --- | --- |
| **Agent push credentials (MSYS default)** | High (process) | Still a **workflow** risk until docs force GfW; **not** “machine has no GitHub creds.” |
| False `user_credentials` blocked | Medium | Calling user to re-login when GCM already works wastes cycles; classify agent_environment. |
| Env secret leakage into session logs | High if mishandled | Never echo `GITHUB_TOKEN` / credential fill passwords into `sessions/`. |
| Over-aggressive `GIT_TERMINAL_PROMPT=0` | Medium | Can make GfW+GCM look broken; use for MSYS fail-fast only. |
| Sandbox regression | Low–medium | Mitigate with Settings / elevated run note. |
| SSH/`gh` as default | Avoid | Secondary options only. |

### Publish / push preflight (this goal includes remote publish tooling)

| Check | Result |
| --- | --- |
| Remote URL scheme | **https** |
| Tracking | `main` → `origin/main` |
| `gh` installed | **no** |
| `gh auth status` | N/A |
| Credential helper (default `git`) | **none** (MSYS) |
| Credential helper (GfW) | **manager** — **verified working** for non-secret fill + dry-run push |
| Agent can push (with GfW) | **yes** (dry-run) |
| Agent can push (default PATH git) | **no** |
| Blocker for “user has no creds” | **no** |
| Blocker for “default agent `git push` as-is” | **yes** — wrong git binary / no helper until workflow docs enforce GfW path |
| Secrets to commit | **none** |

**Do not report `blockers: none`.** Remaining process blocker: workflow docs do not yet encode Option A. Machine GCM credentials for agent **are** available via GfW.

## Canonical references

- Refined prompt: `sessions/2026.09.09-0850/01-prompt-betterment/refined-prompt.md`
- Codebase findings: `sessions/2026.09.09-0850/02-research/codebase-findings.md`
- Online findings: `sessions/2026.09.09-0850/02-research/online-findings.md`
- Prior failure: `sessions/2026.09.09-0831/04-implementation/log.md`, `05-audit/report.md`
- https://cursor.com/docs/agent/security/run-modes
- https://cursor.com/docs/agent/tools/terminal
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/environment.md
- https://forum.cursor.com/t/agent-cannot-run-git-push-or-other-authenticated-commands-no-access-to-user-credentials/151256

## Ready for planner

**Yes** — recommend **Option A**. Acceptance criteria can be verified by doc checklist + optional agent smoke: invoke GfW `git push --dry-run` (or fill) without logging secrets; default MSYS path must be documented as unsafe for HTTPS push.
