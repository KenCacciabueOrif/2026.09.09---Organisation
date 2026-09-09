# Online prompt tips (git add / commit / push)

Actionable prompting practices for agent-run git publish on Windows with GCM.

1. **Spell the full git workflow as numbered steps** — Inspect (`status`/`diff`/`log`), stage named scope, commit with a clear message, push, then return verification (hash, push OK, `git status`). Vague “commit and push” invites wrong files or skipped checks.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

2. **Require a verifiable definition of done** — Success should be checkable outputs (commit hash, push succeeded, clean/post-push `git status`). Agents perform better with concrete success signals.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

3. **State goal + hard constraints together** — Forbid force-push, `git config` edits, `--no-verify`, unsafe amend, and secret paths (`.env`, credentials, keys). Put constraints next to the goal.  
   Source: [Learn Cursor — writing good prompts](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts); [AI Tools Guidebook — Git commits with AI agents](https://aitoolsguidebook.com/en/articles/git-commit-with-ai/)

4. **Analyze the diff before writing the commit message** — Message must match staged content (why-focused, repo log style). Do not invent a fixed message without reading the diff.  
   Source: [Cursor agent best practices — Git workflows](https://cursor.com/blog/agent-best-practices)

5. **Mandate a pre-commit secrets gate** — Before commit, scan staged names/content for secret-like files; **stop and report** if found. Never log credential material from `git credential fill`.  
   Source: [AI Tools Guidebook — Git commits with AI agents](https://aitoolsguidebook.com/en/articles/git-commit-with-ai/)

6. **Name staging scope, branch, and PR intent explicitly** — “Stage all tracked+untracked except secrets” vs path lists; target branch (`main`); push-only vs also open a PR.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

7. **For agent push on Windows: separate “user can push” from “agent can push”** — Dual-preflight the agent’s git binary and credential helper; prefer Git for Windows + GCM when PATH git is MSYS/no helper; missing `gh` alone ≠ missing credentials when GCM works. Fail closed rather than hang on prompts.  
   Source: [GCM configuration — credential.interactive](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md); [GCM for Windows — Automation](https://github.com/microsoft/Git-Credential-Manager-for-Windows/blob/master/Docs/Automation.md)
