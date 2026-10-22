---
name: research
description: Gọi bằng /research <chủ đề> [bộ câu hỏi]. Nghiên cứu một vấn đề ALM phức tạp hoặc một bộ nhiều câu hỏi (vd 20 câu về IRRBB, 7 câu về FTP) dựa trên wiki — lập bản đồ phủ câu hỏi ↔ node, chỉ ra lỗ hổng nguồn và unit cần ingest, rồi viết synthesis origin research theo cụm câu hỏi kèm một synthesis tổng quan (hub) trả lời ở cấp chủ đề, có citation. Câu hỏi đơn lẻ dùng /query. Chỉ chạy khi user gọi.
disable-model-invocation: true
---

# /research <chủ đề> [bộ câu hỏi]

`/query` trả lời một câu. `/research` xử lý cả một vấn đề: nhiều câu hỏi liên quan nhau, cần đi qua nhiều node, nhiều nguồn, và thường lộ ra chỗ wiki chưa có nguồn. Giá trị chính của skill không phải là văn bản dài, mà là **bản đồ phủ**: câu nào wiki trả lời được bằng citation, câu nào chỉ trả lời được một phần, câu nào phải ingest thêm. Synthesis viết ra chỉ đáng tin bằng các citation bên dưới nó.

Không ghi gì vào `01_sources/`. Số liệu, ngưỡng, tham số và nghĩa vụ quy định chỉ lấy từ nguồn đã ingest; thiếu nguồn thì ghi `[cần nguồn]` hoặc đề xuất unit để `/ingest`. Kiến thức nền của LLM chỉ được dùng để nối mạch giữa các ý có nguồn (xem bước 4).

**Quan hệ là dữ liệu của node khái niệm, không phải của synthesis.** Phân tích một vấn đề là đi theo chuỗi quan hệ (A `drives` B, B `input-to` C…), nên research phải đọc, kiểm chứng và trình bày các cạnh đó. Nhưng cạnh chỉ được khai trong `relations` của node đúng chủ thể A. Relation đọc là "A → B, thể chủ động" với A là node chứa nó (`03_meta/taxonomy.md`, mục "Relation"), nên synthesis làm chủ thể ("bài phân tích `measures` basis risk") là sai nghĩa. Khai lặp một cạnh ở cả node lẫn synthesis thì sớm muộn hai bên lệch nhau. Tương tự, synthesis cũng không làm **đích** của relation (`contingency-funding-plan` `input-to` một bài phân tích là sai nghĩa); node tri thức muốn trỏ tới synthesis thì dùng link trong thân bài. Synthesis trình bày chuỗi quan hệ trong thân bài (bước 4) và để `relations: []`.

Theo pattern của Karpathy, kết quả khám phá phải "compound in the knowledge base just like ingested sources do". Ở vault này, thứ được đưa ngược vào wiki là **cấu trúc, không phải nội dung**: cạnh quan hệ có cite, conflict, lỗ hổng nguồn, stub cho khái niệm cần node riêng, link. Diễn giải của synthesis không bao giờ quay lại làm bằng chứng cho node khác.

**Phân tích theo câu hỏi, trình bày theo chủ đề.** Bộ câu hỏi là cách user chia vấn đề trong một lần hỏi, không phải cấu trúc của tri thức: số Qk chỉ có nghĩa trong lần chạy đó, và lần hỏi sau về cùng chủ đề sẽ chia khác. Vì vậy:
- Câu hỏi dùng để **kiểm độ phủ** (mỗi Qk một mức phủ, một câu trả lời thẳng trong `## Kết luận` của cụm).
- Cụm là đơn vị **viết và review** (một synthesis ≤ 300 dòng, cập nhật cục bộ khi ingest gỡ được vài câu).
- **Hub** là đơn vị **đọc theo chủ đề**: khi bộ câu hỏi có ≥ 2 cụm, một synthesis tổng quan trả lời liền mạch cả chủ đề, giữ bảng Qk → cụm → mức phủ hiện hành, và chứa phần regime, hàm ý ALM, bất định ở cấp chủ đề để các cụm không lặp lại. Hub không có fact mới: chỉ dùng lại citation đã verify ở cụm.
- Tri thức về từng khái niệm vẫn thuộc node khái niệm. Hub và cụm không chép lại node; chỗ node còn thiếu nội dung mà source note đã có claim thì đề xuất `/ingest --node` (bước 3, bước 6).

