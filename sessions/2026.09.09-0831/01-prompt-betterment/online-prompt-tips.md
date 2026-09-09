# Online prompt tips (git add / commit / push)

Actionable prompting practices for agent-run git publish tasks.

1. **Spell the full git workflow as numbered steps** — Inspect (`status`/`diff`/`log`), stage named paths, commit with a clear message, push, then return verification (hash, branch, remote). Vague “commit and push” invites wrong files or skipped checks.  
   Source: [Cursor — Best practices for coding with agents (Git workflows)](https://cursor.com/blog/agent-best-practices)

2. **Require a verifiable definition of done** — Success should be checkable commands/outputs (e.g. clean relevant staging, `git status` after commit, push succeeded, no force-push). Agents perform better with concrete success signals.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

3. **State goal + hard constraints in the same brief** — Explicitly forbid force-push, `git config` edits, `--no-verify`, amend-unless-allowed, and secret paths (`.env`, credentials, keys). Constraints next to the goal reduce unsafe defaults.  
   Source: [Learn Cursor — writing good prompts](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

4. **Analyze the diff before writing the commit message** — Message must match staged content (why-focused, repo style). Prefer conventional/`type: summary` only if the history uses it; otherwise match recent `git log` style.  
   Source: [oleg-koval agent-skills — git-commit](https://github.com/oleg-koval/agent-skills/blob/HEAD/packages/software-development/git-commit/SKILL.md)

5. **Mandate a pre-commit secrets gate** — Before commit, scan staged names/content for `.env*`, `*credentials*`, `*.pem`/`*.key`, and token/password patterns; **stop and report** if found.  
   Source: [fusengine agents — commit-pro](https://github.com/fusengine/agents/blob/main/plugins/commit-pro/commands/commit.md)

6. **Name staging scope explicitly** — “Stage all tracked+untracked except X” vs “only these paths.” Avoid silent `git add -A` when large new trees (e.g. `.cursor/`, `sessions/`) are present.  
   Source: [charlesjones-dev ai-git plugin README](https://github.com/charlesjones-dev/claude-code-plugins-dev/blob/main/plugins/ai-git/README.md)

7. **Confirm branch/remote intent** — State target branch (`main` vs feature), remote (`origin`), and whether push-only or also open a PR. Pushing to `main` without saying so is a common misalignment.  
   Source: [Cursor agent workflows (git automation)](https://understandingdata.com/posts/cursor-agent-workflows/)
