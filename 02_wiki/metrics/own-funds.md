---
title: "Own Funds"
aliases: [Own Funds, Regulatory Capital, Vốn tự có, Vốn cấp 1, Tier 1 Capital]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[capital-adequacy-ratio]]", cite: "[[src-tt14-2025-nhnn#^d6-1]]"}
tags: [capital, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn tự có là cơ sở để tính tỷ lệ an toàn vốn theo TT14/2025 [[src-tt14-2025-nhnn#^d6-1]]. Vốn tự có (C) bằng vốn cấp 1 (A) cộng vốn cấp 2 (B) [[src-tt14-2025-nhnn#^pl1-a-struct]]. Vốn cấp 1 gồm vốn lõi cấp 1 ([[common-equity-tier-1-capital]]) và vốn bổ sung vốn cấp 1 ([[additional-tier-1-capital]]); vốn cấp 2 xem [[tier-2-capital]] [[src-tt14-2025-nhnn#^d6-1]].

Công cụ bổ sung vốn cấp 1 là công cụ tài chính do ngân hàng thương mại phát hành, đáp ứng đầy đủ các điều kiện tại Phụ lục I [[src-tt14-2025-nhnn#^d2-17]], xem [[additional-tier-1-instrument-conditions]]. Nợ thứ cấp là khoản nợ mà chủ nợ đồng ý nhận thanh toán sau các nghĩa vụ, chủ nợ có bảo đảm và không bảo đảm khác khi đơn vị vay nợ bị phá sản, giải thể [[src-tt14-2025-nhnn#^d2-5]]; xem [[subordinated-debt]].

## Công thức
$$
C = A + B
$$
[[src-tt14-2025-nhnn#^pl1-a-struct]]

$$
A = A_1 + A_2
$$
[[src-tt14-2025-nhnn#^pl1-a-struct]]

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| C | Vốn tự có | node này | [[src-tt14-2025-nhnn#^pl1-a-struct]] |
| A | Vốn cấp 1 | node này | [[src-tt14-2025-nhnn#^pl1-a-struct]] |
| $A_1 = A_{11} - A_{12}$ | Vốn lõi cấp 1: khoản mục cộng (1)–(10) trừ khoản giảm trừ (11)–(18) | [[common-equity-tier-1-capital]] | [[src-tt14-2025-nhnn#^pl1-a-struct]] |
| $A_2 = A_{21} - A_{22}$ | Vốn bổ sung vốn cấp 1 | [[additional-tier-1-capital]] | [[src-tt14-2025-nhnn#^pl1-a21]] |
| $B = B_1 - B_2$ | Vốn cấp 2 | [[tier-2-capital]] | [[src-tt14-2025-nhnn#^pl1-b-struct]] |
| Khoản giảm trừ | A12, A22, B2 | [[capital-deductions]] | [[src-tt14-2025-nhnn#^pl1-a12]] |

## Diễn giải
**Ba biến thể của Phụ lục I.**
- **Ngân hàng thương mại, riêng lẻ** (Bảng 18): C = A + B với đủ ba cấp vốn [[src-tt14-2025-nhnn#^pl1-a-struct]].
- **Ngân hàng thương mại, hợp nhất** (Bảng 19): lấy từ Báo cáo tình hình tài chính hợp nhất, không hợp nhất công ty con là doanh nghiệp hoạt động theo Luật kinh doanh bảo hiểm. Khi báo cáo hợp nhất không có khoản mục cụ thể, ngân hàng phải xây dựng số liệu thống kê từ các bảng cân đối tài khoản kế toán riêng lẻ của các đối tượng hợp nhất [[src-tt14-2025-nhnn#^pl1-ii-1]]. Khác riêng lẻ ở ba điểm: thêm lợi thế thương mại vào khoản giảm trừ [[src-tt14-2025-nhnn#^pl1-ii-gw]]; góp vốn chéo lấy cả chứng khoán kinh doanh [[src-tt14-2025-nhnn#^pl1-ii-17]]; vốn cấp 2 cộng lợi ích cổ đông không kiểm soát [[src-tt14-2025-nhnn#^pl1-ii-mi]].
- **Chi nhánh ngân hàng nước ngoài** (Bảng 20): vốn cấp 1 chỉ gồm vốn lõi cấp 1 (A = A1), và dùng khoản mục "vốn đã được cấp" thay vốn điều lệ. Chi nhánh căn cứ vào các cấu phần của Phần B, quy định về chế độ tài chính và khoản mục tài sản của mình để xác định vốn tự có [[src-tt14-2025-nhnn#^pl1-br-struct]].

**Ngưỡng 2%.** Vốn tự có là cơ sở của ngưỡng 2% để $K_{FXR}$ và $K_{OPT}$ phát sinh [[src-tt14-2025-nhnn#^d74-4]] [[src-tt14-2025-nhnn#^d74-6]]. Xem [[market-risk-capital-requirement]].

*Diễn giải:* các node khác trong wiki dùng "vốn tự có" theo nghĩa của ngành. [[projected-own-funds]] ($C_A$ trong ICAAP của TT83/2025) là vốn tự có theo quy định NHNN dự phóng 3–5 năm. [[asf-capital-and-long-term-liabilities]] đưa các cấu phần vốn tự có vào ASF của NSFR; TT50/2026 đo vốn cấp 1 và vốn cấp 2 theo cách riêng (vốn lõi cấp 1 chưa giảm trừ, trừ một số mục) [[src-tt50-2026-nhnn#^pl2-a2-1]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu trúc vốn | CET1, AT1, Tier 2 theo CAP10 [cần nguồn] (CAP10 chưa ingest); LEV20.4 xác nhận Tier 1 = CET1 và/hoặc AT1 [[src-bcbs-lev#^lev20-4]] | Vốn tự có = vốn cấp 1 (vốn lõi cấp 1 + vốn bổ sung vốn cấp 1) + vốn cấp 2 [[src-tt14-2025-nhnn#^d6-1]] | Đ6.2, PL1.A.I | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Khoản giảm trừ | [cần nguồn] (CAP30 chưa ingest) | Ba nhóm A12, A22, B2 ([[capital-deductions]]) [[src-tt14-2025-nhnn#^pl1-a12]] | PL1.A.I | Như trên |
| Điều kiện công cụ AT1 | [cần nguồn] | 13 điều kiện, ngưỡng bù đắp lỗ 5,125% [[src-tt14-2025-nhnn#^pl1-iii-10]] | PL1.A.III | Như trên |
| Điều kiện nợ thứ cấp tính vốn cấp 2 | [cần nguồn] | Sáu điều kiện; kỳ hạn ban đầu từ 05 năm; khấu trừ 20% mỗi năm trong 05 năm cuối [[src-tt14-2025-nhnn#^pl1-b-sd-cond]] [[src-tt14-2025-nhnn#^pl1-b-sd-amort]] | PL1.A.I (23) | Như trên |
| Trần dự phòng trong vốn cấp 2 | [cần nguồn] | 1,25% (phương pháp tiêu chuẩn), 0,6% (IRB) [[src-tt14-2025-nhnn#^pl1-b2-cap]] | PL1.A.I (26)–(27) | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* nợ thứ cấp là nguồn huy động ALM dùng để tăng vốn cấp 2. Điều kiện kỳ hạn ban đầu từ 05 năm và lịch khấu trừ 20% mỗi năm trong 05 năm cuối làm giá trị tính vốn giảm dần trước ngày đáo hạn ([[subordinated-debt]]). Công cụ bổ sung vốn cấp 1 cần cơ chế bù đắp lỗ và quyền hủy chi trả, ảnh hưởng chi phí huy động ([[additional-tier-1-instrument-conditions]]).

*Diễn giải:* tài sản thuế hoãn lại, tài sản vô hình, lỗ lũy kế và góp vốn chéo bị trừ khỏi vốn lõi cấp 1 ([[capital-deductions]]), nên vốn tự có theo quy định thấp hơn vốn chủ sở hữu kế toán. [[capital-plan]] và [[projected-own-funds]] cần dự phóng cả các khoản trừ này.

## Nhầm lẫn thường gặp
- Vốn điều lệ không đồng nghĩa với vốn tự có. Vốn điều lệ chỉ là một trong mười khoản mục của vốn lõi cấp 1 chưa giảm trừ [[src-tt14-2025-nhnn#^pl1-a11]]. Giá trị thực của vốn điều lệ theo TT50/2026 là chỉ tiêu riêng, xem [[real-value-of-charter-capital]].
- Vốn kinh tế và vốn mục tiêu là đại lượng nội bộ của ICAAP, khác vốn tự có tính theo Phụ lục I, xem [[economic-capital]] và [[target-capital]].
- Chi nhánh ngân hàng nước ngoài không có vốn bổ sung vốn cấp 1 [[src-tt14-2025-nhnn#^pl1-br-struct]].
