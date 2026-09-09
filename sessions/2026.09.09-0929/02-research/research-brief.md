# Research brief

Session: `sessions/2026.09.09-0929/02-research/`  
Authoritative prompt: `../01-prompt-betterment/refined-prompt.md`  
Scope: **Cycle 0 — Program charter** (analysis & docs only; **zero moves** under `C:\Project`).

## Recommended approach

**Preferred (first-cut): Hybrid — Organisation-repo index + status×date physical layout under `C:\Project`, executed later by adaptive top-level-folder cycles.**

1. **Cycle 0 deliverables (this FAW):** program charter, coarse inventory (this research), taxonomy `yyyy.mm.dd + name`, organisation-approach recommendation, adaptive roadmap with approval gates + dedicated **multi-repo git strategy** planning thread before any git-root moves.
2. **Durable navigation (all cycles):** maintain a whole-corpus **index** in this organisation repo (status, date label, path, git-root flag, “next” notes). Index is the primary “dated view + next + find it” surface even before physical layout is finished.
3. **Later physical layout under `C:\Project`:** introduce light **status buckets** (e.g. `active` / `paused` / `archive` — or PARA-lite) and rename/move project folders to `yyyy.mm.dd - DescriptiveName`, **one top-level folder (or approved batch) at a time** after user approval. Treat each `.git` directory as an **atomic unit**; include dep caches and opaque secrets with the move.
4. **Do not** default to monorepo history rewrite or mass delete of zips; those need explicit later decisions.

## Options considered (max 3)

### 1. Hybrid index + status×date FS (recommended)

- **What:** Index in org repo now; gradual moves into status buckets with dated names under `C:\Project`.
- **Pros:** Matches end-state (history + next + navigation); dates sort; status answers “what’s next”; FAW-friendly adaptive cycles; lowest risk of early breakage.
- **Cons:** Temporary dual reality (old paths + new index) until batches complete; needs discipline to update index after each approved move.

### 2. Index-only (catalog corpus; defer almost all FS change)

- **What:** Rich markdown/JSON inventory and “next” lists; leave folders where they are except rare hygiene.
- **Pros:** Zero move risk; fastest Cycle 0–1 value; good if user later rejects physical reorg.
- **Cons:** Weakens “organisation” end-state; navigation still fights messy names/wrappers; user already chose agent-executed moves after approval for later cycles.

### 3. Pure chronological flat corpus (year or date folders only)

- **What:** Re-home everything under `2025/`, `2026/` or only `yyyy.mm.dd - name` with little/no status layer.
- **Pros:** Strong dated history; simple mental model.
- **Cons:** Poor “what’s next”; active work buried among archives; still needs git-atomic moves and worktree care — same risk as hybrid without the navigation benefit of status buckets.

## Inventory summary (for planner)

- **~29** top-level entries under `C:\Project`; corpus is mostly **2025** creations with **2026** additions (incl. this org effort).
- **≥32** candidate git roots at depth ≤2 (lower bound; deeper not scanned).
- Patterns: many **wrapper folders**; a few **multi-repo containers** (`ProjetOrif`, `PWAExemple`, `WorkSpace`, …); **Obsidian worktrees**; **HTTP Battles** empty parent git + real child; **root orphans** (`package.json` / Docker / `node_modules`).
- **Default-protect:** `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation`.
- Secrets: at least one `.env` path at depth 1 — never open; move opaque with project later.
- Detail: `codebase-findings.md`.

## Taxonomy sketch (input to planner; not final charter)

- **Folder/project label:** `yyyy.mm.dd - ShortName` (match sessions; prefer creation/start date, not LastWrite).
- **Ambiguities to call out in plan/charter:** date source (filesystem Created vs first commit vs user memory); wrappers vs nested git name; container splits; spaces vs hyphens; whether status bucket is prefix (`archive/2025.06.05 - Simpl`) or separate axis.
- **Already conforming example:** `2026.09.09 - Organisation`.

## Git-root implications

| Rule | Implication |
| --- | --- |
| Atomic unit | Move/rename entire directory containing `.git` (and linked worktrees together) |
| Remotes | Sample shows mixed HTTPS/SSH; path move usually keeps remotes; verify after move |
| Nested / empty parents | Classify `HTTP Battles` before touching |
| Worktrees | `Obsidian` main + 3 worktrees — dedicated handling in git-strategy cycle |
| Containers | `ProjetOrif` etc. may need **sub-batches** inside one top-level cycle |
| History rewrite | Out of scope unless git-strategy cycle explicitly chooses monorepo/`filter-repo` |

**Mandatory later thread:** multi-repo git strategy planning **before** any cycle that moves git roots (remotes, worktrees, nested repos, absolute-path configs, agent vs user push).

## Suggested adaptive cycle slicing (by top-level folder)

Order is a **starting suggestion** (easy → hard; adjust after charter review). Each move-capable cycle: classify → propose map → **user approves** → execute → update index.

