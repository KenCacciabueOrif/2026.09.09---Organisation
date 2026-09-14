# Research brief

**Goal:** Fix broken 42 `By:` header under long official email without patching `kube` source or faking a short email — Continuity = **fork/extension switch**, verify on `ft_prework` fixture.  
**Publish:** Q8=A — **no** dual push/pull preflight as primary AC (skipped below as N/A).

## Recommended approach

**Primary:** Switch Cursor from `kube.42header` → **`secondfry.42header-long`**, keep existing `42header.username` / `42header.email`, disable/uninstall stock kube, regenerate fixture header, assert full email + closing `>`.

**Fallback if Marketplace/`secondfry` unavailable in Cursor:** Install **`ensui-dev.42header-multicampus`** (Open VSX + Marketplace; AUTHOR width 43; actively updated 2026-05). Same settings keys; do not rely on campus dropdown if email setting already set.

**Do not:** invent kube source patch locus; shorten official mail; ROADMAP/WorkSpace moves; edit exercise body beyond header regenerate.

## Options considered (max 3)

1. **`secondfry.42header-long` (recommended)**  
   - **Pros:** Built for this exact issue (#18 publisher link); AUTHOR width **42** fits this 41-char `login <email>`; same settings/commands as kube; largest long-header install base among forks.  
   - **Cons:** Last Marketplace update **2021-01-11** (quiet); **not on Open VSX** — Cursor may need Marketplace/VSIX path; still must disable kube to avoid command/save conflicts.

2. **`ensui-dev.42header-multicampus`**  
   - **Pros:** Maintained **2026-05**; Open VSX present; measured AUTHOR **43** also keeps `>`; campus helpers; same `42header.*` settings.  
   - **Cons:** Low install count; README “identical to upstream” is misleading vs measured wider template — verify Norminette/80-col after insert; not the historically cited long-email fix name.

3. **Stay on kube + settings-only / short mail**  
   - **Pros:** Zero extension change.  
   - **Cons:** **Fails Continuity** — settings already correct; clip is hard-coded field width; short/fake mail is an explicit bad outcome.

*(Out of preferred set: `nopons.42next-header` — recent but non-classic header/Python 79-col look.)*

## Required facts

| Fact | Value |
| --- | --- |
| Root cause | Fixed-width AUTHOR token **39** + `pad`/`substr` truncation in `kube.42header` 0.42.9 |
| Settings | Correct: username `kcacciab`, email 30-char campus address in Cursor User `settings.json` |
| Fixture | `C:\Project\current\ft_prework\ex0\ft_first_exception.py` L6: clipped `…lausanne.c`, no `>` |
| Auth string length | `login <email>` = **41** → overflows 39, fits 42/43 |
| Install locus | `~\.cursor\extensions\kube.42header-0.42.9-universal\` |
| Command conflict | Forks share `42header.insertHeader` — disable kube |
| Upstream fix | Issue #18 open; PR #17 closed unmerged |

## Unknowns / blockers

| Item | Status |
| --- | --- |
| Agent can install Marketplace extension without user UI | **Unknown / likely needs user** — plan user install + agent verify |
| Cursor Open VSX vs Marketplace for `secondfry` | **Risk** — not on Open VSX; may need VSIX/Marketplace |
| Norminette available on this machine | **Unknown** — AC allows visual/structural 80-col check if absent |
| Whether ensui output passes school Norminette for all languages | **Spot-check after install** |
| Dual extension already enabled | Currently only kube present — good |

**Blockers for this research phase:** none that stop planning. Soft risk: user-mediated install of fork.

### Push/auth dual preflight

**Skipped (N/A)** — goal is local extension swap + fixture header verify; Q8=A no agent publish. Org-repo session docs only incidental.

| Field | Value |
| --- | --- |
| Remote URL scheme | n/a |
| Tracking branch | n/a |
| Agent git / GCM / push readiness | n/a (not a publish AC) |
| `blocker_type` | none (for publish) |

### Dirty / pull preflight

**Skipped (N/A)** — not a sync cycle.

## Risks

- Leaving `kube.42header` enabled alongside a fork → conflicting save updates / truncated headers return.
- Choosing a visually different header extension (`nopons`) → Norminette / school checker mismatch.
- Regenerating fixture updates Created/Updated timestamps — acceptable for AC; do not churn Python body.
- Privacy: avoid committing unredacted email dumps beyond existing fixture if publishing session notes.

## Canonical references

- Local buggy template: `~\.cursor\extensions\kube.42header-0.42.9-universal\out\src\header.js`
- Fixture: `C:\Project\current\ft_prework\ex0\ft_first_exception.py`
- Issue #18: https://github.com/kube/vscode-42header/issues/18
- Fork (primary): https://marketplace.visualstudio.com/items?itemName=secondfry.42header-long
- Fork (fallback): https://marketplace.visualstudio.com/items?itemName=ensui-dev.42header-multicampus  
  Open VSX: https://open-vsx.org/extension/ensui-dev/42header-multicampus
- Upstream source: https://github.com/kube/vscode-42header

## Suggested implementer verification checklist

1. Disable/uninstall `kube.42header`.
2. Install `secondfry.42header-long` (or ensui fallback).
3. Confirm settings still have official long email (unchanged).
4. On fixture file: Insert 42 header / save → `By:` contains full `…42lausanne.ch>` and line stays 80 cols.
5. Optional: short-mail spot-check or reasoned pad demo (already done in research).
6. Document before/after `By:` lines (redact email in session prose if desired; fixture path OK).
