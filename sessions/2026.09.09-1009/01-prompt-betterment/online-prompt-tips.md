# Online prompt tips

Actionable tips for this Cycle 1 (docs-only) FAW brief — corpus taxonomy / inventory / must-preserve docs.

1. **State outcome + constraint together** — e.g. “ratify taxonomy in `catalogue/` with zero FS mutation under `C:\Project`.” Vague “organise next” invites wrong-phase work.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

2. **Make acceptance criteria binary / checkable** — must-haves, must-nots, quality bar, and “flag if unclear rather than guess.” Prefer “taxonomy status ≠ draft” and “INDEX legend matches ratified axes” over “docs improved.”  
   Source: [How to Make AI Follow Acceptance Criteria](https://newprompt.net/guides/make-ai-follow-acceptance-criteria)

3. **Role → task → constraints** — role = docs foundation for later move batches; task = ratify/deepen/expand listed artefacts; constraints = no moves, no secret reads, inherit Cycle 0 locks. Pair each forbid with a positive alternative (“update INDEX notes” not only “don’t move”).  
   Source: [role-task-constraints pattern](https://github.com/buecking/incontext/blob/main/docs/patterns/role-task-constraints.md)

4. **Plan before multi-file edits; revert+refine if wrong** — Cycle 1 touches several catalogue/program files; require a reviewable plan with paths before implementer writes.  
   Sources: [Cursor agent best practices](https://cursor.com/blog/agent-best-practices) · [Plan Mode](https://cursor.com/docs/agent/plan-mode)

5. **Point at canonical files; don’t paste whole trees** — @/`catalogue/taxonomy.md`, `inventory.md`, `INDEX.md`, `program/ROADMAP.md`, Cycle 0 session. Keeps context tight and conventions durable.  
   Source: [Cursor agent best practices](https://cursor.com/blog/agent-best-practices)

6. **Separate classification schemes from the task** — treat status axis, date-source rules, and wrapper-vs-nested labels as an explicit taxonomy to ratify (not buried prose).  
   Source: [PromptKit taxonomies](https://github.com/microsoft/promptkit) (composable taxonomy layer)

7. **Demand evidence of done** — auditor-verifiable: taxonomy status field, must-preserve draft list path, INDEX/ROADMAP Cycle 1 notes, zero corpus FS mutations. Session report should map to criteria, not “finished.”  
   Source: [Cursor prompts that keep agent sessions focused](https://otf-kit.dev/blog/cursor-prompts-agent-sessions)

# Clarifying questions

Focused on **Cycle 1 — Docs follow-ups** only (do not re-litigate Cycle 0 locks).

1. **Status axis** — Ratify first-cut `active` / `paused` / `archive` (+ existing `protect` / `hygiene` for special rows), or prefer PARA-lite / another set for INDEX Status?
2. **ShortName style** — Keep spaces in `yyyy.mm.dd - ShortName` (match live `Organisation`), or prefer GitHub-style hyphens going forward?
3. **Wrapper vs nested git (docs rule only)** — For thin wrappers with one nested `.git`, should the canonical dated label apply to the **wrapper**, the **nested repo**, or **both same label** (documented as open vs decided for Cycle 1)?
4. **Date-source conflicts** — When CreationTime, earliest commit, and user memory disagree, what is the default winner for proposed labels? (e.g. user > commit > CreationTime)
5. **Inventory deepen — cheap signals** — Approve adding **size bands** (e.g. S/M/L/XL by disk size) and clearer git-root notes / LastWrite-as-activity hints where cheap? Any signal to **skip**?
6. **Must-preserve seed list** — Beyond default-protect org repo, which paths should appear in the Cycle 1 **draft** must-preserve list for your review? (e.g. `Obsidian`, `ProjetOrif`, anything else — or “agent proposes candidates, user ratifies later”)
7. **“Ratify” DoD** — Is Cycle 1 success (a) agent produces a **proposed-ratified** taxonomy marked ready for your sign-off, or (b) taxonomy only marked ratified **after** you explicitly approve in-session / in a follow-up message?
8. **Next row after Cycle 1** — Preferred suggestion to write into ROADMAP/INDEX: **Git-strategy planning** next, or **Early/simple** move-prep docs (still no moves), or leave “user chooses” explicit?

# Answers

1. Status axis: `active` / `paused` / `archive` (+ `protect` / `hygiene`). Not PARA-lite.
2. ShortName: keep spaces.
3. Wrapper vs nested: canonical label on **wrapper**; nested git = child atomic units (proposed-ratified).
4. Date conflicts: **CreationTime wins** (user memory may override later).
5. Inventory: size bands + git-root notes + LastWrite activity where cheap; skip expensive/secret/deep-deps.
6. Must-preserve: agent proposes draft candidates for user review (not auto-locked).
7. Ratify DoD: **proposed-ratified** ready for sign-off — not final without follow-up approval.
8. Next ROADMAP: primary **Early/simple**; Git-strategy hard gate before Obsidian/ProjetOrif/worktrees.
