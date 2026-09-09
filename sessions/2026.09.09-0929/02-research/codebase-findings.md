# Codebase findings

Session: `sessions/2026.09.09-0929/02-research/`  
Corpus root: `C:\Project`  
Scan date: 2026-09-09  
Method: top-level listing + shallow nested `.git` discovery (depth 0–2 under each top-level dir; skipped `node_modules` / common build-cache dir names). **No moves.** Secret files: path presence only, contents not read.

## Default-protected path

- `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` — organisation / FAW host repo (nested git root). Treat as **must-preserve by default** until user finalises must-preserve list.

## Corpus shape (summary)

| Signal | Value |
| --- | --- |
| `C:\Project` itself a git root? | **No** |
| Top-level entries | **29** (25 dirs + 4 files) |
| Creation-year mix (top-level) | **2025: 24**, **2026: 5** |
| LastWrite span (top-level) | oldest `Simpl` ~2025-06-05 → newest `2026.09.09 - Organisation` 2026-09-09 |
| Candidate git roots (depth ≤2) | **32** |
| Root orphan tooling | `package.json`, `package-lock.json`, `Dockerfile`, `.dockerignore`, top-level `node_modules/` (inventory note only; do not deep-list) |
| `.env` path (depth 0–1) | `NextPWATraining\blogr-nextjs-prisma\.env` (presence only) |

## Top-level inventory

| Name | Type | Created | LastWrite | Kids / size | Git @ top? | Type guess / notes |
| --- | --- | --- | --- | --- | --- | --- |
| `.vscode` | dir | 2025-08-07 | 2025-09-05 | 2 | no | Workspace IDE config for corpus root |
| `2026.09.09 - Organisation` | dir | 2026-09-09 | 2026-09-09 | 1 | no | **Already dated naming**; wrapper for org repo. **Default-protect** nested git |
| `AngularTest` | dir | 2025-08-07 | 2025-08-07 | 2 | no | Tutorial / zip + extracted app |
| `CursorMobileWorkspace` | dir | 2026-06-17 | 2026-06-17 | 1 | no | Wrapper; nested git at depth 1 |
| `epsic` | dir | 2025-12-10 | 2025-12-17 | 3 | no | Course-like (BDD, HTML + zip) |
| `GitTest` | dir | 2025-08-08 | 2025-08-08 | 2 | no | Sandbox with **2 nested git roots** |
| `HTTP Battles` | dir | 2025-06-05 | 2025-06-05 | 2 | **yes** | Parent `.git` = **empty repo (no commits)**; real project in nested `http-battles` with remotes |
| `IA` | dir | 2025-12-12 | 2025-12-12 | 1 | no | Misc (`Teams-Messages`) |
| `NextPWATraining` | dir | 2025-06-23 | 2025-06-23 | 1 | no | Nested Next/Prisma blog; **`.env` present** |
| `NextTest` | dir | 2025-06-23 | 2025-06-23 | 1 | no | Wrapper + nested git |
| `node_modules` | dir | 2025-06-24 | 2025-11-18 | 27 pkgs | no | **Orphan root deps** — note presence only; move-preservation payload later if tied to root package |
| `Obsidian` | dir | 2026-04-13 | 2026-05-26 | 2 | no | Vault + **linked worktrees** under `worktrees/` |
| `PlayTestTristan` | dir | 2025-06-23 | 2025-06-23 | 2 | no | RPG experiment + zip |
| `PostManResponses` | dir | 2025-10-01 | 2025-10-01 | 1 | no | Loose artefact (`response.html`) — junk/snippet candidate |
| `ProjetOrif` | dir | 2025-08-07 | 2026-01-07 | 11 | no | **Multi-project container**; several nested git roots (depth 2); highest complexity |
| `PWAExemple` | dir | 2025-06-25 | 2025-06-30 | 3 | no | Multiple PWA experiments; 2 nested gits |
| `PWAExempleTristan` | dir | 2025-07-04 | 2025-07-04 | 1 | no | Nested git |
| `ReactRouterTest` | dir | 2025-08-12 | 2025-08-12 | 1 | no | Nested git |
| `Simpl` | dir | 2025-06-05 | 2025-06-05 | 1 | no | Nested `Project-Simpl` git |
| `Simpl_Next` | dir | 2025-06-23 | 2025-06-23 | 1 | no | Nested git |
| `TestRyan` | dir | 2025-06-25 | 2025-06-25 | 1 | no | Nested python mini-games git |
| `WebCatalogue` | dir | 2025-11-07 | 2025-12-22 | 9 | **yes** | Flat project root with README; SSH remote |
| `WorkSpace` | dir | 2026-05-29 | 2026-06-10 | 2 | no | Agent/workspace experiments; nested gits + deeper `hermes-agent` |
| `WorkStationPWA` | dir | 2025-07-01 | 2025-08-12 | 4 | no | PWA + zip favicon assets; nested gits |
| `ZedTest` | dir | 2026-06-30 | 2026-07-01 | 4 | no | Scraping experiment (`.pytest_cache` present — cache note only) |
| `.dockerignore` | file | 2025-09-05 | 2025-09-05 | 341 B | — | Orphan root Docker context |
| `Dockerfile` | file | 2025-09-05 | 2025-09-05 | 379 B | — | Orphan root Docker context |
| `package-lock.json` | file | 2025-06-24 | 2025-11-18 | ~37 KB | — | Ties to root `package.json` / `node_modules` |
| `package.json` | file | 2025-06-24 | 2025-11-18 | 188 B | — | Vite/React/tone/workbox deps — **not** a clear project folder |

