---
title: "Specific Provision"
aliases: [Specific Provision, SP, Dự phòng cụ thể]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[customer-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^d8-2-vars]]"}
tags: [capital, credit-risk, provisioning, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Dự phòng cụ thể ($SP_i$) là dự phòng của từng khoản phải đòi thứ i [[src-tt14-2025-nhnn#^d8-2-vars]]. TT14/2025 dùng $SP_i$ làm đại lượng trừ trong công thức $RWA_{CR}$ [[src-tt14-2025-nhnn#^d8-2]]. Định nghĩa chi tiết và cách trích lập không nằm trong C2-M1 [cần nguồn].

## Công thức
$$
\max\{0;\ E_i^{*} - SP_i\}
$$
[[src-tt14-2025-nhnn#^d8-2]]

Biểu thức trên là phần trong dấu ngoặc của công thức $RWA_{CR}$: số dư sau giảm thiểu trừ dự phòng cụ thể, sàn 0, rồi nhân $CRW_i$ [[src-tt14-2025-nhnn#^d8-2]]. Xem [[customer-credit-risk-rwa]] và [[exposure-value]].

## Diễn giải
*Diễn giải:* $SP_i$ khác dự phòng chung. Theo Phụ lục I, dự phòng chung là cấu phần của vốn cấp 2 với trần 1,25% ([[tier-2-capital]]). Hai loại dự phòng đi vào CAR ở hai chỗ khác nhau: dự phòng cụ thể làm giảm RWA, dự phòng chung làm tăng vốn tự có [[src-tt14-2025-nhnn#^d8-2]] [[src-tt14-2025-nhnn#^pl1-b2-cap]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Vai trò trong công thức RWA | [cần nguồn] (CRE chưa ingest) | Trừ khỏi $E_i^{*}$, sàn 0 [[src-tt14-2025-nhnn#^d8-2]] | Đ8.2 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Định nghĩa dự phòng cụ thể | [cần nguồn] | [cần nguồn] (ngoài C2-M1) | | |

## Ứng dụng trong ALM
*Diễn giải:* chi phí trích lập dự phòng cụ thể vừa ghi vào kết quả kinh doanh vừa giảm RWA của khoản đó. Mô hình [[expected-credit-loss]] (IFRS 9) là khuôn khổ kế toán khác; mối liên hệ với dự phòng cụ thể của TT14/2025 cần nguồn riêng [cần nguồn].

## Nhầm lẫn thường gặp
- $SP_i$ trừ vào số dư của chính khoản i, không phải trừ vào tổng RWA [[src-tt14-2025-nhnn#^d8-2]].
