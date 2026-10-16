---
title: "BCBS — Interest Rate Risk in the Banking Book (Standards d368)"
aliases: []
type: source
source_id: src-bcbs-irrbb-2016
domains: [basel, alm]
status: active
maturity: canonical
tier: T2
doc_status: final
issuer: BCBS
published: 2016-04-21
effective: 2018-01-01
raw: 01_sources/alm/Basel/IRRBB-d368/d368_irrbb.md
units_done: [preamble, u01, u02, u03, u04, u05, u06, u07]
updated: 2026-10-16
---

## Thông tin nguồn
- Issuer: Basel Committee on Banking Supervision ([[bcbs]])
- Tier T2, `doc_status: final`. Tiêu chuẩn ban hành tháng 04/2016 (Standards d368), thay thế Hướng dẫn IRR 2004 (*2004 Principles for the management and supervision of interest rate risk*).
- Áp dụng: Có hiệu lực từ năm 2018 (công bố thông tin năm 2018 dựa trên dữ liệu ngày 31/12/2017).
- Phạm vi: Áp dụng trên cơ sở hợp nhất cho các ngân hàng hoạt động quốc tế lớn; cơ quan giám sát quốc gia có quyền quyết định mở rộng cho các tổ chức khác.
- Raw: `01_sources/alm/Basel/IRRBB-d368/d368_irrbb.md` (1.048 dòng); meta: `d368_meta.json`.
- Conversion: ok (xem `03_meta/sources.yaml`).
- Node regulation tương ứng: [[bcbs-irrbb]].

## Tóm tắt
Chuẩn mực IRRBB 2016 (d368) thiết lập khuôn khổ toàn diện nâng cấp Trụ cột 2 (Supervisory Review Process) và Trụ cột 3 (Market Discipline) đối với rủi ro lãi suất trên sổ ngân hàng:
- **Lý do lựa chọn Trụ cột 2 nâng cao**: BCBS đã bác bỏ phương án yêu cầu vốn tối thiểu Trụ cột 1 được chuẩn hoá vì tính chất không đồng nhất (heterogeneous nature) của danh mục sổ ngân hàng giữa các tổ chức; việc áp đặt một công thức Trụ cột 1 chuẩn hoá duy nhất sẽ không đủ độ nhạy rủi ro và làm sai lệch bản chất rủi ro. Thay vào đó, BCBS chọn tiếp cận Trụ cột 2 nâng cao kèm công bố thông tin bắt buộc Trụ cột 3.
- **Hai lăng kính đo lường bổ trợ**:
  - *Giá trị kinh tế ($\Delta\text{EVE}$)*: Đo lường biến động giá trị hiện tại thuần của toàn bộ dòng tiền sổ ngân hàng trong kịch bản sốc lãi suất trên đường chân trời run-off cho đến khi tất cả các vị thế đáo hạn. Là chuẩn mực để giám sát đánh giá mức độ an toàn vốn.
  - *Thu nhập thuần từ lãi ($\Delta\text{NII}$)*: Đo lường tác động lên khả năng sinh lời trong ngắn và trung hạn (1–3 năm, chuẩn mực công bố 12 tháng) trên giả định bảng cân đối không đổi (constant) hoặc động (dynamic).
  - *Mâu thuẫn quản trị*: Ngân hàng chỉ tập trung triệt tiêu rủi ro giá trị kinh tế bằng cách khớp kỳ hạn tài sản và nợ dài hạn sẽ phải đối mặt với biến động dữ dội về thu nhập lãi.
- **Ba phân loại rủi ro lãi suất cốt lõi**:
  - *Rủi ro chênh lệch kỳ hạn (Gap risk)*: Phát sinh từ cấu trúc kỳ hạn của các công cụ sổ ngân hàng và độ lệch thời điểm tái định giá lãi suất, gồm rủi ro dịch chuyển song song (parallel) và phi song song/xoắn đường cong (non-parallel/twisting).
  - *Rủi ro cơ sở (Basis risk)*: Phát sinh từ biến động tương đối giữa các công cụ có kỳ hạn tương đương nhưng neo theo các chỉ số lãi suất cơ sở khác nhau.
  - *Rủi ro quyền chọn (Option risk)*: Gồm quyền chọn tự động (automatic options: caps, floors, swaptions) và quyền chọn hành vi (behavioural options: quyền trả nợ trước hạn của người vay, quyền rút tiền gửi có kỳ hạn trước hạn, hành vi tiền gửi không kỳ hạn NMDs).
- **Rủi ro chênh lệch tín dụng trên sổ ngân hàng (CSRBB)**: Rủi ro biến động spread của các công cụ chịu rủi ro tín dụng mà không được giải thích bởi IRRBB hay rủi ro vỡ nợ (jump-to-default risk).
- **Khuôn khổ chuẩn hoá (Standardised Framework)**: Chia dòng tiền tái định giá vào 19 dải kỳ hạn, quy định trần tỷ lệ tiền gửi lõi (core deposits) và kỳ hạn bình quân (retail transactional: 90% trần 5 năm; retail non-transactional: 70% trần 4.5 năm; wholesale: 50% trần 4 năm), bảng tra cứu hệ số nhân sốc cho tỷ lệ trả nợ trước hạn (CPR) và rút tiền gửi sớm (TDRR), đo lường quyền chọn tự động $\text{KAO}_{i,c}$.
- **Ngưỡng kiểm tra ngân hàng ngoại lai (Outlier Bank Test - Nguyên tắc 12)**: Thắt chặt ngưỡng cảnh báo từ 20% tổng vốn (chuẩn 2004) xuống **$\Delta\text{EVE} > 15\%$ Vốn cấp 1 (Tier 1 Capital)** dưới 6 kịch bản sốc lãi suất chuẩn hoá. Khi vượt ngưỡng hoặc quản trị yếu kém, cơ quan giám sát bắt buộc áp dụng các biện pháp giảm rủi ro và/hoặc yêu cầu tăng thêm vốn quy định.
- **6 kịch bản sốc lãi suất chuẩn hoá (Annex 2)**: Parallel up, Parallel down, Steepener, Flattener, Short rate up, Short rate down với các tham số sàn 100 bps và trần cụ thể (Short 500 bps, Parallel 400 bps, Long 300 bps).

