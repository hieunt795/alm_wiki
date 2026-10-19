---
title: "Bank Asset Liability Management Best Practice — Polina Bardaeva"
aliases: []
type: source
source_id: src-bardaeva-alm
domains: [alm, basel]
status: active
maturity: draft
tier: T4
doc_status: final
issuer: Polina Bardaeva
published: 2021-01-01
effective:
raw: "01_sources/alm book/A - Bank Asset Liability Management Best Practice_ Yesterday, Today and Tomorrow-De Gruyter (2021).md"
units_done: [u03, u04]
updated: 2026-10-19
---

## Thông tin nguồn
- Tác giả: Polina Bardaeva.
- Sách: *Bank Asset Liability Management Best Practice: Yesterday, Today and Tomorrow* (De Gruyter, 2021), thuộc The Moorad Choudhry Global Banking Series.
- Tier / doc_status: T4 / final.
- Raw: `01_sources/alm book/A - Bank Asset Liability Management Best Practice_ Yesterday, Today and Tomorrow-De Gruyter (2021).md` (1.899 dòng). Thư mục có thêm bản `(The Moorad Choudhry Global Banking Series) …` cùng nội dung, khác định dạng mục lục; unit tính theo bản `A - …`.
- Conversion: partial (xem `03_meta/sources.yaml`). Raw không có số trang, nên locator ghi theo chương, box hoặc bảng.
- Units covered:
  - `u03` (dòng 874–1288): Ch.10 ALM Operating Model, Ch.11 ALM Inside a Risk Management Triangle (gồm Box 11.2 IRRBB Management), Ch.12 From a Standalone ALM Desk to a Group Treasury (gồm Box 12.1 cấu trúc vốn, Box 12.2), Ch.13 ALM Role in SREP (dừng ở Table 13.1, phần còn lại thuộc u04).
  - `u04` (dòng 1289–1709; claim lấy từ 1289–1611, phần còn lại là bibliography, viết tắt, index): Ch.13 phần tiếp (Table 13.1, P2G, mảng thanh khoản), Ch.14 ALM theo quy mô và loại thị trường (Box 14.1 Recovery & Resolution), Ch.15 ALM trong khủng hoảng, Ch.16 After-Crisis ALM (economic perspective, Box 16.1, output floor, MREL, digitalization, M&A).

## Tóm tắt
- Ch.10: ALM/Treasury tổ chức theo hai mô hình đối lập là Treasury front office và ALM middle office. Mục đích là tách các nhiệm vụ xung đột: đặt hạn mức, định giá, giao dịch.
- Ch.11: ALM không gộp được vào Risk, Trading Desk hay Finance vì mỗi cách gộp sinh xung đột lợi ích. ALM/Treasury là tuyến bảo vệ thứ nhất. ALCO phải có ALM, Risk và Finance.
- Box 11.2: định nghĩa IRRBB qua hai kênh NII và EVE, rồi nêu quy trình quản trị ba bước: nhận diện, đo lường, quản lý; vốn cho IRRBB xét trong ICAAP.
- Ch.12: Group Treasury chọn giữa mô hình tập trung, phân tán và hybrid. Đặc thù thị trường địa phương (chỉ có tiền gửi tiết kiệm, kỳ hạn huy động ngắn, không phòng ngừa được) quyết định công cụ quản lý IRR. Box 12.1 mô tả chồng yêu cầu vốn theo Basel III/CRD.
- Ch.14–16 (u04): thị trường mới nổi có bảng cân đối liability sensitive, ít công cụ phòng ngừa, tiền gửi bán lẻ biến động; recovery plan và resolution (BRRD, MREL); thứ tự hành động thanh khoản, vốn, FTP trong khủng hoảng; economic perspective bổ sung normative perspective.
- Ch.13: SREP đánh giá bốn mảng; trong mảng "Risks to capital", IRRBB thuộc trách nhiệm của ALM; P2R lấy kết quả ICAAP làm điểm xuất phát.

## Key claims

### u03 — Ch.10 ALM Operating Model

- Không bàn Treasury/ALM nào chịu được toàn bộ nhiệm vụ ALM vì một số chức năng xung đột nhau. Ví dụ: một bộ phận không thể vừa đặt hạn mức vị thế vừa thực hiện giao dịch cho vị thế đó, vừa dựng đường cong lãi suất nội bộ vừa giao dịch với biên trên đường cong này.
  > "Of course, no Treasury/ALM desk could have full responsibility for all the tasks listed in the previous chapter, as some of the functions are contradicting each other and raising conflicts of interest."
  > "For example, one department can ' t set limits on positions and execute deals for these positions, construct an internal yield curve, and make deals with margin to this curve."
  > — ch10 ^ch10-1

- Thực tế có hai phương án đối lập: Treasury là front office, và ALM desk là middle office.
  > "In order to exclude obvious contradictory tasks in practice different combinations are observed, among which there are the two quite contrasted options: Treasury as a front office and ALM desk as a middle office."
  > — ch10 ^ch10-2

- Khi ALM là front office, chức năng chiến lược và kiểm soát bị loại ra. Front office ALM desk thường là profit center.
  > "When the ALM department is arranged as a front office, the strategic and controlling functions are excluded."
  > "Moreover, a front office ALM desk is more frequently a profit center."
  > — ch10 ^ch10-3

- Middle office Treasury chịu trách nhiệm chủ yếu về quản lý bảng cân đối chiến lược; ALM desk làm chức năng phân tích, cung cấp thông tin cho Ban điều hành ra quyết định.
  > "Middle office Treasury is responsible mainly for strategic balance sheet management."
  > "It is again possible to avoid a clear conflict of interest in this case, and ALM desk fulfills an analytical function, providing to the bank ' s management board all the necessary information for correct decision-making."
  > — ch10 ^ch10-4

- Table 10.1 chia nhiệm vụ ALM theo bốn nhóm (ALM risk management, BS structure targeting, price benchmarking, resources allocation) và theo tầm (ngắn hạn/chiến thuật, dài hạn/chiến lược going concern, gone concern). Trích phần dài hạn và gone concern:
  > "Table 10.1: Front office Treasury operating model."
  > — ch10 Table 10.1 ^ch10-5

| Tầm | ALM risk management | BS structure targeting | Price benchmarking | Resources allocation |
|---|---|---|---|---|
| Long-term/strategic, going concern | Interest rate risk management; Interest rate gap modelling; Liquidity risk management; Contingency planning; Balance sheet hedging; Determining metrics and limits | Debt issuance; Raising long-term funding; Securitization; Funding and capital planning; Defining capital structure | Product pricing; Business profitability models; Funds transfer pricing; Behavioral modelling; Maturity matching | NII and NIM forecasting; Target RoE setting; RoRWA comparison; Strategy development; RWA and capital allocation; Cost of capital definition |
| Gone concern | ILAAP execution; Liquidity stress-testing; Cash flow stress-testing | ICAAP execution; Capital stress-testing; MREL forecasting; Resolution planning; Recovery planning | | Economic capital calculation and allocation |

- Chọn mô hình vận hành mới là bước đầu. Phải xét toàn bộ tuyến báo cáo, vì thành viên ban điều hành mà bộ phận ALM báo cáo có thể phụ trách bộ phận khác có chức năng xung đột.
  > "It is necessary to investigate the full reporting line, as the board member to which this department reports can be responsible for other departments with which functions there will be conflict of interest, or to have private aims, partially contradicting ALM."
  > — ch10 ^ch10-6

### u03 — Ch.11 ALM Inside a Risk Management Triangle

- Khung quản trị rủi ro bảng cân đối phải xoay quanh một mô hình vận hành bảo đảm tương tác giữa Finance, Treasury (Trading Desk) và Risk.
  > "Governance and oversight framework for balance sheet risk must revolve around an operating model that provides efficient and effective interaction and liaison between Finance, Treasury (here as a Trading Desk), and Risk functions."
  > — ch11 ^ch11-1

- Kết luận của tác giả: không thể gộp ALM với bất kỳ bộ phận truyền thống nào.
  > "Already disclosing the conclusion, the arguments against inclusion are too sufficient, so uniting of ALM with either of the traditional banking units is impossible."
  > — ch11 ^ch11-2

