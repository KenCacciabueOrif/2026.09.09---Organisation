# Research brief — Pull cycle (`sessions/2026.09.09-1332`)

## Goal (from refined prompt)

Agent-executed `git pull --ff-only` of `origin` into local `main` (tracking `origin/main`), **only** inside  
`C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`.  
Abort if dirty; fail-closed on pull/auth failure; full FAW session docs. Mutation class **`docs_only`** (no corpus FS moves). Taxonomy / must-preserve gates out of scope.

## Recommended approach options (max 3)

### Option A — GfW absolute path; dirty-abort then `--ff-only` (**recommended**)

1. `Set-Location` org root; confirm `rev-parse --show-toplevel` matches org path (GfW binary).
2. Dual preflight re-check: remote HTTPS + GfW `credential.helper manager` + GCM fill boolean / fetch reachability.
3. `git status --porcelain` via **same GfW binary**. If any dirty/untracked → **abort**, list paths, session `blocked` (process: dirty tree — not stash). Still run later self-improver.
4. If clean: `git pull --ff-only` (or equivalent fetch + ff-only merge) via GfW against `origin` / tracking `origin/main`.
5. Record before/after HEAD, `status -sb`, ahead/behind vs `origin/main`.

**Tradeoffs:** Matches all locked Choose answers; correctly blocks today on known dirty tree; uses proven GfW path from publish session `1246`. Does **not** sync remote tip `489f03a` until tree is clean (by design).

### Option B — PATH/MSYS git for pull

**Tradeoffs:** MSYS `credential.helper` empty; status porcelain **inflated** (104 vs GfW 15) — unreliable dirty gate; push historically failed under `GIT_TERMINAL_PROMPT=0`. Fetch dry-run happened to exit 0 today (likely env token / incidental), but **do not** choose while Option A is available. Misuse → `blocker_type: agent_environment`.

### Option C — User-terminal pull only / mark complete without agent Shell

**Tradeoffs:** Violates Q5=A and FAW dual-preflight law. Forbidden.

## Required facts (verified this session)

| Fact | Evidence |
| --- | --- |
| Git root | Org path only (GfW toplevel OK) |
| Remote scheme | **https** → `github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| Tracking | `main` → `origin/main` |
| Local HEAD | `f5012d6` (publish session tip) |
| Remote tip | **`489f03a`** (`ls-remote` + fetch dry-run `f5012d6..489f03a`) |
| Local ahead/behind vs cached `origin/main` | **0/0** (cache still `f5012d6`; real pull would need fetch first) |
| Dirty (GfW) | **Yes — 15 porcelain lines** → Q3=A abort |
| Dirty (MSYS) | 104 lines — **do not use** for gate |
| PATH `git` | `C:\msys64\usr\bin\git.exe`; `where`: MSYS then GfW |
| PATH `credential.helper` | **none** (get-regexp empty / exit 1) |
| GfW `git` | `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (2.54.0.windows.1) |
| GfW helper | `credential.helper manager` |
| GfW `credential fill` | **pass** — `has_username=True`, `has_password=True` (values **not** logged) |
| GfW `fetch --dry-run origin main` | **pass** — exit 0; saw `f5012d6..489f03a` |
| `gh` | **absent** (optional only) |
| `GITHUB_TOKEN` in agent env | **present** (boolean only; not sole auth path) |
| User-terminal note | Historical `git push -u origin main` success in terminal `1.txt`; early pull errors are historical bootstrap — **≠** agent-ready alone |
| Prior publish | Session `1246` complete; pushed `f5012d6`; post-push dirty + SI files remain local |
| Corpus / inventory | **N/A** — no moves this cycle |

## Unknowns

- Exact commit message / contents of remote `489f03a` (not required to abort-on-dirty; re-inspect after a successful clean pull).
- Whether user will later approve stash/commit of post-`1246` dirty files so a follow-up pull cycle can proceed (out of scope unless user asks).
- Whether MSYS↔GfW status skew is purely line-ending/stat — treat as standing risk; always pair status+pull on one binary.

## Risks and blockers

| Item | Severity | Classification | Notes |
| --- | --- | --- | --- |
| Dirty working tree (GfW) | **Blocking for pull** | **process / dirty_working_tree** (not auth) | Q3=A → abort; list paths; session `blocked` |
| Remote ahead (`489f03a`) | Medium | expected after clean | ff-only should advance once clean |
| PATH/MSYS used for pull | High if used | `agent_environment` | Empty helper; bad status semantics |
| Auth / GCM failure | High if appears | `user_credentials` or `agent_environment` | Today GfW fill+fetch dry-run **pass** |
| Wrong git root / sibling `C:\Project` | High if done | process | Hard AC fail |
| Merge/rebase/force/hard-reset to “fix” | High if done | out of scope | Forbidden |
| Missing `gh` | None for Option A | — | Not credential failure while GCM works |
| Taxonomy / must-preserve gates | None for this cycle | out of scope | Do not block pull on these |

### Pull / auth dual preflight (mandatory)

| Field | Value |
| --- | --- |
| Remote URL scheme | **https** |
| Tracking branch | `main` → `origin/main` |
| Agent git (`Get-Command`) | `C:\msys64\usr\bin\git.exe` |
| `where.exe git` | (1) MSYS (2) GfW |
| PATH binary `credential.helper` | **none** |
| Prefer GfW (Windows HTTPS)? | **yes** — `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| GCM / non-interactive evidence | **pass** (GfW fill + `fetch --dry-run`; no secrets logged) |
| `gh` present? | **no** (optional only) |
| User-terminal note | Prior push success; **≠** agent-ready alone |
| Agent **auth** ready (GfW Option A)? | **yes** |
| Agent **pull** ready right now? | **no** — dirty tree (Q3=A) |
| `blocker_type` (auth / GfW path) | **none** |
| `blocker_type` (if PATH/MSYS forced for auth ops) | **agent_environment** |
| Pull execution blocker | **dirty_working_tree** — abort and mark session `blocked`; still self-improve |

**Orchestrator summary:** Auth dual preflight for recommended GfW path is green. Do **not** claim `blockers: none` for the **pull goal** while the tree is dirty. Do **not** claim credentials missing solely because `gh` is absent.

## Canonical references

- Refined prompt: `sessions/2026.09.09-1332/01-prompt-betterment/refined-prompt.md`
- Notes (locks): `sessions/2026.09.09-1332/01-prompt-betterment/notes.md`
- Codebase findings: `sessions/2026.09.09-1332/02-research/codebase-findings.md`
- Online findings: `sessions/2026.09.09-1332/02-research/online-findings.md`
- Prior publish brief: `sessions/2026.09.09-1246/02-research/research-brief.md`
- Law: `AGENTS.md`, `.cursor/skills/full-agent-workflow/SKILL.md`, `references/publish-cycle.md`, `references/handoff-templates.md`
- https://git-scm.com/docs/git-pull
- https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md

## Ready for planner

**Yes — plan Option A**, with `ready_to_implement: yes` for the **documented fail-closed path**:

1. Confirm org root + GfW dual preflight.  
2. Dirty check → **expect abort today** (15 GfW dirty paths); set session `blocked`; do **not** pull.  
3. If somehow clean at implement time: GfW `pull --ff-only`; verify SHAs (local `f5012d6` → remote tip currently `489f03a`).  
4. Never use MSYS as sole status/pull binary; never stash without new user decision.

`mutation_class: docs_only` — no corpus plan-gate for moves. Corpus/inventory: N/A.
