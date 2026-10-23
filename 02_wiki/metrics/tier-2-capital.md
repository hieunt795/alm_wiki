---
title: "Tier 2 Capital"
aliases: [Tier 2 Capital, Tier 2, Vốn cấp 2]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[own-funds]]", cite: "[[src-tt14-2025-nhnn#^pl1-a-struct]]"}
tags: [capital, tier-2, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn cấp 2 (B) cộng với vốn cấp 1 (A) thành vốn tự có (C) [[src-tt14-2025-nhnn#^pl1-a-struct]]. Vốn cấp 2 bằng B1 (chưa giảm trừ) trừ B2 (các khoản giảm trừ) [[src-tt14-2025-nhnn#^pl1-b-struct]]. Xem [[own-funds]].

## Công thức
$$
B = B_1 - B_2
$$
[[src-tt14-2025-nhnn#^pl1-b-struct]]

B1 là tổng ba khoản mục (23)–(25). B2 là tổng bốn khoản mục (26)–(29) [[src-tt14-2025-nhnn#^pl1-b-struct]].

| Mục | Khoản mục | Cách xác định | Nguồn |
|---|---|---|---|
| (23) | Nợ thứ cấp đủ điều kiện | Toàn bộ nếu thời hạn còn lại trên 05 năm; từ năm thứ năm trước khi đáo hạn, mỗi năm khấu trừ 20% tổng mệnh giá. Xem [[subordinated-debt]] | [[src-tt14-2025-nhnn#^pl1-b-sd-amort]] |
| (24) | 80% dự phòng chung của danh mục áp dụng phương pháp tiêu chuẩn | 80% tổng các khoản mục Dự phòng chung | [[src-tt14-2025-nhnn#^pl1-b-gp]] |
| (25) | Phần chênh lệch dương giữa dự phòng rủi ro và tổn thất dự kiến của danh mục IRB | Chỉ áp dụng cho danh mục theo khoản 2 Đ62 | [[src-tt14-2025-nhnn#^pl1-b-irb]] |
| (26) | Phần chênh lệch dương giữa (24) và 1,25% Tổng tài sản có rủi ro tín dụng khách hàng | Chỉ danh mục áp dụng phương pháp tiêu chuẩn; giảm trừ | [[src-tt14-2025-nhnn#^pl1-b2-cap]] |
| (27) | Phần chênh lệch dương giữa (25) và 0,6% Tổng tài sản có rủi ro tín dụng khách hàng | Chỉ danh mục IRB; giảm trừ | [[src-tt14-2025-nhnn#^pl1-b2-cap]] |
| (28) | 50% chênh lệch dương của tổn thất dự kiến so với dự phòng của danh mục IRB | Chỉ trong 02 năm kể từ ngày được NHNN chấp thuận IRB; giảm trừ | [[src-tt14-2025-nhnn#^pl1-b2-28]] |
| (29) | Mua, đầu tư nợ thứ cấp của tổ chức tín dụng khác | Khấu trừ 20% tổng giá mua mỗi năm từ năm thứ năm trước khi đáo hạn | [[src-tt14-2025-nhnn#^pl1-b2-29]] |

## Diễn giải
**Trần của dự phòng.** Phần dự phòng chung của danh mục phương pháp tiêu chuẩn vượt 1,25% tổng tài sản có rủi ro tín dụng khách hàng bị giảm trừ khỏi vốn cấp 2 (mục (26)) [[src-tt14-2025-nhnn#^pl1-b2-cap]]. Phần dự phòng vượt tổn thất dự kiến của danh mục IRB vượt 0,6% bị giảm trừ (mục (27)) [[src-tt14-2025-nhnn#^pl1-b2-cap]]. *Diễn giải:* hai khoản giảm trừ này tạo trần 1,25% và 0,6% cho mục (24) và (25).

**Giá trị âm.** Khi B < 0, lấy giá trị giảm trừ là |B| và trừ vào vốn bổ sung vốn cấp 1 (mục (22) của A22) [[src-tt14-2025-nhnn#^pl1-a22]]. *Diễn giải:* vốn cấp 2 âm vì vậy không kéo vốn tự có thấp hơn vốn cấp 1 trừ phần bù.

Khoản mục (25) và (27) áp dụng quy tắc Đ62.2 về dự phòng vượt tổn thất dự kiến của danh mục IRB, xem [[el-provision-difference-treatment]].

**Hợp nhất.** B1 hợp nhất là tổng bốn khoản mục (24)–(27), thêm (27) lợi ích cổ đông không kiểm soát [[src-tt14-2025-nhnn#^pl1-ii-mi]]. Hai trần 1,25% và 0,6% giữ nguyên ở các khoản giảm trừ hợp nhất (28), (29) [[src-tt14-2025-nhnn#^pl1-ii-caps]].

**Chi nhánh ngân hàng nước ngoài.** Chi nhánh có vốn cấp 2 với cấu trúc B = B1 − B2 như ngân hàng thương mại, B1 là tổng khoản mục (16)–(18) [[src-tt14-2025-nhnn#^pl1-br-struct]]. Chi nhánh trừ chênh lệch dương của tổn thất dự kiến so với dự phòng theo cùng lịch 50% / 50% trong 02 năm đầu [[src-tt14-2025-nhnn#^pl1-br-13]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu trúc | [cần nguồn] (CAP10 chưa ingest) | B = B1 − B2 [[src-tt14-2025-nhnn#^pl1-b-struct]] | PL1.A.I | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Khấu trừ nợ thứ cấp theo thời hạn | [cần nguồn] | 20% tổng mệnh giá mỗi năm từ năm thứ năm trước khi đáo hạn [[src-tt14-2025-nhnn#^pl1-b-sd-amort]] | PL1.A.I (23) | Như trên |
| Trần dự phòng chung, phương pháp tiêu chuẩn | [cần nguồn] | 1,25% tài sản có rủi ro tín dụng khách hàng [[src-tt14-2025-nhnn#^pl1-b2-cap]] | PL1.A.I (26) | Như trên |
| Trần dự phòng vượt EL, IRB | [cần nguồn] | 0,6% tài sản có rủi ro tín dụng khách hàng [[src-tt14-2025-nhnn#^pl1-b2-cap]] | PL1.A.I (27) | Như trên |
| Vốn cấp 2 trong ASF của NSFR | Loại phần công cụ Tier 2 có kỳ hạn còn lại dưới 1 năm [[src-bcbs-nsfr#^nsf30-10]] | Theo kỳ hạn còn lại: 0% / 50% / 100% [[src-tt50-2026-nhnn#^pl2-a2-1]] | TT50 PL2 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |

## Ứng dụng trong ALM
*Diễn giải:* nợ thứ cấp còn lại dưới 05 năm giảm dần giá trị tính vào vốn cấp 2 mỗi năm 20% mệnh giá [[src-tt14-2025-nhnn#^pl1-b-sd-amort]]. Kế hoạch huy động nợ thứ cấp cần thay thế phần bị khấu trừ trước khi đáo hạn để giữ tỷ lệ an toàn vốn. Cách tính hệ số ASF cho phần này theo TT50 khác cách khấu trừ của TT14, xem [[asf-capital-and-long-term-liabilities]].

## Nhầm lẫn thường gặp
- Dự phòng chung không tính toàn bộ vào vốn cấp 2: chỉ 80%, và còn bị trần 1,25% tài sản có rủi ro tín dụng khách hàng [[src-tt14-2025-nhnn#^pl1-b-gp]] [[src-tt14-2025-nhnn#^pl1-b2-cap]].
- Khoản mục (28) chỉ áp dụng trong 02 năm đầu sau khi được chấp thuận IRB; từ năm thứ ba không áp dụng [[src-tt14-2025-nhnn#^pl1-b2-28]].