- Table 11.1 so sánh nhiệm vụ của ALM với Risk, Trading và Finance.
  > "Table 11.1: Comparison of ALM tasks with Risk, Finance, and Trading Desk tasks."
  > — ch11 Table 11.1 ^ch11-3

| ALM | Risk | Trading | Finance |
|---|---|---|---|
| ALM risk management | Risk assessment | Execution of deals | Profitability analysis |
| BS structure targeting | Limiting positions/portfolios | Funding strategy development | Budgeting |
| Price benchmarking | Models validation, stress testing | Quoting of rates | Deviations analysis |
| Resources allocation | Economic capital evaluation | Earning income | Profit calculation |

- Trong quản lý rủi ro ALM: Risk xử lý thông tin đầu tiên và phân tích rủi ro; ALM dùng kết quả của Risk và đề xuất công cụ quản lý; Trading Desk thực hiện giao dịch do ALM đề xuất và đã được hội đồng có thẩm quyền phê duyệt.
  > "At the same time, the Risk Department is the first processor of information, analyzes these risks, and their level for separate positions/portfolios. ALM is a consumer of the results of Risk and offers suggestions/tools for managing identified risks (if they were identified). The Trading Desk then carries out risk management transactions proposed by the ALM and approved by the appropriate collegial body."
  > — ch11 ^ch11-4

- ALM xác định nguyên tắc định giá điều chuyển, dựng đường cong FTP nội bộ và quy tắc xác định lãi suất khách hàng tối thiểu.
  > "ALM determines the principles of transfer pricing, builds the internal FTP curve, and defines rules for determining the minimum client rate (and the margin of the transaction)."
  > — ch11 ^ch11-5

- Table 11.2 xếp tuyến bảo vệ: business lines tạo rủi ro và không phải tuyến bảo vệ; ALM/Treasury là tuyến 1 (quản lý bảng cân đối, dự báo vị thế, xây mô hình); Risk là tuyến 2 (đo lường, kiểm soát hạn mức, kiểm định mô hình, báo cáo); kiểm toán nội bộ là tuyến 3.
  > "Table 11.2: Lines of defense."
  > — ch11 Box 11.1, Table 11.2 ^ch11-6

| Bộ phận | Vai trò |
|---|---|
| Business lines | Make deals (generate risk) Are not lines of defense |
| 1st line of defense ALM/Treasury | Manages balance sheet (FTP, target structure, hedging) Forecasts positions; Constructs models |
| 2nd line of defense Risk | Measures and analyzes ALM risk; Controls limits and validates models; Prepares reports |
| 3rd line of defense Internal audit | Internally audits the 1st and the 2nd lines of defense |

- ALM/Treasury thực hiện giao dịch (front office) vẫn được coi là tuyến 1, vì mục tiêu của nó là bảo vệ bảng cân đối khỏi rủi ro.
  > "ALM/Treasury also can be a department that makes the deals (front-office ALM desk), but stillit will be considered as the first line of defense, as its aim is to defend the balance sheet from risk."
  > — ch11 Box 11.1 ^ch11-7

- Ngân hàng thường có "4-eyes check", trong đó cặp mắt thứ hai đến từ Risk.
  > "There is a normal practice in the bank, to have  ' 4-eyes check '  (when the  ' second pair of eyes '  comes from another department, namely from the Risk Department)."
  > — ch11 Box 11.1 ^ch11-8

- Cơ quan giám sát thường được coi là tuyến bảo vệ thứ tư, thực hiện qua SREP và thanh tra tại chỗ.
  > "It is also often admitted that there is the 4th line of defense: supervisory authorities are also fulfilling an audit function and comparison of banks '  risk governance to the defined standards."
  > "This function is executed during SREP and specific on-site inspections"
  > — ch11 Box 11.1 ^ch11-9

- Gộp ALM với Risk dẫn tới ít nhất hai xung đột lợi ích. Thứ nhất, đơn vị đánh giá không thể đánh giá rủi ro khách quan. Thứ hai, đơn vị có thể hạ thấp rủi ro để tránh dùng công cụ bất tiện.
  > "Precise investigation of the ALM and Risk functions shows that uniting both would lead to at least two conflicts of interest. First, the assessing unit wouldn ' t be able to evaluate risks impartially."
  > "In other words, no risks  -  no need for measures."
  > — ch11 ^ch11-10

- Gộp ALM vào Trading Desk là sai do xung đột lợi ích lớn; việc cho ALM không làm profit center cũng không khắc phục được. Riêng với FTP, nguyên tắc gán kỳ hạn trên đường cong không được do đơn vị thực hiện giao dịch quyết định.
  > "Consequently, including ALM into the Trading Desk ( ' external ' Treasury) will be incorrect due to major conflicts of interest, and making ALM not a profit-center does not help to overcome them."
  > "funding principles (i.e., assigning a rate on the curve of a certain tenor for certain types of transactions) can not be determined by the unit making this transaction."
  > — ch11 ^ch11-11

- Gộp ALM vào Finance sinh xung đột mục tiêu: KPI của Finance là ngân sách, nên khi kết quả kém kế hoạch, Finance có thể tăng khẩu vị rủi ro để kiếm thêm từ gap kỳ hạn/tiền tệ.
  > "Traditionally, one of the Finance Department ' s KPIs is budget target for banks '  result."
  > "the bank will be able to additionally earn on the  ' gap '  of maturity/currency positions."
  > "As a conclusion, ALM can hardly be considered a part of the Finance"
  > — ch11 ^ch11-12

- Box 11.2: IRRBB là rủi ro hiện tại hoặc tiềm năng đối với vốn và thu nhập của ngân hàng do biến động bất lợi của lãi suất tác động lên vị thế sổ ngân hàng.
  > "IRRBB refers to the current or prospective risk to the bank ' s capital and earnings arising from adverse movements in interest rates that affect the bank ' s banking book positions."
  > — ch11 Box 11.2 ^ch11-13

- Tác động bất lợi đến từ hai hướng: thu nhập và chi phí nhạy lãi suất (NII) thay đổi; giá trị hiện tại và thời điểm dòng tiền tương lai thay đổi, làm thay đổi EVE.
  > "First, the interest rate sensitive income and expenses (NII) will change, impacting a bank ' s future financial result."
  > "Second, the present value and timing of future cash flows will change, resulting in changes of the underlying value of assets,"
  > "liabilities, and off-balance sheet items, and hence a bank ' s economic value of equity (EVE)."
  > — ch11 Box 11.2 ^ch11-14

- Bước 1 là nhận diện rủi ro. Gap risk, basis risk và yield curve risk là chung cho mọi ngân hàng; optionality risk (kể cả behavioural option) có thể nhỏ hoặc đặc thù tuỳ ngân hàng.
  > "First, risk identification should be executed."
  > "For example, gap risk (comes from the term structure of banking book instruments), basis risk (arises when instruments with similar tenors are priced against different market reference rates/indices), yield curve risk (appears when the shape of the interest rate curve changes), are common to all banks. But optionality risk (arising from embedded in assets, liabilities, offbalance sheet items options, includes behavioral option risk) can be minor (or specific) in different banks."
  > — ch11 Box 11.2 ^ch11-15

- Bước 2 là đo lường tác động của các kịch bản sốc lãi suất lên vốn, NII và EVE. Thước đo giá trị kinh tế xét toàn bộ vòng đời bảng cân đối; thước đo thu nhập xét trong horizon thường là horizon ngân sách 3–4 năm.
  > "As the next step, the identified risks should be measured in terms of their potential negative impact of prescribed interest rate shock scenarios … on capital, net interest income, and EVE."
  > "They assess the effect of interest rate movements over the entire life of the balance sheet. The earnings-based measures focus on changes to future profitability within a given time horizon, usually the budgeting horizon of three to four years, and its further implications on banks '  own funds."
  > — ch11 Box 11.2 ^ch11-16

