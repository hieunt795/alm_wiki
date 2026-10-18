---
name: ingest
description: Gọi bằng /ingest source_id [unit]. Biên dịch một ingest unit đã register (chương Basel, Chương/Mục/Phụ lục thông tư NHNN, chương sách, clipping) thành source note có trích nguyên văn + block-id, rồi tạo/cập nhật node wiki, bảng Basel vs VN, index, overview, registry, log; kết thúc khi tools/lint.py 0 error.
---

# /ingest <source_id> [unit]

Ingest là lúc tri thức được "biên dịch" vào wiki. Source note là lớp evidence: mọi node sau này đều đứng trên các trích dẫn ở đây. Một trích dẫn sai hoặc một block-id bịa sẽ làm hỏng chuỗi truy ngược của mọi node cite nó. Vì vậy phần lớn kỷ luật của skill này nằm ở bước 3. `tools/lint.py` kiểm tra bằng máy rằng mọi trích dẫn có thật trong raw.

Mặc định ingest **một unit mỗi lần**. Nguồn T5 (clipping) có thể làm theo batch khi user yêu cầu. Không ghi gì vào `01_sources/`.

## Ba chế độ
| Lệnh | Khi nào | Đi qua bước |
|---|---|---|
| `/ingest <src> <unit>` (unit `pending`) | Ingest unit mới | 0 → 6 |
| `/ingest <src> <unit>` (unit đã `done`) | **Bổ sung** đoạn mà lần ingest trước bỏ sót (research hay lint chỉ ra locator/dòng raw) | 0, 1 (chỉ đoạn được chỉ ra), 2, 3 (chỉ thêm), 4, 5 (không `mark`), 6 |
| `/ingest --node <id>` | **Biên dịch node từ claim đã có** trong source note, thường để hoàn thiện stub | xem mục "Chế độ --node" |

**Chế độ bổ sung.** Không sửa claim cũ, vì block-id cũ đang được cite. Claim mới dùng block-id tiếp theo sau block-id lớn nhất của unit đó (`grep -o '\^<tiền tố block-id>-[0-9]*\b' 02_wiki/sources/<src>.md | sed 's/.*-//' | sort -n | tail -1`). Không chạy lại `registry.py mark`, để giữ ngày ingest gốc. Log ghi `## [YYYY-MM-DD] ingest | <src> <UNIT> (bổ sung)`, kèm block-id mới.

### Chế độ --node
Dùng khi nguồn đã ingest có đủ claim cho một khái niệm nhưng chưa có node, hoặc node đang là stub. Không có unit raw nào được đọc mới, nên chất lượng node phụ thuộc hoàn toàn vào claim đã duyệt.
1. **Gom claim.** Lấy block-id ở dòng "Claim sẵn có" của stub, rồi grep title, alias và thuật ngữ trong `02_wiki/sources/*.md` để tìm thêm. Không đọc nguyên file raw; chỉ mở raw (`registry.py read <src> <unit> --from N --to M`) khi claim mơ hồ về phạm vi hoặc tính bắt buộc.
2. **Đề xuất rồi dừng chờ** như bước 2: danh sách claim sẽ dùng, type, relations dự kiến, chỗ còn thiếu.
3. **Viết node** theo bước 4. Gỡ callout stub, bỏ `*stub*` ở dòng index.
4. Claim không đủ để viết định nghĩa: giữ stub, sửa dòng "Hoàn thiện bằng" sang unit cần ingest, báo user.
5. Không chạy `registry.py mark`. Log ghi `## [YYYY-MM-DD] ingest | --node <id>`.
6. Chạy mục "Nối lại khi có node mới" (bước 4), rồi bước 6.

