# Prompt betterment notes — Cycle 9 Multi-experiment (`WorkSpace` only)

Session: `sessions/2026.09.10-0848/01-prompt-betterment/`  
Role: **Cycle 9 — Multi-experiment WorkSpace-only** (fail-closed / git-strategy candidate).  
Roadmap row (orchestrator-locked — **do not re-pick / do not jump Primary next / do not mark Complete**): **Multi-experiment remaining: `WorkSpace` only**.  
Prior session: `sessions/2026.09.10-0811/` (Cycle 8 — `PWAExemple` → archive; `WorkSpace` left fail-closed).  
**Do not** reopen Medium wrappers or Early/simple; **do not** re-propose archived Multi-experiment peers (`PWAExemple`, `GitTest`, `WorkStationPWA`) as move sources.  
**Pack type:** short **WorkSpace-only Continuity pack** — **not** Medium soft-deferred finalize-by-default.

## Plain-language meaning of the gates (carry — brief)

| Term | Everyday meaning |
| --- | --- |
| **Plan gate** | After planning, you see a concrete **from → to** list (if any) and say yes **before** any move. Continuity / Choose / starting this FAW is **not** that yes. |
| **fs_mutation** | A plan that moves/renames/deletes real corpus folders on disk (after plan gate). |
| **docs_only** | Docs / INDEX / ROADMAP / session notes only — **zero** corpus folder moves. |
| **Fail-closed** | If hazards are unclear (worktrees / multi-remote / unexpected git roots / locks), we **stop and defer** instead of guessing a move. |
| **Atomic nested git** | Treat each nested `.git` tree as one piece — move intact or not at all; no history rewrite. |
| **Continuity** | Reuse Cycles 2–8 rules unless changed below. |
| **SSH-origin path-only** | Move/relocate path as-is; **do not** rewrite `origin` URLs unless a dedicated git-strategy plan says so. |
| **Dedicated git-strategy** | Planning/docs about remotes, worktrees, agent vs user push — **not** a silent force-move. |
| **Taxonomy proposed-ratified** | Ready for user sign-off — **not** final without explicit approval. |
| **Must-preserve draft** | **draft — not auto-locked / for user review**. |

## Clarifying questions (SHORT WorkSpace-only pack — answered)

Each question included plain-language explanation + pros/cons. **Informed consent:** answering commits only to Continuity/path for research/plan — **not** to executing moves (**plan gate still mandatory and separate** if any `fs_mutation` is proposed).

### Q1 — Path for `WorkSpace` this cycle?

**Ask summary:** Research hazards then defer unless cleared (default A) vs opt into dedicated git-strategy planning (B)?

### Q2 — Confirm Continuity still applies?

**Ask summary:** Carry layout / atomic nested-git / SSH path-only / opaque .env / taxonomy+must-preserve wording / 90-day / Windows lock recovery / INDEX honesty / never force-move / never Complete while WorkSpace remains? Default A.

---

## Answers

User reply (raw): **yes**  
Interpreted as accepting disclosed Continuity defaults (equivalent to **Choose all**). Disclosed defaults locked. **Plan gate still mandatory** before any moves — Continuity yes does **not** approve a from→to map. **No dedicated git-strategy** this cycle (user did not choose B).

| Q | Ask summary | Locked decision | Source | Rationale |
| --- | --- | --- | --- | --- |
| 1 | Research hazards then defer unless cleared (default A) vs dedicated git-strategy (B)? | **A** — Research `WorkSpace` hazards; **finalize/move only if clearly cleared**; otherwise fail-closed defer. **No force-move.** No dedicated git-strategy map this cycle. | `Choose` / defaults (raw: “yes”) | Agent-owned WorkSpace-only default; reversible docs prefer over irreversible FS |
| 2 | Carry Continuity (layout / atomic nested-git / SSH path-only / opaque .env / taxonomy+must-preserve / 90-day / Windows lock recovery / INDEX honesty / never force-move / never Complete while WorkSpace remains)? Default A. | **A** — Carry Continuity as locked below | `Choose` / defaults (raw: “yes”) | Do not re-litigate Cycles 2–8 Continuity |

**Informed consent note:** Q1–Q2 included plain-language explanation + pros/cons in the ask before the user replied “yes”; no jargon-explanation debt.

## Continuity (locked — do not re-ask unless user changes)

| Lock | Value |
| --- | --- |
| ROADMAP row | **Multi-experiment remaining `WorkSpace` only** (orchestrator-locked) — same row; **not** Primary next; **not** Complete while it remains |
| Remaining candidate only | `WorkSpace` |
| Already moved (do not re-propose) | `GitTest`, `WorkStationPWA` (Cycle 7); `PWAExemple` (Cycle 8) → archive |
| Prior rows | Medium wrappers **Complete**; Early/simple **Complete** — do not reopen |
| Path (Q1=A) | Research hazards → defer unless cleared; **never force-move**; no dedicated git-strategy this cycle |
| Mutation class | Likely **`docs_only` defer** unless research clearly clears hazards; **`fs_mutation` only** if cleared **and** separate plan gate approves a map |
| Layout | archive / paused / active per research status (catalogue taxonomy) |
| Nested git | Atomic intact `.git` trees; fail-closed on worktrees / multi-remote / unexpected roots |
| Secrets | Opaque `.env` — path presence only; never read/quote |
| Remotes | SSH/origin **path-only** (no rewrite) |
| Status heuristic | 90-day Continuity (research confirms from disk if classifying) |
| Windows lock recovery | Prefer single move; on PermissionDenied/split → reunify + `robocopy /E /MOVE`; empty `.git` shells only; re-attest; log deviation |
| Taxonomy | **proposed-ratified — ready for user sign-off** (not final without explicit approval) |
| Must-preserve | **draft — not auto-locked / for user review** |
| INDEX honesty | Document deferrals and hazards; do not claim moves that did not happen |
| Pending hard blockers | None; do not re-block solely to re-litigate taxonomy/must-preserve |

## Assumptions

- User “yes” = accept disclosed defaults Q1=A + Q2=A (not Medium finalize-by-default; not git-strategy B).
- User intent “next cycle” = continue Multi-experiment with **`WorkSpace` only**.
- Research live-checks `WorkSpace` hazards only (plus verify archived peers stay put).
- Continuity / yes ≠ move approval; plan gate remains mandatory if any corpus move map is proposed.
- If hazards uncleared → process pass with documented defer; row stays in progress.

## Open risks

- Hazards may remain uncleared → expected fail-closed defer; do not invent substitute sources or jump Primary next.
- Treating Continuity yes as move approval would be a process fail.
- Marking Multi-experiment Complete while `WorkSpace` remains would be a process fail.
- Windows nested-`.git` locks may appear if a cleared move is later approved — recovery Continuity must be followed.

## Self-improvement backlog (if any)

- None for this phase (informed consent pack explained before “yes”).

## Key alignment changes (raw → refined)

- Raw: `/full-agent-workflow do next cycle` + Continuity reply **yes**
- Refined: Cycle 9 Multi-experiment **`WorkSpace` only**; Q1=A research+defer (no force-move; no git-strategy B); Q2=A Continuity carry; plan gate separate; never Complete / Primary next while WorkSpace remains; no Medium/archived peer reopen.

## Status

**`complete`** — refined prompt ready for researcher handoff.