- Ở bước đo lường, nên chú ý xử lý vị thế không chuẩn, nhất là công cụ không xác định kỳ hạn.
  > "At this step special attention should be paid to treatment of nonstandard positions, in particular, instruments with undefined maturities."
  > — ch11 Box 11.2 ^ch11-17

- Bước 3: quyết định quản lý những tác động không phù hợp RAS. Công cụ gồm phòng ngừa bằng phái sinh, đầu tư equity, công cụ không nhạy lãi suất, dự báo lãi suất và kế hoạch bảng cân đối.
  > "Finally, when amounts of potential negative impact are calculated, then a decision on which of them should be managed (which of them are not in line with the RAS)  -  should be taken. Risk management can be done by means of hedging with derivatives, equity investments, non-interest rate sensitive instruments, interest rate forecasting, and balance sheet planning."
  > — ch11 Box 11.2 ^ch11-18

- Mức đủ vốn cho IRRBB phải được xét riêng trong ICAAP.
  > "Capital adequacy for IRRBB must be specifically considered as part of the ICAAP."
  > — ch11 Box 11.2 ^ch11-19

- Vùng đệm/amber zone của khẩu vị rủi ro được đặt ở các hội đồng cấp dưới, với rủi ro ALM là ALCO. ALCO nên bắt buộc có đại diện ALM, Risk và Finance; đại diện kinh doanh có thể tham dự nhưng không luôn có quyền biểu quyết và nên là thiểu số.
  > "Second, the internal buffer/amber zones for risk appetite are set on subsequent collegial bodies (in particular, on the Asset and Liability Management Committee, ALCO, for ALM-related risks). The ALCO should obligatorily include representatives from ALM, Risk, and Finance. Business representatives are welcome to participate to be aware of current stance, limitations, tasks, or achievements, but not always have the voting right (and they definitely should be the minority of the members)."
  > — ch11 ^ch11-20

- Để tránh xung đột lợi ích, đơn vị ALM nên độc lập, trực thuộc CFO hoặc CEO (khi họ có KPI cả về tham số rủi ro), hoặc thuộc đơn vị phụ trách chiến lược dài hạn.
  > "To avoid any conflict of interest, the ALM unit should be independent, give an unbiased assessment of the situation, be subordinate either to the CFO or CEO (when they have KPIs also on risk parameters), or within the unit responsible for the bank ' s long-term strategy."
  > — ch11 ^ch11-21

- Phân công thực tế: Risk lập báo cáo phân tích rủi ro (ví dụ gap analysis) cho ALM; ALM gửi yêu cầu (đã được ALCO duyệt) cho Trading Desk thực hiện giao dịch phòng ngừa, hoặc cho đơn vị kinh doanh đổi chiến lược về khối lượng và lãi suất.
  > "That means that Risk makes risk analysis reports (e.g., gap analysis) and provides them to the ALM."
  > "It can be realized by means of the Trading Desk, so ALM gives (approved by ALCO, of course) requests to the Trading Desk to make some hedging deals or to the business units to change their strategy (in volumes and rates)."
  > — ch11 ^ch11-22

- Xung đột lợi ích, kể cả trong ALM, có xu hướng tăng trong suy thoái và khủng hoảng.
  > "Many measures have already been invented to resolve conflicts of interest, but it must be considered that conflicts of interest, including the ones in ALM, tend to intensify during periods of economic recession and crises, in conditions of increased uncertainty and the search for new ways to increase profitability."
  > — ch11 ^ch11-23

### u03 — Ch.12 From a Standalone ALM Desk to a Group Treasury

- Group Treasury là ALM desk của cả tập đoàn ngân hàng.
  > "A Group Treasury is the ALM desk for the whole banking group."
  > — ch12 ^ch12-1

- Một mục tiêu của Group Treasury là phân tích và quản lý vị thế rủi ro lãi suất và tỷ giá trên sổ ngân hàng: tối thiểu hoá vị thế với rủi ro phòng ngừa được, kiểm soát chặt rủi ro không phòng ngừa được.
  > "To analyze and manage interest rate and FX risk positions in the banking book (including minimization of risk position for hedgeable risks and precise control over non-hedgeable risks)."
  > — ch12 ^ch12-2

- Group Treasury thiết kế nguyên tắc và mô hình FTP (đôi khi cả đường cong) để tối ưu sử dụng vốn và thanh khoản, tối đa hoá giá trị tập đoàn.
  > "Group Treasury is responsible for designing FTP principles, models (and sometimes even curves themselves) in a way that optimizes usage of the bank ' s capital and liquidity and maximizes the group value."
  > — ch12 ^ch12-3

- Box 12.1: Basel III đặt yêu cầu Trụ cột 1 đồng thời cho từng lớp vốn: CET1 ≥ 4,5% RWA, T1 ≥ 6%, tổng vốn ≥ 8%.
  > "Basel III defines Pillar I requirements for each layer of capital: CET1 capital should not be less than 4.5% of total risk weighted assets, T1 capital  -  not less than 6% of RWA and total capital  -  not less than 8%, simultaneously."
  > — ch12 Box 12.1 ^ch12-4

- Ngưỡng chuyển đổi AT1 theo quy định là tỷ lệ CET1 đạt 5,125%.
  > "Regulatory defined trigger is CET1 capital ratio reaching a level of 5.125%, although many banks prefer to put the trigger higher."
  > — ch12 Box 12.1 ^ch12-5

- Công cụ T2 khi còn dưới 5 năm đến hạn bắt đầu khấu trừ dần 20% mỗi năm, đạt 100% khi đáo hạn.
  > "as the instrument reaches the date when it has less than five years until maturity the amortization starts and gradually comprises 20% each year, completely reaching 100% by maturity of the instrument."
  > — ch12 Box 12.1 ^ch12-6

- Yêu cầu bổ sung riêng (Pillar II requirement) áp qua SREP là bắt buộc. Trụ cột 1 và Trụ cột 2 tạo thành TSCR, ngân hàng nên đáp ứng mọi lúc, kể cả khi căng thẳng.
  > "Another obligatory for fulfillment part of requirements is an individual add-on (Pillar II requirement) imposed as a result of SREP."
  > "Pillar I and Pillar II requirements form the Total SREP Capital Ratio (TSCR), which banks should fulfill at all times, including times of stress."
  > — ch12 Box 12.1 ^ch12-7

- Đệm vốn kết hợp gồm: capital conservation buffer 2,5% (áp đủ từ 01/2019 theo CRD IV), countercyclical buffer, systemic risk buffer.
  > "Capital conservation buffer  -  in line with CRD IV was fully phased-in by January 2019 in the amount of 2.5%."
  > "Countercyclical capital buffer (CCyB) can be imposed by national supervisory authorities"
  > — ch12 Box 12.1 ^ch12-8

- Đệm vốn kết hợp cộng TSCR tạo thành OCR, là yêu cầu vốn tối thiểu trong điều kiện cơ sở (không căng thẳng).
  > "Combined buffer requirements together with the TSCR make the overall capital ratio (OCR), which is the minimum capital requirement for banks in baseline (not stressed) conditions."
  > — ch12 Box 12.1 ^ch12-9

- P2G không bắt buộc; vi phạm P2G chỉ kích hoạt thông báo cho cơ quan quản lý kèm lý do và kế hoạch vốn.
  > "It is not obligatory, and breach of the P2G triggers only notification of the regulatory authorities with description of the reasons for this breach and a capital plan, showing how the recovery of the capital position to the level above P2G will take place."
  > — ch12 Box 12.1 ^ch12-10

- Ngày 12/3/2020, ECB lần đầu nới vốn tạm thời: ngân hàng do ECB giám sát được tạm thời vi phạm P2G và CCB.
  > "On the 12th of March 2020 for the first time ever ECB provided temporary capital relief"
  > "All banks under ECB supervision were granted the right to temporary breach P2G and CCB."
  > — ch12 Box 12.1 ^ch12-11

- Theo CRD V, P2R phải được đáp ứng bằng CET1 tối thiểu 56,25% và bằng T1 tối thiểu 75%.
  > "(P2R should be covered by CET1 at least in amount of 56.25% and by T1 in amount of at least 75%)"
  > — ch12 Box 12.2 ^ch12-12

