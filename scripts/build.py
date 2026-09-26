#!/usr/bin/env python3
"""Build the static homepage from the small files in content/."""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "index.html"
OUTPUT = ROOT / "index.html"
CONTENT = ROOT / "content"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").rstrip() + "\n"


def build() -> str:
    template = read(TEMPLATE)
    publications = sorted((CONTENT / "publications").glob("*.html"), reverse=True)
    if not publications:
        raise ValueError("No publication files found in content/publications/")
    sections = {
        "PROFILE": read(CONTENT / "profile.html"),
        "NEWS": read(CONTENT / "news.html"),
        "RESEARCH": read(CONTENT / "research.html"),
        "PUBLICATIONS": "\n".join(read(path).rstrip() for path in publications) + "\n",
    }
    for name, section in sections.items():
        marker = "{{" + name + "}}"
        if template.count(marker) != 1:
            raise ValueError(f"Expected one {marker} marker in {TEMPLATE}")
        template = template.replace(marker, section.rstrip(), 1)
    return template


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if index.html needs rebuilding")
    args = parser.parse_args()
    generated = build()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != generated:
            print("index.html is out of date; run python3 scripts/build.py", file=sys.stderr)
            return 1
        print("index.html is up to date")
        return 0
    OUTPUT.write_text(generated, encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