## 0. Định hướng
```bash
python tools/registry.py show <source_id>     # metadata, units, trạng thái, số dòng
```
- Không chỉ định unit: chọn unit `pending` có giá trị nhất cho ALM. Bỏ qua `preamble`, mục lục, lời nói đầu.
- Unit chỉ định đã `done`: chuyển sang chế độ bổ sung (mục "Ba chế độ"). Không có locator hay dòng raw cần bổ sung thì hỏi user, không ingest lại cả unit.
- Đọc `02_wiki/index.md` để biết node nào đã có, tránh tạo trùng (kiểm tra cả alias) và biết node nào cần cập nhật.
- Source note `02_wiki/sources/<source_id>.md` đã tồn tại: đọc nó để biết `units_done` và các block-id đã dùng. Block-id mới không được trùng block-id cũ.

## 1. Đọc unit
```bash
python tools/registry.py read <source_id> <unit>                 # giữ số dòng gốc, bỏ URL của link
python tools/registry.py read <source_id> <unit> --from 900 --to 1100
```
- Unit dài hơn ~400 dòng: đọc theo từng đoạn. **Không** đọc nguyên file nguồn lớn (BaselFramework 3,6 MB, sách 2–3 MB).
- Unit tham chiếu định nghĩa nằm ở unit khác mà node cần (ví dụ công thức LCR nằm ở LCR20): đọc đoạn đó và trích. Đọc trọn unit đó thì mark done luôn; nếu chỉ đọc một phần thì ghi chú, không mark.
- Nghi lỗi convert (bảng lệch, mất công thức, ký tự lỗi): đối chiếu với file `original` nếu có. Ghi nhận vào mục "Ghi chú convert" của source note và vào `conversion.issues` trong registry (đổi `status` sang `partial` nếu đang là `ok`).
- **Viết công thức trong node**: `$$…$$` đứng riêng dòng, citation ở dòng dưới (cùng thụt lề); không đặt `[[…]]` trong `\text{}`; `%`, `&`, `_` trong `\text{}` phải escape. `lint.py` báo ERROR `math-*` nếu sai.
- **Công thức bị mất** (`<!-- formula-not-decoded -->`, phân số vỡ): không trích công thức đó, vì không có gì để trích. Có thể dựng lại công thức trong node từ lời văn của nguồn, nhưng phải đặt dưới nhãn `*Diễn giải (tái dựng, chưa đối chiếu bản gốc):*`. Nếu nguồn có ví dụ số thì kiểm công thức tái dựng bằng ví dụ đó và ghi kết quả.
- **Nội dung trùng ở nguồn khác** (ví dụ LCR30 có cả trong `src-bcbs-lcr` lẫn `src-bcbs-framework`): ingest một lần ở nguồn chuyên biệt, rồi đề xuất user đánh dấu unit tương ứng ở nguồn kia là `skipped`.

## 2. Đề xuất cho user, rồi dừng chờ
User là người quyết định phạm vi node. Trình bày ngắn:
- 3–5 takeaway chính, mỗi ý kèm locator.
- Bảng node dự kiến: `id | type | tạo mới / cập nhật | lý do`.
- Các điểm khác Basel hoặc mâu thuẫn với wiki hiện có.

Nếu có tool AskUserQuestion, đưa 2–3 phương án: đề xuất / gọn / mở rộng. Nếu user đã nói rõ "làm luôn, khỏi hỏi" thì tự chọn phương án đề xuất, ghi lý do vào báo cáo cuối và tiếp tục.

## 3. Source note — quy tắc trích dẫn
Trước khi viết bước 3 và 4, đọc `.claude/skills/alm-writing-style/SKILL.md`: áp profile V1 cho câu diễn đạt claim, V2 cho node. Rule văn phong không áp lên trích nguyên văn và locator (P2).

Tạo từ `03_meta/templates/source.md` nếu chưa có. Dưới `## Key claims`, mỗi unit một heading `### <UNIT> — <tiêu đề>`. Mỗi claim có dạng:

```markdown
- Diễn đạt ngắn bằng tiếng Việt (tham số, điều kiện, phạm vi).
  > "Đoạn trích nguyên văn, copy từ raw."
  > "Đoạn trích thứ hai nếu cần … phần lược bỏ thay bằng dấu ba chấm."
  > — LCR40.1 ^lcr40-1
```

