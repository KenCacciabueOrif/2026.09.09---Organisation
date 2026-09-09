# Realization & process audit

## Good points

- User requirements mapped 1:1 to agents and folders
- Best-practices doc locations respected
- Mandatory self-improvement encoded in orchestrator, skill, and rule

## Bad points

- Initial `_templates` omitted `02-codebase-findings` and `02-online-findings`
- No helper script to bootstrap a session folder in one command
- Auditor `readonly: true` may block writing `report.md` (orchestrator must persist)

## Evidence

- `sessions/_templates/` listing before fix
- `.cursor/agents/auditor.md` frontmatter