| Priority | Top-level | Rationale |
| --- | --- | --- |
| Protect | `2026.09.09 - Organisation` | Default-preserve; never batch-move casually |
| Early / simple | `PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest` | Few/no git roots or single experiment |
| Medium wrappers | `NextTest`, `Simpl`, `Simpl_Next`, `TestRyan`, `ReactRouterTest`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining` | One nested git each; check `.env` on NextPWA |
| Multi-experiment | `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace` | Multiple nested roots |
| Special git | `WebCatalogue`, `HTTP Battles` | Top-level git; empty-parent oddity |
| High complexity | `ProjetOrif` | Many nested roots / variants — may split into sub-cycles |
| Worktree-critical | `Obsidian` | Only after git-strategy thread |
| Hygiene batch | Root `package.*`, Docker, `node_modules`, `.vscode` | Separate approved mini-batch |

Insert a **Git-strategy planning cycle** before any of: Obsidian, ProjetOrif multi-root moves, or any batch that relocates worktrees / changes remote assumptions.

## Required facts

- Cycle 0 = docs/index in org repo only; **zero** FS mutation under `C:\Project`.
- End-state: dated view + what’s next + easy navigation; no functionality/info loss.
- Naming: `yyyy.mm.dd` + name.
- Later moves: agent-executed **after per-batch approval**; include deps/secrets as payload; don’t deep-inventory caches.
- Artefact home: material under `C:\Project`; index/docs in organisation repo.
- Must-preserve list: **TBD** (open); org repo default-protected.
- Publish/push of corpus or Cycle 0 artefacts: **not required** by refined prompt.

## Unknowns / open decisions

- Full **must-preserve** path list (beyond org repo).
- Final status taxonomy (PARA vs active/paused/archive vs year+status).
- Date attribution rules for renaming.
- Keep vs split multi-project containers.
- Keep sidecar `.zip` files forever vs archive policy.
- Whether root orphan Node/Docker belongs to a known project or junk.
- Deeper-than-2 git roots not yet inventoried.
- Absolute-path breakage surface (IDE, Docker, scripts) per project — verify at move time.

## Risks and blockers

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Incomplete must-preserve → accidental move of critical path | High | Fail-closed; expand must-preserve before first move cycle |
| Skipping git-strategy before worktree/nested moves | High | Hard gate in roadmap |
| Shallow scan missed deep git roots | Medium | Re-scan target folder at start of each top-level cycle |
| Huge `node_modules` moves slow/fragile | Medium | Batch size limits; same-volume rename when possible |
| Dual HTTPS/SSH remotes confuse later agent push | Medium | Document per-repo in git-strategy cycle (informational now) |
| Secret leakage into session logs | High | Path-only; never open `.env` |
| Over-committing organisation design in Cycle 0 | Medium | Present options + preferred cut; user reviews before moves |

**Cycle 0 blockers for research/planning:** none identified that prevent charter/inventory/taxonomy/roadmap docs.

### Push/auth dual preflight

**Publish / agent push not in scope for Cycle 0** (refined prompt). Dual preflight **not executed**. Informational only: corpus remotes exist (HTTPS and SSH samples); org repo has HTTPS origin on `main`. If a later cycle requires agent push of organisation artefacts, run full dual preflight then.

| Field | Value |
| --- | --- |
| Remote URL scheme | n/a for this cycle (sample: org HTTPS; corpus mixed HTTPS/SSH) |
| Tracking branch | n/a (org sample: `main`) |
| Agent git / credential.helper | **not preflighted** — publish out of scope |
| Prefer GfW path (Windows HTTPS)? | n/a this cycle |
| GCM / non-interactive evidence | n/a this cycle |
| `gh` present? | not checked this cycle |
| User-terminal push note | none relied upon |
| `blocker_type` | **none for Cycle 0 research** (publish N/A) |
| Blocker / remediation | Re-run dual preflight when a cycle explicitly requires agent push |

## Canonical references

- Forte Labs — [PARA Method](https://fortelabs.com/blog/para/) — actionability buckets for “what’s next.”
- [ISO-oriented date naming practices](https://renamer.ai/insights/file-naming-conventions-best-practices) — chronological sort; gradual rename.
- [git-worktree docs](https://git-scm.com/docs/git-worktree) — linked checkouts must move carefully.
- [Netlify multirepo→monorepo guide](https://developers.netlify.com/guides/migrating-git-from-multirepo-to-monorepo-without-losing-history/) — history rewrite ≠ simple folder move.
- [Developer status-first Projects layout](https://thatamazingprogrammer.com/posts/a-practical-folder-structure-for-developers-and-solopreneurs/) — active/paused/archive pattern.
- [Indexed local project sprawl](https://dev.to/saqueib/keeping-laravel-projects-findable-when-local-work-starts-to-sprawl-55na) — metadata + unique names + search.
- Local: `codebase-findings.md`, `online-findings.md`, `../01-prompt-betterment/refined-prompt.md`, `AGENTS.md`.

## Hand-off to planner

Produce Cycle 0 **plan** for: charter + inventory artefact (may promote/refine this research) + taxonomy proposal + organisation-approach recommendation (options above) + adaptive multi-cycle roadmap with approval gates and git-strategy thread. **Do not** schedule FS moves in Cycle 0 implementation. Keep diffs small and in the organisation repo only.
