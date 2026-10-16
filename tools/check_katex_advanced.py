#!/usr/bin/env python3
"""Check advanced KaTeX/LaTeX errors in markdown files."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

def check_file(f: Path):
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    issues = []
    
    # 1. Check for $$ inside tables
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("|") and line.strip().endswith("|"):
            if "$$" in line:
                issues.append((idx, "DISPLAY_MATH_IN_TABLE", f"$$ used in table row: {line.strip()[:60]}"))
                
    # 2. Check for unescaped underscore _ inside \text{...}
    # In KaTeX, \text{foo_bar} throws "KaTeX parse error: Undefined control sequence: _" or "Cannot use _ in text mode"
    # It must be \text{foo\_bar}
    text_blocks = re.findall(r"\\text\{([^{}]*)\}", content)
    for tb in text_blocks:
        # Check if tb contains unescaped _
        # An unescaped _ is not preceded by \
        if re.search(r"(?<!\\)_", tb):
            # Find which line it's on
            for idx, line in enumerate(lines, 1):
                if f"\\text{{{tb}}}" in line:
                    issues.append((idx, "UNESCAPED_UNDERSCORE_IN_TEXT", f"\\text{{{tb}}} contains unescaped underscore"))
                    break

    # 3. Check for double subscript / superscript errors
    # In LaTeX: a_b_c without braces is an error. a_{b_c} or a_{b,c} is valid.
    # Also a^b^c without braces is an error.
    # Let's find all $...$ and $$...$$
    maths = re.findall(r"(?<!\\)\$\$(.*?)\$\$", content, re.DOTALL)
    content_no_display = re.sub(r"(?<!\\)\$\$.*?\$\$", "", content, re.DOTALL)
    maths += re.findall(r"(?<!\\)\$(.*?)(?<!\\)\$", content_no_display)
    
    for m in maths:
        # Strip \text{...} from math to avoid false matches
        clean_m = re.sub(r"\\text\{.*?\}", "", m)
        # Check double subscript: e.g. _foo_bar where neither is enclosed in braces
        # A double subscript happens if there's _word_word where the first _ was not a braced block _{...}
        # e.g. x_1_2 or x_a_b
        # Match pattern: _[^{}\s]+_
        matches = re.findall(r"_[^{}\s\\]+_[^{}\s\\]+", clean_m)
        if matches:
            for idx, line in enumerate(lines, 1):
                if any(match in line for match in matches):
                    issues.append((idx, "DOUBLE_SUBSCRIPT", f"Double subscript '{matches}' in formula"))
                    break

    # 4. Check for invalid or incomplete LaTeX commands:
    # \frac with missing braces e.g. \frac followed by not { or letter
    # \sum without limits or invalid syntax
    # unescaped & outside of \begin{matrix} or \begin{aligned} or table
    for idx, line in enumerate(lines, 1):
        if not line.strip().startswith("|"):
            # If line has math
            if "$" in line:
                # Check for \frac without {
                if re.search(r"\\frac\s*[^{0-9a-zA-Z\\]", line):
                    issues.append((idx, "INVALID_FRAC", f"Invalid \\frac syntax: {line.strip()[:60]}"))

    return issues

def main():
    files = sorted(WIKI.rglob("*.md"))
    total = 0
    for f in files:
        issues = check_file(f)
        if issues:
            rel = f.relative_to(ROOT)
            print(f"\n=== {rel} ===")
            for line, code, msg in issues:
                print(f"  Line {line:4d} [{code}] {msg}")
                total += 1
    print(f"\nTotal advanced issues: {total}")

if __name__ == "__main__":
    main()
