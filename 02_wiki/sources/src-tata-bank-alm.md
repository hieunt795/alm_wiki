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
units_done: [u02, u03, u04, u05, u06, u07, u08]
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
  - `u06`: 3.1–3.5 Bank ALM in Practice: bank-specific ALM, NII planning, behavioral economics, lãi suất âm (lines 2177–2468; dòng 2069–2176 là Notes/References của ch2, không lấy claim)
  - `u07`: 3.6 Rapid Rise in Interest Rates, 4 Case Study SVB, 5.1 Lịch sử quy định IRRBB (lines 2469–2874)
  - `u04–u05` (bổ sung 2026-10-22): 2.3 Funds Transfer Pricing, dòng 1581–1783 (2.3.1–2.3.3, 2.3.5–2.3.11; 2.3.4 đã có ^tata-ftp-1, ^tata-ftp-2) — block ^tata-ftp-3..32
  - `u08`: 5.2–5.5 IRRBB Measures (EBA SA/S-SA, SOT EVE/NII, báo cáo EU 2024/855), 6 Future of ALM (lines 2875–3346)

## Tóm tắt
Cuốn sách cung cấp phương pháp luận chi tiết và các mô hình số học mô phỏng cho quản trị ALM hiện đại:
- **Phân định Banking Book vs Trading Book & Phạm vi IRRBB (u02)**: Phân tách ranh giới giữa Sổ ngân hàng (hoạt động kinh doanh khách hàng và tài trợ dài hạn) và Sổ kinh doanh (tự doanh, giao dịch ngắn hạn). Xác định các nhóm công cụ thuộc phạm vi IRRBB (Customer business, External positions, Phái sinh ngoại bảng) và các khoản mục loại trừ (công cụ phi nhạy cảm lãi suất, các tài sản bị trừ khỏi Vốn cấp 1 CET1 như bất động sản, tài sản vô hình, cổ phần phi kinh doanh).
- **Đo lường Giá trị kinh tế (EV / EVE) (u03)**: Phân tích kỹ thuật tính EV thông qua chiết khấu dòng tiền tương lai với lãi suất phi rủi ro, phân tích khe hở tái định giá (Repricing Gap Analysis) qua 5 bước, và mô hình Duration Gap. Điểm mấu chốt: rủi ro lãi suất chỉ tính đến ngày thiết lập lại lãi suất tiếp theo (*next reset date*), không phải ngày đáo hạn hợp đồng, vì sau ngày reset công cụ sẽ giao dịch lại theo giá ngang mệnh giá (*par*).
- **Đo lường Thu nhập (Earnings / NII) (u03)**: Phân biệt rạch ròi giữa góc nhìn hồi cứu quá khứ của phòng Kế toán (*retrospective view*) và góc nhìn hướng về tương lai của phòng ALM (*prospective view*). Mô hình dự báo NII trong chân trời 1–3 năm và cơ chế triệt tiêu sai số mô hình khi tính toán độ nhạy NII ($\Delta\text{NII}$).
- **Mô phỏng NII kịch bản sốc & Phòng hộ Receiver Swap (u04)**: Tác động lệch pha thời điểm tái định giá (tiền gửi 3 tháng vs cho vay 1 năm) khiến NII biến động mạnh qua các năm khi lãi suất giảm. Chiến lược dùng Receiver Swap (nhận cố định, trả thả nổi) giúp ổn định thu nhập NII.
- **Xung đột mục tiêu EVE vs NII (u04)**: Hoán đổi Receiver Swap bảo vệ NII nhưng lại kéo dài thời lượng tài sản, đẩy khe hở định giá lại tăng vọt từ 1,74 lên 3,63, làm khuếch đại rủi ro EVE khi lãi suất đảo chiều tăng. EVE và NII thường có xu hướng phản ứng ngược chiều nhau.
- **FTP mục 2.3 (u04–u05 bổ sung)**: định nghĩa FTP và chi phí cơ hội, transfer price curve, tách FTP thành pure interest rate risk curve cộng funding spread, ví dụ 1,6% + 80 bp = 2,4%, chức năng steering, chi phí LCR/NSFR, contingency liquidity, điều chỉnh optionality (mark-up/discount), ranh giới credit và operational risk, so sánh với FVA.
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

### Unit u06 — 3.1–3.5 Bank ALM in Practice (NII planning, hành vi, lãi suất âm)

- Không có ALM 'một cỡ cho tất cả'. Ở Đức (MFI, cuối 1999 → cuối 2021), lãi suất giảm dài hạn làm tiền gửi không kỳ hạn của khách hàng tăng từ 7,9% lên 29,3%, hơn một nửa do khách hàng rời tiền gửi có kỳ hạn (17,3% → 9,3%) và tiết kiệm (10,8% → 5,8%); phần lớn dòng tiền gửi qua đêm được gửi tại NHTW làm dự trữ dư thừa, đưa tiền mặt trên bảng cân đối từ 1% lên 11,4%.
  > "There is no one-size-fits-all -ALM. The heterogeneity of European banks requires  a  tailored  approach  to  the  use  of  risk  management  techniques."
  > "The composition of assets and liabilities on current balance sheets has changed significantly since the turn of the century. Figure 3.1 illustrates this development  for monetary  financial institutions 1 (MFIs) in  Germany between  EoY  1999  and  EoY  2021. 2"
  > "The  secular  decline  in  interest  rates  between  1999  and  2021  has  led  to  a significant  increase  in  customer  sight  deposits  (from  7.9%  to  29.3%).  More than  half  of  this  21.4%  increase  was  driven  by  customers  moving  out  of term  deposits  (from  17.3%  to  9.3%)  and  savings  accounts  (from  10.8% to 5.8%), as term deposits and savings accounts did not offer sufficient compensation  over  and  above  that  of  sight  deposits."
  > "-A large part of the inflow  of  overnight  retail  deposits  was  parked  with the  central  bank  as  excess  reserves,  leading  to  an  increase  in  the  overall cash  position  of  banks'  balance  sheets  from  1%  to  11.4%."
  > — §3.1.1, line 2179 ^tata-prac-1

- Chỉ trong hai năm (cuối 2021 → cuối 2023), lãi suất tăng khiến dự trữ dư thừa về lại 1%, tiền gửi không kỳ hạn giảm từ 29,3% xuống 26,1%, tiền gửi có kỳ hạn dưới 1 năm tăng từ 2,6% lên 5,9%; nguồn rút ra bài học phải mô hình hoá khối lượng (nhất là bán lẻ) bằng giả định ALM thực tế.
  > "In just two years, the rise in interest rates caused banks to reduce their excess reserves at the central bank, bringing their liquidity back to 1% (roughly the level prior to the low interest rate environment). Customer sight  deposits  declined  from  29.3%  to  26.1%,  while  customer  time  deposits increased.  The  largest  increase  was  in  customer  time  deposits  under  one  year, which  rose  from  2.6%  to  5.9%."
  > "The pronounces whipsaw in the balance sheet structure of banks in response  to changes  in interest rates illustrates  the  importance  of  modeling volumes  (especially  retail  volumes)  with  realistic  ALM  assumptions."
  > — §3.1.1, line 2209 ^tata-prac-2

- Vai trò ALM phụ thuộc mô hình kinh doanh: ngân hàng có mạng lưới huy động bán lẻ lớn không kiểm soát hết lượng tiền gửi nhận vào (không thể từ chối tiền gửi), còn ngân hàng dựa vào liên ngân hàng có nhiều lựa chọn nguồn vốn hơn; tiền gửi không kỳ hạn lớn của ngân hàng tiết kiệm gây vấn đề khi lãi suất âm.
  > "For  example,  banks  with  a  high  degree  of  retail  deposit-generating  infrastructure (i. e., networks of branches and offices) cannot fully control the amount  of retail deposits they receive through that infrastructure; turning down  deposits  is  simply  not  an  option.  Other  banks  that  are  less  dependent on  retail  deposits  and  more  reliant  on  the  interbank  market  and  other  forms of  funding  have  more  discretion  over  their  funding  sources."
  > "ALM  must  adapt  to the specific needs of a bank's business model. For example,  the  strong  sight  deposit  business  of  savings  banks  creates  potential problems  in  the  event  of  negative  interest  rates."
  > — §3.1.3, line 2231 ^tata-prac-3

- FTP cho phép ALM thành profit center: rủi ro tài chính được chuyển về profit center rủi ro lãi suất trong ALM, ALM quyết định có phòng ngừa qua giao dịch thị trường không, lợi nhuận được phân phối lại định kỳ cho các đơn vị kinh doanh. Nếu là cost center, ALM gom chi phí quản trị rủi ro lãi suất mà không nhằm kiếm lợi nhuận từ định vị thị trường, chi phí được chuyển vào chi phí chung của đơn vị kinh doanh.
  > "Funds  Transfer  Pricing  (FTP)  allows  the  ALM  department  to  become  a profit center ."
  > "When  ALM  is  organized  as  a  profit  center,  financial risks are  transferred to the interest rate risk profit center (within ALM). ALM  then decides whether  and  how  to  hedge  the  assumed  risk  through  open  market  transactions.  The  profit  generated  within  ALM  is  then  periodically  redistributed  to the  customer  business  units."
  > "Alternatively,  ALM  can  be  run  as  a cost  center .  In  this  case,  ALM  aggregates the  costs  of  all  necessary  interest  rate  risk  management  activities  without  the objective  of  generating  a  profit  through  market  positioning  and  timing.  These costs  must  be  passed  on  to  the  customer  business  units'  overhead."
  > — §3.1.4, line 2250 ^tata-prac-4

- ALM phải thiết kế riêng theo ngân hàng và thay đổi theo thời gian; mức độ phức tạp của công cụ tuỳ quy mô và trình độ, đôi khi giữ đơn giản với trực giác tốt hơn tạo cảm giác chính xác giả bằng mô hình quá phức tạp.
  > "There  is no one-size-fits-all ALM.  ALM  must  be  tailored  to  the  specific  needs of the bank.  The requirements for  ALM change over time,  as  the market environment,  behavioral  aspects  of  the  customer  base,  best  practices  in  theory and  modeling,  access  to  and  liquidity  in  the  financial  markets,  and  regulatory requirements  change.  Examples  of  questions  to  ask  when  designing  a  tailored ALM  include"
  > "The extent and rigor with which ALM  tools and concepts should be applied in a bank-specific situation also depends  on  the size and sophistication of  the  institution;  sometimes  it  is  better  to  keep  them  simple,  but  have good  intuition about  the process, than to create a false sense of accuracy by using  overly  complicated  models."
  > — §3.1.5, line 2268 ^tata-prac-5

- NII được dự phóng chứ không chỉ tính lùi để báo cáo; lập kế hoạch NII có chiều chính trị: đơn vị kinh doanh ngại lập kế hoạch NII giảm (vì giảm phân bổ nguồn lực) và cũng ngại kế hoạch tăng quá cao; vì vậy cần khách quan, kiểm định giả định, dựa trên dữ liệu.
  > "Because  NII  is  an  important,  if  not the most  important,  measure  of  a  bank's success from an earnings perspective, NII is not only calculated  backward for reporting purposes, but also projected into the future.  The process of planning  NII  goes  beyond  setting  reasonable  expectations  for  future  NII;  the whole  exercise  has  a  significant political dimension.  Business  units  are  typically  reluctant  to  plan  for  a  decline  in  NII,  even  if  this  is  objectively  the  most likely  scenario,  because  of  the  strategic  implications,  such  as  reduced  allocation  of  resources  (including  personnel),  diminished  decision-making  power within  the  organization,  and,  in  the  extreme,  the  discontinuation  of  the  entire business  unit.  At the same  time,  there  is some  reluctance  to  plan  for  a very large increase in NII  because  it would  set the bar very high,  increasing the likelihood  of  disappointment  and  decreasing  the  likelihood  of  exceeding  the plan  (which  could  be  the  basis  for  promotions  and  bonuses)."
  > "These  behavioral  biases in the psychology of  planning make  it  even  more important  to  strive  for  as  much  objectivity  as  possible,  to  test  any  assumptions made,  and  to  keep  the  process  as  data-driven  as  possible."
  > — §3.2, line 2283 ^tata-niip-1

- Ba tầm hoạch định NII: forecast năm hiện tại (kết quả đã biết cộng dự báo các tháng còn lại, thường làm 3–4 lần/năm), budget năm kế tiếp, và plan cho các năm sau đến 3–5 năm; budget và plan là dự báo thuần, phụ thuộc mạnh vào giả định khối lượng, biên lãi, lãi suất.
  > "When  projecting  NII  into  the  future,  various  planning  horizons  are  typically used.  While  bank-specific  terminology  may  vary,  a  common  notation  is  to forecast NII  in  the current calendar  or  fiscal  year, budget for  the next calendar or fiscal  year,  and plan for  calendar  or  fiscal  years thereafter for  a  horizon  of up  to  3-5  years."
  > "The  forecast  is  a  combination  of  known  results  (from  past  months)  and  a prediction  for  future  months.  The  quality  of  the  current  year's  forecast  typically  improves  as  the  calendar  or  fiscal  year  progresses.  A  forecast  is  often  done three  to  four  times  a  year,  sometimes  more."
  > "The  budget  and  plan,  on  the  other  hand,  are  pure  predictions  of  the  future. Assumptions about  future  key  factors (volumes,  margins,  interest  rates, etc.) have  a  significant  impact  on  the  results  and  quality  of  these  predictions."
  > — §3.2.1, line 2289 ^tata-niip-2

- Quy trình lập kế hoạch NII hằng năm tối thiểu gồm khối lượng và biên lãi kỳ vọng của từng mảng kinh doanh cùng môi trường lãi suất kỳ vọng; phải mô hình hoá nhiều môi trường lãi suất, mỗi môi trường có khối lượng và biên lãi nhất quán; kịch bản cơ sở thường là lãi suất spot hiện tại hoặc lãi suất forward; kịch bản thay thế cho thấy phân phối tiềm năng của NII.
  > "The  (annual)  NII  planning  process  of  a  bank  includes,  as  a  minimum,  the planning  of volumes and expected  margins for each  business  line , as well as the expected  future interest  rate  environment ."
  > "Volumes  and margins depend on the interest rate environment.  Therefore, several alternative interest rate environments  must  be modeled  and  a consistent  view  of  volumes  and  margins  must  be  established  for  each."
  > "One  of  the scenarios can be referred to as the baseline  scenario , which  is the  most  widely  expected  interest  rate  environment.  This  is  often  the  current interest rate environment  (i. e., current spot rates) or the one reflected in current forward rates."
  > "Alternative  scenarios  provide  an  idea  of  the  potential  distribution  of  NII (under  uncertainty).  See  Fig.  3.4."
  > — §3.2.2, line 2297 ^tata-niip-3

- Khối lượng của từng mảng lập kế hoạch riêng vì run-off khác nhau (có hay không quyền trả trước); run-off là hàm của môi trường lãi suất và hành vi khách hàng giả định, rồi cộng nghiệp vụ mới (cũng phụ thuộc lãi suất).
  > "The  volume  of  each  business  line  needs  to  be  planned  separately  because  the run-offs  are  different  (e.  g.,  some  business  lines  give  customers  prepayment options,  while  others  don't)."
  > "The run-off needs  to  be  estimated  and  is  a  function  of  the  assumed  interest rate  environment  and  the  assumed  behavior  of  the  bank's  customers.  Then, new business must be planned (which is also a function of the assumed interest rate environment).  As discussed in Sect. 2.5.5 on  volume  changes in  the  context  of  the  replicating  model,  different  assumptions  can  be  made about  new  business.  See  also  Fig.  2.31."
  > — §3.2.3, line 2313 ^tata-niip-4

