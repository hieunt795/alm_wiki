#!/usr/bin/env python3
"""Check for raw LaTeX commands outside math blocks ($ or $$) or code blocks."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

LATEX_COMMANDS = [
    r"\\frac", r"\\sum", r"\\prod", r"\\sqrt", r"\\times", r"\\approx",
    r"\\Delta", r"\\le\b", r"\\ge\b", r"\\partial", r"\\int\b", r"\\cdot",
    r"\\alpha\b", r"\\beta\b", r"\\gamma\b", r"\\sigma\b", r"\\lambda\b"
]
LATEX_RE = re.compile("|".join(LATEX_COMMANDS))

def scan_raw_latex():
    files = sorted(WIKI.rglob("*.md"))
    found = 0
    for f in files:
        content = f.read_text(encoding="utf-8")
        # Strip code blocks
        clean = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        # Strip display math $$ ... $$
        clean = re.sub(r"\$\$.*?\$\$", "", clean, flags=re.DOTALL)
        # Strip inline math $ ... $
        clean = re.sub(r"(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)", "", clean)
        
        lines = clean.splitlines()
        for idx, line in enumerate(lines, 1):
            # check for latex commands
            m = LATEX_RE.search(line)
            if m:
                print(f"RAW LATEX OUTSIDE MATH in {f.name}:{idx}: {line.strip()[:80]}")
                found += 1
    print(f"Total raw LaTeX outside math: {found}")

if __name__ == "__main__":
    scan_raw_latex()
