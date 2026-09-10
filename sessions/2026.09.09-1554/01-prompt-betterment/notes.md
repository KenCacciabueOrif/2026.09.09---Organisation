# Prompt betterment notes — Cycle 5 Medium wrappers (remaining)

Session: `sessions/2026.09.09-1554/01-prompt-betterment/`  
Role: **Cycle 5 — Medium wrappers (remaining)** (`fs_mutation`).  
Roadmap row (orchestrator-locked): **Medium wrappers** — **in progress**; scoped to **remaining 5 only**. Do **not** jump Primary next. Do **not** re-propose Cycle 4 moved folders (`TestRyan`, `ReactRouterTest`, `Simpl`).

## Plain-language meaning of the gates (carry — brief)

| Term | Everyday meaning |
| --- | --- |
| **Plan gate** | After planning, you see a concrete **from → to** list and say yes **before** any move. Continuity / Choose / starting this FAW is not that yes. |
| **fs_mutation** | This cycle will move/rename real folders on disk (after plan gate), not only edit docs. |
| **Fail-closed** | If something unexpected appears (e.g. worktrees / multi-remote), we **stop that item** instead of guessing. |
| **Atomic nested git** | Move the whole top-level folder **including** its inner `.git` as one piece — no history rewrite. |
| **Continuity** | Reuse Cycle 4 Choose-all rules (layout, taxonomy, must-preserve, status, secrets, verify) unless you change them below. |

## Clarifying questions (SHORT Continuity pack — awaiting answers)

**Do not re-ask** the full Cycle 4 first-batch pack (layout, atomic nested git, taxonomy Continuity, must-preserve Continuity, 90-day status, opaque `.env` + fail-closed, verify/rollback + INDEX honesty). Those stay locked unless Q3 says otherwise.

Each question below includes plain-language explanation + pros/cons. **Informed consent:** answering commits only to Continuity/scope for research/plan — **not** to executing moves (plan gate still mandatory).

---

### Q1 — All five remaining vs a smaller subset this cycle?

**Plain language:** Five folders are still at `C:\Project` root for this Medium row. A **smaller subset** means research/plan/implement target only **2–3** of them this cycle (agent proposes which after research unless you name them in Q2/Q1-C). **All five** means one bigger move batch (still one plan gate). Saying **A** commits to a smaller risk surface now and leaves any leftover names for a later Medium cycle until the row is Complete.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Smaller subset (2–3 of the remaining five; research proposes which, respecting Q2) | Safer; faster plan-gate review; matches ROADMAP “prefer small subset” | Leaves 2–3 wrappers at root for another cycle |
| **B** — All five remaining this cycle | Can finish the Medium wrappers row sooner | Larger plan gate; more collision / secret / nested-git surface |
| **C** — I’ll name exact folders (list them) | Full control of this batch | You must specify names; may conflict with hazard findings |

**Ask summary:** Subset (2–3) vs all five remaining vs name list? Default A.

---

### Q2 — Include higher-risk `NextPWATraining` / `CursorMobileWorkspace` now, or defer again?

**Plain language:** Cycle 4 preferred simpler / lower-hazard wrappers first. These two often carry more nested-git / secrets / tooling risk (especially `NextPWATraining` `.env` — **do not read**; still move opaque if included). **Defer** means they stay at root this cycle even if Q1=A picks a subset from the safer three (`NextTest`, `Simpl_Next`, `PWAExempleTristan`). **Include now** means research may shortlist them (still fail-closed if hazards appear). Saying **A** commits to soft-deferring these two unless you choose B/C.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Soft-defer both higher-risk names this cycle; prefer subset from `NextTest`, `Simpl_Next`, `PWAExempleTristan` | Lower blast radius; secrets stay put until a deliberate cycle | Medium row stays in progress longer |
| **B** — Allow research to include either/both if live-check looks low-hazard (still fail-closed) | May clear harder items sooner | Higher chance of defer-at-plan or secrets-in-batch |
| **C** — Force-include one or both (name which) despite risk preference | You control priority | You accept opaque-`.env` + atomic-git handling + possible fail-closed skip |

**Ask summary:** Defer NextPWATraining / CursorMobileWorkspace vs allow/force include? Default A.

---

### Q3 — Confirm Cycle 4 Continuity defaults still OK?

**Plain language:** Carry forward without re-litigation: Early/simple **layout** (`archive|paused|active` + CreationTime date labels); **atomic nested git**; taxonomy Continuity (**proposed-ratified — ready for user sign-off**, not global final); must-preserve Continuity (**draft — not auto-locked / for user review**); **90-day** status rule; **opaque `.env`** + fail-closed hazards; verify/rollback + INDEX current-path honesty. Saying **A** commits this cycle to those same rules. Saying **B** means you want to change something before moves (say what).

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Yes, Continuity still OK; do not re-open first-batch decisions | Fast; consistent with Cycle 4 archives | If you now dislike a rule, Medium remaining moves encode it again |
| **B** — Change something (say what) | Fits a new preference | Research/plan must redesign; risk of inconsistency with Cycle 4 destinations |

**Ask summary:** Keep Cycle 4 Continuity locks? Default A.

---

### Q4 — Soft-defer any of the “safer three” optional peers?

**Plain language:** Besides the higher-risk pair in Q2, you can also ask to leave one of `NextTest` / `Simpl_Next` / `PWAExempleTristan` at root this cycle (e.g. you know it is still in active use). Saying **A** commits to letting research pick among those three (subject to Q1 size). Saying **B** means you name soft-defers.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — No extra soft-defers; research may pick from the safer three | Simple; maximizes progress under Q1=A | A folder you still use daily might be proposed (you can still reject at plan gate) |
| **B** — Soft-defer named folders from the safer three (list them) | Protects active daily work | Shrinks the candidate pool; may force a 1-folder batch |

