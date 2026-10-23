---
title: "Settlement Failure Risk Weighting"
aliases: [Settlement Failure Risk Weighting, Thanh toán chậm giao dịch, Rủi ro thanh toán]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[counterparty-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^pl2-7]]"}
tags: [capital, counterparty-risk, settlement, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
PL2.7 và PL2.8 quy định cách tính tài sản tính theo rủi ro tín dụng đối tác khi đối tác không thanh toán đúng hạn, tách giao dịch có thỏa thuận thanh toán đồng thời khỏi giao dịch không có thỏa thuận này [[src-tt14-2025-nhnn#^pl2-7]] [[src-tt14-2025-nhnn#^pl2-8]]. Xem [[counterparty-credit-risk-rwa]].

## Cơ chế & drivers
**Thanh toán đồng thời (PL2.7).** Đối tác không thanh toán đúng thời gian đã cam kết thì ngân hàng phải có quy trình theo dõi, giám sát chặt chẽ, và phải tính $RWA_{CCR}$ khi giao dịch không được thanh toán sau 05 ngày kể từ ngày thanh toán đã cam kết [[src-tt14-2025-nhnn#^pl2-7]]:

$$
RWA_{CCR} = GD \times r
$$
[[src-tt14-2025-nhnn#^pl2-7]]

Raw viết "RWAccr = x r", mất vế đầu. Công thức trên là tái dựng của wiki từ lời giải thích biến: GD là số dư giao dịch chưa thanh toán đúng hạn, r là hệ số rủi ro theo số ngày chậm trả. Chưa đối chiếu bản gốc [cần nguồn] [[src-tt14-2025-nhnn#^pl2-7]].

| Số ngày chậm thanh toán | Hệ số rủi ro r |
|---|---|
| Từ 5 đến 15 ngày | 8% |
| Từ 16 đến 30 ngày | 50% |
| Từ 31 đến 45 ngày | 75% |
| Từ 46 ngày trở lên | 100% |

[[src-tt14-2025-nhnn#^pl2-7]]

**Không thỏa thuận thanh toán đồng thời (PL2.8).** Ngân hàng đã thanh toán theo cam kết mà trong 05 ngày làm việc kể từ ngày thỏa thuận thanh toán đối tác chưa thực hiện nghĩa vụ thì $RWA_{CCR}$ = $E_j$ × CRW, với $E_j$ là giá trị giao dịch và CRW là hệ số rủi ro tín dụng của đối tác [[src-tt14-2025-nhnn#^pl2-8]]. Sau 05 ngày làm việc đó mà đối tác vẫn chưa thực hiện, ngân hàng phải trừ giá trị giao dịch và chi phí thay thế (nếu có) vào vốn tự có cho tới khi đối tác thực hiện nghĩa vụ [[src-tt14-2025-nhnn#^pl2-8]]. Xem [[own-funds]] và [[capital-deductions]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Ở PL2.8 ngân hàng phải trừ giá trị giao dịch khỏi vốn tự có; đây là xử lý trừ vốn, khác việc nhân hệ số rủi ro [[src-tt14-2025-nhnn#^pl2-8]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* giao dịch ngoại tệ và giấy tờ có giá thanh toán không đồng thời (ngân hàng giao trước, đối tác giao sau) cần giám sát thanh toán hằng ngày; sau 05 ngày làm việc không nhận thanh toán, vốn tự có giảm bằng giá trị giao dịch. Bảng 8%/50%/75%/100% áp dụng riêng cho giao dịch thanh toán đồng thời.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Cách ghi vế đầu bị mất của công thức PL2.7: cần đối chiếu pdf/docx [cần nguồn].
