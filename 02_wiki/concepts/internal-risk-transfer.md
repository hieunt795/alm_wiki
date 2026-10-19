---
title: "Cơ Chế Chuyển Giao Rủi Ro Nội Bộ Qua FTP (Internal Risk Transfer)"
aliases: [Internal Risk Transfer, Cơ chế chuyển giao rủi ro nội bộ, FTP Risk Transfer, Chuyển giao rủi ro qua FTP]
type: concept
domains: [alm, product]
status: active
maturity: canonical
sources: ["[[src-choudhry-principles-banking]]", "[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]"]
relations:
  - {type: input-to, to: "[[ftp-pricing-methodology]]", cite: "[[src-vab-ftp#^vab-ftp-5]]"}
  - {type: input-to, to: "[[ftp-transmission-mechanism]]", cite: "[[src-ftp-transmission-analysis#^ftp-trans-2]]"}
  - {type: priced-by, to: "[[liquidity-transfer-pricing]]", cite: "[[src-choudhry-principles-banking#^choudhry-ftp-6]]"}
tags: [ftp, internal-risk-transfer, alm, treasury, cfu, bu, matched-maturity, nim-decomposition, concept]
updated: 2026-10-17
reviewed:
---

## 1. Bản Chất Cốt Tử: Hợp Đồng Chuyển Giao Rủi Ro Nội Bộ

