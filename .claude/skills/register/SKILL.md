---
name: register
description: Gọi bằng /register đường-dẫn-file. Đăng ký tài liệu .md mới trong 01_sources/ vào 03_meta/sources.yaml qua tools/registry.py — kiểm tra trùng path/hash, gán tier/domain, lấy ngày ban hành/hiệu lực/bãi bỏ, đánh giá chất lượng convert, tách ingest unit (preset basel/vn/chapter, --add, --chunk, --dir).
---

# /register <path>

Registry là danh mục mọi nguồn: id, đường dẫn, hash, tier, domain, ngày hiệu lực, chất lượng convert và danh sách ingest unit. Các bước sau đều dựa vào nó:
- ingest đọc theo line range của unit;
- lint kiểm tra path;
- query đánh giá độ tin cậy qua tier.

Metadata sai (tier, ngày hiệu lực) sẽ lan sang mọi node cite nguồn này. Vì vậy **không đoán**: chưa xác minh được thì để `null` và ghi vào `notes`.

Không ghi gì vào `01_sources/`. Chỉ ghi registry qua `tools/registry.py add` (script tự validate YAML và chặn id/hash trùng).

## 1. Kiểm tra trùng
```bash
python tools/registry.py check "<path>"
```
- `PATH đã đăng ký` hoặc `HASH trùng`: dừng và báo user nguồn đã có (nêu id). Không tạo entry mới.
- Cùng tên sách hoặc cùng kích thước nhưng **khác hash** (ví dụ 2 bản Bardaeva): đây là hai bản convert khác nhau của cùng một tài liệu. Hỏi user giữ bản nào làm canonical. Không tự xoá hay chọn.
- Chỉ có pdf/docx mà chưa có `.md`: báo cần convert trước (marker/docling).

## 2. Nhận dạng cấu trúc → chọn cách tách unit
Unit tốt có 3–60 unit mỗi nguồn, mỗi unit ≤ ~1.000 dòng, và trùng với ranh giới nội dung (chương, mục, standard). Để nhận dạng:
```bash
grep -cE '^## [A-Z]{3}[0-9]{2}' "<path>"                       # Basel Framework  -> --preset basel
grep -cE '^#{1,4} +\**(Chương|Mục|Phụ lục) ' "<path>"           # văn bản VN       -> --preset vn
grep -iE '^#{1,4} *chapter +[0-9]+' "<path>" | head -40         # sách             -> --preset chapter
head -30 "<path>"                                              # frontmatter docling / comment SOURCE FILE / tiêu đề
```
Xem trước bằng `python tools/units.py "<path>" --preset <p>` rồi đánh giá:
- **Thiếu chương** (ví dụ ra ch1, ch2, ch3, ch6 vì converter biến nhãn "CHAPTER 4" thành ảnh, chỉ còn dòng tiêu đề): đối chiếu với mục lục ở `preamble`, grep tiêu đề chương bị thiếu để lấy số dòng, rồi bổ sung bằng `--add LINE:ID`. Ví dụ: `--preset chapter --add 2173:ch4 --add 2663:ch5 --add 3850:ch9`. Làm vậy thì id giữ thống nhất dạng `ch<n>`, khớp với cách user gọi tên ("chương 4"). Ghi `conversion: partial` kèm issue mô tả.
- Số chương lặp (có hậu tố `-2`), hoặc không có heading chương nào dùng được: `--chunk 400`, kèm issue mô tả.
- **Không sửa tay `lines`, `sha256`, `id` của unit** sau khi ghi entry. Cần khác thì chạy lại tool với tham số khác. Các field `notes`, `conversion`, `domains` thì được sửa tay khi có thông tin mới.
- Một unit quá dài: thử `--level` sâu hơn hoặc `--pattern`.
- Thư mục nhiều file `.md` cùng loại: collection `--dir`, id dạng `col-…`.

## 3. Metadata — đọc gì, ở đâu
| Loại | Lấy từ | Lệnh gợi ý |
|---|---|---|
| Văn bản VN | Dòng `Số:` (số hiệu); `ngày … tháng … năm` (ban hành); điều **Hiệu lực thi hành** / **Điều khoản thi hành** (ngày hiệu lực, các mốc lộ trình, văn bản bị **bãi bỏ**, **sửa đổi, bổ sung**) | `grep -nE "Hiệu lực thi hành\|Điều khoản thi hành"` rồi đọc ~20 dòng; `grep -nE "bãi bỏ\|Sửa đổi, bổ sung một số điều"` |
| Basel Framework | `Version effective as of …`, `generated on …` | `grep -m3 -nE "Version effective\|generated on"` |
| BCBS standalone | Tháng/năm trên bìa; "Standards" (final) hay "Consultative Document" | `head -15` |
| Sách | Frontmatter (`extractor: docling`), heading đầu, tác giả; năm và ISBN ở trang bản quyền (chỉ có năm thì để `published: null` và ghi năm vào `notes`) | `head -30`, `grep -nE "ISBN\|Copyright\|published"` |

