---
title: "Net Interest Income Sensitivity (ΔNII)"
aliases: [NII Sensitivity, Thu nhập lãi thuần nhạy cảm lãi suất, ΔNII, Delta NII, Earnings at Risk, EaR]
type: metric
domains: [alm, basel]
status: active
maturity: canonical
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: measures, to: "[[basis-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: measures, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[outlier-bank-test]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-2]]"}
  - {type: input-to, to: "[[balance-sheet-optimisation-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u05-11]]"}
tags: [irrbb, nii, earnings-at-risk, alm, interest-income, constant-balance-sheet]
updated: 2026-10-17
reviewed:
---

## Định nghĩa
Độ nhạy thu nhập lãi thuần (Net Interest Income Sensitivity - $\Delta\text{NII}$) đo lường mức độ biến động của thu nhập thuần từ lãi dự kiến trong một khoảng thời gian xác định (thường là 12 tháng liên tục, hoặc 1 đến 3 năm) do tác động của các kịch bản sốc lãi suất so với kịch bản kế hoạch cơ sở của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u01-4]] [[src-bcbs-irrbb-2016#^irrbb-p08-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

Khác với [[economic-value-of-equity|$\Delta\text{EVE}$]] vốn là thước đo định giá kinh tế dài hạn cho mục tiêu an toàn vốn của cơ quan giám sát, $\Delta\text{NII}$ là thước đo trọng tâm trong hoạt động điều hành thương mại hàng ngày của Ban điều hành và Hội đồng ALCO [[src-bcbs-irrbb-2016#^irrbb-u02-4]]:
- **Tác động trực tiếp lên P&L và cổ tức**: Thu nhập lãi thuần quyết định khả năng sinh lời thực tế, ảnh hưởng đến khả năng chia cổ tức ổn định, chi phí vốn và mức tích lũy lợi nhuận giữ lại để bổ sung vốn tự có trong ngắn hạn [[src-bcbs-irrbb-2016#^irrbb-u06-5]].
- **Góc nhìn hoạt động liên tục (Going-concern)**: Đánh giá khả năng của ngân hàng tạo ra dòng tiền thu nhập đủ lớn để trang trải chi phí hoạt động và duy trì vị thế cạnh tranh mà không bị suy giảm nguồn lực tài chính [[src-bcbs-irrbb-2016#^irrbb-u06-5]].
- **Góc nhìn Kế toán vs ALM theo Fidelio Tata**: Phòng Kế toán tính NII cho quá khứ (*retrospective view*), bao gồm các thay đổi và biến động trong tháng [[src-tata-bank-alm#^tata-nii-12]]; phòng ALM định lượng phơi nhiễm thu nhập lãi thuần theo hướng tương lai (*prospective view*) [[src-tata-bank-alm#^tata-nii-2]]. Khi tính độ nhạy NII, các vị thế không nhạy cảm lãi suất như bất động sản, đầu tư cổ phần, tài sản vô hình và vốn chủ sở hữu của ngân hàng có thể được loại khỏi phân tích [[src-tata-bank-alm#^tata-nii-5]].
- **Cơ chế triệt tiêu sai số mô hình (Error Cancellation)**: Khi tính toán độ nhạy NII ($\Delta\text{NII}$), độ chính xác tuyệt đối của dự báo NII cơ sở ít quan trọng hơn đối với ALM so với dự báo P&L kế toán; bởi vì các giả định sai sẽ được áp dụng lặp lại đồng thời trong cả kịch bản cơ sở và kịch bản sốc, do đó phần lớn sai số sẽ bị triệt tiêu khi lấy hiệu số giữa hai kịch bản [[src-tata-bank-alm#^tata-nii-3]]. Chân trời dự báo NII thường là ngắn đến trung hạn, phổ biến từ 1 đến 3 năm; kéo dài quá xa sẽ tạo cảm giác chính xác giả tạo, vì không thể dự báo vững chắc thay đổi trong hoạt động kinh doanh khách hàng trong dài hạn [[src-tata-bank-alm#^tata-nii-4]].

## Quy chuẩn đo lường và tính toán theo Basel (d368)

Theo Nguyên tắc 8 của [[bcbs-irrbb]], khi tính toán và công bố $\Delta\text{NII}$ theo Bảng B, ngân hàng phải áp dụng các quy chuẩn sau:

### 1. Đường chân trời đánh giá (Horizon)
- Chuẩn mực công bố Trụ cột 3 yêu cầu đánh giá trên giai đoạn **12 tháng liên tục (rolling 12-month period)** [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- Trong quản trị nội bộ ALCO, các ngân hàng thường mở rộng theo dõi lên 2–3 năm (tối đa 5 năm) để kiểm soát rủi ro tích luỹ của chu kỳ lãi suất [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

### 2. Giả định Bảng cân đối kế toán (Balance Sheet Assumption)
Basel và chuẩn mực EBA/Lubinska phân biệt 3 trạng thái mô hình hoá bảng cân đối trong đo lường thu nhập [[src-bcbs-irrbb-2016#^irrbb-u06-5]] [[src-lubinska-alm-optimisation#^lubinska-u05-8]]:
- **Bảng cân đối không đổi (Constant balance sheet)**: Quy mô và cơ cấu bảng cân đối được duy trì cố định; các tài sản và khoản nợ đáo hạn được thay thế bằng các công cụ mới có cùng đặc điểm tài chính (like-for-like replacement). Đây là **giả định bắt buộc đối với công bố Trụ cột 3** [[src-bcbs-irrbb-2016#^irrbb-p08-3]] và là giả định nền tảng cho mô hình tối ưu hóa [[balance-sheet-optimisation-model]] [[src-lubinska-alm-optimisation#^lubinska-u05-8]].
- **Bảng cân đối động (Dynamic balance sheet)**: Phản ánh kế hoạch tăng trưởng kinh doanh mới, sự thay đổi trong hành vi khách hàng và các phản ứng điều hành chủ động của ngân hàng; phù hợp cho mục đích lập ngân sách và kế hoạch tài chính ALCO [[src-bcbs-irrbb-2016#^irrbb-p04-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-5]] [[src-lubinska-alm-optimisation#^lubinska-u05-8]].
- **Bảng cân đối thu hẹp (Run-off balance sheet)**: Giả định các vị thế đáo hạn không được tái đầu tư, ngoại trừ phần cần thiết để tài trợ cho tài sản còn lại [[src-bcbs-irrbb-2016#^irrbb-u06-5]] [[src-lubinska-alm-optimisation#^lubinska-u05-8]].

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


## Xung đột chiến lược giữa EVE và NII (The EVE vs NII Trade-off)

Ủy ban Basel cảnh báo rõ ràng về sự đánh đổi giữa hai thước đo trong điều hành ALM [[src-bcbs-irrbb-2016#^irrbb-u02-4]]:
- **Nếu ngân hàng triệt tiêu rủi ro $\Delta\text{EVE}$**: Ngân hàng thực hiện khớp chính xác kỳ hạn tái định giá giữa tài sản và nợ (ví dụ tài trợ tài sản cố định dài hạn bằng nợ dài hạn cố định, hoặc đưa toàn bộ tài sản về lãi suất thả nổi ngắn hạn khớp với tiền gửi ngắn hạn). Khi đó, giá trị kinh tế của ngân hàng được bảo vệ hoàn hảo trước các cú sốc lãi suất. Tuy nhiên, khi lãi suất thị trường giảm sâu, lợi suất tài sản ngắn hạn giảm ngay lập tức trong khi chi phí vốn (hoặc chi phí vận hành) không thể giảm tương ứng, dẫn tới sự sụt giảm và biến động dữ dội của thu nhập lãi thuần $\Delta\text{NII}$.
- **Nếu ngân hàng triệt tiêu rủi ro $\Delta\text{NII}$**: Để bảo vệ thu nhập lãi ổn định cho nguồn tiền gửi không kỳ hạn (NMDs) hoặc vốn chủ sở hữu, ngân hàng đầu tư nguồn vốn này vào một danh mục trái phiếu cố định dài hạn ([[src-bcbs-irrbb-2016#^irrbb-u06-6]]). Dòng thu nhập từ trái phiếu cố định dài hạn giúp NII hoàn toàn miễn nhiễm với biến động lãi suất ngắn hạn. Tuy nhiên, hành động này kéo dài thời lượng của bảng cân đối, khiến giá trị kinh tế $\Delta\text{EVE}$ chịu rủi ro cực lớn khi lãi suất tăng vọt.
- **Kết luận**: Ngân hàng không thể tối ưu hoá đồng thời cả EVE và NII mà phải chấp nhận một điểm cân bằng chiến lược phù hợp với khẩu vị rủi ro và các hạn mức nội bộ được HĐQT phê duyệt [[src-bcbs-irrbb-2016#^irrbb-p03-1]].

## Tương quan với Quản trị Thanh khoản và FTP
- **Chính sách định giá chuyển vốn nội bộ (FTP)**: Đường cong FTP phải bóc tách riêng phần bù rủi ro lãi suất (IRRBB component) để chuyển toàn bộ rủi ro lãi suất từ các chi nhánh kinh doanh về Khối Nguồn vốn/ALM quản lý tập trung.
- **Đệm thanh khoản HQLA**: Các tài sản Level 1 có kỳ hạn ngắn (như T-bills, tín phiếu NHTW) có rủi ro EVE thấp nhưng tạo ra biến động NII cao khi lãi suất điều hành thay đổi nhanh; ngược lại, trái phiếu chính phủ kỳ hạn 10–15 năm bảo đảm dòng tiền NII cố định nhưng làm tăng đột biến độ nhạy $\Delta\text{EVE}$.
- **Mô hình và công cụ quản trị liên quan**:
  - [[economic-value-at-risk|Earnings at Risk (EaR)]]: Đo lường mức sụt giảm NII tối đa theo phương pháp phân phối xác suất song hành cùng EVaR.
  - [[interest-rate-swap|Hợp đồng Hoán đổi Lãi suất (IRS)]]: Khóa chặt lãi suất thả nổi hoặc cố định hoá chi phí vốn huy động để ổn định biên lãi ròng NIM.
  - [[interest-rate-cap-floor|Hạn mức Trần/Sàn Lãi suất (Caps/Floors)]]: Thiết lập biên độ an toàn cho thu nhập từ các khoản cho vay thả nổi và chi phí tiền gửi.
- Xem thêm tại [[economic-value-of-equity]], [[gap-risk]], [[economic-value-at-risk]], [[interest-rate-swap]], [[interest-rate-cap-floor]], [[integrated-alm-liquidity-strategy]].