- Đặc thù thị trường định hình bài toán ALM: thị trường chỉ có tài khoản tiết kiệm đòi hỏi đánh giá stickiness và chia tài khoản không kỳ hạn vào khung thời gian; thị trường bất định với kỳ hạn huy động tối đa 1 năm cho tài sản dài hạn đòi hỏi dùng IRS (thường kèm phái sinh FX) để phòng ngừa IRR.
  > "For example, if the banking market offers only saving accounts for its customers  -  for the balance sheet this would mean a task to assess the stickiness of funds and to split the undefined maturity accounts into proper time buckets. Another situation would be if there ' s a high uncertainty in the market  -  and, thus, the maximum available tenor of funding would be one year for financing of long-term assets (like mortgage loans). This would require involvement of IRSs (often together with FX derivatives) to hedge IRR."
  > — ch12 ^ch12-13

- Yếu tố định tính: khách hàng không tin ngân hàng do từng trải qua bất ổn thì không sản phẩm nào đổi ngay được hành vi; khách hàng bán lẻ sẽ rút tiền mỗi khi nghe tin đồn.
  > "For example, if the customers do not trust in banks, due to the experiences of many banking turbulences in the past  -  no product offers would immediately change this behavior. The retail customers will continue to run the banks each time when they hear any controversial news or even rumors."
  > — ch12 ^ch12-14

- Group Treasury phải quản lý các rủi ro bảng cân đối này; việc khó hơn khi công ty con hoạt động ở thị trường không phòng ngừa được mọi rủi ro.
  > "These balance sheet risks of different sources and complexity must be managed by the Group Treasury. This task becomes even more complicated if a subsidiary bank operates in markets where it is unable to hedge all the risks."
  > — ch12 ^ch12-15

- Group Treasury có hai mô hình vận hành cơ bản: tập trung và phân tán; kết hợp hai mô hình tạo ra nhiều mô hình lai.
  > "There are two basic operational models for Group Treasury: centralized and decentralized."
  > — ch12 ^ch12-16

- Mô hình tập trung: công ty con quản lý danh mục địa phương theo hướng dẫn của tập đoàn về rủi ro lãi suất, tỷ giá và theo hạn mức do Group Treasury đặt.
  > "From the scope of practical issues subsidiaries manage local portfolios according to the group guidelines for interest rate and FX risk management and defined by Group Treasury limits."
  > — ch12 ^ch12-17

- Nhược điểm chính của mô hình tập trung: funding và phân bổ vốn tập trung có thể không rẻ nhất do bỏ qua chênh lệch chi phí giữa các pháp nhân; phương pháp trung tâm có thể bỏ sót đặc thù địa phương.
  > "The major drawback of this model is that centralized funding and capital allocation can not be the cheapest option due to neglected economic cost differentials between legal entities, as well as centrally developed methodologies can fail to take into account local specifics of subsidiary banks."
  > — ch12 ^ch12-18

- Mô hình phân tán: Group Treasury đặt hạn mức quốc gia (kể cả hạn mức rủi ro lãi suất và tỷ giá); công ty con tự đặt bộ hạn mức chi tiết.
  > "From the practical aspect the Group Treasury defines country limits (including the limits for interest rate and FX risks), with which subsidiaries are required to comply while managing local portfolios. Subsidiaries define their own set of detailed limits."
  > — ch12 ^ch12-19

- Mô hình phân tán thiếu lợi thế quy mô, làm ít nguồn funding và công cụ phòng ngừa hơn, tăng chi phí.
  > "Furthermore, lack of scale shortens the list of possible funding sources and hedging instruments  -  which will also increase the costs."
  > — ch12 ^ch12-20

- Ở thị trường địa phương kém phát triển (thiếu công cụ, khó tiếp cận thị trường), công ty con thiếu nguồn funding và vốn, nên mô hình tập trung là cần thiết.
  > "Lack of financial instruments, little access to financial markets, undeveloped markets and financial relations will lead a subsidiary, operating in these circumstances, to shortage (or lack) of funding and capital resources (senior/subordinated debt) in financial markets."
  > "In this case application of the centralized model is essential."
  > — ch12 ^ch12-21

- Kết luận Part 2: ALM nên là chức năng độc lập với Risk, Finance và Trading Desk, nhưng tương tác và thông tin cho cả ba hằng ngày.
  > "ALM should be an independent function from either of the three but interact and inform each of them daily (also within the lines of defense)."
  > — ch12 Conclusions ^ch12-22

### u03 — Ch.13 ALM Role in SREP

- SREP là cơ chế thuộc Trụ cột 2 Basel III để bảo đảm ngân hàng có đủ vốn cho mọi rủi ro. Kết quả SREP gồm điểm số và yêu cầu vốn bổ sung riêng (P2R).
  > "In general, Supervisory Review and Evaluation Process (SREP) is a mechanism imposed in Pillar II of Basel III to ensure that banks have sufficient capital to support all the risks associated with their businesses."
  > "As a result of SREP each supervised bank receives a score and individual capital requirement add-on (the Pillar-2 Requirement, P2R)."
  > — ch13 ^ch13-1

- Điểm SREP dựa trên bốn mảng đánh giá, không theo công thức toán học cụ thể: mô hình kinh doanh; quản trị nội bộ và kiểm soát; rủi ro đối với vốn; rủi ro đối với thanh khoản và funding.
  > "The score is based on scores in four areas of assessment, although does not follow any particular mathematical dependency."
  > "Business model analysis (whether the business model of the bank can ensure sustainable growth of the institution, even in times of market downturns)."
  > "Internal governance and institution-wide controls"
  > "Risks to capital (whether capital steering is in line with the latest regulatory requirements, the quantity of risk is sufficiently covered by the own funds at the current moment and on the planning horizon)."
  > "Risks to liquidity and funding"
  > — ch13 ^ch13-2

- Theo nguyên tắc tương xứng, tổ chức tài chính được chia bốn nhóm theo tầm quan trọng với hệ thống tài chính và mức hoạt động xuyên biên giới.
  > "Following principle of proportionality all financial institutions are categorized in four distinct categories according to their importance to the global or a local financial system and the extent of any cross-border activities."
  > — ch13 Box 13.1 ^ch13-3

- Theo nguyên tắc liên tục, cơ quan giám sát theo dõi chỉ số chính hằng quý và cập nhật đánh giá từng cấu phần SREP tối thiểu hằng năm.
  > "Monitor key indicators on a quarterly basis (may establish more frequent monitoring)"
  > "Update the assessments of all individual SREP elements at least annually"
  > — ch13 Box 13.1 ^ch13-4

- Trong phân tích mô hình kinh doanh (khả năng sinh lời 12 tháng tới và tối thiểu 3 năm), ALM phụ trách các phần như điều hành chuyển hoá kỳ hạn bằng phòng ngừa IRR hoặc đổi cấu trúc bảng cân đối.
  > "Ability to generate acceptable returns over the following 12 months and over a forward-looking period of at least three years. ALM is responsible for the following parts of this topic:"
  > "Maturity transformation steering (by either hedging the IRR, or changing the balance sheet structure)"
  > — ch13 ^ch13-5

- Trong mảng rủi ro đối với vốn, rủi ro riêng lẻ gồm tín dụng, thị trường, hoạt động và IRRBB; IRRBB thuộc trách nhiệm của ALM, và chính sách, mô hình phù hợp nên chứng minh được tính bền vững của ngân hàng.
  > "Inherent individual risk (split into credit, market, operational, and IRRBB risks)."
  > "On the contrary, IRRBB is in responsibility of ALM (see Box 11.2)  -  and proper policies and models should prove sustainability of the bank."
  > — ch13 ^ch13-6

- Với khung quản lý rủi ro (gồm ICAAP, ILAAP), vai trò của ALM là đưa mọi yêu cầu quản lý vào khung điều hành và phản ánh vào chính sách tập đoàn.
  > "ALM ' s role here is to implement all regulatory requirements into the steering framework and to reflect in a subsequent manner in group policies."
  > — ch13 ^ch13-7

