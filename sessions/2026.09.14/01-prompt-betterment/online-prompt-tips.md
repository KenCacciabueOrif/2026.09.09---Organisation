# Online prompt tips — ad-hoc UI / extension bug fix

Goal type: locate-or-ask product bug (long email breaks a “42” header), then scoped fix with clear acceptance criteria.

## Actionable tips

1. **State expected vs actual, not only “fix it”.** Agents need the rule that should hold (e.g. full email + closing `>` still present; Norminette-clean header) versus what happens now (truncated line, layout overflow).  
   Sources: [QA Wolf — great bug reports](https://www.qawolf.com/blog/what-makes-a-great-bug-report), [Claude CodeLab bug template](https://claudecode-lab.com/en/blog/claude-code-bug-report-template/)

2. **Give numbered reproduction from a known start state.** “Open file → insert header / save → observe By: line” beats a one-line symptom. Prefer an executable repro (sample email setting + insert) when possible.  
   Sources: [QA Wolf](https://www.qawolf.com/blog/what-makes-a-great-bug-report), [arXiv: What Makes a Good Bug Report for an AI Agent?](https://arxiv.org/html/2607.07593v1)

3. **Pin the product and workspace before editing.** For multi-root trees, require locate-or-ask (which extension/repo path) so the agent does not “fix” unrelated open files (e.g. school exercises).  
   Sources: [Cursor agent best practices](https://cursor.com/blog/agent-best-practices), [OTF — plan, scope, verify](https://otf-kit.dev/blog/cursor-agent-best-practices)

4. **Plan before multi-file edits; approve the path.** Require a short plan naming files and the verification check; revert + replan beats compounding wrong patches.  
   Sources: [Cursor blog — Plan Mode](https://cursor.com/blog/agent-best-practices), [Learn Cursor — good prompts](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

5. **Encode hard acceptance criteria in the brief.** “Done when: long email (≥N chars) produces a valid 42 header; short emails unchanged; named verify command or visual check.”  
   Sources: [PromptChief — bug fix brief](https://promptchief.tech/p/bug-fix-brief-for-an-ai-agent.html), [OTF](https://otf-kit.dev/blog/cursor-agent-best-practices)

6. **Separate facts from hypotheses; smallest useful fix.** Instruct later phases to list top hypotheses, disprove with a minimal check, then patch — especially for layout/padding bugs.  
   Sources: [Cursor Debug Mode docs](https://cursor.com/docs/agent/debug-mode), [Claude CodeLab](https://claudecode-lab.com/en/blog/claude-code-bug-report-template/)

7. **Scope guardrails: what not to touch.** Explicit out-of-scope (other extensions, Intra chrome, unrelated school repos, force-publish) prevents drive-by refactors.  
   Sources: [PromptChief bug brief](https://promptchief.tech/p/bug-fix-brief-for-an-ai-agent.html), [NewPrompt triage template](https://newprompt.net/resources/bug-triage-assistant)

## Domain note (not a locked fact)

Public reports describe a known class of bug in **VS Code / Cursor “42 Header”** extensions: emails longer than a fixed field width can clip the closing `>` and fail Norminette (e.g. [kube/vscode-42header#18](https://github.com/kube/vscode-42header/issues/18)). Treat as a **hypothesis to confirm with the user**, not as the cycle lock until they pick the product/path.
