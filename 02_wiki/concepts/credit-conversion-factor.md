---
title: "Credit Conversion Factor"
aliases: [Credit Conversion Factor, CCF, Hệ số chuyển đổi]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[exposure-value]]", cite: "[[src-tt14-2025-nhnn#^d8-3-vars]]"}
tags: [capital, credit-risk, off-balance-sheet, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Hệ số chuyển đổi (CCF) quy phần cam kết ngoại bảng của khoản phải đòi thành giá trị tính rủi ro tín dụng: $E_i = Eon_i + Eoff_i \times CCF_i$ [[src-tt14-2025-nhnn#^d8-3]]. Đ10 TT14/2025 đặt bốn mức CCF: 10%, 20%, 50%, 100% [[src-tt14-2025-nhnn#^d10-1]] [[src-tt14-2025-nhnn#^d10-2]] [[src-tt14-2025-nhnn#^d10-3]] [[src-tt14-2025-nhnn#^d10-4]]. Xem [[exposure-value]].

## Cơ chế & drivers
CCF là tham số do cơ quan quản lý ấn định, nên không phải metric.

| CCF | Khoản mục | Nguồn |
|---|---|---|
| 10% | Cam kết ngoại bảng (kể cả hạn mức chưa sử dụng) mà ngân hàng có quyền hủy ngang hoặc tự động hủy ngang khi khách hàng vi phạm điều kiện hoặc suy giảm khả năng thực hiện nghĩa vụ | [[src-tt14-2025-nhnn#^d10-1]] |
| 10% | Hạn mức tín dụng chưa sử dụng của thẻ tín dụng | [[src-tt14-2025-nhnn#^d10-1]] |
| 20% | Thư tín dụng do ngân hàng phát hành hoặc xác nhận, có chứng từ vận tải, đảm bảo bằng hàng hóa, thời hạn cấp tín dụng gốc từ 01 năm trở xuống | [[src-tt14-2025-nhnn#^d10-2]] |
| 50% | Thư tín dụng như trên nhưng thời hạn cấp tín dụng gốc trên 01 năm | [[src-tt14-2025-nhnn#^d10-3]] |
| 50% | Nợ tiềm tàng dựa trên hoạt động cụ thể (bảo lãnh thực hiện hợp đồng, bảo lãnh dự thầu, thư tín dụng dự phòng cho hoạt động cụ thể) | [[src-tt14-2025-nhnn#^d10-3]] |
| 50% | Bảo lãnh phát hành chứng khoán, giấy tờ có giá | [[src-tt14-2025-nhnn#^d10-3]] |
| 100% | Cam kết ngoại bảng tương đương khoản cho vay (cam kết cho vay không hủy ngang; bảo lãnh và thư tín dụng dự phòng bảo đảm nghĩa vụ tài chính cho khoản nợ hoặc trái phiếu; hạn mức chưa giải ngân không hủy ngang) | [[src-tt14-2025-nhnn#^d10-4]] |
| 100% | Các khoản chấp nhận thanh toán | [[src-tt14-2025-nhnn#^d10-4]] |
| 100% | Nghĩa vụ thanh toán của ngân hàng trong giao dịch bán giấy tờ có giá có bảo lưu quyền truy đòi khi bên phát hành không thực hiện cam kết | [[src-tt14-2025-nhnn#^d10-4]] |
| 100% | Hợp đồng kỳ hạn về tài sản, tiền gửi, chứng khoán trả trước một phần mà ngân hàng cam kết thực hiện | [[src-tt14-2025-nhnn#^d10-4]] |
| 100% | Cam kết ngoại bảng chưa nêu ở khoản 1, 2, 3 và các điểm a–d của khoản 4 | [[src-tt14-2025-nhnn#^d10-4]] |

**Cam kết cung cấp cam kết ngoại bảng** (cam kết cấp bảo lãnh, phát hành hoặc hoàn trả thư tín dụng): CCF là hệ số thấp hơn giữa CCF của cam kết cung cấp và CCF của cam kết ngoại bảng được cam kết cung cấp [[src-tt14-2025-nhnn#^d10-5]].

## Phụ thuộc regime
CCF áp dụng cho phương pháp tiêu chuẩn của Chương II. Phương pháp xếp hạng nội bộ (IRB, Chương III) chưa ingest [cần nguồn]. Hiệu lực: bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Đ10 gom thư tín dụng thành hai mức theo kỳ hạn gốc, tách cam kết hủy ngang (10%) khỏi không hủy ngang (100%) [[src-tt14-2025-nhnn#^d10-1]] [[src-tt14-2025-nhnn#^d10-4]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* hạn mức tín dụng chưa sử dụng được tính CCF cho RWA ở đây. Trong [[lcr]] và [[nsfr]], cam kết chưa sử dụng được xử lý theo hệ số riêng ([[committed-facilities]]). Hai bộ hệ số phục vụ hai mục đích khác nhau và không dùng thay nhau.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Hạn mức tín dụng chưa sử dụng không hủy ngang (CCF 100% theo Đ10.4a) và hạn mức hủy ngang (10% theo Đ10.1a) khác nhau ở điều kiện hủy ngang nào trong hợp đồng thực tế của ngân hàng? Nguồn nêu điều kiện "quyền hủy ngang hoặc tự động hủy ngang khi khách hàng vi phạm điều kiện hủy ngang hoặc suy giảm khả năng thực hiện nghĩa vụ" [[src-tt14-2025-nhnn#^d10-1]].
