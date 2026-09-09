# Agent Creation & Workflow Best Practices

A practical guide focused on **Cursor**, drawn from Cursor’s official docs and blog, plus widely cited community practices (2026). Use this as a living checklist for setting up agents, skills, rules, and day-to-day workflows.

---

## Table of contents

1. [Core mental model](#1-core-mental-model)
2. [Choose the right mode](#2-choose-the-right-mode)
3. [Plan before you code](#3-plan-before-you-code)
4. [Prompting & task design](#4-prompting--task-design)
5. [Context management](#5-context-management)
6. [Rules (`AGENTS.md` & `.cursor/rules`)](#6-rules-agentsmd--cursorrules)
7. [Skills (workflows & slash commands)](#7-skills-workflows--slash-commands)
8. [Custom subagents](#8-custom-subagents)
9. [Hooks](#9-hooks)
10. [Verification, TDD & review](#10-verification-tdd--review)
11. [Parallel & cloud agents](#11-parallel--cloud-agents)
12. [Safety & Git hygiene](#12-safety--git-hygiene)
13. [Workflow maturity ladder](#13-workflow-maturity-ladder)
14. [Quick reference checklists](#14-quick-reference-checklists)
15. [Sources](#15-sources)

---

## 1. Core mental model

An agent harness has three parts:

| Piece | Role |
| --- | --- |
| **Instructions** | System prompt + rules + skills that shape behavior |
| **Tools** | Search, edit, terminal, browser, MCP, etc. |
| **Model** | The model you pick for the task |

**Implications:**

- Different models respond differently to the same prompt; pick the model for the job (planning vs fast edits vs deep reasoning).
- Your job is less “write perfect prompts every time” and more **encode durable guidance** (rules/skills) + **give verifiable goals** (tests, linters, acceptance criteria).
- Treat the agent as a capable collaborator: ask for plans, request explanations, push back on bad approaches.

---

## 2. Choose the right mode

| Mode | Use when | Avoid when |
| --- | --- | --- |
| **Plan** | Multi-file features, unclear requirements, architecture decisions | One-line typo fixes |
| **Ask** | Exploring, onboarding, “how does X work?”, read-only research | You already need code written |
| **Agent** | Scoped implementation with a clear goal | Open-ended product discovery with no plan |
| **Debug** | Reproducible but hard bugs, races, perf, regressions | Simple logic bugs you can fix from reading code |

**Shortcuts (typical):** `Shift+Tab` toggles Plan; `Ctrl+.` / `Cmd+.` cycles modes.

**Mode-switching pattern that works well:**

1. **Ask** — understand the codebase  
2. **Plan** — produce a reviewable plan  
3. **Agent** — implement  
4. **Debug** — only if something still fails under runtime conditions  

If Agent builds the wrong thing: **revert → refine the plan → run again**. Do not steer a bad run with ten follow-up prompts.

---

## 3. Plan before you code

Planning is the highest-leverage habit for multi-file work.

**Plan Mode does:**

1. Research relevant files  
2. Ask clarifying questions  
3. Produce a plan with paths and code references  
4. Wait for your approval before building  

**Practices:**

- Edit the plan markdown before hitting Build (remove noise, add constraints, reorder steps).
- Save plans to `.cursor/plans/` so teammates / future sessions can resume.
- Not every task needs a plan — skip for small, familiar changes.
- For large tickets, break scope: prefer “JWT middleware on `/api/users` only” over “add authentication to the API.”

---

## 4. Prompting & task design

A strong prompt usually includes:

1. **Goal + constraint** — what to build and what not to touch  
2. **Context pointers** — `@file` only when you know the canonical place; otherwise let the agent search  
3. **Plan request** — use Plan Mode for non-trivial work  
4. **Verification** — tests, commands, or acceptance criteria  

**Prefer specific over vague:**

| Weak | Strong |
| --- | --- |
| Add tests for auth | Write tests for `auth.ts` logout edge cases using patterns in `__tests__/`; do not mock the DB |
| Fix the bug | Reproduce from steps X; failing test is Y; fix root cause without changing public API |
| Improve performance | Profile `listOrders`; reduce N+1 queries; keep response shape identical |

**Other habits:**

- One primary task per chat; spin tangents into a new chat.
- Show an example of the pattern you want (or `@` a canonical file).
- Use `/goal` for long-lived objectives the agent should pursue to completion.
- Queue follow-ups while the agent works; use immediate send only when you need to steer.

---

## 5. Context management

**Do:**

- Let the agent find files via search; tag only when you know the exact file.
- Start a **new conversation** when switching features, when the agent loops on mistakes, or after a logical unit of work.
- Use `@Past Chats`, `@Branch`, and similar references instead of pasting entire histories.
- Watch the context gauge; summarize or restart when effectiveness drops.

**Don’t:**

- Dump half the repo into context “just in case.”
- Continue a long, noisy chat hoping more prompts will fix confusion.
- Paste secrets, credentials, or huge unrelated logs.

Irrelevant files confuse the agent about what matters.

---

## 6. Rules (`AGENTS.md` & `.cursor/rules`)

Rules are **static, always-available guidance**. Skills are **on-demand workflows**.

### Layered setup (recommended)

| Layer | Where | Purpose |
| --- | --- | --- |
| Shared cross-tool | `AGENTS.md` (repo root) | How we code — portable across Cursor, Codex, etc. |
| Cursor-scoped | `.cursor/rules/*.mdc` | Glob-scoped or always-on Cursor rules |
| User | Cursor Settings → User Rules | Personal preferences across projects |
| Team | Cursor Team Rules (dashboard) | Org-wide standards |

**Precedence (typical):** Team → Project → User. Prefer one source of truth for shared content to avoid drift. Migrate away from legacy `.cursorrules`.

### Rule activation modes (`.mdc`)

| Mode | Frontmatter | Best for |
| --- | --- | --- |
| Always Apply | `alwaysApply: true` | Tiny set of universal constraints |
| Specific files | `globs: **/*.tsx` | Framework/file-type conventions |
| Intelligently | `description: "..."` | Situational domain guidance |
| Manual | `@rule-name` | Rare playbooks |

### Writing good rules

- Keep focused and short (aim well under ~500 lines; prefer ~50-line focused files).
- One concern per file (`react-patterns.mdc`, `api-validation.mdc`).
- Include **commands to run**, **patterns to follow**, and **pointers to canonical files** — not full style guides.
- Reference files instead of copying them (avoids staleness).
- Add a rule only after the agent repeats the same mistake.
- Check rules into git.

### What to put in rules

```markdown
# Commands
- npm run typecheck
- npm run test -- path/to/file

# Code style
- ES modules only; see components/Button.tsx for structure

# Workflow
- Typecheck after a series of edits
- API routes live in app/api/ following existing patterns
```

### What not to put in rules

- Entire style guides (use linters/formatters)
- Every CLI flag the agent already knows
- Rare edge cases that bloat every chat

---

## 7. Skills (workflows & slash commands)

Skills package **reusable procedures** the agent loads when relevant (or when you type `/skill-name`).

### Locations

| Scope | Path |
| --- | --- |
| Project | `.cursor/skills/` or `.agents/skills/` |
| User | `~/.cursor/skills/` or `~/.agents/skills/` |
| Compat | Also loads `.claude/skills/`, `.codex/skills/` |

Monorepos can nest skills under packages; nested skills are scoped to that directory. Prefer **project skills** for team workflows.

### `SKILL.md` essentials

```markdown
---
name: deploy-staging
description: Deploy the app to staging and verify health checks. Use when deploying, releasing to staging, or the user mentions staging deploys.
paths:
  - "apps/web/**"
disable-model-invocation: false
---

# Deploy Staging

## Steps
1. Run `scripts/validate.py`
2. Run `scripts/deploy.sh staging`
3. Confirm health endpoint returns 200
```

**Frontmatter practices:**

- `name`: lowercase, hyphens, matches folder name  
- `description`: third person; include **WHAT** and **WHEN** (trigger terms) — discovery depends on this  
- `paths`: scope to file globs when skill is domain-specific  
- `disable-model-invocation: true`: slash-command style (only when explicitly invoked)  
- Keep `SKILL.md` under ~500 lines; put detail in `references/`, scripts in `scripts/`

### Skill authoring principles

1. **Concise** — assume the model is smart; only add what it doesn’t know.  
2. **Progressive disclosure** — link to `references/` one level deep.  
3. **Match freedom to fragility** — scripts for fragile ops; prose for judgment calls.  
4. **Concrete steps + verification loops** — “run X; if fail, fix; only proceed when green.”  
5. **Consistent terminology** — one name for each concept.  
6. Create with `/create-skill`; migrate old commands/rules with `/migrate-to-skills`.

### Skills vs rules vs subagents

| Need | Use |
| --- | --- |
| Always-on project law | Rules / `AGENTS.md` |
| Repeatable workflow (“ship a PR”, “run TDD”) | Skill |
| Long research / parallel / separate context | Subagent |
| Enforce policy at tool time | Hook |

### Useful built-in Cursor skills (examples)

`/create-rule`, `/create-skill`, `/create-subagent`, `/create-hook`, `/migrate-to-skills`, `/review`, `/loop`, `/split-to-prs`, `/automate`

---

## 8. Custom subagents

Subagents are specialized assistants with **their own context window**. The parent delegates; the child returns a summary.

### When to create a subagent

| Create a subagent when… | Prefer a skill when… |
| --- | --- |
| Long research would bloat main chat | One-shot repeatable action |
| Parallel workstreams | No need for isolated context |
| Specialized multi-step expertise | Single-purpose formatting / changelog |
| Independent verification of work | Quick slash workflow |

### File locations

| Type | Path |
| --- | --- |
| Project | `.cursor/agents/*.md` |
| User | `~/.cursor/agents/` |
| Compat | `.claude/agents/`, `.codex/agents/` |

### Format & config

```markdown
---
name: verifier
description: Validates completed work. Use after implementation to run tests and report pass/fail gaps.
model: inherit
readonly: true
---

You verify completed work.
1. Run the relevant tests and typecheck
2. Confirm acceptance criteria from the plan
3. Report what passed vs what is incomplete — do not expand scope
```

| Field | Guidance |
| --- | --- |
| `description` | Critical for auto-delegation — write like a job posting for when to call this agent |
| `model` | `inherit` by default; pin a model for cost/speed/reasoning needs |
| `readonly` | `true` for auditors/reviewers |
| `is_background` | `true` for long parallel work |

### Subagent design practices

- Give the parent enough context in the handoff prompt (subagents don’t see prior chat).
- Prefer **narrow roles**: explorer, planner, implementer, verifier, security auditor.
- Return structured results (findings by severity, file list, next steps).
- Don’t over-split: a skill is enough for small verbs.
- Use built-ins (Explore / Bash / Browser) automatically for noisy intermediate work.
- Create via `/create-subagent` or by asking Agent to scaffold `.cursor/agents/`.

---

## 9. Hooks

Hooks run scripts around agent lifecycle events (e.g. `beforeShellExecution`, `afterFileEdit`, `stop`).

**Practices:**

- Define project hooks in `.cursor/hooks.json` (required for Cloud Agents — user `~/.cursor/hooks.json` is **not** loaded in cloud VMs).
- Use matchers so hooks stay fast (don’t run heavy logic on every tool call).
- Block dangerous shell patterns with `beforeShellExecution` + fail-closed where appropriate.
- Use `stop` hooks for grind loops (“keep going until tests pass / scratchpad says DONE”), with a hard iteration cap.
- Prefer `/create-hook` to scaffold safely.
- Cloud agents: command-based hooks only; several IDE-only events do not apply.

**Example pattern (iterate until done):**

```json
{
  "version": 1,
  "hooks": {
    "stop": [{ "command": "bun run .cursor/hooks/grind.ts" }]
  }
}
```

---

## 10. Verification, TDD & review

Agents perform best against **verifiable signals**.

### Give the agent a target

- Typed languages + linters + tests  
- Explicit acceptance criteria in the plan  
- “Run `npm run typecheck` and `npm test` before finishing”

### Test-driven loop (Cursor-recommended)

1. Write tests from expected I/O; say you are doing TDD (no fake implementations).  
2. Run tests — confirm they fail; no implementation yet.  
3. Commit tests when happy.  
4. Implement without changing tests; iterate until green.  
5. Commit implementation.

### Review loop

| When | Action |
| --- | --- |
| During generation | Watch diffs; **Stop** early if direction is wrong |
| After generation | Review → Find Issues; Agent Review vs main |
| On PR | Bugbot / CI; human review of risky paths |
| Architecture | Ask for Mermaid diagrams of data flow before merge |

AI-looking-correct code can still be subtly wrong — review rises in importance as generation gets faster.

### Visual & browser workflows

- Paste screenshots / mockups for design-to-code or visual bugs.  
- Let the agent drive the browser to verify UI.  
- Prefer evidence (logs, screenshots, failing tests) over verbal descriptions alone.

---

## 11. Parallel & cloud agents

### Local parallelism

- Use **git worktrees** so agents don’t collide (`/worktree`, worktree option in agent UI).  
- Run **best-of-N** (same prompt, multiple models) on hard problems; pick the best.  
- Enable notifications/sounds when supervising many agents.  
- Apply/merge worktree results deliberately after review.

### Cloud agents

Best for todo-list work you can defer:

- Side bugfixes, refactors, tests, docs  
- Start from editor, [cursor.com/agents](https://cursor.com/agents), Slack (`@Cursor`), phone  

**Cloud checklist:**

- Put hooks/skills/rules needed in the **repo** (or sync personal skills explicitly).  
- Provide secrets via cloud environment config — not in prompts.  
- Expect a branch + PR; review before merge.  
- Good prompts still need goal, constraints, and verification steps.

---

## 12. Safety & Git hygiene

- **Checkpoints** = local undo for agent edits; **Git** = real audit trail. Commit small and often.  
- Prefer revert + better plan over compounding a bad session.  
- Allowlist auto-run commands carefully (tests/typecheck OK; destructive ops gated).  
- Never commit secrets; keep `.env` out of agent-generated commits.  
- Hooks can enforce policy (block `rm -rf`, force formatters, audit logs).  
- For PRs: small diffs, clear test plan, CI green before merge.

---

## 13. Workflow maturity ladder

Start simple; add machinery only when pain repeats.

| Stage | What to add |
| --- | --- |
| 0 — Manual | Specific prompts + Plan Mode + review diffs |
| 1 — Project law | Short `AGENTS.md` or 1–3 always/glob rules |
| 2 — Repeatable verbs | Skills for `/pr`, `/fix-issue`, TDD, deploy |
| 3 — Specialized roles | Custom subagents (verifier, security, explorer) |
| 4 — Guardrails | Hooks for safety, format, grind-until-green |
| 5 — Scale | Worktrees, best-of-N, cloud agents, team rules/skills |

**Team habit:** when the agent errs the same way twice → update a rule or skill (optionally `@cursor` on a GitHub issue/PR to have it propose the update).

---

## 14. Quick reference checklists

### Starting a multi-file task

- [ ] Switch to Plan Mode  
- [ ] State goal, constraints, and success checks  
- [ ] Answer clarifying questions; edit the plan  
- [ ] Build in Agent; watch the diff  
- [ ] Run tests/typecheck; review; commit  

### Creating a rule

- [ ] One concern; short; actionable examples  
- [ ] Correct activation (`alwaysApply` / `globs` / description)  
- [ ] Pointers to canonical files, not pasted dumps  
- [ ] Checked into git  

### Creating a skill

- [ ] Folder + `SKILL.md`; name matches folder  
- [ ] Description has WHAT + WHEN (trigger terms)  
- [ ] Steps + verification; scripts under `scripts/`  
- [ ] `paths` or nested dir if scoped; commit if team-shared  

### Creating a subagent

- [ ] Clear `description` for delegation  
- [ ] Narrow role; structured output  
- [ ] `readonly` for auditors; model choice intentional  
- [ ] Prefer skill if the job is one-shot  

### Recovering from a bad run

- [ ] Stop the agent  
- [ ] Restore checkpoint and/or `git checkout` / revert  
- [ ] Tighten the plan (files, constraints, tests)  
- [ ] New chat if context is polluted  
- [ ] Re-run  

---

## 15. Sources

Primary (Cursor):

- [Best practices for coding with agents](https://cursor.com/blog/agent-best-practices) — Lee Robinson, Jan 2026  
- [Cursor Agent overview](https://cursor.com/docs/agent/overview)  
- [Rules](https://cursor.com/help/customization/rules)  
- [Agent Skills](https://cursor.com/docs/context/skills)  
- [Subagents](https://cursor.com/docs/context/subagents)  
- [Hooks](https://cursor.com/docs/hooks)  
- [Cloud Agents](https://cursor.com/help/ai-features/cloud-agents)  

Useful secondary reading:

- [Cursor agent best practices: plan, scope, and verify](https://otf-kit.dev/blog/cursor-agent-best-practices)  
- [Agent Modes Deep Dive](https://developertoolkit.ai/en/cursor-ide/advanced-techniques/agent-modes-deep-dive/)  
- [AGENTS.md vs .cursorrules vs Skills (2026)](https://blog.buildbetter.ai/agents-md-vs-cursorrules-vs-claude-skills-2026-comparison/)  
- [AI coding workflow best practices 2026](https://www.youngju.dev/blog/culture/2026-05-14-ai-coding-workflow-best-practices-2026-claude-md-agents-md-cursorrules-subagent-skill-design-deep-dive.en)  
- [Agent Skills standard](https://agentskills.io)  

---

*Compiled for this organisation repo. Prefer updating this doc when Cursor product behavior changes or when the team discovers a repeatable improvement.*