- Biên lãi của từng mảng lập kế hoạch riêng, có ước tính nén biên (margin compression). Bằng chứng thực nghiệm: Busch và cộng sự (2021, ngân hàng Đức) ước tính NIM giảm 5 bp cho mỗi năm thêm sau cú dịch chuyển xuống 100 bp; Cruz-García và cộng sự (2019, 32 nước, 2008–2014) ước tính biên lãi biến động khoảng 19 bp cho mỗi 100 bp lãi suất ngắn hạn; nếu giả định 'margin-beta' thì biên kế hoạch phải điều chỉnh theo kịch bản lãi suất. Thực tế quản lý thường giả định biên giữ nguyên.
  > "The net interest margin of each business needs to be planned separately because  margins  evolve  differently  (e.  g.,  due  to  the  competitive  environment in  different  business  areas).  Estimating  a  potential margin  compression , which could  be  affected by the assumed  interest  rate  environment  itself,  is part of the  planning  process."
  > "Some  empirical evidence suggests that net interest margins are to  some extent directional with respect to the general level of interest rates. For example,  using  data  from  a  quantitative  survey  of  German  banks,  Busch  et  al. (2021)  estimate  that  net  interest  margins  decline  by  5  bp  for  every  additional year  following  a  100  bp  downward  shift  in  the  interest  rate  level. 9 In  another study  looking  at a  broad  panel  of  banks  from  32  countries  over  the  period 2008  to  2014,  Cruz-García  et  al.  (2019)  estimate  that  interest  margins  move by  about  19  bp  for  every  100  bp  shift  in  short-term  market  interest  rates.  If"
  > "we  have  to  assume  a  'margin-beta,'  then  planned  margins  would  need  to  be adjusted  for  different  interest  rate  environments  in  the  future."
  > "Margin  planning  also  tends  to  be  a  highly  political  issue  within  the  bank's panning  process.  Managers  tend  to  shy  away  from  planning  for  a  reduction  in margin.  Often  enough,  the  current  margin  is  assumed  to  remain  unchanged."
  > — §3.2.4, line 2321 ^tata-niip-5

- Kế hoạch ALM toàn diện phải dự phóng rủi ro lãi suất tương lai, tức tính độ nhạy EVE và NII kỳ vọng, đòi hỏi kế hoạch chi tiết hơn kế hoạch khối lượng: chia khối lượng theo phân khúc hành vi lãi suất và chỉ rõ kỳ hạn của nghiệp vụ mới (ví dụ cố định 5 năm hay 20 năm); cũng phải dự phóng LCR, NSFR và yêu cầu vốn, đáp ứng mọi yêu cầu quy định cùng hạn mức, mục tiêu nội bộ.
  > "ALM  planning  involves  forecasting  the  bank's  future  interest  rate  risk.  T o do this, expected EVE  and NII sensitivities should be calculated for the future.  This requires ALM  to  have  a detailed plan of the different business units  that  goes  beyond  a  pure  volume  plan:"
  > "Different  customer  interest  rate  behaviors  should  be  taken  into  account  by dividing  the  planned  volume  into  segments  with  different  assumed  interest rate  behaviors."
  > "Expected  maturities  for new  business need to be specified. For  example, it  makes  a  big  difference  whether  a  business  unit  plans  fixed-rate  business with  a  maturity  of  5  years  or  20  years."
  > "Forecasts  of  future  liquidity  risk  (e. g.,  liquidity  coverage  ratio,  net  stable funding ratio) and capital requirements should also be considered as they can have a significant impact on the ALM  plan. A comprehensive  ALM plan should help meet all regulatory and supervisory requirements as well as  internal  limits  and  targets."
  > — §3.2.5, line 2339 ^tata-niip-6

- Trước đây chỉ một số ngân hàng có giả định hành vi tường minh, nhưng EBA đặt thành yêu cầu cho mọi ngân hàng: khi đánh giá quyền chọn nhúng phải xét tác động lên tốc độ trả trước hiện tại và tương lai từ kịch bản lãi suất, môi trường kinh tế và đặc điểm hợp đồng, và độ co giãn điều chỉnh lãi suất sản phẩm theo lãi suất thị trường.
  > "In  the  past,  only  some  banks  made  explicit  assumptions  about  the  behavioral aspects of their customers, but in the future this will be a regulatory requirement  set  by  the  EBA,  for  all  banks:"
  > "In assessing the implications of optionality, institutions should take into account:"
  > "(a)  The  potential  impact  on  current  and  future  loan  prepayment  speeds  arising from  the  interest  rate  scenario,  underlying  economic  environment  and  contractual features. Institutions should take into account the various dimensions influencing  the  embedded  behavioural  options."
  > "(b)  The  elasticity  of  adjustment  of  product  rates  to  changes  in  market  interest rates. 12"
  > — §3.3.1, line 2358 ^tata-beh-1

- Cần mô hình hoá hành vi cho: NMD (kỳ hạn hành vi), hạn mức như thấu chi (giải ngân và tốc độ trả), khoản vay có quyền trả trước, tiền gửi có kỳ hạn có thể rút sớm. Giả định phải dựa trên dữ liệu lịch sử phù hợp và giả thuyết thận trọng; backtest khó vì môi trường thay đổi, và dữ liệu thời kỳ lãi suất âm không dùng để backtest cho thời kỳ lãi suất dương và ngược lại.
  > "Behavioral  modeling  is  particularly  important  for  balance  sheet  items  with embedded  options.  Examples  of  customer  transactions  that  require  behavioral modeling  include"
  > "Non-maturity  deposits  (NMDs)  with  respect  to  behavioral  maturity"
  > "Lending  facilities,  such  as  overdrafts,  in  terms  of  drawdown  and  repayment speed"
  > "Loans  with  prepayment  options  (such  as  certain  mortgage  loans)"
  > "Certain term deposits with respect to early withdrawal (even if the customer  is  subject  to  a  penalty  for  breaking  the  contract)"
  > "The  modeling  of  key  behavioral  assumptions  must  be  based  on  appropriate underlying  historical  data  and  on  prudent  hypotheses.  However, backtesting 13 is often difficult due to the ever-changing market environment,  change  in customer  sophistication  and  the  development  of  new  banking  products.  In addition,  negative  interest  rates  can  lead  to  atypical  behavior;  therefore,  data from  the  negative  interest  rate  environment  cannot  be  used  for  backtesting in  a  positive  interest  rate  environment  and  vice  versa."
  > — §3.3.1, line 2368 ^tata-beh-2

- Ngân hàng thường là price-taker với lãi suất sản phẩm nên phải mô hình hoá cả hành vi của ngân hàng khác. Ví dụ: ngân hàng lâu đời dùng replicating portfolio có thể chỉ truyền một phần thay đổi lãi suất thị trường vào NMD vì phần lớn tiền gửi đã được phòng ngừa ở lãi suất lịch sử; ngân hàng online mới, ít tiền gửi cũ, có thể truyền gần hết.
  > "Since  banks  are  typically  not  monopolists  in  any  of  the  banking  services  they offer,  their  pricing  power  with  respect  to  so-called  product  rates  is  limited.  At the  extreme,  a  bank  could  be  a  mere  price-taker,  meaning  that  whatever  the market  equilibrium  rate  for  a  particular  banking  product  (say,  sight  deposits) is, it is also be the rate the bank has to offer to its  own  customer  base. 14 Thus,  it is  not  enough  to  model  the  behavior  of  bank  customers  based  on their investment  opportunities  and  preferences, but also to  understand  the behavior  of all other banks  behavior  based  on  idiosyncratic  factors,  such  as their  funding  strategy."
  > "In  another  case,  the  competitive  relationship  is  less  obvious.  A  bank  with branches  in  small  towns,  large  cities,  and  a  strong  online  franchise  competes with  a  large  number  of  banks.  Here,  behavioral  assumptions  must  be  made about many  different banks. This is particularly difficult because different banks  have  different  business  models  and  their  FTP  rates  from  their  respective ALM  frameworks  are  likely  to  be  different.  For  example,  an  established  bank using  a  replicating  portfolio  model  approach  may  pass  on  only  a  fraction  of a market rate change to its non-maturity  deposit customer  base because a large  portion  of  the  deposits  have  been  originated  in  the  past  and  are  already hedged  at  historical  rates.  Alternatively,  a  start-up  online  bank  with  few  legacy deposits  can  afford  to  pass  on  most  of  the  interest  rate  change  (because  it  can also  lock  in  this  higher  funding  rate  with  investments  at  current  rates)."
  > — §3.3.2, line 2379 ^tata-beh-3

- Deposit beta đo mức truyền dẫn lãi suất phi rủi ro (thường là lãi suất chính sách) vào lãi suất tiền gửi, bằng tỷ lệ thay đổi lãi suất thị trường được truyền vào lãi suất tiền gửi; deposit beta rất không ổn định nên suy ra hành vi ngân hàng từ lãi suất sản phẩm quan sát được không hiệu quả, có thể phải mô hình hoá tường minh.
  > "On  an  aggregate  basis,  the  extent  to  with  which  changes  in  interest  rates  are reflected  in  the  rates  of  non-maturity  products  is  estimated  through  deposit beta  modeling.  Deposit  betas  are  a  measure  of  the  pass-through  of  risk-free rates,  typically  the  monetary  policy  rate,  to  the  deposit  market,  measured  as the  portion  of  a  change  in  the  risk-free  market  rate  that  is  passed  through  to the  deposit  rate.  As  discussed  in  Sect.  2.5.8  in  the  context  of  the  replicating model  and  illustrated  in Fig. 2.37, deposit  betas are  highly  unstable.  Thus, extracting implied patterns of banks behavior from empirical observations of product rates does not work very well. In fact, it may be necessary to model  bank  behavior  explicitly,  even  if  it  is  cumbersome  and  based  on  many assumptions."
  > — §3.3.2, line 2385 ^tata-beh-4

- Ngày 5/6/2014 ECB hạ lãi suất deposit facility xuống −0,10%, mở ra khoảng tám năm ZIRP/NIRP; trước đó giả định mô hình phần lớn dựa trên lãi suất chặn dưới ở 0 (ví dụ phân phối log-normal).
  > "On  June 5, 2014, the Governing Council of the ECB  lowered the rate on the deposit facility (DF) to -0.10%.  The eight years that followed are often referred to as the period of zero interest rate policy  (ZIRP)  or  negative  interest  rate  policy  (NIRP).  Historically,  a  basic  truism  of  finance  would reject  the  idea  of  negative  interest  rates,  similar  to  that  of  negative  probabilities or  negative  commodity  prices.  Previously,  modeling  assumptions  were mostly  based  on  zero-bound  interest  rates  (e.  g.,  assuming  that  interest  rates are  log-normally  distributed  with  a  zero  probability  of  negative  interest  rates)."
  > — §3.5, line 2419 ^tata-neg-1

- Lãi suất âm gần như không là vấn đề trong giao dịch định chế (IRS liên ngân hàng, repo); lãi suất chỉ số âm không nhất thiết sinh dòng tiền âm vì dòng tiền thường là chỉ số cộng spread. Với tiền gửi bán lẻ, áp lãi suất âm có thể bị luật bảo vệ người tiêu dùng cấm hoặc không thực tế, nên lãi suất thực trả là max(rI ± x; 0%). Sàn 0% gần như không giá trị khi lãi suất cao nhưng at/in the money khi lãi suất thấp hoặc âm; khả năng khách hàng chống lại lãi suất âm là ví dụ quyền chọn nhúng hay quyền chọn hành vi.
  > "The use of negative interest rates in institutional transactions, such as interbank interest rate swaps or repo transactions, is hardly a problem. 19 Conceptually, nominal interest  rates  are  the real interest  rate  plus  an  adjustment  for  inflation.  If  inflation  is  negative,  negative  nominal  interest  rates  do not  necessarily  imply  a  lack  of  compensation.  Banks  would  normally  be  able to pass on their costs of holding excess liquidity 20 at the central bank to corporate  customers  by  charging  negative  interest  rates  on  corporate  deposits. Also,  negative indicator rates  (market-based  interest  rates,  such  as  EURIBOR, used  to  calculate  the  customer  rate)  do  not  necessarily  result  in  negative  cash flows, as cash flows are often based on an indicator rate plus a spread . For example, in the case of floating rate corporate loans, even if the indicator rate  on  which  the  loan  is  based  becomes  negative,  the  credit  spread,  and  the margin  applied  to  the  indicator  rate  could  easily  make  the  customer  rate  used for  cash  flow  calculations  positive."
  > "The situation is different in retail banking. Charging retail depositors negative  interest  rates  may  be  prohibited  by  consumer  protection  laws  or  may be  impractical  from  a  customer  relationship  perspective.  If  a  bank  expects  to pay  retail  depositors  an  interest  rate  of  rI ± x ,  based  on  a  floating  rate  indicator rate rI and a spread x , the actual deposit rate is not rI ± x , but  the greater  of rI ± x and  zero  percent,  or  max  (  rI ± x ;  0%).  This  fl oor at  zero percent was hardly relevant when  interest rates were high; the situation is different  in  a  negative  interest  rate  environment."
  > "To  draw  an  analogy  from  the  area  of  automatic  interest  rate  options,  where execution  is  rule-based,  such  as  interest  rate  caps  and  floors,  a  0%  floor  is out of  the  money , i. e., has little value, when  interest  rates  are  high,  but  is at the money , or even in the  money , when  interest rates are low or negative.  The ability of consumers  to  resist being  charged  negative  interest rates on retail deposits is an example of embedded  options or behavioral options. Their value  also  increases  in  a  low  interest  rate  environment."
  > — §3.5.1, line 2423 ^tata-neg-2

- Hai loại sàn: coupon floor, lãi suất khách hàng là max(rI + x; 0%) (ví dụ tài khoản tiết kiệm bán lẻ); indicator floor, lãi suất là max(rI; 0%) + x, biên x được bảo vệ (ví dụ khoản vay doanh nghiệp). Coupon floor bất lợi cho nợ phải trả, có lợi cho tài sản; ngân hàng có indicator floor ở tài sản và coupon floor ở nợ thì lãi suất âm có lợi, trường hợp ngược lại gây lỗ tiềm năng.
  > "There  are  two  types  of  floors,  depending  on  the  features  of  the  contract  and how  consumer  protection  laws  are  implemented:  The coupon  floor and the indicator  floor . In the  case of a coupon  floor ,  the  customer's  interest  rate  cannot fall below 0%.  However,  the indicator rate used to calculate the  customer interest rate can be negative as long as the spread applied above the indicator  rate  ensures  that  the  resulting  customer  rate  is  not  negative.  Thus,  the customer  rate  is  max  (  rI + x ;  0%).  While  the  customer  will  never  be  charged a negative interest rate charge, the customer  may  not receive the expected margin x . An  example  of  a coupon  floor  is a retail  savings  account  (where consumer  protection  laws in some  countries prevent retail  customers  from paying  interest  on  such  account  types).  In  the  case  of  an indicator  floor , the indicator rate used to calculate the customer  rate cannot be less than  0%. In  this  case,  the  customer  rate  is  calculated  as  max  (  rI; 0%) + x .  Here,  the margin x is  protected  even  if  the  indicator  rates  fall  below  0%.  An  example  of an  indicator  floor  is  a  corporate  loan  with  a  corresponding  contract  feature."
  > "Whether  a  0%  floor  is  good  or  bad  from  a  bank's  perspective  depends  on whether  the  floor  is  applied  to  an  asset  or  a  liability.  Coupon  floors  are  bad for  liabilities  (e.  g.,  customer  deposits)  because  they  limits  the  bank's  ability to  'charge'  negative  interest  rates  on  funding  transactions.  Coupon  floors  are good  for assets (e. g., customer  loans)  because  they prevent the  bank  from having  to  pay  negative  interest  rates  on  investments."
  > "If  a  bank  faces  indicator  floors  on  assets  and  coupon  floors  on  liabilities,  a negative  interest  rate  environment  is  beneficial  (all  else  being  equal);  if  a  bank faces coupon  floors on assets and indicator floors on liabilities, a negative interest  rate  environment  causes  potential  losses. 21"
  > — §3.5.1, line 2429 ^tata-neg-3

