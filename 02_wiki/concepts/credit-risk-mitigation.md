---
title: "Credit Risk Mitigation"
aliases: [Credit Risk Mitigation, CRM, Giảm thiểu rủi ro tín dụng]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[exposure-value]]", cite: "[[src-tt14-2025-nhnn#^d25-4]]"}
tags: [capital, credit-risk, collateral, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ25 TT14/2025 cho phép ngân hàng điều chỉnh giảm giá trị khoản phải đòi, giao dịch bằng một hoặc kết hợp bốn biện pháp giảm thiểu rủi ro tín dụng [[src-tt14-2025-nhnn#^d25-2]]. Giá trị sau điều chỉnh là $E_i^{*}$, đầu vào của $RWA_{CR}$ ([[customer-credit-risk-rwa]]) và của $RWA_{CCR}$ ([[counterparty-credit-risk-rwa]]) [[src-tt14-2025-nhnn#^d8-2-vars]].

## Cơ chế & drivers
**Bốn biện pháp** [[src-tt14-2025-nhnn#^d25-2]]:

| Biện pháp | Node | Điều |
|---|---|---|
| Tài sản bảo đảm | [[eligible-collateral-haircuts]] | Đ26 |
| Bù trừ số dư nội bảng | [[on-balance-sheet-netting]] | Đ27 |
| Bảo lãnh của bên thứ ba | [[third-party-guarantee-mitigation]] | Đ28 |
| Sản phẩm phái sinh tín dụng | [[credit-derivative-mitigation]] | Đ29 |

**Công thức $E_i^{*}$ (Đ25.4).** $E_i^{*}$ bằng tổng bốn phần max{0; số dư phần đó trừ giá trị biện pháp sau hiệu chỉnh}, cộng phần không giảm thiểu $E_x$ [[src-tt14-2025-nhnn#^d25-4]]:

$$
E_i^{*} = \max\{0;\ E_j - \sum C_j^{*}(1 - Hc_j - H_{fxc,j})\} + \max\{0;\ E_k - \sum L_k^{*}(1 - H_{fxl,k})\} + \max\{0;\ E_l - \sum G_l(1 - CRWgtor_l / CRW_l)\} + \max\{0;\ E_n - \sum CD_n^{*}(1 - H_{fxcd,n})\} + E_x
$$
[[src-tt14-2025-nhnn#^d25-4]]

$$
E_i = E_j + E_k + E_l + E_n + E_x
$$
[[src-tt14-2025-nhnn#^d25-4]]

Ký hiệu của wiki (dấu $\max\{0;\ \cdot\}$, chữ $fxc,j$) là cách viết lại của công thức nguồn, nguồn viết "max{0,[…]}" và $H_{fxcj}$ [[src-tt14-2025-nhnn#^d25-4]].

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $E_i$ | Số dư khoản phải đòi, giao dịch i tính theo Đ8 ([[exposure-value]]) | [[src-tt14-2025-nhnn#^d25-4-e]] |
| $E_j$, $E_k$, $E_l$, $E_n$ | Phần số dư được giảm thiểu bằng tài sản bảo đảm, bù trừ nội bảng, bảo lãnh, phái sinh tín dụng | [[src-tt14-2025-nhnn#^d25-4-e]] |
| $E_x$ | Phần số dư không được điều chỉnh giảm | [[src-tt14-2025-nhnn#^d25-4-e]] |
| $C_j^{*}$, $L_k^{*}$, $CD_n^{*}$ | Giá trị tài sản bảo đảm, nợ phải trả nội bảng, phái sinh tín dụng hiệu chỉnh theo độ lệch thời hạn | [[src-tt14-2025-nhnn#^d25-4-h]] |
| $G_l$ | Giá trị bảo lãnh của bên thứ ba | [[src-tt14-2025-nhnn#^d25-4-h]] |
| $Hc_j$ | Hệ số hiệu chỉnh tài sản bảo đảm | [[src-tt14-2025-nhnn#^d25-4-h]] |
| $H_{fxc}$, $H_{fxl}$, $H_{fxcd}$ | Hệ số hiệu chỉnh độ lệch tiền tệ | [[src-tt14-2025-nhnn#^d25-4-h]] |
| $CRWgtor_l$, $CRW_l$ | Hệ số rủi ro tín dụng của bên bảo lãnh và của khách hàng ([[credit-risk-weight]]) | [[src-tt14-2025-nhnn#^d25-4-h]] |

Các đại lượng $C_j^{*}$, $L_k^{*}$, $G_l$, $CD_n^{*}$ không có node metric riêng vì nguồn chỉ định nghĩa chúng trong công thức giảm thiểu, mỗi đại lượng được mô tả ở node biện pháp tương ứng.

**Nguyên tắc chung (Đ25.3)**
- Biện pháp giảm thiểu phải theo pháp luật liên quan, được các bên thỏa thuận bằng văn bản nêu rõ trách nhiệm, nghĩa vụ, và có hiệu lực tại thời điểm áp dụng [[src-tt14-2025-nhnn#^d25-3a]].
- Khi thời hạn còn lại của biện pháp ngắn hơn thời hạn còn lại của khoản phải đòi, chỉ được điều chỉnh giảm với biện pháp có thời hạn gốc từ 01 năm trở lên và thời hạn còn lại từ 03 tháng trở lên [[src-tt14-2025-nhnn#^d25-3b]].
- Độ lệch thời hạn và độ lệch tiền tệ phải được hiệu chỉnh vào giá trị điều chỉnh giảm, trừ trường hợp Đ26.6 với độ lệch thời hạn [[src-tt14-2025-nhnn#^d25-3cd]].
- Ngân hàng phải có quy định nội bộ để quản lý các rủi ro khác (rủi ro hoạt động, rủi ro thị trường…) phát sinh từ giảm thiểu rủi ro tín dụng và đảm bảo vốn yêu cầu tương ứng [[src-tt14-2025-nhnn#^d25-3dd]].
- Khi dùng nhiều biện pháp, ngân hàng phân tách giá trị từng biện pháp cho từng phần số dư theo thỏa thuận (nếu có) và quy định nội bộ; tổng giá trị phân bổ không vượt quá tổng giá trị biện pháp đủ điều kiện [[src-tt14-2025-nhnn#^d25-3e]].

**Hiệu chỉnh độ lệch thời hạn.** Ba biện pháp có giá trị theo thời gian đều dùng cùng một hình thức $X^{*} = X \times (t - 0{,}25) / (T - 0{,}25)$:
- tài sản bảo đảm (trừ tiền mặt và vàng) [[src-tt14-2025-nhnn#^d26-4]];
- số dư tiền gửi bù trừ nội bảng [[src-tt14-2025-nhnn#^d27-2]];
- sản phẩm phái sinh tín dụng [[src-tt14-2025-nhnn#^d29-3]].

Bảo lãnh không có công thức hiệu chỉnh thời hạn, thay vào đó hợp đồng bảo lãnh phải có hiệu lực tối thiểu bằng thời hạn khoản phải đòi [[src-tt14-2025-nhnn#^d28-3cd]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn của Chương II; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]]. Giảm thiểu rủi ro tín dụng trong IRB (Chương III) chưa ingest [cần nguồn].

## Góc nhìn theo domain
**VN Regulator.** Công thức $E_i^{*}$ trừ giá trị biện pháp theo từng nhóm riêng rồi cộng, mỗi nhóm có sàn 0 [[src-tt14-2025-nhnn#^d25-4]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* hiệu chỉnh độ lệch thời hạn dùng hệ số $(t - 0{,}25) / (T - 0{,}25)$. Với T bằng 5 năm, biện pháp còn 1 năm có hệ số (1 − 0,25) / (5 − 0,25) ≈ 0,158; ví dụ số do wiki dựng, nguồn không đưa ví dụ. Tài sản bảo đảm hoặc tiền gửi kỳ hạn ngắn bảo đảm khoản vay dài chỉ giảm RWA một phần nhỏ. Với repo và phái sinh, Đ26 cũng áp dụng cho tài sản bảo đảm của giao dịch ([[counterparty-credit-risk-rwa]]).

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Đ25.3c ghi giá trị điều chỉnh giảm phải hiệu chỉnh độ lệch thời hạn nhưng không nêu công thức cho bảo lãnh; việc xử lý độ lệch thời hạn của bảo lãnh nằm ngoài C2-M4 [cần nguồn].
