---
title: "Sovereign and Bank Exposure Risk Weighting"
aliases: [Sovereign and Bank Exposure Risk Weighting, Hệ số rủi ro tín dụng khoản phải đòi Chính phủ và tổ chức tín dụng, Hệ số rủi ro tín dụng khoản phải đòi tổ chức tín dụng]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[credit-risk-weight]]", cite: "[[src-tt14-2025-nhnn#^d13-1]]"}
tags: [capital, credit-risk, interbank, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ13 đặt hệ số rủi ro tín dụng (CRW) cho khoản phải đòi nhà nước và tổ chức tài chính quốc tế. Đ14 đặt CRW cho khoản phải đòi tổ chức tín dụng và chi nhánh ngân hàng nước ngoài. Hai điều này quyết định CRW của trái phiếu Chính phủ, tiền gửi tại NHNN và tiền gửi liên ngân hàng trong [[customer-credit-risk-rwa]]. Xem [[credit-risk-weight]].

## Cơ chế & drivers
**Nhà nước và tổ chức tài chính quốc tế (Đ13)**

| Đối tượng | CRW | Nguồn |
|---|---|---|
| Chính phủ Việt Nam, NHNN, Kho bạc Nhà nước, UBND tỉnh/thành phố, ngân hàng chính sách | 0% | [[src-tt14-2025-nhnn#^d13-1]] |
| Tổ chức tài chính quốc tế | 0% | [[src-tt14-2025-nhnn#^d13-1]] |
| Công ty quản lý tài sản | 20%, trừ khi pháp luật áp dụng hệ số khác | [[src-tt14-2025-nhnn#^d13-3]] |
| Công ty mua bán nợ | 20% | [[src-tt14-2025-nhnn#^d13-3]] |
| PSEs, chính quyền địa phương các nước khác | Theo CRW của khoản phải đòi Chính phủ đó (bảng dưới) | [[src-tt14-2025-nhnn#^d13-6]] |

Chính phủ và ngân hàng trung ương các nước khác, theo thứ hạng tín nhiệm [[src-tt14-2025-nhnn#^d13-5]]:

| Thứ hạng | AAA đến AA- | A+ đến A- | BBB+ đến BBB- | BB+ đến B- | Dưới B- hoặc không có xếp hạng |
|---|---|---|---|---|---|
| CRW | 0% | 20% | 50% | 100% | 150% |

**Tổ chức tín dụng nước ngoài (Đ14.1)**, theo thứ hạng tín nhiệm [[src-tt14-2025-nhnn#^d14-1]]:

| Thứ hạng | AAA đến AA- | A+ đến BBB- | BB+ đến B- | Dưới B- hoặc không có xếp hạng |
|---|---|---|---|---|
| CRW | 20% | 50% | 100% | 150% |

**Chi nhánh (Đ14.2).** Chi nhánh ngân hàng nước ngoài tại Việt Nam, tại quốc gia khác và chi nhánh ngân hàng Việt Nam ở nước ngoài dùng thứ hạng tín nhiệm của ngân hàng mẹ [[src-tt14-2025-nhnn#^d14-2]].

**Tổ chức tín dụng trong nước (Đ14.3)**, trừ Đ14.4 và 14.5, theo thứ hạng tín nhiệm và thời hạn ban đầu [[src-tt14-2025-nhnn#^d14-3]]:

| Thời hạn ban đầu | AAA đến AA- | A+ đến BBB- | BB+ đến BB- | B+ đến B- | Dưới B- hoặc không có xếp hạng |
|---|---|---|---|---|---|
| Từ 03 tháng trở lên | 20% | 50% | 80% | 100% | 150% |
| Dưới 03 tháng | 10% | 20% | 40% | 50% | 70% |

**Ngoại lệ 0%** [[src-tt14-2025-nhnn#^d14-4]] [[src-tt14-2025-nhnn#^d14-5]]:
- khoản cho vay, bảo lãnh, tiền gửi của bên nhận chuyển giao bắt buộc và các tổ chức tín dụng khác đối với ngân hàng thương mại được chuyển giao bắt buộc;
- khoản cho vay, tiền gửi của tổ chức tín dụng hỗ trợ tại tổ chức tín dụng đang được kiểm soát đặc biệt.

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]]. Điều kiện với doanh nghiệp xếp hạng và nguyên tắc dùng thứ hạng nằm ở [[external-credit-rating-use]]; bảng quy đổi thang ở [[credit-rating-scale-mapping]].

## Góc nhìn theo domain
**VN Regulator.** Đ14.3 phân biệt kỳ hạn ban đầu dưới 03 tháng với từ 03 tháng trở lên [[src-tt14-2025-nhnn#^d14-3]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* với tổ chức tín dụng trong nước xếp hạng AAA đến AA-, tiền gửi liên ngân hàng dưới 03 tháng có CRW 10%, còn từ 03 tháng trở lên là 20%. Hệ số kỳ hạn này làm kỳ hạn cho vay liên ngân hàng ảnh hưởng RWA. Hệ số 0% của khoản phải đòi Chính phủ Việt Nam và NHNN áp dụng cho [[government-bond-holdings]] nếu thuộc đối tượng của Đ13.1; việc gán từng loại giấy tờ có giá cần đối chiếu Phụ lục VI [cần nguồn].

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Thứ hạng của tổ chức tín dụng trong nước do doanh nghiệp xếp hạng nào cung cấp: nguồn chỉ nêu tiêu chí ([[external-credit-rating-use]]) [cần nguồn].
