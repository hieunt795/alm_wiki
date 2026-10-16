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
units_done: [SRP50]
updated: 2026-10-16
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
