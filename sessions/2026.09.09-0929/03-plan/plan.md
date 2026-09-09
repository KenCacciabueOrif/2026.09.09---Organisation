# Plan — Cycle 0 (Program charter)

Session: `sessions/2026.09.09-0929/`  
Authoritative inputs: `../01-prompt-betterment/refined-prompt.md`, `../02-research/research-brief.md` (+ findings)  
Scope: **documentation / index artefacts only** inside this organisation repo. **Zero** moves, renames, or deletes under `C:\Project`.

## Goal

Deliver Cycle 0 of the multi-cycle `C:\Project` organisation program: a durable **program charter**, a **coarse inventory** (promoted from research), a **`yyyy.mm.dd` + name taxonomy proposal**, a **first-cut organisation-approach recommendation** (hybrid index + later status×date layout), and an **adaptive multi-cycle roadmap** (top-level-folder slices, per-batch approval gates, mandatory multi-repo git-strategy planning thread before any git-root moves). All Cycle 0 outputs live in this organisation repo (`program/` + `catalogue/`); physical reorganisation of corpus material is deferred to later cycles under `C:\Project`. Publish/`git push` is **not** required for this cycle.

## Acceptance criteria

- [ ] **Program charter** exists at `program/CHARTER.md` (purpose/end-state, non-goals, safety, Cycle 0 vs later, adaptive top-level-folder cycle model, how to invoke the next cycle; default-protect org repo; must-preserve list marked TBD/open).
- [ ] **Coarse inventory artefact** exists at `catalogue/inventory.md` (top-level / near-top map from research; type/size/date signals; candidate git roots; no deep `node_modules`/cache docs; no secret contents).
- [ ] **Taxonomy proposal** exists at `catalogue/taxonomy.md` (`yyyy.mm.dd - Name` format; decision rules; good vs ambiguous examples; open ambiguities called out).
- [ ] **Organisation-approach recommendation** exists at `program/organisation-approach.md` (≤3 options; preferred hybrid; no moves executed).
- [ ] **Adaptive multi-cycle roadmap** exists at `program/ROADMAP.md` (cycles by top-level folder; flexible count; user approval gate before each move batch; dedicated **git-strategy planning** cycle/thread before any git-root moves; git roots treated as atomic units).
- [ ] **Corpus index stub** exists at `catalogue/INDEX.md` as the durable “dated view + what’s next + navigate” surface (seeded from inventory; paths still current under `C:\Project`).
- [ ] **README** in this org repo links to `program/` and `catalogue/` so Cycle 0 outputs are discoverable outside the session folder.
- [ ] Session implementation notes under `sessions/2026.09.09-0929/04-implementation/` record what was written and explicitly state **zero FS mutations** under `C:\Project`.
- [ ] Auditor can confirm: **no** intentional moves/renames/deletes under `C:\Project` attributable to this cycle (org-repo doc adds only).
- [ ] No secrets (`.env` contents, tokens, credentials) in any new artefact or session log; `.env` may appear as **path presence only**.
- [ ] **Publish/push not required** — Cycle 0 complete when docs exist locally in the org repo; do not block on dual auth/preflight.

## Recommended durable layout (create in Cycle 0)

| Path | Role |
| --- | --- |
| `program/CHARTER.md` | Program law: purpose, non-goals, safety, cycle model, invoke-next |
| `program/ROADMAP.md` | Adaptive cycle slicing + approval gates + git-strategy gate |
| `program/organisation-approach.md` | Options + preferred hybrid recommendation |
| `catalogue/INDEX.md` | Whole-corpus navigation index (status / date / path / git / next) |
| `catalogue/inventory.md` | Coarse inventory (from research; refined presentation OK) |
| `catalogue/taxonomy.md` | Naming scheme + rules + examples |
| `README.md` | Add short “Program / catalogue” pointer section |

Session mirrors (optional thin pointers, not duplicate bodies unless useful):

