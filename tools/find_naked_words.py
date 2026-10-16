#!/usr/bin/env python3
"""Find naked multi-letter words in LaTeX formulas (e.g. LCR, NSFR, HQLA, Duration, Net, Cash, etc. not in \\text{})."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

# Standard LaTeX functions / operators that are allowed
LATEX_FUNCS = {
    "min", "max", "sum", "prod", "ln", "log", "exp", "lim", "det",
    "sin", "cos", "tan", "inf", "sup", "arg", "dim", "ker", "deg",
    "hom", "gcd", "Pr", "int", "var", "cov", "left", "right", "frac",
    "cdot", "times", "approx", "equiv", "partial", "sqrt", "quad", "qquad",
    "limits", "nolimits", "begin", "end", "matrix", "aligned", "array",
    "cases", "bm", "phi", "Phi", "Delta", "sigma", "beta", "alpha", "gamma",
    "tau", "lambda", "bar", "vec", "hat", "tilde", "dots", "cdots", "ldots"
}

def scan_naked_words():
    files = sorted(WIKI.rglob("*.md"))
    findings = {}
    
    for f in files:
        content = f.read_text(encoding="utf-8")
        clean = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        
        display_math = re.findall(r"\$\$(.*?)\$\$", clean, flags=re.DOTALL)
        no_dd = re.sub(r"\$\$.*?\$\$", "", clean, flags=re.DOTALL)
        inline_math = re.findall(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", no_dd)
        
        all_math = [(m, "display") for m in display_math] + [(m, "inline") for m in inline_math]
        
        file_issues = []
        for mb, mtype in all_math:
            # Strip \text{...}, \mathrm{...}, \mathbf{...}, \mathit{...}
            stripped = mb
            while True:
                new_s = re.sub(r"\\(?:text|mathrm|mathbf|mathit)\{[^{}]*\}", "", stripped)
                if new_s == stripped:
                    break
                stripped = new_s
                
            # Strip LaTeX commands like \Delta, \frac, \sum, etc.
            stripped = re.sub(r"\\[a-zA-Z]+", "", stripped)
            
            # Find words with 3 or more letters
            words = re.findall(r"\b[a-zA-Z]{3,}\b", stripped)
            naked = [w for w in words if w.lower() not in LATEX_FUNCS and w not in LATEX_FUNCS]
            
            if naked:
                file_issues.append((naked, mb.strip()))
                
        if file_issues:
            findings[f.name] = file_issues
            
    print(f"Files with naked words in math: {len(findings)}")
    for fname, issues in findings.items():
        print(f"\n=== {fname} ({len(issues)} issues) ===")
        for words, formula in issues[:5]:
            print(f"  Naked: {words} in: {formula[:70]}")
        if len(issues) > 5:
            print(f"  ... and {len(issues) - 5} more")

if __name__ == "__main__":
    scan_naked_words()
