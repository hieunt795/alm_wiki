---
title: "Operational Loss Data"
aliases: [Operational Loss Data, Dữ liệu tổn thất hoạt động, Operational Loss Event, Sự kiện tổn thất hoạt động]
type: concept
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[loss-component]]", cite: "[[src-tt14-2025-nhnn#^d70-3c]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Dữ liệu tổn thất hoạt động là bộ dữ liệu sự kiện tổn thất làm đầu vào của [[loss-component]]. Dữ liệu phải đáp ứng Đ71 và Đ72 của TT14/2025 [[src-tt14-2025-nhnn#^d70-3c]]. Ngân hàng phải thu thập tất cả sự kiện có tổn thất hoạt động ròng từ 12 triệu đồng trở lên trong khung thời gian tính [[src-tt14-2025-nhnn#^d71-1]].

## Cơ chế & drivers
**Tổn thất ròng của một sự kiện** bằng tổng các giá trị tổn thất ghi nhận trừ các khoản thu hồi đã nhận (kể cả khoản bảo hiểm chi trả). Ngân hàng phải dùng giá trị theo ngày hạch toán [[src-tt14-2025-nhnn#^d71-2]].

**Tổng tổn thất hoạt động gồm bốn loại** [[src-tt14-2025-nhnn#^d71-3]]:
- chi phí ghi trực tiếp vào báo cáo kết quả hoạt động và giá trị ghi giảm (write-downs) của tài sản;
- chi phí hậu quả của sự kiện, gồm chi phí bên ngoài liên hệ trực tiếp (pháp lý, tư vấn) và chi phí sửa chữa, thay thế để khôi phục hiện trạng;
- tổn thất đang chờ xử lý, ghi vào tài khoản tạm thời và chưa phản ánh trong báo cáo kết quả hoạt động;
- tổn thất thời gian: sự kiện chưa ghi nhận kéo dài hơn 01 năm và làm phát sinh rủi ro pháp lý.

**Ba khoản loại trừ** [[src-tt14-2025-nhnn#^d71-4]]:
- chi phí hợp đồng bảo trì chung cho tài sản cố định hữu hình;
- chi phí tăng cường kinh doanh sau tổn thất (nâng cấp, cải tiến, sáng kiến, cải tiến đánh giá rủi ro);
- chi phí mua bảo hiểm rủi ro hoạt động.

**Quản trị dữ liệu (Đ72).**
- Quy định nội bộ về quy trình xác định, thu thập, xử lý thông tin tổn thất. Kiểm toán nội bộ rà soát quy trình trước khi dữ liệu dùng tính vốn. Kiểm toán nội bộ hoặc kiểm toán độc lập định kỳ xem xét, đánh giá dữ liệu [[src-tt14-2025-nhnn#^d72-1]].
- Dữ liệu phải liên kết với hoạt động kinh doanh hiện tại, hệ thống thông tin, dữ liệu và quy trình quản lý rủi ro [[src-tt14-2025-nhnn#^d72-2]].
- Thông tin cần thu thập gồm ba ngày tham chiếu ([[operational-loss-event-dates]]), tổng giá trị tổn thất, các khoản thu hồi, và mô tả nguyên nhân cùng yếu tố tác động [[src-tt14-2025-nhnn#^d72-5]].
- Tổn thất do cùng một sự kiện, hoặc các sự kiện theo thời gian, đã hạch toán cho nhiều năm thì phân bổ theo các năm tương ứng, phù hợp với nguyên tắc kế toán [[src-tt14-2025-nhnn#^d72-7]].

**Ranh giới với rủi ro khác.** Hoạt động làm phát sinh đồng thời rủi ro tín dụng và rủi ro hoạt động: ngân hàng không phải thu thập. Hoạt động làm phát sinh đồng thời rủi ro thị trường và rủi ro hoạt động: ngân hàng phải thu thập [[src-tt14-2025-nhnn#^d72-3]].

**Mua lại, sáp nhập.** Phạm vi tổn thất phải gồm doanh nghiệp được mua lại, bị sáp nhập, bị hợp nhất, kể cả thời gian trước đó [[src-tt14-2025-nhnn#^d72-8]].

## Phụ thuộc regime
Quy định có hiệu lực từ 15/09/2025, bắt buộc áp dụng từ 01/01/2030 hoặc từ thời điểm đăng ký áp dụng sớm [[src-tt14-2025-nhnn#^d7-1]] [[src-tt14-2025-nhnn#^d7-2b]]. Trước thời điểm đó, ngân hàng không đăng ký phương pháp tiêu chuẩn theo Đ7 thực hiện các thông tư cũ đến 31/12/2029 [[src-tt14-2025-nhnn#^d82-2]], nên chưa bị ràng buộc bởi chương này (cách đọc của wiki từ Đ7 và Đ82.2).

## Góc nhìn theo domain
- **VN**: TT83/2025 Đ38–44 yêu cầu quản lý rủi ro hoạt động nội bộ, trong đó có hạn mức tổn thất và báo cáo, xem [[operational-risk-management]]. TT14/2025 dùng cùng bộ dữ liệu cho mục đích vốn.
- **ALM**: *Diễn giải:* sự cố thanh toán, lỗi giao dịch trên sổ kinh doanh và tổn thất pháp lý của hoạt động Treasury đi vào bộ dữ liệu này khi vượt 12 triệu đồng và không đồng thời là rủi ro tín dụng [[src-tt14-2025-nhnn#^d71-1]] [[src-tt14-2025-nhnn#^d72-3]].

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Cách phân loại tổn thất theo nhóm sự kiện và dòng nghiệp vụ [cần nguồn]. Đ70–72 không nêu phân loại này.
- Tiêu chí phân biệt "đồng thời rủi ro tín dụng và hoạt động" trong thực tế [cần nguồn].
