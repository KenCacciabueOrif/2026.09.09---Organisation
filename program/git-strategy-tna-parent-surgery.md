# Git-strategy — TNA parent-surgery (ignored nested clones)

**Program:** organise `C:\Project` · Multi-experiment remaining **`WorkSpace` only**  
**Cycle 20 session:** [`../sessions/2026.09.15-1117/`](../sessions/2026.09.15-1117/) (policy **written**)  
**Cycle 23 session:** [`../sessions/2026.09.15-1432/`](../sessions/2026.09.15-1432/) (#4 **approved-for-named-map**; nest execute **held**)  
**Baseline hazards:** [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md) (Continuity X; do not rewrite Cycle 10–19 classification)  
**Mutation class (Cycle 20):** **`docs_only`** — policy **written**; nest FS not authorized by creating this file.  
**Mutation class (Cycle 23):** **`docs_only`** (plan-gate **A**) — #4 status flip + honesty only; **zero** nest / TNA / WorkSpace FS moves.  
**Clearance #4 status:** **approved-for-named-map** (Cycle 23 plan-gate **A**) — map only: `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` → `C:\Project\archive\2026.09.15 - hermes-agent`. Nest **execute held**. **A+E deliberately reserved** for a later dedicated user-reviewed execute gate (**not declined** — dirty TNA ~**2300** absolute-path consumer risk). Other nests still need their own named-map gate. Whole-tree clearance still **NO**.

**Taxonomy:** **proposed-ratified — ready for user sign-off** (not final).  
**Must-preserve:** **draft — not auto-locked / for user review**.  
**Dirty parent:** TNA ~**2307** porcelain — disclose only; **NO_AUTO_COMMIT** (Q3=A).

---

## Scope / nest table

**Wrapper (keep at root):** `C:\Project\WorkSpace` — never silent whole-tree archive under this policy.

**Nest model:** **Gitignored nested clones** inside the TNA envelope — **not** git submodules. There is **no** `.gitmodules`. TNA `.gitignore` header: *“Nested git repositories (cloned projects — tracked separately)”*. Cite ignore lines:

| Line (TNA `.gitignore`) | Pattern | Covers |
| --- | --- | --- |
| 2 | `Projects/Project Atelier IA/Projet Adrien/orchestrateur/` | orchestrateur nest |
| 3 | `Projects/Project Atelier IA/Workshop/` | WorkshopOrif (under Workshop/) |
| 4 | `hermes-agent` | hermes-agent nest |

| Unit | Absolute path | Role | Status under this policy |
| --- | --- | --- | --- |
| **TNA** | `C:\Project\WorkSpace\TestNewWorkspaceAgent` | Envelope (dirty ~2307; **NO_AUTO_COMMIT**) | Keep at root interim; **not** moved by nest extract |
| **hermes-agent** | `C:\Project\WorkSpace\TestNewWorkspaceAgent\hermes-agent` | In-TNA nest (ignored) | **#4 approved-for-named-map** (Cycle 23) → dest `C:\Project\archive\2026.09.15 - hermes-agent`; **execute held** (A+E reserved, not declined); still live under TNA |
| **orchestrateur** | `C:\Project\WorkSpace\TestNewWorkspaceAgent\Projects\Project Atelier IA\Projet Adrien\orchestrateur` | In-TNA nest (ignored) | Future gated `path_batch` candidate only |
| **WorkshopOrif** | `C:\Project\WorkSpace\TestNewWorkspaceAgent\Projects\Project Atelier IA\Workshop\WorkshopOrif` | In-TNA nest (ignored) | Future gated `path_batch` candidate only |
| **OS-IA** | `C:\Project\archive\2026.09.15 - OS-IA` | Archived Cycle 19 Continuity X | **Verify-only** — do not reverse / re-archive / re-propose |

**Live nested count under WorkSpace after Cycle 19:** **4** (TNA + three in-TNA nests). OS-IA is **outside** the live WorkSpace tree.

**Out of this surgery scope:** Appendix A `_backups` / `_quarantine` (already isolated Cycle 14); Medium / Early / archived Multi-experiment peers (`PWAExemple`, etc.); remote-config; whole `WorkSpace` envelope move.

---

## Clearance #4 definition (written vs approved)

Whole-tree clearance criterion **#4** in [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md):

> Parent-surgery policy for dirty TNA is **written and approved** if any in-TNA nest moves are in map.

| Half | Meaning | Status |
| --- | --- | --- |
| **Written** | This policy exists with procedure + fail-closed rules + post-attest + non-goals | **Satisfied** (Cycle 20) |
| **Approved (named map)** | Dedicated plan-gate **A** / **A+E** / **yes** for an **exact** nest source → destination map, **or** explicit user waiver of #4 for a stated reason | **Cycle 23 plan-gate A:** **approved-for-named-map** for hermes-agent → `C:\Project\archive\2026.09.15 - hermes-agent` only. Nest execute **held** this cycle. **A+E reserved** (not declined). Other nests / maps still **pending** their own gate. Continuity / Choose / docs alone **≠** approval. |

**Hard distinctions:**

- Continuity X / Choose / STAGE 1 docs / creating or amending this file **≠** nest-move approval.
- Writing alone **≠** flip whole-tree clearance **NO → yes** (criteria **#1–#6** must **all** be true).
- **#4 approved-for-named-map** unlocks a **future** dedicated execute gate for **that map only** — it does **not** move files (**A**) and does **not** flip whole-tree clearance **NO → yes**.
- Do **not** treat #4 approved-for-one-map as blanket approval for orchestrateur / WorkshopOrif / TNA envelope / whole WorkSpace.

---

## Preflight (per nest, nest path only)

Run **immediately before** any approved extract. Probe the **nested clone directory** (the path that owns that nest’s `.git`) — **not** the TNA wrapper and **not** `C:\Project\WorkSpace` as if they were the nest.

1. **`Test-Path` source** — nest absolute path exists.
2. **`Test-Path` destination** — destination parent exists; destination leaf is **free** (no collision).
3. **`git worktree list`** on the **nested clone path only** — expected usually **1** (main). Fail-closed if unexpected linked worktrees appear. Do **not** run worktree list on parent wrappers that resolve to outer repos.
4. **Remotes inventory** — `git remote -v` (or Read `.git/config`): record **names + schemes only**; Continuity default = **path-only** (no `set-url` / origin rewrite / force-push).
5. **Porcelain recount** — `git status --porcelain` on the nest (and disclose parent TNA dirt if relevant). Counts may differ from research (~hermes 56 / orchestrateur 60 / WorkshopOrif 119; TNA ~2307). **Disclose only — do not auto-commit / stash-clean.**
6. **Ignore / not-tracked / not-submodule** — confirm nest still matches TNA `.gitignore` (e.g. `git check-ignore -v`); confirm **no** `.gitmodules` surgery needed; confirm nest is **not** unexpectedly tracked by parent TNA.
7. **Opaque secrets** — if plan lists `.env*` under the nest, presence-only under **destination** after move (never open/quote contents). Cycle research may list live counts under WorkSpace — re-attest for units **in map** only.
8. **Non-git absolute references (open)** — presence-only inventory of scripts / IDE / docker / docs under dirty TNA that hard-code the nest path. **Do not invent** a consumer list in docs cycles; require scan **before execute**. Residual breakage risk remains until that scan.

---

## Atomic nest relocate procedure (future execute only)

**Authorize only** after #4 **approved-for-named-map** **and** a dedicated **execute** plan-gate (**A+E** or later execute-only yes) for that same map. Cycle 23 = #4 approved-for-hermes-map; **execute still held** (A+E reserved). Prefer one atomic OS rename per nest.

1. **Intact move** — relocate the **entire** nest tree including its `.git` (e.g. PowerShell `Move-Item -LiteralPath <source> -Destination <dest>`). Confirm parameter names parse **before** the first real move.
2. **No history rewrite** — no `filter-repo`, no dissolve into parent index, no force-push, no remote URL rewrite.
3. **No submodule teardown** — nests are ignored clones; do **not** invent `deinit` / `.git/modules` / `.gitmodules` edits unless live evidence later proves submodule surprise (then fail-closed — see below).
4. **Remotes path-only** — leave remote URLs unchanged unless a **separate** remote-config gate says otherwise.
5. **Windows lock recovery** (only if PermissionDenied / Access Denied leaves a **split** tree) — same as hazards safe rules:
   - Reunify remaining source children into the destination wrapper (same relative layout).
   - For stubborn remainder: `robocopy <src> <dst> /E /MOVE` as recovery (approved payload only).
   - Remove **only empty** leftover `.git` **shells** (0 children) — never delete non-empty payload or unrelated paths.
   - Re-attest destination nested `.git` (+ opaque paths if listed); log under Deviations.
6. **Reverse-move note** — for each successful move, log one-line undo: dest → original source **only if** source empty and dest complete.

**Robocopy is recovery, not the default move tool.** Prefer clean `Move-Item` success (Cycle 8 / Cycle 19 pattern).

---

## Parent TNA handling under NO_AUTO_COMMIT

Because nests are **gitignored**, extract typically:

- Does **not** require submodule teardown.
- Does **not** require a parent TNA commit for the nest tree to leave the working directory.
- Leaves parent TNA dirty (~2307 or live recount) **as-is**.

| Rule | Detail |
| --- | --- |
| **Forbid** | Stash / commit / clean of the bulk TNA WT “to enable” the move |
| **Forbid** | Auto-commit of dirty TNA after extract |
| **Allow** | Leave TNA dirty; disclose porcelain; set **`NO_AUTO_COMMIT=true`** for TNA (and any coupled parent dirt) this cycle |
| **Allow (optional)** | Empty-dir cleanup after nest gone (directory housekeeping only) |
| **Allow (optional, gated)** | `.gitignore` hygiene (remove obsolete ignore lines) **only** under a future step that **explicitly** allows parent **file** edits — still **not** auto-commit of the bulk WT |
| **Disclose** | If parent TNA tracks other dirt while nests move, document coupling; do not invent commits |

**Residual risk:** non-git absolute-path consumers under TNA may break after extract — presence-only inventory is a **pre-execute** requirement, not satisfied by this docs cycle alone.

---

## Fail-closed conditions

Abort the nest row (and do not expand scope) if any of:

| Condition | Action |
| --- | --- |
| Unexpected linked worktree on the **nested clone path** | Fail-closed; do not move |
| Path lock / PermissionDenied unresolved after reunify + allowed robocopy recovery | Fail-closed; reverse-move notes; leave recoverable state |
| Nest unexpectedly **tracked** by parent **or** submodule surprise (`.gitmodules` / gitlink) | Fail-closed — this policy assumes ignored clones; do not invent teardown |
| Destination collision | Fail-closed; pick new dest only via amended plan gate |
| Attempt to move dirty **TNA envelope** or whole **`WorkSpace`** under “parent-surgery” without a **separate** whole-tree / envelope gate | Fail-closed — out of this policy |
| Attempt to reverse / re-archive **OS-IA**, reopen Appendix A parents, or Medium / Early / archived peers as sources | Fail-closed — hard forbid |
| Claiming whole-tree clearance **yes** because docs or one nest moved | Fail-closed honesty — criteria #1–#6 still bind |

---

## Post-move attest (future execute cycle)

After each approved nest relocate:

1. Nest `git rev-parse --show-toplevel` resolves at **destination**.
2. Remotes unchanged (names + URL schemes vs preflight) unless a separate remote-config gate applied.
3. `git worktree list` on destination nest path still OK (expected count).
4. **Source path gone** (or empty leftover shell removed only if empty).
5. Destination nested `.git` present; nested-git count under destination matches preflight expectation (usually 1).
6. Opaque secret paths (if listed) — `Test-Path` / Read / Glob **presence only** under destination.
7. Org honesty: `catalogue/INDEX.md` / `catalogue/inventory.md` / `program/ROADMAP.md` Notes updated for **nested count** and remaining units; Multi-experiment still **Remaining: `WorkSpace` only** while WorkSpace / TNA remain — **not** Complete; **not** Primary next / Special git.
8. Session log: reverse-move note + **NO_AUTO_COMMIT** disclosure for dirty TNA / coupled trees.

---

## Explicit non-goals

- Appendix A re-propose or re-execute (`_backups` / `_quarantine`)
- OS-IA reverse move or re-archive
- Medium / Early / archived Multi-experiment peers (`PWAExemple`, `GitTest`, `WorkStationPWA`, etc.) as sources
- Silent whole-tree archive of `C:\Project\WorkSpace`
- Moving the dirty **TNA envelope** itself under this policy without a separate envelope gate
- Remote `set-url` / force-push / history rewrite
- Auto-commit or stash-clean of dirty TNA (~2307)
- Claiming clearance #4 **approved** from Continuity / docs alone (Cycle 23 approval is **plan-gate A** for the named hermes map only)
- Claiming nest **execute** authorized from #4 approved-for-map alone (still needs dedicated execute / **A+E** gate)
- Claiming **`clearance_whole_tree` yes** after docs alone or after a single nest extract
- Inventing absolute-path consumer lists or destination picks as **execute** decisions in a docs-only cycle

---

## Held defaults for later gates (document — do not execute)

Mark **held / choose at nest `path_batch` gate** — Continuity and this docs file do **not** lock destinations:

| Topic | Held options | Notes |
| --- | --- | --- |
| Destination class | **archive** dated leaf under `C:\Project\archive\…` · **paused** under `C:\Project\paused\…` · **sibling** under `C:\Project\…` (outside WorkSpace) | Choose per nest at move gate; default suggestion may mirror Cycle 19 archive pattern but is **not** pre-approved |
| Batch size | One nest per gate · or named multi-nest map | Prefer small verifiable batches |
| Empty parent-dir delete after extract | Delete empty parents · leave empty shells | Preference **open** — decide at execute gate |
| `.gitignore` hygiene | Leave lines · remove obsolete patterns under explicit parent-edit gate | Never bulk-commit TNA WT to “finish” hygiene |
| Absolute-path consumer scan | Required before execute · scope TBD at gate | Presence-only; do not invent paths now |

---

## How a future cycle uses this artifact

1. Lock ROADMAP **Multi-experiment / WorkSpace only** (TNA envelope).
2. Confirm this file still accurate (paths, ignore model, NO_AUTO_COMMIT).
3. For **hermes-agent** (Cycle 23 #4 already **approved-for-named-map**): plan dedicated **execute** gate (**A+E** reserved / execute-only) with the **same** exact map — do **not** re-litigate #4 for this map unless amending source→dest.
4. For **other** nests: plan `fs_mutation` `path_batch` with **exact** nest map + destinations; user plan-gate **A** / **A+E** / **yes** → #4 **approved-for-that-map** (or record waiver).
5. Implementer (execute): preflight + absolute-path consumer scan → atomic move → post-attest → honesty; **never** auto-commit TNA.
6. Whole-tree archive of WorkSpace remains **blocked** until **all** clearance criteria #1–#6 are true **and** a dedicated whole-tree / envelope gate says so.

**Next FAW lock hint:** keep **`WorkSpace` only** + continue Continuity X clearance / keep-at-root — hermes nest extract still **pending** (dedicated execute / **A+E** reserved; ~2300 TNA absolute-path consumers); other nests still need named-map #4 gates.

---

## Related pointers

- Hazards / Continuity X: [`git-strategy-workspace-hazards.md`](git-strategy-workspace-hazards.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- Index / inventory: [`../catalogue/INDEX.md`](../catalogue/INDEX.md) · [`../catalogue/inventory.md`](../catalogue/inventory.md)
- Cycle 19 OS-IA execute: [`../sessions/2026.09.15-1014/`](../sessions/2026.09.15-1014/)
- Cycle 20 docs: [`../sessions/2026.09.15-1117/`](../sessions/2026.09.15-1117/)
- Cycle 23 #4 approved-for-map: [`../sessions/2026.09.15-1432/`](../sessions/2026.09.15-1432/)
