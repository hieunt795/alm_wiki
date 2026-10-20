---
title: "BCBS — Principles for Sound Liquidity Risk Management and Supervision (BCBS 144)"
aliases: []
type: source
source_id: src-bcbs-liquidity-principles-2008
domains: [basel, alm]
status: active
maturity: draft
tier: T2
doc_status: final
issuer: BCBS
published:
effective:
raw: 01_sources/alm/Basel/BCBS144/bcbs144.md
units_done: [p01, p02, p03, p04, p10, p11]
updated: 2026-10-20
---

## Thông tin nguồn
- Issuer: Basel Committee on Banking Supervision ([[bcbs]]).
- Tier T2, `doc_status: final`. Bìa ghi September 2008; không có ngày ban hành cụ thể nên `published` để trống.
- Cấu trúc: 17 nguyên tắc. P1 nguyên tắc nền; P2–P4 quản trị; P5–P12 đo lường và quản lý (P10 stress test, P11 CFP, P12 đệm tài sản thanh khoản); P13 công bố thông tin; P14–P17 vai trò cơ quan giám sát.
- Được dẫn chiếu tại LCR10.3, NSF10.5, SRP30.48 và SRP50 của Basel Framework.
- Raw: `01_sources/alm/Basel/BCBS144/bcbs144.md` (641 dòng, docling, không có `_meta.json`).
- Conversion: partial (xem `03_meta/sources.yaml`).
- Node regulation tương ứng: [[bcbs-liquidity-principles]].

## Tóm tắt
BCBS 144 đặt 17 nguyên tắc quản trị và giám sát rủi ro thanh khoản sau giai đoạn biến động 2007. Văn bản không dùng thuật ngữ ILAAP, nhưng các thành phần của quy trình tự đánh giá mức đủ thanh khoản đều có ở đây: khung quản trị rủi ro thanh khoản và đệm tài sản thanh khoản (P1), liquidity risk tolerance (P2), stress test theo nhiều kịch bản (P10), kế hoạch tài trợ dự phòng (P11). Phần đã ingest: P1–P4, P10, P11.

## Key claims

### p01 — Principle 1: nguyên tắc nền

- Ngân hàng chịu trách nhiệm quản trị rủi ro thanh khoản; nên có khung quản trị vững chắc bảo đảm đủ thanh khoản, gồm đệm tài sản thanh khoản cao không bị cầm cố, để chịu nhiều sự kiện stress kể cả mất nguồn vốn có và không có bảo đảm; cơ quan giám sát nên đánh giá cả khung quản trị lẫn vị thế thanh khoản.
  > "A bank is responsible for the sound management of liquidity risk. A bank should establish a robust liquidity risk management framework that ensures it maintains sufficient liquidity, including a cushion of unencumbered, high quality liquid assets, to withstand a range of stress events, including those involving the loss or impairment of both unsecured and secured funding sources."
  > "Supervisors should assess the adequacy of both a bank's liquidity risk management framework and its liquidity position and should take prompt action if a bank is deficient in either area"
  > — P1 ^lrm-p01

- Khung quản trị rủi ro thanh khoản nên tích hợp vào quản trị rủi ro toàn hàng; mục tiêu chính là bảo đảm với độ tin cậy cao ngân hàng vừa đáp ứng nghĩa vụ hằng ngày vừa chịu được giai đoạn stress thanh khoản (riêng ngân hàng hoặc toàn thị trường).
  > "A bank should establish a robust liquidity risk management framework that is well integrated into the bank-wide risk management process. A primary objective of the liquidity risk management framework should be to ensure with a high degree of confidence that the firm is in a position to both address its daily liquidity obligations and withstand a period of liquidity stress affecting both secured and unsecured funding, the source of which could be bank-specific or market-wide."
  > — para 8 ^lrm-8

- Ngân hàng nên chứng minh đệm thanh khoản tương xứng với độ phức tạp hoạt động nội và ngoại bảng, thanh khoản của tài sản và nợ, mức chênh lệch funding và chiến lược funding; nên dùng giả định thận trọng về khả năng bán tài sản và tiếp cận nguồn vốn khi stress; không để áp lực cạnh tranh làm suy yếu quản trị rủi ro thanh khoản.
  > "A bank should demonstrate that its liquidity cushion is commensurate with the complexity of its on- and off-balance sheet activities, the liquidity of its assets and liabilities, the extent of its funding mismatches and the diversity of its business mix and funding strategies."
  > "A bank should use appropriately conservative assumptions about the marketability of assets and its access to funding, both secured and unsecured, during periods of stress."
  > "a bank should not allow competitive pressures to compromise the integrity of its liquidity risk management, control functions, limit systems and liquidity cushion."
  > — para 8 ^lrm-8b

