---
title: "ASF Public Sector and Central Bank Funding"
aliases: [ASF Public Sector and Central Bank Funding, ASF nguồn vốn Chính phủ và NHNN, ASF tiền gửi Kho bạc Nhà nước, Sovereign and central bank funding in NSFR]
type: metric
domains: [vn-reg, alm, basel]
status: active
maturity: draft
valid_from: 2026-10-01
valid_to:
as_of:
sources: ["[[src-tt50-2026-nhnn]]", "[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[available-stable-funding]]", cite: "[[src-tt50-2026-nhnn#^pl2-a2-6]]"}
tags: [nsfr, asf, public-sector, central-bank]
updated: 2026-10-21
reviewed:
---

## Định nghĩa
ASF Public Sector and Central Bank Funding là phần [[available-stable-funding]] đến từ hai nhóm đối tác trong Bảng 9 PL2 TT50/2026 [[src-tt50-2026-nhnn#^pl2-a2-6]]:
- khoản 7: Chính phủ, Chính phủ nước ngoài, PSE nước ngoài, tổ chức tài chính quốc tế, Kho bạc Nhà nước, UBND cấp tỉnh, Bảo hiểm tiền gửi Việt Nam, Bảo hiểm xã hội Việt Nam;
- khoản 8: NHNN và NHTW nước ngoài.

Nguồn huy động được phân loại theo thứ tự từ trên xuống trong Bảng 9 [[src-tt50-2026-nhnn#^pl2-a2]].

## Công thức
$$\text{ASF}_{\text{công}} = \sum_{i} \text{Số dư}_i \times \text{Hệ số ASF}_i$$
[[src-tt50-2026-nhnn#^d23-1]]

| Khoản | Phân loại | Không kỳ hạn | < 6T | 6T – < 1N | ≥ 1N | Căn cứ |
|---|---|---|---|---|---|---|
| 7.1 | Chính phủ, KBNN…: tiền gửi hoạt động | 50% | 50% | 50% | 100% | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 7.2 | Chính phủ, KBNN…: tiền gửi không phải tiền gửi hoạt động | 50% | 50% | 50% | 100% | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 7.3 | Chính phủ, KBNN…: nguồn huy động khác | | 50% | 50% | 100% | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 8.1 | NHNN, NHTW nước ngoài: tiền gửi hoạt động | 50% | 50% | 50% | 100% | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 8.2 | NHNN, NHTW nước ngoài: tiền gửi không phải tiền gửi hoạt động | 0% | 0% | 50% | 100% | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 8.3 | NHNN, NHTW nước ngoài: nguồn huy động khác | | 0% | 50% | 100% | [[src-tt50-2026-nhnn#^pl2-a2-6]] |

Tiền gửi hoạt động xác định theo khoản 2.3 Mục III Phần B PL I [[src-tt50-2026-nhnn#^pl2-a2-6]]. Kỳ hạn tính tới thời điểm sớm nhất phải thực hiện nghĩa vụ [[src-tt50-2026-nhnn#^d23-1]].

## Diễn giải
- *Diễn giải:* hai nhóm khác nhau ở phần không phải tiền gửi hoạt động dưới 6 tháng. Tiền gửi của Chính phủ, KBNN nhận 50%, còn tiền gửi và vốn vay từ NHNN nhận 0%. Vay NHNN ngắn hạn (OMO, tái cấp vốn dưới 6 tháng) vì vậy không tạo ASF.
- *Diễn giải:* tiền gửi KBNN không kỳ hạn nhận 50% ASF. Trong LDR, tiền gửi không kỳ hạn của KBNN bị loại khỏi D và 80% tiền gửi có kỳ hạn của KBNN bị loại [[src-tt50-2026-nhnn#^d12-4a]] (xem [[ldr-total-deposits]]). Cùng một khoản tiền gửi KBNN được xử lý khác nhau giữa NSFR và LDR.
- *Diễn giải:* nguồn từ 6 tháng tới dưới 1 năm nhận 50% ở cả hai nhóm, và từ 1 năm nhận 100%. Vay NHNN kỳ hạn dài vẫn là nguồn ổn định đầy đủ.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Chính phủ, PSE, MDB dưới 1 năm | 50% [[src-bcbs-nsfr#^nsf30-13]] | 50%, kể cả không kỳ hạn; thêm KBNN, UBND cấp tỉnh, BHTG, BHXH, tổ chức tài chính quốc tế [[src-tt50-2026-nhnn#^pl2-a2-6]] | TT50 PL2 Bảng 9 khoản 7 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| NHTW dưới 6 tháng | 0% [[src-bcbs-nsfr#^nsf30-14]] | 0%, trừ tiền gửi hoạt động 50% [[src-tt50-2026-nhnn#^pl2-a2-6]] | TT50 PL2 Bảng 9 khoản 8 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| NHTW 6 tháng – dưới 1 năm | 50% [[src-bcbs-nsfr#^nsf30-13]] | 50% [[src-tt50-2026-nhnn#^pl2-a2-6]] | TT50 PL2 Bảng 9 khoản 8 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Từ 1 năm | 100% [[src-bcbs-nsfr#^nsf30-10]] | 100% [[src-tt50-2026-nhnn#^pl2-a2-6]] | TT50 PL2 Bảng 9 khoản 7–8 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Tiền gửi hoạt động | 50% [[src-bcbs-nsfr#^nsf30-13]] | 50% dưới 1 năm, cả với NHNN [[src-tt50-2026-nhnn#^pl2-a2-6]] | TT50 PL2 Bảng 9 khoản 7.1, 8.1 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |

*Diễn giải:* TT50 liệt kê đích danh các đối tác khu vực công VN (KBNN, UBND cấp tỉnh, BHTG, BHXH) thay cho khái niệm PSE chung của Basel.

## Ứng dụng trong ALM
- *Diễn giải:* tăng tiền gửi KBNN, BHXH có kỳ hạn từ 1 năm nâng ASF ở hệ số 100%. Tiền gửi các nhóm này dưới 1 năm chỉ nhận 50%, ngang doanh nghiệp phi tài chính (xem [[asf-wholesale-and-operational-funding]]).
- *Diễn giải:* ALCO nên tách vay NHNN theo kỳ hạn còn lại: phần dưới 6 tháng không đóng góp vào NSFR.

## Nhầm lẫn thường gặp
- *Diễn giải:* tiền gửi của NHNN không phải tiền gửi hoạt động nhận 0% ở cột không kỳ hạn và dưới 6 tháng, khác với Chính phủ, KBNN nhận 50% [[src-tt50-2026-nhnn#^pl2-a2-6]].
