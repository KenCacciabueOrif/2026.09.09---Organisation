# Online prompt tips — Cycle 14 (scoped FS isolation + plan gate)

Actionable tips for Continuity B / Appendix A `fs_mutation` STAGE 1 (plan only; human-held gate).

1. **State goal + hard constraints in the same brief** — Pair the outcome (“relocate named parent trees”) with non-negotiables (atomic nested `.git`, no remote/history rewrite, no whole-tree archive). Vague “clean up WorkSpace” invites over-scope.  
   Source: https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts

2. **Plan before mutate; approve before build** — Treat the planner artifact as the only executable map; Continuity Choose ≠ permission to move files. Match Cursor Plan Mode: research → plan with paths → wait for explicit approval.  
   Source: https://cursor.com/blog/agent-best-practices

3. **Bound the job with a testable done-condition** — Encode exit checks (e.g. nested roots 7→5 if both parents move; destinations free; remotes unchanged; row stays in progress). “Implement the feature” is not an AC.  
   Source: https://otf-kit.dev/blog/cursor-agent-best-practices

4. **Name targets + out-of-scope peers explicitly** — Verb + concrete paths + “do not touch” list (live primary roots, archived Multi-experiment peers, Medium/Early). Prevents context drift into whole-tree or peer reopen.  
   Source: https://baeseokjae.github.io/posts/cursor-agent-best-practices-2026/

5. **Point at canonical law files; don’t paste them** — Reference `program/git-strategy-workspace-hazards.md` Appendix A / safe relocation rules and prior illustrative map; keep the refined prompt short so rules stay authoritative.  
   Source: https://cursor.com/blog/agent-best-practices

6. **Fail-closed on nested-git / destructive ambiguity** — Prefer intact tree moves; never strip `.git`, force-push, or silent delete of repo metadata. Agent tooling patterns block irreversible git-admin deletes unless explicitly gated.  
   Source: https://github.com/mokuyoaxis/agent-guard

7. **Verify each nested root before and after** — Re-check `git rev-parse --show-toplevel` / worktree list immediately before any approved move; treat unexpected extra worktrees as abort.  
   Source: https://dev.to/arafatruetbd/how-i-accidentally-pushed-extra-folders-to-github-and-how-to-fix-it-1dje
