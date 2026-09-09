# Organisation-approach recommendation

**Cycle 0:** recommend only — **no moves executed**.  
**Cycle 1:** taxonomy **proposed-ratified — ready for user sign-off**; status axis locked to `active` / `paused` / `archive` (+ INDEX `protect` / `hygiene`). Still **no moves**.  
**Sources:** `sessions/2026.09.09-0929/02-research/research-brief.md`, `online-findings.md`; Cycle 1 locks in `sessions/2026.09.09-1009/01-prompt-betterment/`.

## Preferred: Option 1 — Hybrid

**Organisation-repo index now + gradual status×date layout under `C:\Project` later.**

1. Maintain a whole-corpus **index** in this repo (`catalogue/INDEX.md`) as the primary “dated view + next + find it” surface — even before physical layout finishes.
2. In later approved cycles, introduce light **status buckets** (`active` / `paused` / `archive`, plus INDEX specials `protect` / `hygiene`) and rename/move projects to `yyyy.mm.dd - DescriptiveName`, one top-level folder (or approved batch) at a time.
3. Treat each `.git` as an **atomic unit**; include deps and opaque secrets with the move.

**Status vocabulary (locked Cycle 1):** `active` / `paused` / `archive` (+ `protect` / `hygiene`). **PARA-lite** is **not** an open alternative for this program (deferred/rejected).

Cycle 0–1 implement **index + docs only**. Physical layout waits for approved move cycles per [`ROADMAP.md`](ROADMAP.md). **Primary next suggestion:** Early/simple after per-batch approval.

## Options (≤3)

### 1. Hybrid index + status×date FS (preferred)

| | |
| --- | --- |
| **What** | Index in org repo now; gradual moves into status buckets with dated names under `C:\Project`. |
| **Dated view** | Strong — date-prefix names + chronological index. |
| **What’s next** | Status buckets + index “Next” column. |
| **Navigation** | Index immediate; FS improves over cycles. |
| **Risks** | Temporary dual reality (old paths + new index) until batches complete; discipline to update index after each move. |
| **Fit** | Matches end-state; FAW-friendly adaptive cycles; lowest early-breakage risk. |

### 2. Index-only (catalog; defer almost all FS change)

| | |
| --- | --- |
| **What** | Rich inventory and “next” lists; leave folders in place except rare approved hygiene. |
| **Dated view** | Via metadata only. |
| **What’s next** | Via index triage. |
| **Navigation** | Index helps; messy wrappers/names remain on disk. |
| **Risks** | Weakens physical “organisation” end-state; user already expects later agent-executed moves after approval. |
| **Fit** | Good fallback if physical reorg is later rejected; fastest early value. |

### 3. Pure chronological flat corpus

| | |
| --- | --- |
| **What** | Re-home under year/date folders or only `yyyy.mm.dd - name` with little/no status layer. |
| **Dated view** | Strong. |
| **What’s next** | Weak — active work buried among archives. |
| **Navigation** | Chronology helps history more than triage. |
| **Risks** | Same git/worktree move risks as hybrid without status navigation benefit. |
| **Fit** | Reject as default; status layer is needed for the program end-state. |

## Citations (optional context)

- [Status-first developer Projects layout](https://thatamazingprogrammer.com/posts/a-practical-folder-structure-for-developers-and-solopreneurs/) — active/paused/archive pattern (program lock).
- [PARA Method – Forte Labs](https://fortelabs.com/blog/para/) — historical context only; **not** the open status choice for this program.
- [Date-prefix naming practices](https://renamer.ai/insights/file-naming-conventions-best-practices) — chronological sort; gradual rename.
- Local research: `sessions/2026.09.09-0929/02-research/online-findings.md`, `sessions/2026.09.09-1009/02-research/`.

## Cycle restatement

**No moves, renames, or deletes under `C:\Project` in Cycle 0 or Cycle 1.** Deliverables are documentation and the corpus index only.
