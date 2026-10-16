---
title: Open conflicts
type: meta
---

# Conflict đang mở

Node có callout `> [!conflict]` mà chưa ghi `Trạng thái: resolved`. Cần plugin **Dataview**, bật *Enable JavaScript Queries*.

```dataviewjs
const rows = [];
for (const p of dv.pages('"02_wiki"')) {
  const text = await dv.io.load(p.file.path);
  const blocks = text.split(/^> \[!conflict\]/m).slice(1);
  const open = blocks.filter(b => !/Trạng thái:\s*resolved/.test(b.split(/\n(?!>)/)[0])).length;
  if (open > 0) rows.push([p.file.link, p.type, p.domains, open, p.updated]);
}
dv.table(["Node", "Type", "Domains", "Open", "Updated"], rows);
```

Fallback không cần plugin: tìm `[!conflict]` trong Obsidian search, hoặc `grep -rn "\[!conflict\]" 02_wiki/`.