- Khi lãi suất âm, tiền gửi không kỳ hạn không chịu lãi âm thành tài sản hấp dẫn và ngân hàng nhận dòng tiền gửi lớn, gọi là rigid deposits (lãi suất không co giãn khi lãi suất thị trường xuống dưới 0); NIRP làm giảm biên trung gian vì lợi suất tài sản giảm trong khi phần lớn chi phí vốn không đổi; một số ngân hàng chuyển sang tài sản lợi suất cao hơn, tăng biên cho vay, hoặc tìm thu nhập phí.
  > "In a negative interest rate environment, non-negatively remunerated sight deposits become  an attractive asset class for bank customers compared  to other low-risk alternatives such as short-term fixed income investments. 22 Not  surprisingly, banks experienced  a significant inflow into sight deposits during  the  ZIRP  /  NIRP  period  (see  Fig.  2.32).  These  deposits  became  what can  be  called rigid  deposits , 23 defined  as  deposits  whose  interest  rate  becomes inelastic  when  market  interest  rates  fall  below  zero."
  > "From  an  economic  perspective,  ZIRP  /  NIRP  creates  frictions  in banks' funding  mix, as banks' retail deposits do not reprice when  policy rates are cut  below  zero.  According  to  Demiralp  et  al.  (2021),  '[r]ate  cuts  resulting  in negative  policy  rates  are  unlikely  to  operate  in  the  same  fashion  as  conventional  rate  cuts  because  banks  may  not  be  able  to  charge  their  retail  customers negative rates on their deposits. Banks' inability to adjust a part of their funding costs may be due to the forces of competition -in  combination with the high regulatory value of retail deposits due to their stability -as well as the existence of  banknotes,  which  offer  an  alternative  store of value with  a  yield  of  zero.  Therefore,  NIRP  should  have  an  impact  on  banks'  profitability as the remuneration  of banks' assets declines as a consequence  of NIRP  while a significant part of their funding costs remains unchanged, leading  to  declining  intermediation  margins.'"
  > "The negative interest rate environment encouraged some of the most deposit-dependent banks to shift the composition of their balance sheets toward higher-yielding assets in order to protect or restore profitability, 24 others that  were  highly  NII-dependent  to  compensate  for  lost  deposit  margins by  increasing  lending  margins,  and still  others to  seek  more  fee  and  commission  income. 25"
  > — §3.5.2, line 2443 ^tata-neg-4

- Cơ quan quản lý kỳ vọng ngân hàng xét kịch bản lãi suất âm và tác động lên hành vi khách hàng bán lẻ; theo EBA, trong môi trường lãi suất thấp phải xét kịch bản lãi suất âm, tác động bất đối xứng, và ràng buộc tái định giá tiền gửi bán lẻ cùng ảnh hưởng của nó tới độ ổn định tiền gửi.
  > "Regulators  expect  banks  to  consider  negative  interest  rate  scenarios  and  their impact  on  retail  customer  behavior.  According  to  the  EBA:"
  > "In low interest rate environments, institutions should also consider negative interest rate scenarios and the possibility of asymmetrical effects of negative interest rates on their interest  rate  sensitive  instruments.  (…)  In  making behavioural  assumptions  about  accounts  without  specific  repricing  dates  (…), institutions  should  (…)  consider  potential  constraints  on  the  repricing  of  retail deposits  in  low  or  negative  interest  rate  environments  and  the  effect  that  such constraints may  have  on  the stability of deposits under  different interest rate scenarios. 26"
  > — §3.5.3, line 2451 ^tata-neg-5

- Thách thức còn lại với lãi suất âm: dữ liệu ngắn gây khó hiệu chỉnh mô hình; chưa có mô hình chuẩn; chuyển từ EURIBOR sang RFR làm đổi chỉ số và spread của hợp đồng, ảnh hưởng tới sàn; hành vi người tiêu dùng chưa hiểu hết; ngân hàng có thể không thực thi sàn vì lý do danh tiếng; tập trung vào sàn 0% không được làm xao nhãng rủi ro lãi suất tăng đột ngột. Sàn 0% gây vấn đề khác nhau cho từng ngân hàng; quản trị mô hình và rủi ro mô hình vẫn là trách nhiệm then chốt của ban điều hành.
  > "Data  availability  is  still  limited  due  to  the  relatively  short  period  of  negative interest  rates.  This  can  lead  to  calibration  issues  for  ALM  models."
  > "Models are still adapting to the inclusion of negative rates, and no benchmark  model  has  yet  taken  hold."
  > "In  the  transition  from  EURIBOR  to  risk-free  rates  (RFRs),  indicators  and customer  spreads  on  existing  contracts  will  change.  This  could  impact  the resulting  floors."
  > "Changes  in  consumer  behavior  are  not  fully  understood."
  > "Reputational issues are also potentially important. Banks must balance legal  positions  with  maintaining  good  customer  relationships. Social  responsibility may  ultimately trump  the pursuit of a legal position. Behavioral aspects (of the bank)  need  to be considered  and  interest rate floors  may not  be  'executed'  by  banks  for  strategic  /  reputational  reasons."
  > "The  focus  on  the  0%  floor  should  not  distract  from  the  analysis  of  the  risks associated  with  a  sudden  rise  in  interest  rates  (see  Sect.  3.6)."
  > "In  summary,  the  0%  interest  rate  floor  on  retail  deposits  caused  different problems  for  different banks  and,  as a result,  banks reacted differently . This illustrates  how  bank-specific  an  ALM  framework  must  be  to  deal  with  shocks such as negative interest rates.  The governance of models and model risk remains  a  key  responsibility  of  banks  management."
  > — §3.5.4, line 2459 ^tata-neg-6

### Unit u07 — 3.6 Rapid Rise in Interest Rates, 4 Case Study SVB, 5.1 Lịch sử quy định IRRBB

- Giai đoạn lãi suất thấp làm mô hình NMD chủ quan: trong chu kỳ 2016–2019 tiền gửi không được bảo hiểm có vẻ 'dính' dù deposit beta thấp, ngân hàng có thể giả định beta thấp kéo dài sang chu kỳ sau; điều này rủi ro vì tiền gửi không được bảo hiểm có thể rời đi và beta tăng nhanh.
  > "The  extended  period  of  relatively  stable  and  declining  interest  rates  through 2022 has been ingrained in the thinking of an entire generation of risk managers,  leading  them  to  believe  that  interest  rate  risk  would  remain  muted."
  > "The  zero-lower  bound  period  was  likely  also  a  factor.  During  the  2016-2019 interest  rate  cycle,  which  was  relatively  shallow,  these  uninsured  checking  and savings  deposits  appeared  'sticky'  and  remained  in  banks  despite  historically  low deposit betas.  Banks  may  have  assumed  these  low  betas  would  persist  during the  current  cycle.  This  is  risky  because  uninsured  deposits  can  become  unstuck and  their  betas  can  rise  quickly. 28"
  > — §3.6, line 2471 ^tata-rr-1

- Năm 2022–2023 khách hàng chuyển phần lớn tiền gửi không kỳ hạn sang sản phẩm khác (có kỳ hạn, tiết kiệm) để hưởng lãi cao hơn, làm tăng duration gap của ngân hàng và làm rủi ro lãi suất hiện thực hoá. Năm 2017 phân tích độ nhạy IRRBB của ECB đã cảnh báo ngân hàng dựa nhiều vào mô hình hành vi được hiệu chỉnh trong môi trường lãi suất giảm.
  > "Indeed,  in 2022  and  2023,  bank  customers  shifted  a significant  portion of  their  deposits  from  sticky  sight  deposits  to  other  products  (term  deposits, savings  accounts,  etc.)  in  order  to  earn  higher  interest  rates  (see  Fig.  3.2).  This led  to  an  increase  in  banks'  duration  gaps  and  the  materialization  of  interest rate  risk. 29"
  > "It  is  worth  noting  that  in  2017,  the  ECB  conducted  a  sensitivity  analysis of  the  banking  books  of  the  largest  European  banks,  focusing  on  interest  rate changes. 30 The  stress test was designed  to provide  the ECB  with  sufficient information to understand  the interest rate sensitivity of a bank's  banking book assets and liabilities, as well as net interest income, to hypothetical interest  rate  changes.  The  results  showed  that  '[b]anks  heavily  rely  on  models of  customer  behavior  which  were  calibrated  in  a  declining  interest  rate  environment.' 31 Thanks  to  this  warning,  some  five  years  before  the  interest  rate cycle  turned  in  2022,  banks  should  have  had  ample  time  to  stress  test  and  to recalibrate  their  models  to  reflect  customer  behavior  in  a  rising  interest  rate environment."
  > — §3.6, line 2477 ^tata-rr-2

- Mô hình trả trước chịu ảnh hưởng mạnh khi lãi suất tăng nhanh: khách hàng đã khoá lãi suất cố định thấp giữ khoản vay lâu hơn dự kiến, có thể giữ thanh khoản dư trong tiền gửi nếu lãi tiền gửi cao hơn lãi vay; ngược lại khoản vay thả nổi có thể trả trước nhanh hơn.
  > "Prepayment  models  are  particularly  affected  by  rapid  interest  rate  increases. Customers who have been able to 'lock in' a low interest rate on fixed rate loans in a  low  interest  rate  environment  are  likely  to  hold  them  longer than expected and not repay them  as quickly as they could (given certain prepayment  options).  It  may  be  more  attractive  for  customers  to  hold  excess liquidity  in  bank  deposits,  rather  than  use  the  funds  to  repay  the  loans  if  the deposit account  pays  a higher interest rate than the fixed rate on the loan. On  the  other  hand,  fl oating-rate loans may  experience  a  higher  prepayment speed  if  interest  rates  rise  rapidly,  as  customers  may  want  to  prepay  as  soon as  possible."
  > — §3.6, line 2481 ^tata-rr-3

- Khi lãi suất tăng nhanh, quy mô, độ nhạy lãi suất và duration của danh mục đầu tư, cùng việc dùng phái sinh lãi suất trong chiến lược ALM, cần được đánh giá lại; ngân hàng có thể phải tinh chỉnh chiến lược phòng ngừa và đầu tư.
  > "Finally,  the  size,  interest  rate  sensitivity,  and  duration  of  a  bank's investment portfolio may  need  to  be  adjusted  if  interest  rates  rise  rapidly.  In  Chapter  4, we discuss an example  of how  a rise in interest rates affected the value of a  particular  bank  (Silicon  Valley  Bank).  In  addition  to  the  investment  portfolio,  the  use  of  interest  rate derivatives (as  part  of  the  ALM  risk  management strategy)  needs  to  be  reassessed."
  > "In summary,  a rapid rise in interest rates may  force banks to fine-tune their  hedging  and  investment  strategies,  which  could  be  significantly  different in a higher interest rate environment. If done properly, this could be an opportunity  to  increase  bank  profitability  and  reduce  risk."
  > — §3.6, line 2485 ^tata-rr-4

- SVB đầu tư mạnh vào chứng khoán nợ trong giai đoạn lãi suất thấp; lạm phát 2021–2023 gây lỗ chưa thực hiện lớn; ngày 8/3/2023 SVB báo lỗ 1,8 tỷ USD khi bán 21 tỷ USD chứng khoán, dẫn tới rút tiền hàng loạt (khách hàng tìm cách rút 142 tỷ USD); ngày 10/3/2023 SVB sụp đổ và bị cơ quan quản lý tiếp quản.
  > "Silicon  Valley  Bank  (SVB)  invested  heavily  in  debt  securities  during  a  period of  low  interest  rates.  The  rise  in  inflation  in  2021-2023  resulted  in  significant unrealized  losses,  and  on  March  8,  2023,  SVB  reported  losses  of  USD  1.8  bn on  the  sale  of  USD  21  bn  in  fixed  income  securities.  This  led  to  a  bank  run,  in which  SVB's  customers  attempted  to  withdraw  USD  142  bn  in  deposits.  On March  10,  2023,  SVB  collapsed  and  was  seized  by  its  regulator. 1 On  March 17, 2023, SVB's holding company  (SVBFG)  filed  a  voluntary  petition for court-supervised reorganization under Chapter  11 of the  U.S.  Bankruptcy Code."
  > — Ch.4, line 2557 ^tata-svb-1

- Năm 2022 hai diễn biến tương quan tác động SVB: hoạt động VC giảm mạnh, làm giảm khả năng huy động tiền gửi gắn với VC; lãi suất tăng nhanh làm giảm giá trị tài sản thu nhập cố định.
  > "In  2022,  two  correlated  developments  negatively  impacted  SVB.  First,  VC activity  declined  sharply  as  part  of  a  broader  pullback  in  technology  investment.  This was partly due to higher interest rates and concerns about the economy.  This  affected  the  ability  of  SVB  to  fund  itself  from  deposits  related to  VC  activity.  The second  development  was  the  rapid  rise  in interest rate, which  led  to  a  write-down  of  fixed-income  assets  on  SVB's  balance  sheet."
  > — §4.1, line 2569 ^tata-svb-2

- Dấu hiệu cảnh báo sớm: SVB không có CRO trong 8 tháng (29/4/2022 – 27/12/2022); chỉ 15,3 tỷ USD (khoảng 12,3%) trong danh mục trái phiếu khoảng 124 tỷ USD được phòng ngừa bằng swap trả cố định, nhận thả nổi vào cuối 2021; nửa đầu 2022 khoảng 11 tỷ USD swap bị tất toán để làm đẹp P&L ngắn hạn, cuối 2022 chỉ còn 0,5 tỷ USD phòng ngừa (0,4% danh mục).
  > "With  respect  to  risk  management,  there  were  a  number  of  red  flags  during the  period  leading  up  to  the  collapse.  Ms.  Laura  Izurieta  resigned  from  her position  as  Chief  Risk  Officer  (CRO)  on  April  29,  2022, 4 and  the  bank  was without  a  CRO  for  eight  months  until  Ms.  Kim  Olson  assumed  the  role  of CRO  on  December  27,  2022. 5"
  > "A  second  warning  sign  was  the  low  degree  to  which  SVB's  approximately USD  124  bn  bond  portfolio  was  hedged  against  a  potential  rise  in  interest rates. Although a large portion of these bonds were highly interest rate sensitive  (30-year  mortgage-backed  securities),  only  USD  15.3  bn  of  the  securities  portfolio,  or  about  12.3%,  was  hedged  with  pay-fixed,  receive-floating interest  rate  swaps  at  the  end  of  2021. 6"
  > "A third and even bigger warning  sign was that in 2022  SVB  started to unwind  its interest rate hedges. About USD  11  bn of the USD  15.3 bn in  interest  rate  swap  positions  were  unwound  in  the  first  half  of  2022.  Not because  SVB's  bond  portfolio  was  shrinking  or  because  the  risk  of  an  interest rate increase was decreasing, but 'to juice its P&amp;L  in the short term.' 7 Removing  only  one  side  of  a  hedge  increases  risk.  By  the  end  of  2022,  only USD  0.5  bn  worth  of  interest rate  hedges  remained,  hedging  just  0.4%  of SVB's  bond  portfolio."
  > — §4.2, line 2573 ^tata-svb-3

- Nguồn vốn của SVB là tiền gửi ngắn hạn không ổn định: cuối 2021 tiền gửi không được FDIC bảo hiểm ước 166 tỷ USD, hơn 88% tổng tiền gửi không kỳ hạn của khách hàng, tăng 87% so với 88,6 tỷ USD năm trước; tiền gửi không được bảo hiểm thường do nhà đầu tư tổ chức 'gửi tạm' và dễ bị rút nhanh.
  > "Finally, SVB's unstable funding from fleeting short-term deposits was a red flag all along. Bank deposits are insured by the U.S. Federal Deposit Insurance  Corporation  (FDIC)  up  to  a  limit  of  USD  250,000  per  depositor. These  small  deposits  tend  to  be  very  stable.  Non-FDIC-insured  deposits,  on the other hand, are often made  by  institutional investors who  'park' their liquidity for only  a short  period  of  time  and  are  also  subject  to  rapid  withdrawal  at  any  sign  of  counterparty  credit  risk.  At  the  end  of  2021,  the  SVB estimated  its  uninsured  deposits  at  USD  166  bn. 8 This  not  only  represents  a large  percentage  of  total  non-maturity  customer  deposits  (more  than  88%), but also reflects an 87%  increase from SVB's uninsured deposits of  USD 88.6  bn  a  year  earlier."
  > — §4.2, line 2579 ^tata-svb-4

