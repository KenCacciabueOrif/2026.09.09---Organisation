# Plan

## Goal

Stop broken 42 `By:` headers under the user’s official long campus email by switching Cursor from stock **`kube.42header`** (fixed AUTHOR width 39 + truncate) to a maintained long-email-capable fork — **primary `secondfry.42header-long`**, **fallback `ensui-dev.42header-multicampus`** — keep existing `42header.username` / `42header.email`, disable/uninstall kube to avoid command conflicts, regenerate the header on the `ft_prework` fixture, and verify full email + closing `>` (80-col structure). No kube source patch, no fake-short email, no ROADMAP/WorkSpace work, no agent publish (Q8=A).

## Mutation class

| Field | Value |
| --- | --- |
| Class | **`product_settings`** (editor extension swap + fixture header regenerate) |
| Binary FAW label (if forced) | **Not `fs_mutation`** — do not invent corpus moves. Prefer `product_settings` over `docs_only` because product/env mutation occurs (extension + optional fixture header touch). |
| Mutation kind | Cursor extension disable/install + header re-insert on evidence fixture |
| Corpus FS | **Zero** intentional corpus / catalogue moves, renames, or deletes under `C:\Project` catalogue batches |
| Org-repo docs | Session logs under `sessions/2026.09.14/` (implementation notes); incidental FAW allowlist only |
| User approval before implementer | **Not required for ROADMAP/corpus plan-gate** (n/a). Soft: Marketplace install may need **user-mediated** UI if CLI cannot install — not a hard Continuity gate. |
| First-move / taxonomy / must-preserve | **N/A** — not a ROADMAP move cycle |

### Attestation (implementer)

- Confirm zero ROADMAP / WorkSpace / INDEX / Multi-experiment path mutations.
- Confirm no edits to kube extension source under `~\.cursor\extensions\kube.42header-*` as the delivery path.
- Confirm `42header.email` remains the official long address (not shortened).

## What the user is approving

**Corpus plan-gate: n/a** (orchestrator will **not** pause for ROADMAP batch approval).

Optional user action (soft): if agent cannot install from Marketplace/CLI, user installs the fork in Cursor Extensions UI and reloads — then agent continues verify + docs.

## Acceptance criteria

- [ ] **Root cause framed** in `04-implementation` (or log): kube AUTHOR width **39** + `pad`/`substr` truncates `login <email>` of length **41**; cite fixture L6 clip (`…lausanne.c`, missing `>`) and extension behavior — without claiming a kube source patch was applied.
- [ ] **Fix path delivered:** `kube.42header` disabled or uninstalled; **`secondfry.42header-long`** installed and enabled (or documented fallback **`ensui-dev.42header-multicampus`** if secondfry unavailable); settings keys kept: `42header.username`, `42header.email` (official long mail unchanged).
- [ ] **Header correctness:** After insert/update with official long mail, `By:` line contains **full email** and closing **`>`**; line remains structurally 80-col / Norminette-compatible when checker available, else note visual/structural check method.
- [ ] **Fixture check:** `C:\Project\current\ft_prework\ex0\ft_first_exception.py` header regenerated (or before/after comparison) showing corrected `By:`; **no** change to exercise Python body below the header unless required for clean regenerate.
- [ ] **No short-mail regression expectation:** Document that shorter emails still produce valid headers (spot-check **or** reasoned from wider AUTHOR field / research pad demo).
- [ ] **Out-of-scope untouched:** No ROADMAP/WorkSpace Continuity; no unauthorized kube upstream source edits; no agent `git push` of extension product; no force-push; no secrets/unredacted email dumps beyond fixture necessity in session prose.
- [ ] **Implementation log:** `sessions/2026.09.14/04-implementation/` records steps taken, extension IDs, before/after `By:` (redact in prose if desired), verify method, and any user-mediated install notes.

## Steps

1. **Baseline / root-cause note**  
   - **Paths:** fixture `C:\Project\current\ft_prework\ex0\ft_first_exception.py`; research brief; optional read of installed kube `header.js` AUTHOR width (read-only).  
   - **Action:** Capture before `By:` line (or reference research fixture evidence); write root-cause framing for AC1.  
   - **Verify:** Note documents width-39 truncate; settings already correct (`kcacciab` + long campus email).

2. **Disable / uninstall stock kube**  
   - **Paths:** Cursor Extensions UI and/or CLI (`cursor --uninstall-extension kube.42header` if available).  
   - **Action:** Disable or uninstall **`kube.42header`** so it cannot own `42header.insertHeader` / save hooks. Prefer uninstall if disable alone leaves conflicts.  
   - **Verify:** Only one 42-header provider remains after Step 3; no dual enabled.

