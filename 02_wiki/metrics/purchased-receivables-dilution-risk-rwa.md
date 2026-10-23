---
title: "Purchased Receivables Dilution Risk RWA"
aliases: [Purchased Receivables Dilution Risk RWA, RWA_DR, Dilution Risk, Rủi ro giảm giá trị khoản mua lại khoản phải thu]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[purchased-receivables-rwa]]", cite: "[[src-tt14-2025-nhnn#^d54-1]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
$RWA_{DR}$ là tài sản có rủi ro giảm giá trị của khoản mua lại khoản phải thu. Rủi ro giảm giá trị xảy ra khi giá trị khoản phải thu giảm theo thỏa thuận giữa bên bán và khách hàng tại hợp đồng cơ sở, như trả lại hàng đã bán, tranh chấp chất lượng sản phẩm, chiết khấu khi thanh toán [[src-tt14-2025-nhnn#^d54-23]]. Là một cấu phần của [[purchased-receivables-rwa]].

## Công thức
$RWA_{DR}$ tính bằng công thức Đ41 ([[irb-capital-requirement]]) cho khoản doanh nghiệp hoặc Đ49 cho khoản bán lẻ, với tham số sau [[src-tt14-2025-nhnn#^d57-2]]:

| Tham số | Giá trị | Nguồn |
|---|---|---|
| $PD_{DR}$ | Tỷ lệ tổn thất dự kiến trong vòng 01 năm cho rủi ro giảm giá trị, tính theo % giá trị khoản mua lại | [[src-tt14-2025-nhnn#^d58-1]] [[src-tt14-2025-nhnn#^d57-2]] |
| $LGD_{DR}$ | 100% | [[src-tt14-2025-nhnn#^d58-1]] |
| $EAD_{DR}$ | Theo Đ47 (doanh nghiệp, [[exposure-at-default]]) hoặc Đ53 (bán lẻ) | [[src-tt14-2025-nhnn#^d58-1]] |
| $M$ (doanh nghiệp) | 2,5 năm; 01 năm khi ngân hàng dự kiến xử lý được khoản mua lại trong vòng 01 năm | [[src-tt14-2025-nhnn#^d58-1]] |

Với khoản bán lẻ, ước tính tỷ lệ tổn thất dự kiến không dùng giả định truy đòi hoặc bảo lãnh từ bên bán và bên khác [[src-tt14-2025-nhnn#^d57-2]].

## Diễn giải
- Không phải tính $RWA_{DR}$ khi khoản mua lại áp dụng phương pháp tiêu chuẩn, hoặc áp dụng IRB mà hợp đồng cơ sở không có thỏa thuận làm phát sinh rủi ro giảm giá trị, hoặc thời hạn thực hiện thỏa thuận đã qua trước khi mua [[src-tt14-2025-nhnn#^d57-1]].
- Bảo lãnh và phái sinh tín dụng giảm thiểu rủi ro giảm giá trị bằng cách dùng PD, LGD của bên bảo vệ cho phần được bảo vệ; phần còn lại dùng tham số của khách hàng [[src-tt14-2025-nhnn#^d59-2]].

*Diễn giải:* với $LGD_{DR} = 100\%$ thì $K$ trong công thức Đ41 và Đ49 còn lại $N(\cdot) - PD$ nhân 1, nên rủi ro giảm giá trị phụ thuộc hoàn toàn vào $PD_{DR}$ và hệ số tương quan. Phần này là suy luận từ công thức, nguồn không nêu.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| $LGD_{DR}$ | [cần nguồn] (CRE chưa ingest) | 100% [[src-tt14-2025-nhnn#^d58-1]] | Đ58.2 | Khi áp dụng IRB |
| $M$ khoản doanh nghiệp | [cần nguồn] | 2,5 năm hoặc 01 năm [[src-tt14-2025-nhnn#^d58-1]] | Đ58.4 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* ngân hàng cần dữ liệu lịch sử về trả hàng, chiết khấu và tranh chấp của chuỗi cung ứng để ước tính $PD_{DR}$. Hợp đồng cơ sở nào không có thỏa thuận làm phát sinh giảm giá trị thì miễn tính cấu phần này.

## Nhầm lẫn thường gặp
- $PD_{DR}$ không phải xác suất vỡ nợ của khách hàng mà là tỷ lệ tổn thất dự kiến 01 năm do giảm giá trị [[src-tt14-2025-nhnn#^d58-1]].
