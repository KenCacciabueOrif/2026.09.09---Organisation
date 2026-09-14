# Prompt betterment notes

**Status:** `complete` — answers locked; full `refined-prompt.md` ready for researcher/planner.

**Program:** n/a — ad-hoc product/UI bug. Do **not** lock Multi-experiment / WorkSpace / ROADMAP Continuity.

**Consent UX:** Prior questions included plain-language + pros/cons. User reply was letter-style + free text; no re-ask needed. Jargon used below defined in one line where needed.

**Ask summary (durable one-liners):**
1. Q1 — Which 42 extension product?
2. Q2 — Where may we change things (source vs settings/fork)?
3. Q3 — What does buggy look like?
4. Q4 — Official mail length / test email?
5. Q5 — Preferred fix strategy?
6. Q6 — Definition of done / verification?
7. Q7 — Good vs bad outcome guardrails?
8. Q8 — Git publish this cycle?
9. Q9 — Are ft_prework files related?

## Answers

| Q | Lock | Source | Rationale |
| --- | --- | --- | --- |
| **Q1** | **A** — Cursor/VS Code **`kube.42header`** (installed; user says settings already correct) | `user reply` | Raw: “the extention is installed with correct settings and is : kube.42header”. Also leading **A.** |
| **Q2** | **B** — Installed-extension path: prefer **switch to a maintained long-email fork** (or equivalent non–source-patch). **No** inventing a patch locus for upstream `kube.42header` this cycle. Research may *look* under `C:\Project` for forks only for verification/docs — not as authorized edit root unless user later names one. | `user reply` | Raw leading **B.** + interpretation. Settings already correct → pure settings-tweak is **insufficient**; do not “fix” by shortening/changing official mail in settings. |
| **Q3** | **A** — Truncated `By:` line / missing closing `>` (field-width overflow) | `Choose (unanswered→default)` → **E→A** | Confirmed by fixture: `ft_prework/ex0/ft_first_exception.py` line 6 shows email clipped mid-domain and no closing `>`. |
| **Q4** | Synthetic / fixture-length: use the **fixture’s intended full address length** (≥ truncated form; community ≥35 chars as floor). Redact in session docs when quoting; fixture file already holds the example. | `Choose (unanswered→default)` → **C**, refined by fixture | Unanswered; default ≥35; fixture implies `…@student.42lausanne.ch`-class length. |
| **Q5** | **B** — Switch to / recommend a **maintained fork** that supports long emails (e.g. community long-header forks). **Not** settings-only (**C** blocked: settings already correct + official long mail must remain). **Not** patching `kube` upstream source (**A**) unless user later authorizes a writable path. | `Choose (unanswered→default)` adjusted | Naive Q5-D preferred patch-if-writable; **overridden** by locked Q2=B + “correct settings still buggy”. Documented reading differs from plain Q5-D on purpose. |
| **Q6** | **A** — After fix path: insert/update header with long official mail → full email + closing `>` present; short mails unchanged if tested; Norminette/80-col OK when available. Verify against regenerating or comparing to the ft_prework fixture. | `Choose (unanswered→default)` → **D→A** | Editor-header product. |
| **Q7** | Accept proposed good/bad (see Continuity) | `Choose (unanswered→default)` → **C** | Unanswered. |
| **Q8** | **A** — Local / document only; **no** agent push required this cycle | `Choose (unanswered→default)` → **C→A** | Unanswered; not a publish-cycle goal. |
| **Q9** | **B** — Related as **symptom evidence / acceptance fixture only** | `user reply` | Raw: “ft_prework contain the folder with a file with an exemple of the bad header”. **Do not** treat Python exercise logic as the product under fix; **do not** “fix” by rewriting exercise code beyond header regeneration if/when verifying. |

**Raw reply (preserved):**
```
A. B. ft_prework contain the folder with a file with an exemple of the bad header

the extention is installed with correct settings and is :
kube.42header
```

**Reading note:** Orchestrator interpretation matches this lock (Q1=A, Q2=B, Q9=B). No conflict.

## Continuity (locked — do not re-ask)

- Not a ROADMAP / Multi-experiment / WorkSpace cycle.
- Product: **`kube.42header`** (buggy with long official mail despite correct settings).
- Delivery path: **fork/extension switch** (or documented equivalent), not upstream source patch, not settings that drop/shorten official mail.
- Fixture: `C:\Project\current\ft_prework\ex0\ft_first_exception.py` (bad `By:` line) — evidence/AC only.
- Publish: local/document only (Q8=A).
- Good: long official mail → valid 42 header; minimal change; verify with fixture/re-insert.
- Bad: editing exercise logic; inventing kube source patch locus; fake short email settings; org ROADMAP/WorkSpace work; force-push; secrets in logs.

## Assumptions

- Spelling: extension.
- Root cause class: fixed-width email field in header template (hypothesis for researcher to confirm against `kube.42header` + known issues/forks).
- User wants official long mail preserved in the header (settings already “correct”).

## Open risks

- Marketplace fork quality / Norminette compatibility — researcher must pick a credible maintained fork and verify.
- Disabling `kube.42header` vs side-by-side — planner should avoid dual-extension fights.
- Regenerating header in fixture may rewrite timestamps — acceptable for verify; don’t churn exercise body.
- Agent cannot always install Marketplace extensions without user UI — plan may include clear user install steps + agent verification after.

## Self-improvement backlog

- None for consent (explanations were present pre-reply).

## Key alignment changes (raw → refined)

- Raw “fix 42 extension header / mail too long” → lock **`kube.42header`** + **fork-switch path** (settings already OK) + **ft_prework header fixture** as DoD evidence.
- Out of scope: patching kube upstream without new authorization; treating prework Python as the product; ROADMAP Continuity.
