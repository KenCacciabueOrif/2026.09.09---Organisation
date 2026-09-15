# Plan — Cycle 22 Dashboard items 20 + 22

**Session:** `sessions/2026.09.15-1340/`  
**Phase:** `03-plan/` (STAGE 1 — **STOP for mandatory plan gate**; Continuity Choose ≠ execute)  
**Locks:** Continuity Choose all **A**; Q6=A plan gate before implement; Q5=A git-manager GfW publish after gate+implement; Q2=A → **1–2** of items 20–22  
**Research:** `02-research/research-brief.md` — dashboard **20 + 22** only; skip **21**; WorkSpace / #4 / nest FS **out of map**; anti-loop = material dashboard advance (not escalate)

---

## Goal

Implement the two remaining high-value Organisation Dashboard performance refinements in the **org-repo catalogue only**:

1. **Item 20 — data split:** Stop embedding ~788 KB of JSON inside `catalogue/work_timeline.html`. Have `catalogue/generate_work_timeline.py` emit a sibling data artifact; change the HTML boot path to load that data asynchronously (HTTP `fetch` of JSON as primary), surface load failures in the existing fatal/DQ UX, and report data age from the payload `generated` field (and optionally fetch time).
2. **Item 22 — repo index Map:** After data parse, build `const repoIndex = new Map(D.repos.map((r, i) => [r, i]))` (or an equivalent stable key if object identity is unsafe) and use it in `renderProjects` instead of `D.repos.indexOf(r)`.

**Skip item 21** — 150 ms debounce on `#c-q` is already live. **No** WorkSpace corpus FS, nest extract, #4 approval theater, or ROADMAP Complete / Primary-next jump.

After plan-gate **yes** (+ amendments): implementer → mid git-manager (GfW) → auditor → self-improver → **final** closing-pass git-manager.

---

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`catalogue_product`** (org-repo **code + data**) — **not** corpus `fs_mutation`; **not** `docs_only` honesty-only; **not** `product_settings`; **not** `escalate_break_loop` |
| Mutation kind | N/A (no corpus path batch; no remote-config) |
| Corpus FS | **Zero** intentional moves/renames/deletes under `C:\Project` catalogue-backed batches / WorkSpace |
| Org-repo disk writes (in scope) | `catalogue/work_timeline.html`, `catalogue/generate_work_timeline.py`, new sibling data file(s) under `catalogue/`, status touch on `catalogue/work_timeline_refinements_2026-09-15.md`, session logs |
| User approval before implementer | **Required** (Continuity Q6) — even though this is **not** corpus `fs_mutation` |
| First-move / taxonomy gates | N/A for this batch (no Early/simple corpus move). Taxonomy remains **proposed-ratified — ready for user sign-off**; must-preserve **draft — not auto-locked** |
| Attest (implementer) | Zero WorkSpace / nest / `#4` path mutation; log probe method if any presence check; do not stage secrets |

**Honesty:** Material advance = unstarted item **20** (+ free **22**). WorkSpace hazards / #4 DRAFT have **no material delta** vs Cycle 20 — deliberately **not** chosen (would be escalate theater). Continuity Choose **≠** this gate.

---

## Context (binding)

| Item | Status |
| --- | --- |
| Refinement source | `catalogue/work_timeline_refinements_2026-09-15.md` §F items 20–22 |
| Item 20 | **Open** — inline `<script id="data">` ~788 KB; no `work_timeline_data.json`; generator in-place HTML patch only |
| Item 21 | **Done** — `setTimeout(…, 150)` on `#c-q` — **do not re-implement** |
| Item 22 | **Open** — `D.repos.indexOf(r)` still in `renderProjects` (~L496) |
| Prior Run 3 | Dedup / path-keyed DQ / global `/` search — **leave alone** |
| WorkSpace / #4 | Live TNA + nests; `#4` DRAFT approval pending — **out of map this cycle** |
| ROADMAP | Multi-experiment **Remaining: WorkSpace only** — unchanged by this cycle; **never** mark Complete |
| `file://` risk | Browsers often block `fetch(.json)` from `file://` — plan **must** pick load strategy at gate (below) |

---

## What the user is approving

Plain-language intent for the orchestrator plan gate. Continuity / Choose / bare **yes** to Continuity **≠** this gate.

### What “yes” means

You approve STAGE 2 in **this same session** to change only the Organisation Dashboard artefacts under `catalogue/`:

- Generator writes a **sibling data file** next to the HTML (default name `work_timeline_data.json`, unless you amend the load strategy).
- HTML **stops** shipping the mega-inline JSON blob; it **loads** data at boot and keeps/extends fatal + DQ error UX on failure.
- `renderProjects` uses an **O(1) Map** instead of `indexOf`.
- Refinement doc marks **20** and **22** done (21 already done).
- Then git-manager **commits and pushes** allowlisted org-repo changes via **Git for Windows + GCM** (mid after implement; final after self-improver when late dirt remains).

**What does not happen on “yes”:** no moves under `C:\Project\WorkSpace`; no nest extract; no `#4` approve; no Multi-experiment Complete; no debounce rework (21); no taxonomy/must-preserve “final” claims.

### Load strategy (pick one at the gate)

| Option | Behaviour | Pros | Cons / tradeoffs |
| --- | --- | --- | --- |
| **L-http (default recommendation)** | Emit `catalogue/work_timeline_data.json`. HTML `fetch('./work_timeline_data.json')` (or same-dir relative). Primary verify over **HTTP** (`python -m http.server` or equivalent from `catalogue/`). On `file://` fetch failure → **visible fatal** panel with short “serve over localhost” tip (not silent blank page). DQ reports payload `generated` (+ optional fetch timestamp). | Matches refinement item 20 wording; HTML stays small/cacheable; simple regenerate pipeline | Double-click `file://` will **not** show data until user serves locally (or opens via a local server) |
| **L-module** | Emit `catalogue/work_timeline_data.js` that assigns a global (e.g. `window.__WORK_TIMELINE_DATA__ = …`). HTML loads via `<script src="…">` then reads the global (no `fetch`). | Often works with double-click `file://`; avoids CORS/`file://` fetch trap | Slightly less “pure JSON”; cache model differs; still need clear error if script 404 |
| **L-both** | Emit **JSON** (canonical regenerate artefact) **and** a thin JS data module; HTML prefers module when present / `file://`, else `fetch` JSON on HTTP | Best of both local UX + HTTP/tooling | More generator + dual-file maintenance; slightly larger surface |

**Default if user answers bare “yes” / accepts defaults:** **L-http**.

### Pros / cons of approving the cycle (20+22)

| Pros | Cons |
| --- | --- |
| Clears the only large remaining perf structural item; HTML shrinks dramatically | `file://` UX depends on load strategy (see above) |
| Item 22 is tiny and free with the same edit pass | Verification needs regenerate + Node smoke (browser harness may still be down) |
| Reversible (git revert / regenerate); no ROADMAP / WorkSpace risk | Publish can still `blocked` on GfW/GCM (fail-closed — honest, not false complete) |

### What “no / edit / hold” means

- **No / hold:** no implementer; session stays `in_progress` or closes without product change; WorkSpace remains Primary-next lock.
- **Edit:** amend load strategy (L-http / L-module / L-both), data filename, or AC wording; re-gate if material; then STAGE 2.

---

## Exact user-gate question

Copy-paste for orchestrator relay:

> **Plan gate — Cycle 22 (dashboard 20 + 22)**  
>  
> **Plain language:** May we implement Organisation Dashboard performance items **20** (split inline data out of `work_timeline.html` into a sibling data file + load at boot with clear error/DQ UX) and **22** (build a one-time repo→index Map; stop using `indexOf` in the projects table)? Item **21** (search debounce) is already done and will **not** be touched. This only changes files under `catalogue/` in the organisation git repo. It does **not** move WorkSpace, extract nests, or approve `#4`. After you say yes, agents will implement, then commit/push with Git for Windows (allowlisted paths).  
>  
> **Load strategy (reply with one):**  
> - **L-http** (recommended default) — `work_timeline_data.json` + `fetch`; verify via local HTTP; `file://` shows a clear fatal tip to serve locally  
> - **L-module** — JS data module + `<script src>` (friendlier double-click `file://`)  
> - **L-both** — JSON + JS module  
>  
> **Pros of yes:** smaller HTML, better cache story, free O(1) index fix, no WorkSpace risk.  
> **Cons of yes:** `file://` may not load data under L-http until you use a local server; slightly more files to regenerate; push can still fail closed.  
>  
> Reply **yes** (implies **L-http** unless you name another), **yes + L-module|L-both**, **amend …**, or **no/hold**.

---

## Acceptance criteria

### Product (after gate yes)

