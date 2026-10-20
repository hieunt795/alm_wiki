---
title: "Rủi ro chênh lệch lãi suất cơ sở (Basis Risk): Đo lường và phòng hộ lệch pha VNIBOR vs Lãi suất Big 4"
aliases: [IRRBB Basis Risk Measurement and Hedging, Do luong va phong ho Basis Risk VNIBOR vs Big 4, Basis Risk VNIBOR Big 4]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Bản chất Basis Risk VNIBOR vs Big 4 12M · Phương pháp đo lường và Stress Testing Basis Spread · Xử lý Basis Risk qua hệ thống Multi-curve FTP · Kỹ thuật phòng hộ Basis Swap và tái cấu trúc hợp đồng · Khung quy định Basel vs NHNN"
as_of: 2026-10-19
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]", "[[src-tata-bank-alm]]", "[[src-tt83-2025-nhnn]]"]
relations: []
tags: [alm, irrbb, basis-risk, vnibor, big4-deposit-rate, basis-swap, multi-curve-ftp, basis-spread, stress-testing, synthesis]
updated: 2026-10-19
reviewed:
---

## Câu hỏi
1. Bản chất của Rủi ro cơ sở ([[basis-risk|Basis Risk]]) phát sinh từ sự lệch pha giữa chỉ số huy động (VNIBOR) và chỉ số cho vay (Lãi suất tiền gửi 12M của Big 4) trong hệ thống ngân hàng Việt Nam là gì? Tại sao hai chỉ số này có độ tương quan không hoàn hảo?
2. Phương pháp đo lường lượng hóa Basis Risk tác động lên thu nhập thuần ([[net-interest-income-sensitivity|ΔNII]]) và giá trị kinh tế ([[economic-value-of-equity|ΔEVE]])? Cách thức thiết lập kịch bản kiểm tra sức chịu đựng (Stress Testing) riêng cho chênh lệch cơ sở (Basis Spread Shock)?
3. Hệ thống [[ftp-pricing-methodology|định giá điều chuyển vốn nội bộ (FTP)]] xử lý Basis Risk ra sao qua cơ chế đa đường cong (Multi-curve FTP Framework) và bóc tách Phụ phí Cơ sở (Basis Spread Charge) chuyển giao về Treasury?
4. ALCO và Treasury áp dụng các kỹ thuật nào để phòng ngừa Basis Risk: Hợp đồng hoán đổi cơ sở (Basis Swap), Tái cấu trúc điều khoản tham chiếu hợp đồng tín dụng, và Phòng hộ tự nhiên qua bảng cân đối (Natural Matched-Basis Hedging)?
5. Chuẩn mực Basel ([[src-bcbs-irrbb-2016]]) và quy định pháp lý của Ngân hàng Nhà nước Việt Nam (Thông tư 83/2025/TT-NHNN) yêu cầu thế nào về đo lường, giám sát hạn mức và quản trị Basis Risk tại NHTM?

