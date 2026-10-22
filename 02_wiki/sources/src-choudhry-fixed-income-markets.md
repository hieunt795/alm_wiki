---
title: "Fixed Income Markets — Moorad Choudhry"
aliases: []
type: source
source_id: src-choudhry-fixed-income-markets
domains: [product, macro]
status: active
maturity: draft
tier: T4
doc_status: final
issuer: Moorad Choudhry
published:
effective:
raw: 01_sources/choudhry_banking_fixed_income/Choudhry_Fixed_Income_Markets.md
units_done: [ch2]
updated: 2026-10-22
---

## Thông tin nguồn
- Issuer: Moorad Choudhry.
- Tier / doc_status: T4 / final (sách phương pháp thị trường trái phiếu).
- Ban hành / hiệu lực: không áp dụng.
- Raw: `01_sources/choudhry_banking_fixed_income/Choudhry_Fixed_Income_Markets.md` (15.415 dòng).
- Conversion: partial (xem `03_meta/sources.yaml`). Ch2 mất toàn bộ công thức; xem "Ghi chú convert".
- Units covered:
  - `ch2`: Bond Instruments and Interest-Rate Risk — duration, modified duration, basis-point value, convexity (dòng 1077–1628).

## Tóm tắt
- Ch2 trình bày thước đo độ nhạy giá trái phiếu theo lợi suất theo cách tiếp cận truyền thống.
- Macaulay duration là thời gian bình quân nhận dòng tiền có trọng số theo PV; modified duration đo độ nhạy giá.
- Basis-point value (BPV) là thay đổi giá khi lợi suất đổi 1 bp, dùng để tính hedge ratio.
- Convexity là thước đo bậc hai, đo sai số của xấp xỉ modified duration khi lợi suất biến động lớn.
- Các ví dụ số dùng trái phiếu giả định (8% 2019, 5% 2009); công thức trong raw bị mất khi convert.

## Key claims

### ch2 — Bond Instruments and Interest-Rate Risk

- Ngày nay khi nói "duration" hay modified duration, thước đo rủi ro lãi suất thường được dùng là thước đo theo từng basis point.
  > "for present-day purposes when one speaks of 'duration' or modifi ed duration the interest risk exposure measure used is generally a per basis point measure."
  > — ch2 (mở đầu) ^ch2-1

- Duration là thời gian bình quân nhận dòng tiền của trái phiếu, có trọng số theo giá trị hiện tại của từng dòng tiền; còn gọi là Macaulay duration.
  > "a more accurate measure would be to take the average time to receipt of a bond's cash fl ows, but weighted in the form of the cash fl ows' present value. This is, in effect, duration."
  > — ch2 §Duration, modified duration, and convexity ^ch2-2

- Ví dụ 2.1: trái phiếu coupon 8% hằng năm, 10 năm, giá 102,497, lợi suất 7,634%; tổng PV 102,49696, tổng n × PV 746,540686; modified duration = 7,28354 / 1,07634 = 6,76695.
  > "Calculating the Macaulay duration for the 8% 2019 annual coupon bond:"
  > "Modifi ed Duration = 7.28354/1.07634 = 6.76695"
  > — ch2 Example 2.1, Table 2.1 ^ch2-3

  | Period (n) | Cash Flow | PV at Current Yield | n × PV |
  |---|---|---|---|
  | 1 | 8 | 7.43260 | 7.4326 |
  | 5 | 8 | 5.53787 | 27.68935 |
  | 10 | 108 | 51.75222 | 517.5222 |
  | Total | | 102.49696 | 746.540686 |

  (Chép rút gọn: Table 2.1 trong raw có đủ 10 kỳ.)

- Macaulay duration đo bằng năm; dưới dạng modified duration, đây từng là thước đo rủi ro lãi suất chính trên thị trường và vẫn được dùng rộng rãi cùng value-at-risk cho rủi ro thị trường.
  > "The Macaulay duration value given by (2.6) is measured in years."
  > "as a risk measure and hedge calculation measure, duration transformed into modifi ed duration was the primary measure of interest-rate risk used in the markets, and is still widely used alongside the value-at-risk measure for market risk."
  > — ch2 §Duration ^ch2-4

