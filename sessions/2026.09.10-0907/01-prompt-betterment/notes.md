# Prompt betterment notes — Cycle 10 Multi-experiment (`WorkSpace` only + hazard remediation)

Session: `sessions/2026.09.10-0907/01-prompt-betterment/`  
Role: **Cycle 10 — Multi-experiment WorkSpace-only + hazard remediation / git-strategy Continuity**.  
Roadmap row (orchestrator-locked — **do not re-pick / do not jump Primary next / do not mark Complete**): **Multi-experiment remaining: `WorkSpace` only**.  
Prior session: `sessions/2026.09.10-0848/` (Cycle 9 — `docs_only` defer; hazards **not** cleared).  
**Do not** reopen Medium wrappers or Early/simple; **do not** re-propose archived Multi-experiment peers (`PWAExemple`, `GitTest`, `WorkStationPWA`) as move sources.  
**Pack type:** short **WorkSpace-only Continuity pack adapted for hazard-solve** — **not** Medium soft-deferred finalize-by-default; **not** Cycle 9 pure-defer default.

## User intent override (orchestrator + raw goal)

Raw goal: `/full-agent-workflow do next cycle and solve WorkSpace hazards`.  
Treat as preferring **dedicated git-strategy / hazard-remediation Continuity** (former Cycle 9 Q1=B class).  
Still **never silent force-move** of the whole XL tree; any corpus path mutation needs a **separate plan gate** with a concrete map.

## Known uncleared hazards (Cycle 9 — carry into research; do not re-litigate existence)

- Multi-remote hermes-agent (`origin` + `cada`) also on backup/quarantine clones  
- Unexpected nested `.git` under `_backups` and `_quarantine`  
- 7 nested roots; XL size; opaque `.env`×17 unread; must-preserve draft Medium caution  

## Plain-language meaning of the gates (carry — brief)

| Term | Everyday meaning |
| --- | --- |
| **Plan gate** | After planning, you see a concrete **from → to** list (if any) and say yes **before** any move. Continuity / Choose / starting this FAW is **not** that yes. |
| **fs_mutation** | A plan that moves/renames/deletes real corpus folders on disk (after plan gate). |
| **docs_only** | Docs / INDEX / ROADMAP / session notes only — **zero** corpus folder moves. |
| **Fail-closed** | If a step is still unsafe or unclear, we **stop** instead of guessing. |
| **Atomic nested git** | Treat each nested `.git` tree as one piece — move intact or not at all; no history rewrite. |
| **Continuity** | Reuse Cycles 2–9 rules unless changed below. |
| **SSH-origin path-only** | Relocate/document path as-is; **do not** rewrite `origin` URLs unless a gated git-strategy step says so. |
| **Dedicated git-strategy / hazard remediation** | Classify remotes, decide fate of backup/quarantine roots, write safe relocation rules; optional **scoped** FS only after plan gate — **not** a silent whole-tree archive. |
| **Taxonomy proposed-ratified** | Ready for user sign-off — **not** final without explicit approval. |
| **Must-preserve draft** | **draft — not auto-locked / for user review**. |

## Clarifying questions (SHORT hazard-solve pack — answered)

Each question included plain-language explanation + what yes/each choice commits to + pros/cons.  
**Informed consent:** answering commits only to Continuity/path for research/plan — **not** to executing moves (**plan gate still mandatory and separate** if any `fs_mutation` is proposed).

### Q1 — Path for `WorkSpace` this cycle?

**Ask summary:** Dedicated git-strategy / hazard remediation (default A) vs back out to pure research+defer (B)?

### Q2 — How far may “solve” go this cycle?

**Ask summary:** Classification + safe-rules docs first with optional scoped FS map only via plan gate (default A) vs prioritize scoped FS map (B) vs docs-only forbid FS proposal (C)?

### Q3 — Confirm Continuity still applies?

**Ask summary:** Carry layout / atomic nested-git / SSH path-only / opaque .env / taxonomy+must-preserve / 90-day / Windows lock recovery / INDEX honesty / never force-move whole tree / never Complete while WorkSpace remains / no peer reopen? Default A.

---

## Answers

User reply (raw): **Choose all**  
Interpreted as accepting all disclosed Continuity defaults. Disclosed defaults locked. **Plan gate still mandatory** before any moves — Continuity Choose **≠** approve a from→to map.