## Key claims

### Preamble

- Văn bản ban hành tiêu chuẩn quản trị và giám sát rủi ro lãi suất trên sổ ngân hàng do Ủy ban Basel công bố vào tháng 04/2016.
  > "Standards April 2016 … Interest rate risk in the banking book"
  > — preamble ^irrbb-preamble

### Unit 1 — Executive summary

- IRRBB là một phần của Trụ cột 2 (Quy trình đánh giá giám sát) trong khuôn khổ vốn Basel, thay thế Hướng dẫn Nguyên tắc IRR năm 2004.
  > "Interest rate risk in the banking book (IRRBB) is part of the Basel capital framework's Pillar 2 (Supervisory Review Process) and subject to the Committee's guidance set out in the 2004 Principles for the management and supervision of interest rate risk"
  > — u01, par 1 ^irrbb-u01-1

- Ủy ban Basel kết luận tính chất không đồng nhất của IRRBB khiến nó phù hợp hơn khi được ghi nhận trong Trụ cột 2 thay vì áp dụng yêu cầu vốn tối thiểu Trụ cột 1 chuẩn hoá.
  > "The Committee noted the industry's feedback on the feasibility of a Pillar 1 approach to IRRBB, in particular the complexities involved in formulating a standardised measure of IRRBB which would be both sufficiently accurate and risk-sensitive to allow it to act as a means of setting regulatory capital requirements. The Committee concludes that the heterogeneous nature of IRRBB would be more appropriately captured in Pillar 2."
  > — u01, par 3 ^irrbb-u01-2

- Các cập nhật trọng yếu theo hướng tiếp cận Trụ cột 2 nâng cao bao gồm hướng dẫn xây dựng kịch bản sốc và căng thẳng (Nguyên tắc 4), các giả định hành vi và mô hình hoá (Nguyên tắc 5), và kiểm định độc lập hệ thống đo lường nội bộ IMS (Nguyên tắc 6).
  > "Greater guidance has been provided on the expectations for a bank's IRRBB management process, in particular the development of shock and stress scenarios (Principle 4) to be applied to the measurement of IRRBB, the key behavioural and modelling assumptions which banks should consider in their measurement of IRRBB (Principle 5) and the internal validation process which banks should apply for their internal measurement systems (IMS) and models used for IRRBB (Principle 6)."
  > — u01, par 4 ^irrbb-u01-3

- Nguyên tắc 8 yêu cầu các ngân hàng phải công bố tác động của các kịch bản sốc lãi suất lên biến động giá trị kinh tế của vốn chủ sở hữu (∆EVE) và biến động thu nhập lãi thuần (∆NII) dựa trên bộ kịch bản sốc quy định.
  > "Banks must disclose, among other requirements, the impact of interest rate shocks on their change in economic value of equity (∆EVE) and net interest income (∆NII), computed based on a set of prescribed interest rate shock scenarios."
  > — u01, par 4 ^irrbb-u01-4

- Cơ quan giám sát có thể bắt buộc các ngân hàng thuộc phạm vi quản lý phải áp dụng khuôn khổ chuẩn hoá đối với IRRBB nếu nhận thấy hệ thống đo lường nội bộ không phản ánh đầy đủ rủi ro.
  > "Supervisors could also mandate the banks under their respective jurisdictions to follow the standardised framework for IRRBB (eg if they find that the bank's IMS does not adequately capture IRRBB)."
  > — u01, par 4 ^irrbb-u01-5

- Ngưỡng xác định ngân hàng ngoại lai (outlier bank) theo Nguyên tắc 12 được thắt chặt xuống mức ∆EVE vượt quá 15% Vốn cấp 1 (Tier 1 capital) dưới các kịch bản sốc lãi suất quy định, đi kèm giả định mạnh mẽ về các chế tài giám sát hoặc yêu cầu vốn bổ sung.
  > "The threshold for the identification of an "outlier bank" has also been tightened, where the outlier/materiality test(s) applied by supervisors should at least include one which compares the bank's ∆EVE with 15% of its Tier 1 capital, under a set of prescribed interest rate shock scenarios. … There is a strong presumption for supervisory and/or regulatory capital consequences, when a review of a bank's IRRBB exposure reveals inadequate management or excessive risk relative to a bank's capital, earnings or general risk profile."
  > — u01, par 4 ^irrbb-u01-6

- Thời hạn các ngân hàng dự kiến triển khai đầy đủ tiêu chuẩn IRRBB 2016 là năm 2018 (công bố năm 2018 dựa trên dữ liệu kết thúc năm tài chính 31/12/2017).
  > "The banks are expected to implement the standards by 2018."
  > — u01, par 7 ^irrbb-u01-7

### Unit 2 — Section I: Introduction on IRRBB

- IRRBB là rủi ro hiện tại hoặc tiềm năng đối với vốn và thu nhập của ngân hàng phát sinh từ các biến động bất lợi của lãi suất tác động lên các vị thế trên sổ ngân hàng.
  > "IRRBB refers to the current or prospective risk to the bank's capital and earnings arising from adverse movements in interest rates that affect the bank's banking book positions."
  > — u02, par 8 ^irrbb-u02-1

- Ba phân loại rủi ro chính của IRRBB gồm: Rủi ro chênh lệch kỳ hạn (Gap risk), Rủi ro cơ sở (Basis risk), và Rủi ro quyền chọn (Option risk bao gồm automatic option và behavioural option).
  > "Three main sub-types of IRRBB are defined for the purposes of these Principles: (a) Gap risk arises from the term structure of banking book instruments, and describes the risk arising from the timing of instruments' rate changes. … (b) Basis risk describes the impact of relative changes in interest rates for financial instruments that have similar tenors but are priced using different interest rate indices. (c) Option risk arises from option derivative positions or from optional elements embedded in a bank's assets, liabilities and/or off-balance sheet items … Option risk can be further characterised into automatic option risk and behavioural option risk."
  > — u02, par 9 ^irrbb-u02-2

