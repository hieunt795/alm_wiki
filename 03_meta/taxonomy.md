---
title: Taxonomy
type: meta
---

# Taxonomy — nguồn sự thật cho mọi enum

Khối YAML dưới đây được `tools/lint.py` đọc trực tiếp. Muốn đổi enum thì sửa ở đây (thay đổi cần user duyệt) và ghi entry `decision` vào `02_wiki/log.md`.

```yaml taxonomy
domains:
  macro:   "Macroeconomic — chính sách tiền tệ, lãi suất, lạm phát, thanh khoản hệ thống"
  product: "Financial Product — fixed income, swap, derivatives, sản phẩm tiền gửi/cho vay"
  alm:     "ALM — IRRBB, thanh khoản, FTP, hành vi khách hàng, balance sheet management"
  basel:   "Basel — chuẩn mực BCBS: vốn, thanh khoản, IRRBB, đòn bẩy"
  vn-reg:  "VN Regulator — Luật TCTD, Nghị định, Thông tư NHNN"

types:
  concept:    concepts
  metric:     metrics
  instrument: instruments
  model:      models
  regulation: regulations
  entity:     entities
  synthesis:  syntheses
  source:     sources

status:   [active, superseded, retired]
maturity: [draft, reviewed, canonical]
tiers:    [T1, T2, T3, T4, T5]
doc_status: [final, consultative, draft]
origin:   [query, research]
jurisdiction: [VN, INTL]

relations:
  # Nhóm 1 — thành phần
  part-of:     "A là cấu phần của B"
  # Nhóm 2 — đo lường / quản trị / giới hạn
  measures:    "Chỉ tiêu hoặc model A đo lường, đánh giá B"
  governs:     "Quy định A điều chỉnh B"
  limits:      "A đặt ngưỡng hoặc ràng buộc lên B"
  # Nhóm 3 — tác động / đầu vào
  drives:      "A tác động lên B (tuỳ chọn direction: '+'|'-', regime)"
  input-to:    "A là đầu vào của tính toán hoặc quá trình B"
  # Khác
  hedges:      "A phòng ngừa B"
  priced-by:   "A được định giá bằng B"
  exposed-to:  "A chịu rủi ro B"
  implements:  "Quy định VN A nội luật hoá chuẩn Basel B"
  supersedes:  "A thay thế B"
  amends:      "A sửa đổi một phần B"

regimes: [rising_rate, falling_rate, stable_rate, stress, normal]

required_fields:
  all:        [title, type, domains, status, maturity, updated]
  knowledge:  [sources]            # mọi type trừ source
  regulation: [issuer, number, jurisdiction, doc_status]
  source:     [source_id, tier, raw]
  synthesis:  [origin, question]

macro_stale_months: 6
```

## Domain

| Code | Tên | Ghi chú |
|---|---|---|
| `macro` | Macroeconomic | Claim định lượng phải có `as_of` |
| `product` | Financial Product | |
| `alm` | ALM | |
| `basel` | Basel | Phân biệt `doc_status: consultative` và `final` |
| `vn-reg` | VN Regulator | Theo dõi sửa đổi, thay thế, hết hiệu lực |

`domains` là list; **phần tử đầu tiên = primary domain**.

## Relation

Khai trong frontmatter `relations` của node A, đọc theo chiều **A → B ở thể chủ động**. Chỉ khai một chiều; chiều ngược (B có thành phần A, B được A đo) đọc qua backlinks hoặc `grep -rn 'to: "\[\[<id>\]\]"' 02_wiki`.

| Nhóm | Relation | Nghĩa | Ví dụ |
|---|---|---|---|
| Thành phần | `part-of` | A là cấu phần của B | `cet1` → `tier-1-capital` |
| Đo lường / quản trị / giới hạn | `measures` | Chỉ tiêu hoặc model A đo lường, đánh giá B | `supervisory-outlier-test` → `irrbb` |
| | `governs` | Quy định A điều chỉnh B | `bcbs-lcr` → `lcr` |
| | `limits` | A đặt ngưỡng hoặc ràng buộc lên B | `lcr` → `hqla` |
| Tác động / đầu vào | `drives` | A tác động lên B, tuỳ chọn `direction`, `regime` | `deposit-beta` → `nii` (−, rising_rate) |
| | `input-to` | A là đầu vào của tính toán hoặc quá trình B | `behavioural-models` → `eve` |
| Khác | `hedges` · `priced-by` · `exposed-to` · `implements` · `supersedes` · `amends` | xem khối YAML | |

Chọn relation: A là một phần của B? → `part-of`. A là quy định? → `governs`. A đặt ngưỡng lên B? → `limits`. A đo B? → `measures`. B được tính từ A? → `input-to`. A làm B tăng/giảm? → `drives`.

Field của mỗi relation: `type`, `to` (bắt buộc); `cite` (tuỳ chọn, `[[src-…#^block-id]]`, nên có khi quan hệ là claim của nguồn); `direction`, `regime` (chỉ với `drives`); `confidence`.

```yaml
relations:
  - {type: governs, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr10-1]]"}
  - {type: drives, to: "[[nii]]", direction: "-", regime: rising_rate}
```

## Source tier (chỉ gán cho source note / registry)

| Tier | Loại |
|---|---|
| T1 | Luật, Nghị định, Thông tư (bắt buộc tại VN) |
| T2 | Chuẩn mực final của standard-setter, hướng dẫn chính thức |
| T3 | Dữ liệu/ấn phẩm chính thức, báo cáo đã kiểm toán |
| T4 | Sách giáo khoa, học thuật, tài liệu phương pháp |
| T5 | Research, commentary, báo chí |

Synthesis của LLM không có tier và không bao giờ được dùng làm nguồn.

## Quy ước ID và block-id

- **ID node = tên file** (không có `.md`), viết kebab-case tiếng Anh, duy nhất toàn vault, không chứa domain hay type. Ví dụ: `lcr`, `deposit-beta`, `tt50-2026-nhnn`.
- **ID source note** bắt đầu bằng `src-`, ví dụ `src-bcbs-lcr`. Collection trong registry bắt đầu bằng `col-`.
- **Block-id** trong source note có dạng `^<unit>-<số>`, chỉ dùng chữ thường, số và gạch ngang. Ví dụ: `^lcr40-1`, `^d5-2a` (Điều 5 khoản 2 điểm a), `^ch7-3`.
- **Citation** trong node: `[[src-bcbs-lcr#^lcr40-1]]`.

## Locator theo loại nguồn

| Nguồn | Locator | Ví dụ |
|---|---|---|
| Basel Framework | `<STD><chapter>.<para>` | `LCR40.70` |
| Thông tư VN | `Đ<điều>.<khoản>.<điểm>` | `Đ5.2.a` |
| BCBS standalone | `para <n>` / `§<n>` | `para 31` |
| Sách | `ch<n> §<n> p.<page>` | `ch7 §7.3 p.212` |
| Clipping | `¶<n>` | `¶3` |