Lint (check `quote-not-found`) so từng dòng `> "…"` với raw đã chuẩn hoá: bỏ URL của link, footnote `[^…]`, `*`, `_`, list marker; gộp khoảng trắng. Vì vậy:
- Copy đúng chữ từ output của `registry.py read`. Không sửa chính tả, không dịch, không viết lại. Văn bản tiếng Việt trích nguyên tiếng Việt.
- Đoạn trích phải liền mạch. Cần bỏ footnote hay mệnh đề xen giữa thì dùng `…`; mỗi mảnh hai bên `…` vẫn phải khớp raw.
- Không escape ngoặc kép (`\"`). Ngoặc kép bên trong để nguyên.
- Bảng trong raw thì chép thành bảng markdown dưới claim, không đặt trong `> "`, kèm trích câu dẫn của bảng.
- Dòng locator đặt cuối claim: `> — <locator> ^<block-id>`.
  - Block-id viết chữ thường, chỉ gồm chữ, số và gạch ngang, theo đơn vị nhỏ nhất của nguồn: Basel `^lcr30-2`; thông tư `^d16-1` (Điều 16 khoản 1), `^d20-2b`, `^pl1-b2` (Phụ lục 1 phần B mục 2); sách `^ch1-3`; clipping `^p3`.
  - Locator theo `03_meta/taxonomy.md`: `LCR30.2`, `Đ16.1`, `PL1.B.II.1`, `ch1 §1.3`.
- Chọn claim có giá trị: định nghĩa, công thức, tham số/ngưỡng, hiệu lực và lộ trình, phạm vi áp dụng, nghĩa vụ, ngoại lệ. Bỏ FAQ lặp lại và footnote kỹ thuật.
- Cập nhật frontmatter `units_done`, mục `## Node bị ảnh hưởng`, `## Mâu thuẫn ghi nhận`.

## 4. Node tri thức
Chọn type theo mục "Chọn node type" trong `CLAUDE.md`. Template nằm ở `03_meta/templates/<type>.md`. ID viết kebab-case tiếng Anh, không chứa domain.

- **Mọi câu factual phải có citation** `[[<source_id>#^<block-id>]]` trỏ tới block-id có thật, **kể cả từng dòng bảng tham số**. Dòng bảng thiếu citation riêng thì `/lint` không ghép được dòng đó với nguồn (`citations.py` bỏ sót), và lỗi số liệu ở dòng đó sẽ lọt. Phần diễn giải hoặc suy luận của LLM (hàm ý ALM, so sánh, nhận định) đặt sau nhãn `*Diễn giải:*`.
  - Đừng viết fact mà nguồn đã ingest không nói. Lỗi pilot từng gặp: viết "Ban thư ký BCBS đặt tại BIS" khi nguồn không nhắc tới. Thiếu nguồn thì ghi `[cần nguồn]`.
- Node `draft`: sửa trực tiếp. Node `reviewed` hoặc `canonical`: không sửa thân bài, ghi vào `## Đề xuất cập nhật`.
- **Node stub**: cần link tới khái niệm chưa đủ nguồn để viết thì tạo stub. Stub tốt hơn link gãy. Đây là định dạng chuẩn, research và lint dùng chung: node `draft` theo template của type, ngay dưới frontmatter là callout 3 dòng cố định để lint đọc được:
  ```markdown
  > [!note] Node stub
  > Claim sẵn có: [[src-…#^…]], [[src-…#^…]] | chưa có
  > Hoàn thiện bằng: `/ingest --node <id>` | `/ingest <src> <unit>`
  > Phát hiện: research <chủ đề> [YYYY-MM-DD] | ingest <src> <unit> [YYYY-MM-DD]
  ```
  - `sources` bắt buộc khác rỗng (lint `required-field`): liệt kê source note chứa claim sẵn có hoặc chứa unit cần ingest. Nguồn chưa có source note (chưa register hoặc chưa ingest unit nào) thì không tạo stub; ghi vào `## Bất định` và gợi ý `/register` hoặc `/ingest`.
  - Thân stub không có câu factual; `relations` chỉ khai cạnh có `cite` tới claim đã có. Dòng index ghi `*stub*`.
  - Khi node thoát stub (ingest đúng unit, hoặc `/ingest --node`): gỡ callout, viết đầy đủ, bỏ `*stub*` ở index, rồi chạy "Nối lại khi có node mới".
