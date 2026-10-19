---
title: "Liquidity Stress Testing"
aliases: [Liquidity Stress Testing, Kiểm tra sức chịu đựng về thanh khoản, Stress test thanh khoản]
type: concept
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[liquidity-risk-management]]", cite: "[[src-tt83-2025-nhnn#^d45-2]]"}
  - {type: input-to, to: "[[contingency-funding-plan]]", cite: "[[src-tt83-2025-nhnn#^d48-4]]"}
  - {type: part-of, to: "[[stress-testing]]", cite: "[[src-tt83-2025-nhnn#^d23-1]]"}
tags: [liquidity, stress-test, internal-control]
updated: 2026-10-19
reviewed:
---

## Ý chính
Kiểm tra sức chịu đựng về thanh khoản đánh giá khả năng ngân hàng thực hiện nghĩa vụ, cam kết và tuân thủ hạn mức rủi ro thanh khoản khi các giả định bất lợi xảy ra. Theo [[tt83-2025]], ngân hàng phải có phương pháp tính tác động của các giả định; giả định và phương pháp phải được rà soát, tự đánh giá [[src-tt83-2025-nhnn#^d48-1]]. Nguyên tắc kiểm tra sức chịu đựng là một nội dung bắt buộc của chiến lược quản lý rủi ro thanh khoản [[src-tt83-2025-nhnn#^d45-2]].

## Cơ chế & drivers
**Kịch bản tối thiểu** [[src-tt83-2025-nhnn#^d48-2]]:

| Kịch bản | Giả định | Nguồn |
|---|---|---|
| Đặc thù ngân hàng | Khủng hoảng thanh khoản ở ngân hàng trong khi thanh khoản toàn hệ thống vẫn ổn định; ví dụ: chất lượng tài sản xấu đi, HQLA sụt giảm nghiêm trọng, xếp hạng tín nhiệm giảm, bị tấn công thông tin | [[src-tt83-2025-nhnn#^d48-2]] [[src-tt83-2025-nhnn#^d48-2b]] |
| Toàn hệ thống | Khủng hoảng tài chính quy mô rộng, ảnh hưởng nhiều ngân hàng hoặc toàn hệ thống | [[src-tt83-2025-nhnn#^d48-2]] |
| Hỗn hợp | Khủng hoảng đặc thù của một ngân hàng lây lan ra toàn hệ thống | [[src-tt83-2025-nhnn#^d48-2]] |

**Yếu tố rủi ro phải xét tối thiểu.** Kịch bản là tập hợp yếu tố rủi ro của tài sản có, nợ phải trả và cam kết ngoại bảng [[src-tt83-2025-nhnn#^d48-3]]:
- loại tiền tệ (VND, USD gồm ngoại tệ quy đổi, ngoại tệ khác), để phản ánh khả năng chuyển đổi tiền tệ [[src-tt83-2025-nhnn#^d48-3b]];
- việc phải mua lại nợ hoặc thực hiện nghĩa vụ khác để giảm rủi ro danh tiếng;
- tỷ lệ rút trước hạn ([[run-off-rate]]) thực tế của nợ phải trả trong thời kỳ căng thẳng gia tăng;
- mức độ tập trung huy động vốn ([[funding-concentration-risk]]);
- mất hoặc giảm đáng kể khả năng thu hút vốn từ khách gửi tiền quan trọng, chủ nợ khác, kể cả liên ngân hàng.

**Tần suất.** Tối thiểu hằng quý, và bất cứ khi nào có sự kiện có thể tác động nghiêm trọng tới thanh khoản [[src-tt83-2025-nhnn#^d23-5]]. Khung chung về kiểm tra sức chịu đựng: [[stress-testing]].

**Đầu ra.** Căn cứ kết quả kiểm tra, ngân hàng phải lập kế hoạch dự phòng cho trường hợp không đáp ứng được yêu cầu thanh khoản [[src-tt83-2025-nhnn#^d48-4]]. Xem [[contingency-funding-plan]].

**Báo cáo.**
- Báo cáo nội bộ hằng quý gồm kết quả kiểm tra sức chịu đựng trong kỳ, nếu có [[src-tt83-2025-nhnn#^d49-1]].
- Báo cáo hằng năm gửi NHNN nêu giả định, phương pháp kèm điểm mạnh và hạn chế, và kết quả [[src-tt83-2025-nhnn#^pl2-ii4]].

## Phụ thuộc regime
*Diễn giải:* ba kịch bản tách nguồn căng thẳng theo phạm vi (riêng ngân hàng, toàn hệ thống, lây lan). Như vậy cùng một bảng cân đối có thể đạt ở kịch bản này và thiếu hụt ở kịch bản khác, tuỳ nguồn vốn phụ thuộc vào thị trường liên ngân hàng hay vào khách gửi lẻ.

## Góc nhìn theo domain
- **VN**: giả định và phương pháp tính tác động phải được rà soát, tự đánh giá [[src-tt83-2025-nhnn#^d48-1]]. *Diễn giải:* Đ48 không ấn định tham số số (run-off rate, haircut, horizon), nên ngân hàng tự đặt các giả định này.
- **Basel**: LCR là một kịch bản căng thẳng 30 ngày có tham số chuẩn hoá. Xem [[lcr]], [[run-off-rate]]. *Diễn giải:* kịch bản LCR gộp yếu tố đặc thù và toàn hệ thống, gần với kịch bản hỗn hợp của Đ48.2.c; chưa có nguồn đối chiếu trực tiếp.
- **ALM**: *Diễn giải:* kết quả stress test là đầu vào để đặt quy mô đệm thanh khoản và chi phí đệm trong [[liquidity-transfer-pricing]].

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Horizon kịch bản (30 ngày, 90 ngày, 1 năm) chưa có nguồn VN [cần nguồn].
