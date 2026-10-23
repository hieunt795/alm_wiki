---
title: "Additional Tier 1 Capital"
aliases: [Additional Tier 1 Capital, AT1, AT1 Capital, Vốn bổ sung vốn cấp 1, Vốn bổ sung cấp 1]
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
tags: [capital, at1, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn bổ sung vốn cấp 1 (A2) cộng với vốn lõi cấp 1 (A1) thành vốn cấp 1 (A) [[src-tt14-2025-nhnn#^pl1-a-struct]]. Vốn bổ sung vốn cấp 1 bằng A21 (chưa giảm trừ) trừ A22 (các khoản giảm trừ) [[src-tt14-2025-nhnn#^pl1-a21]]. Công cụ bổ sung vốn cấp 1 là công cụ tài chính do ngân hàng thương mại phát hành và đáp ứng đầy đủ các điều kiện của Phụ lục I Mục III [[src-tt14-2025-nhnn#^d2-17]], xem [[additional-tier-1-instrument-conditions]].

## Công thức
$$
A_2 = A_{21} - A_{22}
$$
[[src-tt14-2025-nhnn#^pl1-a21]]

| Cấu phần | Khoản mục | Cách xác định | Nguồn |
|---|---|---|---|
| A21, mục (19) | Công cụ bổ sung vốn cấp 1 do chính ngân hàng thương mại phát hành | Giá trị các công cụ đáp ứng đủ điều kiện Mục III | [[src-tt14-2025-nhnn#^pl1-a21]] |
| A21, mục (20) | Thặng dư vốn cổ phần của các công cụ bổ sung vốn cấp 1 | Thặng dư vốn cổ phần nhân tỷ trọng các loại cổ phần không phải cổ phần phổ thông, đáp ứng điều kiện Mục III, trên tổng số cổ phần | [[src-tt14-2025-nhnn#^pl1-a21]] |
| A22, mục (21) | Mua lại công cụ do chính ngân hàng phát hành | Cổ phiếu quỹ theo tỷ trọng các loại cổ phần đủ điều kiện, cộng công cụ không phải cổ phiếu mà ngân hàng mua lại | [[src-tt14-2025-nhnn#^pl1-a22]] |
| A22, mục (22) | Phần bù cho giá trị âm của vốn cấp 2 | Khi B < 0, lấy giá trị giảm trừ là \|B\| | [[src-tt14-2025-nhnn#^pl1-a22]] |

## Diễn giải
**Hợp nhất.** Vốn bổ sung vốn cấp 1 hợp nhất có cùng cấu trúc A21 và A22, tính trên số liệu Báo cáo tình hình tài chính hợp nhất [[src-tt14-2025-nhnn#^pl1-ii-struct]].

**Chi nhánh ngân hàng nước ngoài.** Vốn cấp 1 của chi nhánh chỉ gồm vốn lõi cấp 1 (A = A1), nên chi nhánh không có vốn bổ sung vốn cấp 1 [[src-tt14-2025-nhnn#^pl1-br-struct]].

**Giá trị âm.** Khi A2 nhỏ hơn 0, ngân hàng giảm trừ một khoản bù khỏi vốn lõi cấp 1 (mục (18) của A12) [[src-tt14-2025-nhnn#^pl1-a12-18]]. Ô công thức của mục (18) bị cụt trong raw sau chữ "là". *Diễn giải:* theo mẫu của mục (22), giá trị giảm trừ có thể là giá trị tuyệt đối của A2; wiki chưa khẳng định [cần nguồn: đối chiếu pdf hoặc docx gốc]. Ý nghĩa: vốn bổ sung vốn cấp 1 âm không làm vốn cấp 1 thấp hơn vốn lõi cấp 1.

*Diễn giải:* khoản mục (19) và (20) lấy phần vốn là công cụ nợ kế toán và cổ phần ưu đãi đủ điều kiện, tách khỏi (9) của vốn lõi cấp 1 nhờ tỷ trọng cổ phần phổ thông [[src-tt14-2025-nhnn#^pl1-a11-9]]. Cùng một thặng dư vốn cổ phần được chia hai phần theo loại cổ phần.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu trúc | AT1 theo CAP10 [cần nguồn] (CAP10 chưa ingest); LEV20.4 xác nhận Tier 1 = CET1 và/hoặc AT1 [[src-bcbs-lev#^lev20-4]] | A2 = A21 − A22 [[src-tt14-2025-nhnn#^pl1-a21]] | PL1.A.I | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Chi nhánh ngân hàng nước ngoài | [cần nguồn] | Không có AT1 [[src-tt14-2025-nhnn#^pl1-br-struct]] | PL1.B | Như trên |
| Điều kiện công cụ | [cần nguồn] | 13 điều kiện ([[additional-tier-1-instrument-conditions]]) [[src-tt14-2025-nhnn#^pl1-iii-1]] | PL1.A.III | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* AT1 là nguồn vốn cấp 1 không cần tăng vốn cổ phần phổ thông, nhưng điều kiện Mục III (hủy chi trả linh hoạt, cơ chế bù đắp lỗ khi vốn lõi cấp 1 dưới 5,125%) làm công cụ khó phát hành và khó định giá. Ngân hàng, công ty con và công ty liên kết không được mua công cụ, và ngân hàng không được cấp tín dụng để mua [[src-tt14-2025-nhnn#^pl1-iii-12]]. Với [[contingent-convertible-bond]], xem phần so sánh trong [[additional-tier-1-instrument-conditions]].

## Nhầm lẫn thường gặp
- Thặng dư vốn cổ phần không tự động thuộc vốn lõi cấp 1. Chỉ phần tỷ trọng cổ phần phổ thông thuộc A11 mục (9) [[src-tt14-2025-nhnn#^pl1-a11-9]].
- Chi nhánh ngân hàng nước ngoài không có vốn bổ sung vốn cấp 1 [[src-tt14-2025-nhnn#^pl1-br-struct]].
