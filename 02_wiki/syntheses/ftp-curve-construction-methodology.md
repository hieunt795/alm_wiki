---
title: "Phương Pháp Luận Xây Dựng Đường Cong FTP (FTP Curve) Theo Kỳ Hạn, Đồng Tiền Và Loại Sản Phẩm"
aliases: [FTP Curve Construction Methodology, Xây dựng đường cong FTP, Phương pháp lập đường cong FTP, FTP Curve Tenor Currency Product, FTP Rate Construction]
type: synthesis
domains: [alm, product]
status: active
maturity: draft
origin: query
question: "FTP curve/FTP rate được xây dựng như thế nào cho từng kỳ hạn, đồng tiền và loại sản phẩm?"
sources: ["[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-ftp-transmission-analysis]]", "[[src-tt83-2025-nhnn]]", "[[src-tt50-2026-nhnn]]"]
relations: []
tags: [ftp, ftp-curve, tenor-structure, multi-currency, product-pricing, interpolation, wal, cash-flow-mapping, synthesis]
updated: 2026-10-20
reviewed:
---

## 1. Tóm Tắt Quản Trị Cấp Cao (Executive Summary)

Việc xây dựng hệ thống **Đường cong Định giá Điều chuyển Vốn Nội bộ (FTP Curve / FTP Rate)** là khâu thiết kế kỹ thuật quan trọng nhất trong quản trị cân đối tài sản - nợ (ALM) của ngân hàng thương mại. Một đường cong FTP chuẩn mực không thể là một con số đơn lẻ hay một mức lãi suất cào bằng, mà phải được cấu trúc hóa trong **không gian 3 chiều đồng bộ**:

```
                              [ KHÔNG GIAN 3 CHIỀU XÂY DỰNG HỆ THỐNG FTP ]
                                                   
                                         CHIỀU ĐỒNG TIỀN (Currency)
                                                    ▲
                                                   / 
                                                  /  VND, USD, EUR, JPY...
                                                 /   (Độc lập, FX Swap, CIP, DTBB)
                                                /
                                               +------------------------► CHIỀU LOẠI SẢN PHẨM (Product)
                                              /|                          - VOF (Huy động) vs COF (Cho vay)
                                             / |                          - Trả cuối kỳ vs Trả định kỳ (WAL)
                                            /  |                          - Cố định vs Thả nổi (TLP)
                                           /   |                          - Phi kỳ hạn (CASA Non-term)
                                          /    |                          - Cam kết ngoại bảng & Quyền chọn ẩn
                                         /     |
                                        /      ▼
                                       CHIỀU KỲ HẠN (Tenor)
                                       - Thang kỳ hạn chuẩn: O/N -> 10Y
                                       - Nội suy tuyến tính / Cubic Spline
                                       - Market 1 (Biểu định kỳ) vs Market 2 (Real-time Peer)
```

