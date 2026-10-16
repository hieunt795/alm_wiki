#!/usr/bin/env python3
"""Scan all math formulas for Vietnamese characters outside \text{}, multi-letter variables without \text{}, unbraced sub/superscripts, etc."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

# Vietnamese accented characters regex
VN_CHARS = re.compile(r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]")

def check_math_expression(math_str: str, file_path: Path, line_no: int, is_block: bool):
    issues = []
    
    # 1. Check for Vietnamese characters outside \text{...}
    # Remove all \text{...} and \mathrm{...} and \mathbf{...}
    # Be careful with nested braces inside \text{...}
    # A simple way: iteratively remove innermost \text{...}
    stripped = math_str
    while True:
        new_stripped = re.sub(r"\\(?:text|mathrm|mathbf|mathit)\{[^{}]*\}", "", stripped)
        if new_stripped == stripped:
            break
        stripped = new_stripped
        
    vn_matches = VN_CHARS.findall(stripped)
    if vn_matches:
        issues.append(("VN_CHAR_OUTSIDE_TEXT", f"Vietnamese char '{vn_matches[0]}' outside \\text{{}}: {math_str[:60]}"))
        
    # 2. Check for multi-letter subscript without braces: e.g. _abc
    # Pattern: _[a-zA-Z]{2,}
    unbraced_sub = re.findall(r"_(?![{a-zA-Z]*\})([a-zA-Z]{2,})", stripped)
    # Actually regex for unbraced subscript: _ followed by 2 or more letters without {
    # e.g. _final, _Base, _repricing, _contract
    unbraced_subs = re.findall(r"_(?=[a-zA-Z]{2,}\b)([a-zA-Z]+)", stripped)
    if unbraced_subs:
        issues.append(("UNBRACED_MULTILETTER_SUBSCRIPT", f"Unbraced subscript '_{unbraced_subs[0]}': {math_str[:60]}"))

    # 3. Check for unbraced negative exponents: e.g. ^-t or ^-1
    unbraced_exp = re.findall(r"\^-[a-zA-Z0-9]+", stripped)
    if unbraced_exp:
        issues.append(("UNBRACED_EXPONENT", f"Unbraced exponent '{unbraced_exp[0]}': {math_str[:60]}"))
        
    # 4. Check for double subscript e.g. a_b_c
    if re.search(r"_[a-zA-Z0-9\\]+_[a-zA-Z0-9\\]+", stripped):
        issues.append(("DOUBLE_SUBSCRIPT", f"Double subscript: {math_str[:60]}"))
        
    # 5. Check for unescaped %
    if re.search(r"(?<!\\)%", math_str):
        issues.append(("UNESCAPED_PERCENT", f"Unescaped %: {math_str[:60]}"))

    return issues

def scan_files():
    total_issues = 0
    files = sorted(WIKI.rglob("*.md"))
    
    for f in files:
        content = f.read_text(encoding="utf-8")
        lines = content.splitlines()
        
        # Strip code blocks
        clean_lines = []
        in_code = False
        for l in lines:
            if l.strip().startswith("```"):
                in_code = not in_code
                clean_lines.append("")
            elif in_code:
                clean_lines.append("")
            else:
                clean_lines.append(l)
        clean_content = "\n".join(clean_lines)
        
        file_issues = []
        
        # Check $$ blocks
        for m in re.finditer(r"\$\$(.*?)\$\$", clean_content, re.DOTALL):
            block = m.group(1)
            line_no = clean_content[:m.start()].count("\n") + 1
            issues = check_math_expression(block, f, line_no, True)
            for code, msg in issues:
                file_issues.append((line_no, code, msg))
                
        # Check inline $ ... $
        # Remove $$ first
        no_dd = re.sub(r"\$\$.*?\$\$", lambda m: " " * len(m.group(0)), clean_content, flags=re.DOTALL)
        for idx, line in enumerate(no_dd.splitlines(), 1):
            inlines = re.findall(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", line)
            for im in inlines:
                issues = check_math_expression(im, f, idx, False)
                for code, msg in issues:
                    file_issues.append((idx, code, msg))
                    
        if file_issues:
            rel = f.relative_to(ROOT)
            print(f"\n=== {rel} ({len(file_issues)} issues) ===")
            for lno, code, msg in file_issues:
                print(f"  Line {lno:4d} [{code}] {msg}")
                total_issues += 1
                
    print(f"\n==========================================")
    print(f"Total issues found: {total_issues}")
    print(f"==========================================")

if __name__ == "__main__":
    scan_files()
