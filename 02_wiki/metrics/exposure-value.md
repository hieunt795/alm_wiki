---
title: "Exposure Value"
aliases: [Exposure Value, Giá trị số dư khoản phải đòi, Giá trị khoản phải đòi, E_i]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[customer-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^d8-2-vars]]"}
tags: [capital, credit-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Giá trị số dư của khoản phải đòi ($E_i$) gồm số dư gốc, lãi phải thu và phí phải thu (nếu có) đang được hạch toán vào thu nhập theo quy định của pháp luật [[src-tt14-2025-nhnn#^d8-3]]. $E_i$ xác định theo nguyên giá của khoản phải đòi [[src-tt14-2025-nhnn#^d8-3-vars]].

## Công thức
$$
E_i = Eon_i + Eoff_i \times CCF_i
$$
[[src-tt14-2025-nhnn#^d8-3]]

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $Eon_i$ | Số dư nợ phần nội bảng của khoản phải đòi i | node này | [[src-tt14-2025-nhnn#^d8-3-vars]] |
| $Eoff_i$ | Số dư phần cam kết ngoại bảng của khoản phải đòi i | node này | [[src-tt14-2025-nhnn#^d8-3-vars]] |
| $CCF_i$ | Hệ số chuyển đổi của phần cam kết ngoại bảng | [[credit-conversion-factor]] | [[src-tt14-2025-nhnn#^d8-3-vars]] |

## Diễn giải
**Từ $E_i$ sang $E_i^{*}$.** Trong công thức $RWA_{CR}$, giá trị dùng là $E_i^{*}$: số dư xác định theo công thức trên rồi điều chỉnh giảm theo các biện pháp giảm thiểu rủi ro tín dụng tại Đ25–29 [[src-tt14-2025-nhnn#^d8-2-vars]]. Công thức $E_i^{*}$ và các biện pháp xem [[credit-risk-mitigation]] [[src-tt14-2025-nhnn#^d25-4]]. Xem [[customer-credit-risk-rwa]].

*Diễn giải:* phần ngoại bảng vào $E_i$ qua $CCF_i$ ở Đ10. Ví dụ số do wiki dựng: hạn mức thẻ tín dụng chưa sử dụng 100 tỷ đồng, CCF 10% [[src-tt14-2025-nhnn#^d10-1]], thì đóng góp 10 tỷ đồng vào $E_i$. Nguồn không đưa ví dụ số.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức | [cần nguồn] (CRE chưa ingest) | $Eon_i + Eoff_i \times CCF_i$ [[src-tt14-2025-nhnn#^d8-3]] | Đ8.3 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Gồm lãi, phí phải thu | [cần nguồn] | Có, khi đang hạch toán vào thu nhập [[src-tt14-2025-nhnn#^d8-3]] | Đ8.3 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* do $E_i$ gồm lãi phải thu đang hạch toán vào thu nhập, việc ngừng hạch toán lãi (chuyển nợ xấu) làm đổi giá trị tính RWA. Khoản này liên quan [[effective-interest-rate]] và chính sách ghi nhận thu nhập lãi.

## Nhầm lẫn thường gặp
- $E_i$ theo Đ8.3 chưa trừ giảm thiểu rủi ro tín dụng. $E_i^{*}$ trong công thức $RWA_{CR}$ mới là số đã trừ [[src-tt14-2025-nhnn#^d8-2-vars]].
- $E_j$ (tài sản không phải khoản phải đòi) là đại lượng khác $E_i$ [[src-tt14-2025-nhnn#^d8-2-vars]].
