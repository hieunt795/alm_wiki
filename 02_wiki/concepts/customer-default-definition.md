---
title: "Customer Default Definition"
aliases: [Customer Default Definition, Khách hàng vỡ nợ, Định nghĩa vỡ nợ IRB, Default Definition]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[internal-ratings-based-approach]]", cite: "[[src-tt14-2025-nhnn#^d36-1]]"}
tags: [capital, credit-risk, irb, default, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ36 TT14/2025 định nghĩa khách hàng vỡ nợ cho phương pháp xếp hạng nội bộ bằng chín sự kiện, và quy định điều kiện để khách hàng không còn bị coi là vỡ nợ [[src-tt14-2025-nhnn#^d36-1]] [[src-tt14-2025-nhnn#^d36-4]]. Định nghĩa là đầu vào của PD ([[internal-ratings-based-approach]]). Khi khách hàng vỡ nợ, mọi khoản phải đòi của khách hàng đó tại ngân hàng là khoản phải đòi vỡ nợ và tính $RWA_{CR}$ như nợ xấu theo phương pháp tiêu chuẩn ([[credit-risk-asset-classes]]) [[src-tt14-2025-nhnn#^d36-23]].

## Cơ chế & drivers
**Chín sự kiện vỡ nợ (Đ36.1)** [[src-tt14-2025-nhnn#^d36-1]]:

| Điểm | Sự kiện |
|---|---|
| a | Khoản phải đòi, cam kết ngoại bảng thuộc nhóm nợ xấu sau khi điều chỉnh theo thông tin Trung tâm thông tin tín dụng Quốc gia Việt Nam, theo quy định phân loại tài sản có của NHNN |
| b | Khoản phải đòi tại chính ngân hàng đã sử dụng dự phòng để xử lý rủi ro |
| c | Khoản phải đòi tại chính ngân hàng đã xử lý tổn thất |
| d | Khoản phải đòi tại chính ngân hàng được gia hạn trả nợ, trừ cơ cấu lại giữ nguyên nhóm nợ theo quy định của Chính phủ, Thủ tướng Chính phủ, NHNN |
| đ | Trái phiếu doanh nghiệp đã kéo dài thời hạn trả nợ, hoặc đổi phương thức thanh toán từ tiền sang tài sản khác |
| e | Khoản phải đòi tại chính ngân hàng được bán thấp hơn giá trị ghi sổ nội bảng, trừ bán theo phương án cơ cấu lại được cấp có thẩm quyền phê duyệt |
| g | Khoản phải đòi được mua thấp hơn số dư nợ gốc, trừ mua theo phương án cơ cấu lại được cấp có thẩm quyền phê duyệt |
| h | Có đơn yêu cầu mở thủ tục phá sản đối với khách hàng |
| i | Khách hàng không thuộc a đến h và ngân hàng đánh giá không có khả năng thanh toán đầy đủ nghĩa vụ theo quy định nội bộ |

**Điều kiện không còn vỡ nợ (Đ36.4a, tối thiểu)** [[src-tt14-2025-nhnn#^d36-4a]]:
- sự kiện b: khách hàng đã thanh toán toàn bộ nghĩa vụ quá hạn và được đánh giá có khả năng thanh toán đúng hạn nghĩa vụ còn trong hạn;
- sự kiện c: ngân hàng hoàn thành xử lý tổn thất, và các khoản còn lại của khách hàng cũng đạt điều kiện thanh toán trên;
- sự kiện d, đ (kéo dài) và g: ngân hàng có quy định về khoảng thời gian xem xét, trên cơ sở khoản phải đòi đã được phân loại vào nhóm nợ không phải nợ xấu;
- sự kiện đ (đổi phương thức thanh toán): khách hàng đã thanh toán nghĩa vụ quá hạn và có khả năng thanh toán nghĩa vụ còn trong hạn;
- sự kiện e: ngân hàng bán nợ đã chuyển giao quyền, nghĩa vụ và hoàn thành xử lý tài chính khoản nợ đã bán; các khoản còn lại của khách hàng đạt điều kiện thanh toán;
- sự kiện h: có quyết định không mở thủ tục phá sản hoặc đình chỉ tiến hành thủ tục phá sản của tòa án, và khách hàng đạt điều kiện thanh toán.

**Quy trình (Đ36.4b–c).** Quy trình, trách nhiệm, thẩm quyền đảm bảo công khai, minh bạch, kiểm soát xung đột lợi ích, cá nhân hoặc bộ phận đánh giá độc lập với cá nhân hoặc bộ phận quyết định; hồ sơ chứng minh việc đáp ứng điều kiện và việc thực hiện quy trình [[src-tt14-2025-nhnn#^d36-4]].

## Phụ thuộc regime
Áp dụng cho ngân hàng dùng IRB. Phân loại nợ nhóm 3 đến 5 theo quy định của NHNN về phân loại tài sản có chưa ingest [cần nguồn].

## Góc nhìn theo domain
**VN Regulator.** Định nghĩa vỡ nợ ở cấp khách hàng (một sự kiện làm mọi khoản phải đòi tại ngân hàng vỡ nợ), không ở cấp khoản vay [[src-tt14-2025-nhnn#^d36-23]]. Sự kiện (d) dùng quyền xem xét gia hạn, cơ cấu lại theo quy định của Chính phủ, Thủ tướng Chính phủ và NHNN [[src-tt14-2025-nhnn#^d36-1]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* sự kiện (e) và (g) chạm vào hoạt động mua bán nợ của Treasury và quản lý tài sản có vấn đề: bán nợ dưới giá trị ghi sổ làm khách hàng vỡ nợ cho cả các khoản còn lại tại ngân hàng, và mua nợ dưới dư nợ gốc tạo khoản phải đòi vỡ nợ. Dữ liệu vỡ nợ vì vậy cần nguồn từ cả hệ thống tín dụng, hệ thống pháp lý và hệ thống mua bán nợ.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Cách ngân hàng xác định sự kiện (i) (không có khả năng thanh toán theo đánh giá nội bộ) phải do quy định nội bộ; nguồn không nêu tiêu chí [cần nguồn] [[src-tt14-2025-nhnn#^d36-1]].
