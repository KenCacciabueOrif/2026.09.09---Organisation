# Online prompt tips

Actionable prompting practices for **large-corpus organisation** and **multi-phase agent programs** (Cycle 0 charter style).

1. **Bound each cycle with a testable done-condition** — Prefer `verb + targets + constraints + done-when` over vague “organise everything.” Split when verification would require more than a few clear checks. — https://baeseokjae.github.io/posts/cursor-agent-best-practices-2026/

2. **Plan / inventory before mutate** — For multi-file or corpus-scale work, inspect and write an approved plan (or inventory + taxonomy) before any relocation or deletion. Checkpoints and approval gates beat one mega-run. — https://otf-kit.dev/blog/cursor-agent-best-practices · https://cursor.com/blog/agent-best-practices

3. **Inventory the corpus before taxonomy or moves** — Count what exists (top-level entries, formats, size bands, date hints) before designing categories or touching files; inventory changes the design. — https://multigrid.ai/learn/build-document-corpus

4. **Separate planner vs worker vs judge** — Planners decide boundaries and avoid duplicate decisions across subtrees; workers execute one slice; a judge checks against done-conditions. Fresh cycle starts reduce drift on long programs. — https://github.com/nibzard/awesome-agentic-patterns/blob/main/patterns/planner-worker-separation-for-long-running-agents.md · https://cursor.com/blog/agent-swarm-model-economics

5. **Treat multi-agent prompts as contracts** — Explicit role identity, inputs/outputs, CAN / CANNOT, and stop/escalate rules; typed artefacts at phase boundaries (charter → inventory → taxonomy → roadmap). — https://helain-zimmermann.com/blog/prompt-engineering-for-multi-agent-workflows · https://www.agentpatternscatalog.org/patterns/sop-encoded-multi-agent/

6. **Propose taxonomy with human-in-the-loop before mass assignment** — Seed or draft categories on a sample, then keeper review before bulk classify or folder moves. — https://www.klens.ai/pdf/klens_whitepaper_taxonomy_v1.pdf · https://jaredfoy.com/resolve/doc/633-corpus-taxonomy-and-manifest-design

7. **Version prompts and acceptance criteria together** — A cycle is not “done” until pass/fail criteria for that cycle’s artefacts are explicit; later cycles inherit the charter, not a free-form goal. — https://mlflow.org/articles/why-standardize-ai-workflows/ · https://business.adobe.com/blog/prompting-ai-agents

# Clarifying questions

See `notes.md` § Clarifying questions (relay to user). Answers: none yet.

# Answers

- (none — awaiting user)
