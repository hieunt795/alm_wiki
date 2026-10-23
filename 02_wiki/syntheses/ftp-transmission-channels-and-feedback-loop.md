---
title: "Cơ chế truyền dẫn FTP: kênh thanh khoản, kênh lãi suất, vòng phản hồi và căn cứ quy định"
aliases: [Truyền dẫn FTP theo kênh, vòng phản hồi và quy định, Kênh truyền dẫn FTP và vòng phản hồi, FTP transmission channels and feedback loop]
type: synthesis
domains: [alm, product, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "(Q2) Kênh thanh khoản: FTP phản ánh trạng thái LCR/NSFR so với target vào liquidity spread theo kỳ hạn thế nào, và mức điều chỉnh được xác định ra sao? · (Q3) Kênh lãi suất (IRRBB): FTP chuyển rủi ro tái định giá và basis risk từ đơn vị kinh doanh về ALM/Treasury thế nào, và phần nào ở lại đơn vị kinh doanh? · (Q5) Vòng phản hồi: sau khi đơn vị kinh doanh đổi hành vi, bảng cân đối và các chỉ tiêu thay đổi thế nào, và khi nào cần hiệu chỉnh lại? · (Q6) Điều kiện vận hành và rủi ro của cơ chế: những điều kiện nào để truyền dẫn hiệu quả, và FTP sai gây hậu quả gì? · (Q7) Căn cứ quy định: TT83/2025 yêu cầu gì về FTP, ALCO và RAROC; Basel tham chiếu gì?"
as_of: 2026-10-22
sources: ["[[src-ftp-transmission-analysis]]", "[[src-tata-bank-alm]]", "[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-bcbs-liquidity-principles-2008]]", "[[src-tt83-2025-nhnn]]"]
relations: []
# relations — synthesis: luôn để trống; synthesis không làm chủ thể hay đích của relation. Quan hệ khai ở node tri thức (chủ thể A); thân bài trình bày chuỗi quan hệ trong `## Cơ chế`. Xem 03_meta/taxonomy.md, mục "Relation"
tags: [ftp, transmission, liquidity-spread, irrbb, feedback-loop, steering]
updated: 2026-10-22
reviewed:
---

## Câu hỏi

- Q2. Kênh thanh khoản: FTP phản ánh trạng thái LCR/NSFR so với target vào liquidity spread theo kỳ hạn thế nào, và mức điều chỉnh được xác định ra sao?
- Q3. Kênh lãi suất (IRRBB): FTP chuyển rủi ro tái định giá và basis risk từ đơn vị kinh doanh về ALM/Treasury thế nào, và phần nào ở lại đơn vị kinh doanh?
- Q5. Vòng phản hồi: sau khi đơn vị kinh doanh đổi hành vi, bảng cân đối và các chỉ tiêu thay đổi thế nào, và khi nào cần hiệu chỉnh lại?
- Q6. Điều kiện vận hành và rủi ro của cơ chế: những điều kiện nào để truyền dẫn hiệu quả, và FTP sai gây hậu quả gì?
- Q7. Căn cứ quy định: TT83/2025 yêu cầu gì về FTP, ALCO và RAROC; Basel tham chiếu gì?

Số Q giữ theo bộ khung 7 câu. Q1 (FTP truyền tín hiệu của ALCO thế nào) và Q4 (kênh tín dụng và vốn) không nằm trong cụm này: Q1 trùng [[ftp-purpose-and-balance-sheet-problems]], Q4 trùng [[ftp-balance-sheet-risk-and-cost-components]]. Node nền: [[ftp-transmission-mechanism]], [[internal-risk-transfer]], [[liquidity-transfer-pricing]], [[funds-transfer-pricing]] (đều `draft`). Mốc as_of 2026-10-22.

## Kết luận

Cơ chế truyền dẫn FTP trong wiki dựa gần như hoàn toàn vào một nguồn T5 (`src-ftp-transmission-analysis`, `doc_status: draft`, không rõ tác giả). Nguồn T4 (Tata, Choudhry, Lubinska, Bardaeva) đỡ phần chuyển giao rủi ro lãi suất và rủi ro quản trị, nhưng không đỡ công thức điều chỉnh spread, vòng phản hồi hay độ trễ truyền dẫn. Tất cả kết luận dưới đây về phần T5 là mô tả của nguồn đó, chưa phải kết quả đã đối chiếu.

**Q2 — kênh thanh khoản.** ALM theo dõi LCR, NSFR, Survival Horizon và Structural Ratio; chỉ số tiến gần hoặc vi phạm ngưỡng cảnh báo thì kích hoạt điều chỉnh [[src-ftp-transmission-analysis#^ftp-trans-17]]. LCR thấp thì tăng spread tenor ngắn (O/N đến 30 ngày); NSFR thấp thì tăng spread tenor dài (6M đến 2Y trở lên) [[src-ftp-transmission-analysis#^ftp-trans-8]]. Mức tăng tỷ lệ với khoảng cách tới target qua hệ số α và β do ALCO quyết định [[src-ftp-transmission-analysis#^ftp-trans-15]]. Chỉ nguồn T5 đưa công thức và mức bps.

**Q3 — kênh lãi suất.** Asset Center nhận vốn theo FTP rate cùng kỳ hạn, Liability Center bán vốn theo FTP rate cùng kỳ hạn; Business Unit (BU) chỉ thấy margin cố định, ALM kế thừa toàn bộ mismatch [[src-ftp-transmission-analysis#^ftp-trans-19]] [[src-ftp-transmission-analysis#^ftp-trans-10]]. Lubinska cùng kết luận: rủi ro lãi suất và funding được tách khỏi BU và chuyển về ALM [[src-lubinska-alm-optimisation#^lubinska-u01-7]]. Rủi ro tín dụng không chuyển về ALM, và một số rủi ro không phòng ngừa ra thị trường được [[src-lubinska-alm-optimisation#^lubinska-u01-8]].

**Q5 — vòng phản hồi.** Nguồn T5 mô tả chu trình: tín hiệu Basel III, hiệu chỉnh FTP, BU đổi hành vi, bảng cân đối thay đổi, chỉ số cải thiện, giám sát lại [[src-ftp-transmission-analysis#^ftp-trans-13]]. Chu kỳ diễn ra liên tục, thường hằng tháng hoặc hằng quý [[src-ftp-transmission-analysis#^ftp-trans-28]]. Bardaeva xác nhận phần steering: muốn khuyến khích huy động và hạn chế cho vay thì định giá lại FTP curve hoặc áp steering margin [[src-bardaeva-alm#^ch15-8]]. Phần "trạng thái cân bằng" chỉ có ở T5.

**Q6 — điều kiện và rủi ro.** FTP đặt sai làm hỏng cả hai chiều: UBS báo lãi ảo ở mảng structured credit vì giá chuyển vốn thấp giả tạo [[src-choudhry-principles-banking#^choudhry-gov-12]]. Quyết định gán kỳ hạn không được do đơn vị thực hiện giao dịch đưa ra [[src-bardaeva-alm#^ch11-11]]. Tata nhận định chức năng steering "highly political" [[src-tata-bank-alm#^tata-ftp-17]]. Wiki không có nguồn nào đo độ trễ truyền dẫn từ FTP đến bảng cân đối.

**Q7 — căn cứ quy định.** TT83/2025, hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]], yêu cầu ngân hàng xác định chi phí và rủi ro thanh khoản trong định giá vốn nội bộ [[src-tt83-2025-nhnn#^d45-1b]], và giao ALM đề xuất nguyên tắc xây dựng giá điều chuyển vốn nội bộ [[src-tt83-2025-nhnn#^d25-3]]. RAROC là chỉ tiêu thu nhập trong khẩu vị rủi ro [[src-tt83-2025-nhnn#^d19-2]]. Wiki không có quy định NHNN nào đặt yêu cầu cho công thức điều chỉnh spread hay vòng phản hồi.

## Cơ chế

### Q2 — Kênh thanh khoản

**Cấu phần chịu tác động.** Liquidity Spread là phần bù thanh khoản theo kỳ hạn, phản ánh chi phí huy động vốn biên tế và yêu cầu tuân thủ LCR/NSFR [[src-ftp-transmission-analysis#^ftp-trans-5]]. Nó nằm trong FTP Rate = Base Rate + Liquidity Spread + Credit Spread + Optionality Cost [[src-ftp-transmission-analysis#^ftp-trans-3]]. Choudhry nêu cùng hướng: BU tạo tài sản gây áp lực thanh khoản do chuyển đổi kỳ hạn thì chi phí tìm thanh khoản phải do BU chi trả qua phí FTP [[src-choudhry-principles-banking#^choudhry-ftp-15]].

**Chu trình 4 bước (T5).**
1. Nhận tín hiệu: theo dõi LCR, NSFR, Survival Horizon, Structural Ratio [[src-ftp-transmission-analysis#^ftp-trans-17]].
2. Điều chỉnh curve: LCR thấp tăng spread tenor ngắn, NSFR thấp tăng spread tenor dài [[src-ftp-transmission-analysis#^ftp-trans-8]].
3. BU đổi hành vi: Liability Center tăng huy động ở kỳ hạn được khuyến khích; Asset Center giảm cho vay ở kỳ hạn có chi phí vốn cao vì margin thu hẹp [[src-ftp-transmission-analysis#^ftp-trans-18]].
4. Chỉ số cải thiện: cấu trúc tài sản-nợ thay đổi theo hướng cải thiện LCR và NSFR [[src-ftp-transmission-analysis#^ftp-trans-18]].

**Công thức và ví dụ (chỉ T5).**

| Nội dung | Giá trị | Nguồn |
|---|---|---|
| Tenor ngắn | ΔSpread_short = α × (LCR_target − LCR_actual) | [[src-ftp-transmission-analysis#^ftp-trans-15]] |
| Tenor dài | ΔSpread_long = β × (NSFR_target − NSFR_actual) | [[src-ftp-transmission-analysis#^ftp-trans-15]] |
| α, β | Hệ số nhạy cảm do ALCO quyết định | [[src-ftp-transmission-analysis#^ftp-trans-15]] |
| Ví dụ: LCR 105% (target 115%), NSFR 102% (target 108%) | Tenor 1W-1M tăng 30-50 bps; tenor 6M-2Y tăng 50-80 bps; sau 3-6 tháng LCR 118%, NSFR 108% | [[src-ftp-transmission-analysis#^ftp-trans-16]] |

Nguồn T5 nêu target 110% (LCR) và 105% (NSFR) làm ví dụ trong công thức [[src-ftp-transmission-analysis#^ftp-trans-15]], và target 115% và 108% trong ví dụ minh hoạ [[src-ftp-transmission-analysis#^ftp-trans-16]]. Hai bộ số không trùng nhau. Chúng chỉ là số minh hoạ của nguồn, không phải ngưỡng giám sát. Ngưỡng bắt buộc tại VN nằm ở TT50/2026 (xem [[tt50-2026]]).

**Tata và Choudhry không đưa công thức.** Tata nêu hướng cộng liquidity premium vào FTP nhưng không có công thức; wiki ghi điều này ở [[ftp-balance-sheet-risk-and-cost-components]] mục Bất định. Do đó không có đối chiếu độc lập cho α, β và mức bps.

### Q3 — Kênh lãi suất (IRRBB)

**Chuyển giao.** Asset Center cho vay cố định 5 năm nhận vốn từ ALM theo FTP rate cố định 5 năm; Liability Center huy động 3 tháng bán vốn cho ALM theo FTP rate 3 tháng [[src-ftp-transmission-analysis#^ftp-trans-19]]. BU chỉ thấy fixed margin (customer rate trừ FTP rate), nên không còn exposure với repricing risk [[src-ftp-transmission-analysis#^ftp-trans-10]]. Tata dùng cùng logic: mỗi vị thế được gán FTP rate từ điểm cùng kỳ hạn trên curve [[src-tata-bank-alm#^tata-ftp-8]]. Ví dụ của Tata: tiền gửi 1 năm 1% so với FTP 1 năm 2%, đóng góp margin 1%; khoản vay 2 năm 4% so với FTP 2 năm 3%, đóng góp 1%; chênh lệch giữa điểm 1 năm và 2 năm trên curve là structural contribution [[src-tata-bank-alm#^tata-ftp-9]].

**Phần ở lại BU và phần không chuyển.**

| Rủi ro | Chuyển về ALM? | Nguồn |
|---|---|---|
| Rủi ro lãi suất | Có | [[src-lubinska-alm-optimisation#^lubinska-u01-7]] |
| Rủi ro funding | Có | [[src-lubinska-alm-optimisation#^lubinska-u01-7]] |
| Chi phí thanh khoản | BU chịu qua phí FTP | [[src-choudhry-principles-banking#^choudhry-ftp-15]] |
| Rủi ro tín dụng | Không: theo định nghĩa không chuyển về ALM | [[src-lubinska-alm-optimisation#^lubinska-u01-8]] |
| Rủi ro không phòng ngừa ra thị trường được | Không hết, do FTP thiết lập sai hoặc thị trường phái sinh kém thanh khoản | [[src-lubinska-alm-optimisation#^lubinska-u01-8]] |

**Steering.** Khi ΔNII hoặc ΔEVE tiến gần hoặc vi phạm limit, ALM có thể điều chỉnh FTP curve: tăng spread cho tenor có gap lớn, giảm spread hoặc thêm reward cho matched funding [[src-ftp-transmission-analysis#^ftp-trans-20]]. Hệ số điều chỉnh do ALCO calibrate [[src-ftp-transmission-analysis#^ftp-trans-29]]. Công thức γ, δ nằm ở một dòng liền trong raw (§6.2) và chưa có claim riêng. [cần nguồn]

**Basis risk.** Basis risk phát sinh khi assets và liabilities repriced theo benchmark khác nhau, ví dụ VNIBOR 1M so với VNIBOR 3M, hoặc VNIBOR so với lãi suất điều hành SBV. FTP curve riêng cho từng benchmark giúp theo dõi, và chi phí hedge có thể đưa vào FTP để chuyển cho BU [[src-ftp-transmission-analysis#^ftp-trans-21]]. Tata tách FTP thành hai cấu phần để định giá sản phẩm có kỳ hạn chỉ số tái định giá khác kỳ hạn hợp đồng: ví dụ khoản vay 2 năm FTP = 1,6% rủi ro lãi suất + 80 bp liquidity premium = 2,4% [[src-tata-bank-alm#^tata-ftp-14]].

### Q5 — Vòng phản hồi

**Chu trình.** Basel III Signals (LCR, NSFR, ΔNII, ΔEVE, CAR) → FTP Engine Calibration → Business Unit Behavior Change → Balance Sheet Reshape → Risk Metrics Improve → Re-monitor → Re-calibration [[src-ftp-transmission-analysis#^ftp-trans-13]]. Chu kỳ thường là hằng tháng hoặc hằng quý, tuỳ biến động của thị trường và bảng cân đối [[src-ftp-transmission-analysis#^ftp-trans-28]].

**Trạng thái cân bằng (T5).**
- LCR/NSFR đạt target thì ALM giảm liquidity spread về mức bình thường [[src-ftp-transmission-analysis#^ftp-trans-27]].
- Gap trong limit và ΔNII/ΔEVE ổn định thì FTP curve không cần điều chỉnh [[src-ftp-transmission-analysis#^ftp-trans-27]].
- CAR có đủ buffer thì credit spread phản ánh rủi ro từng rating bucket [[src-ftp-transmission-analysis#^ftp-trans-27]].

**Tương tác chéo.** Tăng liquidity spread dài hạn để cải thiện NSFR làm Asset Center giảm cho vay dài hạn, duration tài sản ngắn lại, ΔEVE giảm. Tăng capital charge để cải thiện CAR đẩy BU sang tài sản RWA thấp, liquidity buffer tăng, LCR cải thiện [[src-ftp-transmission-analysis#^ftp-trans-26]].

**Steering ngoài T5.** Bardaeva nêu cùng hướng: định giá lại FTP curve hoặc áp steering margin để khuyến khích huy động và hạn chế cho vay, và điều chỉnh độ dốc curve để quản lý tác động bất lợi của chuyển đổi kỳ hạn lên NII [[src-bardaeva-alm#^ch15-8]].

### Q6 — Điều kiện vận hành và rủi ro

**Điều kiện về quản trị.**
- ALM xác định nguyên tắc định giá điều chuyển và dựng curve; nguyên tắc gán kỳ hạn cho một loại giao dịch không do đơn vị thực hiện giao dịch quyết định [[src-bardaeva-alm#^ch11-11]].
- Nguồn T5 khuyến nghị thiết lập FTP governance framework với vai trò ALCO phê duyệt FTP curve và steering adjustments, và định kỳ back-test để calibrate hệ số [[src-ftp-transmission-analysis#^ftp-trans-29]].
- Tata nhận định chức năng steering mang tính chính trị cao, vì FTP là nguồn sự thật duy nhất về giá trị gia tăng của từng khối và thay đổi nhỏ có thể đổi bức tranh khối nào đóng góp NII [[src-tata-bank-alm#^tata-ftp-17]].

**Điều kiện về dữ liệu.** Cost approach phụ thuộc lãi suất quá khứ nên phản ứng trễ với thay đổi thị trường, và curve có thể méo vì các kỳ hạn được huy động ở thời điểm khác nhau [[src-choudhry-principles-banking#^choudhry-ifc-17]]. Đây là độ trễ ở khâu dựng curve, không phải độ trễ từ FTP đến hành vi BU.

**Hậu quả khi FTP sai.** UBS: lãnh đạo không phát hiện lỗi trong cơ chế funding nội bộ cho phép mảng structured credit báo lãi ảo; gói cứu trợ 59 tỷ USD cuối 2008; mô hình funding thực tế hơn bị xem là "constraint on the growth strategy" [[src-choudhry-principles-banking#^choudhry-gov-12]]. Lubinska nêu FTP thiết lập sai khiến một phần rủi ro không chuyển ra thị trường được [[src-lubinska-alm-optimisation#^lubinska-u01-8]].

**Chưa có nguồn.** Độ trễ giữa thay đổi spread và thay đổi hành vi BU; quy mô đo được của hiệu ứng điều chỉnh; điều kiện để "cân bằng" của T5 xảy ra trong thực tế. [cần nguồn]

### Q7 — Căn cứ quy định

| Yêu cầu | Nội dung | Nguồn |
|---|---|---|
| Định giá vốn nội bộ | Ngân hàng phải xác định chi phí đáp ứng nhu cầu thanh khoản và rủi ro thanh khoản trong định giá vốn nội bộ, và đánh giá kết quả kinh doanh của hoạt động trọng yếu (nội bảng và ngoại bảng) | [[src-tt83-2025-nhnn#^d45-1b]] |
| Vai trò ALM | ALM rà soát, đề xuất kế hoạch huy động vốn, sử dụng vốn và nguyên tắc xây dựng giá điều chuyển vốn nội bộ; xây dựng khung lãi suất và khung giá sản phẩm; kiểm soát kinh doanh tuân thủ hạn mức rủi ro thanh khoản và IRRBB | [[src-tt83-2025-nhnn#^d25-3]] |
| Hội đồng ALCO | Đề xuất, tham mưu Tổng giám đốc về nội dung quản lý tài sản/nợ phải trả tại Đ25.3; họp định kỳ tối thiểu mỗi quý một lần | [[src-tt83-2025-nhnn#^d6-4b]] |
| Khẩu vị rủi ro | Gồm tỷ lệ an toàn vốn mục tiêu, chỉ tiêu thu nhập ROE và RAROC, chỉ tiêu định tính khác | [[src-tt83-2025-nhnn#^d19-2]] |
| Hiệu lực TT83 | Từ 01/07/2026 | [[src-tt83-2025-nhnn#^d74-1]] |

**Tham chiếu Basel (không phải nghĩa vụ tại VN).** BCBS 144 P4 nêu ngân hàng nên đưa chi phí, lợi ích và rủi ro thanh khoản vào định giá nội bộ, đo lường hiệu quả và phê duyệt sản phẩm mới cho mọi hoạt động trọng yếu, nhằm làm động lực rủi ro của từng business line phù hợp với phơi nhiễm thanh khoản của ngân hàng [[src-bcbs-liquidity-principles-2008#^lrm-p04]]. Liquidity charge gán theo vị thế, danh mục hoặc giao dịch [[src-bcbs-liquidity-principles-2008#^lrm-19]].

## Bằng chứng ủng hộ

- **Chuyển giao rủi ro lãi suất về ALM** có ba nguồn độc lập: T5 [[src-ftp-transmission-analysis#^ftp-trans-10]], Lubinska [[src-lubinska-alm-optimisation#^lubinska-u01-7]] và Tata [[src-tata-bank-alm#^tata-ftp-8]].
- **Rủi ro quản trị của FTP** có ba nguồn T4 độc lập: Choudhry (UBS) [[src-choudhry-principles-banking#^choudhry-gov-12]], Bardaeva [[src-bardaeva-alm#^ch11-11]] và Tata [[src-tata-bank-alm#^tata-ftp-17]].
- **Định giá thanh khoản vào FTP để định hướng hành vi BU** có hai chiều ủng hộ: Choudhry [[src-choudhry-principles-banking#^choudhry-ftp-15]] và BCBS 144 [[src-bcbs-liquidity-principles-2008#^lrm-p04]].

## Bằng chứng trái chiều

- **"Cô lập hoàn toàn" so với "không hết".** T5 nêu FTP tách toàn bộ IRRBB khỏi BU và chuyển về ALM [[src-ftp-transmission-analysis#^ftp-trans-9]]. Lubinska nêu có rủi ro không chuyển ra thị trường được khi FTP sai hoặc thị trường phái sinh kém thanh khoản [[src-lubinska-alm-optimisation#^lubinska-u01-8]]. Hai nguồn khác phạm vi: T5 mô tả thiết kế, Lubinska mô tả giới hạn thực tế. Không phải conflict, nhưng đọc T5 một mình sẽ đánh giá quá cao mức cô lập.
- **Cơ chế "tự cân bằng" so với tính chính trị của FTP.** T5 mô tả chu trình khép kín về trạng thái cân bằng [[src-ftp-transmission-analysis#^ftp-trans-27]]. Tata nhận định steering mang tính chính trị cao vì FTP quyết định bức tranh đóng góp của từng khối [[src-tata-bank-alm#^tata-ftp-17]]. Mô hình T5 không nêu xung đột lợi ích giữa các BU.
- **Mức độ chi tiết công thức.** T5 đưa công thức ΔSpread có hệ số; Tata và Choudhry nêu hướng nhưng không đưa công thức. Chưa có nguồn nào để quyết định công thức nào "đúng".

## Phụ thuộc regime

- **Môi trường thanh khoản.** Công thức ΔSpread theo LCR/NSFR giả định ngân hàng đang dưới target. Khi trên target, T5 chỉ nói ALM giảm spread về mức bình thường [[src-ftp-transmission-analysis#^ftp-trans-27]]; không nêu rule cho hướng ngược lại. [cần nguồn]
- **Độ sâu thị trường phái sinh.** Mức chuyển rủi ro về ALM phụ thuộc thị trường phái sinh đủ thanh khoản ở đồng tiền liên quan [[src-lubinska-alm-optimisation#^lubinska-u01-8]].
- **Phương pháp dựng curve.** Cost approach phù hợp thị trường ổn định, biến động lãi suất thấp, cấu trúc nợ đa dạng kỳ hạn [[src-choudhry-principles-banking#^choudhry-ifc-17]].
- **Jurisdiction.** Nguồn T5 dùng VNIBOR và SBV làm ví dụ benchmark [[src-ftp-transmission-analysis#^ftp-trans-21]]. Không có nguồn T1 nào đặt chuẩn cho các benchmark này trong FTP.

## Hàm ý ALM / quy định

- **Nghĩa vụ tại VN (T1).** TT83/2025 đặt hai yêu cầu mức nguyên tắc: đưa chi phí thanh khoản vào định giá vốn nội bộ [[src-tt83-2025-nhnn#^d45-1b]], và ALM đề xuất nguyên tắc giá điều chuyển [[src-tt83-2025-nhnn#^d25-3]]. TT83 không yêu cầu công thức điều chỉnh spread, chu kỳ hiệu chỉnh hay vòng phản hồi. Theo wiki, các nội dung đó là quyết định thiết kế nội bộ.
- **Tham chiếu Basel (không phải nghĩa vụ tại VN).** BCBS 144 P4 mô tả mục tiêu căn chỉnh động lực của business line theo rủi ro thanh khoản [[src-bcbs-liquidity-principles-2008#^lrm-p04]]; không có yêu cầu định lượng.
- *Diễn giải:* nếu ALCO là cơ quan duyệt FTP curve và steering [[src-ftp-transmission-analysis#^ftp-trans-29]] thì quy chế ALCO theo Đ6.4.b TT83 [[src-tt83-2025-nhnn#^d6-4b]] là nơi tự nhiên để ghi α, β, chu kỳ hiệu chỉnh và nguyên tắc không để đơn vị giao dịch quyết định kỳ hạn gán. Đây là suy luận của LLM, không phải yêu cầu của TT83. (ngoài wiki, chưa có nguồn)
- *Diễn giải:* khi một điều chỉnh FTP tác động sang kênh khác [[src-ftp-transmission-analysis#^ftp-trans-26]], hạn mức NSFR và hạn mức IRRBB cần được đọc cùng nhau khi ALCO duyệt thay đổi spread tenor dài.

## Bất định

- [cần nguồn] Đối chiếu độc lập (T3/T4) cho công thức ΔSpread theo α, β và mức 30-50 / 50-80 bps. Đề xuất `/register` nguồn về FTP steering, ví dụ Cadamagnani et al. (2015), PRA, nằm trong danh mục tham khảo của nguồn T5.
- [cần nguồn] Công thức steering γ, δ cho kênh lãi suất: nằm ở một dòng liền trong raw §6.2 của `src-ftp-transmission-analysis`; cần `/ingest src-ftp-transmission-analysis u01` (bổ sung) nếu muốn có claim riêng.
- [cần nguồn] Độ trễ giữa thay đổi spread và thay đổi hành vi BU; điều kiện để trạng thái "cân bằng" của T5 xảy ra.
- [cần nguồn] Rule điều chỉnh khi LCR/NSFR vượt target.
- Nguồn T5 có `doc_status: draft`, không rõ tác giả, và tự nhận dựa trên Lubinska (2020) kết hợp thực tiễn ngân hàng Việt Nam. Mọi kết luận của phần T5 ở Q2, Q5 cần đọc với mức tin cậy tương ứng.
- Kênh tín dụng và vốn (RAROC, EL, Capital Charge) thuộc Q4, không nằm trong cụm này; xem [[ftp-balance-sheet-risk-and-cost-components]] và mục 4 của [[ftp-transmission-mechanism]].
