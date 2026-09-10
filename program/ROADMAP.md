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
| **Primary next → Multi-experiment** | `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace` | **In progress (partial / nearly complete)** — Cycle 7 (`sessions/2026.09.10/`): moved `GitTest`, `WorkStationPWA` → `archive`. Cycle 8 (`sessions/2026.09.10-0811/`): moved `PWAExemple` → `archive`. Cycle 9 (`sessions/2026.09.10-0848/`): **researched+deferred** `WorkSpace` (`docs_only`; hazards not cleared — multi-remote; `_backups`/`_quarantine` extra roots; live **7** nested vs inventory undercount; XL; must-preserve draft Medium caution). Cycle 10 (`sessions/2026.09.10-0907/`): **docs_only hazard remediation** — classification + safe relocation/isolation rules in [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md); zero corpus moves; `_backups`/`_quarantine` isolation deferred (future plan gate only); whole-tree still fail-closed. Cycle 11 (`sessions/2026.09.10-1047/`): **docs_only continue-strategy** — live re-probe attestation on [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md) (**no material delta**; clearance still **NO**; Appendix A unused); zero corpus moves. Cycle 12 (`sessions/2026.09.10-1247/`): **docs_only continue-strategy** — re-probe attestation on [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md) (**no material delta** vs Cycle 11; clearance still **NO**; Appendix A unused); zero corpus moves. Cycle 13 (`sessions/2026.09.10-1630/`): **docs_only continue-strategy** — re-probe attestation on [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md) (**no material delta** vs Cycle 12; clearance still **NO**; Appendix A unused); zero corpus moves. **Remaining:** `WorkSpace` only (fail-closed / git-strategy; do **not** force-move). Still **per-batch approval**; **not** Complete |
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
2. **Primary next → Multi-experiment** — lock **same row / remaining name:** `WorkSpace` only (or dedicated git-strategy / optional **scoped** `_backups`/`_quarantine` isolation under a **separate plan gate** — still fail-closed for whole-tree). Cycle 9 (`sessions/2026.09.10-0848/`) re-probed and **deferred**. Cycle 10 (`sessions/2026.09.10-0907/`) wrote durable remediation rules ([`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md)); hazards classified not cleared for whole-tree; Continuity Choose ≠ move approval. Cycle 11 (`sessions/2026.09.10-1047/`): **docs_only continue-strategy** re-probe on that artifact (**no material delta**; clearance still **NO**; Appendix A unused). Cycle 12 (`sessions/2026.09.10-1247/`): **docs_only continue-strategy** re-probe on that artifact (**no material delta** vs Cycle 11; clearance still **NO**; Appendix A unused). Cycle 13 (`sessions/2026.09.10-1630/`): **docs_only continue-strategy** re-probe on that artifact (**no material delta** vs Cycle 12; clearance still **NO**; Appendix A unused). **Next FAW lock hint:** **continue strategy** from [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md) **or** explicit Continuity **B** + separate plan gate for Appendix A — **do not** soft-deferred force-finalize / force-move the XL tree; **do not** re-default Cycle 9 pure defer as primary while the durable artifact exists. Do **not** reopen Medium / Early/simple or re-propose archived `PWAExemple`. Do **not** mark Multi-experiment Complete while `WorkSpace` remains. Do **not** jump Primary next / Special git while it remains.
3. New FAW session: `/full-agent-workflow` (or “next cycle”) → orchestrator locks ROADMAP **Primary next → Multi-experiment** with remaining **`WorkSpace` only**; new `sessions/yyyy.mm.dd…`.

## Cycle boundary notes

- Cycle 0/1 schedule and document work; they do **not** execute corpus moves.
- Do not start a move-capable cycle inside the same FAW without a new session after user review/approval.
- **Partial multi-batch:** After a subset pass, update this file’s Notes + “How the next cycle starts” with remaining names before claiming the row Complete.
