# Adaptive multi-cycle roadmap

**Program:** organise `C:\Project` across sequential FAW cycles.  
**Cycle 0:** docs/index only — **no move steps**.  
**Cycle 1:** docs follow-ups — **complete** this session (`sessions/2026.09.09-1009/`); taxonomy **proposed-ratified — ready for user sign-off**; inventory deepened; must-preserve draft added. Cycle 1 did **not** execute moves.  
**Charter:** [`CHARTER.md`](CHARTER.md) · **Index:** [`../catalogue/INDEX.md`](../catalogue/INDEX.md)

## Principles

1. **Adaptive count** — no fixed N; add, split, or skip cycles as inventory and approvals evolve.
2. **Slice by top-level folder** under `C:\Project` (sub-batches allowed inside a complex top-level).
3. **Move-capable cycle shape:** classify → propose batch map → **user approves** → agent executes (deps/secrets opaque) → update `catalogue/INDEX.md`.
4. **Fail-closed** on must-preserve and unclear git strategy.
5. **Git roots are atomic** — move intact `.git` trees; no history rewrite / `filter-repo` unless a cycle explicitly chooses it.

## Hard gate — git-strategy planning

**Reminder (not the primary next row):** run a dedicated **multi-repo git strategy** FAW cycle **before** any cycle that relocates git roots, especially before:

- `Obsidian` (linked worktrees)
- `ProjetOrif` multi-root moves
- Any worktree relocation
- Any batch that changes remote / agent-push assumptions

That planning thread should cover: remotes HTTPS vs SSH, atomic moves, nested/empty parents, worktrees, absolute-path configs, agent vs user push. Default outcome: move intact `.git` trees.

## Suggested order

Adjust after taxonomy / must-preserve review. Priority is a guide, not a contract.