- Rủi ro chênh lệch tín dụng trên sổ ngân hàng (CSRBB) là rủi ro liên quan cần được theo dõi và đánh giá; CSRBB đề cập đến mọi loại rủi ro spread của tài sản/nợ chịu rủi ro tín dụng không được giải thích bởi IRRBB hay rủi ro tín dụng dự kiến/rủi ro vỡ nợ đột ngột (jump-to-default).
  > "CSRBB refers to any kind of asset/liability spread risk of credit-risky instruments that is not explained by IRRBB and by the expected credit/jump to default risk."
  > — u02, par 10 ^irrbb-u02-3

- Việc quản trị IRRBB đòi hỏi phải kết hợp cả hai thước đo giá trị kinh tế và thu nhập; nếu ngân hàng chỉ triệt tiêu rủi ro giá trị kinh tế bằng cách khớp kỳ hạn tái định giá tài sản và nợ ngoài kỳ hạn ngắn, ngân hàng có thể đối mặt với rủi ro biến động thu nhập nghiêm trọng.
  > "The Committee acknowledges the importance of managing IRRBB through both economic value and earnings-based measures. If a bank solely minimises its economic value risk by matching the repricing of its assets with liabilities beyond the short term, it could run the risk of earnings volatility."
  > — u02, par 11 ^irrbb-u02-4

### Unit 3 — Section II: The revised IRR Principles (Principles 1–12)

#### Nguyên tắc dành cho ngân hàng (Principles 1–9)

- **Nguyên tắc 1 (Nhận diện & Kiểm soát)**: IRRBB là rủi ro trọng yếu đối với tất cả ngân hàng, phải được nhận diện, đo lường, theo dõi và kiểm soát cụ thể; đồng thời ngân hàng phải theo dõi và đánh giá CSRBB.
  > "Principle 1: IRRBB is an important risk for all banks that must be specifically identified, measured, monitored and controlled. In addition, banks should monitor and assess CSRBB."
  > — u03, Principle 1 ^irrbb-p01-1

- **Nguyên tắc 2 (Quản trị & Giám sát của HĐQT/ALCO)**: Cơ quan quản trị cao nhất chịu trách nhiệm giám sát khung quản trị IRRBB và khẩu vị rủi ro; việc theo dõi và quản trị có thể được ủy quyền cho ban điều hành cấp cao hoặc Hội đồng Quản lý Tài sản - Nợ (ALCO); ALCO phải họp thường xuyên và có đại diện từ các khối nghiệp vụ trọng yếu.
  > "Principle 2: The governing body 5 of each bank is responsible for oversight of the IRRBB management framework, and the bank's risk appetite for IRRBB. Monitoring and management of IRRBB may be delegated by the governing body to senior management, expert individuals or an asset and liability management committee"
  > — u03, Principle 2 ^irrbb-p02-1

- Cơ quan quản trị cao nhất phải được báo cáo định kỳ (tối thiểu bán niên) về mức độ và xu hướng rủi ro IRRBB, và thường xuyên hơn khi có các vị thế rủi ro lớn hoặc phức tạp.
  > "The governing body should be informed regularly (at least semiannually) on the level and trend of the bank's IRRBB exposures."
  > — u03, par 18 ^irrbb-p02-2

- Ngân hàng phải thiết lập các chức năng nhận diện, đo lường, theo dõi và kiểm soát IRRBB độc lập đầy đủ với các bộ phận kinh doanh chấp nhận rủi ro (risk-taking functions).
  > "Banks should have IRRBB identification, measurement, monitoring and control functions with clearly defined responsibilities that are sufficiently independent from risk-taking functions of the bank and that report IRRBB exposures directly to the governing body or its delegates."
  > — u03, par 21 ^irrbb-p02-3

- **Nguyên tắc 3 (Khẩu vị rủi ro & Hạn mức)**: Khẩu vị rủi ro IRRBB phải được thể hiện qua cả rủi ro đối với giá trị kinh tế và thu nhập; các ngân hàng phải áp dụng hệ thống hạn mức chính sách nhất quán với khẩu vị rủi ro này.
  > "Principle 3: The banks' risk appetite for IRRBB should be articulated in terms of the risk to both economic value and earnings. Banks must implement policy limits that target maintaining IRRBB exposures consistent with their risk appetite."
  > — u03, Principle 3 ^irrbb-p03-1

- **Nguyên tắc 4 (Đo lường & Kịch bản sốc)**: Việc đo lường IRRBB phải dựa trên kết quả của cả hai thước đo giá trị kinh tế và thu nhập dưới một phạm vi rộng các kịch bản sốc và căng thẳng lãi suất phù hợp.
  > "Principle 4: Measurement of IRRBB should be based on outcomes of both economic value and earnings-based measures, arising from a wide and appropriate range of interest rate shock and stress scenarios."
  > — u03, Principle 4 ^irrbb-p04-1

- Thước đo giá trị kinh tế đo lường biến động giá trị hiện tại thuần trên đường chân trời run-off cho đến khi vị thế đáo hạn hết; thước đo thu nhập tập trung vào lợi nhuận trong ngắn và trung hạn và có thể sử dụng giả định bảng cân đối run-off, không đổi (constant), hoặc động (dynamic).
  > "economic value measures compute a change in the net present value of the bank's assets, liabilities and off-balance sheet items subject to specific interest rate shock and stress scenarios, while earnings-based measures focus on changes to future profitability within a given time horizon eventually affecting future levels of a bank's own equity capital"
  > — u03, par 34 ^irrbb-p04-2

