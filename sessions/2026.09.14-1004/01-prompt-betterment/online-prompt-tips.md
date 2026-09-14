# Online prompt tips (ad-hoc lint / product-settings fix)

Actionable tips for framing this flake8 / 42-header length fix. Sources checked 2026-09-14.

1. **Name goal + constraint in one breath** — e.g. “header is correct content-wise but must pass flake8 line-length.” Vague “fix lint” invites ignore-rules instead of a real width fix.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)

2. **Point at exact files and a verify command** — fixture path + `flake8 <file>` (or project config) as the done check beats “make it shorter.”  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

3. **Use a short task frame: task → context → constraints → done state** — keep ROADMAP/corpus out of scope so the agent does not reopen organisation cycles.  
   Source: [Prompt Templates for AI Coding Agents](https://www.learncursor.dev/guides/prompt-templates-for-ai-coding-agents)

4. **Prefer plan-before-edit when the fix may touch extension settings + a sample file** — one wrong locus (global E501 ignore vs regenerating the header) is expensive to unwind.  
   Source: [OTF — Cursor agent best practices](https://otf-kit.dev/blog/cursor-agent-best-practices)

5. **Encode the numeric limit as AC** — flake8/pycodestyle default `max-line-length` is **79**; classic 42 headers are often **80** → E501. State “every header line ≤ 79” (or project override if found).  
   Sources: [flake8 user options](https://flake8.pycqa.org/en/latest/user/options.html), [PEP 8 — Maximum Line Length](https://peps.python.org/pep-0008/)

6. **Prefer fixing the generator over silencing the linter** unless the user asks for ignore/`# noqa` — keeps student code honest under default flake8.  
   Source: [flake8 — Selecting and Ignoring Violations](https://flake8.pycqa.org/en/latest/user/violations.html)

7. **Keep one task per chat / session** — this cycle is only “−1 column for flake8”; do not re-open long-email truncate work already done.  
   Source: [How to Write Good Prompts in Cursor](https://www.learncursor.dev/learn/cursor-agents/writing-good-prompts)
