---
name: alm-writing-style
description: Quy chuẩn văn phong tiếng Việt của ALM wiki (source note, node, Diễn giải, synthesis, câu trả lời query). Không tự kích hoạt; được ingest/query/lint đọc trước khi viết, hoặc user gọi /alm-writing-style <node-id> để rà một node.
disable-model-invocation: true
---

# Quy chuẩn văn phong ALM wiki

Skill thụ động. `/ingest`, `/query`, `/lint` và mọi lần tạo node hay synthesis đều đọc file này **trước khi viết**, rồi viết đúng rule ngay từ đầu. Không có lượt "viết lại cho hay" sau khi xong: mỗi lần viết lại câu đã cite là thêm một cơ hội làm lệch số, phạm vi hoặc tính bắt buộc.

Rule có ID ổn định theo nhóm (R1, C2, T3…). Skill khác và báo cáo lint trích rule qua ID. Rule bị bỏ để trống số, không đánh lại.

Thứ tự ưu tiên khi hai rule kéo về hai hướng: **P > R > C > N > S/T > F**. Đúng nguồn quan trọng hơn câu văn đẹp.

## P — Phạm vi và vùng cấm sửa

**P1. Chỉ áp cho văn do LLM viết:**
- câu diễn đạt claim trong source note;
- thân node;
- đoạn `*Diễn giải:*`;
- synthesis;
- câu trả lời `/query`;
- mục `## Đề xuất cập nhật`.

**P2. Không rule nào được chạm vào:**
- dòng trích nguyên văn `> "…"`, kể cả khi nguồn dùng ẩn dụ, câu dài hay từ cực đoan;
- dòng locator `> — LCR40.1 ^lcr40-1` và mọi block-id;
- citation `[[…]]` và `[[…#^…]]`;
- frontmatter;
- heading do template quy định;
- giá trị, đơn vị và điều khoản trong bảng tham số;
- callout `> [!conflict]` (chỉ được thêm, không sửa claim bên trong).

## R — Quy phạm và provenance

**R1. Giữ đúng mức bắt buộc của nguồn.** must / shall / is required → "phải"; should → "nên"; may / can → "có thể"; should ideally → "lý tưởng nên". Không làm nhẹ "must" thành "nên", không làm mạnh "should" thành "phải". Tiếng Việt trong văn bản NHNN giữ đúng chữ "phải", "được", "không được" của văn bản.

**R2. Tách fact và diễn giải.** Câu factual có citation. Suy luận, hàm ý cho ALM, so sánh giữa nguồn hay nhận định đặt sau nhãn `*Diễn giải:*`. Câu không có citation mà cũng không có nhãn là lỗi.

**R3. Sửa câu chữ không được đổi nội dung đã cite**, gồm:
- số, đơn vị và dấu so sánh (≥, ≤, =);
- "tối thiểu" hay "tối đa";
- phạm vi đối tượng;
- điều kiện "nếu…" và ngoại lệ "trừ…".

Khi sửa một câu đã cite, đọc lại claim gốc trong source note trước.

**R4. Gắn thời điểm cho fact phụ thuộc thời gian.** Tham số quy định đi kèm văn bản và hiệu lực ("theo TT50/2026, hiệu lực từ …"), hoặc đã có `valid_from` trong frontmatter của node. Số liệu thị trường hay macro phải ghi `as_of`. Không viết "hiện nay", "gần đây", "mới nhất" khi không kèm mốc ngày.

**R5. Nguồn không nói thì không viết.** Ghi `[cần nguồn]` thay vì lấp bằng kiến thức chung. Kiến thức nền trong câu trả lời `/query` phải đánh dấu "(ngoài wiki, chưa có nguồn)".

## C — Chủ thể và quy kết

**C1. Câu nhân-quả hoặc câu quy phạm phải có chủ thể cụ thể.** Chủ thể hợp lệ gồm:
- tổ chức: NHNN, BCBS, supervisor, ngân hàng, ALCO;
- văn bản quy phạm, khi đi với động từ quy phạm: "LCR40 quy định…", "TT50/2026 yêu cầu…";
- biến số hoặc tham số: lãi suất, run-off rate, haircut, LCR;
- nhóm xác định: người gửi tiền bán lẻ, đối tác wholesale phi tài chính.

Không dùng "cơ chế", "rủi ro", "xu hướng", "hệ thống", "thị trường" (chung chung) hay "người ta" làm chủ ngữ của động từ hành động. Câu định nghĩa dạng "X là Y" không cần chủ thể hành động. Ví dụ sai → đúng: `references/subject-examples.md`.

**C2. Cấm quy kết mơ hồ.** Các cụm như "giới phân tích cho rằng", "nhiều chuyên gia nhận định", "thị trường tin rằng", "thông lệ quốc tế là" phải được thay bằng nguồn định danh kèm citation. Không có nguồn thì xoá câu hoặc ghi `[cần nguồn]`.

