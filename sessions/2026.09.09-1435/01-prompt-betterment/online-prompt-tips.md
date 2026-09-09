# Online prompt tips (pull / merge sync brief)

Actionable prompting practices for this **agent git pull + merge** cycle. Sources accessed 2026-09-09.

1. **Spell success and stop conditions** — State a verifiable done-check (e.g. agent Shell sync AC met) and an explicit fail-closed stop (no force / hard reset / `--no-verify`). Vague “just sync” drifts into unsafe recovery.  
   Source: [Cursor Agent Best Practices 2026](https://baeseokjae.github.io/posts/cursor-agent-best-practices-2026/)

2. **Name paths, constraints, and non-goals in the brief** — List the git root, allowlisted dirty paths, and what must not change (siblings, corpus FS, taxonomy). Agents need guard rails + exit criteria, not only intent.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

3. **Prefer merge-based update when histories already diverged** — Prompt for fetch + merge (not silent rebase/ff-only) when local and remote both moved; encode “merge commit allowed” as a locked choice so later phases do not re-litigate.  
   Source: [pull — AI Agent skill (merge-oriented sync)](https://eliteai.tools/agent-skills/pull-1)

4. **On conflict: preserve intent, fail closed if ambiguous** — Instruct: summarize both sides’ intent before editing; keep WIP/stash recoverable; stop and report rather than guess product decisions or drop stash.  
   Sources: [Claude Code and Merge Conflicts (Patch Rewrite)](https://www.cvinfotech.com/blog/claude-code-merge-conflicts-git-safety/); [failclosed merge admission](https://github.com/OrionArchitekton/failclosed)

5. **Fail closed on unsafe git finish states** — Brief should forbid force-push, rewriting protected history, and treating “user terminal succeeded” as agent success when agent auth/env failed.  
   Source: [auto-git-finish-push skill (fail-closed git)](https://github.com/5046312/auto-git-finish-push)

6. **Checkpoint / durable WIP before risky combine steps** — Allowlist commit or path-scoped stash before merge so recovery is possible; never `stash drop` on conflict.  
   Source: [Cursor Agent Best Practices 2026](https://baeseokjae.github.io/posts/cursor-agent-best-practices-2026/) (git checkpoint before agent risk)

7. **Keep procedural git law in skills/rules; keep the cycle prompt outcome-focused** — Reference `pull-cycle.md` / FAW allowlist rather than pasting long procedure into every ask; refined prompt holds AC + locks.  
   Source: [Cursor Rules best practices](https://www.stackhawk.com/blog/cursor-rules/)
