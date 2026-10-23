---
title: "IRB Parameter Estimation Requirements"
aliases: [IRB Parameter Estimation Requirements, Yêu cầu ước tính tham số rủi ro IRB, Biên độ thận trọng, Margin of conservatism]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[internal-ratings-based-approach]]", cite: "[[src-tt14-2025-nhnn#^d68-1]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ68 TT14/2025 đặt yêu cầu chung và yêu cầu riêng khi ước tính [[probability-of-default]] (doanh nghiệp, bán lẻ), [[loss-given-default]] và [[exposure-at-default]]: dựa trên dữ liệu lịch sử, có biên độ thận trọng, dữ liệu tối thiểu 05 năm liên tục cho PD [[src-tt14-2025-nhnn#^d68-1]] [[src-tt14-2025-nhnn#^d68-2]] [[src-tt14-2025-nhnn#^d68-3]]. Yêu cầu riêng cho LGD, EAD bán lẻ nằm ở [[irb-retail-parameter-estimation]].

## Cơ chế & drivers
**Yêu cầu chung (Đ68.1)** [[src-tt14-2025-nhnn#^d68-1]]
- PD cho từng hạng khách hàng (doanh nghiệp) và nhóm khoản phải đòi (bán lẻ), dựa trên tỷ lệ vỡ nợ trung bình 01 năm trong lịch sử đã quan sát.
- Dựa trên dữ liệu lịch sử và kinh nghiệm quá khứ, không chỉ dựa vào ý kiến chuyên gia; xét thay đổi thực tiễn cấp tín dụng và thu hồi nợ trong thời gian quan sát; phản ánh kịp thời dữ liệu mới; rà soát tối thiểu hằng năm.
- Nguồn dữ liệu: nội bộ, bên ngoài, theo nhóm khách hàng (pooled), kết hợp thì dùng mọi nguồn quan trọng và đại diện cho dài hạn; danh mục trong dữ liệu và tiêu chuẩn cấp tín dụng phải tương đương danh mục thực tế; mẫu đủ lớn, qua kiểm định ngoài mẫu.
- Biên độ thận trọng (margin of conservatism) cho sai sót ước tính PD, LGD, EAD, lớn hơn khi phương pháp hoặc dữ liệu chưa đạt.
- LGD dùng tổn thất kinh tế, gồm chi phí trực tiếp và gián tiếp của việc thu hồi.

**PD doanh nghiệp (Đ68.2)** [[src-tt14-2025-nhnn#^d68-2]]
- PD trung bình mỗi hạng là số liệu bình quân dài hạn của tỷ lệ vỡ nợ thực tế trong 01 năm của khách hàng trong hạng.
- Ba cách, dùng riêng hoặc kết hợp: dữ liệu vỡ nợ nội bộ (biên độ thận trọng cao hơn khi thiếu thông tin hoặc chính sách phê duyệt thay đổi; được dùng dữ liệu ngân hàng khác nếu hệ thống tương đồng); so sánh với xếp hạng của doanh nghiệp xếp hạng tín nhiệm độc lập hoặc Trung tâm thông tin tín dụng quốc gia Việt Nam (so tiêu chí, điều chỉnh khi định nghĩa vỡ nợ khác, [[customer-default-definition]]); mô hình thống kê.
- Được dùng đánh giá chủ quan bổ trợ. Dữ liệu mỗi nguồn tối thiểu 05 năm liên tục; có nguồn dài hơn thì phải dùng; kết hợp năm thuận lợi và khó khăn.

**PD bán lẻ (Đ68.3)** [[src-tt14-2025-nhnn#^d68-3]]
- Dữ liệu nội bộ là nguồn chính; dùng dữ liệu bên ngoài hoặc mô hình thống kê khi quy trình phân nhóm và hồ sơ rủi ro tương đồng.
- PD trung bình dài hạn ước tính từ tỷ lệ tổn thất dài hạn dự kiến chia cho LGD trung bình dài hạn theo trọng số vỡ nợ, hoặc phương pháp nội bộ khác. Dữ liệu tối thiểu 05 năm liên tục, có cả năm thuận lợi và khó khăn.

## Phụ thuộc regime
Sàn PD (0,05% doanh nghiệp; 0,1% và 0,05% bán lẻ) nằm ở Đ42 và Đ50, xem [[probability-of-default]].

## Góc nhìn theo domain
**VN Regulator.** Nguồn so sánh bên ngoài được nêu rõ gồm doanh nghiệp xếp hạng tín nhiệm độc lập và Trung tâm thông tin tín dụng quốc gia Việt Nam [[src-tt14-2025-nhnn#^d68-2]].

**Basel.** [cần nguồn] (CRE36 chưa ingest).

**ALM.** *Diễn giải:* 05 năm liên tục có cả năm thuận lợi và khó khăn khiến dữ liệu vỡ nợ lịch sử của ngân hàng mới triển khai khó đủ; ngân hàng cần dữ liệu từ giai đoạn trước khi nộp hồ sơ ([[irb-approval-process]]).

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Ngưỡng định lượng của "biên độ thận trọng lớn hơn": nguồn không nêu.
