---
title: "IRB Rating System Design"
aliases: [IRB Rating System Design, Thiết kế hệ thống xếp hạng tín dụng nội bộ, Cơ cấu xếp hạng IRB, Internal Rating System]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[internal-ratings-based-approach]]", cite: "[[src-tt14-2025-nhnn#^d64-12]]"}
tags: [capital, credit-risk, irb, rating, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ64 TT14/2025 quy định thiết kế hệ thống xếp hạng tín dụng nội bộ: hệ thống gồm phương pháp, quy trình, kiểm soát, thu thập số liệu và công nghệ thông tin để đánh giá rủi ro, xếp hạng, lượng hóa PD và ước tính tổn thất [[src-tt14-2025-nhnn#^d64-12]]. Hệ thống phải đáp ứng yêu cầu tối thiểu với mọi loại, nhóm, tiểu nhóm tài sản dùng IRB và ngân hàng tự đánh giá tuân thủ hằng năm [[src-tt14-2025-nhnn#^d63-1]]. Quản trị mô hình xem [[irb-model-governance]]; vận hành xem [[irb-rating-operation-and-governance]].

## Cơ chế & drivers
**Nhiều hệ thống.** Mỗi loại tài sản được dùng nhiều hệ thống, theo ngành hoặc phân khúc thị trường. Phải ghi lý do dùng hệ thống cho từng khách hàng, và không được chuyển khách hàng sang hệ thống khác một cách không hợp lý làm giảm yêu cầu vốn [[src-tt14-2025-nhnn#^d64-12]].

**Doanh nghiệp.** Các khoản phải đòi của cùng khách hàng có chung một mức xếp hạng, trừ khác đồng tiền hoặc có bảo lãnh, phái sinh tín dụng. Chính sách mô tả rủi ro mỗi mức xếp hạng qua [[probability-of-default]] và tiêu chí phân loại [[src-tt14-2025-nhnn#^d64-3a]]. Cơ cấu tối thiểu 7 mức cho khách hàng không vỡ nợ và 1 mức cho khách hàng vỡ nợ ([[customer-default-definition]]); mức có "cộng" hoặc "trừ" chỉ là mức riêng khi đã mô tả đầy đủ tiêu chí và ước tính PD; danh mục tập trung ở một phân khúc phải có đủ mức xếp hạng, và nếu tập trung đáng kể ở vài mức thì cần bằng chứng khoa học, dữ liệu lịch sử rằng mọi khách hàng trong mức đó có cùng PD trong PD band [[src-tt14-2025-nhnn#^d64-4a]].

**Bán lẻ.** Hệ thống đánh giá cả đặc điểm khách hàng và khoản phải đòi rồi phân nhóm tương đồng. Yếu tố phân nhóm: đặc điểm khách hàng, đặc điểm khoản phải đòi (sản phẩm, tài sản bảo đảm gồm [[loan-to-value]] và seasoning effect, bảo lãnh, phái sinh tín dụng, mức ưu tiên), tình trạng quá hạn [[src-tt14-2025-nhnn#^d64-3b]]. PD, LGD, EAD ước tính theo nhóm, nhóm đủ lớn để ước tính và kiểm định, không tập trung quá mức [[src-tt14-2025-nhnn#^d64-4b]].

**Tiêu chí xếp hạng.** Đủ chi tiết để xếp nhất quán, bằng văn bản để bộ phận độc lập và cơ quan quản lý rà soát, thống nhất với quy định nội bộ về cấp tín dụng, cơ cấu lại, mua bán và xử lý nợ xấu. Dùng mọi thông tin sẵn có; thiếu thông tin thì thận trọng hơn; dựa chính vào xếp hạng của doanh nghiệp xếp hạng tín nhiệm độc lập thì phải xem xét thêm thông tin khác ([[external-credit-rating-use]]) [[src-tt14-2025-nhnn#^d64-5]].

**Phạm vi xếp hạng.** Dữ liệu tối thiểu 01 năm; xếp hạng phản ánh khả năng và thiện chí trả nợ trong điều kiện bất lợi, nhất quán với điều kiện trong một chu kỳ kinh doanh; PD của khách hàng đòn bẩy cao hoặc tài sản chủ yếu giao dịch trên sàn phải phản ánh biến động thời khủng hoảng; thận trọng khi thiếu thông tin [[src-tt14-2025-nhnn#^d64-6]].

## Phụ thuộc regime
Chỉ ngân hàng được chấp thuận IRB phải tuân thủ ([[irb-approval-process]]). Hệ thống phải được dùng đáp ứng yêu cầu ít nhất 02 năm liền kề trước khi nộp hồ sơ ([[irb-use-test]]).

## Góc nhìn theo domain
**VN Regulator.** Yêu cầu 7 mức không vỡ nợ cộng 1 mức vỡ nợ nằm ngay trong Thông tư, thay vì để ngân hàng tự đặt [[src-tt14-2025-nhnn#^d64-4a]].

**Basel.** [cần nguồn] (CRE36 chưa ingest).

**ALM.** *Diễn giải:* hệ thống xếp hạng phải đồng thời phục vụ phê duyệt tín dụng, quản lý rủi ro, phân bổ vốn nội bộ và báo cáo ([[irb-use-test]]), nên thang xếp hạng tối thiểu 8 mức là dữ liệu đầu vào chung cho các chức năng này.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Mức PD tối thiểu hoặc khoảng PD band của từng hạng: nguồn không nêu.
