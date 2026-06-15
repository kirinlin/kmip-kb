#!/usr/bin/env python3
"""One-time migration: reorganise kb/profiles/ into source-section-based subdirectories.

prof-3.x          → kb/profiles/authentication/
prof-4.x          → kb/profiles/v1/
prof-5.1–5.5      → kb/profiles/base-encoding/
prof-5.6–5.18     → kb/profiles/key-management/
§14.x + index.md  → stay at kb/profiles/ root

Usage:
    python scripts/migrate_profiles.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROFILES = REPO / "kb" / "profiles"


# ── helpers ──────────────────────────────────────────────────────────────────

def read_source_section(f: Path) -> str:
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.startswith("source_section:"):
            return line.split(":", 1)[1].strip().strip('"')
    return ""


def dest_subdir(source_section: str) -> str | None:
    """Return the subdir name for a given source_section, or None for root."""
    if source_section.startswith("prof-3."):
        return "authentication"
    if source_section.startswith("prof-4."):
        return "v1"
    m = re.match(r"prof-5\.(\d+)$", source_section)
    if m:
        n = int(m.group(1))
        return "base-encoding" if 1 <= n <= 5 else "key-management"
    return None  # §14.x, index.md → root


# ── build move map ───────────────────────────────────────────────────────────

def build_file_map() -> dict[Path, Path]:
    """Map every .md in kb/profiles/ to its new (absolute) path."""
    fmap: dict[Path, Path] = {}
    for f in sorted(PROFILES.glob("*.md")):
        if f.name == "index.md":
            fmap[f] = f
            continue
        ss = read_source_section(f)
        sub = dest_subdir(ss)
        fmap[f] = PROFILES / sub / f.name if sub else f
    return fmap


# ── link rewriter ─────────────────────────────────────────────────────────────

_LINK_RE = re.compile(r"(\[[^\]]*\]\()([^)#\s][^)]*?)(\))")


def relink(link: str, old_file: Path, new_file: Path, fmap: dict[Path, Path]) -> str:
    """Rewrite one relative Markdown link.

    Resolves the link against old_file's directory to find the OLD absolute
    target, maps that to the NEW absolute target via fmap, then computes the
    new relative path from new_file's directory.
    """
    if link.startswith(("http", "#", "mailto")):
        return link
    # Resolve against OLD location
    abs_old_target = (old_file.parent / link).resolve()
    # Map to new target location (may be same if target doesn't move)
    abs_new_target = fmap.get(abs_old_target, abs_old_target)

    # Compute relative path from NEW file's directory to NEW target
    new_dir = new_file.parent
    try:
        rel = abs_new_target.relative_to(new_dir)
        return rel.as_posix()
    except ValueError:
        pass
    # Walk up to common ancestor
    tp = abs_new_target.parts
    dp = new_dir.parts
    i = 0
    while i < len(tp) and i < len(dp) and tp[i] == dp[i]:
        i += 1
    ups = len(dp) - i
    downs = "/".join(tp[i:])
    return "../" * ups + downs


def update_links_in_file(
    content: str, old_file: Path, new_file: Path, fmap: dict[Path, Path]
) -> str:
    def replacer(m: re.Match) -> str:
        prefix, link, suffix = m.group(1), m.group(2), m.group(3)
        new_link = relink(link, old_file, new_file, fmap)
        return prefix + new_link + suffix

    return _LINK_RE.sub(replacer, content)


# ── main ──────────────────────────────────────────────────────────────────────

def main(dry_run: bool) -> int:
    fmap = build_file_map()

    moving = [(old, new) for old, new in fmap.items() if old != new]
    staying = [old for old, new in fmap.items() if old == new]

    print(f"Files to move : {len(moving)}")
    print(f"Files at root : {len(staying)}")

    # -- 1. create subdirectories -----------------------------------------------
    subdirs = {new.parent for _, new in moving}
    for d in sorted(subdirs):
        if not dry_run:
            d.mkdir(parents=True, exist_ok=True)
        print(f"mkdir {d.relative_to(REPO)}")

    # -- 2. rewrite links in ALL profile files BEFORE moving --------------------
    # (so resolve() on old_file still works; we write to a dict first)
    new_contents: dict[Path, str] = {}

    # Files that need link updates: all profile files that have any relative links
    all_profile_files = list(fmap.keys())  # old paths
    for old_file in all_profile_files:
        new_file = fmap[old_file]
        original = old_file.read_text(encoding="utf-8")
        updated = update_links_in_file(original, old_file, new_file, fmap)
        if updated != original or old_file != new_file:
            new_contents[old_file] = (new_file, updated)

    # -- 3. write updated content back to OLD paths first -----------------------
    # (git mv will then carry the updated content to the new path)
    for old_file, (new_file, content) in sorted(new_contents.items()):
        rel_old = old_file.relative_to(REPO)
        rel_new = new_file.relative_to(REPO)
        if old_file != new_file:
            print(f"mv {rel_old} → {rel_new}")
        else:
            print(f"relink {rel_old}")
        if not dry_run:
            old_file.write_text(content, encoding="utf-8")

    # -- 4. git mv --------------------------------------------------------------
    for old_file, new_file in sorted(moving):
        if dry_run:
            continue
        result = subprocess.run(
            ["git", "mv", str(old_file), str(new_file)],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"ERROR git mv {old_file.name}: {result.stderr.strip()}", file=sys.stderr)
            return 1

    print("Done." if not dry_run else "Dry run complete (no files changed).")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print plan without making changes.")
    args = parser.parse_args()
    sys.exit(main(args.dry_run))
