---
title: "Potential Future Exposure"
aliases: [Potential Future Exposure, PFE, Giá trị tương lai trạng thái rủi ro]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[counterparty-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^pl2-4b]]"}
tags: [capital, counterparty-risk, derivatives, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Giá trị tương lai trạng thái rủi ro ($PFE_j$) của giao dịch phái sinh j xác định trên cơ sở tổng giá trị vốn danh nghĩa (theo pháp luật về hạch toán kế toán) nhân với chỉ số tăng thêm (add-on factor) theo thời hạn còn lại [[src-tt14-2025-nhnn#^pl2-4b]]. $PFE_j$ cộng [[replacement-cost]] trong công thức $RWA_{CCR}$ của phái sinh [[src-tt14-2025-nhnn#^pl2-4]].

## Công thức
$$
PFE_j = N_j \times a_j
$$
[[src-tt14-2025-nhnn#^pl2-4b]]

Ký hiệu $N_j$ (vốn danh nghĩa) và $a_j$ (chỉ số tăng thêm theo [[add-on-factor]]) là của wiki; nguồn viết bằng chữ [[src-tt14-2025-nhnn#^pl2-4b]].

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $N_j$ | Tổng giá trị vốn danh nghĩa theo pháp luật về hạch toán kế toán | node này | [[src-tt14-2025-nhnn#^pl2-4b]] |
| $a_j$ | Chỉ số tăng thêm theo loại tài sản cơ sở và thời hạn còn lại | [[add-on-factor]] | [[src-tt14-2025-nhnn#^pl2-4b]] |

## Diễn giải
**Quy tắc điều chỉnh.**
- Hợp đồng trao đổi vốn gốc nhiều lần: chỉ số tăng thêm tính theo từng lần thanh toán còn lại [[src-tt14-2025-nhnn#^pl2-4b1]].
- Vốn danh nghĩa khác nhau theo thỏa thuận: tính theo từng giá trị [[src-tt14-2025-nhnn#^pl2-4b1]].
- Hợp đồng có ngày thanh toán cụ thể và ngày cụ thể định lại giá trị thị trường bằng 0: thời hạn còn lại là thời gian đến kỳ định lại tiếp theo [[src-tt14-2025-nhnn#^pl2-4b1]].
- Hoán đổi lãi suất thả nổi/thả nổi một đồng tiền: không tính PFE [[src-tt14-2025-nhnn#^pl2-4b2]].

**Bù trừ hai bên.** Khi bù trừ hai bên, tổng $PFE_j$ của các giao dịch thành phần là $A_{Gross}$, rồi điều chỉnh bằng NGR ([[bilateral-netting]]) [[src-tt14-2025-nhnn#^pl2-10]].

*Diễn giải:* ví dụ số do wiki dựng: hoán đổi ngoại hối vốn danh nghĩa 200 tỷ đồng, thời hạn còn lại 3 năm, chỉ số tăng thêm 5,0% [[src-tt14-2025-nhnn#^pl2-4b]] cho $PFE_j$ = 10 tỷ đồng. Nguồn không đưa ví dụ số cho PFE.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Phương pháp | [cần nguồn] (CRE chưa ingest) | Vốn danh nghĩa × chỉ số tăng thêm theo loại tài sản và thời hạn [[src-tt14-2025-nhnn#^pl2-4b]] | PL2.4b | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Hoán đổi thả nổi/thả nổi một đồng tiền | [cần nguồn] | Không tính PFE [[src-tt14-2025-nhnn#^pl2-4b2]] | PL2.4b(v) | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* PFE tăng theo vốn danh nghĩa và thời hạn, không theo biến động thị trường. Với phái sinh lãi suất thời hạn trên 05 năm, chỉ số tăng thêm 1,5% [[src-tt14-2025-nhnn#^pl2-4b]]. Danh mục hoán đổi lãi suất dài hạn dùng để phòng ngừa IRRBB làm PFE lớn dù giá trị thị trường gần 0.

## Nhầm lẫn thường gặp
- PFE không phải ước lượng thống kê mà là tích vốn danh nghĩa với hệ số ấn định [[src-tt14-2025-nhnn#^pl2-4b]].
- Hoán đổi lãi suất thả nổi/thả nổi một đồng tiền không có PFE [[src-tt14-2025-nhnn#^pl2-4b2]].
