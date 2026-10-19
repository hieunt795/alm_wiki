---
title: "RAROC"
aliases: [RAROC, Risk Adjusted Returns on Capital, Tỷ suất lợi nhuận có điều chỉnh rủi ro trên vốn]
type: metric
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[risk-appetite]]", cite: "[[src-tt83-2025-nhnn#^d19-2]]"}
tags: [capital, profitability, risk-appetite]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
RAROC (tỷ suất giữa lợi nhuận có điều chỉnh rủi ro so với vốn tự có) là một chỉ tiêu thu nhập trong [[risk-appetite]], cùng với ROE [[src-tt83-2025-nhnn#^d19-2]].

## Công thức
$$
RAROC = \frac{\text{Tổng lợi nhuận trước thuế}}{C_E}
$$
[[src-tt83-2025-nhnn#^pl6-iii]]

Với $C_E$ là [[economic-capital]] [[src-tt83-2025-nhnn#^pl6-iii]].

## Diễn giải
*Diễn giải:*
- Tên chỉ tiêu ở Đ19 nói "so với vốn tự có", nhưng công thức PL6.III dùng vốn kinh tế $C_E$ làm mẫu số [[src-tt83-2025-nhnn#^d19-2]] [[src-tt83-2025-nhnn#^pl6-iii]]. Khi tính, theo công thức PL6.
- Tử số là lợi nhuận trước thuế, không trừ chi phí rủi ro kỳ vọng. "Điều chỉnh rủi ro" nằm ở mẫu số, vì $C_E$ đã gồm cả phần stress.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| RAROC | [cần nguồn] | Lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]] | TT83 PL6.III | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |

## Ứng dụng trong ALM
- RAROC là chỉ tiêu thu nhập trong bảng khẩu vị rủi ro của báo cáo ICAAP gửi NHNN, cùng ROE và $CAR_{target}$, cho năm $t_0$ đến $t_0+3$ [[src-tt83-2025-nhnn#^pl3-2]].
- *Diễn giải:* $RWA_{IRRBB}$ là một cấu phần của $C_E$ [[src-tt83-2025-nhnn#^pl6-1b]]. Vì vậy vị thế IRRBB lớn làm giảm RAROC toàn ngân hàng, kể cả khi NII không đổi. Xem [[rwa-irrbb]], [[ftp-balance-sheet-optimization]].

- **Định giá khoản vay theo RoE mục tiêu (Choudhry, T4)**: lãi suất hoà vốn là hàm của lãi suất funding, biên hoà vốn, RoE và thuế suất [[src-choudhry-principles-banking#^choudhry-lp-3]]. Mọi hoạt động phải tạo lợi nhuận vượt RoE mục tiêu [[src-choudhry-principles-banking#^choudhry-lp-1]]. Xem [[loan-pricing]].
- RoC hoặc RAROC của tài sản và danh mục nên luôn cao hơn cost of capital; CoC là hurdle rate cho mọi hoạt động [[src-choudhry-principles-banking#^choudhry-crd-10]]. Ví dụ danh mục mẫu: RAROC = (Spread − EL)/C(95) = 14,73% [[src-choudhry-principles-banking#^choudhry-crd-6]]. Xem [[expected-loss]], [[shareholder-value-added]].
- **Chọn chỉ tiêu return cho strategic plan (Choudhry, T4)**: RoE và RoA không điều chỉnh rủi ro; lựa chọn khác là RoC trên tổng vốn quy định Pillar I và Pillar II, RARoC (economic profit), RoRAC hay RoEC (economic capital), RoRWA. Choudhry khuyên dùng thước đo điều chỉnh rủi ro cho strategic plan [[src-choudhry-principles-banking#^choudhry-strat-15]]. Mục tiêu nên tính 'through the cycle' [[src-choudhry-principles-banking#^choudhry-strat-14]]. Xem [[bank-strategic-plan]].

## Nhầm lẫn thường gặp
- *Diễn giải:* RAROC theo TT83 là chỉ tiêu cấp ngân hàng trong khẩu vị rủi ro. RAROC theo sản phẩm hay khách hàng trong FTP là cách dùng nội bộ khác, chưa có nguồn VN.
