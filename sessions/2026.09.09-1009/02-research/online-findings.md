# Online findings — Cycle 1

Session: `sessions/2026.09.09-1009/02-research/`  
Focus: locked status axis (`active`/`paused`/`archive` + protect/hygiene), CreationTime vs LastWrite for labels, wrapper-as-canonical-unit, early simple batches before complex git moves, must-preserve / fail-closed habits. Builds on Cycle 0 `sessions/2026.09.09-0929/02-research/online-findings.md` — does not re-litigate hybrid index approach.

## Status axis (not PARA)

- [A Practical Folder Structure for Developers and Solopreneurs](https://thatamazingprogrammer.com/posts/a-practical-folder-structure-for-developers-and-solopreneurs/) — Status-first `active` / `paused` / `archive` (plus inbox/scratch) under `~/Projects`. Matches Cycle 1 lock rejecting PARA-lite for the status axis; supports INDEX specials as separate rows (`protect` / `hygiene`) outside the three lifecycle buckets.
- [The PARA Method – Forte Labs](https://fortelabs.com/blog/para/) — Cited for awareness only: actionability buckets. Cycle 1 explicitly **does not** adopt PARA-lite; keep as contrast reference so implementer does not re-open the decision.
- [Second Brain PARA Structure – AY Automate](https://www.ayautomate.com/resources/breakdowns/second-brain-structure) — Shows how PARA + Archive is used in AI-native vaults; reinforces why this program chose a simpler three-state project lifecycle instead.

## Date source: CreationTime vs LastWrite

- [CASRAI — File naming and folder structure conventions for research data](https://casrai.org/guides/file-naming-and-folder-structure-conventions-for-research-data) — Require the project to **document which date** appears in names (collection/start vs last modification). Supports Cycle 1 lock: state CreationTime as the default for proposed labels; use LastWrite only as activity triage.
- [File Naming Conventions: Best Practices for 2026 – Mapsoft](https://mapsoft.com/posts/file-naming-best-practices.html) — ISO-style date-first naming for chronological sort; status belongs as a separate element/folder, not mashed into the date string — aligns with `yyyy.mm.dd - ShortName` + separate status axis.
- [How can LastWriteTime be earlier than CreationTime? – Stack Overflow](https://stackoverflow.com/questions/10277741/how-can-fileinfo-lastwritetime-be-earlier-than-fileinfo-creationtime) — CreationTime = this filesystem object’s birth on the volume; LastWrite ≈ content modification (and can disagree after copies). Useful caveat for implementer notes: CreationTime-wins is a deliberate local convention, not “true project start” in every edge case; user memory may override later.

## Spaces in ShortName / gradual rename

- Cycle 0 already locked `yyyy.mm.dd - ShortName` with spaces (live example: org folder). Online naming guides often prefer hyphens for cross-tool safety ([Mapsoft](https://mapsoft.com/posts/file-naming-best-practices.html), [renamer.ai naming practices](https://renamer.ai/insights/file-naming-conventions-best-practices)); Cycle 1 **keeps spaces** — document the exception; no silent hyphenation.

## Wrapper vs nested git / atomic moves

- [git-worktree documentation](https://git-scm.com/docs/git-worktree) — Linked worktrees break if main/worktree paths move without `git worktree move` / `repair`. Hard-gate evidence for Obsidian before any relocate. Main worktree cannot use `worktree move`; repair after coordinated move.
- [Migrating Git from multirepo to monorepo – Netlify](https://developers.netlify.com/guides/migrating-git-from-multirepo-to-monorepo-without-losing-history/) — History rewrite ≠ folder relocate. Default remains: move intact `.git` trees. Nested repos inside a dated wrapper stay **child atomic units** (Cycle 1 docs rule).
- Practical takeaway: labeling the **wrapper** as the canonical dated unit matches “top-level move unit” without splitting nested roots — empty-parent cases (`HTTP Battles`) still need classify-before-move notes.

## Navigation / must-preserve / early simple batches

- [Keeping Laravel Projects Findable When Local Work Starts to Sprawl – DEV](https://dev.to/saqueib/keeping-laravel-projects-findable-when-local-work-starts-to-sprawl-55na) — Index + unique names + archive dead work out of active search. Supports deepening INDEX/inventory before physical moves; draft must-preserve before first mutation.
- [Managing Multiple Projects With AI Tools – Vibe Coder Blog](https://blog.vibecoder.me/managing-multiple-projects-ai-tools) — Prefer a small active set and predictable one-project-per-repo layout; starting with **simple / few-git** batches reduces thrash — supports Early/simple as primary next ROADMAP row while complex multi-root waits on git-strategy.
- [Structure First: File Systems and Workspaces – GenAI Skills Academy](https://genaiskills.io/getting-started/structure-first) — Explicit Active vs Archive paths help agents and humans; document placement rules in living docs (here: catalogue + program) before mass moves.

## Takeaways mapped to Cycle 1 deliverables

| Deliverable | Online support |
| --- | --- |
| Status `active`/`paused`/`archive` + INDEX `protect`/`hygiene` | Status-first Projects layout; PARA cited only as rejected alternative |
| CreationTime wins for proposed labels; LastWrite = activity | CASRAI “document which date”; SO Creation vs LastWrite semantics |
| Spaces in ShortName | Program lock overrides common hyphen preference — document exception |
| Wrapper = canonical label; nested git = child atomic | Intact-root moves + worktree hard gate for Obsidian |
| Early/simple next; Git-strategy hard gate reminder | Sprawl/index guidance + worktree docs — simple batches first |
| Must-preserve draft for user review | Fail-closed / index-before-move culture |

## Sources not treated as requirements

Monorepo/`filter-repo` guides remain **awareness only**. Cycle 1 is docs_only — no moves, no git-strategy body of work beyond ROADMAP reminder.
