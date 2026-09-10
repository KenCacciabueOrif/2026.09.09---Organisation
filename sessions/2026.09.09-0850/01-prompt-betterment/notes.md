# Prompt betterment notes

## Assumptions (defaults applied; not re-asked)

- User credentials already work in the interactive Cursor/PowerShell terminal; the gap is **agent execution context**, not first-time GitHub login.
- Desired outcome is a **durable workflow change** so future `/full-agent-workflow` publish steps can push from the agent (or fail closed with clear remediation)—not a one-off manual push.
- Prefer documenting Shell permissions / credential-helper inheritance / non-interactive checks over mandating SSH rewrite unless research shows HTTPS+GCM cannot work from agent Shell.
- Scope stays inside organisation agent/skill/rule/template docs; tiny helper scripts only if necessary.
- No secrets in repo; existing `blocked` / `user_credentials` honesty semantics stay.

## Clarifying questions

None asked this cycle — prior answers + orchestrator defaults were sufficient.

Deferred (optional user preference; researcher may still probe):

1. If both HTTPS+GCM fix and SSH work, which is preferred long-term? → **Default:** keep HTTPS if agent can inherit GCM; else SSH.
2. Is installing `gh` on the agent PATH acceptable as part of remediation docs? → **Default:** yes as optional documented step, not required if GCM inheritance works.
3. Must a live agent `git push` be proven in this cycle, or is documented + preflight-verified sufficient? → **Default:** prefer live smoke if safe; else documented preflight + fail-closed behavior is enough for audit.

## Open risks

- Cursor may intentionally disable credential helpers / interactive GCM in some spawn paths; docs-only fixes might not be enough without Shell permission or remote-URL changes.
- Agent environment may lack `gh` even when user PATH has it — PATH inheritance must be verified.
- Over-broad “always request elevated Shell” guidance could conflict with enterprise safety/allowlists.
- False confidence: updating “mark blocked” docs without a working push path leaves publish goals permanently blocked.
- Research might conclude only user-side setup (SSH keys, `gh auth login`, credential helper config) can fix it — then workflow must encode that as an explicit **user remediation** gate before `ready_to_implement: yes` on push goals.

## Key alignment vs raw goal

| Raw | Refined |
| --- | --- |
| “make git push work in future workflow” | Durable tooling change for agent Shell push when user terminal already authenticated |
| Implied maybe re-auth | Confirmed: no new user auth needed in terminal; fix inheritance / invocation / fallback |
| Unspecified approach | Prefer credential-helper / Shell guidance; SSH/`gh` as researched fallbacks |
| Unspecified DoD | Observable acceptance criteria + no secrets + fail-closed blocked |