- Hệ thống đo lường nội bộ (IMS) phải tính toán được tác động của nhiều kịch bản: (i) kịch bản chọn nội bộ theo ICAAP; (ii) kịch bản căng thẳng lịch sử và giả định; (iii) 6 kịch bản sốc quy định tại Annex 2; (iv) kịch bản bổ sung do cơ quan giám sát yêu cầu; đồng thời thực hiện kiểm tra căng thẳng ngược (reverse stress tests).
  > "Banks' IMS for IRRBB should be able to accommodate the calculation of the impact on economic value and earnings of multiple scenarios, based on: (i) internally selected interest rate shock scenarios … (ii) historical and hypothetical interest rate stress scenarios … (iii) the six prescribed interest rate shock scenarios set out in Annex 2; and (iv) any additional interest rate shock scenarios required by supervisors."
  > — u03, par 35 ^irrbb-p04-3

- **Nguyên tắc 5 (Giả định hành vi & Mô hình hoá)**: Các giả định hành vi trọng yếu đối với quyền chọn lãi suất, tiền gửi không kỳ hạn (NMDs), vốn chủ sở hữu và nguyên tắc kế toán phải được hiểu thấu đáo, có cơ sở lý luận vững chắc, được kiểm định nghiêm ngặt và cập nhật định kỳ (tối thiểu hàng năm).
  > "Principle 5: In measuring IRRBB, key behavioural and modelling assumptions should be fully understood, conceptually sound and documented. Such assumptions should be rigorously tested and aligned with the bank's business strategies."
  > — u03, Principle 5 ^irrbb-p05-1

- Đối với NMDs, ngân hàng phải phân tích cơ sở khách hàng để xác định tỷ lệ tiền gửi lõi (core deposits) - phần tiền gửi khó có khả năng tái định giá ngay cả khi môi trường lãi suất biến động mạnh.
  > "To determine the appropriate assumptions for its NMDs, a bank should analyse its depositor base in order to identify the proportion of core deposits (ie NMDs which are unlikely to reprice even under significant changes in interest rate environment)."
  > — u03, par 45 ^irrbb-p05-2

- Đối với các khoản cho vay lãi suất cố định chịu rủi ro trả nợ trước hạn (prepayment) và tiền gửi có kỳ hạn chịu rủi ro rút trước hạn (early redemption), ngân hàng phải ước tính cẩn trọng tốc độ trả nợ trước hạn và tỷ lệ rút vốn sớm theo từng kịch bản sốc lãi suất.
  > "Banks should understand the nature of prepayment risk for their portfolios and make reasonable and prudent estimates of the expected prepayments. … Specifically, a bank must assess the expected average prepayment speed under each scenario."
  > — u03, par 45 ^irrbb-p05-3

- **Nguyên tắc 6 (Hệ thống dữ liệu & Quản trị mô hình độc lập)**: Hệ thống đo lường và các mô hình sử dụng cho IRRBB phải dựa trên dữ liệu chính xác, được văn bản hoá và kiểm soát chặt chẽ; khung quản trị rủi ro mô hình phải bao gồm chức năng kiểm định độc lập (independent validation) với quá trình phát triển mô hình.
  > "Principle 6: Measurement systems and models used for IRRBB should be based on accurate data, and subject to appropriate documentation, testing and controls to give assurance on the accuracy of calculations. Models used to measure IRRBB should be comprehensive and covered by governance processes for model risk management, including a validation function that is independent of the development process."
  > — u03, Principle 6 ^irrbb-p06-1

- Khung kiểm định độc lập hiệu quả phải bao gồm 3 cấu phần cốt lõi: (1) Đánh giá tính vững chắc về phương pháp luận và lý luận; (2) Giám sát mô hình liên tục và benchmarking; (3) Phân tích kết quả thực tế (outcomes analysis) bao gồm kiểm định ngược (backtesting) các tham số nội bộ chính.
  > "An effective validation framework should include three core elements: evaluation of conceptual/methodological soundness, including developmental evidence; ongoing model monitoring, including process verification and benchmarking; and outcomes analysis, including backtesting of key internal parameters (eg stability of deposits, prepayments, early redemptions, pricing of instruments)."
  > — u03, par 59 ^irrbb-p06-2

- Kiểm toán nội bộ phải rà soát quy trình quản trị rủi ro mô hình như một phần của kế hoạch đánh giá rủi ro và kiểm toán hàng năm.
  > "Internal audit should review the model risk management process as part of its annual risk assessment and audit plans."
  > — u03, par 65 ^irrbb-p06-3

- **Nguyên tắc 7 (Báo cáo định kỳ cho HĐQT/ALCO)**: Kết quả đo lường IRRBB và chiến lược phòng ngừa rủi ro phải được báo cáo thường xuyên cho cơ quan quản trị hoặc các đại diện được ủy quyền (ALCO) ở các cấp độ tổng hợp phù hợp (theo cấp hợp nhất và từng loại tiền tệ).
  > "Principle 7: Measurement outcomes of IRRBB and hedging strategies should be reported to the governing body or its delegates on a regular basis, at relevant levels of aggregation (by consolidation level and currency)."
  > — u03, Principle 7 ^irrbb-p07-1

- **Nguyên tắc 8 (Công bố thông tin Trụ cột 3)**: Thông tin về mức độ rủi ro IRRBB và các thực hành đo lường, kiểm soát phải được công bố công khai định kỳ hàng năm theo mẫu Bảng A (định tính) và Bảng B (định lượng: ∆EVE và ∆NII dưới 6 kịch bản sốc lãi suất).
  > "Principle 8: Information on the level of IRRBB exposure and practices for measuring and controlling IRRBB must be disclosed to the public on a regular basis. … The level of IRRBB exposure should be measured and disclosed. Specifically, banks must disclose the measured ∆EVE and ∆NII under the prescribed interest rate shock scenarios set out in Annex 2."
  > — u03, Principle 8 & par 69 ^irrbb-p08-1

