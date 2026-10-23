---
title: "Financial Component"
aliases: [Financial Component, FC, Cấu phần tài chính]
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
Cấu phần tài chính (FC) là cấu phần thứ ba của [[business-indicator]] [[src-tt14-2025-nhnn#^d70-2b]]. FC bằng tổng ba giá trị tuyệt đối: lãi/lỗ thuần từ hoạt động kinh doanh ngoại hối (gồm vàng tiêu chuẩn), lãi/lỗ thuần từ mua bán chứng khoán kinh doanh, và lãi/lỗ thuần từ mua bán chứng khoán đầu tư [[src-tt14-2025-nhnn#^pl3-1-fc]].

## Công thức
$$
FC = \left| LL_{FX} \right| + \left| LL_{KD} \right| + \left| LL_{DT} \right|
$$
[[src-tt14-2025-nhnn#^pl3-1-fc]]

| Ký hiệu | Khoản mục trong Phụ lục III | Nguồn |
|---|---|---|
| $LL_{FX}$ | Lãi/lỗ thuần từ hoạt động kinh doanh ngoại hối (bao gồm cả vàng tiêu chuẩn) | [[src-tt14-2025-nhnn#^pl3-1-fc]] |
| $LL_{KD}$ | Lãi/lỗ thuần từ mua bán chứng khoán kinh doanh | [[src-tt14-2025-nhnn#^pl3-1-fc]] |
| $LL_{DT}$ | Lãi/lỗ thuần từ mua bán chứng khoán đầu tư | [[src-tt14-2025-nhnn#^pl3-1-fc]] |

Ký hiệu $LL_{FX}$, $LL_{KD}$, $LL_{DT}$ là ký hiệu của wiki; nguồn viết tên khoản mục bằng chữ [[src-tt14-2025-nhnn#^pl3-1-fc]].

## Diễn giải
**Cách tính theo ví dụ của nguồn (tại 31/10/2024).** Giá trị tuyệt đối theo năm của lãi/lỗ thuần ngoại hối bằng tổng giá trị tuyệt đối theo quý của 4 quý liên tiếp (năm 2022 gồm Q4.2021, Q1.2022, Q2.2022 và Q3.2022), rồi lấy trung bình 3 năm. Hai thành phần chứng khoán kinh doanh và chứng khoán đầu tư dùng phương pháp tương tự [[src-tt14-2025-nhnn#^pl3-3-fc]].

*Diễn giải:* FC lấy giá trị tuyệt đối nên lãi và lỗ cùng làm FC tăng. Vì giá trị tuyệt đối lấy theo quý rồi cộng dồn, một quý lãi và một quý lỗ cùng độ lớn không triệt tiêu nhau.

*Diễn giải:* FC gồm các khoản từ sổ kinh doanh (chứng khoán kinh doanh, ngoại hối) và chứng khoán đầu tư. Đây là kết quả hoạt động Treasury; phân loại hai sổ xem [[banking-book]]. Vốn rủi ro thị trường ([[market-risk-capital-requirement]]) tính trên vị thế sổ kinh doanh, còn FC đi vào $K_{OR}$ qua BI; hai khoản vốn dựa trên hai cơ sở khác nhau và cùng nằm trong mẫu số CAR [[src-tt14-2025-nhnn#^d5-1d]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức FC | [cần nguồn] (OPE chưa ingest) | Tổng ba giá trị tuyệt đối [[src-tt14-2025-nhnn#^pl3-1-fc]] | PL3.1 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Cách lấy trung bình | [cần nguồn] | Trung bình 03 năm; giá trị tuyệt đối theo quý, cộng dồn 4 quý liên tiếp [[src-tt14-2025-nhnn#^pl3-1-avg]] [[src-tt14-2025-nhnn#^pl3-3-fc]] | PL3.1, PL3.3.1 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* kết quả giao dịch ngoại hối, vàng và chứng khoán của Treasury đi vào BI bằng giá trị tuyệt đối. Biến động lớn của các khoản này làm tăng BI và BIC dù ngân hàng lãi hay lỗ. Xem [[operational-risk-capital-requirement]].

## Nhầm lẫn thường gặp
- FC không phải lợi nhuận ròng của hoạt động tài chính: ba khoản đều lấy giá trị tuyệt đối trước khi cộng [[src-tt14-2025-nhnn#^pl3-1-fc]].
- FC không phải vốn yêu cầu cho rủi ro thị trường. $K_{MR}$ tính theo Chương V và Phụ lục IV ([[market-risk-capital-requirement]]).
