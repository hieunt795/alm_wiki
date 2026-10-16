#!/usr/bin/env python3
"""Ghép mỗi câu có citation trong node với claim mà nó trỏ tới trong source note.

Dùng cho phần rà ngữ nghĩa của /lint: phát hiện node nói khác nguồn (sai số, sai ngưỡng,
sai phạm vi) mà lint deterministic không bắt được. Chỉ đọc.

    python tools/citations.py                    # mọi node
    python tools/citations.py --node lcr         # một node
    python tools/citations.py --numbers          # chỉ câu có số / % (nơi hay lệch nhất)
    python tools/citations.py --uncited          # câu/dòng bảng có số mà KHÔNG có citation và không phải Diễn giải
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"
CITE = re.compile(r"\[\[(src-[^\]#|]+)#\^([a-z0-9-]+)\]\]")
FM = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)
NUM = re.compile(r"\d")


def claims_of(src: Path) -> dict[str, dict]:
    """block-id -> {loc, text, quotes} từ source note."""
    out: dict[str, dict] = {}
    lines = src.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.search(r">\s*—\s*(.*?)\s+\^([a-z0-9-]+)\s*$", line)
        if not m:
            continue
        j = i
        while j > 0 and not re.match(r"^\s*- ", lines[j]):
            j -= 1
        text = re.sub(r"^\s*- ", "", lines[j]).strip()
        quotes = [re.sub(r'^\s*>\s*"|"\s*$', "", l) for l in lines[j + 1:i] if re.match(r'^\s*>\s*"', l)]
        out[m.group(2)] = {"loc": m.group(1), "text": text, "quotes": quotes}
    return out


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--node", help="chỉ một node (id = tên file)")
    ap.add_argument("--numbers", action="store_true", help="chỉ câu có chữ số")
    ap.add_argument("--uncited", action="store_true", help="liệt kê câu có số nhưng không có citation")
    args = ap.parse_args()

    sources = {p.stem: p for p in (WIKI / "sources").glob("*.md")}
    cache: dict[str, dict] = {}
    for p in sorted(WIKI.rglob("*.md")):
        if p.parent.name == "sources" or p.stem in {"index", "log", "overview"}:
            continue
        if args.node and p.stem != args.node:
            continue
        body = FM.sub("", p.read_text(encoding="utf-8"), count=1)
        offset = p.read_text(encoding="utf-8").count("\n") - body.count("\n")
        interp = in_math = False
        for n, line in enumerate(body.splitlines(), 1 + offset):
            cites = CITE.findall(line)
            if line.startswith("#"):
                interp = False                       # nhãn Diễn giải hết hiệu lực ở heading mới
            if "Diễn giải" in line:
                interp = True
            if line.strip() == "$$":
                in_math = not in_math
                continue
            if args.uncited:
                if in_math:
                    continue
                text = re.sub(r"\[\[[^\]]*\]\]|\$[^$]*\$|`[^`]*`", "", line)
                text = re.sub(r"^\s*(?:[-*]\s+)?\d+\.\s", "", text)                     # số thứ tự list
                text = re.sub(r"\b(?:TT)?\d+/\d{4}(?:/TT-NHNN)?\b|\b[A-Z]{3}\d+(?:\.\d+)*\b"
                              r"|Điều \d+|Đ\d+(?:\.\d+)*|PL\d+|\bch\d+", "", text)       # tên văn bản / locator
                if (NUM.search(text) and not cites and not interp and "cần nguồn" not in line
                        and not line.rstrip().endswith("?")
                        and not re.match(r"^\s*(\|[\s:-]*)+\|?\s*$", line) and not line.startswith(("#", ">"))):
                    print(f"{p.relative_to(ROOT).as_posix()}:{n}	{line.strip()[:200]}")
                continue
            if not cites or (args.numbers and not NUM.search(CITE.sub("", line))):
                continue
            print(f"\n## {p.relative_to(ROOT).as_posix()}:{n}\n   NODE  {line.strip()[:400]}")
            for sid, bid in cites:
                if sid not in sources:
                    print(f"   !! {sid} không có source note")
                    continue
                cl = cache.setdefault(sid, claims_of(sources[sid])).get(bid)
                if not cl:
                    print(f"   !! ^{bid} không có trong {sid}")
                    continue
                print(f"   SRC   [{cl['loc']}] {cl['text'][:300]}")
                for q in cl["quotes"][:3]:
                    print(f"         \"{q[:300]}\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
