---
title: "Regulatory Internal Risk Transfer"
aliases: [Regulatory Internal Risk Transfer, IRT, Internal risk transfer RBC25, GIRR IRT, Chuyển giao rủi ro nội bộ giữa các sổ]
type: concept
domains: [basel, alm]
status: active
maturity: draft
valid_from: 2023-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-framework]]"]
relations: []
tags: [banking-book, trading-book, irrbb, market-risk, capital]
updated: 2026-10-19
reviewed:
---

## Ý chính
Internal risk transfer (IRT) theo RBC25 là bản ghi nội bộ về việc chuyển rủi ro trong banking book, giữa banking book và trading book, hoặc giữa các desk trong trading book [[src-bcbs-framework#^rbc25-18]]. Xử lý IRT chỉ áp dụng cho chuyển rủi ro qua giao dịch phái sinh nội bộ; chuyển chứng khoán giữa hai sổ là chuyển sổ, theo quy định riêng [[src-bcbs-framework#^rbc25-16-faq1]]. Phiên bản RBC25 đã ingest có hiệu lực từ 01/01/2023 [[src-bcbs-framework#^rbc25-0]].

*Diễn giải:* khái niệm này khác [[internal-risk-transfer]] (chuyển rủi ro từ đơn vị kinh doanh sang Treasury qua FTP). IRT theo RBC25 là quy tắc công nhận vốn cho giao dịch nội bộ giữa hai sổ quy định.

## Cơ chế & drivers
**Công nhận vốn theo chiều chuyển:**

| Chiều / loại rủi ro | Điều kiện công nhận vốn | Nguồn |
|---|---|---|
| Trading book → banking book | Không được công nhận | [[src-bcbs-framework#^rbc25-19]] |
| Banking book → trading book, rủi ro tín dụng / cổ phiếu | Trading book phải có hợp đồng phòng ngừa bên ngoài với bên bảo vệ đủ điều kiện, khớp chính xác IRT (được gộp nhiều giao dịch, nhiều đối tác) | [[src-bcbs-framework#^rbc25-21]] |
| Banking book → trading book, rủi ro lãi suất chung (GIRR) | Lập hồ sơ rủi ro được phòng ngừa và nguồn rủi ro; thực hiện với desk IRT chuyên trách được cơ quan giám sát phê duyệt; tính vốn trading book độc lập cho desk đó | [[src-bcbs-framework#^rbc25-25]] |
| Giữa các trading desk trong phạm vi vốn rủi ro thị trường | Thường được công nhận; với desk IRT chỉ khi đáp ứng RBC25.25–25.27 | [[src-bcbs-framework#^rbc25-28]] |
| Danh mục CVA ↔ trading book | Lập hồ sơ rủi ro CVA được phòng ngừa và nguồn rủi ro | [[src-bcbs-framework#^rbc25-31]] |

**Hệ quả khi IRT tín dụng / cổ phiếu đạt hoặc không đạt điều kiện** [[src-bcbs-framework#^rbc25-22]]:
- Đạt: exposure banking book được coi là đã phòng ngừa; chân trading book của IRT và hợp đồng bên ngoài đều tính vốn rủi ro thị trường.
- Không đạt: exposure không được coi là phòng ngừa; hợp đồng bên ngoài tính đủ vào vốn rủi ro thị trường, chân trading book của IRT bị loại.
- Phòng ngừa quá mức tạo vị thế short trong banking book; vị thế này phải tính vốn theo quy tắc rủi ro thị trường nếu chưa tính theo quy tắc banking book [[src-bcbs-framework#^rbc25-24]].

**Desk IRT cho GIRR:**
- Không cần trader hay tài khoản kinh doanh; chỉ áp kiểm định PLA và backtesting (MAR32), không áp tiêu chí định tính MAR12.4 [[src-bcbs-framework#^rbc25-25-faq1]].
- Không giữ vị thế trading book nào ngoài GIRR IRT giữa hai sổ và hợp đồng phòng ngừa bên ngoài đủ điều kiện [[src-bcbs-framework#^rbc25-25-faq1]].
- Mua hợp đồng phòng ngừa trực tiếp từ thị trường, hoặc qua desk khác làm đại lý nếu GIRR IRT với desk đó khớp chính xác hợp đồng thị trường [[src-bcbs-framework#^rbc25-27]].
- Chân trading book của IRT phải đáp ứng cùng yêu cầu như công cụ trading book giao dịch với bên ngoài [[src-bcbs-framework#^rbc25-29]].

## Phụ thuộc regime
Không ghi nhận trong nguồn đã ingest.

## Góc nhìn theo domain
- **Basel**: khi GIRR IRT đáp ứng RBC25.25, chân banking book của IRT phải được đưa vào phép đo rủi ro lãi suất của banking book cho mục đích vốn [[src-bcbs-framework#^rbc25-26]]. Tách phái sinh nhúng khỏi nợ phát hành từ banking book không cần IRT [[src-bcbs-framework#^rbc25-9-faq2]].
- **ALM**: *Diễn giải:*
  - Khi đáp ứng RBC25.25–25.26, ALM có thể phòng ngừa IRRBB qua desk nội bộ thay vì ký phái sinh trực tiếp từ banking book, và chân banking book của IRT được tính vào đo lường [[economic-value-of-equity]] và [[net-interest-income-sensitivity]].
  - Nếu không có desk IRT được phê duyệt, phòng ngừa IRRBB phải dùng phái sinh ghi thẳng vào banking book. Xem [[structural-hedging]].
- **VN**: TT83/2025 xếp phái sinh phòng ngừa cho khoản mục báo cáo tình hình tài chính vào sổ ngân hàng [[src-tt83-2025-nhnn#^d3-33]]; chưa ghi nhận quy định IRT giữa hai sổ trong nguồn VN đã ingest [cần nguồn].

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- d368 có yêu cầu riêng về phòng ngừa nội bộ cho IRRBB không, và có khớp với RBC25.25–25.26 không: chưa đối chiếu.
- NHNN có cơ chế tương đương desk IRT được phê duyệt không [cần nguồn].
