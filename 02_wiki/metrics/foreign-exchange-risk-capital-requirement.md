---
title: "Foreign Exchange Risk Capital Requirement"
aliases: [Foreign Exchange Risk Capital Requirement, K_FXR, KFXR, Vốn yêu cầu cho rủi ro ngoại hối]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[market-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d74-4]]"}
tags: [capital, market-risk, fx, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho rủi ro ngoại hối ($K_{FXR}$, gồm cả vàng) là cấu phần của $K_{MR}$ cho giao dịch không phải quyền chọn [[src-tt14-2025-nhnn#^d74-1]]. $K_{FXR}$ chỉ áp dụng khi tổng giá trị trạng thái ngoại hối ròng (gồm cả vàng) lớn hơn 2% vốn tự có ([[own-funds]]) [[src-tt14-2025-nhnn#^d74-4]]. Xem [[market-risk-capital-requirement]].

## Công thức
$$
K_{FXR} = \left( \max\left( \sum SP,\ \sum LP \right) + GoldP \right) \times 8\%
$$
[[src-tt14-2025-nhnn#^pl4-iv-1]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $\sum SP$ | Tổng các trạng thái âm của các ngoại tệ trong danh mục ngoại tệ | [[src-tt14-2025-nhnn#^pl4-iv-1]] |
| $\sum LP$ | Tổng trạng thái dương của các ngoại tệ trong danh mục ngoại tệ | [[src-tt14-2025-nhnn#^pl4-iv-1]] |
| $GoldP$ | Trạng thái vàng | [[src-tt14-2025-nhnn#^pl4-iv-1]] |
| $\max(\sum SP, \sum LP) + GoldP$ | Tổng giá trị trạng thái ngoại hối ròng, gồm cả vàng | [[src-tt14-2025-nhnn#^pl4-iv-1]] |

## Diễn giải
**Trạng thái ngoại tệ** được xác định cho từng ngoại tệ (gồm vàng tiêu chuẩn). Trạng thái nguyên tệ bằng tổng của [[src-tt14-2025-nhnn#^pl4-iv-2]]:
- trạng thái giao ngay: chênh lệch giữa tổng tài sản và tổng nợ phải trả (gồm lãi dự thu và chi phí trả lãi dự kiến) bằng một ngoại tệ;
- trạng thái kỳ hạn ròng: chênh lệch giữa các khoản nhận được và phải trả bằng một ngoại tệ trong giao dịch ngoại tệ kỳ hạn, gồm giao dịch tương lai và vốn trong giao dịch hoán đổi chưa tính vào trạng thái giao ngay;
- bảo lãnh hoặc nghĩa vụ tương tự không thể hủy ngang mà bên được bảo lãnh không có khả năng thực hiện nghĩa vụ;
- thu nhập, chi phí tương lai ròng chưa dự thu nhưng đã phòng ngừa rủi ro;
- lãi, lỗ bằng ngoại tệ từ hoạt động kinh doanh ở nước ngoài theo quy định hạch toán của nước sở tại.

Trạng thái ngoại tệ là trạng thái nguyên tệ (xác định theo pháp luật về trạng thái ngoại tệ của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài) quy đổi sang Việt Nam đồng theo tỷ giá quy đổi trạng thái [[src-tt14-2025-nhnn#^pl4-iv-2]].

Trạng thái ngoại hối và vàng phát sinh từ trạng thái hàng hóa tính vào mục này [[src-tt14-2025-nhnn#^pl4-iii-6]].

*Diễn giải:* ví dụ số do wiki dựng: ΣLP = 300 tỷ đồng, ΣSP = 220 tỷ đồng (giá trị tuyệt đối), GoldP = 30 tỷ đồng thì tổng trạng thái ròng = 300 + 30 = 330 tỷ đồng và $K_{FXR}$ = 330 × 8% = 26,4 tỷ đồng. Dấu của GoldP và cách cộng với max khi GoldP âm không được nguồn nêu rõ [cần nguồn].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Hệ số vốn | [cần nguồn] (MAR chưa ingest) | 8% [[src-tt14-2025-nhnn#^pl4-iv-1]] | PL4.B.IV.1 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Ngưỡng áp dụng | [cần nguồn] | Trạng thái ngoại hối ròng (gồm vàng) > 2% vốn tự có [[src-tt14-2025-nhnn#^d74-4]] | Đ74.4 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* ngưỡng 2% vốn tự có miễn $K_{FXR}$ khi trạng thái ngoại hối ròng nhỏ. Treasury giữ vị thế ngoại hối dưới 2% vốn tự có không phát sinh $K_{FXR}$; khi vượt, toàn bộ vị thế ròng (không chỉ phần vượt) tính 8% theo cách đọc của công thức. Nguồn không nêu rõ phần vượt hay toàn bộ [cần nguồn].

## Nhầm lẫn thường gặp
- Vàng nằm trong $K_{FXR}$, không nằm trong rủi ro hàng hóa [[src-tt14-2025-nhnn#^pl4-iii-12]].
- Quyền chọn ngoại hối tính ở [[options-risk-capital-requirement]], không ở $K_{FXR}$ [[src-tt14-2025-nhnn#^d74-1]].
