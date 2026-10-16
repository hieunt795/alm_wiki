# ALM Wiki LLM — Kiến trúc v2

> Phiên bản: v2 · 2026-10-15 · Thay thế thiết kế trong [[alm-wiki-llm-architecture]] (v1, giữ lại để tham khảo).
> Phạm vi: hệ thống tri thức cá nhân cho 5 domain — Macroeconomic, Financial Product, ALM, Basel, VN Regulator — vận hành theo pattern LLM Wiki của Karpathy.

---

## 0. Tóm tắt

| Câu hỏi | Trả lời |
|---|---|
| Hệ thống là gì? | Một Obsidian vault gồm markdown do LLM viết và duy trì, nằm giữa người dùng và tài liệu gốc. Tri thức được tích luỹ dần (compounding), không tái tạo lại ở mỗi câu hỏi như RAG. |
| Có mấy lớp? | 3 lớp: **raw** (`01_sources/`, bất biến) → **wiki** (`02_wiki/`, LLM viết, người đọc) → **schema** (`CLAUDE.md` + `03_meta/`, cùng tiến hoá). |
| Evidence ở đâu? | Trong **source note** (`02_wiki/sources/`). Mỗi claim có locator và trích nguyên văn. Không có lớp evidence riêng. |
| Có mấy operation? | 4: **Register**, **Ingest**, **Query**, **Lint**. Review/promote do người dùng làm bằng tay. |
| Có mấy loại node? | 7 loại tri thức (concept, metric, instrument, model, regulation, entity, synthesis) và source note. |
| Ai review? | Một người (chủ wiki). Maturity có 3 mức: `draft` → `reviewed` → `canonical`. |
| Ngôn ngữ? | Nội dung viết tiếng Việt, giữ thuật ngữ chuyên ngành EN. Tên file và ID viết EN. Alias có cả VN và EN. |

---

## 1. Nguyên tắc thiết kế

1. **Ba lớp, không trộn lẫn.** Raw là source of truth. Wiki là tri thức đã biên dịch. Schema quy định cách biên dịch. LLM đóng vai *knowledge compiler / maintainer*, không phải source of truth.
2. **Source says X ≠ Wiki interprets Y.** Phần nguồn nói gì nằm trong source note (trích nguyên văn + locator). Phần diễn giải và tổng hợp nằm trong node tri thức, luôn kèm citation về source note.
3. **Compounding.** Một lần ingest cập nhật nhiều node. Câu trả lời query có giá trị được lưu lại thành synthesis.
4. **Index + log là cơ chế điều hướng chính.** Chỉ thêm search tool khi index không còn đủ.
5. **Một khái niệm = một node.** Không nhân bản node theo domain, cũng không nhân bản theo node type. Domain là metadata many-to-many.
6. **Không xoá lịch sử.** Quy định hết hiệu lực được đánh dấu `superseded` hoặc `retired`, node vẫn còn để trả lời câu hỏi as-of.
7. **Không overwrite âm thầm.** Mâu thuẫn được ghi rõ, giữ cả hai phía.
8. **Đơn giản trước.** Lúc khởi đầu chỉ có 4 skill, không có agent nào, và 2 script. Chỉ mở rộng khi gặp vấn đề thực tế.

---

# PHẦN A — CẤU TRÚC HỆ THỐNG

## A.1. Cây thư mục

```text
202610 ALM wiki/                      ← Obsidian vault root
├── CLAUDE.md                         ← schema / constitution (≤ ~300 dòng)
├── alm-wiki-llm-architecture.md      ← v1 (tham khảo)
├── alm-wiki-architecture-v2.md       ← tài liệu này
│
├── 01_sources/                       ← LỚP RAW — bất biến, giữ nguyên cấu trúc hiện có
│   ├── alm/
│   │   ├── Basel/{BaselFramework, IRRBB-d368, LCR, LEV, NSF}/   (.md + _meta.json + ảnh)
│   │   ├── TT14_2025_SBV/  TT50_2026_SBV/  TT83_2025_SBV/      (.pdf + .docx + .md)
│   │   └── VAB - Phương pháp luận FTP/
│   ├── alm book/  choudhry_banking_fixed_income/  fixed_income_during/
│   ├── bindseil_monetary_policy/  cargill_central_bank_policy/  imf_macro_accounting/
│   ├── tata_bank_alm/  Modern Money Mechanics/  Capitalism and Freedom/
│   └── Clippings/                    ← web clip (Obsidian Web Clipper)
│
├── 02_wiki/                          ← LỚP WIKI — LLM viết, người đọc
│   ├── index.md                      ← catalog mọi node
│   ├── log.md                        ← append-only: register / ingest / query / lint / decision
│   ├── overview.md                   ← bản đồ tri thức + thesis đang tiến hoá
│   ├── sources/                      ← source note (evidence)
│   ├── concepts/
│   ├── metrics/
│   ├── instruments/
│   ├── models/
│   ├── regulations/
│   ├── entities/
│   └── syntheses/
│
├── 03_meta/                          ← SCHEMA chi tiết (CLAUDE.md tham chiếu tới đây)
│   ├── sources.yaml                  ← source registry
│   ├── taxonomy.md                   ← enum: domain, type, status, maturity, relation, tier, tag
│   ├── templates/                    ← Obsidian template, 1 file / node type
│   └── views/                        ← Dataview dashboard
│       ├── review-queue.md           ← draft mới đổi, chờ review
│       ├── open-conflicts.md         ← conflict callout chưa xử lý
│       └── regulation-timeline.md    ← quy định theo hiệu lực
│
├── .claude/
│   ├── settings.json                 ← permissions.deny Edit/Write trên 01_sources/**
│   └── skills/
│       ├── register/SKILL.md
│       ├── ingest/SKILL.md
│       ├── query/SKILL.md
│       └── lint/SKILL.md
│
└── tools/
    ├── units.py                      ← tách nguồn thành ingest unit theo heading → sources.yaml
    └── lint.py                       ← kiểm tra deterministic trên 02_wiki/
```

