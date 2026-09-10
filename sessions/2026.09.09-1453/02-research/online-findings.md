# Online findings — Finish sync / Q3b=B combined-best (`sessions/2026.09.09-1453`)

Authoritative sources for merge of diverged histories, conflict preview without touching the working tree, and Windows HTTPS auth via GCM. No invented APIs; secrets not logged.

## Citations

1. **[Git - git-merge Documentation](https://git-scm.com/docs/git-merge)**  
   Merge joins histories since the merge-base; when tips have diverged, a merge commit (two parents) is the normal result unless ff-only is required. Content conflicts leave the merge incomplete until paths are resolved and staged. Aligns with **Q2=B** (merge commit allowed).

2. **[Git - git-merge-tree Documentation](https://git-scm.com/docs/git-merge-tree)**  
   Modern `--write-tree` mode performs a real three-way merge **without** reading or writing the index/working tree. Exit non-zero with conflicted path list (`--name-only`) is the safe preview used in this research turn. Tree may embed conflict markers for inspection.

3. **[Git - git-pull Documentation](https://git-scm.com/docs/git-pull)**  
   Pull = fetch + integrate. With merge strategy (not rebase / not ff-only), diverged `main`/`origin/main` is the same family of operation as `git fetch` then `git merge origin/main`. This repo has `pull.rebase=false`.

4. **[Git Credential Manager — configuration](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md)**  
   GCM is used when Git’s `credential.helper` includes `manager`. On Windows, default store is Windows Credential Manager (`wincredman`). Prefer the Git for Windows binary that ships this helper over MSYS git with an empty helper.

5. **[GitHub Docs — Caching your GitHub credentials in Git (Windows)](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git?platform=windows)**  
   Recommends Git for Windows + GCM for HTTPS GitHub. Missing `gh` CLI alone is not proof credentials are absent when GCM can fill.

6. **[How to resolve a merge conflict](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts)** (Pro Git)  
   Standard resolve loop: edit conflicted files (study both sides), remove markers, `git add`, then complete the merge commit. Matches **R1 combined-best** (judgment-per-hunk), not whole-file ours/theirs.

## Takeaways for this cycle

| Topic | Takeaway |
| --- | --- |
| Combine strategy | Official path for Q2=B: fetch + `git merge origin/main` (or pull without `--ff-only` / rebase). |
| Preview | `git merge-tree --write-tree [--name-only]` predicts conflicts without starting a merge — used live; 4 allowlist paths. |
| Resolve | Edit hunks by reading both sides; `git add`; complete merge. Abort with `merge --abort` only if policy fails (e.g. non-allowlist path). |
| Auth | Probe with GfW + GCM `credential fill`; log pass/fail and key *names* only — never password values. |
| Binary | Always use absolute GfW for porcelain, allowlist commit, fetch, merge, and resolve — not PATH/MSYS. |
