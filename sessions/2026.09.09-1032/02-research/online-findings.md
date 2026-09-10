# Online findings — safe local folder moves / status buckets / dated names

**Session:** `sessions/2026.09.09-1032/02-research/`  
**Focus:** brief practices for bulk *local* folder relocates into status parents with dated rename. Not cloud sync / remote publish.

## Citations

1. **Move-Item (Microsoft Learn)** — https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item  
   Official cmdlet: moves item + children recursively by default; destination parents are **not** auto-created; use `-LiteralPath` when names have special characters; `-WhatIf` for dry-run; destination name collision errors unless `-Force` (prefer **no** overwrite for this program). Same-drive directory moves stay on one volume — appropriate for `C:\Project\…` → `C:\Project\{archive|paused}\…`.

2. **Move-Item safety notes (Netwrix overview)** — https://www.netwrix.com/en/resources/blog/powershell-move-file/  
   Practical guidance: pre-check with `Test-Path`, use try/catch + logging, create destination folder structure first, prefer explicit one-source → one-destination moves, back up before overwrite scenarios. Aligns with FAW pre/post existence checks and reverse-move logging.

3. **PARA Method (Tiago Forte / Forte Labs)** — https://fortelabs.com/blog/para/  
   Status-bucket intuition: keep inactive but retained material in an **Archive** (or equivalent) rather than deleting; actionability separates active vs archived. This program uses `active` / `paused` / `archive` (taxonomy explicitly **not** full PARA-lite), but the “archive = keep, don’t delete” principle matches CHARTER opaque-payload / no-delete-to-clean rules. `paused` is a local middle bucket for recently touched Early/simple work.

4. **Dated naming practice (ISO-style prefixes in digital filing guides)** — e.g. community PARA naming guides using `YYYY-MM-DD` / `YYYY-MM` prefixes (illustrative: https://github.com/smithjoshua/claude-code-cowork-skills-file-organizer/blob/master/docs/PARA-GUIDE.md)  
   Takeaway: leading date sorts chronologically and preserves start signal. This corpus locks **dots** (`yyyy.mm.dd`) + ` - ShortName` with spaces kept (see `catalogue/taxonomy.md`) — same idea, different separator convention.

5. **Batch move hygiene (dry-run / verify / undo plan)** — https://solr.pling.com/article/how-to-perform-a-batch-move-file-operation-safely-and-efficiently  
   Prefer dry-run first, small subset before large batches, log successes/failures, keep an undo plan (reverse move). Matches this cycle’s **subset of 3** + mandatory plan gate + reverse-move notes in the implementation log.

## Practices mapped to this cycle

| Practice | Application here |
| --- | --- |
| Create parents first | `New-Item` `C:\Project\archive` and `C:\Project\paused` before moves |
| Literal paths | Use `-LiteralPath` for `yyyy.mm.dd - Name` (spaces / hyphens) |
| No silent overwrite | Do not `-Force` into existing targets; collision → stop/skip |
| Whole-tree move | One `Move-Item` per top-level folder (zip+extract stay together) |
| Dry-run optional | `-WhatIf` or plan-gate approval before live move |
| Rollback | Document reverse `dest → source` (or reverse into restored root name) |
| Same volume | All under `C:\Project` — simple rename/move semantics |

## Out of scope online topics

- Git worktree / remote rewrite (not this batch — no `.git`)
- Cross-volume copy+delete transactional patterns (not required on same `C:`)
- Full PARA Projects/Areas/Resources taxonomy (rejected/deferred for this program)
