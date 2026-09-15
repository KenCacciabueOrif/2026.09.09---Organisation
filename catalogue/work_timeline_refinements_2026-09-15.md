# Organisation Dashboard (`work_timeline.html`) — Refinement Plan

> **Status 2026-09-15: Runs 1 & 2 implemented and verified** (Node syntax check + runtime smoke test).
> Run 1: commit-log pagination + month grouping, calendar heatmap (Activity), quick-actions (folder/remote links), sort indicators + `aria-sort`, keyboard access (family tree rows, calendar squares, Enter/Space), drawer dialog semantics + focus restore, KPI trend context + last-14-days strip, granularity switch fixed (was inert inside `<style>`) + persisted to URL/localStorage, O(1) repo index.
> Run 2: shared styled tooltip (replaces native `title`), compact-density toggle (persisted), init error-guard (fatal panel on JSON parse failure + script-error banner in DQ strip), Clear-filters buttons + empty-state reset link, `aria-live` result counts, `th` contrast `--text-3`→`--text-2`.
> Known remaining: ~~292 duplicate commits originate in the **generator**~~ **FIXED Run 3 (2026-09-15, session 2026.09.15-1320)**: generator dedupes by commit hash (`--all` ref double-counting was the root cause); commits carry `path`; dashboard dedupe/DQ keyed by path (same-named repo copies like `template_frontback`×4 no longer collide); DQ relabels same-day same-subject re-commits as informational (verified distinct hashes). Verified: 3490 commits, dqDuplicateEntries=0, Node runtime smoke pass. Global `/` search **done Run 3**: header input, `/` focuses, Enter routes to Projects (project-name/path match) or Commit log with query pre-filled. Remaining: data-split-to-JSON not yet done.

Audit date: 2026-09-15 · Source: full read of `catalogue/work_timeline.html` (479 lines) + external research (UXPin dashboard principles 2026, UX Pilot / NNGroup eye-tracking patterns, Pencil & Paper data-table UX, Microsoft/Esri dashboard accessibility guides).

---

## A. What it already does well (keep)
- Dark-first palette with documented WCAG contrast ratios per token.
- Data-quality strip (`⚠ data is Nd old / ✓ data valid`) — genuinely rare, keep and extend.
- Deep-linking: tab + filters synced to URL (`?f-status=…#commits`).
- Duplicate-commit suppression + in-view dedupe with counts surfaced.
- Progressive disclosure: focus view family tree, detail drawer.

