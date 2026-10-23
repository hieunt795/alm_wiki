---
title: "Countercyclical Capital Buffer"
aliases: [Countercyclical Capital Buffer, CCyB, Bộ đệm vốn phản chu kỳ, Tỷ lệ bộ đệm vốn phản chu kỳ]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[capital-adequacy-ratio]]", cite: "[[src-tt14-2025-nhnn#^d5-6]]"}
tags: [capital, buffer, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tỷ lệ bộ đệm vốn phản chu kỳ (Countercyclical capital buffer, CCyB) là phần tỷ lệ vốn lõi cấp 1 còn lại sau khi ngân hàng đáp ứng đầy đủ tỷ lệ vốn lõi cấp 1, tỷ lệ vốn cấp 1, tỷ lệ an toàn vốn và [[capital-conservation-buffer]] (nếu có) [[src-tt14-2025-nhnn#^d5-6]]. Ngân hàng thực hiện CCyB ngoài các tỷ lệ tại Đ5.3, Đ5.4 và Đ5.5 [[src-tt14-2025-nhnn#^d5-6]].

## Công thức
Thống đốc NHNN quyết định áp dụng tỷ lệ CCyB cụ thể trong khoảng từ 0% đến 2,5% khi cần thiết trong từng thời kỳ [[src-tt14-2025-nhnn#^d5-6]]. TT14/2025 không nêu tiêu chí hay chỉ báo để Thống đốc chọn mức [cần nguồn: quy định khác ngoài C1].

| Tham số | Giá trị | Nguồn |
|---|---|---|
| Khoảng tỷ lệ | 0%–2,5% | [[src-tt14-2025-nhnn#^d5-6]] |
| Người quyết định | Thống đốc NHNN | [[src-tt14-2025-nhnn#^d5-6]] |
| Thời điểm | Khi cần thiết trong từng thời kỳ | [[src-tt14-2025-nhnn#^d5-6]] |

## Diễn giải
*Diễn giải:* khoảng 0%–2,5% và việc xếp sau CCB làm tổng yêu cầu vốn lõi cấp 1 có thể lên tới 4,5% + 2,5% + 2,5% = 9,5% khi CCB đầy đủ và CCyB ở mức tối đa. Con số này là phép cộng của wiki trên các mức của Đ5.3, Đ5.5b và Đ5.6, Thông tư không nêu tổng này. Thông tư cũng không nêu hậu quả cụ thể của việc không đáp ứng CCyB trong C1 [cần nguồn].

Ngoài CCyB, NHNN có thể quyết định áp tỷ lệ bộ đệm vốn đối với ngân hàng thương mại có tầm quan trọng hệ thống trong từng thời kỳ [[src-tt14-2025-nhnn#^d5-8]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Khoảng CCyB | [cần nguồn] (RBC30 chưa ingest) | 0%–2,5% [[src-tt14-2025-nhnn#^d5-6]] | Đ5.6b | Theo từng thời kỳ |
| Cơ quan quyết định | [cần nguồn] | Thống đốc NHNN [[src-tt14-2025-nhnn#^d5-6]] | Đ5.6b | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* CCyB do Thống đốc quyết định theo từng thời kỳ nên kế hoạch vốn ([[capital-plan]]) cần có kịch bản với mức CCyB khác 0%. Xem [[capital-adequacy-management]].

## Nhầm lẫn thường gặp
- CCyB không phải mức cố định: giá trị thay đổi theo quyết định của Thống đốc trong khoảng 0%–2,5% [[src-tt14-2025-nhnn#^d5-6]].
