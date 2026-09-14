# Online findings — kube.42header long email

Citations include title, URL, and a short takeaway. Prefer official Marketplace / GitHub sources.

## Known bug (upstream)

1. **The problem with the email in the header** — https://github.com/kube/vscode-42header/issues/18  
   Open since 2020. Emails longer than ~28 chars clip the closing `>`; Norminette fails. Asks for ≥35-char email support. Matches this session’s fixture class (missing `>`).

2. **PR #17 Update header.ts** — https://github.com/kube/vscode-42header/pull/17  
   Attempted school-email fit fix; **closed without merge** into `kube` (not shipped in stock `0.42.9`). Commenters pointed users at the PR and later at a Marketplace fork.

3. **kube/vscode-42header** — https://github.com/kube/vscode-42header/  
   Upstream README still documents `42header.username` / `42header.email`. Template AUTHOR field remains short (`$AUTHOR________________________________`, 39). Marketplace last update **2016-12-11**, ver **0.42.9**.

4. **Upstream pad behavior (source)** — https://raw.githubusercontent.com/kube/vscode-42header/master/src/header.ts  
   `pad` = concat spaces + `substr(0, width)` — truncates overflowing AUTHOR values. Confirms settings cannot enlarge the field.

## Forks / Marketplace IDs

| Extension ID | Marketplace | Last updated (API) | Installs (API) | Long-email relevance |
| --- | --- | --- | --- | --- |
| `secondfry.42header-long` | https://marketplace.visualstudio.com/items?itemName=secondfry.42header-long | 2021-01-11 | ~9.6k | **Purpose-built** — advertised as using whitespace for filename/email; linked from issue #18 by publisher |
| `ensui-dev.42header-multicampus` | https://marketplace.visualstudio.com/items?itemName=ensui-dev.42header-multicampus | 2026-05-09 | ~25 | Actively maintained; campus presets; measured AUTHOR token **43** (fits 41-char `login <mail>`) |
| `nopons.42next-header` | https://marketplace.visualstudio.com/items?itemName=nopons.42next-header | 2026-03-19 | ~833 | Newer; **different** Python/flake8 79-col look — higher Norminette/format risk for classic 80-col C headers |
| `kube.42header` | https://marketplace.visualstudio.com/items?itemName=kube.42header | 2016-12-11 | ~219k | Stock buggy product |

### Source evidence on field widths

5. **secondfry/vscode-42header** — https://github.com/secondfry/vscode-42header  
   README: “using all whitespace for filename, email and other fields.” Measured `$AUTHOR___________________________________` = **42** → pads `kcacciab <…@student.42lausanne.ch>` with `>` intact.

6. **ensui-dev/vscode-42header-plus** — https://github.com/ensui-dev/vscode-42header-plus  
   Marketplace ID in docs: `ensui-dev.42header-multicampus`. Marketing says output can be byte-identical to upstream for same inputs, but **current `header.ts` AUTHOR width is 43**, not kube’s 39 — so it also absorbs this Lausanne-length mail. Primary feature is multi-campus email derivation + maintenance (`moment`, tests, `onStartupFinished`). Same settings keys; optional `42header.campus`.

7. **Open VSX**  
   - `ensui-dev/42header-multicampus` present (ver 0.42.16).  
   - `secondfry/42header-long` **not found** on Open VSX (`Extension not found`).  
   Implication: Cursor/Open-VSX-only installs may need Marketplace VSIX / Marketplace-enabled install for secondfry; ensui is easier on Open VSX.

## Classic Vim reference (escape hatch, not preferred)

8. **42Paris/42header `stdheader.vim`** — https://github.com/42Paris/42header/blob/master/plugin/stdheader.vim  
   Computes available width; if `By: user <mail>` overflows, falls back to `By: mail` only. Different UX than VS Code forks; Continuity prefers extension fork/switch, not Vim.

## Safe switch practice (editor)

Documented pattern for VS Code / Cursor (community + extension APIs):

1. **Disable or uninstall** `kube.42header` first (Extensions panel → Disable/Uninstall, or CLI `cursor --uninstall-extension kube.42header` / `code --uninstall-extension kube.42header` if available).
2. **Install** chosen fork by ID (`ext install secondfry.42header-long` or Marketplace search “42 Header (Long)”; or `ensui-dev.42header-multicampus`).
3. **Keep** User settings `42header.username` / `42header.email` unchanged (official long mail).
4. **Reload window** after swap.
5. **Re-insert** header (`Ctrl+Alt+H`) or touch-save so the save watcher rewrites `By:`.
6. Avoid enabling **two** header extensions that both own `42header.insertHeader` and `onWillSave` — race/conflict.

Agent limitation: Marketplace install may require **user UI approval**; plan should include user install steps + agent verification of regenerated fixture line.

## What “correct settings still fail” looks like

Authoritative description for AC:

- Settings already contain full campus email (30 chars) and login.
- Insert/update still emits 80-col `By:` line where AUTHOR slot is only 39 chars → email ends at `…lausanne.c`, **no `>`**, then padding into the ` +#+  +:+` art.
- Shortening email in settings would hide the bug; Continuity forbids that workaround.
