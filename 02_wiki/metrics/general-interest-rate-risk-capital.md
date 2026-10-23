---
title: "General Interest Rate Risk Capital"
aliases: [General Interest Rate Risk Capital, K_IRR^GMR, Vốn yêu cầu cho rủi ro lãi suất chung]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[interest-rate-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^pl4-i-4b]]"}
tags: [capital, market-risk, interest-rate, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho rủi ro lãi suất chung ($K_{IRR}^{GMR}$) là vốn cho rủi ro phát sinh từ thay đổi lãi suất trên thị trường [[src-tt14-2025-nhnn#^pl4-i-2a]]. $K_{IRR}^{GMR}$ là tổng các giá trị tuyệt đối của vốn rủi ro lãi suất chung tính riêng cho từng loại đồng tiền, xác định bằng phương pháp thang kỳ hạn [[src-tt14-2025-nhnn#^pl4-i-4b]]. Là thành phần của [[interest-rate-risk-capital-requirement]].

## Công thức
$$
K_{IRR}^{GMR} = NWP + VD + HD
$$
[[src-tt14-2025-nhnn#^pl4-i-4b]]

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| NWP | Vốn bù đắp rủi ro do lệch trạng thái trên sổ kinh doanh | [[net-weighted-position]] | [[src-tt14-2025-nhnn#^pl4-i-4b]] |
| VD | Vốn bù đắp rủi ro do khớp trạng thái trong cùng thang kỳ hạn (vertical disallowance) | [[vertical-disallowance]] | [[src-tt14-2025-nhnn#^pl4-i-4b]] |
| HD | Vốn bù đắp rủi ro do khớp trạng thái trong cùng một vùng hoặc giữa các vùng (horizontal disallowance) | [[horizontal-disallowance]] | [[src-tt14-2025-nhnn#^pl4-i-4b]] |

## Diễn giải
Các bước tính (thang kỳ hạn, vùng, hệ số rủi ro) nằm ở [[maturity-ladder-method]]. Công thức cho một đồng tiền; kết quả của các đồng tiền được cộng bằng giá trị tuyệt đối [[src-tt14-2025-nhnn#^pl4-i-4b]].

**Ví dụ của nguồn.** Danh mục gồm trái phiếu Nhóm 2 (13,33 tỷ đồng, 8 năm, coupon 8%), trái phiếu Chính phủ (75 tỷ đồng, 2 tháng), hoán đổi lãi suất nhận thả nổi trả cố định (150 tỷ đồng, kỳ định lại lãi suất sau 9 tháng, còn lại 8 năm) và trạng thái dương hợp đồng tương lai lãi suất 50 tỷ đồng (6 tháng, tài sản gốc trái phiếu Chính phủ 3,5 năm) [[src-tt14-2025-nhnn#^pl4-i-vd1]]:

| Cấu phần | Giá trị (tỷ đồng) | Nguồn |
|---|---|---|
| NWP | 3 | [[src-tt14-2025-nhnn#^pl4-i-vd2]] |
| VD (thang 7 đến 10 năm) | 0,05 | [[src-tt14-2025-nhnn#^pl4-i-vd3]] |
| Khớp trong vùng 1 | 0,08 | [[src-tt14-2025-nhnn#^pl4-i-vd3]] |
| Khớp giữa vùng 2 và 3 | 0,45 | [[src-tt14-2025-nhnn#^pl4-i-vd4]] |
| Khớp giữa vùng 1 và 3 | 1 | [[src-tt14-2025-nhnn#^pl4-i-vd4]] |
| Tổng | 4,58 | [[src-tt14-2025-nhnn#^pl4-i-vd5]] |

*Diễn giải:* wiki kiểm lại phép tính: 3 + 0,05 + 0,08 + 0,45 + 1 = 4,58. Tổng khớp nguồn. Cộng bốn dòng cuối là HD = 0,08 + 0,45 + 1 = 1,53 tỷ đồng, nên $K_{IRR}^{GMR}$ = 3 + 0,05 + 1,53 = 4,58 tỷ đồng.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức | [cần nguồn] (MAR chưa ingest) | NWP + VD + HD [[src-tt14-2025-nhnn#^pl4-i-4b]] | PL4.B.I.4b | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Cộng theo đồng tiền | [cần nguồn] | Tổng giá trị tuyệt đối từng đồng tiền [[src-tt14-2025-nhnn#^pl4-i-4b]] | PL4.B.I.4a | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* $K_{IRR}^{GMR}$ phụ thuộc trạng thái ròng theo thang kỳ hạn chứ không theo kỳ hạn bình quân. Treasury có thể hạ NWP bằng cách cân bằng trạng thái dương và âm toàn sổ, nhưng phần khớp trong cùng thang và cùng vùng vẫn tốn VD và HD. Lệch kỳ hạn giữa các vùng tốn nhiều nhất khi khớp vùng 1 với vùng 3 (100%).

## Nhầm lẫn thường gặp
- NWP là giá trị tuyệt đối của hiệu hai tổng, không phải tổng các trạng thái ròng [[src-tt14-2025-nhnn#^pl4-i-4c35]].
- Đ74 gọi thành phần này là "GR", Phụ lục IV gọi là "GMR" [[src-tt14-2025-nhnn#^d74-2]].