- Ngân hàng có vốn mạnh vẫn có thể gặp vấn đề thanh khoản; vấn đề thanh khoản thường tần suất thấp nhưng tác động lớn; kỳ vọng hỗ trợ của NHTW và bảo hiểm tiền gửi có thể làm giảm động cơ quản trị thanh khoản thận trọng; cơ quan giám sát nên hành động nếu ngân hàng không giữ đủ thanh khoản để sống qua stress nghiêm trọng.
  > "Even though strong capital positions reduce the likelihood of liquidity pressure, apparently solvent banks can suffer liquidity problems. Liquidity problems are typically low frequency but potentially high impact events"
  > "an expectation that central banks will provide liquidity support, alongside the guarantees to depositors provided by deposit insurance, could diminish the incentives of the bank to manage its liquidity as conservatively as it should."
  > "supervisors should assess whether each bank manages liquidity risk robustly to maintain sufficient liquidity and should take supervisory action if a bank is not holding sufficient liquidity to enable it to survive a period of severe liquidity stress."
  > — para 9 ^lrm-9

### p02 — Principle 2: liquidity risk tolerance

- Ngân hàng nên nêu rõ liquidity risk tolerance phù hợp chiến lược kinh doanh và vai trò trong hệ thống tài chính.
  > "A bank should clearly articulate a liquidity risk tolerance that is appropriate for the business strategy of the organisation and its role in the financial system."
  > — P2 ^lrm-p02

- HĐQT chịu trách nhiệm cuối cùng về rủi ro thanh khoản nên đặt tolerance; tolerance xác định mức rủi ro thanh khoản ngân hàng sẵn sàng chấp nhận, phản ánh tình hình tài chính và năng lực funding, bảo đảm quản lý chặt trong điều kiện thường để chịu được stress kéo dài; nên được diễn đạt để mọi cấp quản lý hiểu đánh đổi rủi ro – lợi nhuận.
  > "A bank should set a liquidity risk tolerance in light of its business objectives, strategic direction and overall risk appetite. The board of directors is ultimately responsible for the liquidity risk assumed by the bank and the manner in which this risk is managed and therefore should establish the bank's liquidity risk tolerance."
  > "The tolerance, which should define the level of liquidity risk that the bank is willing to assume, should be appropriate for the business strategy of the bank and its role in the financial system and should reflect the bank's financial condition and funding capacity."
  > "The tolerance should ensure that the firm manages its liquidity strongly in normal times in such a way that it is able to withstand a prolonged period of stress. The risk tolerance should be articulated in such a way that all levels of management clearly understand the trade-off between risks and profits."
  > — para 10 ^lrm-10

- Tolerance có thể diễn đạt định tính hoặc định lượng, ví dụ bằng mức rủi ro thanh khoản funding chưa giảm thiểu ngân hàng chấp nhận trong điều kiện thường và stress; cơ quan giám sát đánh giá tính phù hợp của tolerance (P14).
  > "For example, a bank may quantify its liquidity risk tolerance in terms of the level of unmitigated funding liquidity risk the bank decides to take under normal and stressed business conditions."
  > "As discussed in Principle 14, supervisors will assess the appropriateness of the bank's risk tolerance and any changes to the risk tolerance over time."
  > — para 10 ^lrm-10b

### p03 — Principle 3: chiến lược, chính sách, vai trò HĐQT và ban điều hành

- Ban điều hành nên xây chiến lược, chính sách, thực hành quản lý rủi ro thanh khoản theo tolerance, liên tục theo dõi và báo cáo HĐQT định kỳ; HĐQT nên rà soát và phê duyệt chiến lược, chính sách, thực hành ít nhất hằng năm.
  > "Senior management should develop a strategy, policies and practices to manage liquidity risk in accordance with the risk tolerance and to ensure that the bank maintains sufficient liquidity. Senior management should continuously review information on the bank's liquidity developments and report to the board of directors on a regular basis."
  > "should review and approve the strategy, policies and practices related to the management of liquidity at least annually and ensure that senior management manages liquidity risk effectively."
  > — P3 ^lrm-p03

