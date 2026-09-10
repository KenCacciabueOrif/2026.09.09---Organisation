# Prompt betterment notes — Cycle 6 Medium wrappers (soft-deferred finalization)

Session: `sessions/2026.09.09-1612/01-prompt-betterment/`  
Role: **Cycle 6 — Medium wrappers (soft-deferred finalization)** (`fs_mutation`).  
Roadmap row (orchestrator-locked): **Medium wrappers** — **in progress — nearly complete**; scoped to soft-deferred remaining only: **`NextPWATraining`**, **`CursorMobileWorkspace`**. Do **not** jump Primary next until both move (or user drops them from scope). Do **not** re-propose Cycle 4/5 archives. Default Continuity: **finalize both** (do **not** re-soft-defer by default).

## Plain-language meaning of the gates (carry — brief)

| Term | Everyday meaning |
| --- | --- |
| **Plan gate** | After planning, you see a concrete **from → to** list and say yes **before** any move. Continuity / Choose / starting this FAW is not that yes. |
| **fs_mutation** | This cycle will move/rename real folders on disk (after plan gate), not only edit docs. |
| **Fail-closed** | If something unexpected appears (e.g. worktrees / SSH / multi-remote), we **stop that item** instead of guessing. |
| **Atomic nested git** | Move the whole top-level folder **including** its inner `.git` as one piece — no history rewrite. |
| **Continuity** | Reuse Cycles 4–5 rules (layout, taxonomy, must-preserve, status, secrets, verify) unless you change them below. |
| **Soft-deferred finalization** | These two were left at root on purpose earlier; this cycle’s default is to **finish moving them**, not to park them again. |

## Clarifying questions (SHORT Continuity pack — answered Choose all)

**Do not re-ask** the full Cycle 4 first-batch pack or Cycle 5 subset pack. Carry layout, atomic nested git, taxonomy/must-preserve Continuity, 90-day status, opaque `.env`, verify/rollback + INDEX honesty unless Q2/Q3 change them.

Each question includes plain-language explanation + pros/cons. **Informed consent:** answering commits only to Continuity/scope for research/plan — **not** to executing moves (plan gate still mandatory and separate).

---

### Q1 — Finalize both remaining folders this cycle?

**Plain language:** Only two Medium wrappers are left at `C:\Project` root: `NextPWATraining` and `CursorMobileWorkspace`. **Finalize both** means research/plan/implement target **both** this cycle (still one plan gate; still fail-closed per item). **One-only** means you name which one moves now and the other stays for a later cycle. **Drop from scope** means that folder is no longer part of the Medium row (you accept it may stay at root or you will handle it outside FAW). Saying **A** commits to finishing the Medium row after a successful batch (then Primary next → Multi-experiment).

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Finalize **both** this cycle | Matches ROADMAP “nearly complete”; clears Medium row; default Continuity | Larger plan-gate surface; more chance one item fail-closes |
| **B** — One only this cycle (name which) | Smaller blast radius; you control priority | Medium row stays in progress; other name waits |
| **C** — Drop one or both from Medium scope (name which) | Unblocks Primary next without moving the dropped name(s) | Dropped folders stay at root unless you move them later outside this row |

**Ask summary:** Finalize both vs one-only (name) vs drop from scope (name)? Default A.

---

### Q2 — Confirm Cycles 4–5 Continuity still OK?

**Plain language:** Carry forward without re-litigation: Early/simple **layout** (`archive|paused|active` + CreationTime date labels); **atomic nested git**; taxonomy Continuity (**proposed-ratified — ready for user sign-off**, not global final); must-preserve Continuity (**draft — not auto-locked / for user review**); **opaque `.env`** + fail-closed hazards; verify/rollback + INDEX current-path honesty. Saying **A** commits this cycle to those same rules. Saying **B** means you want to change something before moves (say what).

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Yes, Continuity still OK | Fast; consistent with Cycle 4/5 archives | If you now dislike a rule, these last two moves encode it again |
| **B** — Change something (say what) | Fits a new preference | Research/plan must redesign; risk of inconsistency with prior Medium destinations |

**Ask summary:** Keep Cycles 4–5 Continuity locks (layout/git/taxonomy/must-preserve/secrets/verify)? Default A.

---

### Q3 — Keep the 90-day status rule?

