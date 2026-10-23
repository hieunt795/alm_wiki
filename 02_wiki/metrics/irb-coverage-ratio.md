---
title: "IRB Coverage Ratio"
aliases: [IRB Coverage Ratio, Tỷ lệ bao phủ IRB, Tỷ lệ bao phủ phương pháp xếp hạng nội bộ]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: limits, to: "[[internal-ratings-based-approach]]", cite: "[[src-tt14-2025-nhnn#^d31-3]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tỷ lệ bao phủ là tỷ lệ $RWA_{CR}$ theo IRB trên tổng $RWA_{CR}$ theo IRB và theo phương pháp tiêu chuẩn, tính riêng cho từng loại tài sản, trên cơ sở riêng lẻ (không gồm công ty con đối với ngân hàng thương mại). Loại tài sản chọn IRB phải đạt tối thiểu 70% [[src-tt14-2025-nhnn#^d31-3]]. Xem [[internal-ratings-based-approach]].

## Công thức
$$
\text{Bao phủ} = \frac{RWA_{CR}(IRB)}{RWA_{CR}(SA) + RWA_{CR}(IRB)} \geq 70\%
$$
[[src-tt14-2025-nhnn#^d31-3]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $RWA_{CR}(IRB)$ | Tài sản có rủi ro tín dụng khách hàng cho tài sản áp dụng IRB | [[src-tt14-2025-nhnn#^d31-3]] |
| $RWA_{CR}(SA)$ | Tài sản có rủi ro tín dụng khách hàng cho tài sản áp dụng phương pháp tiêu chuẩn | [[src-tt14-2025-nhnn#^d31-3]] |

Tử số và mẫu số lấy theo khoản phải đòi trong một loại tài sản (doanh nghiệp, bán lẻ hoặc mua lại khoản phải thu) [[src-tt14-2025-nhnn#^d31-3]]. Nhãn "Bao phủ" là của wiki; nguồn viết bằng chữ.

## Diễn giải
Ngân hàng phải duy trì tỷ lệ tối thiểu kể từ ngày NHNN chấp thuận [[src-tt14-2025-nhnn#^d31-4]]. Tỷ lệ bao phủ nằm trong nội dung kiểm toán độc lập và tự đánh giá của giai đoạn chuyển đổi [[src-tt14-2025-nhnn#^d32-12]] và trong báo cáo kết quả tính toán của hồ sơ chấp thuận [[src-tt14-2025-nhnn#^d33-1d]].

*Diễn giải:* tỷ lệ tính trên RWA, không trên dư nợ. Khoản bắt buộc dùng phương pháp tiêu chuẩn (cấp tín dụng chuyên biệt, tài sản khác) đi vào $RWA_{CR}(SA)$ ở mẫu số và làm bao phủ giảm. Ví dụ số do wiki dựng: RWA_CR(IRB) 700 tỷ đồng và RWA_CR(SA) 300 tỷ đồng cho bao phủ 700 / 1.000 = 70%, đúng ngưỡng.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Ngưỡng bao phủ | [cần nguồn] (CRE chưa ingest) | 70% theo loại tài sản, cơ sở riêng lẻ [[src-tt14-2025-nhnn#^d31-3]] | Đ31.3 | Từ ngày NHNN chấp thuận IRB [[src-tt14-2025-nhnn#^d31-4]] |

## Ứng dụng trong ALM
*Diễn giải:* tăng trưởng danh mục tài sản thuộc phương pháp tiêu chuẩn bắt buộc (như tín dụng chuyên biệt) làm bao phủ giảm. ALM và quản lý rủi ro tín dụng cần dự phóng tỷ lệ bao phủ theo kế hoạch tăng trưởng.

## Nhầm lẫn thường gặp
- Tỷ lệ bao phủ tính riêng cho từng loại tài sản, không phải toàn danh mục [[src-tt14-2025-nhnn#^d31-3]].
- Tỷ lệ bao phủ khác tỷ lệ sàn đầu ra ([[output-floor]]).
