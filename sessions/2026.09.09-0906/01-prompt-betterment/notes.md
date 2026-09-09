# Prompt betterment notes

## Assumptions (locked from prior sessions; not re-asked)

1. Stage **everything** (tracked + untracked); secrets gate only exclusion.
2. Auto-generate commit message from staged diff / log style.
3. Work on **`main`** (no feature branch).
4. **Push only** — no PR / no `gh pr create`.
5. No extra must-exclude paths beyond secrets.
6. Done = commit **hash** + **push OK** + **`git status`**; no remote/`gh` verification pages.
7. **Option A:** agent Shell push via Git for Windows + GCM when PATH git is MSYS; dual preflight; no secrets in logs; BOM-safe PowerShell commit message.

## Clarifying questions

None asked this cycle — prior answers + Option A were sufficient for a publish goal.

## Open risks

- Working tree may include large trees (`.cursor/`, `sessions/`) — “stage everything” is intentional; commit message must still accurately summarize the diff.
- Agent Shell may still resolve MSYS `git` first — implementer must invoke GfW absolute path when helper is missing (do not assume PATH order).
- GCM may fail under some Cursor sandbox/run modes even when GfW is used — fail-closed with `agent_environment` + remediation; do not false-complete.
- Suspected secrets in untracked paths could halt the whole publish; report paths clearly.
- If nothing to commit (clean tree), do not create an empty commit — report clean status and treat push as N/A or up-to-date dry-run per plan.

## Key alignment vs raw goal

| Raw | Refined |
| --- | --- |
| “new git add commit and push” | Full stage → one auto-message commit on `main` → agent push to `origin` |
| Unspecified branch / PR | `main`, push-only, no PR |
| Unspecified DoD | Hash + push OK + `git status` |
| Implied agent can push | Dual preflight + GfW+GCM Option A encoded |
| Unspecified PS commit safety | BOM-safe message; no secrets in logs |
