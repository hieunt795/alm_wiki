#!/usr/bin/env python3
"""Comprehensive LaTeX error and formatting checker for ALM wiki."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

# Vietnamese accented characters regex
VN_CHARS = re.compile(r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]")

def strip_text_environments(s: str) -> str:
    """Iteratively strip \\text{...}, \\mathrm{...}, \\mathbf{...}, \\mathit{...} handling nested braces."""
    # Find innermost \text{...}
    while True:
        new_s = re.sub(r"\\(?:text|mathrm|mathbf|mathit)\{[^{}]*\}", "", s)
        if new_s == s:
            break
        s = new_s
    return s

def check_latex_in_file(f: Path):
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    errors = []
    
    # 1. Clean code blocks
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

    # 2. Extract display math blocks
    for m in re.finditer(r"\$\$(.*?)\$\$", clean_content, re.DOTALL):
        block = m.group(1)
        line_no = clean_content[:m.start()].count("\n") + 1
        
        # Check braces balance
        # Remove \{ and \}
        b_no_escaped = re.sub(r"\\[\{\}]", "", block)
        open_b = b_no_escaped.count("{")
        close_b = b_no_escaped.count("}")
        if open_b != close_b:
            errors.append((line_no, "UNBALANCED_BRACES", f"Open braces {open_b} != close braces {close_b} in: {block.strip()[:60]}"))
            
        # Check \left and \right balance
        # Match \left followed by delimiter, and \right followed by delimiter
        lefts = len(re.findall(r"\\left(?:\s*[\(\[\{\.\|\/\\]|\s*\\\{)", block))
        rights = len(re.findall(r"\\right(?:\s*[\)\]\}\.\|\/\\]|\s*\\\})", block))
        if lefts != rights:
            errors.append((line_no, "UNBALANCED_LEFTRIGHT", f"\\left count ({lefts}) != \\right count ({rights}) in: {block.strip()[:60]}"))
            
        # Check unescaped %
        for b_idx, bl in enumerate(block.splitlines()):
            if re.search(r"(?<!\\)%", bl):
                errors.append((line_no + b_idx, "UNESCAPED_PERCENT", f"Unescaped % comments out formula in: {bl.strip()}"))
                
        # Check Vietnamese chars outside \text
        no_text = strip_text_environments(block)
        vn_chars = VN_CHARS.findall(no_text)
        if vn_chars:
            errors.append((line_no, "VN_CHAR_IN_MATH", f"Vietnamese char '{vn_chars[0]}' outside \\text{{}}: {block.strip()[:60]}"))
            
        # Check for unescaped multi-letter identifier with underscore e.g. ALCO_adj, OptionCost_prepay
        # Pattern: letters_letters where neither is braced and not in \text
        # e.g. ALCO_adj -> should be \text{ALCO\_adj} or \text{ALCO}_{adj}
        raw_words_with_underscore = re.findall(r"(?<!\\)\b([a-zA-Z]{2,}_[a-zA-Z]{2,})\b", no_text)
        for rwu in raw_words_with_underscore:
            errors.append((line_no, "UNDERSCORE_IN_IDENTIFIER", f"Identifier with underscore '{rwu}' should be in \\text{{...}}"))
            
        # Check double subscripts
        if re.search(r"_[^{}\s\\]+_[^{}\s\\]+", no_text):
            errors.append((line_no, "DOUBLE_SUBSCRIPT", f"Double subscript without braces in: {block.strip()[:60]}"))

    # 3. Extract inline math
    # First strip $$...$$
    no_dd = re.sub(r"\$\$.*?\$\$", lambda m: " " * len(m.group(0)), clean_content, flags=re.DOTALL)
    for idx, line in enumerate(no_dd.splitlines(), 1):
        # find inlines
        inlines = re.findall(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", line)
        for im in inlines:
            # Check braces balance
            im_no_esc = re.sub(r"\\[\{\}]", "", im)
            if im_no_esc.count("{") != im_no_esc.count("}"):
                errors.append((idx, "UNBALANCED_BRACES_INLINE", f"Unbalanced braces in: ${im}$"))
                
            # Check unescaped %
            if re.search(r"(?<!\\)%", im):
                errors.append((idx, "UNESCAPED_PERCENT_INLINE", f"Unescaped % in: ${im}$"))
                
            # Check Vietnamese characters outside \text
            no_text = strip_text_environments(im)
            vn_chars = VN_CHARS.findall(no_text)
            if vn_chars:
                errors.append((idx, "VN_CHAR_IN_MATH_INLINE", f"Vietnamese char '{vn_chars[0]}' outside \\text{{}}: ${im}$"))
                
            # Check for unescaped multi-letter identifier with underscore
            raw_words = re.findall(r"(?<!\\)\b([a-zA-Z]{2,}_[a-zA-Z]{2,})\b", no_text)
            for rw in raw_words:
                errors.append((idx, "UNDERSCORE_IN_IDENTIFIER_INLINE", f"Identifier '{rw}' should be in \\text{{...}} in: ${im}$"))
                
            # Check double subscripts
            if re.search(r"_[^{}\s\\]+_[^{}\s\\]+", no_text):
                errors.append((idx, "DOUBLE_SUBSCRIPT_INLINE", f"Double subscript in: ${im}$"))

    return errors

def main():
    files = sorted(WIKI.rglob("*.md"))
    total_errors = 0
    file_errors = {}
    
    for f in files:
        errs = check_latex_in_file(f)
        if errs:
            rel = f.relative_to(ROOT)
            file_errors[str(rel)] = errs
            total_errors += len(errs)
            
    print(f"==================================================")
    print(f"SCAN RESULTS: {total_errors} potential issues in {len(file_errors)} files")
    print(f"==================================================")
    for rel, errs in file_errors.items():
        print(f"\n=== {rel} ({len(errs)} issues) ===")
        for line, code, msg in errs:
            print(f"  Line {line:4d} [{code}] {msg}")

if __name__ == "__main__":
    main()