- [ ] Generator (`catalogue/generate_work_timeline.py`) emits the sibling data artefact(s) required by the **gated** load strategy (`work_timeline_data.json` and/or `work_timeline_data.js`); regenerate no longer depends on mega-inline JSON inside HTML as the sole payload.
- [ ] `catalogue/work_timeline.html` no longer contains the large inline `<script id="data" type="application/json">…</script>` blob (or equivalent mega-inline); HTML size drops materially vs pre-change (~828 KB baseline).
- [ ] Boot load path matches gated strategy:
  - **L-http / L-both:** `fetch` JSON succeeds when served over HTTP from `catalogue/`; failure → visible fatal (and/or DQ) — not a blank silent page.
  - **L-module / L-both:** script-src data module populates data without requiring `fetch` on `file://` (documented).
- [ ] DQ / status reports data age from payload `generated` (and optionally notes fetch/load time).
- [ ] Item **22:** after successful parse, a `Map` (or equivalent O(1) lookup) replaces `D.repos.indexOf(r)` in `renderProjects`; no remaining `indexOf` on `D.repos` in that hot path.
- [ ] Item **21:** debounce left as-is (still ~150 ms); not “fixed” again.
- [ ] `catalogue/work_timeline_refinements_2026-09-15.md` status notes mark **20** and **22** done; **21** already done; remaining-perf line updated honestly.
- [ ] Verification logged in `04-implementation/`:
  - Regenerate run succeeds.
  - Sibling data file(s) exist (`Test-Path` **or** Read/Glob — log probe method).
  - HTML size drop noted (cheap measure OK).
  - **Node smoke** (mock `fetch` / load JSON or evaluate Map + parse path) — required.
  - Browser over `http://localhost` — **optional** if harness/CDP down (Run 3 precedent).
- [ ] Zero WorkSpace / nest / `#4` / corpus path mutations; ROADMAP Multi-experiment **not** marked Complete; no Primary next / Special git jump.

### Process

- [ ] STAGE 1 hold until plan-gate **yes** (+ load strategy).
- [ ] After yes: implementer → mid git-manager (GfW/GCM, org root, allowlist) → auditor → self-improver → **final** closing-pass git when allowlisted late dirt remains.
- [ ] Session never `complete` if final git skipped while late allowlisted dirt remains, or if publish blocked (honest `blocked`).
- [ ] Implementer attests mutation class honesty: org-repo catalogue only.

---

## Steps

**STAGE 1 — stop here until gate yes.**

0. **Orchestrator plan gate** — Relay Exact user-gate question; record answer + load strategy in `01-prompt-betterment/notes.md` (or SESSION notes) and flip STAGE → 2.  
   - **Verify:** gate answer recorded; `ready_to_implement` effectively unlocked only on yes.  
   - **Paths:** `sessions/2026.09.15-1340/SESSION.md`, notes.

**STAGE 2 — only after yes (+ amendments).**

1. **Implement item 20 — generator** — Paths: `catalogue/generate_work_timeline.py`.  
   - Action: After `build()`, write sibling data file(s) per gated strategy; stop (or thin-stub) in-place mega-blob HTML patch; keep `generated` and counts in stdout; update module docstring. Prefer relative paths under `catalogue/` (avoid hardcoding only absolute HTML if easy — do not expand scope beyond regenerate UX).  
   - Verify: regenerate creates `catalogue/work_timeline_data.json` and/or `.js`; exit 0.

2. **Implement item 20 — HTML load / DQ** — Paths: `catalogue/work_timeline.html`.  
   - Action: Remove mega-inline data script; add async boot per **L-http / L-module / L-both**; preserve existing fatal-panel philosophy on failure; extend DQ strip for data age / load failure messaging; keep rest of Run 1–3 behaviour.  
   - Verify: no `id="data"` mega blob; load path present; fatal path exists for missing/bad data.

3. **Implement item 22 — repo index Map** — Paths: `catalogue/work_timeline.html` (`renderProjects`).  
   - Action: Build Map once after `D` is available; replace `indexOf`; ensure `data-i` / `showDetail` still resolve correct repo.  
   - Verify: Grep shows no `D.repos.indexOf` in projects render; Node smoke exercises index path.

4. **Honesty docs** — Paths: `catalogue/work_timeline_refinements_2026-09-15.md` (status / §F / remaining line); `04-implementation/changes.md` + `log.md`.  
   - Action: Mark 20+22 done; note 21 pre-done; document load strategy + verify method; attest zero WorkSpace FS.  
   - Verify: doc text matches live behaviour.

