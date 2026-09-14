# Implementation log — 2026.09.14 (42header fork switch)

## Status

- **status:** complete (fallback fork used)
- **mutation_class:** `product_settings` (extension swap + fixture header regenerate)
- **blocker_type:** none
- **publish:** skipped (Q8=A)

## Root cause (AC1)

- Stock **`kube.42header` 0.42.9** uses fixed AUTHOR field width **39** with `pad`/`substr` truncation (`~\.cursor\extensions\kube.42header-0.42.9-universal\out\src\header.js`, read-only).
- Official identity: username `kcacciab`, email length **30** (`…@student.42lausanne.ch`); author string `login <email>` length **41** → overflows 39.
- **Before (fixture L6):** clipped mid-domain `…lausanne.c`, closing `>` absent before padding; line still 80-col but semantically broken.
- Settings were already correct — clip is hard-coded field width, not bad config.
- **No kube source patch applied.**

## Steps / commands

| Time (local) | Action | Result |
| --- | --- | --- |
| 2026-09-14 ~09:28 | Baseline: read fixture + settings + kube AUTHOR width | AUTHOR=39; author_len=41; email_len=30 unchanged |
| 2026-09-14 ~09:29 | `cursor --uninstall-extension kube.42header` | Success — kube removed from `--list-extensions` |
| 2026-09-14 ~09:29 | `cursor --install-extension secondfry.42header-long` | **Failed** — `Extension 'secondfry.42header-long' not found` (Cursor catalog / Open VSX 404; Marketplace-only ID) |
| 2026-09-14 ~09:30 | `cursor --install-extension ensui-dev.42header-multicampus` | **Success** — `ensui-dev.42header-multicampus` v**0.42.16** |
| 2026-09-14 ~09:30 | Confirm settings | `42header.username` / `42header.email` unchanged (email_len=30; not shortened) |
| 2026-09-14 ~09:33 | Regenerate fixture header from ensui template (AUTHOR width **43**) | By: full email + `>`; all 11 header lines len=80 |
| 2026-09-14 ~09:33 | Norminette | **Not installed** — used structural 80-col + substring checks |

### Extension IDs

| Role | ID | Outcome |
| --- | --- | --- |
| Before | `kube.42header` | Uninstalled via CLI |
| Primary attempt | `secondfry.42header-long` | Unavailable via Cursor CLI / Open VSX |
| Delivered | `ensui-dev.42header-multicampus` @ 0.42.16 | Installed + only 42header listed |

### Leftover note

- Folder `~\.cursor\extensions\kube.42header-0.42.9-universal\` may still exist on disk after uninstall; **not** listed as enabled. Safe to delete manually after Reload if desired. Do not re-enable.

## Settings attestation

- Keys kept: `42header.username`, `42header.email`
- Email **not** shortened; length remains 30 (campus long-form)
- Domain (redacted local-part): `…@student.42lausanne.ch`
- Probe: read `%AppData%\Roaming\Cursor\User\settings.json` (Shell)

## Fixture before / after (By:)

- **Path:** `C:\Project\current\ft_prework\ex0\ft_first_exception.py`
- **Before:** `By: kcacciab <…@student.42lausanne.c` — clipped; no `>`
- **After:** `By: kcacciab <…@student.42lausanne.ch>` — full mail + `>`; 80 cols
- **Body:** unchanged (header-only file; no exercise logic)
- **Timestamps:** Created preserved `2026/09/14 08:58:03`; Updated bumped on regenerate
- **Method:** Computed from installed ensui `dist/extension.js` template (AUTHOR=43) + User settings — equivalent to what `42header.insertHeader` would produce after Reload. Agent cannot invoke Cursor command palette from CLI.

## Verification

- [x] All header lines length 80
- [x] By: contains `@student.42lausanne.ch>`
- [x] By: contains closing `>`
- [x] Old clip pattern `lausanne.c` absent
- [x] Norminette: skipped (not on PATH) — structural method logged
- [x] Short-mail regression (reasoned): AUTHOR width 43 ≫ typical short strings (e.g. ~17); long author 41 fits 43, fails 39
- [x] Zero ROADMAP / WorkSpace / INDEX / Multi-experiment path mutations
- [x] No edits under kube extension source as fix path
- [x] No agent git push

## User-mediated / remaining steps

1. **Reload Cursor window** so `ensui-dev.42header-multicampus` fully activates (commands / save hooks).
2. Optional: Extensions UI → confirm only **42 Header Multi-Campus** enabled; kube absent.
3. Optional: delete leftover `kube.42header-0.42.9-universal` folder after reload.
4. Optional preference for primary fork: install **`secondfry.42header-long`** from VS Marketplace UI / VSIX (not on Open VSX) — then disable ensui to avoid dual providers. Not required; ensui satisfies AC.
5. Ongoing use: **Insert 42 Header** (`42header.insertHeader` / usual shortcut) on new files.

### If primary install desired later (user UI)

1. Open Extensions in Cursor.
2. Search Marketplace for `secondfry.42header-long` (or install VSIX from Marketplace page).
3. Disable/uninstall `ensui-dev.42header-multicampus`.
4. Reload; re-insert header to confirm.

## Rollback

1. `cursor --uninstall-extension ensui-dev.42header-multicampus`
2. `cursor --install-extension kube.42header`
3. Reload — long-email `By:` may clip again (expected).

## Deviations from plan

- Primary `secondfry.42header-long` unavailable via Cursor CLI → used planned **fallback** `ensui-dev.42header-multicampus`.
- Header regenerated from ensui template + settings (not live command-palette insert) — logged; structurally matches fork pad widths.
- Norminette unavailable → 80-col structural verify.
- kube extension folder may linger on disk after successful uninstall.

## Attestations

- Zero corpus / catalogue moves under `C:\Project`.
- No secrets / full unredacted email dumps in this log beyond fixture path pointer + domain.
- Q8=A: no product git push.
