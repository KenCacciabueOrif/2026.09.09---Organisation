# Online findings — 2026.09.14-1004 (42 header vs flake8 79)

## flake8 / pycodestyle default

1. **pycodestyle intro (stable)** — https://pycodestyle.pycqa.org/en/stable/intro.html  
   - `--max-line-length=n` default **79**; **E501** = line too long. Config may live in `setup.cfg` / `tox.ini` `[pycodestyle]` (or flake8 sections).  
   - Takeaway: with no project config under `ft_prework`, E501 at 80 is expected.

2. **pycodestyle source** — https://github.com/PyCQA/pycodestyle/blob/main/pycodestyle.py  
   - `MAX_LINE_LENGTH = 79`; `maximum_line_length` documents PEP 8 “limit all lines to a maximum of 79 characters” and reports E501.  
   - Takeaway: physical lines including `#` comment headers count toward the limit (no header exemption).

## Classic 42 header = 80 columns

3. **42Paris vim stdheader** — https://github.com/42Paris/42header/blob/master/plugin/stdheader.vim  
   - `s:length = 80` hardcoded. Author overflow falls back to mail-only, not frame shrink.  
   - Takeaway: school Norminette / C culture is **80-col** banners; that conflicts with Python flake8 **79**.

4. **ensui fork README / repo** — https://github.com/ensui-dev/vscode-42header-plus  
   - Positions itself as additive multicampus fork; header format “unchanged” / “identical” to kube. Settings: username / email / campus only.  
   - Takeaway: **no published setting** for 79-col or per-language width.

5. **ensui `src/header.ts` (raw)** — https://raw.githubusercontent.com/ensui-dev/vscode-42header-plus/master/src/header.ts  
   - `genericTemplate` lines are 80 `*`-frame columns; `extractHeader` uses `^(.{80}…){10}`. `pad` truncates field values to template field width.  
   - Takeaway: durable 79 fix requires **template + extract regex** change (or a different extension), not User Settings.

## Forks that already emit 79 for Python

6. **nopons / 42Next Header** — Marketplace `nopons.42next-header`; README https://github.com/guizafj/42Next_Header  
   - Explicit **“Python (79 characters - flake8)”** banner (visually different from classic kube art; C remains 80).  
   - Takeaway: solves E501 but **breaks Continuity** “keep ensui” and may diverge from classic Norminette look for Python.

7. **ft-utils VS Code** — https://github.com/2mdtln/ft-utils-vscode (Marketplace-oriented utils)  
   - Documents **79-character total header width for Python** specifically to avoid flake8 E501; C stays school-style. Different settings namespace (`ft_utils.*`).  
   - Takeaway: purpose-built flake8-friendly path; switching away from ensui is Continuity escape hatch only.

8. **secondfry.42header-long** — https://marketplace.visualstudio.com/items?itemName=secondfry.42header-long  
   - Widens AUTHOR/filename fields for long emails; Marketplace sample still shows **80-col** classic frame. Prior cycle: not installable via Cursor Open VSX.  
   - Takeaway: addresses email truncate, **not** the 80↔79 flake8 conflict.

9. **nvim header42 textwidth pattern** — e.g. https://github.com/Ilaivdv/nvim-42header (Codam / similar ports)  
   - Some Neovim ports use `textwidth` 80 for C and **79 for Python**.  
   - Takeaway: community pattern is **language-specific width**, which ensui/kube lack.

## Norminette 80 vs flake8 79 tradeoff

10. **Community consensus (fork READMEs above)**  
    - C / Norminette-oriented tools keep **80**.  
    - Python / flake8-oriented forks deliberately shrink Python banners to **79**.  
    - Takeaway: shrinking Python headers to 79 is the accepted tradeoff for E501; C headers can stay 80. ensui today uses one 80 template for all languages after delimiter swap — a Python-only 79 path would be an enhancement, not a settings toggle.

## VS Code flake8 ignore / max-length (escape hatch only)

11. **vscode-flake8 args patterns** — e.g. Stack Overflow / microsoft/vscode-flake8 discussions on `flake8.args` `--max-line-length=…` / `--ignore=E501`  
    - Easy to silence E501 or raise max to 80.  
    - Takeaway: works but Continuity ranks this **below** fixing the generator; masks other long lines if applied globally.
