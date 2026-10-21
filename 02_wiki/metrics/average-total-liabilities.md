---
title: "Average Monthly Total Liabilities"
aliases: [Average Monthly Total Liabilities, Tổng Nợ phải trả bình quân của tháng, Mẫu số tỷ lệ nắm giữ TPCP]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2026-10-01
valid_to:
as_of:
sources: ["[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[government-bond-holding-ratio]]", cite: "[[src-tt50-2026-nhnn#^d28-1]]"}
tags: [balance-sheet, vn-regulation]
updated: 2026-10-21
reviewed:
---

## Định nghĩa
Average Monthly Total Liabilities (Tổng Nợ phải trả bình quân của tháng) là tổng số dư khoản mục Tổng Nợ phải trả trên cân đối tài khoản kế toán cuối mỗi ngày trong tháng chia cho tổng số ngày trong tháng [[src-tt50-2026-nhnn#^d3-13]]. Giá trị của tháng liền kề trước là mẫu số của [[government-bond-holding-ratio]] [[src-tt50-2026-nhnn#^d28-1]].

## Công thức
$$\overline{TL}_m = \frac{1}{N_m} \sum_{d=1}^{N_m} TL_d$$
[[src-tt50-2026-nhnn#^d3-13]]

$TL_d$ là số dư Tổng Nợ phải trả cuối ngày $d$ trên cân đối tài khoản kế toán, $N_m$ là tổng số ngày trong tháng $m$.

## Diễn giải
- *Diễn giải:* $N_m$ là tổng số ngày trong tháng, không phải số ngày làm việc. Ngày nghỉ vẫn có số dư cuối ngày, thường bằng số dư ngày làm việc liền trước.
- *Diễn giải:* bình quân ngày làm giảm tác động của biến động cuối tháng. Ngân hàng không nâng được mẫu số bằng cách tăng huy động vào ngày cuối tháng.
- *Diễn giải:* điều kiện ngân hàng mới thành lập ở Đ28.5 so sánh "Tổng Nợ phải trả" với vốn điều lệ, vốn được cấp, không dùng bình quân [[src-tt50-2026-nhnn#^d28-5]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Chỉ tiêu tương ứng | Không có trong chuẩn BCBS đã ingest [cần nguồn] | Bình quân số dư cuối ngày của Tổng Nợ phải trả trong tháng [[src-tt50-2026-nhnn#^d3-13]] | TT50 Đ3.13 | 01/10/2026 [[src-tt50-2026-nhnn#^d37-1]] |

## Ứng dụng trong ALM
- *Diễn giải:* ví dụ tháng 30 ngày: 20 ngày số dư 100.000 tỷ, 10 ngày 106.000 tỷ, bình quân 102.000 tỷ. Trần TPCP tháng sau là 30.600 tỷ. Dự báo tăng trưởng nợ phải trả theo ngày giúp ALCO biết trước dư địa mua TPCP.

## Nhầm lẫn thường gặp
- *Diễn giải:* không dùng số dư cuối tháng thay cho bình quân ngày. Hai số khác nhau khi bảng cân đối tăng, giảm trong tháng.
