---
name: lint
description: Gọi bằng /lint. Kiểm tra sức khoẻ ALM wiki — tools/lint.py (link, block-ref, trích dẫn khớp raw, frontmatter/enum, hiệu lực, registry) và rà ngữ nghĩa bằng tools/citations.py (node ghi số liệu/phạm vi/tính bắt buộc khác nguồn, câu có số thiếu citation, mâu thuẫn ngầm). Sửa lỗi kỹ thuật ngay, gom sửa nội dung thành batch chờ user duyệt.
---

# /lint

Lint giữ cho wiki đáng tin khi nó lớn dần. Có hai lớp lỗi với hai cách xử lý khác nhau:
- **Lỗi kỹ thuật** (link, block-id, frontmatter, index): sửa ngay. Sửa sai thì cũng dễ hoàn tác và không làm thay đổi tri thức.
- **Lỗi nội dung** (node nói khác nguồn, mâu thuẫn, trạng thái hiệu lực): là thay đổi tri thức, nên đề xuất cho user duyệt theo write policy trong `CLAUDE.md`.

Không ghi gì vào `01_sources/`.

## 1. Lint deterministic
```bash
python tools/lint.py            # text
python tools/lint.py --json     # khi cần xử lý nhiều lỗi
```

| Check | Mức | Cách sửa |
|---|---|---|
| `broken-link` | ERROR | Link bằng alias → đổi sang id (lint gợi ý id). Gõ sai → sửa. Khái niệm chưa có node → tạo stub theo định dạng ở `.claude/skills/ingest/SKILL.md` (mục "Node stub") hoặc bỏ link |
| `broken-block-ref` | ERROR | Tìm block-id đúng trong source note theo nội dung claim (`grep -n "<cụm từ>" 02_wiki/sources/<src>.md`). Claim không có trong source note → **không bịa block-id**: bổ sung claim từ raw (trích nguyên văn, như /ingest) hoặc thay bằng `[cần nguồn]` |
| `quote-not-found` | ERROR | Trích dẫn đã bị sửa chữ. Grep một cụm 5–8 từ trong raw rồi copy lại đúng. Không được "sửa" bằng cách viết lại đoạn trích |
| `required-field`, `enum-*`, `frontmatter`, `relation` | ERROR | Sửa theo `03_meta/taxonomy.md` (ví dụ `maturity` chỉ có `draft/reviewed/canonical`; relation cũ `affects` → `drives`, `required-by` → `governs` khai ở node regulation) |
| `folder` | ERROR | Chuyển file sang thư mục đúng với type; giữ nguyên nội dung và tên file |
| `temporal` (`valid_to` đã qua mà còn `active`) | ERROR | **Không tự đổi status.** Đề xuất `superseded`/`retired` (cần user duyệt); kiểm tra xem `valid_to` có nhập nhầm không |
| `registry-*`, `raw-path` | ERROR | Sửa path hoặc id trong frontmatter cho khớp `03_meta/sources.yaml`; unit đã ingest thì `python tools/registry.py mark …` |
| `orphan`, `index` | WARN | Thêm dòng vào `index.md`; thêm link từ node liên quan (thường là node cha qua `part-of`) |
| `alias-collision` | WARN | Bỏ alias khỏi node kém đặc thù hơn (source note không cần alias) |
| `supersession`, `macro-stale` | WARN | Đề xuất cho user |
| `stub-plan` | WARN | Bổ sung callout stub đủ 3 dòng theo định dạng ở ingest SKILL; dòng "Hoàn thiện bằng" ghi `/ingest --node <id>` (đã có claim) hoặc `/ingest <src> <unit>` |
| `stub-index` | WARN | Sửa dòng index: stub thì ghi `*stub*`, node đã đầy đủ thì bỏ `*stub*` |
| `stub-stale` | INFO | Đề xuất user: `/ingest --node <id>` nếu đã có claim, hoặc giữ stub chờ ingest unit |
| `stub-count` | INFO | Không sửa; đưa vào báo cáo cuối |

Chạy lại lint sau khi sửa, đến khi hết ERROR kỹ thuật.

