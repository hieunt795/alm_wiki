---
title: "Common Equity Tier 1 Capital"
aliases: [Common Equity Tier 1 Capital, CET1, CET1 Capital, Vốn lõi cấp 1, Vốn lõi cấp 1 chưa giảm trừ]
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
  - {type: input-to, to: "[[capital-adequacy-ratio]]", cite: "[[src-tt14-2025-nhnn#^d5-1a]]"}
tags: [capital, cet1, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn lõi cấp 1 (A1) là tử số của tỷ lệ vốn lõi cấp 1 ([[capital-adequacy-ratio]]) [[src-tt14-2025-nhnn#^d5-1a]] và là cấu phần chính của vốn cấp 1 trong [[own-funds]] [[src-tt14-2025-nhnn#^pl1-a-struct]]. Vốn lõi cấp 1 bằng vốn lõi cấp 1 chưa giảm trừ (A11) trừ các khoản giảm trừ (A12) [[src-tt14-2025-nhnn#^pl1-a-struct]].

## Công thức
$$
A_1 = A_{11} - A_{12}
$$
[[src-tt14-2025-nhnn#^pl1-a-struct]]

$$
A_{11} = \sum_{k=1}^{10} (k)
$$
[[src-tt14-2025-nhnn#^pl1-a11]]

A11 là tổng mười khoản mục (1)–(10). A12 là tổng tám khoản mục (11)–(18), xem [[capital-deductions]] [[src-tt14-2025-nhnn#^pl1-a12]].

**Mười khoản mục của A11 (ngân hàng thương mại, riêng lẻ)** [[src-tt14-2025-nhnn#^pl1-a11]]:

| Mục | Khoản mục | Ghi chú | Nguồn |
|---|---|---|---|
| (1) | Vốn điều lệ (vốn đã góp) | Số liệu trên Báo cáo tình hình tài chính | [[src-tt14-2025-nhnn#^pl1-a11]] |
| (2) | Quỹ dự trữ bổ sung vốn điều lệ | Khoản mục Quỹ của tổ chức tín dụng | [[src-tt14-2025-nhnn#^pl1-a11]] |
| (3) | Quỹ đầu tư phát triển | Khoản mục Quỹ của tổ chức tín dụng | [[src-tt14-2025-nhnn#^pl1-a11]] |
| (4) | Quỹ dự phòng tài chính | Khoản mục Quỹ của tổ chức tín dụng | [[src-tt14-2025-nhnn#^pl1-a11]] |
| (5) | Các quỹ khác trích từ lợi nhuận sau thuế | Không gồm quỹ khen thưởng, phúc lợi, quỹ thưởng ban điều hành | [[src-tt14-2025-nhnn#^pl1-a11]] |
| (6) | Vốn đầu tư xây dựng cơ bản, mua sắm tài sản cố định | Số liệu trên Báo cáo tình hình tài chính | [[src-tt14-2025-nhnn#^pl1-a11]] |
| (7) | Vốn khác | Số liệu trên Báo cáo tình hình tài chính | [[src-tt14-2025-nhnn#^pl1-a11]] |
| (8) | Lợi nhuận chưa phân phối | Ngân hàng được chấp thuận hoãn, giãn trích lập dự phòng rủi ro phải trừ chênh lệch dương giữa dự phòng phải trích và dự phòng đã trích | [[src-tt14-2025-nhnn#^pl1-a11-8]] |
| (9) | Thặng dư vốn cổ phần của cổ phần phổ thông | Thặng dư vốn cổ phần nhân tỷ trọng cổ phần phổ thông trên tổng số cổ phần | [[src-tt14-2025-nhnn#^pl1-a11-9]] |
| (10) | Chênh lệch tỷ giá hối đoái | Do đánh giá lại vốn chủ sở hữu có gốc ngoại tệ khi chuyển đổi báo cáo tài chính | [[src-tt14-2025-nhnn#^pl1-a11]] |

## Diễn giải
**Hợp nhất.** Vốn tự có hợp nhất lấy từ Báo cáo tình hình tài chính hợp nhất, không hợp nhất công ty con hoạt động theo Luật kinh doanh bảo hiểm [[src-tt14-2025-nhnn#^pl1-ii-1]]. Cấu trúc A1 = A11 − A12 giữ nguyên, nhưng A12 là tổng khoản mục (11)–(19) vì có thêm lợi thế thương mại [[src-tt14-2025-nhnn#^pl1-ii-struct]] [[src-tt14-2025-nhnn#^pl1-ii-gw]].

**Chi nhánh ngân hàng nước ngoài.** Vốn cấp 1 chỉ gồm vốn lõi cấp 1. A11 là tổng chín khoản mục, khoản (1) là vốn đã được cấp; A12 là tổng khoản mục (10)–(15) [[src-tt14-2025-nhnn#^pl1-br-struct]].

*Diễn giải:* A11 gồm vốn góp, các quỹ, lợi nhuận giữ lại và chênh lệch tỷ giá, không gồm công cụ nợ. Công cụ bổ sung vốn cấp 1 phân loại là nợ kế toán nên nằm ở [[additional-tier-1-capital]], không nằm ở A11 [[src-tt14-2025-nhnn#^pl1-iii-10]].

*Diễn giải:* lợi nhuận chưa phân phối nằm trong A11 [[src-tt14-2025-nhnn#^pl1-a11]]. Phần lợi nhuận giữ lại vì vậy tăng vốn lõi cấp 1, còn chi trả cổ tức bằng tiền mặt làm giảm vốn lõi cấp 1 và bị ràng buộc bởi [[capital-conservation-buffer]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu trúc | Tier 1 gồm CET1 và/hoặc AT1 theo CAP10 [[src-bcbs-lev#^lev20-4]]; chi tiết CET1 [cần nguồn] (CAP10 chưa ingest) | A1 = A11 − A12 [[src-tt14-2025-nhnn#^pl1-a-struct]] | PL1.A.I | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Mức tối thiểu | [cần nguồn] | 4,5% (xem [[capital-adequacy-ratio]]) [[src-tt14-2025-nhnn#^d5-3]] | Đ5.3a | Như trên |
| Khoản mục cộng | [cần nguồn] | Mười khoản mục (1)–(10) [[src-tt14-2025-nhnn#^pl1-a11]] | PL1.A.I | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* hai đòn bẩy của vốn lõi cấp 1 mà ALM kiểm soát là giữ lại lợi nhuận và kiểm soát các khoản giảm trừ (tài sản thuế hoãn lại, tài sản vô hình, góp vốn chéo; xem [[capital-deductions]]). Vốn cấp 1 cũng là tử số của [[leverage-ratio]].

## Nhầm lẫn thường gặp
- Vốn lõi cấp 1 chưa giảm trừ (A11) chưa phải tử số của tỷ lệ. Tử số là A1 sau giảm trừ A12 [[src-tt14-2025-nhnn#^pl1-a-struct]].
- Tỷ lệ NSFR của TT50 dùng "vốn lõi cấp 1 chưa giảm trừ, trừ một số mục", không phải A1 sau giảm trừ đầy đủ [[src-tt50-2026-nhnn#^pl2-a2-1]]. Xem [[asf-capital-and-long-term-liabilities]].
