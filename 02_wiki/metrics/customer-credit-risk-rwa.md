---
title: "Customer Credit Risk RWA"
aliases: [Customer Credit Risk RWA, RWA_CR, Tài sản có rủi ro tín dụng khách hàng]
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
tags: [capital, credit-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tổng tài sản có rủi ro tín dụng khách hàng ($RWA_{CR}$) là tổng các tài sản trên Báo cáo tình hình tài chính, tính theo hệ số rủi ro tín dụng [[src-tt14-2025-nhnn#^d8-2]]. $RWA_{CR}$ là một trong hai nhánh của [[risk-weighted-assets]] [[src-tt14-2025-nhnn#^d8-1]].

## Công thức
$$
RWA_{CR} = \sum E_j \times CRW_j + \sum \max\{0;\ E_i^{*} - SP_i\} \times CRW_i
$$
[[src-tt14-2025-nhnn#^d8-2]]

Công thức trên là cách viết lại của wiki theo công thức Đ8.2; dấu ngăn cách trong $\max$ do wiki chọn, nguồn viết "Max {0, (…)}" [[src-tt14-2025-nhnn#^d8-2]].

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $E_j$ | Giá trị tài sản thứ j không phải khoản phải đòi | node này | [[src-tt14-2025-nhnn#^d8-2-vars]] |
| $CRW_j$, $CRW_i$ | Hệ số rủi ro tín dụng theo Đ9 và Mục 2 Chương II | [[credit-risk-weight]] | [[src-tt14-2025-nhnn#^d8-2-vars]] |
| $E_i^{*}$ | Số dư khoản phải đòi thứ i sau giảm thiểu rủi ro tín dụng (Đ25–29) | [[exposure-value]] | [[src-tt14-2025-nhnn#^d8-2-vars]] |
| $SP_i$ | Dự phòng cụ thể của khoản phải đòi thứ i | [[specific-provision]] | [[src-tt14-2025-nhnn#^d8-2-vars]] |

## Diễn giải
Công thức trên là của phương pháp tiêu chuẩn (Chương II). Công thức IRB cho khoản phải đòi doanh nghiệp (RW = K × 12,5) nằm ở [[irb-capital-requirement]]. Ngân hàng được NHNN chấp thuận có thể tính $RWA_{CR}$ theo IRB cho từng nhóm tài sản, với tỷ lệ bao phủ tối thiểu 70% và tỷ lệ sàn đầu ra tối thiểu 72,5% ([[internal-ratings-based-approach]], [[irb-coverage-ratio]], [[output-floor]]) [[src-tt14-2025-nhnn#^d31-3]] [[src-tt14-2025-nhnn#^d35-12]].

Công thức chia tài sản thành hai nhóm. Nhóm thứ nhất là tài sản không phải khoản phải đòi (E_j), nhân thẳng với hệ số rủi ro. Nhóm thứ hai là khoản phải đòi (E_i), trừ dự phòng cụ thể rồi mới nhân hệ số [[src-tt14-2025-nhnn#^d8-2]].

*Diễn giải:* hàm max với 0 làm giá trị tính RWA không âm khi dự phòng cụ thể vượt số dư sau giảm thiểu. Ví dụ số do wiki dựng: số dư sau giảm thiểu 100 tỷ đồng, dự phòng cụ thể 20 tỷ đồng, CRW 100% thì đóng góp vào $RWA_{CR}$ là 80 tỷ đồng. Nguồn không đưa ví dụ số.

Cách tính $E_i^{*}$ và bốn biện pháp giảm thiểu rủi ro tín dụng (Đ25–29) nằm ở [[credit-risk-mitigation]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức | [cần nguồn] (CRE chưa ingest) | $\sum E_j \times CRW_j + \sum \max\{0; E_i^{*} - SP_i\} \times CRW_i$ [[src-tt14-2025-nhnn#^d8-2]] | Đ8.2 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Trừ dự phòng cụ thể | [cần nguồn] | Có, trước khi nhân CRW, sàn 0 [[src-tt14-2025-nhnn#^d8-2]] | Đ8.2 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* nhánh này chiếm phần chính của bảng cân đối: cho vay, tiền gửi liên ngân hàng, giấy tờ có giá, tài sản cố định. Trích lập dự phòng cụ thể giảm giá trị tính RWA, nên chính sách phân loại nợ và trích lập ảnh hưởng tới mẫu số CAR. Xem [[credit-risk-management]].

## Nhầm lẫn thường gặp
- Giao dịch đã tính trong [[counterparty-credit-risk-rwa]] không tính lại ở nhánh này [[src-tt14-2025-nhnn#^d8-5]].
- $SP_i$ là dự phòng của từng khoản phải đòi thứ i, trừ riêng cho khoản đó [[src-tt14-2025-nhnn#^d8-2-vars]]. Xem [[specific-provision]].
