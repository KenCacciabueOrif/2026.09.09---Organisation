# Online findings

Citations for agent Shell vs interactive `git push`, GCM, and Cursor sandbox. Prefer official / primary sources.

## Cursor agent Shell / sandbox / credentials

1. **Agent terminal tools (official)** — https://cursor.com/docs/agent/tools/terminal  
   Cursor runs shell commands under Run Mode controls; sandboxing restricts file/network access. Troubleshooting notes `CURSOR_AGENT` for detecting agent-driven shells.

2. **Run Modes & sandboxing (official)** — https://cursor.com/docs/agent/security/run-modes  
   Sandbox can block unauthorized file access and network; commands needing full system access bypass sandbox with approval. Network modes and `sandbox.json` control egress. Windows sandboxing is documented as less complete than macOS/Linux in community reports, but credential/helper isolation still occurs in practice. `CURSOR_SANDBOX` env vars are documented for macOS/Linux sandboxed children.

3. **Agent cannot access user credentials (forum)** — https://forum.cursor.com/t/agent-cannot-run-git-push-or-other-authenticated-commands-no-access-to-user-credentials/151256  
   Same pattern as this repo: interactive Cursor terminal push works; agent `git push` fails. Staff suggestion: enable **Legacy Terminal Tool** (Settings → Agents) so execution inherits a more normal credential environment (esp. WSL; relevant as a Windows remediation path too).

4. **HTTPS push / credential helper not used (forum)** — https://forum.cursor.com/t/git-push-fails-with-could-not-read-username-for-https-github-com-device-not-configured-credential-helper-not-used-when-source-control-runs-git/151765  
   Non-TTY git contexts fail with username/prompt errors when helper cannot supply creds. Suggested workarounds: **SSH remotes**, or **`gh auth login` + `credential.helper '!gh auth git-credential'`**. Aligns with treating SSH/`gh` as fallbacks, not first choice when GCM works.

5. **Sandboxed AI shell / git on Windows (forum)** — https://forum.cursor.com/t/ai-shell-now-sandboxed-can-t-run-real-git-powershell/153876  
   Guidance: change Auto-Run / disable heavy sandbox isolation, enable Legacy Terminal Tool, set explicit PowerShell profile so agent commands run with real local credentials.

6. **MSYS/Git Bash needs `required_permissions: ["all"]` (forum)** — https://forum.cursor.com/t/git-bash-fails-in-cursor-shell-tool-on-windows-due-to-sandbox-restrictions/150918  
   Sandbox blocks MSYS memory mapping; workaround historically was Shell `required_permissions: ["all"]` or Settings to leave sandbox. **Note:** this organisation harness’s Shell schema may not expose that parameter — document Settings remediation + “request elevated/out-of-sandbox run when the product UI offers it.”

## Git Credential Manager / non-interactive git

7. **GCM configuration — `credential.interactive`** — https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md  
   Disabling interaction makes GCM fail instead of hang when a prompt would be required. Cached credentials should still work when available; if fill fails with interactivity disabled, treat as “no usable cached cred for this git/helper context.”

8. **GCM environment — `GCM_INTERACTIVE`** — https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/environment.md  
   Env twin of `credential.interactive`. Useful for fail-closed automation **after** verifying the correct helper + git binary; forcing `never`/`0` too early can false-negative agent preflight on Windows.

9. **Git `GIT_TERMINAL_PROMPT`** — https://git-scm.com/docs/git  
   Setting `GIT_TERMINAL_PROMPT=0` disables username/password terminal prompts (exact class of error seen in session `2026.09.09-0831`). Prefer using it to **fail closed** when probing MSYS/no-helper git, not as the only GCM probe.

## Takeaways for this org

| Topic | Online consensus | Local evidence alignment |
| --- | --- | --- |
| Agent vs user terminal | Different execution context; Legacy Terminal / less sandbox often fixes credential inheritance | Confirmed divergence; **primary local cause is MSYS git without helper**, not missing GitHub login |
| `required_permissions: all` | Community workaround for sandbox | Not available as a Shell arg in this researcher harness; keep as optional product/UI note |
| SSH / `gh` helper | Durable HTTPS alternatives | Secondary; GfW+GCM already works in agent Shell when invoked explicitly |
| Non-interactive flags | Fail closed in CI | Use carefully: with GCM they can block successful store reads in some agent probes |

## Prompt-betterment cross-link

See also `sessions/2026.09.09-0850/01-prompt-betterment/online-prompt-tips.md` (forum + GCM links used while refining the prompt).
