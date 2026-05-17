#!/usr/bin/env python3
"""Depo içi basit arama: markdown ve JSON dosyalarında metin arar."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEARCH_DIRS = ("arkeoloji", "metin-analizi", "etimoloji", "sosyoloji-hukuk", "kaynaklar", "data")
TEXT_GLOBS = ("*.md", "*.json")


def iter_files() -> list[Path]:
    files: list[Path] = []
    for name in SEARCH_DIRS:
        base = ROOT / name
        if not base.is_dir():
            continue
        for pattern in TEXT_GLOBS:
            files.extend(base.rglob(pattern))
    return sorted(set(files))


def search(term: str, as_json: bool = False) -> list[dict]:
    term_lower = term.lower()
    hits: list[dict] = []

    for path in iter_files():
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if term_lower not in text.lower():
            continue
        rel = path.relative_to(ROOT)
        if as_json and path.suffix == ".json":
            try:
                data = json.loads(text)
                hits.append({"file": str(rel), "type": "json", "preview": _json_preview(data, term_lower)})
            except json.JSONDecodeError:
                hits.append({"file": str(rel), "type": "json", "preview": "(parse error)"})
        else:
            line = _first_matching_line(text, term_lower)
            hits.append({"file": str(rel), "type": path.suffix[1:], "preview": line})
    return hits


def _first_matching_line(text: str, term: str) -> str:
    for line in text.splitlines():
        if term in line.lower():
            return line.strip()[:120]
    return ""


def _json_preview(data: object, term: str) -> str:
    raw = json.dumps(data, ensure_ascii=False)
    idx = raw.lower().find(term)
    if idx < 0:
        return raw[:120]
    start = max(0, idx - 40)
    return raw[start : start + 120]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="sumer-ibrahim-izleri depo araması")
    parser.add_argument("term", help="Aranacak kelime veya ifade")
    parser.add_argument("--json", action="store_true", help="JSON çıktı")
    args = parser.parse_args()

    results = search(args.term, as_json=args.json)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        if not results:
            print(f"Sonuç yok: {args.term!r}")
            return 1
        for hit in results:
            print(f"{hit['file']}: {hit['preview']}")
    return 0 if results else 1


if __name__ == "__main__":
    sys.exit(main())
