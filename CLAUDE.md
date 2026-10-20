# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# ALM Wiki — Constitution

## Dự án là gì
Một **Obsidian vault** chứa wiki tri thức cá nhân về quản trị tài sản nợ – tài sản có (ALM) của ngân hàng, vận hành theo pattern LLM Wiki của Karpathy. Đây là repo **nội dung markdown**, không phải phần mềm: "code" duy nhất là các script Python kiểm tra và quản lý registry trong `tools/`.
- Ba lớp: **raw** (`01_sources/`, bất biến) → **wiki** (`02_wiki/`, LLM viết) → **schema** (`CLAUDE.md` + `03_meta/`).
- LLM là *knowledge compiler / maintainer*: đọc nguồn, biên dịch thành node markdown liên kết, duy trì theo thời gian. LLM **không phải** source of truth.
- Tri thức tích luỹ dần (compounding): một lần ingest cập nhật nhiều node, câu trả lời query có giá trị được lưu thành synthesis. Không phải RAG.

## Phục vụ ai
- **Một người dùng duy nhất là chủ wiki.** Người này chọn nguồn, đặt câu hỏi, và là reviewer duy nhất (maturity `draft` → `reviewed` → `canonical`, promote bằng tay).
- Bối cảnh áp dụng là ngân hàng tại Việt Nam: câu hỏi điển hình là "Basel quy định gì, NHNN nội luật hoá ra sao, tác động lên ALM/Treasury thế nào". Với nghĩa vụ tuân thủ tại VN, quy định NHNN (T1) là căn cứ, Basel chỉ là tham chiếu.
- Người đọc wiki đọc tiếng Việt và quen thuật ngữ chuyên ngành tiếng Anh.

## Domain chính
Domain là metadata (`domains: [primary, …]`), không phải thư mục. Enum chính thức nằm trong `03_meta/taxonomy.md`.

| Code | Domain | Phạm vi |
|---|---|---|
| `macro` | Macroeconomic | Chính sách tiền tệ, lãi suất, lạm phát, thanh khoản hệ thống |
| `product` | Financial Product | Fixed income, swap, derivatives, sản phẩm tiền gửi/cho vay |
| `alm` | ALM | IRRBB, thanh khoản (LCR/NSFR), FTP, hành vi khách hàng, balance sheet management |
| `basel` | Basel | Chuẩn mực BCBS: vốn, thanh khoản, IRRBB, đòn bẩy |
| `vn-reg` | VN Regulator | Luật TCTD, Nghị định, Thông tư NHNN (TT14/2025, TT50/2026, TT83/2025) |

Nguồn được xếp tier (chỉ gán cho source note; synthesis của LLM không có tier): **T1** văn bản pháp quy VN · **T2** chuẩn mực BCBS final · **T3** ấn phẩm chính thức (IMF, báo cáo ALM ngân hàng) · **T4** sách/tài liệu phương pháp (Choudhry, Bindseil, Bardaeva, Lubinska, VAB FTP…) · **T5** clippings. Tiến độ ingest từng nguồn: `03_meta/sources.yaml` (nguồn sự thật) và bảng tóm tắt cuối `02_wiki/overview.md`.

Đặc tả đầy đủ nằm ở `alm-wiki-architecture-v2.md`. File này chỉ chứa quy tắc bắt buộc. `alm-wiki-llm-architecture.md` là bản v1 đã bị v2 thay thế, chỉ giữ để tham khảo, không dùng làm đặc tả.

## Bản đồ thư mục

