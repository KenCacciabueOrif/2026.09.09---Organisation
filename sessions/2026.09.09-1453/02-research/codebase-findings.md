# Codebase findings — Finish sync / Q3b=B combined-best (`sessions/2026.09.09-1453`)

Live evidence gathered with **Git for Windows** only:  
`C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` (2.54.0.windows.1).

## Prior art (continuity)

| Path | Why it matters |
| --- | --- |
| `sessions/2026.09.09-1435/` | Prior cycle **blocked** on `other`/`merge_conflict` under **Q3b=A**; merge aborted; tip restored to `f3e1119`. |
| `sessions/2026.09.09-1435/04-implementation/log.md` | Confirms merge of `origin/main` hit **exactly 4** allowlist conflict paths; `merge --abort` left recoverable tip. |
| `sessions/2026.09.09-1435/02-research/research-brief.md` | Earlier dual preflight + merge-tree prediction (then HEAD was `7ac4783` → allowlist commit → `f3e1119`). |
| `sessions/2026.09.09-1453/01-prompt-betterment/refined-prompt.md` | This cycle locks **Q2=B**, **Q3b=B**, **R1=combined-best** (judgment-per-hunk). |

## Policy / pack (implementer must follow)

| Path | Why it matters |
| --- | --- |
| `.cursor/skills/full-agent-workflow/references/pull-cycle.md` | Dirty allowlist; Q3b=B allowlist-only resolve; unrelated → `dirty_working_tree`; conflict abort vocabulary `other`/`merge_conflict`; GfW same-binary gate. |
| `.cursor/skills/full-agent-workflow/SKILL.md` | FAW dirty defaults; fail-closed; no false `complete`. |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | **Predicted conflict #3** — pull/publish pack + Choose language. |
| `.cursor/rules/full-agent-workflow.mdc` | **Predicted conflict #2** — push/pull blockers vs remote scaffolding wording. |
| `.cursor/agents/prompt-betterment.md` | **Predicted conflict #1** — Choose / unanswered→default vs Choose-all + ask summary. |
| `sessions/_templates/01-notes.md` | **Predicted conflict #4** — Answers guidance for Choose / unanswered. |
| `AGENTS.md` | Allowlist + fail-closed law (auto-merges cleanly in merge-tree). |

## Live git topology (verified this research turn)

| Fact | Value |
| --- | --- |
| toplevel | `C:/Project/2026.09.09 - Organisation/2026.09.09---Organisation` |
| branch / tracking | `main` ↔ `origin/main` |
| remote | HTTPS `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| HEAD | `f3e1119b7f4dbcf0a62b509a44bdeb1fcc48186e` (`f3e1119`) |
| `origin/main` | `489f03a6ab96523ac4551f12c4fcee31603ca544` (`489f03a`) — fetch + `ls-remote` agree |
| merge-base | `f5012d6f2d15008e4c211a3167a6682f0a1c7b07` (`f5012d6`) |
| ahead / behind | **2 / 1** (diverged) |
| local-only commits | `7ac4783` (allowlist auto-commit enable) → `f3e1119` (1435 session trail) |
| remote-only | `489f03a` (docs_only scaffolding / 1313 session) |
| MERGE_HEAD | **absent** (clean; prior merge aborted) |
| `pull.rebase` | `false` |

**Matches prior tip notes** (`f3e1119` vs `489f03a`).

## Dirty classification (GfW `status --porcelain`)

**Allowlisted: 19** · **Unrelated: 0**

Allowlist paths present:

- `.cursor/agents/{auditor,implementer,orchestrator,prompt-betterment}.md`
- `.cursor/rules/full-agent-workflow.mdc`
- `.cursor/skills/full-agent-workflow/{SKILL.md,references/handoff-templates.md,references/pull-cycle.md}`
- `AGENTS.md`
- `sessions/2026.09.09-1435/**` (impl/audit/self-improve/SESSION)
- `sessions/_templates/03-plan.md`
- `?? sessions/2026.09.09-1453/`

**Dirty overlap with predicted conflicts:**

| Conflict path | WT dirty vs HEAD? |
| --- | --- |
| `.cursor/agents/prompt-betterment.md` | **yes** (` M`) |
| `.cursor/rules/full-agent-workflow.mdc` | **yes** (` M`) |
| `.../handoff-templates.md` | **yes** (` M`) |
| `sessions/_templates/01-notes.md` | clean |

→ Implementer must **allowlist-commit (or path-scoped stash) before merge** so WT intent is not lost and merge is not blocked by dirty overlap. Already diverged → stash→ff-only is **not** the finish path under Q2=B; prefer **allowlist commit → `git merge origin/main`**.

## merge-tree preview (no WT mutation)

Command: `git merge-tree --write-tree --name-only HEAD origin/main` (exit 1).

**Conflicted paths (4 — all ⊆ FAW allowlist):**

1. `.cursor/agents/prompt-betterment.md`
2. `.cursor/rules/full-agent-workflow.mdc`
3. `.cursor/skills/full-agent-workflow/references/handoff-templates.md`
4. `sessions/_templates/01-notes.md`

**Clean auto-merges noted in messages:** `orchestrator.md`, `SKILL.md`, `AGENTS.md` (still review after real merge).

### Conflict hunk map + combined-best planner hints

(From merge-tree tree blob with conflict markers; **committed HEAD**, not dirty WT.)

| File | Hunks | Likely combined-best direction |
| --- | --- | --- |
| `prompt-betterment.md` | 1 | **Combine both:** keep HEAD’s *unanswered→default* / disclosed-default lock; fold in origin’s *Choose all* + durable one-line ask summary per Q. Do not drop pull/publish pack bullets if they survive only on HEAD outside this hunk — verify full file. |
| `full-agent-workflow.mdc` | 1 | **Prefer HEAD core** for pull/dirty/`dirty_working_tree`/Q3c/SESSION flip/`non_ff`; **fold origin** `docs_only` scaffolding clarity (“incl. org-repo folder/README…”) into §7. Do not regress to origin’s thinner push-only §6. |
| `handoff-templates.md` | 2 | Hunk1: keep HEAD publish/pull pack lines **and** origin Choose-all + ask-summary. Hunk2: keep HEAD pull/Q3c/focus list **and** fold origin docs_only / Choose-all focus items. Re-check auto-merged middle sections so pull dual-preflight bullets are not silently dropped. |
| `sessions/_templates/01-notes.md` | 1 | **Combine:** HEAD unanswered→default Source language **+** origin Choose-all + one-line ask-summary guidance (origin also adds ask-summary under clarifying questions — keep if auto-merged). |

**Blind `--ours` / `--theirs` would lose the other side’s unique FAW improvements — forbidden under R1.**

## Agent environment (codebase-adjacent)

| Item | Evidence |
| --- | --- |
| PATH `git` | `C:\msys64\usr\bin\git.exe` first — **no** `credential.helper` |
| Prefer GfW | `C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe` — helper `manager` (system gitconfig) |
| `gh` | not installed (optional only) |

## Must-read for planner / implementer

- `sessions/2026.09.09-1453/01-prompt-betterment/refined-prompt.md`
- `sessions/2026.09.09-1453/01-prompt-betterment/notes.md`
- `.cursor/skills/full-agent-workflow/references/pull-cycle.md` (Q3b=B + allowlist)
- `sessions/2026.09.09-1435/04-implementation/log.md` (exact prior conflict list + abort)
- The four conflict files above (study both sides per hunk at resolve time)
