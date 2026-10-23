---
title: "Horizontal Disallowance"
aliases: [Horizontal Disallowance, HD, Vốn bù đắp rủi ro khớp trạng thái trong cùng vùng và giữa các vùng]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[general-interest-rate-risk-capital]]", cite: "[[src-tt14-2025-nhnn#^pl4-i-4b]]"}
tags: [capital, market-risk, interest-rate, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Horizontal disallowance (HD) là vốn yêu cầu để bù đắp rủi ro do khớp trạng thái trong cùng một vùng hoặc giữa các vùng khác nhau, thành phần của [[general-interest-rate-risk-capital]] [[src-tt14-2025-nhnn#^pl4-i-4b]].

## Công thức
$$
HD = (b) \times 40\% + (c) \times 30\% + (d) \times 30\% + (e) \times 40\% + (f) \times 40\% + (g) \times 100\%
$$
[[src-tt14-2025-nhnn#^pl4-i-4c9]]

| Ký hiệu | Ý nghĩa | Hệ số | Nguồn |
|---|---|---|---|
| (b) | Trạng thái tương ứng điều chỉnh của vùng 1 | 40% | [[src-tt14-2025-nhnn#^pl4-i-4c78]] [[src-tt14-2025-nhnn#^pl4-i-4c9]] |
| (c) | Trạng thái tương ứng điều chỉnh của vùng 2 | 30% | [[src-tt14-2025-nhnn#^pl4-i-4c78]] [[src-tt14-2025-nhnn#^pl4-i-4c9]] |
| (d) | Trạng thái tương ứng điều chỉnh của vùng 3 | 30% | [[src-tt14-2025-nhnn#^pl4-i-4c78]] [[src-tt14-2025-nhnn#^pl4-i-4c9]] |
| (e) | Trạng thái tương ứng giữa vùng 1 và vùng 2 | 40% | [[src-tt14-2025-nhnn#^pl4-i-4c78]] [[src-tt14-2025-nhnn#^pl4-i-4c9]] |
| (f) | Trạng thái tương ứng giữa vùng 2 và vùng 3 | 40% | [[src-tt14-2025-nhnn#^pl4-i-4c78]] [[src-tt14-2025-nhnn#^pl4-i-4c9]] |
| (g) | Trạng thái tương ứng giữa vùng 1 và vùng 3 | 100% | [[src-tt14-2025-nhnn#^pl4-i-4c78]] [[src-tt14-2025-nhnn#^pl4-i-4c9]] |

## Diễn giải
**Cách xác định (b) đến (g)** [[src-tt14-2025-nhnn#^pl4-i-4c78]]:
- (b), (c), (d): giá trị tuyệt đối nhỏ hơn của tổng trạng thái dương và tổng trạng thái âm điều chỉnh của từng vùng.
- (e): giá trị tuyệt đối nhỏ hơn giữa trạng thái không tương ứng của vùng 1 và của vùng 2 khi hai trạng thái trái dấu.
- (f): như (e) giữa vùng 2 (phần không tương ứng còn lại) và vùng 3.
- (g): như (e) giữa vùng 1 và vùng 3, dùng phần không tương ứng còn lại của hai vùng.

Ví dụ của nguồn: vùng 1 khớp 0,2 × 40% = 0,08; vùng 2 và 3 khớp 1,125 × 40% = 0,45; vùng 1 và 3 khớp 1 × 100% = 1 tỷ đồng [[src-tt14-2025-nhnn#^pl4-i-vd3]] [[src-tt14-2025-nhnn#^pl4-i-vd4]].

*Diễn giải:* trong ví dụ, HD = 0,08 + 0,45 + 1 = 1,53 tỷ đồng, chiếm 33% của tổng 4,58 tỷ đồng. Hệ số 100% cho khớp giữa vùng 1 và 3 làm cặp vùng xa nhau tốn vốn bằng toàn bộ phần khớp.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Hệ số trong vùng | [cần nguồn] (MAR chưa ingest) | 40% / 30% / 30% [[src-tt14-2025-nhnn#^pl4-i-4c9]] | PL4.B.I.4c bước 9 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Hệ số giữa các vùng | [cần nguồn] | 40% (1–2), 40% (2–3), 100% (1–3) [[src-tt14-2025-nhnn#^pl4-i-4c9]] | PL4.B.I.4c bước 9 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* HD phạt lệch kỳ hạn giữa các vùng: sổ kinh doanh giữ trạng thái dương ngắn hạn và âm dài hạn (hoặc ngược lại) chịu hệ số cao hơn so với khớp trong cùng vùng.

## Nhầm lẫn thường gặp
- HD gồm sáu hệ số, ba cho khớp trong vùng và ba cho khớp giữa các vùng [[src-tt14-2025-nhnn#^pl4-i-4c9]].
