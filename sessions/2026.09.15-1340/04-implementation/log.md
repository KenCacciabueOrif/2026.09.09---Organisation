# Implementation log

Session: `2026.09.15-1340` · Phase: `04-implementation` · Cycle 22 STAGE 2 items **20 + 22** (skip **21**)  
Gate: **APPROVED — yes + L-both** + standing amendment (rotate off dashboard next FAW)  
Mutation class: `catalogue_product` (org-repo catalogue only)

## Timeline

- **14:04** — Read plan + SESSION; gate yes + L-both recorded; STAGE 2 unlocked for implementer.
- **14:05** — Inspected `generate_work_timeline.py` (inline HTML patch only) and `work_timeline.html` (~830 KB; `id="data"` blob ~790 KB; `D.repos.indexOf` in `renderProjects`; `#c-q` 150 ms debounce already present).
- **14:06** — Rewrote generator for **L-both**: emits `work_timeline_data.json` (canonical) + `work_timeline_data.js` (`window.__WORK_TIMELINE_DATA__ = …` classic script). No longer patches mega-inline JSON into HTML.
- **14:06** — Transformed HTML: removed inline data script; async boot prefers module on `file://`, `fetch('./work_timeline_data.json')` on http(s), module-fallback if fetch fails, `showDataFatal` otherwise; DQ appends load source / ms / load time; item **22** `repoIndex` Map + `repoIndex.get(r)`; exposed `showDetail` / `closeDetail` / filter clears on `window` for inline handlers. HTML **42 884** bytes (was **829 966**).
- **14:06** — Regenerated: `python generate_work_timeline.py` → exit 0; `generated=2026-09-15 14:06` repos=28 commits=3491 top_level=12; JSON ~788 350 B; JS ~788 385 B.
- **14:07** — Node smoke (14 checks) **PASS** — no inline data; loader/fatal/Map/debounce; JSON shape; JS vm-eval global; HTML size drop.
- **14:07** — Updated `work_timeline_refinements_2026-09-15.md` status + §F items 20–22 honesty; noted dashboard workstream done for now / next FAW rotate.
- **14:07** — Deleted one-shot helper `_cycle22_transform_html.py` (not a product artefact).
- **14:07** — Zero WorkSpace / nest / `#4` attestation (Test-Path presence only; no corpus moves). ROADMAP not edited; Multi-experiment not marked Complete; `#4` not claimed approved.

## Verification

| Check | Result |
| --- | --- |
| Regenerate | PASS — `python generate_work_timeline.py` |
| Sibling data exists | PASS — Test-Path `work_timeline_data.json` + `.js` |
| HTML size drop | PASS — 829 966 → 42 884 bytes |
| No `id="data"` mega blob | PASS (grep / smoke) |
| No `D.repos.indexOf` | PASS |
| Debounce 150 ms untouched | PASS |
| Node smoke | PASS (14/14) |
| Browser localhost | skipped (optional; harness not required) |

## Zero-move / out-of-map attestation

- **Wrote:** org-repo `catalogue/*` product files + this session `04-implementation/*` only.
- **Did not:** move/rename/delete under WorkSpace / nests / TNA; no remote-config; no `#4` approve; no ROADMAP Complete / Primary-next jump.
- **Probe method:** `Test-Path` / `Get-Item` on catalogue siblings; WorkSpace path presence check only.

## Standing amendment (for self-improver / Next FAW)

User gate amendment: after this cycle the **dashboard workstream is done for now**. Next FAW must **not** default to the dashboard; research must justify the workstream against `program/ROADMAP.md` (WorkSpace Continuity X / `#4` approval gate per Q3=A, or other highest-value row). Do not inherit prior cycle topic.

## Deviations from plan

- none material — L-both adapted from plan’s L-http-primary wording exactly as gate directed (classic script assign for `file://`, JSON canonical for HTTP/tooling).
- One-shot HTML transform helper used then **deleted** (not left in catalogue).
- Browser over localhost optional AC skipped (Node smoke required AC satisfied).
