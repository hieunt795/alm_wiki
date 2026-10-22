---
title: "BCBS — Interest Rate Risk in the Banking Book (Standards d368)"
aliases: []
type: source
source_id: src-bcbs-irrbb-2016
domains: [basel, alm]
status: active
maturity: draft
tier: T2
doc_status: final
issuer: BCBS
published: 2016-04-21
effective: 2018-01-01
raw: 01_sources/alm/Basel/IRRBB-d368/d368_irrbb.md
units_done: [preamble, u01, u02, u03, u04, u05, u06, u07]
updated: 2026-10-22
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

- Ngân hàng nên có risk appetite statement được governing body phê duyệt và thực thi qua risk appetite framework (chính sách, thủ tục giới hạn và kiểm soát IRRBB). Mọi chính sách IRRBB nên được rà soát định kỳ, tối thiểu hằng năm.
  > "Banks should have clearly defined risk appetite statements6 that are approved by the governing body and implemented through comprehensive risk appetite frameworks, ie policies and procedures for limiting and controlling IRRBB."
  > "All IRRBB policies should be reviewed periodically (at least annually) and revised as needed."
  > — u03, par 28 ^irrbb-p03-2

- Policy limits do governing body đặt nên nhất quán với cách ngân hàng đo IRRBB. Hạn mức tổng (aggregate risk limits) nên áp dụng trên cơ sở hợp nhất và, khi phù hợp, ở từng công ty con. Hạn mức có thể gắn với kịch bản thay đổi lãi suất hoặc cấu trúc kỳ hạn cụ thể.
  > "Policy limits set by the governing bodies should be consistent with the bank's overall approach for measuring IRRBB. Aggregate risk limits, clearly articulating the amount of IRRBB acceptable to the governing body, should be applied on a consolidated basis and, as appropriate, at the level of individual affiliates. Limits may be associated with specific scenarios of changes in interest rates and/or term structures, such as an increase or decrease of a particular size or a change in shape."
  > — u03, par 29 ^irrbb-p03-3

- Policy limits nên phù hợp với bản chất, quy mô, độ phức tạp, mức đủ vốn và năng lực đo lường của ngân hàng. Tuỳ mô hình kinh doanh, có thể đặt hạn mức con (sub-limits) cho từng đơn vị kinh doanh, danh mục, loại công cụ hoặc công cụ cụ thể. Ngân hàng có phơi nhiễm đáng kể với gap risk, basis risk hoặc vị thế có quyền chọn hiện hoặc ẩn nên đặt risk tolerance riêng cho các rủi ro này.
  > "Policy limits should be appropriate to the nature, size, complexity and capital adequacy of the bank, as well as its ability to measure and manage its risks. Depending on the nature of a bank's activities and business model, sub-limits may also be identified for individual business units, portfolios, instrument types or specific instruments."
  > "Banks with significant exposures to gap risk, basis risk or positions with explicit or embedded options should establish risk tolerances appropriate for these risks."
  > — u03, par 30 ^irrbb-p03-5

- Governing body hoặc người được uỷ quyền nên phê duyệt trước các sáng kiến phòng ngừa hoặc chấp nhận rủi ro lớn. Nên có bộ hạn mức riêng để theo dõi chiến lược phòng ngừa dùng công cụ như phái sinh và kiểm soát rủi ro mark-to-market của công cụ hạch toán theo giá trị thị trường. Đề xuất dùng loại công cụ hoặc chiến lược mới (kể cả phòng ngừa) nên được đánh giá về nguồn lực, sự phù hợp với risk appetite và quy trình nhận diện, đo lường, theo dõi, kiểm soát rủi ro.
  > "The governing body or its delegates should approve major hedging or risk-taking initiatives in advance of implementation."
  > "A dedicated set of risk limits should be developed to monitor the evolution of hedging strategies that rely on instruments such as derivatives, and to control mark-to-market risks in instruments that are accounted for at market value. Proposals to use new instrument types or new strategies (including hedging) should be assessed to ensure that the resources required to establish sound and effective IRRBB management of the product or activity have been identified, that the proposed activities are in line with the bank's overall risk appetite, and procedures to identify, measure, monitor and control the risks of the proposed product or activity have been established."
  > — u03, par 31 ^irrbb-p03-6

- Nên có hệ thống bảo đảm vị thế vượt hoặc có khả năng vượt hạn mức được ban điều hành xử lý kịp thời và báo cáo lên ngay; nên có chính sách rõ về người được thông báo, cách thông báo và hành động khi có ngoại lệ.
  > "There should be systems in place to ensure that positions that exceed, or are likely to exceed, limits defined by the governing body or its delegates should receive prompt management attention and be escalated without delay. There should be a clear policy on who will be informed, how the communication will take place and the actions which will be taken in response to an exception."
  > — u03, par 32 ^irrbb-p03-4

- **Nguyên tắc 4 (Đo lường & Kịch bản sốc)**: Việc đo lường IRRBB phải dựa trên kết quả của cả hai thước đo giá trị kinh tế và thu nhập dưới một phạm vi rộng các kịch bản sốc và căng thẳng lãi suất phù hợp.
  > "Principle 4: Measurement of IRRBB should be based on outcomes of both economic value and earnings-based measures, arising from a wide and appropriate range of interest rate shock and stress scenarios."
  > — u03, Principle 4 ^irrbb-p04-1

- Thước đo giá trị kinh tế đo lường biến động giá trị hiện tại thuần trên đường chân trời run-off cho đến khi vị thế đáo hạn hết; thước đo thu nhập tập trung vào lợi nhuận trong ngắn và trung hạn và có thể sử dụng giả định bảng cân đối run-off, không đổi (constant), hoặc động (dynamic).
  > "economic value measures compute a change in the net present value of the bank's assets, liabilities and off-balance sheet items subject to specific interest rate shock and stress scenarios, while earnings-based measures focus on changes to future profitability within a given time horizon eventually affecting future levels of a bank's own equity capital"
  > — u03, par 34 ^irrbb-p04-2

- Thước đo thu nhập, ngoài góc nhìn run-off, có thể giả định tái tục khoản đáo hạn (constant balance sheet) và/hoặc đánh giá tác động nhất quán với kịch bản lên thu nhập tương lai kể cả kinh doanh mới (dynamic view). Footnote 9: dynamic view có thể hữu ích cho lập kế hoạch kinh doanh và ngân sách, nhưng phụ thuộc biến số và giả định cực khó dự báo chính xác trong thời gian dài và có thể che giấu rủi ro nền tảng.
  > "Earnings measures may, in addition to a run-off view, assume rollover of maturing items (ie a constant balance sheet view) and/or assess the scenario-consistent impact on the bank's future earnings inclusive of future business (ie a dynamic view)."
  > "A dynamic view can be useful for business planning and budgeting purposes. However, dynamic approaches are dependent on key variables and assumptions that are extremely difficult to project with accuracy over an extended period and can potentially hide certain key underlying risk exposures."
  > — u03, par 34 & footnote 9 ^irrbb-p04-4

- Hệ thống đo lường nội bộ (IMS) phải tính toán được tác động của nhiều kịch bản: (i) kịch bản chọn nội bộ theo ICAAP; (ii) kịch bản căng thẳng lịch sử và giả định; (iii) 6 kịch bản sốc quy định tại Annex 2; (iv) kịch bản bổ sung do cơ quan giám sát yêu cầu.
  > "Banks' IMS for IRRBB should be able to accommodate the calculation of the impact on economic value and earnings of multiple scenarios, based on: (i) internally selected interest rate shock scenarios … (ii) historical and hypothetical interest rate stress scenarios … (iii) the six prescribed interest rate shock scenarios set out in Annex 2; and (iv) any additional interest rate shock scenarios required by supervisors."
  > — u03, par 35 ^irrbb-p04-3

- Ngân hàng nên đo mức dễ tổn thất trong điều kiện thị trường căng thẳng, kể cả khi giả định then chốt đổ vỡ, và xem xét kết quả khi thiết lập, rà soát chính sách và hạn mức IRRBB.
  > "Banks should measure their vulnerability to loss under stressful market conditions including the breakdown of key assumptions"
  > "and consider those results when establishing and reviewing their policies and limits for IRRBB."
  > — u03, par 36 ^irrbb-p04-5

