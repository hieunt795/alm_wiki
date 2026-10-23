---
title: "Loss Component"
aliases: [Loss Component, LC, Cấu phần tổn thất]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[internal-loss-multiplier]]", cite: "[[src-tt14-2025-nhnn#^d70-3a]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Cấu phần tổn thất (Loss component, LC) là đầu vào của [[internal-loss-multiplier]] [[src-tt14-2025-nhnn#^d70-3a]]. LC bằng 15 lần giá trị tổn thất hoạt động ròng trung bình năm của khung thời gian tính [[src-tt14-2025-nhnn#^d70-3c5]].

## Công thức
$$
LC = 15 \times \overline{L}
$$
[[src-tt14-2025-nhnn#^d70-3c5]]

Trong đó $\overline{L}$ là tổn thất hoạt động ròng trung bình năm của khung thời gian tính, ký hiệu của wiki; nguồn không đặt ký hiệu riêng cho đại lượng này [[src-tt14-2025-nhnn#^d70-3c5]].

**Các bước xác định** [[src-tt14-2025-nhnn#^d70-3c5]]:
1. Tổn thất hoạt động ròng theo quý bằng tổn thất hoạt động ghi nhận trong quý trừ giá trị thu hồi được ghi nhận trong cùng quý.
2. Tổn thất hoạt động ròng theo năm bằng tổng tổn thất ròng theo quý của 04 quý liên tiếp.
3. Tổn thất hoạt động ròng trung bình năm bằng tổng tổn thất ròng theo năm của các năm trong khung thời gian tính chia cho tổng số năm tính.
4. LC bằng 15 lần giá trị ở bước 3.

## Diễn giải
**Khung thời gian tính** [[src-tt14-2025-nhnn#^d70-3c2]]:

| Độ dài chuỗi dữ liệu tổn thất | Khung thời gian tính |
|---|---|
| Từ 10 năm trở lên | 10 năm trở lại đây |
| Từ 05 đến dưới 10 năm | Độ dài thực của dữ liệu; phần dư từ 06 tháng trở lên làm tròn thành 01 năm |

**Ví dụ của Phụ lục III tại tháng 10/2024: khung thời gian theo số quý liên tiếp** [[src-tt14-2025-nhnn#^pl3-lc-2]]:

| Độ dài dữ liệu | Quý đầu tiên | Khung thời gian tính |
|---|---|---|
| Từ 38 quý liên tiếp trở lên | Trước Q2.2015 | 10 năm |
| Từ 20 đến 37 quý liên tiếp | Từ Q3.2015 đến Q4.2019 | Từ 05 năm đến dưới 10 năm |
| Dưới 20 quý liên tiếp | Từ sau Q1.2020 | Chưa đủ 05 năm (ILM bằng 1) |

Dòng cuối: chuỗi chưa đủ 05 năm là điều kiện để ILM bằng 1 [[src-tt14-2025-nhnn#^d70-3b]].

**Khung 10 năm.** Tổn thất ròng năm 2015 (X1) bằng tổng bốn quý Q4.2014, Q1.2015, Q2.2015, Q3.2015; tương tự cho X2 (2016) đến X10 (2024). LC bằng tổng X1 đến X10 chia 10, nhân 15 [[src-tt14-2025-nhnn#^pl3-lc-3]].

**Khung từ 05 đến dưới 10 năm.** LC bằng tổng tổn thất ròng theo năm của n năm chia n, nhân 15. n bằng số quý thực tế chia 4; phần thập phân từ 0,5 trở lên được làm tròn thành 1 [[src-tt14-2025-nhnn#^pl3-lc-n]].

*Diễn giải:* 38 quý bằng 9,5 năm, làm tròn thành 10 năm theo quy tắc 0,5. Vì vậy ngưỡng 38 quý của ví dụ nhất quán với quy tắc "phần dư từ 06 tháng làm tròn thành 01 năm" của Đ70.3c(ii) [[src-tt14-2025-nhnn#^d70-3c2]]. Phép kiểm này là của wiki; nguồn không giải thích ngưỡng 38 quý.

**Điều kiện.** Ngân hàng chỉ tính LC khi không thuộc hai trường hợp ILM bằng 1 [[src-tt14-2025-nhnn#^d70-3c]], và dữ liệu tổn thất phải đáp ứng Đ71–72 ([[operational-loss-data]]). Ngân hàng thương mại có công ty con dùng LC tính trên dữ liệu riêng lẻ khi tính tỷ lệ hợp nhất [[src-tt14-2025-nhnn#^d70-3c4]].

*Diễn giải:* LC dùng tổn thất ròng sau thu hồi, cộng bốn quý liên tiếp thành năm. Đây là số liệu theo ngày hạch toán ([[operational-loss-event-dates]]). Ví dụ số do wiki dựng: nếu tổn thất ròng trung bình năm là 100 tỷ đồng thì LC là 1.500 tỷ đồng; so với BIC 3.042 tỷ đồng (ví dụ của [[business-indicator-component]]) thì LC/BIC khoảng 0,49 và ILM nhỏ hơn 1. Nguồn không đưa ví dụ số cho LC.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Hệ số nhân tổn thất trung bình năm | [cần nguồn] (OPE chưa ingest) | 15 lần [[src-tt14-2025-nhnn#^d70-3c5]] | Đ70.3c(v) | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Khung thời gian tối đa | [cần nguồn] | 10 năm [[src-tt14-2025-nhnn#^d70-3c2]] | Đ70.3c(ii) | Như trên |
| Ngưỡng theo số quý | [cần nguồn] | 38 quý (10 năm); 20–37 quý (05 đến dưới 10 năm); dưới 20 quý (chưa đủ 05 năm) [[src-tt14-2025-nhnn#^pl3-lc-2]] | PL3.3.2 | Như trên |
| Độ dài chuỗi tối thiểu | [cần nguồn] | 05 năm [[src-tt14-2025-nhnn#^d70-3b]] | Đ70.3b(ii) | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* tổn thất hoạt động từ nghiệp vụ thị trường được thu thập dù đồng thời là rủi ro thị trường, còn tổn thất đồng thời là rủi ro tín dụng thì không phải thu thập [[src-tt14-2025-nhnn#^d72-3]]. Treasury cần biết ranh giới này khi ghi nhận sự cố giao dịch vào bộ dữ liệu.

## Nhầm lẫn thường gặp
- LC dựa trên tổn thất ròng sau thu hồi, không phải tổn thất gộp [[src-tt14-2025-nhnn#^d70-3c5]].
- LC là 15 lần trung bình năm, không phải tổng tổn thất của khung thời gian [[src-tt14-2025-nhnn#^d70-3c5]].
