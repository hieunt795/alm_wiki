---
title: "Target Capital"
aliases: [Target Capital, Vốn mục tiêu]
type: metric
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[capital-plan]]", cite: "[[src-tt83-2025-nhnn#^d61-1]]"}
  - {type: part-of, to: "[[icaap]]", cite: "[[src-tt83-2025-nhnn#^d59-2]]"}
tags: [capital, icaap]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
Vốn mục tiêu ($C_{Target}$) là mức vốn ngân hàng phải duy trì theo [[icaap]]. Bước 3 của ICAAP là xác định vốn mục tiêu và vốn tự có dự kiến theo Phụ lục VI [[src-tt83-2025-nhnn#^d59-2]].

## Công thức
$$
C_{Target} = \max(C_R,\ C_E)
$$
[[src-tt83-2025-nhnn#^pl6-2]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $C_R$ | Vốn tự có để đáp ứng tỷ lệ an toàn vốn theo quy định NHNN | [[src-tt83-2025-nhnn#^pl6-2]] |
| $C_E$ | Vốn kinh tế ([[economic-capital]]) | [[src-tt83-2025-nhnn#^pl6-2]] |

## Diễn giải
Vốn mục tiêu là chuẩn để so sánh với [[projected-own-funds]] ($C_A$):
- Vốn tự có dự kiến không đáp ứng vốn mục tiêu thì kế hoạch vốn phải có phương án tăng vốn [[src-tt83-2025-nhnn#^d61-1]].
- Chính sách cổ tức phải bảo đảm vốn tự có dự kiến sau khi chia không thấp hơn vốn mục tiêu [[src-tt83-2025-nhnn#^d61-1]].
- Vốn mục tiêu được phân bổ theo tài sản tính theo rủi ro cho các rủi ro trọng yếu, làm cơ sở xác định hạn mức [[src-tt83-2025-nhnn#^d61-1]]. Xem [[capital-plan]], [[risk-limits]].

ICAAP thực hiện đột xuất khi có thay đổi dẫn đến không đáp ứng chỉ tiêu vốn mục tiêu [[src-tt83-2025-nhnn#^d59-1]].

*Diễn giải:* phép max bảo đảm vốn mục tiêu không bao giờ thấp hơn mức đáp ứng CAR tối thiểu. Khi vốn kinh tế (gồm CAR mục tiêu và phần stress) cao hơn thì vốn kinh tế trở thành ràng buộc.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Vốn mục tiêu | [cần nguồn] | $\max(C_R, C_E)$ [[src-tt83-2025-nhnn#^pl6-2]] | TT83 PL6.I.2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |

## Ứng dụng trong ALM
- Báo cáo ICAAP gửi NHNN có bảng $C_{Target}$ cho năm $t_0$ đến $t_0+3$, kèm chênh lệch với vốn tự có dự kiến [[src-tt83-2025-nhnn#^pl3-3a]].
- Báo cáo ICAAP hằng năm nêu vốn mục tiêu và vốn kinh tế [[src-tt83-2025-nhnn#^d63-1]].

## Nhầm lẫn thường gặp
- *Diễn giải:* "tỷ lệ an toàn vốn mục tiêu" ($CAR_{Target}$, một chỉ tiêu khẩu vị rủi ro [[src-tt83-2025-nhnn#^d19-2]]) khác "vốn mục tiêu" ($C_{Target}$, số tiền). $CAR_{Target}$ là đầu vào của $C_E$ [[src-tt83-2025-nhnn#^pl6-1a]].