- Ngân hàng nên xây dựng khung stress testing IRRBB trong quy trình quản trị rủi ro rộng hơn, làm đầu vào cho quyết định chiến lược (kế hoạch kinh doanh, kế hoạch vốn); stress testing IRRBB nên được xem xét trong ICAAP, gồm stress test forward-looking nhận diện biến động thị trường nghiêm trọng có thể tác động bất lợi tới vốn hoặc thu nhập, có thể qua thay đổi hành vi khách hàng.
  > "A bank should develop and implement an effective stress testing framework for IRRBB as part of its broader risk management and governance processes. This should feed into the decision-making process at the appropriate management level, including strategic decisions (eg business and capital planning decisions) of the governing body or its delegates. In particular, IRRBB stress testing should be considered in the ICAAP, requiring banks to undertake rigorous, forward-looking stress testing that identifies events of severe changes in market conditions which could adversely impact the bank's capital or earnings, possibly also through changes in the behaviour of its customer base."
  > — u03, par 37 ^irrbb-p04-6

- Khung stress testing IRRBB nên tương xứng với bản chất, quy mô, độ phức tạp và hồ sơ rủi ro; gồm mục tiêu rõ ràng, kịch bản phù hợp hoạt động và rủi ro của ngân hàng, giả định được lập hồ sơ và phương pháp vững chắc; dùng để đánh giá tác động lên tình trạng tài chính và đề xuất hành động.
  > "A bank's stress testing framework for IRRBB should be commensurate with its nature, size and complexity as well as business activities and overall risk profile. The framework should include clearly defined objectives, scenarios tailored to the bank's businesses and risks, well documented assumptions and sound methodologies. The framework will be used to assess the potential impact of the scenarios on the bank's financial condition, enable ongoing and effective review processes for stress tests and recommend actions based on the stress test results."
  > — u03, par 38 ^irrbb-p04-7

- Xác định kịch bản sốc và stress IRRBB cần sự phối hợp của nhiều chuyên gia trong ngân hàng (traders, treasury, tài chính, ALCO, quản lý và kiểm soát rủi ro, chuyên gia kinh tế); chương trình stress testing IRRBB nên bảo đảm ý kiến chuyên gia được xem xét.
  > "The identification of relevant shock and stress scenarios for IRRBB, the application of sound modelling approaches and the appropriate use of the stress testing results require the collaboration of different experts within a bank (eg traders, the treasury department, the finance department, the ALCO, the risk management and risk control departments and/or the bank's economists)."
  > — u03, par 39 ^irrbb-p04-8

- Ngân hàng nên xác định theo từng đồng tiền một dải biến động lãi suất tiềm năng, gồm cả kịch bản có yếu tố stress nghiêm trọng; khi xây dựng kịch bản nên xét hình dạng và mức của cấu trúc kỳ hạn hiện tại, volatility lịch sử và hàm ý; trong môi trường lãi suất thấp nên xét kịch bản lãi suất âm và tác động bất đối xứng lên tài sản và nợ.
  > "Banks should determine, by currency, a range of potential interest rate movements against which they will measure their IRRBB exposures. Management should ensure that risk is measured under a reasonable range of potential interest rate scenarios, including some containing severe stress elements. In developing the scenarios, banks should consider a variety of factors, such as the shape and level of the current term structure of interest rates and the historical and implied volatility of interest rates. In low interest rate environments, banks should also consider negative interest rate scenarios and the possibility of asymmetrical effects of negative interest rates on their assets and liabilities."
  > — u03, par 40 ^irrbb-p04-9

- Khi chọn kịch bản, ngân hàng nên xét bản chất và nguồn của trạng thái IRRBB, thời gian cần để giảm hoặc đóng trạng thái bất lợi, và khả năng/sẵn sàng chịu lỗ kế toán để tái định vị hồ sơ rủi ro; dải sốc nên đủ rộng để governing body hiểu rủi ro trong sản phẩm và hoạt động.
  > "A bank should consider the nature and sources of its IRRBB exposures, the time it would need to take action to reduce or unwind unfavourable IRRBB exposures, and its capability/willingness to withstand accounting losses in order to reposition its risk profile. A bank should select scenarios that provide meaningful estimates of risk and include a range of shocks that is sufficiently wide to allow the governing body or its delegates to understand the risk inherent in the bank's products and activities."
  > — u03, par 41 ^irrbb-p04-10

- Kịch bản nên đủ rộng để nhận diện gap risk song song và phi song song, basis risk và option risk; trong nhiều trường hợp sốc lãi suất tĩnh có thể không đủ; kịch bản nên vừa nghiêm trọng vừa khả dĩ so với mức lãi suất và chu kỳ lãi suất hiện tại.
  > "The scenarios should be sufficiently wide-ranging to identify parallel and non-parallel gap risk, basis risk and option risk. In many cases, static interest rate shocks may be insufficient to assess IRRBB exposure adequately. Banks should ensure that the scenarios are both severe and plausible, in light of the existing level of interest rates and the interest rate cycle."
  > — u03, par 41 (gạch 1) ^irrbb-p04-11

- Nên xem xét riêng các công cụ hoặc thị trường có tập trung, vì vị thế đó có thể khó thanh lý hoặc bù trừ khi thị trường căng thẳng.
  > "Special consideration should be given to instruments or markets where concentrations exist, because those positions may be more difficult to liquidate or offset in a stressful market environment."
  > — u03, par 41 (gạch 2) ^irrbb-p04-12

- Ngân hàng nên đánh giá tương tác có thể có giữa IRRBB với các rủi ro liên quan và rủi ro khác (vd credit risk, liquidity risk).
  > "Banks should assess the possible interaction of IRRBB with its related risks, as well as other risks (eg credit risk, liquidity risk)."
  > — u03, par 41 (gạch 3) ^irrbb-p04-13

- Ngân hàng nên đánh giá tác động lên NII của biến động bất lợi spread của tài sản/nợ mới thay thế tài sản/nợ đáo hạn trong chân trời dự báo.
  > "Banks should assess the effect of adverse changes in the spreads of new assets/liabilities replacing those assets/liabilities maturing over the horizon of the forecast on their NII."
  > — u03, par 41 (gạch 4) ^irrbb-p04-14

- Ngân hàng có option risk đáng kể nên có kịch bản phản ánh việc thực hiện quyền chọn, vd sản phẩm đã bán cap/floor thì đánh giá vị thế thay đổi khi cap/floor vào trạng thái in-the-money; do giá trị quyền chọn biến động theo volatility lãi suất, ngân hàng nên xây dựng giả định để đo IRRBB trước thay đổi volatility.
  > "Banks with significant option risk should include scenarios that capture the exercise of such options. For example, banks that have products with sold caps or floors should include scenarios that assess how the risk positions would change should those caps or floors move into the money. Given that the market value of options also fluctuates with changes in the volatility of interest rates, banks should develop interest rate assumptions to measure their IRRBB exposures to changes in interest rate volatilities."
  > — u03, par 41 (gạch 5) ^irrbb-p04-15

- Khi xây dựng kịch bản, ngân hàng nên chỉ rõ cấu trúc kỳ hạn lãi suất được dùng và basis relationship giữa các đường cong, chỉ số lãi suất; nên ước lượng cách lãi suất do ban điều hành quản lý (prime rate, lãi suất tiền gửi bán lẻ) thay đổi; ban điều hành nên lập hồ sơ cách rút ra các giả định này.
  > "Banks should specify, in building their interest rate shock and stress scenarios, the term structure of interest rates that will be incorporated and the basis relationship between yield curves, rate indices etc. Banks should also estimate how interest rates that are administered or managed by management (eg prime rates or retail deposit rates, as opposed to those that are purely marketdriven) might change. Management should document how these assumptions are derived."
  > — u03, par 41 (gạch 6) ^irrbb-p04-16

- Kịch bản forward-looking nên phản ánh thay đổi cơ cấu danh mục do yếu tố ngân hàng kiểm soát (kế hoạch mua lại, sản xuất) và yếu tố bên ngoài (cạnh tranh, pháp lý, thuế); sản phẩm mới có ít dữ liệu lịch sử; thông tin thị trường mới và rủi ro mới nổi chưa có trong các đợt stress lịch sử.
  > "In addition, forward-looking scenarios should incorporate changes in portfolio composition due to factors under the control of the bank (eg the bank's acquisition and production plans) as well as external factors (eg changing competitive, legal or tax environments); new products where only limited historical data are available; new market information and new emerging risks that are not necessarily covered by historical stress episodes."
  > — u03, par 42 ^irrbb-p04-17

