# Online prompt tips — Cycle 20 Continuity X / WorkSpace TNA

Actionable prompting practices for this cycle type (agent brief + plan-before-mutate + anti-loop). Captured 2026-09-15.

1. **Structure the brief as Goal → Constraints → Context pointers → Acceptance criteria → Out of scope**  
   Put “what must be true when we stop” and “what must not happen” in the same artifact. Constraints beat improvisation on irreversible FS/git work.  
   Source: [Cursor Prompts: Context, Constraints, and Acceptance Criteria](https://eastondev.com/blog/en/posts/dev/20260129-cursor-prompt-engineering/)

2. **Plan first; wait for approval before mutation**  
   Research → clarifying questions → detailed plan with paths → hold for user approval. Continuity choice ≠ plan-gate execute.  
   Source: [Best practices for coding with agents (Cursor)](https://cursor.com/blog/agent-best-practices)

3. **One scoped advance per cycle; name a verifiable stop condition**  
   Prefer a single concrete deliverable (e.g. written parent-surgery policy) over “continue strategy” with no new artifact. Acceptance criteria must be checkable, not vibes.  
   Sources: [DEV — structure Agent Mode prompts](https://dev.to/unfairhq/how-to-structure-cursor-agent-mode-prompts-for-full-stack-app-generation-a-practical-guide-2ap1); [OTF — plan, scope, verify](https://otf-kit.dev/blog/cursor-agent-best-practices)

4. **Encode hard non-goals in Constraints (not only Goal)**  
   Explicitly forbid re-proposing finished work (Appendix A parents, archived OS-IA, Medium peers), silent whole-tree archive, and Complete while WorkSpace remains.  
   Source: [Easton — Constraints section](https://eastondev.com/blog/en/posts/dev/20260129-cursor-prompt-engineering/)

5. **Anti-loop: stop on no material delta; escalate instead of re-attest**  
   If research would only restate prior findings, terminate with a named reason (`escalate_break_loop`) rather than burning another docs-only pass. Prefer a new gated step or structured stop over repetition.  
   Sources: [Stop AI agents looping on the same failed tool call](https://particula.tech/blog/stop-ai-agents-looping-same-tool-call-no-progress); [Stop agent loops with a no-progress guard](https://viralruparel.com/blog/agent-loop-no-progress-detection-guard)

6. **Reference durable artifacts by path; don’t paste whole strategy docs**  
   Point at `program/git-strategy-workspace-hazards.md`, ROADMAP, prior session — keeps the prompt short and avoids stale copies.  
   Source: [Cursor agent best practices](https://cursor.com/blog/agent-best-practices)

7. **Informed consent on every gate ask**  
   Plain language + what each choice commits to + pros/cons. Bare Continuity “yes” only locks disclosed defaults; it does not approve moves.  
   Source: project FAW law + [Cursor Plan Mode clarifying questions](https://cursor.com/blog/agent-best-practices)
