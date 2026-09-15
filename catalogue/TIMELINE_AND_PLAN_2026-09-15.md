# CaDa — Work Timeline & Forward Plan
*Generated 2026-09-15 from live artifacts on this machine (git logs, ROADMAP.md, Obsidian OKR/Planning, Hermes self-improvement log).*

---

## 1. Timeline

### 2025 H1–H2 — Foundations & web experiments
| Date | Activity | Evidence |
|---|---|---|
| 2025-06→07 | **PWA experimentation wave** — Next.js training, Simpl, PlayTestTristan, PWA examples, WorkStationPWA (later all archived) | `archive/2025.06–07.*` |
| 2025-07-01 | **HTTP Battles** started (game/web project, still uncommitted at top level) | `HTTP Battles/` |
| 2025-08 | Angular, React Router, Git tests; **OpenClassroom** Java/Spring coursework | `archive/2025.08.*`, `ProjetOrif/OpenClassroom` |
| 2025-08→11 | **ProjetOrif spring backend work** — springAuth, spring-auth-develop, testSpringDoc | `ProjetOrif/` |
| 2025-10 | PostMan API response collection | `archive/2025.10.01` |
| 2025-11-11 | frontBack template work (Orif) | `ProjetOrif/frontBack` |
| 2025-12 | **epsic coursework** + **IA project** (aid to other groups); WebCatalogue canvas basis (2025-12-22) | `archive/2025.12.*`, `WebCatalogue` |

### 2026 Q1–Q2 — Orif/Epsic engagement year + agent infrastructure
| Date | Activity | Evidence |
|---|---|---|
| 2026-05 | **Q2 OKR active**: internship hunt (SI stage — 9/10 contacts sent), Projet IA final report, Epsic modules 117/122/164-SQL, Orif Conseil Intersection, Planning V4 → Planning.csv rewrite | `Obsidian/Home/OKR_Trimestriel.md`, `Planning.csv` |
| 2026-05-17 | PDS 3 module 164 milestone deposited on Moodle | OKR changes log |
| 2026-05→06 | **Ultimate Agent / parallel-orchestrator** upgrades, doc-keeper, bb-auditor waves, git-agent delegation tests | OKR `Système_Agents_IA` rows |
| 2026-06-17→24 | **OS-IA project** — custom bootloader + C kernel (PE32→ELF+PEI pipeline), sessions 2–5 cycle logs | `WorkSpace/OS-IA` git log |
| 2026-06-25 | Hermes self-improvement iteration 4 — identity-guard relaxation | `self-improvement-log.md` |
| 2026-07-07 | Obsidian vault last commit — SI/stage progress tracking | `Obsidian/Obsidian` git |
| 2026-07-15 | TestNewWorkspaceAgent checkpoint | `WorkSpace/TestNewWorkspaceAgent` |

### 2026-09 — Current phase: consolidation & 42 prep
| Date | Activity | Evidence |
|---|---|---|
| 2026-09-09 | **Project Organisation program launched** — FAW cycles over `C:\Project`, charter + roadmap + catalogue | `2026.09.09 - Organisation/program/` |
| 2026-09-09→10 | Cycles 0–8: taxonomy, archives of ~12 experiment repos, hygiene moves | ROADMAP.md |
| 2026-09-10 | **Hermes↔Cursor Orchestrator** project created (CLI delegation, session registry, Path A architecture) | `hermes-cursor-orchestrator/` |
| 2026-09-10→11 | Cycles 9–16: WorkSpace XL tree investigated fail-closed; `_backups`/`_quarantine` isolated to `archive/hygiene`; hermes remote cleanup. Whole-tree move still **blocked** (git-strategy hard gate) | ROADMAP.md, sessions/ |
| 2026-09-14→15 | **ft_prework started** — C Piscine Reloaded ex00→ex09 + Python Data & Agri ex0 (exception handling), with rich written notion notes; commit cadence: multiple exercises/day | `current/ft_prework/` |

---

## 2. What this shows (pattern analysis)

1. **Trajectory**: web dev (2025) → Java/Spring backend (Orif, 2025) → systems & AI-orchestration infrastructure (2026) → **C/systems fundamentals + Python** (now, ft_prework) — consistent with preparing a 42-style piscine entry.
2. **Strong meta-workstream**: agent orchestration is a year-long thread (parallel-orchestrator → Hermes team → OS-IA → Hermes↔Cursor orchestrator). It's your signature capability, not a side quest.
3. **Open obligations still tracked**: SI internship (KR2 9/10 contacts, 0 interviews), Projet IA (41.5h remaining in May plan — verify current state), Epsic closeout.
4. **One hard blocker**: `C:\Project\WorkSpace` reorganisation — fail-closed pending the dedicated git-strategy FAW cycle.

---

## 3. Forward plan (proposed base)

### Immediate (this week)
- [ ] **ft_prework**: continue C piscine (ex10+, ex09 done 2026-09-15) — daily commit cadence is already working; keep NOTIONS.md notes per exercise.
- [ ] **Python dat_agr**: finish ex0, schedule ex1 (subject PDFs 02–05 already downloaded).
- [ ] Decide the WorkSpace row: schedule the dedicated **git-strategy FAW cycle** (it unblocks Obsidian + ProjetOrif moves too).

### Short term (2–4 weeks)
- [ ] Piscine-style C peak: build a small C project (e.g. kernel follow-up on OS-IA or an ft-style utility) to consolidate.
- [ ] Hermes↔Cursor orchestrator: ship v1 (spawn/resume/registry already specced) and run one real FAW cycle through it.
- [ ] Reconcile Planning.csv / OKR: Q2 is stale (ended 2026-06) — write Q3 OKR from this timeline.

### Structural (ongoing)
- [ ] Finish the Organisation program: hygiene batch (root `package.*`, node_modules), then Special-git row (`WebCatalogue`, `HTTP Battles` — HTTP Battles has **zero commits**, worth a first commit).
- [ ] SI internship: if still relevant, resume KR2 (Lot B + 1 contact) — it gates the CFC.

---
*Deliverables: this file. Timeline is derived from verifiable artifacts; OKR hour figures are as recorded in Planning.csv (not re-verified against reality).*
