# Taxonomy proposal — dated project labels

**Status:** **proposed-ratified — ready for user sign-off** (Cycle 1).  
**Not** final user ratification — do not treat as signed off until the user explicitly approves.  
**Early/simple layout:** **user-validated for Early/simple (2026.09.09)** — Cycle 2 applied `archive` / `paused` dated paths for the subset of 3 only (not global “final forever” corpus ratification).  
**Canonical form:** `yyyy.mm.dd - ShortName`

## Canonical format

```
yyyy.mm.dd - ShortName
```

- Date: zero-padded year.month.day with **dots** (same as FAW sessions).
- Separator: **space-hyphen-space** (` - `) between date and name.
- Live example already in the corpus: `2026.09.09 - Organisation`.

Do **not** encode status (`active` / `archive`) inside the date string. Status is a **separate axis** for later physical layout.

## Decided (Cycle 1)

| Rule | Locked decision |
| --- | --- |
| Status axis | `active` / `paused` / `archive`, plus INDEX specials `protect` / `hygiene`. **Not** PARA-lite (PARA-lite deferred/rejected for this program). |
| ShortName | **Keep spaces** — form `yyyy.mm.dd - ShortName`. Do not silently convert to GitHub-style hyphens. |
| Date source for proposed labels | **CreationTime wins** over earliest commit and LastWrite. User memory may override later if explicitly stated. |
| LastWrite | **Activity / “next” signal only** — not the folder’s date prefix. |
| Wrapper vs nested git | When the top-level folder is a thin wrapper around nested `.git` tree(s), the **canonical dated label applies to the wrapper** (the top-level move unit). Nested git roots are **child atomic units** inside that wrapper (never split without an explicit later plan). |
| Unit of labelling | One label per top-level wrapper / move unit; nested repos stay documented as children. |

## Status axis (separate from date)

Buckets for *later* physical layout under `C:\Project`:

- `active`
- `paused`
- `archive`

INDEX specials (not PARA status):

- `protect` — default-protect / must-preserve handling
- `hygiene` — root orphans / cleanup candidates

Status is **not** part of the `yyyy.mm.dd - ShortName` string. Layout sketch (partially applied in Cycle 2 for Early/simple subset):

```
C:\Project\
  active\
    2025.06.05 - Simpl\          # illustrative — not applied
  archive\
    2025.10.01 - PostManResponses\   # applied Cycle 2
    2025.06.23 - PlayTestTristan\    # applied Cycle 2
  paused\
    2026.06.30 - ZedTest\            # applied Cycle 2
```

## Good examples

| Label | Why |
| --- | --- |
| `2026.09.09 - Organisation` | Already matches canonical form; org host. |
| `2025.06.05 - Simpl` | Illustrative rename from CreationTime of `Simpl` — **label only; do not rename now**. |
| `2025.11.07 - WebCatalogue` | Illustrative; top-level git project with clear start signal. |

## Still open / classify before move

Do **not** silently decide these before a move-capable cycle. They do **not** re-open locked Cycle 0/1 decisions above.

| Topic | Open question |
| --- | --- |
| Empty parent git | `HTTP Battles`: empty parent `.git` vs real nested `http-battles` — classify keep/label before move (default wrapper label still applies to the top folder until classified). |
| Multi-repo containers | Keep `ProjetOrif` (etc.) as one dated unit vs split into multiple dated projects? Wrapper remains the top-level move unit until an explicit keep-vs-split plan. |
| Zip sidecars | Keep `.zip` beside extracts forever vs archive policy? |
| Root orphans | Do `package.json` / Docker / root `node_modules` get a dated project label or stay `hygiene`? |
| Deeper-than-2 git | Roots beyond scan depth 2 — re-scan the target folder before its move cycle. |

## Non-actions

- No filesystem renames under `C:\Project` in Cycle 0 or Cycle 1.
- Cycle 2 applied only the approved Early/simple subset of 3; other INDEX rows may still show **proposed** labels until their move cycle.
- Must-preserve remains **draft — not auto-locked**.
