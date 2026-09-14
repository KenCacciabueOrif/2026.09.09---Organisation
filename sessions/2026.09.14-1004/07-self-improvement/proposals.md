# Improvement proposals

| ID | Area | Problem | Proposed change | Files likely touched |
| --- | --- | --- | --- | --- |
| P1 | planner / prompt-betterment | Norminette-style **80**-col 42 art vs flake8/PEP8 **79** is rediscovered each Python-header cycle | Encode Continuity default: for **Python** prework / flake8 goals, prefer **≤79 generator** over classic 80 art or ignore-first; disclose Norminette-80 tradeoff in Risks; do not raise flake8 max as primary fix | `.cursor/agents/planner.md`, `.cursor/agents/prompt-betterment.md`, `.cursor/agents/researcher.md` |
| P2 | planner / implementer | Local installed-extension **`dist/` patch** worked but was not named as `product_settings` pattern; Marketplace overwrite risk easy to omit | Expand `product_settings` to include local `~\.cursor\extensions\…\dist\` (or `src/`) patches; require **re-apply after Marketplace/Open VSX update** in plan AC + implementer log; never stage product extension paths into org-repo | `.cursor/agents/planner.md`, `.cursor/agents/implementer.md`, `sessions/_templates/03-plan.md`, `sessions/_templates/04-log.md` |
| P3 | implementer / auditor | Soft Reload documented after install/switch only — same tip needed after **dist patch** | Soft Reload after patching `dist/extension.js` (or equivalent); still Low tip, not blocker / not `rework_owner: user`; auditor checklist: re-apply docs present when dist patch claimed | `.cursor/agents/implementer.md`, `.cursor/agents/auditor.md`, handoff-templates |
| P4 | prompt-betterment | “Ignore-first” vs generator can be re-asked | When goal says header too long / flake8 E501: disclosed default = **fix generator** (settings or local patch) + fixture proof; `# noqa` / ignore / max-line-length raise = escape only | `.cursor/agents/prompt-betterment.md` |
| P5 | orchestrator / skill | Dual mid+final + auditor persist already law; cycle still flagged mid checklist lag + final pending | Light reinforce only in self-improver focus / handoff (no rewrite) — mid SESSION flip before auditor; persist `06-audit/report.md`; final closing pass after 07 | handoff-templates self-improver focus line |
| P6 | SKILL / AGENTS | `product_settings` blurb omits dist-patch + re-apply | One-sentence extend in SKILL product_settings bullet (and AGENTS only if short) | `.cursor/skills/full-agent-workflow/SKILL.md` |

## Online best-practice notes

- **Skills stay focused; put detail in references** — Cursor skills docs: keep `SKILL.md` concise; move repeatable domain patterns into agent prompts / templates rather than bloating the skill. Adopted: encode Norminette/flake8 + dist-patch in agents/templates; one short SKILL bullet only. — https://cursor.com/docs/skills
- **Subagents: one responsibility + independent verification** — Prefer specialized agents and a readonly verifier after implementation. Adopted: keep auditor readonly + orchestrator persist (already law); reinforce in focus line only. — https://cursor.com/docs/subagents
- **Rules vs skills** — Short always-on Continuity → agents/rules; multi-step FAW stays in skill. Adopted: P1–P4 in agents; no new always-apply rule dump. — https://cursor.com/blog/agent-best-practices

## Apply now vs defer

- **Apply now:** P1–P5 (concise agent/template/handoff/skill edits).
- **Defer:** Upstream ensui PR / configurable width (product, not FAW); user PATH chores (forbidden by mandate).