**Ask summary:** Extra soft-defer among safer three? Default A (none).

---

## Answers

User reply: **Choose all** for Q1–Q4. Disclosed defaults locked. **Plan gate still mandatory** before any moves — Choose all does **not** approve the from→to map.

| Q | Locked decision | Source | Rationale |
| --- | --- | --- | --- |
| 1 | **A** — Smaller subset (2–3 of remaining five); prefer safer three | `Choose all` | ROADMAP + disclosed default; safer progress |
| 2 | **A** — Soft-defer `NextPWATraining` + `CursorMobileWorkspace` | `Choose all` | Lower blast radius; secrets/tooling stay put |
| 3 | **A** — Keep Cycle 4 Continuity (layout/git/taxonomy/must-preserve/status/secrets/verify) | `Choose all` | Do not re-litigate first-batch locks |
| 4 | **A** — No extra soft-defer among safer three | `Choose all` | Research may pick all of `NextTest`, `Simpl_Next`, `PWAExempleTristan` |

**In-scope pool (locked):** `NextTest`, `Simpl_Next`, `PWAExempleTristan` — research/plan picks **2–3** (typically **all three** if live-check green).  
**Soft-deferred this cycle:** `NextPWATraining`, `CursorMobileWorkspace`.  
**Forbidden sources:** Cycle 4 peers `TestRyan`, `ReactRouterTest`, `Simpl`.

### Durable ask summary (one line per Q)

1. Subset (2–3) vs all five remaining vs name list?
2. Soft-defer NextPWATraining / CursorMobileWorkspace vs allow/force include?
3. Keep Cycle 4 Continuity locks (layout/git/taxonomy/must-preserve/status/secrets/verify)?
4. Extra soft-defer among safer three?

**Informed consent record:** Q1–Q4 were explained with plain language + pros/cons before Choose all; no jargon-only debt this phase. **Plan gate** remains a separate later approval.

## Continuity (locked — do not re-ask / do not re-litigate)

### Orchestrator locks (this cycle)

- ROADMAP row: **Medium wrappers** (**in progress**)
- Cycle id: **Cycle 5 — Medium wrappers (remaining)**
- Remaining at root (verified per orchestrator): `NextTest`, `Simpl_Next`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining`
- **Do not** re-propose / re-move: `TestRyan`, `ReactRouterTest`, `Simpl` (Cycle 4 → archive)
- **mutation_class:** `fs_mutation` with **mandatory user plan gate**
- Live-check INDEX vs disk in research; ignore stale INDEX paths for move decisions
- Do not touch must-preserve draft paths or organisation repo
- Git-strategy FAW **not** in scope unless user expands; worktrees/multi-remote → fail-closed / defer
- Early/simple **Complete** — do not reopen
- Q1–Q4 locked via **Choose all** (defaults A)

### Batch scope (Q1–Q2 / Q4 Choose all)

- In-scope pool: `NextTest`, `Simpl_Next`, `PWAExempleTristan` (2–3; typically all three if research green)
- Soft-deferred: `NextPWATraining`, `CursorMobileWorkspace`
- Nested git: move **wrapper + nested `.git` atomically**; no history rewrite
- Live-check INDEX vs disk in research

### From Cycle 4 Choose-all (Q3=A — locked Continuity)

- Layout: `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\`
- CreationTime wins for date labels; spaces kept
- Atomic nested git; no history rewrite
- Taxonomy: Continuity — **proposed-ratified — ready for user sign-off** (not global final)
- Must-preserve: **draft — not auto-locked / for user review**
- Status: archive default; LastWrite ≤90 days from `2026.09.09` → paused
- Opaque `.env` / secrets; fail-closed hazards
- Verify/rollback + INDEX current-path honesty
- Catalogue update after moves; propose map → user approves → execute
- Org repo protect; never delete payload to clean up

## Assumptions

- No agent git push / pull / remote publish this cycle.
- Hygiene / multi-experiment / Obsidian / ProjetOrif / special-git out of scope.
- Cycle 4 destinations stay put; catalogue may lag — research live-checks.
- Parent status folders may already exist; create if missing.
- In-scope pool is locked; exact destinations/statuses = research/plan until **plan gate**.
- Choose all locked scope/rules only — **not** move execution approval.
- Soft-deferred pair stays at root for a later Medium cycle (row stays in progress until they move or user changes scope).

## Open risks

- Nested `.git` / worktrees / multi-remote on a safer-three candidate → defer that item (fail-closed); batch may shrink below three.
- Target name collision under archive/paused/active → plan must detect before move.
- INDEX lag — do not treat stale paths as sources; do not re-move Cycle 4 archives.
- Soft-deferred higher-risk pair remains at root — Medium row not Complete after this cycle alone.

## Self-improvement backlog

None. Informed-consent explanations + pros/cons were present before Choose all.

## Key alignment changes (raw → refined)

- Raw `/full-agent-workflow next cycle` → **Cycle 5 Medium wrappers (remaining)** `fs_mutation`.
- User **Choose all** → Q1–Q4 defaults **A** locked (`Choose all`).
- In-scope: safer three (`NextTest`, `Simpl_Next`, `PWAExempleTristan`); soft-defer higher-risk pair; Continuity kept.
- Exact from→to map still requires **plan gate** (Choose ≠ move approval).
