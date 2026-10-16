---
title: "Bank Asset-Liability Management — Fidelio Tata"
aliases: [src-tata-bank-alm, Tata Bank ALM, Bank ALM Tata]
type: source
source_id: src-tata-bank-alm
domains: [alm]
status: active
maturity: draft
tier: T4
doc_status: final
issuer: Fidelio Tata
published: 2025-01-01
effective:
raw: 01_sources/tata_bank_alm/Tata_Bank_ALM_2025.md
units_done: [u02, u03, u04, u05]
updated: 2026-10-16
---

## Thông tin nguồn
- Tác giả: Fidelio Tata.
- Chuyên khảo: *Bank Asset-Liability Management* (Palgrave Macmillan / Springer, 2025).
- Tier T4 (Tài liệu chuyên khảo ALM quốc tế cập nhật các khung quy chuẩn mới nhất).
- Raw: `01_sources/tata_bank_alm/Tata_Bank_ALM_2025.md` (3.346 dòng).
- Units covered:
  - `u02`: 1.1.3 Purpose of ALM, 1.1.5 Banking Book vs. Trading Book & 1.1.6 Instruments Used in ALM (lines 410–815)
  - `u03`: 2.1 Economic Value Measures & 2.2 Earnings Measures (lines 816–1242)
  - `u04`: 2.2.4.3 Total Baseline NII, Mô phỏng NII kịch bản sốc, Phòng hộ NII bằng Receiver Swap & Xung đột EVE vs NII, FTP Structural Contribution (lines 1243–1662)
  - `u05`: 2.4 Embedded & Behavioral Options, 2.5 Replicating Portfolio Model & Rolling Portfolio (lines 1663–2068)

## Tóm tắt
Cuốn sách cung cấp phương pháp luận chi tiết và các mô hình số học mô phỏng cho quản trị ALM hiện đại:
- **Phân định Banking Book vs Trading Book & Phạm vi IRRBB (u02)**: Phân tách ranh giới giữa Sổ ngân hàng (hoạt động kinh doanh khách hàng và tài trợ dài hạn) và Sổ kinh doanh (tự doanh, giao dịch ngắn hạn). Xác định các nhóm công cụ thuộc phạm vi IRRBB (Customer business, External positions, Phái sinh ngoại bảng) và các khoản mục loại trừ (công cụ phi nhạy cảm lãi suất, các tài sản bị trừ khỏi Vốn cấp 1 CET1 như bất động sản, tài sản vô hình, cổ phần phi kinh doanh).
- **Đo lường Giá trị kinh tế (EV / EVE) (u03)**: Phân tích kỹ thuật tính EV thông qua chiết khấu dòng tiền tương lai với lãi suất phi rủi ro, phân tích khe hở tái định giá (Repricing Gap Analysis) qua 5 bước, và mô hình Duration Gap. Điểm mấu chốt: rủi ro lãi suất chỉ tính đến ngày thiết lập lại lãi suất tiếp theo (*next reset date*), không phải ngày đáo hạn hợp đồng, vì sau ngày reset công cụ sẽ giao dịch lại theo giá ngang mệnh giá (*par*).
- **Đo lường Thu nhập (Earnings / NII) (u03)**: Phân biệt rạch ròi giữa góc nhìn hồi cứu quá khứ của phòng Kế toán (*retrospective view*) và góc nhìn hướng về tương lai của phòng ALM (*prospective view*). Mô hình dự báo NII trong chân trời 1–3 năm và cơ chế triệt tiêu sai số mô hình khi tính toán độ nhạy NII ($\Delta\text{NII}$).
- **Mô phỏng NII kịch bản sốc & Phòng hộ Receiver Swap (u04)**: Tác động lệch pha thời điểm tái định giá (tiền gửi 3 tháng vs cho vay 1 năm) khiến NII biến động mạnh qua các năm khi lãi suất giảm. Chiến lược dùng Receiver Swap (nhận cố định, trả thả nổi) giúp ổn định thu nhập NII.
- **Xung đột mục tiêu EVE vs NII (u04)**: Hoán đổi Receiver Swap bảo vệ NII nhưng lại kéo dài thời lượng tài sản, đẩy khe hở định giá lại tăng vọt từ 1,74 lên 3,63, làm khuếch đại rủi ro EVE khi lãi suất đảo chiều tăng. EVE và NII thường có xu hướng phản ứng ngược chiều nhau.
- **FTP Structural Contribution (u04)**: Đóng góp cấu trúc trong hệ thống định giá chuyển nhượng vốn nội bộ là khoản bù đắp rủi ro cho Treasury khi gánh vác rủi ro thanh khoản và rủi ro lãi suất từ sự bất cân xứng kỳ hạn tài sản - nợ.
- **Quyền chọn nhúng, Sản phẩm phi kỳ hạn & Mô hình danh mục tái lập (u05)**: Phân biệt quyền chọn tự động (thực hiện theo quy tắc duy lý) vs quyền chọn hành vi (chịu chi phối bởi nhân khẩu học: ly hôn, chuyển nhà...). Định nghĩa sản phẩm phi kỳ hạn (Non-maturity products) là các vị thế có kỳ hạn hành vi khác biệt với kỳ hạn hợp đồng. Kỹ thuật xây dựng Mô hình danh mục tái lập (Replicating Portfolio Model) và danh mục cuốn chiếu (Rolling Portfolio) qua các lát cắt kỳ hạn (vintage tranches) kèm trần kỳ hạn bình quân 5 năm theo quy định Basel/EBA.

