# Prompt betterment notes

Session: `sessions/2026.09.09-1032/01-prompt-betterment/`  
Role: **Cycle 2 — Early/simple subset** (`fs_mutation`).  
Roadmap row (orchestrator-locked): **Early/simple**.

## Plain-language meaning of the gates (user was confused by jargon)

| Gate jargon | What it actually means |
| --- | --- |
| **Taxonomy** | The naming and filing rules: folders get names like `2025.10.01 - PostManResponses`, and live under a status bucket (`active` / `paused` / `archive`). “Proposed-ratified” meant: agents wrote the rules; we still needed your OK before using them for real moves. |
| **Must-preserve** | A “hands off” list of important folders (Obsidian, ProjetOrif, org repo, …). We must not move those casually. Your Early/simple test folders are **not** on that list. |
| **Plan gate** | After research/planning, you see a concrete **from → to** move list and say yes before any folder is moved. Saying “do the cycle” earlier is **not** that yes. |
| **fs_mutation** | This cycle will change real folders on disk (move/rename), not only docs — but only after the plan gate. |
| **Fail-closed** | If something unexpected appears (e.g. a hidden `.git`), we **stop that item** instead of guessing. |

Consent captured below is **informed enough for this cycle** given your “okay / validating the plan,” while noting questions lacked explanations (workflow debt).

## Clarifying questions (answered — do not re-ask)

Original options omitted; see Answers.

## Answers

1. **Taxonomy — consent for this cycle**  
   User was unclear on jargon but said **okay and explicitly validating the plan.**  
   **Locked:** Use Cycle 1 **proposed-ratified** taxonomy rules as **binding** for Early/simple renames/moves this cycle (canonical `yyyy.mm.dd - ShortName`, CreationTime dates from catalogue, status axis separate).  
   **Upgrade path (post-cycle, implementer/docs OK):** may record **“user-validated for Early/simple (2026.09.09)”** on taxonomy/session artefacts.  
   **Do not claim:** user understood every taxonomy term at ask-time, or permanent “final forever” ratification of the whole corpus taxonomy.  
   **Workflow debt:** questions lacked plain-language explanation (see Self-improvement backlog).

2. **Must-preserve — consent for this cycle**  
   Same validating-the-plan consent.  
   **Locked:** Cycle 2 Early/simple **batch folders are not must-preserve** and may be moved after plan approval. Draft list (Obsidian, ProjetOrif, WebCatalogue, WorkSpace, HTTP Battles, optional CursorMobileWorkspace / NextPWATraining, …) **remains draft** for later cycles — **do not touch**. Organisation repo stays **protect**.

3. **Choose → Propose + execute after in-session plan approval**  
   **Locked:** Research + plan produce move map → **mandatory user plan gate** (explicit batch map approval) → then implementer executes. No moves before that yes.

4. **Agent choose → layout + status (decided)**  
   **Layout:** `C:\Project\{archive|paused|active}\yyyy.mm.dd - ShortName\`  
   Create `archive` / `paused` / `active` parent folders under `C:\Project` if missing.  
   **Status rule (locked):** For Early/simple experiments/snippets default **`archive`**. Exception: if inventory **LastWrite** is within **90 days** of the cycle date (`2026.09.09`), assign **`paused`** instead (recent enough to keep out of cold archive).  
   **This subset:**
   | Folder | Status | Target |
   | --- | --- | --- |
   | `PostManResponses` | `archive` | `C:\Project\archive\2025.10.01 - PostManResponses` |
   | `PlayTestTristan` | `archive` | `C:\Project\archive\2025.06.23 - PlayTestTristan` |
   | `ZedTest` | `paused` | `C:\Project\paused\2026.06.30 - ZedTest` |

   Rationale for ZedTest → `paused`: inventory LastWrite `2026-07-01` (~70 days before cycle date) → within 90-day rule. Others older → `archive`.

5. **Subset — agent chooses smallest/safest first batch**  
   **In scope (3 folders):** `PostManResponses`, `PlayTestTristan`, `ZedTest`  
   **Why:** S-band / ~0–0.18 size, no-git per catalogue, lowest risk for first real moves.  
   **Deferred to a later Early/simple cycle:** `IA`, `AngularTest`, `epsic` (IA is tiny but grouping keeps first batch to three clearest low-risk; AngularTest M-band zip extract; epsic M-band course-like).

6. **Default verification/rollback OK**  
   Pre/post path existence; no unexpected `.git` or skip fail-closed; update `catalogue/INDEX.md` (+ inventory as needed); session implementation log includes each move and **reverse-move** notes; never delete payload to clean up.

### Agent decisions on “Choose” (final)

| Q | Decision | Notes |
| --- | --- | --- |
| 3 | Propose + execute after plan approval | User Choose |
| 4 | status×date layout; archive-default + 90-day → paused | User “agent choose”; ZedTest → paused |
| 5 | Subset of 3: PostManResponses, PlayTestTristan, ZedTest | User asked subset; agent picked safest |

## Continuity locks (do not re-ask)

From Cycle 0 + Cycle 1 + this Answers block:

- End-state: dated view + next + navigation; no functionality/info loss
- Naming: `yyyy.mm.dd - ShortName`; CreationTime wins for date labels
- Status axis: `active` / `paused` / `archive` (+ protect / hygiene)
- Moves only after **per-batch** plan approval
- Git roots atomic; git-strategy before Obsidian / ProjetOrif / worktrees
- Org repo protect; secrets opaque
- Taxonomy: **binding for this Early/simple cycle**; upgrade label allowed as “user-validated for Early/simple (2026.09.09)” — not global final forever
- Must-preserve: **draft** unchanged; Early/simple subset not on list

### Orchestrator locks (this cycle)

- ROADMAP row: **Early/simple**
- Cycle id: **Cycle 2 — Early/simple**
- **mutation_class:** `fs_mutation` on **subset of 3** only
- Fail-closed on unexpected `.git`
- Do not touch must-preserve draft paths or organisation repo

## Assumptions

- No agent git push / remote publish this cycle.
- Hygiene orphans out of scope.
- Deferred three folders stay at current `C:\Project\…` paths until a later cycle.
- Parent status folders may be created empty as needed.

## Open risks

- Unexpected `.git` in a “no-git” folder → skip that item fail-closed.
- Target name collision under `archive`/`paused` → plan must detect before move.
- User validated plan without full jargon literacy → mitigate via self-improver explanations debt; still honour consent for this batch.
- Partial execute without reverse-move log → harder rollback.

## Self-improvement backlog (MANDATORY for phase 06 this session)

**Item:** Agents currently assume the user already understands gate jargon and options. **Change the workflow** so clarifying questions always include:

1. A short **plain-language explanation** of what is being asked (and what “yes” commits to).
2. **Pros / cons (or tradeoffs)** for each option so the user can give **informed consent**.

**Touch targets (self-improver implements — not this phase):**  
`prompt-betterment` agent definition, orchestrator handoffs / skill (`full-agent-workflow`), and related templates so every future FAW pause asks explained questions with tradeoffs.

**Do not** edit those agent/skill files in prompt-betterment or implementer; leave for **self-improver** at cycle end.

## Key alignment changes (raw → refined)

- Gates answered: taxonomy + must-preserve consent for this cycle; plan-then-execute; status×date; subset of 3; default verify/rollback.
- Full six → **smallest safe three**; IA / AngularTest / epsic deferred.
- ZedTest → **paused**; other two → **archive** under locked 90-day rule.
- Workflow debt flagged for self-improver: explanations + pros/cons on all clarifying questions.
