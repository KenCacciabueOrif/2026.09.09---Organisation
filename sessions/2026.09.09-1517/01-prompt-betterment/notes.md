# Prompt betterment notes — Cycle 3

Session: `sessions/2026.09.09-1517/01-prompt-betterment/`  
Role: **Cycle 3 — Early/simple (remaining)** (`fs_mutation`).  
Roadmap row (orchestrator-locked): **Early/simple remaining**.

## Plain-language meaning of the gates

| Term | Everyday meaning |
| --- | --- |
| **Taxonomy** | Naming/filing rules: status bucket (`active` / `paused` / `archive`) + dated folder name like `2025.12.12 - IA`. |
| **Must-preserve** | Hands-off list of important folders. Early/simple remaining folders are **not** on that list; we still must not touch items that are. |
| **Plan gate** | After planning, you see a concrete **from → to** list and say yes **before** any move. Starting this cycle is not that yes. |
| **fs_mutation** | This cycle will move/rename real folders on disk (after plan gate), not only edit docs. |
| **Fail-closed** | If something unexpected appears (e.g. a hidden `.git`), we **stop that item** instead of guessing. |

## Clarifying questions (asked — answered via Choose all)

Each question included plain-language explanation + pros/cons. User replied **Choose** (treated as **Choose all** for Q1–Q6). Ask summaries retained below for later phases.

---

### Q1 — Reuse Cycle 2 filing patterns?

**Plain language:** Keep the same filing system as Cycle 2 for these remaining folders: put them under `C:\Project\{archive|paused|active}\yyyy.mm.dd - Name`, use CreationTime for the date in the name, update the catalogue after moves, and stop (fail-closed) if a folder unexpectedly has git history. Saying **yes** commits this cycle to those rules.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Reuse Cycle 2 patterns | Consistent tree; less re-decide; matches prior consent | Wrong if you now want a different layout |
| **B** — Change something (say what) | Fits a new preference | Research/plan must redesign; more risk of inconsistency |

**Ask summary:** Reuse Cycle 2 layout/dates/fail-closed/catalogue? Default A.

---

### Q2 — Move all three remaining folders this cycle?

**Plain language:** Orchestrator locked remaining Early/simple as `IA`, `AngularTest`, `epsic`. **All three** means research/plan/implement target those three (each still needs plan-gate yes). A **subset** means fewer moves now and the rest wait for another cycle.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — All three: `IA`, `AngularTest`, `epsic` | Finishes Early/simple row; one plan gate | Larger batch (esp. M-band AngularTest / epsic) |
| **B** — Subset only (name which) | Smaller risk surface | Leaves Early/simple incomplete |
| **C** — Docs-only / no moves this session | Zero disk risk | Does not advance remaining moves (conflicts with locked `fs_mutation` intent — only pick if you want to abort move goals) |

**Ask summary:** In-scope batch = all three remaining? Default A.

---

### Q3 — Keep Early/simple taxonomy rules binding?

**Plain language:** Cycle 2 already treated the naming rules as binding for Early/simple moves (not “final forever for the whole disk”). **Continue** means we use those same rules for IA / AngularTest / epsic. **Pause for edits** means we stop moves until you change taxonomy docs.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Continue Cycle 2 Early/simple binding | Fast continuity; same look as archive/paused siblings | If you dislike the naming, moves encode it again |
| **B** — Pause; I want taxonomy edits first | Fixes rules before more moves | Blocks this `fs_mutation` cycle until edits + new approval |

**Ask summary:** Taxonomy continuity for Early/simple? Default A.  
Status language if A: **proposed-ratified — ready for user sign-off** remains; may note **user-validated for Early/simple (2026.09.09)** continuity — **not** global final corpus ratification.

---

### Q4 — Must-preserve draft: still hands-off?

**Plain language:** The must-preserve draft is the hands-off list (Obsidian, ProjetOrif, org repo, etc.). Confirm we **do not move** anything on that list, and that `IA` / `AngularTest` / `epsic` are **allowed** to move only after you approve the plan map.

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Leave draft untouched; these three OK after plan gate | Protects critical trees; unblocks Early/simple | Draft still not a final forever lock for later cycles |
| **B** — I want to edit must-preserve before any move | Safer if a folder should be protected | Blocks moves until review/waiver |

**Ask summary:** Must-preserve draft unchanged; batch not on list? Default A.

---

### Q5 — Status rule (archive vs paused)?

**Plain language:** Which status bucket each folder lands in. Cycle 2 rule: Early/simple experiments default **archive**; if LastWrite is within **90 days** of cycle date `2026.09.09`, use **paused** instead. Research assigns per folder from inventory timestamps (catalogue suggests all three LastWrites are older → likely all **archive**; research must re-verify).

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Same 90-day rule; research proposes statuses in the plan | Consistent with Cycle 2; data-driven | You might prefer a folder “active” or always archive |
| **B** — Force all three → `archive` | Simple cold storage | Recent work (if any) looks “dead” |
| **C** — Force all three → `paused` | Keeps them more visible | Crowds paused; weaker archive signal |
| **D** — I’ll name status per folder | Full control | You must specify three statuses |

**Ask summary:** Status assignment rule? Default A.

---

### Q6 — Verification / rollback same as Cycle 2?

**Plain language:** Done means: sources exist then gone; targets absent then present; unexpected `.git` → skip + log; catalogue INDEX (and inventory if planned) updated; implementation log includes each move and how to reverse it; never delete payload to “clean up.”

