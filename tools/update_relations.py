import yaml
import re
from pathlib import Path

RELATIONS_DATA = {
    '02_wiki/regulations/bcbs-lcr.md': [
        {'type': 'governs', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr10-1]]'},
        {'type': 'governs', 'to': '[[hqla]]', 'cite': '[[src-bcbs-lcr#^lcr30-1]]'},
        {'type': 'governs', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'governs', 'to': '[[alternative-liquidity-approaches]]', 'cite': '[[src-bcbs-lcr#^lcr31-1]]'},
        {'type': 'governs', 'to': '[[liquidity-transfer-restrictions]]', 'cite': '[[src-bcbs-lcr#^lcr30-24]]'}
    ],
    '02_wiki/regulations/bcbs-nsfr.md': [
        {'type': 'governs', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf10-1]]'},
        {'type': 'governs', 'to': '[[available-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-6]]'},
        {'type': 'governs', 'to': '[[required-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-15]]'},
        {'type': 'governs', 'to': '[[interdependent-assets-and-liabilities]]', 'cite': '[[src-bcbs-nsfr#^nsf30-35]]'}
    ],
    '02_wiki/metrics/lcr.md': [
        {'type': 'measures', 'to': '[[hqla]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'},
        {'type': 'measures', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'},
        {'type': 'limits', 'to': '[[hqla]]', 'cite': '[[src-bcbs-lcr#^lcr20-4]]'}
    ],
    '02_wiki/metrics/net-cash-outflows.md': [
        {'type': 'part-of', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'},
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'}
    ],
    '02_wiki/metrics/nsfr.md': [
        {'type': 'measures', 'to': '[[available-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'measures', 'to': '[[required-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'limits', 'to': '[[available-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'}
    ],
    '02_wiki/concepts/hqla.md': [
        {'type': 'part-of', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'},
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'}
    ],
    '02_wiki/concepts/level-1-assets.md': [
        {'type': 'part-of', 'to': '[[hqla]]', 'cite': '[[src-bcbs-lcr#^lcr30-41]]'},
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '+', 'cite': '[[src-bcbs-lcr#^lcr30-41]]'}
    ],
    '02_wiki/concepts/level-2-assets.md': [
        {'type': 'part-of', 'to': '[[hqla]]', 'cite': '[[src-bcbs-lcr#^lcr30-43]]'},
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '+', 'cite': '[[src-bcbs-lcr#^lcr30-43]]'}
    ],
    '02_wiki/concepts/hqla-unwinding-mechanism.md': [
        {'type': 'part-of', 'to': '[[hqla]]', 'cite': '[[src-bcbs-lcr#^lcr30-34]]'},
        {'type': 'limits', 'to': '[[level-2-assets]]', 'cite': '[[src-bcbs-lcr#^lcr30-37]]'},
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr30-34]]'}
    ],
    '02_wiki/concepts/liquidity-transfer-restrictions.md': [
        {'type': 'limits', 'to': '[[hqla]]', 'cite': '[[src-bcbs-lcr#^lcr30-24]]'},
        {'type': 'limits', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr10-8]]'}
    ],
    '02_wiki/concepts/alternative-liquidity-approaches.md': [
        {'type': 'part-of', 'to': '[[hqla]]', 'cite': '[[src-bcbs-lcr#^lcr31-1]]'},
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr31-1]]'}
    ],
    '02_wiki/concepts/cash-outflows.md': [
        {'type': 'part-of', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'input-to', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '-', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'}
    ],
    '02_wiki/concepts/cash-inflows.md': [
        {'type': 'part-of', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'input-to', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '+', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'}
    ],
    '02_wiki/concepts/run-off-rate.md': [
        {'type': 'part-of', 'to': '[[cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'input-to', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '-', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'}
    ],
    '02_wiki/concepts/retail-deposit-stability.md': [
        {'type': 'part-of', 'to': '[[cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-5]]'},
        {'type': 'part-of', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'drives', 'to': '[[run-off-rate]]', 'cite': '[[src-bcbs-lcr#^lcr40-6]]'}
    ],
    '02_wiki/concepts/unsecured-wholesale-funding.md': [
        {'type': 'part-of', 'to': '[[cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-19]]'},
        {'type': 'part-of', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '-', 'cite': '[[src-bcbs-lcr#^lcr40-20]]'}
    ],
    '02_wiki/concepts/operational-deposits.md': [
        {'type': 'part-of', 'to': '[[unsecured-wholesale-funding]]', 'cite': '[[src-bcbs-lcr#^lcr40-26]]'},
        {'type': 'part-of', 'to': '[[cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-26]]'},
        {'type': 'part-of', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'}
    ],
    '02_wiki/concepts/secured-funding.md': [
        {'type': 'part-of', 'to': '[[cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-45]]'},
        {'type': 'part-of', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '-', 'cite': '[[src-bcbs-lcr#^lcr40-46]]'}
    ],
    '02_wiki/concepts/committed-facilities.md': [
        {'type': 'part-of', 'to': '[[cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-59]]'},
        {'type': 'part-of', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '-', 'cite': '[[src-bcbs-lcr#^lcr40-64]]'}
    ],
    '02_wiki/concepts/derivatives-and-contingent-outflows.md': [
        {'type': 'part-of', 'to': '[[cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-49]]'},
        {'type': 'input-to', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'drives', 'to': '[[lcr]]', 'direction': '-', 'cite': '[[src-bcbs-lcr#^lcr40-51]]'}
    ],
    '02_wiki/concepts/available-stable-funding.md': [
        {'type': 'part-of', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '+', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'}
    ],
    '02_wiki/concepts/required-stable-funding.md': [
        {'type': 'part-of', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '-', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'}
    ],
    '02_wiki/concepts/interdependent-assets-and-liabilities.md': [
        {'type': 'part-of', 'to': '[[available-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-35]]'},
        {'type': 'part-of', 'to': '[[required-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-35]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf30-35]]'}
    ],
    '02_wiki/concepts/asf-capital-and-long-term-liabilities.md': [
        {'type': 'part-of', 'to': '[[available-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-10]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '+', 'cite': '[[src-bcbs-nsfr#^nsf30-10]]'}
    ],
    '02_wiki/concepts/asf-retail-and-small-business-deposits.md': [
        {'type': 'part-of', 'to': '[[available-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-11]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '+', 'cite': '[[src-bcbs-nsfr#^nsf30-11]]'}
    ],
    '02_wiki/concepts/asf-wholesale-and-operational-funding.md': [
        {'type': 'part-of', 'to': '[[available-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-13]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '+', 'cite': '[[src-bcbs-nsfr#^nsf30-13]]'}
    ],
    '02_wiki/concepts/rsf-hqla-and-central-bank-reserves.md': [
        {'type': 'part-of', 'to': '[[required-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-25]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '-', 'cite': '[[src-bcbs-nsfr#^nsf30-26]]'}
    ],
    '02_wiki/concepts/rsf-loans-and-credit-exposures.md': [
        {'type': 'part-of', 'to': '[[required-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-15]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '-', 'cite': '[[src-bcbs-nsfr#^nsf30-31]]'}
    ],
    '02_wiki/concepts/rsf-securities-financing-and-encumbrance.md': [
        {'type': 'part-of', 'to': '[[required-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-20]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '-', 'cite': '[[src-bcbs-nsfr#^nsf30-20]]'}
    ],
    '02_wiki/concepts/rsf-derivatives-and-off-balance-sheet.md': [
        {'type': 'part-of', 'to': '[[required-stable-funding]]', 'cite': '[[src-bcbs-nsfr#^nsf30-31]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'drives', 'to': '[[nsfr]]', 'direction': '-', 'cite': '[[src-bcbs-nsfr#^nsf30-32]]'}
    ],
    '02_wiki/syntheses/hqla-decomposition-and-tradeoffs.md': [
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'},
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf30-26]]'}
    ],
    '02_wiki/syntheses/lcr-net-cash-outflows-mechanics.md': [
        {'type': 'input-to', 'to': '[[net-cash-outflows]]', 'cite': '[[src-bcbs-lcr#^lcr40-1]]'},
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'}
    ],
    '02_wiki/syntheses/lcr-economic-significance-and-alm-governance.md': [
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'},
        {'type': 'measures', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-3]]'}
    ],
    '02_wiki/syntheses/nsfr-structural-liquidity-and-alm-strategy.md': [
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'input-to', 'to': '[[lcr]]', 'cite': '[[src-bcbs-lcr#^lcr20-1]]'}
    ],
    '02_wiki/syntheses/nsfr-alm-governance-strategy-and-risks.md': [
        {'type': 'input-to', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf20-2]]'},
        {'type': 'measures', 'to': '[[nsfr]]', 'cite': '[[src-bcbs-nsfr#^nsf10-5]]'}
    ]
}

def format_rel(r):
    parts = [f"type: {r['type']}", f"to: \"{r['to']}\""]
    if 'direction' in r:
        parts.append(f"direction: \"{r['direction']}\"")
    if 'regime' in r:
        parts.append(f"regime: \"{r['regime']}\"")
    if 'cite' in r:
        parts.append(f"cite: \"{r['cite']}\"")
    return "  - {" + ", ".join(parts) + "}"

def update_file(file_path, rels):
    p = Path(file_path)
    if not p.exists():
        print(f"MISSING: {file_path}")
        return False
    content = p.read_text(encoding="utf-8")
    m = re.match(r"^(---\s*\n)(.*?\n)(---\s*\n)(.*)$", content, re.S)
    if not m:
        print(f"NO FM: {file_path}")
        return False
    head, fm_text, sep, body = m.groups()
    rel_block = "relations:\n" + "\n".join(format_rel(r) for r in rels) + "\n"
    
    # Check if 'relations:' is present
    if re.search(r"^relations:.*$", fm_text, re.M):
        # Replace the entire relations block up to the next top-level key
        new_fm = re.sub(
            r"^relations:(?:\s*\[\]|\s*\n(?:[ \t]+-[^\n]*\n*)*)",
            rel_block,
            fm_text,
            flags=re.M
        )
    else:
        # Insert before tags or updated
        if "tags:" in fm_text:
            new_fm = fm_text.replace("tags:", rel_block + "tags:")
        elif "updated:" in fm_text:
            new_fm = fm_text.replace("updated:", rel_block + "updated:")
        else:
            new_fm = fm_text + rel_block
            
    p.write_text(head + new_fm + sep + body, encoding="utf-8")
    print(f"Updated {file_path}")
    return True

if __name__ == "__main__":
    count = 0
    for path, rels in RELATIONS_DATA.items():
        if update_file(path, rels):
            count += 1
    print(f"Total updated: {count}")
