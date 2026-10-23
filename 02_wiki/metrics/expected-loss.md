---
title: "Expected Loss"
aliases: [Expected Loss, Tổn thất dự kiến, Unexpected Loss, Tổn thất ngoài dự kiến]
type: metric
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations:
  - {type: input-to, to: "[[raroc]]", cite: "[[src-choudhry-principles-banking#^choudhry-crd-6]]"}
tags: [credit-risk, capital]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
Expected loss (EL) là tổn thất tín dụng dự kiến của tài sản hoặc danh mục, xác định từ xác suất vỡ nợ (PD) và tổn thất khi vỡ nợ (LGD). Mô hình danh mục dùng PD và LGD (LGD = 100 − recovery rate), cùng tham số thứ ba là tương quan vỡ nợ [[src-choudhry-principles-banking#^choudhry-crd-2]].

Cách TT14/2025 dùng EL trong IRB (EL = PD × LGD × EAD so với dự phòng rủi ro) nằm ở [[irb-expected-loss]].

## Công thức
*Diễn giải (tái dựng, chưa đối chiếu bản gốc):* Table 19.3 của Choudhry cho thấy với từng tài sản, EL = notional loss × default probability, trong đó notional loss = notional × LGD. Kiểm bằng dòng 1 (San Pedro Finance): 6 triệu × 0,75% = 45.000, khớp cột £EL của raw.

$$EL_i = N_i \times LGD_i \times PD_i$$
[[src-choudhry-principles-banking#^choudhry-crd-2]]

Vốn cho danh mục trong ví dụ của Choudhry lấy từ phân phối tổn thất:

$$C(95) = L(95\%) - EL$$
[[src-choudhry-principles-banking#^choudhry-crd-6]]

| Chỉ tiêu (danh mục mẫu £255 triệu) | Giá trị | Nguồn |
|---|---|---|
| EL | 0,63% danh nghĩa (£1,612 triệu) | [[src-choudhry-principles-banking#^choudhry-crd-5]] |
| L(95%) | £16,05 triệu (6,29% danh nghĩa) | [[src-choudhry-principles-banking#^choudhry-crd-5]] |
| C(95) | £14,438 triệu (5,66%) | [[src-choudhry-principles-banking#^choudhry-crd-6]] |
| Aggregate UL | £14.557.003 | [[src-choudhry-principles-banking#^choudhry-crd-6]] |

## Diễn giải
- Vốn phân bổ theo C(95) phục vụ phân tích lợi nhuận, không phải vốn quy định [[src-choudhry-principles-banking#^choudhry-crd-6]].
- Phân bổ vốn đơn giản nhất cho từng tài sản dùng standalone loss volatility (LV); cộng gộp LV là cách tiếp cận thận trọng [[src-choudhry-principles-banking#^choudhry-crd-7]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Định nghĩa EL trong vốn quy định | [cần nguồn] | [cần nguồn] | | |

## Ứng dụng trong ALM
- Hạn mức EL theo bên vay, ngành, quốc gia, đồng tiền buộc người quản lý tín dụng đánh giá lợi nhuận điều chỉnh rủi ro; hạn mức LV là kỷ luật về sử dụng vốn [[src-choudhry-principles-banking#^choudhry-crd-9]]. Xem [[risk-limits]].
- EL là đầu vào của [[raroc]] và [[shareholder-value-added]] [[src-choudhry-principles-banking#^choudhry-crd-6]].

## Nhầm lẫn thường gặp
- EL của mô hình danh mục khác ECL theo IFRS 9: IFRS 9 thay incurred loss bằng expected credit loss, nên gần như mọi tài sản có dự phòng từ ngày đầu ghi nhận [[src-choudhry-principles-banking#^choudhry-ecl-2]]. Xem [[expected-credit-loss]], [[credit-risk-management]].