- Nguyên tắc đồng nhất khi tính toán ∆EVE công bố: Loại bỏ vốn chủ sở hữu khỏi tính toán mức độ phơi lượng; bao gồm tất cả dòng tiền từ tài sản nhạy cảm lãi suất, nợ và ngoại bảng; chiết khấu theo lãi suất phi rủi ro (hoặc lãi suất phi rủi ro cộng biên thương mại nếu dòng tiền đã bao gồm biên này); áp dụng giả định bảng cân đối run-off.
  > "∆EVE (a) Banks should exclude their own equity from the computation of the exposure level. (b) Banks should include all cash flows from all interest rate-sensitive assets, 11 liabilities and off-balance sheet items in the banking book in the computation of their exposure. … (c) Cash flows should be discounted using either a risk-free rate 12 or a risk-free rate including commercial margins and other spread components … (d) ∆EVE should be computed with the assumption of a run-off balance sheet"
  > — u03, par 70 ^irrbb-p08-2

- Nguyên tắc tính toán ∆NII công bố: Bao gồm các dòng tiền dự kiến (gồm cả biên thương mại và spread); tính toán trên giả định bảng cân đối không đổi (constant balance sheet); thời gian tính toán là chênh lệch thu nhập lãi trong giai đoạn 12 tháng liên tục (rolling 12-month period).
  > "∆NII (a) Banks should include expected cash flows (including commercial margins and other spread components) arising from all interest rate-sensitive assets, liabilities and offbalance sheet items in the banking book. (b) ∆NII should be computed assuming a constant balance sheet, where maturing or repricing cash flows are replaced by new cash flows with identical features with regard to the amount, repricing period and spread components. (c) ∆NII should be disclosed as the difference in future interest income over a rolling 12-month period."
  > — u03, par 70 ^irrbb-p08-3

- **Nguyên tắc 9 (Đánh giá an toàn vốn nội bộ - ICAAP)**: Mức độ đủ vốn đối với IRRBB phải được xem xét cụ thể trong quy trình ICAAP được cơ quan quản trị phê duyệt, phù hợp với khẩu vị rủi ro IRRBB của ngân hàng.
  > "Principle 9: Capital adequacy for IRRBB must be specifically considered as part of the Internal Capital Adequacy Assessment Process (ICAAP) approved by the governing body, in line with the bank's risk appetite on IRRBB."
  > — u03, Principle 9 ^irrbb-p09-1

- Mức độ đủ vốn đối với IRRBB phải được xem xét liên quan đến các rủi ro giá trị kinh tế (rủi ro tiềm ẩn trong tài sản, nợ và ngoại bảng); đối với rủi ro thu nhập tương lai, ngân hàng nên xem xét các bộ đệm vốn (capital buffers).
  > "Capital adequacy for IRBBB should be considered in relation to the risks to economic value, given that such risks are embedded in the bank's assets, liabilities and off-balance sheet items. For risks to future earnings, given the possibility that future earnings may be lower than expected, banks should consider capital buffers."
  > — u03, par 74 ^irrbb-p09-2

#### Nguyên tắc dành cho cơ quan giám sát (Principles 10–12)

- **Nguyên tắc 10 (Thu thập thông tin giám sát)**: Cơ quan giám sát phải thu thập thông tin định kỳ từ các ngân hàng để theo dõi xu hướng phơi lượng IRRBB, đánh giá sự lành mạnh trong quản trị IRRBB và xác định các ngân hàng ngoại lai (outlier banks).
  > "Principle 10: Supervisors should, on a regular basis, collect sufficient information from banks to be able to monitor trends in banks' IRRBB exposures, assess the soundness of banks' IRRBB management and identify outlier banks that should be subject to review and/or should be expected to hold additional regulatory capital."
  > — u03, Principle 10 ^irrbb-p10-1

- **Nguyên tắc 11 (Quy trình đánh giá giám sát chuyên sâu)**: Cơ quan giám sát phải thường xuyên đánh giá hiệu quả của hệ thống nhận diện, đo lường, theo dõi và kiểm soát IRRBB của ngân hàng; sử dụng các chuyên gia chuyên trách và hợp tác chia sẻ thông tin xuyên biên giới.
  > "Principle 11: Supervisors should regularly assess banks' IRRBB and the effectiveness of the approaches that banks use to identify, measure, monitor and control IRRBB. Supervisory authorities should employ specialist resources to assist with such assessments. Supervisors should cooperate and share information with relevant supervisors in other jurisdictions regarding the supervision of banks' IRRBB exposures."
  > — u03, Principle 11 ^irrbb-p11-1

- Khi hệ thống IMS của ngân hàng bị cơ quan giám sát xác định là khiếm khuyết trong việc đo lường IRRBB, cơ quan giám sát phải yêu cầu ngân hàng cải thiện IMS và/hoặc áp dụng khuôn khổ chuẩn hoá (Section IV) để tính toán ∆EVE.
  > "When a supervisor determines that a bank's IMS is deficient in its measurement of IRRBB, the supervisor should require the bank to improve its IMS and/or use the standardised framework set out in Section IV to compute its IRRBB in terms of ∆EVE."
  > — u03, par 92 ^irrbb-p11-2

- **Nguyên tắc 12 (Ngân hàng ngoại lai & Biện pháp can thiệp giám sát)**: Cơ quan giám sát phải công bố tiêu chí xác định ngân hàng ngoại lai; phép thử ngoại lai/trọng yếu tối thiểu phải so sánh mức giảm giá trị kinh tế cực đại (maximum ∆EVE) dưới 6 kịch bản sốc lãi suất với **15% Vốn cấp 1 (Tier 1 capital)**.
  > "Principle 12: Supervisors must publish their criteria for identifying outlier banks. Banks identified as outliers must be considered as potentially having undue IRRBB. When a review of a bank's IRRBB exposure reveals inadequate management or excessive risk relative to capital, earnings or general risk profile, supervisors must require mitigation actions and/or additional capital. … The supervisor should implement at least one outlier/materiality test that compares the bank's maximum ∆EVE, under the six prescribed interest rate shock scenarios set out in Annex 2, with 15% of its Tier 1 capital"
  > — u03, Principle 12 & par 88 ^irrbb-p12-1