| Path | Role |
| --- | --- |
| `sessions/2026.09.09-0929/04-implementation/changes.md` | List of files created/updated |
| `sessions/2026.09.09-0929/04-implementation/log.md` | Steps taken; zero-move attestation |
| `sessions/2026.09.09-0929/03-plan/plan-mermaid.md` | Cycle-flow diagram (already planned; keep if written) |

**Artefact home rule (write into charter):** organised *material* stays under `C:\Project` when moves happen later; *outputs / index / docs* stay in this organisation repo.

## Steps

### 0. Confirm scope (no push preflight)

- **Paths:** repo root `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`
- **Action:** Confirm Cycle 0 is docs-only; **skip** dual auth/preflight (publish not in AC). Do not `git push`. Do not `git add`/`commit` unless the user separately asks (default: leave working tree dirty for user review).
- **Verify:** Plan AC does not require remote publish; implementer does not attempt push.

### 1. Create `program/` and write charter

- **Paths:** `program/CHARTER.md` (new)
- **Action:** Author a short charter covering:
  1. **End-state:** dated view of what happened + what’s next + easy navigation across projects.
  2. **Non-goals:** no functionality breakage; no information loss; no unsupervised FS mutation; Cycle 0 does not finish physical organisation.
  3. **Safety:** zero moves in Cycle 0; later agent-executed moves **only after per-batch user approval**; never open/read `.env`/credential contents (opaque payload on move); do not deep-document dep/cache trees; include them when moving.
  4. **Atomic git units:** each folder with its own `.git` is one project; do not split a git root without an explicit plan.
  5. **Default-protect:** `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` until must-preserve list is finalised (**TBD / open**).
  6. **Cycle model:** adaptive rounds sliced primarily by **top-level folder** under `C:\Project` (no fixed N); insert a **git-strategy planning** cycle before any cycle that moves git roots / worktrees.
  7. **How to invoke next cycle:** open Agent chat in this repo → `/full-agent-workflow` (or equivalent) → state goal referencing `program/ROADMAP.md` next suggested slice (e.g. “Cycle 1: deepen inventory / ratify taxonomy” or first simple top-level folder after user review) → new `sessions/yyyy.mm.dd…` folder.
  8. Point to `catalogue/INDEX.md` as the living navigation surface.
- **Sources:** refined prompt; research brief Recommended approach / Required facts.
- **Verify:** File exists; sections above present; no move instructions executable in Cycle 0.

### 2. Promote / refine coarse inventory

- **Paths:** `catalogue/inventory.md` (new); sources `sessions/2026.09.09-0929/02-research/codebase-findings.md`
- **Action:** Create inventory artefact from research (may refine presentation, not re-scan unless cheap and safe):
  - Corpus summary (~29 top-level; creation-year mix; ≥32 candidate git roots depth ≤2 as **lower bound**).
  - Top-level table (name, type guess, Created/LastWrite if known, git-at-top?, notes).
  - Candidate git-root list (depth 0–2); note depth limit.
  - Explicit exclusions: no deep `node_modules`/cache trees; root orphans noted as presence only.
  - Secrets: path presence only (e.g. `NextPWATraining\blogr-nextjs-prisma\.env`) — **never** quote contents.
  - Default-protect callout for org repo path.
- **Verify:** All top-level entries from research represented; git roots flagged; no secret values; no claim of complete deep scan.

### 3. Write taxonomy proposal

- **Paths:** `catalogue/taxonomy.md` (new)
- **Action:** Document:
  - **Canonical form:** `yyyy.mm.dd - ShortName` (dots + space-hyphen-space; match sessions / `2026.09.09 - Organisation`).
  - **Decision rules:** prefer project/start date (CreationTime or earliest meaningful commit or user-known start) over LastWrite for the date prefix; LastWrite = activity signal for “next,” not primary name date; descriptive ShortName without `final`/`v2` noise; one label per atomic project/wrapper decision unit.
  - **Status axis (separate from date):** propose status buckets for *later* physical layout (`active` / `paused` / `archive` preferred first-cut; PARA-lite as alternative) — status is **not** encoded in the date string.
  - **Good examples:** `2026.09.09 - Organisation`; illustrative renames for simple wrappers (e.g. conceptual `2025.06.05 - Simpl` — label only, **do not rename now**).
  - **Ambiguous examples / open rules:** wrappers vs nested git name; multi-repo containers (`ProjetOrif`, …); empty parent git (`HTTP Battles`); spaces vs GitHub-style hyphens inside ShortName; date source conflicts; zip sidecars; root orphans.
