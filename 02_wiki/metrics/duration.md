---
title: "Duration"
aliases: [Duration, Macaulay Duration, Modified Duration, MD, Thời lượng, Thời lượng Macaulay, Thời lượng hiệu chỉnh]
type: metric
domains: [product, alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-fixed-income-markets]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: input-to, to: "[[pv01]]", cite: "[[src-choudhry-fixed-income-markets#^ch2-11]]"}
  - {type: input-to, to: "[[duration-gap-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u02-45]]"}
tags: [interest-rate-risk, duration, modified-duration, macaulay-duration, sensitivity, bond]
updated: 2026-10-22
reviewed:
---

## Định nghĩa
Duration (Macaulay duration) là thời gian bình quân nhận dòng tiền của một trái phiếu, có trọng số theo giá trị hiện tại của từng dòng tiền [[src-choudhry-fixed-income-markets#^ch2-2]]. Macaulay duration đo bằng năm [[src-choudhry-fixed-income-markets#^ch2-4]].

Modified duration (MD) đo tác động tương đối lên giá trái phiếu khi lợi suất thay đổi. Dấu âm phản ánh quan hệ ngược chiều giữa giá và lợi suất [[src-choudhry-fixed-income-markets#^ch2-9]]. Ý nghĩa chính của duration là thước đo biến động giá, tức rủi ro lãi suất, không phải thước đo kỳ hạn [[src-choudhry-fixed-income-markets#^ch2-8]].

## Công thức
*Diễn giải (tái dựng, chưa đối chiếu bản gốc):* công thức (2.1)–(2.13) của nguồn bị mất khi convert. Dựng lại từ lời văn: duration là bình quân thời gian nhận dòng tiền theo trọng số PV [[src-choudhry-fixed-income-markets#^ch2-2]]; phần trăm thay đổi giá xấp xỉ bằng MD nhân thay đổi lợi suất, ngược chiều [[src-choudhry-fixed-income-markets#^ch2-8]].

$$
D = \frac{1}{P}\sum_{n=1}^{N} n \cdot \frac{C_n}{(1+r)^n}
$$
  [[src-choudhry-fixed-income-markets#^ch2-2]]

$$
MD = \frac{D}{1+r}
$$
  [[src-choudhry-fixed-income-markets#^ch2-3]]

$$
\frac{\Delta P}{P} \approx -MD \cdot \Delta r
$$
  [[src-choudhry-fixed-income-markets#^ch2-8]]

$C_n$ là dòng tiền kỳ $n$, $r$ là lợi suất đáo hạn (trái phiếu trả coupon năm), $P$ là giá. Kiểm bằng ví dụ của nguồn:

| Ví dụ | Đầu vào | Kết quả tái dựng | Nguồn ghi | Nguồn |
|---|---|---|---|---|
| 2.1, trái phiếu 8% 10 năm | Σ n×PV 746,540686; P 102,49696; r 7,634% | D = 7,2835; MD = 6,7670 | MD = 7,28354 / 1,07634 = 6,76695 | [[src-choudhry-fixed-income-markets#^ch2-3]] |
| 2.3, trái phiếu 8% ngang giá | D 2,74; r 8%; Δr +0,50% | MD = 2,537; P = 100 − 2,537 × 0,5 = 98,7315 | MD 2,537; giá £98,7315 | [[src-choudhry-fixed-income-markets#^ch2-10]] |
| 2.3, MD 3,99 | Δr 1% | %ΔP = −3,99% | giá đổi ngược chiều 3,99% | [[src-choudhry-fixed-income-markets#^ch2-10]] |

## Diễn giải
**Tính chất của Macaulay duration** (trái phiếu thông thường):

| Tính chất | Nguồn |
|---|---|
| Duration luôn nhỏ hơn kỳ hạn; zero-coupon có duration bằng kỳ hạn | [[src-choudhry-fixed-income-markets#^ch2-5]] |
| Duration cao hơn khi coupon thấp hơn, lợi suất thấp hơn, nhìn chung kỳ hạn dài hơn | [[src-choudhry-fixed-income-markets#^ch2-5]] |
| Tăng tần suất trả coupon làm duration ngắn lại | [[src-choudhry-fixed-income-markets#^ch2-6]] |
| Duration danh mục là bình quân duration từng trái phiếu, trọng số là PV trên giá đầy đủ của danh mục (market-weighted duration) | [[src-choudhry-fixed-income-markets#^ch2-7]] |

Dưới dạng modified duration, đây từng là thước đo rủi ro lãi suất chính trên thị trường và vẫn được dùng cùng value-at-risk [[src-choudhry-fixed-income-markets#^ch2-4]]. Thước đo thường dùng ngày nay là thước đo theo từng basis point, xem [[pv01]] [[src-choudhry-fixed-income-markets#^ch2-1]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Duration là chỉ tiêu bắt buộc | Không ghi nhận trong nguồn đã ingest; chỉ tiêu IRRBB chuẩn hoá là ΔEVE và ΔNII ([[economic-value-of-equity]], [[net-interest-income-sensitivity]]) [cần nguồn] | Phần TT83/2025 đã ingest không quy định duration [cần nguồn] | — | — |

## Ứng dụng trong ALM
- Duration bình quân của tài sản ($D_A$) và nợ ($D_L$), cùng trọng số $w = L/A$, là đầu vào của duration gap; DGAP dùng để theo dõi giá trị vốn khi đường lãi suất biến động [[src-lubinska-alm-optimisation#^lubinska-u02-45]]. Xem [[duration-gap-model]].
- BPV của một vị thế tính từ MD và giá; hedge bằng BPV dùng hedge ratio có yield beta [[src-choudhry-fixed-income-markets#^ch2-11]] [[src-choudhry-fixed-income-markets#^ch2-12]]. Xem [[pv01]].
- *Diễn giải:* market-weighted duration của danh mục [[src-choudhry-fixed-income-markets#^ch2-7]] là cách ghép duration từng khoản mục thành $D_A$, $D_L$ của bảng cân đối. Với danh mục HQLA trái phiếu chính phủ, duration cho biết mức giảm giá trị thị trường khi lãi suất tăng; chưa có nguồn về trần duration HQLA trong wiki.

## Nhầm lẫn thường gặp
- **Coi duration là kỳ hạn.** Nguồn nói cách hiểu này bỏ qua ý chính: duration là thước đo biến động giá [[src-choudhry-fixed-income-markets#^ch2-8]].
- **Dùng MD cho sốc lớn.** MD chỉ là xấp xỉ, càng kém chính xác khi lợi suất biến động lớn [[src-choudhry-fixed-income-markets#^ch2-9]]. Với 1 bp, xấp xỉ là hợp lý; với 200 bp, sai đáng kể. MD đánh giá thấp mức tăng giá khi lợi suất giảm, và đánh giá cao mức giảm giá khi lợi suất tăng [[src-choudhry-fixed-income-markets#^ch2-14]]. Phần sai số này đo bằng [[convexity]].
- *Diễn giải:* công thức trên giả định dòng tiền cố định. Khoản mục có quyền chọn nhúng (trả nợ trước hạn, rút tiền gửi sớm) cần duration theo mô hình hành vi; xem [[behavioural-options]]. Effective duration chưa có nguồn trong wiki [cần nguồn].
