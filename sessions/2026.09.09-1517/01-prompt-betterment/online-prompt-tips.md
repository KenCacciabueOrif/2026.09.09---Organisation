# Online prompt tips — Cycle 3 Early/simple remaining

Actionable prompting practices for scoped, approval-gated filesystem move cycles.

1. **Plan then approve before mutating** — For multi-path changes, research → write an explicit plan with paths → wait for human approval before execution. Prior “do next cycle” is not the same as approving a concrete move map.  
   Source: [Cursor — Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)

2. **Narrow allowed surface** — Name exactly which folders may change and list everything else as out of scope. Too much context (other ROADMAP rows, hygiene, git-strategy) increases wrong moves.  
   Source: [OTF — Cursor agent best practices](https://otf-kit.dev/blog/cursor-agent-best-practices)

3. **Verifiable acceptance criteria** — Prefer checkable pass/fail conditions (source gone, target present, INDEX updated, unexpected `.git` skipped) over vague “organised properly.” Separate mechanical checks from human judgment (plan-gate yes).  
   Source: [BrainGrid — Acceptance criteria AI agents can verify](https://www.braingrid.ai/blog/how-to-write-acceptance-criteria-ai-agent-can-verify)

4. **Given → When → Then style for moves** — Attach procedure: given sources exist and targets absent; when approved map executes; then paths and catalogue match the map (or fail-closed skip logged). Agents cannot claim done without the observable result.  
   Source: [PAELLADOC — Acceptance criteria agents can verify](https://paelladoc.com/blog/acceptance-criteria-for-ai-agents/)

5. **Fail closed on unknown / sensitive paths** — Default deny or stop when something unexpected appears (hidden `.git`, path outside allowlist). Do not invent git-strategy mid-batch for “no-git” Early/simple.  
   Source: [Agent File Guardian (policy allow/ask/deny, unanswered ask fails closed)](https://github.com/ShinYeol-Lee/agent-file-guardian)

6. **Human gate on irreversible FS effects** — Staging / explicit commit-style approval for filesystem mutations reduces YOLO damage; this program’s **plan gate** is the analogue (review from→to map, then execute).  
   Source: [YoloFS / arXiv: Don’t Let AI Agents YOLO Your Files](https://arxiv.org/html/2604.13536v2)

7. **Reuse locked conventions; only re-ask deltas** — Carry Cycle 2 layout/status/verify rules as disclosed defaults; ask only what might change (batch size, status overrides, gate continuity). Avoid re-litigating orchestrator locks.  
   Source: [Cursor agent best practices](https://cursor.com/blog/agent-best-practices) (specific prompts + constraints beat vague goals)
