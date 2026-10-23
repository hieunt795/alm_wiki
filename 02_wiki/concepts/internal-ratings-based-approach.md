---
title: "Internal Ratings-Based Approach"
aliases: [Internal Ratings-Based Approach, IRB, Phương pháp xếp hạng nội bộ, FIRB, AIRB, IRB cơ bản, IRB nâng cao]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[customer-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^d31-2]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Phương pháp xếp hạng nội bộ (IRB) cho rủi ro tín dụng khách hàng là phương pháp tính $RWA_{CR}$ theo Chương III TT14/2025, gồm IRB cơ bản (FIRB) và IRB nâng cao (AIRB) [[src-tt14-2025-nhnn#^d2-27]]. Ngân hàng không bắt buộc áp dụng IRB: Đ7.1 loại Chương III khỏi nghĩa vụ áp dụng từ 01/01/2030, và ngân hàng đăng ký, được chấp thuận khi đủ điều kiện [[src-tt14-2025-nhnn#^d7-1]] [[src-tt14-2025-nhnn#^d7-3a]]. Phương pháp thay thế là phương pháp tiêu chuẩn của Chương II ([[credit-risk-weight]]).

## Cơ chế & drivers
**FIRB và AIRB.**
- FIRB: ngân hàng tự ước tính xác suất vỡ nợ (PD) và dùng các tham số rủi ro khác theo Thông tư, cho khoản phải đòi doanh nghiệp và khoản mua lại khoản phải thu doanh nghiệp [[src-tt14-2025-nhnn#^d2-29]].
- AIRB: ngân hàng tự ước tính PD, tỷ lệ tổn thất khi vỡ nợ (LGD) và giá trị khoản phải đòi tại thời điểm vỡ nợ (EAD), cho khoản phải đòi bán lẻ và khoản mua lại khoản phải thu bán lẻ [[src-tt14-2025-nhnn#^d2-29]].
- Tham số: PD, LGD, EAD, thời hạn hiệu lực M và tổn thất dự kiến EL [[src-tt14-2025-nhnn#^d2-31]]. Xem [[expected-loss]].

**Cấu trúc áp dụng (Đ31).**
- Tài sản chia thành 04 loại: khoản phải đòi doanh nghiệp, khoản phải đòi bán lẻ, khoản mua lại khoản phải thu, tài sản khác; mỗi loại chia nhóm theo Đ37–39, và nhóm chia tiểu nhóm theo quy định nội bộ ([[irb-asset-classes]]) [[src-tt14-2025-nhnn#^d31-1]].
- Ngân hàng được chọn IRB hoặc phương pháp tiêu chuẩn cho từng nhóm, tiểu nhóm. Đã chọn IRB cho một nhóm hoặc tiểu nhóm thì áp dụng cho toàn bộ khoản phải đòi trong đó, trừ khoản bắt buộc dùng phương pháp tiêu chuẩn [[src-tt14-2025-nhnn#^d31-2]].
- Loại tài sản chọn IRB phải đạt tỷ lệ bao phủ tối thiểu 70% ([[irb-coverage-ratio]]) [[src-tt14-2025-nhnn#^d31-3]].
- RWA theo IRB tối thiểu bằng tỷ lệ sàn đầu ra nhân RWA theo phương pháp tiêu chuẩn, tỷ lệ sàn tối thiểu 72,5% ([[output-floor]]) [[src-tt14-2025-nhnn#^d35-12]].

**Hai cách chọn phương pháp theo loại tài sản.**

| Loại tài sản | Phương pháp được chọn | Nguồn |
|---|---|---|
| Khoản phải đòi doanh nghiệp nhỏ và vừa; khoản phải đòi doanh nghiệp khác | Tiêu chuẩn hoặc IRB cơ bản | [[src-tt14-2025-nhnn#^d37-34]] |
| Khoản cấp tín dụng chuyên biệt | Tiêu chuẩn | [[src-tt14-2025-nhnn#^d37-34]] |
| Khoản phải đòi bán lẻ | Tiêu chuẩn hoặc IRB nâng cao | [[src-tt14-2025-nhnn#^d38-56]] |
| Khoản mua lại khoản phải thu doanh nghiệp | Như khoản phải đòi doanh nghiệp | [[src-tt14-2025-nhnn#^d39-2]] |
| Khoản mua lại khoản phải thu bán lẻ | Như khoản phải đòi bán lẻ | [[src-tt14-2025-nhnn#^d39-2]] |
| Tài sản khác | Tiêu chuẩn | [[src-tt14-2025-nhnn#^d40-1]] |

**Chuyển đổi và chấp thuận.** Xem [[irb-approval-process]].

**RWA_CCR.** Trong Chương III, tài sản có rủi ro tín dụng đối tác vẫn tính theo Phụ lục II ([[counterparty-credit-risk-rwa]]) [[src-tt14-2025-nhnn#^d30-23]]. Khoản vỡ nợ tính $RWA_{CR}$ như nợ xấu theo phương pháp tiêu chuẩn ([[customer-default-definition]]) [[src-tt14-2025-nhnn#^d36-23]].

## Phụ thuộc regime
Công thức RWA doanh nghiệp theo PD, LGD, EAD, M (Đ41–48) đã ingest ([[irb-capital-requirement]], [[irb-credit-risk-mitigation]]); công thức bán lẻ ([[irb-retail-parameter-estimation]]) đã ingest; khoản mua lại khoản phải thu ([[purchased-receivables-rwa]]) đã ingest; EL và dự phòng ([[el-provision-difference-treatment]]) đã ingest; yêu cầu tối thiểu của hệ thống xếp hạng nội bộ ([[irb-rating-system-design]], [[irb-model-governance]], [[irb-rating-operation-and-governance]], [[irb-use-test]], [[irb-parameter-estimation-requirements]], [[irb-model-validation]]) đã ingest; kế hoạch triển khai và mẫu đơn xem [[irb-implementation-plan]]. Ngân hàng được chấp thuận IRB trước 01/01/2030 không phải tuân thủ mức tối thiểu tỷ lệ an toàn vốn theo phương pháp tiêu chuẩn của Chương II và dừng thực hiện các Thông tư cũ [[src-tt14-2025-nhnn#^d7-3c]].

## Góc nhìn theo domain
**VN Regulator.** Đ35 đặt sàn 72,5% và Đ31.3 đặt bao phủ 70% đồng thời; ngân hàng phải duy trì cả hai từ ngày được chấp thuận [[src-tt14-2025-nhnn#^d31-4]] [[src-tt14-2025-nhnn#^d35-12]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* IRB đổi RWA theo chất lượng tín dụng ước tính nội bộ, nên RWA nhạy với chu kỳ tín dụng hơn phương pháp tiêu chuẩn. Sàn 72,5% giới hạn mức giảm RWA so với phương pháp tiêu chuẩn: ví dụ số do wiki dựng, RWA_CR theo phương pháp tiêu chuẩn 1.000 tỷ đồng thì RWA_CR theo IRB không thấp hơn 725 tỷ đồng. [[capital-plan]] cần dự phóng RWA theo cả hai phương pháp để theo dõi sàn.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
Chưa có.
