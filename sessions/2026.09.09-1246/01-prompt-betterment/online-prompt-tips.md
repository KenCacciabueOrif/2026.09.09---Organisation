# Online prompt tips (git add / commit / push)

Actionable tips for agent briefs that publish via git. Sources checked 2026-09-09.

1. **State an explicit trust boundary for git** — Decide who may stage, who may commit, and who may push; write it in the refined prompt so implementer does not “helpfully” invent a different split. Solo branches can allow agent push if remote+branch are printed first.  
   Source: [Git Commits with AI Agents — AI Tools Guidebook](https://aitoolsguidebook.com/en/articles/git-commit-with-ai/)

2. **Put hard safety rules as imperatives** — Never commit secrets; never amend published commits; never force-push; never skip hooks. Prefer short, literal rules in `AGENTS.md` / the refined prompt over vague “be careful.”  
   Source: same guidebook + [Cursor Rules docs](https://cursor.com/docs/rules)

3. **Commit message = why, not file dump** — Before staging, answer: what was missing, smallest correct publish unit, and whether one commit covers one reason. Prefer conventional style matching repo history (`type(scope): …` + short body).  
   Source: [How I Taught My AI Coding Agent to Write Commit Messages That Don't Suck](https://dev.to/yureki_lab/how-i-taught-my-ai-coding-agent-to-write-commit-messages-that-dont-suck-16lg)

4. **Treat push auth as an environment preflight, not an afterthought** — On Windows, “user can push in their terminal” ≠ agent Shell can push. Prefer Git for Windows + Git Credential Manager (GCM); MSYS/pacman git often lacks a working helper. Dual-check remote reachability and agent `git`/credential helper before claiming success.  
   Sources: [GCM for Windows FAQ](https://github.com/Microsoft/Git-Credential-Manager-for-Windows/blob/master/Docs/Faq.md); [MSYS vs GfW credential issues](https://github.com/Microsoft/Git-Credential-Manager-for-Windows/issues/70)

5. **Fail closed on publish** — If push fails (auth, network, rejected), mark the session blocked / incomplete; do not report “complete” because commit exists locally only. Distinguish agent environment vs user credentials when diagnosing.  
   Source: project `AGENTS.md` / FAW push preflight law; scope-boundary pattern in [maverick scope-boundaries](https://github.com/thermiteau/maverick/blob/stable/docs/scope-boundaries.md)

6. **Stage intentionally; scan for secrets before commit** — List paths to include/exclude; never stage `.env`, credential files, or private keys. A short security pass beats a large “git add .”  
   Source: [commit-guardian agent template](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/agents/git/commit-guardian.md)

7. **Write session evidence before the commit when the commit is the publish artifact** — Implementation/session logs that must be in the same commit should be finalized before `git commit`, so the published tree matches the claimed work.  
   Source: project `AGENTS.md` (single-commit publish note); complements tip 3 atomicity.

8. **Name the git root as a hard boundary** — In multi-folder workspaces (e.g. several trees under `C:\Project`), state absolute repo root in AC and forbid staging/committing outside it. Treat each git root as atomic unless a dedicated git-strategy plan says otherwise.  
   Source: project `AGENTS.md` (git-root atomicity); complements tip 1 trust boundary.
