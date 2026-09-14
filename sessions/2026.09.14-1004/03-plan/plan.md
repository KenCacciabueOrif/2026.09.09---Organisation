# Plan — ensui 42 header ≤79 for flake8 (2026.09.14-1004)

## Goal

Make Python 42-school headers produced by **`ensui-dev.42header-multicampus`** pass **flake8 E501** (default **max-line-length=79**) while keeping the Continuity-correct **full** student email and trailing `>` on the By: line. Research proved there is **no** ensui width setting; stock templates always emit **80**-column frames. The smallest durable Continuity-aligned fix is a **local patch** of the installed extension’s frame/template + `extractHeader` regex (`.{80}` → `.{79}`), keeping **AUTHOR field width ≥41** (prefer keep **43**), then regenerate the fixture and verify with flake8. Prefer this over `# noqa` / ignore / raising max-line-length.

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`product_settings`** |
| Mutation kind | Local extension template tweak + local evidence fixture regenerate (not corpus path batch; not remote-config) |
| Corpus FS | **Zero** intentional corpus / catalogue moves, renames, or deletes under `C:\Project` ROADMAP batches |
| Org-repo disk | Session docs under `sessions/2026.09.14-1004/` only (FAW); **no** publish/push AC |
| User approval before implementer | **Not required** (`product_settings` — plan-gate **n/a**) |
| Same-run continue | **Yes** when `ready_to_implement: yes` → implement → mid git (if any allowlisted session dirt) → audit → self-improver → final git as FAW requires |
| First-move / taxonomy gates | **N/A** (not `fs_mutation`) |

**Primary product touchpoints**

| Role | Path / ID |
| --- | --- |
| Extension (keep) | `ensui-dev.42header-multicampus` (installed folder `ensui-dev.42header-multicampus-0.42.16-universal`) |
| Patch target | `%USERPROFILE%\.cursor\extensions\ensui-dev.42header-multicampus-0.42.16-universal\dist\extension.js` |
| Src note | Installed package has **no** `src/`; if a future install ships `src/header.ts`, mirror the same frame/`extractHeader` edits there for maintainability. Upstream reference: https://github.com/ensui-dev/vscode-42header-plus `src/header.ts` |
| Fallback extension IDs | **Do not switch** unless Continuity waived. Escape-only: `nopons.42next-header` / ft-utils-style 79 Python forks (out of scope for this plan) |
| User settings | Keep existing `42header.username` / `42header.email` / `42header.campus` — **no** width key exists; do **not** treat settings regenerate alone as the fix |
| Fixture | `C:\Project\current\ft_prework\ex0\ft_first_exception.py` |

**Implementer attestation (product_settings):** Log (1) exact extension path + version folder, (2) that only frame/`extractHeader` (and any sibling hard-coded `80` length checks in the same header module) changed — AUTHOR field width still ≥41 / prefer 43, (3) fixture line lengths ≤79 with full email + `>`, (4) flake8 command + result (install method if soft-installed), (5) re-apply note after Marketplace update. Soft tip: **Reload Window** after patching `dist/extension.js` so Cursor loads the patched bundle (optional UI tip, not a Continuity/plan gate).

## Context (locked Continuity)

- Prior session `sessions/2026.09.14/` complete — long-email / kube→ensui **do not reopen**.
- Failure mode confirmed: fixture header lines **len=80**; ephemeral flake8 → **E501** on lines 1–11; no project flake8 config under `ft_prework` → effective max **79**.
- ensui settings: username / email / campus only — **no width**.
- Publish: **local only** — dual push/pull preflight **N/A**.
- Continuity prioritizes **flake8 for Python prework** over classic Norminette-style **80**-col art for this fixture.

## Acceptance criteria

- [ ] Installed ensui remains the 42-header provider; kube leftover folder stays **disabled** / not re-enabled.
- [ ] `dist/extension.js` (and `src/header.ts` **if present**) patched so generic frame emits **79**-column header lines; `extractHeader` (and equivalent) `.{80}` → `.{79}`; any other hard-coded header-length `80` checks in that module updated consistently.
- [ ] AUTHOR field width remains **≥41**; prefer keep **43** — shrink comes from frame/border/padding, **not** from truncating email/login.
- [ ] Fixture `C:\Project\current\ft_prework\ex0\ft_first_exception.py` regenerated (or equivalently updated via extension insert/update) so **every** 42-header line is **≤79** characters.
- [ ] Fixture By: line still shows **full** `kcacciab <kcacciab@student.42lausanne.ch>` and closing `>` (no long-email regression).
- [ ] Primary fix is generator patch + fixture proof — **not** `# noqa: E501`, global `ignore = E501`, or `max-line-length≥80` as the intended solution.
- [ ] Soft-install flake8 if missing (`pip install flake8` user/venv or equivalent); run `python -m flake8` (or `flake8`) on the fixture with default config — **no E501** on header lines (W391 EOF blank or other non-header pre-existing issues may be noted; out of scope unless introduced by this change).
- [ ] Implementation log documents exact edits + **re-apply after extension update** procedure (Marketplace overwrite clobbers local patch).
- [ ] No ROADMAP / WorkSpace / corpus moves; no org-repo or `ft_prework` remote publish required.

## Steps

