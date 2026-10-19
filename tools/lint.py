#!/usr/bin/env python3
"""Lint deterministic cho ALM Wiki (đặc tả v2 §B.4).

Đọc enum từ khối ```yaml taxonomy``` trong `03_meta/taxonomy.md` và registry
`03_meta/sources.yaml`. Chỉ đọc, không sửa file nào.

    python tools/lint.py            # báo cáo dạng text
    python tools/lint.py --json     # báo cáo JSON
    python tools/lint.py --wiki <dir> --meta <dir>

Exit code: 0 = không có ERROR (WARN không làm fail), 1 = có ERROR, 2 = lỗi cấu hình.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

from check_math import scan as scan_math

ROOT = Path(__file__).resolve().parent.parent
NAV = {"index", "log", "overview",           # trang điều hướng: không kiểm tra schema
       "domain-macro", "domain-product", "domain-alm", "domain-basel", "domain-vn-reg"}
REL_KEYS = {"type", "to", "cite", "direction", "regime", "confidence"}   # field hợp lệ của một relation
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*(\n|\Z)", re.S)
LINK = re.compile(r"\[\[([^\]\|#\\]*)(#[^\]\|\\]*)?(\\?\|[^\]]*)?\]\]")   # `\|` = alias trong bảng (Obsidian)
FENCE_BLOCK = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")
COMMENT = re.compile(r"<!--.*?-->", re.S)
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.M)
QUOTE = re.compile(r'^[ \t]*>\s*"(.*)"\s*$', re.M)   # kể cả blockquote thụt lề trong list item
MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
FOOTNOTE_REF = re.compile(r"\[\^[^\]]*\]")
STUB = re.compile(r"^> \[!note\] Node stub[^\n]*\n((?:>[^\n]*(?:\n|\Z))*)", re.M)   # callout stub + các dòng tiếp
STUB_PLAN = re.compile(r"^> Hoàn thiện bằng:.*/ingest", re.M)
STUB_MARK = re.compile(r"\*stub\*", re.I)                     # đánh dấu stub trong dòng index
BLOCK_REF = re.compile(r"\[\[src-[^\]#]+#\^[a-z0-9-]+\]\]")
_raw_cache: dict[Path, str] = {}


def norm_text(s: str) -> str:
    """Chuẩn hoá để so trích dẫn với raw: bỏ link URL, footnote, emphasis, list marker, khoảng trắng."""
    s = MD_LINK.sub(r"\1", s)
    s = FOOTNOTE_REF.sub("", s)
    s = re.sub(r"(?m)^\s*(?:[-*+]\s+|>\s*)+", "", s)
    s = s.replace("<br>", " ").replace("\\", "")
    s = re.sub(r"[*_`]", "", s)
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def raw_text(path: Path) -> str:
    if path not in _raw_cache:
        _raw_cache[path] = norm_text(path.read_text(encoding="utf-8", errors="replace"))
    return _raw_cache[path]


class Report:
    def __init__(self):
        self.items: list[dict] = []

    def add(self, level: str, path: str, check: str, msg: str):
        self.items.append({"level": level, "path": path, "check": check, "msg": msg})

    def error(self, *a):
        self.add("ERROR", *a)

    def warn(self, *a):
        self.add("WARN", *a)

    def info(self, *a):
        self.add("INFO", *a)

    def count(self, level):
        return sum(1 for i in self.items if i["level"] == level)


def load_taxonomy(meta: Path) -> dict:
    text = (meta / "taxonomy.md").read_text(encoding="utf-8")
    m = re.search(r"```yaml taxonomy\s*\n(.*?)```", text, re.S)
    if not m:
        raise SystemExit("taxonomy.md thiếu khối ```yaml taxonomy```")
    return yaml.safe_load(m.group(1))


def to_date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if isinstance(v, str) and v.strip():
        try:
            return dt.date.fromisoformat(v.strip()[:10])
        except ValueError:
            return None
    return None


def as_list(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]


def link_targets(value) -> list[tuple[str, str]]:
    """Trích (target, anchor) từ mọi chuỗi [[...]] trong một giá trị frontmatter."""
    out = []
    if isinstance(value, str):
        for m in LINK.finditer(value):
            out.append((m.group(1).strip(), (m.group(2) or "")[1:]))
    elif isinstance(value, list):
        for x in value:
            out += link_targets(x)
    elif isinstance(value, dict):
        for x in value.values():
            out += link_targets(x)
    return out


def strip_noise(body: str) -> str:
    body = COMMENT.sub("", body)
    body = FENCE_BLOCK.sub("", body)
    return INLINE_CODE.sub("", body)


class Note:
    def __init__(self, path: Path, wiki: Path):
        self.path = path
        self.rel = path.relative_to(wiki.parent).as_posix()
        self.id = path.stem
        self.folder = path.parent.name if path.parent != wiki else ""
        text = path.read_text(encoding="utf-8")
        m = FM.match(text)
        self.fm_error = None
        self.fm: dict = {}
        if m:
            try:
                self.fm = yaml.safe_load(m.group(1)) or {}
                if not isinstance(self.fm, dict):
                    self.fm_error, self.fm = "frontmatter không phải mapping", {}
            except yaml.YAMLError as e:
                self.fm_error = f"YAML lỗi: {str(e).splitlines()[0]}"
            self.body = text[m.end():]
        else:
            self.body = text
        self.clean = strip_noise(self.body)
        self.block_ids = set(re.findall(r"\s\^([a-z0-9-]+)\s*$", self.body, re.M))
        self.headings = {h.strip().lower() for h in HEADING.findall(self.body)}

    @property
    def type(self):
        return self.fm.get("type")

    @property
    def stub(self) -> str | None:
        """Nội dung callout `> [!note] Node stub` (rỗng nếu chỉ có dòng tiêu đề), None nếu không phải stub."""
        m = STUB.search(self.body)
        return m.group(1) if m else None


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wiki", default=str(ROOT / "02_wiki"))
    ap.add_argument("--meta", default=str(ROOT / "03_meta"))
    ap.add_argument("--root", default=str(ROOT), help="vault root để kiểm tra path trong registry")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--today", help="YYYY-MM-DD, mặc định hôm nay (để test)")
    args = ap.parse_args()

    wiki, meta, root = Path(args.wiki), Path(args.meta), Path(args.root)
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    try:
        tax = load_taxonomy(meta)
    except FileNotFoundError:
        print(f"không tìm thấy {meta / 'taxonomy.md'}", file=sys.stderr)
        return 2
    r = Report()

    domains = set(tax["domains"])
    types = tax["types"]                       # type -> folder
    relations = set(tax["relations"])
    req = tax["required_fields"]

    # ---------- load notes ----------
    notes: dict[str, Note] = {}
    for p in sorted(wiki.rglob("*.md")):
        n = Note(p, wiki)
        key = n.id.lower()
        if key in notes:
            r.error(n.rel, "id-duplicate", f"trùng tên file với {notes[key].rel}")
            continue
        notes[key] = n

    aliases: dict[str, str] = {}
    for n in notes.values():
        for a in as_list(n.fm.get("aliases")):
            k = str(a).strip().lower()
            if not k:
                continue
            if k in notes and notes[k] is not n:
                r.warn(n.rel, "alias-collision", f"alias '{a}' trùng tên node {notes[k].rel}")
            elif k in aliases and aliases[k] != n.id:
                r.warn(n.rel, "alias-collision", f"alias '{a}' trùng alias của {aliases[k]}")
            aliases[k] = n.id

    # ---------- công thức LaTeX/KaTeX (tools/check_math.py) ----------
    for n in notes.values():
        for i in scan_math(n.path.read_text(encoding="utf-8")):
            if i["level"] != "INFO":
                r.add(i["level"], n.rel, f"math-{i['code']}", f"dòng {i['line']}: {i['msg']}")

    # ---------- registry ----------
    registry: dict[str, dict] = {}
    reg_path = meta / "sources.yaml"
    if reg_path.exists():
        try:
            reg = yaml.safe_load(reg_path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            r.error("03_meta/sources.yaml", "registry-yaml", str(e).splitlines()[0])
            reg = {}
        for e in reg.get("sources", []) or []:
            sid = e.get("id")
            if not sid:
                r.error("03_meta/sources.yaml", "registry-id", f"entry thiếu id: {e.get('title')}")
                continue
            if sid in registry:
                r.error("03_meta/sources.yaml", "registry-id", f"id trùng: {sid}")
            registry[sid] = e
            for key in ("path", "original", "meta"):
                for pth in as_list(e.get(key)):
                    if pth and not (root / pth).exists():
                        r.error("03_meta/sources.yaml", "registry-path", f"{sid}.{key} không tồn tại: {pth}")
            if e.get("tier") not in tax["tiers"]:
                r.error("03_meta/sources.yaml", "registry-enum", f"{sid}: tier '{e.get('tier')}' không hợp lệ")
            for d in as_list(e.get("domains")):
                if d not in domains:
                    r.error("03_meta/sources.yaml", "registry-enum", f"{sid}: domain '{d}' không hợp lệ")
            reg_date = to_date(e.get("registered"))
            pending = [u for u in e.get("units") or [] if u.get("status") == "pending"]
            if reg_date and pending and (today - reg_date).days > 60:
                r.info("03_meta/sources.yaml", "units-backlog", f"{sid}: {len(pending)} unit pending > 60 ngày")
    else:
        r.warn("03_meta/sources.yaml", "registry-missing", "chưa có registry")

    # ---------- per-note checks ----------
    inbound: dict[str, set[str]] = {k: set() for k in notes}

    def resolve(target: str):
        t = target.split("/")[-1]
        t = t[:-3] if t.lower().endswith(".md") else t
        return notes.get(t.strip().lower())

    def check_link(n: Note, target: str, anchor: str, where: str):
        if not target:                        # [[#heading]] trong cùng note
            return
        if "/" in target and (root / target).exists():
            return                            # link thẳng tới file (vd raw) — cho phép
        dst = resolve(target)
        if dst is None:
            hint = f" (đây là alias của [[{aliases[target.lower()]}]])" if target.lower() in aliases else ""
            r.error(n.rel, "broken-link", f"{where}: [[{target}]] không tồn tại{hint}")
            return
        if dst is not n and n.id not in NAV:
            inbound[dst.id.lower()].add(n.id)
        if anchor.startswith("^"):
            if anchor[1:] not in dst.block_ids:
                r.error(n.rel, "broken-block-ref", f"{where}: [[{target}#{anchor}]] — block-id không có trong {dst.rel}")
        elif anchor and anchor.strip().lower() not in dst.headings:
            r.warn(n.rel, "broken-heading-ref", f"{where}: [[{target}#{anchor}]] — heading không tồn tại")

    for n in notes.values():
        # links trong thân bài
        for m in LINK.finditer(n.clean):
            check_link(n, m.group(1).strip(), (m.group(2) or "")[1:], "body")
        # links trong frontmatter
        for t, a in link_targets(n.fm):
            check_link(n, t, a, "frontmatter")

        if n.id in NAV:
            continue
        if n.fm_error:
            r.error(n.rel, "frontmatter", n.fm_error)
            continue
        if not n.fm:
            r.error(n.rel, "frontmatter", "thiếu frontmatter")
            continue

        t = n.type
        if t not in types:
            r.error(n.rel, "enum-type", f"type '{t}' không hợp lệ")
            continue
        if n.folder != types[t]:
            r.error(n.rel, "folder", f"type '{t}' phải nằm trong 02_wiki/{types[t]}/")

        need = list(req["all"]) + (req.get(t) or []) + ([] if t == "source" else req["knowledge"])
        for f in need:
            if n.fm.get(f) in (None, "", []):
                r.error(n.rel, "required-field", f"thiếu '{f}'")

        doms = as_list(n.fm.get("domains"))
        for d in doms:
            if d not in domains:
                r.error(n.rel, "enum-domain", f"domain '{d}' không hợp lệ")
        for field, allowed in (("status", tax["status"]), ("maturity", tax["maturity"]),
                               ("doc_status", tax["doc_status"]), ("origin", tax["origin"]),
                               ("jurisdiction", tax["jurisdiction"])):
            v = n.fm.get(field)
            if v not in (None, "") and v not in allowed:
                r.error(n.rel, f"enum-{field}", f"{field} '{v}' không hợp lệ")
        if t == "source":
            if n.fm.get("tier") not in tax["tiers"]:
                r.error(n.rel, "enum-tier", f"tier '{n.fm.get('tier')}' không hợp lệ")
            sid = n.fm.get("source_id")
            if registry and sid not in registry:
                r.error(n.rel, "registry", f"source_id '{sid}' không có trong sources.yaml")
            elif sid in registry:
                reg_units = {u.get("id"): u.get("status") for u in registry[sid].get("units") or []}
                for u in as_list(n.fm.get("units_done")):
                    if u not in reg_units:
                        r.error(n.rel, "registry", f"unit '{u}' không có trong registry của {sid}")
                    elif reg_units[u] != "done":
                        r.warn(n.rel, "registry", f"unit '{u}' đã ingest nhưng registry chưa đánh dấu done")
            raw_path = root / str(n.fm.get("raw") or "")
            if n.fm.get("raw") and not raw_path.exists():
                r.error(n.rel, "raw-path", f"raw không tồn tại: {n.fm['raw']}")
            elif n.fm.get("raw") and raw_path.is_file():
                # mọi trích dẫn nguyên văn phải tìm thấy trong raw (cho phép rút gọn bằng "…")
                haystack = raw_text(raw_path)
                for q in QUOTE.findall(n.body):
                    for frag in q.split("…"):
                        f = norm_text(frag).strip(" .,;:")
                        if len(f) >= 8 and f not in haystack:
                            r.error(n.rel, "quote-not-found", f"không tìm thấy trong raw: \"{f[:80]}…\"")

        # sources phải trỏ tới source note
        for s in as_list(n.fm.get("sources")):
            for target, _ in link_targets(s) or [(str(s), "")]:
                dst = resolve(target)
                if dst is not None and dst.type != "source":
                    r.error(n.rel, "sources", f"[[{target}]] không phải source note")

        # relations
        for rel in as_list(n.fm.get("relations")):
            if not isinstance(rel, dict):
                r.error(n.rel, "relation", f"relation phải là mapping: {rel}")
                continue
            if rel.get("type") not in relations:
                r.error(n.rel, "enum-relation", f"relation type '{rel.get('type')}' không hợp lệ")
            if not link_targets(rel.get("to")):
                r.error(n.rel, "relation", f"relation thiếu 'to' dạng [[...]]: {rel}")
            extra = set(rel) - REL_KEYS
            if extra:
                r.error(n.rel, "relation", f"key không hợp lệ {sorted(extra)}: {rel}")
            if rel.get("direction") not in (None, "+", "-"):
                r.error(n.rel, "relation", f"direction phải là '+' hoặc '-': {rel}")
            if rel.get("regime") not in (None, *tax["regimes"]):
                r.error(n.rel, "relation", f"regime '{rel.get('regime')}' không có trong taxonomy")
            if (rel.get("direction") or rel.get("regime")) and rel.get("type") != "drives":
                r.error(n.rel, "relation", f"direction/regime chỉ dùng với drives: {rel}")
            if rel.get("cite") is not None:
                cites = link_targets(rel.get("cite"))
                if not cites:
                    r.error(n.rel, "relation", f"cite phải dạng [[src-…#^block-id]]: {rel}")
                for t, a in cites:
                    dst = resolve(t)
                    if not a.startswith("^") or (dst is not None and dst.type != "source"):
                        r.error(n.rel, "relation", f"cite phải trỏ tới block-id trong source note: [[{t}#{a}]]")

        # temporal
        vt = to_date(n.fm.get("valid_to"))
        if vt and vt < today and n.fm.get("status") == "active":
            r.error(n.rel, "temporal", f"valid_to {vt} đã qua mà status vẫn active")
        vf = to_date(n.fm.get("valid_from"))
        if vf and vt and vf > vt:
            r.error(n.rel, "temporal", "valid_from > valid_to")
        if n.fm.get("status") == "superseded" and not n.fm.get("superseded_by"):
            r.warn(n.rel, "supersession", "status superseded nhưng thiếu superseded_by")
        if doms and doms[0] == "macro":
            ao = to_date(n.fm.get("as_of"))
            months = tax.get("macro_stale_months", 6)
            if ao and (today - ao).days > months * 30.5:
                r.warn(n.rel, "macro-stale", f"as_of {ao} cũ hơn {months} tháng")

    # supersession đối xứng
    for n in notes.values():
        for t, _ in link_targets(n.fm.get("superseded_by")):
            dst = resolve(t)
            if dst and n.id.lower() not in {x.lower() for x, _ in link_targets(dst.fm.get("supersedes"))}:
                r.warn(n.rel, "supersession", f"superseded_by [[{t}]] nhưng {dst.rel} không khai báo supersedes [[{n.id}]]")
        for t, _ in link_targets(n.fm.get("supersedes")):
            dst = resolve(t)
            if dst and n.id.lower() not in {x.lower() for x, _ in link_targets(dst.fm.get("superseded_by"))}:
                r.warn(n.rel, "supersession", f"supersedes [[{t}]] nhưng {dst.rel} không khai báo superseded_by [[{n.id}]]")

    # orphan (link từ index/log/overview không tính)
    for key, n in notes.items():
        if n.id in NAV:
            continue
        if not inbound[key]:
            r.warn(n.rel, "orphan", "không có node nào link tới")

    # index phải liệt kê mọi node
    idx = notes.get("index")
    if idx:
        listed = {m.group(1).strip().lower() for m in LINK.finditer(idx.clean)}
        for key, n in notes.items():
            if n.id not in NAV and key not in listed:
                r.warn(n.rel, "index", "chưa có trong index.md")

    # stub: callout `> [!note] Node stub` theo định dạng của skill ingest
    index_line: dict[str, str] = {}
    if idx:
        for line in idx.clean.splitlines():
            m = LINK.search(line)
            if m and line.lstrip().startswith("- [["):
                index_line.setdefault(m.group(1).strip().lower(), line)
    stale_days = tax.get("stub_stale_days", 60)
    stubs, ready = 0, 0
    for key, n in notes.items():
        if n.id in NAV or n.type == "source":
            continue
        callout = n.stub
        marked = bool(STUB_MARK.search(index_line.get(key, "")))
        if callout is None:
            if marked:
                r.warn(n.rel, "stub-index", "không còn là stub nhưng dòng index vẫn ghi *stub*")
            continue
        stubs += 1
        ready += bool(BLOCK_REF.search(callout))
        if not STUB_PLAN.search(callout):
            r.warn(n.rel, "stub-plan", "stub thiếu dòng '> Hoàn thiện bằng:' có lệnh /ingest")
        if key in index_line and not marked:
            r.warn(n.rel, "stub-index", "là stub nhưng dòng index chưa ghi *stub*")
        upd = to_date(n.fm.get("updated"))
        if upd and (today - upd).days > stale_days:
            r.info(n.rel, "stub-stale", f"stub chưa cập nhật từ {upd} (> {stale_days} ngày)")
    if stubs:
        r.info(wiki.name, "stub-count", f"{stubs} stub ({ready} có claim sẵn → /ingest --node)")

    # ---------- output ----------
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    r.items.sort(key=lambda i: (order[i["level"]], i["path"], i["check"]))
    summary = {"notes": len(notes), "errors": r.count("ERROR"), "warnings": r.count("WARN"),
               "info": r.count("INFO"), "registry_sources": len(registry)}
    if args.json:
        print(json.dumps({"summary": summary, "items": r.items}, ensure_ascii=False, indent=2))
    else:
        for i in r.items:
            print(f"{i['level']:5} {i['path']}  [{i['check']}] {i['msg']}")
        print(f"\n{summary['notes']} note · {summary['registry_sources']} nguồn trong registry · "
              f"{summary['errors']} error · {summary['warnings']} warning · {summary['info']} info")
    return 1 if summary["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
