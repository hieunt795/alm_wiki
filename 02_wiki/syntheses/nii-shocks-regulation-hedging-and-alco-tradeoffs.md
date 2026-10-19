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
as_of: 2026-10-19
sources:
  - "[[src-bcbs-irrbb-2016]]"
  - "[[src-tt83-2025-nhnn]]"
  - "[[src-tata-bank-alm]]"
  - "[[src-choudhry-principles-banking]]"
  - "[[src-lubinska-alm-optimisation]]"
relations: []
tags: [nii, shocks, bcbs-d368, tt83-2025, hedging, irs, alco, tradeoffs, eve]
updated: 2026-10-19
reviewed:
---

## Câu hỏi
- **Q5**: Các kịch bản sốc lãi suất chuẩn hóa (Parallel Up/Down, Flattener, Steepener, Short Rate...) tác động như thế nào đến NII? Làm thế nào để phân tách tác động của biến động lãi suất thị trường (base rate) khỏi biên thương mại (commercial margin / FTP spread) và rủi ro cơ sở ([[basis-risk]])?
- **Q6**: Chuẩn mực BCBS ([[bcbs-irrbb]] d368 / SRP31) và quy định của NHNN Việt Nam ([[tt83-2025]], C3-M7 và Phụ lục 5) quy định nghĩa vụ đo lường, báo cáo và kiểm tra sức chịu đựng (stress testing) đối với NII/EaR như thế nào? Có những điểm khác biệt cốt lõi nào giữa Basel và NHNN về khung đo lường NII?
- **Q7**: Ngân hàng quản trị và phòng ngừa rủi ro NII thông qua những công cụ nào (cơ chế truyền dẫn [[funds-transfer-pricing|FTP]], chính sách định giá cho vay/tiền gửi, danh mục đầu tư sao chép CASA — [[replicating-portfolio-model]], và phái sinh hoán đổi lãi suất — [[interest-rate-swap|IRS]] / cap/floor)?
- **Q8**: Hội đồng [[alco|ALCO]] giải quyết bài toán đánh đổi chiến lược giữa tối ưu hóa NII trong ngắn hạn (12 tháng) và bảo vệ giá trị kinh tế dài hạn của vốn chủ sở hữu ([[economic-value-of-equity|EVE]]), cũng như đánh đổi giữa [[net-interest-margin|NIM]] và chi phí đệm thanh khoản ([[lcr-nsfr-interlinkages]] / carry cost của [[hqla]]) như thế nào?