Ghi đúng extractor vào `--extractor`: `marker` (có `_meta.json` chứa page_id, dùng để truy ngược trang pdf), `docling` (frontmatter `extractor: docling`, không có số trang), hoặc `custom-pdf` (comment `<!-- SOURCE FILE -->`, có `MODE: OCR` nếu là OCR).

Ghi các mốc quan trọng vào `notes` theo dạng điều khoản. Ví dụ: `"Đ37: hiệu lực 01/10/2026; sửa đổi TT22/2019. Đ13.1: từ 01/10/2028 áp dụng LCR + NSFR."`. Phần `notes` này giúp người ingest sau biết văn bản đứng ở đâu trong timeline.

## 4. Tier, domain, doc_status
Theo `03_meta/taxonomy.md`:

| Tier | Nguồn |
|---|---|
| T1 | Luật, Nghị định, Thông tư |
| T2 | Chuẩn mực final của BCBS |
| T3 | Ấn phẩm hoặc dữ liệu chính thức (IMF, NHTW), báo cáo đã kiểm toán |
| T4 | Sách, học thuật, tài liệu phương pháp/tư vấn |
| T5 | Commentary, clipping, tài liệu không rõ tác giả |

`domains` là list, phần tử đầu là primary: `macro`, `product`, `alm`, `basel`, `vn-reg`.
- Primary là domain mà phần lớn nội dung thuộc về.
- Thêm domain phụ khi có ít nhất một unit đáng kể thuộc domain đó, vì đó là nơi người query sẽ tìm. Ví dụ: sách yield curve có chương về funding curve và FTP thì thêm `alm`; thông tư có phụ lục đo IRRBB theo khung BCBS thì thêm `basel`.
- Ghi lý do chọn domain phụ vào báo cáo để user kiểm tra.

Bẫy đã gặp:
- Tên file giống tên ngân hàng (`Tata_Bank_ALM`) nhưng thực ra là **sách** của tác giả Fidelio Tata, nên T4 chứ không phải T3. Đọc trang đầu để xác minh.
- Không rõ tác giả: T5 kèm note "chưa xác minh nguồn gốc".
- Tài liệu tư vấn cho một ngân hàng: T4, ghi bối cảnh trong `notes`.
- BCBS consultative: `doc_status: consultative`. Phân biệt này quan trọng vì wiki không được trích consultative như final.

## 5. Chất lượng convert
Lấy mẫu 2–3 chỗ (đầu file, một bảng, một đoạn có công thức hoặc tiếng Việt có dấu):
- Ký tự lỗi (ví dụ `Chủa\``), heading bị ngắt dòng, cột bảng lệch, OCR (`MODE: OCR`), thiếu heading chương → `--conversion partial --issue "loc|type|note"`.
- Không thấy lỗi → `ok`.

## 6. Ghi entry
Chạy thử bằng `--dry-run`, rồi chạy thật:
```bash
python tools/registry.py add --id src-tt83-2025-nhnn --path "01_sources/alm/TT83_2025_SBV/TT83_2025_SBV.md" \
  --title "Thông tư 83/2025/TT-NHNN — Hệ thống kiểm soát nội bộ" --tier T1 --domains vn-reg,alm \
  --issuer SBV --number 83/2025/TT-NHNN --published 2025-12-31 --effective 2026-07-01 \
  --original "01_sources/alm/TT83_2025_SBV/TT83_2025_SBV.pdf" --meta "01_sources/alm/TT83_2025_SBV/TT83_2025_SBV_meta.json" \
  --extractor marker --preset vn --notes "Đ74: hiệu lực 01/07/2026; bãi bỏ TT13/2018, TT40/2018."

python tools/registry.py add --id src-choudhry-yield-curve --path "01_sources/…/Choudhry_Analysing_Yield_Curve.md" \
  --title "Analysing and Interpreting the Yield Curve — Moorad Choudhry" --tier T4 --domains product,macro \
  --issuer "Moorad Choudhry" --original "01_sources/…/Choudhry_Analysing_Yield_Curve.pdf" --extractor docling \
  --preset chapter --add 2173:ch4 --add 2663:ch5 --add 3850:ch9 \
  --conversion partial --issue "ch4, ch5, ch9|headings|Nhãn CHAPTER bị convert thành ảnh; bổ sung bằng --add theo mục lục"
```
Đặt `source_id` theo dạng `src-<issuer|tác giả>-<tên ngắn>[-<năm>]`, viết kebab-case, ổn định lâu dài (node sẽ link tới nó).

## 7. Kết thúc
- Append vào `02_wiki/log.md`: `## [YYYY-MM-DD] register | <source_id>` + tier, số unit, conversion, câu hỏi mở.
- `python tools/lint.py` phải ra 0 ERROR.
- Báo cáo cho user:
  - id, tier, domains, ngày ban hành/hiệu lực;
  - số unit, chất lượng convert;
  - **2–3 unit nên ingest trước** (giá trị ALM cao nhất, hoặc đối chiếu được với node hiện có, ví dụ phần LCR của thông tư ↔ [[lcr]]);
  - các điểm cần user quyết định.
