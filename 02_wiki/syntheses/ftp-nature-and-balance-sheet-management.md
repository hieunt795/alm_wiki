---
title: "Bản Chất, Mục Tiêu Của FTP Và Các Vấn Đề Cốt Tử Giải Quyết Trong Quản Trị Bảng Cân Đối"
aliases: [FTP Nature and Balance Sheet Management, Bản chất và mục tiêu của FTP, FTP trong quản trị bảng cân đối, FTP Problem Solving, Balance Sheet Governance FTP]
type: synthesis
domains: [alm, product]
status: active
maturity: canonical
origin: query
question: "Bản chất và mục tiêu của Funds Transfer Pricing (FTP) trong ngân hàng là gì? FTP giải quyết vấn đề gì trong quản trị bảng cân đối?"
sources: ["[[src-choudhry-principles-banking]]", "[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]"]
relations: []
tags: [ftp, balance-sheet-management, alm, treasury, alco, internal-risk-transfer, customer-franchise, maturity-transformation, synthesis]
updated: 2026-10-17
reviewed:
---

## 1. Tóm Tắt Quản Trị Cấp Cao (Executive Summary)

Trong lịch sử phát triển của ngành ngân hàng thương mại, **Funds Transfer Pricing (FTP — Cơ chế Định giá Điều chuyển Vốn Nội bộ)** là một trong những phát kiến quản trị mang tính cách mạng nhất. Nếu không có FTP, một ngân hàng thương mại không thể vận hành an toàn và minh bạch theo mô hình hiện đại.

