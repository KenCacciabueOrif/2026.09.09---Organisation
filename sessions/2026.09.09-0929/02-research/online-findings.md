# Online findings

Session: `sessions/2026.09.09-0929/02-research/`  
Focus: multi-year personal project corpora; dated naming; navigation across many local projects; multi-repo move/reorg without breaking functionality.

## Dated naming & file organisation

- [The File Naming Convention System That Actually Works](https://renamer.ai/insights/file-naming-conventions-best-practices) — ISO-style `YYYY-MM-DD` (hyphenated) sorts chronologically across filesystems; avoid special characters that break cross-platform paths; migrate gradually (new files first) rather than big-bang renames.
- [Purposeful Project Folder Structure – Mike Burke](https://www.themikeburke.com/purposeful-project-folder-structure/) — Long-running practice of ISO 8601 date prefixes so chronology is visible without separate archive folders; dates reduce “final/v2” naming chaos.
- [File Naming & Organization – SJSU Library](https://library.sjsu.edu/c.php?g=769588&p=5523042) — Prefer ISO 8601 dates; balance folder breadth vs depth; distinguish active vs past work with archive/year folders to shrink search scope.
- User preference in this program uses **`yyyy.mm.dd` + name** (dots, matching FAW sessions). Functionally equivalent for sort order to `YYYY-MM-DD` if zero-padded; document the chosen separator and stick to it.

## Actionability / status-first corpora (PARA & variants)

- [The PARA Method – Tiago Forte / Forte Labs](https://fortelabs.com/blog/para/) — Canonical four buckets: Projects, Areas, Resources, Archives, organised by **actionability**, not topic. Strong fit for “what’s next” alongside history (Archives hold completed work).
- [Vault and Structure (NIPARAS) – hedwards.dev](https://hedwards.dev/filesystem-as-vault/) — Extends PARA-like layout with Now/Inbox/System; emphasises filesystem-as-source-of-truth and archive as cold storage.
- [open-mnemex/core](https://github.com/open-mnemex/core) — Practical numbered roots (`10_Projects`, `99_Archives`, `__To_Review`) plus machine-readable rules docs; useful pattern for an **index + conventions** living beside the corpus.
- [A Practical Folder Structure for Developers and Solopreneurs](https://thatamazingprogrammer.com/posts/a-practical-folder-structure-for-developers-and-solopreneurs/) — Status-first tree under `~/Projects` (`inbox` / `active` / `paused` / `archive` / `scratch`) with category splits inside; separates “doing work” from “business records.”

## Navigating many local projects

- [Managing Multiple Projects With AI Tools – Vibe Coder Blog](https://blog.vibecoder.me/managing-multiple-projects-ai-tools) — Prefer **flat, one-project-per-repo** predictability; keep a small active set; per-project context docs (e.g. `CLAUDE.md` / README) reduce thrash — aligns with maintaining a **corpus index** in the organisation repo.
- [Keeping Laravel Projects Findable When Local Work Starts to Sprawl – DEV Community](https://dev.to/saqueib/keeping-laravel-projects-findable-when-local-work-starts-to-sprawl-55na) — Treat sprawl as an **indexed system**: unique names, ownership/type in path, lightweight metadata (`PROJECT.md` / `.project-meta.json`), fuzzy launchers (`fzf`/Raycast); archive dead repos out of active search.

## Multi-repo moves, remotes, worktrees (do not break functionality)

- [git-worktree documentation](https://git-scm.com/docs/git-worktree) — Worktrees are linked checkouts; relocating the main repo or worktree directories without updating links breaks the set. Inventory found Obsidian main + 3 worktrees — **move as a coordinated unit** or repair links after move.
- [Migrating Git from multirepo to monorepo without losing history – Netlify](https://developers.netlify.com/guides/migrating-git-from-multirepo-to-monorepo-without-losing-history/) — History-preserving merges need deliberate `filter-repo` + unrelated-history merge; **not** required for simple filesystem relocation of intact git roots. Prefer **atomic folder moves of entire `.git` trees** unless intentionally consolidating repos.
- [Migrating Multiple Repositories to a Monorepo – AKJ.IO](https://akj.io/migrating-repos-to-monorepo-with-git-history) — Reinforces: rewriting history is a separate project from moving folders; use fresh clones and explicit remotes when rewriting.
- [git-filter-repo (newren)](https://github.com/newren/git-filter-repo) — Official-ish tool for history rewrite; refuse to run casually on live working trees — schedule only if a later cycle chooses monorepo/history rewrite (out of Cycle 0 scope).
- Practical implication for this corpus: **default strategy = move each git root intact** (including `node_modules`/opaque `.env` as payload). Remotes (HTTPS vs SSH) usually survive path moves; absolute paths in configs, worktrees, Docker volume mounts, and IDE workspaces may not — verify post-move. Nested empty parent repos (e.g. `HTTP Battles`) need classification before rename.

## Takeaways mapped to Cycle 0 goals

| Goal | Online consensus |
| --- | --- |
| Dated view | Date-prefix folders/names (`yyyy.mm.dd` or ISO) + archive/year buckets |
| What’s next | Actionability/status layer (PARA or active/paused/archive), not dates alone |
| Easy navigation | Corpus **index/metadata** + unique names + launcher/search; don’t rely on deep nesting |
| Don’t break projects | Move **whole git roots**; special-case worktrees; defer history rewrite; keep deps/secrets with the project |

## Sources not treated as requirements

Monorepo migration guides are cited for **awareness** (what *not* to do accidentally). Cycle 0 and likely early move cycles should **not** rewrite git history unless a dedicated git-strategy cycle decides otherwise.
