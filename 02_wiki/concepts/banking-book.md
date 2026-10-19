---
title: "Banking Book"
aliases: [Banking Book, Sổ ngân hàng, Trading Book, Sổ kinh doanh, Phân loại sổ ngân hàng và sổ kinh doanh]
type: concept
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-tata-bank-alm]]", "[[src-bcbs-irrbb-2016]]"]
relations: []
tags: [irrbb, banking-book, trading-book]
updated: 2026-10-19
reviewed:
---

## Ý chính
Sổ ngân hàng và sổ kinh doanh là hai danh mục ghi nhận trạng thái giao dịch của ngân hàng. Cách phân loại này quyết định một vị thế chịu IRRBB hay rủi ro lãi suất thuộc rủi ro thị trường:
- IRRBB là rủi ro do lãi suất biến động bất lợi tác động tới trạng thái sổ ngân hàng [[src-tt83-2025-nhnn#^d3-22]].
- Rủi ro lãi suất thuộc rủi ro thị trường gắn với công cụ trên sổ kinh doanh [[src-tt83-2025-nhnn#^d3-15a]]. Trạng thái sổ kinh doanh chịu hạn mức và báo cáo hằng ngày của [[market-risk-management]] [[src-tt83-2025-nhnn#^d35-2]] [[src-tt83-2025-nhnn#^d37-1]].

## Cơ chế & drivers
**Phân loại theo TT83/2025:**

| Sổ | Gồm trạng thái của | Nguồn |
|---|---|---|
| Sổ kinh doanh | Giao dịch tự doanh; bảo lãnh phát hành công cụ tài chính; phái sinh phòng ngừa rủi ro cho giao dịch tự doanh; mua bán ngoại tệ, vàng, tài sản tài chính phục vụ khách hàng, đối tác và giao dịch đối ứng | [[src-tt83-2025-nhnn#^d3-32]] |
| Sổ ngân hàng | Repo và reverse repo; phái sinh phòng ngừa cho khoản mục báo cáo tình hình tài chính (kể cả ngoại bảng), trừ giao dịch đã vào sổ kinh doanh; mua bán tài sản tài chính để dự trữ thanh khoản; mọi giao dịch còn lại không thuộc sổ kinh doanh | [[src-tt83-2025-nhnn#^d3-33]] |

Giao dịch tự doanh là giao dịch mua, bán, trao đổi trong thời hạn không quá một năm, để thu lợi từ chênh lệch giá thị trường [[src-tt83-2025-nhnn#^d3-32]].

*Diễn giải:* sổ ngân hàng được định nghĩa theo phần dư ("các giao dịch còn lại") [[src-tt83-2025-nhnn#^d3-33]]. Vì vậy ranh giới thực tế do danh sách sổ kinh doanh quyết định.

**Tài liệu phương pháp (Tata):**
- Sổ ngân hàng gồm mọi giao dịch và vị thế dài hạn gắn với hoạt động khách hàng và việc tài trợ cho chúng, kể cả vốn chủ sở hữu [[src-tata-bank-alm#^tata-scope-1]].
- Sổ kinh doanh gồm vị thế nắm giữ để bán lại ngắn hạn, hưởng lợi từ biến động giá hoặc arbitrage [[src-tata-bank-alm#^tata-scope-2]].

## Phụ thuộc regime
Không ghi nhận trong nguồn đã ingest.

## Góc nhìn theo domain
- **Basel**: d368 định nghĩa IRRBB là rủi ro với vốn và thu nhập do lãi suất biến động bất lợi tác động tới các vị thế sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u02-1]]. Cấu phần danh mục sổ ngân hàng chịu IRRBB: [[irrbb-balance-sheet-portfolios]].
- **VN**:
  - TT83/2025 đưa giao dịch mua bán tài sản tài chính để dự trữ thanh khoản vào sổ ngân hàng [[src-tt83-2025-nhnn#^d3-33]].
  - *Diễn giải:* như vậy danh mục HQLA nắm giữ vì mục đích thanh khoản ([[hqla]]) chịu IRRBB, không chịu rủi ro thị trường. Xem [[irrbb-liquidity-hqla-and-ftp-interaction]].
- **ALM**: *Diễn giải:* phái sinh phòng ngừa (ví dụ IRS) cho khoản mục báo cáo tình hình tài chính nằm trong sổ ngân hàng [[src-tt83-2025-nhnn#^d3-33]], nên dòng tiền của chúng vào bảng ΔEVE theo PL5 ([[economic-value-of-equity]]).

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Tiêu chí chuyển sổ (reclassification) giữa sổ kinh doanh và sổ ngân hàng: TT83 C1 không nêu [cần nguồn].
