---
title: "BCBS — The Basel Framework (Consolidated)"
aliases: []
type: source
source_id: src-bcbs-framework
domains: [basel, alm]
status: active
maturity: draft
tier: T2
doc_status: final
issuer: BCBS
published: 2025-12-17
effective: 2019-12-15
raw: 01_sources/alm/Basel/BaselFramework/BaselFramework.md
units_done: [SRP50, RBC25, SRP30]
updated: 2026-10-20
---

## Thông tin nguồn
- Issuer: Basel Committee on Banking Supervision ([[bcbs]])
- Tier T2, `doc_status: final`. Bản tổng hợp toàn bộ khuôn khổ Basel (Consolidated Framework) do website BIS sinh ngày 17/12/2025.
- Scope: File chuẩn mực bao quát toàn bộ các trụ cột Basel (Scope of application SCO, Capital CAP, Risk-based capital RBC, Credit risk CRE, Market risk MAR, Operational risk OPE, Leverage ratio LEV, Liquidity LCR & NSF, Large exposures LEX, Margin requirements MGN, Supervisory review SRP, Disclosure DIS).
- Raw: `01_sources/alm/Basel/BaselFramework/BaselFramework.md` (26.057 dòng); meta: `BaselFramework_meta.json`.
- Ghi chú: Các phần LCR, NSFR, LEV và IRRBB (d368) có file văn bản chuyên biệt riêng (`src-bcbs-lcr`, `src-bcbs-nsfr`, `src-bcbs-lev`, `src-bcbs-irrbb-2016`). Source note này dùng để quản lý việc ingest các chương độc lập trong bộ khung hợp nhất, mở đầu là **Chương SRP50 (Liquidity Monitoring Metrics)**; đã ingest thêm RBC25 và SRP30 (Risk management, Pillar 2).

## Tóm tắt Chương SRP50 — Liquidity Monitoring Metrics
Chương SRP50 (thuộc Trụ cột 2 — Quy trình Đánh giá Giám sát) thiết lập hệ thống **các công cụ đo lường và giám sát thanh khoản bổ trợ** cho hai chuẩn mực định lượng bắt buộc là LCR và NSFR. 

Nếu như LCR tập trung vào kịch bản căng thẳng cấp tính 30 ngày và NSFR đo lường cấu trúc tài trợ ổn định 1 năm, thì SRP50 cung cấp 5 lăng kính giám sát liên tục và vi mô cho cơ quan giám sát và ngân hàng:
1. **Chênh lệch kỳ hạn theo hợp đồng (Contractual maturity mismatch)**: Bóc tách dòng tiền vào và dòng tiền ra thuần túy theo hợp đồng (không giả định hành vi, không rollover nợ) trên 13 dải kỳ hạn (từ qua đêm đến trên 5 năm) để nhận diện khoảng trống thanh khoản thực chất (liquidity gaps).
2. **Mức độ tập trung nguồn vốn (Concentration of funding)**: Đo lường mức độ phụ thuộc rủi ro vào các đối tác bán buôn lớn ($\ge 1\%$ tổng bảng cân đối), các sản phẩm huy động lớn ($\ge 1\%$), và các đồng tiền ngoại tệ trọng yếu ($\ge 5\%$ tổng nợ).
3. **Tài sản không bị phong tỏa khả dụng (Available unencumbered assets)**: Định lượng kho tài sản sạch có thể dùng làm tài sản bảo đảm để vay mượn khẩn cấp trên thị trường thứ cấp hoặc chiết khấu tại NHTW.
4. **LCR theo từng ngoại tệ trọng yếu (LCR by significant currency)**: Đo lường tỷ lệ LCR riêng lẻ cho từng đồng tiền chiếm $\ge 5\%$ tổng nợ nhằm phát hiện rủi ro lệch pha cơ cấu tiền tệ (FX liquidity mismatch).
5. **Các công cụ cảnh báo sớm từ thị trường (Market-related monitoring tools)**: Khai thác dữ liệu thị trường tần suất cao (giá cổ phiếu ngân hàng, chênh lệch CDS, lợi suất trái phiếu, lãi suất liên ngân hàng) để phát hiện sớm các dấu hiệu suy giảm niềm tin.
6. **Bộ công cụ giám sát thanh khoản trong ngày (Intraday liquidity management)**: Đo lường mức sử dụng thanh khoản đỉnh, thanh khoản khả dụng đầu ngày, tổng giá trị thanh toán, nghĩa vụ tại mốc thời gian cố định và tỷ lệ thông lượng (throughput) qua tài khoản thanh toán tại hệ thống thanh toán giá trị lớn (LVPS).

---

## Key claims

### SRP50 — Liquidity monitoring metrics

#### 1. Mục tiêu và Phạm vi Áp dụng

- Bên cạnh LCR và NSFR là các chuẩn mực định lượng tối thiểu bắt buộc, Ủy ban Basel phát triển bộ công cụ giám sát rủi ro thanh khoản nhằm đo lường các khía cạnh khác của hồ sơ thanh khoản và cấu trúc tài trợ.
  > "In addition to the Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR) standards, the minimum quantitative standards that banks must comply with, the Committee has developed a set of liquidity risk monitoring tools to measure other dimensions of a bank's liquidity and funding risk profile."
  > — SRP50.1 ^srp50-1

- Các chỉ số giám sát này, kết hợp cùng chuẩn mực LCR và NSFR, tạo thành nền tảng thông tin giúp cơ quan giám sát đánh giá toàn diện rủi ro thanh khoản của ngân hàng.
  > "These metrics, together with the LCR and NSFR standard, provide the cornerstone of information that aid supervisors in assessing the liquidity risk of a bank."
  > — SRP50.2 ^srp50-2

- Ban điều hành ngân hàng có trách nhiệm thu thập và nộp dữ liệu giám sát cho cơ quan quản lý; dữ liệu này không bắt buộc phải công bố công khai ra thị trường.
  > "Consistent with their broader liquidity risk management responsibilities, bank management will be responsible for collating and submitting the monitoring data for the tools to their banking supervisor."
  > "However, banks and supervisors are not required to disclose these reporting requirements publicly. Public disclosure is not intended to be part of these monitoring tools."
  > — SRP50.3 ^srp50-3

- Các công cụ trong chương này phục vụ mục đích giám sát và bắt buộc áp dụng đối với tất cả các ngân hàng hoạt động quốc tế.
  > "The tools in this chapter are for monitoring purposes only. Internationally active banks must apply these tools."
  > — SRP50.4 ^srp50-4

#### 2. Chênh Lệch Kỳ Hạn Hợp Đồng (Contractual Maturity Mismatch)

- Hồ sơ chênh lệch kỳ hạn theo hợp đồng nhận diện khoảng trống giữa dòng tiền vào và dòng tiền ra theo hợp đồng cho các dải thời gian xác định, cho biết lượng thanh khoản tiềm tàng ngân hàng cần huy động nếu mọi dòng tiền ra xảy ra tại thời điểm sớm nhất có thể.
  > "The contractual maturity mismatch profile identifies the gaps between the contractual inflows and outflows of liquidity for defined time bands. These maturity gaps indicate how much liquidity a bank would potentially need to raise in each of these time bands if all outflows occurred at the earliest possible date. This metric provides insight into the extent to which the bank relies on maturity transformation under its current contracts."
  > — SRP50.6 ^srp50-6

- Ngân hàng phải báo cáo các dòng tiền mặt và dòng chứng khoán theo kỳ hạn hợp đồng còn lại; cơ quan giám sát có thể yêu cầu phân bổ trên 13 dải kỳ hạn (qua đêm, 7 ngày, 14 ngày, 1, 2, 3, 6, 9 tháng, 1, 2, 3, 5 năm và trên 5 năm); các công cụ không xác định kỳ hạn phải báo cáo riêng biệt.
  > "A bank should report contractual cash and security flows in the relevant time bands based on their residual contractual maturity. Supervisors in each jurisdiction will determine the specific template, including required time bands, by which data must be reported."
  > — SRP50.7 ^srp50-7

- Tối thiểu, dữ liệu thu thập từ chênh lệch kỳ hạn hợp đồng phải cung cấp thông tin theo các phân loại danh mục được nêu trong chuẩn mực LCR.
  > "At a minimum, the data collected from the contractual maturity mismatch should provide data on the categories outlined in the LCR."
  > — SRP50.8 ^srp50-8

- Khi lập bảng dòng tiền hợp đồng, ngân hàng phải áp dụng giả định không quay vòng (no rollover) các khoản nợ hiện hữu và không phát sinh hợp đồng mới cho tài sản.
  > "No rollover of existing liabilities is assumed to take place. For assets, the bank is assumed not to enter into any new contracts."
  > — SRP50.9 ^srp50-9

- Do chỉ dựa thuần túy trên kỳ hạn hợp đồng mà không kèm giả định hành vi, số liệu này không phản ánh dòng tiền dự báo thực tế trong trạng thái hoạt động liên tục (going-concern).
  > "Given that the metric is based solely on contractual maturities with no behavioural assumptions, the data will not reflect actual future forecasted flows under the current, or future, strategy or plans, ie, under a going-concern view."
  > — SRP50.11 ^srp50-11

- Ngân hàng phải tự thực hiện phân tích chênh lệch kỳ hạn nội bộ dựa trên các giả định hành vi trong điều kiện hoạt động bình thường và căng thẳng để so sánh với số liệu hợp đồng.
  > "banks should also conduct their own maturity mismatch analyses, based on going-concern behavioural assumptions of the inflows and outflows of funds in both normal situations and under stress."
  > — SRP50.12 ^srp50-12

#### 3. Mức Độ Tập Trung Nguồn Vốn (Concentration of Funding)

