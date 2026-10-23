---
title: "Market Risk Capital Requirement"
aliases: [Market Risk Capital Requirement, K_MR, KMR, Vốn yêu cầu cho rủi ro thị trường]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[capital-adequacy-ratio]]", cite: "[[src-tt14-2025-nhnn#^d5-1d]]"}
tags: [capital, market-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho rủi ro thị trường ($K_{MR}$) là cấu phần của mẫu số tỷ lệ an toàn vốn, nhân 12,5 cùng với $K_{OR}$ [[src-tt14-2025-nhnn#^d5-1d]]. Xem [[capital-adequacy-ratio]]. $K_{MR}$ là tổng năm cấu phần theo Đ74.1 [[src-tt14-2025-nhnn#^d74-1]].

Rủi ro thị trường theo TT14/2025 là rủi ro do biến động bất lợi của lãi suất, tỷ giá, giá vàng, giá chứng khoán và giá hàng hoá [[src-tt14-2025-nhnn#^d2-19]]. Rủi ro lãi suất trong đó gắn với giá trị giấy tờ có giá, công cụ có lãi suất và phái sinh lãi suất trên sổ kinh doanh [[src-tt14-2025-nhnn#^d2-19a]]. Vị thế đưa vào $K_{MR}$ xác định theo ranh giới hai sổ ([[banking-book]]).

## Công thức
$$
K_{MR} = K_{IRR} + K_{ER} + K_{FXR} + K_{CMR} + K_{OPT}
$$
[[src-tt14-2025-nhnn#^d74-1]]

| Cấu phần | Ý nghĩa | Điều kiện áp dụng | Nguồn |
|---|---|---|---|
| $K_{IRR}$ | Rủi ro lãi suất, trừ quyền chọn; gồm hai thành phần $K_{IRR}^{SR}$ và $K_{IRR}^{GR}$ | Không có ngưỡng; tính theo Phụ lục IV | [[src-tt14-2025-nhnn#^d74-1]] [[src-tt14-2025-nhnn#^d74-2]] |
| $K_{ER}$ | Rủi ro giá cổ phiếu, trừ quyền chọn; gồm $K_{ER}^{SR}$ và $K_{ER}^{GR}$ | Không có ngưỡng; tính theo Phụ lục IV | [[src-tt14-2025-nhnn#^d74-1]] [[src-tt14-2025-nhnn#^d74-3]] |
| $K_{FXR}$ | Rủi ro ngoại hối (gồm vàng), trừ quyền chọn | Chỉ áp dụng khi tổng trạng thái ngoại hối ròng (gồm vàng) lớn hơn 2% vốn tự có | [[src-tt14-2025-nhnn#^d74-4]] |
| $K_{CMR}$ | Rủi ro giá hàng hoá, trừ quyền chọn | Không có ngưỡng; tính theo Phụ lục IV | [[src-tt14-2025-nhnn#^d74-5]] |
| $K_{OPT}$ | Giao dịch quyền chọn | Chỉ áp dụng khi tổng giá trị các giao dịch quyền chọn lớn hơn 2% vốn tự có | [[src-tt14-2025-nhnn#^d74-6]] |

Ý nghĩa của các ký hiệu SR và GR, hệ số vốn và cách tính từng cấu phần nằm ở Phụ lục IV [cần nguồn: Phụ lục IV chưa ingest]. Ngưỡng 2% lấy [[own-funds]] làm cơ sở.

## Diễn giải
**Quy định nội bộ bắt buộc (Đ73).** Để xác định $K_{MR}$, ngân hàng phải có quy định nội bộ đáp ứng tối thiểu các nội dung của Đ73.1 [[src-tt14-2025-nhnn#^d73-1]]:
- tiêu chí xác định khoản mục thuộc sổ kinh doanh, phân biệt hai sổ và việc chuyển khoản mục [[src-tt14-2025-nhnn#^d73-1a]];
- dữ liệu giao dịch ghi nhận chính xác, đầy đủ, kịp thời, và xác định được bộ phận kinh doanh [[src-tt14-2025-nhnn#^d73-1b]];
- kiểm toán nội bộ định kỳ rà soát khoản mục hai sổ [[src-tt14-2025-nhnn#^d73-1d]];
- chiến lược tự doanh cho từng loại tiền tệ, công cụ, phái sinh [[src-tt14-2025-nhnn#^d73-1dd]];
- hạn mức rà soát tối thiểu hằng năm hoặc khi có thay đổi lớn [[src-tt14-2025-nhnn#^d73-1e]];
- quy trình quản lý trạng thái gồm bộ phận tự doanh riêng, bộ phận quản lý và hạch toán, báo cáo cho các cấp thẩm quyền [[src-tt14-2025-nhnn#^d73-1g]];
- định giá trạng thái sổ kinh doanh theo giá hoặc dữ liệu thị trường ít nhất 01 lần mỗi ngày làm việc, và rà soát dữ liệu đầu vào [[src-tt14-2025-nhnn#^d73-1g2]];
- phương pháp đo lường có giả định và tham số được mô tả, rà soát hằng năm [[src-tt14-2025-nhnn#^d73-1h]];
- nguyên tắc tính vốn đáp ứng Phụ lục IV [[src-tt14-2025-nhnn#^d73-1k]].

**Phê duyệt và gửi NHNN.** Các cấp có thẩm quyền của ngân hàng phê duyệt quy định nội bộ, và kiểm toán nội bộ rà soát tối thiểu hằng năm [[src-tt14-2025-nhnn#^d73-3]]. Ngân hàng gửi quy định cho NHNN để giám sát trước khi thực hiện, và NHNN có thể có ý kiến bằng văn bản yêu cầu sửa đổi [[src-tt14-2025-nhnn#^d73-4]].

**Chuyển sổ.** Ngân hàng chỉ được chuyển khoản mục từ sổ kinh doanh sang sổ ngân hàng khi khoản mục không còn đáp ứng tiêu chí nội bộ. Ngân hàng không được chuyển công cụ tài chính từ sổ ngân hàng sang sổ kinh doanh [[src-tt14-2025-nhnn#^d73-2b]]. Giao dịch hai sổ phải phản ánh trên sổ sách kế toán và đối chiếu với số liệu của bộ phận kinh doanh [[src-tt14-2025-nhnn#^d73-2a]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu phần của vốn rủi ro thị trường | [cần nguồn] (MAR chưa ingest) | $K_{IRR}$, $K_{ER}$, $K_{FXR}$, $K_{CMR}$, $K_{OPT}$ [[src-tt14-2025-nhnn#^d74-1]] | Đ74.1 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Ngưỡng bắt đầu tính vốn ngoại hối | [cần nguồn] | Trạng thái ngoại hối ròng > 2% vốn tự có [[src-tt14-2025-nhnn#^d74-4]] | Đ74.4 | Như trên |
| Ngưỡng bắt đầu tính vốn quyền chọn | [cần nguồn] | Tổng giá trị quyền chọn > 2% vốn tự có [[src-tt14-2025-nhnn#^d74-6]] | Đ74.6 | Như trên |
| Chuyển sổ kinh doanh sang sổ ngân hàng | Cần chấp thuận của cơ quan giám sát; chuyển ngược (trading → banking) luôn cần chấp thuận [[src-bcbs-framework#^rbc25-16-faq2]] | Chỉ khi khoản mục không còn đáp ứng tiêu chí nội bộ [[src-tt14-2025-nhnn#^d73-2b]] | RBC25.16, Đ73.2b | Như trên |
| Chuyển sổ ngân hàng sang sổ kinh doanh | Hạn chế: chỉ trong hoàn cảnh đặc biệt, cần chấp thuận trước, trừ trường hợp phân loại lại thành tài sản/nợ kinh doanh theo kế toán [[src-bcbs-framework#^rbc25-14]] [[src-bcbs-framework#^rbc25-16]] | Không được phép [[src-tt14-2025-nhnn#^d73-2b]] | RBC25.14, RBC25.16, Đ73.2c | Như trên |

*Diễn giải:* hướng chuyển sổ của hai khung khác nhau. Basel cho phép chuyển cả hai chiều với điều kiện chấp thuận; Đ73.2 cấm chiều từ sổ ngân hàng sang sổ kinh doanh. Đây là khác biệt jurisdiction, không phải conflict. Cột Basel của các dòng ngưỡng chờ ingest MAR.

## Ứng dụng trong ALM
*Diễn giải:* IRRBB trên sổ ngân hàng không có cấu phần nào trong $K_{MR}$. $K_{IRR}$ chỉ tính cho vị thế sổ kinh doanh [[src-tt14-2025-nhnn#^d2-19a]]. Vì vậy quyết định phân loại một vị thế vào sổ nào làm đổi cả khung đo (ΔEVE, ΔNII hay vốn yêu cầu thị trường) và vốn tính vào mẫu số CAR.

*Diễn giải:* khi trạng thái ngoại hối ròng (gồm vàng) hoặc giá trị quyền chọn vượt 2% vốn tự có, $K_{FXR}$ hoặc $K_{OPT}$ phát sinh [[src-tt14-2025-nhnn#^d74-4]] [[src-tt14-2025-nhnn#^d74-6]]. Treasury cần theo dõi hai tỷ lệ này so với vốn tự có. Hạn mức vị thế ngoại hối và vàng theo TT83/2025 xem [[market-risk-management]].

## Nhầm lẫn thường gặp
- $K_{MR}$ là vốn yêu cầu, chưa phải tài sản có rủi ro. Mẫu số nhân $K_{MR}$ với 12,5 [[src-tt14-2025-nhnn#^d5-1d]].
- Bốn cấu phần $K_{IRR}$, $K_{ER}$, $K_{FXR}$, $K_{CMR}$ không gồm giao dịch quyền chọn; quyền chọn nằm riêng ở $K_{OPT}$ [[src-tt14-2025-nhnn#^d74-1]].