| Path | Vai trò | LLM được ghi? |
|---|---|---|
| `01_sources/` | RAW: pdf/docx gốc + md do marker convert + `_meta.json` | **KHÔNG BAO GIỜ** |
| `02_wiki/sources/` | Source note: tóm tắt + key claims có trích nguyên văn + locator | Có |
| `02_wiki/{concepts,metrics,instruments,models,regulations,entities,syntheses}/` | Node tri thức | Có (theo write policy) |
| `02_wiki/index.md` · `log.md` · `overview.md` | Catalog · nhật ký append-only · bản đồ | Có |
| `02_wiki/domains/` | Trang tóm tắt mỗi domain (`domain-<code>`, `type: nav`, gồm mọi node có domain đó, không chia theo primary); claim chép từ node kèm citation | Có |
| `03_meta/sources.yaml` | Source registry (id, path, hash, tier, units) | Có |
| `03_meta/taxonomy.md` | Enum (domain, type, status, relation, tier) | Chỉ khi user duyệt |
| `03_meta/templates/` · `03_meta/views/` | Template node · dashboard Dataview | Chỉ khi user duyệt |
| `tools/registry.py` | show / read unit / check trùng / mark done / add entry vào registry | Chỉ khi user duyệt (sửa code) |
| `tools/units.py` · `tools/lint.py` · `tools/citations.py` | Tách unit + hash · lint deterministic (kể cả trích dẫn ↔ raw) · ghép câu node ↔ claim nguồn | Chỉ khi user duyệt (sửa code) |
| `tools/check_math.py` | Kiểm tra công thức LaTeX/KaTeX (vị trí `$$`, ngoặc, `\left/\right`, `%`/`$` trong math, double subscript, ký tự đặc biệt trong `\text{}`, `$` lẻ trong ô bảng). `lint.py` import nên ERROR ở đây là ERROR của lint; chạy riêng với `--info` để xem gợi ý văn phong | Chỉ khi user duyệt (sửa code) |
| `tools/audit_vault.py` | Script phụ chỉ đọc, được `/lint` chạy ở bước kiểm tra bổ sung: thống kê type/maturity, note ngắn, relation thiếu `cite` | Chỉ khi user duyệt (sửa code) |
| `tools/` (còn lại) | Script phụ ngoài quy trình skill: `update_relations.py` (one-off, dữ liệu hard-code) | Chỉ khi user duyệt (sửa code) |
| `scratch/` | Script/kết quả tạm khi kiểm trích dẫn; bị `.gitignore` | Có |

## Quy tắc cốt lõi
1. `01_sources/` bất biến. Không sửa, move, xoá, hay tạo file trong đó bằng **bất kỳ** tool nào, kể cả Bash/PowerShell. Rule `Edit(/01_sources/**)` trong `.claude/settings.json` chặn các file tool và các lệnh shell được nhận diện (`sed`, `tee`, redirect `>`), nhưng không chặn script Python/Node tự mở file. Script trong `tools/` chỉ được đọc raw.
2. Mọi factual claim trong node phải có citation `[[src-…#^block-id]]` trỏ về source note.
3. Source note chỉ ghi điều nguồn nói, kèm trích nguyên văn và locator. Diễn giải của LLM không bao giờ được coi là nguồn.
4. Không bịa nguồn, locator, số liệu hay block-id. Thiếu nguồn thì ghi `[cần nguồn]`.
5. Fact phụ thuộc thời gian phải có `valid_from`/`valid_to` (hiệu lực) hoặc `as_of` (ngày số liệu).
6. Không xoá node, không xoá lịch sử. Thay vào đó đặt `status: superseded|retired` + `valid_to` + `superseded_by`.
7. Mâu thuẫn được ghi bằng callout `> [!conflict]`, giữ cả hai claim và nguồn. Không overwrite, không áp "newer wins".
8. Một khái niệm chỉ có một node. Domain là metadata (`domains: [primary, …]`).
9. Thư mục wiki tổ chức theo node type, không theo domain.
10. Query đọc wiki trước, chỉ quay về raw để verify.
11. Node `reviewed`/`canonical`: không sửa thân bài, chỉ ghi đề xuất vào mục `## Đề xuất cập nhật`.
12. Basel `doc_status: consultative` không được trích như final standard.
13. Dòng đề xuất (`## Đề xuất cập nhật`) và dòng đánh dấu của ingest (`## Bất định` trong synthesis) đã xử lý thì **xoá khỏi node**: nội dung đã được thay vào thân bài, dấu vết ghi ở `log.md`. Không giữ dòng kèm `→ đã áp dụng`/`→ đã rà`. Mục không còn dòng nào thì ghi `*Chưa có nội dung cần cập nhật.*` Quy tắc 6 ("không xoá lịch sử") áp cho node và trạng thái hiệu lực, không áp cho các dòng này.

## Write policy

| LLM tự làm | LLM đề xuất, user duyệt | Cấm |
|---|---|---|
| Source note; node `draft`; link; relations; conflict callout; synthesis draft; index, overview, log, sources.yaml | Sửa node `reviewed`/`canonical`; diễn giải quy định; phương pháp model và giả định; đánh dấu `superseded`/`retired`; sửa taxonomy, template, tools | Ghi vào `01_sources/`; xoá node hoặc lịch sử; xoá conflict; bịa nguồn, locator hay số liệu |

