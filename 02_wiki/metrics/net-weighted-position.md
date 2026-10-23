---
title: "Net Weighted Position"
aliases: [Net Weighted Position, NWP, Vốn bù đắp rủi ro lệch trạng thái]
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
NWP là vốn yêu cầu để bù đắp rủi ro do lệch trạng thái trên sổ kinh doanh, thành phần của [[general-interest-rate-risk-capital]] [[src-tt14-2025-nhnn#^pl4-i-4b]]. NWP bằng giá trị tuyệt đối của hiệu giữa tổng trạng thái dương điều chỉnh theo hệ số rủi ro của các thang kỳ hạn (L) và tổng trạng thái âm điều chỉnh (S) [[src-tt14-2025-nhnn#^pl4-i-4c35]].

## Công thức
$$
NWP = \left| L - S \right|
$$
[[src-tt14-2025-nhnn#^pl4-i-4c35]]

L và S lấy từ cột "trạng thái điều chỉnh theo hệ số rủi ro" của bảng thang kỳ hạn; trạng thái điều chỉnh bằng trạng thái ròng dương (âm) nhân hệ số rủi ro của thang ([[maturity-ladder-method]]) [[src-tt14-2025-nhnn#^pl4-i-4c35]].

## Diễn giải
Ví dụ của nguồn: NWP = |(75 × 0,2%) − (50 × 0,4%) + (150 × 0,7%) + (50 × 2,25%) − (150 × 3,75%) + (13,33 × 3,75%)| = |0,15 − 0,2 + 1,05 + 1,125 − 5,625 + 0,5| = 3 tỷ đồng [[src-tt14-2025-nhnn#^pl4-i-vd2]].

*Diễn giải:* kiểm lại: 0,15 − 0,2 = −0,05; +1,05 = 1,0; +1,125 = 2,125; −5,625 = −3,5; +0,5 = −3,0. Giá trị tuyệt đối 3. Khớp nguồn. Trong ví dụ, tổng dương L = 2,825, tổng âm S = 5,825 (0,2 + 5,625).

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức | [cần nguồn] (MAR chưa ingest) | $\lvert L - S \rvert$ [[src-tt14-2025-nhnn#^pl4-i-4c35]] | PL4.B.I.4c bước 5 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |

## Ứng dụng trong ALM
*Diễn giải:* NWP chịu hệ số rủi ro của thang kỳ hạn, nên một trạng thái ngắn hạn ròng (hệ số 0,00% đến 0,70%) tốn ít vốn hơn một trạng thái dài hạn (3,75% trở lên) cùng quy mô. Ví dụ trên cho thấy hoán đổi 8 năm nhận thả nổi trả cố định tạo trạng thái âm 5,625 ở thang 7 đến 10 năm, chiếm phần lớn NWP.

## Nhầm lẫn thường gặp
- NWP dùng trạng thái đã nhân hệ số rủi ro, không dùng trạng thái ròng gốc [[src-tt14-2025-nhnn#^pl4-i-4c35]].
