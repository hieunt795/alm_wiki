#!/usr/bin/env python3
"""Kiểm tra công thức LaTeX/KaTeX trong 02_wiki (thay cho các script dò công thức cũ, đã xoá 2026-10-18).

Chỉ đọc. `lint.py` import `scan()` nên mọi ERROR ở đây cũng là ERROR của lint.

    python tools/check_math.py                 # quét toàn bộ 02_wiki
    python tools/check_math.py <file.md> ...   # quét file cụ thể
    python tools/check_math.py --json | --info # --info: hiện cả gợi ý văn phong (INFO)

Exit code: 0 = không có ERROR, 1 = có ERROR.

Quy ước bắt buộc (ERROR):
- Display math `$$…$$` đứng riêng: dòng mở bắt đầu bằng `$$`, dòng đóng kết thúc bằng `$$`,
  không có chữ trước/sau (citation đặt ở dòng sau). Không dùng `$$` giữa câu hay trong bảng.
- Trong math: ngoặc `{}` cân, `\\left`/`\\right` và `\\begin`/`\\end` khớp, không có `$` hay `%`
  chưa escape, không double subscript/superscript, `\\text{}` không chứa `_ ^ & # %` chưa escape.
- Bảng: `$` lẻ trong một ô (thường do `|` trong math chưa viết thành `\\|`).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

FM = re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.S)
FENCE_BLOCK = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1[^\n]*", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")
COMMENT = re.compile(r"<!--.*?-->", re.S)
PREFIX = re.compile(r"^[ \t]*(?:>[ \t]?)*[ \t]*")          # thụt lề + blockquote/callout
DD = re.compile(r"(?<!\\)\$\$")
INLINE = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)")
SINGLE = re.compile(r"(?<![\\$])\$(?!\$)")
TEXT_CMDS = ("text", "textbf", "textit", "textrm", "mathrm", "mathbf", "mathit", "operatorname")
VN_CHARS = re.compile(r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
                      r"ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]")
RAW_LATEX = re.compile(r"\\(?:frac|sum|prod|sqrt|times|approx|Delta|le|ge|leq|geq|partial|int|cdot"
                       r"|alpha|beta|gamma|sigma|lambda|text)\b")
LATEX_WORDS = {"min", "max", "sum", "prod", "ln", "log", "exp", "lim", "det", "sin", "cos", "tan",
               "inf", "sup", "arg", "dim", "ker", "deg", "gcd", "var", "cov", "and", "for", "if"}


def mask(text: str) -> str:
    """Thay frontmatter, code block, inline code, comment bằng khoảng trắng (giữ nguyên số dòng/cột)."""
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    for rx in (FM, COMMENT, FENCE_BLOCK, INLINE_CODE):
        text = rx.sub(blank, text)
    return text


def strip_groups(s: str) -> str:
    """Bỏ `\\text{…}` và họ hàng (xử lý ngoặc lồng) để không bắt nhầm chữ thường."""
    return _walk_groups(s)


def text_groups(s: str) -> list[str]:
    out: list[str] = []
    _walk_groups(s, out)
    return out


def _walk_groups(s: str, out: list[str] | None = None) -> str:
    rx = re.compile(r"\\(?:%s)\s*\{" % "|".join(TEXT_CMDS))
    res, i = [], 0
    while (m := rx.search(s, i)):
        res.append(s[i:m.start()])
        depth, j = 1, m.end()
        while j < len(s) and depth:
            if s[j] == "\\":
                j += 2
                continue
            depth += {"{": 1, "}": -1}.get(s[j], 0)
            j += 1
        if out is not None:
            out.append(s[m.end():j - 1])
        res.append(" X ")                                     # giữ chỗ một token
        i = j
    res.append(s[i:])
    return "".join(res)


def skip_token(s: str, i: int) -> int:
    """Vị trí ngay sau một token TeX bắt đầu tại i (bỏ khoảng trắng đầu)."""
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s):
        return i
    if s[i] == "{":
        depth, j = 1, i + 1
        while j < len(s) and depth:
            if s[j] == "\\":
                j += 2
                continue
            depth += {"{": 1, "}": -1}.get(s[j], 0)
            j += 1
        return j
    if s[i] == "\\":
        m = re.match(r"\\(?:[A-Za-z]+|.)", s[i:])
        return i + (m.end() if m else 1)
    return i + 1


def check_content(math: str) -> list[tuple[str, str, str]]:
    """Kiểm tra nội dung một công thức. Trả về (level, code, msg)."""
    out = []
    short = math.strip()[:70]
    noesc = re.sub(r"\\.", "  ", math)                      # bỏ mọi ký tự đã escape
    if noesc.count("{") != noesc.count("}"):
        out.append(("ERROR", "unbalanced-braces", f"ngoặc {{}} lệch ({noesc.count('{')} mở / {noesc.count('}')} đóng): {short}"))
    lefts, rights = len(re.findall(r"\\left(?![A-Za-z])", math)), len(re.findall(r"\\right(?![A-Za-z])", math))
    if lefts != rights:
        out.append(("ERROR", "unbalanced-left-right", f"\\left ({lefts}) ≠ \\right ({rights}): {short}"))
    stack, env_ok = [], True
    for kind, env in re.findall(r"\\(begin|end)\{(\w+\*?)\}", math):
        if kind == "begin":
            stack.append(env)
        elif not stack or stack.pop() != env:
            env_ok = False
    if stack or not env_ok:
        out.append(("ERROR", "unbalanced-begin-end", f"\\begin/\\end không khớp: {short}"))
    if "$" in noesc:
        out.append(("ERROR", "dollar-in-math", f"ký tự $ nằm trong công thức (KaTeX: Can't use function '$' in math mode): {short}"))
    if "%" in noesc:
        out.append(("ERROR", "unescaped-percent", f"% chưa escape (thành comment, nuốt phần sau) → dùng \\%: {short}"))
    for g in text_groups(math):
        bad = sorted(set(re.findall(r"(?<!\\)[_^&#%]", g)))
        if bad:
            out.append(("ERROR", "special-char-in-text", f"\\text{{{g[:40]}}} chứa {' '.join(bad)} chưa escape"))
    bare = strip_groups(math)
    for i, ch in enumerate(bare):
        if ch in "_^" and (i == 0 or bare[i - 1] != "\\"):
            j = skip_token(bare, i + 1)
            while j < len(bare) and bare[j].isspace():
                j += 1
            if j < len(bare) and bare[j] == ch:
                kind = "subscript" if ch == "_" else "superscript"
                out.append(("ERROR", f"double-{kind}", f"double {kind} '{bare[max(0, i - 8):j + 3].strip()}' → bọc ngoặc {{}}: {short}"))
                break
    if re.search(r"\\frac(?![A-Za-z])\s*(?![\s{\\0-9A-Za-z])", bare):
        out.append(("ERROR", "invalid-frac", f"\\frac thiếu đối số: {short}"))
    # WARN: render được nhưng sai hình thức
    if VN_CHARS.search(bare):
        out.append(("WARN", "vn-char-in-math", f"chữ tiếng Việt ngoài \\text{{}}: {short}"))
    m = re.search(r"(?<!\\)_([A-Za-z]{2,})", bare)
    if m:
        out.append(("WARN", "unbraced-subscript", f"'_{m.group(1)}' chỉ hạ chỉ số ký tự đầu → _{{{m.group(1)}}} hoặc _{{\\text{{{m.group(1)}}}}}: {short}"))
    m = re.search(r"\^-[A-Za-z0-9]", bare)
    if m:
        out.append(("WARN", "unbraced-exponent", f"'{m.group(0)}' → ^{{{m.group(0)[1:]}}}: {short}"))
    # INFO: gợi ý văn phong
    words = [w for w in re.findall(r"\b[A-Za-z]{3,}\b", re.sub(r"\\(?:begin|end)\{[^}]*\}|\\[A-Za-z]+", " ", bare)) if w.lower() not in LATEX_WORDS]
    if words:
        out.append(("INFO", "naked-word", f"từ {words[:3]} chưa bọc \\text{{}}: {short}"))
    return out


def scan(text: str) -> list[dict]:
    """Quét một file markdown. Trả về list {line, level, code, msg}; line tính từ 1, kể cả frontmatter."""
    issues: list[dict] = []
    add = lambda ln, lv, code, msg: issues.append({"line": ln, "level": lv, "code": code, "msg": msg})
    lines = mask(text).split("\n")
    in_display, start, buf = False, 0, []
    for ln, line in enumerate(lines, 1):
        rest = line[PREFIX.match(line).end():]
        dds = list(DD.finditer(rest))
        is_row = rest.strip().startswith("|")
        if in_display:
            if not dds:
                if not rest.strip():
                    add(ln, "ERROR", "display-blank-line", f"dòng trống trong khối $$ mở ở dòng {start} (khối bị cắt đôi)")
                buf.append(rest)
                continue
            close = dds[0]
            buf.append(rest[:close.start()])
            if rest[close.end():].strip():
                add(ln, "ERROR", "display-not-own-line",
                    f"có chữ sau $$ đóng: '{rest[close.end():].strip()[:40]}' → đưa xuống dòng riêng")
            for lv, code, msg in check_content("\n".join(buf)):
                add(start, lv, code, msg)
            in_display, buf = False, []
            continue
        if dds:
            if is_row:
                add(ln, "ERROR", "display-in-table", "$$ trong dòng bảng → dùng $…$")
                continue
            if dds[0].start() != 0:
                add(ln, "ERROR", "display-not-own-line",
                    f"có chữ trước $$: '{rest[:dds[0].start()].strip()[:40]}' → $$ phải mở đầu dòng")
                continue
            if len(dds) == 1:
                in_display, start, buf = True, ln, [rest[2:]]
                continue
            close = dds[1]
            if rest[close.end():].strip() or len(dds) > 2:
                add(ln, "ERROR", "display-not-own-line",
                    f"có chữ sau $$ đóng: '{rest[close.end():].strip()[:40]}' → citation đặt ở dòng sau")
                continue
            for lv, code, msg in check_content(rest[2:close.start()]):
                add(ln, lv, code, msg)
            continue
        # inline math
        if is_row:
            for c, cell in enumerate(re.split(r"(?<!\\)\|", rest.strip())[1:-1], 1):
                if len(SINGLE.findall(cell)) % 2:
                    add(ln, "ERROR", "table-split-math", f"ô {c} có số $ lẻ (| trong math phải là \\|): {cell.strip()[:50]}")
        elif len(SINGLE.findall(rest)) % 2:
            add(ln, "WARN", "unmatched-dollar", f"số $ lẻ trên dòng (thiếu $ đóng, hoặc ký hiệu tiền → \\$): {rest.strip()[:60]}")
        for m in INLINE.finditer(rest):
            body = m.group(1)
            if body != body.strip():
                add(ln, "WARN", "inline-space", f"khoảng trắng sát dấu $ (Obsidian không render): ${body}$"[:90])
            for lv, code, msg in check_content(body):
                add(ln, lv, code, msg)
        outside = INLINE.sub(" ", rest)
        m = RAW_LATEX.search(outside)
        if m:
            add(ln, "WARN", "latex-outside-math", f"lệnh {m.group(0)} nằm ngoài $…$: {outside.strip()[:60]}")
    if in_display:
        add(start, "ERROR", "display-unclosed", "khối $$ không có $$ đóng")
    return issues


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="file .md; mặc định toàn bộ 02_wiki")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--info", action="store_true", help="hiện cả INFO (gợi ý văn phong)")
    args = ap.parse_args()
    paths = [Path(f) for f in args.files] or sorted(WIKI.rglob("*.md"))
    items = []
    for p in paths:
        rel = p.resolve().relative_to(ROOT).as_posix() if p.resolve().is_relative_to(ROOT) else str(p)
        for i in scan(p.read_text(encoding="utf-8")):
            if i["level"] != "INFO" or args.info:
                items.append({"path": rel, **i})
    count = {lv: sum(i["level"] == lv for i in items) for lv in ("ERROR", "WARN", "INFO")}
    if args.json:
        print(json.dumps({"summary": count, "items": items}, ensure_ascii=False, indent=2))
    else:
        for i in items:
            print(f"{i['level']:5} {i['path']}:{i['line']}  [{i['code']}] {i['msg']}")
        print(f"\n{len(paths)} file · {count['ERROR']} error · {count['WARN']} warning"
              + (f" · {count['INFO']} info" if args.info else ""))
    return 1 if count["ERROR"] else 0


if __name__ == "__main__":
    sys.exit(main())
