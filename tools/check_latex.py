#!/usr/bin/env python3
"""Check LaTeX formulas in markdown files for syntax errors and common issues."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

def check_file(path: Path):
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    issues = []
    
    # 1. Remove fenced code blocks ``` ... ```
    # Replace contents of code blocks with blank lines to preserve line numbers
    in_code_block = False
    clean_lines = []
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            clean_lines.append("")
        elif in_code_block:
            clean_lines.append("")
        else:
            clean_lines.append(line)
            
    clean_content = "\n".join(clean_lines)
    
    # 2. Check for unmatched $$
    # Count occurrences of $$
    double_dollars = [m.start() for m in re.finditer(r"\$\$", clean_content)]
    if len(double_dollars) % 2 != 0:
        issues.append(("ERROR", 0, "Unmatched $$ in file"))

    # 3. Check table rows for unescaped pipe in math
    for idx, line in enumerate(clean_lines, 1):
        if line.strip().startswith("|") and line.strip().endswith("|"):
            # Check if there is math with unescaped pipe |
            # If line has $...|...$ where | is not \|
            # Let's inspect cells
            # In markdown tables, | separates cells. If LaTeX has | like $|Gap|$, it gets split into cells:
            # cell 1: "$", cell 2: "Gap", cell 3: "$" which breaks both table and latex!
            # Let's check for isolated single $ in table cells:
            cells = line.split("|")[1:-1]
            for cell in cells:
                # Count unescaped single $ (not preceded by \)
                single_dollars = re.findall(r"(?<!\\)\$", cell)
                if len(single_dollars) % 2 != 0:
                    issues.append(("TABLE_PIPE_MATH", idx, f"Odd number of $ in table cell: {cell.strip()}"))

    # 4. Extract all $$ ... $$ blocks
    for m in re.finditer(r"\$\$(.*?)\$\$", clean_content, flags=re.DOTALL):
        block = m.group(1)
        start_pos = m.start()
        line_num = clean_content[:start_pos].count("\n") + 1
        
        # Check unescaped % inside block
        # In LaTeX, % starts a comment. In display math, unescaped % can comment out code or closing delimiters
        block_lines = block.splitlines()
        for b_idx, bl in enumerate(block_lines):
            # Find % not preceded by \
            un_pct = [pm.start() for pm in re.finditer(r"(?<!\\)%", bl)]
            if un_pct:
                issues.append(("UNESCAPED_PERCENT", line_num + b_idx, f"Unescaped % in display math: {bl.strip()}"))
                
        # Check braces balance
        # Count { and } not preceded by \
        open_braces = len(re.findall(r"(?<!\\)\{", block))
        close_braces = len(re.findall(r"(?<!\\)\}", block))
        if open_braces != close_braces:
            issues.append(("UNBALANCED_BRACES", line_num, f"Unbalanced braces ({open_braces} vs {close_braces}): {block.strip()[:60]}"))
            
        # Check \left and \right balance
        lefts = len(re.findall(r"\\left[\(\[\{\.\|]", block))
        rights = len(re.findall(r"\\right[\)\]\}\.\|]", block))
        if lefts != rights:
            issues.append(("UNBALANCED_LEFTRIGHT", line_num, f"Unbalanced \\left and \\right ({lefts} vs {rights}): {block.strip()[:60]}"))

        # Check double subscripts e.g. x_a_b
        # Remove \text{...} first
        no_text = re.sub(r"\\text\{.*?\}", "", block)
        if re.search(r"_[a-zA-Z0-9\\]+_[a-zA-Z0-9\\]+", no_text):
            issues.append(("DOUBLE_SUBSCRIPT", line_num, f"Possible double subscript in: {block.strip()[:60]}"))

    # 5. Extract all inline $ ... $ (not $$)
    # Match text between single $, ignoring $$
    # Replace $$ with placeholder first
    content_no_double = re.sub(r"\$\$.*?\$\$", "", clean_content, flags=re.DOTALL)
    for idx, line in enumerate(content_no_double.splitlines(), 1):
        # Match inline $...$
        # Regex: (?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)
        inlines = re.findall(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", line)
        
        # Check if line has unmatched single $
        # Count non-escaped single $
        single_dollar_count = len(re.findall(r"(?<!\\)(?<!\$)\$(?!\$)", line))
        if single_dollar_count % 2 != 0:
            # Check if this might be a currency or unclosed dollar
            issues.append(("UNMATCHED_INLINE_DOLLAR", idx, f"Odd number of single $ ({single_dollar_count}): {line.strip()[:80]}"))
            
        for math_str in inlines:
            # Check unescaped %
            # In inline math, $10%$ means the % comments out the closing $!
            if re.search(r"(?<!\\)%", math_str):
                issues.append(("UNESCAPED_PERCENT", idx, f"Unescaped % in inline math: ${math_str}$"))
                
            # Check braces
            open_braces = len(re.findall(r"(?<!\\)\{", math_str))
            close_braces = len(re.findall(r"(?<!\\)\}", math_str))
            if open_braces != close_braces:
                issues.append(("UNBALANCED_BRACES", idx, f"Unbalanced braces in inline math: ${math_str}$"))
                
            # Check \left and \right
            lefts = len(re.findall(r"\\left[\(\[\{\.\|]", math_str))
            rights = len(re.findall(r"\\right[\)\]\}\.\|]", math_str))
            if lefts != rights:
                issues.append(("UNBALANCED_LEFTRIGHT", idx, f"Unbalanced \\left and \\right in inline math: ${math_str}$"))

            # Check double subscript
            no_text = re.sub(r"\\text\{.*?\}", "", math_str)
            if re.search(r"_[a-zA-Z0-9\\]+_[a-zA-Z0-9\\]+", no_text):
                issues.append(("DOUBLE_SUBSCRIPT", idx, f"Possible double subscript in: ${math_str}$"))

    return issues

def main():
    total_issues = 0
    files = sorted(WIKI.rglob("*.md"))
    issue_counts = {}
    
    for f in files:
        issues = check_file(f)
        if issues:
            rel = f.relative_to(ROOT)
            print(f"\n=== {rel} ({len(issues)} issues) ===")
            for itype, line, msg in issues:
                print(f"  Line {line:4d} [{itype}] {msg}")
                issue_counts[itype] = issue_counts.get(itype, 0) + 1
                total_issues += 1
                
    print(f"\n==========================================")
    print(f"Total issues found: {total_issues}")
    for itype, count in sorted(issue_counts.items()):
        print(f"  {itype}: {count}")
    print(f"==========================================")

if __name__ == "__main__":
    main()
