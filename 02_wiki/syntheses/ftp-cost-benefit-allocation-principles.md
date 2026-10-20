---
title: "Nguyên Tắc Phân Bổ Chi Phí Và Lợi Ích Của Từng FTP Portfolio Cho Đơn Vị Kinh Doanh Và Sản Phẩm"
aliases: [FTP Cost Benefit Allocation Principles, Nguyên tắc phân bổ chi phí lợi ích FTP, P&L Attribution FTP, Phân bổ lợi nhuận FTP, FTP Allocation Principles]
type: synthesis
domains: [alm, product]
status: active
maturity: draft
origin: query
question: "Chi phí/lợi ích của từng FTP portfolio được phân bổ cho các đơn vị kinh doanh hoặc sản phẩm theo nguyên tắc nào?"
sources: ["[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-ftp-transmission-analysis]]", "[[src-tt83-2025-nhnn]]", "[[src-tt50-2026-nhnn]]"]
relations: []
tags: [ftp, cost-allocation, benefit-allocation, pnl-attribution, commercial-margin, treasury-margin, matched-maturity, marginality, synthesis]
updated: 2026-10-20
reviewed:
---

## 1. Tóm Tắt Quản Trị Cấp Cao (Executive Summary)

Trong kỹ trị ALM ngân hàng thương mại hiện đại, câu hỏi cốt tử về việc **phân bổ chi phí và lợi ích của từng Danh mục FTP (FTP Portfolio) cho các Đơn vị kinh doanh (Business Units — BU) và từng Sản phẩm** chính là bản thiết kế của cơ chế hạch toán hiệu quả hoạt động (P&L Attribution) và chuyển giao rủi ro nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-10]].

