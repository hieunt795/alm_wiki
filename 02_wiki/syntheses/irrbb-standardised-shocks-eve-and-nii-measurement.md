---
title: "Phương Pháp Đo Lường EVE và NII Dưới Các Kịch Bản Sốc Lãi Suất Chuẩn Hóa"
aliases: [IRRBB Standardised Shocks Measurement, Đo lường EVE và NII theo kịch bản sốc, EVE and NII Standardised Measurement, 6 kịch bản sốc lãi suất Basel, Parallel Steepener Flattener Measurement]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Q1 Phương pháp đo lường ΔEVE dưới 6 kịch bản sốc chuẩn hóa được thực hiện như thế nào (chiết khấu dòng tiền 19 dải kỳ hạn, giả định run-off, phụ trội quyền chọn tự động KAO, tổng hợp đa tiền tệ và ngưỡng ngoại lai 15% Tier 1 Capital)? · Q2 Phương pháp đo lường ΔNII dưới các kịch bản sốc chuẩn hóa được xây dựng như thế nào (khung thời gian 12 tháng, giả định constant balance sheet vs dynamic balance sheet và nén biên lãi ròng NIM)? · Q3 Cấu trúc toán học và tham số của 6 kịch bản sốc lãi suất chuẩn hóa Basel được xác định như thế nào (hàm suy giảm xoay trục e^(-t/4), ma trận biên độ sốc theo đồng tiền, hệ thống sàn 100 bps và trần biên độ)? · Q4 Nghĩa vụ tại VN theo TT83/2025 khi đo ΔEVE và ΔNII bằng kịch bản sốc là gì?"
as_of: 2026-10-20
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tt83-2025-nhnn]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]"]
relations: []
tags: [irrbb, eve, nii, standardised-shocks, parallel-shock, steepener, flattener, time-buckets, kao, outlier-test, synthesis]
updated: 2026-10-20
reviewed:
---

## Câu hỏi

- **Q1**: Phương pháp đo lường Giá trị kinh tế của vốn chủ sở hữu ($\Delta\text{EVE}$) dưới 6 kịch bản sốc chuẩn hóa được thực hiện như thế nào (chiết khấu dòng tiền 19 dải kỳ hạn, giả định run-off, phụ trội quyền chọn tự động $KAO$, tổng hợp đa tiền tệ và ngưỡng ngoại lai 15% Tier 1 Capital)?
- **Q2**: Phương pháp đo lường Độ nhạy thu nhập lãi thuần ($\Delta\text{NII}$) dưới các kịch bản sốc chuẩn hóa được xây dựng như thế nào (khung thời gian 12 tháng, giả định constant balance sheet vs dynamic balance sheet và nén biên lãi ròng NIM)?
- **Q3**: Cấu trúc toán học và tham số của 6 kịch bản sốc lãi suất chuẩn hóa Basel (Parallel up/down, Steepener, Flattener, Short rate up/down) được xác định như thế nào (hàm suy giảm xoay trục $e^{-t_k/4}$, ma trận biên độ sốc theo đồng tiền, hệ thống sàn 100 bps và trần biên độ)?
- **Q4**: Nghĩa vụ tại VN theo TT83/2025 khi đo $\Delta\text{EVE}$ và $\Delta\text{NII}$ bằng kịch bản sốc là gì?

Node dùng: [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[outlier-bank-test]], [[standardised-interest-rate-shocks]], [[irrbb-standardised-framework]] (canonical); [[repricing-gap-analysis]], [[rwa-irrbb]], [[tt83-2025]] (draft). Hiệu lực: d368 là chuẩn Basel final; TT83/2025 hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]].

---

## Kết luận

