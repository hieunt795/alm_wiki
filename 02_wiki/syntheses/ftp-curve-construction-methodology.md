---
title: "Phương Pháp Luận Xây Dựng Đường Cong FTP (FTP Curve) Theo Kỳ Hạn, Đồng Tiền Và Loại Sản Phẩm"
aliases: [FTP Curve Construction Methodology, Xây dựng đường cong FTP, Phương pháp lập đường cong FTP, FTP Curve Tenor Currency Product, FTP Rate Construction]
type: synthesis
domains: [alm, product]
status: active
maturity: draft
origin: research
question: "Q1 Đường cong FTP dựng theo cách tiếp cận nào, gồm cấu phần gì? · Q2 Thang kỳ hạn chuẩn và nội suy/ngoại suy kỳ hạn lẻ? · Q3 Base curve VND, USD, ngoại tệ khác lấy từ đâu? · Q4 Phụ phí pháp định theo đồng tiền (DTBB, BHTG, trần lãi suất)? · Q5 FX swap/CIP có vào đường cong ngoại tệ không? · Q6 VOF/COF theo từng loại sản phẩm (cuối kỳ, định kỳ, cố định/thả nổi, KKH, thấu chi, ưu đãi, quá hạn, gia hạn, TPDN)? · Q7 Cam kết ngoại bảng (contingent premium)? · Q8 TT1 vs TT2 khác nhau thế nào? · Q9 Chu kỳ rà soát, ban hành, phê duyệt?"
as_of: 2026-10-21
sources: ["[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-tt50-2026-nhnn]]"]
relations: []
tags: [ftp, ftp-curve, tenor-structure, multi-currency, product-pricing, interpolation, tlp, synthesis]
updated: 2026-10-21
reviewed:
---

## Câu hỏi

Câu gốc (query 2026-10-20): "FTP curve/FTP rate được xây dựng như thế nào cho từng kỳ hạn, đồng tiền và loại sản phẩm?" Research 2026-10-21 tách thành 9 câu:

- Q1. Đường cong FTP dựng theo cách tiếp cận nào, gồm cấu phần gì?
- Q2. Thang kỳ hạn chuẩn và nội suy/ngoại suy kỳ hạn lẻ?
- Q3. Base curve VND, USD, ngoại tệ khác lấy từ đâu?
- Q4. Phụ phí pháp định theo đồng tiền (DTBB, BHTG, trần lãi suất)?
- Q5. FX swap/CIP có vào đường cong ngoại tệ không?
- Q6. VOF/COF theo từng loại sản phẩm (cuối kỳ, định kỳ, cố định/thả nổi, KKH, thấu chi, ưu đãi, quá hạn, gia hạn, TPDN)?
- Q7. Cam kết ngoại bảng (contingent premium)?
- Q8. TT1 vs TT2 khác nhau thế nào?
- Q9. Chu kỳ rà soát, ban hành, phê duyệt?

Node chính: [[internal-funding-curve]] (Choudhry), [[ftp-pricing-methodology]] (VAB), [[funds-transfer-pricing]], [[liquidity-transfer-pricing]], [[liquidity-cost-risk]], [[non-maturity-deposits]], [[alm-operating-model]]. Mọi node này đang `draft`, chưa review. Nguồn VN duy nhất về phương pháp là tài liệu nội bộ VAB (T4); wiki chưa có quy định NHNN riêng về FTP.

## Kết luận

