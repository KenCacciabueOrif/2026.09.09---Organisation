# Online findings — Cycle 12 Multi-experiment (`WorkSpace` only / continue strategy)

**Session:** `sessions/2026.09.10-1247/02-research/`  
**Purpose:** Authoritative citations supporting **continue-strategy** docs (atomic nested git, multi-remote inventory without rewrite, worktree re-check before any future move, Windows robocopy recovery for *future* gated moves only). No product APIs invented. No corpus mutation this cycle.

## Citations

1. **Git worktree — list / repair before any move**  
   - Title: Git - git-worktree Documentation  
   - URL: https://git-scm.com/docs/git-worktree.html  
   - Takeaway: Linked worktrees attach path metadata; prefer `worktree move` / `worktree repair` over blind FS moves when links exist. Continuity: re-run `worktree list` before any **future** approved move; if >1 worktree, fail-closed. **Live Cycle 12:** no `.git/worktrees` on live hermes — linked-worktree still **not** the blocker.

2. **Git remotes — multiple remotes are normal; inventory ≠ surgery**  
   - Title: Git - Working with Remotes  
   - URL: https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes  
   - Takeaway: Repos may list several remotes; documenting names/schemes is correct ops. Does **not** authorize `set-url` / dropping `cada` mid Multi-experiment Continuity — this cycle is document-only.

3. **Git remote management (official)**  
   - Title: Git - git-remote Documentation  
   - URL: https://git-scm.com/docs/git-remote  
   - Takeaway: `git remote` lists/manages remotes; changing URLs is an explicit `set-url` / rewrite action. Continuity forbids that unless a later gated strategy says otherwise; HTTPS dual-remote on hermes remains **classified**, not “fixed” by docs.

4. **GitHub — managing remote URLs (explicit rewrite is a separate action)**  
   - Title: Managing remote repositories  
   - URL: https://docs.github.com/en/get-started/git-basics/managing-remote-repositories  
   - Takeaway: Changing a remote URL is intentional. Matches SSH-origin **path-only** Continuity (document remotes; no rewrite this cycle).

5. **Robocopy `/E` + `/MOVE` (Windows lock recovery — future gated moves only)**  
   - Title: Robocopy \| Microsoft Learn  
   - URL: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy  
   - Takeaway: `/E` includes empty subdirs; `/MOVE` moves files and directories then deletes from source. Relevant **only** if a future plan-gated scoped isolation hits PermissionDenied/split — reunify + recover; remove **only empty** leftover `.git` shells. **Not** used this cycle (`docs_only`).

6. **Prior session online notes (carry)**  
   - Paths: `sessions/2026.09.10-1047/02-research/online-findings.md`, `sessions/2026.09.10-0907/02-research/online-findings.md`, `sessions/2026.09.10-0848/02-research/online-findings.md`  
   - Takeaway: Same Continuity spine — opaque `.env`, atomic nested `.git`, path-only remotes, fail-closed whole-tree while multi-remote + backup/quarantine clones remain. Cycle 12 is another **re-probe attestation** against the durable strategy file — not a new online remediation path.

## Synthesis for this cycle

- Online guidance reinforces **docs_only continue strategy**: classify/attest, do not rewrite remotes, do not force whole-tree archive.
- Scoped `_backups` / `_quarantine` isolation remains **research-supported for a later Continuity B + plan gate** — not Continuity Q1=A this cycle (research may note readiness; must not select execute).
- Robocopy / worktree repair are **future-move** tools, not Cycle 12 deliverables.
- Prefer official git-scm / Microsoft Learn / GitHub docs over blog posts for planner citations.
