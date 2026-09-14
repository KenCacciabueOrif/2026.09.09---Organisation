# Refined prompt

## Goal

Stop the **42 file header** produced by the installed Cursor/VS Code extension **`kube.42header`** from breaking when the user’s **official long email** is used. Settings are already correct and the bug remains — deliver a **working header** (full email + closing `>`) via a **non–source-patch** path: prefer **switching to a maintained long-email-capable fork** (or equivalent documented extension fix), then verify against the bad-header example under `ft_prework`.

## Constraints

- **Product:** `kube.42header` only (not Intra browser UI, not org ROADMAP/WorkSpace).
- **Authorized change class:** Q2=B — **no invented patch locus** for upstream `kube` source this cycle. Do **not** “fix” by changing settings to a short/fake email; official long mail must stay the intended identity.
- **Fixture vs product:** `C:\Project\current\ft_prework` holds an **example of the bad header** for symptom/AC. Treat as evidence and verification target for the **header lines only** — not as the extension to edit; do not refactor exercise Python/PDF subject work.
- **Publish:** Local / document only — no agent `git push` required (Q8=A). Session artifacts may still follow FAW allowlist norms in the org repo; do not require publishing an extension repo.
- **Privacy:** Prefer redacting full email in session docs when quoting; fixture path is enough for pointer.
- **Minimal scope:** Smallest durable fix path; no force-push; no secrets in commits/logs.

## Context pointers (known only)

- Extension ID: `kube.42header` (installed; user: correct settings, still buggy).
- Bad-header fixture (observe `By:` truncation / missing `>`):  
  `C:\Project\current\ft_prework\ex0\ft_first_exception.py`  
  Example symptom (line 6): email clipped mid-domain (`…42lausanne.c`) and closing `>` absent before padding.
- Workspace: organisation FAW session under `sessions/2026.09.14/`; broader tree `C:\Project` may be searched **read-only** for forks/docs — not an authorized edit root for kube upstream.
- Community precedent (for researcher, not locked solution): long-email clipping issues/forks around 42 Header (e.g. long-header Marketplace forks) — confirm current maintained options before recommending.

## Acceptance criteria / verification

1. **Root cause framed:** Document why `kube.42header` with a long official mail produces a broken `By:` line (field width / padding), citing the fixture and extension behavior — without claiming a source patch was applied unless authorized later.
2. **Fix path delivered:** A concrete, actionable remediation that does **not** rely on incorrect settings or shortening official mail — **preferred:** install/enable a **maintained fork** known to support long emails, and disable or avoid conflict with stock `kube.42header` as needed. Document extension ID + settings to keep (`username` / official `email`).
3. **Header correctness with long mail:** After the fix path, inserting or updating a 42 header with the official long email yields:
   - Full email text present
   - Closing `>` present on the `By:` line
   - Header structure remains Norminette-/80-col-compatible when a checker is available (or visually/structurally valid if Norminette is unavailable — note which).
4. **Fixture check:** Reconcile with `ft_prework/ex0/ft_first_exception.py` — either regenerate header under the fixed extension and show the `By:` line is corrected, or produce a before/after comparison proving the same long mail no longer truncates. Do **not** change exercise logic below the header unless required for a clean regenerate.
5. **No regression expectation:** Document that shorter emails still produce valid headers (spot-check or reasoned from fork behavior).
6. **Out-of-scope untouched:** No ROADMAP/WorkSpace Continuity work; no unauthorized kube source tree edits; no publish/push of an extension unless user later opts in.

## Out of scope

- Corpus organisation / Multi-experiment / WorkSpace / Appendix A
- Patching `kube/vscode-42header` upstream source without a new user-authorized writable path
- Settings workarounds that replace official long mail with a short fake address
- Rewriting `ft_prework` exercise implementations or the subject PDF
- Browser Intra extensions
- Agent-mandated git push of product code

## Mutation class (intent)

- **`code_change (product)` / environment:** primary delivery is **editor extension swap + header verification** (and optional header regenerate on the fixture file). Not `fs_mutation` corpus moves; not docs-only if a fixture header regenerate is included — planner may split “docs+user install steps” vs “touch fixture header” explicitly.
