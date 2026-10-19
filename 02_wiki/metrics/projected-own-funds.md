---
title: "Projected Own Funds"
aliases: [Projected Own Funds, Vốn tự có dự kiến]
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
Vốn tự có dự kiến ($C_A$) là vốn tự có theo quy định NHNN, dự phóng trên kế hoạch kinh doanh 3–5 năm tới [[src-tt83-2025-nhnn#^pl6-ii]]. Bước 3 của [[icaap]] xác định chỉ tiêu này cùng vốn mục tiêu [[src-tt83-2025-nhnn#^d59-2]].

## Công thức
Không có công thức đóng. $C_A$ là kết quả dự phóng với 4 giả định [[src-tt83-2025-nhnn#^pl6-ii]]:

| Giả định | Nguồn |
|---|---|
| Không có kế hoạch tăng vốn | [[src-tt83-2025-nhnn#^pl6-ii]] |
| Không bổ sung vốn cho công ty con, công ty liên kết, khoản góp vốn, mua cổ phần | [[src-tt83-2025-nhnn#^pl6-ii]] |
| Tỷ lệ chia cổ tức bằng bình quân 3 năm gần nhất | [[src-tt83-2025-nhnn#^pl6-ii]] |
| Lợi nhuận giữ lại sau chia cổ tức được bổ sung vốn | [[src-tt83-2025-nhnn#^pl6-ii]] |

## Diễn giải
- $C_A$ được so với [[target-capital]]. Nếu $C_A$ không đáp ứng vốn mục tiêu, kế hoạch vốn phải có phương án tăng vốn: nguồn tăng Vốn cấp 1, Vốn cấp 2, cùng thời gian và lộ trình [[src-tt83-2025-nhnn#^d61-1]].
- *Diễn giải:* giả định "không tăng vốn" làm $C_A$ phản ánh năng lực tự tích luỹ vốn. Khoảng thiếu so với vốn mục tiêu là lượng vốn phải huy động mới.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Vốn tự có dự kiến | [cần nguồn] | Dự phóng 3–5 năm với 4 giả định [[src-tt83-2025-nhnn#^pl6-ii]] | TT83 PL6.II | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |

## Ứng dụng trong ALM
- Rà soát ICAAP đánh giá tính khả thi của phương án tăng vốn [[src-tt83-2025-nhnn#^d62-1]]. Xem [[capital-plan]].

## Nhầm lẫn thường gặp
Không ghi nhận trong nguồn đã ingest.
