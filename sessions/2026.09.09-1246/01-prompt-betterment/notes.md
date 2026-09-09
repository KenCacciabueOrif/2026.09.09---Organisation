# Prompt betterment notes — session `2026.09.09-1246`

## Status

**READY** — Answers locked; `refined-prompt.md` finalized for researcher → planner → implementer.

Questions Q1–Q7 were asked with plain-language explanations + pros/cons (informed consent). User answered Q1–Q5; Q6/Q7 unanswered → prompt-betterment **Choose→A** (documented below).

## Continuity (locked — do not re-ask)

| Lock | Value |
| --- | --- |
| Cycle | **Publish** — organisation-repo `git add` / `commit` / `push` |
| ROADMAP row | n/a — user named publish goal (not Early/simple or git-strategy) |
| Prior sessions | `sessions/2026.09.09-1032/` (Cycle 2 Early/simple complete); also `2026.09.09-1009` Cycle 1 |
| Mutation class | **docs_only** — org-repo git ops only; **no** corpus FS moves/renames/deletes (`fs_mutation` = changing files/folders on disk outside normal edit; not in scope) |
| Repo root | `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` |
| Pending program gates | none for this publish slice; taxonomy / must-preserve stay program-level for future move cycles (**proposed-ratified — ready for user sign-off** / **draft — not auto-locked** language only if those cycles resume) |
| Observed git (prompt phase peek) | branch `main` tracking `origin/main`; remote `https://github.com/KenCacciabueOrif/2026.09.09---Organisation.git`; large dirty tree (modified + untracked `catalogue/`, `program/`, prior sessions, current `sessions/2026.09.09-1246/`) |

## Clarifying questions (archive — answered)

(Full option text + pros/cons retained in prior revision / chat; not re-asked.)

## Answers

| Q | Locked | Source | Detail |
| --- | --- | --- | --- |
| **Q1** | **A** (org-repo root only) | User | Stage **all non-secret project work inside this git root only**. Do **not** stage/commit anything outside `C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation` (no other `C:\Project` folders). Encode git-root boundary in AC. |
| **Q2** | **B** | User | Agent drafts commit message after staging; why-focused; match repo history style; subject ≤ ~72 chars; BOM-safe on Windows. |
| **Q3** | **A** | User | **Agent Shell** must successfully push. Dual preflight (remote + GfW/GCM). **Fail-closed** if push fails. Missing `gh` alone ≠ missing credentials when GCM works. |
| **Q4** | **A** | User | Non-force `git push` to **`origin/main`**. Print remote + branch before push. |
| **Q5** | **A** | User | Default secret/junk exclusions only (no extra user exclude list). |
| **Q6** | **A** | **Choose** (agent) | Exactly **one** commit, then push. |
| **Q7** | **A** | **Choose** (agent) | Include `sessions/2026.09.09-1246/` artifacts written before commit; accept known post-push session dirtiness tradeoff. |

### Choose rationales (user may disagree later)

- **Q6 → A:** Raw goal was a single “git add commit push” publish; orchestrator AC already preferred one commit; splitting needs topic boundaries the user did not supply. Large mixed-topic commit is acceptable for a catch-up publish.
- **Q7 → A:** Matches `AGENTS.md` single-commit publish guidance (write implementation/session logs before commit). Audit trail of this publish attempt should land on remote; post-push log updates may stay dirty or use a tiny follow-up later — do not fail the cycle solely for that dirtiness.

## Assumptions (now aligned with Answers)

- Goal is org-repo publish only; no corpus moves; no taxonomy/must-preserve mutation this cycle.
- No PR creation unless user later asks.
- No `git push --force`, no amend of already-pushed commits, no `--no-verify`.
- Windows agent push uses dual preflight preferring Git for Windows + GCM when PATH git lacks helper.
- Staging never crosses this repo’s git root boundary.

## Open risks

- Dirty tree is large — one mixed-topic commit (Q6=A); harder to revert by topic.
- Agent push may fail (`agent_environment` vs `user_credentials`) even if user terminal works.
- Agent-drafted commit message (Q2=B) may not match user’s preferred phrasing.
- Post-push session log updates may remain uncommitted (documented tradeoff under Q7=A).
- Mid-cycle stubs under `sessions/2026.09.09-1246/` may land incomplete at commit time; later phases continue after push.

## Jargon-explanation debt

- Q1–Q5 answered after informed-consent asks (plain-language + pros/cons) — **no debt**.
- Q6/Q7 locked via **Choose** using the same documented defaults that were explained in the original ask batch — **no debt** (defaults were disclosed before Decide).

## Self-improvement backlog (if any)

- Reusable “publish cycle” question pack (stage scope / message / agent-push / branch / excludes / one-commit / include current session / **git-root-only**).
- Encode “never stage outside this git root” as a standing publish AC template line (multi-root `C:\Project` workspace confusion).

## Key alignment changes (raw → refined)

- Raw `/full-agent-workflow do git add commit push` → **Publish** cycle: org-repo only, `docs_only`, no corpus FS mutation.
- Q1 clarified: **this git root only** — never other `C:\Project` trees.
- Dual preflight + fail-closed agent push to `origin/main`; agent-drafted why-focused message; one commit; include this session folder; default secret/junk excludes.
- Taxonomy/must-preserve **out of scope** (remain proposed-ratified / draft at program level for later).
