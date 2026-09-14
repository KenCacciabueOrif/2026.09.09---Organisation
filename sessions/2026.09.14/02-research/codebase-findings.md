# Codebase findings — kube.42header long-email clip

**Session:** `sessions/2026.09.14/`  
**Scope:** evidence + local install/settings only (no product edits).  
**Privacy:** full email appears in fixture/settings; prefer length + redacted form in prose (`k***@student.42lausanne.ch`, 30 chars).

## Fixture (bad header)

| Item | Evidence |
| --- | --- |
| Path | `C:\Project\current\ft_prework\ex0\ft_first_exception.py` |
| Other headers in `ft_prework` | **None** — Glob found only this `.py` file |
| Line 6 (exact) | `#    By: kcacciab <kcacciab@student.42lausanne.c    +#+  +:+       +#+         #` |
| Line length | **80** (norm-style) |
| Closing `>` | **Absent** (`HAS_GT=False`) |
| AUTHOR payload after `By: ` | `kcacciab <kcacciab@student.42lausanne.c` — **39 chars** |
| Intended email (settings / unclipped) | `kcacciab@student.42lausanne.ch` — **30 chars** |
| Clip point | Domain truncated mid-TLD: `…42lausanne.c` then spaces; missing `h>` |

**Reconstruction:** author string is `login <email>` = `kcacciab <kcacciab@student.42lausanne.ch>` (**41 chars**). Stock pad/clip to **39** yields exactly the fixture AUTHOR field (drops `h>`).

## Installed extension (this machine)

| Item | Value |
| --- | --- |
| Install path | `C:\Users\CaDa\.cursor\extensions\kube.42header-0.42.9-universal\` |
| Also under `.vscode\extensions`? | **No** matching `42header` folder |
| Marketplace ID | `kube.42header` |
| Version | `0.42.9` |
| Upstream repo (package) | https://github.com/kube/vscode-42header |
| Command | `42header.insertHeader` (Ctrl+Alt+H / Cmd+Alt+H) |
| Save hook | `onWillSaveTextDocument` rewrites header if present |

### Settings (correct; still buggy)

Source: `%AppData%\Roaming\Cursor\User\settings.json`

```json
"42header.username": "kcacciab",
"42header.email": "kcacciab@student.42lausanne.ch"
```

No other `42header.*` keys found. Username/email match the fixture login and the intended full campus mail. **Settings are not misconfigured** relative to Continuity.

### Root-cause mechanism (local `out/src`)

From `…\kube.42header-0.42.9-universal\out\src\header.js`:

- Template token `$AUTHOR________________________________` length = **39**.
- `pad(value, width)` = `value + spaces` then `.substr(0, width)` → **hard truncate**.
- `extension.js` builds `author: user + " <" + mail + ">"`.

So with official long mail, the closing `>` (and part of the domain) is cut **inside** the fixed AUTHOR slot. Changing settings to a shorter fake email would “fix” the symptom but violates Continuity; widening the template field (fork) is the intended class of fix.

Short-mail sanity (reasoned): `marvin <marvin@42.fr>` length 20 ≪ 39 → `>` preserved under stock kube — short emails still work; long emails fail.

## Org-repo / ROADMAP

- No corpus move / WorkSpace / INDEX work in scope.
- Session Continuity already locks fork/switch, not ROADMAP.
- Grep under `C:\Project` for local forks of the extension: **none** as editable product trees (session docs only).

## Related local extensions (not the product)

| Folder | Note |
| --- | --- |
| `dokca.42-ft-count-line-0.4.4-universal` | Line-count helper; unrelated to header AUTHOR pad |
| `ms-vscode.cmake-tools-…` | Name match noise only |

## Implications for planner/implementer

1. Treat fixture as **before** evidence; after fork switch, regenerate header (Ctrl+Alt+H or save) and assert full email + `>` on `By:` line.
2. **Disable/uninstall `kube.42header`** before enabling a fork — both register `42header.insertHeader` and save watchers → dual-extension fights.
3. Keep existing `42header.username` / `42header.email` (same keys on recommended forks).
4. Do not patch files under `.cursor\extensions\kube.42header-*` as the delivery path (Q2=B).
