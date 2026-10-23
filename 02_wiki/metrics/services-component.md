---
title: "Services Component"
aliases: [Services Component, SC, Cấu phần dịch vụ]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[business-indicator]]", cite: "[[src-tt14-2025-nhnn#^d70-2b]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Cấu phần dịch vụ (SC) là cấu phần thứ hai của [[business-indicator]] [[src-tt14-2025-nhnn#^d70-2b]]. SC bằng giá trị lớn hơn giữa thu nhập và chi phí hoạt động dịch vụ, cộng giá trị lớn hơn giữa thu nhập và chi phí hoạt động khác [[src-tt14-2025-nhnn#^pl3-1-sc]].

## Công thức
$$
SC = \max(TNDV;\ CPDV) + \max(TNK;\ CPK)
$$
[[src-tt14-2025-nhnn#^pl3-1-sc]]

| Ký hiệu | Khoản mục trong Phụ lục III | Nguồn |
|---|---|---|
| TNDV | Thu nhập từ hoạt động dịch vụ | [[src-tt14-2025-nhnn#^pl3-1-sc]] |
| CPDV | Chi phí hoạt động dịch vụ | [[src-tt14-2025-nhnn#^pl3-1-sc]] |
| TNK | Thu nhập từ hoạt động khác | [[src-tt14-2025-nhnn#^pl3-1-sc]] |
| CPK | Chi phí hoạt động khác | [[src-tt14-2025-nhnn#^pl3-1-sc]] |

Ký hiệu TNDV, CPDV, TNK, CPK là ký hiệu của wiki; nguồn viết tên khoản mục bằng chữ [[src-tt14-2025-nhnn#^pl3-1-sc]].

## Diễn giải
**Cách tính theo ví dụ của nguồn (tại 31/10/2024).**
- Thu nhập từ hoạt động dịch vụ theo năm bằng cách cộng dồn số dư cuối kỳ của 4 quý liên tiếp (năm 2022 gồm Q4.2021, Q1.2022, Q2.2022 và Q3.2022), rồi lấy trung bình 3 năm [[src-tt14-2025-nhnn#^pl3-3-sc]].
- Chi phí hoạt động dịch vụ xác định tương tự. Sau đó lấy giá trị lớn hơn giữa hai trung bình 3 năm [[src-tt14-2025-nhnn#^pl3-3-sc]].
- Cặp thu nhập và chi phí hoạt động khác xác định tương tự cặp hoạt động dịch vụ [[src-tt14-2025-nhnn#^pl3-3-sc]].

*Diễn giải:* khác ILDC và FC, SC không lấy giá trị tuyệt đối. SC lấy giá trị lớn hơn của thu nhập và chi phí trong từng cặp, nên một cặp có chi phí lớn hơn thu nhập vẫn đóng góp bằng chi phí vào SC. Điều này đúng theo công thức max của Bảng 24 [[src-tt14-2025-nhnn#^pl3-1-sc]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức SC | [cần nguồn] (OPE chưa ingest) | max(thu nhập dịch vụ; chi phí dịch vụ) + max(thu nhập khác; chi phí khác) [[src-tt14-2025-nhnn#^pl3-1-sc]] | PL3.1 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Cách lấy trung bình | [cần nguồn] | Trung bình 03 năm; năm bằng tổng 4 quý liên tiếp [[src-tt14-2025-nhnn#^pl3-1-avg]] [[src-tt14-2025-nhnn#^pl3-3-sc]] | PL3.1, PL3.3.1 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* SC phụ thuộc thu nhập phí và chi phí hoạt động, không phụ thuộc cấu trúc kỳ hạn của bảng cân đối. ALM thường không điều khiển trực tiếp cấu phần này; tác động tới vốn qua [[operational-risk-capital-requirement]].

## Nhầm lẫn thường gặp
- Khoản mục kinh doanh bảo hiểm, phí bảo hiểm đã trả và thu hồi chi phí vận hành không tính vào SC hay bất cứ cấu phần nào của BI [[src-tt14-2025-nhnn#^pl3-2]].
- SC không lấy giá trị tuyệt đối, trái với ILDC và FC [[src-tt14-2025-nhnn#^pl3-1-sc]].
