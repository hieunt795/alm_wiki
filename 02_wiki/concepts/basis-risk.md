---
title: "Basis Risk (Rủi ro cơ sở)"
aliases: [Basis Risk, Rủi ro chênh lệch chỉ số lãi suất, Index Mismatch Risk]
type: concept
domains: [alm, product, basel, vn-reg]
status: active
maturity: draft
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tt83-2025-nhnn]]", "[[src-lubinska-alm-optimisation]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
tags: [irrbb, basis-risk, benchmark, index-mismatch, ftp, spreads]
updated: 2026-10-20
reviewed:
---

## Định nghĩa
Rủi ro cơ sở (Basis risk) miêu tả tác động bất lợi của sự thay đổi tương đối giữa các mức lãi suất của các công cụ tài chính có kỳ hạn tương đương nhưng được định giá hoặc tham chiếu theo các chỉ số lãi suất cơ sở (bases / benchmark indices) khác nhau [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

Rủi ro cơ sở phát sinh do sự tương quan không hoàn hảo (imperfect correlation) trong quá trình điều chỉnh lãi suất giữa các thị trường hoặc các công cụ tài chính khác nhau, ngay cả khi kỳ hạn tái định giá (repricing tenor) hoàn toàn trùng khớp [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

## Các nguồn phát sinh Basis Risk chủ yếu

Theo tiêu chuẩn Basel d368 (Annex 1), Basis risk thể hiện rõ qua các biểu hiện thực tế trong bảng cân đối ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u06-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]]:

### 1. Phân kỳ giữa Lãi suất Tham chiếu và Chi phí Tài trợ Thực tế
- Một ví dụ kinh điển là ngân hàng tài trợ một tài sản sinh lời thả nổi neo theo lãi suất tham chiếu liên ngân hàng (như SOFR, Euribor, VNIBOR) bằng nguồn vốn bán buôn hoặc tiền gửi có chi phí vốn neo theo lãi suất tín phiếu Kho bạc hoặc chi phí huy động thực tế của chính ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- Khi căng thẳng thanh khoản xảy ra, biên chênh lệch tín dụng và thanh khoản của ngân hàng tăng vọt khiến chi phí tài trợ thực tế tăng nhanh hơn nhiều so với lãi suất tham chiếu tài sản, làm xói mòn biên thu nhập thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]].

### 2. Lệch pha giữa các Kỳ hạn Tham chiếu khác nhau (Tenor Basis Risk)
- Phát sinh khi ngân hàng nắm giữ tài sản tham chiếu lãi suất 3 tháng (ví dụ 3-month SOFR) nhưng tài trợ bằng nợ tham chiếu lãi suất 1 tháng (1-month SOFR) hoặc ngược lại.
- Dù cùng thuộc một hệ thống lãi suất tham chiếu, spread giữa kỳ hạn 3 tháng và 1 tháng (3M/1M basis spread) có thể biến động mạnh trong chu kỳ chính sách tiền tệ.