- Chiến lược nên có chính sách cụ thể về: cơ cấu và kỳ hạn tài sản, nợ; độ đa dạng và ổn định nguồn vốn; quản lý theo đồng tiền, biên giới, mảng kinh doanh, pháp nhân; quản lý trong ngày; giả định về thanh khoản của tài sản; xét cả điều kiện thường và stress; có thể gồm mục tiêu định lượng và định tính.
  > "The strategy should include specific policies on liquidity management, such as: the composition and maturity of assets and liabilities; the diversity and stability of funding sources; the approach to managing liquidity in different currencies, across borders, and across business lines and legal entities; the approach to intraday liquidity management; and the assumptions on the liquidity and marketability of assets."
  > "The strategy may include various high-level quantitative and qualitative targets. The board of directors should approve the strategy and critical policies and practices and review them at least annually."
  > — para 11 ^lrm-11

- HĐQT nên bảo đảm ban điều hành chuyển chiến lược thành hướng dẫn tác nghiệp, có chuyên môn, quy trình và hệ thống đo lường, kiểm soát mọi nguồn rủi ro thanh khoản; "HĐQT" và "ban điều hành" là nhãn của hai chức năng ra quyết định.
  > "The board should ensure that senior management translates the strategy into clear guidance and operating standards (eg in the form of policies, controls or procedures)."
  > "the notions of the board of directors and senior management are used in this paper not to identify legal constructs but rather to label two decision-making functions within a bank."
  > — para 11, fn 4 ^lrm-11b

- Chiến lược nên tương xứng với bản chất, quy mô, độ phức tạp; xét cấu trúc pháp lý (chi nhánh hay công ty con ở nước ngoài), thị trường, sản phẩm và yêu cầu quy định nước sở tại và nước chủ quản.
  > "The liquidity strategy should be appropriate for the nature, scale and complexity of a bank's activities."
  > "the bank should take into consideration its legal structures (eg mix of foreign branches versus foreign operating subsidiaries), key business lines, the breadth and diversity of markets, products, and jurisdictions in which it operates, and home and host regulatory requirements."
  > — para 12 ^lrm-12

- Ban điều hành nên xác định cấu trúc, trách nhiệm và kiểm soát cho mọi pháp nhân, chi nhánh, công ty con; mức tập trung hay phân tán nên tính hạn chế pháp lý, quy định, vận hành về chuyển vốn; ban điều hành nên theo dõi được rủi ro thanh khoản toàn tập đoàn và từng pháp nhân liên tục.
  > "Senior management should determine the structure, responsibilities and controls for managing liquidity risk and for overseeing the liquidity positions of all legal entities, branches and subsidiaries in the jurisdictions in which a bank is active"
  > "The structure for managing liquidity (ie the degree of centralisation or decentralisation of a bank's liquidity risk management) should take into consideration any legal, regulatory or operational restrictions on the transfer of funds."
  > "Whatever structure is employed, senior management should be able to monitor the liquidity risks across the banking group and at each entity on an ongoing basis."
  > — para 13 ^lrm-13

- Ban điều hành và HĐQT nên hiểu liên kết giữa rủi ro thanh khoản funding và thanh khoản thị trường, và tác động của rủi ro tín dụng, thị trường, hoạt động, danh tiếng lên chiến lược thanh khoản; rủi ro thanh khoản nên nằm trong phạm vi của uỷ ban quản lý rủi ro hoặc chức năng quản lý rủi ro độc lập.
  > "senior management and the board should have a thorough understanding of the close links between funding liquidity risk and market liquidity risk, as well as how other risks, including credit, market, operational and reputation risks affect the bank's overall liquidity risk strategy."
  > "liquidity risk and its potential interaction with other risks should be included in the risks addressed by risk management committees and/or independent risk management functions."
  > — para 14–15 ^lrm-14

- Mọi đơn vị kinh doanh có hoạt động tác động tới thanh khoản nên nắm chiến lược và hoạt động theo chính sách, quy trình, hạn mức, kiểm soát đã duyệt.
  > "All business units conducting activities that have an impact on liquidity should be fully aware of the liquidity strategy and operate under the approved policies, procedures, limits and controls."
  > — para 15 ^lrm-15

