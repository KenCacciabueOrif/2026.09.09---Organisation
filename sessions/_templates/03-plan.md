# Plan

## Goal

## Mutation class

| Field | Value |
| --- | --- |
| Class | `docs_only` \| `fs_mutation` |
| Corpus FS | (zero intentional mutations \| approved batch paths) |
| User approval before implementer | required \| not required (docs_only) |
| First-move gates (if fs_mutation) | taxonomy sign-off/waiver · must-preserve review/waiver · batch approval |

## What the user is approving (required if `fs_mutation`)

Plain-language intent preview for the orchestrator plan gate:

- What “yes” does on disk (paths / parents).
- Pros / cons (tradeoffs) — e.g. path bookmarks break, new parents, partial-batch risk.
- What “no / edit” means (no moves until revised).

## Acceptance criteria

- [ ] 

## Steps

1. **Auth/preflight** (required when plan includes `git push` or `git pull`) — dual preflight: remote scheme + tracking; agent git path / helper / GfW preference (Windows); GCM evidence boolean; `gh` present? (not sole signal); user-terminal note optional; `blocker_type` agent_environment vs user_credentials — verify: agent can push/pull non-interactively or ready_to_implement no
2. **Pull/sync plans** — document success path vs fail-closed outcomes: `dirty_working_tree` | `other`/`non_ff` | `other`/`merge_conflict` (`blocked_conflict`); lock Q2 + Q3b; never claim sync complete on abort
3. **Step** — paths — action — verify: 
4. 

## Non-goals

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Agent environment (wrong git / sandbox) | Prefer GfW absolute path; classify `agent_environment`; do not false `user_credentials` for missing `gh` alone |
| User credentials missing | `ready_to_implement` no; user remediates; leave local commit if already created; status blocked not complete |
| Single-commit vs post-push session log | Write pre-push log before commit; after push leave finalize dirty **or** allow optional tiny session-only follow-up commit in AC |
| Overclaim proposed-ratified / draft must-preserve | Exact “ready for sign-off” / “draft — not auto-locked” wording; auditor greps |

## Ready to implement

yes | no

## Blocking questions

none | 
