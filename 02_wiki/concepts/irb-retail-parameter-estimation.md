---
title: "IRB Retail Parameter Estimation"
aliases: [IRB Retail Parameter Estimation, Ước tính tham số IRB bán lẻ, PD sàn, LGD sàn, EAD sàn, LGD suy thoái]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[internal-ratings-based-approach]]", cite: "[[src-tt14-2025-nhnn#^d49-1]]"}
tags: [capital, credit-risk, irb, retail, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Với khoản phải đòi bán lẻ (IRB nâng cao), ngân hàng tự tính PD, LGD và EAD, nhưng Thông tư đặt sàn cho cả ba tham số và yêu cầu tối thiểu khi ước tính [[src-tt14-2025-nhnn#^d49-1]]. Tham số dùng trong công thức là giá trị lớn hơn giữa ước tính của ngân hàng và sàn [[src-tt14-2025-nhnn#^d50-1]] [[src-tt14-2025-nhnn#^d51-1]] [[src-tt14-2025-nhnn#^d53-1]]. Công thức K xem [[irb-capital-requirement]]; phân loại bán lẻ xem [[irb-asset-classes]].

## Cơ chế & drivers
**Sàn tham số**

| Tham số | Sàn | Nguồn |
|---|---|---|
| [[probability-of-default]] | 0,1% với QRRE; 0,05% với bán lẻ còn lại | [[src-tt14-2025-nhnn#^d50-1]] |
| [[loss-given-default]] (bảo đảm toàn bộ) | 5% thế chấp nhà ở; bán lẻ khác 0% / 10% / 15% theo tài sản Đ44.1a / b / c | [[src-tt14-2025-nhnn#^d51-3a]] |
| LGD (không bảo đảm hoặc tài sản không đủ điều kiện) | 50% QRRE; 30% bán lẻ khác | [[src-tt14-2025-nhnn#^d51-3c]] |
| [[exposure-at-default]] | Nội bảng + 50% của số dư ngoại bảng × CCF tiêu chuẩn ([[credit-conversion-factor]]) | [[src-tt14-2025-nhnn#^d53-1]] |

Bảo đảm một phần thì LGD sàn là trung bình có trọng số theo giá trị của LGD sàn từng phần [[src-tt14-2025-nhnn#^d51-3b]].

**Yêu cầu tối thiểu khi ước tính LGD (Đ51.4)**
- Không thấp hơn LGD trung bình dài hạn có trọng số vỡ nợ, tính từ tổn thất kinh tế trung bình của mọi khoản vỡ nợ quan sát được theo nhóm hoặc tiểu nhóm [[src-tt14-2025-nhnn#^d51-4ab]].
- Tính LGD suy thoái khi tổn thất tín dụng cao hơn đáng kể do suy thoái kinh tế [[src-tt14-2025-nhnn#^d51-4ab]].
- Ước tính thận trọng hơn khi rủi ro khách hàng và rủi ro tài sản hoặc bên bảo đảm phụ thuộc đáng kể, hoặc lệch đồng tiền [[src-tt14-2025-nhnn#^d51-4ab]].
- Dựa cả dữ liệu thu hồi lịch sử, không chỉ giá trị thị trường tài sản bảo đảm; quan sát tối thiểu 05 năm liên tục [[src-tt14-2025-nhnn#^d51-4cd]].

**Yêu cầu tối thiểu khi ước tính EAD (Đ53.4)**
- Có quy trình ước tính EAD phần ngoại bảng; ước tính EAD trung bình dài hạn có trọng số vỡ nợ với biên độ thận trọng, lớn hơn nếu tần suất vỡ nợ tỷ lệ thuận với EAD [[src-tt14-2025-nhnn#^d53-4abc]].
- Ước tính EAD suy thoái và dùng nó khi thận trọng hơn [[src-tt14-2025-nhnn#^d53-4abc]].
- Soát xét tối thiểu hằng năm và đột xuất; có hệ thống theo dõi dư nợ và hạn mức cam kết theo khách hàng và mức xếp hạng; xem xét biện pháp ngăn giải ngân thêm khi khách hàng vi phạm cam kết [[src-tt14-2025-nhnn#^d53-4dde]].
- Dữ liệu theo phân khúc đồng nhất, tối thiểu gồm dư nợ gốc hoặc hạn mức, lãi và phí phải thu; quan sát tối thiểu 05 năm liên tục [[src-tt14-2025-nhnn#^d53-4ghi]].
- Với thẻ tín dụng và khoản không xác định được thời điểm giải ngân thêm, xét lịch sử và dự tính giải ngân trước khi vỡ nợ [[src-tt14-2025-nhnn#^d53-23]].

**Bảo lãnh và phái sinh tín dụng.** Xem [[irb-credit-risk-mitigation]] [[src-tt14-2025-nhnn#^d52-1]].

## Phụ thuộc regime
Yêu cầu tối thiểu với hệ thống xếp hạng và phê duyệt (Mục 8 Chương III) được nhắc ở Đ51.4c: xem [[irb-rating-system-design]], [[irb-rating-operation-and-governance]], [[irb-model-validation]].

## Góc nhìn theo domain
**VN Regulator.** Đ51.4d và Đ53.4i đặt khoảng quan sát 05 năm liên tục cho LGD và EAD bán lẻ. Với PD bán lẻ, khoảng quan sát cũng tối thiểu 05 năm liên tục ([[irb-parameter-estimation-requirements]]) [[src-tt14-2025-nhnn#^d68-3]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* ngân hàng cần dữ liệu vỡ nợ, thu hồi và giải ngân thêm theo phân khúc bán lẻ ít nhất 05 năm liên tục. Thẻ tín dụng và thấu chi (QRRE) có sàn LGD 50% khi không có tài sản bảo đảm, cao hơn 30% của bán lẻ khác.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
Chưa có.
