---
title: "Loan to Value"
aliases: [Loan to Value, LTV, Tỷ lệ bảo đảm, Tỷ lệ cho vay trên giá trị tài sản bảo đảm]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[real-estate-exposure-risk-weighting]]", cite: "[[src-tt14-2025-nhnn#^d16-5ab]]"}
tags: [capital, credit-risk, collateral, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tỷ lệ bảo đảm (Loan to value, LTV) là tỷ số giữa tổng số dư khoản phải đòi và tổng giá trị tài sản bảo đảm là bất động sản [[src-tt14-2025-nhnn#^d16-5ab]]. TT14/2025 dùng LTV để xác định hệ số rủi ro tín dụng của khoản phải đòi bất động sản đủ tiêu chuẩn [[src-tt14-2025-nhnn#^d16-5ab]]. Xem [[real-estate-exposure-risk-weighting]].

## Công thức
$$
LTV(\%) = \frac{L}{V} \times 100\%
$$
[[src-tt14-2025-nhnn#^d16-5ab]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| L | Tổng số dư khoản phải đòi: số dư khoản bất động sản đủ tiêu chuẩn cần tính LTV cộng số dư các khoản phải đòi khác được đảm bảo bằng cùng một tài sản bảo đảm, tại các ngân hàng; gồm số dư nợ gốc nội bảng và số dư cam kết ngoại bảng | [[src-tt14-2025-nhnn#^d16-5l]] |
| V | Tổng giá trị tài sản bảo đảm là bất động sản của khoản cần tính LTV, theo giá trị tại thời điểm định giá gần nhất | [[src-tt14-2025-nhnn#^d16-5v]] |

L và V không có node riêng vì nguồn chỉ định nghĩa hai đại lượng này để tính LTV.

## Diễn giải
**Định giá.** Giá trị tài sản bảo đảm xác định theo quy định nội bộ của ngân hàng về định giá tài sản bảo đảm. Tổ chức thẩm định giá hoặc bộ phận độc lập với bộ phận phê duyệt tín dụng thực hiện [[src-tt14-2025-nhnn#^d16-5c]].

**Phạm vi.** LTV chỉ dùng cho khoản phải đòi bất động sản đủ tiêu chuẩn theo Đ16.2a [[src-tt14-2025-nhnn#^d16-5ab]].

*Diễn giải:* L cộng cả số dư của khoản phải đòi khác cùng dùng một tài sản bảo đảm, tại các ngân hàng. Ngân hàng cần biết số dư của ngân hàng khác trên cùng tài sản; nguồn không nêu cách thu thập thông tin này [cần nguồn].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức LTV | [cần nguồn] (CRE chưa ingest) | $L / V \times 100\%$ [[src-tt14-2025-nhnn#^d16-5ab]] | Đ16.5b | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Mẫu số V | [cần nguồn] | Giá trị tại thời điểm định giá gần nhất [[src-tt14-2025-nhnn#^d16-5v]] | Đ16.5b(ii) | Như trên |
| Tử số L | [cần nguồn] | Gồm khoản phải đòi khác cùng tài sản bảo đảm [[src-tt14-2025-nhnn#^d16-5l]] | Đ16.5b(i) | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* LTV đổi theo giá bất động sản tại lần định giá gần nhất. Giá giảm làm V giảm, LTV tăng và có thể đẩy khoản vay sang dải hệ số cao hơn trong bảng Đ17. Tần suất định giá lại do quy định nội bộ của ngân hàng, nguồn không nêu [cần nguồn].

## Nhầm lẫn thường gặp
- L không chỉ là dư nợ của riêng khoản đang tính mà gồm cả khoản phải đòi khác cùng tài sản bảo đảm [[src-tt14-2025-nhnn#^d16-5l]].
- L gồm cam kết ngoại bảng, không chỉ dư nợ gốc nội bảng [[src-tt14-2025-nhnn#^d16-5l]].