## Key claims

### Unit u02 — Banking Book vs. Trading Book & Instruments Used in ALM

- Mục đích của ALM trong ngân hàng là tối ưu hóa kết quả lãi/lỗ (P&L) và vốn chủ sở hữu trong khi vẫn duy trì mức độ bao phủ thanh khoản đầy đủ và mức độ phơi nhiễm rủi ro lãi suất phù hợp.
  > "The purpose of ALM in banks is to optimize profit and loss (P&amp;L) and equity capital while maintaining adequate liquidity coverage and an adequate  interest rate risk exposure."
  > — Chapter 1, line 488 ^tata-alm-purpose

- Sổ ngân hàng (Banking Book / nonregulatory trading book) bao gồm toàn bộ các giao dịch và vị thế có tính chất dài hạn liên quan đến hoạt động kinh doanh khách hàng của ngân hàng và việc tài trợ cho chúng, bao gồm cả vốn chủ sở hữu của ngân hàng.
  > "The banking  book ,  sometimes  also  referred  to  as  the  nonregulatory  trading book ,  comprises  all  transactions  and  positions  of  a  long-term  nature  that  are related to the bank's  client business  and  its  financing.  It  includes  the  bank's equity  capital."
  > — Chapter 1, line 520 ^tata-scope-1

- Sổ kinh doanh (Trading Book / regulatory trading book) thường bao gồm các vị thế nắm giữ nhằm mục đích bán lại trong ngắn hạn, hưởng lợi từ biến động giá ngắn hạn, tạo lợi nhuận chênh lệch giá (arbitrage) hoặc phòng ngừa rủi ro.
  > "The trading book , sometimes also referred to as the regulatory trading book ,  typically  includes  positions  taken  for  the  purpose  of  short-term  resale, profiting  from  short-term  price  movements,  generating  arbitrage  profits,  or hedging  risks."
  > — Chapter 1, line 522 ^tata-scope-2

- Trong phân tích rủi ro lãi suất, chỉ có các công cụ nhạy cảm với lãi suất mới được đưa vào tính toán IRRBB; các công cụ không nhạy cảm với lãi suất sẽ không chịu biến động giá khi lãi suất thay đổi.
  > "In  the  context  of  interest  rate  risk,  only  interest  rate-sensitive  instruments are  taken  into  account  in  the  calculation  of  IRRBB."
  > — Chapter 1, line 561 ^tata-scope-3

- Định nghĩa công cụ nhạy cảm lãi suất: Là các tài sản, nợ phải trả và khoản mục ngoại bảng trong sổ phi kinh doanh (sổ ngân hàng) chịu nhạy cảm trước các biến động lãi suất, ngoại trừ các tài sản bị trừ khỏi Vốn tự có Cấp 1 (CET1) như bất động sản, tài sản vô hình hoặc các khoản đầu tư cổ phần trong sổ ngân hàng.
  > "Interest  rate  sensitive  instruments:  Assets,  liabilities  and  off-balance-sheet  items in  the  non-trading  book,  which  are  sensitive  to  interest  rate  changes  (excluding assets deducted  from  CET1  capital  -  e. g., real estate or intangible assets or equity  exposures  in  the  non-trading  book)."
  > — Chapter 1, line 563 ^tata-scope-4