Một bộ 20 câu chạm tới hàng chục node dài 200–350 dòng; đọc hết ngay từ đầu sẽ đầy context trước khi viết được chữ nào. Vì vậy skill tách hai pha: bước 1–2 chỉ đọc lướt (index, frontmatter, heading) để lập bản đồ; bước 3–4 mới đọc kỹ, và chỉ cho **một cụm** mỗi lượt.

## 0. Chuẩn bị
- Đọc `.claude/skills/alm-writing-style/SKILL.md` (profile V3 cho synthesis). Trong vault này chỉ dùng skill văn phong đó.
- Chuẩn hoá bộ câu hỏi: đánh số Q1…Qn, giữ nguyên chữ của user. User chỉ đưa chủ đề thì đề xuất 5–10 câu hỏi khung (bản chất → cơ chế → đo lường → quy định Basel/VN → quản trị), chờ user chỉnh rồi mới làm tiếp.
- Xác định thời điểm (mặc định hôm nay; "as-of X" thì lọc theo `valid_from`/`valid_to` như `/query`) và jurisdiction. Câu hỏi nghĩa vụ tại VN: quy định NHNN là căn cứ, Basel chỉ là tham chiếu.
- Tìm research cũ của chủ đề: hub (`grep -l 'research-hub' 02_wiki/syntheses/*.md`, so `question` và title) và dòng `research | <chủ đề>` trong `02_wiki/log.md`. Có hub thì bảng phủ trong `## Câu hỏi` của hub là điểm xuất phát (bản hiện hành); log là lịch sử. Chỉ ra câu nào đã đổi mức phủ (thường sau khi ingest thêm unit).
- Tìm dòng đánh dấu của ingest chưa rà trong synthesis của chủ đề: `grep -n '\] ingest .*cần rà lại' 02_wiki/syntheses/*.md | grep -v 'đã rà'`. Câu hỏi bị đánh dấu được xác nhận lại mức phủ ở bước 1. Khi cập nhật synthesis đó xong, xoá dòng đánh dấu và ghi vào `log.md`; mục rỗng thì ghi `*Chưa có nội dung cần cập nhật.*` (CLAUDE.md quy tắc 13).

## 1. Bản đồ phủ (coverage map)
Với từng câu hỏi, tìm trong wiki, **chỉ đọc lướt**, không đọc thân bài node và không đọc raw:
- `02_wiki/index.md` (dòng tóm tắt từng node) → node liên quan → `relations` trong frontmatter; chiều ngược dùng `grep -rn 'to: "\[\[<id>\]\]"' 02_wiki`.
- Heading và frontmatter: `grep -n '^question\|^maturity\|^## \|^### ' <file>`. Đủ để biết node có mục trả lời câu hỏi không.
- **Synthesis đã có** trong `02_wiki/syntheses/`: so `question` và heading. Synthesis cụm trả lời đúng câu đó thì dùng lại, không viết trùng. Hub (tag `research-hub`) không tính là nơi trả lời: cột "Node / synthesis" ghi synthesis cụm, hub chỉ ghi ở dòng tổng.
- Nguồn VN: kiểm tra có node regulation NHNN cho chủ đề không (`grep -l 'jurisdiction: VN' 02_wiki/regulations/*`). Không có thì ghi rõ trong cột "Thiếu gì".
- Unit chưa ingest có thể chứa câu trả lời: `python tools/registry.py show <src>` (xem unit `pending` và heading).

