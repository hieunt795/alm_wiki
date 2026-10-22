---
title: "Cơ Chế Truyền Dẫn FTP Đến Các Yếu Tố Rủi Ro (FTP Transmission Mechanism)"
aliases: [FTP Transmission Mechanism, Cơ chế truyền dẫn FTP, Kênh truyền dẫn FTP, FTP Risk Transmission]
type: concept
domains: [alm, product]
status: active
maturity: draft
sources: ["[[src-ftp-transmission-analysis]]", "[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: priced-by, to: "[[lcr]]", cite: "[[src-ftp-transmission-analysis#^ftp-trans-8]]"}
  - {type: priced-by, to: "[[nsfr]]", cite: "[[src-ftp-transmission-analysis#^ftp-trans-8]]"}
  - {type: priced-by, to: "[[bcbs-irrbb]]", cite: "[[src-ftp-transmission-analysis#^ftp-trans-9]]"}
  - {type: input-to, to: "[[ftp-pricing-methodology]]", cite: "[[src-vab-ftp#^vab-ftp-5]]"}
  - {type: part-of, to: "[[funds-transfer-pricing]]", cite: "[[src-ftp-transmission-analysis#^ftp-trans-2]]"}
tags: [ftp, transmission, liquidity-risk, irrbb, credit-risk, raroc, economic-capital, feedback-loop, concept]
updated: 2026-10-21
reviewed:
---

## 1. Bản Chất Hệ Thống Điều Khiển Trung Tâm (Unified Control Mechanism)

Trong cấu trúc ngân hàng hiện đại, **Funds Transfer Pricing (FTP)** không chỉ thuần túy là công cụ hạch toán kế toán quản trị để phân bổ doanh thu chi phí giữa các khối kinh doanh. Nghiên cứu lý thuyết ALM của Beata Lubinska (2020) và thực tiễn điều hành ngân hàng khẳng định rằng **FTP đóng vai trò là một hệ thống điều khiển trung tâm (unified control mechanism)** của toàn bộ bảng cân đối tài sản - nợ [[src-ftp-transmission-analysis#^ftp-trans-1]].

```
+---------------------------------------------------------------------------------------------------+
|                  HỆ THỐNG ĐIỀU KHIỂN TRUNG TÂM FTP (UNIFIED CONTROL MECHANISM)                    |
+---------------------------------------------------------------------------------------------------+
|                                  +-----------------------+                                        |
|                                  |   ỦY BAN ALCO ([[alco]]) / ALM   |                                        |
|                                  |  (Chiến lược & Hạn mức)|                                       |
|                                  +-----------+-----------+                                        |
|                                              | (Điều chỉnh FTP Curve & Spreads)                   |
|                                              v                                                    |
|                                  +-----------------------+                                        |
|                                  |      FTP ENGINE       |                                        |
|                                  |  (Định giá & Phân bổ) |                                        |
|                                  +---+-------+-------+---+                                        |
|                                      |       |       |                                            |
|         +----------------------------+       |       +----------------------------+               |
|         | Kênh RRTK                          | Kênh RRLS                          | Kênh RRTD & Vốn|
|         v                                    v                                    v               |
|  +--------------+                     +--------------+                     +--------------+       |
|  |   RỦI RO     |                     |    RỦI RO    |                     |    RỦI RO    |       |
|  | THANH KHOẢN  |                     |   LÃI SUẤT   |                     | TÍN DỤNG & VỐN|      |
|  | (LCR, NSFR)  |                     | (ΔNII, ΔEVE) |                     | (EL, RAROC ([[raroc]]))  |       |
|  +--------------+                     +--------------+                     +--------------+       |
|         |                                    |                                    |               |
|         +----------------------------+       |       +----------------------------+               |
|                                      v       v       v                                            |
|                        +-------------------------------------------+                              |
|                        | TÁC ĐỘNG HÀNH VI ĐƠN VỊ KINH DOANH (BUs)  |                              |
|                        | - Asset Centers: Điều chỉnh giá cho vay   |                              |
|                        | - Liability Centers: Đẩy mạnh huy động lõi|                              |
|                        +---------------------+---------------------+                              |
|                                              |                                                    |
|                                              v (Tái định hình danh mục)                           |
|                        +-------------------------------------------+                              |
|                        |     BẢNG CÂN ĐỐI KẾ TOÁN TỐI ƯU HÓA       |                              |
|                        +---------------------+---------------------+                              |
|                                              | (Giám sát chỉ số phản hồi)                         |
|                                              +----------------------------+ (Feedback Loop)       |
+---------------------------------------------------------------------------|-----------------------+
```

FTP tác động đồng thời đến ba nhóm rủi ro trọng yếu trên bảng cân đối ngân hàng thông qua ba kênh truyền dẫn chuyên biệt nhưng có tính chất tương tác chặt chẽ [[src-ftp-transmission-analysis#^ftp-trans-2]]:
1. **Kênh Rủi ro Thanh khoản (Liquidity Risk Channel)**: Điều tiết cấu trúc kỳ hạn và tuân thủ các tỷ lệ an toàn thanh khoản ([[lcr|LCR]], [[nsfr|NSFR]]).
2. **Kênh Rủi ro Lãi suất trên Sổ Ngân hàng (IRRBB Channel)**: Cô lập rủi ro tái định giá khỏi các đơn vị kinh doanh và điều khiển khe hở kỳ hạn ([[gap-risk]]), bảo vệ [[net-interest-income-sensitivity|ΔNII]] và [[economic-value-of-equity|ΔEVE]].
3. **Kênh Rủi ro Tín dụng và Vốn (Credit Risk & Capital Allocation Channel)**: Nội bộ hóa chi phí tổn thất kỳ vọng (EL) và chi phí vốn kinh tế (Economic Capital, xem [[economic-capital]]), định hướng tăng trưởng danh mục theo thước đo RAROC.

$$\text{FTP Rate} = \text{Base Rate} + \text{Liquidity Spread} + \text{Credit Spread} + \text{Optionality Cost}$$
[[src-ftp-transmission-analysis#^ftp-trans-3]]

---

## 2. Kênh Truyền Dẫn Thứ Nhất: Rủi Ro Thanh Khoản (Liquidity Risk Channel)

### 2.1 Cơ Chế Truyền Dẫn Qua Liquidity Spread
Thành phần bù thanh khoản (Liquidity Spread) trong biểu giá FTP phản ánh chi phí cơ hội và chi phí huy động vốn biên tế trên thị trường bán buôn [[src-ftp-transmission-analysis#^ftp-trans-5]]. Kênh truyền dẫn này vận hành theo chu trình 4 bước:

1. **Thu nhận tín hiệu (Signal Recognition)**: ALM theo dõi liên tục trạng thái thanh khoản thực tế so với mục tiêu do ALCO đề ra, đặc biệt là tỷ lệ [[lcr|LCR]] (thanh khoản 30 ngày) và [[nsfr|NSFR]] (nguồn vốn ổn định 1 năm).
2. **Điều chỉnh đường cong thanh khoản (Liquidity Spread Calibration)**:
   - Khi $\text{LCR} < \text{LCR}_{\text{target}}$ (áp lực thiếu đệm thanh khoản ngắn hạn): ALM tăng mạnh spread ở các kỳ hạn ngắn (qua đêm đến 1 tháng) [[src-ftp-transmission-analysis#^ftp-trans-8]].
   - Khi $\text{NSFR} < \text{NSFR}_{\text{target}}$ (thiếu hụt nguồn vốn trung dài hạn ổn định để tài trợ tài sản): ALM tăng mạnh spread ở các kỳ hạn từ 6 tháng đến 2 năm trở lên [[src-ftp-transmission-analysis#^ftp-trans-8]].
3. **Thay đổi hành vi của các Đơn vị Kinh doanh (Business Units Behavioral Shift)**:
   - **Liability Centers (Khối Huy động)**: Nhận được giá mua vốn (VOF) cao hơn từ ALM, tạo động lực cạnh tranh lãi suất để hút mạnh tiền gửi tại các kỳ hạn mà ngân hàng đang thiếu hụt.
   - **Asset Centers (Khối Cho vay)**: Phải gánh chi phí mua vốn ([[cost-of-funds|COF]]) đắt hơn, buộc phải nâng lãi suất cho vay đối với khách hàng, từ đó làm giảm tốc độ tăng trưởng tín dụng tại các kỳ hạn làm căng thẳng thanh khoản.
4. **Cải thiện chỉ số thanh khoản (Balance Sheet Restoration)**: Dòng tiền vào gia tăng ở các kỳ hạn mục tiêu và dòng tài sản dài hạn được kiểm soát, đưa các chỉ số thanh khoản trở lại vùng an toàn.

### 2.2 Công Thức Điều Chỉnh Định Lượng Thanh Khoản
Mô hình toán học điều tiết thanh khoản qua FTP được lượng hóa:

$$\Delta\text{Spread}_{\text{short}} = \alpha \times \max(0, \, \text{LCR}_{\text{target}} - \text{LCR}_{\text{actual}})$$
$$\Delta\text{Spread}_{\text{long}} = \beta \times \max(0, \, \text{NSFR}_{\text{target}} - \text{NSFR}_{\text{actual}})$$

Trong đó:
- $\alpha, \beta$: Hệ số nhạy cảm truyền dẫn do ALCO quyết định căn cứ theo độ co giãn của cung cầu tiền gửi và tín dụng trên thị trường.

---

## 3. Kênh Truyền Dẫn Thứ Hai: Rủi Ro Lãi Suất Sổ Ngân Hàng (IRRBB Channel)

### 3.1 Nguyên Tắc Tách Biệt và Chuyển Giao Rủi Ro Tập Trung (Matched-Maturity Risk Transfer)
Nguyên tắc cốt lõi của FTP hiện đại là **cô lập hoàn toàn rủi ro lãi suất khỏi các đơn vị kinh doanh và chuyển giao tập trung về Trung tâm Quản lý Vốn (ALM/Treasury)** [[src-ftp-transmission-analysis#^ftp-trans-9]]:

- Khi chi nhánh giải ngân khoản vay cố định 5 năm lãi suất 10%, chi nhánh được ALM cung cấp vốn với giá FTP cố định 5 năm (ví dụ 7,5%). Chi nhánh khóa chặt biên lợi nhuận ròng (margin) cố định 2,5% trong suốt 5 năm, hoàn toàn không bị ảnh hưởng nếu lãi suất thị trường tăng vọt lên 12% [[src-ftp-transmission-analysis#^ftp-trans-10]].
- Khi chi nhánh huy động tiền gửi kỳ hạn 3 tháng lãi suất 4%, chi nhánh bán vốn lại cho ALM với giá FTP 3 tháng là 5,5%, hưởng biên lợi nhuận cố định 1,5%.
- **Toàn bộ khe hở tái định giá (repricing gap) giữa tài sản 5 năm và nợ 3 tháng được chuyển giao toàn bộ về ALM** [[src-ftp-transmission-analysis#^ftp-trans-10]]. ALM có chuyên môn và công cụ phái sinh (IRS, CCS) để phòng ngừa rủi ro này trên toàn danh mục. Xem [[repricing-gap-analysis]].

### 3.2 Cơ Chế Phạt/Thưởng Khe Hở Kỳ Hạn (Mismatch Penalty & Steering)
Khi độ nhạy thu nhập lãi thuần [[net-interest-income-sensitivity|ΔNII]] hoặc giá trị vốn chủ sở hữu [[economic-value-of-equity|ΔEVE]] tiệm cận hạn mức cảnh báo:
- ALM áp dụng phụ phí phạt tái định giá ($\text{Spread}_{\text{mismatch}}$) đối với các giao dịch làm nới rộng khe hở kỳ hạn bất lợi:
  $$\text{Spread}_{\text{mismatch}} = \gamma \times \frac{|\text{Gap}_{\text{actual}}|}{\text{Gap}_{\text{limit}}}$$
- Đồng thời thưởng biên độ cho các giao dịch giúp đóng khe hở kỳ hạn ($\text{Reward}_{\text{match}} = -\delta \times \text{Matched Ratio}$).

### 3.3 Quản Lý Rủi Ro Cơ Sở (Basis Risk Management)
Khi tài sản và nợ được neo theo các chỉ số lãi suất tham chiếu khác nhau (ví dụ tài sản neo theo lãi suất cho vay tham chiếu 12 tháng của Big4, còn nợ huy động neo theo VNIBOR 3 tháng):
- ALM thiết lập các đường cong FTP riêng biệt cho từng benchmark và tính toán chi phí hoán đổi cơ sở (basis swap cost) vào giá FTP để đơn vị kinh doanh nội bộ hóa rủi ro này.

---

## 4. Kênh Truyền Dẫn Thứ Ba: Rủi Ro Tín Dụng, Vốn Kinh Tế và RAROC (Credit Risk & Capital Allocation Channel)

Quy định quản lý rủi ro tín dụng tại VN: xem [[credit-risk-management]].

### 4.1 Định Giá Theo Xếp Hạng Tín Nhiệm (Rating-based Pricing Grid)
FTP kết nối trực tiếp với hệ thống xếp hạng tín dụng nội bộ của ngân hàng:
- **Tổn thất kỳ vọng (Expected Loss — EL, [[expected-loss]])**: Được tính trực tiếp vào giá bán vốn tín dụng [[src-ftp-transmission-analysis#^ftp-trans-11]]:
  $$\text{EL Charge} = \text{PD} \times \text{LGD} \times \text{EAD}$$
- Khách hàng có xếp hạng rủi ro cao (PD lớn) sẽ bị áp Credit Spread cao trong giá FTP, buộc đơn vị kinh doanh phải tính lãi suất cho vay cao tương ứng để bù đắp rủi ro.

### 4.2 Chi Phí Phân Bổ Vốn Kinh Tế và Đòn Bẩy (Economic Capital Charge)
Ngoài tổn thất kỳ vọng được trích lập dự phòng, tài sản tín dụng còn tiêu hao vốn tự có theo quy định an toàn vốn (CAR), tỷ lệ đòn bẩy ([[leverage-ratio|LEV]]) và vốn kinh tế nội bộ ([[economic-capital|Economic Capital — EC]]) [[src-choudhry-principles-banking#^choudhry-crd-10]]:

$$\text{Capital Charge} = \frac{\text{Economic Capital}}{\text{Exposure}} \times \text{Cost of Equity (CoE)} = \text{EC Density} \times \text{Hurdle Rate}$$

Trong mô hình chuẩn hóa dựa trên tài sản tính theo rủi ro (RWA):
$$\text{Capital Charge} = \text{RWA Density} \times \text{Capital Ratio Target} \times \text{Cost of Equity (CoE)}$$
*(Căn cứ: [[src-ftp-transmission-analysis#^ftp-trans-12]])*.

Khi tỷ lệ an toàn vốn CAR của ngân hàng suy giảm hoặc tiệm cận hạn mức an toàn, ALM nâng hệ số Capital Charge trong công thức FTP. Đơn vị kinh doanh lập tức nhận thấy các khoản vay có trọng số rủi ro tín dụng cao (RWA 100%–150% như bất động sản, tài trợ dự án) trở nên đắt đỏ, từ đó chủ động chuyển dịch sang các tài sản có RWA thấp (như trái phiếu chính phủ RWA 0%, cho vay thế chấp nhà ở an toàn RWA 25%–50%).

### 4.3 Tích Hợp RAROC Cấp Độ Từng Giao Dịch và Toàn Bảng Cân Đối
FTP là điều kiện tiên quyết để vận hành mô hình quản trị hiệu quả trên cơ sở rủi ro (Risk-Adjusted Return on Capital — RAROC) [[src-choudhry-principles-banking#^choudhry-crd-6]]:

$$\text{RAROC}_{\text{deal}} = \frac{\text{Lãi suất cho vay} - \text{FTP COF} - \text{EL} - \text{Chi phí hoạt động}}{\text{Vốn kinh tế (Economic Capital)}}$$

Một giao dịch chỉ được phê duyệt khi $\text{RAROC} \ge \text{Hurdle Rate}$ (lợi nhuận đòi hỏi của cổ đông, thường 12%–15% theo Moorad Choudhry [[src-choudhry-principles-banking#^choudhry-crd-10]]). Thước đo giá trị thặng dư kinh tế cho cổ đông (Shareholder Value Added — SVA / EVA) được xác lập:
$$\text{SVA} = (\text{RAROC} - \text{Hurdle Rate}) \times \text{Economic Capital}$$

Nhờ có FTP phản ánh đúng chi phí vốn và rủi ro, chỉ tiêu RAROC mới phản ánh chính xác giá trị kinh tế thực sự của từng hợp đồng tín dụng mà không bị bóp méo bởi chuyển đổi kỳ hạn ([[maturity-transformation]]).

### 4.4 Nghịch Lý Đánh Đổi Động Lực Học giữa NIM và RAROC (NIM - RAROC Trade-off Paradox)
Trong thực tiễn điều hành ALM, tối ưu hóa đơn thuần Biên Lãi thuần (NIM) thường dẫn đến xung đột trực diện với mục tiêu tối ưu hóa tỷ suất sinh lời trên vốn (RAROC):

| Danh mục Tài sản | Lãi suất | Chi phí FTP COF | NIM Danh nghĩa | Mật độ RWA / EC | Tổn thất EL | Chi phí Hoạt động | RAROC | Giá trị Gia tăng SVA |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **A. Vay Tiêu dùng / BĐS rủi ro** | 10.5% | 4.5% | **6.0%** (Rất cao) | 150% ($EC \approx 15\%$) | 2.5% | 1.5% | **13.3%** | $+0.20\%$ (Biên mỏng) |
| **B. Cho vay Mua nhà Thế chấp chuẩn** | 7.5% | 4.5% | **3.0%** (Trung bình) | 35% ($EC \approx 3.5\%$) | 0.2% | 0.8% | **57.1%** | $\mathbf{+1.58\%}$ (Vượt trội) |
| **C. Trái phiếu Chính phủ L1** | 3.5% | 3.0% | **0.5%** (Rất mỏng) | 0% ($EC \approx 0\%$) | 0.0% | 0.1% | $\boldsymbol{\infty}$ | Thanh khoản & CAR tuyệt đối |

*Nghịch lý nhận diện:*
- Nếu chi nhánh chỉ được giao KPI theo doanh số hoặc NIM, họ sẽ tập trung toàn lực vào **Danh mục A** vì mang lại NIM 6.0%. Nhưng danh mục này tiêu tốn tới 15% Vốn Kinh tế và chịu EL lớn, chỉ tạo ra RAROC 13.3% (sát ngưỡng Hurdle Rate 12%).
- Ngược lại, **Danh mục B** có NIM chỉ 3.0% nhưng do tiêu tốn rất ít vốn kinh tế (EC chỉ 3.5%), RAROC đạt tới 57.1%, tạo ra SVA cao gấp 8 lần Danh mục A!
- **Cơ chế Truyền dẫn FTP hóa giải nghịch lý**: Bằng cách tính trực tiếp $\text{Capital Charge} = \text{EC Density} \times \text{Hurdle Rate}$ vào biểu giá COF (Danh mục A bị cộng thêm $+1.8\%$, Danh mục B chỉ bị cộng $+0.42\%$), FTP triệt tiêu ảo tưởng lợi nhuận của Danh mục A, buộc chi nhánh phải hướng dòng tín dụng vào Danh mục B để tối ưu hóa RAROC và an toàn vốn CAR toàn hàng.

### 4.5 Khung Định lượng Vốn Kinh tế và RAROC theo Chuẩn mực Việt Nam (Thông tư 83/2025/TT-NHNN)
Theo quy chuẩn của Ngân hàng Nhà nước tại Thông tư 83/2025/TT-NHNN:
1. **Khái niệm và Vị trí Quản trị**: RAROC là một trong các chỉ tiêu thu nhập cốt lõi trong Khung khẩu vị rủi ro ([[risk-appetite]]), được Hội đồng Quản trị phê duyệt và định kỳ báo cáo NHNN trong hồ sơ ICAAP từ năm $t_0$ đến $t_0+3$ [[src-tt83-2025-nhnn#^d19-2]] [[src-tt83-2025-nhnn#^pl3-2]].
2. **Công thức Đo lường Vốn Kinh tế ($C_E$)**: Vốn kinh tế của ngân hàng được xác định theo Phụ lục VI TT83 [[src-tt83-2025-nhnn#^pl6-1a]]:
   $$C_E = RWA^*_E \times CAR_{\text{Target}} + \Delta RWA_B \times CAR_R$$
   Trong đó, tổng tài sản tính theo rủi ro ở kịch bản bình thường $RWA^*_E$ bao gồm 6 cấu phần rủi ro trọng yếu [[src-tt83-2025-nhnn#^pl6-1b]]:
   $$RWA^*_E = RWA_{CR} + RWA_{OR} + RWA_{MR} + RWA_{IRRBB} + RWA_{COR} + RWA_{OMR}$$
   *(Lưu ý: Rủi ro thanh khoản không tính vào $RWA^*_E$ mà được kiểm soát riêng biệt qua các tỷ lệ LCR, NSFR và LDR theo TT50/2026 [[src-tt83-2025-nhnn#^pl6-1b]])*.
3. **Công thức RAROC Toàn hàng theo Pháp lệnh**:
   $$RAROC = \frac{\text{Tổng lợi nhuận trước thuế}}{C_E}$$
   [[src-tt83-2025-nhnn#^pl6-iii]]
   *Ý nghĩa ALM:* Vị thế rủi ro lãi suất sổ ngân hàng lớn ($RWA_{IRRBB}$) sẽ làm phình to $C_E$ và trực tiếp làm suy giảm RAROC toàn ngân hàng, ngay cả khi NII không đổi. FTP đóng vai trò truyền dẫn chi phí này thông qua phí phạt khe hở kỳ hạn để bảo toàn RAROC mục tiêu.

---

## 5. Vòng Phản Hồi Tích Hợp và Trạng Thái Cân Bằng Động (Integrated Feedback Loop & Dynamic Equilibrium)

Ba kênh truyền dẫn rủi ro của FTP không vận hành biệt lập mà tạo thành một **vòng phản hồi khép kín (closed feedback loop)** [[src-ftp-transmission-analysis#^ftp-trans-13]]:

$$\text{Tín hiệu An toàn (LCR, NSFR, ΔNII, CAR)} \longrightarrow \text{Hiệu chỉnh Đường cong FTP} \longrightarrow \text{Thay đổi Hành vi Chi nhánh/Khối KD} \longrightarrow \text{Tái cấu trúc Bảng cân đối} \longrightarrow \text{Cải thiện Chỉ số Rủi ro} \longrightarrow \text{Tái cân bằng}$$

```
                           +-----------------------------------+
                           | TÍN HIỆU GIÁM SÁT AN TOÀN VỐN & TK|
                           | LCR, NSFR, ΔNII, ΔEVE, CAR, LEV   |
                           +-----------------+-----------------+
                                             |
                                             v
                           +-----------------------------------+
                           |    HIỆU CHỈNH CẤU PHẦN FTP        |
                           | ΔSpread_short, ΔSpread_long, CoE  |
                           +-----------------+-----------------+
                                             |
                                             v
                           +-----------------------------------+
                           | HÀNH VI ĐƠN VỊ KINH DOANH (BUs)   |
                           | Cơ cấu kỳ hạn tiền gửi, giá vay   |
                           +-----------------+-----------------+
                                             |
                                             v
                           +-----------------------------------+
                           | DÒNG TIỀN VÀ BẢNG CÂN ĐỐI TÁI LẬP |
                           | Cân bằng Thanh khoản & Kỳ hạn     |
                           +-----------------+-----------------+
                                             |
                                             +----------> (Vòng lặp tái giám sát định kỳ)
```

### Trạng Thái Cân Bằng Động (Equilibrium States):
- **Cân bằng Thanh khoản**: Khi LCR và NSFR đạt vùng mục tiêu an toàn, ALM hạ các phụ phí thanh khoản về mức cơ sở chuẩn. Ngân hàng không còn phải trả lãi suất ưu đãi quá mức cho huy động dài hạn.
- **Cân bằng Lãi suất**: Khe hở định giá lại nằm trong ngưỡng dung nợ rủi ro, NIM được bảo vệ ổn định trước các cú sốc lãi suất thị trường $\pm 200 \text{ bps}$.
- **Cân bằng Tín dụng & Vốn**: Tỷ lệ CAR và Đòn bẩy có đệm an toàn vững chắc, danh mục tín dụng tạo ra RAROC tối ưu.

## Khái niệm và Liên kết
- [[liquidity-transfer-pricing]]: Tổng quan lý thuyết định giá điều chuyển thanh khoản nội bộ.
- [[ftp-pricing-methodology]]: Phương pháp định giá chi tiết VOF, COF, chi phí dự trữ bắt buộc, bảo hiểm tiền gửi và quyền chọn ẩn.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[bcbs-irrbb]]: Rủi ro lãi suất trên sổ ngân hàng.
- [[net-interest-income-sensitivity]]: Độ nhạy thu nhập lãi thuần.
- [[economic-value-of-equity]]: Độ nhạy giá trị kinh tế của vốn chủ sở hữu.