- **Verify:** Format matches user preference; ambiguities listed as open (not silently decided); no FS rename executed.

### 4. Write organisation-approach recommendation

- **Paths:** `program/organisation-approach.md` (new)
- **Action:** Document the three options from research and recommend **Option 1 — Hybrid**:
  1. **Hybrid (preferred):** org-repo index now + gradual status×date layout under `C:\Project` later.
  2. **Index-only:** catalog/defer almost all FS change.
  3. **Pure chronological flat:** year/date folders without strong status layer.
  - Map each option to end-state goals (dated view / next / navigation) and risks.
  - State clearly: Cycle 0 implements **index + docs only**; physical layout waits for approved move cycles.
- **Verify:** Preferred approach explicit; “no moves in Cycle 0” restated; citations optional (Forte PARA, status-first layouts, date-prefix practices from `online-findings.md`).

### 5. Write adaptive multi-cycle roadmap

- **Paths:** `program/ROADMAP.md` (new); diagram optional in `sessions/2026.09.09-0929/03-plan/plan-mermaid.md`
- **Action:** Author roadmap with:
  - **Principles:** adaptive count; slice by top-level folder; each move-capable cycle = classify → propose batch map → **user approves** → agent executes (deps/secrets opaque) → update `catalogue/INDEX.md`; fail-closed on must-preserve.
  - **Hard gate:** dedicated **multi-repo git strategy planning** FAW cycle (remotes HTTPS/SSH, atomic moves, nested/empty parents, worktrees, absolute-path configs, agent vs user push) **before** any cycle that relocates git roots — especially before `Obsidian`, multi-root `ProjetOrif`, or worktree moves. Default: move intact `.git` trees; no history rewrite/`filter-repo` unless that cycle explicitly chooses it.
  - **Suggested order** (starting suggestion from research; adjustable after charter review):

    | Priority | Top-level / thread | Notes |
    | --- | --- | --- |
    | Protect | `2026.09.09 - Organisation` | Default-preserve; never casual batch-move |
    | Docs follow-ups | Cycle 1+ optional | Ratify taxonomy / deepen inventory / expand must-preserve |
    | Early / simple | `PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest` | Few/no git or experiments |
    | Medium wrappers | `NextTest`, `Simpl`, `Simpl_Next`, `TestRyan`, `ReactRouterTest`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining` | One nested git; `.env` opaque on NextPWA |
    | Multi-experiment | `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace` | Multiple nested roots; sub-batches OK |
    | Special git | `WebCatalogue`, `HTTP Battles` | Top-level git; empty-parent classify |
    | High complexity | `ProjetOrif` | May split into sub-cycles **after** git-strategy |
    | Worktree-critical | `Obsidian` | **After** git-strategy only |
    | Hygiene | Root `package.*`, Docker, `node_modules`, `.vscode` | Separate approved mini-batch |

  - **Insert** git-strategy planning cycle before Obsidian / ProjetOrif multi-root moves / any worktree relocation.
  - **How next cycle starts:** user reviews Cycle 0 → chooses next roadmap row → new FAW session.
- **Verify:** Approval gate and git-strategy gate are explicit; no Cycle 0 move steps; adaptive (not fixed N).

### 6. Seed corpus index stub

- **Paths:** `catalogue/INDEX.md` (new)
- **Action:** Create a navigable index table seeded from inventory, columns at minimum: **Status (guess/TBD)**, **Date label (current or proposed)**, **Current path under `C:\Project`**, **Git root?**, **Next / notes**. Mark status as provisional. Include a one-line legend and pointer to charter/roadmap/taxonomy. Do **not** invent completed renames as if already applied.
- **Verify:** All ~29 top-level entries appear or are grouped with rationale; org repo flagged protected; index is useful before any moves.

### 7. Wire README discoverability

- **Paths:** `README.md` (edit)
- **Action:** Add a short section (e.g. “Project corpus program”) linking to `program/CHARTER.md`, `program/ROADMAP.md`, and `catalogue/INDEX.md`. Do not rewrite unrelated README content.
- **Verify:** Links resolve; Cycle 0 outputs findable without opening session folders.

### 8. Session implementation record + zero-move attestation

- **Paths:** `sessions/2026.09.09-0929/04-implementation/changes.md`, `.../log.md`; update `sessions/2026.09.09-0929/SESSION.md` phase checklist when appropriate
- **Action:** List created/updated paths; state explicitly that implementer performed **no** moves/renames/deletes under `C:\Project` (only org-repo documentation). Note open decisions carried forward (must-preserve list, final status vocabulary, date-attribution conflicts, container split/keep, zip policy, root orphans).
- **Verify:** Auditor can cross-check file list vs git status in org repo and confirm corpus paths untouched by this cycle’s intent.

### 9. Stop conditions / handoff

- **Action:** Do not start a move cycle inside this FAW. Do not deepen inventory beyond promoting research unless a trivial presentation fix. Hand off to auditor against this plan’s AC.
- **Verify:** Implementation log ends with Cycle 0 complete (docs) or honest gap list; status not claiming “organisation finished.”

## Non-goals

- Any relocate / rename / delete under `C:\Project` (including “small” or “obvious” hygiene)
- Deep inventory of `node_modules`, build caches, or OS junk trees
- Opening, quoting, or committing `.env` / credential contents
- Finalising the full must-preserve path list (document as open; default-protect org repo only)
- Implementing multi-repo git migration, remote changes, worktree repairs, or history rewrite
- Committing or pushing organisation artefacts (unless user separately requests)
- Starting Cycle 1 / first move batch inside this same FAW without a new session after user review
- Declaring the corpus “organised” as a single-session outcome

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Accidental FS mutation under `C:\Project` | Implementer restricted to org-repo paths; auditor verifies zero corpus moves |
| Secret leakage into docs | Path-only for `.env`; never read contents; secrets gate on any future commit |
| Over-committing design (status names, date rules) | Present preferred cut + open ambiguities; user ratifies before moves |
| Incomplete git-root scan treated as complete | Inventory states depth ≤2 lower bound; per-folder re-scan at start of later cycles |
| Skipping git-strategy before hard folders | Hard gate in `ROADMAP.md` + charter |
| Dual reality (old paths vs future layout) confusing index | Index stores **current** paths; proposed labels separate until moves approved |
| Publish assumed required | Explicitly out of scope; no preflight; `ready_to_implement` not blocked on push |
| Rollback | Delete or revert new `program/` / `catalogue/` files and README section in org repo only; corpus unchanged |

## Publish / push

**Not required** for Cycle 0. Dual auth/preflight: **N/A**. If a later cycle requires agent push of organisation artefacts, run full dual preflight then (`agent_environment` vs `user_credentials`).

## Ready to implement

**yes**

Research blockers for Cycle 0 docs: **none**. Acceptance criteria are documentation-only with concrete paths; open product decisions (must-preserve expansion, final status vocabulary, date conflicts, container policy) are **documented as open** inside charter/taxonomy/roadmap — they do **not** block writing Cycle 0 artefacts. Push preflight is intentionally skipped.

## Blocking questions

**none** (for Cycle 0 implementation)

Open decisions to carry in artefacts (non-blocking):

1. Full must-preserve path list beyond default-protecting this organisation repo.
2. Final status vocabulary (`active`/`paused`/`archive` vs PARA-lite).
3. Date attribution when Created / first commit / memory disagree.
4. Keep vs split multi-project containers; zip sidecar policy; root orphan ownership.