- Ngân hàng nên thực hiện reverse stress test định tính và định lượng để (i) nhận diện kịch bản lãi suất có thể đe doạ nghiêm trọng vốn và thu nhập; (ii) làm lộ điểm yếu phát sinh từ chiến lược hedging và phản ứng hành vi tiềm năng của khách hàng.
  > "Further, banks should perform qualitative and quantitative reverse stress tests"
  > "in order to (i) identify interest rate scenarios that could severely threaten a bank's capital and earnings; and (ii) reveal vulnerabilities arising from its hedging strategies and the potential behavioural reactions of its customers."
  > — u03, par 43 ^irrbb-p04-18

- **Nguyên tắc 5 (Giả định hành vi & Mô hình hoá)**: Các giả định hành vi trọng yếu đối với quyền chọn lãi suất, tiền gửi không kỳ hạn (NMDs), vốn chủ sở hữu và nguyên tắc kế toán phải được hiểu thấu đáo, có cơ sở lý luận vững chắc, được kiểm định nghiêm ngặt và cập nhật định kỳ (tối thiểu hàng năm).
  > "Principle 5: In measuring IRRBB, key behavioural and modelling assumptions should be fully understood, conceptually sound and documented. Such assumptions should be rigorously tested and aligned with the bank's business strategies."
  > — u03, Principle 5 ^irrbb-p05-1

- Đối với NMDs, ngân hàng phải phân tích cơ sở khách hàng để xác định tỷ lệ tiền gửi lõi (core deposits) - phần tiền gửi khó có khả năng tái định giá ngay cả khi môi trường lãi suất biến động mạnh.
  > "To determine the appropriate assumptions for its NMDs, a bank should analyse its depositor base in order to identify the proportion of core deposits (ie NMDs which are unlikely to reprice even under significant changes in interest rate environment)."
  > — u03, par 45 ^irrbb-p05-2

- Đối với các khoản cho vay lãi suất cố định chịu rủi ro trả nợ trước hạn (prepayment) và tiền gửi có kỳ hạn chịu rủi ro rút trước hạn (early redemption), ngân hàng phải ước tính cẩn trọng tốc độ trả nợ trước hạn và tỷ lệ rút vốn sớm theo từng kịch bản sốc lãi suất.
  > "Banks should understand the nature of prepayment risk for their portfolios and make reasonable and prudent estimates of the expected prepayments. … Specifically, a bank must assess the expected average prepayment speed under each scenario."
  > — u03, par 45 ^irrbb-p05-3

- Giả định hành vi cho tiền gửi không kỳ hạn (NMDs) phải phân tầng theo đặc tính người gửi tiền (bán lẻ vs bán buôn/doanh nghiệp) và đặc tính tài khoản (tài khoản giao dịch transactional vs phi giao dịch non-transactional). Tiền gửi bán buôn có độ nhạy cảm lãi suất và tính thanh khoản khác biệt căn bản so với tiền gửi cá nhân. Đồng thời, đối với cam kết cấp tín dụng lãi suất cố định: việc giải ngân của khách hàng doanh nghiệp bán buôn phản ánh mạnh mẽ đặc tính của quyền chọn tự động (automatic options - giải ngân duy lý thuần tuý theo chênh lệch lãi suất), trong khi cam kết cho vay mua nhà bán lẻ chịu tác động bởi nhiều nhân tố hành vi phi tài chính khác.
  > "Assumptions should vary according to depositor characteristics (eg retail/wholesale) and account characteristics (eg transactional/non-transactional)."
  > "Unlike loan commitments to corporates, where drawdowns strongly reflect characteristics of automatic interest rate options, mortgage commitments (ie pipelines) to retail customers are impacted by other drivers."
  > — u03, par 45 (ii), (iv) ^irrbb-p05-4

- Mô hình hoá hành vi NMDs phải có cơ sở lý luận vững chắc, hợp lý và nhất quán với dữ liệu lịch sử. Việc thực hiện quyền chọn hành vi không chỉ biến động theo kịch bản sốc lãi suất mà còn phụ thuộc vào nhiều chiều kích khác: (1) Mức độ phản ứng của lãi suất sản phẩm trước biến động lãi suất thị trường (pass-through rate / deposit beta); (2) Mặt bằng lãi suất hiện tại; (3) Chênh lệch spread giữa lãi suất chào của ngân hàng và lãi suất thị trường; (4) Áp lực cạnh tranh từ các định chế tài chính khác; (5) Vị trí địa lý và các đặc điểm nhân khẩu học cùng thuộc tính khách hàng. Ngoài ra, ngân hàng phải xem xét tính trọng yếu của quyền chọn hành vi trong các khoản vay lãi suất thả nổi (ví dụ hành vi trả nợ trước hạn do các điều khoản trần và sàn lãi suất nhúng).
  > "Modelling assumptions should be conceptually sound and reasonable, and consistent with historical experience. Banks must carefully consider how the exercise of the behavioural optionality will vary not only under the interest rate shock and stress scenario but also across other dimensions."
  > "Responsiveness of product rates to changes in market interest rates, current level of interest rates, spread between a bank's offer rate and market rate, competition from other firms, the bank's geographical location and demographic and other relevant characteristics of its customer base."
  > "Further, banks should consider the materiality of the impact of behavioural optionalities within floating rate loans. For instance, the behaviour of prepayments arising from embedded caps and floors could impact the banks' economic value of equity."
  > — u03, par 46 & par 48 ^irrbb-p05-5

- Ngân hàng phải có khả năng kiểm định tính phù hợp của các giả định hành vi then chốt và văn bản hoá toàn bộ thay đổi tham số (ví dụ so sánh ΔEVE đo lường theo hệ thống nội bộ IMS với Khuôn khổ chuẩn hoá tại Section IV). Ngân hàng phải định kỳ thực hiện phân tích độ nhạy (sensitivity analyses) cho các giả định chính trên cả thước đo giá trị kinh tế (EVE) và thước đo thu nhập (earnings). Các giả định quan trọng nhất phải được HĐQT hoặc cấp được uỷ quyền hiểu rõ, kèm mô tả cách thức các giả định này tác động đến chiến lược phòng ngừa (hedging strategies). Ngân hàng phải rà soát các giả định đo lường trọng yếu tối thiểu hàng năm (at least annually) và thường xuyên hơn khi điều kiện thị trường thay đổi nhanh.
  > "Banks should be able to test the appropriateness of key behavioural assumptions, and all changes to the assumptions of key parameters should be documented (eg by comparing the economic value of equity measured under their IMS with the standardised framework in Section IV). Banks should periodically perform sensitivity analyses for key assumptions to monitor their impact on measured IRRBB. Sensitivity analyses should be performed with reference to both economic value and earnings-based measures."
  > "The most significant assumptions underlying the system should be documented and clearly understood by the governing body or its delegates. Documentation should also include descriptions on how those assumptions could potentially affect the bank's hedging strategies."
  > "As market conditions, competitive environments and strategies change over time, the bank should review significant measurement assumptions at least annually and more frequently during rapidly changing market conditions."
  > — u03, par 49, 50, 51 ^irrbb-p05-6

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

- Công bố về commercial margin trong dòng tiền ∆EVE: ngân hàng nên (should) đưa mọi dòng tiền từ tài sản, nợ và ngoại bảng nhạy cảm lãi suất của sổ ngân hàng vào tính toán, và nên công bố đã loại trừ hay đưa commercial margin và các cấu phần spread khác vào dòng tiền.
  > "Banks should include all cash flows from all interest rate-sensitive assets, 11 liabilities and off-balance sheet items in the banking book in the computation of their exposure. Banks should disclose whether they have excluded or included commercial margins and other spread components in their cash flows."
  > — u03, par 70(i)(b) ^irrbb-p08-4

