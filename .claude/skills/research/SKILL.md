---
name: research
description: Gọi bằng /research <chủ đề> [bộ câu hỏi]. Nghiên cứu một vấn đề ALM phức tạp hoặc một bộ nhiều câu hỏi (vd 20 câu về IRRBB, 7 câu về FTP) dựa trên wiki — lập bản đồ phủ câu hỏi ↔ node, chỉ ra lỗ hổng nguồn và unit cần ingest, rồi viết synthesis origin research theo cụm câu hỏi, có citation. Câu hỏi đơn lẻ dùng /query. Chỉ chạy khi user gọi.
disable-model-invocation: true
---

# /research <chủ đề> [bộ câu hỏi]

`/query` trả lời một câu. `/research` xử lý cả một vấn đề: nhiều câu hỏi liên quan nhau, cần đi qua nhiều node, nhiều nguồn, và thường lộ ra chỗ wiki chưa có nguồn. Giá trị chính của skill không phải là văn bản dài, mà là **bản đồ phủ**: câu nào wiki trả lời được bằng citation, câu nào chỉ trả lời được một phần, câu nào phải ingest thêm. Synthesis viết ra chỉ đáng tin bằng các citation bên dưới nó.

Không ghi gì vào `01_sources/`. Số liệu, ngưỡng, tham số và nghĩa vụ quy định chỉ lấy từ nguồn đã ingest; thiếu nguồn thì ghi `[cần nguồn]` hoặc đề xuất unit để `/ingest`. Kiến thức nền của LLM chỉ được dùng để nối mạch giữa các ý có nguồn (xem bước 4).

Một bộ 20 câu chạm tới hàng chục node dài 200–350 dòng; đọc hết ngay từ đầu sẽ đầy context trước khi viết được chữ nào. Vì vậy skill tách hai pha: bước 1–2 chỉ đọc lướt (index, frontmatter, heading) để lập bản đồ; bước 3–4 mới đọc kỹ, và chỉ cho **một cụm** mỗi lượt.

## 0. Chuẩn bị
- Đọc `.claude/skills/alm-writing-style/SKILL.md` (profile V3 cho synthesis). Trong vault này chỉ dùng skill văn phong đó.
- Chuẩn hoá bộ câu hỏi: đánh số Q1…Qn, giữ nguyên chữ của user. User chỉ đưa chủ đề thì đề xuất 5–10 câu hỏi khung (bản chất → cơ chế → đo lường → quy định Basel/VN → quản trị), chờ user chỉnh rồi mới làm tiếp.
- Xác định thời điểm (mặc định hôm nay; "as-of X" thì lọc theo `valid_from`/`valid_to` như `/query`) và jurisdiction. Câu hỏi nghĩa vụ tại VN: quy định NHNN là căn cứ, Basel chỉ là tham chiếu.
- Tìm trong `02_wiki/log.md` dòng `research | <chủ đề>` cũ. Có bản đồ phủ trước đó thì dùng làm điểm xuất phát và chỉ ra câu nào đã đổi mức phủ (thường sau khi ingest thêm unit).

## 1. Bản đồ phủ (coverage map)
Với từng câu hỏi, tìm trong wiki, **chỉ đọc lướt**, không đọc thân bài node và không đọc raw:
- `02_wiki/index.md` (dòng tóm tắt từng node) → node liên quan → `relations` trong frontmatter; chiều ngược dùng `grep -rn 'to: "\[\[<id>\]\]"' 02_wiki`.
- Heading và frontmatter: `grep -n '^question\|^maturity\|^## \|^### ' <file>`. Đủ để biết node có mục trả lời câu hỏi không.
- **Synthesis đã có** trong `02_wiki/syntheses/`: so `question` và heading. Synthesis trả lời đúng câu đó thì dùng lại, không viết trùng.
- Nguồn VN: kiểm tra có node regulation NHNN cho chủ đề không (`grep -l 'jurisdiction: VN' 02_wiki/regulations/*`). Không có thì ghi rõ trong cột "Thiếu gì".
- Unit chưa ingest có thể chứa câu trả lời: `python tools/registry.py show <src>` (xem unit `pending` và heading).

- **Provenance của node/synthesis ứng viên.** Heading và số citation không cho biết câu có số liệu nào đang thiếu nguồn; vì vậy mức phủ đọc lướt dễ lệch giữa các lần chạy. Chạy một lần cho toàn vault (dưới 1 giây) và chỉ đếm theo file ứng viên, không đưa toàn bộ output vào context (hơn 1.500 dòng):
  ```bash
  python tools/citations.py --uncited > scratch/uncited.txt
  grep -c '<id>.md' scratch/uncited.txt          # cho từng file ứng viên
  grep '<id>.md' scratch/uncited.txt | head -8   # xem mẫu khi số dòng đáng kể
  ```
  Output là gợi ý, không phải lỗi chắc chắn: dòng nối tiếp của bullet đã cite, sơ đồ ASCII, nhãn in đậm, câu mô tả lỗ hổng thường bị báo nhầm. Chỉ tính những dòng mang tham số, ngưỡng, số liệu thật.

