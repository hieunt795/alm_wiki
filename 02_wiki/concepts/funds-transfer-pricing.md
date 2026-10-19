---
title: "Funds Transfer Pricing (FTP)"
aliases: [Funds Transfer Pricing, FTP, Định giá điều chuyển vốn nội bộ, Cơ chế định giá điều chuyển vốn nội bộ, Giá điều chuyển vốn nội bộ]
type: concept
domains: [alm, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]", "[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]"]
relations: []
tags: [ftp, treasury, transfer-pricing, commercial-margin, matched-maturity, concept]
updated: 2026-10-19
reviewed:
---

## Ý chính

- FTP là hệ thống giá điều chuyển nội bộ giữa Treasury và các đơn vị kinh doanh (BU). Khoản chuyển vốn nội bộ giữa hai bên được thanh toán trên cơ sở trùng khớp kỳ hạn theo một đường cong FTP được chọn phù hợp [[src-choudhry-principles-banking#^choudhry-ftp-6]].
- Theo Choudhry, FTP không phải là phòng ngừa rủi ro ra bên ngoài, cũng không phải là điều chuyển vốn nội bộ; FTP là chuyển giao rủi ro nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-10]]. Chi tiết cơ chế chuyển giao: [[internal-risk-transfer]].
- Giá điều chuyển là giá giả định, dựa trên một giao dịch phòng ngừa danh nghĩa (notional hedge) cho giao dịch khách hàng [[src-choudhry-principles-banking#^choudhry-ftp-5]].
- Hệ thống FTP là ranh giới giữa hai nguồn lợi nhuận [[src-choudhry-principles-banking#^choudhry-ftp-3]]:
  - **maturity transformation**: lợi nhuận rủi ro từ chênh lệch kỳ hạn, có chủ đích hoặc không, giữa tài sản và nợ [[src-choudhry-principles-banking#^choudhry-ftp-1]];
  - **customer franchise**: năng lực bán sản phẩm cho khách hàng ở lãi suất khác lãi suất thị trường vốn [[src-choudhry-principles-banking#^choudhry-ftp-2]].
- Choudhry gọi việc tách maturity transformation "rủi ro" khỏi customer franchise "phi rủi ro" là một hệ quả quan trọng của hệ thống FTP [[src-choudhry-principles-banking#^choudhry-ftp-13]].
- Phân tích chi tiết theo câu hỏi: [[ftp-nature-and-balance-sheet-management]], [[ftp-risk-and-cost-components]], [[ftp-curve-construction-methodology]], [[ftp-portfolio-and-bucket-allocation]], [[ftp-final-rate-determination]], [[ftp-cost-benefit-allocation-principles]], [[ftp-economic-cost-and-incentive-validation]], [[ftp-balance-sheet-optimization]].

## Cơ chế & drivers

- **Commercial margin**: chênh lệch giữa lãi suất khách hàng bên ngoài và lãi suất FTP nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-7]]. Lãi suất FTP được cố định trên cơ sở trùng khớp (cùng kỳ hạn, cùng đồng tiền, cùng cơ sở lãi suất) với lãi suất khách hàng. Vì vậy commercial margin không đổi khi đường cong FTP hoặc tỷ giá biến động sau đó [[src-choudhry-principles-banking#^choudhry-ftp-8]].
- **Đo lường BU**: dùng lãi suất thị trường vốn trùng khớp kỳ hạn làm giá điều chuyển cho phép đo năng lực tạo lợi nhuận từ customer franchise của từng BU [[src-choudhry-principles-banking#^choudhry-ftp-4]]. Giá giao dịch khách hàng và commercial margin không được trợ cấp chéo bằng P&L kỳ vọng chưa thực hiện từ các vị thế chênh lệch kỳ hạn [[src-choudhry-principles-banking#^choudhry-ftp-9]].
- **Matched-maturity principle**: Choudhry nêu đây là thuộc tính thứ hai của hệ thống FTP [[src-choudhry-principles-banking#^choudhry-ftp-11]].
- **Marginality principle**: chi phí đã phát sinh của nguồn vốn hiện có không liên quan tới định giá khoản vay mới; khoản vay mới và tiền gửi mới đều được định giá theo chi phí/lợi ích giả định của điều kiện phòng ngừa đang áp dụng [[src-choudhry-principles-banking#^choudhry-ftp-12]].
- **Liquidity FTP**: FTP lãi suất cổ điển được mở rộng thêm một lớp gọi là liquidity FTP [[src-choudhry-principles-banking#^choudhry-ftp-14]]. BU tạo ra tài sản gây áp lực thanh khoản phải chịu chi phí tìm nguồn thanh khoản đó qua phí FTP [[src-choudhry-principles-banking#^choudhry-ftp-15]]. Chi tiết: [[liquidity-transfer-pricing]].
- **Nội dung chi phí (VAB)**: lãi suất FTP phải phản ánh đủ chi phí vốn đầu vào (lãi suất huy động, chi phí bảo hiểm tiền gửi, chi phí quản lý huy động), chi phí quản lý rủi ro thanh khoản và rủi ro lãi suất [[src-vab-ftp#^vab-ftp-5]]. Phương pháp VOF/COF: [[ftp-pricing-methodology]].
- **Cấu phần lãi suất (nguồn T5)**: FTP Rate = Base Rate + Liquidity Spread + Credit Spread + Optionality Cost [[src-ftp-transmission-analysis#^ftp-trans-3]].
- **Kênh truyền dẫn (nguồn T5)**: FTP tác động đồng thời lên rủi ro thanh khoản, rủi ro lãi suất và rủi ro tín dụng qua các kênh riêng nhưng tương tác nhau [[src-ftp-transmission-analysis#^ftp-trans-2]]. Với IRRBB, FTP tách rủi ro khỏi BU và chuyển toàn bộ về ALM để quản lý tập trung [[src-ftp-transmission-analysis#^ftp-trans-9]]. Chi tiết: [[ftp-transmission-mechanism]].

## Phụ thuộc regime

- Chênh lệch chi phí huy động vốn của ngân hàng nới rộng đã dẫn tới việc bổ sung lớp liquidity FTP vào FTP lãi suất cổ điển [[src-choudhry-principles-banking#^choudhry-ftp-14]].
- Nguồn T5 mô tả cách điều chỉnh theo trạng thái thanh khoản: LCR thấp thì tăng spread cho tenor ngắn (O/N đến 30 ngày); NSFR thấp thì tăng spread cho tenor dài (6M đến 2Y trở lên) [[src-ftp-transmission-analysis#^ftp-trans-8]].

## Góc nhìn theo domain

- **ALM**: nguồn T5 coi FTP là hệ thống điều khiển trung tâm (unified control mechanism) trong quản trị bảng cân đối [[src-ftp-transmission-analysis#^ftp-trans-1]]. VAB nêu các mục tiêu tổng thể của dự án FTP: quản lý lợi nhuận, quản lý bảng cân đối, quản lý rủi ro thanh khoản và rủi ro lãi suất trên sổ ngân hàng, định hướng hoạt động kinh doanh [[src-vab-ftp#^vab-ftp-2]].
- **Product**: commercial margin của giao dịch khách hàng giữ nguyên trước biến động sau đó của đường cong FTP và tỷ giá [[src-choudhry-principles-banking#^choudhry-ftp-8]].
- **Basel / VN**: VAB đặt mục tiêu hướng dẫn định giá điều chuyển vốn tuân thủ quy định pháp luật và phù hợp tiêu chuẩn Basel [[src-vab-ftp#^vab-ftp-3]]. Wiki chưa có chuẩn mực BCBS hay văn bản NHNN quy định trực tiếp về FTP [cần nguồn]. TT83/2025 có hai yêu cầu gián tiếp: đưa chi phí thanh khoản vào định giá vốn nội bộ [[src-tt83-2025-nhnn#^d45-1b]], và có nguyên tắc xác định chi phí bù đắp rủi ro tín dụng trong tính lãi suất, định giá sản phẩm tín dụng theo mức rủi ro của khách hàng [[src-tt83-2025-nhnn#^d26-2c]]. Xem [[credit-risk-management]].

## Bằng chứng thực nghiệm

Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở

- Công thức cấu phần và kênh truyền dẫn ở trên dựa vào nguồn T5 (`src-ftp-transmission-analysis`), chưa đối chiếu với nguồn T4 hoặc cao hơn.
- [[cost-of-funds]] (COF, [[src-vab-ftp#^vab-ftp-7]]) đang là stub; hoàn thiện bằng `/ingest --node cost-of-funds`.
- Chưa có nguồn NHNN về yêu cầu đối với hệ thống FTP tại VN.
