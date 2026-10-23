---
title: "Vertical Disallowance"
aliases: [Vertical Disallowance, VD, Vốn bù đắp rủi ro khớp trạng thái trong cùng thang kỳ hạn]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[general-interest-rate-risk-capital]]", cite: "[[src-tt14-2025-nhnn#^pl4-i-4b]]"}
tags: [capital, market-risk, interest-rate, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vertical disallowance (VD) là vốn yêu cầu để bù đắp rủi ro do khớp trạng thái trong cùng thang kỳ hạn, thành phần của [[general-interest-rate-risk-capital]] [[src-tt14-2025-nhnn#^pl4-i-4b]].

## Công thức
$$
VD = 10\% \times (a)
$$
[[src-tt14-2025-nhnn#^pl4-i-4c6]]

(a) là tổng trạng thái tương ứng điều chỉnh theo hệ số rủi ro của các thang kỳ hạn. Trạng thái tương ứng của một thang là giá trị tuyệt đối nhỏ hơn giữa trạng thái dương điều chỉnh và trạng thái âm điều chỉnh của thang đó; chỉ xét thang có cả hai trạng thái [[src-tt14-2025-nhnn#^pl4-i-4c6]]. Ký hiệu (a) theo bảng thang kỳ hạn của nguồn ([[maturity-ladder-method]]).

## Diễn giải
Ví dụ của nguồn: thang 7 đến 10 năm có trạng thái dương điều chỉnh 0,5 và trạng thái âm điều chỉnh −5,625; trạng thái tương ứng là 0,5; VD = 0,5 × 10% = 0,05 tỷ đồng [[src-tt14-2025-nhnn#^pl4-i-vd3]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Hệ số VD | [cần nguồn] (MAR chưa ingest) | 10% [[src-tt14-2025-nhnn#^pl4-i-4c6]] | PL4.B.I.4c bước 6 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |

## Ứng dụng trong ALM
*Diễn giải:* VD phạt việc giữ đồng thời trạng thái dương và âm trong cùng thang kỳ hạn, vì phòng ngừa giữa hai công cụ khác nhau không triệt tiêu hoàn toàn rủi ro cơ sở. Hệ số 10% trên phần khớp.

## Nhầm lẫn thường gặp
- VD tính trên phần khớp của từng thang, không trên toàn bộ trạng thái [[src-tt14-2025-nhnn#^pl4-i-4c6]].
