# Online prompt tips (git pull / agent brief)

Actionable tips for refining a **git pull** FAW cycle brief. Sources accessed 2026-09-09.

1. **Name the integration policy in the prompt** — Prefer an explicit verb: `--ff-only`, merge (`--no-rebase`), or `--rebase`. Vague “just pull” lets the agent (or Git defaults) create unexpected merge commits or rewrite local SHAs.  
   Source: [LinuxCapable — Git Pull Command](https://linuxcapable.com/git-pull-command-fast-forward-merge-rebase-and-squash/)

2. **Prefer fail-closed on surprise divergence** — Encode “stop if not a clean fast-forward” when the expected state is “local main trails origin.” That turns divergence into a clear blocker instead of a silent merge. (*Fail-closed* = treat failure as blocked, not as success.)  
   Source: [TheCodeForge — Git Pull incidents](https://thecodeforge.io/devops/git-pull/)

3. **Preflight working tree before pull** — Acceptance criteria should require `git status` (and optionally `git branch -vv`) first; dirty trees block rebase and can cause partial/conflicted merges. Spell the dirty-tree policy (abort / stash / user resolve) in AC.  
   Source: [TheLinuxCode — Predictable git pull](https://thelinuxcode.com/git-pull-a-predictable-workflow-for-staying-in-sync/)

4. **Do not rebase shared published history** — If local commits already exist on a shared branch, prefer merge or stop; rebase+force is out of scope unless the user explicitly asks. Keep that in Out of scope.  
   Source: [OneUptime — Rebase vs merge (2026)](https://oneuptime.com/blog/post/2026-01-24-git-rebase-vs-merge-strategies/view)

5. **Goal + constraint + verify** — Structure the refined prompt as: goal (sync local to remote), hard constraint (this org-repo git root only), verification (status, ahead/behind counts, no unrelated trees touched).  
   Source: [Learn Cursor — Writing good prompts](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

6. **“Done when” must be a runnable check** — e.g. `git status -sb` shows tracking `origin/main` with expected ahead/behind, pull exit 0 or documented fail-closed block — not “repo is synced” alone.  
   Source: [Learn Cursor — Prompt templates](https://www.learncursor.dev/guides/prompt-templates-for-ai-coding-agents)

7. **Bound the job; plan before mutating** — For agent cycles, keep one task (pull only), list non-goals (no push, no taxonomy sign-off, no corpus moves), and require a short plan before shell git mutations.  
   Source: [OTF — Cursor agent best practices](https://otf-kit.dev/blog/cursor-agent-best-practices)
