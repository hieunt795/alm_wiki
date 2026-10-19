---
title: "Quản trị Thu nhập Lãi thuần (NII): Bản chất, Cơ chế Khe hở Tái định giá, Rủi ro Hành vi và Kế hoạch hóa"
aliases:
  - "NII Nature, Repricing Mechanisms and Planning"
  - "Quản trị NII: Bản chất, Khe hở tái định giá và Kế hoạch hóa"
  - "Cơ chế truyền dẫn NII và Kế hoạch hóa NII"
type: synthesis
domains: [alm, product]
status: active
maturity: draft
origin: research
question: "Q1. Thu nhập lãi thuần (NII) và tỷ lệ thu nhập lãi thuần (NIM) được định nghĩa như thế nào trong cơ cấu tài chính ngân hàng? Những động lực (drivers) cốt lõi nào cấu thành NII và tạo ra sự biến động của NII/NIM (quy mô danh mục sinh lời/trả lãi — volume, mặt bằng lãi suất — rate, cơ cấu kỳ hạn và sản phẩm — asset-liability mix, và biên lãi thương mại — commercial spread)? · Q2. Rủi ro lãi suất trên sổ ngân hàng (IRRBB) truyền dẫn tới NII như thế nào qua mô hình repricing balance sheet và repricing gap analysis? Sự bất đối xứng về tốc độ và thời điểm tái định giá giữa Tài sản nhạy cảm lãi suất (RSA) và Nợ nhạy cảm lãi suất (RSL) tác động ra sao đến NII khi lãi suất tăng/giảm? · Q3. Hành vi phi kỳ hạn của tiền gửi (non-maturity deposits — hệ số pass-through rate của CASA, rủi ro chuyển dịch sang tiền gửi có kỳ hạn) và hành vi trả nợ trước hạn (prepayment của behavioural options) làm biến dạng và ảnh hưởng tới độ nhạy NII như thế nào qua các chu kỳ lãi suất? · Q4. Kỹ thuật lập kế hoạch NII (nii-planning: tiếp cận top-down vs bottom-up) và đo lường độ nhạy thu nhập lãi thuần (net-interest-income-sensitivity / Earnings at Risk — EaR) được thực hiện như thế nào trong khoảng thời gian 12 tháng (hoặc đa kỳ hạn) dưới giả định bảng cân đối tĩnh (constant balance sheet) vs bảng cân đối động (dynamic balance sheet)?"
as_of: 2026-10-19
sources:
  - "[[src-choudhry-principles-banking]]"
  - "[[src-lubinska-alm-optimisation]]"
  - "[[src-tata-bank-alm]]"
  - "[[src-bcbs-irrbb-2016]]"
  - "[[src-tt83-2025-nhnn]]"
relations: []
tags: [nii, nim, repricing-gap, nmd, behavioural-options, planning, ear]
updated: 2026-10-19
reviewed:
---

## Câu hỏi
- **Q1**: Thu nhập lãi thuần ([[net-interest-income-sensitivity|NII]]) và tỷ lệ thu nhập lãi thuần ([[net-interest-margin|NIM]]) được định nghĩa như thế nào trong cơ cấu tài chính ngân hàng? Những động lực (drivers) cốt lõi nào cấu thành NII và tạo ra sự biến động của NII/NIM (quy mô danh mục sinh lời/trả lãi — volume, mặt bằng lãi suất — rate, cơ cấu kỳ hạn và sản phẩm — asset-liability mix, và biên lãi thương mại — commercial spread)?
- **Q2**: Rủi ro lãi suất trên sổ ngân hàng ([[irrbb-management|IRRBB]]) truyền dẫn tới NII như thế nào qua mô hình [[repricing-balance-sheet]] và [[repricing-gap-analysis]]? Sự bất đối xứng về tốc độ và thời điểm tái định giá giữa Tài sản nhạy cảm lãi suất (RSA) và Nợ nhạy cảm lãi suất (RSL) tác động ra sao đến NII khi lãi suất tăng/giảm?
- **Q3**: Hành vi phi kỳ hạn của tiền gửi ([[non-maturity-deposits|NMD]] — hệ số pass-through rate của CASA, rủi ro chuyển dịch sang tiền gửi có kỳ hạn) và hành vi trả nợ trước hạn (prepayment của [[behavioural-options]]) làm biến dạng và ảnh hưởng tới độ nhạy NII như thế nào qua các chu kỳ lãi suất?
- **Q4**: Kỹ thuật lập kế hoạch NII ([[nii-planning]]: tiếp cận top-down vs bottom-up) và đo lường độ nhạy thu nhập lãi thuần ([[net-interest-income-sensitivity]] / Earnings at Risk — EaR) được thực hiện như thế nào trong khoảng thời gian 12 tháng (hoặc đa kỳ hạn) dưới giả định bảng cân đối tĩnh (*constant balance sheet*) vs bảng cân đối động (*dynamic balance sheet*)?

