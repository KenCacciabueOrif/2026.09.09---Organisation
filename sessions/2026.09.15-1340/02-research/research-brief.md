# Research brief — Cycle 22

**Session:** `sessions/2026.09.15-1340/`  
**Continuity:** Q1=A (research picks), Q2=A (1–2 of 20–22 if dashboard), Q3=A (WorkSpace material or escalate; no nest FS), anti-loop binds.  
**Status:** research complete — **single** concrete advance recommended (no fence-sit).

---

## Verdict (do not fence-sit)

| Field | Value |
| --- | --- |
| **recommended_workstream** | **dashboard** |
| **concrete_advance_candidate** | Implement refinement **item 20** (split inline data → sibling data file + async load; update generator) **and** **item 22** (build repo→index Map once; replace `D.repos.indexOf(r)` in `renderProjects`). **Do not** re-implement item **21** (150 ms debounce already present). |
| **dashboard_items_if_any** | **20 + 22** |
| **anti_loop_verdict** | WorkSpace hazards / #4 DRAFT / nest inventory = **no material delta** vs Cycle 20 → WorkSpace-only docs re-attest would be theater → escalate **if** that path were chosen. Dashboard **20** is **new** unstarted work → overall cycle **not** escalate. |
| **one-line for planner** | Plan org-repo catalogue **code+data**: emit `work_timeline_data.json` (or documented file://-safe data module), fetch/load at boot with DQ/error UX + regenerate pipeline; add O(1) repo index Map; skip debounce; STAGE 1 plan gate; zero WorkSpace FS. |

---

## Recommended approach options (max 3)

### Option A — Dashboard items 20 + 22 (RECOMMENDED)

**Mutation class hint:** org-repo catalogue **code + data** (not corpus `fs_mutation`; still **plan gate** per Continuity Q6).

**Scope:**
1. **20:** Generator writes sibling data file; HTML drops mega-inline blob; load via `fetch` (HTTP) with clear fatal/DQ on failure; report data age from payload `generated` (and optionally fetch timestamp).
2. **22:** Once after parse: `const repoIndex = new Map(D.repos.map((r,i)=>[r,i]))` (or path-keyed if objects are recreated); use in `renderProjects` instead of `indexOf`.

**Tradeoffs:**
- **Pros:** Highest remaining concrete value in 20–22; clears the only large perf structural item; 22 is free; reversible; no ROADMAP/WorkSpace risk; aligns Q2=A (1–2 items).
- **Cons:** `file://` + `fetch(.json)` often fails (see online-findings) — plan must require localhost serve **or** choose a script-src data module; slightly larger verification surface than 22 alone.

**Verification (suggested AC):** regenerate; assert HTML size drop + data file exists; Node smoke (mock fetch or load JSON); optional browser over `http://localhost`. Prior browser-harness may still be down.

### Option B — WorkSpace Continuity X / #4 material docs only

**Would be:** #4 **approval** Continuity (user sign-off framing) without nest FS — **or** escalate.

**Tradeoffs:**
- **Pros:** Advances programme Primary-next lock toward nest extract readiness.
- **Cons:** #4 DRAFT already written Cycle 20; re-write = **no material delta**; approval-only without nest is thin vs dashboard 20; nest extract **forbidden** this Continuity. Under Q3=A + anti-loop → prefer **`escalate_break_loop`** over another honesty pass.

**Not recommended** while dashboard 20 remains undone.

### Option C — `escalate_break_loop`

**When valid:** Forced WorkSpace-only with no new gated step.  
**This cycle:** **Not** the highest-value pick — Option A has concrete unstarted work. If user later forces WorkSpace without approving #4 nest map → escalate then.

---

## Required facts

1. Items **20–22** text confirmed in `catalogue/work_timeline_refinements_2026-09-15.md` §F.
2. **21 done** in live HTML (`setTimeout(…,150)` on `#c-q`).
3. **22 open** — `indexOf` still in `renderProjects`.
4. **20 open** — ~788 KB inline JSON script; generator only patches HTML; no `work_timeline_data.json`.
5. WorkSpace live: TNA + 3 nests; OS-IA archived; no `.gitmodules`; #4 still DRAFT / approval pending — **matches** Cycle 20.
6. Publish Continuity Q5=A → mid + final git-manager (GfW) after implement; research did not re-run full push preflight (goal is not pull/sync-only; implementer/git-manager own GfW publish).

## Unknowns / plan risks

- Exact data-module shape: pure `.json`+HTTP vs `.js` `window.__DATA__=` for `file://` — **plan gate should pick** (recommend document HTTP as primary AC; optional JS module if user insists on double-click `file://`).
- Browser harness CDP may still fail — Node smoke is acceptable (Run 3 precedent).
- After data-split, backup `work_timeline.html.bak-*` may remain — out of scope unless plan says delete.

## Risks and blockers

| Risk | Class | Note |
| --- | --- | --- |
| `file://` fetch blocked | product UX | Mitigate in plan AC |
| Push/GCM fail | `agent_environment` / credentials | Fail-closed session `blocked` (Q5=A) — not researched as cycle blocker |
| Unrelated dirty WT | `dirty_working_tree` | git-manager allowlist only |
| Nest extract temptation | process | **Forbidden** — #4 not approved |
| Claiming Multi-experiment Complete | process | **Forbidden** |

**blockers:** none for choosing Option A research→plan. Plan-gate yes still required before implement.

## Canonical references

- `catalogue/work_timeline_refinements_2026-09-15.md`
- `catalogue/work_timeline.html`, `catalogue/generate_work_timeline.py`
- `program/ROADMAP.md`, `program/git-strategy-workspace-hazards.md`, `program/git-strategy-tna-parent-surgery.md`
- `sessions/2026.09.15-1320/SESSION.md`
- Online: MDN Caching, MDN Map, file:// fetch CORS notes (see `online-findings.md`)

---

## Structured return (orchestrator)

```
status: ready_for_planner
recommended_workstream: dashboard
concrete_advance_candidate: Item 20 data-split-to-JSON (generator+HTML load/DQ) + item 22 repo index Map; skip item 21 (already debounced)
dashboard_items_if_any: 20+22
anti_loop_verdict: WorkSpace no material delta (escalate if WorkSpace-forced); dashboard 20 is material → do not escalate this cycle
one-line for planner: Catalogue code+data plan for items 20+22 only; STAGE 1 hold; zero WorkSpace FS; address file:// fetch in AC.
```
