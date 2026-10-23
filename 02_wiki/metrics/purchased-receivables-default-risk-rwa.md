---
title: "Purchased Receivables Default Risk RWA"
aliases: [Purchased Receivables Default Risk RWA, RWA_DfR, Tài sản có rủi ro tín dụng vỡ nợ của khoản mua lại khoản phải thu]
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
$RWA_{DfR}$ là tài sản có rủi ro tín dụng vỡ nợ của khoản mua lại khoản phải thu, ứng với rủi ro bên có nghĩa vụ thanh toán không thực hiện được nghĩa vụ [[src-tt14-2025-nhnn#^d54-23]]. Là một cấu phần của [[purchased-receivables-rwa]].

## Công thức
Không có công thức riêng; $RWA_{DfR}$ tính như khoản phải đòi cùng loại [[src-tt14-2025-nhnn#^d55-12]]:

| Nhóm | Cách tính | Tham số | Nguồn |
|---|---|---|---|
| Doanh nghiệp | Như khoản phải đòi doanh nghiệp theo Chương II và Mục 4 Chương III ([[irb-capital-requirement]]) | Ước tính PD; LGD, EAD, M theo Mục 4 | [[src-tt14-2025-nhnn#^d55-12]] [[src-tt14-2025-nhnn#^d56-12]] |
| Bán lẻ | Như khoản phải đòi bán lẻ theo Chương II và Mục 5 Chương III | Ước tính PD, LGD, EAD theo Mục 5, loại bỏ giả định truy đòi hoặc bảo lãnh từ bên bán và bên khác | [[src-tt14-2025-nhnn#^d55-12]] [[src-tt14-2025-nhnn#^d56-12]] |

Tham số: [[probability-of-default]], [[loss-given-default]], [[exposure-at-default]], [[maturity-adjustment]], [[irb-retail-parameter-estimation]].

## Diễn giải
Quyền truy đòi hoặc bảo lãnh từ bên bán bị loại khỏi ước tính tham số bán lẻ [[src-tt14-2025-nhnn#^d56-12]]; bảo lãnh đủ điều kiện được ghi nhận riêng qua Đ59 [[src-tt14-2025-nhnn#^d59-2]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| $RWA_{DfR}$ | [cần nguồn] (CRE chưa ingest) | Như khoản phải đòi doanh nghiệp hoặc bán lẻ cùng loại [[src-tt14-2025-nhnn#^d55-12]] | Đ55 | Khi áp dụng IRB |

## Ứng dụng trong ALM
*Diễn giải:* số liệu PD của khách hàng nợ (bên phải trả khoản phải thu) cần có dù ngân hàng không có quan hệ tín dụng trực tiếp; đây là điều kiện dữ liệu để dùng IRB cho nhóm này.

## Nhầm lẫn thường gặp
- Quyền truy đòi từ bên bán không giảm $RWA_{DfR}$ của khoản bán lẻ khi ước tính tham số [[src-tt14-2025-nhnn#^d56-12]].
