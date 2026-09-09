# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | pull-cycle pack / skill | Allowlist **commit-first** while **behind** remote → diverge → `--ff-only` fails; sync still unmet | Add **Q3c** (behind + allowlisted dirty): disclosed default **A = stash allowlist → `pull --ff-only` → stash pop** (then optional allowlist commit). Keep commit-first only when **not** behind. Document diverge risk of commit-first. | `references/pull-cycle.md`, `SKILL.md`, rule, `AGENTS.md` |
| P2 | implementer / researcher | Agents always “auto-commit then ff-only” with no behind check | Instruct: fetch/count ahead-behind **before** dirty handler; if behind>0 and dirt ⊆ allowlist → Q3c stash path (unless user locked commit-first); never claim pull success on non-ff | `implementer.md`, `researcher.md`, handoffs |
| P3 | blocker_type docs | `other`/`non_ff` remediation is vague for next cycle | Spell: `other`/`non_ff` = process pass + session **blocked**; WIP kept; **do not** silent merge under Q2=A; next cycle Choose Q2 B/C **or** recover via soft reset + Q3c path if commit was allowlist-only | pull-cycle, orchestrator, auditor, implementer, SESSION template |
| P4 | prompt-betterment | Next pull Choose may re-pick commit-first and re-deadlock | Surface Q3c + plain-language “already behind?” in pull pack asks; unanswered→Choose default A when behind | `prompt-betterment.md`, `pull-cycle.md` |
| P5 | This blocked session | Invent merge/rebase now to “finish sync” | **Defer** — fail-closed under Q2=A; docs only this self-improve; sync finish = **new** cycle | backlog only |
| P6 | publish-cycle | Publish less affected by behind+dirty | Light cross-ref only; do not change publish default this turn | optional / defer |

## Online best-practice notes

Adopted / reinforced (with URLs):

1. **`--ff-only` refuses diverge by design** — after a local tip that is not an ancestor of remote, pull must abort unless merge/rebase is chosen. Do not treat that abort as a bug when Q2=A. Source: [git-pull(1)](https://git.github.io/htmldocs/git-pull.html) (`--ff-only`).
2. **Dirty tree + pull: stash/autostash is the common safe pattern** when you need remote tip first without creating a divergent local commit. Git documents `--autostash` / `pull.autostash`; defensive scripts use stash → pull → pop and **never auto `stash drop` on conflict**. Sources: [git-pull `--autostash`](https://git.github.io/htmldocs/git-pull.html); [Defensive git pull — stash, pull, pop](https://wiki.r-that.com/snippets/git-pull-defensive-with-stash/); config note [pull.autoStash](https://code.googlesource.com/git/+/0fae78c9d55efe705877ea537fe42c59164ccd94/Documentation/config/pull.adoc).
3. **FAW preference remains durable allowlist commit when not behind**; when **behind**, stash-first avoids the commit-created diverge. Autostash is convenient but FAW still prefers **explicit** stash (path-scoped, recoverable, no silent drop) over opaque config-only behavior for agents.
4. **Cursor skills / subagents:** keep procedural detail in `references/`; concise agent files; progressive disclosure. Sources: [Cursor Skills](https://cursor.com/docs/skills); [Cursor Subagents](https://cursor.com/docs/subagents.md).

**Not adopted this turn:** flipping Q2 default to merge (too sharp a history change without user Choose); inventing merge in this blocked session; enabling global `pull.autostash` via git config (agents must not rewrite user git config).
