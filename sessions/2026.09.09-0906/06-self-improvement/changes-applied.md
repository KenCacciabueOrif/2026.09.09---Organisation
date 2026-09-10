# Changes applied

## Applied

- `.cursor/agents/implementer.md` — added **Session docs vs single-commit push**: finalize pre-push log before commit; after push leave dirty or optional tiny session-only follow-up commit.
- `.cursor/agents/auditor.md` — expected post-push session dirtiness = **Low**, not Medium/rework, when live push verified and pre-push log was committed.
- `.cursor/skills/full-agent-workflow/SKILL.md` — one bullet encoding the single-commit vs session-finalize tradeoff.
- `.cursor/skills/full-agent-workflow/references/session-structure.md` — **Commit+push sessions** note under primary artifacts.
- `sessions/_templates/03-plan.md` — risk row for single-commit vs post-push log.
- `sessions/_templates/05-report.md` — checklist item for Low/expected dirty finalize.
- `AGENTS.md` — portable one-liner on post-push notes tradeoff.

## Why

Cycle `pass_with_issues` Medium finding was the chicken-egg of “exactly one commit” + post-push `log.md`/`changes.md`/`SESSION.md`. Encoding the tradeoff prevents false Medium/rework next publish cycle without forcing a second commit.

## No safe improvement

N/A — improvements applied.