- Các công cụ phái sinh có thể được sử dụng để thực hiện các giao dịch phòng ngừa rủi ro vi mô (micro hedges) đối với từng vị thế bảng cân đối riêng lẻ (như hoán đổi lãi suất cố định sang thả nổi đối với khoản vay 5 năm - asset swap).
  > "Derivatives may be employed for the purpose of implementing micro hedges with  respect  to  an  individual  balance  sheet  position."
  > "Such  a  balance  sheet  position  may  be  found  on  either  the asset  side  or  the  liability  side  of  the  bank's  balance  sheet.  Figure  1.4  provides an  illustration  of  a  customer-driven  asset,  namely  a  five-year  fixed-rate  loan, that  is  micro-hedged  by  a  corresponding  fixed-to-floating  interest  rate  swap. Such  a  swap  transaction  is  referred  to  as  an  asset  swap."
  > — Chapter 1, line 565 ^tata-scope-5

- Thay vì sử dụng hợp đồng hoán đổi lãi suất, các ngân hàng thường có xu hướng bù trừ các bất cân xứng thời lượng tiềm tàng thông qua việc điều phối các vị thế nội bảng.
  > "In  lieu  of  utilizing  swaps,  banks appear to offset  potential  duration  mismatches  through  the  deployment  of on-balance-sheet  positions."
  > — Chapter 1, line 567 ^tata-scope-6

### Unit u03 — 2.1 Economic Value Measures & 2.2 Earnings Measures

- Giá trị kinh tế của một vị thế được xác định bằng tổng hiện giá các dòng tiền tương lai được chiết khấu theo mức lãi suất phù hợp với môi trường hiện hành.
  > "The economic value (EV) of a position is determined by the sum of the present value(s) (PV) of its (multiple) cash flow(s). To do this, the timing and amount of the future cash flows must be known. If not, the expected cash flows must be determined in a model. In addition, a discount rate, r , must be assumed that is consistent with the current interest rate environment."
  > — Chapter 2, line 862 ^tata-ev-1

- Biến động giá trị kinh tế phát sinh từ sự thay đổi lãi suất chiết khấu và phụ thuộc vào độ nhạy cảm lãi suất của tài sản.
  > "By changing the discount rate from r to ( r + /Delta1 r ), one can calculate the change in the previously calculated economic value, /Delta1 EV, resulting from a change in interest rates, /Delta1 r . The change in economic value depends on the interest rate sensitivity of the asset."
  > — Chapter 2, line 868 ^tata-ev-2

- Khi dòng tiền phụ thuộc vào mức lãi suất (do quyền chọn trả nợ trước hạn hoặc lãi suất thả nổi), dự phóng dòng tiền bắt buộc phải được điều chỉnh tương ứng.
  > "If the cash flows depend on the level of interest rates (e. g., because of prepayment options or because the cash flows are based on floating interest rates), the cash flow projections must be adjusted."
  > — Chapter 2, line 870 ^tata-ev-3

- Phân tích khe hở tái định giá dựa trên lịch phân bổ tài sản, nợ và ngoại bảng vào các dải kỳ hạn theo ngày đáo hạn (nếu lãi suất cố định) hoặc thời gian còn lại đến ngày tái định giá tiếp theo (nếu lãi suất thả nổi).
  > "It is based on a maturity / repricing schedule that allocates interest rate sensitive assets, liabilities and off-balance sheet items into a number of pre-defined time bands according to their maturity (if fixed rate) or time remaining until their next repricing (if floating rate)."
  > — Chapter 2, line 882 ^tata-gap-1

- Rủi ro lãi suất chỉ được tính đến ngày tái định giá tiếp theo (next reset date) chứ không phải ngày đáo hạn hợp đồng, vì khi được thiết lập lại theo lãi suất thị trường, công cụ sẽ giao dịch lại theo giá ngang mệnh giá (par).
  > "Note that interest rate risk is only assumed to the next reset date, not to the contractual maturity date. This is because once a fixed-rate instrument is reset to market rates, it will trade at 'par' again."
  > — Chapter 2, line 888 ^tata-gap-2

