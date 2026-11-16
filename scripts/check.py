#!/usr/bin/env python3
"""Checks the public profile before it ships.

1. Every SVG in profile/assets parses as XML and has a <title> for screen readers.
2. Every image the README references exists.
3. Nothing in the public repo names private repos or internal infrastructure.

Exits non-zero with one line per problem.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILE = ROOT / "profile"
SVG_NS = "{http://www.w3.org/2000/svg}"

# Strings that must never appear in this public repo. Patterns are split so the
# check does not match itself.
FORBIDDEN = [
    r"setoff" + r"\.internal",
    r"(admin|api|app)\.setoff\.tax",
    r"SetoffInc/(setoff|setoff-pub|setoff-mobile)\b",
    r"github\.com/SetoffInc/(?!\.github)",
    r"\.env\b",
]
SCANNED = {".md", ".svg", ".py", ".yml", ".yaml"}
SKIP_DIRS = {".git", "docs"}


def check_svgs(problems):
    svgs = sorted((PROFILE / "assets").glob("*.svg"))
    if not svgs:
        problems.append("no SVGs found in profile/assets")
    for svg in svgs:
        try:
            root = ET.parse(svg).getroot()
        except ET.ParseError as err:
            problems.append(f"{svg.name}: invalid XML ({err})")
            continue
        if root.find(f"{SVG_NS}title") is None:
            problems.append(f"{svg.name}: missing <title>")
        if svg.stat().st_size > 200_000:
            problems.append(f"{svg.name}: {svg.stat().st_size} bytes, keep it under 200 KB")


def check_readme_images(problems):
    readme = PROFILE / "README.md"
    if not readme.exists():
        problems.append("profile/README.md is missing")
        return
    text = readme.read_text()
    for src in re.findall(r'(?:src|srcset)="([^"]+)"', text):
        if src.startswith("http"):
            problems.append(f"README: external image {src}; keep assets in this repo")
        elif not (PROFILE / src).exists():
            problems.append(f"README: image {src} does not exist")
    for alt in re.findall(r'<img[^>]*>', text):
        if 'alt="' not in alt or 'alt=""' in alt:
            problems.append(f"README: image without alt text: {alt[:60]}")


def check_leaks(problems):
    for path in ROOT.rglob("*"):
        if path.suffix not in SCANNED or SKIP_DIRS & set(path.relative_to(ROOT).parts):
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(errors="ignore")
        for pattern in FORBIDDEN:
            for match in re.finditer(pattern, text):
                line = text.count("\n", 0, match.start()) + 1
                problems.append(f"{path.relative_to(ROOT)}:{line}: private reference '{match.group(0)}'")


def main():
    problems = []
    check_svgs(problems)
    check_readme_images(problems)
    check_leaks(problems)
    for p in problems:
        print(p)
    if problems:
        sys.exit(1)
    print("ok: profile is clean")


if __name__ == "__main__":
    main()
