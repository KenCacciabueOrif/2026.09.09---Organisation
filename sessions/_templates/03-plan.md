# Plan

## Goal

## Mutation class

| Field | Value |
| --- | --- |
| Class | `docs_only` \| `product_settings` \| `fs_mutation` |
| Mutation kind (if fs_mutation) | `path_batch` \| `remote-config` \| `scoped_isolation` \| other |
| Corpus FS | (zero intentional mutations \| approved batch paths \| remote-config only — zero path moves) |
| User approval before implementer | required \| not required (`docs_only` \| `product_settings`) |
| First-move gates (if fs_mutation) | taxonomy sign-off/waiver · must-preserve review/waiver · batch approval |

Note: `docs_only` covers **org-repo scaffolding creates** (folders/READMEs/docs inside this organisation git root) when there are **no** corpus moves/renames/deletes. `product_settings` covers editor/IDE extension install-switch, settings, **local installed-extension `dist/`/`src/` patches** (document **re-apply after Marketplace/Open VSX update**; Soft Reload tip after patch), and/or local evidence fixtures — **not** corpus `fs_mutation`; plan-gate **n/a**; same-run when ready. For Python 42-header + flake8 Continuity: prefer **≤79 generator** over Norminette-80 art or ignore-first. `fs_mutation` is for corpus / catalogue-backed path batches **or** **remote-config** (e.g. `git remote remove` on a pinned live nested `.git`) — remote-config still needs the plan gate even with zero path moves.

## What the user is approving (required if `fs_mutation`)

Plain-language intent preview for the orchestrator plan gate:

- What “yes” does on disk (paths / parents) **and/or** exact git remote command(s) + clone cwd.
- Pros / cons (tradeoffs) — e.g. path bookmarks break, new parents, partial-batch risk, lost remote-tracking refs.
- What “no / edit” means (no moves/remote edits until revised).

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
