---
title: "Internal Loss Multiplier"
aliases: [Internal Loss Multiplier, ILM, Hệ số tổn thất nội bộ]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[operational-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d70-1]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Hệ số tổn thất nội bộ (Internal loss multiplier, ILM) là hệ số nhân với [[business-indicator-component]] để ra $K_{OR}$ [[src-tt14-2025-nhnn#^d70-1]]. ILM phản ánh lịch sử tổn thất hoạt động của ngân hàng qua [[loss-component]] (LC) so với BIC [[src-tt14-2025-nhnn#^d70-3a]].

## Công thức
$$
ILM = \ln\left( e - 1 + \left( \frac{LC}{BIC} \right)^{0{,}8} \right)
$$
[[src-tt14-2025-nhnn#^d70-3a]]

LC là cấu phần tổn thất ([[loss-component]]) [[src-tt14-2025-nhnn#^d70-3a]]. Nguồn viết hằng số e dưới dạng $\exp(1)$ [[src-tt14-2025-nhnn#^d70-3a]].

## Diễn giải
**Khi ILM bằng 1.** ILM được đặt bằng 1 trong hai trường hợp [[src-tt14-2025-nhnn#^d70-3b]]:
- BI không quá 600 tỷ đồng;
- BI trên 600 tỷ đồng và chuỗi dữ liệu tổn thất để đo lường rủi ro hoạt động không đủ độ dài 05 năm.

**Khi tính LC.** Ngân hàng phải không thuộc hai trường hợp trên, và dữ liệu tổn thất phải đáp ứng Đ71 và Đ72 [[src-tt14-2025-nhnn#^d70-3c]]. Xem [[operational-loss-data]].

*Diễn giải:* khi LC bằng BIC thì $(LC/BIC)^{0{,}8}$ bằng 1 và ILM = ln(e) = 1. Khi LC lớn hơn BIC thì ILM lớn hơn 1 và $K_{OR}$ vượt BIC. Khi LC nhỏ hơn BIC thì ILM nhỏ hơn 1 và $K_{OR}$ thấp hơn BIC. Đây là suy ra toán học từ công thức Đ70.3a. Nguồn không nêu cận dưới hay trên của ILM [cần nguồn].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức | [cần nguồn] (OPE chưa ingest) | $\ln(e - 1 + (LC/BIC)^{0{,}8})$ [[src-tt14-2025-nhnn#^d70-3a]] | Đ70.3a | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Ngưỡng BI để ILM bằng 1 | [cần nguồn] | BI ≤ 600 tỷ đồng [[src-tt14-2025-nhnn#^d70-3b]] | Đ70.3b(i) | Như trên |
| Độ dài chuỗi dữ liệu tối thiểu | [cần nguồn] | 05 năm [[src-tt14-2025-nhnn#^d70-3b]] | Đ70.3b(ii) | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* ngân hàng có BI trên 600 tỷ đồng muốn dùng ILM theo tổn thất cần chuỗi dữ liệu đủ 05 năm và đạt chuẩn Đ71–72. Nếu chuỗi chưa đủ, ILM bằng 1 và $K_{OR}$ bằng BIC. Chất lượng dữ liệu tổn thất vì vậy quyết định ngân hàng có được hưởng ILM dưới 1 hay không.

## Nhầm lẫn thường gặp
- ILM bằng 1 không có nghĩa là ngân hàng không có tổn thất. Đó là trường hợp ngoại lệ về quy mô BI hoặc độ dài dữ liệu [[src-tt14-2025-nhnn#^d70-3b]].
- Tỷ số trong công thức là LC/BIC, không phải LC/BI [[src-tt14-2025-nhnn#^d70-3a]].
