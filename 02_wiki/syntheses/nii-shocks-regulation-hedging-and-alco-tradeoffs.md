---
title: "Quản trị Thu nhập Lãi thuần (NII): Kịch bản Sốc, Khung Pháp quy Basel vs NHNN, Công cụ Phòng ngừa và Đánh đổi Chiến lược tại ALCO"
aliases:
  - "NII Shocks, Regulation, Hedging and ALCO Tradeoffs"
  - "Quản trị NII: Kịch bản sốc, Khung pháp quy và Đánh đổi ALCO"
  - "Sốc lãi suất NII, Phòng ngừa và Chiến lược ALCO"
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Q5. Các kịch bản sốc lãi suất chuẩn hóa (Parallel Up/Down, Flattener, Steepener, Short Rate...) tác động như thế nào đến NII? Làm thế nào để phân tách tác động của biến động lãi suất thị trường (base rate) khỏi biên thương mại (commercial margin / FTP spread) và rủi ro cơ sở (basis risk)? · Q6. Chuẩn mực BCBS (BCBS d368 / SRP31) và quy định của NHNN Việt Nam (Thông tư 83/2025/TT-NHNN, C3-M7 và Phụ lục 5) quy định nghĩa vụ đo lường, báo cáo và kiểm tra sức chịu đựng (stress testing) đối với NII/EaR như thế nào? Có những điểm khác biệt cốt lõi nào giữa Basel và NHNN về khung đo lường NII? · Q7. Ngân hàng quản trị và phòng ngừa rủi ro NII thông qua những công cụ nào (cơ chế truyền dẫn FTP, chính sách định giá cho vay/tiền gửi, danh mục đầu tư sao chép CASA - replicating portfolio, và phái sinh hoán đổi lãi suất - IRS / cap/floor)? · Q8. Hội đồng ALCO giải quyết bài toán đánh đổi chiến lược giữa tối ưu hóa NII trong ngắn hạn (12 tháng) và bảo vệ giá trị kinh tế dài hạn của vốn chủ sở hữu (EVE), cũng như đánh đổi giữa NIM và chi phí đệm thanh khoản (LCR/NSFR/HQLA carry cost) như thế nào?"
as_of: 2026-10-20
sources:
  - "[[src-bcbs-irrbb-2016]]"
  - "[[src-tt83-2025-nhnn]]"
  - "[[src-tata-bank-alm]]"
  - "[[src-choudhry-principles-banking]]"
  - "[[src-lubinska-alm-optimisation]]"
  - "[[src-ftp-transmission-analysis]]"
relations: []
tags: [nii, shocks, bcbs-d368, tt83-2025, hedging, irs, alco, tradeoffs, eve]
updated: 2026-10-20
reviewed:
---

## Câu hỏi
- **Q5**: Các kịch bản sốc lãi suất chuẩn hóa (Parallel Up/Down, Flattener, Steepener, Short Rate...) tác động như thế nào đến NII? Làm thế nào để phân tách tác động của biến động lãi suất thị trường (base rate) khỏi biên thương mại (commercial margin / FTP spread) và rủi ro cơ sở ([[basis-risk]])?
- **Q6**: Chuẩn mực BCBS ([[bcbs-irrbb]] d368 / SRP31) và quy định của NHNN Việt Nam ([[tt83-2025]], C3-M7 và Phụ lục 5) quy định nghĩa vụ đo lường, báo cáo và kiểm tra sức chịu đựng (stress testing) đối với NII/EaR như thế nào? Có những điểm khác biệt cốt lõi nào giữa Basel và NHNN về khung đo lường NII?
- **Q7**: Ngân hàng quản trị và phòng ngừa rủi ro NII thông qua những công cụ nào (cơ chế truyền dẫn [[funds-transfer-pricing|FTP]], chính sách định giá cho vay/tiền gửi, danh mục đầu tư sao chép CASA — [[replicating-portfolio-model]], và phái sinh hoán đổi lãi suất — [[interest-rate-swap|IRS]] / [[interest-rate-cap-floor|cap/floor]])?
- **Q8**: Hội đồng [[alco|ALCO]] giải quyết bài toán đánh đổi chiến lược giữa tối ưu hóa NII trong ngắn hạn (12 tháng) và bảo vệ giá trị kinh tế dài hạn của vốn chủ sở hữu ([[economic-value-of-equity|EVE]]), cũng như đánh đổi giữa [[net-interest-margin|NIM]] và chi phí đệm thanh khoản ([[lcr-nsfr-interlinkages]] / carry cost của [[hqla]]) như thế nào?

Synthesis này đi tiếp [[irrbb-standardised-shocks-eve-and-nii-measurement]] (cấu trúc 6 kịch bản sốc, cách đo ΔNII, bảng nghĩa vụ TT83) và [[nii-nature-repricing-mechanisms-and-planning]] (Q1–Q4 của cùng bộ câu hỏi). Phần đã viết ở đó chỉ được tóm lại ở đây.