- `aliases` có cả tên tiếng Việt và tiếng Anh, nhưng không trùng alias của node khác (lint báo `alias-collision`). Source note không cần alias.
- `relations` chỉ dùng enum trong taxonomy (mục "Relation" của `03_meta/taxonomy.md`): `part-of`; `measures`, `governs`, `limits`; `drives`, `input-to`; `hedges`, `priced-by`, `exposed-to`, `implements`, `supersedes`, `amends`.
  - Khai ở node A theo chiều A → B, thể chủ động, chỉ một chiều. Ví dụ `governs` nằm ở node regulation (`bcbs-lcr` → `lcr`), nên ingest một quy định thì cập nhật `relations` của node regulation đó.
  - A và B đều là node tri thức. Synthesis và source note không làm chủ thể hay đích của relation; cần trỏ tới synthesis thì dùng link trong thân bài (taxonomy, mục "Relation").
  - Quan hệ do nguồn nói ra (A đo B, quy định A điều chỉnh B, A là đầu vào của B) thì thêm `cite: "[[<source_id>#^<block-id>]]"`. Quan hệ là suy luận thì bỏ `cite` và giải thích dưới `*Diễn giải:*` trong thân bài.

### Nguồn VN và bảng Basel vs VN
Đây là giá trị đặc thù của wiki: biết VN khác Basel ở đâu.
- Node metric và concept liên quan có bảng `## Basel vs VN`. Ingest nguồn VN thì thay `[cần nguồn]` bằng giá trị VN kèm citation, và điền điều khoản (`Đ16.1`) cùng hiệu lực.
- Giá trị VN khác Basel không phải mâu thuẫn (khác jurisdiction), nhưng phải ghi rõ trong bảng; có thể thêm một dòng "Khác biệt" dưới bảng. Callout `> [!conflict]` chỉ dùng khi hai nguồn **cùng phạm vi** nói khác nhau. Đánh giá theo thứ tự: cùng đối tượng? → jurisdiction → scope → hiệu lực → specificity → tier.
- Regulation node VN cần các field: `issuer: SBV`, `number`, `jurisdiction: VN`, `issued`, `valid_from` (ngày có hiệu lực), lộ trình nhiều mốc trong bảng "Yêu cầu chính", `amends`/`supersedes` theo điều khoản thi hành. Thêm `implements: ["[[bcbs-…]]"]` khi văn bản nội luật hoá chuẩn Basel tương ứng (tên chỉ tiêu và cấu trúc tương đương). Căn cứ là suy luận thì ghi `*Diễn giải:*`.
- Đánh dấu `superseded`/`retired` cho node khác là quyết định của user: đề xuất, không tự làm.

### Synthesis bị ảnh hưởng
Synthesis đứng trên node tri thức. Unit mới đổi nội dung node mà synthesis không biết thì kết luận của nó cũ dần ("stale claims that newer sources have superseded" theo Karpathy). Ingest không viết lại synthesis, vì synthesis trả lời bộ câu hỏi của user và đổi kết luận là việc của `/research` hoặc `/query`, nơi user tham gia. Ingest chỉ **đánh dấu**:
```bash
grep -l '\[\[<node-id>[]|#]' 02_wiki/syntheses/*.md    # cho từng node vừa đổi nội dung
grep -l '\[\[<source_id>#' 02_wiki/syntheses/*.md      # synthesis cite cùng nguồn
```
- Chỉ đánh dấu khi thay đổi có thể làm lệch kết luận: tham số/ngưỡng mới hoặc khác, conflict mới, giá trị VN thay `[cần nguồn]`, phạm vi hay hiệu lực đổi, quan hệ mới hoặc đổi chiều. Thêm link hay sửa câu chữ thì bỏ qua.
- Synthesis `draft`: append vào `## Bất định` một dòng `- [YYYY-MM-DD] ingest <source_id> <UNIT>: [[node]] <thay đổi gì>; cần rà lại <Qk hoặc mục>.` Không sửa phần còn lại.
- Synthesis `reviewed`/`canonical`: ghi dòng tương tự vào `## Đề xuất cập nhật` (tạo mục này ở cuối file nếu chưa có).
- Dòng đánh dấu không bị xoá khi xử lý xong; lần `/research` hoặc `/query` cập nhật synthesis thêm `→ đã rà [YYYY-MM-DD]` vào cuối dòng.

