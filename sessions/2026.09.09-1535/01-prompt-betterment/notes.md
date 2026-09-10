# Prompt betterment notes — Cycle 4 Medium wrappers (first subset)

Session: `sessions/2026.09.09-1535/01-prompt-betterment/`  
Role: **Cycle 4 — Medium wrappers (first subset)** (`fs_mutation`).  
Roadmap row (orchestrator-locked): **Medium wrappers** (Primary next — Early/simple **Complete**, do not reopen).

## Plain-language meaning of the gates

| Term | Everyday meaning |
| --- | --- |
| **Taxonomy** | Naming/filing rules: status bucket (`active` / `paused` / `archive`) + dated folder name like `2025.xx.xx - NextTest`. |
| **Must-preserve** | Hands-off list of important folders. Medium wrappers are **not** on that list; we still must not touch items that are. |
| **Plan gate** | After planning, you see a concrete **from → to** list and say yes **before** any move. Starting this cycle / Continuity / Choose all is not that yes. |
| **fs_mutation** | This cycle will move/rename real folders on disk (after plan gate), not only edit docs. |
| **Fail-closed** | If something unexpected appears (e.g. worktrees / multi-remote hazards), we **stop that item** instead of guessing. |
| **Atomic nested git** | Move the whole top-level folder **including** its inner `.git` as one piece — no history rewrite, no splitting wrapper from repo. |

## Clarifying questions (asked — answered via Choose all)

Each question included plain-language explanation + pros/cons. User replied **Choose all** for Q1–Q7. Disclosed defaults locked. **Plan gate still mandatory** — Choose all does **not** approve the from→to map.

---

### Q1 — Small first subset vs all eight Medium wrappers?

**Plain language:** The ROADMAP lists eight folders still at `C:\Project` root. A **small first subset** means research/plan/implement target only **2–3** of them this cycle (agent proposes which after research unless you name them). **All eight** means one bigger move batch (still one plan gate). Saying **A** commits to a smaller risk surface now and leaves the rest for a later Medium cycle.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Small first subset (2–3 folders; prefer no nested-git hazard / simpler trees; agent may propose which after research) | Safer; faster review; learns Medium pattern before scaling | Leaves five+ wrappers at root for later |
| **B** — All eight this cycle | Finishes Medium row sooner | Larger plan gate; more collision / hazard surface |
| **C** — I’ll name exact folders (list them) | Full control of batch | You must specify names; may conflict with hazard findings |
| **D** — Docs-only / no moves this session | Zero disk risk | Does not advance Medium moves (conflicts with locked `fs_mutation` intent — only if you want to abort move goals) |

**Ask summary:** Subset (2–3) vs all eight vs name list? Default A.

---

### Q2 — Reuse Early/simple filing patterns for Medium wrappers?

