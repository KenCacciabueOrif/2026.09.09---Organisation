# Refined prompt

## Goal

Make the **42 school header** on Python files **pass flake8 line-length checks** while keeping the **already-correct** long email and `>` from the prior cycle. The header content is right; it is **one character too wide** for flake8 (classic **80**-column frame vs flake8/PEP8 default **79** → likely **E501**). Prefer fixing the **header generator / extension settings** so newly inserted headers fit, then prove on the fixture file.

## Constraints

- **Mutation class:** `product_settings` — Cursor/VS Code extension and/or settings for `ensui-dev.42header-multicampus`, plus local fixture update for verification. Not ROADMAP / corpus `fs_mutation`.
- **Keep** extension **`ensui-dev.42header-multicampus`** (do not revert to kube.42header).
- **Do not** truncate or shorten the email / login fields that prior cycle fixed; only reduce overall line width (padding / frame) so lines are ≤ target max.
- **Do not** treat `# noqa: E501`, global `ignore = E501`, or raising `max-line-length` to 80+ as the primary fix (escape hatch only if research proves the extension cannot emit ≤79).
- **Target max:** **79** characters per line unless research finds a project flake8 config under `ft_prework` (or parents) that sets another limit — then match that config.
- **Git / publish:** **local only** — no org-repo publish/push required for this goal. Do not commit sibling trees (`ft_prework`, etc.) into the organisation repo.
- **Windows:** if any agent git is used for FAW session docs only, prefer Git for Windows + GCM when needed; product proof is `flake8`, not push.
- Smallest change that satisfies AC; no unrelated refactors.

## Context pointers

- Fixture (AC target): `C:\Project\current\ft_prework\ex0\ft_first_exception.py` — header lines currently **80** chars each; email already correct.
- Prior completed session Continuity: `sessions/2026.09.14/` (long-email truncate → ensui multicampus).
- This session: `sessions/2026.09.14-1004/`
- Domain facts for research (not to re-debate): flake8 default `max-line-length=79`; E501 on physical lines including `#` comments.
- Extension id Continuity: `ensui-dev.42header-multicampus`

## Acceptance criteria

- [ ] Researcher confirms failure mode (flake8 E501 or equivalent) on the fixture **or** documents an equivalent line-length rule from project config; notes measured lengths before/after.
- [ ] After the fix, **every line** of the 42 header in the fixture is **≤** the effective max (default **79**, or project config if present).
- [ ] Fixture still shows the **full** student email and `>` (no regression to truncated long-email behavior).
- [ ] Primary fix is via **ensui extension and/or editor settings** (and regenerating/updating the fixture header), not ignore-first.
- [ ] Verification: run `flake8` on `C:\Project\current\ft_prework\ex0\ft_first_exception.py` (or `python -m flake8 …`) with the same effective config students would use; **no E501** on header lines (other pre-existing non-header issues may be noted but are out of scope unless introduced by this change).
- [ ] Implementation / plan documents what setting or generator change was made so the fix is repeatable for new files.
- [ ] No ROADMAP / WorkSpace / corpus moves; no force-publish of org-repo.

## Out of scope

- Reopening prior long-email / kube→ensui migration design
- ROADMAP, WorkSpace, Multi-experiment, corpus archive/moves
- Disabling flake8 E501 project-wide as the intended solution
- Norminette / non-flake8 checkers unless they block the same fixture and research surfaces them
- Publishing/pushing the organisation repo or any `ft_prework` remote
- Unrelated prework exercise logic below the header
