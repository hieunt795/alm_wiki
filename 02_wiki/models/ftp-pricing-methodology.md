---
title: "Phương Pháp Luận Định Giá Điều Chuyển Vốn Nội Bộ (FTP Pricing Methodology)"
aliases: [FTP Pricing Methodology, Phương pháp luận FTP, Cơ chế định giá VOF COF, FTP VOF COF, Định giá điều chuyển vốn ngân hàng]
type: model
domains: [alm, product]
status: active
maturity: draft
sources: ["[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]", "[[src-lubinska-alm-optimisation]]", "[[src-clip-ldr-credit-turnover-bottleneck]]"]
relations:
  - {type: priced-by, to: "[[lcr]]", cite: "[[src-vab-ftp#^vab-ftp-10]]"}
  - {type: input-to, to: "[[ftp-transmission-mechanism]]", cite: "[[src-vab-ftp#^vab-ftp-5]]"}
tags: [ftp, vof, cof, pricing-methodology, statutory-reserves, deposit-insurance, tlp, casa, embedded-options, concept]
updated: 2026-10-21
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
   - Đối với VND: lãi suất huy động tiền gửi VND thực tế bình quân 3 tháng liền kề, đã gồm chi phí huy động [[src-vab-ftp#^vab-ftp-41]]; kỳ hạn thiếu thông số thì nội suy/ngoại suy tuyến tính [[src-vab-ftp#^vab-ftp-42]].
   - Đối với USD: lãi suất tham chiếu thị trường (LIBOR/SOFR, đường cong IRS USD) bình quân 3 tháng liền kề [[src-vab-ftp#^vab-ftp-41]] [[src-vab-ftp#^vab-ftp-42]]; ngoại tệ khác theo phương pháp của USD [[src-vab-ftp#^vab-ftp-79]].
   - Minh hoạ VAB: VND 1M = 2,70%, 3M = 3,22%, 12M = 4,53%, 24M = 2,72%; USD dùng LIBOR cho kỳ ngắn và IRS từ 24M, kỳ 14D và 21D thiếu dữ liệu được gán bằng 7D (0,10%) [[src-vab-ftp#^vab-ftp-82]].
   - *Diễn giải:* trong minh hoạ, đường VND giảm từ 4,53% (12M) xuống 2,72% (24M), trong khi ví dụ TLP dùng 24M = 4,81% [[src-vab-ftp#^vab-ftp-47]]; hai bảng không nhất quán, nên chỉ coi là số minh hoạ. Gán 14D, 21D bằng 7D là ngoại suy phẳng, không phải nội suy tuyến tính như ^vab-ftp-42.
2. **Hỗ trợ huy động (Margin)**:
   - Khoản biên độ cộng thêm do ALCO quyết định nhằm điều chuyển một phần lợi nhuận từ các đơn vị sử dụng vốn sang đơn vị huy động vốn, tạo động lực cạnh tranh phát triển mạng lưới tiền gửi.
   - Theo VAB: hỗ trợ huy động là phần ALCO dùng để tạo động lực cho đơn vị huy động vốn; tính riêng cho từng loại tiền, vào đầu năm, có thể điều chỉnh bán niên hoặc hằng quý khi kế hoạch kinh doanh thay đổi; đầu vào là NII kế hoạch từ cho vay và tiền gửi (gồm trái phiếu doanh nghiệp), chi phí quản lý và chi phí dự phòng năm kế hoạch [[src-vab-ftp#^vab-ftp-80]].
   - Minh hoạ: NII vay gửi = 23,7 − (5,64 + 4,23) − 8,1 = 5,73 tỷ đồng [[src-vab-ftp#^vab-ftp-83]]. Công thức tỷ lệ NIM vay gửi và hỗ trợ huy động bị mất khi convert [cần nguồn].
3. **Điều chỉnh của ALCO cho tài sản nợ (ALCO Adjust)**:
   - Công cụ điều tiết chính sách linh hoạt: tăng mạnh cho các kỳ hạn mà ngân hàng đang thiếu hụt nguồn vốn ổn định để đáp ứng [[nsfr|NSFR]], hoặc giảm tại các kỳ hạn ngân hàng đang dư thừa thanh khoản.
   - Theo VAB: CFU cộng vào giá FTP mua vốn một mức điều chỉnh do ALCO thông qua, theo chiến lược huy động từng thời kỳ (kỳ hạn, loại tiền, khối, đối tượng khách hàng), áp cho mọi sản phẩm [[src-vab-ftp#^vab-ftp-63]].

---

### 3. Cấu Phần Biểu Giá Bán Vốn ([[cost-of-funds|COF — Cost of Funds]])

Biểu giá bán vốn áp dụng cho các tài sản sinh lời (cho vay, đầu tư) của ngân hàng [[src-vab-ftp#^vab-ftp-7]]:

$$\text{COF}(T) = \text{Base Curve}(T) + \text{Margin} + \text{Phụ phí Pháp định (DTBB + BHTG)} + \text{Liquidity Premium} + \text{TLP} + \text{ALCO Adjust}_{\text{Assets}}$$

Nguyên tắc quản trị hiện đại đòi hỏi **đơn vị sử dụng vốn phải chi trả toàn bộ chi phí vốn đầu vào, chi phí duy trì thanh khoản và các chi phí tuân thủ pháp luật mà tài sản đó gây ra cho hệ thống** [[src-vab-ftp#^vab-ftp-5]].

---

**Điều chỉnh ALCO cho tài sản có.** COF được cộng/trừ một mức điều chỉnh chung theo chiến lược cho vay từng thời kỳ (loại tiền, kỳ hạn, sản phẩm); mức này có thể khớp hoặc không khớp với điều chỉnh ALCO cho tài sản nợ, tuỳ mục tiêu chiến lược [[src-vab-ftp#^vab-ftp-64]].

**Tần suất rà soát các cấu phần (VAB Đ4.4)** [[src-vab-ftp#^vab-ftp-65]]:

| Cấu phần | Phương pháp | Tần suất rà soát | Yêu cầu | Nguồn |
|---|---|---|---|---|
| Lãi suất FTP cơ sở | Đường cong (cấu trúc kỳ hạn) | Hằng quý | Bắt buộc | [[src-vab-ftp#^vab-ftp-65]] |
| Hỗ trợ huy động | Phần bù cộng vào đường cong | Hằng năm hoặc khi kế hoạch kinh doanh thay đổi | Bắt buộc | [[src-vab-ftp#^vab-ftp-65]] |
| Chi phí BHTG | Phần bù cộng vào đường cong | Hằng quý | Bắt buộc | [[src-vab-ftp#^vab-ftp-65]] |
| Chi phí DTBB | Phần bù cộng vào đường cong | Hằng quý | Bắt buộc | [[src-vab-ftp#^vab-ftp-65]] |
| Phần bù TSTK | Phần bù cộng vào đường cong | Hằng quý | Bắt buộc | [[src-vab-ftp#^vab-ftp-65]] |
| TLP | Đường cong (cấu trúc kỳ hạn) | Hằng quý | Bắt buộc | [[src-vab-ftp#^vab-ftp-65]] |
| Điều chỉnh ALCO (nợ và có) | Phần bù cộng vào đường cong | Hằng quý | Không bắt buộc, tuỳ ALCO | [[src-vab-ftp#^vab-ftp-65]] |

---

### 4. Phương Pháp Định Lượng Chi Phí Tuân Thủ Pháp Định NHNN

#### 4.1 Chi Phí Dự Trữ Bắt Buộc (Statutory Reserved Cost)
Theo quy định của Ngân hàng Nhà nước (Thông tư 30/2019/TT-NHNN), ngân hàng thương mại bắt buộc phải duy trì một tỷ lệ dự trữ bắt buộc trên tài khoản tiền gửi tại NHNN [[src-vab-ftp#^vab-ftp-9]]:
- Số tiền gửi dự trữ này chỉ được hưởng mức lãi suất rất thấp (hoặc 0%), tạo ra khoản chênh lệch lỗ (cost of negative carry) so với chi phí huy động bình quân.
- Chi phí này được CFU tính toán và phân bổ đều vào giá bán vốn COF của tất cả các tài sản thuộc đối tượng tính FTP:

$$\text{Tỷ lệ Chi phí DTBB} = \frac{\text{Số dư DTBB bình quân 3 tháng} \times (\text{VOF bình quân} - \text{Lãi suất tiền gửi DTBB tại NHNN})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

Trong đó:
- $\text{VOF bình quân}$: Lãi suất mua vốn thực tế bình quân của tất cả các kỳ hạn trên Thị trường 1.
- $\text{Tổng tài sản bị tính FTP} = \text{Tổng tài sản} - \text{Tài sản thanh khoản} - \text{Tài sản ghi nhận cho Khối QL\&KDV} - \text{Tài sản có khác}$, lấy bình quân 3 tháng liền kề. TSTK bị loại vì đã phân bổ vào COF qua phần bù TSTK; tài sản Khối QL&KDV mua bán theo cơ chế TT2; tài sản có khác (gồm tài sản cố định) được tài trợ bằng VCSH [[src-vab-ftp#^vab-ftp-81]].
- Minh hoạ DTBB: yêu cầu DTBB bình quân 13.100,2 tỷ đồng, lãi suất DTBB "-", VOF bình quân 4,17%, bình quân tổng tài sản VND bị tính FTP 677.919,9 tỷ đồng; bảng ghi chi phí DTBB 0,00% [[src-vab-ftp#^vab-ftp-85]].
- *Diễn giải (kiểm ví dụ):* với lãi suất DTBB bằng 0, công thức cho 13.100,2 × 4,17% / 677.919,9 ≈ 0,08%, không phải 0,00%. Bảng minh hoạ có thể làm tròn sai hoặc không tính được khi ô lãi suất DTBB để "-".

#### 4.2 Chi Phí Bảo Hiểm Tiền Gửi (Deposit Insurance Cost)
Theo Luật Bảo hiểm Tiền gửi và hướng dẫn của NHNN, ngân hàng phải thanh toán phí bảo hiểm định kỳ cho tổ chức Bảo hiểm Tiền gửi Việt Nam (BHTGVN) với tỷ lệ cố định **0,15%/năm tính trên số dư tiền gửi VND của khách hàng cá nhân** [[src-vab-ftp#^vab-ftp-8]]:
- Thay vì trừ trực tiếp vào thu nhập của chi nhánh huy động (sẽ làm triệt tiêu động lực huy động tiền gửi cá nhân), chi phí này được Hội sở quy đổi và **phân bổ vào giá COF của bên sử dụng vốn**:

$$\text{Tỷ lệ Chi phí BHTG} = \frac{\text{Tổng chi phí BHTG thực tế 3 tháng quy đổi năm}}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

- Minh hoạ BHTG: tổng chi phí BHTG 3 tháng 85.424.439.251 đồng, quy đổi năm ×4 = 341.697.757.003, chia 643.285.217.739.938, ra 0,05% [[src-vab-ftp#^vab-ftp-84]].
- *Diễn giải (kiểm ví dụ):* phép chia đúng (≈ 0,053%). Mẫu số 643.285.217.739.938 là tổng tài sản ngày 31/12/2019, không phải bình quân "tài sản tính FTP" (636–695 nghìn tỷ trong bảng). Bảng dữ liệu cũng chỉ trừ tài sản TT2 và TSTK, không trừ tài sản có khác như định nghĩa [[src-vab-ftp#^vab-ftp-81]]. Kết quả vẫn làm tròn về 0,05%, nhưng ví dụ không áp đúng định nghĩa.

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
- **Quy trình 2 bước (VAB PL02)**: (1) dùng đường cong FTP cơ sở để hoàn thiện đường lãi suất giả định cho các kỳ tái định giá; (2) tính TLP cho mọi kỳ hạn bằng lãi suất kỳ hạn gốc trừ lãi suất kỳ tái định giá [[src-vab-ftp#^vab-ftp-46]].
- **Ví dụ minh hoạ (VAB, số liệu minh hoạ, %)**. Lãi suất giả định theo kỳ tái định giá [[src-vab-ftp#^vab-ftp-47]]:

| Kỳ | NM | 7D | 1M | 3M | 24M | 36M | 48M | 60M | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| Lãi suất giả định | 2.02 | 2.24 | 2.70 | 3.22 | 4.81 | 4.92 | 4.98 | 5.10 | [[src-vab-ftp#^vab-ftp-47]] |
| TLP, tái định giá NM | 0.00 | 0.22 | 0.68 | 1.20 | 2.79 | 2.90 | 2.96 | 3.08 | [[src-vab-ftp#^vab-ftp-47]] |
| TLP, tái định giá 3M | | | | 0.00 | 1.59 | 1.70 | 1.76 | 1.88 | [[src-vab-ftp#^vab-ftp-47]] |
| TLP, tái định giá 24M | | | | | 0.00 | 0.11 | 0.18 | 0.29 | [[src-vab-ftp#^vab-ftp-47]] |

  *Diễn giải (kiểm ví dụ):* mọi ô đã kiểm khớp công thức ở [[src-vab-ftp#^vab-ftp-33]], ví dụ khoản vay 60 tháng tái định giá 3 tháng: 5,10 − 3,22 = 1,88; tái định giá 24 tháng: 5,10 − 4,81 = 0,29.
- **Phần bù tài sản thanh khoản, minh hoạ**: VAB chỉ cho bảng đầu vào (số dư hằng ngày và lãi suất từng loại tài sản thanh khoản, không gồm repo, cho vay cầm cố) và công thức; kết quả để trống [[src-vab-ftp#^vab-ftp-45]].

#### 5.3 Phần Bù Rủi Ro Thanh Khoản Tiềm Tàng (cấu phần FTP đặc biệt)
VAB minh hoạ với hạn mức chưa giải ngân của thẻ tín dụng [[src-vab-ftp#^vab-ftp-48]]:

| Khoản mục | Giá trị | Nguồn |
|---|---|---|
| Hạn mức / dư nợ hiện tại | 100.000.000 / 20.000.000 | [[src-vab-ftp#^vab-ftp-48]] |
| CCF (Điều 10 TT41) | 10% | [[src-vab-ftp#^vab-ftp-48]] |
| Tỷ lệ dự trữ thanh khoản | 10% | [[src-vab-ftp#^vab-ftp-48]] |
| Chi phí duy trì tài sản thanh khoản | 1,5% (= VOF bình quân 6,5% − lợi suất 5%) | [[src-vab-ftp#^vab-ftp-48]] |
| Phần bù rủi ro thanh khoản tiềm tàng | 12.000 (= 80.000.000 × 10% × 10% × 1,5%) | [[src-vab-ftp#^vab-ftp-48]] |

**Công thức (VAB Đ5.2).** Giá FTP bán vốn cho phần hạn mức chưa sử dụng của thẻ tín dụng, thấu chi và cho vay hạn mức bằng phần bù rủi ro thanh khoản tiềm tàng [[src-vab-ftp#^vab-ftp-68]]:
- có mô hình hành vi về tỷ lệ giải ngân: phần bù = C × P% × tỷ lệ dự trữ thanh khoản × chi phí duy trì TSTK [[src-vab-ftp#^vab-ftp-69]];
- không có mô hình hành vi: phần bù = C × CCF × tỷ lệ dự trữ thanh khoản × chi phí duy trì TSTK [[src-vab-ftp#^vab-ftp-69]].

C là tổng số dư cam kết/hạn mức chưa sử dụng; tỷ lệ dự trữ thanh khoản là đệm thanh khoản thực tế; P% là tỷ lệ giải ngân trên hạn mức chưa giải ngân; CCF theo Điều 10 TT41/2016 [[src-vab-ftp#^vab-ftp-69]]. VAB dẫn văn bản BIS 12/2011 về định giá chuyển vốn rủi ro thanh khoản làm căn cứ [[src-vab-ftp#^vab-ftp-68]].

*Diễn giải (kiểm ví dụ):* ví dụ PL03 dùng nhánh không có mô hình hành vi: 80.000.000 × 10% × 10% × 1,5% = 12.000, khớp công thức. Công thức chi phí duy trì TSTK bị mất khi convert; ví dụ dùng VOF bình quân trừ lợi suất TSTK (6,5% − 5%) [[src-vab-ftp#^vab-ftp-48]]. Vì 1,5% là lãi suất năm (%/năm), 12.000 đồng là mức phí danh nghĩa quy năm (annualized fee) trong ví dụ snapshot tĩnh. Về chu kỳ tính toán và hạch toán thực tế: theo Điều 15, kỳ tính FTP vận hành hằng tháng (từ ngày 25 tháng trước đến 25 tháng này hoặc từ đầu tháng đến cuối tháng) [[src-vab-ftp#^vab-ftp-98]], tương ứng mức phân bổ tháng là 12.000 / 12 = 1.000 đồng/tháng. Đồng thời, theo Phụ lục 04, Báo cáo tổng hợp NII/NIM cấp ĐVKD được lập hằng ngày [[src-vab-ftp#^vab-ftp-99]], trong đó chi phí FTP được trích dồn hằng ngày (daily accrual) với mức tương đương 12.000 / 365 ≈ 32,88 đồng/ngày. FTP cho phần cam kết chưa sử dụng: [[src-vab-ftp#^vab-ftp-35]].

#### 5.4 Chi Phí Vốn Chủ Sở Hữu (cấu phần FTP đặc biệt)
- VCSH tài trợ các khoản mục dài hạn, không sinh lãi như tài sản cố định, đầu tư vào công ty con, công ty liên kết [[src-vab-ftp#^vab-ftp-66]].
- **Chưa áp khung RAROC**: chi phí VCSH tính trên phần thặng dư VCSH theo VOF bình quân TT1; thặng dư = VCSH trừ tài sản cố định, lãi phải thu, tài sản có khác, phí phải trả, nợ phải trả khác. Không có thặng dư thì không tính [[src-vab-ftp#^vab-ftp-66]].
- **Đã áp khung RAROC**: tính kỳ hạn hiệu lực WAT bình quân gia quyền của các khoản vay mới trong kỳ; COF của danh mục nội suy theo WAT trên biểu FTP, riêng từng loại tiền [[src-vab-ftp#^vab-ftp-67]]:

$$\text{Chi phí VCSH} = (\text{ROE}\% - \text{COF}\%) \times \text{Vốn RAROC dự kiến} \times \frac{\text{WAT}}{365}$$
[[src-vab-ftp#^vab-ftp-67]]

*Diễn giải:* nhánh RAROC đo phần lợi nhuận vượt COF mà vốn phân bổ cho đơn vị kinh doanh phải tạo ra; khác cách Choudhry gán RoE mục tiêu làm chi phí quy đổi của vốn cổ phần ([[funds-transfer-pricing]]). Công thức WAT bị mất khi convert [cần nguồn].

---

#### 5.5 Ma Trận Định Giá Theo Sản Phẩm Thị Trường 1 (VAB Điều 6)
VOF cho kỳ hạn ngoài thang chuẩn được nội suy/ngoại suy từ thang chuẩn; ALCO có thể đổi phương pháp định giá VOF cho từng sản phẩm tiền gửi [[src-vab-ftp#^vab-ftp-71]].

| Sản phẩm | Lãi suất cơ sở theo kỳ hạn nào | Hiệu lực | TLP | Nguồn |
|---|---|---|---|---|
| Tiền gửi gốc trả cuối kỳ (cố định hoặc thả nổi) | VOF theo kỳ hạn gốc, biểu tại ngày phát sinh | Cố định suốt thời gian gửi | 0 | [[src-vab-ftp#^vab-ftp-71]] |
| Tiền gửi gửi góp | Lãi suất gửi góp cùng kỳ hạn + (VOF − lãi suất huy động) của tiền gửi gốc trả cuối kỳ cùng kỳ hạn | Cố định suốt thời gian gửi | 0 | [[src-vab-ftp#^vab-ftp-72]] |
| Vostro (tiền gửi KKH của TCTD khác) | VOF cơ sở TT2 kỳ hạn ON | Cố định suốt giao dịch | 0 | [[src-vab-ftp#^vab-ftp-56]] |
| Cho vay gốc trả cuối kỳ, lãi suất cố định | COF theo kỳ hạn gốc (ngày đáo hạn − ngày giải ngân), biểu tại ngày giải ngân | Suốt thời hạn cho vay | 0 | [[src-vab-ftp#^vab-ftp-32]] |
| Cho vay gốc trả cuối kỳ, lãi suất thả nổi | COF theo kỳ tái định giá, biểu của đồng tiền và sản phẩm tại ngày giải ngân hoặc ngày điều chỉnh lãi suất | Đến ngày điều chỉnh lãi suất tiếp theo | Kỳ hạn gốc − kỳ tái định giá, áp đến ngày điều chỉnh tiếp theo | [[src-vab-ftp#^vab-ftp-86]] |
| Cho vay gốc trả định kỳ, lãi suất cố định (W.A) | COF theo kỳ hạn hiệu lực (bình quân gia quyền theo lịch trả gốc), biểu tại ngày giải ngân | Suốt thời gian cho vay | 0 | [[src-vab-ftp#^vab-ftp-73]] |
| Cho vay gốc trả định kỳ, lãi suất thả nổi | COF theo kỳ tái định giá tại ngày giải ngân hoặc ngày điều chỉnh lãi suất | Đến ngày điều chỉnh lãi suất tiếp theo | Kỳ hạn hiệu lực (bình quân gia quyền) − kỳ tái định giá | [[src-vab-ftp#^vab-ftp-87]] |
| Cho vay quá hạn | COF theo kỳ hạn của khoản vay trước khi quá hạn, trên số dư tại thời điểm quá hạn; sản phẩm ưu đãi xử lý như sản phẩm tiêu chuẩn | Cố định suốt thời gian quá hạn | Theo tính chất dòng tiền trước khi quá hạn | [[src-vab-ftp#^vab-ftp-74]] |
| Cho vay gia hạn | COF theo kỳ hạn gốc mới (gốc cũ + thời gian gia hạn) hoặc kỳ điều chỉnh lãi suất | Suốt thời gian gia hạn hoặc đến ngày điều chỉnh lãi suất tiếp theo | Theo tính chất dòng tiền | [[src-vab-ftp#^vab-ftp-75]] |
| Cho vay ưu đãi, gốc cuối kỳ, cố định — phương án 1 | Giữ kỳ hạn gốc; ví dụ 5 năm ưu đãi năm đầu: năm đầu giá 5 năm có kỳ điều chỉnh 12 tháng, 4 năm sau giá 5 năm | Theo kỳ ưu đãi / ngoài ưu đãi | 0 | [[src-vab-ftp#^vab-ftp-76]] |
| Cho vay ưu đãi, gốc cuối kỳ, cố định — phương án 2 | Tách cấu phần; ví dụ năm đầu giá 1 năm, 4 năm sau giá 4 năm | Theo từng cấu phần | 0 | [[src-vab-ftp#^vab-ftp-76]] |
| Cho vay ưu đãi, gốc cuối kỳ, thả nổi — phương án 1 | Giữ kỳ hạn gốc, đổi kỳ điều chỉnh; ví dụ 5 năm cố định năm đầu, sau thả nổi 3 tháng/lần: năm đầu giá 5 năm kỳ điều chỉnh 12 tháng, 4 năm sau giá 5 năm kỳ điều chỉnh 3 tháng | Theo kỳ ưu đãi / ngoài ưu đãi | Trong ưu đãi 0; ngoài ưu đãi: kỳ hạn gốc sau ưu đãi − kỳ tái định giá | [[src-vab-ftp#^vab-ftp-88]] |
| Cho vay ưu đãi, gốc cuối kỳ, thả nổi — phương án 2 | Tách cấu phần; năm đầu giá 1 năm, 4 năm sau giá 4 năm kỳ điều chỉnh 3 tháng; ngoài ưu đãi COF theo kỳ tái định giá tại ngày sau ngày kết thúc ưu đãi | Ngoài ưu đãi: đến ngày điều chỉnh tiếp theo | Như phương án 1 | [[src-vab-ftp#^vab-ftp-88]] |
| Cho vay ưu đãi, gốc trả định kỳ, cố định — phương án 1 | Giữ kỳ hạn hiệu lực tính theo kỳ gốc, đổi lãi suất FTP khi hết ưu đãi | Theo kỳ ưu đãi / ngoài ưu đãi | 0 | [[src-vab-ftp#^vab-ftp-89]] |
| Cho vay ưu đãi, gốc trả định kỳ, cố định — phương án 2 | Tách cấu phần; ngoài ưu đãi COF theo kỳ hạn hiệu lực sau ưu đãi (Ti đo từ ngày hết hạn ưu đãi) | Cố định từ ngày kết thúc ưu đãi đến ngày đáo hạn | 0 | [[src-vab-ftp#^vab-ftp-89]] |
| Cho vay ưu đãi, gốc trả định kỳ, thả nổi — phương án 1 | Giữ kỳ hạn hiệu lực tính theo kỳ gốc, đổi kỳ điều chỉnh (12 tháng rồi 3 tháng) | Theo kỳ ưu đãi / ngoài ưu đãi | Trong ưu đãi 0; ngoài ưu đãi: kỳ hiệu lực sau ưu đãi − kỳ tái định giá | [[src-vab-ftp#^vab-ftp-90]] |
| Cho vay ưu đãi, gốc trả định kỳ, thả nổi — phương án 2 | Tách cấu phần; 4 năm sau giá kỳ hiệu lực của 4 năm kỳ điều chỉnh 3 tháng; ngoài ưu đãi COF theo kỳ tái định giá tại ngày sau ngày kết thúc ưu đãi | Ngoài ưu đãi: đến ngày điều chỉnh tiếp theo | Như phương án 1 | [[src-vab-ftp#^vab-ftp-90]] |
| Trái phiếu doanh nghiệp giữ đến đáo hạn | Như cho vay gốc trả cuối kỳ (cố định hoặc thả nổi) | Như cho vay tương ứng | Như cho vay tương ứng | [[src-vab-ftp#^vab-ftp-77]] |
| Trái phiếu doanh nghiệp kinh doanh / AFS | COF TT1 theo kỳ hạn từ mô hình hành vi; chưa có mô hình thì theo quy tắc phân tách sổ kinh doanh TT41/2016 (thường dưới 1 năm) | Suốt thời hạn đầu tư | [cần nguồn] | [[src-vab-ftp#^vab-ftp-77]] |
| Cổ phiếu đầu tư dài hạn (chiến lược) | COF TT1 theo kỳ hạn nắm giữ dự kiến; chưa xác định thì theo kỳ nhận cổ tức hằng năm (≥ 1 năm) hoặc dải kỳ hạn trên 5 năm (≥ 5 năm) | Cố định suốt thời gian giao dịch | [cần nguồn] | [[src-vab-ftp#^vab-ftp-91]] |
| Tài sản nợ và tài sản có khác | Không tính FTP (mua bán một phần bảng cân đối), tài trợ bằng VCSH; nếu muốn tính thì bình quân lãi suất FTP theo % số dư từng thang kỳ hạn của báo cáo gap thanh khoản | — | — | [[src-vab-ftp#^vab-ftp-92]] |

#### 5.6 Thay Đổi Giá Mua Bán Vốn Trong Vòng Đời Giao Dịch (VAB Điều 8)

| Sự kiện | Căn cứ tính lại | Áp từ | Nguồn |
|---|---|---|---|
| Tiền gửi đổi tần suất xác định lãi suất | Tần suất mới; VOF cơ sở và phần bù thanh khoản tại ngày điều chỉnh | Ngày thay đổi | [[src-vab-ftp#^vab-ftp-93]] |
| Tiền gửi có kỳ hạn tái tục (TT1) | Như tiền gửi phát sinh mới, không áp mô hình hành vi, biểu mới tại thời điểm tái tục | Ngày gửi, cố định suốt thời gian gửi | [[src-vab-ftp#^vab-ftp-95]] |
| Cho vay đổi tần suất xác định lãi suất | Tần suất mới; COF cơ sở và TLP tại ngày điều chỉnh | Ngày điều chỉnh | [[src-vab-ftp#^vab-ftp-96]] |
| Cho vay trả gốc định kỳ, cố định, đổi lịch thanh toán gốc | Lịch trả nợ mới; COF cơ sở | Ngày điều chỉnh lịch | [[src-vab-ftp#^vab-ftp-96]] |
| Cho vay đổi loại hình lãi suất (cố định ↔ thả nổi) | Loại hình mới; lịch trả nợ, tần suất xác định lãi suất; COF cơ sở và TLP tại ngày thay đổi | Ngày thay đổi | [[src-vab-ftp#^vab-ftp-97]] |
| Cơ cấu lại đồng tiền nhận nợ | Chấm dứt COF trên tài khoản đồng tiền cũ, tính COF trên tài khoản đồng tiền mới | Ngày thay đổi đồng tiền | [[src-vab-ftp#^vab-ftp-97]] |
| Cho vay đổi hình thức trả gốc (một lần ↔ trả dần) | Hình thức mới; kỳ hạn gốc, lịch trả nợ; COF cơ sở và TLP | Ngày thay đổi | [[src-vab-ftp#^vab-ftp-97]] |

- Ngoài các sự kiện trên, ALCO xem xét điều chỉnh thủ công VOF hoặc COF khi có sai sót tính toán/hạch toán FTP, khi luật, quy định hoặc biến động thị trường làm giá biến động trên dưới **±0.2%** so với giá FTP hiện tại, hoặc trường hợp khác do ALCO xác định [[src-vab-ftp#^vab-ftp-94]].
- Mức biến động ±0.2% được xác định dựa trên quan sát lịch sử và phương pháp chuyên gia [[src-vab-ftp#^vab-ftp-94]].

*Diễn giải:* Điều 8 giữ nguyên tắc "khoá giá tại ngày phát sinh" của mục 5.5 nhưng mở lại giá khi cấu trúc dòng tiền hoặc kỳ tái định giá của giao dịch đổi. Ngưỡng ±0.2% là ngưỡng để ALCO mở lại giá ngoài các sự kiện đó, khác với chu kỳ rà soát hằng quý của biểu theo Đ4.4 [[src-vab-ftp#^vab-ftp-65]].

Với sản phẩm gốc trả định kỳ, TLP dùng lãi suất của kỳ hiệu lực; VAB định nghĩa kỳ hiệu lực là kỳ hạn đã chiết khấu về hiện tại của các dòng lịch trả [[src-vab-ftp#^vab-ftp-70]].

*Diễn giải:* hai chỗ trong VAB mô tả kỳ hiệu lực khác nhau. Mục TLP gọi là kỳ hạn chiết khấu về hiện tại [[src-vab-ftp#^vab-ftp-70]]; mục cho vay W.A gọi là bình quân gia quyền (thời lượng) theo gốc trả từng lần, với biến N, Pi, Ti và không nhắc chiết khấu [[src-vab-ftp#^vab-ftp-73]]. Mục cho vay thả nổi trả định kỳ cũng ghi kỳ hiệu lực theo bình quân gia quyền [[src-vab-ftp#^vab-ftp-87]]. Cả hai công thức đều mất khi convert, nên chưa xác định được VAB dùng WAL hay duration [cần nguồn: đối chiếu file docx gốc].

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
- **Thị trường 1 (biểu FTP TT1)**: Bộ phận quản lý FTP đề xuất cập nhật biểu định kỳ hằng quý hoặc khi thị trường biến động lớn [[src-vab-ftp#^vab-ftp-49]]; trình ALCO tham mưu, TGĐ phê duyệt và ban hành [[src-vab-ftp#^vab-ftp-50]]; biểu được cập nhật lên hệ thống quản lý vốn nội bộ, giao dịch mua bán vốn nội bộ được kiểm soát và lưu hồ sơ [[src-vab-ftp#^vab-ftp-51]].
- **Thị trường 2 (biểu FTP TT2)**: Bộ phận quản lý FTP tính biểu hằng ngày từ 9 giờ đến 10 giờ, theo phương pháp 1 (mid-rate của các ngân hàng TMCP tham chiếu) hoặc phương pháp 2 (VNIBOR) [[src-vab-ftp#^vab-ftp-52]]; ALCO tham mưu, TGĐ phê duyệt hằng ngày; giao dịch trước khi có biểu mới dùng biểu của ngày làm việc liền trước [[src-vab-ftp#^vab-ftp-53]]. Đầu vào là BID/OFFER của từng ngân hàng tham chiếu theo kỳ hạn ON, 7D, 14D, 21D, 1M, 2M, 3M, 6M và tiếp theo [[src-vab-ftp#^vab-ftp-54]]. Lãi suất TT2 = bình quân lãi suất chào nhận và chào gửi của 3–6 NH TMCP cùng peer [[src-vab-ftp#^vab-ftp-37]].
  - **Phương án 1 (mid-rate peer)**: tối thiểu 3 đến 6 NH TMCP cùng mức xếp hạng tín nhiệm, ưu tiên tương đương quy mô tài sản, xếp hạng, giao dịch thường xuyên với ngân hàng và chiến lược bán lẻ/bán buôn; ALCO rà soát danh sách tối thiểu 1 năm/1 lần [[src-vab-ftp#^vab-ftp-57]]. Kỳ hạn thiếu dữ liệu thì nội suy/ngoại suy; giá của một ngân hàng lệch quá ±15% so với bình quân các ngân hàng còn lại bị loại như outlier; CFU được cộng trừ một biên độ do ALCO thông qua [[src-vab-ftp#^vab-ftp-58]].
  - **Phương án 2 (VNIBOR)**: lãi suất mua bán vốn TT2 bằng VNIBOR kỳ hạn 1 tuần [[src-vab-ftp#^vab-ftp-59]].
  - **Áp cho Khối QL&KDV**: theo từng desk, lãi suất TT2 theo kỳ hạn nhu cầu cân đối vốn của desk, cố định trong thời gian giao dịch [[src-vab-ftp#^vab-ftp-60]]; hoặc theo trạng thái ròng của cả khối qua bộ phận MM, lãi suất VNIBOR 1 tuần, cần hạn mức thanh khoản 30 ngày cho trạng thái ròng của khối (chưa có thì theo dõi hằng ngày/hằng tuần chỉ số khả năng chi trả 30 ngày) [[src-vab-ftp#^vab-ftp-61]].
  - **Một lãi suất cho cả hai chiều**: nguồn gọi là "lãi suất mua bán vốn TT2" [[src-vab-ftp#^vab-ftp-37]]; Vostro (tiền gửi KKH của TCTD khác) lấy VOF cơ sở theo TT2 kỳ hạn ON, TLP = 0 [[src-vab-ftp#^vab-ftp-56]]. Nostro và tiền gửi tại NHNN không mua bán vốn FTP vì đã tính chi phí TSTK [[src-vab-ftp#^vab-ftp-55]].
  - **GTCG**: phát hành theo yêu cầu ALCO cho sổ ngân hàng (book Hội sở) thì không mua bán vốn nội bộ, khối có thể nhận phí hoa hồng tương đương "Điều chỉnh ALCO"; phát hành trên TT2 thì áp như GTCG trên TT1 [[src-vab-ftp#^vab-ftp-62]].

  *Diễn giải:* khác biểu VOF/COF thị trường 1 (cộng margin, DTBB, BHTG, phần bù TSTK, TLP [[src-vab-ftp#^vab-ftp-7]]), biểu TT2 là lãi suất liên ngân hàng cộng biên độ ALCO, không có cấu phần chi phí tuân thủ.

> [!conflict] Tần suất ban hành biểu FTP TT1
> Cùng nguồn (VAB PL05) ghi hai tần suất khác nhau.
> - Cột thời gian và bước 1: hằng quý hoặc khi có yêu cầu / biến động lớn [[src-vab-ftp#^vab-ftp-49]] [[src-vab-ftp#^vab-ftp-50]].
> - Bước 3 và 5: ban hành "Giải pháp FTP hàng tháng" [[src-vab-ftp#^vab-ftp-50]].
> - Bảng tần suất Đ4.4: lãi suất FTP cơ sở và các phần bù rà soát hằng quý [[src-vab-ftp#^vab-ftp-65]].
>
> *Diễn giải:* có thể biểu lãi suất cập nhật theo quý còn văn bản "giải pháp FTP" (gồm điều chỉnh, ngoại lệ) ban hành theo tháng; nguồn không phân biệt rõ [cần nguồn].

Nguyễn Khánh (T5, 22/9/2026) cho rằng thanh khoản phân phối ở thị trường 2 chưa tạo ra tín dụng vào nền kinh tế; thanh khoản chỉ thành tín dụng khi đi qua chuỗi tiền gửi liên ngân hàng → cho vay ngắn hạn → vốn lưu động → deposit ngắn → cho vay mới dài ở thị trường 1 [[src-clip-ldr-credit-turnover-bottleneck#^p3]]. Xem [[credit-turnover]].

*Diễn giải:* nếu mắt xích thị trường 2 → thị trường 1 nghẽn, phần nguồn vốn thị trường 1 mà CFU mua theo VOF phải đặt ở thị trường 2 hoặc chứng khoán. Biên giữa VOF đã trả và lợi suất đặt vốn đó là một chi phí FTP cần theo dõi. (ngoài wiki, chưa có nguồn)

## Khái niệm và Liên kết
- [[credit-risk-management]]: TT83/2025 Đ26.2.c yêu cầu nguyên tắc đưa chi phí bù đắp rủi ro tín dụng vào định giá sản phẩm tín dụng [[src-tt83-2025-nhnn#^d26-2c]].
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn FTP điều tiết rủi ro thanh khoản, lãi suất và tín dụng.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ qua FTP.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản tổng quát.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.
