# Prompt betterment notes — Cycle 7 Multi-experiment (first subset)

Session: `sessions/2026.09.10/01-prompt-betterment/`  
Role: **Cycle 7 — Multi-experiment (first subset)** (`fs_mutation` expected).  
Roadmap row (orchestrator-locked — **do not re-pick**): **Primary next → Multi-experiment** — candidates `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace`.  
Prior session: `sessions/2026.09.09-1612/` (Cycle 6 Medium wrappers **Complete**).  
**Do not** reopen Medium wrappers or Early/simple archive/paused paths as move sources.

## Plain-language meaning of the gates (carry — brief)

| Term | Everyday meaning |
| --- | --- |
| **Plan gate** | After planning, you see a concrete **from → to** list and say yes **before** any move. Continuity / Choose / starting this FAW is **not** that yes. |
| **fs_mutation** | This cycle will move/rename real folders on disk (after plan gate), not only edit docs. |
| **Fail-closed** | If something unexpected appears (worktrees / multi-remote / unclear git roots), we **stop that item** instead of guessing. |
| **Atomic nested git** | Move the whole top-level folder **including** its inner `.git` as one piece — no history rewrite. |
| **Continuity** | Reuse Cycles 2–6 rules (layout, taxonomy, must-preserve, status, secrets, verify, SSH path-only) unless you change them below. |
| **Multi nested-git caution** | These folders may contain **more than one** git repo inside; each stays atomic; research may **defer** a name if roots look unsafe. |
| **SSH-origin path-only** | Move the folder as-is; **do not** change `origin` remote URLs unless you start a dedicated git-strategy cycle. |
| **Taxonomy proposed-ratified** | Folder-type scheme is ready for your sign-off — **not** claimed as final global law without your approval. |
| **Must-preserve draft** | Keep-list is **draft — not auto-locked / for user review** — not silently treated as final. |

## Clarifying questions (SHORT Multi-experiment first-batch Continuity pack — answered Choose all)

**Do not re-ask** Medium/Early first-batch packs. Carry layout destinations, atomic nested git, opaque `.env`, taxonomy/must-preserve Continuity, 90-day status, verify/rollback + INDEX honesty unless a question below changes them.

Each question includes plain-language explanation + pros/cons. **Informed consent:** answering commits only to Continuity/scope for research/plan — **not** to executing moves (**plan gate still mandatory and separate**).

Unanswered items with disclosed defaults → after user reply (or **Choose** / partial leave-blank), lock via Source `Choose` / `Choose (unanswered→default)` — never leave blanks for researcher/planner.

---

### Q1 — How many Multi-experiment folders this cycle?

**Plain language:** Four candidates sit at `C:\Project` root: `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace`. **Small first subset (default)** means research/plan target **1–2** folders this cycle (research prefers lower-risk peers; may name which). **All four** means one map covering every candidate (still one plan gate; still fail-closed per item). **Name your own list** means you pick exact folders. Saying **A** commits only to a **scoped first slice** for research/plan — remaining names stay on the Multi-experiment row for a later cycle. It does **not** approve any move.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Small first subset (**1–2** folders; research picks lower-risk peers) | Lower blast radius; matches ROADMAP “sub-batches OK”; safer with multi nested-git | Row stays in progress; two more folders wait |
| **B** — All four this cycle | Finishes Multi-experiment sooner if all are clean | Larger plan-gate surface; more chance several fail-close |
| **C** — Named list only (you list folders) | Full control of priority | You must name them; research still may defer hazards |

**Ask summary:** Small 1–2 subset (default) vs all four vs named list?

---

### Q2 — Multi nested-git caution OK?

**Plain language:** These projects may contain **several** `.git` folders. Continuity says: each nested git root stays **atomic** (moved intact with its tree). If research finds linked **worktrees**, messy **multi-remote**, or unexpected extra roots, that folder is **fail-closed / deferred** this cycle (logged reason) — not force-moved. Saying **A** commits research/plan to that caution. Saying **B** means you want a different rule (say what) — may require a dedicated **git-strategy** cycle.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Yes: atomic nested git + fail-closed on worktrees / multi-remote / unexpected roots (may defer those names) | Safest Continuity; avoids corrupting repos | Some candidates may stay at root another cycle |
| **B** — Different git handling (describe) | Can address a known special case | Easy to break remotes/worktrees; may block until git-strategy |

**Ask summary:** Keep multi nested-git caution + fail-closed deferrals? Default A.

---

### Q3 — SSH / remotes: path-only moves (no origin rewrite)?

**Plain language:** If a folder’s git remote uses **SSH** (or any URL), Continuity is **path-only**: move the folder on disk; **never rewrite** `origin` (or other remotes) in this cycle. Fixing remotes later is a **separate** git-strategy FAW if you choose it. Saying **A** commits to path-only. Saying **B** means you want remote URL changes now (higher risk; usually wrong cycle).

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Path-only; no remote rewrite | Matches Cycles 2–6; no silent remote edits | After move, tools may need path updates you do yourself |
| **B** — Allow remote rewrite this cycle (say which) | Can “fix” remotes in one go | Wrong URL = broken push/pull; needs dedicated git-strategy care |