- **Bản đồ quan hệ của cụm.** Chỉ đọc frontmatter của node ứng viên:
  ```bash
  for f in <file ứng viên>; do awk '/^---$/{c++;next} c==1' "$f" | grep '{type:' | sed "s|^|$(basename "$f" .md): |"; done
  grep -rn 'to: "\[\[<id>\]\]"' 02_wiki/{concepts,metrics,instruments,models,regulations,entities}   # chiều ngược
  ```
  - Bỏ qua relation khai trong `02_wiki/syntheses/` và relation có `to:` trỏ tới một synthesis: đó là dữ liệu cũ sai quy ước, không dùng làm bằng chứng.
  - Ghi vào cột "Thiếu gì": **thiếu cạnh** (câu hỏi hỏi về quan hệ X–Y nhưng không có cạnh nối), **cạnh không cite**, **thiếu chiều/regime** (câu hỏi hỏi về chiều tác động nhưng `drives` chưa có `direction`/`regime`).
  - Câu hỏi về cơ chế mà cạnh then chốt thiếu hoặc không cite thì tối đa là **một phần**.
  - Câu hỏi mà khái niệm then chốt chỉ có node dạng stub (`> [!note] Node stub`) thì tối đa là **một phần**.

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

Bộ câu hỏi có **≥ 2 cụm** thì đặt luôn id cho hub, theo tên chủ đề (vd `balance-sheet-fundamentals-and-risk-transmission`), và báo cho user cùng lúc với danh sách cụm. Bộ chỉ có một cụm thì không tạo hub: synthesis cụm đó đã là câu trả lời ở cấp chủ đề. Chủ đề đã có hub thì cụm mới gắn vào hub đó, không tạo hub thứ hai.

Hub đã có: `draft` thì cập nhật trực tiếp (bảng phủ, kết luận, các mục cấp chủ đề); `reviewed`/`canonical` thì ghi vào `## Đề xuất cập nhật`, riêng bảng phủ có thể ghi ở log nếu user chưa duyệt.

Cụm đã có synthesis:
- Synthesis `draft`: cập nhật trực tiếp, bổ sung câu hỏi vào `question` và mục `## Câu hỏi`. File cũ không theo heading template thì **giữ nguyên cấu trúc**, chỉ thêm mục mới; tái cấu trúc cả file dễ làm lệch câu đã cite (R3 trong `alm-writing-style`). File cũ còn khai `relations`: xử lý từng cạnh theo mục "Verify cạnh" ở bước 3 (cạnh có cite và đúng chủ thể thì chuyển về node khái niệm nếu node đó chưa có; cạnh synthesis → synthesis thì đổi thành link trong thân bài), rồi đặt `relations: []`.
- Synthesis `reviewed`/`canonical`: không sửa thân bài, ghi vào `## Đề xuất cập nhật`, hoặc tạo synthesis mới bổ sung và link qua lại.

## 3. Verify trước khi viết
Giờ mới đọc kỹ các node và synthesis của **cụm đang viết**. Cập nhật lại mức phủ nếu đọc xong thấy khác ước lượng ở bước 1.

Với mọi số liệu, ngưỡng, tham số, nghĩa vụ quy định sẽ dùng: đi theo citation về source note, đọc trích nguyên văn. Nghi ngờ thì grep locator trong raw (`python tools/registry.py read <src> <unit> --from N --to M`). Không đọc nguyên file nguồn lớn.

Đọc raw có thể lộ ra đoạn liên quan mà source note chưa có claim (unit đã `done` nhưng ingest bỏ sót). **Không tự thêm claim vào source note**, kể cả note `draft` và kể cả khi trích dẫn sẽ khớp raw: thêm claim là việc của `/ingest`, nơi user duyệt phạm vi từng unit; làm ngầm trong research sẽ đẩy mức phủ lên bằng bằng chứng chưa ai duyệt. Ghi đoạn đó (locator, dòng raw, câu hỏi nó gỡ) vào `## Bất định` của synthesis và vào gợi ý cuối (bước 6); với source note `reviewed`/`canonical` có thể thêm vào `## Đề xuất cập nhật` của note đó.

**Verify cạnh.** Với mỗi cạnh sẽ dùng trong chuỗi quan hệ:
- Đi theo `cite` về source note, kiểm tra trích dẫn có nói đúng loại quan hệ, chiều và regime không. Sai thì không dùng cạnh đó, và ghi vào nhóm "Lỗi wiki phát hiện được" (bước 6).
- Cạnh mới, có claim và block-id **đã có** trong source note: node khái niệm A còn `draft` thì thêm vào `relations` của A, kèm `cite`; A đã `reviewed`/`canonical` thì ghi vào `## Đề xuất cập nhật` của A.
- Cạnh chỉ thấy trong raw, source note chưa có claim: không thêm, xử lý như claim bỏ sót ở trên (ghi `## Bất định` và gợi ý `/ingest`).
- Cạnh chỉ là suy luận: không ghi vào `relations` của node nào, chỉ trình bày trong synthesis sau `*Diễn giải:*`.
- Hai nguồn nói ngược chiều về cùng một cạnh: callout `> [!conflict]` ở node khái niệm A, giữ cả hai.

