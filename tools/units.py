#!/usr/bin/env python3
"""Tách một nguồn markdown thành ingest unit và tính SHA-256.

Chỉ đọc `01_sources/`, không bao giờ ghi. Output là YAML để dán vào
`03_meta/sources.yaml` (khối `sha256` + `units`).

Preset:
    basel    "## LCR40 …"                       -> LCR40
    vn       Chương / Mục / Phụ lục             -> C1, C2-M5, PL1
    chapter  "## CHAPTER 7 …" (sách docling)    -> ch7
    auto     tự chọn heading level cho 3–60 unit
    --chunk N  gộp heading thành unit ~N dòng (sách có heading kém)
    --dir      collection: mỗi file .md = 1 unit

Ví dụ:
    python tools/units.py "01_sources/alm/Basel/LCR/LCR.md" --preset basel
    python tools/units.py "01_sources/alm/TT50_2026_SBV/TT50_2026_SBV.md" --preset vn
    python tools/units.py "01_sources/choudhry_banking_fixed_income/Choudhry_Analysing_Yield_Curve.md" --preset chapter
    python tools/units.py "01_sources/tata_bank_alm/Tata_Bank_ALM_2025.md" --chunk 400
    python tools/units.py "01_sources/fixed_income_during" --dir
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

PRESETS = {
    # "## LCR40 Cash inflows and outflows" -> id LCR40
    "basel": r"^##\s+(?P<id>[A-Z]{3}\d{2,3})\b\s*(?P<title>.*)$",
    # "## Chương II …" -> C2 ; "### Mục 5 …" -> C2-M5 ; "## Phụ lục I …" -> PL1
    "vn": r"^#{1,4}\s+\**\s*(?P<kind>Chương|Mục|Phụ lục)\s+(?P<id>[IVXLC]+|\d+)\b\.?\s*(?P<title>.*)$",
    # "## CHAPTER  7 Liquidity" -> ch7 (sách convert bằng docling)
    "chapter": r"^#{1,4}\s+(?:CHAPTER|Chapter)\s+(?P<id>\d+)\b\s*(?P<title>.*)$",
}

HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}


def roman_to_int(s: str) -> int:
    total, prev = 0, 0
    for ch in reversed(s.upper()):
        v = ROMAN[ch]
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    return total


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def iter_headings(lines: list[str]):
    """(line_no 1-based, level, text) cho heading nằm ngoài code fence."""
    in_fence = False
    for i, line in enumerate(lines, 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line)
        if m:
            yield i, len(m.group(1)), m.group(2).strip("* ").strip()


def pick_level(lines: list[str], lo: int = 3, hi: int = 60) -> int:
    counts: dict[int, int] = {}
    for _, level, _ in iter_headings(lines):
        counts[level] = counts.get(level, 0) + 1
    for level in sorted(counts):
        if lo <= counts[level] <= hi:
            return level
    if not counts:
        return 0
    # không level nào nằm trong khoảng: chọn level có số heading gần khoảng nhất
    return min(counts, key=lambda lv: min(abs(counts[lv] - lo), abs(counts[lv] - hi)))


def find_starts(lines: list[str], preset: str, pattern: str | None, level: int | None):
    """Trả về list (line_no, unit_id, heading)."""
    starts = []
    if pattern or preset in PRESETS:
        rx = re.compile(pattern or PRESETS[preset])
        in_fence = False
        chapter = 0
        for i, line in enumerate(lines, 1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = rx.match(line)
            if not m:
                continue
            gd = m.groupdict()
            raw_id = gd.get("id") or f"u{len(starts) + 1:02d}"
            title = (gd.get("title") or "").strip("* ").strip()
            if preset == "vn" and not pattern:
                n = int(raw_id) if raw_id.isdigit() else roman_to_int(raw_id)
                kind = gd.get("kind")
                if kind == "Chương":
                    chapter, raw_id = n, f"C{n}"
                elif kind == "Mục":
                    raw_id = f"C{chapter}-M{n}"
                    # header Chương chỉ có tiêu đề, nội dung nằm trong các Mục -> bỏ unit Chương
                    if starts and starts[-1][1] == f"C{chapter}" and i - starts[-1][0] <= 4:
                        starts.pop()
                else:
                    raw_id = f"PL{n}"
            elif preset == "chapter" and not pattern:
                raw_id = f"ch{int(raw_id)}"
            starts.append((i, raw_id, title or line.strip("# *")))
        return starts

    lv = level or pick_level(lines)
    for i, hl, text in iter_headings(lines):
        if hl == lv:
            starts.append((i, f"u{len(starts) + 1:02d}", text))
    return starts


def chunk_starts(lines: list[str], size: int):
    """Gộp heading (mọi level) thành unit ~size dòng; unit mới chỉ bắt đầu tại heading."""
    starts = []
    for i, _, text in iter_headings(lines):
        if not starts or i - starts[-1][0] >= size:
            starts.append((i, f"u{len(starts) + 1:02d}", text))
    return starts


def build_units(lines: list[str], starts):
    units = []
    if starts and starts[0][0] > 6:
        units.append(("preamble", "Phần mở đầu (trước unit đầu tiên)", 1, starts[0][0] - 1))
    for k, (ln, uid, title) in enumerate(starts):
        end = starts[k + 1][0] - 1 if k + 1 < len(starts) else len(lines)
        units.append((uid, title, ln, end))
    # id trùng (vd 2 heading cùng số chương) -> thêm hậu tố
    seen: dict[str, int] = {}
    out = []
    for uid, title, a, b in units:
        seen[uid] = seen.get(uid, 0) + 1
        if seen[uid] > 1:
            uid = f"{uid}-{seen[uid]}"
        out.append((uid, title, a, b))
    return out


def natural_key(p: Path):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]


def slug(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.UNICODE)
    return re.sub(r"[\s_]+", "-", s).strip("-")[:60]


def emit_unit(uid: str, title: str, a: int, b: int, extra: str = "") -> str:
    return (f"    - {{id: {json.dumps(uid, ensure_ascii=False)}, "
            f"heading: {json.dumps(title[:120], ensure_ascii=False)}, "
            f"lines: [{a}, {b}]{extra}, status: pending}}")


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="file .md, hoặc thư mục khi dùng --dir")
    ap.add_argument("--preset", choices=["basel", "vn", "chapter", "book", "auto"], default="auto")
    ap.add_argument("--chunk", type=int, help="gộp heading thành unit ~N dòng (sách có cấu trúc heading kém)")
    ap.add_argument("--pattern", help="regex tuỳ chỉnh; group (?P<id>) và (?P<title>) nếu có")
    ap.add_argument("--level", type=int, help="ép heading level (preset book/auto)")
    ap.add_argument("--dir", action="store_true", help="collection: mỗi file .md trong thư mục = 1 unit")
    ap.add_argument("--add", action="append", default=[], metavar="LINE:ID",
                    help="thêm điểm bắt đầu unit mà preset bỏ sót, vd 2173:ch4 (heading chương bị convert mất)")
    args = ap.parse_args()

    p = Path(args.path)
    if not p.exists():
        print(f"không tìm thấy: {p}", file=sys.stderr)
        return 2
    print("\n".join(render(p, args.preset, args.pattern, args.level, args.chunk, args.dir, args.add)))
    return 0


def render(p: Path, preset="auto", pattern=None, level=None, chunk=None, is_dir=False, add=()) -> list[str]:
    """Các dòng YAML (thụt 2 space) mô tả hash + units; dùng chung cho CLI và tools/registry.py."""
    out = []
    if is_dir:
        files = sorted((f for f in p.iterdir() if f.suffix.lower() == ".md"), key=natural_key)
        # bỏ tiền tố chung của tên file (vd "Fixed Income - Alexander During-") để id ngắn
        prefix = os.path.commonprefix([f.stem for f in files]) if len(files) > 1 else ""
        out += [f"  path: {p.as_posix()}", f"  files: {len(files)}", "  units:"]
        for f in files:
            n = len(read_lines(f))
            rest = f.stem[len(prefix):]
            uid = (f"f{rest}" if rest.isdigit() else slug(rest)) or slug(f.stem)
            extra = f", file: {json.dumps(f.name, ensure_ascii=False)}, sha256: {sha256(f)[:16]}"
            out.append(emit_unit(uid, f.stem, 1, n, extra))
        return out

    lines = read_lines(p)
    starts = chunk_starts(lines, chunk) if chunk else find_starts(lines, preset, pattern, level)
    for spec in add or ():
        ln, uid = spec.split(":", 1)
        ln = int(ln)
        title = lines[ln - 1].strip("# *") if 0 < ln <= len(lines) else uid
        starts = sorted([s for s in starts if s[0] != ln] + [(ln, uid, title)])
    units = build_units(lines, starts)
    out += [f"  sha256: {sha256(p)}", f"  bytes: {p.stat().st_size}", f"  lines_total: {len(lines)}", "  units:"]
    if not units:
        out.append(emit_unit("all", p.stem, 1, len(lines)))
    for uid, title, a, b in units:
        out.append(emit_unit(uid, title, a, b))
    return out


if __name__ == "__main__":
    sys.exit(main())
