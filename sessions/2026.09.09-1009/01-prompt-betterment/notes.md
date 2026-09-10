# Prompt betterment notes

Session: `sessions/2026.09.09-1009/01-prompt-betterment/`  
Role: **Cycle 1 — Docs follow-ups** (`docs_only`).  
Roadmap row (orchestrator-locked): **Docs follow-ups**.

## Clarifying questions

Answered — do not re-ask. (Original text in `online-prompt-tips.md`.)

## Answers

1. **Status axis:** Keep `active` / `paused` / `archive` (+ `protect` / `hygiene` for special INDEX rows). Not PARA-lite.
2. **ShortName:** Keep spaces (`yyyy.mm.dd - ShortName`).
3. **Wrapper vs nested git:** User “Choose” → locked docs rule: **canonical dated label on the wrapper** (top-level move unit); nested `.git` trees = **child atomic units** inside. Proposed-ratified pending Q7 sign-off. Empty-parent / multi-root edges may stay “classify before move.”
4. **Date conflicts:** **CreationTime wins** as default for proposed labels (over earliest commit / LastWrite). User memory can override later if stated.
5. **Inventory deepen:** User “Choose” → include size bands + clearer git-root notes + LastWrite-as-activity hints where cheap; skip expensive/risky (no secret reads, no deep `node_modules` docs).
6. **Must-preserve:** User “Choose” → agent proposes **draft** candidate list for user review (not auto-locked).
7. **Ratify DoD:** (a) produce **proposed-ratified** taxonomy ready for user sign-off — do **not** claim final ratification without explicit follow-up approval.
8. **Next ROADMAP suggestion:** User “Choose” → **primary next:** Early/simple (move-prep / first simple batch after approval). **Git-strategy** remains hard gate before Obsidian / ProjetOrif / worktrees (reminder, not primary next row).

## Continuity (locked — do not re-ask)

From Cycle 0 (`sessions/2026.09.09-0929/`):

- End-state: dated view + next + navigation; no functionality/info loss
- Naming: `yyyy.mm.dd - name`
- Moves: agent-executed only after per-batch approval
- Git roots atomic; dedicated git-strategy before Obsidian / ProjetOrif / worktree moves
- Index/docs in org repo; material under `C:\Project`
- Inventory: no deep dep/cache docs; secrets opaque; org repo default-protect
- Adaptive cycles by top-level folder

## Assumptions

- Cycle 1 = docs foundation only; does not execute Early/simple moves or git-strategy.
- Researcher may refine empty-parent / multi-root wording under the locked wrapper-default rule without reopening the default.
- Size-band thresholds (S/M/L/XL cutoffs) may be chosen by implementer if cheap and documented.
- Must-preserve draft will likely include high-risk rows (e.g. Obsidian, ProjetOrif) plus other agent-proposed candidates — still draft.
- No agent push required for Cycle 1.

## Open risks

- Must-preserve draft incomplete → later move cycles still risk critical paths; fail-closed until user reviews.
- Inventory deepen may miss nested git beyond scan depth; keep “lower bound / re-scan before move.”
- Scope creep into Early/simple execution or git-strategy body of work — hard out-of-scope.
- Proposed-ratified taxonomy mistaken for final approval — keep explicit sign-off gate language.
- Treating proposed date labels as applied renames — keep “proposal only” language.
- Secret sampling if deepen scan too aggressive — keep read bans.

## Key alignment changes (raw → refined)

- Cycle 1 docs_only locked; placeholders removed after user answers.
- Taxonomy decisions locked (status, spaces, CreationTime, wrapper-label rule, proposed-ratified DoD).
- Inventory deepen locked to cheap signals; must-preserve = draft proposals.
- Next-row primary = Early/simple; Git-strategy = hard-gate reminder only.
- Acceptance criteria binary and auditor-checkable; no re-ask.
