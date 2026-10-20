---
title: "Hệ Thống FTP — Động Cơ Điều Khiển Và Tối Ưu Hóa Bảng Cân Đối ALM Toàn Diện"
aliases: [FTP Balance Sheet Optimization, Tối ưu hóa bảng cân đối qua FTP, FTP Steering Engine, Động cơ điều khiển ALM, Balance Sheet Optimization]
type: synthesis
domains: [alm, product]
status: active
maturity: draft
origin: research
question: "Làm thế nào để hệ thống Funds Transfer Pricing (FTP) vận hành như một động cơ điều khiển trung tâm (unified control engine) giúp Ủy ban ALCO giải quyết bài toán quy hoạch tối ưu hóa bảng cân đối kế toán nhằm tối đa hóa NII và RAROC dưới đa ràng buộc pháp định phức tạp (LCR, NSFR, Leverage Ratio, IRRBB và CAR) mà không cần can thiệp hành chính vào từng giao dịch tác nghiệp của chi nhánh?"
sources: ["[[src-ftp-transmission-analysis]]", "[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-bcbs-lev]]", "[[src-tt50-2026-nhnn]]"]
relations: []
tags: [ftp, balance-sheet-optimization, alm, alco, lcr, nsfr, lev, irrbb, raroc, synthesis]
updated: 2026-10-17
reviewed:
---

## 1. Tổng Quan: FTP Như Một Động Cơ Điều Khiển Bảng Cân Đối Toàn Diện

Một trong những thách thức phức tạp nhất của Quản trị Tài sản Có - Tài sản Nợ (ALM) hiện đại là giải quyết bài toán xung đột mục tiêu đa chiều:
- **Tối đa hóa Lợi nhuận**: Gia tăng thu nhập lãi thuần (NII), biên lãi ròng (NIM) và tỷ suất sinh lời trên vốn (ROE/RAROC).
- **Tuân thủ Chuẩn mực Thanh khoản Khắt khe**: Duy trì đệm tài sản thanh khoản [[lcr|LCR]] $\ge 100\%$ và tỷ lệ nguồn vốn ổn định ròng [[nsfr|NSFR]] $\ge 100\%$.
- **Kiểm soát Rủi ro Lãi suất**: Giới hạn độ nhạy thu nhập [[net-interest-income-sensitivity|ΔNII]] và giá trị vốn chủ sở hữu [[economic-value-of-equity|ΔEVE]] trong các kịch bản sốc lãi suất chuẩn mực của [[bcbs-irrbb|BCBS]].
- **Kiểm soát Đòn bẩy và Vốn**: Thỏa mãn tỷ lệ an toàn vốn (CAR $\ge 8\%-10,5\%$) và chốt chặn tỷ lệ đòn bẩy Basel III ([[leverage-ratio|LEV]] $\ge 3\%$).