**Khái niệm cần node riêng** ("important concepts mentioned but lacking their own page" theo Karpathy). Dấu hiệu:
- Cụm đang viết phải định nghĩa hoặc giải thích công thức, cấu phần của một khái niệm chưa có node.
- Khái niệm đó đã được giải thích trong một synthesis khác, và node tri thức đang link tới synthesis đó để tra khái niệm (dòng "Xem chi tiết tại" trộn node với synthesis).

Khái niệm là **ứng viên stub** chỉ khi thoả cả ba tiêu chí đầu vào:
1. **Nguồn định danh khái niệm**: source note có claim định nghĩa, công thức hoặc cấu phần của nó (`grep -n '<thuật ngữ>' 02_wiki/sources/*.md`), hoặc raw có đoạn như vậy và chỉ ra được unit cần ingest. Khung phân tích hay cách nhóm ý do LLM đặt ra (vd "kiến trúc 5 tầng", "integrated strategy") ở lại trong synthesis: nâng chúng thành node là để wiki tự xác nhận diễn giải của chính nó.
2. **Chưa có node**: không trùng id hay alias của node nào (`grep -rni '^aliases:.*<thuật ngữ>' 02_wiki`); một khái niệm chỉ có một node (CLAUDE.md quy tắc 8).
3. **Chọn được type** theo "Chọn node type" trong `CLAUDE.md`, gồm cả quy tắc metric cấu phần.

Khái niệm không đạt thì ghi vào `## Bất định` của synthesis, không tạo stub. Ứng viên đạt được trình cho user duyệt ở bước 5. Research chỉ tạo **stub**; nội dung node viết qua `/ingest --node <id>` hoặc `/ingest <src> <unit>`.

**Node thiếu nội dung.** Node đã có nhưng thiếu một mục mà cụm cần, trong khi source note **đã có claim** cho mục đó (vd node metric chưa có mục so sánh với một metric khác, trong khi source note có claim so sánh hai metric đó). Đây là tri thức theo chủ đề nên nằm ở node, không chỉ ở synthesis. Research không tự viết vào node; ghi lại `node | mục cần thêm | block-id sẵn có` để đề xuất `/ingest --node <id>` ở bước 6. Trong lúc chờ, synthesis vẫn dùng claim đó bằng citation trực tiếp.

Ghi nhận ngay khi gặp: hai nguồn cùng phạm vi nói khác nhau (→ callout `> [!conflict]`, giữ cả hai), Basel `consultative` (không trích như final), khác biệt Basel vs VN (không phải conflict, ghi rõ jurisdiction).

## 4. Viết synthesis
Viết các cụm trước (4a), hub sau cùng (4b): hub tổng hợp từ những gì cụm đã verify, nên viết hub trước sẽ kéo theo fact chưa kiểm.

### 4a. Synthesis cụm
Tạo `02_wiki/syntheses/<id>.md` từ `03_meta/templates/synthesis.md`. ID kebab-case tiếng Anh theo nội dung cụm (vd `irrbb-repricing-cash-flows-and-buckets`), không chứa "research" hay số câu hỏi.

Frontmatter: `origin: research`, `maturity: draft`, `question` = các câu của cụm (nối bằng " · ", giữ chữ của user, đặt trong ngoặc kép YAML; ngoặc kép bên trong đổi sang ngoặc đơn), `as_of`, `sources` = các source note thực sự được cite, `domains`, `aliases` có tên tiếng Việt và tiếng Anh nhưng không trùng alias node khác (lint báo `alias-collision`). `relations: []` **luôn để trống**: synthesis không làm chủ thể hay đích của relation (xem đoạn đầu skill); cạnh mới khai ở node tri thức theo bước 3.