- Chỉ số này nhận diện các nguồn vốn bán buôn có quy mô trọng yếu đến mức việc rút vốn có thể kích hoạt rủi ro thanh khoản, qua đó thúc đẩy đa dạng hóa nguồn tài trợ.
  > "This metric is meant to identify those sources of wholesale funding that are of such significance that withdrawal of this funding could trigger liquidity problems. The metric thus encourages the diversification of funding sources recommended in the Committee's Sound Principles."
  > — SRP50.14 ^srp50-14

- Đối tác trọng yếu (significant counterparty) được định nghĩa là một đối tác đơn lẻ hoặc nhóm đối tác liên quan chiếm tổng cộng trên 1% tổng bảng cân đối kế toán của ngân hàng.
  > "A \"significant counterparty\" is defined as a single counterparty or group of connected or affiliated counterparties accounting in aggregate for more than 1% of the bank's total balance sheet"
  > — SRP50.17 ^srp50-17

- Chỉ số tập trung đối tác và sản phẩm đo bằng nợ huy động từ từng đối tác/sản phẩm trọng yếu chia tổng nợ phải trả; ngân hàng và cơ quan giám sát nên theo dõi cả tỷ lệ tuyệt đối lẫn mức tăng đáng kể của tập trung.
  > "(1) Funding liabilities sourced from each significant counterparty as a % of total liabilities"
  > "(2) Funding liabilities sourced from each significant production / instrument as a % of total liabilities"
  > "Banks and supervisors should monitor both the absolute percentage of the funding exposure, as well as significant increases in concentrations."
  > — SRP50.14–15 ^srp50-15

- Nhóm đối tác liên quan định nghĩa như quy định Large Exposure của nước sở tại; tiền gửi nội bộ tập đoàn và từ bên liên quan phải được nhận diện riêng, ở cả cấp pháp nhân lẫn tập đoàn, vì giao dịch nội bộ có thể bị hạn chế khi stress.
  > "A group of connected counterparties is, in this context, defined in the same way as in the "Large Exposure" regulation of the host country in the case of consolidated reporting for solvency purposes."
  > "Intra-group deposits and deposits from related parties should be identified specifically under this metric, regardless of whether the metric is being calculated at a legal entity or group level, due to the potential limitations to intra-group transactions in stressed conditions."
  > — SRP50.17 ^srp50-17b

- Sản phẩm/công cụ trọng yếu (significant instrument/product) là một sản phẩm đơn lẻ hoặc nhóm sản phẩm tương tự chiếm trên 1% tổng bảng cân đối của ngân hàng.
  > "A \"significant instrument/product\" is defined as a single instrument/product or group of similar instruments/products that in aggregate amount to more than 1% of the bank's total balance sheet."
  > — SRP50.19 ^srp50-19

- Ngoại tệ trọng yếu (significant currency) là loại tiền tệ có tổng nợ phải trả bằng đồng tiền đó chiếm từ 5% trở lên trong tổng nợ của ngân hàng.
  > "A currency is considered \"significant\" if the aggregate liabilities denominated in that currency amount to 5% or more of the bank's total liabilities."
  > — SRP50.21 ^srp50-21

- Các chỉ số tập trung nguồn vốn phải được báo cáo riêng biệt cho các kỳ hạn: dưới 1 tháng, 1-3 tháng, 3-6 tháng, 6-12 tháng và trên 12 tháng.
  > "The above metrics should be reported separately for the time horizons of less than one month, 1-3 months, 3-6 months, 6-12 months, and for longer than 12 months."
  > — SRP50.22 ^srp50-22

#### 4. Tài Sản Không Bị Phong Tỏa Khả Dụng (Available Unencumbered Assets)

- Chỉ số này cung cấp dữ liệu về số lượng và đặc tính cốt lõi (bao gồm loại tiền tệ và địa điểm lưu ký) của tài sản sạch không bị cầm cố có khả năng chuyển đổi thành thanh khoản.
  > "These metrics provide supervisors with data on the quantity and key characteristics, including currency denomination and location, of banks' available unencumbered assets."
  > — SRP50.27 ^srp50-27

- Ngân hàng phải báo cáo quy mô, chủng loại và vị trí của các tài sản sạch có thể làm tài sản bảo đảm cho các giao dịch vay có tài sản bảo đảm trên thị trường thứ cấp theo tỷ lệ chiết khấu (haircut) thỏa thuận trước hoặc hiện hành.
  > "A bank is to report the amount, type and location of available unencumbered assets that could serve as collateral for secured borrowing in secondary markets at prearranged or current haircuts at reasonable costs."
  > — SRP50.28 ^srp50-28

#### 5. LCR Theo Từng Ngoại Tệ Trọng Yếu (LCR by Significant Currency)

- Dù chuẩn LCR chỉ bắt buộc đáp ứng trên tổng tiền tệ hợp nhất, ngân hàng và cơ quan giám sát phải theo dõi tỷ lệ LCR theo từng ngoại tệ trọng yếu để nhận diện các rủi ro bất cân xứng tiền tệ tiềm ẩn.
  > "While the LCR is required to be met in one single currency, in order to better capture potential currency mismatches, banks and supervisors should also monitor the LCR in significant currencies."
  > — SRP50.35 ^srp50-35

- Tiêu chí xác định đồng tiền trọng yếu để tính LCR riêng biệt là đồng tiền có tổng nợ chiếm từ 5% trở lên trong tổng nợ của ngân hàng.
  > "A currency is considered \"significant\" if the aggregate liabilities denominated in that currency amount to 5% or more of the bank's total liabilities."
  > — SRP50.37 ^srp50-37

#### 6. Công Cụ Giám Sát Thị Trường (Market-related Monitoring Tools)

- Dữ liệu thị trường tần suất cao với độ trễ thấp hoặc không có độ trễ được sử dụng làm các chỉ báo cảnh báo sớm nhằm theo dõi các khó khăn thanh khoản tiềm ẩn của ngân hàng.
  > "High-frequency market data with little or no time lag can be used as early warning indicators in monitoring potential liquidity difficulties at banks."
  > — SRP50.40 ^srp50-40

- Thông tin thị trường có giá trị giám sát bao gồm giá cổ phiếu, thị trường nợ (thị trường tiền tệ, kỳ hạn trung hạn, nợ dài hạn, phái sinh, nợ chính phủ), chênh lệch tín dụng và tỷ giá.
  > "Valuable market information to monitor includes, but is not limited to, equity prices"
  > — SRP50.43 ^srp50-43

#### 7. Quản Trị Thanh Khoản Trong Ngày (Intraday Liquidity Management)

- Việc ngân hàng không quản trị hiệu quả thanh khoản trong ngày có thể khiến ngân hàng không hoàn thành kịp thời các nghĩa vụ thanh toán và bù trừ, dẫn đến đứt gãy thanh khoản lan truyền nhanh chóng qua nhiều hệ thống và định chế.
  > "A bank's failure to effectively manage intraday liquidity could leave it unable to meet its payment and settlement obligations on a timely basis, which could lead to liquidity dislocations that cascade quickly across many systems and institutions."
  > — SRP50.47 ^srp50-47

- Công cụ mức sử dụng thanh khoản đỉnh trong ngày (Daily maximum intraday liquidity usage) cho phép cơ quan giám sát theo dõi mức độ thâm hụt thanh khoản ròng lớn nhất trong ngày của tài khoản quyết toán.
  > "The daily maximum intraday liquidity usage tool will enable supervisors to monitor a bank's intraday liquidity usage in normal conditions."
  > — SRP50.64 ^srp50-64

- Công cụ thanh khoản khả dụng đầu ngày (Available intraday liquidity at start of day) giám sát lượng thanh khoản sẵn sàng phục vụ các nhu cầu thanh toán trong ngày trong điều kiện bình thường.
  > "The available intraday liquidity at the start of the business day tool will enable supervisors to monitor the amount of intraday liquidity a bank has available at the start of each day to meet its intraday liquidity requirements in normal conditions."
  > — SRP50.69 ^srp50-69

- Công cụ tổng thanh toán (Total payments) giám sát quy mô tổng thể của các giao dịch thanh toán đi và đến của ngân hàng.
  > "The total payments tool will enable supervisors to monitor the overall scale of a bank's payment activity."
  > — SRP50.72 ^srp50-72

- Công cụ nghĩa vụ tại mốc thời gian xác định (Time-specific obligations) theo dõi các khoản thanh toán bắt buộc phải hoàn tất trước thời điểm nhất định, tránh nguy cơ bị phạt tài chính hoặc tổn hại uy tín nghiêm trọng.
  > "The time-specific obligations tool will enable supervisors to gain a better understanding of a bank's time specific obligations."
  > — SRP50.73 ^srp50-73

- Công cụ thông lượng trong ngày (Intraday throughput) áp dụng cho các thành viên trực tiếp của hệ thống thanh toán để theo dõi tỷ lệ giải phóng lệnh thanh toán đi theo từng mốc thời gian trong ngày.
  > "The intraday throughput tool will enable supervisors to monitor the throughput of a direct participant's daily payments activity across its settlement account."
  > — SRP50.80 ^srp50-80

- Các công cụ giám sát thanh khoản trong ngày phải được đặt trong các kịch bản kiểm tra sức chịu tải căng thẳng (stress scenarios) bao gồm: stress tài chính nội tại của ngân hàng, stress đối tác, stress ngân hàng khách hàng và stress toàn thị trường.
  > "The monitoring tools in SRP50.64 to SRP50.81 will provide banking supervisors with information on a bank's intraday liquidity profile in normal conditions. However, the availability and usage of intraday liquidity can change markedly in times of stress."
  > — SRP50.82 ^srp50-82

### RBC25 — Boundary between the banking book and the trading book

#### 1. Phạm vi và hiệu lực