## A.2. Vai trò từng thành phần

| Thành phần | Vai trò | Ai ghi |
|---|---|---|
| `01_sources/` | Tài liệu gốc (pdf/docx) + bản markdown do marker convert + `_meta.json` (TOC, `page_id`) | Người dùng thêm file; **LLM không bao giờ sửa** |
| `02_wiki/sources/` | Source note: metadata nguồn, tóm tắt, key claims có locator + trích nguyên văn | LLM |
| `02_wiki/<type>/` | Node tri thức đã biên dịch | LLM viết draft; người dùng review |
| `index.md` | Catalog nội dung, LLM đọc đầu tiên khi query | LLM |
| `log.md` | Nhật ký theo thời gian, có prefix để grep | LLM (append-only) |
| `overview.md` | Bản đồ domain → node trung tâm, thesis chính, câu hỏi mở lớn | LLM, người dùng định hướng |
| `CLAUDE.md` | Mission, quy tắc cốt lõi, write policy, tham chiếu `03_meta/` và skills | Người dùng + LLM cùng tiến hoá |
| `03_meta/sources.yaml` | Registry: id, path, hash, tier, domain, doc_status, ngày, conversion, units | LLM qua skill `register`/`ingest` |
| `03_meta/taxonomy.md` | Nguồn sự thật duy nhất cho mọi enum | Người dùng duyệt thay đổi |
| `.claude/skills/` | Quy trình từng bước cho 4 operation | Người dùng + LLM |
| `tools/` | Việc deterministic (tách unit, lint), không tốn token | LLM viết, người dùng duyệt |

## A.3. `CLAUDE.md` — nội dung tối thiểu

```text
1. Mission (3–5 dòng)
2. Bản đồ thư mục (rút gọn A.1)
3. Quy tắc cốt lõi (12 điều, mục A.4)
4. Write policy (mục B.6)
5. Quy tắc chọn node type (mục C.1) + frontmatter bắt buộc (C.2)
6. Citation format (C.6)
7. Tham chiếu: 03_meta/taxonomy.md, 03_meta/templates/, .claude/skills/*
```

Các chi tiết dài (template, enum) không đưa vào `CLAUDE.md` mà để trong `03_meta/`, để file constitution ngắn và ổn định.

## A.4. Quy tắc cốt lõi

1. `01_sources/` bất biến, enforce bằng `permissions.deny` trong `.claude/settings.json`.
2. Mọi factual claim trong node phải có citation về source note.
3. Source note chỉ ghi điều nguồn nói. Diễn giải của LLM không bao giờ được coi là nguồn.
4. Không bịa nguồn, locator hay số liệu. Thiếu thì ghi `[cần nguồn]`.
5. Mọi fact phụ thuộc thời gian phải có `valid_from`/`valid_to` hoặc `as_of`.
6. Không xoá node, không xoá lịch sử. Thay thế bằng `status: superseded|retired`.
7. Mâu thuẫn ghi bằng callout `> [!conflict]`, giữ cả hai claim, không overwrite.
8. Một khái niệm chỉ có một node. Domain là metadata.
9. Thư mục wiki tổ chức theo node type.
10. Query đọc wiki trước, chỉ quay về raw để verify.
11. Node `reviewed`/`canonical`: LLM chỉ đề xuất, không sửa thân bài.
12. Basel consultative paper không được dùng như final standard.

---

# PHẦN B — THIẾT KẾ OPERATION

## B.0. Ingest unit — khái niệm nền

Corpus có nhiều nguồn rất lớn (`BaselFramework.md` 3,6 MB; `Choudhry_Principles_of_Banking.md` 2,6 MB). Pattern của Karpathy là ingest từng nguồn một, mỗi lần chạm 10–15 trang. Với nguồn lớn, phải hạ đơn vị ingest từ *nguồn* xuống **ingest unit**.

| Loại nguồn | Cách tách unit | Locator | Ví dụ thật |
|---|---|---|---|
| Basel Framework | Theo chapter (`## LCR40 …`) | `LCR40.70` (số đoạn `**40.70**`) | `01_sources/alm/Basel/LCR/LCR.md`, dòng 701: `## LCR40 Cash inflows and outflows` |
| Thông tư NHNN | Theo Chương; Chương dài thì theo nhóm Điều | `Đ5.2.a` (Điều 5, khoản 2, điểm a) | `14_2025_TT-NHNN.md`: `#### Điều 1. Phạm vi điều chỉnh…` |
| Sách / giáo trình | Theo chapter | `ch7 §7.3 p.212` (page từ `_meta.json` → `page_id`) | Choudhry, During |
| BCBS standalone (d368) | Theo section | `§ 4.2` / `para 31` | `IRRBB-d368/d368_irrbb.md` |
| Clipping | Cả bài = 1 unit, ingest theo batch | `¶3` (đoạn thứ 3) | `01_sources/Clippings/*.md` |

Trạng thái unit được ghi trong `sources.yaml`: `pending` → `done` (hoặc `skipped` nếu không liên quan ALM).

## B.1. OP1 — Register (onboard nguồn)