Thân bài giữ heading của template, cụ thể hoá cho bộ câu hỏi:
- `## Câu hỏi`: dòng đầu "Thuộc chủ đề [[<hub>]] (Qa–Qb trong n câu)." khi có hub; sau đó danh sách Qk của cụm, đúng số thứ tự trong bộ gốc.
- `## Kết luận`: mỗi Qk 2–4 câu trả lời thẳng, có citation. Đây là chỉ mục để tra từng câu, nên giữ chia theo Qk.
- `## Cơ chế`: chia `###` **theo cơ chế hoặc ý chính**, không theo Qk; cuối heading gắn tag câu hỏi, vd `### Repricing gap truyền dẫn tới NII (Q3, Q4)`. Một Qk có thể trải nhiều mục, một mục có thể phục vụ nhiều Qk; nhờ vậy hai câu hỏi chạm cùng một cơ chế không phải giải thích hai lần. Mỗi Qk của cụm phải xuất hiện trong tag ít nhất một mục. Giải thích cơ chế, công thức, bảng; **mỗi câu factual và mỗi dòng bảng tham số có citation riêng** `[[src-…#^id]]`. Link node bằng `[[id]]` để người đọc đi sâu, không chép lại nguyên node.
  Mục nói về cơ chế mở đầu bằng **chuỗi quan hệ**, rồi mới giải thích:

  | Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
  |---|---|---|---|---|
  | [[gap-risk]] | drives | [[economic-value-of-equity]] | − · rising_rate | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |

  - Cột "Quan hệ" chỉ dùng enum trong taxonomy. Mỗi dòng có nguồn phải khớp một cạnh có thật trong `relations` của node "Từ", kể cả cạnh vừa thêm ở bước 3.
  - Dòng suy luận: cột Nguồn ghi `*Diễn giải:* (ngoài wiki, chưa có nguồn)`. Cạnh cần cho lập luận nhưng chưa có nguồn: `[cần nguồn]`.
  - Mục không nói về quan hệ (vd định nghĩa thuần) thì bỏ bảng, không viết dòng độn.
- `## Bằng chứng ủng hộ` · `## Bằng chứng trái chiều`: nguồn nào nói gì, chỗ nào các nguồn lệch nhau hoặc chỉ một nguồn T4 đứng sau.
- `## Phụ thuộc regime`: kết luận đổi thế nào theo môi trường lãi suất, loại ngân hàng, jurisdiction.
- `## Hàm ý ALM / quy định`: hàm ý cho ALCO/Treasury, phân biệt rõ nghĩa vụ NHNN và tham chiếu Basel. Wiki chưa có quy định NHNN cho chủ đề thì nói thẳng "chưa có nguồn NHNN trong wiki", để người đọc không hiểu nhầm chuẩn Basel là nghĩa vụ tại VN. Nhận định của LLM đặt sau `*Diễn giải:*`.
- `## Bất định`: câu/ý còn `[cần nguồn]`, unit đề xuất ingest, giả định chưa kiểm.

Heading template là cố định (P2), nhưng không phải câu hỏi nào cũng có nội dung cho mọi mục: câu "xây dựng như thế nào" thường không có bằng chứng trái chiều hay phụ thuộc regime. Khi đó ghi một dòng "Không ghi nhận trong nguồn đã ingest." thay vì viết câu độn. Khi có hub, phần regime, hàm ý ALM và bằng chứng mang tính chủ đề (đúng cho cả bộ câu hỏi, không riêng cụm) viết ở hub; cụm chỉ giữ phần riêng của cụm, phần còn lại ghi một dòng "Xem [[<hub>]]."

Không viết fact mà nguồn đã ingest không nói. Kiến thức nền chỉ dùng để nối mạch giữa các ý có nguồn, đặt sau `*Diễn giải:*` kèm "(ngoài wiki, chưa có nguồn)", và không bao giờ mang số liệu, ngưỡng hay nghĩa vụ quy định.

### 4b. Hub (khi có ≥ 2 cụm)
Người đọc mở hub để hiểu cả chủ đề; người review mở cụm để kiểm từng câu. Hub vì vậy ngắn (khoảng ≤ 150 dòng), liền mạch, và **không chứa fact mới**: mọi citation trong hub phải xuất hiện trong ít nhất một cụm của nó. Cần một fact mà cụm chưa có thì bổ sung vào cụm trước (qua bước 3), rồi mới dùng ở hub.