- RBC25 xác định công cụ thuộc trading book (chịu yêu cầu vốn rủi ro thị trường) và công cụ thuộc banking book (chịu yêu cầu vốn rủi ro tín dụng); phiên bản hiệu lực từ 01/01/2023.
  > "This chapter sets out the instruments to be included in the trading book (which are subject to market risk capital requirements) and those to be included in the banking book (which are subject to credit risk capital requirements)."
  > "Version effective as of 01 Jan 2023"
  > — RBC25 (mở đầu) ^rbc25-0

- Trading book gồm mọi công cụ đáp ứng tiêu chí tại RBC25.2–25.13; mọi công cụ khác phải vào banking book.
  > "A trading book consists of all instruments that meet the specifications for trading book instruments set out in RBC25.2 through RBC25.13. All other instruments must be included in the banking book."
  > — RBC25.1 ^rbc25-1

- Công cụ gồm công cụ tài chính, ngoại hối và hàng hoá; công cụ tài chính gồm cả công cụ cơ sở (cash instruments) và phái sinh.
  > "Instruments comprise financial instruments, foreign exchange (FX), and commodities."
  > "Financial instruments include both primary financial instruments (or cash instruments) and derivative financial instruments."
  > — RBC25.2 ^rbc25-2

- Ngân hàng chỉ được đưa công cụ vào trading book khi không có trở ngại pháp lý đối với việc bán hoặc phòng ngừa toàn bộ.
  > "Banks may only include a financial instrument, instruments on FX or commodity in the trading book when there is no legal impediment against selling or fully hedging it."
  > — RBC25.3 ^rbc25-3

- Ngân hàng phải định giá hợp lý hằng ngày mọi công cụ trading book và ghi nhận thay đổi giá trị vào P&L.
  > "Banks must fair value daily any trading book instrument and recognise any valuation change in the profit and loss (P&L) account."
  > — RBC25.4 ^rbc25-4

#### 2. Tiêu chuẩn phân bổ công cụ vào sổ

- Công cụ nắm giữ cho một trong bốn mục đích phải được chỉ định là trading book ngay khi ghi nhận ban đầu, trừ khi RBC25.3 hoặc RBC25.8 quy định khác: bán lại ngắn hạn; kiếm lời từ biến động giá ngắn hạn; khoá lợi nhuận arbitrage; phòng ngừa rủi ro từ công cụ thuộc ba mục đích trên.
  > "Any instrument a bank holds for one or more of the following purposes must, when it is first recognised on its books, be designated as a trading book instrument, unless specifically otherwise provided for in RBC25.3 or RBC25.8:"
  > "(1) short-term resale;"
  > "(2) profiting from short-term price movements;"
  > "(3) locking in arbitrage profits; or"
  > "(4) hedging risks that arise from instruments meeting (1), (2) or (3) above."
  > — RBC25.5 ^rbc25-5

- Hoạt động bán định kỳ tự nó không đủ để coi một vị thế là nắm giữ để bán lại ngắn hạn.
  > "No. Periodic sale activity on its own is insufficient to consider a position as held for short-term resale."
  > — RBC25.5 FAQ1 ^rbc25-5-faq1

- Các công cụ sau được coi là nắm giữ cho mục đích tại RBC25.5 nên phải vào trading book: danh mục correlation trading; công cụ tạo vị thế bán ròng (net short) tín dụng hoặc cổ phiếu trong banking book; công cụ từ cam kết bảo lãnh phát hành chứng khoán dự kiến thực mua vào ngày thanh toán. Vị thế net short tồn tại khi giá trị hiện tại của banking book tăng lúc giá cổ phiếu giảm hoặc credit spread tăng.
  > "Any of the following instruments is seen as being held for at least one of the purposes listed in RBC25.5 and must therefore be included in the trading book, unless specifically otherwise provided for in RBC25.3 or RBC25.8:"
  > "(1) instruments in the correlation trading portfolio;"
  > "(2) instruments that would give rise to a net short credit or equity position in the banking book;"
  > "(3) instruments resulting from underwriting commitments, where underwriting commitments refer only to securities underwriting, and relate only to securities that are expected to be actually purchased by the bank on the settlement date."
  > "A bank will have a net short risk position for equity risk or credit risk in the banking book if the present value of the banking book increases when an equity price decreases or when a credit spread on an issuer or group of issuers of debt increases."
  > — RBC25.6 ^rbc25-6

- CDS phòng ngừa khoản vay banking book mà tạo vị thế net short tín dụng: phần net short (không bù trừ được với vị thế long) phải được xử lý như vị thế trading book và chịu vốn rủi ro thị trường.
  > "In this example, the net short position resulting from such instruments (ie the amount which cannot be offset against any long positions) must be treated as a trading book position and be subject to market risk capital requirements."
  > — RBC25.6 FAQ2 ^rbc25-6-faq2

- Công cụ không nắm giữ cho mục đích tại RBC25.5 lúc khởi tạo, và không bị coi là nắm giữ cho các mục đích đó theo RBC25.6, phải vào banking book.
  > "Any instrument which is not held for any of the purposes listed in RBC25.5 at inception, nor seen as being held for these purposes according to RBC25.6, must be assigned to the banking book."
  > — RBC25.7 ^rbc25-7

- Danh sách công cụ bắt buộc vào banking book: cổ phiếu chưa niêm yết; công cụ chỉ định cho securitisation warehousing; nắm giữ bất động sản trực tiếp; tín dụng bán lẻ và SME; đầu tư vào quỹ (trừ khi look-through được với thông tin được bên thứ ba độc lập xác minh, hoặc có giá hằng ngày và tiếp cận được mandate của quỹ); quỹ phòng hộ; phái sinh và quỹ có tài sản cơ sở thuộc các loại trên; công cụ phòng ngừa rủi ro cụ thể của các vị thế trên. Cam kết cho vay bán lẻ và SME cũng bị loại khỏi trading book.
  > "The following instruments must be assigned to the banking book:"
  > "(1) unlisted equities;"
  > "(2) instruments designated for securitisation warehousing;"
  > "(4) retail and small or medium-sized enterprise (SME) credit;"
  > "(5) equity investments in a fund, unless the bank meets at least one of the following conditions:"
  > "(6) hedge funds;"
  > "(7) derivative instruments and funds that have the above instrument types as underlying assets; or"
  > "(8) instruments held for the purpose of hedging a particular risk of a position in the types of instrument above."
  > "Yes. Retail and SME lending commitments are excluded from the trading book."
  > — RBC25.8, RBC25.8 FAQ1 ^rbc25-8

- Danh sách suy định (presumptive list) vào trading book: tài sản/nợ kinh doanh theo kế toán; công cụ từ hoạt động market-making; đầu tư vào quỹ (trừ loại vào banking book theo RBC25.8(5)); cổ phiếu niêm yết; giao dịch kiểu repo phục vụ kinh doanh; quyền chọn, kể cả phái sinh nhúng, từ công cụ ngân hàng phát hành ngoài banking book của mình và liên quan rủi ro tín dụng hoặc cổ phiếu. Repo vừa để quản lý thanh khoản vừa ghi nhận theo accrual không thuộc danh sách này.
  > "There is a general presumption that any of the following instruments are being held for at least one of the purposes listed in RBC25.5 and therefore are trading book instruments"
  > "(2) instruments resulting from market-making activities;"
  > "(3) equity investments in a fund excluding those assigned to the banking book in accordance with RBC25.8(5);"
  > "(5) trading-related repo-style transaction;"
  > "Repo-style transactions that are (i) entered for liquidity management and (ii) valued at accrual for accounting purposes are not part of the presumptive list of RBC25.9."
  > — RBC25.9 ^rbc25-9

- Giao dịch kiểu repo phục vụ kinh doanh là giao dịch lập để market-making, khoá lợi nhuận arbitrage hoặc tạo vị thế short tín dụng hay cổ phiếu.
  > "Trading-related repo-style transactions comprise those entered into for the purposes of market-making, locking in arbitrage profits or creating short credit or equity positions."
  > — RBC25.9 FAQ1 ^rbc25-9-faq1

- Nợ phát hành từ banking book có phái sinh nhúng thuộc RBC25.9(6) phải tách: phái sinh nhúng vào trading book, phần nợ còn lại ở banking book; việc tách này không cần IRT.
  > "This means that banks should split the liability into two components: (i) the embedded derivative, which is assigned to the trading book; and (ii) the residual liability, which is retained in the banking book. No internal risk transfers are necessary for this bifurcation."
  > — RBC25.9 FAQ2 ^rbc25-9-faq2

- Quyền chọn quản lý rủi ro ngoại hối của banking book thuộc danh sách suy định vào trading book; chỉ khi có phê duyệt rõ ràng của cơ quan giám sát mới được đưa vào banking book.
  > "Only with explicit supervisory approval may a bank include in its banking book an option that manages banking book FX risk."
  > — RBC25.9 FAQ3 ^rbc25-9-faq3

- Muốn lệch khỏi danh sách suy định, ngân hàng phải gửi đề nghị kèm bằng chứng công cụ không nắm giữ cho mục đích tại RBC25.5 và nhận phê duyệt rõ ràng; không được duyệt thì công cụ phải vào trading book; mọi sai lệch phải được lập hồ sơ chi tiết liên tục.
  > "If a bank believes that it needs to deviate from the presumptive list established in RBC25.9 for an instrument, it must submit a request to its supervisor and receive explicit approval. In its request, the bank must provide evidence that the instrument is not held for any of the purposes in RBC25.5."
  > "In cases where this approval is not given by the supervisor, the instrument must be designated as a trading book instrument. Banks must document any deviations from the presumptive list in detail on an on-going basis."
  > — RBC25.10 ^rbc25-10

#### 3. Quyền của cơ quan giám sát và hồ sơ

