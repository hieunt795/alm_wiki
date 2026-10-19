---
title: "Các Cấu Phần Rủi Ro Và Chi Phí Trong Định Giá FTP: Funding Cost, Liquidity Risk, Interest Rate Risk Và Optionality"
aliases: [FTP Risk and Cost Components, FTP Components, Cấu phần rủi ro và chi phí trong định giá FTP, Funding Liquidity IRRBB Optionality FTP]
type: synthesis
domains: [alm, product]
status: active
maturity: canonical
origin: query
question: "FTP phản ánh và định giá những loại rủi ro/chi phí nào trên bảng cân đối, đặc biệt là funding cost, liquidity risk, interest rate risk và optionality?"
sources: ["[[src-ftp-transmission-analysis]]", "[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]"]
relations: []
tags: [ftp, funding-cost, liquidity-risk, irrbb, optionality, term-liquidity-premium, embedded-options, prepayment, non-maturity-deposits, synthesis]
updated: 2026-10-17
reviewed:
---

## 1. Tóm Tắt Quản Trị Cấp Cao (Executive Summary)

Trong kỹ trị ngân hàng thương mại hiện đại, **Funds Transfer Pricing (FTP — Cơ chế Định giá Điều chuyển Vốn Nội bộ)** không chỉ đơn thuần là một mức lãi suất cào bằng, mà là một **hệ thống điều khiển trung tâm đa tầng (Multi-layered Unified Control Mechanism)** [[src-ftp-transmission-analysis#^ftp-trans-1]]. 

Hệ thống FTP bóc tách toàn bộ bảng cân đối kế toán thành từng cấu phần rủi ro và chi phí độc lập. Mỗi giao dịch tín dụng (tài sản có) hoặc tiền gửi (tài sản nợ) khi phát sinh đều được định giá chính xác dựa trên công thức phân rã rủi ro đa chiều [[src-ftp-transmission-analysis#^ftp-trans-3]] [[src-vab-ftp#^vab-ftp-5]]:

$$\text{FTP Rate} = \text{Base Funding Rate} + \text{Liquidity Premium} + \text{IRRBB Term Structure} + \text{Optionality Charge} + \text{Credit/Capital Spread}$$

```
+---------------------------------------------------------------------------------------------------+
|               BỐN TRỤ CỘT RỦI RO VÀ CHI PHÍ TRỌNG YẾU ĐƯỢC ĐỊNH GIÁ TRONG HỆ THỐNG FTP            |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  1. FUNDING COST (Chi phí Vốn Cơ sở & Lãi suất Tham chiếu)                                        |
|     - Đường cong phi rủi ro tham chiếu thị trường (SOFR / OIS / VNIBOR / TPCP)                    |
|     - Chi phí vốn cận biên (Marginal Cost of Funds) thay vì chi phí bình quân lịch sử             |
|     - Wholesale funding spread phản ánh chi phí huy động vốn bán buôn thực tế của ngân hàng       |
|                                                                                                   |
|  2. LIQUIDITY RISK (Rủi ro Thanh khoản & Chi phí Tuân thủ Pháp lệnh)                               |
|     - Term Liquidity Premium (TLP): Chi phí thanh khoản kỳ hạn cho các tài sản dài hạn thả nổi   |
|     - Liquidity Buffer Carry Cost: Bù đắp khoản lỗ âm khi nắm giữ đệm HQLA / TT22                 |
|     - Chi phí pháp định bắt buộc tại VN: Phí Bảo hiểm tiền gửi (BHTG) và Dự trữ bắt buộc (DTBB)   |
|     - Phụ phí cấu trúc NSFR khuyến khích nguồn vốn ổn định và hạn chế tài sản hao hụt vốn         |
|                                                                                                   |
|  3. INTEREST RATE RISK IN THE BANKING BOOK - IRRBB (Rủi ro Lãi suất Sổ Ngân hàng)                 |
|     - Gap Risk (Rủi ro khe hở tái định giá): Triệt tiêu qua nguyên tắc Trùng khớp kỳ hạn         |
|     - Basis Risk (Rủi ro cơ sở): Xử lý độ lệch giữa chỉ số huy động và chỉ số cho vay             |
|     - Yield Curve Risk: Quản trị tập trung độ dốc, độ cong đường cong lãi suất tại Treasury (CFU)|
|                                                                                                   |
|  4. OPTIONALITY & BEHAVIORAL RISK (Rủi ro Quyền chọn Ẩn & Rủi ro Hành vi Khách hàng)             |
|     - Prepayment Risk: Người vay trả nợ trước hạn khi lãi suất giảm (định giá qua WAL và CPR)     |
|     - Early Withdrawal Risk: Người gửi tiền rút trước hạn khi lãi suất tăng (Thông tư 04/2022)   |
|     - Non-Maturity Deposits (CASA): Mô hình danh mục sao chép phân tách Core vs Non-core CASA    |
|     - Automatic Options: Trần (Cap) và Sàn (Floor) lãi suất ngầm trong hợp đồng tín dụng          |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Trụ Cột 1: Funding Cost (Chi Phí Vốn Cơ Sở & Lãi Suất Tham Chiếu)

### 2.1. Bản chất của Đường cong Lãi suất Cơ sở (Base Curve)
Đường cong lãi suất cơ sở (Base Curve) là nền móng của toàn bộ hệ thống định giá FTP, đại diện cho chi phí cơ hội của vốn và lập trường chính sách tiền tệ [[src-ftp-transmission-analysis#^ftp-trans-4]]:
- **Thị trường quốc tế**: Sử dụng đường cong lãi suất phi rủi ro (Risk-Free Rate — RFR) như SOFR (USD), SONIA (GBP), hoặc đường cong hoán đổi lãi suất qua đêm (OIS Curve).
- **Thị trường Việt Nam**: Do thị trường OIS chưa phát triển hoàn thiện, đường cong cơ sở được xây dựng dựa trên sự kết hợp giữa:
  1. Đường cong lãi suất liên ngân hàng VNIBOR (cho các kỳ hạn ngắn hạn dưới 3 tháng);
  2. Lãi suất chào mua/chào bán OMO và tín phiếu của Ngân hàng Nhà nước;
  3. Đường cong lợi suất Trái phiếu Chính phủ Việt Nam (VGB Yield Curve từ Bloomberg BVAL hoặc Reuters) cho các kỳ hạn trung dài hạn từ 6 tháng đến 10 năm [[src-vab-ftp#^vab-ftp-24]].

### 2.2. Nguyên tắc Cận biên (Marginality Principle)
Theo Giáo sư Moorad Choudhry, một sai lầm phổ biến trong quản trị ngân hàng truyền thống là sử dụng chi phí vốn bình quân trong quá khứ (historical average cost of funds) để định giá:
- Chi phí đã phát sinh của nguồn vốn hiện có hoàn toàn không có giá trị đối với việc định giá các khoản vay mới [[src-choudhry-principles-banking#^choudhry-ftp-12]].
- Mọi khoản vay và tiền gửi mới đều phải được định giá dựa trên **chi phí cơ hội cận biên (Marginal Cost of Funds)** tại đúng thời điểm phát sinh giao dịch trên thị trường vốn [[src-choudhry-principles-banking#^choudhry-ftp-12]].
- Nếu lãi suất thị trường tăng từ 5% lên 8%, thì mọi khoản vay mới phải được định giá trên nền tảng 8%, bất kể ngân hàng vẫn còn những khoản tiền gửi cũ với lãi suất 4%. Nếu lấy giá 4% để cho vay 6%, ngân hàng sẽ chịu lỗ ngay lập tức khi khoản tiền gửi cũ đáo hạn.

### 2.3. Chênh lệch Chi phí Huy động Bán buôn (Bank's Wholesale Funding Spread)
Ngoài lãi suất phi rủi ro, giá vốn của ngân hàng luôn bao gồm một phần bù rủi ro thanh khoản bán buôn (Senior Unsecured Debt Spread) phản ánh mức độ tín nhiệm của chính ngân hàng đó trên thị trường liên ngân hàng và thị trường trái phiếu doanh nghiệp. Ngân hàng có xếp hạng tín nhiệm càng cao thì chi phí vốn nền tảng này càng thấp.

---

## 3. Trụ Cột 2: Liquidity Risk (Rủi Ro Thanh Khoản & Các Khoản Phụ Phí Pháp Định)

Sự kiện khủng hoảng tài chính toàn cầu 2008 đã thúc đẩy việc bổ sung một tầng định giá thanh khoản chuyên biệt gọi là **Liquidity FTP** nằm trên tầng định giá lãi suất truyền thống [[src-choudhry-principles-banking#^choudhry-ftp-14]]. Bất kỳ đơn vị nào tạo ra tài sản gây áp lực thanh khoản cho ngân hàng đều bắt buộc phải trả chi phí tìm kiếm thanh khoản đó [[src-choudhry-principles-banking#^choudhry-ftp-15]].

Trong thực tế điều hành tại Việt Nam (theo chuẩn tư vấn của EY) và chuẩn mực quốc tế, tầng rủi ro thanh khoản bao gồm 4 cấu phần:

### 3.1. Phần bù Thanh khoản Kỳ hạn (Term Liquidity Premium — TLP)
- **Bản chất**: Phản ánh chi phí thanh khoản dài hạn của ngân hàng [[src-vab-ftp#^vab-ftp-11]] [[src-vab-ftp#^vab-ftp-23]].
- **Ứng dụng cho khoản vay lãi suất thả nổi (Floating-rate Loans)**:
  - Một khoản vay thế chấp nhà 10 năm có điều khoản "lãi suất thả nổi tái định giá 3 tháng/lần". Đơn vị kinh doanh cho rằng khoản vay này chỉ chịu rủi ro kỳ hạn 3 tháng.
  - **Kỹ thuật FTP**: Khoản vay này được cách ly rủi ro lãi suất ở kỳ hạn 3 tháng, nhưng **cam kết thanh khoản gốc là 10 năm** [[src-vab-ftp#^vab-ftp-12]]. Ngân hàng không thể đòi lại nợ trước 10 năm. Do đó, khoản vay phải chịu phụ phí TLP bằng chênh lệch giữa lãi suất đường cong FTP kỳ hạn gốc 10 năm và kỳ hạn tái định giá 3 tháng [[src-vab-ftp#^vab-ftp-12]]:
    $$\text{TLP} = \text{FTP Rate}(10\text{Y}) - \text{FTP Rate}(3\text{M})$$
  - Nhờ TLP, chi nhánh không thể trục lợi bằng cách giải ngân tín dụng dài hạn rồi ngụy trang dưới dạng lãi suất thả nổi.

### 3.2. Chi phí Gánh Đệm Thanh khoản (Liquidity Buffer Carry Cost / HQLA Cost)
- Để thỏa mãn quy định về tỷ lệ đảm bảo khả năng thanh khoản [[lcr|LCR]] $\ge 100\%$ hoặc Thông tư 22/2019/TT-NHNN, ngân hàng buộc phải dự trữ một lượng lớn tài sản có tính thanh khoản cao [[hqla|HQLA]] (Trái phiếu Chính phủ, tiền gửi NHNN) [[src-vab-ftp#^vab-ftp-10]].
- Các tài sản này có lợi suất rất thấp, dẫn đến tình trạng chênh lệch lợi suất âm (**negative carry**) so với chi phí huy động vốn bình quân của ngân hàng.
- Chi phí gánh đệm thanh khoản được lượng hóa và phân bổ đều vào giá bán vốn COF của toàn bộ tài sản sinh lời:
  $$\text{Liquidity Buffer Premium} = \frac{\text{Số dư bình quân TSTK} \times (\text{VOF bình quân} - \text{Lợi suất bình quân TSTK})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$
  [[src-vab-ftp#^vab-ftp-10]]

### 3.3. Chi phí Dự trữ Bắt buộc (DTBB) và Bảo hiểm Tiền gửi (BHTG) tại Việt Nam
Đây là hai khoản chi phí pháp định bắt buộc của Ngân hàng Nhà nước nhưng trực tiếp làm hao mòn lợi nhuận nếu không được phân bổ khoa học:
1. **Chi phí Dự trữ Bắt buộc (Statutory Reserved Cost)**:
   - Ngân hàng phải gửi một tỷ lệ % tiền gửi tại NHNN (ví dụ 3% đối với tiền gửi VND không kỳ hạn và kỳ hạn dưới 12 tháng) với lãi suất tiền gửi DTBB cực thấp (0% hoặc 0,5%/năm) [[src-vab-ftp#^vab-ftp-9]].
   - Chi phí cơ hội này được phân bổ vào biểu giá bán vốn COF:
     $$\text{Chi phí DTBB} = \frac{\text{Số dư DTBB} \times (\text{VOF bình quân} - \text{Lãi suất tiền gửi DTBB})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$
     [[src-vab-ftp#^vab-ftp-9]]
2. **Chi phí Bảo hiểm Tiền gửi (Deposit Insurance Cost)**:
   - Ngân hàng phải đóng phí 0,15%/năm trên tổng số dư tiền gửi của khách hàng cá nhân bằng VND [[src-vab-ftp#^vab-ftp-8]].
   - Cấu phần này không trừ vào đơn vị huy động (để tránh triệt tiêu động lực tìm kiếm người gửi tiền) mà được chuyển giao sòng phẳng sang tính vào giá bán vốn COF của bên cho vay [[src-vab-ftp#^vab-ftp-8]].

### 3.4. Phụ phí Cấu trúc NSFR và Chi phí Hạn mức Dự phòng (Contingent Liquidity)
- **Tỷ lệ nguồn vốn ổn định ròng [[nsfr|NSFR]]**: Đơn vị huy động nguồn vốn dài hạn có hệ số [[available-stable-funding|ASF]] 100% được CFU thưởng thêm biên độ spread VOF; ngược lại tài sản cho vay dài hạn có hệ số [[required-stable-funding|RSF]] cao (85%–100%) bị phạt tăng giá COF [[src-ftp-transmission-analysis#^ftp-trans-8]].
- **Cam kết tín dụng chưa giải ngân (Undrawn Committed Facilities)**: Khi cấp hạn mức thấu chi hoặc bảo lãnh tín dụng chưa rút vốn, ngân hàng phải dự trù thanh khoản dự phòng nếu khách hàng rút tiền trong khủng hoảng (theo [[cash-outflows|dòng tiền ra LCR 10%–40%]]). FTP áp phụ phí cam kết (facility fee / liquidity standby charge) trên phần hạn mức chưa sử dụng.

---

## 4. Trụ Cột 3: Interest Rate Risk in the Banking Book (IRRBB)

Hệ thống FTP là công cụ chủ chốt giải quyết trọn vẹn rủi ro lãi suất trên sổ ngân hàng theo chuẩn mực [[bcbs-irrbb|BCBS d368]] [[src-ftp-transmission-analysis#^ftp-trans-9]]:

### 4.1. Rủi ro Khe hở Tái định giá (Gap Risk / Repricing Risk)
- **Cơ chế Triệt tiêu Rủi ro**: Nhờ nguyên tắc Trùng khớp kỳ hạn (Matched-Maturity Principle), BU được neo giá FTP đối ứng cố định theo đúng kỳ hạn tái định giá của hợp đồng [[src-choudhry-principles-banking#^choudhry-ftp-11]].
  - Khoản vay cố định 3 năm: Được CFU cấp vốn với giá COF cố định 3 năm.
  - Tiền gửi tiết kiệm 1 năm: Được CFU mua lại với giá VOF cố định 1 năm.
- **Kết quả**: BU hoàn toàn không chịu phơi nhiễm với rủi ro tái định giá [[src-ftp-transmission-analysis#^ftp-trans-10]]. Toàn bộ khe hở tái định giá ([[gap-risk]]) được dồn về Trung tâm Quản trị Vốn (CFU). CFU quản trị độ nhạy thu nhập lãi thuần ([[net-interest-income-sensitivity|ΔNII]]) và giá trị kinh tế của vốn chủ sở hữu ([[economic-value-of-equity|ΔEVE]]), sau đó sử dụng các hợp đồng hoán đổi lãi suất [[interest-rate-swap|IRS]] để phòng ngừa tập trung.

### 4.2. Rủi ro Cơ sở (Basis Risk)
- **Bản chất**: Xuất hiện khi tài sản có và tài sản nợ có cùng kỳ hạn tái định giá nhưng thả nổi theo các chỉ số lãi suất cơ sở khác nhau [[bcbs-irrbb]].
  - Ví dụ: Khoản cho vay thả nổi theo "Lãi suất tiết kiệm 12 tháng bình quân của 4 NHTM Nhà nước + 3.5%", trong khi nguồn vốn tài trợ của ngân hàng phải huy động trên thị trường liên ngân hàng neo theo "VNIBOR 3 tháng".
- **Cách FTP xử lý**: FTP áp dụng cấu phần **Phụ phí Cơ sở (Basis Spread Charge)**. CFU tính toán mối tương quan lịch sử giữa hai chỉ số lãi suất, định giá chi phí phòng ngừa rủi ro hoán đổi cơ sở (Basis Swap) và cộng trực tiếp vào giá COF của khoản vay.

### 4.3. Rủi ro Cấu trúc Đường cong Lãi suất (Yield Curve Risk)
Đường cong lợi suất không chỉ dịch chuyển song song mà còn biến đổi hình thái (dốc hơn — steepening, phẳng hơn — flattening, hoặc xoắn — twisting). Hệ thống FTP liên tục cập nhật đường cong không kỳ hạn (Zero-coupon Curve), đảm bảo từng dòng tiền đơn lẻ (cash flow bucketing) ở các thời điểm $t_1, t_2, \dots, t_n$ đều được chiết khấu và định giá tại đúng điểm kỳ hạn tương ứng.

---

## 5. Trụ Cột 4: Optionality & Behavioral Risk (Định Giá Quyền Chọn Ẩn)

Quyền chọn ẩn (Embedded Options) là một trong những nguồn gốc gây tổn thất nặng nề nhất cho bảng cân đối ALM nếu bị bỏ qua trong FTP [[src-ftp-transmission-analysis#^ftp-trans-7]].

```
+---------------------------------------------------------------------------------------------------+
|                  CÁC QUYỀN CHỌN ẨN TRỌNG YẾU ĐƯỢC ĐỊNH GIÁ TRONG HỆ THỐNG FTP                     |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [ QUYỀN TRẢ NỢ TRƯỚC HẠN ]                         [ QUYỀN RÚT TIỀN GỬI TRƯỚC HẠN ]              |
|       (Prepayment Option)                               (Early Withdrawal Option)                 |
|  - Khách hàng thực thi khi: LÃI SUẤT GIẢM          - Khách hàng thực thi khi: LÃI SUẤT TĂNG       |
|  - Rủi ro cho Ngân hàng:                           - Rủi ro cho Ngân hàng:                        |
|    Mất khoản vay lãi suất cao;                       Mất nguồn vốn rẻ, phải huy động              |
|    Dòng tiền trả về phải tái đầu tư ở lãi suất thấp  nguồn vốn mới với lãi suất cao hơn           |
|  - Phương pháp định giá FTP:                       - Phương pháp định giá FTP:                    |
|    Kỳ hạn hiệu lực WAL, mô hình hành vi CPR          Áp dụng phí phạt rút trước hạn (TT 04/2022)  |
|                                                                                                   |
|  [ TIỀN GỬI KHÔNG KỲ HẠN - CASA ]                   [ QUYỀN CHỌN TỰ ĐỘNG - CAPS & FLOORS ]        |
|    (Non-Maturity Deposits - NMDs)                         (Embedded Interest Rate Limits)         |
|  - Khách hàng có quyền rút vốn bất kỳ lúc nào      - Trần (Cap): Khách hàng được bảo vệ trần lãi  |
|  - Ngân hàng áp dụng:                                - Sàn (Floor): Ngân hàng được bảo vệ sàn lãi |
|    Mô hình danh mục sao chép (Replicating)           - Phương pháp định giá FTP:                  |
|    Tách Core CASA (dài hạn) vs Non-core (ngắn hạn)   Mô hình Black-76 / Swaption Volatility Matrix|
+---------------------------------------------------------------------------------------------------+
```

### 5.1. Quyền chọn Trả nợ Trước hạn (Prepayment Option)
- **Hành vi**: Khi lãi suất thị trường hạ nhiệt, khách hàng đi vay có xu hướng trả nợ trước hạn để tái tài trợ ở nơi khác với lãi suất rẻ hơn. Ngân hàng bị hụt dòng thu nhập lãi cao dự kiến và phải tái đầu tư số tiền nhận về ở mức lãi suất thị trường thấp hơn ([[option-risk]]).
- **Phương pháp định giá FTP của EY VietABank**:
  - Không thể dùng kỳ hạn pháp lý (Contractual Maturity) để định giá COF.
  - Áp dụng **Kỳ hạn Hiệu lực (Weighted Average Life — WAL)** dựa trên dòng tiền của Mô hình Hành vi trả nợ trước hạn (CPR — Constant Prepayment Rate) [[src-vab-ftp#^vab-ftp-19]] [[src-vab-ftp#^vab-ftp-20]]:
    $$\text{WAL} = \sum_{t=1}^{N} \frac{t \times \text{CF}_t}{\text{Số dư nợ gốc ban đầu}}$$
  - Giá COF cơ sở được xác định dựa trên kỳ hạn hiệu lực WAL thay vì kỳ hạn danh nghĩa của hợp đồng [[src-vab-ftp#^vab-ftp-19]].
  - Khoản vay có điều khoản cho phép trả trước hạn miễn phí sẽ bị cộng thêm **Phụ phí Quyền chọn Trả trước (Prepayment Option Charge)** tương đương với giá trị của quyền chọn bán sàn lãi suất (receiver swaption).

### 5.2. Quyền chọn Rút Tiền Gửi Trước hạn (Early Withdrawal Option)
- **Hành vi**: Khi lãi suất thị trường tăng vọt, người gửi tiết kiệm có động lực rút tiền trước ngày đáo hạn để chuyển sang gửi kỳ hạn mới với lãi suất cao hơn.
- **Phương pháp định giá FTP**:
  - Tại Việt Nam, theo **Thông tư 04/2022/TT-NHNN**, khách hàng rút một phần tiền gửi trước hạn chỉ bị áp lãi suất không kỳ hạn cho phần rút sớm, phần còn lại vẫn giữ nguyên lãi suất cam kết ban đầu.
  - Cơ chế FTP áp dụng **Chi phí phạt rút trước hạn (Early Redemption Penalty)**: Hồi tố toàn bộ phần chênh lệch VOF mà chi nhánh đã tạm ứng ghi nhận, điều chỉnh giá VOF cơ sở của khoản tiền rút sớm về mức lãi suất VOF không kỳ hạn thông thường [[src-vab-ftp#^vab-ftp-18]].

### 5.3. Định Giá Tiền Gửi Không Kỳ Hạn (CASA — Non-Maturity Deposits)
Tiền gửi không kỳ hạn (CASA) là nguồn vốn rẻ nhất nhưng có tính chất kỳ hạn pháp lý bằng 0 và khách hàng có quyền rút toàn bộ bất cứ lúc nào:
- **Phương pháp Đường cong Hoàn trả (Non-term Redemption Curve) & Danh mục Sao chép (Replicating Portfolio)**:
  - Phân tách số dư CASA thành hai phần độc lập [[src-vab-ftp#^vab-ftp-14]]:
    1. **Non-core CASA (CASA không ổn định)**: Dòng tiền biến động ngắn hạn, được định giá VOF theo kỳ hạn ngắn (1 ngày đến 1 tháng).
    2. **Core CASA (CASA ổn định / lõi)**: Số dư gắn bó lâu dài của khách hàng nhờ thói quen thanh toán, được xem như một nguồn vốn trung dài hạn bền vững [[src-vab-ftp#^vab-ftp-14]].
  - Công thức xác định VOF cơ sở cho CASA của VietABank [[src-vab-ftp#^vab-ftp-15]]:
    $$\text{FTP Base Curve}_{\text{CASA}} = \text{Base Curve}_i \times \text{Non-Core CASA}_i + \text{Base Curve}_j \times (1 - \text{Non-Core CASA}_i)$$
  - Nhờ cơ chế này, chi nhánh huy động được nhiều CASA ổn định sẽ được CFU trả giá VOF rất cao (tương đương lãi suất kỳ hạn 3–5 năm), tạo động lực đột phá để chi nhánh đẩy mạnh mở tài khoản thanh toán và dịch vụ thu hộ chi hộ.

### 5.4. Quyền chọn Tự động: Trần (Cap) và Sàn (Floor) Lãi Suất
Nhiều sản phẩm tín dụng có điều khoản trần/sàn ngầm:
- Ví dụ: Cho vay mua nhà "lãi suất thả nổi nhưng không thấp hơn 8%/năm (Floor) và không vượt quá 14%/năm (Cap)".
- **Định giá FTP**: 
  - Điều khoản Cap là một quyền chọn call option mà ngân hàng bán cho khách hàng $\rightarrow$ BU bị tính **phụ phí Cap Charge**.
  - Điều khoản Floor là một quyền chọn put option mà ngân hàng mua từ khách hàng $\rightarrow$ BU được **hoàn trả Floor Benefit**.
  - Giá trị quyền chọn được tính toán bằng mô hình Black-76 hoặc Ma trận biến động Swaption (Swaption Volatility Matrix) của ALM.

---

## 6. Mở Rộng: Credit Spread & Capital Charge (Tích Hợp Deal-Level RAROC)

Bên cạnh 4 trụ cột rủi ro thanh khoản và thị trường, hệ thống FTP tiên tiến của Beata Lubinska còn tích hợp trực tiếp chi phí rủi ro tín dụng và chi phí phân bổ vốn vào giá bán vốn [[src-ftp-transmission-analysis#^ftp-trans-6]]:

```
+---------------------------------------------------------------------------------------------------+
|                        TÍCH HỢP CHI PHÍ TÍN DỤNG VÀ VỐN VÀO HỆ THỐNG ĐỊNH GIÁ                     |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  1. EXPECTED LOSS CHARGE (Chi phí Tổn thất Kỳ vọng):                                               |
|     - Bù đắp chi phí trích lập dự phòng rủi ro tín dụng thông thường                              |
|     - Công thức lượng hóa: EL = PD × LGD × EAD                                                    |
|                                                                                                   |
|  2. CAPITAL CHARGE (Chi phí Vốn Kinh tế cho Tổn thất Ngoài kỳ vọng):                              |
|     - Bù đắp chi phí vốn chủ sở hữu giữ lại để gánh rủi ro tài sản có hệ số rủi ro cao (RWA)     |
|     - Công thức lượng hóa: Capital Charge = RWA × Capital Ratio × Cost of Equity (CoE)            |
|                                                                                                   |
|  3. ĐO LƯỜNG LỢI NHUẬN ĐIỀU CHỈNH THEO RỦI RO (Deal-Level RAROC):                                 |
|                                                                                                   |
|                      Doanh thu Lãi vay - Giá vốn FTP - EL - Chi phí Vận hành                      |
|           RAROC  =  ---------------------------------------------------------                     |
|                                       Vốn Kinh tế (Economic Capital)                              |
+---------------------------------------------------------------------------------------------------+
```

---

## 7. Bảng Tổng Hợp Ma Trận Các Cấu Phần Định Giá FTP

| Cấu phần | Rủi ro / Chi phí phản ánh | Đối tượng áp dụng | Phương pháp xác định / Công thức | Tác động lên Bảng cân đối |
|:---|:---|:---:|:---|:---|
| **Base Funding Rate** | Chi phí cơ hội của vốn, rủi ro lạm phát & chính sách tiền tệ | Toàn bộ Tài sản có & Tài sản nợ | Đường cong phi rủi ro: VNIBOR, OMO, TPCP (Marginality principle) | Thiết lập giá sàn tham chiếu thị trường |
| **Term Liquidity Premium (TLP)** | Rủi ro thanh khoản kỳ hạn của các cam kết dài hạn | Khoản vay trung dài hạn thả nổi | $\text{FTP Rate}(T_{\text{gốc}}) - \text{FTP Rate}(T_{\text{tái định giá}})$ | Chặn đứng cạm bẫy chuyển đổi kỳ hạn quá mức |
| **Liquidity Buffer Premium** | Khoản lỗ âm khi duy trì đệm [[hqla]] (LCR, TT22) | Tài sản có sinh lời (COF) | $\frac{\text{Số dư TSTK} \times (\text{VOF} - \text{Lãi suất TSTK})}{\text{Tổng tài sản FTP}}$ | Nội bộ hóa chi phí an toàn thanh khoản |
| **Chi phí DTBB & BHTG** | Chi phí tuân thủ pháp lệnh của NHNN | Tài sản có sinh lời (COF) | Phân bổ tỷ lệ chi phí nộp BHTG và tiền gửi DTBB tại NHNN | Tính đúng, tính đủ chi phí pháp định vào lãi suất |
| **IRRBB Gap Adjustment** | Rủi ro khe hở tái định giá lãi suất | Mọi hợp đồng tài sản và nợ | Matched-Maturity Pricing (khóa chặt biên thương mại) | Cách ly IRRBB khỏi chi nhánh, chuyển về Treasury |
| **Basis Spread Charge** | Rủi ro chênh lệch chỉ số tham chiếu lãi suất | Khoản vay thả nổi theo lãi suất phi chuẩn | Chi phí phòng ngừa Basis Swap giữa 2 chỉ số | Ngăn ngừa rủi ro co hẹp biên lãi do lệch chỉ số |
| **Prepayment Charge** | Rủi ro trả nợ trước hạn khi lãi suất giảm | Khoản vay có quyền trả trước | Kỳ hạn hiệu lực WAL từ mô hình CPR; phí phạt trả trước | Bảo vệ ngân hàng khỏi rủi ro tái đầu tư giá rẻ |
| **Early Redemption Penalty** | Rủi ro rút tiền gửi trước hạn khi lãi suất tăng | Tiền gửi có kỳ hạn rút sớm | Hồi tố về lãi suất không kỳ hạn (Thông tư 04/2022/TT-NHNN) | Ngăn ngừa trục lợi và ổn định nguồn vốn tiền gửi |
| **Core CASA Benefit** | Hành vi tiền gửi ổn định của khách hàng phi kỳ hạn | Tiền gửi không kỳ hạn (VOF) | Mô hình danh mục sao chép (Replicating Portfolio) | Khuyến khích chi nhánh tăng trưởng CASA giá rẻ |
| **Embedded Caps/Floors** | Quyền chọn trần/sàn lãi suất ngầm trong hợp đồng | Khoản vay có giới hạn lãi suất | Mô hình định giá quyền chọn Black-76 / Swaption Matrix | Định giá sòng phẳng quyền chọn tài chính cho khách hàng |
| **Capital & EL Charge** | Rủi ro tín dụng và chi phí vốn kinh tế (CAR, LEV) | Khoản vay tín dụng (COF) | $\text{EL} + \text{RWA} \times \text{CAR} \times \text{Cost of Equity}$ | Định hướng tín dụng vào tài sản RAROC cao, ít tốn vốn |

---

## 8. Kết Luận và Khuyến Nghị Thực Tiễn Cho Ủy Ban ALCO

Một hệ thống FTP hoàn thiện chính là **chiếc lăng kính quang phổ** giải mã mọi rủi ro tiềm ẩn trên bảng cân đối của ngân hàng thương mại:
1. **Không bỏ sót rủi ro**: Nếu ngân hàng bỏ qua TLP, ngân hàng sẽ chết vì khủng hoảng thanh khoản; nếu bỏ qua chi phí pháp định, ngân hàng sẽ tự ăn mòn vốn chủ sở hữu; nếu bỏ qua quyền chọn ẩn, ngân hàng sẽ thua lỗ nặng nề trong các chu kỳ đảo chiều lãi suất.
2. **Nguyên tắc sòng phẳng và minh bạch**: Mọi phụ phí (spread) đưa vào hệ thống FTP đều phải có cơ sở tính toán khoa học, dựa trên chi phí phòng ngừa rủi ro thực tế trên thị trường tài chính hoặc chi phí cơ hội tuân thủ quy định pháp luật.
3. **Cơ chế dẫn dắt tối ưu**: Thông qua việc hiệu chỉnh linh hoạt các cấu phần này, Ủy ban ALCO có thể điều khiển toàn bộ mạng lưới chi nhánh hoạt động như một cỗ máy thống nhất, đưa bảng cân đối tài sản - nợ đạt đến điểm cân bằng tối ưu giữa **Khả năng sinh lời (NII/RAROC)** và **An toàn hệ thống (LCR, NSFR, IRRBB, CAR)**.

## Khái niệm và Liên kết
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU.
- [[ftp-pricing-methodology]]: Chi tiết công thức tính toán VOF, COF và phụ phí tuân thủ pháp lệnh tại NHTM Việt Nam.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn điều tiết rủi ro thanh khoản, lãi suất, tín dụng và vốn qua FTP.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa quy hoạch bảng cân đối ALM toàn diện.
- [[ftp-nature-and-balance-sheet-management]]: Bản chất, mục tiêu và 5 vấn nạn ALM kinh điển được FTP giải quyết.
- [[ftp-portfolio-and-bucket-allocation]]: Phương pháp phân bổ giao dịch và sản phẩm vào các danh mục và thang kỳ hạn FTP.
- [[ftp-curve-construction-methodology]]: Phương pháp luận xây dựng đường cong FTP theo kỳ hạn, đồng tiền và loại sản phẩm.
- [[ftp-cost-benefit-allocation-principles]]: Nguyên tắc phân bổ chi phí và lợi ích của từng danh mục FTP cho đơn vị kinh doanh.
- [[ftp-final-rate-determination]]: Xác định mức lãi suất FTP cuối cùng cho từng giao dịch sau khi tính đến tenor, repricing, liquidity và embedded options.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản theo Moorad Choudhry.
- [[synthetic-balance-sheet-liquidity-risk]]: Bảng cân đối thanh khoản tổng hợp và động lực dòng tiền.
- [[practical-alm-liquidity-governance]]: Khung quản trị thanh khoản thực chiến.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.
- [[basis-risk]]: Rủi ro cơ sở giữa các chỉ số lãi suất.
- [[option-risk]]: Rủi ro quyền chọn tự động và hành vi.
- [[non-maturity-deposits]]: Mô hình hóa hành vi tiền gửi không kỳ hạn CASA.
- [[behavioural-options]]: Quyền chọn trả nợ trước hạn và rút tiền gửi sớm.
- [[replicating-portfolio-model]]: Mô hình danh mục sao chép tiền gửi CASA.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[hqla]]: Tài sản thanh khoản chất lượng cao.

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế.
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M2: đã có node [[credit-risk-management]]; TT83 Đ26.2.c yêu cầu nguyên tắc đưa chi phí bù đắp rủi ro tín dụng vào định giá sản phẩm tín dụng theo mức rủi ro khách hàng [[src-tt83-2025-nhnn#^d26-2c]] (văn bản NHNN đầu tiên trong wiki chạm tới pricing tín dụng); cần rà lại mục cấu phần credit spread.