Trong kỹ trị ngân hàng thương mại hiện đại, **Funds Transfer Pricing (FTP) không phải là việc phòng ngừa rủi ro ra bên ngoài thị trường, cũng không phải là việc điều chuyển vật lý các dòng tiền tệ; bản chất cốt tử của FTP là cơ chế chuyển giao rủi ro nội bộ (Internal Transfer of Risk)** [[src-choudhry-principles-banking#^choudhry-ftp-10]].

Hệ thống FTP tạo ra một thị trường vốn nội bộ (Internal Capital Market) đóng vai trò là chiếc cầu nối phân định ranh giới giữa hai cấu phần:
1. **Thương quyền khách hàng (Customer Franchise)**: Năng lực của các Đơn vị Kinh doanh (BU — Chi nhánh, Khối KHDN, Khối KHCN) trong việc tìm kiếm khách hàng, đàm phán mức lãi suất hấp dẫn hơn lãi suất thị trường vốn [[src-choudhry-principles-banking#^choudhry-ftp-2]].
2. **Chuyển đổi kỳ hạn rủi ro (Risky Maturity Transformation)**: Hoạt động trung gian tài chính tạo ra lợi nhuận từ sự lệch pha về cấu trúc thời hạn giữa tài sản có và nợ phải trả [[src-choudhry-principles-banking#^choudhry-ftp-1]].

Ranh giới phân tách dứt khoát giữa hai cấu phần này chính là hệ thống FTP [[src-choudhry-principles-banking#^choudhry-ftp-3]]. Thông qua FTP, **BU chuyển giao (bán lại) toàn bộ các rủi ro thị trường và thanh khoản cho Trung tâm Quản lý Vốn (CFU/Treasury) để đổi lấy một biên lợi nhuận thương mại cố định và hoàn toàn phi rủi ro thị trường** [[src-choudhry-principles-banking#^choudhry-ftp-8]].

```
+---------------------------------------------------------------------------------------------------+
|                        MÔ HÌNH HAI LỚP HỢP ĐỒNG TRONG HỆ THỐNG FTP                                |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [KHÁCH HÀNG NGOÀI THỊ TRƯỜNG]      [ĐƠN VỊ KINH DOANH - BU]              [TRUNG TÂM QUẢN LÝ VỐN] |
|                                     (Chi nhánh / Sales)                         (CFU / ALM)       |
|                                                                                                   |
|  1. HUY ĐỘNG TIỀN GỬI:                                                                            |
|     +---------------+                                                    +---------------------+  |
|     |  Khách Gửi    | ==(Lớp 1: Hợp đồng thật)==> [ Chi nhánh A ]        |                     |  |
|     |  Tiền 3 Tháng | <--(Trả lãi 4.0%)----------   (Gốc 100 tỷ)         |                     |  |
|     +---------------+                                     |              |                     |  |
|                               (Lớp 2: Hợp đồng rủi ro nội bộ)----------->|  CFU MUA LẠI NỢ     |  |
|                               <-------(CFU trả VOF 5.5%)----------------- |  Gánh rủi ro 3M     |  |
|                                                                          |                     |  |
|                                                                          |  HỒ ĐIỀU TIẾT CHUNG |  |
|  2. CHO VAY TÍN DỤNG:                                                    |  (NETTING & POOL)   |  |
|     +---------------+                                                    |  Quản trị thanh     |  |
|     |  Khách Vay    | <==(Lớp 1: Hợp đồng thật)== [ Chi nhánh B ]        |  khoản & Lãi suất   |  |
|     |  5 Năm Cố định| ---(Thu lãi 10.0%)-------->   (Dư nợ 100 tỷ)       |                     |  |
|     +---------------+                                     |              |                     |  |
|                               (Lớp 2: Hợp đồng rủi ro nội bộ)<-----------|  CFU BÁN VỐN DÀI HẠN|  |
|                               --------(BU trả COF 7.5%)----------------->|  Bảo hiểm lãi suất  |  |
|                                                                          +---------------------+  |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Ma Trận Phân Định Trách Nhiệm Rủi Ro Giữa BU và CFU

Một hệ thống FTP chuẩn mực thiết lập ranh giới trách nhiệm tuyệt đối rõ ràng [[src-vab-ftp#^vab-ftp-4]] [[src-ftp-transmission-analysis#^ftp-trans-2]]:

```
+---------------------------------------------------------------------------------------------------+
|                        PHÂN ĐỊNH TRÁCH NHIỆM RỦI RO GIỮA BU VÀ CFU                                |
+---------------------------------------------------------------------------------------------------+
|  NHÓM RỦI RO CFU MUA LẠI (CFU ABSORBS 100%)          |  NHÓM RỦI RO BU BUỘC PHẢI GIỮ LẠI (BU'S RISK)     |
+------------------------------------------------------+-------------------------------------------+
|  1. Rủi ro Thanh khoản (Liquidity Risk):             |  1. Rủi ro Tín dụng (Credit Risk):        |
|     - Rủi ro mất cân đối kỳ hạn (Maturity mismatch)  |     - Khách hàng không trả nợ (Default)   |
|     - Chi phí tuân thủ tỷ lệ LCR, NSFR, TT22         |     - Trích lập dự phòng tổn thất tín dụng|
|                                                      |                                           |
|  2. Rủi ro Lãi suất (IRRBB / Repricing Risk):        |  2. Rủi ro Vận hành & Chi phí (OpCost):   |
|     - Rủi ro tái định giá (Repricing Gap)            |     - Chi phí nhân sự, hoa hồng bán hàng  |
|     - Biến động đường cong lợi suất thị trường       |     - Chi phí thuê mặt bằng chi nhánh     |
|                                                      |                                           |
|  3. Rủi ro Cơ sở (Basis Risk):                       |  3. Rủi ro Tuân thủ Vi mô (Branch OpRisk):|
|     - Lệch pha giữa các benchmark (VNIBOR vs SBV OMO)|     - Sai sót hồ sơ, gian lận tác nghiệp  |
+------------------------------------------------------+-------------------------------------------+
```

- **CFU không gánh rủi ro tín dụng**: Nếu khách hàng vay tiền của chi nhánh bị phá sản, chi nhánh phải chịu mất thu nhập lãi và gánh chi phí trích lập dự phòng rủi ro. CFU chỉ cung cấp vốn và bảo hiểm rủi ro thanh khoản / lãi suất; CFU không bao che cho các quyết định cấp tín dụng kém chất lượng của BU.
- **BU không gánh rủi ro thị trường**: Dù lãi suất liên ngân hàng tăng vọt hay thị trường đóng băng thanh khoản, BU đã khóa giá vốn cố định với CFU nên hoàn toàn không bị ảnh hưởng [[src-choudhry-principles-banking#^choudhry-ftp-8]].

---

## 3. Cơ Chế Bù Trừ và Hồ Điều Tiết Trung Tâm (Pooling & Netting Mechanism)

CFU có khả năng quản lý rủi ro vượt trội hơn bất kỳ đơn vị kinh doanh riêng lẻ nào nhờ ba cơ chế kinh tế quy mô:

### 3.1. Hiệu Ứng Bù Trừ Tự Nhiên (Natural Netting Effect)
Trong mạng lưới hàng trăm chi nhánh của ngân hàng:
- Các chi nhánh huy động vốn nông thôn, vùng ven (thặng dư thanh khoản ngắn hạn) bán vốn cho CFU.
- Các chi nhánh cho vay tại các đô thị lớn, khu công nghiệp (thâm hụt vốn dài hạn) mua vốn từ CFU.
- CFU đóng vai trò là "hồ điều tiết trung tâm" (Liquidity Pool). Các dòng tiền vào (Inflows) và dòng tiền ra (Outflows) tự bù trừ lẫn nhau. CFU chỉ cần ra thị trường bán buôn để tài trợ hoặc phòng ngừa cho **vị thế chênh lệch ròng (Net Exposure)**, giúp tiết kiệm hàng trăm tỷ đồng chi phí giao dịch và chi phí phòng ngừa rủi ro cho toàn hệ thống.

### 3.2. Quy Luật Số Lớn Đối Với Tiền Gửi Không Kỳ Hạn (CASA)
Một khách hàng cá nhân có thể rút toàn bộ tiền gửi không kỳ hạn trong tài khoản bất kỳ lúc nào. Nhìn ở cấp độ đơn lẻ, rủi ro thanh khoản là 100%.  
Tuy nhiên, khi CFU tổng hợp hàng triệu tài khoản khách hàng trên toàn quốc, theo quy luật số lớn, luôn tồn tại một tỷ lệ tiền gửi lõi ổn định bền vững (Core CASA, thường chiếm 70%–85% tổng số dư) [[src-vab-ftp#^vab-ftp-14]]. CFU vận hành mô hình danh mục tái lập ([[replicating-portfolio-model]]) để chuyển đổi nguồn vốn không kỳ hạn này thành nguồn vốn tài trợ trung dài hạn ($1\text{Y}-3\text{Y}$) hưởng lợi suất cao mà từng chi nhánh riêng lẻ không thể tự thực hiện.

### 3.3. Quy Mô Giao Dịch Phái Sinh Phòng Ngừa Rủi Ro Chuyên Nghiệp
BU không có giấy phép, chuyên môn và công cụ để tham gia thị trường phái sinh lãi suất. Khi CFU tiếp quản toàn bộ khe hở tái định giá ([[gap-risk]]) từ các BU, CFU tổng hợp thành trạng thái rủi ro lãi suất ròng của toàn ngân hàng và thực hiện các hợp đồng hoán đổi lãi suất ([[interest-rate-swap|IRS]]), hoán đổi tiền tệ chéo (CCS), hoặc giao dịch thị trường mở OMO với Ngân hàng Nhà nước ở mức chi phí bán buôn tối ưu nhất.

---

## 4. Bóc Tách Thặng Dư Lãi Ròng (3-Way NIM Decomposition)

Hệ thống FTP bóc tách toàn bộ Thặng dư Lãi ròng (Net Interest Margin — NIM) của ngân hàng thành ba cấu phần độc lập và minh bạch [[src-choudhry-principles-banking#^choudhry-ftp-13]]:

$$\text{Tổng NIM Ngân Hàng} = \text{Biên Cho Vay (Asset Margin)} + \text{Biên Huy Động (Liability Margin)} + \text{Biên Treasury (Mismatch Margin)}$$

```
                   +-------------------------------------------------------+
                   |     TỔNG THẶNG DƯ LÃI RÒNG CỦA NGÂN HÀNG (TOTAL NIM)  |
                   +-------------------------------------------------------+
                                              |
            +---------------------------------+---------------------------------+
            |                                 |                                 |
            v                                 v                                 v
   [ BIÊN CHO VAY CỦA BU ]           [ BIÊN TREASURY / CFU ]           [ BIÊN TIỀN GỬI CỦA BU ]
  (Asset Commercial Margin)         (Treasury Mismatch Margin)       (Liability Commercial Margin)
     Lãi suất Khách vay                 Lãi suất FTP Cho vay              Lãi suất FTP Tiền gửi
            TRỪ                                 TRỪ                                TRỪ
    Lãi suất FTP Cho vay                Lãi suất FTP Tiền gửi              Lãi suất Khách gửi
          (COF)                               (VOF)                             (Deposit)
```

1. **Biên Thương mại Cho vay (Asset Commercial Margin = Lãi suất vay - COF)**: Đo lường năng lực của khối kinh doanh tín dụng trong việc định giá khoản vay cao hơn chi phí vốn thị trường. Hoàn toàn phi rủi ro thị trường đối với BU.
2. **Biên Thương mại Huy động (Liability Commercial Margin = VOF - Lãi suất gửi)**: Đo lường giá trị thương quyền khách hàng và mạng lưới chi nhánh trong việc thu hút tiền gửi rẻ hơn chi phí huy động bán buôn trên thị trường.
3. **Biên Quản trị Vốn (Treasury Mismatch Margin = COF - VOF)**: Là kết quả P&L thuần túy từ hoạt động quản trị chênh lệch kỳ hạn và vị thế thanh khoản tập trung tại CFU. Khoản lời này chính là **khoản phí bảo hiểm rủi ro** mà CFU tiếp quản từ các BU để chi trả cho các hoạt động phòng ngừa phái sinh trên thị trường.

---

## 5. Động Lực Học Trong Kịch Bản Khủng Hoảng (Stress Test Case)

Xét một kịch bản giả định thực tế: Nền kinh tế đối mặt với cú sốc thắt chặt tiền tệ, **lãi suất thị trường tăng vọt thêm +300 bps (+3.0%)**:

```
+---------------------------------------------------------------------------------------------------+
|                        ĐỘNG LỰC BẢO HIỂM RỦI RO TRONG KỊCH BẢN LÃI SUẤT TĂNG SỐC                  |
+---------------------------------------------------------------------------------------------------+
|  1. KHOẢN VAY CỐ ĐỊNH 5 NĂM (Dư nợ 100 tỷ, lãi suất cho vay 9.5%):                               |
|     - Trước sốc: BU mua vốn COF 8.0%  ==> Biên lợi nhuận BU = 9.5% - 8.0% = +1.5% (+1.5 tỷ/năm)  |
|     - Sau sốc (+300 bps): Lãi suất thị trường tăng lên 11.0%.                                     |
|       Do tuân thủ nguyên tắc Matched-Maturity, CFU bảo lưu giá COF 8.0% cho BU suốt 5 năm.         |
|     ==> BIÊN LỢI NHUẬN BU ĐƯỢC BẢO VỆ NGUYÊN VẸN: 9.5% - 8.0% = +1.5% (Hoàn toàn an toàn!)        |
|                                                                                                   |
|  2. KHOẢN TIỀN GỬI 12 THÁNG (Số dư 100 tỷ, lãi suất huy động ban đầu 5.0%):                      |
|     - Trước sốc: BU bán vốn VOF 6.2%  ==> Biên lợi nhuận BU = 6.2% - 5.0% = +1.2% (+1.2 tỷ/năm)  |
|     - Sau sốc (+300 bps): Hợp đồng 12 tháng đáo hạn. Lãi suất huy động thị trường nhảy lên 8.0%.  |
|       Để giữ chân người gửi tiền, BU phải nâng lãi suất huy động lên 8.0%.                        |
|       CFU lập tức công bố Biểu giá VOF mới cho kỳ hạn 12 tháng là 9.2%.                           |
|     ==> BIÊN LỢI NHUẬN BU TIẾP TỤC ĐƯỢC BẢO TOÀN: 9.2% - 8.0% = +1.2% (Hoàn toàn an toàn!)       |
|                                                                                                   |
|  3. VỊ THẾ CỦA TRUNG TÂM QUẢN LÝ VỐN (CFU):                                                       |
|     - CFU thu từ khoản vay 5 năm:           8.0 tỷ/năm (theo giá COF cũ)                          |
|     - CFU phải trả cho tiền gửi 12 tháng:   9.2 tỷ/năm (theo giá VOF mới)                         |
|     ==> CFU CHỊU KHOẢN LỖ QUẢN TRỊ NỘI BỘ: 8.0% - 9.2% = -1.2% (-1.2 TỶ/NĂM)                     |
|                                                                                                   |
|  4. CƠ CHẾ PHÒNG NGỪA CỦA CFU:                                                                    |
|     - CFU trước đó đã dự liệu khe hở kỳ hạn này và thực hiện hợp đồng Hoán đổi Lãi suất (IRS)     |
|       với một ngân hàng đầu tư quốc tế (Payer Swap: Trả cố định 6.5%, Nhận thả nổi).              |
|     - Khi lãi suất thị trường tăng vọt, HỢP ĐỒNG IRS CỦA CFU LÃI LỚN: +2.0 TỶ/NĂM.                |
|     ==> KHOẢN LÃI PHÁI SINH THỊ TRƯỜNG BÙ ĐẮP TOÀN BỘ KHOẢN LỖ NỘI BỘ (-1.2 TỶ) VÀ DƯ RA LỢI NHUẬN|
+---------------------------------------------------------------------------------------------------+
```

**Bài học quản trị**: Cú sốc thị trường tạo ra rủi ro lỗ, nhưng rủi ro đó đã được chuyển giao hoàn toàn khỏi các chi nhánh kinh doanh và tập trung tại CFU — nơi có đầy đủ công cụ phái sinh để hấp thụ và vô hiệu hóa cú sốc.

---

## 6. Xung Đột Lợi Ích và Cơ Chế Giám Sát Của ALCO

Trong thực tế vận hành, cơ chế chuyển giao rủi ro nội bộ thường phát sinh các xung đột lợi ích:
1. **Tranh chấp giá COF/VOF**: Các đơn vị kinh doanh tín dụng thường khiếu nại rằng giá COF của CFU quá cao khiến họ mất khách hàng vào tay đối thủ; trong khi khối huy động cho rằng giá VOF quá thấp không bù đắp được chi phí bán hàng.
2. **Hành vi luồn lách (Gaming the System)**: Chi nhánh tìm cách phân loại sai bản chất sản phẩm (ví dụ khai báo tiền gửi doanh nghiệp thông thường thành tiền gửi vận hành operational deposits để né phụ phí thanh khoản LCR).
3. **Vai trò Trọng tài của Ủy ban ALCO**:
   - ALCO là cơ quan quyền lực cao nhất phê duyệt phương pháp luận FTP, các đường cong cơ sở và các hệ số biên độ điều chỉnh chính sách.
   - ALCO bảo đảm tính minh bạch: Mọi phụ phí trong FTP đều phải giải trình được bằng chi phí rủi ro thực tế trên thị trường, không biến CFU thành một "hộp đen" trục lợi từ các chi nhánh kinh doanh [[src-choudhry-principles-banking#^choudhry-ftp-9]].

## Khái niệm và Liên kết
- [[ftp-cost-benefit-allocation-principles]]: Nguyên tắc phân bổ chi phí và lợi ích của từng FTP portfolio cho các đơn vị kinh doanh và sản phẩm.
- [[ftp-portfolio-and-bucket-allocation]]: Phương pháp phân bổ giao dịch và sản phẩm vào các danh mục và thang kỳ hạn FTP.
- [[liquidity-transfer-pricing]]: Tổng quan lý thuyết định giá điều chuyển thanh khoản nội bộ.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn điều tiết các kênh rủi ro của FTP.
- [[ftp-pricing-methodology]]: Phương pháp định giá chi tiết VOF, COF và phụ phí tuân thủ pháp lệnh.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa bảng cân đối ALM toàn diện dưới hệ thống điều khiển FTP.
- [[ftp-nature-and-balance-sheet-management]]: Bản chất, mục tiêu của FTP và các vấn đề cốt tử giải quyết trong quản trị bảng cân đối.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất trong sổ ngân hàng.
- [[interest-rate-swap]]: Hợp đồng hoán đổi lãi suất IRS — công cụ phòng ngừa rủi ro thị trường của CFU.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO.
- [2026-10-19] ingest src-bcbs-framework RBC25 — chờ user duyệt: thêm ghi chú phân biệt ở mục 1: Basel RBC25.18 dùng cùng tên "internal risk transfer" cho bản ghi nội bộ chuyển rủi ro giữa banking book và trading book, có hệ quả về vốn quy định [[src-bcbs-framework#^rbc25-18]]; khái niệm này nằm ở node [[regulatory-internal-risk-transfer]], khác với chuyển rủi ro BU → Treasury qua FTP của node này.
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]] và [[loan-pricing]] (lãi suất hoà vốn theo RoE mục tiêu, TRR do ALCO duyệt ngoại lệ); đề xuất link ở chỗ nhắc NIM và định giá khoản vay.
- [2026-10-19] ingest src-choudhry-principles-banking u21–u22 — chờ user duyệt: thêm nguồn T4: thông lệ tốt là toàn bộ rủi ro lãi suất tập trung về Treasury qua giao dịch funding; vị thế của mảng khác được Treasury match fund hoặc phòng ngừa bằng internal swap [[src-choudhry-principles-banking#^choudhry-st-11]].
