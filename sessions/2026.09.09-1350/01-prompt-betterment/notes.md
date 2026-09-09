# Prompt betterment notes

**Phase status:** COMPLETE — Answers locked; `refined-prompt.md` finalized.

**Cycle:** Pull-autonomy — fix dirty-tree deadlock for agent git pull/push, then pull again  
**Mutation class:** `docs_only` (agents/skills/rules/templates + git ops; no corpus moves)  
**Session:** `sessions/2026.09.09-1350/01-prompt-betterment/`  
**Prior session:** `sessions/2026.09.09-1332/` — blocked `dirty_working_tree` under Q3=A abort; introduced `pull-cycle.md`

## Informed consent

Questions were presented with plain-language explanation + pros/cons (`questions-for-user.md`) before the user replied. User answered **"Choose"** → every Q1–Q9 (incl. Q3/Q3b) resolved via disclosed defaults. No jargon-explanation debt.

## Continuity (locked — do not re-ask)

| Lock | Value | Source |
| --- | --- | --- |
| Git root | Org-repo only: `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` — never sibling `C:\Project` | Prior + orchestrator |
| Preferred remote/branch | `origin` / `main` ↔ `origin/main` | Prior Q1 A + this Q1 A |
| Windows git | Dual preflight; prefer Git for Windows + GCM when PATH git is MSYS without helper; **same binary** for dirty gate + pull/push | Continuity |
| Who must succeed | Agent Shell (not “user terminal OK”) | Q5 A |
| On hard failure | Fail-closed + typed `blocker_type` + still self-improver; **no** force push / hard reset / `--no-verify` | Q6 A + hard AC |
| Taxonomy / must-preserve | OUT OF SCOPE — not blockers | Orchestrator |
| User intent | Agent completes pull/push cycles without user cleanup of FAW session dirt; then same-session pull | Raw goal |

## Answers

| Q | Decision | Source | Rationale |
| --- | --- | --- | --- |
| Q1 | **A** — pull `origin` into `main` / tracking `origin/main` | Choose | Continuity; usual sync target |
| Q2 | **A** — `git pull --ff-only` after tree is pullable | Choose | Fail-closed on divergence; no surprise merge |
| Q3 | **E→B** — auto-commit **allowlisted** dirt (`sessions/**` + FAW meta), then pull; **abort** only for unrelated dirty | Choose | Fixes FAW dirty deadlock without silent stash; abort remains for surprise paths |
| Q3b | **A** — fail-closed on conflict; keep WIP commit recoverable; never stash-drop / force / hard reset | Choose | No silent data loss |
| Q4 | **A** — org-repo git root only | Choose | Hard AC |
| Q5 | **A** — agent Shell pull must succeed (dual preflight; GfW if needed) | Choose | Proves autonomy in agent env |
| Q6 | **A** — fail-closed + typed `blocker_type` + still self-improver | Choose | Safe recovery; clear audit |
| Q7 | **A** — full FAW artifacts under this session | Choose | Auditor/self-improver need full trail |
| Q8 | **A** — update workflow docs/defaults **first**, then **same-session** agent pull under new rules | Choose | One cycle delivers both asks |
| Q9 | **A** — mirror pull autonomy on publish for session/FAW-meta allowlist; abort still for unrelated dirty | Choose | Coherent pull/push rule |

User phrase: **"Choose"** → Source for each row: `Choose` (equivalent to Choose / unanswered→default on disclosed defaults). **No Choose decision differs from the expected defaults listed by the orchestrator.**

### Locked FAW dirty allowlist (encode in AC)

Auto-commit **only** these paths when making the tree pullable/pushable (BOM-safe message; no secrets):

1. `sessions/**` (including this session and any other local session dirt)
2. FAW meta allowlist:
   - `.cursor/skills/full-agent-workflow/**`
   - `.cursor/agents/**`
   - `.cursor/rules/full-agent-workflow.mdc` (and other `.cursor/rules/**` only if dirty from this cycle’s workflow edits)
   - `AGENTS.md`
   - `sessions/_templates/**` (if present and dirty)

**Unrelated dirty** (anything outside this allowlist, e.g. `catalogue/**`, `program/**`, user project edits not in allowlist) → **abort** with `blocker_type: dirty_working_tree`, list paths, no stash, no commit-all — session `blocked`; self-improver still runs.

## Assumptions

- Mutation stays docs_only + git ops; no catalogue corpus moves.
- Secrets never logged or committed intentionally.
- Prior pull-cycle Q3=A abort-default is **replaced** for FAW by allowlisted auto-commit; abort remains for non-allowlist dirt.
- “Small local project changes” outside the allowlist are **not** auto-committed; they correctly block until user handles them or a future cycle widens scope — per Choose E→B.
- Same-session pull uses the **updated** policy after docs land.

## Open risks

- Non-allowlist dirty (user’s small project edits outside allowlist) → pull still blocks by design.
- Local commits ahead of / diverged from `origin/main` → `--ff-only` fails → Q3b/Q6 fail-closed (`blocked`), not force.
- Auto-commit on `main` adds history; path-scoped reduces blast radius.
- Implementer must apply doc updates before pull AC in one session (ordering risk if interrupted).

## Jargon-explanation debt

None — questions explained before Choose.

## Key alignment changes (raw → refined)

- Raw: fix dirty deadlock so agent can pull/push without user, then pull again.
- Refined: Update pull (+ publish mirror) dirty policy to **allowlisted auto-commit then `--ff-only`**; abort only for unrelated dirty; fail-closed conflicts; same-session: land docs → agent auto-commit allowlist if needed → agent Shell pull with GfW+GCM.
