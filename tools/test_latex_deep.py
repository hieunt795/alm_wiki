#!/usr/bin/env python3
"""Deep inspection of LaTeX formulas across all markdown files in 02_wiki."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

def inspect_file(f: Path):
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    reports = []
    
    # Track code block fences
    in_code_block = False
    
    for line_idx, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
            
        # Check 1: Odd number of $ on a single line (excluding $$)
        # First remove escaped \$
        temp_line = re.sub(r"\\\$", "", line)
        # Count $$
        dd_count = len(re.findall(r"\$\$", temp_line))
        # Remove $$
        temp_line_no_dd = re.sub(r"\$\$", "", temp_line)
        single_dollar_count = temp_line_no_dd.count("$")
        
        # If odd number of $ on line and dd_count == 0, possible unclosed inline math
        # Note: if a $$ block spans multiple lines, dd_count on start line is 1, on end line is 1
        if dd_count == 0 and single_dollar_count % 2 != 0:
            reports.append((line_idx, "ODD_SINGLE_DOLLAR", line.strip()))
        elif dd_count == 1:
            # Display math starting or ending on this line
            pass
        elif dd_count > 1 and dd_count % 2 != 0:
            reports.append((line_idx, "ODD_DOUBLE_DOLLAR", line.strip()))
            
        # Check 2: Unescaped % inside math
        # Look at inline math on this line
        # Find all $...$
        inlines = re.findall(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", line)
        for im in inlines:
            # Check for unescaped %
            # If there is % not preceded by \
            un_pct = [m.start() for m in re.finditer(r"(?<!\\)%", im)]
            if un_pct:
                reports.append((line_idx, "UNESCAPED_PERCENT_INLINE", f"${im}$"))
                
        # Check 3: Pipe | inside math in markdown table lines
        if line.strip().startswith("|") and line.strip().endswith("|"):
            # Check if cell has odd number of $
            # If so, a pipe | inside math likely split the cell!
            cells = line.split("|")[1:-1]
            for c_idx, cell in enumerate(cells, 1):
                clean_cell = re.sub(r"\\\$", "", cell)
                clean_cell = re.sub(r"\$\$", "", clean_cell)
                if clean_cell.count("$") % 2 != 0:
                    reports.append((line_idx, "SPLIT_MATH_IN_TABLE", f"Cell {c_idx}: {cell.strip()}"))
                    
        # Check 4: \text with unbalanced braces or syntax errors
        # e.g. \text{ without closing }
        for m in re.finditer(r"\\text\{([^}]*)$", line):
            # check if it's not closed on same line (and not multiline display math)
            if "$$" not in line and "$" in line:
                reports.append((line_idx, "UNCLOSED_TEXT", line.strip()))
                
    # Also check multi-line $$ blocks
    # Replace code blocks with blank lines
    code_block_re = re.compile(r"```.*?```", re.DOTALL)
    clean_all = code_block_re.sub(lambda m: "\n" * m.group(0).count("\n"), content)
    
    # Check $$ blocks
    for m in re.finditer(r"\$\$(.*?)\$\$", clean_all, re.DOTALL):
        block = m.group(1)
        start_line = clean_all[:m.start()].count("\n") + 1
        
        # Check unescaped % in display math
        for b_idx, bl in enumerate(block.splitlines()):
            un_pct = [pm.start() for pm in re.finditer(r"(?<!\\)%", bl)]
            if un_pct:
                reports.append((start_line + b_idx, "UNESCAPED_PERCENT_BLOCK", bl.strip()))
                
        # Check unbalanced braces
        open_b = len(re.findall(r"(?<!\\)\{", block))
        close_b = len(re.findall(r"(?<!\\)\}", block))
        if open_b != close_b:
            reports.append((start_line, "UNBALANCED_BRACES_BLOCK", f"open {open_b} != close {close_b} in: {block.strip()[:60]}"))

    return reports

def main():
    files = sorted(WIKI.rglob("*.md"))
    total_issues = 0
    for f in files:
        reps = inspect_file(f)
        if reps:
            rel = f.relative_to(ROOT)
            print(f"\n=== {rel} ({len(reps)} issues) ===")
            for line, code, msg in reps:
                print(f"  Line {line:4d} [{code}] {msg}")
                total_issues += 1
    print(f"\nTotal potential issues: {total_issues}")

if __name__ == "__main__":
    main()
