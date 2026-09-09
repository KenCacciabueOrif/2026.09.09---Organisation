# Research brief

## Recommended approach

Project-scoped `.cursor/agents` + `full-agent-workflow` skill + always-apply rule + `sessions/` templates + `AGENTS.md`.

## Options considered

1. Parent-as-orchestrator (chosen) — matches Cursor Task delegation model
2. Only orchestrator subagent nested — extra hop, weaker UX
3. Skills-only without subagents — loses context isolation per phase

## Canonical references

- https://cursor.com/docs/subagents
- https://cursor.com/blog/agent-best-practices
- `AGENT-AND-WORKFLOW-BEST-PRACTICES.md`
