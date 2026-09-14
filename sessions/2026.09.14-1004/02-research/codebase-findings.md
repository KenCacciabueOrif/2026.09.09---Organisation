# Codebase findings — 2026.09.14-1004 (42 header vs flake8 79)

## Fixture measurement

**Path:** `C:\Project\current\ft_prework\ex0\ft_first_exception.py`  
**Probe:** PowerShell `Get-Content` + `.Length` (UTF-8).

| Line | Length | Notes |
| --- | --- | --- |
| 1–11 (all header) | **80** each | Classic 42 frame |
| 6 (`By:`) | **80** | Full `kcacciab <kcacciab@student.42lausanne.ch>` + closing `>` present |
| Author token | **41** chars | `login <email>` — fits ensui AUTHOR **43**; spare pad **2** |

**Verdict:** Content is Continuity-correct; frame is **one column too wide** for flake8 default 79.

## flake8 run (this machine)

| Probe | Result |
| --- | --- |
| `flake8` on PATH | **Absent** |
| `python -m flake8` (system 3.11) | **No module named flake8** |
| hermes / msys Python | Same — no flake8 |
| Ephemeral venv (`%TEMP%\faw-flake8-probe`) + `pip install flake8` | **flake8 7.3.0** / pycodestyle **2.14.0** |

Ephemeral flake8 on fixture (default config):

```
ft_first_exception.py:1:80: E501 line too long (80 > 79 characters)
… (same E501 for lines 2–11)
ft_first_exception.py:12:1: W391 blank line at end of file   # out of scope
```

`pycodestyle.MAX_LINE_LENGTH` printed as **79**. Failure mode confirmed as **E501**, not a different rule.

## Project flake8 config (effective max)

Searched under:

- `C:\Project\current\ft_prework\` (recursive): **no** `setup.cfg` / `tox.ini` / `.flake8` / `pyproject.toml` / `.pycodestyle`
- `C:\Project\current\` (depth 2): **none** found for this tree

**Effective max for students on this fixture:** flake8/pycodestyle default **79**. Target for AC = **≤79**.

## ensui-dev.42header-multicampus (installed)

| Item | Value |
| --- | --- |
| Install path | `~\.cursor\extensions\ensui-dev.42header-multicampus-0.42.16-universal\` |
| Settings keys only | `42header.username`, `42header.email`, `42header.campus` |
| **Width / max-line setting** | **None** — cannot emit 79 via settings alone |
| Template | Hardcoded **80**-column `genericTemplate` in `dist/extension.js` |
| AUTHOR placeholder | `$AUTHOR` + 36 `_` → field width **43** |
| FILENAME field | **51** |
| Header detect regex | `^(.{80}(\r\n|\n)){10}` — also hardcodes 80 |
| README claim | Output “byte-identical” to upstream kube (canonical 80-col) |
| Upstream source | https://github.com/ensui-dev/vscode-42header-plus → `src/header.ts` same 80 template + `.{80}` |

User settings (kept from prior cycle):

- `42header.username`: `kcacciab`
- `42header.email`: `kcacciab@student.42lausanne.ch` (len 30)

## Leftover kube folder

`~\.cursor\extensions\kube.42header-0.42.9-universal\` still on disk (prior log: uninstalled from CLI; leftover folder OK). Do **not** re-enable. Only ensui is the intended provider.

## Prior cycle art (do not reopen email truncate)

- Session `sessions/2026.09.14/` — switched kube → ensui; AUTHOR 39→43; fixture By: fixed.
- That cycle **verified 80-col** as success criterion; flake8 79 was not in scope then.

## 79-col shrink feasibility (local proof)

Removing **one** character at index **77** (0-based) from each of the 11 header lines yields **len=79** on all lines; line 6 still matches `42lausanne.ch>`. So full email + `>` survive a one-column frame shrink; AUTHOR field need not be narrowed below 41.

## Paths that matter for planner/implementer

- Fixture: `C:\Project\current\ft_prework\ex0\ft_first_exception.py`
- Extension bundle: `~\.cursor\extensions\ensui-dev.42header-multicampus-0.42.16-universal\dist\extension.js`
- Extension source (upstream): `src/header.ts` (`genericTemplate`, `extractHeader`)
- User settings: `%AppData%\Roaming\Cursor\User\settings.json` (`42header.*` only — no width knob)
- Prior research: `sessions/2026.09.14/02-research/research-brief.md`
- Prior impl: `sessions/2026.09.14/04-implementation/log.md`
