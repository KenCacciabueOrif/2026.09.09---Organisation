# Research brief — Cycle 3 Early/simple remaining (fs_mutation)

**Session:** `sessions/2026.09.09-1517/02-research/`  
**mutation_class:** `fs_mutation`  
**Publish/push:** not required (corpus local moves only).  
**Answers:** Q1–Q6 locked (`notes.md`).

## Verdict

All three remaining Early/simple sources **exist** at corpus root, CreationTimes match catalogue hypotheses, **no** `.git` (top or nested), destinations **absent**, parents `archive` / `paused` **already exist**. Per Q5 90-day rule (cutoff `2026-06-11`), all three → **`archive`**. ZedTest remains at `C:\Project\paused\2026.06.30 - ZedTest` (INDEX accurate) — **do not re-move**. **No research blockers** to planning; moves still gated on **user plan-map approval** (Choose all ≠ map approval).

## Proposed move map (for planner)

| # | Source | CreationTime | LastWrite | Status (Q5) | Destination | `.git` | Collision | Move unit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `C:\Project\IA` | 2025-12-12 | 2025-12-12 | `archive` | `C:\Project\archive\2025.12.12 - IA` | none | none | whole tree (`Teams-Messages\`) |
| 2 | `C:\Project\AngularTest` | 2025-08-07 | 2025-08-07 | `archive` | `C:\Project\archive\2025.08.07 - AngularTest` | none | none | whole tree (folder + `.zip`) |
| 3 | `C:\Project\epsic` | 2025-12-10 | 2025-12-17 | `archive` | `C:\Project\archive\2025.12.10 - epsic` | none | none | whole tree (`BDD\`, `HTML\`, `BDD.zip`) |

**Parents:** `archive` and `paused` exist — no create required for this batch. `active` absent — not needed.

**ZedTest (verify only):**

| Expected | Observed | Action |
| --- | --- | --- |
| `C:\Project\paused\2026.06.30 - ZedTest` | Present | **No move** |
| `C:\Project\ZedTest` | Absent | No corrective move |

**Out of map:** Cycle 2 destinations; must-preserve draft; organisation repo; hygiene; other ROADMAP rows.

## Recommended approach options (max 3)

### Option A — Direct same-volume `Move-Item` per row (recommended)

Re-scan `.git` / collision → `Move-Item -LiteralPath` source → exact dated destination under `archive\` → update INDEX (+ inventory if planned) → log reverse paths.

- **Pros:** Matches Cycle 2; fast on same `C:`; whole-tree atomic per folder; simple reverse-move.
- **Cons:** Batch not transactional across three rows (partial possible).
- **Mitigation:** Sequential; stop on first failure; reverse already-moved on Critical if plan requires.

### Option B — Embedded pre-checks + live (Cycle 2 style)

Same as A with mandatory Test-Path + `.git` re-scan immediately before each move (optional `-WhatIf` only if user asks).

- **Pros:** Catches race between research and implement.
- **Cons:** Slightly more logging; still needs live pass.

### Option C — Copy-verify-delete

- **Pros:** Useful cross-volume.
- **Cons:** Unnecessary here; conflicts with prefer move/rename; duplicate risk.
- **Not recommended.**

**Recommended:** **Option A** with Option B’s pre-checks embedded.

## Required facts

- Sources exist; labels = CreationTime (`yyyy.mm.dd - ShortName`); spaces kept.
- LastWrites all before `2026-06-11` → all `archive` (refined-prompt catalogue hypothesis confirmed).
- No `.git` found — fail-closed re-scan still mandatory at implementer start.
- Targets absent; archive parent present.
- AngularTest / epsic are M-band — keep zip + extract in one move unit.
- INDEX still shows root paths + Status `TBD` for the three; ZedTest path already correct.
- Plan gate mandatory; prior Cycle 2 / Choose all ≠ this batch approval.

## Unknowns / residual risks (non-blocking)

| Risk | Severity | Handling |
| --- | --- | --- |
| `.git` appears between research and move | Medium | Skip item; log; no git-strategy invent |
| File lock (esp. larger epsic) | Low–Med | Retry once or skip+log |
| Partial batch | Medium | Per-row reverse-move notes |
| INDEX drift if docs fail after FS move | Medium | Catalogue update in same AC batch |

## Blockers

**none** for research → planning.

Process gates (not research blockers):

1. Planner writes exact map + `fs_mutation`; `ready_to_implement: no` until plan gate.
2. User explicitly approves that map in-session.
3. Implementer only after approval.

## Push / pull preflight

**N/A** — goal does not include `git push` / `git pull` / remote publish.

## Canonical references

- `sessions/2026.09.09-1517/01-prompt-betterment/refined-prompt.md`
- `sessions/2026.09.09-1517/01-prompt-betterment/notes.md`
- `catalogue/INDEX.md`, `catalogue/inventory.md`, `catalogue/taxonomy.md`
- `sessions/2026.09.09-1032/02-research/research-brief.md` (Cycle 2 prior art)
- `02-research/codebase-findings.md`, `02-research/online-findings.md`
- Microsoft Learn: [Move-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item)