- Cơ quan giám sát có thể yêu cầu bằng chứng và buộc chuyển công cụ trading book sang banking book (trừ công cụ thuộc RBC25.6), hoặc công cụ banking book sang trading book (trừ công cụ thuộc RBC25.8).
  > "If the supervisor is of the view that a bank has not provided enough evidence or if the supervisor believes the instrument customarily would belong in the banking book, it may require the bank to assign the instrument to the banking book, except if it is an instrument listed under RBC25.6."
  > "If the supervisor is of the view that a bank has not provided enough evidence, or if the supervisor believes such instruments would customarily belong in the trading book, it may require the bank to assign the instrument to the trading book, except if it is an instrument listed under RBC25.8."
  > — RBC25.11–25.12 ^rbc25-11

- Ngân hàng phải có chính sách, quy trình và thực hành được lập hồ sơ để xác định công cụ vào hoặc ra trading book; bộ phận kiểm soát nội bộ đánh giá liên tục; việc tuân thủ được kiểm toán nội bộ định kỳ, tối thiểu hằng năm.
  > "A bank must have clearly defined policies, procedures and documented practices for determining which instruments to include in or to exclude from the trading book for the purposes of calculating their regulatory capital"
  > "Compliance with the policies and procedures must be fully documented and subject to periodic (at least yearly) internal audit and the results must be available for supervisory review."
  > — RBC25.13 ^rbc25-13

#### 4. Hạn chế chuyển công cụ giữa các sổ

- Ngoài các chuyển dịch bắt buộc theo RBC25.5–25.10, việc ngân hàng tự chuyển sổ sau khi chỉ định ban đầu bị giới hạn chặt; chuyển sổ để arbitrage quy định bị cấm; chỉ được phép trong hoàn cảnh đặc biệt (ví dụ tái cấu trúc đóng vĩnh viễn trading desk, thay đổi chuẩn mực kế toán); biến động thị trường, thay đổi thanh khoản của công cụ hay thay đổi ý định kinh doanh không phải lý do hợp lệ.
  > "Switching instruments for regulatory arbitrage is strictly prohibited. In practice, switching should be rare and will be allowed by supervisors only in extraordinary circumstances."
  > "Market events, changes in the liquidity of a financial instrument, or a change of trading intent alone are not valid reasons for reassigning an instrument to a different book."
  > — RBC25.14 ^rbc25-14

- Không bao giờ được hưởng lợi vốn từ chuyển sổ: nếu tổng vốn yêu cầu (cả hai sổ) giảm sau khi chuyển, phần chênh lệch tại thời điểm chuyển bị áp làm phụ phí vốn Pillar 1 có công bố, giảm dần khi vị thế đáo hạn; quy định áp dụng cả khi chuyển sổ ngoài ý muốn của ngân hàng (ví dụ cổ phiếu bị huỷ niêm yết).
  > "Without exception, a capital benefit as a result of switching will not be allowed in any case or circumstance."
  > "If this capital requirement is reduced as a result of this switch, the difference as measured at the time of the switch will be imposed on the bank as a disclosed Pillar 1 capital surcharge. This surcharge will be allowed to run off as the positions mature or expire, in a manner agreed with the supervisor."
  > "It is therefore independent of whether the switch has been made at the discretion of the bank or is beyond its control, eg in the case of the delisting of an equity."
  > — RBC25.15, RBC25.15 FAQ1 ^rbc25-15

- Mọi chuyển sổ (kể cả bán đứt theo giá thị trường giữa hai sổ) phải được senior management phê duyệt, lập hồ sơ, được cơ quan giám sát chấp thuận trước và công bố công khai; không thể đảo ngược trừ khi đặc điểm vị thế thay đổi; công cụ bị phân loại lại thành tài sản/nợ kinh doanh theo kế toán thì chuyển tự động sang trading book không cần chấp thuận.
  > "Any reallocation of securities between the trading book and banking book, including outright sales at arm's length, should be considered a reassignment of securities and is governed by requirements of this paragraph."
  > "Any reassignment must be approved by senior management thoroughly documented; determined by internal review to be in compliance with the bank's policies; subject to prior approval by the supervisor based on supporting documentation provided by the bank; and publicly disclosed."
  > "Unless required by changes in the characteristics of a position, any such reassignment is irrevocable."
  > "Accordingly, in this case an automatic switch without approval of the supervisor is acceptable."
  > — RBC25.16 ^rbc25-16

- Xử lý IRT chỉ áp dụng cho chuyển rủi ro qua giao dịch phái sinh nội bộ; chuyển chứng khoán giữa hai sổ là chuyển sổ theo RBC25.16.
  > "The treatment specified for internal risk transfers applies only to risk transfers done via internal derivatives trades. The reallocation of securities between trading and banking book should be considered a reassignment of securities and is governed by RBC25.16."
  > — RBC25.16 FAQ1 ^rbc25-16-faq1

- Chuyển từ trading book sang banking book luôn cần chấp thuận của cơ quan giám sát, kể cả khi phân loại kế toán thay đổi.
  > "Although some national accounting regimes provide flexibility to change the accounting classification for an instrument, reallocating positions to the banking book due to changes in accounting classification without supervisory approval is not permitted by this standard."
  > — RBC25.16 FAQ2 ^rbc25-16-faq2

- Chính sách chuyển sổ phải cập nhật tối thiểu hằng năm, dựa trên phân tích sự kiện bất thường năm trước, gửi cơ quan giám sát; nội dung gồm hạn chế chuyển sổ, quy trình phê duyệt, cách nhận diện sự kiện bất thường, và công bố chuyển sổ tại kỳ báo cáo sớm nhất.
  > "A bank must adopt relevant policies that must be updated at least yearly. Updates should be based on an analysis of all extraordinary events identified during the previous year."
  > "A requirement that re-assignments into or out of the trading book be publicly disclosed at the earliest reporting date."
  > — RBC25.17 ^rbc25-17

#### 5. Chuyển giao rủi ro nội bộ (internal risk transfer)

- Internal risk transfer là bản ghi nội bộ về việc chuyển rủi ro trong banking book, giữa banking book và trading book, hoặc trong trading book (giữa các desk).
  > "An internal risk transfer is an internal written record of a transfer of risk within the banking book, between the banking and the trading book or within the trading book (between different desks)."
  > — RBC25.18 ^rbc25-18

- IRT từ trading book sang banking book không được công nhận về vốn quy định; IRT từ banking book sang trading book theo RBC25.21–25.27.
  > "There will be no regulatory capital recognition for internal risk transfers from the trading book to the banking book."
  > "For internal risk transfers from the banking book to the trading book, RBC25.21 to RBC25.27 apply."
  > — RBC25.19–25.20 ^rbc25-19

- Phòng ngừa rủi ro tín dụng hoặc cổ phiếu của banking book qua IRT chỉ được coi là đã phòng ngừa cho mục đích vốn khi và chỉ khi trading book ký hợp đồng phòng ngừa bên ngoài với bên bảo vệ đủ điều kiện, khớp chính xác với IRT (có thể gồm nhiều giao dịch, nhiều đối tác nếu tổng khớp chính xác).
  > "The credit exposure in the banking book is deemed to be hedged for capital requirement purposes if and only if:"
  > "the trading book enters into an external hedge with an eligible thirdparty protection provider that exactly matches the internal risk transfer; and"
  > "can be made up of multiple transactions with multiple counterparties as long as the aggregate external hedge exactly matches the internal risk transfer, and the internal risk transfer exactly matches the aggregate external hedge."
  > — RBC25.21 ^rbc25-21

- Đáp ứng RBC25.21: exposure banking book được coi là phòng ngừa bởi chân banking book của IRT; chân trading book của IRT và hợp đồng phòng ngừa bên ngoài đều tính vốn rủi ro thị trường. Không đáp ứng: exposure không được coi là phòng ngừa; hợp đồng phòng ngừa bên ngoài tính đủ vào vốn rủi ro thị trường, chân trading book của IRT bị loại hoàn toàn.
  > "Moreover both the trading book leg of the internal risk transfer and the external hedge must be included in the market risk capital requirements."
  > "Moreover, the third-party external hedge must be fully included in the market risk capital requirements and the trading book leg of the internal risk transfer must be fully excluded from the market risk capital requirements."
  > — RBC25.22–25.23 ^rbc25-22

- Vị thế short tín dụng hoặc cổ phiếu trong banking book do IRT tạo ra (phòng ngừa quá mức) mà không tính vốn theo quy tắc banking book phải tính vốn theo quy tắc rủi ro thị trường.
  > "A banking book short credit position or a banking book short equity position created by an internal risk transfer"
  > "and not capitalised under banking book rules must be capitalised under the market risk rules together with the trading book exposure."
  > — RBC25.24 ^rbc25-24

- Khi phòng ngừa rủi ro lãi suất của banking book bằng IRT với trading book, chân trading book chỉ được xử lý như công cụ trading book khi và chỉ khi: IRT được lập hồ sơ về rủi ro lãi suất banking book được phòng ngừa và nguồn rủi ro; IRT thực hiện với một desk IRT chuyên trách được cơ quan giám sát phê duyệt riêng cho mục đích này; IRT chịu vốn trading book trên cơ sở độc lập cho desk đó, tách khỏi GIRR và rủi ro thị trường khác của trading book.
  > "When a bank hedges a banking book interest rate risk exposure using an internal risk transfer with its trading book, the trading book leg of the internal risk transfer is treated as a trading book instrument under the market risk framework if and only if:"
  > "(1) the internal risk transfer is documented with respect to the banking book interest rate risk being hedged and the sources of such risk;"
  > "(2) the internal risk transfer is conducted with a dedicated internal risk transfer trading desk which has been specifically approved by the supervisor for this purpose; and"
  > "(3) the internal risk transfer must be subject to trading book capital requirements under the market risk framework on a stand-alone basis for the dedicated internal risk transfer desk, separate from any other GIRR or other market risks generated by activities in the trading book."
  > — RBC25.25 ^rbc25-25