- Bước 5 của phân tích khe hở tái định giá: nhân mỗi khe hở ròng với mức giảm giá trị kinh tế (%) ước tính khi lãi suất tăng 1%, dựa trên modified duration của tài sản và nợ trong từng dải, rồi cộng dồn thành total repricing gap, tức mức giảm EVE cho mỗi 1% lãi suất tăng song song.
  > "Step 5: Weight  and  aggregate  the  of  net  repricing  gaps.  Each  gap  is  multiplied  by  an  assumed  percentage  decrease  in  economic  value  that  would  result from a 1%  increase in interest rates. Such a sensitivity measure would be based  on  estimates  of  the  modified  duration  of  the  assets  and  liabilities  that fall  within  each  time  band."
  > "It estimates the decline in the economic  value of the bank's equity for a  1% (parallel) increase in  interest  rates."
  > — Chapter 2, line 894 ^tata-gap-3

- Bảng cân đối của ngân hàng mô hình (Table 2.2): tài sản gồm Bonds 50, Loans 300, Mortgages 150; nợ gồm Term deposits 150, Savings accounts 200, Interbank deposits 100, Equity capital 50; tổng 500.
  > "| Bonds | 50 | Term deposits | 150 | … | Loans | 300 | Savings accounts | 200 | … | Mortgages | 150 | Interbank deposits | 100 | … | | | Equity capital | 50 | … | Total assets | 500 | Total liabilities | 500 |"
  > — Chapter 2, line 896–904, Table 2.2 ^tata-gap-4

- Kỳ hạn hợp đồng và chu kỳ tái định giá (tháng) theo Table 2.3: Bonds 60/60, Loans 6/6, Mortgages 60/12, Term deposits 3/3, Savings accounts 36/6, Interbank deposits 24/24. Đây là chu kỳ tái định giá bình quân ước tính.
  > "Table 2.3 illustrates the (estimated average) reset  periods  for  various  banking  book  positions."
  > "| Bonds | 60 | 60 | … | Loans | 6 | 6 | … | Mortgages | 60 | 12 | … | Term deposits | 3 | 3 | … | Savings accounts | 36 | 6 | … | Interbank deposits | 24 | 24 |"
  > — Chapter 2, line 888 & 906–915, Table 2.3 ^tata-gap-5

- Phân bổ theo dải tái định giá (<1, 1-3, 3-6, 6-12, 12-24, 24-36, 36-48, 48-60 tháng) và khe hở ròng (Table 2.4–2.5): ∑ Assets 0/0/300/150/0/0/0/50; ∑ Liabilities 0/150/200/0/100/0/0/0; Net repricing gaps 0/−150/100/150/−100/0/0/50. Equity không được phân bổ vào dải nào.
  > "| ∑ Assets | 0 | 0 | 300 | 150 | 0 | 0 | 0 | 50 |"
  > "| ∑ Liabilities | 0 | 150 | 200 | 0 | 100 | 0 | 0 | 0 |"
  > "| Net repricing gaps | 0 | -150 | 100 | 150 | -100 | 0 | 0 | 50 |"
  > — Chapter 2, line 917–935, Table 2.4–2.5 ^tata-gap-6

- Total repricing gap 1.74 nghĩa là EVE giảm 1.74 khi lãi suất tăng 1% (và ngược lại); với vốn chủ sở hữu 50, mức này tương đương 3.48% vốn cho mỗi 100 bp lãi suất tăng.
  > "A total repricing gap of 1.74 implies that the bank's  economic  value,  or economic  value  of  equity  (EVE),  declines  by  1.74  for  a  1%  increase  in  interest rates  (and  vice  versa)  due  to  the  lag  in  repricing  various  balance  sheet  items. Given  that the bank's equity is 50, this corresponds  to a 3.48%  decline  in equity  for  a  100  bp  increase  in  interest  rates."
  > — Chapter 2, line 937 ^tata-gap-7

- Khe hở thời lượng (duration gap) được tính bằng tổng thời lượng hiệu chỉnh có trọng số vị thế của tài sản trừ đi tổng thời lượng hiệu chỉnh có trọng số của nợ phải trả.
  > "The duration gap would be calculated as the position-weighted sum of the modified duration of the bank's assets minus the position-weighted sum of the bank's liabilities"
  > — Chapter 2, line 971 ^tata-dgap-1

- Với duration gap 0,37, mức tăng lãi suất 1% dẫn đến tổn thất 0,37% trên tổng tài sản 500 (tương đương 1,85), tương ứng mức sụt giảm giá trị kinh tế của vốn chủ sở hữu (EVE) là 3,7% trên 50 vốn.
  > "With a duration gap of 0.37, a 1% increase in interest rates results in a loss of 0.37% on 500, or 1.85. This represents 3.7% of the 50 equity, so the decline in the economic value of equity (EVE) is 3.7%."
  > — Chapter 2, line 975 ^tata-dgap-2

