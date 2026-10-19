---
title: "Loan Pricing"
aliases: [Loan Pricing, Định giá khoản vay, Break-even loan rate, Lãi suất cho vay hoà vốn, Target Rate of Return Floor Rate]
type: concept
domains: [alm, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [loan-pricing, roe, break-even-margin, credit-spread, tlp, ftp]
updated: 2026-10-19
reviewed:
---

## Ý chính
Theo Choudhry, định giá khoản vay nên dựa trước hết trên nguyên tắc tài chính doanh nghiệp chính thống, dù phần lớn ngân hàng là "price taker" và phải đặt lãi suất theo các ngân hàng cùng nhóm. RoE mục tiêu dẫn dắt định giá, và mọi hoạt động phải tạo lợi nhuận vượt RoE mục tiêu [[src-choudhry-principles-banking#^choudhry-lp-1]].

Lãi suất cho vay đặt bằng spread trên chi phí funding của ngân hàng. Spread là hàm của RoE mục tiêu, credit spread bù tổn thất dự kiến, và spread bù chi phí vận hành [[src-choudhry-principles-banking#^choudhry-lp-5]].

## Cơ chế & drivers
**Lãi suất hoà vốn** là hàm của lãi suất funding, biên hoà vốn, RoE và thuế suất. Lượng vốn cần cho khoản vay phụ thuộc trọng số rủi ro của tài sản; tài sản không cần vốn rủi ro (trái phiếu chính phủ AAA) có thể có biên thấp hơn [[src-choudhry-principles-banking#^choudhry-lp-3]].

| Ví dụ | Giả định chính | Lãi suất hoà vốn | Nguồn |
|---|---|---|---|
| 1.1 | Funding 5%, khoản vay được hỗ trợ bằng vốn 10 | 5,75% (biên hoà vốn 75bp) | [[src-choudhry-principles-banking#^choudhry-lp-2]] |
| 1.2 | Khoản vay 2 năm, xác suất vỡ nợ 5% ở năm 2, thu hồi 40% | 11,1% | [[src-choudhry-principles-banking#^choudhry-lp-4]] |

Khi đưa xác suất vỡ nợ và tỷ lệ thu hồi vào, định giá có yếu tố chủ quan, vì cả hai là giả định [[src-choudhry-principles-banking#^choudhry-lp-4]].

**Lãi suất khách hàng và reference rate.** Lãi suất khoản vay thường bằng lãi suất thị trường tiền tệ chuẩn cộng biên bù rủi ro tín dụng, liquidity premium, chi phí vận hành và lợi nhuận [[src-choudhry-principles-banking#^choudhry-ref-1]]. Ngân hàng cũng dùng lãi suất quản lý nội bộ (administered), như standard variable mortgage rate [[src-choudhry-principles-banking#^choudhry-ref-2]]. Xem [[basis-risk]].

**Mô hình định giá ChoudWest (Ví dụ 1.4)** [[src-choudhry-principles-banking#^choudhry-lp-6]]:
- ngoài định giá, mô hình xác định lợi nhuận sản phẩm, đánh giá chi phí phòng ngừa, và bảo đảm term liquidity premium (TLP) được tính vào giá;
- mô hình có "Target Rate of Return Floor Rate (TRR)" để bảo đảm ngưỡng chi phí vốn cho mọi khoản cho vay;
- ALCO được Board uỷ quyền phê duyệt khoản cho vay dưới TRR. Xem [[alco]].

Chi phí duy trì HQLA có thể được tính ở nơi khác, không nhất thiết trong mô hình định giá khoản vay [[src-choudhry-principles-banking#^choudhry-lp-5]]. Xem [[liquidity-transfer-pricing]].

## Phụ thuộc regime
[cần nguồn]

## Góc nhìn theo domain
- **ALM/FTP**: chi phí funding trong định giá là lãi suất chuyển giao nội bộ. Xem [[funds-transfer-pricing]].
- **Rủi ro tín dụng**: credit spread bù tổn thất dự kiến [[src-choudhry-principles-banking#^choudhry-lp-5]]. Xem [[expected-credit-loss]].
- **VN**: [cần nguồn]

*Diễn giải:* công thức lãi suất hoà vốn của Choudhry là cách tính RAROC ở cấp khoản vay, với RoE mục tiêu làm ngưỡng. TT83/2025 dùng RAROC ở cấp ngân hàng trong khẩu vị rủi ro; xem [[raroc]].

## Bằng chứng thực nghiệm
[cần nguồn]

## Câu hỏi mở
- Công thức của Ví dụ 1.1–1.3 bị mất hoặc vỡ khi convert; Table 1.8 (input mô hình định giá) là bảng rộng chưa trích. Cần đối chiếu PDF.