- Cuối 2022 vốn chủ sở hữu SVB khoảng 5,7% tổng tài sản (12/212 tỷ USD); sổ HTM (MBS dài hạn) được ghi theo giá vốn phân bổ theo GAAP; lỗ chưa thực hiện ẩn trong sổ HTM là 15,2 tỷ USD, tương ứng lãi suất tăng 2,7% và duration 6,25 năm trên sổ HTM 95 tỷ USD, đủ xoá sạch vốn chủ sở hữu nếu không có lợi thế kế toán GAAP; sổ AFS ước thêm khoảng 1,7 tỷ USD lỗ.
  > "A  first  look  at  SVB's  year-end  balance  sheet  for  2022  shows  that  equity  represents  approximately  5.7%  of  total  assets  (USD  12  bn  out  of  USD  212  bn). Large  portions  of  customer  deposits  (i.  e.,  the  bank's  funding)  are  invested  in available-for-sale  (AFS)  and  held-to-maturity  (HTM)  assets.  HTM  consists of  long-term  mortgage-backed  securities  (MBS)  and  other  bonds. 9 See left panel  of  Fig.  4.1."
  > "Under  U.S.  Generally  Accepted  Accounting  Principles  (GAAP),  securities classified as HTM  are  purchased  with  the  intent and ability to be held to maturity.  Classification  as  HTM  allows  these  securities  to  be  carried  at  amortized historical cost rather  than  at  their  volatile  mark-to-market  value.  AFS financial  investments  are  not  held  to  maturity  and  have  a  readily  observable market  price.  Gains  and  losses  resulting  from  the  fair  value  measurement  of AFS  investments  are  recognized  in  other  comprehensive  income  (OCI)."
  > "A  more  detailed  analysis  shows  that  there  is  already  an  unrealized  GAAP loss  of  USD  15.2  bn  GAAP  hidden  in  the  HTM  book. 10 A  2.7%  increase in interest rates would have caused this unrealized loss of USD  15.2 bn, implying a duration of  6.25  years  on  the  USD  95  bn  HTM  book.  Thus, without  the  benefit  of  GAAP  accounting,  the  bank's  equity  would  have  been completely  wiped  out  by  EoY  2022.  See  right  panel  of  Fig.  4.1."
  > "The  AFS  book  can  be  estimated  to  have  contributed  an  additional  loss  of approximately  USD  1.7  bn  on  top  of  the  unrealized  loss  in  the  HTM  book. 11"
  > — §4.3.1, line 2587 ^tata-svb-5

- Góc nhìn NII: năm 2022 SVB có vẻ lành mạnh với NII 4,5 tỷ USD, thu nhập lãi bình quân 2,73%, chi phí lãi bình quân 0,57%, NIM 2,15%.
  > "From  a  net  interest  income  (NII)  perspective,  the  SVB  appeared  healthy  in 2022, reporting an NII of USD  4.5  bn  for the  year  ended  December  31, 2022. 12 The NII resulted from an average interest income of 2.73%  and an average interest expense of 0.57%.  The net interest margin (NIM) is 2.15%. 13 See  Fig.  4.2."
  > — §4.3.2, line 2601 ^tata-svb-6

- Góc nhìn duration: tài sản (nhất là HTM) có duration dài, nguồn vốn có duration ngắn; khoảng 45% tiền gửi là tiền của start-up và VC chỉ gửi tạm. Kể cả giả định duration tiền gửi gửi tạm là 1 năm, duration gap khoảng 3 năm, tương ứng lỗ khoảng 12,5 tỷ USD (hơn 100% vốn chủ sở hữu) với cú sốc tăng 200 bp; để không là outlier theo SOT EVE (lỗ < 15% vốn), duration tiền gửi phải trên 3,7 năm, một giả định rất bất hợp lý. Quý 1/2023 nhà đầu tư tìm cách rút 42 tỷ USD trong một ngày.
  > "Looking at the duration of the balance sheet items, the real problem of the SVB becomes clear. Some of the assets have a long duration, especially the HTM  positions. 14 The bank's funding, on the other hand, is likely to have a short duration. About 45%  of the deposits are early and later stage tech  money  (from  start-ups  and  VCs,  who  typically  only  'park' money  temporarily  until  investment  opportunities  materialize  in  the  market). This  suggests  a  structural  mismatch  between  long-duration  assets  and  shortduration  liabilities.  See  Fig.  4.3."
  > "The  speed  at  which  deposits  can  disappear  was  demonstrated  in  Q1:2023 when  investors  attempted  to  withdraw  USD  42  bn  in  a  single  day  in  what can  be  characterized  as  a  bank  run."
  > "Even  if  we  assume  an  average  duration  of  1  year  for  the  parked  tech  money, the  duration  gap  of  the  bank  would  be  around  3  years!  A  duration  gap  of  3 years implies  a loss  of  USD  12.5  bn,  or  more  than  100%  of  equity,  in  the event  of  a  200  bp  Basel  interest  rate  (upward)  shock. 15"
  > "To  avoid  being  an  outlier  bank  according  to  the  supervisory  outlier  test  on the  economic  value  of  equity  (i.  e.,  EVE  risk  for  2%  shock  &lt;  15%  of  equity), the  duration  of  the  deposits  would  have  to  be  greater  than  3.7  years. 16 This would  be  a  highly  unreasonable  assumption."
  > "15. Calculation:  USD  209  bn × 2% × 3 [years] ≈ USD  12.5  bn."
  > "16. Calculation:  4.1  [years] -{  (  15% × USD  12  bn)  /  (  USD  209  bn × 2%)} ≈ 3.7  [years]. 17. SVB  (2022, 7). 18. Barr  (2023,  63). 19. Barr  (2023, 1)."
  > — §4.3.3, line 2609 ^tata-svb-7

- Duration NMD phải mô hình hoá theo giả định hành vi về quy mô và thời điểm rút tiền, đòi hỏi hiểu rõ khách hàng; tiền gửi SVB tập trung vào doanh nghiệp công nghệ, khoa học sự sống và PE/VC. Lượng tiền gửi tạm phụ thuộc hai yếu tố lãi suất có quan hệ nhân quả khác nhau: mức lãi suất ảnh hưởng phân bổ vốn vào PE/VC, và ảnh hưởng khả năng quỹ VC đầu tư (đầu tư nhiều thì rút tiền gửi).
  > "Since the duration of non-maturity deposits (NMDs)  cannot  be derived from their contractual maturity (discussed in Sect. 2.4), it is necessary to model their duration based on behavioral assumptions about the extent and  timing  of  depositors'  withdrawal  activity.  This  requires  a  sound  understanding  of  the  nature  of  a  bank's  customers."
  > "SVB  specialized  in  serving  a  relatively  undiversified  depositor  base  concentrated  in  technology  startups.  As  SVB's  2022  annual  report  specifically  noted,"
  > "In order to model the amount  of cash that is temporarily 'parked' in non-maturity  deposits  (NMDs)  ,  at  least  two  interrelated  interest-dependent factors must  be considered.  First, the general level of interest rates (as well as  their  expected  direction)  affects  how  much  money  the  investor  community allocates to alternative investments, including private equity (PE) and venture  capital  (VC)  funds.  When  interest  rates  are  very  low,  investors  tend  to 'chase  yield'  by  shifting  from  low-risk  to  higher-risk  investments.  However, as interest rates rise, traditional investment  opportunities  provide  sufficient returns and risk appetite for alternative investments declines. Second, the general level of interest rates also affects the ability of  VC  funds to invest in start-ups. High investment activity means  that PE /  VC  funds have to withdraw  their bank  deposits and vice versa. A rise in interest rates  makes financing startups more expensive, puts pressure on valuations and causes a temporary  decline  in deal flow.  Rational  decision  making  based  on  these two  factors  (among  others)  will  influence  the  behavior  of  PE  /  VC  funds  that banks  will  observe  as  far  as  deposit  withdrawals  are  concerned.  Unfortunately, the  two  factors  discussed  here  don't  even  have  the  same  causal  relationship, so  modeling  them  will  be  anything  but  trivial.  See  Fig.  4.4."
  > — §4.3.4, line 2623 ^tata-svb-8

- Theo Barr (2023), SVB đổi mô hình làm giảm mức rủi ro hiển thị, ban điều hành đổi giả định thay vì đổi bảng cân đối: tháng 4/2022 tăng duration tiền gửi dựa trên nghiên cứu của tư vấn và phân tích nội bộ, làm giảm chênh lệch duration trên mô hình nhưng không giảm rủi ro thực; giả định không có cơ sở do tiền gửi tăng nhanh, thiếu dữ liệu lịch sử, lãi suất tăng nhanh rút ngắn duration và khách hàng đặc thù.
  > "Unfortunately,  the  SVB  did  not  model  the  behavior  of  its  depositors  to  best reflect  reality,  but  to  engage  in  regulatory  arbitrage.  Barr  (2023)  summarizes this  as  follows:"
  > "[SVB]  made  model  changes  that  reduced  the  level  of  risk  depicted  by  the  model (…)  [and]  management  changed  assumptions  rather  than  the  balance  sheet  to alter  reported  risks.  In  April  2022,  [SVB]  made  a  poorly  supported  change  in assumption  to increase the duration of its deposits based on a deposit study conducted  by  a  consultant  and  in-house  analysis.  Under  the  internal  models  in use,  the  change  reduced  the  mismatch  of  durations  between  assets  and  liabilities and  gave the  appearance  of  reduced  [interest rate risk]; however,  no  risk had been taken off  the  balance  sheet.  The  assumptions  were  unsubstantiated given  recent  deposit  growth,  lack  of  historical  data,  rapid  increases  in  rates  that shorten  deposit  duration,  and  the  uniqueness  of  [SVB's]  client  base. 18"
  > — §4.3.4, line 2633 ^tata-svb-9

- Bài học: kế toán có thể cho phép tách lỗ chưa thực hiện khỏi thu nhập ròng, nên ALM thận trọng càng quan trọng; quản trị rủi ro lãi suất là bắt buộc; tập trung khách hàng tiền gửi cần được giám sát hơn, giả định duration của NMD tương quan cao từ một nhóm nhỏ người gửi phải bị chất vấn; giám sát viên đã thấy thiếu sót IRRBB trong đợt CAMELS 2020–2022 nhưng không ra kết luận giám sát; chênh lệch kỳ hạn lớn không phòng ngừa là nguy cơ lớn.
  > "Silicon Valley Bank (SVB) failed because of a textbook case  of  mismanagement by the bank. Its senior leadership failed to manage  basic interest rate and  liquidity  risk.  Its  board  of  directors  failed  to  oversee  senior  leadership  and hold  them  accountable.  And  Federal  Reserve  supervisors  failed  to  take  forceful enough  action,  as  detailed  in  the  report. 19"
  > "In certain situations, accounting allows for classifying away unrealized security losses from net income. This makes prudent ALM  even more important."
  > "A  proper  governance  of  interest  rate  risk  management  is  imperative.  Flying blind for some  eight months  by  not  having  a Chief  Risk Office did not reflect well on SVB's board of directors and management.  In this case, supervisors  failed  to  catch  the  lack  of  governance. 20"
  > "The  heavy  concentration  in  SVB's  customer  base  (mostly  VC-backed  technology  and  life  sciences  companies)  should  have  received  more  supervisory"
  > "attention. Modeling assumptions of the duration of highly correlated non-maturity deposits (NMDs)  from a small group of similar depositors  should  have  been  questioned  and  challenged.  Supervisors  'identified interest rate  risk  deficiencies  in  the  2020,  2021,  and  2022  Capital,  Asset Quality,  Management,  Earnings,  Liquidity,  and  Sensitivity  to  Market  Risk (CAMELS)  exams  but  did  not  issue  supervisory  findings.' 21"
  > "Despite claims to the contrary, 22 large (and unhedged) maturity mismatches  on  banks'  balance  sheets  pose  a  great  potential  danger."
  > — §4.4, line 2645 ^tata-svb-10

- Từ tháng 10/2024 ngân hàng ở EU phải báo cáo kết quả kiểm tra mới về rủi ro dịch chuyển lãi suất lên thu nhập từ tiền gửi và cho vay trong sổ ngân hàng. RTS của EBA định nghĩa hai SOT: SOT EVE chỉ là cập nhật nhỏ so với hướng dẫn 2018, SOT NII hoàn toàn mới.
  > "Since  October  2024,  banks  in  the  European  Union  are  required  to  report  to their  supervisors  the  results  of  a  new  test  that  measures  the  risk  of  interest  rate shifts on their income from  deposits  and  lending  activities  in  their  banking book."
  > "The EBA RTSs define two supervisory outlier tests (SOTs), one for economic  value  of  equity  (EVE)  and  one  for  net  interest  income  (NII).  While the former is just a minor  update  from the 2018  guidelines, 3 the latter is completely  new.  In  addition,  the  RTSs  detail  the  new  standardized  approach (SA)  as  well  as  the  new  simplified  standardized  approach  (S-SA)  for  both  EVE and  NII."
  > — Ch.5, line 2700 ^tata-reg-1

- Quy định IRRBB có bốn tầng: BCBS (siêu quốc gia); Nghị viện và Hội đồng châu Âu (quy định, chỉ thị); EBA (tiêu chuẩn kỹ thuật, hướng dẫn); cơ quan quốc gia (chuyển hoá chỉ thị vào luật quốc gia).
  > "Interest rate risk arising from the banking book (IRRBB)  is regulated by a number of organizations and authorities. Four layers are of particular importance:  First,  there  is  the  overarching  layer  of  supranational  cooperation among  global  supervisors  through  the Basel  Committee  on  Banking  Supervision (BCBS).  Second,  at  the  European  level,  regulations  and  directives  are  adopted by  the  European  Parliament  and  the  Council.  Third  the European  Banking Authority (EBA),  as  a  regulatory  agency  of  the  European  Union,  is  mandated to  harmonize  European  banking  regulation  through  binding  technical  standards and  guidelines. Finally, national authorities play a role in  transposing EU  directives  into  national  law."
  > — §5.1, line 2712 ^tata-reg-2

- Lịch sử BCBS: Basel I (1988) tập trung rủi ro tín dụng, không xử lý đầy đủ rủi ro lãi suất; 1993 đề xuất tham vấn đo rủi ro lãi suất; 1997 Nguyên tắc quản lý rủi ro lãi suất (cả góc thu nhập và giá trị kinh tế); 2004 bản cập nhật và Basel II; 2016 chuẩn IRRBB; Basel III (2010) dự kiến 2015, hoãn tới 1/2022 rồi 1/2023 do COVID.
  > "The first BCBS requirements for  banks were captured in what is known as Basel I (titled  'International  Convergence  of  Capital  Measurements  and Capital  Standards,'  also  known  as  the 1988  Basel  Accord ). 7 However,  Basel  I focuses  is  on  credit  risk  and  doesn't  adequately  address  interest  rate  risk."
  > "The history of supranational oversight of bank's interest rate risk can be traced back to 1993, when the BCBS issued a consultative proposal for measuring banks' exposure to interest rate risk 8 and, four years later, published  the  first  version  of  its Principles  for  the  Management  of  Interest  Rate Risk . 9 These principles provide a framework  for assessing banks'  exposure to  interest  rate  risk  that  incorporates  both  the  earnings  and  economic  value perspectives."
  > "In July 2004, the BCBS  issued an updated version of the Principles for the  Management  and  Supervision  of  Interest  Rate  Risk. 10 In  the  same  year,  the BCBS  issued  the second Basel Accord, known  as Basel II (entitled 'International Convergence of Capital Measurement and Capital Standards: A Revised Framework'). 11 In parallel, the interest rate risk framework was"
  > "further developed, leading to the  BCBS  publication  on interest rate risk in the  banking  book in  2016. 12"
  > "In 2010, the BCBS  issued the third Basel Accord, known  as Basel III (formally  entitled  'Basel  III:  A  global  regulatory  framework  for  more  resilient banks  and  banking  systems'). 13 Basel  III  was  expected  to  be  implemented  by 2015,  but  was  delayed  first  to  January  2022  and  then  again  to  January  2023 due  to  the  COVID  pandemic."
  > — §5.1.1, line 2720 ^tata-reg-3

