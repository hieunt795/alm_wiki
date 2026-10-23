---
title: "Equity Risk Capital Requirement"
aliases: [Equity Risk Capital Requirement, K_ER, KER, Vốn yêu cầu cho rủi ro giá cổ phiếu]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[market-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d74-1]]"}
tags: [capital, market-risk, equity, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho rủi ro giá cổ phiếu ($K_{ER}$) là cấu phần của $K_{MR}$ cho giao dịch không phải quyền chọn [[src-tt14-2025-nhnn#^d74-1]]. $K_{ER}$ gồm vốn cho rủi ro giá cổ phiếu cụ thể ($K_{ER}^{SR}$) và chung ($K_{ER}^{GR}$) [[src-tt14-2025-nhnn#^d74-3]]. Xem [[market-risk-capital-requirement]].

Phạm vi là trạng thái cổ phiếu trên sổ kinh doanh: cổ phiếu, trái phiếu chuyển đổi và chứng khoán phái sinh có tài sản gốc là cổ phiếu (trừ quyền chọn), trừ cổ phiếu, trái phiếu chuyển đổi đã trừ khỏi vốn tự có theo Phụ lục I [[src-tt14-2025-nhnn#^pl4-ii-1]].

## Công thức
$$
K_{ER}^{SR} = (LP + SP) \times 8\%
$$
[[src-tt14-2025-nhnn#^pl4-ii-34]]

$$
K_{ER}^{GR} = \left| LP - SP \right| \times ERW
$$
[[src-tt14-2025-nhnn#^pl4-ii-34]]

$$
K_{ER} = K_{ER}^{SR} + K_{ER}^{GR}
$$
[[src-tt14-2025-nhnn#^d74-3]]

Dạng tổng $K_{ER}$ là cách đọc của wiki: Đ74.3 nêu công thức nhưng raw không giữ, và gọi hai thành phần là $K_{ER}^{SR}$, $K_{ER}^{GR}$ [[src-tt14-2025-nhnn#^d74-3]]. Chưa đối chiếu bản gốc [cần nguồn]. Nguồn viết "(LP + SP)" và định nghĩa SP là trạng thái cổ phiếu âm; cách lấy dấu của SP trong tổng không được nêu rõ [cần nguồn].

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| LP | Trạng thái cổ phiếu dương (long position) | [[src-tt14-2025-nhnn#^pl4-ii-34]] |
| SP | Trạng thái cổ phiếu âm (short position) | [[src-tt14-2025-nhnn#^pl4-ii-34]] |
| ERW | Hệ số rủi ro chung giá cổ phiếu: 8% với cổ phiếu, công cụ có tính chất cổ phiếu (như trái phiếu chuyển đổi) và chứng khoán phái sinh có tài sản cơ sở là cổ phiếu; 10% với hợp đồng phái sinh có tài sản gốc là chỉ số chứng khoán | [[src-tt14-2025-nhnn#^pl4-ii-34]] |

## Diễn giải
**Xác định trạng thái.** Trạng thái dương (âm) của một loại cổ phiếu hoặc công cụ có tính chất cổ phiếu do một tổ chức phát hành được bù trừ [[src-tt14-2025-nhnn#^pl4-ii-1]]. Phái sinh cổ phiếu quy đổi thành trạng thái danh nghĩa [[src-tt14-2025-nhnn#^pl4-ii-2b]]:
- hợp đồng tương lai, kỳ hạn có tài sản gốc là cổ phiếu lấy theo giá trị thị trường;
- hợp đồng kỳ hạn theo chỉ số chứng khoán xác định theo giá trị thị trường của danh mục trong chỉ số;
- hoán đổi ghi nhận đồng thời hai trạng thái theo nghĩa vụ cam kết: dương khi nhận khoản dựa trên thay đổi giá trị cổ phiếu hoặc chỉ số, âm khi phải trả; nếu một vế gắn với lãi suất cố định hoặc thả nổi thì tính thêm trạng thái rủi ro lãi suất ([[interest-rate-risk-capital-requirement]]).

*Diễn giải:* ví dụ số do wiki dựng, giả định SP lấy giá trị tuyệt đối: LP = 100 tỷ đồng, SP = 40 tỷ đồng, ERW 8%. Khi đó $K_{ER}^{SR}$ = (100 + 40) × 8% = 11,2 tỷ đồng và $K_{ER}^{GR}$ = |100 − 40| × 8% = 4,8 tỷ đồng. Giả định về dấu của SP chưa có nguồn [cần nguồn].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Hệ số rủi ro cụ thể | [cần nguồn] (MAR chưa ingest) | 8% [[src-tt14-2025-nhnn#^pl4-ii-34]] | PL4.B.II.3 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Hệ số rủi ro chung | [cần nguồn] | 8% cổ phiếu; 10% phái sinh theo chỉ số chứng khoán [[src-tt14-2025-nhnn#^pl4-ii-34]] | PL4.B.II.4 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* $K_{ER}$ chỉ phát sinh khi sổ kinh doanh có vị thế cổ phiếu hoặc phái sinh cổ phiếu. Cổ phiếu trong sổ ngân hàng (đầu tư dài hạn, góp vốn) không vào $K_{ER}$ nhưng có thể bị trừ khỏi vốn tự có ([[capital-deductions]]).

## Nhầm lẫn thường gặp
- Hợp đồng quyền chọn cổ phiếu không tính vào $K_{ER}$ mà vào [[options-risk-capital-requirement]] [[src-tt14-2025-nhnn#^pl4-ii-1]].
- Trái phiếu chuyển đổi tính ở $K_{ER}$, không tính ở rủi ro lãi suất [[src-tt14-2025-nhnn#^pl4-i-1]].
