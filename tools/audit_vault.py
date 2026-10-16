#!/usr/bin/env python3
"""Kiểm tra toàn diện chất lượng nội dung và trạng thái các node trong vault."""
from __future__ import annotations
import glob
import os
import re
import sys
import yaml
from pathlib import Path

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "02_wiki"

notes = [Path(p) for p in glob.glob(str(WIKI / "**/*.md"), recursive=True) 
         if not any(x in p for x in ["index.md", "log.md", "overview.md"])]

types = {}
mats = {}
drafts = []
short_notes = []
missing_cite_relations = []
missing_sources = []

for p in notes:
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        continue
    fm = yaml.safe_load(m.group(1)) or {}
    t = fm.get("type", "unknown")
    mat = fm.get("maturity", "unknown")
    types[t] = types.get(t, 0) + 1
    mats[mat] = mats.get(mat, 0) + 1
    stem = p.stem
    if mat == "draft":
        drafts.append(stem)
    
    # check relations for cite
    rels = fm.get("relations", []) or []
    for r in rels:
        if isinstance(r, dict) and not r.get("cite"):
            missing_cite_relations.append((stem, r.get("type"), r.get("to")))
    
    # check sources
    if t != "source" and not fm.get("sources"):
        missing_sources.append(stem)
        
    lines = len(text.splitlines())
    if lines < 30 and t != "entity":
        short_notes.append((stem, lines))

print(f"Tổng số notes: {len(notes)}")
print(f"Theo type: {types}")
print(f"Theo maturity: {mats}")
print(f"\nSố note draft ({len(drafts)}): {drafts}")
print(f"\nNotes ngắn (<30 dòng): {short_notes}")
print(f"\nRelations thiếu cite ({len(missing_cite_relations)}): {missing_cite_relations[:10]}...")