Tạo từ cùng template. Frontmatter như cụm, thêm `research-hub` vào `tags`; `question` = tên bộ câu hỏi của user (vd "Balance Sheet Fundamentals & Risk Transmission: Q1–Q6"); `sources` = hợp các source note được cite trong hub; `relations: []`.

Thân bài giữ 8 heading template, nội dung ở cấp chủ đề:
- `## Câu hỏi`: toàn bộ Q1…Qn (chữ của user) và **bảng phủ hiện hành**:

  | Q | Câu hỏi (rút gọn) | Synthesis cụm | Mức phủ | Thiếu gì |
  |---|---|---|---|---|

  Bảng này là bản hiện hành, được sửa mỗi lần research hoặc ingest đổi mức phủ; log giữ lịch sử. Cụm chưa viết ghi "chưa viết".
- `## Kết luận`: trả lời cả chủ đề thành 2–4 đoạn liền mạch, theo logic của vấn đề chứ không theo thứ tự Qk; tag `(Qk)` cuối câu để truy về câu hỏi. Mỗi câu factual có citation (lấy từ cụm).
- `## Cơ chế`: bản đồ chủ đề, tức các chuỗi quan hệ **nối giữa các cụm** (bảng như 4a, chỉ cạnh có thật trong `relations`) và một dòng cho mỗi cụm: cụm giải thích cơ chế gì, link `[[cụm]]`. Không giải thích lại nội dung đã có ở cụm.
- `## Bằng chứng ủng hộ` · `## Bằng chứng trái chiều`: chỉ những gì đúng ở cấp chủ đề (nguồn nào chống đỡ khung chung, chỗ các nguồn lệch nhau xuyên cụm).
- `## Phụ thuộc regime` · `## Hàm ý ALM / quy định`: phần chính của hub; hàm ý cho ALCO/Treasury ở cấp toàn bảng cân đối, tách nghĩa vụ NHNN và tham chiếu Basel. Nhận định đặt sau `*Diễn giải:*`.
- `## Bất định`: tổng hợp lỗ hổng của cả bộ; unit cần ingest xếp theo số câu gỡ được; node thiếu nội dung (bước 3).

Mỗi cụm có dòng "Thuộc chủ đề [[<hub>]]" trong `## Câu hỏi`. Với cụm `draft` có sẵn chưa có dòng này thì thêm dòng đó, **không** tái cấu trúc `### Qk` cũ sang heading theo cơ chế (R3: tái cấu trúc dễ làm lệch câu đã cite); cụm cũ được chuyển dần khi research lại sửa tới.

## 5. Sổ sách và kiểm tra
- **Duyệt stub** (khi bước 3 có ứng viên): trình bảng `id | type | claim sẵn có hoặc unit cần ingest | lý do`, dùng AskUserQuestion multiSelect nếu có. Dòng nào user duyệt thì tạo stub theo định dạng ở `.claude/skills/ingest/SKILL.md` (mục "Node stub"), thêm dòng index có `*stub*`. Synthesis link thẳng tới stub `[[id]]`; cạnh quan hệ có cite trỏ tới khái niệm đó khai thẳng tới stub, không trỏ tạm tới node gần nhất.
- `02_wiki/index.md`: thêm/sửa dòng synthesis `[[id]] — tóm tắt · domains · draft`. Dòng hub ghi "tổng quan chủ đề, n câu, k cụm" và đứng trước các dòng cụm của nó.
- Node khái niệm liên quan (draft): thêm link tới synthesis ở mục liên kết nếu giúp điều hướng.
- `02_wiki/log.md` (append):
  ```
  ## [YYYY-MM-DD] research | <chủ đề>
  - bộ câu hỏi: n câu · phủ: x đủ / y một phần / z thiếu · phương án: <ingest trước | viết theo cụm | chỉ bản đồ>
  - bản đồ phủ:
    | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
    |---|---|---|---|
  - hub: created | updated [[…]] | không có (1 cụm)
  - created: [[…]] (Q1–Q4) · updated: [[…]] · proposed: [[…]]
  - conflicts: [[…]] | không có
  - relations: added [[a]] —drives→ [[b]] (cite) · proposed [[c]] —input-to→ [[d]] | không có
  - stubs: created [[…]] (<type>, claim: [[src-…#^…]] | cần ingest <src> <unit>) | không có
  - cần ingest: <src> <unit> (gỡ Qk, Qm), … · node thiếu nội dung: [[id]] mục <…> (^block-id) | không có
  ```
  Cột "Thiếu gì" của bảng phủ ghi cả thiếu cạnh, cạnh không cite, thiếu chiều/regime (bước 1).
