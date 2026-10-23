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
  - {type: input-to, to: "[[ftp-pricing-methodology]]", cite: "[[src-vab-ftp#^vab-ftp-5]]"}
  - {type: part-of, to: "[[funds-transfer-pricing]]", cite: "[[src-ftp-transmission-analysis#^ftp-trans-2]]"}
tags: [ftp, transmission, liquidity-risk, irrbb, credit-risk, raroc, economic-capital, feedback-loop, concept]
updated: 2026-10-22
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

1. **Thu nhận tín hiệu (Signal Recognition)**: ALM theo dõi liên tục [[lcr|LCR]], [[nsfr|NSFR]], Survival Horizon và Structural Ratio; chỉ số tiến gần hoặc vi phạm ngưỡng cảnh báo thì kích hoạt điều chỉnh [[src-ftp-transmission-analysis#^ftp-trans-17]].
2. **Điều chỉnh đường cong thanh khoản (Liquidity Spread Calibration)**:
   - LCR thấp (thiếu thanh khoản ngắn hạn): tăng spread cho tenor ngắn (O/N đến 30 ngày) [[src-ftp-transmission-analysis#^ftp-trans-8]].
   - NSFR thấp (thiếu nguồn vốn ổn định): tăng spread cho tenor dài (6M đến 2Y trở lên) [[src-ftp-transmission-analysis#^ftp-trans-8]].
3. **Thay đổi hành vi của các Đơn vị Kinh doanh (Business Units Behavioral Shift)** [[src-ftp-transmission-analysis#^ftp-trans-18]]:
   - **Liability Center**: tăng huy động vốn ở các kỳ hạn được khuyến khích.
   - **Asset Center**: giảm cho vay ở các kỳ hạn có chi phí vốn cao, vì margin bị thu hẹp.
4. **Cải thiện chỉ số thanh khoản**: cấu trúc tài sản-nợ thay đổi theo hướng cải thiện LCR và NSFR [[src-ftp-transmission-analysis#^ftp-trans-18]].

### 2.2 Công Thức Điều Chỉnh Định Lượng Thanh Khoản
Nguồn mô hình hoá điều chỉnh Liquidity Spread theo khoảng cách tới target [[src-ftp-transmission-analysis#^ftp-trans-15]]:

$$\Delta\text{Spread}_{\text{short}} = \alpha \times (\text{LCR}_{\text{target}} - \text{LCR}_{\text{actual}})$$
$$\Delta\text{Spread}_{\text{long}} = \beta \times (\text{NSFR}_{\text{target}} - \text{NSFR}_{\text{actual}})$$
[[src-ftp-transmission-analysis#^ftp-trans-15]]

α và β là hệ số nhạy cảm do ALCO quyết định [[src-ftp-transmission-analysis#^ftp-trans-15]].

### 2.3 Ví Dụ Minh Họa Của Nguồn
Ngân hàng X có LCR 105% (target 115%) và NSFR 102% (target 108%). ALM tăng Liquidity Spread kỳ 1W-1M thêm 30-50 bps và kỳ 6M-2Y thêm 50-80 bps; sau 3-6 tháng, LCR tăng lên 118% và NSFR lên 108% [[src-ftp-transmission-analysis#^ftp-trans-16]].

---

## 3. Kênh Truyền Dẫn Thứ Hai: Rủi Ro Lãi Suất Sổ Ngân Hàng (IRRBB Channel)

### 3.1 Nguyên Tắc Tách Biệt và Chuyển Giao Rủi Ro Tập Trung (Matched-Maturity Risk Transfer)
Nguyên tắc cốt lõi của FTP hiện đại là **cô lập hoàn toàn rủi ro lãi suất khỏi các đơn vị kinh doanh và chuyển giao tập trung về Trung tâm Quản lý Vốn (ALM/Treasury)** [[src-ftp-transmission-analysis#^ftp-trans-9]]:

- Asset Center cho vay cố định 5 năm nhận vốn từ ALM theo FTP rate cố định 5 năm; Liability Center huy động tiền gửi 3 tháng bán vốn cho ALM theo FTP rate 3 tháng [[src-ftp-transmission-analysis#^ftp-trans-19]].
- Business Units chỉ thấy fixed margin (customer rate - FTP rate), nên không còn exposure với repricing risk. ALM kế thừa toàn bộ mismatch giữa asset repricing và liability repricing [[src-ftp-transmission-analysis#^ftp-trans-10]]. Xem [[repricing-gap-analysis]].

*Diễn giải (ví dụ số giả định do LLM dựng ở lần ingest trước, không lấy từ nguồn):* vay cố định 5 năm lãi suất 10% với FTP 5 năm 7,5% cho margin cố định 2,5%, không đổi dù lãi suất thị trường lên 12%; tiền gửi 3 tháng lãi suất 4% với FTP 3 tháng 5,5% cho margin 1,5%. Nguồn không đưa các con số này.

### 3.2 Cơ Chế Phạt/Thưởng Khe Hở Kỳ Hạn (Mismatch Penalty & Steering)
Khi ΔNII hoặc ΔEVE tiến gần hoặc vi phạm limit, ALM có thể điều chỉnh FTP curve để steering hành vi của BUs: tăng spread cho tenor có gap lớn, giảm spread hoặc thêm reward cho matched funding [[src-ftp-transmission-analysis#^ftp-trans-20]]. Nguồn gọi hệ số điều chỉnh là γ và δ, do ALCO calibrate [[src-ftp-transmission-analysis#^ftp-trans-29]].

*Diễn giải:* dạng $\text{Spread}_{\text{mismatch}} = \gamma \times |\text{Gap}| / \text{Limit}$ và $\text{Reward}_{\text{match}} = -\delta \times \text{Matched Ratio}$ xuất hiện trong phần 6.2 của nguồn ở dạng một dòng liền, nên node không dùng làm claim trích dẫn.

### 3.3 Quản Lý Rủi Ro Cơ Sở (Basis Risk Management)
Basis risk phát sinh khi assets và liabilities được repriced theo benchmark khác nhau, ví dụ VNIBOR 1M so với VNIBOR 3M, hoặc VNIBOR so với lãi suất điều hành SBV [[src-ftp-transmission-analysis#^ftp-trans-21]]:
- ALM thiết lập FTP curve riêng cho từng benchmark và áp dụng cross-currency/cross-index adjustment để theo dõi, kiểm soát basis risk exposure [[src-ftp-transmission-analysis#^ftp-trans-21]].
- Chi phí hedge basis risk có thể đưa vào FTP để pass through cho Business Units [[src-ftp-transmission-analysis#^ftp-trans-21]].

---

## 4. Kênh Truyền Dẫn Thứ Ba: Rủi Ro Tín Dụng, Vốn Kinh Tế và RAROC (Credit Risk & Capital Allocation Channel)

Quy định quản lý rủi ro tín dụng tại VN: xem [[credit-risk-management]].

### 4.1 Định Giá Theo Xếp Hạng Tín Nhiệm (Rating-based Pricing Grid)
FTP kết nối với hệ thống xếp hạng tín dụng của ngân hàng:
- **Tổn thất kỳ vọng (Expected Loss — EL, [[expected-loss]])**: tính vào giá bán vốn tín dụng [[src-ftp-transmission-analysis#^ftp-trans-11]]:
  $$\text{EL Charge} = \text{PD} \times \text{LGD} \times \text{EAD}$$
  [[src-ftp-transmission-analysis#^ftp-trans-11]]
- Rating cao (AAA-A) có credit spread thấp, rating thấp (BB trở xuống) có credit spread cao [[src-ftp-transmission-analysis#^ftp-trans-22]].

### 4.2 Chi Phí Phân Bổ Vốn Kinh Tế và Đòn Bẩy (Economic Capital Charge)
Ngoài EL, FTP còn gồm chi phí vốn cho Unexpected Loss [[src-ftp-transmission-analysis#^ftp-trans-12]]:

$$\text{Capital Charge} = \text{RWA} \times \text{Capital Ratio} \times \text{Cost of Equity (CoE)}$$
[[src-ftp-transmission-analysis#^ftp-trans-12]]

*Diễn giải:* với Economic Capital ([[economic-capital]]), cùng logic có thể viết $\text{Capital Charge} = \text{EC Density} \times \text{Hurdle Rate}$ trên mỗi đơn vị phơi nhiễm. Nguồn không đưa dạng này.

Khi CAR tiến gần regulatory minimum, ALM có thể tăng Capital Charge trong FTP để hạn chế tăng trưởng tài sản và khuyến khích deal có RWA density thấp hơn [[src-ftp-transmission-analysis#^ftp-trans-23]]. Nguồn T5 không nhắc tỷ lệ đòn bẩy ([[leverage-ratio|LEV]]) trong công thức này.

### 4.3 Tích Hợp RAROC Cấp Độ Từng Giao Dịch và Toàn Bảng Cân Đối
FTP là công cụ để vận hành khung RAROC (Risk-Adjusted Return on Capital): mỗi deal được định giá trên FTP để lợi suất đủ bù funding cost, EL và chi phí vốn [[src-ftp-transmission-analysis#^ftp-trans-24]].

$$\text{RAROC}_{\text{deal}} = \frac{\text{Revenue} - \text{Funding Cost} - \text{EL} - \text{Operating Cost}}{\text{Economic Capital}}$$
[[src-ftp-transmission-analysis#^ftp-trans-24]]

Deal có RAROC dưới hurdle rate không được chấp thuận hoặc phải reprice [[src-ftp-transmission-analysis#^ftp-trans-24]]. CoE trong công thức FTP là hurdle rate của cổ đông, thường 12%-15% [[src-ftp-transmission-analysis#^ftp-trans-25]]. Choudhry định nghĩa SVA là portfolio expected spread revenue trừ chi phí vốn [[src-choudhry-principles-banking#^choudhry-crd-6]].

*Diễn giải:* nếu RAROC bằng lợi nhuận chia Economic Capital thì $\text{SVA} = (\text{RAROC} - \text{Hurdle Rate}) \times \text{Economic Capital}$. Đây là biến đổi đại số của LLM, không phải công thức nguồn. FTP khớp kỳ hạn ([[maturity-transformation]]) giúp RAROC không bị bóp méo bởi chuyển đổi kỳ hạn.

### 4.4 Nghịch Lý Đánh Đổi Động Lực Học giữa NIM và RAROC (NIM - RAROC Trade-off Paradox)
*Diễn giải (ví dụ số giả định do LLM dựng ở lần ingest trước, không lấy từ nguồn nào trong wiki; chỉ minh hoạ logic NIM so với RAROC, không dùng làm số liệu):* tối ưu NIM đơn thuần có thể xung đột với tối ưu RAROC.

| Danh mục Tài sản | Lãi suất | Chi phí FTP COF | NIM Danh nghĩa | Mật độ RWA / EC | Tổn thất EL | Chi phí Hoạt động | RAROC | Giá trị Gia tăng SVA |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **A. Vay Tiêu dùng / BĐS rủi ro** | 10.5% | 4.5% | **6.0%** (Rất cao) | 150% ($EC \approx 15\%$) | 2.5% | 1.5% | **13.3%** | $+0.20\%$ (Biên mỏng) |
| **B. Cho vay Mua nhà Thế chấp chuẩn** | 7.5% | 4.5% | **3.0%** (Trung bình) | 35% ($EC \approx 3.5\%$) | 0.2% | 0.8% | **57.1%** | $\mathbf{+1.58\%}$ (Vượt trội) |
| **C. Trái phiếu Chính phủ L1** | 3.5% | 3.0% | **0.5%** (Rất mỏng) | 0% ($EC \approx 0\%$) | 0.0% | 0.1% | $\boldsymbol{\infty}$ | Thanh khoản & CAR tuyệt đối |

*Nghịch lý nhận diện (suy luận trên bảng giả định ở trên):*
- Nếu chi nhánh chỉ được giao KPI theo doanh số hoặc NIM, họ sẽ tập trung toàn lực vào **Danh mục A** vì mang lại NIM 6.0%. Nhưng danh mục này tiêu tốn tới 15% Vốn Kinh tế và chịu EL lớn, chỉ tạo ra RAROC 13.3% (sát ngưỡng Hurdle Rate 12%).
- Ngược lại, **Danh mục B** có NIM chỉ 3.0% nhưng do tiêu tốn rất ít vốn kinh tế (EC chỉ 3.5%), RAROC đạt tới 57.1%, tạo ra SVA cao gấp 8 lần Danh mục A!
- **Cơ chế FTP hóa giải nghịch lý (trong ví dụ giả định)**: Bằng cách tính trực tiếp $\text{Capital Charge} = \text{EC Density} \times \text{Hurdle Rate}$ vào biểu giá COF (Danh mục A bị cộng thêm $+1.8\%$, Danh mục B chỉ bị cộng $+0.42\%$), FTP triệt tiêu ảo tưởng lợi nhuận của Danh mục A, buộc chi nhánh phải hướng dòng tín dụng vào Danh mục B để tối ưu hóa RAROC và an toàn vốn CAR toàn hàng.

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

Ba kênh truyền dẫn rủi ro của FTP không vận hành biệt lập mà tạo thành một **vòng phản hồi khép kín (closed feedback loop)** [[src-ftp-transmission-analysis#^ftp-trans-13]]: Chu kỳ này diễn ra liên tục, thường hằng tháng hoặc hằng quý tuỳ biến động của thị trường và bảng cân đối [[src-ftp-transmission-analysis#^ftp-trans-28]].

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
- **Cân bằng Thanh khoản**: khi LCR/NSFR đạt target, ALM giảm liquidity spread về mức bình thường [[src-ftp-transmission-analysis#^ftp-trans-27]]. Business Units không còn bị khuyến khích quá mức huy động hoặc giảm cho vay ở các kỳ hạn cụ thể.
- **Cân bằng Lãi suất**: khi Gap nằm trong limit và ΔNII/ΔEVE ổn định, FTP curve không cần điều chỉnh [[src-ftp-transmission-analysis#^ftp-trans-27]].
- **Cân bằng Tín dụng & Vốn**: khi CAR có đủ buffer, credit spread phản ánh rủi ro của từng rating bucket [[src-ftp-transmission-analysis#^ftp-trans-27]].

### Tương tác chéo giữa các kênh
Một điều chỉnh FTP cho một loại rủi ro tác động sang loại khác [[src-ftp-transmission-analysis#^ftp-trans-26]]:
- Tăng liquidity spread dài hạn để cải thiện NSFR làm Asset Center giảm cho vay dài hạn, duration của asset portfolio ngắn lại và ΔEVE giảm.
- Tăng capital charge để cải thiện CAR đẩy Business Units sang tài sản RWA thấp (ví dụ HQLA), liquidity buffer tăng và LCR cải thiện.

### Khuyến nghị triển khai của nguồn
Nguồn nêu hai khuyến nghị [[src-ftp-transmission-analysis#^ftp-trans-29]]: thiết lập FTP governance framework với vai trò của ALCO trong việc approve FTP curve và steering adjustments; định kỳ review và back-test hiệu quả của FTP steering để calibrate các hệ số α, β, γ, δ, ε, ζ.

## Khái niệm và Liên kết
- [[liquidity-transfer-pricing]]: Tổng quan lý thuyết định giá điều chuyển thanh khoản nội bộ.
- [[ftp-pricing-methodology]]: Phương pháp định giá chi tiết VOF, COF, chi phí dự trữ bắt buộc, bảo hiểm tiền gửi và quyền chọn ẩn.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[bcbs-irrbb]]: Rủi ro lãi suất trên sổ ngân hàng.
- [[net-interest-income-sensitivity]]: Độ nhạy thu nhập lãi thuần.
- [[economic-value-of-equity]]: Độ nhạy giá trị kinh tế của vốn chủ sở hữu.
- [[ftp-transmission-channels-and-feedback-loop]]: Synthesis trả lời các câu hỏi về kênh thanh khoản, kênh lãi suất, vòng phản hồi, rủi ro vận hành và căn cứ quy định của cơ chế truyền dẫn.
