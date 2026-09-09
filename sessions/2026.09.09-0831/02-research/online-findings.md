# Online findings

Authoritative / practical notes for **explicit user-requested** `add` → `commit` → `push` on `main`, with a secrets gate. Prefer official docs; blog sources used only for operational pitfalls.

## Citations

1. **[git-commit documentation](https://git-scm.com/docs/git-commit)** (git-scm.com)  
   Commit records a snapshot of the index. Use `-m` / `--message` or `-F` / `--file` for a non-interactive message. Do not skip hooks unless deliberately using `--no-verify` (forbidden by this task’s constraints).

2. **[git-push documentation](https://git-scm.com/docs/git-push)** (git-scm.com)  
   Default push updates remote refs; force variants rewrite history. For this goal: plain `git push origin main` (or tracking `git push`) with **no** `--force` / `--force-with-lease`.

3. **[Stage, commit, and push changes | GitLab Docs](https://docs.gitlab.com/topics/git/commit/)**  
   Always check status before commit; `git add .` stages the working tree but can include unwanted files — review first. Example push: `git push origin main`. Notes secret push-protection skip options exist on some hosts — **do not use skip options** here.

4. **[about_Quoting_Rules — Here-strings | Microsoft Learn](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-7.5)**  
   On PowerShell, multi-line commit messages should use a here-string (`@'...'@` or `@"..."@`), which is the HEREDOC-equivalent for this shell — not bash `<<'EOF'` unless the command truly runs in bash.

5. **[PowerShell here-string misused in Bash corrupts commit messages](https://github.com/anthropics/claude-code/issues/65162)**  
   Operational pitfall: `@'...'@` inside a bash-invoked tool becomes literal `@` characters in the message. Implementer must run the commit via **PowerShell** (user shell) or use `git commit -F msg.txt` to avoid shell mismatch.

6. **[Git Best Practices for Clean Commits and Teams](https://adnantasdemir.com/en/posts/git-best-practices)**  
   Review `git status` / `git diff` / staged diff before committing; never force-push blindly on shared `main`; keep secrets out of history (rotate if leaked). `git add .` is acceptable only when the user explicitly wants the full tree **and** a secrets review has passed.

7. **[How to Prevent Secret Leaks in Git](https://securecodehq.com/en/blog/git-secrets-prevent-leaks)** / **[DevSecOps for Git](https://dev.to/sharonkynu/devsecops-for-git-security-starts-at-commit-time-3iac)**  
   Defense in depth: filename/path scan before stage, avoid committing `.env` / keys / credentials; once in history, deletion alone is insufficient. This repo has no active pre-commit secret scanner — **manual secrets gate is required**.

8. **General shared-branch caution** (multiple 2025–2026 tutorials, e.g. tech-insider Git tutorial)  
   Direct commits to `main` bypass PR review; force-push on `main` is especially harmful. This task **explicitly** authorizes commit+push on `main` without a PR — proceed, but keep the change set reviewed and non-destructive.

## Takeaways for this session

| Practice | Apply how |
| --- | --- |
| Review before stage | Re-run `git status`, `git diff`, `git log` at implement time |
| Stage all (user-ordered) | `git add -A` or `git add .` from repo root after secrets gate |
| Secrets gate | Halt if `.env`, credentials, keys, tokens appear; do not commit/push |
| Message | Derive from staged diff; plain why-focused subject matching `Initial commit` brevity; PowerShell here-string or `-F` file |
| Hooks | Do not use `--no-verify`; currently only `.sample` hooks exist |
| Push | `git push origin main` or `git push` with tracking; never `--force` |
| Verification | Commit hash + push exit success + `git status` only (no `gh`/Actions) |
