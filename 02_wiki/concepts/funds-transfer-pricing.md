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
sources: ["[[src-choudhry-principles-banking]]", "[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]", "[[src-tata-bank-alm]]", "[[src-tt83-2025-nhnn]]", "[[src-bardaeva-alm]]"]
relations: []
tags: [ftp, treasury, transfer-pricing, commercial-margin, matched-maturity, concept]
updated: 2026-10-19
reviewed:
---

## Ý chính

- FTP là hệ thống giá điều chuyển nội bộ giữa Treasury và các đơn vị kinh doanh (BU). Khoản chuyển vốn nội bộ giữa hai bên được thanh toán trên cơ sở trùng khớp kỳ hạn theo một đường cong FTP được chọn phù hợp [[src-choudhry-principles-banking#^choudhry-ftp-6]].
- Tóm tắt Ch14 của Choudhry: Treasury (hoặc ALM) là 'clearing house' của vốn cho các mảng; lý tưởng FTP lấy từ internal yield curve theo kỳ hạn và là hàm của internal term liquidity premium [[src-choudhry-principles-banking#^choudhry-ftp-16]].
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

- **Rủi ro khí hậu (Tata, xem [[climate-risk]])**: sự kiện khí hậu có thể gây hành vi bất lợi của khách hàng (giảm trả nợ, rút tiền gửi, tăng sử dụng hạn mức); lý tưởng thì lãi suất FTP nên phạt nghiệp vụ làm tập trung các rủi ro này [[src-tata-bank-alm#^tata-fut-4]].
- **ALM là profit center hay cost center (Tata)**: FTP cho phép ALM thành profit center; rủi ro tài chính chuyển về profit center rủi ro lãi suất trong ALM, ALM quyết định có phòng ngừa qua thị trường không, lợi nhuận được phân phối lại định kỳ cho đơn vị kinh doanh. Nếu là cost center, ALM gom chi phí quản trị rủi ro lãi suất mà không nhằm kiếm lợi từ định vị thị trường, chi phí chuyển vào chi phí chung của đơn vị kinh doanh [[src-tata-bank-alm#^tata-prac-4]].
- **Truyền dẫn lãi suất NMD**: ngân hàng có FTP và replicating portfolio khác nhau thì truyền thay đổi lãi suất vào tiền gửi khác nhau [[src-tata-bank-alm#^tata-beh-3]]. Xem [[nii-planning]].

- **NII âm và chiến lược tiền gửi (Choudhry CS6)**: mỗi mảng nhận FTP bid cho nguồn vốn từ Group Treasury; số dư có lãi suất khách hàng cao hơn FTP bid tạo 'NII âm', khoảng 10% số dư trong case; rà soát dẫn tới chiến lược tiền gửi qua ALCO [[src-choudhry-principles-banking#^choudhry-cs-20]].
- **Bỏ FTP Libor-flat (Choudhry CS2, Europe Arab Bank)**: FTP Libor-flat tạo rủi ro thanh khoản dư thừa và lợi nhuận mảng kinh doanh ảo khi ngân hàng huy động cao hơn Libor [[src-choudhry-principles-banking#^choudhry-cs-3]]; chế độ mới thêm liquidity premium theo kỳ hạn [[src-choudhry-principles-banking#^choudhry-cs-4]]. Xem [[liquidity-transfer-pricing]], [[climate-risk]].

**Treasury là cost centre hay profit centre (Choudhry Ch5).** Lãi suất FTP phụ thuộc mandate của Treasury [[src-choudhry-principles-banking#^choudhry-mo-3]]:
- cost centre: cung cấp dịch vụ funding tập trung;
- profit centre: ngoài thu xếp funding còn kiếm P&L từ rủi ro lãi suất phát sinh khi funding ở đầu ngắn đường cong.

Lãi suất chuyển giao thường bằng cost of funds nội bộ của Treasury, có thể cộng spread bù chi phí vận hành [[src-choudhry-principles-banking#^choudhry-mo-3]].

**Funding "cash" và funding "balance sheet".** Có hai cách xác định số tiền Treasury cho vay nội bộ từng khối [[src-choudhry-principles-banking#^choudhry-mo-1]]. Thông lệ tốt trong môi trường trading là lợi ích hay chi phí funding của P&L thuộc về Treasury, không thuộc khối tạo ra P&L [[src-choudhry-principles-banking#^choudhry-mo-2]].

Nguyên tắc 9 của Choudhry: khung FTP phải đặt đúng; lãi suất nội bộ không phản ánh thực tế dẫn tới quyết định kinh doanh sai [[src-choudhry-principles-banking#^choudhry-liq-9]].

**Vốn chủ sở hữu và FTP (Choudhry Ch16).**
- Vốn cổ phần không có chi phí lãi thực nhưng có chi phí quy đổi là RoE mục tiêu; không gán chi phí này thì vốn thành 'free capital' cho mảng kinh doanh và SVA bị báo sai [[src-choudhry-principles-banking#^choudhry-capm-11]].
- Best practice: lợi ích của nguồn vốn 'free' giao cho central ALCO book; thực tế vốn thường nằm trong Treasury book và nhập pool funding do Treasury quản lý [[src-choudhry-principles-banking#^choudhry-capm-12]]. Lợi ích lãi ròng này chịu cùng quy tắc FTP như mọi nguồn funding; lợi nhuận giữ lại xử lý nhất quán với vốn cổ phần [[src-choudhry-principles-banking#^choudhry-capm-13]].
- Lãi subordinated debt tách 3 phần: base rate ngắn hạn, term premium (về Treasury P&L rồi phân bổ lại cho mảng) và subordinated premium (xử lý như return trên vốn cổ phần) [[src-choudhry-principles-banking#^choudhry-capm-14]].

## Phụ thuộc regime

- Trong khủng hoảng, để khuyến khích huy động và hạn chế cho vay, đường cong FTP phải được định giá lại và/hoặc áp steering margin; điều chỉnh độ dốc đường cong FTP để quản lý tác động của kết quả chuyển hoá kỳ hạn lên NII [[src-bardaeva-alm#^ch15-8]].
- Ở thị trường kém phát triển, khả năng dựng đường cong nội bộ hạn chế và có thể áp cách tiếp cận đơn giản hơn [[src-bardaeva-alm#^ch14-16]].
- Chênh lệch chi phí huy động vốn của ngân hàng nới rộng đã dẫn tới việc bổ sung lớp liquidity FTP vào FTP lãi suất cổ điển [[src-choudhry-principles-banking#^choudhry-ftp-14]].
- Nguồn T5 mô tả cách điều chỉnh theo trạng thái thanh khoản: LCR thấp thì tăng spread cho tenor ngắn (O/N đến 30 ngày); NSFR thấp thì tăng spread cho tenor dài (6M đến 2Y trở lên) [[src-ftp-transmission-analysis#^ftp-trans-8]].

## Góc nhìn theo domain

- **ALM**: nguồn T5 coi FTP là hệ thống điều khiển trung tâm (unified control mechanism) trong quản trị bảng cân đối [[src-ftp-transmission-analysis#^ftp-trans-1]]. VAB nêu các mục tiêu tổng thể của dự án FTP: quản lý lợi nhuận, quản lý bảng cân đối, quản lý rủi ro thanh khoản và rủi ro lãi suất trên sổ ngân hàng, định hướng hoạt động kinh doanh [[src-vab-ftp#^vab-ftp-2]].
- **Tổ chức (Bardaeva, T4)**: ALM xác định nguyên tắc định giá điều chuyển, dựng đường cong FTP nội bộ và quy tắc xác định lãi suất khách hàng tối thiểu [[src-bardaeva-alm#^ch11-5]]. Nguyên tắc gán kỳ hạn trên đường cong không được do đơn vị thực hiện giao dịch quyết định [[src-bardaeva-alm#^ch11-11]]. Trong tập đoàn, Group Treasury thiết kế nguyên tắc và mô hình FTP [[src-bardaeva-alm#^ch12-3]]. Xem [[alm-operating-model]].
- **Product**: commercial margin của giao dịch khách hàng giữ nguyên trước biến động sau đó của đường cong FTP và tỷ giá [[src-choudhry-principles-banking#^choudhry-ftp-8]].
- **Basel / VN**: VAB đặt mục tiêu hướng dẫn định giá điều chuyển vốn tuân thủ quy định pháp luật và phù hợp tiêu chuẩn Basel [[src-vab-ftp#^vab-ftp-3]]. Wiki chưa có chuẩn mực BCBS hay văn bản NHNN quy định trực tiếp về FTP [cần nguồn]. TT83/2025 có hai yêu cầu gián tiếp: đưa chi phí thanh khoản vào định giá vốn nội bộ [[src-tt83-2025-nhnn#^d45-1b]], và có nguyên tắc xác định chi phí bù đắp rủi ro tín dụng trong tính lãi suất, định giá sản phẩm tín dụng theo mức rủi ro của khách hàng [[src-tt83-2025-nhnn#^d26-2c]]. Xem [[credit-risk-management]]. Sản phẩm mới phải được bộ phận quản lý rủi ro thẩm định tác động lên vốn tự có, thu nhập trước khi thử nghiệm [[src-tt83-2025-nhnn#^d21-2]]; xem [[new-product-approval]].

## Bằng chứng thực nghiệm

- **UBS (2008)**: lãnh đạo không phát hiện lỗi trong cơ chế funding nội bộ cho phép mảng structured credit báo lãi ảo; mô hình funding thực tế hơn bị xem là 'ràng buộc chiến lược tăng trưởng'. Choudhry kết luận giá chuyển vốn từ Treasury phải phản ánh đúng rủi ro thanh khoản của từng mảng [[src-choudhry-principles-banking#^choudhry-gov-12]]. Xem [[bank-corporate-governance]].

## Câu hỏi mở

- Công thức cấu phần và kênh truyền dẫn ở trên dựa vào nguồn T5 (`src-ftp-transmission-analysis`), chưa đối chiếu với nguồn T4 hoặc cao hơn.
- [[cost-of-funds]] (COF, [[src-vab-ftp#^vab-ftp-7]]) đang là stub; hoàn thiện bằng `/ingest --node cost-of-funds`.
- Chưa có nguồn NHNN về yêu cầu đối với hệ thống FTP tại VN.