| Q | Ask summary | Locked decision | Source | Rationale |
| --- | --- | --- | --- | --- |
| 1 | Dedicated git-strategy / hazard remediation (A) vs pure defer (B)? | **A** — Dedicated **hazard remediation / git-strategy** Continuity: research + plan to classify remotes, fate of `_backups`/`_quarantine` roots, document safe relocation rules. **No silent whole-tree force-move.** | `Choose all` | Matches user “solve WorkSpace hazards”; reversible-leaning strategy over irreversible archive |
| 2 | Remediation depth A/B/C? | **A** — Prefer **classification + safe-rules docs** first. Planner **may** draft a **scoped** `fs_mutation` map only for **named hazard isolation** — still waits for plan gate. Whole XL tree archive under ordinary Multi-experiment Continuity = **OUT OF SCOPE**. | `Choose all` | Prefer reversible docs; scoped FS optional and gated |
| 3 | Carry Continuity? | **A** — Carry Continuity as locked below | `Choose all` | Do not re-litigate Cycles 2–9 Continuity |

**Informed consent note:** Q1–Q3 included plain-language explanation + pros/cons in the prior ask before “Choose all”; no jargon-explanation debt.

## Continuity (locked — do not re-ask unless user changes)

| Lock | Value |
| --- | --- |
| ROADMAP row | **Multi-experiment remaining `WorkSpace` only** (orchestrator-locked) — same row; **not** Primary next; **not** Complete while it remains |
| Remaining candidate only | `WorkSpace` |
| Already moved (do not re-propose) | `GitTest`, `WorkStationPWA` (Cycle 7); `PWAExemple` (Cycle 8) → archive |
| Prior rows | Medium wrappers **Complete**; Early/simple **Complete** — do not reopen |
| Path (Q1=A) | Dedicated **hazard remediation / git-strategy** Continuity (not Cycle 9 pure-defer) |
| Mutation class (Q2=A) | Prefer **docs_only** classification + safe-rules; **scoped `fs_mutation`** only for named hazard isolation **and** only after separate plan gate; whole XL tree archive under ordinary Multi-experiment Continuity **OUT OF SCOPE** |
| Layout | archive / paused / active per research status (catalogue taxonomy) |
| Nested git | Atomic intact `.git` trees; fail-closed on worktrees / multi-remote / unexpected roots unless remediation plan explicitly addresses them under plan gate |
| Secrets | Opaque `.env` — path presence only; never read/quote |
| Remotes | SSH/origin **path-only** (no rewrite) unless a later gated strategy step says otherwise |
| Status heuristic | 90-day Continuity (research confirms from disk if classifying) |
| Windows lock recovery | Prefer single move; on PermissionDenied/split → reunify + `robocopy /E /MOVE`; empty `.git` shells only; re-attest; log deviation |
| Taxonomy | **proposed-ratified — ready for user sign-off** (not final without explicit approval) |
| Must-preserve | **draft — not auto-locked / for user review** |
| INDEX honesty | Document hazards / remediation progress; do not claim moves that did not happen |
| Pending hard blockers | None; do not re-block solely to re-litigate taxonomy/must-preserve |

## Assumptions

- User “Choose all” = Q1=A + Q2=A + Q3=A as disclosed.
- “Solve hazards” = git-strategy / hazard-remediation Continuity, not inventing mid-cycle force archive of the whole XL tree.
- Continuity Choose ≠ move approval; plan gate remains mandatory if any corpus move map is proposed.
- Research may re-probe Cycle 9 hazards; existence is already known — focus on classification + remediation options / safe rules.
- Agent-owned: do not dump “user must fix remotes/PATH” as Continuity chores.
- If scoped FS is not yet safe → process pass with docs + honest INDEX/ROADMAP; row stays in progress (valid).

## Open risks

- Classification may leave hazards uncleared → expected fail-closed on whole-tree move; do not invent substitute sources or jump Primary next.
- Treating Continuity Choose as move approval would be a process fail.
- Marking Multi-experiment Complete while `WorkSpace` remains would be a process fail.
- Silent whole-tree archive would be a process fail.
- Scoped isolation map proposed without plan gate would be a process fail.
- Windows nested-`.git` locks may appear if a scoped move is later approved — recovery Continuity must be followed.

## Self-improvement backlog (if any)

- None for this phase (informed consent pack explained before Choose all).

## Key alignment changes (raw → refined)

- Raw: `/full-agent-workflow do next cycle and solve WorkSpace hazards` + Continuity reply **Choose all**
- Refined: Cycle 10 Multi-experiment **`WorkSpace` only**; Q1=A dedicated hazard remediation / git-strategy; Q2=A docs-first + optional scoped gated FS for named hazards only (whole-tree archive OOS); Q3=A Continuity carry; Choose ≠ plan gate; never Complete / Primary next while WorkSpace remains; no Medium/archived peer reopen.

## Status

**`complete`** — refined prompt ready for researcher handoff.
