---
title: "EL vs Provision Difference Treatment"
aliases: [EL vs Provision Difference Treatment, Xử lý chênh lệch giữa tổn thất dự kiến và dự phòng rủi ro, Shortfall và excess provision IRB]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[internal-ratings-based-approach]]", cite: "[[src-tt14-2025-nhnn#^d62-1]]"}
tags: [capital, credit-risk, irb, provisions, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Ngân hàng áp dụng IRB so sánh [[irb-expected-loss]] (Đ60) với [[irb-risk-provisions]] (Đ61) và xử lý chênh lệch qua vốn tự có (Đ62). Thiếu dự phòng so với EL thì bị trừ vốn; thừa thì được cộng vào vốn cấp 2 có trần [[src-tt14-2025-nhnn#^d62-1]] [[src-tt14-2025-nhnn#^d62-2]]. Xem [[own-funds]].

## Cơ chế & drivers
| Trường hợp | Xử lý | Nguồn |
|---|---|---|
| Dự phòng rủi ro < EL, 02 năm kể từ ngày NHNN chấp thuận IRB | Trừ 50% chênh lệch vào [[common-equity-tier-1-capital]] và 50% còn lại vào [[tier-2-capital]] | [[src-tt14-2025-nhnn#^d62-1]] |
| Dự phòng rủi ro < EL, từ năm thứ ba | Trừ toàn bộ chênh lệch vào vốn lõi cấp 1 | [[src-tt14-2025-nhnn#^d62-1]] |
| Dự phòng rủi ro > EL | Được xem xét cộng chênh lệch vào vốn cấp 2, tối đa 0,6% giá trị tài sản có rủi ro tín dụng khách hàng tính theo IRB | [[src-tt14-2025-nhnn#^d62-2]] |

Phụ lục I phản ánh cùng quy tắc: khoản mục (25) là phần chênh lệch dương giữa dự phòng rủi ro và EL của danh mục IRB, và khoản giảm trừ (27) là phần chênh lệch dương giữa (25) và 0,6% tổng tài sản có rủi ro tín dụng khách hàng của danh mục IRB [[src-tt14-2025-nhnn#^pl1-b-irb]] [[src-tt14-2025-nhnn#^pl1-b2-cap]]. Xem [[capital-deductions]].

## Phụ thuộc regime
Chỉ áp dụng cho danh mục IRB. Danh mục phương pháp tiêu chuẩn dùng trần dự phòng chung 1,25% [[src-tt14-2025-nhnn#^pl1-b2-cap]]. Điều khoản chuyển tiếp "02 năm" tính từ ngày chấp thuận ([[irb-approval-process]]).

## Góc nhìn theo domain
**VN Regulator.** Tỷ lệ trừ chuyển từ 50% / 50% (hai năm đầu) sang 100% vốn lõi cấp 1 từ năm thứ ba, làm khoản thiếu dự phòng nặng dần về chất lượng vốn [[src-tt14-2025-nhnn#^d62-1]].

**Basel.** [cần nguồn] (CRE35 chưa ingest).

**ALM.** *Diễn giải:* khoản thiếu dự phòng so với EL trừ thẳng vốn, nên trích lập thêm dự phòng có thể rẻ hơn về vốn so với để thiếu. Từ năm thứ ba mỗi đồng thiếu hụt trừ 1:1 vốn lõi cấp 1. Phần thừa chỉ cộng vốn cấp 2 tới 0,6% nên dự phòng vượt xa EL không tạo thêm vốn.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Cách tính 50% phần chênh lệch "còn lại" giữa vốn lõi cấp 1 và vốn cấp 2 khi vốn cấp 2 không đủ để trừ: nguồn không nêu [cần nguồn].
