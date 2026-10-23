---
title: "Counterparty Credit Risk RWA"
aliases: [Counterparty Credit Risk RWA, RWA_CCR, Tài sản có rủi ro tín dụng đối tác, Rủi ro tín dụng đối tác]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[risk-weighted-assets]]", cite: "[[src-tt14-2025-nhnn#^d8-1]]"}
tags: [capital, credit-risk, counterparty-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tổng tài sản có rủi ro tín dụng đối tác ($RWA_{CCR}$) là nhánh thứ hai của [[risk-weighted-assets]] [[src-tt14-2025-nhnn#^d8-1]]. $RWA_{CCR}$ được tính cho bốn nhóm giao dịch: tự doanh; mua lại và mua lại đảo ngược; phái sinh phòng ngừa rủi ro; mua bán ngoại tệ, tài sản tài chính phục vụ nhu cầu của khách hàng, đối tác theo Đ2.24d [[src-tt14-2025-nhnn#^d8-4]]. Cách tính nằm ở Phụ lục II [[src-tt14-2025-nhnn#^d8-5]].

## Công thức
Công thức phụ thuộc loại giao dịch. Giao dịch đã tính $RWA_{CCR}$ không tính lại ở [[customer-credit-risk-rwa]] [[src-tt14-2025-nhnn#^d8-5]].

| Giao dịch | Công thức | Nguồn |
|---|---|---|
| Với Trung tâm thanh toán tập trung, Trung tâm lưu ký chứng khoán; ngân hàng bán quyền chọn (short options) | Rủi ro tín dụng đối tác bằng 0 | [[src-tt14-2025-nhnn#^pl2-1]] |
| Phái sinh | $RWA_{CCR,j} = [(RC_j + PFE_j) - C_j] \times CRW$ | [[src-tt14-2025-nhnn#^pl2-4]] |
| Repo và reverse repo | $RWA_{CCR,j} = \max\{0;\ E_j - C_j (1 - H_c - H_{fx})\} \times CRW$ | [[src-tt14-2025-nhnn#^pl2-5]] |
| Mua có kỳ hạn tài sản tài chính theo quy định chiết khấu công cụ chuyển nhượng, giấy tờ có giá khác | $RWA_{CCR} = E_j \times CRW$ | [[src-tt14-2025-nhnn#^pl2-6]] |
| Thanh toán đồng thời, đối tác chậm thanh toán từ 05 ngày | $GD \times r$ (tái dựng) | [[src-tt14-2025-nhnn#^pl2-7]] |
| Không thỏa thuận thanh toán đồng thời, đối tác chưa thực hiện trong 05 ngày làm việc | $RWA_{CCR} = E_j \times CRW$; sau đó trừ vốn tự có | [[src-tt14-2025-nhnn#^pl2-8]] |

Ký hiệu của wiki (dấu $\max\{0;\ \cdot\}$) là cách viết lại; raw ghi công thức phái sinh với dấu ngoặc không cân ("(RC + PFE) - C ]x CRW") và công thức repo "(0, E - C x (1-Hc-Hfx))]}x CRW" [[src-tt14-2025-nhnn#^pl2-4]] [[src-tt14-2025-nhnn#^pl2-5]]. Cấu trúc công thức repo trùng với ví dụ số của nguồn, xem phần Diễn giải.

**Phái sinh (PL2.4).** Các đại lượng:

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $RC_j$ | Chi phí thay thế | [[replacement-cost]] | [[src-tt14-2025-nhnn#^pl2-4a]] |
| $PFE_j$ | Giá trị tương lai trạng thái rủi ro, bằng vốn danh nghĩa nhân chỉ số tăng thêm | [[potential-future-exposure]] | [[src-tt14-2025-nhnn#^pl2-4b]] |
| $C_j$ | Giá trị tài sản đảm bảo, hiệu chỉnh theo Đ26; bằng 0 nếu không đáp ứng Đ26 | [[eligible-collateral-haircuts]] | [[src-tt14-2025-nhnn#^pl2-4c]] |
| CRW | Hệ số rủi ro tín dụng của đối tác theo Mục 2 Chương II | [[credit-risk-weight]] | [[src-tt14-2025-nhnn#^pl2-4c]] |

Chỉ số tăng thêm: xem [[add-on-factor]].

**Repo và reverse repo (PL2.5).** Hc là hệ số hiệu chỉnh của tài sản cơ sở theo Đ26; $H_{fx}$ là hệ số hiệu chỉnh độ lệch tiền tệ, bằng 8% [[src-tt14-2025-nhnn#^pl2-5v]].

| Vai trò của ngân hàng | $E_j$ | $C_j$ | Nguồn |
|---|---|---|---|
| Mua có kỳ hạn | Giá trị mua lại theo thỏa thuận | Giá trị tài sản cơ sở | [[src-tt14-2025-nhnn#^pl2-5v]] |
| Bán có kỳ hạn | Giá trị tài sản cơ sở | Giá trị mua lại theo thỏa thuận | [[src-tt14-2025-nhnn#^pl2-5v]] |

**Giao dịch có ký quỹ, tài sản bảo đảm.** Giá trị giao dịch được giảm trừ số tiền ký quỹ và giảm thiểu rủi ro theo tài sản bảo đảm quy định tại Đ26 [[src-tt14-2025-nhnn#^pl2-2]]. Xem [[eligible-collateral-haircuts]].

**Bù trừ hai bên.** Xem [[bilateral-netting]]. **Chậm thanh toán.** Xem [[settlement-failure-risk-weighting]].

## Diễn giải
**Ví dụ của nguồn: mua bán có kỳ hạn.** Ngân hàng A (xếp hạng B+) ký hợp đồng mua bán có kỳ hạn với Ngân hàng B (không xếp hạng) đối với 100 tỷ đồng trái phiếu 10 năm của Ngân hàng C (không xếp hạng), thời hạn 3 tháng, giá trị mua lại 98 tỷ đồng, giá trị thị trường 99 tỷ đồng. Hc của trái phiếu theo Đ26 là 12% [[src-tt14-2025-nhnn#^pl2-vd1]].

| Bên | CRW đối tác | $RWA_{CCR}$ | Nguồn |
|---|---|---|---|
| Ngân hàng A (bên bán) | 70% | (99 − 98 × (1 − 0,12)) × 70% = 8,932 tỷ đồng | [[src-tt14-2025-nhnn#^pl2-vd2]] |
| Ngân hàng B (bên mua) | 50% | (98 − 99 × (1 − 0,12)) × 50% = 5,44 tỷ đồng | [[src-tt14-2025-nhnn#^pl2-vd3]] |

*Diễn giải:* wiki kiểm lại phép tính của ví dụ: (99 − 86,24) × 0,7 = 8,932 và (98 − 87,12) × 0,5 = 5,44. Cả hai khớp số của nguồn. CRW của đối tác trong ví dụ (70% cho đối tác không xếp hạng kỳ hạn dưới 03 tháng, 50% cho đối tác xếp hạng B+ cùng kỳ hạn) khớp bảng Đ14.3 ([[sovereign-and-bank-exposure-risk-weighting]]). Cả hai bên cùng tính $RWA_{CCR}$ trên một giao dịch, nên bên bán và bên mua đều có tài sản tính theo rủi ro đối tác dương khi tài sản cơ sở và tiền mua lại chênh nhau.

**Mark to market.** Giá trị giao dịch và tài sản cơ sở lấy theo giá trị thị trường (mark to market). Mark to model phải báo cáo NHNN trước khi thực hiện [[src-tt14-2025-nhnn#^pl2-3]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Phạm vi giao dịch | [cần nguồn] (CRE chưa ingest) | Bốn nhóm giao dịch [[src-tt14-2025-nhnn#^d8-4]] | Đ8.4 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Giao dịch với trung tâm thanh toán tập trung, bán quyền chọn | [cần nguồn] | Bằng 0 [[src-tt14-2025-nhnn#^pl2-1]] | PL2.1 | Như trên |
| Phái sinh | [cần nguồn] | (RC + PFE − C) × CRW [[src-tt14-2025-nhnn#^pl2-4]] | PL2.4 | Như trên |
| Repo, reverse repo | [cần nguồn] | max{0; E − C(1 − Hc − Hfx)} × CRW; Hfx 8% [[src-tt14-2025-nhnn#^pl2-5]] [[src-tt14-2025-nhnn#^pl2-5v]] | PL2.5 | Như trên |
| Chậm thanh toán | [cần nguồn] | 8% / 50% / 75% / 100% theo số ngày [[src-tt14-2025-nhnn#^pl2-7]] | PL2.7 | Như trên |
| Bù trừ hai bên | [cần nguồn] | $A_{Net} = A_{Gross}(0{,}4 + 0{,}6 \times NGR)$ [[src-tt14-2025-nhnn#^pl2-10]] | PL2.10 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* repo, phái sinh phòng ngừa IRRBB và giao dịch ngoại tệ của Treasury làm $RWA_{CCR}$ tăng. Phái sinh lãi suất có chỉ số tăng thêm thấp (0,0% đến 1,5%) so với ngoại hối (1,0% đến 7,5%) [[src-tt14-2025-nhnn#^pl2-4b]]. [[capital-plan]] cần dự phóng nhánh này riêng khỏi cho vay. Hệ thống ghi nhận giao dịch phải gắn cờ nhóm giao dịch để tránh tính trùng với $RWA_{CR}$ và để áp đúng công thức.

## Nhầm lẫn thường gặp
- Rủi ro tín dụng đối tác không phải rủi ro thị trường của giao dịch. Rủi ro thị trường tính ở [[market-risk-capital-requirement]].
- Giao dịch trong bốn nhóm không tính lại ở $RWA_{CR}$ [[src-tt14-2025-nhnn#^d8-5]].
- Trong công thức repo, vai trò của $E_j$ và $C_j$ đảo nhau giữa bên mua và bên bán [[src-tt14-2025-nhnn#^pl2-5v]].
