# Codebase findings — Cycle 20 (TNA parent-surgery / Continuity X #4)

**Session:** `sessions/2026.09.15-1117/02-research/`  
**Probe date:** 2026-09-15  
**Probe method:** Shell `Test-Path` + recursive `.git` directory discovery under `C:\Project\WorkSpace`; per-root `git remote -v`, `git worktree list`, `git status --porcelain` (MSYS git `C:\msys64\usr\bin\git.exe`); TNA `.gitignore` / `check-ignore` / no `.gitmodules`.  
**Locks:** Continuity **Q1=A** parent-surgery docs; **`docs_only`** STAGE 1; WorkSpace / TNA only; **Q3=A** dirty disclose **NO_AUTO_COMMIT**.

---

## Path truth (INDEX / disk)

| Path | Disk | INDEX / inventory | Verdict |
| --- | --- | --- | --- |
| `C:\Project\WorkSpace` | **Exists** (sole child: `TestNewWorkspaceAgent`) | Root path for WorkSpace | **verify-only** — still at root; never re-move |
| `C:\Project\WorkSpace\TestNewWorkspaceAgent` | **Exists** (git root) | Implied TNA envelope under WorkSpace | Live |
| `C:\Project\WorkSpace\OS-IA` | **Absent** | — | Correct post–Cycle 19 |
| `C:\Project\archive\2026.09.15 - OS-IA` | **Exists** (git root) | INDEX archive row | **verify-only** — do **not** re-propose as move source |
| Appendix A hygiene parents | Not re-probed as live sources | Archived Cycle 14 | **verify-only** — never Appendix A re-propose |

`catalogue/INDEX.md` WorkSpace row already states nested **4** live after Cycle 19 OS-IA split — **matches** live probe. Inventory WorkSpace notes align (Remaining WorkSpace only; clearance_whole_tree **NO**).

---

## Live nested `.git` inventory (WorkSpace / TNA)

**Count under `C:\Project\WorkSpace`:** **4** (all under TNA). No file-form `.git` (no submodule gitdir pointers) found.

| # | Unit | Absolute path | Envelope | Remotes | Worktrees | Porcelain lines |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **TNA** (`TestNewWorkspaceAgent`) | `C:\Project\WorkSpace\TestNewWorkspaceAgent` | Parent envelope | sole `origin` HTTPS `KenCacciabueOrif/TestNewWorkspaceAgent` | **1** main @ `self-improvement-infra` | **2307** |
| 2 | **hermes-agent** | `…\TestNewWorkspaceAgent\hermes-agent` | In-TNA nest | sole `origin` HTTPS `NousResearch/hermes-agent` | **1** main | **56** |
| 3 | **orchestrateur** | `…\Projects\Project Atelier IA\Projet Adrien\orchestrateur` | In-TNA nest | sole `origin` HTTPS `AdWav/orchestrateur` | **1** master | **60** |
| 4 | **WorkshopOrif** | `…\Projects\Project Atelier IA\Workshop\WorkshopOrif` | In-TNA nest | sole `origin` HTTPS `C0D3X-25/WorkshopOrif` | **1** `feature/formation-level-courses` | **119** |

**Verify-only (archived Continuity X peer):**

| Unit | Path | Remotes | Worktrees | Porcelain | Note |
| --- | --- | --- | --- | --- | --- |
| OS-IA | `C:\Project\archive\2026.09.15 - OS-IA` | sole `origin` HTTPS `KenCacciabueOrif/Projet-OS-IA` | **1** master | **921** | Do **not** re-propose; not in Cycle 20 map |

**WorkSpace top-level:** only `TestNewWorkspaceAgent` remains (OS-IA gone). Non-git wrapper `WorkSpace` still holds the TNA envelope only.

**Live multi-remote:** still **CLEARED** on probed nests (no `cada`). Linked worktrees: **none unexpected** (1 each).

---

## Dirty WT note (Q3=A)

