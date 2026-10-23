---
title: "Effective Maturity and Maturity Adjustment (M, b)"
aliases: [Effective Maturity, Thời hạn hiệu lực của khoản phải đòi, Điều chỉnh kỳ hạn b, Maturity Adjustment IRB]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[irb-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d41-2dd]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Thời hạn hiệu lực của khoản phải đòi (M) là thời hạn còn lại của khoản phải đòi dùng để tính tài sản có rủi ro tín dụng khách hàng [[src-tt14-2025-nhnn#^d2-31]]. Với khoản phải đòi doanh nghiệp, M là 2,5 năm [[src-tt14-2025-nhnn#^d48-1]]. Hệ số điều chỉnh kỳ hạn b nhận PD làm đầu vào [[src-tt14-2025-nhnn#^d41-2dd]].

## Công thức
$$
b = \left[ 0{,}11852 - 0{,}05478 \times \ln(PD) \right]^2
$$
[[src-tt14-2025-nhnn#^d41-2dd]]

Cấu phần kỳ hạn trong K là nhân tử $\frac{1 + (M - 2{,}5) \times b}{1 - 1{,}5 \times b}$ [[src-tt14-2025-nhnn#^d41-2c]].

## Diễn giải
- Khi M = 2,5 thì tử số bằng 1, và nhân tử còn lại là $\frac{1}{1 - 1{,}5 \times b}$ [[src-tt14-2025-nhnn#^d41-2c]] [[src-tt14-2025-nhnn#^d48-1]].
- Mỗi lượng $(M - 2{,}5)$ lệch khỏi 2,5 năm đổi K theo b; b giảm khi PD tăng, vì $\ln(PD)$ càng gần 0 thì b càng nhỏ trong khoảng PD hợp lệ. *Diễn giải:* suy luận từ dạng công thức, chưa có ví dụ số trong nguồn.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| M khoản phải đòi doanh nghiệp (IRB cơ bản) | [cần nguồn] (CRE32 chưa ingest) | 2,5 năm [[src-tt14-2025-nhnn#^d48-1]] | Đ48 | Khi áp dụng IRB |
| b | [cần nguồn] | $[0{,}11852 - 0{,}05478 \ln(PD)]^2$ [[src-tt14-2025-nhnn#^d41-2dd]] | Đ41.2đ | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* với IRB cơ bản cho doanh nghiệp, M cố định nên kỳ hạn thực của danh mục không làm đổi K. Hệ quả cho quản trị kỳ hạn tài sản có chưa được nguồn nói; M tự ước tính của AIRB thuộc đơn vị khác chưa ingest [cần nguồn].

## Nhầm lẫn thường gặp
- M ở Đ48 là hằng số 2,5 năm, khác thời hạn còn lại T và t trong các công thức giảm thiểu rủi ro [[src-tt14-2025-nhnn#^d44-3]].
