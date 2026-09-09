# Online findings — Pull / ff-only / GCM (session `2026.09.09-1332`)

Sources checked 2026-09-09. Prefer official / primary docs.

## `git pull --ff-only`

1. **[Git — git-pull documentation](https://git-scm.com/docs/git-pull)**  
   `--ff-only` updates only when history can fast-forward; it refuses divergent local history instead of merging or rebasing. Matches locked Q2=A and fail-closed AC (no merge fallback on divergence).

2. **[Git — git-merge `--ff-only`](https://git-scm.com/docs/git-merge)**  
   Fast-forward when possible; otherwise refuse and exit non-zero. Pull’s ff-only path is this merge behavior after fetch — implementer should treat non-zero as block, not retry with `--rebase` / `--no-ff`.

## Git Credential Manager (HTTPS on Windows)

3. **[GCM configuration](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md)**  
   Select helper with `credential.helper manager`. Windows default store `wincredman`. Explains why Git for Windows with system `manager` is preferred when PATH/MSYS has no helper.

4. **[GCM repository README](https://github.com/git-ecosystem/git-credential-manager)**  
   GCM is invoked implicitly by Git for HTTPS remotes; correct binary + helper matters more than installing `gh` for agent Shell auth.

5. **[GCM credential stores](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/credstores.md)**  
   `wincredman` may be unavailable over some remote/SSH desktop sessions — if fill/fetch suddenly fail despite prior success, prefer `agent_environment` / store reachability over “missing gh”.

## Agent vs user-terminal auth (context)

6. **[Cursor forum — agent authenticated git](https://forum.cursor.com/t/agent-cannot-run-git-push-or-other-authenticated-commands-no-access-to-user-credentials/151256)**  
   User-terminal success ≠ agent Shell ready. Same dual-preflight law applies to **pull/fetch** as to push.

## Session-local prompt tips

7. **`sessions/2026.09.09-1332/01-prompt-betterment/online-prompt-tips.md`**  
   Already stresses naming `--ff-only` explicitly and treating auth as environment preflight — reuse for planner wording; no need to re-derive.

## Takeaways for implementer

- Use **`git pull --ff-only`** only; on failure do not switch strategies.
- Prefer **absolute GfW** `git.exe` for status + pull even if PATH/MSYS fetch sometimes succeeds (empty helper; push historically failed; status counts diverge).
- Record GCM evidence as booleans only (fill/dry-run exit); never log passwords or full `Env:`.
- Missing `gh` is optional signal only while GCM fill + fetch dry-run pass.
