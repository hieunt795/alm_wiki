---
title: "Probability of Default"
aliases: [Probability of Default, PD, Xác suất vỡ nợ]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[irb-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d41-1]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Xác suất vỡ nợ (PD) là khả năng khách hàng sẽ vỡ nợ, đo bằng số thập phân hoặc phần trăm [[src-tt14-2025-nhnn#^d2-31]]. Khách hàng vỡ nợ theo định nghĩa chín sự kiện của [[customer-default-definition]]. Ngân hàng tính PD tương ứng với xếp hạng của khách hàng [[src-tt14-2025-nhnn#^d41-1]].

## Công thức
Với khoản phải đòi doanh nghiệp:

$$
PD = \max\left( PD_{1Y}, \; 0{,}05\% \right)
$$
[[src-tt14-2025-nhnn#^d42-12]]

Trong đó $PD_{1Y}$ là PD trong vòng 01 năm của mức xếp hạng tín dụng nội bộ mà khoản phải đòi được xếp hạng [[src-tt14-2025-nhnn#^d42-12]].

## Diễn giải
- Sàn PD 0,05% áp dụng cho khoản phải đòi doanh nghiệp [[src-tt14-2025-nhnn#^d42-12]].
- Khi có bảo lãnh hoặc phái sinh tín dụng, phần được giảm thiểu dùng PD của bên bảo lãnh hoặc bên phát hành; bên đó phải có PD thấp hơn bên được bảo vệ [[src-tt14-2025-nhnn#^d45-12]] [[src-tt14-2025-nhnn#^d46-12]]. Xem [[irb-credit-risk-mitigation]].
- PD là đầu vào của hệ số tương quan [[asset-correlation]] và điều chỉnh kỳ hạn [[maturity-adjustment]] ngoài việc xuất hiện trực tiếp trong K [[src-tt14-2025-nhnn#^d41-2c]].

**Khoản phải đòi bán lẻ (Đ50).** PD là giá trị lớn hơn giữa PD ngân hàng tính và PD sàn: 0,1% cho QRRE, 0,05% cho khoản bán lẻ còn lại [[src-tt14-2025-nhnn#^d50-1]]. Khác doanh nghiệp, PD bán lẻ do ngân hàng tính theo AIRB; yêu cầu ước tính xem [[irb-retail-parameter-estimation]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Sàn PD khoản phải đòi doanh nghiệp | [cần nguồn] (CRE32 chưa ingest) | 0,05% [[src-tt14-2025-nhnn#^d42-12]] | Đ42.1 | Khi áp dụng IRB |
| Sàn PD bán lẻ | [cần nguồn] | 0,1% QRRE; 0,05% khoản còn lại [[src-tt14-2025-nhnn#^d50-1]] | Đ50 | Khi áp dụng IRB |

## Ứng dụng trong ALM
*Diễn giải:* PD gắn với hệ thống xếp hạng nội bộ và dữ liệu vỡ nợ lịch sử của ngân hàng. Yêu cầu tối thiểu với hệ thống xếp hạng xem [[irb-rating-system-design]]; ước tính PD (dữ liệu tối thiểu 05 năm liên tục, tỷ lệ vỡ nợ trung bình 01 năm) xem [[irb-parameter-estimation-requirements]] [[src-tt14-2025-nhnn#^d68-1]].

## Nhầm lẫn thường gặp
- PD trong công thức là PD 01 năm của mức xếp hạng, không phải PD theo kỳ hạn của khoản vay [[src-tt14-2025-nhnn#^d42-12]].