**Trigger:** `/register <path>` khi thêm tài liệu mới vào `01_sources/`.

```text
file mới trong 01_sources/
   ↓ 1. hash SHA-256 + so trùng (cùng hash → bỏ; cùng tên/size khác hash → hỏi người dùng)
   ↓ 2. gán source_id, tier, domains, doc_status, ngày ban hành / hiệu lực
   ↓ 3. kiểm tra chất lượng convert (lấy mẫu): heading, bảng, công thức, footnote, encoding tiếng Việt
   ↓ 4. tools/units.py → danh sách unit (heading, line range) trạng thái pending
   ↓ 5. ghi sources.yaml + log
registry entry
```

Ví dụ entry `03_meta/sources.yaml`:

```yaml
- id: src-bcbs-lcr
  title: "LCR — Liquidity Coverage Ratio (Basel Framework)"
  path: 01_sources/alm/Basel/LCR/LCR.md
  original: null                     # bản md sinh từ BIS website, không có pdf gốc
  meta: 01_sources/alm/Basel/LCR/LCR_meta.json
  sha256: "…"
  issuer: BCBS
  tier: T2
  doc_status: final                  # final | consultative | draft
  domains: [basel, alm]
  published: 2025-12-17              # ngày generate bản consolidated
  effective: 2019-12-15
  conversion: {status: ok, issues: []}
  units:
    - {id: LCR10, heading: "Definitions and application", lines: [11, 47],   status: pending}
    - {id: LCR40, heading: "Cash inflows and outflows",   lines: [701, 1324], status: pending}
```

Khi convert có lỗi:

```yaml
  conversion:
    status: partial
    issues:
      - {loc: "p.37", type: table, note: "Cột bảng lệch so với PDF"}
```

**Lưu ý từ corpus hiện tại:** trong `alm book/` có 2 file cùng tên sách Bardaeva và cùng kích thước 392 KB nhưng **khác hash**. Khi register phải hỏi người dùng giữ bản nào làm canonical. Không tự xoá.

## B.2. OP2 — Ingest (biên dịch tri thức)

**Trigger:** `/ingest <source_id> [unit]`. Mặc định ingest **một unit mỗi lần** và người dùng tham gia trực tiếp, như Karpathy khuyến nghị. Batch chỉ dùng cho nguồn T5 (Clippings).

```text
unit pending
   ↓ 1. Đọc unit (raw md theo line range). Nghi lỗi convert → mở pdf/docx đối chiếu.
   ↓ 2. Trao đổi với người dùng: 3–5 takeaway + danh sách node dự kiến tạo/cập nhật.
   ↓ 3. Viết/cập nhật SOURCE NOTE: tóm tắt + key claims (locator + trích nguyên văn).
   ↓ 4. Với mỗi node bị ảnh hưởng (thường 5–15):
   │      - chưa có → tạo từ template, maturity: draft
   │      - có, draft → cập nhật thân bài + citation + relations
   │      - có, reviewed/canonical → ghi vào mục "## Đề xuất cập nhật"
   ↓ 5. Mâu thuẫn với nội dung hiện có → callout [!conflict] (xem B.5)
   ↓ 6. Quy định mới sửa đổi/thay thế quy định cũ → đề xuất superseded (người dùng duyệt)
   ↓ 7. Cập nhật index.md, overview.md (nếu thay đổi bức tranh lớn), sources.yaml (unit → done)
   ↓ 8. Append log.md
```

Output báo cáo cuối mỗi lần ingest (in ra chat và ghi vào log):

```yaml
source: src-bcbs-lcr
unit: LCR40
created:  [run-off-rate, retail-deposit-stability]
updated:  [lcr, hqla, nmd-behaviour]
proposed: [deposit-beta]            # node reviewed → chỉ đề xuất
conflicts: [lcr]                    # có callout mới
```

## B.3. OP3 — Query

**Trigger:** `/query <câu hỏi>`, hoặc hỏi trực tiếp trong session.

```text
câu hỏi
   ↓ 1. Phân loại: định nghĩa | cơ chế | so sánh Basel–VN | số liệu | as-of lịch sử | tổng hợp
   ↓ 2. Temporal: "hiện hành" (hôm nay) hay "as-of <ngày>" → lọc node theo valid_from/valid_to
   ↓ 3. Đọc index.md → chọn node → đọc node + node liên quan qua relations
   ↓ 4. Verify khi cần (số liệu, ngưỡng quy định): citation → source note → raw md (grep locator)
   ↓ 5. Trả lời: citation [[...]], ghi rõ maturity của node dùng, as_of của số liệu
   ↓ 6. Hỏi: "Lưu thành synthesis?" → có: tạo node syntheses/, cập nhật index, log
```

Quy tắc trả lời:
- Câu trả lời dựa vào node `draft` phải ghi rõ: *"dựa trên node draft, chưa review"*.
- Câu hỏi về nghĩa vụ tại VN: quy định NHNN (T1) có hiệu lực là căn cứ. Basel chỉ là tham chiếu.
- Wiki không có thông tin → nói rõ là không có và đề xuất nguồn hoặc unit cần ingest. Không trả lời từ kiến thức nền mà không đánh dấu.

## B.4. OP4 — Lint

**Trigger:** `/lint`, định kỳ hoặc sau mỗi khoảng 10 lần ingest.

**Phần deterministic** (`tools/lint.py`, không tốn token):