Nếu không có một cơ chế điều khiển thống nhất, các đơn vị kinh doanh (Business Units — BUs) tại các chi nhánh sẽ có xu hướng tối đa hóa doanh số cá nhân (cho vay các khoản tín dụng rủi ro cao, kỳ hạn dài để lấy lãi suất cao; hoặc huy động tiền gửi ngắn hạn giá rẻ), đẩy toàn bộ ngân hàng vào tình trạng căng thẳng thanh khoản và mất cân đối kỳ hạn nghiêm trọng [[src-choudhry-principles-banking#^choudhry-ftp-14]].

Nghiên cứu của Beata Lubinska (2020), Giáo sư Moorad Choudhry (2022) và thực tiễn ngân hàng tại Việt Nam khẳng định: **Funds Transfer Pricing (FTP) chính là động cơ điều khiển trung tâm (unified control engine) giúp Ủy ban ALCO dẫn dắt toàn bộ hệ thống đạt trạng thái tối ưu hóa bảng cân đối (Balance Sheet Optimization)** [[src-ftp-transmission-analysis#^ftp-trans-1]] [[src-vab-ftp#^vab-ftp-2]].

```
+---------------------------------------------------------------------------------------------------+
|               HỆ THỐNG ĐIỀU KHIỂN VÀ TỐI ƯU HÓA BẢNG CÂN ĐỐI QUA FTP (ALM STEERING)               |
+---------------------------------------------------------------------------------------------------+
|  CÁC RÀNG BUỘC PHÁP ĐỊNH VÀ QUẢN TRỊ (REGULATORY & INTERNAL BOUNDARIES)                           |
|  - Thanh khoản ngắn hạn:  LCR = HQLA / Net_Outflows >= 100%                                        |
|  - Cấu trúc thanh khoản:  NSFR = ASF / RSF >= 100%                                                |
|  - Chốt chặn đòn bẩy:     LEV = Tier 1 / Exposure Measure >= 3.0%                                 |
|  - Rủi ro lãi suất:       |ΔNII| <= 5% NII_budget;  |ΔEVE| <= 15% Tier 1 Capital                   |
|  - An toàn vốn:           CAR = Total Capital / RWA >= 10.5%                                      |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                          BÀI TOÁN TỐI ƯU HÓA TOÁN HỌC (MATHEMATICAL ENGINE)                       |
|                          MAX [ NII ]  hoặc  MAX [ RAROC toàn hàng ]                               |
|                          Biến điều khiển (Control Variables): Lãi suất FTP (VOF, COF)             |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                          CƠ CHẾ TRUYỀN DẪN VÀ ĐIỀU CHỈNH CỦA ALCO                                 |
|  - Thiếu LCR:             Tăng Spread kỳ hạn ngắn (<30D) -> Liability Center hút tiền gửi nhanh   |
|  - Thiếu NSFR:            Tăng Spread kỳ hạn dài (>1Y) -> Thưởng CASA lõi, phạt cho vay dài hạn   |
|  - Mất cân đối Repricing: Phạt khe hở kỳ hạn (Gap penalty) -> Khuyến khích Matched Funding        |
|  - Chạm trần RWA / LEV:   Tăng Capital Charge trong COF -> Ưu tiên tài sản RWA thấp (TPCP, HQLA)  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                          BẢNG CÂN ĐỐI ĐẠT ĐIỂM TỐI ƯU PARETO (PARETO FRONTIER)                    |
|  - Thanh khoản vững chắc (LCR, NSFR vượt chuẩn)                                                   |
|  - Lợi nhuận lãi thuần (NIM) được bảo vệ trước các chu kỳ biến động lãi suất                       |
|  - Sử dụng vốn hiệu quả nhất trên mỗi đồng rủi ro (Tối đa hóa RAROC và EVA)                       |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Mô Hình Toán Học Tối Ưu Hóa Bảng Cân Đối Bằng FTP

Về mặt định lượng, bài toán điều hành ALM toàn ngân hàng được mô hình hóa dưới dạng một bài toán quy hoạch tối ưu có ràng buộc (Constrained Mathematical Programming) [[src-ftp-transmission-analysis#^ftp-trans-14]]:

### 2.1 Hàm Mục Tiêu (Objective Function)
Ngân hàng tìm kiếm cơ cấu danh mục tài sản $A_i$ và tài sản nợ $L_j$ nhằm tối đa hóa thu nhập lãi thuần điều chỉnh rủi ro:

$$\max_{\{A_i, L_j\}} \quad \text{NII}_{\text{Risk-Adjusted}} = \sum_{i=1}^m A_i \cdot \Big( r_{A_i} - \text{EL}_i - \text{OpCost}_i \Big) - \sum_{j=1}^n L_j \cdot \Big( r_{L_j} + \text{OpCost}_j \Big)$$

Hoặc tối đa hóa tỷ suất sinh lời điều chỉnh theo rủi ro trên vốn kinh tế:
$$\max \quad \text{RAROC} = \frac{\text{NII} - \text{EL} - \text{Chi phí hoạt động}}{\text{Vốn kinh tế (Economic Capital)}}$$

### 2.2 Không Gian Ràng Buộc Đa Chiều (Multi-Regulatory Constraints)
1. **Ràng buộc Cân bằng Bảng cân đối (Balance Sheet Identity)**:
   $$\sum_{i=1}^m A_i = \sum_{j=1}^n L_j + \text{Equity}$$
2. **Ràng buộc Thanh khoản Ngắn hạn ([[lcr|LCR]])**:
   $$\text{LCR} = \frac{\text{HQLA}}{\sum_{k} \text{Dòng tiền ra thuần 30 ngày}_k} \ge 100\% \quad (\text{Mục tiêu nội bộ: } \ge 110\%-115\%)$$
3. **Ràng buộc Cấu trúc Nguồn vốn Ổn định Dài hạn ([[nsfr|NSFR]])**:
   $$\text{NSFR} = \frac{\sum_{j=1}^n L_j \cdot \text{ASF}_j + \text{Equity} \cdot 100\%}{\sum_{i=1}^m A_i \cdot \text{RSF}_i} \ge 100\% \quad (\text{Mục tiêu nội bộ: } \ge 105\%-108\%)$$
4. **Ràng buộc Tỷ lệ Đòn bẩy ([[leverage-ratio|LEV]])**:
   $$\text{LEV} = \frac{\text{Tier 1 Capital}}{\sum_{i=1}^m A_i + \text{Ngoại bảng quy đổi (CCF)}} \ge 3,0\% \quad (\text{Mục tiêu nội bộ: } \ge 4,0\%-5,0\%)$$
5. **Ràng buộc Rủi ro Lãi suất trên Sổ Ngân hàng ([[bcbs-irrbb|IRRBB]])**:
   $$\big| \Delta\text{NII}(\pm 200\text{ bps}) \big| \le \text{Hạn mức NII} \quad (\text{ví dụ: } 5\% \text{ tổng NII kế hoạch})$$
   $$\big| \Delta\text{EVE}(\pm 200\text{ bps}) \big| \le 15\% \cdot \text{Tier 1 Capital}$$
6. **Ràng buộc Tỷ lệ An toàn Vốn (CAR)**:
   $$\text{CAR} = \frac{\text{Vốn tự có}}{\sum_{i=1}^m A_i \cdot \text{RW}_i + \text{RWA}_{\text{Market}} + \text{RWA}_{\text{Op}}} \ge 8,0\% \quad (\text{kèm đệm: } \ge 10,5\%)$$

---

## 3. Cơ Chế FTP Là Biến Số Điều Khiển (FTP as the Control Variable)

Ngân hàng không thể ra lệnh trực tiếp cho hàng nghìn nhân viên tín dụng từ chối khách hàng hoặc ép khách hàng gửi tiền dài hạn bằng mệnh lệnh hành chính. **FTP đóng vai trò là "bàn tay vô hình" điều khiển hành vi phi tập trung của các đơn vị kinh doanh thông qua cơ chế giá cả thị trường nội bộ** [[src-ftp-transmission-analysis#^ftp-trans-13]]:

$$\text{FTP}_{\text{Asset}}(t, T) = \text{BaseRate}(t,T) + \text{LiqSpread}(T) \times \text{LCR}_{\text{adj}} \times \text{NSFR}_{\text{adj}} + \text{CreditSpread}(\text{rating}) \times \text{PD} \times \text{LGD} + \text{OptionCost} + \text{CapitalCharge}(\text{RWA} \times \text{CoE})$$

```
                   BÀI TOÁN TỐI ƯU HÓA ALM (Lagrangian Optimization)
                                        |
                   Nhân tử Lagrange (Shadow Prices của các Ràng buộc):
                   - λ_LCR   = Chi phí bóng của việc thiếu hụt 1 đồng LCR
                   - λ_NSFR  = Chi phí bóng của việc thiếu hụt 1 đồng NSFR
                   - λ_CAR   = Chi phí bóng của việc tiêu hao 1 đồng vốn
                                        |
                                        v
                 CHUYỂN HÓA TRỰC TIẾP THÀNH CÁC PHỤ PHÍ TRONG FTP:
                 - ΔSpread_short  = f(λ_LCR)
                 - ΔSpread_long   = f(λ_NSFR)
                 - Capital Charge = f(λ_CAR)
```

Khi một chỉ số an toàn tiệm cận giới hạn đỏ (ví dụ $\text{NSFR}$ tụt xuống $101\%$):
- Giá trị biên tế (shadow price $\lambda_{\text{NSFR}}$) tăng vọt.
- ALM tự động đẩy $\Delta\text{Spread}_{\text{long}}$ lên thêm $+50$ đến $+80 \text{ bps}$ [[src-ftp-transmission-analysis#^ftp-trans-8]].
- Chi nhánh nhận thấy giá bán vốn tiền gửi dài hạn (VOF 1Y-2Y) tăng lên mức cực kỳ hấp dẫn $\rightarrow$ tung chiến dịch huy động tiền gửi dài hạn.
- Đồng thời, chi nhánh nhận thấy giá mua vốn cho vay trung dài hạn (COF 3Y-5Y) trở nên đắt đỏ $\rightarrow$ tự động thu hẹp cho vay dài hạn, chuyển sang giải ngân các khoản vay ngắn hạn có vòng quay nhanh.
- **Kết quả là NSFR được tái lập mà ALCO không cần can thiệp vi mô vào từng quyết định tác nghiệp**.

---

## 4. Tích Hợp Chi Phí Tuân Thủ Pháp Định Trong Bối Cảnh Việt Nam

Điểm độc đáo trong thực tiễn ngân hàng Việt Nam (theo phản ánh từ tài liệu tư vấn VietABank) là hệ thống FTP tích hợp chặt chẽ các quy định pháp định đặc thù của Ngân hàng Nhà nước [[src-vab-ftp#^vab-ftp-2]]:

| Cấu phần trong Biểu giá FTP | Quy định Pháp định Neo theo | Tác động Điều khiển Bảng cân đối |
| :--- | :--- | :--- |
| **Chi phí Dự trữ Bắt buộc (DTBB)** | Thông tư 30/2019/TT-NHNN | Phân bổ chi phí negative carry vào COF; thúc đẩy cho vay chọn lọc tài sản sinh lời cao [[src-vab-ftp#^vab-ftp-9]]. |
| **Chi phí Bảo hiểm Tiền gửi (BHTG)** | Luật BHTG & NHNN (0,15%/năm) | Chuyển toàn bộ phí BHTG sang bên sử dụng vốn; giải phóng áp lực chi phí cho mạng lưới huy động bán lẻ [[src-vab-ftp#^vab-ftp-8]]. |
| **Liquidity Buffer Premium** | TT22/2019 (chuyển tiếp theo TT50 Đ13.4 [[src-tt50-2026-nhnn#^d13-4]]), LCR TT50 từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] | Tính bù chi phí nắm giữ tài sản thanh khoản cao (TPCP, tín phiếu) vào mọi khoản tín dụng [[src-vab-ftp#^vab-ftp-10]]. |
| **Term Liquidity Premium (TLP)** | Quản trị rủi ro thanh khoản kỳ hạn | Bắt buộc các khoản vay thả nổi phải trả đúng chi phí thanh khoản dài hạn gốc [[src-vab-ftp#^vab-ftp-11]]. |
| **CASA Replicating Portfolio** | Quản trị thanh khoản phi kỳ hạn | Định giá tiền gửi không kỳ hạn theo tỷ lệ lõi (core CASA) hưởng VOF dài hạn [[src-vab-ftp#^vab-ftp-15]]. |
| **Option Charges (Prepayment/TDRR)** | Thông tư 04/2022/TT-NHNN | Phạt rút tiền gửi trước hạn; định giá cho vay theo kỳ hạn hiệu lực mô hình hóa [[src-vab-ftp#^vab-ftp-19]]. |

---

## 5. Quy Trình Vận Hành ALCO: Vòng Lặp Điều Khiển Động (Dynamic Steering Loop)

Để đảm bảo FTP duy trì vai trò động cơ tối ưu hóa liên tục, chu trình vận hành ALCO được chuẩn hóa thành 5 giai đoạn khép kín [[src-ftp-transmission-analysis#^ftp-trans-13]]:

```
[1. GIÁM SÁT REAL-TIME]
Theo dõi LCR, NSFR, LEV, ΔNII, ΔEVE, CAR và diễn biến huy động - tín dụng
            |
            v
[2. NHẬN DIỆN LỆCH PHA & ĐIỀU CHỈNH FTP]
Ủy ban ALCO họp định kỳ (tháng) hoặc bất thường; hiệu chỉnh đường cong VOF/COF và spreads
            |
            v
[3. THỰC THI TRUYỀN DẪN NỘI BỘ]
Ban hành Biểu lãi suất FTP Thị trường 1 cho toàn mạng lưới chi nhánh và TT2 cho Treasury
            |
            v
[4. HÀNH VI TỰ ĐIỀU CHỈNH CỦA ĐƠN VỊ KINH DOANH]
BUs điều chỉnh biểu lãi suất khách hàng, lựa chọn cấu trúc sản phẩm tối ưu hóa RAROC
            |
            v
[5. TÁI ĐỊNH HÌNH BẢNG CÂN ĐỐI & BACKTEST]
Bảng cân đối chuyển dịch về vùng an toàn; kiểm định hiệu quả của các hệ số phản hồi (α, β, γ)
```

Quy trình này biến ALM từ một chức năng thụ động (chỉ đo lường và lập báo cáo khi rủi ro đã xảy ra) thành **một trung tâm kiến tạo giá trị chủ động (active value creation center)**, bảo vệ toàn vẹn thanh khoản ngân hàng đồng thời tối ưu hóa lợi nhuận của cổ đông trên cơ sở bền vững dài hạn.

## Khái niệm và Liên kết
- [[ftp-transmission-mechanism]]: Chi tiết phân tích các kênh truyền dẫn thanh khoản, lãi suất, tín dụng và vốn.
- [[ftp-pricing-methodology]]: Phương pháp luận định giá chi tiết VOF, COF, phụ phí pháp định và quyền chọn ẩn.
- [[liquidity-transfer-pricing]]: Tổng quan lý thuyết định giá điều chuyển thanh khoản nội bộ.
- [[synthetic-balance-sheet-liquidity-risk]]: Bảng cân đối thanh khoản tổng hợp và động lực dòng tiền.
- [[practical-alm-liquidity-governance]]: Khung quản trị thanh khoản thực chiến theo Choudhry.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn Basel III.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn Basel III.
- [[leverage-ratio]]: Tỷ lệ đòn bẩy Basel III.
- [[bcbs-irrbb]]: Chuẩn mực rủi ro lãi suất trên sổ ngân hàng.

## Căn cứ pháp lý VN của đệm thanh khoản (rà 2026-10-20)
- VAB dẫn TT22/2019 cho phần bù tài sản thanh khoản [[src-vab-ftp#^vab-ftp-10]], cho danh mục tài sản thanh khoản (Phụ lục 3 TT22) [[src-vab-ftp#^vab-ftp-43]] và cho tỷ lệ rút tiền KKH tối thiểu 15% khi chưa có mô hình hành vi [[src-vab-ftp#^vab-ftp-44]].
- TT50/2026 sửa Điều 2 TT22: đối tượng của TT22 chỉ còn ngân hàng hợp tác xã và NHTM đang thực hiện Đ23.3 TT41/2016 [[src-tt50-2026-nhnn#^d37-3a]].
- Từ khi TT50 có hiệu lực đến trước ngày áp dụng LCR/NSFR, ngân hàng vẫn phải tuân thủ và báo cáo tỷ lệ dự trữ thanh khoản, tỷ lệ khả năng chi trả 30 ngày, tỷ lệ nguồn vốn ngắn hạn cho vay trung dài hạn và LDR theo TT22 [[src-tt50-2026-nhnn#^d13-4]].
- Từ 01/10/2028 ngân hàng phải áp dụng LCR và NSFR [[src-tt50-2026-nhnn#^d13-1]]; khi đó các tỷ lệ cũ của TT22 không phải tuân thủ nhưng vẫn phải báo cáo [[src-tt50-2026-nhnn#^d13-5]].

*Diễn giải:* trong synthesis này, "TT22" đọc là căn cứ chuyển tiếp theo TT50 Đ13.4. Sau khi ngân hàng áp dụng LCR, đệm thanh khoản trong phần bù FTP nên đo theo [[hqla]] của TT50, và tỷ lệ rút KKH 15% (dẫn từ Phụ lục 3 TT22) mất tính bắt buộc; ngân hàng cần căn cứ khác (mô hình hành vi hoặc hệ số rút tiền của TT50) [cần nguồn: src-tt50-2026-nhnn PL1 cho hệ số rút tiền tiền gửi KKH].

## Bất định
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế.
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
- [2026-10-19] ingest src-tt83-2025-nhnn PL3: [[raroc]] là chỉ tiêu khẩu vị rủi ro trong báo cáo ICAAP gửi NHNN, cùng ROE và CAR_target, cho năm t0 đến t0+3 [[src-tt83-2025-nhnn#^pl3-2]]; cần rà lại chỗ nhắc RAROC.
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04: đã có node [[net-interest-margin]] (định nghĩa, case ChoudWest 5 kịch bản: NII và NIM có thể đi ngược chiều, buffer £1,5bn làm NIM −0,50 điểm %, Table 1.10 hành động quản lý NIM); cần rà lại chỗ dùng NIM làm chỉ số đánh đổi.
- [2026-10-19] ingest --node cost-of-funds: đã có node [[cost-of-funds]] (COF: giá bán vốn FTP cho tài sản gồm 7 cấu phần [[src-vab-ftp#^vab-ftp-7]]); cần rà lại chỗ nhắc đường cong VOF/COF.
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p02–p04: [[funds-transfer-pricing]] có căn cứ Basel cho phần thanh khoản (BCBS 144 P4: liquidity charge gán tới trạng thái/danh mục/giao dịch, tính thời gian nắm giữ, thanh khoản thị trường, lợi ích nguồn vốn ổn định, xét stress), thay cho "[cần nguồn]" chuẩn BCBS về FTP; cần rà lại phần căn cứ Basel.
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M2, C2-M4: [[leverage-ratio]] VN chưa có ngưỡng cố định (Thống đốc quyết định khi cần thiết); [[loan-to-deposit-ratio]] VN tối đa 95% từ khi áp dụng LCR/NSFR; cần rà lại câu về ngưỡng LR/LDR tại VN.
- [2026-10-20] ingest src-tt50-2026-nhnn PL2: [[available-stable-funding]], [[required-stable-funding]], [[nsfr]] có hệ số ASF/RSF của VN (khác Basel: tiền gửi bán lẻ ≥ 1 năm được rút trước hạn chỉ 95%/90%; phải đòi Chính phủ/KBNN RSF 50–65%; add-on nợ phái sinh 10%); cần rà lại các ví dụ tính NSFR và bảng hệ số.
- [2026-10-20] ingest src-tt50-2026-nhnn PL1: [[lcr]], [[hqla]], [[cash-outflows]], [[retail-deposit-stability]], [[level-1-assets]], [[level-2-assets]] có hệ số VN (HQLA cấp 1/2A/2B 100/85/75–50%, run-off bán lẻ 5%/10%, tiền gửi ngoại tệ luôn kém ổn định, DNNVV ≤ 30 tỷ đồng, cổ phiếu VN30 vào cấp 2B); cần rà lại ví dụ tính LCR và bảng hệ số.
