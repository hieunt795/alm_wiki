---
title: "Third-Party Guarantee Mitigation"
aliases: [Third-Party Guarantee Mitigation, Bảo lãnh của bên thứ ba, Giảm thiểu rủi ro bằng bảo lãnh]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[credit-risk-mitigation]]", cite: "[[src-tt14-2025-nhnn#^d25-2]]"}
tags: [capital, credit-risk, guarantee, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ28 TT14/2025 cho phép giảm giá trị khoản phải đòi bằng bảo lãnh của bên thứ ba, với bốn nhóm bên bảo lãnh và năm điều kiện [[src-tt14-2025-nhnn#^d28-2]] [[src-tt14-2025-nhnn#^d28-3ab]] [[src-tt14-2025-nhnn#^d28-3cd]]. Giá trị bảo lãnh $G_l$ đi vào $E_l$ trong công thức $E_i^{*}$ với hệ số $(1 - CRWgtor_l / CRW_l)$ ([[credit-risk-mitigation]]) [[src-tt14-2025-nhnn#^d25-4]].

## Cơ chế & drivers
**Bên bảo lãnh được chấp nhận (Đ28.2)** [[src-tt14-2025-nhnn#^d28-2]]:
- Chính phủ, ngân hàng trung ương, tổ chức công lập của Chính phủ, chính quyền địa phương;
- tổ chức tín dụng, chi nhánh ngân hàng nước ngoài xếp hạng từ BBB- trở lên;
- doanh nghiệp xếp hạng từ A- trở lên;
- tổ chức tài chính quốc tế.

**Điều kiện (Đ28.3)**

| Điều kiện | Nội dung | Nguồn |
|---|---|---|
| Quyền đòi nợ | Ngân hàng có quyền đòi nợ trực tiếp với bên bảo lãnh cho từng nghĩa vụ cụ thể, xác định cụ thể và không thể huỷ ngang | [[src-tt14-2025-nhnn#^d28-3ab]] |
| Cam kết | Không huỷ ngang và không điều kiện; bên bảo lãnh không đơn phương chấm dứt nghĩa vụ hoặc tăng phí khi khả năng của khách hàng suy giảm; cam kết thực hiện kịp thời khi khách hàng không thực hiện | [[src-tt14-2025-nhnn#^d28-3ab]] |
| Thời hạn | Hợp đồng bảo lãnh có hiệu lực tối thiểu bằng thời hạn của khoản phải đòi, giao dịch | [[src-tt14-2025-nhnn#^d28-3cd]] |
| Chất lượng bên bảo lãnh | CRW thấp hơn hoặc xếp hạng tốt hơn bên được bảo lãnh | [[src-tt14-2025-nhnn#^d28-3cd]] |
| Độc lập | Bên bảo lãnh không phải công ty mẹ, công ty con, công ty liên kết của bên được bảo lãnh | [[src-tt14-2025-nhnn#^d28-3cd]] |

**Bảo lãnh một phần (Đ28.4).** Khoản phải đòi không được bảo lãnh toàn bộ thì chỉ điều chỉnh giảm cho phần số dư được bảo lãnh [[src-tt14-2025-nhnn#^d28-4]].

**Độ lệch tiền tệ.** Phần bảo lãnh trong công thức $E_i^{*}$ không có hệ số hiệu chỉnh độ lệch tiền tệ; ba biện pháp còn lại có hệ số này [[src-tt14-2025-nhnn#^d25-4]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Phần giảm thiểu dùng tỷ số CRW của bên bảo lãnh trên CRW của khách hàng: $G_l (1 - CRWgtor_l / CRW_l)$ [[src-tt14-2025-nhnn#^d25-4]]. Bên bảo lãnh có CRW bằng khách hàng thì phần giảm thiểu bằng 0.

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* bảo lãnh của Chính phủ (CRW 0% theo Đ13.1, [[sovereign-and-bank-exposure-risk-weighting]]) với khách hàng có CRW 100% làm phần được bảo lãnh giảm toàn bộ giá trị tính RWA. Ví dụ số do wiki dựng: $G_l$ = 50 tỷ đồng, CRW bên bảo lãnh 0%, CRW khách hàng 100% thì phần giảm thiểu 50 × (1 − 0/1) = 50 tỷ đồng.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Công thức phần bảo lãnh trong Đ25.4 không có hệ số độ lệch tiền tệ, trong khi Đ25.3d yêu cầu hiệu chỉnh độ lệch tiền tệ cho mọi biện pháp: nguồn không giải thích [cần nguồn] [[src-tt14-2025-nhnn#^d25-3cd]].
