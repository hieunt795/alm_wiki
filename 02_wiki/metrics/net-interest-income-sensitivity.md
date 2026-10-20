---
title: "Net Interest Income Sensitivity (ΔNII)"
aliases: [NII Sensitivity, Thu nhập lãi thuần nhạy cảm lãi suất, ΔNII, Delta NII, Earnings at Risk, EaR]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: canonical
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-lubinska-alm-optimisation]]", "[[src-tt83-2025-nhnn]]", "[[src-choudhry-principles-banking]]", "[[src-bardaeva-alm]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: measures, to: "[[basis-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: measures, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[outlier-bank-test]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-2]]"}
  - {type: input-to, to: "[[balance-sheet-optimisation-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u04-12]]"}
tags: [irrbb, nii, earnings-at-risk, alm, interest-income, constant-balance-sheet]
updated: 2026-10-20
reviewed:
---

## Định nghĩa
Độ nhạy thu nhập lãi thuần (Net Interest Income Sensitivity - $\Delta\text{NII}$) đo lường mức độ biến động của thu nhập thuần từ lãi dự kiến trong một khoảng thời gian xác định (thường là 12 tháng liên tục, hoặc 1 đến 3 năm) do tác động của các kịch bản sốc lãi suất so với kịch bản kế hoạch cơ sở của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u01-4]] [[src-bcbs-irrbb-2016#^irrbb-p08-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

Khác với [[economic-value-of-equity|$\Delta\text{EVE}$]] vốn là thước đo định giá kinh tế dài hạn cho mục tiêu an toàn vốn của cơ quan giám sát, $\Delta\text{NII}$ là thước đo trọng tâm trong hoạt động điều hành thương mại hàng ngày của Ban điều hành và Hội đồng [[alco|ALCO]] [[src-bcbs-irrbb-2016#^irrbb-u02-4]]:
- **Tác động trực tiếp lên P&L và cổ tức**: Thu nhập lãi thuần quyết định khả năng sinh lời thực tế, ảnh hưởng đến khả năng chia cổ tức ổn định, chi phí vốn và mức tích lũy lợi nhuận giữ lại để bổ sung vốn tự có trong ngắn hạn [[src-bcbs-irrbb-2016#^irrbb-u06-5]].
- **Góc nhìn hoạt động liên tục (Going-concern)**: Đánh giá khả năng của ngân hàng tạo ra dòng tiền thu nhập đủ lớn để trang trải chi phí hoạt động và duy trì vị thế cạnh tranh mà không bị suy giảm nguồn lực tài chính [[src-bcbs-irrbb-2016#^irrbb-u06-5]].
- **Góc nhìn Kế toán vs ALM theo Fidelio Tata**: Phòng Kế toán tính NII cho quá khứ (*retrospective view*), bao gồm các thay đổi và biến động trong tháng [[src-tata-bank-alm#^tata-nii-12]]; phòng ALM định lượng phơi nhiễm thu nhập lãi thuần theo hướng tương lai (*prospective view*) [[src-tata-bank-alm#^tata-nii-2]]. Khi tính độ nhạy NII, các vị thế không nhạy cảm lãi suất như bất động sản, đầu tư cổ phần, tài sản vô hình và vốn chủ sở hữu của ngân hàng có thể được loại khỏi phân tích [[src-tata-bank-alm#^tata-nii-5]].
- **Cơ chế triệt tiêu sai số mô hình (Error Cancellation)**: Khi tính toán độ nhạy NII ($\Delta\text{NII}$), độ chính xác tuyệt đối của dự báo NII cơ sở ít quan trọng hơn đối với ALM so với dự báo P&L kế toán; bởi vì các giả định sai sẽ được áp dụng lặp lại đồng thời trong cả kịch bản cơ sở và kịch bản sốc, do đó phần lớn sai số sẽ bị triệt tiêu khi lấy hiệu số giữa hai kịch bản [[src-tata-bank-alm#^tata-nii-3]]. Chân trời dự báo NII thường là ngắn đến trung hạn, phổ biến từ 1 đến 3 năm; kéo dài quá xa sẽ tạo cảm giác chính xác giả tạo, vì không thể dự báo vững chắc thay đổi trong hoạt động kinh doanh khách hàng trong dài hạn [[src-tata-bank-alm#^tata-nii-4]].

## Quy chuẩn đo lường và tính toán theo Basel (d368)

Theo Nguyên tắc 8 của [[bcbs-irrbb]], khi tính toán và công bố $\Delta\text{NII}$ theo Bảng B, ngân hàng phải áp dụng các quy chuẩn sau:

### 1. Đường chân trời đánh giá (Horizon)
- Chuẩn mực công bố Trụ cột 3 yêu cầu đánh giá trên giai đoạn **12 tháng liên tục (rolling 12-month period)** [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- Ngoài phần công bố, d368 Annex 1 ghi thước đo thu nhập thường dùng chân trời một đến ba năm, không quá năm năm, để hạn chế tác động cộng dồn của giả định và độ phức tạp tính toán [[src-bcbs-irrbb-2016#^irrbb-u06-8]].
- ΔNII là chênh lệch NII kỳ vọng giữa kịch bản cơ sở và kịch bản stress; kịch bản cơ sở phản ánh kế hoạch kinh doanh hiện tại về khối lượng, giá và ngày tái định giá của giao dịch tương lai [[src-bcbs-irrbb-2016#^irrbb-u06-10]].

- Theo Bardaeva (T4), thước đo thu nhập nội bộ thường dùng horizon ngân sách 3–4 năm [[src-bardaeva-alm#^ch11-16]], khác horizon ΔNII 01 năm của TT83 PL5 [[src-tt83-2025-nhnn#^pl5-b2]]. *Diễn giải:* khác phạm vi (quản trị nội bộ so với đo lường quy định), không phải conflict. Xem [[irrbb-management]].

### 2. Giả định Bảng cân đối kế toán (Balance Sheet Assumption)
d368 Annex 1 và Lubinska phân biệt 3 trạng thái mô hình hoá bảng cân đối trong đo lường thu nhập [[src-bcbs-irrbb-2016#^irrbb-u06-9]] [[src-lubinska-alm-optimisation#^lubinska-u05-8]]:
- **Bảng cân đối không đổi (Constant balance sheet)**: Quy mô và cơ cấu bảng cân đối được duy trì cố định; các tài sản và khoản nợ đáo hạn được thay thế bằng các công cụ mới có cùng đặc điểm tài chính (like-for-like replacement). Đây là **giả định bắt buộc đối với công bố Trụ cột 3** [[src-bcbs-irrbb-2016#^irrbb-p08-3]] và là giả định nền tảng cho mô hình tối ưu hóa [[balance-sheet-optimisation-model]] [[src-lubinska-alm-optimisation#^lubinska-u05-8]].
- **Bảng cân đối động (Dynamic balance sheet)**: Phản ánh kế hoạch tăng trưởng kinh doanh mới, sự thay đổi trong hành vi khách hàng và các phản ứng điều hành chủ động của ngân hàng; d368 gọi đây là cách có ý nghĩa nhất [[src-bcbs-irrbb-2016#^irrbb-u06-9]] [[src-lubinska-alm-optimisation#^lubinska-u05-8]]. Dynamic view hữu ích cho lập kế hoạch kinh doanh và ngân sách, nhưng phụ thuộc biến số rất khó dự báo chính xác trong thời gian dài và có thể che giấu rủi ro nền tảng [[src-bcbs-irrbb-2016#^irrbb-p04-4]].
- **Bảng cân đối thu hẹp (Run-off balance sheet)**: Giả định các vị thế đáo hạn không được tái đầu tư, ngoại trừ phần cần thiết để tài trợ cho tài sản còn lại [[src-bcbs-irrbb-2016#^irrbb-u06-9]] [[src-lubinska-alm-optimisation#^lubinska-u05-8]].

### 3. Dòng tiền và Biên thương mại (Commercial Margins)
$\Delta\text{NII}$ tính toán dựa trên toàn bộ dòng tiền thu lãi và trả lãi thực tế, bao gồm cả biên thương mại (commercial margin) và các thành phần credit spread của tài sản và nợ [[src-bcbs-irrbb-2016#^irrbb-p08-3]].

### 4. Công thức chênh lệch thu nhập thuần

$$
\Delta\text{NII}_i = \text{NII}_i^{\text{shocked}} - \text{NII}_0^{\text{base}}
$$

Trong đó:
- $\text{NII}_0^{\text{base}}$: Thu nhập lãi thuần kỳ vọng 12 tháng tới theo kịch bản kế hoạch cơ sở (sử dụng lãi suất forward hoặc spot hiện hành).
- $\text{NII}_i^{\text{shocked}}$: Thu nhập lãi thuần kỳ vọng 12 tháng tới dưới tác động của kịch bản sốc lãi suất tức thời $i$.
- $\text{NII} = \text{Lãi từ tài sản sinh lời} - \text{Chi phí trả lãi tiền gửi và nợ tài trợ}$.

- **Phương pháp gap (Lubinska, T4)**: ΔNII ≈ GAP × Δi trong gapping period [[src-lubinska-alm-optimisation#^lubinska-u02-23]] [[src-lubinska-alm-optimisation#^lubinska-u02-25]]. Mô phỏng NII phục vụ nhiều mục đích: stress test EBA có giả định cấu trúc sổ; thước đo nội bộ dùng sổ không đổi, khoản đáo hạn thay bằng khoản cùng đặc điểm [[src-lubinska-alm-optimisation#^lubinska-u02-33]]. Xem [[repricing-gap-analysis]].
- **Phương pháp chuẩn hoá EBA (RTS/2022/09, qua Tata)**: NII bằng lãi đã cố định đến ngày tái định giá, cộng lợi suất phi rủi ro sau tái định giá, cộng biên thương mại sau reset, theo bảng cân đối không đổi [[src-tata-bank-alm#^tata-eba-2]]; biên thương mại của nghiệp vụ mới lấy theo biên năm trước [[src-tata-bank-alm#^tata-eba-3]]; cấu phần thay đổi giá trị thị trường cho công cụ ngoài kỳ NII, loại dòng tiền trong kỳ để tránh tính trùng [[src-tata-bank-alm#^tata-eba-4]]. SOT NII là 5% vốn cấp 1 [[src-tata-bank-alm#^tata-sot-3]]. Xem [[outlier-bank-test]].

### 5. Kịch bản sốc áp dụng cho NII và Sàn Lãi suất 0%
Theo Annex 2 của d368, chuẩn mực quy định tối thiểu 2 kịch bản sốc song song (Parallel up và Parallel down) cho công bố $\Delta\text{NII}$, đồng thời khuyến khích các ngân hàng kiểm tra các kịch bản xoay trục (steepener, flattener) để nhận diện rủi ro chênh lệch cấu trúc kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u07-1]].

Theo Beata Lubinska (2020), khi đánh giá kịch bản sốc giảm lãi suất (ví dụ: -200 bps theo quy định của ECB cho đồng EUR), một sàn lãi suất 0% (Floor 0%) được áp dụng để ngăn ngừa lãi suất rơi vào vùng âm [[src-lubinska-alm-optimisation#^lubinska-u05-9]]:
- **Trên danh mục tài sản**: Các hợp đồng tín dụng thương mại thường có điều khoản quyền chọn sàn tự động (embedded floors) bảo vệ lợi suất của ngân hàng khi lãi suất thị trường lao dốc.
- **Trên danh mục nợ**: Ngân hàng thương mại thường chủ động cam kết giữ lãi suất tiền gửi khách hàng bán lẻ không thấp hơn 0% vì lý do cạnh tranh thương mại và bảo vệ thương quyền (franchise preservation) [[src-lubinska-alm-optimisation#^lubinska-u05-9]].

Đặc biệt, nghiên cứu thực nghiệm của Lubinska (2020) chứng minh rằng việc áp đặt giới hạn $\frac{|\Delta\text{NII}_{\pm 200\text{bps}}|}{\text{NII}} \le 4\%$ trong mô hình quy hoạch phi tuyến [[balance-sheet-optimisation-model]] cho phép ngân hàng nén độ nhạy $\Delta\text{NII}_{+200\text{bps}}$ từ mức rủi ro cực cao $80.5\%$ về đúng ngưỡng an toàn $4\%$ mà vẫn đồng thời gia tăng thu nhập lãi thuần thêm EUR 6.9 triệu trong 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u07-8]] [[src-lubinska-alm-optimisation#^lubinska-u07-10]] [[src-lubinska-alm-optimisation#^lubinska-u07-11]]. Tại Ngân hàng 1, dưới kịch bản bị hạ 1 bậc tín nhiệm, mô hình nén $\Delta\text{NII}_{+200\text{bps}}$ từ $72.18\%$ xuống mức an toàn vượt bậc **$6.8\%$** [[src-lubinska-alm-optimisation#^lubinska-u08-4]].

Đối với Ngân hàng 2 (quy mô lớn USD 549 tỷ), việc tối ưu hóa phía tài sản và tinh gọn đệm thanh khoản giúp ngân hàng vừa gia tăng hàng trăm triệu USD thu nhập, vừa kiểm soát độ nhạy lãi suất chặt chẽ qua các kịch bản sốc thị trường:
- Kịch bản Cơ sở (Tài sản): $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $38\%$ xuống **$30.37\%$** song hành cùng thu nhập tăng thêm USD 284.9 triệu / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u08-9]] [[src-lubinska-alm-optimisation#^lubinska-u08-10]].
- Kịch bản Khủng hoảng Dầu mỏ (lãi suất tăng): $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $35\%$ xuống **$27.68\%$** và thu nhập tăng thêm USD 345.2 triệu / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u08-11]] [[src-lubinska-alm-optimisation#^lubinska-u08-12]].
- Kịch bản Động đất (lãi suất giảm): $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $39.5\%$ xuống **$31.5\%$** và thu nhập tăng thêm USD 273.0 triệu / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u08-13]] [[src-lubinska-alm-optimisation#^lubinska-u08-14]].
- Kịch bản Kỳ vọng Lạm phát: $\Delta\text{NII}_{+200\text{bps}}$ nén từ $31.06\%$ xuống **$24.64\%$** song hành với thu nhập tăng thêm USD 382.9 triệu / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u09-1]] [[src-lubinska-alm-optimisation#^lubinska-u09-2]].
- Kịch bản Tối ưu hóa Nguồn vốn (Liabilities Base Scenario): Việc tăng tỷ trọng CASA bán lẻ lên 51.16% và giảm nợ bán buôn ngắn hạn giúp giảm chi phí vốn USD 652.6 triệu / 6 tháng, đồng thời kéo giảm độ nhạy $\Delta\text{NII}_{+200\text{bps}}$ từ $65\%$ xuống **$54\%$** [[src-lubinska-alm-optimisation#^lubinska-u09-14]] [[src-lubinska-alm-optimisation#^lubinska-u09-15]].
- Kịch bản Độ nhạy Nguồn vốn dưới các cú sốc thị trường: $\Delta\text{NII}_{+200\text{bps}}$ được nén mạnh mẽ và kiểm soát an toàn trên tất cả các kịch bản: Lạm phát nén về **$49\%$** [[src-lubinska-alm-optimisation#^lubinska-u10-4]], Khủng hoảng dầu mỏ giảm từ $62\%$ về **$51.7\%$** [[src-lubinska-alm-optimisation#^lubinska-u10-7]], Động đất giảm từ $64\%$ về **$53\%$**, và Hạ 1 bậc tín nhiệm duy trì ở mức **$54.26\%$** [[src-lubinska-alm-optimisation#^lubinska-u10-17]] song hành với mức tiết kiệm chi phí vốn đạt đỉnh USD 745.5 triệu / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u10-16]].
- Kịch bản Biến động Tỷ trọng Tài sản Cố định & Thả nổi (Funding side): Khi tài sản cố định chiếm tỷ trọng quá lớn, cấu trúc nợ sau tối ưu hóa dù cắt giảm chi phí vốn tới USD 866.6 triệu / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u11-2]] vẫn duy trì $\Delta\text{NII}_{+200\text{bps}} = 121\%$ [[src-lubinska-alm-optimisation#^lubinska-u11-3]] do khe hở nhạy cảm lãi suất cố hữu không thể triệt tiêu nếu thiếu hoán đổi lãi suất (IRS); trong khi dưới kịch bản tài sản thả nổi, việc nâng CASA bán lẻ lên 53.23% [[src-lubinska-alm-optimisation#^lubinska-u11-5]] giúp giảm chi phí vốn USD 652.6 triệu [[src-lubinska-alm-optimisation#^lubinska-u11-7]] và kiểm soát $\Delta\text{NII}_{+200\text{bps}}$ ở mức $66\%$ [[src-lubinska-alm-optimisation#^lubinska-u11-8]].

### 6. Cơ chế và ví dụ minh hoạ (Choudhry, T4)
- NII nhạy lãi suất vì tài sản và nợ tái định giá ở thời điểm khác nhau [[src-choudhry-principles-banking#^choudhry-nim-9]]. Lãi suất sản phẩm có ba kiểu phản ứng: giữ nguyên; thay đổi bằng mức thay đổi benchmark; thay đổi nhiều hơn hoặc ít hơn [[src-choudhry-principles-banking#^choudhry-nim-3]]. Ví dụ: khoản vay cố định 10% tài trợ bằng tiền gửi 1 tháng, lãi suất tiền gửi từ 2% lên 4% làm NII giảm từ £800 xuống £600 [[src-choudhry-principles-banking#^choudhry-nim-10]].
- **Ví dụ ChoudWest (Ex 1.5)**: giả định lãi suất 5%, bảng cân đối không đổi 12 tháng, không FTP, đường cong phẳng [[src-choudhry-principles-banking#^choudhry-nim-1]]; NII cơ sở £461,0m [[src-choudhry-principles-banking#^choudhry-nim-2]]; lãi suất +3% làm NII tăng £64,7m (+14%) vì nhiều tài sản tái định giá hơn nợ [[src-choudhry-principles-banking#^choudhry-nim-4]]; lãi suất giảm xuống 4% làm NII giảm £29,5m [[src-choudhry-principles-banking#^choudhry-nim-6]]. *Diễn giải:* giả định của ví dụ khác d368 (không dùng sốc chuẩn hoá).
- **Earnings at Risk (ví dụ 6.12)**: gap tức thời −80, lãi suất +1% song song làm NII giảm 0,8 triệu USD, EAR khoảng 7,8%, [[net-interest-margin|NIM]] giảm 40 bp; NIM = (thu nhập lãi − chi phí lãi) / tài sản sinh lời bình quân [[src-choudhry-principles-banking#^choudhry-hedge-21]]. ALCO thường đặt hạn mức EAR ±5% hoặc ±10% [[src-choudhry-principles-banking#^choudhry-hedge-22]]. Phòng ngừa NII có thể dùng [[overnight-index-swap]] [[src-choudhry-principles-banking#^choudhry-hedge-17]].
- **Dự báo bottom-up**: mô hình cấp tài khoản, sốc lãi suất và tính lại để đo độ nhạy NII; thách thức chính là dữ liệu [[src-choudhry-principles-banking#^choudhry-nim-13]].

### 7. Dự phóng độ nhạy (Tata, T4)
- Kế hoạch ALM phải tính độ nhạy EVE và NII kỳ vọng trong tương lai, cần khối lượng theo phân khúc hành vi và kỳ hạn nghiệp vụ mới [[src-tata-bank-alm#^tata-niip-6]]. Margin-beta: NIM giảm 5 bp mỗi năm sau cú giảm 100 bp; 19 bp mỗi 100 bp lãi suất ngắn hạn [[src-tata-bank-alm#^tata-niip-5]]. Xem [[nii-planning]].


## Xung đột chiến lược giữa EVE và NII (The EVE vs NII Trade-off)

Ủy ban Basel cảnh báo rõ ràng về sự đánh đổi giữa hai thước đo trong điều hành ALM [[src-bcbs-irrbb-2016#^irrbb-u02-4]]:
- **Nếu ngân hàng triệt tiêu rủi ro $\Delta\text{EVE}$**: Ngân hàng thực hiện khớp chính xác kỳ hạn tái định giá giữa tài sản và nợ (ví dụ tài trợ tài sản cố định dài hạn bằng nợ dài hạn cố định, hoặc đưa toàn bộ tài sản về lãi suất thả nổi ngắn hạn khớp với tiền gửi ngắn hạn). Khi đó, giá trị kinh tế của ngân hàng được bảo vệ hoàn hảo trước các cú sốc lãi suất. Tuy nhiên, khi lãi suất thị trường giảm sâu, lợi suất tài sản ngắn hạn giảm ngay lập tức trong khi chi phí vốn (hoặc chi phí vận hành) không thể giảm tương ứng, dẫn tới sự sụt giảm và biến động dữ dội của thu nhập lãi thuần $\Delta\text{NII}$.
- **Nếu ngân hàng triệt tiêu rủi ro $\Delta\text{NII}$**: Để bảo vệ thu nhập lãi ổn định cho nguồn tiền gửi không kỳ hạn (NMDs) hoặc vốn chủ sở hữu, ngân hàng đầu tư nguồn vốn này vào một danh mục trái phiếu cố định dài hạn ([[src-bcbs-irrbb-2016#^irrbb-u06-6]]). Dòng thu nhập từ trái phiếu cố định dài hạn giúp NII hoàn toàn miễn nhiễm với biến động lãi suất ngắn hạn. Tuy nhiên, hành động này kéo dài thời lượng của bảng cân đối, khiến giá trị kinh tế $\Delta\text{EVE}$ chịu rủi ro cực lớn khi lãi suất tăng vọt.
- **Kết luận**: Ngân hàng không thể tối ưu hoá đồng thời cả EVE và NII mà phải chấp nhận một điểm cân bằng chiến lược phù hợp với [[risk-appetite|khẩu vị rủi ro]] và các [[risk-limits|hạn mức]] nội bộ được HĐQT phê duyệt [[src-bcbs-irrbb-2016#^irrbb-p03-1]].

## Tương quan với Quản trị Thanh khoản và FTP
- **Chính sách định giá chuyển vốn nội bộ (FTP)**: Đường cong FTP phải bóc tách riêng phần bù rủi ro lãi suất (IRRBB component) để chuyển toàn bộ rủi ro lãi suất từ các chi nhánh kinh doanh về Khối Nguồn vốn/ALM quản lý tập trung.
- **Đệm thanh khoản HQLA**: Các tài sản Level 1 có kỳ hạn ngắn (như T-bills, tín phiếu NHTW) có rủi ro EVE thấp nhưng tạo ra biến động NII cao khi lãi suất điều hành thay đổi nhanh; ngược lại, trái phiếu chính phủ kỳ hạn 10–15 năm bảo đảm dòng tiền NII cố định nhưng làm tăng đột biến độ nhạy $\Delta\text{EVE}$.
- **Mô hình và công cụ quản trị liên quan**:
  - [[economic-value-at-risk|Earnings at Risk (EaR)]]: Đo lường mức sụt giảm NII tối đa theo phương pháp phân phối xác suất song hành cùng EVaR.
  - [[interest-rate-swap|Hợp đồng Hoán đổi Lãi suất (IRS)]]: Khóa chặt lãi suất thả nổi hoặc cố định hoá chi phí vốn huy động để ổn định biên lãi ròng NIM.
  - [[interest-rate-cap-floor|Hạn mức Trần/Sàn Lãi suất (Caps/Floors)]]: Thiết lập biên độ an toàn cho thu nhập từ các khoản cho vay thả nổi và chi phí tiền gửi.
- Xem thêm tại [[economic-value-of-equity]], [[gap-risk]], [[economic-value-at-risk]], [[interest-rate-swap]], [[interest-rate-cap-floor]], [[integrated-alm-liquidity-strategy]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Định nghĩa | [cần nguồn] | Thay đổi thu nhập lãi thuần do thay đổi lãi suất từ tài sản, nợ phải trả, khoản mục ngoại bảng có lãi suất trên sổ ngân hàng [[src-tt83-2025-nhnn#^pl5-b1]] | TT83 PL5.B.I | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Chân trời, giả định bảng cân đối | Constant balance sheet, rolling 12 tháng [[src-bcbs-irrbb-2016#^irrbb-p08-3]] | 01 năm, constant balance sheet [[src-tt83-2025-nhnn#^pl5-b2]] | d368 par 70; TT83 PL5.B.II | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Kịch bản | 2 kịch bản cho NII [[src-bcbs-irrbb-2016#^irrbb-u07-1]] | Tăng song song và giảm song song; lấy giá trị giảm lớn nhất [[src-tt83-2025-nhnn#^pl5-b3]] | Annex 2; TT83 PL5.B.III | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Hạn mức | Phải có policy limits nhất quán với risk appetite; risk appetite nên thể hiện theo cả economic value và earnings [[src-bcbs-irrbb-2016#^irrbb-p03-1]]; hạn mức tổng nên áp dụng hợp nhất, có thể gắn với kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-p03-3]] | Phải có hạn mức thay đổi thu nhập lãi thuần [[src-tt83-2025-nhnn#^d53-2]] | d368 Principle 3, par 29; TT83 Đ53.2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Vượt hạn mức | Vị thế vượt hoặc có khả năng vượt nên được xử lý kịp thời và báo cáo lên ngay [[src-bcbs-irrbb-2016#^irrbb-p03-4]] | Phải có cảnh báo sớm khi gần vượt và biện pháp xử lý kịp thời khi vượt [[src-tt83-2025-nhnn#^d54-4c]] | d368 par 32; TT83 Đ54.4.c | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Lộ trình | Hiệu lực 2018 [[src-bcbs-irrbb-2016#^irrbb-u04-2]] | Được dùng ΔNII hoặc ΔEVE [[src-tt83-2025-nhnn#^d74-4a]]; phải dùng cả hai [[src-tt83-2025-nhnn#^d74-4b]] | TT83 Đ74.4 | 01/07/2026 – 31/12/2027; chậm nhất 01/01/2028 |
| Stress test IRRBB | IMS tính tác động của nhiều kịch bản, gồm sáu kịch bản sốc chuẩn hoá [[src-bcbs-irrbb-2016#^irrbb-p04-3]] | Tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]] | TT83 Đ23.5 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Commercial margin trong dòng tiền | Nên gồm commercial margin và spread [[src-bcbs-irrbb-2016#^irrbb-p08-3]] | [cần nguồn] (PL5 không nêu) | d368 par 70 | |

Khác biệt: [[tt83-2025]] ghi chân trời "01 năm" thay vì "rolling 12 tháng" và chưa quy định xử lý commercial margin trong dòng tiền ΔNII.

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5 — user duyệt [2026-10-19]: thêm mục `## Basel vs VN`. Định nghĩa ΔNII theo NHNN [[src-tt83-2025-nhnn#^pl5-b1]]; chân trời 01 năm, constant balance sheet [[src-tt83-2025-nhnn#^pl5-b2]] (Basel: rolling 12 tháng, p08-3); 2 kịch bản tăng/giảm song song, lấy giá trị giảm lớn nhất [[src-tt83-2025-nhnn#^pl5-b3]]; hạn mức ΔNII bắt buộc [[src-tt83-2025-nhnn#^d53-2]]; lộ trình [[src-tt83-2025-nhnn#^d74-4a]] [[src-tt83-2025-nhnn#^d74-4b]]. PL5 không nêu cách xử lý commercial margin trong dòng tiền ΔNII [cần nguồn]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 28, 29, 32) — user duyệt [2026-10-19]: trong `## Basel vs VN`, dòng "Hạn mức" thay `[cần nguồn]` ở cột Basel bằng: ngân hàng phải có policy limits nhất quán với risk appetite, risk appetite nên thể hiện theo cả economic value và earnings [[src-bcbs-irrbb-2016#^irrbb-p03-1]]; hạn mức tổng nên áp dụng hợp nhất, có thể gắn với kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-p03-3]]. Thêm dòng "Vượt hạn mức": Basel [[src-bcbs-irrbb-2016#^irrbb-p03-4]]; VN [[src-tt83-2025-nhnn#^d54-4c]]; điều khoản d368 par 32; TT83 Đ54.4.c. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1 — chờ user duyệt: đã có node [[risk-appetite]], [[risk-limits]]; đề xuất link ở lần nhắc đầu risk appetite / hạn mức. VN: stress test IRRBB tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u08 — chờ user duyệt: thêm phương pháp EBA SA (RTS/2022/09) như tham chiếu EU: NII = lãi đã cố định đến ngày tái định giá + lợi suất phi rủi ro sau tái định giá + biên thương mại sau reset, theo bảng cân đối không đổi [[src-tata-bank-alm#^tata-eba-2]]; biên thương mại nghiệp vụ mới theo biên năm trước [[src-tata-bank-alm#^tata-eba-3]]; cấu phần thay đổi giá trị thị trường cho công cụ ngoài kỳ NII, loại dòng tiền trong kỳ để tránh tính trùng [[src-tata-bank-alm#^tata-eba-4]]; SOT NII 5% vốn cấp 1 [[src-tata-bank-alm#^tata-sot-3]]. Link [[outlier-bank-test]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u06 — chờ user duyệt: thêm phần dự phóng: kế hoạch ALM phải tính độ nhạy EVE và NII kỳ vọng trong tương lai, cần khối lượng theo phân khúc hành vi và kỳ hạn nghiệp vụ mới [[src-tata-bank-alm#^tata-niip-6]]; margin-beta (NIM giảm 5 bp mỗi năm sau cú giảm 100 bp; 19 bp mỗi 100 bp lãi suất ngắn hạn) [[src-tata-bank-alm#^tata-niip-5]]. Link [[nii-planning]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm phương pháp gap: ΔNII ≈ GAP × Δi trong gapping period [[src-lubinska-alm-optimisation#^lubinska-u02-23]] [[src-lubinska-alm-optimisation#^lubinska-u02-25]]; mô phỏng NII phục vụ nhiều mục đích (stress test EBA có giả định cấu trúc sổ; thước đo nội bộ dùng sổ không đổi, khoản đáo hạn thay bằng khoản cùng đặc điểm) [[src-lubinska-alm-optimisation#^lubinska-u02-33]]. Link [[repricing-gap-analysis]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: thêm ví dụ số EAR (Choudhry ví dụ 6.12): gap tức thời −80, +1% song song làm NII giảm 0,8 triệu USD, EAR khoảng 7,8%, NIM giảm 40bp; NIM = (thu nhập lãi − chi phí lãi) / tài sản sinh lời bình quân [[src-choudhry-principles-banking#^choudhry-hedge-21]]; ALCO thường đặt hạn mức EAR ±5% hoặc ±10% [[src-choudhry-principles-banking#^choudhry-hedge-22]]. Lưu ý alias 'Earnings at Risk/EaR' đang nằm ở node này. Đã có node [[overnight-index-swap]] (phòng ngừa NII) [[src-choudhry-principles-banking#^choudhry-hedge-17]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: thêm ví dụ minh hoạ T4 (Choudhry Ex 1.5, ChoudWest): giả định lãi suất 5%, bảng cân đối không đổi 12 tháng, không FTP, đường cong phẳng [[src-choudhry-principles-banking#^choudhry-nim-1]]; NII cơ sở £461,0m [[src-choudhry-principles-banking#^choudhry-nim-2]]; +3% → NII +£64,7m (+14%), vì nhiều tài sản tái định giá hơn nợ [[src-choudhry-principles-banking#^choudhry-nim-4]]; lãi suất giảm xuống 4% → NII −£29,5m [[src-choudhry-principles-banking#^choudhry-nim-6]]. Ghi rõ đây là ví dụ minh hoạ, giả định khác d368 (sốc chuẩn, bảng cân đối cố định). → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: thêm cơ chế: NII nhạy lãi suất vì tài sản và nợ tái định giá ở thời điểm khác nhau [[src-choudhry-principles-banking#^choudhry-nim-9]]; ba kiểu phản ứng của lãi suất sản phẩm (giữ nguyên; bằng mức thay đổi benchmark; nhiều hơn hoặc ít hơn) [[src-choudhry-principles-banking#^choudhry-nim-3]]; ví dụ khoản vay cố định 10% và tiền gửi 1 tháng từ 2% lên 4% làm NII giảm từ £800 xuống £600 [[src-choudhry-principles-banking#^choudhry-nim-10]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: thêm vào phần dự báo: mô hình bottom-up cấp tài khoản, sốc lãi suất và tính lại để đo độ nhạy NII; thách thức dữ liệu [[src-choudhry-principles-banking#^choudhry-nim-13]]. Đã có node [[net-interest-margin]]; đề xuất link ở chỗ nhắc NIM. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u03 — chờ user duyệt: thêm vào mục horizon: thước đo thu nhập nội bộ thường dùng horizon ngân sách 3–4 năm [[src-bardaeva-alm#^ch11-16]], khác horizon ΔNII 01 năm của TT83 PL5 [[src-tt83-2025-nhnn#^pl5-b2]] (khác scope, không phải conflict). Link [[irrbb-management]]. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-irrbb-2016 U03/U06 (bổ sung) — chờ user duyệt: thêm vào phần giả định bảng cân đối: d368 Annex 1 phân ba trạng thái mô hình hoá thu nhập (run-off, constant, dynamic; dynamic là cách có ý nghĩa nhất) [[src-bcbs-irrbb-2016#^irrbb-u06-9]]; dynamic view hữu ích cho kế hoạch nhưng có thể che giấu rủi ro nền tảng [[src-bcbs-irrbb-2016#^irrbb-p04-4]]; chân trời thường 1–3 năm, không quá 5 năm [[src-bcbs-irrbb-2016#^irrbb-u06-8]]; ΔNII là chênh lệch giữa kịch bản cơ sở theo kế hoạch kinh doanh và kịch bản stress [[src-bcbs-irrbb-2016#^irrbb-u06-10]]. → đã áp dụng [2026-10-20]
- [2026-10-20] research nii-shocks-regulation-hedging-and-alco-tradeoffs — chờ user duyệt: đổi `cite` của cạnh `input-to → [[balance-sheet-optimisation-model]]` từ `lubinska-u05-11` (giới hạn tập trung nguồn vốn 80%) sang [[src-lubinska-alm-optimisation#^lubinska-u04-12]] (hạn mức biến động NII là ràng buộc bất đẳng thức của bài toán tối ưu). → đã áp dụng [2026-10-20]