- Chạy `python tools/lint.py` (0 ERROR) và `python tools/citations.py --node <id>` cho từng synthesis mới, kể cả hub: đối chiếu số liệu, phạm vi, "may/must" với claim được cite; sửa trước khi báo xong.
- Kiểm tra hub không có fact mới: mọi block-ref trong hub có trong ít nhất một cụm.
  ```bash
  grep -o '\[\[src-[^]]*#\^[^]|]*' 02_wiki/syntheses/<hub>.md | sort -u > scratch/hub-refs.txt
  cat 02_wiki/syntheses/{<cụm1>,<cụm2>,…}.md | grep -o '\[\[src-[^]]*#\^[^]|]*' | sort -u | comm -23 scratch/hub-refs.txt -   # phải rỗng
  ```
- Kiểm tra quan hệ (lint chưa bắt): synthesis mới hoặc vừa sửa (kể cả hub) có `relations: []` và không node nào trỏ relation tới nó (`grep -rn 'to: "\[\[<synthesis-id>\]\]"' 02_wiki` rỗng); mỗi dòng có nguồn trong bảng chuỗi quan hệ tìm thấy cạnh tương ứng bằng `grep '{type: <type>, to: "\[\[<B>\]\]"' <file của A>`.

## 6. Báo cáo cuối và gợi ý tiếp theo
Research đáng giá ở chỗ nó cho user biết **làm gì tiếp** để bộ câu hỏi được trả lời đầy đủ hơn. Báo cáo cuối (cả khi dừng ở bước 2) gồm:
1. Bảng phủ sau khi viết, so với bước 1 (câu nào đổi mức, vì sao).
2. Thay đổi trong vault: hub, created / updated / proposed, conflict. Có hub thì đưa link hub trước: đó là chỗ user đọc câu trả lời theo chủ đề.
3. **`## Gợi ý tiếp theo`** — mục riêng, luôn là mục cuối, mỗi gợi ý một dòng có lệnh chạy được ngay và lý do:
   - **Ingest** (xếp theo số câu gỡ được): `/ingest <src> <unit>` — gỡ Qk, Qm; ghi rõ khi unit đã `done` nhưng ingest bỏ sót đoạn nào (locator, dòng raw).
   - **Stub cần hoàn thiện**: stub vừa tạo hoặc stub có sẵn mà cụm dùng tới, mỗi dòng một lệnh: `/ingest --node <id>` (đã có claim) hoặc `/ingest <src> <unit>` (cần ingest).
   - **Node thiếu nội dung** (bước 3): `/ingest --node <id>` — thêm mục <…> từ claim sẵn có ^…, gỡ Qk. Đây là đường đưa tri thức theo chủ đề về node khái niệm.
   - **Thiếu cạnh**: cạnh nên thêm khi ingest unit nào (`/ingest <src> <unit>` — cạnh A —type→ B, gỡ Qk); cạnh đang chờ duyệt ở node `reviewed`/`canonical`.
   - **Chờ user duyệt**: đề xuất đã ghi vào `## Đề xuất cập nhật` của note `reviewed`/`canonical`; claim source note diễn đạt lệch trích dẫn.
   - **Lỗi wiki phát hiện được** (citation lệch, câu có số thiếu citation, quy định hết hiệu lực): đề xuất `/lint` hoặc `python tools/citations.py --node <id>`, không tự sửa node ngoài cụm.
   - **Research tiếp**: cụm câu hỏi kế tiếp trong bộ gốc, hoặc câu hỏi mới lộ ra khi viết.
   - Khi phù hợp: đề xuất `/compact` trước bước tiếp theo.
