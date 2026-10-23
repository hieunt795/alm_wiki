---
title: "Add-on Factor"
aliases: [Add-on Factor, Chỉ số tăng thêm]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[potential-future-exposure]]", cite: "[[src-tt14-2025-nhnn#^pl2-4b]]"}
tags: [capital, counterparty-risk, derivatives, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Chỉ số tăng thêm (add-on factor) là tỷ lệ phần trăm trên vốn danh nghĩa, do NHNN ấn định theo loại tài sản cơ sở và thời hạn còn lại, dùng để tính [[potential-future-exposure]] [[src-tt14-2025-nhnn#^pl2-4b]]. Đây là tham số do cơ quan quản lý ấn định, nên không phải metric.

## Cơ chế & drivers
**Phái sinh thông thường** [[src-tt14-2025-nhnn#^pl2-4b]]:

| Thời hạn còn lại | Lãi suất | Ngoại hối (gồm vàng tiêu chuẩn) | Cổ phiếu, chứng chỉ quỹ, chứng quyền | Kim loại quý (trừ vàng) | Các hàng hóa khác |
|---|---|---|---|---|---|
| Từ 01 năm trở xuống | 0,0% | 1,0% | 6,0% | 7,0% | 10,0% |
| Trên 01 năm đến 05 năm | 0,5% | 5,0% | 8,0% | 7,0% | 12,0% |
| Trên 05 năm | 1,5% | 7,5% | 10,0% | 8,0% | 15,0% |

"Các hàng hóa khác" gồm hợp đồng kỳ hạn, hoán đổi, quyền chọn mua và phái sinh tương tự không thuộc các cột còn lại [[src-tt14-2025-nhnn#^pl2-4b2]].

**Phái sinh tín dụng** [[src-tt14-2025-nhnn#^pl2-4b3]]:

| Giao dịch | Nghĩa vụ tham chiếu | Chỉ số tăng thêm |
|---|---|---|
| Hoán đổi lợi nhuận tổng | Đủ tiêu chuẩn | 5% |
| Hoán đổi lợi nhuận tổng | Không đủ tiêu chuẩn | 10% |
| Hoán đổi vỡ nợ tín dụng | Đủ tiêu chuẩn | 5% |
| Hoán đổi vỡ nợ tín dụng | Không đủ tiêu chuẩn | 10% |

Nghĩa vụ tham chiếu đủ tiêu chuẩn (với hoán đổi lợi nhuận tổng) là nghĩa vụ của tổ chức tài chính công lập của chính phủ, ngân hàng phát triển hoặc các hợp đồng hoán đổi khác có xếp hạng từ Baa trở lên của Moody hoặc BBB trở lên của Standard & Poor's, Fitch Rating [[src-tt14-2025-nhnn#^pl2-4b3]]. Nguồn không nêu riêng tiêu chuẩn cho hoán đổi vỡ nợ tín dụng [cần nguồn].

**Quy tắc khác.** Hợp đồng lãi suất có thời hạn còn lại trên 01 năm mà đáp ứng điều kiện định lại giá trị thị trường bằng 0 (xem [[potential-future-exposure]]) có chỉ số tăng thêm 0,5% [[src-tt14-2025-nhnn#^pl2-4b1]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Bảng không có cột hàng hóa riêng cho dầu thô hay nông sản; các loại này nằm trong "Các hàng hóa khác" [[src-tt14-2025-nhnn#^pl2-4b2]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* hệ số lãi suất thấp (0,0% đến 1,5%) so với ngoại hối (1,0% đến 7,5%), nên cùng vốn danh nghĩa, hoán đổi tiền tệ chéo ([[cross-currency-swap]]) tạo $RWA_{CCR}$ lớn hơn hoán đổi lãi suất cùng thời hạn. Hoán đổi lãi suất thời hạn trên 05 năm có 1,5%.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Chỉ số tăng thêm cho quyền chọn bán đã bán (ngân hàng bán quyền chọn) bằng 0 theo PL2.1, không theo bảng này [[src-tt14-2025-nhnn#^pl2-1]].