- Cơ quan giám sát có thể áp dụng các bài kiểm tra ngoại lai bổ sung (dựa trên vốn CET1 hoặc rủi ro thu nhập ∆NII) nhưng ngưỡng xác định không được lỏng hơn 15% Vốn cấp 1.
  > "Supervisors may also implement additional outlier/materiality tests … For the additional outlier/materiality tests, the threshold for defining an outlier bank should be at least as stringent as 15% of Tier 1 capital."
  > — u03, par 89 ^irrbb-p12-2

- Khi phát hiện ngân hàng quản trị không đầy đủ hoặc có rủi ro quá mức, cơ quan giám sát phải yêu cầu ngân hàng thực hiện một hoặc nhiều biện pháp can thiệp: giảm phơi lượng rủi ro (ví dụ phòng ngừa rủi ro), tăng thêm vốn quy định, đặt ràng buộc lên các tham số nội bộ, và/hoặc cải thiện khuôn khổ quản trị rủi ro trong một thời hạn xác định.
  > "When a national supervisor concludes that a bank's management of IRRBB is inadequate or that it has excessive risk relative to its capital or earnings, or its general risk profile, the supervisor must require the bank to take one or more of the following actions: reduce its IRRBB exposures (eg by hedging); raise additional capital; set constraints on the internal risk parameters used by a bank; and/or improve its risk management framework."
  > — u03, par 94 ^irrbb-p12-3

### Unit 4 — Section III: Scope of application and implementation timeline

- Khuôn khổ IRRBB áp dụng trên cơ sở hợp nhất cho tất cả các ngân hàng hoạt động quốc tế lớn, và có thể mở rộng cho các tổ chức khác theo quyền quyết định quốc gia.
  > "The framework should be applied to all large internationally active banks on a consolidated basis, but may also be used for other banks and on any subset of entities of internationally active banks, so as to ensure greater consistency and a level playing field between domestic and cross-border banks."
  > — u04, par 96 ^irrbb-u04-1

- Các ngân hàng phải thực thi tiêu chuẩn trước năm 2018 (đối với ngân hàng có năm tài chính kết thúc vào ngày 31 tháng 12, công bố thông tin bắt đầu từ năm 2018 trên số liệu ngày 31/12/2017).
  > "The banks are expected to implement the standards by 2018. Banks whose financial year ends on 31 December would have to provide the disclosure in 2018, based on information as of 31 December 2017."
  > — u04, par 98 ^irrbb-u04-2

### Unit 5 — Section IV: The standardised framework

- Cấu trúc 5 giai đoạn của khuôn khổ chuẩn hoá để đo lường ∆EVE: (1) Phân loại vị thế (có thể chuẩn hoá, ít có khả năng chuẩn hoá, không thể chuẩn hoá); (2) Phân bổ dòng tiền vào các dải kỳ hạn; (3) Xác định ∆EVE theo từng kịch bản sốc lãi suất và loại tiền tệ; (4) Tính giá trị gia tăng đối với quyền chọn lãi suất tự động ($\text{KAO}$ add-on); (5) Tổng hợp tổn thất EVE cực đại qua 6 kịch bản sốc.
  > "The steps involved in measuring a bank's IRRBB, based solely on EVE, are: … Interest rate-sensitive banking book positions are allocated to one of three categories … Determination of slotting of cash flows based on repricing maturities. … Determination of ∆EVE for relevant interest rate shock scenarios for each currency. … Add-ons for changes in the value of automatic interest rate options … The ∆EVE under the standardised framework will be the maximum of the worst aggregated reductions to EVE across the six supervisory prescribed interest rate shocks."
  > — u05, par 100 ^irrbb-u05-1

- Tất cả dòng tiền tái định giá ước tính từ tài sản nhạy cảm lãi suất, nợ (trừ CET1) và ngoại bảng được phân bổ vào 19 dải kỳ hạn chuẩn hoá (hoặc điểm giữa của 19 dải kỳ hạn).
  > "Banks must project all future notional repricing cash flows arising from interest rate-sensitive: assets … liabilities … off-balance sheet items; onto (i) 19 predefined time buckets … or onto (ii) the time bucket midpoints as set out in Table 1"
  > — u05, par 101 ^irrbb-u05-2

- Đối với các vị thế có quyền chọn lãi suất tự động nhúng (như trần cap hoặc sàn floor trong khoản vay lãi suất thả nổi), quyền chọn phải được bóc tách khỏi dòng tiền để xử lý riêng tại Giai đoạn 4, dòng tiền cơ sở được phân bổ như khoản vay thông thường.
  > "For positions with embedded automatic interest rate options, the optionality should be ignored for the purpose of slotting of notional repricing cash flows."
  > — u05, par 100 & par 107 ^irrbb-u05-3

- Tiền gửi không kỳ hạn (NMDs) được phân loại thành Bán lẻ (giao dịch / phi giao dịch) và Bán buôn; quy định trần tỷ lệ tiền gửi lõi (core deposits) và trần kỳ hạn bình quân:
  - Bán lẻ - Tài khoản giao dịch: Trần tiền gửi lõi 90%, trần kỳ hạn bình quân 5 năm.
  - Bán lẻ - Tài khoản phi giao dịch: Trần tiền gửi lõi 70%, trần kỳ hạn bình quân 4,5 năm.
  - Bán buôn: Trần tiền gửi lõi 50%, trần kỳ hạn bình quân 4 năm.
  - Phần tiền gửi phi lõi (non-core deposits) bắt buộc phải phân bổ vào dải kỳ hạn qua đêm (overnight / dải kỳ hạn ngắn nhất).
  > "Noncore deposits should be considered as overnight deposits and accordingly should be placed into the shortest/overnight time bucket or time bucket midpoint. … Banks should determine an appropriate cash flow slotting procedure for each category of core deposits, up to the maximum average maturity per category as specified in Table 2. … Table 2. Caps on core deposits and average maturity by category"
  > — u05, par 114, 115 & Table 2 ^irrbb-u05-4

