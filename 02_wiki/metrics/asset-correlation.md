---
title: "Asset Correlation (R)"
aliases: [Asset Correlation, Hệ số tương quan R, Hệ số tương quan IRB]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[irb-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d41-2d]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Hệ số tương quan R trong công thức K của IRB đo mức độ khoản phải đòi phụ thuộc vào nhân tố hệ thống; R là hàm của PD và nằm giữa 0,12 và 0,24 [[src-tt14-2025-nhnn#^d41-2d]]. Phần "đo mức độ phụ thuộc vào nhân tố hệ thống" là cách đọc của wiki, nguồn TT14 chỉ nêu công thức [cần nguồn Basel CRE31].

## Công thức
$$
R = 0{,}12 \times \frac{1 - e^{-50 \times PD}}{1 - e^{-50}} + 0{,}24 \times \left( 1 - \frac{1 - e^{-50 \times PD}}{1 - e^{-50}} \right)
$$
[[src-tt14-2025-nhnn#^d41-2d]]

Điều chỉnh theo quy mô cho doanh nghiệp nhỏ và vừa: ngân hàng được thay R bằng R trên trừ thêm số hạng điều chỉnh [[src-tt14-2025-nhnn#^d41-3a]].

| Lĩnh vực doanh nghiệp nhỏ và vừa | Số hạng trừ khỏi R | Khoảng S |
|---|---|---|
| Nông nghiệp, lâm nghiệp, thủy sản; công nghiệp và xây dựng | $0{,}04 \times \left( 1 - \frac{S - 20}{180} \right)$ | 20 đến 200 tỷ đồng [[src-tt14-2025-nhnn#^d41-3b]] |
| Thương mại và dịch vụ | $0{,}04 \times \left( 1 - \frac{S - 30}{270} \right)$ | 30 đến 300 tỷ đồng [[src-tt14-2025-nhnn#^d41-3b]] |

$S$ là tổng doanh thu bán hàng và cung cấp dịch vụ của năm, đơn vị tỷ đồng [[src-tt14-2025-nhnn#^d41-3a]].

## Diễn giải
- S dưới sàn (20 hoặc 30 tỷ đồng) hoặc doanh nghiệp mới thành lập dưới 01 năm chưa có doanh thu thì dùng S bằng sàn; S trên trần (200 hoặc 300 tỷ đồng) thì dùng trần [[src-tt14-2025-nhnn#^d41-3b]].
- S lấy từ báo cáo tài chính năm gần nhất: báo cáo đã kiểm toán (hợp nhất nếu phải lập) với doanh nghiệp phải kiểm toán; báo cáo kiểm toán (nếu có) hoặc báo cáo nộp cơ quan thuế có bằng chứng với doanh nghiệp không phải kiểm toán [[src-tt14-2025-nhnn#^d41-3a]].
- Điều chỉnh là quyền chọn ("được phép") của ngân hàng, không bắt buộc [[src-tt14-2025-nhnn#^d41-3a]].

*Diễn giải:* số hạng điều chỉnh bằng 0,04 khi S ở sàn và bằng 0 khi S ở trần, nên R của doanh nghiệp nhỏ giảm tối đa 0,04 so với R thông thường. Kiểm số học theo công thức: S = 20 (nhóm a) cho $1 - 0 = 1$, giảm 0,04; S = 200 cho $1 - 1 = 0$, không giảm.

**Khoản phải đòi bán lẻ (Đ49).** R cố định hoặc theo PD tùy nhóm:

| Nhóm | R | Nguồn |
|---|---|---|
| Cho vay thế chấp nhà ở | 0,15 | [[src-tt14-2025-nhnn#^d49-2]] |
| Bán lẻ quay vòng đủ tiêu chuẩn (QRRE) | 0,04 | [[src-tt14-2025-nhnn#^d49-3]] |
| Cấp tín dụng bán lẻ khác | $0{,}03 \times \frac{1 - e^{-35 \times PD}}{1 - e^{-35}} + 0{,}16 \times \left( 1 - \frac{1 - e^{-35 \times PD}}{1 - e^{-35}} \right)$ | [[src-tt14-2025-nhnn#^d49-4]] |

Nguồn viết hệ số thứ hai là "0.16" (dấu chấm) trong khi các số khác dùng dấu phẩy; wiki đọc là 0,16. Với bán lẻ khác, R nằm giữa 0,03 (PD lớn) và 0,16 (PD nhỏ), khác khoảng 0,12–0,24 của doanh nghiệp.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| R: hệ số 0,12 và 0,24, mũ 50 | [cần nguồn] (CRE31 chưa ingest) | Như công thức trên [[src-tt14-2025-nhnn#^d41-2d]] | Đ41.2d | Khi áp dụng IRB |
| Điều chỉnh doanh nghiệp nhỏ và vừa | [cần nguồn] | Giảm tối đa 0,04, S theo tỷ đồng [[src-tt14-2025-nhnn#^d41-3a]] | Đ41.3 | Như trên |
| R bán lẻ | [cần nguồn] | 0,15 (thế chấp nhà ở); 0,04 (QRRE); 0,03–0,16 theo PD với bán lẻ khác [[src-tt14-2025-nhnn#^d49-4]] | Đ49.2d, 49.3d, 49.4d | Khi áp dụng IRB |

## Ứng dụng trong ALM
*Diễn giải:* R thấp hơn làm K thấp hơn ở cùng PD và LGD. Ngân hàng có danh mục doanh nghiệp nhỏ và vừa có thể cân nhắc quyền chọn Đ41.3 và chi phí thu thập báo cáo tài chính đáng tin cậy.

## Nhầm lẫn thường gặp
- Ngưỡng 20 đến 200 và 30 đến 300 là đơn vị tỷ đồng của doanh thu, không phải định nghĩa quy mô doanh nghiệp nhỏ và vừa.
