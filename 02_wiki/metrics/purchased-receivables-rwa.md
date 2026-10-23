---
title: "Purchased Receivables RWA"
aliases: [Purchased Receivables RWA, RWA_PR, Tài sản có rủi ro tín dụng khách hàng của khoản mua lại khoản phải thu]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[customer-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^d54-1]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tài sản có rủi ro tín dụng khách hàng của khoản mua lại khoản phải thu (RWA<sub>PR</sub>) là tổng của tài sản có rủi ro tín dụng vỡ nợ và tài sản có rủi ro giảm giá trị [[src-tt14-2025-nhnn#^d54-1]]. Loại tài sản này gồm ba nhóm doanh nghiệp, bán lẻ, hỗn hợp [[irb-asset-classes]]. Ngân hàng áp dụng IRB cho nhóm này thì dùng Mục 6 Chương III.

## Công thức
$$
RWA_{PR} = RWA_{DfR} + RWA_{DR}
$$
[[src-tt14-2025-nhnn#^d54-1]]

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $RWA_{DfR}$ | Tài sản có rủi ro tín dụng vỡ nợ | [[purchased-receivables-default-risk-rwa]] | [[src-tt14-2025-nhnn#^d54-1]] |
| $RWA_{DR}$ | Tài sản có rủi ro giảm giá trị | [[purchased-receivables-dilution-risk-rwa]] | [[src-tt14-2025-nhnn#^d54-1]] |

## Diễn giải
- Rủi ro tín dụng vỡ nợ là rủi ro bên có nghĩa vụ thanh toán không thực hiện được nghĩa vụ; rủi ro giảm giá trị là rủi ro giá trị khoản phải thu giảm theo thỏa thuận tại hợp đồng cơ sở giữa bên bán và khách hàng [[src-tt14-2025-nhnn#^d54-23]].
- Bảo lãnh và phái sinh tín dụng giảm thiểu được cả hai rủi ro; bảo vệ một phần thì chỉ phần được bảo vệ dùng PD, LGD của bên bảo vệ [[src-tt14-2025-nhnn#^d59-2]]. Điều kiện ghi nhận: Đ28–29 (phương pháp tiêu chuẩn) hoặc Đ45, 46, 52 (IRB) [[src-tt14-2025-nhnn#^d59-1]]. Xem [[irb-credit-risk-mitigation]].
- Khoản mua lại hỗn hợp không phân tách được tính hệ số rủi ro tín dụng 200% theo phương pháp tiêu chuẩn, không đi theo công thức này [[src-tt14-2025-nhnn#^d39-2]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu phần RWA khoản mua lại khoản phải thu | [cần nguồn] (CRE chưa ingest) | $RWA_{DfR} + RWA_{DR}$ [[src-tt14-2025-nhnn#^d54-1]] | Đ54.1 | Khi áp dụng IRB |

## Ứng dụng trong ALM
*Diễn giải:* nghiệp vụ mua lại khoản phải thu (bao tiêu, chiết khấu, bao thanh toán) phải tách hai nguồn rủi ro: khách hàng của khoản phải thu không trả, và bên bán cùng khách hàng thỏa thuận giảm giá trị. Dữ liệu hợp đồng cơ sở (điều khoản trả hàng, chiết khấu) quyết định có phát sinh $RWA_{DR}$ hay không.

## Nhầm lẫn thường gặp
- Dưới phương pháp tiêu chuẩn không tính $RWA_{DR}$ [[src-tt14-2025-nhnn#^d57-1]].