- Tỷ lệ trả nợ trước hạn có điều kiện (CPR) đối với các khoản cho vay lãi suất cố định chịu rủi ro trả trước được điều chỉnh theo hệ số nhân kịch bản $\gamma_i$: $\text{CPR}_{i,c}^p = \min(1, \gamma_i \cdot \text{CPR}_{0,c}^p)$; hệ số $\gamma_i$ là 0.8 trong kịch bản lãi suất tăng (Parallel up, Steepener, Short rate up) và 1.2 trong kịch bản lãi suất giảm (Parallel down, Flattener, Short rate down).
  > "Prepayment speeds vary according to the interest rate shock scenario. The multipliers … reflect the expectation that prepayments will generally be higher during periods of falling interest rates and lower during periods of rising interest rates."
  > — u05, par 123 ^irrbb-u05-5

- Tỷ lệ rút tiền gửi có kỳ hạn trước hạn (TDRR) được điều chỉnh theo hệ số co giãn $u_i$: $\text{TDRR}_{i,c}^p = \min(1, u_i \cdot \text{TDRR}_{0,c}^p)$; hệ số $u_i$ là 1.2 khi lãi suất tăng (Parallel up, Flattener, Short rate up - người gửi tiền rút vốn để tìm kiếm lãi suất cao hơn) và 0.8 khi lãi suất giảm.
  > "The term deposit redemption ratio for time bucket k or time bucket midpoint … applicable to each homogeneous portfolio p of term deposits in currency c and under scenario i is obtained by multiplying … that depends on the scenario i"
  > — u05, par 128 ^irrbb-u05-6

- Rủi ro quyền chọn lãi suất tự động ($\text{KAO}_{i,c}$) được tính bằng biến động giá trị của các quyền chọn bán trừ biến động giá trị của quyền chọn mua dùng để phòng ngừa rủi ro dưới kịch bản sốc kết hợp với mức tăng độ biến động ngầm định 25%.
  > "For each sold automatic option o in currency c, the value change … is calculated for each interest rate shock scenario i. … a relative increase in the implicit volatility of 25%"
  > — u05, par 130 ^irrbb-u05-7

- Thước đo rủi ro EVE chuẩn hoá tổng thể được xác định bằng tổn thất lớn nhất trong số 6 kịch bản sốc lãi suất quy định sau khi cộng dồn các khoản lỗ EVE dương giữa các loại tiền tệ trọng yếu (chiếm trên 5% tài sản hoặc nợ sổ ngân hàng).
  > "The ∆EVE under the standardised framework will be the maximum of the worst aggregated reductions to EVE across the six supervisory prescribed interest rate shocks. … Finally, the EVE losses … are aggregated under a given interest rate shock scenario i and the maximum loss across all interest rate shock scenarios is the EVE risk measure."
  > — u05, par 100 & par 132 ^irrbb-u05-8

### Unit 6 — Annex 1: Interest rate risk and its measurement techniques

- Kế toán và IRRBB: Các công cụ ghi nhận theo giá trị phân bổ (amortised cost) không phản ánh ngay biến động giá trị thị trường vào báo cáo lãi/lỗ kế toán nhưng vẫn chịu rủi ro kinh tế; ngược lại, các tài sản ghi nhận theo giá trị hợp lý (fair value / mark-to-market như AFS/FVTOCI) chịu biến động trực tiếp lên P&L hoặc vốn tự có khi lãi suất thay đổi.
  > "Since most IRRBB economic value measures aim to estimate the change in economic value under shocks and stresses, the presence or absence of higher/lower accounting values for amortised cost instruments is effectively ignored … Conversely, for assets held at fair value/mark-to-market, changes in interest rates directly affect current accounting values, and thus have an immediate impact on both P&L and available capital."
  > — u06, par 1.2 ^irrbb-u06-1

- Năm thành phần cấu thành lãi suất: (1) Lãi suất phi rủi ro (risk-free rate); (2) Spread thời lượng thị trường (market duration spread); (3) Spread thanh khoản thị trường (market liquidity spread); (4) Spread tín dụng thị trường chung (general market credit spread); (5) Spread tín dụng đặc thù (idiosyncratic credit spread).
  > "Theoretically, all rates contain five elements: 1. The risk-free rate … 2. A market duration spread … 3. A market liquidity spread … 4. A general market credit spread … 5. Idiosyncratic credit spread"
  > — u06, par 1.3 ^irrbb-u06-2

- Phân định ranh giới giữa IRRBB và CSRBB: Các biến động của lãi suất phi rủi ro, spread thời lượng thị trường, lãi suất tham chiếu và biên tài trợ thuộc phạm vi định nghĩa IRRBB; trong khi các biến động của spread thanh khoản thị trường và spread tín dụng thị trường chung được tích hợp trong định nghĩa CSRBB.
  > "Changes to the risk-free rate, market duration spread, reference rate and funding margin all fall within the definition of IRRBB. Changes to the market liquidity spreads and market credit spreads are combined within the definition of CSRBB."
  > — u06, par 1.3 ^irrbb-u06-3

- Rủi ro chênh lệch kỳ hạn (Gap risk) xuất hiện do tái định giá tài sản và nợ lệch nhau; rủi ro cơ sở (Basis risk) phát sinh do sự tương quan không hoàn hảo giữa các chỉ số lãi suất tham chiếu khác nhau; rủi ro quyền chọn (Option risk) gồm quyền chọn tự động và quyền chọn hành vi.
  > "Gap risk arises from the term structure of banking book instruments, and describes the risk arising from the timing of instrument rate changes. … Basis risk describes the impact of relative changes in interest rates for financial instruments that have similar tenors but are priced using different interest rate indices (bases) … Option risk arises from option derivative positions or from the optional elements embedded in many bank assets, liabilities and off-balance sheet items"
  > — u06, par 1.5 ^irrbb-u06-4