- Lãi suất chiết khấu cho ∆EVE công bố: dòng tiền nên được chiết khấu bằng lãi suất phi rủi ro, hoặc lãi suất phi rủi ro cộng commercial margin và spread (chỉ khi dòng tiền đã gồm các cấu phần này); ngân hàng nên công bố đã dùng lựa chọn nào. Footnote 12: hệ số chiết khấu phải (must) đại diện cho lãi suất zero coupon phi rủi ro; ví dụ đường cong chấp nhận được là secured interest rate swap curve.
  > "Cash flows should be discounted using either a risk-free rate 12 or a risk-free rate including commercial margins and other spread components (only if the bank has included commercial margins and other spread components in its cash flows). Banks should disclose whether they have discounted their cash flows using a risk-free rate or a risk-free rate including commercial margins and other spread components."
  > "The discounting factors must be representative of a risk-free zero coupon rate. An example of an acceptable yield curve is a secured interest rate swap curve."
  > — u03, par 70(i)(c) & fn 12 ^irrbb-p08-5

- Table A (công bố định tính, bắt buộc, hằng năm), dòng g: mô tả giả định mô hình và tham số chính dùng để tính ∆EVE và ∆NII trong Table B, gồm việc dòng tiền ∆EVE có bao gồm commercial margin và spread hay không, và lãi suất chiết khấu đã dùng.
  > "Scope of application: Mandatory for all banks within the scope of application set out in Section III."
  > "A high-level description of key modelling and parametric assumptions used in calculating ∆EVE and ∆NII in"
  > "For ∆EVE, whether commercial margins and other spread components have been included in the cash flows"
  > "used in the computation and discount rate used."
  > — u03, Table A dòng g ^irrbb-p08-6

- Khung công bố thông tin định tính và định lượng Bảng A (Table A — Mục đích, phạm vi, tần suất và định dạng): Nhằm mô tả mục tiêu và chính sách quản trị IRRBB; bắt buộc (mandatory) đối với tất cả ngân hàng thuộc phạm vi áp dụng của Section III; tần suất công bố hằng năm (annual); định dạng linh hoạt (flexible format); số liệu định lượng dựa trên số bình quân ngày/tháng trong năm hoặc số liệu tại ngày báo cáo.
  > "Purpose: To provide a description of the risk management objectives and policies concerning IRRBB."
  > "Scope of application: Mandatory for all banks within the scope of application set out in Section III."
  > "Quantitative information is based on the daily or monthly average of the year or on the data as of the reporting date."
  > — u03, Table A ^irrbb-p08-7

- Tám tiêu chí công bố định tính cốt lõi trong Bảng A (Table A, dòng a–f, h):
  - (a) Định nghĩa IRRBB của ngân hàng phục vụ kiểm soát và đo lường rủi ro;
  - (b) Chiến lược quản trị và giảm thiểu rủi ro tổng thể (theo dõi EVE và NII so với hạn mức, thực hành hedging, stress test, outcomes analysis, vai trò kiểm toán độc lập, vai trò và hoạt động của ALCO, kiểm định mô hình, và cập nhật theo điều kiện thị trường);
  - (c) Tần suất tính toán các thước đo IRRBB và mô tả các thước đo độ nhạy cụ thể;
  - (d) Mô tả các kịch bản sốc và stress lãi suất dùng để ước tính thay đổi EVE và thu nhập;
  - (e) Giải trình khi các giả định mô hình trọng yếu trong IMS (dùng cho nội bộ/ICAAP) khác biệt so với giả định quy định trong Bảng B, bao gồm chiều hướng tác động và cơ sở lý luận;
  - (f) Mô tả cấp cao về chiến lược phòng ngừa IRRBB và xử lý kế toán tương ứng (kế toán phòng ngừa);
  - (h) Thông tin tuỳ chọn giải thích độ nhạy hoặc biến động lớn so với các kỳ công bố trước.
  > "A description of the bank's overall IRRBB management and mitigation strategies. Examples are: monitoring of EVE and NII in relation to established limits, hedging practices, conduct of stress testing, outcomes analysis, the role of independent audit, the role and practices of the ALCO, the bank's practices to ensure appropriate model validation, and timely updates in response to changing market conditions."
  > "Where significant modelling assumptions used in the bank's IMS (ie the EVE metric generated by the bank for purposes other than disclosure, eg for internal assessment of capital adequacy) are different from the modelling assumptions prescribed for the disclosure in Table B, the bank should provide a description of those assumptions and of their directional implications and explain its rationale for making those assumptions"
  > "A high-level description of how the bank hedges its IRRBB, as well as the associated accounting treatment."
  > — u03, Table A ^irrbb-p08-8

- Các giả định mô hình và tham số chi tiết trong Bảng A dòng g và công bố định lượng tiền gửi không kỳ hạn NMDs:
  - Dòng g: Mô tả chi tiết phương pháp xác định kỳ hạn tái định giá bình quân của NMDs; phương pháp ước tính tỷ lệ trả nợ trước hạn (prepayment rates) của các khoản vay và tỷ lệ rút tiền gửi có kỳ hạn sớm (early withdrawal rates); các giả định quyền chọn hành vi khác có tác động trọng yếu; phương pháp gộp dòng tiền giữa các đồng tiền và tương quan lãi suất giữa các đồng tiền;
  - Công bố định lượng: Bắt buộc công bố (1) Kỳ hạn tái định giá bình quân gán cho NMDs (Average repricing maturity assigned to NMDs); và (2) Kỳ hạn tái định giá dài nhất gán cho NMDs (Longest repricing maturity assigned to NMDs).
  > "How the average repricing maturity of non-maturity deposits in (1) has been determined (including any unique product characteristics that affect assessment of repricing behaviour)."
  > "The methodology used to estimate the prepayment rates of customer loans, and/or the early withdrawal rates for time deposits, and other significant assumptions."
  > "Any methods of aggregation across currencies and any significant interest rate correlations between different currencies."
  > "Average repricing maturity assigned to NMDs."
  > "Longest repricing maturity assigned to NMDs."
  > — u03, Table A ^irrbb-p08-9

- Khung công bố định lượng Bảng B (Table B — Biến động EVE và NII dưới các kịch bản sốc lãi suất chuẩn hoá):
  - Bắt buộc (mandatory) đối với tất cả ngân hàng trong phạm vi điều chỉnh; tần suất hằng năm tại thời điểm kết thúc năm tài chính; định dạng cố định (fixed format);
  - Bắt buộc đi kèm phần thuyết minh bình luận (accompanying narrative) về ý nghĩa của các giá trị báo cáo và giải thích mọi thay đổi trọng yếu so với kỳ báo cáo trước;
  - Cấu trúc bảng: Trình bày số liệu bằng đồng tiền báo cáo, so sánh giữa kỳ hiện tại ($T$) và kỳ trước ($T-1$) cho 6 kịch bản sốc lãi suất đối với $\Delta EVE$ (Parallel up/down, Steepener, Flattener, Short rate up/down) và 2 kịch bản song song đối với $\Delta NII$ (Parallel up/down); dòng tổn thất cực đại (Maximum $\Delta EVE$); và mức Vốn cấp 1 (Tier 1 capital) tại $T$ và $T-1$.
  > "Frequency: Annual, as at the bank's financial year-end."
  > "Format: Fixed."
  > "Accompanying narrative: Commentary on the significance of the reported values and an explanation of any material changes since the previous reporting period."
  > — u03, Table B ^irrbb-p08-10

- Định nghĩa phương pháp luận tính toán các chỉ số trong Bảng B và khuyến khích công bố tự nguyện:
  - (i) $\Delta EVE$ được tính toán dựa trên hệ thống đo lường nội bộ (IMS) sử dụng giả định bảng cân đối run-off và sốc lãi suất tức thời (instantaneous shock), hoặc tính theo khuôn khổ chuẩn hoá (Section IV) nếu ngân hàng tự nguyện áp dụng hoặc bị cơ quan giám sát bắt buộc;
  - (ii) $\Delta NII$ là biến động thu nhập lãi thuần dự phóng trên chân trời 12 tháng liên tục hướng về tương lai (rolling 12-month period) so với kịch bản dự phóng tốt nhất của ngân hàng, sử dụng giả định bảng cân đối không đổi (constant balance sheet) và cú sốc lãi suất tức thời;
  - Ngoài các thông tin bắt buộc trong Bảng A và Bảng B, ngân hàng được khuyến khích công bố tự nguyện các thước đo rủi ro nội bộ bổ trợ nhằm hỗ trợ thị trường diễn giải đúng đắn các số liệu công bố bắt buộc.
  > "the change in the economic value of equity based on its IMS, using a run-off balance sheet and an instantaneous shock or based on the result of the standardised framework as set out in Section IV"
  > "the change in projected NII over a forward-looking rolling 12-month period compared with the bank's own best estimate 12 month projections, using a constant balance sheet assumption and an instantaneous shock."
  > "In addition to the required disclosures in Tables A and B, banks are encouraged to make voluntary disclosures of information on internal measures of IRRBB that would assist the market in interpreting the mandatory disclosure numbers."
  > — u03, Table B definitions & par 71 ^irrbb-p08-11

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

