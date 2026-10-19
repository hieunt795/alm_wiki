---
title: "Model Validation"
aliases: [Model Validation, Kiểm định mô hình, Independent validation]
type: concept
domains: [alm, vn-reg, basel]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-bcbs-irrbb-2016]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: part-of, to: "[[model-risk-management]]", cite: "[[src-tt83-2025-nhnn#^d56-4d]]"}
tags: [model-risk, validation, governance]
updated: 2026-10-19
reviewed:
---

## Ý chính
Kiểm định mô hình là giai đoạn cuối trong vòng đời mô hình, sau xây dựng, triển khai, sử dụng và theo dõi [[src-tt83-2025-nhnn#^d3-24]]. Nó đánh giá mô hình có đáp ứng mục tiêu ban đầu và hiệu quả khi sử dụng thực tế hay không [[src-tt83-2025-nhnn#^d56-4d]].

Trong quản lý rủi ro mô hình, kiểm định thuộc tuyến bảo vệ thứ hai, tách khỏi tuyến 1 là bên xây dựng, triển khai và sử dụng mô hình [[src-tt83-2025-nhnn#^d56-7]]. Xem [[model-risk-management]], [[three-lines-of-defence]].

## Cơ chế & drivers
**Khi nào phải kiểm định (TT83/2025)** [[src-tt83-2025-nhnn#^d56-4d]]:

| Thời điểm | Yêu cầu | Nguồn |
|---|---|---|
| Trước khi sử dụng | Bắt buộc | [[src-tt83-2025-nhnn#^d56-4d]] |
| Khi có thay đổi trọng yếu | Mức "trọng yếu" theo quy định nội bộ | [[src-tt83-2025-nhnn#^d56-4d]] |
| Định kỳ | Tối thiểu hằng năm | [[src-tt83-2025-nhnn#^d56-4d]] |

Kết quả kiểm định phải gồm báo cáo đánh giá khả năng đáp ứng mục tiêu ban đầu và hiệu quả sử dụng thực tế [[src-tt83-2025-nhnn#^d56-4d]]. Báo cáo nội bộ về rủi ro mô hình (tối thiểu hằng năm) phải nêu kết quả kiểm định định kỳ hoặc đột xuất [[src-tt83-2025-nhnn#^d58-1]].

**Phạm vi.**
- Mục 8 áp dụng tối thiểu cho mô hình rủi ro cao; mô hình rủi ro trung bình và thấp quản lý theo quy định nội bộ [[src-tt83-2025-nhnn#^d56-2]].
- Với mô hình mua ngoài, ngân hàng yêu cầu bên bán cung cấp thông tin để đánh giá, và tự đánh giá hiệu quả sử dụng [[src-tt83-2025-nhnn#^d56-5]].

**Cấu phần kiểm định (Basel IRRBB).**
- d368 Nguyên tắc 6 yêu cầu mô hình đo IRRBB có chức năng kiểm định độc lập với quá trình phát triển mô hình [[src-bcbs-irrbb-2016#^irrbb-p06-1]].
- Khung kiểm định hiệu quả gồm 3 cấu phần [[src-bcbs-irrbb-2016#^irrbb-p06-2]]:
  - đánh giá tính vững chắc về khái niệm và phương pháp luận;
  - giám sát mô hình liên tục, gồm kiểm tra quy trình và benchmarking;
  - phân tích kết quả, gồm backtesting các tham số nội bộ chính như độ ổn định tiền gửi, trả trước hạn, rút trước hạn.

**Tài liệu phương pháp (Lubinska).** Kiểm định dựa trên "phản biện hiệu quả" (effective challenge) bởi nhân sự độc lập, có năng lực, có thẩm quyền [[src-lubinska-alm-optimisation#^lubinska-u05-15]].

## Phụ thuộc regime
*Diễn giải:* tham số hành vi ước lượng trong giai đoạn lãi suất ổn định (độ ổn định tiền gửi, CPR) có thể sai lệch khi lãi suất biến động mạnh. Vì vậy kiểm định "khi có thay đổi trọng yếu" cần gắn với các biến cố thị trường, không chỉ gắn với thay đổi mô hình (ngoài wiki, chưa có nguồn).

## Góc nhìn theo domain
- **VN**: TT83/2025 Đ56.4.đ, hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]]. TT83 ấn định tần suất (tối thiểu hằng năm), nhưng không nêu nội dung kỹ thuật của kiểm định.
- **Basel**: d368 nêu cấu phần kỹ thuật (phương pháp luận, giám sát liên tục, backtesting) [[src-bcbs-irrbb-2016#^irrbb-p06-2]], nhưng phần đã ingest không có tần suất. Kiểm toán nội bộ rà soát quy trình quản trị rủi ro mô hình theo kế hoạch hằng năm [[src-bcbs-irrbb-2016#^irrbb-p06-3]].
- **ALM**: các mô hình dùng cho ΔEVE theo Phụ lục V là đối tượng kiểm định:
  - NMD lõi và kỳ hạn trung bình NMD lõi [[src-tt83-2025-nhnn#^pl5-a2-3a]];
  - $CPR_0$, $TDRR_0$ theo danh mục [[src-tt83-2025-nhnn#^pl5-a2-3b2]] [[src-tt83-2025-nhnn#^pl5-a2-3c2]].
  - *Diễn giải:* TT83 không xếp sẵn các mô hình này vào mức rủi ro nào. Nếu ngân hàng xếp chúng là rủi ro cao [[src-tt83-2025-nhnn#^d56-1]], chúng phải được kiểm định tối thiểu hằng năm.

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Tiêu chí "thay đổi trọng yếu" để kích hoạt kiểm định đột xuất: TT83 để quy định nội bộ [cần nguồn].
