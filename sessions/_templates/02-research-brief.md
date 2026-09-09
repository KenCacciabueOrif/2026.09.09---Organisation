# Research brief

## Recommended approach

## Options considered

1. 
2. 
3. 

## Required facts

## Unknowns / blockers

### Push/auth dual preflight (required when goal includes remote publish)

| Field | Value |
| --- | --- |
| Remote URL scheme | https \| ssh |
| Tracking branch | |
| Agent git path (`Get-Command` / `where`) | |
| Agent `credential.helper` (default binary) | |
| Prefer GfW path (Windows HTTPS)? | yes \| no \| n/a — path: |
| GCM / non-interactive evidence (fill or dry-run; **no secrets logged**) | pass \| fail |
| `gh` present? | yes \| no (optional signal only) |
| User-terminal push note (optional) | |
| `blocker_type` | none \| agent_environment \| user_credentials |
| Blocker / remediation | |

Do **not** list “blockers: none” when agent cannot push non-interactively. Missing `gh` alone ≠ credentials missing when GCM verified.

## Canonical references

- Title — URL — takeaway
