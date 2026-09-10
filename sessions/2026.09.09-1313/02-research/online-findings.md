# Online findings

Brief sources for personal Markdown note folders in a git repo (naming, README, `.gitkeep` vs README). Prefer official / widely cited guidance; no invented APIs.

## Citations

1. **About READMEs (GitHub Docs)** — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes  
   READMEs communicate purpose and how to get started; keep them to necessary info. Nested READMEs are normal; GitHub’s special surfacing applies mainly to root / `.github` / `docs` — a folder-level README still documents local convention for clones and editors.

2. **Personal knowledge base with Markdown & Git (Alibaba Life Tips)** — https://lifetips.alibaba.com/tech-efficiency/personal-knowledge-base-with-markdown-git  
   Practical pattern: plain `.md` in git; start with a README; name dated notes consistently (e.g. `YYYY-MM-DD-topic-…`); prefer relative links; avoid dumping large binaries into the notes tree. Supports this cycle’s date-first filename habit (repo already uses dotted `yyyy.mm.dd`).

3. **The Directory-README Pattern (Kody Wildfeuer)** — https://kody-w.github.io/2026/04/24/directory-readme-pattern/  
   Per top-level subdirectory, a short README should state what belongs, what does not, and naming rules — especially useful when the folder accumulates contributions over time. Matches refined AC (purpose, how to add, filename pattern, exclusion vs catalogue/corpus).

4. **Commit empty folder structure (Stack Overflow)** — https://stackoverflow.com/questions/14541253/commit-empty-folder-structure-with-git  
   Git tracks files, not empty directories. Placeholders (`.gitkeep` or a README) are community workarounds. A documenting `README.md` both tracks the folder and explains intent.

5. **Tracking Empty Folders (.gitkeep) — LetCodes** — https://letcodes.com/git/git-keep  
   `.gitkeep` is convention only (not a Git feature). Prefer `README.md` when the directory’s purpose needs explanation for future readers — aligns with locked “README only, no `.gitkeep`”.

6. **Understanding .keep and .gitkeep (DeployHQ)** — https://www.deployhq.com/blog/understanding-keep-and-gitkeep-files-a-guide  
   Use `.gitkeep` for intentionally empty dirs that will later hold tracked files; remove once real files exist. When documentation is the deliverable, README supersedes a blank keep file.

## Takeaways for this cycle

| Topic | Practice | Fit to refined prompt |
| --- | --- | --- |
| Folder tracking | Need at least one tracked file | `Notes/README.md` is enough; **no `.gitkeep`** |
| Folder README | Purpose + belongs / does-not-belong + naming | Exact AC sections |
| Note filenames | Consistent date-first names | Recommend `yyyy.mm.dd-topic.md` (convention only) |
| Scope of README | Short; not a full wiki/CMS | No sample notes, apps, or automation |
| Root README pointer | Optional later | Out of scope this cycle unless user asks |

## Not required online

No library/SDK APIs named in the refined prompt. No publish/auth docs needed (create-only; no commit/push).
