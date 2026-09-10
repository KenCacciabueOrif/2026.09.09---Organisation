# Prompt betterment notes

Session: `sessions/2026.09.09-0929/01-prompt-betterment/`  
Role of this session: **Cycle 0 / Program charter** (not bulk reorganisation of `C:\Project`).

## Clarifying questions

Answered — do not re-ask.

## Answers

1. **End-state:** Clear dated view of everything that happened and what would be next; easy navigation. Best organisation method is part of the task. Must NOT change project functionalities or lose information.
2. **Later cycles:** (c) agent-executed moves after explicit per-batch approval.
3. **Taxonomy / naming:** `yyyy.mm.dd` + project/folder/file name (same date format as sessions).
4. **Exclusions:** Do not detail dependency/cache trees in inventory; any later move must still include them so functionality is preserved. Criterion: whether it affects functionality.
5. **Secrets:** Do not read/open `.env` and similar; may move them with their projects.
6. **Cycle 0 DoD:** Charter + coarse inventory + taxonomy + multi-cycle roadmap; zero moves under `C:\Project`. Confirmed.
7. **Later cycles:** Slice by **top-level folder**; number of rounds adaptive (determined as we go).
8. **Artefact home:** Organised material under `C:\Project`; maintain whole-corpus **index and documentation** in this organisation repo.
9. **Must-preserve:** TBD — document as open decision; default-protect this organisation repo path until decided.
10. **Git:** Multiple repos under `C:\Project`; strategy needs dedicated planning. Each git folder = its own project; treat git roots as **atomic units** (do not split without a plan).

## Assumptions

- This session = **Cycle 0** only: charter, coarse inventory (incl. git-root candidates), taxonomy (`yyyy.mm.dd` + name), organisation-approach recommendation, adaptive roadmap — docs/index in organisation repo.
- Physical reorganisation of projects happens in **later** cycles under `C:\Project`, after per-batch approval.
- Dependency/cache dirs are **payload**, not inventory subjects; secrets are **opaque payload**.
- Git complexity is deferred to a planned thread, but inventory must **detect** `.git` roots now.
- Cycle 0 publish/push of organisation artefacts is **not** required unless the user later asks.
- Full must-preserve list remains open; organisation repo is protected by default.

## Open risks

- Must-preserve list incomplete → accidental move of a critical path in a later cycle.
- Multi-repo git (remotes, nested repos, worktrees, LFS) may block or complicate approved moves if the git-strategy cycle is skipped.
- Adaptive roadmap may under-specify sequencing; each new cycle still needs a tight FAW prompt.
- Coarse inventory may miss nested git roots if scanning is too shallow — researcher should note depth limits.
- Moving projects with huge `node_modules` is slow/fragile even when functionally correct; later cycles need batch sizing.
- Quoting secrets into session logs if agents sample wrong files — keep read bans strict.
- “Dated view + next + navigation” has multiple valid designs; Cycle 0 recommendation must present options and a preferred cut without over-committing before user review.

## Key alignment changes (raw → refined)

- End-state locked: dated history + next + navigation; no functionality/info loss.
- Later work = **approved agent moves**, not catalog-only.
- Naming locked to **`yyyy.mm.dd` + name**.
- Inventory skips dep/cache detail; moves keep deps + opaque secrets with projects.
- Artefacts: **index/docs in organisation repo**; material stays under `C:\Project`.
- Cycles by **top-level folder**, adaptive count.
- Git roots = atomic projects; dedicated git-strategy planning before git-root moves.
- Cycle 0 adds **organisation-approach recommendation** and **git-root inventory flags**; still zero moves.