1. **Baseline confirm (read-only)**  
   - **Paths:** fixture; ensui extension folder under `~\.cursor\extensions\ensui-dev.42header-multicampus-*`.  
   - **Action:** Confirm header lines still len=80; settings still have correct email; ensui is intended provider (kube not enabled). Note installed version folder name.  
   - **Verify:** Log measured lengths + extension path.

2. **Patch ensui frame + detect regex**  
   - **Paths:** `…\ensui-dev.42header-multicampus-0.42.16-universal\dist\extension.js` (adjust version folder if upgraded). Optionally mirror in `src/header.ts` **only if that file exists** in the install.  
   - **Action:**  
     - Shorten `genericTemplate` (embedded multiline header art) from **80** to **79** columns per line — remove **one** padding/border column; **do not** shrink `$AUTHOR` + underscore field below width **43** (or at least **≥41**). Research local proof: one-column shrink preserves 41-char author token.  
     - Change `extractHeader` / match regex `^(.{80}…)` → `^(.{79}…)`.  
     - Grep the same file for other hard-coded header-width `80` tied to frame detection; update those consistently. Do **not** change username/email settings.  
   - **Verify:** Grep shows no remaining frame-detect `.{80}` for headers; AUTHOR underscore count still yields field width ≥41 (prefer 43).

3. **Reload extension host**  
   - **Action:** Reload Cursor window (or otherwise force extension re-load) so patched `dist/extension.js` is active. Soft tip only if Reload UI is needed.  
   - **Verify:** Note in log that Reload was performed (or why skipped if agent regenerates via direct template render equivalent — prefer real command path when available).

4. **Regenerate fixture header**  
   - **Path:** `C:\Project\current\ft_prework\ex0\ft_first_exception.py`.  
   - **Action:** Re-insert / update 42 header via ensui command (or documented equivalent that uses the patched template). Preserve exercise body below header.  
   - **Verify:** PowerShell/Python length probe — all header lines **≤79**; By: still full email + `>`; no kube-style truncate.

5. **Soft-install flake8 (if missing) + verify**  
   - **Action:** If `python -m flake8` / `flake8` unavailable, `pip install flake8` into user env or a disposable/project venv (document which). Run flake8 on the fixture with **default** max 79 (no project config expected).  
   - **Verify:** **No E501** on header lines 1–11. Note any non-header issues (e.g. W391) as out of scope.

6. **Document repeatability + update risk**  
   - **Paths:** `sessions/2026.09.14-1004/04-implementation/log.md` (implementer).  
   - **Action:** Record exact string/regex changes, AUTHOR width kept, Reload + regenerate steps, and **re-apply after ensui Marketplace/Open VSX update** (patch is machine-local and overwritten on upgrade). Optional nice-to-have (not AC): upstream issue/PR for official Python 79 or configurable width.  
   - **Verify:** Auditor can re-apply from the log alone.

7. **Session hygiene (non-publish)**  
   - **Action:** Write FAW phase artifacts only under this session; do **not** commit/push org-repo or sibling `ft_prework` unless a later publish Continuity asks. Mid/final git-manager only for allowlisted session dirt if orchestrator runs them.  
   - **Verify:** No corpus ROADMAP mutations; no false publish claim.

## Non-goals

- Reopening long-email truncate / kube→ensui migration design.
- Switching to `nopons.42next-header`, ft-utils, or other forks (Continuity keep ensui).
- `# noqa: E501`, per-file-ignores, or raising `max-line-length` as the primary fix.
- Norminette / C 80-col compliance as AC for this Python fixture (see Risks).
- ROADMAP, WorkSpace, Multi-experiment, corpus archive/moves.
- Publishing/pushing organisation repo or any `ft_prework` remote.
- Changing exercise logic below the header; fixing unrelated flake8 codes (e.g. W391) unless introduced by this change.
- Force-editing User `settings.json` for a non-existent width key.

## Risks / rollback

| Risk | Mitigation / rollback |
| --- | --- |
| **Norminette-80 vs flake8-79 tradeoff** | Classic 42 / Norminette culture expects **80**-col banners; flake8/PEP8 default is **79**. Shrinking Python headers to 79 is the accepted community tradeoff for E501 and matches Continuity for **Python prework**. If a later school checker requires exact 80-col Norminette art on `.py`, this patch would diverge — out of scope unless that checker is introduced; do not “fix” by raising flake8 max. |
| Patch only template, leave `extractHeader` on `.{80}` | Always patch detect regex together; verify update-on-save still recognizes 79-col headers. |
| AUTHOR narrowed &lt;41 | Regress long-email Continuity — **forbidden**. Keep field **43** (or ≥41); steal column from frame only. |
| Extension update clobbers patch | Document re-apply; optional upstream PR later. |
| kube leftover re-enabled | Do not enable; conflicting insert/save. |
| flake8 missing on machine | Soft-install for AC verify (research: system flake8 absent). |
| Reload skipped → old 80 art still emitted | Reload after patch before regenerate. |
| Rollback | Restore stock `dist/extension.js` from Marketplace reinstall / copy backup of pre-patch file; restore fixture from prior session art if needed. Prefer copy backup of `extension.js` before edit. |

## Ready to implement

**yes**

Plan-gate **n/a** (`product_settings`). No blocking product decisions remain; Continuity locks (keep ensui, ≤79, patch+fixture, no ignore-first, local only) are sufficient.

## Blocking questions

**none**