- Thước đo thu nhập xem xét thu nhập tạo ra bởi các khoản mục bảng cân đối và cách thức biến động lãi suất làm thay đổi chúng, trong đó thước đo phổ biến là Thu nhập lãi thuần (NII).
  > "Earnings measures look at the earnings generated by balance sheet items and how a change in interest rates causes them to change. A commonly used earnings measure is Net interest income (NII). NII is the difference between interest income on assets and the interest expense on liabilities during a given period."
  > — Chapter 2, line 983 ^tata-nii-1

- NII chính thức do phòng Kế toán tính cho quá khứ (retrospective view) và bao gồm các thay đổi, biến động trong tháng.
  > "The NII calculation is done for the past (retrospective  view)  and  includes  intra-month  changes  and  movements."
  > — Chapter 2, line 987 ^tata-nii-12

- Trong khi phòng Kế toán nhìn về quá khứ (retrospective), phòng ALM định lượng phơi nhiễm thu nhập lãi thuần trên cơ sở hướng về tương lai (prospective).
  > "While the accounting department has a backward-looking view, the ALM department aims to quantify net interest exposure on a forward-looking basis (prospective view)."
  > — Chapter 2, line 989 ^tata-nii-2

- Khi tính toán độ nhạy NII, độ chính xác của dự báo NII cơ sở ít quan trọng hơn đối với ALM vì các giả định sai sẽ được áp dụng lặp lại trong kịch bản sốc và bị triệt tiêu phần lớn khi trừ hai giá trị cho nhau.
  > "While the NII forecast is a very important metric by which senior bank management assesses the health and competitiveness of the bank, the accuracy of the NII forecast is less important to ALM when dealing with NII sensitivities . This is because any (incorrect) assumption made in the calculation of the NII forecast will be applied repeatedly in the calculation of the NII resulting from a changed interest rate environment. Since the NII sensitivity is calculated as the newly calculated NII minus the original NII forecast, a significant portion of the (incorrect) assumption is cancelled out."
  > — Chapter 2, line 1021 ^tata-nii-3

- Chân trời thời gian cho dự báo NII thường là ngắn đến trung hạn, phổ biến từ một đến ba năm; kéo dài kỳ dự báo quá xa sẽ tạo cảm giác chính xác giả tạo vì không thể dự báo vững chắc thay đổi trong hoạt động kinh doanh khách hàng trong dài hạn.
  > "The time horizon for NII forecasts is typically shortto medium  term, often one to three years."
  > "Extending the forecast period too far into the future  would  create  a  false  sense  of  accuracy,  as  robust  predictions  of  changes in  customer  business  cannot  be  made  over  the  long  term."
  > — Chapter 2, line 1025 ^tata-nii-4

- Khi tính toán độ nhạy NII đối với biến động lãi suất, mọi vị thế không nhạy cảm với lãi suất như bất động sản, đầu tư cổ phần, tài sản vô hình và vốn chủ sở hữu kế toán đều được loại trừ khỏi phân tích.
  > "As the objective is to calculate NII sensitivities to changes in interest rates, all positions that are not interest rate sensitive can be excluded from the analysis. These include positions in real estate, equity investments, intangible assets and the bank's own equity."
  > — Chapter 2, line 1027 ^tata-nii-5

- Earning gap (income gap) đo độ nhạy NII năm đầu với cú sốc song song 1%: periodic earning gap = net repricing gap × 1% × (thời gian còn lại của năm đầu tính từ điểm giữa dải / 12); với ngân hàng mô hình, các periodic earning gap là 0 / −1.25 / 0.625 / 0.375 cho các dải <1, 1-3, 3-6, 6-12 tháng.
  > "They  are  defined  as  the  net  repricing  gap × 1% × fi rst  year  impact  (as  a  percentage  of  a  full  12-month  period)."
  > "| Midpoints | 0.5 | 2 | 4.5 | 9 | | 1st year impact | 11.5 | 10 | 7.5 | 3 | | Periodic earning gap | 0 | -1.25 | 0.625 | 0.375 |"
  > — Chapter 2, line 1085–1095, Table 2.11 ^tata-egap-1

