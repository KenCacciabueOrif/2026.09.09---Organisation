# Online findings — publish / GfW+GCM / BOM-safe commits

Sources checked 2026-09-09. Prefer official / primary docs.

## Git Credential Manager (GCM)

1. **[Git Credential Manager — configuration](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md)**  
   GCM is selected with `git config … credential.helper manager`. On Windows the default credential store is `wincredman` (Windows Credential Manager). Confirms why Git for Windows with system `credential.helper manager` is the preferred agent binary for HTTPS remotes.

2. **[Git Credential Manager — repository README](https://github.com/git-ecosystem/git-credential-manager)**  
   GCM is the supported cross-platform helper bundled with Git for Windows; it is invoked implicitly by Git for HTTPS hosts (e.g. GitHub). Not intended as a manual CLI for every push; correct helper + binary is what matters for non-interactive agent Shell.

3. **[GCM credential stores](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/credstores.md)**  
   Windows Credential Manager is the default store; documented limitation: not available over some remote/SSH desktop sessions. Relevant if a future agent sandbox cannot reach DPAPI — classify as `agent_environment` / remount credentials, not “missing gh”.

## Windows PowerShell + UTF-8 BOM in commit messages

4. **[Microsoft Learn — Set-Content -Encoding](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-content?view=powershell-7.6)**  
   PowerShell 7+ documents `utf8NoBOM`. Windows PowerShell 5.1’s `-Encoding utf8` historically writes a BOM — matches repo law in `AGENTS.md` and the visible BOM on historical commit `9708f2e`.

5. **[Stack Overflow — UTF-8 without BOM via `UTF8Encoding($false)`](https://stackoverflow.com/questions/5596982/using-powershell-to-write-a-file-in-utf-8-without-the-bom)**  
   Practical pattern: `[System.IO.File]::WriteAllText(..., (New-Object System.Text.UTF8Encoding $false))` or prefer `git commit -m "$(... here-string ...)"` to avoid message files entirely.

## Agent push vs user credentials (context)

6. **[Cursor forum — agent cannot run authenticated git push](https://forum.cursor.com/t/agent-cannot-run-git-push-or-other-authenticated-commands-no-access-to-user-credentials/151256)**  
   Community reports that user-terminal push success does not imply agent Shell auth. Aligns with project dual-preflight law (user can push ≠ agent ready).

## Prompt / publish process tips (session-local mirror)

7. **This session `01-prompt-betterment/online-prompt-tips.md`** already cites GCM FAQ / MSYS helper issues and fail-closed publish — reuse; no need to re-derive trust-boundary tips for planner.

## Takeaways for implementer

- Use **absolute Git for Windows** `git.exe` for push (and preferably commit-adjacent auth ops) when PATH resolves to MSYS without a working helper under `GIT_TERMINAL_PROMPT=0`.
- Treat GCM fill / `push --dry-run` success as agent-ready evidence; absence of `gh` is **not** a credential failure while GCM works.
- Draft commit messages without UTF-8 BOM (here-string `-m` or explicit no-BOM file encoding).
