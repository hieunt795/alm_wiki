---
title: "Subordinated Debt"
aliases: [Subordinated Debt, Subordinated Bond, Nợ thứ cấp, Trái phiếu thứ cấp, Tier 2 Subordinated Debt]
type: instrument
domains: [vn-reg, alm]
status: active
maturity: draft
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[tier-2-capital]]", cite: "[[src-tt14-2025-nhnn#^pl1-b-sd-amort]]"}
tags: [capital, tier-2, tt14, debt]
updated: 2026-10-23
reviewed:
---

## Định nghĩa & cashflow
Nợ thứ cấp là khoản nợ mà chủ nợ đồng ý nhận thanh toán sau các nghĩa vụ, chủ nợ có bảo đảm và không bảo đảm khác khi đơn vị vay nợ bị phá sản, giải thể [[src-tt14-2025-nhnn#^d2-5]]. Nợ thứ cấp đủ điều kiện được tính vào [[tier-2-capital]] (khoản mục (23) của B1) [[src-tt14-2025-nhnn#^pl1-b-sd-cond]].

**Sáu điều kiện để tính vào vốn cấp 2** [[src-tt14-2025-nhnn#^pl1-b-sd-cond]]:
1. Kỳ hạn ban đầu từ 05 năm trở lên.
2. Không được đảm bảo bằng tài sản của chính ngân hàng.
3. Ngân hàng được trả nợ trước thời gian đáo hạn với điều kiện sau khi thực hiện vẫn đảm bảo các tỷ lệ, giới hạn bảo đảm an toàn và báo cáo NHNN (Cục Quản lý, giám sát tổ chức tín dụng hoặc NHNN chi nhánh Khu vực) để giám sát.
4. Ngân hàng được ngừng trả lãi và chuyển lãi lũy kế sang năm tiếp theo nếu việc trả lãi dẫn đến kết quả kinh doanh trong năm bị lỗ.
5. Khi thanh lý ngân hàng, chủ sở hữu chỉ được thanh toán sau khi ngân hàng đã thanh toán cho tất cả các chủ nợ khác.
6. Lãi suất cố định hoặc công thức tính lãi suất được xác định trước và ghi rõ trong hợp đồng, tài liệu phát hành.

**Quy tắc lãi suất** [[src-tt14-2025-nhnn#^pl1-b-sd-rate]]:
- Lãi suất cố định: điều chỉnh tăng chỉ được thực hiện sau 05 năm kể từ ngày phát hành, ký kết hợp đồng, và chỉ được thay đổi 01 lần trong suốt thời hạn.
- Lãi suất theo công thức: công thức không được thay đổi; chỉ được thay đổi biên độ trong công thức (nếu có) 01 lần sau 05 năm kể từ ngày phát hành, ký kết hợp đồng.

## Pricing
Không ghi nhận trong nguồn đã ingest [cần nguồn].

## Risk factors & sensitivities
Điều kiện (4) cho phép ngừng trả lãi và chuyển lãi lũy kế sang năm sau khi việc trả lãi làm kết quả kinh doanh năm bị lỗ [[src-tt14-2025-nhnn#^pl1-b-sd-cond]]. *Diễn giải:* người mua chịu rủi ro trì hoãn lãi trong năm ngân hàng lỗ, và chịu thứ tự thanh toán sau mọi chủ nợ khác khi thanh lý.

## ALM & hedging usage
**Lịch khấu trừ giá trị tính vào vốn cấp 2** [[src-tt14-2025-nhnn#^pl1-b-sd-amort]]:
- Tại thời điểm xác định giá trị, nếu thời hạn còn lại trên 05 năm, toàn bộ giá trị nợ thứ cấp được tính vào vốn cấp 2.
- Bắt đầu từ năm thứ năm trước khi đến hạn thanh toán, mỗi năm tại ngày đầu tiên của năm (tính theo ngày phát hành), giá trị tính vào vốn cấp 2 bị khấu trừ 20% tổng mệnh giá.

| Số năm còn lại đến đáo hạn (tại ngày đầu tiên của năm) | Tỷ lệ mệnh giá còn tính vào vốn cấp 2 |
|---|---|
| Trên 05 năm | 100% |
| Năm thứ năm trước khi đáo hạn | 80% |
| Năm thứ tư | 60% |
| Năm thứ ba | 40% |
| Năm thứ hai | 20% |
| Năm cuối | 0% |

*Diễn giải:* bảng trên là phép tính của wiki từ mức khấu trừ 20% mỗi năm trong năm năm cuối; nguồn không đưa bảng này, và cách đếm ngày đầu tiên của năm tính theo ngày phát hành có thể làm các mốc lệch một kỳ [cần nguồn: ví dụ số]. Phần vốn cấp 2 từ nợ thứ cấp giảm dần khi đến gần ngày đáo hạn, nên ngân hàng cần phát hành thay thế sớm để giữ tỷ lệ an toàn vốn.

**Mua nợ thứ cấp của tổ chức tín dụng khác.** Khoản mua, đầu tư nợ thứ cấp của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác phát hành, đáp ứng điều kiện tính vào vốn cấp 2 của đơn vị đó, bị giảm trừ khỏi vốn cấp 2 của ngân hàng mua. Không gồm nợ thứ cấp nhận làm tài sản bảo đảm, chiết khấu, tái chiết khấu của khách hàng. Từ năm thứ năm trước khi đáo hạn, mỗi năm khấu trừ 20% tổng giá mua [[src-tt14-2025-nhnn#^pl1-b2-29]]. Xem [[capital-deductions]].

## Kế toán
Không ghi nhận trong nguồn đã ingest [cần nguồn].

## Basel treatment
[cần nguồn] (CAP10 chưa ingest). Đối chiếu một điểm khác biệt đã có nguồn ở NSFR: Basel loại phần công cụ Tier 2 có kỳ hạn còn lại dưới 1 năm khỏi ASF [[src-bcbs-nsfr#^nsf30-10]], còn TT50/2026 không khấu trừ nợ thứ cấp theo thời hạn còn lại khi tính ASF [[src-tt50-2026-nhnn#^pl2-a2-1]]. Xem [[asf-capital-and-long-term-liabilities]].

## Lưu ý tại VN
- TT14/2025 khấu trừ giá trị vốn cấp 2 theo thời hạn (20% mỗi năm trong năm năm cuối), còn TT50/2026 tính hệ số ASF của vốn cấp 2 theo kỳ hạn còn lại (0% / 50% / 100%) [[src-tt14-2025-nhnn#^pl1-b-sd-amort]] [[src-tt50-2026-nhnn#^pl2-a2-1]]. Hai quy định đo hai đại lượng khác nhau và không mâu thuẫn.
- Hợp nhất: vốn cấp 2 hợp nhất cộng thêm lợi ích cổ đông không kiểm soát [[src-tt14-2025-nhnn#^pl1-ii-mi]].