- Total earning gap −0.25 nghĩa là NII năm đầu giảm 0.25 cho mỗi 1% lãi suất tăng song song; nếu lãi suất tăng ngay 400 bp, NII giảm 1.
  > "The  calculated  earning  gap  of -0.25  implies  a  decrease  in  NII  of -0.25  in the  first  year  for  every  1%  parallel  increase  in  interest  rates.  Thus,  if  interest rates  were  to  rise  immediately  by  400  bp,  the  bank  should  expect  a  decline  in NII  of  1."
  > — Chapter 2, line 1097 ^tata-egap-2

### Unit u04 — Total Baseline NII, Shock Scenarios, Hedging & FTP
- NII dự phóng theo giai đoạn của ngân hàng mô hình. Baseline (Table 2.20): 3.750 / 3.639 / 7.002 / 14.124 / 13.956 cho các giai đoạn tháng 1-3, 4-6, 7-12, 13-24, 25-36; tổng 3 năm 42.471. Kịch bản sốc −100 bp (Table 2.27): 3.750 / 4.014 / 7.248 / 13.116 / 13.956; tổng 3 năm 42.084.
  > "| 1-3 | 1.250 | 3 | 3.750 | … | 4-6 | 1.213 | 3 | 3.639 | … | 7-12 | 1.167 | 6 | 7.002 | … | 13-24 | 1.177 | 12 | 14.124 | … | 25-36 | 1.163 | 12 | 13.956 | … | Total 3-year NII | | 36 | 42.471 |"
  > "| 4-6 | 1.338 | 3 | 4.014 | … | 7-12 | 1.208 | 6 | 7.248 | … | 13-24 | 1.093 | 12 | 13.116 | … | Total 3-year NII | | 36 | 42.084 |"
  > — Chapter 2, line 1247–1256 (Table 2.20) & 1374–1383 (Table 2.27) ^tata-nii-13

- Ngân hàng mô hình chịu rủi ro sụt giảm NII đáng kể khi lãi suất giảm 100 bp trong giai đoạn từ năm thứ nhất đến năm thứ hai.
  > "A  visual  inspection  of  Fig.  2.6  suggests  that  the  model  bank  faces  significant  NII  downside  risk  for  a  100  bp  move  lower  in  interest  rates  in  the  period from  one  year  to  two  years  from  now."
  > — Chapter 2, line 1291 ^tata-nii-14

- Mô phỏng dự báo NII 36 tháng cho thấy tác động bất đối xứng về thời điểm tái định giá: khi lãi suất giảm, tiền gửi kỳ hạn hưởng lợi ngay sau 3 tháng giúp tiết kiệm chi phí lãi đáng kể.
  > "What our NII projections suggest makes intuitive sense: Term deposits benefit very quickly from a decline in interest rates because they reset after only three months, resulting in significant interest savings on the cost side."
  > — Chapter 2, line 1323 ^tata-nii-6

- Ngược lại, các khoản cho vay thế chấp không tái định giá trong vòng 1 năm tiếp theo, do đó sự sụt giảm thu nhập lãi xuất hiện muộn hơn.
  > "Mortgages , on the other hand, do not reset for another year, so the decline in interest income comes later ."
  > — Chapter 2, line 1355 ^tata-nii-7

- Các ngân hàng thường nỗ lực triệt tiêu biến động NII nhằm ổn định dòng thu nhập qua thời gian.
  > "Banks typically try to avoid NII volatility in order to stabilize earnings over time."
  > — Chapter 2, line 1357 ^tata-nii-8

- Một biện pháp để tận dụng hoặc phòng hộ trước sự suy giảm lãi suất là ký kết hợp đồng hoán đổi lãi suất nhận cố định - trả thả nổi (receiver swap) trên một quy mô danh nghĩa xác định.
  > "One way to take advantage of a decline in interest rates is to enter into a fixed-for-floating interest rate swap, where one receives a fixed rate and pays a floating rate , both on a given notional amount."
  > — Chapter 2, line 1387 ^tata-nii-9

- Điều khoản receiver swap minh hoạ: kỳ hạn 3 năm, notional EUR 100, chân cố định trả 4.16%, chân thả nổi ban đầu 3.95% và tái định giá mỗi sáu tháng.
  > "As an illustration, assume that the bank enters into a 3-year  EUR  100 (notional) receiver  swap 18 where  the fixed leg of  the  swap  pays  4.16%  and the  floating  leg  is  linked  to  floating  interest  rate  that  is  initially  set  at  3.95% and  reprices  every  six  months  thereafter."
  > — Chapter 2, line 1389 ^tata-nii-15

