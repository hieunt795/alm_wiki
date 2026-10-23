---
title: "IRB Expected Loss"
aliases: [IRB Expected Loss, Tổn thất dự kiến theo IRB, EL theo TT14]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[el-provision-difference-treatment]]", cite: "[[src-tt14-2025-nhnn#^d62-1]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tổn thất dự kiến (EL) theo TT14/2025 là tổng tổn thất dự kiến của các khoản phải đòi được tính tài sản có rủi ro khách hàng theo phương pháp xếp hạng nội bộ [[src-tt14-2025-nhnn#^d60-12]]. EL là phần tổn thất ngân hàng dự kiến sẽ xảy ra [[src-tt14-2025-nhnn#^d2-31]]. Khái niệm chung về expected loss trong quản trị danh mục tín dụng xem [[expected-loss]]; EL theo kế toán IFRS 9 là [[expected-credit-loss]], khác phạm vi.

## Công thức
$$
EL = PD \times LGD \times EAD
$$
[[src-tt14-2025-nhnn#^d60-12]]

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $PD$ | Xác suất vỡ nợ | [[probability-of-default]] | [[src-tt14-2025-nhnn#^d60-12]] |
| $LGD$ | Tỷ lệ tổn thất khi vỡ nợ | [[loss-given-default]] | [[src-tt14-2025-nhnn#^d60-12]] |
| $EAD$ | Giá trị khoản phải đòi tại thời điểm vỡ nợ | [[exposure-at-default]] | [[src-tt14-2025-nhnn#^d60-12]] |

Tính cho từng khoản phải đòi rồi cộng lại, với PD, LGD, EAD xác định theo Chương III [[src-tt14-2025-nhnn#^d60-12]].

## Diễn giải
EL là một vế của phép so sánh với [[irb-risk-provisions]]; chênh lệch hai vế đi vào vốn tự có theo [[el-provision-difference-treatment]] [[src-tt14-2025-nhnn#^d62-1]]. Công thức K của IRB đã trừ $PD \times LGD$ khỏi tổn thất ở phân vị 99,9% ([[irb-capital-requirement]]), nên EL không nằm trong yêu cầu vốn K mà được xử lý qua dự phòng. *Diễn giải:* đây là cách đọc từ dạng công thức K, nguồn TT14 không nói rõ lý do [cần nguồn Basel CRE35].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| EL từng khoản | [cần nguồn] (CRE chưa ingest) | $PD \times LGD \times EAD$ [[src-tt14-2025-nhnn#^d60-12]] | Đ60.2 | Khi được NHNN chấp thuận IRB |

## Ứng dụng trong ALM
*Diễn giải:* EL theo IRB dùng cùng tham số với RWA nên thay đổi PD, LGD hoặc EAD đổi cả RWA lẫn mức dự phòng cần có để tránh khoản trừ vốn.

## Nhầm lẫn thường gặp
- EL ở đây không phải dự phòng kế toán và không tính cho khoản dùng phương pháp tiêu chuẩn; chỉ khoản được tính RWA theo IRB [[src-tt14-2025-nhnn#^d60-12]].
