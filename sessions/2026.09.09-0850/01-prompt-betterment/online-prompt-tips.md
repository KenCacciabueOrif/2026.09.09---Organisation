# Online prompt tips (agent git push / workflow hardening)

Actionable tips for refining prompts about non-interactive `git push` from Cursor agents and durable workflow docs. Not a domain solution design.

1. **State goal + constraint + verification in one brief** — Name the outcome (“agent `git push` succeeds when user shell already can”), the hard constraint (“no secrets in repo”), and a rerunnable check (exact command + expected exit). Vague “make push work” hands judgment back to the agent.
   - Source: https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts

2. **Point at known files; keep one job** — Scope the prompt to workflow artifacts (agents, skill, rules, templates, `AGENTS.md`) and prior failure evidence; avoid open-ended product invention.
   - Source: https://www.learncursor.dev/guides/prompt-engineering-for-developers

3. **Acceptance criteria must be observable stopping conditions** — Prefer checklists like “implementer handoff documents Shell permission / credential-helper guidance” and “preflight fails closed with `blocked` when push auth unverified,” not “push feels fixed.”
   - Source: https://otf-kit.dev/blog/cursor-agent-best-practices

4. **Separate model guidance from security boundaries** — Rules/skills shape behavior; do not treat them as a guarantee that credentials are available. Prompt the researcher to distinguish “document how to invoke Shell so GCM/helpers work” vs “store tokens.”
   - Source: https://cursor.com/docs/enterprise/llm-safety-and-controls

5. **Encode the known failure mode in the brief** — Capture exact errors (`terminal prompts disabled`, missing `gh`) and the contrast (user PowerShell push succeeded without re-auth) so later phases diagnose environment inheritance, not missing login.
   - Source (similar Cursor HTTPS / helper gap): https://forum.cursor.com/t/git-push-fails-with-could-not-read-username-for-https-github-com-device-not-configured-credential-helper-not-used-when-source-control-runs-git/151765

6. **Prefer fail-closed non-interactive git over hung prompts** — GCM docs: disable interactive prompts in automation so missing credentials fail immediately; cached credentials should still work when the helper is reachable.
   - Source: https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md
   - Env twin: https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/environment.md (`GCM_INTERACTIVE`)

7. **Keep SSH / remote rewrite as a researched fallback, not the default ask** — Community guidance often recommends SSH or `gh` as credential helper when HTTPS helpers fail in Cursor-spawned git; only adopt after research confirms agent Shell cannot inherit GCM.
   - Source: https://forum.cursor.com/t/git-push-fails-with-could-not-read-username-for-https-github-com-device-not-configured-credential-helper-not-used-when-source-control-runs-git/151765
