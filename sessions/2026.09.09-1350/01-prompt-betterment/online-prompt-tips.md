# Online prompt tips — Pull-autonomy (dirty-tree + agent git)

Goal type: agent-run git sync + FAW workflow policy change (docs/skills/rules), not corpus moves.

## Actionable tips

1. **State goal + constraints + done-condition in one brief**  
   Name paths, what must not change, and a verifiable exit (e.g. agent Shell pull succeeds inside org-repo root; no force/hard reset). Cursor’s agent prompting guidance favors specific files, patterns, guardrails, and testable done-conditions.  
   Source: https://cursor.com/blog/agent-best-practices

2. **Prefer explicit commits over stash/autostash for automation**  
   Stash / `pull --rebase --autostash` can silently re-apply stale hunks, return success with conflict markers, or lose work if a later step drops the stash. For shared `main`, commit WIP (or isolate in a worktree) before pull.  
   Sources: https://dev.to/ilya_mozerov_867dbdd91feb/a-bare-git-pull-wrote-three-day-old-code-over-the-fix-it-had-just-fetched-28kj · https://kody-w.github.io/2026/04/20/agents-and-bots-share-a-repo/

3. **Checkpoint before multi-file agent work**  
   A normal commit before policy/docs edits gives a rollback point without destructive reset. Encode “commit session/meta before pull” as AC when the tree is never clean because FAW always writes sessions.  
   Source: https://baeseokjae.github.io/posts/cursor-agent-best-practices-2026/

4. **Ban silent destructive git in agents**  
   Fail-closed on conflict: no `stash drop` after failed pop, no `--no-verify`, no hard reset to “make pull work.” Prefer abort + typed `blocker_type` over hiding failure.  
   Source: https://github.com/NodeJSmith/Claudefiles/issues/112

5. **Keep agent blast radius narrow**  
   Confine git ops to one git root (this org-repo). Worktrees/isolation ideas apply when parallel agents collide; here the standing rule is “never sibling `C:\Project` trees.”  
   Sources: https://cursor.com/blog/agent-best-practices · https://www.nazarboyko.com/articles/ai-agents-branch-strategy-safe-automation-git

6. **Do not treat “user terminal can pull” as agent success**  
   Dual-preflight the agent’s git binary/credentials (Windows: Git for Windows + GCM vs MSYS). Encode agent Shell success in AC.  
   Source: https://cursor.com/blog/agent-best-practices (git workflow automation / agent-run commands)

7. **When dirty + pull conflict, prefer commit then merge/ff over stash pop**  
   Happy Git guidance: stash helps only when no overlap; on conflict you gain little vs committing first. For FAW, session-only auto-commit + `--ff-only` (or documented merge) is clearer than stash.  
   Source: https://happygitwithr.com/pull-tricky

## Implication for this cycle’s prompt

- Reframe pull-cycle **Q3** away from “always abort → user cleans” toward **agent-autonomous dirty handling** that is still fail-closed.  
- Prefer **path-scoped auto-commit** (sessions / FAW meta) over stash/autostash as the disclosed default package, unless the user picks otherwise.  
- Keep hard bans: force push, hard reset, `--no-verify`, secrets in logs, sibling trees.