## Chọn node type
Hỏi lần lượt, dừng ở câu đầu tiên trả lời "có":
1. Là văn bản/chuẩn mực có hiệu lực? → `regulation`
2. Là tổ chức, đồng tiền, chỉ số? → `entity`
3. Là hợp đồng/sản phẩm giao dịch được? → `instrument`
4. Là đại lượng đo được, có công thức? → `metric`
5. Là phương pháp định lượng cần giả định/calibration? → `model`
6. Còn lại → `concept`

Mọi đại lượng trong công thức của một metric (tử số, mẫu số, tổng phụ, nhóm cấu phần) cũng là `metric`, vì đều phải được quản trị, ví dụ `hqla`, `cash-outflows`, `level-1-assets`, `asf-*`, `rsf-*`. Tham số do cơ quan quản lý ấn định (run-off rate, hệ số ASF/RSF, haircut) thì không phải metric. Chi tiết và ví dụ nằm ở `alm-wiki-architecture-v2.md` mục C.1.

Không có node "definition" (định nghĩa là mục đầu của node) và không có node "relationship" (quan hệ khai báo trong frontmatter `relations`). Câu hỏi hoặc phân tích được lưu lại thì dùng type `synthesis`.

## Frontmatter và đặt tên
- Tên file = ID, kebab-case tiếng Anh, duy nhất toàn vault, không chứa domain hay type. Source note có tiền tố `src-`.
- Field bắt buộc và enum: xem `03_meta/taxonomy.md`. Template theo type nằm ở `03_meta/templates/`.
- `aliases` có cả tên tiếng Việt và tiếng Anh.
- Link nội bộ dùng `[[id]]`. Obsidian không resolve link theo alias, nên không link bằng alias.

## Citation và provenance
- Trong node: `… claim … [[src-bcbs-lcr#^lcr40-1]]`.
- Công thức display: `$$…$$` đứng riêng một dòng (hoặc một khối nhiều dòng), citation đặt ở **dòng dưới**, cùng thụt lề. Không viết citation ngay sau `$$` trên cùng dòng, không đặt `[[…]]` bên trong `\text{}`. `lint.py` (qua `tools/check_math.py`) báo ERROR nếu vi phạm.
- Trong source note, dưới heading của unit:
  ```
  - Diễn đạt ngắn bằng tiếng Việt.
    > "Trích nguyên văn từ raw."
    > — LCR40.1 ^lcr40-1
  ```
- Block-id có dạng `^<unit>-<số>`, chỉ dùng chữ thường, số và gạch ngang.
- Chuỗi truy ngược: node → source note → raw md (grep locator) → pdf (`_meta.json` page_id).

## Ngôn ngữ
Nội dung viết tiếng Việt, giữ thuật ngữ chuyên ngành tiếng Anh (duration, EVE, run-off rate, …). Trích nguyên văn giữ đúng ngôn ngữ gốc. Quy chuẩn văn phong chi tiết nằm ở `.claude/skills/alm-writing-style/SKILL.md`. **Trong vault này chỉ dùng `alm-writing-style`**: không gọi skill văn phong toàn cục (`anthropic-skills:writing-style` hay tương tự), kể cả khi mô tả của nó khớp yêu cầu, vì hai bộ rule có hệ ID riêng và dễ áp lẫn.

## Operation (skill)

| Lệnh | Khi nào |
|---|---|
| `/register <path>` | Thêm nguồn mới vào `01_sources/` |
| `/ingest <source_id> [unit]` | Biên dịch một unit thành source note + node (mỗi lần một unit, user tham gia) |
| `/query <câu hỏi>` | Hỏi đáp một câu, dựa trên wiki, có thể lưu thành synthesis (`origin: query`) |
| `/research <chủ đề> [bộ câu hỏi]` | Nghiên cứu một vấn đề phức tạp hoặc một bộ câu hỏi (vd 20 câu IRRBB): bản đồ phủ câu hỏi ↔ node, chỉ ra lỗ hổng nguồn, viết synthesis `origin: research` theo cụm câu hỏi. Chỉ chạy khi user gọi |
| `/lint` | Kiểm tra sức khoẻ wiki (`python tools/lint.py`, đã gồm kiểm tra công thức + kiểm tra ngữ nghĩa + script phụ `audit_vault.py`) |
| `/alm-writing-style <node-id>` | Rà văn phong một node. Skill thụ động: không tự kích hoạt, được ingest/query/lint đọc trước khi viết |