- Với hedge, NII kịch bản sốc −100 bp theo giai đoạn là 3.804 / 4.065 / 7.854 / 14.328 / 15.168, tổng 3 năm 45.219 (Table 2.33); hedge giúp ổn định NII, đặc biệt giảm mức sụt NII ở giai đoạn 13-24 tháng.
  > "| 1-3 | 1.268 | 3 | 3.804 | … | 4-6 | 1.355 | 3 | 4.065 | … | 7-12 | 1.309 | 6 | 7.854 | … | 13-24 | 1.194 | 12 | 14.328 | … | 25-36 | 1.264 | 12 | 15.168 | … | Total 3-year NII | | 36 | 45.219 |"
  > "The  hedge  helped  to  stabilize the NII  in the event of a -100  bp  interest rate  shock.  In  particular,  the  NII  downside  in  the  13-24-month  period  was reduced."
  > — Chapter 2, line 1488–1497 (Table 2.33) & 1505 ^tata-nii-16

- Caveat thứ nhất: kết quả hedge "có vẻ quá tốt để là thật" vì NII đã hedge còn cao hơn cả baseline; nguyên nhân là giả định giữ nguyên lãi suất ngắn hạn hiện tại. Nếu lãi suất tăng theo forward rates thì lợi ích ngắn hạn của việc nhận cố định cao, trả thả nổi thấp sẽ mất dần.
  > "First,  the  picture  painted  by  Fig.  2.7  seems too  good  to  be  true :  the  expected NII  for  the  hedged  balance  sheet  is  not  only  better  than  that  in  the  unhedged shock scenario, but also better than that in the baseline scenario."
  > "We  have  chosen  to hold  the  current  interest  rate  constant , i. e. there is no expected  increase  in short-term  interest rates."
  > "If we assume  that interest rates will rise in line with what  forward  rates imply, the  short-term  benefit of receiving a higher fixed rate and paying a currently lower floating rate would  disappear  over  time"
  > — Chapter 2, line 1511–1513 ^tata-nii-17

- Việc bổ sung hợp đồng hoán đổi receiver swap vào phân tích rủi ro giá trị kinh tế làm gia tăng khe hở định giá lại (repricing gap) từ 1,74 lên 3,63.
  > "Adding the receiver swap to the economic value risk analysis increases the repricing gap to 3.63 (see Table 2.35)."
  > — Chapter 2, line 1517 ^tata-nii-10

- Cả thước đo giá trị kinh tế (EVE) và thước đo thu nhập (NII) đều là các thước đo phù hợp để lượng hóa rủi ro lãi suất; biến động lãi suất tác động đến cả EVE và NII, tuy nhiên hai thước đo này thường phản ứng ngược chiều nhau trước cùng một biến động lãi suất.
  > "Both, economic value measures and earnings measures are appropriate measures for quantifying interest rate risk. Changes in interest rates affect both, EVE and NII. However, EVE and NII often react in opposite ways to changes in interest rates."
  > — Chapter 2, line 1521 ^tata-nii-11

- Đóng góp cấu trúc (structural contribution) trong FTP là phần thù lao trả cho bộ phận Treasury khi đảm nhận hai rủi ro khác nhau: rủi ro thanh khoản và rủi ro lãi suất.
  > "The structural contribution is the compensation to the treasury department for taking on two different risks, liquidity risk and interest rate risk."
  > — Chapter 2, line 1631 ^tata-ftp-1

- Do đó, các vị thế tài sản và nợ phải trả lệch pha kỳ hạn cũng đồng thời tạo ra rủi ro lãi suất.
  > "Therefore, the mismatched asset and liability positions also create interest rate risk ."
  > — Chapter 2, line 1633 ^tata-ftp-2

### Unit u05 — Embedded & Behavioral Options, Replicating Model & Rolling Portfolio

- ALM cần xem xét cả hai loại quyền chọn lãi suất: quyền chọn tự động và quyền chọn hành vi; quyền chọn tự động thực thi theo quy tắc (như caps, floors, swaptions), trong khi quyền chọn nhúng/hành vi trao cho khách hàng quyền tự đưa ra quyết định cá nhân về dòng tiền.
  > "ALM  needs to consider both, 'automatic' and 'behavioral' interest rate options.  Automatic  options  execute  rule-based,  such  as  interest  rate  caps  and floors  and  swaptions. Embedded  options ,  also  known  as behavioral or nested options,  give  the  customer  the  right  to  make  individual  decisions  about  cash flows."
  > — Chapter 2, line 1821 ^tata-opt-1