- P2R xuất phát từ yêu cầu vốn theo từng rủi ro dựa trên tính toán ICAAP. Với phần lớn ngân hàng, P2R không lấy y nguyên ICAAP vì cơ quan quản lý không coi là đáng tin cậy, mà dùng thêm benchmark giám sát theo từng rủi ro.
  > "Determination of the additional own funds ' requirements on a risk-by-risk basis using internal quantifications of the bank (ICAAP calculations) is the starting point."
  > "For most of the banks P2R is not defined one-to-one as in ICAAP, because regulators do not find them reliable (see →Table 13.1), and risk-specific supervisory benchmarks to account for business-model-specific considerations are then used."
  > — ch13 Box 13.2 ^ch13-8

### u04 — Ch.13 ALM Role in SREP (phần tiếp)

- Table 13.1 nêu bốn tiêu chí độ tin cậy của tính toán ICAAP: tính toán chia theo loại rủi ro; phản ánh tương quan và cấu trúc danh mục thực tế, dựa trên mô hình được công nhận và giả định thận trọng; driver được nêu rõ; so sánh được với ngân hàng cùng nhóm và benchmark giám sát.
  > "Criteria of ICAAP calculations reliability"
  > — ch13 Box 13.2, Table 13.1 ^ch13-9

| Granularity | Credibility | Understandability | Comparability |
|---|---|---|---|
| Calculations are broken down by risk type | Calculations reflect actual correlations and portfolio compositions; based on recognized or appropriate models and prudent assumptions | Underlying drivers of the calculations/methodologies are clearly specified | Calculations facilitate comparability with peers and supervisory benchmark estimations |

- Lý do và nguyên tắc của benchmark giám sát nên được giải thích cho ngân hàng, nhưng ngân hàng không đánh giá trước được, nên trong ngân sách và dự báo chỉ nên đưa giả định thận trọng về mức P2R.
  > "The rationale and general underlying principles behind the benchmarks should be explained to the institution, but can ' t be assessed by the bank in advance (and, thus, can ' t be implemented in budgeting and forecasting process; for budgeting and forecasting only conservative considerations on P2R level should be included)."
  > — ch13 Box 13.2 ^ch13-10

- Bước 2 xác định P2R: cơ quan giám sát nên kiểm tra để cùng một rủi ro chưa được phủ bởi đệm vốn hay add-on vĩ mô thận trọng khác.
  > "At this stage the competent authorities should check that the same risk isn ' t already covered by other specific capital buffer requirements and/or additional macroprudential add-ons."
  > — ch13 Box 13.2 ^ch13-11

- Bước 3: xác định tổng yêu cầu vốn SREP bằng số tuyệt đối từ bước 1–2, rồi quy ra tỷ lệ TSCR.
  > "At first, the Total SREP Capital Requirement in absolute volume is determined, as a result of steps 1 and 2."
  > — ch13 Box 13.2 ^ch13-12

- P2G là mức và chất lượng vốn tự có ngân hàng được kỳ vọng giữ vượt OCR, xác định từ tác động stress test và đánh giá khả năng đáp ứng OCR, TSCR qua chu kỳ và khi căng thẳng.
  > "Based on assessment, whether the OCR and TSCR can be met over the economic cycle and in the stressed conditions, the P2G ratio is defined."
  > "P2G means the level and quality of own funds the institution is expected to hold in excess of its OCR, determined based on stress test impact"
  > — ch13 Box 13.2 ^ch13-13

- Khi xác định P2G, cơ quan giám sát bảo đảm P2G phủ tối thiểu tác động stress tối đa dự kiến (theo thay đổi tỷ lệ CET1 trong kịch bản bất lợi) cộng dồn qua các năm stress; P2G được bù trừ với capital conservation buffer và, tuỳ trường hợp, với countercyclical buffer, nhưng không bù trừ với systemic risk buffer.
  > "ensure that it covers at least the anticipated maximum stress impact (based on the changes in the CET1 ratio in adverse scenarios) cumulatively in all years of stress"
  > "consider how combined buffer requirements already cover risks revealed by stress testing: offset P2G against the capital conservation buffer and on a caseby-case basis against the capital contra-cyclical buffer. P2G is not offset against the systemic risk buffers, as those are intended to cover the risks an institution poses to the financial system."
  > — ch13 Box 13.2 ^ch13-14

- Mảng rủi ro thanh khoản và funding đánh giá rủi ro thanh khoản nội tại (trong ngày, ngắn và trung hạn, bình thường và căng thẳng, theo đồng tiền). ALM có thông tin này vì quản lý liquidity buffer, nhưng sẽ thận trọng hơn nếu bộ phận kiểm soát rủi ro cung cấp cho cơ quan quản lý.
  > "Inherent liquidity risk (intraday, in the short and medium term, under normal and stressed conditions, in different currencies)."
  > "it would be more prudent if this information is provided to the regulator by the risk controlling function."
  > — ch13 ^ch13-15

- Rủi ro funding nội tại gồm phụ thuộc vào nguồn funding cụ thể, chênh lệch kỳ hạn cấu trúc và thay đổi dự kiến theo kế hoạch funding. Chênh lệch kỳ hạn cấu trúc nên được điều hành trong hạn mức thanh khoản cấu trúc nêu rõ trong chính sách.
  > "Inherent funding risk, in particular banks '  funding profile and its stability. It includes dependence on specific sources of funding, structural maturity mismatch, expected change in funding risk based on the institution ' s funding plan."
  > "Structural maturity mismatch should be steered within settled structural liquidity limits, which description should be explicitly stated in the subsequent policies."
  > — ch13 ^ch13-16

- Từ đánh giá tổng thể về thanh khoản, cơ quan quản lý quyết định có áp biện pháp và yêu cầu thanh khoản riêng cho ngân hàng hay không.
  > "Based on such overall assessment of liquidity, regulators determine the need to apply specific liquidity measures  and quantify specific liquidity requirements for the bank (in addition to common requirements or their levels)."
  > — ch13 ^ch13-17

### u04 — Ch.14 Scope of ALM Involvement for Different Banks

- Box 14.1: các giai đoạn một ngân hàng có thể trải qua gồm going concern, phục hồi do ngân hàng chủ động, phục hồi và/hoặc xử lý do cơ quan có thẩm quyền chủ động, xử lý có dùng nguồn bên ngoài.
  > "By 2020 it was already clear that phases, which a bank may undergo under all possible spectra of circumstances, can be represented by the following list:"
  > "Bank-driven recovery"
  > "Authority-driven recovery and/or resolution"
  > "Resolution involving external funds"
  > — ch14 Box 14.1 ^ch14-1

- Ngân hàng nên nêu trong khung khẩu vị rủi ro các ngưỡng kích hoạt phục hồi. Ngưỡng (recovery triggers), biện pháp (recovery options), quy trình leo thang (kể cả thông báo cơ quan giám sát) và thực hiện biện pháp tạo thành recovery plan. Mỗi ngân hàng tự lập recovery plan, không dựa vào hỗ trợ của nhà nước.
  > "Banks should indicate in the risk appetite framework the levels, reaching which will trigger a recovery situation for a bank"
  > "These levels (recovery triggers) and measures (recovery options), as well as description of step-by-step process of escalation (including informing the supervisors) and execution of the recovery options, together constitute a recovery plan. Each bank is responsible for drafting a recovery plan, outlining recovery options, not applying any state support measures."
  > — ch14 Box 14.1 ^ch14-2

- Resolution plan do cơ quan có thẩm quyền lập, thường với sự hỗ trợ của ngân hàng; cơ quan xử lý quyết định chiến lược, ngân hàng chuẩn bị triển khai biện pháp.
  > "For such purposes authorities have to draft a resolution plan , usually with a help of the bank. The resolution authority defines the appropriate resolution strategy for the bank, while the bank itself is responsible for preparation of the resolution measures implementation."
  > — ch14 Box 14.1 ^ch14-3