**Plain language:** Status folders are where a project “lives” after move: **archive** (done / cold), **paused** (recent but not active daily), **active** (current work). The Continuity rule: default **archive**; if LastWrite is within **90 days** of cycle date `2026.09.09` → prefer **paused**. Orchestrator note: `CursorMobileWorkspace` → likely `paused`; `NextPWATraining` → likely `archive` — research confirms from disk timestamps. Saying **A** commits to that rule for the map. Saying **B** means you override statuses (name them).

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Keep 90-day Continuity (research proposes; expect CursorMobile ≈ paused, NextPWA ≈ archive) | Consistent with Cycles 2–5 | A folder you still use daily might land in paused/archive (you can still reject at plan gate) |
| **B** — Override statuses now (name archive/paused/active per folder) | Full control before research | You must specify; overrides may disagree with LastWrite evidence |

**Ask summary:** Keep 90-day status rule (with expected CursorMobile paused / NextPWA archive) vs override? Default A.

---

### Q4 — Special handling notes OK? (NextPWA opaque `.env` + CursorMobileWorkspace)

**Plain language:** **`NextPWATraining`:** treat any `.env` / secrets as **opaque** — agents must **never read or log** contents; if moved, the files travel with the folder unread. **`CursorMobileWorkspace`:** same opaque-secrets rule; also respect atomic nested git and fail-closed on worktree/SSH/multi-remote (path-only move; **no** remote URL rewrite). Saying **A** commits to those specials. Saying **B** means you want a different secret/git handling (say what) — higher risk.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Opaque `.env` (never read NextPWA); path-only moves; no SSH/remote rewrite; fail-closed on hazards | Safest Continuity; matches Cycles 4–5 | If remotes break after path change, you fix remotes yourself later |
| **B** — Different handling (describe) | Can address a known remote/tooling need | Easy to leak secrets or corrupt git; may force git-strategy cycle |

**Ask summary:** Confirm opaque NextPWA `.env` + path-only CursorMobile / no remote rewrite? Default A.

---

### Q5 — If live-check fail-closes one folder, still finish the other?

**Plain language:** **Fail-closed** means: if research finds a hard hazard (e.g. linked worktrees, multi-remote mess), that folder is **skipped this cycle** with a logged reason — not forced. Saying **A** commits to: move the green one after plan gate; leave the failed one at root (Medium stays in progress or you decide at close). Saying **B** means abort the whole batch if either fails the live-check.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Allow deferring **at most one** hazard item; proceed with the other if plan-gated | Maximizes progress; matches orchestrator “may defer ONE” | Medium row may stay nearly-complete one more cycle |
| **B** — All-or-nothing: if either fail-closes, move neither this cycle | Cleaner “both or none” story | Delays finishing Medium even when one folder is safe |

**Ask summary:** Defer at most one on live-check fail-closed vs all-or-nothing? Default A.

---

## Answers

User reply: **Choose all** for Q1–Q5. Disclosed defaults locked. **Plan gate still mandatory** before any moves — Choose all does **not** approve the from→to map.

| Q | Locked decision | Source | Rationale |
| --- | --- | --- | --- |
| 1 | **A** — Finalize both `NextPWATraining` + `CursorMobileWorkspace` | `Choose all` | Soft-deferred finalization; do not re-soft-defer by default |
| 2 | **A** — Keep Cycles 4–5 Continuity | `Choose all` | Do not re-litigate layout/git/taxonomy/must-preserve/secrets/verify |
| 3 | **A** — 90-day status rule | `Choose all` | CursorMobile ≈ paused; NextPWA ≈ archive (research confirms) |
| 4 | **A** — Opaque NextPWA `.env`; path-only; fail-closed; no SSH rewrite | `Choose all` | Never read secrets; path-only moves |
| 5 | **A** — If live-check blocks one, skip it and still finish the other after plan gate | `Choose all` | Maximize progress; log skip |

**In-scope (locked):** `NextPWATraining`, `CursorMobileWorkspace`.  
**Forbidden sources:** Cycle 4 (`TestRyan`, `ReactRouterTest`, `Simpl`) + Cycle 5 (`NextTest`, `Simpl_Next`, `PWAExempleTristan`) archives.  
**After both succeed:** Medium **Complete** → Primary next **Multi-experiment**.

### Durable ask summary (one line per Q)

