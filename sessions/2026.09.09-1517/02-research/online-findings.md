# Online findings — Cycle 3 Early/simple remaining

**Session:** `sessions/2026.09.09-1517/02-research/`  
**Scope:** Brief — same-volume folder moves / PowerShell (no new libraries). Push/pull not in goal.

## Citations

1. **Move-Item (Microsoft Learn)** — https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item  
   Moves item + children recursively by default; destination can rename in one step. Same-provider directory moves stay on the same drive. Prefer exact destination path; collision raises error unless Force (do not Force over existing project trees).

2. **Rename-Item (Microsoft Learn)** — https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-item  
   Renames in place only — cannot relocate. For move+dated rename under `archive\`, use `Move-Item`, not `Rename-Item`.

3. **Robocopy move metadata (Microsoft Q&A)** — https://learn.microsoft.com/en-us/answers/questions/3932359/how-do-i-use-robocopy-to-do-a-task-like-the-file-e  
   Cross-volume / metadata-heavy moves sometimes use robocopy `/MOVE` + `/DCOPY:DATE`. Unnecessary for same-volume `C:\Project\…` → `C:\Project\archive\…` when `Move-Item` suffices (Cycle 2 pattern).

## Takeaway for this cycle

Same-volume whole-tree `Move-Item -LiteralPath` to dated destination under existing `archive\` matches Cycle 2 and official Move-Item semantics. No agent remote publish.