- Chiến lược xử lý có hai lựa chọn: thanh lý thông thường theo luật phá sản, hoặc resolution theo BRRD. Cơ quan quản lý có thể chọn resolution khi chức năng trọng yếu cho nền kinh tế hoặc ổn định thị trường bị đe doạ.
  > "When regulators decide on the resolution strategy, there can be two options to consider: (a) normal liquidation (ordinary insolvency regime) and (b) resolution"
  > "Regulators may decide in favor of resolution, when by failure of this bank maintenance of critical functions for economy is endangered, or financial stability of the market is endangered."
  > — ch14 Box 14.1 ^ch14-4

- BRRD có bốn công cụ resolution: bán một phần bảng cân đối; chuyển sang tổ chức bắc cầu; tách tài sản sang "bad bank"; bail-in (bù lỗ hoặc chuyển nợ đủ điều kiện thành vốn).
  > "BRRD foresees potential implementation of four different resolution tools for resolution process:"
  > "sale of parts of the balance sheet to an investor, liquidation of the rest of the institution."
  > "transfer of parts of the balance sheet to a new legal entity, liquidation of the rest of the institution."
  > "transfer of assets and liabilities to an asset management vehicle ( ' bad bank ' ), continuation of the more focused/concentrated rest of the institution (core business and the critical functions)."
  > "off-setting of losses/conversion of eligible liabilities into equity (loss absorption and recapitalization), continuation of the institution."
  > — ch14 Box 14.1 ^ch14-5

- Để bảo đảm khả năng xử lý, ngân hàng cần đủ công cụ MREL cho nhu cầu hấp thụ lỗ và tái cấp vốn, và nên có hướng dẫn thực hiện bail-in (bail-in playbook).
  > "First, banks need to ensure that there are sufficient MREL instruments available to cover loss absorption and recapitalization needs in a resolution scenario. Second, working instructions of how loss absorption and subsequent conversion of MREL instruments into equity would be conducted (the bail-in playbook) should be elaborated."
  > — ch14 Box 14.1 ^ch14-6

- Tổ chức nhỏ và đơn giản nhất, không có chức năng trọng yếu hay liên kết với nền kinh tế, chỉ báo cáo theo lịch chuẩn, áp yêu cầu Trụ cột 1 Basel III và thanh lý thông thường khi vỡ nợ.
  > "The simplest and the smallest institutions, for which no critical functions or interconnections in the economy can be identified, stay within a standard reporting schedule and list of reports, with Basel III capital and liquidity requirements (the Pillar I requirements) and go under normal liquidation in case of default."
  > — ch14 ^ch14-7

- Ở ngân hàng nhỏ, thiếu nhân sự thường cản trở phân tách trách nhiệm, dẫn tới mơ hồ trong phân chia chức năng.
  > "In such banks situations often appear, when lack of staff prevents from proper split of responsibilities and some ambiguity in split of functions can take place."
  > — ch14 ^ch14-8

- Table 14.1 so sánh ALM ở ngân hàng thị phần lớn và nhỏ. Trích phần xung đột lợi ích và góc nhìn ALM:
  > "Table 14.1: Differences of ALM in small and large banks."
  > — ch14 Table 14.1 ^ch14-9

| | Large market share | Small market share |
|---|---|---|
| conflicts of interest | prudentially restricted and monitored | ambiguity in split of functions is not excluded |
| ALM risk management | more knowledge on regulatory framework and product characteristics is required | learning from the market is possible, time for implementation is prolonged |
| BS structure targeting | M&A activities require quantification of impact on capital and liquidity | wider angle on the balance sheet and available methods enables to construct a holistic picture |
| Price benchmarking | statistical methods are appropriate IT tools enable correct pricing of optionality of products | internally constructed models should be based on grounded assumptions |
| Resources allocation | more possibilities for resource allocation optimization | calculations can be done manually deal by deal and ensure high transparency |

- Ngân hàng nhỏ không bị cơ quan giám sát yêu cầu đánh giá hay triển khai quy định mới còn ở giai đoạn tham vấn.
  > "Second, supervisors will not require assessment or implementation of the recent regulatory developments already in a consultation stage."
  > — ch14 ^ch14-10

- Thị trường mới nổi: đồng tiền yếu, lạm phát cao, phụ thuộc một nguồn thu nhập khiến lãi suất và giá biến động mạnh, nợ dài hạn và công cụ phòng ngừa kém thanh khoản hoặc không có. Khách hàng lo âu, ra quyết định đột ngột theo cách hiểu tin tức.
  > "Weaker currencies, higher inflation, and dependency on only one economic stream of income makes these countries exposed to high volatility of interest rates and prices, illiquid or even nonexistent long-term debt and hedging instruments."
  > "It is reflected in anxious behavior of customers, who are making sudden decisions, often based on interpretation of news and not analysis of facts."
  > — ch14 §14.2 ^ch14-11

- Thị trường phát triển: khách hàng tin chính phủ và ngân hàng hơn, gắn bó trọn đời với một ngân hàng, hành vi không bốc đồng và mô hình hoá được.
  > "Overall higher level of satisfaction makes customers in such environments more reliable on governments and banks, they keep life-long relations within one bank, and their behavior is not impulse-based and can be modeled."
  > — ch14 §14.2 ^ch14-12

- Ở thị trường mới nổi, chuẩn mực địa phương có khi chặt hơn, có khi không phủ hết các khía cạnh của thông lệ tốt nhất.
  > "Meanwhile their local standards are in place, which are sometimes stricter, sometimes do not cover all aspects considered in best practice legislation."
  > — ch14 §14.2 ^ch14-13

- Thị trường phát triển: ALM quản lý bảng cân đối asset sensitive trong môi trường biên thấp, với cho vay lãi suất thả nổi và tiền gửi bán lẻ sticky; ALM phải chú ý quản lý liquidity buffer, mục tiêu chuyển hoá kỳ hạn và tái định giá tài khoản tiết kiệm.
  > "As for the  ' guardian of the balance sheet '  developed markets set for ALM a task to manage an asset sensitive balance sheet in low margins environment. For such a balance sheet floating rate loans and sticky retail deposits are a usual characteristic. Therefore, ALM has to pay precise attention to liquidity buffer management, maturity transformation targeting and saving accounts repricing."
  > — ch14 §14.2 ^ch14-14

- Thị trường mới nổi: bảng cân đối thường liability sensitive, không có swap, tài sản rất sticky, tiền gửi bán lẻ biến động hơn với phần core ổn định thấp hơn. Cơ quan giám sát không yêu cầu mô hình phức tạp; ALM thường xuyên đối mặt biến động cao, gần với vai trò trong khủng hoảng.
  > "Balance-sheet in emerging financial markets is usually liability sensitive, meaning no swaps available, assets being very sticky, retail deposits more volatile with lower core stable amount."
  > "As a result, supervisory authorities do not request highly sophisticated models covering all risk aspects to be in place"
  > "Moreover, ALM needs to deal constantly with high market volatility that makes ALM operation closer to its role and tasks in a crisis environment."
  > — ch14 §14.2 ^ch14-15

- Table 14.2 so sánh ALM ở thị trường phát triển và kém phát triển. Trích phần thị trường, khách hàng và hàm ý ALM:
  > "Table 14.2: Differences of ALM in banks operating on developed and developing markets."
  > — ch14 Table 14.2 ^ch14-16

| | Developed markets | Undeveloped markets |
|---|---|---|
| products and instruments | high availability and variety of instruments and products | lack of some instruments/products low liquidity of the market short maturities |
| customers ' behavior | customers have life-long relations with banks | lack of financial knowledge high anxiety of society, low level of trust to banks/government |
| ALM risk management | high hedging possibilities transformation result management | limited hedging possibilities |
| BS structure targeting | low margin consideration liquidity buffer management asset sensitive balance sheet composition management | high market volatility consideration liability sensitive balance sheet composition management |
| Price benchmarking | need for embedded options pricing high possibilities to construct internal curve special attention on retail saving accounts pricing targeting | simpler approaches can be applied limited possibilities to construct internal curve |
| Resources allocation | multi-dimensional resource allocation optimization (many criteria available) | very straightforward principles for resource allocation can be applied |

