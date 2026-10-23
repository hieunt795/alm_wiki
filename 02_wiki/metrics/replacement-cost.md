---
title: "Replacement Cost"
aliases: [Replacement Cost, RC, Chi phí thay thế]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[counterparty-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^pl2-4a]]"}
tags: [capital, counterparty-risk, derivatives, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Chi phí thay thế ($RC_j$) của giao dịch phái sinh j là chi phí xác định theo giá trị thị trường của giao dịch thay thế tương ứng với giá trị tài sản cơ sở và giá trị giao dịch gốc; chỉ lấy giá trị dương [[src-tt14-2025-nhnn#^pl2-4a]]. $RC_j$ cộng với [[potential-future-exposure]] tạo giá trị tín dụng đối tác trước khi trừ tài sản bảo đảm [[src-tt14-2025-nhnn#^pl2-4]].

## Công thức
$$
RWA_{CCR,j} = [(RC_j + PFE_j) - C_j] \times CRW
$$
[[src-tt14-2025-nhnn#^pl2-4]]

Raw viết "(RC_j + PFE_j) - C_j ]x CRW", thiếu dấu mở ngoặc vuông; wiki thêm dấu mở theo cấu trúc công thức, đây là tái dựng chưa đối chiếu bản gốc [[src-tt14-2025-nhnn#^pl2-4]].

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $RC_j$ | Chi phí thay thế | node này | [[src-tt14-2025-nhnn#^pl2-4a]] |
| $PFE_j$ | Giá trị tương lai trạng thái rủi ro | [[potential-future-exposure]] | [[src-tt14-2025-nhnn#^pl2-4b]] |
| $C_j$ | Giá trị tài sản đảm bảo, hiệu chỉnh theo Đ26; bằng 0 nếu không đáp ứng Đ26 | [[eligible-collateral-haircuts]] | [[src-tt14-2025-nhnn#^pl2-4c]] |
| CRW | Hệ số rủi ro tín dụng của đối tác | [[credit-risk-weight]] | [[src-tt14-2025-nhnn#^pl2-4c]] |

## Diễn giải
**Giá trị thị trường.** Giá trị giao dịch và tài sản cơ sở lấy theo giá trị thị trường (mark to market). Không có giá trị thị trường thì tính theo dữ liệu thị trường (mark to model); ngân hàng chịu trách nhiệm về phương pháp và báo cáo NHNN trước khi thực hiện [[src-tt14-2025-nhnn#^pl2-3]].

**Hoán đổi lãi suất thả nổi/thả nổi một đồng tiền.** $RWA_{CCR}$ tính theo giá trị thị trường của giao dịch, không tính PFE [[src-tt14-2025-nhnn#^pl2-4b2]].

*Diễn giải:* chỉ lấy $RC_j$ dương nghĩa là giao dịch phái sinh đang có giá trị âm cho ngân hàng không tạo rủi ro đối tác ở thành phần này. Ví dụ số do wiki dựng: giao dịch có giá trị thị trường +3 tỷ đồng cho ngân hàng thì $RC_j$ = 3 tỷ đồng; giá trị −3 tỷ đồng thì $RC_j$ = 0.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Định nghĩa $RC$ | [cần nguồn] (CRE chưa ingest) | Theo giá trị thị trường của giao dịch thay thế, chỉ lấy giá trị dương [[src-tt14-2025-nhnn#^pl2-4a]] | PL2.4a | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Định giá | [cần nguồn] | Mark to market; mark to model báo cáo NHNN trước [[src-tt14-2025-nhnn#^pl2-3]] | PL2.3 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* $RC_j$ thay đổi theo lãi suất và tỷ giá thị trường nên $RWA_{CCR}$ của phái sinh phòng ngừa IRRBB biến động theo đường cong lãi suất. [[capital-plan]] cần dự phóng $RC_j$ theo kịch bản lãi suất.

## Nhầm lẫn thường gặp
- $RC_j$ không bao gồm giá trị âm [[src-tt14-2025-nhnn#^pl2-4a]].
- $RC_j$ chưa trừ tài sản bảo đảm; việc trừ nằm ở $C_j$ [[src-tt14-2025-nhnn#^pl2-4]].
