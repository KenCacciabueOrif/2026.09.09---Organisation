# Prompt betterment notes

## Status

- **Phase status:** `complete` (Choose / Continuity locks — no wait on user)
- **Raw reply used as intent:** “the new header is right but one character too long … flake8 — Fix it”
- **Consent UX:** ask summaries below include plain-language + pros/cons as if disclosed; defaults locked via `Choose (unanswered→default)` / Continuity because user already stated clear fix intent and orchestrator authorized quick defaults.

## Clarifying questions (ask summary + locked choice)

### Q1 — Failure mode
**Ask (1-line):** Is the problem flake8 E501 because header lines are 80 chars vs default max 79?
**Plain language:** Flake8 (a Python style checker) flags lines longer than its limit. Classic 42 headers are often drawn at 80 characters; flake8’s usual limit is 79, so every header line can fail even when the email/text looks correct.
- **A — Treat as E501 / 80→79 (default):** Assume that mismatch and verify with `flake8` on the fixture.  
  - Pros: Matches Continuity measurement + “one character too long”; fast.  
  - Cons: If a custom config uses a different max, we might over-narrow.
- **B — Wait for pasted flake8 output:** Confirm code/path before changing anything.  
  - Pros: Certainty. Cons: Delays an already-strong diagnosis.
**Locked:** **A** — Source: `Choose (unanswered→default)` + Continuity (measured 80-col header; flake8 default 79). Rationale: user said fix for flake8; line lengths on fixture are all 80.

### Q2 — Target max length
**Ask (1-line):** Cap header lines at 79 (flake8/PEP8 default), or follow a project `.flake8` / `setup.cfg` if present?
**Plain language:** “79” is the usual school/default flake8 limit. Some projects raise it (e.g. 88/99). We should match whatever you actually lint with.
- **A — ≤79 unless project config says otherwise (default):** Researcher checks `ft_prework` (and parents) for flake8 config; if none, use 79.  
  - Pros: Honest under default flake8. Cons: Slightly tighter than classic 80-col 42 art.
- **B — Keep 80 and raise flake8 max / ignore E501:** Change the linter, not the header.  
  - Pros: Preserves classic width. Cons: Hides long lines elsewhere; does not match “header … too long.”
**Locked:** **A** — Source: `Choose (unanswered→default)`. Rationale: “one character too long” implies shrink header, not relax lint.

### Q3 — Fix locus
**Ask (1-line):** Shorten via the 42-header extension/settings, or only add flake8 ignore/`# noqa` on headers?
**Plain language:** We can either teach the header tool to emit lines that fit flake8, or tell flake8 to stop complaining about long lines.
- **A — Prefer regenerate/shorter header via ensui extension / settings (default); update fixture to prove:** Real fix at the source.  
  - Pros: New files stay clean; matches “header … too long.” Cons: May need extension/settings research.
- **B — flake8 ignore / per-file-ignores / `# noqa: E501` only:** Silence lint.  
  - Pros: Quick. Cons: Does not fix the header; pollutes student workflow if applied broadly.
- **C — Both:** Shorten generator and add ignore as belt-and-suspenders.  
  - Pros: Extra safety. Cons: Unnecessary if A works; masks regressions.
**Locked:** **A** — Source: `Choose (unanswered→default)`. Rationale: user framed the header as the defect, not the linter policy.

### Q4 — Keep ensui multicampus extension?
**Ask (1-line):** Stay on `ensui-dev.42header-multicampus` (prior cycle), or switch again?
**Plain language:** Prior session already moved away from the long-email-truncating kube header to ensui multicampus so the full email + `>` fit.
- **A — Keep ensui (default).** Pros: Preserves long-email fix. Cons: Fix must be possible inside that extension’s width model.
- **B — Switch / add another extension.** Pros: Escape hatch. Cons: Reopens prior cycle risk; out of scope unless A fails.
**Locked:** **A** — Source: Continuity + `Choose (unanswered→default)`.