5. **Verification pack** — Action: regenerate; measure HTML size; Node smoke (required); optional localhost browser. Log results.  
   - Verify: AC checkboxes above can be audited as pass/fail.

6. **Mid git-manager** — Paths: allowlisted `catalogue/**`, session `04-implementation/**` as applicable.  
   - Action: GfW + GCM stage/commit/push org-repo only; fail-closed on blocker.  
   - Verify: `05-git/log.md` mid section; status not false-complete on push fail.

7. **Auditor** — Readonly vs this plan AC; orchestrator persists `06-audit/report.md`.

8. **Self-improver** — Mandatory end-of-cycle process audit + applied improvements under `07-self-improvement/`.

9. **Final closing-pass git-manager** — Allowlisted late dirt (`06-audit/**`, `07-self-improvement/**`, `SESSION.md` close, cycle `.cursor/**` if any); same GfW/GCM rules.  
   - Verify: no skip while dirt remains; honest `blocked` if push fails.

10. **Close SESSION** — Update framing: mutation class `catalogue_product`; ROADMAP lock hint remains WorkSpace-only for **next** FAW; status `complete` or `blocked` honestly.

---

## Non-goals / out of scope

- WorkSpace nest moves / TNA parent-surgery / `#4` **approve** theater or nest extract.
- Item **21** debounce rework.
- Visual/UX items outside 20+22 (KPI polish, heatmap, etc.).
- Deleting historical `work_timeline.html.bak-*` unless separately requested.
- Claiming Multi-experiment **Complete** or jumping Primary next / Special git.
- Corpus `fs_mutation`, remote-config, whole-tree archive.
- Taxonomy / must-preserve **final** ratification.
- Re-opening Early / Medium / archived Multi-experiment peers as move sources.

---

## Risks / rollback

| Risk | Mitigation |
| --- | --- |
| `file://` + `fetch(JSON)` fails | Gate picks L-http / L-module / L-both; L-http fatal tip mandatory; do not ship silent blank page |
| Browser harness / CDP down | Node smoke required; browser optional |
| Generator still patches old markers | Step 1 removes dependency on mega-inline as sole payload; implementer verifies markers gone or stubbed |
| Push / GCM fail | Q5=A fail-closed → session `blocked`, not false `complete` |
| Unrelated dirty WT | git-manager allowlist only; abort unrelated → `blocked` |
| Accidental WorkSpace touch | Explicit non-goals; auditor checks; implementer attest |
| Rollback | `git revert` of catalogue commit(s) and/or regenerate from last good commit; keep data sibling deletion in revert |

---

## Ready to implement

**no** — STAGE 1 hold until plan-gate **yes** (+ load strategy **L-http** / **L-module** / **L-both**).

After gate yes: orchestrator sets effectively ready and resumes STAGE 2 same session (implement → mid git → audit → self-improver → final git).

---

## Blocking questions

1. **Plan gate** — Exact user-gate question above (yes / load strategy / amend / no-hold).  
   Until answered: **do not** launch implementer.

---

## Structured planner return

```
plan_path: sessions/2026.09.15-1340/03-plan/plan.md
ready_to_implement: no
blocking_questions: [plan-gate yes + load strategy L-http|L-module|L-both]
step_count: 11
mutation_class: catalogue_product (org-repo code+data; not corpus fs_mutation)
dashboard_items: 20+22 (skip 21)
exact_user_gate_question: |
  Plan gate — Cycle 22 (dashboard 20 + 22)

  Plain language: May we implement Organisation Dashboard performance items 20 (split inline data out of work_timeline.html into a sibling data file + load at boot with clear error/DQ UX) and 22 (build a one-time repo→index Map; stop using indexOf in the projects table)? Item 21 (search debounce) is already done and will not be touched. This only changes files under catalogue/ in the organisation git repo. It does not move WorkSpace, extract nests, or approve #4. After you say yes, agents will implement, then commit/push with Git for Windows (allowlisted paths).

  Load strategy (reply with one):
  - L-http (recommended default) — work_timeline_data.json + fetch; verify via local HTTP; file:// shows a clear fatal tip to serve locally
  - L-module — JS data module + <script src> (friendlier double-click file://)
  - L-both — JSON + JS module

  Pros of yes: smaller HTML, better cache story, free O(1) index fix, no WorkSpace risk.
  Cons of yes: file:// may not load data under L-http until you use a local server; slightly more files to regenerate; push can still fail closed.

  Reply yes (implies L-http unless you name another), yes + L-module|L-both, amend …, or no/hold.
```