- Duration luôn nhỏ hơn kỳ hạn; với zero-coupon, duration bằng kỳ hạn. Duration cao hơn khi coupon thấp hơn, lợi suất thấp hơn, và nhìn chung kỳ hạn dài hơn.
  > "A bond's duration is always less than its maturity."
  > "duration for a zero coupon bond is equal to its term to maturity. Duration varies with coupon, yield, and maturity. The following three factors imply higher duration for a bond:"
  > "The lower the coupon,"
  > "The lower the yield,"
  > "Broadly, the longer the maturity."
  > — ch2 §Properties of Macaulay duration ^ch2-5

- Tăng tần suất trả coupon làm duration ngắn lại; giảm tần suất làm duration dài ra.
  > "Thus, increasing the coupon frequency shortens duration and, of course, decreasing coupon frequency has the effect of lengthening duration."
  > — ch2 §Properties of Macaulay duration ^ch2-6

- Duration danh mục là bình quân có trọng số duration từng trái phiếu, trọng số là PV của trái phiếu chia giá đầy đủ của danh mục (market-weighted duration).
  > "Portfolio duration is a weighted average of the duration of the individual bonds. The weights are the present values of the bonds divided by the full price of the entire portfolio, and the resulting duration calculation is often referred to as a market-weighted duration."
  > — ch2 §Properties of Macaulay duration ^ch2-7

- Ý nghĩa chính của duration là thước đo biến động giá (rủi ro lãi suất), không phải kỳ hạn; phần trăm thay đổi giá xấp xỉ bằng modified duration nhân thay đổi lợi suất, và thay đổi lợi suất nhỏ gây thay đổi giá ngược chiều.
  > "such an interpretation is to miss the main point of duration, which is a measure of price volatility or interest-rate risk."
  > "Equation (2.13) expresses the approximate percentage change in price as being equal to the modifi ed duration multiplied by the change in yield."
  > "for small changes in yield, a given change in yield results in an inverse change in bond price."
  > — ch2 §Modified duration ^ch2-8

- Modified duration đo tác động tương đối lên giá khi lợi suất đổi; dấu âm do giá và lợi suất ngược chiều; đây chỉ là xấp xỉ và càng kém chính xác khi lợi suất biến động lớn.
  > "Thus, modifi ed duration measures the proportionate impact on the price of a bond resulting from a change in its yield. The sign in (A2.1.5) is negative because of the inverse relationship between bond prices and yields"
  > "this is an approximation only and is progressively more inaccurate for greater changes in yield."
  > — ch2 Appendix 2.1 ^ch2-9

- Ví dụ 2.3: trái phiếu coupon 8% giao dịch ngang giá, duration 2,74 năm, MD 2,537; lợi suất tăng từ 8% lên 8,50% thì giá còn £98,7315. Trái phiếu MD 3,99: lợi suất đổi 1% thì giá đổi ngược chiều 3,99%.
  > "An 8% annual coupon bond is trading at par with a duration of 2.74 years. If yields rise from 8% to 8.50%, then the price of the bond will fall by:"
  > "That is, the price of the bond will now be £98.7315."
  > "which gives us MD equal to 2.537 years."
  > "This tells us that for a 1% move in the yield to maturity, the price of the bond will move (in the opposite direction) by 3.99%."
  > — ch2 Example 2.3 ^ch2-10

- Basis-point value (BPV) là thay đổi giá trái phiếu khi lợi suất đổi 1 bp; trái phiếu MD 3,99 ngang giá có BPV 3,99 cents.
  > "For a bond with a modifi ed duration of 3.99, priced at par, an increase in yield of 1 basis point (100 basis = 1%) leads to a fall in the bond's price of:"
  > "In this case, 3.99 cents is the basis-point value of the bond, which is the change in the bond price given a one-basis-point change in the bond's yield."
  > — ch2 §Modified duration, (2.18) ^ch2-11

