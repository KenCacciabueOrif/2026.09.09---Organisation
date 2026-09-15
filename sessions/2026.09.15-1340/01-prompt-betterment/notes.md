# Prompt betterment notes — Cycle 22

**Session:** `sessions/2026.09.15-1340/` (adopted incomplete; reframed Cycle 22)  
**Prior:** `sessions/2026.09.15-1320/` complete — dashboard Run 3 (dedupe + global search). Remaining perf: items 20–22 (data-split, debounce, index map).  
**Consent UX:** All clarifying Qs below include plain-language explanation + pros/cons. Recorded: explanations shipped with this pack (no jargon-debt for unanswered state).

---

## Durable ask summary (one line per Q)

1. **Q1 workstream** — Who picks this cycle’s concrete advance: research highest-value (default), force dashboard, force WorkSpace/#4, or escalate now?
2. **Q2 dashboard slice** — If dashboard wins: research picks 1–2 of items 20–22 (default), data-split only, debounce+index only, or all three?
3. **Q3 WorkSpace depth** — If WorkSpace wins: anti-loop material advance or escalate (default), #4 approval gate only (docs), or nest extract (only if #4 already approved — it is not)?
4. **Q4 taxonomy / must-preserve** — Carry proposed-ratified + draft must-preserve Continuity (default) or waive for this cycle’s docs only?
5. **Q5 publish** — After gate + implement: git-manager allowlisted stage/commit/push via GfW (default yes) or session docs only (no push)?
6. **Q6 plan gate reminder** — Confirm Continuity / Choose locks intent only; separate plan-gate yes still required before execute (ack default)?

---

## Clarifying questions (user-facing pack)

### Q1 — Which workstream should Cycle 22 pursue?

**Plain language:** This cycle must produce one **concrete advance** (something new and useful), not another write-up that only repeats what we already know. A *workstream* is the topic we focus on. Saying **Choose** (or leaving blank) means we lock the **default** below. That still does **not** mean “go move files / change the dashboard now” — a later **plan gate** (you approve a written plan) is required before execution.

