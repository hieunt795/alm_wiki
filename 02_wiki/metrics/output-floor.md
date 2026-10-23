---
title: "Output Floor"
aliases: [Output Floor, Tỷ lệ sàn đầu ra, Sàn đầu ra]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: limits, to: "[[customer-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^d35-12]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tỷ lệ sàn đầu ra (output floor) đặt mức tối thiểu cho $RWA_{CR}$ theo phương pháp xếp hạng nội bộ: $RWA_{CR}$ theo IRB tối thiểu bằng tỷ lệ sàn nhân $RWA_{CR}$ theo phương pháp tiêu chuẩn [[src-tt14-2025-nhnn#^d35-12]]. Ngân hàng phải duy trì tỷ lệ sàn tối thiểu 72,5% kể từ ngày được chấp thuận áp dụng IRB [[src-tt14-2025-nhnn#^d35-12]]. Xem [[internal-ratings-based-approach]].

## Công thức
$$
RWA_{CR}(IRB) \geq f \times RWA_{CR}(SA), \quad f \geq 72{,}5\%
$$
[[src-tt14-2025-nhnn#^d35-12]]

Ký hiệu $f$ (tỷ lệ sàn đầu ra) là của wiki; nguồn viết bằng chữ [[src-tt14-2025-nhnn#^d35-12]].

## Diễn giải
Tỷ lệ sàn nằm trong nội dung đánh giá tuân thủ của kiểm toán độc lập, tự đánh giá của Hội đồng quản trị và hồ sơ chấp thuận [[src-tt14-2025-nhnn#^d32-12]] [[src-tt14-2025-nhnn#^d33-1d]].

*Diễn giải:* sàn không áp dụng theo loại tài sản như tỷ lệ bao phủ ([[irb-coverage-ratio]]); câu chữ của Đ35 nói tổng $RWA_{CR}$ theo IRB so với tổng $RWA_{CR}$ theo phương pháp tiêu chuẩn. Ví dụ số do wiki dựng: tổng $RWA_{CR}$ theo phương pháp tiêu chuẩn 1.000 tỷ đồng thì $RWA_{CR}$ theo IRB không thấp hơn 725 tỷ đồng, dù mô hình nội bộ cho ra 600 tỷ đồng.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Mức sàn | [cần nguồn] (CRE chưa ingest) | 72,5% [[src-tt14-2025-nhnn#^d35-12]] | Đ35.2 | Từ ngày NHNN chấp thuận IRB |
| Đối tượng so sánh | [cần nguồn] | Tổng $RWA_{CR}$ theo phương pháp tiêu chuẩn [[src-tt14-2025-nhnn#^d35-12]] | Đ35.1 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* khi sàn ràng buộc, lợi ích vốn của IRB bị giới hạn ở 27,5% RWA tiêu chuẩn. Ngân hàng phải tính song song RWA theo phương pháp tiêu chuẩn kể cả sau khi chuyển sang IRB, để kiểm sàn.

## Nhầm lẫn thường gặp
- Sàn áp dụng trên $RWA_{CR}$, không áp lên $K_{OR}$, $K_{MR}$ hay $RWA_{CCR}$ [[src-tt14-2025-nhnn#^d35-12]].