- Ban điều hành nên bảo đảm kiểm soát nội bộ do nhân sự độc lập về vận hành thực hiện; nhân sự kiểm soát độc lập phải có kỹ năng và thẩm quyền phản biện thông tin và giả định mô hình của mảng kinh doanh; kiểm toán nội bộ nên rà soát định kỳ khung kiểm soát rủi ro thanh khoản.
  > "Senior management should ensure that operationally independent, appropriately trained and competent personnel are responsible for implementing internal controls. It is critical that personnel in independent control functions have the skills and authority to challenge information and modelling assumptions provided by business lines."
  > "Internal audit should regularly review the implementation and effectiveness of the agreed framework for controlling liquidity risk."
  > — para 16 ^lrm-16

- Ban điều hành nên xác định thủ tục và thẩm quyền cho ngoại lệ chính sách, hạn mức, gồm leo thang và xử lý vi phạm hạn mức; bảo đảm stress test, CFP và đệm thanh khoản hiệu quả.
  > "Senior management should define the specific procedures and approvals necessary for exceptions to policies and limits, including the escalation procedures and follow-up actions to be taken for breaches of limits."
  > "Senior management should ensure that stress tests, contingency funding plans and liquidity cushions are effective and appropriate for the bank"
  > — para 17 ^lrm-17

- HĐQT nên xem xét báo cáo định kỳ về vị thế thanh khoản và được báo ngay về dấu hiệu mới: chi phí funding hoặc tập trung tăng, khoảng trống funding lớn dần, nguồn thanh khoản thay thế cạn, vi phạm hạn mức trọng yếu hoặc kéo dài, đệm tài sản thanh khoản giảm đáng kể, thay đổi thị trường.
  > "The board should review regular reports on the liquidity position of the bank. The board should be informed immediately of new or emerging liquidity concerns. These include increasing funding costs or concentrations, the growing size of a funding gap, the drying up of alternative sources of liquidity, material and/or persistent breaches of limits, a significant decline in the cushion of unencumbered, highly liquid assets, or changes in external market conditions which could signal future difficulties."
  > — para 18 ^lrm-18

### p04 — Principle 4: chi phí thanh khoản trong định giá nội bộ

- Ngân hàng nên đưa chi phí, lợi ích, rủi ro thanh khoản vào định giá nội bộ, đo lường hiệu quả và duyệt sản phẩm mới cho mọi hoạt động trọng yếu (nội và ngoại bảng), để động cơ chấp nhận rủi ro của từng mảng khớp với rủi ro thanh khoản chúng tạo ra cho toàn ngân hàng.
  > "A bank should incorporate liquidity costs, benefits and risks in the internal pricing, performance measurement and new product approval process for all significant business activities (both on- and off-balance sheet), thereby aligning the risk-taking incentives of individual business lines with the liquidity risk exposures their activities create for the bank as a whole."
  > — P4 ^lrm-p04

- Quy trình nên đo chi phí, lợi ích, rủi ro thanh khoản ngầm trong mọi hoạt động trọng yếu, kể cả cam kết tiềm tàng chưa tác động trực tiếp lên bảng cân đối; chúng nên được phân bổ tường minh cho hoạt động liên quan, với liquidity charge gán cho trạng thái, danh mục hoặc giao dịch.
  > "Senior management should ensure that a bank's liquidity management process includes measurement of the liquidity costs, benefits and risks implicit in all significant business activities, including activities that involve the creation of contingent exposures which may not immediately have a direct balance sheet impact."
  > "These costs, benefits and risks should then be explicitly attributed to the relevant activity so that line management incentives are consistent with and reinforce the overarching liquidity risk tolerance and strategy of the bank, with a liquidity charge assigned as appropriate to positions, portfolios, or individual transactions."
  > — para 19 ^lrm-19

- Phân bổ nên xét thời gian nắm giữ dự kiến của tài sản và nợ, đặc tính rủi ro thanh khoản thị trường, và lợi ích từ nguồn vốn tương đối ổn định như một số loại tiền gửi bán lẻ.
  > "This assignment of liquidity costs, benefits and risks should incorporate factors related to the anticipated holding periods of assets and liabilities, their market liquidity risk characteristics, and any other relevant factors, including the benefits from having access to relatively stable sources of funding, such as some types of retail deposits."
  > — para 19 ^lrm-19b

