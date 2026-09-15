#!/usr/bin/env python3
"""Regenerate the JSON data blob inside catalogue/work_timeline.html.

Scans C:\\Project for git repos, commit history, and top-level dirs, then
swaps the <script id="data" type="application/json"> blob in-place so the
dashboard reflects the current state of the corpus.

Run:  uv run python generate_work_timeline.py
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CORPUS = Path(r"C:\Project")
HTML = Path(r"C:\Project\2026.09.09 - Organisation\2026.09.09---Organisation\catalogue\work_timeline.html")
GIT = r"C:\Users\CaDa\AppData\Local\Programs\Git\cmd\git.exe"  # GfW git (GCM); PATH git hangs on push, may also misbehave here
OWN_AUTHORS = {"ken cacciabue", "u-secinfo\\cada", "kencacciabueorif", "cada"}

MARK_OPEN = '<script id="data" type="application/json">'
MARK_CLOSE = "</script>"


def find_git_repos(root: Path, depth=0, max_depth=4):
    """Find top-level .git dirs, not descending into nested repos."""
    if (root / ".git").exists() or (root / ".git").is_file():
        yield root
        return
    if depth >= max_depth:
        return
    try:
        entries = sorted(p for p in root.iterdir() if p.is_dir())
    except OSError:
        return
    skip = {"node_modules", ".git", "__pycache__", ".venv", "venv", ".next", "dist", "build"}
    for p in entries:
        if p.name in skip or p.name.startswith("."):
            continue
        yield from find_git_repos(p, depth + 1, max_depth)


def git(repo: Path, *args):
    try:
        out = subprocess.run(
            [GIT, "-C", str(repo), *args],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30,
        )
        return out.stdout if out.returncode == 0 else ""
    except (OSError, subprocess.TimeoutExpired):
        return ""


def dir_stats(path: Path):
    files = 0
    size = 0
    newest = 0.0
    exts = {}
    skip = {".git", "node_modules", "__pycache__", ".next"}
    for dirpath, dirnames, filenames in os.walk(path):
        dirnames[:] = [d for d in dirnames if d not in skip]
        for f in filenames:
            fp = Path(dirpath) / f
            try:
                st = fp.stat()
            except OSError:
                continue
            files += 1
            size += st.st_size
            newest = max(newest, st.st_mtime)
            e = fp.suffix.lower() or "(none)"
            exts[e] = exts.get(e, 0) + 1
    return files, size, newest, exts


def status_for(path: Path):
    rel = str(path).lower()
    if f"{os.sep}archive{os.sep}" in rel or rel.endswith(f"{os.sep}archive"):
        return "archived"
    if f"{os.sep}paused{os.sep}" in rel or rel.endswith(f"{os.sep}paused"):
        return "paused"
    return "workspace"


def top_status(name: str):
    if name == "archive":
        return "archived"
    if name == "paused":
        return "paused"
    if name == "current":
        return "active"
    return "workspace"


def build():
    repos = []
    commits = []
    for repo in find_git_repos(CORPUS):
        # Skip git worktrees of another repo (e.g. Obsidian/worktrees/*)
        wt = repo / ".git"
        if wt.is_file():
            continue
        files, size, newest_mtime, exts = dir_stats(repo)
        top_ext = dict(sorted(exts.items(), key=lambda kv: -kv[1])[:12])

        branches = [b.strip() for b in git(repo, "branch", "-a").splitlines() if b.strip()]
        branches = [b.replace("remotes/", "remotes/").replace("* ", "") for b in branches]
        remotes = []
        for line in git(repo, "remote", "-v").splitlines():
            if line.endswith("(fetch)"):
                name, url = line.split(maxsplit=1)
                remotes.append(f"{name}:{url}")

        log = git(
            repo, "log", "--all",
            "--pretty=format:%H%x09%ad%x09%an%x09%s",
            "--date=short",
        )
        first = last = own_first = own_last = None
        own_count = 0
        seen_hashes = set()
        for line in log.splitlines():
            parts = line.split("\t", 3)
            if len(parts) != 4:
                continue
            chash, date, author, subject = parts
            # `--all` walks every ref: the same commit appears once per ref
            # (branch + remote counterpart). Dedupe at source by commit hash.
            if chash in seen_hashes:
                continue
            seen_hashes.add(chash)
            first = first or date
            last = date
            if author.strip().lower() in OWN_AUTHORS:
                own_count += 1
                own_first = own_first or date
                own_last = date
                commits.append({
                    "repo": repo.name, "path": str(repo), "date": date,
                    "author": author.strip(), "subject": subject, "own": True,
                })
            else:
                commits.append({
                    "repo": repo.name, "path": str(repo), "date": date,
                    "author": author.strip(), "subject": subject, "own": False,
                })

        repos.append({
            "name": repo.name,
            "path": str(repo),
            "kind": "git" if (repo / ".git").exists() else "git",
            "status": status_for(repo),
            "commit_count": len(seen_hashes),
            "own_commits": own_count,
            "first_commit": last,   # git log newest-first: first line is newest
            "last_commit": first,
            "own_first_commit": own_last,
            "own_last_commit": own_first,
            "files": files,
            "size_bytes": size,
            "top_extensions": top_ext,
            "branches": branches[:40],
            "remotes": remotes,
            "newest_file_mtime": datetime.fromtimestamp(newest_mtime).strftime("%Y-%m-%d") if newest_mtime else None,
        })

    repos.sort(key=lambda r: r["path"])

    top_level = []
    for entry in sorted(CORPUS.iterdir()):
        if not entry.is_dir() or entry.name.startswith("~"):
            continue
        files, size, _, _ = dir_stats(entry)
        top_level.append({
            "name": entry.name, "files": files,
            "size_bytes": size, "status": top_status(entry.name),
        })

    # hermes block: keep narrative lists, refresh skill count
    skills_dir = Path.home() / ".hermes" / "skills"
    try:
        skill_count = sum(1 for _ in skills_dir.iterdir()) if skills_dir.exists() else 0
    except OSError:
        skill_count = 0

    data = {
        "generated": datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M"),
        "hermes": {
            "self_improvement_iterations": [
                "Iteration 1 — 2026-06-10: Built-in Observability Foundation",
                "Iteration 2 — 2026-06-10: Auto-Hooking Observability Plugin",
                "Iteration 3 — 2026-06-25: Phantom Notification Count Pattern",
                "Iteration 4b — 2026-06-25: Consul Phantom Storm Self-Improvement (Background Work)",
                "Iteration 4c -- 2026-06-25: Consul Proposals and Active Discipline Framework",
                "Iteration 4 - 2026-06-25: Identity Guard Relaxation (Option A)",
            ],
            "plans": ["iteration-1-observability.md", "iteration-2-observability-plugin.md", "self-improvement-profile.md"],
            "skill_count": skill_count,
        },
        "repos": repos,
        "commits": commits,
        "top_level": top_level,
    }
    return data


def main():
    html = HTML.read_text(encoding="utf-8")
    start = html.index(MARK_OPEN) + len(MARK_OPEN)
    end = html.index(MARK_CLOSE, start)
    data = build()
    blob = json.dumps(data, ensure_ascii=False)
    HTML.write_text(html[:start] + blob + html[end:], encoding="utf-8")
    print(f"updated {HTML.name}: generated={data['generated']} "
          f"repos={len(data['repos'])} commits={len(data['commits'])} top_level={len(data['top_level'])}")


if __name__ == "__main__":
    sys.exit(main())
