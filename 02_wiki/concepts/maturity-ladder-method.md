---
title: "Maturity Ladder Method (Market Risk)"
aliases: [Maturity Ladder Method, Phương pháp thang kỳ hạn, Thang kỳ hạn rủi ro lãi suất chung]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[general-interest-rate-risk-capital]]", cite: "[[src-tt14-2025-nhnn#^pl4-i-4c12]]"}
tags: [capital, market-risk, interest-rate, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Phương pháp thang kỳ hạn phân bổ trạng thái của công cụ tài chính vào 15 thang kỳ hạn, thuộc ba vùng, mỗi thang có hệ số rủi ro (%), để tính $K_{IRR}^{GMR}$ = NWP + VD + HD ([[general-interest-rate-risk-capital]]) [[src-tt14-2025-nhnn#^pl4-i-4c12]]. Không nhầm với thang kỳ hạn thanh khoản của [[contractual-maturity-mismatch]].

## Cơ chế & drivers
**Chín bước** [[src-tt14-2025-nhnn#^pl4-i-4c12]] [[src-tt14-2025-nhnn#^pl4-i-4c35]] [[src-tt14-2025-nhnn#^pl4-i-4c6]] [[src-tt14-2025-nhnn#^pl4-i-4c78]] [[src-tt14-2025-nhnn#^pl4-i-4c9]]:
1. Xác định kỳ hạn theo thời hạn còn lại đến đáo hạn hoặc đến kỳ điều chỉnh lãi suất của từng trạng thái.
2. Phân bổ trạng thái vào thang kỳ hạn theo bảng.
3. Xác định trạng thái ròng dương (long) và âm (short) của từng thang.
4. Nhân trạng thái ròng với hệ số rủi ro của thang, ra trạng thái điều chỉnh theo hệ số rủi ro.
5. Tính [[net-weighted-position]] (NWP).
6. Tính [[vertical-disallowance]] (VD).
7. Xác định trạng thái không tương ứng của từng thang và trạng thái tương ứng của từng vùng.
8. Xác định trạng thái không tương ứng của từng vùng và trạng thái tương ứng giữa các vùng (1–2, 2–3, 1–3).
9. Tính [[horizontal-disallowance]] (HD).

**Bảng thang kỳ hạn và hệ số rủi ro** [[src-tt14-2025-nhnn#^pl4-i-4c12]]. Bảng có hai cột thang kỳ hạn, một cho lãi suất ≥ 3% và một cho lãi suất < 3%; nguồn không nêu lãi suất nào được dùng để chọn cột (xem Câu hỏi mở):

| Vùng | Thang kỳ hạn, lãi suất ≥ 3% | Thang kỳ hạn, lãi suất < 3% | Hệ số rủi ro (%) |
|---|---|---|---|
| 1 | dưới 1 tháng trở xuống | dưới 1 tháng | 0,00 |
| 1 | 1 đến dưới 3 tháng | 1 đến dưới 3 tháng | 0,20 |
| 1 | 3 đến dưới 6 tháng | 3 đến dưới 6 tháng | 0,40 |
| 1 | 6 đến dưới 12 tháng | 6 đến dưới 12 tháng | 0,70 |
| 2 | 1 đến dưới 2 năm | 1 đến dưới 1,9 năm | 1,25 |
| 2 | 2 đến dưới 3 năm | 1,9 đến dưới 2,8 năm | 1,75 |
| 2 | 3 đến dưới 4 năm | 2,8 đến dưới 3,6 năm | 2,25 |
| 3 | 4 đến dưới 5 năm | 3,6 đến dưới 4,3 năm | 2,75 |
| 3 | 5 đến dưới 7 năm | 4,3 đến dưới 5,7 năm | 3,25 |
| 3 | 7 đến dưới 10 năm | 5,7 đến dưới 7,3 năm | 3,75 |
| 3 | 10 đến dưới 15 năm | 7,3 đến dưới 9,3 năm | 4,50 |
| 3 | 15 đến dưới 20 năm | 9,3 đến dưới 10,6 năm | 5,25 |
| 3 | từ 20 năm trở lên | 10,6 đến dưới 12 năm | 6,00 |
| 3 | (không có) | 12 đến dưới 20 năm | 8,00 |
| 3 | (không có) | từ 20 năm trở lên | 12,50 |

Bảng raw có nhiều ô trống và cột lệch; wiki chép theo cấu trúc hàng của nguồn. Hàng "dưới 1 tháng" của lãi suất ≥ 3% ghi "dưới 1 tháng trở xuống" trong nguồn [[src-tt14-2025-nhnn#^pl4-i-4c12]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn của Phụ lục IV; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Nguồn đặt hai cột thang kỳ hạn theo mức lãi suất 3%, nên thang kỳ hạn của một trạng thái phụ thuộc cột lãi suất áp dụng cho nó [[src-tt14-2025-nhnn#^pl4-i-4c12]].

**Basel.** [cần nguồn] (MAR chưa ingest).

**ALM.** *Diễn giải:* kỳ hạn trong bảng là thời hạn còn lại đến kỳ định lại lãi suất với công cụ lãi suất thả nổi, nên hợp đồng hoán đổi thả nổi/cố định đi vào hai thang khác nhau. Ví dụ nguồn: chân thả nổi (9 tháng) vào thang 6 đến dưới 12 tháng, chân cố định (8 năm) vào thang 7 đến dưới 10 năm [[src-tt14-2025-nhnn#^pl4-i-vd1]].

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Cột lãi suất ≥ 3% và < 3% áp dụng cho lãi suất coupon, lãi suất hiện hành hay lãi suất thị trường: nguồn không nêu [cần nguồn].