- Với rủi ro thị trường, BCBS cho chọn phương pháp kỳ hạn (thang 13 dải, hoặc 15 dải với công cụ coupon thấp; cố định theo kỳ hạn còn lại, thả nổi theo ngày tái định giá; trọng số theo độ nhạy giá, bù trừ dài/ngắn trong từng dải) hoặc phương pháp duration (tính độ nhạy giá từng vị thế). CRR II yêu cầu mô hình nội bộ có yếu tố rủi ro lãi suất cho từng đồng tiền, đường cong tối thiểu sáu phân đoạn kỳ hạn với đồng tiền chính.
  > "During  the  delay  in  the  implementation  of  Basel  III,  the  BCBS  issued  a series of proposals for market risk capital requirements for banks, starting with  a fundamental  review  of  the  trading  book (FRTB)  in  2012, 14 followed  by the  consultative  document Fundamental  review  of  the  trading  book:  a  revised market risk framework in 2013, 15 which was incorporated into the standards for minimum  capital requirements for market risk in 2016, 16 and led to the minimum  capital  requirements  for market  risk in 2019. 17 The  BCBS proposes  a  choice  between  two  methods  for  measuring  the  risk  of  loss  arising from  changes  in  market  interest  rates:  the maturity  method and  the duration method ."
  > "Under the maturity method , long or short positions in debt securities and other sources of interest rate risk, including derivative instruments, are placed  on  a maturity  ladder  consisting  of  13  time  bands  (or  15  time bands in the case of low coupon instruments). Fixed-rate instruments are allocated according to the remaining time to maturity and variablerate instruments according to the remaining time to the next repricing date.  Opposite  positions  of  the  same  amount  on  the  same  issues  (but  not on different issues of the same issuer), whether actual or notional,  may be excluded from the interest rate maturity framework, as may closely matched  swaps,  forwards,  futures  and  forward  rate agreements.  The  first step in the calculation  is to weight  the  positions in each time  band  by  a factor  designed  to  reflect  the  price  sensitivity  of  those  positions  to  assumed changes  in  interest  rates.  The  weights  for  each  time  band  are  provided  by the  BCBS.  The  next  step  in  the  calculation  is  to  offset  the  weighted  longs and  shorts  in  each  time  band,  resulting  in  a  single  short  or  long  position for  each  band."
  > "Under  the alternative duration method , banks with the capability to do so  use  a  more  accurate  method  of  measuring  their  overall  market  risk  by calculating  the  price  sensitivity  of  each  position  separately."
  > "An amendment  to  CRR  I  was  adopted  in 2019  and is now  referred to as  CRR  II.  CRR  II  (2019),  in  force since 2021,  explicitly captures  interest rate risk. For example, in Article 325bh (entitled 'Requirements on risk measurement'),  one  of  the  requirements  listed  is:"
  > "[T]he  internal risk-measurement  model  shall  incorporate  a  set of risk factors that  correspond  to  the  interest  rates  in  each  currency  in  which  the  institution has  interest  rate  sensitive  on- or  off-balance-sheet  positions;  the  institution  shall model  the  yield  curves  using  one  of  the  generally  accepted  approaches;  the  yield curve  shall  be  divided  into  various  maturity  segments  to  capture  the  variations of  volatility  of  rates  along  the  yield  curve;  for  material  exposures  to  interest-rate risk  in  the  major  currencies  and  markets,  the  yield  curve  shall  be  modeled  using a  minimum  of  six  maturity  segments,  and  the  number  of  risk  factors  used  to model  the  yield  curve  shall  be  proportionate  to  the  nature  and  complexity  of the  institution's  trading  strategies,  the  model  shall  also  capture  the  risk  spread of less than perfectly correlated  movements  between  different  yield  curves  or different  financial  instruments  on  the  same  underlying  issuer. 24"
  > — §5.1.1, §5.1.2.2, line 2734 ^tata-reg-4

- Chỉ thị 2006/48/EC Điều 124(5) đặt nền cho SOT: biện pháp giám sát khi giá trị kinh tế giảm quá 20% vốn tự có do thay đổi lãi suất đột ngột. CRD IV Điều 98(5): quá 20% vốn tự có với cú sốc 200 bp hoặc theo hướng dẫn EBA. CRD V sửa: EVE giảm quá 15% vốn cấp 1 theo một trong sáu kịch bản sốc giám sát, hoặc NII suy giảm lớn theo một trong hai kịch bản sốc; như vậy góc giá trị kinh tế được bổ sung góc thu nhập.
  > "In  2006,  Directive  2006/48/EC  and  Directive  2006/49/EC  repealed  CRD I (2000)  and  are  now  commonly  referred  to  as  CDR  I.  An  important  milestone  in  the  regulation  of  interest  rate  risk  is  Directive  2006/48/EC.  Article 124(5)  laid  the  groundwork  for  what  later  became  the supervisory  outlier  test or  standard  interest  rate  shock.  Sudden  and  unexpected  changes  in  interest rates  should  not  result  in  a  decline  of  more  than  20%  of  economic  capital:"
  > "The  review and evaluation performed  by  competent  authorities  shall include the exposure of credit institutions to the interest rate risk arising  from  nontrading  activities.  Measures  shall  be  required  in  the  case  of  institutions  whose economic  value declines by more than 20 %  of their own  funds as a result of a sudden and unexpected change in interest rates the size of which shall be  prescribed  by  the  competent  authorities  and  shall  not  differ  between  credit institutions. 18"
  > "The  review and evaluation performed  by  competent  authorities  shall include the exposure  of institutions to the interest rate risk arising  from  non-trading activities. Measures  shall  be  required  at least in the case  of  institutions  whose economic  value  declines  by  more  than  20  %  of  their  own  funds  as  a  result  of a  sudden  and  unexpected  change  in  interest  rates  of  200  basis  points  or  such change  as  defined  in  the  EBA  guidelines. 21"
  > "This 200 basis point stress test is what we have already referred to in Sect.  1.2.1. as the supervisory  outlier  test , or as the Basel  interest  rate  shock ."
  > "The  supervisory  powers  shall  be  exercised  at  least  in  the  following  cases: (a)  where  an  institution's  economic  value  of  equity  (…)  declines  by  more  than 15 %  of its Tier 1 capital as a result of a  sudden  and  unexpected  change  in interest  rates  as  set  out  in  any  of  the  six  supervisory  shock  scenarios  applied  to interest  rates;"
  > "(b) where  an  institution's net interest  income  (…)  experiences  a  large  decline as a result of a sudden  and  unexpected  change  in  interest rates as set out in any  of  the  two  supervisory  shock  scenarios  applied  to  interest  rates. 23"
  > "This  was  an  important  development  in  the  measurement  of  interest  rate risk  under  the  CRD,  as  the  economic  value  perspective  (loss  of  15%  of  Tier 1  capital)  was  complemented  by  the  earnings  perspective  (decline  in  NII)  as part  of  the  IRRBB  analysis."
  > — §5.1.2.1, line 2753 ^tata-reg-5

- CEBS (2006) ưu tiên đo rủi ro theo giá trị kinh tế, thu nhập là thước đo bổ sung; đề xuất cú sốc chuẩn tương đương phân vị 1 và 99 của biến động lãi suất (5 năm dữ liệu một ngày, quy đổi 240 ngày), xấp xỉ sốc song song 200 bp với đồng tiền chính. EBA (2015, GL/2015/08) nhấn mạnh giả định hành vi (quyền chọn nhúng, tài khoản không có ngày tái định giá, kỳ đầu tư vốn chủ sở hữu) và yêu cầu dùng tối thiểu một thước đo theo thu nhập và một theo giá trị kinh tế.
  > "However,  measurement  of  the  impact  on  economic  value  (the  present  value  of the  bank's  expected  net  cash  flows)  provides  a  more  comprehensive  view  of  the potential  longterm  effects  on  an  institution's  overall  exposures.  Therefore,  the supervisory  focus  will primarily  be on measuring  interest  rate risk in relation to economic value. However, and subject to proportionality considerations, institutions  are  also  expected  to  consider  interest  rate  risk  in  relation  to  earnings as  a  supplementary  measure. 31"
  > "A  standard  shock  could,  for  example,  be  set  so  that  it  will  be  broadly  equivalent to the 1st and 99th percentile of observed interest rate changes (five years of observed one day movements  scaled up to a 240 day year), This would currently  equate  approximately  to  a  parallel  200  basis  points  shock  for  major currencies as  suggested  by  the  Basel  Committee  (…). 32"
  > "In  2015,  EBA  (2015)  issued  the  guideline  GL/2015/08  on  the  management  of  interest  rate  risk  arising  from  non-trading  activities  (IRRBB).  EBA (2015)  acknowledges  the  importance  of  assumptions  when  assessing  interest rate risk for products or positions where the assumed  behavioral repricing date  differs  significantly  from  the  contractual  repricing  date,  or  where  there is  no  stated  contractual  repricing  date  (non-maturity  products).  EBA  (2015, 11)  categorizes  the  key  assumptions  when  assessing  exposure  to  interest  rate risk  for  economic  value  and  earnings  at  risk  (EaR,  defined  as  the  short-term sensitivity  of  earnings  to  interest  rate  movements)  as  follows:"
  > "Behavioral  assumptions  for  accounts  with  embedded  customer  optionality"
  > "Behavioral assumptions  for customer  accounts  without  specific repricing dates,  particularly  those  with  no  (or  a  very  low)  interest  rate  attached"
  > "Banks'  planning  assumptions  for  the  investment  term  of  own  equity  capital"
  > "EBA (2015, 30) requires the bank to use at least one earnings-based measure and at least one economic  value measure of interest rate risk for the  monitoring  of  IRRBB."
  > — §5.1.3, line 2807 ^tata-reg-6

- Nguyên tắc tính SOT theo EBA (2018a): gồm mọi công cụ nhạy lãi suất; loại CET1 và vốn vĩnh viễn không có ngày call; gồm quyền chọn tự động và hành vi; NPE tính vào (sau dự phòng) nếu tỷ lệ NPE trên 2%; xử lý biên thương mại theo cách quản trị nội bộ; bảng cân đối run-off; sàn −100 bp tuyến tính tới 0 ở kỳ hạn 20 năm trở lên; cộng thay đổi giữa các đồng tiền với trọng số 50% cho thay đổi dương; một đường cong phi rủi ro mỗi đồng tiền; kỳ hạn bình quân tối đa 5 năm cho NMD.
  > "EBA  (2018a,  7-8)  introduces  a set of principles that institutions should apply  when  calculating  the supervisory  outlier  test :"
  > "All  interest  rate  sensitive  instruments  should  be  included"
  > "Common  equity  tier 1 (CET1)  capital and other perpetual own funds without  any  call  dates  should  be  excluded"
  > "Automatic  and  behavioral  options  should  be  included"
  > "If the NPE  ratio  is  above  the  materiality  threshold  of  2%,  NPEs  should be included net of provisions and should reflect the expected cash flow associated  with  these  assets"
  > "The treatment of commercial  margins and other spread components  in interest payments  in terms of their exclusion or inclusion into the cash flows  should  be  in  accordance  with  the  institution's  internal  management and  measurement  approach"
  > "A  run-off  balance  sheet  should  be  applied"
  > "Lower  reference  rate  of -100  basis  points  (linear  function  between -100  (0 year)  and  0  basis  points  (20 + years))  is  to  be  applied"
  > "For exposures  in various currencies, aggregation  of negative and positive changes  is  to  be  applied  weighting  the  positive  changes  by  a  factor  of  50%"
  > "One  risk-free  yield  curve  is  to  be  applied  per  currency"
  > "For  non-maturity  deposits  (NMDs)  ,  maximum  average  maturity  of  5  years is  to  be  used"
  > — §5.1.3, line 2833 ^tata-reg-7

- EBA (2018a) đặt hai ngưỡng EVE: sốc song song ±200 bp làm giá trị kinh tế giảm quá 20% vốn tự có thì báo ngay cơ quan quản lý; sáu kịch bản sốc (song song lên, xuống, dốc, phẳng, ngắn hạn lên, xuống) làm giảm quá 15% vốn cấp 1 thì báo cơ quan quản lý. Sàn sau sốc theo đoạn 115(k): −100 bp kỳ hạn tức thời, tăng 5 bp mỗi năm, 0% từ kỳ hạn 20 năm.
  > "EBA  (2018a,  8)  prescribes  two  thresholds  for  measuring  the  change  in  the economic  value  of  equity,  the  first  stemming  from  Article  98  (5)  of  CRD  IV (2013),  the  second  from  BCBS  (2016b):"
  > "The  impact  of  parallel  changes  in  interest  rates of ± 200  basis  points  on a  bank's  own  funds.  If  the  decline  in  economic  value  is  greater  than  20%, the  bank  needs  to  inform  the  competent  authority  immediately"
  > "The  impact  of  six  pre-defined  shock  scenarios  on  a  bank's  own  funds.  If  the decline  in  economic  value  is  greater  than  15%  of  Tier  1  capital,  the  bank needs  to  inform  the  competent  authority"
  > "The six  pre-defined  shock  scenarios used  in  the  second  threshold  are  defined in  Annex  III  of  EBA  (2018a):"
  > "EBA (2018a), in paragraph 115(k), also defines a maturity-dependent post-shock interest  rate floor to  be  applied  for  each  currency,  starting  at -100 basis points for immediate  maturities and increasing by 5 basis points per year,  eventually  reaching  0%  for  maturities  of  20  years  and  longer."
  > — §5.1.3, line 2852 ^tata-reg-8

- EBA (2022a, GL/2022/14) giữ cách xử lý IRRBB gần như không đổi so với hướng dẫn 2018, chỉ tăng cường một số điểm như giả định hành vi thận trọng cho NMD của đối tác phi tài chính; phần hoàn toàn mới là khung đánh giá, giám sát CSRBB.
  > "EBA  (2022a),  i.e.  the  guideline  GL/2022/14,  provides  a  regulatory  framework  for banks' internal measurement  with  respect  to  IRRBB,  as  well as a regulatory  framework  for  the  assessment  and  monitoring  of  credit  spread  risk arising  from  the  banking  book  (CSRBB).  The  treatment  of  IRRBB  is  largely unchanged  from  the  EBA  2018a,  b  Guidelines  and  is  only  enhanced  in  some areas,  such  as  the  prudent  behavioral  assumption  for  non-maturity  deposits (NMDs)  from  non-financial  counterparties. 37 What  is  completely  new  is  the elaboration  of  the  CSRBB."
  > — §5.1.3, line 2871 ^tata-reg-9

### Unit u08 — 5.2–5.5 IRRBB Measures (EBA SA, SOT, báo cáo EU) & 6 Future of ALM

- Theo CRD IV Điều 98, RTS/2022/09 của EBA đặt ra phương pháp chuẩn hoá (SA) và chuẩn hoá đơn giản (S-SA) để đánh giá rủi ro do thay đổi lãi suất tác động lên cả EVE và NII của hoạt động ngoài sổ kinh doanh.
  > "Mandated  by  Article 98  of  CRD  IV  (2013),  RTS/2022/09  has  developed regulatory technical standards  (RTS)  for  a  standardized  approach  (SA)  and simplified  standardized  approach  (S-SA)  for  the  purpose  of  assessing  the risks arising from  potential  changes in interest rates that  affect  both  the  Economic Value  of  Equity  (EVE)  and  the  Net  Interest  Income  (NII)  of  an  institution's non-trading  book  activities."
  > — §5.2, line 2877 ^tata-eba-1