- Việc định lượng và phân bổ nên tường minh, minh bạch ở cấp quản lý mảng và xét thanh khoản trong điều kiện stress; khung phân tích nên được rà soát theo thay đổi thị trường; chi phí thanh khoản nên được xét tường minh trong duyệt sản phẩm mới.
  > "The quantification and attribution of these risks should be explicit and transparent at the line management level and should include consideration of how liquidity would be affected under stressed conditions."
  > "The analytical framework should be reviewed as appropriate to reflect changing business and financial market conditions and so maintain the appropriate alignment of incentives. Moreover, liquidity risk costs, benefits and risks should be addressed explicitly in the new product approval process."
  > — para 20–21 ^lrm-20

### p10 — Principle 10: stress test

- Ngân hàng nên stress test định kỳ với kịch bản ngắn hạn và kéo dài, riêng ngân hàng và toàn thị trường (đơn lẻ và kết hợp) để nhận diện nguồn căng thẳng và bảo đảm phơi nhiễm phù hợp liquidity risk tolerance; nên dùng kết quả để điều chỉnh chiến lược, chính sách, vị thế và xây dựng kế hoạch dự phòng.
  > "A bank should conduct stress tests on a regular basis for a variety of short-term and protracted institution-specific and market-wide stress scenarios (individually and in combination) to identify sources of potential liquidity strain and to ensure that current exposures remain in accordance with a bank's established liquidity risk tolerance."
  > "A bank should use stress test outcomes to adjust its liquidity risk management strategies, policies and positions and to develop effective contingency plans."
  > — P10 ^lrm-p10

- Stress test nên phân tích tác động lên dòng tiền, vị thế thanh khoản, lợi nhuận và khả năng thanh toán; kết quả nên được ban điều hành thảo luận và làm cơ sở cho hành động khắc phục, xây đệm thanh khoản, điều chỉnh hồ sơ thanh khoản theo tolerance; stress test và kế hoạch dự phòng gắn chặt với nhau.
  > "A bank should perform stress tests or scenario analyses on a regular basis in order to identify and quantify its exposures to possible future liquidity stresses, analysing possible impacts on the institution's cash flows, liquidity position, profitability and solvency."
  > "The results of stress tests should also play a key role in shaping the bank's contingency planning and in determining the strategy and tactics to deal with events of liquidity stress. As a result, stress testing and contingency planning are closely intertwined."
  > — para 94 ^lrm-94

- Stress test nên phân tích tác động ở cấp hợp nhất, từng pháp nhân và mảng kinh doanh; ngân hàng nên cân nhắc test bổ sung cho công ty con, chi nhánh có rủi ro thanh khoản lớn; nên xét nhiều kỳ hạn, kể cả trong ngày.
  > "Stress tests should enable a bank to analyse the impact of stress scenarios on its consolidated group-wide liquidity position as well as on the liquidity position of individual entities and business lines."
  > "Tests should consider the implication of the scenarios across different time horizons, including on an intraday basis."
  > — para 95 ^lrm-95

- Mức độ và tần suất test nên tương xứng với quy mô, mức rủi ro thanh khoản và tầm quan trọng hệ thống; ngân hàng nên có khả năng tăng tần suất khi thị trường biến động hoặc theo yêu cầu cơ quan giám sát; ban điều hành nên đòi hỏi kịch bản khắt khe cả khi thanh khoản dồi dào.
  > "The extent and frequency of testing should be commensurate with the size of the bank and its liquidity risk exposures, as well as with the relative importance of the bank within the financial systems in which it operates."
  > "Senior management should demand that rigorous and challenging stress scenarios be considered, even in times when liquidity is plentiful."
  > — para 96–97 ^lrm-96

- Kịch bản nên phản ánh rủi ro funding và thanh khoản thị trường chính của ngân hàng; lịch sử chỉ là một căn cứ; kịch bản nên gồm cạn thanh khoản đồng thời ở nhiều thị trường, hạn chế nghiêm trọng tiếp cận vốn có và không có bảo đảm, hạn chế chuyển đổi tiền tệ, gián đoạn vận hành hoặc thanh toán.
  > "In designing stress scenarios, the nature of the bank's business, activities and vulnerabilities should be taken into consideration so that the scenarios incorporate the major funding and market liquidity risks to which the bank is exposed."
  > "History may serve as one guide when designing stress tests; however, historical events may not prove to be a good predictor of future events."
  > "including: a simultaneous drying up of market liquidity in several previously highly liquid markets; severe constraints in accessing secured and unsecured funding; restrictions on currency convertibility; and severe operational or settlement disruptions affecting one or more payment or settlement systems."
  > — para 98–99 ^lrm-98