| Check | Điều kiện lỗi |
|---|---|
| Broken link | `[[x]]` không có file `x.md` |
| Orphan | Node không có link trỏ vào (trừ index) |
| Schema | Thiếu field bắt buộc; giá trị ngoài enum `taxonomy.md` |
| ID trùng | Trùng tên file hoặc trùng alias giữa 2 node |
| Thiếu nguồn | Node tri thức có `sources: []` |
| Temporal | `valid_to` < hôm nay mà `status: active` |
| Supersession | `supersedes`/`superseded_by` không đối xứng |
| Macro stale | `as_of` cũ hơn 6 tháng ở node domain `macro` |
| Unit tồn đọng | Unit `pending` của nguồn đã register > 60 ngày (chỉ thống kê) |

Không kiểm tra "thiếu `valid_to`", vì quy định còn hiệu lực thì `valid_to` trống là đúng.

**Phần LLM** (skill `lint`):
- Mâu thuẫn ngầm giữa các node (cùng tham số, khác giá trị, không có callout).
- Basel consultative được trích như final.
- Thuật ngữ được nhắc ở ≥ 3 node nhưng chưa có node riêng.
- Synthesis cũ có nguồn mới liên quan chưa được tích hợp.
- Lỗ hổng tri thức → đề xuất unit cần ingest hoặc nguồn cần bổ sung.
- Conflict callout mở quá lâu.

Kết quả ghi vào `log.md`. Các sửa đổi được gom thành batch để người dùng duyệt trước khi áp dụng.

## B.5. Xử lý mâu thuẫn (trong Ingest/Lint)

Khi hai claim khác nhau, kiểm tra **theo thứ tự**:

```text
1. Có thực sự cùng đối tượng?  entity · sản phẩm/loại tiền gửi · kỳ · methodology · rate regime
   → khác nhau ở bất kỳ chiều nào: KHÔNG phải mâu thuẫn, ghi rõ phạm vi của từng claim
2. Jurisdiction   VN vs quốc tế
3. Scope          đối tượng áp dụng (NHTM, chi nhánh NHNN ngoài, …)
4. Hiệu lực       claim nào đang có hiệu lực tại thời điểm xét
5. Specificity    quy định cụ thể > quy định chung
6. Tier           T1 > T2 > … > T5
```

Không áp dụng nguyên tắc "newer wins" một cách tự động. Mẫu callout:

```markdown
> [!conflict] Run-off rate tiền gửi bán lẻ ổn định
> - Basel: thường 5% [[src-bcbs-lcr#^lcr40-7]]; jurisdiction có thể áp 3% nếu đủ điều kiện [[src-bcbs-lcr#^lcr40-11]]
> - VN: … (theo [[src-tt50-2026-nhnn#^d…]])
> - Đánh giá: khác jurisdiction → không mâu thuẫn; VN áp dụng cho NHTM tại VN.
> - Trạng thái: open | resolved (2026-10-20)
```

## B.6. Review / Promote và Write policy

**Review** do người dùng làm: đọc node, sửa `maturity: reviewed` (hoặc `canonical`) và điền `reviewed: <ngày>`. Dashboard `03_meta/views/review-queue.md` (Dataview) liệt kê các node `draft` theo `updated` mới nhất.

| Mức | Ý nghĩa | Ai đặt |
|---|---|---|
| `draft` | LLM vừa tạo/cập nhật | LLM |
| `reviewed` | Người dùng đã đọc và chấp nhận | Người dùng |
| `canonical` | Chuẩn tham chiếu; định nghĩa, ngưỡng quy định, phương pháp đã chốt | Người dùng |

| LLM tự làm | LLM đề xuất, người dùng duyệt | Cấm |
|---|---|---|
| Source note; node `draft`; cross-link; relations; conflict callout; synthesis draft; index, overview, log, registry | Sửa thân bài node `reviewed`/`canonical`; diễn giải quy định; phương pháp model và giả định; đánh dấu `superseded`/`retired`; thay đổi `taxonomy.md` | Sửa `01_sources/`; xoá node hoặc lịch sử; xoá conflict; bịa nguồn, locator hay số liệu |

## B.7. Skills và vì sao không có agent

| Skill | Operation | Input | Output |
|---|---|---|---|
| `register` | OP1 | path trong `01_sources/` | entry `sources.yaml`, log |
| `ingest` | OP2 | `source_id` [+ unit] | source note, node, index, log |
| `query` | OP3 | câu hỏi [+ as-of] | câu trả lời có citation; tuỳ chọn synthesis |
| `lint` | OP4 | — | báo cáo lint, đề xuất batch fix |

**Không dùng agent ở giai đoạn đầu.** Lý do:
1. Ingest cần người dùng tham gia, không phù hợp với subagent chạy nền.
2. Subagent của Claude Code không gọi lồng được subagent khác, nên chuỗi ingestor → compiler → linter phải do session chính điều phối.
3. Thêm agent nghĩa là thêm một lớp phải bảo trì.

Có thể cân nhắc một agent read-only cho lint khi wiki vượt khoảng 500 node.

---

# PHẦN C — PHÂN LỚP WIKI NODE

## C.1. Các loại node và quy tắc chọn

