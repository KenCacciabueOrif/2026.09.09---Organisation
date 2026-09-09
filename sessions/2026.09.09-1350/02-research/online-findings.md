# Online findings — Pull-autonomy / allowlist commit + ff-only

Sources checked 2026-09-09. Prefer official / primary docs. No secrets.

## `git pull --ff-only` and divergence

1. **[Git — git-pull documentation](https://git-scm.com/docs/git-pull)**  
   `--ff-only` updates only when history can fast-forward; it refuses divergent local history (no merge/rebase fallback). Matches locked Q2=A. After an allowlist commit on top of `f5012d6` while `origin/main` is `489f03a`, histories diverge → expect non-zero exit, not a silent merge.

2. **[Git — git-merge / ff-only behavior](https://git-scm.com/docs/git-merge)**  
   Fast-forward when tip is a descendant; otherwise refuse. Implementer must treat non-ff as fail-closed (Q3b/Q6), not switch to `--rebase` / `--no-ff` (out of scope this cycle).

3. **Divergent branches / “Not possible to fast-forward”** ([Git Tower FAQ](https://www.git-tower.com/learn/git/faq/you-have-divergent-branches))  
   Local and remote each gained commits → ff-only aborts. Remediation options (merge/rebase) exist in general Git practice but are **locked out** here by Q2=A + out-of-scope list.

## Dirty working tree vs pull

4. **Pull does not overwrite conflicting local WIP** (common Git behavior; see e.g. [Tower — force pull FAQ](https://www.git-tower.com/learn/git/faq/git-force-pull), [freeCodeCamp pull overview](https://www.freecodecamp.org/news/git-pull-force-how-to-overwrite-local-changes-with-git/))  
   If uncommitted changes would be overwritten by merge, Git aborts. This session has **7 overlapping** dirty paths with `HEAD..origin/main` — pull-while-dirty is not a safe shortcut. Prefer **commit allowlist** (locked Q3) over stash/autostash (rejected).

5. **Hard reset / clean to force sync** — widely documented but **forbidden** by hard AC (no hard reset, no force). Do not cite as implementer path.

## Git Credential Manager (HTTPS / Windows)

6. **[GCM configuration](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/configuration.md)**  
   `credential.helper manager`; Windows store typically `wincredman`. Explains preferring Git for Windows when PATH/MSYS has no helper.

7. **[Git — gitcredentials](https://git-scm.com/docs/gitcredentials)**  
   Helpers are per Git invocation/config; absolute GfW binary + its helper matters. Missing `gh` is unrelated when GCM fill succeeds.

8. **[GCM repository](https://github.com/git-ecosystem/git-credential-manager)**  
   GCM is the supported non-interactive HTTPS path for agent Shell on Windows with GfW.

## Agent vs user terminal

9. **[Cursor forum — agent authenticated git](https://forum.cursor.com/t/agent-cannot-run-git-push-or-other-authenticated-commands-no-access-to-user-credentials/151256)**  
   User-terminal success ≠ agent Shell ready. Dual preflight remains mandatory for pull (Q5=A).

## Session-local tips

10. **`sessions/2026.09.09-1350/01-prompt-betterment/online-prompt-tips.md`**  
    Prefer commit over stash for automation; fail-closed on conflict; do not invent stash-drop / `--no-verify`.

11. **`sessions/2026.09.09-1332/02-research/online-findings.md`**  
    Prior pull-cycle citations still valid for GfW/GCM/`--ff-only`; this cycle adds allowlist + diverge risk.

## Takeaways

- Document allowlist auto-commit as the FAW dirty default; keep abort for unrelated dirt.
- Same GfW binary for porcelain, allowlist commit, and pull.
- Expect **`--ff-only` refusal after allowlist commit** when remote is already ahead — that is fail-closed success of AC B (typed blocker), not auth failure.
- Never log credential fill passwords or full environment dumps.
