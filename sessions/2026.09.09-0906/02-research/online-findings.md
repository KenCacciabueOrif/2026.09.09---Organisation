# Online findings

Citations for stage-all → commit → agent HTTPS push on Windows (Option A / GfW+GCM). Prefer official docs; no invented APIs.

## Git Credential Manager (authoritative)

1. **[GCM configuration](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md)**  
   GCM is used only when `credential.helper` is set to `manager`. Documents `credential.interactive` / store options (`wincredman` on Windows). Takeaway: agent must invoke a git binary whose config includes `manager` (Git for Windows system config), not MSYS with no helper.

2. **[GCM environment variables](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/environment.md)**  
   `GCM_INTERACTIVE=0` / related flags disable UI/TTY prompts and fail instead of hanging. Takeaway: do **not** force these on the first GCM probe (refined prompt Option A); OK for MSYS fail-fast with `GIT_TERMINAL_PROMPT=0` only.

3. **[GCM for Windows — Automation (legacy)](https://github.com/microsoft/Git-Credential-Manager-for-Windows/blob/master/Docs/Automation.md)**  
   Historical guidance for non-interactive automation. Takeaway: aligns with fail-closed non-TTY agent Shell behavior when no stored credential / wrong helper.

## Cursor agent / terminal context

4. **[Cursor forum — Agent cannot run authenticated git](https://forum.cursor.com/t/agent-cannot-run-git-push-or-other-authenticated-commands-no-access-to-user-credentials/151256)**  
   User terminal push ≠ agent Shell credentials/context. Windows note: native Shell should see credentials when the right helper/binary is used; sandbox/Legacy Terminal called out when it does not. Takeaway: dual preflight is mandatory; classify `agent_environment` vs `user_credentials`.

5. **[Cursor docs — permissions / Run Modes](https://cursor.com/docs/reference/permissions)**  
   Terminal allowlists and Auto-review steer command approval; not a substitute for GCM. Takeaway: if GfW+GCM still fails only under agent, escalate Run Mode / sandbox remediation (fallback note), not rewrite remote by default.

6. **[Cursor forum — HTTPS push Device not configured](https://forum.cursor.com/t/git-push-fails-with-could-not-read-username-for-https-github-com-device-not-configured-credential-helper-not-used-when-source-control-runs-git/151765/1)**  
   Credential helper not reached in some Cursor git contexts; workarounds include SSH or `gh auth git-credential`. Takeaway: keep SSH/`gh` as **fallbacks** only (refined prompt); prefer GfW+GCM Option A when fill/dry-run pass.

## Git safety / PowerShell BOM (commit message)

7. **PowerShell UTF-8 BOM behavior (known)** — Windows PowerShell 5.1 `Set-Content -Encoding utf8` writes a BOM that can corrupt `git commit -F` subjects. Takeaway: use here-string `git commit -m @"..."@` or `[System.IO.File]::WriteAllText(..., UTF8Encoding($false))` / PS7 `utf8NoBOM` (already encoded in `implementer.md` / refined prompt).

## Not required for this cycle

- Opening a PR / `gh pr create` docs — out of scope.
- Rewriting `origin` to SSH as default — fallback only after Option A fails.