| Type | Thư mục | Mô tả | Ví dụ |
|---|---|---|---|
| `concept` | `concepts/` | Cơ chế, hiện tượng, khung tư duy | IRRBB, yield curve, term premium, NMD behaviour, liquidity transformation, basis risk, funding stability |
| `metric` | `metrics/` | Đại lượng đo được, có công thức | LCR, NSFR, EVE, ΔEVE, NII sensitivity, duration, DV01, duration gap, liquidity gap, deposit beta, CAR |
| `instrument` | `instruments/` | Hợp đồng hoặc sản phẩm giao dịch được | government bond, IRS, CCS, OIS, FRA, repo, FX swap, cap/floor, swaption, FRN, callable bond |
| `model` | `models/` | Phương pháp định lượng cần giả định và calibration | NMD behavioural model, prepayment model, FTP model, NII simulation, liquidity stress model |
| `regulation` | `regulations/` | Văn bản hoặc chuẩn mực có hiệu lực | `tt14-2025-nhnn`, `tt50-2026-nhnn`, `tt83-2025-nhnn`, `bcbs-lcr`, `bcbs-irrbb-2016` |
| `entity` | `entities/` | Tổ chức, đồng tiền, chỉ số | SBV, Fed, ECB, BIS, BCBS, VND, VNIBOR, SOFR |
| `synthesis` | `syntheses/` | Tổng hợp cross-source/cross-domain, từ query hoặc research | "Deposit beta VN trong chu kỳ tăng lãi suất", "So sánh LCR Basel và VN" |
| `source` | `sources/` | Source note (evidence) | `src-bcbs-lcr`, `src-tt14-2025-nhnn`, `src-choudhry-yield-curve` |

**Quy tắc chọn type:** hỏi lần lượt các câu dưới đây, dừng ở câu đầu tiên trả lời "có".

```text
1. Là văn bản / chuẩn mực có hiệu lực?             → regulation
2. Là tổ chức, đồng tiền, chỉ số thị trường?        → entity
3. Là hợp đồng / sản phẩm giao dịch được?          → instrument
4. Là đại lượng đo được, có công thức?             → metric
5. Là phương pháp định lượng cần giả định/calibrate? → model
6. Còn lại                                         → concept
```

Áp dụng cho các trường hợp hay bị xếp trùng:
- **Deposit beta** là metric (một hệ số đo được). Hành vi tiền gửi nằm ở concept `nmd-behaviour`, phương pháp ước lượng nằm ở model `nmd-behavioural-model`.
- **EVE** là metric. Khung quản trị rủi ro nằm ở concept `irrbb`. Yêu cầu tính toán nằm ở regulation `bcbs-irrbb-2016`.
- **Basis risk** là concept: một loại rủi ro, không có một công thức duy nhất.
- **LCR** là metric. Văn bản chuẩn mực là regulation `bcbs-lcr`, quy định VN tương ứng là regulation `tt50-2026-nhnn`.
- **Mọi đại lượng trong công thức của một metric đều là metric**, vì về nguyên tắc mọi đại lượng cấu thành một chỉ số đều phải được quản trị. Gồm tử số và mẫu số (`hqla`, `net-cash-outflows`, `available-stable-funding`, `leverage-exposure-measure`), tổng phụ (`cash-outflows`, `cash-inflows`), nhóm cấu phần (`level-1-assets`, `operational-deposits`, `secured-funding`, `asf-*`, `rsf-*`).
- **Tham số do cơ quan quản lý ấn định** (run-off rate, hệ số ASF/RSF, haircut, drawdown rate) không phải metric vì không đo từ dữ liệu. Tham số được trình bày trong node dùng nó; nếu cần node riêng thì dùng concept (ví dụ `run-off-rate`). Deposit beta khác: hệ số này ước lượng từ dữ liệu nên là metric.
- **Phương pháp đo do cơ quan quản lý quy định** vẫn là model nếu nó là quy trình định lượng có giả định (ví dụ `irrbb-standardised-framework`). Ngưỡng hoặc phép thử dựa trên một tỷ số (ví dụ `outlier-bank-test`: max ΔEVE / Tier 1 > 15%) là metric.

**Không có node "definition" riêng.** Định nghĩa là mục đầu tiên của concept/metric/instrument. **Không có node "relationship" riêng.** Quan hệ được khai báo trong frontmatter (C.3).

## C.2. Frontmatter chung

```yaml
---
title: Liquidity Coverage Ratio (LCR)
aliases: [LCR, Tỷ lệ dự trữ thanh khoản]
type: metric                     # concept|metric|instrument|model|regulation|entity|synthesis|source
domains: [alm, basel, vn-reg]    # phần tử đầu tiên = primary domain
status: active                   # active | superseded | retired
maturity: draft                  # draft | reviewed | canonical
valid_from:                      # khi tri thức/quy định có hiệu lực theo thời gian
valid_to:
as_of:                           # ngày quan sát số liệu (macro, thị trường)
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: measured-by, to: "[[hqla]]"}
  - {type: required-by, to: "[[bcbs-lcr]]"}
  - {type: required-by, to: "[[tt50-2026-nhnn]]"}
tags: [liquidity]
updated: 2026-10-15
reviewed:
---
```

| Field | Quy tắc |
|---|---|
| ID | = tên file, kebab-case EN, duy nhất toàn vault, **không chứa domain hay type** |
| `domains` | Enum: `macro`, `product`, `alm`, `basel`, `vn-reg` |
| `status` | Vòng đời hiệu lực, tách bạch với `maturity` (độ tin cậy biên dịch) |
| `valid_from`/`valid_to` | Thời kỳ tri thức hoặc quy định đúng. Để trống `valid_to` = còn hiệu lực |
| `as_of` | Ngày của số liệu. Bắt buộc với claim định lượng thuộc domain `macro` |
| `sources` | Chỉ trỏ tới source note, không trỏ thẳng vào raw |
| `aliases` | Có cả tên VN và EN. Obsidian dùng alias để resolve link |

Field riêng theo loại:

```yaml
# regulation
issuer: SBV                       # SBV | BCBS | QH | CP | …
number: 50/2026/TT-NHNN
jurisdiction: VN                  # VN | INTL
doc_status: final                 # final | consultative | draft
issued: 2026-..-..
effective_from: 2026-..-..        # = valid_from; có thể có nhiều mốc → bảng "Lộ trình" trong thân bài
supersedes: []                    # ["[[…]]"]
superseded_by:
amends: []
implements: []                    # VN → Basel, vd ["[[bcbs-lcr]]"]

# source
tier: T2                          # T1…T5
raw: 01_sources/alm/Basel/LCR/LCR.md
units_done: [LCR10, LCR40]

# synthesis
origin: query                     # query | research
question: "…"
```

## C.3. Relation vocabulary

Chỉ khai báo trong `relations` ở frontmatter. Link tự do trong thân bài được hiểu là "related". Relation khai ở node A, đọc theo chiều A → B ở thể chủ động, chỉ một chiều; chiều ngược đọc qua backlinks. Enum và cách chọn relation: `03_meta/taxonomy.md`, mục "Relation".

| Nhóm | Relation | Nghĩa | Ví dụ |
|---|---|---|---|
| Thành phần | `part-of` | A là cấu phần của B | CET1 → `part-of` → Tier 1 Capital |
| Đo lường / quản trị / giới hạn | `measures` | Chỉ tiêu hoặc model A đo lường, đánh giá B | Supervisory Outlier Test → `measures` → IRRBB |
| | `governs` | Quy định A điều chỉnh B | tt50-2026-nhnn → `governs` → LCR |
| | `limits` | A đặt ngưỡng hoặc ràng buộc lên B | LCR → `limits` → HQLA |
| Tác động / đầu vào | `drives` | A tác động lên B (thêm `direction: +/-`, `regime`) | deposit beta → `drives` (−, rising_rate) → NII |
| | `input-to` | A là đầu vào của tính toán hoặc quá trình B | behavioural models → `input-to` → EVE, NII |
| Khác | `hedges` | A phòng ngừa B | IRS → `hedges` → EVE sensitivity |
| | `priced-by` | A được định giá bằng B | IRS → `priced-by` → OIS curve |
| | `exposed-to` | A chịu rủi ro B | fixed-rate mortgage → `exposed-to` → prepayment risk |
| | `implements` | Quy định VN A nội luật hoá chuẩn Basel B | tt14-2025-nhnn → `implements` → Basel capital standards |
| | `supersedes` | A thay thế B | (giữa các regulation) |
| | `amends` | A sửa đổi một phần B | (giữa các regulation) |

Bộ cũ `causes`, `affects`, `constrains`, `measured-by`, `required-by` đã bị thay ngày 2026-10-15 (xem `02_wiki/log.md`).

Field: `type`, `to` bắt buộc; `cite: "[[src-…#^block-id]]"` tuỳ chọn, nên có khi quan hệ là claim của nguồn (lint kiểm block-id); `direction`, `regime` chỉ dùng với `drives`; `confidence`.

```yaml
relations:
  - {type: governs, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr10-1]]"}
  - {type: drives, to: "[[nii]]", direction: "-", regime: rising_rate, confidence: medium}
```

## C.4. Source authority (chỉ gán cho source note)

| Tier | Loại | Ví dụ trong corpus |
|---|---|---|
| T1 | Luật, Nghị định, Thông tư (bắt buộc tại VN) | TT14/2025 (an toàn vốn), TT50/2026 (giới hạn, tỷ lệ an toàn), TT83/2025 (kiểm soát nội bộ) |
| T2 | Chuẩn mực final của standard-setter, hướng dẫn chính thức | Basel Framework (LCR, NSF, LEV), IRRBB d368 |
| T3 | Dữ liệu/ấn phẩm chính thức, báo cáo đã kiểm toán | IMF Macroeconomic Accounting, báo cáo ALM Tata Bank |
| T4 | Sách giáo khoa, học thuật, tài liệu phương pháp | Choudhry, During, Bindseil, Cargill, Bardaeva, VAB FTP |
| T5 | Research, commentary, báo chí | Clippings |

- Synthesis của LLM **không có tier** và không bao giờ được dùng làm nguồn.
- Thứ tự tier không áp dụng máy móc giữa các domain. Với số liệu macro, nguồn T3 chính thức (NHTW, IMF) là chuẩn. Với nghĩa vụ tuân thủ tại VN, T1 VN thắng Basel.

## C.5. Template từng loại

Mỗi template nằm ở `03_meta/templates/<type>.md`. Mục nào không có nội dung thì bỏ, không để trống.

**source** — `sources/src-*.md`
```text
## Thông tin nguồn      issuer, tier, doc_status, ban hành/hiệu lực, path raw, conversion
## Tóm tắt              5–10 dòng
## Key claims           theo unit; mỗi claim: diễn đạt ngắn + "trích nguyên văn" + locator + ^block-id
## Node bị ảnh hưởng    danh sách [[…]]
## Mâu thuẫn ghi nhận
## Ghi chú convert
```

**concept**
```text
## Ý chính · ## Cơ chế & drivers · ## Phụ thuộc regime
## Góc nhìn theo domain   (chỉ domain liên quan: Macro / Product / ALM / Basel / VN)
## Bằng chứng thực nghiệm · ## Câu hỏi mở
```

**metric**
```text
## Định nghĩa · ## Công thức · ## Diễn giải
## Basel vs VN           bảng: tham số | Basel | VN | điều khoản | hiệu lực
## Ứng dụng trong ALM · ## Nhầm lẫn thường gặp
```

