---
title: "IRB Model Validation"
aliases: [IRB Model Validation, Kiểm định ước tính nội bộ IRB, Backtesting PD LGD EAD]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[internal-ratings-based-approach]]", cite: "[[src-tt14-2025-nhnn#^d69-1]]"}
tags: [capital, credit-risk, irb, validation, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ69 TT14/2025 yêu cầu ngân hàng kiểm định tính chính xác và nhất quán của hệ thống xếp hạng và ước tính mọi tham số rủi ro: so tỷ lệ vỡ nợ thực tế với [[probability-of-default]] ước tính theo từng hạng, thêm [[loss-given-default]] và [[exposure-at-default]] với IRB nâng cao, cập nhật tối thiểu hằng năm [[src-tt14-2025-nhnn#^d69-1]].

## Cơ chế & drivers
- Tỷ lệ vỡ nợ thực tế phải nằm trong khoảng giá trị kỳ vọng của mỗi hạng. Phải có tài liệu về phương pháp và dữ liệu so sánh; phân tích và tài liệu cập nhật tối thiểu hằng năm [[src-tt14-2025-nhnn#^d69-1]].
- So sánh với nguồn dữ liệu bên ngoài (nếu có), trên dữ liệu phù hợp danh mục; đánh giá hiệu quả nội bộ dựa trên dữ liệu lịch sử dài hạn [[src-tt14-2025-nhnn#^d69-1]].
- Phương pháp kiểm định không thay đổi có hệ thống theo chu kỳ kinh tế; thay đổi phương pháp và dữ liệu phải được ghi lại đầy đủ [[src-tt14-2025-nhnn#^d69-1]].
- Có tiêu chuẩn nội bộ cụ thể về sai lệch đáng kể giữa giá trị thực tế và ước tính dẫn tới xem xét lại, có xét chu kỳ kinh doanh. Khi giá trị thực tế liên tục cao hơn ước tính, phải điều chỉnh lại ước tính theo dữ liệu vỡ nợ và tổn thất lịch sử [[src-tt14-2025-nhnn#^d69-1]].
- Quy trình kiểm định mô hình ở Đ64.8e (hiệu năng, ổn định, khả năng phân biệt, thứ tự xếp hạng) xem [[irb-model-governance]] [[src-tt14-2025-nhnn#^d64-8]].

## Phụ thuộc regime
Kiểm định mô hình nói chung xem [[model-validation]] (TT83/2025). Quan hệ với Đ69 chưa được nguồn nói rõ [cần nguồn].

Kết quả kiểm định là một nội dung của báo cáo hằng năm lên Hội đồng quản trị ([[irb-rating-operation-and-governance]]) và của hồ sơ chấp thuận ([[irb-approval-process]]).

## Góc nhìn theo domain
**VN Regulator.** Bốn việc lặp hằng năm: tự đánh giá tuân thủ (Đ63.1), rà soát ước tính (Đ68.1), kiểm định (Đ69.2), kiểm toán rà soát hệ thống (Đ66.5) [[src-tt14-2025-nhnn#^d63-1]] [[src-tt14-2025-nhnn#^d68-1]] [[src-tt14-2025-nhnn#^d69-1]] [[src-tt14-2025-nhnn#^d66-5]].

**Basel.** [cần nguồn] (CRE36 chưa ingest).

**ALM.** *Diễn giải:* kiểm định yêu cầu giữ dữ liệu chuyển hạng và vỡ nợ theo hạng dài hạn, nên cần kho dữ liệu lịch sử riêng cho IRB ([[irb-rating-operation-and-governance]]).

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Ngưỡng "sai lệch đáng kể" và "liên tục cao hơn" do ngân hàng tự đặt, nguồn không nêu số.