**Plain language:** Keep the same physical layout as Cycles 2–3: `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\`, CreationTime for the date in the name, update catalogue after moves. For Medium: move **wrapper + nested `.git` together** (atomic). Saying **yes** commits this cycle to those rules unless research finds a hazard → fail-closed / defer that item.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Reuse Early/simple layout + CreationTime + catalogue + atomic nested git | Consistent tree; less re-decide | Wrong if you now want a different Medium layout |
| **B** — Change something (say what) | Fits a new preference | Research/plan must redesign; more inconsistency risk |

**Ask summary:** Reuse Early/simple layout/dates/catalogue + atomic nested git? Default A.

---

### Q3 — Taxonomy Continuity (brief — not “final forever”)?

**Plain language:** Early/simple already used the naming rules as **binding for those moves**, not as forever law for the whole disk. **Continuity** means use the same taxonomy rules for Medium renames/moves this cycle. **Pause** means stop moves until you edit taxonomy docs. We will **not** claim global final ratification unless you explicitly sign off.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Continuity: same taxonomy rules for Medium this cycle; status stays **proposed-ratified — ready for user sign-off** (not global final) | Fast; same look as archive/paused siblings | If you dislike naming, Medium moves encode it again |
| **B** — Pause; I want taxonomy edits / explicit global sign-off first | Fixes rules before more moves | Blocks this `fs_mutation` cycle until edits + new approval |
| **C** — Explicitly sign off taxonomy as final for the program now | Clears the open gate | Commits naming rules more broadly; harder to unwind |

**Ask summary:** Taxonomy Continuity for Medium? Default A.

---

### Q4 — Must-preserve draft Continuity?

**Plain language:** The must-preserve draft is the hands-off list (Obsidian, ProjetOrif, org repo, etc.). Confirm we **do not move** anything on that list, and that the Medium candidates are **allowed** to move only after you approve the plan map. Draft stays **draft — not auto-locked / for user review** unless you choose otherwise.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Continuity: leave draft untouched; Medium batch OK after plan gate | Protects critical trees; unblocks Medium | Draft still not a final forever lock |
| **B** — I want to edit must-preserve before any move | Safer if a Medium folder should be protected | Blocks moves until review/waiver |
| **C** — Explicitly lock/sign off must-preserve list now | Stronger protection claim | Broader commitment; may over-lock |

**Ask summary:** Must-preserve Continuity; Medium not on list? Default A.

---

### Q5 — Status rule (archive vs paused vs active)?

**Plain language:** Which status bucket each folder lands in. Early/simple rule: experiments default **archive**; if LastWrite is within **90 days** of cycle date `2026.09.09`, use **paused**. Research assigns per folder. Medium wrappers may still be “recent” training apps — research may propose `paused` or rarely `active` under the same rule unless you force a policy.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Same 90-day rule; research proposes statuses in the plan | Consistent with Early/simple; data-driven | You might prefer all Medium → paused/active |
| **B** — Prefer `paused` for any Medium with nested git + recent activity (override archive default when LastWrite ≤90 days still applies; if older, still archive unless you say otherwise) | Keeps learnable apps more visible | Crowds paused |
| **C** — Force all in-batch → `archive` | Simple cold storage | Recent training work looks “dead” |
| **D** — I’ll name status per folder | Full control | You must specify each |

**Ask summary:** Status assignment rule? Default A.

---

### Q6 — Secrets / NextPWATraining `.env` + nested git hazards?

**Plain language:** For **NextPWATraining** (and any sibling with secrets): **do not read** `.env` / secret files; still **include** them in the move. Nested `.git` moves with the wrapper. If research finds **worktrees / multi-remote / unusual git hazards**, **fail-closed** — defer that item (no dedicated git-strategy FAW unless you expand scope). Saying **A** commits to opaque secrets + atomic git + defer-on-hazard.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Opaque secrets; atomic wrapper+`.git`; fail-closed / defer hazard items; no history rewrite | Safe default; matches ROADMAP | Deferred items stay at root until a later cycle |
| **B** — If hazard found, pause whole batch for git-strategy FAW first | Safer for complex git | Blocks even safe siblings |
| **C** — I’ll specify exceptions | Flexible | You must name them; easy to under-specify |

**Ask summary:** Opaque `.env` + atomic git + fail-closed hazards? Default A.

---

### Q7 — Verification / rollback same as Early/simple?

**Plain language:** Done means: sources exist then gone; targets absent then present; nested `.git` still present under the new wrapper path; unexpected hazards → skip + log; catalogue INDEX (and inventory if planned) updated with **current paths**; implementation log includes each move and how to reverse it; never delete payload to “clean up.” Live-check INDEX vs disk in research (ignore stale Early/simple INDEX paths for this batch).

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Same verify + reverse-move logging + INDEX current-path honesty | Auditable; recoverable | Slightly more logging work |
| **B** — Stricter (say what extra checks) | More confidence | Slower; may over-specify |
| **C** — Lighter checks | Faster | Harder rollback / audit |

**Ask summary:** Keep Early/simple verify/rollback + INDEX honesty? Default A.

---

## Answers

User reply: **Choose all** for Q1–Q7. Disclosed defaults locked. **Plan gate still mandatory** before any moves — Choose all does **not** approve the from→to map.

| Q | Locked decision | Source | Rationale |
| --- | --- | --- | --- |
| 1 | **A** — Small first subset (2–3); research proposes which (prefer simpler / lower hazard) | `Choose all` | ROADMAP + orchestrator default; safer first Medium slice |
| 2 | **A** — Reuse Early/simple layout/CreationTime/catalogue + atomic nested git | `Choose all` | Continuity; consistent tree |
| 3 | **A** — Taxonomy Continuity; **proposed-ratified — ready for user sign-off**; not global final | `Choose all` | Brief Continuity; do not re-block forever |
| 4 | **A** — Must-preserve Continuity; **draft — not auto-locked / for user review**; Medium OK after plan gate | `Choose all` | Hands-off list; unblock Medium |
| 5 | **A** — Same 90-day status rule; research proposes per folder | `Choose all` | Data-driven Continuity |
| 6 | **A** — Opaque `.env`; atomic git; fail-closed/defer hazards; no rewrite | `Choose all` | Safety for NextPWATraining + nested repos |
| 7 | **A** — Same verify/rollback + INDEX live-check honesty | `Choose all` | Auditable recovery |

### Durable ask summary (one line per Q)

1. Subset (2–3) vs all eight vs name list?
2. Reuse Early/simple layout/dates/catalogue + atomic nested git?
3. Taxonomy Continuity for Medium (not final forever)?
4. Must-preserve Continuity; Medium not on list?
5. Status assignment rule (90-day)?
6. Opaque `.env` + atomic git + fail-closed hazards?
7. Keep Early/simple verify/rollback + INDEX honesty?

**Informed consent record:** Questions were explained with plain language + pros/cons before Choose all; no jargon-only debt this phase.

## Continuity (locked — do not re-ask / do not re-litigate)

### Orchestrator locks (this cycle)

- ROADMAP row: **Medium wrappers** (Primary next)
- Cycle id: **Cycle 4 — Medium wrappers (first subset)**
- Candidate set (all still at `C:\Project` root per bootstrap): `NextTest`, `Simpl`, `Simpl_Next`, `TestRyan`, `ReactRouterTest`, `PWAExempleTristan`, `CursorMobileWorkspace`, `NextPWATraining`
- Batch shape (Q1=A): **small first subset** (2–3); research proposes which (prefer simpler / lower hazard)
- **mutation_class:** `fs_mutation` with **mandatory user plan gate**
- Nested git: move **wrapper + nested `.git` atomically**; no history rewrite
- NextPWATraining: `.env` opaque (do not read; include in move)
- Git-strategy FAW **not** required for typical single-nested Medium wrappers; worktrees/multi-remote → fail-closed / defer
- Early/simple is **Complete** — do not reopen that row’s finished scope
- Live-check INDEX vs disk in research; ignore stale Early/simple INDEX paths for this batch’s move decisions
- Do not touch must-preserve draft paths or organisation repo

### From Early/simple (Cycles 2–3) — locked via Q2–Q7 Choose all

- Layout (Q2=A): `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\`
- CreationTime wins for date labels; spaces kept
- Archive default + recent LastWrite (≤90 days from `2026.09.09`) → paused (Q5=A)
- Catalogue update after moves; propose map → user approves → execute
- Org repo protect; secrets opaque; never delete payload to clean up
- Taxonomy (Q3=A): Continuity binding for Medium this cycle — **proposed-ratified — ready for user sign-off** — **not** “final forever” whole-corpus claim
- Must-preserve (Q4=A): **draft — not auto-locked / for user review**
- Verify/rollback (Q7=A): pre/post paths, nested `.git` intact, INDEX current-path honesty, reverse-move log

## Assumptions

- No agent git push / pull / remote publish this cycle.
- Hygiene orphans, multi-experiment, Obsidian, ProjetOrif, special-git rows out of scope.
- Early/simple destinations stay where they are (catalogue may lag — research live-checks; no re-move if already correct).
- Parent status folders may already exist; create if missing.
- Exact 2–3 subset membership is a **research proposal** under Q1=A; shortlist accepted only at **plan gate**.
- Choose all locked scope/rules only — **not** move execution approval.

## Open risks

- Nested `.git` / worktrees / multi-remote on a candidate → defer that item (Q6=A).
- Target name collision under archive/paused/active → plan must detect before move.
- NextPWATraining secrets: accidental read of `.env` must be prevented if that folder is in the shortlist.
- INDEX lag on Early/simple — do not treat stale paths as Medium move targets.
- Research shortlist of 2–3 may still include hazard items that then get deferred — plan must not silently expand to fill quota with unapproved extras without plan-gate visibility.

## Self-improvement backlog

None. Informed-consent explanations + pros/cons were present before Choose all.

## Key alignment changes (raw → refined)

- Raw `/full-agent-workflow next cycle` → **Cycle 4 Medium wrappers (first subset)** `fs_mutation`.
- User **Choose all** → Q1–Q7 defaults **A** locked (`Choose all`).
- Early/simple **not** reopened; Primary next locked.
- Small subset + atomic nested git + opaque `.env` + Continuity taxonomy/must-preserve + 90-day status + verify/rollback — **final for this cycle**.
- Exact 2–3 folder shortlist = research proposal → **plan gate** (Choose ≠ move map approval).
