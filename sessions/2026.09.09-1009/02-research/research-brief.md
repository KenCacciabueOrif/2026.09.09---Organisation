# Research brief — Cycle 1 (Docs follow-ups)

Session: `sessions/2026.09.09-1009/02-research/`  
Authoritative prompt: `../01-prompt-betterment/refined-prompt.md`  
User locks: `../01-prompt-betterment/notes.md`  
Scope: **docs_only** deepen catalogue + propose-ratify taxonomy + ROADMAP next-row; **zero** FS mutation under `C:\Project`. Publish/push **not** in scope.

## Recommended approach

**Preferred: Option A — Docs deepen + proposed-ratify in place (no physical moves).**

1. Mark `catalogue/taxonomy.md` **proposed-ratified — ready for user sign-off** with locked rules: status `active`/`paused`/`archive` + INDEX `protect`/`hygiene`; ShortName keeps spaces; **CreationTime wins** for proposed date labels; wrapper = canonical dated label / nested `.git` = child atomic units; empty-parent / multi-root edges stay in a short “classify before move” note.
2. Deepen `catalogue/inventory.md` (+ INDEX columns/notes) with **cheap size bands S/M/L/XL**, clearer **depth≤2** git-root notes + scan limits, **LastWrite as activity** hints; skip secrets/deep deps.
3. Add **must-preserve draft** candidate list beyond org-repo default-protect — explicitly **draft — not auto-locked**.
4. Update INDEX “What’s next” and `program/ROADMAP.md`: Cycle 1 complete; **primary next = Early/simple**; **Git-strategy** remains hard-gate reminder (not primary next row).
5. Prove docs_only: no intentional moves/renames/deletes under `C:\Project`.

## Options considered (max 3)

### A. Docs deepen + proposed-ratify (recommended)

- **What:** Update taxonomy/inventory/INDEX/ROADMAP only in org repo.
- **Pros:** Matches refined prompt; unlocks user sign-off and Early/simple prep without mutation risk; cheap size/git/activity signals land in catalogue.
- **Cons:** Dual reality (old FS names + proposed labels) continues until move cycles.

### B. Docs + provisional status assignment pass on INDEX

- **What:** Same as A, plus replace many `TBD` statuses with guessed `paused`/`archive` from LastWrite age.
- **Pros:** Stronger “what’s next” immediately.
- **Cons:** Risk of over-claiming status before user review; refined prompt only requires legend sync + deepen — keep status guesses **optional / clearly provisional** if used.

### C. Defer inventory deepen; taxonomy-only cycle

- **What:** Only proposed-ratify taxonomy + ROADMAP next-row.
- **Pros:** Smaller diff.
- **Cons:** Fails acceptance criteria (size bands, git notes, LastWrite hints, must-preserve draft required).

## Inventory deepen facts (for planner/implementer)

| Fact | Detail |
| --- | --- |
| Top-level count | 29 (unchanged) |
| Git roots depth≤2 | **32** lower bound (unchanged list; clearer wrapper classes) |
| Size bands (cheap, excl. node_modules/.git/caches) | S=17, M=9, L=1 (`ProjetOrif`), XL=2 (`WorkSpace`, `Obsidian`) |
| Suggested cutoffs | S &lt;1MB · M &lt;50MB · L &lt;500MB · XL ≥500MB — document in inventory |
| HTTP Battles | Parent `.git` **0 commits**; nested `http-battles` = real project — classify-before-move |
| Early/simple (no git ≤1) | `PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest` |
| `.env` | Path present under NextPWATraining nest — presence only |

Detail tables: `codebase-findings.md`.

## Taxonomy locks to write (proposed-ratified)

| Topic | Locked decision |
| --- | --- |
| Status axis | `active` / `paused` / `archive` + INDEX specials `protect` / `hygiene` — **not** PARA-lite |
| ShortName | Keep spaces: `yyyy.mm.dd - ShortName` |
| Date default | **CreationTime wins** over earliest commit and LastWrite; user memory may override later |
| LastWrite | Activity / “next” signal only |
| Wrapper vs nested | Canonical dated label on **wrapper** (top-level move unit); nested `.git` = **child atomic units** |
| Edges | Empty-parent / multi-root: short open note; default rule still proposed-ratified |
| Ratification language | **proposed-ratified — ready for user sign-off** — do **not** claim final user ratification |

## Must-preserve draft (propose for catalogue)

Label: **draft — not auto-locked**. Candidates beyond default-protect:

1. `Obsidian` (worktrees / XL)
2. `ProjetOrif` (7 nested @ depth 2 / L)
3. `WebCatalogue` (top-level git)
4. `WorkSpace` (XL / multi-nested)
5. `HTTP Battles` (+ nested real repo) — classify before casual batch
6. Optional: `CursorMobileWorkspace`, `NextPWATraining` (opaque `.env`)

User reviews before first move-capable cycle; fail-closed if unclear.

## ROADMAP next-row suggestion

| Priority | Suggestion |
| --- | --- |
| **Primary next** | **Early/simple** — move-prep / first simple batch after per-batch approval (`PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest`) |
| Rationale | No nested git at depth≤1; mostly S/M; exercises approve→execute→INDEX while taxonomy only proposed-ratified |
| **Hard gate (not primary)** | Dedicated **Git-strategy** FAW before Obsidian / ProjetOrif multi-root / worktree moves |

Cycle 1 itself must **not** execute Early/simple or git-strategy bodies.

## Required facts

- Mutation class: **docs_only**; corpus scan read-only.
- Inherit Cycle 0 locks: dated end-state; naming form; per-batch approval; git atomicity; artefact home.
- Publish/push: **not required**.
- Auditor: zero intentional FS moves under `C:\Project` attributable to this cycle.

## Unknowns (non-blocking for Cycle 1 docs)

- Final user sign-off on taxonomy / must-preserve draft (after this cycle).
- Which Early/simple subset becomes the first approved batch.
- Keep-vs-split for multi-nested containers (still open; wrapper default holds).
- Deeper-than-2 git roots (re-scan at move time).
- Absolute-path breakage surface per project (verify at move time).
- Whether implementer assigns provisional INDEX statuses beyond legend sync (optional).

## Risks and blockers

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Claiming final taxonomy ratification | High | Explicit “proposed-ratified / ready for sign-off” wording |
| Scope creep into Early/simple or git-strategy execution | High | Out of scope; ROADMAP pointer only |
| Treating proposed date labels as renames | Medium | INDEX caveat language |
| Cheap size understates true disk (excl. node_modules/.git) | Low | Document metric + band cutoffs |
| Missed deep git roots | Medium | Keep “lower bound / re-scan before move” |
| Secret leakage | High | Path-only; never open `.env` |
| Must-preserve draft incomplete | Medium | Fail-closed until user reviews; draft label |

**Cycle 1 research blockers:** **none** for docs_only catalogue/program updates.

### Push/auth dual preflight

**Publish / agent push not in scope for Cycle 1** (refined prompt). Dual preflight **not executed**.

| Field | Value |
| --- | --- |
| Remote URL scheme | n/a this cycle |
| Tracking branch | n/a |
| Agent git / credential.helper | **not preflighted** |
| Prefer GfW path (Windows HTTPS)? | n/a |
| GCM / non-interactive evidence | n/a |
| `gh` present? | not checked |
| User-terminal push note | none relied upon |
| `blocker_type` | **none for Cycle 1 research** (publish N/A) |
| Blocker / remediation | Re-run dual preflight if a later cycle requires agent push |

## Canonical references

- Local: `codebase-findings.md`, `online-findings.md`, Cycle 0 research under `sessions/2026.09.09-0929/02-research/`, `catalogue/*`, `program/*`, `refined-prompt.md`, `notes.md`
- [Status-first Projects layout](https://thatamazingprogrammer.com/posts/a-practical-folder-structure-for-developers-and-solopreneurs/)
- [CASRAI file naming — document which date](https://casrai.org/guides/file-naming-and-folder-structure-conventions-for-research-data)
- [git-worktree](https://git-scm.com/docs/git-worktree) — Obsidian hard-gate evidence
- [CreationTime vs LastWriteTime](https://stackoverflow.com/questions/10277741/how-can-fileinfo-lastwritetime-be-earlier-than-fileinfo-creationtime)
- [Netlify multirepo note](https://developers.netlify.com/guides/migrating-git-from-multirepo-to-monorepo-without-losing-history/) — intact moves ≠ history rewrite

## Hand-off to planner

Plan Cycle 1 **docs_only** implementation: proposed-ratify taxonomy (+ INDEX legend), deepen inventory with bands/git notes/LastWrite activity, must-preserve draft section, INDEX What’s next + ROADMAP Early/simple primary + Git-strategy hard-gate reminder. **Do not** schedule FS moves, Early/simple execution, or git-strategy deliverables in this cycle.