- Ngân hàng nên xét liên kết giữa suy giảm thanh khoản thị trường và hạn chế thanh khoản funding, và tương tác với stress test của các loại rủi ro khác.
  > "A bank should specifically take into account the link between reductions in market liquidity and constraints on funding liquidity."
  > "A bank should also consider the insights and results of stress tests performed for various other risk types when stress testing its liquidity position and consider possible interactions with these other types of risk."
  > — para 100 ^lrm-100

- Stress có thể đồng thời tạo nhu cầu thanh khoản khẩn cấp ở nhiều đồng tiền và hệ thống thanh toán; test nên phản ánh thời gian thanh toán tài sản và thời gian chuyển thanh khoản qua biên giới.
  > "A bank should recognise that stress events may simultaneously give rise to timecritical liquidity needs in multiple currencies and multiple payment and settlement systems."
  > "Tests should reflect accurate time-frames for the settlement cycles of assets that might be liquidated, and the time required to transfer liquidity across borders."
  > — para 101–102 ^lrm-101

- Ngân hàng nên dùng cách tiếp cận thận trọng khi đặt giả định stress test; danh sách giả định minh hoạ gồm 17 mục (bảng dưới).
  > "A bank should take a conservative approach when setting stress testing assumptions."
  > "This list is illustrative, as a bank should use assumptions which are relevant to its business."
  > — para 103 ^lrm-103

  | # | Giả định (para 103) |
  |---|---|
  | 1 | asset market illiquidity and the erosion in the value of liquid assets |
  | 2 | the run-off of retail funding |
  | 3 | the (un)availability of secured and unsecured wholesale funding sources |
  | 4 | the correlation between funding markets or the effectiveness of diversification across sources of funding |
  | 5 | additional margin calls and collateral requirements |
  | 6 | funding tenors |
  | 7 | contingent claims and more specifically, potential draws on committed lines extended to third parties or the bank's subsidiaries, branches or head office |
  | 8 | the liquidity absorbed by off-balance sheet vehicles and activities (including conduit financing) |
  | 9 | the availability of contingent lines extended to the bank |
  | 10 | liquidity drains associated with complex products/transactions |
  | 11 | the impact of credit rating triggers |
  | 12 | FX convertibility and access to foreign exchange markets |
  | 13 | the ability to transfer liquidity across entities, sectors and borders taking into account legal, regulatory, operational and time zone restrictions and constraints |
  | 14 | the access to central bank facilities |
  | 15 | the operational ability of the bank to monetise assets |
  | 16 | the bank's remedial actions and the availability of the necessary documentation and operational expertise and experience to execute them, taking into account the potential reputational impact when executing these actions |
  | 17 | estimates of future balance sheet growth |

- Stress test nên xét phản ứng hành vi của các bên tham gia thị trường và đối tác (kể cả ảnh hưởng tới thời điểm dòng tiền trong ngày).
  > "A bank should consider in its stress tests the likely behavioural response of other market participants to events of market stress and the extent to which a common response might amplify market movements and exacerbate market strain."
  > "A bank's stress tests should consider how the behaviour of counterparties (or their correspondents and custodians) would affect the timing of cash flows, including on an intraday basis."
  > — para 104–105 ^lrm-104

- Thiết kế kịch bản nên được rà soát định kỳ theo thay đổi thị trường, mô hình kinh doanh và kinh nghiệm stress thực tế; ngân hàng có thể phân tích độ nhạy của kết quả với giả định then chốt.
  > "The scenario design should be subject to regular reviews to ensure that the nature and severity of the tested scenarios remain appropriate and relevant to the bank."
  > "a bank may conduct an analysis of the sensitivity of stress test results to certain key assumptions."
  > — para 106–107 ^lrm-106

- Ban điều hành nên rà soát kịch bản, giả định và kết quả; lựa chọn nên được lập hồ sơ; kết quả và hành động nên được báo cáo, thảo luận với HĐQT và cơ quan giám sát; nên đưa kết quả vào kế hoạch chiến lược và quản trị rủi ro hằng ngày; kết quả nên được xét khi đặt hạn mức nội bộ.
  > "Senior management should review stress test scenarios and assumptions as well as the results of the stress tests. The bank's choice of scenarios and related assumptions should be well documented and reviewed together with the stress test results."
  > "Stress test results and vulnerabilities and any resulting actions should be reported to and discussed with the board and the bank's supervisors."
  > "Senior management should integrate the results of the stress testing process into the bank's strategic planning process (eg bank management could adjust its asset-liability composition) and the firm's day-to-day risk management practices (eg through monitoring sensitive cash flows or reducing concentration limits). The results of the stress tests should be explicitly considered in the setting of internal limits."
  > — para 108 ^lrm-108

