# Online findings — Pull-merge (`sessions/2026.09.09-1435`)

Authoritative / recent sources for HTTPS GCM auth and merge of diverged histories. No invented APIs.

## Citations

1. **[Git - git-merge Documentation](https://git-scm.com/docs/git-merge)**  
   Merge joins histories since divergence; non-FF cases create a merge commit with both parents. Working-tree modifications are allowed only if they do not interfere with the merge. Supports `merge.ff` (`false` / `only`) — relevant when choosing merge commit vs ff-only.

2. **[Git - git-pull Documentation](https://git-scm.com/docs/git-pull)**  
   `git pull` = fetch + integrate. With reconcile strategy merge (not rebase / not ff-only), diverged tips are combined via merge. Useful command form for this cycle: fetch then merge, or `git pull` with rebase disabled.

3. **[Git Credential Manager — configuration](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md)**  
   `credential.helper` / GCM on Windows; `credential.interactive` / headless behavior. Agent should use GfW’s `manager` helper; do not rely on MSYS git with empty helper for HTTPS.

4. **[GCM environment — GCM_INTERACTIVE](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/environment.md)**  
   `GCM_INTERACTIVE=0` / false fails immediately if a prompt would be required (prefer fail over hang in automation). This cycle’s `credential fill` already returned stored creds non-interactively.

5. **[GitHub Docs — Caching credentials on Windows](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git?platform=windows)**  
   Prefer Git for Windows + GCM for HTTPS GitHub; GCM stores creds in Windows Credential Manager. Aligns with FAW dual-preflight prefer-GfW rule. Missing `gh` alone does not mean credentials are missing when GCM works.

6. **Practical diverge resolution (secondary):** community guides and Stack Overflow reiterate fetch + `git merge origin/main` (or pull-with-merge) for 1/1 diverge; reserve hard reset only when discarding local tip — **forbidden** under this session’s Q3b=A.

## Takeaways for this cycle

| Topic | Takeaway |
| --- | --- |
| Q2=B combine | Official merge path is fetch + merge (or pull without rebase / without `--ff-only`). |
| Conflicts | Content conflicts stop the merge until resolved; fail-closed may `merge --abort` without hard reset. |
| Auth | Probe with GCM-backed GfW; log only success/fail and username/password **presence**, never secret values. |
| Binary | GitHub + FAW: use Git for Windows, not MSYS, for HTTPS agent ops. |
