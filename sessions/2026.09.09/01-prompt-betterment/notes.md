# Prompt betterment notes

## Assumptions

- Parent chat acts as orchestrator when the skill/rule applies; `orchestrator.md` encodes the same contract for explicit delegation.
- First cycle may be bootstrapped without live Task subagent calls.

## Open risks

- Nested Task(orchestrator) vs parent-as-orchestrator confusion — mitigated by skill text: “you are the orchestrator.”
