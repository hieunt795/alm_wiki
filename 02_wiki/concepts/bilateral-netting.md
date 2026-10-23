---
title: "Bilateral Netting"
aliases: [Bilateral Netting, Bù trừ hai bên, Netting hai bên]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[counterparty-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^pl2-10]]"}
tags: [capital, counterparty-risk, netting, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Bù trừ hai bên là việc ngân hàng thay thế một nghĩa vụ thanh toán với đối tác cho một đồng tiền nhất định vào thời điểm nhất định, đối với các nghĩa vụ cùng đồng tiền và cùng thời điểm [[src-tt14-2025-nhnn#^pl2-9]]. Khi đủ ba điều kiện, $RWA_{CCR}$ tính trên số dư bù trừ thay vì từng giao dịch riêng lẻ [[src-tt14-2025-nhnn#^pl2-10]]. Xem [[counterparty-credit-risk-rwa]].

## Cơ chế & drivers
**Ba điều kiện (PL2.9)** [[src-tt14-2025-nhnn#^pl2-9a]]:
- có thỏa thuận, hợp đồng bù trừ hai bên tạo nghĩa vụ hợp pháp theo số dư bù trừ của giá trị thị trường các giao dịch riêng lẻ khi đối tác không thực hiện nghĩa vụ do mất khả năng thanh toán, phá sản, thanh lý hoặc tương tự; không có điều khoản cho phép đối tác thanh toán hạn chế hoặc không đầy đủ;
- pháp luật của các nước liên quan cho phép bù trừ hai bên;
- có quy trình đảm bảo yêu cầu pháp lý của thỏa thuận, hợp đồng được rà soát theo thay đổi của pháp luật liên quan.

**Tính $RWA_{CCR}$ (PL2.10).** $RWA_{CCR}$ khi bù trừ hai bên là tổng chi phí thay thế bù trừ (nếu dương) và chỉ số tăng thêm theo giá trị vốn gốc danh nghĩa [[src-tt14-2025-nhnn#^pl2-10]].

$$
A_{Net} = A_{Gross} \times (0{,}4 + 0{,}6 \times NGR)
$$
[[src-tt14-2025-nhnn#^pl2-10]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $A_{Net}$ | Chỉ số tăng thêm của giao dịch bù trừ | [[src-tt14-2025-nhnn#^pl2-10]] |
| $A_{Gross}$ | Chỉ số tăng thêm tổng hợp: tổng PFE của các giao dịch thành phần tính theo Mục 4 Phụ lục II ([[potential-future-exposure]]) | [[src-tt14-2025-nhnn#^pl2-10]] |
| NGR | Tỷ lệ chi phí thay thế bù trừ trên tỷ lệ thay thế tổng hợp của các giao dịch trong thỏa thuận, hợp đồng bù trừ hai bên | [[src-tt14-2025-nhnn#^pl2-10]] |

*Diễn giải:* $A_{Net}$ nằm từ 40% đến 100% của $A_{Gross}$, vì NGR nằm trong khoảng 0 đến 1 (nếu NGR là tỷ số của chi phí thay thế bù trừ trên chi phí thay thế tổng hợp). Nguồn không nêu cận của NGR; ghi nhận của wiki theo cách đọc định nghĩa [cần nguồn]. Ví dụ số do wiki dựng: $A_{Gross}$ = 10 tỷ đồng, NGR = 0,5 thì $A_{Net}$ = 10 × (0,4 + 0,3) = 7 tỷ đồng.

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]]. Khác với bù trừ số dư nội bảng giữa khoản phải đòi và tiền gửi ([[on-balance-sheet-netting]]).

## Góc nhìn theo domain
**VN Regulator.** PL2.9a yêu cầu pháp luật của các nước liên quan cho phép bù trừ hai bên [[src-tt14-2025-nhnn#^pl2-9a]], nên giao dịch với đối tác nước ngoài cần đánh giá pháp lý theo từng nước.

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* hợp đồng khung phái sinh và repo có điều khoản bù trừ thanh toán khi vỡ nợ là điều kiện để được hưởng $A_{Net}$ thay vì $A_{Gross}$. Bộ phận pháp chế cần rà các ý kiến pháp lý theo từng nước định kỳ (PL2.9c).

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Cách tính NGR chi tiết: nguồn chỉ nêu định nghĩa bằng lời [cần nguồn].