Mức phủ ở bước này là ước lượng; bước 3 xác nhận lại khi đọc kỹ. Câu trả lời dựa vào node có tham số/số liệu thật thiếu citation thì tối đa là **một phần**, và ghi node đó vào nhóm "Lỗi wiki phát hiện được" ở bước 6.

Trình bày bảng rồi **dừng chờ user**:

| Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis trả lời | Nguồn cite chính | Thiếu gì · unit nên ingest |
|---|---|---|---|---|---|

Mức phủ: **đủ** (mọi ý chính có citation) · **một phần** (khung có, thiếu tham số/VN/ví dụ) · **thiếu** (wiki không có nguồn). Thêm một dòng tổng: số câu đủ / một phần / thiếu, và danh sách unit đề xuất ingest xếp theo số câu hỏi mà unit đó gỡ được.

## 2. Chốt phạm vi với user
Đưa 2–3 phương án (dùng AskUserQuestion nếu có):
- **Ingest trước**: chạy `/ingest` các unit gỡ được nhiều câu "thiếu", rồi quay lại research. Chọn khi câu "thiếu" chiếm phần lớn.
- **Viết theo cụm, đánh dấu chỗ thiếu**: viết synthesis cho các câu đủ/một phần; câu thiếu ghi `[cần nguồn]` + unit đề xuất.
- **Chỉ lưu bản đồ phủ**: không viết synthesis, chỉ ghi log.

Phương án nào cũng append **nguyên bảng phủ** vào `02_wiki/log.md` (mẫu ở bước 5) ngay khi user chốt. Research thường kéo qua nhiều session (ingest xen giữa); bảng trong log là thứ duy nhất lần chạy sau đọc lại được. Đây là điểm ngắt hợp lý để đề xuất user `/compact` trước khi viết.

Gom câu hỏi thành **cụm**, mỗi cụm một synthesis. Lý do: một synthesis cho 20 câu sẽ dài, khó review và khó cite lại; một synthesis cho mỗi câu thì vụn và trùng nền. Cụm tự nhiên thường theo các phần trong bộ câu hỏi của user (vd IRRBB: bản chất & cấu phần · repricing balance sheet · dòng tiền & thời điểm tái định giá · interest rate curves · đo lường NII/EVE · quản trị). Mục tiêu khoảng ≤ 300 dòng mỗi synthesis.

Cụm đã có synthesis:
- Synthesis `draft`: cập nhật trực tiếp, bổ sung câu hỏi vào `question` và mục `## Câu hỏi`. File cũ không theo heading template thì **giữ nguyên cấu trúc**, chỉ thêm mục mới; tái cấu trúc cả file dễ làm lệch câu đã cite (R3 trong `alm-writing-style`).
- Synthesis `reviewed`/`canonical`: không sửa thân bài, ghi vào `## Đề xuất cập nhật`, hoặc tạo synthesis mới bổ sung và link qua lại.

## 3. Verify trước khi viết
Giờ mới đọc kỹ các node và synthesis của **cụm đang viết**. Cập nhật lại mức phủ nếu đọc xong thấy khác ước lượng ở bước 1.

Với mọi số liệu, ngưỡng, tham số, nghĩa vụ quy định sẽ dùng: đi theo citation về source note, đọc trích nguyên văn. Nghi ngờ thì grep locator trong raw (`python tools/registry.py read <src> <unit> --from N --to M`). Không đọc nguyên file nguồn lớn.

Đọc raw có thể lộ ra đoạn liên quan mà source note chưa có claim (unit đã `done` nhưng ingest bỏ sót). **Không tự thêm claim vào source note**, kể cả note `draft` và kể cả khi trích dẫn sẽ khớp raw: thêm claim là việc của `/ingest`, nơi user duyệt phạm vi từng unit; làm ngầm trong research sẽ đẩy mức phủ lên bằng bằng chứng chưa ai duyệt. Ghi đoạn đó (locator, dòng raw, câu hỏi nó gỡ) vào `## Bất định` của synthesis và vào gợi ý cuối (bước 6); với source note `reviewed`/`canonical` có thể thêm vào `## Đề xuất cập nhật` của note đó.

Ghi nhận ngay khi gặp: hai nguồn cùng phạm vi nói khác nhau (→ callout `> [!conflict]`, giữ cả hai), Basel `consultative` (không trích như final), khác biệt Basel vs VN (không phải conflict, ghi rõ jurisdiction).

## 4. Viết synthesis
Tạo `02_wiki/syntheses/<id>.md` từ `03_meta/templates/synthesis.md`. ID kebab-case tiếng Anh theo nội dung cụm (vd `irrbb-repricing-cash-flows-and-buckets`), không chứa "research" hay số câu hỏi.

Frontmatter: `origin: research`, `maturity: draft`, `question` = các câu của cụm (nối bằng " · ", giữ chữ của user, đặt trong ngoặc kép YAML; ngoặc kép bên trong đổi sang ngoặc đơn), `as_of`, `sources` = các source note thực sự được cite, `domains`, `aliases` có tên tiếng Việt và tiếng Anh nhưng không trùng alias node khác (lint báo `alias-collision`). `relations` thường để trống; quan hệ thuộc về node khái niệm.