### 3. Lệch pha giữa Lãi suất Thị trường và Lãi suất Quản lý Điều hành (Administered Rates)
- Tài sản cho vay của ngân hàng neo theo lãi suất thị trường tự do, trong khi nguồn vốn huy động tiền gửi bán lẻ được định giá theo mức lãi suất do ngân hàng ấn định (administered rate) hoặc bị khống chế bởi trần lãi suất tiền gửi của NHTW [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- Tốc độ và mức độ truyền dẫn lãi suất (deposit beta) giữa hai nhóm công cụ này thường không đối xứng và không tuyến tính.

### 4. Rủi ro cơ sở đa tiền tệ (Cross-Currency Basis Risk)
- Khi ngân hàng sử dụng nguồn vốn bằng một đồng tiền (ví dụ USD) để hoán đổi (FX swap) tài trợ cho tài sản bằng một đồng tiền khác (ví dụ EUR hoặc VND), ngân hàng chịu rủi ro biến động của phần bù hoán đổi tiền tệ (cross-currency basis swap spread) [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

### 5. Các dạng basis risk theo Choudhry (T4)
- Khoản vay Mỹ theo prime rate (administered, không đổi hằng ngày) được tài trợ bằng nguồn theo Libor: hai lãi suất tương quan dương nhưng không thay đổi cùng mức nên spread biến động [[src-choudhry-principles-banking#^choudhry-irr-5]]. Gap analysis giả định dịch chuyển song song, nên bỏ sót basis risk giữa tài sản ngắn và dài hạn [[src-choudhry-principles-banking#^choudhry-irr-7]].
- Cho vay cố định tài trợ bằng tiền gửi bám nhưng không gắn chính thức với lãi suất cơ bản NHTW; phòng ngừa bằng [[overnight-index-swap]] [[src-choudhry-principles-banking#^choudhry-hedge-18]]. "Secondary IRR": tài sản tái định giá chậm hơn nợ [[src-choudhry-principles-banking#^choudhry-hedge-20]].
- Basis risk của futures (chênh lệch giá tiền mặt và futures) [[src-choudhry-principles-banking#^choudhry-hedge-27]] và khi roll strip hedge [[src-choudhry-principles-banking#^choudhry-hedge-7]]; giao dịch đối ứng chính xác giảm basis risk [[src-choudhry-principles-banking#^choudhry-hedge-3]].
- Basis risk trong [[securitisation]]: IBOR 3 tháng so với Bank Base Rate [[src-choudhry-principles-banking#^choudhry-sec-4]].

## Quản trị và Đo lường Basis Risk

Theo Nguyên tắc 4 và Nguyên tắc 5 của [[bcbs-irrbb]]:
- **Xây dựng kịch bản căng thẳng riêng cho Basis Risk**: Các kịch bản sốc lãi suất thông thường (chỉ dịch chuyển song song các đường cong) hoàn toàn bất lực trong việc nhận diện Basis risk [[src-bcbs-irrbb-2016#^irrbb-u06-7]]. Ngân hàng bắt buộc phải thiết lập các kịch bản căng thẳng giả định sự nới rộng hoặc đảo chiều của các mức chênh lệch chỉ số (basis spreads) để đánh giá tác động lên [[economic-value-of-equity|$\Delta\text{EVE}$]] và [[net-interest-income-sensitivity|$\Delta\text{NII}$]] [[src-bcbs-irrbb-2016#^irrbb-p04-1]] [[src-bcbs-irrbb-2016#^irrbb-u06-7]].
- **Công cụ phòng ngừa (Hedging Instruments)**: Sử dụng các hợp đồng hoán đổi rủi ro cơ sở (basis swaps), ví dụ hoán đổi lãi suất 1M/3M, hoặc hoán đổi giữa lãi suất cho vay cơ sở và chỉ số chi phí tài trợ.
- **Cơ chế FTP đa đường cong (Multi-curve FTP Framework)**: Hệ thống định giá điều chuyển vốn nội bộ phải bóc tách riêng phần bù rủi ro cơ sở (basis charge) gán cho các đơn vị kinh doanh tạo ra sự lệch pha chỉ số lãi suất.

- **Cách đo (Lubinska, T4)**: theo dõi benchmark của tài sản và nợ theo từng dải, sốc 1 bp để xem tác động P&L; một số ngân hàng mặc định khớp yếu tố rủi ro hai phía [[src-lubinska-alm-optimisation#^lubinska-u02-31]]. Xem [[pv01]].
- **Báo cáo ALCO (Choudhry)**: mẫu trang "Basis Risk" trong MI pack của [[alco|ALCO]] (Figure 9.18) phân loại tài sản và nợ theo cơ sở lãi suất (fixed theo kỳ, administered, Bank Base Rate, non-interest) kèm cột Mis-Match [[src-choudhry-principles-banking#^choudhry-alco-19]]; FSA yêu cầu MI pack có phân tích basis risk [[src-choudhry-principles-banking#^choudhry-alco-9]].

## Mối liên hệ với Thanh khoản LCR và NSFR
- Trong quản lý đệm thanh khoản [[lcr]], nếu ngân hàng nắm giữ tài sản [[hqla]] bằng ngoại tệ được tài trợ bởi dòng tiền vào bằng nội tệ thông qua các giao dịch FX swap ngắn hạn, biến động của cross-currency basis spread có thể đột ngột làm tăng chi phí đóng thế vị thế hoặc dẫn tới thiếu hụt thanh khoản cục bộ.
- Trong [[nsfr]], việc phân bổ nguồn vốn bán buôn theo các chỉ số lãi suất không ổn định có thể làm sai lệch dự báo chi phí tài trợ dài hạn (ASF).
- Xem chi tiết tại [[gap-risk]], [[option-risk]], [[csrbb]].

## Basel vs VN
| Khía cạnh | Basel d368 | VN TT83/2025 | Nguồn |
|---|---|---|---|
| Định nghĩa | Tác động của thay đổi tương đối giữa lãi suất các công cụ có kỳ hạn tương tự nhưng định giá theo chỉ số khác nhau | Rủi ro cơ sở phát sinh từ sự khác nhau giữa lãi suất dùng để định giá lại tài sản và nợ phải trả có cùng kỳ hạn | [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-tt83-2025-nhnn#^d3-22]] |

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