- Desk IRT cho GIRR không cần có trader hay tài khoản kinh doanh; chỉ áp yêu cầu định lượng (kiểm định PLA và backtesting theo MAR32), không áp tiêu chí định tính MAR12.4; desk không được giữ vị thế trading book nào ngoài GIRR IRT giữa hai sổ và hợp đồng phòng ngừa bên ngoài đủ điều kiện RBC25.27.
  > "GIRR IRTs may be allocated to a trading desk that need not have traders or trading accounts assigned to it. For a GIRR IRT trading desk, only the quantitative trading desk requirements (ie profit and loss attribution test and backtesting) set out in MAR32 apply."
  > "A GIRR IRT desk must not have any trading book positions allocated to it, except GIRR IRTs between the trading book and the banking book as well as any external hedges that meet the conditions specified in RBC25.27."
  > — RBC25.25 FAQ1 ^rbc25-25-faq1

- Khi đáp ứng RBC25.25, chân banking book của IRT phải được đưa vào phép đo rủi ro lãi suất của banking book cho mục đích vốn quy định.
  > "Where the requirements in RBC25.25 are fulfilled, the banking book leg of the internal risk transfer must be included in the banking book's measure of interest rate risk exposures for regulatory capital purposes."
  > — RBC25.26 ^rbc25-26

- Desk IRT được cơ quan giám sát phê duyệt có thể mua công cụ trực tiếp từ thị trường, hoặc qua một desk không phải IRT làm đại lý nếu GIRR IRT với desk đó khớp chính xác hợp đồng phòng ngừa từ thị trường.
  > "The supervisor-approved internal risk transfer desk may include instruments purchased from the market (ie external parties to the bank). Such transactions may be executed directly between the internal risk transfer desk and the market."
  > "Alternatively, the internal risk transfer desk may obtain the external hedge from the market via a separate non-internal risk transfer trading desk acting as an agent, if and only if the GIRR internal risk transfer entered into with the noninternal risk transfer trading desk exactly matches the external hedge from the market."
  > — RBC25.27 ^rbc25-27

- IRT giữa các trading desk trong phạm vi vốn rủi ro thị trường (kể cả rủi ro ngoại hối và hàng hoá của banking book) thường được công nhận về vốn; IRT giữa desk IRT và desk khác chỉ được công nhận khi đáp ứng RBC25.25–25.27.
  > "Internal risk transfers between trading desks within the scope of application of the market risk capital requirements (including FX risk and commodities risk in the banking book) will generally receive regulatory capital recognition."
  > — RBC25.28 ^rbc25-28

- Chân trading book của IRT phải đáp ứng cùng yêu cầu RBC25 như công cụ trading book giao dịch với đối tác bên ngoài.
  > "The trading book leg of internal risk transfers must fulfil the same requirements under RBC25 as instruments in the trading book transacted with external counterparties."
  > — RBC25.29 ^rbc25-29

#### 6. Phòng ngừa CVA và IRT với danh mục CVA

- Hợp đồng phòng ngừa bên ngoài đủ điều kiện đã tính vào vốn CVA phải loại khỏi phép tính vốn rủi ro thị trường.
  > "Eligible external hedges that are included in the credit valuation adjustment (CVA) capital requirement must be removed from the bank's market risk capital requirement calculation."
  > — RBC25.30 ^rbc25-30

- IRT giữa danh mục CVA và trading book gồm phía CVA (tính vốn CVA, loại khỏi vốn rủi ro thị trường) và phía không CVA (tính vốn rủi ro thị trường); chỉ được công nhận khi lập hồ sơ về rủi ro CVA được phòng ngừa và nguồn rủi ro.
  > "Where the CVA portfolio side of an internal risk transfer is recognised in the CVA risk capital requirement, the CVA portfolio side should be excluded from the market risk capital requirement, while the non-CVA portfolio side should be included in the market risk capital requirement."
  > "In any case, such internal CVA risk transfers can only receive regulatory capital recognition if the internal risk transfer is documented with respect to the CVA risk being hedged and the sources of such risk."
  > — RBC25.31–25.32 ^rbc25-31

- IRT CVA chịu curvature, default risk hoặc residual risk add-on chỉ được công nhận khi trading book có thêm hợp đồng phòng ngừa bên ngoài khớp chính xác; IRT giữa danh mục CVA và trading book có thể dùng phòng ngừa counterparty credit risk của phái sinh nếu đáp ứng RBC25.21.
  > "may be recognised in the CVA portfolio capital requirement and market risk capital requirement only if the trading book additionally enters into an external hedge with an eligible thirdparty protection provider that exactly matches the internal risk transfer."
  > "internal risk transfers between the CVA portfolio and the trading book can be used to hedge the counterparty credit risk exposure of a derivative instrument in the trading or banking book as long as the requirements of RBC25.21 are met."
  > — RBC25.33–25.34 ^rbc25-33

### SRP30 — Risk management

#### 1. Phạm vi, ICAAP và Pillar 2

- SRP30 nêu nguyên tắc quản trị rủi ro cho các rủi ro được nhận diện qua quy trình Pillar 2; phiên bản hiệu lực từ 15/12/2019.
  > "The risk management principles in this chapter reinforce how banks should manage and mitigate their risks that are identified through the Pillar 2 process."
  > "Version effective as of 15 Dec 2019"
  > — SRP30 ^srp30-0

- Quy trình quản trị rủi ro vững chắc là cần thiết để cơ quan giám sát và thị trường tin vào đánh giá hồ sơ rủi ro và đánh giá nội bộ về mức đủ vốn của ngân hàng.
  > "Sound risk management processes are necessary to support supervisory and market participants' confidence in banks' assessments of their risk profiles and internal capital adequacy assessments."
  > — SRP30.1 ^srp30-1

- ICAAP nên được thực hiện trên cơ sở hợp nhất, và ở cấp pháp nhân của từng ngân hàng trong tập đoàn khi cơ quan giám sát thấy cần; ICAAP nên gồm stress testing để bổ trợ và kiểm chứng các phương pháp định lượng, định tính khác.
  > "A financial institution's internal capital adequacy assessment process (ICAAP) should be conducted on a consolidated basis and, when deemed necessary by the appropriate supervisors, at the legal entity level for each bank in the group."
  > "the ICAAP should incorporate stress testing to complement and help validate other quantitative and qualitative approaches"
  > — SRP30.2 ^srp30-2

- Ngân hàng nên phân tích công cụ vốn và khả năng hấp thụ lỗ của chúng khi stress; ICAAP nên xét nhu cầu ngắn hạn và dài hạn, cân nhắc tích luỹ vốn dư trong giai đoạn thuận lợi của chu kỳ tín dụng; chênh lệch giữa ICAAP và đánh giá Pillar 2 của cơ quan giám sát nên dẫn tới đối thoại tương xứng với mức chênh lệch.
  > "A bank should also perform a careful analysis of its capital instruments and their potential performance during times of stress, including their ability to absorb losses and support ongoing business operations."
  > "A bank's ICAAP should address both shortand long-term needs and consider the prudence of building excess capital over benign periods of the credit cycle"
  > "Differences between the capital assessment under a bank's ICAAP and the supervisory assessment of capital adequacy made under Pillar 2 should trigger a dialogue that is proportionate to the depth and nature of such differences."
  > — SRP30.2 ^srp30-2b

- ICAAP là quy trình do ngân hàng dẫn dắt, nên dựa trên quy trình quản trị rủi ro nội bộ; một ICAAP có thể dùng cho cả mục đích nội bộ và giám sát.
  > "The ICAAP is a bank-driven process that should leverage off an institution's internal risk management processes. A single ICAAP may be used for internal and regulatory purposes."
  > — SRP30.2 fn ^srp30-2c

- Yêu cầu vốn Pillar 1 là mức tối thiểu; mọi rủi ro nội bảng và ngoại bảng nên được phủ đủ vốn, kể cả qua Pillar 2 vượt mức tối thiểu Pillar 1; một phần gồm việc sử dụng bộ đệm vốn tích luỹ trong giai đoạn tốt; ngân hàng quan trọng hệ thống bắt buộc phải có khả năng hấp thụ cú sốc.
  > "Pillar 1 capital requirements represent minimum requirements."
  > "All of a bank's risks – both on- and off-balance sheet, and particularly those risks related to complex capital market activities – should be adequately covered by capital, including through Pillar 2 in excess of minimum Pillar 1 requirements."
  > "This should, in part, include drawing down on the capital buffer built-up during good times."
  > "it is imperative that systemically important banks have the shock absorption capability to adequately protect against severe stress events."
  > — SRP30.3 ^srp30-3

- Mức chi tiết của chương trình quản trị rủi ro nên tương xứng với quy mô, độ phức tạp và mức rủi ro ngân hàng chấp nhận (áp dụng theo nguyên tắc tương xứng).
  > "The detail and sophistication of a bank's risk management programmes should be commensurate with the size and complexity of its business and the overall level of risk that the bank accepts."
  > — SRP30.4 ^srp30-4