- Quyền chọn hành vi có thể tồn tại đối với cả các sản phẩm có kỳ hạn hợp đồng cụ thể (như các khoản cho vay thả nổi, cho vay mua nhà thế chấp cá nhân).
  > "Behavioral  options  may  also  exist  for  products  that  have  a  stated  contractual  maturity  (e.  g.,  floating-rate  loans,  consumer  mortgages)."
  > — Chapter 2, line 1825 ^tata-opt-2

- Bởi vì quyền chọn hành vi có khả năng làm giảm kỳ hạn kỳ vọng so với kỳ hạn hợp đồng, chúng tạo ra tác động trọng yếu lên giá trị kinh tế của vốn chủ sở hữu (EVE) và các thước đo thu nhập (NII).
  > "Because  behavioral  options potentially reduce the expected  (contractual) maturity, they have a significant impact on economic  value of equity and earnings  measures  (EVE  and  NII)."
  > — Chapter 2, line 1827 ^tata-opt-3

- Lý thuyết định giá quyền chọn chuẩn giả định quyền chọn tự động được thực hiện duy lý; ngược lại, quyền chọn hành vi có thể không được thực hiện tối ưu, một phần do các yếu tố nhân khẩu học (như tử vong, ly hôn hoặc thay đổi công việc).
  > "Standard option pricing theory assumes that rule-based , or automatic , options  are  exercised  in  a  rational  manner.  For  example,  the  holder  of  a  standard  financial  option  would  never  execute  an  out-of-the-money  call  option because,  in  doing  so,  the  price  paid  for  the  underlying  instrument  would  be higher than the prevailing market price. Behavioral options, on the other hand, may not be executed optimally, partially, in part because of  demographic factors (such as death, divorce, or job change)."
  > — Chapter 2, line 1843 ^tata-opt-4

- Sản phẩm phi kỳ hạn (non-maturity products) được định nghĩa là các vị thế có kỳ hạn hành vi (behavioral maturity) khác biệt với kỳ hạn hợp đồng (contractual maturity) hoặc không có kỳ hạn hợp đồng được công bố.
  > "In  Sect.  2.4,we  defined  non-maturity  products  as  positions  where  the behavioral maturity differs from the contractual maturity or where there is no stated  contractual  maturity."
  > — Chapter 2, line 1851 ^tata-nmd-1

- Tỷ lệ rút vốn tự nhiên (run-off) đo lường mức độ suy giảm của tiền gửi trong các tài khoản hiện hữu theo thời gian.
  > "The run-off  measures  the  decay  of  deposits  in  existing  accounts  over  time."
  > — Chapter 2, line 1851 ^tata-nmd-2

- Mô hình danh mục tái lập (replicating model) nhằm mục đích tái lập các sản phẩm phi kỳ hạn bằng một danh mục bao gồm chủ yếu các công cụ tài chính thanh khoản và có thể giao dịch, trong đó diễn biến khối lượng và lãi suất của danh mục tái lập là sự xấp xỉ thực tế hành vi kỳ vọng của sản phẩm phi kỳ hạn.
  > "A replicating model aims to replicate non-maturity products by means of a portfolio consisting mainly of liquid and tradable financial instruments, where  the  volume  and  interest  rate  development  of  the  replicating  portfolio is a realistic approximation of the expected behavior of the non-maturity product."
  > — Chapter 2, line 1847 ^tata-nmd-3

## Node bị ảnh hưởng
- [[economic-value-of-equity]]
- [[net-interest-income-sensitivity]]
- [[duration-gap-model]]
- [[gap-risk]]
- [[ftp-nature-and-balance-sheet-management]]
- [[irrbb-transmission-mechanisms-to-nii-and-eve]]
- [[irrbb-balance-sheet-portfolios]]
- [[repricing-balance-sheet]]
- [[behavioural-options]]
- [[non-maturity-deposits]]
- [[replicating-portfolio-model]]

## Mâu thuẫn ghi nhận
Không có.

## Ghi chú convert
Docling convert: heading chương bị gộp, chia unit theo dải 400 dòng; một số công thức toán chuyển thành `<!-- formula-not-decoded -->`.

