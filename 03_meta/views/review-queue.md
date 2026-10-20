---
title: Review queue
type: meta
---

# Review queue

Node `draft` mới cập nhật gần đây nhất. Cần plugin **Dataview**.

```dataview
TABLE type, domains, updated, length(sources) AS "n_src"
FROM "02_wiki"
WHERE maturity = "draft" AND type != "source"
SORT updated DESC
```

## Đã review, chưa canonical

```dataview
TABLE type, reviewed
FROM "02_wiki"
WHERE maturity = "reviewed"
SORT reviewed DESC
```

## Có đề xuất cập nhật đang chờ

Cần bật *Enable JavaScript Queries* trong Dataview.

```dataviewjs
const hits = [];
for (const p of dv.pages('"02_wiki"')) {
  const text = await dv.io.load(p.file.path);
  const m = text.match(/\n## Đề xuất cập nhật\n([\s\S]*?)(?=\n## |$)/);
  if (m && /^- /m.test(m[1])) hits.push(p.file.link);
}
dv.list(hits);
```
