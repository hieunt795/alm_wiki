---
title: "Capital Conservation Buffer"
aliases: [Capital Conservation Buffer, CCB, Bộ đệm bảo toàn vốn, Tỷ lệ bộ đệm bảo toàn vốn]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[capital-adequacy-ratio]]", cite: "[[src-tt14-2025-nhnn#^d5-5a]]"}
tags: [capital, buffer, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tỷ lệ bộ đệm bảo toàn vốn (Capital conservation buffer, CCB) là phần tỷ lệ vốn lõi cấp 1 còn lại sau khi ngân hàng đáp ứng đầy đủ tỷ lệ vốn lõi cấp 1, tỷ lệ vốn cấp 1 và tỷ lệ an toàn vốn [[src-tt14-2025-nhnn#^d5-5a]]. Ngân hàng thực hiện CCB ngoài các tỷ lệ bắt buộc tại Đ5.3 và Đ5.4 [[src-tt14-2025-nhnn#^d5-5a]]. Mức tối thiểu của ba tỷ lệ xem [[capital-adequacy-ratio]].

## Công thức
CCB không có công thức riêng trong Đ5. CCB là phần vốn lõi cấp 1 vượt các mức tối thiểu, và Thông tư quy định mức CCB phải duy trì theo từng năm [[src-tt14-2025-nhnn#^d5-5b]].

| Thời điểm áp dụng từ | Năm thứ nhất | Năm thứ hai | Năm thứ ba | Năm thứ tư trở đi | Nguồn |
|---|---|---|---|---|---|
| CCB | 0,625% | 1,25% | 1,875% | 2,5% | [[src-tt14-2025-nhnn#^d5-5b]] |
| Vốn lõi cấp 1 (gồm CCB) | 5,125% | 5,75% | 6,375% | 7% | [[src-tt14-2025-nhnn#^d5-5b]] |
| Vốn cấp 1 (gồm CCB) | 6,625% | 7,25% | 7,875% | 8,5% | [[src-tt14-2025-nhnn#^d5-5b]] |
| CAR (gồm CCB) | 8,625% | 9,25% | 9,875% | 10,5% | [[src-tt14-2025-nhnn#^d5-5b]] |

Năm thứ nhất là một trong ba trường hợp [[src-tt14-2025-nhnn#^d5-5c]]:
- năm ngân hàng bắt đầu áp dụng phương pháp tiêu chuẩn đã đăng ký theo Đ7.2b;
- năm ngân hàng được NHNN chấp thuận áp dụng IRB theo Đ7.3c;
- năm 2030 đối với các trường hợp còn lại.

## Diễn giải
Ngân hàng chỉ được phân chia phần lợi nhuận còn lại do ngân hàng tự quyết định, bằng tiền mặt, khi duy trì việc đáp ứng toàn bộ các tỷ lệ của bảng trên theo từng năm [[src-tt14-2025-nhnn#^d5-5b]].

*Diễn giải:* mỗi dòng "gồm CCB" bằng mức tối thiểu cộng CCB của năm đó (ví dụ 4,5% + 0,625% = 5,125%; 8% + 2,5% = 10,5%) nên bảng nhất quán với Đ5.3 [[src-tt14-2025-nhnn#^d5-3]]. Ngân hàng đăng ký phương pháp tiêu chuẩn sớm bắt đầu lộ trình CCB từ năm bắt đầu áp dụng đã đăng ký; ngân hàng không thuộc hai trường hợp đầu bắt đầu từ 2030 và đạt 2,5% vào năm 2033 (đếm theo năm thứ tư).

*Diễn giải:* [[capital-plan]] và [[projected-own-funds]] theo TT83/2025 phải bảo đảm vốn tự có dự kiến sau cổ tức không thấp hơn vốn mục tiêu [[src-tt83-2025-nhnn#^d61-1]]. Điều kiện chia lợi nhuận bằng tiền mặt của CCB là một ràng buộc thêm lên chính sách cổ tức.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Mức CCB đầy đủ | [cần nguồn] (RBC30 chưa ingest) | 2,5% từ năm thứ tư [[src-tt14-2025-nhnn#^d5-5b]] | Đ5.5b | Năm thứ nhất theo Đ5.5b [[src-tt14-2025-nhnn#^d5-5c]] |
| Lộ trình tăng dần | [cần nguồn] | 0,625% → 1,25% → 1,875% → 2,5% [[src-tt14-2025-nhnn#^d5-5b]] | Đ5.5b | Như trên |
| Hậu quả khi thiếu | [cần nguồn] | Chỉ được chia phần lợi nhuận còn lại bằng tiền mặt khi đáp ứng toàn bộ các tỷ lệ của bảng [[src-tt14-2025-nhnn#^d5-5b]] | Đ5.5b | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* CCB đẩy mức vốn lõi cấp 1 cần duy trì lên 7% sau năm thứ tư. ALCO và Treasury cần đưa mức này vào kế hoạch tăng trưởng RWA và chính sách cổ tức. Xem [[capital-adequacy-management]].

## Nhầm lẫn thường gặp
- CCB là phần vượt mức tối thiểu, không phải một tỷ lệ tối thiểu thay thế [[src-tt14-2025-nhnn#^d5-5a]].
- Ràng buộc của CCB nằm ở việc phân chia lợi nhuận bằng tiền mặt, không nằm ở việc cấm hoạt động tín dụng [[src-tt14-2025-nhnn#^d5-5b]].
