---
title: "Credit Risk Weight"
aliases: [Credit Risk Weight, CRW, Hệ số rủi ro tín dụng]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[customer-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^d8-2-vars]]"}
tags: [capital, credit-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Hệ số rủi ro tín dụng (Credit Risk Weight, CRW) là hệ số nhân với giá trị tài sản hoặc khoản phải đòi để ra đóng góp vào $RWA_{CR}$ [[src-tt14-2025-nhnn#^d8-2]]. CRW là tham số do cơ quan quản lý ấn định, nên không phải metric. Xem [[customer-credit-risk-rwa]].

TT14/2025 gán CRW từ 0% đến 200% tuỳ nhóm tài sản (Đ12–Đ23). Ngân hàng phân loại tài sản rồi xác định CRW theo loại tài sản [[src-tt14-2025-nhnn#^d9-1]].

## Cơ chế & drivers
**Quy trình hai bước** [[src-tt14-2025-nhnn#^d9-1]]:
1. ngân hàng phân loại tài sản theo Đ11 và hướng dẫn tại Phụ lục VI; thứ tự phân loại nằm ở [[credit-risk-asset-classes]] [[src-tt14-2025-nhnn#^pl6-1]];
2. ngân hàng xác định CRW tương ứng với loại tài sản theo Mục 2 Chương II.

**Bảng CRW tóm tắt theo nhóm tài sản**

| Nhóm | CRW | Chi tiết | Nguồn |
|---|---|---|---|
| Tiền mặt, vàng, tương đương tiền mặt | 0% | [[credit-risk-asset-classes]] | [[src-tt14-2025-nhnn#^d23-1]] |
| Chính phủ Việt Nam, NHNN, Kho bạc Nhà nước, UBND tỉnh/thành phố, ngân hàng chính sách, tổ chức tài chính quốc tế | 0% | [[sovereign-and-bank-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d13-1]] |
| Công ty quản lý tài sản, Công ty mua bán nợ | 20% | [[sovereign-and-bank-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d13-3]] |
| Chính phủ, ngân hàng trung ương nước ngoài | 0% đến 150% theo thứ hạng | [[sovereign-and-bank-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d13-5]] |
| Tổ chức tín dụng trong nước | 10% đến 150% theo thứ hạng và kỳ hạn | [[sovereign-and-bank-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d14-3]] |
| Tổ chức tín dụng nước ngoài | 20% đến 150% theo thứ hạng | [[sovereign-and-bank-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d14-1]] |
| Cho vay kinh doanh chứng khoán | 150% | [[credit-risk-asset-classes]] | [[src-tt14-2025-nhnn#^d15-1]] |
| Bất động sản thế chấp bằng nhà ở xã hội | 20% đến 50% theo LTV | [[real-estate-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d17-1a]] [[src-tt14-2025-nhnn#^d17-1b]] |
| Bất động sản thế chấp bằng nhà ở đủ tiêu chuẩn | 25% đến 100% theo LTV | [[real-estate-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d17-2a]] [[src-tt14-2025-nhnn#^d17-2b]] |
| Bất động sản thương mại đủ tiêu chuẩn | 60% đến 120% hoặc theo CRW doanh nghiệp | [[real-estate-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d17-3a]] [[src-tt14-2025-nhnn#^d17-3b]] |
| Bất động sản không đủ tiêu chuẩn | 75% đến 150% hoặc theo CRW doanh nghiệp | [[real-estate-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d17-4a]] [[src-tt14-2025-nhnn#^d17-4b]] [[src-tt14-2025-nhnn#^d17-5]] |
| Cấp tín dụng chuyên biệt | 100% đến 200% | [[specialised-lending-risk-weighting]] | [[src-tt14-2025-nhnn#^d18-5]] |
| Doanh nghiệp nhỏ và vừa | 85% | [[corporate-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d19-1]] |
| Doanh nghiệp khác | 50% đến 160%; 150% hoặc 200% ngoại lệ | [[corporate-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d19-2a]] [[src-tt14-2025-nhnn#^d19-2b]] [[src-tt14-2025-nhnn#^d19-2c]] |
| Cho vay cá nhân nông nghiệp, nông thôn | 50% | [[retail-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d20-1]] |
| Khoản phải đòi bán lẻ | 75% | [[retail-exposure-risk-weighting]] | [[src-tt14-2025-nhnn#^d21-2]] |
| Khoản phải đòi khác | 100% | [[credit-risk-asset-classes]] | [[src-tt14-2025-nhnn#^d22-1]] |
| Công cụ vốn chủ sở hữu của doanh nghiệp, cho vay giao dịch ký quỹ của công ty chứng khoán | 150% | [[credit-risk-asset-classes]] | [[src-tt14-2025-nhnn#^d23-1]] |
| Cho thuê tài chính | Cao hơn giữa CRW doanh nghiệp và 160% | [[credit-risk-asset-classes]] | [[src-tt14-2025-nhnn#^d23-3]] |
| Khoản phải thu từ bán nợ xấu | 200% | [[credit-risk-asset-classes]] | [[src-tt14-2025-nhnn#^d23-5]] |
| Tài sản còn lại | 100% | [[credit-risk-asset-classes]] | [[src-tt14-2025-nhnn#^d23-5]] |
| Nợ xấu | 100% hoặc 150% theo dự phòng cụ thể | [[credit-risk-asset-classes]] | [[src-tt14-2025-nhnn#^d12-1]] [[src-tt14-2025-nhnn#^d12-2]] |

**Hợp nhất.** Khi tính tỷ lệ hợp nhất, ngân hàng thương mại áp dụng CRW của Mục 2 cho khoản phải đòi của công ty con và chi nhánh ở nước ngoài [[src-tt14-2025-nhnn#^d9-4]].

**Khoản phải đòi bất động sản có nhiều tài sản bảo đảm.** Nguyên tắc chọn CRW nằm ở [[real-estate-exposure-risk-weighting]].

## Phụ thuộc regime
CRW áp dụng cho phương pháp tiêu chuẩn. Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]]. IRB (Chương III) chưa ingest [cần nguồn]. Cách dùng thứ hạng tín nhiệm độc lập nằm ở [[external-credit-rating-use]] và [[credit-rating-scale-mapping]].

## Góc nhìn theo domain
**VN Regulator.** Bảng CRW trải từ 0% (tiền mặt, Chính phủ Việt Nam, NHNN) đến 200% (khoản phải thu từ bán nợ xấu, tín dụng chuyên biệt thiếu kiểm soát, doanh nghiệp không có báo cáo tài chính hoặc vốn chủ sở hữu âm) [[src-tt14-2025-nhnn#^d23-1]] [[src-tt14-2025-nhnn#^d23-5]] [[src-tt14-2025-nhnn#^d18-5]] [[src-tt14-2025-nhnn#^d19-2b]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* CRW cùng [[credit-conversion-factor]] quyết định vốn tiêu hao của từng tài sản. Trái phiếu Chính phủ Việt Nam và tiền gửi tại NHNN có CRW 0% theo Đ13.1; cho vay doanh nghiệp lớn có CRW từ 50% đến 160% tuỳ doanh thu và đòn bẩy. Chênh lệch này là đầu vào để so sánh lợi suất điều chỉnh theo vốn (ví dụ [[raroc]]) giữa các tài sản. Phép so sánh bằng số cần dữ liệu danh mục thực tế.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Quy định phân loại nợ của NHNN (nhóm 3, 4, 5) chưa ingest.
