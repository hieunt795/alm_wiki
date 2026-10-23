---
title: "Business Indicator Component"
aliases: [Business Indicator Component, BIC, Cấu phần chỉ số kinh doanh]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[operational-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d70-1]]"}
  - {type: input-to, to: "[[internal-loss-multiplier]]", cite: "[[src-tt14-2025-nhnn#^d70-3a]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Cấu phần chỉ số kinh doanh (Business indicator component, BIC) là thành phần quy mô của $K_{OR}$. BIC bằng tổng của chỉ số kinh doanh ([[business-indicator]]) theo từng nhóm nhân hệ số biên của nhóm đó [[src-tt14-2025-nhnn#^d70-2]]. BIC cũng là mẫu số của tỷ số LC/BIC trong [[internal-loss-multiplier]] [[src-tt14-2025-nhnn#^d70-3a]].

## Công thức
$$
BIC = \sum_{i=1}^{3} BI_{i} \times \alpha_{i}
$$
[[src-tt14-2025-nhnn#^d70-2]]

| Nhóm (i) | Khoảng BI (tỷ đồng) | Hệ số biên $\alpha_i$ | Nguồn |
|---|---|---|---|
| 1 | ≤ 600 | 12% | [[src-tt14-2025-nhnn#^d70-2a]] |
| 2 | trên 600 đến 18.000 | 15% | [[src-tt14-2025-nhnn#^d70-2a]] |
| 3 | trên 18.000 | 18% | [[src-tt14-2025-nhnn#^d70-2a]] |

Ví dụ của nguồn: BI là 20.000 tỷ đồng thì BIC = 600×12% + (18.000−600)×15% + (20.000−18.000)×18% = 3.042 tỷ đồng [[src-tt14-2025-nhnn#^d70-2a-vd]].

## Diễn giải
*Diễn giải:* ví dụ của nguồn tính từng bậc: 600 đầu tiên chịu 12%, phần từ 600 đến 18.000 chịu 15%, phần trên 18.000 chịu 18%. Cách tính này là hệ số biên lũy tiến; bảng ghi "hệ số biên" cho từng nhóm. Kiểm tra: 72 + 2.610 + 360 = 3.042 tỷ đồng, khớp ví dụ của nguồn.

*Diễn giải:* với BI trong nhóm 1 (không quá 600 tỷ đồng), BIC = 12% × BI. Ngân hàng nhóm này có ILM bằng 1 nên $K_{OR}$ = 12% × BI [[src-tt14-2025-nhnn#^d70-3b]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Hệ số biên nhóm 1 | [cần nguồn] (OPE chưa ingest) | 12%, BI ≤ 600 tỷ đồng [[src-tt14-2025-nhnn#^d70-2a]] | Đ70.2a | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Hệ số biên nhóm 2 | [cần nguồn] | 15%, trên 600 đến 18.000 tỷ đồng [[src-tt14-2025-nhnn#^d70-2a]] | Đ70.2a | Như trên |
| Hệ số biên nhóm 3 | [cần nguồn] | 18%, trên 18.000 tỷ đồng [[src-tt14-2025-nhnn#^d70-2a]] | Đ70.2a | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* BIC tăng theo quy mô BI mà không phụ thuộc chất lượng kiểm soát. Giảm $K_{OR}$ chỉ qua nhánh ILM khi ngân hàng có đủ dữ liệu tổn thất. Xem [[operational-risk-capital-requirement]].

## Nhầm lẫn thường gặp
- BIC không phải vốn yêu cầu. Vốn yêu cầu là BIC nhân ILM [[src-tt14-2025-nhnn#^d70-1]].
- Hệ số biên áp dụng cho từng phần của BI nằm trong khoảng của nhóm, không áp một hệ số cho toàn bộ BI (xem ví dụ 3.042 tỷ đồng) [[src-tt14-2025-nhnn#^d70-2a-vd]].
