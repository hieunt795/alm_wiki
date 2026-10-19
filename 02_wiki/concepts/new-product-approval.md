---
title: "New Product Approval"
aliases: [New Product Approval, Phê duyệt sản phẩm mới, Quản lý rủi ro sản phẩm mới, NPA]
type: concept
domains: [vn-reg, alm, product]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]"]
relations: []
tags: [governance, new-product, risk-management]
updated: 2026-10-19
reviewed:
---

## Ý chính
Theo [[tt83-2025]], quản lý rủi ro đối với sản phẩm mới hoặc hoạt động trong thị trường mới là quy trình phê duyệt, thẩm định rủi ro và thử nghiệm trước khi ngân hàng chính thức cung cấp. Ngân hàng phải có quy định nội bộ về tiêu chí xác định sản phẩm mới, hoạt động trong thị trường mới [[src-tt83-2025-nhnn#^d21-1]].

## Cơ chế & drivers
**Phân vai phê duyệt** [[src-tt83-2025-nhnn#^d21-1]]:

| Bước | Ngân hàng thương mại | Chi nhánh ngân hàng nước ngoài | Nguồn |
|---|---|---|---|
| Chủ trương | HĐQT/HĐTV phê duyệt, trên cơ sở đề xuất của Tổng giám đốc | Theo quy định ngân hàng mẹ | [[src-tt83-2025-nhnn#^d21-1]] |
| Kế hoạch | Tổng giám đốc phê duyệt | Theo quy định ngân hàng mẹ | [[src-tt83-2025-nhnn#^d21-1]] |

**Thẩm định của bộ phận quản lý rủi ro.** Kế hoạch cung cấp sản phẩm mới phải được bộ phận quản lý rủi ro thẩm định về rủi ro và biện pháp quản lý rủi ro. Kế hoạch xác định tối thiểu [[src-tt83-2025-nhnn#^d21-2]]:
- quy mô và thời gian thử nghiệm, trên cơ sở đánh giá rủi ro và tác động đối với vốn tự có, thu nhập, để phù hợp khả năng kiểm soát rủi ro;
- thời gian chính thức cung cấp, trên cơ sở so kết quả thử nghiệm với các chỉ tiêu quản lý rủi ro.

**Khi chính thức cung cấp**, ngân hàng ban hành quy định, quy trình và quản lý các rủi ro trọng yếu của sản phẩm [[src-tt83-2025-nhnn#^d21-2]]. Danh sách rủi ro trọng yếu theo Đ3.13 [[src-tt83-2025-nhnn#^d3-13]].

## Phụ thuộc regime
Không ghi nhận trong nguồn đã ingest.

## Góc nhìn theo domain
- **VN**: TT83/2025 Đ21, hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]].
- **Basel**: wiki chưa có nguồn Basel về phê duyệt sản phẩm mới [cần nguồn].
- **ALM**: *Diễn giải:*
  - Tác động "đối với vốn tự có và thu nhập" [[src-tt83-2025-nhnn#^d21-2]] là đúng hai góc đo của IRRBB: [[economic-value-of-equity]] và [[net-interest-income-sensitivity]]. Sản phẩm tiền gửi hay cho vay mới có quyền chọn hành vi (rút trước hạn, trả trước, lãi suất thả nổi có sàn) nên được ALM ước tính ΔEVE, ΔNII và cách đưa vào [[funds-transfer-pricing]] trước khi thử nghiệm.
  - Sản phẩm chưa có lịch sử hành vi thì chưa có dữ liệu để hiệu chỉnh mô hình NMD, CPR, TDRR. Giai đoạn thử nghiệm theo Đ21.2.a là lúc thu dữ liệu đó. Xem [[behavioural-options]], [[model-validation]].

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- TT83 không nêu tiêu chí xác định "sản phẩm mới"; để quy định nội bộ [[src-tt83-2025-nhnn#^d21-1]].
