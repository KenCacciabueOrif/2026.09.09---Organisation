# Refined prompt

## Goal

Run **Cycle 1 — Docs follow-ups** of the multi-cycle FAW program that organises `C:\Project`.

**Locked program end-state (do not re-open):** dated view + what’s next + easy navigation; no functionality loss / no information loss; later physical moves only after per-batch approval; git roots atomic; index/docs in this organisation repo; material under `C:\Project`.

**This cycle delivers only (docs_only):**

1. **Propose-ratify taxonomy** in `catalogue/taxonomy.md` (sync INDEX legend) with these **locked Cycle 1 decisions**:
   - **Status axis:** `active` / `paused` / `archive`, plus INDEX specials `protect` / `hygiene`. **Not** PARA-lite.
   - **ShortName:** keep spaces — canonical form `yyyy.mm.dd - ShortName`.
   - **Wrapper vs nested git (docs rule):** when the top-level folder is a thin wrapper around nested `.git` tree(s), the **canonical dated label applies to the wrapper** (the top-level move unit). Nested git roots are documented as **child atomic units** inside that wrapper (still never split without an explicit later plan). Empty-parent / multi-root edge cases may stay in a short “still open / classify before move” note, but the default rule above is **proposed-ratified**.
   - **Date-source default for proposed labels:** **CreationTime wins** over earliest commit and LastWrite. User memory may override later if explicitly stated.
   - Mark taxonomy **proposed-ratified — ready for user sign-off**. Do **not** claim final user ratification without a later explicit approval.
2. **Deepen inventory** (`catalogue/inventory.md` + INDEX columns/notes as needed):
   - Include **size bands** (e.g. S/M/L/XL) where cheap.
   - Clearer **git-root notes** (depth-bounded; record scan limits).
   - **LastWrite as activity / “next” hints** where cheap.
   - Skip expensive/risky work: **no secret reads**, no deep `node_modules` / cache documentation.
3. **Expand must-preserve draft list** beyond default-protect org repo: agent **proposes candidates** for user review; list labelled **draft — not auto-locked**.
4. **Update** `catalogue/INDEX.md` and `program/ROADMAP.md` for Cycle 1 completion and a **concrete next-row suggestion**:
   - **Primary next suggestion:** **Early/simple** (move-prep / first simple batch after per-batch approval) — low-risk top-levels can advance while taxonomy is only proposed-ratified.
   - **Hard gate reminder (not the primary next row):** dedicated **Git-strategy** FAW remains mandatory **before** Obsidian / ProjetOrif multi-root / worktree moves.
5. Prove **docs_only**: zero intentional moves/renames/deletes under `C:\Project`.

## Constraints

- Host workflow repo: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`
- Corpus root: `C:\Project` — **read/scan for docs only**; no FS mutation
- Mutation class: **docs_only** (orchestrator-locked)
- Session: `sessions/2026.09.09-1009/` — phase artefacts under `01-prompt-betterment/` … through self-improver
- Inherit Cycle 0 locks: `yyyy.mm.dd - name`; moves only after per-batch approval; git roots atomic; deps not detailed in inventory but included in future moves; `.env` not read but movable; adaptive cycles by top-level folder
- Prefer small, reviewable diffs in the organisation repo; no secrets in commits or session logs
- Do **not** execute git-strategy planning as this cycle’s body of work (pointer/reminder in ROADMAP only)
- Do **not** execute any move batch in this cycle
- Do **not** require `git push` / remote publish unless the user separately asks (Cycle 1 is local docs)

## Context pointers (known paths)

- Program: `program/CHARTER.md`, `program/ROADMAP.md`, `program/organisation-approach.md`
- Catalogue: `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/taxonomy.md`
- Prior cycle: `sessions/2026.09.09-0929/` (esp. `01-prompt-betterment/notes.md`, audit/implementation)
- This cycle prompt pack: `sessions/2026.09.09-1009/01-prompt-betterment/`
- Workflow law: `AGENTS.md`, `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/agents/orchestrator.md`
- Corpus (do not relocate): `C:\Project`

## Acceptance criteria / verification

- [ ] `catalogue/taxonomy.md` is marked **proposed-ratified — ready for user sign-off** (not “final ratified” without follow-up approval).
- [ ] Taxonomy locks: status axis `active`/`paused`/`archive` (+ `protect`/`hygiene`); ShortName with spaces; date default **CreationTime wins**; wrapper = canonical label / nested git = child atomic units (documented).
- [ ] INDEX legend (and rows as needed) uses the same status vocabulary; proposed date labels remain **proposals**, not applied renames.
- [ ] Inventory deepened vs Cycle 0 with: size bands where cheap, clearer git-root notes, LastWrite-as-activity hints; expensive/secret/deep-dep scans skipped (noted if deferred).
- [ ] Must-preserve **draft** candidate list exists beyond org-repo default-protect; explicitly **for user review / not auto-locked**; no secret contents.
- [ ] `catalogue/INDEX.md` “What’s next” and `program/ROADMAP.md` reflect Cycle 1 complete and suggest **Early/simple** as the primary next row, with **Git-strategy** noted as hard gate before Obsidian/ProjetOrif/worktrees.
- [ ] Auditor verifies: **zero** intentional moves/renames/deletes under `C:\Project` attributable to this cycle.
- [ ] No `.env` / credential contents opened or quoted in session logs or commits.

## Out of scope

- Any FS mutation under `C:\Project` (moves, renames, deletes, mkdir reorg)
- Executing **git-strategy** as a dedicated cycle’s deliverables (beyond ROADMAP hard-gate reminder)
- Any move batch (including Early/simple), even with “tiny” scope
- Deep inventory of `node_modules` / build caches
- Opening or quoting secrets
- Claiming **final** user ratification of taxonomy without explicit follow-up approval
- Re-litigating Cycle 0 locked decisions (dated view + next + navigation; naming form; approval gate; git-root atomicity; artefact home)
- Publishing/push of organisation artefacts unless separately requested
- Marking the whole `C:\Project` organisation program “complete”

## Hand-off for orchestrator

User answers are locked in `notes.md`. Proceed to researcher with this refined prompt; do **not** re-ask Cycle 0 or Cycle 1 clarifying questions. Remaining user actions after this cycle: sign off proposed-ratified taxonomy; review must-preserve draft; choose/approve next Early/simple batch (and later git-strategy before complex git moves).
