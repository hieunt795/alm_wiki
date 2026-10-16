---
title: Regulation timeline
type: meta
---

# Timeline quy định

Cần plugin **Dataview**.

## Đang có hiệu lực

```dataview
TABLE number, issuer, jurisdiction, valid_from, doc_status
FROM "02_wiki/regulations"
WHERE status = "active"
SORT valid_from DESC
```

## Đã bị thay thế / hết hiệu lực

```dataview
TABLE number, valid_from, valid_to, superseded_by
FROM "02_wiki/regulations"
WHERE status != "active"
SORT valid_to DESC
```

## Basel consultative (không dùng như final)

```dataview
LIST
FROM "02_wiki"
WHERE doc_status = "consultative"
```