**Ask summary:** Keep SSH/origin path-only (no rewrite)? Default A.

---

### Q4 — Carry Medium / prior Continuity (layout, secrets, taxonomy, status)?

**Plain language:** Keep the same rules as Cycles 2–6 unless you change them: destination **layout** (`archive` / `paused` / `active` under catalogue taxonomy); **opaque `.env`** (agents never read or quote secrets — path presence only); taxonomy **proposed-ratified — ready for user sign-off** (not claimed final); must-preserve **draft — not auto-locked / for user review**; **90-day** status heuristic (default archive; recent LastWrite → prefer paused); verify / rollback notes + honest `catalogue/INDEX.md` paths. Saying **A** commits this cycle to those locks. Saying **B** means change something before the map (say what). Prior pending gates are **not** hard blockers solely to re-litigate — still keep **plan gate** separate.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Yes, carry Continuity as above | Fast; destinations stay consistent with Medium/Early | If you now dislike a rule, new moves encode it again |
| **B** — Change something (say what) | Fits a new preference | Research/plan redesign; risk of inconsistent destinations |

**Ask summary:** Carry layout / opaque .env / taxonomy+must-preserve Continuity / 90-day status / verify? Default A.

---

## Answers

User reply: **Choose all** for Q1–Q4. Disclosed defaults locked. **Plan gate still mandatory** before any moves — Choose all does **not** approve the from→to map.

| Q | Ask summary | Locked decision | Source | Rationale |
| --- | --- | --- | --- | --- |
| 1 | Small 1–2 subset (default) vs all four vs named list? | **A** — Small first subset (**1–2** folders; research picks lower-risk peers among `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace`) | `Choose all` | ROADMAP sub-batches; lower blast radius for multi nested-git |
| 2 | Keep multi nested-git caution + fail-closed deferrals? Default A. | **A** — Atomic nested `.git`; fail-closed skip/defer on worktrees / multi-remote / unexpected roots | `Choose all` | Safest Continuity; do not force unsafe roots |
| 3 | Keep SSH/origin path-only (no rewrite)? Default A. | **A** — Path-only moves; never rewrite `origin` this cycle | `Choose all` | Matches Cycles 2–6; remotes stay intact |
| 4 | Carry layout / opaque .env / taxonomy+must-preserve Continuity / 90-day status / verify? Default A. | **A** — Carry Cycles 2–6 Continuity as locked below | `Choose all` | Do not re-litigate Medium/Early Continuity |

**Informed consent note:** Q1–Q4 included plain-language explanation + pros/cons in the ask; user Choose all after that pack — no jargon-explanation debt.

## Continuity (locked — do not re-ask unless user changes)

| Lock | Value |
| --- | --- |
| ROADMAP row | **Primary next → Multi-experiment** (orchestrator-locked) |
| Candidates | `PWAExemple`, `GitTest`, `WorkStationPWA`, `WorkSpace` |
| Prior row | Medium wrappers **Complete** (Cycle 6) — do not reopen |
| Early/simple | **Complete** — do not reopen |
| Mutation class | `fs_mutation` expected; **per-batch plan gate mandatory** (separate from Choose) |
| Layout | archive / paused / active per research status (catalogue taxonomy) |
| Nested git | Atomic intact `.git` trees |
| Secrets | Opaque `.env` — path presence only; never read/quote |
| Remotes | SSH/origin **path-only** (no rewrite unless user opts into git-strategy) |
| Status heuristic | 90-day Continuity (research confirms from disk) |
| Taxonomy | **proposed-ratified — ready for user sign-off** (not final without explicit approval) |
| Must-preserve | **draft — not auto-locked / for user review** |
| Pending hard blockers | None; do not re-block solely to re-litigate taxonomy/must-preserve |

## Assumptions

- User intent “next cycle” = execute Multicycle program next row (Multi-experiment first subset), not docs-only.
- Research will live-check candidates and may propose which 1–2 are lower-risk under default Q1=A.
- Optional near-miss plan-gate typos (e.g. “sey”→yes) are an **orchestrator** concern at plan gate later — not a Continuity lock here.

## Open risks

- Multi nested git / worktrees / multi-remote may shrink the executable subset after research (Q2 fail-closed).
- Continuity / Choose must not be treated as move approval — orchestrator must still run plan gate.
- Research must pick concrete 1–2 lower-risk peers; remaining names stay on Multi-experiment row (partial progress Notes).

## Self-improvement backlog (if any)

- None for this phase (informed consent pack explained before Choose all).

## Key alignment changes (raw → refined)

- Raw: “look at the last sessions, do the next cycle”
- Refined: Cycle 7 Multi-experiment **first subset** (`fs_mutation`); Q1–Q4 = A via Choose all; plan gate separate; no Medium/Early reopen.
