# Session structure

## Root

```
sessions/
  _templates/           # seed files for new sessions
  yyyy.mm.dd/           # one session (or yyyy.mm.dd-HHMM if same-day collision)
    SESSION.md
    01-prompt-betterment/
    02-research/
    03-plan/
    04-implementation/
    05-git/
    06-audit/
    07-self-improvement/
```

Date format is **strict**: `yyyy.mm.dd` (example `2026.09.09`).

**Resume mid-cycle:** If the user points at an existing session that is still `in_progress` (incomplete phases) as prior/resume, continue in that folder — do not invent a sibling `yyyy.mm.dd-HHMM` for the same cycle. New collision folders are for true same-day **new** cycles, not for re-entering an open one.

## Primary artifacts per phase

| Folder | Required files |
| --- | --- |
| `01-prompt-betterment/` | `online-prompt-tips.md`, `refined-prompt.md`, `notes.md` |
| `02-research/` | `codebase-findings.md`, `online-findings.md`, `research-brief.md` (templates: `02-codebase-findings.md`, `02-online-findings.md`, `02-research-brief.md`) |
| `03-plan/` | `plan.md` |
| `04-implementation/` | `log.md`, `changes.md` |
| `05-git/` | `log.md` (health snapshot, commits, push, merges) |
| `06-audit/` | `report.md` |
| `07-self-improvement/` | `audit-realization.md`, `proposals.md`, `changes-applied.md`, `backlog.md` |

Bootstrap may copy **empty** `07-*` templates into the session. That does **not** mean phase 07 ran — keep `SESSION.md` checklist item for self-improver unchecked until `self-improver` overwrites those files with a real audit/proposals/changes/backlog.

### Commit+push sessions

For “one commit then push” goals: stage `log.md`/`changes.md` **before** the publish commit with preflight/stage/secrets filled in. After push, appending hash/push/`git status` will dirty the tree again — that is normal unless a follow-up session-only commit is planned.

### Pull / sync sessions

Use `references/pull-cycle.md`. FAW default = order-aware allowlisted autonomy + `--ff-only` (**behind+allowlisted → stash→ff→pop**; else commit-then-pull). Unrelated dirty-abort → session **`blocked`** with `blocker_type: dirty_working_tree`. Expected **`other`/`non_ff`** → **`blocked`** (WIP/stash kept; never claim pull succeeded). Do not mark `complete` on unmet sync AC. Orchestrator updates SESSION status as soon as implementer returns blocked.

## SESSION.md

Must track: raw goal, refined goal link, status, phase checklist, artifact links, final audit verdict, self-improvement summary.

For **program cycles**, also fill Program framing: roadmap pointer, cycle id, **ROADMAP row locked**, mutation class (`docs_only` | `product_settings` | `catalogue_product` | `fs_mutation` | `escalate_break_loop`), batch approval state, **pending user gates** (taxonomy sign-off / must-preserve review / waivers), prior session / locked answers.
