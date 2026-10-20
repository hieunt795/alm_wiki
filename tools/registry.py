#!/usr/bin/env python3
"""Thao tác với source registry `03_meta/sources.yaml` — dùng bởi skill /register và /ingest.

Chỉ ĐỌC `01_sources/`. Chỉ GHI `03_meta/sources.yaml` (lệnh add, mark, resplit).

    python tools/registry.py show  <source_id>                 # metadata + units + trạng thái
    python tools/registry.py read  <source_id> <unit> [--from N] [--to M] [--raw]
                                                              # in nội dung unit, có số dòng gốc, bỏ URL
    python tools/registry.py check <path>                      # path/hash đã có trong registry chưa
    python tools/registry.py mark  <source_id> <unit>... [--status done|skipped|pending]
    python tools/registry.py add   --id src-x --path <md> --tier T4 --domains alm,basel \
                                   --issuer "..." [--title ..] [--number ..] [--doc-status final]
                                   [--published YYYY-MM-DD] [--effective YYYY-MM-DD]
                                   [--original <pdf>]... [--meta <json>] [--extractor ..]
                                   [--conversion ok|partial] [--issue "loc|type|note"]...
                                   [--notes ".."] [--preset vn|basel|chapter|auto] [--chunk N]
                                   [--level N] [--pattern RE] [--add LINE:ID]... [--dir] [--dry-run]
    python tools/registry.py resplit <source_id> [--preset ..] [--pattern RE] [--level N] [--chunk N]
                                   [--add LINE:ID]... [--dry-run]
                                                              # tách lại unit của entry đã có; giữ status/ngày
                                                              # ingest của unit không đổi ranh giới
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "03_meta" / "sources.yaml"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import units as U  # noqa: E402  (tools/units.py)

MD_LINK = re.compile(r"\[([^\]]*)\]\((?:https?://|#)[^)]*\)")


def load() -> dict:
    return yaml.safe_load(REG.read_text(encoding="utf-8")) or {"sources": []}


def find(reg: dict, sid: str) -> dict:
    for e in reg.get("sources") or []:
        if e.get("id") == sid:
            return e
    raise SystemExit(f"không có source_id '{sid}' trong registry (xem: python tools/registry.py check <path>)")


def as_list(v):
    return [] if v in (None, "") else (v if isinstance(v, list) else [v])


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------- show
def cmd_show(a):
    e = find(load(), a.source_id)
    meta = {k: v for k, v in e.items() if k not in ("units", "sha256")}
    print(yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=160).rstrip())
    us = e.get("units") or []
    done = sum(1 for u in us if u.get("status") == "done")
    print(f"units: {done}/{len(us)} done")
    for u in us:
        a_, b_ = u.get("lines", [0, 0])
        print(f"  {u.get('status', '?'):8} {u['id']:<12} [{a_}-{b_}] {b_ - a_ + 1:>5} dòng  {u.get('heading', '')[:70]}")


# ---------------------------------------------------------------- read
def cmd_read(a):
    e = find(load(), a.source_id)
    unit = next((u for u in e.get("units") or [] if u["id"] == a.unit), None)
    if unit is None:
        raise SystemExit(f"unit '{a.unit}' không có trong {a.source_id}")
    base = Path(as_list(e["path"])[0])
    path = ROOT / base / unit["file"] if unit.get("file") else ROOT / base
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    lo, hi = unit["lines"]
    lo, hi = max(lo, a.start or lo), min(hi, a.end or hi)
    print(f"# {a.source_id} · {a.unit} · {path.relative_to(ROOT).as_posix()} · dòng {lo}-{hi}")
    for i in range(lo, hi + 1):
        line = lines[i - 1]
        if not a.raw:
            line = MD_LINK.sub(r"\1", line)        # bỏ URL, giữ chữ của link -> giảm token
        print(f"{i:>6}\t{line}")


# ---------------------------------------------------------------- check
def cmd_check(a):
    p = Path(a.path)
    p = p if p.is_absolute() else ROOT / p
    if not p.exists():
        raise SystemExit(f"không tìm thấy: {p}")
    rel = p.resolve().relative_to(ROOT.resolve()).as_posix()
    h = sha256(p) if p.is_file() else None
    hits = []
    for e in load().get("sources") or []:
        if rel in [str(x) for x in as_list(e.get("path"))]:
            hits.append(f"PATH  đã đăng ký: {e['id']}")
        if h and e.get("sha256") == h:
            hits.append(f"HASH  trùng nội dung với: {e['id']}")
        if h and any(u.get("sha256") and h.startswith(str(u["sha256"])) for u in e.get("units") or []):
            hits.append(f"HASH  trùng một file trong collection: {e['id']}")
    print(f"path: {rel}\nsha256: {h or '(thư mục)'}")
    print("\n".join(hits) if hits else "chưa có trong registry")
    return 1 if hits else 0


# ---------------------------------------------------------------- mark
def cmd_mark(a):
    text = REG.read_text(encoding="utf-8").splitlines()
    start = next((i for i, l in enumerate(text) if re.match(rf"^\s*- id: {re.escape(a.source_id)}\s*$", l)), None)
    if start is None:
        raise SystemExit(f"không có source_id '{a.source_id}'")
    end = next((i for i in range(start + 1, len(text)) if re.match(r"^\s*- id: ", text[i])), len(text))
    today = dt.date.today().isoformat()
    todo = set(a.units)
    for i in range(start, end):
        m = re.match(r'^(\s*- \{id: "([^"]+)".*?), status: \w+(?:, ingested: [\d-]+)?\}$', text[i])
        if m and m.group(2) in todo:
            tail = f", status: {a.status}" + (f", ingested: {today}" if a.status == "done" else "")
            text[i] = m.group(1) + tail + "}"
            todo.discard(m.group(2))
    if todo:
        raise SystemExit(f"không tìm thấy unit: {', '.join(sorted(todo))}")
    REG.write_text("\n".join(text) + "\n", encoding="utf-8")
    yaml.safe_load(REG.read_text(encoding="utf-8"))          # đảm bảo vẫn parse được
    print(f"{a.source_id}: {', '.join(a.units)} -> {a.status}")


# ---------------------------------------------------------------- add
def cmd_add(a):
    reg = load()
    if any(e.get("id") == a.id for e in reg.get("sources") or []):
        raise SystemExit(f"id '{a.id}' đã tồn tại")
    p = ROOT / a.path
    if not p.exists():
        raise SystemExit(f"không tìm thấy: {a.path}")
    if p.is_file():
        h = sha256(p)
        dup = [e["id"] for e in reg.get("sources") or [] if e.get("sha256") == h]
        if dup:
            raise SystemExit(f"nội dung trùng (sha256) với: {', '.join(dup)} — không thêm")
    for x in [*a.original, a.meta]:
        if x and not (ROOT / x).exists():
            raise SystemExit(f"không tìm thấy file: {x}")
    issues = []
    for s in a.issue:
        loc, typ, note = (s.split("|", 2) + ["", ""])[:3]
        issues.append({"loc": loc, "type": typ, "note": note})
    entry = {
        "id": a.id, "title": a.title or p.stem, "path": a.path,
        "original": (a.original[0] if len(a.original) == 1 else a.original) or None,
        "meta": a.meta, "issuer": a.issuer,
        **({"number": a.number} if a.number else {}),
        "tier": a.tier, "doc_status": a.doc_status, "domains": a.domains.split(","),
        "published": a.published, "effective": a.effective, "extractor": a.extractor,
        "conversion": {"status": a.conversion, "issues": issues},
        **({"notes": a.notes} if a.notes else {}),
        "registered": dt.date.today().isoformat(),
    }
    block = ["  " + l for l in yaml.safe_dump([entry], allow_unicode=True, sort_keys=False, width=200).rstrip().splitlines()]
    block += ["  " + l for l in U.render(p, a.preset, a.pattern, a.level, a.chunk, a.dir, a.add)
              if not l.startswith(("  path:", "  files:"))]
    if a.dry_run:
        print("\n".join(block))
        return
    text = REG.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + "\n".join(block) + "\n"
    yaml.safe_load(text)                                       # validate trước khi ghi
    REG.write_text(text, encoding="utf-8")
    n = sum(1 for l in block if l.strip().startswith("- {id:"))
    print(f"đã thêm {a.id}: {n} unit")


# ---------------------------------------------------------------- resplit
UNIT_LINE = re.compile(r'^\s*- \{id: "([^"]+)".*?lines: \[(\d+), (\d+)\].*?status: (\w+)')


def cmd_resplit(a):
    e = find(load(), a.source_id)
    old = e.get("units") or []
    if any(u.get("file") for u in old):
        raise SystemExit("resplit không áp dụng cho collection (--dir)")
    p = ROOT / as_list(e["path"])[0]
    if sha256(p) != e.get("sha256"):
        raise SystemExit("sha256 của raw khác registry — raw đã đổi, không resplit (cần đăng ký lại)")

    text = REG.read_text(encoding="utf-8").splitlines()
    start = next(i for i, l in enumerate(text) if re.match(rf"^\s*- id: {re.escape(a.source_id)}\s*$", l))
    end = next((i for i in range(start + 1, len(text)) if re.match(r"^\s*- id: ", text[i])), len(text))
    ustart = next(i for i in range(start, end) if text[i].strip() == "units:") + 1
    uend = ustart
    while uend < end and UNIT_LINE.match(text[uend]):
        uend += 1
    cur = {m.group(1): (text[i], (int(m.group(2)), int(m.group(3))), m.group(4))
           for i in range(ustart, uend) if (m := UNIT_LINE.match(text[i]))}
    indent = re.match(r"^\s*", text[ustart]).group(0) if uend > ustart else "      "

    new_lines, kept, changed, added, conflicts = [], [], [], [], []
    for l in U.render(p, a.preset, a.pattern, a.level, a.chunk, False, a.add):
        m = UNIT_LINE.match(l)
        if not m:
            continue
        uid, rng = m.group(1), (int(m.group(2)), int(m.group(3)))
        if uid in cur and cur[uid][1] == rng:
            new_lines.append(cur[uid][0]); kept.append(uid)
        else:
            if uid in cur:
                changed.append(f"{uid} {list(cur[uid][1])} -> {list(rng)}")
                if cur[uid][2] in ("done", "skipped"):
                    conflicts.append(f"{uid} ({cur[uid][2]}) đổi ranh giới")
            else:
                added.append(f"{uid} {list(rng)}")
            new_lines.append(indent + l.strip())
    new_ids = {UNIT_LINE.match(l).group(1) for l in new_lines}
    removed = [uid for uid in cur if uid not in new_ids]
    conflicts += [f"{uid} ({cur[uid][2]}) bị mất" for uid in removed if cur[uid][2] in ("done", "skipped")]

    print(f"{a.source_id}: giữ {len(kept)} · đổi {len(changed)} · thêm {len(added)} · bỏ {len(removed)}")
    for label, xs in (("đổi", changed), ("thêm", added), ("bỏ", removed)):
        for x in xs[:10]:
            print(f"  {label}: {x}")
        if len(xs) > 10:
            print(f"  {label}: … và {len(xs) - 10} unit nữa (tham số tách có thể khác lần đăng ký)")
    if conflicts:
        raise SystemExit("dừng — unit đã ingest/skipped bị ảnh hưởng: " + "; ".join(conflicts))
    if not (changed or added or removed):
        print("không có thay đổi")
        return
    if a.dry_run:
        return
    out = text[:ustart] + new_lines + text[uend:]
    yaml.safe_load("\n".join(out))                            # validate trước khi ghi
    REG.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("đã ghi registry")


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)

    s = sp.add_parser("show"); s.add_argument("source_id"); s.set_defaults(fn=cmd_show)
    s = sp.add_parser("read"); s.add_argument("source_id"); s.add_argument("unit")
    s.add_argument("--from", dest="start", type=int); s.add_argument("--to", dest="end", type=int)
    s.add_argument("--raw", action="store_true", help="giữ nguyên URL"); s.set_defaults(fn=cmd_read)
    s = sp.add_parser("check"); s.add_argument("path"); s.set_defaults(fn=cmd_check)
    s = sp.add_parser("mark"); s.add_argument("source_id"); s.add_argument("units", nargs="+")
    s.add_argument("--status", choices=["done", "skipped", "pending"], default="done"); s.set_defaults(fn=cmd_mark)

    s = sp.add_parser("add")
    for f in ("--id", "--path", "--tier", "--domains", "--issuer"):
        s.add_argument(f, required=True)
    for f in ("--title", "--number", "--published", "--effective", "--meta", "--extractor", "--notes", "--pattern"):
        s.add_argument(f)
    s.add_argument("--doc-status", default="final", choices=["final", "consultative", "draft"])
    s.add_argument("--original", action="append", default=[])
    s.add_argument("--conversion", default="ok", choices=["ok", "partial"])
    s.add_argument("--issue", action="append", default=[], help='"loc|type|note"')
    s.add_argument("--preset", default="auto", choices=["basel", "vn", "chapter", "book", "auto"])
    s.add_argument("--chunk", type=int); s.add_argument("--level", type=int)
    s.add_argument("--dir", action="store_true"); s.add_argument("--dry-run", action="store_true")
    s.add_argument("--add", action="append", default=[], metavar="LINE:ID", help="điểm bắt đầu unit bị preset bỏ sót")
    s.set_defaults(fn=cmd_add)

    s = sp.add_parser("resplit"); s.add_argument("source_id")
    s.add_argument("--preset", default="auto", choices=["basel", "vn", "chapter", "book", "auto"])
    s.add_argument("--pattern"); s.add_argument("--chunk", type=int); s.add_argument("--level", type=int)
    s.add_argument("--add", action="append", default=[], metavar="LINE:ID", help="điểm bắt đầu unit mới")
    s.add_argument("--dry-run", action="store_true")
    s.set_defaults(fn=cmd_resplit)

    a = ap.parse_args()
    return a.fn(a) or 0


if __name__ == "__main__":
    sys.exit(main())
