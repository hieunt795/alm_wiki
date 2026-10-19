---
title: "Contingent Convertible Bond"
aliases: [Contingent Convertible Bond, CoCo bond, Contingent capital, Hybrid capital instrument, Trái phiếu chuyển đổi có điều kiện, Công cụ vốn lai]
type: instrument
domains: [product, basel]
status: active
maturity: draft
sources: ["[[src-choudhry-principles-banking]]"]
relations:
  - {type: input-to, to: "[[capital-plan]]", cite: "[[src-choudhry-principles-banking#^choudhry-capm-27]]"}
tags: [capital, tier-1, hybrid, loss-absorbency]
updated: 2026-10-19
reviewed:
---

## Định nghĩa & cashflow
CoCo bond là trái phiếu tự chuyển thành cổ phần khi tỷ lệ Tier 1 của tổ chức phát hành giảm xuống một mức định trước. Coupon cao vì công cụ này gần với vốn cổ phần hơn nợ; Choudhry gọi nó là một đợt phát hành quyền mua cổ phần được tài trợ trước (prefunded rights share issue) [[src-choudhry-principles-banking#^choudhry-coco-4]].

CoCo là một dạng hybrid capital instrument. Bài học sau khủng hoảng 2008 là đệm vốn và hybrid bổ sung cho core Tier 1 phải hấp thụ lỗ khi ngân hàng vẫn hoạt động liên tục (going concern): coupon có thể bị huỷ, gốc có thể bị ghi giảm mà ngân hàng không phải dừng hoạt động [[src-choudhry-principles-banking#^choudhry-coco-1]]. Vì vậy Choudhry khuyên ngân hàng phát hành contingent core Tier 1 có thể chuyển thành cổ phần tại các điểm định trước [[src-choudhry-principles-banking#^choudhry-coco-1]].

Ví dụ Lloyds Banking Group Enhanced Capital Notes (ECN, 2009) [[src-choudhry-principles-banking#^choudhry-coco-4]]:

| Thông số | Giá trị | Nguồn |
|---|---|---|
| Quy mô | 13,5 tỷ GBP | [[src-choudhry-principles-banking#^choudhry-coco-4]] |
| Coupon | 12% | [[src-choudhry-principles-banking#^choudhry-coco-4]] |
| Kỳ hạn | 10 năm | [[src-choudhry-principles-banking#^choudhry-coco-4]] |
| Trigger | Tier 1 ratio xuống 5% | [[src-choudhry-principles-banking#^choudhry-coco-4]] |
| Giá chuyển đổi | 50% mệnh giá phát hành | [[src-choudhry-principles-banking#^choudhry-coco-4]] |

## Pricing
Khả năng hấp thụ lỗ phải theo quyết định của tổ chức phát hành, không chỉ đến từ việc xếp sau các khoản nợ khác. Khi bị kích hoạt, lỗ được hấp thụ ngang với core Tier 1, nên trên thực tế không còn thứ bậc giữa hybrid và cổ phần thường. Do đó hybrid phải trả coupon tương đối đắt [[src-choudhry-principles-banking#^choudhry-coco-3]]. Choudhry đánh giá contingent capital là công cụ đáng dùng trong quản trị và kế hoạch vốn, dù đắt [[src-choudhry-principles-banking#^choudhry-coco-4]].

## Risk factors & sensitivities
*Diễn giải:* rủi ro chính với nhà đầu tư là trigger Tier 1 và việc huỷ coupon theo quyết định của tổ chức phát hành; giá trị CoCo vì vậy nhạy với tỷ lệ vốn của ngân hàng, không chỉ với lãi suất và credit spread. Nguồn đã ingest không định lượng các độ nhạy này [cần nguồn].

## ALM & hedging usage
- Ngân hàng đang nhắm một mức Tier 1 vào một thời điểm định trước có thể cân nhắc CoCo, nếu nhà đầu tư có nhu cầu [[src-choudhry-principles-banking#^choudhry-coco-4]].
- Trong chuỗi capital strategy, target core Tier 1 được đặt sau khi đã phân bổ vốn cho các mảng; CoCo có thể hỗ trợ bước cuối này [[src-choudhry-principles-banking#^choudhry-capm-27]]. Xem [[capital-plan]].
- Theo Choudhry, về lý thuyết hybrid có vai trò trong việc tích luỹ countercyclical capital buffer của Basel III [[src-choudhry-principles-banking#^choudhry-coco-2]].

## Kế toán
Nguồn đã ingest không đề cập [cần nguồn].

## Basel treatment
- Wiki chưa ingest tiêu chí Basel III cho Additional Tier 1 và Tier 2 [cần nguồn].
- **UK FSA (trước Basel III, theo Choudhry)**: hybrid được chiếm tối đa 15%, 35% hoặc 50% Tier 1 tuỳ loại [[src-choudhry-principles-banking#^choudhry-coco-2]]:

| Nhóm | Điều kiện | Nguồn |
|---|---|---|
| 50% | Công cụ chuyển đổi theo quyết định của ngân hàng hoặc cơ quan quản lý vào bất kỳ lúc nào; không gồm convertible có quyền call | [[src-choudhry-principles-banking#^choudhry-coco-2]] |
| 35% | Hybrid hấp thụ lỗ going concern (ghi giảm hoặc chuyển đổi), không có ưu đãi mua lại như coupon step-up | [[src-choudhry-principles-banking#^choudhry-coco-2]] |
| 15% | Hybrid hấp thụ lỗ going concern có ưu đãi mua lại; hybrid phát hành qua SPV | [[src-choudhry-principles-banking#^choudhry-coco-2]] |

## Lưu ý tại VN
Nguồn VN đã ingest không quy định công cụ vốn chuyển đổi có điều kiện [cần nguồn]. Kế hoạch vốn theo TT83/2025 Đ61 có nội dung tăng vốn, xem [[capital-plan]].