Nguồn lớn (BaselFramework.md 3,6 MB, sách 2–3 MB) **không bao giờ đọc nguyên file**. Chỉ đọc theo line range của unit trong `sources.yaml`, hoặc grep locator.

Sau mọi thay đổi trong `02_wiki/`: chạy `python tools/lint.py`, sửa hết ERROR, append `log.md`.

## Lệnh thường dùng
Repo không có build hay test suite. Các script cần Python 3.12+ và PyYAML, chạy từ thư mục gốc vault.

```bash
python tools/lint.py [--json] [--today YYYY-MM-DD]     # lint toàn vault; exit 1 nếu có ERROR; --today để test kiểm tra hiệu lực
python tools/citations.py --numbers | --node <id> | --uncited   # rà ngữ nghĩa: câu trong node ↔ claim được cite; câu có số thiếu citation
python tools/registry.py show <source_id>              # metadata + units + trạng thái
python tools/registry.py read <source_id> <unit> [--from N --to M] [--raw]   # đọc unit, giữ số dòng gốc, bỏ URL (--raw giữ URL)
python tools/registry.py check "<path>"                # path/hash đã đăng ký chưa
python tools/registry.py mark <source_id> <unit>... [--status done|skipped|pending]   # mặc định done
python tools/registry.py add --id … --path … --tier … --domains … --issuer … --preset vn|basel|chapter|book|auto [--chunk N] [--level N] [--add LINE:ID] [--dir] [--dry-run]
python tools/units.py "<path>" --preset … [--chunk N] [--level N] [--pattern REGEX] [--add LINE:ID] [--dir]   # xem trước cách tách unit
```
Muốn kiểm thử thay đổi của tool hoặc skill: chạy trên bản copy vault trong scratchpad, cố tình cài lỗi, rồi chạy `python tools/lint.py --wiki <copy>/02_wiki --meta <copy>/03_meta --root <copy>` để xác nhận lỗi bị bắt (thiếu `--meta`/`--root` thì lint vẫn đọc taxonomy, registry và raw của vault thật). Bộ eval nằm ở `.claude/skills/<skill>/evals/evals.json` (register, ingest, lint; `query` chưa có).

## Kiến trúc: những điểm phải đọc nhiều file mới thấy
- **Luồng dữ liệu:** `01_sources/*.md` → `/register` (entry, hash, unit theo line range trong `sources.yaml`) → `/ingest` (source note có `^block-id` → node cite `[[src#^id]]` → index, overview, log, registry) → `/lint` → `/query`.
- **`03_meta/taxonomy.md` vừa là tài liệu vừa là cấu hình:** `lint.py` đọc khối ` ```yaml taxonomy ` trong file để lấy enum và field bắt buộc.
- **Provenance được kiểm tra bằng máy:** `lint.py` kiểm tra block-ref tồn tại, kiểm tra mọi dòng `> "…"` trong source note là chuỗi con của raw (`raw:` trong frontmatter, sau khi chuẩn hoá link, footnote, emphasis, list marker; `…` đánh dấu phần lược bỏ), và kiểm tra mọi path trong registry. Vì vậy trích dẫn phải copy đúng chữ từ `registry.py read`.
- **`01_sources/` bị `.gitignore`** (dung lượng lớn, có tài liệu bản quyền): raw chỉ tồn tại local, git không có bản lưu nào. Vì vậy lint kiểm tra trích dẫn chỉ chạy được trên máy có raw.
- **`lines`, `sha256`, `id` của unit do tool sinh ra, không sửa tay.** Cần khác thì chạy lại tool với tham số khác. `notes`, `conversion`, `domains` thì được sửa tay.
- **Lint deterministic không biết node nói đúng hay sai**, chỉ biết citation tồn tại. Lệch số liệu, phạm vi, "may" so với "must" phải rà bằng `citations.py` cộng LLM. Dòng bảng tham số cũng cần citation riêng, nếu không sẽ lọt khỏi bước rà này.
- Quy trình chi tiết của từng thao tác nằm trong `.claude/skills/{register,ingest,query,lint}/SKILL.md`.