- Khi thiếu hụt funding dự phóng lớn hơn (hoặc thặng dư nhỏ hơn) mức liquidity risk tolerance cho phép, ban điều hành nên cân nhắc điều chỉnh vị thế thanh khoản hoặc tăng cường kế hoạch dự phòng, tham vấn HĐQT.
  > "Senior management should decide how to incorporate the results of stress tests in assessing and planning for related potential funding shortfalls in the institution's contingency funding plan."
  > "To the extent that projected funding deficits are larger than (or projected funding surpluses are smaller than) implied by the bank's liquidity risk tolerance, management should consider whether to adjust its liquidity position or to bolster the bank's contingency plan in consultation with the board."
  > — para 109 ^lrm-109

### p11 — Principle 11: kế hoạch tài trợ dự phòng (CFP)

- Ngân hàng nên có CFP chính thức nêu chiến lược xử lý thiếu hụt thanh khoản khi khẩn cấp; CFP nên có chính sách cho nhiều môi trường stress, trách nhiệm rõ, thủ tục kích hoạt và leo thang, được kiểm thử và cập nhật định kỳ.
  > "A bank should have a formal contingency funding plan (CFP) that clearly sets out the strategies for addressing liquidity shortfalls in emergency situations."
  > "A CFP should outline policies to manage a range of stress environments, establish clear lines of responsibility, include clear invocation and escalation procedures and be regularly tested and updated to ensure that it is operationally robust."
  > — P11 ^lrm-p11

- Định nghĩa: CFP là tập hợp chính sách, thủ tục và kế hoạch hành động để ứng phó với gián đoạn nghiêm trọng khả năng tài trợ kịp thời, với chi phí hợp lý.
  > "A contingency funding plan (CFP) is the compilation of policies, procedures and action plans for responding to severe disruptions to a bank's ability to fund some or all of its activities in a timely manner and at a reasonable cost."
  > — para 110 ^lrm-110

- CFP nên tương xứng với độ phức tạp và hồ sơ rủi ro; nên có tập biện pháp đa dạng, khả thi; nêu nguồn tài trợ dự phòng và số tiền ước tính từ mỗi nguồn, thủ tục leo thang/ưu tiên và thời gian cần để huy động từ từng nguồn.
  > "CFPs should be commensurate with a bank's complexity, risk profile, scope of operations and role in the financial systems in which the bank operates."
  > "Contingency plans should articulate available potential contingency funding sources and the amount of funds a bank estimates can be derived from these sources; clear escalation/prioritisation procedures detailing when and how each of the actions can and should be activated; and the lead time needed to tap additional funds from each of the contingency sources."
  > — para 111 ^lrm-111

- CFP nên gắn với phân tích rủi ro thanh khoản và kết quả kịch bản, giả định stress test; xét nhiều kỳ hạn kể cả trong ngày; chuẩn bị cho stress riêng ngân hàng, toàn thị trường và tương tác giữa chúng.
  > "The CFP's design, plans and procedures should be closely integrated with the firm's ongoing analysis of liquidity risk and with the results of the scenarios and assumptions used in stress tests."
  > "CFPs should prepare the bank to manage a range of scenarios of severe liquidity stress that include both firm-specific and more generalised market-wide stress, as well as the potential interaction between them."
  > — para 112–113 ^lrm-112

- CFP nên phân định vai trò, thẩm quyền kích hoạt (có thể lập "crisis team"), quy trình ra quyết định và leo thang, thời điểm liên hệ cơ quan giám sát, NHTW, đơn vị vận hành hệ thống thanh toán; nên có kế hoạch truyền thông nội bộ và bên ngoài.
  > "clear specification of roles and responsibilities, including the authority to invoke the CFP. The establishment of a formal "crisis team" may facilitate internal coordination and decision-making during a liquidity crisis;"
  > "It should also address when and how to contact external parties, such as supervisors, central banks, or payments system operators."
  > "Banks therefore should develop a plan that will deliver timely, clear, consistent and frequent communication to internal as well as external parties"
  > — para 114–116 ^lrm-114

