# Codebase findings — Cycle 22

**Session:** `sessions/2026.09.15-1340/`  
**Probe method:** Read / Grep on org-repo catalogue + program docs; Shell `Test-Path` for WorkSpace nests; file-size measure on `work_timeline.html`.

---

## Continuity / ROADMAP lock (context)

| Source | Finding |
| --- | --- |
| `program/ROADMAP.md` | Primary next = Multi-experiment **Remaining: `WorkSpace` only** (TNA); not Complete; do not jump Special git / reopen peers |
| `program/git-strategy-workspace-hazards.md` | Continuity X; #4 **DRAFT written (Cycle 20) / approval pending**; whole-tree clearance still **NO**; nested under WorkSpace **4** |
| `program/git-strategy-tna-parent-surgery.md` | Full parent-surgery **policy DRAFT** exists (Cycle 20); nest extract **forbidden** until #4 approved + dedicated map gate |
| `sessions/2026.09.15-1320/SESSION.md` | Dashboard Run 3 **complete**; close notes said remaining perf 20–21 — **partially stale** (see below) |

---

## WorkSpace live probe (anti-loop baseline)

| Path | Present? |
| --- | --- |
| `C:\Project\WorkSpace` | Yes (children: `TestNewWorkspaceAgent` only) |
| `C:\Project\WorkSpace\TestNewWorkspaceAgent` (TNA) | Yes |
| `…\hermes-agent` | Yes |
| `…\Projects\Project Atelier IA\Projet Adrien\orchestrateur` | Yes |
| `…\Projects\Project Atelier IA\Workshop\WorkshopOrif` | Yes |
| `C:\Project\archive\2026.09.15 - OS-IA` | Yes (verify-only) |
| TNA `.gitmodules` | **No** (ignored nested clones model unchanged) |

**Material delta vs Cycle 20 attestation:** **None** for hazards / nest inventory / #4 status. Re-writing `git-strategy-tna-parent-surgery.md` or honesty re-attest = **no material delta** → WorkSpace-only path this Continuity should **`escalate_break_loop`**, not another docs_only pass. Nest FS **out of scope** (#4 not approved; Q3=A).

---

## Dashboard — refinement items 20–22 (verified)

Source of truth: `catalogue/work_timeline_refinements_2026-09-15.md` §F:

| # | Plan text | Live evidence | Status |
| --- | --- | --- | --- |
| **20** | Split ~594 KB inline JSON to `work_timeline_data.json` fetched at load; DQ fetch age | HTML **~828 KB**; data `<script id="data">` span **~788 KB**; `JSON.parse(document.getElementById('data').textContent)`; **no** `catalogue/work_timeline_data.json`; generator still in-place swaps blob into HTML (`generate_work_timeline.py` `MARK_OPEN`/`MARK_CLOSE`) | **Unstarted — highest concrete gain** |
| **21** | Debounce `renderCommits` on search (~150 ms) | Already present: `let cT;fEl('c-q').oninput=()=>{clearTimeout(cT);cT=setTimeout(()=>renderCommits(true),150);};` (~L541) | **Done** — Run 3 close note “21 unstarted” is **wrong** |
| **22** | Map `D.repos.indexOf(r)` once | Still `const i=D.repos.indexOf(r);` in `renderProjects` (~L496); **no** `Map` / repo-index helper in file (Run 1 status line claiming “O(1) repo index” is **aspirational / not present**) | **Unstarted — trivial free win** |

### Paths that matter

- `catalogue/work_timeline_refinements_2026-09-15.md` — backlog + priority row “Performance: debounce, index map, data split (20–22)”
- `catalogue/work_timeline.html` — load path, `renderProjects` / `renderCommits`, inline data script
- `catalogue/generate_work_timeline.py` — currently only writes into HTML; must gain JSON (or data-module) emit + keep regenerate UX

### Prior Run 3 leftovers (done — do not re-do)

- Hash dedupe in generator; path-keyed DQ; global `/` search — session `2026.09.15-1320`.

---

## Comparison verdict (codebase)

| Option | Material new work? | Value |
| --- | --- | --- |
| Dashboard **20 (+22)** | Yes | Structural HTML shrink / cacheability + tiny index fix |
| Dashboard **21** alone | No | Already shipped |
| WorkSpace #4 rewrite / re-attest | No | Anti-loop → escalate |
| WorkSpace #4 approval Continuity (docs/gate only) | Thin | Unlocks future nest gate but zero FS; Continuity Q3=A prefers material **or** escalate — approval-only is weaker than dashboard 20 |
| `escalate_break_loop` | Process honesty | Correct **if** WorkSpace forced; **wrong** while dashboard 20 remains undone |

**Recommended concrete advance (codebase):** implement **item 20** (data-split) **and** **item 22** (repo index map). Skip 21.