- SA của EBA cho EVE tính thay đổi EVE bằng EVE ở kịch bản sốc trừ EVE ở kịch bản cơ sở. SA cho NII tính NII ở kịch bản cơ sở và từng kịch bản sốc bằng tổng ba cấu phần: lãi đã cố định đến hết ngày tái định giá; lợi suất phi rủi ro của từng dòng tiền tái định giá từ ngày tái định giá đến cuối kỳ dự phóng; biên thương mại của từng dòng tiền từ ngày reset biên (thường là ngày đáo hạn) đến cuối kỳ dự phóng; cả hai cấu phần sau theo giả định bảng cân đối không đổi.
  > "The  EBA  standardized  approach  (SA)  for  the  Economic  Value  of  Equity (EVE)  calculates  the change  in  the  economic  value  of  equity by  subtracting  the economic  value  of  equity  in  the  baseline  scenario  from  the  economic  value  of equity  in  the  shock  scenarios."
  > "The EBA  standardized  approach  (SA) to  net  interest  income  (NII) 38 calculates  NII  for  the  baseline  scenario  and  for  each  individual  interest  rate  shock scenario  as  the  sum  of  three  NII  sub-components:"
  > "The  aggregation of interest payments  up  to and including the repricing date (i.e., NII flows that are already fixed and whose amount  will not change  as  a  result  of  interest  rate  changes);  plus"
  > "the  projection  of  the  risk-free  return  for  each  repricing  cash  flow  between the moment  of repricing up to the end of the projection horizon, in accordance  with  the  assumption  of  a  constant  balance  sheet;  plus"
  > "the  projection  of  the  commercial  margin  for  each  notional  repricing  cash flow  between  the  moment  of  the  reset  of  the  margin  (typically  at  the  instrument's maturity)  up  to the end of the projection horizon,  in  accordance with  the  assumption  of  a  constant  balance  sheet."
  > — §5.2.1, line 2885 ^tata-eba-2

- Cả SA cho EVE lẫn SA cho NII có add-on cho quyền chọn tự động và giới hạn đối với giả định hành vi (tiền gửi không kỳ hạn bán lẻ và bán buôn, trả trước, rút trước hạn tiền gửi có kỳ hạn, cam kết cho vay). Biên thương mại dự phóng của nghiệp vụ mới dựa trên biên của công cụ phát sinh trong năm trước.
  > "For both the SA on EVE  and  the  SA  on NII, an add-on  for  automatic optionality is computed. In addition, some limits are placed on behavioral  assumptions  about  the  timing  and  amount  of  the  customer  cash  flows, e.  g.,  for  non-maturity  retail  and  wholesale  deposits,  loan  prepayments,  term deposit  redemption  rates,  and  loan  commitments."
  > "As for the projected commercial margin component of NII (of new business production), it should be based on the commercial margin of instruments  originated  in  the  previous  year."
  > — §5.2.1, line 2893 ^tata-eba-3

- Để xử lý việc NII không thể hiện tác động lãi suất ngoài kỳ tính NII, SA cho NII của EBA có thêm cấu phần đo thay đổi giá trị thị trường của các công cụ, tính tương tự EVE nhưng loại công cụ không định giá theo thị trường và loại dòng tiền trong kỳ NII để tránh tính trùng.
  > "In order to address the fundamental problem that NII calculations do not show the impact of interest rate changes that are outside of the net interest  income  calculation  horizon  (see  Sect.  2.2.6),  the  EBA  has  included  a component  in  the  SA  on  NII  that  measures  market  value  changes  for  these instruments.  The calculation is based on a similar calculation as for  EVE, but  excludes  instruments  that  are  not  market  to  market. 39 To avoid double counting, cash flows falling within the NII horizon are excluded from the calculation  of  market  value  changes."
  > — §5.2.1, line 2897 ^tata-eba-4

- S-SA dành cho ngân hàng nhỏ và không phức tạp, phải thận trọng tối thiểu bằng SA; đơn giản hoá ở tiền gửi lõi không kỳ hạn, tác động tăng biến động lên quyền chọn tự động, độ chi tiết biên thương mại và cách tính lãi đến ngày tái định giá.
  > "The simplified standardized approach (S-SA) was developed to reflect the generally  less  advanced  capabilities  of  the  small  and  non-complex  bank  and to meet the need for a methodology  that is at least as conservative as the standardized  approach  (SA). 40"
  > "Simplifications include the treatment  of non-maturity  core  deposits and cash  flows,  the  impact  of  an  increase  in  volatility  on  automatic  options,  the granularity  of  commercial  margins,  and  the  calculation  of  interest  payments up  to  and  including  the  repricing  date."
  > — §5.2.2, line 2901 ^tata-eba-5

- SOT trên EVE (RTS/2022/10) nhằm xác định ngân hàng có EVE giảm quá 15% vốn cấp 1 dưới một kịch bản sốc. RTS/2022/10 giữ các kịch bản sốc giám sát của CRD IV Điều 98 và Phụ lục III EBA/GL/2018/02; ΔEVE tính theo giả định bảng cân đối run-off (vị thế đáo hạn không được thay thế).
  > "A supervisory  outlier  test  (SOT)  on  EVE is  envisaged  to  identify  banks  whose economic  value  of  equity  (EVE)  falls  by  more  than  15%  of  their  Tier  1  capital under  a  shock  scenario."
  > "EBA  (2018a),  i.  e.,  the  guidelines  on  the  management  of  interest  rate  risk arising  from  non-trading  book  activities  (EBA/GL/2018/02),  already  laid  out the  EBA  supervisory  outlier  test  (SOT)  with  respect  to  the  economic  value of  equity  (EVA).  RTS/2022/10  keeps  the  supervisory  shock  scenarios  found in  Article  98  of  CRD  IV  (2013)  and  in  Annex  III  of  EBA  (2018a).  They  are listed  in  Sect.  5.1.3."
  > "RTS/2022/10 requires the change in EVE to be calculated under the assumption  of  a  run-off  balance  sheet,  where  existing  positions  mature  and are  not  replaced."
  > — §5.3.1, line 2913 ^tata-sot-1

- RTS/2022/10 hiệu chỉnh sàn lãi suất sau sốc phụ thuộc kỳ hạn thành sàn tuyến tính: −150 bp cho kỳ hạn tức thời, tăng tuyến tính 3 bp mỗi năm, đạt 0% ở kỳ hạn 50 năm; lý do là lãi suất cơ sở đã xuống dưới sàn cũ vào tháng 12/2020 và tháng 3/2022.
  > "RTS/2022/10  also  recalibrates  the  maturity  dependent  post-shock interest rate floor defined in paragraph 115(k) of EBA  (2018a) to reflect the fact that  in  March  2022  and  again  in  December  2020  the  baseline  (unshocked) interest  rate  moved  below  the  floor.  The  new  so-called linear  floor is  defined as  a  lower  bound  starting  with -150  basis  points  for  immediate  maturities  and increasing  linearly  by  3  bps  per  year,  reaching  0%  for  maturities  of  50  years."
  > — §5.3.1, line 2919 ^tata-sot-2

- SOT trên NII nhằm xác định ngân hàng có NII 1 năm suy giảm lớn dưới kịch bản sốc; 'suy giảm lớn' là tỷ lệ thay đổi NII kế toán so với vốn cấp 1 vượt 5%. Khác SOT EVE ở hai điểm: phải bao gồm biên thương mại (EVE thì có thể loại), và tính trong kỳ 1 năm theo bảng cân đối không đổi (thay dòng tiền đáo hạn hoặc tái định giá bằng công cụ mới cùng đồng tiền, số tiền, kỳ tái định giá). SOT NII hiện không áp sàn tuyến tính.
  > "A supervisory  outlier  test (SOT)  on  NII is  envisaged  to  identify  banks  whose one-year  net  interest  income  (NII)  experiences  a  large  decline  in  the  context of  a  shock  scenario.  A  'large  decline'  is  defined  as  the  ratio  of  the  change  in a  bank's  accounting  NII 41 to  its  Tier  1  capital  exceeding  5%. 42"
  > "Many  assumptions  for  the  calculation  of  SOT  on  EVE  and  SOT  on  NII are harmonized,  in  particular those listed in Articles 3(2) to 3(4) and 3(7) to  3(10)  of  RTS/2022/10.  However,  there  are  two  fundamental  differences. Article  4  specifies  that  for  the  calculation  of  SOT  on  NII,"
  > "commercial margins (and other spread components) must be included (whereas  for  EVE  they  may  be  excluded),  and"
  > "the  change  in  NII  must  be  calculated  over  a  one-year  horizon  under  the assumption  of  a constant  balance  sheet ,  where  its  total  size  and  composition, including  on- and  off-balance  sheet  items,  shall  be  maintained  by  replacing maturing  or  repricing  cash  flows  with  new  instruments  that  have  comparable  features  with  regard  to  the  currency,  amount  and  repricing  period  of the  instruments  generating  the  repricing  cash  flows."
  > "Currently, RTS/2022/10  NII  SOT  calculations do not include a linear floor."
  > — §5.3.2, line 2923 ^tata-sot-3

- Bài toán tuân thủ đồng thời: khi ngân hàng muốn không là outlier theo cả EVE và NII, giới hạn SOT EVE áp cận trên và cận dưới lên tỷ trọng tài sản lãi suất cố định theo duration, còn giới hạn SOT NII áp lượng tài sản cố định tối thiểu; phải tối ưu để thoả cả hai, vùng tuân thủ có thể rất nhỏ và dịch chuyển theo thay đổi khối lượng.
  > "A simultaneous  compliance  problem refers  to  a  situation  where  compliance  with one (regulatory) constraint threatens compliance with another one. With respect  to  SOT ,  this  is  the  case  when  a  bank  aims  to  become  neither  an  outlier bank  with  respect  to  EVE  nor  an  outlier  bank  with  respect  to  NII."
  > "If a bank is looking for the right amount and the right duration of fixed-rate assets that would be a SOT-compliant match for a large sight deposit  position  (modeled  by  the  EBA  standardized  approach),  two  partially conflicting  requirements  must  be  met:"
  > "The SOT on EVE limit imposes an upper and lower bound on the proportion  of  fixed-rate  assets  as  a  function  of  asset  duration."
  > "The  SOT  on  NII  limit  imposes  a  minimum  amount  of  fixed  assets."
  > "Each  requirement  defines  its  own  range  of  possible  combinations  between the share of fixed rate assets and  their duration.  In order to satisfy both  at the same  time,  an optimization  has  to be performed.  An  illustrative sketch of  the  constraints  of  a  linear  optimization  problem  between  SOT  EVE  and SOT NII  requirements is shown  in  Fig.  5.2.  Violated  constraints  are  shown in  gray,  while  feasible  solutions  are  shown  in  white."
  > "The  zone  of  compliance  may  be  very  small  and  may  move  over  time  as  a function  of  volume  changes."
  > — §5.4, line 2934 ^tata-sot-4

- Báo cáo giám sát IRRBB ở EU theo quy định thực thi (EU) 2024/855 ngày 15/3/2024, gồm 5 nhóm mẫu biểu: đánh giá IRRBB bằng SOT EVE, NII và thay đổi MV; phân rã độ nhạy (ΔEVE, ΔNII, ΔMV) theo vị thế và đồng tiền; tham số mô hình hành vi; dòng tiền tái định giá (theo góc nhìn EVE, riêng từng đồng tiền); thông tin định tính.
  > "Supervisory  reporting  of  interest  rate  risk  in  the  banking  book  is  detailed  in Commission  implementing  regulation  (EU)  2024/855  of  15  March  2024. 43 It details the reporting requirements  for banks to provide supervisors with the  data  needed  to  monitor  interest  rate  risk  in  the  banking  book  (IRRBB) and  the  impact  of  changes  in  interest  rates,  including  the  interaction  of  the IRRBB  with  the  bank's  management  of  interest  rate  risk  and  the  identification of  outliers  under  both  the  supervisory  outlier  test  (SOT)  for  economic  value of  equity  and  the  SOT  for  net  interest  income."
  > "Annex  II  to  regulation  (EU)  2024/855  contains  five  sets  of  templates:"
  > "IRRBB  assessment using supervisory outlier tests (SOTs) on economic value  of  equity  (EVE)  and  the  net  interest  income  (NII),  and  market  value (MV)  changes"
  > "Breakdown  of  IRRBB  sensitivity  estimates"
  > "Behavioral  modeling  parameters"
  > "IRRBB  repricing  cash  flows"
  > "Qualitative  information"
  > "This  template  requires  a  further  breakdown  of  a  bank's  sensitivity  estimates ( /Delta1 EVE, /Delta1 NII, /Delta1 MV)  by  balance  sheet  position  and  currency."
  > "This template  requires banks  to report repricing cash flows for the  balance sheet items reported in the above templates. This information should be reported  from  an  EVE  perspective,  taking  into  account  the  requirements  and modeling  assumptions  specified  in  the  EBA  supervisory  outlier  test  (SOT), and  separately  for  each  currency."
  > — §5.5, line 2951 ^tata-rep-1

- Trong mẫu dòng tiền tái định giá, góc nhìn hợp đồng xếp sản phẩm không kỳ hạn (kể cả NMD) là vị thế biến đổi ngắn hạn (bucket ngắn nhất), không áp trả trước và rút trước hạn hành vi; góc nhìn hành vi phải nhất quán với dòng tiền đã mô hình hoá.
  > "Contractual and behavioral information shall be reported, considering different  forms  of  optionality:"
  > "Contractual optionality assumes contractual repricing dates without considering behavioral assumptions. Only contractual and legal features (excluding  automatic  options  and  legal  options 44 )  are  considered.  The  cash flow  profile  of  non-maturity  products  (including  NMDs)  should  be  treated as short-term variable positions (shortest time bucket). Behavioral early termination  and  prepayment  are  not  applied."
  > "Behavioral modeling in the baseline scenario should be consistent with the  modeled  repricing  cash  flows,  which  take  behavioral  assumptions  into account  where  appropriate."
  > — §5.5.3, line 2992 ^tata-rep-2

- Mẫu tham số hành vi: ngày tái định giá bình quân của từng nhóm NMD tính bình quân gia quyền theo dòng tiền, tách phần lõi; pass-through rate (PTR) là tỷ lệ bình quân gia quyền của cú sốc lãi suất được giả định truyền vào lãi suất NMD, báo cáo theo từng nhóm NMD; rủi ro trả trước và rút trước hạn báo cáo qua ngày tái định giá bình quân và tỷ lệ trả trước, rút trước hạn có điều kiện.
  > "In this template, average repricing dates are to be calculated as a weighted average of the repricing dates and the notional repricing cash flows of the positions  in  each  relevant  NMD  category  with  a  further  breakdown  of  the part  deemed  to  be  the core  volume (for  those  NMD's  different  to  wholesale financial)."
  > "The  pass-through  rate  (PTR),  defined  as  the  weighted  average  percentage of  the  interest  rate  shock  assumed  to  be  passed  through  to  their  non-maturity deposits (NMDs)  under  the  interest rate regulatory scenarios and the NII metric  specified  in  the  EBA  RTS  on  SOT ,  must  be  reported  per  NMD  category.  This  recognizes  that  the  rates  set  by  the  bank,  known  as  administered rates, are only loosely related to market rates and that the pass-through of changes  in market  rates to sight deposit  rates is partial (see Sect. 2.5.8  and Fig.  2.36)."
  > "Finally, prepayment and early redemption risks must be specified by providing average repricing dates and conditional prepayment and early redemption  rates,  respectively."
  > — §5.5.4, line 3000 ^tata-rep-3