## B. Information architecture & hierarchy
1. **F-pattern placement is inverted.** NNGroup/Tableau eye-tracking: KPIs top → trends middle → detail tables bottom. Current Overview does this, but the **data-quality strip sits above the tabs** and competes with the H1. Move it to a slim status bar (or a dismissible chip next to the tab row) so the first scan lands on KPIs.
2. **KPI cards lack context.** Research is unanimous: a KPI without trend/comparison is a vanity number. Add to each card: sparkline or `+N vs prev period`, e.g. "own commits 25 · ▲ vs last month". Peak month KPI should show relative %.
3. **Five tabs is fine (Hick's law), but Overview vs Activity overlap** — both render the same `renderSpark()` chart. Differentiate: Overview = monthly trend + KPIs; Activity = weekday×hour heatmap + repo breakdown (currently just a text list "Top repos"). A real GitHub-style calendar heatmap is the single highest-value chart missing.
4. **No landing narrative.** The 5-second test: a new viewer can't tell *what changed recently*. Add a "Since you last opened" or "Last 14 days" strip: repos touched, commits, biggest project movement.

## C. Tables & data UX (biggest gap cluster)
5. **No pagination/virtualization on the commit log** — hard cap `slice(-500)` with no way to see older commits. Add "load more" paging or a date-range filter; also paginate the projects table when rows > ~50.
6. **Sortable headers have zero affordance**: `th[data-s]` clicks work but there's no ▲/▼ indicator, no `aria-sort`, no cursor:pointer. Add sort-direction glyphs + `aria-sort` attributes.
7. **Row actions missing**: project rows open a drawer, but there's no quick action (copy path, open in editor/explorer, open remote URL). Add per-row icon buttons — the repo `path` and `remotes` are already in the data.
8. **Commit log lacks grouping**: 500 rows of same-repo noise. Group by date ("Today", "Sep 12") with sticky date headers; collapse multi-commit bursts per repo.
9. **Filter bar feedback**: when filters hide everything, the empty state ("No projects match") offers no reset. Add a "Clear filters" action + `aria-live` count announcements.
10. **Search is substring-only per field.** Add a single global search (projects + commits + languages) with `/` keyboard shortcut — research pattern for dense dashboards.

## D. Interaction & state
11. **Focus view rows aren't keyboard accessible**: `onclick` on `div.prow-h` / `div.kid` only. Convert to `role="button"` `tabindex="0"` + Enter/Space, or real `<button>`s. Same for the spark bars (currently hover-tooltip only — invisible to keyboard/screen readers).
12. **Detail drawer traps nothing and announces nothing**: give `role="dialog" aria-modal="false"`, move focus to the close button on open, restore focus on close, support `Tab` cycling. Escape works already (good).
13. **Granularity switch + tabs don't persist** granularity (`curG`) in the URL while tabs/filters do — inconsistent. Persist it.
14. **No loading/empty/error state for the data payload.** If the embedded JSON fails to parse, the page silently renders nothing. Wrap init in try/catch with a visible error panel (extends your existing DQ philosophy to the script itself).
15. **Tooltips are native `title` only** — no multi-line formatting control, delayed, unstyled. Replace with a shared positioned tooltip div (also fixes keyboard reachability, item 11).

## E. Visual design
16. **Typography scale too flat**: h1 22px, everything else 12–14px. Introduce a 4-step scale (22/16/13.5/11.5) and increase KPI number size to ~28px — primary metrics should dominate (UXPin "visual emphasis" principle).
17. **Color semantics drift**: status pills use green/blue/orange/purple/gray, but the chart legend reuses them while bars are all indigo. Reserve accent color for interactive/primary; keep the 5 status hues exclusively for status.
18. **Density toggle**: you run minimap/dense everywhere — add a "compact/comfortable" density toggle (row padding 5px vs 9px) persisted to localStorage.
19. **Spark bar hover** highlights with teal box-shadow, but teal means nothing in the system — use `--accent` brightening instead, and show a vertical crosshair + value label for the hovered bucket.

## F. Performance & robustness
20. **594 KB single file** with the JSON blob inline. Fine for local use; if it grows, split data to `work_timeline_data.json` fetched at load (keeps HTML cacheable), with the DQ strip reporting fetch age.
21. **`renderCommits` rebuilds all 500 rows per keystroke** on the search field. Debounce input (~150 ms) or build once + `filter`/`hidden` toggling on rows.
22. **`D.repos.indexOf(r)` in loops** — O(n²) map to index once. Trivial but free.
23. **Duplicate suppression happens client-side every load** ("fix generator" warning acknowledged in code) — fix the generator so dedupe is a validation assert, not a runtime patch.

## G. Accessibility checklist (from MS/Esri/WCAG guidance)
- [ ] `aria-sort` on sortable headers (item 6)
- [ ] Keyboard-operable rows, bars, family tree (item 11)
- [ ] Dialog semantics + focus management on drawer (item 12)
- [ ] `aria-live="polite"` on result counts and the DQ strip
- [ ] Prefer not-both red/green alone for status — the current dot+word pill pattern is good, keep the word always visible
- [ ] Contrast: `--text-3` (#6b7484, 3.6:1) is used for table headers and axis labels — decorative ok, but bump header labels to `--text-2` (6.1:1)

## H. Suggested priority order
| # | Item | Effort | Impact |
|---|------|--------|--------|
| 1 | Commit-log pagination + date grouping (5, 8) | M | High |
| 2 | Real activity heatmap (3) | M | High |
| 3 | Row quick-actions: open path/remote (7) | S | High |
| 4 | Sort indicators + aria-sort (6) | S | Med |
| 5 | Keyboard access + dialog semantics (11, 12) | M | Med-High |
| 6 | KPI trend context (2) + "last 14 days" strip (4) | M | High |
| 7 | Global search with `/` (10) | M | Med |
| 8 | Shared tooltip + density toggle (15, 18) | M | Med |
| 9 | Performance: debounce, index map, data split (20–22) | S | Med |
| 10 | Visual polish: type scale, color discipline (16, 17, 19) | S | Med |

## Sources
- UXPin — *Dashboard Design Principles: The Definitive Guide (2026)*
- UX Pilot — *12 Dashboard Design Principles* (NNGroup F-pattern, Tableau eye-tracking, Hick's law)
- Pencil & Paper — *Dashboard Design UX Patterns* / Data Tables checklist
- Microsoft Learn — *Design Power BI reports for accessibility*; Esri — *Dashboard accessibility best practices*
