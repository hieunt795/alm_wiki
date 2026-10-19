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
sources: ["[[src-tt83-2025-nhnn]]"]
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
- *Diễn giải:* $RWA_{IRRBB}$ là một cấu phần của $C_E$ [[src-tt83-2025-nhnn#^pl6-1b]]. Vì vậy vị thế IRRBB lớn làm giảm RAROC toàn ngân hàng, kể cả khi NII không đổi. Xem [[rwa-irrbb]], [[ftp-balance-sheet-optimization]].

## Nhầm lẫn thường gặp
- *Diễn giải:* RAROC theo TT83 là chỉ tiêu cấp ngân hàng trong khẩu vị rủi ro. RAROC theo sản phẩm hay khách hàng trong FTP là cách dùng nội bộ khác, chưa có nguồn VN.
