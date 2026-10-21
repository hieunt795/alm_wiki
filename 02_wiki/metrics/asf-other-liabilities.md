---
title: "ASF Other Liabilities"
aliases: [ASF Other Liabilities, ASF nợ phải trả khác, ASF khoản mục hệ số 0%, Zero-ASF liabilities]
type: metric
domains: [vn-reg, alm, basel]
status: active
maturity: draft
valid_from: 2026-10-01
valid_to:
as_of:
sources: ["[[src-tt50-2026-nhnn]]", "[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[available-stable-funding]]", cite: "[[src-tt50-2026-nhnn#^pl2-a2-2]]"}
tags: [nsfr, asf, derivatives]
updated: 2026-10-21
reviewed:
---

## Định nghĩa
ASF Other Liabilities là nhóm nợ phải trả và vốn trong Bảng 9 PL2 TT50/2026 không thuộc nguồn huy động theo đối tác, phần lớn nhận hệ số ASF 0%. Nhóm gồm khoản 2–5 và 14 của Bảng 9 [[src-tt50-2026-nhnn#^pl2-a2-2]] [[src-tt50-2026-nhnn#^pl2-a2-11]], cùng các khoản nợ liên quan đến ký quỹ không được bù trừ theo Đ25.4.c [[src-tt50-2026-nhnn#^d25-4c]].

## Công thức

| Khoản | Phân loại | Không kỳ hạn | < 6T | 6T – < 1N | ≥ 1N | Không XĐ | Căn cứ |
|---|---|---|---|---|---|---|---|
| 2 | Nợ thuộc cặp tài sản và nợ phải trả phụ thuộc | 0% | 0% | 0% | 0% | | [[src-tt50-2026-nhnn#^pl2-a2-2]] |
| 3 | Chênh lệch dương nợ phái sinh NSFR − tài sản phái sinh NSFR | 0% | | | | | [[src-tt50-2026-nhnn#^pl2-a2-2]] |
| 4 | Trade date payables chưa thanh toán (trừ phái sinh, repo, reverse repo) | 0% | | | | | [[src-tt50-2026-nhnn#^pl2-a2-2]] |
| 5 | Thuế thu nhập hoãn lại phải trả | 0% | 0% | 50% | 100% | 0% | [[src-tt50-2026-nhnn#^pl2-a2-2]] |
| 14.1 | Nợ và vốn khác có kỳ hạn cụ thể | | 0% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-11]] |
| 14.2 | Nợ và vốn khác không xác định kỳ hạn, gồm vị thế bán, vị thế không có ngày đến hạn | | | | | 0% | [[src-tt50-2026-nhnn#^pl2-a2-11]] |
| Đ25.4.c | Nợ liên quan đến ký quỹ biến động không đủ điều kiện, ký quỹ ban đầu nhận được, ký quỹ vượt mức thoả thuận | 0% | | | | | [[src-tt50-2026-nhnn#^d25-4c]] |

**Khoản 2.** Áp cho nợ thuộc cặp đáp ứng đủ điều kiện Đ26.1 [[src-tt50-2026-nhnn#^d26-1]] [[src-tt50-2026-nhnn#^d26-1b]]. NHNN có quyền yêu cầu ngừng áp 0% và tính riêng từng vế [[src-tt50-2026-nhnn#^d26-3]]. Xem [[interdependent-assets-and-liabilities]].

**Khoản 3.** Nợ phái sinh NSFR bằng nợ phái sinh (chi phí thay thế âm, ròng khi có thoả thuận bù trừ đủ điều kiện) trừ ký quỹ biến động bằng tài sản tài chính [[src-tt50-2026-nhnn#^d25-1]] [[src-tt50-2026-nhnn#^d25-5]]. Chỉ phần chênh lệch dương so với tài sản phái sinh NSFR vào ASF, với hệ số 0% [[src-tt50-2026-nhnn#^d25-5]]. Xem [[rsf-derivatives-and-off-balance-sheet]].

**Khoản 4.** Trade date payables phải dự kiến thanh toán đúng thời hạn theo pháp luật, hoặc thanh toán không thành công nhưng vẫn dự kiến thực hiện [[src-tt50-2026-nhnn#^pl2-a2-2]].

## Diễn giải
- *Diễn giải:* hệ số 0% không làm các khoản này biến mất khỏi NSFR. Chúng vẫn được phân loại để toàn bộ nợ phải trả và vốn trên báo cáo tài chính được đưa vào Bảng 9 [[src-tt50-2026-nhnn#^pl2-a1]], nhưng không đóng góp nguồn ổn định.
- *Diễn giải:* thuế hoãn lại phải trả là khoản duy nhất trong nhóm có hệ số theo kỳ hạn (50%, 100%). Khi không xác định được kỳ hạn thì nhận 0%, khác với vốn cấp 2 và công cụ vốn khác nhận 100% ở cột không xác định kỳ hạn [[src-tt50-2026-nhnn#^pl2-a2-1]].
- *Diễn giải:* nợ phái sinh vào ASF với 0%, đồng thời RSF tính thêm 10% tổng nợ phái sinh với 100% [[src-tt50-2026-nhnn#^pl2-b2-19]]. Vị thế nợ phái sinh lớn vì vậy làm NSFR giảm, không tăng.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Nợ phái sinh ròng | 0% [[src-bcbs-nsfr#^nsf30-14]] | 0% [[src-tt50-2026-nhnn#^pl2-a2-2]] | TT50 PL2 Bảng 9 khoản 3; Đ25.5 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Trade date payables | 0% [[src-bcbs-nsfr#^nsf30-14]] | 0% [[src-tt50-2026-nhnn#^pl2-a2-2]] | TT50 PL2 Bảng 9 khoản 4 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Vị thế bán, nợ không xác định kỳ hạn | 0% [[src-bcbs-nsfr#^nsf30-14]] | 0% [[src-tt50-2026-nhnn#^pl2-a2-11]] | TT50 PL2 Bảng 9 khoản 14.2 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Cặp tài sản – nợ phụ thuộc | 0%, supervisor quyết định [[src-bcbs-nsfr#^nsf30-35]] | 0%, ngân hàng tự áp, NHNN có quyền yêu cầu ngừng [[src-tt50-2026-nhnn#^d26-1]] [[src-tt50-2026-nhnn#^d26-3]] | TT50 Đ26; PL2 Bảng 9 khoản 2 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Thuế thu nhập hoãn lại phải trả | [cần nguồn] | 0%, 0%, 50%, 100%; không xác định kỳ hạn 0% [[src-tt50-2026-nhnn#^pl2-a2-2]] | TT50 PL2 Bảng 9 khoản 5 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Ký quỹ nhận được không đủ điều kiện bù trừ | [cần nguồn] | 0%, không bù trừ với tài sản phái sinh [[src-tt50-2026-nhnn#^d25-4c]] | TT50 Đ25.4.c | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |

## Ứng dụng trong ALM
- *Diễn giải:* khi đối chiếu NSFR với báo cáo tài chính, các khoản này giải thích phần chênh giữa tổng nợ phải trả và tổng ASF. Ký quỹ ban đầu nhận được từ khách hàng phái sinh là tiền mặt trên bảng cân đối nhưng không tạo ASF [[src-tt50-2026-nhnn#^d25-4c]].

## Nhầm lẫn thường gặp
- *Diễn giải:* không phải mọi nợ "khác" đều 0%. Nợ và vốn khác có kỳ hạn cụ thể nhận 50% từ 6 tháng và 100% từ 1 năm [[src-tt50-2026-nhnn#^pl2-a2-11]].