## Kết luận
- **Q5**: Với NII, d368 chỉ dùng 2 kịch bản sốc song song (tăng, giảm); 4 kịch bản còn lại (steepener, flattener, short up/down) dùng cho EVE [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. ΔNII công bố nên tính trên bảng cân đối không đổi, kỳ 12 tháng, và **bao gồm** biên thương mại cùng các thành phần spread [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Việc tách base rate khỏi biên thương mại không làm trong phép đo mà làm qua FTP: đơn vị kinh doanh chỉ còn biên cố định (lãi suất khách hàng − FTP), còn ALM nhận toàn bộ chênh lệch tái định giá [[src-ftp-transmission-analysis#^ftp-trans-10]]. Basis risk được đo riêng, theo cơ sở lãi suất của từng khoản mục [[src-bcbs-irrbb-2016#^irrbb-u06-4]] [[src-choudhry-principles-banking#^choudhry-alco-19]].
- **Q6**: d368 yêu cầu công bố ΔNII dưới các kịch bản sốc quy định [[src-bcbs-irrbb-2016#^irrbb-p08-1]]. Phép thử ngoại lai bắt buộc chỉ áp lên ΔEVE (15% Tier 1) [[src-bcbs-irrbb-2016#^irrbb-p12-1]]; phép thử dựa trên thu nhập là tuỳ chọn của supervisor [[src-bcbs-irrbb-2016#^irrbb-p12-2]]. TT83 bắt buộc đo cả ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-1a2]], đặt hạn mức cho cả hai [[src-tt83-2025-nhnn#^d53-2]], đo và báo cáo nội bộ tối thiểu hằng quý [[src-tt83-2025-nhnn#^d54-1a]] [[src-tt83-2025-nhnn#^d55-1]]. ΔNII theo TT83 tính trong 1 năm, bảng cân đối không đổi, lấy mức giảm lớn nhất giữa 2 kịch bản song song [[src-tt83-2025-nhnn#^pl5-b2]] [[src-tt83-2025-nhnn#^pl5-b3]]. Wiki chưa có claim nào cho thấy TT83 đặt ngưỡng ngoại lai định lượng.
- **Q7**: Nguồn đã ingest nêu 5 nhóm công cụ:
  1. FTP: chuyển rủi ro lãi suất về ALM [[src-tata-bank-alm#^tata-prac-4]].
  2. Định giá cho vay: spread trên chi phí vốn, kèm sàn TRR do ALCO kiểm soát [[src-choudhry-principles-banking#^choudhry-lp-5]] [[src-choudhry-principles-banking#^choudhry-lp-6]].
  3. Replicating portfolio cho tiền gửi không kỳ hạn và vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
  4. Receiver IRS: ổn định NII khi lãi suất giảm [[src-tata-bank-alm#^tata-nii-16]].
  5. Cap cho ngân hàng liability-sensitive, floor cho ngân hàng asset-sensitive [[src-choudhry-principles-banking#^choudhry-hedge-20]] [[src-choudhry-principles-banking#^choudhry-hedge-25]].

  Choudhry khuyến nghị phòng ngừa trên phần ròng sau khi tận dụng natural hedge, và khi có thể thì ưu tiên sản phẩm tiền mặt [[src-choudhry-principles-banking#^choudhry-cs-17]].
- **Q8**: d368 nêu đánh đổi ngay trong khung chuẩn: chỉ khớp tái định giá để giảm rủi ro giá trị kinh tế thì ngân hàng có thể chịu biến động thu nhập [[src-bcbs-irrbb-2016#^irrbb-u02-4]]. Ví dụ của Tata: receiver swap ổn định NII khi sốc −100 bp [[src-tata-bank-alm#^tata-nii-16]], nhưng repricing gap tăng từ 1,74 lên 3,63 [[src-tata-bank-alm#^tata-nii-10]]; mỗi đơn vị repricing gap tương ứng mức giảm EVE khi lãi suất tăng 1% [[src-tata-bank-alm#^tata-gap-7]]. Về thanh khoản, ví dụ của Choudhry: tăng đệm thanh khoản với net cost of carry 3% làm NII giảm £45m và NIM giảm 0,50 điểm % [[src-choudhry-principles-banking#^choudhry-nim-5]]. Theo Lubinska, ALCO có thể đưa hạn mức biến động NII và các tỷ lệ thanh khoản vào bài toán tối ưu dưới dạng ràng buộc bất đẳng thức [[src-lubinska-alm-optimisation#^lubinska-u04-12]].

## Cơ chế

### Q5 — Sốc chuẩn hoá tác động lên NII và cách tách base rate, margin, basis

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[standardised-interest-rate-shocks]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-p08-1]] |
| [[basis-risk]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-4]] |
| [[net-interest-income-sensitivity]] | measures | [[basis-risk]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-4]] |
| [[tt83-2025]] | governs | [[standardised-interest-rate-shocks]] | | [[src-tt83-2025-nhnn#^pl5-c1-1]] |

**Kịch bản nào áp cho NII.**
- d368 nêu ngân hàng nên áp 6 kịch bản cho EVE (parallel và non-parallel gap risk) và 2 kịch bản cho NII [[src-bcbs-irrbb-2016#^irrbb-u07-1]].
- TT83 dùng đúng 2 kịch bản song song để đo ΔNII [[src-tt83-2025-nhnn#^pl5-b3]].
- Cấu trúc sốc ngắn hạn, dài hạn, xoay trục và sàn sau sốc nằm ở [[standardised-interest-rate-shocks]] và [[irrbb-standardised-shocks-eve-and-nii-measurement]].

**Biên độ.**
- Table 1 của d368: sốc song song 200 bp cho USD và EUR, 250 bp cho GBP, 100 bp cho JPY [[src-bcbs-irrbb-2016#^irrbb-u07-5]].
- Bảng 5 của TT83 không có VND [[src-tt83-2025-nhnn#^pl5-c1-1]]. Đồng tiền không có trong Bảng 5 thì ngân hàng tự hiệu chỉnh: dùng chuỗi lãi suất hằng ngày 16 năm, có sàn 100 bp và trần 400 bp cho sốc song song [[src-tt83-2025-nhnn#^pl5-c1-2]].
- *Diễn giải:* vì vậy "±400 bp cho VND" chỉ là trần, không phải tham số cố định; con số thật phụ thuộc chuỗi dữ liệu ngân hàng dùng.

**Sàn lãi suất sau sốc.**
- Supervisor quốc gia có thể đặt sàn cho lãi suất sau sốc, với điều kiện sàn không lớn hơn 0 [[src-bcbs-irrbb-2016#^irrbb-u07-11]].
- *Diễn giải:* sàn này giới hạn mức giảm của kịch bản parallel down, nên ở vùng lãi suất thấp nó trực tiếp thu hẹp ΔNII của ngân hàng asset-sensitive.

**Chiều tác động phụ thuộc cấu trúc tái định giá, không phụ thuộc kịch bản.**
- NII và NIM thay đổi theo lãi suất vì tài sản và nợ tái định giá ở các thời điểm khác nhau [[src-choudhry-principles-banking#^choudhry-nim-9]].
- Ngân hàng dùng nhiều nợ thả nổi để tài trợ tài sản cố định là liability-sensitive: lãi suất tăng làm NII giảm [[src-choudhry-principles-banking#^choudhry-hedge-20]].
- Ngân hàng asset-sensitive làm ngược lại [[src-choudhry-principles-banking#^choudhry-hedge-25]].

**Giả định bảng cân đối và chân trời.**
- ΔNII công bố theo d368 dùng constant balance sheet, kỳ 12 tháng [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. TT83 dùng 1 năm, constant balance sheet [[src-tt83-2025-nhnn#^pl5-b2]].
- Cho quản trị nội bộ, Annex 1 của d368 nêu chân trời thường 1–3 năm, không quá 5 năm [[src-bcbs-irrbb-2016#^irrbb-u06-8]]. Annex 1 cũng nêu ba trạng thái run-off, constant và dynamic, trong đó dynamic là cách có ý nghĩa nhất [[src-bcbs-irrbb-2016#^irrbb-u06-9]].
- ΔNII là chênh lệch NII kỳ vọng giữa kịch bản cơ sở (theo kế hoạch kinh doanh) và kịch bản stress [[src-bcbs-irrbb-2016#^irrbb-u06-10]].
- Dynamic view hữu ích cho lập kế hoạch nhưng có thể che giấu rủi ro nền tảng [[src-bcbs-irrbb-2016#^irrbb-p04-4]].
- Theo Tata, sai số trong dự báo NII cơ sở phần lớn triệt tiêu khi lấy kịch bản sốc trừ kịch bản cơ sở [[src-tata-bank-alm#^tata-nii-3]].

**Tách base rate, biên thương mại và basis.**
- Trong phép đo, d368 giữ biên thương mại *trong* ΔNII: dòng tiền dự kiến nên gồm biên thương mại và các thành phần spread khác [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- Với ΔEVE, dòng tiền có thể chiết khấu bằng lãi suất phi rủi ro, hoặc lãi suất phi rủi ro cộng biên thương mại nếu dòng tiền đã gồm biên đó [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- Quy định EU (qua Tata, T4) cũng tách như vậy: SOT NII phải gồm biên thương mại, còn SOT EVE có thể loại ra [[src-tata-bank-alm#^tata-sot-3]].
- Khi đánh giá IRRBB, supervisor nên xét tác động của việc giữ hay loại biên thương mại [[src-bcbs-irrbb-2016#^irrbb-p12-5]].
- Việc tách diễn ra ở tầng tổ chức, qua FTP. Theo nguồn T5, FTP tách IRRBB khỏi đơn vị kinh doanh và chuyển toàn bộ về ALM [[src-ftp-transmission-analysis#^ftp-trans-9]]. Đơn vị kinh doanh chỉ thấy biên cố định (lãi suất khách hàng − FTP), còn ALM kế thừa toàn bộ chênh lệch tái định giá [[src-ftp-transmission-analysis#^ftp-trans-10]]. Tata mô tả cùng cơ chế: rủi ro được chuyển về profit center rủi ro lãi suất trong ALM [[src-tata-bank-alm#^tata-prac-4]].
- Basis risk là tác động của thay đổi tương đối giữa các chỉ số lãi suất khác nhau trên công cụ cùng kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u06-4]]. Trang "Basis Risk" trong ALCO pack của Choudhry phân loại tài sản và nợ theo cơ sở lãi suất (cố định, administered, Bank Base Rate, không chịu lãi), và cột mismatch là tài sản trừ nợ [[src-choudhry-principles-banking#^choudhry-alco-19]]. Tài sản tái định giá thưa hơn nợ cũng tạo rủi ro khi lãi suất tăng; Choudhry gọi đây là "secondary IRR", một dạng basis risk [[src-choudhry-principles-banking#^choudhry-hedge-20]].

*Diễn giải (ngoài wiki, chưa có nguồn):* có thể viết lãi suất sản phẩm thành
$$r_{\text{sản phẩm}} = r_{\text{FTP}} + m_{\text{thương mại}}$$
trong đó $r_{\text{FTP}}$ bám theo chỉ số thị trường, và phần chênh giữa chỉ số định giá của khách hàng với chỉ số của đường FTP là basis. Sốc chuẩn hoá tác động lên $r_{\text{FTP}}$, tức lên sổ của ALM; $m$ giữ cố định trong ΔNII constant balance sheet. Nguồn đã ingest không đưa ra công thức này.

### Q6 — Nghĩa vụ đo, báo cáo, stress NII: d368 và TT83

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[bcbs-irrbb]] | governs | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u01-4]] |
| [[tt83-2025]] | governs | [[net-interest-income-sensitivity]] | | [[src-tt83-2025-nhnn#^d53-1a2]] |
| [[net-interest-income-sensitivity]] | input-to | [[outlier-bank-test]] | | [[src-bcbs-irrbb-2016#^irrbb-p12-2]] |
| [[outlier-bank-test]] | limits | [[economic-value-of-equity]] | | [[src-bcbs-irrbb-2016#^irrbb-p12-1]] |

| Tiêu chí | BCBS d368 (tham chiếu) | TT83/2025 (nghĩa vụ tại VN) |
|---|---|---|
| Chỉ tiêu bắt buộc | Công bố ΔEVE và ΔNII dưới kịch bản sốc quy định [[src-bcbs-irrbb-2016#^irrbb-u01-4]] | Phải gồm ΔNII và ΔEVE, tính theo PL5 [[src-tt83-2025-nhnn#^d53-1a2]] |
| Kịch bản cho NII | 2 kịch bản song song [[src-bcbs-irrbb-2016#^irrbb-u07-1]] | 2 kịch bản song song; lấy mức giảm lớn nhất [[src-tt83-2025-nhnn#^pl5-b3]] |
| Chân trời, giả định | 12 tháng, constant balance sheet, gồm biên thương mại [[src-bcbs-irrbb-2016#^irrbb-p08-3]] | 1 năm, constant balance sheet [[src-tt83-2025-nhnn#^pl5-b2]] |
| Kịch bản nội bộ, stress | IMS phải tính: kịch bản nội bộ theo ICAAP, stress lịch sử và giả định, 6 kịch bản Annex 2, kịch bản supervisor yêu cầu, và reverse stress test [[src-bcbs-irrbb-2016#^irrbb-p04-3]] | Đo lường phải kiểm tra sức chịu đựng qua ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d54-3b]]; quy định nội bộ về stress test phải nêu tần suất [[src-tt83-2025-nhnn#^d23-2]] |
| Hạn mức | Policy limits phù hợp quy mô, độ phức tạp; nên đặt risk tolerance riêng cho gap, basis, option risk [[src-bcbs-irrbb-2016#^irrbb-p03-5]] | Phải có hạn mức tối thiểu cho ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-2]] |
| Tần suất nội bộ | Không ghi nhận trong nguồn đã ingest | Đo lường, theo dõi tối thiểu hằng quý [[src-tt83-2025-nhnn#^d54-1a]]; báo cáo nội bộ hằng quý, gồm ΔNII, ΔEVE, tuân thủ hạn mức [[src-tt83-2025-nhnn#^d55-1]] |
| Ngoại lai | Bắt buộc với ΔEVE, ngưỡng 15% Tier 1 [[src-bcbs-irrbb-2016#^irrbb-p12-1]]; supervisor có thể thêm phép thử dựa trên thu nhập, ngưỡng nên chặt ít nhất bằng 15% Tier 1 [[src-bcbs-irrbb-2016#^irrbb-p12-2]] | Wiki chưa có claim về ngưỡng ngoại lai trong TT83 [cần nguồn] |
| NII đe doạ hoạt động | Ngân hàng có thể bị coi là rủi ro quá mức nếu ΔNII sau sốc không đủ duy trì hoạt động bình thường [[src-bcbs-irrbb-2016#^irrbb-p12-7]] | Không ghi nhận trong nguồn đã ingest |
| Đo theo đồng tiền | Xem [[irrbb-standardised-shocks-eve-and-nii-measurement]] | Đo riêng đồng tiền chiếm từ 5% tổng tài sản hoặc tổng nợ trên sổ ngân hàng [[src-tt83-2025-nhnn#^d54-3c]] |

- EU (qua Tata, T4) có SOT riêng cho NII: suy giảm NII 1 năm so với Tier 1 vượt 5% [[src-tata-bank-alm#^tata-sot-3]]. Đây là lựa chọn của jurisdiction EU, không phải tham số d368.
- *Diễn giải:* khác biệt cốt lõi là TT83 biến ΔNII thành **hạn mức nội bộ bắt buộc**, còn d368 dùng ΔNII chủ yếu cho công bố và cho đánh giá định tính của supervisor. Cả hai đều chỉ dùng 2 kịch bản song song cho NII và giả định constant balance sheet.

### Q7 — Công cụ quản trị và phòng ngừa NII

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[replicating-portfolio-model]] | hedges | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-6]] |
| [[structural-hedging]] | hedges | [[gap-risk]] | | [[src-choudhry-principles-banking#^choudhry-cs-17]] |
| [[interest-rate-swap]] | hedges | [[net-interest-income-sensitivity]] | falling_rate (receiver) | [[src-tata-bank-alm#^tata-nii-16]] |
| [[interest-rate-cap-floor]] | hedges | [[net-interest-income-sensitivity]] | | [[src-choudhry-principles-banking#^choudhry-hedge-20]] |

**1. FTP: chuyển rủi ro về ALM.**
- FTP cho phép ALM thành profit center: rủi ro được chuyển về ALM, ALM quyết định có phòng ngừa ra thị trường hay không [[src-tata-bank-alm#^tata-prac-4]].
- Tại VN, bộ phận ALM có trách nhiệm đề xuất nguyên tắc xây dựng giá điều chuyển vốn nội bộ, xây dựng khung lãi suất và khung giá sản phẩm, và kiểm soát tuân thủ hạn mức IRRBB [[src-tt83-2025-nhnn#^d25-3]].
- Choudhry ghi nhận một trường hợp: trước khi rà soát, mảng kinh doanh không biết khoảng 10% số dư tiền gửi cho NII âm, tức lãi suất khách hàng cao hơn FTP bid [[src-choudhry-principles-banking#^choudhry-cs-20]].

**2. Định giá cho vay và tiền gửi.**
- Lãi suất cho vay là spread trên chi phí vốn, tính từ RoE mục tiêu, credit spread bù tổn thất dự kiến và chi phí vận hành. Chi phí duy trì đệm HQLA có thể được bù ở nơi khác, không nhất thiết trong mô hình định giá khoản vay [[src-choudhry-principles-banking#^choudhry-lp-5]].
- Mô hình định giá có sàn "Target Rate of Return Floor Rate (TRR)". ALCO được Board uỷ quyền phê duyệt khoản vay dưới sàn này [[src-choudhry-principles-banking#^choudhry-lp-6]].
- Với tiền gửi: khoảng 12% số dư rút ngay chịu chi phí đệm dòng ra LCR cao nhất. Các số dư giá cao rất nhạy lãi suất, dễ rời đi nếu giảm lãi suất [[src-choudhry-principles-banking#^choudhry-cs-20]].

**3. Replicating portfolio.**
- Mục đích: tạo kỳ hạn bình quân ổn định cho tiền gửi không kỳ hạn và vốn chủ sở hữu. Ví dụ của d368: tái đầu tư 1/60 mỗi tháng vào kỳ hạn 5 năm cho kỳ hạn bình quân 2,5 năm và lợi suất bằng trung bình trượt của lãi suất 5 năm [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
- Danh mục gồm chủ yếu công cụ thanh khoản, giao dịch được, mô phỏng khối lượng và lãi suất kỳ vọng của sản phẩm không kỳ hạn [[src-tata-bank-alm#^tata-nmd-3]].
- Chi tiết: [[irrbb-casa-replicating-portfolio-and-irs-hedging]].

**4. IRS.**
- Receiver swap (nhận cố định, trả thả nổi) là một cách hưởng lợi hoặc phòng ngừa khi lãi suất giảm [[src-tata-bank-alm#^tata-nii-9]].
- Ví dụ của Tata: swap 3 năm, notional EUR 100, nhận cố định 4,16%, chân thả nổi 3,95% tái định giá 6 tháng [[src-tata-bank-alm#^tata-nii-15]]. Hedge giúp ổn định NII dưới sốc −100 bp, đặc biệt ở giai đoạn 13–24 tháng [[src-tata-bank-alm#^tata-nii-16]].

**5. Cap và floor.**
- Ngân hàng liability-sensitive có thể phòng ngừa bằng interest-rate cap [[src-choudhry-principles-banking#^choudhry-hedge-20]].
- Ví dụ: mua cap notional 80 triệu USD, bằng funding gap chịu rủi ro, loại bỏ hoàn toàn EAR. Strike out-of-the-money rẻ hơn nhưng để lại một phần EAR [[src-choudhry-principles-banking#^choudhry-hedge-23]].
- Ngân hàng asset-sensitive mua floor [[src-choudhry-principles-banking#^choudhry-hedge-25]].

**Chọn công cụ.**
- Nên phòng ngừa phần ròng tài sản − nợ sau khi khớp tenor hành vi, tận dụng natural hedge; khi có thể nên dùng sản phẩm tiền mặt thay phái sinh, ví dụ để giữ hạn mức swap [[src-choudhry-principles-banking#^choudhry-cs-17]].
- Ngược lại, điều chỉnh bằng sản phẩm tiền mặt không làm ngay được; phái sinh điều chỉnh phơi nhiễm tức thời [[src-choudhry-principles-banking#^choudhry-hedge-22]].
- Theo d368, sáng kiến phòng ngừa lớn nên được phê duyệt trước, và nên có bộ hạn mức riêng cho chiến lược phòng ngừa bằng phái sinh [[src-bcbs-irrbb-2016#^irrbb-p03-6]].
- TT83 yêu cầu nhận dạng cả rủi ro mới phát sinh từ hoạt động phòng ngừa IRRBB [[src-tt83-2025-nhnn#^d54-2]].

### Q8 — Đánh đổi tại ALCO: NII vs EVE, NIM vs chi phí đệm thanh khoản

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[tt83-2025]] | governs | [[alco]] | | [[src-tt83-2025-nhnn#^d6-4b]] |
| [[net-interest-income-sensitivity]] | input-to | [[balance-sheet-optimisation-model]] | | [[src-lubinska-alm-optimisation#^lubinska-u04-12]] |
| [[interest-rate-swap]] | drives | [[economic-value-of-equity]] | − · rising_rate (receiver) | *Diễn giải:* ghép [[src-tata-bank-alm#^tata-gap-7]] và [[src-tata-bank-alm#^tata-nii-10]]; chưa khai cạnh |
| [[hqla]] | drives | [[net-interest-margin]] | − | [[src-choudhry-principles-banking#^choudhry-nim-5]] |

**NII và EVE nhìn hai chân trời khác nhau.**
- Thước đo EV phản ánh thay đổi giá trị cho đến khi mọi vị thế chạy hết. Thước đo thu nhập chỉ phủ ngắn–trung hạn, nên không bắt được rủi ro tác động lên P&L sau kỳ ước lượng [[src-bcbs-irrbb-2016#^irrbb-u06-5]].
- d368 thừa nhận cần quản trị qua cả hai thước đo. Nếu chỉ giảm rủi ro giá trị kinh tế bằng cách khớp tái định giá ngoài kỳ ngắn hạn, ngân hàng có thể chịu biến động thu nhập [[src-bcbs-irrbb-2016#^irrbb-u02-4]].
- Tata: EVE và NII thường phản ứng ngược chiều trước cùng một thay đổi lãi suất [[src-tata-bank-alm#^tata-nii-11]].

**Ví dụ định lượng (Tata, T4).**
- Repricing gap 1,74 nghĩa là EVE giảm 1,74 khi lãi suất tăng 1%; với vốn chủ sở hữu 50, tương đương 3,48% vốn [[src-tata-bank-alm#^tata-gap-7]].
- Thêm receiver swap nâng repricing gap lên 3,63 [[src-tata-bank-alm#^tata-nii-10]], trong khi swap đó ổn định NII dưới sốc −100 bp [[src-tata-bank-alm#^tata-nii-16]].
- *Diễn giải:* đọc theo cùng định nghĩa, cùng một giao dịch làm mức giảm EVE khi lãi suất tăng 1% gần gấp đôi, đổi lấy sự ổn định NII khi lãi suất giảm.

**Ràng buộc kép theo quy định.**
- Ở EU (qua Tata), muốn không là outlier theo cả SOT EVE và SOT NII thì phải tối ưu tỷ trọng và duration của tài sản cố định. SOT EVE đặt cận trên và cận dưới, còn SOT NII đặt lượng tài sản cố định tối thiểu. Vùng tuân thủ có thể rất nhỏ và dịch chuyển theo khối lượng [[src-tata-bank-alm#^tata-sot-4]].
- Tại VN, TT83 buộc có hạn mức cho cả ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-2]].
- *Diễn giải:* hai hạn mức này đặt ALCO VN vào cùng dạng bài toán, chỉ khác là ngưỡng do ngân hàng tự đặt.

**NIM và chi phí đệm thanh khoản.**
- Ví dụ ChoudWest: tăng đệm thanh khoản £1,5bn tài trợ bằng nợ dài hạn. Đệm có lợi suất thấp hơn chi phí vốn dài hạn, net cost of carry 3% (7,5% − 4,5%). Kết quả: NII giảm £45m, NIM giảm 0,50 điểm % [[src-choudhry-principles-banking#^choudhry-nim-5]].
- Chi phí HQLA có thể được bù ở nơi khác, ngoài mô hình định giá khoản vay [[src-choudhry-principles-banking#^choudhry-lp-5]].
- Tiền gửi rút ngay chịu chi phí đệm dòng ra LCR cao nhất nên cho giá trị thấp nhất [[src-choudhry-principles-banking#^choudhry-cs-20]].
- Các kênh tương tác LCR–NSFR: [[lcr-nsfr-interlinkages]].

**ALCO giải bài toán thế nào.**
- *Hạn mức.* ALCO thường đặt hạn mức EAR ±5% hoặc ±10% [[src-choudhry-principles-banking#^choudhry-hedge-22]].
- *Tối ưu hoá.* Tối ưu sổ ngân hàng hầu như luôn có ràng buộc bất đẳng thức, như hạn mức biến động NII và các tỷ lệ thanh khoản ngắn và trung–dài hạn [[src-lubinska-alm-optimisation#^lubinska-u04-12]]. Lubinska dựng bài toán gồm tối đa hoá thu nhập tài sản và tối thiểu hoá chi phí vốn, dưới giả định constant balance sheet [[src-lubinska-alm-optimisation#^lubinska-u04-13]]. Chi tiết: [[balance-sheet-optimisation-model]].
- *Nhịp họp.* Quy trình phổ biến là trình ALCO hằng tháng: so NII thực tế với dự báo, kèm các kịch bản lãi suất [[src-choudhry-principles-banking#^choudhry-irr-3]]. Tại VN, ALCO họp tối thiểu mỗi quý một lần và tham mưu Tổng giám đốc về các nội dung quản lý tài sản/nợ tại Đ25.3 [[src-tt83-2025-nhnn#^d6-4b]].
- *Rà soát tiền gửi.* Nên rà soát định kỳ cấu trúc tiền gửi theo tác động lên NII và theo yêu cầu quản lý, bằng mẫu phân tích do ALCO sở hữu [[src-choudhry-principles-banking#^choudhry-cs-23]].

## Bằng chứng ủng hộ
- Đánh đổi NII–EVE có căn cứ T2: d368 par 11 [[src-bcbs-irrbb-2016#^irrbb-u02-4]] và Annex 1 [[src-bcbs-irrbb-2016#^irrbb-u06-5]]. Tata (T4) bổ sung ví dụ số [[src-tata-bank-alm#^tata-gap-7]] [[src-tata-bank-alm#^tata-nii-10]].
- Nguyên tắc "ΔNII gồm biên thương mại, constant balance sheet" thống nhất giữa d368 [[src-bcbs-irrbb-2016#^irrbb-p08-3]], EU RTS (qua Tata) [[src-tata-bank-alm#^tata-sot-3]] và TT83 về giả định bảng cân đối [[src-tt83-2025-nhnn#^pl5-b2]].
- Chi phí đệm thanh khoản lên NIM có ví dụ số cụ thể (Choudhry) [[src-choudhry-principles-banking#^choudhry-nim-5]].

## Bằng chứng trái chiều
- Cách tách base rate khỏi biên thương mại qua FTP chỉ có nguồn T5 nói thẳng [[src-ftp-transmission-analysis#^ftp-trans-10]]. Tata (T4) nói rủi ro được chuyển về ALM [[src-tata-bank-alm#^tata-prac-4]] nhưng không nói biên của đơn vị kinh doanh cố định.
- Hạn mức EAR ±5%/±10% là thực tiễn Choudhry mô tả cho một ngân hàng giả định [[src-choudhry-principles-banking#^choudhry-hedge-22]], không phải chuẩn mực. SOT NII 5% Tier 1 là quy định EU [[src-tata-bank-alm#^tata-sot-3]].
- Choudhry ưu tiên sản phẩm tiền mặt [[src-choudhry-principles-banking#^choudhry-cs-17]], nhưng cũng ghi rằng chúng không điều chỉnh được ngay [[src-choudhry-principles-banking#^choudhry-hedge-22]]. Hai ý này không mâu thuẫn mà là đánh đổi tốc độ và chi phí.
- Annex 1 gọi dynamic balance sheet là cách có ý nghĩa nhất [[src-bcbs-irrbb-2016#^irrbb-u06-9]], còn par 34 cảnh báo dynamic view có thể che giấu rủi ro [[src-bcbs-irrbb-2016#^irrbb-p04-4]]. ΔNII công bố và ΔNII theo TT83 đều dùng constant balance sheet.

## Phụ thuộc regime
- **Lãi suất tăng:** ngân hàng liability-sensitive giảm NII; công cụ là cap [[src-choudhry-principles-banking#^choudhry-hedge-20]].
- **Lãi suất giảm:** ngân hàng asset-sensitive giảm NII; công cụ là floor [[src-choudhry-principles-banking#^choudhry-hedge-25]] hoặc receiver swap [[src-tata-bank-alm#^tata-nii-9]]. Receiver swap lại làm EVE nhạy hơn khi lãi suất tăng trở lại [[src-tata-bank-alm#^tata-nii-10]].
- **Lãi suất thấp, gần 0:** sàn sau sốc (không lớn hơn 0) giới hạn kịch bản parallel down [[src-bcbs-irrbb-2016#^irrbb-u07-11]].
- **Jurisdiction:**
  - d368: ΔNII cho công bố và đánh giá của supervisor [[src-bcbs-irrbb-2016#^irrbb-p08-1]].
  - EU: thêm SOT NII 5% Tier 1 [[src-tata-bank-alm#^tata-sot-3]].
  - VN: hạn mức ΔNII nội bộ bắt buộc [[src-tt83-2025-nhnn#^d53-2]], biên độ sốc VND do ngân hàng hiệu chỉnh trong khoảng 100–400 bp [[src-tt83-2025-nhnn#^pl5-c1-2]].

## Hàm ý ALM / quy định
**Nghĩa vụ tại VN (TT83).**
- Đo ΔNII và ΔEVE theo PL5 [[src-tt83-2025-nhnn#^d53-1a2]].
- Đặt hạn mức cho cả hai [[src-tt83-2025-nhnn#^d53-2]].
- Đo, theo dõi và báo cáo nội bộ tối thiểu hằng quý [[src-tt83-2025-nhnn#^d54-1a]] [[src-tt83-2025-nhnn#^d55-1]].
- Kiểm tra sức chịu đựng qua ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d54-3b]].
- Bộ phận đo lường IRRBB độc lập với bộ phận kinh doanh [[src-tt83-2025-nhnn#^d54-1b]].
- ALM đề xuất nguyên tắc FTP và khung giá [[src-tt83-2025-nhnn#^d25-3]].
- Nhận dạng cả rủi ro phát sinh từ hoạt động phòng ngừa [[src-tt83-2025-nhnn#^d54-2]].

**Tham chiếu Basel, không phải nghĩa vụ tại VN:** risk tolerance riêng cho gap, basis, option risk [[src-bcbs-irrbb-2016#^irrbb-p03-5]]; phê duyệt trước sáng kiến hedging lớn [[src-bcbs-irrbb-2016#^irrbb-p03-6]]; phép thử ngoại lai dựa trên thu nhập [[src-bcbs-irrbb-2016#^irrbb-p12-2]].

*Diễn giải:*
- Vì TT83 yêu cầu hạn mức ΔNII mà không cho ngưỡng (theo wiki hiện có), ALCO cần tự hiệu chỉnh ngưỡng. Ví dụ ±5–10% EAR của Choudhry và SOT 5% Tier 1 của EU là hai mốc tham khảo, khác mẫu số.
- Biên thương mại phải nằm trong ΔNII, nên phần tách margin chỉ dùng cho phân bổ trách nhiệm nội bộ qua FTP, không dùng để làm nhỏ con số ΔNII báo cáo.

## Bất định
- **Thị trường phái sinh lãi suất VND:** wiki chưa có nguồn về độ sâu thị trường IRS/cap/floor VND [cần nguồn]. *Diễn giải:* nếu thị trường mỏng, các công cụ 4–5 ở Q7 khó áp dụng, ngân hàng phụ thuộc nhiều hơn vào FTP, định giá và natural hedge [[src-choudhry-principles-banking#^choudhry-cs-17]].
- **Ngưỡng ngoại lai, can thiệp giám sát của NHNN với ΔNII:** chưa có claim TT83 [cần nguồn].
- **Tần suất stress test IRRBB theo TT83:** Đ23 chỉ yêu cầu quy định nội bộ nêu tần suất [[src-tt83-2025-nhnn#^d23-2]]; wiki chưa có claim nào cho một tần suất tối thiểu riêng cho IRRBB.
- **Thiếu cạnh:**
  - [[funds-transfer-pricing]], [[loan-pricing]], [[alco]] và [[net-interest-margin]] không có relation nào. Cơ chế "FTP chuyển IRRBB về ALM" chưa có enum relation phù hợp, nên chỉ trình bày trong thân bài.
  - Bốn cạnh ở Q7/Q8 đã được duyệt và áp dụng [2026-10-20] ([[interest-rate-swap]], [[interest-rate-cap-floor]], [[hqla]], [[net-interest-income-sensitivity]]).
- **Công thức tách lãi suất** ở Q5 là diễn giải, chưa có nguồn.
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22.
- [2026-10-20] ingest src-tt50-2026-nhnn PL2: [[available-stable-funding]], [[required-stable-funding]], [[nsfr]] có hệ số ASF/RSF của VN (khác Basel: tiền gửi bán lẻ ≥ 1 năm được rút trước hạn chỉ 95%/90%; phải đòi Chính phủ/KBNN RSF 50–65%; add-on nợ phái sinh 10%); cần rà lại các ví dụ tính NSFR và bảng hệ số.
- [2026-10-20] ingest src-tt50-2026-nhnn PL1: [[lcr]], [[hqla]], [[cash-outflows]], [[retail-deposit-stability]], [[level-1-assets]], [[level-2-assets]] có hệ số VN (HQLA cấp 1/2A/2B 100/85/75–50%, run-off bán lẻ 5%/10%, tiền gửi ngoại tệ luôn kém ổn định, DNNVV ≤ 30 tỷ đồng, cổ phiếu VN30 vào cấp 2B); cần rà lại ví dụ tính LCR và bảng hệ số.
