---
title: "IRB Risk Provisions"
aliases: [IRB Risk Provisions, Dự phòng rủi ro theo IRB, Dự phòng rủi ro tính so với EL]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[el-provision-difference-treatment]]", cite: "[[src-tt14-2025-nhnn#^d62-1]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Dự phòng rủi ro theo Đ61 là tổng số tiền dự phòng cụ thể ([[specific-provision]]), dự phòng chung, dự phòng tổn thất các khoản đầu tư (nếu có) và dự phòng nợ phải thu khó đòi (nếu có) mà ngân hàng đã trích lập theo quy định của pháp luật cho các khoản phải đòi được tính tài sản có rủi ro khách hàng theo IRB [[src-tt14-2025-nhnn#^d61-1]]. Đây là vế so sánh với [[irb-expected-loss]].

## Công thức
$$
\text{Dự phòng rủi ro} = DP_{\text{cụ thể}} + DP_{\text{chung}} + DP_{\text{đầu tư}} + DP_{\text{phải thu}}
$$
[[src-tt14-2025-nhnn#^d61-1]]

Hai cấu phần cuối chỉ cộng nếu có [[src-tt14-2025-nhnn#^d61-1]]. Phạm vi chỉ gồm khoản phải đòi dùng IRB; dự phòng của khoản dùng phương pháp tiêu chuẩn không vào phép so sánh này [[src-tt14-2025-nhnn#^d61-1]].

## Diễn giải
Chênh lệch giữa dự phòng rủi ro và EL quyết định khoản trừ hoặc cộng vào vốn tự có, xem [[el-provision-difference-treatment]]. Dự phòng chung của danh mục phương pháp tiêu chuẩn có trần riêng 1,25% trong vốn cấp 2 ([[tier-2-capital]]).

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu phần dự phòng rủi ro | [cần nguồn] (CRE35 chưa ingest) | Dự phòng cụ thể + chung + đầu tư + phải thu khó đòi [[src-tt14-2025-nhnn#^d61-1]] | Đ61 | Khi được NHNN chấp thuận IRB |

## Ứng dụng trong ALM
*Diễn giải:* dự phòng cần được theo dõi theo từng danh mục IRB và danh mục tiêu chuẩn riêng, vì mỗi danh mục có cách xử lý chênh lệch khác nhau.

## Nhầm lẫn thường gặp
- Dự phòng ở Đ61 là số đã trích lập theo pháp luật, không phải số ước tính theo mô hình [[src-tt14-2025-nhnn#^d61-1]].