## Kết luận
- **Q1**: Thu nhập lãi thuần (NII) là chênh lệch giữa thu nhập lãi từ tài sản sinh lời và chi phí lãi phải trả cho nguồn vốn, chiếm 40–80% tổng thu nhập ngân hàng [[src-choudhry-principles-banking#^choudhry-nim-14]] [[src-tata-bank-alm#^tata-nii-1]]. Tỷ lệ thu nhập lãi thuần (NIM) bằng NII chia cho quy mô tài sản sinh lời bình quân, dao động phổ biến từ 1% đến 2,5% [[src-choudhry-principles-banking#^choudhry-nim-14]]. Biến động NII/NIM bị chi phối bởi 4 động lực cốt lõi: quy mô danh mục (*volume*), mặt bằng lãi suất chung (*rate*), cơ cấu kỳ hạn và sản phẩm (*mix*), cùng biên lãi thương mại (*commercial spread*) [[src-choudhry-principles-banking#^choudhry-nim-9]].
- **Q2**: Biến động lãi suất truyền dẫn tới NII thông qua độ lệch về thời điểm và khối lượng tái định giá giữa RSA và RSL theo công thức $\Delta\text{NII} \approx \text{GAP} \times \Delta i$ [[src-lubinska-alm-optimisation#^lubinska-u02-25]]. Trong thực tế, chu kỳ tái định giá diễn ra bất đối xứng: khi lãi suất giảm, nguồn vốn tiền gửi kỳ hạn ngắn reset nhanh giúp ngân hàng tiết kiệm chi phí lãi ngay lập tức, trong khi tài sản cho vay kỳ hạn dài reset chậm hơn khiến thu nhập lãi sụt giảm trễ hơn [[src-tata-bank-alm#^tata-nii-6]] [[src-tata-bank-alm#^tata-nii-7]].
- **Q3**: Tiền gửi không kỳ hạn (CASA/NMD) và quyền chọn trả nợ trước hạn phá vỡ các giả định hợp đồng thuần túy. Hệ số pass-through rate của CASA thường thấp hơn 100% nhưng có rủi ro dịch chuyển sang tiền gửi kỳ hạn và tăng beta khi lãi suất tăng cao [[src-tata-bank-alm#^tata-beh-4]] [[src-tata-bank-alm#^tata-rr-1]]. Quyền chọn prepayment tạo ra tính chất lồi âm (*negative convexity*): khi lãi suất giảm, khách hàng trả nợ sớm buộc ngân hàng phải tái đầu tư với lợi suất thấp hơn, làm suy giảm NII [[src-tata-bank-alm#^tata-opt-1]] [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
- **Q4**: Hoạch định NII được triển khai qua mô hình top-down dựa trên xu hướng sản phẩm hoặc bottom-up chi tiết theo từng tài khoản [[src-choudhry-principles-banking#^choudhry-nim-12]]. Đo lường độ nhạy $\Delta\text{NII}$ / EaR thường xem xét khung thời gian 12 tháng theo chuẩn BCBS d368 [[src-bcbs-irrbb-2016#^irrbb-p08-1]] [[src-tata-bank-alm#^tata-nii-4]]. Khi đo lường độ nhạy, sai số trong dự báo NII cơ sở phần lớn bị triệt tiêu vì các giả định được áp dụng đồng nhất cho cả kịch bản cơ sở lẫn kịch bản sốc [[src-tata-bank-alm#^tata-nii-3]].

## Cơ chế

### Q1 — Bản chất kinh tế và Động lực cốt lõi của NII/NIM

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[nii-planning]] | drives | [[net-interest-margin]] | | [[src-choudhry-principles-banking#^choudhry-nim-12]] |
| [[loan-pricing]] | input-to | [[net-interest-margin]] | | [[src-choudhry-principles-banking#^choudhry-lp-5]] |

- **Định nghĩa kinh tế**: NII là chênh lệch giữa thu nhập lãi từ tài sản và chi phí lãi của nợ phải trả trong một khoảng thời gian xác định [[src-tata-bank-alm#^tata-nii-1]]. Thước đo này đóng góp từ 40% đến 80% tổng thu nhập hoạt động của ngân hàng thương mại [[src-choudhry-principles-banking#^choudhry-nim-14]].
- **Công thức tỷ lệ thu nhập lãi thuần (NIM)**:
  $$\text{NIM} = \frac{\text{NII}}{\text{Average Interest-Earning Assets (IEA)}}$$
  [[src-choudhry-principles-banking#^choudhry-nim-14]]
- **Bốn động lực (drivers) cốt lõi của NII/NIM**:
  - **Quy mô (*Volume*)**: Sự tăng trưởng quy mô tài sản sinh lời (IEA) và nguồn vốn trả lãi (IBL). Tăng trưởng tài sản bằng nguồn vốn chi phí cao có thể làm tăng NII tuyệt đối nhưng lại kéo giảm NIM [[src-choudhry-principles-banking#^choudhry-nim-8]].
  - **Mặt bằng lãi suất (*Rate*)**: Biến động của lãi suất thị trường tác động lên cả lãi suất đầu ra và chi phí huy động đầu vào [[src-choudhry-principles-banking#^choudhry-nim-9]].
  - **Cơ cấu danh mục (*Asset-Liability Mix*)**: Tỷ trọng giữa tài sản có lợi suất cao so với tài sản thanh khoản lợi suất thấp (như đệm [[hqla]]), cũng như tỷ trọng giữa tiền gửi không kỳ hạn giá rẻ ([[non-maturity-deposits|CASA]]) và tiền gửi có kỳ hạn giá cao [[src-choudhry-principles-banking#^choudhry-nim-5]].
  - **Biên lãi thương mại (*Commercial Spread*)**: Khoản chênh lệch lãi suất thuần sau khi trừ chi phí vốn nội bộ ([[funds-transfer-pricing|FTP]]), phản ánh năng lực định giá cho vay ([[loan-pricing]]) và thương quyền của ngân hàng [[src-choudhry-principles-banking#^choudhry-lp-5]].

### Q2 — Cơ chế Khe hở Tái định giá và Sự Bất đối xứng RSA vs RSL

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[repricing-gap-analysis]] | input-to | [[net-interest-income-sensitivity]] | | [[src-lubinska-alm-optimisation#^lubinska-u02-25]] |
| [[repricing-balance-sheet]] | input-to | [[net-interest-income-sensitivity]] | | [[src-lubinska-alm-optimisation#^lubinska-u02-23]] |
| [[gap-risk]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-4]] |

- **Bản chất phơi nhiễm tái định giá**: Rủi ro lãi suất sổ ngân hàng phát sinh do tài sản và nợ trên bảng cân đối kế toán tái định giá tại các thời điểm khác nhau [[src-choudhry-principles-banking#^choudhry-nim-10]].
- **Mô hình Repricing Gap**: Khe hở tái định giá là chênh lệch giữa Tài sản nhạy cảm lãi suất (RSA) và Nợ nhạy cảm lãi suất (RSL) trong một dải kỳ hạn xác định:
  $$\text{GAP} = \text{RSA} - \text{RSL}$$
  [[src-lubinska-alm-optimisation#^lubinska-u02-24]]
- **Tác động tới $\Delta\text{NII}$**:
  $$\Delta\text{NII} \approx \text{GAP} \times \Delta i$$
  [[src-lubinska-alm-optimisation#^lubinska-u02-25]]
  - Khe hở dương ($\text{GAP} > 0$): Khi lãi suất tăng ($\Delta i > 0$), tài sản tái định giá lên mức lãi suất mới nhiều hơn nợ, dẫn đến $\Delta\text{NII} > 0$; ngược lại khi lãi suất giảm, NII sụt giảm [[src-choudhry-principles-banking#^choudhry-nim-6]].
  - Khe hở âm ($\text{GAP} < 0$): Khi lãi suất tăng, chi phí trả lãi tăng nhanh hơn thu nhập từ tài sản, làm giảm NII [[src-choudhry-principles-banking#^choudhry-nim-10]].
- **Cơ chế bất đối xứng thời gian (Tata Model)**:
  - Khi lãi suất giảm 100 bps, tiền gửi có kỳ hạn reset lãi suất sớm (ví dụ kỳ hạn 3 tháng) giúp ngân hàng giảm chi phí lãi ngay trong ngắn hạn [[src-tata-bank-alm#^tata-nii-6]].
  - Các khoản cho vay thế chấp kỳ hạn dài chỉ reset sau 1 năm hoặc lâu hơn, do đó thu nhập lãi giảm muộn hơn; hệ quả là NII có thể tăng tạm thời trong năm thứ nhất nhưng sụt giảm nghiêm trọng trong năm thứ hai và thứ ba [[src-tata-bank-alm#^tata-nii-7]] [[src-tata-bank-alm#^tata-nii-14]].

### Q3 — Biến dạng dòng tiền từ Tiền gửi NMD/CASA và Quyền chọn Prepayment

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[non-maturity-deposits]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-6]] |
| [[behavioural-options]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u02-2]] |
| [[replicating-portfolio-model]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-6]] |

- **Hành vi tiền gửi không kỳ hạn ([[non-maturity-deposits|NMD/CASA]])**:
  - Theo hợp đồng pháp lý, tiền gửi không kỳ hạn có thể bị rút hoặc tái định giá ngay lập tức (xếp vào dải ngắn nhất O/N) [[src-tata-bank-alm#^tata-rep-2]].
  - Trong thực tế, một bộ phận đáng kể số dư tiền gửi này có tính ổn định cao (*core deposits*) và lãi suất trả cho khách hàng biến động chậm hơn lãi suất thị trường (hệ số *pass-through rate* $< 100\%$) [[src-tata-bank-alm#^tata-beh-4]].
  - Chuẩn mực BCBS d368 và [[tt83-2025]] Phụ lục 5 khống chế trần kỳ hạn bình quân của NMD: tối đa 5 năm đối với tiền gửi bán lẻ giao dịch, 4,5 năm đối với bán lẻ phi giao dịch, và 4 năm đối với tiền gửi bán buôn [[src-bcbs-irrbb-2016#^irrbb-u05-4]] [[src-tt83-2025-nhnn#^pl5-a2-3a2]].
  - Nguy cơ chuyển dịch (*deposit migration*): Khi lãi suất thị trường tăng cao, tiền gửi không kỳ hạn có thể mất tính ổn định và hệ số beta tăng nhanh, đẩy chi phí huy động tăng vọt [[src-tata-bank-alm#^tata-rr-1]].
- **Quyền chọn trả nợ trước hạn ([[behavioural-options|Prepayment Risk]])**:
  - Khách hàng vay vốn có quyền chọn kinh tế trả nợ trước hạn khi lãi suất giảm để tái tài trợ với lãi suất rẻ hơn [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
  - Hành vi này triệt tiêu dòng tiền lãi suất cao kỳ vọng của ngân hàng, buộc ngân hàng phải tái đầu tư dòng tiền thu hồi vào các tài sản có lợi suất thấp hơn, gây ra hiện tượng lồi âm (*negative convexity*) đối với NII [[src-tata-bank-alm#^tata-opt-1]].

### Q4 — Phương pháp Hoạch định NII và Đo lường Độ nhạy 12 tháng (Constant vs Dynamic)

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[nii-planning]] | input-to | [[net-interest-income-sensitivity]] | | [[src-tata-bank-alm#^tata-nii-3]] |
| [[bcbs-irrbb]] | governs | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u01-4]] |

- **Cách tiếp cận lập kế hoạch NII ([[nii-planning]])**:
  - **Top-down**: Dự báo dựa trên các xu hướng tổng hợp ở cấp phân khúc sản phẩm hoặc khối kinh doanh, thường sử dụng bảng tính độc lập [[src-choudhry-principles-banking#^choudhry-nim-12]].
  - **Bottom-up**: Dự phóng chi tiết dựa trên dữ liệu dòng tiền và đặc tính từng hợp đồng từ hệ thống giao dịch nguồn. Thách thức lớn nhất là chất lượng và khả năng kết nối dữ liệu cấp tài khoản [[src-choudhry-principles-banking#^choudhry-nim-13]].
- **Nguyên lý bù trừ sai số giả định cơ sở (Fidelio Tata)**:
  - Phòng Kế toán tính NII quá khứ (*retrospective view*), trong khi phòng ALM đo lường NII hướng về tương lai (*prospective view*) [[src-tata-bank-alm#^tata-nii-2]].
  - Khi tính độ nhạy thu nhập:
    $$\Delta\text{NII} = \text{NII}_{\text{shock}} - \text{NII}_{\text{base}}$$
  - Độ chính xác tuyệt đối của dự báo $\text{NII}_{\text{base}}$ ít quan trọng đối với ALM, vì các giả định sai số được áp dụng lặp lại đồng nhất cho cả kịch bản sốc và sẽ bị triệt tiêu phần lớn khi trừ hai giá trị cho nhau [[src-tata-bank-alm#^tata-nii-3]].
- **Khung thời gian và giả định bảng cân đối**:
  - Khung thời gian tiêu chuẩn cho đo lường $\Delta\text{NII}$ / EaR là 12 tháng theo BCBS d368 Nguyên tắc 8, và có thể mở rộng từ 1 đến 3 năm trong quản trị nội bộ [[src-bcbs-irrbb-2016#^irrbb-p08-1]] [[src-tata-bank-alm#^tata-nii-4]].
  - **Bảng cân đối tĩnh (*Constant Balance sheet*)**: Giả định quy mô và cơ cấu tài sản, nợ được giữ nguyên; các khoản mục đáo hạn được tái đầu tư bằng các sản phẩm cùng loại và cùng kỳ hạn gốc [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
  - **Bảng cân đối động (*Dynamic Balance sheet*)**: Kết hợp kế hoạch kinh doanh tăng trưởng, dự kiến phát hành mới và phản ứng hành vi của khách hàng trong tương lai [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- **Vị thế loại trừ**: Toàn bộ tài sản phi tài chính, bất động sản, đầu tư vốn cổ phần và vốn chủ sở hữu kế toán được loại trừ khỏi phân tích độ nhạy NII vì không nhạy cảm với lãi suất [[src-tata-bank-alm#^tata-nii-5]].

## Bằng chứng ủng hộ
- Mô hình minh họa ChoudWest Bank của Moorad Choudhry chứng minh bằng số liệu cụ thể: khi lãi suất giảm trong môi trường tài sản nhạy cảm hơn nợ, thu nhập lãi giảm £102,5m trong khi chi phí trả lãi chỉ giảm £73,0m, kéo theo NII giảm £29,5m và NIM giảm 0,18% [[src-choudhry-principles-banking#^choudhry-nim-6]].
- Dữ liệu mô phỏng của Fidelio Tata trên danh mục mẫu cho thấy hợp đồng hoán đổi lãi suất (*receiver swap*) giúp cố định dòng tiền thu, giảm thiểu đáng kể mức sụt giảm NII trong giai đoạn 13–24 tháng khi xảy ra sốc giảm lãi suất 100 bps [[src-tata-bank-alm#^tata-nii-16]].
- Nghiên cứu của Irena Lubinska xác nhận tương quan chặt chẽ giữa khe hở tái định giá và biến động NII theo mô hình sốc song song $\pm 200$ bps [[src-lubinska-alm-optimisation#^lubinska-u02-23]] [[src-lubinska-alm-optimisation#^lubinska-u02-25]].

## Bằng chứng trái chiều
- **Mâu thuẫn giữa quy mô và hiệu suất**: Mở rộng quy mô tín dụng có thể làm tăng NII danh nghĩa nhưng lại làm giảm NIM nếu biên sinh lời của mảng kinh doanh mới thấp hơn danh mục hiện hữu [[src-choudhry-principles-banking#^choudhry-nim-8]].
- **Mâu thuẫn giữa giảm rủi ro thanh khoản và lợi nhuận NII**: Hành động gia tăng nguồn vốn huy động dài hạn để cải thiện chỉ số thanh khoản tạo thêm chi phí lãi, trực tiếp làm sụt giảm cả NII và NIM so với kịch bản cơ sở [[src-choudhry-principles-banking#^choudhry-nim-5]].
- **Mâu thuẫn giữa góc nhìn kế toán và ALM**: Báo cáo tài chính kế toán ghi nhận NII hồi tố theo chuẩn dồn tích, trong khi ALM tập trung vào độ nhạy dòng tiền kỳ hạn tương lai [[src-tata-bank-alm#^tata-nii-2]].

## Phụ thuộc regime
- **Môi trường lãi suất tăng (*Rising rate regime*)**:
  - Ngân hàng có khe hở tái định giá dương ($\text{RSA} > \text{RSL}$) được hưởng lợi gia tăng NII ngắn hạn [[src-choudhry-principles-banking#^choudhry-nim-4]].
  - Tuy nhiên, lãi suất tăng kích hoạt rủi ro chuyển dịch tiền gửi CASA sang tiền gửi có kỳ hạn, làm tăng nhanh chi phí vốn [[src-tata-bank-alm#^tata-rr-1]].
- **Môi trường lãi suất giảm (*Falling rate regime*)**:
  - Ngân hàng chịu rủi ro sụt giảm NII nếu tài sản reset nhanh hơn nợ [[src-choudhry-principles-banking#^choudhry-nim-6]].
  - Kích hoạt áp lực prepayment từ người vay thế chấp, làm khuếch đại đà giảm của NII [[src-tata-bank-alm#^tata-opt-1]].
- **Bối cảnh pháp lý tại Việt Nam**:
  - Theo [[tt83-2025]] Phụ lục 5, ngân hàng Việt Nam khi đo lường dòng tiền tái định giá phải áp dụng trần kỳ hạn đối với NMD và phân tách tiền gửi có kỳ hạn có khả năng rút trước hạn theo các kịch bản chuẩn hóa của NHNN [[src-tt83-2025-nhnn#^pl5-a2-3a2]] [[src-tt83-2025-nhnn#^pl5-a2-3b]].

## Hàm ý ALM / quy định
- **Thiết lập hệ thống thông tin quản trị (MI pack) cho ALCO**: ALCO cần theo dõi đồng thời báo cáo khe hở tái định giá ([[repricing-gap-analysis]]), độ nhạy NII 12 tháng ([[net-interest-income-sensitivity]]) và phân rã các động lực NIM [[src-choudhry-principles-banking#^choudhry-nim-12]].
- **Kiểm soát định giá tín dụng**: ALCO phải thiết lập lãi suất sàn mục tiêu (*Target Rate of Return Floor Rate — TRR*) để ngăn chặn các đơn vị kinh doanh tăng trưởng quy mô bằng mọi giá làm xói mòn NIM [[src-choudhry-principles-banking#^choudhry-lp-6]].
- **Nâng cao chất lượng dữ liệu cấp tài khoản**: Ngân hàng cần chuyển đổi từ mô hình dự báo top-down trên bảng tính sang mô hình bottom-up tích hợp, cho phép stress testing NII tự động theo từng kịch bản biến động lãi suất [[src-choudhry-principles-banking#^choudhry-nim-13]].

## Bất định
- **Tốc độ phản ứng thực tế của người gửi tiền CASA**: Hệ số pass-through rate và tỷ lệ rút vốn thực tế của tiền gửi không kỳ hạn tại các ngân hàng thương mại Việt Nam có thể biến động mạnh trong giai đoạn biến động thanh khoản hệ thống, vượt khỏi giả định lịch sử.
- **Dữ liệu hành vi prepayment tại Việt Nam**: Hiện nguồn đã ingest chưa có số liệu thống kê chi tiết về tỷ lệ trả nợ trước hạn theo chu kỳ lãi suất của danh mục vay mua nhà tại Việt Nam; ngân hàng cần calibration mô hình nội bộ theo quy định tại Điều 56 Thông tư 83/2025/TT-NHNN [[src-tt83-2025-nhnn#^d56-2]].
