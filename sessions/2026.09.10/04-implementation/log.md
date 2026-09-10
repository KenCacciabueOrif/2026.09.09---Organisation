# Implementation log — Cycle 7 Multi-experiment (first subset)

**Session:** `sessions/2026.09.10/04-implementation/`  
**Plan:** `sessions/2026.09.10/03-plan/plan.md`  
**Mutation class:** `fs_mutation`  
**User batch approval:** yes (2026.09.10 — exact two-folder map)  
**Agent push/pull:** none attempted  

---

## Timeline

### Preflight (Step 1)

- Parent `C:\Project\archive` exists (directory).
- **GitTest:** source present; destination absent; nested `.git` count = 2 (`NextTest\.git`, `test\.git`); `.env*` count = 0.
- **WorkStationPWA:** source present; destination absent; nested `.git` count = 2 (`WorkStationPWA\.git`, `WorkStationRouterPWA\workstation-app\.git`); `.env*` count = 0.
- Nested remotes: GitTest HTTPS×2; WorkStationPWA HTTPS + one SSH (`git@github.com:KenCacciabueOrif/WorkStationRouterPWA.git`) — path-only policy; no rewrite.
- Worktrees: single main worktree each (no linked extras). Dirty trees present; not a fail-closed hazard per plan.
- Verify-only: `PWAExemple` + `WorkSpace` still at `C:\Project\` root; Medium/Early samples present (`archive\2025.06.23 - NextTest`, `archive\2025.07.04 - PWAExempleTristan`, `archive\2025.06.23 - NextPWATraining`, `paused\2026.06.17 - CursorMobileWorkspace`).
- `Move-Item` parameter check: `LiteralPath` + `Destination` available.

### Step 2 — Parent

- `archive` already present; no create.

### Step 3–4 — Moves + attestation

#### 1) GitTest

| Field | Value |
| --- | --- |
| From | `C:\Project\GitTest` |
| To | `C:\Project\archive\2025.08.08 - GitTest` |
| Method | Initial `Move-Item -LiteralPath` hit **PermissionDenied** removing `NextTest\.git` (lock), leaving a **split** tree; recovered by reunifying into destination then finishing remaining children |
| Nested-git attestation | `...\NextTest\.git` = **True**; `...\test\.git` = **True**; count = 2 |
| Opaque `.env` | Pre = 0; Post destination scan count = 0 |
| Source absent / dest present | **True** / **True** |
| Remotes | unchanged (no rewrite) |

**Recovery detail (GitTest):** After failed `Move-Item`, destination held working `NextTest\.git` + root files; source held empty `.git` shell (0 children) + `app-test` + intact `test`. Moved `app-test` into destination `NextTest`, removed empty leftover `.git` shell only, moved `test` to destination, removed empty source wrapper. Post-move `git rev-parse HEAD` OK on both nested roots.

#### 2) WorkStationPWA

| Field | Value |
| --- | --- |
| From | `C:\Project\WorkStationPWA` |
| To | `C:\Project\archive\2025.07.01 - WorkStationPWA` |
| Method | `[System.IO.Directory]::Move` Access Denied; `Move-Item` again PermissionDenied on `WorkStationPWA\.git` → partial split; reunify + **`robocopy /E /MOVE`** for remaining large/router trees |
| Nested-git attestation | `...\WorkStationPWA\.git` = **True**; `...\WorkStationRouterPWA\workstation-app\.git` = **True**; count = 2 |
| Opaque `.env` | Pre = 0; Post destination scan count = 0 |
| Source absent / dest present | **True** / **True** |
| SSH origin | Still `git@github.com:KenCacciabueOrif/WorkStationRouterPWA.git` (fetch/push) — **path-only; not rewritten** |

**Recovery detail (WorkStationPWA):** Destination had full `.git` + `README.md`; source had empty `.git` shell + `workstation-app` (+ `WorkStationRouterPWA` still at source). Robocopy-moved `workstation-app` into destination, removed empty `.git` shell, robocopy-moved `WorkStationRouterPWA`, removed empty source root. Wrapper non-git siblings already at destination (e.g. `favicon_io(3)`) retained.

### Step 5 — Catalogue

- Updated `catalogue/INDEX.md` rows for `GitTest` and `WorkStationPWA` → Status `archive`, dated labels, current archive paths; What’s next shows remaining Multi-experiment names.
- Updated `catalogue/inventory.md` Notes + nested-path bullets for the two moved wrappers.
- Did **not** upgrade taxonomy / must-preserve labels; did **not** edit must-preserve draft list as move sources.

### Step 6 — ROADMAP

- `program/ROADMAP.md` Multi-experiment Notes: **partial progress** — Cycle 7 moved `GitTest`, `WorkStationPWA` → `archive`; **remaining:** `PWAExemple`, `WorkSpace`.
- Row remains **Primary next → Multi-experiment** / in progress — **not** marked Complete.
- “How the next cycle starts” locks same row / remaining names.

### Skips / substitutions

- None skipped after recovery.
- **Zero** intentional moves of `PWAExemple`, `WorkSpace`, Medium/Early destinations, org repo, or other out-of-map paths.
- No substitute folders invented.

---

## Reverse-move notes (successful rows)

| Forward | Reverse (do not delete payload) |
| --- | --- |
| `C:\Project\GitTest` → `C:\Project\archive\2025.08.08 - GitTest` | `Move-Item -LiteralPath 'C:\Project\archive\2025.08.08 - GitTest' -Destination 'C:\Project\GitTest'` |
| `C:\Project\WorkStationPWA` → `C:\Project\archive\2025.07.01 - WorkStationPWA` | `Move-Item -LiteralPath 'C:\Project\archive\2025.07.01 - WorkStationPWA' -Destination 'C:\Project\WorkStationPWA'` |

If locks recur on reverse, prefer `[System.IO.Directory]::Move` or `robocopy /E /MOVE` after ensuring destination root path is free. Nested `.git` and any opaque `.env` ride with the wrapper; remotes stay unchanged.

---

## Zero-move / safety attestations

- Intentional corpus moves outside approved map: **0**
- Medium/Early verify-only paths: present; **not** re-moved
- `PWAExemple` / `WorkSpace`: still at root
- Secret contents logged: **none** (path/`Test-Path` / counts only)
- Agent `git push` / `git pull`: **none**
- SSH/remote URL rewrite: **none**
- ROADMAP Multi-experiment Complete: **no**

---

## Deviations from plan

1. **Move mechanics:** Plan preferred single atomic `Move-Item` rename. Windows file locks on nested `.git` caused partial child-by-child moves; recovered with reunify + (for WorkStation) `robocopy /E /MOVE`. End-state paths and nested-git counts match the approved map.
2. **Empty leftover `.git` directories** (0 children) removed after reunify — shells left by failed delete, not unique payload.

---

## Status

- **Implementation status:** complete (both approved rows at destinations; docs + ROADMAP partial Notes updated)
- **blocker_type:** none
- **Verification (implementer self-checks):** path presence + nested-git `Test-Path` + env counts + ROADMAP partial — pass pending auditor