| Root | Porcelain | vs Cycle 19 research baseline |
| --- | --- | --- |
| TNA | **2307** | **Exact match** (~2307 baseline) |
| hermes-agent | 56 | Match |
| orchestrateur | 60 | Match |
| WorkshopOrif | 119 | Match |
| OS-IA (archive) | 921 | Match (verify-only) |

**Policy:** disclose only — **NO_AUTO_COMMIT** / no stash-as-cleanup of TNA or nests. Implementer (future gated cycle) must live-recount before any nest move; dirty counts are snapshots.

---

## Parent ↔ nest relationship (material for surgery design)

TNA intentionally treats nests as **ignored nested clones**, **not** submodules:

- **No** `.gitmodules` at TNA root.
- `git submodule status` on nest paths → pathspec unknown (not registered).
- `git ls-files` on nest paths → empty (not tracked).
- `git check-ignore -v` hits TNA `.gitignore`:
  - `hermes-agent` ← line 4
  - `Projects/Project Atelier IA/Projet Adrien/orchestrateur/` ← line 2
  - `Projects/Project Atelier IA/Workshop/` (covers WorkshopOrif) ← line 3

Header comment in `.gitignore`: “Nested git repositories (cloned projects — tracked separately)”.

**Implication for parent-surgery:** extracting a nest is primarily an **OS-level intact relocate** of an independent git root. Parent does **not** need submodule `deinit` / `.git/modules` surgery. Parent tracked index is **unlikely** to show nest deletion as a staged change (ignored). Residual parent work is: empty directory cleanup, optional `.gitignore` hygiene, inventory of **non-git** absolute path references (scripts, IDE, docs) under dirty TNA, and honest disclosure that TNA remains dirty (**NO_AUTO_COMMIT**).

---

## Clearance criterion #4 — current gap

From `program/git-strategy-workspace-hazards.md` Continuity X:

> **4.** Parent-surgery policy for dirty TNA is **written and approved** if any in-TNA nest moves are in map.

**What exists today:** one fate-matrix note (“Inner nest extract needs dedicated parent-surgery plan”) + the criterion line itself. **No** procedure, preflight checklist, NO_AUTO_COMMIT parent rules, approval definition, fail-closed conditions, or per-nest map template.

**What must be written to flip “policy written” (docs):** see research-brief. **“Approved”** remains a **later plan gate** — Continuity Q1=A / STAGE 1 docs ≠ approval to execute nest FS.

---

## Prior art in-repo (must-read)

| Path | Why it matters |
| --- | --- |
| `program/git-strategy-workspace-hazards.md` | Continuity X fate + clearance #1–#6; safe relocation rules; OS-IA-first done; #4 stub |
| `sessions/2026.09.15-1014/02-research/*` | Cycle 19 nested 5 map; deferred #3–#5 extract pending parent plan |
| `sessions/2026.09.15-1014/03-plan/plan.md` | Explicitly kept nest extract **out of** OS-IA held map |
| `catalogue/INDEX.md` / `inventory.md` | WorkSpace nested **4**; OS-IA archive row; row not Complete |
| `program/ROADMAP.md` | Primary next Multi-experiment / WorkSpace only |
| TNA `.gitignore` | Authoritative nest ignore list (surgery must not invent submodule workflow) |

---

## Forbidden re-proposals (confirm)

- Appendix A same parents — **out**
- Medium / Early / `PWAExemple` / `GitTest` / `WorkStationPWA` — **out**
- OS-IA reverse or re-archive — **out** (verify-only)
- Silent whole-tree archive / Multi-experiment Complete / Primary next — **out**
- Nest or TNA envelope move this STAGE — **out** (`docs_only`)

---

## concrete_advance_candidate (codebase view)

**`parent-surgery docs`** — material #4 content is **absent** beyond a stub; live evidence (ignored nests, dirty 2307, 3 extractable nests) is enough to draft a real policy. **Not** empty Continuity A re-attest. Escalate only if planner cannot encode material procedure (unexpected).