- **Q1.** Choudhry phân bốn cách dựng đường cong FTP: cost, market, mixed và marginal [[src-choudhry-principles-banking#^choudhry-ifc-16]]. VAB dựng đường cong từ lãi suất FTP cơ sở theo cấu trúc kỳ hạn, cộng các phần bù: hỗ trợ huy động, chi phí BHTG, chi phí DTBB, phần bù tài sản thanh khoản, TLP và điều chỉnh ALCO [[src-vab-ftp#^vab-ftp-65]]. VOF và COF dùng chung base curve nhưng COF mang thêm các phần bù chi phí [[src-vab-ftp#^vab-ftp-6]] [[src-vab-ftp#^vab-ftp-7]].
- **Q2.** VAB ban hành biểu theo thang kỳ hạn chuẩn; kỳ hạn lẻ được nội suy/ngoại suy trực tiếp từ thang chuẩn [[src-vab-ftp#^vab-ftp-30]] [[src-vab-ftp#^vab-ftp-31]]. Với VND, nội suy/ngoại suy là tuyến tính, làm bằng Excel [[src-vab-ftp#^vab-ftp-42]]. Biểu minh hoạ của VAB đi từ NM đến 60M [[src-vab-ftp#^vab-ftp-82]]. Nguồn đã ingest không ghi thang tới 10 năm hay dùng cubic spline cho FTP curve.
- **Q3.** Base curve VND lấy lãi suất huy động tiền gửi VND thực tế bình quân 3 tháng liền kề, đã gồm chi phí huy động [[src-vab-ftp#^vab-ftp-41]]. USD dùng lãi suất tham chiếu thị trường (LIBOR/SIBOR hoặc SOFR, đường cong IRS USD), lấy bình quân 3 tháng trên từng kỳ hạn [[src-vab-ftp#^vab-ftp-41]] [[src-vab-ftp#^vab-ftp-42]]. Ngoại tệ khác theo phương pháp của USD [[src-vab-ftp#^vab-ftp-79]].
- **Q4.** VAB tính mọi cấu phần độc lập theo loại tiền [[src-vab-ftp#^vab-ftp-26]]. Chi phí BHTG và DTBB được chia trên bình quân tổng tài sản bị tính FTP [[src-vab-ftp#^vab-ftp-81]] [[src-vab-ftp#^vab-ftp-84]] [[src-vab-ftp#^vab-ftp-85]]. Mức BHTG VAB ghi là 0.15%/năm trên tiền gửi VND của KHCN [[src-vab-ftp#^vab-ftp-8]]. Tỷ lệ DTBB theo đồng tiền, lãi suất DTBB và trần lãi suất huy động USD: [cần nguồn], vì wiki chưa có TT30/2019 hay văn bản trần lãi suất.
- **Q5.** VAB không dùng FX swap hay CIP để dựng đường cong USD; USD có đường cong riêng từ lãi suất tham chiếu USD [[src-vab-ftp#^vab-ftp-41]]. Choudhry đề xuất synthetic curve từ implied yield và FX forward cho thị trường mới nổi thiếu swap và trái phiếu dài hạn [[src-choudhry-principles-banking#^choudhry-ifc-13]]. Công thức CIP: [cần nguồn].
- **Q6.** VAB định giá theo tính chất dòng tiền: kỳ hạn gốc cho sản phẩm trả cuối kỳ, kỳ hạn hiệu lực cho sản phẩm trả định kỳ, TLP chỉ cho lãi suất thả nổi [[src-vab-ftp#^vab-ftp-12]] [[src-vab-ftp#^vab-ftp-32]] [[src-vab-ftp#^vab-ftp-73]]. Tiền gửi KKH dùng redemption curve, hoặc tỷ lệ rút tối thiểu 15% khi chưa có mô hình hành vi [[src-vab-ftp#^vab-ftp-14]] [[src-vab-ftp#^vab-ftp-44]]. Chi tiết theo sản phẩm ở bảng Q6.
- **Q7.** Phần hạn mức chưa dùng của thẻ tín dụng, thấu chi và cho vay hạn mức nhận giá FTP bán vốn bằng phần bù rủi ro thanh khoản tiềm tàng [[src-vab-ftp#^vab-ftp-68]]. Phần bù bằng C × P% (hoặc CCF) × tỷ lệ dự trữ thanh khoản × chi phí duy trì TSTK [[src-vab-ftp#^vab-ftp-69]].
- **Q8.** Quy định VAB áp cho mọi giao dịch điều chuyển vốn giữa Hội sở và đơn vị kinh doanh, cả TT1 lẫn TT2 [[src-vab-ftp#^vab-ftp-78]]. Biểu TT1 cập nhật hằng quý [[src-vab-ftp#^vab-ftp-49]]. TT2 (giao dịch liên ngân hàng của Khối QL&KDV) dùng biểu tính hằng ngày từ 9 giờ đến 10 giờ, theo mid-rate 3–6 ngân hàng peer hoặc VNIBOR 1 tuần [[src-vab-ftp#^vab-ftp-52]] [[src-vab-ftp#^vab-ftp-57]] [[src-vab-ftp#^vab-ftp-59]].
- **Q9.** Lãi suất FTP cơ sở và các phần bù rà soát hằng quý; hỗ trợ huy động rà soát hằng năm hoặc khi kế hoạch kinh doanh đổi [[src-vab-ftp#^vab-ftp-65]]. Biểu TT1 do ALCO tham mưu, TGĐ phê duyệt [[src-vab-ftp#^vab-ftp-50]]. Nguồn VAB tự mâu thuẫn về tần suất ban hành biểu TT1 (hằng quý vs "hàng tháng"), xem mục Bằng chứng trái chiều.

## Cơ chế

### Q1 — Cách tiếp cận và cấu phần

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[internal-funding-curve]] | input-to | [[funds-transfer-pricing]] | — | [[src-choudhry-principles-banking#^choudhry-ifc-9]] |
| [[cost-of-funds]] | part-of | [[funds-transfer-pricing]] | — | [[src-vab-ftp#^vab-ftp-7]] |
| [[liquidity-transfer-pricing]] | part-of | [[funds-transfer-pricing]] | — | [[src-choudhry-principles-banking#^choudhry-ftp-14]] |
| [[liquidity-transfer-pricing]] | input-to | [[ftp-pricing-methodology]] | — | [[src-vab-ftp#^vab-ftp-5]] |
| [[cost-of-funds]] | input-to | [[loan-pricing]] | — | [[src-choudhry-principles-banking#^choudhry-strat-16]] |

**Bốn cách dựng (Choudhry).** Chi tiết ưu, nhược điểm ở [[internal-funding-curve]].

| Cách | Cấu tạo | Nguồn |
|---|---|---|
| Cost | Lãi suất huy động đã trả | [[src-choudhry-principles-banking#^choudhry-ifc-17]] |
| Market | Lãi suất đặt vốn hoặc vay thay thế trên thị trường | [[src-choudhry-principles-banking#^choudhry-ifc-18]] |
| Mixed | Market curve trộn với chi phí thực tế của nợ theo tỷ trọng nguồn ổn định từng bucket | [[src-choudhry-principles-banking#^choudhry-ifc-19]] |
| Marginal | Chi phí vốn ngắn hạn thị trường + spread riêng phản ánh chi phí thanh khoản theo kỳ hạn | [[src-choudhry-principles-banking#^choudhry-ifc-20]] |

Choudhry khuyến nghị rút đường cong từ giá thị trường theo no-arbitrage: nội suy trên lợi suất nợ đã phát hành của chính ngân hàng, rồi lấy par-par asset swap curve làm TLP curve [[src-choudhry-principles-banking#^choudhry-ifc-3]] [[src-choudhry-principles-banking#^choudhry-ifc-4]]. Cách này cần trái phiếu ngân hàng có thị trường thứ cấp thanh khoản [[src-choudhry-principles-banking#^choudhry-ifc-3]].

**Bảy cấu phần (VAB Đ4.4).**

| Cấu phần | Phương pháp | Tần suất rà soát | Bắt buộc | Nguồn |
|---|---|---|---|---|
| Lãi suất FTP cơ sở | Đường cong (cấu trúc kỳ hạn) | Hàng quý | Có | [[src-vab-ftp#^vab-ftp-65]] |
| Hỗ trợ huy động | Phần bù cộng vào đường cong | Hàng năm hoặc khi kế hoạch kinh doanh đổi | Có | [[src-vab-ftp#^vab-ftp-65]] |
| Chi phí BHTG | Phần bù cộng vào đường cong | Hàng quý | Có | [[src-vab-ftp#^vab-ftp-65]] |
| Chi phí DTBB | Phần bù cộng vào đường cong | Hàng quý | Có | [[src-vab-ftp#^vab-ftp-65]] |
| Phần bù tài sản thanh khoản | Phần bù cộng vào đường cong | Hàng quý | Có | [[src-vab-ftp#^vab-ftp-65]] |
| Phần bù thanh khoản kỳ hạn (TLP) | Đường cong (cấu trúc kỳ hạn) | Hàng quý | Có | [[src-vab-ftp#^vab-ftp-65]] |
| Điều chỉnh ALCO (nợ và có) | Phần bù cộng vào đường cong | Hàng quý | Không, tuỳ ALCO | [[src-vab-ftp#^vab-ftp-65]] |

- VOF gồm lãi suất FTP cơ sở, hỗ trợ huy động và điều chỉnh ALCO cho tài sản nợ [[src-vab-ftp#^vab-ftp-6]] [[src-vab-ftp#^vab-ftp-63]].
- COF gồm lãi suất FTP cơ sở cộng các phần bù chi phí (DTBB, BHTG, tài sản thanh khoản, TLP) và điều chỉnh ALCO cho tài sản có [[src-vab-ftp#^vab-ftp-7]] [[src-vab-ftp#^vab-ftp-65]] [[src-vab-ftp#^vab-ftp-64]].
- Điều chỉnh ALCO cho tài sản có có thể khớp hoặc không khớp với điều chỉnh cho tài sản nợ, tuỳ mục tiêu chiến lược [[src-vab-ftp#^vab-ftp-64]].

*Diễn giải:* base curve VND của VAB lấy từ lãi suất huy động thực tế nên gần cost approach; base curve USD và đường cong TT2 lấy từ lãi suất thị trường nên gần market approach. Phân loại này do LLM gán, VAB không tự gọi tên cách tiếp cận.

### Q2 — Thang kỳ hạn và nội suy

- Kỳ hạn không nằm trên thang chuẩn của biểu được nội suy/ngoại suy trực tiếp từ thang chuẩn, cho cả VOF [[src-vab-ftp#^vab-ftp-30]] và COF [[src-vab-ftp#^vab-ftp-31]].
- Base curve VND: kỳ hạn thiếu thông số được nội suy/ngoại suy tuyến tính bằng Excel [[src-vab-ftp#^vab-ftp-42]].
- Base curve USD minh hoạ: kỳ 14D, 21D không có dữ liệu được gán bằng 7D; từ 24M lấy theo IRS [[src-vab-ftp#^vab-ftp-82]].
- Đường cong TT2: kỳ hạn tham chiếu thiếu thông số được nội/ngoại suy dựa trên biên độ chênh lệch lãi suất giữa các kỳ hạn [[src-vab-ftp#^vab-ftp-58]].

| Đường cong | Thang kỳ hạn trong nguồn | Nguồn |
|---|---|---|
| Base curve TT1 (minh hoạ PL02) | NM, 7D, 14D, 21D, 1M, 2M, 3M, …, 12M, 24M, 36M, 48M, 60M | [[src-vab-ftp#^vab-ftp-82]] |
| Đầu vào TT2 (MB04) | ON, 7D, 14D, 21D, 1M, 2M, 3M, 6M và các kỳ tiếp theo | [[src-vab-ftp#^vab-ftp-54]] |

Choudhry yêu cầu đường cong discount factor dài ít nhất bằng kỳ hạn dài nhất của sản phẩm trên bảng cân đối [[src-choudhry-principles-banking#^choudhry-ifc-23]]. Khi kỳ hạn dài nhất của trái phiếu đã phát hành ngắn hơn kỳ hạn cần dựng, ngân hàng dùng mô hình ngoại suy [[src-choudhry-principles-banking#^choudhry-ifc-5]]. Choudhry nêu spline, Nelson–Siegel và Svensson là cách ngân hàng trung ương dựng zero-coupon curve từ trái phiếu chính phủ; với trái phiếu ngân hàng ngang hàng, Choudhry nêu hạn chế của OLS và Nelson–Siegel [[src-choudhry-principles-banking#^choudhry-ifc-14]]. VAB không dùng các phương pháp này.

*Diễn giải (ngoài wiki, chưa có nguồn):* nội suy tuyến tính giữa hai điểm thang chuẩn $T_1 < T < T_2$ có dạng chuẩn sau; VAB không ghi công thức này.

$$
r(T) = r(T_1) + \frac{T - T_1}{T_2 - T_1}\left[r(T_2) - r(T_1)\right]
$$

### Q3 — Base curve theo đồng tiền

| Đồng tiền | Dữ liệu đầu vào | Xử lý | Nguồn |
|---|---|---|---|
| VND | Lãi suất huy động tiền gửi VND thực tế bình quân 3 tháng liền kề, đã gồm chi phí huy động | Nội/ngoại suy tuyến tính kỳ thiếu | [[src-vab-ftp#^vab-ftp-41]] [[src-vab-ftp#^vab-ftp-42]] |
| USD | LIBOR/SIBOR hoặc công cụ thay thế (SOFR); đường cong IRS USD | Bình quân 3 tháng liền kề trên từng kỳ hạn | [[src-vab-ftp#^vab-ftp-41]] [[src-vab-ftp#^vab-ftp-42]] |
| Ngoại tệ khác | Theo phương pháp của USD | — | [[src-vab-ftp#^vab-ftp-79]] |

- Lãi suất FTP cơ sở được tính riêng cho từng loại tiền [[src-vab-ftp#^vab-ftp-27]].
- Minh hoạ USD: LIBOR bình quân 3 tháng cho kỳ ngắn, IRS bình quân 3 tháng cho kỳ từ 12M trở lên [[src-vab-ftp#^vab-ftp-82]].
- Danh mục đầu vào VND của VAB không có VNIBOR, OMO hay lợi suất TPCP [[src-vab-ftp#^vab-ftp-41]]. VNIBOR chỉ xuất hiện ở đường cong TT2 [[src-vab-ftp#^vab-ftp-59]].

### Q4 — Phụ phí pháp định theo đồng tiền

| Phụ phí | Cách tính (VAB) | Mẫu số | Nguồn |
|---|---|---|---|
| BHTG | Chi phí BHTG thực tế 3 tháng liền kề, quy đổi năm (×4) | Bình quân tổng tài sản bị tính FTP | [[src-vab-ftp#^vab-ftp-84]] |
| DTBB | Số dư DTBB tối thiểu theo yêu cầu NHNN 3 tháng liền kề | Bình quân tổng tài sản bị tính FTP | [[src-vab-ftp#^vab-ftp-85]] |
| Tài sản thanh khoản | Số dư bình quân TSTK × (VOF bình quân − LSBQ TSTK) | Tổng tài sản bị tính FTP | [[src-vab-ftp#^vab-ftp-45]] |
| Hỗ trợ huy động | Từ NII kế hoạch vay gửi, tính đầu năm, riêng từng loại tiền | — | [[src-vab-ftp#^vab-ftp-80]] |

- Tổng tài sản bị tính FTP bằng tổng tài sản trừ tài sản thanh khoản, tài sản ghi nhận cho Khối QL&KDV và tài sản có khác, lấy bình quân 3 tháng liền kề [[src-vab-ftp#^vab-ftp-81]].
- Mức BHTG VAB ghi: 0.15%/năm trên số dư tiền gửi VND của KHCN [[src-vab-ftp#^vab-ftp-8]].
- DTBB là tỷ lệ % tiền gửi NHNN yêu cầu nắm giữ tại NHNN [[src-vab-ftp#^vab-ftp-9]]; VAB dẫn TT30/2019 làm căn cứ [[src-vab-ftp#^vab-ftp-78]].
- TSTK là tài sản thanh khoản cao giữ làm đệm, danh mục theo Phụ lục 3 TT22/2019 [[src-vab-ftp#^vab-ftp-43]].
- Tỷ lệ DTBB VND và ngoại tệ, lãi suất trả cho tiền gửi DTBB, trần lãi suất huy động USD: [cần nguồn].

### Q5 — FX swap và CIP

- VAB dựng đường cong USD từ lãi suất tham chiếu USD và đường cong IRS USD [[src-vab-ftp#^vab-ftp-41]], không quy đổi từ đường cong VND qua điểm swap.
- Choudhry: ở thị trường mới nổi thiếu swap và trái phiếu dài hạn, giải pháp tối ưu là synthetic yield curve từ implied yield và FX forward (có thể là NDF). Đầu vào là IRS của thị trường phát triển, FX spot và FX forward [[src-choudhry-principles-banking#^choudhry-ifc-13]]. Công thức implied yield bị mất khi convert [[src-choudhry-principles-banking#^choudhry-ifc-13]].
- Table 4.2 của Choudhry: thị trường mới nổi dùng cách đơn giản (implied yield curve và FX forward) và có thể bỏ tách liquidity cost khỏi base cost [[src-choudhry-principles-banking#^choudhry-ifc-22]].
- TLP curve của ngân hàng là gốc để dựng mọi cross-currency funding curve [[src-choudhry-principles-banking#^choudhry-ifc-4]].

### Q6 — VOF/COF theo sản phẩm (VAB, TT1)

| Sản phẩm | Base rate | TLP | Nguồn |
|---|---|---|---|
| Tiền gửi gốc trả cuối kỳ (cố định hoặc thả nổi) | VOF theo kỳ hạn gốc, biểu tại ngày phát sinh, cố định suốt thời gian gửi | 0 | [[src-vab-ftp#^vab-ftp-71]] |
| Tiền gửi gửi góp | LS huy động gửi góp + chênh lệch VOF và LS huy động của tiền gửi cuối kỳ cùng kỳ hạn | 0 | [[src-vab-ftp#^vab-ftp-72]] |
| Tiền gửi KKH, có mô hình hành vi | Bình quân gia quyền base curve theo tỷ lệ non-core / core | — | [[src-vab-ftp#^vab-ftp-14]] [[src-vab-ftp#^vab-ftp-15]] |
| Tiền gửi KKH, chưa có mô hình hành vi | VOF KKH × a% + VOF kỳ hạn 2 tháng (hoặc theo ALCO) × (1 − a%), a% ≥ 15% | — | [[src-vab-ftp#^vab-ftp-16]] [[src-vab-ftp#^vab-ftp-44]] |
| Tiền gửi rút trước hạn | VOF theo KKH thông thường | — | [[src-vab-ftp#^vab-ftp-18]] |
| Vostro | VOF TT2 kỳ hạn ON, cố định suốt giao dịch | 0 | [[src-vab-ftp#^vab-ftp-56]] |
| Cho vay gốc trả cuối kỳ | COF theo kỳ hạn gốc (ngày đáo hạn − ngày giải ngân), biểu tại ngày giải ngân | 0 khi cố định | [[src-vab-ftp#^vab-ftp-32]] |
| Cho vay lãi suất thả nổi, trả cuối kỳ | [cần nguồn] (Đ6.2.c chưa có claim) | Kỳ hạn gốc − kỳ tái định giá | [[src-vab-ftp#^vab-ftp-33]] |
| Cho vay trả gốc định kỳ, cố định (W.A) | COF theo kỳ hạn hiệu lực bình quân gia quyền, biểu tại ngày giải ngân | 0 | [[src-vab-ftp#^vab-ftp-73]] |
| Cho vay trả gốc định kỳ, thả nổi | [cần nguồn] (Đ6.2.e chưa có claim) | Kỳ hạn hiệu lực − kỳ tái định giá | [[src-vab-ftp#^vab-ftp-34]] |
| Cho vay trả trước hạn | COF theo kỳ hạn hiệu lực từ dòng tiền mô hình hành vi trả trước hạn | — | [[src-vab-ftp#^vab-ftp-19]] |
| Cho vay quá hạn | COF theo kỳ hạn khoản vay trước khi quá hạn, trên số dư tại thời điểm quá hạn | Theo tính chất dòng tiền trước quá hạn | [[src-vab-ftp#^vab-ftp-74]] |
| Cho vay gia hạn | COF theo kỳ hạn gốc mới hoặc kỳ điều chỉnh lãi suất | Theo tính chất dòng tiền | [[src-vab-ftp#^vab-ftp-75]] |
| Cho vay ưu đãi, cố định, trả cuối kỳ | PA1 giữ kỳ hạn gốc, đổi FTP khi hết ưu đãi; PA2 tách kỳ ưu đãi và ngoài ưu đãi | 0 | [[src-vab-ftp#^vab-ftp-76]] |
| TPDN giữ đến đáo hạn | Như cho vay gốc trả cuối kỳ | — | [[src-vab-ftp#^vab-ftp-77]] |
| TPDN Trading/AFS | COF TT1 theo kỳ hạn từ mô hình hành vi; chưa có mô hình thì theo quy tắc sổ kinh doanh TT41/2016 (thường dưới 1 năm) | — | [[src-vab-ftp#^vab-ftp-77]] |
| Hạn mức thẻ tín dụng, thấu chi chưa dùng | Phần bù rủi ro thanh khoản tiềm tàng (Q7) | — | [[src-vab-ftp#^vab-ftp-68]] |

- TLP chỉ áp cho khoản vay lãi suất thả nổi [[src-vab-ftp#^vab-ftp-12]]. TLP phản ánh rủi ro tín dụng riêng của ngân hàng kết hợp với phần bù thanh khoản kỳ hạn của thị trường [[src-vab-ftp#^vab-ftp-11]].
- TLP tính hai bước: dùng base curve hoàn thiện đường lãi suất giả định cho các kỳ tái định giá, rồi lấy lãi suất kỳ gốc trừ lãi suất kỳ tái định giá [[src-vab-ftp#^vab-ftp-46]]. Ma trận minh hoạ: [[ftp-pricing-methodology]], mục 5.
- Kỳ hạn hiệu lực của khoản vay trả định kỳ tính bằng bình quân gia quyền theo lịch trả gốc [[src-vab-ftp#^vab-ftp-20]] [[src-vab-ftp#^vab-ftp-73]]; công thức bị mất khi convert.
- ALCO có thể đổi phương pháp định giá VOF cho từng sản phẩm tiền gửi [[src-vab-ftp#^vab-ftp-71]].
- Phần dư nợ thấu chi đã dùng (tách core/non-core, gán kỳ hạn): [cần nguồn].

### Q7 — Cam kết ngoại bảng

$$
\text{Contingent charge} = C \times P\% \times \text{Tỷ lệ dự trữ thanh khoản} \times \text{Chi phí duy trì TSTK}
$$
[[src-vab-ftp#^vab-ftp-69]]

- Không có mô hình hành vi thì thay P% bằng CCF theo Điều 10 TT41/2016 [[src-vab-ftp#^vab-ftp-69]].
- C là tổng số dư cam kết/hạn mức chưa sử dụng; tỷ lệ dự trữ thanh khoản là đệm thanh khoản thực tế; P% là tỷ lệ giải ngân trên hạn mức chưa giải ngân [[src-vab-ftp#^vab-ftp-69]].
- Minh hoạ thẻ tín dụng: hạn mức khả dụng 80.000.000, CCF 10%, tỷ lệ dự trữ 10%, chi phí duy trì 1.5% (6.5% − 5%), phần bù 12.000 [[src-vab-ftp#^vab-ftp-48]].
- VAB dẫn văn bản BIS 12/2011 về định giá chuyển vốn rủi ro thanh khoản [[src-vab-ftp#^vab-ftp-68]]. Khái niệm rủi ro liên quan: [[liquidity-cost-risk]].

### Q8 — TT1 và TT2

| Tiêu chí | TT1 | TT2 | Nguồn |
|---|---|---|---|
| Phạm vi | Đơn vị kinh doanh mua bán vốn với CFU | Giao dịch trên thị trường liên ngân hàng | [[src-vab-ftp#^vab-ftp-78]] [[src-vab-ftp#^vab-ftp-36]] |
| Tần suất biểu | Hằng quý hoặc khi thị trường biến động lớn | Hằng ngày, 9–10 giờ | [[src-vab-ftp#^vab-ftp-49]] [[src-vab-ftp#^vab-ftp-52]] |
| Căn cứ lãi suất | Base curve + các phần bù (Q1) | PA1: mid-rate 3–6 NH TMCP cùng peer; PA2: VNIBOR 1 tuần | [[src-vab-ftp#^vab-ftp-65]] [[src-vab-ftp#^vab-ftp-57]] [[src-vab-ftp#^vab-ftp-59]] |
| Lọc dữ liệu | — | Giá peer lệch quá ±15% bình quân nhóm bị loại (outlier) | [[src-vab-ftp#^vab-ftp-58]] |
| Biên độ | Điều chỉnh ALCO | CFU được cộng trừ biên độ đã được ALCO thông qua | [[src-vab-ftp#^vab-ftp-63]] [[src-vab-ftp#^vab-ftp-58]] |
| Đối tượng mua bán | Đơn vị kinh doanh với CFU | PA1: từng desk với CFU; PA2: trạng thái ròng cả khối qua MM | [[src-vab-ftp#^vab-ftp-78]] [[src-vab-ftp#^vab-ftp-60]] [[src-vab-ftp#^vab-ftp-61]] |

- Danh sách ngân hàng peer do ALCO rà soát tối thiểu 1 năm/lần [[src-vab-ftp#^vab-ftp-57]].
- PA2 cơ chế khối cần hạn mức thanh khoản 30 ngày cho trạng thái ròng của khối; chưa có thì theo dõi định kỳ tỷ lệ khả năng chi trả 30 ngày [[src-vab-ftp#^vab-ftp-61]].
- Giao dịch trước khi ban hành biểu TT2 mới áp biểu của ngày làm việc liền trước [[src-vab-ftp#^vab-ftp-53]].
- Nostro (kể cả tiền gửi tại NHNN) đã tính chi phí TSTK nên không mua bán vốn FTP với CFU [[src-vab-ftp#^vab-ftp-55]].
- GTCG phát hành theo yêu cầu ALCO, ghi tại book Hội sở thì không áp mua bán vốn nội bộ [[src-vab-ftp#^vab-ftp-62]].
- Quy trình và vai trò từng bộ phận: [[alm-operating-model]].

### Q9 — Rà soát, ban hành, phê duyệt

Quy trình TT1 (PL05):
1. Hằng quý hoặc khi thị trường biến động lớn, Bộ phận quản lý FTP đề xuất cập nhật biểu và yêu cầu dữ liệu đầu vào [[src-vab-ftp#^vab-ftp-49]].
2. Khối CNTT chiết xuất dữ liệu tính lãi suất FTP cơ sở; khối kinh doanh lập đề xuất FTP đặc biệt/ngoại lệ [[src-vab-ftp#^vab-ftp-49]].
3. Trưởng bộ phận quản lý FTP rà soát, trình ALCO tham mưu TGĐ phê duyệt và ban hành biểu TT1 [[src-vab-ftp#^vab-ftp-50]].
4. Khối CNTT/Bộ phận quản lý FTP cập nhật biểu lên hệ thống quản lý vốn nội bộ; cấp kiểm soát xác nhận giao dịch; kế toán lưu hồ sơ [[src-vab-ftp#^vab-ftp-51]].

- TT2: TGĐ phê duyệt biểu lãi suất FTP nội bộ giữa CFU và Khối QL&KDV hằng ngày [[src-vab-ftp#^vab-ftp-53]].
- Điều chỉnh ALCO cho chương trình hoặc sản phẩm ưu đãi cụ thể được ALCO xem xét trên tờ trình riêng [[src-vab-ftp#^vab-ftp-64]].
- Choudhry: ngân hàng nên làm trơn đường cong bằng trung bình trượt 14 hoặc 30 ngày, đổi sang 60 ngày khi biến động cực mạnh; quyết định thuộc ALCO hoặc tiểu ban ALCO [[src-choudhry-principles-banking#^choudhry-ifc-6]]. Choudhry cũng khuyến nghị nêu quy trình dựng đường cong trong văn bản chính sách chính thức [[src-choudhry-principles-banking#^choudhry-ifc-1]].
- Syndicated loan: TLP có thể đặt ở trung bình trượt 3 tháng, cập nhật hằng quý [[src-choudhry-principles-banking#^choudhry-ifc-7]].

## Bằng chứng ủng hộ

- Q1–Q9 dựa chủ yếu vào một nguồn T4 là phương pháp luận nội bộ VAB; Choudhry (T4) bổ sung khung phân loại và thông lệ dựng đường cong.
- VAB và Choudhry cùng dùng trung bình trượt: VAB lấy bình quân 3 tháng cho đầu vào base curve [[src-vab-ftp#^vab-ftp-41]] [[src-vab-ftp#^vab-ftp-42]], Choudhry khuyến nghị trung bình trượt 14/30/60 ngày [[src-choudhry-principles-banking#^choudhry-ifc-6]].

## Bằng chứng trái chiều

- **Tần suất ban hành biểu TT1 (nội bộ VAB).** Cột thời gian ghi "Hàng quý/khi có yêu cầu", bước 3 và 5 ghi ban hành "Giải pháp FTP hàng tháng" [[src-vab-ftp#^vab-ftp-50]]. Bảng Đ4.4 ghi hằng quý [[src-vab-ftp#^vab-ftp-65]]. Callout conflict ở [[ftp-pricing-methodology]].
- **Định nghĩa kỳ hiệu lực (nội bộ VAB).** Đ4.3.4.b định nghĩa là kỳ hạn chiết khấu về hiện tại của các dòng lịch trả [[src-vab-ftp#^vab-ftp-70]]. Đ6.2.d tính bằng bình quân gia quyền theo lịch trả gốc [[src-vab-ftp#^vab-ftp-73]]. Cần bản docx gốc để đối chiếu công thức.
- **Minh hoạ base curve VND.** 12M = 4.53 rồi 24M = 2.72 [[src-vab-ftp#^vab-ftp-82]], trong khi ví dụ TLP dùng 24M = 4.81 [[src-vab-ftp#^vab-ftp-47]].
- **Minh hoạ BHTG, DTBB.** Ví dụ BHTG dùng tổng tài sản ngày đầu làm mẫu số [[src-vab-ftp#^vab-ftp-84]], khác định nghĩa bình quân tổng tài sản bị tính FTP [[src-vab-ftp#^vab-ftp-81]]. Ví dụ DTBB ghi 0.00% [[src-vab-ftp#^vab-ftp-85]].
- **Cost vs market approach.** Choudhry ghi cost approach phụ thuộc lãi suất quá khứ và phản ứng trễ [[src-choudhry-principles-banking#^choudhry-ifc-17]]; base curve VND của VAB dùng lãi suất huy động thực tế bình quân 3 tháng [[src-vab-ftp#^vab-ftp-41]].

*Diễn giải:* các điểm trên là sai lệch trong một nguồn hoặc giữa khuyến nghị và thực hành, không phải hai quy định cùng phạm vi, nên không đặt callout conflict trong synthesis.

## Phụ thuộc regime

- **Mức phát triển thị trường.** Thị trường phát triển dựng được nhiều loại đường cong và dùng mô hình hành vi; thị trường mới nổi dùng implied yield curve và FX forward, có thể bỏ tách liquidity cost và base cost [[src-choudhry-principles-banking#^choudhry-ifc-22]].
- **Quy mô ngân hàng.** Ngân hàng thị phần lớn cần mô hình và IT riêng cho sản phẩm không kỳ hạn; ngân hàng thị phần nhỏ dùng giả định có căn cứ và tính tay từng giao dịch [[src-choudhry-principles-banking#^choudhry-ifc-21]].
- **Có hay chưa có mô hình hành vi.** VAB đổi cách định giá tiền gửi KKH (redemption curve vs a% ≥ 15%) [[src-vab-ftp#^vab-ftp-14]] [[src-vab-ftp#^vab-ftp-44]], TPDN Trading/AFS [[src-vab-ftp#^vab-ftp-77]] và phần bù tiềm tàng (P% vs CCF) [[src-vab-ftp#^vab-ftp-69]].
- **Biến động thị trường.** Choudhry đổi cửa sổ làm trơn từ 14/30 ngày sang 60 ngày khi biến động cực mạnh [[src-choudhry-principles-banking#^choudhry-ifc-6]]; VAB cập nhật biểu TT1 ngoài kỳ quý khi thị trường biến động lớn [[src-vab-ftp#^vab-ftp-49]].

## Hàm ý ALM / quy định

**Quy định NHNN.** Wiki chưa có văn bản NHNN quy định phương pháp FTP. Căn cứ VN trong synthesis là các văn bản VAB dẫn cho từng phần bù:
- VAB dẫn TT13/2018, TT22/2019, TT30/2019 làm căn cứ [[src-vab-ftp#^vab-ftp-78]], và TT22/2019 cho phần bù tài sản thanh khoản [[src-vab-ftp#^vab-ftp-10]] [[src-vab-ftp#^vab-ftp-43]] [[src-vab-ftp#^vab-ftp-44]].
- TT50/2026 sửa Điều 2 TT22: đối tượng của TT22 chỉ còn ngân hàng hợp tác xã và NHTM đang thực hiện Đ23.3 TT41/2016 [[src-tt50-2026-nhnn#^d37-3a]].
- Từ khi TT50 có hiệu lực đến trước ngày áp dụng LCR/NSFR, ngân hàng vẫn phải tuân thủ và báo cáo tỷ lệ dự trữ thanh khoản, tỷ lệ khả năng chi trả 30 ngày, tỷ lệ nguồn vốn ngắn hạn cho vay trung dài hạn và LDR theo TT22 [[src-tt50-2026-nhnn#^d13-4]].
- Từ 01/10/2028 ngân hàng phải áp dụng LCR và NSFR [[src-tt50-2026-nhnn#^d13-1]]; khi đó các tỷ lệ cũ của TT22 không phải tuân thủ nhưng vẫn phải báo cáo [[src-tt50-2026-nhnn#^d13-5]].

*Diễn giải:*
- Sau khi ngân hàng áp dụng LCR, đệm thanh khoản trong phần bù FTP nên đo theo [[hqla]] của TT50. Tỷ lệ rút KKH 15% dẫn từ Phụ lục 3 TT22 khi đó mất tính bắt buộc, và ngân hàng cần căn cứ khác như mô hình hành vi hoặc hệ số rút tiền của TT50.
- Ngân hàng VN thiếu trái phiếu phát hành có thị trường thứ cấp thanh khoản thì không áp được quy trình no-arbitrage của Choudhry. Khi đó ngân hàng rơi vào nhóm "thị trường mới nổi" của Table 4.2, phù hợp với cách VAB dùng lãi suất huy động thực tế cho VND.
- Base curve VND theo lãi suất huy động bình quân 3 tháng phản ứng trễ với thay đổi lãi suất thị trường. ALCO cần theo dõi chênh lệch giữa biểu TT1 và đường cong TT2 trong kỳ quý.

Synthesis FTP liên quan: [[ftp-final-rate-determination]], [[ftp-risk-and-cost-components]], [[ftp-portfolio-and-bucket-allocation]], [[ftp-cost-benefit-allocation-principles]], [[ftp-nature-and-balance-sheet-management]].

## Bất định
- [2026-10-21] ingest src-vab-ftp u04 (bổ sung nhóm 5): [[ftp-pricing-methodology]] mục 5.5 thêm cổ phiếu chiến lược (≥ 1 năm hoặc ≥ 5 năm) và tài sản khác (không tính FTP) [[src-vab-ftp#^vab-ftp-91]] [[src-vab-ftp#^vab-ftp-92]]; mục 5.6 mới: tính lại VOF/COF khi đổi tần suất lãi suất, lịch trả gốc, loại hình lãi suất, đồng tiền, hình thức trả gốc, tiền gửi tái tục [[src-vab-ftp#^vab-ftp-93]] [[src-vab-ftp#^vab-ftp-95]] [[src-vab-ftp#^vab-ftp-96]] [[src-vab-ftp#^vab-ftp-97]], ALCO điều chỉnh thủ công khi giá biến động ±0.2% [[src-vab-ftp#^vab-ftp-94]]; cần rà lại bảng Q6, Q9 và dòng Q6 trong mục này.
- [2026-10-21] ingest src-vab-ftp u03 (bổ sung nhóm 4): [[ftp-pricing-methodology]] mục 5.5 có cho vay thả nổi trả cuối kỳ và trả định kỳ (COF theo kỳ tái định giá, áp đến ngày điều chỉnh tiếp theo) [[src-vab-ftp#^vab-ftp-86]] [[src-vab-ftp#^vab-ftp-87]] và sản phẩm ưu đãi thả nổi/trả định kỳ hai phương án [[src-vab-ftp#^vab-ftp-88]] [[src-vab-ftp#^vab-ftp-89]] [[src-vab-ftp#^vab-ftp-90]]; cần rà lại bảng Q6 (hai ô [cần nguồn]) và dòng Q6 trong mục này.

- Q4: tỷ lệ DTBB VND và ngoại tệ, lãi suất tiền gửi DTBB, trần lãi suất huy động USD chưa có nguồn. Cần `/register` TT30/2019 (VAB dẫn làm căn cứ, [[src-vab-ftp#^vab-ftp-78]]) và văn bản NHNN về trần lãi suất.
- Q5: công thức CIP và công thức implied yield của synthetic curve chưa có nguồn (Choudhry bị mất công thức khi convert).
- Q6: raw VAB có đoạn chưa có claim trong source note: Đ6.2.c cho vay trả cuối kỳ thả nổi (u03, dòng 731–757), Đ6.2.e cho vay trả định kỳ thả nổi (u03, dòng 758–770), Đ6.2.j và Đ6.2.l sản phẩm ưu đãi thả nổi (u03, dòng 853–930), đổi loại hình lãi suất (u04, dòng 1078–1080). Phần dư nợ thấu chi đã dùng chưa có nguồn.
- Q2: VAB không nêu phương pháp nội suy cho COF/VOF của kỳ hạn lẻ ngoài chữ "nội suy/ngoại suy trực tiếp"; tính tuyến tính chỉ có nguồn cho base curve VND.
- Kỳ hiệu lực và các công thức W.A, WAT, chi phí duy trì TSTK bị mất khi convert; cần bản docx gốc.