### u04 — Ch.15 ALM Role in Crisis

- Trong khủng hoảng, ALM tham gia mọi mảng: thanh khoản và funding, mức đủ vốn, IRRBB và FTP. Mỗi mảng nên có kế hoạch hành động định sẵn theo mức độ nghiêm trọng.
  > "It embraces all areas of ALM: liquidity and funding; capital adequacy; IRRBB and the FTP. In general, for each area there ' s a predefined plan of actions that should be applied if there is an increase of severity of the crisis."
  > — ch15 ^ch15-1

- Ngân hàng sống được một năm không có lợi nhuận nhưng không sống được một ngày thiếu thanh khoản.
  > "A bank can survive a year without profit but will not survive even a day without liquidity."
  > — ch15 ^ch15-2

- Bước đầu của thứ tự hành động thanh khoản là tái định giá tiền gửi doanh nghiệp/bán lẻ; tăng mạnh lãi suất tiền gửi có thể vừa giảm NII vừa không giữ được thanh khoản vì khách hàng đọc là tín hiệu SOS.
  > "Corporate/retail deposits repricing (down) should be initiated, in order to maintain liquidity on the sufficient stable level."
  > "For example, significant increase of interest rates on deposits can not only harm the net interest result, but also fail to achieve the aim of maintaining liquidity  -  the customers may consider this as an SOS-signal of a bank balancing on the edge of survival."
  > — ch15 ^ch15-3

- Các bước tiếp theo: đàm phán gia hạn/vay mới trung dài hạn với tổ chức tài chính; chuẩn bị hỗ trợ thanh khoản từ công ty mẹ; chuẩn bị chuyển nhượng khoản vay khi rất khẩn cấp; cuối cùng là yêu cầu khách hàng trả nợ trước, biện pháp ảnh hưởng uy tín nhất.
  > "Negotiations with other financial institutions on prolongation/new placements of middle- and long-term funding should be started."
  > "For banks having the mother company (see Chapter 12), a short- or middle-term liquidity support from the head office should be prealigned."
  > "For extremely urgent cases loan transfers to the head office or other financial institutions should be prepared."
  > "As a very ultimate measure, initiation of asset repayment by clients should be executed. This measure, more than the other, impacts the bank ' s reputation and hinders its further recovery."
  > — ch15 ^ch15-4

- Kế hoạch hành động về vốn trong khủng hoảng gồm: lượng hoá tác động lên vốn; ước tính mức vốn sau tác động so với yêu cầu; chuẩn bị biện pháp bù thiếu hụt; ước tính thặng dư/thiếu hụt sau biện pháp.
  > "Quantification of the potential capital hit from different factors, such as:"
  > "Estimation of the capital levels after the impacts and comparison to the regulatory requirements."
  > "Preparation of actions to counterbalance the potential capital shortfall:"
  > "Estimation of capital surplus/shortfall after all actions."
  > — ch15 ^ch15-5

- Nguồn tác động lên vốn gồm: nội tệ mất giá làm tăng RWA của khoản vay bằng ngoại tệ mạnh; moratorium; trích lập dự phòng; đánh giá lại danh mục trái phiếu qua OCI.
  > "Depreciation of domestic currency against strong currencies will mean that portion of strong currency denominated loans (and, thus, RWA) will increase  having negative impact on capital adequacy."
  > "Other impacts, including bond portfolio revaluation (and impacting capital through OCI), expected additional taxes/other losses, etc."
  > — ch15 ^ch15-6

- Biện pháp bù thiếu hụt vốn gồm tối ưu RWA, chuyển RWA cho công ty mẹ hoặc tổ chức khác, và cuối cùng là xin bơm vốn.
  > "As in the case of loan transfers for liquidity purposes, RWA transfers to the head office or other financial institutions can be done."
  > "As a last resort, applications for capital injections of different forms should be prepared."
  > — ch15 ^ch15-7

- Để khuyến khích huy động và hạn chế cho vay, đường cong FTP phải được định giá lại và/hoặc áp steering margin; điều chỉnh độ dốc đường cong FTP để quản lý tác động bất lợi của kết quả chuyển hoá kỳ hạn lên NII.
  > "In particular, to stimulate deposits collection and de-stimulate lending, FTP curves must be revaluated accordingly and/or a steering margin can be applied. It is important to take into account maturity transformation result (in particular, coming from maturities mismatch of assets and liabilities)  -  and through the adjustment of steepness of the FTP curve manage the scale of possible negative impacts on the net interest result."
  > — ch15 ^ch15-8

- Biện pháp phục hồi nên được đánh giá lại liên tục, xem ngân hàng đã dùng biện pháp nào khi duy trì thanh khoản, vốn hay kết quả tài chính.
  > "Fourth, the recovery measures should be constantly reassessed, whether some of them were already applied by the bank in the process of liquidity, capital, or financial result maintenance."
  > — ch15 ^ch15-9

### u04 — Ch.16 After-Crisis ALM

- Hướng dẫn ECB tháng 11/2018 gọi cách tiếp cận tuân thủ tỷ lệ quy định là normative perspective và yêu cầu liên kết với economic perspective; từ đó normative perspective không còn được coi là đủ.
  > "In November 2018 ECB issued guidance"
  > "where named this approach the normative perspective, outlining also its necessary interconnection to the opposed to it economic perspective. From then on, the normative (regulatory) perspective officially was not considered sufficient on its own anymore, and prudent asset and liability management always appeared to be informed by the economic perspective."
  > — ch16 §16.1 ^ch16-1

- Khi xây biện pháp quản lý, ALM nên xét kết quả theo economic perspective: dòng ra thanh khoản và tổn thất vốn trong kịch bản xấu nhất giả định mà normative perspective không phản ánh.
  > "While elaborating credible management actions, ALM should take into account results of assessment according to the economic perspective as well: in particular, outflows of liquidity and/or losses impacting capital in hypothetical worst-case scenarios, which were not captured in the normative perspective."
  > — ch16 §16.1 ^ch16-2

- Bản chất kinh tế cũng là một phần của IRRBB: xét cả tác động ngắn hạn lên lợi nhuận lẫn EVE trên toàn bộ vòng đời.
  > "Economic nature of financial categories is also a part of IRRBB (see Box 11.2), which takes into account not only the short-term effects on profitability, but also the economic value of the institution ' s equity on the whole horizon of its existence."
  > — ch16 §16.1 ^ch16-3

- Yêu cầu báo cáo khác nhau theo quy mô: khoảng 600 điểm dữ liệu một năm với ngân hàng nhỏ so với gần 40.000 với tập đoàn lớn.
  > "starting from different reporting requests (600 data points for small banks as opposed to almost 40,000 for large banking groups a year"
  > — ch16 §16.2 ^ch16-4

- Box 16.1: lập kế hoạch vốn gồm xác định vốn tự có, RWA, CAR và so với yêu cầu để ra thặng dư. Khi có yêu cầu theo loại phơi nhiễm như CCyB, thêm bước tính CCyB bình quân gia quyền theo RWA cho tập đoàn và cộng vào yêu cầu: 8% Trụ cột 1 + 2,5% CCB + CCyB tập đoàn.
  > "Definition of own funds absolute amount"
  > "Opposing of the calculated CAR to the regulatory (or internal) requirement and determination of available surplus"
  > "During Step 4a (in the table) a weighted average CCyB for the banking group is calculated: (RWA Hong Kong * CCyB Hong Kong + RWA Luxemburg * CCyB Luxemburg)/RWA total. At Step 4b the calculated CCyB for the group is added to capital requirements: Pillar 1 requirement 8% + capital conservation buffer 2,5% + CCyB Group."
  > — ch16 Box 16.1 ^ch16-5

- Output floor là sàn cho RWA tính bằng mô hình nội bộ, với lộ trình chuyển tiếp 5 năm theo BCBS bắt đầu từ 2022.
  > "a lower limit for the risk-weighted assets that banks calculate with their internal models, giving them the freedom to use internal models while at the same time introducing a  ' safeguard. '  As many other regulatory updates, the output floor will have a gradual 5-year transitional phase-in, according to the BCBS, starting in 2022"
  > "Table 16.2: Output floor phase-in."
  > — ch16 §16.2, Table 16.2 ^ch16-6

