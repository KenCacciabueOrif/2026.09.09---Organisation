# Research brief

**Goal:** Make ensui-generated 42 headers pass flake8 line-length on Python while keeping full long email + `>` (Continuity).  
**Mutation class:** `product_settings` — extension and/or local fixture; not ROADMAP/corpus.  
**Publish:** local only — dual push/pull preflight **N/A**.

## Recommended approach

**Primary (smallest durable fix matching Continuity):** Keep `ensui-dev.42header-multicampus`. There is **no settings knob** for width — patch the installed extension template (and matching `extractHeader` `.{80}` → `.{79}`) so the generic frame is **79** columns while **AUTHOR field stays ≥41** (current **43** is fine; steal the column from border/padding, not from the email). Reload Cursor, regenerate the fixture header, then verify with flake8 (install if missing).

**Do not** treat User Settings regenerate alone as sufficient — settings already correct; stock ensui always emits 80.  
**Do not** prefer `# noqa: E501` / global ignore / `max-line-length=80` first.  
**Do not** reopen long-email / kube→ensui migration; do not switch forks unless patch path is rejected.

## Options considered (max 3)

1. **Local ensui template patch → 79-col frame + regenerate fixture (recommended)**  
   - **Pros:** Keeps ensui + full email; new inserts stay clean after Reload; matches Continuity “fix the header, not the linter”; AUTHOR 43 still fits 41-char author; one-column shrink proven on fixture.  
   - **Cons:** Overwritten on extension update (re-apply or upstream PR); must change both template lines **and** `extractHeader` regex or update-on-save may break; touches machine-local extension files (document path).

2. **Switch to a 79-aware extension (`ft_utils` / `nopons.42next-header`)**  
   - **Pros:** Purpose-built Python 79 headers; no hand-patch of ensui.  
   - **Cons:** Violates locked Continuity “keep ensui”; 42Next look differs from classic; settings namespace change; prior cycle already paid for ensui long-email path.

3. **flake8 escape hatch (`max-line-length=80` or ignore E501 on headers)**  
   - **Pros:** Zero header change; preserves Norminette-style 80 art.  
   - **Cons:** Continuity ranks last; global raise/ignore hides other long lines; does not match “header is one character too long.”

## Required facts

| Fact | Value |
| --- | --- |
| Fixture header lines 1–11 | All **len=80** |
| By: email + `>` | Already correct (author string len **41**) |
| flake8 default max | **79** (`pycodestyle.MAX_LINE_LENGTH`) |
| Project flake8 config under `ft_prework` / nearby | **None** → effective max **79** |
| Ephemeral flake8 on fixture | **E501 on lines 1–11** (`80 > 79`); W391 EOF blank out of scope |
| ensui settings | `username` / `email` / `campus` only — **no width** |
| ensui AUTHOR width | **43**; frame **80**; detect regex **80** |
| System flake8 install | **Absent** — implementer must install flake8 (user/venv) for AC verify |
| kube leftover folder | May remain on disk; must stay disabled |

## Unknowns / blockers

| Item | Status |
| --- | --- |
| Settings-only 79-col from ensui | **Ruled out** (proven) |
| Durable across ensui Marketplace updates | Soft risk — document re-patch or file upstream issue/PR |
| Norminette on this machine | Still absent (prior cycle); Python AC is flake8, not Norminette |
| Whether school graders use flake8 79 vs allow 80 | Assumed 79 per Continuity; no `ft_prework` override found |
| Agent can edit extension under `~\.cursor\extensions\` | Expected yes for product_settings; Reload required |

**Blockers for planning:** **none** that stop a plan. Soft dependency: install flake8 for verification. Soft risk: extension update clobber.

### Push/auth dual preflight

**Skipped (N/A)** — Q6/local only; no org-repo publish AC.

| Field | Value |
| --- | --- |
| Remote URL scheme | n/a |
| Tracking branch | n/a |
| Agent git / GCM | n/a |
| `blocker_type` | none (for publish) |

### Dirty / pull preflight

**Skipped (N/A)** — not a sync cycle.

## Risks

- Patching only the template but leaving `extractHeader` on `.{80}` → extension may fail to detect/update existing 79-col headers on save.
- Narrowing AUTHOR below 41 → regresses long-email Continuity (must not).
- Leaving kube enabled or reinstalling it → conflicting insert/save (currently leftover folder only).
- Using 42Next/ft_utils without Continuity waiver → policy / visual mismatch.
- Raising flake8 max to 80 “just for headers” via global args → masks non-header E501.

## Canonical references

- Fixture: `C:\Project\current\ft_prework\ex0\ft_first_exception.py`
- ensui bundle: `~\.cursor\extensions\ensui-dev.42header-multicampus-0.42.16-universal\dist\extension.js`
- ensui source: https://raw.githubusercontent.com/ensui-dev/vscode-42header-plus/master/src/header.ts
- pycodestyle E501 / default 79: https://pycodestyle.pycqa.org/en/stable/intro.html
- 42 vim 80-col: https://github.com/42Paris/42header/blob/master/plugin/stdheader.vim
- 79 Python forks (escape only): https://github.com/guizafj/42Next_Header ; https://github.com/2mdtln/ft-utils-vscode
- Prior cycle brief: `sessions/2026.09.14/02-research/research-brief.md`

## Suggested implementer verification checklist

1. Confirm ensui still only 42header provider; kube not re-enabled.
2. Patch ensui template to **79**-col frame; keep AUTHOR field width ≥41 (prefer keep 43).
3. Patch `extractHeader` / equivalent `.{80}` → `.{79}` (and any other hard-coded 80 length checks in the same module).
4. Reload Cursor window.
5. Regenerate fixture header (command or equivalent render); assert By: full email + `>`; all header lines **≤79**.
6. `pip install flake8` (user or project venv) if needed; run `python -m flake8` on fixture — **no E501** on header lines.
7. Document exact files/settings changed for repeatability (including re-apply after extension update).
8. Optional: open upstream ensui issue/PR for official Python 79 or configurable width (nice-to-have, not AC).