## 2. Rà ngữ nghĩa
Lint deterministic chỉ biết citation **tồn tại**, không biết node có nói **đúng** điều nguồn nói không. Đây là phần giá trị nhất của lint.
```bash
python tools/citations.py --numbers        # câu có số/% trong node  ↔  claim + trích dẫn được cite
python tools/citations.py --node <id>      # rà kỹ một node
python tools/citations.py --uncited        # câu / dòng bảng có số nhưng không có citation, không gắn nhãn Diễn giải
```
`--numbers` chỉ thấy được những câu **có** citation. Dòng bảng tham số không có citation riêng thì sẽ lọt. Vì vậy chạy thêm `--uncited` và đọc tay những dòng nó liệt kê: đó vừa là chỗ dễ sai số, vừa là chỗ thiếu provenance. Kết quả của `--uncited` là gợi ý, không phải lỗi chắc chắn (ví dụ list con nằm dưới một câu đã cite). Hãy đánh giá từng dòng.
Với mỗi cặp NODE ↔ SRC, kiểm tra:
- **Số và ngưỡng**: %, số ngày, số tiền, ngày hiệu lực có khớp không; "tối thiểu" hay "tối đa"; "≥" hay "=".
- **Phạm vi**: node có mở rộng claim ra ngoài phạm vi nguồn không (ví dụ áp tham số của nhóm này cho nhóm khác, bỏ điều kiện "nếu…").
- **Tính bắt buộc**: nguồn nói "may" (tuỳ chọn) mà node viết như "must" (bắt buộc), hoặc ngược lại.

Ngoài ra rà thêm:
- Mâu thuẫn ngầm giữa các node (cùng tham số, khác giá trị, chưa có callout).
- Basel `doc_status: consultative` bị trích như final.
- Thuật ngữ xuất hiện ở ≥ 3 node nhưng chưa có node riêng → áp tiêu chí đầu vào (`.claude/skills/research/SKILL.md`, bước 3, "Khái niệm cần node riêng"); đạt thì đề xuất stub trong bảng batch, không tự tạo.
- Synthesis cũ có nguồn mới liên quan; dòng đánh dấu của ingest chưa rà (`grep -n '\] ingest .*cần rà lại' 02_wiki/syntheses/*.md | grep -v 'đã rà'`).
- Relation có synthesis làm chủ thể hoặc đích (taxonomy, mục "Relation"): `grep -c '{type:' 02_wiki/syntheses/*.md | grep -v ':0$'` và `grep -rn 'to: "\[\[<synthesis-id>\]\]"' 02_wiki`.
- Callout `[!conflict]` vẫn `open`.
- Câu factual không có citation và không gắn nhãn `*Diễn giải:*`.
- Văn phong theo `.claude/skills/alm-writing-style/SKILL.md`, ưu tiên R1 (mức bắt buộc lệch nguồn), C2 (quy kết mơ hồ), T3 (tính từ không kèm số) trong câu claim và đoạn `*Diễn giải:*`. Ghi rule ID vào cột "Vấn đề" của bảng batch. Không tự sửa node `reviewed`/`canonical`.
- Lỗ hổng tri thức: đề xuất unit `pending` nên ingest (`python tools/registry.py show <src>`).

## 2b. Kiểm tra bổ sung (script phụ, chỉ đọc)
```bash
python tools/audit_vault.py         # thống kê type/maturity, note ngắn (<30 dòng), relation thiếu cite
python tools/check_math.py --info   # gợi ý văn phong công thức (INFO: từ chưa bọc \text{}); ERROR/WARN đã có trong lint.py
```
Lỗi công thức (`math-*`) đã nằm trong `lint.py`: ERROR chặn lint như mọi ERROR khác. Các script ở đây không chặn kết quả lint. Xử lý phát hiện như sau:
- Relation thiếu `cite`: nguồn có nói quan hệ đó thì thêm `cite` trỏ block-id có thật; là suy luận thì giữ không `cite` và đảm bảo thân bài có `*Diễn giải:*`. Node `reviewed`/`canonical`: chỉ đề xuất.
- Note ngắn: liệt kê vào lỗ hổng tri thức, không tự viết thêm nếu chưa có nguồn.
- Lỗi công thức (`math-*` trong lint): sửa cú pháp là lỗi kỹ thuật, sửa ngay ở node `draft`; không đổi nội dung công thức. `math-display-not-own-line`: chuyển citation xuống dòng dưới `$$`, giữ thụt lề. Node `reviewed`/`canonical`: đề xuất.

## 3. Báo cáo, sửa, ghi log
1. Áp dụng các sửa kỹ thuật ở mục 1.
2. Trình bày lỗi nội dung thành bảng batch, chờ user duyệt:

   | Node:dòng | Vấn đề | Bằng chứng (source note / raw) | Đề xuất sửa |
   |---|---|---|---|

   User đã nói "sửa luôn" thì chỉ áp những sửa mà bằng chứng rõ ràng, tức đưa node về đúng claim được cite. Những gì cần phán đoán (đổi status, diễn giải quy định) vẫn để đề xuất.
3. Append vào `02_wiki/log.md`:
   ```
   ## [YYYY-MM-DD] lint | <tóm tắt>
   - trước: X error / Y warning · sau: X' / Y'
   - script phụ: audit_vault (relation thiếu cite: N, note ngắn: N) · công thức (math-*): N lỗi
   - stub: N (M sẵn sàng --node, K quá hạn)
   - đã sửa: …
   - đề xuất chờ duyệt: …
   ```
4. Chạy lại `python tools/lint.py` và báo kết quả cuối.