- Cơ quan giám sát nên xác định ngân hàng có khung quản trị rủi ro toàn hàng cho phép định nghĩa khẩu vị rủi ro và nhận diện mọi rủi ro trọng yếu (tập trung, chứng khoán hoá, ngoại bảng, thực hành định giá…); bốn cách đạt được gồm nhận diện–đo lường–kiểm soát rủi ro, báo cáo rõ cho HĐQT và ban điều hành, stress testing liên tục, và chuẩn nội bộ tối thiểu cho dự phòng, vốn và tài trợ dự phòng.
  > "Supervisors should determine whether a bank has in place a sound firm-wide risk management framework that enables it to define its risk appetite and recognise all material risks, including the risks posed by concentrations, securitisation, offbalance sheet exposures, valuation practices and other risk exposures."
  > "adequately identifying, measuring, monitoring, controlling and mitigating these risks;"
  > "clearly communicating the extent and depth of these risks in an easily understandable, but accurate, manner in reports to senior management and the board of directors, as well as in published financial reports;"
  > "conducting ongoing stress testing to identify potential losses and liquidity needs under adverse circumstances; and"
  > "setting adequate minimum internal standards for allowances or liabilities for losses, capital, and contingency funding."
  > — SRP30.5 ^srp30-5

- Các yếu tố ở SRP30.5 nên được đưa vào hệ thống quản trị rủi ro và ICAAP vì Pillar 1 không bao quát hết.
  > "These elements should be adequately incorporated into a bank's risk management system and ICAAP specifically since they are not fully captured by Pillar 1 of the Basel III framework."
  > — SRP30.6 ^srp30-6

#### 2. Giám sát rủi ro toàn hàng (firm-wide risk oversight)

- Hệ thống quản trị rủi ro vững chắc nên có năm đặc điểm: HĐQT và ban điều hành giám sát tích cực; chính sách, quy trình và hạn mức phù hợp; nhận diện, đo lường, giảm thiểu, kiểm soát, theo dõi và báo cáo rủi ro toàn diện, kịp thời; MIS ở cấp mảng kinh doanh và toàn hàng; kiểm soát nội bộ toàn diện.
  > "A sound risk management system should have the following key features:"
  > "active board and senior management oversight;"
  > "appropriate policies, procedures and limits;"
  > "comprehensive and timely identification, measurement, mitigation, controlling, monitoring and reporting of risks;"
  > "appropriate management information systems (MIS) at the business and firm-wide level; and"
  > "comprehensive internal controls."
  > — SRP30.7 ^srp30-7

- HĐQT và ban điều hành chịu trách nhiệm xác định khẩu vị rủi ro và bảo đảm khung quản trị rủi ro có hạn mức thận trọng toàn hàng nhất quán với khẩu vị và năng lực chấp nhận rủi ro; ban điều hành phải vượt qua tình trạng chia cắt giữa các mảng kinh doanh; quy trình nên bao gồm mọi rủi ro trọng yếu, kể cả rủi ro danh tiếng, pháp lý, chiến lược và rủi ro chỉ trọng yếu khi kết hợp.
  > "It is the responsibility of the board of directors and senior management to define the institution's risk appetite and to ensure that the bank's risk management framework includes detailed policies that set specific firm-wide prudential limits on the bank's activities, which are consistent with its risk taking appetite and capacity."
  > "senior management must overcome organisational silos between business lines and share information on market developments, risks and risk mitigation techniques."
  > "Senior management should establish a risk management process that is not limited to credit, market, liquidity and operational risks, but incorporates all material risks. This includes reputational, legal and strategic risks, as well as risks that do not appear to be significant in isolation, but when combined with other risks could lead to material losses."
  > — SRP30.8 ^srp30-8

- "HĐQT" và "ban điều hành" trong SRP30 là nhãn của hai chức năng ra quyết định, không chỉ cấu trúc pháp lý cụ thể.
  > "the notions of the board of directors and senior management are used in this paper not to identify legal constructs but rather to label two decision-making functions within a bank."
  > — SRP30.8 fn ^srp30-8b

- Với sản phẩm, hoạt động mới hoặc phức tạp, ban điều hành nên hiểu giả định về mô hình kinh doanh, định giá, quản trị rủi ro và đánh giá rủi ro nếu giả định sai.
  > "With respect to new or complex products and activities, senior management should understand the underlying assumptions regarding business models, valuation and risk management practices. In addition, senior management should evaluate the potential risk exposure if those assumptions fail."
  > — SRP30.9 ^srp30-9

- Trước khi triển khai hoạt động hoặc sản phẩm mới, HĐQT và ban điều hành nên rà soát thay đổi rủi ro toàn hàng và bảo đảm hạ tầng, kiểm soát nội bộ sẵn sàng; nên xét khó khăn định giá và diễn biến của sản phẩm khi kinh tế stress.
  > "Before embarking on new activities or introducing products new to the institution, the board and senior management should identify and review the changes in firm-wide risks arising from these potential new products or activities and ensure that the infrastructure and internal controls necessary to manage the related risks are in place."
  > "a bank should also consider the possible difficulty in valuing the new products and how they might perform in a stressed economic environment."
  > — SRP30.10 ^srp30-10

- Chức năng quản lý rủi ro và CRO (hoặc vị trí tương đương) nên độc lập với các mảng kinh doanh, báo cáo trực tiếp CEO và HĐQT; nên báo cáo các vấn đề như tập trung rủi ro và vi phạm hạn mức khẩu vị rủi ro.
  > "A bank's risk function and its chief risk officer or equivalent position should be independent of the individual business lines and report directly to the chief executive officer and the institution's board of directors."
  > "the risk function should highlight to senior management and the board risk management concerns, such as risk concentrations and violations of risk appetite limits."
  > — SRP30.11 ^srp30-11

- Hạn mức nội bộ nên xét vai trò của ngân hàng trong hệ thống tài chính và được xác định theo vốn, tổng tài sản, thu nhập hoặc mức rủi ro tổng thể.
  > "These limits should consider the bank's role in the financial system and be defined in relation to the bank's capital, total assets, earnings or, where adequate measures exist, its overall risk level."
  > — SRP30.12 ^srp30-12

- Chính sách, quy trình và hạn mức nên: ghi nhận đầy đủ bản chất kinh tế của rủi ro (gồm rủi ro danh tiếng, bất định định giá); phân định trách nhiệm và tách bạch mảng kinh doanh với chức năng rủi ro; leo thang và xử lý vi phạm hạn mức trạng thái; rà soát hoạt động, sản phẩm mới với mọi bộ phận liên quan trước khi triển khai; có lịch rà soát, cập nhật định kỳ.
  > "ensure that the economic substance of a bank's risk exposures, including reputational risk and valuation uncertainty, are fully recognised and incorporated into the bank's risk management processes;"
  > "clearly delineate accountability and lines of authority across the bank's various business activities, and ensure there is a clear separation between business lines and the risk function;"
  > "escalate and address breaches of internal position limits;"
  > "provide for the review of new businesses and products by bringing together all relevant risk management, control and business lines to ensure that the bank is able to manage and control the activity prior to it being initiated; and"
  > "include a schedule and process for reviewing the policies, procedures and limits and for updating them as appropriate."
  > — SRP30.13 ^srp30-13

- MIS nên cung cấp cho HĐQT và ban điều hành thông tin kịp thời về hồ sơ rủi ro, gồm mọi rủi ro kể cả ngoại bảng.
  > "A bank's MIS should provide the board and senior management in a clear and concise manner with timely and relevant information concerning their institutions' risk profile. This information should include all risk exposures, including those that are off-balance sheet."
  > — SRP30.14 ^srp30-14

- Tổng hợp rủi ro cần hạ tầng và MIS cho phép tổng hợp trạng thái và thước đo rủi ro xuyên các mảng kinh doanh và nhận diện tập trung, rủi ro mới nổi.
  > "allow for the aggregation of exposures and risk measures across business lines and"
  > "support customised identification of concentrations"
  > — SRP30.15 ^srp30-15

- MIS nên ghi nhận vi phạm hạn mức và có quy trình báo cáo kịp thời lên ban điều hành; trạng thái tương tự nên được tổng hợp xuyên banking book và trading book để phát hiện tập trung hoặc vi phạm hạn mức.
  > "A bank's MIS should be capable of capturing limit breaches and there should be procedures in place to promptly report such breaches to senior management, as well as to ensure that appropriate follow-up actions are taken."
  > "similar exposures should be aggregated across business platforms (including the banking and trading books) to determine whether there is a concentration or a breach of an internal position limit."
  > — SRP30.16 ^srp30-16

- Hệ thống nên đủ linh hoạt để đưa phòng ngừa và giảm thiểu rủi ro toàn hàng vào, có tính đến basis risk liên quan.
  > "a bank's systems should be flexible enough to incorporate hedging and other risk mitigation actions to be carried out on a firmwide basis while taking into account the various related basis risks."
  > — SRP30.17 ^srp30-17

- MIS nên đủ linh hoạt để tạo phân tích kịch bản hướng tới tương lai cho toàn hàng; đầu vào bên thứ ba và công cụ trong MIS (xếp hạng tín dụng, thước đo rủi ro, mô hình) nên được kiểm định ban đầu và liên tục.
  > "it should be sufficiently flexible so that the institution can generate forward-looking bank-wide scenario analyses"
  > "Third-party inputs or other tools used within MIS (eg credit ratings, risk measures, models) should be subject to initial and ongoing validation."
  > — SRP30.18 ^srp30-18

- Quy trình quản trị rủi ro nên được bộ phận kiểm soát độc lập, kiểm toán nội bộ và bên ngoài theo dõi, kiểm tra thường xuyên; chức năng quản lý rủi ro phải độc lập với mảng kinh doanh.
  > "Risk management processes should be frequently monitored and tested by independent control areas and internal, as well as external, auditors."
  > "The risk management function of banks must be independent of the business lines in order to ensure an adequate separation of duties and to avoid conflicts of interest."
  > — SRP30.19 ^srp30-19

#### 3. Rủi ro tập trung (risk concentration)

