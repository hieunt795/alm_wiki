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
units_done: [SRP50, RBC25]
updated: 2026-10-19
---

## Thông tin nguồn
- Issuer: Basel Committee on Banking Supervision ([[bcbs]])
- Tier T2, `doc_status: final`. Bản tổng hợp toàn bộ khuôn khổ Basel (Consolidated Framework) do website BIS sinh ngày 17/12/2025.
- Scope: File chuẩn mực bao quát toàn bộ các trụ cột Basel (Scope of application SCO, Capital CAP, Risk-based capital RBC, Credit risk CRE, Market risk MAR, Operational risk OPE, Leverage ratio LEV, Liquidity LCR & NSF, Large exposures LEX, Margin requirements MGN, Supervisory review SRP, Disclosure DIS).
- Raw: `01_sources/alm/Basel/BaselFramework/BaselFramework.md` (26.057 dòng); meta: `BaselFramework_meta.json`.
- Ghi chú: Các phần LCR, NSFR, LEV và IRRBB (d368) có file văn bản chuyên biệt riêng (`src-bcbs-lcr`, `src-bcbs-nsfr`, `src-bcbs-lev`, `src-bcbs-irrbb-2016`). Source note này dùng để quản lý việc ingest các chương độc lập trong bộ khung hợp nhất, mở đầu là **Chương SRP50 (Liquidity Monitoring Metrics)**.

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

## Node bị ảnh hưởng
- SRP50 [2026-10-16]: xem log ingest SRP50.
- RBC25 [2026-10-19]: cập nhật [[banking-book]] (draft); tạo [[regulatory-internal-risk-transfer]]; đề xuất [[internal-risk-transfer]] (canonical).

## Mâu thuẫn ghi nhận
- RBC25: không có. Khác biệt với TT83/2025 (ngưỡng thời gian tự doanh, xử lý repo) là khác jurisdiction, ghi ở bảng Basel vs VN của [[banking-book]].