- BPV dùng để hedge: mục tiêu là thay đổi giá của vị thế gốc bằng thay đổi giá của công cụ hedge; hedge ratio dùng để tính quy mô vị thế hedge, tỷ số thứ hai trong công thức là yield beta.
  > "Basis-point values (BPVs) are used in hedging."
  > "The objective of a hedge is to ensure that the price change in the primary instrument is equal to the price change in the hedging instrument."
  > "The hedge ratio is used to calculate the size of the hedge position and is given in (2.20)."
  > "The second ratio in (2.20) is known as the yield beta."
  > — ch2 §Modified duration, (2.19)–(2.20) ^ch2-12

- Ví dụ 2.4: vị thế long £1 triệu trái phiếu 8% 2019 (MD 11,14692, giá 129,87596, BPV 0,14477) hedge bằng zero-coupon BPV 0,05549, yield beta 1: bán £2.608.940 zero-coupon.
  > "A trader holds a long position of £1 million of the 8% 2019 bond. The modifi ed duration of the bond is 11.14692, and its price is 129.87596. The basispoint value of this bond is therefore 0.14477."
  > "hedge the position using the 0% 2009 bond, which has a BPV of 0.05549."
  > "Therefore, to hedge £1 million of the 20-year bond, the trader shorts £2,608,940 of the zero-coupon bond."
  > — ch2 Example 2.4 ^ch2-13

- Ví dụ 2.5: với thay đổi 1 bp, xấp xỉ từ duration là ước lượng hợp lý; với thay đổi lớn (200 bp) thì sai đáng kể. Xấp xỉ modified duration đánh giá thấp mức tăng giá khi lợi suất giảm và đánh giá cao mức giảm giá khi lợi suất tăng.
  > "for a one-basis-point change in yield, the change in price given by the dollar duration fi gure, while not completely accurate, is a reasonable estimation of the actual change in price. For a large move, however, say 200 basis points, the approximation is signifi cantly in error, and analysts would not use it."
  > "underestimates the change in price resulting from a fall in yields but overestimates the price change for a rise in yields."
  > — ch2 Example 2.5, Table 2.2 ^ch2-14

  | Yield Change | Price Change | Estimate using Price Duration |
  |---|---|---|
  | down 1 bp | 0.06713 | 0.06936 |
  | up 1 bp | 0.06707 | 0.06936 |

- Convexity là thước đo rủi ro lãi suất bậc hai, đo độ cong của đường giá/lợi suất và sai số khi dùng modified duration; convexity đồng biến với độ phân tán dòng tiền và với duration.
  > "Convexity is a second-order measure of interest-rate risk; it measures the curvature of the present value/yield profi le. Convexity can be regarded as an indication of the error one makes when using modifi ed duration"
  > "The convexity of a bond is positively related to the dispersion of its cash fl ows"
  > "Convexity is also positively related to duration."
  > — ch2 §Convexity ^ch2-15

- Convexity adjustment nhân convexity với một nửa vì số hạng thứ hai của khai triển Taylor có hệ số 1/2; giá trị convexity theo các công thức này luôn dương, nên thay đổi giá do convexity dương cả khi lợi suất tăng lẫn giảm.
  > "The reason we multiply the convexity by half to obtain the convexity adjustment is because the second term in the Taylor expansion contains the coeffi cient"
  > "Note that the value for convexity given by the expressions above will always be positive; that is, the approximate price change due to convexity is positive for both yield increases and decreases."
  > — ch2 §Convexity, (2.25) ^ch2-16

- Ví dụ 2.7A: trái phiếu 5% ngang giá, MD 2,639, convexity 9,57; lợi suất tăng từ 5% lên 7% thì giá còn 94,9134; xấp xỉ bậc một bằng modified duration cho mức giảm giá 5,278 (giá trên mệnh giá 100), đánh giá cao mức giảm thực tế 0,1914.
  > "A 5% annual coupon bond is trading at par with a modifi ed duration of 2.639 and convexity of 9.57. If we assume a signifi cant market correction and yields rise from 5% to 7%, the price of the bond will fall by:"
  > "to \$94.9134. The fi rst-order approximation, using the modifi ed-duration value of 2.639, is -\$5.278, which is an overestimation of the fall in price by \$0.1914."
  > — ch2 Example 2.7(A) ^ch2-17