1. Finalize both vs one-only (name) vs drop from scope (name)?
2. Keep Cycles 4–5 Continuity (layout/git/taxonomy/must-preserve/secrets/verify)?
3. Keep 90-day status rule (CursorMobile ≈ paused / NextPWA ≈ archive) vs override?
4. Confirm opaque NextPWA `.env` + path-only CursorMobile / no remote rewrite?
5. Defer at most one on live-check fail-closed vs all-or-nothing?

**Informed consent record:** Q1–Q5 were explained with plain language + pros/cons before Choose all; no jargon-only debt this phase. **Plan gate** remains a separate later approval.

## Continuity (locked — do not re-ask / do not re-litigate)

### Orchestrator locks (this cycle)

- ROADMAP row: **Medium wrappers** (**in progress — nearly complete**)
- Cycle id: **Cycle 6 — Medium wrappers (soft-deferred finalization)**
- Remaining at root (verified per orchestrator at `C:\Project`): `NextPWATraining`, `CursorMobileWorkspace`
- **Do not** re-propose / re-move Cycle 4 archives: `TestRyan`, `ReactRouterTest`, `Simpl`
- **Do not** re-propose / re-move Cycle 5 archives: `NextTest`, `Simpl_Next`, `PWAExempleTristan`
- **mutation_class:** `fs_mutation` with **mandatory user plan gate**
- Default Continuity: **finalize both**; after successful moves → Medium **Complete** → Primary next **Multi-experiment**
- Live-check INDEX vs disk in research; ignore stale INDEX paths for move decisions
- Do not touch must-preserve draft paths or organisation repo
- Git-strategy FAW **not** in scope unless user expands; worktrees/SSH/multi-remote → fail-closed (may defer one item)
- Early/simple **Complete** — do not reopen
- Q1–Q5 locked via **Choose all** (defaults A)

### From Cycles 4–5 Choose-all (Q2/Q3/Q4 = A — locked Continuity)

- Layout: `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\`
- CreationTime wins for date labels; spaces kept
- Atomic nested git; no history rewrite; no remote URL rewrite
- Taxonomy: Continuity — **proposed-ratified — ready for user sign-off** (not global final)
- Must-preserve: **draft — not auto-locked / for user review**
- Status: archive default; LastWrite ≤90 days from `2026.09.09` → paused
- Opaque `.env` / secrets (**especially NextPWATraining — never read**); fail-closed hazards
- Verify/rollback + INDEX current-path honesty
- Catalogue update after moves; propose map → user approves → execute
- Org repo protect; never delete payload to clean up

## Assumptions

- No agent git push / pull / remote publish this cycle.
- Hygiene / multi-experiment / Obsidian / ProjetOrif / special-git out of scope until Medium Complete + Primary next lock.
- Cycle 4/5 destinations stay put; catalogue may lag — research live-checks.
- Parent status folders may already exist; create if missing.
- Q1–Q5 locked via Choose all; exact destinations/statuses = research/plan until **plan gate**.
- Continuity / Choose locks scope/rules only — **not** move execution approval.

## Open risks

- Nested `.git` / worktrees / SSH / multi-remote on either remaining folder → fail-closed skip (Q5=A allows one defer).
- `NextPWATraining` secrets surface — any read/log of `.env` is Critical process failure.
- Target name collision under archive/paused/active → plan must detect before move.
- INDEX lag — do not treat stale paths as sources; do not re-move Cycle 4/5 archives.
- If one item fail-closes (Q5=A), Medium stays in progress with that remaining name.

## Self-improvement backlog

None. Informed-consent explanations + pros/cons were present before Choose all.

## Key alignment changes (raw → refined)

- Raw `/full-agent-workflow next cycle` → **Cycle 6 Medium wrappers (soft-deferred finalization)** `fs_mutation`.
- User **Choose all** → Q1–Q5 defaults **A** locked (`Choose all`).
- In-scope: finalize both soft-deferred (`NextPWATraining`, `CursorMobileWorkspace`); Continuity kept; opaque `.env`; fail-closed may skip one.
- Forbidden sources: all Cycle 4 + Cycle 5 Medium archives.
- After successful both-moves → Medium **Complete** → Primary next **Multi-experiment**.
- Exact from→to map still requires **plan gate** (Choose ≠ move approval).
