---
title: "Xác Định Mức Lãi Suất FTP Rate Cuối Cùng Cho Từng Giao Dịch Và Sản Phẩm: Tích Hợp Tenor, Repricing Profile, Liquidity Characteristics Và Embedded Options"
aliases: [FTP Final Rate Determination, Xác định mức FTP rate cuối cùng, Final FTP Rate Calculation, Granular FTP Pricing, Deal-Level FTP Rate, Tích hợp lãi suất FTP cuối cùng]
type: synthesis
domains: [alm, product]
status: active
maturity: canonical
origin: query
question: "Mức FTP rate cuối cùng được áp dụng cho từng giao dịch/sản phẩm như thế nào sau khi tính đến tenor, repricing profile, liquidity characteristics và embedded options?"
sources: ["[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-ftp-transmission-analysis]]"]
relations: []
tags: [ftp, final-ftp-rate, deal-level-pricing, tenor, repricing-profile, liquidity-characteristics, embedded-options, wal, tlp, synthesis]
updated: 2026-10-17
reviewed:
---

## 1. Tóm Tắt Quản Trị Cấp Cao (Executive Summary)

Trong kỹ trị ALM ngân hàng thương mại hiện đại, **Mức Lãi suất FTP Rate Cuối cùng (Final Deal-Level FTP Rate)** áp dụng cho từng giao dịch hoặc sản phẩm không phải là một con số đơn lẻ tra cứu trên bảng biểu cố định, mà là **kết quả đầu ra của một thuật toán tích hợp đa tầng (Multi-dimensional Integration Engine)** [[src-ftp-transmission-analysis#^ftp-trans-1]].

Thuật toán định giá FTP cấp độ giao dịch (Deal-level Pricing) xử lý đồng thời 4 yếu tố cấu thành rủi ro tài chính của hợp đồng [[src-ftp-transmission-analysis#^ftp-trans-3]]:
1. **Cấu trúc Kỳ hạn (Tenor Profile)**: Phân định giữa kỳ hạn danh nghĩa hợp đồng ($T_{\text{contractual}}$), kỳ hạn hiệu lực bình quân gia quyền ($\text{WAL}$) đối với các khoản vay trả định kỳ, và kỳ hạn hành vi đối với các sản phẩm phi kỳ hạn [[src-vab-ftp#^vab-ftp-20]].
2. **Đặc tính Tái định giá Lãi suất (Repricing Profile)**: Phân tách rủi ro tái định giá giữa sản phẩm lãi suất cố định (Fixed-rate) và sản phẩm lãi suất thả nổi (Floating-rate), xác định tần suất cập nhật Lãi suất Cơ sở (Base Rate) [[src-vab-ftp#^vab-ftp-33]].
3. **Đặc tính Thanh khoản (Liquidity Characteristics)**: Định lượng chính xác Phần bù thanh khoản kỳ hạn ($\text{TLP}$), chi phí gánh đệm tài sản thanh khoản cao ($\text{HQLA Buffer}$ âm carry), chi phí tuân thủ dự trữ bắt buộc ($\text{DTBB}$), bảo hiểm tiền gửi ($\text{BHTG}$), và chi phí duy trì hạn mức cam kết ngoại bảng chưa rút vốn [[src-vab-ftp#^vab-ftp-7]] [[src-vab-ftp#^vab-ftp-35]].
4. **Quyền chọn Ẩn và Rủi ro Hành vi (Embedded Options & Behavioral Risk)**: Mô hình hóa quyền chọn trả nợ trước hạn ($\text{Prepayment Option}$), quyền chọn rút tiền gửi sớm ($\text{Early Withdrawal}$), mô hình danh mục sao chép tiền gửi không kỳ hạn ($\text{CASA Replicating Portfolio}$), và định giá trần/sàn lãi suất ($\text{Caps/Floors}$) [[src-vab-ftp#^vab-ftp-14]] [[src-vab-ftp#^vab-ftp-18]].

```
+---------------------------------------------------------------------------------------------------+
|               KIẾN TRÚC TÍCH HỢP BỐN CHIỀU XÁC ĐỊNH MỨC FTP RATE CUỐI CÙNG CHO TỪNG DEAL           |
+---------------------------------------------------------------------------------------------------+
|                                THÔNG TIN HỢP ĐỒNG GIAO DỊCH GỐC (CORE BANKING)                    |
|                        (Số tiền, Đồng tiền, Ngày giải ngân, Ngày đáo hạn, Lịch trả gốc,           |
|                         Lãi suất khách hàng, Cơ chế lãi suất, Tần suất tái định giá)               |
|                                                  │                                                |
|            ┌─────────────────────────────────────┼─────────────────────────────────────┐          |
|            ▼                                     ▼                                     ▼          |
|  [ 1. XỬ LÝ KỲ HẠN ]                  [ 2. TÁI ĐỊNH GIÁ ]                   [ 3. THANH KHOẢN ]    |
|  - Trả cuối kỳ -> T_gốc               - Cố định -> 1 Tenor duy nhất         - TLP = COF_wal-COF_rep|
|  - Trả góp -> WAL = Σ(Pi×Ti)/ΣPi      - Thả nổi -> Bóc tách kép:            - Đệm HQLA TT22 carry  |
|  - Phi kỳ hạn -> Core/Non-core          + Repricing Base (1M, 3M)           - Chi phí DTBB & BHTG  |
|  - Nội suy lẻ Interp(T)                 + Liquidity Tenor (WAL)             - Phí cam kết ngoại bảng|
|            │                                     │                                     │          |
|            └─────────────────────────────────────┼─────────────────────────────────────┘          |
|                                                  ▼                                                |
|                                       [ 4. QUYỀN CHỌN ẨN ]                                        |
|                                       - Prepayment: Rút ngắn WAL theo CPR                         |
|                                       - Early Withdrawal: Hồi tố VOF KKH TT04                     |
|                                       - Caps / Floors: Option Add-on Black-76                     |
|                                                  │                                                |
|                                                  ▼                                                |
|            ┌───────────────────────────────────────────────────────────────────────────┐          |
|            ▼                                                                           ▼          |
|  [ MỨC VOF CUỐI CÙNG CHO HUY ĐỘNG ]                       [ MỨC COF CUỐI CÙNG CHO CHO VAY ]       |
|  VOF = Base(T/Replicating) + Margin + ALCO_adj            COF = Base(Repricing) + TLP(WAL)        |
|  (Cố định suốt kỳ hạn để bảo toàn biên)                         + Phụ phí pháp định (DTBB, BHTG,  |
|                                                                 Buffer) + Prepay_cost + ALCO_adj  |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Khung Tích Hợp 4 Chiều Kỹ Trị (The 4-Dimensional Integration Framework)

### 2.1. Chiều 1: Cấu Trúc Kỳ Hạn (Tenor Profile Integration)
- **Quy tắc Trả cuối kỳ (Bullet Maturity)**:
  - Kỳ hạn ánh xạ bằng đúng khoảng thời gian từ ngày giải ngân đến ngày đáo hạn: $T_{\text{gốc}} = \text{Maturity Date} - \text{Origination Date}$.
- **Quy tắc Trả gốc Định kỳ (Amortizing Installment)**:
  - Tuyệt đối không lấy kỳ hạn đáo hạn cuối cùng. Bắt buộc quy đổi thành **Kỳ hạn hiệu lực bình quân gia quyền (Weighted Average Life — WAL)** [[src-vab-ftp#^vab-ftp-20]]:
    $$\text{WAL} = \sum_{i=1}^{N} \frac{P_i \times T_i}{\sum_{i=1}^{N} P_i}$$
    *(Trong đó $P_i$ là số tiền gốc trả kỳ thứ $i$, $T_i$ là thời gian tính từ ngày giải ngân đến kỳ trả nợ thứ $i$)*.
- **Quy tắc Nội suy Tuyến tính Kỳ hạn Lẻ (Odd-Tenor Interpolation)**:
  - Nếu kỳ hạn hợp đồng hoặc $\text{WAL}$ không trùng khớp với các điểm mốc chuẩn trên đường cong FTP (O/N, 1M, 3M, 6M, 1Y, 2Y,...), hệ thống tự động nội suy tuyến tính [[src-vab-ftp#^vab-ftp-30]] [[src-vab-ftp#^vab-ftp-31]]:
    $$\text{Rate}(T) = \text{Rate}(T_1) + \frac{T - T_1}{T_2 - T_1} \times [\text{Rate}(T_2) - \text{Rate}(T_1)]$$

---

### 2.2. Chiều 2: Đặc Tính Tái Định Giá Lãi Suất (Repricing Profile Integration)
- **Khoản vay Lãi suất Cố định (Fixed-Rate Loans)**:
  - Toàn bộ rủi ro lãi suất trong suốt vòng đời được chuyển về CFU.
  - Áp dụng một mức lãi suất FTP duy nhất neo theo kỳ hạn gốc $T_{\text{gốc}}$ hoặc $\text{WAL}$ tại ngày giải ngân:
    $$\text{Base Rate} = \text{Base Curve}(T_{\text{gốc/WAL}})$$ [[src-vab-ftp#^vab-ftp-32]]
  - Mức Base Rate này **giữ nguyên không đổi (locked)** suốt thời hạn vay.
- **Khoản vay Lãi suất Thả nổi (Floating-Rate Loans)**:
  - Ngân hàng chỉ chịu rủi ro lãi suất trong khoảng thời gian giữa hai kỳ tái định giá, nhưng vẫn chịu cam kết thanh khoản suốt toàn bộ kỳ hạn hợp đồng.
  - Hệ thống áp dụng cơ chế **Bóc tách Kép (Dual-tenor Mapping)** [[src-vab-ftp#^vab-ftp-33]] [[src-vab-ftp#^vab-ftp-34]]:
    - Cấu phần Lãi suất Cơ sở ($\text{Base Rate}$): Lấy theo kỳ hạn tái định giá ($T_{\text{repricing}}$ ví dụ 1M, 3M, 6M) và **được cập nhật lại vào mỗi ngày điều chỉnh lãi suất**.
    - Cấu phần Phần bù Thanh khoản Kỳ hạn ($\text{TLP}$): Lấy theo kỳ hạn gốc hoặc $\text{WAL}$ và **giữ nguyên cố định suốt vòng đời khoản vay**.
- **Khoản vay Ưu đãi Hỗn hợp Hai Giai đoạn (Promotional Split Bucketing)**:
  - Giai đoạn ưu đãi (ví dụ cố định 1 năm đầu): Áp FTP cố định 1 năm, $\text{TLP} = 0$.
  - Giai đoạn sau ưu đãi (ví dụ thả nổi 3M trong 4 năm còn lại): Áp Base tái định giá 3M + $\text{TLP}$ tính trên kỳ hạn còn lại (4 năm).

---

### 2.3. Chiều 3: Đặc Tính Thanh Khoản (Liquidity Characteristics Integration)
Hệ thống cộng dồn 4 lớp phụ phí thanh khoản vào giá bán vốn tín dụng $\text{COF}$:
1. **Phần bù Thanh khoản Kỳ hạn (Term Liquidity Premium — TLP)**:
   - Đo lường chi phí duy trì thanh khoản dài hạn của ngân hàng trên thị trường vốn [[src-choudhry-principles-banking#^choudhry-ftp-15]]:
     $$\text{TLP} = \text{COF}(T_{\text{WAL}}) - \text{COF}(T_{\text{repricing}})$$ [[src-vab-ftp#^vab-ftp-34]]
2. **Chi phí Gánh Đệm Tài sản Thanh khoản Cao (Liquidity Buffer Premium)**:
   - Phản ánh khoản lỗ cơ hội (*negative carry*) do ngân hàng phải mua Trái phiếu Chính phủ, tiền gửi NHNN lợi suất thấp để đáp ứng Phụ lục 3 TT22 / LCR [[src-vab-ftp#^vab-ftp-10]]:
     $$\text{Tỷ lệ Buffer} = \frac{\text{Số dư bình quân TSTK} \times (\text{VOF bình quân} - \text{Lợi suất bình quân TSTK})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$
3. **Chi phí Tuân thủ Pháp lệnh (Statutory Compliance Reserves)**:
   - *Chi phí Dự trữ Bắt buộc (DTBB)*:
     $$\text{Phụ phí DTBB} = \frac{\text{Số dư DTBB} \times (\text{VOF bình quân} - \text{Lãi suất tiền gửi DTBB tại NHNN})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$ [[src-vab-ftp#^vab-ftp-9]]
   - *Chi phí Bảo hiểm Tiền gửi (BHTG)*: 0,15%/năm tính trên tiền gửi cá nhân VND quy đổi trên tổng tài sản có [[src-vab-ftp#^vab-ftp-8]].
4. **Phí Thanh khoản Tiềm tàng Cho Cam kết Ngoại bảng Chưa Rút (Contingent Liquidity Charge)**:
   - Đối với phần hạn mức chưa sử dụng $C$ của hạn mức tín dụng / thấu chi [[src-vab-ftp#^vab-ftp-35]]:
     $$\text{Phí thanh khoản ngoại bảng} = C \times \text{CCF} \times \text{Tỷ lệ dự trữ TSTK} \times (\text{VOF} - \text{Lợi suất TSTK})$$

---

### 2.4. Chiều 4: Quyền Chọn Ẩn Và Rủi Ro Hành Vi (Embedded Options Integration)
1. **Quyền chọn Trả nợ Trước hạn (Prepayment Option)**:
   - Dưới tác động của hành vi trả trước hạn (đo lường bằng tỷ lệ trả trước có điều kiện CPR), dòng tiền của khoản vay bị rút ngắn lại.
   - Kỳ hạn hiệu lực tính toán bị kéo giảm từ $\text{WAL}_{\text{hợp đồng}}$ xuống **$\text{WAL}_{\text{hành vi}}$** [[src-vab-ftp#^vab-ftp-19]]:
     $$\text{WAL}_{\text{hành vi}} = \sum_{i=1}^{N} \frac{P_i^{\text{adjust}} \times T_i}{\sum P_i^{\text{adjust}}} < \text{WAL}_{\text{hợp đồng}}$$
   - Khoản vay được gán giá COF theo $\text{WAL}_{\text{hành vi}}$, đồng thời cộng thêm phụ phí phòng ngừa quyền chọn ($\text{OptionCost}_{\text{prepay}}$).
2. **Quyền chọn Rút tiền gửi Trước hạn (Early Withdrawal Option)**:
   - Khách hàng cá nhân rút tiền gửi tiết kiệm trước hạn (theo Thông tư 04/2022/TT-NHNN).
   - Hệ thống thực hiện **cơ chế hồi tố (Clawback)**: Thu hồi lại toàn bộ phần chênh lệch VOF kỳ hạn dài đã tạm phân bổ cho chi nhánh, gán lại khoản tiền rút sớm vào **Bucket Tiền gửi Không kỳ hạn** [[src-vab-ftp#^vab-ftp-18]].
3. **Mô hình Hóa Tiền gửi Không kỳ hạn (CASA Replicating Portfolio)**:
   - Tách số dư CASA thành phần biến động ($\text{Non-core}$) và phần ổn định bền vững ($\text{Core}$) [[src-vab-ftp#^vab-ftp-14]]:
     $$\text{Base Rate}_{\text{CASA}} = \text{Base}(T_{\text{non-core}}) \times \%_{\text{non-core}} + \text{Base}(T_{\text{core}}) \times (1 - \%_{\text{non-core}})$$ [[src-vab-ftp#^vab-ftp-15]]
4. **Quyền chọn Trần/Sàn Lãi suất (Embedded Caps & Floors)**:
   - Các khoản vay có điều khoản trần lãi suất (Cap) hoặc sàn lãi suất (Floor) được bóc tách và định giá bằng mô hình Black-76 / Swaption Matrix để tính phụ phí cộng thêm vào giá COF.

---

## 3. Thuật Toán Tính Mức FTP Rate Cuối Cùng Cho Từng Sản Phẩm Cụ Thể

Dưới đây là công thức định lượng chi tiết mức FTP Rate cuối cùng được áp dụng trên hệ thống cho 8 nhóm sản phẩm điển hình:

```
+---------------------------------------------------------------------------------------------------+
|               BẢNG TỔNG HỢP CÔNG THỨC MỨC FTP RATE CUỐI CÙNG THEO TỪNG LOẠI SẢN PHẨM               |
+---------------------------------------------------------------------------------------------------+
|  MÃ SẢN PHẨM | TÊN SẢN PHẨM             | CÔNG THỨC TÍNH MỨC FTP RATE CUỐI CÙNG                   |
+--------------+--------------------------+---------------------------------------------------------+
|  TD-Fixed    | Tiền gửi tiết kiệm trả   | VOF_final = Base(T_gốc) + Margin + ALCO_adj             |
|              | lãi cuối kỳ              | (Khóa cố định suốt kỳ hạn tiền gửi)                     |
|              |                          |                                                         |
|  CASA-NMD    | Tiền gửi không kỳ hạn    | VOF_final = Base(O/N) × %NonCore + Base(1Y-3Y) × %Core  |
|              | thanh toán / tiết kiệm   |             + Margin + ALCO_adj                         |
|              |                          |                                                         |
|  LN-Fix-Bul  | Cho vay trả gốc cuối kỳ  | COF_final = Base(T_gốc) + Margin + DTBB + BHTG + Buffer |
|              | lãi suất cố định         |             + OptionCost_prepay + ALCO_adj              |
|              |                          |                                                         |
|  LN-Fix-Amor | Cho vay trả góp định kỳ  | COF_final = Base(WAL_behavior) + Margin + DTBB + BHTG   |
|              | lãi suất cố định         |             + Buffer + OptionCost_prepay + ALCO_adj     |
|              |                          |                                                         |
|  LN-Flt-Amor | Cho vay trả góp định kỳ  | COF_final(t) = Base_t(T_repricing)                      |
|              | lãi suất thả nổi         |   + [TLP(WAL) + Margin + DTBB + BHTG + Buffer           |
|              |                          |      + OptionCost_prepay + ALCO_adj] (phần cố định)     |
|              |                          |                                                         |
|  LN-Promo    | Cho vay ưu đãi 2 giai    | GĐ1 (Ưu đãi): COF = Base(T_promo) + Phụ phí cố định     |
|              | đoạn (1Y cố định + float)| GĐ2 (Sau ưu đãi): Base_t(Repricing) + TLP(T_còn lại)    |
|              |                          |                                                         |
|  OD-Credit   | Thấu chi tài khoản / Thẻ | Phần dư nợ sử dụng: Áp COF theo Core OD vs Non-core OD  |
|              | tín dụng nội bảng        |                                                         |
|              |                          |                                                         |
|  LC-Undrawn  | Hạn mức cam kết tín dụng | Phí thanh khoản = C × CCF × Tỷ lệ TSTK × (VOF - Lãi TSTK|
|              | ngoại bảng chưa rút vốn  |                                                         |
+---------------------------------------------------------------------------------------------------+
```

---

### 3.1. Sản Phẩm 1: Tiền Gửi Tiết Kiệm Trả Lãi Cuối Kỳ (Fixed-Rate Term Deposit)
- **Đặc điểm**: Lãi suất cố định, gốc trả một lần khi đáo hạn, không phát sinh TLP.
- **Công thức VOF cuối cùng**:
  $$\text{VOF}_{\text{final}} = \text{Base Curve}(T_{\text{contractual}}) + \text{Margin} + \text{ALCO Adjust}_{\text{deposit}}$$ [[src-vab-ftp#^vab-ftp-6]]
- **Cơ chế áp dụng**: Mức $\text{VOF}_{\text{final}}$ được gán cứng vào mã giao dịch và giữ nguyên không đổi suốt kỳ hạn gửi tiền. Chi nhánh hưởng biên thương mại: $\text{NIM} = \text{VOF}_{\text{final}} - \text{Lãi suất chi trả khách hàng}$.

---

### 3.2. Sản Phẩm 2: Tiền Gửi Không Kỳ Hạn CASA (Non-Maturity Deposits)
- **Đặc điểm**: Dòng tiền biến động liên tục theo hành vi khách hàng, không có ngày đáo hạn hợp đồng.
- **Công thức VOF cuối cùng**:
  $$\text{VOF}_{\text{final}} = [\text{Base}(T_{\text{non-core}}) \times \%_{\text{non-core}} + \text{Base}(T_{\text{core}}) \times (1 - \%_{\text{non-core}})] + \text{Margin} + \text{ALCO Adjust}$$ [[src-vab-ftp#^vab-ftp-15]]
- **Cơ chế áp dụng**:
  - Tỷ lệ $\%_{\text{non-core}}$ và $\%_{\text{core}}$ được mô hình hóa định kỳ (hàng quý).
  - Mức $\text{VOF}_{\text{final}}$ được tính hàng ngày trên số dư tiền gửi bình quân của khách hàng. Phần CASA lõi hưởng lãi suất dài hạn giúp chi nhánh đạt biên NIM rất lớn.

---

### 3.3. Sản Phẩm 3: Khoản Vay Lãi Suất Cố Định Trả Gốc Cuối Kỳ (Fixed Bullet Loan)
- **Đặc điểm**: Lãi suất cố định, toàn bộ gốc trả cuối kỳ, $\text{TLP} = 0$.
- **Công thức COF cuối cùng**:
  $$\text{COF}_{\text{final}} = \text{Base Curve}(T_{\text{gốc}}) + \text{Margin} + \text{DTBB} + \text{BHTG} + \text{Liquidity Buffer} + \text{OptionCost}_{\text{prepay}} + \text{ALCO Adjust}$$ [[src-vab-ftp#^vab-ftp-7]]
- **Cơ chế áp dụng**: Khóa cố định mức $\text{COF}_{\text{final}}$ từ ngày giải ngân cho đến ngày đáo hạn.

---

### 3.4. Sản Phẩm 4: Khoản Vay Lãi Suất Cố Định Trả Góp Định Kỳ (Fixed Amortizing Loan)
- **Đặc điểm**: Lãi suất cố định, nợ gốc trả đều hàng tháng/quý, số dư nợ giảm dần.
- **Bước 1**: Tính kỳ hạn hiệu lực $\text{WAL}$ từ dòng tiền trả nợ gốc: $\text{WAL} = \sum (P_i \times T_i) / \sum P_i$.
- **Bước 2**: Hiệu chỉnh rủi ro trả nợ trước hạn theo mô hình CPR: $\text{WAL}_{\text{behavioral}} = \text{WAL} \times (1 - \text{CPR\_factor})$.
- **Công thức COF cuối cùng**:
  $$\text{COF}_{\text{final}} = \text{Base Curve}(\text{WAL}_{\text{behavioral}}) + \text{Margin} + \text{Phụ phí tuân thủ (DTBB + BHTG + Buffer)} + \text{ALCO Adjust}$$ [[src-vab-ftp#^vab-ftp-20]]
- **Cơ chế áp dụng**: Khóa cố định mức COF này trong suốt vòng đời khoản vay. Khách hàng và chi nhánh được hưởng chi phí vốn rẻ hơn đáng kể so với việc tính theo kỳ hạn pháp lý cuối cùng.

---

### 3.5. Sản Phẩm 5: Khoản Vay Lãi Suất Thả Nổi Trả Góp Định Kỳ (Floating Amortizing Loan)
- **Đặc điểm**: Lãi suất thả nổi điều chỉnh định kỳ (ví dụ 3 tháng/lần), nợ gốc trả góp hàng tháng.
- **Cấu trúc COF tại thời điểm $t$**:
  $$\text{COF}_{\text{final}}(t) = \text{Base Curve}_t(T_{\text{repricing}}) + \text{Spread Cố Định}$$
  Trong đó, **Spread Cố Định** được khóa cứng từ ngày giải ngân:
  $$\text{Spread Cố Định} = \text{TLP}(\text{WAL}, T_{\text{repricing}}) + \text{Margin} + \text{DTBB} + \text{BHTG} + \text{Buffer} + \text{OptionCost}_{\text{prepay}} + \text{ALCO Adjust}$$
  Với:
  $$\text{TLP}(\text{WAL}, T_{\text{repricing}}) = \text{COF}(\text{WAL}) - \text{COF}(T_{\text{repricing}})$$ [[src-vab-ftp#^vab-ftp-34]]
- **Cơ chế áp dụng**:
  - Cứ mỗi chu kỳ điều chỉnh lãi suất (sau 3 tháng), hệ thống chỉ cập nhật lại giá trị $\text{Base Curve}_t(3\text{M})$ theo điều kiện thị trường mới.
  - Toàn bộ phần $\text{Spread Cố Định}$ (chứa đựng TLP và các phụ phí pháp định) được **giữ nguyên không đổi**. Chi nhánh được bảo toàn biên thương mại:
    $$\text{NIM} = \text{Lãi suất cho vay khách hàng}(t) - \text{COF}_{\text{final}}(t) = \text{const}$$

---

### 3.6. Sản Phẩm 6: Khoản Vay Ưu Đãi Hỗn Hợp Hai Giai Đoạn (Promotional Loans)
- **Cấu trúc sản phẩm**: Vay 5 năm, cố định ưu đãi 1 năm đầu, 4 năm sau thả nổi 3 tháng/lần.
- **Áp giá theo phương án Split Bucketing**:
  - **Năm thứ 1 (Thời kỳ ưu đãi)**:
    $$\text{COF}_{\text{GĐ1}} = \text{Base Curve}(1\text{Y}) + \text{Margin} + \text{Phụ phí tuân thủ} + \text{ALCO Adjust}_{\text{promo}}$$
    *(Không tính TLP vì là giai đoạn cố định 1 năm)*.
  - **Năm thứ 2 đến thứ 5 (Thời kỳ thả nổi)**:
    $$\text{COF}_{\text{GĐ2}}(t) = \text{Base Curve}_t(3\text{M}) + \text{TLP}(4\text{Y}, 3\text{M}) + \text{Margin} + \text{Phụ phí tuân thủ} + \text{ALCO Adjust}$$
    *(Tính TLP dựa trên kỳ hạn còn lại là 4 năm)*.

---

### 3.7. Sản Phẩm 7: Cam Kết Ngoại Bảng Chưa Rút Vốn (Undrawn Commitments)
- **Đặc điểm**: Khách hàng được duyệt hạn mức nhưng chưa rút vốn nội bảng.
- **Công thức tính phí thanh khoản tiềm tàng**:
  $$\text{Phí ngoại bảng} = C \times \text{CCF} \times \text{Tỷ lệ dự trữ TSTK} \times (\text{VOF bình quân} - \text{Lợi suất bình quân TSTK})$$ [[src-vab-ftp#^vab-ftp-35]]
- **Cơ chế áp dụng**: Hệ thống tính phí định kỳ hàng tháng trên số dư hạn mức chưa sử dụng $C$. Chi nhánh thu phí cam kết (*commitment fee*) từ khách hàng để bù đắp chi phí này.

---

### 3.8. Mở Rộng: Định Giá Toàn Diện Tích Hợp RAROC (Comprehensive RAROC Pricing)
Đối với các ngân hàng áp dụng chuẩn mực quản trị vốn tiên tiến theo Basel II/III [[src-ftp-transmission-analysis#^ftp-trans-11]] [[src-ftp-transmission-analysis#^ftp-trans-12]]:
$$\text{FTP Rate}_{\text{Comprehensive}} = \text{COF}_{\text{final}} + \text{EL Charge} + \text{Capital Charge}$$
Trong đó:
- $\text{EL Charge} = \text{PD} \times \text{LGD} \times \text{EAD}$ (Bù đắp tổn thất tín dụng kỳ vọng).
- $\text{Capital Charge} = \text{RWA} \times \text{CAR}_{\text{mục tiêu}} \times \text{Cost of Equity}$ (Chi phí bù đắp vốn kinh tế cho tổn thất ngoài kỳ vọng).

---

## 4. Minh Họa Tính Toán Kỹ Thuật Số Liệu Cụ Thể (Numerical Case Studies)

### Tình huống A: Khoản Vay Mua Nhà Trả Góp 10 Năm (120 Tháng)
Giả định thông số hợp đồng giải ngân ngày 16/10/2026:
- Số tiền vay: **2.000.000.000 VND** (2 tỷ VND).
- Kỳ hạn hợp đồng: **10 năm (120 tháng)**. Trả gốc đều mỗi tháng $\approx 16.67$ triệu VND/tháng.
- Cơ chế lãi suất: Thả nổi định kỳ **3 tháng/lần**. Lãi suất cho vay khách hàng kỳ đầu: **9.50%/năm**.
- Dữ liệu đường cong FTP tại ngày giải ngân:
  - $\text{Base Curve}(3\text{M}) = 4.20\%$.
  - $\text{Base Curve}(5\text{Y}) = 6.80\%$.
- Phụ phí tuân thủ ngân hàng:
  - $\text{Margin huy động} = 0.50\%$.
  - $\text{Chi phí DTBB} = 0.12\%$.
  - $\text{Chi phí BHTG} = 0.08\%$.
  - $\text{Liquidity Buffer Premium} = 0.25\%$.
  - $\text{OptionCost}_{\text{prepay}} = 0.15\%$.
  - $\text{ALCO Adjust} = 0.00\%$.

**Các bước tính toán của Engine:**
1. **Tính kỳ hạn hiệu lực $\text{WAL}$**:
   - Khoản vay 10 năm trả gốc đều hàng tháng có:
     $$\text{WAL} = \sum_{i=1}^{120} \frac{P_i \times T_i}{\sum P_i} \approx 5.04 \text{ năm} \approx 5\text{Y}$$
2. **Tính Phần bù Thanh khoản Kỳ hạn ($\text{TLP}$)**:
   - Kỳ hạn thanh khoản gốc hiệu lực là 5Y, kỳ hạn tái định giá là 3M:
     $$\text{TLP}(5\text{Y}, 3\text{M}) = \text{COF}(5\text{Y}) - \text{COF}(3\text{M}) = 6.80\% - 4.20\% = 2.60\%$$
3. **Tính phần Spread Cố Định của khoản vay**:
   $$\text{Spread Cố Định} = \text{TLP}(2.60\%) + \text{Margin}(0.50\%) + \text{DTBB}(0.12\%) + \text{BHTG}(0.08\%) + \text{Buffer}(0.25\%) + \text{Prepay}(0.15\%) = 3.70\%$$
4. **Mức COF cuối cùng áp dụng cho kỳ 3 tháng đầu tiên**:
   $$\text{COF}_{\text{final}}(\text{Kỳ 1}) = \text{Base Curve}(3\text{M}) + \text{Spread Cố Định} = 4.20\% + 3.70\% = \mathbf{7.90\%/\text{năm}}$$
5. **Đo lường hiệu quả tại Chi nhánh**:
   - Lãi suất thu từ khách hàng: $9.50\%$.
   - Chi phí vốn COF phải trả cho CFU: $7.90\%$.
   - **Biên lợi nhuận thương mại cố định của Chi nhánh**:
     $$\text{NIM}_{\text{Chi nhánh}} = 9.50\% - 7.90\% = \mathbf{1.60\%/\text{năm}}$$
   - *Khi thị trường biến động sau 3 tháng*: Giả sử lãi suất thị trường tăng khiến $\text{Base Curve}(3\text{M})$ tăng lên $4.80\%$. Lãi suất khách hàng điều chỉnh lên $10.10\%$. Khi đó $\text{COF}$ mới $= 4.80\% + 3.70\% = 8.50\%$. Biên thương mại của chi nhánh vẫn bảo toàn nguyên vẹn: $10.10\% - 8.50\% = \mathbf{1.60\%}$. Toàn bộ rủi ro biến động lãi suất đã được CFU hấp thụ hoàn toàn.

---

### Tình huống B: Tiền Gửi Không Kỳ Hạn (CASA) Quy Mô 1.000 Tỷ VND
Giả định số dư tiền gửi thanh toán KHDN bình quân tháng:
- Số dư: **1.000 tỷ VND**.
- Lãi suất chi trả thực tế cho khách hàng: **0.20%/năm**.
- Kết quả mô hình hành vi Replicating Portfolio:
  - Tỷ lệ Non-core CASA (biến động): **30%** (gán vào Bucket O/N).
  - Tỷ lệ Core CASA (bám dính ổn định): **70%** (gán vào Bucket 2 năm).
- Dữ liệu đường cong FTP:
  - $\text{Base Curve}(\text{O/N}) = 1.00\%$.
  - $\text{Base Curve}(2\text{Y}) = 5.50\%$.
  - $\text{Margin huy động} = 0.40\%$.
  - $\text{ALCO Adjust} = 0.20\%$ (ALCO thưởng khuyến khích tăng CASA).

**Các bước tính toán của Engine:**
1. **Tính Lãi suất VOF cơ sở từ mô hình Replicating**:
   $$\text{Base}_{\text{CASA}} = 1.00\% \times 30\% + 5.50\% \times 70\% = 0.30\% + 3.85\% = 4.15\%$$
2. **Mức VOF cuối cùng phân bổ cho Chi nhánh**:
   $$\text{VOF}_{\text{final}} = \text{Base}_{\text{CASA}}(4.15\%) + \text{Margin}(0.40\%) + \text{ALCO Adjust}(0.20\%) = \mathbf{4.75\%/\text{năm}}$$
3. **Hiệu quả kinh doanh của Chi nhánh**:
   - Thu nhập FTP nhận từ CFU: $1.000\text{ tỷ} \times 4.75\% = 47.5\text{ tỷ VND/năm}$.
   - Chi phí trả lãi khách hàng: $1.000\text{ tỷ} \times 0.20\% = 2.0\text{ tỷ VND/năm}$.
   - **Lợi nhuận NII thuần Chi nhánh được ghi nhận**:
     $$\text{NII}_{\text{Chi nhánh}} = 47.5\text{ tỷ} - 2.0\text{ tỷ} = \mathbf{45.5\text{ tỷ VND/năm}} \quad (\text{NIM} = 4.55\%)$$

---

## 5. Ý Nghĩa Kỹ Trị Đối Với Vận Hành Hệ Thống ALM

Việc xác định chính xác mức FTP Rate cuối cùng đến từng deal mang lại 3 giá trị sống còn:
1. **Định giá chính xác rủi ro (No Mispricing)**: Chấm dứt triệt để tình trạng định giá sai lệch khiến ngân hàng vô tình khuyến khích các sản phẩm rủi ro thanh khoản cao mà biên lợi nhuận thấp.
2. **Tự động hóa hoàn toàn trên Core Banking**: Loại bỏ toàn bộ sự can thiệp thủ công hay thương lượng chủ quan giữa chi nhánh và hội sở, đảm bảo tính nhất quán và kỷ luật tài chính trên toàn hệ thống.
3. **Bảo toàn biên lợi nhuận thương mại (Insulating Commercial Margin)**: Cho phép cán bộ kinh doanh chi nhánh an tâm tập trung vào phục vụ khách hàng và quản lý rủi ro tín dụng với biên lợi nhuận được khóa chặt, trong khi toàn bộ rủi ro chuyển đổi kỳ hạn và thanh khoản được kiểm soát chuyên nghiệp tại Treasury.

## Khái niệm và Liên kết
- [[ftp-cost-benefit-allocation-principles]]: Nguyên tắc phân bổ chi phí và lợi ích của từng FTP portfolio cho các đơn vị kinh doanh và sản phẩm.
- [[ftp-economic-cost-and-incentive-validation]]: Kiểm tra tính phản ánh economic cost và cơ chế định hướng incentive của hệ thống FTP.
- [[ftp-portfolio-and-bucket-allocation]]: Phương pháp phân bổ giao dịch và sản phẩm vào các danh mục và thang kỳ hạn FTP.
- [[ftp-curve-construction-methodology]]: Phương pháp luận xây dựng đường cong FTP theo kỳ hạn, đồng tiền và loại sản phẩm.
- [[ftp-risk-and-cost-components]]: Các cấu phần rủi ro và chi phí trong định giá FTP.
- [[ftp-pricing-methodology]]: Chi tiết công thức tính toán VOF, COF và phụ phí tuân thủ ngân hàng.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn điều tiết rủi ro thanh khoản, lãi suất và tín dụng của FTP.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU qua FTP.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa quy hoạch bảng cân đối ALM toàn diện.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản theo Moorad Choudhry.
- [[synthetic-balance-sheet-liquidity-risk]]: Bảng cân đối thanh khoản tổng hợp và động lực dòng tiền.
- [[non-maturity-deposits]]: Mô hình hóa hành vi tiền gửi không kỳ hạn CASA.
- [[behavioural-options]]: Quyền chọn trả nợ trước hạn và rút tiền gửi sớm.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.
