# Prompt betterment notes — Cycle 8 Multi-experiment (remaining subset)

Session: `sessions/2026.09.10-0811/01-prompt-betterment/`  
Role: **Cycle 8 — Multi-experiment remaining subset** (`fs_mutation` expected).  
Roadmap row (orchestrator-locked — **do not re-pick / do not jump Primary next**): **Multi-experiment remaining only** — `PWAExemple`, `WorkSpace`.  
Prior session: `sessions/2026.09.10/` (Cycle 7 complete — `GitTest`, `WorkStationPWA` → archive).  
**Do not** reopen Medium wrappers or Early/simple; **do not** re-propose already-archived Multi-experiment peers as move sources.  
**Pack type:** short **Multi-experiment remaining-subset** Continuity pack — **not** first-batch four-name pack; **not** Medium soft-deferred pack.

## Plain-language meaning of the gates (carry — brief)

| Term | Everyday meaning |
| --- | --- |
| **Plan gate** | After planning, you see a concrete **from → to** list and say yes **before** any move. Continuity / Choose / starting this FAW is **not** that yes. |
| **fs_mutation** | This cycle will move/rename real folders on disk (after plan gate), not only edit docs. |
| **Fail-closed** | If something unexpected appears (worktrees / multi-remote / unclear git roots), we **stop that item** instead of guessing. |
| **Atomic nested git** | Move the whole top-level folder **including** its inner `.git` as one piece — no history rewrite. |
| **Continuity** | Reuse Cycles 2–7 rules (layout, taxonomy, must-preserve, status, secrets, verify, SSH path-only, Windows lock recovery) unless you change them below. |
| **Multi nested-git caution** | These folders may contain **more than one** git repo inside; each stays atomic; research may **defer** a name if roots look unsafe. |
| **SSH-origin path-only** | Move the folder as-is; **do not** change `origin` remote URLs unless you start a dedicated git-strategy cycle. |
| **Taxonomy proposed-ratified** | Folder-type scheme is ready for your sign-off — **not** claimed as final global law without your approval. |
| **Must-preserve draft** | Keep-list is **draft — not auto-locked / for user review** — not silently treated as final. |
| **Windows nested-`.git` lock recovery** | Prefer single move; if Windows locks a nested `.git` mid-move, reunify into the destination and finish with `robocopy /E /MOVE`; remove **only empty** leftover `.git` shells; re-check nested git; log as process note — not invent deletes of real content. |

## Clarifying questions (SHORT remaining-subset pack — answered Choose all)

**Do not re-ask** first-batch Multi-experiment Continuity redesign unless the user wants to change it. Carry those locks.

Each question included plain-language explanation + pros/cons. **Informed consent:** answering commits only to Continuity/scope for research/plan — **not** to executing moves (**plan gate still mandatory and separate**).

---

### Q1 — Which remaining folders this cycle?

**Ask summary:** Prefer PWAExemple when green + WorkSpace fail-closed (default) vs both vs PWAExemple-only vs WorkSpace git-strategy opt-in vs named?

### Q2 — Confirm Continuity still applies?

**Ask summary:** Carry layout / multi nested-git / SSH path-only / opaque .env / taxonomy+must-preserve / 90-day / Windows lock recovery / INDEX honesty? Default A.

---

## Answers

User reply: **Choose all** for Q1–Q2. Disclosed defaults locked. **Plan gate still mandatory** before any moves — Choose all does **not** approve the from→to map.

| Q | Ask summary | Locked decision | Source | Rationale |
| --- | --- | --- | --- | --- |
| 1 | Prefer PWAExemple when green + WorkSpace fail-closed (default) vs both vs PWAExemple-only vs WorkSpace git-strategy opt-in vs named? | **A** — Prefer **`PWAExemple`** when research is green; keep **`WorkSpace`** fail-closed / git-strategy candidate until cleared (do not force-move; do not start dedicated git-strategy map unless research clears hazards and plan explicitly includes it — default remains defer) | `Choose all` | Matches Cycle 7 findings + ROADMAP remaining cue; lower blast radius |
| 2 | Carry layout / multi nested-git / SSH path-only / opaque .env / taxonomy+must-preserve / 90-day / Windows lock recovery / INDEX honesty? Default A. | **A** — Carry Continuity as locked below | `Choose all` | Do not re-litigate Cycles 2–7 Continuity |

**Informed consent note:** Q1–Q2 included plain-language explanation + pros/cons in the ask; user Choose all after that pack — no jargon-explanation debt.

## Continuity (locked — do not re-ask unless user changes)

| Lock | Value |
| --- | --- |
| ROADMAP row | **Multi-experiment remaining** (orchestrator-locked) — same row, not Primary next |
| Remaining candidates only | `PWAExemple`, `WorkSpace` |
| Already moved (do not re-propose) | `GitTest`, `WorkStationPWA` → archive (Cycle 7) |
| Prior rows | Medium wrappers **Complete**; Early/simple **Complete** — do not reopen |
| Mutation class | `fs_mutation` expected; **per-batch plan gate mandatory** (separate from Continuity Choose) |
| Scope (Q1=A) | Prefer **`PWAExemple`** when green; **`WorkSpace`** fail-closed / git-strategy until cleared |
| Layout | archive / paused / active per research status (catalogue taxonomy) |
| Nested git | Atomic intact `.git` trees; multi nested-git caution + fail-closed deferrals |
| Secrets | Opaque `.env` — path presence only; never read/quote |
| Remotes | SSH/origin **path-only** (no rewrite unless user opts into git-strategy) |
| Status heuristic | 90-day Continuity (research confirms from disk) |
| Windows lock recovery | Prefer `Move-Item`; on PermissionDenied/split → reunify + `robocopy /E /MOVE`; empty `.git` shells only; re-attest; log deviation |
| Taxonomy | **proposed-ratified — ready for user sign-off** (not final without explicit approval) |
| Must-preserve | **draft — not auto-locked / for user review** |
| Pending hard blockers | None; do not re-block solely to re-litigate taxonomy/must-preserve |

## Assumptions

- User intent “next cycle” = continue Multi-experiment **remaining** subset, not docs-only and not jump to Special git / Primary next.
- Research will live-check only `PWAExemple` and `WorkSpace` (plus verify already-archived peers stay put).
- Under Q1=A, executable map defaults to `PWAExemple` if green; `WorkSpace` deferred unless research clears hazards — still no force-move and still no silent git-strategy execution this cycle.
- Plan gate remains mandatory and separate from this Continuity Choose.

## Open risks

- `WorkSpace` may remain fail-closed after research (expected under Q1=A); row stays in progress until cleared or dedicated git-strategy.
- Continuity / Choose must not be treated as move approval — orchestrator must still run plan gate.
- Windows nested-`.git` locks may recur on `PWAExemple`; recovery Continuity must be followed, not invent unsafe deletes.
- If `PWAExemple` itself fail-closes, executable subset may shrink to zero this cycle — document and keep row in progress (process pass / fail-closed), do not invent substitute sources.

## Self-improvement backlog (if any)

- None for this phase (informed consent pack explained before Choose all).

## Key alignment changes (raw → refined)

- Raw: `/full-agent-workflow do next cycle`
- Refined: Cycle 8 Multi-experiment **remaining only** (`PWAExemple`, `WorkSpace`); Q1–Q2 = A via Choose all; plan gate separate; no Medium/Early reopen; no re-move of `GitTest` / `WorkStationPWA`.

## Status

**`complete`** — refined prompt ready for researcher handoff.