## Kết luận
- **Bản chất bất đối xứng cấu trúc tại Việt Nam**: Basis Risk tại các NHTM Việt Nam bộc lộ rõ nét qua sự phân kỳ giữa chỉ số cho vay thả nổi (neo theo lãi suất tiền gửi 12M bình quân của 4 NHTM Nhà nước: Vietcombank, BIDV, VietinBank, Agribank) và chỉ số chi phí tài trợ vốn bán buôn/cận biên của Treasury (neo theo lãi suất liên ngân hàng VNIBOR) [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-choudhry-principles-banking#^choudhry-irrbb-1]]. Lãi suất Big 4 mang tính chất lãi suất quản lý điều hành (*administered rate*), biến động chậm và có độ trễ lớn; trong khi VNIBOR biến động giật cục theo thanh khoản thị trường liên ngân hàng và chính sách SBV [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- **Kịch bản sốc biên độ riêng biệt**: Các kịch bản sốc lãi suất song song (Parallel shocks) hoàn toàn bất lực trong việc nhận diện Basis Risk [[src-bcbs-irrbb-2016#^irrbb-u06-7]]. Ngân hàng bắt buộc phải thiết lập kịch bản sốc giãn biên độ cơ sở ($\Delta\text{Basis} = \text{VNIBOR} - \text{DepositRate}^{\text{Big4}}$ nới rộng $+150$ đến $+300$ bps) để lượng hóa mức sụt giảm $\Delta\text{NII}$ trong 12 tháng [[src-bcbs-irrbb-2016#^irrbb-p04-1]].
- **Hệ thống Multi-curve FTP và Phụ phí Cơ sở**: FTP bóc tách toàn diện rủi ro cơ sở bằng cách xây dựng các đường cong chuẩn riêng biệt cho từng thị trường (đường cong VNIBOR cho Thị trường 2 và đường cong huy động dân cư cho Thị trường 1) [[src-vab-ftp#^vab-ftp-5]] [[src-vab-ftp#^vab-ftp-37]]. Khi chi nhánh giải ngân khoản vay neo theo Big 4 nhưng được tài trợ bằng vốn liên ngân hàng, Treasury áp phụ phí $\text{Basis Spread Charge}$ vào giá COF, bảo vệ biên lợi nhuận thương mại của đơn vị kinh doanh [[src-ftp-transmission-analysis#^ftp-trans-10]] [[src-choudhry-principles-banking#^choudhry-ftp-11]].
- **Hóa giải bằng tái cấu trúc hợp đồng và phòng hộ tự nhiên**: Do thị trường phái sinh hoán đổi cơ sở (Basis Swap) tại Việt Nam có thanh khoản hạn chế [[src-bcbs-irrbb-2016#^irrbb-u06-4]], ALCO ưu tiên áp dụng giải pháp cấu trúc: Chuyển đổi chỉ số tham chiếu cho vay sang lãi suất cơ sở nội bộ (Prime Rate), thiết lập sàn lãi suất (Interest Rate Floor), và cân bằng trạng thái tài sản - nợ theo cùng chỉ số tham chiếu (Matched-Basis Funding) [[src-choudhry-principles-banking#^choudhry-ftp-11]].
- **Khoảng trống pháp lý tại Việt Nam**: Chuẩn mực quốc tế BCBS d368 yêu cầu kiểm tra sức chịu đựng Basis Risk bắt buộc tại Nguyên tắc 4; tại Việt Nam, Phụ lục V của [[tt83-2025]] chỉ có kịch bản sốc đường cong (6 kịch bản ΔEVE, 2 kịch bản ΔNII) [[src-tt83-2025-nhnn#^pl5-a3-1]] [[src-tt83-2025-nhnn#^pl5-b3]], không có kịch bản sốc chênh lệch lãi suất cơ sở.

## Cơ chế

### Q1 — Bản chất Basis Risk VNIBOR vs Lãi suất Tiền gửi Big 4 tại Việt Nam
Rủi ro cơ sở (Basis Risk) là một trong ba phân loại rủi ro cốt lõi của IRRBB, miêu tả tác động tiêu cực đến nguồn vốn và thu nhập phát sinh từ sự biến động tương đối giữa các công cụ có kỳ hạn tương đương nhưng được định giá dựa trên các chỉ số lãi suất cơ sở (bases) khác nhau [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-choudhry-principles-banking#^choudhry-irrbb-1]].

Tại Việt Nam, cấu trúc bảng cân đối của các NHTM Cổ phần tạo ra phơi nhiễm Basis Risk điển hình:
1. **Bên Tài sản Có (Cho vay Khách hàng)**:
   - Các khoản tín dụng trung dài hạn (cho vay doanh nghiệp, mua nhà thế chấp) áp dụng cơ chế lãi suất thả nổi định kỳ (3 tháng hoặc 6 tháng reset một lần):
     $$\text{Lãi suất cho vay} = \text{Lãi suất tham chiếu} + \text{Margin}$$
   - Lãi suất tham chiếu phổ biến nhất trên thị trường là **Lãi suất tiền gửi tiết kiệm 12 tháng trả lãi sau bình quân của 4 NHTM Nhà nước (Big 4: VCB, BIDV, CTG, Agribank)**.
2. **Bên Tài sản Nợ (Chi phí Tài trợ Vốn)**:
   - Một phần nguồn vốn tài trợ cho tăng trưởng tín dụng hoặc điều hòa thanh khoản ngắn hạn được huy động trên thị trường liên ngân hàng (Thị trường 2) hoặc thị trường mở (OMO), neo chặt theo **VNIBOR (Vietnam Interbank Offered Rate)** [[src-vab-ftp#^vab-ftp-37]].
3. **Cơ chế Lệch pha Tương quan (Imperfect Correlation)**:
   - *Tính chất thị trường khác biệt*: VNIBOR phản ánh cung cầu vốn tức thời giữa các tổ chức tín dụng và chịu tác động trực tiếp từ chính sách tiền tệ ngắn hạn của NHNN [[src-ftp-transmission-analysis#^ftp-trans-4]]. Khi thanh khoản liên ngân hàng căng thẳng cục bộ, VNIBOR kỳ hạn 1M–3M có thể tăng vọt từ 2%–3% lên 7%–9% trong thời gian rất ngắn.
   - *Tính chất lãi suất quản lý (Administered Rate)*: Lãi suất tiền gửi Big 4 đóng vai trò neo giữ mặt bằng lãi suất quốc gia nhằm hỗ trợ nền kinh tế [[src-bcbs-irrbb-2016#^irrbb-u06-3]]. Khi VNIBOR tăng vọt, lãi suất Big 4 thường đứng yên hoặc chỉ tăng rất chậm với độ trễ lớn (lagging indicator).
   - *Hậu quả cho NIM*: Chi phí huy động vốn của ngân hàng tăng tức thì theo VNIBOR trong khi thu nhập lãi từ cho vay neo theo Big 4 không đổi, dẫn tới sự sụt giảm nghiêm trọng của biên lãi thuần ($\text{NIM} \downarrow$) và thu nhập lãi thuần ($\Delta\text{NII} \downarrow$) [[src-choudhry-principles-banking#^choudhry-irrbb-1]].

```
LÃI SUẤT THẢ NỔI CHO VAY = Big 4 Deposit Rate (12M) + Margin [Tăng chậm, trễ pha]
                              ▲
                              │ Chênh lệch cơ sở biến động bất lợi (Basis Spread widens)
                              ▼
CHI PHÍ TÀI TRỢ VỐN TREASURY = VNIBOR (1M-3M) / Interbank [Biến động giật cục, tăng vọt]
➔ KẾT QUẢ: Thu nhập lãi thuần (NII) bị bóp nghẹt, NIM sụt giảm mạnh
```

### Q2 — Phương pháp Đo lường và Kịch bản Kiểm tra Sức chịu đựng (Basis Stress Testing)
Chuẩn mực Basel d368 (Nguyên tắc 4 & Annex 1) khẳng định các kịch bản sốc lãi suất chuẩn hóa (Parallel, Steepener, Flattener) giả định mọi đường cong dịch chuyển đồng bộ nên **hoàn toàn không bắt được Basis Risk** [[src-bcbs-irrbb-2016#^irrbb-u06-7]]. Ngân hàng bắt buộc phải thiết lập mô hình đo lường và kịch bản sốc cơ sở riêng biệt [[src-bcbs-irrbb-2016#^irrbb-p04-1]]:

1. **Lượng hóa Chênh lệch Cơ sở (Basis Spread Modeling)**:
   - Xác định chuỗi thời gian của chênh lệch cơ sở:
     $$\text{Spread}_t = \text{VNIBOR}_t - \text{DepositRate}^{\text{Big4}}_t$$
   - Ước tính hệ số tương quan ($\rho$) và phương sai sai số giữa hai chỉ số. Phân tích hồi quy xác định mức độ truyền dẫn (Pass-through Beta):
     $$\Delta\text{DepositRate}^{\text{Big4}}_t = \alpha + \beta_{\text{basis}} \cdot \Delta\text{VNIBOR}_t + \epsilon_t$$
     Trong ngắn hạn ($\le 6$ tháng), $\beta_{\text{basis}}$ thường chỉ đạt $0.2 - 0.4$, phản ánh sự kém nhạy bén của lãi suất Big 4 so với biến động thị trường.
2. **Đo lường Tác động lên Thu nhập Lãi thuần ($\Delta\text{NII}$)**:
   - Giả định danh mục cho vay neo theo Big 4 có quy mô $A_{\text{Big4}}$ và nguồn vốn tài trợ neo theo VNIBOR có quy mô $L_{\text{VNIBOR}}$ trên cùng kỳ hạn tái định giá $\tau$:
     $$\Delta\text{NII}_{\text{basis}} = A_{\text{Big4}} \cdot \Delta\text{DepositRate}^{\text{Big4}} - L_{\text{VNIBOR}} \cdot \Delta\text{VNIBOR}$$
     [[src-tata-bank-alm#^tata-nii-1]]
   - Nếu ngân hàng có trạng thái ròng phơi nhiễm cơ sở $\text{Net Basis Exposure} = L_{\text{VNIBOR}} - A_{\text{Big4}} > 0$, mọi sự gia tăng của chênh lệch cơ sở ($\Delta\text{Spread} > 0$) đều gây tổn thất trực tiếp lên NII.
3. **Thiết lập Kịch bản Kiểm tra Sức chịu đựng (Basis Stress Scenario)**:
   - ALCO thiết lập kịch bản sốc chênh lệch cơ sở định kỳ hàng quý [[src-bcbs-irrbb-2016#^irrbb-p04-1]]:
     - *Kịch bản Cơ sở (Baseline)*: Chênh lệch $\text{Spread}$ duy trì mức bình quân lịch sử (vd: $\text{VNIBOR} 3\text{M} - \text{Big4 } 12\text{M} = -100 \text{ bps}$).
     - *Kịch bản Căng thẳng Cục bộ (Stress 1)*: VNIBOR tăng $+200$ bps trong khi Lãi suất Big 4 tăng $+50$ bps ($\text{Spread}$ nới rộng $+150$ bps).
     - *Kịch bản Căng thẳng Nghiêm trọng (Stress 2 - Extreme Liquidity Crunch)*: VNIBOR tăng $+400$ bps trong khi Lãi suất Big 4 đứng yên do chỉ đạo chính sách ($\text{Spread}$ nới rộng $+400$ bps).
   - So sánh mức tổn thất $\Delta\text{NII}$ tối đa với hạn mức khẩu vị rủi ro của ALCO và vốn cấp 1 [[src-bcbs-irrbb-2016#^irrbb-p04-1]].

### Q3 — Xử lý Basis Risk qua Hệ thống Multi-curve FTP
Hệ thống định giá điều chuyển vốn nội bộ (FTP) là công cụ trung tâm để bóc tách, định giá và chuyển giao rủi ro cơ sở từ các đơn vị kinh doanh (BU) về Treasury (CFU) [[src-ftp-transmission-analysis#^ftp-trans-2]] [[src-ftp-transmission-analysis#^ftp-trans-9]]:

1. **Nguyên tắc Khớp Cơ sở (Matched-Basis Principle)**:
   - Moorad Choudhry chỉ ra rằng để bảo vệ biên thương mại cố định của BU, giá FTP bắt buộc phải được thiết lập trên cùng kỳ hạn, cùng đồng tiền và **cùng chỉ số cơ sở (same basis)** với giao dịch bên ngoài của khách hàng [[src-choudhry-principles-banking#^choudhry-ftp-11]].
2. **Kiến trúc FTP Đa Đường cong (Multi-curve FTP)**:
   - Treasury xây dựng hai hệ thống đường cong độc lập [[src-vab-ftp#^vab-ftp-5]] [[src-vab-ftp#^vab-ftp-28]]:
     - *Đường cong Thị trường 1 (Retail/Commercial Curve)*: Xây dựng dựa trên lãi suất huy động bình quân toàn hệ thống hoặc tham chiếu trực tiếp theo chỉ số Big 4.
     - *Đường cong Thị trường 2 (Wholesale/Interbank Curve)*: Xây dựng dựa trên VNIBOR và lợi suất Trái phiếu Chính phủ VGB [[src-vab-ftp#^vab-ftp-37]].
3. **Định giá Phụ phí Rủi ro Cơ sở (Basis Spread Charge)**:
   - Khi đơn vị kinh doanh bán tài sản tín dụng neo theo chỉ số Big 4 nhưng Treasury phải huy động vốn trên thị trường 2 theo VNIBOR để tài trợ, giá bán vốn COF được cộng thêm phụ phí cơ sở [[src-ftp-transmission-analysis#^ftp-trans-3]]:
     $$\text{COF Rate} = \text{Base Rate}(\text{Big4}) + \text{Basis Spread Charge} + \text{Liquidity Premium (TLP)} + \text{Buffer Cost}$$
   - $\text{Basis Spread Charge}$ phản ánh chi phí kỳ vọng để phòng ngừa rủi ro lệch pha giữa VNIBOR và Big 4 hoặc phần bù rủi ro biến động lịch sử của spread [[src-ftp-transmission-analysis#^ftp-trans-3]].
   - Nhờ cơ chế này, BU nhận được biên thương mại cố định ($\text{Commercial Margin} = \text{Customer Rate} - \text{COF Rate}$) không bị suy giảm khi VNIBOR biến động [[src-choudhry-principles-banking#^choudhry-ftp-11]]. Toàn bộ rủi ro cơ sở được chuyển giao về Treasury quản lý tập trung [[src-ftp-transmission-analysis#^ftp-trans-10]].

### Q4 — Kỹ thuật Phòng hộ và Tái cấu trúc Bảng Cân đối
Để kiểm soát trạng thái rủi ro cơ sở ròng tập trung tại Treasury, ALCO và Treasury triển khai các giải pháp kỹ trị:

1. **Hợp đồng Hoán đổi Lãi suất Cơ sở (Basis Swap)**:
   - Là hợp đồng phái sinh trong đó hai bên trao đổi hai dòng tiền lãi thả nổi được định giá theo hai chỉ số tham chiếu khác nhau trên cùng một đồng tiền [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
   - *Cơ chế*: Treasury thực hiện giao dịch Basis Swap: Nhận lãi suất thả nổi neo theo VNIBOR (khớp với chi phí huy động nợ) và Trả lãi suất thả nổi neo theo Lãi suất Big 4 (khớp với dòng thu nhập từ tài sản cho vay).
   - *Hạn chế tại Việt Nam*: Thị trường phái sinh lãi suất nội địa (VND) đối với cấu trúc Basis Swap neo theo Big 4 có tính thanh khoản rất thấp; các định chế tài chính quốc tế ít tham gia do thiếu đường cong chuẩn và rủi ro chính sách trong việc ấn định lãi suất Big 4.
2. **Tái cấu trúc Điều khoản Tham chiếu Hợp đồng Tín dụng (Contractual Redesign)**:
   - *Chuyển sang Lãi suất Cơ sở Nội bộ (Internal Base Rate / Prime Rate)*: Ngân hàng thay thế chỉ số Big 4 bằng "Lãi suất cơ sở do ngân hàng công bố định kỳ". Lãi suất này được ALCO tính toán dựa trên chi phí vốn bình quân thực tế (COF toàn hàng), giúp ngân hàng chủ động điều chỉnh tăng lãi suất cho vay khi VNIBOR và chi phí huy động tăng.
   - *Thiết lập Sàn Lãi suất (Interest Rate Floor)*: Hợp đồng cho vay quy định: $\text{Lãi suất cho vay} = \max(\text{Big4} + \text{Margin}, \text{Floor Rate})$. Sàn lãi suất bảo vệ ngân hàng khi lãi suất Big 4 giảm sâu hoặc không theo kịp đà tăng của chi phí vốn.
   - *Điều khoản Điều chỉnh Biên độ (Margin Review Clause)*: Hợp đồng cho phép ngân hàng đánh giá và điều chỉnh lại biên độ margin nếu chênh lệch giữa VNIBOR và lãi suất Big 4 vượt quá một ngưỡng quy định (ví dụ $> 200 \text{ bps}$).
3. **Phòng hộ Tự nhiên qua Bảng Cân đối (Natural Matched-Basis Hedging)**:
   - ALCO điều hành cấu trúc tài sản và nợ hướng tới việc cân bằng trạng thái theo từng chỉ số cơ sở [[src-choudhry-principles-banking#^choudhry-ftp-11]]:
     - Nếu ngân hàng cho vay 50.000 tỷ VND neo theo chỉ số Big 4, ngân hàng chủ động phát triển các sản phẩm huy động tiền gửi tiết kiệm hoặc phát hành Chứng chỉ tiền gửi (CD) bán lẻ có lãi suất liên kết trực tiếp với lãi suất Big 4.
     - Giới hạn tỷ trọng tài sản dài hạn neo theo Big 4 được tài trợ bằng nguồn vốn bán buôn ngắn hạn VNIBOR thông qua hệ thống hạn mức rủi ro cơ sở (Basis Exposure Limit).

### Q5 — Khung quy định: So sánh Basel vs Ngân hàng Nhà nước Việt Nam
- **Chuẩn mực Basel (BCBS d368)**:
  - Phân loại rõ ràng Basis Risk là phân loại rủi ro độc lập với Gap Risk (Par 8, Annex 1 Par 1.5) [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
  - Nguyên tắc 4 yêu cầu hệ thống đo lường nội bộ (IMS) bắt buộc phải tích hợp các kịch bản kiểm tra sức chịu đựng đối với rủi ro cơ sở bên cạnh 6 kịch bản sốc lãi suất chuẩn hóa [[src-bcbs-irrbb-2016#^irrbb-p04-1]] [[src-bcbs-irrbb-2016#^irrbb-u06-7]].
  - Nguyên tắc 7 & 8 yêu cầu báo cáo định kỳ cho ALCO và công bố thông tin minh bạch về mức độ phơi nhiễm Basis Risk [[src-bcbs-irrbb-2016#^irrbb-p07-1]] [[src-bcbs-irrbb-2016#^irrbb-p08-1]].
- **Quy định Ngân hàng Nhà nước Việt Nam**:
  - [[tt83-2025]] (hiệu lực 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]]) yêu cầu nhận dạng rủi ro lãi suất trên sổ ngân hàng phải xác định nguyên nhân, yếu tố làm phát sinh rủi ro, kể cả rủi ro mới từ hoạt động phòng ngừa [[src-tt83-2025-nhnn#^d54-2]]. Chương III Mục 7 không nêu riêng basis risk hay chỉ số lãi suất tham chiếu.
  - Kiểm tra sức chịu đựng IRRBB được thực hiện qua ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d54-3b]]. Phụ lục V chỉ quy định 6 kịch bản sốc đường cong cho ΔEVE [[src-tt83-2025-nhnn#^pl5-a3-1]] và 2 kịch bản song song cho ΔNII [[src-tt83-2025-nhnn#^pl5-b3]]; không có kịch bản sốc chênh lệch cơ sở.
  - *Khoảng trống thực thi*: Chưa có quy định pháp quy cụ thể hướng dẫn biên độ sốc kiểm tra sức chịu đựng chuẩn hóa dành riêng cho chênh lệch cơ sở VNIBOR vs Big 4 tại Việt Nam; các ngân hàng hiện chủ yếu tự xây dựng kịch bản nội bộ trong khuôn khổ ICAAP/ILAAP.

## Bằng chứng ủng hộ
- **Chuẩn mực BCBS**: Định nghĩa và xác lập rủi ro cơ sở phát sinh từ sự tương quan không hoàn hảo giữa các chỉ số tham chiếu (Annex 1 Par 1.5) [[src-bcbs-irrbb-2016#^irrbb-u06-4]], đồng thời chỉ rõ sự bất lực của kịch bản sốc song song đối với rủi ro cơ sở (Annex 1 Par 4.2) [[src-bcbs-irrbb-2016#^irrbb-u06-7]].
- **Moorad Choudhry**: Khẳng định nguyên tắc khớp cơ sở (Matched Basis) trong FTP là điều kiện tiên quyết để triệt tiêu rủi ro lãi suất cho đơn vị kinh doanh và bảo toàn tính toàn vẹn của biên thương mại [[src-choudhry-principles-banking#^choudhry-ftp-11]].
- **Cơ chế FTP tại Việt Nam**: Báo cáo phương pháp luận FTP của VietABank chứng minh sự cần thiết phải phân tách hai đường cong độc lập cho thị trường 1 (dân cư/tổ chức kinh tế) và thị trường 2 (liên ngân hàng VNIBOR) để định giá chính xác chi phí vốn [[src-vab-ftp#^vab-ftp-5]] [[src-vab-ftp#^vab-ftp-37]].

## Bằng chứng trái chiều
- **Rủi ro danh tiếng khi từ bỏ chỉ số Big 4**: Việc thay thế chỉ số tham chiếu khách quan (như Lãi suất Big 4) bằng lãi suất cơ sở nội bộ (Internal Prime Rate) giúp ngân hàng phòng ngừa Basis Risk nhưng vấp phải sự phản đối của khách hàng vay vốn do lo ngại ngân hàng đơn phương tăng lãi suất, tạo ra rủi ro pháp lý và cạnh tranh thị trường.
- **Rào cản phòng hộ phái sinh**: Trên thị trường quốc tế, Basis Swap (như SOFR 1M vs 3M) giao dịch sôi động với thanh khoản sâu. Ngược lại, tại Việt Nam, sự vắng bóng của thị trường Basis Swap buộc các ngân hàng phải gánh chịu rủi ro cơ sở thuần túy trên bảng cân đối mà không có công cụ ngoại bảng phòng hộ hữu hiệu.

## Phụ thuộc regime
- **Regime thanh khoản dồi dào / Lãi suất liên ngân hàng thấp**:
  - VNIBOR duy trì ở mức thấp hơn đáng kể so với lãi suất huy động dân cư và lãi suất Big 4.
  - Ngân hàng hưởng lợi từ chênh lệch cơ sở dương ($\text{VNIBOR} < \text{Big4}$), biên lãi thuần mở rộng, rủi ro cơ sở ở trạng thái tiềm ẩn.
- **Regime thanh khoản căng thẳng / SBV thắt chặt tiền tệ**:
  - VNIBOR tăng vọt nhanh chóng trong khi lãi suất Big 4 bị ghìm giữ để hỗ trợ nền kinh tế.
  - Chênh lệch cơ sở đảo chiều hoặc nới rộng đột biến ($\text{VNIBOR} \gg \text{Big4}$), bào mòn nghiêm trọng thu nhập lãi thuần $\Delta\text{NII}$ của các NHTM phụ thuộc vào vốn liên ngân hàng.

## Hàm ý ALM / quy định
- **Đối với ALCO**:
  - Bắt buộc phải đưa kịch bản căng thẳng chênh lệch cơ sở (Basis Spread Stress Test) vào chương trình nghị sự hàng tháng, không chỉ dựa vào 6 kịch bản sốc song song của Basel.
  - Thiết lập hạn mức phơi nhiễm cơ sở (Basis Risk Limit): Giới hạn quy mô tối đa các khoản vay neo theo Big 4 được tài trợ bằng nguồn vốn liên ngân hàng VNIBOR.
- **Đối với Khối Nguồn vốn (Treasury)**:
  - Vận hành hệ thống Multi-curve FTP, đưa phụ phí Basis Spread Charge vào giá COF đối với các sản phẩm cho vay thả nổi neo theo Big 4.
  - Chủ động cơ cấu danh mục nguồn vốn bán buôn theo các kỳ hạn và chỉ số khớp với danh mục tài sản sinh lời.
- **Đối với Ngân hàng Nhà nước**: Cần nghiên cứu phát triển đường cong lãi suất tham chiếu chuẩn hóa cho thị trường tài chính Việt Nam (như đường cong OIS hoặc chuẩn hóa VNIBOR) và thúc đẩy sự phát triển của thị trường phái sinh lãi suất nội địa nhằm cung cấp công cụ phòng ngừa rủi ro cho các NHTM.
- *Diễn giải:* (ngoài wiki, chưa có nguồn) Nhiều NHTM Cổ phần tại Việt Nam giải quyết bài toán này bằng cách đưa vào hợp đồng tín dụng điều khoản: "Lãi suất tham chiếu là mức cao hơn giữa bình quân Big 4 và lãi suất huy động 12 tháng của chính ngân hàng", từ đó tạo ra cơ chế tự bảo vệ tự nhiên trước sự biến động của chi phí vốn.

## Bất định
- **Khoảng trống kỹ thuật Thông tư 83/2025/TT-NHNN**: C3-M7 và Phụ lục V không có kịch bản sốc basis risk (đã ingest [2026-10-19]). Chưa kiểm C3-M1 (kiểm tra sức chịu đựng chung, raw dòng 709–717) và C3-M9 (ICAAP) `[cần nguồn: src-tt83-2025-nhnn C3-M1, C3-M9]`.
- **Triển vọng thị trường phái sinh lãi suất VND**: Khả năng hình thành thị trường hoán đổi rủi ro cơ sở (Basis Swap) chuẩn hóa giữa VNIBOR và lãi suất tiền gửi dân cư trong tương lai gần còn rất nhiều rào cản về cơ sở pháp lý và sự tham gia của các ngân hàng tạo lập thị trường (Market Makers).
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1: đã có node [[risk-appetite]], [[risk-limits]], [[stress-testing]]; stress test IRRBB tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]]; cần rà lại chỗ nhắc khẩu vị rủi ro / hạn mức.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
- [2026-10-19] ingest src-choudhry-principles-banking u25: đã có node [[structural-hedging]] (phòng ngừa IRRBB theo phần ròng sau natural hedge, macro hedge pool IRS không áp được hedge accounting [[src-choudhry-principles-banking#^choudhry-cs-14]] [[src-choudhry-principles-banking#^choudhry-cs-17]]); cần rà lại mục phòng ngừa basis risk.
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: [[structural-hedging]] thêm công cụ phòng ngừa (FRA, futures, OIS, cap) và ví dụ EAR: gap −80, +1% làm NII giảm 0,8 triệu USD (EAR ~7,8%), cap 80 triệu strike 3% loại bỏ EAR với chi phí 5bp NIM, hạn mức EAR ALCO ±5%/±10%; cần rà lại phần lựa chọn công cụ phòng ngừa.
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: đã có node [[overnight-index-swap]] (OIS/SONIA, phòng ngừa NII và basis risk tiền gửi so với lãi suất cơ bản); cần rà lại chỗ nhắc OIS để link.
- [2026-10-19] ingest src-choudhry-principles-banking u23–u24: đã có node [[ilaap]], [[reverse-stress-testing]]; cần rà lại mục "Khoảng trống thực thi" (ICAAP/ILAAP).
- [2026-10-20] ingest src-bcbs-framework SRP30: đã có node [[reputational-risk]]; cần rà lại mục rủi ro danh tiếng khi từ bỏ chỉ số Big 4.
- [2026-10-20] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 30–31): [[risk-limits]] thêm basis risk: risk tolerance riêng khi phơi nhiễm đáng kể [[src-bcbs-irrbb-2016#^irrbb-p03-5]] [[src-bcbs-irrbb-2016#^irrbb-p03-6]]; cần rà lại mục hạn mức.
