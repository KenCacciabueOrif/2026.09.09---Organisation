# Codebase findings — Pull cycle (`sessions/2026.09.09-1332`)

Evidence gathered 2026-09-09 for agent-executed `git pull --ff-only` of `origin` → `main` / `origin/main` in the org-repo git root only.

## Live git state (org root)

| Fact | Value |
| --- | --- |
| `rev-parse --show-toplevel` (GfW) | `C:/Project/2026.09.09 - Organisation/2026.09.09---Organisation` |
| Branch / upstream | `main` → `origin/main` |
| Local HEAD | `f5012d6` — *Publish organisation catch-up so origin/main matches local FAW work.* |
| Local `origin/main` cache | `f5012d6` (not refreshed by dry-run) |
| Ahead/behind vs local `origin/main` | **0 / 0** (stale until real fetch) |
| Remote tip (`ls-remote` / `fetch --dry-run`) | **`489f03a`** — dry-run reported `f5012d6..489f03a  main -> origin/main` |
| Remote URL | HTTPS `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git` |
| Dirty? (GfW porcelain — **authoritative for Option A**) | **Yes — 15 lines** (13 modified + 2 untracked) |

### Dirty paths (GfW `status --porcelain`)

```
 M .cursor/agents/prompt-betterment.md
 M .cursor/rules/full-agent-workflow.mdc
 M .cursor/skills/full-agent-workflow/SKILL.md
 M .cursor/skills/full-agent-workflow/references/handoff-templates.md
 M AGENTS.md
 M sessions/2026.09.09-1246/04-implementation/log.md
 M sessions/2026.09.09-1246/05-audit/report.md
 M sessions/2026.09.09-1246/06-self-improvement/audit-realization.md
 M sessions/2026.09.09-1246/06-self-improvement/backlog.md
 M sessions/2026.09.09-1246/06-self-improvement/changes-applied.md
 M sessions/2026.09.09-1246/06-self-improvement/proposals.md
 M sessions/2026.09.09-1246/SESSION.md
 M sessions/_templates/01-notes.md
?? .cursor/skills/full-agent-workflow/references/publish-cycle.md
?? sessions/2026.09.09-1332/
```

Interpretation: expected **post-publish finalize dirtiness** from session `1246` (Q7=A) plus self-improvement edits (`publish-cycle.md`, law/skill updates) that were **not** in pushed commit `f5012d6`, plus the **current** session folder `1332`. Per locked Q3=A, any non-empty porcelain → **abort pull** (no stash).

### PATH/MSYS vs GfW status discrepancy (important)

| Binary | Porcelain count |
| --- | --- |
| GfW `...\Git\cmd\git.exe` | **15** |
| PATH/MSYS `C:\msys64\usr\bin\git.exe` | **104** |

MSYS lists many additional “modified” paths under `catalogue/`, `program/`, and prior `sessions/2026.09.09-*` that GfW does **not**. Same toplevel. Treat **GfW status as canonical** when pull uses GfW; do not let MSYS false-dirty inflate the abort list, and do not use MSYS alone to claim “clean”. Prefer one binary for both preflight status and pull.

## Prior publish session context (`sessions/2026.09.09-1246`)

| Item | Path / value | Why it matters |
| --- | --- | --- |
| Session status | `complete`; audit pass | Last successful agent publish |
| Pushed commit | `f5012d6` on `origin/main` (at close of 1246) | Local HEAD still here; **remote has since moved** to `489f03a` |
| Research dual preflight | `02-research/research-brief.md` | Proven GfW+GCM pattern to reuse |
| Implementation log | `04-implementation/log.md` | Documents GfW path, MSYS helper empty, push via absolute GfW |
| Self-improvement | `06-self-improvement/changes-applied.md` | Added `publish-cycle.md` + skill/agent pointers — files now dirty/untracked locally |

## Workflow / law prior art (pull adapts push dual-preflight)

| Path | Why it matters |
| --- | --- |
| `AGENTS.md` | Dual preflight, GfW over MSYS, fail-closed, org-root only |
| `.cursor/rules/full-agent-workflow.mdc` | Same law for orchestrated cycles |
| `.cursor/skills/full-agent-workflow/SKILL.md` | Dual preflight + blocker_type typing |
| `.cursor/skills/full-agent-workflow/references/publish-cycle.md` | Publish Q pack; git-root boundary; **no pull-cycle pack yet** (notes backlog) |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | Researcher dual-preflight checklist (worded for push; apply same for pull) |
| `sessions/2026.09.09-1332/01-prompt-betterment/refined-prompt.md` | AC: ff-only, dirty-abort, agent Shell success, fail-closed |
| `sessions/2026.09.09-1332/01-prompt-betterment/notes.md` | Locked Choose→all A |

## Out of scope (do not treat as pull blockers)

- Taxonomy **proposed-ratified — ready for user sign-off**
- Must-preserve **draft** review
- Corpus FS moves / inventory batching (`docs_only` git ops)

## Multi-root workspace risk

Workspace includes sibling `C:\Project`. Hard AC: every git command’s `rev-parse --show-toplevel` must equal the org-repo path before fetch/pull. Never operate on sibling trees.