| Option | Pros | Cons / tradeoffs |
| --- | --- | --- |
| **A (default)** — Same verify + reverse-move logging | Auditable; recoverable | Slightly more logging work |
| **B** — Stricter (say what extra checks) | More confidence | Slower; may over-specify |
| **C** — Lighter checks | Faster | Harder rollback / audit |

**Ask summary:** Keep Cycle 2 verify/rollback? Default A.

---

## Answers

User reply: **Choose** → treated as **Choose all** for Q1–Q6. Disclosed defaults locked. **Plan gate still mandatory** before any moves — Choose all does **not** approve the from→to map.

| Q | Locked decision | Source | Rationale |
| --- | --- | --- | --- |
| 1 | **A** — Reuse Cycle 2 patterns (layout, CreationTime, fail-closed, catalogue after moves) | `Choose` / `Choose all` | Continuity with Cycle 2; reversible preference vs redesign |
| 2 | **A** — All three: `IA`, `AngularTest`, `epsic` | `Choose` / `Choose all` | Finishes Early/simple remaining row in one batch |
| 3 | **A** — Taxonomy continuity: Early/simple binding; **proposed-ratified — ready for user sign-off**; may note **user-validated for Early/simple (2026.09.09)** continuity — **not** global final corpus ratification | `Choose` / `Choose all` | Same naming rules as Cycle 2 siblings |
| 4 | **A** — Must-preserve draft untouched (**draft — not auto-locked / for user review**); batch OK only after plan gate | `Choose` / `Choose all` | Protect hands-off list; unblock Early/simple |
| 5 | **A** — Same 90-day status rule: default `archive`; LastWrite ≤90 days of `2026.09.09` → `paused`; research proposes per folder | `Choose` / `Choose all` | Data-driven; consistent with Cycle 2 |
| 6 | **A** — Same verify/rollback as Cycle 2 (pre/post paths, fail-closed `.git`, INDEX/inventory, reverse-move log; never delete payload) | `Choose` / `Choose all` | Auditable recovery path |

### Durable ask summary (one line per Q)

1. Reuse Cycle 2 layout/dates/fail-closed/catalogue?
2. In-scope batch = all three remaining?
3. Taxonomy continuity for Early/simple?
4. Must-preserve draft unchanged; batch not on list?
5. Status assignment rule (90-day)?
6. Keep Cycle 2 verify/rollback?

**Informed consent record:** Questions were explained with plain language + pros/cons before Choose; no jargon-only debt this phase.

## Continuity (locked — do not re-ask / do not re-litigate)

### Orchestrator locks (this cycle)

- ROADMAP row: **Early/simple remaining**
- Cycle id: **Cycle 3 — Early/simple (remaining)**
- Folders: `IA`, `AngularTest`, `epsic` under `C:\Project` (bootstrap-verified present)
- Already moved Cycle 2: PostManResponses + PlayTestTristan → archive; ZedTest → paused (research **re-verify** ZedTest location — INDEX may lag; **do not re-move** if already at paused path)
- **mutation_class:** `fs_mutation` with **mandatory user plan gate**
- Do not touch must-preserve draft paths or organisation repo
- Git-strategy **not** required for no-git Early/simple

### From Cycle 2 (locked via Q1–Q6 Choose all)

- Layout: `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\`
- CreationTime wins for date labels; spaces kept
- Archive default + recent LastWrite (≤90 days from `2026.09.09`) → paused
- No-git fail-closed; catalogue update after moves
- Propose map → user approves → execute; prior cycle approval ≠ this batch
- Org repo protect; secrets opaque; never delete payload to clean up
- In-scope move candidates: `IA`, `AngularTest`, `epsic` only (plus ZedTest verify / corrective if still at root)

### Prior program continuity

- End-state: dated view + next + navigation; no functionality/info loss
- Git roots atomic; git-strategy before Obsidian / ProjetOrif / worktrees
- Taxonomy: Early/simple binding continuity — **not** “final forever” whole-corpus claim
- Must-preserve: **draft — not auto-locked / for user review**

## Assumptions

- No agent git push / pull / remote publish this cycle.
- Hygiene orphans and other ROADMAP rows out of scope.
- Cycle 2 targets stay where they are; only remaining three are move candidates (plus ZedTest location check for catalogue honesty).
- Parent status folders may already exist from Cycle 2; create if missing.
- Catalogue date-label hypotheses: AngularTest `2025.08.07`, epsic `2025.12.10`, IA `2025.12.12` — research must confirm CreationTime before plan finalizes.
- Choose all locked scope/rules only — **not** move execution approval.

## Open risks

- Unexpected `.git` in a catalogue “no-git” folder → skip fail-closed.
- Target name collision under archive/paused → plan must detect before move.
- AngularTest / epsic are M-band (larger) than Cycle 2 S-band — longer moves / more collision surface.
- INDEX lag on ZedTest → research must not “move again” if already at paused path.

## Self-improvement backlog

None new beyond continuity of informed-consent asks (explanations + pros/cons) — already applied this phase.

## Key alignment changes (raw → refined)

- Raw `/full-agent-workflow next cycle` → **Cycle 3 Early/simple remaining** `fs_mutation` for `IA`, `AngularTest`, `epsic`.
- User **Choose** → all Q1–Q6 defaults locked (`Choose` / `Choose all`).
- Cycle 2 patterns, taxonomy Early/simple binding, must-preserve draft hands-off, 90-day status, verify/rollback — **final for this cycle**.
- ZedTest: **verify only** (unless still at old root — then plan may propose corrective move).
- **Plan gate still required** before implementer; Choose ≠ move map approval.