- Ngân hàng nên tổng hợp mọi trạng thái trực tiếp và gián tiếp tương tự bất kể nơi hạch toán; tập trung rủi ro là trạng thái đơn lẻ hoặc nhóm trạng thái tương tự có thể gây (i) tổn thất đủ lớn so với thu nhập, vốn, tổng tài sản hoặc mức rủi ro để đe doạ khả năng duy trì hoạt động cốt lõi, hoặc (ii) thay đổi trọng yếu hồ sơ rủi ro; nên phân tích ở cả cấp pháp nhân và hợp nhất.
  > "A bank should aggregate all similar direct and indirect exposures regardless of where the exposures have been booked."
  > "A risk concentration is any single exposure or group of similar exposures (eg to the same borrower or counterparty, including protection providers, geographic area, industry or other risk factors) with the potential to produce (i) losses large enough (relative to a bank's earnings, capital, total assets or overall risk level) to threaten a bank's creditworthiness or ability to maintain its core operations or (ii) a material change in a bank's risk profile."
  > "Risk concentrations should be analysed on both a bank legal entity and consolidated basis"
  > — SRP30.20 ^srp30-20

- Ngân hàng nên xét tập trung dựa trên yếu tố rủi ro chung hoặc tương quan, như tương quan giữa rủi ro thị trường, tín dụng và thanh khoản.
  > "A bank should consider concentrations that are based on common or correlated risk factors that reflect more subtle or more situation-specific factors than traditional concentrations, such as correlations between market, credit risks and liquidity risk."
  > — SRP30.21 ^srp30-21

- Chín tình huống điển hình phát sinh tập trung: một đối tác/nhóm liên quan; ngành, lĩnh vực (kể cả định chế tài chính không chịu giám sát); vùng địa lý; kỹ thuật giảm thiểu rủi ro tín dụng (cùng loại TSBĐ, cùng bên bảo đảm); trạng thái kinh doanh/rủi ro thị trường; đối tác qua thực hiện, xử lý giao dịch; nguồn vốn; tài sản ở banking book hoặc trading book; trạng thái ngoại bảng (bảo lãnh, hạn mức thanh khoản, cam kết).
  > "The typical situations in which risk concentrations can arise include:"
  > "exposures to a single counterparty, borrower or group of connected counterparties or borrowers;"
  > "exposures arising from credit risk mitigation techniques, including exposure to similar collateral types or to a single or closely related credit protection provider;"
  > "funding sources;"
  > "off-balance sheet exposures, including guarantees, liquidity lines and other commitments."
  > — SRP30.22 ^srp30-22

- Ngân hàng nên có quy trình có hệ thống để nhận diện tương quan cao giữa tín nhiệm của bên bảo đảm và người có nghĩa vụ của khoản cơ sở ("wrong way risk").
  > "A bank should have in place adequate, systematic procedures for identifying high correlation between the creditworthiness of a protection provider and the obligors of the underlying exposures due to their performance being dependent on common factors beyond systematic risk (ie "wrong way risk")."
  > — SRP30.24 ^srp30-24

- Ngân hàng nên có chiến lược giảm thiểu tập trung được ban điều hành phê duyệt, có thể gồm đổi chiến lược kinh doanh, giảm hạn mức hoặc tăng đệm vốn.
  > "A bank should have credible risk mitigation strategies in place that have senior management approval. This may include altering business strategies, reducing limits or increasing capital buffers in line with the desired risk profile."
  > — SRP30.25 ^srp30-25

- Kỹ thuật đo tập trung gồm sốc yếu tố rủi ro, kịch bản cấp mảng và toàn hàng, stress testing tích hợp và mô hình vốn kinh tế; ngân hàng nên đặt hạn mức trạng thái nội bộ cho tập trung.
  > "These techniques include shocks to various risk factors; use of business level and firm-wide scenarios; and the use of integrated stress testing and economic capital models."
  > "a bank should establish internal position limits for concentrations to which it may be exposed."
  > — SRP30.26 ^srp30-26

- Đánh giá tập trung trong ICAAP không nên máy móc mà theo điểm yếu riêng của mô hình kinh doanh; mức vốn phù hợp cho tập trung nên được đưa vào ICAAP và đánh giá Pillar 2.
  > "should not be a mechanical process, but one in which each bank determines, depending on its business model, its own specific vulnerabilities."
  > "An appropriate level of capital for risk concentrations should be incorporated in a bank's ICAAP, as well as in Pillar 2 assessments."
  > — SRP30.27 ^srp30-27

- Ngân hàng nên xét cả sự tích tụ tập trung khi thị trường stress, suy thoái và mất thanh khoản; kịch bản nên kết hợp tích tụ trạng thái pipeline với mất thanh khoản thị trường và giảm giá tài sản.
  > "Not only should normal market conditions be considered, but also the potential build-up of concentrations under stressed market conditions, economic downturns and periods of general market illiquidity."
  > "The scenarios should also combine the potential build-up of pipeline exposures together with the loss of market liquidity and a significant decline in asset values."
  > — SRP30.28 ^srp30-28

#### 4. Rủi ro danh tiếng (reputational risk)

- Định nghĩa: rủi ro phát sinh từ nhận thức tiêu cực của khách hàng, đối tác, cổ đông, nhà đầu tư, chủ nợ, nhà phân tích hoặc cơ quan quản lý, ảnh hưởng tới khả năng duy trì, thiết lập quan hệ kinh doanh và tiếp cận nguồn vốn.
  > "Reputational risk can be defined as the risk arising from negative perception on the part of customers, counterparties, shareholders, investors, debt-holders, market analysts, other relevant parties or regulators that can adversely affect a bank's ability to maintain existing, or establish new, business relationships and continued access to sources of funding (eg through the interbank or securitisation markets)."
  > — SRP30.29 ^srp30-29

- Rủi ro danh tiếng có thể dẫn tới hỗ trợ ngầm (implicit support), từ đó phát sinh rủi ro tín dụng, thanh khoản, thị trường, pháp lý; rủi ro này nên được đưa vào quy trình quản trị rủi ro, ICAAP và kế hoạch dự phòng thanh khoản.
  > "Reputational risk can lead to the provision of implicit support, which may give rise to credit, liquidity, market and legal risk – all of which can have a negative impact on a bank's earnings, liquidity and capital position."
  > "The risks that arise should be incorporated into the bank's risk management processes and appropriately addressed in its ICAAP and liquidity contingency plans."
  > — SRP30.30 ^srp30-30

- Khi stress (trước biến động 2007), một số ngân hàng đã hỗ trợ vượt nghĩa vụ hợp đồng cho các cấu trúc chứng khoán hoá và vehicle ngoại bảng do mình bảo trợ.
  > "In stressed conditions some firms went beyond their contractual obligations to support their sponsored securitisations and off-balance sheet vehicles."
  > — SRP30.31 ^srp30-31

- Nguồn rủi ro danh tiếng ví dụ: bảo trợ ABCP conduit, SIV, bán khoản tín dụng cho trust chứng khoán hoá; bảo trợ quỹ thị trường tiền tệ, hedge fund nội bộ, REIT.
  > "Reputational risk may arise, for example, from a bank's sponsorship of securitisation structures such as asset-backed commercial paper conduits and SIVs, as well as from the sale of credit exposures to securitisation trusts."
  > "Reputational risk also arises when a bank sponsors activities such as money market mutual funds, in-house hedge funds and real estate investment trusts."
  > — SRP30.32 ^srp30-32

- Rủi ro danh tiếng có thể tác động lên nợ phải trả: để tránh tổn hại uy tín, ngân hàng có thể gọi (mua lại) nợ dù làm xấu hồ sơ thanh khoản, đặc biệt với nợ là cấu phần vốn quy định như nợ hybrid/thứ cấp.
  > "Reputational risk also may affect a bank's liabilities, since market confidence and a bank's ability to fund its business are closely related to its reputation. For instance, to avoid damaging its reputation, a bank may call its liabilities even though this might negatively affect its liquidity profile. This is particularly true for liabilities that are components of regulatory capital, such as hybrid/subordinated debt."
  > — SRP30.33 ^srp30-33

- Quy trình stress testing nên tính đến rủi ro danh tiếng và hiệu ứng vòng hai.
  > "a bank's stress testing procedures should take account of reputational risk so management has a firm understanding of the consequences and second round effects of reputational risk."
  > — SRP30.34 ^srp30-34

- Ngân hàng nên đo mức hỗ trợ có thể phải cung cấp (kể cả hỗ trợ ngầm cho chứng khoán hoá) hoặc tổn thất khi thị trường bất lợi, có thể qua kịch bản rủi ro danh tiếng trong stress test định kỳ, hoặc so sánh trạng thái nội bảng với mức phơi nhiễm ngoại bảng tối đa.
  > "it should measure the amount of support it might have to provide (including implicit support of securitisations) or losses it might experience under adverse market conditions."
  > "This could be accomplished by including reputational risk scenarios in regular stress tests."
  > "Methodologies also could include comparing the actual amount of exposure carried on the balance sheet versus the maximum exposure amount held off-balance sheet, that is, the potential amount to which the bank could be exposed."
  > — SRP30.35 ^srp30-35

- Ngân hàng nên chú ý tác động của rủi ro danh tiếng lên vị thế thanh khoản tổng thể, gồm khả năng tài sản tăng và nguồn vốn bị hạn chế.
  > "A bank should pay particular attention to the effects of reputational risk on its overall liquidity position, taking into account both possible increases in the asset side of the balance sheet and possible restrictions on funding"
  > — SRP30.36 ^srp30-36

#### 5. Thực hành định giá (valuation practices)

- BCBS ban hành hướng dẫn giám sát thực hành định giá hợp lý (fair value) công cụ tài chính tháng 4/2009, áp dụng cho mọi trạng thái đo theo fair value và mọi thời điểm, không chỉ khi stress.
  > "the Basel Committee published Supervisory guidance for assessing banks' financial instrument fair value practices in April 2009."
  > "This guidance applies to all positions that are measured at fair value and at all times, not only during times of stress."
  > — SRP30.37 ^srp30-37