### Nối lại khi có node mới
Áp dụng khi tạo node mới (bất kỳ chế độ nào) và khi node thoát stub. Trước khi node tồn tại, các node và synthesis khác chỉ nhắc khái niệm bằng chữ, link tạm tới node gần nhất, hoặc giải thích nó ngay trong thân bài. Không nối lại thì node mới đứng riêng và wiki không tích luỹ:
```bash
grep -rlin -e '<title>' -e '<alias1>' -e '<alias2>' 02_wiki --include=*.md | grep -v '02_wiki/sources/'
grep -rn '#\^<block-id node mới cite>\]\]' 02_wiki/{concepts,metrics,instruments,models,regulations,entities}
```
- **Node tri thức nhắc khái niệm mà chưa link**: node `draft` thì thêm `[[id]]` ở lần nhắc đầu; `reviewed`/`canonical` thì ghi vào `## Đề xuất cập nhật`.
- **Quan hệ có `cite` thuộc claim của node mới nhưng `to` trỏ tới node khác**: liệt kê và đề xuất chuyển đích, chờ user duyệt. Không tự chuyển, vì đổi đích là đổi nghĩa quan hệ.
- **Synthesis nhắc khái niệm**: đánh dấu như mục trên (`## Bất định` hoặc `## Đề xuất cập nhật`): `- [YYYY-MM-DD] ingest <src> <UNIT | --node>: đã có node [[id]]; cần rà lại <mục>.`
- Ghi kết quả vào log (dòng `backfill`) và báo cáo cuối.

## 5. Cập nhật sổ sách
```bash
python tools/registry.py mark <source_id> <unit> [<unit>…]     # status: done + ngày ingest
```
- `02_wiki/index.md`: mỗi node mới một dòng `[[id]] — tóm tắt · domains · maturity`. Sửa dòng của node đã cập nhật nếu tóm tắt thay đổi; bỏ chữ *stub* khi node đã đầy đủ.
- `02_wiki/overview.md`: bảng tiến độ; cập nhật node trung tâm hoặc thesis nếu bức tranh thay đổi.
- `02_wiki/log.md` (append):
  ```
  ## [YYYY-MM-DD] ingest | <source_id> <UNIT>
  - created: [[…]]
  - updated: [[…]]
  - proposed: [[…]] (node reviewed — chỉ đề xuất)
  - conflicts: [[…]] | không có
  - syntheses flagged: [[…]] (<thay đổi>) | không có
  - backfill: linked [[…]] · flagged [[…]] · proposed [[…]] | không có
  - tiếp theo: <unit nên ingest tiếp>
  ```

## 6. Kiểm tra trước khi báo xong
```bash
python tools/lint.py      # phải 0 ERROR
```
Hay gặp: `quote-not-found` (trích dẫn bị sửa chữ, hãy copy lại từ raw), `broken-block-ref` (cite block-id chưa tạo), `broken-link` (link bằng alias hoặc node chưa tạo, dùng id hoặc tạo stub). Sửa cả warning `orphan`/`index` nếu do lần ingest này gây ra.

Báo cáo cuối cho user gồm:
- node created/updated;
- số claim;
- tham số Basel vs VN đã điền;
- conflict;
- synthesis đã đánh dấu cần rà lại; kết quả nối lại (link đã thêm, quan hệ đề xuất chuyển đích);
- stub đã tạo hoặc đã hoàn thiện;
- câu hỏi mở;
- 1–2 unit nên ingest tiếp.