## Kết luận
- **Q5**: Sáu kịch bản sốc chuẩn hóa của Basel d368 chi phối toàn bộ đường cong lãi suất; trong đó 2 kịch bản sốc song song (Parallel Up/Down) được áp dụng bắt buộc để đo lường $\Delta\text{NII}$ [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. Để phân tích chính xác, ngân hàng phân tách lãi suất thành lãi suất thị trường phi rủi ro (*base rate*), biên thương mại (*commercial margin*) và độ lệch cơ sở (*basis spread*); trong đó biên thương mại được giả định giữ nguyên hoặc khấu trừ để cách ly rủi ro tái định giá thuần túy [[src-bcbs-irrbb-2016#^irrbb-p08-3]] [[src-choudhry-principles-banking#^choudhry-alco-19]].
- **Q6**: Chuẩn mực Basel d368 (Nguyên tắc 8) yêu cầu công bố $\Delta\text{NII}$ 12 tháng dưới kịch bản sốc song song, nhưng không quy định tỷ lệ trừng phạt ngoại lai (*outlier test*) cứng đối với NII (chỉ EBA/EU áp ngưỡng SOT NII 5% Vốn cấp 1) [[src-bcbs-irrbb-2016#^irrbb-p08-1]] [[src-tata-bank-alm#^tata-sot-3]]. Ngược lại, [[tt83-2025]] (Điều 53–55 và Phụ lục 5) bắt buộc đo lường $\Delta\text{NII}$ định kỳ tối thiểu hằng quý, kiểm tra sức chịu đựng hằng năm và giao HĐQT/ALCO thiết lập hạn mức nội bộ; giá trị giảm lớn nhất giữa 2 kịch bản sốc song song là mức đo lường IRRBB theo NII của ngân hàng [[src-tt83-2025-nhnn#^d53-1a2]] [[src-tt83-2025-nhnn#^pl5-b3]].
- **Q7**: Ngân hàng điều hành và phòng ngừa rủi ro NII thông qua cơ chế 4 tầng: (1) truyền dẫn chi phí vốn qua đường cong [[funds-transfer-pricing|FTP]] để tập trung rủi ro lãi suất về Treasury; (2) kiểm soát lãi suất sàn mục tiêu (TRR) trong định giá cho vay ([[loan-pricing]]); (3) mô hình hóa danh mục sao chép ([[replicating-portfolio-model]]) cho CASA để ổn định lợi suất; và (4) sử dụng các hợp đồng hoán đổi lãi suất ([[interest-rate-swap|Receiver/Payer IRS]]) để cân bằng khe hở tái định giá và bảo vệ dòng tiền thu nhập [[src-choudhry-principles-banking#^choudhry-lp-6]] [[src-tata-bank-alm#^tata-nii-16]] [[src-bcbs-irrbb-2016#^irrbb-u06-5]].
- **Q8**: Hội đồng ALCO đối mặt với sự đánh đổi cơ bản: NII và EVE thường phản ứng ngược chiều nhau trước cùng một biến động lãi suất [[src-tata-bank-alm#^tata-nii-11]]. Việc kéo dài thời lượng tài sản hoặc dùng Receiver IRS giúp ổn định NII khi lãi suất giảm nhưng lại làm tăng tổn thất EVE khi lãi suất tăng [[src-tata-bank-alm#^tata-nii-10]]. Đồng thời, việc duy trì tỷ lệ thanh khoản pháp định (LCR/NSFR) buộc ngân hàng nắm giữ đệm [[hqla]] sinh lời thấp, gây chi phí carry âm trực tiếp làm suy giảm NIM và NII [[src-choudhry-principles-banking#^choudhry-cs-20]] [[src-lubinska-alm-optimisation#^lubinska-u04-12]].

## Cơ chế

### Q5 — Kịch bản Sốc Chuẩn hóa và Phân rã Biên Thương mại / Basis Risk

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[standardised-interest-rate-shocks]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-p08-1]] |
| [[basis-risk]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-4]] |

- **Hệ thống 6 kịch bản sốc chuẩn hóa Basel Annex 2**:
  - Gồm: (1) Tăng song song (*parallel up*); (2) Giảm song song (*parallel down*); (3) Dốc lên (*steepener*); (4) Phẳng đi (*flattener*); (5) Lãi suất ngắn hạn tăng (*short rates up*); (6) Lãi suất ngắn hạn giảm (*short rates down*) [[src-bcbs-irrbb-2016#^irrbb-u07-1]].
  - Riêng đối với thước đo thu nhập $\Delta\text{NII}$, chuẩn BCBS d368 và [[tt83-2025]] Phụ lục 5 áp dụng bắt buộc 2 kịch bản cú sốc song song (tăng và giảm) [[src-bcbs-irrbb-2016#^irrbb-u07-1]] [[src-tt83-2025-nhnn#^pl5-b3]].
- **Biên độ sốc theo đồng tiền**:
  - Đối với các ngoại tệ lớn (USD, EUR, GBP): biên độ sốc song song là $\pm 200$ bps [[src-bcbs-irrbb-2016#^irrbb-u07-5]].
  - Đối với đồng Việt Nam (VND): [[tt83-2025]] Phụ lục 5 quy định biên độ sốc song song là $\pm 400$ bps (hoặc số liệu hiệu chỉnh theo chu kỳ phân vị 99% / 16 năm của NHNN) [[src-tt83-2025-nhnn#^pl5-c1-2]].
- **Kỹ thuật phân rã dòng tiền (Commercial Margin Unbundling)**:
  - Lãi suất sản phẩm được bóc tách:
    $$r_{\text{product}} = r_{\text{base}} + s_{\text{basis}} + m_{\text{commercial}}$$
  - Theo chuẩn BCBS d368 Nguyên tắc 8, khi tính toán $\Delta\text{NII}$, các dòng tiền tái định giá phải bao gồm biên thương mại và spread hiện hữu [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
  - Khi phân tích nguồn gốc biến động, ALCO phân tách: phần thay đổi do lãi suất cơ sở ($r_{\text{base}}$) thuộc trách nhiệm quản trị của Treasury; phần thay đổi do biên thương mại ($m_{\text{commercial}}$) thuộc trách nhiệm định giá của khối kinh doanh; và phần thay đổi do tương quan các chỉ số tham chiếu ($s_{\text{basis}}$) phản ánh rủi ro cơ sở [[src-choudhry-principles-banking#^choudhry-alco-19]].

### Q6 — Khung Pháp lý Đo lường NII: Chuẩn mực BCBS vs Quy định NHNN

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[bcbs-irrbb]] | governs | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u01-4]] |
| [[tt83-2025]] | governs | [[net-interest-income-sensitivity]] | | [[src-tt83-2025-nhnn#^d53-1a2]] |
| [[outlier-bank-test]] | part-of | [[bcbs-irrbb]] | | [[src-bcbs-irrbb-2016#^irrbb-p12-1]] |

- **So sánh Khung Đo lường NII giữa BCBS d368 và TT83/2025/TT-NHNN**:

| Tiêu chí | Chuẩn mực BCBS d368 | Quy định NHNN (TT83/2025/TT-NHNN) |
|---|---|---|
| **Vị thế đo lường** | Bắt buộc song song cả $\Delta\text{EVE}$ và $\Delta\text{NII}$ (Nguyên tắc 1 & 8) [[src-bcbs-irrbb-2016#^irrbb-u01-4]] | Bắt buộc song song cả $\Delta\text{EVE}$ và $\Delta\text{NII}$ (Điều 53.1.a.ii) [[src-tt83-2025-nhnn#^d53-1a2]] |
| **Kịch bản sốc cho NII** | 2 kịch bản song song (Parallel Up / Down) [[src-bcbs-irrbb-2016#^irrbb-u07-1]] | 2 kịch bản song song (tăng và giảm) (PL5.B.III) [[src-tt83-2025-nhnn#^pl5-b3]] |
| **Giá trị đo lường rủi ro** | Chênh lệch thu nhập lãi trong giai đoạn 12 tháng liên tục [[src-bcbs-irrbb-2016#^irrbb-p08-3]] | Giá trị giảm lớn nhất của NII trong 2 kịch bản sốc (PL5.B.III) [[src-tt83-2025-nhnn#^pl5-b3]] |
| **Phép thử ngoại lai (Outlier test)** | Chỉ áp dụng ngưỡng cứng $\Delta\text{EVE} \ge 15\%$ Tier 1 Capital (Nguyên tắc 12) [[src-bcbs-irrbb-2016#^irrbb-p12-1]]. Không có ngưỡng cứng cho NII (để ngỏ cho supervisor) [[src-bcbs-irrbb-2016#^irrbb-p12-7]] | Không áp ngưỡng ngoại lai cứng cho NII; HĐQT/ALCO tự phê duyệt hạn mức IRRBB nội bộ (Điều 54) [[src-tt83-2025-nhnn#^d54-1a]] |
| **Tần suất kiểm tra** | Rà soát thường xuyên; công bố định kỳ hàng năm [[src-bcbs-irrbb-2016#^irrbb-p08-1]] | Nhận dạng, đo lường tối thiểu hằng quý (Điều 54.1.a); stress test tối thiểu hằng năm (Điều 55.1) [[src-tt83-2025-nhnn#^d54-1a]] [[src-tt83-2025-nhnn#^d55-1]] |
| **Khung EU/EBA tham chiếu** | EBA RTS áp dụng ngưỡng giám sát bổ sung (SOT NII) là $\Delta\text{NII} \ge 5\%$ Vốn cấp 1 [[src-tata-bank-alm#^tata-sot-3]] | Không áp dụng ngưỡng SOT NII 5% |

### Q7 — Công cụ Quản trị và Phòng ngừa Rủi ro NII tại Ngân hàng

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[structural-hedging]] | hedges | [[gap-risk]] | | [[src-choudhry-principles-banking#^choudhry-cs-17]] |
| [[interest-rate-swap]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-5]] |
| [[loan-pricing]] | input-to | [[net-interest-margin]] | | [[src-choudhry-principles-banking#^choudhry-lp-5]] |

- **Hệ thống điều chuyển vốn nội bộ ([[funds-transfer-pricing|FTP]])**:
  - FTP là động cơ trung tâm giúp ngân hàng tách rủi ro lãi suất khỏi các đơn vị kinh doanh (chi nhánh) và chuyển giao tập trung về ALM Desk / Treasury [[src-choudhry-principles-banking#^choudhry-cs-20]].
  - Đơn vị huy động nhận được lãi suất FTP mua vốn (FTP credit); đơn vị cho vay trả lãi suất FTP bán vốn (FTP charge); biên thương mại của đơn vị kinh doanh được cố định độc lập với biến động lãi suất thị trường [[src-choudhry-principles-banking#^choudhry-cs-20]].
- **Cơ chế kiểm soát định giá cho vay ([[loan-pricing]])**:
  - Lãi suất cho vay được xây dựng dựa trên chi phí vốn FTP, chi phí tổn thất tín dụng kỳ vọng ([[expected-credit-loss|ECL]]), chi phí vận hành và tỷ suất sinh lời trên vốn mục tiêu (target RoE) [[src-choudhry-principles-banking#^choudhry-lp-5]].
  - Hội đồng ALCO ban hành sàn lãi suất mục tiêu (*Target Rate of Return Floor Rate — TRR*) để ngăn chặn các đơn vị kinh doanh hạ chuẩn định giá [[src-choudhry-principles-banking#^choudhry-lp-6]].
- **Mô hình danh mục sao chép ([[replicating-portfolio-model]]) cho CASA**:
  - Thay vì xem CASA là nguồn vốn ngắn hạn tái định giá O/N, Treasury mô phỏng hành vi tiền gửi lõi thành một chuỗi các danh mục đầu tư kỳ hạn cố định liên hoàn (*rolling tranches*) [[src-tata-bank-alm#^tata-nmd-3]].
  - Kỹ thuật này giúp khóa chặt lợi suất đầu tư dài hạn, tạo ra dòng thu nhập lãi thuần ổn định qua các chu kỳ biến động lãi suất [[src-tata-bank-alm#^tata-nmd-3]].
- **Phòng ngừa cấu trúc ([[structural-hedging]]) bằng Hoán đổi Lãi suất ([[interest-rate-swap|IRS]])**:
  - Khi ngân hàng có khe hở tái định giá dương ($\text{RSA} > \text{RSL}$) đối mặt với nguy cơ sụt giảm NII khi lãi suất giảm: Treasury tham gia vị thế **Receiver IRS** (nhận lãi suất cố định, trả lãi suất thả nổi) [[src-tata-bank-alm#^tata-nii-15]].
  - Kết quả mô phỏng của Fidelio Tata: Hợp đồng 3 năm Receiver IRS giúp ổn định NII, cắt giảm đáng kể mức sụt giảm thu nhập trong năm thứ hai khi xảy ra cú sốc giảm lãi suất 100 bps [[src-tata-bank-alm#^tata-nii-16]].

### Q8 — Bài toán Đánh đổi Chiến lược tại ALCO: NII vs EVE và NIM vs HQLA Carry

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[lcr-nsfr-interlinkages]] | drives | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u02-4]] |
| [[balance-sheet-optimisation-model]] | drives | [[repricing-balance-sheet]] | | [[src-lubinska-alm-optimisation#^lubinska-u04-13]] |
| [[net-interest-income-sensitivity]] | input-to | [[alco]] | | [[src-choudhry-principles-banking#^choudhry-alco-18]] |

- **Sự đánh đổi căn bản: NII (Thu nhập ngắn hạn) vs EVE (Giá trị kinh tế dài hạn)**:
  - NII và EVE thường phản ứng ngược chiều nhau trước cùng một biến động lãi suất [[src-tata-bank-alm#^tata-nii-11]].
  - Ví dụ: Việc bổ sung hợp đồng Receiver IRS giúp bảo vệ thu nhập NII khi lãi suất giảm, nhưng lại làm gia tăng khe hở thời lượng (*repricing gap*) từ 1,74 lên 3,63; hệ quả là làm tăng mức tổn thất giá trị vốn chủ sở hữu ($\Delta\text{EVE}$) nếu lãi suất bất ngờ tăng trở lại [[src-tata-bank-alm#^tata-nii-10]].
  - Bài toán tuân thủ đồng thời (*joint compliance*): ALCO phải giải bài toán quy hoạch tuyến tính đa mục tiêu để vùng khả thi không bị vi phạm dưới cả hai lăng kính EVE và NII [[src-tata-bank-alm#^tata-sot-4]].
- **Sự đánh đổi giữa NIM và Chi phí Đệm Thanh khoản (LCR / NSFR)**:
  - Để đáp ứng tỷ lệ khả năng chi trả ([[lcr]]) và tỷ lệ nguồn vốn ổn định ròng ([[nsfr]]), ngân hàng phải nắm giữ tài sản thanh khoản chất lượng cao ([[hqla]]) và phát hành trái phiếu kỳ hạn dài [[src-lubinska-alm-optimisation#^lubinska-u04-12]].
  - Đệm HQLA chủ yếu gồm trái phiếu chính phủ có lợi suất thấp hơn chi phí huy động bình quân, tạo ra chi phí gánh âm (*negative carry*) [[src-choudhry-principles-banking#^choudhry-lp-5]].
  - Việc gia tăng đệm an toàn thanh khoản trực tiếp kéo giảm NIM và tổng quy mô NII của ngân hàng [[src-choudhry-principles-banking#^choudhry-nim-5]].
- **Quy trình điều hành ALCO tích hợp**:
  - ALCO nhận báo cáo MI pack định kỳ hàng tháng tích hợp: khe hở kỳ hạn, độ nhạy NII/EaR (với hạn mức thường là $\pm 5\%$ hoặc $\pm 10\%$), mức tiêu hao đệm thanh khoản và phân rã rủi ro cơ sở [[src-choudhry-principles-banking#^choudhry-hedge-22]] [[src-choudhry-principles-banking#^choudhry-alco-18]].

## Bằng chứng ủng hộ
- Mô hình minh họa của Fidelio Tata chứng minh cụ thể bài toán tối ưu hóa tuyến tính: vùng khả thi kết hợp giữa hai điều kiện SOT EVE ($\le 15\%$ Tier 1) và SOT NII ($\le 5\%$ Tier 1) rất hẹp và dịch chuyển liên tục theo quy mô bảng cân đối [[src-tata-bank-alm#^tata-sot-4]].
- Báo cáo của Moorad Choudhry về thực tiễn quản trị tại các ngân hàng Anh chỉ ra rằng việc mảng kinh doanh huy động tiền gửi ngắn hạn để tài trợ cho tài sản dài hạn tạo ra NII tức thời cao nhưng đẩy ngân hàng vào tình trạng vi phạm hạn mức rủi ro thanh khoản và rủi ro tái định giá nghiêm trọng tại ALCO [[src-choudhry-principles-banking#^choudhry-cs-23]].
- Mô hình quy hoạch tuyến tính LPP của Irena Lubinska chứng minh việc tích hợp các ràng buộc pháp định Basel III (LCR, NSFR, Leverage Ratio, IRRBB) vào hàm mục tiêu tối đa hóa NII giúp ALCO tìm ra cơ cấu phân bổ tài sản tối ưu mà không vi phạm quy chế an toàn [[src-lubinska-alm-optimisation#^lubinska-u04-13]] [[src-lubinska-alm-optimisation#^lubinska-u05-11]].

## Bằng chứng trái chiều
- **Nghịch lý giữa EVE và Giá trị thị trường cổ phiếu ngân hàng (Moorad Choudhry)**: Về lý thuyết kinh tế, tăng EVE phản ánh giá trị nội tại dài hạn tăng; tuy nhiên, trên thị trường chứng khoán, giá cổ phiếu ngân hàng thường tương quan thuận chặt chẽ với thu nhập NII và NIM công bố hàng quý hơn là chỉ số EVE lý thuyết [[src-choudhry-principles-banking#^choudhry-nim-14]].
- **Xung đột giữa mục tiêu kinh doanh chi nhánh và Treasury**: Chi nhánh muốn tối đa hóa dư nợ cho vay và huy động tiền gửi kỳ hạn ngắn giá rẻ để đạt chỉ tiêu doanh số; hành vi này làm gia tăng rủi ro khe hở tái định giá và chi phí carry đệm thanh khoản mà Treasury phải gánh chịu [[src-choudhry-principles-banking#^choudhry-cs-1]].

## Phụ thuộc regime
- **Môi trường đường cong lãi suất đảo ngược (*Inverted yield curve*)**:
  - Lãi suất ngắn hạn cao hơn lãi suất dài hạn: chi phí huy động tăng vượt lợi suất cho vay dài hạn mới, bóp nghẹt NIM và NII của ngân hàng [[src-choudhry-principles-banking#^choudhry-nim-9]].
  - ALCO buộc phải hạn chế các hợp đồng tài trợ kỳ hạn dài cố định và gia tăng tỷ trọng tài sản lãi suất thả nổi.
- **Môi trường thanh khoản hệ thống thắt chặt tại Việt Nam**:
  - Khi lãi suất liên ngân hàng (VNIBOR) tăng đột biến trong khi trần lãi suất huy động dân cư bị khống chế hoặc tăng chậm: rủi ro cơ sở ([[basis-risk]]) giữa tài sản và nợ bộc lộ mạnh mẽ, làm suy giảm đột ngột thu nhập lãi thuần [[src-choudhry-principles-banking#^choudhry-alco-19]].
  - Ngân hàng Việt Nam chịu sự điều chỉnh của [[tt83-2025]] có hiệu lực từ ngày 01/07/2026, đòi hỏi hệ thống ALM phải tự động hóa việc tính toán cả $\Delta\text{NII}$ và $\Delta\text{EVE}$ theo danh mục tiền tệ riêng biệt [[src-tt83-2025-nhnn#^d53-1a2]] [[src-tt83-2025-nhnn#^pl5-b3]].

## Hàm ý ALM / quy định
- **Tích hợp hạn mức ALCO**: ALCO cần thiết lập hệ thống hạn mức kép kết hợp: hạn mức EaR cho NII ngắn hạn ($\pm 5\%$ đến $\pm 10\%$) và hạn mức $\Delta\text{EVE}$ dài hạn theo tỷ lệ phần trăm vốn tự có [[src-choudhry-principles-banking#^choudhry-hedge-22]].
- **Vận hành FTP đa cấu phần**: Chính sách FTP tại các ngân hàng thương mại Việt Nam cần bóc tách riêng phần bù thanh khoản kỳ hạn (TLP), chi phí gánh đệm HQLA và phụ phí cơ sở (basis spread charge) để đảm bảo phản ánh đầy đủ chi phí kinh tế vào giá sản phẩm [[src-choudhry-principles-banking#^choudhry-lp-5]].
- **Tính độc lập của bộ phận quản lý rủi ro**: Theo quy định tại Điều 54.1.b Thông tư 83/2025/TT-NHNN, bộ phận đo lường và theo dõi rủi ro lãi suất sổ ngân hàng phải hoàn toàn độc lập với các khối kinh doanh phát sinh rủi ro [[src-tt83-2025-nhnn#^d54-1b]].

## Bất định
- **Thiếu thị trường phái sinh lãi suất sâu rộng tại Việt Nam**: Dù hợp đồng hoán đổi lãi suất (IRS) là công cụ phòng ngừa NII tiêu chuẩn trong lý thuyết quốc tế, thanh khoản thị trường phái sinh lãi suất nội địa tại Việt Nam còn hạn chế; ngân hàng thương mại Việt Nam chủ yếu phải sử dụng các biện pháp phòng hộ tự nhiên (*natural hedging*) thông qua tái cơ cấu kỳ hạn trên bảng cân đối.
- **Quy chuẩn ngưỡng trừng phạt NII trong tương lai**: Hiện NHNN chưa ban hành ngưỡng định lượng cứng cho tỷ lệ sụt giảm NII (như ngưỡng 5% Tier 1 của EBA); tuy nhiên, trong quá trình thanh tra giám sát Trụ cột 2 (SREP), cơ quan thanh tra giám sát NHNN có thể đưa ra các yêu cầu bổ sung vốn nếu $\Delta\text{NII}$ sụt giảm nghiêm trọng đe dọa khả năng duy trì hoạt động bình thường [[src-bcbs-irrbb-2016#^irrbb-p12-7]] [[src-tt83-2025-nhnn#^d55-1]].
