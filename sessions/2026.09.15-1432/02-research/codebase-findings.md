# Codebase findings — Cycle 23 (WorkSpace / Continuity X / #4)

**Session:** `sessions/2026.09.15-1432/02-research/`  
**Probe date:** 2026-09-15  
**Method:** Shell `Test-Path` + GfW-preferred remotes/worktree/porcelain (PATH default was MSYS `git.exe` — counts match Cycle 20 baseline); Read of strategy docs + ROADMAP + catalogue.

---

## Must-read paths

| Path | Why it matters |
| --- | --- |
| `program/ROADMAP.md` | Suggested order; Primary next → Multi-experiment **Remaining: WorkSpace only**; Next FAW lock hint after Cycle 20 |
| `program/git-strategy-workspace-hazards.md` | Continuity X baseline; clearance #1–#6; #4 still **DRAFT written / approval pending** |
| `program/git-strategy-tna-parent-surgery.md` | Full parent-surgery **policy already written** Cycle 20; defines written vs approved; held nest table |
| `catalogue/INDEX.md` | WorkSpace still at `C:\Project\WorkSpace`; nested **4**; OS-IA archive row verify-only |
| `catalogue/inventory.md` | Multi-remote **Cleared**; Cycle 20 surgery DRAFT noted; row not Complete |
| `sessions/2026.09.15-1117/` (Cycle 20) | Created surgery md; #4 DRAFT; Next FAW = approve then nest gate |
| `sessions/2026.09.15-1340/` (Cycle 22) | Dashboard done for now; Next FAW must research-justify — never inherit dashboard |
| `sessions/2026.09.15-1432/01-prompt-betterment/` | Continuity Q1–Q5 all **A**; material #4 or escalate |

---

## Live path truth (disk vs INDEX)

| Unit | Expected path | `Test-Path` | Verdict |
| --- | --- | --- | --- |
| WorkSpace wrapper | `C:\Project\WorkSpace` | **True** | INDEX root path correct — **verify-only** (not already under archive) |
| TNA envelope | `C:\Project\WorkSpace\TestNewWorkspaceAgent` | **True** | Only child under WorkSpace root |
| hermes-agent | `…\TestNewWorkspaceAgent\hermes-agent` | **True** | Live nest |
| orchestrateur | `…\Projects\Project Atelier IA\Projet Adrien\orchestrateur` | **True** | Live nest |
| WorkshopOrif | `…\Projects\Project Atelier IA\Workshop\WorkshopOrif` | **True** | Live nest |
| OS-IA | `C:\Project\archive\2026.09.15 - OS-IA` | **True** | Archived Cycle 19 — **verify-only**; never re-propose as move source |

**INDEX drift:** none on presence — WorkSpace still at root; nests still under TNA; OS-IA archive row matches disk. **Never** propose re-move of OS-IA / Appendix A / Medium / Early / archived Multi peers.

---

## Live hazard re-probe vs Cycle 20 / hazards artifact

| Field | Cycle 20 / artifact | Live Cycle 23 | Material delta? |
| --- | --- | --- | --- |
| Nested under WorkSpace | **4** (TNA + 3 in-TNA) | **4** | **No** |
| Nest model | Ignored clones; no `.gitmodules` | Confirmed (`check-ignore` hits; `gitmodules=False`) | **No** |
| Live multi-remote | CLEARED | Sole `origin` HTTPS on TNA + all 3 nests; **no `cada`** | **No** |
| Linked worktrees | 1 each (expected) | 1 each on nest paths | **No** |
| Dirty TNA porcelain | ~2307 NO_AUTO_COMMIT | **2307** | **No** |
| Nest porcelain (disclose) | hermes 56 / orch 60 / Workshop 119 | **56 / 60 / 119** | **No** |
| Clearance #4 | DRAFT written / approval pending | Still DRAFT (file unchanged status) | Status still pending — see advance |
| Whole-tree clearance | **NO** | Still **NO** | **No** |
| Parent-surgery md | Full procedure written | Exists; complete | **Re-write = no delta** |

**Anti-loop signal:** Hazard inventory is **stable**. Re-attesting classification or rewriting `git-strategy-tna-parent-surgery.md` procedure sections = **theater**. Only remaining #4 half is **Approved** for a **named** nest map (or escalate).

---

## Nest extract candidates (held — not execute)

| Nest | Porcelain | Remotes | Worktrees | Ignore | Prefer as first map? |
| --- | --- | --- | --- | --- | --- |
| **hermes-agent** | 56 | sole `origin` (NousResearch) | 1 main | `.gitignore:4` | **Yes** — shallowest path under TNA; remote already cleared Cycle 15; lowest nest dirt |
| orchestrateur | 60 | sole `origin` | 1 master | line 2 | Secondary |
| WorkshopOrif | 119 | sole `origin` | 1 feature branch | Workshop/ line 3 | Tertiary (dirtier WT; feature branch) |

**Suggested named map (document for plan gate — do not invent execute):**

| Field | Held default |
| --- | --- |
| Source | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` |
| Destination (default archive) | `C:\Project\archive\2026.09.15 - hermes-agent` |
| Remotes | Path-only (no set-url) |
| Parent TNA | Disclose dirty **2307**; **NO_AUTO_COMMIT** |
| Out of map | TNA envelope; WorkSpace whole-tree; other nests; OS-IA; Appendix A |

Absolute-path consumer scan under dirty TNA remains an **open pre-execute** requirement (surgery md § Preflight #8) — do not invent consumer lists in research.

---

## ROADMAP row comparison (workstream justification evidence)

| Row / thread | Status | Why not this cycle’s primary |
| --- | --- | --- |
| **Multi-experiment / WorkSpace** | In progress; Remaining WorkSpace only | **Program Primary next**; Continuity X / #4 approval is the unfinished clearance half |
| Special git (`WebCatalogue`, `HTTP Battles`) | Later in Suggested order | Jumping Primary next **forbidden** while WorkSpace remains |
| Git-strategy planning (hard gate) | Reminder before Obsidian / ProjetOrif | Continuity X **is** the live git-strategy thread for WorkSpace; a separate “planning” cycle that skips #4 would be parallel theater |
| ProjetOrif | High complexity; after git-strategy | Blocked by hard gate; WorkSpace uncleared ≠ free to start |
| Obsidian | Worktree-critical; after git-strategy | Same hard gate |
| Hygiene (root package.*, Docker, `.vscode`) | Separate mini-batch | Lower programme priority than Primary-next lock |
| Dashboard / catalogue 20–22 | Cycle 22 **done for now** | **Forbidden** as default/inherited topic (user Continuity + Cycle 22 Next FAW) |
| Medium / Early / archived Multi peers | Complete / verify-only | Never reopen as move sources |

---

## Catalogue honesty (already accurate)

- Inventory multi-remote line already **Cleared** — no Continuity A honesty delta required.
- #4 still correctly described as DRAFT / approval pending — material flip only after plan-gate yes for named map.

---

## Publish / push preflight

**N/A for research goal** (no org-repo sync AC in Continuity research stage). Continuity Q5=A applies only if implement publishes — dual mid+final git-manager later; not a research blocker.
