# Online findings — Cycle 10 Multi-experiment (`WorkSpace` only + hazard remediation)

**Session:** `sessions/2026.09.10-0907/02-research/`  
**Purpose:** Authoritative citations for nested-git atomic moves, multi-remote inventory (no URL rewrite), and Windows lock-recovery Continuity supporting **safe relocation / isolation rules**. No product APIs invented.

## Citations

1. **Git worktree — move / repair hazards**  
   - Title: Git - git-worktree Documentation  
   - URL: https://git-scm.com/docs/git-worktree  
   - Takeaway: Linked worktrees store path metadata; casual FS moves can break absolute `gitdir` links — prefer `worktree move` / `worktree repair` when links exist. Continuity: if `worktree list` shows more than the main tree, fail-closed unless a gated plan addresses it. **Live Cycle 10:** all seven WorkSpace nested roots show **one main worktree only** — linked-worktree is **not** the blocker; multi-remote + backup/quarantine clones are.

2. **Git remotes — multiple remotes are first-class; inventory ≠ rewrite**  
   - Title: Git - git-remote Documentation  
   - URL: https://git-scm.com/docs/git-remote  
   - Takeaway: Repos may have several remotes (`origin`, second names such as `cada`); `set-url` exists but Continuity this cycle is **SSH/HTTPS path-only document** — **no** `origin`/`cada` URL rewrite, no history rewrite. Moving an intact tree preserves remote config; organisational hazard is **duplicate clones + dual remotes**, not “missing” remote support in Git.

3. **Git remotes — working with multiple remotes (book)**  
   - Title: Git - Working with Remotes  
   - URL: https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
   - Takeaway: Multiple remotes are normal collaboration tooling. Classification should name remotes and schemes without treating dual-remote alone as a license for remote surgery mid Multi-experiment.

4. **Robocopy `/E` `/MOVE` (Windows lock recovery Continuity)**  
   - Title: Robocopy \| Microsoft Learn  
   - URL: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
   - Takeaway: `/E` includes empty subdirs; `/MOVE` moves files and directories then deletes from source. Use **only** as recovery after PermissionDenied/split on an **approved** move — reunify destination + source leftovers; remove **only empty** leftover `.git` shells; re-attest; log deviation. Exit codes ≥8 indicate copy failure — do not claim success from a partial move.

5. **Robocopy move / lock caveats (operational)**  
   - Title: How to detect robocopy's failure to delete from source?  
   - URL: https://serverfault.com/questions/409644/how-to-detect-robocopys-failure-to-delete-from-source  
   - Takeaway: Locked files can leave source trees behind after `/MOVE`; inspect logs (ERROR 32 / ERROR 5), not exit-code friendliness alone. Aligns with Continuity: prefer single atomic move; on split → reunify + recover; never delete non-empty leftover `.git`.

6. **Prior session online notes (carry forward)**  
   - Paths: `sessions/2026.09.10-0848/02-research/online-findings.md`, `sessions/2026.09.10-0811/02-research/online-findings.md`, `sessions/2026.09.10/02-research/online-findings.md`  
   - Takeaway: Same Continuity spine — opaque `.env`, atomic nested `.git`, path-only remotes, fail-closed on unexpected roots / multi-remote mess for **whole-tree** archive. Cycle 10 adds **classification + optional scoped isolation** of named backup/quarantine trees under plan gate — still not whole-tree “solved.”

## Synthesis for this cycle

- Prefer **docs_only** strategy artifacts (classification, fate, safe rules, INDEX/ROADMAP honesty).  
- Optional **scoped** `fs_mutation` of named `_backups` / `_quarantine` trees is consistent with official “move intact trees; don’t invent remote surgery” guidance — **still plan-gated**.  
- **Never** treat whole XL `WorkSpace` ordinary Multi-experiment archive as remediation success while live multi-remote + clone hazards remain.  
- **Never** use `filter-repo` / history rewrite for this remediation thread (out of scope; Continuity forbid).
