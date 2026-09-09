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
| **Primary next → Early / simple** | `PostManResponses`, `IA`, `AngularTest`, `PlayTestTristan`, `epsic`, `ZedTest` | First move-prep / simple batch **after per-batch approval**; lowest git-strategy coupling |
| Medium wrappers | `NextTest`, `Simpl`, `Simpl_Next`, `TestRyan`, `ReactRouterTest`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining` | One nested git; `.env` opaque on NextPWA |
| Multi-experiment | `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace` | Multiple nested roots; sub-batches OK |
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

1. User reviews Cycle 1 artefacts: sign off taxonomy (or request edits) and review [`../catalogue/must-preserve.md`](../catalogue/must-preserve.md) draft.
2. **Prefer** choosing an **Early/simple** subset for the first approved move batch — or run **Git-strategy** first if the next target needs it.
3. New FAW session: `/full-agent-workflow` with that goal → new `sessions/yyyy.mm.dd…`.

## Cycle boundary notes

- Cycle 0/1 schedule and document work; they do **not** execute corpus moves.
- Do not start a move-capable cycle inside the same FAW without a new session after user review/approval.
