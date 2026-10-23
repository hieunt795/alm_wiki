---
title: "Interest, Leases and Dividend Component"
aliases: [Interest Leases and Dividend Component, ILDC, Cấu phần lãi]
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
Cấu phần lãi (ILDC) là cấu phần thứ nhất của [[business-indicator]] [[src-tt14-2025-nhnn#^d70-2b]]. ILDC bằng giá trị nhỏ hơn giữa giá trị tuyệt đối của chênh lệch thu nhập lãi trừ chi phí lãi và một trần theo tài sản tạo lãi, cộng thu nhập từ góp vốn, mua cổ phần [[src-tt14-2025-nhnn#^pl3-1-ildc]].

## Công thức
$$
ILDC = \min\left( \left| TNL - CPL \right|;\ 2{,}25\% \times TSTL \right) + TNGV
$$
[[src-tt14-2025-nhnn#^pl3-1-ildc]]

| Ký hiệu | Khoản mục trong Phụ lục III | Nguồn |
|---|---|---|
| TNL | Thu nhập lãi và các khoản thu nhập tương tự | [[src-tt14-2025-nhnn#^pl3-1-ildc]] |
| CPL | Chi phí lãi và các chi phí tương tự | [[src-tt14-2025-nhnn#^pl3-1-ildc]] |
| TSTL | Tài sản tạo lãi ([[interest-earning-assets]]) | [[src-tt14-2025-nhnn#^pl3-1-eaa]] |
| TNGV | Thu nhập từ góp vốn, mua cổ phần | [[src-tt14-2025-nhnn#^pl3-1-ildc]] |

Ký hiệu TNL, CPL, TSTL, TNGV là ký hiệu của wiki; nguồn viết tên khoản mục bằng chữ [[src-tt14-2025-nhnn#^pl3-1-ildc]].

> [!conflict] Hệ số của trần tài sản tạo lãi: 2,25% hay 2,25 lần
> - Công thức (Bảng 24) ghi 2,25% × tài sản tạo lãi [[src-tt14-2025-nhnn#^pl3-1-ildc]].
> - Ví dụ ở PL3.3.1, bước 3, ghi "2,25 lần giá trị trung bình 3 năm của Tài sản tạo lãi" [[src-tt14-2025-nhnn#^pl3-3-ildc3]].
> - Hai câu cùng một văn bản khác nhau 100 lần. Wiki dùng 2,25% trong công thức trên vì đây là bảng công thức, và đánh dấu chưa kết luận. Cần đối chiếu pdf hoặc docx gốc.

## Diễn giải
**Cách tính từng thành phần theo ví dụ của nguồn (tại 31/10/2024).**
- Giá trị tuyệt đối của (thu nhập lãi trừ chi phí lãi) theo năm bằng tổng giá trị tuyệt đối theo quý của 4 quý liên tiếp, ví dụ năm 2022 gồm Q4.2021, Q1.2022, Q2.2022 và Q3.2022. Sau đó lấy trung bình 3 năm [[src-tt14-2025-nhnn#^pl3-3-ildc1]].
- Tài sản tạo lãi theo năm bằng trung bình số dư tại bốn thời điểm của năm đó. Sau đó lấy trung bình 3 năm [[src-tt14-2025-nhnn#^pl3-3-ildc2]].
- Thu nhập từ góp vốn, mua cổ phần tính trung bình 3 năm bằng phương pháp tương tự cách tính của giá trị tuyệt đối (thu nhập lãi trừ chi phí lãi) [[src-tt14-2025-nhnn#^pl3-3-div]].
- So sánh và chọn giá trị nhỏ hơn giữa hai thành phần đầu, rồi cộng thu nhập từ góp vốn [[src-tt14-2025-nhnn#^pl3-3-ildc3]].

*Diễn giải:* ví dụ lấy giá trị tuyệt đối theo từng quý rồi cộng dồn thành năm. Cách này khác lấy giá trị tuyệt đối của chênh lệch cả năm: một quý chênh lệch âm vẫn cộng dương vào tổng năm. Nguồn viết rõ "giá trị tuyệt đối theo quý" ở bước 1, nên wiki ghi như vậy [[src-tt14-2025-nhnn#^pl3-3-ildc1]].

*Diễn giải:* tên tiếng Anh có "leases" (thuê), nhưng Bảng 24 chỉ liệt kê thu nhập lãi, chi phí lãi, tài sản tạo lãi và thu nhập từ góp vốn; không có khoản mục thuê [[src-tt14-2025-nhnn#^pl3-1-ildc]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức ILDC | [cần nguồn] (OPE chưa ingest) | min(\|TNL − CPL\|; 2,25% × TSTL) + TNGV [[src-tt14-2025-nhnn#^pl3-1-ildc]] | PL3.1 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Hệ số trần | [cần nguồn] | 2,25% theo công thức; ví dụ ghi "2,25 lần" (xem callout conflict) [[src-tt14-2025-nhnn#^pl3-1-ildc]] [[src-tt14-2025-nhnn#^pl3-3-ildc3]] | PL3.1, PL3.3.1 | Như trên |
| Cách lấy trung bình | [cần nguồn] | Trung bình 03 năm [[src-tt14-2025-nhnn#^pl3-1-avg]] | PL3.1 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* ILDC chịu ảnh hưởng của chênh lệch thu nhập lãi và chi phí lãi, nên liên quan trực tiếp tới biên lãi và cấu trúc bảng cân đối mà ALM quản lý (xem [[net-interest-margin]]). Trần theo tài sản tạo lãi giới hạn ILDC khi chênh lệch lãi lớn so với quy mô tài sản.

## Nhầm lẫn thường gặp
- Lãi thuần trong ILDC lấy giá trị tuyệt đối, nên ngân hàng có lãi thuần âm vẫn có ILDC dương [[src-tt14-2025-nhnn#^pl3-1-ildc]].
- Thu nhập từ góp vốn, mua cổ phần được cộng ngoài min, không bị trần theo tài sản tạo lãi [[src-tt14-2025-nhnn#^pl3-1-ildc]].