Bản chất của cơ chế phân bổ này dựa trên nguyên lý nền tảng: **Tách biệt hoàn toàn giữa Thương quyền Khách hàng (Customer Franchise) phi rủi ro thị trường và Hoạt động Chuyển đổi Kỳ hạn (Maturity Transformation) gánh chịu rủi ro** [[src-choudhry-principles-banking#^choudhry-ftp-3]] [[src-choudhry-principles-banking#^choudhry-ftp-13]]:
1. **Đơn vị Kinh doanh (BU)**: Chỉ tập trung phục vụ khách hàng, khai thác thương quyền để thu hút tiền gửi với lãi suất thấp hoặc giải ngân cho vay với lãi suất cao. BU được hưởng một **Biên lợi nhuận thương mại (Commercial Margin) cố định** và hoàn toàn được miễn trừ khỏi biến động rủi ro lãi suất hay rủi ro thanh khoản của thị trường [[src-choudhry-principles-banking#^choudhry-ftp-8]] [[src-ftp-transmission-analysis#^ftp-trans-10]].
2. **Trung tâm Quản lý Vốn (CFU / ALM Treasury)**: Kế thừa toàn bộ trạng thái không khớp kỳ hạn (mismatch), quản trị tập trung rủi ro thanh khoản và rủi ro lãi suất; ghi nhận **Biên lợi nhuận điều hòa vốn (Treasury / CFU Margin)** [[src-vab-ftp#^vab-ftp-2]] [[src-choudhry-principles-banking#^choudhry-ftp-1]].

Hệ thống phân bổ chi phí/lợi ích vận hành trên **6 nguyên tắc kỹ trị bất khả xâm phạm** (Trùng khớp kỳ hạn, Chi phí cơ hội cận biên, Trách nhiệm phân định rủi ro, Người gây rủi ro chịu phí, Hồ điều tiết tập trung, và Định hướng chiến lược ALCO) [[src-choudhry-principles-banking#^choudhry-ftp-11]] [[src-choudhry-principles-banking#^choudhry-ftp-12]].

Đối chiếu NHNN (TT83/2025): Hội đồng [[alco|ALCO]] đề xuất, tham mưu Tổng giám đốc về quản lý tài sản/nợ và họp định kỳ tối thiểu mỗi quý 01 lần [[src-tt83-2025-nhnn#^d6-4b]]. Bộ phận ALM rà soát, đề xuất nguyên tắc xây dựng giá điều chuyển vốn nội bộ và kiểm soát hoạt động kinh doanh tuân thủ hạn mức rủi ro thanh khoản, hạn mức IRRBB [[src-tt83-2025-nhnn#^d25-3]]. Khẩu vị và hạn mức làm căn cứ cho nguyên tắc 6: xem [[risk-appetite]], [[risk-limits]].

```
+---------------------------------------------------------------------------------------------------+
|               SƠ ĐỒ PHÂN BỔ CHI PHÍ VÀ LỢI ÍCH NII THEO HỆ THỐNG FTP TOÀN HÀNG                     |
+---------------------------------------------------------------------------------------------------+
|                                 TỔNG THU NHẬP LÃI THUẦN (NII TOÀN HÀNG)                           |
|                    NII = Thu nhập lãi cho vay khách hàng - Chi phí trả lãi tiền gửi               |
|                                                  │                                                |
|            ┌─────────────────────────────────────┼─────────────────────────────────────┐          |
|            ▼                                     ▼                                     ▼          |
|  [ BIÊN HUY ĐỘNG (BU NỢ) ]             [ BIÊN ALM / CFU ]                   [ BIÊN TÍN DỤNG (BU CÓ) ]|
|  (Liability Commercial Margin)          (Treasury Mismatch Margin)           (Asset Commercial Margin)|
|                                                                                                   |
|  Doanh thu: VOF nhận từ CFU             Doanh thu: COF thu từ BU Có          Doanh thu: Lãi suất KH   |
|  Chi phí: Lãi trả cho KH                Chi phí: VOF trả cho BU Nợ           Chi phí: COF trả cho CFU |
|  ─────────────────────────────          ──────────────────────────           ─────────────────────────|
|  Margin = VOF - Lãi suất KH             Margin = Net COF/VOF ± Hedging P&L   Margin = Lãi suất KH -COF|
|                                                                                                   |
|  [ĐẶC ĐIỂM QUẢN TRỊ]                   [ĐẶC ĐIỂM QUẢN TRỊ]                  [ĐẶC ĐIỂM QUẢN TRỊ]       |
|  - Cố định suốt kỳ hạn                 - Chịu biến động thị trường          - Cố định suốt kỳ hạn     |
|  - Khuyến khích tăng CASA              - Phòng ngừa tập trung bằng IRS      - Phản ánh chất lượng bù  |
|  - Thưởng đệm nguồn vốn                - Quản trị đệm HQLA âm carry           rủi ro tín dụng đối tác |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Sáu Nguyên Tắc Kỹ Trị Chi Phối Phân Bổ Chi Phí & Lợi Ích

Toàn bộ việc phân bổ lợi ích (doanh thu FTP) và chi phí (giá vốn FTP) giữa các đơn vị kinh doanh và các dòng sản phẩm được chi phối bởi 6 nguyên tắc chuẩn mực:

```
+---------------------------------------------------------------------------------------------------+
|                    SÁU NGUYÊN TẮC KỸ TRỊ PHÂN BỔ CHI PHÍ VÀ LỢI ÍCH TRONG FTP                     |
+---------------------------------------------------------------------------------------------------+
|  1. NGUYÊN TẮC TRÙNG KHỚP KỲ HẠN  | Khóa cố định giá FTP theo kỳ hạn/WAL và đồng tiền gốc         |
|     (Matched-Maturity Principle)  | Bảo toàn biên thương mại cho BU trước biến động thị trường    |
|                                   |                                                               |
|  2. CHI PHÍ CƠ HỘI CẬN BIÊN       | Định giá theo chi phí thay thế tại thời điểm giao dịch        |
|     (Marginality Principle)       | Tuyệt đối không trợ cấp chéo từ chi phí bình quân quá khứ     |
|                                   |                                                               |
|  3. TRÁCH NHIỆM PHÂN ĐỊNH RỦI RO  | BU chỉ chịu rủi ro kiểm soát được (khách hàng, tín dụng)      |
|     (Risk Ownership Principle)    | Rủi ro thị trường (thanh khoản, lãi suất) chuyển 100% về CFU  |
|                                   |                                                               |
|  4. NGƯỜI GÂY RỦI RO CHỊU PHÍ     | Sản phẩm dài hạn tiêu hao thanh khoản phải trả TLP            |
|     (User-Pays / Causality)       | Sản phẩm tiêu tốn dự trữ pháp định phải trả DTBB/BHTG/Buffer  |
|                                   |                                                               |
|  5. HỒ ĐIỀU TIẾT TẬP TRUNG        | Mọi dòng tiền mua bán vốn đều qua CFU (Central Pool)          |
|     (Pooling & Netting Principle) | Cấm tuyệt đối các chi nhánh tự giao dịch vốn chéo lẫn nhau    |
|                                   |                                                               |
|  6. ĐỊNH HƯỚNG CHIẾN LƯỢC ALCO    | Hiệu chỉnh ALCO Adjust và Margin để khuyến khích sản phẩm mục |
|     (Incentive Alignment)         | tiêu hoặc hạn chế sản phẩm lệch chuẩn khẩu vị rủi ro          |
+---------------------------------------------------------------------------------------------------+
```

### 2.1. Nguyên Tắc Trùng Khớp Kỳ Hạn (Matched-Maturity Principle)
- Mức giá mua vốn (VOF) và giá bán vốn (COF) được xác định cố định tại thời điểm giao dịch phát sinh dựa trên kỳ hạn danh nghĩa hoặc kỳ hạn hiệu lực bình quân gia quyền (WAL) của sản phẩm [[src-choudhry-principles-banking#^choudhry-ftp-11]].
- Khi lãi suất thị trường biến động trong tương lai, mức giá FTP đã gán cho hợp đồng hiện hữu **không bị thay đổi** (đối với sản phẩm cố định) [[src-choudhry-principles-banking#^choudhry-ftp-8]]. Điều này bảo vệ biên lợi nhuận của chi nhánh khỏi các cú sốc lãi suất bên ngoài.

### 2.2. Nguyên Tắc Chi Phí Cơ Hội Cận Biên (Marginality Principle)
- Chi phí vốn đã phát sinh trong quá khứ của các khoản huy động cũ hoàn toàn không có giá trị đối với việc định giá các khoản tín dụng mới [[src-choudhry-principles-banking#^choudhry-ftp-12]].
- Mọi khoản giải ngân mới và khoản huy động mới đều được định giá dựa trên **chi phí thay thế cận biên (Marginal Cost of Funds)** trên thị trường tài chính tại thời điểm đó.
- Ngăn chặn triệt để hiện tượng **trợ cấp chéo (Cross-subsidisation)**: Không lấy nguồn tiền gửi không kỳ hạn giá rẻ từ quá khứ để tài trợ cho khoản vay dài hạn mới với giá rẻ mạt [[src-choudhry-principles-banking#^choudhry-ftp-9]].

### 2.3. Nguyên Tắc Trách Nhiệm Phân Định Rủi Ro (Risk Ownership & Controllability)
- Chi nhánh chỉ chịu trách nhiệm về các quyết định mà họ trực tiếp kiểm soát: lựa chọn khách hàng, thẩm định uy tín tín dụng, đàm phán lãi suất vay và lãi suất gửi [[src-choudhry-principles-banking#^choudhry-ftp-2]].
- Chi nhánh **không có công cụ và không được phép** đánh cược vào biến động của đường cong lãi suất hay rủi ro thanh khoản toàn hệ thống. Toàn bộ rủi ro này được CFU mua lại sòng phẳng [[src-choudhry-principles-banking#^choudhry-ftp-10]].

### 2.4. Nguyên Tắc Người Gây Ra Rủi Ro Phải Trả Phí (User-Pays / Causality Principle)
- Một sản phẩm tín dụng dài hạn gây áp lực thanh khoản cho bảng cân đối (buộc ngân hàng phải tìm kiếm nguồn vốn dài hạn đắt đỏ và duy trì tỷ lệ NSFR) thì đơn vị giải ngân sản phẩm đó bắt buộc phải trả **Phần bù thanh khoản kỳ hạn (TLP)** [[src-choudhry-principles-banking#^choudhry-ftp-15]].
- Một sản phẩm huy động tạo ra gánh nặng pháp lý (như tiền gửi phải trích lập DTBB tại NHNN hoặc nộp phí bảo hiểm tiền gửi 0,15%) thì chi phí cơ hội đó phải được tính toán và phân bổ sòng phẳng vào hệ thống [[src-vab-ftp#^vab-ftp-9]] [[src-vab-ftp#^vab-ftp-11]].

### 2.5. Nguyên Tắc Hồ Điều Tiết Trung Tâm (Pooling & Netting Principle)
- Toàn bộ nguồn vốn huy động được từ các chi nhánh thặng dư đều phải bán về Trung tâm Vốn (CFU); toàn bộ vốn giải ngân cho các chi nhánh thiếu hụt đều phải mua từ CFU [[src-vab-ftp#^vab-ftp-1]].
- Tuyệt đối cấm cơ chế chi nhánh A tự cho chi nhánh B vay vốn trực tiếp (peer-to-peer funding). Cơ chế hồ tập trung cho phép CFU bù trừ dòng tiền tự nhiên (netting), tối ưu hóa quy mô vốn vay mượn từ thị trường liên ngân hàng và giảm thiểu chi phí giao dịch bên ngoài.

### 2.6. Nguyên Tắc Khuyến Khích Định Hướng Chiến Lược Của ALCO (Incentive Alignment)
- Ủy ban ALCO có quyền hiệu chỉnh các biên độ phụ phí (`ALCO Adjust`) hoặc mức `Margin` hỗ trợ huy động để truyền dẫn chính sách kinh doanh xuống mạng lưới [[src-vab-ftp#^vab-ftp-8]]:
  - Tăng VOF thưởng cho sản phẩm tiền gửi kỳ hạn dài hoặc địa bàn chiến lược.
  - Tăng COF phạt đối với các lĩnh vực tín dụng rủi ro cao hoặc các khoản vay tiêu tốn nhiều vốn tự có (CAR/LEV).

---

## 3. Cơ Chế Phân Bổ Chi Phí Và Lợi Ích Chi Tiết Theo Từng Portfolio

Mỗi Portfolio trên bảng cân đối sở hữu cơ chế phân bổ doanh thu (lợi ích) và chi phí riêng biệt:

```
+---------------------------------------------------------------------------------------------------+
|                    CƠ CHẾ PHÂN BỔ CHI PHÍ & LỢI ÍCH THEO TỪNG FTP PORTFOLIO                       |
+---------------------------------------------------------------------------------------------------+
|  DANH MỤC (PORTFOLIO)    | LỢI ÍCH PHÂN BỔ CHO BU / SẢN PHẨM      | CHI PHÍ PHÂN BỔ CHO BU / SẢN PHẨM     |
+--------------------------+----------------------------------------+---------------------------------------+
|  1. TIỀN GỬI CÓ KỲ HẠN   | Nhận Doanh thu VOF = Số dư × VOF_rate  | Trả Chi phí Lãi thực tế cho khách hàng|
|     (Term Deposits)      | VOF = Base + Margin + ALCO_adj         | Không bị trừ phí DTBB hay BHTG        |
|                          |                                        |                                       |
|  2. TIỀN GỬI KHÔNG KỲ HẠN| Nhận Doanh thu VOF hỗn hợp:            | Trả Chi phí Lãi KKH rất thấp cho KH   |
|     (CASA Portfolio)     | - Non-core CASA hưởng Base O/N         | Toàn bộ thặng dư chênh lệch VOF - Lãi |
|                          | - Core CASA hưởng Base dài hạn (cao)   | được ghi nhận vào NIM của chi nhánh   |
|                          |                                        |                                       |
|  3. TÍN DỤNG DOANH NGHIỆP| Thu Lãi suất Cho vay từ khách hàng     | Trả Chi phí COF = Số dư × COF_rate    |
|     VÀ CÁ NHÂN           | (Lãi suất thỏa thuận theo rủi ro KH)   | COF = Base + Margin + DTBB + BHTG     |
|                          |                                        |       + Buffer + TLP + ALCO_adj       |
|                          |                                        |                                       |
|  4. ĐỆM TÀI SẢN THANH    | Không tính trực tiếp cho BU huy động   | Negative carry (Lỗ cơ hội nắm giữ)    |
|     KHOẢN (HQLA Buffer)  | hay BU tín dụng (loại trừ khỏi mẫu số) | CFU gom lại và phân bổ vào COF của    |
|                          |                                        | toàn bộ tài sản sinh lời qua Buffer   |
|                          |                                        |                                       |
|  5. CAM KẾT NGOẠI BẢNG   | Thu Phí cam kết tín dụng (Commitment   | Trả Phí thanh khoản tiềm tàng cho CFU:|
|     (Undrawn Facilities) | fee) từ khách hàng                     | C × CCF × TSTK_ratio × (VOF - Lợi suất|
|                          |                                        |                                       |
|  6. KHỐI KINH DOANH VỐN  | Doanh thu từ kinh doanh TT2 thực tế    | Trả chi phí vốn TT2 cho CFU:          |
|     (Treasury Trading)   | (kinh doanh trái phiếu, FX, MM)        | Deal-by-deal real-time hoặc VNIBOR 1W |
+---------------------------------------------------------------------------------------------------+
```

---

### 3.1. Phân Bổ Cho Danh Mục Huy Động Vốn (Liability Portfolios)

Đơn vị huy động (chi nhánh bán lẻ hoặc trung tâm KHDN) hoạt động như một **nhà bán buôn vốn** cho Hội sở:

1. **Lợi ích được phân bổ (FTP Benefit / Revenue)**:
   - BU được ghi nhận một khoản thu nhập nội bộ tính bằng:
     $$\text{Thu nhập FTP} = \text{Số dư tiền gửi bình quân} \times \text{Lãi suất Mua vốn (VOF)}$$
   - Trong đó: $\text{VOF} = \text{Base Curve} + \text{Hỗ trợ huy động (Margin)} + \text{Điều chỉnh ALCO}$ [[src-vab-ftp#^vab-ftp-6]].
   - Mức `Margin` được ALCO phê duyệt nhằm đảm bảo bù đắp chi phí hoạt động trực tiếp của mạng lưới chi nhánh (chi phí nhân sự, thuê mặt bằng, khấu hao trang thiết bị) và tạo động lực tăng trưởng nguồn vốn [[src-vab-ftp#^vab-ftp-8]].
2. **Chi phí bị phân bổ**:
   - BU chịu trách nhiệm chi trả chi phí lãi thực tế theo hợp đồng ký kết với người gửi tiền.
   - **Biên lợi nhuận huy động của chi nhánh** được cố định sòng phẳng:
     $$\text{NIM}_{\text{Huy động}} = \text{VOF} - \text{Lãi suất chi trả khách hàng}$$
3. **Cơ chế đặc thù cho Portfolio Tiền gửi Không kỳ hạn (CASA)**:
   - Theo mô hình Danh mục Sao chép (Replicating Portfolio), CFU bóc tách số dư CASA thành 2 phần [[src-vab-ftp#^vab-ftp-14]] [[src-vab-ftp#^vab-ftp-15]]:
     - Phần biến động ngắn hạn (**Non-core**): BU chỉ nhận được VOF kỳ hạn qua đêm (O/N) hoặc 1 tháng.
     - Phần ổn định bền vững (**Core**): BU được nhận VOF kỳ hạn trung dài hạn (ví dụ 1 năm đến 3 năm) với lãi suất rất cao.
   - *Kết quả phân bổ*: Chi nhánh phát triển được nhiều tài khoản lương, tiền gửi thanh toán doanh nghiệp có tính bám dính cao sẽ được ghi nhận lợi nhuận NIM khổng lồ, bù đắp xứng đáng cho nỗ lực phát triển quan hệ khách hàng.

---

### 3.2. Phân Bổ Cho Danh Mục Tín Dụng (Asset Portfolios)

Đơn vị kinh doanh tín dụng hoạt động như một **người sử dụng vốn**:

1. **Doanh thu ghi nhận**:
   - BU trực tiếp thu lãi từ khách hàng vay theo hợp đồng tín dụng.
2. **Chi phí bị phân bổ (FTP Cost Charge)**:
   - BU phải trả chi phí vốn cho CFU theo Biểu giá Bán vốn (COF):
     $$\text{Chi phí FTP} = \text{Dư nợ cho vay bình quân} \times \text{Lãi suất Bán vốn (COF)}$$
   - Cấu trúc COF phân bổ bao gồm toàn bộ các loại chi phí cấu thành [[src-vab-ftp#^vab-ftp-7]]:
     $$\text{COF} = \text{Base Rate} + \text{Margin huy động} + \text{Phụ phí DTBB} + \text{Phụ phí BHTG} + \text{Buffer Premium} + \text{TLP} + \text{ALCO Adjust}$$
3. **Biên lợi nhuận tín dụng của chi nhánh**:
   $$\text{NIM}_{\text{Cho vay}} = \text{Lãi suất cho vay khách hàng} - \text{COF}$$
   - Nếu chi nhánh muốn đạt chỉ tiêu lợi nhuận cao, chi nhánh phải nâng cao năng lực đàm phán thương mại (tăng lãi suất cho vay trên cơ sở phân loại rủi ro tín dụng khách hàng) chứ không thể dựa dẫm vào việc xin cấp vốn giá rẻ từ Hội sở.

---

### 3.3. Phân Bổ Chi Phí Đệm Tài Sản Thanh Khoản (HQLA / Liquidity Buffer Portfolio)

Đây là vấn đề kỹ trị tinh vi nhất trong hệ thống FTP:
1. **Bản chất chi phí cơ hội (Negative Carry)**:
   - Để thỏa mãn danh mục tài sản thanh khoản tại Phụ lục 3 TT22/2019 [[src-vab-ftp#^vab-ftp-43]] (áp dụng chuyển tiếp theo TT50 Đ13.4 [[src-tt50-2026-nhnn#^d13-4]]) hoặc LCR, ngân hàng buộc phải duy trì một danh mục Trái phiếu Chính phủ, tiền gửi NHNN và tiền mặt có lợi suất rất thấp (thường thấp hơn chi phí huy động vốn bình quân) [[src-vab-ftp#^vab-ftp-10]].
2. **Nguyên tắc phân bổ**:
   - **Loại trừ khỏi chi nhánh**: Chi nhánh huy động hay Treasury không bị trừ thu nhập vì việc duy trì đệm thanh khoản này [[src-vab-ftp#^vab-ftp-10]].
   - **Tập hợp và phân bổ về đầu tài sản có**: CFU tính toán tổng số tiền thâm hụt lợi suất của toàn hàng:
     $$\text{Chi phí Negative Carry} = \text{Dư nợ đệm TSTK} \times (\text{Lãi suất VOF bình quân} - \text{Lợi suất bình quân TSTK})$$
   - Chi phí này được chia đều cho tổng tài sản sinh lời thuộc diện tính FTP để cấu thành **Phụ phí Đệm Thanh khoản (Liquidity Buffer Premium)** trong giá bán vốn COF của mọi khoản vay [[src-vab-ftp#^vab-ftp-10]].
   - *Ý nghĩa*: Đơn vị cho vay tạo ra quy mô tài sản khiến ngân hàng phải mở rộng đệm thanh khoản dự phòng thì đơn vị đó phải có nghĩa vụ gánh vác chi phí này thông qua giá vốn đầu vào.

---

### 3.4. Phân Bổ Cho Danh Mục Cam Kết Ngoại Bảng (Off-Balance Sheet Commitments)

- Đối với các hạn mức tín dụng đã cấp nhưng khách hàng chưa rút vốn (Undrawn Commitments) hoặc các cam kết bảo lãnh:
  - Mặc dù dòng tiền chưa xuất hiện trên nội bảng, nhưng theo chuẩn mực LCR, ngân hàng vẫn phải trích lập đệm thanh khoản để dự phòng nguy cơ khách hàng rút vốn ồ ạt [[src-vab-ftp#^vab-ftp-35]]. *Diễn giải:* bản trước dẫn cả TT41/2016, nhưng wiki chưa có nguồn nào cho thấy TT41 đặt nghĩa vụ đệm thanh khoản với cam kết ngoại bảng [cần nguồn]. Tại VN, hệ số rút tiền cho cam kết ngoại bảng trong LCR nằm ở TT50 Phụ lục I (xem [[committed-facilities]]).
  - CFU tính toán và phân bổ trực tiếp một khoản **Phí thanh khoản tiềm tàng** xuống đơn vị quản lý hạn mức tín dụng:
    $$\text{Phí thanh khoản ngoại bảng} = C \times \text{CCF} \times \text{Tỷ lệ dự trữ TSTK} \times (\text{VOF} - \text{Lợi suất TSTK})$$
    [[src-vab-ftp#^vab-ftp-35]]
  - Đơn vị kinh doanh có trách nhiệm thu phí cam kết tín dụng (*commitment fee*) từ khách hàng để bù đắp chi phí bị CFU charge.

---

### 3.5. Phân Bổ Cho Danh Mục Treasury & Thị Trường 2 (Interbank Portfolios)

Khối Quản lý & Kinh doanh Vốn (QL&KDV) hoạt động trên thị trường liên ngân hàng và thị trường vốn:

- **Nguyên tắc phân bổ theo Phương án 1 (Desk-level)**:
  - Từng bộ phận (MM Desk, FX Desk, Bond Desk) mua bán vốn trực tiếp với CFU theo giá khớp thực tế trên thị trường (Deal-by-deal real-time) [[src-vab-ftp#^vab-ftp-36]].
  - Lợi nhuận của từng Desk được đo lường chính xác bằng chênh lệch giữa giá thị trường bên ngoài và giá nội bộ với CFU.
- **Nguyên tắc phân bổ theo Phương án 2 (Net Portfolio - Khối QL&KDV)**:
  - Khối QL&KDV bù trừ ròng trạng thái thặng dư hoặc thiếu hụt vốn của toàn Khối. Bộ phận Điều hòa vốn (MM) đại diện cho cả Khối thực hiện mua bán vốn với CFU theo mức lãi suất VNIBOR kỳ hạn 1 tuần [[src-vab-ftp#^vab-ftp-37]].
  - Khối QL&KDV phải tuân thủ hạn mức trạng thái thanh khoản ròng trong vòng 30 ngày do ALCO phê duyệt.

---

## 4. Khung Báo Cáo Phân Bổ Lợi Nhuận (P&L Attribution Framework)

Để đảm bảo tính minh bạch và cung cấp dữ liệu ra quyết định cho Ban điều hành, hệ thống báo cáo FTP phân bổ lợi nhuận theo **5 cấp độ phân tích** [[src-vab-ftp#^vab-ftp-38]]:

```
+---------------------------------------------------------------------------------------------------+
|                        HỆ THỐNG NĂM CẤP ĐỘ BÁO CÁO PHÂN BỔ LỢI NHUẬN FTP                          |
+---------------------------------------------------------------------------------------------------+
|  CẤP ĐỘ BÁO CÁO          | CHỈ SỐ THEO DÕI CỐT LÕI                | Ý NGHĨA QUẢN TRỊ KỸ TRỊ       |
+--------------------------+----------------------------------------+-------------------------------+
|  1. CẤP TOÀN HÀNG        | Tổng NII = NII_HuyĐộng + NII_ChoVay    | Xác nhận tính cân đối khép    |
|     (Bank-wide P&L)      |            + NII_CFU/Treasury          | kín của toàn bộ bảng cân đối  |
|                          |                                        |                               |
|  2. CẤP ĐƠN VỊ KINH DOANH| NII và NIM của từng Chi nhánh / Khối KD| Xếp hạng hiệu quả kinh doanh  |
|     (Branch / BU Level)  | Tách rõ đóng góp từ nợ vs từ có        | minh bạch, sòng phẳng         |
|                          |                                        |                               |
|  3. CẤP LOẠI SẢN PHẨM    | NIM của từng mã sản phẩm tín dụng      | Nhận diện sản phẩm sinh lời   |
|     (Product Level)      | và sản phẩm tiền gửi tiết kiệm/CASA    | cao vs sản phẩm bào mòn vốn   |
|                          |                                        |                               |
|  4. CẤP ĐỘ KHÁCH HÀNG    | Tổng đóng góp NIM của từng khách hàng  | Phục vụ chính sách định giá   |
|     (Customer Profit)    | lớn hoặc phân khúc khách hàng mục tiêu | trọn gói (Relationship Pricing|
|                          |                                        |                               |
|  5. CẤP ĐỘ NGOẠI LỆ      | So sánh NIM thông thường vs NIM sau    | Giám sát chi phí tài trợ từ   |
|     (Exceptions & Promo) | phê duyệt ngoại lệ / gói vay ưu đãi    | các quyết định của ALCO/TGĐ   |
+---------------------------------------------------------------------------------------------------+
```

### Phương trình Cân Bằng Thu Nhập Lãi Thuần (NII Identity)
Toàn bộ hệ thống phân bổ phải đảm bảo tính toàn vẹn kế toán [[src-vab-ftp#^vab-ftp-39]] [[src-vab-ftp#^vab-ftp-40]]:
$$\sum_{\text{All BUs}} \text{NII}_{\text{Commercial}} + \text{NII}_{\text{CFU/Treasury}} \equiv \text{NII}_{\text{Toàn Hàng Báo Cáo Tài Chính}}$$

Trong đó:
- $\text{NII}_{\text{Commercial}}$ là tổng lợi nhuận từ thương quyền khách hàng được phân bổ cho tất cả các chi nhánh.
- $\text{NII}_{\text{CFU/Treasury}}$ là lợi nhuận từ chuyển đổi kỳ hạn và chênh lệch điều hòa thanh khoản tập trung tại Hội sở.

---

## 5. Ý Nghĩa Kỹ Trị Đối Với Vận Hành Ngân Hàng

Việc áp dụng các nguyên tắc phân bổ chi phí/lợi ích FTP mang lại 3 giá trị chuyển hóa căn bản:
1. **Triệt tiêu văn hóa "tranh công, đổ lỗi"**: Chi nhánh huy động không thể than phiền bị chi nhánh tín dụng ép lãi suất, chi nhánh tín dụng không thể bao biện việc kinh doanh kém hiệu quả là do Hội sở cấp vốn giá đắt. Mọi giao dịch đều được soi chiếu sòng phẳng qua lăng kính giá thị trường.
2. **Khuyến khích hành vi tối ưu bảng cân đối**: Đơn vị kinh doanh tự động hướng tới việc thu hút các dòng tiền gửi ổn định (CASA, tiền gửi kỳ hạn dài) vì nhận được VOF cao; đồng thời cân nhắc kỹ lưỡng khi giải ngân các khoản vay dài hạn thả nổi vì nhận thức rõ gánh nặng chi phí TLP và đệm thanh khoản.
3. **Cung cấp cơ sở khoa học cho cơ chế khoán tài chính (KPIs) và RAROC**: Hiệu quả kinh doanh của từng giám đốc chi nhánh và từng cán bộ quan hệ khách hàng (RM) được đánh giá dựa trên lợi nhuận thuần túy từ thương quyền khách hàng sau khi đã trừ đi đầy đủ chi phí rủi ro thanh khoản, rủi ro lãi suất và chi phí vốn kinh tế [[src-ftp-transmission-analysis#^ftp-trans-11]] [[src-ftp-transmission-analysis#^ftp-trans-12]].

Đối chiếu NHNN (TT83/2025): [[raroc|RAROC]] là tỷ lệ phần trăm giữa tổng lợi nhuận trước thuế và [[economic-capital|vốn kinh tế]] [[src-tt83-2025-nhnn#^pl6-iii]]. Kiểm tra sức chịu đựng về vốn phải tính tác động của giả định lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; xem [[icaap]], [[rwa-irrbb]].

Phân bổ lợi ích funding từ vốn chủ sở hữu (Choudhry, T4):
- Vốn cổ phần không có chi phí lãi thực nhưng có chi phí quy đổi là RoE mục tiêu; không gán chi phí này thì vốn thành 'free capital' cho mảng kinh doanh và SVA bị báo sai [[src-choudhry-principles-banking#^choudhry-capm-11]].
- Best practice là giao lợi ích của nguồn vốn 'free' cho central ALCO book; thực tế vốn thường nằm trong Treasury book và nhập pool funding do Treasury quản lý [[src-choudhry-principles-banking#^choudhry-capm-12]]. Lợi ích lãi ròng này chịu cùng quy tắc FTP như mọi nguồn funding; lợi nhuận giữ lại xử lý nhất quán với vốn cổ phần [[src-choudhry-principles-banking#^choudhry-capm-13]].
- Case UBS (2008): lãnh đạo không phát hiện lỗi trong cơ chế funding nội bộ cho phép mảng structured credit ghi nhận lợi nhuận giả tạo (artificial profits); Choudhry kết luận giá chuyển vốn từ Treasury phải phản ánh đúng rủi ro thanh khoản của từng mảng [[src-choudhry-principles-banking#^choudhry-gov-12]]. Xem [[funds-transfer-pricing]].

## Khái niệm và Liên kết
- [[ftp-final-rate-determination]]: Xác định mức lãi suất FTP rate cuối cùng cho từng giao dịch và sản phẩm.
- [[ftp-economic-cost-and-incentive-validation]]: Kiểm tra tính phản ánh economic cost và cơ chế định hướng incentive của hệ thống FTP.
- [[ftp-portfolio-and-bucket-allocation]]: Phương pháp phân bổ giao dịch và sản phẩm vào các danh mục và thang kỳ hạn FTP.
- [[ftp-curve-construction-methodology]]: Phương pháp luận xây dựng đường cong FTP theo kỳ hạn, đồng tiền và loại sản phẩm.
- [[src-lubinska-alm-optimisation]]: Chuyên khảo về tối ưu hóa ALM, Target Operating Model FTP, khuyến nghị PRA và Incentive Premium.
- [[ftp-risk-and-cost-components]]: Các cấu phần rủi ro và chi phí trong định giá FTP.
- [[ftp-pricing-methodology]]: Chi tiết công thức tính toán VOF, COF và phụ phí tuân thủ ngân hàng.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn điều tiết rủi ro thanh khoản, lãi suất và tín dụng của FTP.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU qua FTP.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa quy hoạch bảng cân đối ALM toàn diện.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản theo Moorad Choudhry.
- [[synthetic-balance-sheet-liquidity-risk]]: Bảng cân đối thanh khoản tổng hợp và động lực dòng tiền.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[non-maturity-deposits]]: Mô hình hóa hành vi tiền gửi không kỳ hạn CASA.
- [[behavioural-options]]: Quyền chọn trả nợ trước hạn và rút tiền gửi sớm.

## Căn cứ pháp lý VN của đệm thanh khoản (rà 2026-10-20)
- VAB dẫn TT22/2019 cho phần bù tài sản thanh khoản [[src-vab-ftp#^vab-ftp-10]], cho danh mục tài sản thanh khoản (Phụ lục 3 TT22) [[src-vab-ftp#^vab-ftp-43]] và cho tỷ lệ rút tiền KKH tối thiểu 15% khi chưa có mô hình hành vi [[src-vab-ftp#^vab-ftp-44]].
- TT50/2026 sửa Điều 2 TT22: đối tượng của TT22 chỉ còn ngân hàng hợp tác xã và NHTM đang thực hiện Đ23.3 TT41/2016 [[src-tt50-2026-nhnn#^d37-3a]].
- Từ khi TT50 có hiệu lực đến trước ngày áp dụng LCR/NSFR, ngân hàng vẫn phải tuân thủ và báo cáo tỷ lệ dự trữ thanh khoản, tỷ lệ khả năng chi trả 30 ngày, tỷ lệ nguồn vốn ngắn hạn cho vay trung dài hạn và LDR theo TT22 [[src-tt50-2026-nhnn#^d13-4]].
- Từ 01/10/2028 ngân hàng phải áp dụng LCR và NSFR [[src-tt50-2026-nhnn#^d13-1]]; khi đó các tỷ lệ cũ của TT22 không phải tuân thủ nhưng vẫn phải báo cáo [[src-tt50-2026-nhnn#^d13-5]].

*Diễn giải:* trong synthesis này, "TT22" đọc là căn cứ chuyển tiếp theo TT50 Đ13.4. Sau khi ngân hàng áp dụng LCR, đệm thanh khoản trong phần bù FTP nên đo theo [[hqla]] của TT50, và tỷ lệ rút KKH 15% (dẫn từ Phụ lục 3 TT22) mất tính bắt buộc; ngân hàng cần căn cứ khác (mô hình hành vi hoặc hệ số rút tiền của TT50) [cần nguồn: src-tt50-2026-nhnn PL1 cho hệ số rút tiền tiền gửi KKH].

## Bất định
- [2026-10-20] ingest src-tt50-2026-nhnn PL2: [[available-stable-funding]], [[required-stable-funding]], [[nsfr]] có hệ số ASF/RSF của VN (khác Basel: tiền gửi bán lẻ ≥ 1 năm được rút trước hạn chỉ 95%/90%; phải đòi Chính phủ/KBNN RSF 50–65%; add-on nợ phái sinh 10%); cần rà lại các ví dụ tính NSFR và bảng hệ số.
- [2026-10-20] ingest src-tt50-2026-nhnn PL1: [[lcr]], [[hqla]], [[cash-outflows]], [[retail-deposit-stability]], [[level-1-assets]], [[level-2-assets]] có hệ số VN (HQLA cấp 1/2A/2B 100/85/75–50%, run-off bán lẻ 5%/10%, tiền gửi ngoại tệ luôn kém ổn định, DNNVV ≤ 30 tỷ đồng, cổ phiếu VN30 vào cấp 2B); cần rà lại ví dụ tính LCR và bảng hệ số.

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