- Ví dụ 2.7B: trái phiếu 5% 2009 giá £96,23119 (lợi suất 5,50%), 10 năm, CV = 100, MD 7,64498. Lợi suất tăng 200 bp lên 7,50%: giá thực tế £82,83980 (−13,92%); convexity effect 1,92462%; MD cộng convexity cho −13,36534%.
  > "The 5% 2009 bond is trading at a price of £96.23119 (a yield of 5.50%) and has precisely 10 years to maturity, and its convexity parameter CV equals 100. If the yield rises to 7.50%, a change of 200 basis points, the percentage price change due to the convexity effect is given by:"
  > "7.50%, we see that it is £82.83980, a change in price of 13.92%. The convexity measure of 1.92462% is an approximation of the error we would make when using the modifi ed-duration value to estimate the price of the bond following the 200-basis-point rise in yield."
  > "its modifi ed duration is 7.64498."
  > "This gives us a net percentage price change of 13.36534. As we saw in Example 2.7B, the actual percentage price change is 13.92%."
  > — ch2 Example 2.7(B) ^ch2-18

- Cùng trái phiếu, lợi suất giảm 150 bp: MD cộng convexity cho +12,55007%, thực tế +10,98843%, nên MD đơn lẻ gần hơn; convexity chỉ hiệu quả với thay đổi lợi suất lớn.
  > "This gives us a percentage price change of 12.55007. The actual price change was 10.98843%, so here the modifi ed duration estimate is actually closer! This illustrates that the convexity measure is effective for larger yield changes only."
  > — ch2 Example 2.7 (tiếp) ^ch2-19

- Ví dụ 2.8: lợi suất tăng 300 bp lên 8,50%: ước lượng MD cộng convexity −18,60454%, thực tế −19,9477%, vẫn gần hơn MD đơn lẻ; sai số còn lại vì convexity cũng thay đổi theo lợi suất.
  > "This gives a percentage price change of 18.60454%. The actual percentage price change was 19.9477%, but our estimate is still closer than that obtained using only the modifi ed-duration measure. The continuing error refl ects the fact that convexity is also a dynamic measure and changes with yield changes"
  > — ch2 Example 2.8 ^ch2-20

- Convexity tăng theo bình phương kỳ hạn, giảm khi coupon và lợi suất tăng; lợi suất giảm làm convexity tăng (tính chất của convexity dương).
  > "The convexity measure increases with the square of maturity, and it decreases with both coupon and yield."
  > "A decrease in bond yield leads to an increase in the bond's convexity; this is a property of positive convexity."
  > — ch2 §Convexity properties ^ch2-21

- Trái phiếu vanilla thông thường gần như luôn có convexity dương; convexity âm (đường giá/lợi suất lõm) không hấp dẫn với người nắm giữ, phổ biến nhất ở callable bond.
  > "For a conventional vanilla bond, convexity is almost always positive. Negative convexity resulting from a bond with a concave price/yield profi le would not be an attractive property for a bondholder. The most common occurrence of negative convexity in the cash markets is with callable bonds."
  > — ch2 §Convexity properties ^ch2-22

## Node bị ảnh hưởng
- ch2: [[duration]] (tạo mới), [[convexity]] (tạo mới), [[pv01]], [[duration-gap-model]].

## Mâu thuẫn ghi nhận
- Không có mâu thuẫn với nguồn khác. Trong nội bộ ch2, Ví dụ 2.7B ghi CV = 100 nhưng convexity effect 1,92462% ứng với ½ × CV × (Δr)² khi CV khoảng 96,23 (xem [[convexity]]).

## Ghi chú convert
- Ch2 (dòng 1077–1628): mọi công thức (2.1)–(2.25) và Appendix A2.1–A2.3 là `<!-- formula-not-decoded -->`. Dòng 1380, 1384, 1440, 1456 công thức vỡ thành chuỗi số. Không trích công thức; node dựng lại từ lời văn dưới nhãn tái dựng.
- Ligature "fi", "fl" bị tách bằng khoảng trắng ("fi  rst", "modifi  ed", "cash fl  ows"). Trích dẫn giữ nguyên chữ bị tách để khớp raw.
- Example 2.1 ghi "8% 2019" ở tiêu đề nhưng Table 2.1 ghi "8% 2009 Bond".
