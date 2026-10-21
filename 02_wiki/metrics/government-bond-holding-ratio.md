---
title: "Government Bond Holding Ratio"
aliases: [Government Bond Holding Ratio, "Tỷ lệ mua, nắm giữ, đầu tư trái phiếu Chính phủ", Tỷ lệ nắm giữ TPCP, Government bond holding limit]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2026-10-01
valid_to:
as_of:
sources: ["[[src-tt50-2026-nhnn]]"]
relations: []
tags: [liquidity, hqla, government-bond, vn-regulation]
updated: 2026-10-21
reviewed:
---

## Định nghĩa
Government Bond Holding Ratio (tỷ lệ mua, nắm giữ, đầu tư trái phiếu Chính phủ, trái phiếu được Chính phủ bảo lãnh) là một trong các tỷ lệ bảo đảm an toàn mà ngân hàng phải thường xuyên duy trì theo TT50/2026 [[src-tt50-2026-nhnn#^d1-1]]. Tử số là [[government-bond-holdings]], mẫu số là [[average-total-liabilities]] của tháng liền kề trước. Tỷ lệ tối đa là 30% [[src-tt50-2026-nhnn#^d28-1]].

## Công thức
$$\text{Tỷ lệ TPCP} = \frac{\text{Số dư TPCP, TPCPBL}}{\text{Tổng Nợ phải trả bình quân tháng liền kề trước}} \times 100\% \le 30\%$$
[[src-tt50-2026-nhnn#^d28-1]] [[src-tt50-2026-nhnn#^d28-4]] [[src-tt50-2026-nhnn#^d3-13]]

TPCP là trái phiếu Chính phủ, TPCPBL là trái phiếu được Chính phủ bảo lãnh.

| Tham số | Giá trị | Căn cứ |
|---|---|---|
| Trần chung | 30% Tổng Nợ phải trả bình quân của tháng liền kề trước | [[src-tt50-2026-nhnn#^d28-1]] |
| Trần cho ngân hàng mới thành lập | 30% vốn điều lệ, vốn được cấp | [[src-tt50-2026-nhnn#^d28-5]] |
| Điều kiện áp trần ngân hàng mới | Hoạt động dưới 2 năm kể từ ngày khai trương; Tổng Nợ phải trả nhỏ hơn vốn điều lệ, vốn được cấp; không gồm TCTD được tổ chức lại | [[src-tt50-2026-nhnn#^d28-5]] |
| Phạm vi TPCP | Công cụ nợ của Chính phủ, kể cả tín phiếu Kho bạc, công trái xây dựng Tổ quốc | [[src-tt50-2026-nhnn#^d28-2]] |
| Phạm vi TPCPBL | Trái phiếu doanh nghiệp và trái phiếu ngân hàng chính sách được Chính phủ bảo lãnh | [[src-tt50-2026-nhnn#^d28-2]] |

## Diễn giải
- *Diễn giải:* Đ28 không nêu ngày chốt tử số hay tần suất tính. Cách đọc hợp lý là tử số lấy tại ngày tính, mẫu số cố định trong cả tháng vì là bình quân tháng trước [cần nguồn: chế độ báo cáo NHNN].
- *Diễn giải:* với ngân hàng mới, Tổng Nợ phải trả còn nhỏ hơn vốn điều lệ. Đ28.5 chuyển mẫu số sang vốn điều lệ, vốn được cấp, nên ngân hàng mới có thể đặt vốn tự có vào TPCP vượt mức 30% nợ phải trả. Điều kiện ở Đ28.5 dùng "Tổng Nợ phải trả", không có chữ "bình quân" [[src-tt50-2026-nhnn#^d28-5]].
- **Quan hệ với HQLA.** Công cụ nợ của Chính phủ VN (gồm TPCP, tín phiếu Kho bạc) và tín phiếu NHNN là tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a2-3d]] [[src-tt50-2026-nhnn#^pl1-a2-3dd]]. Trái phiếu được Chính phủ bảo lãnh thanh toán 100% gốc, lãi cũng là tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a2-3e]]. *Diễn giải:* trần 30% vì vậy là giới hạn trên cho phần [[level-1-assets]] dạng trái phiếu Chính phủ. Tiền mặt và tiền gửi NHNN không bị trần này. Đ28.2 chỉ nói công cụ nợ của Chính phủ, nên tín phiếu NHNN có thể nằm ngoài trần [cần nguồn: hướng dẫn NHNN].
- *Diễn giải:* trần thường không ràng buộc LCR. Ví dụ, Tổng Nợ phải trả bình quân 100.000 tỷ cho phép tối đa 30.000 tỷ TPCP. Nếu dòng tiền ra ròng 30 ngày là 20.000 tỷ, LCR 100% chỉ cần 20.000 tỷ HQLA. Trần chỉ ràng buộc khi dòng tiền ra ròng vượt khoảng 30% Tổng Nợ phải trả, hoặc khi ngân hàng giữ TPCP cho mục đích khác (kinh doanh, repo với NHNN).
- *Diễn giải:* tử số tính theo giá mua [[src-tt50-2026-nhnn#^d28-4]], còn HQLA dùng giá trị khác (xem [[hqla]]). Giá trái phiếu giảm không làm tỷ lệ giảm theo.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Chỉ tiêu tương ứng | Không có trần nắm giữ trái phiếu Chính phủ trong chuẩn BCBS đã ingest [cần nguồn] | Tối đa 30% Tổng Nợ phải trả bình quân tháng liền kề trước [[src-tt50-2026-nhnn#^d28-1]] | TT50 Đ28.1 | 01/10/2026 [[src-tt50-2026-nhnn#^d37-1]] |
| Ngân hàng mới thành lập | [cần nguồn] | 30% vốn điều lệ, vốn được cấp [[src-tt50-2026-nhnn#^d28-5]] | TT50 Đ28.5 | 01/10/2026 [[src-tt50-2026-nhnn#^d37-1]] |

*Diễn giải:* Basel LCR khuyến khích nắm giữ trái phiếu Chính phủ ở Level 1 không trần [[src-bcbs-lcr#^lcr30-41]]. TT50 đặt cả tài sản cấp 1 không giới hạn trong LCR [[src-tt50-2026-nhnn#^pl1-a2]] lẫn trần 30% ngoài LCR, nên tại VN hai quy định cùng tác động lên một danh mục.

## Ứng dụng trong ALM
- *Diễn giải:* ALCO theo dõi tỷ lệ này cùng [[lcr]]. Lộ trình LCR quy VNĐ tăng từ 50% (01/10/2028) lên 100% (01/10/2033) [[src-tt50-2026-nhnn#^d16-1c]], nên nhu cầu HQLA tăng dần. Ngân hàng có dòng tiền ra ròng lớn so với nợ phải trả cần dựng HQLA ngoài TPCP: tiền gửi NHNN, tín phiếu NHNN, tài sản cấp 2A.
- *Diễn giải:* mẫu số là bình quân tháng trước, nên khi bảng cân đối co lại thì trần cũng giảm theo, trễ một tháng. Ngân hàng nên đặt hạn mức nội bộ thấp hơn 30% để có vùng đệm.

## Nhầm lẫn thường gặp
- *Diễn giải:* mẫu số không phải tổng tài sản hay vốn tự có, mà là Tổng Nợ phải trả bình quân của tháng liền kề trước [[src-tt50-2026-nhnn#^d28-1]]. Chỉ ngân hàng mới thành lập đủ điều kiện mới dùng vốn điều lệ [[src-tt50-2026-nhnn#^d28-5]].
- *Diễn giải:* trái phiếu nhận làm tài sản bảo đảm hay chiết khấu không vào tử số, nhưng trái phiếu uỷ thác cho bên khác mua thì vào tử số [[src-tt50-2026-nhnn#^d28-4]].
