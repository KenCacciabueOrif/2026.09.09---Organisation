# Codebase findings — Pull-merge (`sessions/2026.09.09-1435`)

## Goal alignment

Finish sync after `2026.09.09-1350` (`blocked` / `other`/`non_ff`): agent **GfW** merge of `origin/main` into `main` under locked **Q2=B**. Dirty ⊆ FAW allowlist → order-aware autonomy then merge; unrelated → abort; conflict → fail-closed (Q3b=A).

## Canonical policy / pack (must-read)

| Path | Why it matters |
| --- | --- |
| `.cursor/skills/full-agent-workflow/references/pull-cycle.md` | Dirty allowlist; already-diverged → no silent merge under Q2=A; finish via new cycle Q2=B/C; GfW same-binary gate; blockers |
| `.cursor/skills/full-agent-workflow/SKILL.md` | Dual preflight; behind+allowlisted stash→ff→pop; diverge → `other`/`non_ff`; fail-closed |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | Researcher pull preflight fields (auth vs dirty vs ahead/behind) |
| `.cursor/skills/full-agent-workflow/references/session-structure.md` | Pull cycle session status rules |
| `.cursor/rules/full-agent-workflow.mdc` | Workspace law mirroring FAW pull/publish |
| `AGENTS.md` | Portable law: GfW, allowlist, stash→ff when behind, merge only when Q2≠A |
| `sessions/2026.09.09-1435/01-prompt-betterment/refined-prompt.md` | Locked AC for this cycle |
| `sessions/2026.09.09-1435/01-prompt-betterment/notes.md` | Choose locks: Q1A, **Q2B**, Q3/Q3c merge-path, Q3bA, Q4–Q7 A |

## Prior session continuity

| Path | Why it matters |
| --- | --- |
| `sessions/2026.09.09-1350/SESSION.md` | Status `blocked`; blocker `other`/`non_ff`; HEAD `7ac4783` vs `origin/main` `489f03a` (1/1) |
| `sessions/2026.09.09-1350/04-implementation/log.md` | Allowlist commit then `--ff-only` exit 128; WIP tip kept |
| `sessions/2026.09.09-1350/06-self-improvement/backlog.md` | **B1** finish sync via new cycle Q2=B merge (this session) |
| `sessions/2026.09.09-1350/02-research/research-brief.md` | Prior dual preflight pattern; GfW path; predicted diverge |

## Live dual preflight (this research pass)

**Org root (GfW):** `C:/Project/2026.09.09 - Organisation/2026.09.09---Organisation`  
**Do not** gate or merge sibling trees under multi-root `C:\Project`.

### Remote / tracking

| Field | Value |
| --- | --- |
| `origin` fetch/push | `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| Scheme | **https** |
| Branch | `main` tracks `origin/main` |
| `ls-remote origin refs/heads/main` | `489f03a6ab96523ac4551f12c4fcee31603ca544` |
| Fetch | **pass** (exit 0) |

### Diverge state (post-fetch, confirmed)

| Tip | Full SHA | Subject (short) |
| --- | --- | --- |
| Local `HEAD` | `7ac47835abd7ccb56195bae0daf364baef3e2580` | Enable allowlisted FAW auto-commit… |
| `origin/main` | `489f03a6ab96523ac4551f12c4fcee31603ca544` | Clarify docs_only org-repo scaffolding… (1313 session) |
| Merge-base | `f5012d6f2d15008e4c211a3167a6682f0a1c7b07` | Publish organisation catch-up… |

- Ahead/behind `HEAD...origin/main`: **1 / 1** (unchanged after fetch)
- Neither tip is ancestor of the other (`merge-base --is-ancestor` both exit 1)
- Matches 1350 diverge SHAs (still current)

### Agent git / GCM

| Field | Value |
| --- | --- |
| PATH `Get-Command git` | `C:\msys64\usr\bin\git.exe` (**MSYS**) |
| `where.exe git` | (1) MSYS (2) `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` |
| Prefer GfW | **yes** — absolute `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (2.54.0.windows.1) |
| Note | `C:\Program Files\Git\cmd\git.exe` **absent** on this machine |
| GfW `credential.helper` | `manager` (system; local get also `manager`) |
| MSYS `credential.helper` | **empty** |
| GfW `credential fill` (protocol=https host=github.com) | exit **0**; `has_username=True` `has_password=True` — **values not logged** |
| `gh` | **absent** (optional only; not sole credential signal) |
| `GITHUB_TOKEN` present | **True** (boolean only) |
| `pull.rebase` | `false` (merge-friendly for `git pull`) |
| `pull.ff` / `merge.ff` | unset |
| Stash list | empty |

### Porcelain classification (**GfW only** — authoritative gate)

Dirty ⊆ allowlist (**unrelated = 0**):

| Class | Paths |
| --- | --- |
| Allowlist modified | `.cursor/agents/{auditor,implementer,orchestrator,prompt-betterment,researcher}.md`; `.cursor/rules/full-agent-workflow.mdc`; `.cursor/skills/full-agent-workflow/{SKILL.md,references/handoff-templates.md,pull-cycle.md,session-structure.md}`; `AGENTS.md`; `sessions/2026.09.09-1350/{04-implementation/log.md,05-audit/report.md,06-self-improvement/*,SESSION.md}`; `sessions/_templates/SESSION.md` |
| Allowlist untracked | `sessions/2026.09.09-1435/` |
| **Unrelated** | **none** |

**MSYS porcelain skew:** MSYS lists **many** additional `M` paths under `catalogue/**`, `program/**`, and older `sessions/**` that GfW does **not**. Using MSYS for the dirty gate would falsely trigger `dirty_working_tree` → classify as **`agent_environment`** if that binary is used for gate/merge.

### Predicted merge conflicts (`git merge-tree HEAD origin/main`)

Exit **1** — content conflicts (committed tips only; dirty WT not applied):

1. `.cursor/agents/prompt-betterment.md`
2. `.cursor/rules/full-agent-workflow.mdc`
3. `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
4. `sessions/_templates/01-notes.md`

Several of these paths are also **currently dirty** under GfW → implementer **must** allowlist-commit or path-stash **before** merge so the index is clean enough to start merge; otherwise merge may refuse or compound conflicts.

### Overlap note (local tip vs remote tip file sets)

- Local-only arm (`f5012d6..HEAD`): FAW allowlist docs + sessions `1332`/`1350`/`1246` finalize + templates.
- Remote-only arm (`f5012d6..origin/main`): FAW docs edits + session `1313` + `Notes/README.md` + template tweaks.
- Shared edited paths across arms include orchestrator/prompt-betterment/rule/SKILL/handoffs/`AGENTS.md`/templates — explains conflict set.

## Allowlist (locked)

`sessions/**`, `.cursor/skills/full-agent-workflow/**`, `.cursor/agents/**`, `.cursor/rules/**`, `AGENTS.md`, `sessions/_templates/**`.

## Implications for implementer

1. Same GfW binary for porcelain, allowlist commit/stash, fetch, and merge.
2. Dirty ⊆ allowlist → commit (preferred checkpoint while already diverged) **or** path-scoped stash, then merge.
3. `git merge origin/main` or `git pull` with `--no-rebase` / existing `pull.rebase=false` — **not** `--ff-only`.
4. Expect conflicts on the four paths above → Q3b=A fail-closed; keep commit/stash recoverable; no force / hard reset / `--no-verify` / `stash drop`. Prefer `git merge --abort` if merge started and sync must stop cleanly.
5. Never mark `complete` unless HEAD incorporates `origin/main` via successful merge.