- Khi không có giá minh bạch từ thị trường thanh khoản, định giá phải dựa vào mô hình, phương pháp giá đại diện và phán đoán chuyên gia.
  > "The absence of a transparent price from a liquid market means that the valuation must rely on models or proxy-pricing methodologies, as well as on expert judgment."
  > — SRP30.38 ^srp30-38

- Ngân hàng được kỳ vọng có cấu trúc quản trị và quy trình kiểm soát định giá hợp lý cho cả quản trị rủi ro và báo cáo tài chính; HĐQT nên nhận báo cáo về giám sát định giá, hiệu quả mô hình định giá và thay đổi chính sách định giá trọng yếu.
  > "a bank is expected to have adequate governance structures and control processes for fair valuing exposures for risk management and financial reporting purposes."
  > "the board should receive reports from senior management on the valuation oversight and valuation model performance issues that are brought to senior management for resolution, as well as all significant changes to valuation policies."
  > — SRP30.39 ^srp30-39

- Phê duyệt phương pháp định giá nên được lập hồ sơ; quy trình duyệt sản phẩm mới nên gồm mọi bên liên quan tới đo lường rủi ro, kiểm soát rủi ro và xác minh định giá.
  > "Policies should ensure that the approvals of all valuation methodologies are well documented."
  > "New product approval processes should include all internal stakeholders relevant to risk measurement, risk control, and the assignment and verification of valuations of financial instruments."
  > — SRP30.40 ^srp30-40

- Kiểm soát định giá nên nhất quán giữa các công cụ tương tự và giữa các sổ, và chịu kiểm toán nội bộ.
  > "valuation controls should be applied consistently across similar instruments (risks) and consistent across business lines (books). These controls should be subject to internal audit."
  > — SRP30.41 ^srp30-41

- Với trạng thái rủi ro trọng yếu, ngân hàng được kỳ vọng có năng lực định giá bằng phương pháp thay thế khi đầu vào chính không còn tin cậy; ngân hàng phải kiểm tra hiệu quả mô hình trong điều kiện stress.
  > "for those exposures that represent material risk, a bank is expected to have the capacity to produce valuations using alternative methods in the event that primary inputs and approaches become unreliable, unavailable or not relevant due to market discontinuities or illiquidity. A bank must test and review the performance of its models under stress conditions so that it understands the limitations of the models under stress conditions."
  > — SRP30.42 ^srp30-42

- Ở thị trường hoạt động, ngân hàng nên tối đa hoá đầu vào quan sát được và tối thiểu hoá đầu vào không quan sát được; tám tiêu chí đánh giá độ tin cậy của nguồn giá (tần suất báo giá, giao dịch thực, độ phủ dữ liệu, tính kịp thời, số nguồn độc lập, giao dịch hỗ trợ, độ trưởng thành thị trường, độ tương đồng công cụ).
  > "Where values are determined to be in an active market, a bank should maximise the use of relevant observable inputs and minimise the use of unobservable inputs when estimating fair value using a valuation technique."
  > "In assessing whether a source is reliable and relevant, a bank should consider, among other things:"
  > — SRP30.43 ^srp30-43

- Ban điều hành nên cân nhắc công bố thông tin về bất định định giá có ý nghĩa hơn, ví dụ độ nhạy của fair value với đầu vào mô hình và tác động của kịch bản stress.
  > "Senior management should consider whether disclosures around valuation uncertainty can be made more meaningful."
  > "the sensitivity of fair values to modelling inputs and assumptions; and the impact of stress scenarios on valuations."
  > — SRP30.44 ^srp30-44

#### 6. Stress testing

- Stress testing là cấu phần của quản trị rủi ro và công cụ cốt lõi của giám sát; chỉ ra nguồn lực tài chính có thể cần để hấp thụ tổn thất khi có cú sốc lớn.
  > "Stress testing is a critical element of risk management for banks and a core tool for banking supervisors and macroprudential authorities."
  > "provides an indication to banks and supervisory authorities of the financial resources that might be needed to absorb losses should large shocks occur."
  > — SRP30.45 ^srp30-45

- BCBS có bộ Stress testing principles (10/2018) cho ngân hàng lớn hoạt động quốc tế; BCBS kỳ vọng stress testing được lồng vào quản trị rủi ro và giám sát của ngân hàng hoạt động quốc tế.
  > "the Committee has in place Stress testing principles"
  > "Stress testing principles, Basel Committee on Banking Supervision, October 2018"
  > "the Basel Committee expects that for internationally active banks, stress testing is embedded as a critical component of sound risk management and supervisory oversight."
  > — SRP30.46 ^srp30-46

- Các nguyên tắc áp dụng tương xứng theo quy mô, độ phức tạp và hồ sơ rủi ro; ngân hàng nhỏ có thể dùng phương pháp đơn giản hơn thay cho khung stress testing chính thức.
  > "The principles are intended to be applied on a proportionate basis, depending on size, complexity and risk profile of the bank or banking sector for which the authority is responsible."
  > "smaller banks and authorities in all jurisdictions can benefit from considering in a structured way the potential impact of adverse scenarios on their business, even if they are not using a formal stress testing framework but are instead using simpler methods."
  > — SRP30.47 ^srp30-47

#### 7. Quản trị rủi ro thanh khoản

- Ngân hàng nên quản lý rủi ro thanh khoản chặt chẽ và duy trì đủ thanh khoản để chịu được nhiều loại sự kiện stress (tham chiếu Principles for Sound Liquidity Risk Management and Supervision, 9/2008).
  > "A bank should both assiduously manage its liquidity risk and also maintain sufficient liquidity to withstand a range of stress events."
  > "See also the Basel Committee's Principles for Sound Liquidity Risk Management and Supervision, September 2008."
  > — SRP30.48 ^srp30-48

- Quy trình nên dự phóng dòng tiền tài sản, nợ và ngoại bảng theo nhiều kỳ hạn, đa dạng hoá kỳ hạn và nguồn vốn; nên dùng chỉ báo cảnh báo sớm; kiểm soát thanh khoản xuyên pháp nhân, mảng và đồng tiền có tính tới hạn chế chuyển giao thanh khoản.
  > "This process should involve the ability to project cash flows arising from assets, liabilities and off-balance sheet items over various time horizons, and should ensure diversification in both the tenor and source of funding. A bank should utilise early warning indicators to identify the emergence of increased risk or vulnerabilities in its liquidity position or funding needs."
  > "taking into account any legal, regulatory and operational limitations to the transferability of liquidity."
  > — SRP30.49 ^srp30-49

- HĐQT đặt liquidity risk tolerance; ngân hàng nên đưa chi phí, lợi ích và rủi ro thanh khoản vào định giá nội bộ, đo lường hiệu quả và duyệt sản phẩm mới của mọi hoạt động kinh doanh trọng yếu.
  > "A key element in the management of liquidity risk is the need for strong governance of liquidity risk, including the setting of a liquidity risk tolerance by the board."
  > "a bank should appropriately price the costs, benefits and risks of liquidity into the internal pricing, performance measurement, and new product approval process of all significant business activities."
  > — SRP30.50 ^srp30-50

- Ngân hàng nên stress test thanh khoản định kỳ, phân tích tác động lên dòng tiền, vị thế thanh khoản, lợi nhuận và khả năng thanh toán; kết quả nên định hình kế hoạch tài trợ dự phòng (contingency funding planning).
  > "A bank should perform stress tests or scenario analyses on a regular basis in order to identify and quantify their exposures to possible future liquidity stresses, analysing possible impacts on the institutions' cash flows, liquidity positions, profitability, and solvency."
  > "The results of stress tests should also play a key role in shaping the bank's contingency funding"
  > "planning, which should outline policies for managing a range of stress events and clearly sets out strategies for addressing liquidity shortfalls in emergency situations."
  > — SRP30.51 ^srp30-51

- Ban điều hành nên xét quan hệ giữa thanh khoản và vốn: rủi ro thanh khoản ảnh hưởng mức đủ vốn, và mức đủ vốn lại có thể làm xấu hồ sơ thanh khoản.
  > "Senior management should consider the relationship between liquidity and capital since liquidity risk can impact capital adequacy which, in turn, can aggravate a bank's liquidity profile."
  > — SRP30.52 ^srp30-52

## Node bị ảnh hưởng
- SRP50 [2026-10-16]: xem log ingest SRP50.
- RBC25 [2026-10-19]: cập nhật [[banking-book]] (draft); tạo [[regulatory-internal-risk-transfer]]; đề xuất [[internal-risk-transfer]] (canonical).
- SRP30 [2026-10-20]: tạo [[reputational-risk]], [[firm-wide-risk-management]], [[valuation-governance]]; cập nhật [[icaap]], [[concentration-risk-management]], [[liquidity-risk-management]], [[risk-appetite]], [[risk-limits]], [[stress-testing]], [[new-product-approval]], [[three-lines-of-defence]], [[srep]] (draft); đề xuất [[funding-concentration-risk]] (canonical).

## Mâu thuẫn ghi nhận
- RBC25: không có. Khác biệt với TT83/2025 (ngưỡng thời gian tự doanh, xử lý repo) là khác jurisdiction, ghi ở bảng Basel vs VN của [[banking-book]].
- SRP30: không có. Khác biệt với TT83/2025 (nguồn vốn trong phạm vi rủi ro tập trung, chủ thể đặt tolerance/hạn mức, vị trí CRO) là khác jurisdiction, ghi ở bảng Basel vs VN của [[concentration-risk-management]], [[liquidity-risk-management]], [[firm-wide-risk-management]].