| Option | What it commits to | Pros | Cons |
| --- | --- | --- | --- |
| **A (default)** | Researcher surveys ROADMAP + dashboard backlog and proposes the **single highest-value concrete advance**; planner presents it at the plan gate. May be dashboard perf, WorkSpace Continuity X / #4, or **escalate** if nothing new. | Maximizes value; respects anti-loop; you still approve the plan. | You do not pre-lock the topic; surprise if you wanted a forced path. |
| **B** | Lock **dashboard** catalogue betterment (perf candidates 20–22) this cycle. ROADMAP WorkSpace row stays untouched. | Clear, reversible org-repo code; uses Run 3 leftover backlog. | Defers ROADMAP Primary next (WorkSpace TNA / #4). |
| **C** | Lock **WorkSpace only** Continuity X path (#4 / TNA / nests). Do not mark Multi-experiment Complete. | Advances programme Primary next. | Higher risk / more gates; nest extract blocked until #4 **approved**. |
| **D** | **Escalate now** (`escalate_break_loop`) — stop iterating; Continuity gate for next FAW (e.g. X/P/N/H), zero corpus FS this cycle. | Honest anti-loop; no empty re-attest. | No product/dashboard progress this cycle. |

**Choose / unanswered / yes→defaults → A.**

---

### Q2 — If dashboard is selected (Q1=A picks it, or Q1=B): which perf slice?

**Plain language:** The dashboard refinement plan still lists three performance items: (20) split the big data blob into a JSON file, (21) debounce commit-list redraws while typing, (22) build a repo index map once instead of slow lookups. We can do a small slice or all three.

| Option | What it commits to | Pros | Cons |
| --- | --- | --- | --- |
| **A (default)** | Research picks **1–2** of items 20–22 for highest concrete gain this cycle. | Focused; less thrash. | Not all perf items land together. |
| **B** | **Data-split-to-JSON only** (item 20). | Biggest structural perf/cache win. | Leaves debounce/index for later. |
| **C** | **Debounce + index map** (21–22) only. | Small, safe UX/CPU wins. | Leaves 594KB inline blob. |
| **D** | **All three** (20–22). | Clears perf cluster. | Larger diff; more verification. |

**N/A if Q1=C or Q1=D.** Choose / unanswered → **A** when dashboard applies.

---

### Q3 — If WorkSpace / Continuity X is selected (Q1=A picks it, or Q1=C): how deep?

**Plain language:** `WorkSpace` is still the only unfinished Multi-experiment folder. Cycle 20 wrote a **draft** parent-surgery plan (#4) — “draft” means written for review, **not** approved to move nested projects. Whole-tree archive is **forbidden**.

| Option | What it commits to | Pros | Cons |
| --- | --- | --- | --- |
| **A (default)** | Require a **material** clearance/#4 advance; if research finds **no material delta** vs Cycles 18–20 → **escalate** instead of another honesty pass. | Anti-loop; no theater. | May end in escalate, not nest move. |
| **B** | This cycle aims at **#4 approval gate** (docs / user sign-off on surgery draft) — still **zero nest moves** until a later dedicated plan gate after approval. | Unblocks future nest extract. | Docs/gate only; no FS progress. |
| **C** | Nest extract / TNA path mutation — **only valid if #4 already approved** (it is **not**). Treat as invalid → fall back to A. | — | Do not choose; #4 pending. |

**N/A if Q1=B or Q1=D.** Choose / unanswered → **A** when WorkSpace applies. **Continuity yes ≠ nest execute.**

---

### Q4 — Taxonomy / must-preserve Continuity?

**Plain language:** Earlier cycles proposed a folder-classification scheme (*taxonomy*) and a caution list (*must-preserve*). Those are **proposed / draft**, not final user sign-off, unless you already signed off elsewhere.

| Option | Pros | Cons |
| --- | --- | --- |
| **A (default) Carry** — keep prior Continuity; do not re-litigate. | Stable; matches ROADMAP. | Draft remains draft. |
| **B Waive for this cycle’s docs only** — allow wording updates without claiming final ratification. | Flexibility on docs. | Slight Continuity churn. |

**Choose / unanswered → A.**

---

### Q5 — Publish after successful implement (allowlisted)?

**Plain language:** *Publish* means the **git-manager** agent stages/commits/pushes only this organisation repo’s allowlisted files (session docs, FAW/workflow paths, and any approved catalogue/program changes) using **Git for Windows + credential manager**. You are not asked to push by hand.

| Option | Pros | Cons |
| --- | --- | --- |
| **A (default) Yes** — mid + final closing-pass git-manager as FAW requires. | Session closes clean on remote. | Needs agent GfW/GCM working. |
| **B No push** — write session artifacts only; leave commit/push for a later cycle. | Safer if auth flaky. | Session may stay dirty / incomplete vs publish AC. |

**Choose / unanswered → A.** Fail-closed if push blocked (session `blocked`, not false complete).

---

### Q6 — Acknowledge plan gate?

**Plain language:** Answering this Continuity pack (even **yes** / **Choose**) only locks **intent**. The planner will still stop for a **plan gate**: you must approve (or amend) the written plan before implementer runs. Nest moves also need **#4 approved** first.

| Option | Pros | Cons |
| --- | --- | --- |
| **A (default) Ack** | Clear consent model. | Extra pause before code/FS. |
| **B** (not offered for FS) — cannot waive plan gate for corpus moves / remote-config. | — | — |

**Choose / unanswered → A.**

---

## Answers

**Raw Continuity reply:** `Continuity pack — Choose: all defaults locked (A/A/A/A/A/A). …`  
**Source:** `Choose` / `yes→defaults`  
**Consent note:** Pack shipped with plain-language + pros/cons before Choose; no jargon-explanation debt.

| Q | Locked | Meaning | Source | Rationale |
| --- | --- | --- | --- | --- |
| Q1 | **A** | Research picks single highest-value concrete advance (dashboard perf **or** WorkSpace/#4 **or** escalate) | Choose | Disclosed default; maximizes concrete value under anti-loop |
| Q2 | **A** | If dashboard applies: research picks **1–2** of items 20–22 | Choose | Focused slice; applies only if Q1 research selects dashboard |
| Q3 | **A** | If WorkSpace applies: material advance **or** escalate; **no** empty re-attest; **no** nest moves (#4 not approved) | Choose | Anti-loop; #4 draft ≠ nest execute |
| Q4 | **A** | Carry taxonomy / must-preserve Continuity (proposed-ratified / draft) | Choose | Stable programme Continuity |
| Q5 | **A** | git-manager publish via GfW after gate + implement; fail-closed if push blocked | Choose | Standard FAW mid + final closing pass |
| Q6 | **A** | Ack: Continuity locks **intent only**; separate **plan-gate** approval still required before execute | Choose | Continuity ≠ execute |

**Phase 1 status:** complete — proceed research → planner → **present plan gate** (do not implement until plan-gate yes).

---

## Continuity (locked — do not re-ask)

- **Session folder:** `sessions/2026.09.15-1340/` — resume adopted; no parallel session.
- **Cycle id:** Cycle 22 (not Cycle 21 reorg stub).
- **Continuity Choose:** Q1=A, Q2=A, Q3=A, Q4=A, Q5=A, Q6=A (Source Choose / yes→defaults).
- **Workstream:** research-owned highest-value pick among dashboard perf 20–22, WorkSpace Continuity X/#4 material path, or `escalate_break_loop`.
- **Prior dashboard:** Run 3 complete (`2026.09.15-1320`); remaining perf 20–22 unstarted.
- **ROADMAP Primary next:** Multi-experiment **Remaining: `WorkSpace` only** (TNA envelope); **not** Complete; do **not** jump Special git / Primary next past it; do **not** reopen Medium/Early or archived Multi-experiment peers (`PWAExemple`, `OS-IA`, etc.).
- **Strategy artifacts:** `program/git-strategy-workspace-hazards.md`; `program/git-strategy-tna-parent-surgery.md` — clearance **#4 DRAFT written (Cycle 20) / approval pending**.
- **#4 draft ≠ nest-move approval**; docs gate yes ≠ nest execute; OS-IA alone never Completes row; this Continuity **forbids nest FS** until #4 approved + later dedicated gate.
- **Anti-loop:** concrete advance required; no material delta → `escalate_break_loop` (not Continuity A theater).
- **Git:** git-manager owns add/commit/push (GfW); org-repo git-root only; Q5=A publish Continuity.
- **Continuity / Choose ≠ plan-gate execute** (Q6=A).
- **Taxonomy / must-preserve:** carry as proposed-ratified / draft (Q4=A).

---

## Assumptions

- Orchestrator reframed stub correctly as Cycle 22; prior phase stubs under this folder are superseded by this prompt-betterment pass.
- Research will compare dashboard vs WorkSpace material vs escalate and name one winner for the plan gate.
- Browser harness may still be unavailable; dashboard verification may use Node smoke (as Run 3).
- Plan-gate presentation is orchestrator/user-facing after planner; implementer waits.

---

## Open risks

- Q1=A may surprise if user expected forced WorkSpace progress.
- WorkSpace path without #4 approval cannot legally nest-extract; risk of docs-only loop → must escalate if no delta.
- Dashboard data-split changes load path; needs fetch/error UX + regenerate pipeline AC.
- Agent GfW/GCM failure → fail-closed `blocked`.

---

## Self-improvement backlog (if any)

- None yet (explanations included in this pack).

---

## Key alignment changes (raw → refined)

- Raw “Cycle 22 survey + propose highest-value advance” → Continuity **Choose all A** locked; research owns workstream pick.
- Explicit anti-loop: no-delta → escalate, not re-attest; nest FS forbidden until #4 approved.
- Separated Continuity intent vs plan-gate execute (Q6=A).
- Publish ownership locked to git-manager / GfW (Q5=A).
- Phase 1 complete → hand off research → planner → plan gate.
