#!/usr/bin/env python3
"""Find all multi-letter subscripts and variables in math without \\text{} or \\mathrm{}."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

pattern = re.compile(r"_\{([a-zA-Z]{2,})\}")

def scan():
    found = 0
    files = sorted(WIKI.rglob("*.md"))
    for f in files:
        content = f.read_text(encoding="utf-8")
        clean = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        
        display_math = re.findall(r"\$\$(.*?)\$\$", clean, flags=re.DOTALL)
        no_dd = re.sub(r"\$\$.*?\$\$", "", clean, flags=re.DOTALL)
        inline_math = re.findall(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", no_dd)
        
        all_math = [(m, "display") for m in display_math] + [(m, "inline") for m in inline_math]
        
        for mb, mtype in all_math:
            for m in pattern.finditer(mb):
                word = m.group(1)
                print(f"[{f.name}] _{{{word}}} in: {mb.strip()[:70]}")
                found += 1
    print(f"\nTotal findings: {found}")

if __name__ == "__main__":
    scan()