- Mẫu định tính hỏi: dùng SA, S-SA hay IMS cho SOT; phương pháp tính (repricing gap, duration gap, định giá lại toàn bộ); có xét dòng tiền có điều kiện, rủi ro quyền chọn, basis risk, phí trả trước, nợ xấu, cam kết cho vay lãi suất cố định; EVE SOT có gồm biên thương mại không; phương pháp xác định kỳ tái định giá hành vi NMD (kể cả replicating model) và yếu tố xác định số dư lõi; chiến lược phòng ngừa; đường cong phi rủi ro dùng để chiết khấu.
  > "Which approach is used for SOT EVE and SOT NII, the Standardized  Approach  (SA),  the  Simplified  Standardized  Approach  (S-SA),  or  an Internal  Measurement  System  (IMS)."
  > "The method used to calculate the SOT NII and the SOT EVE, i.e. repricing or duration gap analysis, a full revaluation, or a mix/other method."
  > "An  indication of whether  conditional cash flows, option risk, basis risk, loan prepayment penalty fees, pension obligations/pension plan assets, non-performing exposures, fixed rate loan commitments, risk of retail prepayments and risk of early redemption have been considered in the calculation  of  the  NII  SOT  and  the  EVE  SOT ."
  > "An  indication  of  whether  commercial  margins  or  other  spread  components have  been  included  in  the  calculation  of  the  EVE  SOT ."
  > "The  method  used  to  determine  the  behavioral  repricing  time  of  the  nonmaturity  deposits  (NMDs),  including  a  replicating  model."
  > "With  respect  to  NMDs,  relevant  drivers  used  to  identify  core  balances."
  > "IRRBB  mitigation  and  hedging  strategies  with  respect  to  EVE  and  NII."
  > "Indication  of  the  risk-free  yield  curve  used  for  discounting  in  the  context of  EVE  and  SOT  EVE."
  > — §5.5.5, line 3010 ^tata-rep-4

- FinTech (kể cả mobile banking) giúp khách hàng phản ứng nhanh hơn với thay đổi lãi suất và chuyển tài khoản dễ hơn; khách hàng bán lẻ có xu hướng giao dịch nhiều hơn, ít gắn bó lâu dài. Điều này buộc ngân hàng xem lại khung ALM, nhất là mô hình quyền chọn nhúng của NMD, với cơ sở khách hàng không đồng nhất và lịch sử dữ liệu ngắn khi hiệu chỉnh lại.
  > "FinTech has enabled bank customers to react much  more quickly and opportunistically to changes in the interest rate environment. Whereas 'sleepy' depositors used to stay put when interest rates rose, FinTech (including mobile  banking)  has made  it less time consuming,  less difficult and less stressful to switch  accounts. 4 There appears to be a trend  among retail bank customers (mirroring a similar trend among  institutional bank customers) to become  more transactional , and less inclined to maintain a long-term  relationship  with  their  house  bank  in  what  is  known  as relationship banking . 5"
  > "The  changing  behavior  of  customers  using  FinTech  innovations  requires banks to rethink their ALM  frameworks, especially those used to model embedded options in non-maturity deposits (NMDs).  The challenge for ALM  is  to develop  new  models  that  reflect  a  heterogeneous  customer  base and  to  rely  on  a  relatively  short  history  when  recalibrating  existing  models."
  > — §6.1, line 3135 ^tata-fut-1

- Công cụ DeFi gần như chưa trải qua một chu kỳ tài chính đầy đủ, nên thiếu dữ liệu lịch sử để hiệu chỉnh mô hình ALM về hành vi khách hàng (trả trước, rút sớm, chuyển nhà cung cấp).
  > "One of the megatrends shaping the world of finance is the push toward decentralization. This new form of financial activity, referred to as  decentralized finance or DeFi,  aims  to replace  central  market  participants  with  a network  of  decentralized  entities.  The  most  prominent  case  of  decentralization  in  the  financial  markets  comes  from  the  field  of  data  storage  in  the  form of  the  distributed  ledger  technology  (DLT).  DLT  allows  information  to  be stored  through  a  distributed  ledger,  which  is  a  repeated  digital  copy  of  data in  multiple  locations,  as  in  a  blockchain."
  > "Virtually none  of the  DeFi-based  instruments  have  been tested  through a full financial  cycle.  Asa  result, there  is a lack of  historical  data  that  can  be used  to  calibrate  risk  management  and  ALM  models  with  respect  to  customer behavior (e. g., prepayment,  early withdrawal, switching between  financial service  providers)."
  > — §6.2, line 3143 ^tata-fut-2

- Big data và advanced analytics cho phép đánh giá rủi ro theo thời gian thực ở mức từng khách hàng (ví dụ mô hình duration kỳ vọng của từng khoản tiền gửi không kỳ hạn); khả năng kiểm toán là vấn đề quan trọng khi dùng AI/ML trong ALM, giám sát kỳ vọng tổ chức ghi chép và giải thích lựa chọn đặc tả mô hình khi kiểm định phương pháp đo IRRBB.
  > "As banks collect a wealth of data from thousands and millions of end customers,  it  makes  sense  to  gain  insights  that  can  be  used  for  risk  management and ALM.  While the computing power of the past did not allow for  detailed  analysis  of  each  individual  customer,  today's  massive  computing power, cheap data storage capacity, and advances in artificial intelligence and machine learning make it possible to assess risk in real time and at customer-level granularity. In the same way that social media platforms deliver  individualized  content  to  billions  of  users,  banks  could,  for  example, model  the expected duration of each individual sight deposit in real time, based  on  each  individual  customer's  behavior  as  observed  by  the  bank.  In  an ideal  world,  the  bank  anticipates  a  customer's  withdrawal  before  it  happens and  proactively  makes  the  necessary  ALM  adjustments. 16"
  > "Auditability is an important  issue when  it comes  to the use of artificial intelligence and machine  learning in ALM.  As  part of  model governance, supervisors  expect  that  when  validating  IRRBB  measurement  methodologies, 'institution  should  document  and  explain  model  specification  choices  as  part of the validation  process.' 17 The  FSB  suggests  that '[in] some  cases, firms may  be  simulating  the  outcomes  of  AI  models  in  traditional  models  or  restrict themselves  to  a smaller set of AI approaches  that  do  not  suffer  from  'black box'  problems.' 18"
  > — §6.3, line 3159 ^tata-fut-3

- Rủi ro khí hậu tác động lên thu nhập và vốn qua các kênh tín dụng đối tác, huy động vốn, đầu tư và quy định; trong FTP, sự kiện khí hậu có thể gây hành vi bất lợi của khách hàng (giảm trả nợ, rút tiền gửi, tăng sử dụng hạn mức) và lý tưởng thì lãi suất FTP nên phạt nghiệp vụ làm tập trung các rủi ro này.
  > "Climate  risk  impacts  banks'  earnings  and  capital  through  several  transition channels.  These  include:"
  > "Counterparty  credit  risk  channel:  The  bank's  customers  and  capital  market counterparties  may  be  affected  by  climate  change.  This  affects  their  credit quality  and  should  be  reflected  in  credit  risk  management."
  > "Funding  channel:  Banks'  funding  channels  (such  as  bond  issuance)  may  be affected  by  their  perceived  climate  risk.  This  affects  their  cost  of  funding."
  > "Investment  channel:  Banks'  return  on  investment  in  assets  (e.  g.,  their  securities  portfolio)  may  be  affected  by  climate  risk.  This  affects  not  only  the expected  return  on  assets,  but  also  the  realized  return  after  climate  events have  occurred."
  > "Regulatory  channel:  Regulators  and  supervisors  are  pushing  banks  to  assess climate risks and to maintain capital and liquidity buffers. This affects, among  other  things,  banks'  regulatory  cost  of  capital."
  > "An  example  of  an  area  where  climate  risk  management  is  likely  to  become an  integral  part  of  treasury  and  ALM  in  the  future  is  the  FTP  process.  Certain climate events (flooding, extreme heat, etc.) can lead to adverse customer behavior  (reduction  in  loan  payments,  withdrawal  of  deposits,  increased  use of credit facilities), and ideally the FTP  rate should penalize business that leads  to  a  concentration  of  these  risks."
  > — §6.4, line 3175 ^tata-fut-4

- Mô hình hành vi trong ALM thường phân khúc khách hàng theo đặc điểm (địa vị kinh tế xã hội, lịch sử vay, địa lý, thu nhập, tuổi); yếu tố phân biệt hành vi số dư tiền gửi gồm số dư ban đầu, có lãi suất khuyến mãi hay không, độ sâu và thời gian quan hệ, tuổi khách hàng, kênh mở; mỗi nhóm được hiệu chỉnh mô hình riêng và phải được điều chỉnh, hiệu chỉnh, backtest liên tục.
  > "A common  approach to behavioral modeling in ALM  is to segment a bank's customer pool into more granular buckets according to customerspecific  factors,  such  as  socioeconomic  status,  borrowing  history,  geography, net income, or physical age. 30 Soulellis (2017, 123) details several key differentiators that can be used to model differentiated deposit balance behavior:"
  > "The  amount  of  originating  incoming  balance"
  > "Whether  or  not  a  promotional  or  introductory  deposit  rate  was  given"
  > "The  depth  and  age  of  the  customer's  relationship  with  the  bank"
  > "The  physical  age  of  the  customer"
  > "The  origination  channel  when  opening  the  deposit  (e.  g.,  online  vs.  in a branch)."
  > "After  segmenting  the  customer  base,  multiple  behavioral  models  are  individually  calibrated  to  the  different  observed  behaviors  within  each  pool.  On an  ongoing  basis,  these  models  need  to  be  adjusted,  calibrated  and  back-tested to reflect changes in market factors (interest rates, etc.), macroeconomic events,  new  banking  products,  differences  in  customer  sophistication,  changes in  competitor  strategy  and  the  evolution  of  the  bank's  balance  sheet."
  > — §6.5, line 3194 ^tata-fut-5

### Unit u04–u05 (bổ sung 2026-10-22) — 2.3 Funds Transfer Pricing (dòng 1581–1783)

- FTP là quy trình nội bộ gán lãi suất tài trợ cho từng vị thế bên tài sản và lãi suất sinh lời cho từng vị thế bên nợ phải trả trong sổ ngân hàng.
  > "Funds Transfer Pricing is an internal process that aims to assign a funding rate to each asset-side position and an earning rate to each liability-side position within the banking book."
  > — Chapter 2, §2.3, line 1583 ^tata-ftp-3

- Không được giả định nguồn vốn là miễn phí chỉ vì ngân hàng đang dư thanh khoản, vì vi phạm nguyên tắc chi phí cơ hội; cũng không phù hợp khi dùng một lãi suất duy nhất như WACC cho mọi tài sản và nợ phải trả, vì tài sản dài hạn cần nguồn vốn dài hạn, thường đắt hơn.
  > "it would be wrong to assume that funding is free because the bank has excess liquidity on its balance sheet that could be used"
  > "This would be a violation of the economic principle of opportunity cost"
  > "It would also be inappropriate to use a single rate, such as the bank's weighted average cost of capital (WACC), as the funding and as the earnings rate for all assets and liabilities, respectively. Longer-term assets require longer-term funding"
  > — Chapter 2, §2.3, line 1585 ^tata-ftp-4

- Sau khi có lãi suất phản ánh đúng chi phí tài trợ của từng vị thế, thu nhập lãi được phân bổ nội bộ: khối khách hàng nhận phần thu nhập từ khả năng đạt lãi suất khách hàng tốt hơn thị trường, Treasury nhận phần thu nhập từ việc đi vay hoặc đầu tư vốn theo lãi suất thị trường hiện hành.
  > "The customer area of a bank should receive the portion of the earned income that results from its ability to secure a better-than-market customer rate"
  > "is allocated the portion of the earned income that results from the need to borrow or to invest the appropriate funds at prevailing market rates"
  > — Chapter 2, §2.3, line 1587 ^tata-ftp-5

- Khi tài sản và nợ phải trả khớp hoàn toàn về quy mô và kỳ hạn, ngân hàng không chịu rủi ro lãi suất, nhưng NIM vẫn cần được chia cho bộ phận huy động và bộ phận cho vay; việc chia này đòi hỏi hệ thống FTP.
  > "As asset and liability positions are perfectly matched in terms of both size and maturity, the bank is not exposed to any interest rate risk."
  > "the total margin contribution must be divided into two individual margin contributions for the customer deposit and for the customer loan departments, respectively."
  > "This requires an FTP system."
  > — Chapter 2, §2.3.1, lines 1597–1599 ^tata-ftp-6

- Cost of funds là lãi suất mà Treasury cho là phù hợp để huy động vốn trên thị trường vốn qua các kênh của ngân hàng; chênh lệch giữa lãi suất cho vay khách hàng và cost of funds là đóng góp biên của khối cho vay. Chi phí tài trợ phụ thuộc kỳ hạn: khoản vay 2 năm thường đắt hơn khoản vay 1 năm.
  > "The rate that the treasury department deems appropriate for raising funds on the capital market (using bank-specific funding channels) is the cost of funds"
  > "The difference between the customer lending rate and the cost of funds is the margin contribution assigned to the lending area."
  > "The cost of funding depends on the term. A 2-year loan is typically more expensive than a 1-year loan."
  > — Chapter 2, §2.3.2, lines 1609–1611 ^tata-ftp-7

- Gộp các điểm cost of funds theo các kỳ hạn tạo thành transfer price curve (còn gọi Cost of Funds Curve hoặc Funds Transfer Price Curve). Theo phương pháp matched maturity, mỗi vị thế phát sinh được gán FTP rate từ điểm cùng kỳ hạn trên đường cong.
  > "Combining all points of cost of funds rates for different maturities gives the transfer price curve."
  > "In the matched maturity method of FTP implementation, each originated asset or liability position is assigned an FTP rate from the transfer price curve that matches the maturity of the position."
  > — Chapter 2, §2.3.3, lines 1615–1617 ^tata-ftp-8

- Ví dụ của Tata: tiền gửi 1 năm lãi suất 1% so với FTP 1 năm 2% cho đóng góp 1% của khối huy động; khoản vay 2 năm lãi suất 4% so với FTP 2 năm 3% cho đóng góp 1% của khối cho vay. Chênh lệch giữa điểm 1 năm và 2 năm trên FTP curve là structural contribution.
  > "the 1-year deposit rate is compared to an internal 1-year transfer price rate of 2%. The difference, 1%, is the margin contribution of the deposit area."
  > "The 2-year loan rate is compared to the corresponding transfer price rate, which is 3%, and the resulting margin contribution of the lending department is 1%."
  > "The difference between a 1- and a 2-year rate on the FTP curve, called structural contribution"
  > — Chapter 2, §2.3.3, line 1623 ^tata-ftp-9

- Vì FTP curve bù đắp cho Treasury cả rủi ro lãi suất lẫn rủi ro thanh khoản, nên tách rủi ro gộp này thành hai cấu phần: dựng pure interest rate risk curve rồi cộng thêm funding spread.
  > "Since the FTP curve compensates the treasury department for both, interest rate and liquidity risk"
  > "it is useful to separate this combined risk into its two components"
  > "This is done by constructing a pure interest rate risk curve and then adding a funding spread to it."
  > — Chapter 2, §2.3.5, line 1641 ^tata-ftp-10

- Đường cong phi rủi ro dựng từ repo rate có thể coi gần như phi rủi ro vì dựa trên vay có tài sản bảo đảm, nhưng thị trường repo mang tính ngắn hạn, thường chỉ thanh khoản đến 1–2 năm và có lúc mất thanh khoản (như khủng hoảng 2007/2008).
  > "The downside of this approach is that the repo market is short-term in nature and typically only liquid out to one or two years."
  > "the repo market can become illiquid at times"
  > — Chapter 2, §2.3.5, line 1654 ^tata-ftp-11

- Dùng đường cong swap EURIBOR làm proxy phi rủi ro có ưu điểm kéo dài tới 30 năm và khá thanh khoản; hạn chế là lãi suất swap phản ánh rủi ro đối tác giữa các ngân hàng vì dựa trên vay không bảo đảm liên ngân hàng.
  > "The main advantage of using the swap curve as a benchmark is that it extends out to 30 years and is quite liquid."
  > "the rate that is exchanged in a EURIBOR interest rate swap is based on unsecured borrowing and lending between banks, and, therefore the swap rate reflects the counterparty credit risk between banks"
  > — Chapter 2, §2.3.5, lines 1655–1657 ^tata-ftp-12