- **Nguyên tắc 12 (Ngân hàng ngoại lai & Biện pháp can thiệp giám sát)**: Cơ quan giám sát phải công bố tiêu chí xác định ngân hàng ngoại lai; cơ quan giám sát nên (should) áp dụng ít nhất một phép thử ngoại lai/trọng yếu so sánh mức giảm giá trị kinh tế cực đại (maximum ∆EVE) dưới 6 kịch bản sốc lãi suất với **15% Vốn cấp 1 (Tier 1 capital)**.
  > "Principle 12: Supervisors must publish their criteria for identifying outlier banks. Banks identified as outliers must be considered as potentially having undue IRRBB. When a review of a bank's IRRBB exposure reveals inadequate management or excessive risk relative to capital, earnings or general risk profile, supervisors must require mitigation actions and/or additional capital. … The supervisor should implement at least one outlier/materiality test that compares the bank's maximum ∆EVE, under the six prescribed interest rate shock scenarios set out in Annex 2, with 15% of its Tier 1 capital"
  > — u03, Principle 12 & par 88 ^irrbb-p12-1

- Cơ quan giám sát có thể áp dụng các bài kiểm tra ngoại lai bổ sung (dựa trên vốn CET1 hoặc rủi ro thu nhập ∆NII) nhưng ngưỡng xác định không được lỏng hơn 15% Vốn cấp 1.
  > "Supervisors may also implement additional outlier/materiality tests … For the additional outlier/materiality tests, the threshold for defining an outlier bank should be at least as stringent as 15% of Tier 1 capital."
  > — u03, par 89 ^irrbb-p12-2

- Khi phát hiện ngân hàng quản trị không đầy đủ hoặc có rủi ro quá mức, cơ quan giám sát phải yêu cầu ngân hàng thực hiện một hoặc nhiều biện pháp can thiệp: giảm phơi lượng rủi ro (ví dụ phòng ngừa rủi ro), tăng thêm vốn quy định, đặt ràng buộc lên các tham số nội bộ, và/hoặc cải thiện khuôn khổ quản trị rủi ro (thời hạn thực hiện: par 95).
  > "When a national supervisor concludes that a bank's management of IRRBB is inadequate or that it has excessive risk relative to its capital or earnings, or its general risk profile, the supervisor must require the bank to take one or more of the following actions: reduce its IRRBB exposures (eg by hedging); raise additional capital; set constraints on the internal risk parameters used by a bank; and/or improve its risk management framework."
  > — u03, par 94 ^irrbb-p12-3

- Ngân hàng bị cơ quan giám sát xác định là outlier theo tiêu chí đã công bố phải (must) được coi là có khả năng mang IRRBB quá mức và phải được rà soát.
  > "Banks identified by supervisors under their criteria as outliers must be considered as potentially having undue IRRBB and subject to review."
  > — u03, par 90 ^irrbb-p12-4

- Khi đánh giá vốn và thu nhập so với IRRBB, cơ quan giám sát nên xét: ∆EVE dưới nhiều kịch bản sốc và stress, kèm tác động của các giả định then chốt (giữ/trừ commercial margin, cơ cấu phân bổ vốn chủ sở hữu thực tế, độ ổn định NMD, quyền trả trước); và sức mạnh, độ ổn định của dòng thu nhập so với mức thu nhập cần cho hoạt động bình thường.
  > "With regard to IRRBB, supervisors should evaluate whether the bank has adequate capital and earnings that are commensurate with its level of short-term and long-term IRRBB exposures, as well as the risk those exposures may pose to its future financial performance. Supervisors should consider the following factors:"
  > "The ∆EVE under a variety of shocked and stressed interest rate scenarios."
  > "Supervisors should, in their assessment, consider the impact of key assumptions on the ∆EVE calculated, including those related to the inclusion/exclusion of commercial margins, the bank's actual equity allocation profile, the stability of NMDs and prepayment optionality."
  > "The strength and stability of the earnings stream and the level of income needed to generate and maintain normal business operations."
  > — u03, par 91 ^irrbb-p12-5

- Khi IMS của ngân hàng đo lường IRRBB không đạt, cơ quan giám sát nên (should) yêu cầu ngân hàng cải thiện IMS và/hoặc dùng standardised framework ở Section IV để tính IRRBB theo ∆EVE.
  > "When a supervisor determines that a bank's IMS is deficient in its measurement of IRRBB, the supervisor should require the bank to improve its IMS and/or use the standardised framework set out in Section IV to compute its IRRBB in terms of ∆EVE."
  > — u03, par 92 ^irrbb-p12-6

- Ngân hàng cũng có thể (could) bị coi là có rủi ro quá mức so với thu nhập nếu ∆NII dưới sốc khiến thu nhập không đủ duy trì hoạt động kinh doanh bình thường.
  > "A bank could also be considered to have excessive risk relative to earnings if its shocked ΔNII was such that the bank would not have sufficient income to maintain its normal business operations."
  > — u03, par 93 ^irrbb-p12-7

- Việc giảm IRRBB và/hoặc nâng vốn nên (should) đạt được trong một thời hạn xác định, được ấn định có tính tới điều kiện tài chính và kinh tế đang diễn ra và nguyên nhân khiến phơi lượng IRRBB vượt ngưỡng giám sát.
  > "The reduction in IRRBB and/or the expected higher level of capital should be achieved within a specified time frame, to be established taking into consideration prevailing financial and economic conditions, as well as the causes of IRRBB exposure exceeding the supervisory threshold."
  > — u03, par 95 ^irrbb-p12-8

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

- Notional repricing cash flow CF(t) là một trong ba loại: hoàn trả gốc (ví dụ tại contractual maturity), tái định giá gốc, hoặc thanh toán lãi trên phần gốc chưa hoàn trả hay chưa tái định giá. Ngày của mỗi khoản hoàn trả, tái định giá hay thanh toán lãi đều được gọi là repricing date của khoản đó.
  > "A notional repricing cash flow CF() is defined as:"
  > "any repayment of principal (eg at contractual maturity);"
  > "any repricing of principal;"
  > "any interest payment on a tranche of principal that has not yet been repaid or repriced;"
  > "The date of each repayment, repricing or interest payment is referred to as its repricing date."
  > — u05, par 102 ^irrbb-u05-9

- Tái định giá xảy ra tại ngày sớm nhất mà ngân hàng hoặc đối tác được quyền đơn phương thay đổi lãi suất, hoặc ngày lãi suất của công cụ thả nổi tự động thay đổi theo biến động của benchmark bên ngoài.
  > "repricing is said to occur at the earliest date at which either the bank or its counterparty is entitled to unilaterally change the interest rate, or at which the rate on a floating rate instrument changes automatically in response to a change in an external benchmark"
  > — u05, par 102 ^irrbb-u05-10

- Phần spread của khoản thanh toán lãi trên phần gốc chưa hoàn trả và không tái định giá phải được slot tới contractual maturity, bất kể phần gốc chưa khấu hao đã tái định giá hay chưa.
  > "spread components of interest payments on a tranche of principal that has not yet been repaid and which do not reprice must be slotted until their contractual maturity irrespective of whether the non-amortised principal has been repriced or not."
  > — u05, par 102 ^irrbb-u05-11

- Công cụ lãi suất thả nổi được giả định tái định giá toàn bộ tại first reset date. Toàn bộ gốc được slot vào dải kỳ hạn chứa ngày đó, không slot thêm dòng tiền vào dải sau, trừ phần spread không tái định giá.
  > "Floating rate instruments are assumed to reprice fully at the first reset date. Hence, the entire principal amount is slotted into the bucket in which that date falls, with no additional slotting of notional repricing cash flows to later time buckets or time bucket midpoints (other than the spread component which is not repriced)."
  > — u05, par 104 ^irrbb-u05-12

