---
title: "Phương Pháp Phân Bổ Giao Dịch Và Sản Phẩm Vào Các FTP Portfolio Và Tenor Bucket"
aliases: [FTP Portfolio and Bucket Allocation, Phân bổ danh mục và kỳ hạn FTP, FTP Bucketing Rules, FTP Allocation Criteria, Portfolio Segmentation FTP]
type: synthesis
domains: [alm, product]
status: active
maturity: canonical
origin: query
question: "Các giao dịch hoặc sản phẩm được phân bổ vào các FTP portfolio/bucket như thế nào? Tiêu chí phân bổ là gì?"
sources: ["[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-ftp-transmission-analysis]]"]
relations: []
tags: [ftp, portfolio-segmentation, bucketing-rules, tenor-buckets, allocation-criteria, wal, cash-flow-mapping, synthesis]
updated: 2026-10-17
reviewed:
---

## 1. Tóm Tắt Quản Trị Cấp Cao (Executive Summary)

Trong kỹ trị ALM hiện đại, việc **phân bổ giao dịch và sản phẩm vào các Danh mục FTP (FTP Portfolios) và Thang kỳ hạn (Tenor Buckets)** là khâu trung gian chuyển hóa giữa toàn bộ dữ liệu hợp đồng thô của Core Banking và hệ thống định giá điều chuyển vốn nội bộ [[src-ftp-transmission-analysis#^ftp-trans-1]]. 

Nếu phân bổ sai Portfolio, ngân hàng sẽ làm méo mó việc đo lường hiệu quả kinh doanh giữa các Khối; nếu phân bổ sai Bucket kỳ hạn, ngân hàng sẽ gán sai lãi suất cơ sở, bỏ sót phần bù thanh khoản kỳ hạn (TLP) và phá vỡ cơ chế phòng ngừa rủi ro lãi suất tập trung tại Treasury [[src-choudhry-principles-banking#^choudhry-ftp-11]].

Quy trình phân bổ được thực hiện theo cấu trúc phân tầng chặt chẽ:
1. **Phân bổ theo Danh mục (Portfolio Segmentation)**: Tách bạch giữa Sổ ngân hàng (Banking Book / Thị trường 1) với Sổ kinh doanh (Trading Book / Thị trường 2); phân định các Portfolio Tài sản nợ (Huy động), Tài sản có (Cho vay & Đầu tư) và các Danh mục đặc biệt bị loại trừ khỏi FTP thông thường (Đệm tài sản thanh khoản HQLA, Tài sản cố định tài trợ bởi Vốn chủ sở hữu) [[src-vab-ftp#^vab-ftp-10]].
2. **Phân bổ theo Thang kỳ hạn (Bucketing & Cash Flow Mapping)**: Áp dụng **7 tiêu chí kỹ trị cốt lõi** để định tuyến từng dòng tiền vào các Bucket kỳ hạn chuẩn (O/N đến 10Y) hoặc điểm kỳ hạn nội suy, dựa trên: (1) Cơ chế lãi suất (Cố định vs Thả nổi); (2) Cấu trúc dòng tiền gốc (Trả cuối kỳ vs Trả định kỳ theo WAL); (3) Kỳ hạn hợp đồng vs Hành vi (CASA Core/Non-core); (4) Đồng tiền độc lập; (5) Tính chất ưu đãi; (6) Trạng thái tín dụng; và (7) Tính chất ngoại bảng / Quyền chọn ẩn [[src-vab-ftp#^vab-ftp-20]] [[src-vab-ftp#^vab-ftp-33]].

```
+---------------------------------------------------------------------------------------------------+
|               SƠ ĐỒ PHÂN TẦNG ĐỊNH TUYẾN DÒNG TIỀN VÀO CÁC FTP PORTFOLIO VÀ BUCKET                |
+---------------------------------------------------------------------------------------------------+
|                                     TOÀN BỘ BẢNG CÂN ĐỐI KẾ TOÁN                                  |
|                                                  │                                                |
|            ┌─────────────────────────────────────┴─────────────────────────────────────┐          |
|            ▼                                                                           ▼          |
|  [ DANH MỤC LOẠI TRỪ FTP THÔNG THƯỜNG ]                                   [ CÁC DANH MỤC TÍNH FTP ] |
|  - Đệm TSTK thanh khoản cao (Phụ lục 3 TT22)                                           │          |
|  - Tiền mặt tồn quỹ trong hạn mức, Nostro NHNN                                         │          |
|  - Tài sản cố định (tài trợ bởi VCSH)                                                  │          |
|  (Được CFU quản lý tập trung và phân bổ chi phí)                                       │          |
|                                                                                        │          |
|            ┌───────────────────────────────────────────────────────────────────────────┘          |
|            ▼                                                                                      |
|  [ PHÂN BỔ THỊ TRƯỜNG & SỔ ]                                                                      |
|  ├── Sổ Kinh doanh / Khối QL&KDV (Thị trường 2): Deal-by-deal real-time hoặc Net Position VNIBOR  |
|  └── Sổ Ngân hàng / Mạng lưới Chi nhánh (Thị trường 1): Áp biểu định kỳ tháng/quý                 |
|            │                                                                                      |
|            ▼                                                                                      |
|  [ PHÂN BỔ THEO 7 TIÊU CHÍ KỸ TRỊ ]                                                               |
|  ├── 1. Cơ chế Lãi suất: Cố định (Fixed Tenor) vs Thả nổi (Repricing Bucket + TLP Bucket)         |
|  ├── 2. Lịch trả gốc: Cuối kỳ (Contractual Maturity) vs Định kỳ (Weighted Average Life - WAL)    |
|  ├── 3. Tính chất Kỳ hạn: Có kỳ hạn xác định vs Phi kỳ hạn (CASA Core vs Non-core)                |
|  ├── 4. Đồng tiền: Phân lập độc lập tuyệt đối (VND Bucket vs USD Bucket)                          |
|  ├── 5. Tính chất Ưu đãi: Chia nhỏ kỳ ưu đãi (Promo Tenor) vs kỳ ngoài ưu đãi                     |
|  ├── 6. Trạng thái Tín dụng: Nợ trong hạn, Nợ quá hạn (đóng băng COF), Nợ gia hạn                 |
|  └── 7. Ngoại bảng & Quyền chọn: Hạn mức chưa rút (Contingent Liquidity), Prepayment WAL          |
|            │                                                                                      |
|            ▼                                                                                      |
|  [ ÁP VÀO CÁC TENOR BUCKET CHUẨN TRÊN HỆ THỐNG ]                                                  |
|  O/N │ 1W │ 2W │ 3W │ 1M │ 2M │ 3M │ 6M │ 9M │ 12M │ 18M │ 24M │ 36M │ 60M (5Y) │ 120M (10Y)     |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Phân Bổ Theo Danh Mục FTP (Portfolio Segmentation)

Trong kiến trúc quản trị ALM, toàn bộ các khoản mục tài sản nội và ngoại bảng được phân loại thành 4 nhóm danh mục lớn:

```
+---------------------------------------------------------------------------------------------------+
|                          BỐN NHÓM DANH MỤC FTP TRÊN BẢNG CÂN ĐỐI                                  |
+---------------------------------------------------------------------------------------------------+
|  DANH MỤC               | PHẠM VI SẢN PHẨM               | CƠ CHẾ FTP ÁP DỤNG                     |
+-------------------------+--------------------------------+----------------------------------------+
|  1. DANH MỤC HUY ĐỘNG   | - Tiền gửi tiết kiệm, có kỳ hạn| Áp dụng Biểu giá Mua vốn (VOF):        |
|     (Liability Book)    | - Tiền gửi không kỳ hạn (CASA) | VOF = Base + Margin + ALCO_adj         |
|                         | - Tiền gửi gửi góp, ký quỹ     | Khóa biên huy động cố định cho BU      |
|                         | - Giấy tờ có giá (GTCG) TT1    |                                        |
|                         |                                |                                        |
|  2. DANH MỤC TÍN DỤNG   | - Cho vay Khách hàng Cá nhân   | Áp dụng Biểu giá Bán vốn (COF):        |
|     (Asset Book)        | - Cho vay Khách hàng Doanh ngh.| COF = Base + Margin + Phụ phí pháp định|
|                         | - Thấu chi, Thẻ tín dụng       |       (DTBB, BHTG, Buffer, TLP)        |
|                         | - Trái phiếu Doanh nghiệp HTM  |                                        |
|                         |                                |                                        |
|  3. DANH MỤC TREASURY   | - Nhận/gửi tiền Liên ngân hàng | Áp dụng Cơ chế Thị trường 2 (TT2):     |
|     (Interbank Book)    | - Giao dịch FX, Repo/Reverse   | Deal-by-deal real-time bám sát mid-rate|
|                         | - Trái phiếu Chính phủ trading | nhóm Peer hoặc VNIBOR 1 tuần           |
|                         |                                |                                        |
|  4. DANH MỤC LOẠI TRỪ   | - Đệm TSTK cao (Phụ lục 3 TT22)| KHÔNG tính FTP trực tiếp cho BU:       |
|     (Excluded Book)     | - Tiền mặt tồn quỹ trong hạn m.| Chi phí cơ hội (negative carry) được   |
|                         | - Tài khoản Nostro tại NHNN    | CFU gom lại và phân bổ vào COF chung   |
|                         | - Tài sản cố định tài trợ VCSH | qua Liquidity Buffer Premium           |
+-------------------------+--------------------------------+----------------------------------------+
```

### 2.1. Danh mục Loại trừ (Excluded Portfolios)
Theo quy định tư vấn của EY cho VietABank, không phải mọi tài sản trên bảng cân đối đều được mua bán vốn thông thường qua FTP [[src-vab-ftp#^vab-ftp-10]]:
1. **Tài sản Thanh khoản Đệm (Liquidity Buffer Assets)**: Bao gồm tiền mặt tồn quỹ trong hạn mức, tiền gửi Nostro tại NHNN, và các Trái phiếu Chính phủ nắm giữ làm đệm thanh khoản theo Phụ lục 3 Thông tư 22/2019/TT-NHNN [[src-vab-ftp#^vab-ftp-10]].
   - *Nguyên tắc kỹ trị*: Các tài sản này **bị loại trừ hoàn toàn khỏi mẫu số Tổng tài sản bị tính FTP** [[src-vab-ftp#^vab-ftp-10]]. Chi phí cơ hội do nắm giữ tài sản lợi suất thấp đã được CFU lượng hóa thành cấu phần *Liquidity Buffer Premium* và phân bổ đều vào giá bán vốn COF của các tài sản sinh lời khác.
2. **Tài sản Cố định & Tài sản Phi Sinh lời**: Được tài trợ trực tiếp từ nguồn Vốn chủ sở hữu (Equity), không phát sinh nhu cầu huy động vốn từ thị trường nên không tính FTP [[src-vab-ftp#^vab-ftp-10]].
3. **Tài sản của Khối Quản lý & Kinh doanh Vốn (QL&KDV)**: Mua bán theo cơ chế riêng của Thị trường 2, không đưa vào danh mục tính FTP Thị trường 1.

---

## 3. Bảy Tiêu Chí Kỹ Trị Phân Bổ Vào Các Tenor Buckets

Để định vị chính xác mức lãi suất FTP nội bộ cho từng giao dịch, hệ thống ALM áp dụng tuần tự 7 tiêu chí phân bổ:

```
+---------------------------------------------------------------------------------------------------+
|                         BẢY TIÊU CHÍ KỸ TRỊ PHÂN BỔ VÀO CÁC FTP BUCKETS                           |
+---------------------------------------------------------------------------------------------------+
|  1. CƠ CHẾ LÃI SUẤT           | Lãi suất cố định -> Bucket kỳ hạn gốc / WAL                       |
|                               | Lãi suất thả nổi -> Repricing Bucket (Base) + Tenor Bucket (TLP)  |
|                               |                                                                   |
|  2. ĐẶC TÍNH HOÀN TRẢ GỐC     | Trả gốc cuối kỳ -> Contractual Maturity Bucket                    |
|                               | Trả gốc định kỳ -> Weighted Average Life (WAL) Bucket             |
|                               |                                                                   |
|  3. KỲ HẠN HỢP ĐỒNG VS HÀNH VI| Có kỳ hạn -> Phân bổ theo lịch dòng tiền hợp đồng                 |
|                               | Phi kỳ hạn (CASA) -> Core Bucket (dài hạn) vs Non-core (ngắn hạn) |
|                               |                                                                   |
|  4. LOẠI ĐỒNG TIỀN (CURRENCY) | Phân lập độc lập tuyệt đối: VND Bucket riêng, USD Bucket riêng    |
|                               | Không bù trừ chéo dòng tiền giữa các loại tiền tệ                 |
|                               |                                                                   |
|  5. TÍNH CHẤT ƯU ĐÃI (PROMO)  | Tách 2 giai đoạn: Trong kỳ ưu đãi (áp Tenor ưu đãi)               |
|                               | Ngoài kỳ ưu đãi (áp Tenor còn lại theo giá thị trường mới)        |
|                               |                                                                   |
|  6. TRẠNG THÁI TÍN DỤNG       | Nợ trong hạn -> Áp biểu FTP chuẩn                                 |
|                               | Nợ quá hạn -> Đóng băng COF tại thời điểm quá hạn                 |
|                               | Nợ gia hạn -> Bucket mới = Kỳ hạn cũ + Thời gian gia hạn thêm     |
|                               |                                                                   |
|  7. TÍNH CHẤT NGOẠI BẢNG &    | Hạn mức tín dụng chưa rút -> Contingent Liquidity Charge          |
|     QUYỀN CHỌN ẨN             | Prepayment -> Rút ngắn WAL Bucket theo mô hình CPR                |
|                               | Early Withdrawal -> Hồi tố gán vào Bucket tiền gửi không kỳ hạn   |
+---------------------------------------------------------------------------------------------------+
```

---

### 3.1. Tiêu Chí 1: Cơ Chế Lãi Suất (Rate Mechanism — Cố Định vs Thả Nổi)

- **Sản phẩm Lãi suất Cố định (Fixed-Rate Products)**:
  - *Cách phân bổ*: Toàn bộ số dư được gán vào **Tenor Bucket trùng khớp với kỳ hạn gốc** (đối với trả cuối kỳ) hoặc **WAL Bucket** (đối với trả định kỳ) [[src-vab-ftp#^vab-ftp-32]].
  - *Đặc điểm*: Mức lãi suất FTP cơ sở giữ nguyên không đổi suốt vòng đời hợp đồng. Không áp dụng phần bù thanh khoản kỳ hạn ($\text{TLP} = 0$).
- **Sản phẩm Lãi suất Thả nổi (Floating-Rate Products)**:
  - *Cách phân bổ*: Bản chất của sản phẩm thả nổi là sự kết hợp giữa cam kết thanh khoản dài hạn và rủi ro tái định giá ngắn hạn. Hệ thống phân rã và gán vào **2 Bucket đồng thời** [[src-vab-ftp#^vab-ftp-33]]:
    1. **Repricing Bucket (Dải kỳ hạn tái định giá)**: Gán số dư vào kỳ hạn điều chỉnh lãi suất (1M, 3M, 6M) để xác định Lãi suất Cơ sở (Base Rate). Lãi suất này được cập nhật lại vào mỗi ngày điều chỉnh lãi suất.
    2. **Liquidity Tenor Bucket (Dải kỳ hạn thanh khoản gốc)**: Gán số dư vào kỳ hạn gốc hợp đồng hoặc kỳ hạn hiệu lực WAL để tính **Phần bù thanh khoản kỳ hạn (Term Liquidity Premium — TLP)**:
       $$\text{TLP} = \text{Lãi suất COF}(\text{Kỳ hạn gốc/WAL}) - \text{Lãi suất COF}(\text{Kỳ hạn tái định giá})$$
       [[src-vab-ftp#^vab-ftp-33]]
  - *Ý nghĩa*: Chặn đứng tình trạng chi nhánh giải ngân khoản vay 10 năm thả nổi 3 tháng rồi chỉ trả chi phí vốn 3 tháng, đẩy rủi ro thanh khoản dài hạn cho Treasury.

---

### 3.2. Tiêu Chí 2: Đặc Tính Hoàn Trả Gốc (Amortization Pattern — Cuối Kỳ vs Định Kỳ)

- **Khoản vay Trả gốc Cuối kỳ (Bullet / Straight-term)**:
  - Kỳ hạn phân bổ được tính đơn giản bằng:
    $$T_{\text{gốc}} = \text{Ngày đáo hạn} - \text{Ngày giải ngân}$$
- **Khoản vay Trả gốc Định kỳ (Amortizing / Installment Loans)**:
  - *Vấn đề*: Khách hàng trả nợ gốc đều đặn hàng tháng/quý. Số dư nợ giảm dần theo thời gian, do đó việc áp giá FTP theo kỳ hạn cuối cùng sẽ đánh giá quá cao chi phí vốn của khoản vay.
  - *Quy tắc phân bổ*: Bắt buộc chuyển đổi toàn bộ dòng tiền trả nợ thành **Kỳ hạn Hiệu lực Bình quân Gia quyền (Weighted Average Life — WAL / WAT)** [[src-vab-ftp#^vab-ftp-20]]:
    $$\text{WAL} = \sum_{i=1}^{N} \frac{P_i \times T_i}{\sum P_i}$$
    Trong đó:
    - $P_i$: Số dư gốc được thanh toán trong kỳ thứ $i$.
    - $T_i$: Khoảng thời gian từ ngày giải ngân đến ngày thanh toán lần thứ $i$ (tính theo số ngày thực tế).
  - *Ví dụ minh họa*: Khoản vay 5 năm (60 tháng), trả gốc đều mỗi tháng. Kỳ hạn pháp lý là 5 năm, nhưng kỳ hạn hiệu lực WAL thực tế chỉ xấp xỉ **2.5 năm**. Khoản vay sẽ được gán vào **Tenor Bucket 2.5 năm** trên đường cong FTP thay vì 5 năm [[src-vab-ftp#^vab-ftp-20]].

---

### 3.3. Tiêu Chí 3: Tính Chất Kỳ Hạn Hợp Đồng vs Hành Vi (Contractual vs Behavioural)

Đối với các sản phẩm phi kỳ hạn (Non-Maturity Products), dòng tiền không có ngày đáo hạn pháp lý:

```
+---------------------------------------------------------------------------------------------------+
|             PHÂN BỔ DÒNG TIỀN TIỀN GỬI KHÔNG KỲ HẠN (CASA) THEO MÔ HÌNH HÀNH VI                   |
+---------------------------------------------------------------------------------------------------+
|                                      TỔNG SỐ DƯ TIỀN GỬI CASA                                     |
|                                                  │                                                |
|                        ┌─────────────────────────┴─────────────────────────┐                      |
|                        ▼                                                   ▼                      |
|       [ NON-CORE CASA BUCKET ]                            [ CORE CASA BUCKET ]                    |
|       - Tỷ lệ: %NonCore (biến động)                       - Tỷ lệ: (1 - %NonCore) (bền vững)      |
|       - Bản chất: Dòng tiền luân chuyển thanh             - Bản chất: Số dư đọng lại ổn định      |
|         toán hàng ngày của khách hàng                       nhờ thói quen tiêu dùng & trả lương   |
|       - Bucket phân bổ: O/N đến 1 tháng                   - Bucket phân bổ: 6 tháng đến 3–5 năm   |
|       - Lãi suất VOF: Rất thấp                            - Lãi suất VOF: Rất cao (kỳ hạn dài)    |
+---------------------------------------------------------------------------------------------------+
```

- **Tiền gửi Không kỳ hạn (CASA)**:
  - Áp dụng **Mô hình Danh mục Sao chép (Replicating Portfolio)** và **Đường cong Hoàn trả Non-term Redemption Curve** [[src-vab-ftp#^vab-ftp-14]]:
    - **Non-core Bucket**: Phân bổ vào thang kỳ hạn $i$ (O/N đến 1M).
    - **Core Bucket**: Phân bổ vào thang kỳ hạn $j$ (6M đến 3–5 năm do ALCO quy định) [[src-vab-ftp#^vab-ftp-15]].
  - *Công thức gán VOF*:
    $$\text{VOF}_{\text{CASA}} = \text{Base Curve}_i \times \text{Non-Core CASA}_i + \text{Base Curve}_j \times (1 - \text{Non-Core CASA}_i)$$
    [[src-vab-ftp#^vab-ftp-15]]
  - *Nếu chưa có mô hình hành vi*: Áp dụng tỷ lệ thận trọng Thông tư 22/2019/TT-NHNN: gán 15% vào Bucket KKH và 85% vào Bucket có kỳ hạn (2 tháng) [[src-vab-ftp#^vab-ftp-16]].
- **Cho vay Thấu chi & Thẻ tín dụng (Overdraft)**:
  - Phân bổ thành **Core OD** (gán vào Bucket 6M hoặc 1Y do ALCO quy định) và **Non-core OD** (gán vào Bucket 1M hoặc 45 ngày miễn lãi) [[src-vab-ftp#^vab-ftp-35]].

---

### 3.4. Tiêu Chí 4: Loại Đồng Tiền (Currency Segmentation)

- **Nguyên tắc phân lập**: Mỗi loại tiền tệ (VND, USD, EUR, JPY,...) cấu thành một Portfolio độc lập và sở hữu một bảng thang kỳ hạn chuẩn riêng biệt [[src-vab-ftp#^vab-ftp-26]].
- **Quy tắc gán Bucket**:
  - Giao dịch bằng đồng tiền nào thì bắt buộc phải ánh xạ vào Tenor Bucket của đồng tiền đó.
  - Khoản vay bằng USD tuyệt đối không được gán vào đường cong VND rồi quy đổi tỷ giá.
  - Các phụ phí DTBB và LCR Buffer được tính toán độc lập cho từng Portfolio đồng tiền [[src-vab-ftp#^vab-ftp-27]].

---

### 3.5. Tiêu Chí 5: Tính Chất Ưu Đãi (Standard vs Non-Standard Promotional Loans)

Nhiều sản phẩm tín dụng cạnh tranh có cấu trúc hai giai đoạn: ví dụ vay 5 năm, cố định ưu đãi 7.5% trong 1 năm đầu, sau đó thả nổi 3 tháng/lần trong 4 năm tiếp theo.
Hệ thống FTP cung cấp **2 phương án phân bổ Bucket** [[src-vab-ftp#^vab-ftp-32]]:

1. **Phương án 1 (Giữ nguyên kỳ hạn gốc, đổi kỳ tái định giá)**:
   - Năm đầu tiên: Gán vào Bucket 5 năm có tần suất tái định giá 12 tháng.
   - Bốn năm sau: Gán vào Bucket 5 năm có tần suất tái định giá 3 tháng.
2. **Phương án 2 (Tách nhỏ sản phẩm — Split Bucketing — Khuyến nghị)**:
   - **Giai đoạn ưu đãi (1 năm đầu)**: Gán vào **Bucket 1 năm cố định**. Áp COF cố định 1 năm, $\text{TLP} = 0$.
   - **Giai đoạn sau ưu đãi (4 năm còn lại)**: Gán vào **Bucket tái định giá 3 tháng**, đồng thời tính phụ phí TLP dựa trên kỳ hạn gốc còn lại là 4 năm:
     $$\text{TLP} = \text{COF}(4\text{Y}) - \text{COF}(3\text{M})$$
   - *Ưu điểm*: Đảm bảo tính toán sòng phẳng chi phí vốn giữa thời kỳ được ngân hàng trợ giá và thời kỳ hoạt động theo cơ chế thị trường bình thường.

---

### 3.6. Tiêu Chí 6: Trạng Thái Tín Dụng & Cơ Cấu Nợ (Credit Status)

- **Khoản vay trong hạn (Standard Performing Loans)**: Phân bổ vào các Tenor Bucket bình thường theo hợp đồng.
- **Khoản vay Quá hạn (Overdue Loans)**:
  - Khi khoản vay bị chuyển nhóm nợ quá hạn, hệ thống **đóng băng mức lãi suất COF cơ sở tại thời điểm quá hạn** và giữ nguyên cố định trong suốt thời gian quá hạn.
  - Ngân hàng không điều chỉnh giảm COF kể cả khi lãi suất thị trường hạ nhiệt, nhằm phản ánh đúng rủi ro thanh khoản bị ứ đọng do nợ xấu.
- **Khoản vay Gia hạn nợ (Restructured / Extended Loans)**:
  - Phân bổ lại vào một **Tenor Bucket mới** có kỳ hạn bằng:
    $$\text{Kỳ hạn mới} = \text{Kỳ hạn gốc ban đầu} + \text{Thời gian gia hạn thêm}$$
  - Giá COF mới được cập nhật theo đường cong FTP tại ngày gia hạn nợ.

---

### 3.7. Tiêu Chí 7: Cam Kết Ngoại Bảng & Quyền Chọn Ẩn (Off-Balance Sheet & Embedded Options)

- **Cam kết Tín dụng Ngoại bảng Chưa Rút Vốn (Undrawn Commitments)**:
  - Không phân bổ vào tài sản có nội bảng thông thường.
  - Gán vào **Contingent Liquidity Bucket** để tính phí duy trì đệm thanh khoản dự phòng [[src-vab-ftp#^vab-ftp-35]]:
    $$\text{Phí thanh khoản tiềm tàng} = C \times \text{CCF} \times \text{Tỷ lệ dự trữ TSTK} \times (\text{VOF} - \text{Lợi suất TSTK})$$
    Trong đó: $C$ là hạn mức chưa sử dụng, $\text{CCF}$ là hệ số chuyển đổi tín dụng theo Thông tư 41/2016/TT-NHNN.
- **Khoản vay có Quyền chọn Trả trước (Prepayment Option)**:
  - Dòng tiền được rút ngắn dựa trên tỷ lệ trả nợ trước hạn (CPR). Khoản vay được gán vào **Effective WAL Bucket** ngắn hơn kỳ hạn danh nghĩa, đồng thời cộng thêm phụ phí phòng ngừa quyền chọn (*prepayment charge*).
- **Tiền gửi Rút trước hạn**:
  - Hồi tố toàn bộ phần chênh lệch VOF kỳ hạn dài, gán lại khoản tiền rút sớm vào **Bucket tiền gửi không kỳ hạn (KKH)** theo Thông tư 04/2022/TT-NHNN.

---

## 4. Ma Trận Quy Tắc Ánh Xạ Sản Phẩm Vào FTP Buckets (Master Bucketing Rule Matrix)

Bảng tổng hợp chi tiết quy tắc ánh xạ kỹ thuật cho toàn bộ sản phẩm trên Core Banking:

| Mã Sản phẩm | Tên Sản phẩm / Giao dịch | Danh mục (Portfolio) | Tiêu chí phân bổ Bucket | Tenor Bucket ánh xạ | Quy tắc tính TLP |
|:---:|:---|:---:|:---|:---|:---:|
| **TD-01** | Tiền gửi tiết kiệm trả lãi cuối kỳ | Huy động (TT1) | Lãi suất cố định, gốc trả cuối kỳ | Trùng khớp Kỳ hạn gốc ($T_{\text{gốc}}$) | $\text{TLP} = 0$ |
| **TD-02** | Tiền gửi gửi góp tích lũy | Huy động (TT1) | Gửi tích lũy định kỳ | Kỳ hạn hợp đồng gửi góp | $\text{TLP} = 0$ |
| **CASA-01**| Tiền gửi thanh toán / KKH cá nhân | Huy động (TT1) | Mô hình hành vi Replicating Portfolio | Split: Non-core (1M) vs Core (1Y–3Y) | $\text{TLP} = 0$ |
| **CASA-02**| Tiền gửi KKH doanh nghiệp | Huy động (TT1) | Mô hình hành vi Replicating Portfolio | Split: Non-core (O/N) vs Core (6M–1Y) | $\text{TLP} = 0$ |
| **LN-01** | Cho vay mua nhà cố định 3 năm | Tín dụng (TT1) | Lãi suất cố định, trả định kỳ | Kỳ hạn hiệu lực WAL ($\approx 1.8\text{Y}$) | $\text{TLP} = 0$ |
| **LN-02** | Cho vay SXKD 1 năm trả gốc cuối kỳ | Tín dụng (TT1) | Lãi suất cố định, gốc cuối kỳ | Kỳ hạn gốc 12 tháng (12M) | $\text{TLP} = 0$ |
| **LN-03** | Cho vay thế chấp 10 năm thả nổi 3M | Tín dụng (TT1) | Lãi suất thả nổi, trả định kỳ | Base: Bucket 3M; TLP: Bucket WAL (5Y) | $\text{TLP} = \text{COF}(\text{WAL}) - \text{COF}(3\text{M})$ |
| **LN-04** | Cho vay ưu đãi (1Y cố định + 4Y float)| Tín dụng (TT1) | Sản phẩm ưu đãi chia 2 giai đoạn | GĐ1: Bucket 1Y; GĐ2: Base 3M + TLP 4Y | $\text{TLP}$ áp dụng cho GĐ2 |
| **OD-01** | Thấu chi tài khoản cá nhân/doanh nghiệp| Tín dụng (TT1) | Dư nợ không xác định kỳ hạn | Split: Core OD (1Y) vs Non-core OD (1M) | $\text{TLP} = 0$ |
| **LC-01** | Cam kết tín dụng / Hạn mức chưa rút | Ngoại bảng (TT1)| Cam kết tiềm tàng chưa sử dụng | Contingent Liquidity Bucket | Tính phí trên $C \times \text{CCF}$ |
| **IB-01** | Gửi tiền liên ngân hàng 1 tuần | Treasury (TT2) | Thị trường 2 (Interbank) | Deal-by-deal Tenor 1W (Mid-rate Peer) | Theo giá khớp thực |
| **IB-02** | Trạng thái ròng MM Desk | Treasury (TT2) | Bù trừ trạng thái Khối QL&KDV | VNIBOR Bucket 1W | Thanh toán ròng với CFU |
| **EX-01** | Trái phiếu Chính phủ đệm TT22 | Loại trừ | Tài sản thanh khoản cao HQLA | Excluded khỏi FTP nội bộ (CFU quản lý)| Phân bổ qua Buffer Premium |

---

## 5. Ý Nghĩa Kỹ Trị Đối Với Vận Hành Hệ Thống ALM

Việc chuẩn hóa quy tắc phân bổ vào các FTP Portfolio và Tenor Bucket mang lại 3 giá trị sống còn cho ngân hàng:
1. **Tự động hóa hoàn toàn trên hệ thống**: Loại bỏ sự can thiệp chủ quan hoặc gian lận phân bổ từ các chi nhánh (ví dụ cố tình khai báo khoản vay thả nổi thành cố định, hoặc khai báo tiền gửi doanh nghiệp thông thường thành tiền gửi vận hành operational deposits để né phụ phí).
2. **Khóa chặt rủi ro và bảo toàn biên lợi nhuận (Matched-Maturity)**: Định tuyến chính xác từng dòng tiền vào đúng bucket phòng ngừa tương ứng, giúp chi nhánh an tâm kinh doanh với biên thương mại cố định và chuyển toàn bộ rủi ro về CFU [[src-choudhry-principles-banking#^choudhry-ftp-10]].
3. **Cung cấp dữ liệu đầu vào chuẩn xác cho bài toán Tối ưu hóa ALM**: Dữ liệu sau khi phân bổ vào các bucket chính là ma trận đầu vào trực tiếp cho mô hình quy hoạch tuyến tính tối ưu hóa bảng cân đối của ALCO nhằm tối đa hóa NII dưới đa ràng buộc LCR, NSFR, LEV và CAR [[src-ftp-transmission-analysis#^ftp-trans-13]].

## Khái niệm và Liên kết
- [[ftp-final-rate-determination]]: Xác định mức lãi suất FTP rate cuối cùng cho từng giao dịch và sản phẩm.
- [[ftp-cost-benefit-allocation-principles]]: Nguyên tắc phân bổ chi phí và lợi ích của từng FTP portfolio cho các đơn vị kinh doanh và sản phẩm.
- [[ftp-curve-construction-methodology]]: Phương pháp luận xây dựng đường cong FTP theo kỳ hạn, đồng tiền và sản phẩm.
- [[ftp-risk-and-cost-components]]: Các cấu phần rủi ro và chi phí trong định giá FTP.
- [[ftp-pricing-methodology]]: Chi tiết công thức tính toán VOF, COF và phụ phí tuân thủ ngân hàng.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn điều tiết rủi ro thanh khoản, lãi suất và tín dụng của FTP.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU qua FTP.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa quy hoạch bảng cân đối ALM toàn diện.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản theo Moorad Choudhry.
- [[synthetic-balance-sheet-liquidity-risk]]: Bảng cân đối thanh khoản tổng hợp và động lực dòng tiền.
- [[non-maturity-deposits]]: Mô hình hóa hành vi tiền gửi không kỳ hạn CASA.
- [[behavioural-options]]: Quyền chọn trả nợ trước hạn và rút tiền gửi sớm.
- [[replicating-portfolio-model]]: Mô hình danh mục sao chép phân tách Core vs Non-core CASA.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M3: đã có node [[market-risk-management]]; sổ kinh doanh (Thị trường 2) chịu hạn mức rủi ro thị trường [[src-tt83-2025-nhnn#^d35-2]] và báo cáo hằng ngày [[src-tt83-2025-nhnn#^d37-1]]; cần rà lại mục Phân bổ theo Danh mục (Trading Book).
