---
title: "Xây dựng FTP curve và FTP rate theo kỳ hạn, đồng tiền và loại sản phẩm"
aliases: [FTP curve và FTP rate theo kỳ hạn, đồng tiền, sản phẩm, FTP curve and rate by tenor, currency and product]
type: synthesis
domains: [alm, product, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "FTP curve/FTP rate được xây dựng như thế nào cho từng kỳ hạn, đồng tiền và loại sản phẩm? · (Q1) kỳ hạn · (Q2) đồng tiền · (Q3) loại sản phẩm · (Q4) từ base curve đến FTP rate cuối cùng · (Q5) rà soát, phê duyệt và thay đổi trong vòng đời giao dịch"
as_of: 2026-10-22
sources: ["[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-tata-bank-alm]]", "[[src-lubinska-alm-optimisation]]", "[[src-bardaeva-alm]]", "[[src-bcbs-liquidity-principles-2008]]", "[[src-tt83-2025-nhnn]]", "[[src-tt50-2026-nhnn]]"]
relations: []
# relations — synthesis: luôn để trống; synthesis không làm chủ thể hay đích của relation. Quan hệ khai ở node tri thức (chủ thể A); thân bài trình bày chuỗi quan hệ trong `## Cơ chế`. Xem 03_meta/taxonomy.md, mục "Relation"
tags: [ftp, ftp-curve, tenor, currency, product, vof, cof, tlp]
updated: 2026-10-22
reviewed:
---

## Câu hỏi

- Q1. FTP curve được xây dựng thế nào cho từng kỳ hạn (cách dựng base curve, thang kỳ hạn, nội suy)?
- Q2. FTP curve được xây dựng thế nào cho từng đồng tiền (VND, USD, ngoại tệ khác, cross-currency)?
- Q3. FTP rate được gán thế nào cho từng loại sản phẩm (tiền gửi, CASA, cho vay cố định, thả nổi, trả dần, ưu đãi, trái phiếu, cổ phiếu, khoản mục khác)?
- Q4. Từ base curve đến FTP rate cuối cùng gồm những cấu phần cộng thêm nào?
- Q5. FTP curve và FTP rate được rà soát, phê duyệt và thay đổi trong vòng đời giao dịch thế nào?

Câu gốc của user: "FTP curve/FTP rate được xây dựng như thế nào cho từng kỳ hạn, đồng tiền và loại sản phẩm?" Một cụm, không hub. Cụm này đi vào cách dựng và cách gán. [[ftp-balance-sheet-risk-and-cost-components]] trả lời rủi ro và chi phí nào nằm trong FTP; [[ftp-purpose-and-balance-sheet-problems]] trả lời FTP là gì. Node nền: [[internal-funding-curve]], [[ftp-pricing-methodology]], [[cost-of-funds]], [[funds-transfer-pricing]] (đều `draft`). Mốc as_of 2026-10-22.

## Kết luận

Nguồn đã ingest mô tả FTP rate như tích của hai bước: dựng base curve theo từng đồng tiền và kỳ hạn, rồi gán cho mỗi giao dịch một điểm kỳ hạn trên curve cùng các cấu phần cộng thêm. Phía VN chỉ có tài liệu tư vấn VAB (T4, `draft`, không rõ ngày). TT83/2025 mới đặt yêu cầu ở mức nguyên tắc.

**Q1 — kỳ hạn.** Choudhry nêu bốn cách dựng FTP curve: market, cost, mixed và marginal [[src-choudhry-principles-banking#^choudhry-ifc-16]]. VAB dùng thang kỳ hạn chuẩn trong biểu ban hành, kỳ hạn ngoài thang được nội suy hoặc ngoại suy từ thang này [[src-vab-ftp#^vab-ftp-30]] [[src-vab-ftp#^vab-ftp-31]]. Với tiền VND, base curve lấy lãi suất huy động thực tế bình quân toàn hàng của các khoản phát sinh trong 3 tháng liền kề, và kỳ hạn thiếu dữ liệu được nội suy tuyến tính [[src-vab-ftp#^vab-ftp-28]] [[src-vab-ftp#^vab-ftp-42]]. Cách dựng TLP curve từ giá nợ đã phát hành của ngân hàng có quy trình 4 bước [[src-choudhry-principles-banking#^choudhry-ifc-4]].

**Q2 — đồng tiền.** Mọi cấu phần của giá FTP được tính độc lập theo từng loại tiền [[src-vab-ftp#^vab-ftp-26]]. VAB dựng base curve VND từ lãi suất huy động thực tế, base curve USD từ lãi suất tham chiếu thị trường, và áp phương pháp của USD cho ngoại tệ khác [[src-vab-ftp#^vab-ftp-28]] [[src-vab-ftp#^vab-ftp-29]] [[src-vab-ftp#^vab-ftp-79]]. Với vị thế ngoại tệ do ALM tập trung, Tata nêu lựa chọn định giá trên FTP curve của đồng tiền cơ sở sau điều chỉnh cross-currency lên funding spread [[src-tata-bank-alm#^tata-ftp-15]]. Choudhry nêu synthetic yield curve dựng từ IRS thị trường phát triển cùng FX spot và FX forward cho thị trường mới nổi [[src-choudhry-principles-banking#^choudhry-ifc-13]].

**Q3 — sản phẩm.** Quy tắc chung của VAB: kỳ hạn tính giá của tiền gửi gốc trả cuối kỳ là kỳ hạn gốc [[src-vab-ftp#^vab-ftp-71]]; của cho vay trả gốc định kỳ lãi suất cố định là kỳ hạn hiệu lực bình quân gia quyền [[src-vab-ftp#^vab-ftp-73]]; của cho vay thả nổi là kỳ tái định giá, phần chênh với kỳ hạn gốc hoặc hiệu lực là TLP [[src-vab-ftp#^vab-ftp-86]] [[src-vab-ftp#^vab-ftp-87]]. CASA nhận base curve trung bình có trọng số theo tỷ lệ không ổn định do mô hình hành vi tính [[src-vab-ftp#^vab-ftp-15]]. Bảng đầy đủ ở mục Q3.

**Q4 — cấu phần FTP rate.** VOF gồm base curve, margin hỗ trợ huy động và điều chỉnh ALCO [[src-vab-ftp#^vab-ftp-6]]. COF thêm chi phí DTBB, chi phí BHTG, phần bù tài sản thanh khoản và TLP [[src-vab-ftp#^vab-ftp-7]]. Tata tách FTP thành pure interest rate risk curve cộng funding spread [[src-tata-bank-alm#^tata-ftp-10]].

**Q5 — rà soát và thay đổi.** VAB rà soát base curve, BHTG, DTBB, phần bù TSTK, TLP và điều chỉnh ALCO hằng quý; hỗ trợ huy động rà soát hằng năm [[src-vab-ftp#^vab-ftp-65]]. Biểu FTP thị trường 1 trình ALCO tham mưu để Tổng giám đốc phê duyệt [[src-vab-ftp#^vab-ftp-50]]. Giá FTP của giao dịch cố định suốt thời gian giao dịch và chỉ tính lại khi có sự kiện trong vòng đời [[src-vab-ftp#^vab-ftp-71]] [[src-vab-ftp#^vab-ftp-93]].

## Cơ chế

Viết tắt: BU (business unit, đơn vị kinh doanh); CFU (Trung tâm Quản lý Vốn); TT1 và TT2 (thị trường 1 và thị trường 2 trong tài liệu VAB); DTBB (dự trữ bắt buộc); BHTG (bảo hiểm tiền gửi); TSTK (tài sản thanh khoản); KKH (không kỳ hạn); VOF (giá mua vốn); COF (giá bán vốn); TLP (Term Liquidity Premium).

### Q1 — Kỳ hạn

**Nguyên tắc gán.** Tata mô tả: gộp các điểm cost of funds theo kỳ hạn thành transfer price curve; theo matched maturity, mỗi vị thế phát sinh nhận FTP rate từ điểm cùng kỳ hạn trên curve [[src-tata-bank-alm#^tata-ftp-8]]. Choudhry nêu việc chuyển vốn giữa Treasury và BU thanh toán trên cơ sở trùng khớp kỳ hạn theo một đường cong FTP phù hợp [[src-choudhry-principles-banking#^choudhry-ftp-6]].

**Bốn cách dựng base curve (Choudhry).**

| Cách | Nội dung | Ưu điểm | Hạn chế | Nguồn |
|---|---|---|---|---|
| Cost | Dựa trên lãi suất huy động | Dùng được khi thị trường ổn định, cấu trúc nợ đa dạng theo kỳ hạn | Phụ thuộc lãi suất quá khứ nên phản ứng trễ; đường cong có thể méo vì các kỳ hạn huy động ở thời điểm khác nhau; khi thừa nguồn không có công cụ điều tiết khối lượng tiền gửi | [[src-choudhry-principles-banking#^choudhry-ifc-17]] |
| Market | Dựa trên lãi suất thị trường | Khách quan, minh bạch, có FTP rate cho cả kỳ hạn chưa có khoản mục bảng cân đối, đường cong trơn | Chỉ báo tiền tệ biến động mạnh; thiếu chỉ báo trung dài hạn và giao dịch trái phiếu chính phủ mỏng ở một số thị trường | [[src-choudhry-principles-banking#^choudhry-ifc-18]] |
| Mixed | Pha đường cong thị trường và đường cong chi phí thực tế của nợ theo 3 bước, gồm phân tích nguồn vốn ổn định từng kỳ hạn | Phản ánh cơ cấu nợ đa dạng | Không nêu trong claim | [[src-choudhry-principles-banking#^choudhry-ifc-19]] |
| Marginal | Cấu phần thị trường cho chi phí vốn ngắn hạn cơ sở cộng spread riêng của ngân hàng phản ánh chi phí thanh khoản theo kỳ hạn | Phản ứng khá nhanh với thị trường | Tính chủ quan; giảm được ở ngân hàng có core liabilities đa dạng | [[src-choudhry-principles-banking#^choudhry-ifc-20]] |

**Marginal được bổ sung sau.** Ban đầu chỉ có market, cost và mixed; marginal thêm vào theo hướng dẫn của cơ quan quản lý [[src-choudhry-principles-banking#^choudhry-ifc-16]]. EBA Guidelines (10/2010) nêu giá nội bộ nên phản ánh chi phí vốn cận biên và khớp giá giao dịch wholesale khi có [[src-choudhry-principles-banking#^choudhry-ifc-15]].

**TLP curve từ nợ đã phát hành (Choudhry).** Quy trình gồm 4 bước:
1. fit phương pháp vào dữ liệu thị trường;
2. rút risky yield curve của ngân hàng;
3. dùng discount function để dựng par-par asset swap curve;
4. lấy đường cong này làm TLP curve hàm ý thị trường.

Bước này đòi hỏi thị trường thứ cấp thanh khoản cho trái phiếu của ngân hàng, nếu không phải dùng proxy [[src-choudhry-principles-banking#^choudhry-ifc-3]] [[src-choudhry-principles-banking#^choudhry-ifc-4]]. TLP curve là đường cong định giá không có tài sản bảo đảm, và có thể ngoại suy khi kỳ hạn dài nhất của trái phiếu phát hành ngắn hơn kỳ hạn cần dựng [[src-choudhry-principles-banking#^choudhry-ifc-5]]. Ngân hàng dựng curve có discount factor cho mọi kỳ hạn tới ít nhất kỳ hạn dài nhất của sản phẩm trên bảng cân đối [[src-choudhry-principles-banking#^choudhry-ifc-23]].

**Cách VAB dựng (TT1).**
- VND: lãi suất huy động tiền gửi VND thực tế bình quân 3 tháng liền kề, đã gồm chi phí huy động [[src-vab-ftp#^vab-ftp-41]].
- Kỳ hạn thiếu thông số: nội suy hoặc ngoại suy tuyến tính bằng Excel [[src-vab-ftp#^vab-ftp-42]].
- Kỳ hạn ngoài thang chuẩn của biểu ban hành: nội suy hoặc ngoại suy trực tiếp từ thang chuẩn, cho cả VOF và COF [[src-vab-ftp#^vab-ftp-30]] [[src-vab-ftp#^vab-ftp-31]].
- Ví dụ của VAB: VND dùng lãi suất huy động thực tế bình quân theo kỳ hạn; kỳ 14D và 21D của USD không có dữ liệu được gán 0,10 (bằng 7D) [[src-vab-ftp#^vab-ftp-82]].

**Cách VAB dựng (TT2, liên ngân hàng).** Có hai phương án [[src-vab-ftp#^vab-ftp-36]]:
- phương án 1 là mid-rate của 3 đến 6 ngân hàng TMCP cùng peer; ngân hàng có giá lệch quá ±15% so với bình quân các ngân hàng còn lại bị loại; CFU cộng trừ biên độ ALCO đã thông qua [[src-vab-ftp#^vab-ftp-57]] [[src-vab-ftp#^vab-ftp-58]];
- phương án 2 là VNIBOR kỳ hạn 1 tuần [[src-vab-ftp#^vab-ftp-59]].

Biểu TT2 được tính hằng ngày từ 9 giờ đến 10 giờ [[src-vab-ftp#^vab-ftp-52]].

**Làm trơn và ổn định.**
- Ngân hàng nên có quy trình làm trơn: trung bình trượt 14 hoặc 30 ngày của curve, có thể đổi sang 60 ngày khi biến động cực mạnh, quyết định ở cấp ALCO hoặc tiểu ban ALCO [[src-choudhry-principles-banking#^choudhry-ifc-6]].
- Với khoản vay có thời gian thu xếp dài như syndicated loan, TLP có thể đặt ở mức trung bình trượt 3 tháng, cập nhật hằng quý [[src-choudhry-principles-banking#^choudhry-ifc-7]].
- Cơ quan quản lý (PRA, EBA) nhấn mạnh một đường cong nhất quán cho mọi business line, bám giá thị trường [[src-choudhry-principles-banking#^choudhry-ifc-8]].

**Tách theo hai cấu phần (Tata).** FTP curve bù đắp cho Treasury cả rủi ro lãi suất và thanh khoản, nên dựng pure interest rate risk curve rồi cộng funding spread [[src-tata-bank-alm#^tata-ftp-10]]. Tata liệt kê các nguồn cho curve phi rủi ro: repo (thường thanh khoản đến 1–2 năm) và swap EURIBOR (kéo dài tới 30 năm, phản ánh rủi ro đối tác liên ngân hàng) [[src-tata-bank-alm#^tata-ftp-11]] [[src-tata-bank-alm#^tata-ftp-12]]. Funding spread đặc thù theo tài sản; thực tế dùng một FTP curve với spread bình quân rồi điều chỉnh theo trường hợp [[src-tata-bank-alm#^tata-ftp-13]].

### Q2 — Đồng tiền

- **Tính riêng theo đồng tiền.** Mọi cấu phần của giá FTP được tính độc lập theo từng loại tiền, và lãi suất FTP cơ sở được tính riêng cho từng loại tiền [[src-vab-ftp#^vab-ftp-26]] [[src-vab-ftp#^vab-ftp-27]]. Hỗ trợ huy động và lãi suất COF cơ sở của danh mục cũng tính riêng theo đồng tiền [[src-vab-ftp#^vab-ftp-80]] [[src-vab-ftp#^vab-ftp-67]].
- **VND.** Base curve dựng từ lãi suất huy động bình quân toàn hàng của các khoản phát sinh trong 3 tháng liền kề [[src-vab-ftp#^vab-ftp-28]].
- **USD.** Base curve dùng lãi suất tham chiếu thị trường, đầu vào gồm đường cong LIBOR/SIBOR hoặc công cụ thay thế như SOFR, và đường cong lãi suất hoán đổi USD; lấy bình quân 3 tháng liền kề trên từng kỳ hạn [[src-vab-ftp#^vab-ftp-29]] [[src-vab-ftp#^vab-ftp-41]] [[src-vab-ftp#^vab-ftp-42]]. Trong ví dụ của VAB, kỳ ngắn dùng LIBOR bình quân 3 tháng, từ 12M dùng IRS bình quân 3 tháng [[src-vab-ftp#^vab-ftp-82]].
- **Ngoại tệ khác.** Xác định theo phương pháp của USD [[src-vab-ftp#^vab-ftp-79]].
- **Cross-currency (Tata).** Công ty con ở vùng tiền tệ khác có thể dựng FTP curve theo từng đồng tiền dựa trên hoạt động thị trường tại chỗ. Khi ALM tập trung quản lý, thường không thực tế tạo nhiều curve; có thể định giá trên curve của đồng tiền cơ sở sau điều chỉnh cross-currency lên funding spread, quan sát được trên thị trường cross-currency swap của các đồng tiền chính [[src-tata-bank-alm#^tata-ftp-15]].
- **Synthetic curve cho thị trường mới nổi (Choudhry).** Thiếu swap và trái phiếu kỳ hạn dài thì dựng synthetic yield curve từ công thức implied yield và FX forward (có thể là NDF); đầu vào là IRS của thị trường phát triển theo kỳ hạn, FX spot và FX forward [[src-choudhry-principles-banking#^choudhry-ifc-13]]. Công thức bị mất khi convert nên không chép lại. [cần nguồn]
- **Môi trường.** Thị trường mới nổi có lạm phát và biến động lãi suất cao, khả năng dựng curve hạn chế hơn, và có thể dùng cách đơn giản như implied yield curve cộng FX forward; đường cong dựng ra cần tách chi phí thanh khoản và base curve để cho BU động lực đúng [[src-choudhry-principles-banking#^choudhry-ifc-22]].
- **Đổi đồng tiền trong vòng đời.** Khoản vay cơ cấu lại đồng tiền nhận nợ thì chấm dứt COF trên tài khoản cũ và tính COF trên tài khoản đồng tiền mới [[src-vab-ftp#^vab-ftp-97]].
- **Chưa có nguồn.** Trần lãi suất huy động USD và tỷ lệ DTBB theo đồng tiền của NHNN chưa có source note; VAB chỉ dẫn TT30/2019 (dự trữ bắt buộc) và TT24/2014 (bảo hiểm tiền gửi) là văn bản liên quan [[src-vab-ftp#^vab-ftp-78]]. [cần nguồn]

### Q3 — Loại sản phẩm

Nguồn duy nhất cho ma trận gán là VAB (T4, `draft`). "Cơ sở" là COF hoặc VOF cơ sở lấy từ biểu của đồng tiền và sản phẩm.

**Tiền gửi (VOF)**

| Sản phẩm | Kỳ hạn tính VOF cơ sở | TLP | Nguồn |
|---|---|---|---|
| Có kỳ hạn TT1, gốc trả cuối kỳ (cố định hoặc thả nổi) | Kỳ hạn gốc theo biểu tại ngày phát sinh, cố định suốt thời gian gửi | Bằng 0 | [[src-vab-ftp#^vab-ftp-71]] |
| Gửi góp | Lãi suất huy động gửi góp theo kỳ hạn cộng chênh lệch giữa VOF và lãi suất huy động của tiền gửi gốc trả cuối kỳ cùng kỳ hạn | Bằng 0 | [[src-vab-ftp#^vab-ftp-72]] |
| Có kỳ hạn tái tục | Như tiền gửi phát sinh mới, dùng biểu cập nhật tại thời điểm tái tục, cố định suốt thời gian gửi | Không nêu | [[src-vab-ftp#^vab-ftp-95]] |
| Rút trước hạn | VOF cơ sở theo VOF của tiền gửi KKH thông thường | Không nêu | [[src-vab-ftp#^vab-ftp-18]] |
| KKH (CASA) có mô hình hành vi | Trung bình có trọng số hai điểm kỳ hạn theo tỷ lệ không ổn định: Base Curve = Base Curve_i × Non-CoreCasa_i + Base Curve_j × (1 − Non-CoreCasa_i) | Không nêu | [[src-vab-ftp#^vab-ftp-15]] |
| KKH chưa có mô hình hành vi | VOF = VOF KKH × a% + VOF CKH × (1 − a%); a% không nhỏ hơn 15%; VOF CKH là VOF kỳ hạn 2 tháng hoặc theo ALCO phê duyệt | Không nêu | [[src-vab-ftp#^vab-ftp-16]] [[src-vab-ftp#^vab-ftp-44]] |
| Tiền gửi tại TCTD khác (Nostro, gồm tiền gửi tại NHNN) | Không mua bán vốn FTP với CFU vì đã được tính chi phí TSTK | — | [[src-vab-ftp#^vab-ftp-55]] |
| Vostro | VOF cơ sở TT2 kỳ hạn qua đêm, cố định suốt giao dịch | Bằng 0 | [[src-vab-ftp#^vab-ftp-56]] |

**Cho vay (COF)**

| Sản phẩm | Kỳ hạn tính COF cơ sở | TLP | Nguồn |
|---|---|---|---|
| Gốc trả cuối kỳ, lãi suất cố định | Kỳ hạn gốc (ngày đáo hạn trừ ngày giải ngân) theo biểu tại ngày giải ngân | Không nêu | [[src-vab-ftp#^vab-ftp-32]] |
| Gốc trả định kỳ, lãi suất cố định | Kỳ hạn hiệu lực, bình quân gia quyền theo lịch trả gốc, áp suốt thời gian cho vay | Bằng 0 | [[src-vab-ftp#^vab-ftp-73]] |
| Gốc trả cuối kỳ, lãi suất thả nổi | Kỳ tái định giá, áp đến ngày điều chỉnh tiếp theo | Lãi suất kỳ hạn gốc trừ lãi suất kỳ tái định giá | [[src-vab-ftp#^vab-ftp-86]] |
| Gốc trả định kỳ, lãi suất thả nổi | Kỳ tái định giá | Lãi suất kỳ hạn hiệu lực trừ lãi suất kỳ tái định giá | [[src-vab-ftp#^vab-ftp-87]] |
| Trả trước hạn | Kỳ hạn hiệu lực tính từ dòng tiền của mô hình hành vi trả trước hạn, bằng bình quân gia quyền | Không nêu | [[src-vab-ftp#^vab-ftp-19]] [[src-vab-ftp#^vab-ftp-20]] |
| Quá hạn | Kỳ hạn của khoản vay thông thường trước khi chuyển quá hạn, trên số dư tại thời điểm quá hạn, cố định suốt thời gian quá hạn | Theo tính chất dòng tiền trước quá hạn | [[src-vab-ftp#^vab-ftp-74]] |
| Gia hạn | Kỳ hạn gốc mới (kỳ hạn gốc trước gia hạn cộng thời gian gia hạn) hoặc theo kỳ điều chỉnh lãi suất, tuỳ tính chất dòng tiền | Theo tính chất dòng tiền | [[src-vab-ftp#^vab-ftp-75]] |
| Không tiêu chuẩn (ưu đãi), gốc cuối kỳ, lãi suất cố định | Phương án 1: giữ kỳ hạn gốc, chỉ đổi FTP khi hết ưu đãi. Phương án 2: tách kỳ ưu đãi và ngoài ưu đãi (ví dụ năm đầu giá 1 năm, 4 năm sau giá 4 năm) | Bằng 0 | [[src-vab-ftp#^vab-ftp-76]] |
| Ưu đãi, gốc cuối kỳ, thả nổi | Trong kỳ ưu đãi: COF theo kỳ ưu đãi, cố định; ngoài kỳ ưu đãi: theo kỳ tái định giá sau ngày kết thúc ưu đãi | Trong kỳ ưu đãi bằng 0; ngoài kỳ ưu đãi theo kỳ hạn gốc sau ưu đãi | [[src-vab-ftp#^vab-ftp-88]] |
| Ưu đãi, gốc trả định kỳ, cố định | Hai phương án như trên; ngoài kỳ ưu đãi dùng kỳ hạn hiệu lực sau ưu đãi | Bằng 0 | [[src-vab-ftp#^vab-ftp-89]] |
| Ưu đãi, gốc trả định kỳ, thả nổi | Hai phương án; ngoài kỳ ưu đãi theo kỳ tái định giá sau ưu đãi | Kỳ hạn hiệu lực sau ưu đãi trừ kỳ tái định giá | [[src-vab-ftp#^vab-ftp-90]] |
| Hạn mức chưa sử dụng (thẻ tín dụng, thấu chi, cho vay hạn mức) | Phần bù rủi ro thanh khoản tiềm tàng | — | [[src-vab-ftp#^vab-ftp-35]] [[src-vab-ftp#^vab-ftp-68]] |

Phần bù rủi ro thanh khoản tiềm tàng có công thức C × P% × tỷ lệ dự trữ thanh khoản × chi phí duy trì TSTK khi có mô hình hành vi giải ngân, hoặc C × CCF × … khi chưa có [[src-vab-ftp#^vab-ftp-69]].

**Đầu tư và khoản mục khác**

| Khoản mục | Cách tính | Nguồn |
|---|---|---|
| Trái phiếu doanh nghiệp giữ đến đáo hạn | COF cơ sở như khoản vay gốc trả cuối kỳ (cố định hoặc thả nổi) | [[src-vab-ftp#^vab-ftp-77]] |
| Trái phiếu doanh nghiệp nắm giữ kinh doanh hoặc AFS | COF cơ sở TT1 theo kỳ hạn từ mô hình hành vi; chưa có mô hình thì áp như cho vay với kỳ hạn theo quy tắc phân tách sổ kinh doanh của TT41/2016 | [[src-vab-ftp#^vab-ftp-77]] |
| Cổ phiếu đầu tư dài hạn (chiến lược) | COF cơ sở TT1 theo kỳ hạn nắm giữ dự kiến; chưa xác định được thì theo kỳ hạn nhận cổ tức hằng năm hoặc dải trên 5 năm | [[src-vab-ftp#^vab-ftp-91]] |
| Tài sản nợ và tài sản có khác | Không tính FTP trong cách tiếp cận mua bán một phần bảng cân đối, được tài trợ bằng VCSH | [[src-vab-ftp#^vab-ftp-92]] |
| Giao dịch liên ngân hàng khối QL&KDV | Phương án 1 áp cho trạng thái ròng từng desk, lãi suất TT2 theo kỳ hạn nhu cầu cân đối vốn của desk | [[src-vab-ftp#^vab-ftp-60]] |

**Quyền chọn ẩn.** Tata nêu FTP rate nên điều chỉnh mark-up cho short optionality và discount cho long optionality, và nhận xét embedded options dựa trên giả định hành vi khó định giá bằng mô hình chuẩn [[src-tata-bank-alm#^tata-ftp-27]] [[src-tata-bank-alm#^tata-ftp-28]]. Lubinska nêu CASA gồm phần biến động tái định giá qua đêm và phần ổn định; phần lõi coi như nguồn dài hạn lãi suất 0% [[src-lubinska-alm-optimisation#^lubinska-u04-1]].

**Thấu chi core / non-core.** Chưa có nguồn đã ingest cho cách tách kỳ hạn. [cần nguồn]

### Q4 — Từ base curve đến FTP rate cuối cùng

**Công thức (VAB).**
- VOF = Base Curve + Margin + ALCO Adjust [[src-vab-ftp#^vab-ftp-6]].
- COF = Base Curve + Margin + Chi phí DTBB + Chi phí BHTG + Liquidity Premium + TLP + ALCO Adjust [[src-vab-ftp#^vab-ftp-7]].

| Cấu phần | Nội dung và cách xác định | Nguồn |
|---|---|---|
| Base curve | Theo đồng tiền và kỳ hạn (mục Q1, Q2) | [[src-vab-ftp#^vab-ftp-27]] |
| Margin hỗ trợ huy động | Phần ALCO dùng để tạo động lực cho đơn vị huy động vốn; tính vào đầu năm, tính riêng theo đồng tiền; đầu vào gồm NII kế hoạch từ vay và gửi, chi phí quản lý và chi phí dự phòng năm kế hoạch | [[src-vab-ftp#^vab-ftp-25]] [[src-vab-ftp#^vab-ftp-80]] |
| Chi phí BHTG | Phí bảo hiểm tiền gửi theo quy định NHNN, VAB ghi 0,15% năm trên số dư tiền gửi VND của cá nhân (mốc "hiện tại" của VAB không rõ ngày) | [[src-vab-ftp#^vab-ftp-8]] |
| Chi phí DTBB | Chi phí cơ hội của tiền gửi dự trữ tại NHNN | [[src-vab-ftp#^vab-ftp-9]] |
| Phần bù TSTK | Chi phí duy trì danh mục tài sản thanh khoản | [[src-vab-ftp#^vab-ftp-10]] |
| TLP | Chi phí thanh khoản dài hạn, phần bù cấu trúc cộng vào lãi suất cơ sở; công thức = lãi suất kỳ hạn gốc trừ lãi suất kỳ tái định giá | [[src-vab-ftp#^vab-ftp-23]] [[src-vab-ftp#^vab-ftp-33]] [[src-vab-ftp#^vab-ftp-46]] |
| Điều chỉnh ALCO (tài sản nợ) | Mức cộng thêm vào giá mua vốn để điều tiết hành vi BU theo chiến lược huy động | [[src-vab-ftp#^vab-ftp-63]] |
| Điều chỉnh ALCO (cho vay) | Mức cộng hoặc trừ vào COF theo chiến lược cho vay; có thể khớp hoặc không khớp với điều chỉnh bên nợ | [[src-vab-ftp#^vab-ftp-64]] |
| Chi phí vốn chủ sở hữu | Khi áp RAROC: (ROE% − COF%) × vốn RAROC dự kiến × WAT/365 | [[src-vab-ftp#^vab-ftp-67]] |

Mẫu số của các tỷ lệ BHTG, DTBB, phần bù TSTK là bình quân 3 tháng của tổng tài sản bị tính FTP, bằng tổng tài sản trừ tài sản thanh khoản, tài sản ghi nhận cho Khối QL&KDV và tài sản có khác [[src-vab-ftp#^vab-ftp-81]]. Chi tiết cấu phần xem [[ftp-balance-sheet-risk-and-cost-components]].

**Từ FTP rate đến margin.** FTP rate là giá tham chiếu cho giao dịch mới, và là cơ sở tính gross margin, net margin (sau expected loss và dự phòng) và SVA [[src-choudhry-principles-banking#^choudhry-ifc-10]]. Với tiền gửi, gross margin là FTP rate trừ lãi suất tiền gửi [[src-choudhry-principles-banking#^choudhry-ifc-11]]. VAB định nghĩa NIM là chênh lệch lãi suất cho vay với giá FTP bán vốn, và giá FTP mua vốn với lãi suất huy động [[src-vab-ftp#^vab-ftp-40]].

**Hai tầng trong ví dụ của Tata.** Khoản vay 2 năm cố định lãi suất 1 năm đầu rồi tái định giá có FTP rate = 1,6% rủi ro lãi suất + 80 bp liquidity premium = 2,4% [[src-tata-bank-alm#^tata-ftp-14]]. Ví dụ khác: tiền gửi 1 năm 1% so với FTP 1 năm 2%, khoản vay 2 năm 4% so với FTP 2 năm 3%; chênh lệch giữa điểm 1 năm và 2 năm trên curve là structural contribution [[src-tata-bank-alm#^tata-ftp-9]].

**Cost centre hay profit centre.** Lãi suất chuyển giao thường bằng COF nội bộ của Treasury, có thể cộng spread bù chi phí vận hành [[src-choudhry-principles-banking#^choudhry-mo-3]].

### Q5 — Rà soát, phê duyệt và thay đổi

**Chu kỳ rà soát (VAB).** Base curve, BHTG, DTBB, phần bù TSTK, TLP, điều chỉnh ALCO rà soát hằng quý; hỗ trợ huy động rà soát hằng năm hoặc khi kế hoạch kinh doanh thay đổi. Mọi cấu phần bắt buộc, trừ điều chỉnh ALCO [[src-vab-ftp#^vab-ftp-65]].

**Quy trình TT1.** Định kỳ hằng quý hoặc khi thị trường biến động lớn, bộ phận quản lý FTP đề xuất cập nhật biểu; khối CNTT chiết xuất dữ liệu [[src-vab-ftp#^vab-ftp-49]]. Trưởng bộ phận quản lý FTP kiểm soát, trình ALCO tham mưu Tổng giám đốc phê duyệt và ban hành [[src-vab-ftp#^vab-ftp-50]].

**Quy trình TT2.** Biểu FTP TT2 tính hằng ngày [[src-vab-ftp#^vab-ftp-52]], ALCO thông qua danh sách ngân hàng peer ít nhất mỗi năm một lần [[src-vab-ftp#^vab-ftp-57]].

**Điều chỉnh thủ công.** ALCO xem xét cho phép khi có sai sót tính toán, hoặc khi luật, quy định hay biến động thị trường làm giá biến động trên dưới ±0,2% so với giá FTP hiện tại [[src-vab-ftp#^vab-ftp-94]].

**Khoá giá trong vòng đời.** Tiền gửi TT1 và khoản vay cố định có FTP cố định suốt thời gian giao dịch (mục Q3). Choudhry cho cùng kết quả: FTP rate cố định theo kỳ hạn trùng khớp nên commercial margin không đổi trước thay đổi đường cong sau đó [[src-choudhry-principles-banking#^choudhry-ftp-8]].

**Tính lại khi có sự kiện.**

| Sự kiện | Xử lý | Nguồn |
|---|---|---|
| Tiền gửi đổi tần suất xác định lãi suất | Tính lại VOF theo tần suất mới và VOF cơ sở, áp từ ngày thay đổi | [[src-vab-ftp#^vab-ftp-93]] |
| Tiền gửi tái tục | Xác định như tiền gửi phát sinh mới | [[src-vab-ftp#^vab-ftp-95]] |
| Khoản vay đổi tần suất hoặc lịch trả gốc | Tính lại COF vào ngày thay đổi | [[src-vab-ftp#^vab-ftp-96]] |
| Khoản vay đổi loại hình lãi suất, đồng tiền hoặc hình thức trả gốc | COF mới xác định tại ngày thay đổi; đổi đồng tiền thì chấm dứt COF tài khoản cũ | [[src-vab-ftp#^vab-ftp-97]] |

**Kỳ tính và báo cáo.** Kỳ tính FTP hằng tháng theo một trong hai phương án: từ ngày 25 tháng trước đến hết ngày 25 tháng hiện tại, hoặc từ đầu đến cuối tháng [[src-vab-ftp#^vab-ftp-98]]. Báo cáo NII/NIM cấp đơn vị kinh doanh và cụm chi nhánh lập hằng ngày cho mọi loại tiền [[src-vab-ftp#^vab-ftp-99]].

**Vai trò quản trị.** Nguyên tắc gán kỳ hạn trên curve cho một loại giao dịch không được do đơn vị thực hiện giao dịch quyết định [[src-bardaeva-alm#^ch11-11]]. ALM xác định nguyên tắc định giá điều chuyển và dựng curve FTP [[src-bardaeva-alm#^ch11-5]]. Điều chỉnh độ dốc curve hoặc áp steering margin để khuyến khích huy động và hạn chế cho vay [[src-bardaeva-alm#^ch15-8]]. Tata nhận định chức năng steering mang tính chính trị cao vì FTP là nguồn sự thật duy nhất về giá trị gia tăng của từng khối [[src-tata-bank-alm#^tata-ftp-17]].

## Bằng chứng ủng hộ

- Nguyên tắc matched maturity xuất hiện ở ba nguồn T4 độc lập: Choudhry [[src-choudhry-principles-banking#^choudhry-ftp-6]], Tata [[src-tata-bank-alm#^tata-ftp-8]] và VAB [[src-vab-ftp#^vab-ftp-32]].
- Tách rủi ro lãi suất khỏi liquidity premium khi định giá khoản vay thả nổi có hai nguồn: Tata [[src-tata-bank-alm#^tata-ftp-14]] và VAB [[src-vab-ftp#^vab-ftp-86]].
- Ma trận gán theo sản phẩm, base curve VND/USD, thang kỳ hạn và quy trình vận hành chỉ có VAB (một nguồn tư vấn T4, `draft`).

## Bằng chứng trái chiều

- **Cost approach và marginality.** Choudhry nêu nguyên tắc cận biên: chi phí đã phát sinh của nguồn vốn hiện có không liên quan tới định giá khoản vay mới [[src-choudhry-principles-banking#^choudhry-ftp-12]], và cost approach phản ứng trễ [[src-choudhry-principles-banking#^choudhry-ifc-17]]. Base curve VND của VAB lấy lãi suất huy động thực tế bình quân 3 tháng [[src-vab-ftp#^vab-ftp-28]]. Đây là khác biệt thiết kế, không phải conflict, vì VAB dựng biểu theo chu kỳ rà soát hằng quý và có điều chỉnh ALCO.
- **TLP chỉ cho khoản vay thả nổi hay mọi sản phẩm.** VAB nói TLP chỉ áp dụng cho khoản vay thả nổi [[src-vab-ftp#^vab-ftp-12]] nhưng cũng nêu TLP theo tính chất dòng tiền cho khoản quá hạn và gia hạn [[src-vab-ftp#^vab-ftp-74]] [[src-vab-ftp#^vab-ftp-75]]. Tata tách FTP thành hai cấu phần cho sản phẩm có kỳ hạn chỉ số lãi suất khác kỳ hạn hợp đồng [[src-tata-bank-alm#^tata-ftp-14]]. Phạm vi áp dụng TLP chưa thống nhất giữa các claim của VAB.
- **Tần suất cập nhật biểu TT1.** Các claim của VAB ghi "hằng quý" ở cột thời gian [[src-vab-ftp#^vab-ftp-49]] nhưng bước 3 và 5 của quy trình ghi ban hành "Giải pháp FTP hàng tháng" [[src-vab-ftp#^vab-ftp-50]]. Conflict nội bộ này đã được ghi ở [[ftp-pricing-methodology]]; cụm này giữ cả hai.

## Phụ thuộc regime

- **Thị trường phát triển và mới nổi.** Thị trường phát triển có nhiều chỉ báo để dựng curve, curve phải áp dụng được cho sản phẩm có quyền chọn ẩn; thị trường mới nổi hạn chế hơn, có thể dùng implied yield curve cộng FX forward [[src-choudhry-principles-banking#^choudhry-ifc-22]].
- **Ngân hàng lớn và nhỏ.** Ngân hàng thị phần lớn cần mô hình thống kê cho kỳ hạn và giá của sản phẩm không xác định kỳ hạn; ngân hàng nhỏ có thể học nguyên tắc từ ngân hàng khác và tính tay từng giao dịch [[src-choudhry-principles-banking#^choudhry-ifc-21]].
- **Thị trường ổn định.** Cost approach hợp thị trường biến động lãi suất thấp, cấu trúc nợ đa dạng theo kỳ hạn [[src-choudhry-principles-banking#^choudhry-ifc-17]].
- **Ngân hàng chỉ huy động tiền gửi.** Ngân hàng không phát hành wholesale có thể nới một số nguyên tắc EBA [[src-choudhry-principles-banking#^choudhry-ifc-15]].
- Nguồn đã ingest chưa phân tích cách các quy tắc trên đổi theo chiều lãi suất tăng hay giảm. [cần nguồn]

## Hàm ý ALM / quy định

- **Nghĩa vụ tại VN (T1).** TT83/2025, hiệu lực từ 2026-07-01 [[src-tt83-2025-nhnn#^d74-1]], yêu cầu ngân hàng phải xác định chi phí đáp ứng nhu cầu thanh khoản và rủi ro thanh khoản trong định giá vốn nội bộ (Đ45.1.b) [[src-tt83-2025-nhnn#^d45-1b]]. Bộ phận ALM rà soát, đề xuất nguyên tắc xây dựng giá điều chuyển vốn nội bộ (Đ25.3.b) [[src-tt83-2025-nhnn#^d25-3]]. Wiki chưa có quy định NHNN đặt yêu cầu cho cách dựng curve, thang kỳ hạn, đồng tiền hay ma trận sản phẩm.
- **Tham chiếu Basel (không phải nghĩa vụ tại VN).** BCBS 144 P4 chỉ nói liquidity charge theo vị thế, danh mục hoặc giao dịch, kể cả cam kết tiềm tàng [[src-bcbs-liquidity-principles-2008#^lrm-19]]. Wiki chưa có chuẩn BCBS về dựng FTP curve.
- **Tài liệu VN.** VAB là nguồn duy nhất cho thang kỳ hạn, base curve VND/USD, ma trận sản phẩm và quy trình; VAB dẫn TT22/2019, TT24/2014 và TT30/2019 là văn bản liên quan [[src-vab-ftp#^vab-ftp-78]], và TT41/2016 cho quy tắc phân tách sổ kinh doanh [[src-vab-ftp#^vab-ftp-77]].
- *Diễn giải:* nếu hai yêu cầu TT83 là phần duy nhất của nghĩa vụ NHNN về FTP, thì thang kỳ hạn, nguồn dữ liệu và gán kỳ hạn theo sản phẩm là quyết định thiết kế nội bộ của ngân hàng, có tham chiếu Choudhry, Tata và VAB. ALCO duyệt các quyết định này (xem [[alco]]). (ngoài wiki, chưa có nguồn)

## Bất định

- [cần nguồn] Công thức implied yield và FX forward cho synthetic curve; công thức bị mất khi convert từ Choudhry Ch14. Bổ sung công thức từ file gốc trước khi dùng.
- [cần nguồn] Văn bản NHNN về trần lãi suất huy động USD và tỷ lệ DTBB theo đồng tiền (TT30/2019 chưa có source note).
- [cần nguồn] Cách tách kỳ hạn cho thấu chi core / non-core.
- [cần nguồn] Premium cho quyền chọn trong FTP rate; Tata nêu hướng mark-up/discount nhưng không đưa công thức.
- Thang kỳ hạn chuẩn đầy đủ của VAB nằm ở MB01, chưa có claim liệt kê các kỳ hạn; ví dụ chỉ nêu 14D, 21D (USD), 24M [[src-vab-ftp#^vab-ftp-82]].
- Các claim về TT22/2019 trong VAB (đệm TSTK, tỷ lệ rút KKH 15%) chưa được đối chiếu với TT50/2026, thay TT22/2019 cho NHTM và chi nhánh NHNNg từ 2026-10-01 [[src-tt50-2026-nhnn#^d37-3a]].
- Bước 3 chưa đọc raw: mọi claim lấy từ source note đã ingest; trích nguyên văn đã khớp lint.
