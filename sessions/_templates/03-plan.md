# Plan

## Goal

## Acceptance criteria

- [ ] 

## Steps

1. **Auth/preflight** (required when plan includes `git push`) — dual preflight: remote scheme + tracking; agent git path / helper / GfW preference (Windows); GCM evidence boolean; `gh` present? (not sole signal); user-terminal note optional; `blocker_type` agent_environment vs user_credentials — verify: agent can push non-interactively or ready_to_implement no
2. **Step** — paths — action — verify: 
3. 

## Non-goals

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| Agent environment (wrong git / sandbox) | Prefer GfW absolute path; classify `agent_environment`; do not false `user_credentials` for missing `gh` alone |
| User credentials missing | `ready_to_implement` no; user remediates; leave local commit if already created; status blocked not complete |

## Ready to implement

yes | no

## Blocking questions

none | 