### Q5 — Fixture still the acceptance target?
**Ask (1-line):** Must `C:\Project\current\ft_prework\ex0\ft_first_exception.py` pass flake8 header-line checks after the fix?
**Plain language:** That sample file is how we proved the last header fix; using it again keeps the done check concrete.
- **A — Yes, regenerate/adjust that fixture and run flake8 on it (default).** Pros: Clear AC. Cons: Touches a non-org path (expected for product_settings).
- **B — Settings-only; fixture optional.** Pros: Less file churn. Cons: Weaker proof.
**Locked:** **A** — Source: Continuity + `Choose (unanswered→default)`.

### Q6 — Publish / org-repo git?
**Ask (1-line):** Publish this org-repo session to origin, or keep git local-only for this product fix?
**Plain language:** FAW may still log the session in the organisation repo. “Publish” means agent commit/push of allowlisted session/meta — not pushing `ft_prework`.
- **A — Local only; no publish pack / no agent push required (default for this goal).** Pros: Matches ad-hoc product fix; avoids Windows GCM push friction. Cons: Session artifacts stay local until a later publish cycle.
- **B — Full publish-cycle pack (stage/commit/push org-repo).** Pros: Remote backup of FAW docs. Cons: Extra gates; not requested.
**Locked:** **A** — Source: `Choose (unanswered→default)` (orchestrator: Publish Q8 default local). No publish-cycle Q1–Q8 locks beyond “local only.”

## Answers (concrete)

| Q | Lock | Source | Rationale |
| --- | --- | --- | --- |
| Q1 Failure mode | E501 / 80 vs 79 | Choose (unanswered→default) + Continuity | Fixture lines measured 80; flake8 default 79 |
| Q2 Max length | ≤79 unless project flake8 config higher | Choose (unanswered→default) | Shrink header, don’t relax lint |
| Q3 Locus | Extension/settings + fixture proof; no ignore-first | Choose (unanswered→default) | “Header … too long” |
| Q4 Extension | Keep `ensui-dev.42header-multicampus` | Continuity | Prior cycle long-email fix |
| Q5 Fixture AC | Yes — `ft_first_exception.py` | Continuity | Same proof path |
| Q6 Publish | Local only | Choose (unanswered→default) | Ad-hoc product fix; Q8 local |

## Continuity (locked — do not re-ask)

- Prior session `sessions/2026.09.14/` **complete** — do **not** reopen long-email truncate work.
- Product: **`ensui-dev.42header-multicampus`** (not kube.42header).
- Fixture: `C:\Project\current\ft_prework\ex0\ft_first_exception.py` — full email + `>` already correct; width problem only.
- Not ROADMAP / WorkSpace / corpus FS.
- Mutation class intent: **`product_settings`** (editor extension/settings + local fixture verification). Not `fs_mutation` corpus; org-repo session docs may still be written by FAW.

## Assumptions

- Default flake8/`pycodestyle` `max-line-length=79` applies unless research finds project override in `ft_prework` tree.
- “One character too long” means reduce **frame width** (or equivalent padding) so all `# … #` header lines are ≤ target — without truncating the email again.
- Regenerating the header after settings change is an acceptable way to update the fixture.

## Open risks

- ensui extension may hardcode 80-col art; fix might need fork, settings knob, or alternate padding strategy — researcher must confirm.
- If school checkers use 80 or Norminette-style rules instead of flake8 79, shrinking could diverge from another tool (out of scope unless discovered).
- Touching VS Code/Cursor user settings is machine-local; document what changed for audit.

## Self-improvement backlog

- None this phase (questions explained in notes; defaults locked without forcing user to re-answer Continuity).

## Key alignment changes (raw → refined)

- Raw “fix it” → concrete AC: header lines ≤ flake8 limit (default 79); fixture passes `flake8` on those lines; keep ensui; no E501-ignore-first; no ROADMAP; local git only.
- Explicit non-goal: redoing long-email truncation; whole-project E501 disable; org publish.
