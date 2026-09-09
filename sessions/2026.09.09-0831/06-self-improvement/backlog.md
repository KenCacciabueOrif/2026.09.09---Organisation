# Deferred backlog

| ID | Proposal | Why deferred |
| --- | --- | --- |
| P8 | Document or auto-stage post-commit dirty session docs (`log.md`, `SESSION.md`) | Low severity; expected mid-session dirt; optional follow-up commit after user push auth |
| P9 | Corrective commit for BOM-free subject on `9708f2e` + fold dirty session/audit files | Product/git remediation for the user after credentials work; not workflow-machinery; amend unsafe without user ask |
| P10 | Dedicated QA-handoff / multi-round verify skill | Heavier than needed; Cursor verifier pattern already covered by auditor + honesty rules |
| P11 | Add `.gitignore` for agent temp commit-msg files | Out of scope this cycle; no temp files left in tree from this pass |
| P12 | Shell snippet / script helper for BOM-free commit on Windows | Prefer agent prompt guidance first; script can wait until repeated BOM incidents |
