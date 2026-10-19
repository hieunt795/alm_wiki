---
title: "Shareholder Value Added"
aliases: [Shareholder Value Added, SVA, Giá trị gia tăng cho cổ đông]
type: metric
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [performance, capital, pricing]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
Shareholder value added (SVA) là doanh thu spread kỳ vọng của danh mục trừ chi phí vốn [[src-choudhry-principles-banking#^choudhry-crd-6]]. SVA xét cả [[expected-loss]] và cost of capital (CoC) [[src-choudhry-principles-banking#^choudhry-crd-11]].

## Công thức
$$SVA = (Spread - EL) - CoC \times Capital$$
[[src-choudhry-principles-banking#^choudhry-crd-6]]

$$SVA_{unit} = \frac{SVA}{N}$$
[[src-choudhry-principles-banking#^choudhry-crd-11]]

| Chỉ tiêu (danh mục mẫu) | Giá trị | Nguồn |
|---|---|---|
| CoC giả định | 10% | [[src-choudhry-principles-banking#^choudhry-crd-6]] |
| SVA (theo C(ES)) | £522.300 | [[src-choudhry-principles-banking#^choudhry-crd-11]] |
| SVA trên một đơn vị phơi nhiễm | 522.300 / 255.000.000 = 0,20% | [[src-choudhry-principles-banking#^choudhry-crd-11]] |

## Diễn giải
- Choudhry coi SVA trên một đơn vị phơi nhiễm danh mục là thước đo phù hợp nhất; tài sản mới nên vượt mức bình quân này [[src-choudhry-principles-banking#^choudhry-crd-11]].
- RoA không có mức hoà vốn để so sánh, còn RoC hoặc [[raroc]] nên luôn cao hơn CoC; CoC là hurdle rate cho mọi hoạt động [[src-choudhry-principles-banking#^choudhry-crd-10]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| SVA | Không phải chỉ tiêu quy định [cần nguồn] | [cần nguồn] | | |

## Ứng dụng trong ALM
- Ngân hàng nên tạo tài sản có SVA cao nhất, với điều kiện các yếu tố khác như nhau [[src-choudhry-principles-banking#^choudhry-crd-11]].
- Tài sản có SVA thấp hơn bình quân danh mục có thể đang bị định giá thấp; SVA âm là ứng viên bán bớt [[src-choudhry-principles-banking#^choudhry-crd-11]].
- Tài sản có thể bị bán, chứng khoán hoá hay phòng ngừa khi không còn đạt yêu cầu RoC hoặc SVA, không chỉ khi là nợ xấu [[src-choudhry-principles-banking#^choudhry-crd-8]]. Xem [[loan-pricing]].

## Nhầm lẫn thường gặp
- *Diễn giải:* SVA là số tuyệt đối và phụ thuộc vào cách đo vốn (L(95%), C(95) hay C(ES)); RAROC là tỷ lệ. Hai chỉ tiêu có thể xếp hạng tài sản khác nhau.
