#!/usr/bin/env python3
"""List and check all display formulas in 02_wiki."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

def check_all_formulas():
    files = sorted(WIKI.rglob("*.md"))
    for f in files:
        content = f.read_text(encoding="utf-8")
        clean = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        
        # Find display math
        display_math = re.findall(r"\$\$(.*?)\$\$", clean, flags=re.DOTALL)
        for b in display_math:
            b_str = b.strip()
            # Check if there are plain underscores like FOO_BAR not in \text
            # Check if there are typos like \alpa, \lamda, etc.
            # Check if there are non-ASCII characters outside \text
            no_text = re.sub(r"\\(?:text|mathrm|mathbf|mathit)\{[^{}]*\}", "", b_str)
            
            # Check for _ followed by words
            for match in re.finditer(r"([a-zA-Z0-9]+)_([a-zA-Z0-9_]+)", no_text):
                # if the sub is not in braces, e.g. Base_t or COF_final
                sub = match.group(2)
                if len(sub) > 1 and not sub.startswith("{"):
                    print(f"[{f.name}] Multi-char sub without braces: {match.group(0)} in:\n  {b_str}\n")
                    
        # Check inline math with multi-char sub without braces
        no_dd = re.sub(r"\$\$.*?\$\$", "", clean, flags=re.DOTALL)
        for idx, line in enumerate(no_dd.splitlines(), 1):
            for im in re.findall(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", line):
                no_text = re.sub(r"\\(?:text|mathrm|mathbf|mathit)\{[^{}]*\}", "", im)
                for match in re.finditer(r"([a-zA-Z0-9]+)_([a-zA-Z0-9_]+)", no_text):
                    sub = match.group(2)
                    if len(sub) > 1 and not sub.startswith("{"):
                        print(f"[{f.name}:{idx}] Inline multi-char sub without braces: {match.group(0)} in: ${im}$")

if __name__ == "__main__":
    check_all_formulas()