**instrument**
```text
## Định nghĩa & cashflow · ## Pricing · ## Risk factors & sensitivities
## ALM & hedging usage · ## Kế toán · ## Basel treatment · ## Lưu ý tại VN
```

**model**
```text
## Mục tiêu · ## Công thức · ## Inputs & giả định · ## Calibration
## Output & usage (regulatory / management) · ## Hạn chế & validation
```

**regulation**
```text
## Mục đích & phạm vi
## Yêu cầu chính         bảng: điều khoản | yêu cầu | ngưỡng | hiệu lực / lộ trình
## Định nghĩa đáng chú ý · ## Báo cáo & nghĩa vụ · ## Ngoại lệ
## Sửa đổi / thay thế    timeline
## Đối chiếu Basel       (với regulation VN)
## Tác động ALM
```

**entity**
```text
## Vai trò · ## Công cụ / chính sách · ## Timeline · ## Liên quan ALM
```

**synthesis**
```text
## Câu hỏi · ## Kết luận · ## Cơ chế
## Bằng chứng ủng hộ · ## Bằng chứng trái chiều · ## Phụ thuộc regime
## Hàm ý ALM / quy định · ## Bất định
```

## C.6. Citation và provenance chain

Citation dùng **Obsidian block reference**, trỏ tới đúng claim trong source note:

```markdown
<!-- trong metrics/lcr.md -->
Tổng dòng tiền ra ròng được tính trong 30 ngày dưới kịch bản stress [[src-bcbs-lcr#^lcr40-1]].
```

```markdown
<!-- trong sources/src-bcbs-lcr.md -->
### LCR40 — Cash inflows and outflows
- Total net cash outflows = tổng dòng ra kỳ vọng − tổng dòng vào kỳ vọng trong 30 ngày stress.
  > "The term total net cash outflows is defined as the total expected cash outflows minus total expected cash inflows in the specified stress scenario for the subsequent 30 calendar days."
  > — LCR40.1 ^lcr40-1
```

Chuỗi truy ngược:

```text
metrics/lcr.md  ──[[src-bcbs-lcr#^lcr40-1]]──►  sources/src-bcbs-lcr.md (trích nguyên văn + LCR40.1)
     ──grep "**40.1**"──►  01_sources/alm/Basel/LCR/LCR.md (dòng 709)
     ──_meta.json page_id──►  trang trong pdf/bản gốc
```

Quy ước block-id: chữ thường, chỉ có chữ, số và gạch ngang, dạng `^<unit>-<số>`, ví dụ `^lcr40-1`, `^d5-2a`, `^ch7-3`.

Độ hạt source note: **mặc định một source note cho mỗi nguồn**, mỗi unit là một heading. Nguồn có trên 20 unit (BaselFramework, sách dày) thì tách thành một note cho mỗi unit (`src-choudhry-principles-ch07`), kèm một note cha `src-choudhry-principles` liệt kê các note con.

## C.7. Index, log, overview

**`index.md`** nhóm theo type, mỗi node một dòng:

```markdown
## Metrics
- [[lcr]] — HQLA / dòng ra ròng 30 ngày stress · alm, basel, vn-reg · draft
- [[deposit-beta]] — mức truyền dẫn lãi suất thị trường vào lãi suất tiền gửi · alm, macro · reviewed
```

Khi wiki vượt khoảng 300 node, tách thành sub-index theo type (`index-metrics.md`, …) và giữ `index.md` làm mục lục cấp 1.

**`log.md`** append-only, có prefix để grep:

```markdown
## [2026-10-15] ingest | src-bcbs-lcr LCR40
- created: [[run-off-rate]]
- updated: [[lcr]], [[hqla]]
- conflicts: [[lcr]]
```

```bash
grep "^## \[" 02_wiki/log.md | tail -5        # 5 hoạt động gần nhất
grep "^## \[.*\] ingest" 02_wiki/log.md        # lịch sử ingest
```

Loại entry: `register`, `ingest`, `query`, `lint`, `decision` (quyết định schema, review quan trọng).

**`overview.md`** gồm: 5 domain → các node trung tâm của từng domain, các thesis đang hình thành, câu hỏi mở lớn, và tiến độ ingest (số unit done/pending của mỗi nguồn). LLM cập nhật khi bức tranh lớn thay đổi.

## C.8. Domain model

| Code | Domain | Phạm vi | Node trung tâm (dự kiến) |
|---|---|---|---|
| `macro` | Macroeconomic | Chính sách tiền tệ, lãi suất, lạm phát, thanh khoản hệ thống, cán cân | monetary-transmission, yield-curve, term-premium, sbv |
| `product` | Financial Product | Fixed income, swap, derivatives, sản phẩm tiền gửi/cho vay | government-bond, irs, ois, repo, fx-swap |
| `alm` | ALM | IRRBB, thanh khoản, FTP, hành vi khách hàng, balance sheet management | irrbb, eve, nii-sensitivity, ftp-model, nmd-behaviour |
| `basel` | Basel | Chuẩn mực BCBS: vốn, thanh khoản, IRRBB, đòn bẩy | bcbs-lcr, bcbs-nsfr, bcbs-irrbb-2016, leverage-ratio |
| `vn-reg` | VN Regulator | Thông tư/Nghị định NHNN, Luật TCTD | tt14-2025-nhnn, tt50-2026-nhnn, tt83-2025-nhnn |

Ví dụ node đa domain:

```yaml
# concepts/yield-curve.md      domains: [macro, product, alm]
# instruments/irs.md           domains: [product, alm, basel]
# concepts/irrbb.md            domains: [alm, basel, vn-reg]
```

