---
title: "Phương Pháp Luận Định Giá Điều Chuyển Vốn Nội Bộ (FTP Pricing Methodology)"
aliases: [FTP Pricing Methodology, Phương pháp luận FTP, Cơ chế định giá VOF COF, FTP VOF COF, Định giá điều chuyển vốn ngân hàng]
type: model
domains: [alm, product]
status: active
maturity: draft
sources: ["[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: priced-by, to: "[[lcr]]", cite: "[[src-vab-ftp#^vab-ftp-10]]"}
  - {type: input-to, to: "[[ftp-transmission-mechanism]]", cite: "[[src-vab-ftp#^vab-ftp-5]]"}
tags: [ftp, vof, cof, pricing-methodology, statutory-reserves, deposit-insurance, tlp, casa, embedded-options, concept]
updated: 2026-10-19
reviewed:
---

## Mục tiêu

### 1. Kiến Trúc Hai Chiều: Giá Mua Vốn (VOF) và Giá Bán Vốn (COF)

Trong mô hình quản trị vốn nội bộ của các Ngân hàng Thương mại Việt Nam (theo tư vấn chuẩn mực của EY và thông lệ quốc tế), hệ thống FTP vận hành cơ chế định giá hai chiều thông qua Trung tâm Quản lý Vốn (CFU/ALM) nhằm điều tiết toàn diện dòng tiền trên bảng cân đối [[src-vab-ftp#^vab-ftp-1]] [[src-vab-ftp#^vab-ftp-2]]:

```
+---------------------------------------------------------------------------------------------------+
|                     KIẾN TRÚC ĐỊNH GIÁ ĐIỀU CHUYỂN VỐN NỘI BỘ (VOF & COF)                         |
+---------------------------------------------------------------------------------------------------+
|  [ĐƠN VỊ HUY ĐỘNG VỐN]                  [TRUNG TÂM QUẢN LÝ VỐN]              [ĐƠN VỊ SỬ DỤNG VỐN] |
|   (Liability Centers)                         (CFU / ALM)                      (Asset Centers)    |
|                                                                                                   |
|   +-------------------+                     +---------------+                 +-----------------+ |
|   |  Tiền gửi KKH     | -- Bán vốn (VOF) -> |  TRUNG TÂM    | - Mua vốn (COF)->| Cho vay KHDN    | |
|   |  Tiền gửi CKH     |                     |  ĐIỀU PHỐI    |                 | Cho vay KHCN    | |
|   |  Giấy tờ có giá   | <- Nhận VOF rate -- |   VỐN TẬP     | <- Trả COF rate- | Đầu tư TPCP, TPDN|
|   +-------------------+                     |    TRUNG      |                 +-----------------+ |
|                                             +---------------+                                     |
|   Biểu giá Mua vốn (VOF):                                          Biểu giá Bán vốn (COF):        |
|   = Base Curve                                                    = Base Curve                    |
|   + Margin (Hỗ trợ huy động)                                      + Margin (Hỗ trợ huy động)      |
|   + ALCO Adjust                                                   + Chi phí Dự trữ Bắt buộc       |
|                                                                   + Chi phí Bảo hiểm Tiền gửi     |
|                                                                   + Liquidity Premium (Đệm TSTK)  |
|                                                                   + Term Liquidity Premium (TLP)  |
|                                                                   + ALCO Adjust                   |
+---------------------------------------------------------------------------------------------------+
```

---

## Công thức

### 2. Cấu Phần Biểu Giá Mua Vốn (VOF — Value of Funds)

Biểu giá mua vốn áp dụng cho toàn bộ các sản phẩm huy động nguồn vốn từ khách hàng trên Thị trường 1 [[src-vab-ftp#^vab-ftp-6]]:

$$\text{VOF}(T) = \text{Base Curve}(T) + \text{Margin}_{\text{Huy động}} + \text{ALCO Adjust}_{\text{Liabilities}}$$

1. **Lãi suất FTP cơ sở (Base Curve)**:
   - Đại diện cho chi phí cơ hội của nguồn vốn theo từng kỳ hạn huy động $T$.
   - Đối với VND: Neo theo lãi suất huy động bình quân toàn hệ thống hoặc đường cong lợi suất trái phiếu chính phủ / VNIBOR có điều chỉnh kỳ hạn.
   - Đối với USD và ngoại tệ khác: Neo theo SOFR / lãi suất thị trường quốc tế hoặc chính sách điều hành ngoại hối của NHNN.
2. **Hỗ trợ huy động (Margin)**:
   - Khoản biên độ cộng thêm do ALCO quyết định nhằm điều chuyển một phần lợi nhuận từ các đơn vị sử dụng vốn sang đơn vị huy động vốn, tạo động lực cạnh tranh phát triển mạng lưới tiền gửi.
3. **Điều chỉnh của ALCO cho tài sản nợ (ALCO Adjust)**:
   - Công cụ điều tiết chính sách linh hoạt: tăng mạnh cho các kỳ hạn mà ngân hàng đang thiếu hụt nguồn vốn ổn định để đáp ứng [[nsfr|NSFR]], hoặc giảm tại các kỳ hạn ngân hàng đang dư thừa thanh khoản.

---

### 3. Cấu Phần Biểu Giá Bán Vốn ([[cost-of-funds|COF — Cost of Funds]])

Biểu giá bán vốn áp dụng cho các tài sản sinh lời (cho vay, đầu tư) của ngân hàng [[src-vab-ftp#^vab-ftp-7]]:

$$\text{COF}(T) = \text{Base Curve}(T) + \text{Margin} + \text{Phụ phí Pháp định (DTBB + BHTG)} + \text{Liquidity Premium} + \text{TLP} + \text{ALCO Adjust}_{\text{Assets}}$$

Nguyên tắc quản trị hiện đại đòi hỏi **đơn vị sử dụng vốn phải chi trả toàn bộ chi phí vốn đầu vào, chi phí duy trì thanh khoản và các chi phí tuân thủ pháp luật mà tài sản đó gây ra cho hệ thống** [[src-vab-ftp#^vab-ftp-5]].

---

### 4. Phương Pháp Định Lượng Chi Phí Tuân Thủ Pháp Định NHNN

#### 4.1 Chi Phí Dự Trữ Bắt Buộc (Statutory Reserved Cost)
Theo quy định của Ngân hàng Nhà nước (Thông tư 30/2019/TT-NHNN), ngân hàng thương mại bắt buộc phải duy trì một tỷ lệ dự trữ bắt buộc trên tài khoản tiền gửi tại NHNN [[src-vab-ftp#^vab-ftp-9]]:
- Số tiền gửi dự trữ này chỉ được hưởng mức lãi suất rất thấp (hoặc 0%), tạo ra khoản chênh lệch lỗ (cost of negative carry) so với chi phí huy động bình quân.
- Chi phí này được CFU tính toán và phân bổ đều vào giá bán vốn COF của tất cả các tài sản thuộc đối tượng tính FTP:

$$\text{Tỷ lệ Chi phí DTBB} = \frac{\text{Số dư DTBB bình quân 3 tháng} \times (\text{VOF bình quân} - \text{Lãi suất tiền gửi DTBB tại NHNN})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

Trong đó:
- $\text{VOF bình quân}$: Lãi suất mua vốn thực tế bình quân của tất cả các kỳ hạn trên Thị trường 1.
- $\text{Tổng tài sản bị tính FTP} = \text{Tổng tài sản} - \text{Tài sản thanh khoản đệm} - \text{Tài sản Thị trường 2 (Treasury)} - \text{Tài sản cố định}$.

#### 4.2 Chi Phí Bảo Hiểm Tiền Gửi (Deposit Insurance Cost)
Theo Luật Bảo hiểm Tiền gửi và hướng dẫn của NHNN, ngân hàng phải thanh toán phí bảo hiểm định kỳ cho tổ chức Bảo hiểm Tiền gửi Việt Nam (BHTGVN) với tỷ lệ cố định **0,15%/năm tính trên số dư tiền gửi VND của khách hàng cá nhân** [[src-vab-ftp#^vab-ftp-8]]:
- Thay vì trừ trực tiếp vào thu nhập của chi nhánh huy động (sẽ làm triệt tiêu động lực huy động tiền gửi cá nhân), chi phí này được Hội sở quy đổi và **phân bổ vào giá COF của bên sử dụng vốn**:

$$\text{Tỷ lệ Chi phí BHTG} = \frac{\text{Tổng chi phí BHTG thực tế 3 tháng quy đổi năm}}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

---

### 5. Phần Bù Tài Sản Thanh Khoản và Phần Bù Thanh Khoản Kỳ Hạn (TLP)

#### 5.1 Phần Bù cho Tài Sản Thanh Khoản (Liquidity Buffer Premium)
Để tuân thủ tỷ lệ dự trữ thanh khoản theo Thông tư 22/2019/TT-NHNN và chuẩn mực quốc tế [[lcr|LCR]], ngân hàng phải nắm giữ một đệm tài sản thanh khoản cao (trái phiếu chính phủ, tín phiếu NHNN) [[src-vab-ftp#^vab-ftp-10]].
- Lợi suất đầu tư của danh mục này thường thấp hơn chi phí huy động vốn thương mại (negative carry).
- Khoản chi phí duy trì đệm an toàn này được phân bổ vào biểu giá COF áp dụng đồng nhất cho mọi kỳ hạn:

$$\text{Liquidity Premium} = \frac{\text{Số dư bình quân TSTK} \times (\text{VOF bình quân} - \text{Lãi suất bình quân danh mục TSTK})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

#### 5.2 Phần Bù Thanh Khoản Kỳ Hạn (Term Liquidity Premium — TLP)
Phần bù thanh khoản kỳ hạn là cấu phần đặc thù **chỉ áp dụng cho các khoản vay có lãi suất thả nổi** [[src-vab-ftp#^vab-ftp-11]] [[src-vab-ftp#^vab-ftp-12]]:

- **Vấn đề bản chất**: Một khoản vay kỳ hạn 5 năm nhưng lãi suất thả nổi điều chỉnh 3 tháng một lần (floating rate loan) chỉ chịu rủi ro lãi suất ngắn hạn 3 tháng, nhưng lại **khóa chặt rủi ro thanh khoản của ngân hàng suốt 5 năm**. Nếu chỉ tính giá COF theo kỳ hạn 3 tháng, ngân hàng sẽ định giá thiếu trầm trọng chi phí thanh khoản dài hạn.
- **Công thức tính TLP**:
  $$\text{TLP} = \text{Lãi suất FTP cơ sở kỳ hạn gốc (5 năm)} - \text{Lãi suất FTP cơ sở kỳ hạn tái định giá (3 tháng)}$$
- Khi bổ sung TLP, tổng lãi suất FTP mà khoản vay thả nổi phải gánh sẽ bằng đúng chi phí thanh khoản của khoản vay cố định có cùng kỳ hạn hợp đồng.

---

## Inputs & giả định

### 6. Mô Hình Hóa Sản Phẩm Phi Kỳ Hạn — Đường Cong Hoàn Trả Tiền Gửi CASA (Non-term Redemption Curve)

Tiền gửi không kỳ hạn (CASA) có đặc tính pháp lý là khách hàng có thể rút tiền bất kỳ lúc nào, nhưng về mặt hành vi tổng thể, một tỷ lệ lớn tiền gửi luôn duy trì bền vững trong hệ thống [[src-vab-ftp#^vab-ftp-13]]. 

```
                                      TỔNG SỐ DƯ TIỀN GỬI CASA
                                                 |
                       +-------------------------+-------------------------+
                       |                                                   |
                       v                                                   v
        [NON-CORE CASA — BIẾN ĐỘNG]                              [CORE CASA — BỀN VỮNG]
        - Tỷ lệ rút vốn ngắn hạn (vd 20%-30%)                   - Số dư lõi ổn định lâu dài (vd 70%-80%)
        - Tài trợ tài sản thanh khoản ngắn hạn                  - Tài trợ danh mục cho vay trung dài hạn
        - Hưởng giá VOF kỳ hạn ngắn (1M-3M)                     - Hưởng giá VOF kỳ hạn dài (1Y-3Y)
```

VietABank áp dụng phương pháp **Đường cong hoàn trả (Redemption Curve)** để xác định giá mua vốn VOF cơ sở thông qua danh mục sao chép (replicating portfolio) [[src-vab-ftp#^vab-ftp-14]]:

$$\text{Base Curve}_{\text{CASA}} = \text{Base Curve}_i \times \text{Non-CoreCasa}_i + \text{Base Curve}_j \times (1 - \text{Non-CoreCasa}_i)$$
[[src-vab-ftp#^vab-ftp-15]]

Trong đó:
- $\text{Non-CoreCasa}_i$: Tỷ lệ tiền gửi CASA không ổn định (biến động ngắn hạn) do mô hình hành vi ước lượng theo từng khối kinh doanh.
- $\text{Base Curve}_i$: Lãi suất FTP cơ sở tương ứng với kỳ hạn ngắn hạn $i$ (ví dụ qua đêm hoặc 1 tháng).
- $\text{Base Curve}_j$: Lãi suất FTP cơ sở tương ứng với kỳ hạn ổn định dài hạn $j$ (ví dụ 1 năm đến 3 năm).

Trong trường hợp ngân hàng chưa hoàn thiện mô hình hành vi kinh tế lượng, áp dụng công thức phân bổ thận trọng theo quy định NHNN (với tỷ lệ rút tiền tối thiểu 15%) [[src-vab-ftp#^vab-ftp-16]]:

$$\text{VOF} = \text{VOF}_{\text{KKH}} \times a\% + \text{VOF}_{\text{CKH}} \times (1 - a\%)$$

Cơ chế này khuyến khích các chi nhánh tích cực tăng trưởng tiền gửi CASA vì chi nhánh được nhận mức giá VOF hấp dẫn của nguồn vốn dài hạn cho phần số dư tiền gửi lõi ổn định.

---

### 7. Định Giá Sản Phẩm Chứa Quyền Chọn Ẩn (Embedded Options Pricing)

Hành vi tài chính của khách hàng thường tạo ra các quyền chọn ẩn (embedded options) gây rủi ro cho ngân hàng [[src-vab-ftp#^vab-ftp-17]]:

#### 7.1 Quyền Chọn Trả Nợ Trước Hạn Khoản Vay (Prepayment Option)
Khi khách hàng trả nợ trước hạn (đặc biệt khi lãi suất thị trường giảm), ngân hàng bị thất thu lãi và đối mặt với rủi ro tái đầu tư với lãi suất thấp hơn:
- Áp dụng mô hình hành vi trả trước hạn (prepayment behavior model) để ước lượng dòng tiền thực tế và tính toán lại **kỳ hạn hiệu lực bình quân gia quyền (Weighted Average Life — WAL)** của khoản vay thay vì kỳ hạn pháp lý trên hợp đồng [[src-vab-ftp#^vab-ftp-19]] [[src-vab-ftp#^vab-ftp-20]]:
  $$\text{Kỳ hạn hiệu lực} = \frac{\sum_{i=1}^N P_i \times T_i}{\sum_{i=1}^N P_i}$$
- Giá COF được áp theo kỳ hạn hiệu lực thực tế này, kết hợp với phí phạt trả nợ trước hạn được phân bổ bù đắp chi phí cho ALM.

#### 7.2 Rút Tiền Gửi Có Kỳ Hạn Trước Ngày Đáo Hạn (Early Redemption)
Khách hàng cá nhân tại Việt Nam có quyền tất toán sổ tiết kiệm trước hạn (theo Thông tư 04/2022/TT-NHNN):
- Ngân hàng áp dụng cơ chế hồi tố lãi suất về mức lãi suất không kỳ hạn đối với phần rút trước hạn [[src-vab-ftp#^vab-ftp-18]], đồng thời đơn vị huy động chỉ được ghi nhận VOF theo kỳ hạn thực gửi, đảm bảo CFU không bị thâm hụt chi phí vốn.

#### 7.3 Phương Pháp FTP Behaviouralisation & Chi Phí Thanh Khoản Dự Phòng (Beata Lubinska)
Theo Beata Lubinska (2020), hệ thống FTP hiện đại phải tích hợp toàn diện phương pháp luận hành vi (FTP behaviouralisation) nhằm nắm bắt đồng thời cả rủi ro lãi suất và chi phí/giá trị thanh khoản của sản phẩm [[src-lubinska-alm-optimisation#^lubinska-u04-2]]:
- **Tách hồ sơ lãi suất CASA**: Hồ sơ lãi suất CASA luôn bao gồm hai cấu phần: phần biến động được mô hình hóa tái định giá trên cơ sở qua đêm (O/N) theo chuẩn BCBS d368, và phần ổn định được coi là nhạy cảm theo thị trường hoặc phần lõi phi nhạy cảm lãi suất đóng vai trò nguồn tài trợ dài hạn lãi suất 0% [[src-lubinska-alm-optimisation#^lubinska-u04-1]].
- **Phân bổ chi phí thanh khoản dự phòng (Contingent Liquidity Cost)**: Nắm giữ đệm thanh khoản bảo vệ ngân hàng trước dòng tiền rút bất ngờ trong kịch bản căng thẳng là rất tốn kém (do chi phí vốn tài trợ cho đệm thường vượt quá lợi suất sinh lời của tài sản thanh khoản) [[src-lubinska-alm-optimisation#^lubinska-u04-3]]. Chi phí dự phòng này bắt buộc phải được tính gộp vào tỷ lệ FTP và phân bổ trực tiếp cho các mảng kinh doanh tại thời điểm giải ngân giao dịch nhằm ngăn ngừa việc định giá thấp chi phí tài trợ [[src-lubinska-alm-optimisation#^lubinska-u04-2]] [[src-lubinska-alm-optimisation#^lubinska-u04-3]].

---

## Output & usage

### 8. Phân Tách Giữa Thị Trường 1 và Thị Trường 2

Hệ thống FTP thiết lập ranh giới rõ ràng giữa hai thị trường:
- **Thị trường 1 (Retail & Corporate Banking)**: Áp dụng cơ chế định giá VOF/COF bán buôn nội bộ theo biểu công bố định kỳ (tháng/quý) do ALCO phê duyệt để thúc đẩy các mục tiêu kinh doanh chi nhánh.
- **Thị trường 2 (Treasury / Interbank Market)**: Áp dụng định giá theo từng giao dịch cụ thể (deal-by-deal pricing) bám sát lãi suất liên ngân hàng thời gian thực, phục vụ quản lý trạng thái thanh khoản tức thời và danh mục đầu tư kinh doanh của Hội sở.

## Khái niệm và Liên kết
- [[credit-risk-management]]: TT83/2025 Đ26.2.c yêu cầu nguyên tắc đưa chi phí bù đắp rủi ro tín dụng vào định giá sản phẩm tín dụng [[src-tt83-2025-nhnn#^d26-2c]].
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn FTP điều tiết rủi ro thanh khoản, lãi suất và tín dụng.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa bảng cân đối ALM toàn diện.
- [[ftp-risk-and-cost-components]]: Các cấu phần rủi ro và chi phí trong định giá FTP.
- [[ftp-curve-construction-methodology]]: Phương pháp luận xây dựng đường cong FTP theo kỳ hạn, đồng tiền và loại sản phẩm.
- [[ftp-portfolio-and-bucket-allocation]]: Phân bổ giao dịch và sản phẩm vào các danh mục và thang kỳ hạn FTP.
- [[ftp-cost-benefit-allocation-principles]]: Nguyên tắc phân bổ chi phí và lợi ích của từng FTP portfolio cho các đơn vị kinh doanh và sản phẩm.
- [[ftp-final-rate-determination]]: Xác định mức lãi suất FTP cuối cùng cho từng giao dịch sau khi tính đến tenor, repricing, liquidity và embedded options.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ qua FTP.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản tổng quát.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.