1. **Chiều Cấu trúc Kỳ hạn (Tenor Dimension)**:
   - Phân đoạn thành các thang kỳ hạn chuẩn từ qua đêm (O/N) đến 10 năm.
   - Ứng dụng phương pháp nội suy tuyến tính (Linear Interpolation) hoặc hàm Cubic Spline đối với các kỳ hạn lẻ nằm ngoài thang chuẩn [[src-vab-ftp#^vab-ftp-30]] [[src-vab-ftp#^vab-ftp-31]].
2. **Chiều Đồng tiền (Currency Dimension)**:
   - Các đường cong FTP được xây dựng **độc lập và tách biệt cho từng loại tiền tệ** (VND, USD, EUR,...) [[src-vab-ftp#^vab-ftp-26]] [[src-vab-ftp#^vab-ftp-27]].
   - Theo VAB, lãi suất FTP cơ sở VND dựa trên lãi suất huy động bình quân toàn hàng của các khoản phát sinh trong 3 tháng liền kề [[src-vab-ftp#^vab-ftp-28]]; lãi suất FTP cơ sở USD dùng lãi suất tham chiếu của thị trường [[src-vab-ftp#^vab-ftp-29]]. Phương án VNIBOR kết hợp TPCP cho VND: [cần nguồn].
   - Tích hợp chi phí hoán đổi ngoại tệ (FX Swap Curve) và ngang giá lãi suất có bảo hiểm (CIP).
3. **Chiều Loại Sản phẩm (Product Dimension)**:
   - Phân định rõ ràng giữa **Giá mua vốn áp dụng cho tài sản nợ (VOF)** và **Giá bán vốn áp dụng cho tài sản có (COF)** [[src-vab-ftp#^vab-ftp-6]] [[src-vab-ftp#^vab-ftp-7]].
   - Khoản vay trả gốc cuối kỳ vs trả định kỳ theo kỳ hạn hiệu lực bình quân gia quyền (WAL) [[src-vab-ftp#^vab-ftp-20]].
   - Khoản vay lãi suất cố định vs thả nổi (bổ sung Term Liquidity Premium — TLP) [[src-vab-ftp#^vab-ftp-33]] [[src-vab-ftp#^vab-ftp-34]].
   - Tiền gửi không kỳ hạn (CASA) định giá qua Đường cong hoàn trả phi kỳ hạn (Non-term Redemption Curve) tách Core vs Non-core CASA [[src-vab-ftp#^vab-ftp-14]].
   - Cam kết hạn mức ngoại bảng định giá qua phụ phí thanh khoản tiềm tàng [[src-vab-ftp#^vab-ftp-35]].

---

## 2. Chiều Không Gian 1: Xây Dựng Đường Cong FTP Theo Cấu Trúc Kỳ Hạn (Tenor Structure)

### 2.1. Thang Kỳ Hạn Chuẩn Hóa (Standard Tenor Buckets)
Trong thực tiễn các ngân hàng thương mại Việt Nam (theo chuẩn tư vấn của EY) và thông lệ quốc tế, biểu lãi suất FTP được chuẩn hóa thành các điểm kỳ hạn (*tenor pillars*):

```
+---------------------------------------------------------------------------------------------------+
|                        PHÂN ĐOẠN ĐƯỜNG CONG FTP THEO THANG KỲ HẠN CHUẨN                           |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [ ĐOẠN NGẮN HẠN: THỊ TRƯỜNG TIỀN TỆ ]      [ ĐOẠN TRUNG HẠN ]         [ ĐOẠN DÀI HẠN: VỐN ]      |
|  Tenors: O/N, 1W, 2W, 3W, 1M, 2M, 3M        Tenors: 6M, 9M, 12M, 18M   Tenors: 24M, 36M, 60M, 120M|
|  - Căn cứ: VNIBOR, OMO, Tín phiếu SBV       - Căn cứ: Tiền gửi liên    - Căn cứ: Lợi suất TPCP    |
|  - Đặc trưng: Thanh khoản dồi dào,            tục, TPCP kỳ hạn ngắn      (VGB Benchmark Yield)    |
|    biến động sát lãi suất điều hành         - Đặc trưng: Bắt đầu chịu  - Đặc trưng: Phần bù thanh |
|                                               phần bù thanh khoản TLP    khoản TLP cao, chi phối  |
|                                                                          bởi chỉ số Basel NSFR    |
+---------------------------------------------------------------------------------------------------+
```

### 2.2. Phương Pháp Nội Suy / Ngoại Suy Cho Các Kỳ Hạn Lẻ (Interpolation & Bootstrapping)
Hầu hết các hợp đồng thực tế ngoài thị trường không có kỳ hạn tròn trĩnh theo thang chuẩn (ví dụ: khoản vay 4 tháng 12 ngày, hoặc tiền gửi 73 ngày):
- **Nguyên tắc kỹ trị**: Mọi kỳ hạn không nằm trên thang chuẩn đều phải được tính **nội suy trực tiếp (Linear Interpolation)** từ hai điểm kỳ hạn liền kề trên biểu ban hành [[src-vab-ftp#^vab-ftp-30]] [[src-vab-ftp#^vab-ftp-31]]:
  $$\text{FTP Rate}(T) = \text{FTP Rate}(T_1) + \frac{T - T_1}{T_2 - T_1} \times \left[ \text{FTP Rate}(T_2) - \text{FTP Rate}(T_1) \right]$$
  Trong đó:
  - $T$: Số ngày thực tế của giao dịch (tính theo năm tài chính 365 ngày).
  - $T_1, T_2$: Điểm kỳ hạn chuẩn liền trước và liền sau kỳ hạn $T$.
- **Kỹ thuật hàm nội suy trong hệ thống**: Hệ thống ALM/FTP tự động áp dụng hàm `Interp(WAT, Cột kỳ hạn, Cột lãi suất)` để xác định mức giá tức thì cho từng dòng tiền [[src-vab-ftp#^vab-ftp-20]].
- **Kỹ thuật nâng cao (Bootstrapping / Cubic Spline)**: Đối với các kỳ hạn trung dài hạn thiếu giao dịch thanh khoản, CFU sử dụng mô hình tham số Nelson-Siegel-Svensson để nội suy đường cong lãi suất giao ngay (Zero-coupon spot curve) mượt mà, không bị gấp khúc tại các điểm chuyển tiếp.

### 2.3. Chu Kỳ Rà Soát và Ban Hành
- **Biểu giá Thị trường 1 (Retail & Corporate)**: Được rà soát và phê duyệt định kỳ hàng tháng hoặc hàng quý bởi Ủy ban [[alco|ALCO]] [cần nguồn]. Theo TT83/2025, Hội đồng ALCO đề xuất, tham mưu Tổng giám đốc về quản lý tài sản/nợ và họp định kỳ tối thiểu mỗi quý 01 lần [[src-tt83-2025-nhnn#^d6-4b]]; bộ phận ALM rà soát, đề xuất nguyên tắc xây dựng giá điều chuyển vốn nội bộ [[src-tt83-2025-nhnn#^d25-3]]. Giữ ổn định tương đối để chi nhánh chủ động đàm phán hợp đồng.
- **Biểu giá Thị trường 2 (Treasury Interbank)**: Được CFU cập nhật hàng ngày hoặc theo thời gian thực (real-time) để phản ánh tức thời chi phí vốn trên thị trường liên ngân hàng.

---

## 3. Chiều Không Gian 2: Xây Dựng Đường Cong FTP Theo Đồng Tiền (Currency Dimension)

Hệ thống FTP vận hành theo nguyên tắc: **Cấu phần giá FTP của từng loại tiền tệ phải được tính toán độc lập hoàn toàn với nhau** [[src-vab-ftp#^vab-ftp-26]] [[src-vab-ftp#^vab-ftp-27]]. Ngân hàng không được lấy đường cong VND để áp cho USD hoặc ngược lại.

```
+---------------------------------------------------------------------------------------------------+
|                  SO SÁNH PHƯƠNG PHÁP XÂY DỰNG ĐƯỜNG CONG FTP: VND VS NGOẠI TỆ (USD)               |
+---------------------------------------------------------------------------------------------------+
|  TIÊU CHÍ              | ĐỒNG VIỆT NAM (VND)                    | ĐÔ LA MỸ (USD) / NGOẠI TỆ       |
+------------------------+----------------------------------------+---------------------------------+
|  1. Lãi suất cơ sở     | - Ngắn hạn: VNIBOR / OMO / Tín phiếu   | - Ngắn hạn (≤ 1Y): SOFR, Term   |
|     (Base Curve)       | - Trung dài hạn: Lợi suất TPCP (VGB)   |   SOFR, SIBOR bình quân 3 tháng |
|                        |   hoặc bình quân huy động 3 tháng gần  | - Trung dài hạn (> 1Y): Lãi suất|
|                        |   nhất toàn ngân hàng                  |   hoán đổi IRS ngoại tệ         |
|                        |                                        |                                 |
|  2. Dự trữ bắt buộc    | Tính theo tỷ lệ DTBB VND của NHNN      | Tính theo tỷ lệ DTBB ngoại tệ   |
|     (Statutory Reserve)| (ví dụ: 3% cho kỳ hạn dưới 12M;        | (thường cao hơn rất nhiều: 8%   |
|                        |  lãi suất gửi DTBB 0.5%/năm)           |  cho KKH & <12M; lãi suất 0%)   |
|                        |                                        |                                 |
|  3. Bảo hiểm tiền gửi  | Phân bổ tỷ lệ 0.15%/năm tính trên      | KHÔNG ÁP DỤNG                   |
|     (Deposit Insurance)| số dư tiền gửi cá nhân VND             | (Luật BHTG chỉ bảo hiểm cho VND)|
|                        |                                        |                                 |
|  4. Cơ chế trần LS     | Trần lãi suất huy động ngắn hạn (<6M)  | Trần lãi suất huy động 0%/năm   |
|     (Regulatory Caps)  | theo Thông tư NHNN từng thời kỳ        | theo Thông tư 24/2015/TT-NHNN   |
|                        |                                        |                                 |
|  5. Liên kết tỷ giá    | Đồng tiền yết giá gốc                  | Định giá qua điểm hoán đổi      |
|     (FX Swap Linkage)  |                                        | FX Swap Forward Points (CIP)    |
+---------------------------------------------------------------------------------------------------+
```

### 3.1. Phương Pháp Lập Đường Cong VND
Tài liệu VAB nêu lãi suất FTP cơ sở VND dựa trên lãi suất huy động bình quân toàn hàng 3 tháng liền kề [[src-vab-ftp#^vab-ftp-28]], tức phương án 1 dưới đây. Danh mục đầu vào của VAB chỉ gồm lãi suất huy động thực tế cho VND và LIBOR/SOFR cộng đường cong hoán đổi USD cho USD [[src-vab-ftp#^vab-ftp-41]], không có VNIBOR hay TPCP. *Diễn giải:* phương án 2 là phương án thay thế ngoài VAB [cần nguồn].
- **Phương án 1 (Nội sinh — Chi phí huy động bình quân)**: Lấy số dư huy động và lãi suất thực tế phát sinh trong 3 tháng liền kề của toàn ngân hàng cho từng kỳ hạn chuẩn để tính lãi suất bình quân gia quyền:
  $$\text{Base Curve}_{\text{VND}}(i) = \frac{\sum_{j} \text{Số dư}_j \times \text{Lãi suất}_j}{\sum_{j} \text{Số dư}_j}$$
- **Phương án 2 (Thị trường vốn — Capital Market Rates)**: Sử dụng VNIBOR cho kỳ hạn dưới 3 tháng và đường cong Trái phiếu Chính phủ Việt Nam (VGB Yield Curve từ Bloomberg BVAL) cho kỳ hạn từ 6 tháng đến 10 năm. Đây là phương án chuẩn mực giúp triệt tiêu hoàn toàn sự méo mó chi phí lịch sử theo nguyên tắc Cận biên [[src-choudhry-principles-banking#^choudhry-ftp-12]].

### 3.2. Phương Pháp Lập Đường Cong USD & Ngoại Tệ
Tại thị trường Việt Nam, tiền gửi USD của dân cư và tổ chức kinh tế bị khống chế trần lãi suất huy động 0%/năm theo quy định của NHNN:
- **Lãi suất cơ sở USD** được xây dựng hoàn toàn dựa trên lãi suất tham chiếu thị trường quốc tế [[src-vab-ftp#^vab-ftp-29]]:
  - **Kỳ hạn ngắn hạn ($\le 1$ năm)**: Lấy lãi suất tham chiếu **SOFR (Secured Overnight Financing Rate)**, Term SOFR (hoặc SIBOR/LIBOR trước đây) bình quân không trọng số trong 3 tháng gần nhất cho từng thang kỳ hạn [[src-vab-ftp#^vab-ftp-29]].
  - **Kỳ hạn trung và dài hạn (> 1 năm)**: Lấy lãi suất của các hợp đồng hoán đổi lãi suất USD (Interest Rate Swap — IRS) bình quân không trọng số 3 tháng gần nhất trên Thomson Reuters / Bloomberg [[src-vab-ftp#^vab-ftp-29]].
- **Các ngoại tệ khác (EUR, JPY, GBP, AUD)**: Áp dụng phương pháp tương tự như USD, dựa trên lãi suất RFR chuẩn tương ứng (EURIBOR/€STR cho EUR, TONAR cho JPY, SONIA cho GBP).

### 3.3. Cơ Chế FX Swap Curve và Ngang Giá Lãi Suất (CIP)
Khi ngân hàng thừa thanh khoản USD nhưng thiếu VND (hoặc ngược lại), Treasury thực hiện các giao dịch hoán đổi ngoại tệ (FX Swap). Giá điều chuyển vốn giữa hai đồng tiền được liên kết chặt chẽ thông qua điều kiện **Ngang giá Lãi suất có Bảo hiểm (Covered Interest Parity — CIP)**:
$$F = S \times \frac{1 + r_{\text{VND}} \times \frac{\text{Days}}{365}}{1 + r_{\text{USD}} \times \frac{\text{Days}}{360}}$$
Trong đó:
- $S$: Tỷ giá giao ngay (Spot rate).
- $F$: Tỷ giá kỳ hạn (Forward rate).
- Điểm hoán đổi kỳ hạn (*FX Swap Forward points* $= F - S$) chính là đại lượng chuyển hóa chênh lệch chi phí vốn giữa đường cong FTP VND và đường cong FTP USD.

---

## 4. Chiều Không Gian 3: Phương Pháp Định Giá FTP Chi Tiết Theo Từng Loại Sản Phẩm

Biểu giá FTP phân rã theo bản chất dòng tiền và tính chất rủi ro của từng sản phẩm cụ thể trên bảng cân đối:

```
+---------------------------------------------------------------------------------------------------+
|                     MA TRẬN ĐỊNH GIÁ FTP CHI TIẾT THEO TỪNG LOẠI SẢN PHẨM                          |
+---------------------------------------------------------------------------------------------------+
|  NHÓM SẢN PHẨM         | TÍNH CHẤT DÒNG TIỀN     | CÔNG THỨC FTP VOF / COF    | PHẦN BÙ TLP       |
+------------------------+-------------------------+----------------------------+-------------------+
|  1. TIỀN GỬI (NỢ)      | - Gốc trả cuối kỳ       | VOF = Base(Kỳ hạn gốc)     | TLP = 0           |
|     Lãi suất cố định   |                         |       + Margin + ALCO_adj  | (không chịu TLP)  |
|                        |                         |                            |                   |
|  2. TIỀN GỬI GỬI GÓP   | - Gửi tích lũy hàng kỳ  | VOF = LS gửi góp           | TLP = 0           |
|                        |                         |       + [VOF CKH - LS CKH] |                   |
|                        |                         |                            |                   |
|  3. TIỀN GỬI KKH       | - Không kỳ hạn          | Non-term Redemption Curve: | TLP = 0           |
|     (CASA)             |   (Hành vi dòng tiền)   | VOF = Base_i × %NonCore    |                   |
|                        |                         |     + Base_j × (1 - %Non)  |                   |
|                        |                         |                            |                   |
|  4. CHO VAY CỐ ĐỊNH    | - Gốc trả cuối kỳ       | COF = Base(Kỳ hạn gốc)     | TLP = 0           |
|     (Straight fixed)   |   Lãi suất cố định      |       + Phụ phí pháp định  |                   |
|                        |                         |                            |                   |
|  5. CHO VAY THẢ NỔI    | - Gốc trả cuối kỳ       | COF = Base(Kỳ hạn repricing| TLP = Base(Gốc)   |
|     (Straight float)   |   Lãi suất thả nổi      |       + Phụ phí pháp định  |     - Base(Repr.) |
|                        |                         |       + TLP                |                   |
|                        |                         |                            |                   |
|  6. CHO VAY TRẢ ĐỊNH KỲ| - Gốc trả góp định kỳ   | COF = Base(WAL)            | TLP = 0           |
|     (Amortizing fixed) |   Lãi suất cố định      |       + Phụ phí pháp định  |                   |
|                        |                         |                            |                   |
|  7. CHO VAY TRẢ ĐỊNH KỲ| - Gốc trả góp định kỳ   | COF = Base(Kỳ hạn repricing| TLP = Base(WAL)   |
|     (Amortizing float) |   Lãi suất thả nổi      |       + Phụ phí pháp định  |     - Base(Repr.) |
|                        |                         |       + TLP                |                   |
|                        |                         |                            |                   |
|  8. THẤU CHI, THẺ TÍN  | - Không xác định kỳ hạn | COF = Base_i × %NonCore_OD | TLP = 0           |
|     DỤNG (Overdraft)   |   (Hạn mức thấu chi)    |     + Base_j × %Core_OD    |                   |
|                        |                         |                            |                   |
|  9. HẠN MỨC CHƯA RÚT   | - Cam kết ngoại bảng    | Phụ phí thanh khoản tiềm   | Tính trên phần    |
|     (Undrawn lines)    |   chưa sử dụng          | tàng = C × CCF × TSTK_fee  | hạn mức chưa rút  |
+------------------------+-------------------------+----------------------------+-------------------+
```

### 4.1. Định Giá Sản Phẩm Huy Động (Tài Sản Nợ — VOF)

1. **Tiền gửi trả gốc cuối kỳ, lãi suất cố định**:
   - Áp dụng mức lãi suất VOF cơ sở tương ứng với kỳ hạn gốc của khoản tiền gửi tại ngày phát sinh [[src-vab-ftp#^vab-ftp-6]].
   - Lãi suất VOF cơ sở được **khóa chặt cố định trong suốt kỳ hạn gửi tiền**; không chịu phần bù thanh khoản kỳ hạn (TLP = 0).
2. **Tiền gửi gửi góp (gốc gửi định kỳ)**:
   - Khoản tiền gửi tích lũy định kỳ hàng tháng. Giá VOF cơ sở được tính bằng lãi suất biểu gửi góp cộng với chênh lệch giữa giá VOF và lãi suất của sản phẩm tiền gửi trả gốc cuối kỳ cùng kỳ hạn [[src-vab-ftp#^vab-ftp-6]].
3. **Tiền gửi không kỳ hạn (CASA — Non-term Redemption Curve)**:
   - Áp dụng phương pháp phân tích mô hình hành vi (MHHV) để tách thành dòng tiền không ổn định (*non-core*) và dòng tiền ổn định (*core*) [[src-vab-ftp#^vab-ftp-14]]:
     $$\text{VOF}_{\text{CASA}} = \text{Base Curve}_i \times \text{Non-Core CASA}_i + \text{Base Curve}_j \times (1 - \text{Non-Core CASA}_i)$$
     [[src-vab-ftp#^vab-ftp-15]]
     - Kỳ hạn $i$ (non-core): 1 ngày đến 1 tháng (lãi suất VOF thấp).
     - Kỳ hạn $j$ (core): 6 tháng đến 3 năm (lãi suất VOF cao tương đương kỳ hạn trung dài hạn).
   - Nếu ngân hàng chưa hoàn thiện mô hình hành vi: Áp dụng quy định thận trọng dẫn từ Phụ lục 3 TT22/2019 với tỷ lệ rút tiền tối thiểu $a\% = 15\%$ [[src-vab-ftp#^vab-ftp-16]] [[src-vab-ftp#^vab-ftp-44]]:
     $$\text{VOF} = \text{VOF}_{\text{KKH}} \times 15\% + \text{VOF}_{\text{CKH (2M)}} \times 85\%$$

### 4.2. Định Giá Sản Phẩm Tín Dụng (Tài Sản Có — COF)

1. **Khoản vay trả gốc cuối kỳ, lãi suất cố định (Straight-term, fixed rate)**:
   - Lãi suất COF cơ sở lấy theo đúng kỳ hạn gốc (ngày đáo hạn trừ ngày giải ngân) trên biểu ban hành tại ngày giải ngân [[src-vab-ftp#^vab-ftp-32]].
   - Lãi suất COF cơ sở cố định suốt vòng đời khoản vay. Phần bù TLP = 0.
2. **Khoản vay trả gốc cuối kỳ, lãi suất thả nổi (Straight-term, floating rate)**:
   - Lãi suất COF cơ sở lấy theo **kỳ hạn tái định giá** (ví dụ 3 tháng hoặc 6 tháng) tại ngày giải ngân hoặc ngày điều chỉnh lãi suất [[src-vab-ftp#^vab-ftp-33]].
   - **Bắt buộc cộng thêm phần bù thanh khoản kỳ hạn (TLP)** để bù đắp cam kết thanh khoản vốn gốc dài hạn:
     $$\text{TLP} = \text{Lãi suất COF kỳ hạn gốc} - \text{Lãi suất COF kỳ hạn tái định giá}$$
     [[src-vab-ftp#^vab-ftp-33]]
3. **Khoản vay trả gốc định kỳ, lãi suất cố định (Amortizing, fixed rate)**:
   - Do số dư nợ gốc giảm dần theo thời gian, ngân hàng không thể lấy kỳ hạn cuối cùng để tính giá vốn.
   - Bắt buộc xác định **Kỳ hạn Hiệu lực Bình quân Gia quyền (Weighted Average Life — WAL / WAT)** [[src-vab-ftp#^vab-ftp-20]]:
     $$\text{WAL} = \sum_{i=1}^{N} \frac{P_i \times T_i}{\sum P_i}$$
     Trong đó: $P_i$ là số dư gốc trả kỳ thứ $i$, $T_i$ là số ngày từ ngày giải ngân đến ngày trả nợ lần $i$.
   - Giá COF cơ sở được lấy theo điểm kỳ hạn WAL trên đường cong FTP [[src-vab-ftp#^vab-ftp-20]].
4. **Khoản vay trả gốc định kỳ, lãi suất thả nổi (Amortizing, floating rate)**:
   - Lãi suất COF cơ sở neo theo kỳ hạn tái định giá.
   - Phần bù TLP được xác định bằng chênh lệch giữa kỳ hạn hiệu lực WAL và kỳ hạn tái định giá [[src-vab-ftp#^vab-ftp-34]]:
     $$\text{TLP} = \text{Lãi suất COF}(\text{WAL}) - \text{Lãi suất COF}(\text{Kỳ hạn tái định giá})$$
5. **Cho vay không xác định kỳ hạn (Thấu chi, Thẻ tín dụng)**:
   - Áp dụng mô hình hành vi phân tách Core Overdraft (thường gán kỳ hạn 6M hoặc 1Y do ALCO quy định) và Non-core Overdraft (kỳ hạn 1M hoặc 45 ngày miễn lãi).
6. **Cho vay có chương trình ưu đãi lãi suất**:
   - Chia tách thành 2 giai đoạn độc lập: Giai đoạn trong kỳ ưu đãi (COF áp dụng theo kỳ hạn ưu đãi) và Giai đoạn sau ưu đãi (COF áp dụng theo kỳ hạn còn lại căn cứ vào biểu giá tại ngày hết hạn ưu đãi).

### 4.3. Định Giá Sản Phẩm Cam Kết Ngoại Bảng (Contingent Facilities)
Đối với hạn mức thẻ tín dụng, hạn mức thấu chi hoặc cam kết cấp tín dụng chưa giải ngân:
- Ngân hàng phải duy trì lớp đệm thanh khoản dự phòng đề phòng khách hàng rút vốn bất ngờ trong khủng hoảng.
- CFU áp dụng **Phần bù rủi ro thanh khoản tiềm tàng (Contingent Liquidity Charge)** [[src-vab-ftp#^vab-ftp-35]]:
  $$\text{Phần bù thanh khoản tiềm tàng} = C \times \text{CCF} \times \text{Tỷ lệ dự trữ thanh khoản} \times (\text{VOF bình quân} - \text{Lợi suất TSTK})$$
  Trong đó: $C$ là số dư hạn mức chưa sử dụng; $\text{CCF}$ là hệ số chuyển đổi tín dụng theo Thông tư 41/2016/TT-NHNN (từ 10% đến 50%).

---

## 5. Phân Tách Giữa Thị Trường 1 (Mạng Lưới Chi Nhánh) Và Thị Trường 2 (Liên Ngân Hàng / Treasury)

Hệ thống FTP tại ngân hàng được vận hành theo kiến trúc hai thị trường chuyên biệt:

```
+---------------------------------------------------------------------------------------------------+
|               SO SÁNH CƠ CHẾ FTP: THỊ TRƯỜNG 1 (CHI NHÁNH) VS THỊ TRƯỜNG 2 (TREASURY)              |
+---------------------------------------------------------------------------------------------------+
|  TIÊU CHÍ              | THỊ TRƯỜNG 1 (MẠNG LƯỚI CHI NHÁNH)     | THỊ TRƯỜNG 2 (TREASURY / LIÊN NH)|
+------------------------+----------------------------------------+---------------------------------+
|  1. Đối tượng         | Chi nhánh, Khối Bán lẻ, Khối KHDN      | Khối Quản lý & Kinh doanh Vốn   |
|     tham gia           | giao dịch với CFU                      | (QL&KDV / Treasury) với CFU     |
|                        |                                        |                                 |
|  2. Cơ chế biểu giá    | Ban hành định kỳ (tháng/quý)           | Deal-by-deal pricing thời gian  |
|                        | Cố định theo kỳ hạn hợp đồng           | thực (real-time) hoặc hàng ngày |
|                        |                                        |                                 |
|  3. Căn cứ xác định    | Đường cong FTP chuẩn hóa               | - Phương án 1: Mid-rate bình    |
|     lãi suất           | + Hỗ trợ huy động (Margin)             |   quân của 3–6 ngân hàng cùng   |
|                        | + Điều chỉnh ALCO Adjust               |   nhóm Peer tín nhiệm           |
|                        | + Phụ phí pháp định (DTBB, BHTG, TLP)  | - Phương án 2: VNIBOR 1 tuần    |
|                        |                                        |                                 |
|  4. Lọc dữ liệu        | Phê duyệt bởi Hội đồng ALCO            | Loại bỏ dữ liệu ngoại lai       |
|     bất thường         |                                        | (outlier) nếu lệch quá ±15%     |
|                        |                                        | so với trung bình nhóm Peer     |
+---------------------------------------------------------------------------------------------------+
```

Theo quy định tư vấn của EY cho VietABank:
- **Thị trường 2 (Interbank)** phản ánh giá giao dịch bán buôn sòng phẳng giữa các định chế tài chính [[src-vab-ftp#^vab-ftp-36]]. Lãi suất mua bán vốn TT2 được xác định dựa trên bình quân giá chào mua và chào bán (mid-rate) của 3 đến 6 ngân hàng thương mại có cùng quy mô tài sản, cùng mức xếp hạng tín nhiệm và có quan hệ giao dịch tích cực [[src-vab-ftp#^vab-ftp-37]].
- Trạng thái ròng (net position) của Khối Treasury được thanh toán nội bộ với CFU dựa trên lãi suất VNIBOR kỳ hạn 1 tuần, kết hợp với hạn mức thanh khoản 30 ngày để đảm bảo tỷ lệ an toàn của NHNN.

---

## 6. Tổng Kết: Quy Trình Vận Hành 5 Bước Xây Dựng Đường Cong FTP

Để đường cong FTP luôn là tấm gương phản chiếu trung thực chi phí vốn và rủi ro của toàn hàng, Phòng ALM/CFU thực hiện quy trình vận hành chuẩn mực gồm 5 bước:

```
[BƯỚC 1: THU THẬP DỮ LIỆU ĐẦU VÀO]
├── Lãi suất thị trường: VNIBOR, OMO, Tín phiếu SBV, Lợi suất TPCP (VGB), SOFR, IRS
├── Dữ liệu giao dịch nội bộ: Số dư và lãi suất huy động 3 tháng gần nhất theo từng đồng tiền
└── Tham số pháp định: Tỷ lệ DTBB, Phí BHTG 0.15%, Danh mục TSTK Phụ lục 3 TT22
                  │
                  ▼
[BƯỚC 2: THIẾT LẬP ĐƯỜNG CONG CƠ SỞ (BASE CURVES)]
├── Xây dựng Base Curve VND (kết hợp VNIBOR và TPCP)
└── Xây dựng Base Curve Ngoại tệ (USD SOFR + USD IRS; EUR, JPY)
                  │
                  ▼
[BƯỚC 3: TÍNH TOÁN CÁC PHỤ PHÍ RỦI RO & PHÁP ĐỊNH (SPREADS)]
├── Tỷ lệ Chi phí DTBB & Chi phí BHTG phân bổ vào COF
├── Chi phí gánh đệm thanh khoản Liquidity Buffer Premium
└── Bảng tra cứu Term Liquidity Premium (TLP) theo ma trận kỳ hạn gốc vs kỳ hạn tái định giá
                  │
                  ▼
[BƯỚC 4: HIỆU CHỈNH CHÍNH SÁCH ĐIỀU HÀNH CỦA ALCO]
├── Phân bổ chỉ tiêu NIM toàn hàng xuống NIM huy động (Margin)
└── Áp dụng các hệ số điều chỉnh ALCO Adjust theo kỳ hạn/sản phẩm mục tiêu
                  │
                  ▼
[BƯỚC 5: BAN HÀNH VÀ ÁP GIÁ TỰ ĐỘNG LÊN HỆ THỐNG CORE BANKING]
├── Biểu giá VOF cho các sản phẩm tiền gửi (Thị trường 1)
├── Biểu giá COF cho các sản phẩm tín dụng (Thị trường 1)
└── Cơ chế Deal-by-deal cho Khối Quản lý & Kinh doanh Vốn (Thị trường 2)
```

## Khái niệm và Liên kết
- [[ftp-final-rate-determination]]: Xác định mức lãi suất FTP rate cuối cùng cho từng giao dịch và sản phẩm.
- [[ftp-cost-benefit-allocation-principles]]: Nguyên tắc phân bổ chi phí và lợi ích của từng FTP portfolio cho các đơn vị kinh doanh và sản phẩm.
- [[ftp-portfolio-and-bucket-allocation]]: Phương pháp phân bổ giao dịch và sản phẩm vào các danh mục và thang kỳ hạn FTP theo 7 tiêu chí kỹ trị.
- [[ftp-risk-and-cost-components]]: Phân tích chi tiết 4 cấu phần rủi ro trong định giá FTP.
- [[ftp-pricing-methodology]]: Phương pháp luận định giá VOF, COF và phụ phí tuân thủ ngân hàng.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn điều tiết rủi ro thanh khoản, lãi suất và tín dụng của FTP.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU qua FTP.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa bảng cân đối ALM toàn diện dưới hệ thống điều khiển FTP.
- [[liquidity-transfer-pricing]]: Tổng quan lý thuyết định giá điều chuyển thanh khoản nội bộ theo Moorad Choudhry.
- [[synthetic-balance-sheet-liquidity-risk]]: Bảng cân đối thanh khoản tổng hợp và động lực dòng tiền.
- [[practical-alm-liquidity-governance]]: Khung điều hành quản trị thanh khoản thực chiến.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.
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