## Candidate git roots (shallow)

### Depth 0 (top-level `.git`)

- `HTTP Battles` — empty parent repo (no commits); contains nested real repo
- `WebCatalogue` — active project git root

### Depth 1

- `2026.09.09 - Organisation\2026.09.09---Organisation` (**default-protect**)
- `CursorMobileWorkspace\CursorMobileWorkspace`
- `GitTest\NextTest`, `GitTest\test`
- `HTTP Battles\http-battles` (has HTTPS origin)
- `NextPWATraining\blogr-nextjs-prisma`
- `NextTest\NextTest`
- `Obsidian\Obsidian` (main vault; worktrees linked)
- `PWAExemple\PWAExempleNext`, `PWAExemple\PWAFrontAuthTest`
- `PWAExempleTristan\PWATristan`
- `ReactRouterTest\ReactRouterTest`
- `Simpl\Project-Simpl`
- `Simpl_Next\SimplNext`
- `TestRyan\python-mini-jeux`
- `WorkSpace\OS-IA`, `WorkSpace\TestNewWorkspaceAgent`
- `WorkStationPWA\WorkStationPWA`

### Depth 2 (notable)

- `Obsidian\worktrees\*` — **3 additional git worktree checkouts** (linked to `Obsidian\Obsidian`)
- `ProjetOrif\frontBack\template_frontback` (+ Clean / TestAzure / `_test` variants)
- `ProjetOrif\springAuth\spring-auth`
- `ProjetOrif\testSpringDoc\gs-rest-service`, `gs-testing-restdocs`
- `WorkSpace\TestNewWorkspaceAgent\hermes-agent`
- `WorkStationPWA\WorkStationRouterPWA\workstation-app`

**Depth limit:** roots deeper than 2 were not scanned. Planner/auditor should treat the 32 count as a **lower bound**.

## Sample remotes (informational; Cycle 0 does not require push)

| Path | Origin scheme (redacted) | HEAD tip |
| --- | --- | --- |
| `HTTP Battles` | (no origin) | empty master |
| `HTTP Battles\http-battles` | `https://github.com/.../http-battles.git` | `kenV2` |
| `WebCatalogue` | `git@github.com:.../WebCatalogue.git` | `feature/add-simple-game` |
| org repo | `https://github.com/.../2026.09.09---Organisation.git` | `main` |
| `Obsidian\Obsidian` | HTTPS | `main` + 3 worktrees |
| `ProjetOrif\...\template_frontback` | HTTPS (`OrifInformatique`) | `develop` |
| `WorkSpace\OS-IA` | HTTPS | `master` |
| `Simpl\Project-Simpl` | HTTPS | `BetaCorr` |

Mixed **HTTPS and SSH** remotes across corpus — relevant for later git-strategy cycle, not Cycle 0 publish.

## Organisation-repo prior art (why it matters)

- `AGENTS.md`, `.cursor/skills/full-agent-workflow/SKILL.md`, `.cursor/agents/*` — FAW law; Cycle 0 artefacts stay here; later moves stay under `C:\Project`.
- Session naming already uses `yyyy.mm.dd` / `yyyy.mm.dd-HHMM` — aligns with user taxonomy preference.
- `sessions/2026.09.09-0929/01-prompt-betterment/refined-prompt.md` — authoritative Cycle 0 scope (charter + inventory + taxonomy + roadmap; **zero moves**).
- Existing FAW session history under `sessions/` shows mature workflow docs pattern for index/charter placement.

## Signals useful for later adaptive cycles

1. **Wrapper pattern:** many top-level folders are thin shells around one nested project (good atomic move unit = wrapper **or** nested git — decide per folder).
2. **Containers:** `ProjetOrif`, `PWAExemple`, `WorkSpace`, `WorkStationPWA`, `GitTest` need **split or keep-together** decisions inside a top-level cycle.
3. **Worktrees:** `Obsidian` must be moved as a **linked set** (main + `worktrees/*`) or worktrees repaired — see online git-worktree notes.
4. **Empty/nested git oddity:** `HTTP Battles` parent `.git` vs real child repo — classify before any rename.
5. **Root orphans:** package/Docker/`node_modules` — candidate for a dedicated “root hygiene” mini-batch (still after approval).
6. **Zips beside extracts:** several folders keep `.zip` siblings — archive vs delete is user policy (Cycle 0: do not delete).
7. **Date anchors:** prefer `CreationTime` / earliest commit / user-known start for `yyyy.mm.dd` labels; LastWrite ≈ last activity for “what’s next” triage, not primary name date.
8. **Already-dated:** `2026.09.09 - Organisation` is a live example of preferred naming.

## Explicit non-actions this pass

- No deep walk of `node_modules` / caches
- No reading of `.env` or credential stores
- No moves / renames / deletes
- No full remote inventory for all 32 roots (sample only)
