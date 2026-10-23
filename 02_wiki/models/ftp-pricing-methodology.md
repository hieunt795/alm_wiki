---
title: "Phương Pháp Luận Định Giá Điều Chuyển Vốn Nội Bộ (FTP Pricing Methodology)"
aliases: [FTP Pricing Methodology, Phương pháp luận FTP, Cơ chế định giá VOF COF, FTP VOF COF, Định giá điều chuyển vốn ngân hàng]
type: model
domains: [alm, product]
status: active
maturity: draft
sources: ["[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]", "[[src-lubinska-alm-optimisation]]", "[[src-clip-ldr-credit-turnover-bottleneck]]", "[[src-tata-bank-alm]]"]
relations:
  - {type: input-to, to: "[[ftp-transmission-mechanism]]", cite: "[[src-vab-ftp#^vab-ftp-5]]"}
  - {type: input-to, to: "[[net-interest-margin]]", cite: "[[src-vab-ftp#^vab-ftp-40]]"}
tags: [ftp, vof, cof, pricing-methodology, statutory-reserves, deposit-insurance, tlp, casa, embedded-options, concept]
updated: 2026-10-22
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

- **Mục tiêu tài liệu (VAB).** Hướng dẫn chi tiết việc định giá điều chuyển vốn nội bộ, tuân thủ quy định của pháp luật và phù hợp tiêu chuẩn Basel [[src-vab-ftp#^vab-ftp-3]]. FTP phản ánh các rủi ro mà bộ phận FTP phải quản lý, gồm rủi ro thanh khoản và rủi ro lãi suất sổ ngân hàng [[src-vab-ftp#^vab-ftp-4]].
- **COF.** Mức lãi suất các đơn vị kinh doanh (ĐVKD) phải trả cho CFU khi CFU bán vốn để ĐVKD sử dụng cho tài sản có [[src-vab-ftp#^vab-ftp-21]].
- **VOF.** Mức lãi suất các ĐVKD được hưởng khi CFU mua tài sản nợ của ĐVKD [[src-vab-ftp#^vab-ftp-22]].
- **Định nghĩa FTP (Tata).** FTP là quy trình nội bộ gán lãi suất tài trợ cho từng vị thế bên tài sản và lãi suất sinh lời cho từng vị thế bên nợ phải trả trong sổ ngân hàng [[src-tata-bank-alm#^tata-ftp-3]]. Không được coi nguồn vốn là miễn phí khi ngân hàng dư thanh khoản, vì vi phạm nguyên tắc chi phí cơ hội; cũng không dùng một lãi suất như WACC cho mọi vị thế [[src-tata-bank-alm#^tata-ftp-4]].
- **Phân bổ thu nhập lãi (Tata).** Khối khách hàng nhận phần thu nhập từ khả năng đạt lãi suất khách hàng tốt hơn thị trường; Treasury nhận phần thu nhập từ việc đi vay hoặc đầu tư vốn theo lãi suất thị trường hiện hành [[src-tata-bank-alm#^tata-ftp-5]]. Khi tài sản và nợ khớp quy mô và kỳ hạn, ngân hàng không chịu rủi ro lãi suất nhưng NIM vẫn cần được chia giữa bộ phận huy động và cho vay, việc chia này đòi hỏi hệ thống FTP [[src-tata-bank-alm#^tata-ftp-6]].

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
   - Theo VAB, margin bù đắp chi phí quản lý của các đơn vị huy động vốn và khuyến khích hoạt động huy động của các đơn vị kinh doanh [[src-vab-ftp#^vab-ftp-25]].
   - Theo VAB: hỗ trợ huy động là phần ALCO dùng để tạo động lực cho đơn vị huy động vốn; tính riêng cho từng loại tiền, vào đầu năm, có thể điều chỉnh bán niên hoặc hằng quý khi kế hoạch kinh doanh thay đổi; đầu vào là NII kế hoạch từ cho vay và tiền gửi (gồm trái phiếu doanh nghiệp), chi phí quản lý và chi phí dự phòng năm kế hoạch [[src-vab-ftp#^vab-ftp-80]].
   - Minh hoạ: NII vay gửi = 23,7 − (5,64 + 4,23) − 8,1 = 5,73 tỷ đồng [[src-vab-ftp#^vab-ftp-83]]. Công thức tỷ lệ NIM vay gửi và hỗ trợ huy động bị mất khi convert [cần nguồn].
3. **Điều chỉnh của ALCO cho tài sản nợ (ALCO Adjust)**:
   - Công cụ ALCO điều tiết hành vi BU theo chiến lược huy động từng thời kỳ [[src-vab-ftp#^vab-ftp-63]].
   - *Diễn giải:* ALCO có thể tăng điều chỉnh ở kỳ hạn thiếu nguồn vốn ổn định (liên hệ [[nsfr|NSFR]]) hoặc giảm ở kỳ hạn dư thanh khoản; VAB không nêu ví dụ này. (ngoài wiki, chưa có nguồn)
   - Theo VAB: CFU cộng vào giá FTP mua vốn một mức điều chỉnh do ALCO thông qua, theo chiến lược huy động từng thời kỳ (kỳ hạn, loại tiền, khối, đối tượng khách hàng), áp cho mọi sản phẩm [[src-vab-ftp#^vab-ftp-63]].

---

### 2b. Base Curve Theo Đồng Tiền Và Kỳ Hạn

- **Tính riêng theo đồng tiền.** Mọi cấu phần của giá FTP được tính độc lập theo từng loại tiền, và lãi suất FTP cơ sở được tính riêng cho từng loại tiền [[src-vab-ftp#^vab-ftp-26]] [[src-vab-ftp#^vab-ftp-27]].
- **VND.** Base curve dựng từ lãi suất huy động bình quân toàn hàng của các khoản phát sinh trong 3 tháng liền kề trước thời điểm tính [[src-vab-ftp#^vab-ftp-28]].
- **USD.** Base curve dùng lãi suất tham chiếu của thị trường [[src-vab-ftp#^vab-ftp-29]]; ngoại tệ khác theo phương pháp của USD [[src-vab-ftp#^vab-ftp-79]].
- **Thang kỳ hạn.** Kỳ hạn không theo thang chuẩn của biểu ban hành được nội suy hoặc ngoại suy trực tiếp từ thang chuẩn, cho cả VOF và COF [[src-vab-ftp#^vab-ftp-30]] [[src-vab-ftp#^vab-ftp-31]].
- **Vị thế ngoại tệ khi ALM tập trung (Tata).** Thường không thực tế tạo nhiều FTP curve; có thể định giá trên curve của đồng tiền cơ sở sau điều chỉnh cross-currency lên funding spread, quan sát được trên thị trường cross-currency swap [[src-tata-bank-alm#^tata-ftp-15]].
- **Transfer price curve (Tata).** Gộp các điểm cost of funds theo kỳ hạn thành transfer price curve; theo matched maturity, mỗi vị thế nhận FTP rate ở điểm cùng kỳ hạn [[src-tata-bank-alm#^tata-ftp-8]]. Chênh lệch giữa điểm 1 năm và 2 năm trên curve là structural contribution [[src-tata-bank-alm#^tata-ftp-9]].
- Chi tiết theo từng đồng tiền, kỳ hạn và sản phẩm: [[ftp-curve-and-rate-by-tenor-currency-product]]. Công thức implied yield cho synthetic curve vẫn thiếu do lỗi convert [cần nguồn].

---

### 3. Cấu Phần Biểu Giá Bán Vốn ([[cost-of-funds|COF — Cost of Funds]])

Biểu giá bán vốn áp dụng cho các tài sản sinh lời (cho vay, đầu tư) của ngân hàng [[src-vab-ftp#^vab-ftp-7]]:

$$\text{COF}(T) = \text{Base Curve}(T) + \text{Margin} + \text{Phụ phí Pháp định (DTBB + BHTG)} + \text{Liquidity Premium} + \text{TLP} + \text{ALCO Adjust}_{\text{Assets}}$$

VAB yêu cầu lãi suất FTP phải phản ánh đầy đủ chi phí vốn đầu vào (lãi suất huy động, chi phí bảo hiểm tiền gửi, chi phí quản lý huy động), chi phí quản lý rủi ro thanh khoản và rủi ro lãi suất [[src-vab-ftp#^vab-ftp-5]].

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

### 3b. Tách FTP Thành Pure Interest Rate Risk Curve Và Funding Spread (Tata)

- FTP curve bù đắp cho Treasury cả rủi ro lãi suất lẫn rủi ro thanh khoản, nên tách thành pure interest rate risk curve cộng funding spread [[src-tata-bank-alm#^tata-ftp-10]].
- Repo là một nguồn cho curve phi rủi ro nhưng thị trường repo thường chỉ thanh khoản đến 1–2 năm [[src-tata-bank-alm#^tata-ftp-11]]; swap EURIBOR kéo dài đến 30 năm nhưng phản ánh rủi ro đối tác liên ngân hàng [[src-tata-bank-alm#^tata-ftp-12]].
- Funding spread đặc thù theo tài sản; thực tế dùng một FTP curve với spread bình quân rồi điều chỉnh theo trường hợp. Ví dụ: note cố định 2 năm 3% và note thả nổi 2 năm 2,2% cho funding spread 2 năm là 80 bp [[src-tata-bank-alm#^tata-ftp-13]].
- Cách tách cho phép định giá sản phẩm có kỳ hạn chỉ số lãi suất tái định giá khác kỳ hạn hợp đồng; ví dụ khoản vay 2 năm tái định giá sau 1 năm có FTP rate = 1,6% + 80 bp = 2,4% [[src-tata-bank-alm#^tata-ftp-14]].
- *Diễn giải:* cách tách của Tata và TLP của VAB (mục 5.2) cùng tách kỳ tái định giá khỏi kỳ hạn hợp đồng. VAB tính TLP bằng chênh lệch lãi suất giữa hai điểm kỳ hạn của base curve [[src-vab-ftp#^vab-ftp-33]]; Tata tính funding spread từ lãi suất phát hành của ngân hàng. Hai cách tính không đồng nhất.

---

### 4. Phương Pháp Định Lượng Chi Phí Tuân Thủ Pháp Định NHNN

#### 4.1 Chi Phí Dự Trữ Bắt Buộc (Statutory Reserved Cost)
Theo VAB, NHNN yêu cầu các ngân hàng phải nắm giữ tỷ lệ phần trăm tiền gửi nhất định làm dự trữ tại NHNN [[src-vab-ftp#^vab-ftp-9]]. VAB dẫn TT30/2019 là văn bản liên quan [[src-vab-ftp#^vab-ftp-78]]:
- *Diễn giải:* khi lãi suất tiền gửi DTBB tại NHNN thấp hơn VOF bình quân, công thức dưới đây cho giá trị dương, tức chi phí cơ hội (negative carry) của khoản dự trữ.
- Chi phí DTBB được phân bổ vào giá COF [[src-vab-ftp#^vab-ftp-7]]:

$$\text{Tỷ lệ Chi phí DTBB} = \frac{\text{Số dư DTBB bình quân 3 tháng} \times (\text{VOF bình quân} - \text{Lãi suất tiền gửi DTBB tại NHNN})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

Trong đó:
- $\text{VOF bình quân}$: Lãi suất mua vốn thực tế bình quân của tất cả các kỳ hạn trên Thị trường 1.
- $\text{Tổng tài sản bị tính FTP} = \text{Tổng tài sản} - \text{Tài sản thanh khoản} - \text{Tài sản ghi nhận cho Khối QL\&KDV} - \text{Tài sản có khác}$, lấy bình quân 3 tháng liền kề. TSTK bị loại vì đã phân bổ vào COF qua phần bù TSTK; tài sản Khối QL&KDV mua bán theo cơ chế TT2; tài sản có khác (gồm tài sản cố định) được tài trợ bằng VCSH [[src-vab-ftp#^vab-ftp-81]].
- Minh hoạ DTBB: yêu cầu DTBB bình quân 13.100,2 tỷ đồng, lãi suất DTBB "-", VOF bình quân 4,17%, bình quân tổng tài sản VND bị tính FTP 677.919,9 tỷ đồng; bảng ghi chi phí DTBB 0,00% [[src-vab-ftp#^vab-ftp-85]].
- *Diễn giải (kiểm ví dụ):* với lãi suất DTBB bằng 0, công thức cho 13.100,2 × 4,17% / 677.919,9 ≈ 0,08%, không phải 0,00%. Bảng minh hoạ có thể làm tròn sai hoặc không tính được khi ô lãi suất DTBB để "-".

#### 4.2 Chi Phí Bảo Hiểm Tiền Gửi (Deposit Insurance Cost)
Theo VAB, ngân hàng phải thanh toán phí cho tổ chức bảo hiểm tiền gửi theo quy định của NHNN, "hiện tại" là **0,15%/năm tính trên số dư tiền gửi VND của khách hàng cá nhân** (VAB không ghi ngày của mốc này) [[src-vab-ftp#^vab-ftp-8]]:
- Chi phí này được Hội sở quy đổi và **phân bổ vào giá COF của bên sử dụng vốn** [[src-vab-ftp#^vab-ftp-7]]:

$$\text{Tỷ lệ Chi phí BHTG} = \frac{\text{Tổng chi phí BHTG thực tế 3 tháng quy đổi năm}}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

- Minh hoạ BHTG: tổng chi phí BHTG 3 tháng 85.424.439.251 đồng, quy đổi năm ×4 = 341.697.757.003, chia 643.285.217.739.938, ra 0,05% [[src-vab-ftp#^vab-ftp-84]].
- *Diễn giải (kiểm ví dụ):* phép chia đúng (≈ 0,053%). Mẫu số 643.285.217.739.938 là tổng tài sản ngày 31/12/2019, không phải bình quân "tài sản tính FTP" (636–695 nghìn tỷ trong bảng). Bảng dữ liệu cũng chỉ trừ tài sản TT2 và TSTK, không trừ tài sản có khác như định nghĩa [[src-vab-ftp#^vab-ftp-81]]. Kết quả vẫn làm tròn về 0,05%, nhưng ví dụ không áp đúng định nghĩa.

---

### 5. Phần Bù Tài Sản Thanh Khoản và Phần Bù Thanh Khoản Kỳ Hạn (TLP)

#### 5.1 Phần Bù cho Tài Sản Thanh Khoản (Liquidity Buffer Premium)
Theo VAB, phần bù cho tài sản thanh khoản thể hiện chi phí duy trì danh mục tài sản thanh khoản đáp ứng yêu cầu theo TT22/2019/TT-NHNN, quy định nội bộ và/hoặc yêu cầu luật định [[src-vab-ftp#^vab-ftp-10]]. Danh mục TSTK theo Phụ lục 3 TT22/2019 [[src-vab-ftp#^vab-ftp-43]].
- *Diễn giải:* khi lợi suất bình quân của danh mục TSTK thấp hơn VOF bình quân, công thức dưới đây cho giá trị dương (negative carry).
- Phần bù được phân bổ vào biểu giá COF [[src-vab-ftp#^vab-ftp-7]]; công thức không có biến kỳ hạn:

$$\text{Liquidity Premium} = \frac{\text{Số dư bình quân TSTK} \times (\text{VOF bình quân} - \text{Lãi suất bình quân danh mục TSTK})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

#### 5.2 Phần Bù Thanh Khoản Kỳ Hạn (Term Liquidity Premium — TLP)
Phần bù thanh khoản kỳ hạn là cấu phần đặc thù **chỉ áp dụng cho các khoản vay có lãi suất thả nổi** [[src-vab-ftp#^vab-ftp-11]] [[src-vab-ftp#^vab-ftp-12]]:

- **Vấn đề bản chất**: TLP phản ánh chi phí thanh khoản dài hạn và là phần bù cấu trúc cộng vào lãi suất cơ sở [[src-vab-ftp#^vab-ftp-23]]. *Diễn giải:* khoản vay 5 năm thả nổi 3 tháng một lần chỉ nhận COF cơ sở theo kỳ 3 tháng; không có TLP thì chi phí thanh khoản của 5 năm không được tính vào giá.
- **Công thức tính TLP**:
  $$\text{TLP} = \text{Lãi suất FTP cơ sở kỳ hạn gốc (5 năm)} - \text{Lãi suất FTP cơ sở kỳ hạn tái định giá (3 tháng)}$$
- *Diễn giải:* theo công thức TLP, FTP cơ sở kỳ tái định giá cộng TLP bằng FTP cơ sở kỳ hạn gốc, tức bằng COF cơ sở của khoản vay cố định cùng kỳ hạn gốc.
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

Với sản phẩm gốc trả định kỳ, TLP dùng lãi suất của kỳ hiệu lực; VAB định nghĩa kỳ hiệu lực là kỳ hạn đã chiết khấu về hiện tại của các dòng lịch trả [[src-vab-ftp#^vab-ftp-70]]. Công thức TLP cho sản phẩm này là lãi suất của kỳ hạn hiệu lực trừ lãi suất của kỳ hạn tái định lại lãi suất [[src-vab-ftp#^vab-ftp-34]].

*Diễn giải:* hai chỗ trong VAB mô tả kỳ hiệu lực khác nhau. Mục TLP gọi là kỳ hạn chiết khấu về hiện tại [[src-vab-ftp#^vab-ftp-70]]; mục cho vay W.A gọi là bình quân gia quyền (thời lượng) theo gốc trả từng lần, với biến N, Pi, Ti và không nhắc chiết khấu [[src-vab-ftp#^vab-ftp-73]]. Mục cho vay thả nổi trả định kỳ cũng ghi kỳ hiệu lực theo bình quân gia quyền [[src-vab-ftp#^vab-ftp-87]]. Cả hai công thức đều mất khi convert, nên chưa xác định được VAB dùng WAL hay duration [cần nguồn: đối chiếu file docx gốc].

## Inputs & giả định

### 6. Mô Hình Hóa Sản Phẩm Phi Kỳ Hạn — Đường Cong Hoàn Trả Tiền Gửi CASA (Non-term Redemption Curve)

VAB áp dụng cách định giá này cho sản phẩm tiền gửi của khách hàng không có kỳ hạn (CASA) [[src-vab-ftp#^vab-ftp-13]].

VAB tách CASA thành phần không ổn định (non-core) và phần ổn định (core). Giá VOF xác định theo giá bình quân gia quyền của các thang kỳ hạn tương ứng với tỷ lệ dòng tiền ổn định và không ổn định [[src-vab-ftp#^vab-ftp-14]].

VietABank áp dụng phương pháp **Đường cong hoàn trả (Redemption Curve)** để xác định giá mua vốn VOF cơ sở thông qua danh mục sao chép (replicating portfolio) [[src-vab-ftp#^vab-ftp-14]]:

$$\text{Base Curve}_{\text{CASA}} = \text{Base Curve}_i \times \text{Non-CoreCasa}_i + \text{Base Curve}_j \times (1 - \text{Non-CoreCasa}_i)$$
[[src-vab-ftp#^vab-ftp-15]]

Trong đó:
- $\text{Non-CoreCasa}_i$: Tỷ lệ tiền gửi CASA không ổn định của thang kỳ hạn $i$, xác định theo kết quả tính toán định kỳ của mô hình hành vi tại thời điểm liền kề gần nhất [[src-vab-ftp#^vab-ftp-15]].
- $\text{Base Curve}_i$: Lãi suất FTP cơ sở của thang kỳ hạn $i$ [[src-vab-ftp#^vab-ftp-15]].
- $\text{Base Curve}_j$: Lãi suất FTP cơ sở của thang kỳ hạn $j$ [[src-vab-ftp#^vab-ftp-15]]. VAB không nêu giá trị $i$, $j$ cụ thể trong claim đã ingest. [cần nguồn]

Khi chưa áp dụng mô hình hành vi, phần tiền gửi không kỳ hạn có khả năng bị rút không thấp hơn 15% số dư bình quân 30 ngày liền kề theo quy định NHNN [[src-vab-ftp#^vab-ftp-16]]. Trong công thức, $a\%$ là tỷ lệ rút ra, không nhỏ hơn 15%, và $\text{VOF}_{\text{CKH}}$ là VOF kỳ hạn 2 tháng hoặc theo ALCO phê duyệt trong từng thời kỳ [[src-vab-ftp#^vab-ftp-44]]:

$$\text{VOF} = \text{VOF}_{\text{KKH}} \times a\% + \text{VOF}_{\text{CKH}} \times (1 - a\%)$$


---

### 7. Định Giá Sản Phẩm Chứa Quyền Chọn Ẩn (Embedded Options Pricing)

VAB có mục giá mua bán vốn áp dụng cho các sản phẩm có quyền chọn ẩn (embedded options) [[src-vab-ftp#^vab-ftp-17]]:

#### 7.1 Quyền Chọn Trả Nợ Trước Hạn Khoản Vay (Prepayment Option)
Với khoản vay trả trước hạn:
- Áp dụng mô hình hành vi trả trước hạn (prepayment behavior model) để ước lượng dòng tiền thực tế và tính toán lại **kỳ hạn hiệu lực bình quân gia quyền (Weighted Average Life — WAL)** của khoản vay thay vì kỳ hạn pháp lý trên hợp đồng [[src-vab-ftp#^vab-ftp-19]] [[src-vab-ftp#^vab-ftp-20]]:
  $$\text{Kỳ hạn hiệu lực} = \frac{\sum_{i=1}^N P_i \times T_i}{\sum_{i=1}^N P_i}$$
- COF cơ sở được xác định theo kỳ hạn hiệu lực tính từ dòng tiền của mô hình hành vi trả trước hạn đối với từng khoản vay [[src-vab-ftp#^vab-ftp-19]].

#### 7.2 Rút Tiền Gửi Có Kỳ Hạn Trước Ngày Đáo Hạn (Early Redemption)
- VAB áp dụng chi phí phạt rút trước hạn: VOF cơ sở xác định dựa trên VOF tương ứng tiền gửi không kỳ hạn thông thường [[src-vab-ftp#^vab-ftp-18]].
- Căn cứ pháp lý của quyền rút trước hạn (Thông tư 04/2022/TT-NHNN) chưa có source note trong wiki. [cần nguồn]

#### 7.3 Phương Pháp FTP Behaviouralisation & Chi Phí Thanh Khoản Dự Phòng (Beata Lubinska)
Theo Beata Lubinska, FTP behaviouralisation là phương pháp luận nhằm nắm bắt đầy đủ rủi ro lãi suất hành vi và chi phí/giá trị thanh khoản hành vi của sản phẩm [[src-lubinska-alm-optimisation#^lubinska-u04-2]]:
- **Tách hồ sơ lãi suất CASA**: Hồ sơ lãi suất CASA luôn bao gồm hai cấu phần: phần biến động được mô hình hóa tái định giá trên cơ sở qua đêm (O/N) theo chuẩn BCBS d368, và phần ổn định được coi là nhạy cảm theo thị trường hoặc phần lõi phi nhạy cảm lãi suất đóng vai trò nguồn tài trợ dài hạn lãi suất 0% [[src-lubinska-alm-optimisation#^lubinska-u04-1]].
- **Phân bổ chi phí thanh khoản dự phòng (Contingent Liquidity Cost)**: Nắm giữ đệm thanh khoản bảo vệ ngân hàng trước dòng tiền rút bất ngờ trong kịch bản căng thẳng tốn kém, vì chi phí tài trợ cho đệm thường vượt lợi suất sinh ra [[src-lubinska-alm-optimisation#^lubinska-u04-3]]. Chi phí thanh khoản dự phòng này phải được phân bổ ngược lại cho mảng kinh doanh [[src-lubinska-alm-optimisation#^lubinska-u04-3]]. Nếu chi phí tài trợ bị ước lượng thấp, BU cho vay rẻ hơn và tăng khối lượng nguồn vốn vì tưởng có lãi [[src-lubinska-alm-optimisation#^lubinska-u04-2]].

#### 7.4 Quan điểm của Tata về optionality trong FTP
- Tata (T4) nêu FTP rate nên được điều chỉnh theo optionality: mark-up cho short optionality (khách hàng có quyền, như trả nợ trước hạn), discount cho long optionality [[src-tata-bank-alm#^tata-ftp-27]]. Treasury có thể phải mua quyền chọn để bù short optionality, nhưng embedded options dựa trên giả định hành vi khó định giá bằng mô hình chuẩn [[src-tata-bank-alm#^tata-ftp-28]].
- *Diễn giải:* VAB xử lý prepayment và rút trước hạn bằng kỳ hạn hiệu lực và chi phí phạt (mục 7.1, 7.2), các claim VAB đã ingest không nêu premium. Tata nêu hướng mark-up/discount nhưng không đưa công thức; hai cách tiếp cận khác nhau về hình thức, chưa đủ cơ sở gọi là conflict.

---

## Output & usage

### 8. Phân Tách Giữa Thị Trường 1 và Thị Trường 2

Hệ thống FTP thiết lập ranh giới rõ ràng giữa hai thị trường:
- **Thị trường 1 (biểu FTP TT1)**: Bộ phận quản lý FTP đề xuất cập nhật biểu định kỳ hằng quý hoặc khi thị trường biến động lớn [[src-vab-ftp#^vab-ftp-49]]; trình ALCO tham mưu, TGĐ phê duyệt và ban hành [[src-vab-ftp#^vab-ftp-50]]; biểu được cập nhật lên hệ thống quản lý vốn nội bộ, giao dịch mua bán vốn nội bộ được kiểm soát và lưu hồ sơ [[src-vab-ftp#^vab-ftp-51]].
- **Thị trường 2 (biểu FTP TT2)**: Bộ phận quản lý FTP tính biểu hằng ngày từ 9 giờ đến 10 giờ, theo phương pháp 1 (mid-rate của các ngân hàng TMCP tham chiếu) hoặc phương pháp 2 (VNIBOR) [[src-vab-ftp#^vab-ftp-52]]; ALCO tham mưu, TGĐ phê duyệt hằng ngày; giao dịch trước khi có biểu mới dùng biểu của ngày làm việc liền trước [[src-vab-ftp#^vab-ftp-53]]. Đầu vào là BID/OFFER của từng ngân hàng tham chiếu theo kỳ hạn ON, 7D, 14D, 21D, 1M, 2M, 3M, 6M và tiếp theo [[src-vab-ftp#^vab-ftp-54]]. Lãi suất TT2 = bình quân lãi suất chào nhận và chào gửi của 3–6 NH TMCP cùng peer [[src-vab-ftp#^vab-ftp-37]].
  - **Phương án 1 (mid-rate peer)**: tối thiểu 3 đến 6 NH TMCP cùng mức xếp hạng tín nhiệm, ưu tiên tương đương quy mô tài sản, xếp hạng, giao dịch thường xuyên với ngân hàng và chiến lược bán lẻ/bán buôn; ALCO rà soát danh sách tối thiểu 1 năm/1 lần [[src-vab-ftp#^vab-ftp-57]]. Kỳ hạn thiếu dữ liệu thì nội suy/ngoại suy; giá của một ngân hàng lệch quá ±15% so với bình quân các ngân hàng còn lại bị loại như outlier; CFU được cộng trừ một biên độ do ALCO thông qua [[src-vab-ftp#^vab-ftp-58]].
  - Lãi suất FTP cơ sở mua bán vốn TT2 được thiết lập theo một trong hai phương án này [[src-vab-ftp#^vab-ftp-36]].
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

#### 8.1 Đo Lường NII Và NIM Theo FTP (VAB)

- Báo cáo tổng hợp NII đánh giá hiệu quả hoạt động của toàn bộ ĐVKD và các sản phẩm, xác định sản phẩm và ĐVKD kém hiệu quả [[src-vab-ftp#^vab-ftp-38]].
- Với từng sản phẩm, khách hàng hoặc ĐVKD, NII xác định bằng thu nhập lãi (thu nhập lãi cho vay hoặc thu nhập FTP) so với chi phí lãi [[src-vab-ftp#^vab-ftp-39]].
- NIM trong tài liệu VAB là chênh lệch giữa lãi suất cho vay và giá FTP bán vốn đối với tài sản, và giữa giá FTP mua vốn và lãi suất huy động đối với nợ phải trả [[src-vab-ftp#^vab-ftp-40]]. Phạm vi là NIM theo sản phẩm; xem [[net-interest-margin]].
- Báo cáo NII/NIM cấp ĐVKD và cụm chi nhánh lập hằng ngày cho mọi loại tiền [[src-vab-ftp#^vab-ftp-99]].

#### 8.2 Chức Năng Steering (Tata)

- Ngoài phân bổ NIM và tập trung rủi ro lãi suất, thanh khoản về Treasury, FTP dùng để steer hoạt động khách hàng và cấu trúc bảng cân đối. Ngân hàng dư tiền gửi và thiếu khoản vay có thể dịch FTP curve xuống, giảm đóng góp của khối tiền gửi và tăng đóng góp của khối cho vay [[src-tata-bank-alm#^tata-ftp-16]].
- Tata nhận định chức năng này mang tính chính trị cao vì FTP là nguồn sự thật duy nhất về giá trị gia tăng cảm nhận được của các khối kinh doanh [[src-tata-bank-alm#^tata-ftp-17]].
- Schäfer et al. (trích bởi Tata): một phần đáng kể NII chủ yếu do mô hình nội bộ định giá chi phí tài trợ chi phối chứ không do biên khách hàng; đổi giả định kỳ hạn hành vi của tiền gửi không kỳ hạn doanh nghiệp làm lệch NII mà quan hệ kinh doanh bên ngoài không đổi [[src-tata-bank-alm#^tata-ftp-18]].

## Khái niệm và Liên kết
- [[funds-transfer-pricing]]: Khái niệm FTP và nguyên tắc matched-maturity.
- [[internal-funding-curve]]: Cách dựng đường cong vốn nội bộ.
- [[net-interest-margin]]: NIM; VAB tính NIM theo sản phẩm với giá FTP.
- [[ftp-curve-and-rate-by-tenor-currency-product]]: Synthesis cách dựng FTP curve và gán FTP rate.
- [[credit-risk-management]]: TT83/2025 Đ26.2.c yêu cầu nguyên tắc đưa chi phí bù đắp rủi ro tín dụng vào định giá sản phẩm tín dụng [[src-tt83-2025-nhnn#^d26-2c]].
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn FTP điều tiết rủi ro thanh khoản, lãi suất và tín dụng.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ qua FTP.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản tổng quát.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.
