# Deferred backlog — Cycle 13

| ID | Proposal | Why deferred |
| --- | --- | --- |
| P6 | Cursor **hooks** to auto-save auditor/subagent structured outputs | Orchestrator always-persist is FAW equivalent; hooks = optional infra / larger change |
| P7 | Flip auditor to `readonly: false` so it can write only under `05-audit/` | Keeps verifier non-mutating by design; parent persist matches Cursor readonly guidance |
| — | Dedicated Continuity pack file under `references/` for WorkSpace-only post–strategy | Agents already encode packs; extract later if prompt-betterment bloats |
| — | Align `catalogue/inventory.md` WorkSpace size column with ~5786 MB Notes band | Product/docs optional; not FAW Continuity law |
| — | Tick SESSION phase checklist immediately when each phase returns | Orchestrator habit; reinforced by STAGE + persist law; no extra rule file |
