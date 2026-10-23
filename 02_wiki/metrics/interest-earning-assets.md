---
title: "Interest-Earning Assets"
aliases: [Interest-Earning Assets, Interest Earning Assets, Tài sản tạo lãi]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[interest-leases-and-dividend-component]]", cite: "[[src-tt14-2025-nhnn#^pl3-1-ildc]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tài sản tạo lãi là những tài sản tạo ra thu nhập lãi và các khoản thu nhập tương tự từ Báo cáo tình hình tài chính [[src-tt14-2025-nhnn#^pl3-1-eaa]]. Trong TT14/2025, tài sản tạo lãi là đại lượng đặt trần cho cấu phần lãi ([[interest-leases-and-dividend-component]]) [[src-tt14-2025-nhnn#^pl3-1-ildc]].

## Công thức
Tài sản tạo lãi là tổng sáu nhóm khoản mục [[src-tt14-2025-nhnn#^pl3-1-eaa]]:

| Nhóm | Khoản mục | Nguồn |
|---|---|---|
| 1 | Tiền gửi tại NHNN | [[src-tt14-2025-nhnn#^pl3-1-eaa]] |
| 2 | Tiền gửi và cho vay các TCTD khác | [[src-tt14-2025-nhnn#^pl3-1-eaa]] |
| 3 | Chứng khoán kinh doanh | [[src-tt14-2025-nhnn#^pl3-1-eaa]] |
| 4 | Cho vay khách hàng | [[src-tt14-2025-nhnn#^pl3-1-eaa]] |
| 5 | Hoạt động mua nợ | [[src-tt14-2025-nhnn#^pl3-1-eaa]] |
| 6 | Chứng khoán đầu tư | [[src-tt14-2025-nhnn#^pl3-1-eaa]] |

Giá trị theo năm bằng trung bình số dư tại 4 thời điểm của năm (năm 2022 gồm Q4.2021, Q1.2022, Q2.2022 và Q3.2022). Sau đó lấy trung bình 3 năm [[src-tt14-2025-nhnn#^pl3-3-ildc2]].

## Diễn giải
*Diễn giải:* khác các khoản lãi/lỗ và thu nhập được cộng dồn bốn quý, tài sản tạo lãi là số dư nên được lấy trung bình bốn thời điểm. Nguồn ghi rõ cách này ở bước 2 của ví dụ [[src-tt14-2025-nhnn#^pl3-3-ildc2]].

Wiki chỉ dùng danh sách sáu nhóm của Phụ lục III cho node này. Đối chiếu với mẫu số của [[net-interest-margin]] [cần nguồn].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Phạm vi tài sản tạo lãi | [cần nguồn] (OPE chưa ingest) | Sáu nhóm khoản mục [[src-tt14-2025-nhnn#^pl3-1-eaa]] | PL3.1 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Hệ số trần trong ILDC | [cần nguồn] | 2,25% theo công thức; ví dụ ghi "2,25 lần" (callout conflict trong [[interest-leases-and-dividend-component]]) [[src-tt14-2025-nhnn#^pl3-1-ildc]] | PL3.1, PL3.3.1 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* quy mô tài sản tạo lãi quyết định trần của ILDC. Tăng cho vay khách hàng, tiền gửi liên ngân hàng và chứng khoán làm tăng trần này; ILDC chỉ chạm trần khi lãi thuần tuyệt đối lớn so với tài sản.

## Nhầm lẫn thường gặp
- Tài sản tạo lãi tính trung bình bốn thời điểm trong năm, không cộng dồn [[src-tt14-2025-nhnn#^pl3-3-ildc2]].
- Tài sản tạo lãi ở đây chỉ phục vụ trần của ILDC; mẫu số của tỷ lệ an toàn vốn gồm RWA, $K_{OR}$ và $K_{MR}$ [[src-tt14-2025-nhnn#^d5-1d]].
