# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# ALM Wiki — Constitution

## Mission
Wiki tri thức cá nhân cho 5 domain: **Macroeconomic, Financial Product, ALM, Basel, VN Regulator**. Vận hành theo pattern LLM Wiki của Karpathy.
- LLM là *knowledge compiler / maintainer*: đọc nguồn, biên dịch thành node markdown liên kết, duy trì theo thời gian.
- LLM **không phải** source of truth.
- Người dùng chọn nguồn, đặt câu hỏi và review.

Đặc tả đầy đủ nằm ở `alm-wiki-architecture-v2.md`. File này chỉ chứa quy tắc bắt buộc. `alm-wiki-llm-architecture.md` là bản v1 đã bị v2 thay thế, chỉ giữ để tham khảo, không dùng làm đặc tả.

## Bản đồ thư mục

| Path | Vai trò | LLM được ghi? |
|---|---|---|
| `01_sources/` | RAW: pdf/docx gốc + md do marker convert + `_meta.json` | **KHÔNG BAO GIỜ** |
| `02_wiki/sources/` | Source note: tóm tắt + key claims có trích nguyên văn + locator | Có |
| `02_wiki/{concepts,metrics,instruments,models,regulations,entities,syntheses}/` | Node tri thức | Có (theo write policy) |
| `02_wiki/index.md` · `log.md` · `overview.md` | Catalog · nhật ký append-only · bản đồ | Có |
| `03_meta/sources.yaml` | Source registry (id, path, hash, tier, units) | Có |
| `03_meta/taxonomy.md` | Enum (domain, type, status, relation, tier) | Chỉ khi user duyệt |
| `03_meta/templates/` · `03_meta/views/` | Template node · dashboard Dataview | Chỉ khi user duyệt |
| `tools/registry.py` | show / read unit / check trùng / mark done / add entry vào registry | Chỉ khi user duyệt (sửa code) |
| `tools/units.py` · `tools/lint.py` · `tools/citations.py` | Tách unit + hash · lint deterministic (kể cả trích dẫn ↔ raw) · ghép câu node ↔ claim nguồn | Chỉ khi user duyệt (sửa code) |

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
- Trong source note, dưới heading của unit:
  ```
  - Diễn đạt ngắn bằng tiếng Việt.
    > "Trích nguyên văn từ raw."
    > — LCR40.1 ^lcr40-1
  ```
- Block-id có dạng `^<unit>-<số>`, chỉ dùng chữ thường, số và gạch ngang.
- Chuỗi truy ngược: node → source note → raw md (grep locator) → pdf (`_meta.json` page_id).

## Ngôn ngữ
Nội dung viết tiếng Việt, giữ thuật ngữ chuyên ngành tiếng Anh (duration, EVE, run-off rate, …). Trích nguyên văn giữ đúng ngôn ngữ gốc. Quy chuẩn văn phong chi tiết nằm ở `.claude/skills/alm-writing-style/SKILL.md`.

## Operation (skill)

| Lệnh | Khi nào |
|---|---|
| `/register <path>` | Thêm nguồn mới vào `01_sources/` |
| `/ingest <source_id> [unit]` | Biên dịch một unit thành source note + node (mỗi lần một unit, user tham gia) |
| `/query <câu hỏi>` | Hỏi đáp dựa trên wiki, có thể lưu thành synthesis |
| `/lint` | Kiểm tra sức khoẻ wiki (`python tools/lint.py` + kiểm tra ngữ nghĩa) |
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
- **`lines`, `sha256`, `id` của unit do tool sinh ra, không sửa tay.** Cần khác thì chạy lại tool với tham số khác. `notes`, `conversion`, `domains` thì được sửa tay.
- **Lint deterministic không biết node nói đúng hay sai**, chỉ biết citation tồn tại. Lệch số liệu, phạm vi, "may" so với "must" phải rà bằng `citations.py` cộng LLM. Dòng bảng tham số cũng cần citation riêng, nếu không sẽ lọt khỏi bước rà này.
- Quy trình chi tiết của từng thao tác nằm trong `.claude/skills/{register,ingest,query,lint}/SKILL.md`.