- Khi thiết kế CFP, ngân hàng nên tính: tác động stress lên khả năng bán hoặc chứng khoán hoá tài sản; liên kết thanh khoản thị trường và funding; hiệu ứng vòng hai và danh tiếng khi thực hiện biện pháp dự phòng; khả năng chuyển thanh khoản giữa pháp nhân, biên giới và mảng kinh doanh.
  > "When designing its CFP, a bank should account for: (a) the impact of stressed market conditions on its ability to sell or securitise assets; (b) the link between asset market and funding liquidity (eg the extensive or complete loss of typically available market funding options); (c) second round and reputational effects related to execution of contingency funding measures; and (d) the potential to transfer liquidity across group entities, borders and lines of business, taking into account legal, regulatory, operational and time zone restrictions and constraints."
  > — para 117 ^lrm-117

- CFP nên phản ánh chương trình cho vay và yêu cầu tài sản bảo đảm của NHTW, kể cả vấn đề danh tiếng khi tiếp cận; nên có bước bảo đảm thanh toán quan trọng trong ngày và khả năng xếp thứ tự ưu tiên thanh toán.
  > "A bank's CFP (as well as the bank's day-to-day liquidity risk management) should reflect central bank lending programmes and collateral requirements"
  > "The inclusion of central bank lending in a CFP should consider the types of lending facilities, acceptable collateral, the operational procedures to access central bank funds and potential reputational issues involved in accessing them."
  > "In situations where intraday liquidity resources become scarce, a bank should have the ability to identify critical payments and to sequence or schedule payments based on priority."
  > — para 118–119 ^lrm-118

- Tài sản dự định cầm cố khi dùng nguồn dự phòng phải nằm ở pháp nhân và địa điểm phù hợp với kế hoạch funding.
  > "Assets that are intended to be pledged for collateral in the event that back-up funding sources are utilised must be in a legal entity and location consistent with management's funding plans."
  > — para 120 ^lrm-120

- CFP nên được rà soát và kiểm thử định kỳ (vai trò, thông tin liên lạc, khả năng chuyển tiền và tài sản bảo đảm, hồ sơ pháp lý); nên kiểm thử giả định then chốt như khả năng bán hoặc repo tài sản, rút hạn mức tín dụng; ban điều hành nên rà soát, cập nhật CFP ít nhất hằng năm để HĐQT phê duyệt.
  > "CFPs should be reviewed and tested regularly to ensure their effectiveness and operational feasibility."
  > "A bank should regularly test key assumptions, such as the ability to sell or repo certain assets or periodically draw down credit lines."
  > "Senior management should review and update the CFP at least every year for the board's approval, or more often as business or market circumstances change."
  > — para 121 ^lrm-121

- CFP nên nhất quán với kế hoạch kinh doanh liên tục và vận hành được khi kế hoạch đó được kích hoạt.
  > "The CFP should be consistent with the bank's business continuity plans and should be operational under situations where business continuity arrangements have been invoked."
  > — para 122 ^lrm-122

## Node bị ảnh hưởng
- p01, p10, p11 [2026-10-20]: tạo [[bcbs-liquidity-principles]]; cập nhật [[ilaap]], [[liquidity-stress-testing]], [[liquidity-risk-management]] (draft); đề xuất [[contingency-funding-plan]] (canonical).
- p02, p03, p04 [2026-10-20]: cập nhật [[bcbs-liquidity-principles]], [[liquidity-risk-management]], [[risk-appetite]], [[funds-transfer-pricing]], [[new-product-approval]], [[alco]], [[three-lines-of-defence]] (draft); đề xuất [[liquidity-transfer-pricing]] (canonical).

## Mâu thuẫn ghi nhận
- Không có. SRP30.51 của Basel Framework lặp gần nguyên văn para 94 ([[src-bcbs-framework#^srp30-51]]); SRP30.50 lặp nội dung P2 (tolerance do HĐQT đặt) và P4 (chi phí thanh khoản trong định giá nội bộ).

## Ghi chú convert
- Câu nguyên tắc P12 bị tách: phần cuối thành heading ở dòng 528 (chưa ảnh hưởng unit đã ingest).
- Số footnote chèn rời trong câu ở một số đoạn (vd para 23, câu nguyên tắc P3 'board of directors 4 should'); không trích qua các số này.
- Raw có nhiều khoảng trắng kép; lint chuẩn hoá khoảng trắng nên trích dẫn dùng khoảng trắng đơn.