## C.9. Search khi wiki lớn dần

| Quy mô | Cơ chế |
|---|---|
| < ~300 node | `index.md` + grep trên `02_wiki/` |
| Raw quá lớn (BaselFramework 3,6 MB) | Không đọc cả file: grep locator/heading, đọc theo line range trong `sources.yaml` |
| Index không còn đủ để chọn node | Thêm **qmd** (local, BM25 + vector + LLM re-rank, có MCP server) |

---

# PHẦN D — THAY ĐỔI SO VỚI v1

| v1 | v2 | Lý do |
|---|---|---|
| `source-original/` + `source-md/` tách thư mục | `01_sources/` giữ chung; trạng thái convert ghi trong `sources.yaml` | Không phải move 249 file; marker output vốn để chung |
| Lớp `evidence/` với claim atomic | Source note trong `02_wiki/sources/` | Giảm số file một bậc; vẫn trace được đến đoạn/điều |
| 10 node type, có `definition`, `relationship`, `analysis` | 7 type + source | Định nghĩa là một mục; quan hệ nằm trong frontmatter; analysis gộp vào synthesis |
| Deposit Beta/EVE thuộc 2–3 type | Quy tắc chọn type một chiều (C.1) | Một khái niệm = một node |
| `status: synthesized` + `maturity: M2` | `status` (vòng đời) tách khỏi `maturity` (3 mức) | Hết chồng chéo |
| M0–M5 | draft → reviewed → canonical | Chỉ một người review |
| ID dạng `CONCEPT-ALM-DEPOSIT-BETA` | ID = tên file kebab-case, không chứa domain/type | Đổi primary domain không làm gãy ID; Obsidian resolve trực tiếp |
| Domain viết 3 kiểu (`VN Regulator`, `VN-Regulator`, `regulator-vn`) | Enum duy nhất `vn-reg` trong `taxonomy.md` | Lint và routing không bị lệch |
| `effective_from` + `valid_from` + `observed_at` | `valid_from`/`valid_to` + `as_of`; ngày ban hành chỉ ở regulation/source | Mỗi field một ngữ nghĩa |
| Authority A1–A10, có `derived` lạc thang | T1–T5; LLM synthesis không có tier | Gọn, áp dụng theo domain |
| Lint "missing `valid_to`" | Lint "`valid_to` đã qua mà còn active" | Quy định còn hiệu lực thì không có `valid_to` |
| 9 agent, 10 skill, 6 command, 7 rule file | 0 agent, 4 skill, quy tắc nằm trong `CLAUDE.md` | Giảm gánh bảo trì; subagent không gọi lồng được |
| `config/` + `.claude/schemas/` + `.claude/context/` | `03_meta/` duy nhất | Một nguồn sự thật |
| `INDEX.md`, `CHANGELOG.md`, 4 file log | `index.md` + `log.md` | Đúng pattern Karpathy |
| `archive/` | Không có; node retired nằm tại chỗ với `status` | Không gãy link, hỗ trợ query as-of |

**Giữ nguyên từ v1:** tinh thần Karpathy, raw bất biến, tách evidence khỏi interpretation, provenance, temporal validity, không "newer wins", không xoá lịch sử, domain many-to-many, thư mục tổ chức theo node type, query wiki-first, review trước khi promote.

---

# PHẦN E — LỘ TRÌNH TRIỂN KHAI

**Phase 0 — Scaffold**
- `CLAUDE.md`, các thư mục `02_wiki/`, `03_meta/`, `tools/`
- `03_meta/taxonomy.md`, 8 template, 3 dashboard Dataview
- `.claude/settings.json` deny Edit/Write `01_sources/**`
- `tools/units.py`, `tools/lint.py`
- 4 skill: register, ingest, query, lint

**Phase 1 — Pilot (~10 unit)**, chọn để phủ đủ 5 domain và cặp Basel–VN:

| Nguồn | Unit | Domain kiểm thử |
|---|---|---|
| `src-bcbs-lcr` | LCR20, LCR30, LCR40 | basel, alm |
| `src-tt50-2026-nhnn` | Chương về tỷ lệ thanh khoản | vn-reg (đối chiếu với LCR) |
| `src-bcbs-irrbb-2016` (d368) | 2 section về EVE/NII | basel, alm |
| `src-choudhry-yield-curve` | 1 chapter | product, macro |
| `src-vab-ftp` | 1 phần phương pháp luận | alm (model) |

Tiêu chí kết thúc pilot: trace được claim đến tận raw; bảng Basel vs VN của `lcr` có đủ tham số; lint sạch. Sau đó sửa schema/template (co-evolve) và ghi `decision` vào log.

**Phase 2 — Scale**
- Ingest phần còn lại theo ưu tiên ALM → Basel/VN → product → macro.
- Clippings ingest theo batch (T5).
- Thêm qmd khi index không còn đủ.

---

# PHỤ LỤC — Câu hỏi mở cần chốt trong pilot

1. Nguồn canonical cho sách Bardaeva: 2 file cùng tên, cùng kích thước, khác hash.
2. TT50/2026 thay thế hay sửa đổi văn bản nào trước đó? Cần đọc Điều khoản thi hành để thiết lập `supersedes`.
3. Ngưỡng tách source note theo unit (đang đặt > 20 unit) có hợp lý không với sách 2,6 MB.
4. Có cần thêm tier riêng cho tài liệu nội bộ/tư vấn (như VAB FTP) thay vì xếp vào T4?
