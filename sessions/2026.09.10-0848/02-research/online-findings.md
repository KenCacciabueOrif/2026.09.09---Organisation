# Online findings — Cycle 9 Multi-experiment (`WorkSpace` only)

**Session:** `sessions/2026.09.10-0848/02-research/`  
**Purpose:** Authoritative citations for nested-git / multi-remote / Windows move Continuity. No product APIs invented.

## Citations

1. **Git worktree — move / repair hazards**  
   - Title: Git - git-worktree Documentation  
   - URL: https://git-scm.com/docs/git-worktree  
   - Takeaway: Linked worktrees store path metadata; casual moves can break absolute `gitdir` links; use `worktree move` / `worktree repair` rather than inventing fixes. Continuity fail-closed: if `worktree list` shows more than the main tree, **defer**. Live-check: all seven WorkSpace nested roots show **one main worktree only** — linked-worktree is **not** the blocking hazard this cycle; multi-remote + unexpected backup/quarantine roots are.

2. **Git remotes — multiple remotes are first-class**  
   - Title: Git - git-remote Documentation  
   - URL: https://git-scm.com/docs/git-remote  
   - Takeaway: A repo may have several remotes (`add`, separate fetch/push URLs). Moving an intact tree does not rewrite remotes, but **multi-remote + duplicate backup/quarantine clones** is an organisational/git-strategy hazard under Continuity fail-closed — not something to “fix” mid Multi-experiment by inventing remote surgery or force-moving.

3. **Robocopy `/E` `/MOVE` (Windows lock recovery Continuity)**  
   - Title: Robocopy \| Microsoft Learn  
   - URL: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
   - Takeaway: `/E` copies subdirectories including empty; `/MOVE` moves files and directories then deletes from source. Relevant **only if** a future **cleared / approved** WorkSpace move hits PermissionDenied/split — reunify + empty `.git` shells only. **Not** a license to force-move while hazards remain.

4. **Prior session online notes (carry forward)**  
   - Paths: `sessions/2026.09.10/02-research/online-findings.md`, `sessions/2026.09.10-0811/02-research/online-findings.md`  
   - Takeaway: Same Continuity: path-only SSH, opaque `.env`, atomic nested `.git`, fail-closed on unexpected roots / multi-remote mess — WorkSpace deferred in Cycles 7–8 for those reasons; Cycle 9 live re-probe **re-confirms**.

## Synthesis for this cycle

Recommend **no corpus move**. Document hazards; keep Multi-experiment **in progress** with **Remaining: `WorkSpace` only**. Dedicated **git-strategy** remains a **future Continuity opt-in (Q1=B)** — out of scope this cycle (Q1=A). If a later cycle clears hazards or opts into git-strategy, re-scan remotes/worktrees/`.env` paths immediately before any plan-gated move; never rewrite `origin` URLs; never read `.env` contents.
