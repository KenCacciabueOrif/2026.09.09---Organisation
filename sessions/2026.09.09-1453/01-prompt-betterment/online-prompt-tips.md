# Online prompt tips (pull + allowlist conflict resolve)

Goal type: finish a blocked `git pull` / merge after allowlist-only conflicts, with an explicit resolve rule.

1. **Name the operation before “ours/theirs”** — During a **merge**, `ours` = current branch (HEAD), `theirs` = incoming (`origin/main`). Labels flip under rebase; this cycle is merge (Q2=B), so keep merge semantics in the refined prompt.  
   Sources: [ast.rocks — ours/theirs](https://ast.rocks/blog/git-merge-strategies/), [somaz — merge vs rebase](https://somaz.blog/category/cicd/git-merge-vs-rebase/)

2. **Prefer intent merge over blind side-pick for docs** — For FAW meta/session markdown edited on both sides, pure `--ours` or `--theirs` risks silently dropping remote or local workflow improvements. A **combined** resolve (keep both intents, remove markers) matches “both sides meant to improve the same files.”  
   Sources: [knowledgelib.io — conflict strategies](https://knowledgelib.io/software/debugging/git-merge-conflicts/2026), [School of Web — resolve structure](https://schoolofweb.net/en/posts/git-workflow-4-conflict-resolution-mergetool-rerere/)

3. **Never confuse `-X ours` with `-s ours`** — `-X ours/theirs` only tie-breaks conflicted hunks while still merging; `-s ours` records a merge and **discards the other tree**. Encode “no `-s ours`” in constraints.  
   Sources: [ast.rocks](https://ast.rocks/blog/git-merge-strategies/), [Uniqcret Part 5](https://www.uniqcret.com/post/git-merge-conflicts-strategies)

4. **Bound resolve paths in the prompt** — State every conflict path must stay on the FAW dirty allowlist; any outside path → fail-closed abort (same as Q3b=A). Prevents scope creep into corpus files.  
   Sources: pull-cycle pack (repo); [knowledgelib.io](https://knowledgelib.io/software/debugging/git-merge-conflicts/2026)

5. **Verify after resolve, don’t assume** — Acceptance criteria should require: markers gone, `git add` of conflict paths, merge completed, HEAD incorporates `origin/main`, and a short post-resolve sanity check (status / log) — not “conflict gone” alone.  
   Sources: [knowledgelib.io](https://knowledgelib.io/software/debugging/git-merge-conflicts/2026)

6. **Keep user questions tiny for finish-sync** — Lock one irreversible choice (resolve rule); disclose defaults for the rest. Minimizes another cleanup cycle.  
   Sources: Cursor subagents / focused prompts practice; prior session self-improvement workload note

7. **Fail-closed language in AC** — On non-allowlist conflict, auth/env fail, or incomplete merge: session `blocked` + typed `blocker_type`; never mark pull complete; no force/hard reset/`--no-verify`.  
   Sources: pull-cycle.md (repo); [knowledgelib.io](https://knowledgelib.io/software/debugging/git-merge-conflicts/2026)