- Funding spread trên lãi suất phi rủi ro là đặc thù theo từng tài sản. Về lý thuyết mỗi khoản mục bảng cân đối có thể có một FTP curve riêng, nhưng thực tế nên dùng một FTP curve phản ánh funding spread bình quân rồi điều chỉnh spread theo từng trường hợp. Ví dụ: ngân hàng phát hành note cố định 2 năm 3% và note thả nổi 2 năm 2,2% thì funding spread 2 năm là 80 bp trên đường cong phi rủi ro.
  > "Funding spreads over and above the risk-free interest rate are asset specific."
  > "it is more appropriate to use a single FTP-curve that reflects an average funding spread and then to adjust the spread on a case-by-case basis as necessary"
  > "if the bank currently issues 2-year fixed rate notes at 3% and 2-year floating rate notes at 2.2%, then the funding spread for a 2-year term would be 80 bp over the interest rate risk-free curve"
  > — Chapter 2, §2.3.5, line 1659 ^tata-ftp-13

- Việc tách FTP thành hai cấu phần cho phép định giá sản phẩm có kỳ hạn của chỉ số lãi suất tái định giá khác kỳ hạn hợp đồng. Ví dụ: khoản vay 2 năm cố định lãi suất 1 năm đầu rồi tái định giá có FTP rate = 1,6% rủi ro lãi suất + 80 bp liquidity premium = 2,4%.
  > "The Separation of FTP into two risk sub-components has the advantage of allowing the pricing of products where the contractual reset reference interest rate index has a different maturity than the contractual maturity of the instrument"
  > "would have an FTP rate calculated as 1.6% interest rate risk + 80 bp liquidity premium = 2.4%"
  > — Chapter 2, §2.3.5, line 1661 ^tata-ftp-14

- Với vị thế ngoại tệ do ALM tập trung quản lý, thường không thực tế tạo nhiều FTP curve; cách khác là định giá trên FTP curve của đồng tiền cơ sở sau khi áp điều chỉnh cross-currency lên funding spread, quan sát được trên thị trường cross-currency swap của các đồng tiền chính. Công ty con ở vùng tiền tệ khác có thể dựng FTP curve theo từng đồng tiền dựa trên hoạt động thị trường tại chỗ.
  > "it may not be practical to create multiple FTP curves for multiple currencies, but rather to price the non-base currency position on the base currency FTP curve after applying a cross-currency adjustment to the funding spread"
  > "this cross-currency adjustment can be observed in the cross-currency swap market"
  > "the local ALM desks may be able to create currency-specific FTP curves, based on market activity (funding, deposits etc.) in those regions"
  > — Chapter 2, §2.3.6, lines 1667–1673 ^tata-ftp-15

- Ngoài phân bổ NIM và tập trung rủi ro lãi suất, thanh khoản về Treasury, FTP có chức năng thứ ba là steer hoạt động khách hàng và cấu trúc bảng cân đối. Ví dụ: ngân hàng dư tiền gửi và thiếu khoản vay có thể dịch FTP curve xuống, giảm đóng góp biên của khối tiền gửi, tăng đóng góp của khối cho vay, khuyến khích cho vay thêm và hạn chế huy động.
  > "Internal allocation of the net interest margin to different business units."
  > "Centralization of interest rate and liquidity risk in the treasury department at an appropriate transfer price based on the riskiness of the positions."
  > "it can be used to steer the bank's customer business and as a tool to influence the evolution of the balance sheet structure"
  > "shifting the FTP curve downward. This will reduce the margin contribution allocated to the customer deposit department, while increasing the margin contribution to the loan department."
  > — Chapter 2, §2.3.7, lines 1677–1682 ^tata-ftp-16

- Tata nhận định chức năng steering của FTP mang tính chính trị cao, vì FTP là nguồn sự thật duy nhất để đánh giá giá trị gia tăng cảm nhận được của các khối kinh doanh, và thay đổi nhỏ có thể cho bức tranh khác về khối nào đóng góp NII.
  > "The steering function of FTP is highly political"
  > "FTP is essentially the single source of truth for assessing the perceived value added by different business lines."
  > "Small changes in FTP can paint significantly different pictures of which business line contributed to a bank's overall NII."
  > — Chapter 2, §2.3.7, line 1692 ^tata-ftp-17

- Schäfer et al. (2017, trích bởi Tata): một phần đáng kể NII chủ yếu do mô hình nội bộ định giá chi phí tài trợ từ/đến Treasury chi phối chứ không do biên khách hàng; đổi giả định kỳ hạn hành vi của danh mục tiền gửi không kỳ hạn doanh nghiệp hoặc lãi suất tính lợi ích vốn sẽ làm lệch NII mà quan hệ kinh doanh bên ngoài không đổi.
  > "a significant portion of the net interest income is usually primarily driven not by client margins but by internal models that value the cost of funding provided from or to the bank's treasury department"
  > "adjusting the behavioural maturity assumption for a corporate sight deposit portfolio, or a different interest rate applied to calculate capital benefit"
  > "will distort the net interest income significantly without the slightest change to the bank's actual business relationships to the outside world"
  > — Chapter 2, §2.3.7, line 1694 (trích Schäfer et al. 2017, p. 584) ^tata-ftp-18

- Các yêu cầu quy định sau khủng hoảng 2007/2008 tác động lên chi phí tài trợ của vị thế nội và ngoại bảng. Mỗi yêu cầu, khi bị vị thế cần định giá trên FTP curve kích hoạt, tạo ra một chi phí biên cho ngân hàng.
  > "a number of regulatory requirements have been adopted that have an impact on the funding costs of both on- and off-balance sheet positions of banks"
  > "Each requirement, when triggered by a position to be priced on the FTP curve, results in some cost (at the margin) to the bank."
  > — Chapter 2, §2.3.8, line 1700 ^tata-ftp-19

- LCR: trích dẫn trong Tata cho rằng phần chi phí HQLA bổ sung mà một vị thế đòi hỏi, vượt chiến lược thông thường, có lẽ nên được tính vào transfer price; nếu không, hoạt động mới sẽ làm xấu LCR vì chi phí HQLA tăng thêm không được định giá.
  > "this additional cost of HQLA should probably be transfer priced"
  > "new business will tend to deteriorate the bank's LCR as the incremental cost of additional HQLA will not be priced"
  > — Chapter 2, §2.3.8.1, line 1704 ^tata-ftp-20

- Một số hệ thống FTP đã phân bổ chi phí LCR cho cả nợ phải trả và tài sản, tạo động lực cho tài sản sinh dòng vào LCR và giảm quy mô danh mục tài sản thanh khoản cần nắm giữ.
  > "Some FTP systems already address the cost of doing business from a regulatory constraint perspective by allocating LCR costs to both liabilities and assets"
  > "incentivizing assets that generate an LCR inflow and reduce the size of the required liquid asset portfolio holdings"
  > — Chapter 2, §2.3.8.1, line 1706 ^tata-ftp-21

- NSFR: có thể phát sinh chi phí bổ sung cần phản ánh vào FTP. Một số vị thế (như phái sinh) không cần tài trợ thường xuyên nhưng làm xấu NSFR và có thể buộc ngân hàng huy động thêm vốn dài hạn đắt hơn; vị thế ảnh hưởng NSFR nên bị phạt trên FTP curve.
  > "This may result in additional costs and will need to be reflected in funds transfer pricing."
  > "Some positions (e. g., derivatives positions) do not require regular funding (they are considered self-funded positions), but lead to a deterioration of a bank's NSFR."
  > "positions that impact the NSFR should be penalized on the funds transfer pricing curve"
  > — Chapter 2, §2.3.8.2, line 1710 ^tata-ftp-22

- Yêu cầu thanh toán bù trừ tập trung (clearing mandate) với phái sinh OTC chuẩn hoá và yêu cầu ký quỹ với phái sinh không bù trừ tập trung đều tạo thêm chi phí tài trợ do yêu cầu ký quỹ.
  > "Standardized over-the-counter (OTC) derivatives are required to be centrally cleared"
  > "which in turn results in additional funding costs due to the margin requirements set by the CCPs"
  > "regulatory margin requirements for non-centrally cleared transactions impose additional costs"
  > — Chapter 2, §2.3.8.3–2.3.8.4, lines 1714–1720 ^tata-ftp-23

- Tata so sánh FTP với funding value adjustment (FVA) trong định giá phái sinh: trong khung FTP, yếu tố credit value không đóng vai trò vì Treasury thường không nhận rủi ro tín dụng đối tác, vốn ở lại khối khách hàng; chi phí thanh khoản và vốn kinh tế được công nhận chậm như các cấu phần của FTP rate.
  > "In an FTP framework, credit value considerations do not play a role because the treasury department typically does not absorb the counterparty credit risk that remains with the customer business areas"
  > "while liquidity and economic capital costs have been slow to be recognized as components of the FTP rate"
  > — Chapter 2, §2.3.9, line 1730 ^tata-ftp-24

- FTP là quy trình nội bộ không bị các bên tham gia thị trường tích cực (như hedge fund) arbitrage nên chấp nhận được một mức thiếu chính xác nhất định; do đó Tata cho rằng kỹ thuật FVA có khả năng tiên tiến hơn mô hình FTP thông thường.
  > "FTP , on the other hand, is merely an internal process that cannot be arbitraged by aggressive market participants (such as hedge funds) and therefore can live with a certain lack of accuracy"
  > "it is reasonable to assume that FVA techniques are more advanced than typical FTP models"
  > — Chapter 2, §2.3.9, line 1728 ^tata-ftp-25

- Contingency liquidity gồm tiền mặt, tương đương tiền và HQLA không bị cầm cố giữ cho quản trị rủi ro thanh khoản và mục đích quy định. Chi phí contingency liquidity được cộng vào FTP rate, tương tự LVA; ví dụ giao dịch phát sinh chi phí này là hạn mức tín dụng cam kết cho khách hàng.
  > "Contingency liquidity consists of cash, cash equivalents, and unencumbered high quality liquid assets held for liquidity risk management and for regulatory purposes"
  > "Contingency liquidity costs are added to the FTP rate, similar to the LVA discussed in Sect. 2.3.9."
  > "An example of a bank customer transaction that gives rise to contingency liquidity costs is a committed line of credit to a customer."
  > — Chapter 2, §2.3.10.1, lines 1750–1754 ^tata-ftp-26

- FTP rate nên được điều chỉnh theo optionality: vị thế tạo short optionality thì điều chỉnh là mark-up, long optionality thì là discount. Ngân hàng 'short' optionality khi khách hàng có quyền đổi dòng tiền (ví dụ trả nợ trước hạn) và 'long' khi chính ngân hàng có quyền chọn (ví dụ phát hành trái phiếu có quyền mua lại).
  > "The FTP rate should be adjusted for optionality."
  > "Depending on whether a position creates a short or a long optionality, the adjustment to the FTP curve is a mark-up or a discount."
  > "The bank is 'short' optionality when the customer who has the right to change the cash flow of a transaction (e. g., the customer having the right to prepay a loan) and 'long' optionality when the bank that has a choice (e. g., after issuing a callable bond)."
  > — Chapter 2, §2.3.10.2, line 1758 ^tata-ftp-27

- Treasury có thể phải mua quyền chọn trên thị trường để bù short optionality và bán quyền chọn khi ngân hàng long optionality. Một phần optionality đến từ embedded options khó định lượng và/hoặc dựa trên giả định hành vi, nên không tính được giá trị bằng mô hình định giá quyền chọn chuẩn và/hoặc không phòng ngừa được bằng quyền chọn chuẩn trên thị trường.
  > "One can imagine the treasury department having to buy options in the market to offset short optionality, and being able to sell options in the market when the bank is long optionality."
  > "some of the optionality comes from so-called embedded options that are difficult to quantify"
  > "their value cannot be calculated with standard option pricing models and / or cannot be hedged with standard options traded in the financial market"
  > — Chapter 2, §2.3.10.2, line 1758 ^tata-ftp-28

- Nguyên tắc chung: chỉ rủi ro được chuyển cho Treasury quản lý mới nên được định giá trong khung FTP. Rủi ro tín dụng đối tác và rủi ro hoạt động thường không thuộc nhóm này vì khối khách hàng có khả năng nhận diện, định lượng và quản lý tốt hơn; nếu khối khách hàng không còn chịu tác động của sự kiện tín dụng và rủi ro hoạt động thì có nguy cơ phân bổ sai vốn do lựa chọn đối nghịch (adverse selection) và giám sát lỏng lẻo do rủi ro đạo đức (moral hazard).
  > "In general, only risks that are to be transferred to the treasury department for management should be priced in the FTP framework."
  > "Counterparty credit risk and operational risk are typically not considered such a risks because the client-facing customer area is much better equipped to identify, quantify and manage these risks."
  > "there is a potential for misallocation of the bank's funds due to adverse selection"
  > — Chapter 2, §2.3.10.3, line 1762 ^tata-ftp-29

- Nếu Treasury chào phòng ngừa rủi ro tín dụng đối tác, ví dụ bằng CDS, thì phí CDS có thể dùng làm add-on cho FTP curve.
  > "the treasury department may offer to hedge the counterparty credit risk, e. g. by entering into a credit default swaps (CDS), in which case the CDS premium could be used as an add-on to the FTP curve"
  > — Chapter 2, §2.3.10.3, line 1764 ^tata-ftp-30

- FTP là công cụ đo hiệu quả điều chỉnh theo rủi ro và lợi nhuận: phân bổ NIM theo cơ sở điều chỉnh rủi ro thúc đẩy thực hành khởi tạo và định giá lành mạnh, và gắn hoạt động của khối kinh doanh với khẩu vị rủi ro của ngân hàng. Phân bổ sai chi phí tài trợ có thể khuyến khích khối kinh doanh nhận rủi ro quá mức.
  > "FTP is a tool for measuring risk-adjusted performance and profitability"
  > "aligns business unit activities with the bank's overall risk appetite"
  > "Misallocating funding costs to business unit activities can incentivize a business unit to take excessive risk to improve its own performance metrics"
  > — Chapter 2, §2.3.11, lines 1768–1770 ^tata-ftp-31

- FTP cũng là công cụ tập trung quản lý các rủi ro, đặc biệt rủi ro lãi suất và thanh khoản, vào một đơn vị, cho cái nhìn rộng hơn về mọi vị thế và rủi ro để lập kế hoạch phòng ngừa và giảm thiểu tốt hơn.
  > "FTP is also a tool for centralizing the management of various risks"
  > "particularly interest rate and liquidity risk."
  > "provides a broader view of all exposures and their inherent risks for better hedging and mitigation planning"
  > — Chapter 2, §2.3.11, line 1772 ^tata-ftp-32

## Node bị ảnh hưởng
- u06 [2026-10-19]: tạo [[nii-planning]], [[negative-interest-rates]]; cập nhật [[funds-transfer-pricing]], [[model-validation]] (draft); đề xuất [[non-maturity-deposits]], [[behavioural-options]], [[net-interest-income-sensitivity]], [[option-risk]] (canonical).
- u07 [2026-10-19]: tạo [[silicon-valley-bank]]; cập nhật [[model-validation]]; đề xuất [[outlier-bank-test]], [[non-maturity-deposits]], [[behavioural-options]], [[duration-gap-model]] (canonical).
- u08 [2026-10-19]: đề xuất [[outlier-bank-test]], [[net-interest-income-sensitivity]], [[economic-value-of-equity]], [[non-maturity-deposits]], [[behavioural-options]] (canonical); cập nhật [[model-validation]], [[funds-transfer-pricing]] (draft).
- [[economic-value-of-equity]]
- [[net-interest-income-sensitivity]]
- [[duration-gap-model]]
- [[gap-risk]]
- [[irrbb-balance-sheet-portfolios]]
- [[repricing-balance-sheet]]
- [[behavioural-options]]
- [[non-maturity-deposits]]
- [[replicating-portfolio-model]]

## Mâu thuẫn ghi nhận
Không có.

## Ghi chú convert
Docling convert: heading chương bị gộp, chia unit theo dải 400 dòng; một số công thức toán chuyển thành `<!-- formula-not-decoded -->`.

