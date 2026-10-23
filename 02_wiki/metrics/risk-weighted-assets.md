---
title: "Risk-Weighted Assets"
aliases: [Risk-Weighted Assets, RWA, Tổng tài sản có rủi ro tín dụng, Tài sản có rủi ro tín dụng]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[capital-adequacy-ratio]]", cite: "[[src-tt14-2025-nhnn#^d5-1d]]"}
tags: [capital, credit-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tổng tài sản có rủi ro tín dụng (RWA) là cấu phần đầu tiên của mẫu số tỷ lệ an toàn vốn [[src-tt14-2025-nhnn#^d5-1d]]. RWA gồm tổng tài sản có rủi ro tín dụng khách hàng (RWA<sub>CR</sub>) và tổng tài sản có rủi ro tín dụng đối tác (RWA<sub>CCR</sub>) [[src-tt14-2025-nhnn#^d8-1]]. Xem [[capital-adequacy-ratio]]. Phương pháp tính $RWA_{CR}$ có hai cách: tiêu chuẩn (Chương II) và xếp hạng nội bộ ([[internal-ratings-based-approach]], Chương III) [[src-tt14-2025-nhnn#^d30-1]].

## Công thức
$$
RWA = RWA_{CR} + RWA_{CCR}
$$
[[src-tt14-2025-nhnn#^d8-1]]

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $RWA_{CR}$ | Tổng tài sản có rủi ro tín dụng khách hàng | [[customer-credit-risk-rwa]] | [[src-tt14-2025-nhnn#^d8-1]] |
| $RWA_{CCR}$ | Tổng tài sản có rủi ro tín dụng đối tác | [[counterparty-credit-risk-rwa]] | [[src-tt14-2025-nhnn#^d8-1]] |

## Diễn giải
**Không tính trùng.** Giao dịch đã tính rủi ro tín dụng đối tác không phải tính rủi ro tín dụng khách hàng khi tính tỷ lệ an toàn vốn [[src-tt14-2025-nhnn#^d8-5]].

**Mẫu số CAR.** RWA cộng 12,5 lần ($K_{OR}$ + $K_{MR}$) tạo mẫu số của ba tỷ lệ [[src-tt14-2025-nhnn#^d5-1d]]. Xem [[operational-risk-capital-requirement]] và [[market-risk-capital-requirement]].

**Hợp nhất.** Khi tính tỷ lệ hợp nhất, ngân hàng thương mại áp dụng hệ số rủi ro tín dụng của Mục 2 Chương II cho khoản phải đòi của công ty con và chi nhánh ở nước ngoài [[src-tt14-2025-nhnn#^d9-4]].

*Diễn giải:* theo Đ8.1, RWA của TT14/2025 chỉ gồm hai nhánh tín dụng là khách hàng và đối tác. Rủi ro hoạt động và rủi ro thị trường vào mẫu số bằng nhánh riêng, qua hệ số 12,5 [[src-tt14-2025-nhnn#^d5-1d]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu phần của RWA | [cần nguồn] (CAP/CRE chưa ingest) | $RWA_{CR}$ + $RWA_{CCR}$ [[src-tt14-2025-nhnn#^d8-1]] | Đ8.1 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Tránh tính trùng | [cần nguồn] | Giao dịch đã tính $RWA_{CCR}$ không tính $RWA_{CR}$ [[src-tt14-2025-nhnn#^d8-5]] | Đ8.5 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* RWA là đại lượng đổi theo cơ cấu bảng cân đối. Tăng trưởng cho vay, danh mục giấy tờ có giá và cam kết ngoại bảng đều làm RWA đổi qua hệ số rủi ro tín dụng ([[credit-risk-weight]]) và hệ số chuyển đổi ([[credit-conversion-factor]]). [[capital-plan]] dự phóng RWA cùng [[own-funds]].

## Nhầm lẫn thường gặp
- RWA trong TT14/2025 chỉ là phần rủi ro tín dụng. Mẫu số CAR còn thêm $K_{OR}$ và $K_{MR}$ nhân 12,5 [[src-tt14-2025-nhnn#^d5-1d]].
- RWA khác [[rwa-irrbb]], là đại lượng nội bộ cho vốn kinh tế theo TT83/2025, không thuộc mẫu số CAR.