- Với vị thế amenable to standardisation, notional repricing cash flow có thể được slot theo contractual maturity nếu coupon cố định, hoặc vào kỳ tái định giá kế tiếp nếu coupon thả nổi. Với vị thế lãi suất cố định (dòng tiền chắc chắn tới contractual maturity), mọi coupon và mọi khoản trả gốc định kỳ hay cuối kỳ nên được phân bổ vào time bucket midpoint gần nhất với contractual maturity.
  > "Notional repricing cash flows can be slotted into appropriate time buckets or time bucket midpoints based on their contractual maturity, if subject to fixed coupons, or into the next repricing period if coupons are floating."
  > "Fixed rate positions: such positions generate cash flows that are certain till the point of contractual maturity."
  > "All coupon cash flows and periodic or final principal repayments should be allocated to the time bucket midpoints closest to the contractual maturity."
  > — u05, par 106 ^irrbb-u05-13

- Vị thế lãi suất thả nổi có dòng tiền không dự báo được sau next repricing date, ngoài việc giá trị hiện tại được đặt lại về par. Vì vậy công cụ này có thể được coi là chuỗi coupon tới lần tái định giá kế tiếp cộng một dòng par notional tại time bucket midpoint gần nhất với dải chứa next reset date.
  > "Floating rate positions: such positions generate cash flows that are not predictable past the next repricing date other than that the present value would be reset to par. Accordingly, such instruments can be treated as a series of coupon payments until the next repricing and a par notional cash flow at the time bucket midpoint closest to the next reset date bucket."
  > — u05, par 106 ^irrbb-u05-14

- Ngân hàng được chọn có trừ commercial margin và các spread component khác khỏi notional repricing cash flow hay không; phương pháp dùng phải thận trọng và minh bạch.
  > "Banks have the choice of whether to deduct commercial margins and other spread components from the notional repricing cash flows, using a prudent and transparent methodology."
  > — u05, par 103 ^irrbb-u05-15

- Mọi notional repricing cash flow của tài sản, nợ và khoản mục ngoại bảng nhạy cảm lãi suất, theo từng đồng tiền, được phân bổ vào các dải kỳ hạn hoặc điểm giữa dải theo khả năng chuẩn hoá của vị thế.
  > "All notional repricing cash flows associated with interest rate-sensitive assets, liabilities and offbalance sheet items, for each currency, are allocated to the prescribed time buckets or time bucket midpoints"
  > "based on their amenability to standardisation."
  > — u05, par 105 ^irrbb-u05-16

- Bước 1 tính ∆EVE: theo từng kịch bản i, mọi notional repricing cash flow được slot vào dải k hoặc điểm giữa t_k; trong mỗi dải, dòng tiền dương và âm được bù trừ thành một vị thế long hoặc short duy nhất, phần bù trừ bị loại khỏi phép tính. Kết quả là tập CF_{i,c}(k) hoặc CF_{i,c}(t_k).
  > "Under each scenario i, all notional repricing cash flows are slotted into the respective time bucket"
  > "all positive and negative notional repricing cash flows are netted"
  > "to form a single long or short position, with the cancelled parts removed from the calculation."
  > — u05, par 132 (1) ^irrbb-u05-17

- Bước 2: notional repricing cash flow ròng của mỗi dải được nhân với discount factor liên tục, phản ánh kịch bản sốc i của đồng tiền c theo Annex 2; t_k là điểm giữa dải k. Kết quả là vị thế ròng có trọng số, có thể dương hoặc âm.

  $$DF_{i,c}(t_k) = \exp(-R_{i,c}(t_k) \cdot t_k)$$

  > "Net notional repricing cash flows in each time bucket k or time bucket midpoint"
  > "are weighted by a continuously compounded discount factor:"
  > "that reflects the interest rate shock scenario i in currency c as set out in Annex 2, and where"
  > "is the midpoint of time bucket k. This results in a weighted net position, which may be positive or negative for each time bucket."
  > — u05, par 132 (2) ^irrbb-u05-18

- Dòng tiền nên được chiết khấu bằng risk-free rate, hoặc risk-free rate cộng commercial margin và spread component (chỉ khi ngân hàng đã đưa các phần này vào dòng tiền). Discount factor phải đại diện cho risk-free zero coupon rate; ví dụ đường cong chấp nhận được là secured interest rate swap curve.
  > "The cash flows should be discounted using either a risk-free rate"
  > "or a risk-free rate including commercial margin and other spread components (only if the bank has included commercial margins and other spread components in its cash flows)."
  > "The discounting factors must be representative of a risk-free zero coupon rate. An example of an acceptable yield curve is a secured interest rate swap curve."
  > — u05, par 132 (2) & footnote 29 ^irrbb-u05-19

- Bước 3: cộng các vị thế ròng có trọng số để ra EVE của đồng tiền c trong kịch bản i, không gồm vị thế quyền chọn lãi suất tự động.

  $$EVE_{i,c}^{nao} = \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k)$$

  > "These risk-weighted net positions are summed to determine the EVE in currency c under scenario i (excluding automatic interest rate option positions):"
  > — u05, par 132 (3) ^irrbb-u05-20

- Bước 4: ∆EVE của đồng tiền c trong kịch bản i bằng EVE^nao theo cấu trúc kỳ hạn hiện tại trừ EVE^nao của kịch bản i, cộng tổng thước đo rủi ro quyền chọn lãi suất tự động KAO_{i,c}.

  $$\Delta EVE_{i,c} = \sum_{k=1}^{K} CF_{0,c}(k) \cdot DF_{0,c}(t_k) - \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k) + KAO_{i,c}$$

  > "Then, the full change in EVE in currency c associated with scenario i is obtained by subtracting"
  > "from the EVE under the current interest rate term structure"
  > "and by adding the the total measure for automatic interest rate option risk"
  > — u05, par 132 (4) ^irrbb-u05-21

- Intra-bucket mismatch risk: các notional repricing cash flow có ngày đáo hạn khác nhau nhưng cùng dải được giả định khớp hoàn toàn; rủi ro này được giảm nhờ dùng nhiều dải (K = 19).
  > "Intra-bucket mismatch risk arises as notional repricing cash flows with different maturity dates, but falling within the same time bucket or time bucket midpoint, are assumed to match perfectly. This is mitigated by introducing a high number of time buckets (ie K=19)."
  > — u05, par 132 (chú thích) ^irrbb-u05-22

- Tuỳ cách xử lý NMD, prepayment và sản phẩm có behavioural option nhúng khác, notional repricing cash flow có thể khác nhau theo kịch bản i.
  > "Note that, depending on the approach taken for NMDs, prepayments and products with other embedded behavioural options, the notional repricing cash flows may vary by scenario i (scenario-dependent cash flow products)."
  > — u05, par 132 (chú thích) ^irrbb-u05-23

- Cơ quan giám sát quốc gia được phép quy định cách gộp tiền tệ khác cho ngân hàng của mình, nếu chứng minh được bằng bằng chứng rằng cách đó vẫn phù hợp khẩu vị IRRBB của jurisdiction.
  > "National supervisors would, however, be allowed to prescribe a different method of currency aggregation for their banks, if the national supervisor is able to support, with evidence, that such a method would remain in line with the jurisdiction's appetite for IRRBB."
  > — u05, par 132 ^irrbb-u05-24

