---
name: query
description: Trả lời câu hỏi dựa trên wiki ALM (wiki first, raw để verify), có citation, ghi rõ maturity và as_of, xử lý câu hỏi as-of lịch sử; đề xuất lưu câu trả lời giá trị thành synthesis node. Dùng khi user gọi /query hoặc hỏi về khái niệm, quy định, số liệu trong 5 domain.
---

# /query <câu hỏi> [as-of YYYY-MM-DD]

## Các bước

1. **Phân loại câu hỏi**: định nghĩa · cơ chế · so sánh Basel–VN · tham số/ngưỡng quy định · số liệu · as-of lịch sử · tổng hợp nhiều nguồn.
2. **Xác định thời điểm**: mặc định là hôm nay. Nếu user hỏi "tại thời điểm X", chỉ dùng node và claim có `valid_from ≤ X` và (`valid_to` trống hoặc `≥ X`), kể cả node `superseded`.
3. **Tìm node**:
   - Đọc `02_wiki/index.md`, chọn node liên quan.
   - Đọc các node đó, rồi đi theo `relations` và link một bước. Relation chỉ khai một chiều (A → B tại node A); chiều ngược tìm bằng `grep -rn 'to: "\[\[<id>\]\]"' 02_wiki`.
   - Index không đủ: `grep -ril "<từ khoá>" 02_wiki/`.
4. **Verify** khi câu trả lời có số liệu, ngưỡng hay nghĩa vụ quy định: đi theo citation về source note, đọc trích nguyên văn. Nghi ngờ thì grep locator trong raw.
5. **Trả lời** (đọc `.claude/skills/alm-writing-style/SKILL.md` trước, áp profile V3; synthesis lưu ở bước 6 cũng theo V3):
   - Có citation `[[node]]` / `[[src-…#^id]]` cho từng ý chính.
   - Ghi rõ maturity của node dùng. Có node `draft` thì thêm câu: *"dựa trên node draft, chưa review"*.
   - Ghi `as_of` với số liệu macro hoặc thị trường.
   - Câu hỏi nghĩa vụ tại VN: quy định NHNN có hiệu lực là căn cứ, Basel chỉ là tham chiếu.
   - Wiki không có thông tin: nói rõ là không có, đề xuất unit hoặc nguồn cần ingest. Kiến thức nền của LLM phải đánh dấu "(ngoài wiki, chưa có nguồn)".
6. **Đề xuất lưu**: câu trả lời tổng hợp có giá trị thì hỏi user có lưu không. Nếu có:
   - tạo `02_wiki/syntheses/<id>.md` từ template, `origin: query`, `question`, `as_of`, `maturity: draft`;
   - cập nhật `index.md`;
   - append `## [YYYY-MM-DD] query | <id>` vào `log.md`;
   - chạy `python tools/lint.py`.
7. Câu hỏi làm lộ ra lỗ hổng hoặc mâu thuẫn: ghi gợi ý vào log để `/lint` hoặc `/ingest` xử lý sau.