Thân bài giữ heading của template, cụ thể hoá cho bộ câu hỏi:
- `## Câu hỏi`: danh sách Qk của cụm, đúng số thứ tự trong bộ gốc.
- `## Kết luận`: mỗi Qk 2–4 câu trả lời thẳng, có citation. Đây là phần người đọc dùng nhiều nhất.
- `## Cơ chế`: mỗi Qk một mục `### Qk — <ý chính>`, giải thích cơ chế, công thức, bảng; **mỗi câu factual và mỗi dòng bảng tham số có citation riêng** `[[src-…#^id]]`. Link node bằng `[[id]]` để người đọc đi sâu, không chép lại nguyên node.
- `## Bằng chứng ủng hộ` · `## Bằng chứng trái chiều`: nguồn nào nói gì, chỗ nào các nguồn lệch nhau hoặc chỉ một nguồn T4 đứng sau.
- `## Phụ thuộc regime`: kết luận đổi thế nào theo môi trường lãi suất, loại ngân hàng, jurisdiction.
- `## Hàm ý ALM / quy định`: hàm ý cho ALCO/Treasury, phân biệt rõ nghĩa vụ NHNN và tham chiếu Basel. Wiki chưa có quy định NHNN cho chủ đề thì nói thẳng "chưa có nguồn NHNN trong wiki", để người đọc không hiểu nhầm chuẩn Basel là nghĩa vụ tại VN. Nhận định của LLM đặt sau `*Diễn giải:*`.
- `## Bất định`: câu/ý còn `[cần nguồn]`, unit đề xuất ingest, giả định chưa kiểm.

Heading template là cố định (P2), nhưng không phải câu hỏi nào cũng có nội dung cho mọi mục: câu "xây dựng như thế nào" thường không có bằng chứng trái chiều hay phụ thuộc regime. Khi đó ghi một dòng "Không ghi nhận trong nguồn đã ingest." thay vì viết câu độn.

Không viết fact mà nguồn đã ingest không nói. Kiến thức nền chỉ dùng để nối mạch giữa các ý có nguồn, đặt sau `*Diễn giải:*` kèm "(ngoài wiki, chưa có nguồn)", và không bao giờ mang số liệu, ngưỡng hay nghĩa vụ quy định.

## 5. Sổ sách và kiểm tra
- `02_wiki/index.md`: thêm/sửa dòng synthesis `[[id]] — tóm tắt · domains · draft`.
- Node khái niệm liên quan (draft): thêm link tới synthesis ở mục liên kết nếu giúp điều hướng.
- `02_wiki/log.md` (append):
  ```
  ## [YYYY-MM-DD] research | <chủ đề>
  - bộ câu hỏi: n câu · phủ: x đủ / y một phần / z thiếu · phương án: <ingest trước | viết theo cụm | chỉ bản đồ>
  - bản đồ phủ:
    | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
    |---|---|---|---|
  - created: [[…]] (Q1–Q4) · updated: [[…]] · proposed: [[…]]
  - conflicts: [[…]] | không có
  - cần ingest: <src> <unit> (gỡ Qk, Qm), …
  ```
- Chạy `python tools/lint.py` (0 ERROR) và `python tools/citations.py --node <id>` cho từng synthesis mới: đối chiếu số liệu, phạm vi, "may/must" với claim được cite; sửa trước khi báo xong.

## 6. Báo cáo cuối và gợi ý tiếp theo
Research đáng giá ở chỗ nó cho user biết **làm gì tiếp** để bộ câu hỏi được trả lời đầy đủ hơn. Báo cáo cuối (cả khi dừng ở bước 2) gồm:
1. Bảng phủ sau khi viết, so với bước 1 (câu nào đổi mức, vì sao).
2. Thay đổi trong vault: created / updated / proposed, conflict.
3. **`## Gợi ý tiếp theo`** — mục riêng, luôn là mục cuối, mỗi gợi ý một dòng có lệnh chạy được ngay và lý do:
   - **Ingest** (xếp theo số câu gỡ được): `/ingest <src> <unit>` — gỡ Qk, Qm; ghi rõ khi unit đã `done` nhưng ingest bỏ sót đoạn nào (locator, dòng raw).
   - **Chờ user duyệt**: đề xuất đã ghi vào `## Đề xuất cập nhật` của note `reviewed`/`canonical`; claim source note diễn đạt lệch trích dẫn.
   - **Lỗi wiki phát hiện được** (citation lệch, câu có số thiếu citation, quy định hết hiệu lực): đề xuất `/lint` hoặc `python tools/citations.py --node <id>`, không tự sửa node ngoài cụm.
   - **Research tiếp**: cụm câu hỏi kế tiếp trong bộ gốc, hoặc câu hỏi mới lộ ra khi viết.
   - Khi phù hợp: đề xuất `/compact` trước bước tiếp theo.
