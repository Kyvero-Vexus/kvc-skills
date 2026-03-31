#!/usr/bin/env python3
"""Local lookup helper for the mirrored CLIM 2 specification."""

from __future__ import annotations

import argparse
import fnmatch
import html
import re
import sys
from pathlib import Path
from typing import Iterator, List, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[3]
SPEC_ROOT = REPO_ROOT / "docs" / "clim-spec" / "bauhh.dyndns.org:8000" / "clim-spec"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def page_title(raw_html: str, fallback: str) -> str:
    match = re.search(r"<title\b[^>]*>(.*?)</title\s*>", raw_html, re.IGNORECASE | re.DOTALL)
    if not match:
        return fallback
    title = html_to_text(match.group(1)).strip()
    return title or fallback


def html_to_text(raw_html: str) -> str:
    text = raw_html
    text = re.sub(r"(?is)<script\b.*?</script>", " ", text)
    text = re.sub(r"(?is)<style\b.*?</style>", " ", text)
    text = re.sub(r"(?i)<br\s*/?>", "\n", text)
    text = re.sub(r"(?i)</p\s*>", "\n\n", text)
    text = re.sub(r"(?i)</?(div|li|tr|td|th|table|pre|blockquote|h1|h2|h3|h4|h5|h6)\b[^>]*>", "\n", text)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\[annotate\]", " ", text, flags=re.IGNORECASE)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\r", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text


def toc_entries(contents_file: Path) -> List[Tuple[str, str]]:
    raw = read_text(contents_file)
    entries: List[Tuple[str, str]] = []
    skip_labels = {"Prev", "Next", "Table of Contents", "CLIM 2 Specification"}
    for href, label in re.findall(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a\s*>', raw, flags=re.IGNORECASE | re.DOTALL):
        label_text = html_to_text(label).strip()
        if not label_text or label_text in skip_labels:
            continue
        if href == "index.html":
            continue
        entries.append((href, label_text))
    return entries


def candidate_files(spec_root: Path, patterns: Sequence[str] | None) -> List[Path]:
    files = sorted(spec_root.glob("*.html"))
    if not patterns:
        return files
    kept: List[Path] = []
    for path in files:
        if any(fnmatch.fnmatch(path.name, pattern) for pattern in patterns):
            kept.append(path)
    return kept


def iter_hits(text: str, needle_re: re.Pattern[str], context: int) -> Iterator[str]:
    lines = [line.strip() for line in text.splitlines()]
    for idx, line in enumerate(lines):
        if not line:
            continue
        if needle_re.search(line):
            start = max(0, idx - context)
            end = min(len(lines), idx + context + 1)
            snippet_lines = [part for part in lines[start:end] if part]
            yield " | ".join(snippet_lines)


def search(spec_root: Path, query: str, limit: int, patterns: Sequence[str] | None, context: int) -> int:
    needle_re = re.compile(query, re.IGNORECASE)
    hits = 0
    for path in candidate_files(spec_root, patterns):
        raw = read_text(path)
        text = html_to_text(raw)
        title = page_title(raw, path.name)
        for snippet in iter_hits(text, needle_re, context):
            print(f"{path.name}\t{title}\t{snippet}")
            hits += 1
            if hits >= limit:
                return hits
    return hits


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=SPEC_ROOT, help="spec root (defaults to mirrored CLIM corpus)")
    parser.add_argument("--toc", action="store_true", help="print table of contents entries")
    parser.add_argument("--query", help="case-insensitive regex/text query over stripped HTML text")
    parser.add_argument("--files", nargs="*", help="optional filename glob(s), e.g. 28*.html 29*.html")
    parser.add_argument("--limit", type=int, default=20, help="maximum number of hits to print")
    parser.add_argument("--context", type=int, default=0, help="number of neighboring stripped-text lines to include")
    args = parser.parse_args(argv)

    spec_root = args.root
    contents_file = spec_root / "contents.html"

    if not spec_root.exists():
        print(f"error: spec root not found: {spec_root}", file=sys.stderr)
        return 2

    if args.toc:
        for href, label in toc_entries(contents_file):
            print(f"{href}\t{label}")
        return 0

    if args.query:
        hits = search(spec_root, args.query, args.limit, args.files, args.context)
        if hits == 0:
            print("No matches.", file=sys.stderr)
            return 1
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