| Priority | Top-level / thread | Notes |
| --- | --- | --- |
| Protect | `2026.09.09 - Organisation` | Default-preserve; never casual batch-move |
| Docs follow-ups | Cycle 1 | **Done** — taxonomy proposed-ratified (pending user sign-off); inventory + must-preserve draft |
| Early / simple | `PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest` | **Complete** — Cycle 2 (`PostManResponses`, `PlayTestTristan` → `archive`; `ZedTest` → `paused`); Cycle 3 (`IA`, `AngularTest`, `epsic` → `archive`) |
| Medium wrappers | `NextTest`, `Simpl`, `Simpl_Next`, `TestRyan`, `ReactRouterTest`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining` | **Complete** — Cycle 4 (`sessions/2026.09.09-1535/`): `TestRyan`, `ReactRouterTest`, `Simpl` → `archive`. Cycle 5 (`sessions/2026.09.09-1554/`): `NextTest`, `Simpl_Next`, `PWAExempleTristan` → `archive`. Cycle 6 (`sessions/2026.09.09-1612/`): `NextPWATraining` → `archive`; `CursorMobileWorkspace` → `paused`. Nested git atomic; `.env` opaque (unread) |
| **Primary next → Multi-experiment** | `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace` | **In progress (partial / nearly complete)** — Cycle 7 (`sessions/2026.09.10/`): moved `GitTest`, `WorkStationPWA` → `archive`. Cycle 8 (`sessions/2026.09.10-0811/`): moved `PWAExemple` → `archive`. Cycle 9 (`sessions/2026.09.10-0848/`): **researched+deferred** `WorkSpace` (`docs_only`; hazards not cleared — multi-remote; `_backups`/`_quarantine` extra roots; live **7** nested vs inventory undercount; XL; must-preserve draft Medium caution). Cycle 10 (`sessions/2026.09.10-0907/`): **docs_only hazard remediation** — classification + safe relocation/isolation rules in [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md); zero corpus moves; `_backups`/`_quarantine` isolation deferred (future plan gate only); whole-tree still fail-closed. Cycle 11–13: **docs_only continue-strategy** re-probe (**no material delta**; clearance still **NO**; Appendix A unused). Cycle 14 (`sessions/2026.09.11/`): Continuity **B** Appendix A **`fs_mutation` executed** — `_backups` → `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_backups`; `_quarantine` → `C:\Project\archive\hygiene\2026.09.11 - WorkSpace-_quarantine`; nested under WorkSpace **7→5**; live primaries kept; remotes path-only unchanged; parent TNA dirty WT disclosed (**no** auto-commit); whole WorkSpace still at root; whole-tree clearance still **NO**. Cycle 15 (`sessions/2026.09.11-0859/`): Continuity **Q1=B** Option A **`fs_mutation` executed** — live hermes `git remote remove cada` (wrong-target TNA URL); sole **`origin`** (`NousResearch/hermes-agent`) kept; **zero** corpus path moves; live multi-remote **cleared**; nested still **5**; hermes + TNA dirty WT disclosed (**NO_AUTO_COMMIT** / Q3=A). Cycle 16 (`sessions/2026.09.11-1038/`): Continuity **Q1=A** **`docs_only`** re-probe — **no material hazard delta** vs Cycle 15; strategy attestation + inventory multi-remote honesty (**Cleared**; confirmed); zero corpus moves / zero remote-config; row still **Remaining: `WorkSpace` only**. Cycle 18 (`sessions/2026.09.15/`): Continuity **Q1=B→E** → research **no new** narrow gated advance → **`escalate_break_loop`**; user locked next Continuity **X** (dedicated XL / whole-tree **git-strategy**; new cycle + plan gate before any path mutation). Cycle 19 (`sessions/2026.09.15-1014/`): Continuity **X** plan gate **D+M** (archive default) — extended [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md) with fate matrix + whole-tree clearance criteria; **OS-IA** intact → `C:\Project\archive\2026.09.15 - OS-IA` (remotes path-only; NO_AUTO_COMMIT); WorkSpace remains at root with **TNA envelope** (live nested under WorkSpace **5→4**); whole-tree clearance still **NO**. Cycle 20 (`sessions/2026.09.15-1117/`): Continuity **X** **`docs_only`** — created [`git-strategy-tna-parent-surgery.md`](git-strategy-tna-parent-surgery.md); clearance **#4** → **DRAFT written (Cycle 20) / approval pending**; zero nest / TNA / WorkSpace moves; whole-tree clearance still **NO**. Cycle 23 (`sessions/2026.09.15-1432/`): Continuity **X** plan-gate **A** **`docs_only`** — clearance **#4** → **approved-for-named-map** (`hermes-agent` → `C:\Project\archive\2026.09.15 - hermes-agent`); nest execute **held**; **A+E reserved** (not declined; dirty TNA ~2300 absolute-path consumers); nested still **4**; hermes still under TNA; whole-tree still **NO**. **Remaining:** `WorkSpace` only (TNA + nests; fail-closed / git-strategy; do **not** force-move whole tree). Still **per-batch approval**; **not** Complete; do **not** jump Primary next / Special git |
| Special git | `WebCatalogue`, `HTTP Battles` | Top-level git; empty-parent classify |
| **Git-strategy planning** | Dedicated FAW cycle | **Hard gate** — insert **before** Obsidian / ProjetOrif multi-root / worktree moves |
| High complexity | `ProjetOrif` | May split into sub-cycles **after** git-strategy |
| Worktree-critical | `Obsidian` | **After** git-strategy only |
| Hygiene | Root `package.*`, Docker, `node_modules`, `.vscode` | Separate approved mini-batch |

## Approval gate (every move batch)

```
propose map → USER APPROVES → execute → update INDEX
```

No agent-executed move without explicit per-batch approval.

## How the next cycle starts

1. Pending user gates (when still open): taxonomy final sign-off and/or [`../catalogue/must-preserve.md`](../catalogue/must-preserve.md) draft review — Continuity from Early/simple and Medium may already waive these for later move rows; do not re-block solely to re-litigate them.
2. **Primary next → Multi-experiment** — lock **same row / remaining name:** `WorkSpace` only (still fail-closed for whole-tree). Cycle 9 deferred; Cycle 10 wrote [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md); Cycle 11–13 docs_only continue-strategy (**no material delta**; Appendix A unused). Cycle 14 (`sessions/2026.09.11/`): Continuity **B** Appendix A isolation **executed** (`_backups`/`_quarantine` → `archive\hygiene\`; nested **7→5**); whole-tree clearance still **NO**. Cycle 15 (`sessions/2026.09.11-0859/`): live hermes multi-remote **cleared** (Option A remove `cada`; sole `origin`). Cycle 16 (`sessions/2026.09.11-1038/`): Continuity **Q1=A** `docs_only` re-probe (**no material hazard delta**; inventory Cleared confirmed). Cycle 18 (`sessions/2026.09.15/`): anti-loop **escalate_break_loop** (no new narrow gated advance); user Continuity **X**. Cycle 19 (`sessions/2026.09.15-1014/`): Continuity **X** **D+M** — fate matrix + clearance criteria in hazard artifact; **OS-IA** → `C:\Project\archive\2026.09.15 - OS-IA`; WorkSpace remains (TNA envelope; nested under WorkSpace **5→4**); OS-IA move alone **never** Completes the row. Cycle 20 (`sessions/2026.09.15-1117/`): Continuity **X** parent-surgery **DRAFT** ([`git-strategy-tna-parent-surgery.md`](git-strategy-tna-parent-surgery.md); hazards #4 **DRAFT written / approval pending**); zero nest FS; docs alone **never** Completes the row. Cycle 23 (`sessions/2026.09.15-1432/`): Continuity **X** plan-gate **A** — #4 **approved-for-named-map** (hermes-agent → `C:\Project\archive\2026.09.15 - hermes-agent`); nest execute **held**; **A+E reserved** (not declined); nested still **4**; hermes still under TNA; #4 approved-for-map alone **never** Completes the row. **Next FAW lock hint:** keep **`WorkSpace` only** (TNA + hermes / orchestrateur / WorkshopOrif) — continue Continuity X clearance / keep-at-root; hermes nest extract still **pending** dedicated execute / **A+E** gate ([`git-strategy-tna-parent-surgery.md`](git-strategy-tna-parent-surgery.md) + [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md)); **do not** soft-deferred force-finalize / silent whole-tree archive; **do not** Continuity A docs_only re-attest theater; **do not** treat Appendix A, Cycle 15 remote-config, Cycle 16 docs honesty, Cycle 18 escalate, Cycle 19 OS-IA split, Cycle 20 surgery draft, or Cycle 23 #4 approved-for-map as Multi-experiment Complete. Do **not** reopen Medium / Early/simple or re-propose archived `PWAExemple` / `OS-IA`. Do **not** mark Multi-experiment Complete while `WorkSpace` remains. Do **not** jump Primary next / Special git while it remains.
3. New FAW session: `/full-agent-workflow` (or Continuity next) → orchestrator locks ROADMAP **Primary next → Multi-experiment** with remaining **`WorkSpace` only** + Continuity from hazard artifact; new `sessions/yyyy.mm.dd…`.

## Cycle boundary notes

- Cycle 0/1 schedule and document work; they do **not** execute corpus moves.
- Do not start a move-capable cycle inside the same FAW without a new session after user review/approval.
- **Partial multi-batch:** After a subset pass, update this file’s Notes + “How the next cycle starts” with remaining names before claiming the row Complete.
