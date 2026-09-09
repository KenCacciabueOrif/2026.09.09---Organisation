# Prompt betterment notes

## Clarifying questions — all answered

1. **Staging scope:** Stage everything (all dirty/untracked: `README.md`, `.cursor/`, `AGENTS.md`, `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`, `sessions/`, etc.).
2. **Commit message:** Auto-generate from the diff; no user-supplied fixed message.
3. **Branch:** Commit and push on **`main`**.
4. **Remote:** Push only to **`origin`**; **no PR**.
5. **Secrets / excludes:** No extra must-exclude paths; still apply secrets gate (never commit secrets).
6. **Done signal:** Commit hash + push OK + `git status` only; no remote/`gh` verification.

## Assumptions (confirmed)

- User intent is publish-local-work only: add → commit → push; no product implementation in this cycle.
- Full working-tree stage is intentional for organisation-repo bootstrap (`.cursor/`, `sessions/` included).
- Message authoring is the implementer’s responsibility from the staged diff + log style.
- Force-push and config changes remain forbidden.

## Open risks

- **Direct push to `main`** with a large first content drop — accepted by user; still use secrets gate and clear failure reporting.
- **Sessions folder** is included going forward; future sessions may contain sensitive notes — secrets gate remains the control.
- **Tree may change** between betterment and implement — re-run `status`/`diff` immediately before stage.
- **Hooks / auth:** push may fail on GitHub auth or pre-push hooks; report clearly; do not retry with unsafe flags.

## Handoff

- Refined prompt is **finalized**; ready for researcher (and subsequent) phases.
