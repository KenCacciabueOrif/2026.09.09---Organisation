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
    05-audit/
    06-self-improvement/
```

Date format is **strict**: `yyyy.mm.dd` (example `2026.09.09`).

## Primary artifacts per phase

| Folder | Required files |
| --- | --- |
| `01-prompt-betterment/` | `online-prompt-tips.md`, `refined-prompt.md`, `notes.md` |
| `02-research/` | `codebase-findings.md`, `online-findings.md`, `research-brief.md` (templates: `02-codebase-findings.md`, `02-online-findings.md`, `02-research-brief.md`) |
| `03-plan/` | `plan.md` |
| `04-implementation/` | `log.md`, `changes.md` |
| `05-audit/` | `report.md` |
| `06-self-improvement/` | `audit-realization.md`, `proposals.md`, `changes-applied.md`, `backlog.md` |

## SESSION.md

Must track: raw goal, refined goal link, status, phase checklist, artifact links, final audit verdict, self-improvement summary.