- So sánh giữa thước đo Giá trị kinh tế (EV/EVE) và thước đo Thu nhập (Earnings-based / NII):
  - Giá trị kinh tế đo lường sự thay đổi giá trị hiện tại thuần của các tài sản và nợ trên bảng cân đối hiện hữu cho đến khi chạy hết dòng tiền (run-off horizon), không tính vốn chủ sở hữu trong EVE;
  - Thước đo thu nhập đo lường biến động thu nhập lãi thuần NII trong chân trời ngắn-trung hạn (1–3 năm) và có thể sử dụng giả định bảng cân đối run-off, không đổi (constant), hoặc động (dynamic);
  - Cả hai phương pháp mang tính bổ trợ và không thể triệt tiêu đồng thời cả hai rủi ro mà không có sự đánh đổi (trade-off).
  > "EV measures reflect changes in value relative to equity over the remaining life of the balance sheet, ie until all positions have run off. Earnings-based measures cover only the short to medium term, and therefore do not capture in full those risks that will continue to impact profit and loss accounts beyond the period of estimation."
  > — u06, par 2.1 ^irrbb-u06-5

- Danh mục tái lập (Replicating portfolio) là kỹ thuật phổ biến để quản lý rủi ro biến động thu nhập từ nguồn vốn tiền gửi không kỳ hạn và vốn chủ sở hữu bằng cách tạo ra một danh mục tài sản sinh lời có kỳ hạn bình quân cố định (ví dụ tái đầu tư 1/60 mỗi tháng trong 5 năm để đạt thời lượng bình quân 2,5 năm).
  > "One common technique for achieving a constant maturity profile is a replicating portfolio of matching assets that produces a moving average fixed return in line with the risk appetite (eg a portfolio where one sixtieth of the total is reinvested each month for five years fixed will deliver a weighted average maturity of 2.5 years and a moving average of the five-year rate)."
  > — u06, footnote 38 ^irrbb-u06-6

- Các kỹ thuật định lượng rủi ro giá trị kinh tế: Phân tích khoảng cách định giá (Gap analysis / PV01), Giá trị kinh tế của vốn chủ sở hữu (EVE), và Giá trị kinh tế chịu rủi ro (EVaR). EVaR có hạn chế lớn là được thiết kế cho điều kiện thị trường bình thường và không đánh giá đầy đủ rủi ro đuôi (tail risk).
  > "EVaR is designed for normal market circumstances and does not adequately assess tail risk. Both historical VaR and variance-covariance VaR are backward-looking methods which are prone to missing the tail events that carry significant risks."
  > — u06, par 4.2 ^irrbb-u06-7

### Unit 7 — Annex 2: The standardised interest rate shock scenarios

- Sáu kịch bản sốc lãi suất chuẩn hoá áp dụng cho EVE gồm: (1) Dịch chuyển song song tăng (parallel shock up); (2) Dịch chuyển song song giảm (parallel shock down); (3) Đường cong dốc lên (steepener shock: ngắn hạn giảm, dài hạn tăng); (4) Đường cong phẳng đi (flattener shock: ngắn hạn tăng, dài hạn giảm); (5) Lãi suất ngắn hạn tăng (short rates shock up); (6) Lãi suất ngắn hạn giảm (short rates shock down). Hai kịch bản sốc song song được dùng cho NII.
  > "Banks should apply six prescribed interest rate shock scenarios to capture parallel and non-parallel gap risks for EVE and two prescribed interest rate shock scenarios for NII. … (i) parallel shock up; (ii) parallel shock down; (iii) steepener shock (short rates down and long rates up); (iv) flattener shock (short rates up and long rates down); (v) short rates shock up; and (vi) short rates shock down"
  > — u07, lines 930-940 ^irrbb-u07-1

- Biên độ sốc lãi suất quy định theo loại tiền tệ (Table 1): Sốc lãi suất được thiết lập riêng cho từng đồng tiền dựa trên chuỗi số liệu lịch sử 16 năm (2000–2015).
  > "These scenarios are applied to IRRBB exposures in each currency for which the bank has material positions. In order to accommodate heterogeneous economic environments across jurisdictions, the six shock scenarios reflect … absolute shocks as specified in Table 1 below."
  > — u07, lines 930-931 ^irrbb-u07-2

- Công thức sốc xoay trục đường cong (Rotation shocks: Steepener và Flattener):
  $$\Delta R_{\text{steepener},c}(t_k) = -0.65 \cdot |\Delta R_{\text{short},c}(t_k)| + 0.9 \cdot |\Delta R_{\text{long},c}(t_k)|$$
  $$\Delta R_{\text{flattener},c}(t_k) = +0.8 \cdot |\Delta R_{\text{short},c}(t_k)| - 0.6 \cdot |\Delta R_{\text{long},c}(t_k)|$$
  Hàm suy giảm của sốc ngắn hạn là $S_{\text{short}}(t_k) = e^{-t_k / x}$ với tham số $x=4$.
  > "Rotation shocks for currency c: involving rotations to the term structure (ie steepeners and flatteners) of the interest rates … The value of x in the denominator … controls the rate of decay of the shock. This should be set to the value of 4 for most currencies and the related shocks unless otherwise determined by national supervisors."
  > — u07, lines 973 & 989 ^irrbb-u07-3

- Hiệu chỉnh biên độ sốc: Thiết lập sàn tối thiểu 100 bps và trần tối đa cho các kịch bản: trần 500 bps cho lãi suất ngắn hạn, 400 bps cho dịch chuyển song song, và 300 bps cho lãi suất dài hạn; cơ quan giám sát quốc gia có quyền quyết định áp dụng mức sàn không âm hoặc sàn âm cho lãi suất sau sốc.
  > "In order to ensure a minimum level of prudence and a level playing field, a floor of 100 bp and variable caps … are set for the scenarios concerned, those caps being 500 bp for the short-term, 400 bp for the parallel and 300 bp for the long-term interest rate shock scenario. Supervisors may, applying national discretion, set a higher floor under the local interest rate shock scenarios for their home currency."
  > — u07, lines 1034-1048 ^irrbb-u07-4