**C3. Cấm thổi phồng tầm quan trọng.** Không viết "bước ngoặt", "thay đổi căn bản", "then chốt", "vô cùng quan trọng" khi không có số liệu hoặc sự kiện chứng minh. Muốn nói một tham số quan trọng thì nêu tác động bằng số ("chiếm X% tổng dòng ra").

## N — Thuật ngữ

**N1. Một khái niệm, một thuật ngữ.** Trong toàn node, gọi khái niệm bằng `title` của node đích. Không đổi qua lại giữa "run-off rate", "tỷ lệ rút vốn", "hệ số dòng ra" trong cùng một node. Biến thể đặt trong `aliases`.

**N2. Giữ thuật ngữ tiếng Anh chuyên ngành** (duration, EVE, NII, run-off rate, HQLA, haircut, operational deposits). Tên tiếng Việt nằm trong `aliases`, có thể chú một lần trong ngoặc ở lần xuất hiện đầu. Không tự dịch thuật ngữ mới gặp. Tra `references/term-glossary.md` trước; chưa có thì giữ tiếng Anh và bổ sung vào bảng.

**N3. Nội dung VN Regulator dùng đúng chữ của văn bản NHNN.** Ví dụ, chỉ tiêu nào văn bản gọi tên tiếng Việt thì node dùng đúng tên đó. Không dịch ngược từ tên Basel. Basel và NHNN gọi khác nhau thì ghi cả hai trong bảng `## Basel vs VN` và trong `term-glossary.md`.

**N4. Viết tắt giải nghĩa ở lần đầu trong node**, trừ khi viết tắt đó chính là `title` của node được link. Thuật ngữ thông dụng không viết hoa ("lãi suất", "tiền gửi").

## S — Câu

**S1. Một câu một luận điểm, tối đa khoảng 60 từ.** Câu dài thì tách tại mệnh đề phụ đứng độc lập được.

**S2. Cấm câu nhồi.** Ví dụ mẫu sai: "Cơ chế X vận hành thông qua Y, bộc lộ trong điều kiện Z [số liệu], dẫn đến hệ quả là W". Câu kiểu này mở bằng danh ngữ trừu tượng và nhồi luận điểm, điều kiện, số liệu, kết luận vào một chỗ. Viết lại theo một trong hai cách:
- đưa số liệu thành câu riêng trước, rồi nêu hệ quả ở câu sau bằng "vì vậy" hoặc "do đó";
- nêu kết luận trước, giải thích sau.

**S3. Tối đa ba mệnh đề nối bằng dấu phẩy trong một câu.** Nhiều hơn thì tách câu hoặc chuyển thành bullet.

**S4. Cấm "không chỉ… mà còn…"** và cấm ép ý thành nhóm ba khi số lượng thực tế khác ba.

**S5. Bị động chỉ dùng khi chủ thể không xác định hoặc không cần.** "Được giả định", "được coi là" là cách diễn đạt chuẩn của văn bản Basel nên hợp lệ. Còn lại nêu đích danh chủ thể (C1).

## T — Từ vựng

**T1. Từ sáo tối đa 3 lần mỗi node** (đếm riêng từng node, không cộng dồn trong một lượt ingest). Danh sách từ và từ thay thế: `references/hollow-words.md`.

**T2. Cấm từ cực đoan và ẩn dụ bạo lực, thảm hoạ** ("tàn phá", "khốc liệt", "nghiền nát", "chết người", "bom nổ chậm"). Biến động mạnh thì mô tả bằng số hoặc động từ tài chính chuẩn ("giảm X% trong Y ngày", "rút ròng"). Nếu nguồn dùng những từ này thì chúng chỉ được nằm trong trích nguyên văn.

**T3. Tính từ định tính phải kèm số hoặc bị xoá.** Áp cho các từ như "lớn", "đáng kể", "nghiêm trọng", "khổng lồ", "cực kỳ", "rất thấp". Ngoại lệ là cụm định danh của nguồn: "significant stress" → "stress đáng kể" là tên kịch bản LCR nên giữ nguyên.

**T4. Dùng từ thường thay từ hoa mỹ.** "Đóng vai trò là" → "là"; "nhằm mục đích" → "để"; "tiến hành thực hiện" → "làm" hoặc bỏ; "cần lưu ý rằng" → xoá. Xem thêm `references/hollow-words.md`.

**T5. Cấm cụm marketing thay thuật ngữ** ("dòng tiền thông minh", "lá chắn thanh khoản", "tấm đệm an toàn vững chắc"). Dùng tên thuật ngữ hoặc mô tả hành vi cụ thể.

## F — Hình thức

**F1. Theo template `03_meta/templates/<type>.md`.** Giữ đúng các heading của template, không thêm heading ngoài template khi chưa cần. Bullet và bảng là hình thức chính. Đoạn văn xuôi mỗi đoạn một luận điểm. Mục rỗng thì để trống hoặc ghi `[cần nguồn]`, không viết câu độn.