- Table 1 của Section IV: lịch 19 dải kỳ hạn cho notional repricing cash flow, số trong ngoặc là điểm giữa dải $t_k$ (năm). Dải đầu là Overnight (điểm giữa 0.0028Y), dải cuối là trên 20 năm (điểm giữa 25Y). Bảng chia ba nhóm: lãi suất ngắn hạn (8 dải, tới 2Y), trung hạn (5 dải, 2Y–7Y), dài hạn (6 dải, trên 7Y).
  > "Table 1. The maturity schedule with 19 time buckets for notional repricing cash flows repricing at"
  > "The number in brackets is the time bucket's midpoint"
  > "Overnight (0.0028Y)"
  > "CF 9M< t ≦1Y (0.875Y)"
  > "CF 15Y< t ≦ 20Y (17.5Y)"
  > "CF > 20Y t (25Y)"
  > — u05, Table 1 (lines 477-483) ^irrbb-u05-25

  | Nhóm | Dải (điểm giữa $t_k$) |
  |---|---|
  | Short term rates | O/N (0.0028Y) · O/N–1M (0.0417Y) · 1M–3M (0.1667Y) · 3M–6M (0.375Y) · 6M–9M (0.625Y) · 9M–1Y (0.875Y) · 1Y–1.5Y (1.25Y) · 1.5Y–2Y (1.75Y) |
  | Medium term rates | 2Y–3Y (2.5Y) · 3Y–4Y (3.5Y) · 4Y–5Y (4.5Y) · 5Y–6Y (5.5Y) · 6Y–7Y (6.5Y) |
  | Long term rates | 7Y–8Y (7.5Y) · 8Y–9Y (8.5Y) · 9Y–10Y (9.5Y) · 10Y–15Y (12.5Y) · 15Y–20Y (17.5Y) · >20Y (25Y) |

- Các quyền chọn tự động quan trọng nhất trong sổ ngân hàng là caps và floors, thường được nhúng trong sản phẩm ngân hàng. Swaptions (như quyền trả trước trên sản phẩm phi bán lẻ) cũng có thể được coi là quyền chọn tự động nếu đối tác tài chính tinh vi chắc chắn thực hiện quyền khi có lợi tài chính. Bất kỳ vị thế quyền chọn hành vi nào với khách hàng bán buôn làm thay đổi mẫu hình dòng tiền tái định giá danh nghĩa đều được coi là quyền chọn lãi suất tự động nhúng.
  > "The most important automatic interest rate options likely to occur in the banking book are caps and floors, which are often embedded in banking products."
  > "Swaptions, such as prepayment options on non-retail products, may also be treated as automatic interest rate options, as, in cases where such options are held by sophisticated financial market counterparties, the option holder will almost certainly exercise the option if it is in their financial interest to do so."
  > "Any behavioural option positions with wholesale customers that may change the pattern of notional repricing cash flows are considered as embedded automatic interest rate options for the purposes of this subsection."
  > — u05, par 130 & footnote 25 ^irrbb-u05-26

- Phương pháp định giá biến động giá trị hợp lý của quyền chọn bán $o$ ($\Delta FVAO_{i,c}^o$): bằng ước lượng giá trị của quyền chọn đối với người nắm giữ dưới đường cong lợi suất kịch bản sốc $i$ kết hợp mức tăng tương đối của độ biến động ngầm định là 25%, trừ đi giá trị của quyền chọn bán đối với người nắm giữ theo đường cong lợi suất tại ngày định giá (yêu cầu phương pháp luận được cơ quan giám sát phê duyệt). Tương tự, với mỗi quyền chọn mua tự động $q$, ngân hàng xác định biến động giá trị $\Delta FVAO_{i,c}^q$ giữa kịch bản sốc $i$ và cấu trúc kỳ hạn hiện tại kết hợp mức tăng độ biến động ngầm định 25%.
  > "an estimate of the value of the option to the option holder"
  > "a. a yield curve in currency c under the interest rate shock scenario i; and"
  > "b. a relative increase in the implicit volatility of 25%;"
  > "minus"
  > "(ii) the value of the sold option to the option holder, given the yield curve in currency c at the valuation date."
  > "This estimate requires a methodology approved by the supervisor."
  > "Likewise, for each bought automatic interest rate option q, the bank must determine the change in value of the option between interest rate shock scenario i and the current interest rate term structure combined with a relative increase in the implicit volatility of 25%."
  > — u05, par 130 (1), (2) ^irrbb-u05-27

- Tổng thước đo rủi ro quyền chọn lãi suất tự động $KAO_{i,c}$ của kịch bản $i$ theo đồng tiền $c$ là chênh lệch giữa tổng biến động giá trị của các quyền chọn bán và tổng biến động giá trị của các quyền chọn mua. Ngân hàng được chọn đưa toàn bộ quyền chọn mua hoặc chỉ đưa các quyền chọn mua dùng để phòng ngừa quyền chọn bán; nếu chọn chỉ đưa quyền chọn mua dùng để phòng ngừa, ngân hàng phải cộng bất kỳ biến động giá trị thị trường nào của các quyền chọn mua còn lại (phản ánh trong vốn pháp định CET1, AT1 hoặc Total Capital) vào tổng thước đo $KAO_{i,c}$.

  $$KAO_{i,c} = \sum_{o=1}^{n_c} \Delta FVAO_{i,c}^o - \sum_{q=1}^{m_c} \Delta FVAO_{i,c}^q$$

  > "The bank's total measure for automatic interest rate option risk under interest rate shock scenario *i* in currency *c* is calculated as:"
  > "Banks have a choice to either include all bought automatic options or include only automatic options used for hedging sold automatic interest rate options:"
  > "If the bank chooses to only include bought automatic interest rate options that are used for hedging sold automatic interest rate options, the bank must, for the remaining bought options, add any changes in market values reflected in the regulatory capital measure of the respective capital ratio (ie CET1, AT1 or total capital) to the total automatic interest rate option risk measure"
  > — u05, par 130 (3) & par 131 ^irrbb-u05-28

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

- Thước đo thu nhập thường tập trung vào chân trời ngắn–trung hạn (thường một đến ba năm, không quá năm năm) để hạn chế tác động cộng dồn của giả định và độ phức tạp tính toán. EV thường chỉ xét dòng tiền của công cụ đã có trên bảng cân đối; thước đo thu nhập có thể theo run-off hoặc static balance sheet, còn mô hình dynamic xét cả kinh doanh mới dự kiến.
  > "Earnings-based measures can be based on balance sheet run-off, or a static balance sheet, but more sophisticated or dynamic models tend to consider the impact of new business/production that is expected to be written in the future, as well as the run-off of existing business."
  > "The normal focus is on the short/medium-term horizon (typically one to three years, no more than five years), to limit the cumulative impact of underlying assumptions and the complexity of the calculations."
  > — u06, Annex 1 §2.1–2.2 ^irrbb-u06-8

- Dự phóng thu nhập dưới kịch bản cần giả định về khối lượng và loại tài sản, nợ mới; khoản đáo hạn, giảm; lãi suất cơ sở và margin; phí thực hiện quyền chọn. Thu nhập có thể mô hình hoá theo ba trạng thái: (a) run-off balance sheet, tài sản và nợ không được thay khi đáo hạn, trừ phần cần để tài trợ bảng cân đối còn lại; (b) constant balance sheet, giữ quy mô và cơ cấu bằng thay thế tương đương; (c) dynamic balance sheet, đưa kỳ vọng kinh doanh tương lai vào, điều chỉnh nhất quán theo kịch bản; nguồn gọi đây là cách có ý nghĩa nhất.
  > "Such projections involve a range of further assumptions about client/market behaviour, and the bank's own management response to the evolving economic climate, including:"
  > "In practical terms, this may result in modelling of earnings under three different states:"
  > "run-off balance sheet: existing assets and liabilities not replaced as they mature, except to the extent necessary to fund the remaining balance sheet;"
  > "constant balance sheet: total balance sheet size and shape maintained by assuming likefor-like replacement of assets and liabilities as they run off; and"
  > "incorporating future business expectations, adjusted for the relevant scenario in a consistent manner, ie this is the most meaningful approach."
  > — u06, Annex 1 §2.2 ^irrbb-u06-9

- ΔNII là chênh lệch NII kỳ vọng giữa kịch bản cơ sở và kịch bản stress, trên chân trời thường một đến ba năm, tối đa năm năm. Kịch bản cơ sở phản ánh kế hoạch kinh doanh hiện tại về khối lượng, giá và ngày tái định giá của giao dịch tương lai. Mô hình thu nhập phân theo độ phức tạp: run-off, constant balance sheet, và dynamic (phản ánh thay đổi khối lượng, loại kinh doanh theo môi trường lãi suất).
  > "The change in NII is the difference in the expected NII between a base scenario and an alternative, more stressful scenario. The base case scenario reflects the bank's current corporate plan in projecting the volume, pricing and repricing dates of future business transactions."
  > "Earnings measures can be differentiated according to the complexity of their forward calculations of income, from simple run-off models which assume that existing assets and liabilities mature without replacement, to constant balance sheet models which assume that assets and liabilities are replaced like for like, to the most complex dynamic models which reflect the changes in the volumes and types of business that will be undertaken (or not undertaken) in differing interest rate environments, with the expected level of prices in those circumstances."
  > — u06, Annex 1 §4.3 ^irrbb-u06-10

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

