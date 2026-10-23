---
title: "FTP phản ánh và định giá những rủi ro, chi phí nào trên bảng cân đối"
aliases: [FTP: rủi ro và chi phí được phản ánh trên bảng cân đối, FTP risk and cost components on the balance sheet]
type: synthesis
domains: [alm, product, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "FTP phản ánh và định giá những loại rủi ro/chi phí nào trên bảng cân đối, đặc biệt là funding cost, liquidity risk, interest rate risk và optionality? · (Q1) funding cost · (Q2) liquidity risk · (Q3) interest rate risk · (Q4) optionality · (Q5) FTP không định giá những rủi ro nào"
as_of: 2026-10-22
sources: ["[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-bardaeva-alm]]", "[[src-tata-bank-alm]]", "[[src-bcbs-liquidity-principles-2008]]", "[[src-tt83-2025-nhnn]]", "[[src-tt50-2026-nhnn]]", "[[src-ftp-transmission-analysis]]"]
relations: []
# relations — synthesis: luôn để trống; synthesis không làm chủ thể hay đích của relation. Quan hệ khai ở node tri thức (chủ thể A); thân bài trình bày chuỗi quan hệ trong `## Cơ chế`. Xem 03_meta/taxonomy.md, mục "Relation"
tags: [ftp, funding-cost, liquidity, irrbb, embedded-options, balance-sheet]
updated: 2026-10-22
reviewed:
---

## Câu hỏi

- Q1. FTP phản ánh và định giá funding cost nào trên bảng cân đối?
- Q2. FTP phản ánh và định giá liquidity risk nào?
- Q3. FTP phản ánh và định giá interest rate risk nào?
- Q4. FTP phản ánh và định giá optionality nào?
- Q5. FTP không định giá những rủi ro nào, và ranh giới nằm ở đâu?

Câu gốc của user: "FTP phản ánh và định giá những loại rủi ro/chi phí nào trên bảng cân đối, đặc biệt là funding cost, liquidity risk, interest rate risk và optionality?" Một cụm, không hub. Synthesis [[ftp-purpose-and-balance-sheet-problems]] đã trả lời FTP là gì và giải quyết vấn đề gì; cụm này chỉ đi vào các cấu phần. Node nền: [[funds-transfer-pricing]], [[liquidity-transfer-pricing]], [[internal-funding-curve]], [[ftp-pricing-methodology]], [[cost-of-funds]] (đều `draft`). Mốc as_of 2026-10-22.

## Kết luận

Nguồn T4 đã ingest cho thấy FTP trực tiếp phản ánh ba nhóm: chi phí vốn đầu vào, chi phí thanh khoản và rủi ro lãi suất. Optionality được phản ánh gián tiếp qua kỳ hạn hiệu lực và tỷ lệ hành vi, chưa thấy nguồn T3/T4 định giá quyền chọn bằng premium. Rủi ro tín dụng của khách hàng nằm ngoài FTP [[src-lubinska-alm-optimisation#^lubinska-u01-8]]. Phía VN chỉ có tài liệu tư vấn VAB (T4, `draft`) cho cấu phần; TT83/2025 mới đặt yêu cầu ở mức nguyên tắc [[src-tt83-2025-nhnn#^d45-1b]].

**Q1 — funding cost.** VAB yêu cầu lãi suất FTP phản ánh đủ chi phí vốn đầu vào: lãi suất huy động, chi phí bảo hiểm tiền gửi và chi phí quản lý huy động [[src-vab-ftp#^vab-ftp-5]]. Giá mua vốn VOF gồm base curve, margin hỗ trợ huy động và điều chỉnh ALCO [[src-vab-ftp#^vab-ftp-6]]. Giá bán vốn COF thêm chi phí DTBB, chi phí BHTG, phần bù tài sản thanh khoản và TLP [[src-vab-ftp#^vab-ftp-7]]. Base curve dựng theo một trong bốn cách: market, cost, mixed, marginal [[src-choudhry-principles-banking#^choudhry-ifc-16]].

**Q2 — liquidity risk.** Liquidity FTP là lớp cộng thêm vào FTP lãi suất cổ điển, sau khi chênh lệch chi phí huy động của ngân hàng nới rộng [[src-choudhry-principles-banking#^choudhry-ftp-14]]. VAB có ba cấu phần thanh khoản:

- phần bù tài sản thanh khoản (chi phí duy trì đệm) [[src-vab-ftp#^vab-ftp-10]];
- TLP [[src-vab-ftp#^vab-ftp-11]];
- phần bù rủi ro thanh khoản tiềm tàng cho hạn mức chưa sử dụng [[src-vab-ftp#^vab-ftp-68]].

Chi phí DTBB được xếp vào chi phí pháp định ở Q1. Basel (tham chiếu) và TT83/2025 (nghĩa vụ VN) đều yêu cầu đưa chi phí thanh khoản vào định giá nội bộ [[src-bcbs-liquidity-principles-2008#^lrm-p04]] [[src-tt83-2025-nhnn#^d45-1b]].

Tata (T4) bổ sung hai chi phí quy định: chi phí HQLA bổ sung cho LCR có lẽ nên được tính vào transfer price [[src-tata-bank-alm#^tata-ftp-20]], và vị thế làm xấu NSFR nên bị phạt trên FTP curve [[src-tata-bank-alm#^tata-ftp-22]]. Chi phí contingency liquidity được cộng vào FTP rate [[src-tata-bank-alm#^tata-ftp-26]]. Tata không nêu công thức hay mức phí.

**Q3 — interest rate risk.** FTP tách rủi ro lãi suất và rủi ro funding khỏi BU và chuyển về ALM [[src-lubinska-alm-optimisation#^lubinska-u01-7]]. Cơ chế là trùng khớp kỳ hạn: lãi suất FTP cố định cùng kỳ hạn, đồng tiền, cơ sở lãi suất với lãi suất khách hàng, nên commercial margin không đổi trước thay đổi đường cong sau đó [[src-choudhry-principles-banking#^choudhry-ftp-8]]. Với khoản vay thả nổi, VAB định COF cơ sở theo kỳ tái định giá và đặt TLP bằng chênh lệch giữa kỳ hạn gốc và kỳ tái định giá [[src-vab-ftp#^vab-ftp-86]]. Phần chênh lệch kỳ hạn và lãi suất còn lại nằm ở ALM [[src-lubinska-alm-optimisation#^lubinska-u01-13]].

**Q4 — optionality.** VAB phản ánh hai quyền chọn hành vi bằng cách đổi kỳ hạn tính giá. Các claim VAB đã ingest không nêu premium. Tiền gửi rút trước hạn nhận VOF cơ sở của tiền gửi không kỳ hạn thông thường [[src-vab-ftp#^vab-ftp-18]]. Khoản vay trả trước hạn nhận COF cơ sở theo kỳ hạn hiệu lực lấy từ dòng tiền của mô hình hành vi [[src-vab-ftp#^vab-ftp-19]]. Tiền gửi không kỳ hạn (CASA) tách thành phần không ổn định và phần ổn định theo tỷ lệ của mô hình hành vi [[src-vab-ftp#^vab-ftp-15]]. Giá của quyền chọn như một khoản premium: [cần nguồn].

**Q5 — ranh giới.** Rủi ro tín dụng theo định nghĩa không chuyển về ALM [[src-lubinska-alm-optimisation#^lubinska-u01-8]]. Expected loss, dự phòng và chi phí vốn cổ phần được tính sau lãi suất FTP, trong net margin và SVA [[src-choudhry-principles-banking#^choudhry-ifc-10]]. Rủi ro không phòng ngừa ra thị trường được cũng nằm ngoài chuyển giao, khi FTP thiết lập sai hoặc thị trường phái sinh kém thanh khoản [[src-lubinska-alm-optimisation#^lubinska-u01-8]].

## Cơ chế

Viết tắt: BU (business unit, đơn vị kinh doanh); DTBB (dự trữ bắt buộc); BHTG (bảo hiểm tiền gửi); TSTK (tài sản thanh khoản); VCSH (vốn chủ sở hữu); VOF (giá mua vốn, Value of Funds); COF (giá bán vốn, Cost of Funds); TLP (Term Liquidity Premium).

### Bảng tổng hợp: cấu phần FTP và rủi ro/chi phí tương ứng (Q1–Q4)

| Cấu phần | Rủi ro / chi phí phản ánh | Áp cho | Nguồn |
|---|---|---|---|
| Base curve | Chi phí vốn theo kỳ hạn | VOF và COF | [[src-vab-ftp#^vab-ftp-6]] [[src-vab-ftp#^vab-ftp-7]] |
| Margin hỗ trợ huy động | Phần ALCO dùng để tạo động lực cho đơn vị huy động vốn | VOF và COF | [[src-vab-ftp#^vab-ftp-80]] |
| Chi phí BHTG | Phí bảo hiểm tiền gửi | COF | [[src-vab-ftp#^vab-ftp-8]] |
| Chi phí DTBB | Chi phí cơ hội của tiền gửi dự trữ tại NHNN | COF | [[src-vab-ftp#^vab-ftp-9]] |
| Phần bù tài sản thanh khoản | Chi phí duy trì danh mục đệm thanh khoản | COF | [[src-vab-ftp#^vab-ftp-10]] |
| TLP | Chi phí thanh khoản dài hạn (kèm rủi ro tín dụng riêng của ngân hàng); chỉ áp cho khoản vay thả nổi | COF | [[src-vab-ftp#^vab-ftp-11]] [[src-vab-ftp#^vab-ftp-12]] |
| Phần bù rủi ro thanh khoản tiềm tàng | Chi phí đệm cho hạn mức chưa sử dụng | COF của phần hạn mức chưa sử dụng | [[src-vab-ftp#^vab-ftp-68]] |
| Chi phí LCR / NSFR (hướng của Tata, chưa có tham số) | Chi phí HQLA bổ sung; chi phí tài trợ dài hạn do vị thế làm xấu NSFR | Vị thế kích hoạt yêu cầu | [[src-tata-bank-alm#^tata-ftp-20]] [[src-tata-bank-alm#^tata-ftp-22]] |
| Điều chỉnh ALCO | Điều tiết hành vi BU theo chiến lược từng thời kỳ | VOF và COF | [[src-vab-ftp#^vab-ftp-63]] [[src-vab-ftp#^vab-ftp-64]] |
| Chi phí vốn chủ sở hữu | Chi phí vốn cổ phần cho phần tài sản tài trợ bằng VCSH | Khi áp RAROC | [[src-vab-ftp#^vab-ftp-67]] |
| Kỳ hạn hiệu lực / tỷ lệ hành vi | Optionality (prepayment, rút trước hạn, CASA) | Chọn điểm kỳ hạn trên base curve | [[src-vab-ftp#^vab-ftp-15]] [[src-vab-ftp#^vab-ftp-19]] |

### Q1 — Funding cost

- **Base curve có bốn cách dựng.** Cost approach dựa trên lãi suất huy động; market approach dựa trên lãi suất thị trường; mixed approach pha hai đường cong; marginal approach bổ sung sau, theo hướng dẫn của cơ quan quản lý [[src-choudhry-principles-banking#^choudhry-ifc-16]]. Marginal approach gồm cấu phần thị trường cho chi phí vốn ngắn hạn cơ sở cộng spread riêng của ngân hàng phản ánh chi phí thanh khoản theo kỳ hạn [[src-choudhry-principles-banking#^choudhry-ifc-20]].
- **VAB dùng chi phí thực tế cho VND.** Base curve VND trong ví dụ của VAB lấy lãi suất huy động thực tế bình quân theo kỳ hạn [[src-vab-ftp#^vab-ftp-82]].
- **Nguyên tắc cận biên.** Chi phí đã phát sinh của nguồn vốn hiện có không liên quan tới định giá khoản vay mới [[src-choudhry-principles-banking#^choudhry-ftp-12]]. EBA Guidelines (10/2010) nêu giá nội bộ nên phản ánh chi phí vốn cận biên [[src-choudhry-principles-banking#^choudhry-ifc-15]].
- **Chi phí pháp định.** Chi phí BHTG là khoản ngân hàng nộp cho tổ chức BHTG theo quy định NHNN, được VAB ghi ở mức 0,15% năm trên số dư tiền gửi VND của cá nhân (mốc "hiện tại" của tài liệu VAB không rõ ngày) [[src-vab-ftp#^vab-ftp-8]]. Chi phí DTBB là khoản chênh giữa VOF bình quân và lãi suất tiền gửi DTBB tại NHNN [[src-vab-ftp#^vab-ftp-9]]. Cả hai được chia cho bình quân tổng tài sản bị tính FTP, tính bình quân 3 tháng [[src-vab-ftp#^vab-ftp-81]].
- **Hệ quả của sai funding cost.** Ước lượng thấp chi phí vốn khiến BU cho vay rẻ và tăng nguồn vốn vì tưởng có lãi; ước lượng cao khiến BU đòi lãi suất khách hàng cao [[src-lubinska-alm-optimisation#^lubinska-u04-2]].
- **Cost centre hay profit centre.** Lãi suất chuyển giao thường bằng COF nội bộ của Treasury, có thể cộng spread bù chi phí vận hành [[src-choudhry-principles-banking#^choudhry-mo-3]].

### Q2 — Liquidity risk

- **Phần bù tài sản thanh khoản.** Thể hiện chi phí duy trì danh mục tài sản thanh khoản đáp ứng yêu cầu thanh khoản theo quy định NHNN, quy định nội bộ hoặc luật định [[src-vab-ftp#^vab-ftp-10]]. Danh mục TSTK theo Phụ lục 3 TT22/2019 [[src-vab-ftp#^vab-ftp-43]]. Ví dụ tính toán nằm ở [[src-vab-ftp#^vab-ftp-45]].
- **TLP.** Phản ánh sự kết hợp giữa rủi ro tín dụng riêng của ngân hàng và phần bù thanh khoản kỳ hạn phổ biến trên thị trường [[src-vab-ftp#^vab-ftp-11]]. Choudhry dựng TLP curve từ giá nợ đã phát hành của chính ngân hàng bằng quy trình no-arbitrage 4 bước [[src-choudhry-principles-banking#^choudhry-ifc-4]].
- **Liquidity premium theo kỳ hạn.** Trong case Europe Arab Bank, FTP Libor-flat tạo rủi ro thanh khoản dư thừa khi ngân hàng huy động cao hơn Libor [[src-choudhry-principles-banking#^choudhry-cs-3]]. Chế độ FTP mới của Europe Arab Bank thêm liquidity premium tăng theo kỳ hạn [[src-choudhry-principles-banking#^choudhry-cs-4]].
- **Rủi ro thanh khoản tiềm tàng.** Giá FTP bán vốn cho phần hạn mức chưa sử dụng của thẻ tín dụng, thấu chi và cho vay hạn mức bằng chính phần bù rủi ro thanh khoản tiềm tàng [[src-vab-ftp#^vab-ftp-68]]. Công thức: C × P% × tỷ lệ dự trữ thanh khoản × chi phí duy trì TSTK, hoặc C × CCF × … khi chưa có mô hình hành vi [[src-vab-ftp#^vab-ftp-69]]. Lubinska nêu chi phí thanh khoản dự phòng phải được phân bổ ngược lại cho mảng kinh doanh [[src-lubinska-alm-optimisation#^lubinska-u04-3]].
- **Căn cứ quy định.** BCBS 144 P4: liquidity charge gán cho trạng thái, danh mục hoặc giao dịch, kể cả cam kết tiềm tàng chưa tác động trực tiếp lên bảng cân đối [[src-bcbs-liquidity-principles-2008#^lrm-19]]. TT83/2025 Đ45.1.b yêu cầu ngân hàng phải xác định chi phí đáp ứng nhu cầu thanh khoản và rủi ro thanh khoản trong định giá vốn nội bộ [[src-tt83-2025-nhnn#^d45-1b]].
- **Funding spread (Tata).** FTP curve bù đắp cho Treasury cả rủi ro lãi suất lẫn rủi ro thanh khoản, nên tách thành pure interest rate risk curve cộng funding spread [[src-tata-bank-alm#^tata-ftp-10]]. Funding spread đặc thù theo tài sản; thực tế dùng một FTP curve với spread bình quân rồi điều chỉnh theo trường hợp. Ví dụ của Tata: ngân hàng phát hành note cố định 2 năm 3% và note thả nổi 2 năm 2,2% thì funding spread 2 năm là 80 bp [[src-tata-bank-alm#^tata-ftp-13]].
- **Chi phí LCR (Tata).** Mỗi yêu cầu quy định bị vị thế kích hoạt tạo chi phí biên cho ngân hàng [[src-tata-bank-alm#^tata-ftp-19]]. Nếu chi phí HQLA bổ sung không được định giá, hoạt động mới có xu hướng làm xấu LCR [[src-tata-bank-alm#^tata-ftp-20]]. Một số hệ thống FTP đã phân bổ chi phí LCR cho cả tài sản và nợ phải trả, tạo động lực cho tài sản sinh dòng vào LCR [[src-tata-bank-alm#^tata-ftp-21]].
- **Chi phí NSFR (Tata).** Một số vị thế (như phái sinh) không cần tài trợ thường xuyên nhưng làm xấu NSFR, có thể buộc ngân hàng huy động thêm vốn dài hạn đắt hơn. Vị thế ảnh hưởng NSFR nên bị phạt trên FTP curve [[src-tata-bank-alm#^tata-ftp-22]].
- **Contingency liquidity (Tata).** Gồm tiền mặt, tương đương tiền và HQLA không bị cầm cố; chi phí được cộng vào FTP rate, ví dụ hạn mức tín dụng cam kết [[src-tata-bank-alm#^tata-ftp-26]]. Tata nhận xét chi phí thanh khoản và vốn kinh tế được công nhận chậm như cấu phần của FTP rate [[src-tata-bank-alm#^tata-ftp-24]].
- *Diễn giải:* Tata là sách T4 theo bối cảnh EU; nguồn này nêu hướng và không đưa công thức hay mức phí. Các tầng "Buffer carry" và "Regulatory charge" của [[liquidity-transfer-pricing]] mục 2 vẫn chỉ dựa nguồn T5 cho phần tham số, nên cụm này không dùng chúng. Nghĩa vụ NHNN về LCR/NSFR nằm ở TT50/2026; wiki chưa có quy định nào nói cách tính chi phí đó vào FTP.

### Q3 — Interest rate risk

- **Chuyển giao.** Rủi ro lãi suất và rủi ro funding được tách khỏi BU và chuyển về ALM [[src-lubinska-alm-optimisation#^lubinska-u01-7]]. VAB nêu FTP phản ánh rủi ro thanh khoản và rủi ro lãi suất sổ ngân hàng mà bộ phận FTP phải quản lý [[src-vab-ftp#^vab-ftp-4]].
- **Giá điều chuyển là hedge giả định.** FTP dựa trên một phòng ngừa danh nghĩa cho giao dịch khách hàng [[src-choudhry-principles-banking#^choudhry-ftp-5]]. Chuyển vốn giữa Treasury và BU được thanh toán trên cơ sở trùng khớp kỳ hạn theo một đường cong FTP phù hợp [[src-choudhry-principles-banking#^choudhry-ftp-6]].
- **Cách VAB gán kỳ hạn theo loại sản phẩm.**

| Sản phẩm | Kỳ hạn tính COF/VOF cơ sở | TLP | Nguồn |
|---|---|---|---|
| Tiền gửi TT1 gốc trả cuối kỳ | Kỳ hạn gốc, cố định suốt thời gian gửi | Bằng 0 | [[src-vab-ftp#^vab-ftp-71]] |
| Cho vay trả gốc định kỳ, lãi suất cố định | Kỳ hạn hiệu lực (bình quân gia quyền), áp suốt thời gian cho vay | Không nêu trong claim | [[src-vab-ftp#^vab-ftp-73]] |
| Cho vay trả gốc cuối kỳ, lãi suất thả nổi | Kỳ tái định giá, áp đến ngày điều chỉnh lãi suất tiếp theo | Kỳ hạn gốc trừ kỳ tái định giá | [[src-vab-ftp#^vab-ftp-86]] |
| Cho vay trả gốc định kỳ, lãi suất thả nổi | Kỳ tái định giá | Kỳ hạn hiệu lực trừ kỳ tái định giá | [[src-vab-ftp#^vab-ftp-87]] |

- *Diễn giải:* với khoản vay thả nổi, VAB tách hai chiều: kỳ tái định giá quyết định phần lãi suất, còn chênh lệch giữa kỳ hạn gốc (hoặc hiệu lực) và kỳ tái định giá quyết định phần thanh khoản (TLP). Cách tách này được suy từ bảng trên, VAB không tự gọi tên như vậy.
- **Phần ALM giữ lại.** ALM huy động vốn có đặc tính không nhất thiết khớp vốn cấp cho asset centre, nên còn chênh lệch kỳ hạn và lãi suất. Treasurer tách thành tài khoản rủi ro lãi suất (IRRM) và tài khoản thanh khoản, rồi quyết định phòng ngừa hoặc để mở [[src-lubinska-alm-optimisation#^lubinska-u01-13]]. Ví dụ khoản vay cố định 5 năm cho ba lựa chọn phòng ngừa, mỗi lựa chọn đóng một tập rủi ro khác nhau [[src-lubinska-alm-optimisation#^lubinska-u01-14]].
- **Steering bằng đường cong.** Bardaeva nêu điều chỉnh độ dốc đường cong FTP để quản lý tác động bất lợi của chuyển hoá kỳ hạn lên NII [[src-bardaeva-alm#^ch15-8]].
- **Treasury profit centre.** Ngoài thu xếp funding, Treasury kiếm P&L từ rủi ro lãi suất phát sinh khi funding ở đầu ngắn đường cong [[src-choudhry-principles-banking#^choudhry-mo-3]].

### Q4 — Optionality

- **Tiền gửi rút trước hạn.** Áp dụng chi phí phạt rút trước hạn: VOF cơ sở xác định theo VOF của tiền gửi không kỳ hạn thông thường [[src-vab-ftp#^vab-ftp-18]].
- **Khoản vay trả trước hạn.** COF cơ sở lấy theo kỳ hạn hiệu lực tính từ dòng tiền của mô hình hành vi trả trước hạn của từng khoản vay [[src-vab-ftp#^vab-ftp-19]], bằng phương pháp bình quân gia quyền để tính kỳ hạn bình quân của khoản vay [[src-vab-ftp#^vab-ftp-20]].
- **CASA.** Base curve của CASA là trung bình có trọng số giữa hai điểm kỳ hạn theo tỷ lệ CASA không ổn định do mô hình hành vi tính [[src-vab-ftp#^vab-ftp-15]]. Khi chưa có mô hình hành vi: phần tiền gửi không kỳ hạn bị rút lấy không thấp hơn 15% số dư bình quân 30 ngày, phần còn lại nhận VOF kỳ hạn 2 tháng hoặc theo ALCO phê duyệt [[src-vab-ftp#^vab-ftp-44]].
- **Behaviouralisation (Lubinska).** Là phương pháp nắm bắt rủi ro lãi suất hành vi và chi phí/giá trị thanh khoản hành vi của sản phẩm [[src-lubinska-alm-optimisation#^lubinska-u04-2]]. CASA tách thành phần biến động (tái định giá qua đêm) và phần ổn định, phần lõi coi như nguồn dài hạn lãi suất 0% [[src-lubinska-alm-optimisation#^lubinska-u04-1]]. Mô hình biến động số dư chia số dư thành core và non-core [[src-lubinska-alm-optimisation#^lubinska-u04-5]].
- **Hậu quả khi bỏ qua.** Trả nợ trước hạn không đưa vào chiến lược phòng ngừa gây overhedging, vì số swap payer vượt dư nợ tài sản lãi suất cố định thực tế, và tác động tiêu cực lên PV01 [[src-lubinska-alm-optimisation#^lubinska-u04-4]].
- **Hạn mức chưa sử dụng.** Cam kết tiềm tàng được định giá bằng phần bù rủi ro thanh khoản tiềm tàng (mục Q2) [[src-vab-ftp#^vab-ftp-68]]. *Diễn giải:* khách hàng quyết định rút hạn mức hay không, nên có thể coi phần bù này là cách đưa quyền chọn rút hạn mức vào FTP. VAB không gọi nó là quyền chọn. (ngoài wiki, chưa có nguồn)

### Q5 — Ranh giới của FTP

| Rủi ro / chi phí | FTP có định giá? | Nguồn |
|---|---|---|
| Rủi ro tín dụng của khách hàng | Không chuyển về ALM | [[src-lubinska-alm-optimisation#^lubinska-u01-8]] |
| Expected loss, dự phòng, cost of capital | Tính sau FTP rate (net margin, SVA) | [[src-choudhry-principles-banking#^choudhry-ifc-10]] |
| Rủi ro tín dụng riêng của ngân hàng | Có, nằm trong TLP | [[src-vab-ftp#^vab-ftp-11]] |
| Chi phí vốn chủ sở hữu | Có khi áp RAROC, tính riêng bằng (ROE% − COF%) × vốn RAROC × WAT/365 | [[src-vab-ftp#^vab-ftp-67]] |
| Rủi ro không phòng ngừa được ra thị trường | Không hết, do FTP sai hoặc phái sinh kém thanh khoản | [[src-lubinska-alm-optimisation#^lubinska-u01-8]] |
| Hành vi khách hàng do sự kiện khí hậu (tập trung rủi ro) | Lý tưởng nên bị phạt qua lãi suất FTP | [[src-tata-bank-alm#^tata-fut-4]] |

- TT83/2025 Đ26.2.c đặt yêu cầu riêng: chiến lược phải có nguyên tắc xác định chi phí bù đắp rủi ro tín dụng trong tính lãi suất và định giá tín dụng theo mức độ rủi ro của khách hàng [[src-tt83-2025-nhnn#^d26-2c]]. Yêu cầu này nằm ngoài Đ45.1.b (chi phí thanh khoản).

## Bằng chứng ủng hộ

- Chuyển giao rủi ro lãi suất và funding về ALM xuất hiện ở ba nguồn T4 độc lập: Lubinska [[src-lubinska-alm-optimisation#^lubinska-u01-7]], Choudhry [[src-choudhry-principles-banking#^choudhry-ftp-10]] và VAB [[src-vab-ftp#^vab-ftp-4]].
- Liquidity FTP có hai nguồn quy định: BCBS 144 P4 (T2) [[src-bcbs-liquidity-principles-2008#^lrm-p04]] và TT83/2025 (T1) [[src-tt83-2025-nhnn#^d45-1b]], cộng thực hành của Choudhry và VAB.
- Chi phí LCR/NSFR và contingency liquidity trong FTP chỉ có một nguồn T4 là Tata, ở mức hướng dẫn, không có tham số.
- Cấu phần pháp định (BHTG, DTBB), TSTK, TLP, kỳ hạn hiệu lực chỉ có VAB (một nguồn tư vấn T4, `draft`).

## Bằng chứng trái chiều

- **Cấu phần credit và optionality.** Nguồn T5 (`doc_status: draft`) viết FTP Rate = Base Rate + Liquidity Spread + Credit Spread + Optionality Cost [[src-ftp-transmission-analysis#^ftp-trans-3]]. Lubinska nói rủi ro tín dụng theo định nghĩa không chuyển về ALM [[src-lubinska-alm-optimisation#^lubinska-u01-8]], và danh sách cấu phần COF của VAB không có "credit spread" cho khách hàng [[src-vab-ftp#^vab-ftp-7]]. Cụm này theo nguồn T4 và không dùng công thức T5. Chưa đủ cơ sở gọi là conflict vì phạm vi hai nguồn khác nhau (T5 không nói rõ credit của ai).
- **Cost hay market approach.** Cost approach phụ thuộc lãi suất quá khứ nên phản ứng trễ và đường cong có thể méo [[src-choudhry-principles-banking#^choudhry-ifc-17]]. VAB lại dùng chi phí huy động thực tế cho base curve VND [[src-vab-ftp#^vab-ftp-82]]. Đây là khác biệt thiết kế, không phải conflict.

## Phụ thuộc regime

- Khi chênh lệch chi phí huy động nới rộng, FTP lãi suất cổ điển không đủ và cần lớp liquidity FTP [[src-choudhry-principles-banking#^choudhry-ftp-14]].
- Ngân hàng chỉ huy động bằng tiền gửi khách hàng và không phát hành wholesale có thể nới một số nguyên tắc dựng đường cong của EBA [[src-choudhry-principles-banking#^choudhry-ifc-15]].
- Cost approach hợp thị trường ổn định, biến động lãi suất thấp, cấu trúc nợ đa dạng theo kỳ hạn [[src-choudhry-principles-banking#^choudhry-ifc-17]].
- Nguồn đã ingest chưa phân tích việc cấu phần optionality đổi thế nào khi lãi suất tăng hay giảm. [cần nguồn]

## Hàm ý ALM / quy định

- **Nghĩa vụ tại VN (T1).** TT83/2025 hiệu lực từ 2026-07-01 [[src-tt83-2025-nhnn#^d74-1]] có hai yêu cầu liên quan: chi phí thanh khoản và rủi ro thanh khoản trong định giá vốn nội bộ (Đ45.1.b) [[src-tt83-2025-nhnn#^d45-1b]], và nguyên tắc chi phí bù đắp rủi ro tín dụng trong tính lãi suất (Đ26.2.c) [[src-tt83-2025-nhnn#^d26-2c]]. Bộ phận ALM rà soát, đề xuất nguyên tắc xây dựng giá điều chuyển vốn nội bộ (Đ25.3.b) [[src-tt83-2025-nhnn#^d25-3]]. Wiki chưa có quy định NHNN nào đặt yêu cầu cho từng cấu phần funding cost, rủi ro lãi suất hay optionality của FTP.
- **Tham chiếu Basel (không phải nghĩa vụ tại VN).** BCBS 144 P4 chỉ nói phần thanh khoản [[src-bcbs-liquidity-principles-2008#^lrm-p04]]. Wiki chưa có chuẩn BCBS về FTP cho lãi suất và optionality. [cần nguồn]
- **Tài liệu VN.** VAB (T4, `draft`, tư vấn) là nguồn duy nhất cho cấu phần cụ thể. VAB rà soát lãi suất FTP cơ sở, BHTG, DTBB, phần bù TSTK, TLP và điều chỉnh ALCO hằng quý; hỗ trợ huy động rà soát hằng năm [[src-vab-ftp#^vab-ftp-65]].
- *Diễn giải:* thiết kế cấu phần (đặc biệt TLP, kỳ hạn hiệu lực, tỷ lệ hành vi) là quyết định nội bộ có tham chiếu VAB, Choudhry, Lubinska; ALCO duyệt (xem [[alco]]). (ngoài wiki, chưa có nguồn)

## Bất định

- [cần nguồn] Premium cho quyền chọn trong lãi suất FTP (prepayment, rút trước hạn, CASA). Chưa thấy nguồn T3/T4 trong wiki; hiện chỉ có cách đổi kỳ hạn tính giá của VAB.
- [cần nguồn] Công thức và mức phí LCR/NSFR trong FTP. Tata (T4) nêu hướng nhưng không đưa công thức; tham số ở [[liquidity-transfer-pricing]] mục 2 chỉ có nguồn T5. Chưa có nguồn cho cách ngân hàng VN tính chi phí này.
- Phần bù TSTK của VAB viện dẫn Phụ lục 3 TT22/2019 [[src-vab-ftp#^vab-ftp-43]]. TT50/2026 (hiệu lực 2026-10-01) thay TT22/2019 cho NHTM và chi nhánh NHNNg [[src-tt50-2026-nhnn#^d37-3a]]. Trước khi áp LCR/NSFR, Đ13.4 yêu cầu tiếp tục tuân thủ các tỷ lệ tính theo TT22/2019 [[src-tt50-2026-nhnn#^d13-4]]. Danh mục TSTK theo TT50 so với Phụ lục 3 TT22 chưa được đối chiếu.
- Mức 0,15% phí BHTG là số của tài liệu VAB, không ghi ngày; chưa đối chiếu với văn bản NHNN hiện hành.
- [2026-10-22] ingest src-tata-bank-alm (bổ sung 2.3 FTP, ^tata-ftp-3..32): [[liquidity-transfer-pricing]] mục 7 có nguồn T4 cho chi phí LCR/NSFR và contingency liquidity; [[funds-transfer-pricing]] có Tata ^tata-ftp-27 (FTP rate điều chỉnh mark-up/discount theo optionality) và ^tata-ftp-29 (credit/operational risk thường không định giá), kèm callout conflict với nguồn T5; Q2 đã rà lại (2026-10-22); còn cần rà lại Q4, Q5 và Bằng chứng trái chiều.
- Bước 3 chưa đọc raw: mọi claim lấy từ source note đã ingest; trích nguyên văn đã khớp lint.
- [2026-10-22] ingest src-ftp-transmission-analysis u01 (bổ sung): [[ftp-transmission-mechanism]] nay có công thức ΔSpread theo khoảng cách LCR/NSFR so với target (`^ftp-trans-15`) và ví dụ bps (`^ftp-trans-16`), chỉ từ nguồn T5; cần rà lại dòng [cần nguồn] về công thức và mức phí LCR/NSFR.