**F2. Bullet có nhãn `- **nhãn**: …` chỉ dùng khi mỗi dòng mang nội dung riêng**, ví dụ các driver của run-off. In đậm chỉ dùng cho nhãn đó hoặc một ngưỡng then chốt trong câu, không in đậm tràn lan thuật ngữ.

**F3. Dấu câu.** Hạn chế gạch ngang làm liên từ trong câu văn; dùng dấu chấm hoặc dấu phẩy. Dấu hai chấm chỉ đứng trước danh sách hoặc ví dụ. Không emoji. Dòng locator và bảng được miễn theo P2.

**F4. Cấm cụm hội thoại và tự đánh giá:**
- cụm chatbot: "Hy vọng điều này hữu ích", "Câu hỏi hay!";
- filler mở câu: "Nhìn chung", "Đáng chú ý là", "Cần nhấn mạnh rằng", "Không thể phủ nhận";
- tự đánh giá tiến độ: "đã đầy đủ", "hoàn chỉnh", "chỉn chu".

Muốn nói phần nào còn thiếu thì nêu đúng phần đó ("cột VN chờ ingest TT50/2026 PL1").

## V — Profile theo loại văn bản

**V1. Source note: claim một dòng, trung lập.** Chỉ nói điều đoạn trích nói: tham số, điều kiện, phạm vi, mức bắt buộc (R1). Không diễn giải, không so sánh với nguồn khác, không hàm ý ALM. Nếu claim dài hơn đoạn trích thì claim đang chứa diễn giải.

**V2. Node: giọng phân tích kỹ thuật, người đọc là chủ wiki.**
- Mục đầu (`Ý chính` / `Định nghĩa`) mở bằng định nghĩa, không mở bằng bối cảnh hay lịch sử.
- Mỗi dòng bảng tham số có citation riêng.
- Góc nhìn domain nêu khác biệt cụ thể, không nêu khẩu hiệu.
- Không khuyến nghị hành động cho ngân hàng, trừ phần `*Diễn giải:*` khi nêu hàm ý ALM.

**V3. Synthesis và câu trả lời `/query`: mở bằng kết luận, sau đó dẫn chứng có citation.**
- Ghi maturity của node dùng và `as_of` hoặc hiệu lực (R4).
- Với câu hỏi nghĩa vụ tại VN, nêu quy định NHNN trước, Basel sau, và ghi rõ Basel chỉ là tham chiếu.
- Không kết bằng tóm tắt lặp lại ý đã nói.

**V4. log, index, overview: một dòng một sự kiện.** Dùng động từ và đối tượng cụ thể ("created", "updated", số claim, số trích dẫn). Không dùng tính từ đánh giá.

## Quy trình

**Khi được skill khác gọi** (ingest, query, lint): đọc file này trước khi soạn. Viết theo profile V tương ứng. Trước khi chốt, tự rà phần LLM viết theo thứ tự R → C → N → S/T → F. Chỉ mở `references/` khi gặp trường hợp nghi ngờ cụ thể.

**Khi user gọi `/alm-writing-style <node-id>`:**
1. Đọc node và các claim được cite trong source note.
2. Lập bảng `dòng | rule | câu hiện tại | đề xuất | ảnh hưởng nội dung? (có/không)`. Đề xuất nào có "có" thì phải kèm claim gốc làm bằng chứng.
3. Áp sửa:
   - node `draft`: áp sửa khi user đồng ý;
   - node `reviewed` hoặc `canonical`: chỉ ghi vào `## Đề xuất cập nhật`.
4. Chạy `python tools/lint.py` (0 ERROR) và append `02_wiki/log.md`: `## [YYYY-MM-DD] style | <node-id>`.

## Phụ lục — ví dụ sai → đúng

**Claim trong source note (R1, V1).** Đoạn trích là "Supervisors should allow for differentiated responses to a reported LCR below 100%."
- Sai: "Supervisor phải phản ứng có phân biệt và tương xứng khi LCR < 100%." Câu này đổi "should" thành "phải", và thêm "tương xứng" vốn không có trong đoạn trích.
- Đúng: "Supervisor nên cho phép phản ứng có phân biệt khi LCR báo cáo dưới 100%."

**Dòng bảng tham số (T3, R2).**
- Sai: `| Stable retail | rất thấp, khoảng 5% | |`. Dòng này dùng tính từ không cần thiết và không có citation riêng.
- Đúng: `| Stable retail / SME | 5% (jurisdiction có thể 3%) | [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-11]] |`

**Đoạn diễn giải (F4, C1, T1, T3, R2).**
- Sai: "Nhìn chung, cơ chế run-off rate đóng vai trò then chốt, kích hoạt áp lực thanh khoản khổng lồ lên ngân hàng."
- Đúng: "*Diễn giải:* run-off rate theo LCR là giả định giám sát. Mô hình NMD nội bộ dùng giả định hành vi. Hai bộ giả định phục vụ hai mục đích khác nhau và không thay thế nhau."