3. **Install maintained fork**  
   - **Primary:** `secondfry.42header-long` (Marketplace; not on Open VSX — may need Marketplace/VSIX).  
   - **Fallback:** If primary unavailable in Cursor → `ensui-dev.42header-multicampus` (Marketplace and/or Open VSX).  
   - **Action:** Install via CLI if possible; **if CLI fails, stop and give user clear Marketplace install steps**, then resume after reload. Do not invent VSIX from untrusted sources without documenting source URL.  
   - **Verify:** Extension folder appears under `~\.cursor\extensions\` (or Cursor reports enabled); ID matches primary or fallback.

4. **Reload window**  
   - **Action:** Reload Cursor window so commands/bindings bind to the fork only.  
   - **Verify:** Command palette shows 42 Header insert from the fork; kube not active.

5. **Confirm settings unchanged**  
   - **Path:** `%AppData%\Roaming\Cursor\User\settings.json`  
   - **Action:** Confirm `42header.username` and `42header.email` still hold official identity (long email). **Do not** shorten or fake email.  
   - **Verify:** Email length remains campus long-form (research: 30-char mail; author string 41).

6. **Regenerate header on fixture**  
   - **Path:** `C:\Project\current\ft_prework\ex0\ft_first_exception.py`  
   - **Action:** Insert/update 42 header (Ctrl+Alt+H or save with header present) via the fork. Touch **header block only**; leave exercise body empty/as-is below header. Timestamps may update — acceptable.  
   - **Verify:** Open file; `By:` contains full `…@student.42lausanne.ch` **and** closing `>`; line length ~80.

7. **Structural / Norminette check**  
   - **Action:** If Norminette available, run on fixture; else measure/assert 80-col header lines visually/structurally and log method.  
   - **Verify:** AC3 satisfied; method named in log.

8. **Short-mail regression note**  
   - **Action:** Optional spot-check with a short address **in a throwaway buffer** (restore official email after) **or** reason from research (AUTHOR width 42/43 ≫ short strings). Prefer restore official email immediately if spot-check changes settings.  
   - **Verify:** AC5 documented.

9. **Document in 04-implementation**  
   - **Path:** `sessions/2026.09.14/04-implementation/` (log.md or equivalent).  
   - **Action:** Record root cause, extension IDs (before/after), install path (CLI vs user UI), settings attestation, before/after `By:` (redact in prose OK), verify checklist, fallback used if any, rollback pointer.  
   - **Verify:** All AC checkboxes addressable from the log + fixture state.

10. **Auth / publish preflight**  
    - **Skipped (N/A)** — Q8=A local/document only; no agent `git push`/`pull` AC for this cycle.

## Non-goals

- Corpus organisation, Multi-experiment, WorkSpace, Appendix A, ROADMAP moves
- Patching `kube/vscode-42header` upstream source or editing files under the kube extension install as the fix
- Settings workarounds that replace official long mail with a short/fake address
- Rewriting `ft_prework` exercise implementations or the subject PDF
- Browser Intra extensions; alternate header styles (e.g. `nopons.42next-header`) unless Continuity expands
- Agent-mandated git push of product/extension code; force-push; secrets in commits/logs

## Risks / rollback

| Risk | Mitigation / rollback |
| --- | --- |
| Marketplace install blocked for agent | Soft blocker: user installs fork in UI; agent resumes verify+docs. Prefer ensui Open VSX path if secondfry Marketplace path fails. |
| Dual extension still enabled | Always disable/uninstall kube before relying on fork; re-check Extensions list after reload. |
| Wrong fork / visual mismatch | Stick to secondfry primary or ensui fallback; avoid nopons unless Continuity changes. Spot-check Norminette/80-col after ensui. |
| Fixture timestamp churn | Expected on regenerate; do not churn Python body. |
| Privacy in session docs | Redact full email in prose; fixture path is enough pointer. |
| **Rollback** | Re-enable or reinstall `kube.42header`; disable/uninstall the fork; reload. Headers may clip again with long mail — expected. Fixture can be re-inserted with kube if needed for before-state demo only. |
| Force-push / publish | Forbidden this cycle (Q8=A). |
| Agent environment vs credentials | N/A for publish; classify any install failure as **user-mediated install** or **agent Marketplace access**, not `user_credentials` git. |

## Soft blocker (non-blocking for planning)

**Marketplace / CLI install may be user-mediated.** If `cursor --install-extension …` (or equivalent) fails or is unavailable, implementer documents exact user steps (Extensions → search ID → Install → Reload) and continues verification once the fork is present. This does **not** set `ready_to_implement: no`.

## Ready to implement

**yes**

Steps are ordered and actionable; Continuity locks fork-switch; research named primary + fallback; corpus plan-gate n/a; soft install mediation only.

## Blocking questions

**none**
