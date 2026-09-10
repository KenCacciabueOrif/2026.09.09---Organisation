# Codebase findings — Pull-autonomy (`sessions/2026.09.09-1350`)

Evidence gathered 2026-09-09 for allowlisted auto-commit + same-session agent pull. Paths relative to org-repo root unless noted.

## Prior blocked pull (must-read context)

| Path | Why it matters |
| --- | --- |
| `sessions/2026.09.09-1332/SESSION.md` | Session **`blocked`**, `blocker_type: dirty_working_tree`; Q3=A abort; HEAD stayed `f5012d6`; auth was green |
| `sessions/2026.09.09-1332/04-implementation/log.md` | 15 GfW porcelain paths; pull not attempted; lists exact dirty set that became today’s allowlist seed |
| `sessions/2026.09.09-1332/02-research/research-brief.md` | Dual-preflight template; GfW vs MSYS skew (15 vs 104); remote tip already noted as `489f03a` |
| `sessions/2026.09.09-1332/06-self-improvement/changes-applied.md` | Introduced `pull-cycle.md` + wired `dirty_working_tree` into agents/skill — **abort-default** that this cycle supersedes |
| `sessions/2026.09.09-1332/06-self-improvement/backlog.md` | P6 “dirty-tree cleanup helper” deferred; this cycle answers that need via allowlist policy |

## Primary docs to change (AC A)

| Path | Current state | Needed change |
| --- | --- | --- |
| `.cursor/skills/full-agent-workflow/references/pull-cycle.md` | Q3 default **A = abort**; `blocker_type dirty_working_tree` when any porcelain; remediation = user clean | Q3 → allowlisted auto-commit then pull; abort **only** unrelated dirty; document allowlist; update defaults / blocker text |
| `.cursor/skills/full-agent-workflow/references/publish-cycle.md` | No dirty autonomy Q; publish pack silent on session/FAW-meta WIP | Mirror same allowlist autonomy for push/publish dirty (Q9); unrelated still aborts |
| `.cursor/skills/full-agent-workflow/SKILL.md` | “dirty-abort default”; pull-cycle link; `rework_owner: user` for dirty cleanup | Align wording with allowlist-first FAW default; keep fail-closed / GfW same-binary |
| `.cursor/rules/full-agent-workflow.mdc` | “correct dirty-abort pull = process pass + blocked” | Retain fail-closed; distinguish allowlist commit path vs unrelated abort |
| `AGENTS.md` | “Pull dirty-abort (default) → session blocked” | Update default language to allowlist auto-commit then ff-only |

## Agents / handoffs still saying “any dirty → abort / user cleanup”

| Path | Why it matters |
| --- | --- |
| `.cursor/agents/prompt-betterment.md` | Pull pack described as dirty-abort default |
| `.cursor/agents/researcher.md` | “if dirty under abort policy → dirty_working_tree”; must mention classify allowlist vs unrelated |
| `.cursor/agents/planner.md` | (via handoff) pull dirty-abort expected path |
| `.cursor/agents/implementer.md` | Dirty abort → blocked; remediation “user clean/stash/commit”; needs allowlist auto-commit path |
| `.cursor/agents/auditor.md` | Checklist: any porcelain → pull not attempted; `rework_owner: user` for dirty cleanup — wrong when dirt ⊆ allowlist |
| `.cursor/agents/orchestrator.md` | Dirty remediation = user clean then new cycle — wrong for allowlisted FAW dirt |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | “default dirty = abort” in prompt/research/plan/implement/audit snippets |
| `.cursor/skills/full-agent-workflow/references/session-structure.md` | Pull: dirty-abort → blocked |

## Locked allowlist (encode in refs; match refined prompt)

Auto-commit **only**:

- `sessions/**`
- `.cursor/skills/full-agent-workflow/**`
- `.cursor/agents/**`
- `.cursor/rules/**`
- `AGENTS.md`
- `sessions/_templates/**` (subset of `sessions/**`; list explicitly in docs)

Outside → abort, list paths, `blocker_type: dirty_working_tree`.

## Live porcelain classification (GfW, this research turn)

Binary: `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe`  
Command: `git status --porcelain`

| Class | Count | Notes |
| --- | --- | --- |
| **Allowlisted** | **23** | All current dirty/untracked paths |
| **Unrelated** | **0** | No `catalogue/**`, `program/**`, or other non-allowlist dirt |

Allowlisted paths observed:

- Modified agents: `auditor`, `implementer`, `orchestrator`, `prompt-betterment`, `researcher` (+ prior SI edits)
- Modified: `.cursor/rules/full-agent-workflow.mdc`, `SKILL.md`, `handoff-templates.md`, `session-structure.md`, `AGENTS.md`
- Modified: `sessions/2026.09.09-1246/**` (7 files), `sessions/_templates/{01-notes.md,SESSION.md}`
- Untracked: `publish-cycle.md`, `pull-cycle.md`, `sessions/2026.09.09-1332/`, `sessions/2026.09.09-1350/`

MSYS `git status --porcelain` count: **112** (skew — do **not** use for gate). Same finding as 1332.

## Remote / history facts (org-repo only)

| Fact | Value |
| --- | --- |
| Git root | `C:/Project/2026.09.09 - Organisation/2026.09.09---Organisation` |
| Remote | `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| Branch | `main` ↔ `origin/main` |
| Local HEAD | `f5012d6` — *Publish organisation catch-up…* |
| Remote tip (`ls-remote` / post-fetch `origin/main`) | **`489f03a`** — *Clarify docs_only… + session 1313* |
| Ahead/behind after agent `fetch` | **0 ahead / 1 behind** (then allowlist commit would make **diverged**) |

### Overlap: dirty vs incoming remote (`HEAD..origin/main`)

Seven dirty paths overlap remote file changes — pull **while dirty** would hit “local changes would be overwritten”:

1. `.cursor/agents/orchestrator.md`
2. `.cursor/agents/prompt-betterment.md`
3. `.cursor/rules/full-agent-workflow.mdc`
4. `.cursor/skills/full-agent-workflow/SKILL.md`
5. `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
6. `AGENTS.md`
7. `sessions/_templates/01-notes.md`

Incoming also adds `sessions/2026.09.09-1313/**`, `Notes/README.md`, planner agent edits, etc. (no conflict with untracked `1332`/`1350` dirs by name).

## Standing constraints already encoded (preserve)

- Org-repo root only; never sibling `C:\Project` trees (`publish-cycle.md`, `AGENTS.md`, skill)
- Dual preflight; GfW absolute path when PATH is MSYS without helper
- Same binary for porcelain + pull/push
- No force push / hard reset / `--no-verify`; self-improver still on block
- BOM-safe commit messages on Windows PowerShell (`AGENTS.md`)

## Mutation class

`docs_only` + org-repo git ops — **no** catalogue/program corpus moves; taxonomy/must-preserve **out of scope** (do not gate).

## Implications for planner

1. Doc edits land in allowlisted paths — they fold into the same allowlist commit as other FAW dirt.
2. Under **new** policy, current tree is **not** a `dirty_working_tree` abort (unrelated = 0).
3. Naive “commit allowlist → `pull --ff-only`” after remote `489f03a` will **diverge** (local tip + remote tip both children of `f5012d6`) → ff-only fails → Q3b/Q6 fail-closed (valid AC path if typed correctly).
4. Pull-while-dirty without commit is also blocked by the 7-file overlap — commit-first remains correct under locked Q3.
