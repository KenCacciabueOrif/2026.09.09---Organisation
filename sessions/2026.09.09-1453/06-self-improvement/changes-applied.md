# Changes applied — session `2026.09.09-1453`

**Focus:** diminish user workload after a successful finish-sync (merge `bee1667`). Harden FAW so the 1332→1350→1435 deadlock is less likely to dump Choose/resolve chores on the user.

## Applied

| Path | What | Why |
| --- | --- | --- |
| `.cursor/skills/full-agent-workflow/references/pull-cycle.md` | Finish-sync continuity defaults: **Q3b=B** + R1 **`combined-best`**; standing R1 vocabulary; next-cycle allowlist-only remediation = **agent-owned**; auditor note `rework_owner: orchestrator` not user | Encode autonomy so unanswered→Choose finishes sync without another ask / user resolve |
| `.cursor/agents/prompt-betterment.md` | Finish-sync locks B+combined-best; do not invent user-resolve chores | Fewer clarifying questions on continuity |
| `.cursor/agents/orchestrator.md` | Allowlist-only `merge_conflict` → carry Continuity locks; agent-owned next FAW | Stop primary remediation “user must resolve” |
| `.cursor/agents/auditor.md` | `rework_owner: orchestrator` for allowlist-only conflict abort; enum includes orchestrator; user reserved for unrelated/non-allowlist/credentials | Align ownership with workload mandate |
| `.cursor/agents/implementer.md` | Blank R1 under finish-sync Q3b=B → default `combined-best`; remediation text agent-owned | Implement without waiting on user for FAW docs |
| `.cursor/agents/self-improver.md` | Standing **user-workload mandate** | Prevent future backlog that assigns recurring checks to the user |
| `.cursor/skills/full-agent-workflow/references/handoff-templates.md` | Pull/auditor/self-improver handoffs carry continuity + workload priority | Orchestrator handoffs match pack |
| `.cursor/skills/full-agent-workflow/SKILL.md` | Dirty-policy finish-sync continuity line | Skill standing law |
| `.cursor/rules/full-agent-workflow.mdc` | Q3b=B via Choose **or** finish-sync continuity | Always-on rule |
| `AGENTS.md` | Finish-sync continuity + agent-owned allowlist remediation | Portable project law |
| `sessions/_templates/01-notes.md` | Continuity pointer for Q3b/R1 finish-sync locks | Template memory |

## Celebrated (this cycle — no change needed)

- Dual preflight GfW+GCM, allowlist commit, Q2=B merge, Q3b=B gate, combined-best judgment trail, ancestor check — **sync AC met**.

## Explicit non-claims / still fail-closed

- Unrelated dirty and non-allowlist conflicts still abort; no force-push / hard reset.
- Generic first-time ff-only pull still defaults Q3b=**A** (no silent resolve without continuity or Choose).
- Push remains OOS this cycle (`ahead 4`).
