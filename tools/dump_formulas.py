#!/usr/bin/env python3
"""Dump all math formulas across 02_wiki for manual and automated validation."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

def dump_and_validate():
    files = sorted(WIKI.rglob("*.md"))
    display_count = 0
    inline_count = 0
    
    for f in files:
        content = f.read_text(encoding="utf-8")
        clean = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        
        display_math = re.findall(r"\$\$(.*?)\$\$", clean, flags=re.DOTALL)
        if display_math:
            print(f"\n=================== {f.relative_to(ROOT)} ({len(display_math)} display) ===================")
            for b in display_math:
                display_count += 1
                b_str = b.strip()
                print(f"$$ {b_str} $$")
                
    print(f"\nTotal display formulas: {display_count}")

if __name__ == "__main__":
    dump_and_validate()
