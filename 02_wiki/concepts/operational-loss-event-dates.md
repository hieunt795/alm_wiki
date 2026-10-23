---
title: "Operational Loss Event Dates"
aliases: [Operational Loss Event Dates, Ngày tham chiếu của sự kiện tổn thất hoạt động, Ngày hạch toán tổn thất, Ngày xảy ra sự kiện, Ngày ghi nhận sự kiện]
type: concept
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[operational-loss-data]]", cite: "[[src-tt14-2025-nhnn#^d72-5]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Mỗi sự kiện tổn thất hoạt động có ba ngày tham chiếu. Ngân hàng dùng ngày hạch toán để xây dựng bộ dữ liệu tổn thất [[src-tt14-2025-nhnn#^d72-6]]. Ngày hạch toán cũng là cơ sở của giá trị tổn thất ròng của từng sự kiện [[src-tt14-2025-nhnn#^d71-2]]. Xem [[operational-loss-data]].

## Cơ chế & drivers
| Ngày | Định nghĩa | Nguồn |
|---|---|---|
| Ngày xảy ra sự kiện | Ngày bắt đầu diễn ra | [[src-tt14-2025-nhnn#^d72-5]] |
| Ngày ghi nhận sự kiện | Ngày ngân hàng nhận biết về sự kiện | [[src-tt14-2025-nhnn#^d72-5]] |
| Ngày hạch toán | Ngày hoặc các ngày xảy ra sự kiện tổn thất dẫn đến tổn thất được ghi nhận trong các khoản mục lãi, lỗ; với tổn thất chờ xử lý là ngày ghi vào tài khoản chờ xử lý | [[src-tt14-2025-nhnn#^d72-5]] |

**Quy tắc sử dụng:**
- Ngân hàng dùng ngày hạch toán để xây dựng bộ dữ liệu tổn thất [[src-tt14-2025-nhnn#^d72-6]].
- Với tổn thất phát sinh từ sự kiện pháp lý, ngân hàng phải dùng ngày chậm nhất là ngày hạch toán để ghi nhận [[src-tt14-2025-nhnn#^d72-6]].
- Tổn thất của cùng một sự kiện đã hạch toán cho nhiều năm được phân bổ theo các năm tương ứng [[src-tt14-2025-nhnn#^d72-7]].

*Diễn giải:* khoảng cách giữa ngày xảy ra, ngày ghi nhận và ngày hạch toán quyết định tổn thất rơi vào năm nào của [[loss-component]]. Một sự kiện bắt đầu năm N nhưng hạch toán năm N+1 thuộc dữ liệu của năm N+1. Tổn thất thời gian (sự kiện chưa ghi nhận hơn 01 năm và làm phát sinh rủi ro pháp lý) là loại tổn thất tính vào tổng mức [[src-tt14-2025-nhnn#^d71-3]].

## Phụ thuộc regime
Bắt buộc từ 01/01/2030 hoặc từ thời điểm đăng ký áp dụng sớm [[src-tt14-2025-nhnn#^d7-1]] [[src-tt14-2025-nhnn#^d7-2b]].

## Góc nhìn theo domain
- **VN**: Đ72.5–6 TT14/2025 quy định ba ngày và ngày dùng để xây bộ dữ liệu [[src-tt14-2025-nhnn#^d72-5]] [[src-tt14-2025-nhnn#^d72-6]].
- **Basel**: [cần nguồn] (OPE chưa ingest).

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Cách xác định "ngày chậm nhất" khi sự kiện pháp lý có nhiều khoản hạch toán [cần nguồn].