- **Q1**: d368 đo $\Delta\text{EVE}$ qua 5 bước: phân loại vị thế, slot dòng tiền vào dải kỳ hạn, tính $\Delta\text{EVE}$ theo kịch bản và đồng tiền, cộng add-on quyền chọn tự động $\text{KAO}$, rồi lấy tổn thất lớn nhất qua 6 kịch bản [[src-bcbs-irrbb-2016#^irrbb-u05-1]]. Dòng tiền slot theo giả định run-off và loại vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Lỗ $\Delta EVE_{i,c} > 0$ của các đồng tiền trọng yếu (trên 5% tài sản hoặc nợ sổ ngân hàng) được cộng, không bù trừ lãi [[src-bcbs-irrbb-2016#^irrbb-u05-8]]. Supervisor nên áp dụng ít nhất một outlier test so $\max \Delta\text{EVE}$ với 15% Tier 1 capital [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
- **Q2**: $\Delta\text{NII}$ công bố nên tính trên 12 tháng liên tục, theo constant balance sheet và gồm commercial margin [[src-bcbs-irrbb-2016#^irrbb-p08-3]], dưới 2 kịch bản sốc cho NII [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. d368 Annex 1 phân ba trạng thái mô hình hoá thu nhập: run-off, constant và dynamic balance sheet; nguồn gọi dynamic là cách có ý nghĩa nhất [[src-bcbs-irrbb-2016#^irrbb-u06-9]], nhưng cũng cảnh báo dynamic view có thể che giấu rủi ro nền tảng [[src-bcbs-irrbb-2016#^irrbb-p04-4]]. Tata và Lubinska xấp xỉ $\Delta\text{NII}$ bằng repricing gap nhân cú sốc [[src-tata-bank-alm#^tata-egap-1]] [[src-lubinska-alm-optimisation#^lubinska-u02-25]].
- **Q3**: 6 kịch bản gồm 2 song song, steepener, flattener và 2 sốc ngắn hạn [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. Sốc ngắn hạn suy giảm theo $e^{-t_k/4}$ [[src-bcbs-irrbb-2016#^irrbb-u07-3]]. Biên độ theo đồng tiền lấy từ Table 1 [[src-bcbs-irrbb-2016#^irrbb-u07-5]], có sàn 100 bp và trần 500/400/300 bp cho ngắn hạn/song song/dài hạn [[src-bcbs-irrbb-2016#^irrbb-u07-4]]. Supervisor quốc gia có thể đặt sàn lãi suất sau sốc không lớn hơn 0 [[src-bcbs-irrbb-2016#^irrbb-u07-11]]; EBA dùng sàn âm phụ thuộc kỳ hạn [[src-tata-bank-alm#^tata-reg-8]] [[src-tata-bank-alm#^tata-sot-2]].
- **Q4**: Theo [[tt83-2025]], ngân hàng phải đo bằng cả ΔNII và ΔEVE theo Phụ lục V [[src-tt83-2025-nhnn#^d53-1a2]], có hạn mức tối thiểu cho cả hai [[src-tt83-2025-nhnn#^d53-2]]. Từ 01/07/2026 đến 31/12/2027 được dùng một trong hai chỉ tiêu [[src-tt83-2025-nhnn#^d74-4a]], chậm nhất từ 01/01/2028 phải dùng cả hai [[src-tt83-2025-nhnn#^d74-4b]]. Bảng tham số sốc không có VND [[src-tt83-2025-nhnn#^pl5-c1-1]]. TT83 không có outlier test, nhưng từ 01/01/2028 $RWA_{IRRBB}$ tính theo ΔEVE [[src-tt83-2025-nhnn#^pl6-1c]].

---

## Cơ chế

### Q1 — Đo ΔEVE theo khuôn khổ chuẩn hoá

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[standardised-interest-rate-shocks]] | input-to | [[economic-value-of-equity]] | — | [[src-bcbs-irrbb-2016#^irrbb-p08-1]] |
| [[irrbb-standardised-framework]] | measures | [[economic-value-of-equity]] | — | [[src-bcbs-irrbb-2016#^irrbb-u05-1]] |
| [[irrbb-standardised-framework]] | governs | [[non-maturity-deposits]] | — | [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| [[irrbb-standardised-framework]] | governs | [[behavioural-options]] | — | [[src-bcbs-irrbb-2016#^irrbb-u05-5]] |
| [[economic-value-of-equity]] | measures | [[option-risk]] | — | [[src-bcbs-irrbb-2016#^irrbb-u05-1]] |
| [[economic-value-of-equity]] | input-to | [[outlier-bank-test]] | — | [[src-bcbs-irrbb-2016#^irrbb-p12-1]] |
| [[economic-value-of-equity]] | input-to | [[rwa-irrbb]] | — · VN từ 01/01/2028 | [[src-tt83-2025-nhnn#^pl6-1c]] |

**Năm bước của d368** [[src-bcbs-irrbb-2016#^irrbb-u05-1]]:

1. **Phân loại và slot dòng tiền.**
   - Mọi notional repricing cash flow của tài sản, nợ và khoản mục ngoại bảng nhạy lãi suất, theo từng đồng tiền, được phân bổ vào dải kỳ hạn hoặc điểm giữa dải theo khả năng chuẩn hoá của vị thế [[src-bcbs-irrbb-2016#^irrbb-u05-16]]. Có 19 dải [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. Chi tiết ở [[notional-repricing-cash-flow]].
   - Vị thế chuẩn hoá được có thể được slot theo ngày đáo hạn hợp đồng nếu coupon cố định, hoặc vào kỳ tái định giá kế tiếp nếu coupon thả nổi [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-tata-bank-alm#^tata-gap-1]].
   - Giả định run-off: vị thế hiện hữu đáo hạn và không được thay thế; ngân hàng nên loại vốn chủ sở hữu khỏi phép tính [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
   - NMD tách thành phần core và non-core. Phần non-core slot vào dải qua đêm. Trần tỷ lệ core và trần kỳ hạn bình quân là 90% và 5 năm (bán lẻ giao dịch), 70% và 4,5 năm (bán lẻ phi giao dịch), 50% và 4 năm (bán buôn) [[src-bcbs-irrbb-2016#^irrbb-u05-4]]. Xem [[non-maturity-deposits]], [[repricing-balance-sheet]].
   - CPR của khoản vay cố định có quyền trả trước nhân hệ số $\gamma_i$ theo kịch bản [[src-bcbs-irrbb-2016#^irrbb-u05-5]]; TDRR của tiền gửi có kỳ hạn nhân hệ số $u_i$ [[src-bcbs-irrbb-2016#^irrbb-u05-6]]. Vì vậy dòng tiền có thể khác nhau theo kịch bản $i$ [[src-bcbs-irrbb-2016#^irrbb-u05-23]].
2. **Bù trừ và chiết khấu.**
   - Trong mỗi dải $k$, dòng tiền dương và âm được bù trừ thành một vị thế long hoặc short [[src-bcbs-irrbb-2016#^irrbb-u05-17]]. Dòng tiền cùng dải được giả định khớp hoàn toàn (intra-bucket mismatch); BCBS giảm rủi ro này bằng 19 dải [[src-bcbs-irrbb-2016#^irrbb-u05-22]].
   - Dòng tiền ròng của dải $k$ nhân với discount factor liên tục của kịch bản $i$, với $t_k$ là điểm giữa dải [[src-bcbs-irrbb-2016#^irrbb-u05-18]]:
     $$DF_{i,c}(t_k) = \exp(-R_{i,c}(t_k) \cdot t_k)$$
     [[src-bcbs-irrbb-2016#^irrbb-u05-18]]
   - Dòng tiền nên được chiết khấu bằng risk-free rate. Nếu ngân hàng đã đưa commercial margin và spread component vào dòng tiền thì chiết khấu bằng risk-free rate cộng các phần đó. Discount factor phải đại diện cho risk-free zero coupon rate [[src-bcbs-irrbb-2016#^irrbb-u05-19]].
3. **Tính ΔEVE theo kịch bản và đồng tiền.** Cộng các vị thế ròng có trọng số ra EVE của đồng tiền $c$ trong kịch bản $i$, không gồm quyền chọn lãi suất tự động [[src-bcbs-irrbb-2016#^irrbb-u05-20]]:
     $$EVE_{i,c}^{nao} = \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k)$$
     [[src-bcbs-irrbb-2016#^irrbb-u05-20]]

   $\Delta EVE_{i,c}$ bằng EVE theo cấu trúc kỳ hạn hiện tại trừ EVE của kịch bản $i$, cộng $KAO_{i,c}$ [[src-bcbs-irrbb-2016#^irrbb-u05-21]]:
     $$\Delta EVE_{i,c} = EVE_{0,c}^{nao} - EVE_{i,c}^{nao} + KAO_{i,c}$$
     [[src-bcbs-irrbb-2016#^irrbb-u05-21]]

   Theo quy ước này, $\Delta EVE_{i,c} > 0$ là khoản lỗ [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
4. **Add-on quyền chọn tự động ($KAO$).** Quyền chọn tự động nhúng nên được bỏ qua khi slot dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-3]]. Với mỗi quyền chọn tự động đã bán, ngân hàng tính thay đổi giá trị dưới từng kịch bản, kết hợp mức tăng tương đối 25% của implicit volatility; trừ đi thay đổi giá trị của quyền chọn mua dùng để phòng ngừa [[src-bcbs-irrbb-2016#^irrbb-u05-7]]. Mô hình định giá quyền chọn: [cần nguồn].
5. **Tổng hợp và outlier test.**
   - Trong mỗi kịch bản, chỉ lỗ $\Delta EVE_{i,c} > 0$ của các đồng tiền trọng yếu được cộng; tổn thất lớn nhất qua 6 kịch bản là thước đo rủi ro EVE [[src-bcbs-irrbb-2016#^irrbb-u05-8]]:
     $$\Delta EVE^{*} = \max_{i=1..6} \sum_{c} \max(0, \Delta EVE_{i,c})$$
     [[src-bcbs-irrbb-2016#^irrbb-u05-8]]

     *Diễn giải:* công thức trên viết gọn câu "the EVE losses … are aggregated", không chép từ nguồn. TT83 viết công thức tương đương [[src-tt83-2025-nhnn#^pl5-a5]].
   - Supervisor quốc gia được phép quy định cách gộp tiền tệ khác nếu chứng minh được cách đó vẫn phù hợp khẩu vị IRRBB của jurisdiction [[src-bcbs-irrbb-2016#^irrbb-u05-24]].
   - Supervisor nên áp dụng ít nhất một outlier test so $\max \Delta\text{EVE}$ dưới 6 kịch bản với 15% Tier 1 capital. Ngân hàng bị xác định là outlier phải được coi là có thể mang IRRBB quá mức [[src-bcbs-irrbb-2016#^irrbb-p12-1]]. Phép thử bổ sung (theo CET1 hoặc ΔNII) có thể được dùng, nhưng ngưỡng không được lỏng hơn 15% Tier 1 [[src-bcbs-irrbb-2016#^irrbb-p12-2]]. Chi tiết ở [[outlier-bank-test]].
   - Khi supervisor kết luận IRRBB quá mức so với vốn hoặc thu nhập, supervisor phải yêu cầu ít nhất một biện pháp: giảm exposure, tăng vốn, ràng buộc tham số nội bộ, hoặc cải thiện khung quản trị [[src-bcbs-irrbb-2016#^irrbb-p12-3]].

**Tham chiếu EU (Tata, T4).** SOT EVE theo RTS/2022/10 xác định ngân hàng có EVE giảm quá 15% vốn cấp 1 dưới một kịch bản sốc, tính theo run-off balance sheet [[src-tata-bank-alm#^tata-sot-1]]. Ngưỡng EU đổi từ 20% vốn tự có (Chỉ thị 2006/48/EC, CRD IV) sang 15% vốn cấp 1 cộng phép thử NII (CRD V) [[src-tata-bank-alm#^tata-reg-5]].

---

### Q2 — Đo ΔNII dưới kịch bản sốc

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[standardised-interest-rate-shocks]] | input-to | [[net-interest-income-sensitivity]] | — | [[src-bcbs-irrbb-2016#^irrbb-p08-1]] |
| [[repricing-gap-analysis]] | input-to | [[net-interest-income-sensitivity]] | — | [[src-lubinska-alm-optimisation#^lubinska-u02-23]] |
| [[net-interest-income-sensitivity]] | measures | [[gap-risk]] | — | [[src-bcbs-irrbb-2016#^irrbb-u06-4]] |
| [[net-interest-income-sensitivity]] | input-to | [[outlier-bank-test]] | — | [[src-bcbs-irrbb-2016#^irrbb-p12-2]] |

1. **Chân trời và kịch bản.**
   - $\Delta\text{NII}$ công bố là chênh lệch thu nhập lãi trong 12 tháng liên tục [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Choudhry mô tả góc độ thu nhập là biến động NII từ tài sản và nợ tái định giá trong chân trời 12 tháng [[src-choudhry-principles-banking#^choudhry-irrbb-3]].
   - Ngân hàng nên áp dụng 2 kịch bản sốc cho NII [[src-bcbs-irrbb-2016#^irrbb-u07-1]] và phải công bố $\Delta\text{NII}$ dưới các kịch bản ở Annex 2 [[src-bcbs-irrbb-2016#^irrbb-p08-1]].
   - Ngoài phần công bố, d368 Annex 1 ghi thước đo thu nhập thường dùng chân trời một đến ba năm, không quá năm năm [[src-bcbs-irrbb-2016#^irrbb-u06-8]]. ΔNII là chênh lệch NII kỳ vọng giữa kịch bản cơ sở (theo kế hoạch kinh doanh hiện tại) và kịch bản stress [[src-bcbs-irrbb-2016#^irrbb-u06-10]].
   - Tata ghi chân trời dự báo NII nội bộ thường từ một đến ba năm; kéo dài hơn tạo cảm giác chính xác giả [[src-tata-bank-alm#^tata-nii-4]].
2. **Giả định bảng cân đối.**
   - **Constant balance sheet (d368)**: dòng tiền đáo hạn hoặc tái định giá được thay bằng dòng tiền mới có cùng số tiền, kỳ tái định giá và spread component. Dòng tiền dự kiến nên gồm commercial margin và spread component [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
   - **Ba trạng thái theo d368 Annex 1** [[src-bcbs-irrbb-2016#^irrbb-u06-9]]:

     | Trạng thái | Giả định | Nguồn |
     |---|---|---|
     | Run-off | Tài sản và nợ không được thay khi đáo hạn, trừ phần cần để tài trợ bảng cân đối còn lại | [[src-bcbs-irrbb-2016#^irrbb-u06-9]] |
     | Constant | Giữ quy mô và cơ cấu bằng thay thế tương đương | [[src-bcbs-irrbb-2016#^irrbb-u06-9]] |
     | Dynamic | Đưa kỳ vọng kinh doanh tương lai vào, điều chỉnh nhất quán theo kịch bản; nguồn gọi là cách có ý nghĩa nhất | [[src-bcbs-irrbb-2016#^irrbb-u06-9]] |

     Mô hình dynamic phản ánh thay đổi khối lượng và loại kinh doanh theo môi trường lãi suất; đây là dạng phức tạp nhất [[src-bcbs-irrbb-2016#^irrbb-u06-10]]. Dự phóng cần giả định về khối lượng tài sản, nợ mới, khoản đáo hạn, margin và phí quyền chọn [[src-bcbs-irrbb-2016#^irrbb-u06-9]].
   - **Giới hạn của dynamic view**: hữu ích cho lập kế hoạch kinh doanh và ngân sách, nhưng phụ thuộc biến số rất khó dự báo chính xác trong thời gian dài và có thể che giấu rủi ro nền tảng [[src-bcbs-irrbb-2016#^irrbb-p04-4]]. *Diễn giải:* đây là lý do phần công bố của d368 dùng constant balance sheet [[src-bcbs-irrbb-2016#^irrbb-p08-3]], còn dynamic để cho quản trị nội bộ.
   - **Thực tế ALCO**: Choudhry ghi phân tích kịch bản của ALCO thường giả định sổ không đổi trong một tháng và gọi giả định đó là không thực tế [[src-choudhry-principles-banking#^choudhry-irr-3]]. Gap analysis không tính tăng trưởng hay thay đổi cơ cấu tài sản và nợ [[src-choudhry-principles-banking#^choudhry-irr-8]].
   - Theo Tata, khối lượng từng mảng kinh doanh nên được lập kế hoạch riêng vì run-off khác nhau. Run-off phải ước tính và phụ thuộc môi trường lãi suất giả định cùng hành vi khách hàng [[src-tata-bank-alm#^tata-niip-4]].
3. **Xấp xỉ bằng repricing gap.**
   - Lubinska: $\Delta\text{NII}$ bằng thay đổi lãi suất $\Delta i$ nhân GAP (RSA trừ RSL trong gapping period) [[src-lubinska-alm-optimisation#^lubinska-u02-25]]. Xem [[repricing-gap-analysis]].
   - Tata: periodic earning gap bằng net repricing gap × 1% × phần còn lại của năm đầu tính từ điểm giữa dải; tổng các periodic earning gap là độ nhạy NII năm đầu với sốc song song 1% [[src-tata-bank-alm#^tata-egap-1]]. Viết dưới dạng tổng, với $\tau_k$ là điểm giữa dải $k$ tính theo năm:
     $$\Delta\text{NII} \approx \sum_{k} \text{Gap}_k \cdot \Delta R \cdot (1 - \tau_k)$$
     [[src-tata-bank-alm#^tata-egap-1]]
   - Với ngân hàng mô hình của Tata, total earning gap −0,25 nghĩa là NII năm đầu giảm 0,25 cho mỗi 1% lãi suất tăng song song [[src-tata-bank-alm#^tata-egap-2]].
   - Giả định của gap analysis: lãi suất dịch song song, lịch trả nợ theo hợp đồng (bỏ qua prepayment và quyền chọn), tái định giá ở giữa dải [[src-choudhry-principles-banking#^choudhry-irr-7]]. *Diễn giải:* vì vậy xấp xỉ gap không thay được mô phỏng NII khi có [[behavioural-options]].
4. **Nén NIM.** *Diễn giải:* earning gap âm nghĩa là nợ tái định giá trong năm nhiều hơn tài sản, nên lãi suất tăng làm [[net-interest-margin]] thu hẹp. Wiki chưa có claim nối trực tiếp ΔNII dưới sốc chuẩn hoá với NIM.

**Tham chiếu EU (Tata, T4).** SOT NII: NII 1 năm giảm quá 5% vốn cấp 1 là "suy giảm lớn"; khác SOT EVE ở chỗ phải gồm commercial margin và tính theo constant balance sheet [[src-tata-bank-alm#^tata-sot-3]]. d368 và TT83 không có ngưỡng NII này.

---

### Q3 — Cấu trúc 6 kịch bản sốc

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[standardised-interest-rate-shocks]] | part-of | [[bcbs-irrbb]] | — | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| [[tt83-2025]] | governs | [[standardised-interest-rate-shocks]] | — · VN | [[src-tt83-2025-nhnn#^pl5-c1-1]] |

| Kịch bản $i$ | Đường cong | Dùng cho | Nguồn |
|---|---|---|---|
| 1. Parallel up | Tăng cùng biên độ ở mọi kỳ hạn | EVE, NII | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| 2. Parallel down | Giảm cùng biên độ ở mọi kỳ hạn | EVE, NII | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| 3. Steepener | Ngắn hạn giảm, dài hạn tăng | EVE | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| 4. Flattener | Ngắn hạn tăng, dài hạn giảm | EVE | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| 5. Short rate up | Ngắn hạn tăng, suy giảm theo kỳ hạn | EVE | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| 6. Short rate down | Ngắn hạn giảm, suy giảm theo kỳ hạn | EVE | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |

1. **Sốc xoay trục.** Sốc ngắn hạn suy giảm theo $S_{\text{short}}(t_k) = e^{-t_k/x}$; $x = 4$ cho hầu hết đồng tiền, trừ khi supervisor quốc gia quyết định khác [[src-bcbs-irrbb-2016#^irrbb-u07-3]]:
   $$\Delta R_{\text{steepener},c}(t_k) = -0.65 \cdot |\Delta R_{\text{short},c}(t_k)| + 0.9 \cdot |\Delta R_{\text{long},c}(t_k)|$$
   [[src-bcbs-irrbb-2016#^irrbb-u07-3]]

   $$\Delta R_{\text{flattener},c}(t_k) = 0.8 \cdot |\Delta R_{\text{short},c}(t_k)| - 0.6 \cdot |\Delta R_{\text{long},c}(t_k)|$$
   [[src-bcbs-irrbb-2016#^irrbb-u07-3]]

   Sốc ngắn hạn $\pm\bar{R}_{short,c} \cdot e^{-t_k/x}$ lớn nhất ở kỳ hạn ngắn nhất. Sốc dài hạn $\pm\bar{R}_{long,c} \cdot (1 - e^{-t_k/x})$, tức $S_{long} = 1 - S_{short}$, chỉ dùng trong sốc xoay trục [[src-bcbs-irrbb-2016#^irrbb-u07-10]]. TT83 dùng cùng công thức [[src-tt83-2025-nhnn#^pl5-c1-3]].

   Ví dụ của d368 tại $t_k = 3{,}5$ năm, hệ số short 0,417, short và long cùng 100 bp (như JPY): sốc ngắn hạn +41,7 bp, steepener +25,4 bp, flattener −1,6 bp [[src-bcbs-irrbb-2016#^irrbb-u07-10]].
2. **Biên độ theo đồng tiền (Table 1).** Mỗi đồng tiền có material position nhận ba biên độ tuyệt đối Parallel, Short, Long [[src-bcbs-irrbb-2016#^irrbb-u07-2]] [[src-bcbs-irrbb-2016#^irrbb-u07-5]]. Bảng đủ 21 đồng tiền ở claim u07-5. Table 1 không ghi đơn vị; *Diễn giải:* đọc là bp theo sàn và trần ở u07-4.

   | Đồng tiền | Parallel | Short | Long | Nguồn |
   |---|---|---|---|---|
   | USD | 200 | 300 | 150 | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |
   | EUR | 200 | 250 | 100 | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |
   | JPY | 100 | 100 | 100 | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |

3. **Cách dựng Table 1.** Chuỗi 16 năm lãi suất bình quân hằng ngày từ 03/01/2000 tới 31/12/2015 [[src-bcbs-irrbb-2016#^irrbb-u07-7]], nhân tham số toàn cầu 60% / 85% / 40% cho song song / ngắn hạn / dài hạn [[src-bcbs-irrbb-2016#^irrbb-u07-8]], rồi áp sàn và trần [[src-bcbs-irrbb-2016#^irrbb-u07-9]]. BCBS sẽ rà lại hiệu chỉnh định kỳ, ví dụ năm năm một lần [[src-bcbs-irrbb-2016#^irrbb-u07-6]].
4. **Sàn và trần của biên độ sốc.** Sàn 100 bp; trần 500 bp (ngắn hạn), 400 bp (song song), 300 bp (dài hạn). Supervisor có thể đặt sàn cao hơn cho home currency [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
5. **Sàn lãi suất sau sốc (post-shock floor).** Sàn 100 bp ở trên là sàn của biên độ sốc, không phải sàn của lãi suất sau sốc [[src-bcbs-irrbb-2016#^irrbb-u07-4]]. Sàn của EBA (Tata, T4):
   - EBA 2018: −100 bp ở kỳ hạn tức thời, tăng 5 bp mỗi năm, đạt 0% ở kỳ hạn 20 năm [[src-tata-bank-alm#^tata-reg-8]];
   - RTS/2022/10: sàn tuyến tính −150 bp ở kỳ hạn tức thời, tăng 3 bp mỗi năm, đạt 0% ở kỳ hạn 50 năm [[src-tata-bank-alm#^tata-sot-2]]. SOT NII theo RTS/2022/10 không dùng sàn tuyến tính [[src-tata-bank-alm#^tata-sot-3]].

   - d368: supervisor quốc gia có thể đặt sàn lãi suất sau sốc cho sáu kịch bản, với điều kiện sàn không lớn hơn 0 [[src-bcbs-irrbb-2016#^irrbb-u07-11]]. *Diễn giải:* hai sàn EBA ở trên đều âm, nên nằm trong khung này.

---

### Q4 — Nghĩa vụ tại VN theo TT83/2025

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[tt83-2025]] | governs | [[economic-value-of-equity]] | — · VN | [[src-tt83-2025-nhnn#^d53-1a2]] |
| [[tt83-2025]] | governs | [[net-interest-income-sensitivity]] | — · VN | [[src-tt83-2025-nhnn#^d53-1a2]] |
| [[tt83-2025]] | governs | [[irrbb-standardised-framework]] | — · VN | [[src-tt83-2025-nhnn#^d53-1a2]] |
| [[tt83-2025]] | governs | [[rwa-irrbb]] | — · VN | [[src-tt83-2025-nhnn#^pl6-1c]] |
| [[rwa-irrbb]] | part-of | [[economic-capital]] | — · VN | [[src-tt83-2025-nhnn#^pl6-1b]] |

TT83 là căn cứ; d368 chỉ là tham chiếu.

| Nội dung | TT83/2025 | Nguồn |
|---|---|---|
| Chỉ số đo | Phải gồm ΔNII và ΔEVE, cách tính theo Phụ lục V | [[src-tt83-2025-nhnn#^d53-1a2]] |
| Hạn mức | Tối thiểu hạn mức ΔNII và ΔEVE | [[src-tt83-2025-nhnn#^d53-2]] |
| Lộ trình | 01/07/2026–31/12/2027: ΔNII hoặc ΔEVE | [[src-tt83-2025-nhnn#^d74-4a]] |
| Lộ trình | Chậm nhất từ 01/01/2028: cả ΔNII và ΔEVE | [[src-tt83-2025-nhnn#^d74-4b]] |
| Kịch bản ΔEVE | 6 kịch bản như d368 | [[src-tt83-2025-nhnn#^pl5-a3-1]] |
| Chiết khấu | Lãi kép liên tục theo risk-free rate | [[src-tt83-2025-nhnn#^pl5-a3-2]] |
| KAO | Ngân hàng tự đo (nếu có) | [[src-tt83-2025-nhnn#^pl5-a4]] |
| Tổng hợp ΔEVE | Cộng khoản giảm dương của mọi đồng tiền, lấy kịch bản lớn nhất | [[src-tt83-2025-nhnn#^pl5-a5]] |
| ΔNII | 01 năm, constant balance sheet | [[src-tt83-2025-nhnn#^pl5-b2]] |
| Kịch bản ΔNII | Tăng và giảm song song, lấy mức giảm lớn nhất | [[src-tt83-2025-nhnn#^pl5-b3]] |
| Tham số sốc | Bảng 5 có 21 đồng tiền, không có VND | [[src-tt83-2025-nhnn#^pl5-c1-1]] |
| Tham số sốc VND | Bình quân lãi suất hằng ngày 16 năm (9 kỳ hạn 3 tháng–20 năm) nhân 60% / 85% / 40%; sàn 100 bp; trần 400 / 500 / 300 bp | [[src-tt83-2025-nhnn#^pl5-c1-2]] [[src-tt83-2025-nhnn#^pl5-c1-2b]] |
| Phương án khác | Tự xác định cú sốc theo hướng dẫn cập nhật của BCBS (chú thích dẫn d578, 2024) | [[src-tt83-2025-nhnn#^pl5-c2]] |
| Vốn | Chậm nhất từ 01/01/2028, $RWA_{IRRBB}$ tính theo ΔEVE | [[src-tt83-2025-nhnn#^pl6-1c]] |
| Báo cáo ICAAP | Mô tả phương pháp $RWA_{IRRBB}$, điểm mạnh, hạn chế, điều chỉnh giả định | [[src-tt83-2025-nhnn#^pl3-3b]] |
| Stress test vốn | 2 kịch bản, tối thiểu có giả định lãi suất | [[src-tt83-2025-nhnn#^d60-1]] |

Khác d368:
- TT83 không có outlier test so ΔEVE với vốn cấp 1. Hệ quả vốn của ΔEVE đi qua $RWA_{IRRBB}$ trong vốn kinh tế [[src-tt83-2025-nhnn#^pl6-1c]].
- Chân trời ΔNII là "01 năm" [[src-tt83-2025-nhnn#^pl5-b2]], còn d368 dùng 12 tháng liên tục [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- TT83 chiết khấu theo risk-free rate [[src-tt83-2025-nhnn#^pl5-a3-2]]; d368 cho phép cộng commercial margin nếu dòng tiền đã gồm margin [[src-bcbs-irrbb-2016#^irrbb-u05-19]].

---

## Bằng chứng ủng hộ

- **d368 (T2)**: quy trình 5 bước đo ΔEVE [[src-bcbs-irrbb-2016#^irrbb-u05-1]], nguyên tắc công bố ΔEVE và ΔNII [[src-bcbs-irrbb-2016#^irrbb-p08-2]] [[src-bcbs-irrbb-2016#^irrbb-p08-3]], outlier test 15% Tier 1 [[src-bcbs-irrbb-2016#^irrbb-p12-1]], tham số 6 kịch bản ở Annex 2 [[src-bcbs-irrbb-2016#^irrbb-u07-3]] [[src-bcbs-irrbb-2016#^irrbb-u07-5]].
- **TT83/2025 (T1)**: chép cấu trúc 6 kịch bản, công thức xoay trục và cách dựng tham số sốc của d368 [[src-tt83-2025-nhnn#^pl5-a3-1]] [[src-tt83-2025-nhnn#^pl5-c1-2]] [[src-tt83-2025-nhnn#^pl5-c1-3]].
- **Tata (T4)**: giá trị kinh tế là tổng hiện giá dòng tiền tương lai [[src-tata-bank-alm#^tata-ev-1]]; rủi ro lãi suất chỉ tính tới ngày tái định giá kế tiếp [[src-tata-bank-alm#^tata-gap-2]]; earning gap cho độ nhạy NII năm đầu [[src-tata-bank-alm#^tata-egap-1]].
- **Choudhry (T4)**: IRRBB tác động qua góc độ vốn (giá trị kinh tế) và góc độ thu nhập (NII 12 tháng) [[src-choudhry-principles-banking#^choudhry-irrbb-3]].

---

## Bằng chứng trái chiều

- d368: nếu ngân hàng chỉ triệt tiêu rủi ro giá trị kinh tế bằng cách khớp kỳ tái định giá ngoài kỳ hạn ngắn, ngân hàng có thể chịu rủi ro biến động thu nhập [[src-bcbs-irrbb-2016#^irrbb-u02-4]]. Tata: EVE và NII thường phản ứng ngược chiều trước cùng một biến động lãi suất [[src-tata-bank-alm#^tata-nii-11]].
- Tata: muốn không là outlier theo cả SOT EVE và SOT NII, ngân hàng phải đặt tỷ trọng tài sản cố định trong một vùng; vùng này có thể rất hẹp và dịch chuyển theo thay đổi khối lượng [[src-tata-bank-alm#^tata-sot-4]]. *Diễn giải:* d368 và TT83 không có ngưỡng NII, nên ràng buộc kép này là đặc thù EU.
- Choudhry: gap analysis vẫn được dùng rộng rãi vì dữ liệu sẵn và dễ giải thích, dù bỏ qua time value và tăng trưởng [[src-choudhry-principles-banking#^choudhry-irr-8]].

---

## Phụ thuộc regime

- **Lãi suất âm hoặc rất thấp**:
  - EBA yêu cầu xét kịch bản lãi suất âm, tác động bất đối xứng và ràng buộc tái định giá tiền gửi bán lẻ [[src-tata-bank-alm#^tata-neg-5]]. Xem [[negative-interest-rates]].
  - Choudhry: tiền gửi bán lẻ và SME có sàn 0,00% nên được coi như sản phẩm fixed-rate; khi đó có thể dùng IRS nhận cố định với tenor bằng behavioural tenor của NMD [[src-choudhry-principles-banking#^choudhry-neg-3]].
  - d368 cho supervisor quốc gia đặt sàn lãi suất sau sốc, không lớn hơn 0 [[src-bcbs-irrbb-2016#^irrbb-u07-11]].
  - *Diễn giải:* trong kịch bản Parallel down, phần NMD có sàn 0% không giảm lãi theo, nên ΔNII dưới sốc giảm phụ thuộc mạnh vào giả định sàn. Sàn lãi suất sau sốc (Q3 mục 5) giới hạn mức giảm của lãi suất thị trường.
- **Đường cong đảo ngược**: *Diễn giải:* (ngoài wiki, chưa có nguồn) với ngân hàng có nợ tái định giá ngắn và tài sản cố định dài, flattener làm giảm NII 12 tháng qua chi phí nợ; tác động lên EVE tuỳ cấu trúc vị thế theo kỳ hạn.
- **Jurisdiction**: VN theo TT83 không có outlier test, EU có SOT EVE và SOT NII, d368 chỉ bắt buộc phép thử EVE (Q1, Q4).

---

## Hàm ý ALM / quy định

- **VN (căn cứ)**: trong giai đoạn 01/07/2026–31/12/2027, ngân hàng được chọn một trong hai chỉ tiêu [[src-tt83-2025-nhnn#^d74-4a]]. *Diễn giải:* vì $RWA_{IRRBB}$ tính theo ΔEVE chậm nhất từ 01/01/2028 [[src-tt83-2025-nhnn#^pl6-1c]], ngân hàng cần có dữ liệu ΔEVE trước mốc này, kể cả khi đang dùng ΔNII.
- **Tham số sốc VND**: ngân hàng tự tính theo PL5.C.I.2 [[src-tt83-2025-nhnn#^pl5-c1-2]] hoặc tự xác định theo hướng dẫn BCBS cập nhật [[src-tt83-2025-nhnn#^pl5-c2]]. *Diễn giải:* hai cách cho kết quả khác nhau; lựa chọn phải được thuyết minh trong báo cáo ICAAP [[src-tt83-2025-nhnn#^pl3-3b]].
- **ALCO**: *Diễn giải:* [[alco]] có thể đặt hai hạn mức riêng cho ΔEVE (góc độ vốn) và ΔNII (góc độ thu nhập), tương ứng hai góc độ Choudhry mô tả [[src-choudhry-principles-banking#^choudhry-irrbb-3]]. Ở VN đây là nghĩa vụ tối thiểu [[src-tt83-2025-nhnn#^d53-2]].
- **Phòng ngừa**: *Diễn giải:* sáu kịch bản tác động khác nhau lên từng dải kỳ hạn, nên ngân hàng có thể dùng [[interest-rate-swap]], [[swaption]], [[interest-rate-cap-floor]] để phòng ngừa theo điểm kỳ hạn thay vì chỉ theo sốc song song. Xem [[irrbb-casa-replicating-portfolio-and-irs-hedging]].

---

## Bất định
- Biên độ sốc VND: có phương pháp tính [[src-tt83-2025-nhnn#^pl5-c1-2]]; giá trị bp cụ thể phụ thuộc chuỗi lãi suất ngân hàng chọn, wiki chưa có số liệu `[cần nguồn]`.
- Ngưỡng outlier tại Việt Nam: không có trong C3-M7, PL5 (đã ingest [2026-10-19]). Ứng viên: PL6 (raw dòng 2794 có `RWA_IRRBB`, tài sản tính theo rủi ro IRRBB) và C3-M9 (ICAAP) `[cần nguồn: src-tt83-2025-nhnn PL6, C3-M9]`. → đã rà [2026-10-20]: PL6, C3-M9 đã ingest; TT83 không có outlier test, ΔEVE đi vào $RWA_{IRRBB}$ (Q4).
- Table 1 Annex 2 (biên độ Parallel/Short/Long theo đồng tiền): giá trị USD, EUR, JPY ở mục Q3 khớp raw u07 dòng 947–955, nhưng claim [[src-bcbs-irrbb-2016#^irrbb-u07-2]] chưa chép bảng. Unit u07 đã `done`; cần `/ingest src-bcbs-irrbb-2016 u07` bổ sung claim Table 1. → đã bổ sung [2026-10-18]: [[src-bcbs-irrbb-2016#^irrbb-u07-5]].
- Claim [[src-bcbs-irrbb-2016#^irrbb-u07-4]] ghi "sàn không âm hoặc sàn âm cho lãi suất sau sốc", trong khi trích nguyên văn nói supervisor có thể đặt "a higher floor … for their home currency". Synthesis này đã viết theo trích dẫn; claim source note cần sửa qua `/lint` hoặc `/ingest`. → đã sửa diễn đạt claim [2026-10-18] (trích dẫn và block-id giữ nguyên).
- Sàn lãi suất sau sốc (post-shock floor) và mô hình định giá quyền chọn cho $\text{KAO}$: `[cần nguồn]`; có thể nằm trong u07 (Annex 2) hoặc u05 par 130–131. → đã rà [2026-10-20]: sàn EBA có nguồn qua Tata (reg-8, sot-2). Raw d368 u07 dòng 979 và 1048 nói supervisor quốc gia có thể đặt sàn lãi suất sau sốc, chưa có claim. Mô hình định giá KAO vẫn `[cần nguồn]`. → đã ingest [2026-10-20]: [[src-bcbs-irrbb-2016#^irrbb-u07-11]]; Q3 mục 5 cập nhật.
- Dynamic balance sheet cho $\Delta\text{NII}$: `[cần nguồn]`; claim đã ingest của d368 (p08-3) chỉ nêu constant balance sheet. → đã rà [2026-10-20]: raw d368 có đoạn chưa ingest: u03 footnote 9 (dòng 154, dynamic view hữu ích cho lập kế hoạch nhưng phụ thuộc biến khó dự báo); u06 dòng 784–809 (earnings measure theo run-off, static, dynamic balance sheet; dynamic là "the most meaningful approach") và dòng 918. → đã ingest [2026-10-20]: [[src-bcbs-irrbb-2016#^irrbb-p04-4]], [[src-bcbs-irrbb-2016#^irrbb-u06-8]], [[src-bcbs-irrbb-2016#^irrbb-u06-9]], [[src-bcbs-irrbb-2016#^irrbb-u06-10]]; Q2 cập nhật.
- [2026-10-20] research: hàm sốc dài hạn $S_{long}(t_k) = 1 - S_{short}(t_k)$ của d368 (raw u07 dòng 969–971) chưa có claim; Q3 dùng claim TT83 [[src-tt83-2025-nhnn#^pl5-c1-3]]. → đã ingest [2026-10-20]: [[src-bcbs-irrbb-2016#^irrbb-u07-10]].
- [2026-10-20] research: TT83 PL5.C.II dẫn BCBS d578 (hiệu chỉnh cú sốc IRRBB 2024) [[src-tt83-2025-nhnn#^pl5-c2]]; d578 chưa có trong registry.

## Liên Kết Quan Hệ
- **Đầu vào từ**: [[repricing-balance-sheet]], [[irrbb-balance-sheet-portfolios]], [[non-maturity-deposits]], [[notional-repricing-cash-flow]], [[repricing-gap-analysis]]
- **Chỉ số đo lường**: [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[outlier-bank-test]], [[rwa-irrbb]], [[net-interest-margin]]
- **Kịch bản & Mô hình**: [[standardised-interest-rate-shocks]], [[irrbb-standardised-framework]], [[key-rate-duration]], [[duration-gap-model]]
- **Quy định giám sát**: [[bcbs-irrbb]], [[tt83-2025]]
- **Synthesis liên quan**: [[irrbb-alm-governance-strategy-and-tradeoffs]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]]