| Output floor | 50% | 55% | 60% | 65% | 70% | 72.5% |
|---|---|---|---|---|---|---|
| Phase-in | 1 January 2022 | 1 January 2023 | 1 January 2024 | 1 January 2025 | 1 January 2026 | 1 January 2027 |

- Phơi nhiễm với quốc gia, ngành có thể bị khủng hoảng phi tài chính nên được theo dõi riêng trong dự báo vốn và kế hoạch kinh doanh; stress test nên có kịch bản cho các phơi nhiễm này.
  > "Exposures to countries, sectors, economies, which could be damaged by non-financial crisis, should be separately observed as components of capital forecasting and business planning, stress tests should incorporate scenarios, which would assess the scale of possible disasters connected with these types of exposures."
  > — ch16 §16.3 ^ch16-7

- Ngân hàng được thanh lý thông thường thì không có yêu cầu MREL bổ sung ngoài vốn tự có. MREL target gồm LAA (yêu cầu vốn trong kịch bản căng thẳng, P1 + P2R), RCA (P1 + P2R sau khi vốn ban đầu bị tiêu hết) và MCC (CBR trừ phần CCyB), theo logic SRB cập nhật 2020.
  > "If the competent authority has revealed neither any critical service, which the bank executes, nor financial stability endangerment, the institution can go under common liquidation, and no additional MREL requirements on top of the own funds will be imposed."
  > "MREL target consists of loss absorbency amount (LAA, equal to capital requirements under stressed scenario, consisting of P1 + P2R), recapitalization amount (RCA, representing requirements for stressed conditions P1 + P2R, after the initial capital is fully consumed by the loss) and market confidence charge (MCC, equal to CBR less the amount maintained to meet the CCyB), according to updated in 2020 SRB logic."
  > — ch16 §16.4 ^ch16-8

- Khi add-on resolution vượt thặng dư vốn, ALM chịu trách nhiệm huy động nguồn đủ chuẩn MREL và duy trì qua chu kỳ. Điều kiện cơ bản: kỳ hạn còn lại trên một năm, không phải tiền gửi (bán lẻ) được bảo hiểm, không phải nợ với cơ quan nhà nước hay bảo hiểm xã hội, không do chính ngân hàng mua lại.
  > "If the  ' resolution '  add-ons are higher than the capital surplus of the bank, ALM is responsible to raise MREL eligible funding, and to maintain MREL amount on a sufficient level through the cycle."
  > "(including residual maturity in more than one year, not (retail) deposits covered by Deposit Guarantee Scheme, DGS, not liabilities against authorities or social insurance, not purchased by the institution itself)"
  > — ch16 §16.4 ^ch16-9

- Digitalization cho phép người gửi tiền chuyển ngân hàng bằng vài cú click, nên tiền gửi kém tin cậy hơn như nguồn funding; điều này nên được phản ánh trong mô hình ALM và biện pháp duy trì thanh khoản.
  > "Digitalization might affect funding, with new digital tools allowing depositors to switch banks by means of a few clicks. That implies that deposits are becoming a less reliable source of funding, what should be accounted in ALM models and liquidity maintenance measures."
  > — ch16 §16.5 ^ch16-10

- M&A: vị thế thanh khoản sau giao dịch bằng tổng (hiệu) vị thế thanh khoản hai pháp nhân trừ (cộng) giá trả (nhận) tại ngày hoàn tất; LCR nên được tính cho từng pháp nhân mới.
  > "The  ' liquidity '  amount equals the sum (a difference) of liquidity positions of the two entities minus (plus) the amount paid (received) for the investment (disentanglement) at the date of closing the deal."
  > "LCR or subsequent other liquidity requirement should be calculated for each new entity and when needed appropriate actions should be elaborated."
  > — ch16 §16.6 ^ch16-11

- Khi bán: IFRS 5 đo tài sản theo giá trị thấp hơn giữa giá trị ghi sổ và giá trị hợp lý trừ chi phí bán, nên lỗ giao dịch được ghi nhận ngay và tác động lên vốn.
  > "Shortly, IFRS 5 prescribes that assets must be measured as lower of their carrying amount and fair value less the costs to sell. That means that the financial result of the deal, when negative, should be immediately booked in financial statements and impact capital calculations."
  > — ch16 §16.6 ^ch16-12

- Khi mua: theo IFRS 3, ngày mua là ngày bên mua nắm quyền kiểm soát; goodwill dương được ghi nhận là tài sản vô hình và trừ khỏi vốn tự có.
  > "according to IFRS 3, the acquisition date is the date on which the acquirer obtains control over another entity."
  > "For own funds calculation purpose, if goodwill is positive, it is recognized as an intangible asset and is deducted from own funds."
  > — ch16 §16.6 ^ch16-13

- Sau hợp nhất, P2R và P2G của pháp nhân hợp nhất trong trường hợp thông thường là bình quân gia quyền của mức áp cho hai pháp nhân trước hợp nhất (theo hướng dẫn ECB).
  > "the capital requirements in terms of P2R and P2G for a consolidated entity in general cases will be the weighted average of the P2R and P2G levels applicable to the two entities prior to the consolidation"
  > — ch16 §16.6 ^ch16-14

## Node bị ảnh hưởng
- Tạo mới: [[irrbb-management]], [[alm-operating-model]], [[srep]].
- Cập nhật (draft): [[alco]], [[three-lines-of-defence]], [[icaap]], [[risk-appetite]], [[structural-hedging]], [[funds-transfer-pricing]].
- Đề xuất (canonical): [[gap-risk]], [[net-interest-income-sensitivity]], [[non-maturity-deposits]].
- u04 — tạo mới: [[recovery-and-resolution-planning]], [[mrel]]; cập nhật: [[srep]], [[icaap]], [[irrbb-management]], [[alm-operating-model]], [[capital-plan]], [[funds-transfer-pricing]], [[liquidity-risk-management]]; đề xuất: [[contingency-funding-plan]], [[non-maturity-deposits]].

## Mâu thuẫn ghi nhận
- Không có conflict cùng phạm vi. Khác biệt: Table 11.2 coi business lines không phải tuyến bảo vệ và xếp ALM/Treasury vào tuyến 1, trong khi TT83/2025 Đ4.2 xếp bộ phận tạo rủi ro vào tuyến 1 (khác jurisdiction và loại nguồn, ghi ở [[three-lines-of-defence]]).
- Output floor (^ch16-6): Bardaeva ghi lộ trình bắt đầu từ 2022 theo BCBS; wiki chưa có văn bản BCBS về output floor để đối chiếu [cần nguồn].
- Horizon earnings 3–4 năm (^ch11-16) là thực hành nội bộ, khác horizon ΔNII chuẩn hoá của d368; khác scope, không phải mâu thuẫn.

## Ghi chú convert
- Table 10.1 và 10.2 bị tách đôi (phần gone concern thành bảng riêng không có cột tầm); bảng ở ^ch10-5 ghép lại theo thứ tự hàng trong raw. Chữ "non-shaded" trong raw ám chỉ ô tô màu đã mất khi convert, nên không xác định được ô nào thuộc front office và ô nào thuộc middle office.
- Figure 12.1, 12.2 là `<!-- image -->`; chỉ còn bảng mô tả lớp vốn.
- Raw tách câu qua dòng trống ở một số chỗ (dòng 997/999, 1010/1012, 1160/1162); trích dẫn dừng trước chỗ ngắt.
- u04: công thức tỷ lệ TSCR (dòng 1307) bị vỡ phân số, không trích. Table 16.2 (output floor) lệch ô năm 2022/2023 ("1 January 2022 1 2023 | January"); bảng ở ^ch16-6 ghép lại theo thứ tự. Bảng Figure 16.2–16.5 (M&A) vỡ cột, không chép. Danh sách thứ tự hành động thanh khoản ở Ch.15 bị đánh số lại sai (1, 2, 3, 2, 5, 3, 4, 5).