- Hiệu chỉnh biên độ sốc: Thiết lập sàn tối thiểu 100 bps và trần tối đa cho các kịch bản: trần 500 bps cho lãi suất ngắn hạn, 400 bps cho dịch chuyển song song, và 300 bps cho lãi suất dài hạn; cơ quan giám sát có thể (may), theo quyết định quốc gia, đặt mức sàn cao hơn trong kịch bản sốc địa phương cho đồng nội tệ của mình.
  > "In order to ensure a minimum level of prudence and a level playing field, a floor of 100 bp and variable caps … are set for the scenarios concerned, those caps being 500 bp for the short-term, 400 bp for the parallel and 300 bp for the long-term interest rate shock scenario. Supervisors may, applying national discretion, set a higher floor under the local interest rate shock scenarios for their home currency."
  > — u07, lines 1034-1048 ^irrbb-u07-4

- Table 1 — biên độ sốc lãi suất tuyệt đối theo đồng tiền (Parallel, Short, Long) do BCBS hiệu chỉnh tại thời điểm công bố; đây là đầu vào để tham số hoá sáu kịch bản sốc cho từng đồng tiền. Raw không ghi đơn vị trong bảng.
  > "The final calibration of the interest rate shock size determined by the Basel Committee at the time of publication is as follows:"
  > "Given Table 1, the instantaneous shocks to the risk-free rate for parallel, short and long, for each currency, the following parameterisations of the six interest rate shock scenarios should be applied:"
  > — u07, Table 1 (lines 941-957) ^irrbb-u07-5

  |  | ARS | AUD | BRL | CAD | CHF | CNY | EUR | GBP | HKD | IDR | INR |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Parallel | 400 | 300 | 400 | 200 | 100 | 250 | 200 | 250 | 200 | 400 | 400 |
  | Short | 500 | 450 | 500 | 300 | 150 | 300 | 250 | 300 | 250 | 500 | 500 |
  | Long | 300 | 200 | 300 | 150 | 100 | 150 | 100 | 150 | 100 | 350 | 300 |

  |  | JPY | KRW | MXN | RUB | SAR | SEK | SGD | TRY | USD | ZAR |
  |---|---|---|---|---|---|---|---|---|---|---|
  | Parallel | 100 | 300 | 400 | 400 | 200 | 200 | 150 | 400 | 200 | 400 |
  | Short | 100 | 400 | 500 | 500 | 300 | 300 | 200 | 500 | 300 | 500 |
  | Long | 100 | 200 | 300 | 300 | 150 | 150 | 100 | 300 | 150 | 300 |

- BCBS sẽ rà lại hiệu chỉnh biên độ sốc theo đồng tiền định kỳ (ví dụ năm năm một lần) để phản ánh điều kiện địa phương.
  > "The Committee acknowledges that shock sizes of different currencies should reflect local conditions in a timely manner. For this reason, the Committee will review the calibration of the interest rate shock sizes (eg every five years)."
  > — u07, line 995 ^irrbb-u07-6

- Bước 1 dựng Table 1: lập chuỗi 16 năm lãi suất bình quân hằng ngày cho từng đồng tiền, từ 03/01/2000 tới 31/12/2015 (Table 2); mức bình quân tính trên mọi lãi suất hằng ngày ở các kỳ hạn 3m, 6m, 1Y, 2Y, 5Y, 7Y, 10Y, 15Y và 20Y.
  > "Generate a 16-year time series of daily average interest rates for each currency"
  > "The average daily interest rates from the year 2000 (3 January 2000) to 2015 (31 December 2015) are contained in Table 2."
  > "by calculating the average rate across all daily rates in time buckets 3m, 6m, 1Y, 2Y, 5Y, 7Y, 10Y, 15Y and 20Y."
  > — u07, line 1001 ^irrbb-u07-7

- Bước 2: tham số sốc toàn cầu là bình quân gia quyền các tham số sốc theo đồng tiền. Tham số sốc toàn cầu cơ sở (Table 3): parallel 60%, short rate 85%, long rate 40%.
  > "The global shock parameter is prescribed based on the weighted average of the currencyspecific shock parameters"
  > "Table 3. Baseline global interest rate shock parameters"
  > "Parallel 60%"
  > "Short rate 85%"
  > "Long rate 40%"
  > — u07, lines 1009-1019, Table 3 ^irrbb-u07-8

- Áp tham số Table 3 vào lãi suất bình quân dài hạn ở Table 2 cho ra biên độ sốc hiệu chỉnh theo đồng tiền (Table 4); áp sàn và trần lên Table 4 cho ra bộ biên độ sốc cuối cùng ở Table 1.
  > "Applying the from Table 3 to the average long-term rates from Table 2 results in the revised interest rate shocks by currency for parallel, short and long segments of the yield curve in Table 4."
  > "Applying the caps and floors to the shocks described in Table 4 results in the final set of interest rate shocks by currency that is shown in Table 1"
  > — u07, lines 1021 & 1042 ^irrbb-u07-9

- Ba dạng sốc cơ sở: song song $\Delta R_{parallel,c}(t_k) = \pm \bar{R}_{parallel,c}$ (hằng số ở mọi dải); ngắn hạn $\Delta R_{short,c}(t_k) = \pm \bar{R}_{short,c} \cdot e^{-t_k/x}$ (lớn nhất ở kỳ hạn ngắn nhất, giảm dần về 0); dài hạn $\Delta R_{long,c}(t_k) = \pm \bar{R}_{long,c} \cdot (1 - e^{-t_k/x})$ với $S_{long}(t_k) = 1 - S_{short}(t_k)$, chỉ dùng trong sốc xoay trục. Ví dụ của nguồn tại $t_k = 3{,}5$ năm, hệ số short 0,417: sốc ngắn hạn 100 bp làm đường cong tăng 41,7 bp; với short và long cùng 100 bp (như JPY), steepener +25,4 bp, flattener −1,6 bp.
  > "(i) Parallel shock for currency c: a constant parallel shock up or down across all time buckets."
  > "(ii) Short rate shock for currency c: shock up or down that is greatest at the shortest tenor midpoint."
  > "(iii) Long rate shock for currency c (note: this is used only in the rotational shocks): Here the shock is greatest at the longest tenor midpoint and is related to the short scaling factor as:"
  > "If the absolute value of the short rate shock was 100 bp and the absolute value of the long rate shock was 100 bp (as for the Japanese yen), the change in the yield curve at"
  > — u07, lines 961–987 ^irrbb-u07-10

- Supervisor quốc gia có thể, theo national discretion, đặt sàn cho lãi suất sau sốc trong sáu kịch bản, với điều kiện sàn không lớn hơn 0; có thể đặt sàn bằng 0 hoặc âm.
  > "National supervisors may, at their discretion, set floors for the post-shock interest rates under the six interest rate shock scenarios, provided the floors are not greater than zero."
  > "Supervisors may also, applying national discretion, set a zero or negative lower bound for the post-shock interest rates, where:"
  > — u07, lines 979 & 1048 ^irrbb-u07-11

## Ghi chú convert
- u05 par 105 (raw dòng 487) và par 102 (dòng 464): marker làm mất ký hiệu toán trong lời văn (`CF()`, `,() or ,()`). Claim ^irrbb-u05-9 và ^irrbb-u05-16 chỉ trích phần lời văn còn nguyên; ký hiệu CF_{i,c}(k), CF_{i,c}(t_k) lấy theo par 132 (^irrbb-u05-17).
- u07 dòng 1003–1032 (Table 2, 3, 4): marker làm vỡ bảng. Table 2 mất giá trị hàng JPY–ZAR (dòng 1011 trôi khỏi bảng), Table 3 ký hiệu $\hat{\alpha}$ thành ký tự rác, tiêu đề Table 4 vỡ; dòng 1021 mất ký hiệu ở "Applying the from Table 3". Claim ^irrbb-u07-7, ^irrbb-u07-8, ^irrbb-u07-9 chỉ trích lời văn và các ô còn đọc được; không chép Table 2, Table 4.