Hai luận điểm cốt lõi trả lời trực diện cho câu hỏi nghiên cứu:
1. **Về Bản chất**: FTP không phải là việc phòng ngừa rủi ro ra bên ngoài thị trường, cũng không phải là việc luân chuyển vật lý dòng tiền tệ nội bộ; **FTP là cơ chế chuyển giao rủi ro nội bộ (Internal Transfer of Risk)** [[src-choudhry-principles-banking#^choudhry-ftp-10]]. FTP thiết lập ranh giới kinh tế dứt khoát giữa **thương quyền khách hàng phi rủi ro thị trường (Customer Franchise)** của các chi nhánh và **hoạt động chuyển đổi kỳ hạn rủi ro (Maturity Transformation)** được quản trị tập trung tại Treasury [[src-choudhry-principles-banking#^choudhry-ftp-3]] [[src-choudhry-principles-banking#^choudhry-ftp-13]].
2. **Về Mục tiêu & Vấn đề giải quyết**: FTP là **hệ thống điều khiển trung tâm (Unified Control Mechanism)** [[src-ftp-transmission-analysis#^ftp-trans-1]] giải quyết triệt để 5 vấn nạn kinh điển của bảng cân đối ngân hàng:
   - *(i) Triệt tiêu tình trạng trợ cấp chéo rủi ro (cross-subsidization)* và méo mó đo lường hiệu quả kinh doanh giữa các chi nhánh [[src-choudhry-principles-banking#^choudhry-ftp-9]];
   - *(ii) Chặn đứng cạm bẫy chuyển đổi kỳ hạn quá mức* (dùng vốn ngắn hạn tài trợ cho vay dài hạn mất kiểm soát) thông qua cơ chế tính đúng chi phí thanh khoản kỳ hạn TLP [[src-choudhry-principles-banking#^choudhry-ftp-15]] [[src-vab-ftp#^vab-ftp-11]];
   - *(iii) Tập trung hóa và tối ưu hóa việc quản trị rủi ro thanh khoản ([lcr|LCR], [nsfr|NSFR]) và rủi ro lãi suất ([bcbs-irrbb|IRRBB])* về một đầu mối chuyên nghiệp thay vì để các chi nhánh tự xoay xở phân tán [[src-ftp-transmission-analysis#^ftp-trans-9]] [[src-vab-ftp#^vab-ftp-4]];
   - *(iv) Nội bộ hóa sòng phẳng các chi phí tuân thủ pháp lệnh của NHNN* (Dự trữ bắt buộc, Bảo hiểm tiền gửi, Đệm tài sản thanh khoản) vào giá bán vốn tín dụng [[src-vab-ftp#^vab-ftp-5]];
   - *(v) Thay thế mệnh lệnh hành chính xơ cứng bằng đòn bẩy giá cả thị trường nội bộ*, giúp Ủy ban ALCO dẫn dắt toàn hệ thống đạt điểm tối ưu Pareto trên bảng cân đối [[src-ftp-transmission-analysis#^ftp-trans-13]] [[src-vab-ftp#^vab-ftp-2]].

---

## 2. Bản Chất Sâu Xa Của Funds Transfer Pricing (FTP)

```
+---------------------------------------------------------------------------------------------------+
|                        BẢN CHẤT CỐT LÕI CỦA HỆ THỐNG FTP: TÁCH BẠCH 2 THỰC THỂ                    |
+---------------------------------------------------------------------------------------------------+
|                                     BẢNG CÂN ĐỐI NGÂN HÀNG                                        |
|                                                |                                                  |
|                        +-----------------------+-----------------------+                          |
|                        |                                               |                          |
|                        v                                               v                          |
|      [ THƯƠNG QUYỀN KHÁCH HÀNG ]                     [ CHUYỂN ĐỔI KỲ HẠN RỦI RO ]                 |
|          (Customer Franchise)                           (Maturity Transformation)                 |
|                                                                                                   |
|  - Thực thể: Chi nhánh / Khối KHDN, KHCN       - Thực thể: Trung tâm Quản trị Vốn (CFU/ALM)       |
|  - Bản chất: Mối quan hệ khách hàng, mạng lưới  - Bản chất: Mất cân đối kỳ hạn Tài sản - Nợ       |
|  - Rủi ro: Tín dụng vi mô & Vận hành           - Rủi ro: Thanh khoản LCR/NSFR & Lãi suất IRRBB    |
|  - Lợi nhuận: BIÊN THƯƠNG MẠI CỐ ĐỊNH          - Lợi nhuận: BIÊN TREASURY (MISMATCH MARGIN)       |
|    (Phi rủi ro thị trường)                       (Bù đắp chi phí phòng ngừa rủi ro phái sinh)     |
|                        ^                                               ^                          |
|                        +-----------------------+-----------------------+                          |
|                                                |                                                  |
|                                  +---------------------------+                                    |
|                                  |   RANH GIỚI PHÂN TÁCH:    |                                    |
|                                  |       HỆ THỐNG FTP        |                                    |
|                                  +---------------------------+                                    |
+---------------------------------------------------------------------------------------------------+
```

### 2.1. Phân định Thương quyền Khách hàng vs. Chuyển đổi Kỳ hạn
Theo Giáo sư Moorad Choudhry, hoạt động ngân hàng luôn chứa đựng hai cấu phần giá trị hoàn toàn khác biệt:
- **Chuyển đổi kỳ hạn (Maturity Transformation)**: Việc tạo ra lợi nhuận rủi ro từ sự không khớp kỳ hạn trong cấu trúc thời hạn của tài sản và nợ [[src-choudhry-principles-banking#^choudhry-ftp-1]]. Ngân hàng huy động ngắn hạn và cho vay dài hạn để hưởng chênh lệch dốc của đường cong lợi suất.
- **Thương quyền khách hàng (Customer Franchise)**: Năng lực của một ngân hàng trong việc tạo ra lợi nhuận từ việc bán các sản phẩm cho khách hàng ở mức lãi suất khác biệt với lãi suất thị trường vốn [[src-choudhry-principles-banking#^choudhry-ftp-2]]. Chi nhánh giỏi là chi nhánh thuyết phục được khách hàng gửi tiền với lãi suất thấp hơn thị trường (ví dụ CASA 0,5%), hoặc tìm được người vay tốt chấp nhận trả lãi suất cao hơn thị trường.

**Bản chất của FTP chính là ranh giới phân định dứt khoát giữa hai cấu phần này** [[src-choudhry-principles-banking#^choudhry-ftp-3]]. FTP cho phép ngân hàng đo lường chuẩn xác năng lực tạo lợi nhuận từ thương quyền khách hàng của từng đơn vị kinh doanh mà không bị lẫn lộn với rủi ro chuyển đổi kỳ hạn của toàn hàng [[src-choudhry-principles-banking#^choudhry-ftp-4]].

### 2.2. Hai Nguyên Tắc Nền Tảng Của FTP
Hệ thống FTP vận hành dựa trên 2 nguyên tắc kỹ trị nền tảng:
1. **Nguyên tắc Trùng khớp Kỳ hạn (Matched-Maturity Principle)**:
   - Mỗi giao dịch khách hàng được định giá nội bộ đối ứng với một mức giá phòng ngừa danh nghĩa (notional hedge) có cùng kỳ hạn, cùng đồng tiền và cùng cơ sở lãi suất trên đường cong FTP [[src-choudhry-principles-banking#^choudhry-ftp-5]] [[src-choudhry-principles-banking#^choudhry-ftp-6]] [[src-choudhry-principles-banking#^choudhry-ftp-11]].
   - Nhờ vậy, **biên lợi nhuận thương mại của đơn vị kinh doanh giữ nguyên không đổi trong suốt vòng đời của hợp đồng**, hoàn toàn không bị ảnh hưởng bởi các biến động tăng/giảm lãi suất thị trường sau đó [[src-choudhry-principles-banking#^choudhry-ftp-8]].
2. **Nguyên tắc Cận biên (Marginality Principle)**:
   - Chi phí vốn lịch sử đã phát sinh trong quá khứ không có giá trị đối với việc định giá các giao dịch mới [[src-choudhry-principles-banking#^choudhry-ftp-12]].
   - Mọi khoản vay mới và tiền gửi mới đều phải được định giá dựa trên chi phí/lợi ích biên tế tại thời điểm phát sinh giao dịch trên thị trường vốn hiện hành.

---

## 3. Bốn Mục Tiêu Chiến Lược Của Hệ Thống FTP Trong Ngân Hàng

Theo tài liệu tư vấn của EY cho VietABank và chuẩn mực quản trị quốc tế, việc triển khai dự án FTP giúp ngân hàng nâng cao hiệu quả điều hành Bảng cân đối kế toán và đáp ứng đồng thời **4 mục tiêu chiến lược cốt lõi** [[src-vab-ftp#^vab-ftp-1]] [[src-vab-ftp#^vab-ftp-2]]:

```
+---------------------------------------------------------------------------------------------------+
|                            BỐN MỤC TIÊU CHIẾN LƯỢC CỦA HỆ THỐNG FTP                               |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  1. QUẢN LÝ LỢI NHUẬN & HIỆU QUẢ HOẠT ĐỘNG (Profitability & Performance Measurement)              |
|     - Bóc tách minh bạch 3 nguồn lợi nhuận trong NIM (Biên cho vay, Biên tiền gửi, Biên Treasury) |
|     - Đánh giá KPI công bằng giữa các chi nhánh, không bị méo mó bởi biến động thị trường         |
|     - Thiết lập cơ sở định giá sản phẩm trên cơ sở rủi ro (Deal-level RAROC)                      |
|                                                                                                   |
|  2. QUẢN LÝ TẬP TRUNG RỦI RO THANH KHOẢN & LÃI SUẤT (Centralized Liquidity & IRRBB Management)    |
|     - Cách ly rủi ro tái định giá (Repricing Gap) và rủi ro thanh khoản khỏi các chi nhánh         |
|     - Chuyển giao toàn bộ rủi ro về Treasury (CFU) để quản lý tập trung và bù trừ tự nhiên        |
|     - Phòng ngừa rủi ro chuyên nghiệp thông qua thị trường tài chính và phái sinh (IRS)           |
|                                                                                                   |
|  3. QUẢN TRỊ & TỐI ƯU HÓA BẢNG CÂN ĐỐI (Balance Sheet Management & Optimization)                  |
|     - Kiểm soát cấu trúc kỳ hạn và động lực dòng tiền vào/ra trên toàn hệ thống                   |
|     - Đảm bảo tuân thủ đồng thời các tỷ lệ an toàn: LCR >= 100%, NSFR >= 100%, LEV >= 3%, CAR     |
|     - Giải bài toán quy hoạch tối ưu hóa thu nhập lãi thuần NII dưới đa ràng buộc                 |
|                                                                                                   |
|  4. ĐỊNH HƯỚNG HOẠT ĐỘNG KINH DOANH (Business Steering & Behavioral Incentives)                   |
|     - Dẫn dắt hành vi chi nhánh thông qua tín hiệu giá cả nội bộ (Biểu giá VOF và COF)           |
|     - Khuyến khích tăng trưởng tiền gửi CASA và nguồn vốn trung dài hạn bền vững                   |
|     - Điều tiết dòng vốn vào các ngành kinh tế ưu tiên theo khẩu vị rủi ro của ALCO               |
+---------------------------------------------------------------------------------------------------+
```

---

## 4. Năm Vấn Đề Cốt Tử FTP Giải Quyết Trong Quản Trị Bảng Cân Đối

Nếu không có hệ thống FTP đa tầng hiện đại, bảng cân đối của ngân hàng thương mại tất yếu rơi vào 5 "căn bệnh hiểm nghèo" sau đây:

### 4.1. Vấn nạn 1: Trợ Cấp Chéo Rủi Ro (Cross-Subsidization) và Méo Mó Đánh Giá Hiệu Quả
- **Căn bệnh trong mô hình cổ điển**: Ngân hàng áp dụng một mức lãi suất cào bằng hoặc tính lãi suất hòa vốn bình quân (average cost of funds). 
  - Chi nhánh A cho vay 5 năm cố định với lãi suất 10% được tung hô là "chi nhánh ngôi sao" vì mang lại doanh thu cao.
  - Chi nhánh B chuyên đi huy động tiền gửi kỳ hạn dài 3 năm với lãi suất 7% bị chê là "chi phí cao, làm ăn kém hiệu quả".
  - Chi nhánh C chuyên huy động tiền gửi ngắn hạn 1 tháng giá 3.5% được khen ngợi là "tiết kiệm chi phí".
  - **Sự thật bị che giấu**: Chi nhánh A và C đang cùng nhau tạo ra một quả bom nổ chậm về mất cân đối kỳ hạn (lấy nợ 1 tháng tài trợ tài sản 5 năm). Khi lãi suất thị trường tăng lên 8%, Chi nhánh C vỡ trận vì chi phí vốn nhảy vọt, Chi nhánh A trở thành gánh nặng vì kẹt vốn 10%, trong khi Chi nhánh B (với nguồn vốn 3 năm giá 7%) mới thực sự là cứu tinh của ngân hàng!
- **FTP giải quyết thế nào**: 
  - FTP triệt tiêu hoàn toàn sự trợ cấp chéo giữa các giao dịch [[src-choudhry-principles-banking#^choudhry-ftp-9]].
  - Chi nhánh A vay vốn 5 năm của CFU với giá COF 5 năm là 8.5% $\rightarrow$ Biên thực tế chỉ là $1.5\%$.
  - Chi nhánh B bán vốn 3 năm cho CFU với giá VOF 3 năm là 8.0% $\rightarrow$ Chi nhánh B được ghi nhận lãi thực tế $+1.0\%$ và được vinh danh xứng đáng.
  - Mỗi chi nhánh chỉ được hưởng đúng phần giá trị gia tăng từ thương quyền khách hàng của mình, không thể "ăn cắp" lợi nhuận từ việc đánh cược rủi ro kỳ hạn.

---

### 4.2. Vấn nạn 2: Cạm Bẫy Chuyển Đổi Kỳ Hạn Quá Mức (Maturity Transformation Trap)
- **Căn bệnh**: Bản chất của ngân hàng là thực hiện chuyển đổi kỳ hạn. Nhưng nếu không có cơ chế tính giá thanh khoản dài hạn, các nhân viên tín dụng sẽ luôn tìm cách bán các khoản vay trung dài hạn (5–10 năm) có lãi suất danh nghĩa cao để dễ đạt KPI doanh số và hoa hồng. Hậu quả là toàn bộ bảng cân đối bị "đóng băng" thanh khoản, tỷ lệ vốn ngắn hạn cho vay trung dài hạn vi phạm trần quy định của NHNN, và chỉ số [nsfr](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/nsfr.md) tụt dốc thảm hại.
- **FTP giải quyết thế nào**:
  - **Tách tầng Liquidity FTP**: Bổ sung cấu phần **Phần bù thanh khoản kỳ hạn (Term Liquidity Premium — TLP)** [[src-choudhry-principles-banking#^choudhry-ftp-14]] [[src-vab-ftp#^vab-ftp-11]].
  - Bất kỳ đơn vị nào tạo ra tài sản dài hạn gây áp lực thanh khoản cho ngân hàng đều **bắt buộc phải trả phí thanh khoản dài hạn đó thông qua giá FTP (COF)** [[src-choudhry-principles-banking#^choudhry-ftp-15]].
  - Đối với các khoản vay lãi suất thả nổi (ví dụ vay 5 năm thả nổi 3 tháng/lần), FTP áp cấu phần TLP bằng chênh lệch giữa đường cong kỳ hạn gốc 5 năm và kỳ hạn tái định giá 3 tháng [[src-vab-ftp#^vab-ftp-12]]. Chi nhánh không thể "ăn gian" bằng cách viện cớ lãi suất thả nổi để né tránh chi phí thanh khoản dài hạn.

---

### 4.3. Vấn nạn 3: Quản Trị Rủi Ro Thị Trường Bị Phân Tán và Tê Liệt
- **Căn bệnh**: Nếu không có cơ chế chuyển giao rủi ro tập trung, từng giám đốc chi nhánh sẽ phải tự mình dự đoán xem tuần tới Ngân hàng Nhà nước tăng hay giảm lãi suất OMO, đường cong lợi suất TPCP sẽ dốc hay phẳng để quyết định có nhận tiền gửi hay cho vay hay không. Đây là điều bất khả thi và sẽ làm tê liệt toàn bộ hoạt động kinh doanh bán lẻ.
- **FTP giải quyết thế nào**:
  - **Nguyên tắc chuyển giao rủi ro nội bộ (Internal Risk Transfer)** [[internal-risk-transfer]]: BU chuyển giao toàn bộ rủi ro thanh khoản và rủi ro lãi suất cho CFU [[src-choudhry-principles-banking#^choudhry-ftp-10]].
  - BU hoàn toàn yên tâm tập trung vào chuyên môn bán hàng và chăm sóc khách hàng với biên thương mại được bảo hiểm cố định [[src-ftp-transmission-analysis#^ftp-trans-10]].
  - CFU gom toàn bộ các dòng tiền trên toàn quốc vào một "hồ chứa trung tâm" (Liquidity & Risk Pool), tận dụng triệt để hiệu ứng bù trừ tự nhiên (natural netting), quy luật số lớn trên tiền gửi CASA [[src-vab-ftp#^vab-ftp-14]], và sử dụng các công cụ thị trường tài chính chuyên nghiệp như hợp đồng hoán đổi lãi suất [[interest-rate-swap|IRS]], giao dịch Repo để phòng ngừa rủi ro tập trung với chi phí thấp nhất.

---

### 4.4. Vấn nạn 4: Chi Phí Tuân Thủ Pháp Định Bị Xem Là "Khoản Lỗ Chung Của Hội Sở"
- **Căn bệnh**: Để duy trì hoạt động ngân hàng, hệ thống phải gánh chịu nhiều chi phí pháp lệnh khổng lồ theo quy định của Ngân hàng Nhà nước và Basel:
  1. Tiền gửi Dự trữ bắt buộc (DTBB) tại NHNN hưởng lãi suất 0% hoặc gần 0% (Thông tư 30/2019/TT-NHNN).
  2. Phí Bảo hiểm tiền gửi nộp định kỳ 0,15%/năm trên số dư tiền gửi cá nhân VND.
  3. Chi phí gánh khoản lỗ âm (negative carry) khi phải nắm giữ hàng chục nghìn tỷ đồng Trái phiếu Chính phủ lợi suất thấp để làm đệm thanh khoản [lcr](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/lcr.md) theo Thông tư 22/2019/TT-NHNN.
  - Nếu Hội sở tự gánh các chi phí này vào P&L chung, các chi nhánh sẽ có ảo tưởng rằng nguồn vốn rất rẻ, từ đó hạ lãi suất cho vay khách hàng xuống mức không đủ bù đắp chi phí tuân thủ thực tế của ngân hàng.
- **FTP giải quyết thế nào**:
  - Hệ thống FTP tại Việt Nam (theo chuẩn mực tư vấn của EY) **lượng hóa và phân bổ sòng phẳng toàn bộ các chi phí pháp định này vào giá bán vốn COF của bên sử dụng vốn** [[src-vab-ftp#^vab-ftp-5]]:
    $$\text{Tỷ lệ Chi phí DTBB} = \frac{\text{Số dư DTBB} \times (\text{VOF bình quân} - \text{Lãi suất gửi tại SBV})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$ [[src-vab-ftp#^vab-ftp-9]]
    $$\text{Tỷ lệ Chi phí BHTG} = \frac{\text{Tổng chi phí BHTG thực tế 3 tháng quy đổi năm}}{\text{Bình quân Tổng tài sản bị tính FTP}}$$ [[src-vab-ftp#^vab-ftp-8]]
    $$\text{Liquidity Buffer Premium} = \frac{\text{Số dư TSTK} \times (\text{VOF bình quân} - \text{Lãi suất TSTK})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$ [[src-vab-ftp#^vab-ftp-10]]
  - Nhờ vậy, mỗi hợp đồng tín dụng được giải ngân ra thị trường đều đã được tính đúng, tính đủ toàn bộ các chi phí pháp định cần thiết để bảo vệ an toàn cho hệ thống.

---

### 4.5. Vấn nạn 5: Mâu Thuẫn Giữa Mệnh Lệnh Hành Chính Và Động Lực Thị Trường Nội Bộ
- **Căn bệnh**: Khi ngân hàng đối mặt với áp lực thiếu hụt thanh khoản hoặc rủi ro lãi suất tăng cao, Ban Điều hành thường dùng biện pháp hành chính: ra công văn cấm cho vay trung dài hạn, ép từng chi nhánh giao chỉ tiêu huy động tiền gửi dài hạn. Phương pháp này thường gây bức xúc, triệt tiêu động lực kinh doanh của nhân viên, và chi nhánh sẽ tìm cách "lách" quy định (như biến tướng hợp đồng hoặc cơ cấu nợ).
- **FTP giải quyết thế nào**:
  - ALCO sử dụng FTP như **cơ chế dẫn dắt bằng giá cả thị trường nội bộ (Market-based Steering)** [[src-ftp-transmission-analysis#^ftp-trans-13]]:
    - Khi ngân hàng cần tăng nguồn vốn ổn định dài hạn để cải thiện [nsfr](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/nsfr.md), ALCO chỉ cần điều chỉnh tăng biên độ giá mua vốn VOF kỳ hạn 12M–24M [[src-ftp-transmission-analysis#^ftp-trans-8]]. Chi nhánh nhận thấy bán vốn dài hạn cho CFU có lời lớn sẽ tự động chuyển hướng tiếp thị tiền gửi dài hạn.
    - Khi ngân hàng muốn kìm hãm tín dụng bất động sản có hệ số rủi ro cao (RWA 150%–200%) để bảo vệ tỷ lệ an toàn vốn CAR và tỷ lệ đòn bẩy [leverage-ratio](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/leverage-ratio.md), ALCO chỉ việc tăng thành phần **Capital Charge** trong giá bán vốn COF [[src-ftp-transmission-analysis#^ftp-trans-12]]. Chi nhánh nhận thấy biên lợi nhuận bị thu hẹp sẽ tự động chuyển dịch dòng vốn sang cho vay sản xuất kinh doanh hoặc cho vay mua nhà ở an toàn.
  - Mọi sự chuyển dịch bảng cân đối đều diễn ra tự giác, nhịp nhàng theo quy luật kinh tế học, không cần đến mệnh lệnh hành chính khiên cưỡng.

---

## 5. Tổng Kết: Kiến Trúc Hoàn Hảo Của Quản Trị Bảng Cân Đối Hiện Đại

```
====================================================================================================
               VỊ TRÍ TRUNG TÂM CỦA FTP TRONG QUẢN TRỊ BẢNG CÂN ĐỐI NGÂN HÀNG (ALM)
====================================================================================================

               ỦY BAN ALCO (Hạn mức Rủi ro, Khẩu vị Rủi ro & Chiến lược Tối ưu hóa)
                                                |
               +--------------------------------+--------------------------------+
               |  Biến số Điều khiển: HIỆU CHỈNH ĐƯỜNG CONG VOF / COF VÀ SPREADS |
               v                                                                 v
+--------------------------------------------------------------------------------------------------+
|                            TRUNG TÂM QUẢN LÝ VỐN TẬP TRUNG (CFU)                                 |
|  - Hấp thụ 100% Rủi ro Thanh khoản (LCR, NSFR) & Rủi ro Lãi suất (IRRBB, Repricing Gap)          |
|  - Vận hành Hồ điều tiết trung tâm (Netting & Pooling dòng tiền toàn hàng)                       |
|  - Phòng ngừa rủi ro phái sinh tập trung trên thị trường liên ngân hàng (IRS, CCS, OMO, Repo)    |
+--------------------------------------------------------------------------------------------------+
               ^                                                                 ^
               | Bán Vốn (Nhận VOF)                           Mua Vốn (Trả COF)  |
               | Chuyển giao Rủi ro                           Mua Bảo hiểm Rủi ro|
               v                                                                 v
+---------------------------------------+              +-------------------------------------------+
|    ĐƠN VỊ HUY ĐỘNG (Liabilities)      |              |        ĐƠN VỊ SỬ DỤNG VỐN (Assets)        |
|  - Tập trung phát triển tiền gửi CASA |              |  - Cho vay Doanh nghiệp & Cá nhân         |
|  - Khóa chặt Biên Huy động cố định:   |              |  - Khóa chặt Biên Cho vay cố định:        |
|    Margin = VOF - Lãi suất khách gửi  |              |    Margin = Lãi suất khách vay - COF      |
|  - An tâm kinh doanh, không sợ biến   |              |  - An tâm giải ngân, không sợ biến động   |
|    động lãi suất thị trường           |              |    lãi suất và áp lực thanh khoản kỳ hạn  |
+---------------------------------------+              +-------------------------------------------+
               ^                                                                 ^
               | Nhận tiền gửi thật                               Giải ngân nợ vay thật
               v                                                                 v
+---------------------------------------+              +-------------------------------------------+
|       NGƯỜI GỬI TIỀN NGOẠI BẢNG       |              |         NGƯỜI VAY TIỀN NGOẠI BẢNG         |
+---------------------------------------+              +-------------------------------------------+

====================================================================================================
```

### Thông điệp đúc kết
FTP chính là **trái tim điều phối dòng chảy giá trị và rủi ro** của ngân hàng thương mại:
- Nó trả lời chính xác **"Ai làm ra tiền và ai đang gánh rủi ro"**.
- Nó bảo vệ **chi nhánh kinh doanh bằng một chiếc áo giáp bảo hiểm biên lợi nhuận**.
- Nó cung cấp cho **Ủy ban ALCO một chiếc vô lăng điều khiển tối tân** để lèo lái con tàu bảng cân đối vượt qua mọi cuộc khủng hoảng thanh khoản và chu kỳ biến động lãi suất khốc liệt của thị trường tài chính.

## Khái niệm và Liên kết
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn FTP đến các yếu tố rủi ro thanh khoản, lãi suất, tín dụng và vốn.
- [[ftp-pricing-methodology]]: Phương pháp luận định giá chi tiết VOF, COF, phụ phí pháp định và quyền chọn ẩn.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa bảng cân đối ALM toàn diện dưới hệ thống điều khiển FTP.
- [[ftp-risk-and-cost-components]]: Các cấu phần rủi ro và chi phí trong định giá FTP (Funding, Liquidity, IRRBB, Optionality).
- [[ftp-curve-construction-methodology]]: Phương pháp luận xây dựng đường cong FTP theo kỳ hạn, đồng tiền và loại sản phẩm.
- [[liquidity-transfer-pricing]]: Tổng quan lý thuyết định giá điều chuyển thanh khoản nội bộ theo Moorad Choudhry.
- [[synthetic-balance-sheet-liquidity-risk]]: Bảng cân đối thanh khoản tổng hợp và động lực dòng tiền.
- [[practical-alm-liquidity-governance]]: Khung điều hành quản trị thanh khoản thực chiến.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn Basel III.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn Basel III.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.
