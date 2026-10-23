---
title: "Banking Book"
aliases: [Banking Book, Sổ ngân hàng, Trading Book, Sổ kinh doanh, Phân loại sổ ngân hàng và sổ kinh doanh]
type: concept
domains: [alm, vn-reg, basel]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-tt14-2025-nhnn]]", "[[src-tata-bank-alm]]", "[[src-bcbs-irrbb-2016]]", "[[src-bcbs-framework]]", "[[src-choudhry-principles-banking]]"]
relations: []
tags: [irrbb, banking-book, trading-book]
updated: 2026-10-23
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

**Phân loại theo TT14/2025 (tỷ lệ an toàn vốn):** Đ2.24 và Đ2.25 định nghĩa hai sổ theo cùng cấu trúc bốn nhóm với TT83/2025 [[src-tt14-2025-nhnn#^d2-24]] [[src-tt14-2025-nhnn#^d2-25]]. Sổ kinh doanh ghi nhận tự doanh (thời hạn không quá 01 năm), bảo lãnh phát hành, phái sinh phòng ngừa cho tự doanh, và giao dịch phục vụ khách hàng, đối tác cùng giao dịch đối ứng. Sổ ngân hàng ghi nhận repo và reverse repo, phái sinh phòng ngừa cho khoản mục Báo cáo tình hình tài chính trừ giao dịch đã vào sổ kinh doanh, mua bán tài sản tài chính để dự trữ khả năng thanh khoản, và các giao dịch còn lại [[src-tt14-2025-nhnn#^d2-23]] [[src-tt14-2025-nhnn#^d2-25]]. Trong TT14/2025, rủi ro lãi suất thuộc rủi ro thị trường là rủi ro đối với giấy tờ có giá, công cụ tài chính có lãi suất và phái sinh lãi suất trên sổ kinh doanh [[src-tt14-2025-nhnn#^d2-19a]]. Xem [[capital-adequacy-ratio]] cho mẫu số có $K_{MR}$ và [[market-risk-capital-requirement]].

**Chuyển sổ theo TT14/2025 Đ73.2:** ngân hàng chỉ được phân loại lại và chuyển khoản mục từ sổ kinh doanh sang sổ ngân hàng khi khoản mục không còn đáp ứng điều kiện, tiêu chí theo quy định nội bộ; ngân hàng không được chuyển công cụ tài chính từ sổ ngân hàng sang sổ kinh doanh [[src-tt14-2025-nhnn#^d73-2b]]. Quy định nội bộ phải nêu tiêu chí xác định khoản mục sổ kinh doanh và việc chuyển khoản mục giữa hai sổ [[src-tt14-2025-nhnn#^d73-1a]]. Kiểm toán nội bộ rà soát định kỳ khoản mục hai sổ [[src-tt14-2025-nhnn#^d73-1d]].

*Diễn giải:* sổ ngân hàng được định nghĩa theo phần dư ("các giao dịch còn lại") [[src-tt83-2025-nhnn#^d3-33]]. Vì vậy ranh giới thực tế do danh sách sổ kinh doanh quyết định.

**Phân loại theo Basel RBC25 (hiệu lực 01/01/2023)** [[src-bcbs-framework#^rbc25-0]]:
- Trading book gồm công cụ đáp ứng tiêu chí RBC25.2–25.13; mọi công cụ khác phải vào banking book [[src-bcbs-framework#^rbc25-1]].
- Công cụ nắm giữ để bán lại ngắn hạn, kiếm lời từ biến động giá ngắn hạn, khoá lợi nhuận arbitrage, hoặc phòng ngừa cho ba mục đích đó phải được chỉ định là trading book khi ghi nhận ban đầu [[src-bcbs-framework#^rbc25-5]]. Bán định kỳ tự nó không đủ để coi là nắm giữ để bán lại ngắn hạn [[src-bcbs-framework#^rbc25-5-faq1]].
- Điều kiện để vào trading book: không có trở ngại pháp lý khi bán hoặc phòng ngừa toàn bộ [[src-bcbs-framework#^rbc25-3]]; định giá hợp lý hằng ngày qua P&L [[src-bcbs-framework#^rbc25-4]].

| Danh sách | Nội dung chính | Nguồn |
|---|---|---|
| Bắt buộc vào trading book | Danh mục correlation trading; công cụ tạo net short tín dụng/cổ phiếu trong banking book; cam kết bảo lãnh phát hành chứng khoán | [[src-bcbs-framework#^rbc25-6]] |
| Bắt buộc vào banking book | Cổ phiếu chưa niêm yết; [[securitisation]] warehousing; bất động sản trực tiếp; tín dụng và cam kết cho vay bán lẻ, SME; quỹ không look-through được; quỹ phòng hộ; phái sinh trên các loại này; công cụ phòng ngừa chúng | [[src-bcbs-framework#^rbc25-8]] |
| Suy định vào trading book (presumptive list) | Tài sản/nợ kinh doanh theo kế toán; market-making; cổ phiếu niêm yết; repo phục vụ kinh doanh; quyền chọn và phái sinh nhúng liên quan tín dụng/cổ phiếu | [[src-bcbs-framework#^rbc25-9]] |
| Ngoại lệ của danh sách suy định | Repo vừa để quản lý thanh khoản vừa ghi nhận accrual | [[src-bcbs-framework#^rbc25-9]] |
| Lệch khỏi danh sách suy định | Phải có phê duyệt rõ ràng của cơ quan giám sát; không được duyệt thì vào trading book | [[src-bcbs-framework#^rbc25-10]] |

- Repo phục vụ kinh doanh là repo lập để market-making, khoá arbitrage hoặc tạo vị thế short [[src-bcbs-framework#^rbc25-9-faq1]]. Quyền chọn quản lý rủi ro ngoại hối của banking book chỉ được vào banking book khi cơ quan giám sát phê duyệt rõ ràng [[src-bcbs-framework#^rbc25-9-faq3]].
- Cơ quan giám sát có thể buộc chuyển công cụ giữa hai sổ nếu bằng chứng của ngân hàng chưa đủ, trừ công cụ thuộc danh sách bắt buộc [[src-bcbs-framework#^rbc25-11]]. Chính sách phân loại phải được lập hồ sơ và kiểm toán nội bộ tối thiểu hằng năm [[src-bcbs-framework#^rbc25-13]].

**Chuyển sổ (reassignment) theo RBC25:**

| Yếu tố | Yêu cầu | Nguồn |
|---|---|---|
| Nguyên tắc | Cấm chuyển sổ để arbitrage quy định; chỉ cho phép trong hoàn cảnh đặc biệt; biến động thị trường, thay đổi thanh khoản hay ý định kinh doanh không phải lý do hợp lệ | [[src-bcbs-framework#^rbc25-14]] |
| Lợi ích vốn | Không bao giờ được hưởng; phần vốn giảm do chuyển sổ thành phụ phí Pillar 1 có công bố, giảm dần khi vị thế đáo hạn | [[src-bcbs-framework#^rbc25-15]] |
| Phê duyệt | Senior management phê duyệt, cơ quan giám sát chấp thuận trước, công bố công khai; không đảo ngược được | [[src-bcbs-framework#^rbc25-16]] |
| Ngoại lệ tự động | Phân loại lại thành tài sản/nợ kinh doanh theo kế toán thì chuyển sang trading book không cần chấp thuận | [[src-bcbs-framework#^rbc25-16]] |
| Trading → banking | Luôn cần chấp thuận, kể cả khi phân loại kế toán đổi | [[src-bcbs-framework#^rbc25-16-faq2]] |
| Chính sách | Cập nhật tối thiểu hằng năm, gửi cơ quan giám sát | [[src-bcbs-framework#^rbc25-17]] |

Chuyển rủi ro giữa hai sổ qua phái sinh nội bộ không phải chuyển sổ mà theo quy tắc [[regulatory-internal-risk-transfer]] [[src-bcbs-framework#^rbc25-16-faq1]].

**Tài liệu phương pháp (Tata):**
- Sổ ngân hàng gồm mọi giao dịch và vị thế dài hạn gắn với hoạt động khách hàng và việc tài trợ cho chúng, kể cả vốn chủ sở hữu [[src-tata-bank-alm#^tata-scope-1]].
- Sổ kinh doanh gồm vị thế nắm giữ để bán lại ngắn hạn, hưởng lợi từ biến động giá hoặc arbitrage [[src-tata-bank-alm#^tata-scope-2]].

## Phụ thuộc regime
Không ghi nhận trong nguồn đã ingest.

## Góc nhìn theo domain
- **Basel vs VN**:

| Tiêu chí | Basel RBC25 | VN TT83/2025 | Nguồn |
|---|---|---|---|
| Cách xác định trading book | Theo mục đích nắm giữ (bán lại ngắn hạn, lợi nhuận giá ngắn hạn, arbitrage, phòng ngừa các vị thế đó) | Liệt kê loại giao dịch; tự doanh là giao dịch có thời hạn không quá một năm | [[src-bcbs-framework#^rbc25-5]] [[src-tt83-2025-nhnn#^d3-32]] |
| Repo | Repo phục vụ kinh doanh thuộc danh sách suy định trading book; repo quản lý thanh khoản ghi nhận accrual thì không | Repo và reverse repo thuộc sổ ngân hàng | [[src-bcbs-framework#^rbc25-9]] [[src-tt83-2025-nhnn#^d3-33]] |
| Phái sinh phòng ngừa | Phòng ngừa cho vị thế trading book thuộc trading book; phòng ngừa cho danh sách bắt buộc banking book thuộc banking book | Phòng ngừa khoản mục báo cáo tình hình tài chính thuộc sổ ngân hàng, trừ giao dịch đã vào sổ kinh doanh | [[src-bcbs-framework#^rbc25-5]] [[src-bcbs-framework#^rbc25-8]] [[src-tt83-2025-nhnn#^d3-33]] |
| Chuyển sổ | Hạn chế, cần chấp thuận, phụ phí vốn nếu giảm vốn | Chỉ chuyển từ sổ kinh doanh sang sổ ngân hàng khi hết đáp ứng tiêu chí nội bộ; cấm chuyển từ sổ ngân hàng sang sổ kinh doanh (TT14/2025 Đ73.2) | [[src-bcbs-framework#^rbc25-14]] [[src-tt14-2025-nhnn#^d73-2b]] |

- *Diễn giải:* khác biệt về repo là khác jurisdiction, không phải conflict. Theo TT83, mọi repo nằm trong sổ ngân hàng nên chịu IRRBB; theo RBC25, repo phục vụ kinh doanh mặc định thuộc trading book.
- **Basel**: d368 định nghĩa IRRBB là rủi ro với vốn và thu nhập do lãi suất biến động bất lợi tác động tới các vị thế sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u02-1]]. Cấu phần danh mục sổ ngân hàng chịu IRRBB: [[irrbb-balance-sheet-portfolios]].
- **VN**:
  - TT83/2025 đưa giao dịch mua bán tài sản tài chính để dự trữ thanh khoản vào sổ ngân hàng [[src-tt83-2025-nhnn#^d3-33]].
  - *Diễn giải:* như vậy danh mục HQLA nắm giữ vì mục đích thanh khoản ([[hqla]]) chịu IRRBB, không chịu rủi ro thị trường.
- **ALM**: *Diễn giải:* phái sinh phòng ngừa (ví dụ IRS) cho khoản mục báo cáo tình hình tài chính nằm trong sổ ngân hàng [[src-tt83-2025-nhnn#^d3-33]], nên dòng tiền của chúng vào bảng ΔEVE theo PL5 ([[economic-value-of-equity]]).
- **Banking Book Policy Statement (Choudhry, T4)**: giao dịch là trading khi dealer được phép mở vị thế tạo rủi ro thị trường theo thẩm quyền giao dịch; mọi giao dịch khác là non-trading [[src-choudhry-principles-banking#^choudhry-bbp-2]]. Banking Book gồm tài sản và nợ từ hoạt động non-trading [[src-choudhry-principles-banking#^choudhry-bbp-3]]. Chính sách xác định cách ghi nhận giao dịch vào sổ và khung kiểm soát mà Treasury dùng để quản lý các sổ [[src-choudhry-principles-banking#^choudhry-bbp-2]].
  - Rủi ro trong Banking Book gồm thị trường, thanh khoản, tín dụng, hoạt động, quy định; hạn mức gồm BPV, Interest Rate Gap Limits, Trader/Desk, Product, Credit [[src-choudhry-principles-banking#^choudhry-bbp-5]].
  - Phần lớn ngân hàng giao quyền sở hữu chính sách cho bộ phận "độc lập" như quản lý rủi ro middle office hoặc Product Control, thay vì Treasury [[src-choudhry-principles-banking#^choudhry-bbp-6]].
  - Ngân hàng mẫu trong RMF của Choudhry không có sổ kinh doanh [[src-choudhry-principles-banking#^choudhry-rmf-13]].

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Tiêu chí chuyển sổ (reclassification) giữa sổ kinh doanh và sổ ngân hàng: Basel đã có (RBC25.14–25.17, xem bảng trên); TT14/2025 Đ73.2 có quy tắc một chiều; TT83 C1 không nêu [cần nguồn]. Phụ lục IV của TT14 có thể bổ sung tiêu chí xác định khoản mục sổ kinh doanh [cần nguồn].
